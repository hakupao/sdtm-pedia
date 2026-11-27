#!/usr/bin/env python3
"""Collect the reviewers' per-atom verdicts of the T4.1 supplementary full check (evidence/t4_supp_raw), the Q9 extension
(evidence/t4_q9_raw) and the round-2 follow-up (evidence/t4_round2_raw); write
  work/t4/supp/verdicts.json                      every atom: layer, final verdict, reviewer verdict, raw file:line
  work/t4/supp/relabel_pending.json               the label changes these results call for (NOT applied to the ledger)
  work/t4/supp/scenarios.json                     gate numbers per option, computed on scratch COPIES of the ledger
  evidence/checkpoints/t4_supp_fullcheck.md       summary (main-controller transcript; raw files are the reviewers' own)
  evidence/checkpoints/t4_relabel_pending.md      the pending list + the scenario table
Nothing here writes the working ledger or the KB. Text after the REVIEW marker of t4_supp_fullcheck.md is kept across re-runs.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_report.py
"""
import collections, glob, hashlib, json, os, re, subprocess

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
W = f"{TB}/work"
CK = f"{TB}/evidence/checkpoints"
SC = f"{W}/scratch/t4/relabel_preview"
MARK = "<!-- REVIEW: 以下由主控手写 / 誊录, 脚本重跑时原样保留 -->"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
VERD = ["NOT_HOLD_SELF", "NOT_HOLD_XDOC", "NOT_HOLD_R1", "HOLDS_AS_EQUIV", "TYPO_AFFECTED", "NOT_AFFECTED", "NOT_HOLD", "UNVERIFIABLE", "HOLDS"]
# supplementary-check rows judged HOLDS_AS_EQUIV whose only KB/PDF difference is a registered PDF typo (reviewer text names the id)
TYPO = {"ig34_p0147_a025": "B-BE T-3", "ig34_p0262_a016": "B-MB T-1", "ig34_p0262_a017": "B-MB T-1", "ig34_p0296_a023": "B-NV T-2"}


def parse(raw_dir, samples, need_all=True):
    ids = {}
    for s in samples:
        if os.path.exists(s):
            ids.update({x["atom_id"]: x for x in lj(s)})
    got = {}
    for f in sorted(glob.glob(f"{raw_dir}/pack_*.md")):
        for n, l in enumerate(open(f, encoding="utf-8"), 1):
            if not l.startswith("|"):
                continue
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            m = re.search(r"((?:ig34|sv20)_p\d{4}_a\d+)", cells[1]) if len(cells) >= 4 else None
            if not m or m.group(1) not in ids or m.group(1) in got:
                continue
            v = None
            for c in cells[2:6]:
                c2 = c.replace("*", "").replace("`", "").strip()
                v = next((x for x in VERD if c2 == x or c2.startswith(x + " ") or c2.startswith(x + "(")), None)
                if v:
                    break
            if v:
                x = ids[m.group(1)]
                got[m.group(1)] = dict(num=cells[0], layer=x["layer"].split(":", 1)[1], final=x["verdict_final"], verdict=v,
                                       raw=f"{os.path.relpath(f, TB)}:{n}", note=cells[-1][:160], reg=x.get("sib_registry"), line=l)
    miss = [a for a in ids if a not in got]
    if need_all:
        assert not miss, (raw_dir, miss[:5])
    return got, miss


