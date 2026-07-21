# SDTMIG v3.4 --- Domain Models: Interventions — Part 2

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 2/2 — 6.1.4-6.1.6: ML, PR, SU
> **Original:** `SDTMIG34_04_DomainModels_Interventions.md`
> **Related:** `SDTMIG34_04a_DomainModels_Interventions.md`

---

### 6.1.4 Meal Data (ML)

**ML -- Description/Overview**

An interventions domain that contains information describing a subject's food product consumption.

**ML -- Specification**

ml.xpt, Meal Data -- Interventions. One record per food product occurrence or constant intake interval per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | ML | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| MLSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| MLGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| MLSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. Examples: a number preprinted on the CRF as an explicit line identifier, record identifier defined in the sponsor's operational database. | Perm |
| MLTRT | Name of Meal | Char | \* | Topic | Verbatim food product name that is either preprinted or collected on a CRF. | Req |
| MLCAT | Category for Meal | Char | \* | Grouping Qualifier | Used to define a category of MLTRT values. | Perm |
| MLSCAT | Subcategory for Meal | Char | \* | Grouping Qualifier | Used to define a further categorization of MLCAT values. | Perm |
| MLPRESP | ML Pre-specified | Char | (NY) | Variable Qualifier | Used when a specific meal is prespecified on a CRF. Values should be "Y" or null. | Perm |
| MLOCCUR | ML Occurrence | Char | (NY) | Record Qualifier | Used to record whether a prespecified meal occurred when information about the occurrence of a specific meal is solicited. | Perm |
| MLSTAT | Completion Status | Char | (ND) | Record Qualifier | Used to indicate when a question about the occurrence of a prespecified meal was not answered. Should be null or have a value of "NOT DONE". | Perm |
| MLREASND | Reason Meal Not Collected | Char | | Record Qualifier | Describes the reason a response to a question about the occurrence of a meal was not collected. Used in conjunction with MLSTAT when value is "NOT DONE". | Perm |
| MLDOSE | Dose | Num | | Record Qualifier | Amount of MLTRT consumed. Not populated when MLDOSTXT is populated. | Perm |
| MLDOSTXT | Dose Description | Char | | Record Qualifier | Amount description of MLTRT consumed, collected in text form. Not populated when MLDOSE is populated. Examples: "<1 per day", "200-400". | Perm |
| MLDOSU | Dose Units | Char | (UNIT) | Variable Qualifier | Units for MLDOSE, MLDOSTOT, or MLDOSTXT. | Perm |
| MLDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dosage form for MLTRT. Example: "BAR, CHEWABLE". | Perm |
| VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Perm |
| VISIT | Visit Name | Char | | Timing | Protocol-defined description of a clinical encounter. | Perm |
| VISITDY | Planned Study Day of Visit | Num | | Timing | Planned study day of VISIT. Should be an integer. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm for the element in which the meal started. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the start date/time of the meal. | Perm |
| MLDTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Collection date and time of the meal represented in ISO 8601 character format. | Perm |
| MLSTDTC | Start Date/Time of Meal | Char | ISO 8601 datetime or interval | Timing | Start date/time of the meal represented in ISO 8601 character format. | Perm |
| MLENDTC | End Date/Time of Meal | Char | ISO 8601 datetime or interval | Timing | End date/time of the meal represented in ISO 8601 character format. | Perm |
| MLDY | Study Day of Visit/Collection/Exam | Num | | Timing | Actual study day of the visit/collection expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. | Perm |
| MLSTDY | Study Day of Start of Meal | Num | | Timing | Actual study day of start of the meal expressed in integer days relative to sponsor-defined RFSTDTC in Demographics. | Perm |
| MLENDY | Study Day of End of Meal | Num | | Timing | Actual study day of end of the meal expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. | Perm |
| MLDUR | Duration of Meal | Char | ISO 8601 duration | Timing | Collected duration of the meal represented in ISO 8601 character format. Used only if collected on the CRF and not derived. | Perm |
| MLTPT | Planned Time Point Name | Char | | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. See MLTPTNUM and MLTPTREF. | Perm |
| MLTPTNUM | Planned Time Point Number | Num | | Timing | Numeric version of planned time point used in sorting. | Perm |
| MLELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration. | Perm |
| MLTPTREF | Time Point Reference | Char | | Timing | Description of the fixed reference point referred to by MLELTM, MLTPTNUM, and MLTPT. | Perm |
| MLRFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 datetime or interval | Timing | Date/time for a fixed reference time point defined by MLTPTREF in ISO 8601 character format. | Perm |
| MIDS | Disease Milestone Instance Name | Char | | Timing | The name of a specific instance of a disease milestone type (MIDSTYPE) described in the Trial Disease Milestones dataset. This should be unique within a subject. Used only in conjunction with RELMIDS and MIDSDTC. | Perm |
| RELMIDS | Temporal Relation to Milestone Instance | Char | | Timing | The temporal relationship of the observation to the disease milestone instance name in MIDS. Examples: "IMMEDIATELY BEFORE", "AT TIME OF", "AFTER". | Perm |
| MIDSDTC | Disease Milestone Instance Date/Time | Char | ISO 8601 datetime or interval | Timing | The start date/time of the disease milestone instance name in MIDS, in ISO 8601 format. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**ML -- Assumptions**

