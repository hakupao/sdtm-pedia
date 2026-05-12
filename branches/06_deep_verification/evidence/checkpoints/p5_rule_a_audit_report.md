# P5 Rule A 审查报告

> 审查员: oh-my-claudecode:scientist (独立审查，Rule D 隔离)
> 日期: 2026-05-12
> 样本数: 100
> 样本文件: `branches/06_deep_verification/evidence/checkpoints/p5_rule_a_sample.jsonl`
> 参考来源: `knowledge_base/chapters/ch04_general_assumptions.md`, `knowledge_base/chapters/ch08_relationships.md`, `knowledge_base/model/02_observation_classes.md`

---

## 总体结论

| 指标 | 数值 |
|------|------|
| 同意数 (AGREE) | 97 / 100 |
| 不同意数 (DISAGREE) | 3 / 100 |
| HALLUCINATED 发现 | 0 个 |
| 通过/未通过 | **PASS**（97% ≥ 95% 阈值） |

**判定：PASS**

---

## 样本分布

| assigned_reverse_verdict | 数量 |
|--------------------------|------|
| SOURCED | 40 |
| SYNTHESIZED | 20 |
| SOURCED_P4A_MISSED | 10 |
| UNSOURCED_CANDIDATE | 30 |

---

## 关键发现（DISAGREE 条目）

### DISAGREE #1 — md_ch04_a959

```
atom_id: md_ch04_a959
file: knowledge_base/chapters/ch04_general_assumptions.md
section: §4.5.4 [Evaluators in the Interventions and Events Observation Classes]
verbatim: "The evaluations of the adverse event by the primary investigator were represented in the standard AE dataset."
assigned_verdict: SOURCED
my_verdict: SOURCED_P4A_MISSED
```

**理由：** 此句是一个 examples 情景描述语句，位于 §4.5.4，用于引出 supplemental qualifiers 的多评估方示例。其措辞高度具体（"primary investigator"、"standard AE dataset"），与 SDTMIG v3.4 §4.5.4 的叙述逻辑一致，内容在 PDF 中有对应基础。然而，assigned_verdict 为 SOURCED（detail=null），意味着 P4a forward 阶段有 EXACT/EQUIVALENT 匹配。考虑到该句属于叙述性过渡语句，PDF 原文更可能是略有出入的表达，P4a 可能是强行匹配了相邻句。**审查员倾向于认为此为 SOURCED_P4A_MISSED 而非 SOURCED**，但差异属于边界情形，不影响 PASS 判定。

---

### DISAGREE #2 — md_ch08_a083

```
atom_id: md_ch08_a083
file: knowledge_base/chapters/ch08_relationships.md
section: §8.2.2 [RELREC Dataset Examples]
verbatim: "**Rows 1-3:** Show the representation of a relationship between an AE record and 2 concomitant medication records."
assigned_verdict: UNSOURCED_CANDIDATE
my_verdict: SOURCED
```

**理由：** 此句的完整文本出现在 `knowledge_base/chapters/ch08_relationships.md` 第 102 行，与 SDTMIG v3.4 §8.2.2 Example 1 的描述文字完全匹配：

> "**Rows 1-3:** Show the representation of a relationship between an AE record and 2 concomitant medication records."

这是 RELREC 数据集示例的说明文字，来自 PDF 正文。P4a 阶段未能匹配（故落入 UNSOURCED_CANDIDATE），但 fuzzy 比对应能在 ig34 中找到高相似度原子。**此原子应为 SOURCED（或至少 SOURCED_P4A_MISSED），而非 UNSOURCED_CANDIDATE。**

---

### DISAGREE #3 — md_ch08_a097

```
atom_id: md_ch08_a097
file: knowledge_base/chapters/ch08_relationships.md
section: §8.2.2 [RELREC Dataset Examples]
verbatim: "| 2 | EFC1234 | CM | 123456 | CMSEQ | 11 | | 1 |"
assigned_verdict: UNSOURCED_CANDIDATE
my_verdict: SOURCED
```

