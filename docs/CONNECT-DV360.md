# Connect your DV360 account and get real information

DV360 (Display & Video 360) is an enterprise platform. If you have a DV360 seat, because you
work at an advertiser or agency with access, here are the real ways to get live information into
the assistant, from the one that needs no setup to the one that needs engineering. If you do not
have a DV360 seat, none of these apply, because there is no consumer DV360 login. You would
start with a Google sales contact, not with this package.

In every path the assistant reads and recommends. It does not change your DV360 account. You do.

## Path 1: Export a report and hand it over (no setup, works today, any model)

This is what most people should do. It needs no credentials and no API.

1. In DV360, open Reporting. Run an Offline report or an Instant report for the campaign and date
   range you care about. The `dv360-reporting` and `reporting-by-campaign-goal` skills tell you
   which metrics and dimensions to pick for your goal.
2. Export it as CSV.
3. Give the CSV to your assistant and ask, for example, "read this DV360 report, tell me which
   line items are underpacing and why, and what you would change."

The skills do the rest: `dv360-reporting` reads the columns, `reporting-by-campaign-goal` judges
against the objective, and `dv360-pacing-and-optimization` and `dv360-troubleshooting` diagnose
and recommend. This works with any model, including a local one, because it is just a file plus
the skills.

## Path 2: Pull reports programmatically (bring your own API access)

For repeatable, scripted reporting, the package ships a read-only report puller that uses the
Bid Manager (DV360 reporting) API:
`skills/dv360-api-and-sdf-automation/scripts/dv360_report_puller.py`.

What you need (this is the real gate, and it is more than a login):

- A Google Cloud project with the **Display & Video 360 API** and the **Bid Manager API** enabled.
- A **service account** (or an OAuth client) in that project.
- That service account's email added as a **user in your DV360 account**, with a role that can run reports. DV360 API access is granted through your DV360 user, not a separate developer token.
- The OAuth scope `https://www.googleapis.com/auth/doubleclickbidmanager` for reporting. The entity API (campaigns, line items) uses a different scope, `display-video`.

Then:

```bash
pip install google-api-python-client google-auth google-auth-oauthlib
export GOOGLE_APPLICATION_CREDENTIALS=/secure/path/dv360-sa.json
python3 skills/dv360-api-and-sdf-automation/scripts/dv360_report_puller.py \
    --advertiser-id YOUR_ADVERTISER_ID \
    --start 2026-06-01 --end 2026-06-30 \
    --out report.csv
```

It creates a report query, runs it, waits, and downloads the CSV. Then feed the CSV to the
assistant as in Path 1. The `dv360-api-and-sdf-automation` skill explains the API model and what
is safe to automate: reporting is safe, and changes stay human-gated. Credentials live only in
your service-account key file, pointed at by an environment variable. Nothing goes in this
repository or in a prompt.

## Path 3: Conversational live data (a DV360 MCP server, advanced)

If you want the assistant to pull DV360 data on request inside the conversation, that needs a
DV360 MCP server. The honest state of this:

- There is **no official DV360 MCP server** today. Google Ads has an official read-only one (see [DEMO-GOOGLE-ADS.md](DEMO-GOOGLE-ADS.md)). DV360 does not.
- Community DV360 MCP servers exist but are early and low-adoption. If you use one, treat it as experimental, keep it read-only, and review its code, because it will hold your credentials.
- The access requirements are the same as Path 2: a Google Cloud project with the APIs enabled and a DV360 user with access.

Until an official server exists, Path 1 and Path 2 are the dependable ways to get real DV360
information into the assistant.

## The honest summary

- Most people: export a report from DV360 and give it to the assistant. No setup.
- Teams with engineering: use the bundled report puller with your own Google Cloud project and DV360 API access.
- Live conversational pulls: possible with a community MCP server today, officially supported not yet.

## Sources

- Display & Video 360 API: https://developers.google.com/display-video/api (as of June 2026)
- Bid Manager API (reporting): https://developers.google.com/bid-manager (as of June 2026)
- The `dv360-api-and-sdf-automation` and `dv360-reporting` skills cite the deeper verified pages.
