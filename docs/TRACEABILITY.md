# 溯源矩阵 (Traceability Matrix)

> 创建日期: 2026-04-15
> 验证计划步骤: Step 3.5
> 目的: 证明知识库产出的完整性——每一页源文件都被处理过，未收录的内容有明确排除理由，而非遗漏。

---

## 方法说明

本矩阵覆盖全部 4 份源文件，逐章/节建立从源文件到知识库文件的映射。

**处理决策**:
- **收录** — 内容已提取到知识库文件
- **故意排除** — 经评估后决定不收录，附理由

**域文件规范**: SDTMIG 中每个域在 `domains/{域名}/` 下拆分为 3 个文件：

| 文件 | 来源 | 说明 |
|------|------|------|
| `spec.md` | `SDTMIG_v3.4.xlsx` | 变量规范表（脚本生成，非 PDF 提取） |
| `assumptions.md` | SDTMIG v3.4 PDF | 业务规则与假设 |
| `examples.md` | SDTMIG v3.4 PDF | 示例数据表与说明 |

**验证状态**: 全部 138 个 PDF 提取文件已通过逐页对照 PDF 原文验证（Step 0–3），详见 `.work/03_verification/plan.md`。

---

## 1. SDTM v2.0 (74 页) → `model/`

源文件: `source/SDTM_v2.0.pdf`

| 章节 | 页码 | 知识库文件 | 决策 | 排除理由 |
|------|------|----------|------|---------|
| 封面 + 修订历史 | 1 | — | 故意排除 | 封面元信息，非技术规范 |
| 目录 (Contents) | 2–3 | — | 故意排除 | 导航性内容 |
| 1 Introduction | 4–7 | — | 故意排除 | 介绍性内容（目的、实施建议、与先前模型关系、版本变更概述）；不含可操作的模型定义 |
| **2 Model Concepts and Terms** | **8–10** | `model/01_concepts_and_terms.md` | **收录** | |
| **3.1 The General Observation Classes** | **11–39** | `model/02_observation_classes.md` | **收录** | |
| **3.2 Special-Purpose Domains** | **40–49** | `model/03_special_purpose_domains.md` | **收录** | |
| **4 Associated Persons Data** | **50** | `model/04_associated_persons.md` | **收录** | |
| **5 Study-Level Data** | **51–63** | `model/05_study_level_data.md` | **收录** | |
| **6 Datasets for Representing Relationships** | **64–69** | `model/06_relationship_datasets.md` | **收录** | |
| 7 Changes from SDTM v1.8 to v2.0 | 70–72 | — | 故意排除 | 版本变更日志；仅记录历史差异，不影响当前模型定义 |
| 8 Proposed Future Changes | 73 | — | 故意排除 | 未来计划提案，非当前规范，内容可能已过时 |
| 9 Appendices (Appendix A) | 74 | — | 故意排除 | 法律免责声明 (Representations and Warranties) |

**小计**: 62/74 页收录 (p.8–69)，12 页故意排除

---

## 2. SDTMIG v3.4 (461 页) → `chapters/` + `domains/`

源文件: `source/SDTMIG v3.4 (no header footer).pdf`

### 2.1 前页

| 内容 | 页码 | 决策 | 排除理由 |
|------|------|------|---------|
| 封面 + 修订历史 | 1 | 故意排除 | 封面元信息 |
| 目录 (Contents) | 2–6 | 故意排除 | 导航性内容 |

### 2.2 通用章节 → `chapters/`

| 章节 | 页码 | 知识库文件 | 决策 |
|------|------|----------|------|
| **1 Introduction** | **7–10** | `chapters/ch01_introduction.md` | **收录** |
| **2 Fundamentals of the SDTM** | **11–16** | `chapters/ch02_fundamentals.md` | **收录** |
| **3 Submitting Data in Standard Format** | **17–21** | `chapters/ch03_submitting_data.md` | **收录** |
| **4 Assumptions for Domain Models** | **22–59** | `chapters/ch04_general_assumptions.md` | **收录** |

### 2.3 Chapter 5: Models for Special-Purpose Domains (p.60–91)

每域 → `domains/{域名}/{spec,assumptions,examples}.md`

| 域 | 节号 | 页码 | 决策 |
|----|------|------|------|
| CO | 5.1 | 60–62 | 收录 |
| DM | 5.2 | 62–78 | 收录 |
| SE | 5.3 | 79–83 | 收录 |
| SM | 5.4 | 84–86 | 收录 |
| SV | 5.5 | 86–91 | 收录 |

> **注**: Chapter 5 标题引言（p.60 顶部，2 句）与 CO 在同一页，已融入 CO 域描述。

### 2.4 Chapter 6: Domain Models Based on General Observation Classes (p.92–381)

每域 → `domains/{域名}/{spec,assumptions,examples}.md`

#### 6.1 Interventions Domains (p.92–133)

