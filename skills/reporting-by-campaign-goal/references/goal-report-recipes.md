# Per-goal report recipes

The full recipe for each campaign objective. For each goal: the primary KPI set, the report type that surfaces it, the dimensions to slice by, the state of the art quality bar a strong report clears, and the common misread that sinks a weak one. Metric definitions and KPI math live in the `programmatic-foundations` skill. Build mechanics live in the `dv360-reporting` skill. Read these recipes top to bottom for one goal; do not mix KPIs across stages.

A note on platforms: the report-type column names the surface in the Google Marketing Platform stack (Display & Video 360 reporting, Campaign Manager 360, Google Analytics 4) because that is what the cited documentation covers. The KPI set, the dimensions, the quality bar, and the misread are platform-agnostic and carry to any DSP. In another DSP, find the equivalent surface and apply the same recipe.

## Awareness and brand

The goal is to reach the right people, enough times, in a seen ad, and to shift perception. Delivery metrics prove the ad got there; a lift study proves it mattered.

| Element | What to use |
| --- | --- |
| Primary KPIs | Unique reach (deduplicated people), on-target reach and on-target percentage, frequency distribution and average frequency, effective frequency band, viewability rate, video completion rate (VCR), and Brand Lift (Awareness, Ad recall, Consideration, Favorability) |
| Report type | Reach report for deduplicated reach and frequency; Cross-Media Reach to combine digital and linear TV; a Brand Lift study against an unexposed control for perception |
| Slice by | Audience or demographic, frequency bucket, device type, geo, creative. Reach reports require Country, Gender, and Age dimensions |
| State of the art bar | Reach reported as deduplicated and on-target, not gross and not summed. Frequency reported as a distribution with an effective-frequency judgment, not a bare average. Viewability read next to measurable rate. Perception proven by a controlled Brand Lift study with lifted users and absolute and relative lift, not inferred from impressions |
| Common misread | Declaring awareness success on impressions served and a high viewability rate, with no lift study, so perception change is assumed rather than measured. Second misread: summing reach across days or segments, which overcounts people |

Notes. Effective frequency (the exposure band where the message lands before it wastes, often cited around 3 to 10 and set by brand and creative) is a planning judgment, not a documented constant, so present it as best practice and set it per campaign. Frequency-cap mechanics live in `dv360-frequency-and-brand-safety`. Brand Lift design, response thresholds, and control-group protection live in `dv360-measurement-and-attribution`.

## Consideration and engagement

The goal is to earn interest: clicks that mean something, qualified visits, video views, and a measurable rise in intent. The trap is rewarding the click itself.

| Element | What to use |
| --- | --- |
| Primary KPIs | Click-through rate (CTR), engagement rate, qualified site visits or engaged sessions, video views and view rate (VTR), and Search Lift (the rise in branded search the campaign caused) |
| Report type | Standard report with engagement and video metrics for the media side; site analytics for qualified-visit and engagement events; a Search Lift study for branded-search intent |
| Slice by | Creative, placement or inventory, audience, device. For video, add the format and player environment |
| State of the art bar | The click is tied to a qualified outcome (a non-bounce visit, an engagement event, a video view milestone), not counted in isolation. View rate is read with the completion curve, not just starts. Intent lift is measured by a Search Lift study, not proxied from CTR |
| Common misread | Optimizing to CTR, which rewards clickbait creative that bounces on arrival. A high CTR with a high bounce rate is an overpromising ad, not a winning one. Read CTR next to the qualified-visit rate it produced |

Notes. Video view rate and completion are surfaced in the video and YouTube reports; YouTube and partners line items carry the TrueView view, view rate, and cost-per-view set, which a standard report does not fully carry. The path from a click to an on-site action, and where it deduplicates against a conversion, is in `path-to-conversion-analysis`.

## Performance and conversion (direct response)

The goal is the action, efficiently, and the conversions must be real, not coincidental. This is the stage where incrementality and attribution-model choice decide the read.

