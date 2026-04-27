# 01_navigation_and_routing

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `01`
> - **Concept**: 导航 + 路由提示 + Req 变量速查入口
> - **Merged files**: 2
> - **Words**: 2,145
> - **Chars**: 21,877
> - **Sources**:
>   - `INDEX.md`
>   - `ROUTING.md`

---
## Source: `INDEX.md`

# SDTM Knowledge Base — Index

> Generated from SDTM v2.0 and SDTMIG v3.4 source documents.
> Total: **293 files** (63 domains × 3 files + 91 terminology + 6 model + 6 chapters + 1 index)

## Quick Lookup

- **问题路由** → [ROUTING.md](ROUTING.md) — 按问题类型查找应读哪些文件（AI 首选入口）
- **按变量名查询** → [VARIABLE_INDEX.md](VARIABLE_INDEX.md) — 1523 个变量的反向索引（变量→域→定义位置 + CT 交叉引用）

---

## Model (SDTM v2.0 Conceptual Model)

| File | Source | Description |
|------|--------|-------------|
| [concepts_and_terms.md](model/01_concepts_and_terms.md) | SDTM v2.0 Ch2 | Variable roles, qualifier subclasses, table structure |
| [observation_classes.md](model/02_observation_classes.md) | SDTM v2.0 Ch3.1 | Interventions (43 vars), Events (56 vars), Findings (100+ vars), Identifiers (16 vars), Timing (48 vars) |
| [special_purpose_domains.md](model/03_special_purpose_domains.md) | SDTM v2.0 Ch3.2 | DM (38 vars), CO (15 vars), SE (13 vars), SJ (10 vars), SV (16 vars), SM (10 vars) |
| [associated_persons.md](model/04_associated_persons.md) | SDTM v2.0 Ch4 | AP domain rules, APID/RSUBJID/RDEVID/SREL |
| [study_level_data.md](model/05_study_level_data.md) | SDTM v2.0 Ch5 | Trial Design (TE/TA/TX/TT/TP/TV/TD/TM/TI/TS/AC) + Study References (DI/OI) |
| [relationship_datasets.md](model/06_relationship_datasets.md) | SDTM v2.0 Ch6 | RELREC, SUPP--, POOLDEF, RELSUB, DR, APRELSUB, RELSPEC |

## Chapters (SDTMIG v3.4 Implementation Guide)

| File | Source | Description |
|------|--------|-------------|
| [ch01_introduction.md](chapters/ch01_introduction.md) | SDTMIG Ch1 | Purpose, organization, changes from v3.3, reading guide |
| [ch02_fundamentals.md](chapters/ch02_fundamentals.md) | SDTMIG Ch2 | Observations, variables, domains, GOC, creating new domains, disallowed variables |
| [ch03_submitting_data.md](chapters/ch03_submitting_data.md) | SDTMIG Ch3 | Standard metadata, dataset metadata, primary keys, value-level metadata |
| [ch04_general_assumptions.md](chapters/ch04_general_assumptions.md) | SDTMIG Ch4 | Domain/variable/coding/timing/other assumptions |
| [ch08_relationships.md](chapters/ch08_relationships.md) | SDTMIG Ch8 | GRPID, RELREC, SUPP--, comments, data placement, RELSUB, RELSPEC |
| [ch10_appendices.md](chapters/ch10_appendices.md) | SDTMIG Ch10 | Glossary, controlled terminology, QNAM codes, naming fragments, revision history |

---

## Domains (63 domains)

Each domain directory contains 3 files:
- **spec.md** — Variable specification table (from SDTMIG v3.4 xlsx)
- **assumptions.md** — Domain-specific assumptions and business rules (from SDTMIG v3.4 PDF)
- **examples.md** — Implementation examples with data tables (from SDTMIG v3.4 PDF)

### Special-purpose Domains