| 域 | 节号 | 页码 | 决策 | 备注 |
|----|------|------|------|------|
| AG | 6.1.1 | 92–97 | 收录 | |
| CM | 6.1.2 | 98–103 | 收录 | |
| EX | 6.1.3.1 | 104–120 | 收录 | 示例 (p.111–120) 与 EC 共享 |
| EC | 6.1.3.2 | 107–120 | 收录 | 示例 (p.111–120) 与 EX 共享 |
| ML | 6.1.4 | 121–124 | 收录 | |
| PR | 6.1.5 | 125–128 | 收录 | |
| SU | 6.1.6 | 129–133 | 收录 | |

#### 6.2 Events Domains (p.133–179)

| 域 | 节号 | 页码 | 决策 |
|----|------|------|------|
| AE | 6.2.1 | 133–142 | 收录 |
| BE | 6.2.2 | 143–148 | 收录 |
| CE | 6.2.3 | 148–155 | 收录 |
| DS | 6.2.4 | 155–167 | 收录 |
| HO | 6.2.5 | 167–171 | 收录 |
| MH | 6.2.6 | 171–178 | 收录 |
| DV | 6.2.7 | 178–179 | 收录 |

#### 6.3 Findings Domains (p.180–361)

| 域 | 节号 | 页码 | 决策 | 备注 |
|----|------|------|------|------|
| DA | 6.3.1 | 180–182 | 收录 | |
| DD | 6.3.2 | 183–185 | 收录 | |
| EG | 6.3.3 | 185–192 | 收录 | |
| IE | 6.3.4 | 193–194 | 收录 | |
| BS | 6.3.5.2 | 196–199 | 收录 | |
| CP | 6.3.5.3 | 199–220 | 收录 | |
| GF | 6.3.5.4 | 220–228 | 收录 | |
| IS | 6.3.5.5 | 228–241 | 收录 | |
| LB | 6.3.5.6 | 241–248 | 收录 | |
| MB | 6.3.5.7 | 248–262 | 收录 | 示例 (p.256–262) 与 MS 共享 |
| MS | 6.3.5.8 | 252–262 | 收录 | 示例 (p.256–262) 与 MB 共享 |
| MI | 6.3.5.9 | 263–267 | 收录 | |
| PC | 6.3.5.10 | 267–284 | 收录 | 示例与 PP 共享 |
| PP | 6.3.5.10 | 270–284 | 收录 | 示例与 PC 共享 |
| CV | 6.3.7.2 | 286–289 | 收录 | |
| MK | 6.3.7.3 | 290–294 | 收录 | |
| NV | 6.3.7.4 | 294–298 | 收录 | |
| OE | 6.3.7.5 | 298–305 | 收录 | |
| RP | 6.3.7.6 | 305–307 | 收录 | |
| RE | 6.3.7.7 | 308–312 | 收录 | |
| UR | 6.3.7.8 | 312–315 | 收录 | |
| PE | 6.3.8 | 315–318 | 收录 | |
| FT | 6.3.9.1 | 319–324 | 收录 | |
| QS | 6.3.9.2 | 324–329 | 收录 | |
| RS | 6.3.9.3 | 329–339 | 收录 | |
| SC | 6.3.10 | 339–342 | 收录 | |
| SS | 6.3.11 | 342–343 | 收录 | |
| TU | 6.3.12.1 | 344–358 | 收录 | 示例 (p.353–358) 与 TR 共享 |
| TR | 6.3.12.2 | 350–358 | 收录 | 示例 (p.353–358) 与 TU 共享 |
| VS | 6.3.13 | 358–361 | 收录 | |

#### 6.4 Findings About Events or Interventions (p.361–381)

| 域 | 节号 | 页码 | 决策 | 备注 |
|----|------|------|------|------|
| FA | 6.4.4 | 364–375 | 收录 | |
| SR | 6.4.5 | 375–381 | 收录 | |