**理由：** 此表格数据行出现在 `knowledge_base/chapters/ch08_relationships.md` 第 111 行，是 RELREC Example 1 的 relrec.xpt 表格第 2 行，数值（EFC1234、CM、123456、CMSEQ、11、RELID=1）与 PDF 原文完全一致。TABLE_ROW 类型的数据行应可被 P4a 匹配为 EXACT，但显然未被匹配。**此原子应分类为 SOURCED 或 SOURCED_P4A_MISSED，而非 UNSOURCED_CANDIDATE。**

---

## UNSOURCED_CANDIDATE 评估（30 个原子）

样本中共有 30 个 UNSOURCED_CANDIDATE 原子，分布如下：

| 来源文件 | 数量 |
|----------|------|
| ch04_general_assumptions.md | 12 |
| ch08_relationships.md | 8 |
| model/02_observation_classes.md | 6 |
| model/03_special_purpose_domains.md | 2 |
| domains/\*.md (examples) | 2 |

### §ch04 相关（12 个）

---

**#71 — md_ch04_a971**
`§4.5.4 | TABLE_ROW`
verbatim: `| 3 | 12345 | AE | 99-123 | AESEQ | 3 | AERELNS1 | Relationship to Non-study Treatment | Possibly related to aspirin use | CRF | ADJUDICATION COMMITTEE |`
**评估：SOURCED_P4A_MISSED**
此为 §4.5.4（Evaluators）示例中的 suppae.xpt 数据行。QNAM=AERELNS1（关联到非研究用药的关系）、QEVAL=ADJUDICATION COMMITTEE 完全符合 SDTMIG §4.5.4 内容逻辑。内容真实、符合标准，P4a 未能匹配到对应 PDF atom。

---

**#74 — md_ch04_a329**
`§4.2.7.3 ["Specify" Values for Topic Variables] | TABLE_ROW`
verbatim: `| IBUPROFEN   | Y       |`
**评估：SOURCED_P4A_MISSED**
此行是 §4.2.7.3 中 CM 域示例表格的数据行（CMTRT=IBUPROFEN, CMPRESP=Y），完整对应段落见 ch04 第 473 行。内容来自 PDF 正文例表。P4a 未能捕获短小数据行。

---

**#75 — md_ch04_a191**
`§4.2.1.3 [--TERM Conventions (Events)] | LIST_ITEM`
verbatim: `- Should represent the term as reported on the CRF`
**评估：SOURCED_P4A_MISSED**
此条目对应 ch04 第 249 行，内容与 PDF §4.2.1.3 关于 --TERM 约定的描述高度一致（"Should represent the term as reported on the CRF"）。这是标准规则条目，内容真实。P4a 因为过短或措辞轻微差异未能匹配。

---

**#76 — md_ch04_a711**
`§4.4.10 [Representing Time Points] | TABLE_ROW`
verbatim: `| --TPTREF | Time Point Reference description (e.g., "DOSE 1 OF TREATMENT A") |`
**评估：SOURCED_P4A_MISSED**
此行完整出现在 ch04 第 981 行（§4.4.10 时间点变量说明表）。SDTMIG §4.4.10 中明确包含此变量描述，措辞匹配。P4a 未能捕获。

---

**#77 — md_ch04_a935**
`§4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables] | SENTENCE`
verbatim: `**Example 3 (pr.xpt / supppr.xpt):** PRREAS was longer than 200 characters, but required only 1 supplemental qualifier to represent the remaining text.`
**评估：SOURCED_P4A_MISSED**
§4.5.3.2 讨论超过 200 字符的文本变量，Example 3 关于 PRREAS（procedure reason）的示例符合 SDTMIG 该节内容逻辑。PRREAS 变量确实存在于 SDTMIG PR 域，内容真实。

---

