---
name: amazon-dsp-bidding-and-optimization
description: Choose the optimization goal and tune bidding and budget on an Amazon DSP campaign. Use when the user asks about Amazon DSP bidding, Amazon DSP optimization, DSP bid strategy, how to optimize an Amazon DSP campaign, DSP budget pacing, which optimization goal to pick (reach, cost per click, cost per action, return on ad spend, video completion rate, detail page view rate), bid optimization, supply and audience optimization, in-flight management, or why a line item is underdelivering.
---

# Amazon DSP bidding and optimization

Pick the optimization goal that matches the campaign objective, then let Amazon DSP bid toward it
and manage budget so the line item delivers efficiently. The optimization goal is the single most
consequential setting on a line item: it tells the system what a good impression is, and every bid,
supply decision, and pacing choice flows from it. Set it wrong and the algorithm optimizes hard
toward the wrong outcome.

Amazon DSP is Amazon's programmatic demand-side platform for display, video, streaming TV, and audio
across Amazon properties and third-party exchanges. It is distinct from Amazon Ads sponsored ads
(Sponsored Products, Sponsored Brands, Sponsored Display), which are keyword and cost-per-click
retail-search ads with no order, line item, or optimization-goal model. There are no keyword bids or
ASIN bids here; if the request is about bidding on search terms, it is sponsored ads, not the DSP.

This skill assumes you know what a CPM, CPC, CPA, ROAS, and a video completion rate are. For those
definitions and the KPI math, see the `programmatic-foundations` skill. For which report proves a
goal was met, see the `reporting-by-campaign-goal` skill.

## When to use this skill

- "What optimization goal should I use on this Amazon DSP line item?"
- "Optimize my Amazon DSP campaign." / "Why is this line item underdelivering or overspending?"
- "Set up bidding for reach / CPC / CPA / ROAS / video completion / detail page view rate."
- "What is supply optimization vs audience optimization on Amazon DSP?"
- "How do I pace an Amazon DSP budget?" / "DSP budget pacing." / "It spent too fast."
- "Should I cap the bid?" / "Why won't this line item win auctions?"

Boundaries with sibling skills:
- Where the line item sits (advertiser, order, line item, product types): hand off to
  `amazon-dsp-account-structure`.
- The full click path for creating an order and its line items in order: hand off to
  `amazon-dsp-campaign-setup`. This skill is the goal-and-bidding logic that step depends on.
- Choosing exchanges, deals, PMP, and programmatic guaranteed supply: hand off to
  `amazon-dsp-inventory-and-supply`. This skill covers how supply optimization reshapes a chosen pool,
  not how to choose the pool.
- Building and layering the audience: hand off to `amazon-dsp-audiences`. This skill covers how
  audience optimization expands within a chosen audience.
- Reading detail page views, new-to-brand, ROAS, and attribution windows: hand off to
  `amazon-dsp-measurement-and-reporting`.
- Setting any of this through the API: hand off to `amazon-dsp-api-and-automation`.

## Quick reference

Map the objective to the goal first; everything else follows.

| Campaign objective | Optimization goal | Why |
| --- | --- | --- |
| Maximum unique reach, awareness | Reach | Bids toward unique users, not repeat impressions |
| Drive traffic, clicks | Cost per click (CPC) | Bids toward the click at a target cost |
| Drive a conversion or sign-up | Cost per action (CPA) | Bids toward the conversion event at a target cost |
| Revenue efficiency on Amazon | Return on ad spend (ROAS) | Bids toward sales value per ad dollar |
| Video attention, completed views | Video completion rate (VCR) | Bids toward impressions that finish the video |
| Mid-funnel retail consideration | Detail page view rate (DPVR) | Bids toward exposures that drive product page views |

Two levers the system uses to hit the goal once it is set:

- **Supply optimization.** Within the supply you chose, shift spend toward placements and exchanges
  that produce the goal outcome and away from those that do not.
- **Audience optimization.** Within the audience you chose, lean into the segments and signals that
  convert and expand toward similar high-value users.

Budget controls that decide delivery shape:

- **Pacing.** Even (spread across the flight) or accelerated (spend ahead). Even is the default and the
  right answer for most flights.
- **Budget cap.** A ceiling at the order and at the line item that the system spends against. Daily caps
  smooth delivery; total caps bound the flight.

## Core process

1. State the one objective for this line item. Awareness, consideration, traffic, conversion, or
   revenue. The objective is upstream of the goal; if you cannot name it in one phrase, resolve it
   before touching settings.
