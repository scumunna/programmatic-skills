# State of the art reporting practices

The cross-cutting practices that separate an expert report from a competent-looking one, in depth. These apply across every objective and every DSP. Use them to build a report to the bar, to explain why a practice matters, or to audit an existing report. Where a practice is industry best practice rather than a single documented page, it is labeled as best practice and carries no fabricated citation.

## 1. Deduplicated cross-channel reach, not summed reach

The problem. Reach is a count of distinct people. A person reached on mobile and on desktop, or in two line items, or on two days, is one person, not two. Reporting surfaces model and deduplicate reach across devices using statistical methods, so the reach number is not the arithmetic sum of impressions or of daily or per-segment rows.

The practice. Read reach at the grain you need it from a reach surface that deduplicates, and never add reach rows together. To combine digital and linear TV into one audience number, use Cross-Media Reach, which reports incremental and deduplicated reach across channels with third-party TV data, so you can see what TV and digital each add to the other rather than double-counting the overlap. Cross-Media Reach runs on a window of about 92 days with data over the trailing 24 months and is single-advertiser.

The failure it prevents. A "total reach" built by summing campaign-level or daily reach overstates the audience, sometimes by a large multiple, and makes a campaign look like it reached more distinct people than it did. Every reach decision built on that number (frequency, incremental budget, saturation) is then wrong.

Where the mechanics live: reach report construction and the required Country, Gender, and Age dimensions in `dv360-reporting`; reach and co-viewing methodology in `dv360-measurement-and-attribution`; event-level deduplicated reach across campaigns in `dv360-advanced-analytics-adh`.

## 2. On-target percentage, not just gross reach

The problem. Gross reach counts everyone the ad touched, on-target or not. Digital targeting is imprecise, so even a tightly targeted campaign buys impressions outside the intended demographic. A campaign can post large gross reach while wasting a meaningful share of it on people outside the target.

The practice. Report on-target reach (the estimated people who actually match the target demographic) and on-target percentage (on-target reach over the target-demographic population). On-target percentage is the honest measure of whether the buy reached the audience that was bought. The denominator can be defined against a census, digital, TV, or YouTube population, so state which denominator you used.

The failure it prevents. Optimizing and reporting on gross reach rewards cheap, off-target inventory that inflates the headline number while missing the audience. On-target percentage exposes media, channels, and data partners that deliver volume but not the right people.

Where the mechanics live: on-target reach and percentage definitions in `dv360-measurement-and-attribution` and `dv360-reporting`; the planning view of on-target percentage in the reach and frequency planning recipe.

## 3. Incrementality and lift over last-click

The problem. Last-click (and last-touch generally) credits the conversion to whatever the user touched last, and counts every conversion on a converting path, including the ones that would have happened with no ad at all. A retargeting line item that serves to people already heading to checkout will post a glorious last-click ROAS while causing very little.

The practice. Measure incrementality with a controlled experiment: a Conversion Lift study that splits the audience into a treatment group that can see the ads and a control group that cannot (shown the next-auction ad instead), then reports the conversions the ads actually caused rather than those that merely co-occurred. Where a packaged lift product does not fit, build the lift analysis from event-level data with a holdout. For budget decisions, lead with incremental conversions and treat last-click as a directional diagnostic, not as truth. Compare attribution models (last-click versus data-driven) to see how credit shifts, which exposes where last-click underprices upper-funnel work, but understand that even data-driven attribution is correlational; only an experiment isolates cause.

The failure it prevents. Reallocating budget toward the line items with the best last-click ROAS concentrates spend on the closers that take credit for inevitable conversions, and starves the prospecting that actually creates demand. Incrementality is what stops that mistake.

Where the mechanics live: Conversion Lift, attribution-model setup, and lookback windows in `dv360-measurement-and-attribution`; the multi-touch path that reveals assisted, non-last-click work in `path-to-conversion-analysis`; custom event-level incrementality in `dv360-advanced-analytics-adh`.

## 4. Attention as an emerging signal next to viewability

The problem. Viewability confirms an ad met a pixel-and-time condition (the opportunity to be seen), not that a person actually noticed it. A high viewability rate can sit on inventory no one looked at.

The practice. Where attention data is available, read it alongside viewability and outcomes. The IAB and the MRC have published an Attention Measurement framework that standardizes attention as a complementary signal, distinct from viewability, spanning data-signal, visual and audio tracking, physiological, and panel or survey methods. Attention estimates whether the ad was noticed and to what depth. It complements delivery and outcome metrics; it does not replace them and is not yet a settled single number. Treat it as an emerging, directional signal, not a hard target, and never read a high viewability rate as proof of attention.

