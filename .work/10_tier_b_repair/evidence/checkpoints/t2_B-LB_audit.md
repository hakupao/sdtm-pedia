# T2 B-LB auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- KB 状态: LB/assumptions.md md5 `10a137d1cbad1e7abd1166259dc10b13`, LB/examples.md `496bb1298f9e69d0e7268a09f9340ace` (= writer 续 X-4 之后); diff 基线 97e1895.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-LB_auditor/` (sample.json, cells.txt, 渲染 p194-196/p246-248, Ex1 300dpi 6 段 / Ex2 Ex3 300dpi 各 3 段, 通用表 160dpi)
- 抽样命令: t2_auditor_v1.0.md 抽样脚本原样 (b=B-LB, seed=20261126), 输出写 scratch/sample.json.
- 结果: **C=7, P=45, N=10** (C 抽 5 + P−C 对照 5). 先独立判, 判完才读 writer/reviewer 报告.

### Rule A 样本

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0195_a003 | 195:5-6 bullet 3 "variables in the generic domain specification table include required, expected, and permissible…" | LB/assumptions.md:13 | 否 | 是 | 是 (§6.3.5.1) | 逐字 |
| 2 | ig34_p0195_a006 | 195:10-11 子 bullet "Permissible identifier and timing variables may be added…" | LB/assumptions.md:16 | 否 | 是 | 是 | 逐字, 缩进层级同 PDF |
| 3 | ig34_p0194_a022 | 194 末 "This section describes variables commonly used in specimen-based laboratory domains (e.g., IS, LB, MB/MS, MI, PC/PP)." | LB/assumptions.md:9 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0195_a004 | 195:7 子 bullet "Individual domains include additional variables…Core values." | LB/assumptions.md:14 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0195_a001 | 195:1-3 bullet 1 "SDTMIG includes several domains…(e.g., microbiology susceptibility…)" | LB/assumptions.md:11 | 否 | 是 | 是 | 两句全, e.g. 三项全 |
| 6 | ig34_p0247_a003 | 247:4 Ex1 Row 18 LBSTNRC urine protein, not clinically significant | LB/examples.md:17 | 否 | 是 | 是 (Ex1) | 对照 (P−C) |
| 7 | ig34_p0196_a017 | 196 §6.3.5.2 "…in preparation for the retirement of the SDTMIG-PGx upon publication of SDTMIG v3.4." | RELSPEC/assumptions.md:3 | 否 | 是 | 范围外 | 对照; 在 kb_files 外. 句子在 RELSPEC 而非 BS 节 (既有布局, 非本批) → 范围外观察, 不计本批 |
| 8 | ig34_p0247_a001 | 247:1-2 Ex1 Row 16 cholesterol <200 mg/dL, LBSTNRHI="199" | LB/examples.md:16 | 否 | 是 | 是 | 对照 |
| 9 | ig34_p0194_a010 | 194 IE Ex1 "Rows 3-4: Show data for 2 other subjects…same inclusion criterion." | IE/examples.md:9 | 否 | 是 | 是 | 对照; kb_files 外, 存在 |
| 10 | ig34_p0247_a018 | 247 Ex3 Row 2 pregnancy test not performed, subject male; sponsor reason record | LB/examples.md:63 | 否 | 是 | 是 | 对照, 两句全 |

**独有丢失 0/10, 忠实度错 0/10.**

### 补充抽检 (样本外; 主控要求覆盖新增 prose N1-N15 及 C 中未抽到的)

