---
name: privacy-and-consent
description: Apply privacy law and consent signals to programmatic buying across regions and DSPs: GDPR, the California privacy law (CCPA and CPRA), Google Consent Mode, the IAB Transparency and Consent Framework (TCF), consent for identity solutions (UID2 and EUID), the cookieless transition and the Privacy Sandbox, hashed first-party data, and clean rooms. Use when the user asks about privacy, consent, GDPR, CCPA, CPRA, Consent Mode, TCF, cookieless, the Privacy Sandbox, third-party cookies, the Global Privacy Platform, or consent for UID2 and EUID, and how regional consent changes what data and signals you can use.
---

# Privacy and consent

Decide what data and which signals you may use for a given user in a given region, and configure consent so measurement and targeting survive it. This skill is DSP-agnostic: it encodes the legal bases, the consent frameworks, and the identity-signal eligibility rules an experienced trader applies on any platform. Regional consent is the gate; everything downstream (audiences, identity, measurement) depends on what that gate allows.

For shared definitions and KPI math, see the `programmatic-foundations` skill. This skill owns consent and regional eligibility; the measurement and identity skills own the mechanics of building on top of what consent permits.

## When to use this skill

Use when the user wants to:

- Determine whether they may use third-party cookies, device identifiers, hashed emails, or behavioral audiences for a user in a given region.
- Configure or interpret Google Consent Mode (the current version) and how consent state changes what is collected.
- Work with the IAB Transparency and Consent Framework (TCF) or the Global Privacy Platform (GPP), including the US state privacy signals.
- Apply GDPR (consent and legitimate interest) or the California privacy law (CCPA as amended by CPRA), including opt-out of sale or sharing and Global Privacy Control.
- Use an identity solution (UID2 or EUID) and get the consent and legal basis right for each.
- Plan for the cookieless transition, the Privacy Sandbox, hashed first-party data, and clean-room measurement.

Boundary with sibling skills:

- For UID2 setup, token mechanics, and identity graph operations on a specific DSP, hand off to `ttd-identity-and-uid2`. This skill owns the consent and legal-basis layer; that skill owns the integration.
- For privacy-safe measurement and clean-room analysis, use `dv360-advanced-analytics-adh` (Ads Data Hub) and `amazon-marketing-cloud` (AMC). This skill owns when you may use a clean room and what data may enter it; those skills own the queries.
- For attribution windows and conversion measurement under consent, use `dv360-measurement-and-attribution`.
- For brand safety, regulated categories, and COPPA on CTV, use `brand-safety-and-suitability`.

## Quick reference

| Region or context | Default legal basis for ad targeting | Signal you can rely on |
| --- | --- | --- |
| EU and UK (GDPR) | Consent, captured via a TCF consent management platform | Behavioral data only with opt-in consent; otherwise contextual |
| California (CCPA and CPRA) | Notice plus right to opt out of sale or sharing | Behavioral allowed until the user opts out; honor GPC |
| Other US states | Notice plus opt-out (varies by state) | Signal via GPP and the relevant US state string |
| Cookieless or consent denied | Modeling and contextual | Consent Mode pings, first-party data, clean-room matches |
| Logged-in or first-party | First-party consent you collected | Hashed first-party identifiers, identity solutions where consented |

## Core process

1. **Resolve the region and legal basis first, because it gates every signal downstream.** Under GDPR (EU and UK), targeting and most ad measurement need opt-in consent; legitimate interest is not a safe basis for cross-site advertising and the TCF has tightened around it. Under the California law (CCPA as amended by CPRA), you may process personal information with notice but must honor a request to opt out of sale or sharing and must respect the Global Privacy Control signal as such a request. Other US states follow their own opt-out regimes. Determine the user's region and basis before deciding what data you may use.

2. **Capture consent with the right framework and pass it through.** In the EU and UK, use a TCF-registered consent management platform so the consent state travels with the bid request as a standard string vendors can read. Across US states, the Global Privacy Platform (GPP) carries the US national and state strings and the opt-out signals. Do not invent a bespoke consent flow when a standard string exists; downstream vendors only honor what they can parse.

