#!/usr/bin/env bash
# Deploy the SDTM RAG service from the repo tree into a self-contained service directory
# (~/MyProject/sdtm-rag-service by default) and `uv sync` there. DEPLOY_PLAN.md §3.
#
#   ./deploy/deploy.sh            # sync + uv sync
#   ./deploy/deploy.sh --dry-run  # show what would change, touch nothing
#
# Self-contained: code + data/chroma + knowledge_base are copied in, so the running
# service no longer depends on the active git tree (set SDTM_RAG_KB_ROOT /
# SDTM_RAG_CHROMA_DIR in the service .env — see deploy/.env.service.template).
#
# SAFETY: this script is ADDITIVE for secrets — it NEVER overwrites $DEST/.env or touches
# $DEST/.venv. Stop the service (or accept a brief read during the chroma copy) before a
# production deploy; chroma is read-only at runtime so a live copy is generally safe.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$(cd "$HERE/.." && pwd)"             # .../branches/07_rag_kg/sdtm-rag
REPO_ROOT="$(cd "$SRC/../../.." && pwd)"  # sdtm-pedia repo root
KB="$REPO_ROOT/knowledge_base"
DEST="${SDTM_RAG_SERVICE_DIR:-$HOME/MyProject/sdtm-rag-service}"

DRY=()
[[ "${1:-}" == "--dry-run" ]] && DRY=(-n -v --itemize-changes)  # -v so dry-run lists adds/deletes

EXCL=(--exclude='__pycache__' --exclude='*.pyc' --exclude='.pytest_cache'
      --exclude='.ruff_cache' --exclude='.venv' --exclude='.omc'
      --exclude='*.egg-info' --exclude='logs/')

echo "SRC : $SRC"
echo "KB  : $KB"
echo "DEST: $DEST"
[[ -n "${DRY[*]}" ]] && echo "(dry-run)"

[[ -d "$KB" ]] || { echo "ERROR: knowledge_base not found at $KB" >&2; exit 1; }
[[ -d "$SRC/data/chroma" ]] || { echo "ERROR: data/chroma not found at $SRC/data/chroma" >&2; exit 1; }

mkdir -p "$DEST/data"

# Code dirs: trailing-slash + --delete keeps each dir an exact mirror (removes files
# deleted upstream) WITHOUT touching siblings like $DEST/.env or $DEST/.venv.
for d in server scripts ui webchat eval; do
  rsync "${DRY[@]}" -a --delete "${EXCL[@]}" "$SRC/$d/" "$DEST/$d/"
done
rsync "${DRY[@]}" -a "$SRC/pyproject.toml" "$SRC/uv.lock" "$SRC/README.md" "$DEST/"

# Data + KB (copied in for self-containment).
rsync "${DRY[@]}" -a --delete "$SRC/data/chroma/" "$DEST/data/chroma/"
rsync "${DRY[@]}" -a --delete "$KB/" "$DEST/knowledge_base/"

# Seed the service .env from the template ONLY if absent (never clobber live secrets).
if [[ -z "${DRY[*]}" && ! -f "$DEST/.env" ]]; then
  cp "$HERE/.env.service.template" "$DEST/.env"
  sed -i '' "s#__SERVICE_DIR__#$DEST#g" "$DEST/.env"  # bake the real service dir into KB/chroma paths
  chmod 600 "$DEST/.env"
  echo "Seeded $DEST/.env from template — fill in secrets (python -m scripts.gen_password_hash) before go-live."
fi

if [[ -z "${DRY[*]}" ]]; then
  ( cd "$DEST" && uv sync )
  echo "Deploy complete."
  echo "NEXT (go-live, after IT signoff): see deploy/README.md — fill .env, load the"
  echo "service-dir LaunchAgent (--host 0.0.0.0), pmset, firewall."
else
  echo "[dry-run] nothing changed; uv sync skipped."
fi
