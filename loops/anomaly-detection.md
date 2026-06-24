# Anomaly detection

Once a day, scan the core metrics against their recent baseline and raise an alert on anything that breaks out, stopping when the scan is complete.

- **Use when:** Daily, on the core metric set for live campaigns (spend, CPA or ROAS, CTR, viewability, win rate, conversion volume).
- **Action:** Read today's values and compare each to its recent baseline (`reporting-by-campaign-goal`, the platform reporting skill). Flag any metric that moves beyond a set tolerance, up or down, with the campaign, the metric, the change, and a likely explanation to check. Use the `reporting-analyst` agent.
- **Verify:** Each alert states the baseline, the current value, and the size of the move against the tolerance, so it is reproducible rather than a feeling. Normal variation is not flagged.
- **Stop:** Done when the scan completes. Clean no-op if nothing breaches tolerance. Run again tomorrow.
- **Guardrails:** Alert only. Do not change anything. A spike can be a tracking break, not a real change, so the alert proposes what to check rather than asserting a cause. Use fresh data and note where conversion lag may distort a same-day read.
- **Handoff:** The trader or analyst, who investigates with [delivery-and-deal-watch](delivery-and-deal-watch.md) or the weekly optimization pass.

Prompt:
> Once a day, compare each core metric (spend, CPA or ROAS, CTR, viewability, win rate, conversions) to its recent baseline and alert on any move beyond the agreed tolerance, showing baseline, current value, and the size of the change, with a likely cause to check. Alert only; change nothing. Do not flag normal variation. Stop when the scan is complete.
