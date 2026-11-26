# LB — Examples

## Example 1

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

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBGRPID | LBTESTCD | LBTEST | LBTSTCND | LBCAT | LBSCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBCOLSRT | LBORNRLO | LBORNRHI | LBLLOD | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBSTNRC | LBNRIND | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBMETHOD | LBTMTHSN | LBLOBXFL | LBFAST | LBDRVFL | LBCLSIG | VISITNUM | VISIT | LBDTC | LBPTFL | LBPDUR |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|-------|--------|---------|----------|----------|----------|----------|----------|----------|--------|----------|----------|----------|----------|----------|---------|---------|--------|----------|---------|--------|----------|----------|----------|--------|---------|---------|----------|-------|-------|--------|--------|
| 1 | ABC | LB | ABC-001-001 | 1 | | ALB | Albumin | | CHEMISTRY | | 30 | g/L | QUANTITATIVE | MASS CONCENTRATION | | 35 | 50 | | 3.0 | 3.0 | g/dL | 3.5 | 5 | | LOW | | | 2862-1 | SERUM | ELECTROPHORESIS | | Y | Y | | N | 1 | Week 1 | 1999-06-19 | Y | |
| 2 | ABC | LB | ABC-001-001 | 2 | A | ALP | Alkaline Phosphatase | | CHEMISTRY | | 398 | IU/L | QUANTITATIVE | CATALYTIC CONCENTRATION | | 40 | 160 | | 398 | 398 | IU/L | 40 | 160 | | | | | 6768-6 | SERUM | | | | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 3 | ABC | LB | ABC-001-001 | 3 | A | ALP | Alkaline Phosphatase | | CHEMISTRY | | 350 | IU/L | QUANTITATIVE | CATALYTIC CONCENTRATION | | 40 | 160 | | 350 | 350 | IU/L | 40 | 160 | | | | | 6768-6 | SERUM | | | Y | Y | | | 1 | Week 1 | 1999-06-20 | Y | |
| 4 | ABC | LB | ABC-001-001 | 4 | A | ALP | Alkaline Phosphatase | | CHEMISTRY | | | | QUANTITATIVE | CATALYTIC CONCENTRATION | MEAN, ARITHMETIC | | | | 374 | 374 | IU/L | 40 | 160 | | | | | | SERUM | | | | Y | | | 1 | Week 1 | 1999-06-19 | | |
| 5 | ABC | LB | ABC-001-001 | 5 | A | ALP | Alkaline Phosphatase | | CHEMISTRY | | | | QUANTITATIVE | CATALYTIC CONCENTRATION | | | | | 398 | 398 | IU/L | 40 | 160 | | | | | | SERUM | | | | Y | Y | | 1 | Week 1 | 1999-06-19 | | |
| 6 | ABC | LB | ABC-001-001 | 6 | | CRP | C Reactive Protein | | CHEMISTRY | | 2.5 | mg/L | QUANTITATIVE | MASS CONCENTRATION | | 0.5 | 10 | | 2.5 | 2.5 | mg/L | 0.5 | 10 | | | | | 30522-7 | SERUM | | HIGH SENSITIVITY | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 7 | ABC | LB | ABC-001-001 | 7 | | CRYOGLBN | Cryoglobulin | 1D COLD INCUBATION | CHEMISTRY | | ABSENT | | ORDINAL | PRESENCE OR THRESHOLD | | | | | ABSENT | | | | | | | | | 12201-0 | SERUM | OBSERVATION | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 8 | ABC | LB | ABC-001-001 | 8 | | PSA | Prostate Specific Antigen | | CHEMISTRY | | 3.3 | ug/L | QUANTITATIVE | MASS CONCENTRATION | | 0 | 2.5 | Detection limit <=0.01 ng/mL | 3.3 | 3.3 | ug/L | 0 | 2.5 | | | | | 35741-8 | SERUM | | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 9 | ABC | LB | ABC-001-001 | 9 | | PROT | Protein | | CHEMISTRY | | 200 | g/L | QUANTITATIVE | MASS CONCENTRATION | | | | | 200 | 200 | g/L | | | | | | | 21482-5 | URINE | | | Y | | | | 1 | Week 1 | 1999-06-19 | | PT24H |
| 10 | ABC | LB | ABC-001-001 | 10 | | PLATAGGR | Platelet Aggregation | COLLAGEN INDUCED | COAGULATION | | NORMAL | | ORDINAL | PRESENCE OR THRESHOLD | | | | | NORMAL | | | | | | | | | 24379-0 | PLATELET RICH PLASMA | | | Y | | | | 1 | Week 1 | 1999-06-19 | Y | |
| 11 | ABC | LB | ABC-001-001 | 11 | | WBC | Leukocytes | | HEMATOLOGY | | 5.9 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION | | 4 | 11 | | 5.9 | 5.9 | 10^9/L | 4 | 11 | | | | | 6690-2 | BLOOD | AUTOMATED COUNT | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 12 | ABC | LB | ABC-001-001 | 12 | | LYMLE | Lymphocytes/Leukocytes | | HEMATOLOGY | DIFFERENTIAL | 6.7 | % | QUANTITATIVE | NUMBER FRACTION | | 25 | 40 | | 6.7 | 6.7 | % | 25 | 40 | | LOW | | | 736-9 | BLOOD | AUTOMATED COUNT | | Y | Y | | N | 1 | Week 1 | 1999-06-19 | Y | |
| 13 | ABC | LB | ABC-001-001 | 13 | | NEUT | Neutrophils | | HEMATOLOGY | DIFFERENTIAL | 5.1 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION | | 2 | 8 | | 5.1 | 5.1 | 10^9/L | 2 | 8 | | | | | 751-8 | BLOOD | AUTOMATED COUNT | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 14 | ABC | LB | ABC-001-001 | 14 | | PH | pH | | URINALYSIS | | 7.5 | | QUANTITATIVE | LOG SUBSTANCE CONCENTRATION | | 5.0 | 9.0 | | 7.5 | | | 5.00 | 9.00 | | | | | 5803-2 | URINE | TEST STRIP | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
| 15 | ABC | LB | ABC-001-001 | 15 | | ALB | Albumin | | CHEMISTRY | | | | QUANTITATIVE | MASS CONCENTRATION | | | | | | | | | | | | NOT DONE | INSUFFICIENT SAMPLE | 2862-1 | SERUM | ELECTROPHORESIS | | | | | | 2 | Week 2 | 1999-07-21 | Y | |
| 16 | ABC | LB | ABC-001-001 | 16 | | CHOL | Cholesterol | | CHEMISTRY | | 229 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | | 0 | <200 | | 229 | 229 | mg/dL | 0 | 199 | | | | | 2093-3 | SERUM | | | | | | | 2 | Week 2 | 1999-07-21 | Y | |
| 17 | ABC | LB | ABC-001-001 | 17 | | WBC | Leukocytes | | HEMATOLOGY | | 5.9 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION | | 4 | 11 | | 5.9 | 5.9 | 10^9/L | 4 | 11 | | | | | 6690-2 | BLOOD | AUTOMATED COUNT | | | Y | | | 2 | Week 2 | 1999-07-21 | Y | |
| 18 | ABC | LB | ABC-001-001 | 18 | | PROT | Protein | | URINALYSIS | | MODERATE | | ORDINAL | PRESENCE OR THRESHOLD | | | | | MODERATE | | | | | NEGATIVE to TRACE | ABNORMAL | | | 20454-5 | URINE | TEST STRIP | | | | | N | 2 | Week 2 | 1999-07-21 | Y | |

