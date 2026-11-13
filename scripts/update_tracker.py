#!/usr/bin/env python3
"""Fetch Apple's EU interoperability request list and each request's HTML page.

Usage:
    python scripts/update_tracker.py
    python scripts/update_tracker.py --source snapshot/index.html --details-dir snapshot

Offline detail files are named fbNNNN.html (lowercase request ID).
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
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup
from markdownify import markdownify

DEFAULT_SOURCE_URL = "https://developer.apple.com/eu-interoperability-request/"
OFFICIAL_REQUEST_URL_BASE = DEFAULT_SOURCE_URL
DEFAULT_OUT_DIR = "requests"
DEFAULT_INDEX = "index.md"
COOKIE_ENV = "APPLE_DEV_COOKIE"
FETCH_RETRIES = 3
FETCH_BACKOFF_SECONDS = 5
MIN_EXPECTED_REQUESTS = 50
MANAGED_FILENAME_RE = re.compile(r"^(\d{3,})-(FB\d+)-.+\.md$")


class TrackerRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Do not forward the developer session cookie to a login/other host.
        validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def validate_url(url: str) -> None:
    parts = urlsplit(url)
    if (parts.scheme != "https" or parts.netloc != "developer.apple.com"
            or not re.fullmatch(r"/eu-interoperability-request(?:/fb\d+)?/?", parts.path, re.I)
            or parts.query or parts.fragment):
        raise RuntimeError(
            "Unexpected redirect/source (possibly Apple sign-in). "
            f"Set {COOKIE_ENV} to a valid Apple Developer session cookie."
        )


def fetch_html(source: str) -> str:
    if not source.startswith(("http://", "https://")):
        return Path(source).read_text(encoding="utf-8")
    validate_url(source)
    headers = {"User-Agent": "Mozilla/5.0 (apple-interoperability-tracker bot)",
               "Accept": "text/html"}
    cookie = os.environ.get(COOKIE_ENV, "").strip()
    if cookie:
        headers["Cookie"] = cookie
    opener = urllib.request.build_opener(TrackerRedirectHandler())
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            with opener.open(urllib.request.Request(source, headers=headers), timeout=60) as resp:
                validate_url(resp.geturl())
                if resp.headers.get_content_type() != "text/html":
                    raise RuntimeError("Expected an HTML tracker page.")
                return resp.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError):
            if attempt == FETCH_RETRIES:
                raise
            print(f"Fetch attempt {attempt}/{FETCH_RETRIES} failed; retrying", file=sys.stderr)
            time.sleep(FETCH_BACKOFF_SECONDS * attempt)
    raise RuntimeError("Fetch retries exhausted")


def parse_listing(html: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    count = soup.select_one("#eui-count")
    links = soup.select("main .item-container a.item-link")
    if count is None or not count.get_text(strip=True).isdigit():
        raise RuntimeError("Missing request count; sign-in or listing format may have changed.")
    requests = {}
    for link in links:
        url = urljoin(DEFAULT_SOURCE_URL, link.get("href", ""))
        validate_url(url)
        match = re.fullmatch(r"/eu-interoperability-request/(fb\d+)/?", urlsplit(url).path, re.I)
        if not match or urlsplit(url).query or urlsplit(url).fragment:
            raise RuntimeError("Unexpected request URL in listing.")
        rid = match[1].upper()
        if rid in requests:
            raise RuntimeError(f"Duplicate request in listing: {rid}")
        requests[rid] = url
    expected = int(count.get_text(strip=True))
    if len(requests) != expected or len(requests) < MIN_EXPECTED_REQUESTS:
        raise RuntimeError(
            f"Incomplete listing: found {len(requests)}, advertised {expected}; "
            "refusing to publish. Check pagination or changes to the page."
        )
    return sorted(requests.items(), key=lambda item: int(item[0][2:]))


def parse_detail(html: str, expected_id: str) -> tuple[dict, list[tuple[str, list[str]]]]:
    soup = BeautifulSoup(html, "html.parser")
    detail = soup.select_one("main .request-detail")
    if detail is None:
        raise RuntimeError(f"{expected_id}: missing request detail (sign-in or changed HTML).")
    fields = {}
    for label in detail.select("#request-meta .meta-label"):
        value = label.find_next_sibling(class_="meta-value")
        key = label.get_text(" ", strip=True).rstrip(":")
        if value is None or key in fields:
            raise RuntimeError(f"{expected_id}: invalid metadata field {key}")
        fields[key] = value.get_text(" ", strip=True)
    required = ("Developer", "Request ID", "Request Title", "Date Received", "Status", "Request Type")
    if any(not fields.get(key) for key in required) or fields["Request ID"] != expected_id:
        raise RuntimeError(f"{expected_id}: incomplete metadata or mismatched request ID.")
    if fields.keys() - set(required):
        raise RuntimeError(f"{expected_id}: unrecognized metadata fields; update the parser.")
    for link in detail.select("a[href]"):
        link["href"] = urljoin(official_request_url(expected_id), link["href"])
    meta = {"developer": fields["Developer"], "request_id": expected_id,
            "date_received": fields["Date Received"], "status": fields["Status"]}
    if meta["developer"] in ("Confidential", "[Confidential]"):
        meta["developer"] = "[Confidential]"
        meta["confidential"] = True
    sections = [("Descriptive Title", [fields["Request Title"]]),
                ("Request Type", [fields["Request Type"]])]
    # Keep every section, including new headings and confidentiality notices.
    headings = detail.find_all("h3", recursive=False)
    if not headings or not any(h.get_text(strip=True) == "Communications" for h in headings):
        raise RuntimeError(f"{expected_id}: missing detail sections or communications.")
    for heading in headings:
        body = []
        for sibling in heading.next_siblings:
            if getattr(sibling, "name", None) == "h3":
                break
            body.append(str(sibling))
        text = markdownify("".join(body), heading_style="ATX").strip()
        if not text:
            raise RuntimeError(f"{expected_id}: empty section {heading.get_text(strip=True)}")
        sections.append((heading.get_text(" ", strip=True), text.splitlines()))
    return meta, sections


def official_request_url(request_id: str) -> str:
    return f"{OFFICIAL_REQUEST_URL_BASE}{request_id.lower()}/"


def safe_slug(s: str, maxlen: int = 40) -> str:
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE).strip()
    s = re.sub(r"\s+", "-", s)
    return s[:maxlen].strip("-_") or "request"


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
        f"| Developer | {table_cell(dev)} |",
        f"| Request ID | {rid} |",
        f"| Official page | [{official_url}]({official_url}) |",
        f"| Date Received | {table_cell(date)} |",
        f"| Current Status | {table_cell(status)} |",
    ]
    if confidential:
        out.append("| Confidential | Yes |")
    out.append("")

    for lbl, lines in sections:
        text = "\n".join(lines).strip()
        if not text:
            continue
        # Preserve Markdown lists and emphasis from the web page.
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


def existing_filenames(directory: Path) -> dict[str, str]:
    names = {}
    for path in sorted(directory.glob('*.md')):
        match = MANAGED_FILENAME_RE.fullmatch(path.name)
        if match:
            if match[2] in names:
                raise RuntimeError(f"Duplicate existing request: {match[2]}")
            names[match[2]] = path.name
    return names


def table_cell(value: str) -> str:
    return value.replace('|', r'\|').replace('\n', '<br>')


def read_preserved_request(path: Path, request_id: str) -> tuple[bytes, dict]:
    """Keep the original bytes and recover index metadata from its header only."""
    content = path.read_bytes()
    header = content.decode('utf-8').split('\n## ', 1)[0]
    fields = dict(re.findall(r'^\| ([^|]+) \| (.*) \|$', header, re.MULTILINE))
    required = {'developer': 'Developer', 'date_received': 'Date Received',
                'status': 'Current Status', 'request_id': 'Request ID'}
    if any(not fields.get(label) for label in required.values()) or fields['Request ID'] != request_id:
        raise RuntimeError(f'{request_id}: invalid existing metadata; refusing to preserve.')
    meta = {key: fields[label].replace(r'\|', '|').replace('<br>', '\n')
            for key, label in required.items()}
    return content, meta


def write_outputs(records: list[tuple[dict, list]], out_dir: Path,
                  index_path: Path, existing: dict[str, str],
                  preserved: dict[str, tuple[bytes, dict]] | None = None) -> int:
    next_number = max((int(name.split('-')[0]) for name in existing.values()), default=0)
    outputs = {}
    rows = []
    for meta, sections in records:
        rid = meta['request_id']
        name = existing.get(rid)
        if name is None:
            next_number += 1
            slug = safe_slug(meta['developer'].replace('[', '').replace(']', ''))
            name = f'{next_number:03d}-{rid}-{slug}.md'
        outputs[name] = render_markdown(meta, sections).encode('utf-8')
        rows.append((name, meta))
    for rid, (content, meta) in (preserved or {}).items():
        name = existing[rid]
        outputs[name] = content
        rows.append((name, meta))
    rows.sort(key=lambda row: int(row[0].split('-')[0]))
    link_prefix = os.path.relpath(out_dir.resolve(), index_path.resolve().parent)
    index = [
        '# DMA 6.7 Interoperability Requests Received by Apple\n',
        f'Source: <{DEFAULT_SOURCE_URL}> and individual request pages.\n',
        '| # | Request ID | Developer | Date Received | Status | File |',
        '| ---: | --- | --- | --- | --- | --- |',
    ]
    for name, meta in rows:
        rid = meta['request_id']
        index.append(
            f"| {int(name.split('-')[0])} | [{rid}]({official_request_url(rid)}) | "
            f"{table_cell(meta['developer'])} | {table_cell(meta['date_received'])} | "
            f"{table_cell(meta['status'])} | [{name}]({link_prefix}/{name}) |"
        )
    # Fetch, parse, and render everything before replacing existing outputs.
    _safe_clear_out_dir(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, markdown in outputs.items():
        (out_dir / name).write_bytes(markdown)
    index_path.write_text('\n'.join(index) + '\n', encoding='utf-8')
    return len(outputs)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default=DEFAULT_SOURCE_URL,
                        help='Apple listing URL or saved listing HTML')
    parser.add_argument('--details-dir', type=Path,
                        help='Read saved detail HTML (fbNNNN.html) from this directory')
    parser.add_argument('--existing-dir', type=Path,
                        help='Existing requests directory for stable filenames (default: --out)')
    parser.add_argument('--out', type=Path, default=Path(DEFAULT_OUT_DIR))
    parser.add_argument('--index', type=Path, default=Path(DEFAULT_INDEX))
    args = parser.parse_args(argv)
    existing_dir = args.existing_dir or args.out
    existing = existing_filenames(existing_dir)
    listing = parse_listing(fetch_html(args.source))
    missing = existing.keys() - {rid for rid, _ in listing}
    if missing:
        raise RuntimeError(f'Listing omits existing requests: {sorted(missing)}; refusing removal.')
    records = []
    preserved = {}
    for i, (rid, url) in enumerate(listing, 1):
        print(f'Fetching {i}/{len(listing)}: {rid}', file=sys.stderr)
        source = str(args.details_dir / f'{rid.lower()}.html') if args.details_dir else url
        try:
            html = fetch_html(source)
        except urllib.error.HTTPError as error:
            if error.code != 500:
                raise
            # fetch_html has already exhausted its retries. Only detail-page
            # HTTP 500 responses qualify; authentication and parsing still fail.
            if rid in existing:
                preserved[rid] = read_preserved_request(existing_dir / existing[rid], rid)
                action = 'preserving existing Markdown and index metadata'
            else:
                action = 'deferring new request until a later sync'
            print(f'::warning::{rid}: HTTP 500 after retries; {action}.', file=sys.stderr)
            continue
        records.append(parse_detail(html, rid))
    n = write_outputs(records, args.out, args.index, existing, preserved)
    print(f'Wrote {n} request files + {args.index}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
