# Playbook: under-pacing

**Symptom.** The line item is delivering but is behind its prorated target and will not finish the flight at the current rate.

Under-pacing means impressions are being lost to a constraint. Identify the binding constraint from the Impressions lost chart, then raise that one lever. Raising every lever at once wastes budget and hides which change worked.

## Ordered checks

1. **Read the loss buckets.** Open the Impressions lost chart and rank the buckets: auctions lost, below minimum bid, budget or pacing, frequency limited, no eligible creative. The largest bucket is your target.
2. **Below minimum bid or auctions lost (the bid is too low).** If most loss is below-minimum-bid or external-auction loss, the bid is uncompetitive. Raise the fixed bid, or raise the Target CPA or max bid ceiling on an automated strategy so it can clear floors and win. Hand strategy choice to `dv360-bid-strategy`.
3. **Auctions lost, internal (you outbid yourself).** If loss is internal-auction, a higher-priority line item in the same insertion order is taking the impressions. Rebalance priorities or budgets across the line items.
4. **Targeting too narrow (thin pool).** If win rate is high but volume is low, the addressable pool is too small. Broaden geo, audiences, devices, or dayparts, or relax a viewability or inventory threshold. A high win rate on a tiny pool still under-delivers.
5. **Frequency limited.** If the frequency-limited bucket is large, the cap is throttling reachable users. Loosen the cap or widen the audience so there are more uncapped users to serve. Cap design lives in `dv360-frequency-and-brand-safety`.
6. **Budget below absorbable spend.** If the line item spends its daily allowance early and then idles, the pool can absorb more than the budget allows. Raise the line item budget or shift budget from an over-funded sibling.
7. **Pacing mode.** Confirm the pacing mode fits the goal. Even pacing scales to inventory; if the flight is short or front-loaded demand is fine, ASAP delivers faster. Pacing-mode selection and math live in `dv360-pacing-and-optimization`.

## Fix

Change one lever, let it run long enough to clear any learning effect, then re-read the loss buckets. Repeat against the new largest bucket. Document each change so the cause of improvement is attributable.

## Cross-links

- Pacing modes and pacing math: `dv360-pacing-and-optimization`.
- Bid strategy and learning periods: `dv360-bid-strategy`.
- Frequency caps: `dv360-frequency-and-brand-safety`.
