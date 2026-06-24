---
name: google-ads-performance-max
description: Set up, tune, and decide when to run a Google Ads Performance Max campaign. Use when the user asks about Performance Max, PMax, asset groups, audience signals, listing groups, search themes, final URL expansion, brand exclusions or brand safety in PMax, PMax vs Search, "should I use Performance Max", why PMax reporting is limited, or how to feed PMax good signals.
---

# Google Ads Performance Max

Decide whether Performance Max fits the goal, then set it up and feed it the signals it needs to
optimize. Performance Max is one goal-based campaign that serves across every Google channel from a
single campaign, so the leverage is almost entirely in the inputs you give it: the conversion goal,
the asset groups, the audience signals, the listing groups for retail, and the brand-safety
boundary. Google AI controls bidding, budget allocation, placement, and creative assembly. You
control what it optimizes toward and what it has to work with.

Google Ads is Google's self-service auction platform across Search, YouTube, the Display Network,
Discover, Gmail, and Maps. It is a different platform from DV360; do not carry DV360 line-item or
insertion-order concepts into Google Ads. For KPI definitions and goal math (CPA, ROAS, CPM), see
the `programmatic-foundations` skill. For choosing Performance Max against other campaign types, see
`google-ads-campaign-types`. For reading results against the goal the campaign serves, see
`reporting-by-campaign-goal`.

## When to use this skill

- "Should I use Performance Max?" / "Performance Max vs Search?"
- "How do I set up a PMax campaign / asset groups / audience signals?"
- "What are search themes / listing groups / final URL expansion?"
- "How do I keep PMax brand-safe?" / "How do brand exclusions work in PMax?"
- "Why can't I see where PMax spent / which placement converted?" (reporting limits)
- "How do I feed Performance Max better signals?"
- "PMax is eating my Search and brand budget. What do I do?"

Boundaries with sibling skills:
- Which campaign type to run at all (Search, Shopping, Demand Gen, Video, App): `google-ads-campaign-types`.
- Bid strategy mechanics (Target CPA, Target ROAS, Maximize conversions or value, learning period):
  `google-ads-bidding`. PMax uses Smart Bidding, but the strategy details live there.
- Conversion tracking and attribution that PMax depends on to optimize:
  `google-ads-conversion-tracking-and-attribution`.
- Budget setting and pacing across campaigns: `google-ads-budgets-and-pacing`.
- Audience list building and targeting concepts reused as signals:
  `google-ads-audiences-and-targeting`.

## Quick reference

What you supply versus what Google controls:

| You control | Google AI controls |
| --- | --- |
| Conversion goal and conversion values | Bid per auction (Smart Bidding) |
| Budget and bid strategy targets | Budget split across channels |
| Asset groups (text, image, video, logos) | Which channel and placement serves |
| Audience signals (per asset group) | Final creative assembly and combination |
| Listing groups (retail, from the feed) | Which products and placements to push |
| Search themes | Query and keyword-less matching |
| Brand exclusions and brand safety settings | Final URL chosen when expansion is on |

Performance Max vs Search, the decision in one table:

| Situation | Run | Why |
| --- | --- | --- |
| You want explicit keyword and query control | Search | PMax does not expose keyword-level bidding or full query control |
| You want one conversion campaign across all Google inventory | Performance Max | One campaign optimizes Search, YouTube, Display, Discover, Gmail, Maps |
| Retail catalog, want maximum reach and automation | Performance Max with a feed | Listing groups extend the catalog across every channel |
| Lead gen with a clean conversion goal and good signals | Performance Max, alongside Search | PMax finds incremental converters Search keywords miss |
| No working conversion tracking | Neither yet | PMax has nothing to optimize toward; set up tracking first |
| You need channel-level control and reporting | Search plus per-channel campaigns | PMax reporting is rolled up, not placement-level |

Run Performance Max alongside Search, not instead of it. PMax complements keyword-based Search;
brand and high-intent Search terms still deserve a dedicated Search campaign with brand exclusions
on PMax so the two do not cannibalize.

## Core process

1. Confirm the prerequisites before building. PMax is goal-based, so it needs working conversion
   tracking and, for retail, a linked Merchant Center feed. Without tracking it cannot optimize;
   without a feed it cannot run listing groups. If either is missing, set it up first (hand off to
   `google-ads-conversion-tracking-and-attribution`).
