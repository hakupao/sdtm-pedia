# SDTM v2.0 — Chapter 3.2: Special-purpose Domains

Source: SDTM v2.0, Section 3.2 (Pages 40-49)

## Overview

### 3.2 Special-purpose Domains

In addition to the 3 general observation classes, a submission will generally include a set of other special-purpose datasets of specific standardized structures to represent additional important information. A Demographics special-purpose domain is included with human and animal studies (see Section 3.2.1, Demographics). Other special-purpose domains may be included.

## 3.2.1 Demographics

Each study must include 1 standardized set of observations in a specific structure; this is the Demographics domain described here. Demographics is the parent domain for all other observations for subjects and should be identified with the domain code of "DM". The DM domain describes the essential characteristics of the study subjects, and is used by reviewers for selecting subsets of subjects for analysis. The DM domain, as with other datasets, includes identifiers, a topic variable, timing variables, and qualifiers. See the respective implementation guides for further guidance regarding use of additional identifier and timing variables.

> KB note (not in SDTM v2.0): **Structure:** One record per subject

### Variables (38 variables)

**Subject Demographics Domain Variables**

> KB note (not in SDTM v2.0): The Notes column is KB-written: most cells quote or condense the PDF Format, Notes and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0.

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "DM" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SUBJID | Subject Identifier for the Study | Char | Topic | Subject identifier, which must be unique within the study |
| 5 | RFSTDTC | Subject Reference Start Date/Time | Char | Record Qualifier | Usually first dose date |
| 6 | RFENDTC | Subject Reference End Date/Time | Char | Record Qualifier | Usually equivalent to the date/time when a subject was determined to have ended the trial. |
| 7 | RFXSTDTC | Date/Time of First Study Treatment | Char | Record Qualifier | |
| 8 | RFXENDTC | Date/Time of Last Study Treatment | Char | Record Qualifier | |
| 9 | RFCSTDTC | Date/Time of First Challenge Agent Admin | Char | Record Qualifier | |
| 10 | RFCENDTC | Date/Time of Last Challenge Agent Admin | Char | Record Qualifier | |
| 11 | RFICDTC | Date/Time of Informed Consent | Char | Record Qualifier | Not in nonclinical trials |
| 12 | RFPENDTC | Date/Time of End of Participation | Char | Record Qualifier | Not in nonclinical trials |
| 13 | DTHDTC | Date/Time of Death | Char | Record Qualifier | Not in nonclinical trials |
| 14 | DTHFL | Subject Death Flag | Char | Record Qualifier | "Y" or null. Not in nonclinical trials |
| 15 | SITEID | Study Site Identifier | Char | Record Qualifier | |
| 16 | INVID | Investigator Identifier | Char | Record Qualifier | Not in nonclinical trials |
| 17 | INVNAM | Investigator Name | Char | Synonym Qualifier (INVID) | Not in nonclinical trials |
| 18 | BRTHDTC | Date/Time of Birth | Char | Record Qualifier | |
| 19 | AGE | Age | Num | Record Qualifier | May be derived as (RFSTDTC-BRTHDTC), but BRTHDTC may not be available in all cases (due to subject privacy concerns). |
| 20 | AGETXT | Age Text | Char | Record Qualifier | Used when exact age is unknown; e.g., "18-25" |
| 21 | AGEU | Age Units | Char | Variable Qualifier (AGE/AGETXT) | "YEARS", "MONTHS", "DAYS" |
| 22 | SEX | Sex | Char | Record Qualifier | Subject to controlled terminology |
| 23 | RACE | Race | Char | Record Qualifier | Not in nonclinical trials |
| 24 | ETHNIC | Ethnicity | Char | Record Qualifier | Not in nonclinical trials |
| 25 | SPECIES | Species | Char | Record Qualifier | **Not in human clinical trials** |
| 26 | STRAIN | Strain/Substrain | Char | Record Qualifier | **Not in human clinical trials** |
| 27 | SBSTRAIN | Strain/Substrain Details | Char | Variable Qualifier (STRAIN) | **Not in human clinical trials** |
| 28 | ARMCD | Planned Arm Code | Char | Record Qualifier | Short version of ARM |
| 29 | ARM | Description of Planned Arm | Char | Synonym Qualifier (ARMCD) | |
| 30 | ACTARMCD | Actual Arm Code | Char | Record Qualifier | Not in nonclinical trials |
| 31 | ACTARM | Description of Actual Arm | Char | Synonym Qualifier (ACTARMCD) | Not in nonclinical trials |
| 32 | ARMNRS | Reason Arm and/or Actual Arm is Null | Char | Record Qualifier | The reason why the actual arm variables are null or why both the planned and actual arm variables are null. |
| 33 | ACTARMUD | Description of Unplanned Actual Arm | Char | Record Qualifier | |
| 34 | SETCD | Set Code | Char | Record Qualifier | Use with extreme caution |
| 35 | RPATHCD | Planned Repro Path Code | Char | Record Qualifier | **Not in human clinical trials** |
| 36 | COUNTRY | Country | Char | Record Qualifier | ISO 3166-1 Alpha-3. Not in nonclinical trials |
| 37 | DMDTC | Date/Time of Collection | Char | Timing | |
| 38 | DMDY | Study Day of Collection | Num | Timing | |

