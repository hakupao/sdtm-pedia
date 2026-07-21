# SDTMIG v3.4 --- Domain Models: Interventions — Part 1

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 1/2 — 6.1.1-6.1.3: AG, CM, Exposure (EX/EC)
> **Original:** `SDTMIG34_04_DomainModels_Interventions.md`
> **Related:** `SDTMIG34_04b_DomainModels_Interventions.md`

---

## 6 Domain Models Based on the General Observation Classes

### 6.1 Models for Interventions Domains

Most subject-level observations collected during the study should be represented according to one of the 3 SDTM general observation classes. The domains in the Interventions class include:

### 6.1.1 Procedure Agents (AG)

**AG -- Description/Overview**

An interventions domain that contains the agents administered to the subject as part of a procedure or assessment, as opposed to drugs, medications and therapies administered with therapeutic intent.

**AG -- Specification**

ag.xpt, Procedure Agents -- Interventions. One record per recorded intervention occurrence per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | AG | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| AGSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| AGGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| AGSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the procedure or test page. | Perm |
| AGLNKID | Link ID | Char | | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. | Perm |
| AGLNKGRP | Link Group ID | Char | | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. | Perm |
| AGTRT | Reported Agent Name | Char | | Topic | Verbatim medication name that is either preprinted or collected on a CRF. | Req |
| AGMODIFY | Modified Reported Name | Char | | Synonym Qualifier | If AGTRT is modified to facilitate coding, then AGMODIFY will contain the modified text. | Perm |
| AGDECOD | Standardized Agent Name | Char | \* | Synonym Qualifier | Standardized or dictionary-derived text description of AGTRT or AGMODIFY. Equivalent to the generic medication name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then AGDECOD will be left blank. | Perm |
| AGCAT | Category for Agent | Char | \* | Grouping Qualifier | Used to define a category of agent. Examples: "CHALLENGE AGENT", "PET TRACER". | Perm |
| AGSCAT | Subcategory for Agent | Char | \* | Grouping Qualifier | Further categorization of agent. | Perm |
| AGPRESP | AG Pre-Specified | Char | (NY) | Variable Qualifier | Used to indicate whether ("Y"/null) information about the use of a specific agent was solicited on the CRF. | Perm |
| AGOCCUR | AG Occurrence | Char | (NY) | Record Qualifier | When the use of specific agent is solicited, AGOCCUR is used to indicate whether ("Y"/"N") use of the agent occurred. Values are null for agents not specifically solicited. | Perm |
| AGSTAT | Completion Status | Char | (ND) | Record Qualifier | Used to indicate that a question about a prespecified agent was not answered. Should be null or have a value of "NOT DONE". | Perm |
| AGREASND | Reason Procedure Agent Not Collected | Char | | Record Qualifier | Describes the reason a response to a question about the occurrence of a procedure agent was not collected. Used in conjunction with AGSTAT when value is "NOT DONE". | Perm |
| AGCLAS | Agent Class | Char | \* | Variable Qualifier | Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLAS. | Perm |
| AGCLASCD | Agent Class Code | Char | \* | Variable Qualifier | Class code corresponding to AGCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLASCD. | Perm |
| AGDOSE | Dose per Administration | Num | | Record Qualifier | Amount of AGTRT taken. | Perm |
| AGDOSTXT | Dose Description | Char | | Record Qualifier | Dosing amounts or a range of dosing information collected in text form. Units may be stored in AGDOSU. Examples: "200-400", "15-20". | Perm |
| AGDOSU | Dose Units | Char | (UNIT) | Variable Qualifier | Units for AGDOSE and AGDOSTXT. Examples: "ng", "mg", "mg/kg". | Perm |
| AGDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dose form for AGTRT. Examples: "TABLET", "AEROSOL". | Perm |
| AGDOSFRQ | Dosing Frequency per Interval | Char | (FREQ) | Record Qualifier | Usually expressed as the number of repeated administrations of AGDOSE within a specific time period. Example: "ONCE". | Perm |
| AGROUTE | Route of Administration | Char | (ROUTE) | Variable Qualifier | Route of administration for AGTRT. Example: "ORAL". | Perm |
| VISITNUM | Visit Number | Num | | Timing | 1. Clinical encounter number. 2. Numeric version of VISIT, used for sorting. | Exp |
| VISIT | Visit Name | Char | | Timing | 1. Protocol-defined description of clinical encounter. 2. May be used in addition to VISITNUM and/or VISITDY. | Perm |
| VISITDY | Planned Study Day of Visit | Num | | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm for the element in which the agent administration started. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the start date/time of the agent administration started. | Perm |
| AGSTDTC | Start Date/Time of Agent | Char | ISO 8601 datetime or interval | Timing | The date/time when administration of the treatment indicated by AGTRT and the dosing variables began. | Perm |
| AGENDTC | End Date/Time of Agent | Char | ISO 8601 datetime or interval | Timing | The date/time when administration of the treatment indicated by AGTRT and the dosing variables ended. | Perm |
| AGSTDY | Study Day of Start of Agent | Num | | Timing | Study day of start of agent relative to the sponsor-defined RFSTDTC. | Perm |
| AGENDY | Study Day of End of Agent | Num | | Timing | Study day of end of agent relative to the sponsor-defined RFSTDTC. | Perm |
| AGDUR | Duration of Agent | Char | ISO 8601 duration | Timing | Collected duration for an agent episode. Used only if collected on the CRF and not derived from start and end date/times. | Perm |
| AGSTRF | Start Relative to Reference Period | Char | (STENRF) | Timing | Describes the start of the agent relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGSTRF. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| AGENRF | End Relative to Reference Period | Char | (STENRF) | Timing | Describes the end of the agent relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGENRF. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| AGSTRTPT | Start Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the start of the agent as being before or after the sponsor-defined reference time point defined by variable AGSTTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| AGSTTPT | Start Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by AGSTRTPT. Examples: "2003-12-15", "VISIT 1". | Perm |
| AGENRTPT | End Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the end of the agent as being before or after the reference time point defined by variable AGENTPT. Identifies the end of the agent as being before or after the sponsor-defined reference time point defined by variable AGENTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| AGENTPT | End Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by AGENRTPT. Examples: "2003-12-25", "VISIT 2". | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**AG -- Assumptions**

1. Purpose of the domain: Some tests involve administration of substances, and it has been unclear in which domain these should be represented.

   a. The Concomitant/Prior Medications (CM) domain seemed particularly inappropriate when the substance was one that would never be given as a medication. Even substances that are medications are not being used as such when they are given as part of a testing procedure.

   b. The Exposure (EX) domain also seemed inappropriate; although the testing procedure might be part of the study plan, these data would not be used or analyzed in the same way as data about study treatments. The AG domain was created to fill this gap.

   c. The AG domain has advantages over the Procedures (PR) domain for this purpose. It allows recording of multiple substance administrations for a single testing procedure. It also separates data about substance administrations from data about procedures that do not involve substance administration.

   d. Information about the conduct of the procedure with which the procedure agent administration was associated, if collected, should be represented in the PR domain.

2. Examples and structure

   a. Examples of agents administered as part of a procedure include a short-acting bronchodilator administered as part of a reversibility assessment and contrast agents or radio-labeled substances used in imaging studies.

   b. The structure of the AG domain is 1 record per agent intervention episode, or prespecified agent assessment per subject. It is the sponsor's responsibility to define an intervention episode. This definition may vary based on the sponsor's requirements for review and analysis.

3. AG description and coding

   a. AGTRT captures the name of the agent and it is the topic variable. It is a required variable and must have a value. AGTRT should include only the agent name, and should not include dosage, formulation, or other qualifying information. For example, "ALBUTEROL 2 PUFF" is not a valid value for AGTRT. This example should be expressed as AGTRT = "ALBUTEROL", AGDOSE = "2", AGDOSU = "PUFF", and AGDOSFRM = "AEROSOL".

   b. AGMODIFY should be included if the sponsor's procedure permits modification of a verbatim term for coding.

   c. AGDECOD is the standardized agent term derived by the sponsor from the coding dictionary. It is possible that the reported term (AGTRT) or the modified term (AGMODIFY) can be coded using a standard dictionary. In such cases, sponsors are expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

4. Prespecified terms; presence or absence of procedure agents

   a. AGPRESP is used to indicate whether an agent was prespecified.

   b. AGOCCUR is used to indicate whether a prespecified agent was used. A value of "Y" indicates that the agent was used and "N" indicates that it was not.

   c. If an agent was not prespecified, the value of AGOCCUR should be null. AGPRESP and AGOCCUR are permissible fields and may be omitted from the dataset if all agents were collected as free text. Values of AGOCCUR may also be null for prespecified agents if no Y/N response was collected; in this case, AGSTAT = "NOT DONE", and AGREASND could be used to describe the reason the answer was missing.

5. Any identifier variables, timing variables, or interventions general observation-class qualifiers may be added to the AG domain.

   a. However, --INDC, although allowed, would not generally be used because substance administrations represented in AG are given as part of a testing procedure rather than with therapeutic intent.

   b. The variables --DOSTOT and --DOSRGM, although allowed, would generally not be used because procedure agents are likely to be recorded at the level of single administrations.

**AG -- Examples**

**Example 1**

This example captures data about the allergen administered to the subject as part of a bronchial allergen challenge (BAC) test. Prior to the BAC, the subject had a skin-prick allergen test to help identify the allergen to be used for the BAC test. The skin-prick test identified grass as the allergen to be used in the BAC test.

Data from the allergen skin test are not shown, but the CRF for the BAC includes collection of the allergen chosen for use in the BAC. A predetermined set of ascending doses of the chosen allergen was used in the screening BAC test. The results of the screening BAC are not shown, but would be represented in the Respiratory System Findings (RE) domain.

Row 1:
The first dose given in the BAC was saline.

Rows 2-4:
Three successively higher doses of grass allergen were given.

