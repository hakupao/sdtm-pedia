# 31_model_obs_classes

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `31`
> - **Concept**: Model: observation classes + special purpose domains
> - **Merged files**: 2
> - **Words**: 6,596
> - **Chars**: 35,500
> - **Sources**:
>   - `model/02_observation_classes.md`
>   - `model/03_special_purpose_domains.md`

---
## Source: `model/02_observation_classes.md`

# SDTM v2.0 — Chapter 3.1: The General Observation Classes

Source: SDTM v2.0, Section 3.1 (Pages 11-39)

## Overview

The majority of observations collected during a study can be divided among 3 general observation classes: Interventions, Events, and Findings. SDTM datasets that represent data about study subjects are of 2 types: general observation class datasets and special-purpose datasets.

Domains based on the general observation classes share a set of common identifier and timing variables (see Section 3.1.4, Identifiers for All Classes, and Section 3.1.5, Timing Variables for All Classes). As a general rule, any valid identifier or timing variable is permissible for use in any dataset based on a general observation class.

## 3.1.1 The Interventions Observation Class

**Structure:** One Record per Constant-dosing Interval or Intervention Episode

The Interventions Observation Class represents investigational, therapeutic, and other treatments that are administered to or used by a subject (with some actual or expected physiological effect). This includes treatments specified by the study protocol (i.e., "exposure").

### Topic and Qualifier Variables (43 variables)

