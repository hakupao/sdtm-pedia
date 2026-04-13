# TS — Assumptions

The Trial Summary (TS) dataset allows the sponsor to submit a summary of the trial in a structured format. Each record in the TS dataset contains the value of a parameter, a characteristic of the trial. For example, TS is used to record basic information about the study such as trial phase, protocol title, and trial objectives. The TS dataset contains information about the planned and actual trial characteristics.

1. The intent of this dataset is to provide a summary of trial information. This is not subject-level data.

2. Recipients may specify their requirements for which trial summary parameters should be included under which conditions. For example, the US FDA includes such information in their Study Data Technical Conformance Guide.

3. The order of parameters in the examples of TS datasets should not be taken as a requirement. There are no requirements or expectations about the order of parameters within the TS dataset.

4. The method for treating text >200 characters in TS is similar to that used for the Comments (CO) special-purpose domain (Section 5.1, Comments). If TSVAL is >200 characters, then it should be split into multiple variables, TSVAL-TSVALn. See Section 4.5.3.2, Text Strings Greater than 200 Characters in Other Variables.

5. A list of values for TSPARM and TSPARMCD can be found in CDISC Controlled Terminology, available at https://www.cancer.gov/research/resources/terminology/cdisc.

6. Controlled terminology for TSPARM is extensible. The meaning of any added parameters should be explained in the metadata for the TS dataset.

7. For a particular trial summary parameter, responses (values in TSVAL) may be numeric, datetimes or amounts of time represented in ISO8601 format, or text. For some parameters, textual responses may be taken from controlled terminology; for others, responses may be free text.

8. For some trial summary parameters, CDISC Controlled Terminology includes codelists for use with TSVAL. The associations between trial summary parameters and response codelists are in the TS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology. Recipients may also specify controlled terminology for TSVAL. These specifications may be for trial summary parameters for which there is no CDISC Controlled Terminology or they may replace CDISC Controlled Terminology for a trial summary parameter. For example, the US FDA Data Standards Catalog includes terminologies to be used for certain trial summary parameters.

9. There is a code value for TSVALCD only when there is controlled terminology for TSVAL. For example, when TSPARMCD = "PLANSUB" (Planned Number of Subjects) or TSPARMCD = "TITLE" (Trial Title), then TSVALCD will be null.

10. TSVALNF contains a "null flavor," a value that provides additional coded information when TSVAL is null. For example, for TSPARM = "AGEMAX" (Planned Maximum Age of Subjects), there is no value if a study does not specify a maximum age. In this case, the appropriate null flavor is "PINF", which stands for "positive infinity." In a clinical pharmacology study conducted in healthy volunteers for a drug where indications are not yet established, the appropriate null flavor for TSPARM = "INDIC" (Trial Disease/Condition Indication) would be "NA" (i.e., not applicable). TSVALNF can also be used in a case where the value of a particular parameter is unknown.

11. Some codelists used for TSVAL include terms which are also null flavors. For example, the Pharmaceutical Dosage Form codelist includes the values "UNKNOWN" and "NOT APPLICABLE". In such cases, TSVAL should have the term from the codelist and TSVALNF should be null.

12. For some trials, there will be multiple records in the TS dataset for a single parameter. For example, a trial that addresses both safety and efficacy could have 2 records with TSPARMCD = "TTYPE" (Trial Type), one with the TSVAL = "SAFETY" and the other with TSVAL = "EFFICACY". TSSEQ has a different value for each record for the same parameter.

    Note that this is different from datasets that contain subject data, where the --SEQ variable has a different value for each record for the same subject.

13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-level datasets that the blocks bound by TSGRPID are within a subject. TSGRPID can be used to tie together any block of records in the TS dataset. TSGRPID is most likely to be used when the TS dataset includes multiple records for the same parameter.

    For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.

    | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL |
    |-------|---------|----------|--------|-------|
    | 1 | A | DOSE | Dose per Administration | 50 |
    | 1 | A | DOSFREQ | Dosing Frequency | BID |
    | 2 | B | DOSE | Dose per Administration | 100 |
    | 2 | B | DOSFREQ | Dosing Frequency | Q24H |
    | 1 | | DOSU | Dose Units | mg |

