# Connecting tools and platforms

The skills, agents, and loops in this repository are useful on their own: they make an agent
reason like a programmatic specialist. This guide is for when you want the agent to also read
live data from your accounts, and it explains where the safe line is for taking actions.

## The one rule: read and recommend, gate the spending

Automate reading and recommending. Put a human in front of anything that spends money or
changes a live campaign (budgets, bids, launch or pause, targeting). This is not caution for
its own sake. It is where the industry and the security guidance sit in 2026:

- The most advanced agent on a major DSP, The Trade Desk's Claude-powered Koa Agents, builds campaigns and troubleshoots but does no autonomous bidding and runs human-approved (Digiday, May 2026).
- OWASP's "Excessive Agency" guidance says to require human approval for high-impact actions, and spending money is the textbook example (OWASP LLM06, 2025).
- Practitioners in 2026 still call autonomous buying "not ready" for the large majority of campaigns.

So read-only tools can run freely. A write path, if you build one, is opt-in, off by default,
and always ends in a human clicking approve.

## Two ways to give an agent live data

### 1. Bundled scripts (bring your own credentials)

The read-only report pullers in this repo (DV360, Google Ads) run against your own account
with your own credentials, read from environment variables. They never change anything. This
is the simplest path and needs no extra software. See `tools/README.md`.

### 2. MCP servers (connect what already exists)

Model Context Protocol (MCP) servers let an agent call a platform's API as a set of tools. You
do not need to build these. Connect an existing one and have the skills here orchestrate it. In
a skill, reference an MCP tool by its fully qualified name, `ServerName:tool_name`, so the agent
finds it.

What exists today (verified, as of June 2026):

| Platform | MCP server | What it does | Notes |
| --- | --- | --- | --- |
| Google Ads | Official: github.com/google-marketing-solutions/google_ads_mcp | Read-only: run GAQL queries, list accounts | Cannot change bids, budgets, or campaigns by design |
| Amazon Ads (and DSP) | Official, open beta: the Amazon Ads MCP server on advertising.amazon.com | Read and write, including campaign creation | Beta. Needs active Amazon Ads API credentials. Treat writes as gated. |
| DV360 | Community, read-only (search GitHub for a DV360 MCP server) | Read campaigns and reports | Community-maintained, or use the bundled report puller |
| StackAdapt | Community, read-only | Read campaigns and delivery | Needs a request-only GraphQL token from your account manager |
| The Trade Desk | None public | API is partner-gated | No self-serve access. Use the skills as knowledge unless you hold partner API access. |

Anthropic does not ship ad-platform connectors itself. The platforms (Google, Amazon) publish
their own, listed in the public MCP registry.

For a concrete, read-only walkthrough that connects the official Google Ads server and pulls a
real report from your account, see [DEMO-GOOGLE-ADS.md](DEMO-GOOGLE-ADS.md).

## Credentials and security

- Never put credentials in this repository, in a skill, or in a prompt. Read them from environment variables or the MCP server's own configuration.
- Use scoped, short-lived credentials where the platform allows. A read-only token cannot move budget.
- Each platform's API needs its own access: Google Ads and Amazon require an application and approval; The Trade Desk and StackAdapt issue access through your account team. The skills describe each platform's model.

## If you do build a write path

Build it as "execute a change a human already approved," not "decide and act":

1. Off by default, behind an explicit opt-in.
2. Show a dry-run diff of exactly what will change.
3. Require a human confirmation before the change is sent.
4. Enforce hard budget caps and rate limits.
5. Log every action for audit.
6. Isolate any untrusted data the agent reads, since a report or a feed can carry hidden instructions (prompt injection).

## Where this is heading

The industry is standardizing agent-to-platform buying. The IAB Tech Lab published an Agentic
RTB Framework in late 2025 built on MCP and agent-to-agent communication. As official,
write-capable, well-governed servers mature, the safe surface for agent actions will grow.
Until then, this package keeps the agent advisory by default, which is both safer and, for now,
what the platforms themselves do.

## Sources

- Anthropic, Agent Skills (skills bundle scripts and orchestrate MCP tools): https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (as of June 2026)
- Anthropic, Code execution with MCP: https://www.anthropic.com/engineering/code-execution-with-mcp (as of June 2026)
- Google Ads API MCP server (official, read-only): https://github.com/google-marketing-solutions/google_ads_mcp (as of June 2026)
- Amazon Ads MCP server (official, open beta): https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta (as of June 2026)
- IAB Tech Lab, Agentic RTB Framework v1.0: https://iabtechlab.com/press-releases/iab-tech-lab-announces-agentic-rtb-framework-artf-v1-0-for-public-comment/ (as of June 2026)
- The Trade Desk Claude-powered Koa Agents (human-approved, no autonomous bidding): https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/ (as of June 2026)
- OWASP LLM06 Excessive Agency (human-in-the-loop for high-impact actions): https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ (as of June 2026)
