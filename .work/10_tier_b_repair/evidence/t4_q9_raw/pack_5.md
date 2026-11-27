# T4.1 Q9 扩检 — 包 5 审查结果 (Q9_SV20_EQUIV, Q105-Q127, 23 条)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:01:53Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_q9_extension_v1.0.md` (五选一) + `t4_supp_fullcheck_v1.0.md` (背景 / 输出格式)
- 看过的渲染页 (`source/cdisc/SDTM_v2.0.pdf`, Read 带 pages): 58, 59, 60, 61, 65, 68, 69
- 文本层: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` / `p0059` / `p0060` / `p0065` / `p0069` / `p0050` (核 §4 AP 表 SREL 行)
- KB: `knowledge_base/model/05_study_level_data.md` (§5.1.5 TI 表 198-207; §5.1.6 TS 211-229; §5.2 254-259), `knowledge_base/model/06_relationship_datasets.md` (§6.1 RELREC 表 35-46; §6.6 APRELSUB 表 146-154), `knowledge_base/model/04_associated_persons.md` (§4 AP 变量表 37-42)
- 命令: `grep -n "6.6\|APRELSUB\|RSUBJID\|SREL\b" knowledge_base/model/06_relationship_datasets.md`; `grep -rn "IESCAT\|TIRL\|TIVERS\|TSGRPID\|TSPARMCD" knowledge_base/model/`; `cat .work/10_tier_b_repair/work/pdf_pages/sv20_p00{58,59,60,65,69}.txt`; `grep -n -A10 "SREL" .work/10_tier_b_repair/work/pdf_pages/sv20_p0050.txt`; `grep -n "sv20_p00\(58\|59\|60\|61\|65\|69\)" .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (无命中)
- PDF 笔误登记: 本包涉及页 (58/59/60/61/65/69) 无登记条目.

