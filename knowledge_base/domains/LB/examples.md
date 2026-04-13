# LB — Examples

## Example 1

This example illustrates the use of previously published LB domain variables and introduces several new variables that were added to SDTMv2.0, including LBTSTCND, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBPTFL, and LBPDUR. These variables, in part, aid in harmonization to LOINC.

**Row 1:** Shows a value collected in 1 unit, but converted to selected standard unit. See Section 4.5.1, Original and Standardized Results of Findings and Tests Not Done, for additional examples for the population of result qualifiers. The result was evaluated by the investigator and determined to be not clinically significant.
**Rows 2-3:** Show 2 records for alkaline phosphatase done at the same visit, a day apart. LBPTFL is set to "Y" for both rows because each result is based on a sample from a single point in time.
**Rows 4-5:** Show 2 derived records (mean of records 2 and 3 and maximum value of records 2 and 3) grouped by a common LBGRPID value. The derived result in row 4 is described as a mean (LBCOLSRT="MEAN, ARITHMETIC"), but LBDRVFL is missing because the mean result was provided by the vendor. The derived result in row 5 was derived by the sponsor, and so is flagged as derived (LBDRVFL="Y"); LBCOLSRT is not populated because the result is not a collected summary result. For both derived results, the sponsor chose to populate LBRESSCL, LBRESTYP, LBSPEC, and LBFAST consistent with the 2 individual alkaline phosphatase records but did not populate LBLOINC or LBPTFL because neither derived record represented a single point in time. The sponsor chose to populate LBDTC with the first of the 2 specimen collection dates.
**Row 6:** Shows use of LBTMTHSN to represent "HIGH SENSITIVITY" for the high-sensitivity C-reactive protein (hs-CRP) test.
**Rows 7, 10:** Show use of LBTSTCND. For the cryoglobulin test, 1-day cold incubation is noted; for the platelet aggregation test, collagen induced is noted.
**Row 8:** Shows use of LBLLOD for a prostate-specific antigen test.
**Row 9:** Shows use of LBPDUR to represent the planned duration of "PT24H" for collection of urine samples for the protein test. LBPTFL is set to indicate that this test was not conducted at a single point in time.
**Rows 12-13:** Show a suggested use of the LBSCAT variable. LBSCAT could be used to further classify types of tests within a laboratory panel (e.g., "DIFFERENTIAL"). The LYMLE result was evaluated by the investigator and determined to be not clinically significant.
**Row 15:** Shows the proper use of the LBSTAT variable to indicate "NOT DONE", where a reason was collected when a test was not done. LBRESSCL, LBRESTYP, LBLOINC, LBSPEC, LBMETHOD, and LBPTFL are populated to describe the properties of the test that was not done.
**Row 16:** Shows measuring of the subject's cholesterol. The normal range for this test is <200 mg/dL. Note that although in this example the sponsor has decided to make LBSTNRHI="199", other sponsors may choose a different value.
**Row 17:** Shows use of LBPTFL set to "Y" to indicate that the test used a sample taken at a single point in time.
**Row 18:** Shows use of LBSTNRC for urine protein that is not reported as a continuous numeric result. The result was evaluated by the investigator and determined to be not clinically significant.

**lb.xpt**

*Note: The LB Example 1 table contains 18 rows and over 30 columns including STUDYID, DOMAIN, USUBJID, LBSEQ, LBGRPID, LBTESTCD, LBTEST, LBCAT, LBSCAT, LBORRES, LBORRESU, LBORNRLO, LBORNRHI, LBSTRESC, LBSTRESN, LBSTRESU, LBSTNRLO, LBSTNRHI, LBSTNRC, LBNRIND, LBSTAT, LBREASND, LBNAM, LBLOINC, LBSPEC, LBMETHOD, LBBLFL, LBFAST, LBDRVFL, LBTOX, LBTOXGR, LBCLSIG, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBTSTCND, LBPTFL, LBPDUR, VISITNUM, VISIT, LBDTC, LBENDTC. Representative test types include Albumin, Alkaline Phosphatase (with derived mean/max), C-Reactive Protein (high sensitivity), Cryoglobulin, Prostate Specific Antigen, Protein (24h urine), Platelet Aggregation, WBC, Lymphocytes, Monocytes, Neutrophils, Cholesterol, and Urine Protein.*

## Example 2

This example illustrates the use of timing variables for pre- and post-dose timed urine collections.