ag.xpt

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGTRT | AGPRESP | AGOCCUR | AGDOSE | AGDOSU | AGROUTE | VISIT | AGENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | AG | XYZ-001-001 | 1 | SALINE | Y | Y | 0 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T10:56:00 |
| 2 | XYZ | AG | XYZ-001-001 | 2 | GRASS | Y | Y | 250 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T11:19:00 |
| 3 | XYZ | AG | XYZ-001-001 | 3 | GRASS | Y | Y | 1000 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T11:43:00 |
| 4 | XYZ | AG | XYZ-001-001 | 4 | GRASS | Y | Y | 2000 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T12:06:00 |

**Example 2**

In this example, first there was a check that the subject had not taken a short-acting bronchodilator in the previous 4 hours (Concomitant/Prior Medications (CM) domain). Then the procedure agent (AG domain) was given as part of a reversibility assessment. Spirometry measurements (RE domain) were obtained before and after agent administration. An identifier was assigned to the reversibility test and this identifier was used to link data across the multiple SDTM domains in which the data are represented.

The question as to whether a short-acting bronchodilator was administered in the 4 hours prior to the reversibility assessment is represented in the CM domain because this prior administration would have been for therapeutic effect, not as part of the procedure. The question asked was about the administration of any short-acting bronchodilator, rather than a specific medication, so both CMTRT and CMCAT are populated with "SHORT-ACTING BRONCHODILATOR", which describes a group of medications. The CMSPID value RV1 was used to indicate that this question was associated with the reversibility test.

cm.xpt

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMSPID | CMTRT | CMCAT | CMPRESP | CMOCCUR | CMEVLINT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | CM | XYZ-001-001 | 1 | RV1 | SHORT-ACTING BRONCHODILATOR | SHORT-ACTING BRONCHODILATOR | Y | N | -PT4H |

The administration of albuterol as part of the reversibility procedure is represented in the AG domain. The AGSPID value RV1 was used to indicate that this administration was associated with the reversibility test.

ag.xpt

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGSPID | AGTRT | AGPRESP | AGOCCUR | AGDOSE | AGDOSU | AGDOSFRM | AGDOSFRQ | AGROUTE | VISIT | AGSTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | AG | XYZ-001-001 | 1 | RV1 | ALBUTEROL | Y | Y | 2 | PUFF | AEROSOL | ONCE | RESPIRATORY (INHALATION) | VISIT 2 | 2013-06-18T10:05 |

The sponsor populated REGRPID with RV1 to indicate that these pulmonary function tests were associated with the reversibility test. The spirometer used in the testing is identified in SPDEVID. See the SDTMIG-MD for information about representing device-related information.

Row 1:
Shows the results for the pre-bronchodilator FEV1 test performed as part of a reversibility assessment. The timing reference variables RETPT, RETPTNUM, REELTM, RETPTREF, and RERFTDTC show that this test was performed 5 minutes before the bronchodilator challenge.

Row 2:
Shows the results for FEV1 test performed 20 minutes after the bronchodilator challenge.

Row 3:
Because the percentage reversibility was collected on the CRF, it is included in the SDTM dataset.

re.xpt

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | RESEQ | REGRPID | RETESTCD | RETEST | REORRES | REORRESU | RESTRESC | RESTRESN | RESTRESU | VISIT | REDTC | RETPT | RETPTNUM | REELTM | RETPTREF | RERFTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | RE | XYZ-001-001 | ABC001 | 1 | RV1 | FEV1 | Forced Expiratory Volume in 1 Second | 2.43 | L | 2.43 | 2.43 | L | VISIT 2 | 2013-06-18T10:00 | PRE-BRONCHODILATOR ADMINISTRATION | 1 | -PT5M | BRONCHODILATOR ADMINISTRATION | 2013-06-18T10:05 |
| 2 | XYZ | RE | XYZ-001-001 | ABC001 | 2 | RV1 | FEV1 | Forced Expiratory Volume in 1 Second | 2.77 | L | 2.77 | 2.77 | L | VISIT 2 | 2013-06-18T10:00 | POST-BRONCHODILATOR ADMINISTRATION | 2 | PT20M | BRONCHODILATOR ADMINISTRATION | 2013-06-18T10:05 |
| 3 | XYZ | RE | XYZ-001-001 | ABC001 | 3 | RV1 | PTCREV | Percentage Reversibility | 13.99 | % | 13.99 | 13.99 | % | VISIT 2 | 2013-06-18T10:00 | | | | BRONCHODILATOR ADMINISTRATION | 2013-06-18T10:05 |

The identifier for the device used in the test was established in the Device Identifier (DI) domain.

di.xpt

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | DI | ABC001 | 1 | TYPE | Device Type | SPIROMETER |

The relationship of the test agent to the spirometry measurements obtained before and after its administration and to the prior occurrence of short acting bronchodilator administration is recorded by means of a relationship in RELREC.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | AG | XYZ-001-001 | AGSPID | RV1 | | 1 |
| 2 | XYZ | RE | XYZ-001-001 | REGRPID | RV1 | | 1 |
| 3 | XYZ | CM | XYZ-001-001 | CMSPID | RV1 | | 1 |

---

### 6.1.2 Concomitant/Prior Medications (CM)

**CM -- Description/Overview**

An interventions domain that contains concomitant and prior medications used by the subject, such as those given on an as needed basis or condition-appropriate medications.

**CM -- Specification**

cm.xpt, Concomitant/Prior Medications -- Interventions. One record per recorded intervention occurrence or constant-dosing interval per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | CM | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| CMSEQ | Sequence Number | Num | | Identifier | Sequence number to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| CMGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| CMSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. Example: a number preprinted on the CRF as an explicit line identifier or record identifier defined in the sponsor’s operational database. Example: line number on a concomitant medication page. | Perm |
| CMTRT | Reported Name of Drug, Med, or Therapy | Char | | Topic | Verbatim medication name that is either preprinted or collected on a CRF. | Req |
| CMMODIFY | Modified Reported Name | Char | | Synonym Qualifier | If CMTRT is modified to facilitate coding, then CMMODIFY will contain the modified text. | Perm |
| CMDECOD | Standardized Medication Name | Char | | Synonym Qualifier | Standardized or dictionary-derived text description of CMTRT or CMMODIFY. Equivalent to the generic drug name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank. | Perm |
| CMCAT | Category for Medication | Char | | Grouping Qualifier | Used to define a category of medications/treatment. Examples: “PRIOR”, “CONCOMITANT”, “ANTI-CANCER MEDICATION”, “GENERAL CONMED”. | Perm |
| CMSCAT | Subcategory for Medication | Char | | Grouping Qualifier | A further categorization of medications/treatment. Examples: “CHEMOTHERAPY”, “HORMONAL THERAPY”, “ALTERNATIVE THERAPY”. | Perm |
| CMPRESP | CM Pre-specified | Char | (NY) | Variable Qualifier | Used to indicate whether (“Y”/null) information about the use of a specific medication was solicited on the CRF. | Perm |
| CMOCCUR | CM Occurrence | Char | (NY) | Record Qualifier | When the use of a specific medication is solicited. CMOCCUR is used to indicate whether (“Y”/”N”) use of the medication occurred. Values are null for medications not specifically solicited. | Perm |
| CMSTAT | Completion Status | Char | (ND) | Record Qualifier | Used to indicate that a question about the occurrence of a prespecified intervention was not answered. Should be null or have a value of “NOT DONE”. | Perm |
| CMREASND | Reason Medication Not Collected | Char | | Record Qualifier | Reason not done. Used in conjunction with CMSTAT when value is “NOT DONE”. | Perm |
| CMINDC | Indication | Char | | Record Qualifier | Denotes why a medication was taken or administered. Examples: “NAUSEA”, “HYPERTENSION”. | Perm |
| CMCLAS | Medication Class | Char | | Variable Qualifier | Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLAS. | Perm |
| CMCLASCD | Medication Class Code | Char | | Variable Qualifier | Class code corresponding to CMCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLASCD. | Perm |
| CMDOSE | Dose per Administration | Num | | Record Qualifier | Amount of CMTRT given. Not populated when CMDOSTXT is populated. | Perm |
| CMDOSTXT | Dose Description | Char | | Record Qualifier | Dosing amounts or a range of dosing information collected in text form. Units may be stored in CMDOSU. Examples: “200-400”, “15-20”. Not populated when CMDOSE is populated. | Perm |
| CMDOSU | Dose Units | Char | (UNIT) | Variable Qualifier | Units for CMDOSE, CMDOSTOT, or CMDOSTXT. Examples: “ng”, “mg”, “mg/kg”. | Perm |
| CMDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dose form for CMTRT. Examples: “TABLET”, “LOTION”. | Perm |
| CMDOSFRQ | Dosing Frequency per Interval | Char | (FREQ) | Record Qualifier | Usually expressed as the number of repeated administrations of CMDOSE within a specific time period. Examples: “BID” (twice daily), “Q12H” (every 12 hours). | Perm |
| CMDOSTOT | Total Daily Dose | Num | | Record Qualifier | Total daily dose of CMTRT using the units in CMDOSU. Used when dosing is collected as total daily dose. Total dose over a period other than day could be recorded in a separate supplemental qualifier variable. | Perm |
| CMDOSRGM | Intended Dose Regimen | Char | | Record Qualifier | Text description of the (intended) schedule or regimen for the Intervention. Example: “TWO WEEKS ON, TWO WEEKS OFF”. | Perm |
| CMROUTE | Route of Administration | Char | (ROUTE) | Variable Qualifier | Route of administration for the intervention. Examples: “ORAL”, “INTRAVENOUS”. | Perm |
| CMADJ | Reason for Dose Adjustment | Char | | Record Qualifier | Describes reason or explanation of why a dose is adjusted. Examples: “ADVERSE EVENT”, “INSUFFICIENT RESPONSE”, “NON-MEDICAL REASON”. | Perm |
| CMRSDISC | Reason the Intervention Was Discontinued | Char | | Record Qualifier | When dosing of a treatment is recorded over multiple successive records, this variable is applicable only for the (chronologically) last record for the treatment. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm for the element in which the medication administration started. Null for medications that started before study participation. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the start date/time of the medication administration. Null for medications that started before study participation. | Perm |
| CMSTDTC | Start Date/Time of Medication | Char | ISO 8601 datetime or interval | Timing | Start date/time of the medication administration represented in ISO 8601 character format. | Perm |
| CMENDTC | End Date/Time of Medication | Char | ISO 8601 datetime or interval | Timing | End date/time of the medication administration represented in ISO 8601 character format. | Perm |
| CMSTDY | Study Day of Start of Medication | Num | | Timing | Study day of start of medication relative to the sponsor-defined RFSTDTC. | Perm |
| CMENDY | Study Day of End of Medication | Num | | Timing | Study day of end of medication relative to the sponsor-defined RFSTDTC. | Perm |
| CMDUR | Duration | Char | ISO 8601 duration | Timing | Collected duration for a treatment episode. Used only if collected on the CRF and not derived from start and end date/times. | Perm |
| CMSTRF | Start Relative to Reference Period | Char | (STENRF) | Timing | Describes the start of the medication relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as “PRIOR” was collected, this information may be translated into CMSTRF. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| CMENRF | End Relative to Reference Period | Char | (STENRF) | Timing | Describes the end of the medication relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as “PRIOR”, “ONGOING, or “CONTINUING” was collected, this information may be translated into CMENRF. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| CMSTRTPT | Start Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the start of the medication as being before or after the sponsor-defined reference time point defined by variable CMSTTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| CMSTTPT | Start Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMSTRTPT. Examples: “2003-12-15”, “VISIT 1”. | Perm |
| CMENRTPT | End Relative to Reference Time Point | Char | (STENRF) | Timing | Identifies the end of the medication as being before or after the sponsor-defined reference time point defined by variable CMENTPT. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
| CMENTPT | End Reference Time Point | Char | | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMENRTPT. Examples: “2003-12-25”, “VISIT 2”. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**CM -- Assumptions**