| Domain | Name | Class | Files |
|--------|------|-------|-------|
| [CO](domains/CO/) | Comments | Special Purpose | [spec](domains/CO/spec.md) · [assumptions](domains/CO/assumptions.md) · [examples](domains/CO/examples.md) |
| [DM](domains/DM/) | Demographics | Special Purpose | [spec](domains/DM/spec.md) · [assumptions](domains/DM/assumptions.md) · [examples](domains/DM/examples.md) |
| [SE](domains/SE/) | Subject Elements | Special Purpose | [spec](domains/SE/spec.md) · [assumptions](domains/SE/assumptions.md) · [examples](domains/SE/examples.md) |
| [SM](domains/SM/) | Subject Disease Milestones | Special Purpose | [spec](domains/SM/spec.md) · [assumptions](domains/SM/assumptions.md) · [examples](domains/SM/examples.md) |
| [SV](domains/SV/) | Subject Visits | Special Purpose | [spec](domains/SV/spec.md) · [assumptions](domains/SV/assumptions.md) · [examples](domains/SV/examples.md) |

### Interventions Domains

| Domain | Name | Files |
|--------|------|-------|
| [AG](domains/AG/) | Procedure Agents | [spec](domains/AG/spec.md) · [assumptions](domains/AG/assumptions.md) · [examples](domains/AG/examples.md) |
| [CM](domains/CM/) | Concomitant/Prior Medications | [spec](domains/CM/spec.md) · [assumptions](domains/CM/assumptions.md) · [examples](domains/CM/examples.md) |
| [EC](domains/EC/) | Exposure as Collected | [spec](domains/EC/spec.md) · [assumptions](domains/EC/assumptions.md) · [examples](domains/EC/examples.md) |
| [EX](domains/EX/) | Exposure | [spec](domains/EX/spec.md) · [assumptions](domains/EX/assumptions.md) · [examples](domains/EX/examples.md) |
| [ML](domains/ML/) | Meal Data | [spec](domains/ML/spec.md) · [assumptions](domains/ML/assumptions.md) · [examples](domains/ML/examples.md) |
| [PR](domains/PR/) | Procedures | [spec](domains/PR/spec.md) · [assumptions](domains/PR/assumptions.md) · [examples](domains/PR/examples.md) |
| [SU](domains/SU/) | Substance Use | [spec](domains/SU/spec.md) · [assumptions](domains/SU/assumptions.md) · [examples](domains/SU/examples.md) |

### Events Domains

| Domain | Name | Files |
|--------|------|-------|
| [AE](domains/AE/) | Adverse Events | [spec](domains/AE/spec.md) · [assumptions](domains/AE/assumptions.md) · [examples](domains/AE/examples.md) |
| [BE](domains/BE/) | Biospecimen Events | [spec](domains/BE/spec.md) · [assumptions](domains/BE/assumptions.md) · [examples](domains/BE/examples.md) |
| [CE](domains/CE/) | Clinical Events | [spec](domains/CE/spec.md) · [assumptions](domains/CE/assumptions.md) · [examples](domains/CE/examples.md) |
| [DS](domains/DS/) | Disposition | [spec](domains/DS/spec.md) · [assumptions](domains/DS/assumptions.md) · [examples](domains/DS/examples.md) |
| [DV](domains/DV/) | Protocol Deviations | [spec](domains/DV/spec.md) · [assumptions](domains/DV/assumptions.md) · [examples](domains/DV/examples.md) |
| [HO](domains/HO/) | Healthcare Encounters | [spec](domains/HO/spec.md) · [assumptions](domains/HO/assumptions.md) · [examples](domains/HO/examples.md) |
| [MH](domains/MH/) | Medical History | [spec](domains/MH/spec.md) · [assumptions](domains/MH/assumptions.md) · [examples](domains/MH/examples.md) |

### Findings Domains

