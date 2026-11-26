# T4 用户裁定汇总 (O25)
> 状态: 草拟, 待主控审后交用户 (2026-11-26, T2S.REG, executor)
> 来源: `evidence/checkpoints/t2_B-*.md` / `t2_S-*.md` (含 _review / _audit 改判)、`work/out_of_scope_findings.md` O1-O61、`evidence/checkpoints/t2_post_user_ack.md`、`evidence/checkpoints/t1_lane_notes.md` "T4 汇总须列" 条、`work/t1_errata.json` (pending_user 4 条为 T1 REAL_GAP 争议, 非 typo, 不入本表)。
> 机读登记: `work/t2_pdf_typo_registry.jsonl` (269 行; 位置按 HEAD b982581 内容重定位)。引文 ≤ 25 词/处。

## 0. 用法
- 每行二选一: **A = 维持现状** (KB 照录 PDF), **B = 改为候选值**。"主控建议" 列是登记员草拟, 主控审后可改。
- 口径 (沿用 dispatch "PDF_TYPO 取舍规则"): 正确值能由 PDF 自身单值确定 → KB 写正确值; 否则照录 + T4。下列 A 组都是 "不能单值确定" 的项。建议列对 "语法只有一种补法" 的项倾向 B (与已接受的 B-IS T-5 / B-ch01 T-1 keep-correct 同口径), 对 "多种修法" 的项倾向 A。
- 同一 PDF 问题有多个 KB 副本的, 表中逐个列出, 裁定时一并改。

## 1. A 组: 照录 + T4 待用户 A/B

