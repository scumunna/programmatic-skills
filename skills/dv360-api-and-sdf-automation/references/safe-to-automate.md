# Safe-to-automate matrix and human-in-the-loop patterns

The hardest part of DV360 automation is not the API calls. It is deciding what an agent may do unattended against a live account that spends real money. This file is the rationale behind the matrix in the SKILL and the four patterns that keep automation safe.

## Principles

1. **Read freely, write carefully, never destroy.** Reading and alerting carry no account risk. Writes move money and reach. Deletion and archival are irreversible at the speed and scale a script operates.
2. **Reversibility sets the gate.** The easier a change is to undo cleanly, the lighter the gate. Pausing is reversible, so it can be conditional. Cross-campaign budget moves and deletes are hard to unwind, so they need a human or are off-limits.
3. **Bound every automated write.** A write the agent is allowed to make must have hard limits: maximum step size, maximum frequency, and a scope it cannot exceed. An unbounded "optimize" loop is how an account gets wrecked overnight.
4. **Log everything.** Every write must be traceable to a run, with the before and after values. If you cannot explain later why a change happened, the automation was not safe.
5. **Never decide on stale data.** See the data-freshness caveats. A fresh conversion reading is usually incomplete.

## The matrix, with rationale

| Action | Verdict | Why and what control |
| --- | --- | --- |
| Read and monitor entities, reports, pacing, delivery | Safe | No write, no account risk. Log reads. This is where most automation should live. |
| Bulk create from a validated template | Safe | New line items start in draft (`ENTITY_STATUS_DRAFT`), so nothing serves until a human activates. QA the draft, then activate by hand. |
| Guardrailed small bid change | Conditional | Allowed only within hard step-size and frequency caps, fully logged, behind an approval gate. A small, bounded, logged, approved nudge is fine; an open-ended auto-bidder is not. |
| Pause an underperformer | Conditional | Alert a human first. Pausing is reversible, so it can be automated with notification, but do not auto-resume: resuming is a judgment call about whether the underlying problem is fixed. |
| Broad targeting change | Conditional | Human approval. Targeting changes shift spend and reach and are hard to reverse cleanly once delivery has moved. |
| Cross-campaign budget reallocation | Conditional | Human approval. Moving budget between campaigns is a strategy decision a script cannot weigh. |
| Delete or archive | Never automate | Destructive and easy to get catastrophically wrong at scale. Do it by hand, deliberately. |

## The four human-in-the-loop patterns

### 1. Monitor and alert

The agent reads on a schedule, compares against thresholds, and raises an alert when something trips. It never writes. This is the safe default and the right home for most automation: pacing watch, delivery watch, win-rate and viewability watch, budget-burn watch. The human decides what to do; the agent just makes sure nothing is missed.

### 2. Guardrailed change with an approval gate

For a small bid adjustment, the agent computes a proposed change inside hard limits (for example no more than a small fixed percentage per step, no more than once per defined interval), writes the proposal and its rationale to a log or queue, and waits for a human to approve before it applies. The gate plus the caps mean the worst case is bounded and reviewed.

### 3. SDF bulk with a QA gate

The agent prepares the SDF, edits the CSV, and validates it against the format reference, producing a clear diff. A human reviews the diff and performs the upload in the UI. The agent then reads the result file to confirm what landed. The platform enforces this gate for you: SDF upload is UI-only, so the agent physically cannot perform the bulk write itself.

### 4. Staged custom-bidding rollout

For a new custom bidding algorithm or a new score, never flip it account-wide in one move. Roll it to a small slice of spend, run it against a control, watch the result over a matured data window, and only widen once it proves out. Stage up; do not jump. The scoring logic itself lives in the `dv360-custom-bidding` skill.

## Data-freshness caveats

- Do not auto-optimize on conversion data that is only a few hours old. View-through and offline conversions lag, so a fresh "no conversions" or "low conversions" reading is usually incomplete rather than real.
- Build alerts and changes around matured data windows, not the most recent hour.
- Require a signal to persist across more than one read before acting on it, so a single noisy data point does not trigger a change.

## Sources

- DV360 API release notes (v4, draft entity status, SDF v10): https://developers.google.com/display-video/api/release-notes
- DV360 API v4 advertisers.lineItems (entity status on create): https://developers.google.com/display-video/api/reference/rest/v4/advertisers.lineItems
- Structured Data Files overview (UI-only upload): https://developers.google.com/display-video/api/guides/concepts/structured-data-files/overview
