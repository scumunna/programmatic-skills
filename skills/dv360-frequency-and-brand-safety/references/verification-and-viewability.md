# Third-party verification, viewability, and invalid traffic (DV360)

Deep reference for choosing a verification approach and interpreting viewability and invalid-traffic numbers. Read SKILL.md first for the decision rules.

## Table of contents

- Pre-bid avoidance vs post-bid measurement
- DoubleVerify and IAS in DV360
- The Oracle Moat sunset
- Active View viewability targeting and its limits
- MRC-accredited viewability and IVT metrics
- Invalid traffic filtration model

## Pre-bid avoidance vs post-bid measurement

Two distinct jobs, often confused:

- **Pre-bid avoidance** adds a third-party segment (DoubleVerify or IAS) into line item or IO targeting. DV360 looks up the vendor's classification for the impression and will not bid when it fails the rule or when classification is missing. Effect: you never pay for the bad impression. This is a spend-control.
- **Post-bid measurement** places a verification tag that reports quality after the impression served. Effect: you get an independent measured number, but the buy already happened. This is a reporting and contract instrument, not prevention.

Decision: use pre-bid avoidance to control what you buy. Add post-bid measurement only when a contract requires an independent verified metric. Do not pay for both on the same risk category, because the pre-bid segment already prevented the buy that post-bid would only measure.

## DoubleVerify and IAS in DV360

Both integrate as pre-bid controls set in default IO targeting or per line item:

- **DoubleVerify** offers Authentic Brand Safety profiles (entered by segment ID), brand-safety avoidance tiers (high-risk, medium-risk) and 20-plus avoidance categories, and IAB-definition viewability targeting. Vendor rate cards change; for example DoubleVerify revised its standard pre-bid rate card in 2025. Confirm current pricing with the client and the help center before committing.
- **IAS** supplies pre-bid classification looked up by impression URL; DV360 will not bid on impressions lacking IAS classification when the segment is active. YouTube and partners inventory is not supported by IAS pre-bid verification and only supports IAS post-campaign measurement.

Pick one pre-bid vendor per risk category. The choice is usually driven by which vendor the client already contracts and which the measurement plan reports on, not by a feature gap, since native DV360 exclusions already cover the common cases.

## The Oracle Moat sunset

Oracle shut down its advertising business, including Moat measurement, in September 2024. Do not propose Moat as a current verification vendor and do not assume legacy Moat tags still report. If you find Moat referenced in an old setup, treat it as defunct and migrate the measurement need to a supported vendor (for example DoubleVerify or IAS) or to native DV360 metrics. This is an industry fact, not a DV360 Help page; verify the client's current vendor stack directly rather than citing a product page.

## Active View viewability targeting and its limits

Active View is Google's viewability technology. Viewability targeting lets a line item bid only on impressions above a predicted viewability threshold (for example 50% or greater), set on the line item or IO viewability targeting page.

Limits to respect:

- High predicted-viewability inventory is a small subset of all inventory, so a high threshold matches far fewer impressions and can leave budget unspent. Raise the threshold only as far as the KPI needs.
- Impressions that are not measurable for Active View (for example mobile-app inventory not integrated with the Open Measurement SDK) should not be viewability-targeted, because none will qualify and the line item will starve.
- Connected TV devices are excluded by default from viewability targeting applied to a video line item, so you can still bid on most CTV inventory regardless of the viewability setting.
- Predicted viewability is a forecast, not a guarantee. Confirm delivered viewability with post-buy measurement.

## MRC-accredited viewability and IVT metrics

The Media Rating Council accredits specific DV360 metrics. Practical notes:

- Accreditation applies to certain Active View and Begin-to-render impression metrics. To report accredited numbers, count impressions with the Begin-to-render method; other impression-counting methods are not MRC-accredited.
- Viewability accreditation spans viewable, measurable, and eligible impression categories for the accredited metrics.
- Invalid-traffic filtration is accredited for both GIVT and SIVT, with exceptions (for example mobile-app Begin-to-render impressions and tracked ads are noted as not accredited for SIVT filtration).
- Reports can show gross metrics (including invalid traffic) and net metrics (filtered for quality). Know which one a stakeholder is reading before comparing numbers across tools.

## Invalid traffic filtration model

DV360 filters invalid traffic automatically; you confirm it rather than configure it:

- **GIVT** (General Invalid Traffic) is caught by lists of known bots and spiders and routine checks.
- **SIVT** (Sophisticated Invalid Traffic) is harder to detect and needs deeper or human analysis.
- Removal happens **pre-bid** (the traffic is never bought) or **post-serve** (it is credited back to the account, so you do not pay for it).
- Google adds a **HUMAN** integration as an extra safety check, requiring no configuration.

Add third-party verification for invalid traffic only when a client needs an independent number. The native filtration plus HUMAN is the default protection; layering vendors does not change what was already filtered, it only adds an external measurement.

## Sources

- About Integral Ad Science's media quality verification: https://support.google.com/displayvideo/answer/3297897 (as of June 2026)
- Brand suitability (covers DoubleVerify, IAS, and third-party verification integration): https://support.google.com/displayvideo/answer/3032915 (as of June 2026)
- Viewability targeting: https://support.google.com/displayvideo/answer/6101342 (as of June 2026)
- Media Rating Council (MRC) accredited metrics: https://support.google.com/displayvideo/answer/7620594 (as of June 2026)
- Filtering invalid traffic to ensure quality: https://support.google.com/displayvideo/answer/6076504 (as of June 2026)
