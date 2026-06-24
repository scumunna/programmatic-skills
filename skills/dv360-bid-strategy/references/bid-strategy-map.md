# Bid strategy map

Load-on-demand companion to the `dv360-bid-strategy` SKILL.md. Use this when picking a specific
strategy or setting one through the DV360 API or Structured Data Files. The SKILL.md has the
decision logic; this file maps each strategy to its goal, applicable line item types, and the
matching API v4 field.

## The three top-level strategy objects (DV360 API v4)

The line item carries one `bidStrategy`, which is one of three mutually exclusive schemes:

| Object | What it does | Set the price how |
| --- | --- | --- |
| `fixedBid` | Uses a predetermined bid amount | You set the bid (micros of advertiser currency) |
| `maximizeSpendAutoBid` | Adjusts the bid to optimize a performance goal while spending the full budget | Volume-first; you pick the goal type |
| `performanceGoalAutoBid` | Adjusts the bid to meet or beat a specified performance goal | Efficiency-first; you set the goal amount |

## Fixed bidding

| Strategy | Goal | Use when |
| --- | --- | --- |
| Fixed CPM | None; you control the bid | Low conversion data, reserved/PG fixed-rate deals, hard CPM control, small scale, reach/brand |

Notes:
- The bid you set determines how much DV360 can spend to win any single impression.
- Optimized fixed bidding is on by default to avoid overpaying; opt out to send the exact bid.

## Automated bidding: maximize while spending the full budget

These map to `maximizeSpendAutoBid` with a performance goal type. Volume-first.

| Strategy (UI intent) | Optimizes for | Applies to | API goal type |
| --- | --- | --- | --- |
| Maximize KPI / spend full budget | Most of the chosen KPI for the budget | Display, video | varies by chosen goal |
| Maximize conversions | Conversion volume | Display, video | CPA-oriented |
| Maximize conversion value | Total conversion value | Value-eligible line items | value-oriented |
| Completed in-view and audible impressions | CIVA | Video | `CIVA` |
| Impressions viewable for at least 10 seconds | In-view time over 10s | Video | `IVO_TEN` |
| Viewable impressions | Viewability | Display, video | `AV_VIEWED` |
| Optimized reach | Reach | Connected TV | `REACH` |
| Maximize installs | App installs | App install line items | install-oriented |

## Automated bidding: prioritize a target (goal-constrained)

These map to `performanceGoalAutoBid`. Efficiency-first; you set the target amount.

| Strategy | Optimizes for | API goal type |
| --- | --- | --- |
| Target CPA (minimize/meet CPA) | Cost per action | `CPA` |
| Target / minimize CPC | Cost per click | `CPC` |
| Target viewable CPM | Cost per thousand viewable impressions | `VIEWABLE_CPM` |
| Custom (algorithm) | Your custom score | `CUSTOM_ALGO` (set `customBiddingAlgorithmId`) |

`performanceGoalAutoBid` supports custom bidding: when the goal type is the custom-algorithm
type, it references a `customBiddingAlgorithmId`. Build that algorithm in `dv360-custom-bidding`.

## Value-based bidding

Target ROAS and maximize conversion value are value-based strategies. They consider the value
that different Floodlight activities carry for the business, so Floodlight value reporting must
be configured. Availability is narrower than standard goals (for example YouTube video action
and Demand Gen line items), and they require a minimum conversion history before they qualify.
After switching to a value-based strategy, hold the campaign unchanged through the recommended
no-change window so the strategy can calibrate.

## Performance goal type enum (DV360 API v4)

`BiddingStrategyPerformanceGoalType` values seen in the v4 reference:

- `CPA` (cost per action)
- `CPC` (cost per click)
- `VIEWABLE_CPM`
- `CUSTOM_ALGO`
- `CIVA` (completed in-view and audible)
- `IVO_TEN` (in-view over 10 seconds)
- `AV_VIEWED` (viewable impressions)
- `REACH`

When setting strategies in bulk through Structured Data Files or the API, encode the goal type
exactly and keep it stable. Changing it resets the learning period (see SKILL.md). For the
field-level API and SDF automation, hand off to `dv360-api-and-sdf-automation`.

## Sources

- [Automated bid strategies](https://support.google.com/displayvideo/answer/2997422?hl=en) (as of June 2026)
- [Value based bidding strategies](https://support.google.com/displayvideo/answer/14161766?hl=en) (as of June 2026)
- [Set a fixed CPM bid for a line item](https://support.google.com/displayvideo/answer/2696858?hl=en) (as of June 2026)
- [BiddingStrategy, DV360 API v4 reference](https://developers.google.com/display-video/api/reference/rest/v4/BiddingStrategy) (as of June 2026)
- [advertisers.lineItems, DV360 API v4 reference](https://developers.google.com/display-video/api/reference/rest/v4/advertisers.lineItems) (as of June 2026)
