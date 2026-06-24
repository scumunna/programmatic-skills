# DV360 roles and permissions

Read this when granting access or auditing users. It maps the user roles to what they can do, where they apply, and the least-privilege pattern to default to. Assign the narrowest role at the narrowest scope that lets the person do their job.

For role behavior that changes over time, confirm against the official help page in the Sources section of the parent SKILL.md before relying on an edge case.

## Scope: partner versus advertiser

Access is granted per partner and per advertiser. A user can hold one role per partner and per advertiser they have access to.

- **Partner scope** grants the role across every advertiser under that partner. Use it sparingly. A partner-level Admin can edit any advertiser and manage other users.
- **Advertiser scope** confines the role to a single advertiser. This is the default for day-to-day traders, designers, and analysts.

Rule of thumb: if a person works on one brand, give them an advertiser-scoped role on that advertiser, not a partner-scoped role.

## Role types and what they do

The roles available in Display & Video 360 include the following. Capabilities are summarized for planning; confirm specifics against the help page when an edge case matters.

| Role | Can edit campaigns and spend | Can manage users | Can see reporting | API access | Typical user |
| --- | --- | --- | --- | --- | --- |
| Admin | Yes | Yes | Yes | Yes | Account owner, ops lead |
| Standard | Yes | No | Yes | Yes | Trader who builds and manages campaigns |
| Read only | No | No | Yes | Yes | Reviewer who needs full visibility but no edits |
| Reporting only | No | No | Reporting | No | Analyst or stakeholder |
| Reporting only, limited | No | No | Limited reporting | No | Client-safe reporting access |
| Planner | Plan and draft, not live edits | No | Yes | No | Media planner building drafts |
| Planner, limited | Plan and draft, narrower | No | Limited | No | Restricted planning access |
| Creative | Manage creatives | No | Limited | No | Designer or creative trafficker |
| Creative admin | Manage creatives, broader | No | Limited | No | Creative operations lead |
| Partner client | Constrained partner-level view | No | Yes | No | External partner-side stakeholder |

Notes:
- Only **Admin**, **Standard**, and **Read only** have access to the Display & Video 360 API. Any user or service identity that drives the API or a structured data file workflow must hold one of these three.
- Only **Admin** users can create users and edit access. Everyone else requests changes from an Admin.
- A new user must have a Google Account on their email address before being added. There is no separate password or welcome email; sign-in uses the Google Account.

## Least-privilege patterns

Default each person to the lowest role that still lets them do their job:

- **Stakeholders, clients, finance:** Reporting only (or Reporting only, limited for client-safe views). No edit, no API.
- **Analysts who pull and build reports:** Reporting only. Upgrade to Read only if they need to inspect live campaign settings.
- **Media planners:** Planner, so they can draft without touching live spend.
- **Creative team:** Creative or Creative admin, scoped to the advertiser they design for.
- **Traders who build and manage live campaigns:** Standard on the specific advertiser. Not partner-scoped.
- **Ops leads and account owners:** Admin, kept to a small named list. Partner-level Admin only for the few who genuinely manage multiple advertisers and other users.
- **Service accounts and automation identities:** the minimum API-capable role (often Standard) scoped to the single advertiser the automation touches. Never a partner-wide Admin service account.

## Audit cadence

Review access quarterly:
1. List every user and their role and scope.
2. Remove anyone who changed teams or left.
3. Downgrade anyone holding more than they use (the most common finding is partner Admin that should be advertiser Standard).
4. Confirm every API-driving identity holds an API-capable role and nothing broader.
5. Record the review date so the next audit has a baseline.