1. The structure of the CM domain is 1 record per medication intervention episode, constant-dosing interval, or prespecified medication assessment per subject. It is the sponsor’s responsibility to define an intervention episode. This definition may vary based on the sponsor’s requirements for review and analysis. The submission dataset structure may differ from the structure used for collection. One common approach is to submit a new record when there is a change in the dosing regimen. Another approach is to collapse all records for a medication to a summary level with either a dose range or the highest dose level. Other approaches may also be reasonable as long as they meet the sponsor’s evaluation requirements.

2. CM description and coding

   a. CMTRT is the topic variable and captures the name of the concomitant medication/therapy or the prespecified term used to collect information about the occurrence of any of a group of medications and/or therapies. It is a required variable and must have a value. CMTRT only includes the medication/therapy name and does not include dosage, formulation, or other qualifying information. For example, “ASPIRIN 100MG TABLET” is not a valid value for CMTRT. This example should be expressed as CMTRT= “ASPIRIN”, CMDOSE= “100”, CMDOSU= “MG”, and CMDOSFRM= “TABLET”. When referring to a prespecified group of medications/therapies, CMTRT contains the description of the group used to solicit the occurrence response.

   b. CMMODIFY should be included if the sponsor’s procedure permits modification of a verbatim term for coding.

   c. CMDECOD is the standardized medication/therapy term derived by the sponsor from the coding dictionary. It is expected that the reported term (CMTRT) or the modified term (CMMODIFY) will be coded using a standard dictionary. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

   d. When CMDECOD values from the WHODrug Dictionary are longer than 200 characters, split the values at semicolons rather than spaces when implementing guidance in Section 4.5.3.2, Text Strings Greater than 200 Characters.

3. Prespecified terms; presence or absence of concomitant medications

   a. Information on concomitant medications is generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. Because the solicitation of information on specific concomitant medications may affect the frequency at which they are reported, the fact that a specific medication was solicited may be of interest to reviewers. CMPRESP and CMOCCUR are used together to indicate whether the intervention in CMTRT was prespecified and whether it occurred, respectively.

   b. CMOCCUR is used to indicate whether a prespecified medication was used. A value of “Y” indicates that the medication was used and “N” indicates that it was not.

   c. If a medication was not prespecified, the value of CMOCCUR should be null. CMPRESP and CMOCCUR are permissible fields and may be omitted from the dataset if all medications were collected as free text. Values of CMOCCUR may also be null for prespecified medications if no Y/N response was collected; in such cases, CMSTAT = “NOT DONE”, and CMREASND could be used to describe the reason the answer was missing.

4. Variables for timing relative to a time point

   a. CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = “2007-04-30” (the date the assessment was made) and CMENRTPT = “ONGOING”.

5. Although any identifier variables, timing variables, or interventions general observation-class qualifiers may be added to the CM domain, the following qualifiers would generally not be used: --MOOD, --LOT.

**CM -- Examples**

**Example 1**

Sponsors collect the timing of concomitant medication use with varying specificity, depending on the pattern of use; the type, purpose, and importance of the medication; and the needs of the study. It is often unnecessary to record every unique instance of medication use, since the same information can be conveyed with start and end dates and frequency of use. If appropriate, medications taken as needed (intermittently or sporadically over a time period) may be reported with a start and end date and a frequency of “PRN”.

The example below shows 3 subjects who took the same medication on the same day.

Rows 1-6:
For subject ABC-0001, each instance of aspirin use was recorded separately, and the frequency in each record is (CMDOSFRQ) is “ONCE”.

Rows 7-9:
For subject ABC-0002, frequency was once a day (“QD”) in the first and third records (where CMSEQ is “1” and “3”), but twice a day in the second record (CMSEQ = “2”).

Row 10:
Records for subject ABC-0003 are collapsed into a single entry that spans the relevant time period, with a frequency of “PRN”. This is shown as an example only, not as a recommendation. This approach assumes that knowing exactly when aspirin was used is not important for evaluating safety and efficacy in this study.

cm.xpt

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMDOSE | CMDOSU | CMDOSFRQ | CMSTDTC | CMENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | CM | ABC-0001 | 1 | ASPIRIN | 100 | mg | ONCE | 2004-01-01 | 2004-01-01 |
| 2 | ABC | CM | ABC-0001 | 2 | ASPIRIN | 100 | mg | ONCE | 2004-01-02 | 2004-01-02 |
| 3 | ABC | CM | ABC-0001 | 3 | ASPIRIN | 100 | mg | ONCE | 2004-01-03 | 2004-01-03 |
| 4 | ABC | CM | ABC-0001 | 4 | ASPIRIN | 100 | mg | ONCE | 2004-01-07 | 2004-01-07 |
| 5 | ABC | CM | ABC-0001 | 5 | ASPIRIN | 100 | mg | ONCE | 2004-01-07 | 2004-01-07 |
| 6 | ABC | CM | ABC-0001 | 6 | ASPIRIN | 100 | mg | ONCE | 2004-01-09 | 2004-01-09 |
| 7 | ABC | CM | ABC-0002 | 1 | ASPIRIN | 100 | mg | QD | 2004-01-01 | 2004-01-03 |
| 8 | ABC | CM | ABC-0002 | 2 | ASPIRIN | 100 | mg | BID | 2004-01-07 | 2004-01-07 |
| 9 | ABC | CM | ABC-0002 | 3 | ASPIRIN | 100 | mg | QD | 2004-01-09 | 2004-01-09 |
| 10 | ABC | CM | ABC-0003 | 1 | ASPIRIN | 100 | mg | PRN | 2004-01-01 | 2004-01-09 |

**Example 2**

In this example study, it was of particular interest whether subjects use any anticonvulsant medications. The medication history, dosing, and so on was not of interest; the study only asked for the anticonvulsants to which subjects were exposed.

cm.xpt

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMCAT |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | CM | 1 | 1 | LITHIUM | ANTI-CONVULSANT |
| 2 | ABC123 | CM | 2 | 1 | VPA | ANTI-CONVULSANT |

**Example 3**

Sponsors often are interested in whether subjects are exposed to specific concomitant medications, and collect this information using a checklist. This example is for a study that had a particular interest in the antidepressant medications that subjects used. For the study’s purposes, absence is just as important as presence of a medication. This can be clearly shown using CMOCCUR.

In this example, CMPRESP shows that the subjects were specifically asked if they use any of 3 antidepressants (Zoloft, Prozac, and Paxil). The value of CMOCCUR indicates the response to the prespecified medication question. CMSTAT indicates whether the response was missing for a prespecified medication, and CMREASND shows the reason for missing response. The medication details (e.g., dose, frequency) were not of interest in this study.

Row 1:
Medication use was solicited and the medication was taken.

Row 2:
Medication use was solicited and the medication was not taken.

Row 3:
Medication use was solicited, but data were not collected. The reason for the lack of a response was collected and is represented in CMREASND.

cm.xpt

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMPRESP | CMOCCUR | CMSTAT | CMREASND |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | CM | 1 | 1 | ZOLOFT | Y | Y | | |
| 2 | ABC123 | CM | 1 | 2 | PROZAC | Y | N | | |
| 3 | ABC123 | CM | 1 | 3 | PAXIL | Y | | NOT DONE | Didn’t ask due to interruption |

**Example 4**

In this hepatitis C study, collection of data on prior treatments included reason for discontinuation. Because hepatitis C is usually treated with a combination of medications, CMGRPID was used to group records into regimens.

Rows 1-3:
This subject’s treatment consisted of the 3 medications grouped by means of CMGRPID = “1”. The subject completed the scheduled treatment.

Rows 4-6:
Another subject received the same set of 3 medications. The medications for this subject are also grouped using CMGRPID = “1”. Note, however, that the fact that the same CMGRPID value has been used for the same set of medications for subjects “ABC123-765” and “ABC123-899” is coincidence; CMGRPID groups records only within a subject. This subject stopped the regimen due to side effects.