| Domain | Name | Files |
|--------|------|-------|
| [BS](domains/BS/) | Biospecimen Findings | [spec](domains/BS/spec.md) · [assumptions](domains/BS/assumptions.md) · [examples](domains/BS/examples.md) |
| [CP](domains/CP/) | Cell Phenotype Findings | [spec](domains/CP/spec.md) · [assumptions](domains/CP/assumptions.md) · [examples](domains/CP/examples.md) |
| [CV](domains/CV/) | Cardiovascular System Findings | [spec](domains/CV/spec.md) · [assumptions](domains/CV/assumptions.md) · [examples](domains/CV/examples.md) |
| [DA](domains/DA/) | Product Accountability | [spec](domains/DA/spec.md) · [assumptions](domains/DA/assumptions.md) · [examples](domains/DA/examples.md) |
| [DD](domains/DD/) | Death Details | [spec](domains/DD/spec.md) · [assumptions](domains/DD/assumptions.md) · [examples](domains/DD/examples.md) |
| [EG](domains/EG/) | ECG Test Results | [spec](domains/EG/spec.md) · [assumptions](domains/EG/assumptions.md) · [examples](domains/EG/examples.md) |
| [FA](domains/FA/) | Findings About Events or Interventions | [spec](domains/FA/spec.md) · [assumptions](domains/FA/assumptions.md) · [examples](domains/FA/examples.md) |
| [FT](domains/FT/) | Functional Tests | [spec](domains/FT/spec.md) · [assumptions](domains/FT/assumptions.md) · [examples](domains/FT/examples.md) |
| [GF](domains/GF/) | Genomics Findings | [spec](domains/GF/spec.md) · [assumptions](domains/GF/assumptions.md) · [examples](domains/GF/examples.md) |
| [IE](domains/IE/) | Inclusion/Exclusion Criteria Not Met | [spec](domains/IE/spec.md) · [assumptions](domains/IE/assumptions.md) · [examples](domains/IE/examples.md) |
| [IS](domains/IS/) | Immunogenicity Specimen Assessments | [spec](domains/IS/spec.md) · [assumptions](domains/IS/assumptions.md) · [examples](domains/IS/examples.md) |
| [LB](domains/LB/) | Laboratory Test Results | [spec](domains/LB/spec.md) · [assumptions](domains/LB/assumptions.md) · [examples](domains/LB/examples.md) |
| [MB](domains/MB/) | Microbiology Specimen | [spec](domains/MB/spec.md) · [assumptions](domains/MB/assumptions.md) · [examples](domains/MB/examples.md) |
| [MI](domains/MI/) | Microscopic Findings | [spec](domains/MI/spec.md) · [assumptions](domains/MI/assumptions.md) · [examples](domains/MI/examples.md) |
| [MK](domains/MK/) | Musculoskeletal System Findings | [spec](domains/MK/spec.md) · [assumptions](domains/MK/assumptions.md) · [examples](domains/MK/examples.md) |
| [MS](domains/MS/) | Microbiology Susceptibility | [spec](domains/MS/spec.md) · [assumptions](domains/MS/assumptions.md) · [examples](domains/MS/examples.md) |
| [NV](domains/NV/) | Nervous System Findings | [spec](domains/NV/spec.md) · [assumptions](domains/NV/assumptions.md) · [examples](domains/NV/examples.md) |
| [OE](domains/OE/) | Ophthalmic Examinations | [spec](domains/OE/spec.md) · [assumptions](domains/OE/assumptions.md) · [examples](domains/OE/examples.md) |
| [PC](domains/PC/) | Pharmacokinetics Concentrations | [spec](domains/PC/spec.md) · [assumptions](domains/PC/assumptions.md) · [examples](domains/PC/examples.md) |
| [PE](domains/PE/) | Physical Examination | [spec](domains/PE/spec.md) · [assumptions](domains/PE/assumptions.md) · [examples](domains/PE/examples.md) |
| [PP](domains/PP/) | Pharmacokinetics Parameters | [spec](domains/PP/spec.md) · [assumptions](domains/PP/assumptions.md) · [examples](domains/PP/examples.md) |
| [QS](domains/QS/) | Questionnaires | [spec](domains/QS/spec.md) · [assumptions](domains/QS/assumptions.md) · [examples](domains/QS/examples.md) |
| [RE](domains/RE/) | Respiratory System Findings | [spec](domains/RE/spec.md) · [assumptions](domains/RE/assumptions.md) · [examples](domains/RE/examples.md) |
| [RP](domains/RP/) | Reproductive System Findings | [spec](domains/RP/spec.md) · [assumptions](domains/RP/assumptions.md) · [examples](domains/RP/examples.md) |
| [RS](domains/RS/) | Disease Response and Clin Classification | [spec](domains/RS/spec.md) · [assumptions](domains/RS/assumptions.md) · [examples](domains/RS/examples.md) |
| [SC](domains/SC/) | Subject Characteristics | [spec](domains/SC/spec.md) · [assumptions](domains/SC/assumptions.md) · [examples](domains/SC/examples.md) |
| [SR](domains/SR/) | Skin Response | [spec](domains/SR/spec.md) · [assumptions](domains/SR/assumptions.md) · [examples](domains/SR/examples.md) |
| [SS](domains/SS/) | Subject Status | [spec](domains/SS/spec.md) · [assumptions](domains/SS/assumptions.md) · [examples](domains/SS/examples.md) |
| [TR](domains/TR/) | Tumor/Lesion Results | [spec](domains/TR/spec.md) · [assumptions](domains/TR/assumptions.md) · [examples](domains/TR/examples.md) |
| [TU](domains/TU/) | Tumor/Lesion Identification | [spec](domains/TU/spec.md) · [assumptions](domains/TU/assumptions.md) · [examples](domains/TU/examples.md) |
| [UR](domains/UR/) | Urinary System Findings | [spec](domains/UR/spec.md) · [assumptions](domains/UR/assumptions.md) · [examples](domains/UR/examples.md) |
| [VS](domains/VS/) | Vital Signs | [spec](domains/VS/spec.md) · [assumptions](domains/VS/assumptions.md) · [examples](domains/VS/examples.md) |

