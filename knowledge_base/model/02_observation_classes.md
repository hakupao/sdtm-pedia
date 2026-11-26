# SDTM v2.0 — Sections 3-3.1: Study Subject Data; The General Observation Classes

Source: SDTM v2.0, Sections 3-3.1 (Pages 11-39)

## 3 Study Subject Data

Observations about study subjects are normally represented in a series of domains. A domain is defined as a collection of logically related observations with a common topic. The logic of the relationship may pertain to the scientific subject matter of the data or to its role in the trial. For example, "Subject 101 had an adverse event of mild nausea starting on study day 6" is an observation belonging to the Adverse Events (AE) domain in a clinical trial.

SDTM datasets that represent data about study subjects are of 2 types: general observation class datasets and special-purpose datasets. General observation class domains conform to general structures for 1 of 3 classes: findings, events, and interventions. The data for a study would generally include multiple domains in each general observation class. In contrast to general observation class models on which individual domains can be based, special-purpose domains are specified completely.

Domains based on the general observation classes are specified in SDTM implementation guides (see Section 1.2, Implementation Advice for this Model).

Each study subject domain dataset is distinguished by a unique 2-character code. This code, which is stored in the SDTM variable named DOMAIN, is used in the dataset name, as the value of the DOMAIN variable in that dataset, and as a prefix for most variable names in that dataset.

Domain codes are also used in RDOMAIN, a variable that is included in several relationship datasets and in the Comments special-purpose domain.

## 3.1 The General Observation Classes

The majority of observations collected during a study can be divided among 3 general observation classes: Interventions, Events, and Findings.

- The Interventions Observation Class represents investigational, therapeutic, and other treatments that are administered to or used by a subject (with some actual or expected physiological effect). This includes treatments specified by the study protocol (i.e., "exposure").
- The Events Observation Class represents planned protocol milestones such as randomization and study completion, and occurrences, conditions, or incidents independent of planned study evaluations occurring during the study (e.g., adverse events) or prior to the study (e.g., medical history).
- The Findings Observation Class represents observations resulting from planned evaluations to address specific tests or questions such as laboratory tests, electrocardiogram (ECG) testing, and questions listed on questionnaires. The Findings class also includes a subtype, Findings About, which is used to record findings related to observations in the Interventions or Events classes.

Datasets based on any of the general observation classes share a set of common identifier and timing variables (see Section 3.1.4, Identifiers for All Classes, and Section 3.1.5, Timing Variables for All Classes). As a general rule, any valid identifier or timing variable is permissible for use in any dataset based on a general observation class.

The SDTM is the foundation for many implementations. SDTM implementation guides specify particular domains based on the general observation classes. Domain specification tables in the implementation guides describe which variables must be included in the domain. Not all variables described in the tables in this document (SDTM tables) are appropriate for all domains in all implementations. The SDTM includes information on variables which are not to be used in human clinical trials. Refer to the implementation guides for specific information on any identifier or timing variables that are not allowed in a particular observation class domain.

In the tables in this document, the presence of 2 hyphens before the variable name (e.g., --TRT) is used to indicate the required use of a prefix based on the 2-character domain code. The domain code is used as a variable prefix to minimize the risk of difficulty when merging or joining domains for reporting purposes. The variable with 2 hyphens may be referred to as a "root" variable.

Domain-specific variables, a concept introduced in SDTM v1.5, are for use in a limited number of designated domains based on general observation classes and will be identified in the appropriate implementation guide. The variable names include the specific domain prefix. Domain-specific variables are included in the table of general observation class variables; the Usage Restrictions column of the table indicates the domains in which the variable is allowed.

In addition to the 3 general observation classes, a study will generally include a set of other special-purpose datasets; see Section 3.2, Special-purpose Domains.

## 3.1.1 The Interventions Observation Class

### Topic and Qualifier Variables (43 variables)

**Interventions—Topic and Qualifier Variables—One Record per Constant-dosing Interval or Intervention Episode**

