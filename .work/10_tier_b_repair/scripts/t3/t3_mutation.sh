#!/usr/bin/env bash
# T3 S3.5 mutation (retrospective rule 5): delete one T2-added sentence in a KB temp copy -> t3_direct_hit must go RED
# (fp_match regression stays blind to it: the atom never hit at T0); restore -> GREEN. Real KB md5 unchanged.
# T4 W3 (主控决定 3, 2026-11-27): M3 retargeted from CE '[ ] Surgery' (0 matches after the U-9a CRF glyph change; the 14 CE
# p153 atoms moved to rule T1-two-agent+T2-rework, which direct_hit does not anchor) to DM/spec.md:219 ARMCD CDISC Notes, the
# T1-two-agent kb_loc line of ig34_p0064_a001 (PRESENT, unique in file) -> deleting one sentence must give anchor_lost (RED).
# Usage (repo root): bash .work/10_tier_b_repair/scripts/t3/t3_mutation.sh
set -u
cd /Volumes/DevSSD/Project/sdtm-pedia
T=.work/10_tier_b_repair; S=$T/work/scratch/t3; K=$S/kbcopy
ATOM=ig34_p0133_a021; F=domains/AE/assumptions.md   # B-AE INSERTED (t2_batches/B-AE.writer.jsonl:1), TB EXACT, absent at 302ec4c
kbmd5() { find "$1" -name '*.md' -type f | LC_ALL=C sort | xargs cat | md5 -q; }
REAL0=$(kbmd5 knowledge_base); echo "real KB md5 before: $REAL0"
rm -rf "$K"; cp -R knowledge_base "$K"
echo "== M0 copy as-is";  python3 -I $T/scripts/t3/t3_direct_hit.py --kb-root "$K" | grep -E "tb_exact_miss|unexplained|RESULT"; echo "rc=${PIPESTATUS[0]}"
cp "$K/$F" "$S/mut_orig.md"
python3 -I - "$K/$F" <<'EOF'
import sys
p = sys.argv[1]; s = open(p, encoding="utf-8").read()
key = "An events domain that contains data describing untoward medical occurrences"
i = s.index(key); j = s.index(".", i) + 1
open(p, "w", encoding="utf-8").write(s[:i] + s[j:])
print("deleted chars", j - i, "from", p)
EOF
echo "== M1 sentence deleted"; python3 -I $T/scripts/t3/t3_direct_hit.py --kb-root "$K" | grep -E "tb_exact_miss|unexplained|RESULT"; echo "rc=${PIPESTATUS[0]}"
echo "== M1 fp_match regression on the same copy (blind check)"
python3 -I $T/scripts/fp_match.py --sections $T/work/section_coverage.wc.baseline.jsonl --kb-root "$K" --out $S/fp_mut.jsonl --baseline $T/work/fp_baseline.jsonl --regress-out $S/reg_mut.jsonl | grep -E "regressions="
grep -c "$ATOM" $S/reg_mut.jsonl | sed 's/^/  mutated atom in fp regress list: /'
cp "$S/mut_orig.md" "$K/$F"
echo "== M2 restored"; python3 -I $T/scripts/t3/t3_direct_hit.py --kb-root "$K" | grep -E "tb_exact_miss|unexplained|RESULT"; echo "rc=${PIPESTATUS[0]}"
# ---- attempt 2: audit kbcopy2 mutations (step_T3_audit.md §5.3), each on a fresh copy, then all three together
mut() {  # $1 label, $2.. python mutation snippets applied to copy
  local L=$1; shift; rm -rf "$K"; cp -R knowledge_base "$K"
  python3 -I - "$K" "$@" <<'EOF2'
import re, sys
K = sys.argv[1]
def sub(rel, pat, rep, flags=0):
    p = f"{K}/{rel}"; s = open(p, encoding="utf-8").read(); s2, n = re.subn(pat, rep, s, flags=flags)
    open(p, "w", encoding="utf-8").write(s2); print(f"  {rel}: {n} replacement(s)")
for m in sys.argv[2:]:
    if m == "surgery":   sub("domains/CE/examples.md", r"  \[ \] Surgery", "")   # retired (T4 W3): CRF now '□ Surgery', CE atoms no longer T1-two-agent
    if m == "armcd":     sub("domains/DM/spec.md", r" It is not subject to the character restrictions that apply to TESTCD\.", "")
    if m == "ecxpt":     sub("domains/EX/examples.md", r"\bec\.xpt", "ecX.xpt"); sub("domains/EC/examples.md", r"\bec\.xpt", "ecX.xpt")
    if m == "visitnum":  sub("domains/NV/spec.md", r"^### VISITNUM\n(?:(?!### ).*\n)*", "", re.M)
EOF2
  echo "== $L"; python3 -I $T/scripts/t3/t3_direct_hit.py --kb-root "$K" | grep -E "tb_exact_miss|k11_short|anchor_lost|unexplained|RESULT"; echo "rc=${PIPESTATUS[0]}"
}
mut "M3 DM/spec ARMCD CDISC Notes sentence deleted (T1-two-agent kb_loc ig34_p0064_a001; was CE [ ] Surgery)" armcd
mut "M4 EX/EC ec.xpt renamed" ecxpt
mut "M5 NV/spec '### VISITNUM' block deleted" visitnum
mut "M6 M3+M4+M5" armcd ecxpt visitnum
rm -rf "$K"; cp -R knowledge_base "$K"
echo "== M7 fresh copy (restored)"; python3 -I $T/scripts/t3/t3_direct_hit.py --kb-root "$K" | grep -E "tb_exact_miss|anchor_lost|RESULT"; echo "rc=${PIPESTATUS[0]}"
REAL1=$(kbmd5 knowledge_base); echo "real KB md5 after:  $REAL1"; [ "$REAL0" = "$REAL1" ] && echo "real KB unchanged: OK" || echo "real KB CHANGED: FAIL"
