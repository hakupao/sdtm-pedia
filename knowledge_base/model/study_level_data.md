# SDTM v2.0 — Chapter 5: Study-level Data

Source: SDTM v2.0, Sections 5.1-5.2 (Pages 51-63)

## Overview

The SDTM includes a set of tables for representing data at the study level. These datasets are specified in this section. Study-level data falls into 2 categories:
1. **Trial Design Model (TDM)** — datasets describing the planned structure of the trial
2. **Study References** — datasets for study-specific terminology

---

## 5.1 Trial Design Model

The Trial Design Model (TDM) provides a standardized way to describe the planned design of a clinical trial, including treatment arms, elements, visits, and assessments.

### Trial Elements (TE)

**Structure:** One record per planned Element

Describes the basic building blocks of a trial design — discrete periods of time during which a specific type of treatment or activity is planned.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | ETCD | Element Code | Char | Topic |
| 4 | ELEMENT | Description of Element | Char | Synonym Qualifier |
| 5 | TESTRL | Rule for Start of Element | Char | Rule |
| 6 | TEENRL | Rule for End of Element | Char | Rule |
| 7 | TEDUR | Planned Duration of Element | Char | Timing |

### Trial Arms (TA)

**Structure:** One record per planned Element per Arm

Describes the sequence of Elements that comprise each Arm of the trial.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | ARMCD | Planned Arm Code | Char | Topic |
| 4 | ARM | Description of Planned Arm | Char | Synonym Qualifier |
| 5 | TAESSION | Planned Element | Num | Timing |
| 6 | ETCD | Element Code | Char | Record Qualifier |
| 7 | ELEMENT | Description of Element | Char | Synonym Qualifier |
| 8 | TABESSION | Branch | Char | Rule |
| 9 | TATESSION | Transition Rule | Char | Rule |
| 10 | EPOCH | Epoch | Char | Timing |

### Trial Sets (TX)

**Structure:** One record per Trial Set parameter per Trial Set

Describes sets of subjects that share common characteristics (e.g., treatment groups, pooled analysis groups).

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | SETCD | Set Code | Char | Identifier |
| 4 | SET | Set Description | Char | Record Qualifier |
| 5 | TXSEQ | Sequence Number | Num | Identifier |
| 6 | TXPARMCD | Trial Set Parameter Short Name | Char | Topic |
| 7 | TXPARM | Trial Set Parameter Name | Char | Synonym Qualifier |
| 8 | TXVAL | Parameter Value | Char | Result Qualifier |

### Trial Reproductive Stages (TT)

**Structure:** One record per Reproductive Stage

For nonclinical reproductive/developmental toxicology studies.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | TTSEQ | Sequence Number | Num | Identifier |
| 4 | TTSTGCD | Reproductive Stage Code | Char | Topic |
| 5 | TTSTAGE | Reproductive Stage | Char | Synonym Qualifier |
| 6 | TTSTRL | Rule for Start of Stage | Char | Rule |
| 7 | TTENRL | Rule for End of Stage | Char | Rule |

### Trial Reproductive Paths (TP)

**Structure:** One record per Reproductive Path per Stage

| Variables: 10 | Including STUDYID, DOMAIN, TPSEQ, TPSTGCD, TPSTAGE, TPARMCD, TPARM, TPESSION, TPETCD, TPELEMENT |

### Trial Visits (TV)

**Structure:** One record per planned Visit per Arm

Describes the visits planned in the protocol.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | VISITNUM | Visit Number | Num | Topic |
| 4 | VISIT | Visit Name | Char | Synonym Qualifier |
| 5 | VISITDY | Planned Study Day of Visit | Num | Timing |
| 6 | ARMCD | Planned Arm Code | Char | Record Qualifier |
| 7 | ARM | Description of Planned Arm | Char | Synonym Qualifier |
| 8 | TVSTRL | Visit Start Rule | Char | Rule |
| 9 | TVENRL | Visit End Rule | Char | Rule |

### Trial Disease Assessments (TD)

**Structure:** One record per planned constant assessment period