### A1 表格格值: 日期 / 编号 / ID / 单位 (正确值 PDF 自身不能单值确定)

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) |
|---|---|---|---|---|---|---|
| A1-1 | B-AE U-1 | `domains/AE/examples.md:82` | p142 Ex5 r2 AEENDY 25 | AEENDY 24 或 AEENDTC 2018-05-11 | AESTDTC 2018-05-01=Day 15 → 05-10 应为 Day 24; 日期/Day 谁错不可单值 | A |
| A1-2 | B-AE U-2 | `domains/AE/examples.md:97` | p142 Ex6 r2 AEENDTC 2014-11-27 | AEENDTC 2018-11-27 (仅改年份) | 早于 AESTDTC, 年份必错; 按 Day 推得 11-28 ≠ 11-27, 非单值 | A |
| A1-3 | B-AE U-3 | `domains/AE/examples.md:96` | p142 Ex6 USUBJID r1 002 / r2 001 | 两行同一 USUBJID (001 或 002) | 同 SPDEVID、AESEQ 1/2、叙述同一受试者; 哪个对不可定 | A |
| A1-4 | B-AE U-4 | `domains/AE/examples.md:97` | p142 Ex6 r2 AESTDY 78 | AESTDY 80 | r1 Day 27=2018-09-01 推得 10-24 应为 Day 80 | A |
| A1-5 | B-AE U-5 | `domains/AE/examples.md:96` | p142 Ex6 r1 AERLDEV CAUSAL | CAUSAL RELATIONSHIP (原 KB 值) | 原 KB CAUSAL RELATIONSHIP; KB 无 ISO 14155 码表可证 | A |
| A1-6 | B-BE O28 | `domains/BE/examples.md:122` | p147 Ex2 bs r1 BSORRES 12 mL vs BSSTRESC/N 6 | BSORRES 6 mL 或 STRESC/N 12 | PDF 内部不一致, 无法由 PDF 定正确值 (O28) | A |
| A1-7 | B-CE T-2 | `domains/CE/examples.md:101` | p153 USUBJID ABC -US-701-002 (mh/ce/pr 8 格) | ABC-US-701-002 (去空格) | USUBJID 惯例不含空格; PDF 8 处一致带空格 (O44: 3.5pt 字距说法不成立) | A (PDF 8 处一致); 若重 ID 惯例则 B |
| A1-8 | B-CE T-3 | `domains/CE/examples.md:110` | p153 suppmh/suppce USUBJID 001-001 | supp USUBJID = 父表 USUBJID | 与父表 ABC -US-701-002 不一致, PDF 内部矛盾 | A |
| A1-9 | B-DS U-1 | `domains/DS/examples.md:294` | p165 Ex10 se ETCD SCREEN | ETCD SCRN (SE.ETCD 须∈TE.ETCD, spec 约束) | 同例 TE/TA 为 SCRN; 跨表不可定 (reviewer: 可用 SE.ETCD∈TE spec) | B (spec 约束可单值定) |
| A1-10 | B-DS U-2 | `domains/DS/examples.md:407` | p167 Ex11 ds 筛选 3 行 TAETORD=1 | TAETORD 0 (同 TA 筛选元素) | TA/SE 筛选元素 TAETORD=0; 跨表 | A |
| A1-11 | B-EX T-5 | `domains/EX/examples.md:300` | p117 Ex6 ex EXENDTC 24 行全空 | EXENDTC = 同行 EXSTDTC (Assumption 4b) | EXENDY 有值; Assumption 4b 要求点给药复制 EXSTDTC; 自填属生成 | A (自填 24 格属生成) |
| A1-12 | B-FA T-10 | `domains/FA/examples.md:321` | p375 Ex6 relrec STUDYID ABC vs ae/faae XYZ | relrec STUDYID XYZ | 跨表矛盾; USUBJID 亦不一致, 无单值 | A |
| A1-13 | B-GF U-1 | `domains/GF/examples.md:64` | p225 GFMETHOD REAL_TIME POLYMERASE CHAIN REACTION ×3 | REAL-TIME POLYMERASE CHAIN REACTION (去下划线) / CT 全称 …ASSAY | 引言 real-time…; CT C51962 为 REAL-TIME … ASSAY, 不单值 | A |
| A1-14 | B-GF U-2 | `domains/GF/examples.md:145` | p227 MB r1 MBREFID INFLU0101 | INFLU0101.1 | GF/MS r1 为 INFLU0101.1; 可能有意 | A |
| A1-15 | B-IS U-1 | `domains/IS/examples.md:117` | p236 ISSEQ 同受试者内重复 (Ex5/10/11 共 18 格) | ISSEQ 按受试者连续编号 (18 格) | spec 要求唯一但 any valid number, 正确编号不可单值 | A |
| A1-16 | B-IS U-3 | `domains/IS/examples.md:164` | p237 Ex7 r3/r4 VISIT 1 ISDTC 2017-08-27 | ISDTC 2017-07-27 | 同受试者 Ex5/Ex8 VISIT 1=2017-07-27; 跨例 | A |
| A1-17 | B-MH T-2 | `domains/MH/examples.md:106` | p178 Ex5 r1 MHDTC 2019-011-02 | 2019-11-02 或 2019-01-02 | 可读 2019-11-02 或 2019-01-02, 不单值 | A |
| A1-18 | B-MS T-4 | `domains/MS/examples.md:80` | p262 suppms QNAM MSMEDTYPE (9 字符) | QNAM MSMEDTYP (8 字符) | QNAM≤8; 正确值非 PDF 自证 | A |
| A1-19 | B-OE U-1 | `domains/OE/examples.md:144` | p304 Ex4 OESEQ 1/2/1/2 | OESEQ 3/4 (OS 行) | 同受试者 SEQ 重复, 正确编号不可定 | A |
| A1-20 | B-PCPP T-4 | `domains/PC/examples.md:85` | p277 文字 Rows 14-26 RELID 2/DY8DRGX vs 表 RELID 1/DY1DRGX | 文字改 RELID 1 / DY1DRGX, 或表改 RELID 2 | PDF 文字与表矛盾 | A |
| A1-21 | B-PCPP T-7 | `domains/PP/examples.md:16` | p271 Ex1 PPSTRESU H | PPSTRESU h (UNIT CT 值小写, 同列一致) | 同列 h; UNIT CT C25529 提交值为 h (terminology/core/other_part3.md:212) | B |
| A1-22 | B-SC T-2 | `domains/SC/examples.md:36` | p342 Row 3 SCDTC 2017-06-10 vs SCDY 297 | SCDY 296 或 SCDTC 2017-06-11 | 按 Row 1/2 推应为 296; 日期/SCDY 谁错不可定 (O52) | A |
| A1-23 | B-SM T-2 | `domains/SM/examples.md:39` | p86 ce r1 CEENDTC 2013-09-01T2:30 | CEENDTC 2013-09-01T12:30 (原 KB 自推值) | 早于 CESTDTC T11:00; 正确时刻 PDF 无证 | A |
| A1-24 | B-SR T-2 | `domains/SR/examples.md:97` | p380 表 SRDTC 14:08:24 vs 叙述 53h56m | 改叙述为 53h38m 或改表为 14:26 | PDF 表与叙述自相矛盾, 无第三来源 | A |
| A1-25 | B-ch04 T-2 | `chapters/ch04_general_assumptions.md:1327` | p53 lb r7 说明 LBDRVFL=Y, 表列 LBLOBXFL | 表头 LBLOBXFL→LBDRVFL, 或叙述改 LBLOBXFL | 仅 visit 3 r7 有 Y, 疑表头错标 | A |