### Trial Design Domains

| Domain | Name | Files |
|--------|------|-------|
| [TA](domains/TA/) | Trial Arms | [spec](domains/TA/spec.md) · [assumptions](domains/TA/assumptions.md) · [examples](domains/TA/examples.md) |
| [TD](domains/TD/) | Trial Disease Assessments | [spec](domains/TD/spec.md) · [assumptions](domains/TD/assumptions.md) · [examples](domains/TD/examples.md) |
| [TE](domains/TE/) | Trial Elements | [spec](domains/TE/spec.md) · [assumptions](domains/TE/assumptions.md) · [examples](domains/TE/examples.md) |
| [TI](domains/TI/) | Trial Inclusion/Exclusion Criteria | [spec](domains/TI/spec.md) · [assumptions](domains/TI/assumptions.md) · [examples](domains/TI/examples.md) |
| [TM](domains/TM/) | Trial Disease Milestones | [spec](domains/TM/spec.md) · [assumptions](domains/TM/assumptions.md) · [examples](domains/TM/examples.md) |
| [TS](domains/TS/) | Trial Summary | [spec](domains/TS/spec.md) · [assumptions](domains/TS/assumptions.md) · [examples](domains/TS/examples.md) |
| [TV](domains/TV/) | Trial Visits | [spec](domains/TV/spec.md) · [assumptions](domains/TV/assumptions.md) · [examples](domains/TV/examples.md) |

### Relationship Domains

| Domain | Name | Files |
|--------|------|-------|
| [RELREC](domains/RELREC/) | Related Records | [spec](domains/RELREC/spec.md) · [assumptions](domains/RELREC/assumptions.md) · [examples](domains/RELREC/examples.md) |
| [RELSPEC](domains/RELSPEC/) | Related Specimens | [spec](domains/RELSPEC/spec.md) · [assumptions](domains/RELSPEC/assumptions.md) · [examples](domains/RELSPEC/examples.md) |
| [RELSUB](domains/RELSUB/) | Related Subjects | [spec](domains/RELSUB/spec.md) · [assumptions](domains/RELSUB/assumptions.md) · [examples](domains/RELSUB/examples.md) |
| [SUPPQUAL](domains/SUPPQUAL/) | Supplemental Qualifiers | [spec](domains/SUPPQUAL/spec.md) · [assumptions](domains/SUPPQUAL/assumptions.md) · [examples](domains/SUPPQUAL/examples.md) |

### Study Reference Domains

| Domain | Name | Files |
|--------|------|-------|
| [OI](domains/OI/) | Non-host Organism Identifiers | [spec](domains/OI/spec.md) · [assumptions](domains/OI/assumptions.md) · [examples](domains/OI/examples.md) |

---

## Terminology (91 files)

Controlled terminology extracted from SDTM Terminology.xlsx (1,005 codelists, 37,939 terms).

### Core Terminology (42 files)