1. The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX), Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would be represented in other domains include:

   a. Investigational nutritional products (represented in EC/EX)

   b. Food or drink used to treat hypoglycemic events (represented in CM)

   c. Glucose given as part of a glucose tolerance test (represented in AG)

   d. Caffeinated drinks (represented in SU)

   The nutritional items represented in ML may be prospectively defined within a protocol, collected retrospectively as potential precipitants of clinical events, and/or to describe nutritional intake.

2. Additional timing variables

   a. Any additional timing variables may be added to this domain.

   b. Consumption of a food product is considered to occur over an interval of time (as opposed to a point in time). If start and end date/times are collected, they should be represented in MLSTDTC and MLENDTC, respectively. If only a start date/time is collected, it should not be copied to MLENDTC.

3. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the ML domain, but the following qualifiers would generally not be used: --MOOD, --LOT, --LOC, --LAT, --DIR, --PORTOT.

**ML -- Examples**

**Example 1**

This example shows meal data collected in an effort to understand the causes of 2 different kinds of events.

- Data was collected about the last meal before each hypoglycemic event
- Data was collected about the occurrence of prespecified foods prior to a suspected event of drug-induced liver injury (DILI).

Meal Log CRF -- Record the last type of meal/food consumption prior to the hypoglycemic event:

| Type | If Nutritional Drink, Volume (ounces) | Start Date | Start Time | Event ID |
|---|---|---|---|---|
| Snack (X) | | 2015 Jun 03 | 14:15 | CE001 |
| Nutritional drink (X) | 8 oz | 2015 Sep 03 | 8:30 | CE002 |
| Meal (X) | | 2015 Dec 31 | 19:00 | CE003 |

DILI Meal CRF -- If suspected DILI, did you consume any of the following in the past week?

| Type | Occurrence | If yes, Date |
|---|---|---|
| Wild mushrooms | Yes (X) | 2015 DEC 24 |
| Ackee fruit | No (X) | |
| Cycad seeds | No (X) | |

Note that in this example MLENDTC is null. Because no end date was collected, the meal was represented as a point-in-time event, as described in Assumption 2b.

Rows 1-3:
Show the last meal data for 3 hypoglycemic events.

Rows 4-6:
Show the meal data collected relative to the suspected DILI.

ml.xpt

| Row | STUDYID | DOMAIN | USUBJID | MLSEQ | MLTRT | MLCAT | MLPRESP | MLOCCUR | MLDOSE | MLDOSU | MLDTC | MLSTDTC | MLENDTC | MLEVLINT | RELMIDS | MIDS | MIDSDTC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | XYZ | ML | XYZ-001-001 | 1 | SNACK | HYPOGLYCEMIA EVALUATION | Y | Y | | | | 2015-06-03T14:15 | | | LAST MEAL PRIOR TO | HYPO1 | 2015-06-03T19:20 |
| 2 | XYZ | ML | XYZ-001-001 | 2 | NUTRITIONAL DRINK | HYPOGLYCEMIA EVALUATION | Y | Y | 8 | oz | | 2015-09-03T08:30 | | | LAST MEAL PRIOR TO | HYPO2 | 2015-09-03T17:00 |
| 3 | XYZ | ML | XYZ-001-001 | 3 | MEAL | HYPOGLYCEMIA EVALUATION | Y | Y | | | | 2015-12-31T19:00 | | | LAST MEAL PRIOR TO | HYPO3 | 2016-01-01T10:30 |
| 4 | XYZ | ML | XYZ-001-001 | 4 | WILD MUSHROOMS | DILI EVALUATION | Y | Y | | | 2015-12-27 | 2015-12-24 | | -P1W | | | |
| 5 | XYZ | ML | XYZ-001-001 | 5 | ACKEE FRUIT | DILI EVALUATION | Y | N | | | 2015-12-27 | | | -P1W | | | |
| 6 | XYZ | ML | XYZ-001-001 | 6 | CYCAD SEEDS | DILI EVALUATION | Y | N | | | 2015-12-27 | | | -P1W | | | |

