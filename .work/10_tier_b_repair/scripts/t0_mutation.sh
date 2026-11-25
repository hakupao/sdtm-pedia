#!/bin/bash
# T0.4 mutation test (retrospective §4 rule 5; PLAN G-TB9). Mutates ONLY a temp copy of knowledge_base/
# under work/scratch/ (gitignored). Usage: bash .work/10_tier_b_repair/scripts/t0_mutation.sh
# Baselines (made on the real KB, see t0_mutation.md): work/fp_baseline.jsonl, work/census_BPCPP.v2.json (census v2;
# v1 baseline work/census_BPCPP.json kept for scripts/archive/table_census_v1.py), work/section_coverage.wc.baseline.jsonl,
# work/census_mut_{MB,EG}.v2.json (M4* cases). v3 (§6): M4a-M4d = T1 false-OK modes a-d, census only, targeted asserts.
set -u
R=/Volumes/DevSSD/Project/sdtm-pedia
T=$R/.work/10_tier_b_repair
S=$T/work/scratch
K=$S/knowledge_base
PY="python3 -I"
CEN="--pages ig34:275-284 --kb knowledge_base/domains/PC/examples.md knowledge_base/domains/PP/examples.md knowledge_base/domains/PC/assumptions.md"
kbsum() { (cd "$1" && find . -type f -name '*.md' -print0 | sort -z | xargs -0 md5 -q | md5 -q); }

reset() { rm -rf "$K"; mkdir -p "$S"; cp -R "$R/knowledge_base" "$K"; }

# expected exit codes "fp census t3" per mutation (1 = RED vs baseline, 0 = GREEN); mismatch -> script exit 1
expect() { case "$1" in M0|RESTORE) echo "0 0 0";; M1|M3) echo "1 0 1";; M2|M2b|M2c|M2d) echo "0 1 0";; *) echo "?";; esac; }  # bash 3.2: no assoc arrays
MISMATCH=0; SUMMARY=""