### A2 变量名 / 参数码 / 代码写法

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) |
|---|---|---|---|---|---|---|
| A2-1 | B-ch03 T-4 | `chapters/ch03_submitting_data.md:52` | p18 IS Keys ISSCMBCL | ISMSCBCE (p456 新增变量) | 全书仅此处; 候选 ISMSCBCE (p456) | A |
| A2-2 | B-PCPP T-8 | `domains/PC/examples.md:284` | p280 散文 DYIDRGX_A / DYIDRGX_HALF | DY1DRGX_A / DY1DRGX_HALF (同页表值) | 文本层即如此, 与表 DY1DRGX_* 不一致 | B |
| A2-3 | B-PCPP T-8b | `domains/PC/examples.md:278` | p280 Ex3 引言 DYDRGX_HALF | DY1DRGX_HALF | 应为 DY1DRGX_HALF, 不单值 | B |
| A2-4 | B-TS T-2 | `domains/TS/assumptions.md:43` | p419 正文 "Dose" vs 表 DOSE | TSPARMCD = "DOSE" (CT 参数码) | 大小写不一致 | B (CT 可定) |
| A2-5 | B-TS T-3 | `domains/TS/assumptions.md:43` | p419 DOSFREQ vs Ex4 DOSFRQ | DOSFRQ (CT C-code 参数码) | 两处互异 | B (CT 可定) |
| A2-6 | B-TS T-4 | `domains/TS/assumptions.md:57` | p419 OUTMSPR vs Ex1 OUTMSPRI | OUTMSPRI (CT 参数码) | 两处互异 | B (CT 可定) |
| A2-7 | B-TS T-6 | `domains/TS/assumptions.md:115` | p425 MAXAGE vs 参数 AGEMAX | AGEMAX case (CT 参数码) | PDF 内不一致 | B (CT 可定) |
| A2-8 | B-SM O32 | `domains/SM/examples.md:7` | p85 Row 1 叙述 SMDY | SMSTDY (Rows 2-3 叙述同变量) | 非 SM 变量 (疑 SMSTDY); 不能唯一确定 (O32) | B |
| A2-9 | B-EG T-1 | `domains/EG/examples.md:15` | p189 叙述 EGCAT="FINDINGS" vs 表 FINDING | 叙述 EGCAT = "FINDING" (同表) | 叙述与表矛盾, 无第三证据 | A |
| A2-10 | B-EG T-2 | `domains/EG/examples.md:42` | p190 叙述 SCREEN 2 vs 表 SCREEN II | 叙述 "SCREEN II" (同表 VISIT) | 可能同一访视两种写法 | A |
| A2-11 | B-ch02 T-1 | `chapters/ch02_fundamentals.md:176` | p16 Trials Sets domain | Trial Sets (sv20 p53 §5.1.2) | SDTMIG 自身无 Trial Sets; sv20 p53 §5.1.2 标题 | B |
| A2-12 | S-TUFA TR T-5 | `domains/TR/spec.md:264` | p351 TAETORD Notes Epoch associated with… | Number that gives the planned order of the element within the arm. (FA/SR 同变量) | 与 Label 不符; 候选 = FA/SR 同变量 Notes | B |
| A2-13 | REG CP N-1 | `domains/CP/examples.md:171` | p214 GATE and GATEDEF show the gating strategy | CPGATE and CPGATDEF | p214 原文; 变量名应为 CPGATE/CPGATDEF? 与 T-15 同型但为泛型省略写法, 未登记 | A (泛型省略写法, 新发现) |
| A2-14 | REG BS N-1 | `domains/BS/assumptions.md:23` | p198 Assumption 5 --ORNLO, --ORNHI | --ORNRLO, --ORNRHI (同 GF T-6 列表写法) | 非标准变量名 (应 --ORNRLO/--ORNRHI); 同句 --STRNLO 已按 T-3 改正, 处理不一致 | B (与同句 T-3 口径一致) |
| A2-15 | S-SPC2 N-1 | `domains/PC/examples.md:299` | p281 PP records with PCSEQ values | PC records with PCSEQ | 应为 PC records (PCSEQ 属 PC), 照录 | B (PCSEQ 属 PC, 单值) |
| A2-16 | S-SPC2 N-2 | `domains/PC/examples.md:333` | p281 PP records with PGRPID values | PPGRPID values | 应为 PPGRPID, 照录 | B (单值) |