cm.xpt

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMGRPID | CMTRT | CMCAT | CMDOSFRM | CMROUTE | CMRSDISC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | CM | ABC123-765 | 1 | 1 | PEGINTRON | HCV TREATMENT | INJECTION | SUBCUTANEOUS | COMPLETED SCHEDULED TREATMENT |
| 2 | ABC123 | CM | ABC123-765 | 2 | 1 | RIBAVIRIN | HCV TREATMENT | TABLET | ORAL | COMPLETED SCHEDULED TREATMENT |
| 3 | ABC123 | CM | ABC123-765 | 3 | 1 | BOCEPREVIR | HCV TREATMENT | TABLET | ORAL | COMPLETED SCHEDULED TREATMENT |
| 4 | ABC123 | CM | ABC123-899 | 1 | 1 | PEGINTRON | HCV TREATMENT | INJECTION | SUBCUTANEOUS | TOXICITY/INTOLERANCE |
| 5 | ABC123 | CM | ABC123-899 | 2 | 1 | RIBAVIRIN | HCV TREATMENT | TABLET | ORAL | TOXICITY/INTOLERANCE |
| 6 | ABC123 | CM | ABC123-899 | 3 | 1 | BOCEPREVIR | HCV TREATMENT | TABLET | ORAL | TOXICITY/INTOLERANCE |

**Example 5**

In this rheumatoid arthritis (RA) study, the sponsor collected medications using the category “Prior RA Medications”, then collected information on whether the subject had received certain medication classes, represented as subcategories. If a subject did receive medications in a subcategory, information about those medications was collected. This example shows data for 2 subjects who received prior RA medications. It includes data only about their prior disease-modifying antirheumatic drugs (DMARDs); information about other kinds of prior RA medications is not included.

Row 1:
Shows that subject 101 received prior RA medications. The values of CMTRT and CMCAT are the same, indicating that this record represents the response to a question about a category of medications, rather than an individual medication.

Row 2:
Shows that subject 101 did not receive prior DMARDs. The values in CMTRT and CMSCAT are the same, indicating that this record represents the response to a question about a group of medications, rather than an individual medication.

Row 3:
Shows that subject 102 received prior RA medications.

Row 4:
Shows that subject 102 received prior DMARDs.

Rows 5-6:
Show 2 prior DMARDS received by subject 102, one ending before the date of data collection, and the other ongoing at that time. These medications were not prespecified, so CMPRESP is null.

cm.xpt

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMCAT | CMSCAT | CMPRESP | CMOCCUR | CMINDC | CMDTC | CMDY | CMENRTPT | CMENTPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | CM | 101 | 1 | PRIOR RA MEDICATIONS | PRIOR RA MEDICATIONS | | Y | Y | RHEUMATOID ARTHRITIS | 2020-02-02 | -1 | | |
| 2 | ABC123 | CM | 101 | 2 | PRIOR DMARDS | PRIOR RA MEDICATIONS | PRIOR DMARDS | Y | N | RHEUMATOID ARTHRITIS | 2020-02-02 | -1 | | |
| 3 | ABC123 | CM | 102 | 1 | PRIOR RA MEDICATIONS | PRIOR RA MEDICATIONS | | Y | Y | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | | |
| 4 | ABC123 | CM | 102 | 2 | PRIOR DMARDS | PRIOR RA MEDICATIONS | PRIOR DMARDS | Y | Y | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | | |
| 5 | ABC123 | CM | 102 | 3 | SULFASALAZINE | PRIOR RA MEDICATIONS | PRIOR DMARDS | | | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | BEFORE | 2020-01-25 |
| 6 | ABC123 | CM | 102 | 4 | METHOTREXATE | PRIOR RA MEDICATIONS | PRIOR DMARDS | | | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | ONGOING | 2020-01-25 |

---

### 6.1.3 Exposure Domains

Clinical trial study designs can range from open label (where subjects and investigators know which product each subject is receiving) to blinded (where the subject, investigator, or anyone assessing the outcome is unaware of the treatment assignment(s) to reduce potential for bias). To support standardization of various collection methods and details, as well as process differences between open-label and blinded studies, 2 SDTM domains based on the Interventions General Observation Class are available to represent details of subject exposure to protocol-specified study treatment(s): Exposure (EX) and Exposure as Collected (EC).

#### 6.1.3.1 Exposure (EX)

**EX -- Description/Overview**

An interventions domain that contains the details of a subject's exposure to protocol-specified study treatment. Study treatment may be any intervention that is prospectively defined as a test material within a study, and is typically but not always supplied to the subject.

**EX -- Specification**

ex.xpt, Exposure -- Interventions. One record per protocol-specified study treatment, constant-dosing interval, per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | EX | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| EXSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| EXGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| EXREFID | Reference ID | Char | | Identifier | Internal or external identifier (e.g., kit number, bottle label, vial identifier). | Perm |
| EXSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. | Perm |
| EXLNKID | Link ID | Char | | Identifier | Identifier used to link related records across domains. | Perm |
| EXLNKGRP | Link Group ID | Char | | Identifier | Identifier used to link related, grouped records across domains. | Perm |
| EXTRT | Name of Treatment | Char | \* | Topic | Name of the protocol-specified study treatment given during the dosing period for the observation. | Req |
| EXCAT | Category of Treatment | Char | \* | Grouping Qualifier | Used to define a category of EXTRT values. | Perm |
| EXSCAT | Subcategory of Treatment | Char | \* | Grouping Qualifier | A further categorization of EXCAT values. | Perm |
| EXDOSE | Dose | Num | | Record Qualifier | Amount of EXTRT when numeric. Not populated when EXDOSTXT is populated. | Exp |
| EXDOSTXT | Dose Description | Char | | Record Qualifier | Amount of EXTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when EXDOSE is populated. | Perm |
| EXDOSU | Dose Units | Char | (UNIT) | Variable Qualifier | Units for EXDOSE, EXDOSTOT, or EXDOSTXT representing protocol-specified values. Examples: "ng", "mg", "mg/kg", "mg/m2". | Exp |
| EXDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dose form for EXTRT. Examples: "TABLET", "LOTION". | Exp |
| EXDOSFRQ | Dosing Frequency per Interval | Char | (FREQ) | Record Qualifier | Usually expressed as the number of repeated administrations of EXDOSE within a specific time period. Examples: "Q2H", "QD", "BID". | Perm |
| EXDOSRGM | Intended Dose Regimen | Char | | Record Qualifier | Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF". | Perm |
| EXROUTE | Route of Administration | Char | (ROUTE) | Variable Qualifier | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". | Perm |
| EXLOT | Lot Number | Char | | Record Qualifier | Lot number of the intervention product. | Perm |
| EXLOC | Location of Dose Administration | Char | (LOC) | Record Qualifier | Specifies location of administration. Examples: "ARM", "LIP". | Perm |
| EXLAT | Laterality | Char | (LAT) | Variable Qualifier | Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT". | Perm |
| EXDIR | Directionality | Char | (DIR) | Variable Qualifier | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER". | Perm |
| EXFAST | Fasting Status | Char | (NY) | Record Qualifier | Indicator used to identify fasting status. Examples: "Y", "N". | Perm |
| EXADJ | Reason for Dose Adjustment | Char | \* | Record Qualifier | Describes reason or explanation of why a dose is adjusted. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Trial epoch of the exposure record. Examples: "RUN-IN", "TREATMENT". | Perm |
| EXSTDTC | Start Date/Time of Treatment | Char | ISO 8601 datetime or interval | Timing | The date/time when administration of the treatment indicated by EXTRT and EXDOSE began. | Exp |
| EXENDTC | End Date/Time of Treatment | Char | ISO 8601 datetime or interval | Timing | The date/time when administration of the treatment indicated by EXTRT and EXDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation. | Exp |
| EXSTDY | Study Day of Start of Treatment | Num | | Timing | Study day of EXSTDTC relative to DM.RFSTDTC. | Perm |
| EXENDY | Study Day of End of Treatment | Num | | Timing | Study day of EXENDTC relative to DM.RFSTDTC. | Perm |
| EXDUR | Duration of Treatment | Char | ISO 8601 duration | Timing | Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times. | Perm |
| EXTPT | Planned Time Point Name | Char | | Timing | Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EXTPTNUM and EXTPTREF. | Perm |
| EXTPTNUM | Planned Time Point Number | Num | | Timing | Numerical version of EXTPT to aid in sorting. | Perm |
| EXELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time relative to the planned fixed reference (EXTPTREF). This variable is useful where there are repetitive measures. Not a clock time. | Perm |
| EXTPTREF | Time Point Reference | Char | | Timing | Name of the fixed reference point referred to by EXELTM, EXTPTNUM, and EXTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL. | Perm |
| EXRFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 datetime or interval | Timing | Date/time for a fixed reference time point defined by EXTPTREF. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**EX -- Assumptions**

1. EX structure and use

   a. Examples of treatments represented in the EX domain include but are not limited to placebo, active comparators, and investigational products. Treatments that are not protocol-specified should be represented in the Concomitant/Prior Medications (CM) or another Interventions domain as appropriate.

   b. The EX domain is recognized in most cases as a derived dataset where EXDOSU reflects the protocol-specified unit per study treatment. Collected data points (e.g., number of tablets, total volume infused) along with additional inputs (e.g., randomization file, concentration, dosage strength, product accountability) are used to derive records in the EX domain.

   c. The EX domain is required for all studies that include protocol-specified study treatment. Exposure records may be directly or indirectly determined; metadata should describe how the records were derived. Common methods for determining exposure (from most direct to least direct) include the following:

      i. Derived from actual observation of the administration of drug by the investigator

      ii. Derived from automated dispensing device that records administrations

      iii. Derived from subject recall

      iv. Derived from product accountability data

      v. Derived from the protocol. When a study is still masked and protocol-specified study treatment doses cannot yet be reflected in the protocol-specified unit due to blinding requirements, then the EX domain is not expected to be populated.

   d. The EX domain should contain 1 record per constant-dosing interval per subject. Sponsors define the constant-dosing interval, which may include any period of time that can be described in terms of a known treatment given at a consistent dose, frequency, infusion rate, and so on. For example, for a study with once-a-week administration of a standard dose for 6 weeks, exposure may be represented as:

      i. a single record per subject, spanning the entire 6-week treatment phase, if information about each dose is not collected; or

      ii. up to 6 records (1 for each weekly administration), if the sponsor monitors each treatment administration.

