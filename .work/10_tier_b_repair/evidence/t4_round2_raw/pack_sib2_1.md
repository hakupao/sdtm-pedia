# T4.1 第二轮补检 — TYPO_SIB2 补充批 b1 (S1-S20) 审查结果

- 审查者: `oh-my-claudecode:tracer` (opus), 只读角色
- 时间: 2026-11-27T05:46:20Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round2_v1.0.md` § TYPO_SIB (冲突以后者为准)
- 样本包: `.work/10_tier_b_repair/work/t4/round2/round2b_pack_1.md`
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, pdftoppm -r 150, 输出在 scratchpad `r2_b1/`): p10 (§1.5 段落裁切), p37 (§4.3.2 裁切), p43 (§4.4.7 裁切), p69 (整页), p118 (整页), p201 (整页), p212 (整页), p213 (整页)。p44 / p210 / p211 只看文本层 (内容无歧义)。
- 用过的命令:
  - `grep -E '"id": ?"(B-ch01 T-2|B-ch04 T-3|S-CH4 T-10d|S-CH4 T-10e|B-DM T-3|B-EX T-6|S-SPC1 CP T-20|B-CP T-5|B-CP T-6)"' .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl`
  - 台账 / 原子邻居: python 读 `work/coverage_ledger.wc.jsonl` (`pdf_atom_id`, `verdict`) 与 `work/pdf_atoms.jsonl` (`atom_id`, `verbatim`), 查 p10 a020-a025、p43 a015-a023、p44、p69 a001-a012、p118 a015-a018、p201、p212、p213 a010-a012
  - `grep -n '04:20\|12:20' work/pdf_pages/ig34_p021[012].txt`; `cat -n work/pdf_pages/ig34_p0069.txt`; `sed -n` 读 KB 行
  - `pdftoppm -r 150 -f N -l N [-x -y -W -H] -png "<pdf>" <scratchpad>/r2_b1/...`

## 表格

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| S1 | `ig34_p0010_a020` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0010.txt:33-34` + p10 渲染; `chapters/ch01_introduction.md:105` | 该句 (--DRVFL 段末句) 与登记 B-ch01 T-2 无关; 笔误在 --LNKID 段第 2 句 (原子 `ig34_p0010_a023`, 已是 PDF_TYPO)。KB 与 PDF 一致 |
| S2 | `ig34_p0010_a022` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0010.txt:36-37` + p10 渲染; `ch01_introduction.md:109` | 定义句, PDF 与 KB 一致。B-ch01 T-2 ("MANY → --LNKID") 在下一句 a023 |
| S3 | `ig34_p0010_a024` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0010.txt:39-40` + p10 渲染; `ch01_introduction.md:109` | "The examples ... --LNKID and --LNKGRP." PDF 与 KB 一致; 笔误在前一句 a023 |
| S4 | `ig34_p0037_a002` | TYPO_SIB2 | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0037.txt:2-3` + p37 渲染; `chapters/ch04_general_assumptions.md:668` | 登记 `B-ch04 T-3`。PDF 印 "in the case that appears the source"; KB 写 "appears in the source"。差异即已登记笔误, 现标签应为 PDF_TYPO。其余内容一致 |
| S5 | `ig34_p0043_a015` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0043.txt:20-21` + p43 渲染; `ch04_general_assumptions.md:943` | --STRF 段句子, PDF 与 KB 一致。T-10d 在 --ENRF 段 "variables.As" (a019/a020 交界), T-10e 在 "CMSTRF.Some" (a022/a023 交界) |
| S6 | `ig34_p0043_a019` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0043.txt:26-27` + p43 渲染; `ch04_general_assumptions.md:947` | 原子文字 "...--ENRF variables." PDF 与 KB 逐词一致。T-10d 只是句号后缺空格 ("variables.As"), 落在本原子与下一原子 a020 (EXACT) 的句界上, 不改本原子任何字符 (空白差异按 EXACT/EQUIVALENT 定义本就归一) |
| S7 | `ig34_p0044_a010` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0044.txt:16-17`; `ch04_general_assumptions.md:979` | --STRTPT/--ENRTPT 句, PDF 与 KB 一致。T-10d/e 都在 p43 |
| S8 | `ig34_p0069_a002` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0069.txt:21` + p69 渲染; `domains/DM/examples.md:68` | PDF 对应处 = Example 3 "Row 1: Subject 001 was randomized to drug A." KB:68 与 PDF 一致 (包给的 KB:20 是 p68 Example 2, 定位偏)。笔误 ACTRMCD 在同段第 3 句 (S10)。附注: 原子 verbatim 写 "arm A", PDF 是 "drug A" — 原子抽错, KB 按 PDF; 标签级别更贴切是 ATOM_ERR, 但内容层 KB 无问题 |
| S9 | `ig34_p0069_a003` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0069.txt:21-22` + p69 渲染; `DM/examples.md:68` | "...ARMCD is "AA"." PDF 与 KB 一致; 笔误在下一句 a004 |
| S10 | `ig34_p0069_a004` | TYPO_SIB2 | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0069.txt:22-23` + p69 渲染; `DM/examples.md:68` | 登记 `B-DM T-3`。PDF 印 "assigned, so ACTRMCD is also "AA""; KB 写 "ACTARMCD"。差异即已登记笔误。附注: 原子 verbatim 抽成 "ACTRMD" (与 PDF 的 ACTRMCD 也不同), 不影响判定 |
| S11 | `ig34_p0069_a006` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0069.txt:24-26` + p69 渲染; `DM/examples.md:70` | Row 2 第 2 句, PDF 与 KB 一致; 与 ACTRMCD 无关 |
| S12 | `ig34_p0069_a009` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0069.txt:28` + p69 渲染; `DM/examples.md:72` | Row 3 首句, PDF 与 KB 一致 |
| S13 | `ig34_p0069_a010` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0069.txt:28-29` + p69 渲染; `DM/examples.md:72` | PDF 与 KB 一致 |
| S14 | `ig34_p0118_a016` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0118.txt:20` + p118 渲染; `domains/EX/examples.md:362` | 原子只含首句 "Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED"." PDF 与 KB 一致。B-EX T-6 ("represented in mg/mL") 在后一句, 即原子 `ig34_p0118_a017` (已是 PDF_TYPO) |
| S15 | `ig34_p0201_a005` | TYPO_SIB2 | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0201.txt:15-18` + p201 渲染 (CPCELSTA 行 CDISC Notes); `domains/CP/spec.md:113-120` | 登记 `S-SPC1 CP T-20`。PDF 印 "the values in CPCELSTA and CPSMRKS"; KB 写 "CPCELSTA and CPCSMRKS"。其余格 (Cell State / Char / (CELSTATE) / Variable Qualifier / Perm; KB 另附 C181172) 一致。附注: 原子 verbatim 抽成 "CPSBMRKS", 与 PDF 也不同 |
| S16 | `ig34_p0210_a026` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0210.txt:51-52` (Example 1b cp.xpt row 2); `domains/CP/examples.md:63` | 逐格比对 21 格一致, CPDTC = 2021-08-16T04:20 (Ex1b 全表均 T04:20, 无笔误)。B-CP T-5 在 Example 2 row 6 (p212), 不是本表 |
| S17 | `ig34_p0212_a001` | TYPO_SIB2 | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0212.txt:2-4` + p212 渲染 (Ex2 row 6); `domains/CP/examples.md:92` | 登记 `B-CP T-5`。PDF row 6 CPDTC 印 "2020-08-16T04:20" (同表 row 1-5、7-11 均 T12:20); KB 写 "2020-08-16T12:20"。其余 25 格逐格一致 (CPGATE=LYM, CPGATDEF=FSC SSC\|CD45+ 等)。附注: 登记 pdf_page 写 211, 实际该行在物理页 / 印刷页 212 (表从 p211 起头); 原子 verbatim 把 CPGATE/CPGATDEF 抽错位, KB 按 PDF |
| S18 | `ig34_p0213_a008` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0213.txt:21-22` + p213 渲染 (Ex3 row 1); `domains/CP/examples.md:129` | 26 格逐格一致 (CPTEST "Monocytes")。B-CP T-6 "MonoSub" 在 row 2 (KB:130) |
| S19 | `ig34_p0213_a011` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0213.txt:27-28` + p213 渲染 (row 4); `CP/examples.md:132` | 逐格一致, CPTEST "Mono Sub/Mono", CPMRKSTR "CD14+Ki67+/CD14+" (原子 verbatim 漏 "+", 抽取物问题; KB 按 PDF)。MonoSub 笔误在 row 2 |
| S20 | `ig34_p0213_a012` | TYPO_SIB2 | EQUIVALENT | NOT_AFFECTED | `ig34_p0213.txt:29-30` + p213 渲染 (row 5); `CP/examples.md:133` | 逐格一致 (NON-PROLIFERATING / Ki67- / CD14+Ki67-/CD14+ / 87.31 ...) |

