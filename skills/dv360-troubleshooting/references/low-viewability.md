# Playbook: low viewability

**Symptom.** The line item delivers, but the viewable rate (measured viewable impressions divided by measured impressions) is below the campaign target.

Viewability is a delivery-quality metric, not an impression-loss bucket. You do not raise it by bidding higher. You raise it by buying inventory that is structurally more viewable and by filtering out what is not, before the bid.

## Ordered checks

1. **Inventory mix.** Identify which placements, formats, and positions are dragging the average down. Below-the-fold placements, certain out-stream video, and some long-page positions are structurally low-viewability. Segment viewable rate by placement and format to find the worst offenders.
2. **Prebid viewability threshold.** Add or tighten a predicted-viewability targeting threshold so the line item only bids on impressions above a viewability likelihood. This trades some scale for quality, so widen other targeting if the pool gets too small (see `under-pacing.md`).
3. **Exclude the worst placements.** Exclude or down-weight the specific placements with the lowest viewable rates rather than lowering the global threshold, which preserves more scale.
4. **Format and position targeting.** Prefer above-the-fold and in-view positions where the line item type and creative allow.
5. **Measurement firing.** Confirm the viewability measurement vendor is actually firing on these impressions. A low measured rate can be a measurement gap (large unmeasured share) rather than genuinely poor viewability. Confirm measured rate is high enough to trust the viewable rate.

## Fix

Set a sensible prebid viewability threshold, exclude the worst placements, then rebalance targeting so scale holds. Standards, thresholds, and vendor configuration (Active View and third-party verification) live in `dv360-frequency-and-brand-safety`.

## Cross-links

- Viewability standards, IVT, and verification vendor setup: `dv360-frequency-and-brand-safety`.
- Recovering scale lost to a tighter threshold: `under-pacing.md` and `dv360-pacing-and-optimization`.