### A3 叙述语法 / 措辞 (单一补全建议 B, 多解建议 A)

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) |
|---|---|---|---|---|---|---|
| A3-1 | B-DM N-1 | `domains/DM/examples.md:24` | p68 The arm actual arm variables are null | The arm and actual arm variables are null | 疑缺 and, 不能由 PDF 自身确定 | A |
| A3-2 | B-DS U-4 | `domains/DS/examples.md:87` | p160 and in the AE record was represented | The relationship between the DS record and the AE record | PDF 原句语法瑕疵 | B (删 in, 单一) |
| A3-3 | B-DS U-6 | `domains/DS/examples.md:346` | p166 AB +C (空格) | AB+C (去空格) | 空格是否多余不可定 | A |
| A3-4 | B-DV T-1 | `domains/DV/examples.md:17` | p179 DVTERM 末尾句点 | 去尾句点 (同 spec Notes 引用值) | spec Notes 引同值句点在引号外; verbatim 尾句点不构成可证错 | A |
| A3-5 | B-EG T-3 | `domains/EG/examples.md:42` | p190 principal investigation | principal investigator (同表 EGEVAL) | 表 EGEVAL=PRINCIPAL INVESTIGATOR; 改正属语义改写 | B |
| A3-6 | B-FA T-3 | `domains/FA/assumptions.md:19` | p361 These type of assessments | These types of assessments | 语法类 | A |
| A3-7 | B-FA T-4 | `domains/FA/assumptions.md:39` | p362 thought be related | thought to be related | 漏词 (语法) | B (单一补全) |
| A3-8 | B-FA T-6 | `domains/FA/assumptions.md:51` | p363 FA may provided | FA may provide | 语法类 | B (单一补全) |
| A3-9 | B-FA T-8 | `domains/FA/examples.md:183` | p372 used to populated FADTC | used to populate FADTC | 语法类 | B (单一补全) |
| A3-10 | B-IS U-2 | `domains/IS/examples.md:101` | p235 RSV-protein B ×3 | RSV-protein Z ×3 | 语境疑应为 Z, PDF 未明载 | A |
| A3-11 | B-IS U-4 | `domains/IS/examples.md:193` | p239 expressed in by the opsonization index | expressed by / expressed in | 删 in 或删 by 皆通 | A |
| A3-12 | B-MB T-4 | `domains/MB/examples.md:171` | p261 sputum (Ex3 实为灌洗液) | lavage fluid sample | PDF 原文如此, 不可单值 | A |
| A3-13 | B-MI O43 | `domains/MI/examples.md:23` | p266 is a represented in a derived record | is represented in a derived record | 语法错, 不可唯一确定 (O43) | A |
| A3-14 | B-NV N-1 | `domains/NV/assumptions.md:23` | p294 may included | may include | PDF 语法, 照录 | B (单一补全) |
| A3-15 | B-NV N-2 | `domains/NV/examples.md:63` | p297 links the each | links each | PDF 语法, 照录 | B (删 the, 单一) |
| A3-16 | B-ch08 T-7 | `chapters/ch08_relationships.md:443` | p440 therefore is does not | therefore it does not / therefore does not | is→it 或删 is 两解 | A |
| A3-17 | B-REL T-7 (RELSPEC 副本) | `domains/RELSPEC/assumptions.md:19` | p440 therefore is does not | 同 ch08 T-7, 两处同改 | is→it 或删 is 两解 (=ch08 T-7) | A |
| A3-18 | B-ch08 T-8 | `chapters/ch08_relationships.md:321` | p436 whether the data represent as an event or a finding | represent an event / are represented as an event | 删 as 或 are represented as 均有 PDF 先例 | A |
| A3-19 | B-ch03 T-3 (ch03) | `chapters/ch03_submitting_data.md:71` | p19 per location per per visit | per location per visit / per location per time point per visit | p19/p312 同为 per per; 少词或多词不可定 (OE 同位 per time point) | A; 三处同改 |
| A3-20 | S-FND UR U-1 (assumptions) | `domains/UR/assumptions.md:9` | p312 per location per per visit | 同 ch03 T-3 | p19/p312 同为 per per; 少词或多词不可定 (OE 同位 per time point) | A; 三处同改 |
| A3-21 | S-FND UR U-1 / O55 (spec) | `domains/UR/spec.md:3` | p312 per location per per visit | 同 ch03 T-3 | p19/p312 同为 per per; 少词或多词不可定 (OE 同位 per time point) | A; 三处同改 |
| A3-22 | B-TA T-3 | `domains/TA/examples.md:363` | p392 (Open DRUG X and Rescue) | (Open Drug A and Rescue) | 图块 Open A / TDM Open Drug A; 不可唯一 | A |
| A3-23 | B-TA T-5 | `domains/TA/examples.md:385` | p392 Example 7 in Section 5.2 vs §7.2.1.1 DM Example 3 | DM Example 3 (§7.2.1.1 说法) | PDF 两处 DM 例号不同 | A |
| A3-24 | B-TE T-1 | `domains/TE/examples.md:102` | p407 First dose of treatment in Element | First dose of treatment Element (去 in, 3:2 多数) | 表/叙述矛盾 (3:2 无 in, reviewer 倾向去 in) | B |
| A3-25 | B-TE T-2 | `domains/TE/examples.md:103` | p407 16 days … WBC recovers | At least 16 days … WBC recovered (同 Ex3) | 与 Ex3 Row 4 措辞多处不同, 无唯一值 | A |
| A3-26 | B-TS T-5 | `domains/TS/assumptions.md:65` | p425 14 terms vs 表 15 行 | among its 15 terms | 含 NA 行计数不一 | A |
| A3-27 | B-TS T-7 | `domains/TS/assumptions.md:106` | p425 Quantity sufficient vs 表 Sufficient quantity | Sufficient quantity (同表) | PDF 内不一致 | A |
| A3-28 | S-CH10 T-3 | `chapters/ch10_appendices.md:386` | p457 in version the underwent | in the version that underwent | 语法错, 正确词无依据 | B (单一补全) |
| A3-29 | S-TDM TD U-1 | `domains/TD/examples.md:161` | p414 repeats every 24 weeks (week 120, week 144, etc.) | repeats every 12 weeks (同图/表) | 图 Sched 3/表 P12W=12 周; 同句 week 96→120/144 只与 24 自洽 | A (同句周数只与 24 自洽) |
| A3-30 | S-TDM TD U-2 | `domains/TD/spec.md:39` | p411 This must be a referenced from the ADaM ADSL | must be referenced / must be a reference | be referenced / a reference 二义 | A |
| A3-31 | S-SPREL SE T-2 | `domains/SE/spec.md:39` | p79 to be consistent chronological order | to be consistent with chronological order | 缺 with | B (单一补全); SM 副本同改 |
| A3-32 | REG SM N-1 (同 SE T-2) | `domains/SM/spec.md:39` | p84 SMSEQ Should be assigned to be consistent chronological order | 同 SE T-2 | p84 同 SE T-2 (缺 with); S-SPREL 只登记 SE 副本 | 随 SE T-2 |
| A3-33 | S-SPREL OI T-1 | `domains/OI/spec.md:39` | p441 Sequence number to given to ensure | Sequence number given to ensure | 语法 | A |
| A3-34 | B-ch04 N-1 | `chapters/ch04_general_assumptions.md:863` | p41 solidus or foreword slash [/] | forward slash | PDF 拼写 foreword (应 forward), 照录 | B (拼写, 单值) |

