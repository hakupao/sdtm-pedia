#!/usr/bin/env python3
"""Read-only: does every final ATOM_ERR / PDF_TYPO atom have its own verdict row in the raw output of an independent
T4 review? Scans the reviewers' result tables (a row whose first cells hold the atom id and a verdict word).
Also prints the coverage numbers for the scenarios of the add-on check on in-memory copies of the ledger
(no ledger is written). Since the R4L batch the scenarios are computed on the pre-R4L backup
(the ledger the check was done on) and the working ledger is printed as it is now. Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_coverage.py
"""
import collections, glob, hashlib, json, os

TB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LED = f"{TB}/work/coverage_ledger.wc.pre_r4l.jsonl"   # the ledger the add-on check was done on (before the R4L batch)
WORK = f"{TB}/work/coverage_ledger.wc.jsonl"
rows = [json.loads(l) for l in open(LED, encoding="utf-8") if l.strip()]
L = {r["pdf_atom_id"]: r for r in rows}
RAW = ["evidence/t4_gate_raw/pack[1-4].md", "evidence/t4_supp_raw/pack_*.md", "evidence/t4_q9_raw/pack_*.md",
       "evidence/t4_round2_raw/pack_*.md", "evidence/t4_round3_raw/pack_*.md", "evidence/t4_gate_raw/attempt3_report.md",
       "evidence/t4_gate_raw/attempt3_delta_report.md", "evidence/checkpoints/t4_human_prescreen.md",
       "evidence/checkpoints/t4_human_prescreen_postthaw.md", "evidence/checkpoints/t4_u5_c7_fullcheck.md",
       "evidence/checkpoints/t4_round2_ledger_audit.md", "evidence/t4_atomerr_raw/pack_*.md"]
V = ("HOLDS_AS_EQUIV", "NOT_HOLD", "HOLDS", "UNVERIFIABLE", "TYPO_AFFECTED", "NOT_AFFECTED", "内容正确", "内容错误", "看不出",
     "成立", "不成立")
seen = collections.defaultdict(list)
for pat in RAW:
    for f in sorted(glob.glob(f"{TB}/{pat}")):
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            if not line.startswith("|"):
                continue
            cells = [c.strip().strip("`*") for c in line.replace("\\|", "/").split("|")]
            ids = [c for c in cells[1:4] if c in L]
            v = next((v for c in cells[2:8] for v in V if c.replace("*", "").strip().startswith(v)), None)
            if ids and v:
                seen[ids[0]].append((os.path.relpath(f, TB).split("/")[1], n, v))
for lab in ("ATOM_ERR", "PDF_TYPO"):
    ids = [i for i, r in L.items() if r["verdict"] == lab]
    miss = [i for i in ids if i not in seen]
    src = collections.Counter(seen[i][0][0] for i in ids if i in seen)
    print(f"{lab} {len(ids)}: with a verdict row {len(ids) - len(miss)}, without {len(miss)} {miss}; first source {dict(src)}")

COV, NEW, IE = {"EXACT", "EQUIVALENT", "PARTIAL", "MISPLACED"}, {"ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED"}, "INTENTIONAL_EXCLUDE"
C1 = ["ig34_p0124_a001"]
CE = [i for i, r in L.items() if r["verdict"] == "ATOM_ERR" and r["matched_by"]["evidence"].get("registry") == ["B-CE T-2"]]


def nums(flip, to):
    v = [to if r["pdf_atom_id"] in flip else r["verdict"] for r in rows]
    den = sum(1 for x in v if x != IE)
    den_m = sum(1 for x in v if x != IE and x not in NEW)
    cov = sum(1 for x in v if x in COV)
    b = cov + sum(1 for x in v if x in ("ATOM_ERR", "PDF_TYPO"))
    c = sum(1 for x in v if x in ("EXACT", "EQUIVALENT"))
    n = collections.Counter(v)
    return (f"U-1 B {b}/{den} = {b / den * 100:.4f}% | strict {cov}/{den} = {cov / den * 100:.4f}% | mapped {cov}/{den_m} = "
            f"{cov / den_m * 100:.4f}% | content {c}/{den_m} = {c / den_m * 100:.4f}% | EXACT {n['EXACT']} ATOM_ERR {n['ATOM_ERR']} PDF_TYPO {n['PDF_TYPO']}")


assert len(CE) == 8 and all(L[i]["verdict"] == "ATOM_ERR" for i in C1)
print("before R4L (checked ledger):", nums(set(), None))
print("C1 (1 -> EXACT)           :", nums(set(C1), "EXACT"))
print("B-CE 8 -> EXACT           :", nums(set(CE), "EXACT"))
print("B-CE 8 -> PDF_TYPO        :", nums(set(CE), "PDF_TYPO"))
print("C1 + B-CE 8 -> EXACT      :", nums(set(C1) | set(CE), "EXACT"))
print("B-CE atoms:", sorted(CE))
rows = [json.loads(l) for l in open(WORK, encoding="utf-8") if l.strip()]
print("working ledger now        :", nums(set(), None))
print("B-CE 8 in the working ledger:", sorted({r["verdict"] for r in rows if r["pdf_atom_id"] in set(CE)}), "| C1 atom:", [r["verdict"] for r in rows if r["pdf_atom_id"] in C1])
print("md5: checked ledger", hashlib.md5(open(LED, "rb").read()).hexdigest(), "| working ledger", hashlib.md5(open(WORK, "rb").read()).hexdigest())
