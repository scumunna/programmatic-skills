# Safe-to-automate matrix and human-in-the-loop patterns

The hardest part of Google Ads automation is not the API calls. It is deciding what an agent may do unattended against a live account that spends real money. This file is the rationale behind the matrix in the SKILL and the four patterns that keep automation safe. It applies to anything that can write to the account: the API, Google Ads scripts, scheduled jobs, or a bulk upload pipeline.

## Principles

1. **Read freely, write carefully, never destroy.** Reading and alerting carry no account risk. Writes move money and reach. Removal is irreversible at the speed and scale a script operates.
2. **Reversibility sets the gate.** The easier a change is to undo cleanly, the lighter the gate. Pausing is reversible, so it can be conditional. Cross-account budget moves and removals are hard to unwind, so they need a human or are off-limits.
3. **Bound every automated write.** A write the agent is allowed to make must have hard limits: maximum step size, maximum frequency, and a scope it cannot exceed. An unbounded "optimize" loop is how an account gets wrecked overnight, and a budget script with no cap can spend real money fast.
4. **Log everything.** Every mutate must be traceable to a run, with before and after values. If you cannot explain later why a change happened, the automation was not safe.
5. **Never decide on stale data.** See the data-freshness caveats. A fresh conversion reading is usually incomplete.

## The matrix, with rationale

| Action | Verdict | Why and what control |
| --- | --- | --- |
| Read and monitor (GAQL pulls, reports, spend, pacing, disapprovals) | Safe | No write, no account risk. Log reads. This is where most automation should live. |
| Bulk create from a validated template | Safe | Create campaigns, ad groups, and ads paused, so nothing serves until a human enables it. QA the entities, then enable by hand. |
| Guardrailed bid change | Conditional | Allowed only within hard step-size and frequency caps, fully logged, behind an approval gate. A small, bounded, logged, approved nudge is fine; an open-ended auto-bidder is not. |
| Guardrailed budget change | Conditional | Same caps and gate as bids. Budgets translate directly into spend, so a runaway budget write is among the most expensive mistakes a script can make. |
| Pause an underperformer | Conditional | Alert a human first. Pausing is reversible, so it can be automated with notification, but do not auto-resume: resuming is a judgment call about whether the underlying problem is fixed. |
| Add or change keywords, audiences, or other criteria | Conditional | Human approval. Criteria changes shift spend and reach and are hard to reverse cleanly once delivery has moved. |
| Performance Max asset or asset-group change | Conditional | Extra care and human approval. Asset edits can reset learning and reshape where spend goes across channels, with less direct visibility than Search. |
| Cross-account or cross-campaign budget reallocation | Conditional | Human approval. Moving budget is a strategy decision a script cannot weigh. |
| Remove or permanently delete anything | Never automate | Destructive and easy to get catastrophically wrong at scale. Do it by hand, deliberately. |

## The four human-in-the-loop patterns

### 1. Monitor and alert

The agent runs GAQL on a schedule, compares against thresholds, and raises an alert when something trips. It never writes. This is the safe default and the right home for most automation: spend-pace watch, conversion-stall watch, disapproval watch, impression-share-loss watch. The human decides what to do; the agent just makes sure nothing is missed.

### 2. Guardrailed change with an approval gate

For a small bid or budget adjustment, the agent computes a proposed change inside hard limits (for example no more than a small fixed percentage per step, no more than once per defined interval), writes the proposal and its rationale to a log or queue, and waits for a human to approve before it sends the mutate. The gate plus the caps mean the worst case is bounded and reviewed.

### 3. Bulk with a QA gate

The agent prepares a bulk create or edit (through the API, a script, or a bulk-upload sheet) and validates it, producing a clear diff. New campaigns, ad groups, and ads are created paused. A human reviews the diff and enables the entities only after QA. The paused-on-create default does the gating: nothing serves until a person turns it on.

### 4. Staged rollout

For a new automated change, never flip it account-wide in one move. Roll it to a small slice (one campaign, one ad group), run it against the rest as a control, watch the result over a matured data window, and only widen once it proves out. Stage up; do not jump. This is especially important for bidding, budget, and Performance Max asset changes, where learning periods mean the early signal is noisy.

## Data-freshness caveats

- Do not auto-optimize on conversion data that is only a few hours old. Some conversions import on a delay and attribution windows can be long, so a fresh "no conversions" or "low conversions" reading is usually incomplete rather than real.
- Recent reporting windows are estimates that settle later. Build alerts and changes around matured windows, not the most recent hour.
- Require a signal to persist across more than one read before acting on it, so a single noisy data point does not trigger a change.

## Sources

- Mutating resources overview (atomic mutates, cross-account block): https://developers.google.com/google-ads/api/docs/mutating/overview
- Rate limits (token bucket, RESOURCE_TEMPORARILY_EXHAUSTED, backoff): https://developers.google.com/google-ads/api/docs/best-practices/rate-limits
- Using scripts to make automated changes (scheduled writes): https://support.google.com/google-ads/answer/188712
- Performance Max overview (asset groups, learning): https://developers.google.com/google-ads/api/docs/performance-max/overview
