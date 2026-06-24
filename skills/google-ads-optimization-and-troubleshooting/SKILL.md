---
name: google-ads-optimization-and-troubleshooting
description: Diagnose and fix a Google Ads account that is underperforming, and apply optimization score and recommendations with judgment. Use when the user says Google Ads is "not delivering", "no impressions", "no conversions", a campaign is "limited by budget" or "eligible (limited)", a bid strategy is "learning" or "misconfigured" or "limited", an ad is "disapproved", impression share is low, or asks about optimization score, why Search and Performance Max overlap, or why conversions are not tracking. Walk the triage flow first, then the matching playbook.
---

# Google Ads optimization and troubleshooting

Ordered playbooks for the most common Google Ads delivery, performance, and tracking failures, plus how to use optimization score and recommendations without hurting the account. The goal is to find the single binding constraint fast, fix that one thing, and avoid the trap of applying ten recommendations at once and learning nothing.

Google Ads is a separate platform from Display & Video 360. The statuses, recommendations, and bid strategies here are Google Ads concepts. Do not map them onto DV360 line items or carry DV360 troubleshooting steps into Google Ads. For KPI definitions and auction mechanics, see the `programmatic-foundations` skill. To pull the exact report or impression-share columns a diagnosis needs, see the `google-ads-reporting` skill. To choose which metrics prove success for a goal, see the `reporting-by-campaign-goal` skill. For conversion-credit and assisted-path questions, see the `path-to-conversion-analysis` skill.

## When to use this skill

Use it when a campaign is live and something is wrong, or when you are deciding what to change:

- No delivery, zero impressions, or near-zero spend.
- Campaign status reads "Eligible (limited)" or "Limited by budget".
- A bid strategy status reads "Learning", "Limited", or "Misconfigured".
- An ad or asset is "Disapproved" or otherwise not serving.
- Search impression share is low and you need to know whether it is budget or rank.
- Conversions are zero, far below plan, or the tracking status looks wrong.
- Search and Performance Max appear to be competing or overlapping.
- The account shows a low optimization score and a stack of recommendations to triage.

Boundary: if the question is how a metric is defined or how the math works, that is `programmatic-foundations`. If it is which report or column to pull, that is `google-ads-reporting`. If it is how a conversion is credited across touchpoints, that is `path-to-conversion-analysis`. This skill is the entry point for "something is broken or could be better, what do I change."

## Quick reference: triage flow

Always run this top-down. Each step gates the next, so a problem high in the list masks everything below it. Do not touch bids, recommendations, or creative before confirming status, budget, and approval.

1. **Status.** Are the campaign, ad group, and at least one ad all Eligible and not paused, removed, or ended? Is the campaign inside its start and end dates? A paused parent or an empty ad group stops everything under it.
2. **Approval.** Is at least one ad Approved (or Approved limited)? A Disapproved or under-review ad cannot serve. Check the ad Status column for the policy reason.
3. **Budget.** Does the campaign read "Limited by budget" or "Eligible (limited)"? If so, spend is capped before the auction even matters.
4. **Bid strategy.** Is the bid strategy Active, or is it Learning, Limited, or Misconfigured? A Misconfigured strategy can stop optimizing entirely.
5. **Auction and rank.** With status, budget, and strategy healthy, is the bid and quality enough to win? Read Search lost IS (rank) to see how much you are losing to Ad Rank.
6. **Targeting size.** After every targeting layer is intersected (keywords, audiences, geo, schedule, devices), is the addressable pool large enough to deliver? Over-narrow targeting is the most common silent killer.
7. **Tracking.** If delivery is healthy but conversions are missing, the fault is almost always measurement, not media: conversion action status, tag firing, or the attribution window.

## Optimization score and recommendations

Optimization score is an estimate (0 to 100 percent) of how well the account is set to perform, shown for active Search, Display, Video Action, App, Performance Max, Demand Gen, and Shopping campaigns. Each recommendation lists how many points it would add. Treat the score as a prompt to review, not a target to max out.

Apply with judgment:

- **Read the recommendation, then decide.** Recommendations come from account history and Google forecasts. Many are sound (fix tracking, add a missing conversion action, raise a budget that is demonstrably capped). Some loosen targeting, broaden match types, or raise budgets in ways that conflict with the plan.
- **Never bulk-apply blindly.** "Apply all" can change match types, budgets, and bidding at once. If results move, you will not know which change did it. Apply one meaningful recommendation at a time on anything that affects spend or targeting.
- **Dismiss what does not fit, on purpose.** Dismissing a recommendation raises the score for that item and tells the system the trade-off is intentional. A 100 percent score is not the goal; a score that reflects deliberate choices is.
- **Watch auto-apply.** If auto-apply is on, recommendations can change the account without review. Audit which categories are enabled before trusting the account is in the state you left it.