> KB note (not in SDTM v2.0): The Key Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0.

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
| 9 | --REASOC | Reason for Occur Value | Char | Record Qualifier | --REASOC is the reason the intervention did or did not occur, according to the value in --OCCUR. This does not replace --INDC. |
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
| 21 | --FTDOSD | Factor for Toxic/Physiologic Dose Descr | Num | Variable Qualifier (--TDOSD) | The quantity given for the multiplier of --TDOSD. |
| 22 | --DOSFRM | Dose Form | Char | Variable Qualifier (--TRT) | "TABLET", "CAPSULE" |
| 23 | --DOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | "Q2H", "QD", "PRN" |
| 24 | --DOSTOT | Total Daily Dose | Num | Record Qualifier | Uses units in --DOSU |
| 25 | --DOSRGM | Intended Dose Regimen | Char | Record Qualifier | "TWO WEEKS ON, TWO WEEKS OFF" |
| 26 | --ROUTE | Route of Administration | Char | Record Qualifier | "ORAL", "INTRAVENOUS" |
| 27 | --LOT | Lot Number | Char | Record Qualifier | Identifier assigned by manufacturer or distributor |
| 28 | --LOC | Location of Administration | Char | Record Qualifier | "ARM" for an injection site |
| 29 | --METHOD | Method of Administration | Char | Record Qualifier | "INFUSION" when ROUTE is "INTRAVENOUS". Not in human clinical trials; EX domain only |
| 30 | --LAT | Laterality | Char | Variable Qualifier (--LOC) | "RIGHT", "LEFT", "BILATERAL" |
| 31 | --DIR | Directionality | Char | Variable Qualifier (--LOC) | "ANTERIOR", "LOWER", "PROXIMAL" |
| 32 | --PORTOT | Portion or Totality | Char | Variable Qualifier (--LOC) | "ENTIRE", "SINGLE", "SEGMENT", "MANY" |
| 33 | --FAST | Fasting Status | Char | Record Qualifier | "Y", "N", "U", or null if not relevant |
| 34 | --PSTRG | Pharmaceutical Strength | Num | Record Qualifier | Amount of active ingredient: "50", "300" |
| 35 | --PSTRGU | Pharmaceutical Strength Units | Char | Variable Qualifier (--PSTRG) | "mg/TABLET", "mg/mL" |
| 36 | --TRTV | Treatment Vehicle | Char | Record Qualifier | Carrier or inert medium: "SALINE" |
| 37 | --VAMT | Treatment Vehicle Amount | Num | Record Qualifier | Amount of the prepared product (treatment plus vehicle) administered. Note: Should not be diluent amount alone. |
| 38 | --VAMTU | Treatment Vehicle Amount Units | Char | Variable Qualifier (--VAMT) | "mL", "mg" |
| 39 | --ADJ | Reason for Dose Adjustment | Char | Record Qualifier | "ADVERSE EVENT", "INSUFFICIENT RESPONSE" |
| 40 | --RSDISC | Reason for Treatment Discontinuation | Char | Record Qualifier | Reason the treatment was discontinued |
| 41 | --USCHFL | Unscheduled Flag | Char | Record Qualifier | "Y" or null. Not in human clinical trials |
| 42 | --RSTIND | Restraint Indicator | Char | Record Qualifier | Whether animal subject was restrained. Not in human clinical trials |
| 43 | --RSTMOD | Restraint Mode | Char | Record Qualifier | Physical and/or chemical restraint. Not in human clinical trials |

## 3.1.2 The Events Observation Class

### Topic and Qualifier Variables (56 variables)

**Events—Topic and Qualifier Variables—One Record per Event**

> KB note (not in SDTM v2.0): The Key Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0.

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
| 35 | --ACNDEV | Action Taken with Device | Char | Record Qualifier | An action taken with a device as the result of the event. |
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

### Topic and Qualifier Variables (100 variables)

> KB note (not in SDTM v2.0): The Findings class has the largest number of variables due to the wide range of measurement types it supports.

**Findings—Topic and Qualifier Variables—One Record per Finding**

> KB note (not in SDTM v2.0): The Key Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0. Cells that state only a domain restriction quote the PDF Usage Restrictions column; a blank cell means the PDF Usage Restrictions column is also blank.