| # | Variable | Label | Type | Role | Key Notes |
|---|----------|-------|------|------|-----------|
| 1 | --TRT | Name of Treatment | Char | Topic | The reported name of the intervention drug, procedure, or therapy |
| 2 | --MODIFY | Modified Treatment Name | Char | Synonym Qualifier (--TRT) | Alteration to collected value for coding purposes |
| 3 | --DECOD | Standardized Treatment Name | Char | Synonym Qualifier (--TRT) | Equivalent to WHODrug generic drug name, SNOMED term, ICD-9 |
| 4 | --MOOD | Mood | Char | Record Qualifier | State applied to a record: "SCHEDULED", "PERFORMED" |
| 5 | --CAT | Category | Char | Grouping Qualifier | Grouping or classification of the topic |
| 6 | --SCAT | Subcategory | Char | Grouping Qualifier | Further grouping; category is in --CAT |
| 7 | --PRESP | Pre-Specified | Char | Variable Qualifier (--TRT) | Values: "Y" or null. Not in nonclinical trials |
| 8 | --OCCUR | Occurrence Indicator | Char | Record Qualifier | Whether a prespecified event or intervention has occurred |
| 9 | --REASOC | Reason for Occur Value | Char | Record Qualifier | Reason the event did or did not occur |
| 10 | --STAT | Completion Status | Char | Record Qualifier | "NOT DONE" or null |
| 11 | --REASND | Reason Not Done | Char | Record Qualifier | Used with --STAT when value is "NOT DONE" |
| 12 | --CNTMOD | Contact Mode | Char | Record Qualifier | Way in which event, visit, or contact was conducted |
| 13 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | Whether intervention was changed due to epidemic or pandemic |
| 14 | --INDC | Indication | Char | Record Qualifier | Sign, symptom, or condition that is the basis for treatment initiation |
| 15 | --CLAS | Class | Char | Variable Qualifier (--TRT) | Standardized or dictionary-derived name for a grouping of drugs |
| 16 | --CLASCD | Class Code | Char | Variable Qualifier (--TRT) | Short sequence of characters to represent --CLAS |
| 17 | --DOSE | Dose | Num | Record Qualifier | Quantity of agent taken or absorbed at a single administration |
| 18 | --DOSTXT | Dose Description | Char | Record Qualifier | Textual description when --DOSE is not populated. E.g., "200-400" |
| 19 | --DOSU | Dose Units | Char | Variable Qualifier (--DOSE/--DOSTXT/--DOSTOT) | Unit of measure: "ng", "mg", "mg/kg" |
| 20 | --TDOSD | Toxic/Physiologic Dose Descr | Char | Record Qualifier | E.g., "LD50", "ED90" |
| 21 | --FTDOSD | Factor for Toxic/Physiologic Dose Descr | Num | Variable Qualifier (--TDOSD) | Multiplier for the value represented by --DOSE and --DOSU |
| 22 | --DOSFRM | Dose Form | Char | Variable Qualifier (--TRT) | "TABLET", "CAPSULE" |
| 23 | --DOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | "Q2H", "QD", "PRN" |
| 24 | --DOSTOT | Total Daily Dose | Num | Record Qualifier | Uses units in --DOSU |
| 25 | --DOSRGM | Intended Dose Regimen | Char | Record Qualifier | "TWO WEEKS ON, TWO WEEKS OFF" |
| 26 | --ROUTE | Route of Administration | Char | Record Qualifier | "ORAL", "INTRAVENOUS" |
| 27 | --LOT | Lot Number | Char | Record Qualifier | Identifier assigned by manufacturer or distributor |
| 28 | --LOC | Location of Administration | Char | Record Qualifier | "ARM" for an injection site |
| 29 | --METHOD | Method of Administration | Char | Record Qualifier | "INFUSION", "INTRAVENOUS". Not in human clinical trials; EX domain only |
| 30 | --LAT | Laterality | Char | Variable Qualifier (--LOC) | "RIGHT", "LEFT", "BILATERAL" |
| 31 | --DIR | Directionality | Char | Variable Qualifier (--LOC) | "ANTERIOR", "LOWER", "PROXIMAL" |
| 32 | --PORTOT | Portion or Totality | Char | Variable Qualifier (--LOC) | "ENTIRE", "SINGLE", "SEGMENT", "MANY" |
| 33 | --FAST | Fasting Status | Char | Record Qualifier | "Y", "N", "U", or null if not relevant |
| 34 | --PSTRG | Pharmaceutical Strength | Num | Record Qualifier | Amount of active ingredient: "50", "300" |
| 35 | --PSTRGU | Pharmaceutical Strength Units | Char | Variable Qualifier (--PSTRG) | "mg/TABLET", "mg/mL" |
| 36 | --TRTV | Treatment Vehicle | Char | Record Qualifier | Carrier or inert medium: "SALINE" |
| 37 | --VAMT | Treatment Vehicle Amount | Num | Record Qualifier | Amount of diluent; not diluent amount alone |
| 38 | --VAMTU | Treatment Vehicle Amount Units | Char | Variable Qualifier (--VAMT) | "mL", "mg" |
| 39 | --ADJ | Reason for Dose Adjustment | Char | Record Qualifier | "ADVERSE EVENT", "INSUFFICIENT RESPONSE" |
| 40 | --RSDISC | Reason for Treatment Discontinuation | Char | Record Qualifier | Reason the treatment was discontinued |
| 41 | --USCHFL | Unscheduled Flag | Char | Record Qualifier | "Y" or null. Not in human clinical trials |
| 42 | --RSTIND | Restraint Indicator | Char | Record Qualifier | Whether animal subject was restrained. Not in human clinical trials |
| 43 | --RSTMOD | Restraint Mode | Char | Record Qualifier | Physical and/or chemical restraint. Not in human clinical trials |

## 3.1.2 The Events Observation Class

**Structure:** One Record per Event

The Events Observation Class represents planned protocol milestones such as randomization and study completion, and occurrences, conditions, or incidents independent of planned study evaluations occurring during the study (e.g., adverse events) or prior to the study (e.g., medical history).

### Topic and Qualifier Variables (56 variables)

