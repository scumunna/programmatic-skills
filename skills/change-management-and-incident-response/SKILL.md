---
name: change-management-and-incident-response
description: Make changes safely and run incidents calmly in live ad accounts. Use when the user says "change management", "approval process", "four eyes", "maker checker", "bulk edit safely", "pre-flight check", "rollback", "incident", "runbook", "runaway spend", "spend spike", "a deal went dark", "pixel outage", "brand-safety breach", "postmortem", or asks how to apply a large edit without breaking live delivery. Covers the four-eyes approval pattern, a bulk-edit safety sequence, severity tiers, first-five-minutes containment, escalation, and a postmortem template.
---

# Change management and incident response

Live ad accounts spend real money every minute, so a careless bulk edit or a slow incident response burns budget you cannot get back. This skill gives you a maker-checker approval pattern, a pre-flight safety sequence for bulk edits, and an incident runbook with severity tiers and first-five-minutes containment for the failures that actually happen: runaway spend, a deal going dark mid-flight, a tracking or pixel outage, and a brand-safety breach.

For the API, Structured Data Files, and the safe-to-automate matrix that bulk edits ride on, see `dv360-api-and-sdf-automation`. For diagnosing a single line item that is misbehaving, see `dv360-troubleshooting`. For who is allowed to approve what and the formal escalation ladder, see `approval-and-escalation-governance`. This skill is the operational drill; that skill is the authority model.

## When to use this skill

- You are about to apply a bulk edit (many line items, an SDF upload, an API batch) and want a safety sequence so a mistake is bounded and reversible.
- You need a maker-checker (four-eyes) approval pattern before a risky change ships.
- Something is on fire right now: spend is running away, a deal stopped delivering, a pixel or tag is down, or unsafe inventory is serving, and you need the first five minutes.
- You need a severity model so the team treats a spend spike and a typo with the right urgency.
- The incident is over and you owe a postmortem.

Boundaries with sibling skills:

- API auth, SDF round trips, batch limits, and which operations are safe to automate at all: `dv360-api-and-sdf-automation`.
- Symptom-by-symptom diagnosis of a non-delivering or misbehaving line item: `dv360-troubleshooting`.
- Approval authority, sign-off thresholds, and the formal escalation ladder: `approval-and-escalation-governance`.
- Reconciling delivered vs billed after an incident distorted delivery: `discrepancy-and-reconciliation`.

## Quick reference: pick the right play

| Situation | Play |
| --- | --- |
| Risky change, not yet made | Maker-checker approval, then the bulk-edit safety sequence |
| Large edit across many entities | Bulk-edit pre-flight safety sequence (six steps below) |
| Something is actively breaking | Incident runbook: classify severity, contain in five minutes, then fix |
| Spend, deal, pixel, or brand-safety failure | The matching first-five-minutes drill |
| Incident resolved | Postmortem template, blameless |

Default posture: changes are reversible until proven safe. Never apply a bulk edit you cannot roll back, and never let an unbounded incident run while you investigate. Contain first, diagnose second.

## Maker-checker (four-eyes) approval

One person prepares a change; a different person reviews and approves it before it goes live. The reviewer is not the maker. This catches the class of error a maker is blind to (wrong scope, a fat-fingered budget, a targeting inversion) precisely because the maker already believes the change is correct.

Apply four-eyes whenever a change is hard to reverse or moves money at scale:

- Budget or bid changes above the team's defined threshold (set it in `approval-and-escalation-governance`).
- Any bulk edit touching more than a handful of entities, or any SDF or API batch.
- Targeting, flight, or pacing changes on a flighted, high-spend campaign.
- Activating or repricing a deal.
- Anything touching brand-safety or suitability controls.

The pattern:

1. **Maker prepares and documents.** What is changing, on which exact entities, why, the expected effect, and the rollback. The maker attaches the before-state export and the proposed diff.
2. **Checker reviews against intent.** The checker confirms the scope matches the request, the numbers are sane, and the rollback is real. The checker is empowered to reject.
3. **Approve, then apply.** Only after explicit approval does the change ship. The approval and the diff are recorded.
4. **Both verify the result.** Maker and checker confirm the post-change state matches the expected effect, using the result file or a fresh report.

Standard control practice, not a platform feature: the platform will let one person push a catastrophic change. Four-eyes is a process you impose, not a button the tool provides.