| # | Variable | Label | Type | Role | Key Notes |
|---|----------|-------|------|------|-----------|
| 1 | --TESTCD | Short Name of Measurement, Test, or Exam | Char | Topic |  |
| 2 | --TEST | Name of Measurement, Test, or Exam | Char | Synonym Qualifier (--TESTCD) |  |
| 3 | --SBMRKS | Sublineage Marker String | Char | Variable Qualifier (--TESTCD) | CP domain only |
| 4 | --CELSTA | Cell State | Char | Variable Qualifier (--TESTCD) | CP domain only |
| 5 | --CSMRKS | Cell State Marker String | Char | Variable Qualifier (--TESTCD) | CP domain only |
| 6 | --CNTMOD | Contact Mode | Char | Record Qualifier |  |
| 7 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier |  |
| 8 | --TSTCND | Test Condition | Char | Variable Qualifier (--TESTCD) | CP, IS, and LB domains only |
| 9 | --CNDAGT | Test Condition Agent | Char | Record Qualifier | CP, IS, and LB domains only |
| 10 | --BDAGNT | Binding Agent | Char | Variable Qualifier (--TESTCD) | CP, IS, and LB domains only |
| 11 | --ABCLID | Antibody Clone Identifier | Char | Record Qualifier | CP domain only |
| 12 | --MRKSTR | Marker String | Char | Record Qualifier | CP domain only |
| 13 | --GATE | Gate | Char | Record Qualifier | CP domain only |
| 14 | --GATDEF | Gate Definition | Char | Record Qualifier | CP domain only |
| 15 | --TSTOPO | Test Operational Objective | Char | Variable Qualifier (--TESTCD) |  |
| 16 | --MSCBCE | Molecule Secreted by Cells | Char | Variable Qualifier (--TESTCD) | IS domain only |
| 17 | --AGENT | Agent Name | Char | Record Qualifier | MS Domain only |
| 18 | --CONC | Agent Concentration | Num | Variable Qualifier (--AGENT) | MS Domain only |
| 19 | --CONCU | Agent Concentration Units | Char | Variable Qualifier (--CONC) | MS Domain only |
| 20 | --MODIFY | Modified Result Term | Char | Synonym Qualifier (--ORRES) |  |
| 21 | --TSTDTL | Measurement, Test, or Examination Detail | Char | Variable Qualifier (--TESTCD) |  |
| 22 | --SPTSTD | Sponsor Test Description | Char | Record Qualifier | CP domain only |
| 23 | --CAT | Category | Char | Grouping Qualifier |  |
| 24 | --SCAT | Subcategory | Char | Grouping Qualifier |  |
| 25 | --TSTPNL | Test Panel | Char | Grouping Qualifier | CP domain only |
| 26 | --POS | Position of Subject During Observation | Char | Record Qualifier |  |
| 27 | --BODSYS | Body System or Organ Class | Char | Record Qualifier |  |
| 28 | --ORRES | Result or Finding in Original Units | Char | Result Qualifier | Original collected result |
| 29 | --ORRESU | Original Units | Char | Variable Qualifier (--ORRES/--ORNRLO/--ORNRHI/--ORREF) |  |
| 30 | --RESSCL | Result Scale | Char | Record Qualifier |  |
| 31 | --RESTYP | Result Type | Char | Record Qualifier |  |
| 32 | --COLSRT | Collected Summary Result Type | Char | Variable Qualifier (--TESTCD) |  |
| 33 | --ORNRLO | Normal Range Lower Limit-Original Units | Char | Variable Qualifier (--ORRES) | Original units |
| 34 | --ORNRHI | Normal Range Upper Limit-Original Units | Char | Variable Qualifier (--ORRES) | Original units |
| 35 | --ORREF | Reference Result in Original Units | Char | Variable Qualifier (--ORRES) |  |
| 36 | --LLOD | Lower Limit of Detection | Char | Variable Qualifier (--TESTCD) |  |
| 37 | --STRESC | Result or Finding in Standard Format | Char | Result Qualifier | Standardized result |
| 38 | --IMPLBL | Implantation Site Label | Char | Record Qualifier | Not in human clinical trials; IC Domain only |
| 39 | --STRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Numeric standardized result |
| 40 | --STRESU | Standard Units | Char | Variable Qualifier (--STRESC/--STRESN/--STNRLO/--STNRHI/--STREFC/--STREFN/--LLOQ/--ULOQ) |  |
| 41 | --STNRLO | Normal Range Lower Limit-Standard Units | Num | Variable Qualifier (--STRESC/--STRESN) | Standard units |
| 42 | --STNRHI | Normal Range Upper Limit-Standard Units | Num | Variable Qualifier (--STRESC/--STRESN) | Standard units |
| 43 | --STNRC | Normal Range for Character Results | Char | Variable Qualifier (--STRESC) | Char reference range |
| 44 | --STREFC | Reference Result in Standard Format | Char | Variable Qualifier (--STRESC) |  |
| 45 | --STREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier (--STRESN) |  |
| 46 | --NRIND | Normal/Reference Range Indicator | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | "NORMAL", "HIGH", "LOW" |
| 47 | --RESCAT | Result Category | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) |  |
| 48 | --INHERT | Inheritability | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 49 | --GENREF | Genome Reference | Char | Variable Qualifier (--METHOD) | GF domain only |
| 50 | --CHROM | Chromosome Identifier | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 51 | --SYM | Genomic Symbol | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 52 | --SYMTYP | Genomic Symbol Type | Char | Variable Qualifier (--SYM) | GF domain only |
| 53 | --GENLOC | Genetic Location | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 54 | --GENSR | Genetic Sub-Region | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 55 | --SEQID | Sequence Identifier | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 56 | --PVRID | Published Variant Identifier | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 57 | --COPYID | Copy Identifier | Char | Variable Qualifier (--ORRES/--STRESC/--STRESN) | GF domain only |
| 58 | --CHRON | Chronicity of Finding | Char | Variable Qualifier (--STRESC) |  |
| 59 | --DISTR | Distribution Pattern of Finding | Char | Variable Qualifier (--STRESC) |  |
| 60 | --RESLOC | Result Location of Finding | Char | Record Qualifier | Not in human clinical trials |
| 61 | --STAT | Completion Status | Char | Record Qualifier |  |
| 62 | --REASND | Reason Not Done | Char | Record Qualifier |  |
| 63 | --XFN | External File Path | Char | Record Qualifier |  |
| 64 | --NAM | Laboratory/Vendor Name | Char | Record Qualifier |  |
| 65 | --LOINC | LOINC Code | Char | Record Qualifier |  |
| 66 | --SPEC | Specimen Material Type | Char | Record Qualifier | "BLOOD", "URINE", "TISSUE" |
| 67 | --ANTREG | Anatomical Region | Char | Variable Qualifier (--SPEC) |  |
| 68 | --SPCCND | Specimen Condition | Char | Record Qualifier | "HEMOLYZED", "LIPEMIC" |
| 69 | --SPCUFL | Specimen Usability for the Test | Char | Record Qualifier | The value will be "N" if the specimen is not usable, and null if the specimen is usable. |
| 70 | --LOC | Location Used for the Measurement | Char | Record Qualifier |  |
| 71 | --LAT | Laterality | Char | Variable Qualifier (--LOC/--SPEC) |  |
| 72 | --DIR | Directionality | Char | Variable Qualifier (--LOC/--SPEC) |  |
| 73 | --PORTOT | Portion or Totality | Char | Variable Qualifier (--LOC/--SPEC) |  |
| 74 | --METHOD | Method of Test or Examination | Char | Record Qualifier |  |
| 75 | --RUNID | Run ID | Char | Record Qualifier |  |
| 76 | --ANMETH | Analysis Method | Char | Record Qualifier |  |
| 77 | --TMTHSN | Test Method Sensitivity | Char | Record Qualifier |  |
| 78 | --LEAD | Lead Identified to Collect Measurements | Char | Record Qualifier |  |
| 79 | --CSTATE | Consciousness State | Char | Record Qualifier |  |
| 80 | --LOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier |  |
| 81 | --BLFL | Baseline Flag | Char | Record Qualifier |  |
| 82 | --FAST | Fasting Status | Char | Record Qualifier |  |
| 83 | --DRVFL | Derived Flag | Char | Record Qualifier |  |
| 84 | --EVAL | Evaluator | Char | Record Qualifier | Not in QS, FT, and clinical classifications use case of RS |
| 85 | --EVALID | Evaluator Identifier | Char | Variable Qualifier (--EVAL) | Not in QS, FT, and clinical classifications use case of RS |
| 86 | --ACPTFL | Accepted Record Flag | Char | Record Qualifier |  |
| 87 | --TOX | Toxicity | Char | Variable Qualifier (--TOXGR) |  |
| 88 | --TOXGR | Toxicity Grade | Char | Record Qualifier |  |
| 89 | --SEV | Severity/Intensity | Char | Record Qualifier |  |
| 90 | --CLSIG | Clinically Significant, Collected | Char | Record Qualifier |  |
| 91 | --DTHREL | Relationship to Death | Char | Record Qualifier | Not in human clinical trials |
| 92 | --LLOQ | Lower Limit of Quantitation | Num | Variable Qualifier (--STRESC/--STRESN) |  |
| 93 | --ULOQ | Upper Limit of Quantitation | Num | Variable Qualifier (--STRESC/--STRESN) |  |
| 94 | --REASPF | Reason Test Performed | Char | Record Qualifier |  |
| 95 | --EXCLFL | Exclude from Statistics | Char | Record Qualifier | Not in human clinical trials |
| 96 | --REASEX | Reason for Exclusion from Statistics | Char | Record Qualifier | Not in human clinical trials |
| 97 | --USCHFL | Unscheduled Flag | Char | Record Qualifier | Not in human clinical trials |
| 98 | --REPNUM | Repetition Number | Num | Record Qualifier |  |
| 99 | --RSTIND | Restraint Indicator | Char | Record Qualifier | Not in human clinical trials |
| 100 | --RSTMOD | Restraint Mode | Char | Record Qualifier | Not in human clinical trials |

