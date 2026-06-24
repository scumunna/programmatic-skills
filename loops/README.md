# Programmatic loop library

A catalog of repeatable agent loops for programmatic traders, analysts, and ad-operations
specialists. Each loop is a bounded feedback cycle: it observes fresh state, chooses one
in-scope action, acts, verifies against an observable check, records what it did, and repeats
only while progress is measurable. Then it stops in a named terminal state.

These loops are recipes. They do not run themselves. You invoke one on demand or put it on a
schedule. They pair with the skills and the specialist agents in this repository.

## The safe-by-default posture

Every loop here monitors, diagnoses, and recommends. None applies a budget change, a bid
change, a pause, a targeting change, or a client message on its own. Those actions are gated on
human approval, matching the safe-to-automate guidance in each platform's skills. A loop reads
state, produces a recommendation or an artifact, and hands the decision to a person.

This is deliberate. Programmatic changes spend real money and reach real people, so a loop
should make a person faster and better informed, not take the wheel.

## Loop anatomy

Each loop documents:

- **Use when:** the trigger. When to run it.
- **Action:** the bounded steps, and which skills and agents it uses.
- **Verify:** the observable acceptance check. A threshold or an independent review, not "until it looks good."
- **Stop:** the terminal states. Done, nothing to do, blocked, approval needed, or no measurable progress.
- **Guardrails:** the limits and the approval boundary.
- **Handoff:** who or what the loop hands its output to.
- **Prompt:** a short, copy-ready prompt.

## How to run a loop

- On demand: paste the loop's Prompt to your agent.
- On a schedule: in Claude Code use the `/schedule` command. In any runtime, wire the Prompt into your scheduler. A loop runs only when you enable it.

## Index

| Loop | Use when | Hands off to |
| --- | --- | --- |
| [daily-pacing-sweep](daily-pacing-sweep.md) | Each morning, across live campaigns | The trader, for approval of any fix |
| [weekly-optimization-pass](weekly-optimization-pass.md) | Weekly, per campaign against its KPI | qa-scrutinizer, then the trader |
| [pre-launch-qa-gate](pre-launch-qa-gate.md) | Before any campaign goes live | qa-scrutinizer, then go or no-go |
| [budget-reallocation](budget-reallocation.md) | When spend efficiency diverges across lines | The trader, for approval |
| [creative-fatigue-watch](creative-fatigue-watch.md) | When frequency rises and response falls | The trader, for a creative refresh |
| [delivery-and-deal-watch](delivery-and-deal-watch.md) | When a line or deal underdelivers | optimization-specialist, then approval |
| [anomaly-detection](anomaly-detection.md) | Daily, on the core metric set | The trader or analyst, as an alert |
| [search-term-mining](search-term-mining.md) | Weekly, on search and query data | The trader, for approval to apply |
| [brand-safety-monitor](brand-safety-monitor.md) | Daily or weekly, on quality signals | The trader, for approval of exclusions |
| [weekly-client-report](weekly-client-report.md) | Weekly or per reporting cadence | The client, after independent review |
| [audience-performance-review](audience-performance-review.md) | Weekly, on audience and segment data | The trader, for approval |
| [business-review-prep](business-review-prep.md) | Before a monthly or quarterly review | The client team, after review |
| [frequency-saturation-watch](frequency-saturation-watch.md) | On reach campaigns and long CTV flights | The trader, for a cap or fresh reach |
| [video-completion-watch](video-completion-watch.md) | In flight on video and CTV | The trader, or brand safety for placements |

## Format credit

The loop format (an explicit trigger, action, verification, stopping condition, guardrails, and
handoff) follows the spirit of the Forward Future Loop Library at
signals.forwardfuture.ai/loop-library. The loops in this folder are original to this repository
and are not published there.
