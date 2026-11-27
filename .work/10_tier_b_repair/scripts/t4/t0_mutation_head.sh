#!/bin/bash
# T0.4 mutation test re-proved on the current KB (G-TB9; T4.1 attempt 2 gap "t0_mutation MISMATCH").
# Same gates and same mutations as scripts/t0_mutation.sh (kept untouched, with its T0 baselines, for the record);
# what changed, and why, is listed in evidence/checkpoints/t4_t0_refresh.md:
#   1. baselines: regenerated read-only on the current KB into work/t4/t0_head/ (the T0 files work/fp_baseline.jsonl,
#      work/section_coverage.wc.baseline.jsonl, work/census_*.v2.json are still read by the T3 / T4 scripts -> not overwritten);
#   2. every mutation target is located by content (must match exactly once / under a named heading), not by line number;
#      a mutation that cannot be applied makes the whole run a MISMATCH (the T0 script only printed the AssertionError);
#   3. M4a / M4d0 / M4d: the KB state they were written against no longer exists (D2 de-duplicated the second MB copy,
#      T2 added the missing MB Ex3 relrec table) -> see the per-case comments.
# Mutates ONLY a temp copy under work/scratch/t0_head/ (gitignored). Usage (repo root):
#   bash .work/10_tier_b_repair/scripts/t4/t0_mutation_head.sh --make-baseline   # once per KB state
#   bash .work/10_tier_b_repair/scripts/t4/t0_mutation_head.sh
set -u
R=/Volumes/DevSSD/Project/sdtm-pedia
T=$R/.work/10_tier_b_repair
B=$T/work/t4/t0_head
S=$T/work/scratch/t0_head
K=$S/knowledge_base
PY="python3 -I"
SEC=$T/work/section_coverage.wc.baseline.jsonl   # md_target_files source for fp_match (HANDOFF: always pass it)
CEN="--pages ig34:275-284 --kb knowledge_base/domains/PC/examples.md knowledge_base/domains/PP/examples.md knowledge_base/domains/PC/assumptions.md"
CMB="--pages ig34:248-264 --kb knowledge_base/domains/MB/assumptions.md knowledge_base/domains/MB/examples.md"
CEG="--pages ig34:185-193 --kb knowledge_base/domains/EG/assumptions.md knowledge_base/domains/EG/examples.md"
CRL="--pages ig34:427-431 --kb knowledge_base/chapters/ch08_relationships.md knowledge_base/domains/RELREC/examples.md"
V1=$T/scripts/archive/table_census_v1.py
kbsum() { (cd "$1" && find . -type f -name '*.md' -print0 | sort -z | xargs -0 md5 -q | md5 -q); }
fresh() { rm -rf "$K"; mkdir -p "$S"; cp -R "$R/knowledge_base" "$K"; }
cfg() { case "$1" in MB) echo "$CMB";; EG) echo "$CEG";; REL) echo "$CRL";; esac; }
mkdir -p "$B" "$S"

if [ "${1:-}" = "--make-baseline" ]; then
  echo "real KB md5: $(kbsum $R/knowledge_base); KB tree: $(cd $R && git rev-parse HEAD:knowledge_base); HEAD $(cd $R && git rev-parse --short HEAD)"
  $PY $T/scripts/fp_match.py --sections $SEC --out "$B/fp_baseline.head.jsonl" | grep -E "^(atoms|RESULT)" | head -3
  $PY $T/scripts/t3_recompute.py --out "$B/section_coverage.wc.head.jsonl" | grep -E "^(TB:|RESULT)" | head -3
  $PY $T/scripts/table_census.py $CEN --out "$B/census_BPCPP.v2.head.json" | head -1
  for U in MB EG REL; do $PY $T/scripts/table_census.py $(cfg $U) --out "$B/census_mut_$U.v2.head.json" | head -1; done
  (cd "$B" && md5 -r fp_baseline.head.jsonl section_coverage.wc.head.jsonl census_BPCPP.v2.head.json census_mut_MB.v2.head.json census_mut_EG.v2.head.json census_mut_REL.v2.head.json)
  echo "git status knowledge_base/:"; (cd $R && git status --short knowledge_base; echo "(end)")
  exit 0
fi