### Key Reference Date Variables

> KB note (not in SDTM v2.0): This table is a KB summary of the reference date variables in the table above: the Description column repeats the PDF Variable Label, and the Typical Use column is KB-written (RFENDTC and RFPENDTC quote the PDF Notes column).

| Variable | Description | Typical Use |
|----------|-------------|-------------|
| RFSTDTC | Subject Reference Start Date/Time | Usually first dose; basis for study day calculation |
| RFENDTC | Subject Reference End Date/Time | Usually equivalent to the date/time when a subject was determined to have ended the trial. |
| RFXSTDTC | Date/Time of First Study Treatment | First exposure to study treatment |
| RFXENDTC | Date/Time of Last Study Treatment | Last exposure to study treatment |
| RFCSTDTC | Date/Time of First Challenge Agent Admin | First exposure to challenge agent |
| RFCENDTC | Date/Time of Last Challenge Agent Admin | Last exposure to challenge agent |
| RFICDTC | Date/Time of Informed Consent | Consent date |
| RFPENDTC | Date/Time of End of Participation | Should correspond to the last known date of contact. |

## 3.2.2 Comments

Comments are collected during the conduct of many studies. These are normally supplied by a principal investigator, but might also be collected from other sources such as central reviewers. When collected, comments should be submitted in a single Comments domain, defined here.

See the implementation guides for further guidance regarding use of additional identifier and timing variables.

> KB note (not in SDTM v2.0): **Structure:** One record per comment per subject (or per study). The Comments special-purpose domain is used to capture free-text comments that are not a part of normal domain data.

### Variables (15 variables)

**Comments Domain Variables**

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | RDOMAIN | Related Domain Abbreviation | Char | Record Qualifier |
| 4 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 5 | POOLID | Pool Identifier | Char | Identifier |
| 6 | SPDEVID | Sponsor Device Identifier | Char | Identifier |
| 7 | COSEQ | Sequence Number | Num | Identifier |
| 8 | IDVAR | Identifying Variable | Char | Record Qualifier |
| 9 | IDVARVAL | Identifying Variable Value | Char | Record Qualifier |
| 10 | COREF | Comment Reference | Char | Record Qualifier |
| 11 | COVAL | Comment | Char | Topic |
| 12 | COEVAL | Evaluator | Char | Record Qualifier |
| 13 | COEVALID | Evaluator Identifier | Char | Variable Qualifier (COEVAL) |
| 14 | CODTC | Date/Time of Comment | Char | Timing |
| 15 | CODY | Study Day of Comment | Num | Timing |

## 3.2.3 Subject Summary Domains

Several special-purpose domains are designed to provide summaries of a subject's progress over time. Each dataset is based on a study-level dataset in Section 5.1, The Trial Design Model.

### 3.2.3.1 Subject Elements

Subject Elements describes the actual order of elements that were traversed by the subject, together with the start date or start date and time and end date/time for each. Planned elements are described in the Trial Design Model (see Section 5.1.1, Trial Arms and Trial Elements). Because actual data does not always follow the plan, the SDTM allows for descriptions of an unplanned element for subjects (SEUPDES).

See the implementation guides for further guidance regarding use of additional identifier and timing variables.

> KB note (not in SDTM v2.0): Elements are blocks of time.

### Variables (13 variables)

**Subject Elements—One Record per Actual Element per Subject**

> KB note (not in SDTM v2.0): The Notes column is KB-written: the DOMAIN and SEUPDES cells quote or condense the PDF Notes column, the TAETORD and EPOCH cells give the PDF Variable C-code, and the ETCD cell adds KB wording not given in SDTM v2.0.

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SE" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SESEQ | Sequence Number | Num | Identifier | |
| 5 | ETCD | Element Code | Char | Topic | Code for the Element (from TE) |
| 6 | ELEMENT | Description of Element | Char | Synonym Qualifier (ETCD) | |
| 7 | TAETORD | Planned Order of Element within Arm | Num | Timing | C83438 |
| 8 | EPOCH | Epoch | Char | Timing | C71738 |
| 9 | SESTDTC | Start Date/Time of Element | Char | Timing | |
| 10 | SEENDTC | End Date/Time of Element | Char | Timing | |
| 11 | SESTDY | Study Day of Start of Element | Num | Timing | |
| 12 | SEENDY | Study Day of End of Element | Num | Timing | |
| 13 | SEUPDES | Description of Unplanned Element | Char | Synonym Qualifier (ETCD) | Used only if ETCD has a value of "UNPLAN" |