The highest-value recommendations usually map to the triage flow: fix Disapproved ads, fix Misconfigured bid strategies, fix broken conversion tracking, and raise budgets only where Search lost IS (budget) proves the cap is real.

## Playbook: no delivery or near-zero impressions

Most often a status, approval, or budget gate, not a bidding problem. In order:

1. Confirm nothing in the chain is paused, removed, or ended, and that today is inside the campaign dates.
2. Confirm the ad group has at least one Eligible, Approved ad and active keywords or targeting. An ad group with only Disapproved ads serves nothing.
3. Confirm the campaign is not "Limited by budget" or "Eligible (limited)" to the point of barely serving.
4. Confirm the bid strategy is Active, not Misconfigured.
5. Confirm the bid clears typical first-page and floor expectations for the keywords, and read Search lost IS (rank).
6. Confirm targeting is not so narrow that the eligible pool is empty: check geo, ad schedule, device exclusions, audience layering, and negative keywords that may be over-blocking.
7. For Performance Max specifically, confirm asset groups have approved assets and the campaign is not held by a setup issue.

## Playbook: "Eligible (limited)" and "Limited by budget"

These two statuses both mean the campaign serves less than it could, but they have different causes, so read the exact label.

- **Limited by budget.** The campaign is held back by its budget. Confirm with Search lost IS (budget): a meaningful value there proves the cap is real. Then decide whether to raise the budget (only if the incremental spend pays back at the goal), tighten targeting so the existing budget concentrates on the best traffic, or lower bids so the budget buys more clicks. Raising budget on a campaign that is actually rank-limited wastes money.
- **Eligible (limited).** The campaign is active but serving only occasionally. This can be budget, but it can also be a policy restriction on the ads or a recent significant change (a budget jump, a bid-strategy switch) that put the strategy back into learning. Hover the status for the specific reason. If it is policy, fix the ad. If it is a recent change, let it settle before judging.

Always pair the lost-IS read: budget-limited shows in Search lost IS (budget), rank-limited shows in Search lost IS (rank). Pull both from `google-ads-reporting`.

## Playbook: bid strategy status (Learning, Limited, Misconfigured)

A bid strategy status tells you whether automated bidding is working as intended.

- **Active.** The strategy is setting bids to optimize. Nothing to do.
- **Learning.** The strategy is recalibrating after a new strategy, a setting change, or a composition change (campaigns, ad groups, or keywords added or removed). Calibration can take roughly 50 conversion events or about 3 conversion cycles. Do not stack more changes during learning, and do not judge performance until it exits. If you keep editing, you keep restarting the clock.
- **Limited.** The strategy is constrained: by inventory, by a bid limit (a cap set too low for the market), by budget, or by the strategy itself. Identify which limit binds and relax that one. A Target CPA or max-bid cap set below market will starve delivery no matter how healthy everything else is.
- **Misconfigured.** The strategy cannot optimize. Two common causes: a maximize strategy shares a budget with campaigns not all on the same portfolio strategy (remove the shared budget or put every campaign in one portfolio strategy), or a conversion-based strategy has no valid conversion actions set up (fix conversion tracking first). Misconfigured is urgent, because the strategy may not be optimizing at all.

For choosing or tuning the strategy itself rather than fixing its status, treat that as a bidding decision and apply the goal from `reporting-by-campaign-goal`.

## Playbook: ad disapproved or not serving

A Disapproved ad will not show, because it violates a policy. In order:

1. Hover or open the ad Status column to read the specific policy reason; the violation can be in the ad text, an asset, or the landing page.
2. Read the cited policy so the fix actually addresses it.
3. Fix the cause: edit the ad, the asset, or the destination to comply. Editing resubmits the ad for review, which returns it to under-review until it is approved again.
4. If you believe the decision is wrong or you have fixed the violation, appeal the policy decision (dispute, or state that you made changes to comply) and track it in Policy manager.
5. Distinguish "Approved (limited)" from "Disapproved": approved-limited serves but with restrictions (for example, limited locations or audiences), while disapproved does not serve at all.

## Playbook: low search impression share (budget vs rank)

Low Search IS means you are capturing a small share of the demand you are eligible for. The fix depends entirely on which lost-IS bucket is larger.

