# 人判包 — 分类归属 (b) 层

> 判据: 无归属断言 ⇒ PASS(N/A) · 有断言且与下表一致 ⇒ PASS · 不一致或权威出处是编的 ⇒ FAIL

## 权威表

| Dataset | Class |
|---|---|
| CO | Special Purpose |
| DM | Special Purpose |
| SE | Special Purpose |
| SM | Special Purpose |
| SV | Special Purpose |
| AG | Interventions |
| CM | Interventions |
| EC | Interventions |
| EX | Interventions |
| ML | Interventions |
| PR | Interventions |
| SU | Interventions |
| AE | Events |
| BE | Events |
| CE | Events |
| DS | Events |
| DV | Events |
| HO | Events |
| MH | Events |
| BS | Findings |
| CP | Findings |
| CV | Findings |
| DA | Findings |
| DD | Findings |
| EG | Findings |
| FT | Findings |
| GF | Findings |
| IE | Findings |
| IS | Findings |
| LB | Findings |
| MB | Findings |
| MI | Findings |
| MK | Findings |
| MS | Findings |
| NV | Findings |
| OE | Findings |
| PC | Findings |
| PE | Findings |
| PP | Findings |
| QS | Findings |
| RE | Findings |
| RP | Findings |
| RS | Findings |
| SC | Findings |
| SS | Findings |
| TR | Findings |
| TU | Findings |
| UR | Findings |
| VS | Findings |
| FA | Findings About |
| SR | Findings About |
| TA | Trial Design |
| TD | Trial Design |
| TE | Trial Design |
| TI | Trial Design |
| TM | Trial Design |
| TS | Trial Design |
| TV | Trial Design |
| RELREC | Relationship |
| RELSPEC | Relationship |
| RELSUB | Relationship |
| SUPP-- | Relationship |
| OI | Study Reference |

## 待判条目

### 1. `q16`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

## AESEV — Severity/Intensity

**Variable definition** [Source: domains/AE/spec.md -- AESEV]
- **Order:** 27
- **Label:** Severity/Intensity
- **Type:** Char
- **Controlled Terms:** C66769
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE".

**Codelist code:** **C66769** — this codelist is referenced by exactly one variable in SDTMIG v3.4, AE.AESEV [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C66769].

**Allowed values:** The retrieved context does not include the value rows of codelist C66769, so I cannot give the authoritative complete list. The values explicitly cited in the AESEV CDISC Notes as examples are:

- MILD
- MODERATE
- SEVERE

[Source: domains/AE/spec.md -- AESEV]

