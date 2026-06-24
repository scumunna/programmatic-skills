#!/usr/bin/env python3
"""Compare media buys on a common eCPM basis.

Buys priced on different models (CPM, CPC, CPA, CPCV) are not directly comparable.
Convert each to an effective CPM (eCPM, cost per 1000 impressions) so you can rank
lines on one axis. This is the "convert each to eCPM first" rule from the
programmatic-foundations skill.

Formulas:
  CPM:  eCPM = cpm
  CPC:  eCPM = cpc  * ctr        * 1000
  CPA:  eCPM = cpa  * ctr * cvr  * 1000
  CPCV: eCPM = cpcv * vcr        * 1000

Examples:
  ecpm_compare.py --model cpm  --cpm 5
  ecpm_compare.py --model cpc  --cpc 1.50 --ctr 0.002
  ecpm_compare.py --model cpa  --cpa 25   --ctr 0.002 --cvr 0.05
  ecpm_compare.py --model cpcv --cpcv 0.03 --vcr 0.70

No credentials and no network. Pure arithmetic.
"""

from __future__ import annotations

import argparse
import sys


def compute_ecpm(args: argparse.Namespace) -> float:
    """Return the effective CPM for the chosen model, or raise ValueError."""
    if args.model == "cpm":
        _require(args, ["cpm"])
        return args.cpm
    if args.model == "cpc":
        _require(args, ["cpc", "ctr"])
        return args.cpc * args.ctr * 1000
    if args.model == "cpa":
        _require(args, ["cpa", "ctr", "cvr"])
        return args.cpa * args.ctr * args.cvr * 1000
    if args.model == "cpcv":
        _require(args, ["cpcv", "vcr"])
        return args.cpcv * args.vcr * 1000
    raise ValueError(f"unknown model: {args.model}")


def _require(args: argparse.Namespace, names: list[str]) -> None:
    missing = [n for n in names if getattr(args, n) is None]
    if missing:
        raise ValueError(
            f"model '{args.model}' needs: {', '.join('--' + m for m in missing)}"
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a media buy to a common eCPM so lines can be compared.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Rates are fractions, not percents: a 0.2 percent CTR is --ctr 0.002.",
    )
    parser.add_argument("--model", required=True, choices=["cpm", "cpc", "cpa", "cpcv"],
                        help="the pricing model of the buy")
    parser.add_argument("--cpm", type=float, help="cost per 1000 impressions")
    parser.add_argument("--cpc", type=float, help="cost per click")
    parser.add_argument("--cpa", type=float, help="cost per action")
    parser.add_argument("--cpcv", type=float, help="cost per completed view")
    parser.add_argument("--ctr", type=float, help="click-through rate as a fraction (0.002 = 0.2 percent)")
    parser.add_argument("--cvr", type=float, help="conversion rate per click as a fraction")
    parser.add_argument("--vcr", type=float, help="video completion rate as a fraction")
    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    if not argv:
        parser.print_help()
        return 0
    args = parser.parse_args(argv)
    try:
        value = compute_ecpm(args)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(f"model: {args.model}")
    print(f"eCPM:  {value:.2f} (cost per 1000 impressions)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
