---
name: stackadapt-reporting-and-attribution
description: Read StackAdapt performance and tie it to conversions. Use when the user asks about StackAdapt reporting, the StackAdapt dashboard, exportable reports, which StackAdapt metrics matter, StackAdapt conversion tracking, the StackAdapt universal or conversion pixel, UTM and event setup, view-through vs click-through conversions, cross-channel attribution, or the StackAdapt reporting REST API.
---

# StackAdapt reporting and attribution

Turn StackAdapt delivery into a performance read that ties spend to conversions. This skill
covers the dashboards and exportable reports, the metrics that matter by goal, conversion
tracking through the StackAdapt pixel, UTM and event setup, and the attribution approach
(view-through and click-through across channels). The job is to answer "what happened, and did
it drive conversions" with numbers you can defend.

StackAdapt is a self-serve multi-channel demand-side platform (native, display, video, connected
TV, audio, in-app, digital out-of-home). For KPI definitions and shared math (CTR, CPA, ROAS,
viewability), see the `programmatic-foundations` skill. For which metrics a given objective should
be judged on, see `reporting-by-campaign-goal`. For multi-touch path and sequencing analysis, see
`path-to-conversion-analysis`. For the campaign build that these reports measure, see
`stackadapt-campaign-setup`, and for how supply choices show up in the numbers, see
`stackadapt-inventory-and-brand-safety`.

## When to use this skill

- "Pull a StackAdapt report." / "Show me the StackAdapt dashboard." / "Export performance."
- "Which StackAdapt metrics actually matter for this goal?"
- "Set up StackAdapt conversion tracking." / "Install the pixel." / "Add a conversion event."
- "Set up UTMs for StackAdapt." / "Why are my conversions not showing?"
- "View-through vs click-through on StackAdapt." / "How does StackAdapt attribution work?"
- "Is there a StackAdapt reporting API?"

Boundaries with sibling skills:
- Definitions and KPI formulas: `programmatic-foundations`.
- Goal-to-metric mapping and report recipes by objective: `reporting-by-campaign-goal`.
- Multi-touch path, sequencing, and assist analysis: `path-to-conversion-analysis`.
- Acting on what the report says (bids, budgets, fixing under-delivery): `stackadapt-optimization-and-troubleshooting`.
- Pulling reporting data by API at scale: `stackadapt-api-and-automation`.

## Quick reference

Where to read performance, in order of effort:

| Surface | Use it for | Notes |
| --- | --- | --- |
| In-platform dashboard | Real-time, at-a-glance, day-to-day monitoring | Customizable; programmatic and email in one view |
| Exportable reports | Sharing, deeper slices, scheduled delivery | Break out by dimension (campaign, ad group, creative, domain, geo, day) |
| Reporting REST API | Automated, recurring pulls into your own stack | Read-only; returns spend and effectiveness by dimensions and metrics |

Conversion tracking pieces:

| Piece | What it does |
| --- | --- |
| Universal pixel | One site-wide pixel that records visits and powers retargeting and attribution |
| Conversion event | A tracked action (purchase, form fill, newsletter signup) fired on the right page |
| Custom pixel parameters | Extra values passed in: revenue, order value, item ID, SKU, number of products, cart value |
| UTM parameters | Tag click destinations so non-StackAdapt channels show up in the conversion path |
| Pixel API (server-to-server) | Send conversions and build audiences without a site pixel |

Attribution at a glance: StackAdapt credits both view-through (impression-led) and click-through
conversions, joins its own impression and click data to site activity by shared identifiers, and
represents non-StackAdapt channels through UTM-tagged click activity. Last-touch gives all credit
to the final touch; multi-touch accounts for the touches before it.

## Core process

1. Confirm tracking is live before you trust any conversion number. The universal pixel must be on
   the site, the conversion events must fire on the right pages, and any revenue or order values
   must be passed as parameters. A conversion-optimized campaign with no live events has nothing to
   report and nothing to learn from.
2. Pick the surface for the question. Day-to-day monitoring lives in the dashboard; a stakeholder
   deliverable or a deeper slice is an exportable report; a recurring automated feed is the
   reporting REST API. Do not export by hand what a scheduled report or the API can deliver on a
   cadence.
3. Read the metrics that match the goal, not every metric. Awareness and CTV read impressions,
   reach, unique households, frequency, completion rate, CPM, and CPCV; consideration reads clicks,
   CTR, CPC, and engagement; performance reads conversions, conversion rate, CPA, and ROAS. Get the
   goal-to-metric mapping from `reporting-by-campaign-goal` and the formulas from
   `programmatic-foundations`.
4. Separate view-through from click-through conversions. Read them as distinct columns, never
   summed blind. View-through is essential for clickless channels like CTV, but it overstates
   credit if you treat it like a click. Hold the view-through window constant when comparing
   periods or campaigns so the comparison is fair.
5. Bring in non-StackAdapt channels with UTMs. Tag every click destination consistently across
   paid and owned channels (search, social, email) so the conversion path shows where StackAdapt
   views and clicks sat alongside other channels' UTM-tracked clicks. Inconsistent UTMs are the
   most common reason a path looks broken.
6. Choose the attribution lens for the question. Use last-touch for a simple, conservative "what
   closed" read; use multi-touch when you need to value the touches that set up the conversion.
   StackAdapt's cross-channel attribution surfaces programmatic's influence directly. For deep
   sequencing and assist analysis, hand off to `path-to-conversion-analysis`.
7. Slice to find the lever, then hand off the action. Break performance by ad group, creative,
   domain, geo, device, and day to locate what is working and what is wasting spend. Reporting
   ends at the finding; the change (bid, budget, creative, supply) belongs to
   `stackadapt-optimization-and-troubleshooting`.

