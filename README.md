# Apple Interoperability Request Tracker

Track changes to Apple's **DMA Article 6(7) Interoperability Request** tracker —
one reviewable diff per request, per pull request.

## Why this exists

Under the EU Digital Markets Act, Apple publishes the interoperability requests
it receives. As of July 7, 2026, the request list can be viewed on a
[web page](https://developer.apple.com/eu-interoperability-request/) as well as
the original PDF — but neither surface shows *what actually changed* when Apple
updates it. A new request, a status change, or a fresh reply from Apple is
invisible unless you compare snapshots by hand.

This repository solves that. It fetches the web listing and each request page, generates one Markdown
file per request, and commits every change through a dedicated pull request.
That way each update to Apple's document shows up as an isolated, human-readable
diff in the [PR history](../../pulls?q=is%3Apr) — easy to scan, review, and
reference.

## Sources

- Apple's page: <https://developer.apple.com/eu-interoperability-request>
- Support page: <https://developer.apple.com/support/interoperability-requests/>
- Legacy PDF (not fetched): <https://developer.apple.com/file/?file=interoperability-request-tracker&format=pdf>

## Repository layout

| Path | Description |
| --- | --- |
| [`index.md`](index.md) | Generated summary table of every request (ID, developer, date, status, links). |
| [`requests/`](requests/) | One Markdown file per request, named `NNN-FBxxxxxx-<developer>.md`. |
| [`scripts/update_tracker.py`](scripts/update_tracker.py) | Fetches the web listing and request pages and generates `requests/` + `index.md`. |
| [`scripts/sync_prs.py`](scripts/sync_prs.py) | Diffs a fresh generation against the repo and opens one PR per change. |
| [`.github/workflows/update-tracker.yml`](.github/workflows/update-tracker.yml) | Runs the sync on a daily schedule. |

## Running locally

Install dependencies with `pip install -r scripts/requirements.txt`, then run
`python scripts/update_tracker.py`. Set `APPLE_DEV_COOKIE` to a valid Apple
Developer session cookie; the daily workflow uses the existing secret of the
same name. An expired cookie stops the run without publishing partial results.

For saved HTML snapshots, use:

```sh
python scripts/update_tracker.py --source snapshot/index.html --details-dir snapshot
```

Save each detail page as `snapshot/fbNNNN.html`, using its lowercase request ID.
The parser checks the listing's advertised count, required metadata, request IDs,
and communications sections before writing any output. Missing existing requests
stop the run for investigation rather than automatically deleting their history.
Existing filenames and sequence numbers are retained; new requests are appended
in request-ID order. Use `--existing-dir requests` when generating into a separate
staging directory (the PR sync passes this automatically).

The first web sync may change many files: Apple has revised titles, descriptions,
section labels, and statuses, and HTML removes the PDF's artificial line breaks.

Run regression tests with `python -m unittest discover -s tests`.

If an individual detail page still returns HTTP 500 after all three attempts,
the sync emits an Actions warning with its request ID and continues. Existing
requests keep their exact Markdown bytes and previous index metadata; new
requests are omitted until a later successful sync. Every listed request is
retried on the next run. Listing failures, other HTTP errors, authentication
failures, and invalid HTML still stop the run before any output is replaced.

If GitHub rejects a merge with “Base branch was modified. Review and try the
merge again.”, the sync retries the same PR after 5 seconds and then 10 seconds
(three attempts total). Other errors and exhausted retries still stop the sync.
