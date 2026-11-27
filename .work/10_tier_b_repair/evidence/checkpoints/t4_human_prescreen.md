# T4.2 人工抽样 42 条 — AI 预筛 (U-6)

<!-- chain: E (plans) -->
> 性质: AI 预筛 (general-purpose, opus), 不是人工判定; 不替代 T4.2 人工闸; t4_human_sample.md 用户判定栏保持空白.
> 日期: 2026-11-27 · KB 版本 = 当前 HEAD (dc6bb34) 的 KB (冻结; `git diff 00a2e93 HEAD -- knowledge_base` 为空, 即 KB 内容 = 00a2e93).
> brief: `subagent_prompts/t4/t4_u6_prescreen_v1.0.md` + `t4_common_v1.0.md`. 被审包: `evidence/checkpoints/t4_human_sample.md` (未修改).
> 方法: 每条都用 Read(pages=N) 看了原 PDF 渲染页 (IG = `source/cdisc/SDTMIG v3.4 (no header footer).pdf`, SV = `SDTM_v2.0.pdf`), 并用 grep/sed 在 KB 现文里重新定位核对 (不只信包里给的行号). 引文 ≤ 25 词.

## 分层计数

| 层 | 内容正确 | 内容错误 | 看不出 |
|---|--:|--:|--:|
| REWRITE_OK (10) | 10 | 0 | 0 |
| REAL_GAP (10) | 10 | 0 | 0 |
| VALUE_DIFF+IE (10) | 10 | 0 | 0 |
| RISK_ANCHORLESS (12) | 12 | 0 | 0 |
| **合计 42** | **42** | **0** | **0** |

## 逐条

