# DV360 launch QA: full checklist

Work this top to bottom before go-live. Mark each item pass, fail, or not applicable with a short note. A failed item blocks launch until fixed and re-checked. Items marked best practice reflect standard ad-ops discipline rather than a single documented page; items tied to product behavior are backed by the Sources in the parent SKILL.md.

For the how-to behind any area, see the sibling skill named in the parent SKILL.md (bid strategy, deals and inventory, frequency and brand safety, reporting, troubleshooting, account setup and taxonomy).

---

## 1. Campaign, insertion order, and line item setup

- [ ] Campaign exists under the correct advertiser.
- [ ] Campaign, insertion order, and line item names follow the team naming convention (see `dv360-account-setup-and-taxonomy`). Best practice.
- [ ] Every insertion order is attached to the campaign and every line item is attached to the right insertion order.
- [ ] Line item types (display, video, audio, and so on) match the media plan. Best practice.
- [ ] No orphaned or duplicate entities left over from drafting. Best practice.
- [ ] Each line item has at least one creative assigned (serving requires an approved assigned creative).
- [ ] Owner and point of contact recorded for the campaign. Best practice.

## 2. Flight, budget, and pacing

- [ ] Start and end dates set correctly at campaign, insertion order, and line item. Best practice.
- [ ] Timezone is the advertiser's billing timezone, so flights start and end on the intended day. Best practice.
- [ ] Budget cap set at the insertion order. Uncapped spend is the most expensive mistake.
- [ ] Budget cap set at the line item.
- [ ] Line item budgets sum to the insertion order budget and reconcile to the booked buy. Best practice.
- [ ] Pacing model (even, ahead, or as-fast-as-possible) chosen deliberately per the plan and the flight length.
- [ ] Budget type (impressions or amount) matches how the buy was sold. Best practice.
- [ ] For short flights, pacing will not exhaust the budget on day one. Best practice.

## 3. Bidding

- [ ] Bid strategy matches the line item KPI (see `dv360-bid-strategy`).
- [ ] Goal value (target CPA, target CPM, target ROAS, or fixed bid) set to the agreed number. Best practice.
- [ ] Bid floors and caps are sane and will not starve delivery or overpay. Best practice.
- [ ] For automated strategies, the line item has enough budget and conversions to learn. Best practice.
- [ ] Any custom bidding or value rules are attached to the right line items. Best practice.

## 4. Targeting, audiences, and exclusions

- [ ] Geo targeting matches the brief, with the right include and exclude regions. Best practice.
- [ ] Audience targeting matches the plan; audience lists are populated and large enough to deliver. Best practice.
- [ ] Language, device, environment, and operating-system targeting match the plan. Best practice.
- [ ] Day-part and ad-scheduling set if required. Best practice.
- [ ] Inventory and content exclusions applied (the advertiser brand-safety floor plus any campaign-specific exclusions).
- [ ] Negative keyword and URL or app exclusions applied where required.
- [ ] No conflicting include and exclude targeting that zeroes out reach. Best practice.
- [ ] Inherited default targeting reviewed and overridden where it does not fit. Defaults cascade from the partner and insertion order.

## 5. Inventory and deals

- [ ] Each deal ID is active and not expired or paused (see `dv360-deals-and-inventory`).
- [ ] Each deal is assigned to the intended line items and not orphaned or mis-assigned. Best practice.
- [ ] Inventory source type (open auction, private auction, preferred, programmatic guaranteed) matches the plan. Best practice.
- [ ] Programmatic guaranteed and preferred deal terms (price, impression commitment) match the agreement. Best practice.
- [ ] Deal-level floor prices are consistent with the bid strategy. Best practice.

## 6. Brand safety, verification, and viewability

- [ ] Brand suitability tier and content exclusions set per the advertiser policy and the campaign brief.
- [ ] Digital content labels and sensitive category exclusions applied.
- [ ] Third-party verification (for example a verification vendor) enabled where required.
- [ ] Viewability target set or measured where the buy is sold on viewable impressions. Best practice.
- [ ] Invalid-traffic and authorized-seller posture consistent with the advertiser settings.

## 7. Creatives, trafficking, landing pages, and tracking

- [ ] Every creative is approved and Servable, not pending or rejected (review starts automatically and can take time, so confirm at QA).
- [ ] Creative sizes and formats match the line items and the inventory they target. Best practice.
- [ ] Click-through URLs are correct, live, and land on the intended page. Best practice.
- [ ] Landing pages load, are the right pages, and are mobile-friendly where relevant. Best practice.
- [ ] Impression and click trackers (and any third-party tags) are attached and correctly formed. Best practice.
- [ ] Conversion tracking is linked at the advertiser (Floodlight or the conversion setup) and a test or recent conversion is recording. Optimizing to conversions with broken tracking wastes budget.
- [ ] UTM or campaign parameters on click-throughs are correct for downstream analytics. Best practice.
- [ ] Creative rotation or optimization setting is intentional. Best practice.

## 8. Frequency

- [ ] Frequency cap set at the appropriate level (campaign, insertion order, or line item) for the objective.
- [ ] Cap count and time window fit the objective (tighter for awareness reach, looser for performance). Best practice.
- [ ] No unintended stacking of caps across levels that over-restricts or under-restricts delivery. Best practice.

## 9. Reporting and alerts

- [ ] Scheduled reports configured for the campaign owner and stakeholders (see `dv360-reporting`). Best practice.
- [ ] Pacing visibility in place so under- or over-delivery is caught early. Best practice.
- [ ] Alerts configured for budget, pacing, or delivery anomalies where supported. Best practice.
- [ ] Report dimensions and metrics match what the client or team needs to see. Best practice.

## 10. Billing and purchase order

- [ ] Purchase order or billing reference in place for the spend. Best practice.
- [ ] Partner costs, agency fees, and any third-party data or verification fees configured. Best practice.
- [ ] Billing profile and currency on the partner and advertiser are correct (see `dv360-account-setup-and-taxonomy`). Best practice.
- [ ] Total committed budget reconciles to the signed buy and the PO amount. Best practice.

---

## Sign-off (required before go-live)

- [ ] Builder self-QA complete: every group above checked.
- [ ] Peer QA complete: a second qualified person re-checked groups 2 (budget), 4 (targeting), 6 and 7 (brand safety and tracking), and 3 (bidding). Best practice.
- [ ] All failed items fixed and re-checked.
- [ ] Change freeze in effect: no edits between sign-off and go-live. Best practice.
- [ ] Go-live executed and confirmed.

## Post-launch check at 24 to 48 hours

- [ ] Delivery has started on every line item; none stuck unapproved or not serving.
- [ ] Pacing is on track against budget and flight. Best practice.
- [ ] Conversions are recording (where applicable).
- [ ] Spend matches intent and there is no runaway delivery. Best practice.
- [ ] No deal has gone inactive and no tracker has silently stopped. Best practice.
- [ ] Hand off any non-delivery to `dv360-troubleshooting`.