# expected exit codes "fp census t3" per mutation (1 = RED vs baseline, 0 = GREEN); mismatch -> script exit 1
expect() { case "$1" in M0|RESTORE) echo "0 0 0";; M1|M3) echo "1 0 1";; M2|M2b|M2c|M2d) echo "0 1 0";; *) echo "?";; esac; }
MISMATCH=0; SUMMARY=""; APPLIED=""
applied() { APPLIED+="$(printf '%-6s mutation applied: %s' "$1" "$2")"$'\n'; [ "$2" = yes ] || MISMATCH=1; }

gates() {  # $1 = label
  echo "---- [$1] fp_match"
  $PY $T/scripts/fp_match.py --sections $SEC --kb-root "$K" --out "$S/fp_$1.jsonl" \
      --baseline "$B/fp_baseline.head.jsonl" --regress-out "$S/reg_$1.jsonl" | grep -E "^(atoms|BASELINE|  REGRESS|RESULT)" | head -12
  local e1=${PIPESTATUS[0]}; echo "fp_match exit=$e1"
  echo "---- [$1] table_census"
  $PY $T/scripts/table_census.py --kb-root "$K" $CEN --out "$S/census_$1.json" \
      --baseline "$B/census_BPCPP.v2.head.json" | grep -E "^(PDF tables|BASELINE|  CHANGED|RESULT)"
  local e2=${PIPESTATUS[0]}; echo "table_census exit=$e2"
  echo "---- [$1] t3_recompute (--downgrade fp regressions)"
  $PY $T/scripts/t3_recompute.py --downgrade "$S/reg_$1.jsonl" --out "$S/sc_$1.jsonl" \
      --baseline "$B/section_coverage.wc.head.jsonl" | grep -E "^(  downgraded|TB:|BASELINE|  DIFF|RESULT)"
  local e3=${PIPESTATUS[0]}; echo "t3_recompute exit=$e3"
  local got="$e1 $e2 $e3" ok=OK
  [ "$got" = "$(expect $1)" ] || { ok=MISMATCH; MISMATCH=1; }
  SUMMARY+="$(printf '%-8s expect=[%s] got=[%s] %s' "$1" "$(expect $1)" "$got" "$ok")"$'\n'
}
# apply one python mutation (body on stdin; it gets p = path, s = text, L = lines). "APPLIED" is printed only if the body
# ran to the end without an assertion error; otherwise the case is recorded as not applied -> MISMATCH.
mutate() {  # $1 label  $2 file (relative to the KB copy)
  local LBL=$1 F=$2 out
  out=$( { echo 'import sys, re'; echo 'p = sys.argv[1]; s = open(p, encoding="utf-8").read(); L = s.split("\n")'; cat; echo 'print("APPLIED")'; } | $PY - "$K/$F" 2>&1 )
  echo "$out" | sed 's/^/  /'
  if echo "$out" | grep -q "^APPLIED$"; then applied "$LBL" yes; else applied "$LBL" NO; fi
}

echo "real KB md5 (before): $(kbsum $R/knowledge_base); KB tree $(cd $R && git rev-parse HEAD:knowledge_base)"
echo "==== M0 pristine copy"
fresh; echo "copy KB md5: $(kbsum $K)"; gates M0

echo "==== M1 delete 1 prose sentence (atom ig34_p0008_a022, EXACT, unique in ch01_introduction.md) [same target as T0]"
fresh
mutate M1 chapters/ch01_introduction.md <<'PYEOF'
v = "The SDTMIG is best read online, so the reader can benefit from the many hyperlinks to internal and external references."
assert s.count(v) == 1, s.count(v); open(p, "w", encoding="utf-8").write(s.replace(v, "")); print("M1 deleted:", v[:60], "...")
PYEOF
gates M1

