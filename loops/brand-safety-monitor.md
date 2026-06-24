# Brand safety and quality monitor

Watch the quality signals for unsafe or low-value placements and propose exclusions, stopping once the review is complete.

- **Use when:** Daily or weekly, on viewability, invalid traffic, brand-safety flags, and placement quality.
- **Action:** Read viewability, invalid traffic, and any verification flags, and review the placement or domain and app report (`dv360-frequency-and-brand-safety`, the platform brand-safety and reporting skills). Identify placements that breach the safety or quality bar and propose exclusions. Use the `optimization-specialist` agent.
- **Verify:** Each proposed exclusion cites the placement, the breached signal, and the threshold it crossed. Placements within the bar are left in.
- **Stop:** Review complete with proposed exclusions awaiting approval. Clean no-op if everything is within the bar.
- **Guardrails:** Recommend only. Do not apply exclusions, change verification settings, or broaden targeting. Approval required before any exclusion is applied. A low viewability or quality reading is fixed through inventory and exclusions, not by raising the bid.
- **Handoff:** The trader approves and applies the exclusions.

Prompt:
> Review viewability, invalid traffic, verification flags, and the placement report against the agreed safety and quality bar, and propose exclusions for placements that breach it, each citing the signal and threshold. Recommend only; apply nothing and do not change verification settings or targeting. Stop when the review is complete, and hand the proposed exclusions to me for approval.