| # | atom_id | 层 | 终态 | 预筛 | 理由 | 依据 |
|---|---|---|---|---|---|---|
| 1 | ig34_p0010_a002 | REWRITE_OK | PDF_TYPO | 内容正确 | 渲染页确为 "a codelist not yet been developed" (缺 has); KB 写 "has not yet been developed", 与登记 B-ch01 T-1 "KB 写正确值" 一致; 嵌套层级 (Controlled Terms 下的三级列表) 同 PDF. | IG 渲染 p10 第 2 个圆点; registry `t2_pdf_typo_registry.jsonl:195`; KB `chapters/ch01_introduction.md:85` |
| 2 | ig34_p0010_a012 | REWRITE_OK | EXACT | 内容正确 | "CDISC Notes may include" 下第 1 项, 逐字一致, 层级同. | IG 渲染 p10; KB `ch01_introduction.md:95` |
| 3 | ig34_p0011_a018 | REWRITE_OK | EXACT | 内容正确 | Record Qualifiers 条逐字一致 (PDF 句末本无句号, KB 同); 只加了粗体. | IG 渲染 p11; KB `chapters/ch02_fundamentals.md:30` |
| 4 | ig34_p0011_a030 | REWRITE_OK | EXACT | 内容正确 | 跨页句 (p11 末 + p12 首 "name, as the value of the DOMAIN variable…") KB 合成一段, 4 种用途齐全. | IG 渲染 p11 末行、p12 首 2 行; KB `ch02_fundamentals.md:39` |
| 5 | ig34_p0044_a008 | REWRITE_OK | EXACT | 内容正确 | 位于 "If the reference time point is prior to…" 之下的 Start values, 未与上一组 (that time point) 混淆. | IG 渲染 p44 第 2 组圆点; KB `chapters/ch04_general_assumptions.md:974-976` |
| 6 | ig34_p0152_a0006 | REWRITE_OK | EQUIVALENT | 内容正确 | 原子只是 CRF Severity 列一个 "o Severe" 选项; KB 每行 Severity 格都有 "( ) Mild ( ) Moderate ( ) Severe", 4 行事件与 PDF CRF 一致 (勾选圈改写成 "( )", 等价). | IG 渲染 p152 CRF 表; KB `domains/CE/examples.md:41-46` |
| 7 | ig34_p0152_a0009 | REWRITE_OK | EQUIVALENT | 内容正确 | 同 #6, 为另一行事件的 Severe 选项; KB 4 行均承载. | 同上 |
| 8 | ig34_p0152_a0010 | REWRITE_OK | EQUIVALENT | 内容正确 | Diarrhea 行: Yes/No、两日期格 (dd/mmm/yyyy)、Mild/Moderate/Severe 全有, 位置在 Ex2 CRF. | IG 渲染 p152; KB `CE/examples.md:45` |
| 9 | ig34_p0153_a0008 | REWRITE_OK | EQUIVALENT | 内容正确 | "How did fracture occur?" 选项 Pathologic/Fall/Other trauma/Unknown 顺序与渲染一致 (○ 改写为 "( )"). | IG 渲染 p153 Bone Fracture Assessment 表; KB `CE/examples.md:77` |
| 10 | ig34_p0367_a019 | REWRITE_OK | EXACT | 内容正确 | PDF Ex1 CRF 有 3 个时间点 (5 min BEFORE / 30 / 90 min AFTER), 各有一个 Associated symptoms 块; KB 14/17/20 三行分别对应, 4 个症状各 No/Yes, 无遗漏. 标签与选项拼成同一格, 顺序不变. | IG 渲染 p367; KB `domains/FA/examples.md:12-20` |
| 11 | ig34_p0009_a006 | REAL_GAP | EXACT | 内容正确 | 阅读步骤第 7 条逐字一致, 编号与前后条一致. | IG 渲染 p9; KB `ch01_introduction.md:61` |
| 12 | ig34_p0012_a015 | REAL_GAP | EXACT | 内容正确 | Interventions class 条逐字一致 (self-administered 的不换行连字符归一为普通连字符). | IG 渲染 p12 §2.3; KB `ch02_fundamentals.md:51` |
| 13 | ig34_p0013_a008 | REAL_GAP | EXACT | 内容正确 | "Final domains will be published only in an SDTM implementation guide…" 句在 §2.5 第 2 段, 位置与 PDF 一致. | IG 渲染 p13 §2.5; KB `ch02_fundamentals.md:74` |
| 14 | ig34_p0196_a003 | REAL_GAP | EXACT | 内容正确 | 通用 lab 规范表 --NAM 行 7 格 (Char / * / Record Qualifier / Perm) 全对, 在 §6.3.5.1 表中 --REASND 与 --SPEC 之间, 同 PDF. | IG 渲染 p196 表; KB `domains/LB/assumptions.md:40` |
| 15 | ig34_p0208_a023 | REAL_GAP | EXACT | 内容正确 | Example 1a "Rows 1-3" 跨页说明前半段逐字一致; KB 与 p209 续文合成一段, 在 Ex1a 的 cp.xpt 之前 (同 PDF). | IG 渲染 p208 末、p209 首; KB `domains/CP/examples.md:15` |
| 16 | ig34_p0209_a001 | REAL_GAP | EXACT | 内容正确 | 同段后半 ("CD45+ leukocytes. Once they have been included…" 至 "denominator marker string."), 逐字一致. | IG 渲染 p209 第 1 段; KB `CP/examples.md:15` |
| 17 | ig34_p0214_a001 | REAL_GAP | EXACT | 内容正确 | Example 4 编号说明第 1 条 (CPTSTCND) 逐字一致, 位于 Ex4 引言之后、Rows 1-3 之前, 同 PDF. | IG 渲染 p213 末 (Example 4 引言)、p214; KB `CP/examples.md:146` |
| 18 | ig34_p0373_a012 | REAL_GAP | EXACT | 内容正确 | FA Example 5 说明句逐字一致, 弯引号 “about” 与 PDF 同. | IG 渲染 p373; KB `FA/examples.md:226` |
| 19 | ig34_p0416_a006 | REAL_GAP | EXACT | 内容正确 | TI Description/Overview 定义句一致, 后半句 "This domain is not subject oriented." 也在. | IG 渲染 p416; KB `domains/TI/assumptions.md:18` |
| 20 | sv20_p0004_a013 | REAL_GAP | EXACT | 内容正确 | SDTM v2.0 §1.2 句逐字一致, 在 §1.2 Implementation Advice 下. | SV 渲染 p4 §1.2; KB `model/01_concepts_and_terms.md:15` |
| 21 | ig34_p0055_a026 | VALUE_DIFF | EXACT | 内容正确 | p55 的表头属于 Example 1 suppmh.xpt (11 列), 对应 KB 1428 (Ex1 suppmh); 1445 是 p56 Ex2 suppae, 不是这条. 列名与列序一致. | IG 渲染 p55 suppmh.xpt; KB `ch04_general_assumptions.md:1426-1431` |
| 22 | ig34_p0169_a0024 | VALUE_DIFF | PDF_TYPO | 内容正确 | 渲染 p170 Ex1 ho.xpt 第 5 行确为 "REHABILIATION FACILITY" (笔误), KB 写 REHABILITATION, 与登记 B-HO T-1 一致; KB Ex1 全 12 行逐格与 PDF 一致. 注意: 原子 verbatim 本身抽错 (见样本外 1). | IG 渲染 p170; registry `t2_pdf_typo_registry.jsonl:98`; KB `domains/HO/examples.md:19-32` |
| 23 | ig34_p0190_a011 | VALUE_DIFF | ATOM_ERR | 内容正确 | 渲染 p190 Ex1 第 9 行 EGXFN 为 "PQW436789-07.xml" (原子误作 P0W), VISIT 折行为 "Screening 1" (原子漏 1); KB 两处都按 PDF 写. 原子抽错、KB 正确. | IG 渲染 p190 eg.xpt 第 9 行; KB `domains/EG/examples.md:33` |
| 24 | ig34_p0353_a015 | VALUE_DIFF | EXACT | 内容正确 | TU Ex1 第 2 行: TULOC 三行折行 "AORTO-ILIAC / PERIPHERAL / ARTERY" 合成后与 KB 一致, 其余格一致. | IG 渲染 p353 tu.xpt; KB `domains/TU/examples.md:24` |
| 25 | ig34_p0371_a018 | VALUE_DIFF | EXACT | 内容正确 | FA Ex3 mh.xpt 第 1 行: MHEVDTYP=DIAGNOSIS, MHSCAT 空, MHSEV/MHDTC 空, MHSTDTC=2003, MHEVLINT 空, 与渲染逐格一致. | IG 渲染 p371; KB `FA/examples.md:155` |
| 26 | ig34_p0122_a009 | IE | INTENTIONAL_EXCLUDE | 内容正确 | 规范表行 (SPEC_TABLE_ROW) 由 spec.md 以字段格式承载, 不进叙述合理. 渲染为 "(in ISO 8601)" 与 "(MLTPTREF)"; 原子 "ISO 8601 values"/"MLTPREF" 是抽错, KB 按 PDF 写对. | IG 渲染 p122 MLELTM 行; KB `domains/ML/spec.md:284-291` |
| 27 | ig34_p0188_a003 | IE | INTENTIONAL_EXCLUDE | 内容正确 | EGTPTREF 行 Label/Type/Role/Notes/Core 全部在 spec.md 中, 不重复进 assumptions 合理. | IG 渲染 p188 首表; KB `domains/EG/spec.md:383-390` |
| 28 | ig34_p0295_a021 | IE | INTENTIONAL_EXCLUDE | 内容正确 | NV 规范表 VISIT 行 (Char, Timing, Perm, Notes) 在 spec.md 承载. | IG 渲染 p295; KB `domains/NV/spec.md:284-291` |
| 29 | ig34_p0309_a014 | IE | INTENTIONAL_EXCLUDE | 内容正确 | RE 规范表 REEVALID 行在 spec.md 承载; KB 多写 C-code "C96777" 属附加, 不改原意. | IG 渲染 p309; KB `domains/RE/spec.md:302-309` |
| 30 | sv20_p0046_a005 | IE | INTENTIONAL_EXCLUDE | 内容正确 | 符合用户裁定 R1-row: model/ 中有 5 列精简版, 且 #/name/label/type/role 与 PDF 一致 (3/USUBJID/Unique Subject Identifier/Char/Identifier); C-code C69256 与 Definition 不收属于该类. | SV 渲染 p46 SE 表第 3 行; 规则 `evidence/checkpoints/t1_r1_r4_resolution.md:8`; KB `model/03_special_purpose_domains.md:131` |
| 31 | ig34_p0065_a022 | RISK_ANCHORLESS | EXACT | 内容正确 | 交叉引用 "see Section 7.2.1, Trial Arms, Example Trial 3" 在 DM Assumption 4.b 中, 位置与上下文 (4.a.i-iv 之后、4.c 之前) 同 PDF. | IG 渲染 p65 4.b; KB `domains/DM/assumptions.md:25` |
| 32 | ig34_p0071_a015 | RISK_ANCHORLESS | EXACT | 内容正确 | 这句 (QNAM="CRACEn"、QLABEL="Collected Race n") 在 p71 是 Ex4 aCRF 红框批注, 在 p72-73 是 Ex4 CRF Metadata 的 SDTM Target Mapping 格. KB 在 Ex4 CRF Metadata 188-194 行逐字承载 (340/342 属 Ex6, 不对应). 同例内信息无损; aCRF 图的 KB 改写未复述批注 (见样本外 2). | IG 渲染 p71 三个红框、p72 CRF Metadata; KB `domains/DM/examples.md:111-175, 188-194` |
| 33 | ig34_p0120_a004 | RISK_ANCHORLESS | EXACT | 内容正确 | EX Example 8 ec.xpt 第 2 行 (EXCEPTION DOSE, ECOCCUR=N, ECDOSE 空, 2012-01-15, ECSTDY/ECENDY=3) 与渲染逐格一致, 在 Ex8 下. | IG 渲染 p119 末 (Example 8)、p120; KB `domains/EX/examples.md:446` |
| 34 | ig34_p0157_a0026 | RISK_ANCHORLESS | EXACT | 内容正确 | DS Assumption 5 全句一致, 包括末句 "Additional reasons should be submitted in SUPPDS." 和弯引号. | IG 渲染 p157 第 5 条; KB `domains/DS/assumptions.md:43` |
| 35 | ig34_p0171_a0002 | RISK_ANCHORLESS | EXACT | 内容正确 | HO Example 2 第 10 行 (ABC123102, HOSEQ 3, ICU, INITIAL HOSPITALIZATION, 两个日期时间) 一致; 原子多 1 个空格是抽取伪影. | IG 渲染 p171 首表; KB `HO/examples.md:72` |
| 36 | ig34_p0209_a006 | RISK_ANCHORLESS | EXACT | 内容正确 | Ex1a "Rows 14-15" 说明逐字一致, 在 Rows 12-13 与 Row 16 之间, 同 PDF. | IG 渲染 p209; KB `CP/examples.md:25` |
| 37 | ig34_p0210_a022 | RISK_ANCHORLESS | EXACT | 内容正确 | 这条是 Example 1b 的 "Row 4" (不是 1a), KB 放在 "### Example 1b" 下 Rows 2-3 之后, 位置正确. | IG 渲染 p210 Example 1b; KB `CP/examples.md:47-56` |
| 38 | ig34_p0389_a008 | RISK_ANCHORLESS | EXACT | 内容正确 | TA Example 1 段落逐字一致, 在 Trial Design Matrix 之后、ta.xpt 之前 (同 PDF), 属 "## Example 1". | IG 渲染 p389; KB `domains/TA/examples.md:20, 140-147` |
| 39 | ig34_p0342_a022 | RISK_ANCHORLESS | EXACT | 内容正确 | SS 规范表标题句逐字一致, 在 "SS – Specification" 下. | IG 渲染 p342 §6.3.11; KB `domains/SS/assumptions.md:7-9` |
| 40 | ig34_p0367_a001 | RISK_ANCHORLESS | EXACT | 内容正确 | FA Assumption 5 一致, 子项 5.a 也随后承载. | IG 渲染 p367 顶部; KB `domains/FA/assumptions.md:114-115` |
| 41 | ig34_p0367_a013 | RISK_ANCHORLESS | EXACT | 内容正确 | 与 #10 同一 CRF 的另一时间点 Associated symptoms 块; KB 三处都在, 能对上. | IG 渲染 p367; KB `FA/examples.md:14,17,20` |
| 42 | ig34_p0369_a024 | RISK_ANCHORLESS | EXACT | 内容正确 | FA Ex2 Rash Assessment 的 Scars 行 (末行, 在 Scabs 之后), 6 档选项一致. | IG 渲染 p369; KB `FA/examples.md:87` |

