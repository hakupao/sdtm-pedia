# T4.1 Q9 扩检 — 包 1 审查结果 (Q9_SV20_EQUIV, Q1-Q26)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:00:54Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (背景/判定口径/输出) + `subagent_prompts/t4/t4_q9_extension_v1.0.md` (五选一, TOC 规则: KB 有对应节号 + 标题文字 → HOLDS "TOC→标题")
- 看过的渲染页: `source/cdisc/SDTM_v2.0.pdf` p.2 (目录页, Read pages=2)
- 用过的命令:
  - `grep -n '^#' knowledge_base/model/*.md` (列出 KB SDTM v2.0 全部标题)
  - `grep -nE '^\s*5\.1\.(1\.[12]|2|3\.[12]|4\.[123])\s' sv20_p005*.txt` 及 `grep -nE '^\s*(1\.3|2\.1|2\.2|3\.2|4|5)\s+[A-Z]' sv20_p00[0-5]*.txt` (在 `.work/10_tier_b_repair/work/pdf_pages/` 下, 核正文节标题原文)
- 总体说明: 26 条全是 p.2 目录条目 (`§0 [TOC]`). 渲染页确认目录里 1.x/2.x/3.1/3.2/5.1/5.2 级用小型大写 (small caps), 文本层的全大写是字形产物, 正文标题为标题大小写 (如 p.5 `1.3 Relationship to Prior CDISC Models`). KB 标题大小写差异不算标题文字不同. 目录页码 KB 不承载, 按 TOC 规则只核节号 + 标题文字. 包内 KB 指针多处偏 (Q1 指到了 SDTMIG `chapters/ch01_introduction.md` 的 "Relationship to Prior CDISC Documents", Q3-Q8/Q10/Q19/Q21/Q22 指到正文交叉引用句而非标题), 以下依据栏均为自行定位的标题行.

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| Q1 | sv20_p0002_a005 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:10, 渲染 p.2; `knowledge_base/model/01_concepts_and_terms.md:30` `## 1.3 Relationship to Prior CDISC Models` | TOC→标题. 包内指针 (IG ch01 "…Prior CDISC Documents") 是别的文档, 不采用 |
| Q2 | sv20_p0002_a008 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:14; `model/01_concepts_and_terms.md:154` `## 2.1 Model Concepts and Terms – Variables` | TOC→标题 (en dash 一致) |
| Q3 | sv20_p0002_a009 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:15; `model/01_concepts_and_terms.md:193` `## 2.2 Table Structure` | TOC→标题. 包内指针 INDEX.md 不对 |
| Q4 | sv20_p0002_a012 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:19; `model/02_observation_classes.md:35` `## 3.1.1 The Interventions Observation Class` | TOC→标题 |
| Q5 | sv20_p0002_a013 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:20; `model/02_observation_classes.md:89` `## 3.1.2 The Events Observation Class` | TOC→标题 |
| Q6 | sv20_p0002_a014 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:21; `model/02_observation_classes.md:156` `## 3.1.3 The Findings Observation Class` | TOC→标题 |
| Q7 | sv20_p0002_a016 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:23; `model/02_observation_classes.md:279` `## 3.1.4 Identifiers for All Classes` | TOC→标题 |
| Q8 | sv20_p0002_a017 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:24; `model/02_observation_classes.md:308` `## 3.1.5 Timing Variables for All Classes` | TOC→标题 |
| Q9 | sv20_p0002_a018 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:25, 正文 sv20_p0040.txt:5; `model/03_special_purpose_domains.md:7` `### 3.2 Special-purpose Domains` | TOC→标题 (连字符一致; 另有 H1 文件标题 "Chapter 3.2: Special-purpose Domains") |
| Q10 | sv20_p0002_a019 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:26; `model/03_special_purpose_domains.md:11` `## 3.2.1 Demographics` | TOC→标题 |
| Q11 | sv20_p0002_a020 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:27; `model/03_special_purpose_domains.md:79` `## 3.2.2 Comments` | TOC→标题 |
| Q12 | sv20_p0002_a022 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:29; `model/03_special_purpose_domains.md:113` `### 3.2.3.1 Subject Elements` | TOC→标题 |
| Q13 | sv20_p0002_a023 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:30; `model/03_special_purpose_domains.md:143` `### 3.2.3.2 Subject Repro Stages` | TOC→标题 |
| Q14 | sv20_p0002_a024 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:31; `model/03_special_purpose_domains.md:166` `### 3.2.3.3 Subject Visits` | TOC→标题 |
| Q15 | sv20_p0002_a025 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:32; `model/03_special_purpose_domains.md:197` `### 3.2.3.4 Subject Disease Milestones` | TOC→标题 |
| Q16 | sv20_p0002_a026 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:34, 正文 sv20_p0050.txt:6; `model/04_associated_persons.md:7` `### 4 Associated Persons Data` | TOC→标题 |
| Q17 | sv20_p0002_a027 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:36; `model/05_study_level_data.md:5` `## 5 Study-level Data` | TOC→标题 |
| Q18 | sv20_p0002_a028 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:37; `model/05_study_level_data.md:11` `## 5.1 The Trial Design Model` | TOC→标题 |
| Q19 | sv20_p0002_a030 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:39 (包内写 38 行, 实为 39), 正文 sv20_p0051.txt:25; `model/05_study_level_data.md:29` `#### 5.1.1.1 Trial Elements (TE)` | TOC→标题; KB 在标题后追加域代码 "(TE)" (PDF 目录与正文都没有), 标题文字本身一致, 属附加非改义 |
| Q20 | sv20_p0002_a031 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:40, 正文 sv20_p0052.txt:20; `model/05_study_level_data.md:45` `#### 5.1.1.2 Trial Arms (TA)` | TOC→标题; KB 追加 "(TA)" |
| Q21 | sv20_p0002_a032 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:41, 正文 sv20_p0053.txt:21; `model/05_study_level_data.md:66` `### 5.1.2 Trial Sets (TX)` | TOC→标题; KB 追加 "(TX)" |
| Q22 | sv20_p0002_a034 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:43 (包内写 42 行, 实为 43), 正文 sv20_p0054.txt:10; `model/05_study_level_data.md:89` `#### 5.1.3.1 Trial Repro Stages (TT)` | TOC→标题; KB 追加 "(TT)" |
| Q23 | sv20_p0002_a035 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:44, 正文 sv20_p0054.txt:37; `model/05_study_level_data.md:109` `#### 5.1.3.2 Trial Repro Paths (TP)` | TOC→标题; KB 追加 "(TP)" |
| Q24 | sv20_p0002_a037 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:46, 正文 sv20_p0056.txt:5; `model/05_study_level_data.md:140` `#### 5.1.4.1 Trial Visits (TV)` | TOC→标题; KB 追加 "(TV)" |
| Q25 | sv20_p0002_a038 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:47, 正文 sv20_p0056.txt:40; `model/05_study_level_data.md:158` `#### 5.1.4.2 Trial Disease Assessments (TD)` | TOC→标题; KB 追加 "(TD)" |
| Q26 | sv20_p0002_a039 | Q9_SV20_EQUIV | EQUIVALENT | HOLDS (TOC) | sv20_p0002.txt:48, 正文 sv20_p0057.txt:54; `model/05_study_level_data.md:178` `#### 5.1.4.3 Trial Disease Milestones (TM)` | TOC→标题; KB 追加 "(TM)" |

## 计数

| 层 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE | 合计 | 其中 TOC |
|---|---|---|---|---|---|---|
| Q9_SV20_EQUIV (包 1) | 26 | 0 | 0 | 0 | 26 | 26 (全部计入 HOLDS) |

- 非 HOLDS 条目: 无.
- 备注 (不影响判定): Q19-Q26 共 8 条 KB 标题末尾追加了域代码 (TE/TA/TX/TT/TP/TV/TD/TM), PDF 目录与正文标题都没有; 节号与标题文字本身逐字一致, 按 "附加信息、无改义" 判 HOLDS. 若主控认为 "标题文字不同" 应从严 (任何附加都算不同), 这 8 条需复议.

## 样本外发现的 KB 内容问题

无 KB 内容问题. 仅样本包生成方面的观察 (非 KB): Q1 自动指针跨文档指到 SDTMIG `knowledge_base/chapters/ch01_introduction.md:28` (标题 "Relationship to Prior CDISC Documents"), 与 SDTM v2.0 的 §1.3 无关; Q19/Q22 包内 PDF 行号偏 1 行.