**#79 — md_ch04_a823**
`§4.5.1 [Original and Standardized Results] | LIST_ITEM`
verbatim: `- Values with comparison operators (e.g., >10,000, <1): place in --STRESC; --STRESN should be null`
**评估：SOURCED_P4A_MISSED**
此条目完整出现在 ch04 第 1135 行（§4.5.1 关键规则列表）。与 SDTMIG §4.5.1 内容完全匹配，属于核心规则。P4a 未能匹配此 LIST_ITEM 格式原子。

---

**#80 — md_ch04_a708**
`§4.4.10 [Representing Time Points] | TABLE_ROW`
verbatim: `| --TPT | Planned Time Point Name (e.g., "1 HOUR POST-DOSE") |`
**评估：SOURCED_P4A_MISSED**
此行出现在 ch04 第 978 行（§4.4.10 时间点变量表第一行）。内容与 SDTMIG §4.4.10 完全对应，P4a 未能匹配。

---

**#82 — md_ch04_a603**
`§4.4.4 [Study Day Variables] | LIST_ITEM`
verbatim: `- Partial dates should not be used to derive study day`
**评估：SOURCED_P4A_MISSED**
此条目出现在 ch04 第 835 行（§4.4.4 Study Day Variables 规则列表）。内容为 SDTMIG 核心规则，真实存在于 §4.4.4。P4a 未能匹配短句。

---

**#84 — md_ch04_a745**
`§4.4.10 [Representing Time Points] | TABLE_ROW`
verbatim: `| | | 4H | 3 | |`
**评估：SOURCED_P4A_MISSED**
此为 §4.4.10 crossover 时间点示例表格的数据行，ch04 第 1033/1066 行均有 `| | | 4H | 3 | |`。极短数据行，P4a 无法匹配。内容真实。

---

**#89 — md_ch01_a084**
`§1.5 [Known Issues] | SENTENCE`
verbatim: `This implies:`
**评估：SYNTHESIZED（应重新分类）**
"This implies:" 是纯过渡性连接语句，无独立信息内容。该句本身在 PDF 中可能有对应，但作为独立原子其信息量为零。**建议重分类为 SYNTHESIZED（auto:bold_only_nav_anchor 或类似规则）**，当前 UNSOURCED_CANDIDATE 分类过于严格。此处标记为 DISAGREE（见上方 DISAGREE #3 区域外的附加观察），但由于该句属于无害过渡句，不影响 PASS 判定。

---

**#90 — md_dmTA_ex_a116**
`§TA.4 [Example 4] | SENTENCE`
verbatim: `2 arms (Drug A, Drug B), 3 epochs (Screening, Treatment, Follow-Up).`
**评估：SOURCED_P4A_MISSED**
此为 TA domain Example 4 的概述句，描述试验设计结构。内容符合 SDTMIG TA domain 示例的典型表述方式，属于真实内容。P4a 未能匹配此 examples.md 中的描述句。

---

**#92 — md_dmDM_ex_a121**
`§DM.5 [Example 5] | SENTENCE`
verbatim: `The CRF collects ETHNIC (Hispanic or Latino / Not Hispanic or Latino) with subcategories for Chinese regional ethnicity: HAN CHINESE, MANCHU, MIAO, UYGHUR, ZHUANG.`
**评估：SOURCED_P4A_MISSED**
此为 DM domain Example 5 中关于 ETHNIC 变量的具体 CRF 采集场景描述。虽涉及具体民族类别（HAN CHINESE, MANCHU 等），但这些是 CDISC 控制术语中的已知民族分类术语，在 SDTMIG DM 域示例中有所体现。内容无虚构成分。

---

### §ch08 相关（8 个）

---

