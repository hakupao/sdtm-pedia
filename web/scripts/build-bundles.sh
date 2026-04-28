#!/usr/bin/env bash
# web/scripts/build-bundles.sh — produces 4 platform zip bundles in web/dist-bundles/
set -euo pipefail

VERSION="${1:-v1.0}"
SRC_ROOT="$(cd "$(dirname "$0")/../.." && pwd)/ai_platforms/release/v1.0/self_deploy"
OUT_DIR="$(cd "$(dirname "$0")/.." && pwd)/dist-bundles"

mkdir -p "$OUT_DIR"
rm -f "$OUT_DIR"/*.zip

for PLATFORM in claude chatgpt gemini notebooklm; do
  SRC="$SRC_ROOT/$PLATFORM"
  if [[ ! -d "$SRC" ]]; then
    echo "ERROR: $SRC not found" >&2
    exit 1
  fi
  OUT="$OUT_DIR/${PLATFORM}_bundle_${VERSION}.zip"
  ( cd "$SRC_ROOT" && zip -rq "$OUT" "$PLATFORM/" )
  echo "✓ $OUT  ($(du -h "$OUT" | cut -f1))"
done

echo ""
echo "Done. Upload to GH Release: gh release create $VERSION $OUT_DIR/*.zip"
