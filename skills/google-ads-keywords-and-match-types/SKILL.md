---
name: google-ads-keywords-and-match-types
description: Build and govern the keyword layer of a Google Ads Search account. Use when the user asks about keyword match types, broad vs phrase vs exact, how broad match pairs with Smart Bidding, negative keywords and negative match types, the search terms report, Keyword Planner research, brand vs non-brand structure, keyword themes for Smart campaigns, or search themes in Performance Max. This is Google Ads Search, not DV360.
---

# Google Ads keywords and match types

Choose match types, manage negatives, and mine the search terms report so a Google Ads Search
account spends on the queries that convert and starves the ones that do not. This skill is the
keyword brain for Search. Google Ads is a different platform from Display & Video 360; do not
carry DV360 line-item targeting logic over here. For KPI and funnel math (CPC, CPA, ROAS,
quality of a click), see `programmatic-foundations`. For how keywords sit inside campaign and
ad-group structure, see `google-ads-account-structure`. For the bid strategy that match types
depend on, see `google-ads-bidding`.

## When to use this skill

Use this when the task is about WHICH queries a Search ad is eligible for and how you control
that, including:

- Picking broad, phrase, or exact match for a keyword, and when to mix them.
- Pairing broad match with Smart Bidding so the model, not the match type, controls reach.
- Adding negative keywords and choosing the negative match type (broad, phrase, exact).
- Reading the search terms report to harvest new keywords and add negatives.
- Researching volume, competition, and forecasts in Keyword Planner.
- Splitting brand from non-brand so each gets its own budget, bids, and read.
- Keyword themes in Smart campaigns and search themes in Performance Max.

Boundaries with sibling skills:
- Audience layering (your data, in-market, affinity, custom segments, targeting vs observation)
  lives in `google-ads-audiences-and-targeting`. This skill is keywords; that skill is people.
- Bid strategy choice (Target CPA, Target ROAS, Maximize conversions) lives in
  `google-ads-bidding`. Match type and bid strategy are decided together but documented there.
- Performance Max as a campaign type (asset groups, channels, when to run it) lives in
  `google-ads-performance-max`. This skill only covers the search-themes input to it.
- Reporting structure and goal-specific report recipes live in `google-ads-reporting` and
  `reporting-by-campaign-goal`. This skill tells you what to pull from the search terms report;
  those tell you how to build the recurring report.

## Quick reference

Match types as they work now. All three match on meaning and intent, not just literal text,
and all three serve close variants (misspellings, singular/plural, stemming, paraphrase):

| Match type | Syntax | Eligible queries | Reach for it when |
| --- | --- | --- | --- |
| Broad | `running shoes` | Anything related to the meaning, including the landing page and other keywords in the ad group as context | You run Smart Bidding and want the model to find converting queries you would never list |
| Phrase | `"running shoes"` | Queries that include the meaning of the keyword | You want meaning coverage but a tighter gate than broad, often mid-funnel |
| Exact | `[running shoes]` | Queries with the same meaning or intent as the keyword | You want the tightest control, usually high-intent or brand terms |

Negative keywords block queries. They have their own match types and do NOT match close
variants, so you must list the variants you want blocked:

| Negative match type | Syntax | Blocks |
| --- | --- | --- |
| Negative broad | `free` | Queries containing all the words in any order (does not block close variants) |
| Negative phrase | `"free shoes"` | Queries containing the exact phrase in order |
| Negative exact | `[free shoes]` | Only the exact query, that term and nothing more |

One-line rule: positive match types reach by meaning and expand to close variants; negative match
types are literal and do not expand, so block the specific variants you do not want.

## Core process

1. **Set structure before keywords.** Decide brand vs non-brand first, then theme ad groups
   tightly so one ad group maps to one intent. Loose ad groups make match-type behavior and
   the search terms report unreadable. See `google-ads-account-structure` for the structure.
2. **Research in Keyword Planner.** Discover new keywords from a seed term or your site, read the
   monthly search volume and competition, and pull the forecast (impressions, clicks, cost,
   conversions at a given bid) before you commit budget. Use it to size the opportunity, not to
   finalize bids.
3. **Choose the match type from your bidding posture, not by habit.** If you run Smart Bidding,
   lead with broad match and let the model gate reach by predicted value. If you are on manual or
   portfolio bidding without enough conversion data, lead with phrase and exact so you keep
   control while the account learns.
4. **Pair broad match with Smart Bidding deliberately.** Broad match is built to work with Smart
   Bidding: the model reads each query, the landing page, and the other keywords in the ad group
   as context, then bids per auction. Broad match without Smart Bidding hands reach to the match
   type with no value control and burns budget. Treat "broad + Smart Bidding" as one decision.
5. **Seed negatives at launch, then mine continuously.** Add an obvious negative list up front
   (competitors you will not bid on, "free", "jobs", "diy" when irrelevant). After launch, the
   search terms report is the engine: it is where negatives come from.
6. **Work the search terms report on a cadence.** Pull it weekly early in a campaign, then at a
   steady interval. For each surfaced query: if it converts and is not already a keyword, add it
   as a keyword in the right ad group; if it is irrelevant or wastes spend, add it as a negative
   at the right level and match type. This is the single highest-leverage keyword task.
7. **Keep brand and non-brand separate end to end.** Separate campaigns or ad groups, separate
   budgets, separate bid targets, and a brand negative on non-brand campaigns so non-brand does
   not absorb cheap branded clicks and flatter its own CPA. Report them apart.

