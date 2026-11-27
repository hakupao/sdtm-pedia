#!/usr/bin/env bash
# Pre-push check of what `git push origin main` would publish (added lines of origin/main..HEAD + commit metadata).
# Read-only. Personal patterns (user name / real name / e-mail local part) are NOT stored in the repo: pass them as an
# extended regex in $PREPUSH_PERSONAL, e.g.  PREPUSH_PERSONAL='name1|name2' bash .work/10_tier_b_repair/scripts/t4/t4_prepush_check.sh
# Exit 1 if any blocking count is non-zero. Machine paths without a user name are counted and reported, not blocking
# (coordinator's ruling 2026-11-27, see evidence/checkpoints/t4_prepush_check.md).
set -u
cd "$(git rev-parse --show-toplevel)"
BASE=${1:-origin/main}
TMP=$(mktemp); trap 'rm -f "$TMP"' EXIT
git diff "$BASE"..HEAD | grep '^+' | grep -v '^+++' > "$TMP"
cnt() { grep -cE -- "$1" "$TMP"; }
bad=0
blk() { local n; n=$(cnt "$2"); echo "BLOCKING  $1: $n"; [ "$n" = 0 ] || bad=1; }
echo "range $BASE..HEAD = $(git rev-parse --short "$BASE")..$(git rev-parse --short HEAD); commits $(git rev-list --count "$BASE"..HEAD); added lines $(wc -l < "$TMP" | tr -d ' ')"
blk "/Users/<name> or /home/<name> paths" '/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+'
if [ -n "${PREPUSH_PERSONAL:-}" ]; then blk "personal patterns (from env, not stored)" "$PREPUSH_PERSONAL"; else echo "BLOCKING  personal patterns: NOT RUN (set PREPUSH_PERSONAL)"; bad=1; fi
n=$(grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}' "$TMP" | grep -vc 'noreply@anthropic\.com'); echo "BLOCKING  e-mail addresses other than the Co-Authored-By noreply address: $n"; [ "$n" = 0 ] || bad=1
blk "private network addresses" '(^|[^0-9])(192\.168\.[0-9]+\.[0-9]+|10\.[0-9]+\.[0-9]+\.[0-9]+|172\.(1[6-9]|2[0-9]|3[01])\.[0-9]+\.[0-9]+)([^0-9]|$)'
blk "key-shaped strings" '(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|xox[baprs]-[A-Za-z0-9-]{10,})'
blk "password / secret / api key assignments" '(password|passwd|secret|api[_-]?key)["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"' ]{8,}'
# "token": "<word>" is a data field of this project (text tokens of PDF / KB lines); listed for the eye, not blocking
echo "REPORTED  \"token\": \"...\" assignments (text-token data fields): $(cnt 'token["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"' ]{8,}') lines; distinct values: $(grep -oE 'token["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"' ]{8,}' "$TMP" | sed -E 's/^token["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"']//' | sort -u | tr '\n' ' ')"
n=$(git diff --name-only "$BASE"..HEAD | grep -ciE '\.(pdf|xlsx|xls)$|^source/|/pdf_pages/|/pdf_bbox/'); echo "BLOCKING  pdf / xlsx / source / pdf_pages / pdf_bbox files in the range: $n"; [ "$n" = 0 ] || bad=1
n=$(git ls-files | grep -cE '/pdf_pages/|/pdf_bbox/|^source/'); echo "BLOCKING  tracked files under pdf_pages / pdf_bbox / source: $n"; [ "$n" = 0 ] || bad=1
n=$(git log "$BASE"..HEAD --format='%an|%cn' | grep -vc '^hakupao|hakupao$'); echo "BLOCKING  commits whose author or committer is not hakupao: $n"; [ "$n" = 0 ] || bad=1
n=$(comm -13 <(git log "$BASE" --format='%ae%n%ce' | sort -u) <(git log "$BASE"..HEAD --format='%ae%n%ce' | sort -u) | wc -l | tr -d ' '); echo "BLOCKING  author / committer e-mails not already public on $BASE: $n"; [ "$n" = 0 ] || bad=1
echo "REPORTED  machine paths without a user name: /Volumes/ $(cnt '/Volumes/') lines, /private/tmp $(cnt '/private/tmp') lines, files $(for f in $(git diff --name-only "$BASE"..HEAD); do git diff "$BASE"..HEAD -- "$f" | grep '^+' | grep -v '^+++' | grep -qE '/Volumes/|/private/tmp' && echo x; done | wc -l | tr -d ' ')"
echo "REPORTED  Co-Authored-By trailers: $(git log "$BASE"..HEAD --format=%B | grep -c '^Co-Authored-By:') ($(git log "$BASE"..HEAD --format=%B | grep '^Co-Authored-By:' | sed 's/.*<//;s/>.*//' | sort -u | tr '\n' ' '))"
[ "$bad" = 0 ] && echo "RESULT: no blocking item" || echo "RESULT: BLOCKING ITEM(S) FOUND"
exit $bad
