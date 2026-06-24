# Daily pacing sweep

Each morning, find the campaigns that will miss their flight and surface a recommended fix for each, then stop once every live campaign has been checked.

- **Use when:** Daily, at the start of the trading day, across all live campaigns.
- **Action:** Read current pacing against flight for each live campaign (`dv360-pacing-and-optimization`, or the matching platform skill). For each campaign that is under or over the expected spend curve, name the likely binding constraint using the impression-loss model and write one recommended fix with its expected effect. Use the `optimization-specialist` agent.
- **Verify:** Every live campaign appears in the output with a pacing status (on track, under, or over) and, where off track, one specific recommendation. Pacing math is shown, not asserted.
- **Stop:** Done when all live campaigns are reviewed. Clean no-op if everything is on track. Re-run tomorrow, not in a tight loop.
- **Guardrails:** Read and recommend only. Do not change budgets, bids, or pacing. Use the current day's pacing data, not yesterday's cached view. Hold conversion-based conclusions if the conversion data is only a few hours old.
- **Handoff:** The trader, who approves and applies any fix. Escalate a structural delivery failure to [delivery-and-deal-watch](delivery-and-deal-watch.md).

Prompt:
> Each morning, review pacing against flight for every live campaign. For each one off the expected spend curve, name the binding constraint (show the pacing math) and recommend one fix with its expected effect. Report only. Do not change budgets, bids, or pacing. Stop when all live campaigns are reviewed. Flag any change you recommend for my approval before it is applied.