These are given as *examples* in the specification, so the full, definitive set of terms (and each term's individual NCI concept code) must be confirmed against the CDISC Controlled Terminology file for C66769 (see `terminology/core/ae.md`). Note also that the analogous severity codelist for Clinical Events is different: CE.CESEV uses codelist C165643 [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C165643].

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 2. `q102`

**裁判定位到的句子** (只用来定位, 不是判定):

> | **Role** | Record Qualifier |

**答案原文**:

## VSPOS

| Attribute | Value |
|---|---|
| **Variable** | VSPOS |
| **Order** | 11 |
| **Label** | Vital Signs Position of Subject |
| **Type** | Char |
| **Controlled Terms** | C71148 |
| **Role** | Record Qualifier |
| **Core** | Perm |
| **CDISC Notes** | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |

[Source: domains/VS/spec.md -- VSPOS]

## Controlled Terminology

VSPOS uses the **Position** codelist, **C71148** (Extensible: Yes), which is shared across domains — it is referenced by CV.CVPOS, EG.EGPOS, FT.FTPOS, MK.MKPOS, RE.REPOS, and VS.VSPOS. [Source: domains/VS/spec.md -- Controlled Terminology] [Source: terminology/core/interventions.md -- Position] [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C71148]

## Selected values from Position (C71148)

Directly answering your two examples:

- **PRONE** (C62165) — face-down: "An anterior recumbent body position whereby the person lies on its stomach and faces downward. (NCI)"
- **FOWLERS** (C62173) — semi-sitting with head of adjustable bed elevated ~60–90 cm, usually 45°–60° angulation
- **SEMI-FOWLERS** (C62174) — semi-sitting/semi-reclined with head elevated at approximately 30°

Other values in the codelist:

| Code | Submission Value |
|---|---|
| C77532 | DECUBITUS |
| C100758 | LATERAL DECUBITUS |
| C62172 | LEFT LATERAL DECUBITUS |
| C62171 | RIGHT LATERAL DECUBITUS |
| C62169 | REVERSE TRENDELENBURG |
| C62168 | TRENDELENBURG |
| C111310 | SEMI-RECUMBENT |
| C62122 | SITTING |
| C150885 | SITTING, LEGS DEPENDENT |
| C92604 | SLING |
| C62166 | STANDING |
| C174357 | STANDING, BENT FORWARD |
| C62167 | SUPINE |
| C90480 | UNCONSTRAINED |

[Source: terminology/core/interventions.md -- Position]

## Related note

Associations between specific vital sign tests and their qualifier codelists (including position) are described in the VS codetable available at https://www.cdisc.org/standards/terminology/controlled-terminology. [Source: domains/VS/assumptions.md -- item_3]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 3. `q100`

**裁判定位到的句子** (只用来定位, 不是判定):

> | **Role** | **Topic** |

**答案原文**:

## ARMCD in TA

| Attribute | Value |
|---|---|
| **Order** | 3 |
| **Label** | Planned Arm Code |
| **Type** | Char |
| **Controlled Terms** | (none) |
| **Role** | **Topic** |
| **Core** | **Req** |

CDISC Notes: "ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other 'short' variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20." [Source: domains/TA/spec.md -- ARMCD]

Note the contrast with the same-named variable in other domains: in DM, ARMCD is a **Record Qualifier / Exp** [Source: domains/DM/spec.md -- ARMCD], and in TV it is likewise **Record Qualifier / Exp** [Source: domains/TV/spec.md -- ARMCD]. ARMCD appears in 3 domains: DM, TA, TV [Source: VARIABLE_INDEX.md -- §一 通用变量: ARMCD]. TA is the source of truth for arm codes: with the exception of multistage arm-assignment trials, DM.ARMCD/ACTARMCD must be populated with ARMCD values from the TA dataset, and the one-to-one ARM↔ARMCD relationship in TA must be preserved in DM [Source: domains/DM/assumptions.md -- item_4].

## ETCD

The retrieved context does **not** include the TA specification row for ETCD, so I cannot give you its authoritative Label, Type, Role, Core, or CDISC Notes. What the available context supports:

- The Trial Design Model divides each arm (a planned path through the trial covering the entire time of the trial) into **study cells**, one per epoch, and elements are the building blocks referenced by the Trial Elements (TE) dataset [Source: domains/TA/assumptions.md -- overview].
- ETCD functions as the short code for an element and is paired one-to-one with the descriptive ELEMENT name; this pairing is visible in the Subject Elements (SE) data, e.g. ETCD "SCRN"/ELEMENT "Screen", ETCD "DBA"/ELEMENT "Treatment A", ETCD "OA"/ELEMENT "Open Drug A", ETCD "RSC"/ELEMENT "Rescue" [Source: domains/DM/examples.md -- Example 3].

For the definitive ETCD attributes in TA (and its ordering/Core status), read `domains/TA/spec.md` in full and `domains/TE/spec.md` for the element definitions it references.

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 4. `q57`

**裁判定位到的句子** (只用来定位, 不是判定):

> It is built on the **Interventions** observation class

**答案原文**:

## PR (Procedures) Domain — Purpose

PR captures procedures performed on/for a subject. It is built on the **Interventions** observation class [Source: domains/PR/assumptions.md]. Key scoping rules:

- The extent of physiological effect may range from observable to microscopic; **regardless of the extent of effect or whether it is collected in the study, all collected procedures are represented in this domain**. The protocol design should specify whether procedure information will be collected [Source: domains/PR/assumptions.md].
- **Measurements/results obtained from procedures are NOT placed in PR** — they go to their respective Findings domain(s). Example: a biopsy procedure is represented in PR, while the histopathology evaluation of the tissue sample goes to MI (Microscopic Findings). Whether the PR–MI relationship is described in RELREC depends on whether the relationship was collected (explicitly or implicitly) [Source: domains/PR/assumptions.md].
- Related pattern in oncology: when additional data are collected about a procedure used for tumor/lesion identification, the procedure data are stored in PR, and the link to the tumor/lesion identification record is recorded using RELREC [Source: domains/TU/assumptions.md].

Example procedure types in scope [Source: domains/PR/assumptions.md]:

| Type | Examples |
|---|---|
| Disease screening | mammogram, pap smear |
| Endoscopic examinations | arthroscopy, diagnostic/therapeutic colonoscopy, diagnostic/therapeutic laparoscopy |
| Diagnostic tests | amniocentesis, biopsy, catheterization, cutaneous oximetry, finger stick, fluorophotometry, imaging (DXA, CT, MRI), phlebotomy, pulmonary function test, skin test, stress test, tympanometry |
| Therapeutic procedures | ablation therapy, catheterization, cryotherapy, mechanical ventilation, phototherapy, radiation therapy, thermotherapy |
| Surgical procedures | curative/diagnostic/palliative/therapeutic/prophylactic surgery, resection, stenting, hysterectomy, tubal ligation, implantation |

## PRTRT — the Topic Variable

| Attribute | Value |
|---|---|
| **Variable** | PRTRT |
| **Order** | 9 |
| **Label** | Reported Name of Procedure |
| **Type** | Char |
| **Controlled Terms** | (none) |
| **Role** | Topic |
| **Core** | **Req** (Required) |

**CDISC Notes:** Name of procedure performed, either preprinted or collected on a CRF [Source: domains/PR/spec.md].

Because PRTRT is Core = **Req**, it must always be present and populated in the PR dataset.

### Qualifiers that reference PRTRT
- **PRDECOD** (Standardized Procedure Name, Char, Synonym Qualifier, Perm, CT **C101858** = Procedure): standardized/dictionary-derived name of PRTRT. If the codelist "PROCEDUR" is not used, the sponsor is expected to provide the dictionary name and version in the external codelist element of the Define-XML document; if a term has no decode value, PRDECOD is null [Source: domains/PR/spec.md].
- **PRROUTE** (Route of Administration, Char, Variable Qualifier, Perm, CT **C66729**): route of administration for PRTRT [Source: domains/PR/spec.md].
- **PRDOSE** (Dose, Num, Record Qualifier, Perm): amount of PRTRT administered; not populated when PRDOSTXT is populated [Source: domains/PR/spec.md].
- **PRPRESP** (Pre-specified, Char, Variable Qualifier, Perm, CT **C66742**): used when a specific procedure is pre-specified on a CRF; values should be "Y" or null [Source: domains/PR/spec.md].

### Example of PRTRT population
Verbatim procedure names such as "Wisdom Teeth Extraction", "Reset Broken Arm", "Prostate Examination", "Endoscopy", "Heart Transplant" — here the sponsor chose to represent long verbatim text in mixed case (see Section 4.2.4, Text Case in Submitted Data) [Source: domains/PR/examples.md].

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 5. `s05`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

## VSTESTCD — Controlled Terminology

**Codelist code:** **C66741**

- **Codelist name:** Vital Signs Test Code — referenced by **VS.VSTESTCD** [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C66741]
- The VS specification links it as "Vital Signs Test Code (C66741) — VSTESTCD", with the value list residing in the VS terminology file [Source: domains/VS/spec.md -- Controlled Terminology]
- Companion codelist for the decoded name: **Vital Signs Test Name (C67153)** for **VSTEST** [Source: domains/VS/spec.md -- Controlled Terminology] [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C67153]

## Items I cannot confirm from the retrieved context

1. **Extensibility:** the retrieved context does not state whether C66741 is extensible or non-extensible. This must be confirmed in the terminology file (`terminology/core/vs.md`), which carries the codelist's Extensible flag.

2. **Example VSTESTCD values for blood pressure and heart rate:** the retrieved context does not contain any rows from the C66741 value list, so I cannot supply the actual short codes without risk of error. What *is* shown are **VSTEST** (test name) examples from the CDISC Notes: "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Mass Index" — note these are test *names*, not TESTCD values, and heart rate is not among them [Source: domains/VS/spec.md -- VSTEST]. The corresponding VSTESTCD codes (and any heart-rate term) must be read from `terminology/core/vs.md`.

## Related note

Associations between particular vital sign tests and their qualifier codelists (e.g., VSPOS, VSLOC, VSORRESU) are documented in the **VS codetable**, published at https://www.cdisc.org/standards/terminology/controlled-terminology [Source: domains/VS/assumptions.md -- item_3].

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 6. `q21`

**裁判定位到的句子** (只用来定位, 不是判定):

> | **Domain** | LB — Laboratory Test Results (Findings class) |

**答案原文**:

## LBTESTCD — Lab Test or Examination Short Name

| Attribute | Value |
|---|---|
| **Domain** | LB — Laboratory Test Results (Findings class) |
| **Order** | 8 |
| **Label** | Lab Test or Examination Short Name |
| **Type** | Char |
| **Controlled Terms** | C65047 — *Laboratory Test Code* |
| **Role** | Topic |
| **Core** | Req (Required) |

[Source: domains/LB/spec.md -- LBTESTCD] [Source: VARIABLE_INDEX.md -- LB — Laboratory Test Results (Findings)]

### Role

LBTESTCD is the **Topic** variable of the LB domain — i.e., it carries the focus of the observation (which lab test was performed). Because it is **Required**, it must be present and populated on every record. Its companion variable **LBTEST** (Lab Test or Examination Name, Char, Synonym Qualifier, Req, CT **C67154**) carries the corresponding long/verbatim test name, limited to 40 characters. [Source: domains/LB/spec.md -- LBTEST]

### Controlled terminology

- Codelist code **C65047** (Laboratory Test Code), located in `terminology/core/lb_part2.md`; it is referenced only by LB.LBTESTCD. [Source: domains/LB/spec.md -- Controlled Terminology] [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C65047]
- The paired name codelist is **C67154** (Laboratory Test Name) in `terminology/core/lb_part3.md`, used by LBTEST. [Source: domains/LB/spec.md -- Controlled Terminology] [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C67154]
- Note: CDISC publishes a **LOINC to LB Mapping Codetable** (at https://www.cdisc.org/standards/terminology/controlled-terminology) that can be used to identify the appropriate CDISC CT value for a test with a given LOINC code (LBLOINC). [Source: domains/LB/assumptions.md -- item_8]

### Naming constraints

Per the CDISC Notes for LBTESTCD [Source: domains/LB/spec.md -- LBTESTCD]:

1. It is the **short name** of the measurement, test, or examination described in LBTEST.
2. **Maximum 8 characters.**
3. **Cannot start with a number** (e.g., "1TEST" is invalid).
4. **Cannot contain characters other than letters, numbers, or underscores.**
5. It is designed so it can serve as a **column name** when transposing a dataset from vertical (normalized) to horizontal format.

Examples: `ALT`, `LDH` (with LBTEST values "Alanine Aminotransferase", "Lactate Dehydrogenase" respectively). [Source: domains/LB/spec.md -- LBTESTCD] [Source: domains/LB/spec.md -- LBTEST]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 7. `q41`

**裁判定位到的句子** (只用来定位, 不是判定):

> The SDTM contains **4 types of datasets that are not based on the general observation classes**, one of which is the Trial Design Model: ... | **Trial Design Model (TDM)** | **Study design information, not subject data** | **TA, TE** | Section 7 |

**答案原文**:

## Trial Design Model (TDM) — position within SDTM

The SDTM contains **4 types of datasets that are not based on the general observation classes**, one of which is the Trial Design Model:

| Type | Description | Examples | Section |
|------|-------------|----------|---------|
| Special-purpose domains | Subject-level data not conforming to a GOC | DM, CO, SE, SV | Section 5 |
| **Trial Design Model (TDM)** | **Study design information, not subject data** | **TA, TE** | Section 7 |
| Relationship datasets | Describe relationships among datasets/records | RELREC, SUPP-- | Section 8 |
| Study Reference datasets | Study-specific terminology | DI, OI | Section 9 |

[Source: chapters/ch02_fundamentals.md -- 2.4 Datasets Other than General Observation Class Domains]

At the model level, study-level data is divided into two kinds: "The SDTM includes 2 types of study-level data: **trial design data** and **study reference data**." [Source: model/05_study_level_data.md -- Overview] The conceptual map confirms that "Domains for Study-Level Data" include the **Trial Design Model** (an extensible set of domains) and the **Study Reference Datasets** [Source: model/01_concepts_and_terms.md -- 2.1 Model Concepts and Terms — Variables]. The general framework of the SDTM — general observation classes, special-purpose domains, **trial design model datasets**, relationship datasets, and study references — is described in the SDTM itself [Source: chapters/ch04_general_assumptions.md -- 4.1.1 Review Study Data Tabulation Model and Implementation Guide].

## The Trial Design datasets (SDTMIG v3.4)

The following domains are designated Trial Design in the knowledge base, each pointing to the Trial Design class definition in the model:

| Domain | Name | Class designation source |
|--------|------|--------------------------|
| TA | Trial Arms | [Source: domains/TA/spec.md -- Model Definition] |
| TE | Trial Elements | [Source: domains/TE/spec.md -- Model Definition] |
| TV | Trial Visits | [Source: domains/TV/spec.md -- Model Definition] |
| TD | Trial Disease Assessments | [Source: domains/TD/spec.md -- Model Definition] |
| TM | Trial Disease Milestones | [Source: domains/TM/spec.md -- Model Definition] |
| TI | Trial Inclusion/Exclusion Criteria | [Source: domains/TI/spec.md -- Model Definition] |
| TS | Trial Summary | [Source: domains/TS/spec.md -- Model Definition] |

(The SDTM v2.0 model chapter on study-level data covers the trial design datasets plus the study reference datasets DI and OI [Source: model/05_study_level_data.md -- Overview].)

## What kind of information they capture

- **Study design rather than subject data** — TDM datasets describe the design of the study (e.g., arms, elements), and are not observations about subjects [Source: chapters/ch02_fundamentals.md -- 2.4 Datasets Other than General Observation Class Domains].
- **Eligibility and trial characteristics** — the TI/TS section of the Trial Design datasets describes:
  - subject eligibility criteria for trial participation (TI, Trial Inclusion/Exclusion Criteria)
  - the characteristics of the trial (TS, Trial Summary)
  
  "The TI and TS datasets are tabular synopses of parts of the study protocol." TI contains **all** inclusion and exclusion criteria for the trial, thereby providing information that may not be present in subject-level data; by contrast, the IE domain contains records only for criteria that subjects did **not** meet [Source: domains/TI/assumptions.md -- overview].
- **Rule variables** — TDM datasets are the location of the SDTM **Rule** variable role, which "describe[s] the condition to start, end, branch, or loop in the Trial Design Model" [Source: chapters/ch02_fundamentals.md -- 2.1 Observations and Variables]; [Source: model/01_concepts_and_terms.md -- 2.1 Model Concepts and Terms — Variables].
- **Role shifts across TDM vs. subject domains** — the same variable can play different roles in trial design vs. general observation class datasets; e.g., ARMCD is the **topic** variable in TA but a **record qualifier** in DM and TV [Source: model/01_concepts_and_terms.md -- 2.1 Model Concepts and Terms — Variables].

## Limitation of the retrieved context

The context does not contain the detailed content descriptions for TA (arms as ordered sequences of elements), TE (element definitions and start/end rules), TV (planned visits), TD (planned disease-assessment schedule), or TM (planned disease milestones). For those specifics, consult `domains/{TA|TE|TV|TD|TM}/spec.md` and `assumptions.md`, plus `model/05_study_level_data.md` and SDTMIG Section 7 (Trial Design Model). Detailed trial design implementation examples (parallel, crossover, cyclic designs) are in `domains/TA/examples.md`.

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 8. `q39`

**裁判定位到的句子** (只用来定位, 不是判定):

> The domain that implements this concept is **FA — "Findings About Events or Interventions"**, and it is listed among the **Findings** domains in the knowledge base domain listing.

**答案原文**:

## Answer scope note

The retrieved context is **insufficient** to answer this question substantively. All 15 retrieved chunks are the "Model Definition" cross-reference stubs from various Findings-class domain specs (IS, MI, RP, LB, SS, TU, CV, EG, MB, NV, OE, PC, PP, RE, RS), each containing only a link to the Findings class definition — no descriptive text about the Findings About class or its distinguishing variables was returned. [Source: domains/LB/spec.md] [Source: domains/EG/spec.md]

## What can be stated from available material

- The domain that implements this concept is **FA — "Findings About Events or Interventions"**, and it is listed among the **Findings** domains in the knowledge base domain listing. [Source: INDEX.md]
- The generic Findings class variable template (including the result qualifiers and the `--OBJ` variable) is defined at the model level. [Source: model/02_observation_classes.md]

I will not characterize the semantic difference (e.g., how the finding's object is represented, how records link back to the parent event/intervention record, or when to use FA vs. a standard Findings domain) without the actual source text, since that would risk misstating normative rules.

## Where to retrieve the answer

Per the routing guide, the following should be read to answer this properly:

1. **domains/FA/assumptions.md** — domain-specific rules for Findings About, including when FA is appropriate versus a standard Findings domain. [Source: ROUTING.md]
2. **model/02_observation_classes.md** — the Findings class variable template, including `--OBJ`. [Source: ROUTING.md]
3. **chapters/ch04_general_assumptions.md §4.3** — observation-class–specific assumptions, explicitly covering `--OBJ`, `--CAT`, and result qualifiers. [Source: ROUTING.md]
4. **chapters/ch08_relationships.md** and **domains/RELREC/** — for how FA records are related to their parent event/intervention records. [Source: ROUTING.md]
5. **terminology/core/findings_about.md** — Findings About codelists. [Source: INDEX.md]

Please re-query against those paths (particularly `domains/FA/assumptions.md` and `chapters/ch04_general_assumptions.md`) and I can give a precise, cited comparison.

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---