14. Protocols vary in how they describe objectives. If the protocol does not provide information about which objectives meet the definition of TSPARM = "OBJPRIM" (Trial Primary Objective; i.e., the principal purpose of the trial), then the objectives should be provided as values of TSPARM = "OBJPRIM". Consult the controlled terminology for trial summary parameters for appropriate parameter values for representing other objective designations (e.g., secondary, exploratory).

15. As per the definitions, the primary outcome measure is associated with the primary objective, the secondary outcome measure is associated with the secondary objective, and the exploratory outcome measure is associated with the exploratory objective. It is possible for the same outcome measure to be associated with more than 1 objective. For example, 2 objectives could use the same outcome measure at different time points, or using different analysis methods.

16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome measures should be provided as values of TSPARM = "OUTMSPR" (Primary Outcome Measure). Similarly, all outcome measures used to assess secondary objectives should be provided as values of TSPARM = "OUTMSSEC" (Secondary Outcome Measure), and all outcome measures used to assess exploratory objectives should be provided as values of TSPARM = "OUTMSEXP" (Exploratory Outcome Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory should be provided as values of TSPARM = "OUTMSADD" (Additional Outcome Measure).

17. Trial indication: Values for TSVAL when TSPARMCD = "INDIC" would indicate the condition, disease, or disorder the trial is intended to investigate or address. A vaccine study of healthy subjects, with the intended purpose of preventing influenza infection, would have TSVAL = "Influenza". A clinical pharmacology study of healthy volunteers, with the purpose of collecting pharmacokinetic data, would have TSVAL be null and TSVALNF = "NA" if TS contains a row where TSPARMCD = "INDIC".

18. Values for TSVAL when TSPARMCD = "REGID" (Registry Identifier) will be identifiers assigned by the registry (e.g., ClinicalTrials.gov, EudraCT).

### Use of Null Flavor

The variable TSVALNF is based on the idea of a "null flavor" as embodied in the ISO 21090 standard. A null flavor is an ancillary piece of data that provides additional information when its primary piece of data is null (has a missing value). There is controlled terminology for the null flavor data item which includes such familiar values as "Unknown", "Other", and "Not Applicable" among its 14 terms.

The controlled terminology for null flavor, which supersedes Appendix C1, Supplemental Qualifiers Name Codes, is included below.

**NullFlavor Enumeration (OID: 2.16.840.1.113883.5.1008)**

| Rank | Code | Display Name | Definition |
|------|------|---|---|
| 1 | NI | No information | The value is exceptional (i.e., missing, omitted, incomplete, improper). No information as to the reason for being an exceptional value is provided. This is the most general exceptional value. It is also the default exceptional value. |
| 2 | INV | Invalid | The value as represented in the instance is not a member of the set of permitted data values in the constrained value domain of a variable. |
| 3 | OTH | Other | The actual value is not a member of the set of permitted data values in the constrained value domain of a variable (e.g., concept not provided by required code system). |
| 4 | PINF | Positive infinity | Positive infinity of numbers |
| 4 | NINF | Negative infinity | Negative infinity of numbers |
| 3 | UNC | Unencoded | No attempt has been made to encode the information correctly, but the raw source information is represented (usually in original Text). |
| 3 | DER | Derived | An actual value may exist, but it must be derived from the information provided (usually an expression is provided directly). |
| 2 | UNK | Unknown | A proper value is applicable, but not known. |
| 3 | ASKU | Asked but unknown | Information was sought but not found (e.g., patient was asked but didn't know). |
| 4 | NAV | Temporarily unavailable | Information is not available at this time, but is expected to be available later. |
| 3 | NASK | Not asked | This information has not been sought (e.g., patient was not asked). |
| 3 | QS | Sufficient quantity | The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material. For example, if directions said, "Add 10 mg of ingredient X, 50 mg of ingredient Y, and sufficient quantity of water to 100 ml", the null flavor "QS" would be used to express the quantity of water. |
| 3 | TRC | Trace | The content is greater than zero, but too small to be quantified. |
| 2 | MSK | Masked | There is information on this item available, but it has not been provided by the sender due to security, privacy or other reasons. There may be an alternate mechanism for gaining access to this information. |