| Element | What to use |
| --- | --- |
| Primary KPIs | Conversions (post-click and post-view, kept separate), cost per acquisition (CPA), return on ad spend (ROAS), conversion rate (CVR), conversion lag (time to convert), attribution-model comparison (last-click versus data-driven), and incremental conversions |
| Report type | Conversion report by line item and creative for counts and efficiency; an attribution-model comparison to see how credit shifts; a Conversion Lift experiment (or an event-level lift analysis) for the incrementality read |
| Slice by | Line item, creative, audience, device, conversion type or Floodlight activity. Add conversion lag as a distribution, not a single average |
| State of the art bar | CPA and ROAS judged against the media-plan target, never across line items on different goals. Post-click and post-view split. Conversion lag checked before judging a fresh campaign. Budget decisions led by incremental conversions, with last-click and data-driven compared rather than trusting either alone |
| Common misread | Reporting platform last-click ROAS as the whole truth and never testing incrementality, so the campaign gets credit for conversions that would have happened anyway. Second misread: collapsing post-click and post-view into one number, which overstates view-through credit |

Notes. Floodlight setup, counting methods, lookback windows, and attribution-model mechanics live in `dv360-measurement-and-attribution`. The multi-touch path, assists, and time lag read live in `path-to-conversion-analysis`. Build a custom or event-level incrementality and attribution model in `dv360-advanced-analytics-adh`.

## Retention and loyalty

The goal is to keep and re-engage customers, and to grow their value over time. The DSP does not have a concept of a returning customer, so this almost always means leaving DSP delivery reporting.

| Element | What to use |
| --- | --- |
| Primary KPIs | Repeat conversion or repeat purchase rate, returning-user retention by cohort, and lifetime-value proxies (lifetime revenue, predicted value, lifetime engagement) |
| Report type | Cohort exploration keyed to an acquisition date for retention and repeat rate; user-lifetime analysis for the value proxy; segment-level analysis joining first-party value to exposure when the question needs it. These live in site analytics or event-level analysis, not the DSP |
| Slice by | Cohort by acquisition date, new versus returning, audience segment, and where available a value band (loyalty tier, predicted-value decile) |
| State of the art bar | Retention read as a cohort curve keyed to when users were acquired, not as a flat returning-user count. Lifetime value treated as a proxy and stated as such, with the model named. Segment value joined to ad exposure through privacy-safe, aggregated analysis, never user-level rows pulled out |
| Common misread | Trying to read retention or lifetime value from DSP delivery reporting, which has neither. Second misread: reporting a single lifetime-value number with no cohort or model behind it, which is unfalsifiable |

Notes. Lifetime-value and segment-value work that joins first-party data to ad logs is a privacy-safe, event-level task; route it to `dv360-advanced-analytics-adh`. Cohort and user-lifetime explorations are Google Analytics 4 surfaces. The DSP can still inform retention indirectly by feeding a returning-customer audience back into targeting, which is a `dv360-targeting-and-audiences` task, not a reporting one.

## Reach and frequency planning

The goal is to size and shape a buy before it runs: how much net reach a budget buys, where the reach curve flattens, and what frequency cap maximizes net reach for the spend. This is forecasting, not in-flight reporting.

| Element | What to use |
| --- | --- |
| Primary KPIs | Forecast unique reach, the reach curve (reach as a function of impressions or budget), on-target percentage, and frequency at the point of saturation |
| Report type | Planning and forecast tools for pre-launch sizing; a modeled reach curve for the saturation point. After launch, the Reach report validates the forecast against delivered reach |
| Slice by | Frequency-cap scenario, audience, channel mix, geo. Compare scenarios side by side rather than reading one in isolation |
| State of the art bar | Reach planned on-target, not gross. The cap chosen at the point where the reach curve flattens, so spend stops buying frequency it does not need. The forecast validated against delivered reach after launch, not filed and forgotten |
| Common misread | Planning to gross reach and ignoring on-target percentage, so the plan looks bigger than the audience it actually reaches. Second misread: setting a frequency cap by habit rather than from the curve, leaving spend buying an over-exposed tail |

