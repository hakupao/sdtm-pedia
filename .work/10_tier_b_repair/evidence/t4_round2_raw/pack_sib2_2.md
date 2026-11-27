# T4.1 第二轮补检 — TYPO_SIB2 补充批 b2 (S21-S40) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:46:14Z (`date -u`)
- 输入: `.work/10_tier_b_repair/work/t4/round2/round2b_pack_2.md`; brief `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round2_v1.0.md` (TYPO_SIB 口径)
- 登记查表: `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (按 id grep)
- 看过的渲染页 (SDTMIG v3.4, `pdftoppm` 输出在 scratchpad `r2_b2/`, 未写仓库): p213 (全页 + 放大), p256 (item 4 区域 250dpi 放大), p262, p357; 另渲染 p280/p297/p298/p419/p425/p433 备查 (叙述句以文本层为准, 文本层无歧义)
- 用过的命令: `sed -n` 读 `work/pdf_pages/ig34_p0{213,256,257,262,279,280,281,296,297,298,357,419,425,433}.txt`; `grep -n` 在 `knowledge_base/domains/{CP,MS,MB,PC,NV,TR,TS}/*.md`、`knowledge_base/chapters/ch08_relationships.md` 定位; `grep` 登记 id; `pdftoppm -r 110/220/250 -f N -l N [-x -y -W -H] -png`; `pdftotext -layout -f 256 -l 256`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| S21 | `ig34_p0213_a014` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | p213 渲染页 cp.xpt Row 7 / `ig34_p0213.txt:34-35`; `knowledge_base/domains/CP/examples.md:135` | B-CP T-6 笔误 "MonoSub" 在 Row 2 (渲染页确认), 不在 Row 7. Row 7 KB 26 格与 PDF 逐格一致 (CPTEST Monocytes, CPGATE MONO, CPGATDEF FSC+SSC+\|CD14+, CPTSTPNL MONOCYTE CD SUBSETS, 394...). 附注: 原子 verbatim 漏了 CPGATE "MONO" 一格且 CPGATDEF 丢了 "\|" (抽取物问题, KB 正确) |
| S22 | `ig34_p0213_a017` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | p213 渲染页 Row 10 / `ig34_p0213.txt:40-41`; `CP/examples.md:138` | 笔误在 Row 2. Row 10 KB 与 PDF 逐格一致 (CPTEST "Mono Sub/Mono", CPMRKSTR CD14+CDxx+CDyy-/CD14+, 93.00 %). 原子同样漏 CPGATE 一格 (抽取物) |
| S23 | `ig34_p0213_a018` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | p213 渲染页 Row 11 / `ig34_p0213.txt:42-43`; `CP/examples.md:139` | 笔误在 Row 2. Row 11 PDF CPMRKSTR = "CD14+CDxx-CDyy+/CD14+" (渲染页确认), KB 同; 原子写 "CDxx-CDyy-" 是抽取错 (另漏 CPGATE 格), KB 按 PDF 正确, 其余格一致 |
| S24 | `ig34_p0256_a007` | TYPO_SIB2 | EQUIVALENT | **TYPO_AFFECTED** | p256 渲染页 (250dpi 放大) item 4 / `ig34_p0256.txt:13`; `knowledge_base/domains/MS/assumptions.md:27` | 登记 `B-MS T-5`. PDF 原文 "It should only populated with values" (缺 be, 渲染页确认); KB "It should only be populated" = 改正值. 其余文字逐字一致. 现标签 EQUIVALENT 应为 PDF_TYPO |
| S25 | `ig34_p0257_a014` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0257.txt:24-25` (ms.xpt Row 7); `MS/examples.md:29` | B-MS T-1 笔误 (MSSTRESC 空) 在 Row 9 (`ig34_p0257.txt:28`). Row 7 MSSTRESC = 23, KB 22 格与 PDF 一致 |
| S26 | `ig34_p0262_a007` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | p262 渲染页 mb.xpt Row 4 / `ig34_p0262.txt:11-12`; `MB/examples.md:192` | B-MB T-1 笔误 (suppmb Row 列 1,2,3,4,7,8 跳号) 在同页 suppmb 表 (KB :202-203 改为 5,6), 不在 mb.xpt. Row 4 KB 与 PDF 逐格一致 |
| S27 | `ig34_p0262_a009` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | p262 渲染页 mb.xpt Row 6 / `ig34_p0262.txt:15-16`; `MB/examples.md:194` | 笔误在 suppmb 表 Row 列. mb.xpt Row 6 PDF: MBSEQ 6, MBGRPID 2, MBLNKGRP 1, 100.3, MTB, COLONY COUNT, 2+... (渲染页确认), KB 一致. 附注: 原子 verbatim 写 MBSEQ "8"、MBLNKGRP 空, 与 PDF 不符 (抽取错; 按定义更接近 ATOM_ERR 的形态, 但 KB 内容完整无误, 不算 NOT_HOLD, 列为标签级别观察) |
| S28 | `ig34_p0279_a035` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0279.txt:38-39` (Example 2 引言); `knowledge_base/domains/PC/examples.md:196` (### Example 2 下) | 包内 KB 指针为 "(无)", 自行 grep 找到 :196 逐字承载. B-PCPP T-8b 笔误 "DYDRGX_HALF" 在 p280 Example 3 引言 (`ig34_p0280.txt:44`, KB :278), 不在本句. 本句 PDF "DY1_DRGX" 与 KB 一致 |
| S29 | `ig34_p0281_a046` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0281.txt:54-55` (Ex3 Method D Rows 1-17); `PC/examples.md:353` (### Example 3 / #### Method D 下) | 包内 KB 指针为 "(无)", 自行 grep 找到 :353, 逐字一致 (仅 "- " 列表前缀). 三条候选登记都在别处: S-SPC2 PCPP T-11 ("1 through "7") 在 `ig34_p0280.txt:18` (Ex2 Method C); S-SPC2 N-1 ("PP records with PCSEQ") 在 `ig34_p0281.txt:2,4` (Ex3 Method B); S-SPC2 N-2 ("PGRPID") 在 `ig34_p0281.txt:35` (Ex3 Method C). 本句 PDF 原文无笔误 |
| S30 | `ig34_p0296_a017` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0296.txt:26`; `knowledge_base/domains/NV/examples.md:9` | B-NV T-1 "an fluorodeoxyglucose" 在 Rows 5-6 句 (`ig34_p0296.txt:28`, KB :11). 本句一致 (KB 仅加粗标签) |
| S31 | `ig34_p0296_a018` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0296.txt:27`; `NV/examples.md:10` | 同上, 笔误在 Rows 5-6 句; 本句一致 |
| S32 | `ig34_p0297_a037` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0297.txt:41` + `ig34_p0298.txt:1` (句子跨页: "...may have an / interpretation."); `NV/examples.md:63` | B-NV N-2 "links the each" 在后一句 "NVGRPID links the each VEP component..." (`ig34_p0298.txt:1-2`), 不在本原子. 本原子 (截断于页界) 内容 KB :63 逐字承载, 且 KB 补全了跨页的 "interpretation." |
| S33 | `ig34_p0357_a013` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | p357 渲染页 tr.xpt Row 14 / `ig34_p0357.txt:30-33`; `knowledge_base/domains/TR/examples.md:83` | B-TR T-2 笔误 (TRSTRESC -60) 在 Row 15 (渲染页确认). Row 14 TRORRES/TRSTRESC/TRSTRESN 均 -25, KB 23 格与 PDF 一致 |
| S34 | `ig34_p0419_a005` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0419.txt:15-16`; `knowledge_base/domains/TS/assumptions.md:43` | B-TS T-2 ("Dose") / T-3 ("DOSFREQ") 在下一句 "There are 2 records each for TSPARMCD = ..." (`ig34_p0419.txt:16-17`). 本句 "For example, ... following records." KB 逐字一致 |
| S35 | `ig34_p0419_a007` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0419.txt:17-18`; `TS/assumptions.md:43` | 同上, 笔误在 "There are 2 records..." 句; 本句 "Records with the same TSGRPID are associated with each other." 一致 |
| S36 | `ig34_p0419_a008` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0419.txt:18-19`; `TS/assumptions.md:43` | 同上; 本句 "...only 1 record for DOSU is needed." 一致 |
| S37 | `ig34_p0425_a023` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0425.txt:29`; `TS/assumptions.md:115` | B-TS T-6 "MAXAGE case" 在下一句 "For example, for the MAXAGE case..." (`ig34_p0425.txt:29-30`). 本句 "The values at levels 3 and 4 ..." 一致 |
| S38 | `ig34_p0425_a025` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0425.txt:32-33`; `TS/assumptions.md:115` | 同上, 笔误在 MAXAGE 句; 本句 "The null flavor PINF provides..." 一致 |
| S39 | `ig34_p0433_a031` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0433.txt:43-44`; `knowledge_base/chapters/ch08_relationships.md:241` | B-SUPPQUAL T-1 "llustrate" 在 `ig34_p0433.txt:28` ("These examples llustrate", 节引言); B-ch08 T-5 是 `ig34_p0433.txt:42` 的无编号标签 "Example". 本句 "The parent domain (RDOMAIN) is QS, and IDVAR is QSCAT." KB 逐字一致 |
| S40 | `ig34_p0433_a032` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0433.txt:44-45`; `ch08_relationships.md:241` | 同上; 本句 "QNAM holds ... (QSLANG)." 一致 |

## 计数

| 判定 | 数 |
|---|---|
| TYPO_AFFECTED | 1 (S24) |
| NOT_AFFECTED | 19 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |
| 合计 | 20 |

TYPO_AFFECTED 明细: S24 `ig34_p0256_a007` — 登记 `B-MS T-5`; PDF "It should only populated with values"; KB `knowledge_base/domains/MS/assumptions.md:27` "should only be populated" → 应改标 PDF_TYPO (并入 `evidence/checkpoints/t4_relabel_pending.md` 由主控处理).

## 标签级别观察 (不算样本判定的 NOT_HOLD)

- 原子 verbatim 与 PDF 不符、KB 按 PDF 正确的: S21/S22/S23 (CP 原子漏 CPGATE "MONO" 一格; S21 CPGATDEF 丢 "|"; S23 CPMRKSTR 写成 "CDxx-CDyy-"), S27 (MB 原子 MBSEQ 写 "8"、MBLNKGRP 空; PDF 为 6 / 1). KB 内容均完整、值一致, 故终态 EQUIVALENT 对 "KB 是否承载" 成立; 若按严格定义这些原子形态更接近 ATOM_ERR, 留主控决定是否进入标签级别后续项.
- S28 / S29 包内 KB 指针为 "(无)", 实际 KB 分别在 `knowledge_base/domains/PC/examples.md:196` / `:353` 逐字承载 (指针缺失, 非内容缺失).

## 样本外发现的 KB 内容问题

无. (顺带看到 `ig34_p0280.txt:52,54` PDF 写 "DYIDRGX_A" / "DYIDRGX_HALF" (字母 I), KB `PC/examples.md:284-285` 写 "DY1DRGX_..."; 已核 registry 有 `B-PCPP T-8` 覆盖, 不另列.)
