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

### 1. `q68`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

Based on the retrieved context, the following domains use the Completion Status codelist **C66789** for their `--STAT` variable:

| Domain | Variable | What --STAT Indicates |
|--------|----------|------------------------|
| CM | CMSTAT | Indicates that a question about the occurrence of a prespecified intervention was not answered. Should be null or have a value of "NOT DONE." [Source: domains/CM/spec.md] |
| SC | SCSTAT | Indicates that the measurement was not done. Should be null if a result exists in SCORRES. [Source: domains/SC/spec.md] |
| SS | SSSTAT | Indicates a status assessment was not done. Should be null if a result exists in SSORRES. [Source: domains/SS/spec.md] |
| MS | MSSTAT | Indicates that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE." [Source: domains/MS/spec.md] |
| CP | CPSTAT | Indicates that the test was not performed or was attempted but did not generate a result. Should be null if a result exists in CPORRES. [Source: domains/CP/spec.md] |
| VS | VSSTAT | Indicates that a vital sign measurement was not done. Should be null if a result exists in VSORRES. [Source: domains/VS/spec.md] |
| BS | BSSTAT | Indicates that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE. [Source: domains/BS/spec.md] |
| PC | PCSTAT | Indicates a result was not obtained. Should be null if a result exists in PCORRES. [Source: domains/PC/spec.md] |
| QS | QSSTAT | Indicates that a question was not done or was not answered. Should be null if a result exists in QSORRES. [Source: domains/QS/spec.md] |
| IS | ISSTAT | Indicates a test was not done. Should be null if a result exists in ISORRES. [Source: domains/IS/spec.md] |
| CV | CVSTAT | Indicates that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE." [Source: domains/CV/spec.md] |
| AG | AGSTAT | Indicates that a question about a prespecified agent was not answered. Should be null or have a value of "NOT DONE." [Source: domains/AG/spec.md] |
| MB | MBSTAT | Indicates that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE." [Source: domains/MB/spec.md] |
| SR | SRSTAT | Indicates exam not done. Should be null if a result exists in SRORRES. [Source: domains/SR/spec.md] |
| MH | MHSTAT | Indicates that the prespecified question was not asked/answered. [Source: domains/MH/spec.md] |

**Common pattern across all domains:**
- **Label:** Completion Status
- **Type:** Char
- **Role:** Record Qualifier
- **Core:** Perm (Permissible)
- **Controlled Terms:** C66789

The general purpose of `--STAT` is to flag that a prespecified test, question, measurement, or intervention was **not done / not asked / not answered**, typically taking the value "NOT DONE" (per codelist C66789), and it should generally be null whenever a corresponding result exists in the domain's `--ORRES` (or equivalent) variable.

Note: The codelist code C66789 itself is confirmed present in the context for each of these `--STAT` variables. The individual controlled-terminology *values* within codelist C66789 (e.g., "NOT DONE") are not shown in the retrieved context with their own codes, so I have not attached any value-level codes.

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 2. `q56`

**裁判定位到的句子** (只用来定位, 不是判定):

> SU is classified as an **Interventions** domain

**答案原文**:

## SU (Substance Use) Domain Observation Class

SU is classified as an **Interventions** domain [Source: VARIABLE_INDEX.md -- SU — Substance Use (Interventions)].

## SUTRT Variable Definition

| Attribute | Value |
|-----------|-------|
| **Label** | Reported Name of Substance |
| **Type** | Char |
| **Role** | Topic |
| **Core** | Req (Required) |
| **Controlled Terms** | — (none specified) |

**CDISC Notes:** SUTRT captures the substance name (e.g., "CIGARETTES", "COFFEE"). It serves as the **topic variable** for the SU dataset — as such, it is a required variable and must always have a value [Source: domains/SU/spec.md -- SUTRT].

Per the domain assumptions, SUTRT captures the verbatim or the prespecified text collected for the substance, consistent with its role as the topic variable [Source: domains/SU/assumptions.md -- item_2].

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 3. `q77`

**裁判定位到的句子** (只用来定位, 不是判定):

> EPOCH (**Epoch**) is a **Timing** class variable, of Type **Char**, with **Core** designation **Perm** (Permissible), and Controlled Terms code **C99079** ...

