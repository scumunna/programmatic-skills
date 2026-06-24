# Structure decision tables

Load-on-demand companion to the `dv360-campaign-architecture` SKILL.md. Use these when laying
out a real media plan. The SKILL.md has the summary rules; this file has the full checklists,
a worked plan, and the naming cheat sheet.

## Insertion order split checklist

Work down the list. Any "yes" means the slice needs its own insertion order, because the IO
is the only level that carries a budget, a flight, pacing, and a KPI.

| Question | If yes, split because |
| --- | --- |
| Does this slice have its own budget that must not be shared? | Line items in one IO share its budget pool |
| Does it run on different start/end dates? | Line items in one IO share the IO flight |
| Is it a different funnel stage (awareness / consideration / conversion)? | Different KPI and budget per stage |
| Is it a different market or geo with independent budget/reporting? | Independent pacing and finance lines |
| Is it a different channel or format family (display / video / CTV / audio)? | Different benchmarks, viewability, pacing behavior |
| Is it a different buying type (open auction vs PG/PMP)? | Reserved/guaranteed deals are fixed commitments and fixed price |
| Does it need a different bid strategy / optimization goal at the IO level? | One IO goal should not constrain another |
| Does it use a different verification or brand-safety vendor? | Cost and reporting attach per IO |
| Does finance or the client need a clean budget line for it? | Reporting clarity |

## Line item split checklist

Any "yes" means a separate line item, because the line item is the unit you target, bid,
optimize, and report on.

| Question | If yes, split because |
| --- | --- |
| Different audience strategy (prospecting vs retargeting, distinct segments)? | Bids and budgets should not bleed across intent |
| Different creative set, message, or offer? | A line item serves its assigned creatives |
| Different format or size you want to read or pace apart? | Format-level performance visibility |
| Different device (mobile / desktop / CTV / tablet)? | Device-level bids and creatives |
| Different frequency rule or exposure goal? | Per-slice frequency control |
| A distinct optimization axis or test cell? | Isolate the variable you are acting on |
| A specific deal you want controlled apart from open auction? | Deal delivery and pricing visibility |

Counter-rule: do not split where you will not act on the difference. Each extra line item
divides conversion volume, and thin volume starves automated bidding. If two cells would
always share bid, targeting, and creative, keep them in one line item.

## Worked plan: regulated retailer, two markets, full funnel

Plan inputs: one advertiser, two markets (US, CA), three funnel stages, a mix of open auction
and one PMP deal for premium CTV, separate budgets per market and stage.

```
Advertiser: ACME (Floodlight from CM360 at advertiser level)

  IO  ACME_US_DISPLAY_Awareness_UpperFunnel_2026Q3      budget A | even pacing | viewable CPM goal
      LI  ..._Prospecting_300x250_2026Q3
      LI  ..._Prospecting_728x90_2026Q3

  IO  ACME_US_CTV_Consideration_MidFunnel_2026Q3         budget B | even pacing | CPCV goal
      LI  ..._OpenAuction_15s_2026Q3
      LI  ..._PMPDeal_Premium_30s_2026Q3                 deal isolated from open auction

  IO  ACME_US_DISPLAY_Conversion_LowerFunnel_2026Q3      budget C | even pacing | tCPA goal
      LI  ..._Retargeting_300x250_2026Q3

  IO  ACME_CA_DISPLAY_Awareness_UpperFunnel_2026Q3       budget D | even pacing | viewable CPM goal
      LI  ..._Prospecting_300x250_2026Q3
```

Reasoning trace:
- US and CA are separate IOs: independent budgets and reporting.
- Awareness, consideration, and conversion are separate IOs: different KPIs and budgets.
- Display and CTV are separate IOs: different benchmarks and pacing.
- The PMP deal is its own line item inside the CTV IO: deal pricing and delivery stay visible
  and controllable, separate from the open auction line item next to it.
- Sizes are separate line items only where the team will read or pace them apart.

## Naming field cheat sheet

Order: client, market, channel, objective, funnel stage, [audience], [format], flight.

| Field | Example values | Notes |
| --- | --- | --- |
| client | ACME | Short, fixed per advertiser |
| market | US, CA, UK, EMEA | Controlled vocabulary, ISO-style codes |
| channel | DISPLAY, OLV, CTV, AUDIO | Fixed channel codes |
| objective | Awareness, Consideration, Conversion | Maps to funnel stage |
| funnel stage | UpperFunnel, MidFunnel, LowerFunnel | Redundant with objective but aids filtering |
| audience (LI only) | Prospecting, Retargeting | Line item level |
| format (LI only) | 300x250, 15s, 30s | Line item level |
| flight | 2026Q3, 2026-07 | Consistent date format |

Rules that keep automation working:
- One delimiter everywhere (underscore recommended). Never mix delimiters.
- No commas, no special characters, no leading/trailing spaces. CSV-based SDF round-trips and
  report filters break on them.
- Same fields, same order, on every object so a wildcard filter isolates an exact slice.
- Controlled vocabulary only. Free text defeats filtering. Ownership of that vocabulary lives
  in `dv360-account-setup-and-taxonomy`.