**Example 2**

This example describes a study that examines the effect of physical modifications in a cafeteria on selection/consumption among school students.

| Group | Arms | Details |
|---|---|---|
| 1 | Control | Students received standard meals in a standard cafeteria environment. |
| 2 | Experimental: choice architecture | Students were exposed to modifications to the physical environment in the cafeteria to "nudge" students towards healthier choices. Physical modifications included: placing vegetables at the beginning of the lunch line; placing fruits in attractive bowls, trays lined with appealing fabric, and fruit options next to cash registers; promoting fruits and vegetables with prominently displayed signage and images; placing white milk selection more predominantly than chocolate milk. |

Food-card data was collected over a 7-month period by students receiving a school meal 1 day per week. Students who brought a lunch from home or those not eating lunch in the cafeteria on a study day were excluded.

The dataset below shows the food-card data collected for the first 3 weeks for a subject.

ml.xpt

| Row | STUDYID | DOMAIN | USUBJID | MLSEQ | MLTRT | VISITNUM | VISIT | MLSTDTC |
|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | ML | ABC123-001 | 1 | FRUIT ROLLUP | 1 | WEEK 1 | 2015-09-09 |
| 2 | ABC123 | ML | ABC123-001 | 2 | WHITE MILK | 1 | WEEK 1 | 2015-09-09 |
| 3 | ABC123 | ML | ABC123-001 | 3 | PEANUT BUTTER SANDWICH | 1 | WEEK 1 | 2015-09-09 |
| 4 | ABC123 | ML | ABC123-001 | 4 | BANANA | 2 | WEEK 2 | 2015-09-17 |
| 5 | ABC123 | ML | ABC123-001 | 5 | CHOCOLATE MILK | 2 | WEEK 2 | 2015-09-17 |
| 6 | ABC123 | ML | ABC123-001 | 6 | PIZZA | 2 | WEEK 2 | 2015-09-17 |
| 7 | ABC123 | ML | ABC123-001 | 7 | APPLE | 3 | WEEK 3 | 2015-09-22 |
| 8 | ABC123 | ML | ABC123-001 | 8 | WHITE MILK | 3 | WEEK 3 | 2015-09-22 |
| 9 | ABC123 | ML | ABC123-001 | 9 | SALAD | 3 | WEEK 3 | 2015-09-22 |

---

### 6.1.5 Procedures (PR)

**PR -- Description/Overview**

An interventions domain that contains interventional activity intended to have diagnostic, preventive, therapeutic, or palliative effects.

**PR -- Specification**

