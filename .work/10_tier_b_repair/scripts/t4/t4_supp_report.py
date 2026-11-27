#!/usr/bin/env python3
"""Collect the reviewers' per-atom verdicts of the T4.1 supplementary full check (evidence/t4_supp_raw/pack_*.md) and of
the Q9 extension (evidence/t4_q9_raw/pack_*.md); write
  work/t4/supp/verdicts.json                      every atom: layer, final verdict, reviewer verdict, raw file:line
  work/t4/supp/relabel_pending.json               the label changes these results call for (NOT applied to the ledger)
  evidence/checkpoints/t4_supp_fullcheck.md       summary (main-controller transcript; raw files are the reviewers' own)
  evidence/checkpoints/t4_relabel_pending.md      the pending list + gate numbers recomputed on a scratch COPY of the ledger
Nothing here writes the working ledger or the KB. Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_report.py
"""
import collections, glob, hashlib, json, os, re, subprocess

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
W = f"{TB}/work"
CK = f"{TB}/evidence/checkpoints"
SC = f"{W}/scratch/t4/relabel_preview"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
VERD = ["HOLDS_AS_EQUIV", "NOT_HOLD_R1", "NOT_HOLD", "UNVERIFIABLE", "HOLDS"]
# HOLDS_AS_EQUIV rows whose only KB/PDF difference is a registered PDF typo (reviewer text names the registry id)
TYPO = {"ig34_p0147_a025": "B-BE T-3", "ig34_p0262_a016": "B-MB T-1", "ig34_p0262_a017": "B-MB T-1", "ig34_p0296_a023": "B-NV T-2"}


def parse(raw_dir, sample):
    ids = {x["atom_id"]: x for x in lj(sample)}
    got = {}
    for f in sorted(glob.glob(f"{raw_dir}/pack_*.md")):
        for n, l in enumerate(open(f, encoding="utf-8"), 1):
            if not l.startswith("|"):
                continue
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            m = re.search(r"((?:ig34|sv20)_p\d{4}_a\d+)", cells[1]) if len(cells) >= 5 else None
            if not m or m.group(1) not in ids or m.group(1) in got:
                continue
            v = None
            for c in cells[2:6]:
                c2 = c.replace("*", "").replace("`", "").strip()
                v = next((x for x in VERD if c2 == x or c2.startswith(x + " ") or c2.startswith(x + "(")), None)
                if v:
                    break
            if v:
                got[m.group(1)] = dict(num=cells[0], layer=ids[m.group(1)]["layer"].split(":", 1)[1], final=ids[m.group(1)]["verdict_final"],
                                       verdict=v, raw=f"{os.path.relpath(f, TB)}:{n}", note=cells[-1][:160])
    miss = [a for a in ids if a not in got]
    assert not miss, (raw_dir, miss[:5])
    return got


