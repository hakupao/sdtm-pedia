#!/usr/bin/env bash
# branches/jp_delivery/scripts/build_zip.sh — pack iTMS deliverable zip.
#
# Pulls from single source of truth:
#   release/$VERSION/                      (md + self_deploy/)
#   branches/jp_delivery/*.xlsx            (6 xlsx, produced by build_xlsx.py)
#
# Output:
#   branches/jp_delivery/deliverable/YYYYMMDD_iTMS_SDTM_進捗版_$VERSION.zip
#   + .sha256
#
# Usage:
#   branches/jp_delivery/scripts/build_zip.sh [VERSION]
#   branches/jp_delivery/scripts/build_zip.sh v1.0

set -euo pipefail

VERSION="${1:-v1.0}"
REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
JP_ROOT="$REPO_ROOT/branches/jp_delivery"
RELEASE_DIR="$REPO_ROOT/release/$VERSION"
OUT_DIR="$JP_ROOT/deliverable"
DATE_STAMP="$(date +%Y%m%d)"
ZIP_NAME="${DATE_STAMP}_iTMS_SDTM_進捗版_${VERSION}.zip"
ZIP_PATH="$OUT_DIR/$ZIP_NAME"

if [[ ! -d "$RELEASE_DIR" ]]; then
  echo "ERROR: $RELEASE_DIR not found" >&2
  exit 1
fi

# Required xlsx (produced by build_xlsx.py upstream)
REQUIRED_XLSX=(
  "00_納品範囲.xlsx"
  "01_要件定義書.xlsx"
  "02_基本設計書.xlsx"
  "07_進捗報告書.xlsx"
  "08_反復実績記録.xlsx"
  "99_用語集.xlsx"
)
for x in "${REQUIRED_XLSX[@]}"; do
  if [[ ! -f "$JP_ROOT/$x" ]]; then
    echo "ERROR: $JP_ROOT/$x not found (run build_xlsx.py first)" >&2
    exit 1
  fi
done

mkdir -p "$OUT_DIR"

# Stage in a temp dir to control the top-level directory name in the zip
STAGE_DIR="$(mktemp -d -t jp_delivery_zip.XXXXXX)"
trap 'rm -rf "$STAGE_DIR"' EXIT
TOP="${DATE_STAMP}_iTMS_SDTM_進捗版_${VERSION}"
mkdir -p "$STAGE_DIR/$TOP"

# 1. copy 6 xlsx
for x in "${REQUIRED_XLSX[@]}"; do
  cp "$JP_ROOT/$x" "$STAGE_DIR/$TOP/"
done

# 2. copy release/$VERSION/ → release_$VERSION/  (flat-named inside zip)
INNER="release_${VERSION}"
mkdir -p "$STAGE_DIR/$TOP/$INNER"
( cd "$RELEASE_DIR" && tar cf - . ) | ( cd "$STAGE_DIR/$TOP/$INNER" && tar xf - )

# 3. zip
rm -f "$ZIP_PATH"
( cd "$STAGE_DIR" && zip -rq "$ZIP_PATH" "$TOP/" )

# 4. sha256
( cd "$OUT_DIR" && shasum -a 256 "$ZIP_NAME" > "${ZIP_NAME}.sha256" )

echo "✓ $ZIP_PATH  ($(du -h "$ZIP_PATH" | cut -f1))"
echo "✓ $ZIP_PATH.sha256"
