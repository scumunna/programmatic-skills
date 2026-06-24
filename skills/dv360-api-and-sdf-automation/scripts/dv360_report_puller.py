#!/usr/bin/env python3
"""Create, run, and download a Display & Video 360 report via the Bid Manager API.

This is a documented skeleton. It is correct in shape and safe to import or run with
``--help`` without credentials, because every network call is created lazily and only
inside ``run()``. Nothing reaches the network at import time or when you print usage.

Workflow (Bid Manager API v2):
  1. queries.create  -> define a report (metrics, dimensions, date range) as a Query.
  2. queries.run     -> generate the report; the CSV is written to Google Cloud Storage.
  3. queries.reports.list -> find the latest report and read its googleCloudStoragePath.
  4. download the CSV from that path.

Setup:
  pip install google-api-python-client google-auth google-auth-oauthlib

  OAuth scope required (Bid Manager / reporting API):
    https://www.googleapis.com/auth/doubleclickbidmanager

  This is a SEPARATE service and scope from the Display & Video 360 entity API
  (which uses https://www.googleapis.com/auth/display-video). A token for one does
  not authorize the other.

Credentials (no secrets in code):
  Set GOOGLE_APPLICATION_CREDENTIALS to the path of a service-account JSON key, then
  associate that service account's email with a DV360 user that can run reports.
  This script never embeds a key and never prints credential contents.

Example:
  export GOOGLE_APPLICATION_CREDENTIALS=/secure/path/dv360-sa.json
  python3 dv360_report_puller.py \\
      --advertiser-id 123456 \\
      --start 2026-06-01 --end 2026-06-23 \\
      --out report.csv

Design notes:
  - Report design (which metrics and dimensions to request) belongs to the
    dv360-reporting skill. The QUERY_TEMPLATE below is a minimal, editable starting
    point, not an opinion about the right report.
  - This skeleton will not be executed against a live account here. The guarded
    structure lets you read it, import it, and run --help with no dependencies and
    no network access.
"""

from __future__ import annotations

import argparse
import os
import sys
import time

# Bid Manager (reporting) API. Distinct from the Display & Video 360 entity API.
BIDMANAGER_API_NAME = "doubleclickbidmanager"
BIDMANAGER_API_VERSION = "v2"
BIDMANAGER_SCOPE = "https://www.googleapis.com/auth/doubleclickbidmanager"

# Environment variable that points at the service-account JSON key. Never hardcode keys.
CREDENTIALS_ENV_VAR = "GOOGLE_APPLICATION_CREDENTIALS"

# Minimal, editable report definition. Adjust metrics/dimensions per dv360-reporting.
# dataRange uses CUSTOM_DATES so the --start / --end flags drive the window.
QUERY_TEMPLATE = {
    "metadata": {
        "title": "dv360-report-puller",
        "dataRange": {"range": "CUSTOM_DATES"},
        "format": "CSV",
    },
    "params": {
        "type": "STANDARD",
        "groupBys": ["FILTER_ADVERTISER", "FILTER_DATE"],
        "metrics": ["METRIC_IMPRESSIONS", "METRIC_CLICKS", "METRIC_REVENUE_ADVERTISER"],
        "filters": [],  # filled in run() from --partner-id / --advertiser-id
    },
    "schedule": {"frequency": "ONE_TIME"},
}


def build_query(args: argparse.Namespace) -> dict:
    """Return a Query body for queries.create from the parsed flags.

    Kept pure (no network, no imports beyond stdlib) so it is trivially testable and
    so importing this module is cheap.
    """
    query = {
        "metadata": dict(QUERY_TEMPLATE["metadata"]),
        "params": {
            "type": QUERY_TEMPLATE["params"]["type"],
            "groupBys": list(QUERY_TEMPLATE["params"]["groupBys"]),
            "metrics": list(QUERY_TEMPLATE["params"]["metrics"]),
            "filters": [],
        },
        "schedule": dict(QUERY_TEMPLATE["schedule"]),
    }
    # CUSTOM_DATES needs an explicit window. Dates are YYYY-MM-DD strings.
    start_y, start_m, start_d = (int(p) for p in args.start.split("-"))
    end_y, end_m, end_d = (int(p) for p in args.end.split("-"))
    query["metadata"]["dataRange"] = {
        "range": "CUSTOM_DATES",
        "customStartDate": {"year": start_y, "month": start_m, "day": start_d},
        "customEndDate": {"year": end_y, "month": end_m, "day": end_d},
    }
    if args.partner_id:
        query["params"]["filters"].append(
            {"type": "FILTER_PARTNER", "value": str(args.partner_id)}
        )
    if args.advertiser_id:
        query["params"]["filters"].append(
            {"type": "FILTER_ADVERTISER", "value": str(args.advertiser_id)}
        )
    return query


