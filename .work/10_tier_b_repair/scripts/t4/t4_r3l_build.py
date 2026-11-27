#!/usr/bin/env python3
"""One-off fixation (T4 问题 A 改台账 R3L, 规格 subagent_prompts/t4/t4_round3_ledger_spec_v1.0.md §1):
1. write work/t4_r3l_relabel.json from work/t4/supp/relabel_pending.json (group typo-overlabel, 4 entries).
   Each entry: group / now / to / raw (reviewer raw result file:line) / why / decision (owner 2026-11-27 问题 A = A1) /
   k3b_drop = the registry ids whose K3b touch on this atom the reviewers rejected (taken from the atom's
   keep_k3b entry in work/t3_k3b_out_of_scope_keep.json, which is how the atom became PDF_TYPO).
2. mark those keep-list entries: action keep_k3b -> t4_r3l_drop, field t4_r3l_fix records before -> after.
Idempotent. Run once; afterwards the two JSON files are the source (t3_writeback.py reads them).
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_r3l_build.py
"""
import json, os
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
W = f"{TB}/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
REG = {r["id"] for r in lj(f"{W}/t2_pdf_typo_registry.jsonl")}
DEC = "owner 2026-11-27 问题 A = A1 (evidence/checkpoints/t4_owner_confirmation.md 消息 4)"
SPEC = "subagent_prompts/t4/t4_round3_ledger_spec_v1.0.md §1"
KEEPF = f"{W}/t3_k3b_out_of_scope_keep.json"

def raw_ok(p):
    f, n = p.rsplit(":", 1)
    return os.path.exists(f"{TB}/{f}") and int(n) <= len(open(f"{TB}/{f}", encoding="utf-8").read().splitlines())

src = [x for x in json.load(open(f"{W}/t4/supp/relabel_pending.json")) if x["group"] == "typo-overlabel"]
assert len(src) == 4 and all(x["now"] == "PDF_TYPO" and x["to"] == "EXACT" and raw_ok(x["raw"]) for x in src), src
keep = json.load(open(KEEPF, encoding="utf-8"))
rel = {}
for x in src:
    i, k = x["atom_id"], keep[x["atom_id"]]
    assert k["action"] in ("keep_k3b", "t4_r3l_drop") and k["registry"] and set(k["registry"]) <= REG, (i, k)
    rel[i] = dict(group=x["group"], now=x["now"], to=x["to"], raw=x["raw"], why=x["why"], decision=DEC,
                  k3b_drop=sorted(set(k["registry"])), k3b_rule=k["rule"])
    if k["action"] == "keep_k3b":
        k["action"] = "t4_r3l_drop"
        k["t4_r3l_fix"] = dict(action=dict(before="keep_k3b", after="t4_r3l_drop"), decision=DEC, raw=x["raw"], spec=SPEC,
                               basis="两位独立审查者: 登记笔误不在这条原子里 (在相邻原子 / 另一张表), 原子 KB 与 PDF 逐字一致; "
                                     "K3b 对它的触及作废 (t3_writeback.py 读 work/t4_r3l_relabel.json 剔除), 由 live-hit 判 EXACT")
if "R3L" not in keep["_note"]:
    n = lambda a: sum(v.get("action") == a for k, v in keep.items() if not k.startswith("_"))
    keep["_note"] += (f" | T4 问题 A 改台账 R3L (2026-11-27, 主人 A1): {' / '.join(sorted(rel))} 由 keep_k3b 改为 t4_r3l_drop "
                      f"(K3b 触及作废, 见 work/t4_r3l_relabel.json); 现 keep_k3b {n('keep_k3b')} / t4_r3l_drop {n('t4_r3l_drop')} / t4_only {n('t4_only')}.")
out = dict(_note="T4 问题 A 改台账 R3L (主人 2026-11-27 直接回答 A1; evidence/checkpoints/t4_owner_confirmation.md 消息 4). "
                 "relabel: 4 条 PDF_TYPO → EXACT. k3b_drop = 被审查者否定的 K3b 触及 (登记 id); t3_writeback.py 在 K3b 扫描之后剔除这些触及, "
                 "原子进允许集, 由现有 live-hit 路径判定 (断言 rule = live-hit, 终态 = to). 对应 keep 清单条目 action 改为 t4_r3l_drop. "
                 "生成: scripts/t4/t4_r3l_build.py (一次性).",
           relabel=dict(sorted(rel.items())))
json.dump(out, open(f"{W}/t4_r3l_relabel.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(keep, open(KEEPF, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("r3l relabel", len(rel), "| keep t4_r3l_drop", sum(v.get("action") == "t4_r3l_drop" for k, v in keep.items() if not k.startswith("_")))
