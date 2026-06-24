---
name: tag-and-pixel-governance
description: Place, validate, govern, and retire conversion tags and pixels so measurement is trustworthy and bidding optimizes on real signal. Use when the user asks about Floodlight setup, placing a conversion pixel, a conversion tag not firing, verifying a conversion end to end, the Google tag or Tag Manager deployment, Consent Mode on the DV360 side, cross-domain or iframe firing, tag deduplication, a pixel inventory, or retiring a stale pixel. This is the shared tagging hygiene layer across measurement and ops.
---

# Tag and pixel governance

Own the lifecycle of every conversion tag and pixel: place it correctly, prove it fires, confirm it counts once, confirm it feeds bidding, and retire it when it goes stale. A tag that silently stops firing, double counts, or ignores consent corrupts reporting and trains bid strategies on noise, and the damage compounds for the length of the flight before anyone notices.

This skill is the tagging hygiene layer shared across measurement and operations. For what a conversion means and which attribution model or counting method to choose, see the `dv360-measurement-and-attribution` skill. For the full pre-launch sign-off that gates go-live, see the `dv360-launch-qa` skill. For consent law, regional policy, and the privacy posture this implements, see the `privacy-and-consent` skill. Where a Google Ads conversion tag is in scope rather than a DV360 Floodlight tag, see the `google-ads-conversion-tracking-and-attribution` skill, which owns Consent Mode in detail for that surface.

## When to use this skill

- "Set up Floodlight" or "place a conversion pixel" or "add a conversion tag."
- "The conversion tag is not firing" or "conversions stopped recording."
- "Verify a conversion" or "prove this tag works end to end before launch."
- "Deploy the Google tag" or "do this through Tag Manager."
- "Handle Consent Mode for DV360" or "are we passing consent on the buy side?"
- "Validate cross-domain firing" or "the tag is inside an iframe, does it still fire?"
- "Are we double counting?" or "deduplicate these tags."
- "Build a pixel inventory" or "audit what tags are on the site" or "retire this stale pixel."

Boundary: this skill is the mechanics and governance of the tag itself. The choice of activity type, counting method, attribution model, and lookback window is `dv360-measurement-and-attribution`. The go or no-go launch decision is `dv360-launch-qa`. Consent law and regional policy are `privacy-and-consent`. Floodlight activities are defined in Campaign Manager 360 and shared to DV360 and Search Ads 360, so configuration steps that live in CM360 are flagged as such.

## Quick reference

| Situation | Do this | Why |
| --- | --- | --- |
| New conversion to track | Define the activity in CM360, place the Google tag on the page, fire a test, verify in report, confirm it feeds bidding | A tag is not done until a real conversion is visible and counted once |
| Site already runs Tag Manager | Deploy the tag through Tag Manager, not a second hardcoded snippet | One governed deployment path avoids duplicate fires and orphan tags |
| Lighter install, no tag manager | Place the Google tag directly on the page | Fewer moving parts when there is no third-party tag estate |
| EEA, UK, or Switzerland traffic | Confirm consent signals reach the buy side and Consent Mode is set on the Google tag | Without it, denied-consent conversions are lost, not modeled |
| Conversion spans two domains | Validate the tag fires on the destination domain and the path crosses domains cleanly | A cross-domain gap drops the conversion or breaks attribution |
| Tag lives inside an iframe | Confirm it fires from the framed context and is not blocked | Framed and third-party contexts silently suppress tags |
| Two tags for one event | Pick one source of truth, dedupe the rest | Two tags on one event double counts and inflates the optimizer's signal |
| Tag of unknown purpose on a page | Trace it in the inventory, find the owner, retire if orphaned | Untracked tags leak data, slow the page, and corrupt counts |

Rule of thumb: a tag is not "set up" when the snippet is on the page. It is set up when a test conversion has fired, appeared in the report under the right activity, shown in the attribution column you expect, and is confirmed to feed (or deliberately not feed) the bid strategy. Stop short of any of those and you have an unverified tag, which is worse than no tag because it looks done.

## Core process: place and validate a conversion tag

Run this as an ordered gate. Each step must pass before the next, because a failure upstream makes every downstream check meaningless.