gates() {  # $1 = label
  echo "---- [$1] fp_match"
  $PY $T/scripts/fp_match.py --kb-root "$K" --out "$S/fp_$1.jsonl" \
      --baseline $T/work/fp_baseline.jsonl --regress-out "$S/reg_$1.jsonl" | grep -E "^(atoms|BASELINE|  REGRESS|RESULT)" | head -12
  local e1=${PIPESTATUS[0]}; echo "fp_match exit=$e1"
  echo "---- [$1] table_census"
  $PY $T/scripts/table_census.py --kb-root "$K" $CEN --out "$S/census_$1.json" \
      --baseline $T/work/census_BPCPP.v2.json | grep -E "^(PDF tables|BASELINE|  CHANGED|RESULT)"
  local e2=${PIPESTATUS[0]}; echo "table_census exit=$e2"
  echo "---- [$1] t3_recompute (--downgrade fp regressions)"
  $PY $T/scripts/t3_recompute.py --downgrade "$S/reg_$1.jsonl" --out "$S/sc_$1.jsonl" \
      --baseline $T/work/section_coverage.wc.baseline.jsonl | grep -E "^(  downgraded|TB:|BASELINE|  DIFF|RESULT)"
  local e3=${PIPESTATUS[0]}; echo "t3_recompute exit=$e3"
  local got="$e1 $e2 $e3" ok=OK
  [ "$got" = "$(expect $1)" ] || { ok=MISMATCH; MISMATCH=1; }
  SUMMARY+="$(printf '%-8s expect=[%s] got=[%s] %s' "$1" "$(expect $1)" "$got" "$ok")"$'\n'
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

# ── v3: T1 false-OK modes (census only). Per case: v2 vs real-KB baseline must be RED, a targeted assert must find the
# mutated table/row/column (and it must be absent from the baseline); v1 (scripts/archive/table_census_v1.py) is run
# against its own pristine-copy baseline and logged (v1=GREEN means v1 was blind to the mode).
CMB="--pages ig34:248-264 --kb knowledge_base/domains/MB/assumptions.md knowledge_base/domains/MB/examples.md"
CEG="--pages ig34:185-193 --kb knowledge_base/domains/EG/assumptions.md knowledge_base/domains/EG/examples.md"
V1=$T/scripts/archive/table_census_v1.py
M4SUM=""; M4BAD=0
v1base() { reset; $PY $V1 --kb-root "$K" $CMB --out "$S/v1base_MB.json" >/dev/null; $PY $V1 --kb-root "$K" $CEG --out "$S/v1base_EG.json" >/dev/null;
           $PY $T/scripts/table_census.py --kb-root "$K" $CMB --out "$S/m4_M0_MB.json" --baseline $T/work/census_mut_MB.v2.json | tail -1
           [ ${PIPESTATUS[0]} = 0 ] || { echo "M4 setup: MB not GREEN"; M4BAD=1; }
           $PY $T/scripts/table_census.py --kb-root "$K" $CEG --out "$S/m4_M0_EG.json" --baseline $T/work/census_mut_EG.v2.json | tail -1
           [ ${PIPESTATUS[0]} = 0 ] || { echo "M4 setup: EG not GREEN"; M4BAD=1; }
           echo "---- [M4d0] real-KB pairing (mode d): MB copy-2 Ex1 relrec @229 must pair with PDF Ex1, PDF Ex3 relrec PDF_ONLY"
           census_check "$S/m4_M0_MB.json" $T/work/census_mut_MB.v2.json pair MB/examples.md 229 1 relrec.xpt 3 || M4BAD=1
           $PY -c "import json,sys; t=[t for t in json.load(open(sys.argv[1]))['tables'] if t['line']==229][0]; print('  v1 (pristine): MB/examples.md:229 ->', t['status'], 'pdf_pages', t.get('pdf_pages'))" "$S/v1base_MB.json"; }
# $1 label  $2 MB|EG  $3.. assert spec (see census_check below)
m4() {
  local L=$1 U=$2; shift 2; local CFG; [ "$U" = MB ] && CFG=$CMB || CFG=$CEG
  echo "---- [$L] table_census v2 ($U)"
  $PY $T/scripts/table_census.py --kb-root "$K" $CFG --out "$S/m4_$L.json" --baseline $T/work/census_mut_$U.v2.json | grep -E "^(BASELINE|  CHANGED|RESULT)" | head -8
  local e2=${PIPESTATUS[0]}
  echo "---- [$L] targeted assert: $*"
  census_check "$S/m4_$L.json" $T/work/census_mut_$U.v2.json "$@"; local ea=$?
  echo "---- [$L] table_census v1 ($U, vs v1 pristine baseline)"
  $PY $V1 --kb-root "$K" $CFG --out "$S/m4v1_$L.json" --baseline "$S/v1base_$U.json" | grep -E "^(BASELINE|  CHANGED|RESULT)" | head -6
  local e1=${PIPESTATUS[0]}
  local ok=OK; { [ "$e2" = 1 ] && [ "$ea" = 0 ]; } || { ok=MISMATCH; M4BAD=1; }
  M4SUM+="$(printf '%-6s v2=%s(expect 1) assert=%s(expect 0) v1=%s %s' "$L" "$e2" "$ea" "$( [ "$e1" = 0 ] && echo GREEN-blind || echo RED )" "$ok")"$'\n'
}
census_check() {  # report baseline kind args...  kind: cell FILE LINE KBROW COL | row FILE LINE KBROW | pdfonly DS EX |
                  #   only1 FILE LINE COL KBVAL | pair FILE LINE PDFEX ONLY_DS ONLY_EX
  $PY - "$@" <<'EOF'
import json, sys
rep, base, kind, *a = sys.argv[1:]
R, B = json.load(open(rep)), json.load(open(base))
def tab(r, f, ln): return next((t for t in r["tables"] if t["file"].endswith(f) and t["line"] == int(ln)), None)
if kind == "cell":
    f, ln, row, col = a
    hit = lambda r: [d for d in (tab(r, f, ln) or {}).get("diffs", []) if d.get("kb_row") == row and d.get("col") == col]
    ok = bool(hit(R)) and not hit(B); print("  assert cell", f, ln, "row", row, col, "->", hit(R)[:1], "| in baseline:", bool(hit(B)))
elif kind == "row":
    f, ln, row = a
    hit = lambda r: [d for d in (tab(r, f, ln) or {}).get("diffs", []) if d.get("kb_row") == row]
    ok = bool(hit(R)) and not hit(B); print("  assert row", f, ln, "row", row, "->", hit(R)[:2], "| in baseline:", bool(hit(B)))
elif kind == "pair":   # real-KB property (no baseline condition): table FILE:LINE pairs with a PDF table of example EX,
    f, ln, ex, ods, oex = a      # and PDF table (ODS, OEX) is PDF_ONLY
    t = tab(R, f, ln) or {}; po = [p for p in R["pdf_only"] if p["ds"] == ods and p["ex"] == oex]
    ok = t.get("pdf_ex") == ex and bool(po)
    print("  assert pair", f, ln, "-> pdf_ex", t.get("pdf_ex"), t.get("pdf_pages"), "| PDF_ONLY", ods, oex, "->", [p["pages"] for p in po])
elif kind == "pdfonly":
    ds, ex = a
    hit = lambda r: [p for p in r["pdf_only"] if p["ds"] == ds and p["ex"] == ex]
    ok = bool(hit(R)) and not hit(B); print("  assert pdf_only", ds, "ex", ex, "->", hit(R)[:1], "| in baseline:", bool(hit(B)))
elif kind == "only1":
    f, ln, col, kv = a
    t = tab(R, f, ln) or {}
    cells = [d for d in t.get("diffs", []) if d["type"] == "CELL" and d["col"] != "Row"]
    unm = [d for d in t.get("diffs", []) if d["type"] in ("KB_ROW_UNMATCHED", "PDF_ROW_MISSING")]
    ok = len(cells) == 1 and cells[0]["col"] == col and cells[0]["kb"] == kv and len(unm) == 1
    print("  assert only1", f, ln, "non-Row cell diffs:", [(d["kb_row"], d["col"], d["kb"], d["pdf"]) for d in cells][:4],
          "| unmatched rows:", [(d["type"], d.get("kb_row"), d.get("pdf_row")) for d in unm])
print("  ASSERT", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
EOF
}

echo "==== M4 setup: v1 baselines on a pristine copy; v2 vs real-KB baselines on the pristine copy must be GREEN"
v1base

echo "==== M4a every KB copy checked (mode a): MB/examples.md:258 copy-2 suppbe row 1 QVAL SPUTUM -> BLOOD (copy 1 @48 untouched)"
reset
$PY - "$K/domains/MB/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 257
old = "| 1 | ABC | BE | ABC-01-101 | BEREFID | SP01 | BESPEC | Specimen Type | SPUTUM | CRF |"
assert L[i] == old and L[47] == old, (L[i], L[47]); L[i] = old.replace("SPUTUM", "BLOOD"); open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4a MB cell MB/examples.md 256 1 QVAL

echo "==== M4b swap 2 values inside a wrapped (multi-line) PDF record (mode b): EG/examples.md:64 Ex3 row 1 EGCAT <-> EGPOS"
reset
$PY - "$K/domains/EG/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 63
assert L[i].startswith("| 1 | STUDY01 |") and L[i].count("| INTERVAL | SUPINE |") == 1, L[i][:60]
L[i] = L[i].replace("| INTERVAL | SUPINE |", "| SUPINE | INTERVAL |"); open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4b EG cell EG/examples.md 62 1 EGPOS

echo "==== M4b2 move a value into the empty neighbour cell of a wrapped record (mode b): EG/examples.md:64 EGLEAD -> EGLOBXFL"
reset
$PY - "$K/domains/EG/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 63
assert L[i].count("| LEAD II | | 2 |") == 1, L[i][:60]
L[i] = L[i].replace("| LEAD II | | 2 |", "| | LEAD II | 2 |"); open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4b2 EG cell EG/examples.md 62 1 EGLOBXFL

echo "==== M4c duplicate KB row number (mode c, v1 keyed rows on Row): EG/examples.md Ex3, wrong copy of row 5 inserted before row 5"
reset
$PY - "$K/domains/EG/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 67
assert L[i].startswith("| 5 | STUDY01 |") and L[i].count("| 176 | msec | 176 | 176 |") == 1, L[i][:60]
L.insert(i, L[i].replace("| 176 | msec | 176 | 176 |", "| 999 | msec | 999 | 999 |")); open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4c EG row EG/examples.md 62 5

echo "==== M4c2 row alignment by content (mode c): EG Ex3 extra KB row after row 10, later rows renumbered +1, one real change"
echo "     (row 20 -> 21 EGORRES 402 -> 403). Only that one non-Row cell may be reported (no cascade), plus 1 unmatched row."
reset
$PY - "$K/domains/EG/examples.md" <<'EOF'
import sys, re; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n")
assert L[72].startswith("| 10 | STUDY01 |") and L[86].startswith("| 24 | STUDY01 |") and L[82].count("| 402 | msec | 402 | 402 |") == 1
L[82] = L[82].replace("| 402 | msec | 402 | 402 |", "| 403 | msec | 402 | 402 |")
for i in range(73, 87):
    L[i] = re.sub(r"^\| (\d+) \|", lambda m: f"| {int(m.group(1)) + 1} |", L[i])
L.insert(73, "| 11 | STUDY01 | EG | 2324-P0001 | 11 | ... | XXAG | XX Interval, Aggregate | INTERVAL | SUPINE | 123 | msec | 123 | 123 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |")
open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4c2 EG only1 EG/examples.md 62 EGORRES 403

echo "==== M4e KB row shorter than its header (dropped last cell): EG/examples.md:64 Ex3 row 1 loses EGREPNUM"
reset
$PY - "$K/domains/EG/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n"); i = 63
assert L[i].startswith("| 1 | STUDY01 |") and L[i].endswith("| ... | 1 |"), L[i][-30:]
L[i] = L[i][: -len(" 1 |")]; open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4e EG row EG/examples.md 62 1

echo "==== M4d pairing by example + dataset (mode d): delete both KB copies of MB Ex2 suppbe.xpt -> PDF table must be PDF_ONLY"
reset
$PY - "$K/domains/MB/examples.md" <<'EOF'
import sys; p = sys.argv[1]; L = open(p, encoding="utf-8").read().split("\n")
assert L[253] == "**suppbe.xpt**" and L[43] == "**suppbe.xpt**" and L[262].startswith("| 6 |") and L[52].startswith("| 6 |")
del L[253:263]; del L[43:53]; open(p, "w", encoding="utf-8").write("\n".join(L))
EOF
m4 M4d MB pdfonly suppbe.xpt 2

echo "==== RESTORE (fresh copy of the unmodified KB)"
reset; echo "copy KB md5: $(kbsum $K)"; gates RESTORE

echo "real KB md5 (after): $(kbsum $R/knowledge_base)"
echo "git status knowledge_base/ archive/ releases/:"; (cd $R && git status --short knowledge_base archive releases; echo "(end)")
echo "==== EXPECT TABLE (fp census t3)"; printf '%s' "$SUMMARY"
echo "==== M4 TABLE (census v2 RED + targeted assert; v1 logged)"; printf '%s' "$M4SUM"
echo "---- RESTORE census v2 MB/EG vs baselines (must be GREEN)"
R1=0; $PY $T/scripts/table_census.py --kb-root "$K" $CMB --out "$S/m4_RESTORE_MB.json" --baseline $T/work/census_mut_MB.v2.json | tail -1; [ ${PIPESTATUS[0]} = 0 ] || R1=1
$PY $T/scripts/table_census.py --kb-root "$K" $CEG --out "$S/m4_RESTORE_EG.json" --baseline $T/work/census_mut_EG.v2.json | tail -1; [ ${PIPESTATUS[0]} = 0 ] || R1=1
[ "$R1" = 0 ] || { echo "RESTORE M4 census not GREEN"; MISMATCH=1; }
[ "$M4BAD" = 0 ] || MISMATCH=1
if [ "$MISMATCH" = 0 ]; then echo "MUTATION RESULT: ALL MATCH (exit 0)"; exit 0; else echo "MUTATION RESULT: MISMATCH (exit 1)"; exit 1; fi
