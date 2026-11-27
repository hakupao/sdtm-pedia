# T4.1 第二轮补检 — TYPO_SIB 层 包 4 (R53-R77, 25 条) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:38:04Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round2_v1.0.md` (TYPO_SIB 层)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, pdftoppm -r 200, 输出在临时目录): p211, p212, p213
- 看过的文本层: `work/pdf_pages/ig34_p0205/0206/0211/0212/0213/0224/0225/0236/0261/0262/0263.txt`
- 用过的命令: `python3` 按 id 查 `work/t2_pdf_typo_registry.jsonl`; `grep -n` 在文本层定位各登记笔误 (CPSCMRKS / inheritab / STUDY.RELATED / RSC1230 / MSCON / MBGPRID / MBTRESN / xpt); `sed -n` 读 PDF 文本层与 KB 文件 (`knowledge_base/domains/{CP,GF,IS,MB,MS}/...`); `pdftoppm -r 200 -f N -l N -png`.

## 关键定位 (每个候选登记的笔误实际在哪)

| 登记 id | 笔误实际位置 (PDF) | 本包涉及的原子 |
|---|---|---|
| `S-SPC1 CP T-16b` | p205 文本层 13-14 行, assumption 4 ("used in conjunction with CPSCMRKS" ×3) | R53 是 assumption 8 (p206:20), PDF 印 CPCSMRKS |
| `B-CP T-5` | p212 渲染页 Ex2 Row 6 CPDTC "2020-08-16T04:20" (文本层 p212:3) | R54-R58 (p211 Row 1-5)、R59-R62 (p212 Row 7-10), 渲染页均为 T12:20 |
| `B-CP T-6` | p213 渲染页 Ex3 Row 2 CPTEST "MonoSub" (文本层 p213:22) | R63/R64/R65/R66 = Row 3/8/9/12, 渲染页均为 "Mono Sub" |
| `B-GF T-1` | p224:24, GF Example 1 "inheritabilty" | R67 = p225 Example 2, PDF 印 "inheritability" |
| `B-IS T-3` | p236:17, "Rows 3-4" 说明句 "NON-STUDY RELATED IMMUNOGENICITY" | R68/R69 叙述句 (p236:3-4, 10) 与 R71 表格 Row 3 (p236:28) 均印 "NON-STUDY-RELATED" |
| `B-IS T-1/T-2` | p236:37/40, Ex5 Row 6/7 STUDYID "RSC1230" | R70 = Row 1, R72 = Row 5, STUDYID 均印 RSV1230 |
| `B-MB T-1` | p262:21-28, Ex3 suppmb.xpt 的 Row 列 1,2,3,4,7,8 | R73 = p261 relspec.xpt Row 5; R75 = p262 mb.xpt Row 5; 都不是 suppmb |
| `B-MB T-2/T-3` | p263:25, Example 4 mb.xpt 表头 "MBGPRID" / "MBTRESN" | R74 = p262:4, Example 3 mb.xpt 表头, PDF 印 MBGRPID / MBSTRESN |
| `B-MS T-2` | p262:36, "Rows 3-4" 句 "MSCONC and MSCONU" | R76 = "Rows 1-2" 句 (p262:33 印 MSCONCU); R77 = ms.xpt 表头 (p262:39 印 MSCONCU) |

