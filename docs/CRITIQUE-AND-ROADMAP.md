# Practitioner critique and roadmap

This package was reviewed by a panel of programmatic trader and operations personas: a CTV and
video trader, a performance and direct-response trader, an ad operations and trafficking lead,
an analytics and measurement lead, an agency account director, and a head of programmatic. This
file records what they praised, what was fixed and built in response, and what remains on the
roadmap, so nothing the panel raised is lost.

## What the panel praised

- The safe-by-default posture (read and recommend, gate the spend), enforced across skills, agents, loops, and tools.
- The troubleshooting and launch-QA discipline (the impression-loss model, top-down triage, one lever at a time).
- The measurement framing (incrementality over last-click, deduplicated reach, the "can this report fail?" test).
- The honesty about gated platforms (The Trade Desk written at the public-concept level, every claim sourced).

## Shipped in response to the critique

New skills:

- `dsp-selection`: which platform for which goal, and the tradeoffs that decide it.
- `incrementality-and-experimentation`: lift testing with real statistical rigor (conversion lift, geo lift, holdouts, power and minimum detectable effect, reading a result). The panel's number-one ask.
- `reach-and-frequency-planning`: deduplicated reach across platforms, effective frequency, and the identity limits.
- `dv360-youtube-and-video`: the biggest single coverage gap, buying YouTube and video on DV360.
- `dv360-creative-trafficking`: third-party tags, VAST, macros, secure tags, and a creative QA checklist.
- `client-deliverable-templates`: fill-in media plan, QBR deck, proposal, plain-English client glossary, and bad-news framing.

Fixes:

- Wired all seven agents and the `programmatic-foundations` router to route across all five platforms, not DV360 only. This was the headline finding.
- Aligned the DV360 attribution-model description with the current Google direction (data-driven and last interaction, with the rules-based models being retired), removing the contradiction with the Google Ads skill.
- Corrected the Amazon view-through viewability note to include the video threshold (2 continuous seconds) alongside display (1 second).
- Made the `creative-fatigue-watch` loop video-aware (video completion rate and the frequency distribution for non-skippable formats, not CTR).

## Roadmap (raised by the panel, not yet built)

Operations:

- A discrepancy and reconciliation playbook (third-party ad server versus DSP counts, tolerance, make-goods).
- A change-management and incident runbook (maker-checker approvals, severity tiers, first-five-minutes containment).
- A tag and pixel governance plus Floodlight setup-and-validation checklist, including Consent Mode on the DV360 side.
- A partner and advertiser onboarding runbook.

Performance:

- A value-based-bidding skill (constructing and feeding accurate conversion values, lifetime-value proxies, new-customer-acquisition value).
- A Google Ads Shopping and feed-quality skill (Merchant Center, feed attributes, product-level performance).
- A bid-landscape and win-rate economics skill (the bid-response curve, marginal CPA versus volume).
- A direct-response creative-testing skill (experiments, asset-level reading, significance).

Analytics:

- Geo-lift and marketing-mix-modeling depth, and a data-quality and reconciliation skill with a real anomaly-detection method (seasonality and day-of-week, not a flat tolerance).
- Cross-platform reporting-warehouse patterns (a unified schema across the five platforms).

Team and scale:

- A trader onboarding path and a top-level junior glossary.
- An approval-matrix and escalation-governance skill (who signs off on what), plus service levels and a capability model.

Brand safety and compliance:

- Made-for-advertising and invalid-traffic depth, suitability tiers, regulated categories, supply-path transparency (sellers.json, ads.txt), and a privacy and consent skill (GDPR, CPRA, Consent Mode, UID2 consent).

CTV and video:

- A cross-platform reach-and-frequency loop and a video completion loop, and a DV360 video creative-specs reference.

Depth parity:

- Bring the non-DV360 platforms up to DV360's reference-file depth (audiences, inventory, API field maps).