## 样本外发现 (不计入 42 条判定)

1. **#22 原子标签问题 (不影响 KB 内容)**: `ig34_p0169_a0024` 的 verbatim "| 5 | ABC | HO | ABC123105 | 1 | GENERAL WARD | | TREATMENT | 2011-09-09 | 2011-09-11 |" 与 PDF 任何一行都对不上 (p169 没有数据表行; p170 Ex1 第 5 行是 ABC123102 / 3 / REHABILIATION FACILITY / 2011-08-15), 多一列, 而且混杂了第 3 行和第 6 行的值. 终态只记 PDF_TYPO, 没有体现 "原子抽错". 建议主控核对该原子是否该同时登记 ATOM_ERR, 或在包里注明 verbatim 不可信.
2. **#32 DM Ex4 aCRF 改写**: `domains/DM/examples.md:113-175` 用 Mermaid 加 KB note 改写 p70-71 的 aCRF 图, 但没有复述红框批注 "For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn"…", 也没有复述灰框里的 CRF 完成说明. 这些信息在同例 CRF Metadata (188-194) 中逐字都有, 所以不判错, 只是图本身信息不全.
3. **FA Ex5 CRF 灰底格**: 渲染 p373 中 Diarrhea/Nausea 的 Volume (mL) 格是灰底 (表示不收集); KB `FA/examples.md:222-224` 只留空格, 灰底的含义没有保留. 影响小.
4. **FA Ex3 Row 说明格式**: `FA/examples.md:148-149` 的 "Row 1:" 和 "Rows 2-6:" 之间没有空行, Markdown 渲染时会并成一段 (文字本身正确). 只是格式问题.
5. 叙述 "FAEVINTX" (p373) 已登记为 B-FA T-9 (`t2_pdf_typo_registry.jsonl:81`), KB 228 写的是 FAEVLINT, 与登记一致. 只是顺带核对.
