# Playbook: low or no conversions

**Symptom.** Impressions and clicks are delivering, but reported conversions are zero or far below plan.

Suspect measurement before media. The most common cause of "no conversions" is a tracking or reporting problem, not poor targeting. Confirm the conversion is being measured and that you are reading it correctly before you touch bids or audiences.

## Ordered checks

1. **Floodlight firing.** Confirm the Floodlight tag (or equivalent conversion tag) is implemented on the conversion page and is actually firing. A tag that is missing, broken, or not firing reports zero conversions regardless of media quality.
2. **Floodlight attached to the campaign.** Confirm the Floodlight activity is associated with the campaign or line item you are evaluating. An unattached activity records nothing for this campaign.
3. **Conversion column and window.** Confirm you are reading the right column. Post-click and post-view (view-through) conversions differ substantially, and the attribution window (for example 30-day click, 1-day view) changes the count. Reading a post-click-only column on a prospecting display campaign will understate results.
4. **Data freshness.** View-through and some offline conversions lag by hours. Do not declare "no conversions" or re-optimize on data that is only a few hours old. Wait for the data to mature before concluding.
5. **Conversion volume sanity.** Confirm the expected conversion rate against impressions and clicks is realistic. A genuinely tiny conversion count on low click volume can be statistical, not a fault.
6. **Only then question media.** If measurement is confirmed healthy and enough time has passed, then investigate audience quality, bid strategy alignment to the conversion goal, and landing-page experience.

## Fix

Repair the tracking first: fix or attach the Floodlight tag, then read the correct column and window. Once measurement is trustworthy and the data has matured, hand conversion-focused optimization to the bid strategy and audience skills. Do not raise Target CPA aggressiveness on the back of immature or mis-read conversion data.

## Cross-links

- Floodlight, Campaign Manager 360, attribution models and windows: `dv360-measurement-and-attribution`.
- Conversion-oriented bid strategies and learning: `dv360-bid-strategy`.
- Audience quality: `dv360-targeting-and-audiences`.
