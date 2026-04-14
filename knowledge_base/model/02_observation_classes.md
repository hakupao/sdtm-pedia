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

### Topic and Qualifier Variables (100+ variables)

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

The Findings About observation class is a subtype of Findings used to record findings about events or interventions. Key additional variables:

| Variable | Label | Notes |
|----------|-------|-------|
| --OBJ | Object of the Observation | Identifies the event or intervention being assessed |
| FAOBJ | Object of the Finding About Observation | FA domain-specific |

## 3.1.4 Identifiers for All Classes

Variables shared across all 3 general observation classes:

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Unique identifier for a study |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Two-character abbreviation for the domain |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Unique identifier for a subject across all studies for the submission |
| 4 | --SEQ | Sequence Number | Num | Identifier | Unique within STUDYID, USUBJID, and DOMAIN |
| 5 | --GRPID | Group ID | Char | Identifier | Used to tie together a block of related records |
| 6 | --REFID | Reference ID | Char | Identifier | Internal or external identifier (e.g., specimen ID, ECG ID) |
| 7 | --SPID | Sponsor-Defined Identifier | Char | Identifier | Sponsor-defined reference number |
| 8 | --LNKID | Link ID | Char | Identifier | Used with RELREC dataset-to-dataset linking |
| 9 | --LNKGRP | Link Group ID | Char | Identifier | Used with RELREC to link groups of records |
| 10 | POOLID | Pool Identifier | Char | Identifier | Identifier used for pooling subjects in nonclinical studies |
| 11 | SPDEVID | Sponsor Device Identifier | Char | Identifier | AE domain only |
| 12 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Focus identifier for study-specific interest |
| 13 | --BEATNO | ECG Beat Number | Num | Identifier | Beat number for ECG observations |
| 14 | --RUNID | Run or Replicate ID | Char | Identifier | Lab run/replicate identifier |
| 15 | --REFID (duplicate role as Reference ID and External File Name) | | | | |
| 16 | --RDEVID | Related Device Identifier | Char | Identifier | AP domains only |

## 3.1.5 Timing Variables for All Classes

Variables for representing time in all general observation class domains (48 variables):

### Date/Time Variables

| Variable | Label | Format | Notes |
|----------|-------|--------|-------|
| --DTC | Date/Time of Collection | ISO 8601 datetime or interval | Primary date/time for the observation |
| --STDTC | Start Date/Time of Observation | ISO 8601 datetime or interval | |
| --ENDTC | End Date/Time of Observation | ISO 8601 datetime or interval | |
| --DY | Study Day of Visit/Collection/Exam | Num | Derived from --DTC and RFSTDTC |
| --STDY | Study Day of Start of Observation | Num | |
| --ENDY | Study Day of End of Observation | Num | |
| --DUR | Duration | ISO 8601 duration | |

### Visit Variables

| Variable | Label | Notes |
|----------|-------|-------|
| VISITNUM | Visit Number | Numeric version of VISIT for sorting |
| VISIT | Visit Name | Protocol-defined visit name |
| VISITDY | Planned Study Day of Visit | Protocol-defined study day |

### Time Point Variables

| Variable | Label | Notes |
|----------|-------|-------|
| --TPT | Planned Time Point Name | Protocol-defined time point description |
| --TPTNUM | Planned Time Point Number | Numeric version for sorting |
| --ELTM | Planned Elapsed Time from Time Point Ref | ISO 8601 duration |
| --TPTREF | Time Point Reference | Description of the reference point |
| --RFTDTC | Date/Time of Reference Time Point | ISO 8601 |

### Relative Timing Variables

| Variable | Label | Notes |
|----------|-------|-------|
| --STRF | Start Relative to Reference Period | BEFORE, DURING, DURING/AFTER, AFTER, UNKNOWN |
| --ENRF | End Relative to Reference Period | Same values as --STRF |
| --STTPT | Start Reference Time Point | Text description of start anchor |
| --STRTPT | Start Relative to Reference Time Point | BEFORE, COINCIDENT, AFTER, UNKNOWN |
| --ENTPT | End Reference Time Point | Text description of end anchor |
| --ENRTPT | End Relative to Reference Time Point | BEFORE, COINCIDENT, AFTER, ONGOING, UNKNOWN |

### Disease Milestone Variables

| Variable | Label | Notes |
|----------|-------|-------|
| MIDS | Disease Milestone Instance Name | Unique name of a disease milestone instance |
| RELMIDS | Relationship to Disease Milestone Instance | How observation relates to MIDS |
| MIDSDTC | Disease Milestone Instance Date | Date/time of the disease milestone |

### Additional Timing Variables

| Variable | Label | Notes |
|----------|-------|-------|
| --STINT | Planned Start of Assessment Interval | ISO 8601 duration |
| --ENINT | Planned End of Assessment Interval | ISO 8601 duration |
| --DETECT | Detection Day of Onset | Num |
| --PTFL | Point in Time Flag | "Y" for point-in-time observations |
| --PDUR | Planned Duration of Observation | ISO 8601 duration |
| --XSTDY | Study Day of Start of Crossover Study Day | Num |
| --CHSTDY | Change of Study Day | Num |
