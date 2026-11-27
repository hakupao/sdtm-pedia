#!/usr/bin/env python3
"""T4 ack lists: every atom whose final verdict is ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED (G-TB1 needs user ack).
Unit = PDF atom (not registry row). -> evidence/checkpoints/t4_ack_lists.md
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_ack_lists.py
"""
import collections, json

TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
W = f"{TB}/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
L = {r["pdf_atom_id"]: r for r in lj(f"{W}/coverage_ledger.wc.jsonl")}
D = json.load(open(f"{W}/t3_writeback_decisions.json"))
ER = json.load(open(f"{W}/t3_errata.json"))["atom_err"]
K3W = json.load(open(f"{W}/t3_rules.json"))["K3b_why"]
cell = lambda s, n=90: (str(s or "-").replace("|", "\\|").replace("\n", " "))[:n]

out = ["# T4 用户确认清单: ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED", "", "<!-- chain: E (plans) -->",
       "> 状态: **待用户确认** (2026-11-27 生成). 生成: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_ack_lists.py`.",
       "> 单位 = PDF 原子 (不是登记行; 一条登记行可覆盖多个原子, 一个原子也可挂多条登记). 数据源: 最终 ledger `work/coverage_ledger.wc.jsonl` + `work/t3_writeback_decisions.json` + `work/t3_errata.json`.",
       "> G-TB1 要求这三类 \"每条有登记 + 用户 ack\". 这三类在 G-TB3 mapped 口径中从分母去掉, 在 strict 口径中算未覆盖.", ""]
ids = {v: sorted(i for i, r in L.items() if r["verdict"] == v) for v in ("ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED")}
out += ["## 汇总", "", "| 终态 | 原子数 | 按判定规则 | 用户确认 |", "|---|--:|---|---|"]
for v, xs in ids.items():
    c = collections.Counter((D.get(i) or {}).get("rule", "(不在 T3 决策表)") for i in xs)
    out.append(f"| {v} | {len(xs)} | {', '.join(f'{k} {n}' for k, n in c.most_common())} | ☐ 整类确认　☐ 有异议 (在下表备注) |")
out += ["", "规则含义: `S1-R1` = 原子 verbatim 与 PDF 不符 (原子抽错, KB 按 PDF); `S1-R2` = PDF 自身笔误且已登记; "
        "`C7-atom-not-in-PDF` = 原子文本在 PDF 页中不存在; `K3b-registry` / `writer-Tn-registry` = 由 PDF 笔误登记 (T-n) 触及; "
        "`FIGURE` = 图, 暂缓.", ""]
for v, xs in ids.items():
    out += [f"## {v} ({len(xs)})", "", "| # | atom_id | 页 | 节 | 规则 | 依据 / 登记 | 出处 | 异议 |", "|--:|---|--:|---|---|---|---|---|"]
    for n, i in enumerate(xs, 1):
        d, e = D.get(i) or {}, ER.get(i) or {}
        ev = d.get("evidence") or {}
        c7 = ev.get("c7") or (f"atom_in_pdf={ev.get('atom_in_pdf')}; 修订行 {ev.get('fix_row')}" if "atom_in_pdf" in ev else None)
        regs = d.get("registry") or ev.get("registry") or e.get("registry") or []
        basis = e.get("basis") or c7 or ((", ".join(regs) + (f" ({ev['registry_handling']})" if ev.get("registry_handling") else "")) if regs else None) or ("; ".join(K3W[i]) if i in K3W else None) or (", ".join(d.get("registry") or []) if d.get("registry") else ((d.get("evidence") or {}).get("triage") or {}).get("kb_loc"))
        reg = ", ".join(regs)
        ck = d.get("checkpoint") or e.get("checkpoint") or ev.get("checkpoint") or ev.get("writer_row") or ""
        ck = ck.replace(".work/10_tier_b_repair/", "")
        out.append(f"| {n} | `{i}` | {A[i]['page']} | {cell(A[i]['parent_section'], 50)} | {d.get('rule', '-')} | "
                   f"{cell(basis)}{' [' + cell(reg, 40) + ']' if reg and reg not in str(basis) else ''} | `{cell(ck, 80)}` | |")
    out.append("")
open(f"{TB}/evidence/checkpoints/t4_ack_lists.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print({v: len(x) for v, x in ids.items()})
