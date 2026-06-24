# Practitioner critique and roadmap

This package was reviewed by a panel of programmatic trader and operations personas: a CTV and
video trader, a performance and direct-response trader, an ad operations and trafficking lead,
an analytics and measurement lead, an agency account director, and a head of programmatic. This
file records what they praised, what was built in response across two waves, what genuinely
remains, and the honest limits that building more cannot fix.

## Honest limits (read this first)

Two gaps are real and are not closed by adding more skills:

1. **It advises; it does not act.** By default the package is knowledge. It cannot log into a real account and make changes. A human still does the work in the platform. The connection guide (`docs/CONNECTING-TOOLS.md`) explains the safe path to live data, but actions stay human-gated by design.
2. **The review was simulated.** The panel below was AI personas, not real traders using this on live campaigns. The single most valuable next step is getting one or two working traders to use it and report where it breaks. Until then, "reviewed by practitioners" is aspirational.

Other standing limits: the content is a June 2026 snapshot and drifts as platforms change; depth is uneven (DV360 is deep and operational, The Trade Desk and StackAdapt are concept-level because their docs are gated).

## What the panel praised

- The safe-by-default posture (read and recommend, gate the spend), enforced across skills, agents, loops, and tools.
- The troubleshooting and launch-QA discipline (the impression-loss model, top-down triage, one lever at a time).
- The measurement framing (incrementality over last-click, deduplicated reach, the "can this report fail?" test).
- The honesty about gated platforms (The Trade Desk written at the public-concept level, every claim sourced).

## Shipped, first wave

New skills: `dsp-selection`, `incrementality-and-experimentation`, `reach-and-frequency-planning`,
`dv360-youtube-and-video`, `dv360-creative-trafficking`, `client-deliverable-templates`.

Fixes: wired all seven agents and the `programmatic-foundations` router across all five platforms;
aligned the DV360 attribution-model description with the current data-driven and last-interaction
direction; corrected the Amazon view-through viewability note for video; made the
`creative-fatigue-watch` loop video-aware.

## Shipped, second wave (the deferred roadmap)

Operations: `discrepancy-and-reconciliation`, `change-management-and-incident-response`,
`tag-and-pixel-governance`, `partner-and-advertiser-onboarding`.

Performance: `value-based-bidding`, `bid-landscape-and-win-rate`, `google-ads-shopping-and-feed`.

Analytics: `data-quality-and-reconciliation`, `marketing-mix-modeling`.

Brand safety and privacy: `brand-safety-and-suitability`, `privacy-and-consent`.

Team and scale: `trader-onboarding`, `approval-and-escalation-governance`.

CTV loops: `frequency-saturation-watch`, `video-completion-watch`.

## What genuinely remains

- A direct-response creative-testing skill (experiments, asset-level reading, significance).
- Cross-platform reporting-warehouse patterns (a unified schema across the five platforms).
- A DV360 video creative-specs reference (the trafficking skill covers the serving mechanics; exact specs are deferred to the live help).
- Depth parity: bringing The Trade Desk, StackAdapt, and Amazon DSP up to DV360's reference-file depth. This is an ongoing effort, bounded by how much each platform documents publicly.
- The two limits at the top: real-world practitioner validation, and live in-account action (which is deliberately human-gated).