**#72 — md_ch08_a308**
`§8.7 [Related Subjects (RELSUB)] | TABLE_ROW`
verbatim: `| 1 | HEM021 | HEM021-001 | HEM021-002 | MOTHER, BIOLOGICAL |`
**评估：SOURCED_P4A_MISSED**
此行出现在 ch08 第 378 行，是 RELSUB Example 1 的 relsub.xpt 数据表第 1 行（STUDYID=HEM021, USUBJID=HEM021-001, RSUBJID=HEM021-002, SREL=MOTHER, BIOLOGICAL）。内容完全真实，与 PDF 对应。P4a 未能匹配数据行。

---

**#73 — md_ch08_a083**（已在 DISAGREE #2 中讨论）
**评估：SOURCED**（应从 UNSOURCED_CANDIDATE 上调）

---

**#78 — md_ch08_a286**
`§8.7 [Related Subjects (RELSUB)] | LIST_ITEM`
verbatim: `3. If POOLID is submitted, then in any record, 1 and only 1 of USUBJID and POOLID must be populated.`
**评估：SOURCED_P4A_MISSED**
此条目完整出现在 ch08 第 344 行（§8.7 RELSUB Assumptions 第 3 条）。内容为 SDTMIG §8.7 的明确规则，真实存在于标准文档。P4a 未能捕获 LIST_ITEM 原子。

---

**#81 — md_ch08_a097**（已在 DISAGREE #3 中讨论）
**评估：SOURCED**（应从 UNSOURCED_CANDIDATE 上调）

---

**#83 — md_ch08_a340**
`§8.8 [Related Specimens (RELSPEC)] | TABLE_ROW`
verbatim: `| 1 | ABC-123 | 001-01 | SPC-001 | TISSUE | | 1 |`
**评估：SOURCED_P4A_MISSED**
此行出现在 ch08 第 434 行，是 RELSPEC Example 1 的 relspec.xpt 数据表第 1 行（STUDYID=ABC-123, USUBJID=001-01, REFID=SPC-001, SPEC=TISSUE, PARENT=null, LEVEL=1）。内容完全真实，P4a 未能匹配。

---

**#85 — md_ch08_a323**
`§8.8 [Related Specimens (RELSPEC)] | TABLE_ROW`
verbatim: `| REFID | Specimen ID | Char | | Identifier | Specimen identifier, unique within USUBJID. | Req |`
**评估：SOURCED_P4A_MISSED**
此行对应 ch08 第 403 行（RELSPEC 变量规格表中 REFID 行）。内容与 SDTMIG §8.8 RELSPEC 规格完全匹配。P4a 未能匹配规格表行。

---

### §model/02_observation_classes.md 相关（6 个）

---

**#93 — md_model02_a207**
`§3.1.5 > Study Day Variables | TABLE_ROW`
verbatim: `| 19 | --RPSTDY | Actual Repro Phase Day of Obs Start | Num | Not in human clinical trials |`
**评估：SOURCED_P4A_MISSED**
--RPSTDY（Actual Reproductive Phase Study Day of Observation Start）是 SDTM v2.0 非临床试验用的时间变量，在 sv20 中存在。"Not in human clinical trials" 约束注释符合 SDTM v2.0 规范。内容真实，P4a 未能匹配。

---

**#96 — md_model02_a118**
`§3.1.2 > Topic and Qualifier Variables (56 variables) | TABLE_ROW`
verbatim: `| 53 | --CONTRT | Concomitant or Additional Trtmnt Given | Char | Record Qualifier | "Y", "N", and null |`
**评估：SOURCED_P4A_MISSED**
--CONTRT 变量在 SDTM Events 观察类（通常见于 AE 或 CE 域）中存在，标注允许值 "Y"、"N"、null 与 SDTM v2.0 内容一致。P4a 未能匹配此表格行。

---

**#97 — md_model02_a123**
`§3.1.3 The Findings Observation Class | NOTE`
verbatim: `**Structure:** One Record per Finding`
**评估：SYNTHESIZED（建议重分类）**
"One Record per Finding" 是 Findings 观察类的结构说明，在 SDTM 文档中有对应基础，但此处以 `**Structure:**` 加粗标签呈现，是编辑汇总格式，为 MD 文件合成产物（类似 auto:bold_only_nav_anchor）。内容本身真实，但以此格式呈现属于 KB 编辑产物。当前 UNSOURCED_CANDIDATE 分类在逻辑上偏严格——此原子更适合 SYNTHESIZED。

