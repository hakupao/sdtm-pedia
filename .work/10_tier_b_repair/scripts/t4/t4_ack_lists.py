#!/usr/bin/env python3
"""T4 ack lists: every atom whose final verdict is ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED (G-TB1 needs user ack).
Unit = PDF atom (not registry row). -> evidence/checkpoints/t4_ack_lists.md
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_ack_lists.py
"""
import collections, json, subprocess

TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
W = f"{TB}/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
L = {r["pdf_atom_id"]: r for r in lj(f"{W}/coverage_ledger.wc.jsonl")}
D = json.load(open(f"{W}/t3_writeback_decisions.json"))
ER = json.load(open(f"{W}/t3_errata.json"))["atom_err"]
K3W = json.load(open(f"{W}/t3_rules.json"))["K3b_why"]
# T4 W3 (主控决定 5): atoms that entered these classes after the U-5 ruling (ledger at 3a24a1c) carry their own decision source
U5_REV = "3a24a1c"
U5 = {}
for l in subprocess.run(["git", "-C", TB, "show", f"{U5_REV}:.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl"], capture_output=True, text=True, check=True).stdout.splitlines():
    if l.strip():
        r = json.loads(l); U5[r["pdf_atom_id"]] = r["verdict"]
REGD = {r["id"]: r.get("t4_decision") for r in lj(f"{W}/t2_pdf_typo_registry.jsonl")}
KEEPD = {k: v.get("t4_decision") for k, v in json.load(open(f"{W}/t3_k3b_out_of_scope_keep.json")).items() if not k.startswith("_")}
def source(i, v):
    if U5.get(i) == v:
        return "U-5 (整类, 委托代裁)"
    e, d = ER.get(i) or {}, D.get(i) or {}
    if str(e.get("source", "")).startswith("T4 U-2"):
        return "U-2 委托代裁 (§000), 非 U-5"
    if KEEPD.get(i):
        return "U-8 委托代裁 (§000), 非 U-5"
    regs = (d.get("evidence") or {}).get("registry") or e.get("registry") or []
    t4 = [f"{x}: {REGD[x]}" for x in regs if REGD.get(x)]
    if t4:
        return "U-7 委托代裁 (§000), 非 U-5; " + "; ".join(t4)
    return "(未归因)"
cell = lambda s, n=90: (str(s or "-").replace("|", "\\|").replace("\n", " "))[:n]

out = ["# T4 用户确认清单: ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED", "", "<!-- chain: E (plans) -->",
       "> 状态: **委托代裁整类确认 (U-5=B, C7 38 全检成立), 见 t4_user_decisions.md §000; 非主人逐条确认** (2026-11-27 T4 解冻轮 W3 重生成). U-5 裁定时 (ledger @3a24a1c) 为 ATOM_ERR 197 / PDF_TYPO 122 / FIG 11; 之后进入这三类的原子按 \"决定来源\" 列标注 (U-2 / U-8 / U-7 委托代裁, 见 t4_user_decisions.md §000), 不归入 U-5; 明细见 `evidence/checkpoints/t4_thaw_W3.md`. 生成: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_ack_lists.py`.",
       "> 单位 = PDF 原子 (不是登记行; 一条登记行可覆盖多个原子, 一个原子也可挂多条登记). 数据源: 最终 ledger `work/coverage_ledger.wc.jsonl` + `work/t3_writeback_decisions.json` + `work/t3_errata.json`.",
       "> G-TB1 要求这三类 \"每条有登记 + 用户 ack\". 这三类在 G-TB3 mapped 口径中从分母去掉, 在 strict 口径中算未覆盖.", ""]
ids = {v: sorted(i for i, r in L.items() if r["verdict"] == v) for v in ("ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED")}
SRC = {i: source(i, v) for v, xs in ids.items() for i in xs}
out += ["## 汇总", "", "| 终态 | 原子数 | 按判定规则 | 决定来源 | 用户确认 |", "|---|--:|---|---|---|"]
for v, xs in ids.items():
    c = collections.Counter((D.get(i) or {}).get("rule", "(不在 T3 决策表)") for i in xs)
    cs = collections.Counter(SRC[i].split(" (")[0].split(";")[0] for i in xs)
    out.append(f"| {v} | {len(xs)} | {', '.join(f'{k} {n}' for k, n in c.most_common())} | {', '.join(f'{k} {n}' for k, n in cs.most_common())} | ☐ 整类确认　☐ 有异议 (在下表备注) |")
out += ["", "规则含义: `S1-R1` = 原子 verbatim 与 PDF 不符 (原子抽错, KB 按 PDF); `S1-R2` = PDF 自身笔误且已登记; "
        "`C7-atom-not-in-PDF` = 原子文本在 PDF 页中不存在; `K3b-registry` / `writer-Tn-registry` = 由 PDF 笔误登记 (T-n) 触及; "
        "`FIGURE` = 图, 暂缓.", ""]
for v, xs in ids.items():
    out += [f"## {v} ({len(xs)})", "", "| # | atom_id | 页 | 节 | 规则 | 依据 / 登记 | 出处 | 决定来源 | 异议 |", "|--:|---|--:|---|---|---|---|---|---|"]
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
                   f"{cell(basis)}{' [' + cell(reg, 40) + ']' if reg and reg not in str(basis) else ''} | `{cell(ck, 80)}` | {cell(SRC[i], 120)} | |")
    out.append("")
open(f"{TB}/evidence/checkpoints/t4_ack_lists.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print({v: len(x) for v, x in ids.items()}, "| decision source:", dict(collections.Counter(s.split(" (")[0].split(";")[0] for s in SRC.values())))
assert "(未归因)" not in SRC.values(), [i for i, s in SRC.items() if s == "(未归因)"]
