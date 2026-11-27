#!/usr/bin/env python3
"""Round-2b layer (follow-up of TYPO_SIB): in-scope EQUIVALENT atoms (non-HEADING) on the page (+-1) of a registry entry
handled "KB 写正确值" that overlap (>= 0.8 of the atom's tokens) the KB line(s) the registry points at but whose verbatim does
NOT contain the registry's corrected span (TYPO_SIB took the ones that do). EXACT atoms are left out on purpose: an EXACT
label needs the atom text verbatim in the KB, so an EXACT atom covering the typo location would contain the corrected span.
Atoms already judged (gate / supp / q9 / U-5 C7 / round2) are excluded. Writes only work/t4/round2/round2b_*.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_round2b_sample.py
"""
import collections, hashlib, json, os, random, re

HERE = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.dirname(os.path.dirname(TB))
OUT = f"{TB}/work/t4/round2"
SEED, PER_RULE, PACK = 20261132, 15, 25
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

done |= {x["atom_id"] for x in lj(f"{W}/t4/round2/round2_sample.jsonl")}
tok = lambda s: set(re.findall(r"[A-Za-z0-9]+", s.lower()))
files, sib = {}, collections.OrderedDict()
for r in REG.values():
    if r.get("handling") != "KB 写正确值":
        continue
    span = (r.get("kb_text_span") or "").strip(" |")
    lines = r.get("span_lines_in_file") or ([r["kb_line_now"]] if r.get("kb_line_now") else [])
    try:
        pg = int(str(r["pdf_page"]).split("-")[0].split(",")[0])
    except ValueError:
        continue
    f = r["kb_file"]
    if f not in files:
        files[f] = open(f"{ROOT}/{f}", encoding="utf-8").read().split("\n")
    kbl = [files[f][n - 1] for n in lines if 0 < n <= len(files[f])]
    src = "sv20" if "/model/" in f else "ig34"
    for i, a in A.items():
        if (not i.startswith(src) or abs(a["page"] - pg) > 1 or i not in L or not in_scope(i) or L[i]["verdict"] != "EQUIVALENT"
                or a["atom_type"] == "HEADING" or i in done):
            continue
        ta = tok(a["verbatim"])
        if len(ta) >= 3 and max((len(ta & tok(k)) / len(ta) for k in kbl), default=0) >= 0.8 and not (span and span in a["verbatim"]):
            sib.setdefault(i, []).append(r["id"])
ids = sorted(sib)
rows = []
for i in ids:
    x = S["refine_human"](S["row"](i, "r2:TYPO_SIB2"))
    x["sib_registry"] = sib[i]
    x["registry_rows"] = [dict(id=g, pdf_value=REG[g].get("pdf_value"), kb_value=REG[g].get("kb_value"), handling=REG[g].get("handling"),
                               kb=f"{REG[g]['kb_file']}:{REG[g].get('kb_line_now')}", basis=REG[g].get("basis")) for g in sib[i]]
    rows.append(x)
with open(f"{OUT}/round2b_sample.jsonl", "w", encoding="utf-8") as fh:
    for x in rows:
        fh.write(json.dumps(x, ensure_ascii=False) + "\n")
H = (len(rows) + 1) // 2
for k, part in enumerate((rows[:H], rows[H:]), 1):
    base = 0 if k == 1 else H
    out = [f"# T4.1 第二轮补检包 b{k} — TYPO_SIB2 ({len(part)} 条; 编号 S{base + 1}-S{base + len(part)})", "",
           "> 由 `scripts/t4/t4_round2b_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号前缀 S.", ""]
    for n, x in enumerate(part, base + 1):
        out += R["block"](x, f"S{n}")
    open(f"{OUT}/round2b_pack_{k}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"TYPO_SIB2 candidates {len(rows)}; round2b_sample.jsonl md5 {hashlib.md5(open(f'{OUT}/round2b_sample.jsonl','rb').read()).hexdigest()}")