| File | Scope |
|------|-------|
| [ae.md](terminology/core/ae.md) | Adverse Events codelists |
| [cp_part1.md](terminology/core/cp_part1.md), [cp_part2.md](terminology/core/cp_part2.md) | Cell Phenotyping codelists |
| [disposition.md](terminology/core/disposition.md) | Disposition codelists |
| [dm.md](terminology/core/dm.md) | Demographics codelists |
| [eg_part1.md](terminology/core/eg_part1.md) — [eg_part3.md](terminology/core/eg_part3.md) | ECG codelists |
| [findings_about.md](terminology/core/findings_about.md) | Findings About codelists |
| [general_part1.md](terminology/core/general_part1.md) — [general_part5.md](terminology/core/general_part5.md) | General/cross-domain codelists |
| [gf.md](terminology/core/gf.md) | Genomics Findings codelists |
| [interventions.md](terminology/core/interventions.md) | Interventions codelists |
| [is_domain_part1.md](terminology/core/is_domain_part1.md), [is_domain_part2.md](terminology/core/is_domain_part2.md) | Immunogenicity codelists |
| [lb_part1.md](terminology/core/lb_part1.md) — [lb_part4.md](terminology/core/lb_part4.md) | Laboratory codelists |
| [mi.md](terminology/core/mi.md) | Microscopic Findings codelists |
| [microbiology_part1.md](terminology/core/microbiology_part1.md) — [microbiology_part3.md](terminology/core/microbiology_part3.md) | Microbiology codelists |
| [oi.md](terminology/core/oi.md) | Non-host Organism codelists |
| [oncology_part1.md](terminology/core/oncology_part1.md), [oncology_part2.md](terminology/core/oncology_part2.md) | Oncology (TU/TR/RS) codelists |
| [other_part1.md](terminology/core/other_part1.md) — [other_part5.md](terminology/core/other_part5.md) | Other domain codelists (CV, MK, NV, OE, PE, RE, RP, SC, SR, SS, UR) |
| [pk_part1.md](terminology/core/pk_part1.md) — [pk_part4.md](terminology/core/pk_part4.md) | Pharmacokinetics codelists |
| [qs_part1.md](terminology/core/qs_part1.md) | Questionnaires core codelists |
| [special_purpose.md](terminology/core/special_purpose.md) | Special-purpose domain codelists |
| [trial_design.md](terminology/core/trial_design.md) | Trial Design codelists |
| [vs.md](terminology/core/vs.md) | Vital Signs codelists |

### Questionnaires Terminology (43 files)

Files: [questionnaires_part1.md](terminology/questionnaires/questionnaires_part1.md) — [questionnaires_part43.md](terminology/questionnaires/questionnaires_part43.md)

670 questionnaire-specific codelists covering instruments such as BDI-II, ADAS-COG, HAM-D, BPI, EORTC, SF-36, UPDRS, and hundreds more.

### Supplementary Terminology (6 files)

Files: [supplementary_part1.md](terminology/supplementary/supplementary_part1.md) — [supplementary_part6.md](terminology/supplementary/supplementary_part6.md)

188 supplementary codelists for specialized use cases.

---

## Source Documents

| Document | Version | Pages |
|----------|---------|-------|
| SDTM (Study Data Tabulation Model) | v2.0 Final (2021-11-29) | 74 |
| SDTMIG (Implementation Guide) | v3.4 | 461 |
| SDTMIG v3.4 xlsx | — | 63 domain specifications |
| SDTM Terminology xlsx | — | 1,005 codelists / 37,939 terms |

## Source: `ROUTING.md`

# SDTM Knowledge Base — Query Routing Guide

> AI 在回答 SDTM 相关问题时，**先读本文件确定查找路径，再读目标文件获取答案**。
> 不要猜测文件位置，按下方规则路由。

---

## 快速入口

| 需要什么 | 去哪里 |
|---------|--------|
| 按变量名查找 | [VARIABLE_INDEX.md](VARIABLE_INDEX.md) |
| 按域名查找 | [INDEX.md](INDEX.md) → domains/{DOMAIN}/ |
| 按 CT Code 查找 | [VARIABLE_INDEX.md](VARIABLE_INDEX.md) § 三、CT 交叉引用 |
| 域内交叉引用 | domains/{DOMAIN}/spec.md → 末尾 Cross References 段 |

---

## 路由规则

### 1. 变量定义类

**问法示例**: "AETERM 是什么？"、"AE 域有哪些变量？"、"USUBJID 出现在哪些域？"

