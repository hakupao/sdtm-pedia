# SDTMIG v3.4 — Chapter 8: Representing Relationships and Data

Source: SDTMIG v3.4, Section 8 (Pages 427-446)

## Overview

This section describes how to represent relationships between separate domains, datasets, and/or records, and provides information to help sponsors determine where data belong in the SDTM.

---

## 8.1 Relating Records Within a Domain Using --GRPID

--GRPID is used to link related records within the same domain. All records sharing the same --GRPID value are considered a related group.

**Example:** Combination therapy in CM domain — a subject taking a combination of drugs as a single therapy:

| Row | CMTRT | CMGRPID | CMSTDTC | CMENDTC |
|-----|-------|---------|---------|---------|
| 1 | ASPIRIN | COMBO1 | 2005-01-01 | 2005-06-30 |
| 2 | DIPYRIDAMOLE | COMBO1 | 2005-01-01 | 2005-06-30 |
| ... | (up to 12 rows showing combination therapy grouping) | | | |

---

## 8.2 Relating Peer Records Across Domains Using RELREC

RELREC is used to describe relationships between records in different domains (peer records). Relationships are defined in pairs of rows in the RELREC dataset.

### RELREC Specification

| Variable | Label | Type | Core | Notes |
|----------|-------|------|------|-------|
| STUDYID | Study Identifier | Char | Req | |
| RDOMAIN | Related Domain Abbreviation | Char | Req | |
| USUBJID | Unique Subject Identifier | Char | Exp | Null for dataset-level relationships |
| IDVAR | Identifying Variable | Char | Req | e.g., --GRPID, --SEQ, --LNKID |
| IDVARVAL | Identifying Variable Value | Char | Req | |
| RELTYPE | Relationship Type | Char | Exp | "ONE" or "MANY" |
| RELID | Relationship Identifier | Char | Req | Groups paired RELREC records |

### Relationship Type Combinations

| RELTYPE Pair | Meaning |
|-------------|---------|
| ONE-to-ONE | One record in domain A relates to exactly one record in domain B |
| ONE-to-MANY | One record relates to multiple records |
| MANY-to-ONE | Multiple records relate to one record |
| MANY-to-MANY | Multiple records relate to multiple records |

### Examples

**Example 1:** Linking an AE record to a CM record (concomitant medication taken for the AE)
```
RELREC Row 1: RDOMAIN=AE, IDVAR=AESEQ, IDVARVAL=3, RELTYPE=ONE, RELID=1
RELREC Row 2: RDOMAIN=CM, IDVAR=CMSEQ, IDVARVAL=7, RELTYPE=ONE, RELID=1
```

**Example 2:** Linking a group of AE records to a single DS record
```
RELREC Row 1: RDOMAIN=AE, IDVAR=AEGRPID, IDVARVAL=GRP01, RELTYPE=MANY, RELID=2
RELREC Row 2: RDOMAIN=DS, IDVAR=DSSEQ, IDVARVAL=1, RELTYPE=ONE, RELID=2
```

---

## 8.3 Relating Datasets Using RELREC

For dataset-level relationships, USUBJID is null and IDVAR/IDVARVAL identify the linking variables.

**Example:** Linking TU and TR datasets (tumor identification and tumor results)
```
RELREC Row 1: RDOMAIN=TU, USUBJID=(null), IDVAR=TULNKID, RELTYPE=ONE, RELID=DS1
RELREC Row 2: RDOMAIN=TR, USUBJID=(null), IDVAR=TRLNKID, RELTYPE=MANY, RELID=DS1
```

---

## 8.4 Supplemental Qualifiers (SUPP--)

### Specification

| Variable | Label | Type | Core |
|----------|-------|------|------|
| STUDYID | Study Identifier | Char | Req |
| RDOMAIN | Related Domain Abbreviation | Char | Req |
| USUBJID | Unique Subject Identifier | Char | Req |
| POOLID | Pool Identifier | Char | Perm |
| IDVAR | Identifying Variable | Char | Req |
| IDVARVAL | Identifying Variable Value | Char | Req |
| QNAM | Qualifier Variable Name | Char | Req |
| QLABEL | Qualifier Variable Label | Char | Req |
| QVAL | Data Value | Char | Req |
| QORIG | Origin | Char | Req |
| QEVAL | Evaluator | Char | Perm |

### Key Rules

- Separate SUPP-- datasets are required for each parent domain (e.g., suppae.xpt, suppcm.xpt)
- QNAM must be a valid SAS variable name (1-8 characters, starting with a letter)
- QNAM should follow CDISC naming conventions (see Appendix D for naming fragments)
- QVAL is always character type (even for numeric values)
- IDVAR is typically --SEQ but can be --LNKID or other identifier

### When NOT to Use SUPP--

- Do not use SUPP-- for standard SDTM variables that belong in the parent domain
- Do not use SUPP-- for data that belongs in a different domain
- Do not use SUPP-- for analysis-derived variables (those belong in ADaM)

### Examples

**Example 1:** SUPPAE — additional AE qualifiers
```
RDOMAIN=AE, IDVAR=AESEQ, IDVARVAL=1, QNAM=AESOSP, QLABEL="Other Medically Important SAE", QVAL="Y"
```