## 计数

| 判定 | 条数 | 编号 |
|---|---|---|
| TYPO_AFFECTED | 4 | S4, S10, S15, S17 |
| NOT_AFFECTED | 16 | S1-S3, S5-S9, S11-S14, S16, S18-S20 |
| NOT_HOLD | 0 | — |
| UNVERIFIABLE | 0 | — |

TYPO_AFFECTED 明细 (并入待改标签清单候选, 现标签 EQUIVALENT → 应为 PDF_TYPO):
- S4 `ig34_p0037_a002` — `B-ch04 T-3` — PDF "appears the source" / KB `ch04_general_assumptions.md:668` "appears in the source"
- S10 `ig34_p0069_a004` — `B-DM T-3` — PDF "so ACTRMCD is also" / KB `DM/examples.md:68` "ACTARMCD"
- S15 `ig34_p0201_a005` — `S-SPC1 CP T-20` — PDF "CPCELSTA and CPSMRKS" / KB `CP/spec.md:120` "CPCSMRKS"
- S17 `ig34_p0212_a001` — `B-CP T-5` — PDF row 6 CPDTC "2020-08-16T04:20" / KB `CP/examples.md:92` "T12:20"

## 附注 (不算判定)

- 原子 verbatim 与 PDF 不符 (KB 按 PDF, KB 无问题): S8 ("arm A" vs PDF "drug A"), S10 ("ACTRMD"), S15 ("CPSBMRKS"), S17 (CPGATE/CPGATDEF 错位), S19 ("CD14+Ki67/CD14+" 漏 "+")。S8 若按标签定义严格归类, 更贴切的是 ATOM_ERR 而非 EQUIVALENT, 交主控酌定。
- 登记 `B-CP T-5` 的 `pdf_page` 写 211, 实际 row 6 在 p212 (物理页 = 印刷页 212)。
- 样本包给的 KB 指针偏位: S8 指到 `DM/examples.md:20` (Example 2), 正确为 `:68`; S15 指到 `CP/examples.md:107-109`, 正确为 `CP/spec.md:120`。

## 样本外发现的 KB 内容问题

无 (顺看到 `CP/examples.md:109/117` "CPGATDEF" 对 PDF "CPGATEDEF", 登记表中已有 CPGATEDEF 条目, 不另列)。
