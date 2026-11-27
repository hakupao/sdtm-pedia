#!/usr/bin/env python3
"""T4.1 attempt-2 gap: full check (no sampling) of the classes the gate samples never reached.
Layers (each atom goes to the first layer it matches, in this order):
  PRE_EXISTING  : stock EXACT rows inside §5.0 whose text has no valid fingerprint hit at HEAD nor at 302ec4c
                  (bucket 'pre_existing' of scripts/t3/t3_direct_hit.py, re-run at HEAD -> work/t4/supp/direct_hit_head.json)
  FIG           : final verdict FIGURE_DEFERRED (= triage class FIGURE)
  TRIAGE_ATOM_ERR / TRIAGE_RELOCATE / TRIAGE_LOCATE : triage final_class
  RULE_<rule>   : t3_writeback_decisions rule in RULES below
Excluded: atoms already judged by the T4.1 gate reviewers (work/t4/gate_sample.jsonl) or by the U-5 C7 full check
(work/t4/u5_c7_38.jsonl); the overlap is printed.
Reuses the row builders of t4_sample.py / the block renderer of t4_render.py by exec-ing only their definition part
(both scripts write work/t4/{gate,human}_sample.jsonl / t4_human_sample.md at module level and must NOT be re-run).
Writes only under work/t4/supp/. Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_sample.py
"""
import collections, hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(os.path.dirname(HERE))
OUT = f"{TB}/work/t4/supp"
RULES = ["T1-two-agent+T2-rework", "T2-fix+deltaRereviewPASS+auditPASS", "live-hit(was-IE-ack)", "C1-manual-PDF+KB",
         "C7-K4-rereview", "T1-two-agent"]
PACKS = [("1", ["PRE_EXISTING"], 0, 29), ("2", ["PRE_EXISTING"], 29, 58),
         ("3", ["TRIAGE_ATOM_ERR"], 0, 25), ("4", ["TRIAGE_ATOM_ERR"], 25, 50), ("5", ["TRIAGE_ATOM_ERR"], 50, 999),
         ("6", ["FIG", "TRIAGE_RELOCATE", "TRIAGE_LOCATE", "RULE_C1-manual-PDF+KB", "RULE_C7-K4-rereview",
                "RULE_T2-fix+deltaRereviewPASS+auditPASS", "RULE_T1-two-agent"], 0, 999),
         ("7", ["RULE_T1-two-agent+T2-rework"], 0, 999), ("8", ["RULE_live-hit(was-IE-ack)"], 0, 999)]


def defs_only(path, marker):
    src = open(path, encoding="utf-8").read()
    assert src.count(marker) == 1, (path, marker, src.count(marker))
    return src.split(marker)[0]


S = {"__file__": f"{HERE}/t4_sample.py", "__name__": "t4_sample_defs"}
exec(compile(defs_only(f"{HERE}/t4_sample.py", "\ncls = lambda c:"), f"{HERE}/t4_sample.py", "exec"), S)
R = {"__name__": "t4_render_defs"}
exec(compile(defs_only(f"{HERE}/t4_render.py", '\ngate = lj(f"{TB}/work/t4/gate_sample.jsonl")'), f"{HERE}/t4_render.py", "exec"), R)
lj, L, T, D, W = S["lj"], S["L"], S["T"], S["D"], S["W"]

done_gate = {g["atom_id"] for g in lj(f"{W}/t4/gate_sample.jsonl")}
done_c7 = {g["atom_id"] for g in lj(f"{W}/t4/u5_c7_38.jsonl")}
layers = collections.OrderedDict()
layers["PRE_EXISTING"] = json.load(open(f"{OUT}/direct_hit_head.json"))["pre_existing"]
layers["FIG"] = [i for i, r in L.items() if r["verdict"] == "FIGURE_DEFERRED"]
for c in ("ATOM_ERR", "RELOCATE", "LOCATE"):
    layers[f"TRIAGE_{c}"] = [i for i, t in T.items() if t["final_class"] == c]
for r in RULES:
    layers[f"RULE_{r}"] = [i for i, d in D.items() if d.get("rule") == r]

seen, rows, pop = set(), collections.OrderedDict(), []
for name, ids in layers.items():
    ids = sorted(set(ids))
    keep = [i for i in ids if i not in seen and i not in done_gate and i not in done_c7]
    pop.append(dict(layer=name, population=len(ids), in_gate=sorted(set(ids) & done_gate), in_c7=sorted(set(ids) & done_c7),
                    in_earlier_layer=sorted(set(ids) & seen), checked_here=keep,
                    final=dict(collections.Counter(L[i]["verdict"] for i in ids))))
    seen |= set(ids)
    rows[name] = [S["refine_human"](S["row"](i, f"supp:{name}")) for i in keep]
    print(f"{name:45s} population {len(ids):3d} | gate {len(set(ids) & done_gate)} | C7 {len(set(ids) & done_c7)} | "
          f"earlier layer {pop[-1]['in_earlier_layer'].__len__()} | checked here {len(keep)} | final {pop[-1]['final']}")
flat = [x for v in rows.values() for x in v]
with open(f"{OUT}/supp_sample.jsonl", "w", encoding="utf-8") as fh:
    for x in flat:
        fh.write(json.dumps(x, ensure_ascii=False) + "\n")
json.dump(pop, open(f"{OUT}/supp_population.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

n = 0
for pid, names, lo, hi in PACKS:
    part = [x for nm in names for x in rows[nm]][lo:hi]
    out = [f"# T4.1 补检包 {pid}/8 — {' + '.join(names)} ({len(part)} 条, 全检, 不抽样)", "",
           "> 由 `scripts/t4/t4_supp_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续.", ""]
    for x in part:
        n += 1
        out += R["block"](x, n)
    open(f"{OUT}/supp_pack_{pid}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
assert n == len(flat), (n, len(flat))
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
print(f"total checked {len(flat)} (union {len(seen)}); supp_sample.jsonl md5 {md5(f'{OUT}/supp_sample.jsonl')}; "
      f"supp_population.json md5 {md5(f'{OUT}/supp_population.json')}")
for x in flat:
    if x["pdf"]["score"] < 0.8 or x["kb"]["src"] == "none":
        print("weak:", x["layer"], x["atom_id"], x["verdict_final"], "pdf", x["pdf"]["score"], "kb", x["kb"]["src"])
