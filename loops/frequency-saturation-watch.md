# Frequency saturation watch

Find audiences being over-exposed (rising frequency, flattening reach) and flag a cap or a shift to fresh reach, stopping once the reach campaigns are reviewed.

- **Use when:** Periodically on reach and awareness campaigns, especially long flights and connected TV.
- **Action:** Read reach by frequency bucket (1+, 2+, 3+) and the frequency distribution against the effective-frequency band for the goal (`reach-and-frequency-planning`, the platform reporting and frequency skills). Flag campaigns where a large share of impressions land above the effective band (an over-exposed tail) while incremental reach has flattened. Account for co-viewing on connected TV, which inflates true per-person frequency. Use the `optimization-specialist` agent.
- **Verify:** Each flag shows the frequency distribution and the share of impressions above the effective band, not the average frequency alone.
- **Stop:** Done when the reach campaigns are reviewed. Clean no-op if frequency sits inside the band.
- **Guardrails:** Recommend only. Do not change frequency caps or budgets. A cap change requires approval. Read the distribution, never just the average.
- **Handoff:** The trader, who approves a tighter cap or a budget shift toward fresh reach.

Prompt:
> Review reach campaigns for frequency saturation. For each, read reach by frequency bucket and the distribution against the effective-frequency band for the goal, and flag any with a large over-exposed tail while incremental reach has flattened. Account for connected TV co-viewing. Show the distribution, not just the average. Recommend only; change nothing. Stop when the reach campaigns are reviewed, and hand flags to me for a cap or a shift to fresh reach.