3. **Configure Consent Mode so denied consent still yields modeled measurement.** Google Consent Mode communicates the user's consent state to Google tags, which adjust behavior accordingly. The current version uses the consent signals `ad_storage`, `analytics_storage`, `ad_user_data`, and `ad_personalization`. Choose advanced Consent Mode when you want tags to load and send privacy-preserving cookieless pings while consent is denied (enabling conversion modeling), and basic Consent Mode when tags must not load at all until the user consents. Advanced preserves more measurement signal; basic is stricter. Allow at least the documented learning window before judging modeled uplift.

4. **Pick the identity solution that matches the region's consent regime.** UID2 (Unified ID 2.0) is a deterministic identifier built from a hashed and salted email or phone number, with consumer opt-out through its transparency portal; it is governed in line with US privacy law (CCPA and CPRA). EUID (European Unified ID) builds on the same framework but is a separate namespace governed for European and UK law, driven by GDPR, the TCF, and local guidance. Use UID2 where US consent applies and EUID where European consent applies; do not run a US-consented identifier against EU traffic. The legal basis still flows from step 1: an identity solution does not replace consent, it carries an identifier you are already permitted to use.

5. **Plan for cookieless as the floor, not a deadline, because the timeline changed.** Verify the current state before asserting it. As of mid-2026: in April 2025 Google decided not to roll out a new standalone third-party-cookie prompt in Chrome, so third-party cookies remain available to users by their existing settings rather than being deprecated on a fixed date. In October 2025 Google announced it would retire most Privacy Sandbox advertising APIs (including Topics, Protected Audience, and Attribution Reporting), keeping a smaller set of platform privacy features (such as CHIPS, FedCM, and Private State Tokens) and continuing standards work on an interoperable attribution proposal. The practical consequence: do not architect on Privacy Sandbox advertising APIs, and do not assume a hard cookie cutoff, but still build durable measurement and addressability that does not depend on third-party cookies, because Safari and Firefox already block them and consent already removes them for many users.

6. **Lead with hashed first-party data and clean rooms for durable, consented addressability.** Collect first-party identifiers (typically email) under your own consent, hash them (SHA-256, normalized) before they leave your environment, and use them for matching, suppression, and identity solutions where consent allows. For measurement and overlap analysis without moving raw user data, use a clean room: each party brings consented data, queries run on the joined set, and only aggregated, privacy-thresholded output leaves. This is the addressability path that survives cookie loss and satisfies regional consent, provided the data entering it was consented for that use.

7. **Let regional consent narrow the toolset, and fall back gracefully.** When consent is absent or denied, do not target behaviorally: use contextual, modeled conversions from Consent Mode pings, and aggregated clean-room measurement. When consent is present and regionally valid, layer first-party identifiers, the matching identity solution, and standard audiences. The fallback is contextual plus modeling, never silently dropping signals you were not permitted to use in the first place.

## Decision rules and thresholds

- **GDPR means opt-in or contextual.** No valid opt-in consent in the EU or UK means no behavioral targeting and no cross-site identifiers for that user. Run contextual and rely on aggregated or modeled measurement. Do not lean on legitimate interest for cross-site advertising.

- **California means honor the opt-out, including GPC.** You may target until the user opts out of sale or sharing, but you must treat a Global Privacy Control browser signal as a valid opt-out request and stop selling or sharing that user's data. Confirm your stack reads and honors GPC.

- **Match the identifier to the regime.** UID2 for US-consented traffic, EUID for European-consented traffic. Never apply a US-consented identifier to EU users or vice versa; the namespaces and legal bases differ.

- **Consent Mode choice.** Use advanced Consent Mode when modeled conversions matter and the legal team accepts cookieless pings on denied consent; use basic Consent Mode when no tag may fire before consent. Advanced retains more signal; basic is the conservative default for the strictest interpretations.

- **Do not build on retired Privacy Sandbox advertising APIs.** Topics, Protected Audience, and Attribution Reporting are being wound down. Treat the surviving platform features (CHIPS, FedCM, Private State Tokens) as infrastructure, not as a targeting stack, and invest in first-party data, identity solutions, and clean rooms. Re-verify status before committing, since this area keeps moving.

- **Hash before data leaves your environment.** Normalize (lowercase, trim) and SHA-256 email addresses on your side before sharing for match or identity. Never ship raw personal data to a partner or a clean room when a hash or an aggregated query will do.