echo "==== M2 change 1 table value (PC/examples.md Example 1 Method C relrec row 5: IDVARVAL 4 -> 9) [same row as T0; located under its headings]"
fresh
mutate M2 domains/PC/examples.md <<'PYEOF'
old = "| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1 |"
e1 = [i for i, l in enumerate(L) if l.strip() == "### Example 1"]; e2 = [i for i, l in enumerate(L) if l.strip() == "### Example 2"]
assert len(e1) == 2 and len(e2) == 1, (e1, e2)          # 1st '### Example 1' = PC examples, 2nd = 6.3.5.9.3 worked examples
mc = [i for i in range(e1[1], e2[0]) if L[i].startswith("#### Method C")]; md = [i for i in range(e1[1], e2[0]) if L[i].startswith("#### Method D")]
assert len(mc) == 1 and len(md) == 1, (mc, md)
hit = [i for i in range(mc[0], md[0]) if L[i] == old]; assert len(hit) == 1, hit
i = hit[0]; L[i] = old.replace("| 4 |", "| 9 |"); open(p, "w", encoding="utf-8").write("\n".join(L)); print("M2 line", i + 1, ":", old, "->", L[i])
PYEOF
gates M2

echo "==== M2b move 1 value into an empty neighbour cell (PC/assumptions.md relrec row 1: MANY RELTYPE -> IDVARVAL) [same row as T0]"
fresh
mutate M2b domains/PC/assumptions.md <<'PYEOF'
old = "| 1 | ABC-123 | PC | | PCGRPID | | MANY | A |"
hit = [i for i, l in enumerate(L) if l == old]; assert len(hit) == 1, hit
i = hit[0]; L[i] = "| 1 | ABC-123 | PC | | PCGRPID | MANY | | A |"; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M2b line", i + 1, ":", old, "->", L[i])
PYEOF
gates M2b

echo "==== M2c change 1 value in a wrapped (multi-line) PDF record (PC/assumptions.md pc.xpt row 13 PCORRES 10 -> 11) [same row as T0]"
fresh
mutate M2c domains/PC/assumptions.md <<'PYEOF'
hit = [i for i, l in enumerate(L) if l.startswith("| 13 | ABC-123 | PC |") and l.count("| ANALYTE | 10 | ug/mL |") == 1]; assert len(hit) == 1, hit
i = hit[0]; L[i] = L[i].replace("| ANALYTE | 10 | ug/mL |", "| ANALYTE | 11 | ug/mL |"); open(p, "w", encoding="utf-8").write("\n".join(L)); print("M2c line", i + 1, ": PCORRES 10 -> 11")
PYEOF
gates M2c

echo "==== M2d delete 1 KB table row (PC/examples.md Example 1 Method D relrec row 20) [same row as T0]"
fresh
mutate M2d domains/PC/examples.md <<'PYEOF'
old = "| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 | | 2 |"
hit = [i for i, l in enumerate(L) if l == old]; assert len(hit) == 1, hit
i = hit[0]; del L[i]; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M2d deleted line", i + 1, "(row 20)")
PYEOF
gates M2d

echo "==== M3 delete 1 subsection (ch04 '#### 4.5.1.2 Tests Not Done' .. before '#### 4.5.1.3') [same subsection as T0]"
fresh
mutate M3 chapters/ch04_general_assumptions.md <<'PYEOF'
a = [i for i, l in enumerate(L) if l.startswith("#### 4.5.1.2 Tests Not Done")]; b = [i for i, l in enumerate(L) if l.startswith("#### 4.5.1.3")]
assert len(a) == 1 and len(b) == 1 and a[0] < b[0], (a, b)
n = b[0] - a[0]; del L[a[0]:b[0]]; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M3 deleted", n, "lines (4.5.1.2 heading..before 4.5.1.3), from line", a[0] + 1)
PYEOF
gates M3