2. Exposure treatment description

   a. EXTRT captures the name of the protocol-specified study treatment and is the topic variable. It is a required variable and must have a value. EXTRT must include only the treatment name and must not include dosage, formulation, or other qualifying information. For example, "ASPIRIN 100MG TABLET" is not a valid value for EXTRT. This example should be expressed as EXTRT = "ASPIRIN", EXDOSE = "100", EXDOSU = "mg", and EXDOSFRM = "TABLET".

   b. Doses of placebo should be represented by EXTRT = "PLACEBO" and EXDOSE = "0" (indicating 0 mg of active ingredient was taken or administered).

3. Categorization and grouping

   a. EXCAT and EXSCAT may be used when appropriate to categorize treatments into categories and subcategories. For example, if a study contains several active comparator medications, EXCAT may be set to "ACTIVE COMPARATOR". Such categorization may not be useful in all studies, so these variables are permissible.

4. Timing variables

   a. The timing of exposure to study treatment is captured by the start/end date and start/end time of each constant-dosing interval. If the subject is only exposed to study medication within a clinical encounter (e.g., if an injection is administered at the clinic), VISITNUM may be added to the domain as an additional timing variable. VISITDY and VISIT would then also be permissible qualifiers. However, if the beginning and end of a constant-dosing interval is not confined within the time limits of a clinical encounter (e.g., if a subject takes pills at home), then it is not appropriate to include VISITNUM in the EX domain. This is because EX is designed to capture the timing of exposure to treatment, not the timing of dispensing treatment. Further, VISITNUM should not be used to indicate that treatment began at a particular visit and continued for a period of time. The SDTM does not have any provision for recording "start visit" and "end visit" of exposure.

   b. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation.

5. Collected exposure data points are to be represented in the Exposure as Collected (EC) domain. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.

6. Additional interventions qualifiers

   a. EX contains medications received; the inclusion of administrations not taken, not given, or missed is under evaluation. Because EX includes only treatments received, --MOOD would generally not be used in EX.

   b. --DOSTOT is under evaluation for potential deprecation and replacement with a mechanism to describe total dose over any interval of time (e.g., day, week, month). Sponsors considering use of EXDOSTOT may want to consider using other dose-amount variables (EXDOSE or EXDOSTXT) in combination with frequency (EXDOSFRQ) and timing variables to represent the data.

   c. When the EC domain is implemented in conjunction with the EX domain, EXVAMT and EXVAMTU would not be used in EX; collected values instead would be represented in ECDOSE and ECDOSU (and ECVAMT and ECVAMTU as needed).

   d. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the EX domain, but the following qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, and --REASND.

#### 6.1.3.2 Exposure as Collected (EC)

**EC -- Description/Overview**

An interventions domain that contains information about protocol-specified study treatment administrations, as collected.

**EC -- Specification**

ec.xpt, Exposure as Collected -- Interventions. One record per protocol-specified study treatment, collected-dosing interval, per subject, per mood, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format<sup>1</sup> | Role | CDISC Notes | Core |
|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | EC | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| ECSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| ECGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| ECREFID | Reference ID | Char | | Identifier | Internal or external identifier (e.g., kit number, bottle label, vial identifier). | Perm |
| ECSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. | Perm |
| ECLNKID | Link ID | Char | | Identifier | Identifier used to link related records across domains. | Perm |
| ECLNKGRP | Link Group ID | Char | | Identifier | Identifier used to link related, grouped records across domains. | Perm |
| ECTRT | Name of Treatment | Char | \* | Topic | Name of the intervention treatment known to the subject and/or administrator. | Req |
| ECMOOD | Mood | Char | (BRDGMOOD) | Record Qualifier | Mode or condition of the record specifying whether the intervention (activity) is intended to happen or has happened. Values align with BRIDG pillars (e.g., scheduled context, performed context) and HL7 activity moods (e.g., intent, event). Examples: "SCHEDULED", "PERFORMED". | Perm |
| ECCAT | Category of Treatment | Char | \* | Grouping Qualifier | Used to define a category of related ECTRT values. | Perm |
| ECSCAT | Subcategory of Treatment | Char | \* | Grouping Qualifier | A further categorization of ECCAT values. | Perm |
| ECPRESP | Pre-Specified | Char | (NY) | Variable Qualifier | Used when a specific intervention is prespecified. Values should be "Y" or null. | Perm |
| ECOCCUR | Occurrence | Char | (NY) | Record Qualifier | Used to indicate whether a treatment occurred when information about the occurrence is solicited. ECOCCUR = "N" when a treatment was not taken, not given, or missed. | Perm |
| ECREASOC | Reason for Occur Value | Char | | Record Qualifier | The reason for the value in --OCCUR. If --OCCUR = "N", this is the reason the exposure did not occur. | Perm |
| ECDOSE | Dose | Num | | Record Qualifier | Amount of ECTRT when numeric. Not populated when ECDOSTXT is populated. | Exp |
| ECDOSTXT | Dose Description | Char | | Record Qualifier | Amount of ECTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when ECDOSE is populated. | Perm |
| ECDOSU | Dose Units | Char | (UNIT) | Variable Qualifier | Units for ECDOSE, ECDOSTOT, or ECDOSTXT. | Exp |
| ECDOSFRM | Dose Form | Char | (FRM) | Variable Qualifier | Dose form for ECTRT. Examples: "TABLET", "LOTION". | Exp |
| ECDOSFRQ | Dosing Frequency per Interval | Char | (FREQ) | Record Qualifier | Usually expressed as the number of repeated administrations of ECDOSE within a specific time period. Examples: "Q2H", "QD", "BID". | Perm |
| ECDOSTOT | Total Daily Dose | Num | | Record Qualifier | Total daily dose of ECTRT using the units in ECDOSU. Used when dosing is collected as total daily dose. | Perm |
| ECDOSRGM | Intended Dose Regimen | Char | | Record Qualifier | Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF". | Perm |
| ECROUTE | Route of Administration | Char | (ROUTE) | Variable Qualifier | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". | Perm |
| ECLOT | Lot Number | Char | | Record Qualifier | Lot number of the ECTRT product. | Perm |
| ECLOC | Location of Dose Administration | Char | (LOC) | Record Qualifier | Specifies location of administration. Example: "ARM", "LIP". | Perm |
| ECLAT | Laterality | Char | (LAT) | Variable Qualifier | Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT". | Perm |
| ECDIR | Directionality | Char | (DIR) | Variable Qualifier | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER". | Perm |
| ECPORTOT | Portion or Totality | Char | (PORTOT) | Variable Qualifier | Qualifier for anatomical location further detailing distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT". | Perm |
| ECFAST | Fasting Status | Char | (NY) | Record Qualifier | Indicator used to identify fasting status. Examples: "Y", "N". | Perm |
| ECPSTRG | Pharmaceutical Strength | Num | | Record Qualifier | Amount of an active ingredient expressed quantitatively per dosage unit, per unit of volume, or per unit of weight, according to the pharmaceutical dose form. | Perm |
| ECPSTRGU | Pharmaceutical Strength Units | Char | (UNIT) | Variable Qualifier | Unit for ECPSTRG. Examples: "mg/TABLET", "mg/mL". | Perm |
| ECADJ | Reason for Dose Adjustment | Char | | Record Qualifier | Describes reason or explanation of why a dose is adjusted. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Trial epoch of the exposure as collected record. Examples: "RUN-IN", "TREATMENT". | Perm |
| ECSTDTC | Start Date/Time of Treatment | Char | ISO 8601 datetime or interval | Timing | The date/time when administration of the treatment indicated by ECTRT and ECDOSE began. | Exp |
| ECENDTC | End Date/Time of Treatment | Char | ISO 8601 datetime or interval | Timing | The date/time when administration of the treatment indicated by ECTRT and ECDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC as the standard representation. | Exp |
| ECSTDY | Study Day of Start of Treatment | Num | | Timing | Study day of ECSTDTC relative to the sponsor-defined DM.RFSTDTC. | Perm |
| ECENDY | Study Day of End of Treatment | Num | | Timing | Study day of ECENDTC relative to the sponsor-defined DM.RFSTDTC. | Perm |
| ECDUR | Duration of Treatment | Char | ISO 8601 duration | Timing | Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times. | Perm |
| ECTPT | Planned Time Point Name | Char | | Timing | Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ECTPTNUM and ECTPTREF. | Perm |
| ECTPTNUM | Planned Time Point Number | Num | | Timing | Numerical version of ECTPT to aid in sorting. | Perm |
| ECELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time relative to the planned fixed reference (ECTPTREF). This variable is useful where there are repetitive measures. Not a clock time. | Perm |
| ECTPTREF | Time Point Reference | Char | | Timing | Name of the fixed reference point referred to by ECELTM, ECTPTNUM, and ECTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". | Perm |
| ECRFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 datetime or interval | Timing | Date/time for a fixed reference time point defined by ECTPTREF. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**EC -- Assumptions**

1. The EC domain model reflects protocol-specified study treatment administrations, as collected.

   a. EC should be used in all cases where collected exposure information cannot or should not be directly represented in the Exposure (EX) domain. For example, administrations collected in tablets when the protocol-specified unit is mg, or administrations collected in mL when the protocol-specified unit is mg/kg. Product accountability details (e.g., amount dispensed, amount returned) are represented in the DA domain, not in EC.

   b. Collected exposure data are in most cases represented in a combination of 1 or more of EC, DA, or Findings About Events or Interventions (FA) domains. If the entire EC dataset is an exact duplicate of the entire EX dataset, then EC is optional and at the sponsor's discretion.

   c. Collected exposure log data points descriptive of administrations typically reflect amounts at the product-level (e.g., number of tablets, number of mL).

2. Treatment description (ECTRT) is sponsor-defined and should reflect how the protocol-specified study treatment is known or referred to in data collection. In an open-label study, ECTRT should store the treatment name. In a masked study, if treatment is collected and known as tablet A to the subject or administrator, then ECTRT = "TABLET A". If, in a masked study, the treatment is not known by a synonym and the data are to be exchanged between sponsors, partners, and/or regulatory agency(s), then assign ECTRT the value of "MASKED".

