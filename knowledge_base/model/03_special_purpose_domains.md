# SDTM v2.0 — Chapter 3.2: Special-purpose Domains

Source: SDTM v2.0, Section 3.2 (Pages 40-49)

## Overview

In addition to the 3 general observation classes, a study will generally include a set of other special-purpose datasets. Special-purpose domains are specified completely (unlike general observation class domains on which individual domains can be based).

## Demographics (DM)

**Structure:** One record per subject

The Demographics domain includes a set of essential standard variables that describe each subject in a clinical study. It is the parent domain to which all other observations are linked.

### Variables (38 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "DM" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SUBJID | Subject Identifier for the Study | Char | Identifier | |
| 5 | RFSTDTC | Subject Reference Start Date/Time | Char | Record Qualifier | Usually first dose date |
| 6 | RFENDTC | Subject Reference End Date/Time | Char | Record Qualifier | Usually date of last dose |
| 7 | RFXSTDTC | Date/Time of First Study Treatment | Char | Record Qualifier | |
| 8 | RFXENDTC | Date/Time of Last Study Treatment | Char | Record Qualifier | |
| 9 | RFCSTDTC | Date/Time of First Study Contact | Char | Record Qualifier | |
| 10 | RFCENDTC | Date/Time of Last Study Contact | Char | Record Qualifier | |
| 11 | RFICDTC | Date/Time of Informed Consent | Char | Record Qualifier | |
| 12 | RFPENDTC | Date/Time of End of Participation | Char | Record Qualifier | |
| 13 | DTHDTC | Date/Time of Death | Char | Record Qualifier | |
| 14 | DTHFL | Subject Death Flag | Char | Record Qualifier | "Y" or null |
| 15 | SITEID | Study Site Identifier | Char | Record Qualifier | |
| 16 | INVID | Investigator Identifier | Char | Record Qualifier | |
| 17 | INVNAM | Investigator Name | Char | Record Qualifier | |
| 18 | BRTHDTC | Date/Time of Birth | Char | Record Qualifier | |
| 19 | AGE | Age | Num | Record Qualifier | Numeric age at RFSTDTC |
| 20 | AGETXT | Age Text | Char | Record Qualifier | Used when exact age is unknown; e.g., "18-25" |
| 21 | AGEU | Age Units | Char | Variable Qualifier (AGE/AGETXT) | "YEARS", "MONTHS", "DAYS" |
| 22 | SEX | Sex | Char | Record Qualifier | Subject to controlled terminology |
| 23 | RACE | Race | Char | Record Qualifier | |
| 24 | ETHNIC | Ethnicity | Char | Record Qualifier | |
| 25 | SPECIES | Species | Char | Record Qualifier | **Not for human clinical trials** |
| 26 | STRAIN | Strain/Substrain | Char | Record Qualifier | **Not for human clinical trials** |
| 27 | SBSTRAIN | Substrain | Char | Record Qualifier | **Not for human clinical trials** |
| 28 | ARMCD | Planned Arm Code | Char | Record Qualifier | Short version of ARM |
| 29 | ARM | Description of Planned Arm | Char | Record Qualifier | |
| 30 | ACTARMCD | Actual Arm Code | Char | Record Qualifier | |
| 31 | ACTARM | Description of Actual Arm | Char | Record Qualifier | |
| 32 | ARMNRS | Reason Arm and/or Actual Arm is Null | Char | Record Qualifier | When arm assignment is not possible |
| 33 | ACTARMUD | Description of Unplanned Actual Arm | Char | Record Qualifier | |
| 34 | SETCD | Set Code | Char | Record Qualifier | Use with extreme caution |
| 35 | RPATHCD | Reproductive Pathway Code | Char | Record Qualifier | **Not for human clinical trials** |
| 36 | COUNTRY | Country | Char | Record Qualifier | ISO 3166-1 Alpha-3 |
| 37 | DMDTC | Date/Time of Collection | Char | Timing | |
| 38 | DMDY | Study Day of Collection | Num | Timing | |

### Key Reference Date Variables

| Variable | Description | Typical Use |
|----------|-------------|-------------|
| RFSTDTC | Subject Reference Start Date/Time | Usually first dose; basis for study day calculation |
| RFENDTC | Subject Reference End Date/Time | Usually last dose date |
| RFXSTDTC | Date/Time of First Study Treatment | First exposure to study treatment |
| RFXENDTC | Date/Time of Last Study Treatment | Last exposure to study treatment |
| RFCSTDTC | Date/Time of First Study Contact | First protocol contact (screening) |
| RFCENDTC | Date/Time of Last Study Contact | Last protocol contact |
| RFICDTC | Date/Time of Informed Consent | Consent date |
| RFPENDTC | Date/Time of End of Participation | Completion/withdrawal date |

## Comments (CO)

