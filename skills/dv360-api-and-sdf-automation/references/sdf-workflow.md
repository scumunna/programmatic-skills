# Structured Data Files (SDF) v10 workflow

Structured Data Files are the bulk CSV interface to Display & Video 360. One file per resource type, a header row of column names, then one row per resource. v10 is the current version. SDF is the right tool for bulk create and edit and for YouTube and Demand Gen resources.

## Resource files

Standard-format SDF resource files:

- Campaigns
- Insertion Orders
- Inventory Sources
- Line Items
- Media Products
- YouTube Ad Groups
- YouTube Ads

QA-format variants exist for Line Items and YouTube Ad Groups. You pick the resource file that matches what you are creating or editing.

## File format rules

- The first row is always a header row of column names.
- Except for the header, non-empty string values are wrapped in quotation marks.
- Missing values are left blank.
- List values are separated by semicolons with a trailing semicolon. Nested lists use parentheses inside the semicolon-delimited list.
- You may upload a subset of supported columns. Smaller files with only the columns you are changing process faster and let you move more resources per upload. Include the identifier columns and the columns you are changing; omit the rest.

Always validate your file against the current SDF format reference before uploading, because exact column names and accepted values change between versions.

## Workflow

1. **Download the current SDF.** Two ways:
   - Through the UI (download for the entities you want).
   - Programmatically with the DV360 API `sdfdownloadtasks` resource: `create` a download task, poll `sdfdownloadtasks.operations.get` until it completes, then retrieve the file. This is download only.
2. **Edit the CSV locally.**
   - To update existing resources, change values in their rows.
   - To create resources, add new rows. New resources use a negative or placeholder ID convention per the format reference so the platform assigns real IDs on upload.
   - Remove rows you are not touching so the upload is small and fast.
3. **Upload through the UI.** SDF upload is UI-only. The API can download SDFs but cannot upload them. This is a deliberate guardrail: every bulk write passes through a human in the UI, which is the natural QA gate for SDF automation.
4. **Process and review the result file.** After the upload processes, read the result file. It reports which rows succeeded and which failed and why. Treat the result file as the source of truth for whether the bulk change actually landed; do not assume success.

## Where SDF fits versus the API

- Use the **API** for targeted, programmatic, single-entity or moderate bulk changes where you want full control in code and an audit trail per call, and for anything that must be unattended end to end (within the safe-to-automate limits).
- Use **SDF** for large spreadsheet-driven creates and edits, for changes a media trader will review as a diff, and for YouTube and Demand Gen resource management. The UI-only upload makes SDF inherently human-gated.

## Automation pattern for SDF

The safe pattern is the SDF bulk QA gate: a script downloads the SDF (UI or `sdfdownloadtasks`), builds the edited CSV, and validates it against the format reference; a human reviews the diff and performs the upload in the UI; then the script (or the human) reads the result file to confirm. The script never performs the write itself, because the platform does not expose an SDF upload API. See `safe-to-automate.md`.

## Sources

- Structured Data Files overview: https://developers.google.com/display-video/api/guides/concepts/structured-data-files/overview
- Structured Data Files format (v10): https://developers.google.com/display-video/api/structured-data-file/format
- DV360 API v4 sdfdownloadtasks: https://developers.google.com/display-video/api/reference/rest/v4/sdfdownloadtasks
- DV360 API release notes (SDF v10): https://developers.google.com/display-video/api/release-notes