3. ECMOOD is permissible; when implemented, it must be populated for all records.

   a. Values of ECMOOD, to date include:

      i. "SCHEDULED" (for collected subject-level intended dose records)

      ii. "PERFORMED" (for collected subject-level actual dose records)

   b. Qualifier variables should be populated with equal granularity across scheduled and performed records when known. For example, if ECDOSU and ECDOSFRQ are known at scheduling and administration, then the variables would be populated on both records. If ECLOC is determined at the time of administration, then it would be populated on the Performed record only.

   c. Appropriate timing variable(s) should be populated. Note: Details on Scheduled records may describe timing at a higher level than Performed records.

   d. ECOCCUR is generally not applicable for Scheduled records.

   e. An activity may be rescheduled or modified multiple times before being performed. Representation of Scheduled records is dependent on the collected, available data. If each rescheduled or modified activity is collected, then multiple Scheduled records may be represented. If only the final scheduled activity is collected, then it would be the only Scheduled record represented.

4. Doses not taken, not given, or missed

   a. The record qualifier --OCCUR, with value of "N", is available in domains based on the Interventions and Events General Observation Classes as the standard way to represent whether an intervention or event did not happen. In the EC domain, ECOCCUR value of "N" indicates a dose was not taken, not given, or missed. For example, if zero tablets are taken within a timeframe or zero mL is infused at a visit, then ECOCCUR = "N" is the standard representation of the collected doses not taken, not given, or missed. Dose amount variables (e.g., ECDOSE, ECDOSTXT) must not be set to zero (0) as an alternative method for indicating doses not taken, not given, or missed.

   b. The population of qualifier variables (e.g., grouping, record) and additional timing variables (e.g., date of collection, visit, time point) for records representing information collected about doses not taken, not given, or missed should be populated with equal granularity as administered records, when known and/or applicable. Qualifiers that indicate dose amount (e.g., ECDOSE, ECDOSTXT) may be populated with positive (non-zero) values in cases where the sponsor feels it is necessary and/or appropriate to represent specific dose amounts not taken, not given, or missed.

   c. If a reason why a dose was not given is collected, it is represented in ECREASOC, the reason why ECOCCUR = "N".

5. Timing variables

   a. Timing variables in the EC domain should reflect administrations by the intervals they were collected (e.g., constant-dosing intervals, visits, targeted dates like first dose, last dose).

   b. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC.

6. The degree of summarization of records from EC to EX is sponsor-defined to support study purpose and analysis. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.

7. Additional interventions qualifiers

   a. --DOSTOT is under evaluation for potential deprecation and replacement with a mechanism to describe total dose over any interval of time (e.g., day, week, month). Sponsors considering ECDOSTOT may want to consider using other dose amount variables (ECDOSE or ECDOSTXT) in combination with frequency (ECDOSFRQ) and timing variables to represent the data.

   b. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the EC domain, but the following qualifiers would generally not be used: --STAT and --REASND.

#### 6.1.3.3 Exposure/Exposure as Collected Examples

**Example 1**

This is an example of a double-blind study comparing drug X extended release (ER; 2 500-mg tablets once daily) vs. drug Z (2 250-mg tablets once daily). Per example CRFs, subject ABC1001 took 2 tablets from 2011-01-14 to 2011-01-28 and subject ABC2001 took 2 tablets within the same timeframe but missed dosing on 2011-01-24.

Exposure CRF:

Subject: ABC1001

| Bottle | Number of Tablets Taken Daily | Reason for Variation | Start Date | End Date |
|---|---|---|---|---|
| A | 2 | | 2011-01-14 | 2011-01-28 |

Subject: ABC2001

| Bottle | Number of Tablets Taken Daily | Reason for Variation | Start Date | End Date |
|---|---|---|---|---|
| A | 2 | | 2011-01-14 | 2011-01-23 |
| A | 0 | Patient mistake | 2011-01-24 | 2011-01-24 |
| A | 2 | | 2011-01-25 | 2011-01-28 |

Upon unmasking, it became known that subject ABC1001 received drug X and Subject ABC2001 received drug Z. The EC dataset shows the administrations of study treatment as collected.

Rows 1-2, 4:
Show treatments administered.

Row 3:
Shows that the zero for Number of Tablets Taken Daily on the CRF was represented as ECOCCUR = "N". The reason this treatment did not occur is represented in ECREASOC.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECREASOC | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | ABC1001 | 1 | A2-20110114 | BOTTLE A | Y | Y | | 2 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |
| 2 | ABC | EC | ABC2001 | 1 | A2-20110114 | BOTTLE A | Y | Y | | 2 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-23 | 1 | 10 |
| 3 | ABC | EC | ABC2001 | 2 | A0-20110124 | BOTTLE A | Y | N | PATIENT MISTAKE | | TABLET | QD | TREATMENT | 2011-01-24 | 2011-01-24 | 11 | 11 |
| 4 | ABC | EC | ABC2001 | 3 | A2-20110125 | BOTTLE A | Y | Y | | 2 | TABLET | QD | TREATMENT | 2011-01-25 | 2011-01-28 | 12 | 15 |

The EX dataset shows the unmasked administrations. Two tablets from bottle A became 1000 mg of drug X extended release for subject ABC1001, but 500 mg of drug Z for subject ABC2001. Note that there is no record in the EX dataset for non-occurrence of study treatment. The non-occurrence of study drug for subject ABC2001 is reflected in the gap in time between the 2 EX records.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXLNKID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EX | ABC1001 | 1 | A2-20110114 | DRUG X | 1000 | mg | TABLET, EXTENDED RELEASE | QD | ORAL | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |
| 2 | ABC | EX | ABC2001 | 1 | A2-20110114 | DRUG Z | 500 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-14 | 2011-01-23 | 1 | 10 |
| 3 | ABC | EX | ABC2001 | 2 | A2-20110125 | DRUG Z | 500 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-25 | 2011-01-28 | 12 | 15 |

The relrec.xpt example reflects a one-to-one dataset-level relationship between EC and EX using --LNKID.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | | ECLNKID | | ONE | 1 |
| 2 | ABC | EX | | EXLNKID | | ONE | 1 |

**Example 2**

This example shows data from an open-label study. A subject received drug X as a 20 mg/mL solution administered across 3 injection sites to deliver a total dose of 3 mg/kg. The subject's weight was 100 kg.

Exposure CRF:

|Visit |  3 |
|---|---|
| Date | 2009-05-10 |
| Injection 1 -- Volume Given (mL) | 5 |
| Injection 1 -- Location | ABDOMEN |
| Injection 1 -- Side | LEFT |
| Injection 2 -- Volume Given (mL) | 5 |
| Injection 2 -- Location | ABDOMEN |
| Injection 2 -- Side | CENTER |
| Injection 3 -- Volume Given (mL) | 5 |
| Injection 3 -- Location | ABDOMEN |
| Injection 3 -- Side | RIGHT |

The collected administration amounts, in mL, and their locations are represented in the EC dataset.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECSPID | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | ECLOC | ECLAT | VISITNUM | VISIT | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | ABC3001 | 1 | INJ1 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | LEFT | 3 | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |
| 2 | ABC | EC | ABC3001 | 2 | INJ2 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | CENTER | 3 | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |
| 3 | ABC | EC | ABC3001 | 3 | INJ3 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | RIGHT | 3 | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |

The sponsor considered the 3 injections to constitute a single administration, so the EX dataset shows the total dose given in the protocol-specified unit, mg/kg. EXLOC = "ABDOMEN" is included because this location was common to all injections, but EXLAT was not included. If the sponsor had chosen to represent laterality in the EX record, this would have been handled as described in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXSPID | EXLNKID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EXLOC | VISITNUM | VISIT | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EX | ABC3001 | 1 | | V3 | DRUG X | 3 | mg/kg | INJECTION | ONCE | SUBCUTANEOUS | ABDOMEN | 3 | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |

The relrec.xpt example reflects a many-to-one dataset-level relationship between EC and EX using --LNKID.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | | ECLNKID | | MANY | 1 |
| 2 | ABC | EX | | EXLNKID | | ONE | 1 |

**Example 3**

The study in this example was a double-blind study comparing 10, 20, and 30 mg of Drug X once daily vs. placebo. Study treatment was given as 1 tablet each from bottles A, B, and C taken together once daily. The subject in this example took:

- 1 tablet from bottles A, B and C from 2011-01-14 to 2011-01-20
- 0 tablets from bottle B on 2011-01-21, then 2 tablets on 2011-01-22
- 1 tablet from bottles A and C on 2011-01-21 and 2011-01-22
- 1 tablet from bottles A, B and C from 2011-01-23 to 2011-01-28

The EC dataset shows administrations as collected, in tablets.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | ABC4001 | 1 | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |
| 2 | ABC | EC | ABC4001 | 2 | BOTTLE C | Y | Y | 1 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |
| 3 | ABC | EC | ABC4001 | 3 | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-20 | 1 | 7 |
| 4 | ABC | EC | ABC4001 | 4 | BOTTLE B | Y | N | | TABLET | QD | TREATMENT | 2011-01-21 | 2011-01-21 | 8 | 8 |
| 5 | ABC | EC | ABC4001 | 5 | BOTTLE B | Y | Y | 2 | TABLET | QD | TREATMENT | 2011-01-22 | 2011-01-22 | 9 | 9 |
| 6 | ABC | EC | ABC4001 | 6 | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2011-01-23 | 2011-01-28 | 10 | 15 |

Upon unmasking, it became known that the subject was randomized to drug X 20 mg and that:

- Bottle A contained 10 mg/tablet
- Bottle B contained 10 mg/tablet
- Bottle C contained placebo (i.e., 0 mg of active ingredient/tablet)

The EX dataset shows the doses administered in the protocol-specified unit (mg). The sponsor considered an administration to consist of the total amount for bottles A, B, and C. The derivation of EX records from multiple EC records should be shown in the Define-XML document.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EX | ABC4001 | 1 | DRUG X | 20 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-14 | 2011-01-20 | 1 | 7 |
| 2 | ABC | EX | ABC4001 | 2 | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-21 | 2011-01-21 | 8 | 8 |
| 3 | ABC | EX | ABC4001 | 3 | DRUG X | 30 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-22 | 2011-01-22 | 9 | 9 |
| 4 | ABC | EX | ABC4001 | 4 | DRUG X | 20 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-23 | 2011-01-28 | 10 | 15 |