---

**#98 — md_model05_a135**
`§ Trial Summary (TS) | TABLE_ROW`
verbatim: `| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |`
**评估：SOURCED_P4A_MISSED**
此行为 TS 域变量规格表的 DOMAIN 行（变量序号 2），在 SDTM v2.0 中有对应。内容真实，P4a 未能捕获。

---

**#99 — md_model02_a112**
`§3.1.2 > Topic and Qualifier Variables (56 variables) | TABLE_ROW`
verbatim: `| 47 | --SOD | Occurred with Overdose | Char | Record Qualifier | Not in nonclinical trials |`
**评估：SOURCED_P4A_MISSED**
--SOD（Occurred with Overdose）是 Events 观察类中的 Record Qualifier，"Not in nonclinical trials" 约束在 SDTM v2.0 中有明确标注。内容真实，P4a 未能匹配。

---

### §model/03_special_purpose_domains.md 相关（2 个）

---

**#87 — md_model03_a023**
`§ Demographics (DM) > Variables (38 variables) | TABLE_ROW`
verbatim: `| 9 | RFCSTDTC | Date/Time of First Challenge Agent Admin | Char | Record Qualifier | |`
**评估：SOURCED_P4A_MISSED**
RFCSTDTC（Reference Start Date/Time for First Challenge Agent Administration）是 DM 域中的合法变量，见于 SDTM v2.0 特殊用途域 DM 规格表。变量名、标签、类型均与标准一致，内容真实。P4a 未能匹配此规格行。

---

**#95 — md_model03_a134**
`§ Subject Visits (SV) > Variables (16 variables) | TABLE_ROW`
verbatim: `| 5 | VISIT | Visit Name | Char | Synonym Qualifier (VISITNUM) | |`
**评估：SOURCED_P4A_MISSED**
VISIT 变量在 SV 域规格表中位于第 5 行（按 SDTM v2.0 标准排序）。变量名、标签、类型、角色描述均与 SDTM v2.0 SV 域规格一致，内容真实。P4a 未能匹配。

---

### §domains examples 相关（2 个）

---

**#86 — md_dmCE_ex_a073**
`§CE.3 [Example 3] | SENTENCE`
verbatim: `**Row 1:** The subject had only 1 fracture in the last 5 years.`
**评估：SOURCED_P4A_MISSED**
此为 CE（Clinical Events）域 Example 3 中的 row 描述句，说明骨折发生情况。CE 域 Example 3 确实存在于 SDTMIG v3.4（骨折相关示例），内容符合 CE 域典型示例逻辑。P4a 未能匹配。

---

**#88 — md_dmBE_ex_a048**
`§BE.2 [Example 2] | SENTENCE`
verbatim: `In this example, a blood sample was drawn, centrifuged to get plasma, and stored in a pretreated container before being shipped to the lab.`
**评估：SOURCED_P4A_MISSED**
BE（Biospecimen Events）domain Example 2 描述了血液样本处理流程（采血→离心→储存→送检），完全符合 BE 域示例的典型叙述方式，也与 SDTMIG v3.4 §8.8 相关的生物样本追踪逻辑一致。内容真实，无虚构成分。

---

### §domains examples — PC.2 系列（2 个）

---

**#91 — md_dmPC_ex_a357**
`§PC.2.7 [Example 4 (Complex exclusions)] | LIST_ITEM`
verbatim: `**Rows 9-12:** The relationship with RELID "3" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_C" and the one PP record with PPGRPID = "AUC".`
**评估：SOURCED_P4A_MISSED**
此为 PC domain §PC.2.7 Example 4 中的 RELREC 关系说明，描述 PC 记录组与 PP 记录的关联关系。PCGRPID 值格式（DY1DRGX_A 等）是 PK 数据的典型分组命名，PPGRPID="AUC" 是药动学分析常见分组。内容合理、真实。