独立方法: KB 行去 markdown 前缀后去空白, 与 PDF 页文本 (p194-196, p245-248) 去空白做子串比对 + 目视原页.
- assumptions.md:3,5,7,9,11-16 全命中 (含 N1-N3 §6.3.5/§6.3.5.1 标题与引言 3 句, C 中 p195_a002/a005); :18 表标题行与渲染一致; :52 脚注、:54 `## LB – Assumptions` 为 PDF 原文.
- N9 (assumptions.md:73 补 LBPOS, LBLOC, LBFAST): 对照 p246:7-8 一致. N10 (examples.md:13 "set to missing because"): p246:29-30 一致.
  N11/N12 (LBRFTDTC): p247 渲染一致. N13 (Ex4 r3 LBLOBXFL=Y): p248 一致. N14 ("single agent"), N15 ("total amount of HGFR"): p248:16/20 一致.
- examples.md 5-17, 47, 48, 60, 63, 90, 92 全命中; :62 未命中仅因 PDF 弯引号 “-”, 该行非本批改动, 内容一致.

### 表格复核 (渲染图, 独立于 writer/reviewer)

- 通用规格表 p195-196 随机 10 格 (seed 20261126, scratch/cells.txt): --STRESU/CT `*`, DOMAIN/Role Identifier, --LOBXFL 变量名, --DTC/Type Char, --ORRES/Notes, --TEST/Notes, --METHOD/Type Char, --SEQ/CT 空, --ORRESU/Label, --REASND/Core Perm → **10/10 一致**. 另目视全表 29 行 × 7 列, 无差异.
- Ex1 (p247) 随机 10 格: R5 LBCLSIG 空, R13 LBSTAT 空, R12 LBSTNRC 空, R7 LBLOBXFL Y, R3 VISIT Week 1, R8 LBTEST Prostate Specific Antigen, R12 LBPTFL Y, R13 LBORNRHI 8, R17 LBSTNRC 空, R9 USUBJID ABC-001-001 → **10/10 一致**. 因空格占比高, 另对 300dpi 6 段渲染逐行全格目视 18 行 × 41 列 (表头列序同 PDF), 无差异.
- Ex2 / Ex3 (p247) 全格目视一致; Ex3 "Ord"/"PrThr" 为 PDF 原样; PDF 表头 "LBSTRNHI" → KB LBSTNRHI (T-1 已登记, 依据同表 LBSTNRLO 与 Ex1/Ex2).

### 删除项 X-1..X-4 复核

- X-1 Ex1 斜体概述: KB 自写, 列名含 LBTOX/LBTOXGR/LBNAM/LBBLFL/LBENDTC、测试含 Monocytes, p247 表均无 → 无 PDF 承载信息丢失; 被整表替代.
- X-2 "binding": p248:16 原文 "for a single agent." → 删除正确.
- X-3 旧 Ex2 (CREAT/2000-02-01) / 旧 Ex3 (含 LBMETHOD 列): p247 渲染无对应 → 无丢失.
- X-4 孤儿脚注 (原 assumptions.md:3): 承载 ig34_p0245_a007 (LB 规格脚注, NOTE). 删后同文仍在 :52, 紧接 `## LB – Assumptions` 之前, 与 PDF 顺序 (LB 规格脚注 → LB – Assumptions) 吻合 → 文本无丢失. 观察 (低风险, 非 FAIL): 该脚注现同时充当 §6.3.5.1 通用表脚注; LB/spec.md 无脚注是全库惯例.

### 汇总

- 独有丢失: 0; 忠实度错误: 0 → **PASS**.
- 范围外观察 1: p196_a017 (§6.3.5.2 BS 引言) 落在 RELSPEC/assumptions.md:3, 不在 BS 节; 另该段末 "publication, after v3.4" 在 KB 为 "SDTMIG." (属 p196_a018, 未抽, 仅记).
- G-TB8: trace.jsonl 有 T2.B-LB writer (`oh-my-claudecode:executor`, 01:05:59Z) 与 reviewer (`oh-my-claudecode:code-reviewer`, 01:13:40Z, CONDITIONAL → 续 X-4 已执行) 的 subagent_done; 无 `agent: main` 写 KB 记录 → 通过. 注: reviewer 对 X-4 后状态无第二条 trace, 本次审计已在 X-4 后 md5 上复核.
