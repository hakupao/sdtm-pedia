#!/usr/bin/env bash
# tools/build_release.sh — single entry point to build all release products.
#
# Inputs (single source of truth):
#   release/$VERSION/                       (the only authoritative source)
#
# Outputs:
#   web/dist-bundles/*_bundle_$VERSION.zip   (4 per-platform GitHub-release zips)
#   branches/jp_delivery/deliverable/*.zip   (iTMS bundle, includes release/ copy)
#   release/$VERSION/BUILD_MANIFEST.json     (hash + size record, prevents drift)
#
# Usage:
#   tools/build_release.sh [VERSION] [--skip-jp] [--skip-web]
#   tools/build_release.sh v1.0
#   tools/build_release.sh v1.1 --skip-jp

set -euo pipefail

VERSION="${1:-v1.0}"
SKIP_JP=0
SKIP_WEB=0
for arg in "$@"; do
  case "$arg" in
    --skip-jp)  SKIP_JP=1 ;;
    --skip-web) SKIP_WEB=1 ;;
  esac
done

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RELEASE_DIR="$REPO_ROOT/release/$VERSION"

if [[ ! -d "$RELEASE_DIR" ]]; then
  echo "ERROR: $RELEASE_DIR not found" >&2
  exit 1
fi

echo "=== build_release.sh — VERSION=$VERSION ==="
echo "release source: $RELEASE_DIR"
echo

# --- 1. web bundles (4 platform zips for GitHub release) ---
if [[ $SKIP_WEB -eq 0 ]]; then
  echo "→ building web bundles..."
  bash "$REPO_ROOT/web/scripts/build-bundles.sh" "$VERSION"
  echo
else
  echo "→ skip web bundles (--skip-web)"
fi

# --- 2. jp_delivery zip (iTMS bundle) ---
if [[ $SKIP_JP -eq 0 ]]; then
  echo "→ building jp_delivery zip..."
  bash "$REPO_ROOT/branches/jp_delivery/scripts/build_zip.sh" "$VERSION"
  echo
else
  echo "→ skip jp_delivery zip (--skip-jp)"
fi

# --- 3. BUILD_MANIFEST.json (hash record) ---
MANIFEST="$RELEASE_DIR/BUILD_MANIFEST.json"
echo "→ writing $MANIFEST"
{
  echo "{"
  echo "  \"version\": \"$VERSION\","
  echo "  \"built_at\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\","
  echo "  \"git_commit\": \"$(git -C "$REPO_ROOT" rev-parse HEAD 2>/dev/null || echo unknown)\","
  echo "  \"source_md_count\": $(find "$RELEASE_DIR" -name '*.md' | wc -l | tr -d ' '),"
  echo "  \"artifacts\": ["
  FIRST=1
  for f in "$REPO_ROOT/web/dist-bundles"/*.zip "$REPO_ROOT/branches/jp_delivery/deliverable"/*.zip; do
    [[ -f "$f" ]] || continue
    [[ $FIRST -eq 0 ]] && echo ","
    FIRST=0
    REL="${f#$REPO_ROOT/}"
    SIZE=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f")
    SHA=$(shasum -a 256 "$f" | awk '{print $1}')
    printf '    {"path": "%s", "size": %s, "sha256": "%s"}' "$REL" "$SIZE" "$SHA"
  done
  echo
  echo "  ]"
  echo "}"
} > "$MANIFEST"

echo
echo "=== build complete ==="
echo "manifest: $MANIFEST"
