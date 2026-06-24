#!/usr/bin/env python3
"""Check whether a frequency cap can deliver the impressions a plan needs.

The most impressions a capped buy can deliver over its flight is:
    reachable audience  x  frequency cap
If the impressions you need exceed that, the cap or the audience size will starve
delivery no matter how high you bid. This is the audience-times-cap versus
required-impressions check from the frequency and troubleshooting skills.

Give the required impressions directly, or a budget and a CPM to derive them:
    required impressions = budget / cpm x 1000

Examples:
  frequency_delivery_check.py --audience 500000 --freq-cap 10 --required-impressions 4000000
  frequency_delivery_check.py --audience 500000 --freq-cap 10 --budget 30000 --cpm 6

No credentials and no network. Pure arithmetic.
"""

from __future__ import annotations

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check if a frequency cap can deliver the impressions a plan needs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--audience", type=int, required=True,
                        help="reachable audience size (unique users)")
    parser.add_argument("--freq-cap", type=float, required=True, dest="freq_cap",
                        help="frequency cap: impressions per user over the flight")
    parser.add_argument("--required-impressions", type=float, dest="required",
                        help="impressions the plan needs")
    parser.add_argument("--budget", type=float, help="flight budget, used with --cpm to derive impressions")
    parser.add_argument("--cpm", type=float, help="CPM, used with --budget to derive impressions")
    return parser


def derive_required(args: argparse.Namespace) -> float:
    if args.required is not None:
        return args.required
    if args.budget is not None and args.cpm is not None:
        if args.cpm <= 0:
            raise ValueError("--cpm must be greater than 0")
        return args.budget / args.cpm * 1000
    raise ValueError("provide --required-impressions, or both --budget and --cpm")


def main(argv: list[str]) -> int:
    parser = build_parser()
    if not argv:
        parser.print_help()
        return 0
    args = parser.parse_args(argv)
    if args.audience <= 0 or args.freq_cap <= 0:
        print("error: --audience and --freq-cap must be greater than 0", file=sys.stderr)
        return 2
    try:
        required = derive_required(args)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    max_deliverable = args.audience * args.freq_cap
    avg_freq_needed = required / args.audience
    feasible = required <= max_deliverable

    print(f"reachable audience:      {args.audience:,}")
    print(f"frequency cap:           {args.freq_cap:g} per user")
    print(f"required impressions:    {required:,.0f}")
    print(f"max deliverable at cap:  {max_deliverable:,.0f}")
    print(f"avg frequency to hit it: {avg_freq_needed:.2f} per user")
    if feasible:
        headroom = max_deliverable - required
        print(f"verdict: feasible. {headroom:,.0f} impressions of headroom under the cap.")
    else:
        shortfall = required - max_deliverable
        print(f"verdict: the cap starves delivery. Short by {shortfall:,.0f} impressions.")
        print("fix: raise the frequency cap, widen the audience, or lower the impression target.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