**Example 2:** SUPPQS — supplemental questionnaire data
```
RDOMAIN=QS, IDVAR=QSSEQ, IDVARVAL=5, QNAM=QSREASND, QLABEL="Reason Not Done", QVAL="PATIENT REFUSED"
```

---

## 8.5 Relating Comments to a Parent Domain

Comments in the CO domain can be related to parent domain records in 3 ways:

1. **Direct relationship using RDOMAIN, IDVAR, IDVARVAL** — the CO record specifies which domain and record the comment relates to
2. **Using RELREC** — a RELREC record links the CO record to a parent domain record
3. **Standalone comments** — RDOMAIN is null; the comment is not related to any specific domain

---

## 8.6 Where Data Belong

### 8.6.1 Guidelines for Determining the General Observation Class

Use these questions to determine the appropriate GOC:

| Question | If Yes |
|----------|--------|
| Was it administered to or used by the subject? | → **Interventions** |
| Did it happen to the subject (planned or unplanned)? | → **Events** |
| Was it a measurement, test, or assessment? | → **Findings** |
| Is it about an event or intervention (not the subject directly)? | → **Findings About** |

### 8.6.2 Guidelines for Forming New Domains

When existing domains do not fit, follow the procedure in Section 2.6 (Creating a New Domain).

### 8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About

A decision table to help determine the appropriate observation class:

| Data Characteristic | Interventions | Events | Findings | Findings About |
|--------------------|---------------|--------|----------|----------------|
| Treatment/medication data | Yes | | | |
| Adverse event / medical history | | Yes | | |
| Lab test / measurement | | | Yes | |
| Assessment of an AE (e.g., severity) | | | | Yes |
| Symptom occurrence checklist | | Prespecified Events | | |
| Symptom severity rating | | | | Yes |
| Data about symptoms collected as QS items | | | QS | Or FA |

---

## 8.7 Related Subjects (RELSUB)

### Specification

| Variable | Label | Type | Core |
|----------|-------|------|------|
| STUDYID | Study Identifier | Char | Req |
| USUBJID | Unique Subject Identifier | Char | Req |
| RSUBJID | Related Subject or Pool Identifier | Char | Req |
| SREL | Subject Relationship to Related Subject/Pool | Char | Req |

### Assumptions

1. Each record in RELSUB describes 1 directional relationship from USUBJID to RSUBJID
2. SREL describes the relationship from the perspective of RSUBJID relative to USUBJID (e.g., SREL = "MOTHER" means RSUBJID is the mother of USUBJID)
3. Reciprocal relationships require 2 records
4. RSUBJID can reference subjects within or outside the current study
5. If RSUBJID references a subject in another study, a compound-level subject identifier should be used
6. Relationships to pools use POOLID in RSUBJID
7. Family relationships (genetic studies) are a primary use case
8. RELSUB can also be used to represent caregiver-patient relationships

### Example

Hemophilia study with family relationships:

**dm.xpt** (3 subjects):
| USUBJID | SEX | AGE |
|---------|-----|-----|
| HEM-001 | M | 8 |
| HEM-002 | F | 35 |
| HEM-003 | M | 37 |

**relsub.xpt** (6 relationship records):
| USUBJID | RSUBJID | SREL |
|---------|---------|------|
| HEM-001 | HEM-002 | MOTHER |
| HEM-001 | HEM-003 | FATHER |
| HEM-002 | HEM-001 | SON |
| HEM-002 | HEM-003 | HUSBAND |
| HEM-003 | HEM-001 | SON |
| HEM-003 | HEM-002 | WIFE |

---

## 8.8 Related Specimens (RELSPEC)

### Specification

| Variable | Label | Type | Core |
|----------|-------|------|------|
| STUDYID | Study Identifier | Char | Req |
| DOMAIN | Domain Abbreviation | Char | Req |
| USUBJID | Unique Subject Identifier | Char | Req |
| REFID | Specimen Identifier | Char | Req |
| SPEC | Specimen Material Type | Char | Exp |
| PARENT | Parent Specimen Identifier | Char | Exp |

### Assumptions

1. Each record describes a specimen and its relationship to a parent specimen
2. The root specimen (original collection) has PARENT = null
3. REFID must be unique within a subject across all domains that reference the specimen
4. The SPEC variable describes the type of material (e.g., "BLOOD", "SERUM", "PLASMA")

### Example

Specimen lineage diagram:
```
BLOOD (root specimen S001)
├── SERUM (derived specimen S002, PARENT=S001)
│   └── SERUM ALIQUOT (S004, PARENT=S002)
└── PLASMA (derived specimen S003, PARENT=S001)
    ├── PLASMA ALIQUOT (S005, PARENT=S003)
    └── PLASMA ALIQUOT (S006, PARENT=S003)
```

**relspec.xpt:**

| REFID | SPEC | PARENT |
|-------|------|--------|
| S001 | BLOOD | |
| S002 | SERUM | S001 |
| S003 | PLASMA | S001 |
| S004 | SERUM | S002 |
| S005 | PLASMA | S003 |
| S006 | PLASMA | S003 |