1. **Define the activity at the source.** Create the Floodlight activity in Campaign Manager 360 (counter for non-monetary actions, sales for revenue), choosing the counting method and any custom variables there so one definition feeds DV360 and SA360. The activity choice itself is `dv360-measurement-and-attribution`; here you are getting a tag to deploy.
2. **Place the tag on the correct page.** Put the tag on the exact page that represents the action (the order-confirmation page for a purchase, the thank-you page for a lead), not a generic page that fires on every visit. Prefer the Google tag format. Use an iframe or image tag only when the Google tag is not viable, and validate the framed case explicitly (see cross-domain and iframe validation below). Editing the activity does not update the tag already on the site, so a redeployment is required after any change.
3. **Fire a test conversion.** Complete the real action end to end (a test purchase, a test form submission) so the tag fires in production conditions, not just a synthetic call. Validate the tag is present and firing with a tag inspector or the network panel, confirming the request to the measurement endpoint returns successfully and carries the expected activity identifier and any custom variables.
4. **Verify it in the report.** Pull a conversions report and confirm the test conversion appears under the correct activity, at the expected count, with the value populated for a sales activity. A tag that fires in the browser but never lands in the report points to a configuration or identity mismatch, not a placement problem. Allow for reporting latency before declaring a miss.
5. **Confirm the attribution column.** Confirm the conversion shows in the column you expect: post-click versus post-view, and Conversions (the selected, bidding-eligible set) versus All Conversions (the raw count). A conversion in All Conversions but not Conversions means it is recorded but not selected to feed bidding, which is a silent optimization gap.
6. **Confirm it feeds bidding.** If a bid strategy optimizes to this conversion, confirm the activity is in the selected set the strategy consumes. A strategy chasing a conversion that is recorded but not selected learns nothing from it, and a strategy chasing a test or junk activity optimizes toward garbage. Be deliberate about which activities are in the bidding set.
7. **Record it in the inventory.** Add the tag to the pixel inventory (page, owner, purpose, activity, deployment path, date) the moment it is live, not later. An untracked tag is a future orphan.

A tag that clears all seven steps is verified. Document the verification (a screenshot of the test conversion in the report under the right column is enough) so the launch QA sign-off can rely on it rather than re-proving it.

## The Google tag and Tag Manager deployment path

The Google tag (gtag.js) is a single tag that sends data to linked Google destinations, and it is configurable from DV360, CM360, Google Ads, Analytics, and Tag Manager. Choose the deployment path by the site's existing tag estate, not by habit.

- **Direct Google tag.** Place gtag.js on the page when the site has no tag manager and needs a lighter install with default measurement. Fewer moving parts, but every change is a code change.
- **Through Tag Manager.** Deploy the Google tag through Google Tag Manager when the site already runs it, when you manage third-party tags alongside Google tags, or when you want version control, a non-code change path, and centralized governance. This is the better default for any non-trivial tag estate because it gives one place to see and control what fires.
- **One deployment, one source of truth.** Do not hardcode a snippet and also fire the same tag through Tag Manager. Two deployment paths for one tag is the most common cause of double counting. Pick one path per tag and record it in the inventory.
- **Set destinations once.** If the same Google tag serves multiple Google products, configure it in one place and add the others as destinations rather than installing a second tag. Duplicate base tags fragment data and multiply maintenance.

## Consent Mode on the DV360 side

Consent Mode communicates a user's consent choices to Google tags so measurement and bidding respect them. The `google-ads-conversion-tracking-and-attribution` skill owns the full Consent Mode mechanics (basic versus advanced, the ad_storage and analytics_storage signals, cookieless pings, conversion modeling); the same model applies to the Google tags that carry DV360 measurement, so mirror it here rather than restating it. On the DV360 buy side, the consent picture has two layers that are easy to conflate:

- **Tag-level consent (Consent Mode).** Where the Google tag carries DV360 conversion measurement, set Consent Mode so the tag adjusts behavior to the user's consent state. Prefer advanced mode where your privacy posture allows, because it preserves modeled signal: denied-consent conversions are modeled rather than simply lost, which protects both reporting and the bid strategy. Basic mode blocks the tag until the banner is answered and forfeits that modeling.
- **Serving-side consent (EU user consent policy and GDPR).** Independently of the conversion tag, DV360 restricts its use of user data on GDPR traffic (the EEA, the UK, and Switzerland). Without valid consent signals (TCF consent for storage, personalized-ads profile creation, and personalized-ads selection), DV360 falls back to limited or non-personalized ads. So a conversion can be consent-gated at the tag and the impression consent-gated at serving, and both must be handled. The law, the regional scope, and the policy posture are `privacy-and-consent`; this skill ensures the tag and serving consent signals are actually present and correct.