Best-practice caveat. Attention vendors and methods differ, and there is no single universal attention metric to optimize to yet. Use it to compare environments and creative, not as a contractual KPI, until the standard matures further.

Where the mechanics live: the viewability standard (50 percent of pixels for 1 second display, 2 seconds video) and measurable rate in `programmatic-foundations`; Active View metrics in `dv360-reporting`.

## 5. Blended versus platform ROAS, and the place of MMM and MTA

The problem. Every platform claims the same conversion for itself. Sum the ROAS each DSP, each social platform, and each analytics tool reports, and the total revenue is counted several times over. Platform ROAS is real for optimizing inside one channel but cannot be added across channels.

The practice. Read two ROAS numbers side by side. Platform ROAS (what one platform attributes to itself) drives in-channel optimization. Blended ROAS (total revenue over total spend across all channels) is the un-attributed, un-double-counted reality check on the whole program. When they diverge sharply, attribution is over-crediting somewhere. Then place the three measurement methods correctly, best practice rather than a single citable page:

- Multi-touch attribution (MTA) assigns fractional credit across the digital touchpoints it can see. Use it for tactical, in-channel optimization within already-validated channels. It is blind to offline and to anything it cannot track, and it is correlational.
- Marketing mix modeling (MMM) regresses outcomes against spend across all channels including offline, at a coarse grain. Use it for cross-channel budget allocation and for channels MTA cannot see. It does not optimize a single creative.
- Incrementality experiments are the ground truth. Use controlled tests to prove causal lift, and use them to calibrate both MMM and MTA so those models are anchored to reality rather than to correlation.

The mature stance is triangulation: incrementality calibrates MMM for allocation, MTA handles tactical in-channel credit, and platform reporting handles day-to-day operations, in that order of authority. Do not crown one method as the single source of truth.

The failure it prevents. Trusting platform ROAS as the whole truth inflates measured performance and double-counts revenue across channels, which leads to over-investing in whatever platform claims credit most aggressively. Reading blended ROAS and triangulating with MMM and incrementality keeps the program honest.

Where the mechanics live: ROAS and eCPM math, and converting buys to a common basis, in `programmatic-foundations`; cross-channel attribution beyond a single platform, and segment-level ROAS with first-party data, in `dv360-advanced-analytics-adh`.

## Auditing an existing report against the bar

Run any report a stakeholder relies on through these checks:

1. Is reach summed anywhere? If a total reach is an addition of smaller reach figures, it is wrong. Replace it with a deduplicated read.
2. Is reach gross or on-target? If there is no on-target percentage, the report cannot say whether the right audience was reached.
3. Does a budget recommendation rest on last-click? If so, there is no incrementality behind it. Add a lift read before reallocating.
4. Is viewability being read as attention or as proof of impact? If so, separate the two and add a lift study for awareness goals.
5. Is ROAS platform-only? If there is no blended number and no MMM or incrementality context, the ROAS is likely over-credited.
6. Can the report fail? If there is no target, no prior period, and no control, it can only confirm. Add the benchmark or the holdout.

A report that passes all six is built to the state of the art bar. One that fails any of them is competent-looking but misleading in a specific, nameable way.

## Sources

- Reach reports, Display & Video 360 Help: https://support.google.com/displayvideo/answer/6170584 (as of June 2026)
- Cross-Media Reach reporting, Display & Video 360 Help: https://support.google.com/displayvideo/answer/13955444 (as of June 2026)
- On-target reach, Display & Video 360 Help: https://support.google.com/displayvideo/answer/9545617 (as of June 2026)
- Set up Conversion Lift measurement, Display & Video 360 Help: https://support.google.com/displayvideo/answer/16804790 (as of June 2026)
- Key event attribution models report, Google Analytics 4 Help: https://support.google.com/analytics/answer/10596865 (as of June 2026)
- Get started with attribution, Google Analytics 4 Help: https://support.google.com/analytics/answer/10596866 (as of June 2026)
- About Active View, Display & Video 360 Help: https://support.google.com/displayvideo/answer/3214556 (as of June 2026)
- Attention Measurement framework (IAB and MRC), Interactive Advertising Bureau: https://www.iab.com/guidelines/attention/ (as of June 2026)
