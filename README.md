# Programmatic Trader Skills

A library of agent skills that let an AI assistant work as a programmatic **trader**,
**analyst**, and **account-operations** specialist. The first complete platform is Google
**Display & Video 360 (DV360)**. The foundations are DSP-agnostic, so the same library
extends to other demand-side platforms over time.

These skills encode researched, source-cited best practices: how to structure a campaign,
choose a bid strategy, manage pacing and budgets, set up deals and brand safety, pull and
read reports, run measurement and attribution, QA an account, and troubleshoot delivery.
They work in **Claude Code** and **Codex** from a single skills tree, and in Copilot CLI and
Gemini CLI through the shared skills path.

## Who this is for

Programmatic traders, ad ops specialists, and analysts who want an agent that already knows
the platform, and anyone learning DV360 who wants the decision rules an experienced trader
applies. The skills assume working knowledge of programmatic media. Shared definitions and
KPI math live in the `programmatic-foundations` skill.

## What is in the box

A growing library of agent skills across three jobs, plus shared foundations and reporting,
and specialist agents that chain those skills into a full workflow. DV360 is the first
platform and more demand-side platforms are being added.

| Skill | Job | What it does |
| --- | --- | --- |
| `programmatic-foundations` | Shared | Glossary, auction and KPI math, funnel model, the trader, analyst, and ops mental model. |
| `dv360-campaign-architecture` | Trading | Partner to advertiser to campaign to insertion order to line item structure, and when to split. |
| `dv360-bid-strategy` | Trading | Fixed, automated, and custom bidding. Target CPA, CPM, ROAS. Learning periods and pitfalls. |
| `dv360-targeting-and-audiences` | Trading | First-party and Google audiences, combination logic, geo, device, contextual, viewability and IVT. |
| `dv360-deals-and-inventory` | Trading | Open auction, PMP, Programmatic Guaranteed, Preferred Deals. Activation and non-delivery fixes. |
| `dv360-frequency-and-brand-safety` | Trading | Frequency caps, content and publisher exclusions, DoubleVerify and IAS, viewability standards. |
| `dv360-pacing-and-optimization` | Trading | Pacing modes, pacing math, under and over-delivery fix trees, impression loss diagnosis. |
| `dv360-reporting` | Analytics | Offline vs instant reporting, report types, the metric and dimension glossary, scheduling. |
| `dv360-measurement-and-attribution` | Analytics | Floodlight, Campaign Manager 360, attribution models, Brand Lift, reach and frequency. |
| `dv360-advanced-analytics-adh` | Analytics | Ads Data Hub, privacy checks, BigQuery Data Transfer, joining first-party data. |
| `dv360-custom-bidding` | Analytics | Rule-based, script, and Ads Data Hub custom bidding. Scoring, attribution, staged rollout. |
| `reporting-by-campaign-goal` | Analytics (cross-DSP) | State-of-the-art report recipes per objective: awareness, consideration, conversion, retention, reach planning. |
| `path-to-conversion-analysis` | Analytics (cross-DSP) | Multi-touch paths: touchpoints to convert, time lag, top paths, assisted conversions, via CM360, GA4, Ads Data Hub. |
| `dv360-account-setup-and-taxonomy` | Ops | Partner and advertiser setup, naming conventions, roles and permissions, governance. |
| `dv360-launch-qa` | Ops | Pre-flight QA checklist and sign-off workflow before any campaign goes live. |
| `dv360-troubleshooting` | Ops | Ordered playbooks for no delivery, pacing, win rate, viewability, creatives, conversions. |
| `dv360-api-and-sdf-automation` | Ops | DV360 API v4 resources, Structured Data Files v10, and a safe-to-automate matrix. |

## Specialist agents

The package also ships specialist agents that use the skills above to run a full workflow.
Installed with the plugin they are auto-discovered, and you can call one by name.

| Agent | Role |
| --- | --- |
| `media-planner` | Turns a brief into a media plan: objective, KPI, audience, inventory, budget, and measurement. |
| `programmatic-trader` | Builds the campaign from the plan: structure, bidding, targeting, deals, frequency, pacing. |
| `optimization-specialist` | Optimizes and troubleshoots in flight, one lever at a time, with expected impact. |
| `account-operations-specialist` | Sets up the account, enforces taxonomy, runs launch QA, and handles safe bulk operations. |
| `reporting-analyst` | Builds the right report per goal and runs measurement, attribution, and path to conversion. |
| `client-communications-lead` | Translates results into clear, honest, client-ready communication. |
| `qa-scrutinizer` | Independent reviewer that scores and gates builds, reports, and client comms before they ship. |

A typical flow: `media-planner`, then `account-operations-specialist` to set up, then
`programmatic-trader` to build, then `optimization-specialist` in flight, then
`reporting-analyst` and `client-communications-lead` to report, with `qa-scrutinizer`
reviewing at each gate.

## Install

### Claude Code (plugin marketplace)

```
/plugin marketplace add scumunna/programmatic-skills
/plugin install programmatic-skills
```

### Codex

Add the repository as a plugin source. Codex reads `.codex-plugin/plugin.json`, which points
at the shared `skills/` directory.

### Any runtime (manual)

Clone the repo and run the installer. It symlinks each skill into the runtime skills
directories so a `git pull` keeps them current.

```
git clone https://github.com/scumunna/programmatic-skills.git
cd programmatic-skills
./install.sh            # symlink skills and agents into the runtime directories
./install.sh --copy     # copy instead of symlink
```

`~/.agents/skills` is the shared path read by Codex, Copilot CLI, and Gemini CLI, so a single
install covers all of them. Agents are symlinked into `~/.claude/agents` and `~/.codex/agents`.
The plugin marketplace install is the simplest way to get both skills and agents in every
runtime.

## Using the skills

Talk to your agent normally. Skills activate when your request matches what a skill covers,
for example "structure a DV360 prospecting campaign for three markets" or "my line item is
underpacing, what do I check". Each skill carries the decision rules, checklists, and
templates the agent needs to respond like a practitioner.

## Optional scripts

Some skills ship runnable Python helpers (a report puller, a Structured Data File template, a
pacing calculator). They are optional. Each reads credentials from environment variables or a
path you supply, and prints usage when run with no arguments. The playbooks are useful on
their own even if you never run a script.

## Multi-DSP roadmap

The structure is built for more platforms. Cross-platform concepts live in
`programmatic-foundations`. A new platform is added as its own prefixed set of skills, for
example `ttd-*` for The Trade Desk or `amzn-*` for Amazon DSP, without restructuring. See
`CONTRIBUTING.md` for the recipe.

## Validate

```
python3 scripts/validate_skills.py
```

This checks every skill and agent: frontmatter, naming, description length, the no-em-dash
writing standard, that reference links resolve, and that each agent only references skills
that exist.

## Disclaimer

This is an independent, unofficial project. It is not affiliated with, endorsed by, or
sponsored by Google. Display & Video 360, DV360, Campaign Manager 360, and Ads Data Hub are
trademarks of Google LLC. Platform behavior changes over time. Verify against the current
official documentation before acting on a live account.

## License

MIT. See `LICENSE`.