Validate consent end to end, not in the abstract: in a consent-regulated region, confirm the consent banner updates the tag's consent state (denied before interaction, granted after) and confirm the serving side is receiving consent signals so personalized inventory is eligible when consent is present. A site that shows a banner but never passes the resulting state to the tags is the silent failure mode.

## Cross-domain and iframe firing validation

A tag that fires on the page you tested can still fail in the contexts that matter. Validate the hard cases explicitly:

- **Cross-domain conversions.** When the click and the conversion live on different domains (an ad on one domain, a checkout on a separate payment or booking domain), confirm the tag fires on the destination domain where the action completes and that the path links the two domains so the conversion attributes back to the click. A cross-domain gap either drops the conversion or strands it as unattributed. Test the full real journey across the domain boundary, not each domain in isolation.
- **Iframe and framed contexts.** A tag rendered inside an iframe (a framed checkout, a third-party booking widget, an embedded form) fires from a different context than the top page and can be blocked or scoped to the frame. Confirm the tag is present in the framed document, fires when the action completes inside the frame, and is not suppressed by frame sandboxing or third-party storage limits. Where the Google tag cannot fire in the frame, the iframe Floodlight tag format exists for exactly this case, but it still must be validated firing.
- **Third-party and storage-restricted contexts.** Browser restrictions on third-party storage can suppress a tag that depends on it. Validate firing in the conditions real users hit (the action completing where it actually completes), not only in a permissive test setup, so a tag that passes in the lab but fails in the wild is caught before launch.

The discipline is the same in every case: reproduce the real user journey, watch the tag fire at the moment the action completes in that exact context, and confirm the conversion lands in the report. A tag verified only on a clean top-level page is not verified for a cross-domain or framed conversion.

## Deduplication across tags

Floodlight already deduplicates a single conversion across DV360, SA360, and CM360 because those platforms share the activity definition, and it credits a click over an impression within the windows so post-click and post-view are not both counted for the same event. The deduplication problems you have to solve are the ones the platform cannot see:

- **Two deployment paths for one tag.** A hardcoded snippet plus the same tag in Tag Manager fires twice. Collapse to one path.
- **Two activities for one business event.** A purchase instrumented as two separate Floodlight activities double counts in any report that sums them. Define one activity per real event and retire the duplicate.
- **Overlapping platform tags on one action.** A Floodlight tag and a separate Google Ads conversion tag on the same action are two systems counting one event; that is expected (they are different systems) but must be read as such, never summed into one total. Keep platform conversions in their own columns. See `google-ads-conversion-tracking-and-attribution` for the Google Ads side.
- **Per-event over-counting from the wrong counting method.** A counter activity set to Standard where the business event is once-per-user inflates the count. The counting-method choice is `dv360-measurement-and-attribution`; here, suspect it when one user generates many conversions from one action.

When in doubt, trace one real conversion from the action to every place it is counted and confirm it appears once per system, in the right column. Summing across tags or systems is the error; counting once per system and reading them side by side is correct.

## Pixel inventory and retirement policy

Tags accumulate. Every campaign, vendor pilot, and one-off study leaves a tag behind, and an unowned tag is a liability: it leaks data, slows the page, and can keep counting into reports long after anyone remembers why. Govern the estate as a register, not as tribal knowledge.