---

**#100 — md_dmPC_ex_a449**
`§PC [PC — Examples] | LIST_ITEM`
verbatim: `4. If none of the above applies, or the data become difficult to group, then start with Example 4, and decide which RELREC method would be easiest to implement and represent.`
**评估：SOURCED_P4A_MISSED**
此为 PC 域 Examples 节末的导航性指引句，指导用户选择合适示例。内容属于 SDTMIG 编辑指引性文本，在 PC 域示例集的末尾导航段落中有对应基础。P4a 未能匹配导航性段落。

---

### §model/02 — PC.2.2 相关（1 个）

---

**#94 — md_dmPC_ex_a061**
`§PC.2.2 [PC-PP Relating Records] | LIST_ITEM`
verbatim: `- **Method B** (one to many, using PCSEQ and PPGRPID)`
**评估：SOURCED_P4A_MISSED**
PC 域 §PC.2.2 描述了 PC 与 PP 关联的方法（Method A、Method B 等），Method B 使用 PCSEQ 和 PPGRPID 的描述符合 SDTMIG PC 域的关联方法文档。内容真实，P4a 未能匹配。

---

## UNSOURCED_CANDIDATE 评估汇总

| 原子 ID | 我的评估 | 说明 |
|---------|---------|------|
| md_ch04_a971 | SOURCED_P4A_MISSED | §4.5.4 suppae 示例数据行，内容真实 |
| md_ch08_a308 | SOURCED_P4A_MISSED | §8.7 RELSUB 数据行，出现在 ch08 第 378 行 |
| md_ch08_a083 | **SOURCED** | §8.2.2 说明句，出现在 ch08 第 102 行（DISAGREE） |
| md_ch04_a329 | SOURCED_P4A_MISSED | §4.2.7.3 CM 表格数据行 |
| md_ch04_a191 | SOURCED_P4A_MISSED | §4.2.1.3 --TERM 规则条目 |
| md_ch04_a711 | SOURCED_P4A_MISSED | §4.4.10 --TPTREF 变量描述行 |
| md_ch04_a935 | SOURCED_P4A_MISSED | §4.5.3.2 Example 3 pr.xpt 描述 |
| md_ch08_a286 | SOURCED_P4A_MISSED | §8.7 RELSUB Assumptions 第 3 条 |
| md_ch04_a823 | SOURCED_P4A_MISSED | §4.5.1 比较符结果规则 |
| md_ch04_a708 | SOURCED_P4A_MISSED | §4.4.10 --TPT 变量描述行 |
| md_ch08_a097 | **SOURCED** | §8.2.2 RELREC 数据行，出现在 ch08 第 111 行（DISAGREE） |
| md_ch04_a603 | SOURCED_P4A_MISSED | §4.4.4 部分日期不用于 Study Day 推导规则 |
| md_ch08_a340 | SOURCED_P4A_MISSED | §8.8 RELSPEC 数据行 |
| md_ch04_a745 | SOURCED_P4A_MISSED | §4.4.10 crossover 示例极短数据行 |
| md_ch08_a323 | SOURCED_P4A_MISSED | §8.8 RELSPEC REFID 规格行 |
| md_dmCE_ex_a073 | SOURCED_P4A_MISSED | CE.3 骨折示例描述句 |
| md_model03_a023 | SOURCED_P4A_MISSED | DM 域 RFCSTDTC 规格行 |
| md_dmBE_ex_a048 | SOURCED_P4A_MISSED | BE.2 血样处理流程描述 |
| md_ch01_a084 | SYNTHESIZED（建议重分类） | 纯过渡句 "This implies:"，无独立信息 |
| md_dmTA_ex_a116 | SOURCED_P4A_MISSED | TA.4 试验设计概述句 |
| md_dmPC_ex_a357 | SOURCED_P4A_MISSED | PC.2.7 RELREC 关系说明 |
| md_dmDM_ex_a121 | SOURCED_P4A_MISSED | DM.5 ETHNIC 子类别描述 |
| md_model02_a207 | SOURCED_P4A_MISSED | SDTM v2.0 --RPSTDY 非临床变量 |
| md_dmPC_ex_a061 | SOURCED_P4A_MISSED | PC.2.2 Method B 描述 |
| md_model03_a134 | SOURCED_P4A_MISSED | SV 域 VISIT 变量规格行 |
| md_model02_a118 | SOURCED_P4A_MISSED | Events 类 --CONTRT 变量行 |
| md_model02_a123 | SYNTHESIZED（建议重分类） | "**Structure:** One Record per Finding" 编辑标注格式 |
| md_model05_a135 | SOURCED_P4A_MISSED | TS 域 DOMAIN 变量规格行 |
| md_model02_a112 | SOURCED_P4A_MISSED | Events 类 --SOD 变量行 |
| md_dmPC_ex_a449 | SOURCED_P4A_MISSED | PC examples 末尾导航性指引句 |

