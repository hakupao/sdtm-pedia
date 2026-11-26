#!/usr/bin/env python3
"""T3 attempt 1 -> attempt 2 per-atom diff (audit re-checks only changed layers) -> work/t3_attempt2_diff.jsonl.
attempt-1 decisions are frozen in work/t3_attempt1/t3_writeback_decisions.attempt1.json (copy of the attempt-1 output,
also archived gz under evidence/failures/t3_attempt_1/).
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_attempt_diff.py [--prev <decisions.json>] [--out <diff.jsonl>]
  attempt 3: --prev work/t3_attempt2/t3_writeback_decisions.attempt2.json --out work/t3_attempt3_diff.jsonl
"""
import collections, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import W
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--prev", default=f"{W}/t3_attempt1/t3_writeback_decisions.attempt1.json")
ap.add_argument("--out", default=f"{W}/t3_attempt2_diff.jsonl")
args = ap.parse_args()
D1 = json.load(open(args.prev))
D2 = json.load(open(f"{W}/t3_writeback_decisions.json"))
ER = json.load(open(f"{W}/t3_errata.json"))
R = json.load(open(f"{W}/t3_rules.json"))
K4 = set(ER.get("k4", {}).get("to_R2", {}))
out = []
for i in sorted(set(D1) | set(D2)):
    a, b = D1.get(i), D2.get(i)
    av, bv = (a or {}).get("new", "(not in allowed set)"), (b or {}).get("new", "(not in allowed set)")
    ah, bh = (a or {}).get("evidence", {}).get("hit_file"), (b or {}).get("evidence", {}).get("hit_file")
    ar, br = (a or {}).get("rule"), (b or {}).get("rule")
    if av == bv and ah == bh and ar == br:
        continue
    if a is None:
        layer = "K3b allowed-set extension (registry-driven)" if br == "K3b-registry" else "allowed-set extension"
    elif br == "K3b-registry":
        layer = "K3b registry-driven PDF_TYPO"
    elif br == "C7-atom-not-in-PDF":
        layer = "C7 atom ∉ PDF -> ATOM_ERR"
    elif i in K4:
        layer = "K4 R1->R2"
    elif br and ("C7" in br or "deltaRereview" in br):
        layer = "C7 delta re-review"
    elif br == "writer-Tn-registry" and ar != br:
        layer = "K3 T-n from ref"
    elif av == "EXACT" and bv != "EXACT":
        layer = "K11 surplus" if b["evidence"].get("k11_surplus") else "K1 boundary/anchor demote"
    elif bv == "EXACT" and av != "EXACT":
        layer = "K1 targets/anchor (new EXACT)"
    elif av == bv == "EXACT":
        layer = "K1 re-target (tier/boundary)"
    else:
        layer = "rule change"
    out.append(dict(atom_id=i, layer=layer, a1=dict(verdict=av, rule=ar, hit_file=ah), a2=dict(verdict=bv, rule=br, hit_file=bh,
               hit_lines=(b or {}).get("evidence", {}).get("hit_lines"))))
with open(args.out, "w", encoding="utf-8") as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("diff rows:", len(out))
for k, n in collections.Counter(r["layer"] for r in out).most_common():
    print(f"  {k}: {n}")
print("verdict transitions:", dict(collections.Counter((r["a1"]["verdict"], r["a2"]["verdict"]) for r in out if r["a1"]["verdict"] != r["a2"]["verdict"])))