## 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| R53 | `ig34_p0206_a005` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0206.txt:20-24`; KB `knowledge_base/domains/CP/assumptions.md:78` | 笔误在 p205 assumption 4 (KB :58); assumption 8 PDF 原印 CPCSMRKS, KB 逐字一致 |
| R54 | `ig34_p0211_a012` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p211 Ex2 Row 1; KB `knowledge_base/domains/CP/examples.md:87` | 笔误在 Row 6 (p212); Row 1 CPDTC 印 2020-08-16T12:20; 逐格比对一致 (STUDYID IM001-123、USUBJID "0005 00542" 两行折行) |
| R55 | `ig34_p0211_a013` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p211 Row 2; KB `CP/examples.md:88` | 笔误在 Row 6; 逐格一致 (CPGRPID=1, CPGATE "LEUK, VIABLE")。原子 verbatim 把 CPGRPID 抽成空 (原子抽错, KB=PDF) |
| R56 | `ig34_p0211_a014` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p211 Row 3; KB `CP/examples.md:89` | 笔误在 Row 6; 逐格一致 (CPGATDEF "FSC SSC\|CD45+")。原子写 "FSC SSC/CD45+" (原子抽错) |
| R57 | `ig34_p0211_a015` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p211 Row 4; KB `CP/examples.md:90` | 笔误在 Row 6; 逐格一致 (CPDTC T12:20) |
| R58 | `ig34_p0211_a016` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p211 Row 5; KB `CP/examples.md:91` | 笔误在 Row 6; 逐格一致 (CPDTC T12:20) |
| R59 | `ig34_p0212_a002` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p212 Row 7; KB `CP/examples.md:93` | 笔误在 Row 6 (同页上一行); Row 7 CPDTC 印 T12:20; 逐格一致 (CPGRPID 1, CPCSMRKS "7AAD-ANXV+")。原子把 CPGRPID 抽成 6、CPCSMRKS 抽成 "ANXV-" (原子抽错) |
| R60 | `ig34_p0212_a003` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p212 Row 8; KB `CP/examples.md:94` | 笔误在 Row 6; 逐格一致 (CPGRPID 1, CPGATE LYM, CPDTC T12:20)。原子 CPGRPID=6、CPCSMRKS "ANXV-"、CPGATE 空 (原子抽错) |
| R61 | `ig34_p0212_a004` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p212 Row 9; KB `CP/examples.md:95` | 笔误在 Row 6; 逐格一致 |
| R62 | `ig34_p0212_a005` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p212 Row 10; KB `CP/examples.md:96` | 笔误在 Row 6; 逐格一致 |
| R63 | `ig34_p0213_a010` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p213 Ex3 Row 3; KB `CP/examples.md:131` | 笔误在 Row 2 "MonoSub" (KB :130); Row 3 PDF 印 "Mono Sub"; 逐格一致 (CPSBMRKS 空, NON-PROLIFERATING, Ki67-)。原子漏了 CPSBMRKS 空格、"FSC+SSC+\|CD14+" 丢了管道符 (原子抽错) |
| R64 | `ig34_p0213_a015` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p213 Row 8; KB `CP/examples.md:136` | 笔误在 Row 2; Row 8 印 "Mono Sub"; 结果值 PDF 366 = KB 366。原子写 368 (原子抽错) |
| R65 | `ig34_p0213_a016` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p213 Row 9; KB `CP/examples.md:137` | 笔误在 Row 2; Row 9 印 "Mono Sub"; 逐格一致 |
| R66 | `ig34_p0213_a019` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | 渲染页 p213 Row 12; KB `CP/examples.md:140` | 笔误在 Row 2; Row 12 印 "Mono Sub"; CPSBMRKS PDF "CDxx+CDyy-" = KB; CPMRKSTR "CD14+CDxx+CDyy-ANXV+" 一致。原子 CPSBMRKS 写 "CDxx+CDyy+" (原子抽错) |
| R67 | `ig34_p0225_a012` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0225.txt:45-47`; KB `knowledge_base/domains/GF/examples.md:52` | 笔误在 p224:24 Example 1 (KB :5); Example 2 PDF 原印 "inheritability", KB 逐字 |
| R68 | `ig34_p0236_a002` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | PDF `ig34_p0236.txt:3-7`; KB `knowledge_base/domains/IS/examples.md:103` | 笔误在 p236:17 "Rows 3-4" 说明 (KB :108); 本句 PDF 两处均印 "NON-STUDY-RELATED"; KB 实为逐字 |
| R69 | `ig34_p0236_a003` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0236.txt:8-11`; KB `IS/examples.md:105` | 笔误在 p236:17; 本句 PDF 印 “NON-STUDY-RELATED IMMUNOGENICITY” (弯引号), KB 逐字 |
| R70 | `ig34_p0236_a009` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0236.txt:22-24`; KB `IS/examples.md:115` | 笔误 RSC1230 在 Row 6/7; Row 1 STUDYID 印 RSV1230; 逐格一致 |
| R71 | `ig34_p0236_a011` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0236.txt:28-30`; KB `IS/examples.md:117` | 笔误在 p236:17 叙述句; 表格 Row 3 ISCAT 印 "NON-STUDY-RELATED IMMUNOGENICITY"; 逐格一致 |
| R72 | `ig34_p0236_a013` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0236.txt:34-36`; KB `IS/examples.md:119` | 笔误在 Row 6/7 (p236:37/40); Row 5 STUDYID 印 RSV1230; 逐格一致 (ISGRPID 空, 1:90/90/90, VISIT 1, 2017-07-27) |
| R73 | `ig34_p0261_a010` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0261.txt:13`; KB `knowledge_base/domains/MB/examples.md:168` | 登记笔误在 p262 suppmb.xpt 的 Row 列 (KB :204); 本条是 relspec.xpt Row 5, PDF 行号就是 5; 逐格一致 |
| R74 | `ig34_p0262_a003` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0262.txt:4`; KB `MB/examples.md:187` | 登记笔误在 p263:25 Example 4 表头 (KB :241); 本条是 Example 3 表头, PDF 印 MBGRPID / MBSTRESN, 24 列顺序与 KB 一致 |
| R75 | `ig34_p0262_a008` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | PDF `ig34_p0262.txt:13-14`; KB `MB/examples.md:193` | 登记笔误在 suppmb.xpt 的 Row 列; 本条是 mb.xpt Row 5, 逐格一致 (MBLNKGRP 1, 147 CFU, 14700 CFU/mL, WEEK 1, 2011-01-17T06:00)。原子漏了 MBLNKGRP=1 (原子抽错) |
| R76 | `ig34_p0262_a019` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | PDF `ig34_p0262.txt:32-34`; KB `knowledge_base/domains/MS/examples.md:64` | 笔误在 p262:36 "Rows 3-4" (KB :65); "Rows 1-2" PDF 印 MSCONCU, KB 一致 (只是加了粗体标签) |
| R77 | `ig34_p0262_a022` | TYPO_SIB | EXACT | NOT_AFFECTED | PDF `ig34_p0262.txt:39-40`; KB `MS/examples.md:69` | 笔误在 p262:36 叙述句; ms.xpt 表头 PDF 印 MSCONCU, 20 列顺序与 KB 一致 |

## 计数

- TYPO_AFFECTED: 0
- NOT_AFFECTED: 25
- NOT_HOLD: 0
- UNVERIFIABLE: 0

本包中, 候选登记的笔误都不在样本原子对应的那一处 (分别在同页另一行、相邻页、另一个例子或另一张表)。

## 样本外发现 / 附注 (不计入判定, 不修)

1. **原子 verbatim 抽错 (KB 与 PDF 一致)**: R55、R56、R59、R60、R63、R64、R66、R75 的原子 verbatim 与 PDF 有格值差异 (见上表说明)。KB 都与 PDF 一致, 所以按 KB↔PDF 比对, 现标签 EQUIVALENT 成立。但如果严格按标签定义 ("原子≠PDF 且 KB=PDF" 算 ATOM_ERR), 这几条也可以标成 ATOM_ERR。这里只记录, 是否改标由主控决定。
2. 无 KB 内容问题。
