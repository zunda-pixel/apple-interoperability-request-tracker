#!/usr/bin/env python3
"""Fetch Apple's DMA 6.7 Interoperability Request tracker PDF and split it
into one Markdown file per request, plus a top-level index.

Usage:
    python scripts/update_tracker.py
    python scripts/update_tracker.py --source path/to/local.pdf
    python scripts/update_tracker.py --source https://.../tracker.pdf --out requests
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import fitz  # PyMuPDF

DEFAULT_PDF_URL = "https://developer.apple.com/file/?file=interoperability-request-tracker&format=pdf"
OFFICIAL_REQUEST_URL_BASE = "https://developer.apple.com/eu-interoperability-request/"
DEFAULT_OUT_DIR = "requests"
DEFAULT_INDEX = "index.md"
COOKIE_ENV = "APPLE_DEV_COOKIE"
FETCH_RETRIES = 3
FETCH_BACKOFF_SECONDS = 5
# A successful parse on the May 2026 tracker yields 95 chunks. Anything far
# below this almost certainly means the PDF format or separator changed.
MIN_EXPECTED_CHUNKS = 50
# Filenames written by this script follow this regex; rmtree refuses to
# clear an out_dir that contains anything else.
MANAGED_FILENAME_RE = re.compile(r"^\d{3}-FB\d+-.+\.md$")

FIELD_LABELS: list[tuple[str, str, str | None]] = [
    ("Name of Developer:", "Name of Developer", None),
    ("ID# of Request:", "ID# of Request", None),
    ("Date Request Received:", "Date Request Received", None),
    ("Current Status:", "Current Status", None),
    ("Request marked as Confidential", "Request marked as Confidential", None),
    ("Please provide a descriptive title for your request:", "Descriptive Title", "*"),
    ("Please provide a generic description of the request:", "Generic Description", "*"),
    ("Request Type", "Request Type", None),
    ("Please provide the iOS, iPadOS, iPhone or iPad feature name:", "Feature Name", "*"),
    ("Please provide the reason why you need Apple", "Reason for Request", "*"),
    ("Please describe the product that uses or will use the feature", "Product Description", "*"),
    ("How will your product(s) use the feature?", "How the Product Will Use the Feature", "*"),
    ("Where do you offer or will you offer the product(s)?", "Where the Product Is/Will Be Offered", "*"),
    ("Have you evaluated other frameworks or technologies", "Other Frameworks Evaluated", "*"),
    ("Confidential Treatment of Your Request", "Confidential Treatment", "*"),
    ("If you have additional information that may be useful", "Additional Information", "(such as diagrams)."),
    ("Communications with Developer:", "Communications with Developer", None),
]

INLINE_META = {
    "Name of Developer": "developer",
    "ID# of Request": "request_id",
    "Date Request Received": "date_received",
    "Current Status": "status",
}


def _fetch_url_once(url: str) -> tuple[bytes, str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (apple-interoperability-tracker bot)",
        "Accept": "application/pdf,*/*",
    }
    cookie = os.environ.get(COOKIE_ENV, "").strip()
    if cookie:
        headers["Cookie"] = cookie
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read(), resp.geturl()


def fetch_pdf_bytes(source: str) -> bytes:
    if not source.startswith(("http://", "https://")):
        return Path(source).read_bytes()

    last_err: Exception | None = None
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            data, final_url = _fetch_url_once(source)
            break
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
            if attempt == FETCH_RETRIES:
                raise
            wait = FETCH_BACKOFF_SECONDS * attempt
            print(
                f"Fetch attempt {attempt}/{FETCH_RETRIES} failed: {e}; "
                f"retrying in {wait}s",
                file=sys.stderr,
            )
            time.sleep(wait)
    else:  # pragma: no cover — exhausted without break
        raise RuntimeError(f"Exhausted retries fetching {source}") from last_err

    if not data.startswith(b"%PDF"):
        preview = data[:256].decode("utf-8", errors="replace")
        hint = ""
        if "idmsa.apple.com" in final_url or "signin" in final_url.lower():
            hint = (
                f" (redirected to sign-in: {final_url}). Set the {COOKIE_ENV} "
                "environment variable to a valid Apple Developer session cookie, "
                "or pass --source <local.pdf>."
            )
        raise RuntimeError(
            f"Source did not return a PDF{hint} First bytes: {preview!r}"
        )
    return data


def extract_text(pdf_bytes: bytes) -> str:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    try:
        return "".join(page.get_text() for page in doc)
    finally:
        doc.close()


def official_request_url(request_id: str) -> str:
    return f"{OFFICIAL_REQUEST_URL_BASE}{request_id.lower()}/"


def safe_slug(s: str, maxlen: int = 40) -> str:
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE).strip()
    s = re.sub(r"\s+", "-", s)
    return s[:maxlen].strip("-_") or "request"


def split_into_chunks(text: str) -> list[str]:
    # Drop everything up to and including the first separator (table of contents).
    m = re.search(r"^\+{5,}\s*$", text, flags=re.MULTILINE)
    if m:
        text = text[m.end():]
    chunks = re.split(r"^\+{5,}\s*$", text, flags=re.MULTILINE)
    chunks = [c.strip() for c in chunks if c.strip()]
    if len(chunks) < MIN_EXPECTED_CHUNKS:
        raise RuntimeError(
            f"Parser produced only {len(chunks)} chunks (expected ≥ "
            f"{MIN_EXPECTED_CHUNKS}). The PDF separator format may have changed; "
            "refusing to publish a degraded output."
        )
    return chunks


def clean_lines(chunk: str) -> list[str]:
    """Drop standalone page-number lines and trailing whitespace."""
    out: list[str] = []
    for ln in chunk.split("\n"):
        ln = ln.rstrip()
        if re.fullmatch(r"\s*\d{1,3}\s*", ln):
            continue
        out.append(ln)
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out


def header_complete(line: str, end_marker: str | None) -> bool:
    s = line.rstrip()
    if end_marker is not None:
        return s.endswith(end_marker)
    return s.endswith("*") or s.endswith(":") or s.endswith("?")


def parse_request(lines: list[str]) -> tuple[dict, list[tuple[str, list[str]]]]:
    meta: dict = {}
    sections: list[tuple[str, list[str]]] = []
    current_label: str | None = None
    current_lines: list[str] = []

    def flush():
        nonlocal current_label, current_lines
        if current_label is not None:
            sections.append((current_label, current_lines))
        current_label = None
        current_lines = []

    i = 0
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()

        matched: tuple[str, str, str | None] | None = None
        for prefix, lbl, end_marker in FIELD_LABELS:
            if stripped.startswith(prefix):
                matched = (prefix, lbl, end_marker)
                break

        if matched:
            prefix, lbl, end_marker = matched

            if lbl in INLINE_META:
                val = stripped[len(prefix):].strip().lstrip(":").strip()
                meta[INLINE_META[lbl]] = val
                flush()
                i += 1
                continue

            if lbl == "Request marked as Confidential":
                meta["confidential"] = True
                flush()
                i += 1
                continue

            # Single-line headers ("Request Type", "Communications with Developer:")
            # have no continuation; the value starts on the next line.
            if lbl in ("Request Type", "Communications with Developer"):
                flush()
                current_label = lbl
                current_lines = []
                i += 1
                continue

            flush()
            current_label = lbl
            current_lines = []
            if not header_complete(stripped, end_marker):
                j = i + 1
                while j < len(lines):
                    if header_complete(lines[j].strip(), end_marker):
                        i = j
                        break
                    j += 1
                else:
                    i = len(lines) - 1
            i += 1
            continue

        if current_label is not None:
            current_lines.append(ln)
        i += 1
    flush()
    return meta, sections


def render_markdown(meta: dict, sections: list[tuple[str, list[str]]]) -> str:
    dev = meta.get("developer", "[Confidential]")
    rid = meta.get("request_id", "UNKNOWN")
    date = meta.get("date_received", "")
    status = meta.get("status", "")
    confidential = meta.get("confidential", False) or dev == "[Confidential]"

    official_url = official_request_url(rid)
    out: list[str] = [
        f"# {rid} — {dev}\n",
        "| Field | Value |",
        "| --- | --- |",
        f"| Developer | {dev} |",
        f"| Request ID | {rid} |",
        f"| Official page | [{official_url}]({official_url}) |",
        f"| Date Received | {date} |",
        f"| Current Status | {status} |",
    ]
    if confidential:
        out.append("| Confidential | Yes |")
    out.append("")

    for lbl, lines in sections:
        text = "\n".join(lines).strip()
        if not text:
            continue
        text = re.sub(r"^\*\s*", "", text, flags=re.MULTILINE)
        out.append(f"## {lbl}\n")
        out.append(text)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _safe_clear_out_dir(out_dir: Path) -> None:
    """Refuse to clear out_dir if it looks unsafe.

    We only delete the directory if every entry inside it matches the filenames
    this script writes (NNN-FBxxx-name.md). This prevents accidental loss when
    the user passes `--out .` or points at a populated directory.
    """
    resolved = out_dir.resolve()
    forbidden_roots = {Path.cwd().resolve(), Path(__file__).resolve().parent.parent.resolve()}
    if resolved == Path("/") or resolved in forbidden_roots:
        raise RuntimeError(
            f"Refusing to clear {out_dir!s}: resolves to a project/system root."
        )
    if not out_dir.exists():
        return
    for entry in out_dir.iterdir():
        if not entry.is_file() or not MANAGED_FILENAME_RE.match(entry.name):
            raise RuntimeError(
                f"Refusing to clear {out_dir!s}: contains non-managed entry "
                f"{entry.name!r}. Move or delete it manually."
            )
    shutil.rmtree(out_dir)


def write_outputs(chunks: list[str], out_dir: Path, index_path: Path) -> int:
    _safe_clear_out_dir(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    for i, chunk in enumerate(chunks, start=1):
        lines = clean_lines(chunk)
        if not lines:
            continue
        meta, sections = parse_request(lines)
        rid = meta.get("request_id", f"UNKNOWN{i:03d}")
        dev = meta.get("developer", "[Confidential]")
        slug = safe_slug(dev.replace("[", "").replace("]", ""))
        fname = f"{i:03d}-{rid}-{slug}.md"
        (out_dir / fname).write_text(render_markdown(meta, sections), encoding="utf-8")
        rows.append({
            "n": i,
            "file": fname,
            "developer": dev,
            "request_id": rid,
            "date": meta.get("date_received", ""),
            "status": meta.get("status", ""),
        })

    # Build the link prefix as out_dir relative to index.md's directory, so
    # arbitrary --out paths (including nested ones) produce working links.
    try:
        link_prefix = out_dir.resolve().relative_to(index_path.resolve().parent).as_posix()
    except ValueError:
        # out_dir is not under index_path's parent; fall back to absolute URI.
        link_prefix = out_dir.resolve().as_uri()

    index = [
        "# DMA 6.7 Interoperability Requests Received by Apple\n",
        "Source: *DMA 6.7 Interoperability Requests Received by Apple Since May 20, 2025*. "
        f"Generated from <{DEFAULT_PDF_URL}>.\n",
        "| # | Request ID | Developer | Date Received | Status | File |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        rid = r["request_id"]
        official_url = official_request_url(rid)
        index.append(
            f"| {r['n']} | [{rid}]({official_url}) | {r['developer']} | "
            f"{r['date']} | {r['status']} | "
            f"[{r['file']}]({link_prefix}/{r['file']}) |"
        )
    index_path.write_text("\n".join(index) + "\n", encoding="utf-8")
    return len(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=DEFAULT_PDF_URL,
                        help="PDF URL or local path (default: Apple's tracker URL)")
    parser.add_argument("--out", default=DEFAULT_OUT_DIR,
                        help="Directory for per-request Markdown files")
    parser.add_argument("--index", default=DEFAULT_INDEX,
                        help="Path to the index Markdown file")
    args = parser.parse_args(argv)

    print(f"Fetching: {args.source}", file=sys.stderr)
    pdf_bytes = fetch_pdf_bytes(args.source)
    print(f"PDF size: {len(pdf_bytes):,} bytes", file=sys.stderr)
    text = extract_text(pdf_bytes)
    chunks = split_into_chunks(text)
    print(f"Found {len(chunks)} request chunks", file=sys.stderr)

    n = write_outputs(chunks, Path(args.out), Path(args.index))
    print(f"Wrote {n} request files + {args.index}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