### 3.1.3.1 Findings About Events or Interventions

Findings About Events or Interventions is a specialization of the Findings class that utilizes the Findings general observation class variables with the addition of the --OBJ variable, as described in the following table. The order of the --OBJ variable among Findings qualifiers is immediately after the --TEST variable.

**Findings About—Additional Qualifier Variables**

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | --OBJ | Object of the Observation | Char | Record Qualifier | Used in domains modeled as Findings About Events or Findings About Interventions. Describes the event or intervention whose property is being measured in --TESTCD/--TEST. |

## 3.1.4 Identifiers for All Classes

STUDYID, DOMAIN, and --SEQ are required in all domains based on one of the 3 general observation classes. Each general class domain must also include at least 1 of the following subject identifiers: USUBJID, SPDEVID, or POOLID.

All identifier variables are allowed for any domain based on one of the 3 general observation classes, unless otherwise noted in the Usage Restrictions.

**All Observation Classes—Identifiers**

> KB note (not in SDTM v2.0): The Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0.

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

The following timing variables are available for use in any domain based on one of the 3 general observation classes, except where restricted in the assumptions for the standard domain models in the implementation guides. See Section 3.2, Special-purpose Domains, for additional guidance relating to special-purpose domains.

**All Observation Classes—Timing Variables**

