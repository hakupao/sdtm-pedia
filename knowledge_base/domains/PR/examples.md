# PR — Examples

## Example 1

A procedures log CRF may collect verbatim values (procedure names) and dates performed. This example shows a subject who had 5 procedures collected and represented in the PR domain. In this study, the sponsor chose to consider verbatim text in PRTRT as long text represented in mixed case. See Section 4.2.4, Text Case in Submitted Data.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRTRT | PRSTDTC | PRENDTC |
|-----|---------|--------|---------|-------|-------|---------|---------|
| 1 | XYZ | PR | XYZ789-002 | 1 | Wisdom Teeth Extraction | 2010-06-08 | 2010-06-08 |
| 2 | XYZ | PR | XYZ789-002 | 2 | Reset Broken Arm | 2010-08-06 | 2010-08-06 |
| 3 | XYZ | PR | XYZ789-002 | 3 | Prostate Examination | 2010-12-12 | 2010-12-12 |
| 4 | XYZ | PR | XYZ789-002 | 4 | Endoscopy | 2010-12-12 | 2010-12-12 |
| 5 | XYZ | PR | XYZ789-002 | 5 | Heart Transplant | 2011-08-29 | 2011-08-29 |

## Example 2

This example shows data from a 24-hour Holter monitor, an ambulatory electrocardiography device that records a continuous electrocardiographic rhythm pattern.

The start and end of the Holter monitoring procedure are represented in the PR domain.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRLNKID | PRTRT | PRDECOD | PRPRESP | PROCCUR | PRSTDTC | PRENDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|---------|---------|---------|---------|
| 1 | ABC123 | PR | ABC123-001 | 1 | 20110101_20110102 | 24-HOUR HOLTER MONITOR | HOLTER CONTINUOUS ECG RECORDING | Y | Y | 2011-01-01T08:00 | 2011-01-02T09:45 |

The heart rate findings from the procedure are represented in the ECG Test Results (EG) domain.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGLNKID | EGTESTCD | EGTEST | EGORRES | EGORRESU | EGMETHOD | EGDTC | EGENDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|----------|-------|---------|
| 1 | ABC123 | EG | ABC123-001 | 1 | 20110101_20110102 | EGHRMIN | ECG Minimum Heart Rate | 70 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |
| 2 | ABC123 | EG | ABC123-001 | 2 | 20110101_20110102 | EGHRMAX | ECG Maximum Heart Rate | 100 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |
| 3 | ABC123 | EG | ABC123-001 | 3 | 20110101_20110102 | EGHRMEAN | ECG Mean Heart Rate | 75 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |

The relrec.xpt reflects a one-to-many dataset-level relationship between PR and EG using --LNKID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | PR | | PRLNKID | | ONE | 1 |
| 2 | ABC123 | EG | | EGLNKID | | MANY | 1 |

## Example 3

This example shows data for 3 subjects who had on-study radiotherapy. Dose, dose unit, location, and timing are represented. In this study, the sponsor chose to consider verbatim text in PRTRT as long text represented in mixed case. See Section 4.2.4, Text Case in Submitted Data.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRTRT | PRDOSE | PRDOSU | PRLOC | PRLAT | PRSTDTC | PRENDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|-------|-------|---------|---------|
| 1 | ABC123 | PR | ABC123-1001 | 1 | External beam radiation therapy | 70 | Gy | BREAST | RIGHT | 2011-06-01 | 2011-06-25 |
| 2 | ABC123 | PR | ABC123-2002 | 1 | Brachytherapy | 25 | Gy | PROSTATE | | 2011-07-15 | 2011-07-15 |
| 3 | ABC123 | PR | ABC123-3003 | 1 | Radiotherapy | 300 | cGy | BONE | | 2011-08-19 | 2011-08-22 |
