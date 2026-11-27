#!/usr/bin/env python3
"""T4 第二轮改台账 R2L §2 (规格 subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md): registry corrections in
work/t2_pdf_typo_registry.jsonl. Each changed row gets field t4_r2l_fix (before -> after + basis); new rows carry
t4_decision. Idempotent (a row already carrying t4_r2l_fix / an id already present is left as is).
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_r2l_registry_fix.py ITEM [ITEM ...]
  ITEM: page (§2.1) | add (§2.2) | basis (§2.3 basis 文字) | suppqual (§2.3 位置) | pdfvalue (§2.3 pdf_value)
"""
import json, sys
W = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work"
P = f"{W}/t2_pdf_typo_registry.jsonl"
SRC = "T4 R2L (规格 t4_round2_ledger_spec_v1.0.md §2"
FIX = {
    "page": {"B-IS T-6": ("pdf_page", 239, "§2.1) pdf_page 241 → 239 (依据 work/pdf_pages/ig34_p0239.txt:35,39,43 'AUREUS–EPITOPE X')"),
             "B-CP T-5": ("pdf_page", 212, "§2.1) pdf_page 211 → 212 (依据 evidence/t4_round2_raw/pack_sib2_1.md:34 附注; 复核 work/pdf_pages/ig34_p0212.txt:2-6 Ex2 row 6 CPDTC '…16T04:20', 同表其余行 12:20)")},
    "basis": {k: ("basis", v, "§2.3) basis 去掉与 handling 'KB 写正确值' 矛盾的 '照录' 字样 (evidence/t4_round3_raw/pack_8.md / pack_9.md)")
              for k, v in {"S-SPC2 N-1": "应为 PC records (PCSEQ 属 PC); KB 写正确值 (U-7 B)",
                           "S-SPC2 N-2": "应为 PC records / PCGRPID (同页 relrec RDOMAIN=PC, IDVAR=PCGRPID); KB 写正确值 (U-7 B)",
                           "B-NV N-1": "PDF 语法 (may included); KB 写正确值 (U-7 B)",
                           "B-NV N-2": "PDF 语法 (links the each); KB 写正确值 (U-7 B)"}.items()},
    "suppqual": {"B-SUPPQUAL T-1": ("other_kb_lines", ["knowledge_base/chapters/ch08_relationships.md:228"],
                                    "§2.3) 位置清单补 ch08_relationships.md:228 (同一 p433 句, KB 写改正值 'illustrate'; evidence/t4_round2_raw/pack_sib_3.md:67)")},
    "pdfvalue": {"B-CP T-3": ("pdf_value", "(e.g., CD40+ in rows 15-16 in addition to non-cell state, non-sublineage marker(s). Rows 17-18",
                              "§2.3) pdf_value 改为 PDF 原文: '(e.g.,' 括号未闭合, 不是多一个右括号 (evidence/t4_round3_raw/pack_8.md:28,58)"),
                 "S-SPC1 CP T-16a": ("pdf_value", "引号未闭合 \"CD3+CD19- (T lymphocyte) / 引号未闭合 \"CD278+ (activated)",
                                     "§2.3) pdf_value 补第二处未闭合引号 \"CD278+ (evidence/t4_round3_raw/pack_8.md:25,59; t2_S-SPC1.md:127)")},
}
NEW = [
    {"batch": "T4-R2L", "id": "T4R2 sv20 N-1", "kb_file": "knowledge_base/model/04_associated_persons.md", "kb_line_now": 42,
     "kb_text_span": "to the device identified in RDEVID", "pdf_page": 69,
     "pdf_value": "sv20 p69 §6.6 APRELSUB SREL Notes 写 subject or pool (identified in RDEVID); p50 §4 同句写 device",
     "kb_value": "照录 (KB 只收 p50 那句 = device; p69 §6.6 表只有精简列, 未收 Notes)", "handling": "照录",
     "basis": "PDF 自身不一致: sv20 p69 (§6.6) SREL Notes vs p50 同句; KB 不改", "cat": "obs", "span_count_in_file": 1,
     "note": "PDF 文本层 work/pdf_pages/sv20_p0069.txt:18-23 vs sv20_p0050.txt:33-36; 审查者 evidence/t4_q9_raw/pack_5.md",
     "t4_decision": "owner 2026-11-27 问题 9 = A (补登记)"},
    {"batch": "T4-R2L", "id": "T4R2 RELSPEC N-1", "kb_file": "knowledge_base/domains/RELSPEC/examples.md", "kb_line_now": 17,
     "kb_text_span": "SPC-003<br/>(Brain)", "pdf_page": 440,
     "pdf_value": "ig34 p440 图中 SPC-003 标 Brain; 同页 relspec 表 Row 5 SPEC 写 TISSUE",
     "kb_value": "照录 (图 :17 Brain, 表 :50 TISSUE)", "handling": "照录",
     "basis": "PDF 自身不一致: p440 图与同页表格; KB 两处照录, 不改", "cat": "obs", "span_count_in_file": 1,
     "note": "PDF 文本层 work/pdf_pages/ig34_p0440.txt:26 (表 Row 5); 审查者 evidence/t4_supp_raw/pack_6.md:25,64",
     "t4_decision": "owner 2026-11-27 问题 9 = A (补登记)"},
]
items = sys.argv[1:]
assert items and set(items) <= set(FIX) | {"add"}, items
rows = [json.loads(l) for l in open(P, encoding="utf-8") if l.strip()]
ids = [r["id"] for r in rows]
done = []
for it in items:
    if it == "add":
        for n in NEW:
            if n["id"] not in ids:
                rows.append(n); ids.append(n["id"]); done.append(f"add {n['id']}")
        continue
    for rid, (k, v, why) in FIX[it].items():
        r = next(x for x in rows if x["id"] == rid)
        fx = r.get("t4_r2l_fix") or ""
        if f"{SRC} {why.split(')')[0]})" in fx and r.get(k) == v:
            continue
        r["t4_r2l_fix"] = (fx + " | " if fx else "") + f"{SRC} {why}; before {k} = {json.dumps(r.get(k), ensure_ascii=False)}"
        r[k] = v
        done.append(f"{it} {rid}.{k}")
assert len(set(ids)) == len(ids)
open(P, "w", encoding="utf-8").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
print(len(rows), "rows;", done)
