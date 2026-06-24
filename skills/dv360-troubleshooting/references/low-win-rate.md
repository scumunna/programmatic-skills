# Playbook: low win rate

**Symptom.** The line item is bidding into auctions but wins a small fraction of them.

Win rate is bids won divided by bids submitted. A low win rate means your bid loses, your request is filtered before the auction, or you are competing against yourself. Separate those three causes before raising the bid, because raising the bid does nothing if the loss is prebid filtering or internal competition.

## Ordered checks

1. **Floor versus bid.** Confirm the bid clears typical floor prices for the inventory targeted. If most loss is the below-minimum-bid bucket, the bid is simply under the floor. Raise the fixed bid or lift the ceiling on the automated strategy.
2. **Internal versus external loss.** In the loss breakdown, distinguish auctions lost internally (to your own higher-priority line items in the same insertion order) from auctions lost externally (to other buyers on the exchange). Internal loss is fixed by rebalancing priority and budget across your line items, not by bidding higher.
3. **Prebid filtering.** Use the deals and line items Troubleshooter to see whether requests are removed before the auction by brand-safety controls, invalid-traffic filters, or unauthorized-seller (sellers.json or ads.txt) rules. Filtered requests never reach a bid, so they depress effective win rate. Loosen or correct the offending filter if it is over-broad.
4. **Strategy ceiling.** Confirm an automated strategy is not capped below market. A Target CPA, Target CPM, or max bid that is too low forces the algorithm to bid under winning levels. Raise the target or ceiling, then allow the learning period to settle. Strategy selection lives in `dv360-bid-strategy`.
5. **Inventory competitiveness.** Some premium or scarce inventory is structurally hard to win at any reasonable bid. If the targeted supply is highly contested, expand to comparable inventory rather than overpaying.

## Fix

Address the dominant loss cause: raise the bid only when loss is below-minimum-bid or external-auction; rebalance priorities when loss is internal; correct filters when loss is prebid. After any change, let the auction stabilize and the strategy relearn before re-measuring.

## Cross-links

- Bid strategy, targets, and learning periods: `dv360-bid-strategy`.
- Brand-safety and IVT filters that remove requests prebid: `dv360-frequency-and-brand-safety`.
- Deal floors and priority: `dv360-deals-and-inventory`.
