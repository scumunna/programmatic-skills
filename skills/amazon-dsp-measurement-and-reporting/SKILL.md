---
name: amazon-dsp-measurement-and-reporting
description: Pull Amazon DSP reporting and read the retail funnel like an expert. Use when the user asks about Amazon DSP reporting, Amazon DSP metrics, Amazon DSP ROAS, new to brand, detail page views, add to cart, retail metrics, attribution windows on Amazon, or full-funnel and brand measurement on Amazon DSP. Covers the signals that make Amazon distinct from a standard display DSP.
---

# Amazon DSP measurement and reporting

Read an Amazon DSP campaign the way the platform is built to be read: not just impressions and clicks, but the retail funnel underneath them. Amazon DSP joins ad exposure to shopping behavior on Amazon, so a report can show detail page views, add to cart, purchases, sales, and return on ad spend that an off-Amazon display DSP cannot see. This skill names the metrics that matter, the order to read them in, the attribution rules that decide which conversions count, and the new-to-brand signal that separates acquisition from repeat business.

Amazon DSP is the programmatic, audience-first buying platform. It is distinct from Amazon sponsored ads, which are self-service cost-per-click placements that capture demand on Amazon search and detail pages. The two report differently and chase different parts of the funnel, so do not blend their numbers. This skill is about Amazon DSP.

For what each metric means in the abstract and the KPI math, see the `programmatic-foundations` skill. For choosing the report shape that fits a campaign objective, see the `reporting-by-campaign-goal` skill. For the multi-touch path to a conversion, see the `path-to-conversion-analysis` skill. For event-level, privacy-safe analysis, custom attribution, overlap, and incrementality on Amazon signals, see the `amazon-marketing-cloud` skill.

## When to use this skill

- "Pull / read an Amazon DSP report" or "what Amazon DSP metrics matter for [goal]?"
- "What are detail page views / add to cart / purchases in Amazon DSP?"
- "New to brand," "NTB," "how many first-time buyers did this drive?"
- "Amazon DSP ROAS," "is this campaign profitable on Amazon?"
- "What attribution window does Amazon DSP use?" or "post-view vs post-click on Amazon."
- "How do I read the retail funnel?" or "measure a full-funnel Amazon brand campaign."
- "Reach, frequency, and video completion rate for an Amazon DSP campaign."

Boundary: if the question is what a metric means in general or the KPI formula, that is `programmatic-foundations`. If it is which report fits an objective regardless of platform, that is `reporting-by-campaign-goal`. If it is the ordered sequence of touchpoints before a conversion, that is `path-to-conversion-analysis`. If it needs event-level joins, custom attribution, audience overlap, or incrementality, that is `amazon-marketing-cloud`. If the question is about sponsored ads (cost-per-click on Amazon), this is the wrong skill.

## Quick reference

Read the funnel top to bottom. Each stage answers a different question; do not jump to ROAS before you know reach and consideration moved.

| Funnel stage | Primary metrics | The question it answers |
| --- | --- | --- |
| Delivery | Impressions, spend, eCPM | Did the campaign deliver, and at what cost per thousand? |
| Engagement | Click-through rate (CTR), video completion rate (VCR) | Did the creative earn attention? |
| Reach and saturation | Reach, average frequency | How many distinct people, and how often each? |
| Consideration (retail) | Detail page views, detail page view rate, add to cart | Did exposure drive shopping behavior on Amazon? |
| Purchase (retail) | Purchases, sales, units sold, ROAS | Did it drive revenue, and was it efficient? |
| Acquisition (retail) | New-to-brand purchases, NTB sales, NTB ROAS, percent of purchases NTB | How much of the outcome was net-new customers? |

Default read order: confirm delivery, then engagement, then reach and frequency, then walk the retail funnel from detail page views to purchases, and only then judge ROAS and new-to-brand. A strong purchase number on weak consideration signals is a measurement artifact to investigate, not a win to report.

## The retail funnel and why Amazon is distinct

A standard display DSP stops at impressions, clicks, viewability, and whatever conversions a pixel reports. Amazon DSP adds the shopping signals that happen on Amazon after the ad, because the platform sees the retail behavior directly:

- **Detail page views (DPV).** A shopper viewed the product detail page for a promoted ASIN after ad exposure. This is the first retail consideration signal, the Amazon analog of a qualified site visit. Detail page view rate (DPVR) is detail page views over impressions.
- **Add to cart (ATC).** The shopper added a promoted ASIN to the cart. A stronger consideration signal than a detail page view, one step short of purchase.
- **Purchases and sales.** Purchases is the count of attributed orders of promoted products; sales is the attributed revenue in local currency. Units sold counts items, and a single purchase event can include multiple units.
- **Return on ad spend (ROAS).** Attributed sales over ad cost. This is the efficiency read for a lower-funnel or full-funnel Amazon campaign. Pair it with new-to-brand ROAS to separate growth from harvesting existing demand.
- **Subscribe and Save subscriptions.** For eligible products, recurring-purchase signups attributed to the ad. Tracking these requires the parent ASIN to be associated with the order.

