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

### 1. `q40`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

In SDTM:

- **Collected data** are data captured or received from a source, such as a CRF, vendor, central laboratory, or device. A value calculated by a central laboratory according to its own procedures is still considered **collected**, rather than sponsor-derived. [Source: chapters/ch04_general_assumptions.md] [Source: domains/LB/assumptions.md]
- **Derived data** are values produced through a sponsor-applied derivation or calculation algorithm. Derived data should be traceable to the applicable derivation algorithm. SDTM datasets may contain both originally collected/received data and derived data. [Source: chapters/ch04_general_assumptions.md] [Source: chapters/ch02_fundamentals.md]

### How origin is indicated

Origin is documented in the **Define-XML `Origin` metadata**, not inferred merely from the SDTM value:

- At **variable level**, `Origin` indicates where all values of that variable originated—for example, collected from a CRF, vendor, or device; derived; or assigned. CRF origins should be traceable to an annotated CRF, while derived origins should be traceable to a derivation algorithm. The Define-XML specification is the definitive source for allowable `Origin` values. [Source: chapters/ch04_general_assumptions.md]
- If a variable contains values with different origins—for example, collected questionnaire responses and a derived total score—the origins must be specified using **value-level metadata** in Define-XML. A variable-level `Origin` of derived means all values in that variable were derived; similarly, a CRF-collected origin applies to all values. [Source: chapters/ch04_general_assumptions.md]

