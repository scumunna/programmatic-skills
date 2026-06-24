# Google Ads API v24: resources, GAQL, mutates, auth, libraries

This is the field map for writing code against the Google Ads API. v24 is the current major version (v24.1 is the latest point release as of 2026-05-13). The Google Ads API is a single service that handles both reads (GAQL) and writes (mutates); there is no separate reporting service the way DV360 splits out Bid Manager.

This is a different API from the Display & Video 360 API. Different endpoint, different auth model (developer token plus OAuth, not a DV360 user role), different resources. See the `dv360-api-and-sdf-automation` skill for DV360.

## Access prerequisites

You need all three before the first call:

1. **A manager account (MCC).** The developer token is issued and managed in the API Center of a Google Ads manager account, not a client account. Place the manager account at the root of the hierarchy to simplify the token review.
2. **A developer token.** Sent on every call. Access levels:
   - **Test account access:** can call test accounts only. Assigned when an automatic review cannot complete.
   - **Explorer access:** can call production accounts with usage caps. Often granted by default.
   - **Basic and Standard access:** lift the restrictions after Google reviews and approves the application. Apply early; do not assume immediate Standard access.
3. **OAuth 2.0 credentials.** Authorize every call. See Authentication below.

## Authentication

The API supports the OAuth 2.0 flows Google supports generally. Two credential models matter:

- **Service account (server-to-server).** The right choice for unattended automation. Create a service account, download its JSON key, protect the key file, and add the service account email as a user on the Google Ads account it manages. The Google Ads service-account guide adds the service account directly as a Google Ads user; it does not require Google Workspace domain-wide delegation (this differs from the DV360 and several other Google APIs, so do not assume the delegation step applies here). The application runs the server-to-server OAuth flow using the key. No browser login.
- **User OAuth (installed app or web).** A human authorizes in the browser once and the application persists the refresh token. Use this for interactive tooling or to manage accounts on behalf of other users (multi-user authentication).

### The login-customer-id header

When you call against a client account through a manager, set the `login-customer-id` request header to the manager account ID (digits only, no dashes). This tells the API to authorize the request through the manager in the hierarchy. The operating customer ID (the account you are actually reading or changing) goes in the request path or body.

### Credential handling

Read the developer token, OAuth client ID and secret, and refresh token (or the service-account key path) from environment variables or a path the user supplies at runtime. Never hardcode any of them, and never commit a key file or token. Grant the OAuth user or service account the least Google Ads access role the automation needs.

## Official client libraries

