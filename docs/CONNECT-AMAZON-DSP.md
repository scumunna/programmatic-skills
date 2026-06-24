# Connect your Amazon DSP account and get real information

Amazon DSP is an enterprise platform. You connect a DSP seat (self-service or managed-service),
not a personal login. If you do not have Amazon DSP access, the answer is "talk to Amazon Ads,"
not this package. In every path the assistant reads and recommends. It does not change your
account.

## Path 1: Export a report and hand it over (no setup, any model)

1. In Amazon DSP, run a report for the campaign and dates you need. The
   `amazon-dsp-measurement-and-reporting` and `reporting-by-campaign-goal` skills tell you which
   metrics matter (impressions, detail page views, add to cart, purchases, ROAS, new to brand).
2. Export it.
3. Give it to your assistant and ask it to read the retail funnel and recommend.

No credentials, no API, works with any model.

## Path 2: The Amazon Ads API (bring your own access)

Amazon DSP is served by the Amazon Ads API. What you need:

- Apply for Amazon Ads API access (an application and approval process).
- Login with Amazon OAuth credentials and your advertiser profile.
- DSP campaign management and reporting are gated to accounts with DSP access, and some surfaces are managed-service only.

The `amazon-dsp-api-and-automation` skill explains the model and the safe-to-automate posture.
For event-level analysis, Amazon Marketing Cloud (the `amazon-marketing-cloud` skill) needs a
provisioned AMC instance.

## Path 3: Conversational live data (MCP)

- Amazon Ads has an **official** MCP server (open beta) that can read and, with an explicit flag, write. Its coverage is centered on Sponsored Ads and reporting. Confirm the current Amazon DSP coverage in the Amazon docs before relying on it.
- A community MCP server explicitly covers Amazon DSP. Treat community servers as experimental and keep them read-only.
- All of these need your own Amazon Ads API access.

## Honest summary

- Most people: export a report and feed it to the assistant.
- Teams with API access: the Amazon Ads API, plus AMC for event-level work.
- Conversational: an official MCP exists in beta (Sponsored-Ads-centric); DSP-specific coverage is maturing.

## Sources

- Amazon Ads API: https://advertising.amazon.com/API/docs (as of June 2026)
- Amazon Ads MCP server (official, open beta): https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta (as of June 2026)