| # | Variable | Label | Type | Role | Key Notes |
|---|----------|-------|------|------|-----------|
| 1 | --TERM | Reported Term | Char | Topic | The collected name for an event observation |
| 2 | --MODIFY | Modified Reported Term | Char | Synonym Qualifier (--TERM) | Alteration to collected value for coding purposes |
| 3 | --LLT | Lowest Level Term | Char | Variable Qualifier (--TERM) | Lowest-level term from MedDRA. Not in nonclinical trials |
| 4 | --LLTCD | Lowest Level Term Code | Num | Variable Qualifier (--LLT) | Lowest-level code from MedDRA. Not in nonclinical trials |
| 5 | --DECOD | Dictionary-Derived Term | Char | Synonym Qualifier (--TERM) | Equivalent to Preferred Term ("PT" in MedDRA) |
| 6 | --EVDTYP | Medical History Event Date Type | Char | Variable Qualifier (--STDTC/--ENDTC) | "DIAGNOSIS", "SYMPTOM ONSET", "DISEASE RELAPSE". MH domain only |
| 7 | --PTCD | Preferred Term Code | Num | Variable Qualifier (--DECOD) | Preferred term code from MedDRA. Not in nonclinical trials |
| 8 | --HLT | High Level Term | Char | Variable Qualifier (--TERM) | High-level term from MedDRA. Not in nonclinical trials |
| 9 | --HLTCD | High Level Term Code | Num | Variable Qualifier (--HLT) | Not in nonclinical trials |
| 10 | --HLGT | High Level Group Term | Char | Variable Qualifier (--TERM) | Not in nonclinical trials |
| 11 | --HLGTCD | High Level Group Term Code | Num | Variable Qualifier (--HLGT) | Not in nonclinical trials |
| 12 | --CAT | Category | Char | Grouping Qualifier | Grouping or classification |
| 13 | --SCAT | Subcategory | Char | Grouping Qualifier | Further grouping; category is in --CAT |
| 14 | --PRESP | Pre-Specified | Char | Variable Qualifier (--TERM) | "Y" for prespecified events, null for spontaneously reported |
| 15 | --OCCUR | Occurrence Indicator | Char | Record Qualifier | Not in AE domain |
| 16 | --REASOC | Reason for Occur Value | Char | Record Qualifier | Not in AE domain |
| 17 | --STAT | Completion Status | Char | Record Qualifier | Not in AE domain |
| 18 | --REASND | Reason Not Done | Char | Record Qualifier | Not in AE domain |
| 19 | --BODSYS | Body System or Organ Class | Char | Record Qualifier | "GASTROINTESTINAL DISORDERS" |
| 20 | --BDSYCD | Body System or Organ Class Code | Num | Variable Qualifier (--BODSYS) | MedDRA SOC code. Not in nonclinical trials |
| 21 | --SOC | Primary System Organ Class | Char | Variable Qualifier (--TERM) | SOC from MedDRA. Not in nonclinical trials |
| 22 | --SOCCD | Primary System Organ Class Code | Num | Variable Qualifier (--SOC) | Not in nonclinical trials |
| 23 | --CNTMOD | Contact Mode | Char | Record Qualifier | "IN PERSON", "TELEPHONE", "IVRS" |
| 24 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | |
| 25 | --LOC | Location of Event | Char | Record Qualifier | "ARM" for skin rash |
| 26 | --LAT | Laterality | Char | Variable Qualifier (--LOC) | "RIGHT", "LEFT", "BILATERAL" |
| 27 | --DIR | Directionality | Char | Variable Qualifier (--LOC) | "ANTERIOR", "LOWER", "PROXIMAL" |
| 28 | --PORTOT | Portion or Totality | Char | Variable Qualifier (--LOC) | "ENTIRE", "SINGLE", "SEGMENT", "MANY" |
| 29 | --PARTY | Accountable Party | Char | Record Qualifier | Not in nonclinical trials |
| 30 | --PRTYID | Identification of Accountable Party | Char | Variable Qualifier (--PARTY) | Not in nonclinical trials |
| 31 | --SEV | Severity/Intensity | Char | Record Qualifier | "MILD", "MODERATE", "SEVERE" |
| 32 | --SER | Serious Event | Char | Record Qualifier | "Y" and "N" |
| 33 | --ACN | Action Taken with Study Treatment | Char | Record Qualifier | "DOSE INCREASED", "DOSE NOT CHANGED" |
| 34 | --ACNOTH | Other Action Taken | Char | Record Qualifier | Action unrelated to study treatment |
| 35 | --ACNDEV | Action Taken with Device | Char | Record Qualifier | AE domain only |
| 36 | --REL | Causality | Char | Record Qualifier | "NOT RELATED", "UNLIKELY RELATED", "POSSIBLY RELATED", "RELATED" |
| 37 | --RLDEV | Relationship of Event to Device | Char | Record Qualifier | "CAUSAL", "UNLIKELY" |
| 38 | --RELNST | Relationship to Non-Study Treatment | Char | Record Qualifier | "MORE LIKELY RELATED TO ASPIRIN USE" |
| 39 | --PATT | Pattern of Event | Char | Record Qualifier | "INTERMITTENT", "CONTINUOUS", "SINGLE EVENT" |
| 40 | --OUT | Outcome of Event | Char | Record Qualifier | "RECOVERED/RESOLVED", "FATAL" |
| 41 | --SCAN | Involves Cancer | Char | Record Qualifier | "Y", "N", and null. Not in nonclinical trials |
| 42 | --SCONG | Congenital Anomaly or Birth Defect | Char | Record Qualifier | "Y", "N", and null. Not in nonclinical trials |
| 43 | --SDISAB | Persist or Signif Disability/Incapacity | Char | Record Qualifier | Not in nonclinical trials |
| 44 | --SDTH | Results in Death | Char | Record Qualifier | Not in nonclinical trials |
| 45 | --SHOSP | Requires or Prolongs Hospitalization | Char | Record Qualifier | Not in nonclinical trials |
| 46 | --SLIFE | Is Life Threatening | Char | Record Qualifier | Not in nonclinical trials |
| 47 | --SOD | Occurred with Overdose | Char | Record Qualifier | Not in nonclinical trials |
| 48 | --SMIE | Other Medically Important Serious Event | Char | Record Qualifier | Not in nonclinical trials |
| 49 | --SINTV | Needs Intervention to Prevent Impairment | Char | Record Qualifier | AE domain only; for medical device-related trials |
| 50 | --UNANT | Unanticipated Adverse Device Effect | Char | Record Qualifier | AE domain only |
| 51 | --RLPRT | Rel of AE to Device-Related Procedure | Char | Record Qualifier | AE domain only. "CAUSAL", "UNLIKELY" |
| 52 | --RLPRC | Rel of AE to Non-Dev-Rel Study Activity | Char | Record Qualifier | AE domain only. "CAUSAL", "UNLIKELY" |
| 53 | --CONTRT | Concomitant or Additional Trtmnt Given | Char | Record Qualifier | "Y", "N", and null |
| 54 | --TOX | Toxicity | Char | Variable Qualifier (--TOXGR) | An NCI CTCAE Short Name |
| 55 | --TOXGR | Toxicity Grade | Char | Record Qualifier | A toxicity grade from NCI CTCAE |
| 56 | --USCHFL | Unscheduled Flag | Char | Record Qualifier | Not in human clinical trials |

