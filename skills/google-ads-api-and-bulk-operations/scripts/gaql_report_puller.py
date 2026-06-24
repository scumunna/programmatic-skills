#!/usr/bin/env python3
"""Pull a Google Ads report by running a GAQL query through SearchStream.

This is a documented skeleton. It is correct in shape and safe to import or run with
``--help`` (or no arguments) without credentials, because the client and every network
call are created lazily and only inside ``run()``. Nothing reaches the network at import
time or when you print usage.

Read path only. GAQL is read only: this script retrieves rows and never mutates. Writes
go through mutate operations, which are deliberately not included here so an unattended
run cannot change a live account. See the safe-to-automate matrix in the skill.

Workflow (Google Ads API, current major version v24):
  1. Build a GoogleAdsClient from credentials in the environment or a config file.
  2. Get GoogleAdsService.
  3. Run a GAQL query with search_stream against one customer ID.
  4. Print or write the rows.

Setup:
  pip install google-ads

Credentials (no secrets in code):
  The google-ads library reads its configuration from environment variables or a
  google-ads.yaml file. This script never embeds a token or key and never prints
  credential contents. Provide, by environment variable or YAML:
    - developer token        (GOOGLE_ADS_DEVELOPER_TOKEN)
    - OAuth client id/secret (GOOGLE_ADS_CLIENT_ID / GOOGLE_ADS_CLIENT_SECRET)
    - OAuth refresh token    (GOOGLE_ADS_REFRESH_TOKEN)
      or a service-account key path for the service-account flow
    - login customer id      (GOOGLE_ADS_LOGIN_CUSTOMER_ID), the manager (MCC) account,
      digits only, when calling a client account through a manager.

Example:
  export GOOGLE_ADS_DEVELOPER_TOKEN=...
  export GOOGLE_ADS_CLIENT_ID=...
  export GOOGLE_ADS_CLIENT_SECRET=...
  export GOOGLE_ADS_REFRESH_TOKEN=...
  export GOOGLE_ADS_LOGIN_CUSTOMER_ID=1234567890
  python3 gaql_report_puller.py \\
      --customer-id 9876543210 \\
      --start 2026-06-01 --end 2026-06-23 \\
      --out report.csv

Design notes:
  - Report design (which fields, segments, and metrics to request) belongs to the
    google-ads-reporting skill. The QUERY_TEMPLATE below is a minimal, editable
    starting point, not an opinion about the right report.
  - Cost is returned in micros (1,000,000 micros = one unit of account currency).
    This skeleton emits the raw values; convert before showing a human.
  - This skeleton will not be executed against a live account here. The guarded
    structure lets you read it, import it, and run --help with no dependencies and
    no network access.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys

# Pin the API version the query and client target. Bump deliberately when upgrading.
API_VERSION = "v24"

# Environment variables the google-ads library reads. Listed here for documentation;
# the library itself loads them. Never hardcode their values.
ENV_VARS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
)

# Minimal, editable GAQL query. The {start} and {end} placeholders are filled in
# build_query from the --start / --end flags. Adjust fields per google-ads-reporting.
QUERY_TEMPLATE = """
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE segments.date BETWEEN '{start}' AND '{end}'
ORDER BY metrics.cost_micros DESC
"""

# Columns pulled out of each returned row, in output order. Keep aligned with the SELECT.
OUTPUT_COLUMNS = (
    "campaign.id",
    "campaign.name",
    "campaign.status",
    "metrics.impressions",
    "metrics.clicks",
    "metrics.cost_micros",
    "metrics.conversions",
)


def build_query(args: argparse.Namespace) -> str:
    """Return the GAQL query string from the parsed flags.

    Kept pure (no network, no imports beyond stdlib) so it is trivially testable and
    so importing this module is cheap. Dates are validated as YYYY-MM-DD before they
    are interpolated, so the query string cannot be steered by malformed input.
    """
    for label, value in (("--start", args.start), ("--end", args.end)):
        parts = value.split("-")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            raise SystemExit(f"{label} must be YYYY-MM-DD, got: {value}")
    return QUERY_TEMPLATE.format(start=args.start, end=args.end).strip()


def _build_client():
    """Build an authenticated GoogleAdsClient.

    Imported lazily so the module imports and prints --help without the google-ads
    library installed and without touching credentials or the network. The library
    loads its own configuration from environment variables or a google-ads.yaml file.
    """
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:  # pragma: no cover - depends on optional deps
        raise SystemExit(
            "Missing dependency. Install with:\n  pip install google-ads"
        ) from exc

    # load_from_env reads GOOGLE_ADS_* variables. load_from_storage reads a YAML file.
    if os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN"):
        return GoogleAdsClient.load_from_env(version=API_VERSION)
    config_path = os.environ.get("GOOGLE_ADS_CONFIGURATION_FILE_PATH")
    if config_path:
        return GoogleAdsClient.load_from_storage(config_path, version=API_VERSION)
    raise SystemExit(
        "No Google Ads credentials found. Set the GOOGLE_ADS_* environment variables "
        "(see this file's header) or GOOGLE_ADS_CONFIGURATION_FILE_PATH to a "
        "google-ads.yaml. This script never hardcodes credentials."
    )


def _row_values(row) -> list:
    """Pull OUTPUT_COLUMNS out of one GoogleAdsRow as plain Python values."""
    values = []
    for column in OUTPUT_COLUMNS:
        obj = row
        for attr in column.split("."):
            obj = getattr(obj, attr)
        values.append(obj)
    return values


def run(args: argparse.Namespace) -> int:
    """Execute the GAQL query against the live API and emit rows."""
    query = build_query(args)
    client = _build_client()
    service = client.get_service("GoogleAdsService")

    # search_stream returns batches of rows; iterate batches then rows within each.
    stream = service.search_stream(customer_id=args.customer_id, query=query)

    if args.out:
        handle = open(args.out, "w", newline="", encoding="utf-8")
        writer = csv.writer(handle)
    else:
        handle = None
        writer = csv.writer(sys.stdout)

    try:
        writer.writerow(OUTPUT_COLUMNS)
        count = 0
        for batch in stream:
            for row in batch.results:
                writer.writerow(_row_values(row))
                count += 1
    finally:
        if handle is not None:
            handle.close()

    where = args.out if args.out else "stdout"
    print(f"Wrote {count} rows to {where}", file=sys.stderr)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Pull a Google Ads report by running a GAQL query via SearchStream.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--customer-id",
        help="Operating customer ID to query (digits only, no dashes).",
    )
    parser.add_argument("--start", help="Report start date, YYYY-MM-DD.")
    parser.add_argument("--end", help="Report end date, YYYY-MM-DD.")
    parser.add_argument(
        "--out",
        default=None,
        help="Output CSV path. Omit to print CSV to stdout.",
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

    # Validate required flags here (not via required=True) so bare invocation shows help.
    missing = [
        name for name in ("customer_id", "start", "end") if not getattr(args, name)
    ]
    if missing:
        parser.error(
            "missing required argument(s): "
            + ", ".join(name.replace("_", "-") for name in missing)
        )

    return run(args)


if __name__ == "__main__":
    sys.exit(main())
