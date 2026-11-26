# T2 B-PCPP — Auditor (Rule A) attempt 1

> agent: oh-my-claudecode:verifier (opus); 2026-11-26; base HEAD 302ec4c, KB 未提交工作区. 未改 KB. scratch: `scratchpad/t2_BPCPP_auditor/`.
> 先独立判 (只读 PDF 页 + KB), 判完才对照 writer/reviewer.

## 抽样
- 命令: `subagent_prompts/t2_auditor_v1.0.md` §抽样 脚本原样, b=B-PCPP, **seed=20261126** → `scratchpad/t2_BPCPP_auditor/sample.json`
- 结果: C=0 (本批 atoms 全为 TABLE_*), P=56, N=10 (全部来自 P−C 对照原子)

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0275_a026 | p275:40 RELREC 链接变量决定表示方法 | PC/assumptions.md:40 | 否 | 是 | 是 (§PC-PP Relating Records) | 逐字 |
| 2 | ig34_p0275_a022 | p275:36-37 参考时点+analyte 属 natural key; --GRPID surrogate key | PC/assumptions.md:34 | 否 | 是 | 是 | 逐字, 含 Section 3.2.1.1 引用 |
| 3 | ig34_p0270_a004 | p270:6 Rows 1-2 day1 pre-dose plasma+urine | PC/examples.md:15 | 否 | 是 | 是 (PC Ex1) | 逐字 |
| 4 | ig34_p0277_a017 | p277:18 All PC records used to calc all PK params | PC/examples.md:64 | 否 | 是 | 是 (§6.3.5.9.3 Ex1) | 逐字 |
| 5 | ig34_p0277_a021 | p277:22 Rows 3-4 RELID 2, GRPID DY8_DRGX / DY8DRGX | PC/examples.md:71 | 否 | 是 | 是 (Ex1 Method A) | 逐字 |
| 6 | ig34_p0270_a007 | p270:10 Rows 7-12 day1 post-dose plasma | PC/examples.md:18 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0273_a036 | p273:39-40 PP Ex2 Rows 1-3 AUC T1-T2, LIN-LOG in PPANMETH | PP/examples.md:47 | 否 | 是 | 是 (PP Ex2) | 逐字 |
| 8 | ig34_p0274_a001 | p274:1 PP Ex2 Row 5 Ratio AUC Met2/Met1 | PP/examples.md:49 | 否 | 是 | 是 (PP Ex2) | 逐字 |
| 9 | ig34_p0277_a018 | p277:19 uses PCGRPID/PPGRPID (Example 1) cols | PC/examples.md:66 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0273_a006 | p273:8 PP Ex1 Rows 1-12 day 1 | PP/examples.md:11 | 否 | 是 | 是 (PP Ex1) | 逐字 |

**独有丢失 = 0; 忠实度错误 = 0.**

## 主控追加核查
1. **PC Ex1 pc.xpt (PC/examples.md:25-58, 32 行×31 列) 随机 10 格** (seed 20261126, 渲染 p270/p271 @300dpi 逐格比): row2 USUBJID 123-0001; row3 PCENDTC 2001-02-01T07:45; row10 PCELTM PT6H; row12 USUBJID; row16 PCREFID A554134-16; row17 PCTESTCD DRGA_MET; row22 PCCAT ANALYTE; row22 PCTPT 6H; row23 PCRFTDTC 2001-02-11T08:00; row30 PCTESTCD PH → **10/10 一致**. 附带: row9 PCELTM "PT6H00M" 与 PDF 原样一致.
2. **删除核查** (`scratchpad/t2_BPCPP_auditor/deleted.py`, difflib HEAD vs 工作区, 结果 `deleted.txt`): PP/examples.md 纯删除/替换块只有:
   - D-1 head:110-125 (pp.xpt 标签+12 行表) → 1 行指针. 被删 12 数据行与 PC/assumptions.md:88-99 逐字相同; 表头仅 PPRFDTC→PPRFTDTC (PDF p277 为 PPRFTDTC). 锚点 `#pc-pp--relating-records` 对应 PC/assumptions.md:36. 无信息丢失.
   - D-2 SUPPPP 块 (head:42-54) 未动, Ex2 叙述+表 (head:57-76) 移到其前 → SUPPPP 归 Ex2, 与 PDF p274 一致; 仅 row7 QORIG "Collected"→空 (PDF p274 row7 QORIG 空).
   - D-3 head:131 只删括注 "(the most common pattern …)"; D-4 head:178 只删次句 "This is what "Many to One" means here …"; D-5 head:187-193 只删 Cross-domain summary 节 (KB 自写, 页码/方法与 PDF 不符).
   - 其余改动均为表格值/列名替换 (PP Ex1 重建、Ex3 PPRFTDTC/L/hr、Method D 标题页码 278-279 — PDF p278:56 起, p279:35 进 Ex2, 正确). 无列表外删除.
3. **Reviewer 缺陷 3 (PP Row 4 "截断")**: 不成立. PP/examples.md:48 与 HEAD:62 相同且完整, 与 PDF p273:41-43 一致 (以 "...pre-coordinated PK parameter values." 结尾).
   旁注 (非本批引入, 不计): PDF p273:41 原文 "pre-corrdinating" 拼写错, KB (HEAD 起) 写作 "pre-coordinating".
4. 抽查 PC/examples.md:293 DYIDRGX_A→DY1DRGX_A: PDF p280:59 为 DY1DRGX_A, 正确.

## G-TB8
trace.jsonl 本批有 executor subagent_done ×3 (行 43/44/46) + code-reviewer ×1 (行 45); 本批无 `agent: main` 写 KB 记录 → OK.

## 判定
**PASS** — Rule A N=10 seed=20261126: 丢失 0 / 忠实 0; 追加 10 格 0 差; 5 处删除无越界.
