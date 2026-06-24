---
name: stackadapt-inventory-and-brand-safety
description: Choose StackAdapt supply and lock down brand safety. Use when the user asks about StackAdapt inventory, open exchange vs StackAdapt deals or PMP, StackAdapt CTV inventory, programmatic guaranteed or preferred deals, Deal IDs, StackAdapt brand safety, domain or app exclusion and inclusion lists, category and contextual avoidance, viewability, fraud and invalid traffic, or third-party verification on StackAdapt.
---

# StackAdapt inventory and brand safety

Pick the supply a StackAdapt ad group runs against and put the right safety and verification
controls around it. The core tension is scale versus quality and safety: open exchange gives
reach and price, deals give premium and control, and safety controls keep either one off
inventory that would hurt the brand. This skill is the supply-and-safety decision; it is applied
per ad group because the ad group is the line item on StackAdapt.

StackAdapt is a self-serve multi-channel demand-side platform, strongest in native and also
running display, video, connected TV, audio, in-app, and digital out-of-home. For where this
sits in the build flow, see `stackadapt-campaign-setup`. For KPI math and definitions of
viewability, CPM, and the like, see the `programmatic-foundations` skill. For how supply choices
read out in reporting, see `stackadapt-reporting-and-attribution`.

## When to use this skill

- "What inventory should this StackAdapt campaign run on?" / "Open exchange or a deal?"
- "Set up a StackAdapt deal or PMP." / "How do Deal IDs work on StackAdapt?"
- "Get me premium CTV inventory on StackAdapt."
- "Lock down brand safety." / "Add a domain or app exclusion list." / "Block these categories."
- "What verification does StackAdapt support?" / "How do I get viewability and IVT data?"

Boundaries with sibling skills:
- The end-to-end campaign build and where each setting lives: `stackadapt-campaign-setup`.
- Audience construction and contextual targeting (the who, not the where): `stackadapt-targeting-and-audiences`.
- Bid and budget sizing against the supply you picked: `stackadapt-bidding-and-budgets`.
- Reading inventory and viewability performance in reports: `stackadapt-reporting-and-attribution`.
- Fixing a deal that is not delivering or scaling supply mid-flight: `stackadapt-optimization-and-troubleshooting`.

## Quick reference

Supply types, ranked roughly from most scale to most control. Match the buy to the goal:

| Supply type | Auction | Price | Best for |
| --- | --- | --- | --- |
| Open exchange (open marketplace, RTB) | Open real-time auction | Lowest, market-set | Scale, prospecting, broad reach and retargeting, budget efficiency |
| Private marketplace (PMP) | Invite-only private auction | Higher, still bid | Premium placements, a publisher's first-party data, premium CTV, more transparency |
| Preferred deal | No auction, fixed CPM | Fixed, negotiated | Priority over PMP at a set price without reserving volume |
| Programmatic guaranteed (PG) | No auction, reserved | Fixed, negotiated | Guaranteed delivery and strict placement control: regulated verticals, tentpoles, premium CTV |

Safety layers, applied per ad group on top of whatever supply you chose:

| Layer | Control | Purpose |
| --- | --- | --- |
| Supply selection | Open vs deal, and which exchanges | Deals are inherently more curated than the open exchange |
| Domain and app lists | Exclusion (blocklist) or inclusion (allowlist) | Keep off bad domains/apps, or restrict to vetted ones |
| Category and contextual | Avoid sensitive categories and keywords | Stay out of content that clashes with the brand |
| Pre-bid filtering | Screen the page, app, or stream before bidding | Avoid risky placements before spend, not after |
| Post-impression verification | Viewability, IVT/fraud, suitability scoring | Confirm where ads landed and feed it back |

## Core process

1. Start from the goal and pick the supply tier. Prospecting and broad reach on a tight CPM go
   to the open exchange; premium environments, a publisher's first-party data, or premium CTV go
   to a PMP; guaranteed delivery and tight placement control (regulated verticals, short flights,
   tentpole competition) go to programmatic guaranteed. Open exchange is the most cost-efficient
   and scalable; each step toward a deal trades price for control and quality.
