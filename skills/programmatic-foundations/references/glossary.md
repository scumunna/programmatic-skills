# Programmatic glossary

The canonical definitions for this skill library. Other skills link here instead of
redefining terms. Definitions are written for a practitioner: short, operational, with the
"why it matters" attached. Platform-specific names (Floodlight, Active View) are flagged as
Google Marketing Platform terms where relevant.

## The marketplace and its machinery

**DSP (demand-side platform).** The buy-side system a trader operates. It ingests bid
requests, decides whether and how much to bid per impression, and buys across many exchanges
from one seat. DV360 is a DSP. Why it matters: the DSP is where every lever in this library
lives (bidding, targeting, pacing, frequency).

**SSP (supply-side platform).** The sell-side system a publisher operates to expose
inventory to many DSPs and run the auction that maximizes their yield. The SSP sends the bid
request and enforces the floor.

**Ad exchange.** The marketplace that connects DSPs and SSPs and runs the real-time auction.
In practice "exchange" and "SSP" overlap; treat the exchange as the auction venue and the SSP
as the publisher's gateway to it.

**RTB (real-time bidding).** Buying and selling a single impression through an automated
auction that completes in roughly 100 milliseconds while the page or app loads. RTB is the
mechanism; open auction and invite-only (deal) auctions both run over it.

**OpenRTB.** The IAB Tech Lab protocol that standardizes the bid request and bid response so
any DSP can transact with any SSP. Current line is OpenRTB 2.x (2.6) with 3.0 available.
Knowing the object model helps when you read log-level data or debug why a bid was filtered.

**Bid request.** The message the SSP sends to DSPs describing the available impression: site
or app, ad slot size and position, user signals allowed under privacy, device, geo, and the
floor. The DSP decides on this payload alone.

**Bid response.** The DSP's reply: the price, the creative, and any deal ID. If the response
wins the auction and clears the floor, the creative serves.

**Floor price.** The minimum the publisher will accept for an impression. A bid below the
floor never wins, which is a frequent cause of low win rate on cheap line items.

**First-price auction.** The winner pays exactly what they bid. The open programmatic
auction moved from second-price to first-price across the industry, so a bid is now the
actual cost of winning, not a ceiling. This changes bid-shading and pacing behavior: overbid
and you overpay on every win.

**Second-price auction.** The winner pays one cent above the second-highest bid. Largely
historical for open auction, but the mental model still appears in some private setups and
legacy explanations, so know the distinction.

## Deals and private supply

**Deal ID.** The identifier that ties a line item to a negotiated arrangement with a
publisher. The DSP keys the deal's pricing and access off this ID. A wrong or unactivated
deal ID is the first thing to check when a deal line item will not deliver.

**PMP (private marketplace).** Invitation-only auctions where a publisher offers select
inventory to chosen buyers, usually at a floor above open auction. Access and often better
viewability and brand safety are the trade for the higher floor.

**Programmatic Guaranteed (PG).** A direct, automated buy: fixed volume at a fixed price,
guaranteed delivery, no auction. Use for reserved, high-confidence inventory (homepage
takeovers, premium video). Settings like targeting and budget are locked once agreed.

**Preferred Deal.** A non-guaranteed, fixed-price, one-to-one deal that gives a buyer a
first look at inventory before it goes to auction. No volume commitment; the buyer chooses
per impression. Sits between PG and PMP on the control-versus-flexibility spectrum.

**Open auction.** The fully public RTB marketplace, no deal required. Largest scale, lowest
floors, the most variance in quality, so it leans hardest on brand safety and viewability
controls.

## Counting, seeing, and reaching

**Impression.** One ad served. The base unit of delivery and the denominator under most rate
metrics.

**Viewable impression.** An impression that met the MRC and IAB viewability standard:
display = at least 50 percent of the ad's pixels in view for at least 1 continuous second;
in-stream video = at least 50 percent of pixels in view for at least 2 continuous seconds.
Served is not seen; this is the line between them. In Google Marketing Platform, viewability
is measured by Active View.

**Active View.** Google's technology for measuring whether an impression was viewable and
for how long, applying the MRC and IAB thresholds above. It is the GMP implementation of the
viewability standard, not a separate standard.

**Reach.** The count of unique users (or households, or devices) exposed at least once.
Reach plus frequency together describe how an audience was covered; impressions alone do not.

**Frequency.** Average number of times a unique user saw the ad over a window
(impressions / reach). The lever you cap to avoid overexposure and wasted spend.

**Pacing.** How the system spreads budget across a flight so it neither front-loads and
exhausts early nor underdelivers. Pacing can be even (steady daily spend) or ahead (spend as
fast as the market allows). See the `dv360-pacing-and-optimization` skill for the math and
fix trees.

**Flight.** The scheduled run window of a line item or campaign, from start date to end date.
Pacing is computed against the flight.

## Plan structure and money

**IO (insertion order).** The buy-level container that holds line items and carries the
budget and flight for a campaign objective. The unit most reporting and budgeting rolls up
to. See `dv360-campaign-architecture` for the full hierarchy.

**Line item.** The atomic buying unit: one bid strategy, targeting set, creative assignment,
and budget. Where optimization actually happens. Splitting or merging line items is a
core trading decision covered in `dv360-campaign-architecture`.

**Working media.** Spend that actually buys impressions (the media cost paid to publishers).

**Non-working media.** Spend on everything around the media: ad serving, verification,
data and audience fees, agency and platform fees, creative production. Traders watch the
working-to-total ratio because non-working spend buys no reach. Be explicit about which costs
sit inside a CPM and which are layered on, because it changes effective CPM and ROAS.

## Safety and quality

**Brand safety.** Avoiding content that is objectively harmful or illegal to be near
(violence, hate, illegal content). The floor every campaign enforces. Treated as a hard
exclusion.

**Brand suitability.** The advertiser-specific layer above brand safety: content that is safe
in general but wrong for this brand (an alcohol brand avoiding content aimed at minors). Tuned
per advertiser, not universal. Conflating the two leads to over-blocking and lost scale. See
`dv360-frequency-and-brand-safety`.

**IVT (invalid traffic).** Impressions, clicks, or conversions not from genuine human intent.
Split into two tiers:

- **GIVT (general invalid traffic).** Detected by routine filtration: known bots and
  spiders, data-center traffic, declared crawlers. Filtered with lists and rules.
- **SIVT (sophisticated invalid traffic).** Requires advanced analytics to catch: hijacked
  devices, falsified impressions, domain spoofing, bot nets that mimic humans. The
  expensive, deliberate fraud. Verification vendors and the exchange both work to remove it.

Why the split matters: GIVT removal is table stakes and largely automatic; SIVT is where
verification budget and scrutiny earn their keep.

## Conversion tracking (Google Marketing Platform)

**Floodlight.** Google Marketing Platform's conversion tracking system. Floodlight activities
are tags that record conversions and build audiences, shared across Display & Video 360,
Campaign Manager 360, and Search Ads 360 so conversions can be de-duplicated across channels.
A line item counts conversions by the Floodlight activities assigned to it. Deep coverage is
in `dv360-measurement-and-attribution`.

## See also

- KPI and auction formulas: `metrics.md` in this skill.
- Bidding mechanics and strategy selection: `dv360-bid-strategy`.
- Deal setup and non-delivery fixes: `dv360-deals-and-inventory`.
- Viewability, IVT, and suitability controls in practice: `dv360-frequency-and-brand-safety`
  and `dv360-targeting-and-audiences`.
