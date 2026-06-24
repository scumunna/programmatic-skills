---
name: google-ads-conversion-tracking-and-attribution
description: Set up Google Ads conversion tracking and choose the right attribution. Use when the user asks about Google Ads conversion tracking, conversion actions, the Google tag or Tag Manager for conversions, importing GA4 conversions, app or call or offline conversion import, Enhanced Conversions, Consent Mode, primary versus secondary conversion actions, conversion windows, conversion value rules, attribution models, or data-driven attribution. Google Ads conversions are separate from DV360 Floodlight, so do not apply Floodlight rules here.
---

# Google Ads conversion tracking and attribution

Instrument the conversions a campaign optimizes toward, count them once and correctly, and assign credit across the clicks that led to them. This skill covers conversion actions and their sources (website, GA4 import, app, calls, offline), Enhanced Conversions, Consent Mode, primary versus secondary actions, conversion windows, conversion value rules, and attribution models. Getting this layer right matters because Smart Bidding optimizes to exactly the conversions you mark primary, so a counting or attribution mistake propagates straight into bidding.

Google Ads conversion tracking is a separate system from DV360 Floodlight. Do not apply Floodlight activity types, counting methods, or CM360 attribution settings here. For DV360 measurement, use the DV360 measurement and attribution skill. For shared definitions of click-through, view-through, and KPI math, see the `programmatic-foundations` skill. For multi-touch path analysis and how assist credit is read, see the `path-to-conversion-analysis` skill.

## When to use this skill

- "Set up conversion tracking" or "is this conversion counting correctly?"
- "Add the Google tag" or "track conversions with Tag Manager."
- "Import my GA4 conversions" or "bring Analytics key events into Google Ads."
- "Track app installs," "track phone calls," or "import offline conversions."
- "Turn on Enhanced Conversions" or "improve measurement accuracy."
- "Set up Consent Mode" or "handle consent for ad measurement."
- "Primary vs secondary conversions," "which conversions feed bidding."
- "What conversion window should I set?" or "adjust the click and view windows."
- "Which attribution model should I use?" or "is data-driven the default?"
- "Set up conversion value rules" or "adjust value by location or device."

Boundary with sibling skills:

- Choosing a bid strategy that consumes these conversions belongs to `google-ads-bidding`. This skill defines and counts the conversions; that skill bids on them.
- Reading conversion and attribution reports belongs to `reporting-by-campaign-goal`. Reasoning about full conversion paths and assist credit belongs to `path-to-conversion-analysis`.
- Term definitions in the abstract (what view-through means) live in `programmatic-foundations`.

## Quick reference

| Goal | Conversion source | Notes |
| --- | --- | --- |
| Web purchase or sign-up | Website, via Google tag or Tag Manager | The default for online actions |
| Reuse Analytics events | Import from Google Analytics (GA4) | Event must be a key event; account linked, auto-tagging on |
| App install or in-app action | App, via Google Play, Firebase, or third-party | Google Play installs tracked automatically |
| Phone lead | Calls from ads, calls to a website number, or import | Forwarding-number methods need a Google forwarding number |
| Offline sale tied to a click | Offline conversion import, or Enhanced Conversions for leads | Capture GCLID or hashed first-party data at lead time |
| More accurate online measurement | Enhanced Conversions | Hashed (SHA256) first-party data supplements existing tags |
| Respect consent for measurement | Consent Mode (basic or advanced) | Communicates consent state to Google tags |
| Decide what feeds bidding | Primary vs secondary actions | Primary feeds bidding; secondary is observation only |
| Split credit across clicks | Attribution model | Data-driven is the default; only data-driven and last click remain |

Rule of thumb: instrument the action that is the real business outcome, mark only the actions you want to optimize toward as primary, and let everything else report as secondary. Match the conversion source to where the action happens, not to whichever tag is easiest.

## Conversion actions and their sources

A conversion action defines a single valuable event and where it is measured. Conversion tracking works by recording the action after an ad interaction, usually through a Google tag (code snippet) on the site or app, with some sources (phone calls, Google Play installs) tracked without a site tag. Google Ads groups conversion sources into website, app, phone calls, and offline (import).

- **Website conversions.** The main path for online actions like purchases, sign-ups, and form submissions. Deploy the Google tag directly on the site, or manage it through Google Tag Manager. In setup you add the site as a data source, pick the conversion category, and define the action (a page load or a button click), capturing a dynamic value where the action has a transaction value. Use Tag Manager when the site already runs it or you want centralized tag governance; use the Google tag directly for a lighter install.
- **Imported GA4 conversions.** Reuse measurement you already have in Google Analytics 4 rather than instrumenting twice. The Analytics event must be marked as a key event, the Google Ads and Analytics accounts must be linked, and auto-tagging must be on. Imported Analytics conversions arrive in Google Ads up to 24 hours after they occur, and they are created as secondary by default (see primary versus secondary below).
- **App conversions.** Track installs and in-app actions. Google Play handles Android installs, in-app purchases, and pre-registrations automatically once linked. For richer in-app events and for iOS, use Google Analytics for Firebase, which integrates with Apple SKAdNetwork for iOS measurement, or a third-party app analytics provider.
- **Call conversions.** Measure phone leads in several ways: calls placed from call assets or call-only ads, calls to a forwarding number shown on the site after an ad click, clicks on a mobile site phone number, or calls imported from another system. The forwarding-number methods require a Google forwarding number and are available only in certain countries; set a minimum call length so only meaningful calls count.
- **Offline conversion import.** Tie an offline sale back to the ad click that started it. Capture the Google Click ID (GCLID) or hashed first-party data at lead time, then upload the conversion against that identifier when the sale closes. Google now recommends Enhanced Conversions for leads over the legacy GCLID file import, because it is easier to maintain and gives more durable, cross-device measurement.

