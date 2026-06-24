# Per-tool setup for path-to-conversion analysis

Field-level setup for each report that produces a conversion path in the Google Marketing
Platform. Read the section for the tool you picked in the SKILL.md quick reference. Every
claim here is from the official documentation listed in the SKILL.md Sources section. Where
the docs describe a field set as configurable rather than fixed, this file says so and hands
off to the help page rather than asserting a closed list.

## Campaign Manager 360 Path to Conversion (P2C) report

The only Google report that lists the raw, ordered sequence of ad impressions and clicks
that preceded a Floodlight conversion. It shows not just the final conversion and the
interaction credited for it, but the longer path of exposures that led there. An exposure is
an impression or a click on one of your ads.

Configuration:

- Build it in Report Builder: create a new report and select the Path To Conversion type.
- A Floodlight configuration ID is required. Selecting it automatically adds all advertisers
  associated with that configuration ID. If you do not pick specific Floodlight activities,
  the report defaults to all of them.
- Set a conversion window of up to 90 days for clicks and impressions. The report checks
  whether an interaction occurred within that window before the associated conversion.
- You can set the maximum gap between interactions and a maximum interaction count (up to
  100 interactions each for clicks and impressions).
- Optionally select "Pivot On Interaction Path" to reorganize rows and columns so several
  interactions can be compared side by side.

Layout: each conversion gets its own row, and its interactions are listed in separate
columns from most to least recent, with detail for each interaction in its column.

Available fields (the docs group these as conversion dimensions, per-interaction dimensions,
metrics, and custom Floodlight variables; treat the exact picklist as configurable and
confirm on the help page). Documented examples include:

- Path structure: interaction count, click count, impression count, path length, and the
  interaction number (the order position, most to least recent before the conversion).
- Time to conversion: the timestamp of each interaction, days between the attributed ad and
  the conversion, days between the first ad in the path and the conversion, and hours
  between the attributed ad and the conversion.
- Interaction attributes: interaction type (click or impression), interaction date and time,
  channel mix, browser and platform, and DMA.
- Custom Floodlight variables and Rich Media metrics, when present on the activity.

Use this report when you need the literal ordered ad exposures per conversion. Its path
length, interaction count, and days-to-conversion fields are the source for the path-length
and time-lag readings in the SKILL.md.

Source: Path to Conversion reports, Campaign Manager 360 Help
(https://support.google.com/campaignmanager/answer/2823644).

## Campaign Manager 360 attribution segments

Inside the Campaign Manager 360 attribution modeling view you can segment conversion-path
data to isolate assists, view-through versus click-through paths, and channel-position
behavior. This is where the assisted-conversion and first-versus-last reads come from.

Documented default segments include:

- Click-through only: conversions attributed to clicks.
- View-through only: conversions from impressions without a click.
- Assisted paths: conversions whose path had more than one touchpoint.
- Unassisted paths: single-interaction conversions.
- First, any, or last interaction is from a given channel (for example Display or Paid
  Search): segments by where a channel sits in the path.

You can also build custom segments through the condition builder using criteria such as
Floodlight variables, revenue, placement, and interaction type. The docs do not provide
prebuilt segments for path length or time lag, so derive those from the P2C report fields
above rather than expecting a ready-made segment.

Use these segments to answer "how many conversions were assisted" and "which channel
initiates versus closes," which is the assisted-conversion reading in the SKILL.md.

Source: Segment conversion path data, Campaign Manager 360 Help
(https://support.google.com/campaignmanager/answer/2823657).

## Google Analytics 4 conversion paths report

GA4 calls this the conversion paths report, surfaced as the key event attribution paths
report. It models the path across paid and organic touchpoints, gives path length and time
lag, and lets you switch attribution models. Unlike the Campaign Manager 360 P2C report, it
covers non-ad channels, not only ad exposures.

Location: open the Advertising section, then under Key events select the key event
attribution paths report.

What it shows:

- A data visualization that splits the path into early touchpoints (the first 25 percent of
  interactions), mid touchpoints (the middle 50 percent), and late touchpoints (the final
  25 percent), so you can see which channels initiate, assist, and close.
- A data table with the metrics Key events, Purchase revenue, Days to key event (the time
  lag reading), and Touchpoints to key event (the path-length reading).
- Paths up to 20 touchpoints long, with the option to filter by path length using an
  operator (equal to, not equal to, greater than, and so on) against a touchpoint count.
- An attribution model selector. The visualization defaults to a paid and organic last-click
  model, and you can switch models to see credit redistribute across the path.

Use this report when you need path length and days to conversion read against an attribution
model and across channels GA4 sees, not only the ad exposures Campaign Manager 360 logs.

Source: Conversion paths (key event attribution paths) report, Google Analytics 4 Help
(https://support.google.com/analytics/answer/10595568).

## Ads Data Hub path and touchpoint analysis

Reach for Ads Data Hub when you need de-duplicated cross-device paths or a credit model you
define yourself, with privacy enforced on output. Ads Data Hub reads aggregated, event-level
Google campaign data in BigQuery and enforces privacy checks and aggregation before any
result is written back, so you never receive user-level rows. The framing, the BigQuery
setup, and the decision of whether a question even needs Ads Data Hub live in the
`dv360-advanced-analytics-adh` skill; this section covers only the path-specific mechanics.

Current path and touchpoint credit approach:

- Touchpoint contribution is computed with the Markov chain analysis, which builds an ordered
  graph where each vertex is a touchpoint and each edge is the probability of moving to the
  next touchpoint, then measures each touchpoint's contribution by removing it and
  recomputing the modeled conversion probability. A Shapley value method is also available
  for credit allocation.
- The analysis runs through the ADH.TOUCHPOINT_ANALYSIS table-valued function, which takes a
  touchpoint table and a user-credit table. Per the docs, this function works with the Data
  Transfer based tables (the cm_dt_ and dv360_dt_ families), not arbitrary sources.
- Privacy threshold: a touchpoint must include 50 or more converting users and 50 or more
  non-converting users, or it is removed by the privacy filters. Outlier users that
  contribute disproportionate credit may also be filtered, so the output can omit touchpoints
  that were present in the input.
- Capacity: Markov chain analysis is currently limited to a maximum of 150 touchpoints.

Note on deprecated tables: the older path tables (the retired CM360 and DV360 paths tables)
were deprecated due to privacy regulations. Do not build new path analysis on them. Use the
current touchpoint and Markov approach above, and confirm the current table and function
names on the Ads Data Hub guide before writing a query.

Use Ads Data Hub when aggregated reports cannot express the path question: de-duplicated
cross-device sequences, custom touchpoint credit, or paths joined to your own first-party
data.

Sources: Ads Data Hub introduction, Google for Developers
(https://developers.google.com/ads-data-hub/guides/intro); Markov chain analysis, Ads Data
Hub, Google for Developers (https://developers.google.com/ads-data-hub/guides/markov).