pr.xpt, Procedures -- Interventions. One record per recorded procedure per occurrence per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | PR | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| PRSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| PRGRPID | Group ID | Char | | Identifier | Used to link together a block of related records within a subject in a domain. | Perm |
| PRSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined identifier. Example: preprinted line identifier on a CRF, record identifier defined in the sponsor’s operational database. | Perm |
| PRLNKID | Link ID | Char | | Identifier | Used to facilitate identification of relationships between records. | Perm |
| PRLNKGRP | Link Group ID | Char | | Identifier | Used to facilitate identification of relationships between records. | Perm |
| PRTRT | Reported Name of Procedure | Char | | Topic | Name of procedure performed, either preprinted or collected on a CRF. | Req |
| PRDECOD | Standardized Procedure Name | Char | (PROCEDUR) | Synonym Qualifier | Standardized or dictionary-derived name of PRTRT. If the codelist "PROCEDUR" is not used, the sponsor is expected to provide the dictionary name and version used to map the terms in the external codelist element in the Define-XML document. If an intervention term does not have a decode value, then PRDECOD will be null. | Perm |
| PRCAT | Category | Char | \* | Grouping Qualifier | Used to define a category of procedure values. | Perm |
| PRSCAT | Subcategory | Char | \* | Grouping Qualifier | Used to define a further categorization of PRCAT values. | Perm |
| PRPRESP | Pre-specified | Char | (NY) | Variable Qualifier | Used when a specific procedure is pre-specified on a CRF. Values should be "Y" or null. | Perm |
| PROCCUR | Occurrence | Char | (NY) | Record Qualifier | Used to record whether a prespecified procedure occurred when information about the occurrence of a specific procedure is solicited. | Perm |
| PRINDC | Indication | Char | | Record Qualifier | Denotes the indication for the procedure (e.g., why the procedure was performed). | Perm |
| PRDOSE | Dose | Num | | Record Qualifier | Amount of PRTRT administered. Not populated when PRDOSTXT is populated. | Perm |
| PRDOSTXT | Dose Description | Char | | Record Qualifier | Dosing information collected in text form. Examples: "<1", "200-400". Not populated when PRDOSE is populated. | Perm |
| PRDOSU | Dose Units | Char | (UNIT) | Variable Qualifier | Units for PRDOSE, PRDOSTOT, or PRDOSTXT. | Perm |
| PRDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dose form for PRTRT. | Perm |
| PRDOSFRQ | Dosing Frequency per Interval | Char | (FREQ) | Record Qualifier | Usually expressed as the number of doses given per a specific interval. | Perm |
| PRDOSRGM | Intended Dose Regimen | Char | | Record Qualifier | Text description of the intended schedule or regimen for the procedure. | Perm |
| PRROUTE | Route of Administration | Char | (ROUTE) | Variable Qualifier | Route of administration for PRTRT. | Perm |
| PRLOC | Location of Procedure | Char | (LOC) | Record Qualifier | Anatomical location of a procedure. | Perm |
| PRLAT | Laterality | Char | (LAT) | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. | Perm |
| PRDIR | Directionality | Char | (DIR) | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. | Perm |
| PRPORTOT | Portion or Totality | Char | (PORTOT) | Variable Qualifier | Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, apportioning of. | Perm |
| VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Perm |
| VISIT | Visit Name | Char | | Timing | Protocol-defined description of a clinical encounter. | Perm |
| VISITDY | Planned Study Day of Visit | Num | | Timing | Planned study day of VISIT. Should be an integer. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the start date/time of the procedure. | Perm |
| PRSTDTC | Start Date/Time of Procedure | Char | ISO 8601 datetime or interval | Timing | Start date/time of the procedure represented in ISO 8601 character format. | Exp |
| PRENDTC | End Date/Time of Procedure | Char | ISO 8601 datetime or interval | Timing | End date/time of the procedure represented in ISO 8601 character format. | Perm |
| PRSTDY | Study Day of Start of Procedure | Num | | Timing | Study day of start of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. | Perm |
| PRENDY | Study Day of End of Procedure | Num | | Timing | Study day of end of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. | Perm |
| PRDUR | Duration of Procedure | Char | ISO 8601 duration | Timing | Collected duration of a procedure represented in ISO 8601 character format. Used only if collected on the CRF and not derived from start and end date/times. | Perm |
| PRTPT | Planned Time Point Name | Char | | Timing | Text description of time when a procedure should be performed. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PRTPTNUM and PRTPTREF. | Perm |
| PRTPTNUM | Planned Time Point Number | Num | | Timing | Numerical version of planned time point used in sorting. | Perm |
| PRELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time in ISO 8601 format relative to a planned fixed reference (PRTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. | Perm |
| PRTPTREF | Time Point Reference | Char | | Timing | Description of the fixed reference point referred to by PRELTM, PRTPTNUM, and PRTPT. | Perm |
| PRRFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 datetime or interval | Timing | Date/time for a fixed reference time point defined by PRTRTREF in ISO 8601 character format. | Perm |
| PRSTRTPT | Start Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable PRSTTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| PRSTTPT | Start Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRSTRTPT. Examples: "2003-12-15", "VISIT 1". | Perm |
| PRENRTPT | End Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable PRENTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| PRENTPT | End Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRENRTPT. Examples: "2003-12-25", "VISIT 2". | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**PR -- Assumptions**

1. Some examples of procedures, by type, include the following:

   a. Disease screening (e.g., mammogram, pap smear)

   b. Endoscopic examinations (e.g., arthroscopy, diagnostic colonoscopy, therapeutic colonoscopy, diagnostic laparoscopy, therapeutic laparoscopy)

   c. Diagnostic tests (e.g., amniocentesis, biopsy, catheterization, cutaneous oximetry, finger stick, fluorophotometry, imaging techniques (e.g., DXA scan, CT scan, MRI), phlebotomy, pulmonary function test, skin test, stress test, tympanometry)

   d. Therapeutic procedures (e.g., ablation therapy, catheterization, cryotherapy, mechanical ventilation, phototherapy, radiation therapy/radiotherapy, thermotherapy)

   e. Surgical procedures (e.g., curative surgery, diagnostic surgery, palliative surgery, therapeutic surgery, prophylactic surgery, resection, stenting, hysterectomy, tubal ligation, implantation)

   The Procedures domain is based on the Interventions observation class. The extent of physiological effect may range from observable to microscopic. Regardless of the extent of effect or whether it is collected in the study, all collected procedures are represented in this domain. The protocol design should specify whether procedure information will be collected. Measurements obtained from procedures are to be represented in their respective Findings domain(s). For example, a biopsy may be performed to obtain a tissue sample that is then evaluated histopathologically. In this case, details of the biopsy procedure can be represented in the PR domain and the histopathology findings in the Microscopic Findings (MI) domain. Describing the relationship between PR and MI records (in RELREC) in this example is dependent on whether the relationship is collected, either explicitly or implicitly.

2. In the Findings Observation Class, the test method is represented in the --METHOD variable (e.g., electrophoresis, gram stain, polymerase chain reaction). At times, the test method overlaps with diagnostic/therapeutic procedures (e.g., ultrasound, MRI, x-ray) in-scope for the PR domain. The following is recommended: If timing (start, end or duration) or an indicator populating PROCCUR, PRSTAT, or PRREASND is collected, then a PR record should be created. If only the findings from a procedure are collected, then --METHOD in the Findings domain(s) may be sufficient to reflect the procedure and a related PR record is optional. It is at the sponsor’s discretion whether to represent the procedure as both a test method (--METHOD) and related PR record.

3. PRINDC is used to represent a medical indication, a medical condition which makes a treatment advisable. The reason for a procedure may be something other than a medical indication. For example, an x-ray might be taken to determine whether a fracture was present. Reasons other than medical indications should be represented using the supplemental qualifier PRREAS (see Appendix C1, Supplemental Qualifiers Name Codes).

4. Any identifier variables, timing variables, or interventions general observation-class qualifiers may be added to the PR domain, but the following qualifiers would generally not be used: --MOOD, --LOT.

**PR -- Examples**

**Example 1**

A procedures log CRF may collect verbatim values (procedure names) and dates performed. This example shows a subject who had 5 procedures collected and represented in the PR domain. In this study, the sponsor chose to consider verbatim text in PRTRT as long text represented in mixed case. See Section 4.2.4, Text Case in Submitted Data.

pr.xpt

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRTRT | PRSTDTC | PRENDTC |
|---|---|---|---|---|---|---|---|
| 1 | XYZ | PR | XYZ789-002 | 1 | Wisdom Teeth Extraction | 2010-06-08 | 2010-06-08 |
| 2 | XYZ | PR | XYZ789-002 | 2 | Reset Broken Arm | 2010-08-06 | 2010-08-06 |
| 3 | XYZ | PR | XYZ789-002 | 3 | Prostate Examination | 2010-12-12 | 2010-12-12 |
| 4 | XYZ | PR | XYZ789-002 | 4 | Endoscopy | 2010-12-12 | 2010-12-12 |
| 5 | XYZ | PR | XYZ789-002 | 5 | Heart Transplant | 2011-08-29 | 2011-08-29 |

**Example 2**

This example shows data from a 24-hour Holter monitor, an ambulatory electrocardiography device that records a continuous electrocardiographic rhythm pattern.

The start and end of the Holter monitoring procedure are represented in the PR domain.

pr.xpt

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRLNKID | PRTRT | PRDECOD | PRPRESP | PROCCUR | PRSTDTC | PRENDTC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | PR | ABC123-001 | 1 | 20110101_20110102 | 24-HOUR HOLTER MONITOR | HOLTER CONTINUOUS ECG RECORDING | Y | Y | 2011-01-01T08:00 | 2011-01-02T09:45 |

The heart rate findings from the procedure are represented in the ECG Test Results (EG) domain.

eg.xpt

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGLNKID | EGTESTCD | EGTEST | EGORRES | EGORRESU | EGMETHOD | EGDTC | EGENDTC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | EG | ABC123-001 | 1 | 20110101_20110102 | EGHRMIN | ECG Minimum Heart Rate | 70 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |
| 2 | ABC123 | EG | ABC123-001 | 2 | 20110101_20110102 | EGHRMAX | ECG Maximum Heart Rate | 100 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |
| 3 | ABC123 | EG | ABC123-001 | 3 | 20110101_20110102 | EGHRMEAN | ECG Mean Heart Rate | 75 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |

The relrec.xpt reflects a one-to-many dataset-level relationship between PR and EG using --LNKID.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|---|
| 1 | ABC123 | PR | | PRLNKID | | ONE | 1 |
| 2 | ABC123 | EG | | EGLNKID | | MANY | 1 |

**Example 3**

This example shows data for 3 subjects who had on-study radiotherapy. Dose, dose unit, location, and timing are represented. In this study, the sponsor chose to consider verbatim text in PRTRT as long text represented in mixed case. See Section 4.2.4, Text Case in Submitted Data.

pr.xpt

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRTRT | PRDOSE | PRDOSU | PRLOC | PRLAT | PRSTDTC | PRENDTC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | PR | ABC123-1001 | 1 | External beam radiation therapy | 70 | Gy | BREAST | RIGHT | 2011-06-01 | 2011-06-25 |
| 2 | ABC123 | PR | ABC123-2002 | 1 | Brachytherapy | 25 | Gy | PROSTATE | | 2011-07-15 | 2011-07-15 |
| 3 | ABC123 | PR | ABC123-3003 | 1 | Radiotherapy | 300 | cGy | BONE | | 2011-08-19 | 2011-08-22 |

---

### 6.1.6 Substance Use (SU)

**SU -- Description/Overview**

An interventions domain that contains substance use information that may be used to assess the efficacy and/or safety of therapies that look to mitigate the effects of chronic substance use.

**SU -- Specification**

su.xpt, Substance Use -- Interventions. One record per substance type per reported occurrence per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | SU | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| SUSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| SUGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| SUSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor’s operational database. Example: Line number on a Tobacco & Alcohol Use CRF page. | Perm |
| SUTRT | Reported Name of Substance | Char | | Topic | Substance name. Examples: “CIGARETTES”, “COFFEE”. | Req |
| SUMODIFY | Modified Substance Name | Char | | Synonym Qualifier | If SUTRT is modified, then the modified text is placed here. | Perm |
| SUDECOD | Standardized Substance Name | Char | \* | Synonym Qualifier | Standardized or dictionary-derived text description of SUTRT or SUMODIFY if the sponsor chooses to code the substance use. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. | Perm |
| SUCAT | Category for Substance Use | Char | \* | Grouping Qualifier | Used to define a category of related records. Examples: “TOBACCO”, “ALCOHOL”, or “CAFFEINE”. | Perm |
| SUSCAT | Subcategory for Substance Use | Char | \* | Grouping Qualifier | A further categorization of substance use. Examples: “CIGARS”, “CIGARETTES”, “BEER”, “WINE”. | Perm |
| SUPRESP | SU Pre-Specified | Char | (NY) | Variable Qualifier | Used to indicate whether (“Y”/null) information about the use of a specific substance was solicited on the CRF. | Perm |
| SUOCCUR | SU Occurrence | Char | (NY) | Record Qualifier | When the use of specific substances is solicited, SUOCCUR is used to indicate whether (“Y”/”N”) a particular prespecified substance was used. Values are null for substances not specifically solicited. | Perm |
| SUSTAT | Completion Status | Char | (ND) | Record Qualifier | When the use of prespecified substances is solicited, the completion status indicates that there was no response to the question about the prespecified substance. When there is no prespecified list on the CRF, then the completion status indicates that substance use was not assessed for the subject. | Perm |
| SUREASND | Reason Substance Use Not Collected | Char | | Record Qualifier | Describes the reason substance use was not collected. Used in conjunction with SUSTAT when value of SUSTAT is “NOT DONE”. | Perm |
| SUCLAS | Substance Use Class | Char | \* | Variable Qualifier | Substance use class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit SUCLAS. | Perm |
| SUCLASCD | Substance Use Class Code | Char | \* | Variable Qualifier | Code corresponding to SUCLAS. May be obtained from coding. | Perm |
| SUDOSE | Substance Use Consumption | Num | | Record Qualifier | Amount of SUTRT consumed. Not populated if SUDOSTXT is populated. | Perm |
| SUDOSTXT | Substance Use Consumption Text | Char | | Record Qualifier | Substance use consumption amounts or a range of consumption information collected in text form. Not populated if SUDOSE is populated. | Perm |
| SUDOSU | Consumption Units | Char | (UNIT) | Variable Qualifier | Units for SUDOSE, SUDOSTOT, or SUDOSTXT. Examples: “oz”, “CIGARETTE”, “PACK”, “g”. | Perm |
| SUDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dose form for SUTRT. Examples: “INJECTABLE”, “LIQUID”, “POWDER”. | Perm |
| SUDOSFRQ | Use Frequency Per Interval | Char | (FREQ) | Variable Qualifier | Usually expressed as the number of repeated administrations of SUDOSE within a specific time period. Example: “Q24H” (every day). | Perm |
| SUDOSTOT | Total Daily Consumption | Num | | Record Qualifier | Total daily use of SUTRT using the units in SUDOSU. Used when dosing is collected as total daily dose. If a sponsor needs to aggregate the data over a period other than daily, then the aggregated total could be recorded in a supplemental qualifier variable. | Perm |
| SUROUTE | Route of Administration | Char | (ROUTE) | Variable Qualifier | Route of administration for SUTRT. Examples: “ORAL”, “INTRAVENOUS”. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm for the element in which the substance use started. Null for substances that started before study participation. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the start date/time of the substance use. Null for substances that started before study participation. | Perm |
| SUSTDTC | Start Date/Time of Substance Use | Char | ISO 8601 datetime or interval | Timing | Start date/time of the substance use represented in ISO 8601 character format. | Perm |
| SUENDTC | End Date/Time of Substance Use | Char | ISO 8601 datetime or interval | Timing | End date/time of the substance use represented in ISO 8601 character format. | Perm |
| SUSTDY | Study Day of Start of Substance Use | Num | | Timing | Study day of start of substance use relative to the sponsor-defined RFSTDTC. | Perm |
| SUENDY | Study Day of End of Substance Use | Num | | Timing | Study day of end of substance use relative to the sponsor-defined RFSTDTC. | Perm |
| SUDUR | Duration of Substance Use | Char | ISO 8601 duration | Timing | Collected duration of substance use in ISO 8601 format. Used only if collected on the CRF and not derived from start and end date/times. | Perm |
| SUSTRF | Start Relative to Reference Period | Char | (STENRF) | Timing | Describes the start of the substance use relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as “PRIOR” was collected, this information may be translated into SUSTRF. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| SUENRF | End Relative to Reference Period | Char | (STENRF) | Timing | Describes the end of the substance use with relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as “PRIOR”, “ONGOING”, or “CONTINUING” was collected, this information may be translated into SUENRF. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| SUSTRTPT | Start Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the start of the substance as being before or after the reference time point defined by variable SUSTTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| SUSTTPT | Start Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by SUSTRTPT. Examples: “2003-12-15”, “VISIT 1”. | Perm |
| SUENRTPT | End Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the end of the substance as being before or after the reference time point defined by variable SUENTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| SUENTPT | End Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by SUENRTPT. Examples: “2003-12-25”, “VISIT 2”. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**SU -- Assumptions**

1. Substance use information may be independent of planned study evaluations, or may be a key outcome (e.g., planned evaluation) of a clinical trial.

   a. In many clinical trials, detailed substance use information as provided for in the domain model above may not be required (e.g., the only information collected may be a response to the question “Have you ever smoked tobacco?”); in such cases, many of the qualifier variables would not be submitted.

   b. SU may contain responses to questions about use of prespecified substances as well as records of substance use collected as free text.

2. SU description and coding

   a. SUTRT captures the verbatim or the prespecified text collected for the substance. It is the topic variable for the SU dataset. SUTRT is a required variable and must have a value.

   b. SUMODIFY is a permissible variable and should be included if coding is performed and the sponsor’s procedure permits modification of a verbatim substance use term for coding. The modified term is listed in SUMODIFY. The variable may be populated as per the sponsor’s procedures.

   c. SUDECOD is the preferred term derived by the sponsor from the coding dictionary if coding is performed. It is a permissible variable. Where deemed necessary by the sponsor, the verbatim term (SUTRT) should be coded using a standard dictionary such as WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

3. Additional categorization and grouping

   a. SUCAT and SUSCAT should not be redundant with the domain code or dictionary classification provided by SUDECOD, or with SUTRT. That is, they should provide a different means of defining or classifying SU records. For example, a sponsor may be interested in identifying all substances that the investigator feels might represent opium use, and to collect such use on a separate CRF page. This categorization might differ from the categorization derived from the coding dictionary.

   b. SUGRPID may be used to link (or associate) different records together to form a block of related records within SU at the subject level (see Section 4.2.6, Grouping Variables and Categorization). It should not be used in place of SUCAT or SUSCAT.

4. Timing variables

   a. SUSTDTC and SUENDTC may be populated as required.

   b. If substance use information is collected more than once within the CRF (indicating that the data are visit-based) then VISITNUM would be added to the domain as an additional timing variable. VISITDY and VISIT would then be permissible variables.

5. Any additional qualifiers from the Interventions class may be added to the SU domain, but the following qualifiers would generally not be used: --MOOD, --LOT.

**SU -- Examples**

**Example 1**

This example illustrates how typical SU data could be populated. Here, the CRF collected:

- Smoking data
  - Smoking status of “previous”, “current”, or “never”
  - If a current or past smoker, number of packs per day
  - If a former smoker, the year the subject quit
- Current caffeine use
  - What caffeine drinks subjects consumed today
  - How many cups today

SUCAT allows the records to be grouped into smoking-related data and caffeine-related data. In this example, the treatments are prespecified on the CRF page, so SUTRT does not require a standardized SUDECOD equivalent.

Not shown: A subject who never smoked does not have a tobacco record. Alternatively, a row for the subject could have been included with SUOCCUR = “N” and null dosing and timing fields; the interpretation would be the same. A subject who did not drink any caffeinated drinks on the day of the assessment does not have any caffeine records. A subject who never smoked and did not drink caffeinated drinks on the day of the assessment does not appear in the dataset.

Row 1:
Subject 1234005 is a 2-pack/day current smoker. “Current” implies that smoking started sometime before the time the question was asked (SUSTTPT = “2006-01-01”, SUSTRTPT = “BEFORE”) and had not ended as of that date (SUENTPT = “2006-01-01”, SUENRTPT = “ONGOING”). See Section 4.4.7, Use of Relative Timing Variables for the use of these variables. Both the beginning and ending reference time points for this question are the date of the assessment.

Row 2:
Subject 1234005 drank 3 cups of coffee on the day of the assessment.

Row 3:
Subject 1234006 is a former smoker. The date this subject began smoking is unknown, but it was sometime before the assessment date; this is shown by the values of SUSTTPT and SUSTRTPT. The end date of smoking was collected, so SUENTPT and SUENRTPT are not populated. Instead, the end date is in SUENDTC.

Row 4:
Subject 1234006 drank tea on the day of the assessment.

Row 5:
Subject 1234006 drank coffee on the day of the assessment.

Row 6:
Subject 1234007 had missing data for the smoking questions; this is indicated by SUSTAT = “NOT DONE”. The reason is in SUREASND.

Row 7:
Subject 1234007 also had missing data for all of the caffeine questions.

su.xpt

| Row | STUDYID | DOMAIN | USUBJID | SUSEQ | SUTRT | SUCAT | SUSTAT | SUREASND | SUDOSE | SUDOSU | SUDOSFRQ | SUSTDTC | SUENDTC | SUSTTPT | SUSTRTPT | SUENTPT | SUENRTPT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | 2 | PACK | QD | | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
| 2 | 1234 | SU | 1234005 | 2 | COFFEE | CAFFEINE | | | 3 | CUP | QD | 2006-01-01 | 2006-01-01 | | | | |
| 3 | 1234 | SU | 1234006 | 1 | CIGARETTES | TOBACCO | | | 1 | PACK | QD | | 2003 | 2006-03-15 | BEFORE | | |
| 4 | 1234 | SU | 1234006 | 2 | TEA | CAFFEINE | | | 1 | CUP | QD | 2006-03-15 | 2006-03-15 | | | | |
| 5 | 1234 | SU | 1234006 | 3 | COFFEE | CAFFEINE | | | 2 | CUP | QD | 2006-03-15 | 2006-03-15 | | | | |
| 6 | 1234 | SU | 1234007 | 1 | CIGARETTES | TOBACCO | NOT DONE | Subject left office before CRF was completed | | | | | | | | | |
| 7 | 1234 | SU | 1234007 | 2 | CAFFEINE | CAFFEINE | NOT DONE | Subject left office before CRF was completed | | | | | | | | | |