supp = parse(f"{TB}/evidence/t4_supp_raw", f"{W}/t4/supp/supp_sample.jsonl")
q9 = parse(f"{TB}/evidence/t4_q9_raw", f"{W}/t4/q9/q9_sample.jsonl")
json.dump(dict(supp=supp, q9=q9), open(f"{W}/t4/supp/verdicts.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ---- pending label changes (not applied)
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
pend = []
for src, d in (("supp", supp), ("q9", q9)):
    for a, r in d.items():
        if r["verdict"] == "NOT_HOLD_R1" or (r["verdict"] == "NOT_HOLD" and r["layer"] == "PRE_EXISTING"):
            pend.append(dict(atom_id=a, now=r["final"], to="INTENTIONAL_EXCLUDE", group="R1-row",
                             why="SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类)", raw=r["raw"]))
        elif r["verdict"] == "NOT_HOLD":
            pend.append(dict(atom_id=a, now=r["final"], to="INTENTIONAL_EXCLUDE", group="v2.0-TOC",
                             why="SDTM v2.0 目录条目, 对应章节 KB 未收 (同页 a009 / a010 已是 IE VERSION_MISMATCH)", raw=r["raw"]))
        elif a in TYPO:
            pend.append(dict(atom_id=a, now=r["final"], to="PDF_TYPO", group="registered-typo",
                             why=f"KB 与 PDF 的差异 = 已登记 PDF 笔误 {TYPO[a]} (KB 写正确值)", raw=r["raw"]))
pend.sort(key=lambda x: (x["group"], x["atom_id"]))
json.dump(pend, open(f"{W}/t4/supp/relabel_pending.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ---- gate numbers on a scratch copy of the ledger
os.makedirs(SC, exist_ok=True)
led = f"{W}/coverage_ledger.wc.jsonl"
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
to = {p["atom_id"]: p["to"] for p in pend}
n = 0
with open(f"{SC}/ledger_preview.jsonl", "w", encoding="utf-8") as fh:
    for l in open(led, encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            if r["pdf_atom_id"] in to:
                assert r["verdict"] in ("EXACT", "EQUIVALENT"), r
                r["verdict"] = to[r["pdf_atom_id"]]
                n += 1
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
assert n == len(pend), (n, len(pend))
run = lambda *a: subprocess.run(["python3", "-I", *a], capture_output=True, text=True, cwd=ROOT).stdout
dec = lambda p: [l for l in run(f"{TB}/scripts/t4/t4_coverage_decomp.py", *p).splitlines() if l.startswith(("final", "content"))]
tbl = lambda p: [l for l in run(f"{TB}/scripts/t3_recompute.py", "--out", f"{SC}/sc_{'prev' if p else 'now'}.jsonl", *p).splitlines() if "§5.0 scope" in l]
now_dec, prev_dec = dec([]), dec([f"{SC}/ledger_preview.jsonl"])
now_tb, prev_tb = tbl([]), tbl(["--ledger", f"{SC}/ledger_preview.jsonl"])
assert md5(led) == "60729f7b64b7c1dfaf2174e394f6dd9c", md5(led)   # working ledger untouched (value cited in t4_attempt2_report.md)

# ---- reconcile the rule counts quoted by the attempt-1 reviewer with today's
dec_now = json.load(open(f"{W}/t3_writeback_decisions.json"))
dec_old = json.loads(subprocess.check_output(["git", "-C", ROOT, "show", "3a24a1c:.work/10_tier_b_repair/work/t3_writeback_decisions.json"]))
RULES = ["T1-two-agent", "T1-two-agent+T2-rework", "T2-fix+deltaRereviewPASS+auditPASS", "live-hit(was-IE-ack)", "C1-manual-PDF+KB", "C7-K4-rereview"]
cnt = lambda d, r: sum(1 for x in d.values() if x.get("rule") == r)
moved = collections.Counter((dec_old.get(i, {}).get("rule", "(不在决策表)"), d.get("rule")) for i, d in dec_now.items()
                            if d.get("rule") in RULES and dec_old.get(i, {}).get("rule") != d.get("rule"))

# ---- summary md
pop = json.load(open(f"{W}/t4/supp/supp_population.json"))
qp = json.load(open(f"{W}/t4/q9/q9_population.json"))
o = ["# T4.1 补检 (\"0 抽中\" 各类全检) + Q9 扩检 — 汇总", "", "<!-- chain: E (plans) -->",
     "> 状态: **补检 PRE_EXISTING 层不通过 (2 条 NOT_HOLD) → 触发 Q9 升级; Q9 扩检已跑完, 结论待主人裁定** (2026-11-27). 其余各层通过. KB 未改; 台账未改.",
     "> 审查: `oh-my-claudecode:tracer` (opus) × 16 个独立实例 (补检 8 + Q9 8), 只读; 原始结果由审查者自己写入 `evidence/t4_supp_raw/pack_{1..8}.md` 与 `evidence/t4_q9_raw/pack_{1..8}.md`. 本文件是主控用 `scripts/t4/t4_supp_report.py` 从原始结果机械汇总的, 不改判 (规则 D).",
     "> 口径 (派发前写死): `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`, `subagent_prompts/t4/t4_q9_extension_v1.0.md`. 规则 B 归档: `evidence/failures/step_T4.SUPP_attempt_1.md`.", "",
     "## 1. 复跑", "", "```bash", "T=.work/10_tier_b_repair",
     "python3 -I $T/scripts/t3/t3_direct_hit.py --out $T/work/t4/supp/direct_hit_head.json   # pre_existing 58 (GREEN)",
     "python3 -I $T/scripts/t4/t4_supp_sample.py   # 203 条 / 8 包; 不触碰 gate / human 样本文件",
     "python3 -I $T/scripts/t4/t4_q9_sample.py     # 192 条 / 8 包 (seed 20261131)",
     "python3 -I $T/scripts/t4/t4_supp_report.py   # 本文件 + t4_relabel_pending.md (台账只读)", "```",
     f"- 样本 md5: `work/t4/supp/supp_sample.jsonl` `{md5(f'{W}/t4/supp/supp_sample.jsonl')}`; `work/t4/q9/q9_sample.jsonl` `{md5(f'{W}/t4/q9/q9_sample.jsonl')}`. 总闸 / 人工样本文件未动 (`gate_sample.jsonl` `{md5(f'{W}/t4/gate_sample.jsonl')}`, `human_sample.jsonl` `{md5(f'{W}/t4/human_sample.jsonl')}`).", "",
     "## 2. 补检: 总体与结果 (全检, 不抽样)", "",
     "总体取自 HEAD 的台账与决策表; 一个原子只进它命中的第一层; 已被总闸审查者判过的 (gate 84 条) 与 U-5 C7 全检过的 (38 条) 不重复审.", "",
     "| 层 | 终态 | 总体 | 已在 gate 样本 | 本次审 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 层结论 |", "|---|---|--:|--:|--:|--:|--:|--:|--:|---|"]
tot = collections.Counter()
for p in pop:
    if not p["population"]:
        o.append(f"| {p['layer']} | — | 0 | 0 | 0 | — | — | — | — | 总体为空 (T1 的 LOCATE 类在 T2 已全部定位) |")
        continue
    c = collections.Counter(supp[a]["verdict"] for a in p["checked_here"])
    tot.update(c)
    res = "**不通过**" if c["NOT_HOLD"] or c["UNVERIFIABLE"] else "通过"
    o.append(f"| {p['layer']} | {', '.join(p['final'])} | {p['population']} | {len(p['in_gate'])} | {len(p['checked_here'])} | {c['HOLDS']} | {c['HOLDS_AS_EQUIV']} | {c['NOT_HOLD']} | {c['UNVERIFIABLE']} | {res} |")
o += [f"| **合计** | | | | **{sum(tot.values())}** | **{tot['HOLDS']}** | **{tot['HOLDS_AS_EQUIV']}** | **{tot['NOT_HOLD']}** | **{tot['UNVERIFIABLE']}** | |", "",
      "- `FIG` 11 条 = 终态 FIGURE_DEFERRED 全部 = triage 类 FIGURE 全部 (同一批原子); 审查者逐条看了渲染页, 并核了 KB 里的 Mermaid 再现与原图不矛盾.",
      "- attempt 1 审查者点名的规则计数与今天不同, 原因是解冻轮 (W3) 改了规则名, 不是总体漏算:", "",
      "| 规则 | attempt 1 时 (`3a24a1c` 的决策表) | HEAD | 变化来源 (旧规则 → 新规则: 条数) |", "|---|--:|--:|---|"]
for r in RULES:
    mv = "; ".join(f"`{a}` → 本规则: {n}" for (a, b), n in moved.items() if b == r) or "—"
    o.append(f"| `{r}` | {cnt(dec_old, r)} | {cnt(dec_now, r)} | {mv} |")
o += ["", "### 2.1 NOT_HOLD (2 条, 都在 PRE_EXISTING 层)", "", "| # | atom_id | 终态 | 审查者结论 (摘) | 原始结果 |", "|--:|---|---|---|---|"]
for a, r in supp.items():
    if r["verdict"] == "NOT_HOLD":
        o.append(f"| {r['num']} | `{a}` | {r['final']} | {r['note'].replace('|', '¦')} | `{r['raw']}` |")
o += ["", "含义: 这两条是 SDTM v2.0 §6.6 APRELSUB 变量表的 APID / RDEVID 行. KB 该表只有 5 列 (# / Variable / Label / Type / Role), 这 5 格与 PDF 一致; PDF 的 Notes 格文字 KB 本表没有, 06 的旧匹配器把它们配到了 §4 的另一张表上, 所以旧 EXACT 不成立. **不是 KB 写错**: v2.0 变量表只收精简列是 T1.4 R1 用户已裁定的做法; 问题在旧标签.", "",
      "### 2.2 HOLDS_AS_EQUIV (30 条, 都在 PRE_EXISTING 层; 内容成立, 标签级别偏高)", "", "| 原因 | 条数 | 原子 |", "|---|--:|---|"]
grp = collections.OrderedDict()
for a, r in supp.items():
    if r["verdict"] == "HOLDS_AS_EQUIV":
        k = ("已登记 PDF 笔误造成的差异 (" + TYPO[a] + "); 标签宜为 PDF_TYPO") if a in TYPO else \
            ("PDF 省略列字符 `…` (U+2026), KB 写 `...` (EG Ex3 表, p191)" if a.startswith("ig34_p0191") else
             ("ML CRF: PDF 用粗体 X 标选中项, KB 写 `[X]` / `[ ]`" if a.startswith("ig34_p0123") else "同格分行合并 / 填空线长度 (CE CRF p153)"))
        grp.setdefault(k, []).append(a)
for k, v in grp.items():
    o.append(f"| {k} | {len(v)} | {', '.join('`' + x + '`' for x in v[:6])}{' …' if len(v) > 6 else ''} |")
o += ["", "这 30 条在各覆盖率口径里仍算已覆盖 (EXACT 与 EQUIVALENT 同计); 其中 4 条登记笔误的见 `t4_relabel_pending.md` (改 PDF_TYPO 会影响 strict 口径). 其余 26 条归入 \"标签级别\" 后续项 (同 U-10⑤), 不改.", "",
      "## 3. Q9 扩检 (PRE_EXISTING 层不通过 → 按 PLAN §9 Q9 升级)", "",
      f"- 范围内、本项目没改过的旧标签 (stock) 共 {qp['stock_in_scope']} 条: " + " / ".join(f"{k} {v}" for k, v in qp["stock_verdicts"].items()) + ".",
      "- 旧 EXACT: 已由 `t3_direct_hit.py` 全量指纹复验, 命中不了的 58 条就是上面的 PRE_EXISTING 层 (全部审完). Q9 写的 \"全量指纹复验\" 对 EXACT 已做完.",
      f"- 旧 EQUIVALENT 指纹验不了, 另定方案: SDTM v2.0 的 {qp['equiv_sv20']} 条**全检** (出问题的正是 v2.0 变量表); SDTMIG v3.4 的 {qp['equiv_ig34']} 条按原子类型分层随机抽 {len(qp['checked']['Q9_IG34_EQUIV'])} 条 (seed {qp['seed']}; 另有 {len(qp['equiv_ig34_in_gate'])} 条已在总闸对照层判过, 全成立).", "",
      "| 层 | 总体 | 本次审 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE |", "|---|--:|--:|--:|--:|--:|--:|"]
for name, popn in (("Q9_SV20_EQUIV", qp["equiv_sv20"]), ("Q9_IG34_EQUIV", qp["equiv_ig34"])):
    c = collections.Counter(r["verdict"] for r in q9.values() if r["layer"] == name)
    o.append(f"| {name} | {popn} | {sum(c.values())} | {c['HOLDS']} | {c['NOT_HOLD_R1']} | {c['NOT_HOLD']} | {c['UNVERIFIABLE']} |")
n_ig = len(qp["checked"]["Q9_IG34_EQUIV"]) + len(qp["equiv_ig34_in_gate"])
o += ["", f"- **SDTM v2.0**: 127 条里 51 条旧 EQUIVALENT 不成立 — 49 条是变量表行 / 表头 (NOT_HOLD_R1: KB 精简列对, PDF 其它列的内容 KB 本表没收), 2 条是目录条目被跨文档配到了 SDTMIG ch10 (`sv20_p0003_a011` / `a012`). 都不是 KB 内容错.",
      f"- **SDTMIG v3.4**: 抽 65 条 0 错; 连同总闸对照层的 {len(qp['equiv_ig34_in_gate'])} 条共 {n_ig} 条 0 错. 0 错时错误率的 95% 置信上界约 {(1 - 0.05 ** (1 / n_ig)) * 100:.1f}% (按 1 − 0.05^(1/n), n = {n_ig}; 假设简单随机, 实际是分层抽). **这不等于全检**; 2207 条是否全检由主人定 (按每包 26 条约需 85 个审查实例).",
      "- NOT_HOLD_R1 按 PDF 表分布: " + ", ".join(f"p{k} {v}" for k, v in sorted(collections.Counter(A[a]["page"] for a, r in q9.items() if r["verdict"] == "NOT_HOLD_R1").items())) + ".", "",
      "## 4. 后果 (按派发前写死的条款)", "",
      "- PRE_EXISTING 层 NOT_HOLD ≥ 1 → Q9 升级已触发并执行到 §3; **主控不自行结案**. 需要主人定的事列在 `t4_owner_decisions_round2.md`.",
      f"- 待改标签共 {len(pend)} 条, 逐条清单与改后各闸数字 (在台账副本上算) 见 `t4_relabel_pending.md`. **台账现在没改** (md5 仍 `60729f7b…`): IE 要逐条清单经用户 ack 才生效 (PLAN B5), PDF_TYPO 每条要用户 ack (G-TB1).",
      "- 其余各层 (145 条) 通过: FIG 11、triage ATOM_ERR 74、RELOCATE 3、六条规则类 57.", "",
      "## 5. 审查者顺带记录的事项 (都不改 KB; KB 冻结)", "",
      "- KB 观察 (排版): `knowledge_base/domains/EG/examples.md:62-87` (Ex3 表) 省略列写 `...`, PDF p190-191 是 `…` (U+2026). S-TYPO 闭表含 `...`↔`…`, 该文件有 48 行在残余清单 (`work/t2_batches/S-TYPO.residual.jsonl`; U-9(c) 代裁 \"接受现状\").",
      "- PDF 自身不一致, 未登记: sv20 p69 SREL 行 Notes 写 \"subject or pool identified in RDEVID\", p50 同句写 \"device\" (`evidence/t4_q9_raw/pack_5.md`); ig34 p440 图中 SPC-003 标 \"(Brain)\", 同页表写 TISSUE (`evidence/t4_supp_raw/pack_6.md`).",
      "- 范围外旧标签同类错配 (未改, 只记): `sv20_p0074_a001` (PARTIAL) / `a002` / `a003` (EXACT) 被配到 SDTMIG `ch10_appendices.md` 的 Appendix F (`evidence/t4_q9_raw/pack_2.md`).",
      "- 台账指针类 (不影响标签): 若干 `md_atom_ids` 指向别的域 / 文件 (如 `ig34_p0153_a0009` → DM; `ig34_p0255_a036` → MS examples); 原子页号偏一页 (`ig34_p0169_a0025` 等实在 p170; `ig34_p0057_a001` 实在 p56). 样本包里的 KB 指针多处近似, 审查者都自行重新定位.",
      "- 标签级别 (内容成立): `ig34_p0057_a006`、`ig34_p0068_a004` (旧 EQUIVALENT, 实为原子抽错 + KB 逐字); 补检 #3 / #4 (旧 EXACT, 实为原子抽错).", ""]
open(f"{CK}/t4_supp_fullcheck.md", "w", encoding="utf-8").write("\n".join(o) + "\n")

# ---- pending relabel md
g = collections.Counter((p["group"], p["now"], p["to"]) for p in pend)
o = ["# 待改标签清单 (补检 + Q9 扩检查出; **未执行, 待主人裁定**)", "", "<!-- chain: E (plans) -->",
     f"> 状态: **待主人裁定** (2026-11-27). 台账 `work/coverage_ledger.wc.jsonl` 未改 (md5 `{md5(led)}`). 本文件由 `scripts/t4/t4_supp_report.py` 生成; 依据是独立审查者的原始结果 (\"原始结果\" 列), 主控未改判.",
     "> 为什么不直接改: IE 须逐条清单经用户 ack 才生效 (PLAN §3.1 B5); PDF_TYPO 每条须用户 ack (G-TB1); 主人即将确认的 U-1 口径数字建立在当前台账上.", "",
     "## 1. 要主人选的", "",
     "| 组 | 条数 | 现标签 → 建议 | 选项 |", "|---|--:|---|---|"]
OPT = {"R1-row": "A = 认 IE (与 T1.4 R1 对 70 条 v2.0 变量表行的裁定同类, 不动 KB) / B = 把 PDF 这些列补进 KB 的 model 表 (要解冻 KB, 另开批) / C = 其它",
       "v2.0-TOC": "A = 认 IE (同页 §7 / §8 两条目录条目已是 IE VERSION_MISMATCH) / B = 其它",
       "registered-typo": "A = 改标 PDF_TYPO (与范围内同类一致; U-1 B 口径下仍算覆盖, strict 口径下不算) / B = 维持 EXACT (与 \"逐字\" 定义不符)"}
for (grp_, now, to_), n in sorted(g.items()):
    o.append(f"| {grp_} | {n} | {now} → {to_} | {OPT[grp_]} |")
o += ["", "## 2. 若三组都按建议改, 各闸数字 (在台账**副本**上算, 命令见 §4)", "", "| 项 | 现在 (台账未改) | 改后 (预演) |", "|---|---|---|"]
lab = {"final strict": "G-TB3 strict", "final mapped": "G-TB3 mapped", "final U-1 B": "G-TB3 U-1 B 口径", "content EXACT+EQUIV": "内容指标 (EXACT+EQUIV)"}
for a, b in zip(now_dec, prev_dec):
    k = a.split(":")[0].strip()
    o.append(f"| {lab.get(k, k)} | {a.split(':', 1)[1].split('(')[0].strip()} | {b.split(':', 1)[1].split('(')[0].strip()} |")
o.append(f"| G-TB1 / G-TB2 (范围内) | {now_tb[0].split('sections=')[1]} | {prev_tb[0].split('sections=')[1]} |")
o += ["", "- 99.02% 的闸线 (06 口径 99.0192%) 在 U-1 B 口径下改前改后都高于; strict 口径改前改后都低于 (与 attempt 2 相同的性质).",
      "- 改标只动标签, 不动 KB. 真正执行时走 writer (`oh-my-claudecode:executor`) → reviewer, 并在同一次回写里一并处理 registry `B-IS T-6` 页号 p241 → p239 (见 `t4_owner_decisions_round2.md` 末节: 页号参与登记匹配, 单独改有改变台账的风险).", "",
      "## 3. 逐条", "", "| # | atom_id | 页 | 节 | 现标签 | 建议 | 组 | 理由 | 原始结果 |", "|--:|---|--:|---|---|---|---|---|---|"]
for n_, p in enumerate(pend, 1):
    a = A[p["atom_id"]]
    o.append(f"| {n_} | `{p['atom_id']}` | {a['page']} | {a['parent_section'][:44].replace('|', '¦')} | {p['now']} | {p['to']} | {p['group']} | {p['why']} | `{p['raw']}` |")
o += ["", "## 4. 复跑", "", "```bash", "python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_report.py",
      "# 预演台账副本: work/scratch/t4/relabel_preview/ledger_preview.jsonl (gitignored); 工作台账 md5 断言不变", "```", ""]
open(f"{CK}/t4_relabel_pending.md", "w", encoding="utf-8").write("\n".join(o) + "\n")
print("supp", dict(collections.Counter(r["verdict"] for r in supp.values())), "| q9", dict(collections.Counter(r["verdict"] for r in q9.values())))
print("pending relabels", len(pend), dict(g))
print("now :", now_dec, now_tb)
print("prev:", prev_dec, prev_tb)
print("rule moves:", dict(moved))