### A4 未编号标点 / 空格 / 人名照录 (S-TYPO 必须不动)

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) |
|---|---|---|---|---|---|---|
| A4-1 | S-CH10 N-1 | `chapters/ch10_appendices.md:384` | p453 codelists . | codelists. | PDF 原文多空格 | A |
| A4-2 | S-SPREL OI T-2 | `domains/OI/spec.md:30` | p441 OIVAL . (句点前空格) | OIVAL. | PDF 排版 | A |
| A4-3 | S-SPEC1 N-1 | `domains/DM/spec.md:296` | p64 Services;2016 | Services; 2016 | 无空格, 不在裁定内 | A |
| A4-4 | S-CH10 N-2 | `chapters/ch10_appendices.md:409` | p459 Section 9.3 PB was part of | Section 9.3 PB, which was part of | PDF 语法 | A |
| A4-5 | S-CH10 N-3 | `chapters/ch10_appendices.md:388` | p452 Nov, 2021 | Nov 2021 | PDF 原文 | A |
| A4-6 | S-CH10 N-4 | `chapters/ch10_appendices.md:60` | p445 Ben Qgunsulire / Gbenga Ogunsulire | 两处人名统一 | 人名写法两处不同 | A |
| A4-7 | B-REL N-1 (RELREC 副本) | `domains/RELREC/examples.md:42` | p430 正文 "COMBO 1" vs 表 COMBO1 | "COMBO1" (同表) | PDF 自相矛盾 | A; 两处同改 |
| A4-8 | B-ch08 N-1 | `chapters/ch08_relationships.md:135` | p430 正文 COMBO 1 vs 表 COMBO1 | 同上 | PDF 自相矛盾 | A |
| A4-9 | B-REL N-2 (RELSPEC 副本) | `domains/RELSPEC/examples.md:17` | p440 图 SPC-003 (Brain) vs relspec r5 TISSUE | 图注 (Tissue) | PDF 图表矛盾 | A; 两处同改 |
| A4-10 | B-ch08 N-2 | `chapters/ch08_relationships.md:461` | p440 图 (Brain) vs relspec r5 TISSUE | 同上 | PDF 图表矛盾 | A |
| A4-11 | B-ch02 N-1 | `chapters/ch02_fundamentals.md:106` | p14 (shown in the models as “--“) | “--” (右引号闭合) | 两个左引号, 与 pdftotext 码位一致 | A |
| A4-12 | S-CH4 N-1 | `chapters/ch04_general_assumptions.md:756` | p39 (e.g. 2001-12-26T00:00:01) | (e.g., 2001-…) | 缺 e.g. 后逗号; 主控裁定 4 照 PDF | A (主控裁定 4 已定照 PDF) |
| A4-13 | B-NV N-3 | `domains/NV/assumptions.md:23` | p294 句末无句点 | 句末补句点 | PDF 原样 | A |
| A4-14 | S-INT N-1 | `domains/AG/spec.md:363` | p94 AGENRTPT Notes 同义句重复两次 | 删重复句 | PDF p94 原样即重复 | A |
| A4-15 | S-TDM N-1 | `domains/TD/examples.md:157` | p414 - 3 days / + 1 week (符号后空格) | "+1 week" / "-3 days" (去空格) | PDF 本节写法之一; Ex1 bullet 1 无空格亦照录; S-TYPO 不归一 | A |

### A6 与 U1 (排版字符照 PDF) 冲突的 keep-correct

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) |
|---|---|---|---|---|---|---|
| A6-1 | B-IS T-6 | `domains/IS/examples.md:205` | p241 STAPHYLOCOCCUS AUREUS–EPITOPE X (en dash) | en dash AUREUS–EPITOPE X (照 PDF, 按 U1) | 同例叙述 S. aureus-epitope X 用连字符 | B (U1 优先) |
| A6-2 | B-TA T-4 | `domains/TA/examples.md:351` | p391 …10 mg – Placebo (en dash) | en dash "10 mg – Placebo" (照 PDF, 按 U1) | 同表其他行用 - | B (U1 优先) |

### A5 结构 / 标题 / 口径 (O 项, 无单值正确答案)