**Example 4**

The study in this example was an open-label study examining the tolerability of different doses of drug A. The study drug was taken orally, daily for 3 months. Dose adjustments were allowed as needed in response to tolerability or efficacy issues.

The EX dataset shows administrations collected in the protocol-specified unit, mg. No EC dataset was needed because the open-label administrations were collected in the protocol-specified unit; EC would be an exact duplicate of the entire EX domain.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EXADJ | EPOCH | EXSTDTC | EXENDTC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 37841 | EX | 37841001 | 1 | DRUG A | 20 | mg | TABLET | QD | ORAL | | TREATMENT | 2002-07-01 | 2002-10-01 |
| 2 | 37841 | EX | 37841002 | 1 | DRUG A | 20 | mg | TABLET | QD | ORAL | | TREATMENT | 2002-04-02 | 2002-04-21 |
| 3 | 37841 | EX | 37841002 | 2 | DRUG A | 15 | mg | TABLET | QD | ORAL | Reduced due to toxicity | TREATMENT | 2002-04-22 | 2002-07-01 |
| 4 | 37841 | EX | 37841003 | 1 | DRUG A | 20 | mg | TABLET | QD | ORAL | | TREATMENT | 2002-05-09 | 2002-06-01 |
| 5 | 37841 | EX | 37841003 | 2 | DRUG A | 25 | mg | TABLET | QD | ORAL | Increased due to suboptimal efficacy | TREATMENT | 2002-06-02 | 2002-07-01 |
| 6 | 37841 | EX | 37841003 | 3 | DRUG A | 30 | mg | TABLET | QD | ORAL | Increased due to suboptimal efficacy | TREATMENT | 2002-07-02 | 2002-08-01 |

**Example 5**

This is an example of a double-blind study design comparing 10 and 20 mg of drug X vs. placebo taken daily, morning and evening, for a week.

Exposure CRF:

Subject: ABC5001

| Bottle | Time Point | Number of Tablets Taken | Start Date | End Date |
|---|---|---|---|---|
| A | AM | 1 | 2012-01-01 | 2012-01-08 |
| B | PM | 1 | 2012-01-01 | 2012-01-08 |

Subject: ABC5002

| Bottle | Time Point | Number of Tablets Taken | Start Date | End Date |
|---|---|---|---|---|
| A | AM | 1 | 2012-02-01 | 2012-02-08 |
| B | PM | 1 | 2012-02-01 | 2012-02-08 |

Subject: ABC5003

| Bottle | Time Point | Number of Tablets Taken | Start Date | End Date |
|---|---|---|---|---|
| A | AM | 1 | 2012-03-01 | 2012-03-08 |
| B | PM | 1 | 2012-03-01 | 2012-03-08 |

The EC dataset shows the administrations as collected. The time-point variables ECTPT and ECTPTNUM were used to describe the time of day of administration. This use of time-point variables is novel, representing data about multiple time points, 1 on each day of administration, rather than data for a single time point.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECTPTNUM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | ABC5001 | 1 | 20120101-20120108-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | AM | 1 |
| 2 | ABC | EC | ABC5001 | 2 | 20120101-20120108-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | PM | 2 |
| 3 | ABC | EC | ABC5002 | 1 | 20120201-20120208-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | AM | 1 |
| 4 | ABC | EC | ABC5002 | 2 | 20120201-20120208-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | PM | 2 |
| 5 | ABC | EC | ABC5003 | 1 | 20120301-20120308-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | AM | 1 |
| 6 | ABC | EC | ABC5003 | 2 | 20120301-20120308-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | PM | 2 |

The EX dataset shows the unmasked administrations in the protocol specified unit, mg. Amount of placebo was represented as 0 mg. The sponsor chose to represent the administrations at the time-point level.

Rows 1-2:
Show administrations for a subject who was randomized to the 20 mg drug X arm.

Rows 3-4:
Show administrations for a subject who was randomized to the 10 mg drug X arm.

Rows 5-6:
Show administrations for a subject who was randomized to the placebo arm.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXLNKID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY | EXTPT | EXTPTNUM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EX | ABC5001 | 1 | 20120101-20120108-AM | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | AM | 1 |
| 2 | ABC | EX | ABC5001 | 2 | 20120101-20120108-PM | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | PM | 2 |
| 3 | ABC | EX | ABC5002 | 1 | 20120201-20120208-AM | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | AM | 1 |
| 4 | ABC | EX | ABC5002 | 2 | 20120201-20120208-PM | PLACEBO | 0 | mg | TABLET | QD | ORAL | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | PM | 2 |
| 5 | ABC | EX | ABC5003 | 1 | 20120301-20120308-AM | PLACEBO | 0 | mg | TABLET | QD | ORAL | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | AM | 1 |
| 6 | ABC | EX | ABC5003 | 2 | 20120301-20120308-PM | PLACEBO | 0 | mg | TABLET | QD | ORAL | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | PM | 2 |

The relrec.xpt example reflects a one-to-one dataset-level relationship between EC and EX using --LNKID.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | | ECLNKID | | ONE | 1 |
| 2 | ABC | EX | | EXLNKID | | ONE | 1 |

**Example 6**

The study in this example was a single-crossover study comparing once-daily oral administration of drug A 20 mg capsules with drug B 30 mg coated tablets. The study drug was taken for 3 consecutive mornings, 30 minutes prior to a standardized breakfast. There was a 6-day washout period between treatments.

The following CRFs show data for 2 subjects.

Subject: 56789001

| | Period 1 | | | | | Period 2 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time | | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time |
| 1 | 1 | 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 1 | 2002-07-09T07:30 | 2002-07-09T07:30 |
| 2 | 1 | 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 1 | 1 | 2002-07-10T07:30 | 2002-07-10T07:30 |
| 3 | 1 | 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 1 | 1 | 2002-07-11T07:34 | 2002-07-11T07:34 |

Subject: 56789003

| | Period 1 | | | | | Period 2 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time | | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time |
| 1 | 1 | 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 1 | 2002-07-11T07:30 | 2002-07-11T07:30 |
| 2 | 1 | 1 | 2002-07-04T07:24 | 2002-07-04T07:24 | 2 | 1 | 1 | 2002-07-12T07:43 | 2002-07-12T07:43 |
| 3 | 1 | 1 | 2002-07-05T07:24 | 2002-07-05T07:24 | 3 | 1 | 1 | 2002-07-13T07:38 | 2002-07-13T07:38 |

The EC dataset shows administrations as collected.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECELTM | ECTPTREF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 56789 | EC | 56789001 | 1 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 2 | 56789 | EC | 56789001 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 3 | 56789 | EC | 56789001 | 3 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 4 | 56789 | EC | 56789001 | 4 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 5 | 56789 | EC | 56789001 | 5 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 6 | 56789 | EC | 56789001 | 6 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 7 | 56789 | EC | 56789001 | 7 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-09T07:30 | 2002-07-09T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 8 | 56789 | EC | 56789001 | 8 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-09T07:30 | 2002-07-09T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 9 | 56789 | EC | 56789001 | 9 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-10T07:30 | 2002-07-10T07:30 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 10 | 56789 | EC | 56789001 | 10 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-10T07:30 | 2002-07-10T07:30 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 11 | 56789 | EC | 56789001 | 11 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:34 | 2002-07-11T07:34 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 12 | 56789 | EC | 56789001 | 12 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-11T07:34 | 2002-07-11T07:34 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 13 | 56789 | EC | 56789003 | 1 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 14 | 56789 | EC | 56789003 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 15 | 56789 | EC | 56789003 | 3 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-04T07:24 | 2002-07-04T07:24 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 16 | 56789 | EC | 56789003 | 4 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-04T07:24 | 2002-07-04T07:24 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 17 | 56789 | EC | 56789003 | 5 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-05T07:24 | 2002-07-05T07:24 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 18 | 56789 | EC | 56789003 | 6 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-05T07:24 | 2002-07-05T07:24 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 19 | 56789 | EC | 56789003 | 7 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:30 | 2002-07-11T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 20 | 56789 | EC | 56789003 | 8 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-11T07:30 | 2002-07-11T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 21 | 56789 | EC | 56789003 | 9 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-12T07:43 | 2002-07-12T07:43 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 22 | 56789 | EC | 56789003 | 10 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-12T07:43 | 2002-07-12T07:43 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 23 | 56789 | EC | 56789003 | 11 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-13T07:38 | 2002-07-13T07:38 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 24 | 56789 | EC | 56789003 | 12 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-13T07:38 | 2002-07-13T07:38 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |

The EX dataset shows the unblinded administrations.

Rows 1-12:
Unblinding revealed that subject 56789001 received placebo-coated tablets during the first treatment epoch and placebo capsules during the second treatment epoch.

Rows 13-24:
Unblinding revealed that subject 56789003 received placebo capsules during the first treatment epoch and placebo-coated tablets during the second treatment epoch.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY | EXTPT | EXELTM | EXTPTREF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 56789 | EX | 56789001 | 1 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 2 | 56789 | EX | 56789001 | 2 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 3 | 56789 | EX | 56789001 | 3 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 4 | 56789 | EX | 56789001 | 4 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 5 | 56789 | EX | 56789001 | 5 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 6 | 56789 | EX | 56789001 | 6 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 7 | 56789 | EX | 56789001 | 7 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-09T07:30 | | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 8 | 56789 | EX | 56789001 | 8 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-09T07:30 | | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 9 | 56789 | EX | 56789001 | 9 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-10T07:30 | | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 10 | 56789 | EX | 56789001 | 10 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-10T07:30 | | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 11 | 56789 | EX | 56789001 | 11 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:34 | | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 12 | 56789 | EX | 56789001 | 12 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-11T07:34 | | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 13 | 56789 | EX | 56789003 | 1 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 14 | 56789 | EX | 56789003 | 2 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 15 | 56789 | EX | 56789003 | 3 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-04T07:24 | | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 16 | 56789 | EX | 56789003 | 4 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-04T07:24 | | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 17 | 56789 | EX | 56789003 | 5 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-05T07:24 | | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 18 | 56789 | EX | 56789003 | 6 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-05T07:24 | | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 19 | 56789 | EX | 56789003 | 7 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:30 | | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 20 | 56789 | EX | 56789003 | 8 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-11T07:30 | | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 21 | 56789 | EX | 56789003 | 9 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-12T07:43 | | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 22 | 56789 | EX | 56789003 | 10 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-12T07:43 | | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 23 | 56789 | EX | 56789003 | 11 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-13T07:38 | | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 24 | 56789 | EX | 56789003 | 12 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-13T07:38 | | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |

