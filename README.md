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

This repository solves that. It fetches the tracker, splits it into one Markdown
file per request, and commits every change through a dedicated pull request.
That way each update to Apple's document shows up as an isolated, human-readable
diff in the [PR history](../../pulls?q=is%3Apr) — easy to scan, review, and
reference.

## Sources

- Apple's page: <https://developer.apple.com/eu-interoperability-request>
- Support page: <https://developer.apple.com/support/interoperability-requests/>
- The tracked PDF: <https://developer.apple.com/file/?file=interoperability-request-tracker&format=pdf>

## Repository layout

| Path | Description |
| --- | --- |
| [`index.md`](index.md) | Generated summary table of every request (ID, developer, date, status, link). |
| [`requests/`](requests/) | One Markdown file per request, named `NNN-FBxxxxxx-<developer>.md`. |
| [`scripts/update_tracker.py`](scripts/update_tracker.py) | Fetches the PDF and generates `requests/` + `index.md`. |
| [`scripts/sync_prs.py`](scripts/sync_prs.py) | Diffs a fresh generation against the repo and opens one PR per change. |
| [`.github/workflows/update-tracker.yml`](.github/workflows/update-tracker.yml) | Runs the sync on a daily schedule. |