## Decision rules and thresholds

- No tracking, no conversion read. Verify the universal pixel and events are live before reporting
  on or optimizing toward conversions. If events are missing, fixing tracking is the first task,
  not interpreting noise.
- Report on the goal's metrics only. An awareness CTV buy judged on CPA, or a performance buy
  judged on impressions, produces the wrong decision. Map metrics to the objective first.
- View-through and click-through stay separate. Read them in distinct columns. Lean on
  view-through for CTV and other clickless inventory; discount it for lower-funnel claims where a
  click is the stronger signal.
- Hold the attribution window constant across comparisons. Changing the view-through window
  between periods or campaigns invalidates the comparison. Pick a window, state it, keep it.
- Last-touch for "what closed," multi-touch for "what contributed." Pick the lens to fit the
  question rather than defaulting to one. Roughly half of conversion journeys touch more than one
  channel, so last-touch alone undercredits upper-funnel and cross-channel work.
- UTMs must be consistent or the cross-channel path breaks. Standardize source, medium, and
  campaign tags across every channel before trusting a multi-channel report.
- Automate recurring pulls. If the same report goes out on a cadence, schedule it or use the
  read-only reporting REST API instead of exporting by hand. Hand the API build to
  `stackadapt-api-and-automation`.

## Reporting REST API

StackAdapt exposes a read-only REST API that returns reporting data broken out by dimensions and
metrics to understand a campaign's spend and effectiveness. Use it for recurring, automated pulls
into a warehouse or a BI tool rather than manual exports. Note that REST write operations are
deprecated; creating or managing campaigns goes through the GraphQL API, and conversions can be
sent server-to-server through the Pixel API. Read credentials from environment variables, never
hardcode a token, and keep the integration in `stackadapt-api-and-automation`. Confirm current
dimensions, metrics, authentication, and rate limits in the developer docs before building.

## Templates and examples

A monthly performance read for a native consideration plus CTV awareness campaign:

```
Report: ACME_2026Q3_July_Performance
  Surface:   Scheduled export (stakeholder deck) + dashboard for daily checks
  Window:    Click-through 30 days, view-through 1 day, held constant vs June

  Native consideration ad group (goal: traffic / engagement)
    Read:    Impressions, clicks, CTR, CPC, engagement rate, spend
    Conv:    Click-through conversions (form fills), conversion rate, CPA
    Slice:   By creative and by domain to find winners and waste

  CTV awareness ad group (goal: awareness / reach)
    Read:    Impressions, unique households, reach, frequency, completion rate, CPM, CPCV
    Conv:    View-through conversions ONLY (CTV is clickless), reported separately
    Note:    Do not sum view-through into the native click-through totals

  Cross-channel:
    UTMs:    Consistent source/medium/campaign across StackAdapt, search, social, email
    Lens:    Last-touch for "what closed"; multi-touch when valuing CTV/native assists
    Deep:    Sequencing + assists -> hand to path-to-conversion-analysis
```

Why it is built this way: each ad group is read on its own goal's metrics, so the CTV buy is
judged on reach and completion and view-through rather than CPA; view-through is kept in its own
column and never folded into the native click-through totals; the windows are stated and held
constant against the prior month so the comparison is fair; and UTM consistency is called out
because without it the cross-channel path falls apart.

## Common pitfalls

- Reporting conversions before the pixel and events are verified live. Numbers exist but mean
  nothing. Confirm tracking first.
- Summing view-through and click-through into one conversion number. They are different signals;
  blending them overstates credit, especially for CTV view-through.
- Changing the attribution window between periods and comparing anyway. Hold it constant or the
  trend is an artifact of the window, not the campaign.
- Judging every campaign on the same metrics. Read awareness on reach and completion, performance
  on CPA and ROAS. Map metrics to the goal with `reporting-by-campaign-goal`.
- Inconsistent or missing UTMs, then wondering why other channels do not appear in the path.
  Standardize tags across all channels first.
- Exporting the same report by hand every week. Schedule it, or pull it from the read-only
  reporting REST API via `stackadapt-api-and-automation`.
- Stopping at the number instead of the action, or acting inside this skill. Reporting finds the
  lever; pulling it (bid, budget, creative, supply) belongs to
  `stackadapt-optimization-and-troubleshooting`.

## Sources

- [StackAdapt Developer Documentation (REST, GraphQL, Pixel API, Data Taxonomy, MCP Server)](https://docs.stackadapt.com) (as of June 2026)
- [The AI-Powered Marketing Platform (campaign analysis and reporting) | StackAdapt](https://www.stackadapt.com/campaign-analysis) (as of June 2026)
- [What is cross-channel attribution? An in-depth guide for marketers | StackAdapt](https://www.stackadapt.com/resources/blog/cross-channel-attribution) (as of June 2026)
- [Conversion Journey: The Key to Understanding Your Customers | StackAdapt](https://www.stackadapt.com/resources/blog/tracking-conversion-journey) (as of June 2026)
- [CTV measurement: metrics and KPIs you should track | StackAdapt](https://www.stackadapt.com/resources/blog/ctv-measurement) (as of June 2026)

The exact in-product steps for installing the universal pixel, defining conversion events and
their parameters, configuring UTM handling, setting attribution windows, and building or
scheduling exports are documented in the StackAdapt help center at support.stackadapt.com. Some
help center articles require a logged-in account, so they are not cited here. Where a specific
in-product default, field name, or attribution-window value is not publicly documented, the
guidance above states the operational best practice and points to the help center and the
developer docs rather than citing a fabricated page.