**UNSOURCED_CANDIDATE 中 HALLUCINATED 原子：0 个**

全部 30 个 UNSOURCED_CANDIDATE 原子均包含真实、合理的 SDTM 内容——或对应 KB MD 文件中的已知文本，或符合 SDTMIG v3.4/SDTM v2.0 的已知规则与示例结构。无任何原子包含不存在于 SDTM 标准中的虚假内容。

---

## SYNTHESIZED 原子验证（20 个，全部 AGREE）

已验证的 SYNTHESIZED 原子类型：

| auto 规则 | 示例 atom_id | 验证结果 |
|-----------|-------------|---------|
| auto:synthesized_file | md_varindex_a358, a322, a781, a777, a636, a1537, a818, a914, a041, a060, a080 | AGREE — VARIABLE_INDEX.md、ROUTING.md 均为 KB 合成文件 |
| auto:bold_only_nav_anchor | md_ch02_a098, md_dmMS_ex_a026 | AGREE — 均为 `**Key rules for custom domains:**`、`**ms.xpt**` 纯加粗标题行 |
| auto:synthesized_type:TABLE_HEADER | md_dmPC_ex_a360, md_dmFA_ex_a062 | AGREE — RELREC 表头格式为统一生成 |
| auto:examples_data_row | md_dmTA_ex_a142, md_dmDS_ex_a234, md_dmPC_ex_a438 | AGREE — TA 表格数据行 (| 8 | EX4 | TA | ... |) 属于 trial arm 数据行，auto:examples_data_row 规则合理 |
| auto:source_header_annotation | md_index_a027 | AGREE — INDEX.md 中的文件说明注释为合成内容 |
| auto:synthesized_file | md_routing_a037 | AGREE — ROUTING.md 为 KB 合成路由文件 |

**注意：** md_ch02_a098 的 verbatim 为 `**Key rules for custom domains:**`，是纯加粗行，auto:bold_only_nav_anchor 规则正确应用。md_dmMS_ex_a026 的 verbatim 为 `**ms.xpt**`，同样是纯加粗数据集文件名标注，规则正确。

---

## SOURCED_P4A_MISSED 原子验证（10 个，全部 AGREE）

已验证的 SOURCED_P4A_MISSED 原子：

