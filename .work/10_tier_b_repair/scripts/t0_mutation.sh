#!/bin/bash
# T0.4 mutation test (retrospective §4 rule 5; PLAN G-TB9). Mutates ONLY a temp copy of knowledge_base/
# under work/scratch/ (gitignored). Usage: bash .work/10_tier_b_repair/scripts/t0_mutation.sh
# Baselines (made on the real KB, see t0_mutation.md): work/fp_baseline.jsonl, work/census_BPCPP.json,
# work/section_coverage.wc.baseline.jsonl
set -u
R=/Volumes/DevSSD/Project/sdtm-pedia
T=$R/.work/10_tier_b_repair
S=$T/work/scratch
K=$S/knowledge_base
PY="python3 -I"
CEN="--pages ig34:275-284 --kb knowledge_base/domains/PC/examples.md knowledge_base/domains/PP/examples.md knowledge_base/domains/PC/assumptions.md"
kbsum() { (cd "$1" && find . -type f -name '*.md' -print0 | sort -z | xargs -0 md5 -q | md5 -q); }

reset() { rm -rf "$K"; mkdir -p "$S"; cp -R "$R/knowledge_base" "$K"; }

gates() {  # $1 = label
  echo "---- [$1] fp_match"
  $PY $T/scripts/fp_match.py --kb-root "$K" --out "$S/fp_$1.jsonl" \
      --baseline $T/work/fp_baseline.jsonl --regress-out "$S/reg_$1.jsonl" | grep -E "^(atoms|BASELINE|  REGRESS|RESULT)" | head -12
  echo "fp_match exit=${PIPESTATUS[0]}"
  echo "---- [$1] table_census"
  $PY $T/scripts/table_census.py --kb-root "$K" $CEN --out "$S/census_$1.json" \
      --baseline $T/work/census_BPCPP.json | grep -E "^(PDF tables|BASELINE|  CHANGED|RESULT)"
  echo "table_census exit=${PIPESTATUS[0]}"
  echo "---- [$1] t3_recompute (--downgrade fp regressions)"
  $PY $T/scripts/t3_recompute.py --downgrade "$S/reg_$1.jsonl" --out "$S/sc_$1.jsonl" \
      --baseline $T/work/section_coverage.wc.baseline.jsonl | grep -E "^(  downgraded|TB:|BASELINE|  DIFF|RESULT)"
  echo "t3_recompute exit=${PIPESTATUS[0]}"
}

echo "real KB md5 (before): $(kbsum $R/knowledge_base)"

echo "==== M0 pristine copy"
reset; echo "copy KB md5: $(kbsum $K)"; gates M0

echo "==== M1 delete 1 prose sentence (atom ig34_p0008_a022, EXACT, unique in ch01_introduction.md)"
reset
$PY - "$K/chapters/ch01_introduction.md" <<'EOF'
import sys; p = sys.argv[1]; s = open(p, encoding="utf-8").read()
v = "The SDTMIG is best read online, so the reader can benefit from the many hyperlinks to internal and external references."
assert s.count(v) == 1, s.count(v); open(p, "w", encoding="utf-8").write(s.replace(v, "")); print("M1 deleted:", v[:60], "...")
EOF
gates M1

echo "==== M2 change 1 table value (PC/examples.md Ex1 Method C relrec row 5: IDVARVAL 4 -> 9)"
reset
$PY - "$K/domains/PC/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n")
old = "| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1 |"; i = 77            # line 78 (Ex1 Method C table @72)
assert L[i] == old, L[i]; L[i] = old.replace("| 4 |", "| 9 |"); open(p, "w", encoding="utf-8").write("\n".join(L))
print("M2 line 78:", old, "->", L[i])
EOF
gates M2

echo "==== M2b move 1 value into an empty neighbour cell (PC/assumptions.md:31 relrec row 1: MANY RELTYPE -> IDVARVAL)"
reset
$PY - "$K/domains/PC/assumptions.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n")
old = "| 1 | ABC-123 | PC | | PCGRPID | | MANY | A |"; i = 30
assert L[i] == old, L[i]; L[i] = "| 1 | ABC-123 | PC | | PCGRPID | MANY | | A |"; open(p, "w", encoding="utf-8").write("\n".join(L))
print("M2b line 31:", old, "->", L[i])
EOF
gates M2b

echo "==== M2c change 1 value in a wrapped (multi-line) PDF record (PC/assumptions.md:69 pc.xpt row 13 PCORRES 10 -> 11)"
reset
$PY - "$K/domains/PC/assumptions.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 68
assert L[i].startswith("| 13 | ABC-123 | PC |") and L[i].count("| ANALYTE | 10 | ug/mL |") == 1, L[i][:80]
L[i] = L[i].replace("| ANALYTE | 10 | ug/mL |", "| ANALYTE | 11 | ug/mL |"); open(p, "w", encoding="utf-8").write("\n".join(L))
print("M2c line 69: PCORRES 10 -> 11")
EOF
gates M2c

echo "==== M2d delete 1 KB table row (PC/examples.md:119 Ex1 Method D relrec row 20)"
reset
$PY - "$K/domains/PC/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 118
assert L[i] == "| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 | | 2 |", L[i]
del L[i]; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M2d deleted line 119 (row 20)")
EOF
gates M2d

echo "==== M3 delete 1 subsection (ch04 '#### 4.5.1.2 Tests Not Done', lines 1171-1207)"
reset
$PY - "$K/chapters/ch04_general_assumptions.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n")
assert L[1170].startswith("#### 4.5.1.2 Tests Not Done") and L[1207].startswith("#### 4.5.1.3"), (L[1170], L[1207])
del L[1170:1207]; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M3 deleted 37 lines (4.5.1.2 heading..before 4.5.1.3)")
EOF
gates M3

echo "==== RESTORE (fresh copy of the unmodified KB)"
reset; echo "copy KB md5: $(kbsum $K)"; gates RESTORE

echo "real KB md5 (after): $(kbsum $R/knowledge_base)"
echo "git status knowledge_base/ archive/ releases/:"; (cd $R && git status --short knowledge_base archive releases; echo "(end)")