These retail signals are the reason to run Amazon DSP rather than a generic display buy: the report ties media to shopping behavior and revenue on Amazon without a separate conversion pixel for the on-Amazon path.

## New-to-brand: the acquisition signal

New-to-brand (NTB) is the metric that tells you whether media bought new customers or repeat ones. Amazon classifies a purchase as new-to-brand by looking back over roughly the prior 12 months (a one-year lookback) of the shopper's purchase history for the brand: a buyer who has not purchased ASINs of the same brand in that window is new-to-brand, and one who has is an existing customer.

Read these together:

- **New-to-brand purchases.** First-time brand purchases of promoted products over the one-year lookback.
- **New-to-brand sales.** Revenue from those first-time purchases.
- **New-to-brand units sold.** Quantity of promoted products purchased for the first time within the brand over the one-year window.
- **New-to-brand ROAS.** New-to-brand sales over total ad cost. This isolates the efficiency of acquisition, not total revenue.
- **Percent of purchases new-to-brand.** The share of attributed purchases that were first-time brand buyers. A high percent on an acquisition campaign is the goal; a high percent on a loyalty or repeat campaign means the targeting is off.

Why it matters: total ROAS rewards a campaign that simply harvested customers who would have bought anyway. New-to-brand metrics separate incremental customer growth from that harvesting, which is the whole point of upper-funnel and prospecting spend on Amazon. New-to-brand is available for display and video (and sponsored brands) for campaigns from late 2018 onward.

## Attribution on Amazon DSP

Amazon DSP attributes conversions on a last-touch model with a 14-day lookback window as the standard default. The rules that change how you read a report:

- **14-day lookback.** An ad is eligible for attribution if it was clicked or viewed within 14 days before the conversion. A conversion outside that window does not credit the campaign.
- **Last touch, clicks over views.** When a shopper interacted with multiple ads, attribution weighs each ad's relevance to the sold product, then applies a last-touch model that prioritizes the last click over the last view. Clicks beat views because a click is the stronger engagement signal.
- **View-through requires a viewable impression.** A view-through conversion is credited only if the impression met the Media Rating Council standard for a viewable impression. That standard differs by format: broadly, at least 50 percent of the ad's pixels in view for at least 1 continuous second for display, and at least 2 continuous seconds for video. A served-but-not-viewed impression does not earn view-through credit.
- **Total conversions combine views and clicks.** The conversion count in a report is the sum of view-through and click-through conversions. To split them, read the metric variants: "Purchases" is the total, "Purchases views" is view-through, and "Purchases clicks" is click-through. Collapsing the two hides how much credit is view-through.

Confirm the attribution window in the campaign's own settings and reporting before you quote it. The 14-day last-touch default is the standard, but treat the window as a setting to verify rather than an immutable constant, because attribution configuration evolves.

## Brand and full-funnel measurement

Lower-funnel ROAS is not the only goal on Amazon, and forcing an awareness campaign to prove ROAS misreads it.

- **Upper funnel (awareness, consideration).** Lead with reach, frequency, video completion rate, detail page views, and detail page view rate. The job is to grow qualified consideration, so judge it on reach and the consideration signals, not on immediate purchases.
- **Full funnel.** Read the whole table top to bottom: delivery and engagement, then reach and frequency, then the retail funnel from detail page views through purchases and sales, then ROAS and new-to-brand. The story is the movement between stages, not any single number.
- **Brand-impact studies.** For lift in awareness, consideration, purchase intent, or ad recall, Amazon offers brand-survey and lift measurement beyond click and conversion logs. Treat these as a separate study layer that answers "did perception move," which standard delivery metrics cannot. For incrementality measured from the event log itself, route to the `amazon-marketing-cloud` skill.

## Core process

1. **State the question and the goal in one sentence.** "Did the prospecting line item drive new-to-brand purchases efficiently last month?" fixes the funnel stage, the metric set, and the window. A vague pull returns a wide table no one reads.
2. **Match the metric set to the funnel stage, not to habit.** Awareness reads reach, frequency, VCR, and detail page views. Performance reads add to cart, purchases, sales, ROAS, and new-to-brand. Pulling purchase metrics for an awareness goal invites the wrong verdict.
3. **Pull the report at the right grain.** Order, line item, creative, and audience are the useful cuts. Start at the coarsest grain that answers the question and add a split only to explain a number you already see.
4. **Walk the funnel in order.** Confirm delivery and engagement, then reach and frequency, then detail page views and add to cart, then purchases, sales, and ROAS, then new-to-brand. Each stage qualifies the next.
5. **Separate view-through from click-through and total from new-to-brand.** Read the "views" and "clicks" variants of conversion metrics, and read new-to-brand against total. Collapsing either hides the real driver.
6. **Read every number against its plan target and the attribution window.** A ROAS or NTB figure is good or bad only against the media-plan benchmark for that goal, and only over the window the campaign actually attributes on.