## Enhanced Conversions

Enhanced Conversions improves measurement accuracy by supplementing your existing conversion tags with hashed first-party customer data (email, name, address, phone) that the user provided. The data is hashed locally with the SHA256 one-way algorithm before it is sent, so Google receives only the hash, which it matches against signed-in Google accounts to recover conversions that the base tag would have missed.

- **Two variants.** Enhanced Conversions for web improves measurement of online conversions. Enhanced Conversions for leads measures offline sales that began as a web lead, and is the recommended successor to legacy offline conversion import.
- **Setup methods.** Configure through the Google tag, through Google Tag Manager, or through the API, depending on how the site is instrumented and how the lead data flows.
- **Why it matters.** More recovered conversions means more signal for Smart Bidding, so Enhanced Conversions is usually worth enabling wherever first-party data is available and consent allows it.

## Consent Mode

Consent Mode communicates a user's consent choices to Google tags so measurement respects them. You set default consent states and update them when the user interacts with a consent banner, controlling consent types such as ad_storage and analytics_storage.

- **Basic Consent Mode** blocks Google tags from loading until the user interacts with the consent banner. When consent is denied, no data, not even consent state, is sent.
- **Advanced Consent Mode** loads Google tags on page open. While consent is denied the tags send cookieless pings, and only after the user grants consent do they send full measurement data. Advanced mode preserves more modeled signal, so prefer it where your consent and privacy requirements allow.
- **Why it matters here.** Consent state feeds conversion modeling. Without Consent Mode in consent-regulated regions, denied-consent conversions are simply lost rather than modeled, which weakens both reporting and bidding.

## Primary versus secondary conversion actions

Every conversion action is either primary or secondary, and the distinction controls bidding, not just reporting.

- **Primary actions** are reported in the "Conversions" column and are used for bidding, as long as the goal they belong to is used for bidding. Mark an action primary only when you want Smart Bidding to optimize toward it.
- **Secondary actions** are for observation only. They report in the "All conversions" column but do not feed bidding. Use secondary for actions you want to watch but not optimize toward, such as a soft micro-conversion.
- **Defaults and exceptions.** Conversions imported from Google Analytics are secondary by default and can be promoted to primary in Google Ads. Note one exception: a conversion added to a custom goal is used for both reporting and bidding by any campaign using that custom goal, even if it is otherwise marked secondary. Be deliberate about custom-goal membership for this reason.

The practical rule: keep the "Conversions" column to the actions you genuinely want to drive spend, because that column is what Smart Bidding chases. Everything else lives in "All conversions" for visibility.

## Conversion windows

A conversion window is the period after an ad interaction during which a conversion is still credited to it. Set it to match the real consideration cycle.

- **Click-through window:** configurable from 1 day up to 30, 60, or 90 days, depending on campaign type and conversion source. A longer window captures slow-converting purchases but credits clicks further back.
- **View-through window:** configurable from 1 to 30 days (1 to 4 weeks). A long view window inflates credit on incidental impressions, so keep it tight unless the buying cycle justifies it.
- **Engaged-view window:** configurable from 1 to 30 days, defaulting to 3 days when not customized, for video engagements.

Match the window to the buying cycle: too long over-credits old or incidental interactions, too short undercounts genuine influence. Click-through and view-through definitions live in `programmatic-foundations`.

## Conversion value rules

Conversion value rules adjust the value recorded for a conversion at auction time, based on conditions, so value-based bidding (Target ROAS, Maximize conversion value) optimizes to the true worth of each conversion without editing tracking code.

- **Conditions.** Use up to two conditions per rule from location, device, and audience (a second condition is optional). This lets you, for example, raise the value of conversions from a high-margin region or a high-value audience.
- **Adjustment.** Add a fixed amount on top of the recorded value, or multiply the value by a factor.
- **Scope.** Value rules apply to Search, Shopping, Display, Hotel, and Performance Max campaigns. They feed Smart Bidding, so they change both reported value and bidding behavior; document them so a value lift is not mistaken for organic performance change.

## Attribution models

Attribution decides how credit for a conversion is split across the ad interactions that preceded it. The model set has narrowed significantly, so confirm before advising.