## 3.1.3 The Findings Observation Class

**Structure:** One Record per Finding

The Findings Observation Class represents observations resulting from planned evaluations to address specific tests or questions such as laboratory tests, ECG testing, and questions listed on questionnaires. The Findings class also includes a subtype, Findings About, which is used to record findings related to observations in the Interventions or Events classes.

### Topic and Qualifier Variables (100 variables)

The Findings class has the largest number of variables due to the wide range of measurement types it supports. Key variable groups include:

**Topic Variables:**

| Variable | Label | Type | Role |
|----------|-------|------|------|
| --TESTCD | Short Name of Measurement, Test, or Exam | Char | Topic |
| --TEST | Name of Measurement, Test, or Exam | Char | Synonym Qualifier (--TESTCD) |

**Result Variables:**

| Variable | Label | Type | Role | Notes |
|----------|-------|------|------|-------|
| --ORRES | Result or Finding in Original Units | Char | Result Qualifier | Original collected result |
| --ORRESU | Original Units | Char | Variable Qualifier (--ORRES) | |
| --STRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Standardized result |
| --STRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Numeric standardized result |
| --STRESU | Standard Units | Char | Variable Qualifier (--STRESC/--STRESN) | |

**Normal Range Variables:**

| Variable | Label | Notes |
|----------|-------|-------|
| --ORNRLO | Reference Range Lower Limit in Orig Unit | Original units |
| --ORNRHI | Reference Range Upper Limit in Orig Unit | Original units |
| --STNRLO | Reference Range Lower Limit-Std Units | Standard units |
| --STNRHI | Reference Range Upper Limit-Std Units | Standard units |
| --STNRC | Reference Range for Char Rslt-Std Units | Char reference range |
| --NRIND | Reference Range Indicator | "NORMAL", "HIGH", "LOW" |