1. Pull Search IS, Search lost IS (budget), and Search lost IS (rank) for the campaign (see `google-ads-reporting`).
2. **If lost IS (budget) dominates,** you are budget-limited. Raise the budget only where the incremental spend pays back, or concentrate the existing budget by tightening targeting or trimming low-value keywords.
3. **If lost IS (rank) dominates,** you are rank-limited. Ad Rank is bid times quality plus context, so raise bids and improve quality (more relevant ads and keywords, better expected CTR, better landing-page experience). More budget will not help a rank problem.
4. If both are high, fix the larger bucket first, let it settle, then re-read. Chasing both at once makes the cause unknowable.
5. To judge prominence rather than presence, read Search top IS and Search absolute top IS and their lost variants to see whether budget or rank is keeping you out of the top positions.

## Playbook: low or no conversions

If impressions are delivering but conversions are zero or far below plan, suspect measurement before media. In order:

1. Open the conversion action and read its tracking status. "Unverified", "Inactive", "Tag inactive", or "No recent conversions" each point at a specific tag or setup problem, not a media problem.
2. Confirm the tag fires on the right pages and that the conversion action is included in the "Conversions" column and counted toward bidding.
3. Confirm enough time has passed: conversions lag, and some actions take hours to a day or more to register. Do not declare failure on data that is only a few hours old.
4. Confirm you are reading the right attribution window and model before concluding media is failing.
5. Only after measurement is verified should you question audience quality, match types, or the bid strategy.

For how credit is assigned across multiple touchpoints and assisted conversions, hand off to `path-to-conversion-analysis`.

## Playbook: Search and Performance Max overlap

When a Search campaign and a Performance Max campaign could both serve for the same query, the tie-break is specific:

1. A Search campaign with a keyword that exactly matches (or is spell-corrected to) the query is preferred over Performance Max.
2. If no keyword across match types exactly matches the query, the campaign with the higher Ad Rank serves.
3. Performance Max can still show for brand or other terms when the Search campaign is constrained (for example, limited by budget or narrower targeting). If you need to keep Performance Max off specific terms, use brand exclusions or negative keywords in Performance Max where supported.
4. Before assuming "Performance Max is stealing my Search traffic," confirm the Search campaign is not itself budget-limited or rank-limited, because that, not Performance Max, is often why exact-match terms are not winning.

## Common pitfalls

- **Applying many changes or recommendations at once.** Move one lever, let it run a learning cycle, then read the result. Simultaneous changes make the cause unknowable.
- **Skipping status and approval.** A paused campaign, an empty ad group, or an all-disapproved ad produces zero delivery that looks like a bidding problem. Confirm the chain first.
- **Confusing budget-limited with rank-limited.** They demand opposite fixes. Read both Search lost IS columns before changing budgets or bids.
- **Editing during learning.** Every significant edit restarts the learning period. Make the change you need, then leave it alone until the strategy calibrates.
- **Trusting fresh conversion data.** Conversions lag. Do not re-optimize or declare "no conversions" on a few hours of data.
- **Maxing optimization score for its own sake.** The score is a prompt, not a KPI. Apply what helps, dismiss what does not, and keep changes deliberate.
- **Treating Google Ads statuses like DV360 statuses.** They are different systems. Diagnose Google Ads on its own terms.

## Sources

- About optimization score, Google Ads Help: https://support.google.com/google-ads/answer/9061546 (as of June 2026)
- About recommendations, Google Ads Help: https://support.google.com/google-ads/answer/9232380 (as of June 2026)
- About bid strategy statuses, Google Ads Help: https://support.google.com/google-ads/answer/6263057 (as of June 2026)
- Duration of the learning period for campaigns and what affects it, Google Ads Help: https://support.google.com/google-ads/answer/13020501 (as of June 2026)
- Campaign status: Definition, Google Ads Help: https://support.google.com/google-ads/answer/2549115 (as of June 2026)
- Fix "Limited by budget" status, Google Ads Help: https://support.google.com/google-ads/answer/6385220 (as of June 2026)
- Get impression share data, Google Ads Help: https://support.google.com/google-ads/answer/7103314 (as of June 2026)
- Disapproved: Definition, Google Ads Help: https://support.google.com/google-ads/answer/2615949 (as of June 2026)
- Fix a disapproved ad or appeal a policy decision, Advertising Policies Help: https://support.google.com/adspolicy/answer/9338593 (as of June 2026)
- Troubleshoot your conversion tracking status, Google Ads Help: https://support.google.com/google-ads/answer/12674892 (as of June 2026)
- How Performance Max interacts with other campaigns in your account, Google Ads Help: https://support.google.com/google-ads/answer/13810170 (as of June 2026)
