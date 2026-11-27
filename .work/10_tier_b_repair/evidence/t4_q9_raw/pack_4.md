# T4.1 Q9 扩检 — 包 4 结果 (Q9_SV20_EQUIV, Q79-Q104, 26 条)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:01:14Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `.work/10_tier_b_repair/subagent_prompts/t4/t4_q9_extension_v1.0.md` (五选一), 背景/输出沿用 `t4_supp_fullcheck_v1.0.md`
- 看过的渲染页: `source/cdisc/SDTM_v2.0.pdf` p55, p56, p57, p58 (Read pages=55-58); p54 只看文本层 (句子原子, 无列归属问题)
- 用过的命令:
  - `cat .work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt ... sv20_p0058.txt`; `sed -n 30,45p .../sv20_p0054.txt`
  - Read `knowledge_base/model/05_study_level_data.md` 100-314 行
  - `grep -c "sv20_p005[4-8]" .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` → 0 (本包无登记笔误)
  - `grep -rn -e "Should be zero or 1" -e "repro path to branch" -e "only once (\"N\")" -e "1TEST" -e "rather than TI" -e "HYPOGLYCEMIC" -e "in relation to the sequence of elements" -e "ordinal sequencing of the planned" knowledge_base/model/` → 仅 06 文件 1 处无关命中 (QNAM 行), 即这些 Notes / Examples 在 KB model 内任何位置都没有