## Decision rules and thresholds

- **Default attribution is 14-day, last-touch, clicks over views.** Quote it only after confirming it in the campaign settings, because the window is configurable.
- **Read viewable-impression-gated view-through with care.** View-through credit requires an MRC-viewable impression. A campaign heavy in non-viewable inventory will under-credit view-through, which is a delivery-quality signal, not a demand signal.
- **Judge prospecting on new-to-brand, retargeting on total ROAS.** Acquisition campaigns live or die on NTB purchases and NTB ROAS. A retargeting line with high total ROAS but near-zero NTB is harvesting existing demand, which may be fine for its goal but is not growth.
- **Detail page view rate is a creative-and-targeting read.** A high impression count with a low DPVR points at weak creative or mismatched audience, upstream of any purchase problem.
- **Do not compare Amazon DSP and sponsored-ads ROAS head to head.** Different attribution, different funnel position, different intent. Compare each to its own benchmark.

## Templates and examples

Awareness line item, monthly read:

> Impressions 4.2M, eCPM at plan. VCR 71 percent (above the 65 percent video benchmark). Reach 1.1M unique, average frequency 3.8. Detail page views 38k, DPVR 0.90 percent. Verdict: delivered, creative held attention, consideration moved. Not judged on purchases; this is upper funnel.

Prospecting line item, acquisition read:

> Purchases 1,240, sales attributed, total ROAS 3.1. New-to-brand purchases 1,000 (about 80 percent of purchases NTB), new-to-brand ROAS 2.5. Verdict: strong acquisition, four in five buyers were new to the brand. Report NTB ROAS as the headline, total ROAS as context.

Reconciliation note when a stakeholder questions a conversion count:

> "Purchases" 1,240 = "Purchases clicks" 760 + "Purchases views" 480. The 14-day last-touch model credits the last click over the last view, and view-through counts only viewable impressions. Splitting the metric explains the gap between click-reported and total purchases.

## Common pitfalls

- **Blending Amazon DSP and sponsored-ads numbers.** They attribute differently and sit at different funnel positions. Keep them in separate reports and compare each to its own benchmark.
- **Judging an awareness campaign on ROAS.** Upper-funnel media is bought to grow reach and consideration. Force-fitting a purchase KPI produces a false negative. Read reach, frequency, VCR, and detail page views instead.
- **Reading total ROAS as growth.** Total ROAS includes existing customers. Without new-to-brand alongside it, a campaign that only harvested loyal buyers looks like acquisition.
- **Collapsing view-through and click-through.** The total hides the mix. Read the "views" and "clicks" variants before you attribute the outcome to a tactic.
- **Quoting a 14-day window without checking.** The 14-day last-touch default is standard but configurable. Confirm it in the campaign before stating it to a client.
- **Ignoring the viewability gate on view-through.** Non-viewable inventory suppresses view-through credit. A view-through shortfall can be an inventory-quality problem, not a demand problem.
- **Summing reach across rows.** Reach is de-duplicated people. Adding reach across days, line items, or audiences overcounts. For de-duplicated reach across campaigns or devices, use the `amazon-marketing-cloud` skill.

## Sources

- What is a demand-side platform? A complete guide, Amazon Ads (distinguishes Amazon DSP from sponsored ads): https://advertising.amazon.com/library/guides/demand-side-platform (as of June 2026)
- Amazon DSP product overview, Amazon Ads: https://advertising.amazon.com/solutions/products/amazon-dsp (as of June 2026)
- Amazon DSP Self-Service Reporting Guide (Amazon-hosted PDF; attribution window, retail conversion metrics, new-to-brand definitions): https://m.media-amazon.com/images/G/09/AdvertisingSite/AmazonDSPLearningHub/CampaignManagement/Amazon_DSP-SS_Reporting_Guide_EN.pdf (as of June 2026)
- New-to-brand detail page view metrics available via DSP UI and reports, Amazon Ads (new-to-brand lookback): https://advertising.amazon.com/resources/whats-new/detail-page-view-metrics (as of June 2026)
- Campaign reporting: analyze advertising performance, Amazon Ads: https://advertising.amazon.com/measurement-analytics/campaign-reporting (as of June 2026)
- DSP reporting metrics, Amazon Ads advanced tools documentation: https://advertising.amazon.com/API/docs/en-us/guides/reporting/dsp/metrics (as of June 2026)

Note on sources: Amazon's advanced-tools documentation (advertising.amazon.com/API/docs) renders client-side and cannot be machine-verified line by line, and some retail-funnel definitions are documented only inside the help center or the reporting console. Where this skill states attribution mechanics, conversion-metric definitions, or new-to-brand lookback windows, those are drawn from the Amazon-hosted reporting guide PDF above and stated as general Amazon DSP practice; confirm the live values in the Amazon DSP reporting console and the Amazon Ads documentation before quoting them to a client, because windows and metric availability are configurable and change over time.