KB 表结构要点 (渲染页核过列归属):
- §5.1.5 TI 表 (KB 05:198-207): 只有 `# / Variable / Label / Type / Role` 五列. PDF 行 6-8 的 Notes (及 IESCAT 的 Examples) 都非空.
- §5.1.6 TS 表 (KB 05:217-229): 五列 + Usage Restrictions (KB note 05:215 自述只加了这一列). PDF 行 3-11 的 Notes 全非空; 5/7/10 行 Examples 非空.
- §6.1 RELREC 表 (KB 06:35-46): 五列 + Notes. PDF Examples 列只有 IDVAR 行非空 ("--SEQ and --GRPID").
- §6.6 APRELSUB 表 (KB 06:146-154): 只有五列. PDF 行 2-5 Notes 非空. 同名变量的 Notes 文字在 KB §4 AP 变量表 (04:37-42) 里有, 但那是另一张表 (PDF p50), 且 SREL 行文字与 §6.6 不同 (见 Q127).

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| Q105 | `sv20_p0058_a018` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p58 渲染页 + p59 顶 (sv20_p0058.txt:54-56, sv20_p0059.txt:6-7); KB 05:205 | 五列 (6/IESCAT/Inclusion/Exclusion Subcategory/Char/Grouping Qualifier) 一致. PDF Notes "A further categorization of the exception criterion. Can be used to distinguish criteria for a substudy or to categorize major or minor exceptions. The prefix "IE" (rather than TI) is used to ensure consistency with the IE domain." 与 Examples `"MAJOR", "MINOR"` 非空, KB 本表无这两列, 05 文件内 grep 无其它承载 |
| Q106 | `sv20_p0059_a001` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 渲染页 (sv20_p0059.txt:8-9); KB 05:206 | 五列 (7/TIRL/Inclusion/Exclusion Criterion Rule/Char/Rule) 一致. PDF Notes "Rule that expresses the criterion in computer-executable form." 非空, KB 本表未承载 |
| Q107 | `sv20_p0059_a002` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:10-11); KB 05:207 | 五列 (8/TIVERS/Protocol Criteria Versions/Char/Record Qualifier) 一致. PDF Notes "The number of this version of the inclusion/exclusion criteria. May be omitted if there is only 1 version." 非空, KB 未承载 |
| Q108 | `sv20_p0059_a004` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p59 (sv20_p0059.txt:15); KB 05:211 (§5.1.6 首段) | 实为逐字; 位置正确 (§5.1.6) |
| Q109 | `sv20_p0059_a005` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p59 (sv20_p0059.txt:15-16); KB 05:211 | 实为逐字 (含 "(e.g., trial phase, protocol title, design objectives)"); 位置正确 |
| Q110 | `sv20_p0059_a010` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:29-30); KB 05:221 | 五列 (3/TSSEQ/Sequence Number/Num/Identifier) + Usage Restrictions 空 一致. PDF Notes "Sequence number to ensure uniqueness within the dataset." 非空, KB 本表无 Notes 列 |
| Q111 | `sv20_p0059_a011` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:31); KB 05:222 | 五列 (4/TSGRPID/Group ID/Char/Identifier) 一致. PDF Notes "Used to tie together a group of related records." 未承载 (包里指针 TS/assumptions.md:41 是 SDTMIG 域文件, 不同文字、不同来源, 不算承载) |
| Q112 | `sv20_p0059_a012` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:32-37); KB 05:223 | 五列 (5/TSPARMCD/Trial Summary Parameter Short Name/Char/Topic) 一致. PDF Notes (TSPARMCD 限 8 字符、无特殊字符限制、不需作变量名) 与 Examples `"AGEMIN", "AGEMAX"` 未承载 |
| Q113 | `sv20_p0059_a014` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:42-45); KB 05:225 | 五列 (7/TSVAL/Parameter Value/Char/Result Qualifier) 一致. PDF Notes "Value of TSPARM. If TSVAL is null, a value is required for TSVALNF. Text over 200 characters can be added to additional columns TSVAL1-TSVALn." 与 Examples `"ASTHMA" when TSPARM value is "Trial Indications"` 未承载 |
| Q114 | `sv20_p0059_a015` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:46-48); KB 05:226 | 五列 (8/TSVALNF/Parameter Null Flavor/Char/Result Qualifier) 一致. PDF Notes "Null flavor for the value of TSVAL describing the reason the value is null, to be populated only if TSVAL is null." 未承载 |
| Q115 | `sv20_p0059_a016` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:49-51); KB 05:227 | 五列 + Usage Restrictions "Not in nonclinical trials" 一致. PDF Notes "Code of the term in TSVAL from the reference terminology cited in TSVCDREF." 未承载 |
| Q116 | `sv20_p0059_a017` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p59 (sv20_p0059.txt:52-54); KB 05:228 | 五列 + Usage Restrictions 一致. PDF Notes "The name of the reference terminology or standard format from which TSVALCD is taken." 与 Examples `"CDISC CT", "SNOMED", "ISO 8601"` 未承载 |
| Q117 | `sv20_p0060_a001` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p60 渲染页 (sv20_p0060.txt:6-8); KB 05:229 | 五列 + Usage Restrictions 一致. PDF Notes "The version number of the reference terminology cited in TSVCDREF, if applicable." 未承载 (原子 verbatim 列位多了空格, 不影响) |
| Q118 | `sv20_p0061_a002` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p61 渲染页 (sv20_p0061.txt:6); KB 05:256 (§5.2) | 实为逐字; 位置正确 |
| Q119 | `sv20_p0061_a003` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p61 (sv20_p0061.txt:6); KB 05:256 | 实为逐字 |
| Q120 | `sv20_p0061_a004` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p61 (sv20_p0061.txt:7); KB 05:258 | 实为逐字 (列表项) |
| Q121 | `sv20_p0061_a005` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p61 (sv20_p0061.txt:8); KB 05:259 | 实为逐字 (列表项) |
| Q122 | `sv20_p0065_a003` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p65 渲染页 (sv20_p0065.txt:15-16); KB 06:43 | 五列 + Notes 逐字一致. 但 PDF Examples 列 "--SEQ and --GRPID" 非空 (渲染页确认在 Examples 列), KB RELREC 表无 Examples 列, 未承载 |
| Q123 | `sv20_p0065_a004` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p65 (sv20_p0065.txt:17-19); KB 06:44 | 五列 + Notes 实为逐字; 其余 PDF 列 (Format/Qualified/Usage/C-code/Definition/Examples) 渲染页确认全空 |
| Q124 | `sv20_p0065_a005` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p65 (sv20_p0065.txt:20-23); KB 06:45 | 同上, 实为逐字; 其余列全空 |
| Q125 | `sv20_p0065_a006` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF p65 (sv20_p0065.txt:24-30); KB 06:46 | 同上, 实为逐字; 其余列全空 |
| Q126 | `sv20_p0069_a002` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p69 渲染页 (sv20_p0069.txt:11-15); KB 06:152 (§6.6 APRELSUB 表) | 五列 (3/RSUBJID/Related Subject or Pool Identifier/Char/Identifier) 一致. PDF Notes (RSUBJID 定义 + "will be null for ... not to any study subjects") 非空, §6.6 表无 Notes 列. 同文字只在 KB §4 AP 表 04:40 (另一张表, 对应 PDF p50, 且 # 为 2 不是 3) → 位置不对, 属 R1 类. 与补检 NOT_HOLD 的 `sv20_p0069_a001/a003` 同一机制 |
| Q127 | `sv20_p0069_a004` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | PDF p69 (sv20_p0069.txt:18-26); KB 06:154 | 五列 (5/SREL/Subject, Device, or Study Relationship/Char/Record Qualifier) 一致. PDF Notes 三段非空, §6.6 表未承载. 包里指针 04:42 是 §4 AP 表 (PDF p50), 那里 # = 4、Role = Identifier、第二句为 "...to the device identified in RDEVID"; 而 §6.6 PDF 原文是 "...to the subject or pool identified in RDEVID" — 文字也不同, 更不能当作承载 |

## 计数

| 判定 | 条数 | 编号 |
|---|---|---|
| HOLDS | 9 | Q108, Q109, Q118, Q119, Q120, Q121, Q123, Q124, Q125 (全部实为逐字) |
| NOT_HOLD_R1 | 14 | Q105, Q106, Q107, Q110, Q111, Q112, Q113, Q114, Q115, Q116, Q117, Q122, Q126, Q127 |
| NOT_HOLD | 0 | — |
| UNVERIFIABLE | 0 | — |
| 合计 | 23 | |
| 其中 TOC | 0 | — |

按层: 全部 23 条均为 `Q9_SV20_EQUIV`, 计数同上.

## 样本外发现的 KB 内容问题

无内容错误. 观察 (不算样本判定, 不修):
1. §6.6 APRELSUB SREL 的 PDF Notes (p69) 第二句写 "to the subject or pool identified in RDEVID", 而 §4 AP 表 (p50) 同句写 "to the device identified in RDEVID"; KB 04:42 按 p50 写 "device", 与 p50 一致, 无误. 两处 PDF 文字不一致疑为 PDF p69 的复制笔误 (RDEVID 指设备), 现未在 `t2_pdf_typo_registry.jsonl` 登记; 若后续给 §6.6 表补 Notes, 需先定此处口径.
2. 包里 Q111-Q114 的 KB 指针指向 `knowledge_base/domains/TS/assumptions.md` (SDTMIG 域假设), 是取包脚本的 fuzzy locate 跨文档误配 (score ≤ 0.714), 不能作为 SDTM v2.0 §5.1.6 变量表的承载. 旧匹配器当年为何给这些行 EQUIVALENT, 本审查无证据, 不推断.
