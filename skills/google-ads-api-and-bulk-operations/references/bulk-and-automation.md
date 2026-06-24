# Bulk and automation surfaces: Editor, scripts, bulk uploads

Three surfaces handle bulk and automation work outside the API. This file is the decision logic for picking among them and what each can and cannot do. For the API itself, see `api-resources.md`. For what is safe to let any of these do unattended, see `safe-to-automate.md`.

## Quick pick

| You want to | Use | Why |
| --- | --- | --- |
| Restructure an account by hand, reviewing everything before it goes live | Google Ads Editor | Offline desktop bulk editing with full review before posting. |
| Run recurring in-account logic on a schedule, possibly using an external feed | Google Ads scripts | JavaScript on a schedule, reads and writes the account, can pull external data. |
| Apply one large change from a spreadsheet, without writing code | Bulk uploads | Edit a template sheet offline, upload once. |
| Build a system, integration, or unattended agent | Google Ads API | Full programmatic control. See `api-resources.md`. |

## Google Ads Editor

A free, downloadable desktop application for managing campaigns. The workflow is: download one or more accounts, make changes offline, then post the changes back to Google Ads.

Strengths:

- Bulk editing tools: multi-select edits, find and replace, copy and paste across campaigns and accounts, advanced bulk operations.
- Work fully offline and review every change before it posts.
- Manage and edit multiple accounts in one place.
- Export and import files to share proposals or move changes between accounts.

Best for a human doing heavy manual surgery on structure who wants to see and approve everything before it goes live. It is not an automation surface: a person drives it. It runs on the desktop (64-bit Windows or recent macOS per the current system requirements), so it is not where unattended logic lives.

## Google Ads scripts

JavaScript entered in a browser-based editor that runs on Google's infrastructure, not on your machine and not as code living inside the account's serving logic. Scripts read and change the account through search and mutate calls, and most Google Ads features are reachable this way.

Strengths:

- Automate in-account tasks: change bids, pause ad groups, add keywords, generate reports, and more.
- Use data from external sources to drive changes, for example an external conversion feed to adjust bids, or an inventory feed to pause and unpause based on stock.
- Schedule a script to run once, daily, weekly, or monthly at a set hour, with no active user session.
- Logging and a script library to start from.

Best for recurring in-account logic that does not justify a full external integration. Because scripts can write to the account on a schedule, treat them like any other automated write: apply the safe-to-automate matrix, bound every change, and gate or alert on writes that move money or reach. Time limits apply to a single execution, so design long jobs to chunk work across runs.

Scripts versus the API: scripts are quickest for self-contained in-account automation with light infrastructure. The API is the choice when you need a real application, cross-system integration, tighter control, or to operate at a scale and reliability scripts do not target.

## Bulk uploads (sheets)

Download a spreadsheet template, edit it offline, and upload it to apply many changes at once. Templates exist for common jobs: campaign settings (budgets, names, languages, dates, status), assets (sitelinks, calls, callouts, images), keywords and audiences, responsive search and display ads, and location targeting.

Best for a one-time, large, sheet-driven change by someone who does not write code. It is a manual surface: a person prepares and uploads the sheet. It is not scheduled automation. For recurring logic, use scripts or the API; for heavy interactive restructuring, use Editor.

## How these relate to "bulk edits" overall

Google Ads groups several things under bulk management: direct in-interface bulk edits (select many items and change them), bulk uploads (the sheet workflow above), Google Ads Editor, and the automation tools (the API and scripts). The first three are manual, human-driven surfaces. The API and scripts are the automated ones and carry the most risk, so they need the guardrails in `safe-to-automate.md`.

## Sources

- About Google Ads Editor: https://support.google.com/google-ads/editor/answer/2484521
- Google Ads scripts (developer docs): https://developers.google.com/google-ads/scripts
- Using scripts to make automated changes: https://support.google.com/google-ads/answer/188712
- Bulk edits (definition and tools): https://support.google.com/google-ads/answer/144560