**Structure:** One record per comment per subject (or per study)

The Comments special-purpose domain is used to capture free-text comments that are not a part of normal domain data. Comments typically do not have a natural parent domain.

### Variables (15 variables)

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | RDOMAIN | Related Domain Abbreviation | Char | Record Qualifier |
| 4 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 5 | COSEQ | Sequence Number | Num | Identifier |
| 6 | COVAL | Comment | Char | Topic |
| 7 | IDVAR | Identifying Variable | Char | Record Qualifier |
| 8 | IDVARVAL | Identifying Variable Value | Char | Record Qualifier |
| 9 | COREF | Comment Reference | Char | Record Qualifier |
| 10 | CODTC | Date/Time of Comment | Char | Timing |
| 11 | CODY | Study Day of Comment | Num | Timing |
| + Additional timing variables as needed |

**Note:** The CO domain in the SDTM does not include DOMAIN as a variable (unlike the SDTMIG implementation). RDOMAIN is used to relate comments to specific domains.

## Subject Elements (SE)

**Structure:** One record per actual Element per subject

Describes the actual Elements (blocks of time) experienced by each subject during the study.

### Variables (13 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SE" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SESEQ | Sequence Number | Num | Identifier | |
| 5 | ETCD | Element Code | Char | Topic | Code for the Element (from TE) |
| 6 | ELEMENT | Description of Element | Char | Synonym Qualifier | |
| 7 | SESTDTC | Start Date/Time of Element | Char | Timing | |
| 8 | SEENDTC | End Date/Time of Element | Char | Timing | |
| 9 | TAESSION | Planned Element | Char | Record Qualifier | |
| 10 | EPOCH | Epoch | Char | Timing | |
| 11 | SESTDY | Study Day of Start of Element | Num | Timing | |
| 12 | SEENDY | Study Day of End of Element | Num | Timing | |
| 13 | SEDUR | Duration of Element | Char | Timing | |

## Subject Disease Journey (SJ)

**Structure:** One record per Disease Journey per subject

Represents the disease journey of a subject through a study.

### Variables (10 variables)

| # | Variable | Label | Notes |
|---|----------|-------|-------|
| 1 | STUDYID | Study Identifier | |
| 2 | DOMAIN | Domain Abbreviation | "SJ" |
| 3 | USUBJID | Unique Subject Identifier | |
| 4 | SJSEQ | Sequence Number | |
| 5 | SJTERM | Disease Journey Term | Topic variable |
| 6 | SJDECOD | Dictionary-Derived Term | |
| 7 | SJCAT | Category | |
| 8 | SJSTDTC | Start Date/Time | |
| 9 | SJENDTC | End Date/Time | |
| 10 | SJDY | Study Day | |

## Subject Visits (SV)

**Structure:** One record per actual or planned visit per subject

Describes the actual study visits experienced by each subject.

### Variables (16 variables)

| # | Variable | Label | Notes |
|---|----------|-------|-------|
| 1 | STUDYID | Study Identifier | |
| 2 | DOMAIN | Domain Abbreviation | "SV" |
| 3 | USUBJID | Unique Subject Identifier | |
| 4 | VISITNUM | Visit Number | |
| 5 | VISIT | Visit Name | |
| 6 | VISITDY | Planned Study Day of Visit | |
| 7 | SVSTDTC | Start Date/Time of Visit | |
| 8 | SVENDTC | End Date/Time of Visit | |
| 9 | SVSTDY | Study Day of Start of Visit | |
| 10 | SVENDY | Study Day of End of Visit | |
| 11 | SVUPDES | Description of Unplanned Visit | |
| 12 | SVPRESP | Pre-Specified | |
| 13 | SVOCCUR | Occurrence | |
| 14 | SVREASOC | Reason for Occurrence Value | |
| 15 | SVCNTMOD | Contact Mode | |
| 16 | SVEPCHGI | Epi/Pandemic Related Change | |

## Subject Disease Milestones (SM)

**Structure:** One record per Disease Milestone per subject

Records the disease milestones experienced by each subject (e.g., diagnosis, progression, relapse, remission).

### Variables (10 variables)

| # | Variable | Label | Notes |
|---|----------|-------|-------|
| 1 | STUDYID | Study Identifier | |
| 2 | DOMAIN | Domain Abbreviation | "SM" |
| 3 | USUBJID | Unique Subject Identifier | |
| 4 | MIDS | Disease Milestone Instance Name | Topic: unique name linking to TM |
| 5 | MIDSTYPE | Disease Milestone Type | From Trial Disease Milestones (TM) |
| 6 | SMDTC | Date/Time of Milestone | |
| 7 | SMDY | Study Day of Milestone | |
| 8 | SMSTDTC | Start Date/Time | |
| 9 | SMENDTC | End Date/Time | |
| 10 | SMEVAL | Evaluator | |