## Bulk-edit pre-flight safety sequence

Run all six steps in order for any bulk edit. The sequence makes a mistake small (bounded scope), visible (reviewed diff), and reversible (snapshot plus documented rollback). Skipping a step is how a single upload pauses an entire account.

1. **Snapshot current state.** Export the exact entities you are about to change before you touch them (SDF download or API read), and save it as the rollback artifact. If you cannot snapshot it, you cannot safely change it.
2. **Bound the scope.** Filter to the precise set of entities the change should hit, then count them. Confirm the count matches your intent. A scope of "all line items" when you meant "these twelve" is the most common bulk-edit disaster.
3. **Review the diff.** Compare the proposed file against the snapshot field by field. Confirm only the columns you intend to change differ, and that every changed value is what you expect. Unintended column changes (a tool rewriting a field you did not touch) are caught here.
4. **Stage the apply.** Apply to a small canary slice first (one or a few entities), or use a validate-only or dry-run path if the platform offers one, before the full batch. Respect batch limits; the SDF format caps entries per file, so split large changes rather than forcing one oversized upload.
5. **Verify the result file.** Read back what the platform reports it actually changed (the upload result or API response). Confirm success on every row and reconcile the changed count against your bounded scope from step 2. Do not assume success because the upload did not error.
6. **Document the rollback.** Record exactly how to revert: re-upload the snapshot from step 1, or the specific inverse operation, with the entity IDs. Keep it with the change record so anyone on the team can execute it under pressure.

For SDF round trips, batch limits, validate-only behavior, and which operations are safe to automate, follow `dv360-api-and-sdf-automation`. Treat anything it flags as human-in-the-loop as a hard four-eyes gate.

## Incident runbook

An incident is any live failure burning budget, breaking measurement, or risking the brand. The order is always the same: classify, contain, diagnose, fix, verify, write it up. Containment comes before diagnosis, because an unbounded incident gets more expensive every minute you investigate.

### Severity tiers

| Tier | Definition | Response |
| --- | --- | --- |
| **Sev 1** | Money or brand at acute risk: runaway spend, brand-safety breach serving now, an outage corrupting all billing data | Contain immediately, page the lead, all-hands until contained |
| **Sev 2** | Material delivery or measurement broken but bounded: a key deal dark, a pixel outage on a major advertiser, pacing badly wrong | Contain within the hour, notify the lead and the client owner |
| **Sev 3** | Localized or low-dollar: one line item misbehaving, a minor reporting gap | Handle in normal workflow, log it |

Classify on blast radius and dollars per hour, not on how alarming it feels. A 5x overspend on a small test line is Sev 3; a deal going dark on a flagship flight is Sev 2; unsafe inventory serving against a regulated brand is Sev 1.

### First five minutes by incident type

**Runaway pacing and spend (spend spike, budget exhausting fast).**

1. Stop the bleed: pause the offending line item or insertion order, or hard-cap the budget to near current spend. Pausing is reversible; an exhausted daily budget is not.
2. Bound the loss: note current spend vs plan and the dollars-per-hour rate so you can size the impact and the make-good.
3. Then diagnose: ASAP pacing left on, a daily cap removed, an automated bid spending into cheap inventory, or a flight shorter than the budget assumed. Hand the diagnosis to `dv360-troubleshooting` and the pacing fix to `dv360-pacing-and-optimization`.

**A deal gone dark mid-flight (delivering, then suddenly zero).**

1. Confirm scope: is it this one deal, or did a parent pause or a bulk edit take down more? Check the most recent change first; a deal going dark right after an edit is the edit until proven otherwise.
2. Contain the knock-on: if guaranteed delivery is at risk, shift the committed budget to a backup line or deal so you do not also miss the guarantee while you fix the deal.
3. Then diagnose: deal expired or paused on the sell side, unmapped from the line item, a bid now below the deal floor, or targeting on the line item excluding the deal inventory. Full deal tree in `dv360-deals-and-inventory`.

**A tracking or pixel outage (conversions flatline, a tag stops firing).**

1. Confirm it is measurement, not media: is delivery still normal while conversions or measured impressions dropped to zero? If delivery is healthy, treat it as a measurement incident, not a performance one.
2. Protect decisions: freeze any automated bidding or optimization that feeds on the broken signal, so a dead pixel does not drive the algorithm to throttle a healthy campaign.
3. Then diagnose: the pixel or Floodlight tag removed from the site, a container or consent change suppressing it, or a tag-manager break. Coordinate the site-side fix; measurement plumbing detail lives in `dv360-measurement-and-attribution`.

