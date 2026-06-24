# Search term mining

Mine the search and query data for waste to exclude and intent to capture, and return proposed negatives and new keywords for approval, stopping when no significant new terms remain.

- **Use when:** Weekly, on search-driven buys (Google Ads search, or any platform with a search terms or query report).
- **Action:** Pull the search terms report (`google-ads-keywords-and-match-types`, `google-ads-reporting`, or the platform skill). Separate wasteful queries to add as negatives from high-intent queries worth adding as keywords, each with the spend and performance that justifies it. Use the `optimization-specialist` agent.
- **Verify:** Each proposed negative or new keyword cites the query, its spend, and its performance against the goal. Brand and competitor terms are handled per the account's stated policy.
- **Stop:** Proposals ready for approval. Clean no-op if no query crosses the significance threshold this week.
- **Guardrails:** Recommend only. Do not add or remove keywords or negatives. Approval required before any change. Do not propose a negative that would block a converting query.
- **Handoff:** The trader approves and applies the negatives and new keywords.

Prompt:
> Weekly, pull the search terms report and propose negatives for wasteful queries and new keywords for high-intent queries, each justified by spend and performance against the goal. Do not block converting queries. Recommend only; apply nothing. Stop when no query crosses the significance threshold, and hand the proposals to me for approval.