列归属 (渲染页核定): TP / TV / TD / TM / TI 五张表里, 无 C-code 的行其长文本全部落在 **Notes** 列 (Definition 列空); 有 C-code 的行 (RPATHCD / VISITDY / ARMCD) Definition 与 Notes 都有内容. TD 第 6-8 行 Format = `ISO 8601 duration`. KB 这五张表: TP 为 5 基列 + Usage Restrictions; TV / TD / TM / TI 为 5 基列 (# / Variable / Label / Type / Role, Variable(s) Qualified 并进 Role 括号). 五张表 KB 均无 Format / C-code / Definition / Notes / Examples 列, 表后也无承载这些内容的文字.

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| Q79 | `sv20_p0054_a020` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF `sv20_p0054.txt`:40-41; KB `knowledge_base/model/05_study_level_data.md`:113 (§5.1.3.2 TP) | 实为逐字 |
| Q80 | `sv20_p0055_a005` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | 渲染页 p55 TP 行 3; KB 05:123 | 精简列一致 (3/RPATHCD/Planned Repro Path Code/Char/Topic/Not in human clinical trials); KB 缺 Variable C-code `C170503`、Definition "A short sequence of characters that represents the planned reproductive path to which the subject was assigned."、Notes "Limited to 20 characters. Should be populated in Demographics when repro paths have been defined in this domain." |
| Q81 | `sv20_p0055_a006` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 4; KB 05:124 | 精简列一致 (Synonym Qualifier + RPATHCD 并为 "Synonym Qualifier (RPATHCD)", Usage Restrictions 一致); KB 缺 Notes "Name of the planned repro path." |
| Q82 | `sv20_p0055_a007` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 5; KB 05:125 | 精简列一致; KB 缺 Notes "Number that gives the planned order of the repro stage within the repro path." |
| Q83 | `sv20_p0055_a008` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 6; KB 05:126 | 精简列一致; KB 缺 Notes "Short name of the repro stage used for programming and sorting. Maximum 8 characters. The values of RSTGCD used in the Trial Paths dataset must match values for the same repro stage in the Trial Stages dataset." |
| Q84 | `sv20_p0055_a009` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 7; KB 05:127 | 精简列一致 (Synonym Qualifier (RSTGCD)); KB 缺 Notes "The name of the repro stage." |
| Q85 | `sv20_p0055_a010` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 8; KB 05:128 | 精简列一致; KB 缺 Notes "Conditions subjects meet, occurring at the end of a repro stage, which cause a repro path to branch off from another repro path." |
| Q86 | `sv20_p0055_a011` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 9; KB 05:129 | 精简列一致; KB 缺 Notes "Name of the reproductive phase with which this repro stage of the repro path is associated." |
| Q87 | `sv20_p0055_a012` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p55 TP 行 10; KB 05:130 | 精简列一致; KB 缺 Notes "Sponsor protocol-defined first day of repro phase. Should be zero or 1." |
| Q88 | `sv20_p0056_a002` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF `sv20_p0056.txt`:6; KB 05:142 (§5.1.4.1 TV) | 实为逐字 (原子 = 段首句, KB 段落逐字含该句) |
| Q89 | `sv20_p0056_a012` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p56 TV 行 5; KB 05:152 | 精简列一致 (5/VISITDY/Planned Study Day of Visit/Num/Timing); KB 缺 C-code `C171011`、Definition "The planned study day of a clinical encounter relative to the sponsor-defined reference start date."、Notes "Due to its sequential nature can be used for sorting." |
| Q90 | `sv20_p0056_a013` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p56 TV 行 6; KB 05:153 | 精简列一致 (Record Qualifier); KB 缺 C-code `C83216`、Definition "A short sequence of characters that represents the planned arm to which the subject was assigned."、Notes "ARMCD is limited to 20 characters ... then ARMCD should be null." |
| Q91 | `sv20_p0056_a015` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p56 TV 行 8; KB 05:155 (包指针 43-47 指向 TE/TA, 偏) | 精简列一致; KB 缺 Notes "Rule describing when the visit starts, in relation to the sequence of elements." |
| Q92 | `sv20_p0056_a016` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p56 TV 行 9; KB 05:156 (包指针 42-47 偏) | 精简列一致; KB 缺 Notes "Rule describing when the visit ends, in relation to the sequence of elements." |
| Q93 | `sv20_p0056_a018` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF `sv20_p0056.txt`:41-42; KB 05:160 (§5.1.4.2 TD) | 实为逐字 |
| Q94 | `sv20_p0057_a005` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p57 TD 行 3; KB 05:170 | 精简列一致; KB 缺 Notes "A number given to ensure ordinal sequencing of the planned assessment schedules within a trial." |
| Q95 | `sv20_p0057_a008` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p57 TD 行 6; KB 05:173 | 精简列一致; KB 缺 Format "ISO 8601 duration"、Notes "The planned interval between disease assessments." |
| Q96 | `sv20_p0057_a009` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p57 TD 行 7; KB 05:174 | 精简列一致; KB 缺 Format "ISO 8601 duration"、Notes "The lower limit of the allowed range for the planned interval between disease assessments." |
| Q97 | `sv20_p0057_a010` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p57 TD 行 8; KB 05:175 | 精简列一致; KB 缺 Format "ISO 8601 duration"、Notes "The upper limit of the allowed range for the planned interval between disease assessments." |
| Q98 | `sv20_p0057_a013` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF `sv20_p0057.txt`:55-56; KB 05:180 (§5.1.4.3 TM) | 实为逐字 |
| Q99 | `sv20_p0058_a005` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p58 TM 行 3; KB 05:188 | 精简列一致; KB 缺 Notes "The type of disease milestone."、Examples "\"HYPOGLYCEMIC EVENT\"" |
| Q100 | `sv20_p0058_a006` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p58 TM 行 4; KB 05:189 | 精简列一致 (Variable Qualifier (MIDSTYPE)); KB 缺 Notes "Definition of the disease milestone." |
| Q101 | `sv20_p0058_a007` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p58 TM 行 5; KB 05:190 | 精简列一致; KB 缺 Notes "Indicates whether this is a disease milestone that can occur only once (\"N\") or one that can occur multiple times (\"Y\")." |
| Q102 | `sv20_p0058_a009` | Q9_SV20_EQUIV | EQUIVALENT | HOLDS | PDF `sv20_p0058.txt`:26; KB 05:194 (§5.1.5 TI) | 实为逐字 (原子 = 段首句) |
| Q103 | `sv20_p0058_a015` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p58 TI 行 3; KB 05:202 | 精简列一致; KB 缺 Notes "Short name IETEST. It can be used as a column name ... The prefix \"IE\" is used to ensure consistency with the IE domain." (含 8 字符上限 / 不以数字开头 / 字符集限制) |
| Q104 | `sv20_p0058_a017` | Q9_SV20_EQUIV | EQUIVALENT | NOT_HOLD_R1 | p58 TI 行 5; KB 05:204 | 精简列一致 (Grouping Qualifier); KB 缺 Notes "Used for categorization of the inclusion or exclusion criterion. The prefix \"IE\" (rather than TI) is used to ensure consistency with the IE domain."、Examples "\"INCLUSION\", \"EXCLUSION\"" |

## 计数

| 判定 | 条数 |
|---|---|
| HOLDS | 5 (Q79, Q88, Q93, Q98, Q102; 全部为 SENTENCE, 实为逐字) |
| NOT_HOLD_R1 | 21 (Q80-Q87, Q89-Q92, Q94-Q97, Q99-Q101, Q103, Q104; 全部为 TABLE_ROW) |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |
| TOC (另报) | 0 |

合计 26. 21 条 TABLE_ROW 的精简列 (# / Variable / Label / Type / Role 含 Variable(s) Qualified, TP 另含 Usage Restrictions) 逐格比对均与 PDF 一致, 无值错; 不成立的原因仅为 KB 未收 Format / C-code / Definition / Notes / Examples 列内容 (R1 有意不收类).

## 样本外发现的 KB 内容问题

无 (KB 内容问题层面). 附注: 包内 Q91 / Q92 的 "KB 现文" 自动指针指向 §5.1.1.1/§5.1.1.2 (TE/TA, 05:42-47), 是定位偏差, 正确位置为 05:155-156; 不影响判定.
