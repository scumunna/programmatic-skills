# Playbook: low CTR or engagement

**Symptom.** The line item delivers in full but click-through rate or another engagement metric (video completion, interaction rate) is below benchmark.

Low engagement is rarely a delivery bug. Delivery is working; the message, the placement, or the audience is not resonating. Diagnose by segmenting until you find where engagement collapses, then act on that segment.

## Ordered checks

1. **Segment by creative.** Break CTR or engagement out by creative. If one creative drags the average, the problem is creative, not media. Pause the laggards and shift weight to the winners.
2. **Segment by placement and inventory.** Some placements draw impressions but almost no clicks (accidental or low-attention environments). Identify the lowest-engagement placements and exclude or down-weight them.
3. **Segment by device and format.** Engagement varies by device and by format. Confirm the creative is right for the environment (for example mobile-appropriate sizes, appropriate video length) and reallocate toward formats and devices that engage.
4. **Segment by audience.** If engagement is poor across all creatives and placements, the audience may be poorly matched. Tighten to higher-intent segments or revisit the audience strategy in `dv360-targeting-and-audiences`.
5. **Creative fatigue.** If engagement was healthy and decayed over the flight, the audience has seen the creative too many times. Refresh the creative or tighten the frequency cap. Frequency design lives in `dv360-frequency-and-brand-safety`.

## Fix

Act on the worst-performing segment first: rotate or refresh creative, prune low-engagement placements, or re-aim the audience. Make one change, let it accumulate enough impressions to be significant, then re-segment. Engagement is noisy at low volume, so wait for a meaningful sample before concluding.

## Cross-links

- Audience strategy and segment selection: `dv360-targeting-and-audiences`.
- Frequency caps and creative fatigue: `dv360-frequency-and-brand-safety`.
- Reading and segmenting the metrics: `dv360-reporting`.