**Example 7**

The study in this example involved weekly infusions of drug Z 10 mg/kg. If a subject experienced a dose-limiting toxicity (DLT), the intended dose could be reduced to 7.5 mg/kg.

The example CRF below was for subject ABC123-0201, who weighed 55 kg. The CRF shows that:

- The subject's first administration of drug Z was on 2009-02-13; the intended dose was 10 mg/kg, but the actual amount given was 99 mL at 5.5 mg/mL, so the actual dose was 9.9 mg/kg.
- The subject's second administration of drug Z occurred on 2009-02-20; the intended dose was reduced to 7.5 mg/kg due to dose-limiting toxicity, and the infusion was stopped early due to an injection site reaction. However, the actual amount given was 35 mL at a concentration of 4.12 mg/mL, so the calculated actual dose was 2.6 mg/kg.
- The subject's third administration was intended to occur on 2009-02-27; the intended dose was 7.5 mg/kg but, due to a personal reason, the administration did not occur.

Exposure CRF:

| | Visit 1 | Visit 2 | Visit 3 |
|---|---|---|---|
| Intended Dose | 10 mg/kg | 7.5 mg/kg | 7.5 mg/kg |
| Reason for Dose Adjustment | | Dose-limiting toxicity | |
| Dose Administered | Yes | Yes | No -- Personal reason |
| Date | 13-FEB-2009 | 20-FEB-2009 | 27-FEB-2009 |
| Start Time (24 hour clock) | 10:00 | 11:00 | |
| End Time (24 hour clock) | 10:45 | 11:20 | |
| Amount (mL) | 99 mL | 35 mL | 0 mL |
| Concentration | 5.5 mg/mL | 4.12 mg/mL | 4.12 mg/mL |
| If dose was adjusted, what was the reason | | Injection site reaction | |

The EC dataset shows both intended and actual doses of Drug Z, as collected.

Rows 1, 3, 5:
Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED". Scheduled dose is represented in mg/mL.

Rows 2, 4:
Show the collected actual administration amounts (mL) and ECMOOD is "PERFORMED". Actual doses are represented using dose in mL and concentration (pharmaceutical strength) in mg/mL.

Row 6:
Shows a dose that was not given. ECREASOC shows the reason that ECOCCUR = "N", and ECDOSE is null.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECLNKGRP | ECTRT | ECMOOD | ECPRESP | ECOCCUR | ECREASOC | ECDOSE | ECDOSU | ECPSTRG | ECPSTRGU | ECADJ | VISITNUM | VISIT | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | EC | ABC123-0201 | 1 | | V1 | DRUG Z | SCHEDULED | | | | 10 | mg/kg | | | | 1 | VISIT 1 | TREATMENT | 2009-02-13 | 2009-02-13 | 1 | 1 |
| 2 | ABC123 | EC | ABC123-0201 | 2 | 20090213T1000 | V1 | DRUG Z | PERFORMED | Y | Y | | 99 | mL | 5.5 | mg/mL | | 1 | VISIT 1 | TREATMENT | 2009-02-13T10:00 | 2009-02-13T10:45 | 1 | 1 |
| 3 | ABC123 | EC | ABC123-0201 | 3 | | V2 | DRUG Z | SCHEDULED | | | | 7.5 | mg/kg | | | Dose limiting toxicity | 2 | VISIT 2 | TREATMENT | 2009-02-20 | 2009-02-20 | 8 | 8 |
| 4 | ABC123 | EC | ABC123-0201 | 4 | 20090220T1100 | V2 | DRUG Z | PERFORMED | Y | Y | | 35 | mL | 4.12 | mg/mL | | 2 | VISIT 2 | TREATMENT | 2009-02-20T11:00 | 2009-02-20T11:20 | 8 | 8 |
| 5 | ABC123 | EC | ABC123-0201 | 5 | | V3 | DRUG Z | SCHEDULED | | | | 7.5 | mg/kg | | | | 3 | VISIT 3 | TREATMENT | 2009-02-27 | 2009-02-27 | 15 | 15 |
| 6 | ABC123 | EC | ABC123-0201 | 6 | 20090227 | V3 | DRUG Z | PERFORMED | Y | N | PERSONAL REASON | | mL | 4.12 | mg/mL | | 3 | VISIT 3 | TREATMENT | 2009-02-27 | 2009-02-27 | 15 | 15 |

The EX dataset shows the administrations in protocol-specified unit (mg/kg). There is no record for the intended third dose that was not given. Intended doses in EC (records with ECMOOD = "SCHEDULED") can be compared with actual doses in EX.

Row 1:
Shows the subject's first dose.

Row 2:
Shows the subject's second dose. The collected explanation for the adjusted dose amount administered at visit 2 is in EXADJ.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXLNKID | EXLNKGRP | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EXADJ | VISITNUM | VISIT | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | EX | ABC123-0201 | 1 | 20090213T1000 | V1 | DRUG Z | 9.9 | mg/kg | SOLUTION | CONTINUOUS | INTRAVENOUS | | 1 | VISIT 1 | TREATMENT | 2009-02-13T10:00 | 2009-02-13T10:00 | 1 | 1 |
| 2 | ABC123 | EX | ABC123-0201 | 2 | 20090220T1100 | V2 | DRUG Z | 2.6 | mg/kg | SOLUTION | CONTINUOUS | INTRAVENOUS | Injection site reaction | 2 | VISIT 2 | TREATMENT | 2009-02-20T11:00 | 2009-02-20T11:00 | 8 | 8 |

To complete this example the relevant records from the Vital Signs domain are represented below, to show the collected weight of the subject which was used for the dosing calculations.

vs.xpt

| Row | STUDYID | DOMAIN | USUBJID | VSSEQ | VSLNKID | VSLNKGRP | VSTESTCD | VSTEST | VSORRES | VSORRESU | VSSTRESC | VSSTRESN | VSSTRESU | VSLOBXFL | VISITNUM | VISIT | VSDTC | EPOCH |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC123 | VS | ABC123-0201 | 1 | 20090213T1000 | V1 | WEIGHT | Weight | 55 | kg | 55 | 55 | kg | Y | 1 | VISIT 1 | 2009-02-13 | TREATMENT |
| 2 | ABC123 | VS | ABC123-0201 | 2 | 20090220T1100 | V2 | WEIGHT | Weight | 55 | kg | 55 | 55 | kg | | 2 | VISIT 2 | 2009-02-20 | TREATMENT |

The RELREC dataset represents relationships between EC, EX, and VS.

Rows 1-3:
Represent the one-to-one-to-one relationship between "PERFORMED" records in EC, records in EX, and records in VS using --LNKID.

Rows 4-6:
Represent the many-to-one-to-one relationship between many records in EC (both "SCHEDULED" and "PERFORMED"), one record in EX, and one record in VS (for each visit), using --LNKGRP.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|---|
| 1 | ABC123 | EC | | ECLNKID | | ONE | 1 |
| 2 | ABC123 | EX | | EXLNKID | | ONE | 1 |
| 3 | ABC123 | VS | | VSLNKID | | ONE | 1 |
| 4 | ABC123 | EC | | ECLNKGRP | | MANY | 2 |
| 5 | ABC123 | EX | | EXLNKGRP | | ONE | 2 |
| 6 | ABC123 | VS | | VSLNKGRP | | ONE | 2 |

**Example 8**

In this example, a 100 mg tablet is scheduled to be taken daily. Start and end of dosing were collected, along with deviations from the planned daily dosing. Note: This method of data collection design is not consistent with current CDASH standards.

Exposure CRF:

| First Dose Date | Last Dose Date |
|---|---|
| 2012-01-13 | 2012-01-20 |

| Date | Number of Doses Daily | If/When Deviated from Plan |
|---|---|---|
| 2012-01-15 | 0 | |
| 2012-01-16 | 2 | |

The EC dataset shows administrations as collected.

Row 1:
Shows the overall dosing interval from first dose date to last dose date.

Row 2:
Shows the missed dose on 2012-01-15, which falls within the overall dosing interval.

Row 3:
Shows a doubled dose on 2012-01-16, which also falls within the overall dosing interval.

ec.xpt

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECCAT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EC | ABC7001 | 1 | BOTTLE A | FIRST TO LAST DOSE INTERVAL | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-13 | 2012-01-20 | 1 | 8 |
| 2 | ABC | EC | ABC7001 | 2 | BOTTLE A | EXCEPTION DOSE | Y | N | | TABLET | QD | TREATMENT | 2012-01-15 | 2012-01-15 | 3 | 3 |
| 3 | ABC | EC | ABC7001 | 3 | BOTTLE A | EXCEPTION DOSE | Y | Y | 2 | TABLET | QD | TREATMENT | 2012-01-16 | 2012-01-16 | 4 | 4 |

The EX dataset shows the unmasked treatment for this subject, "DRUG X", and represents dosing in nonoverlapping intervals of time. There is no EX record for the missed dose, but the missed dose is reflected in a gap between dates in the EX records.

Row 1:
Shows the administration from first dose date to the day before the missed dose.

Row 2:
Shows the doubled dose.

Row 3:
Shows the remaining administrations to the last dose date.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ABC | EX | ABC7001 | 1 | DRUG X | 100 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-13 | 2012-01-14 | 1 | 2 |
| 2 | ABC | EX | ABC7001 | 2 | DRUG X | 200 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-16 | 2012-01-16 | 4 | 4 |
| 3 | ABC | EX | ABC7001 | 3 | DRUG X | 100 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-17 | 2012-01-20 | 5 | 8 |

---

