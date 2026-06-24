# Video completion watch

Catch video and connected TV creatives whose completion is slipping and flag them, stopping once the active video is reviewed.

- **Use when:** In flight on video and connected TV campaigns.
- **Action:** Read video completion rate and cost per completed view over time, and the quartile drop-off (25, 50, 75, 100 percent), per creative and placement (`reporting-by-campaign-goal`, `dv360-youtube-and-video`, the platform reporting skill). Flag creatives or placements where completion is falling or the quartile drop-off is steep. Use the `optimization-specialist` agent.
- **Verify:** Each flag shows the completion-rate trend or the quartile curve against a stated threshold. Skippable and non-skippable formats are read on their own terms.
- **Stop:** Done when the active video is reviewed. Clean no-op if completion holds.
- **Guardrails:** Recommend only. Do not pause or swap creatives. A change requires approval. Tell a creative problem apart from a low-quality-placement problem before recommending.
- **Handoff:** The trader for a creative refresh, or [brand-safety-monitor](brand-safety-monitor.md) when the cause is placement quality.

Prompt:
> Review video and connected TV creatives for completion decay. For each creative and placement, read the completion rate over time and the quartile drop-off, and flag falling completion or steep drop-off against the agreed threshold. Read skippable and non-skippable on their own terms. Recommend only; change nothing. Stop when active video is reviewed, and tell me whether each flag is a creative problem or a placement-quality problem.
