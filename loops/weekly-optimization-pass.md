# Weekly optimization pass

Once a week, improve each campaign toward its KPI by proposing one change at a time and verifying the last change worked, stopping when the KPI is met or two cycles show no measurable gain.

- **Use when:** Weekly, per campaign, against the KPI set in its plan.
- **Action:** Pull the goal-appropriate report (`reporting-by-campaign-goal`, the platform reporting skill). Diagnose the single binding constraint with the platform troubleshooting and optimization skills. Propose exactly one change with its expected impact. After a human approves and applies it, on the next cycle verify the change against the KPI before proposing the next one. Use the `optimization-specialist` agent.
- **Verify:** The KPI moves in the intended direction after the applied change, read against the campaign objective and not a vanity metric. One lever changed per cycle so the effect is attributable.
- **Stop:** Success when the KPI reaches target. Stagnated when two consecutive cycles produce no measurable improvement; escalate instead of churning. Blocked if the report or conversion data is missing.
- **Guardrails:** One change per cycle. Every change requires approval before it is applied. Do not re-optimize on conversion data less than about a day old. Do not stack edits.
- **Handoff:** `qa-scrutinizer` reviews the recommendation, then the trader approves and applies it.

Prompt:
> Once a week per campaign, pull the report for its goal, diagnose the one binding constraint, and propose a single change with its expected impact. Have it reviewed, then I will approve and apply it. Next week, verify that change against the KPI before proposing the next. Change one lever at a time. Stop when the KPI is on target or two cycles show no measurable gain, and tell me when you stop.