# ── T1 false-OK modes (census only). Per case: v2 vs current-KB baseline must be RED and a targeted assert must find the
# mutated table/row/column (and it must be absent from the baseline); v1 is run against its own pristine-copy baseline, logged only.
M4SUM=""; M4BAD=0
tline() {  # 1-based line of the table header at / after the first line matching regex $2 in KB-copy file $1 (header = 2 lines above the first data row)
  $PY - "$K/$1" "$2" <<'PYEOF'
import re, sys
L = open(sys.argv[1], encoding="utf-8").read().split("\n"); hits = [i for i, l in enumerate(L) if re.search(sys.argv[2], l)]
assert len(hits) == 1, hits
i = hits[0]
while not L[i].lstrip().startswith("|"): i += 1
print(i + 1)
PYEOF
}
census_check() {  # report baseline kind args...  kind: cell FILE LINE KBROW COL | row FILE LINE KBROW | pdfonly DS EX |
                  #   only1 FILE LINE COL KBVAL | pairds FILE DS EX (every KB table FILE/DS/EX pairs with PDF example EX, none PDF_ONLY)
                  #   ok FILE LINE (table status OK)
  $PY - "$@" <<'PYEOF'
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
elif kind == "pairds":
    f, ds, ex = a
    ts = [t for t in R["tables"] if t["file"].endswith(f) and t.get("ds") == ds and t.get("ex") == ex]
    po = [p for p in R["pdf_only"] if p["ds"] == ds and p["ex"] == ex]
    ok = bool(ts) and all(t.get("pdf_ex") == ex and t["status"] in ("OK", "DIFF") for t in ts) and not po
    print("  assert pairds", f, ds, "ex", ex, "->", [(t["line"], t["status"], t.get("pdf_ex"), t.get("pdf_pages")) for t in ts], "| PDF_ONLY:", [p["pages"] for p in po])
elif kind == "ok":
    f, ln = a
    t = tab(R, f, ln) or {}; ok = t.get("status") == "OK"; print("  assert ok", f, ln, "->", t.get("status"), len(t.get("diffs", [])))
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
else:
    ok = False; print("  unknown assert kind", kind)
print("  ASSERT", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
PYEOF
}
# $1 label  $2 MB|EG|REL  $3.. assert spec ; optional second assert via M4EXTRA="kind args" (must also pass)
m4() {
  local LBL=$1 U=$2; shift 2; local CFG; CFG=$(cfg $U)
  echo "---- [$LBL] table_census v2 ($U)"
  $PY $T/scripts/table_census.py --kb-root "$K" $CFG --out "$S/m4_$LBL.json" --baseline "$B/census_mut_$U.v2.head.json" | grep -E "^(BASELINE|  CHANGED|RESULT)" | head -8
  local e2=${PIPESTATUS[0]}
  echo "---- [$LBL] targeted assert: $*"
  census_check "$S/m4_$LBL.json" "$B/census_mut_$U.v2.head.json" "$@"; local ea=$?
  if [ -n "${M4EXTRA:-}" ]; then echo "---- [$LBL] extra assert: $M4EXTRA"; census_check "$S/m4_$LBL.json" "$B/census_mut_$U.v2.head.json" $M4EXTRA || ea=1; fi
  echo "---- [$LBL] table_census v1 ($U, vs v1 pristine baseline)"
  $PY $V1 --kb-root "$K" $CFG --out "$S/m4v1_$LBL.json" --baseline "$S/v1base_$U.json" | grep -E "^(BASELINE|  CHANGED|RESULT)" | head -6
  local e1=${PIPESTATUS[0]}
  local ok=OK; { [ "$e2" = 1 ] && [ "$ea" = 0 ]; } || { ok=MISMATCH; M4BAD=1; }
  M4SUM+="$(printf '%-6s v2=%s(expect 1) assert=%s(expect 0) v1=%s %s' "$LBL" "$e2" "$ea" "$( [ "$e1" = 0 ] && echo GREEN-blind || echo RED )" "$ok")"$'\n'
}

echo "==== M4 setup: v1 baselines on a pristine copy; v2 vs current-KB baselines on the pristine copy must be GREEN"
fresh
for U in MB EG REL; do
  $PY $V1 --kb-root "$K" $(cfg $U) --out "$S/v1base_$U.json" >/dev/null
  $PY $T/scripts/table_census.py --kb-root "$K" $(cfg $U) --out "$S/m4_M0_$U.json" --baseline "$B/census_mut_$U.v2.head.json" | tail -1
  [ ${PIPESTATUS[0]} = 0 ] || { echo "M4 setup: $U not GREEN"; M4BAD=1; }
done
echo "---- [M4d0] real-KB pairing (mode d). T0 asserted the then-defect 'MB Ex3 relrec missing -> PDF Ex3 relrec PDF_ONLY';"
echo "     t0_mutation.md 6.3 said: once T2 adds the table, assert instead 'Ex1 relrec still pairs with Ex1, the new table pairs with Ex3'."
census_check "$S/m4_M0_MB.json" "$B/census_mut_MB.v2.head.json" pairds MB/examples.md relrec.xpt 1 || M4BAD=1
census_check "$S/m4_M0_MB.json" "$B/census_mut_MB.v2.head.json" pairds MB/examples.md relrec.xpt 3 || M4BAD=1

echo "==== M4a every KB copy checked (mode a). T0 target (second MB copy of Ex2 suppbe) was removed by D2 de-duplication."
echo "     Retargeted (main-controller decision, listed for owner ratification): PDF p431 relrec Ex1 has two KB copies (D7):"
echo "     chapters/ch08_relationships.md and domains/RELREC/examples.md. Mutate the ch08 copy only (row 2 RELTYPE MANY -> ONE)."
fresh
REL8=$(tline chapters/ch08_relationships.md '^### 8\.3\.1 RELREC Dataset Relationship Example')
RELD=$(tline domains/RELREC/examples.md '^\| 1 \| EFC1234 \| TU \| \| TULNKID \| \| ONE \| 1 \|$'); RELD=$((RELD - 2))
mutate M4a chapters/ch08_relationships.md <<'PYEOF'
old = "| 2 | EFC1234 | TR | | TRLNKID | | MANY | 1 |"
hit = [i for i, l in enumerate(L) if l == old]; assert len(hit) == 1, hit
i = hit[0]; L[i] = old.replace("| MANY |", "| ONE |"); open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4a ch08 line", i + 1, ":", old, "->", L[i])
PYEOF
echo "     ch08 table header line $REL8, RELREC copy table header line $RELD"
M4EXTRA="ok RELREC/examples.md $RELD" m4 M4a REL cell ch08_relationships.md $REL8 2 RELTYPE

echo "==== M4b swap 2 values inside a wrapped (multi-line) PDF record (mode b): EG/examples.md Ex3 row 1 EGCAT <-> EGPOS [same as T0]"
fresh
EGT=$(tline domains/EG/examples.md '^\| 1 \| STUDY01 \| EG \| 2324-P0001 \| 1 \| \.\.\. \| PRAG \|'); EGT=$((EGT - 2))
mutate M4b domains/EG/examples.md <<'PYEOF'
hit = [i for i, l in enumerate(L) if l.startswith("| 1 | STUDY01 |") and l.count("| INTERVAL | SUPINE |") == 1 and "| PRAG |" in l]; assert len(hit) == 1, hit
i = hit[0]; L[i] = L[i].replace("| INTERVAL | SUPINE |", "| SUPINE | INTERVAL |"); open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4b line", i + 1)
PYEOF
m4 M4b EG cell EG/examples.md $EGT 1 EGPOS

echo "==== M4b2 move a value into the empty neighbour cell of a wrapped record (mode b): same row, EGLEAD -> EGLOBXFL [same as T0]"
fresh
mutate M4b2 domains/EG/examples.md <<'PYEOF'
hit = [i for i, l in enumerate(L) if l.startswith("| 1 | STUDY01 |") and l.count("| LEAD II | | 2 |") == 1 and "| PRAG |" in l]; assert len(hit) == 1, hit
i = hit[0]; L[i] = L[i].replace("| LEAD II | | 2 |", "| | LEAD II | 2 |"); open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4b2 line", i + 1)
PYEOF
m4 M4b2 EG cell EG/examples.md $EGT 1 EGLOBXFL

echo "==== M4c duplicate KB row number (mode c): EG Ex3, wrong copy of row 5 inserted before row 5 [same as T0]"
fresh
mutate M4c domains/EG/examples.md <<'PYEOF'
hit = [i for i, l in enumerate(L) if l.startswith("| 5 | STUDY01 |") and l.count("| 176 | msec | 176 | 176 |") == 1]; assert len(hit) == 1, hit
i = hit[0]; L.insert(i, L[i].replace("| 176 | msec | 176 | 176 |", "| 999 | msec | 999 | 999 |")); open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4c inserted before line", i + 1)
PYEOF
m4 M4c EG row EG/examples.md $EGT 5

echo "==== M4c2 row alignment by content (mode c): EG Ex3 extra KB row after row 10, later rows renumbered +1, one real change"
echo "     (row 20 -> 21 EGORRES 402 -> 403). Only that one non-Row cell may be reported (no cascade), plus 1 unmatched row. [same as T0]"
fresh
mutate M4c2 domains/EG/examples.md <<'PYEOF'
r1 = [i for i, l in enumerate(L) if l.startswith("| 1 | STUDY01 |") and "| PRAG |" in l]; assert len(r1) == 1, r1
b = r1[0] - 1                                             # L[b + n] = table row n
assert L[b + 10].startswith("| 10 | STUDY01 |") and L[b + 24].startswith("| 24 | STUDY01 |") and L[b + 20].count("| 402 | msec | 402 | 402 |") == 1
L[b + 20] = L[b + 20].replace("| 402 | msec | 402 | 402 |", "| 403 | msec | 402 | 402 |")
for i in range(b + 11, b + 25):
    L[i] = re.sub(r"^\| (\d+) \|", lambda m: f"| {int(m.group(1)) + 1} |", L[i])
L.insert(b + 11, "| 11 | STUDY01 | EG | 2324-P0001 | 11 | ... | XXAG | XX Interval, Aggregate | INTERVAL | SUPINE | 123 | msec | 123 | 123 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |")
open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4c2 applied; table row 1 at line", b + 2)
PYEOF
m4 M4c2 EG only1 EG/examples.md $EGT EGORRES 403

echo "==== M4e KB row shorter than its header (dropped last cell): EG Ex3 row 1 loses EGREPNUM [same as T0]"
fresh
mutate M4e domains/EG/examples.md <<'PYEOF'
hit = [i for i, l in enumerate(L) if l.startswith("| 1 | STUDY01 |") and "| PRAG |" in l and l.endswith("| ... | 1 |")]; assert len(hit) == 1, hit
i = hit[0]; L[i] = L[i][: -len(" 1 |")]; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4e line", i + 1)
PYEOF
m4 M4e EG row EG/examples.md $EGT 1

echo "==== M4d pairing by example + dataset (mode d): delete every KB copy of MB Ex2 suppbe.xpt -> PDF table must be PDF_ONLY"
echo "     [same table as T0; T0 deleted two copies, D2 left one]"
fresh
mutate M4d domains/MB/examples.md <<'PYEOF'
e2 = [i for i, l in enumerate(L) if l.strip() == "### Example 2"]; e3 = [i for i, l in enumerate(L) if l.strip() == "### Example 3"]
assert len(e2) == 1 and len(e3) == 1, (e2, e3)
m = [i for i in range(e2[0], e3[0]) if L[i] == "**suppbe.xpt**"]; assert len(m) == 1, m
j = m[0] + 1
while not L[j].startswith("|"): j += 1
k = j
while k < len(L) and L[k].startswith("|"): k += 1
assert L[k - 1].startswith("| 6 |"), L[k - 1][:40]
del L[m[0]:k]; open(p, "w", encoding="utf-8").write("\n".join(L)); print("M4d deleted lines", m[0] + 1, "-", k)
PYEOF
m4 M4d MB pdfonly suppbe.xpt 2

echo "==== RESTORE (fresh copy of the unmodified KB)"
fresh; echo "copy KB md5: $(kbsum $K)"; gates RESTORE

echo "real KB md5 (after): $(kbsum $R/knowledge_base); KB tree $(cd $R && git rev-parse HEAD:knowledge_base)"
echo "git status knowledge_base/ archive/ releases/:"; (cd $R && git status --short knowledge_base archive releases; echo "(end)")
echo "==== MUTATIONS APPLIED (a case whose mutation was not applied is a MISMATCH)"; printf '%s' "$APPLIED"
echo "==== EXPECT TABLE (fp census t3)"; printf '%s' "$SUMMARY"
echo "==== M4 TABLE (census v2 RED + targeted assert; v1 logged)"; printf '%s' "$M4SUM"
echo "---- RESTORE census v2 MB/EG/REL vs baselines (must be GREEN)"
R1=0
for U in MB EG REL; do $PY $T/scripts/table_census.py --kb-root "$K" $(cfg $U) --out "$S/m4_RESTORE_$U.json" --baseline "$B/census_mut_$U.v2.head.json" | tail -1; [ ${PIPESTATUS[0]} = 0 ] || R1=1; done
[ "$R1" = 0 ] || { echo "RESTORE M4 census not GREEN"; MISMATCH=1; }
[ "$M4BAD" = 0 ] || MISMATCH=1
if [ "$MISMATCH" = 0 ]; then echo "MUTATION RESULT: ALL MATCH (exit 0)"; exit 0; else echo "MUTATION RESULT: MISMATCH (exit 1)"; exit 1; fi
