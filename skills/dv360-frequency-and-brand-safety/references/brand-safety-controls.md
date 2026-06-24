# Brand safety and suitability controls (DV360)

Deep reference for configuring exclusions and auditing an advertiser's brand controls. Read the SKILL.md first for the decision rules; this file is the field-level detail.

## Table of contents

- Where brand controls live
- Digital content labels
- Sensitive categories
- Content theme exclusions
- Inventory source and exclusion-list controls
- Keyword and category exclusions
- Advertiser vs line-item control matrix

## Where brand controls live

Set advertiser-wide brand safety and suitability under the advertiser's brand controls (navigate to the advertiser, then its resources, then brand controls). Settings made there apply to all current and future campaigns, insertion orders, and line items under that advertiser and cannot be loosened at a lower level. Line items can add further restrictions on top.

This is the core leverage rule: the advertiser level is the floor, the line item is the tightening dial. Audit the advertiser level first when a campaign is running on inventory it should not, because a missing floor affects every line item at once.

## Digital content labels

Digital content labels classify domains and apps by suggested audience maturity so you can exclude inventory above the brand's tolerance. The tiers:

- DL-G: general audiences
- DL-Y: families
- DL-PG: most audiences, parental guidance
- DL-T: teen and older
- DL-MA: mature audiences only
- Not yet labeled: unclassified (new sites, masked or semi-transparent URLs, or unsupported languages)

Google reclassifies on a recurring (roughly monthly) basis from many signals about a site's construction, content, quality, and experience. Excluding DL-MA is the common floor. Excluding unlabeled inventory as well removes risk but can sharply reduce scale, because a large share of new or semi-transparent inventory is unlabeled. Decide unlabeled treatment explicitly rather than by accident.

## Sensitive categories

Sensitive categories let you exclude content that complies with policy but may not suit the brand. Available for display, video, and audio line items. The category set includes (non-exhaustive, and Google revises it over time):

- Sexual, Suggestive, Derogatory
- Profanity, Shocking
- Violence, Tragedy, Transportation accidents
- Weapons, Sensitive social issues
- Gambling, Alcohol, Tobacco, Drugs
- Politics, Religion
- Downloads and sharing

Exclude the categories the brand rejects. Some subcategories cannot be excluded independently. Over-excluding compounds with content-label exclusions to cut reach, so exclude what the brand truly cannot run beside, not every category by reflex.

## Content theme exclusions

Brand suitability adds theme-based exclusions (for example politics, religion, news, gaming, health) and content-type exclusions (for example embedded or live-stream video). Suitability tiers (a maximum, moderate, limited style of escalating strictness) bundle controls for profanity, sexual content, violence, drugs, and similar, graded by context and severity. Use suitability to match inventory to one brand's tone, distinct from the universal safety floor.

YouTube has its own handling: some sponsorship inventory bypasses most advertiser-level exclusions to meet share-of-voice objectives, and some label or category controls have restricted availability on YouTube at advertiser and line-item levels. Verify YouTube behavior separately when a buy includes it.

## Inventory source and exclusion-list controls

- **Inventory source targeting.** An inventory source is an exchange or a private deal supplying buyable impressions. With no inventory source targeting set, a line item targets open auction inventory on all enabled exchanges by default. Target only the sources you want, or exclude specific sources, to drop whole exchanges or sub-exchanges.
- **Channel, URL, and app exclusion lists.** Build reusable lists of sites or apps to exclude and apply them across line items. Negative app/URL targeting drops specific placements the brand will not run on.
- DV360 also integrates third-party data sources for fraud and quality filtering across URL, app, domain, and subdomain levels. Treat these as supplements to native exclusions, not replacements.

## Keyword and category exclusions

- **Negative keyword targeting** can be set at advertiser, campaign, insertion order, or line item level. Advertiser-level exclusions apply a blanket block to all campaigns. Save reusable negative keyword lists (limited per advertiser) and apply them. A line item can target up to a combined 25,000 negative keywords from individual entries and lists.
- **Category targeting** is primarily an inclusion tool (target market verticals and page content); selecting a parent category targets its subcategories. For exclusion of unsuitable content, prefer sensitive categories and content theme exclusions, which are built for exclusion.

## Advertiser vs line-item control matrix

| Control | Advertiser (floor) | Line item (tighten only) |
| --- | --- | --- |
| Digital content labels | Yes, applies account-wide | Yes, can exclude more |
| Sensitive categories | Yes | Yes, can exclude more |
| Content theme / suitability tier | Yes | Yes, can restrict more |
| Inventory source exclusion | Via shared targeting | Yes |
| Channel/URL/app exclusion lists | Yes (shared lists) | Yes |
| Negative keywords | Yes (blanket) | Yes (adds, up to the 25,000 combined cap) |
| Third-party pre-bid avoidance segment | Via IO default targeting | Yes |

Rule of thumb: put what the brand requires everywhere at the advertiser level so it cannot be dropped, and use line items only to go stricter for a specific buy.

## Sources

- Brand suitability: https://support.google.com/displayvideo/answer/3032915 (as of June 2026)
- Digital content labels in Display & Video 360: https://support.google.com/displayvideo/answer/2735881 (as of June 2026)
- Sensitive categories in Display & Video 360 brand safety targeting: https://support.google.com/displayvideo/answer/6327207 (as of June 2026)
- Inventory source targeting: https://support.google.com/displayvideo/answer/2726009 (as of June 2026)
- Keyword targeting: https://support.google.com/displayvideo/answer/2697825 (as of June 2026)