Describes the assessments of disease that are planned in the protocol.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | TDSEQ | Sequence Number | Num | Identifier |
| 4 | TDORDER | Order of Assessment | Num | Timing |
| 5 | TDANCVAR | Anchor Variable | Char | Record Qualifier |
| 6 | TDSTOFF | Start Offset from Anchor | Char | Timing |
| 7 | TDTGTDTC | Target Date | Char | Timing |
| 8 | TDMININT | Minimum Assessment Interval | Char | Timing |
| 9 | TDMAXINT | Maximum Assessment Interval | Char | Timing |

### Trial Disease Milestones (TM)

**Structure:** One record per Disease Milestone type

Describes the types of disease milestones that may occur in a study.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | MIDSTYPE | Disease Milestone Type | Char | Topic |
| 4 | TMDEF | Definition of Disease Milestone | Char | Variable Qualifier |
| 5 | TMRPT | Repeating | Char | Record Qualifier |

### Trial Inclusion/Exclusion Criteria (TI)

**Structure:** One record per I/E criterion

Describes the inclusion and exclusion criteria for the trial.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | IETESTCD | Incl/Excl Criterion Short Name | Char | Topic |
| 4 | IETEST | Incl/Excl Criterion | Char | Synonym Qualifier |
| 5 | IECAT | Incl/Excl Category | Char | Grouping Qualifier |
| 6 | IESCAT | Incl/Excl Subcategory | Char | Grouping Qualifier |
| 7 | TIRL | Criterion Evaluation Rule | Char | Rule |
| 8 | TIVERS | Protocol Criteria Versions | Char | Record Qualifier |

### Trial Summary (TS)

**Structure:** One record per trial summary parameter value

Contains summary information about the trial (e.g., trial phase, objectives, design).

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | TSSEQ | Sequence Number | Num | Identifier |
| 4 | TSGRPID | Group ID | Char | Identifier |
| 5 | TSPARMCD | Trial Summary Parameter Short Name | Char | Topic |
| 6 | TSPARM | Trial Summary Parameter Name | Char | Synonym Qualifier |
| 7 | TSVAL | Parameter Value | Char | Result Qualifier |
| 8 | TSVALNF | Parameter Null Flavor | Char | Record Qualifier |
| 9 | TSVALCD | Parameter Value Code | Char | Record Qualifier |
| 10 | TSVCDREF | Name of Reference Terminology | Char | Record Qualifier |
| 11 | TSVCDVER | Version of Reference Terminology | Char | Record Qualifier |

### Challenge Agent Characterization (AC)

**Structure:** One record per Challenge Agent attribute per subject (nonclinical)

| Variables: 12 | Including STUDYID, DOMAIN, USUBJID, ACSEQ, ACSPID, ACGRPID, ACTRT, ACPARMCD, ACPARM, ACVAL, ACVALU, ACDTC |

---

## 5.2 Study References

Study Reference datasets provide structures for representing study-specific terminology used in subject data.

### Device Identifiers (DI)

**Structure:** One record per device attribute per device

Used to identify the devices used in a study.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | SPDEVID | Sponsor Device Identifier | Char | Topic |
| 4 | DIPARMCD | Device Identifier Parameter Short Name | Char | Topic |
| 5 | DIPARM | Device Identifier Parameter Name | Char | Synonym Qualifier |
| 6 | DIVAL | Parameter Value | Char | Result Qualifier |
| 7 | DIVALU | Parameter Value Units | Char | Variable Qualifier |

**Concept Map:** DI acts as a lookup table to describe characteristics of devices referenced by SPDEVID in subject-level domains (e.g., AE, PR).

### Non-host Organism Identifiers (OI)

**Structure:** One record per taxon per non-host organism

Used to represent taxonomic information for non-host organisms such as bacteria and viruses.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | NHOID | Non-host Organism Identifier | Char | Topic |
| 4 | OISEQ | Sequence Number | Num | Identifier |
| 5 | OITESTCD | Organism ID Test Short Name | Char | Topic |
| 6 | OITEST | Organism ID Test Name | Char | Synonym Qualifier |
| 7 | OIORRES | Result or Finding in Original Units | Char | Result Qualifier |

**Concept Map:** OI acts as a lookup table to describe characteristics of organisms referenced by NHOID in subject-level domains (e.g., MB, MS).