```
问某个变量的定义/属性 (Label, Type, Role, Core)
  → 先查 VARIABLE_INDEX.md 定位该变量所在的域
  → 再读 domains/{DOMAIN}/spec.md 获取完整定义 (含 CDISC Notes)

问某个域有哪些变量
  → 读 domains/{DOMAIN}/spec.md（全部变量按 Order 排列）

问某个变量出现在哪些域
  → 查 VARIABLE_INDEX.md §一 (通用变量) 或 §二 (专属变量)

问某类角色的变量 (如所有 Identifier、所有 Timing)
  → 查 VARIABLE_INDEX.md（按 Role 列筛选）
  → 或读 model/02_observation_classes.md（class 级变量定义）
```

### 2. 编码/术语类

**问法示例**: "AESER 可以填什么值？"、"C66742 是什么 codelist？"、"LBTESTCD 的标准编码在哪？"

```
问某个变量的允许值/编码
  → 读 domains/{DOMAIN}/spec.md 找到该变量的 Controlled Terms 字段
  → 如果有 CT Code (如 C66742):
    → 方法 1: 查 VARIABLE_INDEX.md §三 找到 CT Code 对应的 terminology 文件
    → 方法 2: 查 spec.md 末尾 Cross References → Controlled Terminology 段（有直接链接）
  → 读对应的 terminology/ 文件获取完整值列表

问某个 CT Code 的含义和值列表
  → 查 VARIABLE_INDEX.md §三 → 找到 terminology 文件路径 → 读取

问问卷类编码 (BDI-II, ADAS-COG, HAM-D 等)
  → 读 terminology/questionnaires/ 下的文件
  → 文件较多 (43 个分片)，先在 INDEX.md § Questionnaires Terminology 确认范围

问编码规范的通用规则 (如何选择 codelist, extensible 含义)
  → 读 chapters/ch04_general_assumptions.md §4.2 (Coding and Controlled Terminology)
  → 读 chapters/ch10_appendices.md (Appendix C: Controlled Terminology)
```

### 3. 业务规则/假设类

**问法示例**: "AE 数据怎么收集？"、"EPOCH 怎么用？"、"什么时候拆分 domain？"

```
问某个域的业务规则和数据收集假设
  → 读 domains/{DOMAIN}/assumptions.md（领域专属规则）
  → 补充读 chapters/ch04_general_assumptions.md（通用规则，可能被引用）

问通用变量规则 (命名、Core、Origin、Natural Key 等)
  → 读 chapters/ch04_general_assumptions.md:
    - §4.1: 域级假设 (拆分域、命名、Core 定义、Origin metadata)
    - §4.2: 变量级假设 (编码、文本大小写、自由文本、多值处理)
    - §4.3: 观察类特定假设 (--OBJ, --CAT, result qualifiers)
    - §4.4: 时间变量 (--DTC, --DY, --DUR, EPOCH, reference time points)
    - §4.5: 其他假设

问变量角色/类型的定义 (Identifier, Topic, Qualifier 是什么)
  → 读 model/01_concepts_and_terms.md

问某个 Observation Class 的变量模板
  → 读 model/02_observation_classes.md (Interventions/Events/Findings 各自的变量列表)

问提交要求 (metadata, primary key, Define-XML)
  → 读 chapters/ch03_submitting_data.md
```

### 4. 域间关系类

**问法示例**: "AE 和 CM 怎么关联？"、"什么是 SUPPQUAL？"、"RELREC 怎么用？"

```
问两个域之间如何关联
  → 读 chapters/ch08_relationships.md（关联机制总述）
  → 读 domains/RELREC/（RELREC 变量定义 + 使用假设 + 示例）
  → 查两个域的 spec.md 末尾 Cross References → Related Domains 段

问 Supplemental Qualifier (SUPPQUAL / SUPP--)
  → 读 domains/SUPPQUAL/spec.md + assumptions.md
  → 读 chapters/ch08_relationships.md §8.4 (SUPP-- 详细规则)

问 RELREC 的用法和示例
  → 读 domains/RELREC/（spec + assumptions + examples）
  → 读 chapters/ch08_relationships.md §8.2-8.3

问标本关系 (specimen hierarchy)
  → 读 domains/RELSPEC/
  → 读 chapters/ch08_relationships.md §8.5

问受试者关系 (pooled subjects)
  → 读 domains/RELSUB/
  → 读 chapters/ch08_relationships.md §8.6
```

