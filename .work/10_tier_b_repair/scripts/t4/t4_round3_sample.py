#!/usr/bin/env python3
"""Round 3 = the extra checks the owner chose on 2026-11-27 (evidence/checkpoints/t4_owner_decisions_round2.md):
  R3_IG34_EQUIV (4a = B) : 150 more of the in-scope stock EQUIVALENT atoms from SDTMIG (non-HEADING), allocated to atom types
                           in proportion to the unjudged pool (largest remainder), seed 20261133
  R3_PDF_TYPO   (4b = B) : every final PDF_TYPO atom no reviewer has judged yet (full check)
  R3_HEADING    (4c = B) : 60 of the in-scope stock HEADING atoms (EXACT / EQUIVALENT) not yet judged, proportional, same seed
  R3_XTYPO      (7b = A) : the 6 out-of-scope atoms the delta reviewer found hit by a registered typo (full check)
Atoms already judged (gate / supp / q9 / U-5 C7 / round2 / round2b) are excluded. Same builders / renderer as the gate
packs (definition parts exec-ed; t4_sample.py / t4_render.py never re-run). Writes only under work/t4/round3/.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_round3_sample.py
"""
import collections, hashlib, json, os, random, re

HERE = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.dirname(os.path.dirname(TB))
OUT = f"{TB}/work/t4/round3"
SEED, PACK = 20261133, 25
os.makedirs(OUT, exist_ok=True)


def defs_only(path, marker):
    src = open(path, encoding="utf-8").read()
    assert src.count(marker) == 1, (path, marker)
    return src.split(marker)[0]


S = {"__file__": f"{HERE}/t4_sample.py", "__name__": "t4_sample_defs"}
exec(compile(defs_only(f"{HERE}/t4_sample.py", "\ncls = lambda c:"), f"{HERE}/t4_sample.py", "exec"), S)
R = {"__name__": "t4_render_defs"}
exec(compile(defs_only(f"{HERE}/t4_render.py", '\ngate = lj(f"{TB}/work/t4/gate_sample.jsonl")'), f"{HERE}/t4_render.py", "exec"), R)
lj, L, D, A, W, in_scope, MD, REG = S["lj"], S["L"], S["D"], S["A"], S["W"], S["in_scope"], S["MD"], S["REG"]
done = set()
for f in ("t4/gate_sample.jsonl", "t4/supp/supp_sample.jsonl", "t4/q9/q9_sample.jsonl", "t4/u5_c7_38.jsonl"):
    done |= {x["atom_id"] for x in lj(f"{W}/{f}")}

for f in ("t4/round2/round2_sample.jsonl", "t4/round2/round2b_sample.jsonl"):
    done |= {x["atom_id"] for x in lj(f"{W}/{f}")}
XTYPO = {"ig34_p0083_a020": ["S-SPREL SE T-1"], "ig34_p0304_a026": ["B-OE T-2"], "ig34_p0304_a027": ["B-OE T-2"],
         "ig34_p0304_a028": ["B-OE T-2"], "ig34_p0304_a029": ["B-OE T-2"], "ig34_p0316_a023": ["S-FND PE T-1"]}
rng = random.Random(SEED)


def prop_sample(pool, key, n):
    """n atoms from pool, allocated to key-groups in proportion to group size (largest remainder), sorted pools."""
    groups = collections.defaultdict(list)
    for i in sorted(pool):
        groups[key(i)].append(i)
    quota = {k: n * len(v) / len(pool) for k, v in groups.items()}
    alloc = {k: int(q) for k, q in quota.items()}
    for k in sorted(quota, key=lambda k: (-(quota[k] - alloc[k]), k))[: n - sum(alloc.values())]:
        alloc[k] += 1
    out = []
    for k in sorted(groups):
        out += sorted(rng.sample(groups[k], alloc[k]))
    return out, {k: (len(groups[k]), alloc[k]) for k in sorted(groups)}


stock = [i for i in A if i in L and i not in D and in_scope(i)]
eq_pool = [i for i in stock if i.startswith("ig34_") and A[i]["atom_type"] != "HEADING" and L[i]["verdict"] == "EQUIVALENT" and i not in done]
eq_s, eq_alloc = prop_sample(eq_pool, lambda i: A[i]["atom_type"], 150)
pt = sorted(i for i, e in L.items() if e["verdict"] == "PDF_TYPO" and i not in done)
hd_pool = [i for i in stock if A[i]["atom_type"] == "HEADING" and L[i]["verdict"] in ("EXACT", "EQUIVALENT") and i not in done]
hd_s, hd_alloc = prop_sample(hd_pool, lambda i: (i[:4], L[i]["verdict"]), 60)
layers = [("R3_IG34_EQUIV", eq_s), ("R3_PDF_TYPO", pt), ("R3_HEADING", hd_s), ("R3_XTYPO", sorted(XTYPO))]
assert not (set(XTYPO) & done) and all(not in_scope(i) for i in XTYPO)
pop = dict(seed=SEED, ig34_equiv_unjudged=len(eq_pool), ig34_equiv_alloc=eq_alloc, pdf_typo_unjudged=len(pt),
           heading_unjudged=len(hd_pool), heading_alloc={f"{k[0]}:{k[1]}": v for k, v in hd_alloc.items()}, checked={k: v for k, v in layers})
json.dump(pop, open(f"{OUT}/round3_population.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
rows = []
for name, ids in layers:
    for i in ids:
        x = S["refine_human"](S["row"](i, f"r3:{name}"))
        if name == "R3_XTYPO":
            x["sib_registry"] = XTYPO[i]
            x["registry_rows"] = [dict(id=g, pdf_value=REG[g].get("pdf_value"), kb_value=REG[g].get("kb_value"), handling=REG[g].get("handling"),
                                       kb=f"{REG[g]['kb_file']}:{REG[g].get('kb_line_now')}", basis=REG[g].get("basis")) for g in XTYPO[i]]
        rows.append(x)
with open(f"{OUT}/round3_sample.jsonl", "w", encoding="utf-8") as fh:
    for x in rows:
        fh.write(json.dumps(x, ensure_ascii=False) + "\n")
n = k = 0
for name, ids in layers:
    part_all = [x for x in rows if x["layer"] == f"r3:{name}"]
    for lo in range(0, len(part_all), PACK):
        k += 1
        part = part_all[lo:lo + PACK]
        out = [f"# T4.1 第三轮补检包 {k} — {name} ({len(part)} 条; 编号 T{n + 1}-T{n + len(part)})", "",
               "> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).", ""]
        for x in part:
            n += 1
            out += R["block"](x, f"T{n}")
        open(f"{OUT}/round3_pack_{k}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
print(f"IG34 EQUIV unjudged {len(eq_pool)} -> 150 {eq_alloc}")
print(f"PDF_TYPO unjudged {len(pt)} (full)")
print(f"HEADING unjudged {len(hd_pool)} -> 60 {pop['heading_alloc']}")
print(f"XTYPO {len(XTYPO)}; packs {k}, rows {len(rows)}; round3_sample.jsonl md5 {md5(f'{OUT}/round3_sample.jsonl')}")