- **Clean-room gate.** Data may enter a clean room only if it was consented for that purpose. Output must be aggregated and above the clean room's privacy threshold. If a query would expose user-level data, it does not belong in the clean room.

## Reference material

This skill is self-contained on the consent and eligibility layer. For identity mechanics read `ttd-identity-and-uid2`; for clean-room queries read `dv360-advanced-analytics-adh` and `amazon-marketing-cloud`; for attribution under consent read `dv360-measurement-and-attribution`.

## Templates and examples

**Pan-European awareness campaign.** Region is GDPR, so consent is the gate. A TCF consent management platform captures opt-in and passes the consent string. Where consent is granted, run EUID and first-party audiences; where denied, run contextual only. Advanced Consent Mode supplies modeled conversions for the denied population. No US-consented identifiers touch this traffic.

**US retail performance campaign.** Region is the California and other US state laws. GPP carries the state strings; the stack honors Global Privacy Control as an opt-out of sale or sharing. UID2 built from hashed first-party emails drives addressability for consented users; opted-out users drop to contextual. Measurement runs in a clean room on consented data with aggregated output.

**Cross-region brand with one creative.** Split by region at the gate. EU and UK traffic follows the GDPR template (consent or contextual, EUID); US traffic follows the US template (opt-out honored, UID2). Do not let the EU and US identifier graphs mix. Plan all measurement to work without third-party cookies, since they are already gone for much of the audience.

**Cookieless measurement fallback.** Consent denied or no third-party cookie available. Use Consent Mode cookieless pings for modeled conversions, contextual targeting for delivery, and a clean room for overlap and incrementality on consented first-party data. Report modeled and aggregated figures, and state that they are modeled.

## Common pitfalls

- Treating legitimate interest as a basis for cross-site advertising under GDPR. It is not safe; rely on opt-in consent or run contextual.
- Ignoring Global Privacy Control in California. GPC is a valid opt-out request; the stack must read and honor it.
- Running a US-consented identifier (UID2) against EU traffic, or EUID against US traffic. Match the identifier to the region's consent regime.
- Assuming third-party cookies will be killed on a fixed date. As of mid-2026 Google is not deprecating them on a set timeline, but Safari and Firefox already block them and consent removes them for many users, so build cookie-independent measurement anyway. Verify current state before asserting it.
- Architecting on Privacy Sandbox advertising APIs (Topics, Protected Audience, Attribution Reporting). They are being retired; lead with first-party data, identity solutions, and clean rooms.
- Shipping raw personal data to a partner or clean room. Normalize and SHA-256 hash on your side first, and keep clean-room output aggregated.
- Building a bespoke consent flow when a TCF or GPP string exists. Downstream vendors only honor signals they can parse.
- Choosing basic Consent Mode and then expecting full conversion data on denied consent. Basic blocks the tag; use advanced if you need modeled conversions.

## Sources

- Regulation (EU) 2016/679 (GDPR), official text on EUR-Lex: https://eur-lex.europa.eu/eli/reg/2016/679/oj (as of June 2026)
- California Consumer Privacy Act (CCPA), California Attorney General: https://oag.ca.gov/privacy/ccpa (as of June 2026)
- About Consent Mode, Google Ads Help: https://support.google.com/google-ads/answer/10000067 (as of June 2026)
- Consent Mode, Google tag platform developer documentation: https://developers.google.com/tag-platform/security/concepts/consent-mode (as of June 2026)
- IAB Europe Transparency and Consent Framework (TCF): https://iabeurope.eu/transparency-consent-framework/ (as of June 2026)
- IAB Tech Lab Global Privacy Platform (GPP): https://iabtechlab.com/gpp/ (as of June 2026)
- UID2 documentation: https://unifiedid.com/docs/intro (as of June 2026)
- EUID documentation: https://euid.eu/docs/intro (as of June 2026)
- Next steps for Privacy Sandbox and tracking protections in Chrome (April 2025): https://privacysandbox.google.com/blog/privacy-sandbox-next-steps (as of June 2026)
- Update on plans for Privacy Sandbox technologies (October 2025): https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies (as of June 2026)