- **Data-driven attribution is the default.** It distributes credit across interactions based on your account's own conversion data rather than a fixed rule, which is why Google recommends it where volume supports it.
- **Deprecated models.** First click, linear, time decay, and position-based attribution models are no longer supported. Conversion actions that used them were automatically upgraded to data-driven. Do not recommend any of these four; they are not selectable.
- **What remains.** Data-driven and last click are the available models. Last click assigns all credit to the final clicked ad and keyword. Choose last click only when you specifically need that single-touch, transparent rule; otherwise stay on data-driven.
- **Switching.** Some accounts are auto-migrated to data-driven, with administrators emailed about 30 days ahead and an option to opt out or switch earlier. For multi-touch path reading and assist analysis beyond the model itself, use `path-to-conversion-analysis`.

## Decision rules and thresholds

- **Count once, at the source of the real outcome.** Pick the conversion source that matches where the action happens; do not double-instrument a web purchase and its GA4 import as two primary actions.
- **Primary equals what bidding chases.** Mark an action primary only to optimize toward it; everything else is secondary and observation-only.
- **Default to data-driven attribution.** It is the default and recommended model; the older rules-based models (first click, linear, time decay, position-based) are deprecated and unavailable. Use last click only for a deliberate single-touch reason.
- **Set windows to the buying cycle.** Long click windows catch slow conversions; long view windows over-credit incidental impressions. Tune both deliberately.
- **Enable Enhanced Conversions where first-party data and consent allow.** More recovered conversions means more bidding signal.
- **Use Consent Mode in consent-regulated regions.** Without it, denied-consent conversions are lost rather than modeled.

## Templates and examples

**E-commerce web purchase.** Goal is online revenue. Create a website purchase conversion via the Google tag (or Tag Manager if the site runs it), capture the order value as a dynamic value, mark it primary so Smart Bidding optimizes to revenue, keep the click-through window at 30 days for a short consideration cycle, and enable Enhanced Conversions for web to recover matched conversions. Leave newsletter sign-ups as secondary for visibility.

**Lead-gen with offline close.** Goal is qualified leads that close offline weeks later. Track the form submission as a primary website conversion, set up Enhanced Conversions for leads (preferred over legacy GCLID file import) to tie the eventual sale back to the click, and set a longer click window (60 or 90 days) to match the sales cycle. Mark the raw form fill primary only if you want bidding to chase volume; if you want bidding to chase closed deals, make the imported sale the primary action.

**Reusing GA4 measurement.** The advertiser already tracks checkout in GA4. Link the accounts, confirm auto-tagging is on, mark the GA4 checkout event a key event, and import it. Remember it lands as secondary by default, so promote it to primary in Google Ads if it should feed bidding, and expect up to a 24-hour data delay.

**Value-based bidding by geography.** Margins are higher in one region. Keep the purchase conversion primary on Maximize conversion value, then add a conversion value rule that multiplies value for that region's location condition. Document the rule so the resulting value lift is not misread as a market shift.

## Common pitfalls

- Recommending a deprecated attribution model. First click, linear, time decay, and position-based are gone; only data-driven and last click exist.
- Marking too many actions primary, so Smart Bidding chases soft micro-conversions and over-optimizes to low-value events. Keep the "Conversions" column tight.
- Double-counting a web conversion and its GA4 import as two primaries. Pick one source as the primary truth.
- Forgetting that imported GA4 conversions are secondary by default, then wondering why bidding ignores them.
- Setting a long view-through window and inflating credit on incidental impressions.
- Skipping Consent Mode in consent-regulated regions, then losing denied-consent conversions that could have been modeled.
- Treating these as DV360 Floodlight. They are a separate system; Floodlight activity types, counting methods, and CM360 attribution do not apply.

## Sources

- About conversion measurement, Google Ads Help: https://support.google.com/google-ads/answer/1722022 (as of June 2026)
- Different ways to track conversions, Google Ads Help: https://support.google.com/google-ads/answer/1722054 (as of June 2026)
- Set up your web conversions, Google Ads Help: https://support.google.com/google-ads/answer/6095821 (as of June 2026)
- Create conversions from Google Analytics events in Google Ads, Google Ads Help: https://support.google.com/google-ads/answer/2375435 (as of June 2026)
- About mobile app conversion tracking, Google Ads Help: https://support.google.com/google-ads/answer/6100665 (as of June 2026)
- About offline conversion imports, Google Ads Help: https://support.google.com/google-ads/answer/2998031 (as of June 2026)
- About enhanced conversions, Google Ads Help: https://support.google.com/google-ads/answer/9888656 (as of June 2026)
- About consent mode, Google Ads Help: https://support.google.com/google-ads/answer/10000067 (as of June 2026)
- About primary and secondary conversion actions, Google Ads Help: https://support.google.com/google-ads/answer/11461796 (as of June 2026)
- About "All conversions", Google Ads Help: https://support.google.com/google-ads/answer/3419678 (as of June 2026)
- About conversion windows, Google Ads Help: https://support.google.com/google-ads/answer/3123169 (as of June 2026)
- About conversion value rules, Google Ads Help: https://support.google.com/google-ads/answer/10518330 (as of June 2026)
- About attribution models, Google Ads Help: https://support.google.com/google-ads/answer/6259715 (as of June 2026)
