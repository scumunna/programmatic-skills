# DV360 API v4 and Bid Manager API: resources, auth, libraries

This is the field map for writing code against the two APIs. v4 is the current, generally available version of the Display & Video 360 API. The Bid Manager (reporting) API is a separate service at v2.

## Service endpoints

- Display & Video 360 API: `https://displayvideo.googleapis.com`.
- Bid Manager API: `https://doubleclickbidmanager.googleapis.com`.

These are distinct services with distinct scopes. A DV360 API token does not authorize Bid Manager calls and vice versa.

## Authentication

Both APIs use OAuth 2.0. Two credential models:

- **Service account (server-to-server).** The right choice for unattended automation. Steps: create a service account in the Google API console, generate a JSON key, protect the key file, and associate the service account email with a DV360 user that holds the role the automation needs. The application runs the server-to-server OAuth flow using the key. No browser login.
- **User OAuth (installed application).** A human authorizes in the browser the first time and the script persists the refresh token for later runs. Suitable for local interactive tooling.

### Scopes

- `https://www.googleapis.com/auth/display-video`: read and write access to DV360 API entities.
- `https://www.googleapis.com/auth/display-video-user-management`: read and write access for user management (service-account user administration).
- `https://www.googleapis.com/auth/doubleclickbidmanager`: the Bid Manager (reporting) API.

### Credential handling

Read the key path or contents from an environment variable (for example `GOOGLE_APPLICATION_CREDENTIALS` pointing at the JSON key) or a path the user supplies at runtime. Never hardcode a key, and never commit a key file. Grant the least role the automation needs.

## Official client libraries

Google publishes client libraries for the DV360 API in .NET, Java, JavaScript, Objective-C, PHP, Python, Go, Node.js, and Ruby. The developer guides show snippets in Java, Python, and PHP. For Python, the common stack is the Google API Python client plus Google auth:

```
pip install google-api-python-client google-auth google-auth-oauthlib
```

The Bid Manager API has its own examples and uses the same Python client stack.

## DV360 API v4 resource map

Top-level resource collections (service root `displayvideo.googleapis.com`):

- `advertisers` and nested: `advertisers.campaigns`, `advertisers.insertionOrders`, `advertisers.lineItems`, `advertisers.creatives`, `advertisers.channels`, `advertisers.locationLists`, `advertisers.negativeKeywordLists`, `advertisers.assets`, `advertisers.invoices`, and the Demand Gen ad-group and ad resources.
- `partners`.
- `customBiddingAlgorithms`.
- `inventorySources` and `inventorySourceGroups`.
- `guaranteedOrders`.
- Audience resources: `firstPartyAndPartnerAudiences`, `googleAudiences`, `combinedAudiences`, `customLists`.
- `floodlightGroups`.
- `targetingTypes.targetingOptions` (the catalog of targeting options) and the per-entity assigned-targeting subresources.
- `sdfdownloadtasks` (and `sdfdownloadtasks.operations`).
- `media`, `users`.

### Resource hierarchy

Advertiser then campaign then insertion order then line item. Targeting is attached as assigned targeting options at the line item level (and at higher levels where supported). Creatives, custom bidding algorithms, inventory sources, and guaranteed orders associate at the advertiser or partner level.

### Key methods you will use

- `advertisers.lineItems`: `get`, `list`, `create`, `patch`, `delete`, `duplicate`, `bulkUpdate`, `bulkEditAssignedTargetingOptions`, `bulkListAssignedTargetingOptions`. A created line item must start in `ENTITY_STATUS_DRAFT`, which is the built-in safety gate for bulk creation.
- `advertisers.insertionOrders`: `get`, `list`, `create`, `patch`, `delete`.
- `advertisers.creatives`: create and manage creatives.
- `customBiddingAlgorithms`: manage custom bidding algorithms and scripts (scoring logic lives in the `dv360-custom-bidding` skill).
- `inventorySources`: read and manage inventory sources and deals.
- `sdfdownloadtasks`: `create` an SDF download task, then poll `sdfdownloadtasks.operations.get` for completion. Produces an SDF in a supported version (v10 and recent v9.x versions). Upload of the edited SDF is not part of the API; it is UI-only.

Use the bulk methods rather than looping single calls when changing many line items or their targeting. It is faster and stays within quota more comfortably.

## Bid Manager API v2 (reporting)

The reporting API manages `queries` and retrieves `queries.reports` metadata. Workflow:

1. `queries.create` (POST to `/v2/queries`) with a `Query` body that defines metrics, dimensions, date range, filters, and an optional `schedule`. Requires the `doubleclickbidmanager` scope.
2. Run the query (on demand or on its schedule). Running produces a CSV stored automatically in Google Cloud Storage.
3. `queries.reports.list` with `orderBy` to find the most recent report, then read `metadata.googleCloudStoragePath` (output only: the location of the generated report file in Cloud Storage) and download from that path. Direct bucket access is not granted.

For which metrics and dimensions to request and how to read them, see the `dv360-reporting` skill.

## Sources

- DV360 API release notes (v4 current, GA): https://developers.google.com/display-video/api/release-notes
- DV360 API v4 REST reference (resource list): https://developers.google.com/display-video/api/reference/rest
- DV360 API v4 advertisers.lineItems: https://developers.google.com/display-video/api/reference/rest/v4/advertisers.lineItems
- DV360 API v4 advertisers.insertionOrders: https://developers.google.com/display-video/api/reference/rest/v4/advertisers.insertionOrders
- DV360 API v4 sdfdownloadtasks: https://developers.google.com/display-video/api/reference/rest/v4/sdfdownloadtasks
- Use a service account: https://developers.google.com/display-video/api/guides/concepts/general/service-accounts
- Authorize requests: https://developers.google.com/display-video/api/guides/how-tos/authorizing
- Install client libraries: https://developers.google.com/display-video/api/guides/getting-started/libraries
- Bid Manager API getting started: https://developers.google.com/bid-manager/guides/getting-started-api
- Bid Manager API v2 queries.create: https://developers.google.com/bid-manager/reference/rest/v2/queries/create
- Bid Manager API v2 queries.reports.list: https://developers.google.com/bid-manager/reference/rest/v2/queries.reports/list