## Example 2

This example illustrates the use of timing variables for pre- and post-dose timed urine collections.

**Row 1:** Shows an example of a pre-dose urine collection interval (from 4 hours prior to dosing until 15 minutes prior to dosing) with a negative value for LBELTM that reflects the end of the interval in reference to the fixed reference LBTPTREF, the date of which is recorded in LBRFTDTC.
**Rows 2-3:** Show an example of post-dose urine collection intervals with values for LBELTM that reflect the end of the intervals in reference to the fixed reference LBTPTREF, the date of which is recorded in LBRFTDTC.

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBORNRLO | LBORNRHI | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBNRIND | LBLOINC | LBSPEC | LBMETHOD | LBLOBXFL | VISITNUM | VISIT | LBDTC | LBENDTC | LBTPT | LBTPTNUM | LBELTM | LBTPTREF | LBRFTDTC | LBPTFL |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|---------|---------|--------|----------|----------|----------|-------|-------|---------|-------|----------|--------|----------|----------|--------|
| 1 | ABC | LB | ABC-001-001 | 1 | GLUC | Glucose | URINALYSIS | 7 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | 1 | 15 | 0.39 | 0.39 | mmol/L | 0.1 | 0.8 | NORMAL | 5792-7 | URINE | TEST STRIP | Y | 2 | INITIAL DOSING | 1999-06-19T04:00 | 1999-06-19T07:45 | Pre-dose | 1 | -PT15M | Dosing | 1999-06-19T08:00 | Y |
| 2 | ABC | LB | ABC-001-001 | 2 | GLUC | Glucose | URINALYSIS | 11 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | 1 | 15 | 0.61 | 0.61 | mmol/L | 0.1 | 0.8 | NORMAL | 5792-7 | URINE | TEST STRIP | | 2 | INITIAL DOSING | 1999-06-19T08:00 | 1999-06-19T16:00 | 0-8 hours after dosing | 2 | PT8H | Dosing | 1999-06-19T08:00 | Y |
| 3 | ABC | LB | ABC-001-001 | 3 | GLUC | Glucose | URINALYSIS | 9 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | 1 | 15 | 0.5 | 0.5 | mmol/L | 0.1 | 0.8 | NORMAL | 5792-7 | URINE | TEST STRIP | | 2 | INITIAL DOSING | 1999-06-19T16:00 | 1999-06-20T00:00 | 8-16 hours after dosing | 3 | PT16H | Dosing | 1999-06-19T08:00 | Y |