**Specimen-related Variables:**

| Variable | Label | Notes |
|----------|-------|-------|
| --SPEC | Specimen Material Type | "BLOOD", "URINE", "TISSUE" |
| --SPCCND | Specimen Condition | "HEMOLYZED", "LIPEMIC" |
| --SPCUFL | Specimen Usability for the Test | "Y" or null |

**Additional Findings-specific Variables** include --LOINC, --METHOD, --ANMETH, --BLFL, --DRVFL, --LOBXFL, --FAST, --TOX, --TOXGR, --SEV, --CLSIG, --XFN, --NAM, --EVAL, --EVALID, --ACPTFL, --LNKID, --LNKGRP, and many domain-specific variables.

### Findings About (Subtype)

The Findings About observation class is a subtype of Findings used to record findings about events or interventions. It utilizes the Findings general observation class variables with the addition of the --OBJ variable. The order of the --OBJ variable among Findings qualifiers is immediately after the --TEST variable.

| Variable | Label | Type | Role | Notes |
|----------|-------|------|------|-------|
| --OBJ | Object of the Observation | Char | Record Qualifier | Used in domains modeled as Findings About Events or Findings About Interventions. Describes the event or intervention whose property is being measured in --TESTCD/--TEST. |

## 3.1.4 Identifiers for All Classes

STUDYID, DOMAIN, and --SEQ are required in all domains based on one of the 3 general observation classes. Each general class domain must also include at least 1 of the following subject identifiers: USUBJID, SPDEVID, or POOLID.

All identifier variables are allowed for any domain based on one of the 3 general observation classes, unless otherwise noted in the Usage Restrictions.

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Two-character abbreviation for the domain |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Unique identifier for a subject across all studies for the submission |
| 4 | POOLID | Pool Identifier | Char | Identifier | Used for results that are not assignable to a specific subject |
| 5 | SPDEVID | Sponsor Device Identifier | Char | Identifier | |
| 6 | NHOID | Non-Host Organism Identifier | Char | Identifier | Sponsor-defined identifier for a non-host organism |
| 7 | FETUSID | Fetus Identifier | Char | Identifier | Not in human clinical trials |
| 8 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Identification of a focus of study-specific interest |
| 9 | --SEQ | Sequence Number | Num | Identifier | Unique within STUDYID, USUBJID, and DOMAIN |
| 10 | --GRPID | Group ID | Char | Identifier | Used to tie together a block of related records |
| 11 | --REFID | Reference ID | Char | Identifier | Internal or external identifier (e.g., specimen ID, ECG ID) |
| 12 | --RECID | Invariant Record Identifier | Char | Identifier | Identifier for a record that is unique within a domain for a study and remains invariant through subsequent versions |
| 13 | --SPID | Sponsor-Defined Identifier | Char | Identifier | Sponsor-defined reference number |
| 14 | --LNKID | Link ID | Char | Identifier | Used with RELREC dataset-to-dataset linking |
| 15 | --LNKGRP | Link Group ID | Char | Identifier | Used with RELREC to link groups of records |
| 16 | --BEATNO | ECG Beat Number | Num | Identifier | EG Domain only |

## 3.1.5 Timing Variables for All Classes

The following timing variables are available for use in any domain based on one of the 3 general observation classes, except where restricted in the assumptions for the standard domain models in the implementation guides (48 variables):

### Visit and Epoch Variables

| # | Variable | Label | Type | Notes |
|---|----------|-------|------|-------|
| 1 | VISITNUM | Visit Number | Num | Numeric version of VISIT for sorting |
| 2 | VISIT | Visit Name | Char | Protocol-defined visit name |
| 3 | VISITDY | Planned Study Day of Visit | Num | Protocol-defined study day |
| 4 | TAETORD | Planned Order of Element Within Arm | Num | Value for the element within the subject's assigned arm |
| 5 | EPOCH | Epoch | Char | Time period defined in the protocol with a study-specific purpose |
| 6 | RPHASE | Repro Phase | Char | Not in human clinical trials |
| 7 | RPPLDY | Planned Repro Phase Day of Observation | Num | Not in human clinical trials |
| 8 | RPPLSTDY | Planned Repro Phase Day of Obs Start | Num | Not in human clinical trials |
| 9 | RPPLENDY | Planned Repro Phase Day of Obs End | Num | Not in human clinical trials |