2. Set one clear conversion goal and its values. PMax optimizes toward the conversion goal and, for
   value-based bidding, the conversion values you report. A muddy goal (many weakly related
   conversion actions) produces muddy optimization. Pick the primary action and value it correctly.
3. Choose the bid strategy for the goal. Maximize conversions or Maximize conversion value, with an
   optional Target CPA or Target ROAS once you have history. The strategy, conversion-data needs,
   and learning period live in `google-ads-bidding`. Avoid an overly tight target at launch; it
   starves delivery before the campaign learns.
4. Build asset groups around themes or audiences. Each asset group is a collection of creatives
   (headlines, descriptions, images, logos, videos) centered on a theme or a target audience.
   Provide a full, diverse set so Ad Strength is strong and Google can assemble ads for every
   channel. Separate asset groups by product line, theme, or audience, not arbitrarily.
5. Add audience signals to each asset group. Audience signals (first-party data, Customer Match,
   custom segments, demographics, interests) tell Google AI who is likely to convert so it ramps
   faster. Signals are suggestions, not hard targeting: PMax can and will serve outside them when
   conversion likelihood is high. Use your strongest first-party and converter data as the signal.
6. For retail, structure listing groups from the feed. Listing groups organize the products by
   their Merchant Center attributes so you control which products PMax pushes. Subdivide only as far
   as you can meaningfully manage.
7. Add search themes where you have query knowledge. Search themes are optional inputs that tell
   Google what your customers search for, which helps coverage on Search inventory inside PMax and
   speeds ramp. They guide, they do not pin, matching.
8. Set the brand-safety boundary. Decide final URL expansion, brand exclusions, and content
   suitability before launch (see Brand safety below), so PMax does not serve where you do not want
   it or send traffic to the wrong pages.
9. Launch and hold through the learning period. Avoid frequent changes to budget, bid strategy, or
   goal during ramp; edits reset learning. Give it time before judging (see `google-ads-bidding`
   for the learning window). Read results with the goal in mind (hand off to
   `reporting-by-campaign-goal`).

## Decision rules and thresholds

- Run PMax only with conversion tracking live. It is a goal-based type; with nothing to optimize
  toward it spends without direction.
- Run PMax alongside Search, not as a replacement. Keep brand and core high-intent terms in a
  dedicated Search campaign and apply brand exclusions to PMax so it does not absorb branded
  conversions and take the credit.
- Feed first-party and converter data as audience signals. The strongest signal is your own
  customer and past-converter data; generic interest segments ramp slower.
- Keep the conversion goal tight. One primary conversion action, valued correctly, optimizes far
  better than a bundle of loosely related actions.
- Do not over-segment asset groups or listing groups. More groups means thinner data per group and
  slower learning. Split by real theme, product line, or audience, then stop.
- Leave final URL expansion on only if your whole site is a valid destination. If parts of the site
  should not receive traffic, turn it off or add URL exclusions, because expansion can route users
  to pages you did not intend.
- Set brand exclusions when brand defense matters. They stop PMax serving on queries for brands you
  want to avoid, across Search and Shopping inventory in PMax.
- Hold changes during the learning period. Budget, goal, and bid-strategy edits reset calibration;
  decide up front and let it stabilize.

## Brand safety, brand exclusions, and final URL expansion

- Brand settings for Search and PMax let you control branded queries. Brand exclusions stop the
  campaign serving on queries associated with brands you want to avoid; for PMax they apply to
  Search and Shopping inventory. Brand inclusions (Search only) restrict serving to brands you
  select. Use exclusions to keep PMax off competitor or sensitive brand terms and to stop it
  poaching your own brand traffic from a dedicated Search campaign.
- Apply brand exclusions from a brand list at the account level and attach the list to the PMax (or
  Search) campaign; you can bulk-apply across campaigns. For PMax there is an option to still allow
  Shopping ads on searches that mention excluded brands, so decide whether brand defense or Shopping
  coverage wins for your catalog.
- Final URL expansion is on by default in PMax. It can replace your final URL with a more relevant
  landing page from your domain and generate a matching headline. Keep it on when any page on your
  site is a fair destination and you want maximum reach; turn it off or add URL exclusions when
  specific pages must not receive paid traffic. It is not supported for store-goal-only campaigns.