supp, _ = parse(f"{TB}/evidence/t4_supp_raw", [f"{W}/t4/supp/supp_sample.jsonl"])
q9, _ = parse(f"{TB}/evidence/t4_q9_raw", [f"{W}/t4/q9/q9_sample.jsonl"])
r2, r2_missing = parse(f"{TB}/evidence/t4_round2_raw", [f"{W}/t4/round2/round2_sample.jsonl", f"{W}/t4/round2/round2b_sample.jsonl"], need_all=False)
r3, r3_missing = parse(f"{TB}/evidence/t4_round3_raw", [f"{W}/t4/round3/round3_sample.jsonl"])
json.dump(dict(round3={k: {x: y for x, y in v.items() if x != "line"} for k, v in r3.items()}, supp={k: {x: y for x, y in v.items() if x != "line"} for k, v in supp.items()}, q9={k: {x: y for x, y in v.items() if x != "line"} for k, v in q9.items()}, round2={k: {x: y for x, y in v.items() if x != "line"} for k, v in r2.items()}, round2_missing=r2_missing), open(f"{W}/t4/supp/verdicts.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ---- pending label changes (not applied)
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
pend = []
for d in (supp, q9, r2):
    for a, r in d.items():
        if r["verdict"] == "NOT_HOLD_R1" or (r["verdict"] == "NOT_HOLD" and r["layer"] == "PRE_EXISTING"):
            pend.append(dict(atom_id=a, now=r["final"], to="INTENTIONAL_EXCLUDE", group="R1-row",
                             why="SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类)", raw=r["raw"]))
        elif r["verdict"] == "NOT_HOLD" and r["layer"] == "Q9_SV20_EQUIV":
            pend.append(dict(atom_id=a, now=r["final"], to="INTENTIONAL_EXCLUDE", group="v2.0-TOC",
                             why="SDTM v2.0 目录条目, 对应章节 KB 未收 (同页 a009 / a010 已是 IE VERSION_MISMATCH)", raw=r["raw"]))
        elif a in TYPO:
            pend.append(dict(atom_id=a, now=r["final"], to="PDF_TYPO", group="registered-typo",
                             why=f"KB 与 PDF 的差异 = 已登记 PDF 笔误 {TYPO[a]} (KB 写正确值)", raw=r["raw"], registry=TYPO[a]))
        elif r["verdict"] == "TYPO_AFFECTED":
            named = [g_ for g_ in (r.get("reg") or []) if g_ in r["line"]]   # the id(s) the reviewer wrote in that row
            assert len(named) == 1, (a, r.get("reg"), named)
            pend.append(dict(atom_id=a, now=r["final"], to="PDF_TYPO", group="registered-typo",
                             why=f"KB 与 PDF 的差异 = 已登记 PDF 笔误 {named[0]} (KB 写正确值; 审查者在原始结果该行确认)", raw=r["raw"], registry=named[0]))
for a, r in r3.items():
    if r["verdict"] == "TYPO_AFFECTED":
        named = [g_ for g_ in (r.get("reg") or []) if g_ in r["line"]]
        assert len(named) == 1 and r["layer"] == "R3_XTYPO", (a, named)
        pend.append(dict(atom_id=a, now=r["final"], to="PDF_TYPO", group="registered-typo-oos",
                         why=f"范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 {named[0]} (KB 写正确值; 审查者对渲染页确认)", raw=r["raw"], registry=named[0]))
    elif r["verdict"] == "NOT_HOLD" and r["layer"] == "R3_PDF_TYPO":
        pend.append(dict(atom_id=a, now=r["final"], to="EXACT", group="typo-overlabel",
                         why="登记的笔误不在这条原子里 (在相邻原子 / 另一张表); 这条 KB 与 PDF 逐字一致, 现标 PDF_TYPO 多标了", raw=r["raw"]))
assert len({p["atom_id"] for p in pend}) == len(pend)
pend.sort(key=lambda x: (x["group"], x["atom_id"]))
json.dump(pend, open(f"{W}/t4/supp/relabel_pending.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ---- gate numbers per option, on scratch copies of the ledger
os.makedirs(SC, exist_ok=True)
led = f"{W}/coverage_ledger.wc.pre_r2l.jsonl"   # frozen pre-R2L ledger (rule-B backup): the baseline every scenario is rehearsed on
LEDGER_MD5 = "60729f7b64b7c1dfaf2174e394f6dd9c"   # value cited in t4_attempt2_report.md; asserted unchanged below
LIVE = f"{W}/coverage_ledger.wc.jsonl"          # working ledger after the R2L batch (read-only here)
rows = lj(led)
L = {r["pdf_atom_id"]: r for r in rows}
r2pop = json.load(open(f"{W}/t4/round2/round2_population.json"))
XOUT = r2pop["xdoc_out_of_scope"]
P74 = sorted(a for a in XOUT if a.startswith("sv20_p0074_"))
# out-of-scope atoms hit by a registered typo, confirmed on the text layer by the delta reviewer (review_c.md H4); not reviewed by a tracer
XTYPO = ["ig34_p0083_a020", "ig34_p0304_a026", "ig34_p0304_a027", "ig34_p0304_a028", "ig34_p0304_a029", "ig34_p0316_a023"]
grp = lambda *g: {p["atom_id"]: p["to"] for p in pend if p["group"] in g}


def scen(name, to):
    f = f"{SC}/ledger_{name}.jsonl"
    with open(f, "w", encoding="utf-8") as fh:
        for r in rows:
            r2_ = dict(r)
            if r2_["pdf_atom_id"] in to:
                r2_["verdict"] = to[r2_["pdf_atom_id"]]
            fh.write(json.dumps(r2_, ensure_ascii=False) + "\n")
    return dict(n=len(to), **nums(f, name))


def nums(f, name):
    out = subprocess.run(["python3", "-I", f"{TB}/scripts/t4/t4_coverage_decomp.py", f], capture_output=True, text=True, cwd=ROOT).stdout
    d = {l.split(":")[0].strip(): l.split(":", 1)[1].split("(")[0].strip() for l in out.splitlines() if l.startswith(("final", "content"))}
    tb = subprocess.run(["python3", "-I", f"{TB}/scripts/t3_recompute.py", "--ledger", f, "--out", f"{SC}/sc_{name}.jsonl"], capture_output=True, text=True, cwd=ROOT).stdout
    g = next(l for l in tb.splitlines() if "§5.0 scope" in l)
    return dict(u1b=d["final U-1 B"], strict=d["final strict"], mapped=d["final mapped"], content=d["content EXACT+EQUIV"],
                g1=re.search(r"G-TB1 pass=(\S+)", g).group(1), g2_literal=re.search(r"G-TB2 pass=(\S+)", g).group(1), residual=re.search(r"residual_gap=(\d+)", g).group(1))


ALL = grp("R1-row", "v2.0-TOC", "registered-typo")
DECIDED = grp("R1-row", "v2.0-TOC", "registered-typo", "registered-typo-oos")   # owner 2026-11-27: 1A / 2A / 3A / 7b-A
assert set(XTYPO) == set(grp("registered-typo-oos")), "round-3 confirmed out-of-scope typo atoms differ from the delta reviewer's list"
SCEN = collections.OrderedDict([
    ("都不改 (现状)", scen("now", {})),
    ("只改: 变量表行 → 有意不收", scen("r1", grp("R1-row"))),
    ("只改: 目录条目 → 有意不收", scen("toc", grp("v2.0-TOC"))),
    ("只改: 笔误原子 → PDF 笔误", scen("typo", grp("registered-typo"))),
    ("变量表行 + 目录条目", scen("r1_toc", grp("R1-row", "v2.0-TOC"))),
    ("变量表行 + 笔误原子", scen("r1_typo", grp("R1-row", "registered-typo"))),
    ("三组都改 (建议)", scen("all", ALL)),
    ("三组都改 + 范围外 p74 的 14 条 → 有意不收", scen("all_p74", {**ALL, **{a: "INTENTIONAL_EXCLUDE" for a in P74}})),
    ("三组都改 + 范围外跨文档指针 146 条全 → 有意不收 (按都认 IE 计的情形)", scen("all_xout", {**ALL, **{a: "INTENTIONAL_EXCLUDE" for a in XOUT}})),
    ("三组都改 + 范围外已登记笔误同类 6 条 → PDF 笔误 (= 主人已定的全部: 1A / 2A / 3A / 7b-A)", scen("decided", DECIDED)),
    ("主人已定的全部 + 4 条多标的 PDF 笔误 → 逐字 (待主人定)", scen("decided_plus4", {**DECIDED, **grp("typo-overlabel")})),
])
json.dump(SCEN, open(f"{W}/t4/supp/scenarios.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
assert md5(led) == LEDGER_MD5, md5(led)
# ---- what the R2L batch actually did to the working ledger, checked against the list
LIVE_MD5 = md5(LIVE)
LV = collections.defaultdict(set)
for r in lj(LIVE):
    LV[r["pdf_atom_id"]].add(r["verdict"])
APPLIED = [p["atom_id"] for p in pend if LV[p["atom_id"]] == {p["to"]}]
NOT_APPLIED = [p["atom_id"] for p in pend if LV[p["atom_id"]] == {p["now"]}]
assert len(APPLIED) + len(NOT_APPLIED) == len(pend), "a listed atom is in neither its old nor its proposed label"
# owner 2026-11-27: 1A / 2A / 3A / 7b-A (R2L batch, 78) and, after gate attempt 3, A1 (R3L batch, 4) -> all listed atoms applied
DECIDED_ALL = {**DECIDED, **grp("typo-overlabel")}
assert set(APPLIED) == set(DECIDED_ALL), "applied set differs from what the owner decided (1A / 2A / 3A / 7b-A / A1)"
assert NOT_APPLIED == [], NOT_APPLIED
R2L_MD5, N_R2L, N_R3L = "16024ac09721cb3f8519cd68fa455196", len(DECIDED), len(grp("typo-overlabel"))
assert md5(f"{W}/coverage_ledger.wc.pre_r3l.jsonl") == R2L_MD5   # the ledger between the two batches
changed_live = sum(1 for a, b in zip(rows, lj(LIVE)) if a["verdict"] != b["verdict"])
assert len(rows) == len(lj(LIVE)) and changed_live == len(APPLIED), changed_live
LIVE_NUMS = nums(LIVE, "live")
DEC_KEY = next(k for k in SCEN if "4 条多标的 PDF 笔误" in k)   # = everything the owner decided, R2L + R3L
assert LIVE_NUMS == {k: v for k, v in SCEN[DEC_KEY].items() if k != "n"}, (LIVE_NUMS, SCEN[DEC_KEY])

# ---- reconcile the rule counts quoted by the attempt-1 reviewer with today's
dec_now = json.load(open(f"{W}/t3_writeback_decisions.json"))
dec_old = json.loads(subprocess.check_output(["git", "-C", ROOT, "show", "3a24a1c:.work/10_tier_b_repair/work/t3_writeback_decisions.json"]))
RULES = ["T1-two-agent", "T1-two-agent+T2-rework", "T2-fix+deltaRereviewPASS+auditPASS", "live-hit(was-IE-ack)", "C1-manual-PDF+KB", "C7-K4-rereview"]
cnt = lambda d, r: sum(1 for x in d.values() if x.get("rule") == r)
moved = collections.Counter((dec_old.get(i, {}).get("rule", "(不在决策表)"), d.get("rule")) for i, d in dec_now.items()
                            if d.get("rule") in RULES and dec_old.get(i, {}).get("rule") != d.get("rule"))
ub = lambda n: (1 - 0.05 ** (1 / n)) * 100
vc = lambda d, layer=None: collections.Counter(r["verdict"] for r in d.values() if layer is None or r["layer"] == layer)

# ---- summary md
pop = json.load(open(f"{W}/t4/supp/supp_population.json"))
qp = json.load(open(f"{W}/t4/q9/q9_population.json"))
o = ["# T4.1 补检 (\"0 抽中\" 各类全检) + Q9 扩检 + 第二轮补检 — 汇总", "", "<!-- chain: E (plans) -->",
     f"> 状态: **补检 PRE_EXISTING 层不通过 → 触发 Q9 升级; Q9 扩检与第二轮补检已跑完; 共查出 {len(pend)} 条标签应改, 主人都已直接定, 全部已执行: {N_R2L} 条 (1A / 2A / 3A / 7b-A) 由 R2L 批, {N_R3L} 条多标的 PDF_TYPO (问题 A = A1) 由 R3L 批; 1 条判不了的 (问题 B = B1) 维持 PDF_TYPO 并写明无法判定** (2026-11-27). KB 未改; 台账 `{LEDGER_MD5[:8]}…` → (R2L) `{R2L_MD5[:8]}…` → (R3L) `{LIVE_MD5[:8]}…`; 备份 `work/coverage_ledger.wc.pre_r2l.jsonl` / `work/coverage_ledger.wc.pre_r3l.jsonl`; 见 `t4_round2_ledger_W.md` / `t4_round2_ledger_review.md` / `t4_round2_ledger_audit.md` 与 `t4_round3_ledger_W.md` / `t4_round3_ledger_review.md`.",
     "> 审查: `oh-my-claudecode:tracer` (opus) 独立实例, 只读: 补检 8 + Q9 8 + 第二轮 8. 原始结果由审查者自己写入 `evidence/t4_supp_raw/`、`evidence/t4_q9_raw/`、`evidence/t4_round2_raw/`. 本文件 §1-§6 是主控用 `scripts/t4/t4_supp_report.py` 从原始结果机械汇总的, 不改判 (规则 D); 文末一节是主控手写的 \"独立审查 B 的处理\".",
     "> 口径 (派发前写死): `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`, `t4_q9_extension_v1.0.md`, `t4_supp_round2_v1.0.md`. 规则 B 归档: `evidence/failures/step_T4.SUPP_attempt_1.md`. 对本汇总的独立审查原文: `evidence/t4_gap_review_raw/review_b.md`.", "",
     "## 1. 复跑", "", "```bash", "T=.work/10_tier_b_repair",
     "python3 -I $T/scripts/t3/t3_direct_hit.py --out $T/work/t4/supp/direct_hit_head.json   # GREEN; pre_existing: R2L 之前 58 (补检取的就是这 58 条), R2L 之后 52 (其中 6 条改标后不再是 EXACT)",
     "python3 -I $T/scripts/t4/t4_supp_sample.py     # 补检 203 条 / 8 包",
     "python3 -I $T/scripts/t4/t4_q9_sample.py       # Q9 192 条 / 8 包 (seed 20261131)",
     "python3 -I $T/scripts/t4/t4_round2_sample.py   # 第二轮 135 条 / 7 包 (seed 20261132)",
     "python3 -I $T/scripts/t4/t4_round2b_sample.py  # 第二轮补充 40 条 / 2 包",
     "python3 -I $T/scripts/t4/t4_supp_report.py     # 本文件 + t4_relabel_pending.md (台账只读; 各选法在改前备份台账的副本上预演)", "```",
     "- 这些抽样脚本不触碰总闸 / 人工样本文件 (`gate_sample.jsonl` `" + md5(f"{W}/t4/gate_sample.jsonl") + "`, `human_sample.jsonl` `" + md5(f"{W}/t4/human_sample.jsonl") + "`); 它们只 exec `t4_sample.py` / `t4_render.py` 的定义段.",
     "- 样本 md5: supp `" + md5(f"{W}/t4/supp/supp_sample.jsonl") + "`; q9 `" + md5(f"{W}/t4/q9/q9_sample.jsonl") + "`; round2 `" + md5(f"{W}/t4/round2/round2_sample.jsonl") + "`" +
     ("; round2b `" + md5(f"{W}/t4/round2/round2b_sample.jsonl") + "`" if os.path.exists(f"{W}/t4/round2/round2b_sample.jsonl") else "") + ".", "",
     "## 2. 补检: 总体与结果 (全检, 不抽样)", "",
     "总体取自 HEAD 的台账与决策表; 一个原子只进它命中的第一层; 已被总闸审查者判过的 (gate 84 条) 与 U-5 C7 全检过的 (38 条) 不重复审.", "",
     "| 层 | 终态 | 总体 | 已在 gate 样本 | 本次审 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 层结论 |", "|---|---|--:|--:|--:|--:|--:|--:|--:|---|"]
tot = collections.Counter()
for p in pop:
    if not p["population"]:
        o.append(f"| {p['layer']} | — | 0 | 0 | 0 | — | — | — | — | 总体为空 (T1 的 28 条 LOCATE 在 T1.4 定批时按 `ruling:LOCATE-LB` 转成了 REAL_GAP, 归 B-LB 批; `t2_batch_table.md:18`) |")
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
g2 = collections.OrderedDict()
for a, r in supp.items():
    if r["verdict"] == "HOLDS_AS_EQUIV":
        k = ("已登记 PDF 笔误造成的差异 (" + TYPO[a] + "); 标签宜为 PDF_TYPO") if a in TYPO else \
            ("PDF 省略列字符 `…` (U+2026), KB 写 `...` (EG Ex3 表, p191)" if a.startswith("ig34_p0191") else
             ("ML CRF: PDF 用粗体 X 标选中项, KB 写 `[X]` / `[ ]`" if a.startswith("ig34_p0123") else "同格分行合并 / 填空线长度 (CE CRF p153)"))
        g2.setdefault(k, []).append(a)
for k, v in g2.items():
    o.append(f"| {k} | {len(v)} | {', '.join('`' + x + '`' for x in v[:6])}{' …' if len(v) > 6 else ''} |")
o += ["", "这 30 条在各覆盖率口径里仍算已覆盖 (EXACT 与 EQUIVALENT 同计); 其中 4 条登记笔误的进 `t4_relabel_pending.md` (改 PDF_TYPO 会影响 strict 口径). 其余 26 条归入 \"标签级别\" 后续项 (同 U-10⑤), 不改.", "",
      "## 3. Q9 扩检 (PRE_EXISTING 层不通过 → 按 PLAN §9 Q9 升级)", "",
      f"- 范围内、本项目没改过的旧标签 (stock), **不含标题类原子** (G-TB1 的定义就是 \"非 HEADING\"): {qp['stock_in_scope']} 条 = " + " / ".join(f"{k} {v}" for k, v in qp["stock_verdicts"].items()) + ". 范围内另有 stock 标题类原子 EXACT 149 / EQUIVALENT 167, 不在指纹复验里也不在 Q9 里 (其中 11 条因台账指针跨文档在第二轮 XDOC 层审过, 见 §4).",
      "- 旧 EXACT: `scripts/t3/t3_direct_hit.py` 做的是全量指纹复验 — 原子文字须在它的目标文件里逐字命中并锚在本节. 它检查 1758 条 (上面 1753 条 + 5 条虽在决策表里但标签未变的), 命中不了的 58 条就是 §2 的 PRE_EXISTING 层 (全部审完). **它验不了两件事**: ① 目标文件属于另一份 PDF 的 KB 文件时不做节锚点检查 (`t3_common.py` 的 `anchor_ok` 直接放行), 即不判 \"文字落在哪份文档\"; ② 原子抽取时把 PDF 的笔误 \"顺手改对\" 了的, 原子文字 = KB 改正值, 指纹照样命中 — 这两类分别由第二轮的 XDOC 层与 TYPO_SIB 层补 (§4).",
      f"- 旧 EQUIVALENT 指纹验不了, 另定方案: SDTM v2.0 的 {qp['equiv_sv20']} 条**全检** (出问题的正是 v2.0 变量表); SDTMIG v3.4 的 {qp['equiv_ig34']} 条按原子类型分层随机抽 {len(qp['checked']['Q9_IG34_EQUIV'])} 条 (seed {qp['seed']}).", "",
      "| 层 | 总体 | 本次审 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE |", "|---|--:|--:|--:|--:|--:|--:|"]
for name, popn in (("Q9_SV20_EQUIV", qp["equiv_sv20"]), ("Q9_IG34_EQUIV", qp["equiv_ig34"])):
    c = vc(q9, name)
    o.append(f"| {name} | {popn} | {sum(c.values())} | {c['HOLDS']} | {c['NOT_HOLD_R1']} | {c['NOT_HOLD']} | {c['UNVERIFIABLE']} |")
n65 = len(qp["checked"]["Q9_IG34_EQUIV"])
n_ig = n65 + len(qp["equiv_ig34_in_gate"])
o += ["", "- **SDTM v2.0**: 127 条里 51 条旧 EQUIVALENT 不成立 — 49 条是变量表行 / 表头 (NOT_HOLD_R1: KB 精简列对, PDF 其它列的内容 KB 本表没收), 2 条是目录条目被跨文档配到了 SDTMIG ch10 (`sv20_p0003_a011` / `a012`). 都不是 KB 内容错.",
      f"- **SDTMIG v3.4**: 抽 {n65} 条 0 错 → 错误率 95% 置信上界约 **{ub(n65):.1f}%** (1 − 0.05^(1/{n65})). 若把总闸对照层判过的 {len(qp['equiv_ig34_in_gate'])} 条也算上 (另一个抽样框), {n_ig} 条 0 错 → 约 {ub(n_ig):.1f}%. 两个数都是近似: 按简单随机算, 实际是按原子类型分层且不按比例. **这不等于全检**; 是否够由主人定.",
      "- NOT_HOLD_R1 按 PDF 页分布: " + ", ".join(f"p{k} {v}" for k, v in sorted(collections.Counter(A[a]["page"] for a, r in q9.items() if r["verdict"] == "NOT_HOLD_R1").items())) + ".",
      "- 与 Q9 brief 的一处偏离 (收紧, 不是放宽): brief 的后果条款写 \"NOT_HOLD_R1 → 台账改标 IE (R1, 用户已 ack 的类别)\"; 实际没有直接改, 而是列入待改清单请主人定 — 协调方 2026-11-27 指示 \"不按委托代裁处理, 先不改台账\" (`t4_coordinator_note_20261127.md`), 且 R1 当时 ack 的是列出的 70 条, 这 51 条不在其中.", "",
      "## 4. 第二轮补检 (独立审查 B 指出的三处没覆盖到)", ""]
xc, sc_, s2c, tc = vc(r2, "XDOC"), vc(r2, "TYPO_SIB"), vc(r2, "TYPO_SIB2"), vc(r2, "PDF_TYPO")
n_sib2 = len(lj(f"{W}/t4/round2/round2b_sample.jsonl")) if os.path.exists(f"{W}/t4/round2/round2b_sample.jsonl") else 0
sib2_state = " (全检)" if n_sib2 and sum(s2c.values()) == n_sib2 else f" / {n_sib2} (**结果未齐**)"
o += ["| 层 | 取法 | 本次审 | 结果 |", "|---|---|--:|---|",
      f"| XDOC | 范围内 stock EXACT / EQUIVALENT (含标题类) 且台账 `md_atom_ids` 只指向另一份文档的 KB 文件; 这一筛法筛出 {len(r2pop['xdoc_in_scope'])} 条 (与第 1 稿的 \"57 条待改\" 只是数字相同, 无关), 其中 {len(r2pop['xdoc_in_scope_already_judged'])} 条已在 Q9 / 补检审过 | {sum(xc.values())} (全检) | HOLDS {xc['HOLDS']} / NOT_HOLD_XDOC {xc['NOT_HOLD_XDOC']} / NOT_HOLD_R1 {xc['NOT_HOLD_R1']} / NOT_HOLD {xc['NOT_HOLD']} / UNVERIFIABLE {xc['UNVERIFIABLE']} |",
      f"| TYPO_SIB | 范围内 EXACT / EQUIVALENT, 与某条 \"KB 写正确值\" 登记同页 (±1), 原子文字含改正值且与登记所在 KB 行重合 ≥ 0.8; 候选 {len(r2pop['typo_sib_candidates'])} 条, 其中 {len(r2pop['typo_sib_already_judged'])} 条已审过 | {sum(sc_.values())} (全检) | TYPO_AFFECTED {sc_['TYPO_AFFECTED']} / NOT_AFFECTED {sc_['NOT_AFFECTED']} / NOT_HOLD {sc_['NOT_HOLD']} / UNVERIFIABLE {sc_['UNVERIFIABLE']} |",
      f"| TYPO_SIB2 | 同上但原子文字**不含**改正值, 只取 EQUIVALENT (EXACT 须逐字命中 KB, 覆盖笔误处的 EXACT 原子必含改正值); 候选 {n_sib2} 条 | {sum(s2c.values())}{sib2_state} | TYPO_AFFECTED {s2c['TYPO_AFFECTED']} / NOT_AFFECTED {s2c['NOT_AFFECTED']} / NOT_HOLD {s2c['NOT_HOLD']} / UNVERIFIABLE {s2c['UNVERIFIABLE']} |",
      f"| PDF_TYPO | (第二轮当时, R2L 之前) 终态 PDF_TYPO {r2pop['pdf_typo_total']} 条里未被任何审查者看过的 {r2pop['pdf_typo_unjudged']} 条, 按判定规则分层各抽 15 (seed {r2pop['seed']}) | {sum(tc.values())} (抽样) | HOLDS {tc['HOLDS']} / NOT_HOLD {tc['NOT_HOLD']} / UNVERIFIABLE {tc['UNVERIFIABLE']} |", "",
      "- **XDOC**: 没有跨文档误配 — 16 条 SDTMIG 非标题原子与 8 条标题原子的内容都在 SDTMIG 自己的 KB 文件里 (台账指针指向 model/ 只是旧匹配器的指针问题). 3 条 NOT_HOLD 都是标题类, 属口径问题而非内容问题: `ig34_p0079_a001` (5.3 SE) 与 `ig34_p0442_a001` (9.2 OI) — KB 域文件标题 `# XX — 域名` 不带 PDF 节号; `ig34_p0441_a006` (9.1 Device Identifiers) — KB 对应标题是自拟的 `## DI – Description/Overview (§9.1)`. 审查者指出 64 个域目录里 57 个同型. 标题类不在 G-TB1 范围内; 口径交主人定 (`t4_owner_decisions_round2.md`).",
      f"- **TYPO_SIB / TYPO_SIB2**: {sc_['TYPO_AFFECTED'] + s2c['TYPO_AFFECTED']} 条原子所在处 PDF 印的是已登记的笔误、KB 是改正值, 现标签 EXACT / EQUIVALENT 不准 → 进待改清单 (改 PDF_TYPO). 其余候选的笔误实际在同页别处." +
      (f" TYPO_SIB2 另有 NOT_HOLD {s2c['NOT_HOLD']} 条, 见 §6." if s2c["NOT_HOLD"] else ""),
      f"- **PDF_TYPO**: 抽 {sum(tc.values())} 条 0 错 → 错误率 95% 上界约 {ub(max(1, sum(tc.values()))):.1f}% (同样是近似). 连同总闸样本里判过的 5 条共 {sum(tc.values()) + 5} 条看过; PDF_TYPO 类**不是全检**. attempt 1 要求的 \"ATOM_ERR / PDF_TYPO 合计补抽到 ≥ 30\" 现为: ATOM_ERR 侧 C7 38 + triage 74 + K4 2 全检, PDF_TYPO 侧抽 {sum(tc.values())}.",
      "- **TYPO 筛法的盲区 (delta 复审 M5; 如实)**: ① 只按登记的 `pdf_page` ±1 取原子, 而有些登记实际跨多页 (页段写在 `pdf_value` / `basis` 的文字里); ② 与 KB 行比重合度时只用登记给的行号; ③ TYPO_SIB2 不收 EXACT. delta 复审者另用 \"PDF 笔误写法的 token 在全 KB 不存在\" 做全量反查, **范围内没有找到漏掉的原子**, 但 195 条 \"KB 写正确值\" 登记里有 73 条 (空格 / 标点类笔误) 抽不出可用 token, 测不了. 主控用更宽的筛法 (改正值在 KB 的所有出现行都算) 重筛: 范围内另有 169 条候选、范围外 142 条候选, **都没有审** (宽筛法噪声大; 是否审交主人定).",
      "- **范围外的已登记笔误同类原子 (delta 复审 H4)**: 第二轮 TYPO 层只取了范围内. delta 复审者在文本层 (未看渲染页) 确认范围外有 6 条同类: `ig34_p0083_a020` (S-SPREL SE T-1, 现 EXACT)、`ig34_p0304_a026` ~ `a029` (B-OE T-2, 现 EQUIVALENT)、`ig34_p0316_a023` (S-FND PE T-1, 现 EQUIVALENT). 上一轮 U-8 把范围外同类的 4 条改成了 PDF_TYPO. 这 6 条在第二轮时未经 tracer 审, 未进待改清单, 交主人定 (一页问题 7); 后续: 主人选 7b = A, 第三轮审查者对渲染页逐条确认, 已并入清单 (见下一节).",
      "- 范围外 (只列不审): 台账指针跨文档的旧标签另有 " + str(len(XOUT)) + " 条在 §5.0 范围外 (" + " / ".join(f"{k} {v}" for k, v in collections.Counter(XOUT.values()).most_common()) + f"), 其中 SDTM v2.0 第 74 页 {len(P74)} 条已被 Q9 审查者指认为配到了 SDTMIG 附录 F. 清单 `work/t4/round2/round2_population.json` 的 `xdoc_out_of_scope`.", "",
      "## 4b. 第三轮补检 (主人 2026-11-27 选定的追加审查: 4a = B / 4b = B / 4c = B / 7b = A)", "",
      "口径 `subagent_prompts/t4/t4_supp_round3_v1.0.md`; 样本 `work/t4/round3/round3_sample.jsonl` (md5 `" + md5(f"{W}/t4/round3/round3_sample.jsonl") + "`; seed 20261133); 原始结果 `evidence/t4_round3_raw/` (tracer ×13).", "",
      "| 层 | 取法 | 本次审 | 结果 |", "|---|---|--:|---|"]
r3pop = json.load(open(f"{W}/t4/round3/round3_population.json"))
e3, p3, h3, x3 = vc(r3, "R3_IG34_EQUIV"), vc(r3, "R3_PDF_TYPO"), vc(r3, "R3_HEADING"), vc(r3, "R3_XTYPO")
n_eq = n65 + sum(e3.values())
o += [f"| R3_IG34_EQUIV | SDTMIG 旧 EQUIVALENT (范围内, 非标题) 未审的 {r3pop['ig34_equiv_unjudged']} 条里按原子类型比例抽 150 | {sum(e3.values())} (抽样) | HOLDS {e3['HOLDS']} / TYPO_AFFECTED {e3['TYPO_AFFECTED']} / NOT_HOLD {e3['NOT_HOLD']} / UNVERIFIABLE {e3['UNVERIFIABLE']} |",
      f"| R3_PDF_TYPO | 终态 PDF_TYPO 里此前没人审过的全部 {r3pop['pdf_typo_unjudged']} 条 | {sum(p3.values())} (全检) | HOLDS {p3['HOLDS']} / **NOT_HOLD {p3['NOT_HOLD']}** / **UNVERIFIABLE {p3['UNVERIFIABLE']}** |",
      f"| R3_HEADING | 范围内 stock 标题类 (EXACT / EQUIVALENT) 未审的 {r3pop['heading_unjudged']} 条里按比例抽 60 | {sum(h3.values())} (抽样) | HOLDS {h3['HOLDS']} / HOLDS_AS_EQUIV {h3['HOLDS_AS_EQUIV']} / NOT_HOLD_SELF {h3['NOT_HOLD_SELF']} / NOT_HOLD {h3['NOT_HOLD']} / UNVERIFIABLE {h3['UNVERIFIABLE']} |",
      f"| R3_XTYPO | delta 复审者在文本层指出的范围外 6 条 | {sum(x3.values())} (全检, 看渲染页) | TYPO_AFFECTED {x3['TYPO_AFFECTED']} / NOT_AFFECTED {x3['NOT_AFFECTED']} / NOT_HOLD {x3['NOT_HOLD']} / UNVERIFIABLE {x3['UNVERIFIABLE']} |", "",
      f"- **SDTMIG 旧 EQUIVALENT**: 两次随机抽样合计 {n_eq} 条 (65 + 150) 0 错 → 错误率 95% 置信上界约 {ub(n_eq):.1f}% (近似: 分层抽样按简单随机算). 另有 16 条跨文档指针的全检 0 错. 仍**不是全检**: 范围内这类标签共 2207 条.",
      f"- **PDF_TYPO**: 至此 (R2L 之前) 终态 PDF_TYPO 149 条全部经独立审查者看过 (总闸样本 5 + 第二轮 45 + 第三轮 99); R2L 新进入 PDF_TYPO 的 25 条本身就来自第二轮 / 第三轮审查者逐条判的 TYPO_AFFECTED, R2L 后共 174 条, R3L 后 170 条. 结果: {p3['NOT_HOLD']} 条**多标** — " + "; ".join(f"`{a}`" for a, r in r3.items() if r["layer"] == "R3_PDF_TYPO" and r["verdict"] == "NOT_HOLD") + " — 登记的笔误 (`S-TDM TD T-1` / `T-4`) 其实在相邻原子 / 另一张表头里, 这 4 条自己的 PDF 原文没有笔误, KB 与 PDF 逐字一致, 标签应为 EXACT. (`t3_recompute.md` 早就记过 \"S-TDM TD T-1 有 2 条可能多标\".) 这是标签方向与问题 3 相反的新发现 (改回 EXACT 对 U-1 B 口径无影响, strict 口径 +4 条); 当时待主人定, 主人后来选 A1 (消息 4), 已由 R3L 批改回 EXACT.",
      "- **判不了的 1 条**: " + "; ".join(f"`{a}`" for a, r in r3.items() if r["verdict"] == "UNVERIFIABLE") + " (登记 `B-MK T-2`: PDF 写 \"REPLACEMENT/ SURGICAL\" 多一个空格). 该处正好是表格单元格折行 (`pdftotext -bbox`: \"REPLACEMENT/\" 与 \"SURGICAL\" 在上下两行), 文本层与渲染页都无法判定有没有空格; 登记自己也注了 \"折行歧义而非确证印刷错\". KB 写 \"REPLACEMENT/SURGICAL\", 两种情况下内容都没错; 悬而未决的只是标签 (PDF_TYPO 还是 EXACT). 按 brief 该层因此**不算全通过**.",
      f"- **标题类**: 60 条内容全部成立, 无 KB 自拟标题、无缺节. {h3['HOLDS_AS_EQUIV']} 条 HOLDS_AS_EQUIV = PDF 标题 \"X – Examples\" 用 en dash, KB 文件首行 `# X — Examples` 用 em dash (标 EXACT 的应为 EQUIVALENT; 标签级别后续项). 连同第二轮 11 条, 标题类共审 71 / 316.",
      "- **范围外笔误同类 6 条**: 全部对渲染页确认 (`S-SPREL SE T-1` 1 条 / `B-OE T-2` 4 条 / `S-FND PE T-1` 1 条) → 按主人 7b = A 并入改台账.",
      "- 第三轮审查者顺带记的事项: p220 \"at runtime to for measuring\" 疑似 PDF 多一个词, 未登记, KB 照录 (`CP/examples.md:305`; `pack_2.md`); `TS/assumptions.md` NullFlavor 表与 `TA/assumptions.md:94` 有 KB 自拟的表头 / 标题 (`pack_6.md` / `pack_12.md`); 登记文字不准或前后矛盾: `B-CP T-3`、`S-SPC1 CP T-16a` (漏记一处未闭合引号)、`S-SPC2 N-1` / `N-2`、`B-NV N-1` / `N-2` 的 `basis` 写 \"照录\" 而 `handling` 是 \"KB 写正确值\" (`pack_8.md` / `pack_9.md`); 决策表登记指针应补: `ig34_p0355_a027` 与 p356 第 27 行原子补 `B-TR T-1`, 另有 3 条漏列第二个登记 id (`pack_8.md`); `MH/assumptions.md:27` 闭引号方向 (U-9(b) 已定照录; `pack_7.md`). `pack_4.md` 说 `CP/spec.md` 缺规格表脚注 — 主控核实为误报 (脚注在 `CP/spec.md:564`, 原子 `ig34_p0204_a013` 标 EXACT 成立).", "",
      "## 5. 后果 (按派发前写死的条款)", "",
      "- PRE_EXISTING 层 NOT_HOLD ≥ 1 → Q9 升级已触发并执行到 §3 / §4; **主控不自行结案**. 需要主人定的事列在 `t4_owner_decisions_round2.md`.",
      f"- 待改标签共 {len(pend)} 条, 逐条清单与各选法下的闸数字 (在台账副本上算) 见 `t4_relabel_pending.md`. 这些都是闸口径层面的事, 须主人本人定 (总闸 attempt 2 C 项; 协调方指示); PDF_TYPO 每条须用户 ack (G-TB1). **主人 2026-11-27 在主控聊天里直接定了全部 {len(APPLIED)} 条** (原话 `t4_owner_confirmation.md` 第二轮一节): 先定 {N_R2L} 条 (消息 2), 由 R2L 批落到台账 (`{LEDGER_MD5[:8]}…` → `{R2L_MD5[:8]}…`); 那 {N_R3L} 条多标的 PDF_TYPO 第一次问时未答 (消息 3), 总闸 attempt 3 把它判为唯一挡闸项后再问, 主人答 A1 (消息 4), 由 R3L 批改回 EXACT (`{R2L_MD5[:8]}…` → `{LIVE_MD5[:8]}…`). 两批清单外标签变化都是 0. 判不了的 1 条 (`ig34_p0293_a038`) 主人答 B1: 维持 PDF_TYPO, 写明 \"折行处无法判定有没有空格\".",
      "- 补检其余 9 个非空层 (145 条) 通过: FIG 11、triage ATOM_ERR 74、RELOCATE 3、六条规则类 57.", "",
      "## 6. 审查者顺带记录的事项 (都不改 KB; KB 冻结)", "",
      "需要定口径的 (已并入给主人的一页):",
      "- 标题后缀: Q9 包 1 的 Q19-Q26 (8 条 v2.0 目录条目) KB 标题带 `(TE)` 等域代码后缀, 审查者按 \"附加信息不改原意\" 判 HOLDS 并提醒 \"若任何附加都算标题文字不同, 这 8 条要改判\" (`evidence/t4_q9_raw/pack_1.md`). 主控依据: U-10① 已定 \"(XX) 后缀为保留的检索导航, 只补登记\" (`t4_user_decisions.md` §000), 维持 HOLDS.",
      "- 域标题不带节号 / DI 自拟标题: 见 §4 XDOC.",
      "- `sv20` §6.4 RELSUB / §6.5 DR 的 KB 表也只有 5 列, PDF 对应表有 C-code 与 Definition 格 (`evidence/t4_supp_raw/pack_2.md` 样本外发现; 审查者写 \"需要 owner 定口径\"). 与 R1 同类; 这两节不在 §5.0 范围内.",
      "- KB 排版: `knowledge_base/domains/EG/examples.md:62-87` (Ex3 表) 省略列写 `...`, PDF p190-191 是 `…` (U+2026). 这 26 行在 S-TYPO 残余清单里归类 `table_elision` (`work/t2_batches/S-TYPO.residual.jsonl`; 全表 1091 行 = kb_nav 685 / body 235 / heading 144 / table_elision 26 / kb_note 1). 这 26 行 = EG 例 3 表 25 行 (`:62`, `:64-87`; `:63` 是表格分隔线) + `knowledge_base/domains/RE/examples.md:15` 1 行 (同样是表头用 `...` 表示省略列). U-9(c) 当时说的是 \"残余 230 行\", 与文件行数对不上, **不能确认 U-9(c) 的 \"接受现状\" 覆盖这 26 行**. 受影响的 19 条 p191 原子现标签仍是 EXACT (审查者判 HOLDS_AS_EQUIV, 即按定义应为 EQUIVALENT; 归标签级别后续项, 未改).",
      "",
      "PDF 自身不一致 (前两条未登记):",
      "- sv20 p69 SREL 行 Notes 写 \"subject or pool identified in RDEVID\", p50 同句写 \"device\" (`evidence/t4_q9_raw/pack_5.md`).",
      "- ig34 p440 图中 SPC-003 标 \"(Brain)\", 同页表写 TISSUE (`evidence/t4_supp_raw/pack_6.md`).",
      "- ig34 p277 叙述 / p278 Method B 表: 叙述说第 14-26 行 RELID 为 2 / `DY8DRGX`, 表里这些行印 RELID 1, 第 26 行 IDVARVAL 印 `DY1DRGX` (`evidence/t4_round2_raw/pack_sib_3.md`). 这一处**已登记**: `t4_user_decisions.md` A1-20 / `B-PCPP T-4` (照录 + T4), 不是新发现.",
      "- 登记页号: `B-CP T-5` 的 `pdf_page` 写 211, 该行实际在 p212 (`pack_sib2_1.md`); `B-IS T-6` 写 241 实为 239 (解冻轮 W1 已发现). 都留到改台账那一批更正.",
      "",
      "台账 / 登记的指针类 (不影响标签):",
      "- 若干 `md_atom_ids` 指向别的域 / 文件 (如 `ig34_p0153_a0009` → DM; `ig34_p0255_a036` → MS examples; XDOC 层 27 条); 原子页号偏一页 (`ig34_p0169_a0025` 等实在 p170; `ig34_p0057_a001` 实在 p56; `ig34_p0442_a001` 实在 p441).",
      "- `ig34_p0355_a027` (PDF_TYPO): 决策表登记指针只列 `B-TR T-3`, 漏 `B-TR T-1` (`evidence/t4_round2_raw/pack_typo_2.md`). `chapters/ch08_relationships.md:228` 也承载了 `B-SUPPQUAL T-1` 的改正值, 登记的位置清单没列这一行 (`pack_sib_3.md`).",
      "- 登记 `S-CH4 T-10e` (p43 两句之间缺空格) 落在 `ig34_p0043_a022` 与 `a023` 的交界; 仅空白差异; 审查者判 `a022` NOT_AFFECTED 并提示 \"若从严, 受影响的可能是下一个原子\"; `a023` 未经审查者看, 主控按 \"EXACT 允许空白归一\" 认为两条都成立 (`pack_sib_1.md` R29; 同页 `S-CH4 T-10d` 的相邻原子同理).",
      "- 样本包里的 KB 指针多处近似, 审查者都自行重新定位.",
      "",
      "标签级别 (内容成立; 记后续, 同 U-10⑤):",
      "- 旧 EXACT / EQUIVALENT 实为 \"原子抽错 + KB 与 PDF 一致\" (按定义更接近 ATOM_ERR): 补检 PRE_EXISTING 层 #3、#4、#11-#16、#19-#26、#46-#48、#51、#53 (见 `evidence/t4_supp_raw/pack_1.md` / `pack_2.md` 各行说明); Q9 的 `ig34_p0057_a006`、`ig34_p0068_a004` 及包 6 的 Q132-Q135、Q146; 第二轮 `pack_sib_2.md` 附注的 8 条 (R55 / R56 / R59 / R60 / R63 / R64 / R66 / R75)、`pack_sib_1.md` 的 R34 / R43 / R50、`pack_sib2_1.md` 的 S8 / S10 / S15 / S17 / S19 (审查者: \"S8 更贴切的标签是 ATOM_ERR, 请定\")、`pack_sib2_2.md` 的 S21 / S22 / S23 / S27 (审查者: \"是否进入标签级别后续项由你决定\")、`pack_sib_3.md` 提到的 `ig34_p0147_a024` / `a025`; delta 复审者另指出 `ig34_p0280_a045` (未审; 原子写 `DYIDRGX_A`, PDF 与 KB 都是 `DY1DRGX_A`). 主控处理: 一律记标签级别后续项, 不在本轮改 (与 U-10⑤ 同).",
      "- 范围内 sv20 标题类旧 EQUIVALENT 共 5 条: 3 条在 XDOC 层审过 (成立); `sv20_p0052_a010`、`sv20_p0054_a001` 两条没有审 (台账指针不跨文档, 不在任何一层的取法里).",
      "- 原子抽取本身的问题 (只影响台账, KB 对): p69 原子 a023-a032 把两张 se.xpt 的值混在一起、p77 原子 a015-a018 把 dm.xpt 抽成 suppdm (`evidence/t4_supp_raw/pack_3.md`); `sv20_p0053_a018` 把 Notes 文字放进 Definition 格 (`evidence/t4_q9_raw/pack_3.md`).",
      "- KB 附加信息: `CE/spec.md:261,279`、`HO/spec.md:81` 的受控术语格比 PDF 多写了 NCI C-code (`evidence/t4_supp_raw/pack_4.md`; S-CT 批 U5/U6 的做法, 各 spec.md 有统一 KB note, 这三格是否在其覆盖内待核).", ""]
old = open(f"{CK}/t4_supp_fullcheck.md", encoding="utf-8").read() if os.path.exists(f"{CK}/t4_supp_fullcheck.md") else ""
tail = old.split(MARK, 1)[1] if MARK in old else "\n\n## 独立审查 B 的处理\n\n(待写)\n"
open(f"{CK}/t4_supp_fullcheck.md", "w", encoding="utf-8").write("\n".join(o) + "\n" + MARK + tail)

# ---- pending relabel md
g = collections.Counter((p["group"], p["now"], p["to"]) for p in pend)
gn = collections.Counter(p["group"] for p in pend)
o = ["# 待改标签清单 (补检 + Q9 扩检 + 第二轮 / 第三轮补检查出; **82 条全部已执行**)", "", "<!-- chain: E (plans) -->",
     f"> 状态: **{len(APPLIED)} 条全部已执行** (2026-11-27): {N_R2L} 条 = R2L 批 (主人直接定的 1A / 2A / 3A / 7b-A), {N_R3L} 条 (`typo-overlabel` 组) = R3L 批 (主人直接定的 A1). 共 {len(pend)} 条. 台账 `work/coverage_ledger.wc.jsonl` md5 `{LEDGER_MD5}` → (R2L) `{R2L_MD5}` → (R3L) `{LIVE_MD5}` (本脚本逐条核过: {len(APPLIED)} 条现标签都 = \"建议\" 列, 全台账相对最初备份标签有变化的行数 = {changed_live}; 现台账实算的四个数与下表最后一行逐字相同). \"现标签\" 列一律指**改前**. 本文件由 `scripts/t4/t4_supp_report.py` 生成; 依据是独立审查者的原始结果 (\"原始结果\" 列), 主控未改判.",
     "> 当初为什么不直接改 (历史说明): 这些是闸口径层面的事, 须主人本人定 (总闸 attempt 2 C 项; 协调方 2026-11-27 指示, `t4_coordinator_note_20261127.md`); PDF_TYPO 每条须用户 ack (G-TB1); 主人已确认的 U-1 口径数字建立在当前台账上. (Q9 brief 原写 \"NOT_HOLD_R1 → 改 IE\", 这里收紧为先问主人.)", "",
     "## 1. 三组 (提问与选项以 `t4_owner_decisions_round2.md` 为准, 这里只列组)", "",
     "| 组 | 条数 | 现标签 → 建议 | 对应给主人一页的 |", "|---|--:|---|---|"]
QN = {"R1-row": "问题 1 (主人选 A)", "v2.0-TOC": "问题 2 (主人选 A)", "registered-typo": "问题 3 (主人选 A)",
      "registered-typo-oos": "问题 7b (主人选 A; 第三轮审查者已对渲染页确认)", "typo-overlabel": "第三轮新发现; 问题 A — 第一次问未答 (消息 3 「继续」), 总闸 attempt 3 后再问, 主人选 A1 (消息 4) → R3L 批"}
for (grp_, now, to_), n in sorted(g.items()):
    o.append(f"| {grp_} | {n} | {now} → {to_} | {QN[grp_]} |")
o += ["", "## 2. 各选法下的闸数字 (在**改前备份台账** `work/coverage_ledger.wc.pre_r2l.jsonl` 的副本上实算; \"现状\" = 改前; 实际执行的是最后一行: R2L 批先到倒数第二行, R3L 批再到最后一行)", "",
      "| 选法 | 改几条 | G-TB3 U-1 B 口径 (过闸用; 闸线 99.0192%) | strict (并列报) | mapped | 内容指标 (EXACT+EQUIV) | G-TB1 范围内节 / 残留 | G-TB2 字面口径 |", "|---|--:|---|---|---|---|---|---|"]
for k, v in SCEN.items():
    o.append(f"| {k.replace('(待主人定)', '(当时待主人定; 主人后来选 A1, 已执行 = 现状)')} | {v['n']} | {v['u1b']} | {v['strict']} | {v['mapped']} | {v['content']} | {v['g1']} / {v['residual']} | {v['g2_literal']} |")
o += ["", "- G-TB2 的过闸口径是 \"范围内\" (U-3 A): 174/174; 表里最后一列是 `t3_recompute.py` 打印的字面口径值 (17 个结构父节仅因范围外子节不满), 两者在各选法下都不变.",
      "- U-1 B 口径在所有选法下都高于闸线; strict 在所有选法下都低于 (与 attempt 2 相同的性质).",
      "- 改成 \"有意不收\" 的原子同时离开分子和分母; 改成 PDF_TYPO 的在 U-1 B 口径下仍算覆盖, 在 strict / mapped / 内容指标里不算.",
      "- 范围外的三行不在 G-TB1 / G-TB2 的范围内, 但 G-TB3 按整本台账算, 所以会动 G-TB3 的分子分母. \"146 条全改\" 是**假设配错的都认 IE** 的情形 (那 146 条里只有 p74 的 14 条被审查者看过; 其中 113 条现标 PARTIAL): 若有的内容自己文档的 KB 里也没有、又不认 IE, 应记未覆盖, 数字会比这一行更低; 若内容其实在 `model/` 里只是指针错, 标签不变. 所以这一行不是严格的下限.",
      "- \"范围外已登记笔误同类 6 条\" 先由 delta 复审者在文本层确认, 后经第三轮 tracer 对渲染页逐条确认, 在下面 §3 的清单里 (组 `registered-typo-oos`).",
      "- 改标只动标签, 不动 KB. 已执行: writer (`oh-my-claudecode:executor`) → reviewer (`oh-my-claudecode:code-reviewer`, PASS + delta PASS) → auditor (`oh-my-claudecode:verifier`, 33 / 33) (R2L 批; R3L 批 4 条 = writer → reviewer PASS, 语义依据是第三轮审查者与总闸 attempt 3 审查者两次独立复核, 未另设 auditor), 并在 R2L 那次回写里处理了 registry `B-IS T-6` 页号 p241 → p239 (页号参与登记匹配 `t3_errata_build.py:150` / `t3_writeback.py:404`, 单独改有改变台账的风险) 与 `t4_supp_fullcheck.md` §6 所列的登记指针补全.", "",
      "## 3. 逐条", "", "| # | atom_id | 页 | 节 | 现标签 (改前) | 建议 | 组 | 执行 | 理由 | 原始结果 |", "|--:|---|--:|---|---|---|---|---|---|---|"]
for n_, p in enumerate(pend, 1):
    a = A[p["atom_id"]]
    o.append(f"| {n_} | `{p['atom_id']}` | {a['page']} | {a['parent_section'][:44].replace('|', '¦')} | {p['now']} | {p['to']} | {p['group']} | {('已执行 (R3L)' if p['group'] == 'typo-overlabel' else '已执行 (R2L)') if p['atom_id'] in APPLIED else '**未动**'} | {p['why']} | `{p['raw']}` |")
o += ["", "## 4. 复跑", "", "```bash", "python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_report.py",
      "# 各选法的台账副本: work/scratch/t4/relabel_preview/ledger_<name>.jsonl (gitignored); 数字另存 work/t4/supp/scenarios.json", "```", ""]
open(f"{CK}/t4_relabel_pending.md", "w", encoding="utf-8").write("\n".join(o) + "\n")
print("supp", dict(vc(supp)), "| q9", dict(vc(q9)), "| round2", {k: dict(vc(r2, k)) for k in ("XDOC", "TYPO_SIB", "TYPO_SIB2", "PDF_TYPO")}, "| round2 missing", len(r2_missing))
print("round3", {k: dict(vc(r3, k)) for k in ("R3_IG34_EQUIV", "R3_PDF_TYPO", "R3_HEADING", "R3_XTYPO")}, "missing", len(r3_missing))
print("pending relabels", len(pend), dict(gn))
for k, v in SCEN.items():
    print(f"  {k}: n={v['n']} U-1B {v['u1b']} | strict {v['strict']} | content {v['content']}")
print("bounds: 65 ->", round(ub(65), 2), "73 ->", round(ub(73), 2), "45 ->", round(ub(45), 2), "215 ->", round(ub(215), 2))
