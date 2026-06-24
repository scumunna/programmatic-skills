#!/usr/bin/env bash
#
# Install the skills in this repository into the agent runtime skills directories.
#
# By default each skill is symlinked (so a "git pull" updates installed skills).
# Pass --copy to copy instead of symlink.
#
# Targets:
#   ~/.claude/skills   read by Claude Code
#   ~/.codex/skills    read by Codex
#   ~/.agents/skills   shared path read by Codex, Copilot CLI, and Gemini CLI
#
# Usage:
#   ./install.sh            # symlink skills into all targets
#   ./install.sh --copy     # copy skills instead of symlinking

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$REPO_DIR/skills"

MODE="symlink"
if [ "${1:-}" = "--copy" ]; then
  MODE="copy"
fi

if [ ! -d "$SRC_DIR" ]; then
  echo "Error: no skills directory found at $SRC_DIR" >&2
  exit 1
fi

TARGETS=("$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.agents/skills")

skill_count=0
for skill in "$SRC_DIR"/*/; do
  [ -d "$skill" ] && skill_count=$((skill_count + 1))
done

for target in "${TARGETS[@]}"; do
  mkdir -p "$target"
  for skill in "$SRC_DIR"/*/; do
    [ -d "$skill" ] || continue
    name="$(basename "$skill")"
    dest="$target/$name"
    rm -rf "$dest"
    if [ "$MODE" = "copy" ]; then
      cp -R "$skill" "$dest"
    else
      ln -s "$skill" "$dest"
    fi
  done
  echo "Installed $skill_count skills into $target ($MODE)"
done

echo "Done. Restart your agent session so it rediscovers the skills."
