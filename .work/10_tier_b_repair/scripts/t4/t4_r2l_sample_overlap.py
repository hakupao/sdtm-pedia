#!/usr/bin/env python3
"""Read-only. Which already-judged samples are touched by the R2L ledger batch?

Compares the pre-R2L backup ledger (the state at gate attempt 2) with the working ledger (after R2L and R3L) (positional, pdf_atom_id asserted equal), then intersects
(a) rows whose verdict changed and (b) rows changed in other fields only, with every sample file a reviewer or the owner
has judged: the gate sample (84), the T4.2 human sample (prescreen 42, owner's 6 among them), and the supplementary /
Q9 / round-2 / round-3 samples. Also prints the change set by from -> to and the PDF_TYPO ack sources.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_r2l_sample_overlap.py
"""
import collections
import json

T = ".work/10_tier_b_repair"
W = f"{T}/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
pre, cur = lj(f"{W}/coverage_ledger.wc.pre_r2l.jsonl"), lj(f"{W}/coverage_ledger.wc.jsonl")
assert len(pre) == len(cur) == 12492 and all(a["pdf_atom_id"] == b["pdf_atom_id"] for a, b in zip(pre, cur))
label = {a["pdf_atom_id"]: (a["verdict"], b["verdict"]) for a, b in zip(pre, cur) if a["verdict"] != b["verdict"]}
other = sorted(a["pdf_atom_id"] for a, b in zip(pre, cur) if a["verdict"] == b["verdict"] and a != b)
print("rows", len(cur), "| label changed", len(label), "| other fields only", len(other), other)
for (f, t), n in sorted(collections.Counter(label.values()).items()):
    print(f"  {f} -> {t}: {n}")
rel = json.load(open(f"{W}/t4_r2l_relabel.json", encoding="utf-8"))
r3l = json.load(open(f"{W}/t4_r3l_relabel.json", encoding="utf-8"))["relabel"]
listed = {**rel["relabel"], **r3l}
ids = set(listed)
print("changed set == work/t4_r2l_relabel.json + work/t4_r3l_relabel.json 'relabel' lists:", set(label) == ids, f"({len(rel['relabel'])} + {len(r3l)} listed);",
      "direction as listed:", all(label[a] == (e["now"], e["to"]) for a, e in listed.items() if a in label))
mid = lj(f"{W}/coverage_ledger.wc.pre_r3l.jsonl")
r3_changed = {a["pdf_atom_id"]: (a["verdict"], b["verdict"]) for a, b in zip(mid, cur) if a["verdict"] != b["verdict"]}
print("R3L batch alone (pre_r3l backup vs working ledger): label changed", len(r3_changed), r3_changed, "| other rows byte-identical:",
      sum(1 for a, b in zip(mid, cur) if a != b) == len(r3_changed), "| == R3L list:", set(r3_changed) == set(r3l))
print("other-fields-only set == 'registry_ptr' list:", set(other) == set(rel["registry_ptr"]))

OWNER6 = ["ig34_p0011_a018", "sv20_p0004_a013", "ig34_p0055_a026", "ig34_p0295_a021", "ig34_p0171_a0002", "ig34_p0209_a006"]
hv = open(f"{T}/evidence/checkpoints/t4_human_verdicts.md", encoding="utf-8").read()
assert all(f"`{a}`" in hv for a in OWNER6), "owner's six differ from t4_human_verdicts.md"
SAMPLES = [("gate sample (attempt 1 / 2; 84)", f"{W}/t4/gate_sample.jsonl"),
           ("T4.2 human sample (prescreen 42)", f"{W}/t4/human_sample.jsonl"),
           ("supplementary check (203)", f"{W}/t4/supp/supp_sample.jsonl"),
           ("Q9 extension (192)", f"{W}/t4/q9/q9_sample.jsonl"),
           ("round 2 (135)", f"{W}/t4/round2/round2_sample.jsonl"),
           ("round 2b (40)", f"{W}/t4/round2/round2b_sample.jsonl"),
           ("round 3 (315)", f"{W}/t4/round3/round3_sample.jsonl")]
print("\nsample | n | label-changed in it | other-fields-only in it")
for name, p in SAMPLES:
    s = [r["atom_id"] for r in lj(p)]
    hit, oth = [a for a in s if a in label], [a for a in s if a in other]
    print(f"{name} | {len(s)} | {len(hit)} | {len(oth)}")
    for a in hit:
        print(f"    {a}: {label[a][0]} -> {label[a][1]}")
    for a in oth:
        print(f"    {a}: (pointer fields only)")
print("owner's 6 (t4_human_verdicts.md) | label-changed:", [a for a in OWNER6 if a in label], "| other-fields-only:", [a for a in OWNER6 if a in other])

ack = open(f"{T}/evidence/checkpoints/t4_ack_lists.md", encoding="utf-8").read()
print("\nt4_ack_lists.md: '(未归因)' occurrences =", ack.count("(未归因)"))
fin = collections.Counter(r["verdict"] for r in cur)
print("final:", {k: fin[k] for k in ("EXACT", "EQUIVALENT", "INTENTIONAL_EXCLUDE", "ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED", "PARTIAL", "MISPLACED", "ERROR")})
reg = lj(f"{W}/t2_pdf_typo_registry.jsonl")
print("registry rows", len(reg), "| handling:", dict(collections.Counter(r.get("handling") for r in reg)))
UNANSWERED = ["ig34_p0412_a006", "ig34_p0412_a007", "ig34_p0412_a008", "ig34_p0413_a010", "ig34_p0293_a038"]
print("question A x4 (owner: A1 -> EXACT) and question B x1 (owner: B1 -> stays PDF_TYPO) now:", {a: [r["verdict"] for r in cur if r["pdf_atom_id"] == a] for a in UNANSWERED})
