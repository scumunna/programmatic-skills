#!/usr/bin/env python3
"""Pacing calculator for a DV360 flight (or any flighted budget).

Pure Python 3 standard library. No credentials, no third-party dependencies,
no network calls. It does arithmetic on numbers you already have from a pacing
report, so it is safe to run anywhere.

Given a total budget, the flight start and end dates, an "as of" date, and the
spend booked so far, it reports:

  - ideal even daily spend        total budget / total flight days
  - expected spend to date        even daily spend * days elapsed
  - pacing index                  actual spend / expected spend
                                  (1.0 = on pace, <1.0 behind, >1.0 ahead)
  - projected end-of-flight spend  current daily run rate * total flight days
  - recommended new daily spend    remaining budget / remaining days, so the
                                  flight lands exactly on budget from here

Dates are inclusive on both ends, matching how a flight is booked: a flight
that runs 2026-06-01 to 2026-06-30 is 30 days, not 29.

Worked example
--------------
A $30,000 line item runs 2026-06-01 to 2026-06-30 (30 days). On 2026-06-10,
10 days have elapsed (June 1 through 10 inclusive) and $8,000 has been spent.

    python3 pacing_calculator.py \\
        --budget 30000 \\
        --start 2026-06-01 \\
        --end 2026-06-30 \\
        --as-of 2026-06-10 \\
        --spend 8000

    Ideal even daily spend:        $1,000.00
    Expected spend to date:        $10,000.00
    Pacing index (actual/expected): 0.80   (behind pace)
    Projected end-of-flight spend: $24,000.00  (80.0% of budget)
    Recommended new daily spend:   $1,100.00  for the remaining 20 days

The line item is underpacing at 0.80. Left alone it would end at $24,000 and
leave $6,000 unspent, so the daily target must rise from $1,000 to $1,100 to
finish on budget.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime


def parse_date(value: str) -> date:
    """Parse YYYY-MM-DD, raising a clear error the CLI can surface."""
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"invalid date '{value}', expected YYYY-MM-DD (for example 2026-06-30)"
        )


def inclusive_days(start: date, end: date) -> int:
    """Number of days from start to end with both ends counted."""
    return (end - start).days + 1


def compute(budget: float, start: date, end: date, as_of: date, spend: float) -> dict:
    """Return the pacing figures. Pure function, easy to test.

    Validation guards the arithmetic so callers never divide by zero or feed
    in a nonsensical flight (end before start, as-of outside the flight, or a
    negative amount).
    """
    if budget <= 0:
        raise ValueError("budget must be greater than 0")
    if spend < 0:
        raise ValueError("spend to date cannot be negative")
    if end < start:
        raise ValueError("flight end date is before the start date")
    if as_of < start:
        raise ValueError("as-of date is before the flight start; nothing has elapsed yet")
    if as_of > end:
        raise ValueError("as-of date is after the flight end; the flight is already over")

    total_days = inclusive_days(start, end)
    days_elapsed = inclusive_days(start, as_of)
    days_remaining = total_days - days_elapsed

    ideal_daily = budget / total_days
    expected_to_date = ideal_daily * days_elapsed

    # Pacing index compares booked spend to where even pacing would be today.
    pacing_index = spend / expected_to_date if expected_to_date else 0.0

    # Run rate from actual spend so far, projected across the whole flight.
    daily_run_rate = spend / days_elapsed if days_elapsed else 0.0
    projected_total = daily_run_rate * total_days

    remaining_budget = budget - spend
    # If there are remaining days, spread the remaining budget across them.
    # On the final day, there is no "new daily" to set, so report the leftover.
    if days_remaining > 0:
        recommended_daily = remaining_budget / days_remaining
    else:
        recommended_daily = 0.0

    return {
        "total_days": total_days,
        "days_elapsed": days_elapsed,
        "days_remaining": days_remaining,
        "ideal_daily": ideal_daily,
        "expected_to_date": expected_to_date,
        "pacing_index": pacing_index,
        "projected_total": projected_total,
        "projected_pct_of_budget": (projected_total / budget * 100) if budget else 0.0,
        "remaining_budget": remaining_budget,
        "recommended_daily": recommended_daily,
    }


def pace_label(index: float) -> str:
    """Plain-language read of the pacing index for the report line."""
    if index < 0.95:
        return "behind pace"
    if index > 1.05:
        return "ahead of pace"
    return "on pace"


def format_report(figures: dict) -> str:
    lines = [
        f"Flight length:                 {figures['total_days']} days "
        f"({figures['days_elapsed']} elapsed, {figures['days_remaining']} remaining)",
        f"Ideal even daily spend:        ${figures['ideal_daily']:,.2f}",
        f"Expected spend to date:        ${figures['expected_to_date']:,.2f}",
        f"Pacing index (actual/expected): {figures['pacing_index']:.2f}   "
        f"({pace_label(figures['pacing_index'])})",
        f"Projected end-of-flight spend: ${figures['projected_total']:,.2f}  "
        f"({figures['projected_pct_of_budget']:.1f}% of budget)",
        f"Remaining budget:              ${figures['remaining_budget']:,.2f}",
    ]
    if figures["days_remaining"] > 0:
        lines.append(
            f"Recommended new daily spend:   ${figures['recommended_daily']:,.2f}  "
            f"for the remaining {figures['days_remaining']} days"
        )
    else:
        lines.append(
            "Recommended new daily spend:   n/a, this is the final flight day; "
            f"${figures['remaining_budget']:,.2f} remains to spend today"
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pacing_calculator.py",
        description=(
            "Compute even daily spend, expected spend to date, pacing index, "
            "projected end-of-flight spend, and the recommended new daily spend "
            "to finish a flight exactly on budget."
        ),
        epilog=(
            "Example:\n"
            "  python3 pacing_calculator.py --budget 30000 --start 2026-06-01 "
            "--end 2026-06-30 --as-of 2026-06-10 --spend 8000\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--budget", type=float, required=True,
                        help="total flight budget (amount, same units as spend)")
    parser.add_argument("--start", type=parse_date, required=True,
                        help="flight start date, YYYY-MM-DD (inclusive)")
    parser.add_argument("--end", type=parse_date, required=True,
                        help="flight end date, YYYY-MM-DD (inclusive)")
    parser.add_argument("--as-of", type=parse_date, required=True, dest="as_of",
                        help="date you are evaluating pacing on, YYYY-MM-DD (inclusive)")
    parser.add_argument("--spend", type=float, required=True,
                        help="spend booked so far, as of the --as-of date")
    return parser


def main(argv: list[str]) -> int:
    # Print full usage when run with no arguments, matching --help.
    if not argv:
        build_parser().print_help()
        return 0

    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        figures = compute(args.budget, args.start, args.end, args.as_of, args.spend)
    except ValueError as exc:
        parser.error(str(exc))
        return 2  # argparse.error exits, but keep the type checker honest

    print(format_report(figures))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
