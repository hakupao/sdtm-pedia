# T4.1 Q9 扩检 — 包 2 结果 (Q9_SV20_EQUIV, Q27-Q52, 26 条)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:01:40Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_q9_extension_v1.0.md` (五选一) + `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (背景 / 输出)
- 看过的渲染页: `source/cdisc/SDTM_v2.0.pdf` p2, p3 (TOC). p4/p5/p8/p9 为纯正文段落, 用文本层核对 (无表格列归属问题)
- 用过的命令:
  - `grep -n '^#' knowledge_base/model/*.md` (节标题全表)
  - `grep -rn -i 'appendi\|representations and warranties' knowledge_base/model/` (0 命中)
  - `grep -n '^#\|Appendices\*\*' knowledge_base/chapters/ch10_appendices.md`; `grep -rn 'Appendix A' knowledge_base/`
  - `cat .work/10_tier_b_repair/work/pdf_pages/sv20_p000{2,3,4,5,8,9}.txt`
  - `grep -E '"sv20_p00(74|70|73)_a00[1-3]"|"sv20_p0003_a0(09|10|11|12)"' .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl`
  - Read `knowledge_base/model/01_concepts_and_terms.md:1-160`
- 说明: 包里 Q40-Q52 的 KB 指针全部指向 SDTMIG 的 `knowledge_base/chapters/ch0x_*.md` (位置错), 已全部改在 SDTM v2.0 的 `knowledge_base/model/` 里重找. TOC 页码 KB 不承载, 按 brief 只核节号 + 标题.

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| Q27 | sv20_p0002_a040 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0002.txt:49`, 渲染 p2; `knowledge_base/model/05_study_level_data.md:192` | TOC→标题 `### 5.1.5 Trial Inclusion/Exclusion Criteria (TI)` (多缩写) |
| Q28 | sv20_p0002_a042 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0002.txt:51`, 渲染 p2; `05_study_level_data.md:231` | TOC→标题 `### 5.1.7 Challenge Agent Characterization (AC)` |
| Q29 | sv20_p0002_a043 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0002.txt:52`, 渲染 p2; `05_study_level_data.md:254` | TOC→标题 `## 5.2 Study References` (仅大小写; 渲染页为小型大写) |
| Q30 | sv20_p0002_a044 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0002.txt:53`, 渲染 p2; `05_study_level_data.md:261` | TOC→标题 `### 5.2.1 Device Identifiers Dataset (DI)` |
| Q31 | sv20_p0002_a045 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0002.txt:54`, 渲染 p2; `05_study_level_data.md:299` | TOC→标题 `### 5.2.2 Non-host Organism Identifiers Dataset (OI)` |
| Q32 | sv20_p0003_a001 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:5`, 渲染 p3; `knowledge_base/model/06_relationship_datasets.md:5` | TOC→标题 `## 6 Datasets for Representing Relationships` (包指针给的是 :1 文件标题, 实际节标题在 :5) |
| Q33 | sv20_p0003_a002 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:6`, 渲染 p3; `06_relationship_datasets.md:23` | TOC→标题 `## 6.1 Related Records Dataset (RELREC)` |
| Q34 | sv20_p0003_a003 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:7`, 渲染 p3; `06_relationship_datasets.md:52` | TOC→标题 `## 6.2 Supplemental Qualifiers Dataset (SUPP--)` |
| Q35 | sv20_p0003_a004 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:8`, 渲染 p3; `06_relationship_datasets.md:86` | TOC→标题 `## 6.3 Pool Definition Dataset (POOLDEF)` (包指针 :40 是 APID 表行, 错位; 已自找) |
| Q36 | sv20_p0003_a005 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:9`, 渲染 p3; `06_relationship_datasets.md:103` | TOC→标题 `## 6.4 Related Subjects Dataset (RELSUB)` |
| Q37 | sv20_p0003_a006 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:10`, 渲染 p3 ("Device-subject"); `06_relationship_datasets.md:121` | TOC→标题 `## 6.5 Device-subject Relationships Dataset (DR)` |
| Q38 | sv20_p0003_a007 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:11`, 渲染 p3; `06_relationship_datasets.md:138` | TOC→标题 `## 6.6 Associated Persons Relationships (APRELSUB)` |
| Q39 | sv20_p0003_a008 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | `sv20_p0003.txt:12`, 渲染 p3; `06_relationship_datasets.md:158` | TOC→标题 `## 6.7 Related Specimens Dataset (RELSPEC)` |
| Q40 | sv20_p0003_a011 | Q9_SV20_EQUIV | EQUIVALENT | **NOT_HOLD** (TOC) | `sv20_p0003.txt:18`, 渲染 p3; KB: `knowledge_base/model/` 无 §9 (grep `appendi` 0 命中) | PDF: SDTM v2.0 节标题 "9 APPENDICES". KB: `knowledge_base/model/01..06` 没有 §9 Appendices 这一节. 旧匹配 `md_ch10_a240` = `knowledge_base/chapters/ch10_appendices.md:411` 的 `**Appendices**`, 那是 SDTMIG v3.4 Appendix E 修订历史表里的分组小标题, 属于另一份文档, 位置错, 不是本节标题 |
| Q41 | sv20_p0003_a012 | Q9_SV20_EQUIV | EQUIVALENT | **NOT_HOLD** (TOC) | `sv20_p0003.txt:19`, 渲染 p3; KB: `knowledge_base/chapters/ch10_appendices.md:422` | PDF: SDTM v2.0 "APPENDIX A: REPRESENTATIONS AND WARRANTIES, LIMITATIONS OF LIABILITY, AND DISCLAIMERS". KB: `knowledge_base/model/` 没有这一节; 只有 SDTMIG v3.4 的 `## Appendix F: Representations and Warranties, Limitations of Liability, and Disclaimers` (`ch10_appendices.md:422`). 标题文字相同, 但编号不同 (A vs F), 而且在另一份文档的章节里 → 按 TOC 口径属于 "没有该节" |
| Q42 | sv20_p0004_a004 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0004.txt:9-10`; `knowledge_base/model/01_concepts_and_terms.md:9` | 实为逐字 (§1.1). 包指针 `ch01_introduction.md` 是 SDTMIG, 错位 |
| Q43 | sv20_p0004_a006 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0004.txt:12-14`; `01_concepts_and_terms.md:11` | 实为逐字 (§1.1). 包指针 SDTMIG ch01:11 的句子是 "clinical data that will be submitted…", 意思不同; 正确位置在 model/01 |
| Q44 | sv20_p0004_a014 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0004.txt:23-24`; `01_concepts_and_terms.md:15` | 实为逐字 (§1.2) |
| Q45 | sv20_p0004_a017 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0004.txt:27-28`; `01_concepts_and_terms.md:17` | 实为逐字 (列表项 + URL 一致) |
| Q46 | sv20_p0004_a026 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0004.txt:46-47`; `01_concepts_and_terms.md:28` | 实为逐字 (URL 一致) |
| Q47 | sv20_p0005_a007 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0005.txt:13-14`; `01_concepts_and_terms.md:38` | 实为逐字 (§1.4) |
| Q48 | sv20_p0008_a003 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0008.txt:9-10`; `01_concepts_and_terms.md:112` | 实为逐字 (KB 多了 `**observations**` 粗体, 允许) |
| Q49 | sv20_p0008_a006 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0008.txt:15-19`; `01_concepts_and_terms.md:114` | 实为逐字 (4 句全在; "Special-purpose" 是 PDF 跨行断字) |
| Q50 | sv20_p0008_a008 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0008.txt:23-24`; `01_concepts_and_terms.md:118` | 实为逐字 |
| Q51 | sv20_p0009_a002 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:6-7`; `01_concepts_and_terms.md:158` | 实为逐字 (分号版在 model/01; 包指针 SDTMIG ch02:41 是句号拆句版, 属另一文档) |
| Q52 | sv20_p0009_a003 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:8-9`; `01_concepts_and_terms.md:158` | 实为逐字 (URL 一致) |

## 计数

| 层 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE | 合计 |
|---|---|---|---|---|---|
| Q9_SV20_EQUIV (包 2) | 24 | 0 | 2 | 0 | 26 |

- TOC 条目: 15 条 (Q27-Q41), 其中 13 条 HOLDS、2 条 NOT_HOLD (Q40, Q41)
- 非 TOC: 11 条 (Q42-Q52), 全部 HOLDS 且都是逐字承载
- NOT_HOLD: Q40 `sv20_p0003_a011`, Q41 `sv20_p0003_a012`

### NOT_HOLD 补充 (供主控定处理方式, 不是判定)
- 这两条的根源一样: SDTM v2.0 §9 / Appendix A 在 KB 的 SDTM v2.0 部分 (`knowledge_base/model/`) 没有节标题. 旧匹配器把它们配到了 SDTMIG v3.4 `ch10_appendices.md` 里文字相近的地方, 属于跨文档错配.
- 同一个 TOC 页上, §7 (`sv20_p0003_a009`) 和 §8 (`sv20_p0003_a010`) 两条已在台账里标成 INTENTIONAL_EXCLUDE / VERSION_MISMATCH (`user-ack-2026-05-12-P6-T2`). Q40/Q41 是同一类 "KB 不收的 v2.0 章节", 但口径里没有现成的 R1 类可以套, 所以按 brief 判 NOT_HOLD. 是否改标 IE 由主人决定.
- 内容层面: Appendix A 的免责正文是 CDISC 通用样板, KB 在 SDTMIG `ch10_appendices.md:422-` (Appendix F) 有同文. 实际损失的信息只有 "SDTM v2.0 也带这份附录" 这个结构事实.

## 样本外发现的 KB 内容 / 台账问题 (只记录, 不修)
1. 台账 `sv20_p0074_a001` (PARTIAL → `md_ch10_a001`)、`sv20_p0074_a002` / `sv20_p0074_a003` (EXACT → `md_ch10_a245` / `md_ch10_a246`): SDTM v2.0 p74 的 Appendix A 原子都配到了 SDTMIG `knowledge_base/chapters/ch10_appendices.md` (Appendix F). 和 Q40/Q41 是同一种跨文档错配. 文字可能确实相同, 但 "位置正确" 不成立. 建议在 Q9 / 旧 EXACT 口径里一起看 (旧 EXACT 的指纹复验只检查文字能不能命中, 不检查在哪份文档).
2. 包 2 的 KB 指针生成脚本 (`scripts/t4/t4_q9_sample.py`) 对 sv20 §1/§2/§9 原子全都指向 SDTMIG `chapters/` 文件, 没有一条指向 `knowledge_base/model/01_concepts_and_terms.md`. 这不影响本次判定 (都已自己重找), 但别的包如果直接采信指针会出偏差.
