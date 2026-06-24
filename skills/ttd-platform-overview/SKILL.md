---
name: ttd-platform-overview
description: Orient on what The Trade Desk is, where it sits in the programmatic stack, and how its platform is generationally organized. Use when the user asks "what is The Trade Desk", "Kokai", "TTD platform overview", "is The Trade Desk an independent DSP", "Koa AI", "what does Koa do", "TTD omnichannel", "does The Trade Desk own media", "self-service vs managed service on TTD", or "how is The Trade Desk different from Google DV360 or Amazon DSP". This is the entry point for the TTD skill set; it routes to the sibling TTD skills for setup, targeting, bidding, inventory, identity, measurement, and automation.
---

# The Trade Desk platform overview

Establish what The Trade Desk (TTD) is, why its independence is the whole pitch, and how the
platform is organized so the rest of the TTD skill set makes sense. The Trade Desk is the
largest independent demand-side platform (DSP) for the open internet. It is buy-side only and
does not own or operate media, which is the basis for its positioning as an objective partner
that prioritizes inventory on the advertiser's behalf rather than its own. This skill is the
orientation layer. It does not walk through in-platform setup; it points you to the sibling
skill that does.

This skill assumes you already know what a DSP, a CPM, an auction, and a funnel stage are. For
those definitions and the shared KPI math, see the `programmatic-foundations` skill. For
choosing the right report once a campaign is live, see the `reporting-by-campaign-goal` skill.

A sourcing note that governs this entire skill set: The Trade Desk's operational knowledge base
and API reference sit behind a partner login, and the in-platform help is only visible to
logged-in seat holders. Everything here is drawn from public pages. Where an exact menu path,
field name, endpoint, or number would require platform access, this skill states the publicly
known concept and flags that the specifics live in the partner platform. It does not invent
screen names or values.

## When to use this skill

- "What is The Trade Desk?" or "what does TTD do?"
- "Is The Trade Desk an independent DSP?" or "does The Trade Desk own media?"
- "What is Kokai?" or "what platform generation is TTD on now?"
- "What is Koa?" or "what does Koa AI actually do?"
- "What channels does The Trade Desk run?" or "is The Trade Desk good for connected TV?"
- "Self-service or managed service on The Trade Desk?"
- "How is The Trade Desk different from a walled garden like Google DV360 or Amazon DSP?"
- The user is new to the TTD skill set and needs routing to the right sibling skill.

Boundary with sibling skills. This skill orients and routes. It does not configure anything.
The moment the question becomes "how do I build, target, bid, deal, identify, measure, or
automate," hand off using the routing table below. Define and orient here; act there.

## Quick reference

| The user wants | Answer or route to |
| --- | --- |
| What TTD is and why independence matters | "What The Trade Desk is" below |
| The current platform generation (Kokai) and Koa AI | "Platform generation and Koa" below |
| Which channels TTD covers | "Channels" below |
| Self-service vs managed-service | "Service models" below |
| How TTD differs from a walled garden | "Independence and objectivity" below |
| The account and campaign hierarchy | `ttd-campaign-structure` |
| Targeting, audiences, data | `ttd-targeting-and-audiences` |
| Bidding and optimization | `ttd-bidding-and-optimization` |
| Inventory, PMP and programmatic guaranteed deals | `ttd-inventory-and-deals` |
| Identity, UID2, cookieless | `ttd-identity-and-uid2` |
| Reporting, attribution, measurement | `ttd-measurement-and-reporting` |
| API and bulk automation | `ttd-api-and-automation` |

## What The Trade Desk is

The Trade Desk is a demand-side platform: software that advertisers and their agencies use to
buy programmatic advertising across the open internet through real-time auctions and deals. The
defining facts, all from public company pages:

- **Independent and the largest of its kind.** It is positioned and widely described as the
  largest independent DSP for the open internet, distinct from platforms owned by the large
  media companies.
- **Buy-side only, no owned media.** In its own words, "we don't own media. We just help you
  buy it better," and "because we don't own or operate media, we can help you objectively
  prioritize inventory." This is the structural difference from a walled garden.
- **Omnichannel.** A single platform to plan, execute, and measure media buying across channels
  rather than one channel in isolation.

Read independence as the product, not a slogan. Because TTD has no inventory to favor, its
auction and optimization can prioritize what performs for the advertiser. That is the lever the
rest of the skill set keeps pulling.

## Platform generation and Koa

**Kokai** is the current generation of The Trade Desk platform. The Trade Desk launched Kokai on
June 6, 2023, describing it as a new approach that distributes artificial intelligence across
the media buying process, with new measurement tools, streamlined partner integrations, and a
reworked user experience. Treat "Kokai" as the name of the current platform experience a trader
logs into, not a separate product to buy.

**Koa** is The Trade Desk's AI layer. Per the Kokai announcement, Koa launched in 2018 and
"assisted the marketer in setting up campaigns based on business objectives and optimizing based
on performance"; Kokai then "distributes the power of Koa's AI across various aspects of media
buying on The Trade Desk platform." Koa is also publicly described as an AI forecasting engine.
So at the level this skill supports, Koa is the assistive intelligence that helps with setup
recommendations, optimization, and forecasting inside the platform.

What requires platform access: the exact Koa recommendations surfaced in a given seat, the
specific optimization controls, and how each one is configured are in-platform behaviors that
change over releases. Describe Koa as setup, optimization, and forecasting assistance, and route
configuration questions to `ttd-bidding-and-optimization`. Do not assert specific Koa toggle
names or numeric outputs you cannot see.