2. Pick the optimization goal that matches the objective from the table above. One goal per line item.
   The goal defines what the algorithm treats as a good impression, so a mismatch optimizes hard in the
   wrong direction (a reach goal will not chase conversions, and a CPA goal will not maximize reach).
3. Confirm the goal has signal to optimize against. Conversion and revenue goals (CPA, ROAS, DPVR) need
   a working pixel or retail signal and enough events to learn from. If the conversion volume is thin,
   start on a goal the inventory can actually produce (reach, CPC, or VCR for video) and move down the
   funnel once volume builds. Set up the pixel and events in `amazon-dsp-account-structure`.
4. Set the target where the goal takes one. A target CPA, target CPC, or target ROAS guides the bid.
   Ground the target in the channel's real clearing economics, not an aspirational number. A target the
   inventory cannot meet starves delivery because the system cannot find impressions at that price.
5. Decide the bidding mode and any cap. Let the system bid toward the goal by default. Add a bid cap or
   a floor only when you must control the price explicitly, knowing a tight cap can throttle the
   algorithm and block it from winning the valuable impressions the goal points at.
6. Set pacing and budget caps. Even pacing for a steady flight, accelerated only for a short flight or to
   gather optimization signal fast. Set a daily or total cap that matches the flight so the system has a
   ceiling to optimize within. For the full setup sequence, see `amazon-dsp-campaign-setup`.
7. Let supply and audience optimization run within the pools you chose. They reshape spend toward what
   produces the goal; that is the mechanism by which the goal becomes delivery.
8. Hold the line item stable through the learning window, then manage in flight (below). Do not judge or
   re-tune in the first days, when the algorithm is still calibrating.

## Decision rules and thresholds

### Choosing the goal

- One objective, one goal, one line item. If a slice needs a different goal, it belongs in its own line
  item so its bidding reads and optimizes independently. Splitting the objective is in
  `amazon-dsp-campaign-setup`.
- Match the goal to the funnel stage. Upper funnel: reach (unique users) or VCR (video attention). Mid
  funnel: DPVR or CPC (consideration and traffic). Lower funnel: CPA (a conversion) or ROAS (revenue
  efficiency). A goal two stages off the objective wastes budget optimizing the wrong signal.
- DPVR and ROAS are retail-native goals. They lean on the shopping signals Amazon sees directly (detail
  page views, purchases, sales), which an off-Amazon display DSP cannot optimize toward. Use them when
  the objective is retail consideration or retail revenue. See `amazon-dsp-measurement-and-reporting`
  for what those signals mean.
- Reach is for breadth, not response. A reach goal optimizes toward unique users and will not chase
  clicks or conversions; do not set it and then judge it on CPA.

### Bidding and targets

- Targets are guides the system tries to hold on average, not hard ceilings on any single impression. If
  you need an absolute price ceiling, use a bid cap, and accept that it can limit delivery.
- A target set below the clearing price starves delivery, because the algorithm cannot find impressions
  at that price. If the line item underdelivers, loosen the target or widen targeting before assuming the
  goal is wrong, then let it relearn.
- A bid cap that is too low throttles automated bidding and blocks it from winning the high-value
  impressions the goal points at. Remove or raise the cap if delivery or performance suffers.

### Supply and audience optimization

- Supply optimization works within the supply you selected; it reallocates spend, it does not add new
  exchanges or deals. To change which inventory is eligible at all, go to
  `amazon-dsp-inventory-and-supply`.
- Audience optimization works within the audience you selected; it leans into converting segments and
  expands toward similar users. To change the audience definition, go to `amazon-dsp-audiences`.
- Over-stacked targeting defeats optimization. Audience plus contextual plus geo plus device plus
  daypart can shrink addressable supply so far that the algorithm has nothing to optimize across. Keep
  layers to what the goal needs.

### Budget and pacing

- Even pacing by default. It lets the algorithm optimize across the whole flight and spread delivery.
  Use accelerated pacing only for a short flight or to seed optimization fast, then watch for the budget
  exhausting before the flight ends.
- Accelerated pacing fights optimization on a long flight. It front-loads spend before the algorithm has
  learned and can burn budget early. Reserve it for deliberate, short-term use.
- Leave runway before a hard end date so pacing and optimization finish smoothly rather than dumping
  spend at the close.
- Cap to match the flight. A daily cap smooths delivery; a total cap bounds the flight. The order budget
  is the pool the line items spend against, so set both levels coherently (order setup is in
  `amazon-dsp-account-structure`).

### Learning and in-flight management

- Hold the goal, target, and budget stable through the learning window. Editing the goal or moving the
  target mid-learning resets calibration and wastes the window, the same failure mode as on any
  goal-based DSP. Decide up front and hold it.
