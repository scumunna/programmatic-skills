# Weekly client report

Turn the week's performance into a clear, honest client update, passed through an independent accuracy review before it is sent, stopping when the review is clean.

- **Use when:** Weekly, or on the client's reporting cadence.
- **Action:** Pull the goal-appropriate report and the so-what (`reporting-by-campaign-goal`, the platform reporting and measurement skills) with the `reporting-analyst` agent. Draft the client-facing update with the `client-communications-lead` agent: headline against the objective, the few numbers that matter, the so-what, and the next step. Then have the `qa-scrutinizer` agent review it for math, attribution validity, overclaiming, and tone.
- **Verify:** The scrutinizer confirms every number is sourced to a report, no assist is presented as an incremental conversion, no correlation is stated as cause, and the headline matches the objective. Independent reviewer, not the author.
- **Stop:** Ready to send once the review is clean. Loop once to fix issues the reviewer raises, then re-review. Blocked if the underlying numbers are missing.
- **Guardrails:** Do not send the report. External delivery requires human approval. No number without a source. No em dashes in the client text.
- **Handoff:** The human sends the approved report to the client.

Prompt:
> Weekly, pull the report for each campaign's goal, draft a client update (headline against the objective, the few numbers that matter, the so-what, the next step), then have it independently reviewed for math, attribution validity, overclaiming, and tone. Every number must cite a report. Fix what the review raises and re-review. Do not send it. Stop at a clean, ready-to-send draft for my approval.