> 6.4 节引言 (p.361–364) 的处理见 [§2.9 节引言与共享规范](#29-节引言与共享规范处理)。

### 2.5 Chapter 7: Trial Design Model Datasets (p.382–426)

每域 → `domains/{域名}/{spec,assumptions,examples}.md`

| 域 | 节号 | 页码 | 决策 | 备注 |
|----|------|------|------|------|
| TA | 7.2.1 | 384–403 | 收录 | 含 7.2.1.1 Trial Arms Issues |
| TE | 7.2.2 | 403–407 | 收录 | 含 7.2.2.1 Trial Elements Issues |
| TV | 7.3.1 | 407–412 | 收录 | 含 7.3.1.1 Trial Visits Issues |
| TD | 7.3.2 | 412–417 | 收录 | |
| TM | 7.3.3 | 418 | 收录 | 全部内容在单页 |
| TI | 7.4.1 | 419–420 | 收录 | |
| TS | 7.4.2 | 420–425 | 收录 | 含 7.4.2.1 Use of Null Flavor |

> 7.1 Introduction (p.382–383) 和 7.5 How to Model (p.425–426) 的处理见 [§2.9 节引言与共享规范](#29-节引言与共享规范处理)。

### 2.6 Chapter 8: Representing Relationships and Data (p.427–440)

Chapter 8 采用双层映射：章节级指南 → `chapters/ch08_relationships.md`，域规范 → `domains/` 域文件。

| 内容 | 节号 | 页码 | 知识库文件 | 决策 |
|------|------|------|----------|------|
| **章节级内容**（GRPID, 数据归属指南, 关联评论等） | 8.1, 8.5–8.6 | 427–436 | `chapters/ch08_relationships.md` | **收录** |
| RELREC | 8.2 | 428–431 | `domains/RELREC/` | 收录 |
| SUPPQUAL | 8.4 | 431–434 | `domains/SUPPQUAL/` | 收录 |
| RELSUB | 8.7 | 437–439 | `domains/RELSUB/` | 收录 |
| RELSPEC | 8.8 | 439–440 | `domains/RELSPEC/` | 收录 |

> **注**: ch08_relationships.md 与域文件在页码上有重叠——章节文件覆盖跨域指南（§8.1 GRPID, §8.3 Dataset Relationships, §8.5 Relating Comments, §8.6 Data Placement Guidelines），域文件覆盖各域的规范表和示例。

### 2.7 Chapter 9: Study References (p.441–443)

| 内容 | 节号 | 页码 | 知识库文件 | 决策 | 备注 |
|------|------|------|----------|------|------|
| Device Identifiers | 9.1 | 441 | — | 故意排除 | 仅一句交叉引用，指向 SDTMIG-MD（医疗器械指南）；本项目范围为人体临床试验 |
| OI | 9.2 | 441–443 | `domains/OI/` | 收录 | |

### 2.8 Chapter 10: Appendices (p.444–461)

| 内容 | 页码 | 知识库文件 | 决策 | 备注 |
|------|------|----------|------|------|
| **Appendix A**: CDISC SDS Team | 444–445 | `chapters/ch10_appendices.md` | **收录** | 团队名单 |
| **Appendix B**: Glossary and Abbreviations | 446–447 | `chapters/ch10_appendices.md` | **收录** | 术语表 |
| **Appendix C**: Controlled Terminology | 448 | `chapters/ch10_appendices.md` | **收录** | 受控术语说明 |
| **Appendix D**: Variable-naming Fragments | 449–451 | `chapters/ch10_appendices.md` | **收录** | 变量命名片段表 |
| **Appendix E**: Revision History | 452–460 | `chapters/ch10_appendices.md` | **收录** | 版本修订历史 |
| **Appendix F**: Legal Disclaimers | 461 | — | 故意排除 | 法律免责声明 (Representations and Warranties) |

### 2.9 节引言与共享规范处理

SDTMIG 的 Chapter 5–7 中，部分"节引言"和"共享规范模板"不属于任何特定域。以下逐一说明处理方式：

#### 节引言（Section Introductions）

| 内容 | 页码 | 处理 | 说明 |
|------|------|------|------|
| Ch5 引言 | 60 顶部 | 融入 CO | 2 句（"Special-purpose Domains is an SDTM class..."），与 CO 在同一页 |
| Ch6 + §6.1 引言 | 92 顶部 | 融入 AG | 各 2 句，与 AG 在同一页 |
| §6.1.3 Exposure Domains 引言 | 103 | 融入 CM/EX | 介绍 EX/EC 关系，在 CM 末页与 EX 首页之间 |
| §6.2 Events 引言 | 133 顶部 | 融入 AE | 2 句，与 AE 在同一页 |
| §6.3 Findings 引言 | 180 顶部 | 融入 DA | 2 句，与 DA 在同一页 |
| §6.3.9 QRS 引言 | 318 | 融入 PE/FT | 介绍 FT/QS/RS 分组，在 PE 末页 |
| §6.3.12 Tumor/Lesion 引言 | 344 顶部 | 融入 TU | 与 TU 在同一页 |
| **§6.4 Findings About 引言** | **361–364** | **故意排除** | 3 页：何时使用 FA 域 (§6.4.1)、命名规则 (§6.4.2)、特有变量 (§6.4.3)。FA assumptions.md 通过交叉引用指向这些章节（"See Section 6.4.1…"），未内联全文。排除理由：属于组织性指南，读者应参照原始 PDF 获取完整判断树 |
| **§7.1 Trial Design 概念导论** | **382–383** | **故意排除** | 2 页：定义 Epoch、Arm、Element、Study Cell、Branch、Visit 等核心概念。排除理由：属于概念性教学内容，非可操作的域规范；各试验设计域 (TA–TS) 的 assumptions.md 已含域级业务规则 |
| **§7.5 How to Model a Clinical Trial** | **425–426** | **故意排除** | 2 页：12 步建模工作流（从 Schema 到 TS 填充）。排除理由：属于方法论指南，非数据模型定义；内容为操作建议，非规范性要求 |

#### 共享规范模板（Shared Specification Templates）

| 内容 | 页码 | 处理 | 说明 |
|------|------|------|------|
| §6.3.5.1 Generic Specimen-based Lab Findings Spec | 194–196 | 已覆盖 | 通用变量表模板，各域 (BS/CP/GF/IS/LB/MB/MS/MI/PC/PP) 的 spec.md 已从 xlsx 生成完整变量表，包含此模板的全部字段 |
| §6.3.6 Morphology (MO) 说明 | 285 | 已覆盖 | MO 非独立域，仅一段说明形态数据应使用 Morphology/Physiology 域收集 |
| §6.3.7.1 Generic Morphology/Physiology Spec | 285–286 | 已覆盖 | 通用变量表模板，各域 (CV/MK/NV/OE/RP/RE/UR) 的 spec.md 已从 xlsx 生成完整变量表 |

**SDTMIG 小计**: 461 页中 ~448 页收录，~7 页故意排除（§6.4 引言 3 页 + §7.1 引言 2 页 + §7.5 指南 2 页），6 页前页排除

---

## 3. SDTMIG_v3.4.xlsx → `domains/*/spec.md`

源文件: `source/SDTMIG_v3.4.xlsx`

| 内容 | 产出 | 方法 | 验证 |
|------|------|------|------|
| 63 个域的变量规范表 | 63 个 `domains/{域名}/spec.md` | Python 脚本自动生成 | 脚本校验通过（字段、行数、格式一致） |

> 此 xlsx 为 CDISC 官方发布的结构化数据，与 PDF 中的规范表内容一致但格式更规范。采用 xlsx 而非 PDF 作为 spec.md 的数据源，可避免 PDF 表格解析误差。

---

## 4. SDTM Terminology.xlsx → `terminology/`

源文件: `source/SDTM Terminology.xlsx`

| 分类 | 文件数 | 产出目录 | 方法 | 验证 |
|------|--------|---------|------|------|
| Core Codelists | 42 | `terminology/core/` | Python 脚本生成 | 脚本校验通过 |
| Questionnaire Codelists | 43 | `terminology/questionnaires/` | Python 脚本生成 | 脚本校验通过 |
| Supplementary Codelists | 6 | `terminology/supplementary/` | Python 脚本生成 | 脚本校验通过 |
| **合计** | **91** | | | |

> 受控术语为 CDISC 官方发布的结构化数据，脚本一对一转换为 Markdown 格式。

---

## 5. 覆盖统计汇总

### 按源文件

| 源文件 | 总页/条 | 收录 | 故意排除 | 排除率 |
|--------|---------|------|---------|--------|
| SDTM v2.0 PDF | 74 页 | 62 页 (p.8–69) | 12 页 | 16% |
| SDTMIG v3.4 PDF | 461 页 | ~448 页 | ~13 页 | 3% |
| SDTMIG_v3.4.xlsx | 63 域 | 63 域 | 0 | 0% |
| SDTM Terminology.xlsx | 91 条 | 91 条 | 0 | 0% |

### 按产出文件

| 目录 | 文件数 | 来源 | 验证方式 |
|------|--------|------|---------|
| `model/` | 6 | SDTM v2.0 PDF | PDF 逐页对照 (Step 3-1, 3-2) |
| `chapters/` | 6 | SDTMIG v3.4 PDF | PDF 逐页对照 (Step 3-3, 3-4, 3-5) |
| `domains/*/spec.md` | 63 | SDTMIG_v3.4.xlsx | 脚本校验 |
| `domains/*/assumptions.md` | 63 | SDTMIG v3.4 PDF | PDF 逐页对照 (Step 1) |
| `domains/*/examples.md` | 63 | SDTMIG v3.4 PDF | PDF 逐页对照 (Step 2) |
| `terminology/` | 91 | SDTM Terminology.xlsx | 脚本校验 |
| **合计** | **292** | | |

### 排除内容分类

| 类别 | 来源 | 页数 | 说明 |
|------|------|------|------|
| 封面/目录 | 两份 PDF | 9 | 元信息和导航，非技术内容 |
| 介绍章节 | SDTM v2.0 Ch1 | 4 | 目的、建议、关系、变更概述 |
| 版本变更日志 | SDTM v2.0 Ch7 | 3 | v1.8→v2.0 差异记录 |
| 未来变更提案 | SDTM v2.0 Ch8 | 1 | 非当前规范 |
| 法律免责声明 | 两份 PDF 附录 | 2 | 法律条款 |
| 节引言/概念导论 | SDTMIG §6.4, §7.1, §7.5 | 7 | 教学性/方法论内容，域文件通过交叉引用指向原文 |
| 器械域引用 | SDTMIG §9.1 | <1 | 指向 SDTMIG-MD，超出项目范围 |
| **合计** | | **~26** | |

---

## 附录: 63 域完整页码映射

以下为 SDTMIG v3.4 PDF 中 63 个域的完整页码索引（已在 Step 0 中逐域验证）。

| # | 域 | 章节 | 类别 | 页码范围 | 共享示例 |
|---|-----|------|------|---------|---------|
| 1 | CO | Ch5 | Special Purpose | 60–62 | |
| 2 | DM | Ch5 | Special Purpose | 62–78 | |
| 3 | SE | Ch5 | Special Purpose | 79–83 | |
| 4 | SM | Ch5 | Special Purpose | 84–86 | |
| 5 | SV | Ch5 | Special Purpose | 86–91 | |
| 6 | AG | Ch6 | Interventions | 92–97 | |
| 7 | CM | Ch6 | Interventions | 98–103 | |
| 8 | EX | Ch6 | Interventions | 104–120 | 示例 p.111–120 与 EC 共享 |
| 9 | EC | Ch6 | Interventions | 107–120 | 示例 p.111–120 与 EX 共享 |
| 10 | ML | Ch6 | Interventions | 121–124 | |
| 11 | PR | Ch6 | Interventions | 125–128 | |
| 12 | SU | Ch6 | Interventions | 129–133 | |
| 13 | AE | Ch6 | Events | 133–142 | |
| 14 | BE | Ch6 | Events | 143–148 | |
| 15 | CE | Ch6 | Events | 148–155 | |
| 16 | DS | Ch6 | Events | 155–167 | |
| 17 | HO | Ch6 | Events | 167–171 | |
| 18 | MH | Ch6 | Events | 171–178 | |
| 19 | DV | Ch6 | Events | 178–179 | |
| 20 | DA | Ch6 | Findings | 180–182 | |
| 21 | DD | Ch6 | Findings | 183–185 | |
| 22 | EG | Ch6 | Findings | 185–192 | |
| 23 | IE | Ch6 | Findings | 193–194 | |
| 24 | BS | Ch6 | Findings | 196–199 | |
| 25 | CP | Ch6 | Findings | 199–220 | |
| 26 | GF | Ch6 | Findings | 220–228 | |
| 27 | IS | Ch6 | Findings | 228–241 | |
| 28 | LB | Ch6 | Findings | 241–248 | |
| 29 | MB | Ch6 | Findings | 248–262 | 示例 p.256–262 与 MS 共享 |
| 30 | MS | Ch6 | Findings | 252–262 | 示例 p.256–262 与 MB 共享 |
| 31 | MI | Ch6 | Findings | 263–267 | |
| 32 | PC | Ch6 | Findings | 267–284 | 示例与 PP 共享 |
| 33 | PP | Ch6 | Findings | 270–284 | 示例与 PC 共享 |
| 34 | CV | Ch6 | Findings | 286–289 | |
| 35 | MK | Ch6 | Findings | 290–294 | |
| 36 | NV | Ch6 | Findings | 294–298 | |
| 37 | OE | Ch6 | Findings | 298–305 | |
| 38 | RP | Ch6 | Findings | 305–307 | |
| 39 | RE | Ch6 | Findings | 308–312 | |
| 40 | UR | Ch6 | Findings | 312–315 | |
| 41 | PE | Ch6 | Findings | 315–318 | |
| 42 | FT | Ch6 | Findings (QRS) | 319–324 | |
| 43 | QS | Ch6 | Findings (QRS) | 324–329 | |
| 44 | RS | Ch6 | Findings (QRS) | 329–339 | |
| 45 | SC | Ch6 | Findings | 339–342 | |
| 46 | SS | Ch6 | Findings | 342–343 | |
| 47 | TU | Ch6 | Findings | 344–358 | 示例 p.353–358 与 TR 共享 |
| 48 | TR | Ch6 | Findings | 350–358 | 示例 p.353–358 与 TU 共享 |
| 49 | VS | Ch6 | Findings | 358–361 | |
| 50 | FA | Ch6 | Findings About | 364–375 | |
| 51 | SR | Ch6 | Findings About | 375–381 | |
| 52 | TA | Ch7 | Trial Design | 384–403 | |
| 53 | TE | Ch7 | Trial Design | 403–407 | |
| 54 | TV | Ch7 | Trial Design | 407–412 | |
| 55 | TD | Ch7 | Trial Design | 412–417 | |
| 56 | TM | Ch7 | Trial Design | 418 | |
| 57 | TI | Ch7 | Trial Design | 419–420 | |
| 58 | TS | Ch7 | Trial Design | 420–425 | |
| 59 | RELREC | Ch8 | Relationship | 428–431 | |
| 60 | SUPPQUAL | Ch8 | Relationship | 431–434 | |
| 61 | RELSUB | Ch8 | Relationship | 437–439 | |
| 62 | RELSPEC | Ch8 | Relationship | 439–440 | |
| 63 | OI | Ch9 | Study Reference | 441–443 | |

---

## 6. 图像内容溯源 (Image Traceability)

> 完成日期: 2026-04-15 (Step 3.6)
> 扫描范围: SDTM v2.0 (74页) + SDTMIG v3.4 (461页) = 535页
> 方法: 6 个 agent 并行扫描全部 PDF 页面，识别所有非文字、非表格的视觉内容

### 方法说明

**扫描**: 将 535 页 PDF 分为 6 个批次，由 6 个 agent 并行逐页视觉扫描，记录所有图形化内容（流程图、决策树、CRF 模拟图、关系图、时间轴、Schema 图等）。

**转化格式**:
- 流程图 / 决策树 / 关系图 / 时间轴 / Schema → **Mermaid** 代码块
- CRF 模拟图 / CRF Mockup → **Markdown 表格**（CRF 表单的结构更接近表格）

**页码说明**: 下表页码为 agent 视觉扫描估算值，可能存在 ±2 页偏移，仅作为定位参考。精确溯源应以所属章节/域+图像描述为准。

### 统计

| 状态 | 数量 | 说明 |
|------|------|------|
| 已转化 (Mermaid) | 24 | Step 2-final (13组) + Step 3-final (6幅) + Step 3.6 (6幅 Mermaid) |
| 已转化 (表格) | 15 | Step 3.6 CRF → Markdown table |
| 已转化 (Mermaid, TA 子视图) | 19 | TA Examples 1-7 的多视图（含在 Step 2-final 13 组中） |
| 故意排除 | 2 | 两份 PDF 封面 CDISC Logo |
| **合计** | **60** | |

### 完整图像清单

#### A. SDTM v2.0 (4 幅)

| # | ~页码 | 所属章节 | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 |
|---|-------|----------|----------|----------|----------|----------|----------|------|
| 1 | 1 | 封面 | Logo | CDISC 彩色圆点 Logo | — | — | — | 故意排除 |
| 2 | 8 | §2 Concepts and Terms | 关系/层次图 | Concept Map: SDTM Domains 全局关系树状图 | Mermaid | model/01_concepts_and_terms.md | Step 3.6 | 已转化 |
| 3 | 62 | §5.2.1 Device Identifiers | 关系图 | Concept Map: Device Identifier Variables | Mermaid | model/05_study_level_data.md | Step 3.6 | 已转化 |
| 4 | 63 | §5.2.2 Non-host Organism IDs | 关系图 | Concept Map: Non-host Organism Identifier Variables | Mermaid | model/05_study_level_data.md | Step 3.6 | 已转化 |

#### B. SDTMIG v3.4 — 通用章节 (9 幅)

| # | ~页码 | 所属章节 | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 |
|---|-------|----------|----------|----------|----------|----------|----------|------|
| 5 | 1 | 封面 | Logo | CDISC 彩色圆点 Logo | — | — | — | 故意排除 |
| 6 | 15 | §2.6 Creating a New Domain | 关系/层次图 | Creating a New Domain 组合构成图 | Mermaid | chapters/ch02_fundamentals.md | Step 3-final | 已转化 |
| 7 | 31 | §4.2.7.1 Specify Non-result | CRF 模拟图 | EXADJ 复选框 + 镇痛药适应证 CRF | 表格 | chapters/ch04_general_assumptions.md | Step 3.6 | 已转化 |
| 8 | 32 | §4.2.7.2 Specify Result | CRF 模拟图 | Eye Color CRF (Other specify) | 表格 | chapters/ch04_general_assumptions.md | Step 3.6 | 已转化 |
| 9 | 33 | §4.2.7.3 Specify Topic | CRF 模拟图 | Concomitant Medications CRF | 表格 | chapters/ch04_general_assumptions.md | Step 3.6 | 已转化 |
| 10 | 34 | §4.2.7.4 Specify --OBJ | 决策树 | Decision Tree for Populating --OBJ | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 |
| 11 | 44 | §4.4.7 Relative Timing | 时间轴 | --ENRTPT/--ENTPT for Medical History | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 |
| 12 | 46 | §4.4.10 Representing Time Points | 时间轴/架构图 | Reference/Elapsed/Collection 时间点关系 | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 |
| 13 | 51 | §4.5.1.1 Original & Standardized | 流程图 | --ORRES→--STRESC→--STRESN 转换 | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 |

#### C. SDTMIG v3.4 — DM 域 CRF (6 幅)

| # | ~页码 | 所属域/Example | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 |
|---|-------|---------------|----------|----------|----------|----------|----------|------|
| 14 | 71 | DM Example 4 | CRF Mockup | aCRF for Race — RACE01-07 主表 | Mermaid | domains/DM/examples.md | Step 2-final | 已转化 |
| 15 | 71 | DM Example 4 | CRF Mockup | AMERICAN INDIAN 子分类 (CRACE01-04) | Mermaid | domains/DM/examples.md | Step 2-final | 已转化 |
| 16 | 72 | DM Example 4 | CRF Mockup | ASIAN/BLACK/WHITE 子分类 (CRACE05-21) | Mermaid | domains/DM/examples.md | Step 2-final | 已转化 |
| 17 | 74 | DM Example 5 | CRF Mockup | 中国民族子分类 HAN/MANCHU/MIAO/UYGHUR/ZHUANG | Mermaid | domains/DM/examples.md | Step 2-final | 已转化 |
| 18 | 75 | DM Example 6 | CRF Mockup | aCRF for Race（第二版）+ 子分类 | Mermaid | domains/DM/examples.md | Step 2-final | 已转化 |
| 19 | 78 | DM Example 7 | CRF Mockup | 5 种族 + Unknown + Other + RACEOTH | Mermaid | domains/DM/examples.md | Step 2-final | 已转化 |

#### D. SDTMIG v3.4 — EX/EC 域 CRF (6 幅)

| # | ~页码 | 所属域/Example | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 |
|---|-------|---------------|----------|----------|----------|----------|----------|------|
| 20 | 111 | EX Example 1 | CRF Mockup | 口服给药 CRF — Bottle/Tablets/Variation/Dates | 表格 | domains/EX/examples.md | Step 3.6 | 已转化 |
| 21 | 112 | EX Example 2 | CRF Mockup | 注射给药 CRF — Injection 1-3 Volume/Location/Side | 表格 | domains/EX/examples.md | Step 3.6 | 已转化 |
| 22 | 114 | EX Example 5 | CRF Mockup | 双盲交叉 CRF — 3 subjects | 表格 | domains/EX/examples.md | Step 3.6 | 已转化 |
| 23 | 115 | EX Example 6 | CRF Mockup | 单次给药交叉 CRF — Period 1/2 | 表格 | domains/EX/examples.md | Step 3.6 | 已转化 |
| 24 | 118 | EX Example 7 | CRF Mockup | 输液给药 CRF — Dose/Adjustment/Amount | 表格 | domains/EX/examples.md | Step 3.6 | 已转化 |
| 25 | 119 | EX Example 8 | CRF Mockup | 简化给药日志 CRF — First/Last Dose + Deviation | 表格 | domains/EX/examples.md | Step 3.6 | 已转化 |

#### E. SDTMIG v3.4 — ML/AE/CE 域 CRF (6 幅)

| # | ~页码 | 所属域/Example | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 |
|---|-------|---------------|----------|----------|----------|----------|----------|------|
| 26 | 123 | ML Example 1 | CRF Mockup | Meal Log CRF — Type/Volume/Date/Time | 表格 | domains/ML/examples.md | Step 3.6 | 已转化 |
| 27 | 123 | ML Example 1 | CRF Mockup | DILI Meal CRF — Mushrooms/Ackee/Cycad | 表格 | domains/ML/examples.md | Step 3.6 | 已转化 |
| 28 | 139 | AE Assumptions | CRF 片段 | AE 严重性分类 — Serious?/Fatal/Life-threatening | 表格 | domains/AE/assumptions.md | Step 3.6 | 已转化 |
| 29 | 151 | CE Example 1 | CRF Mockup | 预设临床事件 — Rash/Wheezing/Edema Yes/No | 表格 | domains/CE/examples.md | Step 3.6 | 已转化 |
| 30 | 152 | CE Example 2 | CRF Mockup | 含严重程度 — Nausea/Vomit + Severity | 表格 | domains/CE/examples.md | Step 3.6 | 已转化 |
| 31 | 153 | CE Example 3 | CRF Mockup | Bone Fracture Assessment 详细评估表 | 表格 | domains/CE/examples.md | Step 3.6 | 已转化 |

#### F. SDTMIG v3.4 — p.160-359 (0 幅)

> p.160-359 (200页) 全部为纯文字和标准数据表格，无图形化内容。
> 涵盖 32 个域：DS, HO, MH, DV, DA, DD, EG, IE, BS, CP, GF, IS, LB, MB, MS, MI, PC, PP, MO, CV, MK, NV, OE, RP, RE, UR, PE, FT, QS, RS, SC, SS

#### G. SDTMIG v3.4 — TA/TV/TD/RELSPEC 域 (29 幅)

| # | ~页码 | 所属域/Example | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 |
|---|-------|---------------|----------|----------|----------|----------|----------|------|
| 32 | 386 | TA Example 1 | Study Schema | Parallel Design Study Schema | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 33 | 387 | TA Example 1 | Schema (前瞻) | Parallel Design Prospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 34 | 387 | TA Example 1 | Schema (回顾) | Parallel Design Retrospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 35 | 387 | TA Example 1 | Schema (盲态) | Parallel Design Blinded View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 36 | 389 | TA Example 2 | Study Schema | Crossover Trial Study Schema | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 37 | 390 | TA Example 2 | Schema (前瞻) | Crossover Trial Prospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 38 | 390 | TA Example 2 | Schema (回顾) | Crossover Trial Retrospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 39 | 391 | TA Example 2 | Schema (盲态) | Crossover Trial Blinded View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 40 | 393 | TA Example 3 | Study Schema | Multiple Branches Study Schema | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 41 | 393 | TA Example 3 | Schema (前瞻) | Multiple Branches Prospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 42 | 394 | TA Example 3 | Schema (回顾) | Multiple Branches Retrospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 43 | 394 | TA Example 3 | Schema (盲态) | Multiple Branches Blinded View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 44 | 396 | TA Example 4 | Study Schema | Cyclical Chemotherapy Study Schema | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 45 | 397 | TA Example 4 | Schema (前瞻) | Cyclical Chemo Prospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 46 | 397 | TA Example 4 | Schema (回顾) | Cyclical Chemo Retrospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 47 | 397 | TA Example 4 | Schema (回顾+显式) | Cyclical Chemo with Explicit Repeats | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 48 | 398 | TA Example 4 | Schema (盲态) | Cyclical Chemo Blinded View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 49 | 399 | TA Example 5 | Study Schema | Different Chemo Durations Study Schema | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 50 | 399 | TA Example 5 | Schema (回顾) | Different Chemo Durations Retrospective | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 51 | 400 | TA Example 6 | Study Schema | Different Cycle Durations Study Schema | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 52 | 400 | TA Example 6 | Schema (回顾) | Different Cycle Durations Retrospective | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 53 | 401 | TA Example 7 | Study Schema | RTOG 93-09 Study Schema with 5 Options | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 54 | 402 | TA Example 7 | Schema (前瞻) | RTOG 93-09 Prospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 55 | 403 | TA Example 7 | Schema (回顾) | RTOG 93-09 Retrospective View | Mermaid | domains/TA/examples.md | Step 2-final | 已转化 |
| 56 | 412 | TV Example 1 | 时间轴 | Parallel Design Planned Visits | Mermaid | domains/TV/examples.md | Step 2-final | 已转化 |
| 57 | ~413 | TD Example 1 | 时间轴 | Disease Assessment 3 Schedules (8w/12w/24w) | Mermaid | domains/TD/examples.md | Step 3.6 | 已转化 |
| 58 | ~414 | TD Example 2 | 时间轴 | Disease Assessment 2 Periods (ANCH1DT/ANCH2DT) | Mermaid | domains/TD/examples.md | Step 3.6 | 已转化 |
| 59 | ~415 | TD Example 3 | 时间轴 | Disease Assessment Double Blind + Extension | Mermaid | domains/TD/examples.md | Step 3.6 | 已转化 |
| 60 | 440 | RELSPEC Example 1 | 层次/关系图 | Sample Specimen Relationship 层次衍生 | Mermaid | domains/RELSPEC/examples.md + chapters/ch08_relationships.md | Step 2-final + Step 3-final | 已转化 |

### 排除内容

| # | ~页码 | 源 PDF | 图像类型 | 描述 | 排除理由 |
|---|-------|--------|----------|------|----------|
| 1 | 1 | SDTM v2.0 | Logo | CDISC 彩色圆点 Logo | 装饰性图片，无知识内容 |
| 5 | 1 | SDTMIG v3.4 | Logo | CDISC 彩色圆点 Logo | 装饰性图片，无知识内容 |

### 图像类型分布

| 图像类型 | 数量 | 转化格式 |
|----------|------|----------|
| Study Schema / 架构图 | 24 | Mermaid |
| CRF Mockup / CRF 模拟图 | 21 | Mermaid (DM 6幅) / 表格 (其余 15幅) |
| 时间轴 (Timeline) | 7 | Mermaid |
| 关系/层次图 (Concept Map) | 5 | Mermaid |
| 决策树 (Decision Tree) | 1 | Mermaid |
| Logo / 装饰 | 2 | — (排除) |
| **合计** | **60** | |

### 处理批次分布

| 处理批次 | 图像数 | 说明 |
|----------|--------|------|
| Step 2-final | 32 | 13 组域图像（含 TA 24 个子视图） |
| Step 3-final | 6 | chapters/ 章节图像（含 1 幅与 Step 2-final 重叠） |
| Step 3.6 | 21 | 本次补全（3 Concept Map + 3 TD 时间轴 + 15 CRF 表格） |
| 故意排除 | 2 | CDISC Logo |
| **合计** | **60** | 扣除 1 幅重叠 = 59 独立图像 + 1 幅双处引用 |
