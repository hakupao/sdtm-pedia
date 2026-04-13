# DV — Examples

## Example 1

This is an example of data that was collected on a protocol-deviations CRF. The DVDECOD column is for controlled terminology, whereas the DVTERM is free text.

**Rows 1, 3:** Show examples of a TREATMENT DEVIATION type of protocol deviation.

**Row 2:** Shows an example of a deviation due to the subject taking a prohibited concomitant medication.

**Row 4:** Shows an example of a medication that should not be taken during the study.

**dv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DVSEQ | DVTERM | DVDECOD | EPOCH | DVSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|---------|
| 1 | ABC123 | DV | 123101 | 1 | IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED | TREATMENT DEVIATION | TREATMENT | 2003-09-21 |
| 2 | ABC123 | DV | 123103 | 1 | DRUG XXX ADMINISTERED DURING STUDY TREATMENT PERIOD | EXCLUDED CONCOMITANT MEDICATION | TREATMENT | 2003-10-30 |
| 3 | ABC123 | DV | 123103 | 2 | VISIT 3 DOSE <15 MG | TREATMENT DEVIATION | TREATMENT | 2003-10-30 |
| 4 | ABC123 | DV | 123104 | 1 | TOOK ASPIRIN | PROHIBITED MEDS | TREATMENT | 2003-11-30 |

**References**

1. European Medicines Agency. ICH E3: Structure and Content of Clinical Study Reports. European Medicines Agency; 1996. Accessed February 22, 2021. https://www.ema.europa.eu/en/ich-e3-content-clinical-study-reports