### 3.2.3.2 Subject Repro Stages

Subject Repro Stages (not for use with human clinical trials) describes the actual order of repro stages experienced by the subject, together with the start date or start date and time and end date/time for each. Planned repro stages are described in the Trial Design Model (see Section 5.1.3.1, Trial Repro Stages). Because actual data does not always follow the plan, the SDTM allows for descriptions of an unplanned repro stage for subjects (SJUPDES).

### Variables (10 variables)

**Subject Repro Stages—One Record per Actual Repro Stage per Subject**

> KB note (not in SDTM v2.0): The Notes column is KB-written: the DOMAIN cell condenses the PDF Notes column, and the other non-blank cells quote the PDF Usage Restrictions column.

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SJ" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SJSEQ | Sequence Number | Num | Identifier | Not in human clinical trials |
| 5 | RSTGCD | Repro Stage Code | Char | Topic | Not in human clinical trials |
| 6 | RSTAGE | Description of Repro Stage | Char | Synonym Qualifier (RSTGCD) | Not in human clinical trials |
| 7 | SJSTDTC | Start Date/Time of Repro Stage | Char | Timing | Not in human clinical trials |
| 8 | SJENDTC | End Date/Time of Repro Stage | Char | Timing | Not in human clinical trials |
| 9 | RPHASE | Repro Phase | Char | Timing | Not in human clinical trials |
| 10 | SJUPDES | Description of Unplanned Repro Stage | Char | Synonym Qualifier (RSTGCD) | Not in human clinical trials |

### 3.2.3.3 Subject Visits

Subject Visits describes the actual start and end date/time for each visit of each individual subject. Planned trial visits are described in the Trial Design Model (see Section 5.1.4.1, Trial Visits). Because actual data does not always follow the plan, the SDTM allows for descriptions of unplanned visits for subjects (SVUPDES).

See the implementation guides for further guidance regarding use of additional identifier and timing variables.

### Variables (16 variables)

**Subject Visits—One Record per Subject Visit, per Subject**

> KB note (not in SDTM v2.0): The Notes column is KB-written: the DOMAIN cell condenses the PDF Notes column; the other cells are blank.

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SV" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | VISITNUM | Visit Number | Num | Topic | |
| 5 | VISIT | Visit Name | Char | Synonym Qualifier (VISITNUM) | |
| 6 | SVPRESP | Pre-Specified | Char | Variable Qualifier (VISITNUM) | |
| 7 | SVOCCUR | Occurrence | Char | Record Qualifier | |
| 8 | SVREASOC | Reason for Occur Value | Char | Record Qualifier | |
| 9 | SVCNTMOD | Contact Mode | Char | Record Qualifier | |
| 10 | SVEPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | |
| 11 | VISITDY | Planned Study Day of Visit | Num | Timing | |
| 12 | SVSTDTC | Start Date/Time of Visit | Char | Timing | |
| 13 | SVENDTC | End Date/Time of Visit | Char | Timing | |
| 14 | SVSTDY | Study Day of Start of Visit | Num | Timing | |
| 15 | SVENDY | Study Day of End of Visit | Num | Timing | |
| 16 | SVUPDES | Description of Unplanned Visit | Char | Record Qualifier | |

### 3.2.3.4 Subject Disease Milestones

Subject Disease Milestones is designed to record the timing, for each subject, of defined trial disease milestones (see Section 5.1.4.3, Trial Disease Milestones).

See the implementation guides for further guidance regarding use of additional identifier and timing variables.

> KB note (not in SDTM v2.0): Examples of disease milestones: diagnosis, progression, relapse, remission.

### Variables (10 variables)

**Subject Disease Milestones—One Record per Disease Milestone, per Subject**

> KB note (not in SDTM v2.0): The Notes column is KB-written: the DOMAIN and MIDS cells quote or condense the PDF Notes column, and the MIDSTYPE cell adds KB wording not given in SDTM v2.0.

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SM" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SMSEQ | Sequence Number | Num | Identifier | |
| 5 | MIDS | Disease Milestone Instance Name | Char | Topic | Name of the specific disease milestone. For disease milestones that can occur multiple times, the name will end with a sequence number. |
| 6 | MIDSTYPE | Disease Milestone Type | Char | Record Qualifier | From Trial Disease Milestones (TM) |
| 7 | SMSTDTC | Start Date/Time of Milestone | Char | Timing | |
| 8 | SMENDTC | End Date/Time of Milestone | Char | Timing | |
| 9 | SMSTDY | Study Day of Start of Milestone | Num | Timing | |
| 10 | SMENDY | Study Day of End of Milestone | Num | Timing | |
