#!/usr/bin/env python3
"""PLAN Q9 escalation (triggered by 2 NOT_HOLD in the PRE_EXISTING layer of the T4.1 supplementary full check):
old 06 labels that this project never touched ("stock": in §5.0 scope, non-HEADING, not in t3_writeback_decisions).
  stock EXACT      : already fingerprint-rechecked in full by scripts/t3/t3_direct_hit.py (misses = PRE_EXISTING, all reviewed).
  Q9_SV20_EQUIV    : every stock EQUIVALENT atom from SDTM v2.0 (full check; the failure mode found is v2.0 table rows).
  Q9_IG34_EQUIV    : seeded stratified sample of the stock EQUIVALENT atoms from SDTMIG v3.4 (allocation in ALLOC).
Atoms already judged by the T4.1 gate reviewers are excluded and counted. Same row builders / renderer as the gate packs
(definition part of t4_sample.py / t4_render.py exec-ed, never re-run). Writes only under work/t4/q9/.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_q9_sample.py
"""
import collections, hashlib, json, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(os.path.dirname(HERE))
OUT = f"{TB}/work/t4/q9"
SEED = 20261131
ALLOC = [("TABLE_ROW", 26), ("SENTENCE", 16), ("LIST_ITEM", 12), ("CODE_LITERAL", 5), ("TABLE_HEADER", 3), ("CROSS_REF", 1), ("NOTE", 1), ("FIGURE", 1)]
PACK = 26
os.makedirs(OUT, exist_ok=True)


def defs_only(path, marker):
    src = open(path, encoding="utf-8").read()
    assert src.count(marker) == 1, (path, marker)
    return src.split(marker)[0]


S = {"__file__": f"{HERE}/t4_sample.py", "__name__": "t4_sample_defs"}
exec(compile(defs_only(f"{HERE}/t4_sample.py", "\ncls = lambda c:"), f"{HERE}/t4_sample.py", "exec"), S)
R = {"__name__": "t4_render_defs"}
exec(compile(defs_only(f"{HERE}/t4_render.py", '\ngate = lj(f"{TB}/work/t4/gate_sample.jsonl")'), f"{HERE}/t4_render.py", "exec"), R)
lj, L, D, A, W, in_scope = S["lj"], S["L"], S["D"], S["A"], S["W"], S["in_scope"]
gate = {g["atom_id"] for g in lj(f"{W}/t4/gate_sample.jsonl")}
stock = sorted(i for i in A if i in L and i not in D and in_scope(i) and A[i]["atom_type"] != "HEADING")
eq = [i for i in stock if L[i]["verdict"] == "EQUIVALENT"]
sv = [i for i in eq if i.startswith("sv20_")]
ig = [i for i in eq if i.startswith("ig34_")]
rng = random.Random(SEED)
samp = []
for typ, n in ALLOC:
    pool = sorted(i for i in ig if A[i]["atom_type"] == typ and i not in gate)
    samp += sorted(rng.sample(pool, min(n, len(pool))))
layers = [("Q9_SV20_EQUIV", [i for i in sv if i not in gate]), ("Q9_IG34_EQUIV", samp)]
pop = dict(seed=SEED, stock_in_scope=len(stock), stock_verdicts=dict(collections.Counter(L[i]["verdict"] for i in stock)),
           equiv_sv20=len(sv), equiv_sv20_in_gate=sorted(set(sv) & gate), equiv_ig34=len(ig), equiv_ig34_in_gate=sorted(set(ig) & gate),
           equiv_ig34_by_type=dict(collections.Counter(A[i]["atom_type"] for i in ig)), alloc=ALLOC,
           checked={k: v for k, v in layers})
json.dump(pop, open(f"{OUT}/q9_population.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
rows = [S["refine_human"](S["row"](i, f"q9:{name}")) for name, ids in layers for i in ids]
with open(f"{OUT}/q9_sample.jsonl", "w", encoding="utf-8") as fh:
    for x in rows:
        fh.write(json.dumps(x, ensure_ascii=False) + "\n")
n, k = 0, 0
for name, ids in layers:
    part_all = [x for x in rows if x["layer"] == f"q9:{name}"]
    for lo in range(0, len(part_all), PACK):
        k += 1
        part = part_all[lo:lo + PACK]
        out = [f"# T4.1 Q9 扩检包 {k} — {name} ({len(part)} 条; 编号 Q{n + 1}-Q{n + len(part)})", "",
               "> 由 `scripts/t4/t4_q9_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (加前缀 Q).", ""]
        for x in part:
            n += 1
            out += R["block"](x, f"Q{n}")
        open(f"{OUT}/q9_pack_{k}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
print(f"stock in scope {len(stock)} {pop['stock_verdicts']}; EQUIV sv20 {len(sv)} (gate {len(set(sv) & gate)}) / ig34 {len(ig)} (gate {len(set(ig) & gate)})")
print(f"checked: sv20 full {len(layers[0][1])}, ig34 sample {len(samp)} (seed {SEED}); packs {k}; q9_sample.jsonl md5 {md5(f'{OUT}/q9_sample.jsonl')}")