### Date/Time Variables

| # | Variable | Label | Type | Format | Notes |
|---|----------|-------|------|--------|-------|
| 10 | --DTC | Date/Time of Collection | Char | ISO 8601 | Primary date/time for the observation |
| 11 | --STDTC | Start Date/Time of Observation | Char | ISO 8601 | Not in Findings class domains |
| 12 | --ENDTC | End Date/Time of Observation | Char | ISO 8601 | |

### Study Day Variables

| # | Variable | Label | Type | Notes |
|---|----------|-------|------|-------|
| 13 | --DY | Study Day of Visit/Collection/Exam | Num | Derived from --DTC and RFSTDTC |
| 14 | --STDY | Study Day of Start of Observation | Num | Not in Findings class domains |
| 15 | --ENDY | Study Day of End of Observation | Num | |
| 16 | --NOMDY | Nominal Study Day for Tabulations | Num | Not in human clinical trials |
| 17 | --NOMLBL | Label for Nominal Study Day | Char | Not in human clinical trials |
| 18 | --RPDY | Actual Repro Phase Day of Observation | Num | Not in human clinical trials |
| 19 | --RPSTDY | Actual Repro Phase Day of Obs Start | Num | Not in human clinical trials |
| 20 | --RPENDY | Actual Repro Phase Day of Obs End | Num | Not in human clinical trials |
| 21 | --XDY | Day of Obs Relative to Exposure | Num | Derived relative to RFXSTDTC |
| 22 | --XSTDY | Start Day of Obs Relative to Exposure | Num | Not in Findings class domains |
| 23 | --XENDY | End Day of Obs Relative to Exposure | Num | |
| 24 | --CHDY | Day of Obs Rel to Challenge Agent | Num | Derived relative to RFCSTDTC |
| 25 | --CHSTDY | Start Day of Obs Rel to Challenge Agent | Num | Not in Findings class domains |
| 26 | --CHENDY | End Day of Obs Rel to Challenge Agent | Num | |
| 27 | --DUR | Collected Duration | Char | ISO 8601 duration |

### Time Point Variables

| # | Variable | Label | Type | Notes |
|---|----------|-------|------|-------|
| 28 | --TPT | Planned Time Point Name | Char | Protocol-defined time point description |
| 29 | --TPTNUM | Planned Time Point Number | Num | Numeric version for sorting |
| 30 | --ELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration |
| 31 | --TPTREF | Time Point Reference | Char | Description of the reference point |
| 32 | --RFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 |

### Relative Timing Variables

| # | Variable | Label | Type | Notes |
|---|----------|-------|------|-------|
| 33 | --STRF | Start Relative to Reference Period | Char | BEFORE, DURING, DURING/AFTER, AFTER, UNKNOWN |
| 34 | --ENRF | End Relative to Reference Period | Char | Same values as --STRF |
| 35 | --EVLINT | Evaluation Interval | Char | ISO 8601 duration or interval |
| 36 | --EVINTX | Evaluation Interval Text | Char | Text description when interval cannot be represented in ISO 8601 |
| 37 | --STRTPT | Start Relative to Reference Time Point | Char | BEFORE, COINCIDENT, AFTER, UNKNOWN |
| 38 | --STTPT | Start Reference Time Point | Char | Text description of start anchor |
| 39 | --ENRTPT | End Relative to Reference Time Point | Char | BEFORE, COINCIDENT, AFTER, ONGOING, UNKNOWN |
| 40 | --ENTPT | End Reference Time Point | Char | Text description of end anchor |

### Disease Milestone Variables

| # | Variable | Label | Type | Notes |
|---|----------|-------|------|-------|
| 41 | MIDS | Disease Milestone Instance Name | Char | Unique name of a disease milestone instance |
| 42 | RELMIDS | Temporal Relation to Milestone Instance | Char | How observation relates to MIDS |
| 43 | MIDSDTC | Disease Milestone Instance Date/Time | Char | Date/time of the disease milestone |