- Change one variable at a time in flight. If you adjust the target and the audience and the supply at
  once, you cannot tell which move helped, and you reset learning three ways.
- Diagnose before you re-tune. Underdelivery usually traces to a target below clearing price, targeting
  too narrow, a bid cap too low, no eligible creative, or thin conversion signal, not to the goal being
  wrong. Work that list first.

Exact in-console behavior varies over time and by product type, country, and console version, and some
goal availability and pacing options sit on login-gated pages. Several specifics (which goals a given
product type exposes, default and minimum bid behavior, exact pacing presets) are not fully documented
on public pages. Where this skill states a number or a preset it cannot point to publicly, treat it as
standard Amazon DSP practice and confirm the current option in the Amazon DSP console for your market.

## Templates and examples

A lower-funnel conversion line item with healthy retail signal:

```
Objective: drive purchases on Amazon
Optimization goal: ROAS (or CPA if a fixed cost-per-action target matters more than revenue ratio)
Target: grounded in real product margin and observed sales-per-dollar, not an aspirational ROAS
Bidding: system bids toward the goal, no bid cap unless a hard price ceiling is required
Pacing: even | Budget cap: daily cap sized to the flight
Optimization: supply + audience optimization on; let them shift spend toward converting placements
              and segments
Manage: hold stable through learning; if underdelivering, loosen target or widen audience, not the goal
```

An upper-funnel streaming TV awareness line item with no conversion signal:

```
Objective: maximum unique reach with completed views
Optimization goal: reach (breadth) or VCR if completed video views are the success metric
Target: none for reach; VCR has no cost target, the system optimizes toward completions
Bidding: system bids toward the goal
Pacing: even for a long flight; accelerated only if the flight is short
Optimization: audience optimization on within a broad demo + lifestyle audience; keep extra layers
              minimal to protect scale
Why not CPA/ROAS: no conversion signal to learn from at this stage; a conversion goal would starve
```

A mid-funnel traffic line item driving shoppers to the product detail page:

```
Objective: drive qualified Amazon shopping consideration
Optimization goal: DPVR (retail consideration) or CPC (traffic) depending on whether the success
                   signal is the detail page view or the click
Target: a CPC target grounded in the channel's click economics if using CPC
Pacing: even | Optimization: supply + audience optimization on
Why DPVR: it optimizes toward the retail consideration signal Amazon sees directly, which a generic
          click goal does not capture
```

## Common pitfalls

- Goal mismatched to objective. A reach goal judged on CPA, or a CPA goal expected to maximize reach.
  The algorithm optimizes hard toward whatever the goal names, so name the right one.
- A conversion or ROAS goal with no signal. Without a working pixel or enough events, the system cannot
  learn; start higher in the funnel and move down as volume builds.
- Target below the clearing price. The line item starves because the algorithm cannot find impressions
  at that price. Loosen the target or widen targeting, then relearn.
- Bid cap throttling the algorithm. A cap set too low blocks the bids the goal needs. Raise or remove it
  if delivery or performance suffers.
- Re-tuning during learning. Editing the goal or target mid-learning resets calibration. Hold it.
- Changing several variables at once in flight. You cannot attribute the result and you reset learning
  multiple ways. Move one lever at a time.
- Accelerated pacing on a long flight. Front-loads spend before the algorithm has learned and exhausts
  budget early. Use even pacing unless the flight is short.
- Over-stacked targeting. Too many layers shrink addressable supply so far that supply and audience
  optimization have nothing to work across.
- Treating it as sponsored ads. There are no keyword or ASIN bids in the DSP. If the request is about
  bidding on search terms, it is Sponsored Products, Brands, or Display, not Amazon DSP.

## Sources

- [Amazon DSP: Advertise with a demand-side platform](https://advertising.amazon.com/solutions/products/amazon-dsp) (as of June 2026)
- [What is a demand-side platform? A complete guide](https://advertising.amazon.com/library/guides/demand-side-platform) (as of June 2026)
- [amzn/ads-advanced-tools-docs (official Amazon Ads advanced tools documentation)](https://github.com/amzn/ads-advanced-tools-docs) (as of June 2026)

Amazon's public documentation for DSP bidding and optimization is thin, and the in-console help that
spells out exact goal availability, default bid behavior, and pacing presets sits behind login. The
Amazon Ads API reference under advertising.amazon.com/API/docs is a JavaScript single-page app that
returns a page shell for any path and exposes no readable prose, so it is not cited here as proof. Where
this skill states a specific goal behavior, target, or pacing preset that is not on a public page, it
describes standard Amazon DSP practice; confirm the current option in the Amazon DSP console for your
market.