2. For a deal, get or request the Deal ID. StackAdapt offers pre-packaged deals across channels
   and supply sources, and the StackAdapt Partnerships team builds custom deals when the
   pre-packaged set does not cover the publisher, format, or audience you need (including
   tentpole and vertical-specific deals). A pre-negotiated deal from a publisher is brought in by
   its unique Deal ID. Request custom deals with enough lead time before the flight.
3. Attach supply to the ad group. Apply supply selection per ad group so different audiences can
   run against different supply. Keep one ad group's supply coherent so you can read its
   performance cleanly later.
4. Set the domain and app lists. Choose exclusion (blocklist) to keep off known-bad or
   off-brand domains and apps, or inclusion (allowlist) to restrict delivery to a vetted set.
   On the open exchange in particular, a domain inclusion list is the lever that buys back
   control without giving up the exchange's scale. Reuse a maintained account-level list rather
   than hand-typing domains per campaign.
5. Set category and contextual avoidance. Exclude sensitive content categories and add keyword
   or contextual exclusions so ads stay out of content that clashes with the brand. Match the
   strictness to the client's risk tolerance and vertical; a regulated advertiser needs tighter
   avoidance than a performance prospecting push.
6. Layer verification. Pre-bid filtering screens the page, app, or stream before the bid so risky
   placements are avoided before spend. Post-impression, third-party verification adds viewability
   and invalid-traffic (fraud) measurement on top of StackAdapt's internal IVT and brand-safety
   tooling. StackAdapt integrates DoubleVerify for post-impression viewability and fraud
   measurement. DoubleVerify, Integral Ad Science, and Oracle are the widely used verification
   providers; confirm current availability and what is in scope for the account in the StackAdapt
   help center before promising a specific integration.
7. Balance scale against safety, then verify it can still deliver. Every list and avoidance layer
   shrinks the addressable pool. After stacking controls, confirm the ad group can still spend its
   budget across the flight. If a tight allowlist plus category avoidance starves delivery, either
   loosen a layer or move premium-only goals to a PMP or PG deal where the inventory is reserved.

## Decision rules and thresholds

- Open exchange is the default for scale and efficiency; reach for a deal when you need premium
  placements, a publisher's first-party data, premium CTV, or guaranteed delivery. Do not buy a
  PG deal to do a job the open exchange plus an inclusion list can do for less.
- PMP when you want premium and transparency but can tolerate auction price movement and
  no volume guarantee. PG when the campaign cannot tolerate missing inventory: regulated
  verticals, short-duration flights, or high-competition tentpole windows. Preferred deal when you
  want fixed-price priority above PMP without reserving volume.
- CTV usually runs as a deal. CTV premium supply commonly comes through PMP or PG for transparency
  and guaranteed access, and CTV is effectively clickless, so plan to measure it by view-through
  (hand the measurement design to `stackadapt-reporting-and-attribution`).
- Exclusion list to keep off a known-bad set, inclusion list to restrict to a vetted set. An
  inclusion list is stricter and safer but caps scale hard; only use one when the brand's risk
  tolerance demands it or when a buy is meant to run on a defined publisher set.
- Match avoidance strictness to the vertical and risk tolerance. Tighten category, keyword, and
  contextual avoidance for regulated or sensitive brands; loosen for broad performance prospecting
  where over-blocking would choke delivery and inflate CPMs.
- Pre-bid prevents spend on bad inventory; post-impression verification proves what happened and
  informs the next decision. Use both: pre-bid to stay safe, post-impression to measure and
  optimize. Do not rely on post-impression alone, since by then the spend already happened.
- After stacking supply selection plus lists plus avoidance, confirm deliverability against the
  flight before launch. If controls starve delivery, loosen the least risky layer first or switch
  the premium-only portion to reserved (PG) supply.

## Templates and examples

A regulated-vertical CTV plus open-exchange prospecting setup, filled in:

