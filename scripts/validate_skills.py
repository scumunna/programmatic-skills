#!/usr/bin/env python3
"""Validate every skill in this repository.

For each skills/<name>/SKILL.md this checks:
  1. SKILL.md exists.
  2. YAML frontmatter is present and parses (delimited by lines that are exactly '---').
  3. 'name' is present, kebab-case, and matches the skill directory name.
  4. 'description' is present and within length bounds.
  5. No em dash characters anywhere in the skill's markdown (project writing standard).
  6. Markdown links of the form references/<file>.md resolve to a real file in the skill.

Exit code is 0 when every skill passes and 1 otherwise. No third-party dependencies,
so it runs anywhere Python 3.8+ is available.
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KEY_LINE = re.compile(r"^([A-Za-z0-9_-]+):\s?(.*)$")
REFERENCE_LINK = re.compile(r"(references/[A-Za-z0-9_./-]+\.md)")
EM_DASH = "—"  # em dash codepoint; written escaped so this file holds no literal em dash
DESC_MIN = 40
DESC_MAX = 700


def parse_frontmatter(text: str):
    """Return (data dict, None) on success or (None, reason) on failure."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing opening '---' frontmatter delimiter on line 1"

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, "missing closing '---' frontmatter delimiter"

    data: dict[str, str] = {}
    key = None
    buf: list[str] = []

    def flush():
        nonlocal key, buf
        if key is not None:
            data[key] = "\n".join(buf).strip().strip('"').strip("'").strip()
        key, buf = None, []

    for raw in lines[1:end]:
        match = KEY_LINE.match(raw)
        is_top_level = match and not raw.startswith((" ", "\t"))
        if is_top_level:
            flush()
            key = match.group(1)
            value = match.group(2).strip()
            if value in (">", "|", ">-", "|-", ">+", "|+"):
                buf = []
            else:
                buf = [value]
        elif key is not None:
            buf.append(raw.strip())
    flush()
    return data, None


def find_em_dashes(path: str):
    """Return a list of (line_number, line_text) containing em dashes."""
    hits = []
    with open(path, "r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if EM_DASH in line:
                hits.append((number, line.rstrip()))
    return hits


def validate_skill(skill_dir: str):
    """Return a list of error strings for one skill directory."""
    name = os.path.basename(skill_dir)
    errors: list[str] = []

    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        return [f"{name}: SKILL.md is missing"]

    with open(skill_md, "r", encoding="utf-8") as handle:
        text = handle.read()

    data, reason = parse_frontmatter(text)
    if data is None:
        errors.append(f"{name}: frontmatter error ({reason})")
        return errors

    fm_name = data.get("name", "")
    if not fm_name:
        errors.append(f"{name}: frontmatter is missing 'name'")
    else:
        if fm_name != name:
            errors.append(f"{name}: frontmatter name '{fm_name}' does not match directory")
        if not KEBAB.match(fm_name):
            errors.append(f"{name}: name '{fm_name}' is not kebab-case")

    description = data.get("description", "")
    if not description:
        errors.append(f"{name}: frontmatter is missing 'description'")
    else:
        length = len(description)
        if length < DESC_MIN:
            errors.append(f"{name}: description is too short ({length} chars, min {DESC_MIN})")
        if length > DESC_MAX:
            errors.append(f"{name}: description is too long ({length} chars, max {DESC_MAX})")

    # Em dash scan across SKILL.md and every markdown file under the skill.
    for current, _dirs, files in os.walk(skill_dir):
        for filename in files:
            if filename.endswith(".md"):
                path = os.path.join(current, filename)
                for number, line in find_em_dashes(path):
                    rel = os.path.relpath(path, skill_dir)
                    errors.append(f"{name}: em dash in {rel}:{number} -> {line.strip()}")

    # Reference links must resolve.
    for ref in sorted(set(REFERENCE_LINK.findall(text))):
        ref_path = os.path.join(skill_dir, ref)
        if not os.path.isfile(ref_path):
            errors.append(f"{name}: SKILL.md links missing reference '{ref}'")

    return errors


def main() -> int:
    if not os.path.isdir(SKILLS_DIR):
        print(f"No skills directory found at {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(
        os.path.join(SKILLS_DIR, entry)
        for entry in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, entry))
    )
    if not skill_dirs:
        print("No skills found to validate.")
        return 1

    all_errors: list[str] = []
    passed = 0
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            all_errors.extend(errors)
        else:
            passed += 1

    print(f"Validated {len(skill_dirs)} skills: {passed} passed, {len(skill_dirs) - passed} with issues.")
    if all_errors:
        print("\nIssues found:")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print("All skills valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
