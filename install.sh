#!/usr/bin/env bash
set -euo pipefail
skill="${1:-all}"
dest="${DEST:-$HOME/.claude/skills}"
src="$(cd "$(dirname "$0")" && pwd)/skills"
mkdir -p "$dest"
if [ "$skill" = "all" ]; then names=$(ls "$src"); else names="$skill"; fi
for name in $names; do
  [ -f "$src/$name/SKILL.md" ] || { echo "Skill source not found: $src/$name" >&2; exit 1; }
  mkdir -p "$dest/$name"
  cp -R "$src/$name/." "$dest/$name/"
  echo "Installed: $name -> $dest/$name"
done
echo "Restart Claude Code to refresh the skill list."