### Assessment Interval and Other Timing Variables

| # | Variable | Label | Type | Notes |
|---|----------|-------|------|-------|
| 44 | --STINT | Planned Start of Assessment Interval | Char | ISO 8601 duration |
| 45 | --ENINT | Planned End of Assessment Interval | Char | ISO 8601 duration |
| 46 | --DETECT | Time in Days to Detection | Num | Not in human clinical trials |
| 47 | --PTFL | Point in Time Flag | Char | Only in Findings class specimen-based domains |
| 48 | --PDUR | Planned Duration of Observation | Char | Only in Findings class specimen-based domains |

## Source: `model/03_special_purpose_domains.md`

# SDTM v2.0 — Chapter 3.2: Special-purpose Domains

Source: SDTM v2.0, Section 3.2 (Pages 40-49)

## Overview

In addition to the 3 general observation classes, a submission will generally include a set of other special-purpose datasets of specific standardized structures to represent additional important information. A Demographics special-purpose domain is included with human and animal studies. Other special-purpose domains may be included.

## Demographics (DM)

**Structure:** One record per subject

The Demographics domain includes a set of essential standard variables that describe each subject in a clinical study. It is the parent domain to which all other observations are linked. The DM domain describes the essential characteristics of the study subjects, and is used by reviewers for selecting subsets of subjects for analysis. The DM domain, as with other datasets, includes identifiers, a topic variable, timing variables, and qualifiers.

### Variables (38 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "DM" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SUBJID | Subject Identifier for the Study | Char | Topic | Subject identifier, which must be unique within the study |
| 5 | RFSTDTC | Subject Reference Start Date/Time | Char | Record Qualifier | Usually first dose date |
| 6 | RFENDTC | Subject Reference End Date/Time | Char | Record Qualifier | Usually date of last dose |
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
| 19 | AGE | Age | Num | Record Qualifier | Numeric age at RFSTDTC |
| 20 | AGETXT | Age Text | Char | Record Qualifier | Used when exact age is unknown; e.g., "18-25" |
| 21 | AGEU | Age Units | Char | Variable Qualifier (AGE/AGETXT) | "YEARS", "MONTHS", "DAYS" |
| 22 | SEX | Sex | Char | Record Qualifier | Subject to controlled terminology |
| 23 | RACE | Race | Char | Record Qualifier | Not in nonclinical trials |
| 24 | ETHNIC | Ethnicity | Char | Record Qualifier | Not in nonclinical trials |
| 25 | SPECIES | Species | Char | Record Qualifier | **Not for human clinical trials** |
| 26 | STRAIN | Strain/Substrain | Char | Record Qualifier | **Not for human clinical trials** |
| 27 | SBSTRAIN | Strain/Substrain Details | Char | Variable Qualifier (STRAIN) | **Not for human clinical trials** |
| 28 | ARMCD | Planned Arm Code | Char | Record Qualifier | Short version of ARM |
| 29 | ARM | Description of Planned Arm | Char | Synonym Qualifier (ARMCD) | |
| 30 | ACTARMCD | Actual Arm Code | Char | Record Qualifier | Not in nonclinical trials |
| 31 | ACTARM | Description of Actual Arm | Char | Synonym Qualifier (ACTARMCD) | Not in nonclinical trials |
| 32 | ARMNRS | Reason Arm and/or Actual Arm is Null | Char | Record Qualifier | When arm assignment is not possible |
| 33 | ACTARMUD | Description of Unplanned Actual Arm | Char | Record Qualifier | |
| 34 | SETCD | Set Code | Char | Record Qualifier | Use with extreme caution |
| 35 | RPATHCD | Reproductive Pathway Code | Char | Record Qualifier | **Not for human clinical trials** |
| 36 | COUNTRY | Country | Char | Record Qualifier | ISO 3166-1 Alpha-3. Not in nonclinical trials |
| 37 | DMDTC | Date/Time of Collection | Char | Timing | |
| 38 | DMDY | Study Day of Collection | Num | Timing | |

