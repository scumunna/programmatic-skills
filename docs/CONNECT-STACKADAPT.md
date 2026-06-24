# Connect your StackAdapt account and get real information

StackAdapt is a self-serve, multi-channel DSP. You connect your StackAdapt account. In every
path the assistant reads and recommends. It does not change your account.

## Path 1: Export a report and hand it over (no setup, any model)

1. In StackAdapt, run a report or open the reporting dashboards for the campaign and dates you
   need. The `stackadapt-reporting-and-attribution` and `reporting-by-campaign-goal` skills tell
   you what to pull (impressions, clicks, conversions, CPA, ROAS, channel and audience splits).
2. Export it as CSV.
3. Give it to your assistant and ask it to read and recommend.

No credentials, no API, works with any model.

## Path 2: The StackAdapt GraphQL API (bring your own access)

StackAdapt exposes a GraphQL API. Access is **request-only**: you ask your StackAdapt account
manager for an API token, it is not a self-serve key. The `stackadapt-api-and-automation` skill
covers the model:

- The older REST reporting API is read-only and being retired. GraphQL is the path forward.
- Write access and some surfaces are tier-restricted, so confirm what your token allows.
- Once you have a token, pull reporting and campaign data programmatically and feed it to the assistant.

Keep the token in an environment variable, never in this repository or a prompt.

## Path 3: Conversational live data (MCP)

- There is **no official StackAdapt MCP server**. A community read-only MCP exists but is early. Treat it as experimental and keep it read-only.
- It needs the same request-only GraphQL token from your account manager.

## Honest summary

- Most people: export a report and feed it to the assistant.
- Teams: the GraphQL API, with a token your account manager issues.
- Conversational: community MCP only, and early.

## Sources

- StackAdapt developer and API documentation: https://docs.stackadapt.com (as of June 2026)
- The `stackadapt-api-and-automation` and `stackadapt-reporting-and-attribution` skills cite the deeper pages.