| # | 来源 | 位置 | 现状 (A) | 候选 (B) | 依据 | 主控建议 (草拟) |
|---|---|---|---|---|---|---|
| A5-1 | O35-1 B-model05 / S-MOD3 M-2 | `model/05_study_level_data.md` 既有标题 | 标题缺 PDF 节号/原名; 5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3 共 7 个四级节与父节同为 `###` | 补 PDF 节号+原名, 四级节改 `####` | 规则 6 保留现状; S-MOD3 核过改 `####` 无锚点风险 | B |
| A5-2 | O35-2 | `model/05` TT/TP 表 "Notes" 列 | 列名 Notes | 列名改 "Usage Restrictions" (内容实为 PDF Usage Restrictions) | B-model05 writer | B |
| A5-3 | O35-3 / S-MOD3 M-4 | `model/05` TS 表 TSVALCD/TSVCDREF/TSVCDVER | 不补 "Not in nonclinical trials" (R1 缺列不补) | 补进与 TT/TP 同一承载列 | TT/TP 同类值已在 Notes 列, 承载不一致 | B |
| A5-4 | O35-4 / O38-2 | `model/05`、`model/06` Role 列括注 | 括注不统一; RELSPEC 有 "(REFID)", SUPP-- QLABEL 无 "(QNAM)" | 全部统一为 `Role (Variable(s) Qualified)` | S-MOD2 已沿用此写法 | B |
| A5-5 | O38-1 | `model/06_relationship_datasets.md` 6.1-6.7 标题 / H1 | KB 标题 (如 6.6 "Related Subjects") | PDF 原标题 (6.6 "Relationships") | 规则 6 未改 | B |
| A5-6 | O38-3 | `model/06` RELREC USUBJID/POOLID Notes | KB 自写 (PDF 空), 未标 D6 (主控 M-2a 维持) | 加 `> KB note (not in SDTMIG):` 或删 | R1 IE 行 | B (加 D6) |
| A5-7 | O38-4 | `model/06` RELREC APID Notes | 截断, 缺 POOLDEF 句 | 补全 PDF 句 | B-model06 audit | B |
| A5-8 | O41 / B-model06 review | `model/06_relationship_datasets.md:50` RELTYPE Combinations 表 (D6) + Summary 表 SUPP-- "Yes" | 保留 KB 自写表 (记录级解释, 并列 MANY/ONE) | 改为指向 ch08 的交叉引用或删; Summary "Yes" 改准确说法 | 与 SDTMIG ch08 (数据集级, 3 种组合) 不一致 | B |
| A5-9 | O48 | `domains/TI/assumptions.md` §7.4 标题 | KB 标题 | PDF "7.4 Trial Eligibility and Summary (TI and TS)" | 规则 6 未改 | B |
| A5-10 | O56 / S-SPC2 audit | `domains/PP/examples.md` "RELREC Method Quick Reference (PP-side view)" 整节 | D6 整节保留 | 换一行交叉引用到 PC/examples.md | KB 自写摘要, 与 PC/examples.md 部分重复 | B |
| A5-11 | O60 (S-MOD2/S-MOD3/S-TDM/S-TUFA) | TA §7.1/§7.2 自拟标题 (X-4)、FA `## §6.4.4 FA – Description/Overview` 合并标题、MB H2 "and"、SS `#####` 层级 | 规则 6 保留 KB 自拟标题 | 统一改 PDF 原标题 (先核 0 入站链接), S-TYPO 后一次性脚本 + 抽检 | S-MOD2/S-MOD3 已在 0 入站链接时改 PDF 原标题, 口径不一 | B |
| A5-12 | S-CH10 T-4 | `chapters/ch10_appendices.md:353` | 变更表 4.1 行在 4.5 后重复, 照录两行 | 删第二行 | p454 渲染确认 PDF 原样 | A (PDF 忠实) |
| A5-13 | t1_lane_notes "T4 统一措辞" / B-REL audit | `domains/RELREC/assumptions.md:5` D6 行 | "KB note (not in SDTMIG): … are from the SDTMIG v3.4 §8 introduction" | 改措辞避免 "not in / from" 字面矛盾 | B-REL audit LOW | B |
| A5-14 | t1_lane_notes | 全库 D6 前缀 | 说明来源/位置的 note 也用 `> KB note (not in SDTMIG):` | 这类 note 改用 `> Note:` | 前缀语义只适用于 KB 自写内容 | 主控先定口径 |
| A5-15 | S-CH8 需主控定 #2 / B-ch08 T-5 | `chapters/ch08_relationships.md:241` | 行内 `**Example 2:**` | 改独立行 `**Example 2**` (与 :100/:119/:133/:158/:230 统一) | 改后 census 因 PDF 标签无编号失配 (OK 10→9), 需 census 侧豁免 | A |

### A6 说明
- B-IS T-6 / B-TA T-4: 当时按 "KB 保留 hyphen" 登记为 keep-correct, 但 U1 (排版字符照 PDF) 后应改成 PDF 的 en dash。两项不是错值, 属 U1 适用范围, 建议直接交 S-TYPO 执行 (B)。B-MK T-1 所在 MK 表范围 "51–75%" 等 en dash 同理 (KB 全表用 hyphen), 归 S-TYPO。

## 2. B 组: 已按 keep-correct 写正确值, reviewer / auditor 要求让用户知悉
否决 (= 改回照录 PDF) 时按 "若否决" 列回退。