## Channels

The Trade Desk lists these channels on its public platform pages. The channel determines the
available formats, inventory, and measurement, the same way it does on any omnichannel DSP.

- **Connected TV (CTV) and OTT.** Publicly highlighted as a core strength and, in reputable
  recent coverage, the company's fastest-growing channel. Treat CTV as the flagship when the
  goal is premium video reach on the open internet.
- **Display.**
- **Video** (online and in-stream video distinct from CTV).
- **Audio.** Streaming music and podcasts.
- **Native.**
- **Digital out-of-home (DOOH).**
- **Mobile** as a device context across the above.
- **Retail data and retail media.** The platform exposes retail data to target high-value
  audiences and connect omnichannel buys to sales and ROI, and retail media is a publicly
  emphasized growth area alongside CTV.

Because all channels run from one platform, the same audiences and identity graph carry across
them, which is what makes a single omnichannel buy and a unified measurement view possible. Lean
on that when planning: build the audience once, then run it on whichever channels fit the goal.
Channel-level setup is in `ttd-campaign-structure` and the targeting and inventory skills.

## Service models

The Trade Desk supports both self-service and managed-service engagement. The platform is built
as a self-serve experience for traders to plan, execute, and measure directly, and many seats
are run as a managed or hybrid service by the agency or a partner. Which model a given
organization uses is a commercial arrangement, not a product setting. For an agent, the
practical implication is the same playbooks apply; only who clicks the buttons changes.

## Independence and objectivity

This is the positioning that separates TTD from the walled gardens (for example Google DV360 and
Amazon DSP, both of which sit next to owned media and inventory). The argument, in three steps:

1. The Trade Desk does not own or operate media, so it has no house inventory to push.
2. With no inventory to favor, it can objectively prioritize whatever performs for the
   advertiser across the open internet.
3. That objectivity is the reason to use an independent DSP when you want buying decisions
   aligned to your outcomes rather than to a platform's media P&L.

Keep the claim disciplined. The defensible public statement is structural: no owned media,
therefore no inventory conflict of interest. Avoid turning that into unverifiable performance
superiority claims against named competitors. For where this matters operationally, identity is
the clearest case: see `ttd-identity-and-uid2` for how TTD pushes an open-internet identity
approach rather than a single login graph.

## Reference material

This overview has no bundled reference files; it routes to sibling skills. Open the sibling skill
named in the Quick reference table for any task beyond orientation. For DSP-agnostic definitions
and KPI formulas, open `programmatic-foundations`. For goal-to-report selection, open
`reporting-by-campaign-goal`.

## Common pitfalls

- **Calling Kokai a separate product.** Kokai is the current platform generation, the experience
  the trader uses, not an add-on to purchase. Describe it as "the current version of the
  platform."
- **Overstating what Koa does from memory.** Koa is setup, optimization, and forecasting
  assistance at the level public sources support. Specific recommendations, controls, and
  outputs are in-platform and release-dependent. Route specifics to
  `ttd-bidding-and-optimization` instead of inventing toggle names.
- **Turning independence into an unprovable performance claim.** The verified point is
  structural: no owned media, so no inventory conflict. Do not extend that into blanket "beats
  competitor X on ROI" statements.
- **Forgetting CTV is the flagship.** When the goal is premium video reach on the open internet,
  CTV is TTD's publicly emphasized strength and fastest-growing channel. Start there for
  upper-funnel video.
- **Answering in-platform setup from this skill.** This skill orients. For any build, target,
  bid, deal, identity, measurement, or automation task, hand off to the named sibling skill.

## Sources

- Our Demand Side Platform (DSP), The Trade Desk (independent DSP, self-serve, omnichannel, "we
  don't own media. We just help you buy it better," "because we don't own or operate media, we
  can help you objectively prioritize inventory," Frost Radar leader):
  https://www.thetradedesk.com/us/our-platform/dsp-demand-side-platform (as of June 2026)
- Our platform, The Trade Desk (channel list: Audio, CTV / OTT, Digital out-of-home, Display,
  Mobile, Native, Video; retail data; self-serve): https://www.thetradedesk.com/us/our-platform
  (as of June 2026)
- About us, The Trade Desk (independent media buying platform for the open internet, objective
  partner): https://www.thetradedesk.com/us/about-us (as of June 2026)
- The Trade Desk Launches Kokai, The Trade Desk press room (Kokai launched June 6, 2023;
  distributed AI; Koa launched 2018 and assisted setup and optimization; CTV and retail
  measurement):
  https://www.thetradedesk.com/press-room/the-trade-desk-launches-kokai-a-new-media-buying-platform-that-brings-the-full-power-of-ai-to-digital-marketing
  (as of June 2026)
- The Trade Desk, Wikipedia (largest independent demand-side platform in the world; Koa described
  as an AI forecasting engine; Kokai; Unified ID 2.0):
  https://en.wikipedia.org/wiki/The_Trade_Desk (as of June 2026)
- What is Driving Trade Desk's Rapid CTV and Retail Media Growth, Yahoo Finance / Zacks (CTV the
  company's fastest-growing channel in Q3 2025; retail media momentum):
  https://finance.yahoo.com/news/driving-trade-desks-rapid-ctv-163500468.html (as of June 2026)

Operational specifics that require The Trade Desk platform or partner access (not cited above
because the relevant pages sit behind a partner login): the live Koa recommendations and
optimization controls in a seat, the exact in-platform menus and field names, the API reference,
and any rate-card or performance figures specific to an account. For those, use the partner
platform and its in-platform help.
