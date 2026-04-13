# LB — Assumptions

1. This domain captures laboratory data collected on the CRF or received from a central provider or vendor.

2. For lab tests that do not have continuous numeric results (e.g., urine protein as measured by dipstick, descriptive tests such as urine color), LBSTNRC could be populated either with normal range values that are a range of character values for an ordinal scale (e.g., "NEGATIVE to TRACE") or a delimited set of values that are considered to be normal (e.g., "YELLOW", "AMBER"). LBORNRLO, LBORNRHI, LBSTNRLO, and LBSTNRHI should be null for these types of tests.

3. LBNRIND can be added to indicate where a result falls with respect to reference range defined by LBORNRLO and LBORNRHI. Examples: "HIGH", "LOW". If toxicity grading is available, values would be represented in the variables LBTOX and LBTOXGR. Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in LBCLSIG (see also LB Example 1).

4. For lab tests where the specimen is collected over time (e.g., 24-hour urine collection), the start date/time of the collection goes into LBDTC and the end date/time of collection goes into LBENDTC. See Section 4.4.8, Date and Time Reported in a Domain Based on Findings.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the LB domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.

6. A value derived by a central lab according to its procedures is considered collected rather than derived. See Section 4.1.8.1, Origin Metadata for Variables.

7. The variable LBORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology List that is maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing/published unit from the UNIT codelist and submit their lab values using the published CDISC submission value. Example: "g/L" and "mg/mL" are mathematically synonymous, but only "g/L" is the submission value in the CDISC Unit codelist. If this is not the case, the unit must be added as a codelist extensible value in the Define.xml, and a new-term request must be submitted.
   a. CDISC Controlled Terminology Rules for Lab and Unit are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

8. The LBLOINC variable contains a code from the Logical Observation Identifiers Names and Codes (LOINC) database that identifies a specific laboratory test. The LOINC to LB Mapping Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology, may be used to identify appropriate CDISC CT values for a test with a particular LOINC code. In addition to LBTEST, LBSPEC, LBMETHOD, and LBORRESU, the aspects of a test that are associated with a LOINC code may be represented in the variables LBTPT, LBANMETH, LBTSTCND, LBBDAGNT, LBTSTOPO, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBPTFL, and LBPDUR. These additional variables are only required to be populated when necessary to provide a semantically meaningful distinction between records with different LBLOINC values.
