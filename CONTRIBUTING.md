# Contributing

Thanks for improving this library. The goal is a set of skills that are accurate, source
cited, and consistent across agent runtimes.

## Before you start

Read `docs/AUTHORING_GUIDE.md`. It is the contract every skill follows: voice, structure,
frontmatter, the no-em-dash writing standard, runtime-portable language, and the citation
requirement.

## Add or edit a skill

1. Create or open `skills/<skill-name>/SKILL.md`. The directory name is kebab-case and must
   match the `name` in the frontmatter.
2. Follow the body skeleton in the authoring guide. Keep SKILL.md under about 500 lines and
   move deep content into `references/`.
3. Cite only verified official sources. Fetch each URL and confirm it covers the claim before
   you add it. End the skill with a Sources section and an "as of" date.
4. Run the validator until it passes:
   ```
   python3 scripts/validate_skills.py
   ```

## Add a new DSP

The library is multi-DSP by design.

1. Keep all DSP-agnostic concepts in `programmatic-foundations`. Do not fork it per platform.
2. Add the new platform as its own prefixed skills, for example `ttd-bid-strategy` or
   `amzn-campaign-architecture`. Mirror the DV360 skill set so the same workflow is
   comparable across platforms.
3. Reuse the section structure of the matching DV360 skill so a reader can move between
   platforms without relearning the layout.
4. Update the skill table in `README.md`.

## Pull requests

- One logical change per commit. Use conventional commit messages, for example
  `feat: add dv360-custom-bidding skill` or `fix: correct viewability thresholds`.
- Describe what changed and why in the PR. Note any sources you added or verified.
- The validator must pass.

## Scope and accuracy

If a platform behavior is uncertain or version dependent, say so in the skill and link to the
official reference rather than guessing. Accuracy beats completeness.
