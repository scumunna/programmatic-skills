# Example: rule-based custom bidding scoring

This is an illustrative template, not a literal import file. It shows the shape of a
rule-based custom bidding scoring scheme so you can reason about weights before building the
real algorithm in the Display & Video 360 UI. Field names, allowed value ranges, available
signals, and counting methods change over time, so validate every rule against the current
product (the "Use rules to create custom bidding algorithms" Help page) when you build it. Do
not treat the numbers here as defaults; they are an example to think against.

## How rule-based scoring works (in brief)

A rule-based algorithm assigns a positive numeric score to impressions that lead to the
events you value. You weight each event so that more valuable events get higher scores, the
optimizer learns to bid up impressions likely to produce high-scoring events, and non-matching
impressions score zero. Scores must be greater than zero, and the product currently allows a
few decimal places. When more than one rule can apply to an impression, you choose how the
score resolves (for example, take the highest matching rule). Confirm the exact rules,
ranges, and conflict handling in the product before relying on them.

## Example A: weighted conversion events

The classic case. Several conversion events matter, but not equally, so weight them by
business value instead of counting every conversion the same. Purchases should pull bids far
harder than a shallow product view.

| Event (Floodlight or GA4) | Illustrative weight | Why this weight |
| --- | --- | --- |
| Purchase / sale completed | 5.0 | The outcome you are buying. Bid hardest for impressions that drive it. |
| Add to cart | 2.0 | Strong intent, one step from purchase, but not yet revenue. |
| Begin checkout | 3.0 | Higher intent than add-to-cart; closer to the purchase. |
| Product view / detail page | 0.5 | Weak signal. Counts a little so the model can still learn from it, but must not rival a purchase. |
| Newsletter signup | 1.0 | A real but low-value action. Mid-low weight. |

Reading the table: a purchase is worth ten times a product view (5.0 versus 0.5), so the
optimizer treats one purchase-driving impression as far more valuable than ten that only drive
views. Set the relative weights to match how the business actually values the events, not the
raw conversion counts. If purchase value varies widely (a $20 order versus a $2,000 order),
weighted conversions are a blunt instrument; that is a signal to consider a script-based
approach that can read order value. See the main skill for when to move from rules to a script.

## Example B: viewability plus video completion (no conversions)

For an upper-funnel line item with no conversions to optimize against, score on quality
signals instead. The goal is impressions that are both seen and watched through.

| Condition | Illustrative weight | Why |
| --- | --- | --- |
| Active View viewed (impression measured as viewable) | 1.0 | Baseline for a seen impression. An unviewable impression should score zero. |
| Video completed (100 percent played) | 3.0 | A completed view is the outcome for a completion goal. Weight it well above a bare viewable. |
| Viewable and completed | 4.0 | Both signals together; the best outcome for this goal. Combine the weights. |
| Not viewable | 0 | Served but not seen. No value for a visibility goal. |

Reading the table: an impression that is both viewable and completed scores 4.0, a completed
but borderline-viewable one less, and an unseen impression zero, so the optimizer favors
inventory that is actually watched. Pair this with the matching automated goal on the line
item (for example completed in-view and audible impressions); see the `dv360-bid-strategy`
skill for choosing the surrounding strategy.

## Before you use any of this

- These weights are a teaching example. Pick your own based on the line item's goal and the
  real business value of each event.
- Confirm the available signals, the allowed score range and decimal precision, the counting
  methods, and the multiple-rules-true behavior against the current Help documentation.
- Validate your conversion data first. Rule-based scoring is only as good as the Floodlight or
  GA4 events feeding it. Garbage events produce a confidently wrong algorithm.
- Test the score distribution before assigning the algorithm, and roll out on one line item
  with a small budget first. The main skill covers the staged-rollout process.
