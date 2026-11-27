#!/usr/bin/env python3
"""One-off fixation (T4 第二轮改台账 R2L, 规格 subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md §1/§2):
write work/t4_r2l_relabel.json from work/t4/supp/relabel_pending.json (the 78 entries of groups R1-row / v2.0-TOC /
registered-typo / registered-typo-oos; group typo-overlabel is NOT taken: the owner has not answered).
Each relabel entry: atom_id / group / now / to / raw (reviewer raw result file:line) / decision (owner 2026-11-27).
PDF_TYPO entries carry their registry id; the 6 out-of-scope ones also carry keep-style pdf / kb line + token
(re-asserted at run time by t3_errata_build.py, like the U-8 keep list). registry_ptr: extra registry ids on the
decision-table evidence of atoms whose label stays PDF_TYPO (§2 item 3; pointer only).
Run once; afterwards the JSON is the source. Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_r2l_build.py
"""
import json, os
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
W = f"{TB}/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
REG = {r["id"] for r in lj(f"{W}/t2_pdf_typo_registry.jsonl")}
OC = "evidence/checkpoints/t4_owner_confirmation.md 第二轮"
DEC = {"R1-row": f"owner 2026-11-27: {OC} (问题 1 = A)", "v2.0-TOC": f"owner 2026-11-27: {OC} (问题 2 = A)",
       "registered-typo": f"owner 2026-11-27 问题 3 = A ({OC})", "registered-typo-oos": f"owner 2026-11-27 问题 7b = A ({OC})"}
# out-of-scope 6 (问题 7b): PDF line holds the registered typo, KB line holds the corrected value (raw: evidence/t4_round3_raw/pack_13_14.md)
KEEP = {"ig34_p0083_a020": ("ig34_p0083:39", "birthdtc", "knowledge_base/domains/SE/examples.md:79", "brthdtc"),
        "ig34_p0304_a026": ("ig34_p0304:29", "occular", "knowledge_base/domains/OE/examples.md:142", "ocular comfort"),
        "ig34_p0304_a027": ("ig34_p0304:32", "occular", "knowledge_base/domains/OE/examples.md:143", "ocular comfort"),
        "ig34_p0304_a028": ("ig34_p0304:35", "occular", "knowledge_base/domains/OE/examples.md:144", "ocular comfort"),
        "ig34_p0304_a029": ("ig34_p0304:38", "occular", "knowledge_base/domains/OE/examples.md:145", "ocular comfort"),
        "ig34_p0316_a023": ("ig34_p0316:46", "laterallity", "knowledge_base/domains/PE/spec.md:174", "detailing laterality.")}
# §2 item 3: registry ids missing from the evidence of atoms that stay PDF_TYPO (reviewer raw results)
PTR = {"ig34_p0355_a027": (["B-TR T-1"], "evidence/t4_round2_raw/pack_typo_2.md:50"),
       "ig34_p0356_a001": (["B-TR T-1"], "evidence/t4_round3_raw/pack_10.md:57"),
       "ig34_p0198_a014": (["REG BS N-1"], "evidence/t4_round3_raw/pack_8.md:54"),
       "ig34_p0206_a009": (["S-SPC1 CP T-16a"], "evidence/t4_round3_raw/pack_8.md:54"),
       "ig34_p0263_a020": (["B-MB T-2"], "evidence/t4_round3_raw/pack_8.md:54")}

def raw_ok(p):
    f, n = p.rsplit(":", 1)
    return os.path.exists(f"{TB}/{f}") and int(n) <= len(open(f"{TB}/{f}", encoding="utf-8").read().splitlines())

src = [x for x in json.load(open(f"{W}/t4/supp/relabel_pending.json")) if x["group"] in DEC]
assert len(src) == 78, len(src)
rel = {}
for x in src:
    e = dict(group=x["group"], now=x["now"], to=x["to"], raw=x["raw"], decision=DEC[x["group"]])
    assert raw_ok(x["raw"]), x
    if x["to"] == "PDF_TYPO":
        assert x["registry"] in REG, x
        e["registry"] = [x["registry"]]
        if x["group"] == "registered-typo-oos":
            pl, pt, kl, kt = KEEP[x["atom_id"]]
            e.update(pdf=dict(line=pl, token=pt), kb=dict(line=kl, token=kt))
    rel[x["atom_id"]] = e
assert set(KEEP) == {i for i, e in rel.items() if e["group"] == "registered-typo-oos"}
for i, (ids, raw) in PTR.items():
    assert all(r in REG for r in ids) and raw_ok(raw) and i not in rel, i
out = {"_note": "T4 第二轮改台账 R2L (主人 2026-11-27 直接决定 1A / 2A / 3A / 7b-A; evidence/checkpoints/t4_owner_confirmation.md 第二轮). "
                "relabel: 78 条 (IE 53 → t3_writeback.py 规则 T4-R2L-owner-IE; PDF_TYPO 25 → t3_errata_build.py atom_err R2). "
                "registry_ptr: 只补决策表登记指针, 标签不变. typo-overlabel 4 条主人未答, 不在本清单. 生成: scripts/t4/t4_r2l_build.py (一次性).",
       "relabel": dict(sorted(rel.items())),
       "registry_ptr": {i: dict(add=ids, raw=raw) for i, (ids, raw) in sorted(PTR.items())}}
json.dump(out, open(f"{W}/t4_r2l_relabel.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
import collections
print("relabel", len(rel), dict(collections.Counter((e["group"], e["to"]) for e in rel.values())), "| registry_ptr", len(PTR))
