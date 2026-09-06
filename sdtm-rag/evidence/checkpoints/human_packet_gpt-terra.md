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

### 1. `q69`

**裁判定位到的句子** (只用来定位, 不是判定):

> 以下 **Interventions** 域变量引用剂量单位受控术语表 **Unit (C71620)**

**答案原文**:

基于已提供的上下文，以下 **Interventions** 域变量引用剂量单位受控术语表 **Unit (C71620)**：

| 域 | 变量 | Label | Type | Role | Core | Controlled Terms | 用途 |
|---|---|---|---|---|---|---|---|
| AG | AGDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 | 用于 AGDOSE 和 AGDOSTXT 的单位。 [Source: domains/AG/spec.md] |
| CM | CMDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 | 用于 CMDOSE、CMDOSTOT 或 CMDOSTXT 的单位。 [Source: domains/CM/spec.md] |
| EC | ECDOSU | Dose Units | Char | Variable Qualifier | Exp | C71620 | 用于 ECDOSE、ECDOSTOT 或 ECDOSTXT 的单位。 [Source: domains/EC/spec.md] |
| EX | EXDOSU | Dose Units | Char | Variable Qualifier | Exp | C71620 | 用于 EXDOSE、EXDOSTOT 或 EXDOSTXT、表示 protocol-specified values 的单位。 [Source: domains/EX/spec.md] |
| ML | MLDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 | 用于 MLDOSE、MLDOSTOT 或 MLDOSTXT 的单位。 [Source: domains/ML/spec.md] |

在已给出的 CM 和 EX 受控术语交叉引用中，C71620 的名称为 **Unit**，分别由 CMDOSU 和 EXDOSU 使用。 [Source: domains/CM/spec.md] [Source: domains/EX/spec.md]

提供的上下文未包含 **Findings** 域中引用 C71620 的变量清单，因此无法据此可靠地列出全部 Findings-domain 变量；需查阅 `VARIABLE_INDEX.md` 的 C71620 交叉引用或各 Findings 域的 `spec.md` 以完成全量清单。

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 2. `q56`

**裁判定位到的句子** (只用来定位, 不是判定):

> SU is an **Interventions** domain.

**答案原文**:

SU is an **Interventions** domain. [Source: VARIABLE_INDEX.md]

`SUTRT` is the required Topic variable that captures the reported substance name—either verbatim text or prespecified text collected for the substance-use record. It must be populated for each SU record. Examples include `CIGARETTES` and `COFFEE`. [Source: domains/SU/assumptions.md] [Source: domains/SU/spec.md]

| Attribute | Value |
|---|---|
| Variable | `SUTRT` |
| Label | Reported Name of Substance |
| Type | Char |
| Role | Topic |
| Core | Req |
| Controlled Terms | None specified | 

