#!/usr/bin/env bash
#
# Install the skills in this repository into the agent runtime skills directories.
#
# By default each skill is symlinked (so a "git pull" updates installed skills).
# Pass --copy to copy instead of symlink.
#
# Skill targets:
#   ~/.claude/skills   read by Claude Code
#   ~/.codex/skills    read by Codex
#   ~/.agents/skills   shared path read by Codex, Copilot CLI, and Gemini CLI
#
# Agent targets:
#   ~/.claude/agents   read by Claude Code
#   ~/.codex/agents    read by Codex
# The plugin marketplace install is the simplest way to get skills and agents in every runtime.
#
# Usage:
#   ./install.sh            # symlink skills and agents into the runtime directories
#   ./install.sh --copy     # copy instead of symlinking

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

# Install agent definitions. Claude Code and Codex each read an agents directory.
AGENTS_SRC="$REPO_DIR/agents"
if [ -d "$AGENTS_SRC" ]; then
  agent_count=0
  for agent in "$AGENTS_SRC"/*.md; do
    [ -f "$agent" ] && agent_count=$((agent_count + 1))
  done
  for target in "$HOME/.claude/agents" "$HOME/.codex/agents"; do
    mkdir -p "$target"
    for agent in "$AGENTS_SRC"/*.md; do
      [ -f "$agent" ] || continue
      dest="$target/$(basename "$agent")"
      rm -rf "$dest"
      if [ "$MODE" = "copy" ]; then
        cp "$agent" "$dest"
      else
        ln -s "$agent" "$dest"
      fi
    done
    echo "Installed $agent_count agents into $target ($MODE)"
  done
fi

echo "Done. Restart your agent session so it rediscovers the skills and agents."