## Decision rules and thresholds

- **Broad belongs with Smart Bidding; otherwise tighten.** The documented guidance is to use
  Smart Bidding with broad match because each query differs and needs a per-auction bid, and the
  wide query set is what lets the model learn. No Smart Bidding means lead with phrase and exact.
- **Do not stack all three match types for the same term in the same ad group by default.** With
  modern matching and Smart Bidding, overlapping duplicates mostly add management overhead, not
  control. Prefer broad under Smart Bidding, and reserve exact for terms where you want a hard
  intent gate or a separate bid.
- **Negatives are literal: list the variants.** Because negative keywords do not match close
  variants, a single negative will not catch misspellings or plurals. Add the variants, and
  prefer negative phrase or exact when a negative broad would over-block (negative broad ignores
  word order and can block wanted queries that happen to contain those words).
- **Place each negative at the right level.** Campaign-level (or a shared negative list) for
  account-wide junk and for brand exclusion on non-brand campaigns; ad-group-level to steer a
  query toward the better-matched ad group rather than killing it outright. Account-level negative
  lists exist for terms you never want anywhere.
- **Use search terms insights and the search terms report for different jobs.** The search terms
  report is the line-item view for harvesting keywords and negatives; it handles low-volume and
  conversion attribution differently from the aggregated insights view. Drive keyword and negative
  actions from the report.
- **Keyword themes and search themes are guidance, not exact-match keywords.** In Smart campaigns,
  a keyword theme stands in for many similar searches (keep to a small set; too many themes widen
  to less relevant queries). In Performance Max, search themes tell the system queries you expect
  to perform; they act at the same priority as phrase and broad match in Search, up to 50 per
  asset group, and existing negatives and exclusions still apply. Hand off Performance Max setup
  to `google-ads-performance-max`.

## Reference material

- See `programmatic-foundations` for CPC, CPA, ROAS, conversion-rate, and quality definitions.
  This skill does not redefine them.
- See `google-ads-account-structure` for how brand/non-brand campaigns and tightly themed ad
  groups are built; the keyword layer assumes that structure exists.
- See `google-ads-bidding` for choosing the Smart Bidding strategy that broad match depends on.
- See `google-ads-performance-max` for asset groups and when Performance Max is the right vehicle;
  this skill only covers the search-themes input.

## Templates and examples

Non-brand Search ad group, "trail running shoes" retailer on Smart Bidding:

- Match types: broad keywords (`trail running shoes`, `trail runners`, `off road running shoes`)
  under a Target ROAS strategy, so the model gates reach by predicted value.
- Negatives (campaign list): `free`, `repair`, `how to clean`, `[running shoes]` is NOT a negative
  here, but the brand term is added as a campaign negative so brand traffic stays in the brand
  campaign.
- Search terms cadence: pull weekly for the first month. Promote converting queries like
  "waterproof trail running shoes" to a keyword; add "barefoot" and "minimalist" as negatives if
  the catalog does not carry them.
- Brand split: a separate brand campaign holds `[brandname]` and `"brandname trail shoes"` on a
  tighter target, reported separately so non-brand CPA is honest.

Brand-defense Search campaign:

- Match types: exact and phrase on the brand name and obvious brand+category combinations, for
  control and a clean read.
- Negatives: none that would block legitimate brand queries; competitor terms are handled in a
  separate, clearly labeled campaign if the account chooses to bid on them at all.
- Why separate: brand clicks are cheap and high-converting; leaving them in non-brand inflates
  non-brand performance and hides where demand actually comes from.

## Common pitfalls

- **Broad match without Smart Bidding.** The most expensive mistake here. Broad match assumes a
  value-based model is gating each auction; without it you pay for loosely related queries at a
  flat bid. Either turn on Smart Bidding or tighten to phrase and exact.
- **Expecting negatives to catch variants.** Negative keywords are literal and do not expand to
  close variants. One negative does not block its misspellings or plurals; enumerate them.
- **Over-broad negative broad.** A negative broad ignores word order and blocks any query
  containing those words, which can silently suppress wanted traffic. Use negative phrase or exact
  when precision matters.
- **Ignoring the search terms report.** An account that never mines it drifts: good queries never
  become keywords and wasteful queries keep spending. Put it on a calendar.
- **Letting brand bleed into non-brand.** Without a brand negative on non-brand campaigns, cheap
  branded clicks land in non-brand and make its CPA and ROAS look better than the prospecting work
  actually is. Separate and exclude.
- **Treating search themes as keywords.** Search themes guide Performance Max; they are not a
  keyword list and do not give you query-level bidding. Set realistic expectations and lean on the
  asset feed and audience signal too (see `google-ads-performance-max`).

## Sources

Official Google Ads Help, all pages opened and verified as of June 2026.

- About keyword matching options (broad, phrase, exact; broad match with Smart Bidding): https://support.google.com/google-ads/answer/7478529
- About negative keywords (negative broad, phrase, exact; no close-variant matching): https://support.google.com/google-ads/answer/2453972
- About the search terms report: https://support.google.com/google-ads/answer/2472708
- Use Keyword Planner (discover keywords, volume, forecasts): https://support.google.com/google-ads/answer/7337243
- About keyword themes in Smart campaigns: https://support.google.com/google-ads/answer/9263830
- Use search themes with your Performance Max campaign (up to 50 per asset group; priority like phrase and broad match): https://support.google.com/google-ads/answer/14767319