### 5. 实现示例类

**问法示例**: "给我看一个 AE 的数据示例"、"交叉试验的 TA 怎么建？"

```
问某个域的数据表示例
  → 读 domains/{DOMAIN}/examples.md

问试验设计示例 (并行/交叉/周期设计)
  → 读 domains/TA/examples.md（7 个完整试验设计示例，含 Mermaid 图）

问访视设计示例
  → 读 domains/TV/examples.md

问药代动力学数据示例
  → 读 domains/PC/examples.md + domains/PP/examples.md（共享数据集）
```

### 6. 概念/模型类

**问法示例**: "SDTM 的数据模型是什么？"、"怎么创建新 domain？"、"Events 和 Findings 有什么区别？"

```
问 SDTM 整体模型概念
  → 读 model/01_concepts_and_terms.md（概念总述）
  → 读 model/02_observation_classes.md（三大观察类）

问如何创建自定义 domain
  → 读 chapters/ch02_fundamentals.md（创建新域的流程和规则）
  → 读 model/02_observation_classes.md（确认适用的观察类）

问特殊用途域 (DM, CO, SE, SV, SM)
  → 读 model/03_special_purpose_domains.md

问 Associated Persons 数据
  → 读 model/04_associated_persons.md

问试验设计模型 (TE/TA/TV/TD/TM/TI/TS)
  → 读 model/05_study_level_data.md

问关系数据集模型 (RELREC/SUPP/POOLDEF/RELSUB)
  → 读 model/06_relationship_datasets.md
```

### 7. 跨域/全局查询类

**问法示例**: "哪些域用了 EPOCH？"、"Events class 包含哪些域？"、"哪些变量用了 C66742？"

```
问某个变量在哪些域中使用
  → 查 VARIABLE_INDEX.md §一 (通用变量区)

问某个 class 包含哪些域
  → 查 VARIABLE_INDEX.md §二 的域分组标题 (每个域标注了 class)
  → 或查 INDEX.md 的域列表 (按 class 分组)

问哪些变量引用了某个 CT Code
  → 查 VARIABLE_INDEX.md §三 (CT 交叉引用)

问 SDTM 版本变更/新增内容
  → 读 chapters/ch01_introduction.md §1.3 (Changes from v3.3)

问术语表/词汇定义
  → 读 chapters/ch10_appendices.md (Appendix B: Glossary)
```

---

## 多文件查询策略

当一个问题涉及多个文件时，按以下优先级读取：

1. **先定位**: VARIABLE_INDEX.md 或 INDEX.md（确定目标文件）
2. **再读主文件**: spec.md 或 assumptions.md（获取核心信息）
3. **按需补充**: Cross References 中的链接（扩展相关信息）
4. **通用规则兜底**: ch04_general_assumptions.md（如果主文件未覆盖）

**不要一次读取超过 3 个文件**。先读最可能包含答案的文件，根据其中的线索决定是否需要补充读取。

---

## 文件类型速查

| 文件类型 | 路径模式 | 内容 | 何时读 |
|---------|---------|------|--------|
| spec.md | domains/{DOMAIN}/spec.md | 变量定义表 (Order, Label, Type, CT, Role, Core, Notes) | 查变量属性 |
| assumptions.md | domains/{DOMAIN}/assumptions.md | 域专属业务规则，编号列表 | 查数据收集/处理规则 |
| examples.md | domains/{DOMAIN}/examples.md | 数据表示例 + Mermaid 图 | 查实际数据格式 |
| model/*.md | model/01-06_*.md | SDTM v2.0 概念模型 | 查模型定义/变量模板 |
| chapters/*.md | chapters/ch01-10_*.md | SDTMIG 实施指南通用章节 | 查通用规则/关系/提交 |
| terminology/*.md | terminology/{category}/*.md | CDISC 受控术语值列表 | 查编码允许值 |
| VARIABLE_INDEX.md | knowledge_base/VARIABLE_INDEX.md | 1523 变量反向索引 | 按变量名/CT Code 查找 |
| INDEX.md | knowledge_base/INDEX.md | 知识库总目录 | 初始导航 |
