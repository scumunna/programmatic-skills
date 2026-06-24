# Pre-launch QA gate

Before a campaign goes live, run the launch checklist and an independent review, and return either a sign-off or a list of blockers, never a soft pass.

- **Use when:** A campaign is built and proposed for launch, before it serves.
- **Action:** Run the full pre-flight checklist with `dv360-launch-qa` (or the platform's setup and QA skill) using the `account-operations-specialist` agent. Then have the `qa-scrutinizer` agent independently review the same build against the checklist. Collect every failed or missing item.
- **Verify:** Two passes agree the build is correct and complete: the operations checklist and the independent scrutinizer review. The reviewer is not the builder.
- **Stop:** Success when both passes are clean; emit a sign-off. Blocked when any item fails; emit the itemized blocker list and return it to the trader. Never report a build with open blockers as ready.
- **Guardrails:** No launch without a clean sign-off from both passes. The scrutinizer reviews only and does not edit the build. Re-read the live build, not an earlier draft.
- **Handoff:** Go or no-go to the trader. On no-go, the trader fixes and re-runs the gate.

Prompt:
> Before this campaign launches, run the full pre-flight QA checklist, then have an independent reviewer check the same build against it. Return a sign-off only if both passes are clean. If anything fails, return the itemized blockers and do not approve launch. Review the live build, not an earlier draft. Do not edit the build; report only.