**A brand-safety breach (ads serving against unsafe or off-limits content).**

1. Stop serving into the unsafe context immediately: pause the affected line items and apply or tighten the relevant exclusion. With a regulated or sensitive brand, pause broad and narrow back later; the cost of over-pausing is far below the cost of one more unsafe impression.
2. Preserve evidence: capture the placement, domain or app, screenshot, and timestamp before anything changes, for the client conversation and the postmortem.
3. Then diagnose and harden: a gap in the exclusion list, a new domain, a wrapper or CTV app bypassing controls, or a verification vendor misfire. Hand the durable fix to `dv360-frequency-and-brand-safety`.

### Escalation path

Escalate on tier and on time-in-state, not on ego. Default ladder (tune the names and thresholds in `approval-and-escalation-governance`):

1. **On-call ad ops** owns first response and containment for every incident.
2. **Ops lead or account lead** is paged immediately for Sev 1, and within the hour for an uncontained Sev 2.
3. **Client or advertiser owner** is told as soon as the incident is contained and the impact is sized, for anything client-affecting. Tell them with a number and a remedy, not just an alarm.
4. **Finance** is looped when spend impact or a make-good or credit will hit billing, so it flows into close. Hand the dollar impact to `discrepancy-and-reconciliation`.

Rule: if an incident is not contained within its tier's window, escalate up one level rather than keep grinding alone.

## Postmortem template

Write one for every Sev 1 and Sev 2, blameless, within a couple of days while memory is fresh. The goal is a systemic fix, not a name.

```
Incident: <short title>
Severity: Sev <1|2|3>
Date / duration: <start> to <contained> to <resolved> (time zone)
Owner: <incident owner>

Impact
- What broke, who was affected, and the dollar or delivery impact (quantified).

Timeline
- <time> detection (how it was caught: alert, client, manual)
- <time> containment action
- <time> root cause identified
- <time> resolved

Root cause
- The actual cause, not the symptom. Why did it happen and why now?

What went well / what hurt
- Detection speed, containment, communication, tooling.

Action items (owner, due date)
- Prevention: the systemic fix so this class cannot recur.
- Detection: the alert or check that would have caught it sooner.
- Process: the four-eyes gate, runbook step, or threshold to add.

Billing follow-up
- Make-good or credit owed? Handed to reconciliation? (link)
```

## Common pitfalls

- **Diagnosing before containing.** Every minute spent investigating a runaway spend is more money gone. Pause or cap first, then investigate the paused entity.
- **Bulk-editing without a snapshot.** No before-state means no rollback. Export first, every time, even for a "quick" change.
- **A scope that is wider than you think.** "All line items" instead of "these twelve" is the classic bulk disaster. Count the bounded set before you apply.
- **Trusting an upload that did not error.** Silence is not success. Read the result file and reconcile the changed count.
- **Maker checking their own work.** Self-review misses the error the maker is blind to. The checker must be a second person.
- **Optimizing on a broken signal.** A dead pixel makes a healthy campaign look like a failure. Freeze automated optimization during a measurement outage.
- **A blameful postmortem.** Blame suppresses the honest timeline you need. Fix the system, not the person.

## Reference material

- For the SDF round trip, batch limits, validate-only behavior, and the safe-to-automate matrix behind every bulk edit: `dv360-api-and-sdf-automation`.
- For symptom-by-symptom diagnosis once an incident is contained: `dv360-troubleshooting`.
- For approval authority, sign-off thresholds, and the formal escalation ladder: `approval-and-escalation-governance`.

## Sources

- Structured Data File (SDF) format (round-trip format, per-file entry limits, partial upload): https://developers.google.com/display-video/api/structured-data-file/format (as of June 2026)
- Run an ad campaign (DV360 API guide, programmatic create and edit workflow): https://developers.google.com/display-video/api/guides/managing-line-items/overview (as of June 2026)
- Monitor impression loss (reading a pacing or delivery failure during an incident): https://support.google.com/displayvideo/answer/3103324 (as of June 2026)
- Troubleshoot your deals and line items (a deal going dark; prebid and brand-safety filtering view): https://support.google.com/displayvideo/answer/6292894 (as of June 2026)
