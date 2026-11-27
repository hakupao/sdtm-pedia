# T4.1 Q9 扩检 — 包 7 审查结果 (Q9_IG34_EQUIV, Q154-Q179, 26 条)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:01:43Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` 背景 / 判定口径 + `subagent_prompts/t4/t4_q9_extension_v1.0.md` 五选一 (后者优先)
- 看过的渲染页: `source/cdisc/SDTMIG v3.4 (no header footer).pdf` p71 (CRF 图, Q175)
- 用过的命令 (均在仓根执行):
  - `grep -rn "<PDF 原句关键片段>" knowledge_base` (逐条, 共 23 个片段, 找 KB 承载位置)
  - `awk -v n=<行号> 'NR<=n && /^#/{h=NR": "$0} END{print h}' <KB 文件>` (核 KB 行所属节 / Example 标题)
  - `grep -n "^ *Example [0-9]*$" .work/10_tier_b_repair/work/pdf_pages/ig34_p<页>.txt` (核 PDF 原子所属 Example 编号, 页 68/112-115/215-218/224/296-297/310-311/397-399/405-406)
  - `sed -n` 读 `pdf_pages/ig34_p0055/0057/0071/0224/0248/0283/0284.txt` 与对应 KB 段落
  - `grep -n ig34_p0071_a0 .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl` (核 p71 原子编排, 确认 a016 = BLACK OR AFRICAN AMERICAN 子选项块第 1 项)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| Q154 | ig34_p0029_a010 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0029.txt:12-13`; `knowledge_base/chapters/ch04_general_assumptions.md:296` (§4.2.3) | 实为逐字. 信息点: "no 2 or more subjects" / "across all trials in the submission" / "same USUBJID" 全在, 节对 |
| Q155 | ig34_p0048_a024 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0048.txt:28-30`; `ch04_general_assumptions.md:1177` (§4.4.10) | 实为逐字. "However, because" 让步语气、"only ... ISO 8601 periods of time"、交叉引用 §4.4.3 全名、"may not be populated for all time points" 全在 |
| Q156 | ig34_p0057_a006 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0056.txt:60` + `ig34_p0057.txt:1` (句子跨页); `ch04_general_assumptions.md:1489` (§4.5.4, 标题在 1481) | 实为逐字: KB "See Section 8.4, Relating Non-standard Variable Values to a Parent Domain." = PDF. 包内指针 568 行是 §4.2.8 另一处同引用, 非本处. 注: 原子 verbatim 抽错 ("to a Datasets" ≠ PDF "to a Parent Domain"), KB 按 PDF 写对; 标签级别上更贴近 ATOM_ERR, 但内容成立 |
| Q157 | ig34_p0061_a009 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0061.txt:14`; `knowledge_base/domains/CO/assumptions.md:26` (CO – Assumptions, 1c) | 实为逐字. 引用 §8.5 全名一致 |
| Q158 | ig34_p0065_a026 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0065.txt:39-40`; `knowledge_base/domains/DM/assumptions.md:25` (DM – Assumptions, 4b) | 实为逐字. "Example 3 below" + "Section 5.3, Subject Elements, Example 2" 全在 |
| Q159 | ig34_p0068_a014 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0068.txt:26-28` (Example 2); `knowledge_base/domains/DM/examples.md:18` (## Example 2) | 实为逐字. "2 elements, screen and run-in" / "before ... randomized" 全在, Example 编号对 |
| Q160 | ig34_p0101_a010 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0101.txt:10`; `knowledge_base/domains/CM/assumptions.md:27` (CM – Assumptions, a) | 实为逐字. 限定 "(or at least a partial date)" 保留 |
| Q161 | ig34_p0115_a028 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0115.txt:29-32` (Example 6); `knowledge_base/domains/EX/examples.md:239` (## Example 6) | 实为逐字, Example 编号对 |
| Q162 | ig34_p0121_a003 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0121.txt:2-3`; `knowledge_base/domains/ML/assumptions.md:5` (## ML – Description/Overview) | 实为逐字, 节对 (术语表 `terminology/core/general_part4.md:204` 另有同文, 不作为承载位置) |
| Q163 | ig34_p0248_a011 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0248.txt:15` (LB – Examples 第 5 个); `knowledge_base/domains/LB/examples.md:88` (`## Example 5`, 前接 Example 1-4 于 3/43/58/72 行) | 标题原子, KB 为 Markdown 标题, 编号与 PDF 顺序一致; 后续正文 (LBBDAGNT 单 agent) 与 PDF 第 16 行起一致 |
| Q164 | ig34_p0279_a036 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0279.txt:40-41` (Example 2, 前句为 PCGRPID="EXCLUDE"); `knowledge_base/domains/PC/examples.md:198` (### Example 2, 192 行) | 实为逐字. 包内 KB 指针为 "无", 自查找到. 注意 KB 280 行 (Example 3) 有同句, 对应 PDF 另一原子; 本原子按上下文 (EXCLUDE) 归 Example 2, 位置对 |
| Q165 | ig34_p0282_a026 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0282.txt:27-29` (Example 4); `knowledge_base/domains/PC/examples.md:392` (### Example 4, 390 行) | 实为逐字. 信息点: time point 5→Tmax / 6→Cmax / 11 和 12→AUC 全对. 包内指针 "无", 自查找到 |
| Q166 | ig34_p0297_a034 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0297.txt:34-39` (Example 2); `knowledge_base/domains/NV/examples.md:61` (## Example 2) | 实为逐字. "normative values" / "by the laboratory" / "healthy controls" 全在 |
| Q167 | ig34_p0311_a024 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0311.txt:22-26` (Example 2); `knowledge_base/domains/RE/examples.md:42` (## Example 2) | 实为逐字. "1 of the attempts" / "with the reasons" 全在 |
| Q168 | ig34_p0399_a033 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0399.txt:29,46-47` (Example 7); `knowledge_base/domains/TA/examples.md:869` (## Example 7, 865 行) | 实为逐字 (弯引号 “schema” 两边一致). "5 options" 值对 |
| Q169 | ig34_p0406_a014 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0406.txt:8,18-19` (Distinguishing Elements, Study Cells, and Epochs); `knowledge_base/domains/TE/examples.md:71` (### Distinguishing Elements, Study Cells, and Epochs, 65 行) | 实为逐字, 节对 |
| Q170 | ig34_p0042_a024 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0042.txt:44-45`; `ch04_general_assumptions.md:912` (§4.4.5, 896 行) | 实为逐字 (项目符号 • → -). 两句均在, 列表位置 (unplanned visits 三项的第 3 项) 一致 |
| Q171 | ig34_p0052_a023 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0052.txt:26-27`; `ch04_general_assumptions.md:1295-1297` (§4.5.1.2, 1268 行) | 实为逐字. 引导句 "if urinalysis tests were not done" 与后两项 LBTEST / LBCAT 也在, 上下文完整 |
| Q172 | ig34_p0055_a013 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0055.txt:20-21`; `ch04_general_assumptions.md:1410` (§4.5.3.2, 1401 行) | 实为逐字. "(>200 characters)" / "1-digit integer, beginning with 1" 全在 |
| Q173 | ig34_p0055_a017 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0055.txt:30-33`; `ch04_general_assumptions.md:1414` (§4.5.3.2) | 实为逐字. 层级一致: PDF 为 QLABEL 项下 "o" 子项第 3 个, KB 为 1411 行父项下缩进子项第 3 个. AEACNOTH / AEACNOT1 / AEACNOT2 值对 |
| Q174 | ig34_p0065_a021 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0065.txt:33-34`; `knowledge_base/domains/DM/assumptions.md:25` | 实为逐字. 项号 "b." 与引用 "Section 7.2.1, Trial Arms, Example Trial 3" 全在 |
| Q175 | ig34_p0071_a016 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p71 (Example 4 CRF 图续页, "BLACK OR AFRICAN AMERICAN" 块 CRACE11-CRACE17 的第 1 个勾选项 "AFRICAN"); `knowledge_base/domains/DM/examples.md:136` (## Example 4 Mermaid, SC3) | 原子是 CRF 图内勾选项. KB Mermaid SC3 "Subcategories CRACE11-17 → SUPPDM.QVAL ☐ AFRICAN ..." 承载, 所属块 (R3 BLACK OR AFRICAN AMERICAN → SC3) 与变量区间 CRACE11-17 与 PDF 一致, 7 项顺序一致. 包内列的 11 行 (DM 数据表 RACE 值) 和 120 行 (父选项) 不是本原子承载处 |
| Q176 | ig34_p0218_a018 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0218.txt:11,29-30` (Example 8); `knowledge_base/domains/CP/examples.md:273` (## Example 8, 261 行) | 实为逐字 (行标签加粗). 注意 KB 77 行另有 "Rows 7-8" (别的 Example), 本原子对应 273 行, 位置对 |
| Q177 | ig34_p0224_a018 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0224.txt:21,29` (Example 1); `knowledge_base/domains/GF/examples.md:15` (## Example 1) | 实为逐字 (行标签加粗), Row 1-6 顺序一致 |
| Q178 | ig34_p0283_a009 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0283.txt:8,13-14` (Example 4, Method D); `knowledge_base/domains/PC/examples.md:440` (### Example 4 → #### Method D, 436 行) | 实为逐字. 值逐个核: Rows 24-35 / RELID "3" / PCSEQ "1" through "10" / PPSEQ = "3" 全对 (PDF 本身 "Rows 13-24" 与 "Rows 24-35" 行号重叠, KB 照搬, 不属 KB 错). 包内指针 "无", 自查找到 |
| Q179 | ig34_p0284_a014 | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0284.txt:27-29,40-45` (PC-PP – Suggestions for Implementing RELREC..., 第 3 问); `knowledge_base/domains/PC/assumptions.md:121` (### PC-PP – Suggestions for Implementing RELREC in the Submission of PK Data, 113 行) | 实为逐字. 项号 3、"Examples 1 and 2" / "Example 3" / "method A" / "methods B, C, and D" 全在, 1-4 项顺序一致. 包内指针 "无", 自查找到 |

## 计数

| 判定 | 数 |
|---|---|
| HOLDS | 26 |
| NOT_HOLD_R1 | 0 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |
| (其中 TOC 条目) | 0 |

按层: Q9_IG34_EQUIV 26 条 = HOLDS 26. 26 条中 25 条 KB 实为逐字 (仅 Markdown 格式差), Q175 为图内选项由 Mermaid 承载.

标签级别备注 (不影响判定): Q156 原子 verbatim 抽错 ("a Datasets" vs PDF "a Parent Domain"), KB = PDF.

## 样本外发现的 KB 内容问题

无.
