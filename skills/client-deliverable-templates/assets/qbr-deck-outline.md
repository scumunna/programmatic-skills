# Quarterly business review: slide spine

A fixed running order for a quarterly business review (QBR) deck. Build the slides in this
order every time so the client learns where to look and the story always lands the same way:
result first, then proof, then plan. Do not reorder. Add appendix slides freely, but keep the
spine intact.

Every number on every slide is sourced and every claim is honest. No overpromising, no
view-through assist presented as a conversion, no correlation stated as a cause, plain
language throughout, and no em dashes in client text. Route the finished deck through the
`qa-scrutinizer` agent before it ships. Pull verified numbers from the `reporting-analyst`
agent and shape the narrative with the `client-communications-lead` agent.

## Slide 1: Cover

- Title: [Client] quarterly business review, [quarter and year]
- Subtitle: the one-line story of the quarter [for example, hit the cost-per-order target and
  grew incremental orders]
- Prepared by and date.

## Slide 2: Executive summary (three numbers)

The whole quarter in three numbers a busy executive can repeat. Pick the three that matter
most against the objective, show each against its target, and write one sentence of so-what.
Resist a fourth number here. Detail lives later.

- Number 1: [primary KPI] is [value] against a target of [target] ([ahead or behind]).
- Number 2: [scale or efficiency metric] is [value].
- Number 3: [proof metric, for example incremental lift] is [value].
- One-sentence takeaway: [what this means for the client's business].

## Slide 3: Performance versus goals

Each objective and KPI against its target, in a table the client can scan. Green or red is
fine, but show the actual, the target, and the gap. This is the scoreboard, not the analysis.

| Objective | KPI | Target | Actual | Status |
| --- | --- | --- | --- | --- |
| [awareness] | [reach or on-target] | [target] | [actual] | [on or off track] |
| [conversion] | [cost per action] | [target] | [actual] | [on or off track] |

Every actual cites its source report. Keep post-click and post-view separate where relevant.

## Slide 4: What worked

The two or three things that drove the result, with the evidence. Tie each win to a number on
slide 3, not to a feeling. Say what we will do more of.

- [Win 1]: [what we did], [the result it drove], [the number that proves it].
- [Win 2]: [...]
- What we will scale next quarter as a result: [...]

## Slide 5: What did not work and what we changed

Name the misses plainly and show the action taken. This slide builds trust. A QBR that only
shows wins reads as spin. State the issue, the cause, the fix, and the early read on whether
the fix worked.

- [Miss 1]: [what underperformed], [why], [what we changed], [result of the change so far].
- [Miss 2]: [...]
- Still open: [anything unresolved, with the plan to resolve it].

## Slide 6: Market and competitive context

What moved outside our control that the client should weigh when reading the result. Keep it
factual and sourced. Do not use the market as an excuse for a miss; use it to explain.

- Market shifts: [seasonality, demand, pricing, auction conditions].
- Competitive context: [category trends, share signals where reliably known].
- What it means for us: [the implication for strategy, not a guess dressed as fact].

## Slide 7: Learnings

The durable lessons from the quarter that change how we plan, not a recap. Each learning is a
rule we will carry forward.

- Learning 1: [what we now know], [how it changes the plan].
- Learning 2: [...]
- Learning 3: [...]

## Slide 8: Next-quarter plan and budget

What we will do next quarter and what it costs. Connect each initiative to a learning or a
win above so the plan reads as earned, not invented. Show the budget by funnel stage.

- Priorities: [the two or three plays for next quarter, each tied to a learning].
- Budget: [total], split [awareness %, consideration %, conversion %].
- Targets: [the KPI targets we are committing to test against, stated as targets, not
  promises].
- Forecasts, if shown, are estimates with stated assumptions, given as ranges, never as
  guarantees.

## Appendix

Supporting detail for anyone who wants to go deeper. Nothing here is required reading; the
story stands on slides 1 to 8.

- Full metric tables by line item, creative, audience, and geo.
- Methodology notes: attribution model, lift-test design, measurement windows.
- Glossary: link to the client glossary that ships with this skill for any term used.
- Source list: every report and study the numbers came from.
