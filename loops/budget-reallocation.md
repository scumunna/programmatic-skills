# Budget reallocation

When spend efficiency diverges across line items, propose moving budget from the laggards to the leaders within a capped shift, and stop at a recommendation for approval.

- **Use when:** Spend efficiency (CPA, ROAS, or the campaign KPI) has clearly diverged across line items or campaigns under the same goal and budget pool.
- **Action:** Read current spend and KPI per line item (`reporting-by-campaign-goal`, the platform reporting skill). Rank by efficiency against the shared goal. Propose a reallocation that moves budget from the weakest to the strongest, sized within the cap, with the expected effect. Use the `optimization-specialist` agent.
- **Verify:** The proposal names the source and destination lines, the amount, and the expected KPI effect, and the math reconciles to the total budget. The lines compared share one goal and one budget pool.
- **Stop:** Proposal ready and awaiting approval. Clean no-op if efficiency is even or the data is too thin to separate winners from losers.
- **Guardrails:** Recommend only. No budget moves without approval. Never move budget across advertisers or clients. Cap any single shift at a pre-agreed share of the line's budget. Re-read current spend before proposing.
- **Handoff:** The trader approves and applies the reallocation.

Prompt:
> When spend efficiency diverges across line items in the same goal and budget pool, rank them by efficiency and propose moving budget from the weakest to the strongest, capped at the agreed share, with the expected KPI effect and reconciled math. Recommend only. Never move money across clients. Stop at a proposal for my approval, or report no action if efficiency is even.
