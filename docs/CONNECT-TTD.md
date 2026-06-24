# Connect your The Trade Desk account and get real information

The Trade Desk is an enterprise, partner-gated platform, and it is the most gated of the
platforms in this package, so this guide is blunt about it. You connect a TTD seat. In every
path the assistant reads and recommends. It does not change your account.

## Path 1: Export a report and hand it over (no setup, any model)

This is the dependable path for almost everyone.

1. In The Trade Desk, run a report (the platform's reporting, including the MyReports and
   scheduled report exports) for the campaign and dates you need. The
   `ttd-measurement-and-reporting` and `reporting-by-campaign-goal` skills tell you what to read.
2. Export it.
3. Give it to your assistant and ask it to read and recommend.

No credentials, no API, works with any model.

## Path 2: The Trade Desk API (partner-gated)

The TTD API is closed partner infrastructure. There is no self-serve key, and the documentation
sits behind the partner portal. Access is provisioned by your TTD account team, usually under a
commercial arrangement. If your organization holds a provisioned partner API entitlement, the
`ttd-api-and-automation` skill covers the model and the safe-to-automate posture. If it does not,
this path is simply not open to you, and Path 1 is the answer.

## Path 3: Conversational live data (MCP)

- There is **no official TTD MCP server**, and no realistic public path, because the API itself is partner-gated. Any community wrapper still depends on a partner API entitlement you must already hold.
- Note for context: The Trade Desk's own Claude-powered Koa Agents build and troubleshoot campaigns inside the platform, human-approved, with no autonomous bidding. That is TTD's first-party agent, not a connector you install.

## Honest summary

- The Trade Desk is the most gated platform here. For almost everyone, export a report and feed it to the assistant.
- API and conversational access require a provisioned TTD partner entitlement, which is a commercial arrangement, not a sign-up.

## Sources

- The Trade Desk partner portal and API (gated): https://partner.thetradedesk.com (as of June 2026)
- The Trade Desk Claude-powered Koa Agents (human-approved, no autonomous bidding): https://digiday.com/media-buying/inside-the-trade-desks-claude-powered-campaign-agent/ (as of June 2026)
- The `ttd-*` skills are written at the public-concept level, because deeper details sit behind the partner login.
