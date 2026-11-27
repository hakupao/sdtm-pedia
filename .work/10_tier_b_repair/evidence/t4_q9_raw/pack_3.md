# T4.1 Q9 扩检 — 包 3 审查结果 (Q9_SV20_EQUIV, Q53-Q78, 26 条)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:01:50Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_q9_extension_v1.0.md` (五选一) + `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (背景 / 输出格式)
- 看过的渲染页 (`source/cdisc/SDTM_v2.0.pdf`, Read 带 pages): p46, p47, p52, p53
- 文本层: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0009.txt`, `sv20_p0046.txt`, `sv20_p0047.txt`, `sv20_p0052.txt`, `sv20_p0053.txt` (另引包内 p45 / p51 / p54 片段)
- 用过的命令:
  - `grep -n "named variables\|5 major roles\|..." knowledge_base/model/*.md`
  - `sed -n '108,175p' knowledge_base/model/03_special_purpose_domains.md`; `sed -n '1,100p' knowledge_base/model/05_study_level_data.md`
  - `sed -n ... .work/10_tier_b_repair/work/pdf_pages/sv20_p00{09,46,47,52,53}.txt`
  - `grep -n "^| [0-9]* | (STUDYID|...) |" knowledge_base/model/05_study_level_data.md`; `grep -n "^| # |" knowledge_base/model/03_special_purpose_domains.md`
  - `grep -c "sv20_p005[23]\|sv20_p004[67]\|sv20_p0009" .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` → 0 (本包无登记笔误)
- 定位说明: 包里 Q53-Q57 的 KB 指针 (`chapters/ch02_fundamentals.md`, SDTMIG 内容) 位置不对; SDTM v2.0 §2.1 在 `knowledge_base/model/01_concepts_and_terms.md:154-168`, 已按此核. 表行类的 KB 指针 (06 / 02 / ch04) 也都不是本表, 本表在 `knowledge_base/model/05_study_level_data.md` (TA: 53-64, TX: 72-81) 与 `03_special_purpose_domains.md` (SE 表头 127, SJ 表头 153).

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| Q53 | `sv20_p0009_a004` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:10-11`; `model/01_concepts_and_terms.md:160` | 实为逐字 (KB 仅 role 加粗). 节 2.1 Variables 位置正确 |
| Q54 | `sv20_p0009_a007` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:19`; `model/01_concepts_and_terms.md:162` | 实为逐字 |
| Q55 | `sv20_p0009_a008` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:20-21`; `model/01_concepts_and_terms.md:164` | 实为逐字 (加粗) |
| Q56 | `sv20_p0009_a011` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:24-25`; `model/01_concepts_and_terms.md:167` | 实为逐字 (含 "; and") |
| Q57 | `sv20_p0009_a012` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0009.txt:26-27`; `model/01_concepts_and_terms.md:168` | 实为逐字 ("Trial Design model." 一致) |
| Q58 | `sv20_p0045_a015` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0045.txt:44-45`; `model/03_special_purpose_domains.md:115` | 实为逐字, §3.2.3.1 下 |
| Q59 | `sv20_p0046_a002` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p46 SE 表头; `model/03_special_purpose_domains.md:127` | PDF 表头 12 列; KB 表头 `# / Variable / Label / Type / Role / Notes`. Variable Name/Label→Variable/Label 等价; PDF 的 Format / Variable(s) Qualified / Usage Restrictions / Variable C-code / Definition / Examples 六列 KB 本表没有 (Variable(s) Qualified 以 Role 括号形式部分折入; KB 的 Notes 列按 KB note 自述为 KB-written 混合列, 非 PDF Notes 列). 表头信息不等价, 属 R1 精简表 |
| Q60 | `sv20_p0046_a019` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0046.txt:54-56`; `model/03_special_purpose_domains.md:145` | 实为逐字, §3.2.3.2 下 |
| Q61 | `sv20_p0047_a002` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p47 SJ 表头; `model/03_special_purpose_domains.md:153` | 同 Q59: KB 表头只有 `# / Variable / Label / Type / Role / Notes`, 缺 Format / Variable(s) Qualified / Usage Restrictions / Variable C-code / Definition / Examples (KB Notes 列按 KB note 是 DOMAIN 浓缩 Notes + 其余格引 Usage Restrictions 的混合列) |
| Q62 | `sv20_p0051_a004` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0051.txt:10`; `model/05_study_level_data.md:13` | 实为逐字, §5.1 下 |
| Q63 | `sv20_p0051_a011` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0051.txt:18`; `model/05_study_level_data.md:20` | 实为逐字 |
| Q64 | `sv20_p0051_a015` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0051.txt:24`; `model/05_study_level_data.md:25-27` | 实为逐字, 在 `### 5.1.1 Trial Arms and Trial Elements` 下 (包指针 `domains/TE/assumptions.md` 是 SDTMIG 别处文字, 不采用) |
| Q65 | `sv20_p0052_a006` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0052.txt:21`; `model/05_study_level_data.md:47` | 实为逐字, §5.1.1.2 下 |
| Q66 | `sv20_p0052_a012` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p52 TA 行 1; `model/05_study_level_data.md:55` | 精简列一致 (1 / STUDYID / Study Identifier / Char / Identifier). PDF 非空而 KB 本表无列: Variable C-code `C83082`; Definition "A sequence of characters used by the sponsor to uniquely identify the study." |
| Q67 | `sv20_p0052_a013` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p52 TA 行 2; `model/05_study_level_data.md:56` | 精简列一致 (2 / DOMAIN / Domain Abbreviation / Char / Identifier). PDF 非空 KB 无: C-code `C49558`; Definition "An abbreviation for a collection of observations, with a topic-specific commonality."; Notes "2-character abbreviation, which must be "TA"." (KB TA 表无 Notes 列) |
| Q68 | `sv20_p0052_a014` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p52 TA 行 3; `model/05_study_level_data.md:57` | 精简列一致 (3 / ARMCD / Planned Arm Code / Char / Topic). PDF 非空 KB 无: C-code `C83216`; Definition "A short sequence of characters that represents the planned arm to which the subject was assigned."; Notes "ARMCD is limited to 20 characters and does not have special character restrictions." (包指针 `ch04_general_assumptions.md:254` 是 SDTMIG 另一处近似文字, 位置不对) |
| Q69 | `sv20_p0052_a016` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p52 TA 行 5; `model/05_study_level_data.md:59` | 精简列一致 (5 / TAETORD / Planned Order of Element within Arm / Num / Timing). PDF 非空 KB 无: C-code `C83438`; Definition "An assigned numeric identifier that gives the planned order of the element within the trial arm of the study." |
| Q70 | `sv20_p0052_a017` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p52 TA 行 6; `model/05_study_level_data.md:60` | 精简列一致 (6 / ETCD / Element Code / Char / Record Qualifier). PDF Notes 非空 KB 无: "ETCD (the companion to ELEMENT) is limited to 8 characters ... not expected that ETCD will need to serve as a variable name." (C-code / Definition 空). 包指针 `ch04_general_assumptions.md:253` 为 SDTMIG 合并 ETCD+TSPARMCD 的改写句, 位置不对 |
| Q71 | `sv20_p0053_a004` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TA 行 10; `model/05_study_level_data.md:64` | 精简列一致 (10 / EPOCH / Epoch / Char / Timing). PDF 非空 KB 无: C-code `C71738`; Definition "A time period defined in the protocol with a study-specific purpose."; Notes "The epoch associated with the value in ELEMENT and the value in ARMCD." (包指针 02 文件 EPOCH 行是另一张表) |
| Q72 | `sv20_p0053_a011` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TX 行 1; `model/05_study_level_data.md:74` | 精简列一致. PDF 非空 KB 无: C-code `C83082`; Definition "A sequence of characters used by the sponsor to uniquely identify the study." |
| Q73 | `sv20_p0053_a012` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TX 行 2; `model/05_study_level_data.md:75` | 精简列一致. PDF 非空 KB 无: C-code `C49558`; Definition (同 Q67); Notes "2-character abbreviation, which must be "TX"." |
| Q74 | `sv20_p0053_a014` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TX 行 4; `model/05_study_level_data.md:77` | 精简列一致 (4 / SET / Set Description / Char / Synonym Qualifier; Variable(s) Qualified `SETCD` 以 Role 括号 "(SETCD)" 承载). PDF Notes 非空 KB 无: "Long description of a specific trial set, as defined by the sponsor." |
| Q75 | `sv20_p0053_a015` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TX 行 5; `model/05_study_level_data.md:78` | 精简列一致 (5 / TXSEQ / Sequence Number / Num / Identifier). PDF Notes 非空 KB 无: "Unique number for this record within this dataset." |
| Q76 | `sv20_p0053_a016` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TX 行 6; `model/05_study_level_data.md:79` | 精简列一致 (6 / TXPARMCD / Trial Set Parameter Short Name / Char / Topic). PDF Notes 非空 KB 无: "Short character value for the trial set parameter described in TXPARM. Maximum 8 characters." |
| Q77 | `sv20_p0053_a018` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p53 TX 行 8; `model/05_study_level_data.md:81` | 精简列一致 (8 / TXVAL / Trial Set Parameter Value / Char / Result Qualifier). PDF 非空 KB 无: Notes "Value of the trial set parameter. Some parameters may be subject to controlled terminology."; Examples ""Fed ad libitum" or "Restricted Feeding" when TXPARM is "FEEDREG"". 附: 原子 verbatim 把 Notes 文字放进了 Definition 格 (渲染页 Definition 为空, 文字在 Notes 列) — 原子列归属抽错, 不影响本判定 |
| Q78 | `sv20_p0054_a003` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | `sv20_p0054.txt:7`; `model/05_study_level_data.md:87` | 实为逐字, §5.1.3 下 |

## 计数

| 判定 | 条数 | 编号 |
|---|---|---|
| HOLDS | 12 | Q53-Q58, Q60, Q62-Q65, Q78 (全部 "实为逐字") |
| NOT_HOLD_R1 | 14 | 表头 Q59, Q61; 表行 Q66-Q77 |
| NOT_HOLD | 0 | — |
| UNVERIFIABLE | 0 | — |
| TOC (另报) | 0 | 本包无 `§0 [TOC]` 原子 |

按层: 全部 26 条属 `Q9_SV20_EQUIV`, 计数同上.

## 样本外发现的 KB 内容问题

无 (仅记一条非 KB 的抽取物观察: `sv20_p0053_a018` 原子列归属错位, 见 Q77 说明; 另包内 Q53-Q57 / Q64 / Q66-Q77 的 KB 自动指针多指向 SDTMIG 章节或其它表, 若后续脚本依赖这些指针需注意).
