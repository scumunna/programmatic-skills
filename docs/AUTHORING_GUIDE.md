# Authoring guide

This is the contract for every skill in this repository. Follow it exactly so the skills
stay consistent, portable across agent runtimes, and pass `scripts/validate_skills.py`.

## Audience and voice

Write for an experienced programmatic practitioner who is using an AI agent to move faster.
Assume the reader knows what a CPM is. Encode decision rules, thresholds, and sequences,
not 101 definitions. Definitions and shared math live once in `programmatic-foundations`;
link to it rather than repeating it.

Voice: expert, operational, direct. Imperative mood ("Set the bid", "Pull the report").
Explain the **why** behind a rule in one clause so the agent can generalize. No filler, no
marketing language, no hedging.

## Hard rules

1. **No em dashes.** Use periods, commas, parentheses, or "and" / "but". The validator
   fails on any em dash. This applies to SKILL.md and every file under the skill.
2. **Runtime-portable language.** Describe actions, never name a host tool. Write "pull a
   report", "run the script", "open the API client", not "use the Bash tool" or "use the
   Skill tool". This is what lets one SKILL.md serve Claude Code, Codex, and other runtimes
   unchanged.
3. **Cite only verified sources.** Before you cite a Google Help or Developers URL, fetch it
   and confirm it resolves and covers the claim. Drop anything you cannot verify. Never ship
   a link reconstructed from memory. Every skill ends with a Sources section listing the
   verified links and an "as of" date.
4. **Stay in scope.** One skill, one job. If content belongs to a sibling skill, link to it
   by name instead of duplicating it.
5. **No secrets.** Scripts read credentials from environment variables or a path the user
   supplies. Never hardcode keys, tokens, or service-account contents, and never commit them.

## Directory layout

```
skills/<skill-name>/
  SKILL.md                 required
  references/*.md          optional, load-on-demand deep content
  scripts/*.py             optional, runnable helpers (bring your own credentials)
  assets/*                 optional, templates the skill emits
```

`<skill-name>` is kebab-case and must match the `name` in the frontmatter.

## SKILL.md frontmatter

```yaml
---
name: dv360-bid-strategy
description: Choose and configure the right DV360 bid strategy. Use when the user asks about bidding, fixed vs automated bidding, Target CPA, Target CPM, Target ROAS, maximize conversions or value, custom bidding, learning periods, or why a line item is not winning auctions.
---
```

- `name`: kebab-case, identical to the directory name.
- `description`: 1 to 4 sentences, 40 to 700 characters. Lead with what the skill does, then
  list concrete trigger phrases the user might say. Be generous about triggers; agents tend
  to under-invoke skills, so name the obvious phrasings explicitly.

## SKILL.md body structure

Keep the body under about 500 lines. Push long tables, full checklists, and field-level API
maps into `references/` and link to them. Use this skeleton:

```markdown
# <Title>

<One or two sentences on what this skill helps the user do and when it matters.>

## When to use this skill

<Bulleted triggers and the boundary with sibling skills.>

## Quick reference

<A decision table or short flow the agent can scan first.>

## Core process

1. <Step, imperative, with the why in a clause.>
2. ...

## Decision rules and thresholds

<The numeric thresholds and if/then rules an expert would apply.>

## Reference material

<Links to references/*.md with a one-line "read this when ..." for each.>

## Templates and examples

<Real, filled-in examples. Not abstract placeholders.>

## Common pitfalls

<What goes wrong and how to catch it.>

## Sources

- <Verified official URL> (as of <Month Year>)
```

Not every skill needs every section, but every skill needs: title, "When to use this
skill", a quick reference, a core process, and Sources.

## Cross-linking

Refer to other skills by name in prose, for example "see the `programmatic-foundations`
skill for KPI math" or "hand off to `dv360-troubleshooting` if the line item is not
delivering". Do not assume a file path; skills are installed into a flat directory.

## Scripts

- Pure Python 3, standard library where possible. If a script needs the Google API client,
  state the `pip install` line and the required scopes at the top of the file.
- Read credentials from environment variables or a user-supplied path. Document them.
- Each script prints clear usage when run with `--help` or no arguments.
- Scripts are optional helpers, not a dependency of the playbook. The skill must be useful
  to an agent even if the script is never run.

## DV360 specifics that change over time

Note product versions where they matter (DV360 API v4, Structured Data Files v10) but write
the playbook so the decision logic survives a version bump. When you cite a version, cite
the release-notes or reference page that confirms it.

## Before you finish a skill

1. Read it back as the practitioner. Does it tell them something they would actually do?
2. Confirm every cited URL resolves.
3. Confirm no em dashes and no host-tool names.
4. The repository validator will be run after authoring; write so it passes the first time.