- For account-level content suitability (placement and content exclusions that apply beyond one
  campaign), set those alongside the campaign; brand exclusions handle branded queries, content
  suitability handles where ads appear.

## Reporting limitations

Performance Max reporting is rolled up by design, so set expectations before launch.

- Reporting is largely at the campaign and asset-group level, not a full placement-by-placement or
  channel-by-channel performance breakdown like single-channel campaigns give you. You see asset
  performance ratings and campaign results, but not the granular channel attribution a Search or
  Display campaign exposes.
- You cannot bid or report at the keyword level inside PMax. Search themes and final URL expansion
  drive matching, but there is no keyword-level performance table to optimize against.
- Because PMax serves across channels and uses keyword-less matching, judge it on the conversion
  goal and incremental conversions, not on channel-level CPMs or placement lists. Hand off to
  `reporting-by-campaign-goal` for how to read it against the objective, and keep a dedicated Search
  campaign when you need query-level visibility.

## Templates and examples

- Lead-gen advertiser, Search already running: keep brand and core terms in a Search campaign with
  brand exclusions on PMax. New PMax with one lead conversion goal, Maximize conversions (add a
  Target CPA after ~30 conversions, see `google-ads-bidding`), one asset group per service line,
  Customer Match and past-converter lists as audience signals, search themes for the top service
  queries. Hold for the learning window before reading.
- Retailer with a Merchant Center feed: PMax with the feed, Maximize conversion value with Target
  ROAS once value history exists, listing groups split by top product categories, asset groups per
  category with category-specific creative and audience signals, final URL expansion on with
  product and category pages as valid destinations.
- Brand-protective advertiser: PMax for prospecting, brand exclusions applied from an account brand
  list (competitor and own-brand terms), final URL expansion off with a curated set of campaign
  landing pages, content suitability set at the account level.

## Common pitfalls

- Launching PMax without conversion tracking. It optimizes toward nothing and burns budget. Set up
  tracking first (`google-ads-conversion-tracking-and-attribution`).
- Letting PMax cannibalize brand and Search. Without brand exclusions PMax serves on branded queries
  and claims conversions a dedicated Search campaign would have captured, distorting both. Apply
  brand exclusions and keep Search separate.
- Weak or thin asset groups. Too few assets means low Ad Strength and fewer channels Google can
  assemble ads for. Provide a full, diverse set per group.
- Treating audience signals as targeting. They guide ramp; PMax still serves outside them. Use them
  to point the algorithm at likely converters, not to fence it in.
- A muddy conversion goal. Many loosely related conversion actions dilute optimization. Pick the
  primary action and value it.
- Leaving final URL expansion on with pages that should not get traffic. It can route users to
  unintended landing pages. Turn it off or add URL exclusions.
- Changing budget, goal, or bid strategy during learning. It resets calibration and wastes the
  window. Decide up front and hold.
- Expecting placement-level reporting. PMax reporting is rolled up; judge it on the conversion goal,
  not on channel CPMs (see `reporting-by-campaign-goal`).

## Sources

- [About Performance Max campaigns](https://support.google.com/google-ads/answer/10724817) (as of June 2026)
- [Create a Performance Max campaign](https://support.google.com/google-ads/answer/10724896) (as of June 2026)
- [How asset groups work](https://support.google.com/google-ads/answer/10724748) (as of June 2026)
- [About audience signals for Performance Max campaigns](https://support.google.com/google-ads/answer/14530785) (as of June 2026)
- [Guide to getting started with Performance Max (for new users)](https://support.google.com/google-ads/answer/14951594) (as of June 2026)
- [About Final URL expansion in Performance Max](https://support.google.com/google-ads/answer/14337539) (as of June 2026)
- [About brand settings for Search and Performance Max](https://support.google.com/google-ads/answer/13721847) (as of June 2026)
- [Apply brand exclusions to Performance Max or Search campaigns](https://support.google.com/google-ads/answer/14505308) (as of June 2026)
- [Optimization tips for Performance Max campaign for all business types](https://support.google.com/google-ads/answer/11385582) (as of June 2026)