**答案原文**:

EPOCH (**Epoch**) is a **Timing** class variable, of Type **Char**, with **Core** designation **Perm** (Permissible), and Controlled Terms code **C99079** (values are name-only unless individually confirmed in the terminology file, per sourcing rules) **[Source: domains/SR/spec.md]** **[Source: domains/UR/spec.md]** **[Source: domains/LB/spec.md]** **[Source: domains/PP/spec.md]** **[Source: domains/CP/spec.md]** **[Source: domains/FA/spec.md]** **[Source: domains/PC/spec.md]** **[Source: domains/IS/spec.md]** **[Source: domains/FT/spec.md]** **[Source: domains/DS/spec.md]** **[Source: domains/DA/spec.md]** **[Source: domains/RS/spec.md]** **[Source: domains/EG/spec.md]**.

EPOCH represents the trial epoch (e.g., "SCREENING", "TREATMENT", "FOLLOW-UP") associated with the date/time of the observation, and its exact CDISC Notes wording varies slightly by domain (e.g., "associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected" for LB, PC, PP, CP, IS, DA; "associated with the date/time of the observation" for SR, FA; "associated with the date/time at which the assessment was made" for RS, EG) **[Source: domains/LB/spec.md]** **[Source: domains/SR/spec.md]** **[Source: domains/RS/spec.md]**.

According to the general assumptions in Trial Arms (TA), EPOCH may be used as a timing variable in other datasets such as Exposure (EX) and Disposition (DS), and each distinct epoch (e.g., in a crossover trial with multiple treatment epochs) must have a distinct EPOCH value **[Source: domains/TA/assumptions.md]**.

According to the VARIABLE_INDEX.md cross-reference, EPOCH appears in 44 SDTM domains, including: AE, AG, CE, CM, CP, CV, DA, DS, DV, EC, EG, EX, FA, FT, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PP, PR, QS, RE, RP, RS, SC, SE, SR, SS, SU, TA, TR, TU, UR, VS **[Source: VARIABLE_INDEX.md]**.

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 4. `q21`

**裁判定位到的句子** (只用来定位, 不是判定):

> **LBTESTCD** (Order 8) is a variable within the LB (Laboratory Test Results) domain, which belongs to the **Findings** observation class.

**答案原文**:

# LBTESTCD Variable in the LB Domain

**LBTESTCD** (Order 8) is a variable within the LB (Laboratory Test Results) domain, which belongs to the **Findings** observation class.

## Definition

- **Label:** Lab Test or Examination Short Name
- **Type:** Char
- **Role:** Topic
- **Core:** Req (Required)
- **Controlled Terms:** C65047 (Laboratory Test Code)

## CDISC Notes / Description

LBTESTCD is the short name of the measurement, test, or examination described in **LBTEST**. It can be used as a column name when converting the dataset from a vertical (long) format to a horizontal (wide) format.

**Naming constraints:**
- Cannot exceed **8 characters** in length.
- Cannot **start with a number** (e.g., "1TEST" is not a valid value).
- Cannot contain characters **other than letters, numbers, or underscores**.

**Examples:** "ALT", "LDH"

[Source: domains/LB/spec.md]

## Controlled Terminology

LBTESTCD is coded against the **Laboratory Test Code (C65047)** codelist. This codelist is found in the terminology file `terminology/core/lb_part2.md`. [Source: domains/LB/spec.md] [Source: VARIABLE_INDEX.md]

Note: The C65047 codelist is confirmed as the codelist code for LBTESTCD from the source metadata; however, the individual permissible test code values within C65047 (e.g., specific short names) were not present in the retrieved context, so their exact term-level entries would need to be confirmed by reading `terminology/core/lb_part2.md` directly.

## Relationship to Other Variables

