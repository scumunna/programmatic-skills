# Delivery and deal watch

When a line item or a deal is underdelivering, run the triage to the single binding cause and return it with a fix, stopping once the cause is identified or no issue is found.

- **Use when:** A line item underdelivers, or a deal (private marketplace or programmatic guaranteed) is not spending as expected.
- **Action:** Walk the platform troubleshooting triage in order (status, budget and flight, bid and win rate, targeting size, inventory or deal, creative, tracking) using `dv360-troubleshooting` or the platform's troubleshooting skill and `dv360-deals-and-inventory` for deal-specific checks. Read the impression-loss breakdown to find the binding bucket. Use the `optimization-specialist` agent.
- **Verify:** The output names one binding cause supported by the impression-loss data or a status check, plus the specific fix. The triage was followed in order rather than guessing.
- **Stop:** Cause identified, with the fix awaiting approval. Clean no-op if delivery is healthy. Blocked if the data needed to diagnose is unavailable.
- **Guardrails:** Diagnose and recommend only. Any fix (bid, budget, targeting, deal, creative) requires approval. Do not broaden targeting or change a deal automatically. Re-read live status first.
- **Handoff:** The trader approves the fix, or the publisher or partner is contacted for a deal that is paused on the sell side.

Prompt:
> When a line item or deal is underdelivering, walk the troubleshooting triage in order and read the impression-loss breakdown to find the single binding cause, then recommend the specific fix. Diagnose only. Do not change bids, budgets, targeting, or deals. Stop when you have named the cause and fix for my approval, or report that delivery is healthy.
