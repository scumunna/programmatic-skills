# Cross-platform workflows

How the three layers in this repository fit together:

- **Skills** are the knowledge: how each platform and each task works. They are grouped by platform (DV360, Google Ads, Amazon DSP, StackAdapt, The Trade Desk) plus shared foundations and reporting.
- **Agents** are the roles: a media planner, a trader, an optimization specialist, an account-operations specialist, a reporting analyst, a client-communications lead, and a QA scrutinizer. Each agent uses the skills and hands off to the next.
- **Loops** are the recurring cycles: bounded routines, run on demand or on a schedule, that monitor and recommend.

The point is one workflow that works across every platform. The agents and loops stay the same. Only the platform skill set changes.

## Workflow 1: Launch a campaign

1. `media-planner` turns the brief into a plan (objective, KPI, audience, inventory, budget, measurement), using `reporting-by-campaign-goal` and the platform's targeting and inventory skills.
2. `account-operations-specialist` stands up the account and the taxonomy.
3. `programmatic-trader` builds the campaign from the plan with the platform's structure, bidding, targeting, deals, and pacing skills.
4. The [pre-launch-qa-gate](loops/pre-launch-qa-gate.md) loop runs: `account-operations-specialist` checks the build against the launch QA skill, and `qa-scrutinizer` independently reviews it. Launch only on a clean sign-off.

## Workflow 2: Run a campaign in flight

1. The [daily-pacing-sweep](loops/daily-pacing-sweep.md) and [anomaly-detection](loops/anomaly-detection.md) loops watch delivery and the core metrics and surface what needs attention.
2. The [weekly-optimization-pass](loops/weekly-optimization-pass.md) loop has `optimization-specialist` diagnose the one binding constraint and propose a single change with its expected impact.
3. `qa-scrutinizer` reviews the recommendation, then the trader approves and applies it. One lever at a time, verified the next cycle.
4. [delivery-and-deal-watch](loops/delivery-and-deal-watch.md), [creative-fatigue-watch](loops/creative-fatigue-watch.md), [brand-safety-monitor](loops/brand-safety-monitor.md), [budget-reallocation](loops/budget-reallocation.md), [search-term-mining](loops/search-term-mining.md), and [audience-performance-review](loops/audience-performance-review.md) run as the situation calls for them, each ending in a recommendation for approval.

## Workflow 3: Report and communicate

1. The [weekly-client-report](loops/weekly-client-report.md) loop has `reporting-analyst` pull the goal-appropriate report and the so-what, `client-communications-lead` draft the update, and `qa-scrutinizer` review it for accuracy and overclaiming before a human sends it.
2. Ahead of a monthly or quarterly review, the [business-review-prep](loops/business-review-prep.md) loop assembles the period's results and the path to conversion, reviewed before it reaches the client.

## Workflow 4: Add or switch platforms

The same four roles and the same loops run on any platform. To move a campaign from one demand-side platform to another, swap the platform skill set the agents draw on:

- DV360: the `dv360-*` skills.
- Google Ads: the `google-ads-*` skills.
- Amazon DSP: the `amazon-dsp-*` and `amazon-marketing-cloud` skills.
- StackAdapt: the `stackadapt-*` skills.
- The Trade Desk: the `ttd-*` skills.

The shared foundations, the `reporting-by-campaign-goal` and `path-to-conversion-analysis` skills, the agents, and the loops do not change. That is what makes this a multi-platform operating system rather than five separate playbooks.
