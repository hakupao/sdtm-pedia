# T4 U-7 A/B 逐行复核 (t4_user_decisions.md §1 草拟 B 26 行 + §2 B 组 15 行)
> 状态: 审查完成 (2026-11-27), 审查者 pr-review-toolkit:code-reviewer (opus)
<!-- chain: E (plans) -->

- brief: `subagent_prompts/t4/t4_u7_rowcheck_v1.0.md` (+ `t4_common_v1.0.md`). 规则照 brief 套用, 未改规则.
- 每行均用 Read 工具看过渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`; SDTM v2.0 为 `source/cdisc/SDTM_v2.0.pdf`), 页号 = PDF 物理页. KB 行号按当前工作树 (HEAD dc6bb34).
- 单值依据类型: (i) CT 提交值 / (ii) spec 约束 / (iii) 同页表值 / (iv) 语法唯一补法 / 无.
- 路径省略前缀 `knowledge_base/`.

## 1. A1-A3 草拟 B 的 26 行

| 行 | 判定 | 类型 | 决定性依据 | 精确改法 (维持 B 时) |
|---|---|---|---|---|
| A1-9 | 维持 B | (ii) | 渲染 p165 se r1/r5 ETCD=SCREEN、ELEMENT=Screen. SE Assumption 4 (`domains/SE/assumptions.md:37`): 时段要么用一个 planned element, 要么 ETCD="UNPLAN"; planned element 由 TE 定义 (`SE/assumptions.md:11`), 同例 TE p163 / TA p164 "Screen" 的 ETCD 唯一为 SCRN. SE 是引用方, TE 是定义方, 故改 SE 不改 TE | `domains/DS/examples.md:294` 与 `:298` ETCD 格 `\| SCREEN \|` → `\| SCRN \|` (各 1 格, 共 2 格). 全库无其他副本 |
| A1-21 | 维持 B | (i) | 渲染 **p273** (表/registry 写 p271, 页号错) pp r1/r4 PPSTRESU=`H`, 同列其余行 `h`. PPSTRESU 受 PKUNIT 约束 (p272 spec); `terminology/core/other_part3.md:5` PK Units of Measure (C85494), `:212` C25529 提交值 `h`, 该 codelist 无 `H` | `domains/PP/examples.md:16` 与 `:19` PPSTRESU 格 `\| H \|` → `\| h \|` (每行唯一一处 `\| H \|`). 全库无其他副本 |
| A2-2 | 维持 B | (iii) | 渲染 p280 Method A 叙述 "DYIDRGX_A" / "DYIDRGX_HALF" (字母 I); 同页 relrec r3/r5 IDVARVAL = DY1DRGX_A / DY1DRGX_HALF | `domains/PC/examples.md:284` `PPGRPID = "DYIDRGX_A"` → `PPGRPID = "DY1DRGX_A"`; `:285` `PPGRPID = "DYIDRGX_HALF"` → `PPGRPID = "DY1DRGX_HALF"` (表只写 :284, 实际 2 行) |
| A2-3 | 维持 B | (iii) | 渲染 p280 Example 3 引言 PPGRPID = "DYDRGX_HALF"; 同页 relrec r5 = DY1DRGX_HALF (半衰期 PP 记录) | `domains/PC/examples.md:278` `PPGRPID = "DYDRGX_HALF"` → `PPGRPID = "DY1DRGX_HALF"` |
| A2-4 | 维持 B | (i)+(iii) | 渲染 p419 叙述 TSPARMCD = "Dose"; 同页表 DOSE; `terminology/core/trial_design.md:54` C25488 提交值 DOSE | `domains/TS/assumptions.md:43` `TSPARMCD = "Dose"` → `TSPARMCD = "DOSE"` |
| A2-5 | 维持 B (改法须扩到表格) | (i) | 渲染 p419 叙述**和同页表 2 格**都是 DOSFREQ; TSPARMCD CT `trial_design.md:56` C89081 提交值 DOSFRQ, codelist 无 DOSFREQ. 同页表与 CT 冲突, 以 CT 为准 | `domains/TS/assumptions.md:43` `TSPARMCD = "DOSFREQ"` → `TSPARMCD = "DOSFRQ"`; `:48`、`:50` `\| DOSFREQ \|` → `\| DOSFRQ \|`. 共 3 处; 草拟位置只写 :43, registry span 为 [43,48,50]. 若只改 :43, 叙述会和表不一致 |
| A2-6 | 维持 B | (i) | 渲染 p419 Assumption 16 "OUTMSPR" (Primary Outcome Measure); `trial_design.md:103` C98772 提交值 OUTMSPRI | `domains/TS/assumptions.md:57` `TSPARM = "OUTMSPR"` → `TSPARM = "OUTMSPRI"` (同句 "TSPARM =" 本应为 TSPARMCD, 属另一问题, 不在本行; 见 §3) |
| A2-7 | 维持 B | (i) | 渲染 p425 "for the MAXAGE case"; `trial_design.md:35` C49694 提交值 AGEMAX, codelist 无 MAXAGE | `domains/TS/assumptions.md:115` `the MAXAGE case` → `the AGEMAX case` |
| A2-8 | 维持 B | (ii)+(iii) | 渲染 p85 Row 1 "Because this is a partial date, SMDY is not populated." 同页 SM Assumption 3b: "The start study day will not be populated if the start date/time includes only a year…"; 同页表 r1 SMSTDTC=2005-10, SMSTDY 空; Rows 2-3 叙述用 SMSTDY. SM 无 SMDY 变量 | `domains/SM/examples.md:7` `SMDY is not populated` → `SMSTDY is not populated` |
| A2-11 | 维持 B | (ii) | 渲染 p16 "Trials Sets domain"; SDTMIG 全书无其他写法. SDTM v2.0 渲染 p53 §5.1.2 数据集正式名 "Trial Sets" (TX); 只差 1 个字母, 不存在第二个合理名称. 依据来自 SDTM v2.0 的数据集定义, 不是同页值, 裁定方如只认 SDTMIG 本身, 本行属边界 | `chapters/ch02_fundamentals.md:176` `Trials Sets domain` → `Trial Sets domain` |
| A2-12 | **改回 A** | 无 | 渲染 p351 TR TAETORD Notes = "Epoch associated with the date/time at which the assessment was made." 候选来自其他域 (跨页), 且 KB 各域 TAETORD Notes 至少有两种常用写法: "…within the arm." 16 处, "…for the element in which the assessment was made." 15 处 (`grep -A7 "^### TAETORD" domains/*/spec.md`); TR 属 Findings, 后一种同样合理 → 不单值, 且属整句改写 | — |
| A2-14 | 维持 B | (ii) | 渲染 p198 BS Assumption 5 "--ORNLO, --ORNHI"; SDTM 无此变量, 对应变量为 --ORNRLO/--ORNRHI (同句 --STRNLO 已按 T-3 改为 --STNRLO, 列表顺序与 --STNRLO/--STNRHI 平行) | `domains/BS/assumptions.md:23` `--ORNLO, --ORNHI` → `--ORNRLO, --ORNRHI` |
| A2-15 | 维持 B | (iii) | 渲染 p281 Method B 两句 "includes PP records with PCSEQ values"; 同页 relrec r1-12 / r14-23 RDOMAIN=PC, IDVAR=PCSEQ | `domains/PC/examples.md:299` 与 `:300` `includes PP records with PCSEQ values` → `includes PC records with PCSEQ values` (2 处; 表只写 :299) |
| A2-16 | 维持 B (**草拟候选值错, 须更正**) | (iii) | 渲染 p281 Method C 两句 "all PP records with PGRPID value(s) "DY1_DRGX_A"…"; 同页 relrec r1/r2/r8 为 RDOMAIN=**PC**, IDVAR=**PCGRPID**, 标题 "Using PCGRPID and PPSEQ". 草拟候选 "PPGRPID" 与同页表矛盾, 是错值 | `domains/PC/examples.md:333` `all PP records with PGRPID values` → `all PC records with PCGRPID values`; `:334` `all PP records with PGRPID value` → `all PC records with PCGRPID value`. 2 处都要改 PP→PC; 若裁定方不接受同时改 "PP", 则本行应改回 A |
| A3-2 | 维持 B | (iv) | 渲染 p160 "The relationship between the DS record and in the AE record was represented"; "between X and Y" 只容名词短语, 只能删 in | `domains/DS/examples.md:87` `the DS record and in the AE record` → `the DS record and the AE record` |
| A3-5 | 维持 B | (iii) | 渲染 p190 Ex2 "interpretations performed by the principal investigation"; 同页表 r1-4 EGEVAL = PRINCIPAL INVESTIGATOR | `domains/EG/examples.md:42` `principal investigation` → `principal investigator` |
| A3-7 | 维持 B | (iv) | 渲染 p362 末段 "to which they are thought be related"; 只能补成 thought to be | `domains/FA/assumptions.md:39` `thought be related` → `thought to be related` |
| A3-8 | 维持 B | (iv) | 渲染 p363 "If so, FA may provided a clearer representation…"; 前后句为现在时 (may … would also allow), 只能改 provide | `domains/FA/assumptions.md:51` `FA may provided` → `FA may provide` |
| A3-9 | 维持 B | (iv) | 渲染 p372 "The visit date was used to populated FADTC." | `domains/FA/examples.md:183` `used to populated FADTC` → `used to populate FADTC` |
| A3-14 | 维持 B | (iv) | 渲染 **p285** (表/registry 写 p294, 页号错) §6.3.7.1 "domains may included additional expected variables" | `domains/NV/assumptions.md:23` `may included` → `may include`. 全库只有这一处 |
| A3-15 | 维持 B | (iv) | 渲染 **p298** 首行 (表/registry 写 p297; p297 末行到 "may have an") "NVGRPID links the each VEP component" | `domains/NV/examples.md:63` `links the each` → `links each` |
| A3-24 | **改回 A** | 无 | 渲染 p407 表 r2/r4 TESTRL "First dose of treatment in Element, …", 同页叙述 "First dose of treatment Element, …". 两种写法都合语法; 去 in 的理由是 "3:2 多数" (另有 `TE/examples.md:43-44`、`DS/examples.md:345-346` 无 in), 属多数写法 + 跨例, 且也可以反过来给叙述补 in | — |
| A3-28 | **改回 A** | 无 | 渲染 p457 §6.4.1 "The new criterion added in version the underwent the first public review"; 至少有 "in the version that underwent" / "in the version which underwent" / "in version that underwent" 几种改法, 要改 2 个词, 不是单值补法 (草拟依据栏也写了 "正确词无依据") | — |
| A3-31 | **改回 A** | 无 | 渲染 p79 SESEQ "Should be assigned to be consistent chronological order."; 已有原文的补法不止一种: SDTMIG p81 SE Assumption 5 "consistent with the chronological order"; SDTM v2.0 渲染 p46 SE SESEQ "to be in a consistent chronological order"; v2.0 p49 SM "consistent with chronological order" → 不是只有一种补法 | — |
| A3-32 | **改回 A** (随 A3-31) | 无 | 渲染 p84 SMSEQ 同句缺词. 理由同 A3-31. 注: SDTM v2.0 p49 SM 同变量 Notes 逐字为 "Should be assigned to be consistent with chronological order", 但这是另一份文件, 不属于 i-iv 中任何一类 | — |
| A3-34 | 维持 B | (iv) | 渲染 p41 §4.4.3.2 "solidus or foreword slash [/]"; 拼写错, 只有 forward 一种 | `chapters/ch04_general_assumptions.md:863` `foreword slash` → `forward slash` |

## 2. B 组 15 行 (KB 已写正确值)

| 行 | 判定 | 类型 | 决定性依据 | 否决回退 (否决时) |
|---|---|---|---|---|
| B-1 | 维持 | (iii) | 渲染 p142 Ex5 Row 2 "…as the AE was probably related to the event."; 同页表 r2 AERLDEV=PROBABLE, AEACNDEV=REMOVED, AERLPRC=N, AERLPRT=N → 唯一的 "probable" 相关对象是 device. KB `domains/AE/examples.md:75` 已为 device | — |
| B-2 | 维持 | (iv) | 渲染 p237 Ex7 "a subject participating a vaccine study"; 只能补 in (这条就是 brief 给的口径基准). KB `domains/IS/examples.md:153` | — |
| B-3 | 维持 | (iv) | 渲染 p296 "based on an fluorodeoxyglucose (FDG)-PET scan"; 全拼词以辅音 /f/ 开头, 只能用 a. KB `domains/NV/examples.md:11` | — |
| B-4 | 维持 | (iv) | 渲染 p10 "but for which a codelist not yet been developed."; 只能补 has (这条也是 brief 给的口径基准). KB `chapters/ch01_introduction.md:85` | — |
| B-5 | 维持 | (iii)+(iv) | 渲染 p10 §1.5 同段: --LNKID "used to identify a record", --LNKGRP "a group of records"; ONE 句为 --LNKID, MANY 句也印 "--LNKID (and not --LNKGRP)". 按同段定义, MANY 句只能是两名对调. KB `chapters/ch01_introduction.md:109` | — |
| B-6 | 维持 | (iii) | 渲染 p118 "Rows 1, 3, 5: …dose levels (mg/kg)… Scheduled dose is represented in mg/mL."; 同句括注 + 同页表 r1/r3/r5 ECDOSU=mg/kg. KB `domains/EX/examples.md:362` | — |
| B-7 | 维持 | (ii) | 渲染 p199 "--BNDAGT (Binding Agent)… --GATEDEF (Gate Definition)", p200 "--GATE and --GATEDEF", p206 "CPBNDAGT". PDF 的 CP spec 只有 CPBDAGNT (p201)、CPGATDEF (p202); KB `domains/CP/spec.md:149/185`. KB `domains/CP/assumptions.md:24/:42/:72` 已改; 全库已无 BNDAGT | — |
| B-8 | 维持 (T-7、T-9 都维持) | (iii) | T-7: 渲染 p370 "linked to the parent CE record via the AE reference number… AESPID and FASPID"; 同页 ae.xpt + relrec RDOMAIN=AE/IDVAR=AESPID → 只能是 AE. T-9: 渲染 p373 叙述 FAEVINTX; 同页 face.xpt 列名 FAEVLINT, 值 -PT24H (ISO 时长, 符合 FAEVLINT). KB `domains/FA/examples.md:118/:228` | — |
| B-9 | 维持 | (ii)+(iii) | 渲染 p262 suppms RDOMAIN=MS, IDVAR=MBREFID, IDVARVAL 100.4/100.5; 同页 ms.xpt 的 MSREFID 列就是 100.4/100.5, IDVAR 须为 RDOMAIN 中的变量. KB `domains/MS/examples.md:80-81` | — |
| B-10 | 维持 | (i)+(iii) | 渲染 p421 Ex2 r1 TSPARMCD=TITLE, TSPARM "Trial Type"; 同页 "Row 1: Shows the trial title."; TSPARM CT C67152 `terminology/core/trial_design.md:281` C49802 = "Trial Title". KB `domains/TS/examples.md:76` | — |
| B-11 | 维持 (T-1、T-2 都维持) | (ii)+(iii) | 渲染 p18 Keys. T-2: FT 行 "TESTCD, VISITNUM, FTTPTREF, FTTPTNUM", 前缀只能是 FT. T-1: BE 行 "BESDTC". 拼写上与 BESTDTC、BEDTC 都只差 1 个字母; 但 BE Assumption 5b (`domains/BE/assumptions.md:27`) 说 BEDTC 是标本采集时间, 同一 BEREFID 下不变, 不能区分 "per instance per biospecimen event", 不能作 key; 同页 Events 行 key 都是 --STDTC → BESTDTC. KB `chapters/ch03_submitting_data.md:37/:49` | — |
| B-12 | 维持 | (iv) | 渲染 p64 脚注² "…2016. Accessed January 8, 2020. https://…/ucm126396.pdf)": 全句没有开括号. 删去孤立的 ")" 只有一种改法; 补 "(" 则可放在 URL / Accessed / 2020 前等多个位置, 不唯一. 该脚注为 AMA 体例, URL 本来不加括号. KB `domains/DM/spec.md:296` | — |
| B-13 | 维持 | (iii) | 渲染 p166 te r3 "where treatment AB +C"; 同页 r2 平行句 "where treatment is AB". KB `domains/DS/examples.md:346` | — |
| B-14 | 维持 | (ii)+(iii) | 渲染 p215 叙述 "CPCSMRKR"; 同页 cp.xpt 列名 CPCSMRKS. 渲染 p211 叙述 "Gate Definition (CPGATEDEF)"; 同页表列名 CPGATDEF; spec p202 CPGATDEF. KB `domains/CP/examples.md:202`、`:71` 等; 全库已无 CSMRKR, CPGATEDEF 也已清零 (`CP/examples.md:171` 的 "GATEDEF" 属 A2-13, 不在本行) | — |
| B-15 | 维持 | (iv) | 渲染 p293 r3 MKREASND 单元格在 "REPLACEMENT/" 后折行 (bbox `work/pdf_bbox/ig34_p0293.tsv`: "REPLACEMENT/" 与 "SURGICAL" 分在两行); p294 r12 同值 bbox 为一个整词 "REPLACEMENT/SURGICAL". 所谓空格是折行造成的, KB `domains/MK/examples.md:53/:62` 两格一致 | — |

## 3. 计数
- A1-A3 (26 行): **维持 B 21 / 改回 A 5** (A2-12, A3-24, A3-28, A3-31, A3-32). 维持 B 中 A2-5 (改法须扩到 :48/:50)、A2-16 (候选值须更正) 不能照草拟直接执行.
- B 组 (15 行): **维持 15 / 否决 0**.

## 4. 顺手发现 (不修)
1. 页号错 (表与 registry 同错): A1-21 / B-PCPP T-7 实为 p273 (不是 p271); A3-14 / B-NV N-1 实为 p285 (不是 p294); A3-15 / B-NV N-2 实为 p298 (不是 p297).
2. A1-21 依据栏写 "UNIT CT C25529" 不准: PPSTRESU 的 codelist 是 PKUNIT (C85494, `other_part3.md:5`), C25529 是其中的 term code.
3. 草拟位置漏了副本: A2-2 漏 :285; A2-5 漏 :48/:50; A2-15 漏 :300; A2-16 漏 :334 (registry 的 span [333,427,432] 中 427/432 匹配的是 "PPGRPID values", 是正常文字, 不是副本).
4. A2-6 同句 PDF 用 `TSPARM = "OUTMSPR"` 写参数码 (同段 OUTMSSEC/OUTMSEXP/OUTMSADD 也一样), 严格应为 TSPARMCD; 未登记. 是否处理由裁定方定 (本复核不评).
5. A3-31/A3-32: 如果裁定方以后把 SDTM v2.0 同变量 Notes 也算单值依据, SM 可单值定为 "consistent with chronological order" (v2.0 p49), SE 在 v2.0 却是 "in a consistent chronological order" (p46), 两处结果不同.
6. A1-9 是本表最弱的维持 B: spec 只要求 SE.ETCD 与 TE 一致, 不规定改哪一边; 判改 SE 依赖 "TE 为定义方" 的方向性. 裁定方如只认同页依据, 应改回 A.