def _build_service():
    """Build an authenticated Bid Manager service client.

    Imported lazily so the module imports and prints --help without the Google client
    libraries installed and without touching credentials or the network.
    """
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError as exc:  # pragma: no cover - depends on optional deps
        raise SystemExit(
            "Missing dependencies. Install with:\n"
            "  pip install google-api-python-client google-auth google-auth-oauthlib"
        ) from exc

    key_path = os.environ.get(CREDENTIALS_ENV_VAR)
    if not key_path:
        raise SystemExit(
            f"Set {CREDENTIALS_ENV_VAR} to your service-account JSON key path. "
            "This script never hardcodes credentials."
        )
    if not os.path.isfile(key_path):
        raise SystemExit(f"{CREDENTIALS_ENV_VAR} points at a missing file: {key_path}")

    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=[BIDMANAGER_SCOPE]
    )
    return build(
        BIDMANAGER_API_NAME, BIDMANAGER_API_VERSION, credentials=credentials,
        cache_discovery=False,
    )


def _download(url: str, out_path: str) -> None:
    """Download the report CSV from its Cloud Storage path to out_path."""
    from urllib.request import urlopen  # stdlib; lazy import keeps top-level cheap

    with urlopen(url) as response, open(out_path, "wb") as handle:  # noqa: S310
        handle.write(response.read())


def run(args: argparse.Namespace) -> int:
    """Execute the full create -> run -> poll -> download flow against the live API."""
    query_body = build_query(args)
    service = _build_service()

    # 1. Create the query (the reusable report definition).
    created = service.queries().create(body=query_body).execute()
    query_id = created["queryId"]
    print(f"Created query {query_id}")

    # 2. Run the query. This generates the CSV in Google Cloud Storage.
    run_op = service.queries().run(queryId=query_id).execute()
    print(f"Started run for query {query_id}: {run_op}")

    # 3. Poll queries.reports.list for the latest report and wait until it is done.
    storage_path = None
    deadline = time.time() + args.timeout
    while time.time() < deadline:
        reports = (
            service.queries()
            .reports()
            .list(queryId=query_id, orderBy="key.reportId desc", pageSize=1)
            .execute()
            .get("reports", [])
        )
        if reports:
            metadata = reports[0].get("metadata", {})
            status = metadata.get("status", {}).get("state")
            if status == "DONE":
                storage_path = metadata.get("googleCloudStoragePath")
                break
            if status == "FAILED":
                raise SystemExit(f"Report for query {query_id} failed: {metadata}")
        time.sleep(args.poll_interval)

    if not storage_path:
        raise SystemExit(
            f"Report did not finish within {args.timeout}s. Re-run later or raise --timeout."
        )

    # 4. Download the CSV from the path the API returned.
    _download(storage_path, args.out)
    print(f"Downloaded report to {args.out}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create, run, and download a DV360 report via the Bid Manager API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--partner-id", help="DV360 partner ID to filter on.")
    parser.add_argument("--advertiser-id", help="DV360 advertiser ID to filter on.")
    parser.add_argument("--start", help="Report start date, YYYY-MM-DD.")
    parser.add_argument("--end", help="Report end date, YYYY-MM-DD.")
    parser.add_argument("--out", default="report.csv", help="Output CSV path.")
    parser.add_argument(
        "--poll-interval", type=int, default=15,
        help="Seconds between report status checks (default 15).",
    )
    parser.add_argument(
        "--timeout", type=int, default=1800,
        help="Max seconds to wait for the report (default 1800).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()

    # With no arguments, print usage and exit cleanly (do not error, do not call out).
    if not argv:
        parser.print_help()
        return 0

    args = parser.parse_args(argv)

    # Validate required flags here (not via required=True) so bare invocation can show help.
    missing = [name for name in ("start", "end") if not getattr(args, name)]
    if not args.partner_id and not args.advertiser_id:
        missing.append("partner-id or advertiser-id")
    if missing:
        parser.error("missing required argument(s): " + ", ".join(missing))

    return run(args)


if __name__ == "__main__":
    sys.exit(main())
