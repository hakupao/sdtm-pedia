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