In domains where `--DRVFL` is applicable, it can identify particular sponsor-derived records. For example, sponsor-derived QRS subtotal or total scores are flagged with `--DRVFL = "Y"`, whereas scores received from a central provider/vendor have `--DRVFL` null and are treated as captured data. `--DRVFL` is therefore a domain/record-level indicator used under applicable domain rules; it does not replace Define-XML `Origin` metadata. [Source: domains/QS/assumptions.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 2. `q102`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

### VSPOS

- **Label:** Vital Signs Position of Subject  
- **Type:** Char  
- **Role:** Record Qualifier  
- **Core:** Perm  
- **Controlled Terms:** **Position (C71148)**  
- **Definition:** Records the subject’s position during a vital-sign measurement or examination. [Source: domains/VS/spec.md]

Examples from **Position (C71148)** include:

- **PRONE** — face-down, lying on the stomach.
- **FOWLERS** — semi-sitting, typically with the head of an adjustable bed elevated about 45–60 degrees.
- **SEMI-FOWLERS** — semi-sitting or semi-reclined, with the head elevated approximately 30 degrees.
- **SUPINE** — lying on the back, face upward.
- **SITTING**
- **STANDING** [Source: terminology/core/interventions.md]

The **Position (C71148)** codelist is extensible. [Source: terminology/core/interventions.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 3. `q101`

**裁判定位到的句子** (只用来定位, 不是判定):

> | **Role** | Synonym Qualifier |

**答案原文**:

**TSPARM** in the **TS (Trial Summary)** domain identifies the descriptive name of the trial summary parameter. It is the companion variable to **TSPARMCD**, and its value must not exceed 40 characters. [Source: domains/TS/spec.md]

| Attribute | Value |
|---|---|
| **Label** | Trial Summary Parameter |
| **Type** | Char |
| **Role** | Synonym Qualifier |
| **Core** | Req |
| **Controlled Terms** | C67152 — Trial Summary Parameter Test Name |

[Source: domains/TS/spec.md]

Example trial summary parameter names include:

- `Planned Minimum Age of Subjects`
- `Planned Maximum Age of Subjects`

[Source: domains/TS/spec.md]

The **C67152** codelist is extensible. If a sponsor adds a parameter, its meaning should be documented in the TS dataset metadata. [Source: domains/TS/assumptions.md]

The retrieved context does not contain the complete **C67152** value list, so additional parameter names should be confirmed against the applicable CDISC Controlled Terminology release. [Source: domains/TS/assumptions.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 4. `q57`

**裁判定位到的句子** (只用来定位, 不是判定):

> It is based on the **Interventions** observation class.

**答案原文**:

The **PR (Procedures)** domain represents all collected procedures, including screening, diagnostic, therapeutic, and surgical procedures. It is based on the **Interventions** observation class. Measurements resulting from procedures are represented in the appropriate Findings domain(s), rather than in PR. [Source: domains/PR/assumptions.md]

**PRTRT variable definition:**

- **Label:** Reported Name of Procedure
- **Type:** Char
- **Role:** Topic
- **Core:** Req
- **Controlled Terms:** None specified
- **Definition:** The name of the procedure performed, either preprinted or collected on a CRF. [Source: domains/PR/spec.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 5. `s04`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

The controlled terminology codelist code for `AEACN` is **C66767** (“Action Taken with Study Treatment”). [Source: domains/AE/spec.md]

The CDISC Notes list these ICH E2B example values:

- `DRUG WITHDRAWN`
- `DOSE REDUCED`
- `DOSE INCREASED`
- `DOSE NOT CHANGED`
- `UNKNOWN`
- `NOT APPLICABLE`

[Source: domains/AE/spec.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 6. `q21`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

**LBTESTCD** is the required topic variable identifying the short name of the laboratory measurement, test, or examination described by **LBTEST**. It may also serve as a column name when transforming an LB dataset from vertical to horizontal structure. [Source: domains/LB/spec.md]

| Attribute | Value |
|---|---|
| **Label** | Lab Test or Examination Short Name |
| **Type** | Char |
| **Role** | Topic |
| **Core** | Req |
| **Controlled Terms** | **C65047** — Laboratory Test Code |

[Source: domains/LB/spec.md] [Source: VARIABLE_INDEX.md]

### Naming constraints

An **LBTESTCD** value:

- Must not exceed **8 characters**.
- Must not begin with a number; for example, `"1TEST"` is invalid.
- May contain only letters, numbers, or underscores.
- Examples include `"ALT"` and `"LDH"`.

[Source: domains/LB/spec.md]

The codelist **C65047** is specifically referenced by **LB.LBTESTCD**. [Source: VARIABLE_INDEX.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 7. `q56`

**裁判定位到的句子** (只用来定位, 不是判定):

> **SU observation class:** **Interventions**.

**答案原文**:

- **SU observation class:** **Interventions**. [Source: VARIABLE_INDEX.md]

- **SUTRT** is the topic variable for the SU dataset and captures the verbatim or prespecified substance text collected; it is required and must have a value. Examples include `"CIGARETTES"` and `"COFFEE"`. [Source: domains/SU/assumptions.md] [Source: domains/SU/spec.md]

  | Attribute | Value |
  |---|---|
  | Label | Reported Name of Substance |
  | Type | Char |
  | Role | Topic |
  | Core | Req |
  | Controlled Terms | None specified |

  [Source: domains/SU/spec.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 8. `s02`

**裁判定位到的句子** (只用来定位, 不是判定):

> Role: Topic

**答案原文**:

**QNAM — Qualifier Variable Name**

- **Label:** Qualifier Variable Name  
- **Type:** Char  
- **Role:** Topic  
- **Core:** Req  
- **Controlled Terms:** May be subject to controlled terminology; Appendix C1 provides terminology for some common QNAM/QLABEL values, and additional QNAM values may be sponsor-defined as needed. [Source: domains/SUPPQUAL/spec.md] [Source: chapters/ch08_relationships.md]

QNAM is the short name of a supplemental qualifier variable. When SUPP-- data are transposed or viewed with their parent domain, QNAM is used as the column name. [Source: domains/SUPPQUAL/spec.md]

**Character constraints:**

- Maximum length: **8 characters**
- Must **not begin with a number**
- May contain only:
  - letters
  - numbers
  - underscores (`_`)
- Therefore, `1TEST` is invalid. [Source: domains/SUPPQUAL/spec.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---
