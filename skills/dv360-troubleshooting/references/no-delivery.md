# Playbook: no delivery / zero impressions

**Symptom.** A line item or insertion order shows zero impressions or zero spend, or delivery stopped abruptly.

Zero delivery is almost always a hard gate (status, eligibility, or an empty pool), not a soft bidding inefficiency. Work the gates top to bottom and stop at the first one that fails.

## Ordered checks

1. **Parent chain status.** Confirm the line item, its insertion order, its campaign, and the advertiser are all active. A paused, ended, or archived parent zeroes out everything beneath it. This is the single most common cause of sudden zero delivery.
2. **Flight dates.** Confirm today is inside the line item flight and the insertion order flight. A flight that has not started or has already ended delivers nothing. Check the time zone of the flight against the current time.
3. **Budget remaining.** Confirm the line item and insertion order have unspent budget in the current pacing period, and that the insertion order cap has not already been consumed by sibling line items. If the cap is hit, this line item starves even with its own budget left.
4. **Creative eligibility.** Confirm at least one creative is assigned and its status is Approved or Servable. Pending and Rejected creatives do not serve, so a line item whose only creative is pending or rejected shows zero delivery. See `creative-issues.md`.
5. **Creative compatibility.** Confirm the creative size, format, and type match the line item type and the inventory. A display line item with only a video creative, or sizes no exchange requests, will not serve.
6. **Bid versus floor.** Confirm the bid clears the floor for the inventory targeted. A fixed bid set below typical floors, or an automated strategy capped too low, loses every auction as "below minimum bid".
7. **Targeting size.** Confirm the addressable pool is not empty after every targeting layer is intersected. Incompatible combinations (for example desktop-only targeting against mobile-app inventory, or a tiny geo crossed with a small audience and a narrow daypart) can drive the pool to zero. Remove layers one at a time to find the killer.
8. **Inventory or deal.** Confirm there is matching supply. For a deal, confirm it is active, assigned, mapped, and prioritized so it can win. See `deal-not-delivering.md`.

## Fix

Fix the first failing gate, then let the line item run before judging it. Use the official Troubleshooter and the Impressions lost chart to confirm where bids were filtered: by line item settings, by creative requirements, or in the auction. The Fix spend problems troubleshooter walks the same gates interactively.

## Cross-links

- Pacing and budget mechanics: `dv360-pacing-and-optimization`.
- Bid and floor strategy: `dv360-bid-strategy`.
- Deal activation and mapping: `dv360-deals-and-inventory`.