LBTESTCD works together with **LBTEST** (Order 9, Role: Synonym Qualifier, Core: Req, CT: C67154 — Laboratory Test Name), which provides the verbatim/full name corresponding to the short code in LBTESTCD (e.g., "ALT" ↔ "Alanine Aminotransferase"). [Source: domains/LB/spec.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 5. `s04`

**裁判定位到的句子** (只用来定位, 不是判定):

> **Type:** Char
**Role:** Record Qualifier
**Core:** Exp

**答案原文**:

**AEACN (Action Taken with Study Treatment)**

- **Controlled Terminology codelist code:** C66767 [Source: domains/AE/spec.md -- AEACN]
- **Label:** Action Taken with Study Treatment
- **Type:** Char
- **Role:** Record Qualifier
- **Core:** Exp

According to the CDISC Notes field, AEACN describes changes to the study treatment as a result of the event, and is specifically for the relationship to study treatment (as distinct from AEACNOTH, which covers actions unrelated to dose adjustments of study treatment). The example ICH E2B values listed are:

- "DRUG WITHDRAWN"
- "DOSE REDUCED"
- "DOSE INCREASED"
- "DOSE NOT CHANGED"
- "UNKNOWN"
- "NOT APPLICABLE"

[Source: domains/AE/spec.md -- AEACN]

Note: these individual value names are given as illustrative examples in the CDISC Notes text rather than as rows from the C66767 terminology codelist file itself, so per sourcing rules I have not attached individual NCI codes to any of these values — only the codelist-level code C66767 is confirmed from the spec [Source: domains/AE/spec.md -- Controlled Terminology] [Source: VARIABLE_INDEX.md -- §三 CT 交叉引用: C66767].

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 6. `q40`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

# Collected vs. Derived Data in SDTM

## Definitions and Distinction

SDTM datasets include multiple categories of data, distinguished by how the value came to exist:
- **Data as originally collected or received**
- **Data from the protocol**
- **Assigned data**
- **Derived data**

**[Source: chapters/ch02_fundamentals.md -- 2.2 Datasets and Domains]**

The core distinction between "collected" and "derived":
- **Collected data**: Values that come directly from a data source (CRF, a vendor, or a device) without transformation/computation by the sponsor. Notably, **a value derived by a central lab according to its own procedures is considered collected rather than derived** — the perspective is from the sponsor's data flow, not the ultimate origin of the calculation. **[Source: domains/LB/assumptions.md -- item_6]**
- **Derived data**: Values computed/transformed by the sponsor via some algorithm from other data (e.g., a total/subtotal score computed by the sponsor from item-level responses). "Derived data should be traceable to some derivation algorithm." **[Source: chapters/ch04_general_assumptions.md -- 4.1.8 Origin Metadata]**

A useful illustration is in the QRS/Questionnaires domains (QS, FT): subtotal/total scores are generally treated as **captured (collected)** data if they appear on the CRF, or in the instrument's manual/reference paper, or are otherwise known to be included in the eCRF workflow and part of the instrument's controlled terminology. They are only flagged as **derived** if the sponsor computes them operationally (in which case --DRVFL = "Y"). If the score comes from a central provider/vendor, it goes into --ORRES and --DRVFL is left null (treated as collected). **[Source: domains/QS/assumptions.md -- item_4; domains/FT/assumptions.md -- item_4]**

## How Origin Is Indicated

The origin of a variable's value is **not indicated by an SDTM dataset variable itself**, but rather through **Origin metadata in the Define-XML document**:

- **Origin Metadata for Variables** (§4.1.8.1): The Define-XML "origin" element unambiguously communicates where the data originated — e.g., collected (CRF, vendor, device), derived, or assigned. CRF-collected data should be traceable to an annotated CRF, and derived data should be traceable to a derivation algorithm. The Define-XML specification is the definitive source of allowable origin values. **[Source: chapters/ch04_general_assumptions.md -- 4.1.8 Origin Metadata]**

- **Origin Metadata for Records** (§4.1.8.2): Sponsors must be careful, because a "derived" origin designation implies *all* values for that variable were derived, and "collected on the CRF" implies that applies to *all* records for that variable. When a single variable contains a mix of collected and derived values across different records (e.g., in QS, some records are collected CRF responses while others are derived total scores), the origin must instead be described using **value-level metadata** in the Define-XML document, rather than a single dataset-level origin designation. **[Source: chapters/ch04_general_assumptions.md -- 4.1.8 Origin Metadata]**

In domain-specific practice (e.g., QS, FT), the flag variable **--DRVFL** ("Derived Flag") is used at the record level to indicate whether a specific record's result was operationally derived by the sponsor ("Y") versus collected/captured — this works alongside, and is distinct from, the Define-XML origin metadata concept. **[Source: domains/QS/assumptions.md -- item_4; domains/FT/assumptions.md -- item_4]**

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 7. `s02`

**裁判定位到的句子** (只用来定位, 不是判定):

> **Role:** Topic

**答案原文**:

## QNAM (Supplemental Qualifiers)

**QNAM** — Qualifier Variable Name
- **Type:** Char
- **Role:** Topic
- **Core:** Req
- **Controlled Terms:** — (none; it is a sponsor-defined short name, though the CDISC Notes indicate certain common QNAM/QLABEL codes are provided in Appendix C1, Supplemental Qualifiers Name Codes)

**Definition:** The short name of the qualifier variable, which is used as a column name in a domain view with data from the parent domain. This will often be the column name in the sponsor's operational dataset. **[Source: domains/SUPPQUAL/spec.md]** **[Source: chapters/ch08_relationships.md — 8.4.1 Supplemental Qualifiers (SUPP--)]**

### Character constraints

- **Maximum length:** QNAM cannot be longer than **8 characters**.
- **Allowed characters:** letters, numbers, or underscores only.
- **Additional restriction:** QNAM cannot start with a number (e.g., "1TEST" is not valid).

**[Source: domains/SUPPQUAL/spec.md]** **[Source: chapters/ch08_relationships.md — 8.4.1 Supplemental Qualifiers (SUPP--)]** **[Source: VARIABLE_INDEX.md — SUPPQUAL — Supplemental Qualifiers for [domain name] (Relationship)]**

### Related naming conventions

- Additional QNAM values may be created as needed, following the guidelines in the CDISC Notes for QVAL; Appendix C1 provides controlled terminology for QNAM and QLABEL for some of the most common supplemental qualifiers. **[Source: chapters/ch08_relationships.md — Key Rules]**
- When a standard domain variable name already occupies all 8 characters and a secondary evaluator's QNAM needs a numeric suffix (e.g., for primary/secondary attributions per Section 4.5.4), the sponsor should **replace the last character** of the 8-character name with the suffix digit rather than appending it (e.g., AERELNST → AERELNS1, since appending "1" would exceed 8 characters). **[Source: chapters/ch04_general_assumptions.md — 4.5.4 Evaluators in the Interventions and Events Observation Classes]**
- The same replace-last-character rule applies when QNAM needs sequential numeric suffixes for text strings exceeding 200 characters (e.g., AEACNOTH → AEACNOT1, AEACNOT2, etc.). **[Source: chapters/ch04_general_assumptions.md — 4.5.3.2 Text Strings Greater than 200 Characters in Other Variables]**

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 8. `q100`

**裁判定位到的句子** (只用来定位, 不是判定):

> In the TA (Trial Arms) domain, **ARMCD** (Planned Arm Code) has: - **Role:** Topic - **Core:** Req (Required) - Type: Char

**答案原文**:

In the TA (Trial Arms) domain, **ARMCD** (Planned Arm Code) has:
- **Role:** Topic
- **Core:** Req (Required)
- Type: Char

It is limited to 20 characters and does not have special character restrictions; the maximum length is longer than that for other "short" variables to accommodate values needed for crossover trials (e.g., a 7-period crossover using 2-character abbreviations with hyphens could reach 20 characters) **[Source: domains/TA/spec.md]**.

Regarding **ETCD**, the retrieved context does not contain the TA spec.md row for ETCD directly. However, from the TA/DM/SE-related context, ETCD is the Element Code, used to identify a specific Trial Element within the trial design — TA associates each arm with a sequence of Elements identified by ETCD, and the Subject Elements (SE) domain uses ETCD to record which elements a subject actually passed through (as shown in the SE example table with ETCD values like "SCRN", "DBA", "OA") **[Source: domains/DM/examples.md]**. I don't have the authoritative TA spec.md row (Label/Type/Role/Core/CDISC Notes) for ETCD in the retrieved context, so I cannot confirm its exact Role/Core designation in TA from this material — please consult domains/TA/spec.md directly for that row.

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---