**Row 1:** Shows an example of a pre-dose urine collection interval (from 4 hours prior to dosing until 15 minutes prior to dosing) with a negative value for LBELTM that reflects the end of the interval in reference to the fixed reference LBTPTREF, the date of which is recorded in LBRFDTC.
**Rows 2-3:** Show an example of post-dose urine collection intervals with values for LBELTM that reflect the end of the intervals in reference to the fixed reference LBTPTREF, the date of which is recorded in LBRFDTC.

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | LBSPEC | LBMETHOD | LBBLFL | LBDRVFL | LBLOINC | LBPTFL | LBPDUR | LBTPT | LBTPTNUM | LBTPTREF | LBRFDTC | LBELTM | VISITNUM | VISIT | LBDTC | LBENDTC |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|--------|---------|---------|--------|--------|-------|----------|----------|---------|--------|----------|-------|-------|---------|
| 1 | ABC | LB | ABC-001-001 | 1 | CREAT | Creatinine Concentration | | 0.563 | g | 5.63 | 5.63 | g/L | URINE | | Y | | 2161-7 | | PT4H | -15 min pre-dose | 1 | PREVIOUS DOSE | 2000-02-01 | -PT15M | 1 | VISIT 1 | 2000-02-01T04:00 | 2000-02-01T07:45 |
| 2 | ABC | LB | ABC-001-001 | 2 | CREAT | Creatinine Concentration | | 0.879 | g | 8.79 | 8.79 | g/L | URINE | | | | 2161-7 | | PT12H | 12 h post-dose | 2 | PREVIOUS DOSE | 2000-02-01 | PT12H | 1 | VISIT 1 | 2000-02-01T08:00 | 2000-02-01T20:00 |
| 3 | ABC | LB | ABC-001-001 | 3 | CREAT | Creatinine Concentration | | 0.541 | g | 5.41 | 5.41 | g/L | URINE | | | | 2161-7 | | PT24H | 24 h post-dose | 3 | PREVIOUS DOSE | 2000-02-01 | PT24H | 1 | VISIT 1 | 2000-02-01T20:00 | 2000-02-02T08:00 |

## Example 3

This example illustrates the use of LBSTAT and LBREASND when there is no data value reported in LBORRES.

**Row 1:** Shows a pregnancy test with an original result of "-" (negative sign) standardized to the text value "NEGATIVE" in LBSTRESC.
**Row 2:** Shows a pregnancy test that was not performed because the subject was male. The sponsor felt it was necessary to include a record documenting the reason why the test was not performed, rather than simply not including a record.

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | LBNRIND | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBMETHOD | VISITNUM | VISIT | LBDTC | LBPTFL |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|---------|--------|----------|---------|--------|----------|----------|-------|-------|--------|
| 1 | ABC | LB | ABC-001-001 | 1 | HCG | Choriogonadotropin Beta | | - | | NEGATIVE | | | | | | 2106-3 | URINE | | 1 | BASELINE | 1999-06-09T10:00 | Y |
| 2 | ABC | LB | ABC-001-002 | 1 | HCG | Choriogonadotropin Beta | | | | | | | | NOT DONE | NOT APPLICABLE (SUBJECT MALE) | 2106-3 | URINE | | 1 | BASELINE | 1999-06-09T10:00 | Y |

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
| 3 | ABC | LB | ABC-001-001 | 1 | 3 | CANNAB | Cannabinoids | QUANTIFY | DRUG TOXICITY | 271 | ug/L | 271 | 271 | ug/L | 42860-7 | URINE | GC/MS | | 2013-02-16 | 1 | Week 1 |

## Example 5

This example illustrates the use of the LBBDAGNT variable for a single binding agent. **Note:** More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment, the target protein analytes interact with the binding agent. The use of the word "free" in the descriptions of rows 2 and 4 does not refer to the naturally occurring hepatocyte growth factor receptors or epidermal growth factor receptors, but rather to the receptors not bound to the binding agent. Representing the binding agent shows that what is being measured is the portion of the target receptors not bound to the binding agent, not the concentration of the receptors at their natural state.

**Row 1:** Shows the total of HGFR, both soluble and bound, to the target "ABC-8675309".
**Row 2:** Shows the amount of free HGFR not bound to the target "ABC-8675309" (i.e., a measure of the soluble analyte not bound to the target).
**Row 3:** Shows the total amount of EGFR, both soluble and bound, to the target "ABC-8675309".
**Row 4:** Shows the amount of free EGFR not bound to the target "ABC-8675309" (i.e., a measure of the soluble analyte not bound to the target).

**lb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBBDAGNT | LBCAT | LBORRES | LBORRESU | LBSTRESC | LBSTRESN | LBSTRESU | ISSPEC | LBMETHOD | LBDTC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|----------|--------|----------|-------|---------|----------|----------|----------|----------|--------|----------|-------|----------|-------|
| 1 | ABC | LB | ABC-123456 | 1 | HGFR | Hepatocyte Growth Factor Receptor | ABC-8675309 | TARGET ENGAGEMENT | 35 | ng/mL | 35 | 35 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 2 | ABC | LB | ABC-123456 | 2 | HGFRFR | Hepatocyte Growth Factor Receptor, Free | ABC-8675309 | TARGET ENGAGEMENT | 10 | ng/mL | 10 | 10 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 3 | ABC | LB | ABC-123456 | 3 | EGFR | Epidermal Growth Factor Receptor | ABC-8675309 | TARGET ENGAGEMENT | 100 | ng/mL | 100 | 100 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
| 4 | ABC | LB | ABC-123456 | 4 | EGFRFR | Epidermal Growth Factor Receptor, Free | ABC-8675309 | TARGET ENGAGEMENT | 20 | ng/mL | 20 | 20 | ng/mL | SERUM | ELISA | 2017-07-05 | 2 | WEEK 2 |
