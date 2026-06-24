# Creative fatigue watch

Find creatives whose response is decaying as frequency climbs and flag them for refresh, stopping once every active creative has been checked.

- **Use when:** Periodically in flight, especially on longer campaigns where the same users see the same creative repeatedly.
- **Action:** For each active creative, read frequency alongside CTR and conversion rate over time (`reporting-by-campaign-goal`, the platform reporting and frequency skills). Flag creatives where frequency is rising while response is falling past a set threshold. Use the `optimization-specialist` agent.
- **Verify:** Each flag shows the trend, the frequency, and the response decline against a stated threshold, not a hunch. Creatives still performing are left alone.
- **Stop:** Done when all active creatives are reviewed. Clean no-op if none are fatigued.
- **Guardrails:** Recommend only. Do not pause creatives or upload replacements. A creative swap requires approval and trafficking by a person. Read current period data.
- **Handoff:** The trader, who approves a refresh and traffics new creative.

Prompt:
> Review each active creative for fatigue: flag any where frequency is rising while CTR or conversion rate falls past the agreed threshold, showing the trend. Leave performing creatives alone. Recommend only. Do not pause or replace anything. Stop when all active creatives are reviewed, and hand flagged ones to me for a refresh.
