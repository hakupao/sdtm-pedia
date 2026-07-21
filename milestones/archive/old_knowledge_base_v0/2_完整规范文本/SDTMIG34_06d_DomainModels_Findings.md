# SDTMIG v3.4 --- Domain Models: Findings — Part 4

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 4/8 — 6.3.5.6-6.3.5.7: Specimen-based (LB, Microbiology)
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

#### 6.3.5.6 Laboratory Test Results (LB)

##### LB – Description/Overview
A findings domain that contains laboratory test data such as hematology, clinical chemistry and urinalysis. This domain does not include microbiology or pharmacokinetic data, which are stored in separate domains.


##### LB – Specification
lb.xpt, Laboratory Test Results — Findings. One record per lab test per time point per visit per subject, Tabulation.

**Structure:** One record per lab test per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | LB |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | LBSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | LBGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | LBREFID | Specimen ID | Char | Identifier | Perm |  |
| 7 | LBSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | LBTESTCD | Lab Test or Examination Short Name | Char | Topic | Req | C65047 |
| 9 | LBTEST | Lab Test or Examination Name | Char | Synonym Qualifier | Req | C67154 |
| 10 | LBTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |
| 11 | LBBDAGNT | Binding Agent | Char | Variable Qualifier | Perm |  |
| 12 | LBTSTOPO | Test Operational Objective | Char | Variable Qualifier | Perm | C181170 |
| 13 | LBCAT | Category for Lab Test | Char | Grouping Qualifier | Exp |  |
| 14 | LBSCAT | Subcategory for Lab Test | Char | Grouping Qualifier | Perm |  |
| 15 | LBORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 16 | LBORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| 17 | LBRESSCL | Result Scale | Char | Record Qualifier | Perm | C177910 |
| 18 | LBRESTYP | Result Type | Char | Record Qualifier | Perm | C179588 |
| 19 | LBCOLSRT | Collected Summary Result Type | Char | Record Qualifier | Perm | C177908 |
| 20 | LBORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Exp |  |
| 21 | LBORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Exp |  |
| 22 | LBLLOD | Lower Limit of Detection | Char | Variable Qualifier | Perm |  |
| 23 | LBSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C102580 |
| 24 | LBSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 25 | LBSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| 26 | LBSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Exp |  |
| 27 | LBSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Exp |  |
| 28 | LBSTNRC | Reference Range for Char Rslt-Std Units | Char | Variable Qualifier | Perm |  |
| 29 | LBNRIND | Reference Range Indicator | Char | Variable Qualifier | Exp | C78736 |
| 30 | LBSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 31 | LBREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |
| 32 | LBNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 33 | LBLOINC | LOINC Code | Char | Synonym Qualifier | Perm | LOINC |
| 34 | LBSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| 35 | LBSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 36 | LBSPCUFL | Specimen Usability for the Test | Char | Record Qualifier | Perm | C66742 |
| 37 | LBMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 38 | LBANMETH | Analysis Method | Char | Record Qualifier | Perm | C160922 |
| 39 | LBTMTHSN | Test Method Sensitivity | Char | Record Qualifier | Perm | C179589 |
| 40 | LBLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 41 | LBBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 42 | LBFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| 43 | LBDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 44 | LBTOX | Toxicity | Char | Variable Qualifier | Perm |  |
| 45 | LBTOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm |  |
| 46 | LBCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| 47 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 48 | VISIT | Visit Name | Char | Timing | Perm |  |
| 49 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 50 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 51 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 52 | LBDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 53 | LBENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 54 | LBDY | Study Day of Specimen Collection | Num | Timing | Perm |  |
| 55 | LBENDY | Study Day of End of Observation | Num | Timing | Perm |  |
| 56 | LBTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 57 | LBTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 58 | LBELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 59 | LBTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 60 | LBRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| 61 | LBPTFL | Point in Time Flag | Char | Timing | Perm | C66742 |
| 62 | LBPDUR | Planned Duration | Char | Timing | Perm | ISO 8601 duration |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **LBSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **LBGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **LBREFID**: Internal or external specimen identifier. Example: specimen ID.
- **LBSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Lab page.
- **LBTESTCD**: Short name of the measurement, test, or examination described in LBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in LBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). LBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ALT", "LDH".
- **LBTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. Note: Any test normally performed by a clinical laboratory is considered a lab test. The value in LBTEST cannot be longer than 40 characters. Examples: "Alanine Aminotransferase", "Lactate Dehydrogenase".
- **LBTSTCND**: Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.
- **LBBDAGNT**: The textual description of the agent that is binding to the entity in the LBTEST variable. The LBBDAGNT variable is used to indicate that there is a binding relationship between the entities in the LBTEST and LBBDAGNT variables, regardless of direction.; LBBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in LBTEST and LBBDAGNT. In other words, the combination of LBTEST and LBBDAGNT should describe the thing, the entity, or the analyte being measured, without the need for additional variables.; The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, or an endogenous molecule.
- **LBTSTOPO**: Text description of the high-level purpose of the test at the operational level.
- **LBCAT**: Used to define a category of related records across subjects. Examples: "HEMATOLOGY", "URINALYSIS", "CHEMISTRY".
- **LBSCAT**: A further categorization of a test category. Examples: "DIFFERENTIAL", "COAGULATION", "LIVER FUNCTION", "ELECTROLYTES".
- **LBORRES**: Result of the measurement or finding as originally received or collected.
- **LBORRESU**: Original units in which the data were collected. The unit for LBORRES. Example: "g/L".
- **LBRESSCL**: Classifies the scale of the original result value; for example, whether the result is ordinal, nominal, quantitative, or narrative.
- **LBRESTYP**: Classifies the kind of result (i.e., property type) originally reported for the test. Examples include substance concentration, proportion, mass rate, and arbitrary concentration.
- **LBCOLSRT**: Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived by the sponsor using individual source data records from SDTM, the derived summary result is represented in ADaM. If the summary result is produced and reported by the lab, the collected summary result is represented in SDTM.
- **LBORNRLO**: Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.
- **LBORNRHI**: Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.
- **LBLLOD**: The lowest threshold (as originally received or collected) for reliably detecting the presence or absence of substance measured by a specific test. The value for the field will be as described in documentation from the instrument or lab vendor.
- **LBSTRESC**: Contains the result value for all findings, copied or derived from LBORRES in a standard format or standard units. LBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in LBSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in LBORRES and these results effectively have the same meaning, they could be represented in standard format in LBSTRESC as "NEGATIVE". For other examples, see Original and Standardized Results.
- **LBSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from LBSTRESC. LBSTRESN should store all numeric test results or findings.
- **LBSTRESU**: Standardized unit used for LBSTRESC or LBSTRESN.
- **LBSTNRLO**: Lower end of reference range for continuous measurements for LBSTRESC/LBSTRESN in standardized units. Should be populated only for continuous results.
- **LBSTNRHI**: Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.
- **LBSTNRC**: For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".
- **LBNRIND**: Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI, LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate clinical significance.
- **LBSTAT**: Used to indicate exam not done. Should be null if a result exists in LBORRES.
- **LBREASND**: Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED", or "SPECIMEN LOST". Used in conjunction with LBSTAT when value is "NOT DONE".
- **LBNAM**: The name or identifier of the laboratory that performed the test.
- **LBLOINC**: Code for the lab test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.
- **LBSPEC**: Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE".
- **LBSPCCND**: The physical state or quality of a sample for an assessment. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".
- **LBSPCUFL**: Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.
- **LBMETHOD**: Method of the test or examination. Examples: "EIA" (enzyme immunoassay), "ELECTROPHORESIS", "DIPSTICK".
- **LBANMETH**: Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., a calculation used to measure eGFR).
- **LBTMTHSN**: The sensitivity of the test methodology with respect to observation, detection, or quantification.
- **LBLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **LBBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that LBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **LBFAST**: Indicator used to identify fasting status. Examples: "Y", "N".
- **LBDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If LBDRVFL="Y", then LBORRES may be null, with LBSTRESC and (if numeric) LBSTRESN having the derived value.
- **LBTOX**: Description of toxicity quantified by LBTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.
- **LBTOXGR**: Records toxicity grade value using a standard toxicity scale (e.g., the NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2" not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.
- **LBCLSIG**: Used to indicate whether a collected observation is clinically significant based on judgment.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.
- **LBDTC**: Date/time of specimen collection represented in ISO 8601 character format.
- **LBENDTC**: End date/time of specimen collection represented in ISO 8601 character format.
- **LBDY**: Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.
- **LBENDY**: Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **LBTPT**: Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See LBTPTNUM and LBTPTREF. Examples: "Start", "5 min post".
- **LBTPTNUM**: Numerical version of LBTPT to aid in sorting.
- **LBELTM**: Planned elapsed time (in ISO 8601) relative to a planned fixed reference (LBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by LBTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by LBTPTREF.
- **LBTPTREF**: Name of the fixed reference point referred to by LBELTM, LBTPTNUM, and LBTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **LBRFTDTC**: Date/time of the reference time point, LBTPTREF.
- **LBPTFL**: An indication that the specimen was collected at a single point in time. The value is "Y" or null. The intent of this variable in the LB domain is to aid mapping to LOINC codes in the dataset, when LOINC part "Time Aspect" = "Pt".
- **LBPDUR**: Planned duration of specimen collection. If LBPTFL is "Y" then LBPDUR is null.


##### LB – Assumptions
1. This domain captures laboratory data collected on the CRF or received from a central provider or vendor.
2. For lab tests that do not have continuous numeric results (e.g., urine protein as measured by dipstick, descriptive tests such as urine color), LBSTNRC could be populated either with normal range values that are a range of character values for an ordinal scale  (e.g., “NEGATIVE to TRACE") or a delimited set of values that are considered to be normal (e.g., “YELLOW”, “AMBER”). LBORNRLO, LBORNRHI, LBSTNRLO, and LBSTNRHI should be null for these types of tests.
3. LBNRIND can be added to indicate where a result falls with respect to reference range defined by LBORNRLO and LBORNRHI. Examples: "HIGH", "LOW". If toxicity grading is available, values would be represented in the variables LBTOX and LBTOXGR. Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in LBCLSIG (see also LB Example 1).
4. For lab tests where the specimen is collected over time (e.g., 24-hour urine collection), the start date/time of the collection goes into LBDTC and the end date/time of collection goes into LBENDTC. See Section 4.4.8, Date and Time Reported in a Domain Based on Findings.
5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the LB domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.
6. A value derived by a central lab according to its procedures is considered collected rather than derived. See Section 4.1.8.1, Origin Metadata for Variables.
7. The variable LBORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology List that is maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing/published unit from the UNIT codelist and submit their lab values using the published CDISC submission value. Example: "g/L" and "mg/mL" are mathematically synonymous, but only "g/L" is the submission value in the CDISC Unit codelist. If this is not the case, the unit must be added as a codelist extensible value in the Define.xml, and a new-term request must be submitted.
    a. CDISC Controlled Terminology Rules for Lab and Unit are available at https://www.cdisc.org/standards/terminology/controlled-terminology.
8. The LBLOINC variable contains a code from the Logical Observation Identifiers Names and Codes (LOINC) database that identifies a specific laboratory test. The LOINC to LB Mapping Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology, may be used to identify appropriate CDISC CT values for a test with a particular LOINC code. In addition to LBTEST, LBSPEC, LBMETHOD, and LBORRESU, the aspects of a test that are associated with a LOINC code may be represented in the variables LBTPT, LBANMETH, LBPOS, LBLOC, LBFAST, LBTSTCND, LBBDAGNT, LBTSTOPO, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBPTFL, and LBPDUR. These additional variables are only required to be populated when necessary to provide a semantically meaningful distinction between records with different LBLOINC values.

##### LB – Examples

**Example 1**
This example illustrates the use of previously published LB domain variables and introduces several new variables that were added to SDTMv2.0, including LBTSTCND, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBPTFL, and LBPDUR. These variables, in part, aid in harmonization to LOINC.
**Row 1:** Shows a value collected in 1 unit, but converted to selected standard unit. See Section 4.5.1, Original and Standardized Results of Findings and Tests Not Done, for additional examples for the population of result qualifiers. The result was evaluated by the investigator and determined to be not clinically significant.
**Rows 2-3:** Show 2 records for alkaline phosphatase done at the same visit, a day apart. LBPTFL is set to "Y" for both rows because each result is based on a sample from a single point in time.
**Rows 4-5:** Show 2 derived records (mean of records 2 and 3 and maximum value of records 2 and 3) grouped by a common LBGRPID value. The derived result in row 4 is described as a mean (LBCOLSRT="MEAN, ARITHMETIC"), but LBDRVFL is missing because the mean result was provided by the vendor. The derived result in row 5 was derived by the sponsor, and so is flagged as derived (LBDRVFL="Y"); LBCOLSRT is not populated because the result is not a collected summary result. For both derived results, the sponsor chose to populate LBRESSCL, LBRESTYP, LBSPEC, and LBFAST consistent with the 2 individual alkaline phosphatase records but did not populate LBLOINC or LBPTFL because neither derived record represented a single point in time. The sponsor chose to populate LBDTC with the first of the 2 specimen collection dates.
**Row 6:** Shows use of LBTMTHSN to represent "HIGH SENSITIVITY" for the high-sensitivity C-reactive protein (hs-CRP) test.
**Rows 7, 10:** Show use of LBTSTCND. For the cryoglobulin test, 1-day cold incubation is noted; for the platelet aggregation test, collagen induced is noted.
**Row 8:** Shows use of LBLLOD for a prostate-specific antigen test.
**Row 9:** Shows use of LBPDUR to represent the planned duration of "PT24H" for collection of urine samples for the protein test. LBPTFL is set to missing because this test was not conducted at a single point in time.
**Rows 12-13:** Show a suggested use of the LBSCAT variable. LBSCAT could be used to further classify types of tests within a laboratory panel (e.g., "DIFFERENTIAL"). The LYMLE result was evaluated by the investigator and determined to be not clinically significant.
**Row 15:** Shows the proper use of the LBSTAT variable to indicate "NOT DONE", where a reason was collected when a test was not done. LBRESSCL, LBRESTYP, LBLOINC, LBSPEC, LBMETHOD, and LBPTFL are populated to describe the properties of the test that was not done.
**Row 16:** Shows measuring of the subject's cholesterol. The normal range for this test is <200 mg/dL. Note that although in this example the sponsor has decided to make LBSTNRHI="199", other sponsors may choose a different value.
**Row 17:** Shows use of LBPTFL set to "Y" to indicate that the test used a sample taken at a single point in time.
**Row 18:** Shows use of LBSTNRC for urine protein that is not reported as a continuous numeric result. The result was evaluated by the investigator and determined to be not clinically significant.
*lb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBGRPID | LBTESTCD | LBTEST | LBTSTCND | LBCAT | LBSCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBCOLSRT | LBORNRLO | LBORNRHI | LBLLOD | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBSTNRC | LBNRIND | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBMETHOD | LBTMTHSN | LBLOBXFL | LBFAST | LBDRVFL | LBCLSIG | VISITNUM | VISIT | LBDTC | LBPTFL | LBPDUR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | LB | ABC-001-001 | 1 |  | ALB | Albumin |  | CHEMISTRY |  | 30 | g/L | QUANTITATIVE | MASS CONCENTRATION |  | 35 | 50 |  | 3.0 | 3.0 | g/dL | 3.5 | 5 |  | LOW |  |  | 2862-1 | SERUM | ELECTROPHORESIS |  | Y | Y |  | N | 1 | Week 1 | 1999-06-19 | Y |  |
| 2 | ABC | LB | ABC-001-001 | 2 | A | ALP | Alkaline Phosphatase |  | CHEMISTRY |  | 398 | IU/L | QUANTITATIVE | CATALYTIC CONCENTRATION |  | 40 | 160 |  | 398 | 398 | IU/L | 40 | 160 |  |  |  |  | 6768-6 | SERUM |  |  |  | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 3 | ABC | LB | ABC-001-001 | 3 | A | ALP | Alkaline Phosphatase |  | CHEMISTRY |  | 350 | IU/L | QUANTITATIVE | CATALYTIC CONCENTRATION |  | 40 | 160 |  | 350 | 350 | IU/L | 40 | 160 |  |  |  |  | 6768-6 | SERUM |  |  |  | Y |  |  | 1 | Week 1 | 1999-06-20 | Y |  |
| 4 | ABC | LB | ABC-001-001 | 4 | A | ALP | Alkaline Phosphatase |  | CHEMISTRY |  |  |  | QUANTITATIVE | CATALYTIC CONCENTRATION | MEAN, ARITHMETIC |  |  |  | 374 | 374 | IU/L | 40 | 160 |  |  |  |  |  | SERUM |  |  |  | Y |  |  | 1 | Week 1 | 1999-06-19 |  |  |
| 5 | ABC | LB | ABC-001-001 | 5 | A | ALP | Alkaline Phosphatase |  | CHEMISTRY |  |  |  | QUANTITATIVE | CATALYTIC CONCENTRATION |  |  |  |  | 398 | 398 | IU/L | 40 | 160 |  |  |  |  |  | SERUM |  |  |  | Y | Y |  | 1 | Week 1 | 1999-06-19 |  |  |
| 6 | ABC | LB | ABC-001-001 | 6 |  | CRP | C Reactive Protein |  | CHEMISTRY |  | 2.5 | mg/L | QUANTITATIVE | MASS CONCENTRATION |  |  |  |  | 2.5 | 2.5 | mg/L | 0.5 | 10 |  |  |  |  | 30522-7 | SERUM |  | HIGH SENSITIVITY | Y | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 7 | ABC | LB | ABC-001-001 | 7 |  | CRYOGLBN | Cryoglobulin | 1D COLD INCUBATION | CHEMISTRY |  | ABSENT |  | ORDINAL | PRESENCE OR THRESHOLD |  |  |  |  | ABSENT |  |  |  |  |  |  |  |  | 12201-0 | SERUM | OBSERVATION |  | Y | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 8 | ABC | LB | ABC-001-001 | 8 |  | PSA | Prostate Specific Antigen |  | CHEMISTRY |  | 3.3 | ug/L | QUANTITATIVE | MASS CONCENTRATION |  | 0 | 2.5 |  | 3.3 | 3.3 | ug/L | 0 | 2.5 |  |  |  |  | 35741-8 | SERUM |  |  | Y | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 9 | ABC | LB | ABC-001-001 | 9 |  | PROT | Protein |  | CHEMISTRY |  | 200 | g/L | QUANTITATIVE | MASS CONCENTRATION |  |  |  |  | 200 |  | g/L |  |  |  |  |  |  | 21482-5 | URINE |  |  | Y |  |  |  | 1 | Week 1 | 1999-06-19 |  | PT24H |
| 10 | ABC | LB | ABC-001-001 | 10 |  | PLATAGGR | Platelet Aggregation | COLLAGEN INDUCED | COAGULATION |  | NORMAL |  | ORDINAL | PRESENCE OR THRESHOLD |  |  |  |  | NORMAL |  |  |  |  |  |  |  |  | 24379-0 | PLATELET RICH PLASMA |  |  | Y |  |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 11 | ABC | LB | ABC-001-001 | 11 |  | WBC | Leukocytes |  | HEMATOLOGY |  | 5.9 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION |  |  |  |  | 5.9 | 5.9 | 10^9/L | 4 | 11 |  |  |  |  | 6690-2 | BLOOD | AUTOMATED COUNT |  | Y | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 12 | ABC | LB | ABC-001-001 | 12 |  | LYMLE | Lymphocytes/Leukocytes |  | HEMATOLOGY | DIFFERENTIAL | 6.7 | % | QUANTITATIVE | NUMBER FRACTION |  |  |  |  | 6.7 | 6.7 | % | 25 | 40 |  | LOW |  |  | 736-9 | BLOOD | AUTOMATED COUNT |  | Y | Y |  | N | 1 | Week 1 | 1999-06-19 | Y |  |
| 13 | ABC | LB | ABC-001-001 | 13 |  | NEUT | Neutrophils |  | HEMATOLOGY | DIFFERENTIAL | 5.1 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION |  |  |  |  | 5.1 | 5.1 | 10^9/L | 2 | 8 |  |  |  |  | 751-8 | BLOOD | AUTOMATED COUNT |  | Y | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 14 | ABC | LB | ABC-001-001 | 14 |  | PH | pH |  | URINALYSIS |  | 7.5 |  | QUANTITATIVE | LOG SUBSTANCE CONCENTRATION |  |  |  |  | 7.5 |  |  | 5.0 | 9.0 |  |  |  |  | 5803-2 | URINE | TEST STRIP |  | Y | Y |  |  | 1 | Week 1 | 1999-06-19 | Y |  |
| 15 | ABC | LB | ABC-001-001 | 15 |  | ALB | Albumin |  | CHEMISTRY |  |  |  | QUANTITATIVE | MASS CONCENTRATION |  |  |  |  |  |  |  |  |  |  |  | NOT DONE | INSUFFICIENT SAMPLE | 2862-1 | SERUM | ELECTROPHORESIS |  |  |  |  |  | 2 | Week 2 | 1999-07-21 | Y |  |
| 16 | ABC | LB | ABC-001-001 | 16 |  | CHOL | Cholesterol |  | CHEMISTRY |  | 229 | mg/dL | QUANTITATIVE | MASS CONCENTRATION |  | 0 |  |  | 229 | 229 | mg/dL | 0 | 199 |  | ABNORMAL |  |  | 2093-3 | SERUM |  |  |  | Y |  |  | 2 | Week 2 | 1999-07-21 |  |  |
| 17 | ABC | LB | ABC-001-001 | 17 |  | WBC | Leukocytes |  | HEMATOLOGY |  | 5.9 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION |  |  |  |  | 5.9 | 5.9 | 10^9/L | 4 | 11 |  |  |  |  | 6690-2 | BLOOD | AUTOMATED COUNT |  |  |  |  |  | 2 | Week 2 | 1999-07-21 | Y |  |
| 18 | ABC | LB | ABC-001-001 | 18 |  | PROT | Protein |  | URINALYSIS |  | MODERATE |  | ORDINAL | PRESENCE OR THRESHOLD |  |  |  |  | MODERATE |  |  |  |  | NEGATIVE to TRACE |  |  |  | 20454-5 | URINE | TEST STRIP |  |  |  |  | N | 2 | Week 2 | 1999-07-21 |  |  |

**Example 2**
This example illustrates the use of timing variables for pre- and post-dose timed urine collections.
**Row 1:** Shows an example of a pre-dose urine collection interval (from 4 hours prior to dosing until 15 minutes prior to dosing) with a negative value for LBELTM that reflects the end of the interval in reference to the fixed reference LBTPTREF, the date of which is recorded in LBRFTDTC.
**Rows 2-3:** Show an example of post-dose urine collection intervals with values for LBELTM that reflect the end of the intervals in reference to the fixed reference LBTPTREF, the date of which is recorded in LBRFTDTC.
*lb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBORNRLO | LBORNRHI | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBNRIND | LBLOINC | LBSPEC | LBMETHOD | LBLOBXFL | VISITNUM | VISIT | LBDTC | LBENDTC | LBTPT | LBTPTNUM | LBELTM | LBTPTREF | LBRFTDTC | LBPTFL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | LB | ABC-001-001 | 1 | GLUC | Glucose | URINALYSIS | 7 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | 1 | 15 | 0.39 | 0.39 | mmol/L | 0.1 | 0.8 | NORMAL | 5792-7 | URINE | TEST STRIP | Y | 2 | INITIAL DOSING | 1999-06-19T04:00 | 1999-06-19T07:45 | Pre-dose | 1 | -PT15M | Dosing | 1999-06-19T08:00 |  |
| 2 | ABC | LB | ABC-001-001 | 2 | GLUC | Glucose | URINALYSIS | 11 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | 1 | 15 | 0.61 | 0.61 | mmol/L | 0.1 | 0.8 | NORMAL | 5792-7 | URINE | TEST STRIP |  | 2 | INITIAL DOSING | 1999-06-19T08:00 | 1999-06-19T16:00 | 0-8 hours after dosing | 2 | PT8H | Dosing | 1999-06-19T08:00 | Y |
| 3 | ABC | LB | ABC-001-001 | 3 | GLUC | Glucose | URINALYSIS | 9 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | 1 | 15 | 0.5 | 0.5 | mmol/L | 0.1 | 0.8 | NORMAL | 5792-7 | URINE | TEST STRIP |  | 2 | INITIAL DOSING | 1999-06-19T16:00 | 1999-06-20T00:00 | 8-16 hours after dosing | 3 | PT16H | Dosing | 1999-06-19T08:00 | Y |

**Example 3**
This example illustrates the use of LBSTAT and LBREASND when there is no data value reported in LBORRES.
**Row 1:** Shows a pregnancy test with an original result of "-" (negative sign) standardized to the text value "NEGATIVE" in LBSTRESC.
**Row 2:** Shows a pregnancy test that was not performed because the subject was male. The sponsor felt it was necessary to include a record documenting the reason why the test was not performed, rather than simply not including a record.
*lb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBSTRESC | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBLOBXFL | VISITNUM | VISIT | LBDTC | LBPTFL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | LB | ABC-001-001 | 1 | HCG | Choriogonadotropin Beta | CHEMISTRY | - |  | ORDINAL | PRESENCE OR THRESHOLD | NEGATIVE |  |  | 2106-3 | URINE | Y | 1 | BASELINE | 1999-06-19T04:00 | Y |
| 2 | ABC | LB | ABC-001-002 | 1 | HCG | Choriogonadotropin Beta | CHEMISTRY |  |  | ORDINAL | PRESENCE OR THRESHOLD |  | NOT DONE | NOT APPLICABLE (SUBJECT MALE) | 2106-3 | URINE |  | 1 | BASELINE | 1999-06-24T08:00 | Y |

**Example 4**
This example illustrates the use of the LBTSTOPO variable to identify the tests that screen, confirm, and quantify the presence of a substance.
**Row 1:** Shows cannabinoids are screened.
**Row 2:** Shows the previously detected cannabinoids are further confirmed in the subject.
**Row 3:** Shows the quantification of the cannabinoids.
*lb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | LBGRPID | LBSEQ | LBTESTCD | LBTEST | LBTSTOPO | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | LBLOINC | LBSPEC | LBMETHOD | LBLOBXFL | LBDTC | VISITNUM | VISIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | LB | ABC-001-001 | 1 | 1 | CANNAB | Cannabinoids | SCREEN | DRUG TOXICITY | POSITIVE |  | POSITIVE |  |  | 19287-2 | URINE | KINETIC MICROPARTICLE IMMUNOASSAY | Y | 2013-02-16 | 1 | Week 1 |
| 2 | ABC | LB | ABC-001-001 | 1 | 2 | CANNAB | Cannabinoids | CONFIRM | DRUG TOXICITY | POSITIVE |  | POSITIVE |  |  | 19289-8 | URINE | MASS SPECTROMETRY | Y | 2013-02-16 | 1 | Week 1 |
| 3 | ABC | LB | ABC-001-001 | 1 | 3 | CANNAB | Cannabinoids | QUANTIFY | DRUG TOXICITY | 271 | ug/L | 271 | 271 | ug/L | 42860-7 | URINE | GC/MS | Y | 2013-02-16 | 1 | Week 1 |

**Example 5**
This example illustrates the use of the LBBDAGNT variable for a single agent. Note: More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment, the target protein analytes interact with the binding agent. The use of the word "free" in the descriptions of rows 2 and 4 does not refer to the naturally occurring hepatocyte growth factor receptors or epidermal growth factor receptors, but rather to the receptors not bound to the binding agent. Representing the binding agent shows that what is being measured is the portion of the target receptors not bound to the binding agent, not the concentration of the receptors at their natural state.
**Row 1:** Shows the total amount of HGFR, both soluble and bound, to the target "ABC-8675309".
**Row 2:** Shows the amount of free HGFR not bound to the target "ABC-8675309" (i.e., a measure of the soluble analyte not bound to the target).
**Row 3:** Shows the total amount of EGFR, both soluble and bound, to the target "ABC-8675309".
**Row 4:** Shows the amount of free EGFR not bound to the target "ABC-8675309" (i.e., a measure of the soluble analyte not bound to the target).
*lb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBBDAGNT | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | LBSPEC | LBMETHOD | LBDTC | VISITNUM | VISIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | LB | ABC-123456 | 1 | HGFR | Hepatocyte Growth Factor Receptor | ABC-8675309 | TARGET ENGAGEMENT | 35 | ng/mL | 35 | 35 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 2 | ABC | LB | ABC-123456 | 2 | HGFRFR | Hepatocyte Growth Factor Receptor, Free | ABC-8675309 | TARGET ENGAGEMENT | 10 | ng/mL | 10 | 10 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 3 | ABC | LB | ABC-123456 | 3 | EGFR | Epidermal Growth Factor Receptor | ABC-8675309 | TARGET ENGAGEMENT | 100 | ng/mL | 100 | 100 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 4 | ABC | LB | ABC-123456 | 4 | EGFRFR | Epidermal Growth Factor Receptor, Free | ABC-8675309 | TARGET ENGAGEMENT | 20 | ng/mL | 20 | 20 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |

#### 6.3.5.7 Microbiology Domains

The microbiology domains include Microbiology Specimen (MB) and Microbiology Susceptibility (MS). The MB domain is used for the detection, identification, quantification, and other characterizations of microorganisms in subject samples, except for drug susceptibility testing. MS is used for representing data from drug-susceptibility testing on the organisms identified in MB. All non-host infectious organisms— including bacteria, viruses, fungi, and parasites—are appropriate for the microbiology domains.

##### 6.3.5.7.1 Microbiology Specimen (MB)

###### MB – Description/Overview
A findings domain that represents non-host organisms identified including bacteria, viruses, parasites, protozoa and fungi.


###### MB – Specification
mb.xpt, Microbiology Specimen — Findings. One record per microbiology specimen finding per time point per visit per subject, Tabulation.

**Structure:** One record per microbiology specimen finding per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | MB |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm |  |
| 5 | MBSEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | MBGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | MBREFID | Reference ID | Char | Identifier | Perm |  |
| 8 | MBSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | MBLNKID | Link ID | Char | Identifier | Perm |  |
| 10 | MBLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 11 | MBTESTCD | Microbiology Test or Finding Short Name | Char | Topic | Req | C120527 |
| 12 | MBTEST | Microbiology Test or Finding Name | Char | Synonym Qualifier | Req | C120528 |
| 13 | MBTSTDTL | Measurement, Test or Examination Detail | Char | Variable Qualifier | Perm | C174225 |
| 14 | MBCAT | Category | Char | Grouping Qualifier | Perm |  |
| 15 | MBSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |
| 16 | MBORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 17 | MBORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 18 | MBSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 19 | MBSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 20 | MBSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 21 | MBRESCAT | Result Category | Char | Variable Qualifier | Perm |  |
| 22 | MBSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 23 | MBREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 24 | MBNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |
| 25 | MBLOINC | LOINC Code | Char | Synonym Qualifier | Perm |  |
| 26 | MBSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C78734 |
| 27 | MBSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 28 | MBLOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |
| 29 | MBLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 30 | MBDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 31 | MBMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |
| 32 | MBLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 33 | MBBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 34 | MBFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| 35 | MBDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 36 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 37 | VISIT | Visit Name | Char | Timing | Perm |  |
| 38 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 39 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 40 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 41 | MBDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 42 | MBDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 43 | MBTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 44 | MBTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 45 | MBELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 46 | MBTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 47 | MBRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **FOCID**: Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. The value in this variable should have inherent semantic meaning.
- **MBSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.
- **MBGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **MBREFID**: Internal or external specimen identifier (e.g., sample ID for a subject sample from which a microbial culture was generated).
- **MBSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.
- **MBLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed.
- **MBLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **MBTESTCD**: Short name of the measurement, test, or finding described in MBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MCORGIDN" for Microbial Organism Identification "GMNCOC" for Gram Negative Cocci.
- **MBTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in MBTEST cannot be longer than 40 characters. Examples: "Microbial Organism Identification", "Gram Negative Cocci", "HIV-1 RNA".
- **MBTSTDTL**: Further description of MBTESTCD and MBTEST. Example: "VIRAL LOAD" when MBTESTCD represents viral genetic material, such as "HCRNA", "QUANTIFICATION" when MBTESTCD represents any organism being quantified.
- **MBCAT**: Used to define a category of related records.
- **MBSCAT**: Used to define a further categorization of MBCAT values.
- **MBORRES**: Result of the microbiology measurement or finding as originally received or collected. Examples for "GRAM STAIN" findings: "+3 MODERATE", "+2 FEW", "<10". Examples for "CULTURE PLATE" findings: "KLEBSIELLA PNEUMONIAE", "STREPTOCOCCUS PNEUMONIAE".
- **MBORRESU**: Original unit for MBORRES. Example: "mcg/mL".
- **MBSTRESC**: Contains the result value for all findings copied or derived from MBORRES, in a standard format or standard units. MBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MBSTRESN. For example, if a test has results "+3 MODERATE", "MOD", and "MODERATE" in MBORRES and these results effectively have the same meaning, they could be represented in standard format in MBSTRESC as "MODERATE".
- **MBSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from MBSTRESC. MBSTRESN should store all numeric test results or findings.
- **MBSTRESU**: Standardized units used for MBSTRESC and MBSTRESN.
- **MBRESCAT**: Used to categorize the result of a finding in a standard format.
- **MBSTAT**: Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **MBREASND**: Reason not done. Used in conjunction with MBSTAT when value is NOT DONE. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED".
- **MBNAM**: Name or identifier of the vendor (e.g., laboratory) that provided the test results.
- **MBLOINC**: Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable (e.g., lab test).
- **MBSPEC**: Defines the type of specimen used for a measurement. Examples: "SPUTUM", "BLOOD", "PUS".
- **MBSPCCND**: Free or standardized text describing the condition of the specimen. Example: "CONTAMINATED".
- **MBLOC**: Anatomical location relevant to the collection of the measurement.
- **MBLAT**: Qualifier for specimen collection location further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **MBDIR**: Qualifier for specimen collection location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **MBMETHOD**: Method of the test or examination. Examples: "GRAM STAIN", "MICROBIAL CULTURE, LIQUID", "QUANTITATIVE REVERSE TRANSCRIPTASE POLYMERASE CHAIN REACTION".
- **MBLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **MBBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that MBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **MBFAST**: Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant.
- **MBDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element which the specimen collection occurred.
- **EPOCH**: Epoch associated with the date/time at which the specimen was collected.
- **MBDTC**: Date/time of specimen collection.
- **MBDY**: Study day of the specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.
- **MBTPT**: Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MBTPTNUM and MBTPTREF. Examples: "Start", "5 min post".
- **MBTPTNUM**: Numeric version of MBTPT used in sorting.
- **MBELTM**: Planned elapsed time (in ISO 8601) relative to a planned fixed reference (MBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by MBTPTREF, or "PT8H" to represent the period of 8 hours after the reference point indicated by MBTPTREF.
- **MBTPTREF**: Name of the fixed reference point referred to by MBELTM, MBTPTNUM, and MBTPT. Example: "PREVIOUS DOSE".
- **MBRFTDTC**: Date/time for a fixed reference time point, MBTPTREF.

###### MB – Assumptions
1. Representation of findings in the Microbiology Specimen domain should be handled as follows:
    a. In cases of tests that target an organism, group of organisms, or antigen for identification, MBTEST equals the name of the organism/antigen targeted by the identification assay, and
        i. MBTSTDTL should be “DETECTION”.
        ii. The result should generally be “PRESENT”/”ABSENT”, “POSITIVE”/”NEGATIVE”, or “INDETERMINATE”. However, there may be cases where a test differentiates between 2 or more similar organisms, in which case it would be appropriate for the result to be the name of the organism detected. For example, a test may look for influenza A or influenza B antigen. In this case, MBTEST would be “Influenza A/B Antigen”; the result could be “INFLUENZA A ANTIGEN”, “INFLUENZA B ANTIGEN”, or “INFLUENZA A/B ANTIGEN”.
    b. For non-targeted identification of organisms (i.e., tests that have the ability to identify a range of organisms without specifically targeting any), the value for MBTESTCD/MBTEST should be “MCORGIDN”/”Microbial Organism Identification”, and the result should be the name of the organism or group of organisms found to be present (e.g., “INFLUENZA A VIRUS SUBTYPE H1N1”; “CLONORCHIS SINENSIS”). In this scenario MBORRES is populated with values from the Microorganism Codelist (C85491).
    c. Culture characteristics covers concepts such as growth/no growth, colony quantification measures, colony color, colony morphology, and so on. Note that this does not include drug susceptibility testing, which is represented in the Microbiology Susceptibility (MS) domain.
        i. MBTESTCD/MBTEST should be the name of the organism or group of organisms being characterized.
        ii. MBTSTDTL should be the name of the characteristic being described (e.g., “COLONY COUNT”, “VIRAL LOAD”).
        iii. MBGRPID should be used to group characteristic records with the identification record of the organism to which the characteristics apply.
        iv. CDISC Controlled Terminology Rules for Microbiology (MB/MS) domains are available at https://www.cdisc.org/standards/terminology/controlled-terminology.
2. MBDTC represents the date the specimen was collected.
3. If the specimen was cultured, the start and end date of culture are represented in the Biospecimen Events (BE) domain in BESTDTC and BEENDTC respectively. The variable --REFID represents the sample ID as originally assigned in the BE domain. See BE domain assumptions in the SDTMIG v3.4, section 6.2.2, for guidelines on assigning --REFID values to samples and subsamples.
    a. Culture dates can be connected to the MB record via MBREFID and BEREFID.
    b. If the same sample is associated with many biospecimen events and tests, users may need to make use of additional linking variables such as --LNKID.
4. The variable NHOID is not allowed for use in the MB domain. Any additional Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MB domain, but the following variables would not generally be used: --MODIFY, --BODSYS, --FAST, --TOX, --TOXGR, --SEV.

##### 6.3.5.7.2 Microbiology Susceptibility (MS)

###### MS – Description/Overview
A findings domain that represents drug susceptibility testing results only. This includes phenotypic testing (where drug is added directly to a culture of organisms) and genotypic tests that provide results in terms of susceptible or resistant. Drug susceptibility testing may occur on a wide variety of non-host organisms, including bacteria, viruses, fungi, protozoa and parasites.

###### MS – Specification
ms.xpt, Microbiology Susceptibility — Findings. One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB, Tabulation.

**Structure:** One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | MS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | NHOID | Non-host Organism ID | Char | Identifier | Perm |  |
| 5 | MSSEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | MSGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | MSREFID | Reference ID | Char | Identifier | Perm |  |
| 8 | MSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | MSLNKID | Link ID | Char | Identifier | Perm |  |
| 10 | MSTESTCD | Short Name of Assessment | Char | Topic | Req | C128688 |
| 11 | MSTEST | Name of Assessment | Char | Synonym Qualifier | Req | C128687 |
| 12 | MSAGENT | Agent Name | Char | Variable Qualifier | Exp |  |
| 13 | MSCONC | Agent Concentration | Num | Variable Qualifier | Perm |  |
| 14 | MSCONCU | Agent Concentration Units | Char | Variable Qualifier | Perm | C71620 |
| 15 | MSTSTDTL | Measurement, Test or Examination Detail | Char | Variable Qualifier | Perm |  |
| 16 | MSCAT | Category | Char | Grouping Qualifier | Perm |  |
| 17 | MSSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |
| 18 | MSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 19 | MSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 20 | MSSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 21 | MSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 22 | MSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 23 | MSNRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |
| 24 | MSRESCAT | Result Category | Char | Variable Qualifier | Perm | C85495 |
| 25 | MSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 26 | MSREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 27 | MSXFN | External File Path | Char | Record Qualifier | Perm |  |
| 28 | MSNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |
| 29 | MSLOINC | LOINC Code | Char | Synonym Qualifier | Perm |  |
| 30 | MSSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C78734 |
| 31 | MSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 32 | MSLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| 33 | MSLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 34 | MSDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 35 | MSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 36 | MSANMETH | Analysis Method | Char | Record Qualifier | Perm |  |
| 37 | MSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 38 | MSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 39 | MSFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| 40 | MSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 41 | MSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 42 | MSEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 43 | MSACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| 44 | MSLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm |  |
| 45 | MSULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm |  |
| 46 | MSREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |
| 47 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 48 | VISIT | Visit Name | Char | Timing | Perm |  |
| 49 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 50 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 51 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 52 | MSDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 53 | MSDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 54 | MSDUR | Duration | Char | Timing | Perm | ISO 8601 duration |
| 55 | MSTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 56 | MSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 57 | MSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 58 | MSTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 59 | MSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| 60 | MSEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |
| 61 | MSEVINTX | Evaluation Interval Text | Char | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **NHOID**: Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.
- **MSSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.
- **MSGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain. In SDTMIG v3.2 this was an Expected variable. In this version, the core designation has been changed to Permissible.
- **MSREFID**: Optional internal or external identifier (e.g., an identifier for the culture/isolate being tested for susceptibility).
- **MSSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.
- **MSLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed.
- **MSTESTCD**: Short character value for MSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MIC" for Minimum Inhibitory Concentration; "MICROSUS" for Microbial Susceptibility.
- **MSTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in MSTEST cannot be longer than 40 characters. Examples: "Minimum Inhibitory Concentration", "Microbial Susceptibility".
- **MSAGENT**: The name of the agent for which resistance is tested. The agent specified may be based on genetic markers or direct phenotypic drug sensitivity testing. Examples: "Penicillin", name of study drug.
- **MSCONC**: Numeric concentration of agent listed in MSAGENT.
- **MSCONCU**: Units for value of the agent concentration listed in MSCONC. Example: "mg/L".
- **MSTSTDTL**: Further description of MSTESTCD and MSTEST.
- **MSCAT**: Used to define a category of MSTEST values.
- **MSSCAT**: Used to define a further categorization of MSCAT values.
- **MSORRES**: Result of the measurement or finding as originally received or collected.
- **MSORRESU**: Unit for MSORRES. Examples: "ug/mL".
- **MSSTRESC**: Contains the result value for all findings, copied or derived from MSORRES in a standard format or in standard units. MSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MSSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MSORRES and these results effectively have the same meaning, they could be represented in standard format in MSSTRESC as "NEGATIVE".
- **MSSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from MSSTRESC. MSSTRESN should store all numeric test results or findings.
- **MSSTRESU**: Standardized units used for MSSTRESC and MSSTRESN. Example: "mol/L".
- **MSNRIND**: Used to indicate the value is outside the normal range or reference range. May be defined by MSORNRLO and MSORNRHI or other objective criteria. Examples: "Y", "N", "HIGH", "LOW", "NORMAL". "ABNORMAL".
- **MSRESCAT**: Used to categorize the result of a finding. In SDTMIG v3.2, MSRESCAT was used to categorize a numeric susceptibility result represented in MSORRES as either "SUSCEPTIBLE", "INTERMEDIATE", or "RESISTANT". However, results from some susceptibility tests may report only a categorical result and not a numeric result. Thus, in order for susceptibility results to be represented consistently, MSRESCAT should no longer be used for this purpose. In this version, the core designation has been changed from Expected to Permissible.
- **MSSTAT**: Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **MSREASND**: Reason not done. Used in conjunction with MSSTAT when value is "NOT DONE".
- **MSXFN**: Filename for an external file.
- **MSNAM**: Name or identifier of the vendor (e.g., laboratory) that provided the test results.
- **MSLOINC**: Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable such as a lab test.
- **MSSPEC**: Defines the type of specimen used for a measurement. Example: "SPUTUM".
- **MSSPCCND**: Defines the condition of the specimen. Example: "CLOUDY".
- **MSLOC**: Anatomical location of the subject relevant to the collection of the measurement.
- **MSLAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **MSDIR**: Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **MSMETHOD**: Method of the test or examination. Examples: "EPSILOMETER", "MACRO BROTH DILUTION".
- **MSANMETH**: Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., an image or a genetic sequence).
- **MSLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **MSBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that MSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **MSFAST**: Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant.
- **MSDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **MSEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "MICROSCOPIST".
- **MSEVALID**: Used to distinguish multiple evaluators with the same role recorded in MSEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".
- **MSACPTFL**: In cases where more than 1 assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null.
- **MSLLOQ**: Indicates the lower limit of quantitation for an assay. Units will be those used for MSSTRESU.
- **MSULOQ**: Indicates the upper limit of quantitation for an assay. Units will be those used for MSSTRESU.
- **MSREPNUM**: The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the specimen was collected.
- **EPOCH**: Epoch associated with the date/time at which the specimen was collected.
- **MSDTC**: Collection date and time of an observation.
- **MSDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **MSDUR**: Collected duration of an event, intervention, or finding. Used only if collected on the CRF and not derived.
- **MSTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See MSTPTNUM and MSTPTREF.
- **MSTPTNUM**: Numeric version of planned time point used in sorting.
- **MSELTM**: Planned elapsed time relative to a planned fixed reference (MSTPTREF; e.g., previous dose, previous meal). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **MSTPTREF**: Description of the fixed reference point referred to by MSELTM, MSTPTNUM, and MSTPT. Example: "PREVIOUS DOSE".
- **MSRFTDTC**: Date/time for a fixed reference time point defined by MSTPTREF.
- **MSEVLINT**: Duration of interval associated with an observation such as a finding MSTESTCD. Example: "-P2M" to represent a period of the past 2 months before the assessment.
- **MSEVINTX**: Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".


###### MS – Assumptions
1. Microbiology Susceptibility testing includes testing of the following types:
    a. Phenotypic drug susceptibility testing (qualitative), which may involve determining susceptibility/resistance (qualitative) at a predefined concentration of drug, or determining a specific dose (quantitative) at which a drug inhibits organism growth or some other process associated with virulence.
        i. For studies using qualitative testing methods, MSAGENT, MSCONC, and MSCONCU are used to represent the predefined drug, concentration, and units, respectively. Results are represented with values such as “SUSCEPTIBLE” or “RESISTANT”.
        ii. For studies using quantitative testing methods, MSAGENT is used to represent the drug being tested; MSCONC and MSCONCU are not used. The concentration at which growth is inhibited is the result in these cases (MSORRES, MSSTRESC/MSSTRESN), with units being represented in MSORRESU/MSSTRESU.
    b. Genetic tests that provide results in terms of susceptible/resistant only (e.g., nucleic acid amplification tests (NAAT)). Genotypic tests that provide results in terms of specific changes to nucleotides, codons, or amino acids of genes/gene products associated with resistance should be represented in the Genomic Findings (GF) domain, as that domain structure contains the variables necessary to accommodate data of this type. If a test provides both mutation data and susceptibility data, the mutation results should be represented in GF and the susceptibility information should be represented in MS. In these cases, the GF records should be linked via RELREC to susceptibility records in MS.
        i. As in 1.a.ii, MSAGENT should be populated with the drug whose action would be affected by the genetic marker being assessed via the genotypic test. MSCONC and MSCONCU are null in these records.
    c. CDISC Controlled Terminology Rules for Microbiology (MB/MS) domains are available at https://www.cdisc.org/standards/terminology/controlled-terminology.
2. MSDTC represents the date the specimen was collected.
3. If the specimen was cultured, the start and end date of culture are represented in the Biospecimen Events (BE) domain in BESTDTC and BEENDTC, respectively. --REFID represents the sample ID as originally assigned in the BE domain. See BE domain assumptions in the SDTMIG v3.4, Section 6.2.2, for guidelines on assigning --REFID values to samples and subsamples.
    a. Culture dates can be connected to the MS record via MSREFID and BEREFID.
    b. If the same sample is associated with many biospecimen events and tests, users may need to make use of additional linking variables such as --LNKID.
4. NHOID is a sponsor-defined, intuitive name of the non-host organism being tested. It should only populated with values representing what is known about the identity of the organism before the results of the test are determined. It should therefore never be used as a qualifier of result.
5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MS domain, but the following variables would not generally be used: --MODIFY, --BODSYS, --TOX, --TOXGR, --SEV.

##### 6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples

**Example 1**
In this example, both a central and a local lab (MBNAM) independently identified Enterococcus faecalis (MBORRES) in a fluid specimen (MBSPEC) taken from the skin (MBLOC) of a subject at visit 1. The method used by both labs was a solid microbial culture (MBMETHOD). Because the culture was not targeted to encourage the growth of a specific organism, MBTESTCD/MBTEST = "MCORGIDN"/"Microbial Organism Identification" and MBORRES represents the name of the organism identified.
*mb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBLNKID | MBTESTCD | MBTEST | MBORRES | MBSTRESC | MBNAM | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-001-002 | 1 | SPEC01 | 1 | MCORGIDN | Microbial Organism Identification | ENTEROCOCCUS FAECALIS | ENTEROCOCCUS FAECALIS | CENTRAL LAB ABC | FLUID | SKIN | MICROBIAL CULTURE, SOLID | 1 | VISIT 1 | 2005-07-21T08:00 |
| 2 | ABC | MB | ABC-001-002 | 2 | SPEC01 | 2 | MCORGIDN | Microbial Organism Identification | ENTEROCOCCUS FAECALIS | ENTEROCOCCUS FAECALIS | LOCAL LAB XYZ | FLUID | SKIN | MICROBIAL CULTURE, SOLID | 1 | VISIT 1 | 2005-07-21T08:00 |

After E. faecalis was identified in the subject sample, drug susceptibility testing was performed at each of the labs using both the sponsor's investigational drug and amoxicillin. Because an identified organism is the subject of the test, the NHOID variable is populated with "ENTEROCOCCUS FAECALIS". Between the 2 labs (MSNAM), a total of 3 susceptibility testing methods were used: epsilometer, disk diffusion, and macro broth dilution (MSMETHOD). Epsilometer and disk diffusion both use agar diffusion methods, in which an agar plate is inoculated with the microorganism of interest and either a strip (epsilometer) or discs (disk diffusion) containing various concentrations of the drug are placed on the agar plate. The epsilometer test method provides both a minimum inhibitory concentration (MSTESTCD = "MIC"), the lowest concentration of a drug that inhibits the growth of a microorganism, and a qualitative interpretation (MSTESTCD = "MICROSUS") such as susceptible, intermediate, or resistant. The disk diffusion test method provides the diameter of the zone of inhibition (MSTESTCD = "DIAZOINH") and a qualitative interpretation such as susceptible, intermediate, or resistant (MSTESTCD = "MICROSUS"). The quantitative and qualitative results are grouped together using MSGRPID.
The third method, macro broth dilution, was used to test the specimen at a predefined drug concentration of each of the drugs. When the drug and amount are a predefined part of the test, the variable MSAGENT is populated with the name of the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used.
**Rows 1-4:** Show the minimum inhibitory concentration and the interpretation result reported from Central Lab ABC from a sample that was tested for susceptibility to the sponsor drug and amoxicillin, using an epsilometer test method.
**Rows 5-6:** Show that Local Lab XYZ found that the sample was susceptible to the sponsor drug at a concentration of 0.5 ug/dL and resistant to amoxicillin at a concentration of 0.5 ug/dL.
**Rows 7-10:** Show the diameter of the zone of inhibition and the interpretation result reported from Local Lab XYZ from a sample that was tested for susceptibility to the sponsor drug and amoxicillin using a disk diffusion test method.
*ms.xpt*

| Row | STUDYID | DOMAIN | USUBJID | NHOID | MSGRPID | MSSEQ | MSREFID | MSLNKGRP | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSORRESU | MSSTRESC | MSSTRESN | MSSTRESU | MSNAM | MSMETHOD | MSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 1 | 1 | SPEC01 | 1 | MIC | Minimum Inhibitory Concentration | Sponsor Drug |  |  | 0.25 | ug/dL | 0.25 | 0.25 | ug/dL | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 2 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 1 | 2 | SPEC01 | 1 | MICROSUS | Microbial Susceptibility | Sponsor Drug |  |  | SUSCEPTIBLE |  | SUSCEPTIBLE |  |  | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 3 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 2 | 3 | SPEC01 | 1 | MIC | Minimum Inhibitory Concentration | Amoxicillin |  |  | 1 | ug/dL | 1 | 1 | ug/dL | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 4 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 2 | 4 | SPEC01 | 1 | MICROSUS | Microbial Susceptibility | Amoxicillin |  |  | RESISTANT |  | RESISTANT |  |  | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 5 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS |  | 5 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Sponsor Drug | 0.5 | ug/dL | SUSCEPTIBLE |  | SUSCEPTIBLE |  |  | LOCAL LAB XYZ | MACRO BROTH DILUTION | 2005-06-19T08:00 |
| 6 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS |  | 6 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Amoxicillin | 0.5 | ug/dL | RESISTANT |  | RESISTANT |  |  | LOCAL LAB XYZ | MACRO BROTH DILUTION | 2005-06-19T08:00 |
| 7 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 3 | 7 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Sponsor Drug |  |  | 23 | mm | 23 | 23 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00 |
| 8 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 3 | 8 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Sponsor Drug |  |  | SUSCEPTIBLE |  | SUSCEPTIBLE |  |  | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00 |
| 9 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 4 | 9 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Amoxicillin |  |  | 25 | mm |  | 25 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00 |
| 10 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 4 | 10 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Amoxicillin |  |  | RESISTANT |  | RESISTANT |  |  | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00 |

Although not expected, the sponsor decided to connect the identification records in MB to the records in MS using the variables MBLNKID and MSLNKGRP.
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB |  | MBLNKID |  | ONE | A |
| 2 | ABC | MS |  | MSLNKGRP |  | MANY | A |

**Example 2**
In this example, a sputum sample, collected from the subject at 3 visits over the course of 15 days, was tested for the presence of infectious organisms. The 2 organisms identified were also tested for susceptibility to both penicillin and the sponsor's study drug (MSAGENT). The example shows that the 2 infecting organisms were cleared over the course of the 3 visits.
Specimen collection was represented in the Biospecimen Events (BE) domain.
*be.xpt*

| Row | STUDYID | DOMAIN | USUBJID | BESEQ | BEREFID | BETERM | BEDTC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | BE | ABC-001-001 | 1 | SP01 | Collecting | 2005-06-19T08:00 |
| 2 | ABC | BE | ABC-001-001 | 2 | SP02 | Collecting | 2005-06-26T08:00 |
| 3 | ABC | BE | ABC-001-001 | 3 | SP03 | Collecting | 2005-07-06T08:00 |

The SUPPBE dataset is used to represent 2 non-standard variables of BE.
**Rows 1-3:** Show that all 3 samples (IDVARVAL where IDVAR="BEREFID") were sputum, as indicated by QVAL where QNAM="BESPEC" and QLABEL="Specimen Type".
**Rows 4-6:** Show that all 3 sputum samples were collected via expectoration, as indicated by QVAL where QNAM="Specimen Collection Method". QVAL is populated using the CDISC Controlled Terminology codelist, "Specimen Collection Method".
*suppbe.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | BE | ABC-01-101 | BEREFID | SP01 | BESPEC | Specimen Type | SPUTUM | CRF |
| 2 | ABC | BE | ABC-01-101 | BEREFID | SP02 | BESPEC | Specimen Type | SPUTUM | CRF |
| 3 | ABC | BE | ABC-01-101 | BEREFID | SP03 | BESPEC | Specimen Type | SPUTUM | CRF |
| 4 | ABC | BE | ABC-01-101 | BEREFID | SP01 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |
| 5 | ABC | BE | ABC-01-101 | BEREFID | SP02 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |
| 6 | ABC | BE | ABC-01-101 | BEREFID | SP03 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |

**Rows 1-2:** Show that a gram stain was used on a subject sputum sample to identify the presence of gram negative cocci (row 1) and to quantify the bacteria (row 2). MBORRES in row 2 represents an ordinal result (MBRSLSCL = "Ord"), such as from a published quantification scale. This value decodes to "FEW" as shown in MBSTRESC. The quantification scale used is represented as Supplemental Qualifiers of MB.
**Rows 3-4:** Show that the same gram-stained sample was used to identify and quantify the presence of gram negative rods.
**Rows 5-6:** Show that microbial culture of the same sample was used at the same visit to identify the presence of two organisms, "STREPTOCOCCUS PNEUMONIAE" and "KLEBSIELLA PNEUMONIAE" (MBORRES).
**Row 7:** Shows that microbial culture of a subsequent sample at a later visit indicated only the presence of "KLEBSIELLA PNEUMONIAE" (MBORRES).
**Row 8:** Shows that microbial culture of a third subject sample at the third visit indicated "NO GROWTH" (MBORRES) of any organisms.
*mb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBRSLSCL | MBSTRESC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-001-001 | 1 | SP01 | GMNCOC | Gram Negative Cocci | DETECTION | PRESENT | Ord | PRESENT | LUNG | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 2 | ABC | MB | ABC-001-001 | 2 | SP01 | GMNCOC | Gram Negative Cocci | CELL COUNT | 2+ | Ord | FEW | LUNG | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 3 | ABC | MB | ABC-001-001 | 3 | SP01 | GMNROD | Gram Negative Rods | DETECTION | PRESENT | Ord | PRESENT | LUNG | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 4 | ABC | MB | ABC-001-001 | 4 | SP01 | GMNROD | Gram Negative Rods | CELL COUNT | 2+ | Ord | FEW | LUNG | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 5 | ABC | MB | ABC-001-001 | 5 | SP01 | MCORGIDN | Microbial Organism Identification |  | STREPTOCOCCUS PNEUMONIAE | Nom | STREPTOCOCCUS PNEUMONIAE | LUNG | MICROBIAL CULTURE, SOLID | 1 | VISIT 1 | 2005-06-19T08:00 |
| 6 | ABC | MB | ABC-001-001 | 6 | SP01 | MCORGIDN | Microbial Organism Identification |  | KLEBSIELLA PNEUMONIAE | Nom | KLEBSIELLA PNEUMONIAE | LUNG | MICROBIAL CULTURE, SOLID | 1 | VISIT 1 | 2005-06-19T08:00 |
| 7 | ABC | MB | ABC-001-001 | 7 | SP02 | MCORGIDN | Microbial Organism Identification |  | KLEBSIELLA PNEUMONIAE | Nom | KLEBSIELLA PNEUMONIAE | LUNG | MICROBIAL CULTURE, SOLID | 2 | VISIT 2 | 2005-06-26T08:00 |
| 8 | ABC | MB | ABC-001-001 | 8 | SP03 | MCORGIDN | Microbial Organism Identification |  | NO GROWTH | Nom | NO GROWTH | LUNG | MICROBIAL CULTURE, SOLID | 3 | VISIT 3 | 2005-07-06T08:00 |

*suppmb.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-01-101 | MBTSTDTL | CELL COUNT | MBQSCAL | Quantification Scale | CDC semi-quantitative score for gram staining | CRF |

**Rows 1-2:** Show that the sponsor drug (MSAGENT) was tested against "STREPTOCOCCUS PNEUMONIAE" (NHOID) from subject sample SP01 and that the drug has a minimum inhibitory concentration (MSTESTCD/MSTEST) of 0.004 mg/L (row 1). This led to the conclusion that this organism is susceptible to that drug (row 2).
**Rows 3-4:** Show that penicillin was tested against the same organism from the same sample and was found to have a minimum inhibitory concentration of 0.023 mg/L (row 3). This led to the conclusion that "STREPTOCOCCUS PNEUMONIAE" is resistant to penicillin (row 4).
**Rows 5-8:** Similar to rows 1-4, the sponsor drug (rows 5-6) and penicillin (rows 7-8) were tested against "KLEBSIELLA PNEUMONIAE" from an additional sample from the same subject at a later time point. Results from these tests indicated that the organism was susceptible to sponsor drug, yet had intermediate resistance to penicillin.
**Rows 9-10:** A test against "KLEBSIELLA PNEUMONIAE" from an additional sample at a later time point showed little change in the minimum inhibitory concentration of penicillin, and that the organism was still classified as having intermediate resistance to this drug.
*ms.xpt*

| Row | STUDYID | DOMAIN | USUBJID | NHOID | MSSEQ | MSREFID | MSGRPID | MSTESTCD | MSTEST | MSAGENT | MSORRES | MSORRESU | MSSTRESC | MSSTRESN | MSSTRESU | MSMETHOD | MSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | 1 | SP01 | 1 | MIC | Minimum Inhibitory Concentration | Sponsor Drug | 0.004 | mg/L | 0.004 | 0.004 | mg/L | EPSILOMETER | 2005-06-19T08:00 |
| 2 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | 2 | SP01 | 1 | MICROSUS | Microbial Susceptibility | Sponsor Drug | SUSCEPTIBLE |  | SUSCEPTIBLE |  |  | EPSILOMETER | 2005-06-19T08:00 |
| 3 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | 3 | SP01 | 2 | MIC | Minimum Inhibitory Concentration | Penicillin | 0.023 | mg/L | 0.023 | 0.023 | mg/L | EPSILOMETER | 2005-06-19T08:00 |
| 4 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | 4 | SP01 | 2 | MICROSUS | Microbial Susceptibility | Penicillin | RESISTANT |  | RESISTANT |  |  | EPSILOMETER | 2005-06-19T08:00 |
| 5 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | 5 | SP02 | 3 | MIC | Minimum Inhibitory Concentration | Sponsor Drug | 0.125 | mg/L | 0.125 | 0.125 | mg/L | EPSILOMETER | 2005-06-26T08:00 |
| 6 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | 6 | SP02 | 3 | MICROSUS | Microbial Susceptibility | Sponsor Drug | SUSCEPTIBLE |  | SUSCEPTIBLE |  |  | EPSILOMETER | 2005-06-26T08:00 |
| 7 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | 7 | SP02 | 4 | MIC | Minimum Inhibitory Concentration | Penicillin | 0.023 | mg/L | 0.023 | 0.023 | mg/L | EPSILOMETER | 2005-06-26T08:00 |
| 8 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | 8 | SP02 | 4 | MICROSUS | Microbial Susceptibility | Penicillin | INTERMEDIATE |  | INTERMEDIATE |  |  | EPSILOMETER | 2005-06-26T08:00 |
| 9 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | 9 | SP03 | 5 | MIC | Minimum Inhibitory Concentration | Penicillin | 0.026 | mg/L | 0.026 | 0.026 | mg/L | EPSILOMETER | 2005-07-06T08:00 |
| 10 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | 10 | SP03 | 5 | MICROSUS | Microbial Susceptibility | Penicillin | INTERMEDIATE |  | INTERMEDIATE |  |  | EPSILOMETER | 2005-07-06T08:00 |

**Example 3**
This example shows the microorganisms detected from a gastric aspirate specimen from a child with suspected tuberculosis (TB). In this example, gastric lavage is only performed once. Three records in the MB domain store detection records for 2 levels of detection: acid-fast bacilli, and Mycobacterium tuberculosis (Mtb). Characteristics from a culture on solid media that support the presumptive detection of Mtb are also represented in MB. The susceptibility results from both the nucleic acid amplification test (NAAT) and the solid culture are represented in the MS domain.
Specimen processing events included sample collection, preparation, and culturing; these events are represented in the BE domain. For TB studies, each sample needs a separate identifier to link it to further actions or characteristics of the sample. Therefore, each aliquot is assigned a unique BEREFID value that can be traced to the BEREFID value assigned to the collected "parent" sample. BEREFID is also used to connect the BE and Biospecimen Findings (BS) domains (via BSREFID), as well as any results obtained from the sample that are in the MB or MS domains (via MBREFID and MSREFID). If the same sample is used in many tests, the use of --REFID may result in a potentially undesirable many-to-many merge; users may need to make use of additional linking variables such as --LNKID and --LNKGRP. Information about the BE and BS domains including the specification tables, assumptions, and examples can be found in the Sections 6.2.2 and 6.3.5.2 of this document.
In the BE, BS, MB, and MS domains, --DTC represents the date of sample collection. --LNKID and --LNKGRP are used to link culture start and stop dates (BE) with culture results (MB and MS).
**Row 1:** Shows the event of specimen collection. This is the genesis of the sample identified by BEREFID="100"; therefore, BEDTC and BESTDTC are the same. The specimen collection setting, collection method, and specimen type are represented using supplemental qualifiers. Even though the variable Specimen Type is available for use in Findings domains, it is not available for use in Events domains and thus it is represented as supplemental qualifier.
**Rows 2-6:** Show that the sample was aliquoted (i.e., smaller subsamples were portioned out from the parent sample) and each separate aliquot assigned a unique BEREFID. In such cases, BEREFID is an incremented decimal value with the original sample's BEREFID (when BECAT="COLLECTION") as the base number. (This is not an explicit requirement, but makes tracking the samples easier.) The definitive link between parent-child samples is defined by the PARENT variable shown in the RELSPEC dataset.
**Rows 7-9:** Show that 3 of the aliquots (100.3, 100.4, and 100.5) were cultured for detection (row 7) and tested for drug susceptibility (rows 8 and 9). The inoculation and read dates of a culture should be represented in BESTDTC and BEENDTC, respectively. These dates can be linked to the culture results in MB and MS using BELNKID, MBLNKGRP, and MSLNKID.
**Row 10:** Shows that sample 100.1 was concentrated.
*be.xpt*

| Row | STUDYID | DOMAIN | USUBJID | BESEQ | BEREFID | BELNKID | BETERM | BECAT | BEDTC | BESTDTC | BEENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | BE | ABC-01-101 | 1 | 100 |  | Collecting | COLLECTION | 2011-01-17T06:00 | 2011-01-17T06:00 |  |
| 2 | ABC | BE | ABC-01-101 | 2 | 100.1 |  | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 |  |
| 3 | ABC | BE | ABC-01-101 | 3 | 100.2 |  | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 |  |
| 4 | ABC | BE | ABC-01-101 | 4 | 100.3 |  | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 |  |
| 5 | ABC | BE | ABC-01-101 | 5 | 100.4 |  | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 |  |
| 6 | ABC | BE | ABC-01-101 | 6 | 100.5 |  | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 |  |
| 7 | ABC | BE | ABC-01-101 | 7 | 100.3 | 1 | Culturing | CULTURE | 2011-01-17T06:00 | 2011-01-17T09:30 | 2011-02-02T09:00 |
| 8 | ABC | BE | ABC-01-101 | 8 | 100.4 | 2 | Culturing | CULTURE | 2011-01-17T06:00 | 2011-02-02T10:00 | 2011-02-21T09:00 |
| 9 | ABC | BE | ABC-01-101 | 9 | 100.5 | 3 | Culturing | CULTURE | 2011-01-17T06:00 | 2011-02-02T10:00 | 2011-02-22T09:00 |
| 10 | ABC | BE | ABC-01-101 | 10 | 100.1 |  | Concentrating | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:15 |  |

*suppbe.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | BE | ABC-01-101 | BEREFID | 100 | BECLSET | Specimen Collection Setting | HOSPITAL | CRF |
| 2 | ABC | BE | ABC-01-101 | BEREFID | 100 | BECLMETH | Specimen Collection Method | GASTRIC LAVAGE | CRF |
| 3 | ABC | BE | ABC-01-101 | BEREFID | 100 | BESPEC | Specimen Type | LAVAGE FLUID | CRF |
| 4 | ABC | BE | ABC-01-101 | BEREFID | 100.1 | BESPEC | Specimen Type | LAVAGE FLUID | CRF |
| 5 | ABC | BE | ABC-01-101 | BEREFID | 100.2 | BESPEC | Specimen Type | LAVAGE FLUID | CRF |
| 6 | ABC | BE | ABC-01-101 | BEREFID | 100.3 | BESPEC | Specimen Type | LAVAGE FLUID | CRF |
| 7 | ABC | BE | ABC-01-101 | BEREFID | 100.4 | BESPEC | Specimen Type | LAVAGE FLUID | CRF |
| 8 | ABC | BE | ABC-01-101 | BEREFID | 100.5 | BESPEC | Specimen Type | LAVAGE FLUID | CRF |

Findings data captured about the specimen during collection, preparation, and handling are represented in the BS domain.
**Row 1:** Shows the total volume of lavage fluid collected during the gastric lavage by using the same values for BSREFID and BEREFID. This is the parent (collected) sample from which further aliquots were generated.
**Rows 2-6:** Show the volume of each aliquot created.
*bs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSORRES | BSORRESU | BSSTRESC | BSSTRESN | BSSTRESU | BSSPEC | BSLOC | BSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | BS | ABC-01-101 | 1 | 100 | VOLUME | Volume | 20 | mL | 20 | 20 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 2 | ABC | BS | ABC-01-101 | 2 | 100.1 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 3 | ABC | BS | ABC-01-101 | 3 | 100.2 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 4 | ABC | BS | ABC-01-101 | 4 | 100.3 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 5 | ABC | BS | ABC-01-101 | 5 | 100.4 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 6 | ABC | BS | ABC-01-101 | 6 | 100.5 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |

The RELSPEC table shows the relationship of the parent sample to its aliquots. The LEVEL variable indicates that the sample has been subsampled. The original parent sample is always LEVEL="1". An aliquot of the sample would be LEVEL="2". If the aliquot was further split, that subsample would be LEVEL="3".
**Row 1:** Shows the original collected (parent) sample. The PARENT variable is left blank to indicate that this is the highest level sample.
**Rows 2-6:** Show the relationship of each aliquot in the BE domain to the parent sample. PARENT is populated with the REFID value of the parent sample, indicating that the sample with REFID="100" is the parent of these samples. LEVEL="2" indicates that these aliquots are subsamples of the original (LEVEL="1") sample.
*relspec.xpt*

| Row | STUDYID | USUBJID | REFID | SPEC | PARENT | LEVEL |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | ABC-01-101 | 100 | LAVAGE FLUID |  | 1 |
| 2 | ABC | ABC-01-101 | 100.1 | LAVAGE FLUID | 100 | 2 |
| 3 | ABC | ABC-01-101 | 100.2 | LAVAGE FLUID | 100 | 2 |
| 4 | ABC | ABC-01-101 | 100.3 | LAVAGE FLUID | 100 | 2 |
| 5 | ABC | ABC-01-101 | 100.4 | LAVAGE FLUID | 100 | 2 |
| 6 | ABC | ABC-01-101 | 100.5 | LAVAGE FLUID | 100 | 2 |

Results from detection tests performed on samples are represented in the MB domain. The sputum sample was aliquoted 5 times. Three of these aliquots underwent detection testing using 3 separate tests: 1 for acid-fast bacillus (AFB), 1 for M. tuberculosis complex, and 1 for M. tuberculosis. MBTESTCD/MBTEST represents the organism being investigated, MBMETHOD represents the testing method, and MBREFID represents which aliquot was tested. The variable MBTSTDTL is used to provide further description of the test performed in producing the MB result. In addition to detection, MBTSTDTL can be used to represent specific attributes (e.g., quantifiable and semi-quantifiable results of the culture) as well as qualitative details about the culture (e.g., colony color, morphology).
**Row 1:** Shows a test targeting the presence or absence of AFB using a stain. The MBSPCCND shows that the sample used in the test was concentrated. MBGRPID can be used to connect the detection record with the corresponding AFB quantification results shown in row 2.
**Row 2:** Shows a categorical result for an AFB test using a stain. MBORRES contains a result based on a CDC AFB quantification scale. The name of the scale used is represented as a supplemental qualifier. MBREFID indicates which aliquot the procedure was performed upon and MBGRPID is used to connect the AFB quantification record to the detection record in row 1.
**Row 3:** Shows a test targeting the presence or absence of M. tuberculosis complex using a genotyping method. Details about the assay can be found in the Device Identifiers (DI) domain. The value in SPDEVID links the genotype result to the assay information in the DI domain. The microbial detection certainty is represented as a supplemental qualifier. Because genotyping was used, the detection is considered to be definitive.
**Row 4:** Shows a test targeting the presence or absence of M. tuberculosis performed on a solid culture. The medium type and microbial detection certainty are represented as supplemental qualifier. Because genotyping was not used, the detection is considered to be presumptive. The culture start and stop dates are represented in BE and are connected to the culture results via BELNKID and MBLNKGRP. MBGRPID is used to connect the detection record in MB with the corresponding culture characteristics shown in rows 5-7.
**Row 5:** Shows a colony-forming unit (CFU) count from a solid culture. The MBORRES value represents the actual colony count from this plate. However, the sample that was spread on this plate represented a 100-fold dilution from the original subject sample. This information is represented in the Dilution Factor supplemental qualifier (MBDILFCT), whose value = 10^-2 (1/100th). In order to enable more straightforward pooling of CFU data, a simple integer result (14700) is used in MBSTRESC/N, and MBSTRESU="CFU/mL". The medium type for the solid culture is also represented as a supplemental qualifier.
**Row 6:** Shows the standardized colony count category based on a CDC M. tuberculosis colony quantification scale. The quantification scale used and the medium type for the solid culture are represented as supplemental qualifiers.
*mb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | MBSEQ | MBGRPID | MBLNKGRP | MBREFID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBORRESU | MBRSLSCL | MBSTRESC | MBSTRESN | MBSTRESU | MBLOC | MBSPCCND | MBMETHOD | VISITNUM | VISIT | MBDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-01-101 |  | 1 | 1 |  | 100.1 | AFB | Acid-Fast Bacilli | DETECTION | PRESENT |  | Ord | PRESENT |  |  | STOMACH | CONCENTRATED | ZIEHL NEELSEN ACID FAST STAIN | 1 | WEEK 1 | 2011-01-17T06:00 |
| 2 | ABC | MB | ABC-01-101 |  | 2 | 1 |  | 100.1 | AFB | Acid-Fast Bacilli | CELL COUNT | 3+ |  | Ord | 3+ |  |  | STOMACH | CONCENTRATED | ZIEHL NEELSEN ACID FAST STAIN | 1 | WEEK 1 | 2011-01-17T06:00 |
| 3 | ABC | MB | ABC-01-101 | ABC765 | 3 |  |  | 100.2 | MTBCMPLX | Mycobacterium Tuberculosis Complex | DETECTION | PRESENT |  | Ord | PRESENT |  |  | STOMACH |  | NUCLEIC ACID AMPLIFICATION TEST | 1 | WEEK 1 | 2011-01-17T06:00 |
| 4 | ABC | MB | ABC-01-101 |  | 4 | 2 | 1 | 100.3 | MTB | Mycobacterium Tuberculosis | DETECTION | PRESENT |  | Ord | PRESENT |  |  | STOMACH |  | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
| 5 | ABC | MB | ABC-01-101 |  | 5 | 2 | 1 | 100.3 | MTB | Mycobacterium Tuberculosis | COLONY COUNT | 147 | CFU | Qn | 14700 | 14700 | CFU/mL | STOMACH |  | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
| 6 | ABC | MB | ABC-01-101 |  | 6 | 2 | 1 | 100.3 | MTB | Mycobacterium Tuberculosis | COLONY COUNT | 2+ |  | Ord | 2+ |  |  | STOMACH |  | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |

*suppmb.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-01-101 | MBSEQ | 2 | MBQSCAL | Quantification Scale | Smear Quantification: Centers for Disease Control Method for Carbol Fuchsin Staining (1000X) | Collected |
| 2 | ABC | MB | ABC-01-101 | MBSEQ | 3 | MBMICERT | Microbial Identification Certainty | DEFINITIVE | Collected |
| 3 | ABC | MB | ABC-01-101 | MBSEQ | 4 | MBMICERT | Microbial Identification Certainty | PRESUMPTIVE | Collected |
| 4 | ABC | MB | ABC-01-101 | MBREFID | 100.3 | MBMEDTYP | Medium Type | MIDDLEBROOK 7H10 AGAR | Collected |
| 7 | ABC | MB | ABC-01-101 | MBSEQ | 6 | MBQSCAL | Quantification Scale | Solid Media Result: Centers for Disease Control (CDC) Quantification Scale | Collected |
| 8 | ABC | MB | ABC-01-101 | MBSEQ | 5 | MBDILFCT | Dilution Factor | 10^-2 | Collected |

Results from drug susceptibility tests performed on samples are represented in the MS domain. This includes all phenotypic tests (where the drug is added directly to the culture medium) and genotypic tests (when the result is given as susceptible or resistant). Genotypic tests that give results of specific genetic polymorphisms should be represented in the Pharmacogenomics/Genetics Findings (PF) domain, even though such results may be categorized as susceptible or resistant. In this example, the variable NHOID (Non-host Organism Identifier) is populated with the name of the organism that is the subject of the test.
**Rows 1-2:** Show phenotypic testing results on 2 separate culture plates: 1 with medium containing rifampicin (row 1) and 1 with medium containing isoniazid (row 2). MSAGENT is populated with the name of the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used. The culture start and stop dates are represented in BE and can be linked to MS by BELNKID and MSLNKID.
**Rows 3-4:** Show genotypic susceptibility testing results on the same aliquot from a NAAT that looks for mutations that confer resistance to 2 drugs. MSAGENT should be populated with the name of the drug whose action is affected by the mutation being tested for. However, because the drug is not used in the test, MSCONC and MSCONU should be null. These results are represented in MS because the only result given is in terms of resistant/susceptible; no genetic results are reported.
*ms.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | NHOID | MSSEQ | MSREFID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSSTRESC | MSSPEC | MSLOC | MSMETHOD | MSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MS | ABC-01-101 |  | MYCOBACTERIUM TUBERCULOSIS | 1 | 100.4 | 2 | MICROSUS | Microbial Susceptibility | Rifampicin | 1 | ug/mL | RESISTANT | RESISTANT | LAVAGE FLUID | STOMACH | ANTIBIOTIC AGAR SCREEN | 2011-01-17T06:00 |
| 2 | ABC | MS | ABC-01-101 |  | MYCOBACTERIUM TUBERCULOSIS | 2 | 100.5 | 3 | MICROSUS | Microbial Susceptibility | Isoniazid | 0.2 | ug/mL | SUSCEPTIBLE | SUSCEPTIBLE | LAVAGE FLUID | STOMACH | ANTIBIOTIC AGAR SCREEN | 2011-01-17T06:00 |
| 3 | ABC | MS | ABC-01-101 | ABC765 | MYCOBACTERIUM TUBERCULOSIS | 3 | 100.2 |  | MICROSUS | Microbial Susceptibility | Rifampicin |  |  | RESISTANT | RESISTANT | LAVAGE FLUID | STOMACH | NUCLEIC ACID AMPLIFICATION TEST | 2011-01-17T06:00 |
| 4 | ABC | MS | ABC-01-101 | ABC765 | MYCOBACTERIUM TUBERCULOSIS | 4 | 100.2 |  | MICROSUS | Microbial Susceptibility | Isoniazid |  |  | SUSCEPTIBLE | SUSCEPTIBLE | LAVAGE FLUID | STOMACH | NUCLEIC ACID AMPLIFICATION TEST | 2011-01-17T06:00 |

*suppms.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MS | ABC-01-101 | MBREFID | 100.4 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected |
| 2 | ABC | MS | ABC-01-101 | MBREFID | 100.5 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected |

Data about the device used (row 3 of the MB dataset example and rows 3-4 of the MS dataset example) can be represented in the DI domain if needed.
*di.xpt*

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | DI | ABC765 | 1 | DEVTYPE | Device Type | NUCLEIC ACID AMPLIFICATION TEST |
| 2 | ABC | DI | ABC765 | 2 | TRADENAM | Trade Name | HAIN GENOTYPE MTBDRplus |

The RELREC table shows how culture start and end dates from BE were linked to the culture results in MB and MS using --LNKID and --LNKGRP. It also shows how the detection record (MB) was linked to the susceptibility results (MS) from the NAAT, using --REFID.
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | BE |  | BELNKID |  | ONE | A |
| 2 | ABC | MB |  | MBLNKGRP |  | MANY | A |
| 3 | ABC | BE |  | BELNKID |  | ONE | B |
| 4 | ABC | MS |  | MSLNKID |  | ONE | B |
| 5 | ABC | MB |  | MBREFID |  | ONE | C |
| 6 | ABC | MS |  | MSREFID |  | MANY | C |

**Example 4**
When a culture has become contaminated, the sponsor may choose to report results despite the contamination. This example shows how to flag results using a supplemental qualifier to indicate that the results are coming from a contaminated culture. This example also illustrates how to use Timing variables to represent an 8-hour pooled overnight sputum sample collection when the start and end times are collected. MBDTC is used to represent the start date/time of the overnight sputum collection and MBENDTC is used to represent the end date/time.
**Row 1:** Shows a test targeting the presence or absence of M. tuberculosis from a solid culture that has been contaminated (see SUPPMB).
**Row 2:** Shows the number of colony-forming units from the contaminated solid culture (see SUPPMB).
*mb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBGRPID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBORRESU | MBRSLSCL | MBSTRESC | MBSTRESN | MBSTRESU | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC | MBENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-01-601 | 1 | 600 | 1 | MTB | Mycobacterium Tuberculosis | DETECTION | PRESENT |  | Ord | PRESENT |  |  | SPUTUM | LUNG | MICROBIAL CULTURE, SOLID | 5 | WEEK 5 | 2011-03-01T22:00 | 2011-03-02T06:00 |
| 2 | ABC | MB | ABC-01-601 | 2 | 600 | 1 | MTB | Mycobacterium Tuberculosis | COLONY COUNT | 87 | CFU/mL | Qn | 87 | 87 | CFU/mL | SPUTUM | LUNG | MICROBIAL CULTURE, SOLID | 5 | WEEK 5 | 2011-03-01T22:00 | 2011-03-02T06:00 |

The culture-contamination indicator flag is shown in SUPPMB.
*suppmb.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MB | ABC-01-601 | MBSEQ | 1 | MBCNMIND | Culture Contamination Indicator | Y | Collected |
| 2 | ABC | MB | ABC-01-601 | MBSEQ | 2 | MBCNMIND | Culture Contamination Indicator | Y | Collected |