[Source: VARIABLE_INDEX.md] [Source: domains/SU/spec.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 3. `q73`

**裁判定位到的句子** (只用来定位, 不是判定):

> | Special Purpose | `CO` | Record Qualifier / Perm |

**答案原文**:

`RDOMAIN` occurs in the following domains:

| Category | Domains carrying `RDOMAIN` | `RDOMAIN` Role/Core |
|---|---|---|
| Special Purpose | `CO` | Record Qualifier / Perm |
| Relationship | `RELREC`, `SUPPQUAL` | Identifier / Req |

`RDOMAIN` identifies the **related/parent record’s domain abbreviation** and is controlled by `C66734` (SDTM Domain Abbreviation).

- In `RELREC`, it is the abbreviation for the domain of the parent record(s). [Source: domains/RELREC/spec.md]
- In `SUPPQUAL`, it is the two-character abbreviation for the domain of the parent record(s). [Source: domains/SUPPQUAL/spec.md]
- In `CO`, it is the two-character abbreviation for the domain of the parent record(s); it is null for comments collected on a general-comments or additional-information CRF page. [Source: domains/CO/spec.md]

Variable attributes:

| Domain | Label | Type | Role | Core | Controlled Terms |
|---|---|---|---|---|---|
| `CO` | Related Domain Abbreviation | Char | Record Qualifier | Perm | `C66734` |
| `RELREC` | Related Domain Abbreviation | Char | Identifier | Req | `C66734` |
| `SUPPQUAL` | Related Domain Abbreviation | Char | Identifier | Req | `C66734` |

[Source: domains/CO/spec.md] [Source: domains/RELREC/spec.md] [Source: domains/SUPPQUAL/spec.md]

`VARIABLE_INDEX.md` likewise identifies `CO`, `RELREC`, and `SUPPQUAL` as the three SDTM domains containing `RDOMAIN`. [Source: VARIABLE_INDEX.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 4. `q21`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

`LBTESTCD` is the short, standardized identifier for the laboratory test or examination represented by an LB record.

| Attribute | Value |
|---|---|
| Label | Lab Test or Examination Short Name |
| Type | Char |
| Role | Topic |
| Core | Req |
| Controlled Terms | Laboratory Test Code, `C65047` |

`LBTESTCD` identifies the measurement, test, or examination described in `LBTEST`; it may also be used as a column name when transforming data from vertical to horizontal structure. The associated full/verbatim test name is represented in `LBTEST`, which uses codelist `C67154`. [Source: domains/LB/spec.md] [Source: VARIABLE_INDEX.md]

**Naming constraints for `LBTESTCD`:**

- Maximum length: **8 characters**.
- Must **not begin with a number**; for example, `1TEST` is invalid.
- May contain only **letters, numbers, and underscores**.
- Examples include `ALT` and `LDH`. [Source: domains/LB/spec.md]

The controlled terminology cross-reference confirms that `C65047` is referenced by `LB.LBTESTCD`. [Source: VARIABLE_INDEX.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 5. `s04`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

In the AE domain, **AEACN** (Label: *Action Taken with Study Treatment*) uses controlled terminology codelist **C66767**. Its attributes are:

- **Type:** Char  
- **Role:** Record Qualifier  
- **Core:** Exp  
- **Controlled Terms:** C66767  

The CDISC Notes lists these ICH E2B example values:

- `DRUG WITHDRAWN`
- `DOSE REDUCED`
- `DOSE INCREASED`
- `DOSE NOT CHANGED`
- `UNKNOWN`
- `NOT APPLICABLE`

AEACN specifically describes actions concerning the relationship to study treatment; actions unrelated to study-treatment dose adjustments belong in AEACNOTH. [Source: domains/AE/spec.md] [Source: domains/AE/assumptions.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 6. `q40`

**裁判定位到的句子** (只用来定位, 不是判定):

> (裁判未定位到)

**答案原文**:

In SDTM, datasets may contain data that are **collected/received**, **assigned**, or **derived**. “Collected” is not limited to direct CRF entry; it also includes data received from sources such as a vendor, central laboratory, or device. “Derived” data are produced through a documented derivation algorithm. [Source: chapters/ch02_fundamentals.md] [Source: chapters/ch04_general_assumptions.md]

### Collected data

Collected data originate from a source without sponsor operational calculation of the submitted value—for example:

- values entered on the CRF;
- data received from a vendor or device;
- a value produced by a central laboratory according to that laboratory’s own procedures.

A central-lab-derived result is treated as **collected**, rather than sponsor-derived. [Source: chapters/ch04_general_assumptions.md] [Source: domains/LB/assumptions.md]

For QRS domains such as QS and FT, a subtotal or total score documented on the CRF, in the instrument documentation, or received from a central provider/vendor is considered captured/collected. A score written on the CRF by an investigator is likewise captured rather than derived. [Source: domains/QS/assumptions.md] [Source: domains/FT/assumptions.md]

### Derived data

Derived data are values calculated or otherwise generated by the sponsor from source data. They must be traceable to a derivation algorithm. For example, if a sponsor operationally calculates a QRS total score, the submitted record is derived and `--DRVFL` must be set to `"Y"`. Transformations or imputations of numeric standardized responses to create a total score are ADaM derivations. [Source: chapters/ch04_general_assumptions.md] [Source: domains/QS/assumptions.md] [Source: domains/FT/assumptions.md]

### Indicating origin in metadata

The origin of a variable is indicated using the **origin element** in Define-XML. Its purpose is to clearly communicate the source of the submitted value to reviewers. Origin can indicate, for example:

- collected on the CRF;
- collected from a vendor or device;
- derived;
- assigned.

CRF-originated values should trace to an annotated CRF, while derived values should trace to their derivation algorithm. The Define-XML specification is the authoritative source for permitted origin values. [Source: chapters/ch04_general_assumptions.md]

Origin is normally a **variable-level** metadata attribute. However, an origin of derived means *all* values of that variable are derived; similarly, CRF-collected means *all* values are CRF-collected. If a single variable contains both collected and derived records—for example, collected QS item responses and derived total-score records—Define-XML **value-level metadata** must describe the different origins. [Source: chapters/ch04_general_assumptions.md]

Thus, `--DRVFL` is a record-level flag used in applicable QRS records to identify sponsor-operationally derived results, whereas Define-XML origin metadata documents the provenance of variables or, when necessary, particular values. A vendor/central-provider QRS total score is entered in `--ORRES` with `--DRVFL` null, even though the provider itself may have calculated it. [Source: domains/QS/assumptions.md] [Source: domains/FT/assumptions.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 7. `q66`

**裁判定位到的句子** (只用来定位, 不是判定):

> It appears in these 36 SDTM domains: - **Interventions:** AG, ML, PR - **Events:** BE - **Findings:** BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, QS, RE, RP, RS, SC, SR, SS, TR, TU, UR, VS - **Special Purpose:** SV - **Trial Design:** TV

**答案原文**:

`VISITNUM` (Visit Number) is a Timing variable with Type `Num` and Core `Exp`. It appears in these 36 SDTM domains:

- **Interventions:** AG, ML, PR  
- **Events:** BE  
- **Findings:** BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, QS, RE, RP, RS, SC, SR, SS, TR, TU, UR, VS  
- **Special Purpose:** SV  
- **Trial Design:** TV  

[Source: VARIABLE_INDEX.md]

Additionally, `VISITNUM` may be added conditionally to:
- **SU**, when substance-use data are collected more than once in the CRF on a visit-based basis. [Source: domains/SU/assumptions.md]
- **EX**, when study treatment exposure occurs entirely within a clinical encounter; it should not be used merely to represent the visit at which a longer exposure interval began or ended. [Source: domains/EX/assumptions.md]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---

### 8. `q96`

**裁判定位到的句子** (只用来定位, 不是判定):

> | Role | Synonym Qualifier |

**答案原文**:

In the FA domain, **FATEST** identifies the verbatim name of the measurement, test, or examination used to obtain a finding.

| Attribute | Value |
|---|---|
| Variable | FATEST |
| Label | Findings About Test Name |
| Type | Char |
| Role | Synonym Qualifier |
| Core | Req |
| Controlled Terms | C101833 — Findings About Test Name |

FATEST is limited to 40 characters. It is the descriptive test name corresponding to the short topic code in FATESTCD; examples shown in the specification include `Severity/Intensity` and `Occurrence`. [Source: domains/FA/spec.md]

`C101833` is the controlled-terminology codelist referenced by `FA.FATEST`; `FATESTCD` correspondingly uses `C101832`. [Source: domains/FA/spec.md] [Source: VARIABLE_INDEX.md]

The retrieved context does **not** contain the value rows for codelist `C101833`. Therefore, although `Diameter` and `Cumulative Exposure` are the example test names mentioned in the question, their membership in `C101833`—and any individual NCI codes—must be confirmed from `terminology/core/findings_about.md`; individual value codes cannot be established from the available context. [Source: domains/FA/spec.md — Controlled Terminology]

**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)

---