```
Campaign: ACME_Health_AwarenessConsideration_2026Q3

  Ad group: ACME_Health_CTV_Awareness_PG_2026Q3
    Supply:        Programmatic guaranteed (CTV), Deal ID from Partnerships
    Why deal:      Regulated vertical needs guaranteed delivery + strict placement control
    Domain/app:    Publisher set fixed by the PG deal
    Category:      Health-sensitive category + keyword exclusions applied
    Verification:  Pre-bid filtering on; DoubleVerify post-impression viewability + IVT
    Measurement:   View-through (CTV is clickless), hand to reporting skill

  Ad group: ACME_Health_Display_Prospecting_OpenExchange_2026Q3
    Supply:        Open exchange (RTB)
    Why open:      Scale and CPM efficiency for top-funnel prospecting
    Domain/app:    Account domain INCLUSION list (vetted publishers) to buy back control
    Category:      Health-sensitive category + keyword exclusions applied
    Verification:  Pre-bid filtering on; DoubleVerify post-impression viewability + IVT
    Deliverability: Confirmed inclusion list + avoidance still spends the budget over the flight
```

Why it is built this way: the regulated brand cannot risk missing or off-brand CTV placements, so
that ad group is reserved PG supply with the publisher set fixed by the deal; prospecting still
wants the open exchange for scale, but an inclusion list plus category avoidance keeps it
brand-safe, and deliverability was checked because those controls shrink the pool. Both ad groups
carry the same category/keyword avoidance and the same verification so the safety bar is uniform.

## Common pitfalls

- Buying a PG or PMP deal for a job the open exchange plus an inclusion list could do. Deals cost
  more and reserve effort; use them for premium, first-party data, or guaranteed delivery, not as
  a reflex.
- Over-blocking. Stacking an allowlist, broad category exclusions, and keyword avoidance until the
  ad group cannot spend, then blaming delivery on the bid. Check deliverability against the flight
  and loosen the least risky layer.
- Treating post-impression verification as prevention. Viewability and IVT scores tell you what
  already happened. Pre-bid filtering is what keeps spend off bad inventory in the first place.
- Promising a specific verification integration without checking. Confirm current availability and
  scope (for example DoubleVerify viewability and fraud) in the StackAdapt help center for the
  account before committing it to a client.
- Forgetting CTV is clickless and judging it on clicks. Plan CTV measurement around view-through
  up front with `stackadapt-reporting-and-attribution`.
- Hand-maintaining domain lists per campaign. Keep a vetted account-level inclusion or exclusion
  list and reuse it so safety is consistent and auditable.

## Sources

- [StackAdapt Developer Documentation (REST, GraphQL, Pixel API, Data Taxonomy, MCP Server)](https://docs.stackadapt.com) (as of June 2026)
- [Open Marketplace vs. Private Marketplace | StackAdapt](https://www.stackadapt.com/resources/blog/open-marketplace-vs-private-marketplace) (as of June 2026)
- [StackAdapt Custom Deals | StackAdapt](https://www.stackadapt.com/resources/blog/private-marketplace-opportunities) (as of June 2026)
- [Programmatic Guaranteed: How It Works and When to Use It | StackAdapt](https://www.stackadapt.com/resources/blog/programmatic-guaranteed) (as of June 2026)
- [Your Guide to Building a Campaign Inventory Strategy | StackAdapt](https://www.stackadapt.com/resources/blog/building-an-inventory-strategy) (as of June 2026)
- [StackAdapt and SpotX Launch Connected TV Partnership | StackAdapt](https://www.stackadapt.com/resources/blog/spotx-connectedtv-inventory) (as of June 2026)
- [StackAdapt Partners With DoubleVerify for Enhanced Post-Impression Measurement | StackAdapt](https://www.stackadapt.com/resources/blog/stackadapt-partners-with-doubleverify) (as of June 2026)
- [AI and Brand Safety in Advertising | StackAdapt](https://www.stackadapt.com/resources/blog/brand-safety-advertising) (as of June 2026)

The exact in-product screens for attaching Deal IDs, building domain and app lists, choosing
category and contextual exclusions, and enabling a verification integration are documented in the
StackAdapt help center at support.stackadapt.com. Some help center articles require a logged-in
account, so they are not cited here. Where a specific in-product default, list mechanic, or the
current scope of a verification integration is not publicly documented, the guidance above states
the operational best practice and points to the help center rather than citing a fabricated page.