Google officially supports client libraries in Java, .NET (C#), PHP, Python, Ruby, and Perl. Node.js and Go libraries exist but are community-maintained, not officially supported. Each library publishes a compatibility table mapping library versions to API versions (v24, v23, v22, v21 at time of writing). For Python:

```
pip install google-ads
```

The `google-ads` library wraps auth, the protobuf request and response types, and the services below. Configure it with a YAML file or environment variables holding the developer token, OAuth credentials, and optional `login_customer_id`.

## Reading with GAQL

The Google Ads Query Language is the read interface. It is read only and cannot mutate. Two methods on `GoogleAdsService` run a query:

- `SearchStream`: streams all matching rows in a single streamed response. Prefer it for large pulls; it avoids manual pagination.
- `Search`: returns rows in pages with a page token. Use it when you want page-by-page control or a bounded page size.

### GAQL clauses

- `SELECT` (required): the fields, segments, and metrics to return.
- `FROM` (required): exactly one resource. The resource determines which fields, segments, and metrics are selectable and how rows are shaped.
- `WHERE` (optional): filters. Operators include `=`, `!=`, `>`, `<`, `>=`, `<=`, `IN`, `NOT IN`, `LIKE`, `NOT LIKE`, `REGEXP_MATCH`, `CONTAINS ANY`, `DURING`, and `BETWEEN`.
- `ORDER BY` (optional): sort.
- `LIMIT` (optional): cap row count.
- `PARAMETERS` (optional): query-level options, for example `include_drafts`.

A report and an entity retrieval are the same mechanism: a report just selects metrics and segments. The queryable resource list (which fields, segments, and metrics each resource exposes) is the Reporting reference for v24. For report design and reading, see the `google-ads-reporting` skill.

### Example GAQL

```
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```

Cost is reported in micros (1,000,000 micros = one unit of account currency). Convert before presenting to a human. KPI math lives in `programmatic-foundations`.

## Writing with mutates

Writes never go through GAQL. They go through mutate operations:

- **Service-level mutates.** Each resource has a service with a mutate method, for example `CampaignService.MutateCampaigns`, `AdGroupService.MutateAdGroups`, `AdGroupAdService.MutateAdGroupAds`, `AdGroupCriterionService.MutateAdGroupCriteria`, `AssetService.MutateAssets`, `AssetGroupService.MutateAssetGroups`, `ConversionActionService.MutateConversionActions`. One resource type per call.
- **`GoogleAdsService.Mutate`.** A single endpoint that batches operations across multiple resource services in one atomic request. It supports temporary (negative) resource IDs so you can create a parent and its children in one call and reference the not-yet-created parent. The whole request succeeds or fails together.

### Safety properties

- **Atomicity.** A mutate request applies fully or not at all, so a failed bulk change does not leave half-built entities.
- **Cross-account block.** By default an account cannot mutate objects it did not create, unless it is the manager of the account that created them. This contains the blast radius of a misconfigured credential.
- **Create paused.** When you create campaigns, ad groups, or ads, create them paused and enable them only after QA. This is your built-in human gate for bulk creation.

## Core resources

The resources an automation touches most:

- `customer`: the account. Account creation, hierarchy, and account-level settings.
- `campaign`: the campaign. Type, status, budget link, bidding strategy.
- `ad_group`: ad group within a campaign (Search and Display).
- `ad_group_ad`: an ad inside an ad group.
- `ad_group_criterion`: targeting and bidding criteria on an ad group (keywords, audiences, and more).
- `asset`: a reusable creative asset (image, text, video, sitelink, and others).
- `asset_group`: the Performance Max grouping that replaces ad groups, ads, and keywords. Performance Max uses asset groups plus listing groups for retail, so its structure and mutates differ from Search and Display.
- `conversion_action`: a defined conversion action used for conversion tracking and bidding goals.

Each resource has a v24 field reference page listing its attributes, segments, and metrics, and whether it is queryable.

## Rate limits

The API meters requests with a token-bucket algorithm per developer token and per customer ID, so the exact QPS limit varies with server load. Over-limit requests are rejected with `RESOURCE_TEMPORARILY_EXHAUSTED`. To stay under limits: cap concurrent tasks, batch operations into single mutate calls, throttle client-side, and queue and spread load. Retry rejected requests with exponential backoff rather than tight retries.

## Sources

- Google Ads API release notes (v24 current; v24.1 latest 2026-05-13): https://developers.google.com/google-ads/api/docs/release-notes
- Get started: https://developers.google.com/google-ads/api/docs/start
- Obtain a developer token: https://developers.google.com/google-ads/api/docs/get-started/dev-token
- OAuth 2.0 overview: https://developers.google.com/google-ads/api/docs/oauth/overview
- Use a service account: https://developers.google.com/google-ads/api/docs/oauth/service-accounts
- Account management overview (manager accounts, login-customer-id): https://developers.google.com/google-ads/api/docs/account-management/overview
- GAQL overview: https://developers.google.com/google-ads/api/docs/query/overview
- GAQL grammar: https://developers.google.com/google-ads/api/docs/query/grammar
- Reporting overview (SearchStream and Search): https://developers.google.com/google-ads/api/docs/reporting/overview
- Reporting reference, queryable resources (v24): https://developers.google.com/google-ads/api/fields/v24/overview
- Mutating resources overview: https://developers.google.com/google-ads/api/docs/mutating/overview
- Performance Max overview: https://developers.google.com/google-ads/api/docs/performance-max/overview
- Rate limits: https://developers.google.com/google-ads/api/docs/best-practices/rate-limits
- Client libraries: https://developers.google.com/google-ads/api/docs/client-libs