## Example 3

This example illustrates the use of LBSTAT and LBREASND when there is no data value reported in LBORRES.

**Row 1:** Shows a pregnancy test with an original result of “-” (negative sign) standardized to the text value “NEGATIVE” in LBSTRESC.
**Row 2:** Shows a pregnancy test that was not performed because the subject was male. The sponsor felt it was necessary to include a record documenting the reason why the test was not performed, rather than simply not including a record.

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBORNRLO | LBORNRHI | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBNRIND | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBLOBXFL | VISITNUM | VISIT | LBDTC | LBPTFL |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|---------|--------|----------|---------|--------|----------|----------|-------|-------|--------|
| 1 | ABC | LB | ABC-001-001 | 1 | HCG | Choriogonadotropin Beta | CHEMISTRY | - | | Ord | PrThr | | | NEGATIVE | | | | | | | | 2106-3 | URINE | Y | 1 | BASELINE | 1999-06-19T04:00 | Y |
| 2 | ABC | LB | ABC-001-002 | 1 | HCG | Choriogonadotropin Beta | CHEMISTRY | | | Ord | PrThr | | | | | | | | | NOT DONE | NOT APPLICABLE (SUBJECT MALE) | 2106-3 | URINE | | 1 | BASELINE | 1999-06-24T08:00 | Y |

## Example 4

This example illustrates the use of the LBTSTOPO variable to identify the tests that screen, confirm, and quantify the presence of a substance.

**Row 1:** Shows cannabinoids are screened.
**Row 2:** Shows the previously detected cannabinoids are further confirmed in the subject.
**Row 3:** Shows the quantification of the cannabinoids.

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBGRPID | LBSEQ | LBTESTCD | LBTEST | LBTSTOPO | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | LBLOINC | LBSPEC | LBMETHOD | LBLOBXFL | LBDTC | VISITNUM | VISIT |
|-----|---------|--------|---------|---------|-------|----------|--------|----------|-------|---------|----------|----------|----------|----------|---------|--------|----------|----------|-------|----------|-------|
| 1 | ABC | LB | ABC-001-001 | 1 | 1 | CANNAB | Cannabinoids | SCREEN | DRUG TOXICITY | POSITIVE | | POSITIVE | | | 19287-2 | URINE | KINETIC MICROPARTICLE IMMUNOASSAY | Y | 2013-02-16 | 1 | Week 1 |
| 2 | ABC | LB | ABC-001-001 | 1 | 2 | CANNAB | Cannabinoids | CONFIRM | DRUG TOXICITY | POSITIVE | | POSITIVE | | | 19289-8 | URINE | MASS SPECTROMETRY | Y | 2013-02-16 | 1 | Week 1 |
| 3 | ABC | LB | ABC-001-001 | 1 | 3 | CANNAB | Cannabinoids | QUANTIFY | DRUG TOXICITY | 271 | ug/L | 271 | 271 | ug/L | 42860-7 | URINE | GC/MS | Y | 2013-02-16 | 1 | Week 1 |

## Example 5

This example illustrates the use of the LBBDAGNT variable for a single agent. **Note:** More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment, the target protein analytes interact with the binding agent. The use of the word "free" in the descriptions of rows 2 and 4 does not refer to the naturally occurring hepatocyte growth factor receptors or epidermal growth factor receptors, but rather to the receptors not bound to the binding agent. Representing the binding agent shows that what is being measured is the portion of the target receptors not bound to the binding agent, not the concentration of the receptors at their natural state.

**Row 1:** Shows the total amount of HGFR, both soluble and bound, to the target "ABC-8675309".
**Row 2:** Shows the amount of free HGFR not bound to the target "ABC-8675309" (i.e., a measure of the soluble analyte not bound to the target).
**Row 3:** Shows the total amount of EGFR, both soluble and bound, to the target "ABC-8675309".
**Row 4:** Shows the amount of free EGFR not bound to the target "ABC-8675309" (i.e., a measure of the soluble analyte not bound to the target).

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBBDAGNT | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | LBSPEC | LBMETHOD | LBDTC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|----------|--------|----------|-------|---------|----------|----------|----------|----------|--------|----------|-------|----------|-------|
| 1 | ABC | LB | ABC-123456 | 1 | HGFR | Hepatocyte Growth Factor Receptor | ABC-8675309 | TARGET ENGAGEMENT | 35 | ng/mL | 35 | 35 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 2 | ABC | LB | ABC-123456 | 2 | HGFRFR | Hepatocyte Growth Factor Receptor, Free | ABC-8675309 | TARGET ENGAGEMENT | 10 | ng/mL | 10 | 10 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 3 | ABC | LB | ABC-123456 | 3 | EGFR | Epidermal Growth Factor Receptor | ABC-8675309 | TARGET ENGAGEMENT | 100 | ng/mL | 100 | 100 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 4 | ABC | LB | ABC-123456 | 4 | EGFRFR | Epidermal Growth Factor Receptor, Free | ABC-8675309 | TARGET ENGAGEMENT | 20 | ng/mL | 20 | 20 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
