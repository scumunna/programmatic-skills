#!/usr/bin/env python3
"""Plan a budget across a flight and project outcomes before launch.

Given a budget, a flight, and a target CPM (plus optional CTR and CVR), project the
even daily budget, the impressions the budget buys, and the clicks, conversions, and
CPA you would expect at those rates. It also prints cumulative spend checkpoints at 25,
50, and 75 percent of the flight so you can spot pacing drift early.

Dates are YYYY-MM-DD and the flight includes both the start and the end day.

Examples:
  budget_flight_planner.py --budget 30000 --start 2026-07-01 --end 2026-07-31 --cpm 6
  budget_flight_planner.py --budget 30000 --start 2026-07-01 --end 2026-07-31 --cpm 6 --ctr 0.002 --cvr 0.05

No credentials and no network. Pure arithmetic. Dates come from the arguments, not the clock.
"""

from __future__ import annotations

import argparse
import datetime
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Plan a budget across a flight and project impressions, clicks, and conversions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Rates are fractions: a 0.2 percent CTR is --ctr 0.002.",
    )
    parser.add_argument("--budget", type=float, required=True, help="total flight budget")
    parser.add_argument("--start", required=True, help="flight start date, YYYY-MM-DD (inclusive)")
    parser.add_argument("--end", required=True, help="flight end date, YYYY-MM-DD (inclusive)")
    parser.add_argument("--cpm", type=float, required=True, help="target or expected CPM")
    parser.add_argument("--ctr", type=float, help="expected click-through rate as a fraction")
    parser.add_argument("--cvr", type=float, help="expected conversion rate per click as a fraction")
    return parser


def parse_date(value: str) -> datetime.date:
    return datetime.datetime.strptime(value, "%Y-%m-%d").date()


def main(argv: list[str]) -> int:
    parser = build_parser()
    if not argv:
        parser.print_help()
        return 0
    args = parser.parse_args(argv)

    try:
        start = parse_date(args.start)
        end = parse_date(args.end)
    except ValueError:
        print("error: dates must be YYYY-MM-DD", file=sys.stderr)
        return 2
    if end < start:
        print("error: --end is before --start", file=sys.stderr)
        return 2
    if args.cpm <= 0 or args.budget <= 0:
        print("error: --budget and --cpm must be greater than 0", file=sys.stderr)
        return 2

    days = (end - start).days + 1
    daily = args.budget / days
    impressions = args.budget / args.cpm * 1000

    print(f"flight:            {start} to {end} ({days} days)")
    print(f"budget:            {args.budget:,.2f}")
    print(f"even daily budget: {daily:,.2f}")
    print(f"projected impressions: {impressions:,.0f} at a {args.cpm:g} CPM")

    if args.ctr is not None:
        clicks = impressions * args.ctr
        print(f"projected clicks:      {clicks:,.0f} at a {args.ctr:g} CTR")
        if args.cvr is not None:
            conversions = clicks * args.cvr
            print(f"projected conversions: {conversions:,.1f} at a {args.cvr:g} CVR")
            if conversions > 0:
                print(f"projected CPA:         {args.budget / conversions:,.2f}")

    print("pacing checkpoints (expected cumulative spend):")
    for pct in (0.25, 0.50, 0.75):
        checkpoint_day = max(1, round(days * pct))
        print(f"  by day {checkpoint_day:>3} ({int(pct * 100)} percent of flight): {daily * checkpoint_day:,.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
