#!/usr/bin/env python3
"""Follow-up layers asked for by the independent review of the supplementary check (REVIEW_B findings #1 #4 #6 #7):
  XDOC      : in-scope stock EXACT / EQUIVALENT atoms (HEADING included) whose ledger md_atom_ids point only into the
              other document's KB files (ig34 atom -> knowledge_base/model/ only; sv20 atom -> no model/ file) and that
              no reviewer has judged yet. Full check. (The out-of-scope ones are only listed, in round2_population.json.)
  TYPO_SIB  : in-scope EXACT / EQUIVALENT atoms (stock or TB) on the page (+-1) of a registry entry handled "KB 写正确值",
              whose verbatim contains the registry's corrected KB span and overlaps (>= 0.8 of the atom's tokens) the KB
              line(s) the registry points at -> candidates for "label should be PDF_TYPO". Full check of the candidates.
  PDF_TYPO  : seeded stratified sample (15 per rule) of the final PDF_TYPO atoms not yet judged by any reviewer.
Atoms already judged (gate / supp / q9 / U-5 C7) are excluded. Same row builders / renderer as the gate packs
(definition parts exec-ed; t4_sample.py / t4_render.py are never re-run). Writes only under work/t4/round2/.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_round2_sample.py
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

# ---- XDOC
xdoc_in, xdoc_out = [], []
for i, e in L.items():
    if i not in A or i in D or e["verdict"] not in ("EXACT", "EQUIVALENT", "PARTIAL"):
        continue
    fs = {MD[m]["file"] for m in e.get("md_atom_ids") or [] if m in MD}
    if not fs:
        continue
    model = [f.startswith("knowledge_base/model/") for f in fs]
    if (i.startswith("sv20") and not any(model)) or (i.startswith("ig34") and all(model)):
        (xdoc_in if in_scope(i) else xdoc_out).append(i)
xdoc = sorted(i for i in xdoc_in if i not in done and L[i]["verdict"] != "PARTIAL")

# ---- TYPO_SIB
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
        if not i.startswith(src) or abs(a["page"] - pg) > 1 or i not in L or not in_scope(i) or L[i]["verdict"] not in ("EXACT", "EQUIVALENT"):
            continue
        ta = tok(a["verbatim"])
        if ta and span and span in a["verbatim"] and max((len(ta & tok(k)) / len(ta) for k in kbl), default=0) >= 0.8:
            sib.setdefault(i, []).append(r["id"])
sib_ids = sorted(i for i in sib if i not in done)

# ---- PDF_TYPO sample
rng = random.Random(SEED)
pt = sorted(i for i, e in L.items() if e["verdict"] == "PDF_TYPO" and i not in done)
by_rule = collections.defaultdict(list)
for i in pt:
    by_rule[(D.get(i) or {}).get("rule", "(none)")].append(i)
pt_s = []
for rule in sorted(by_rule):
    pt_s += sorted(rng.sample(by_rule[rule], min(PER_RULE, len(by_rule[rule]))))

layers = [("XDOC", xdoc), ("TYPO_SIB", sib_ids), ("PDF_TYPO", pt_s)]
pop = dict(seed=SEED, xdoc_in_scope=sorted(xdoc_in), xdoc_in_scope_already_judged=sorted(set(xdoc_in) & done),
           xdoc_out_of_scope={i: L[i]["verdict"] for i in sorted(xdoc_out)},
           typo_sib_candidates={i: sib[i] for i in sorted(sib)}, typo_sib_already_judged=sorted(set(sib) & done),
           pdf_typo_total=sum(1 for e in L.values() if e["verdict"] == "PDF_TYPO"), pdf_typo_unjudged=len(pt),
           pdf_typo_unjudged_by_rule={k: len(v) for k, v in by_rule.items()}, checked={k: v for k, v in layers})
json.dump(pop, open(f"{OUT}/round2_population.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
rows = []
for name, ids in layers:
    for i in ids:
        x = S["refine_human"](S["row"](i, f"r2:{name}"))
        if name == "TYPO_SIB":
            x["sib_registry"] = sib[i]
            x["registry_rows"] = [dict(id=g, pdf_value=REG[g].get("pdf_value"), kb_value=REG[g].get("kb_value"), handling=REG[g].get("handling"),
                                       kb=f"{REG[g]['kb_file']}:{REG[g].get('kb_line_now')}", basis=REG[g].get("basis")) for g in sib[i]]
        rows.append(x)
with open(f"{OUT}/round2_sample.jsonl", "w", encoding="utf-8") as fh:
    for x in rows:
        fh.write(json.dumps(x, ensure_ascii=False) + "\n")
n = k = 0
for name, ids in layers:
    part_all = [x for x in rows if x["layer"] == f"r2:{name}"]
    for lo in range(0, len(part_all), PACK):
        k += 1
        part = part_all[lo:lo + PACK]
        out = [f"# T4.1 第二轮补检包 {k} — {name} ({len(part)} 条; 编号 R{n + 1}-R{n + len(part)})", "",
               "> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).", ""]
        for x in part:
            n += 1
            out += R["block"](x, f"R{n}")
        open(f"{OUT}/round2_pack_{k}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
print(f"XDOC in scope {len(xdoc_in)} (already judged {len(set(xdoc_in) & done)}, checked here {len(xdoc)}); out of scope {len(xdoc_out)}")
print(f"TYPO_SIB candidates {len(sib)} (already judged {len(set(sib) & done)}, checked here {len(sib_ids)})")
print(f"PDF_TYPO total {pop['pdf_typo_total']}, unjudged {len(pt)} {pop['pdf_typo_unjudged_by_rule']}, sampled {len(pt_s)} (seed {SEED})")
print(f"packs {k}, rows {len(rows)}; round2_sample.jsonl md5 {md5(f'{OUT}/round2_sample.jsonl')}")
