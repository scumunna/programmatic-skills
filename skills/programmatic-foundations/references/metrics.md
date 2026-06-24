# KPI and auction formulas

The canonical math for this library. Other skills reference these formulas instead of
restating them. Each row gives the formula and what the number actually tells you so an agent
can both compute and interpret it. Currency cancels as long as cost and revenue use the same
unit. Watch the per-mille (1,000) factor on CPM and eCPM.

## Rate and efficiency metrics

| Metric | Formula | What it tells you |
| --- | --- | --- |
| CPM (cost per mille) | (cost / impressions) x 1000 | Price to serve 1,000 impressions. The base buying price. Compare against floors and benchmarks. |
| CPC (cost per click) | cost / clicks | Price per click. Efficiency for click-driven goals; meaningless if clicks are not the objective. |
| CPA (cost per acquisition) | cost / conversions | Price per conversion. The core lower-funnel efficiency number; compare to target CPA and margin. |
| CTR (click-through rate) | clicks / impressions | Share of impressions that drew a click. Creative and relevance signal, not a conversion signal. A high CTR with low CVR points at curiosity clicks or a broken landing path. |
| CVR (conversion rate) | conversions / clicks | Share of clicks that converted. Landing-page and audience quality. Pair with CTR to locate where the funnel leaks. |
| VCR (video completion rate) | completed views / video starts (impressions) | Share of video plays that ran to 100 percent. Attention and creative-length signal for video and CTV. |
| CPCV (cost per completed view) | cost / completed views | Price per full video view. The efficiency KPI for completion-priced video. |
| eCPM (effective CPM) | (total cost / total impressions) x 1000 | Normalizes any buy (CPC, CPA, CPCV, deal) back to a CPM so you can compare line items on one axis. The universal translator. |
| ROAS (return on ad spend) | revenue / cost | Revenue per unit of spend (often stated as a multiple or percent). The value-based north star; needs reliable revenue from conversion tracking. |

## Delivery and auction metrics

| Metric | Formula | What it tells you |
| --- | --- | --- |
| Win rate | impressions won / bids submitted | Share of auctions entered that you won. Low win rate points at bid price, floors, or deal access, not at targeting size. |
| Viewability rate | viewable impressions / measurable impressions | Share of measurable impressions that met the viewability standard. Always read it next to measurable rate, because a great viewability rate on a tiny measurable base is noise. |
| Measurable rate | measurable impressions / total impressions | Share of impressions a viewability vendor could actually measure. Low measurable rate (heavy iframes, unsupported environments) caps how much you can trust the viewability rate. |

Notes that catch people:

- Win rate uses bids submitted as the denominator, not bid requests received. A line item can
  see millions of requests, bid on few, and still show a high win rate. To diagnose scale,
  look at bid rate (bids / requests) separately.
- Viewability rate and measurable rate are a pair. Optimize measurable rate first; you cannot
  improve what you cannot measure.
- CTR and CVR answer different questions. Moving CTR is a creative and targeting job; moving
  CVR is a landing-page, offer, and audience-quality job.
- eCPM is the comparison tool. When line items buy on different models, convert each to eCPM
  before judging which is cheaper.

## The funnel and the KPI that matters at each stage

Match the KPI to the objective. Judging an awareness line item on CPA, or a conversion line
item on reach, is the most common way to optimize toward the wrong thing.

| Stage | Goal | Primary KPIs | What to ignore here |
| --- | --- | --- | --- |
| Awareness | Be seen by the right people at scale | Reach, CPM, viewability rate, VCR | CPA and ROAS (too few conversions to be stable; chasing them starves reach) |
| Consideration | Earn active interest and on-site engagement | CTR, site visits, engagement rate, dwell, video quartiles | Raw impression volume (cheap impressions that do not engage flatter the buy) |
| Conversion | Drive the action efficiently | CPA, ROAS, CVR | Reach (you want the right user, not the most users) |
| Retention | Keep and re-engage existing customers | Repeat conversion rate, CPA on retained segments, frequency control | Broad prospecting reach (you are talking to a known list; cap frequency and suppress converters) |

How to use this in practice:

1. Read the objective before the metrics. The objective names the primary KPI; everything
   else is a guardrail or a diagnostic.
2. Keep one or two guardrails per stage (for example viewability on an awareness buy, or
   frequency on retention) so optimizing the primary KPI does not quietly break quality.
3. When a stakeholder cites a metric from the wrong row (CTR as proof a brand campaign
   worked), reframe to the stage-appropriate KPI and explain the mismatch.

## Worked examples

Numbers chosen to be checkable by hand.

- A line item spends 5,000 and serves 2,000,000 impressions. CPM = (5,000 / 2,000,000) x
  1000 = 2.50.
- It drives 8,000 clicks and 200 conversions. CTR = 8,000 / 2,000,000 = 0.4 percent.
  CVR = 200 / 8,000 = 2.5 percent. CPA = 5,000 / 200 = 25.00.
- Those 200 conversions return 30,000 in revenue. ROAS = 30,000 / 5,000 = 6.0 (600 percent).
- A video line spends 3,000 for 600,000 starts and 360,000 completes. VCR = 360,000 /
  600,000 = 60 percent. CPCV = 3,000 / 360,000 = 0.0083.
- It submitted 4,000,000 bids and won 2,000,000. Win rate = 2,000,000 / 4,000,000 = 50
  percent. Of impressions, 1,800,000 were measurable and 1,260,000 viewable. Measurable rate
  = 1,800,000 / 2,000,000 = 90 percent. Viewability rate = 1,260,000 / 1,800,000 = 70 percent.

## See also

- Term definitions behind these metrics: `glossary.md` in this skill.
- Pulling and reading these in DV360: `dv360-reporting`.
- Diagnosing a bad win rate or viewability number: `dv360-troubleshooting`.
- Revenue, ROAS, and attribution plumbing: `dv360-measurement-and-attribution`.
