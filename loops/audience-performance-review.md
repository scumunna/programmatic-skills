# Audience performance review

Review how audiences and segments are performing and propose pruning the weak and scaling the strong, stopping once the segments have been reviewed.

- **Use when:** Weekly, on audience and segment performance.
- **Action:** Read performance by audience and segment against the goal (`reporting-by-campaign-goal`, the platform reporting and targeting skills). Identify segments to prune for waste and segments to scale for strength, each with the supporting metrics. Use the `optimization-specialist` agent. Mind overlap and recency so a prune does not cut a segment that assists conversions.
- **Verify:** Each prune or scale recommendation cites the segment, its spend, and its performance against the goal. Assisted contribution is considered before cutting an upper-funnel segment ([path-to-conversion-analysis](../skills/path-to-conversion-analysis)).
- **Stop:** Recommendations ready for approval. Clean no-op if performance is even or the data is too thin.
- **Guardrails:** Recommend only. Do not add, remove, or resize audiences. Approval required. Do not cut a segment on last-click alone if it carries assists.
- **Handoff:** The trader approves and applies the audience changes.

Prompt:
> Weekly, review performance by audience and segment against the goal and propose which to prune and which to scale, each justified by spend and performance. Check assisted contribution before cutting an upper-funnel segment. Recommend only; change no audiences. Stop when the segments are reviewed, and hand the proposals to me for approval.