| # | id | 位置 | PDF 原值 | KB 现值 | 依据 | 若否决 |
|---|---|---|---|---|---|---|
| B-1 | B-AE T-3 | `domains/AE/examples.md:75` | p142 "probably related to the event" | related to the device | 同表 r2 AERLDEV=PROBABLE / AEACNDEV=REMOVED; 改词判断, 信心中高 | 改回 event |
| B-2 | B-IS T-5 | `domains/IS/examples.md:153` | p237 "participating a vaccine study" | participating in | 漏介词, 单一补全 (无同文平行句) | 删 in |
| B-3 | B-NV T-1 | `domains/NV/examples.md:11` | p296 "an fluorodeoxyglucose" | a fluorodeoxyglucose | 冠词错, 归 "拼写错" 属扩展解释 (NV review L-3) | 改回 an |
| B-4 | B-ch01 T-1 | `chapters/ch01_introduction.md:85` | p10 "a codelist not yet been developed" | has not yet been | p49 同短语 "has not yet been developed" 为旁证 | 删 has |
| B-5 | B-ch01 T-2 | `chapters/ch01_introduction.md:109` | p10 MANY → "--LNKID (and not --LNKGRP)" | --LNKGRP (and not --LNKID) | 同段前句 + p31 §4 --LNKGRP 定义; 需互换两名 | 两名换回 |
| B-6 | B-EX T-6 | `domains/EX/examples.md:362` | p118 "represented in mg/mL" | mg/kg | 同句 (mg/kg) + Ex7 ec ECDOSU=mg/kg | 改回 mg/mL |
| B-7 | S-SPC1 CP T-21 | `domains/CP/assumptions.md:24` (另 :42, :72) | p199/200/206 --BNDAGT / --GATEDEF / CPBNDAGT | --BDAGNT / --GATDEF / CPBDAGNT | spec 变量名; 改的是 Description 泛型名 (S-SPC1 需主控定 #1) | 回退 4 处 |
| B-8 | B-FA T-7 / T-9 | `domains/FA/examples.md:118` / `:228` | p370 "parent CE record" / p373 FAEVINTX | parent AE record / FAEVLINT | writer 原判照录, review C-3 改判 (同例自证) | 两处改回 |
| B-9 | B-MS T-3 | `domains/MS/examples.md:80` | p262 suppms IDVAR MBREFID | MSREFID | RDOMAIN=MS, IDVARVAL=ms MSREFID (原判照录, 后改判) | 改回 MBREFID |
| B-10 | B-TS T-1 | `domains/TS/examples.md:76` | p421 TSPARM "Trial Type" (TSPARMCD=TITLE) | Trial Title | Ex1/Ex4 同码; Row 1 说明 (writer Q-2 留回退口) | 改回 Trial Type |
| B-11 | B-ch03 T-1 / T-2 | `chapters/ch03_submitting_data.md:37` / `:49` | p18 Keys BESDTC / TESTCD | BESTDTC / FTTESTCD | 全书仅此处; 主控已裁 keep-correct (派单曾要求 Keys 逐字) | 改回 PDF |
| B-12 | S-SPEC1 T-3 | `domains/DM/spec.md:296` | p64 脚注² URL 后孤立 ")" | 删 ")" | 脚注全文无开括号 (原判照录, 后改判) | 补回 ")" |
| B-13 | B-DS T-2 | `domains/DS/examples.md:346` | p166 "where treatment AB +C" | where treatment is AB +C | 同表 r2 平行句 (DS review LOW) | 删 is |
| B-14 | B-CP T-2 / T-15 | `domains/CP/examples.md:202` / `:71` 等 8 处 | CPCSMRKR / CPGATEDEF | CPCSMRKS / CPGATDEF | spec/表头; 致 fp 回退 ig34_p0215_a018 / p0218_a014 (已接受) | 改回 PDF |
| B-15 | B-MK T-2 | `domains/MK/examples.md:53` | p293 "REPLACEMENT/ SURGICAL" | REPLACEMENT/SURGICAL | r12 同值无空格; review L-1: 实为折行歧义, 非确证印刷错 | 无需操作 (知悉即可) |

## 3. 观察项 (照录, 不需用户选择, 仅知悉)

| id | 位置 | PDF | 说明 |
|---|---|---|---|
| B-DS U-3 | `domains/DS/examples.md:37` | p159 Ex1 123104 DSSEQ RANDOMIZED=3/COMPLETED=2 | 与日期先后一致, reviewer 判非错; 仅知悉 |
| B-DS U-5 | `domains/DS/examples.md:212` | p165 Ex10 dm 仅 Row 1/3 | 叙述明载 Not all records are shown, 非 typo |
| B-TR T-4 | `domains/TR/examples.md:44` | p356 PDF r27 NT01 结果/状态全空 | review 裁定 PDF 忠实, 仅登记 (疑 PDF 漏 TRORRES) |
| S-CH10 T-5 | `chapters/ch10_appendices.md:317` | p452 deprecate MO in SDTMIG v3.4 vs p285 in a future version | PDF 内部不一致, 各节照本节 |
| S-TDM TD U-3 | `domains/TD/examples.md:98` | p413 文字 -1 week and + 1 week vs 表 P53D/P9W | PDF 文字与表不一致 |
| S-INT review L-3 | `domains/AG/assumptions.md:5` | p92 §6.1 引言以 ":" 结尾而无列表 | PDF 自身遗漏, KB 照录正确 |
| B-MB O-d | `domains/MB/examples.md` Ex3 Row 4 说明 | "rows 5-7" 而表只有 6 行 | PDF 原文, 照录 |
| B-RE writer | `domains/RE/examples.md:59` | — | 同句 "IRREA1" 与表 REIRREA2: 已由 B-RE T-1 改正, 列此备查 |

## 4. 已裁, 不再提交用户
- 用户规则级裁定 U1-U8 (`t2_post_user_ack.md`): O40/O42 排版字符与 CRF 符号 (U1/U4)、O15/O24/O26/O34 spec 脚注与 CT `*` (U2/U7)、O17/O18/O31/O39/O45/O46/O50 章级引言宿主 (U3)、O24 C-code 记法 (U5)、DOMAIN CT (U6)、Class/Structure 行与 Cross References (U8)。
- 主控已裁: B-MH T-2 改为照录 + T4 (仍在 A1 表); B-CP T-1..T-14 全部 keep-correct (CP review "T4 用户裁定项: 无"); B-TR T-4 PDF 忠实 (review 裁定); S-CH4 #11 "(e.g. 2001-…)" 照 PDF (裁定 4); S-CH10 ② p459 空 bullet 行不落、③ App A 补整表; S-TDM TD U-1 维持照录 + T4 (仍在 A3 表); S-TUFA (1) TR T-5 照录 + T4 (仍在 A2 表)。
- O28 / O32 / O43 / O44 / O52 / O53 / O55 已并入上表 (B-BE O28、B-SM O32、B-MI O43、B-CE T-2、B-SC T-2、B-ch03 T-3/T-4、S-FND UR U-1)。

## 5. 主控待定 (非用户项, 登记时未见裁定记录)
- S-SPREL 需主控定 #3: `chapters/ch10_appendices.md:64-69` §9 引言副本与 DI 顶部重复 (D2 候选: 改一行交叉引用)。
- S-SPREL 需主控定 #4: `domains/SE/assumptions.md:17` PDF `– DTC` 已改 `--DTC` (登记 S-SPREL N-1, keep-correct); 是否归 S-TYPO。
- O51: T2 期间新改 Mermaid (TA/DM/model05/TV/TD) 统一渲染一次。
- O36 / O29 / O57 / O58 / O61: ledger 与原子回写, 属 T3。

## 6. 给 S-TYPO 的 do-not-touch 规则 (由登记推出)
1. 所有 `kb_text_span` 为 do-not-touch: 照录项不得被 "修正", keep-correct 项不得被改回 PDF 字形。
2. **变量前缀 `--` 一律不转 en dash**: PDF 多处把 `--` 印成 `–` (B-ch04/S-CH4 T-9 `--TPTREF`、S-INT EX T-8 `--PRESP`、S-CH10 T-1 `--DRVFL`、S-SPREL N-1 `--DTC`、S-FND PESCAT `–CAT`)。U1 只管引号/破折号/省略号排版, 不含变量记法。
3. 登记 cat=typo-dnt 的 22 行是空格/引号/标点类 keep-correct (如 B-FA T-1 KB 已是 “findings about”, PDF 为两个右引号): 不得按 PDF 字形回退。
4. A4 组未编号照录项 (`codelists .`、`OIVAL .`、`Services;2016`、`Nov, 2021`、人名、ch02 `“--“`、`(e.g. 2001-`、TD `+ 1 week`、AG 重复句) 在用户裁定前保持 PDF 原样。
5. B-IS T-6 / B-TA T-4 / B-MK 范围 dash: 按 U1 改 en dash 是允许的 (见 A6)。

## 7. 统计
复跑: `python3 -c "import json,collections as C;R=[json.loads(l) for l in open('.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl')];print(len(R),C.Counter(r['handling'] for r in R),C.Counter(r.get('cat','-') for r in R))"`
- 登记总行数 269: KB 写正确值 173, 照录+T4 96, 定位失败 0。定位按 `git show HEAD:<file>` 内容 (HEAD b982581); 工作树另有 63 个 spec.md 未提交改动 (他批), 已核本表全部行在 HEAD 与工作树同行同片段。
- 照录+T4 96 行 = A1-A4 决策行 90 + A5 的 S-CH10 T-4 1 + 观察 5; A6 的 2 行属 keep-correct。A5 另列 O 项 / 口径项 14 条 (不在 jsonl)。
- cat 分布: - 210, U1冲突 2, new 3, obs 5, typo-dnt 22, unnum 16, unnum-sp 5, 知悉 6 ('-' = 普通编号项)。
- 状态断言 (锚在表头/行号的 3 项): EX Ex6 24 行 EXENDTC 非空 0; TR Ex2 r26 TRORRES/TRSTAT/TRREASND 全空 (TRDTC 2010-04-02); ch04 lb r7 LBLOBXFL = Y。
- A2 中 TS T-2/T-3/T-4/T-6 的 CT 依据: `grep -rhoE "\| (DOSFRQ|OUTMSPRI|AGEMAX|DOSE) \|[^|]*\|" knowledge_base/terminology` → 4 码各 1 处; PCPP T-7 依据 `terminology/core/other_part3.md:212` C25529 = h。CT 属 KB 术语表, 不是 SDTMIG 正文, 故仍列 T4。
- 新发现 (登记员, 未经 reviewer): REG CP N-1 `GATE and GATEDEF` (p214)、REG SM N-1 SMSEQ 缺 with (p84, SE T-2 镜像)、REG BS N-1 `--ORNLO, --ORNHI` (p198; 同句 --STRNLO 已按 B-BS T-3 改正, 口径不一)。

## 主控补注 (2026-11-26)
- REG 报 "未见裁定" 的两项已有主控裁定: S-SPREL #3 (ch10 §9 引言副本) → S-CH10 已按 D2 换成指向 DI 的交叉引用 (已提交 b80d263); S-SPREL #4 (SE `– DTC`→`--DTC`) → 属变量名前缀修正, 保留在 S-SPREL (已提交 669405f), 不归 S-TYPO。
- O51 Mermaid 统一渲染: 留 T4 (本表 A5 类)。
- REG 新发现 3 条 (未经 reviewer, 记 O62): CP N-1 / SM N-1 / BS N-1 —— 主控建议: BS N-1 与同句 B-BS T-3 统一 (KB 写正确值); SM N-1 与 SE T-2 同型 (照录 + T4); CP N-1 交 T4 核 p214 后定。
- SR T-5 (S-CT 写入) 已由主控补进 `work/t2_pdf_typo_registry.jsonl`。