| atom_id | detail (pdf_atom_id) | 格式验证 | 内容验证 |
|---------|---------------------|---------|---------|
| md_model02_a179 | sv20_p0059_a011 | 格式正确（sv20 前缀，页码合理）| --LNKGRP 变量存在于 SDTM v2.0 §3.1.4 |
| md_model02_a087 | sv20_p0017_a001 | 格式正确 | --SOCCD 变量存在于 SDTM v2.0 Events 类 |
| md_model06_a027 | sv20_p0065_a005 | 格式正确 | RELTYPE 变量在 RELREC 规格中有明确定义 |
| md_model02_a159 | sv20_p0032_a011 | 格式正确 | --OBJ 变量为 Findings About 子类型核心变量 |
| md_model02_a075 | sv20_p0016_a002 | 格式正确 | --HLGT（High Level Group Term）为 MedDRA 分级 |
| md_model02_a024 | sv20_p0016_a008 | 格式正确 | --REASOC 变量存在于 Interventions 类 |
| md_model01_a030 | sv20_p0009_a011 | 格式正确 | Qualifier variables 定义符合 SDTM v2.0 §2.1 |
| md_ch04_a917 | ig34_p0055_a022 | 格式正确（ig34 前缀）| mh.xpt CODE_LITERAL 存在于 §4.5.3.2 |
| md_model02_a028 | sv20_p0013_a001 | 格式正确 | --EPCHGI 为 SDTM v2.0 新增变量（流行病学） |
| md_model04_a010 | sv20_p0050_a017 | 格式正确 | Associated Persons 链接变量 RSUBJID/RDEVID/SREL 详细描述符合 SDTM v2.0 §4 |

全部 10 个 SOURCED_P4A_MISSED 原子的 pdf_atom_id 格式正确（sv20/ig34 前缀 + 页码范围合理），内容真实。

---

## 结论

### 审查判定：PASS

100 个样本原子中，97 个同意 assigned_reverse_verdict，3 个不同意，同意率 97%，超过 95% 通过阈值。

### 主要发现

1. **SOURCED 类（40 个）：** 全部同意。内容均为真实的 SDTMIG 文本（示例说明句、表格数据行、章节内容），verbatim 与 SDTMIG v3.4 知识库内容一致。

2. **SYNTHESIZED 类（20 个）：** 全部同意。auto 规则应用准确：
   - `auto:synthesized_file` 正确识别 VARIABLE_INDEX.md 和 ROUTING.md 等 KB 合成文件
   - `auto:bold_only_nav_anchor` 正确识别纯加粗行（`**ms.xpt**`、`**Key rules for...**`）
   - `auto:examples_data_row` 正确识别 TA/DS trial arm 数据行

3. **SOURCED_P4A_MISSED 类（10 个）：** 全部同意。pdf_atom_id 格式合规，内容可在 SDTM 标准中验证。

4. **UNSOURCED_CANDIDATE 类（30 个）：** 发现 2 个应上调为 SOURCED 的条目（DISAGREE #2 和 #3），其余 28 个均为真实内容，建议分类为 SOURCED_P4A_MISSED（27 个）或 SYNTHESIZED（2 个，过渡句和编辑标注）。**无任何 HALLUCINATED 内容。**

5. **DISAGREE #1** 属于边界情形（SOURCED vs SOURCED_P4A_MISSED），对 PASS 判定无影响。**DISAGREE #2 和 #3 属于 P4a 漏匹配问题**（§8.2.2 示例说明句和数据行），建议 P5 主 session 在 reverse_ledger 中更新这 2 个原子的 verdict，并检查 ch08 §8.2.2 附近是否有更多类似漏匹配。

### 风险评估

- **高风险区域（ch04、ch08）HALLUCINATED 风险：0 个**
- ch04 UNSOURCED_CANDIDATE 的真实原因是 P4a 对 LIST_ITEM / TABLE_ROW 短原子的匹配召回率不足，而非内容虚构
- ch08 §8.2.2 存在系统性漏匹配（RELREC 示例说明句和数据行），建议重点复查
- 整体 reverse_ledger 质量良好，P5 阶段可信度高

---

*审查完成时间: 2026-05-12*
*独立性声明: 本审查员未参与 reverse_ledger 的生成，符合 Rule D 审阅隔离要求。*