> KB note (not in SDTM v2.0): The PDF presents the 48 timing variables as one table; the KB splits it into the sub-tables below (row numbers follow the PDF).
>
> KB note (not in SDTM v2.0): In the timing sub-tables, the Notes column is KB-written: most cells quote or condense the PDF Format, Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or value lists not given in SDTM v2.0.

### Visit and Epoch Variables

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | VISITNUM | Visit Number | Num | Timing | Numeric version of VISIT for sorting |
| 2 | VISIT | Visit Name | Char | Timing | Protocol-defined visit name |
| 3 | VISITDY | Planned Study Day of Visit | Num | Timing | Protocol-defined study day |
| 4 | TAETORD | Planned Order of Element Within Arm | Num | Timing | Value for the element within the subject's assigned arm |
| 5 | EPOCH | Epoch | Char | Timing | Time period defined in the protocol with a study-specific purpose |
| 6 | RPHASE | Repro Phase | Char | Timing | Not in human clinical trials |
| 7 | RPPLDY | Planned Repro Phase Day of Observation | Num | Timing | Not in human clinical trials |
| 8 | RPPLSTDY | Planned Repro Phase Day of Obs Start | Num | Timing | Not in human clinical trials |
| 9 | RPPLENDY | Planned Repro Phase Day of Obs End | Num | Timing | Not in human clinical trials |

### Date/Time Variables

| # | Variable | Label | Type | Format | Role | Notes |
|---|----------|-------|------|--------|------|-------|
| 10 | --DTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Primary date/time for the observation |
| 11 | --STDTC | Start Date/Time of Observation | Char | ISO 8601 datetime or interval | Timing | Not in Findings class domains |
| 12 | --ENDTC | End Date/Time of Observation | Char | ISO 8601 datetime or interval | Timing |  |

