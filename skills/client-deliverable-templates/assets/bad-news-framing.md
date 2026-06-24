# Framing bad news for a client

When a result misses, a budget is at risk, or something broke, lead with control and a plan,
not with apology or excuse. Use this four-part pattern. It tells the client what happened,
proves we understand it, shows we are already acting, and gives them a clear ask. Send it
early. Bad news ages badly, and a client who hears it from us first stays a client.

Keep it honest and plain. Do not bury the miss, do not blame the client, do not present a
correlation as the cause when you are not sure, and do not promise a recovery you cannot
support. State expected recovery as a range, not a guarantee. No em dashes in the text. Route
anything client-facing through the `qa-scrutinizer` agent and shape it with the
`client-communications-lead` agent.

## The four parts

1. **The situation.** State plainly what is happening, in one or two sentences. No softening
   preamble. The client should know the headline by the end of the first line.
2. **What we saw.** The facts and the cause, with the numbers and where they came from. Show
   we understand why it happened. If the cause is not yet certain, say so and say what we are
   doing to find it. Do not guess a cause and present it as fact.
3. **What we are doing.** The actions already underway and the expected effect, with timing.
   This is the part that rebuilds confidence. Change one lever at a time so we can tell what
   worked. State the expected recovery as a range, not a promise.
4. **What we need from you.** The specific decision, approval, or input we need, and by when.
   End with a clear ask so the client knows exactly how to help.

## Worked example

A retargeting line item's cost per order ran well over target after a landing-page change on
the client's site broke conversion tracking for several days.

> **The situation.** Cost per order on the retargeting campaign came in at 42 dollars last
> week against our 25 dollar target, and I want to walk you through why and what we have
> already changed.
>
> **What we saw.** The conversion tag stopped firing on the checkout page from the 8th to the
> 11th, right after the landing-page update went live, so orders were happening but not being
> recorded (source: tag-firing logs and the conversion report for those dates). The spend was
> real, but roughly three days of orders were missing from the numbers, which pushed the
> recorded cost per order up. The underlying performance before and after that window held at
> about 24 dollars.
>
> **What we are doing.** We fixed the tag on the 12th and confirmed it is firing on every
> checkout, and we have paused new spend reallocation until the recovered data settles so we
> do not optimize on a bad signal. Once the corrected orders backfill, we expect the cost per
> order for the period to land between 26 and 30 dollars, close to target. We will confirm the
> recovered figure in this week's report.
>
> **What we need from you.** Please confirm your team will give us a heads-up before the next
> site change so we can verify tracking in advance. If you can approve that quick check as a
> standing step, we can keep this from recurring.

Notice the example states the miss in the first sentence, sources every number, separates what
broke (tracking) from how the campaign actually performed, gives the recovery as a range, and
ends with a concrete ask. It does not apologize three times, does not blame the client's
developers, and does not promise the number will fully recover.