### Key Reference Date Variables

| Variable | Description | Typical Use |
|----------|-------------|-------------|
| RFSTDTC | Subject Reference Start Date/Time | Usually first dose; basis for study day calculation |
| RFENDTC | Subject Reference End Date/Time | Usually last dose date |
| RFXSTDTC | Date/Time of First Study Treatment | First exposure to study treatment |
| RFXENDTC | Date/Time of Last Study Treatment | Last exposure to study treatment |
| RFCSTDTC | Date/Time of First Challenge Agent Admin | First exposure to challenge agent |
| RFCENDTC | Date/Time of Last Challenge Agent Admin | Last exposure to challenge agent |
| RFICDTC | Date/Time of Informed Consent | Consent date |
| RFPENDTC | Date/Time of End of Participation | Completion/withdrawal date |

## Comments (CO)

**Structure:** One record per comment per subject (or per study)

The Comments special-purpose domain is used to capture free-text comments that are not a part of normal domain data. Comments are normally supplied by a principal investigator, but might also be collected from other sources such as central reviewers. When collected, comments should be submitted in a single Comments domain, defined here.

### Variables (15 variables)

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

## Subject Elements (SE)

**Structure:** One record per actual Element per subject

Describes the actual Elements (blocks of time) experienced by each subject during the study. Planned elements are described in the Trial Design Model. Because actual data does not always follow the plan, the SDTM allows for descriptions of an unplanned element for subjects (SEUPDES).

### Variables (13 variables)

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

## Subject Repro Stages

**Structure:** One record per Actual Repro Stage per Subject

**Note:** Not for use with human clinical trials.

Describes the actual order of repro stages experienced by the subject, together with the start date or start date and time and end date/time for each. Planned repro stages are described in the Trial Design Model. Because actual data does not always follow the plan, the SDTM allows for descriptions of an unplanned repro stage for subjects (SJUPDES).

### Variables (10 variables)

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

## Subject Visits (SV)

**Structure:** One record per actual or planned visit per subject

Describes the actual study visits experienced by each individual subject. Planned trial visits are described in the Trial Design Model. Because actual data does not always follow the plan, the SDTM allows for descriptions of unplanned visits for subjects (SVUPDES).

### Variables (16 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SV" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | VISITNUM | Visit Number | Num | Topic | |
| 5 | VISIT | Visit Name | Char | Synonym Qualifier (VISITNUM) | |
| 6 | SVPRESP | Pre-Specified | Char | Variable Qualifier (VISITNUM) | |
| 7 | SVOCCUR | Occurrence | Char | Record Qualifier | |
| 8 | SVREASOC | Reason for Occurrence Value | Char | Record Qualifier | |
| 9 | SVCNTMOD | Contact Mode | Char | Record Qualifier | |
| 10 | SVEPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | |
| 11 | VISITDY | Planned Study Day of Visit | Num | Timing | |
| 12 | SVSTDTC | Start Date/Time of Visit | Char | Timing | |
| 13 | SVENDTC | End Date/Time of Visit | Char | Timing | |
| 14 | SVSTDY | Study Day of Start of Visit | Num | Timing | |
| 15 | SVENDY | Study Day of End of Visit | Num | Timing | |
| 16 | SVUPDES | Description of Unplanned Visit | Char | Record Qualifier | |

## Subject Disease Milestones (SM)

**Structure:** One record per Disease Milestone per subject

Records the disease milestones experienced by each subject (e.g., diagnosis, progression, relapse, remission).

### Variables (10 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | "SM" |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | SMSEQ | Sequence Number | Num | Identifier | |
| 5 | MIDS | Disease Milestone Instance Name | Char | Topic | Unique name linking to TM |
| 6 | MIDSTYPE | Disease Milestone Type | Char | Record Qualifier | From Trial Disease Milestones (TM) |
| 7 | SMSTDTC | Start Date/Time of Milestone | Char | Timing | |
| 8 | SMENDTC | End Date/Time of Milestone | Char | Timing | |
| 9 | SMSTDY | Study Day of Start of Milestone | Num | Timing | |
| 10 | SMENDY | Study Day of End of Milestone | Num | Timing | |