### Study Day Variables

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 13 | --DY | Study Day of Visit/Collection/Exam | Num | Timing | Derived from --DTC and RFSTDTC |
| 14 | --STDY | Study Day of Start of Observation | Num | Timing | Not in Findings class domains |
| 15 | --ENDY | Study Day of End of Observation | Num | Timing |  |
| 16 | --NOMDY | Nominal Study Day for Tabulations | Num | Timing | Not in human clinical trials |
| 17 | --NOMLBL | Label for Nominal Study Day | Char | Timing | Not in human clinical trials |
| 18 | --RPDY | Actual Repro Phase Day of Observation | Num | Timing | Not in human clinical trials |
| 19 | --RPSTDY | Actual Repro Phase Day of Obs Start | Num | Timing | Not in human clinical trials |
| 20 | --RPENDY | Actual Repro Phase Day of Obs End | Num | Timing | Not in human clinical trials |
| 21 | --XDY | Day of Obs Relative to Exposure | Num | Timing | Derived relative to RFXSTDTC |
| 22 | --XSTDY | Start Day of Obs Relative to Exposure | Num | Timing | Not in Findings class domains |
| 23 | --XENDY | End Day of Obs Relative to Exposure | Num | Timing |  |
| 24 | --CHDY | Day of Obs Rel to Challenge Agent | Num | Timing | Derived relative to RFCSTDTC |
| 25 | --CHSTDY | Start Day of Obs Rel to Challenge Agent | Num | Timing | Not in Findings class domains |
| 26 | --CHENDY | End Day of Obs Rel to Challenge Agent | Num | Timing |  |
| 27 | --DUR | Collected Duration | Char | Timing | ISO 8601 duration |

### Time Point Variables

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 28 | --TPT | Planned Time Point Name | Char | Timing | Protocol-defined time point description |
| 29 | --TPTNUM | Planned Time Point Number | Num | Timing | Numeric version for sorting |
| 30 | --ELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | ISO 8601 duration |
| 31 | --TPTREF | Time Point Reference | Char | Timing | Description of the reference point |
| 32 | --RFTDTC | Date/Time of Reference Time Point | Char | Timing | ISO 8601 |

### Relative Timing Variables

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 33 | --STRF | Start Relative to Reference Period | Char | Timing | BEFORE, DURING, DURING/AFTER, AFTER, UNKNOWN |
| 34 | --ENRF | End Relative to Reference Period | Char | Timing | Same values as --STRF |
| 35 | --EVLINT | Evaluation Interval | Char | Timing | ISO 8601 duration or interval |
| 36 | --EVINTX | Evaluation Interval Text | Char | Timing | Text description when interval cannot be represented in ISO 8601 |
| 37 | --STRTPT | Start Relative to Reference Time Point | Char | Timing | BEFORE, COINCIDENT, AFTER, UNKNOWN |
| 38 | --STTPT | Start Reference Time Point | Char | Timing | Text description of start anchor |
| 39 | --ENRTPT | End Relative to Reference Time Point | Char | Timing | BEFORE, COINCIDENT, AFTER, ONGOING, UNKNOWN |
| 40 | --ENTPT | End Reference Time Point | Char | Timing | Text description of end anchor |

### Disease Milestone Variables

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 41 | MIDS | Disease Milestone Instance Name | Char | Timing | Unique name of a disease milestone instance |
| 42 | RELMIDS | Temporal Relation to Milestone Instance | Char | Timing | How observation relates to MIDS |
| 43 | MIDSDTC | Disease Milestone Instance Date/Time | Char | Timing | Date/time of the disease milestone |

### Assessment Interval and Other Timing Variables

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 44 | --STINT | Planned Start of Assessment Interval | Char | Timing | ISO 8601 duration |
| 45 | --ENINT | Planned End of Assessment Interval | Char | Timing | ISO 8601 duration |
| 46 | --DETECT | Time in Days to Detection | Num | Timing | Not in human clinical trials |
| 47 | --PTFL | Point in Time Flag | Char | Timing | Only in Findings class specimen-based domains: BS, CP, GF, IS, LB, MB, MS, MI, PC, PP |
| 48 | --PDUR | Planned Duration | Char | Timing | Only in Findings class specimen-based domains: BS, CP, GF, IS, LB, MB, MS, MI, PC, PP |