Notes. Building the reach curve and finding the optimal frequency from event-level logs is an `dv360-advanced-analytics-adh` task when the planning tools cannot express it. Setting the cap once the number is known is `dv360-frequency-and-brand-safety`.

## Pacing plus performance (combined view)

The goal is one view that answers "are we on pace, and is the pace producing the goal KPI", so delivery and outcome are read together rather than in two disconnected reports.

| Element | What to use |
| --- | --- |
| Primary KPIs | Pace against the flight (spend and impressions delivered versus planned, time elapsed versus budget elapsed) shown next to the goal KPI for the campaign (CPA and ROAS for performance, reach and frequency for awareness, qualified visits for consideration) |
| Report type | A delivery report joined to the goal KPI in a single view, by date and line item. Scheduled when it is a recurring stakeholder deliverable |
| Slice by | Date and line item for the pace, plus the one dimension the goal KPI is read on. Resist adding more, because a combined view buries fast |
| State of the art bar | Pace and the goal KPI in the same frame, so a campaign that is on pace but missing the KPI (or hitting the KPI while under-pacing) is visible at a glance. A target line on both axes, so being on pace is judged against plan, not against itself |
| Common misread | Reading pace alone and calling a campaign healthy because it is spending on time, while the goal KPI is failing. On pace is not the same as on target. Second misread: cramming every dimension into the combined view until neither the pace nor the KPI is legible |

Notes. Pacing modes, under and over-delivery diagnosis, and the pacing math live in `dv360-pacing-and-optimization`. Scheduling a recurring combined report, and the warning that undownloaded scheduled reports deactivate, live in `dv360-reporting`.

## How to use these recipes

1. Identify the objective and read only that recipe. Do not borrow KPIs from an adjacent stage, because that is the most common way a report ends up answering the wrong question.
2. Take the primary KPI set as the columns, the slice-by list as the rows, and the report type as the surface to build in. Build mechanics are in `dv360-reporting`.
3. Hold the result against the state of the art bar before sharing it. If it does not clear the bar, the report is built but not yet trustworthy.
4. Watch for the common misread named in the recipe. Each one is the specific way a competent-looking report for that goal misleads.

## Sources

- Reach reports, Display & Video 360 Help: https://support.google.com/displayvideo/answer/6170584 (as of June 2026)
- Cross-Media Reach reporting, Display & Video 360 Help: https://support.google.com/displayvideo/answer/13955444 (as of June 2026)
- On-target reach, Display & Video 360 Help: https://support.google.com/displayvideo/answer/9545617 (as of June 2026)
- Set up Brand Lift measurement, Display & Video 360 Help: https://support.google.com/displayvideo/answer/9570506 (as of June 2026)
- Set up Search Lift measurement, Display & Video 360 Help: https://support.google.com/displayvideo/answer/15001171 (as of June 2026)
- Set up Conversion Lift measurement, Display & Video 360 Help: https://support.google.com/displayvideo/answer/16804790 (as of June 2026)
- Report on video campaigns, Display & Video 360 Help: https://support.google.com/displayvideo/answer/3521206 (as of June 2026)
- Report on YouTube and partners line items, Display & Video 360 Help: https://support.google.com/displayvideo/answer/6274610 (as of June 2026)
- About Active View, Display & Video 360 Help: https://support.google.com/displayvideo/answer/3214556 (as of June 2026)
- Metrics in reports, Display & Video 360 Help: https://support.google.com/displayvideo/table/3187025 (as of June 2026)
- Cohort exploration, Google Analytics 4 Help: https://support.google.com/analytics/answer/9670133 (as of June 2026)
- User lifetime exploration, Google Analytics 4 Help: https://support.google.com/analytics/answer/9947257 (as of June 2026)
- Key event attribution models report, Google Analytics 4 Help: https://support.google.com/analytics/answer/10596865 (as of June 2026)
