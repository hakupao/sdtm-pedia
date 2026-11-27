#!/usr/bin/env python3
"""Render work/t4/{gate,human}_sample.jsonl into review packs.
  gate  -> work/t4/gate_pack_{1..4}.md (21 rows each, for the read-only T4.1 reviewers)
  human -> evidence/checkpoints/t4_human_sample.md (with empty user-judgement fields)
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_render.py
"""
import json

TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
FENCE = "~~~~"


def block(x, n, human=False):
    o = [f"### {n}. `{x['atom_id']}` — {x['layer']}", ""]
    meta = [f"PDF 页 {x['page']} · 原子类型 {x['atom_type']} · 所在节 `{x['parent_section']}`",
            f"triage 类 **{x['triage_class'] or '-'}** · 终态 **{x['verdict_final']}** (T3 前 {x['verdict_pre_t3']}) · "
            f"判定规则 `{x['rule'] or '(本项目未改, stock)'}` · 批 `{x['batch'] or '-'}`"]
    if x.get("ie_cat") or x["verdict_final"] == "INTENTIONAL_EXCLUDE":
        meta.append(f"IE 类别 `{x.get('ie_cat') or '-'}` · 排除理由: {x.get('exclusion_reason') or '-'}")
    if x.get("errata"):
        e = x["errata"]
        meta.append(f"原子抽错登记: {e.get('cls')} → {e.get('terminal')}; 依据: {e.get('basis')}; 出处 `{e.get('checkpoint')}`")
    if x.get("registry"):
        meta.append("PDF 笔误登记: " + ", ".join(f"`{r}`" for r in x["registry"]) + " (见 `work/t2_pdf_typo_registry.jsonl`)")
    o += [f"- {m}" for m in meta]
    o += ["", "原子 verbatim (抽取物, 可能抽错, 仅供对照):", "", FENCE, x["atom_verbatim"], FENCE, ""]
    p = x["pdf"]
    o += [f"PDF 原文: `{p['page_txt']}` 第 {p.get('lines') or '?'} 行 (自动定位, 词覆盖 {p['score']}; 版式以原 PDF 为准):", "",
          FENCE, p["text"] or "(未定位, 请直接看该页)", FENCE, ""]
    k = x["kb"]
    o += [f"KB 现文: `{k['loc'] or '(无)'}` (来源: {k['src']}):", "", FENCE, k["text"] or "(无 KB 文本; IE 类或未定位)", FENCE, ""]
    if human:
        o += ["**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF", "", "备注: ", ""]
    return o


gate = lj(f"{TB}/work/t4/gate_sample.jsonl")
K = 21
for k in range(4):
    part = gate[k * K:(k + 1) * K]
    out = [f"# T4.1 总闸样本包 {k + 1}/4 (行 {k * K + 1}-{k * K + len(part)} / {len(gate)})", "",
           "> 由 `scripts/t4/t4_sample.py` (seed 20261127) 生成, `scripts/t4/t4_render.py` 渲染. 只读材料.", ""]
    for n, x in enumerate(part, k * K + 1):
        out += block(x, n)
    open(f"{TB}/work/t4/gate_pack_{k + 1}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")

human = lj(f"{TB}/work/t4/human_sample.jsonl")
hdr = open(f"{TB}/scripts/t4/t4_human_header.md", encoding="utf-8").read()
out = [hdr.rstrip(), ""]
cur = None
for n, x in enumerate(human, 1):
    if x["layer"] != cur:
        cur = x["layer"]
        out += [f"## {cur}", ""]
    out += block(x, n, human=True)
open(f"{TB}/evidence/checkpoints/t4_human_sample.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("gate packs 4 x 21 =", len(gate), "human", len(human))
