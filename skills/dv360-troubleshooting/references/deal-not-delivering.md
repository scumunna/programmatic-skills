# Playbook: deal not delivering

**Symptom.** A PMP (Private Marketplace), Programmatic Guaranteed, or Preferred Deal is assigned but not spending.

A deal can fail to deliver on either the buy side or the sell side, and the most common buy-side cause is a mapping or priority problem rather than a bid problem. Walk both sides.

## Ordered checks

1. **Deal active on both sides.** Confirm the deal is active and not expired or paused in DV360, and that the publisher or exchange has the deal live and is sending the impressions to it. A deal that is paused or expired on the sell side delivers nothing no matter what the buy side does.
2. **Deal assigned and mapped.** Confirm the deal is attached to the line item and that the deal ID maps correctly to the inventory source. A mismatched or unassigned deal ID means the line item never sees the deal's requests.
3. **Bid meets the deal floor.** Confirm the line item bid meets or exceeds the deal's agreed floor or fixed price. A bid under the deal price loses the deal's impressions as below-minimum-bid.
4. **Line item targeting does not exclude the deal.** Confirm targeting and exclusions on the line item are not filtering out the deal's inventory (geo, brand-safety, viewability thresholds, or inventory exclusions that happen to remove the deal's domains or apps). Over-broad exclusions silently starve a deal.
5. **Priority for guaranteed deals.** For Programmatic Guaranteed, confirm the line item priority is high enough that the guaranteed deal is not outbid by your own open-auction or PMP line items in the internal auction. Guaranteed inventory must be prioritized to meet its commitment.
6. **Budget and pacing.** Confirm the line item has budget and is pacing so it can actually buy the deal's available volume across the flight.

## Fix

Confirm the deal is live on both sides, mapped to the line item, priced at or above the floor, not excluded by targeting, and (for guaranteed) prioritized. The full deal activation and non-delivery tree, including deal types and sell-side coordination, lives in `dv360-deals-and-inventory`.

## Cross-links

- Deal types, activation, and the complete non-delivery tree: `dv360-deals-and-inventory`.
- Internal-auction priority and bidding against your own line items: `low-win-rate.md`.
- Exclusions that can remove deal inventory: `dv360-frequency-and-brand-safety`.
