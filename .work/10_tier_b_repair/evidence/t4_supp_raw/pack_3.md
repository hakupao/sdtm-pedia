# T4.1 补检 pack 3/8 结果 — TRIAGE_ATOM_ERR (全局 #59-83, 25 条, 全检)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读; brief `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`
- 时间: 2026-11-27T04:52:05Z (`date -u` 开工时取)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p69, p70, p78, p112, p116; 放大: p70 (300dpi, CRACE01-04 红色注释框), p116 (250dpi, ec.xpt 行 5-13 的 ECTRT / EPOCH 换行格)
- 文本层: `ig34_p0056.txt` `p0057` `p0063` `p0067` `p0068` `p0069` `p0070` `p0077` `p0078` `p0080` `p0101` `p0112` `p0116`
- 用过的命令: `sed -n` 读文本层页与 KB 段; `grep -n` 查 KB (`ch04_general_assumptions.md`, `DM/{spec,assumptions,examples}.md`, `SE/spec.md`, `CM/assumptions.md`, `EX/examples.md`); python 读 `pdf_atoms.jsonl` 同页原子序列 (判定原子对应哪张表/哪一行) 与 `triage_merged.json`; python 规整空白后比对 PDF 段与 KB 行 (#62 RFICDTC 段、#78 CMSTRTPT 段, 均 True); `grep` `t2_pdf_typo_registry.jsonl`; `pdftoppm -r 300/250 -x -y -W -H` 裁切放大
- 原子 ≠ PDF 一律以文本层 + 渲染页为准; KB = PDF 一律逐格 / 逐字核.

## 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| 59 | ig34_p0056_a001 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0056.txt:32-36`; `ch04_general_assumptions.md:1477` | ① 原子 "separate additional 200 characters of text in supplemental qualifiers" ≠ PDF "each additional 200 characters of text should be stored as a record in the SUPP-- dataset". ② KB 表格首格逐字一致 (pack 指针 1361 偏, 实际在 1477) |
| 60 | ig34_p0057_a002 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0056.txt:49-51` (+ p57:1); `ch04_general_assumptions.md:1485,1489` | ① 原子 "See Section 8.4.1, Supplemental Qualifiers—SUPP-- Datasets for additional detail." PDF 无此句; 原文是 QEVAL 句内括注 "(see Section 8.4.1, Supplemental Qualifiers – SUPP-- Datasets)", 无 "for additional detail". ② KB:1485 逐字承载该句及括注; 相邻 "See Section 8.4, Relating Non-standard Variable Values to a Parent Domain." 亦在 KB:1489 |
| 61 | ig34_p0063_a017 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0063.txt:40-41`; `DM/spec.md:176-183` | ① 原子 Type "Num", PDF "Char". ② KB 逐格: AGEU / Age Units / Char / (AGEU) / Variable Qualifier / Units associated with AGE. / Exp 全一致 (KB 另附 C66781 代码, 不改值) |
| 62 | ig34_p0067_a014 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0067.txt:21-31`; `DM/assumptions.md:50` | ① 原子 "RFICIDITC" 且句子截断, PDF "RFICDTC ... used: They represent ...". ② KB:50 与 PDF d 项全段规整空白后逐字相等 (脚本比对 True) |
| 63 | ig34_p0068_a017 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0068.txt:36`; `DM/examples.md:32` | ① 原子末列 "ACTARMNRS" + 前缀 "ARMCD Example table with columns", PDF 末列 "ACTARMUD". ② KB 表头 10 列逐格一致; 同表 5 行亦逐格一致 (KB:33-37) |
| 64 | ig34_p0069_a013 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0069.txt:32` + 渲染 p69; `DM/examples.md:76` | ① 原子末列 "ACTARMNRS", PDF "ACTARMUD". ② KB 表头逐格一致; 3 行亦一致 (KB:78-80) |
| 65 | ig34_p0069_a023 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0069.txt:8,40` + 渲染 p69; `DM/examples.md:54,94` | ① 原子 "1 \| ABC \| ... \| 2006-01-07 \| 2006-01-12" 把 Ex2 (ABC) 与 Ex3 (DEF) 混在一起: Ex2 Row1 日期为 2006-06-01/2006-06-07, Ex3 Row1 STUDYID 为 DEF; 与两者都不符. ② KB Ex2 se 全 11 行、Ex3 se 全 8 行逐格对 PDF 一致 |
| 66 | ig34_p0069_a024 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 同上 (`p0069.txt:9,41`); `DM/examples.md:55,95` | ① 原子 "ABC 001 2 DBA Treatment A 2006-01-12 2006-06-21": Ex2 Row2 为 RI/Run-In/06-07~06-21, Ex3 Row2 为 DEF/…/01-12~04-10; 两者都不符. ② KB 两表对应行一致 |
| 67 | ig34_p0069_a025 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `p0069.txt:10,42`; `DM/examples.md:56,96` | ① 原子 ETCD "OA" + ELEMENT "Drug A": Ex2 Row3 ETCD 为 "A"; Ex3 Row3 为 DEF/OA/Open Drug A/04-10. 不符. ② KB 一致 |
| 68 | ig34_p0069_a027 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `p0069.txt:12,44`; `DM/examples.md:58,98` | ① 原子 "ABC 002 2 DBA Treatment A 05-10 05-24": Ex2 Row5 为 RI/Run-In; Ex3 Row5 为 DEF/02-10~03-24. 不符. ② KB 一致 |
| 69 | ig34_p0069_a029 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `p0069.txt:14`; `DM/examples.md:60` | ① 原子 SESTDTC "2006-05-27", PDF Ex2 Row7 "2006-06-27". ② KB:60 "2006-06-27 \| 2006-06-30" 一致 |
| 70 | ig34_p0069_a030 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `p0069.txt:15-16`; `DM/examples.md:61-62` | ① 原子 Row8 = "004 2 RI Run-in 05-21 05-26"; PDF Row8 = "004 1 SCRN Screen 05-14 05-21" (原子内容是 Row9 且 "Run-in" 大小写也错, PDF "Run-In"). ② KB Row8/Row9 一致 |
| 71 | ig34_p0069_a031 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `p0069.txt:16`; `DM/examples.md:62` | ① 原子 SESTDTC "2006-05-14" + "Run-in"; PDF Row9 "Run-In 2006-05-21 2006-05-26". ② KB 一致 |
| 72 | ig34_p0069_a032 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `p0069.txt:17`; `DM/examples.md:63` | ① 原子 Row10 "004 1 RI Run-in 05-14 05-26"; PDF Row10 "005 1 SCRN Screen 2006-05-14 2006-05-21". ② KB 一致 |
| 73 | ig34_p0070_a022 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p70 + 300dpi 放大 (CRACE01-CRACE04 红框); `DM/examples.md:188` (另 Mermaid :134, 文字 :168) | ① 原子 "SUPPQUAL where SUPPQUAL.QNAM = "<RACEC" and SUPPQUAL.QLABEL is the choice value" ≠ PDF 红框 "For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value." ② KB:188 映射列逐字一致 (该注释在 PDF 是图内文字, 文本层抽不出, 以渲染页为准) |
| 74 | ig34_p0077_a015 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0077.txt:31-35`, `ig34_p0078.txt:4-8` + 渲染 p78; `DM/examples.md:356-360,372-376` | ① 原子 suppdm 表头 "DOMAIN" (PDF "RDOMAIN") 且漏 "QVAL"; 且 p77 该位置实际是 dm.xpt (Row/STUDYID/DOMAIN/USUBJID/SUBJID/RACE), 不是 suppdm. 与哪张都不符. ② KB p77 dm.xpt 表头+3 行、p78 suppdm 表头 11 列+3 行均逐格一致 |
| 75 | ig34_p0078_a007 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0078.txt:5` + 渲染 p78; `DM/examples.md:372` | ① 同 #74: "DOMAIN" 应为 "RDOMAIN", 漏 "QVAL". ② KB 表头 Row/STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL/QNAM/QLABEL/QVAL/QORIG/QEVAL 逐格一致 |
| 76 | ig34_p0078_a021 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0078.txt:25` + 渲染 p78; `DM/examples.md:439` | ① 原子 SEX "M", PDF Row3 (ABC789-010-047) SEX "F". ② KB:439 逐格一致 (…\|24\|YEARS\|F\|OTHER\|HISPANIC OR LATINO). 同表下一行 PDF 行号重复 "3", KB 写 "4" — 已登记 `B-DM T-1`, 不算本条问题 |
| 77 | ig34_p0080_a002 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0080.txt:8-9`; `SE/spec.md:50-57` | ① 原子 CDISC Notes "...the value for ELEMENT would be as specified in the Comment Concepts) section after a comment in the CRF." 且缺 Core; PDF "...If ETCD has a value of "UNPLAN", then ELEMENT should be null." Core Perm. ② KB 逐格: Description of Element / Char / * / Synonym Qualifier / Perm / Notes 逐字一致 |
| 78 | ig34_p0101_a011 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0101.txt:8-12`; `CM/assumptions.md:27` | ① 原子 "CMENDC could be used to indicate that the use is unknown/has not yet happened." PDF 无此句, 原文 "CMENDTC is null because the end date is unknown/has not yet happened." ② KB:27 全段规整空白后包含 PDF 4.a 全文 (脚本 True) |
| 79 | ig34_p0112_a009 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p112 (Exposure CRF 表); `EX/examples.md:67-82` | ① 原子表头 "[Field] \| [Value]" 为抽取物虚构, PDF 该 CRF 表无表头行 (首行即 Visit \| 3). ② KB 用空表头 "\| \| \|" (Markdown 语法所需, 未虚构表头文字), 15 行逐格一致 |
| 80 | ig34_p0116_a009 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0116.txt:11` + 渲染 p116; `EX/examples.md:265` | ① 原子 "ECPREP" / "ECDOSEU" / "ECTRREF", PDF "ECPRESP" / "ECDOSU" / "ECTPTREF". ② KB 21 列表头逐格一致 |
| 81 | ig34_p0116_a010 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0116.txt:14-15` + 渲染 p116 放大; `EX/examples.md:268` | ① 原子 ECTRT "BOTTLE"、EPOCH "TREATMENT"; PDF 格内换行值为 "BOTTLE 2"、"TREATMENT 1". ② KB Row2 21 格逐格一致 |
| 82 | ig34_p0116_a012 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0116.txt:16-17` + 渲染; `EX/examples.md:269` | ① 原子 Row3 ECDOSU/ECDOSFRM "TABLET, COATED"、日期 07-01、STDY/ENDY 1; PDF 为 "CAPSULE"、2002-07-02T07:30、2/2, 且 ECTRT "BOTTLE 1"、EPOCH "TREATMENT 1". ② KB Row3 逐格一致 |
| 83 | ig34_p0116_a014 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0116.txt:20-21` + 渲染放大; `EX/examples.md:271` | ① 原子 Row5 "TABLET, COATED"、2002-07-02T07:30、2/2; PDF 为 "CAPSULE"、2002-07-03T07:32、3/3, ECTRT "BOTTLE 1"、EPOCH "TREATMENT 1". ② KB Row5 逐格一致 |

## 计数

| 层 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|---|
| TRIAGE_ATOM_ERR (25) | 25 | 0 | 0 | 0 |

层通过条件 (NOT_HOLD 0 且 UNVERIFIABLE 0): 满足.

## 样本外发现的 KB 内容问题

无新问题. 顺带核到的两处 KB≠PDF 均已登记:
- `knowledge_base/domains/DM/examples.md:68` "ACTARMCD" vs PDF p69 Ex3 Row1 叙述 "ACTRMCD" — 登记 `B-DM T-3`.
- `knowledge_base/domains/DM/examples.md:440` Row "4" vs PDF p78 Ex7 dm 行号重复 "3" — 登记 `B-DM T-1`.

备注 (原子层, 非 KB): p69 原子 a023-a032 混了 Ex2 (ABC) 与 Ex3 (DEF) 两张 se.xpt 表的值; p77 原子 a015-a018 把 dm.xpt 抽成了 suppdm 表 (与 p78 a007-a010 重复). 只影响台账原子, KB 两张表都正确.
