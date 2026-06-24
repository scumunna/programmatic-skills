---
name: stackadapt-optimization-and-troubleshooting
description: Diagnose and fix a StackAdapt campaign that is not delivering or not performing. Use when the user says "StackAdapt not delivering", "StackAdapt underpacing", "StackAdapt troubleshooting", "StackAdapt optimization", "improve StackAdapt performance", "StackAdapt conversion not tracking", "no impressions on StackAdapt", "StackAdapt creative disapproved", "StackAdapt campaign not spending", or "why is my StackAdapt campaign behind pace". Walk the triage flow first, then the matching symptom playbook.
---

# StackAdapt optimization and troubleshooting

Ordered playbooks for the most common StackAdapt delivery and performance failures. StackAdapt is a self-serve multi-channel DSP whose core strength is native, plus display, video, connected TV (CTV), audio, and digital out-of-home (DOOH). The goal here is to find the single binding constraint fast, fix it, and avoid the trap of changing five settings at once and learning nothing.

For KPI definitions, auction mechanics, and the impression-loss model, see the `programmatic-foundations` skill. This skill assumes you know what pacing, eCPC, win rate, and viewable rate mean, and tells you what to check, in what order, when one of them is wrong. For pulling the numbers and reading attribution, see the `stackadapt-reporting-and-attribution` skill.

## When to use this skill

Use it when a campaign is live and a metric is wrong:

- No delivery, zero impressions, or zero spend on a campaign or line item.
- Underpacing (will not finish the flight) or overpacing (will exhaust budget early).
- Weak performance: high eCPC or eCPA, low CTR or conversion rate, low viewability or video completion.
- A creative is pending, rejected, or disapproved by a media owner and not serving.
- Conversions are not firing or not attributing, so a conversion-goal campaign looks broken.

Boundaries with sibling skills:

- Campaign, line item, and flight construction: `stackadapt-campaign-setup`.
- Bid type choice (CPC, CPM, CPCV, CPA goal), budget shape, and pacing mode: `stackadapt-bidding-and-budgets`.
- Audience build, retargeting, lookalikes, and targeting layers: `stackadapt-targeting-and-audiences`.
- Inventory, deals, supply path, and brand-safety controls: `stackadapt-inventory-and-brand-safety`.
- Account, advertiser, and pixel structure: `stackadapt-account-structure`.
- Report design, conversion paths, and attribution windows: `stackadapt-reporting-and-attribution`.

This skill is the entry point. It routes to those skills when the fix lives there.

## Quick reference: triage flow

Always run this top-down. Each step gates the next, so a problem high in the list masks everything below it. Do not jump to bids or creative before confirming status, budget, and flight.

1. **Status.** Is the campaign, its line items, the campaign group, and the advertiser all active and not paused, ended, or archived? Is at least one approved creative attached? A paused parent stops everything under it.
2. **Budget and flight.** Is today inside the flight dates? Is there unspent budget in the current pacing window (daily and total)? Has a shared budget been consumed by sibling line items?
3. **Bid and win rate.** Is the bid high enough to clear the floor for the inventory and channel you target? CTV and premium video floors sit far above native and display, so a bid that wins native loses CTV. Is win rate plausible for the bid type?
4. **Targeting size.** Is the addressable pool large enough after every targeting layer (geo, audience, device, daypart, inventory, brand safety) is intersected? Over-narrow targeting is the most common silent killer, especially small retargeting pools and tight geofences.
5. **Inventory and deals.** Is there matching supply for the channel? For a deal or PMP, is it active, mapped to the line item, and is the bid above the deal floor?
6. **Creative.** Is a creative approved and the right format and size for the channel? Native, display, video, CTV, audio, and DOOH each require their own asset specs, and each media owner can approve or reject independently.
7. **Tracking.** If delivery is fine but conversions are missing, the fault is usually measurement, not media: the pixel did not fire, the conversion event is not mapped, or you are reading the wrong attribution window.

Most platforms expose a delivery or pacing view and an optimization suggestions surface. Read those first. StackAdapt analyzes campaign data and recommends optimizations to performance and delivery based on the bid type and goal you defined, after the campaign has run for at least a day. Do not act on suggestions on day one.

## The delivery-loss model

When a campaign delivers below plan, frame it as impressions lost to a specific cause, then fix that cause. The buckets, in the order they usually bind:

- **Nothing eligible to serve.** No approved creative for the channel, or a paused parent. Zero is the signature.
- **Bid below the clearing price.** The bid does not clear the floor for the targeted inventory and channel, so requests are lost in the auction. Common when one bid is shared across native and high-floor CTV or premium video.
- **Pool too thin.** Targeting is intersected so tightly that few requests match. Retargeting and lookalike seeds that are too small, narrow geofences, and stacked audience plus daypart plus device filters are the usual culprits.
- **Budget or pacing exhausted.** The daily or total budget is spent, or the pacing mode front-loaded spend. A campaign can look healthy on total and still go dark mid-day on a daily cap.
- **Frequency capped.** A tight frequency cap exhausts eligible users, so additional impressions cannot be bought against the same audience.

Diagnose the largest bucket first. Shrinking a small bucket changes nothing. Viewability and completion rate are delivery-quality metrics, not loss buckets: fix them through inventory mix and prebid thresholds, not by raising the bid.

## Symptom playbooks

Each playbook is the fast path. Run the triage flow first to confirm you are in the right symptom, then work the ordered steps. Move one lever, let it run, then read the result.

### No delivery / zero impressions

Most often a status or eligibility gate, not a bidding problem. In order:

1. Confirm nothing in the parent chain (advertiser, campaign group, campaign, line item) is paused, ended, or archived.
2. Confirm today is inside the flight and budget remains in both the daily and total windows.
3. Confirm at least one creative is approved for the channel and attached to the line item. A pending or rejected creative serves nothing. CTV, audio, and DOOH lines need channel-specific assets.
4. Confirm the bid clears the floor for the targeted channel. Raise it to a realistic level for that inventory and re-check.
5. Confirm targeting is not so narrow that the pool is empty. Loosen the tightest layer (often a small retargeting list or a tight geo) and re-check.
6. For a deal or PMP line, confirm the deal is active, mapped to the line item, and that the bid clears the deal floor. Hand off to `stackadapt-inventory-and-brand-safety` for the full deal tree.

### Underpacing

The campaign is delivering but will not finish the flight. Find the binding loss bucket from the delivery-loss model, then raise that one lever:

1. **Bid too low.** If loss is in the auction, raise the bid toward the clearing price for the channel. CTV and premium video need materially higher bids than native and display.
2. **Pool too thin.** Broaden the tightest targeting layer. Expand a retargeting window, enlarge a lookalike seed, widen a geofence, or relax a daypart or device filter.
3. **Budget shaped wrong.** If a daily cap goes dark mid-day, raise the cap or switch the pacing mode so spend spreads across the flight. Pacing-mode mechanics live in `stackadapt-bidding-and-budgets`.
4. **Frequency too tight.** Loosen the frequency cap so more impressions are eligible per user.
5. **Inventory too restricted.** Open additional inventory, channels, or a deal so there is more supply to buy. Then confirm against `stackadapt-inventory-and-brand-safety` that brand-safety filters are not removing most of it.

Raise the binding lever, not all of them, then wait. StackAdapt advises spreading larger optimizations over several days and allowing two to three days for a change to take effect before tweaking the next thing, because the bidding model needs time to relearn.

### Overpacing

The campaign will exhaust budget before the flight ends, risking a dark period:

1. Set or lower a daily cap so spend cannot front-load.
2. Switch to an even or evenly distributed pacing mode if it was set to spend as fast as possible.
3. Verify the flight dates are what you intended. A flight shorter than planned overpaces by definition.
4. If automated bidding is buying cheap, low-quality inventory fast, tighten inventory and brand-safety filters and reset the goal. See `stackadapt-bidding-and-budgets`.

### Weak performance: high eCPC, high eCPA, low CTR, low completion

Delivery is fine but the outcome is weak. This is usually a creative, placement, or audience-relevance problem, not a delivery bug. Segment before you act:

1. Pull performance broken out by creative, domain or app, channel, device, and audience to find where the metric collapses. The `stackadapt-reporting-and-attribution` skill covers report design and the breakdowns to request.
2. Exclude the worst-performing domains or apps. Adding a chronically underperforming domain to an exclusion list is a standard StackAdapt optimization and improves eCPC and eCPA.
3. Rotate or refresh creative where CTR or completion is weak. Native fatigues; refresh headlines, images, and thumbnails. For video and CTV, check that the format and length match the placement.
4. Tighten audience relevance: prune broad segments, lean on the audiences and retargeting pools that convert, and re-weight budget toward them.
5. Re-check the bid goal. If you set an aggressive CPA or CPC goal that starves delivery of quality inventory, loosen it so the model can buy what converts. Bid-goal tuning is in `stackadapt-bidding-and-budgets`.
6. Give every change two to three days before judging it. After day one results are not a true indicator; the campaign ramps and learns on day two, and trends in supply sources and domains become readable from day three onward.

### Creative disapproved or not serving

A creative cannot serve until it is approved for the channel. Native, display, video, CTV, audio, and DOOH each have their own asset specs, and each media owner reviews independently, so a creative can be live on some supply and rejected on others:

1. Open the creative status and read the media-owner-level approval state. StackAdapt surfaces which partners approved, rejected, or are still reviewing, and why a creative was rejected, so you do not have to guess.
2. Fix the cause: wrong format or size for the channel, a content-policy violation, a broken or non-compliant landing page, or a missing required asset.
3. Resubmit. Review restarts and the creative returns to pending until it is approved again.
4. If only some media owners rejected it while others approved, you can keep delivering on the approved supply while you fix or dispute the rest. Do not pause the whole campaign for a partial rejection.

### Conversions not firing or not attributing

If impressions are delivering but conversions are zero or far below plan, suspect measurement before media:

1. Confirm the StackAdapt pixel is installed and firing on the conversion page. The universal pixel plus an event for the action (purchase, form fill) is what records a conversion. Validate that the event actually fires on the live page before blaming media.
2. Confirm the conversion event is mapped to the campaign and to the conversion goal you are optimizing toward. An unmapped event records nothing against the campaign.
3. For server-to-server setups, confirm the server-side or universal-event pixel is sending events with the correct identifiers. StackAdapt supports a server-side pixel for conversion tracking, retargeting, and lookalikes in both universal-event and standalone formats.
4. Confirm you are reading the right attribution window and the right conversion type (click-through versus view-through). These differ a lot. Window and path mechanics live in `stackadapt-reporting-and-attribution`.
5. Allow time. View-through and offline conversions lag, so a fresh "no conversions" reading is usually incomplete, not real. Wait for the data to mature before re-optimizing.

## Decision rules and thresholds

- **Find the single binding constraint before touching anything.** The triage flow and the delivery-loss model exist to identify it. Fixing a non-binding lever wastes a flight.
- **One lever at a time, then wait two to three days.** The bidding model relearns after each change. Simultaneous changes make the cause unknowable.
- **No data before day one is over.** Do not judge or pause a campaign on day-one numbers. Wait for a baseline of results, whichever way they point.
- **Match the bid to the channel.** A single bid across native and CTV underdelivers the expensive channel. Bid per channel to its floor.
- **Loosen the tightest targeting layer first.** Over-narrow targeting, not low bids, is the most common cause of a thin pool.
- **Measurement before media on missing conversions.** Validate the pixel and the event mapping before concluding the audience or bid is at fault.
- **A partial creative rejection is not a full stop.** Keep delivering on approved media owners while you fix the rest.

## Common pitfalls

- **Changing many levers at once.** Move one, let it run, read the result. This is the single most important discipline.
- **Pausing too early.** Pulling the plug on day one starves the model of the data it needs to optimize. Give it a baseline.
- **Sharing one bid across channels.** Native and display floors are low; CTV, premium video, and DOOH are high. One bid cannot win all of them.
- **Trusting fresh conversion data.** View-through and offline conversions lag. Do not declare "no conversions" or re-optimize on data only a few hours old.
- **Reading the wrong conversion column.** Click-through and view-through differ a lot. Confirm the type and the attribution window before concluding media is failing.
- **Treating viewability or completion as a loss bucket.** They are quality metrics. Fix them with inventory mix and prebid thresholds, not by raising the bid.
- **Fixing a small loss bucket.** Always fix the largest one first.

## Sources

- StackAdapt API documentation (platform surfaces, channels, pixel): https://docs.stackadapt.com (as of June 2026)
- Build your own advertising platform with the StackAdapt API (channels: native, display, video, CTV, audio, in-game, DOOH): https://www.stackadapt.com/enterprise-api-solution (as of June 2026)
- Optimize your campaigns with Suggestions Hub (bid, domain-exclusion, and goal suggestions after one day): https://www.stackadapt.com/resources/blog/suggestions-hub (as of June 2026)
- Marketers, stop pausing campaigns too early (learning period, day-one to day-three behavior, two-to-three-day change windows): https://www.stackadapt.com/resources/blog/pausing-digital-campaigns (as of June 2026)
- Programmatic campaign reporting 101 (mid-flight checks, pacing, goal-dependent metrics): https://www.stackadapt.com/resources/blog/programmatic-campaign-reporting (as of June 2026)
- StackAdapt server-side pixel (conversion tracking, retargeting, lookalikes; universal-event and standalone formats): https://github.com/StackAdapt/stackadapt-gtm-server-side-pixel (as of June 2026)

Media-owner-level creative approval visibility, pixel-event mapping detail, and pacing-mode names are described here as general StackAdapt practice. The platform's in-app help (StackAdapt Academy at learn.stackadapt.com) documents the exact UI steps but is gated behind a login, so the operational rules above are stated as practice rather than cited to a public page. Confirm the current UI labels in the StackAdapt documentation when you execute.