- **Maintain a single inventory.** One source-of-truth list of every tag and pixel, carrying: the page or pages it is on, the owner (a named person or team), its purpose and the activity it maps to, the deployment path (direct or Tag Manager), the platform it serves, and the date it went live. A tag with no owner in the inventory is the definition of an orphan and is the first candidate for retirement.
- **Assign ownership at creation.** Every new tag gets an owner and an inventory row the day it ships (step 7 of the core process). Ownership is what makes retirement possible later; an unowned tag is one nobody is willing to remove because nobody knows what it does.
- **Review on a cadence.** Quarterly, reconcile the inventory against what is actually firing on the site (from the tag manager's tag list and a page scan). Flag any tag firing that is not in the inventory (an unauthorized or forgotten add) and any tag in the inventory that is no longer firing or no longer needed.
- **Retire stale tags deliberately.** A tag tied to an ended campaign, a churned vendor, or a discontinued activity should be removed, not left to rot. Before removing, confirm no live campaign or bid strategy depends on its activity, archive the historical conversion data per the measurement record, remove the tag from its deployment path (delete the Tag Manager tag or remove the snippet), and mark it retired in the inventory with the date and reason. Retiring through the deployment path, not by deleting the page, keeps the removal auditable.
- **Never leave a dangling test tag.** A tag placed to validate a launch (a test conversion) is removed or clearly marked as test once validation is done, so it never feeds a production count or a bid strategy.

The test of a healthy estate: for any tag firing on the site, you can name its owner and purpose from the inventory in seconds, and for any ended campaign, its tags are already retired. Anything you cannot explain is investigated and then owned or retired.

## Decision rules and thresholds

- **A tag is unverified until a real conversion clears all six validation gates.** Fired in the browser, present in the report, under the right activity, in the expected post-click or post-view column, in Conversions versus All Conversions as intended, and feeding (or deliberately not feeding) bidding. Stop short of any gate and treat the tag as not done.
- **One tag, one deployment path.** Direct or Tag Manager, never both for the same tag. Two paths is the default cause of double counting.
- **Prefer Tag Manager for any non-trivial tag estate.** Version control, a non-code change path, and one place to govern third-party tags outweigh the lighter direct install once more than a couple of tags are in play.
- **Consent-regulated traffic requires consent proven at the tag and at serving.** Confirm the banner updates the tag's consent state and that serving receives consent signals; do not assume a banner implies either. Prefer advanced Consent Mode to keep modeled signal.
- **Validate cross-domain and iframe conversions on the real journey.** A top-level page test does not prove a framed or cross-domain conversion fires. Reproduce the actual path across the boundary.
- **Count once per system, never sum across systems.** Floodlight and a Google Ads conversion on one action are two valid counts of one event; read them in separate columns, never add them.
- **Every tag has an owner and an inventory row from day one.** No owner means no one can safely retire it later. Unowned and stale tags are removed through their deployment path and marked retired with a date and reason.

## Common pitfalls

- **Declaring a tag done when the snippet is on the page.** The snippet is step two of seven. Unverified tags look finished and fail silently.
- **Hardcoding a tag and also firing it through Tag Manager.** The single most common double-count. One path per tag.
- **Editing a Floodlight activity and assuming the site tag updated.** It does not; the tag on the page must be redeployed after any activity change.
- **Testing only on a clean top-level page.** Cross-domain and iframe conversions fail in contexts a simple test never exercises. Reproduce the real journey.
- **Showing a consent banner but never passing the consent state to the tags.** The banner is theater if the tag's consent state never updates and serving never receives signals. Validate consent end to end.
- **Summing Floodlight and Google Ads conversions into one total.** Two systems counting one event are not additive. Keep them in separate columns.
- **Leaving test tags live.** A validation tag left firing feeds production counts and bid strategies with noise. Remove or clearly mark it after validation.
- **An estate nobody owns.** Tags with no owner and no inventory row cannot be safely retired, so they accumulate and leak. Assign ownership at creation and reconcile quarterly.

## Sources

- Create a Floodlight activity, Display & Video 360 Help: https://support.google.com/displayvideo/answer/2697097 (as of June 2026)
- About Floodlight and Floodlight activities, Display & Video 360 Help: https://support.google.com/displayvideo/answer/3027419 (as of June 2026)
- The Floodlight activities tab, Campaign Manager 360 Help: https://support.google.com/campaignmanager/answer/2823234 (as of June 2026)
- How Floodlight counts conversions, Campaign Manager 360 Help: https://support.google.com/campaignmanager/answer/2823400 (as of June 2026)
- Create an attribution model and change your primary model, Display & Video 360 Help: https://support.google.com/displayvideo/answer/7409983 (as of June 2026)
- Set up your Google tag across your Google accounts, Google Ads Help: https://support.google.com/google-ads/answer/12002338 (as of June 2026)
- Set up your Google tag across your Google accounts, Tag Manager Help: https://support.google.com/tagmanager/answer/12002338 (as of June 2026)
- Google Tag Manager vs. gtag.js, Tag Manager Help: https://support.google.com/tagmanager/answer/7582054 (as of June 2026)
- About consent mode, Google Ads Help: https://support.google.com/google-ads/answer/10000067 (as of June 2026)
- About Display & Video 360 and bidding on personalized ads inventory in compliance with the GDPR, Display & Video 360 Help: https://support.google.com/displayvideo/answer/9634508 (as of June 2026)
- About the creative review process, Display & Video 360 Help: https://support.google.com/displayvideo/answer/6063030 (as of June 2026)
