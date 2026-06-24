# Live demo: a read-only Google Ads report

This is the shortest path from "impressive knowledge base" to "it actually works." It connects
the assistant to a real Google Ads account, read-only, using the official open-source Google Ads
MCP server, and has it pull a real report. The skills in this repo tell the assistant which
report to build and how to read it. The MCP server fetches the live data. Nothing in the account
is changed.

## What you need

- A Google Ads account you can read.
- Google Ads API access: a developer token (this requires a one-time application to Google) and OAuth credentials. The official server reads these from a `google-ads.yaml` file with your `client_id`, `client_secret`, `refresh_token`, and `developer_token`, plus an optional `login_customer_id`.
- Python 3.12 with `pipx` (or `uv`).
- Never put these credentials in this repository or in a prompt. They live only in your local `google-ads.yaml`.

## Step 1: connect the official Google Ads MCP server (read-only)

Use the official server from Google's marketing-solutions team. It is read-only by default. The
mutation tools stay off unless you explicitly set an environment flag, which this demo does not.

Register it in your agent's MCP configuration:

```json
{
  "mcpServers": {
    "GoogleAds": {
      "command": "pipx",
      "args": ["run", "--spec", "git+https://github.com/google-marketing-solutions/google_ads_mcp.git", "run-mcp-server"],
      "env": { "GOOGLE_ADS_CREDENTIALS": "/absolute/path/to/google-ads.yaml" },
      "timeout": 30000,
      "trust": false
    }
  }
}
```

This exposes read-only tools: run a GAQL query, list the accounts you can access, and look up
reporting fields. The mutation tools (creating campaigns, budgets, ads) require setting
`ADS_MCP_ENABLE_MUTATIONS=true`, which this demo deliberately leaves unset, so the assistant can
read your account but cannot change it.

## Step 2: install these skills

Install the package (see the main README) so the assistant has the Google Ads playbooks. The
`google-ads-reporting` and `google-ads-api-and-bulk-operations` skills tell it which metrics and
GAQL to use, and `google-ads-optimization-and-troubleshooting` tells it how to read the result.

## Step 3: ask for a real report

With the server connected and the skills installed, ask in plain language. For example:

- "List the Google Ads accounts I can access."
- "Pull the last 30 days of campaign performance for account 123-456-7890: impressions, clicks, CTR, cost, conversions, and cost per conversion. Rank by cost."
- "Which campaigns are limited by budget right now, and which are limited by rank?"
- "Show me the search terms from the last 14 days that spent the most with no conversions."

The assistant uses the `google-ads-reporting` skill to choose the right metrics and write the
GAQL, calls the GoogleAds server's query tool to fetch the live data from your account, and uses
the optimization skill to read it back to you. It reads only, it recommends, and it changes
nothing.

## Why this is the demo that matters

Knowledge alone is a claim. A real report from a real account, pulled live and read correctly,
is proof. Keep it read-only, keep credentials out of the repository, and you have a
demonstration that holds up.

## Sources

- Google Ads MCP server (official, read-only by default), Google Marketing Solutions: https://github.com/google-marketing-solutions/google_ads_mcp (as of June 2026)
- Google Ads API access levels and developer token: https://developers.google.com/google-ads/api/docs/api-policy/access-levels (as of June 2026)
