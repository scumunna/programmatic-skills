#!/usr/bin/env python3
"""Generate a minimal Structured Data File (SDF) v10 Line Items template.

Emits a header row plus one example line item row to stdout or to a path. Pure Python
standard library, no dependencies, no network. Use it as a starting point for a bulk
create, then fill in real values and add one row per line item.

IMPORTANT: column names and accepted values change between SDF versions. ALWAYS validate
this template against the CURRENT SDF format reference before uploading:
  https://developers.google.com/display-video/api/structured-data-file/format

This emits a deliberately small SUBSET of columns. SDF supports uploading a subset, which
keeps files small and fast to process. Add the columns you need from the format reference;
do not assume this subset is complete for your use case. For a brand-new line item, the
"Line Item Id" is left blank so the platform assigns one on upload (per the format
reference's convention for new resources).

SDF upload is UI-only: the DV360 API can download SDFs but cannot upload them. Generate the
file here, review it as a diff, and upload it through the Display & Video 360 UI. Then read
the result file to confirm which rows succeeded.

Usage:
  python3 sdf_template.py                # no args: print this usage
  python3 sdf_template.py --stdout       # print the template to stdout
  python3 sdf_template.py --out li.csv   # write the template to li.csv
  python3 sdf_template.py --help         # show help
"""

from __future__ import annotations

import argparse
import csv
import io
import sys

# SDF version this template targets. Confirm against the format reference before use.
SDF_VERSION = "v10"

# A minimal, illustrative subset of Line Items columns. NOT the full column set.
# Confirm exact names/order against the current SDF Line Items format reference.
LINE_ITEMS_HEADER = [
    "Line Item Id",        # blank for a new line item; platform assigns on upload
    "Io Id",               # parent insertion order ID (required)
    "Type",                # e.g. Display, Video
    "Name",                # line item name
    "Timestamp",           # leave blank for new rows
    "Status",              # Draft / Active / Paused; create as Draft to QA first
    "Start Date",          # MM/DD/YYYY HH:MM or per format reference
    "End Date",
    "Budget Type",         # Amount / Impressions
    "Budget Amount",
    "Pacing",              # Daily / Flight
    "Pacing Rate",         # ASAP / Even / Ahead
    "Pacing Amount",
    "Frequency Enabled",   # TRUE / FALSE
    "Frequency Exposures",
    "Frequency Period",    # Minutes / Hours / Days / Weeks / Months
    "Frequency Amount",
    "Bid Strategy Type",   # Minimize / Maximize / Beat / Optimize / Fixed
    "Bid Strategy Value",
    "Geography Targeting - Include",
]

# One example row. Placeholder values only. Replace before uploading. A new line item
# leaves "Line Item Id" blank and is created in Draft so it can be QA'd before activation.
EXAMPLE_ROW = [
    "",                       # Line Item Id (blank = create new)
    "987654321",              # Io Id (parent insertion order)
    "Display",                # Type
    "PROSPECTING_DISPLAY_US", # Name
    "",                       # Timestamp (blank for new)
    "Draft",                  # Status (create as Draft, then QA, then activate)
    "06/01/2026 00:00",       # Start Date
    "06/30/2026 23:59",       # End Date
    "Amount",                 # Budget Type
    "10000",                  # Budget Amount
    "Flight",                 # Pacing
    "Even",                   # Pacing Rate
    "10000",                  # Pacing Amount
    "TRUE",                   # Frequency Enabled
    "3",                      # Frequency Exposures
    "Days",                   # Frequency Period
    "1",                      # Frequency Amount
    "Minimize",               # Bid Strategy Type (e.g. minimize CPA/CPC)
    "",                       # Bid Strategy Value
    "United States",          # Geography Targeting - Include
]

NOTE_LINE = (
    f"# SDF {SDF_VERSION} Line Items template (subset of columns). "
    "Validate against the current SDF format reference before uploading. "
    "Upload is UI-only; the API cannot upload SDFs."
)


def render() -> str:
    """Return the template as CSV text, with a leading comment note."""
    buffer = io.StringIO()
    buffer.write(NOTE_LINE + "\n")
    writer = csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(LINE_ITEMS_HEADER)
    writer.writerow(EXAMPLE_ROW)
    return buffer.getvalue()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            f"Generate a minimal SDF {SDF_VERSION} Line Items template "
            "(header plus one example row)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--out",
        help="Write the template to this path.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print the template to stdout.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()

    # No arguments: print usage so the user sees what this does. Emit the template only
    # when asked explicitly with --stdout or --out.
    if not argv:
        parser.print_help()
        return 0

    args = parser.parse_args(argv)

    if not args.out and not args.stdout:
        parser.error("choose an output: --stdout to print, or --out PATH to write a file.")

    text = render()

    if args.out:
        try:
            with open(args.out, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)
        except OSError as exc:
            parser.error(f"could not write to {args.out}: {exc}")
        print(f"Wrote SDF {SDF_VERSION} Line Items template to {args.out}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
