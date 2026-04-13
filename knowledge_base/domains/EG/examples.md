# EG — Examples

## Example 1

This example shows ECG measurements and other findings from one ECG for one subject. EGCAT has been used to group tests.

**Row 1:** Shows a measurement of ventricular rate. This result was assessed as not clinically significant (EGCLSIG = "N").

**Row 2:** Shows a measurement of PR interval. This result was assessed as clinically significant (EGCLSIG = "Y").

**Rows 2-4:** These interval measurements were collected in seconds. However, in this submission, the standard unit for these tests was milliseconds, so the results have been converted in EGSTRESC and EGSTRESN.

**Rows 5-6:** Show "QTcB Interval, Aggregate" and "QTcF Interval, Aggregate". These results were derived by the sponsor, as indicated by the "Y" in the EGDRVFL column. Note that EGORRES is null for these derived records.

**Rows 7-10:** Show results from tests looking for certain kinds of abnormalities, which have been grouped using EGCAT = "FINDINGS".

**Row 11:** Shows a technical problem represented as the result of the test "Technical Quality". Results of this test can be important to the overall understanding of an ECG, but are not truly findings or interpretations about the subject's heart function.

**Row 12:** Shows the result of the TEST "Interpretation" (i.e., the interpretation of the ECG strip as a whole), which for this ECG was "ABNORMAL".

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGREFID | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGXFN | EGNAM | EGCLSIG | EGDRVFL | VISITNUM | VISIT | EGDTC | EGDY |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|-------|---------|----------|----------|----------|----------|-------|-------|---------|---------|----------|-------|-------|------|
| 1 | XYZ | EG | XYZ-US-701-002 | 1 | 334PT89 | EGHRMN | ECG Mean Heart Rate | MEASUREMENT | SUPINE | 62 | beats/min | 62 | 62 | beats/min | PQW43787B-07.xml | Test | N | | 1 | Screening | 2003-04-36 | -36 |
| 2 | XYZ | EG | XYZ-US-701-002 | 2 | 334PT89 | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 0.15 | sec | 150 | 150 | msec | PQW43787B-07.xml | Test | Y | | 1 | Screening | 2003-04-36 | -36 |
| 3 | XYZ | EG | XYZ-US-701-002 | 3 | 334PT89 | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 0.103 | sec | 103 | 103 | msec | PQW43787B-07.xml | Test | | | 1 | Screening | 2003-04-36 | -36 |
| 4 | XYZ | EG | XYZ-US-701-002 | 4 | 334PT89 | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 0.406 | sec | 406 | 406 | msec | PQW43787B-07.xml | Test | | | 1 | Screening | 2003-04-36 | -36 |
| 5 | XYZ | EG | XYZ-US-701-002 | 5 | 334PT89 | QTCBAG | QTcB Interval, Aggregate | INTERVAL | SUPINE | | | 469 | 469 | msec | PQW43787B-07.xml | Test | Y | | 1 | Screening | 2003-04-36 | -36 |
| 6 | XYZ | EG | XYZ-US-701-002 | 6 | 334PT89 | QTCFAG | QTcF Interval, Aggregate | INTERVAL | SUPINE | | | 448 | 448 | msec | PQW43787B-07.xml | Test | Y | | 1 | Screening | 2003-04-36 | -36 |
| 7 | XYZ | EG | XYZ-US-701-002 | 7 | 334PT89 | SPRATRY | Supraventricular Tachyarrhythmias | FINDING | SUPINE | ATRIAL FIBRILLATION | | ATRIAL FIBRILLATION | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 8 | XYZ | EG | XYZ-US-701-002 | 8 | 334PT89 | SPRATRY | Supraventricular Tachyarrhythmias | FINDING | SUPINE | ATRIAL FLUTTER | | ATRIAL FLUTTER | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 9 | XYZ | EG | XYZ-US-701-002 | 9 | 334PT89 | STSTWUN | ST Segment, T wave, and U wave Changes: nonspecific or Enlargement | FINDING | SUPINE | PROLONGED QT | | PROLONGED QT | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 10 | XYZ | EG | XYZ-US-701-002 | 10 | 334PT89 | CHPTEN2 | Chamber Hypertrophy or Enlargement | FINDING | SUPINE | LEFT VENTRICULAR HYPERTROPHY | | LEFT VENTRICULAR HYPERTROPHY | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 11 | XYZ | EG | XYZ-US-701-002 | 11 | 334PT89 | TECHQUAL | Technical Quality | FINDING | SUPINE | OTHER/INCORRECT ELECTRODE PLACEMENT | | OTHER/INCORRECT ELECTRODE PLACEMENT | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 12 | XYZ | EG | XYZ-US-701-002 | 12 | 334PT89 | INTP | Interpretation | | SUPINE | ABNORMAL | | ABNORMAL | | | | | | | 1 | Screening | 15T11:58 | -36 |

## Example 2

This example shows ECG results where only the overall assessment was collected. Results are for one subject across multiple visits. In addition, the ECG interpretation was provided by the investigator and, when necessary, by a cardiologist. EGGRPID is used to group the overall assessments collected on each ECG.

**Rows 1-3:** Show interpretations performed by the principal investigation on three different occasions. The ECG at Visit "SCREEN 2" has been flagged as the last observation before start of study treatment.

**Rows 4-5:** Show interpretations of the same ECG by both the investigator and a cardiologist. EGGRPID has been used to group these two records to emphasize their relationship.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGGRPID | EGTESTCD | EGTEST | EGPOS | EGORRES | EGSTRESC | EGLOBXFL | EGEVAL | VISITNUM | VISIT | VISITDY | EGDTC | EGDY |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|--------|----------|-------|---------|-------|------|
| 1 | ABC | EG | ABC-99-CA-456 | 1 | | INTP | Interpretation | SUPINE | NORMAL | NORMAL | | PRINCIPAL INVESTIGATOR | 1 | SCREEN 1 | -2 | 2003-11-26 | -2 |
| 2 | ABC | EG | ABC-99-CA-456 | 2 | | INTP | Interpretation | SUPINE | NORMAL | NORMAL | Y | PRINCIPAL INVESTIGATOR | 2 | SCREEN II | -1 | 2003-11-27 | -1 |
| 3 | ABC | EG | ABC-99-CA-456 | 3 | | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL | | PRINCIPAL INVESTIGATOR | 3 | DAY 10 | 10 | 2003-12-07T09:02 | 10 |
| 4 | ABC | EG | ABC-99-CA-456 | 4 | Comp 1 | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL | | PRINCIPAL INVESTIGATOR | 4 | DAY 15 | 15 | 2003-12-12 | 15 |
| 5 | ABC | EG | ABC-99-CA-456 | 5 | Comp 1 | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL | | CARDIOLOGIST | 4 | DAY 15 | 15 | 2003-12-12 | 15 |

## Example 3

This example shows 10-second ECG replicates extracted from a continuous recording. The example shows one subject's extracted 10-second ECG replicate results. Three replicates were extracted for planned time points "1 HR" and "2 HR"; EGREPNUM is used to identify the replicates. Summary mean measurements are reported for the 10 seconds of extracted data for each replicate. EGDTC is the date/time of the first individual beat in the extracted 10-second ECG. In order to save space, some permissible variables (EGREFID, VISITDY, EGTPTNUM, EGTPTREF, EGRFTDTC) have been omitted, as marked by ellipses.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | ... | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGMETHOD | EGLEAD | EGLOBXFL | VISITNUM | VISIT | EGDTC | EGTPT | ... | EGREPNUM |
|-----|---------|--------|---------|-------|-----|----------|--------|-------|-------|---------|----------|----------|----------|----------|----------|--------|----------|----------|-------|-------|-------|-----|----------|
| 1 | STUDY01 | EG | 2324-P0001 | 1 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 2 | STUDY01 | EG | 2324-P0001 | 2 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 658 | msec | 658 | 658 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 3 | STUDY01 | EG | 2324-P0001 | 3 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 97 | msec | 97 | 97 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT | 2014-03-22T10:00:21 | 1 HR | ... | 1 |

*(Table continues with rows 4-23 for additional replicates at 1 HR and 2 HR time points, covering PR Interval, RR Interval, QRS Duration, QT Interval, and PR Interval measurements across 3 replicates per time point.)*

## Example 4

The example shows one subject's continuous beat-to-beat EG results. Only 3 beats are shown, but there could be measurements for, as an example, 101,000 complexes in 24 hours. The actual number of complexes in 24 hours can be variable and depends on average heart rate. The results are mapped to the EG domain using EGBEATNO. If there is no result to be reported, then the row would not be included.

**Rows 1-2:** Show the first beat recorded. The first beat was considered to be the beat for which the recording contained a complete P-wave. It was assigned EGBEATNO = "1". There is an RR measurement for this beat because RR is measured as the duration (time) between the peak of the R-wave in the reported single beat and peak of the R-wave in the preceding single beat, and the partial recording that preceded EGBEATNO = "1" did not contain an R-wave. EGDTC was the date/time of the individual beat.

**Rows 3-5:** EGBEATNO = "2" had an RR measurement, since the R-wave of the preceding beat (EGBEATNO = "1") was recorded.

**Rows 6-8:** There is a 1-hour gap between beats 2 and 3 due to electrical interference or other artifacts that prevented measurements from being recorded. Note that EGBEATNO = "3" does have an RR measurement because the partial beat preceding EGBEATNO = "3" contained an R-wave.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGBEATNO | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGMETHOD | EGLEAD | EGLOBXFL | VISITNUM | VISIT | EGDTC | EGTPT | VISITDY | EGREPNUM |
|-----|---------|--------|---------|-------|----------|----------|--------|-------|-------|---------|----------|----------|----------|----------|----------|--------|----------|----------|-------|-------|-------|---------|----------|
| 1 | STUDY01 | EG | 2324-P0001 | 1 | 1 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 | | | |
| 2 | STUDY01 | EG | 2324-P0001 | 2 | 1 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 97 | msec | 97 | 97 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 | | | |
| 3 | STUDY01 | EG | 2324-P0001 | 3 | 2 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 | | | |
| 4 | STUDY01 | EG | 2324-P0001 | 4 | 2 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 | | | |
| 5 | STUDY01 | EG | 2324-P0001 | 5 | 2 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 95 | msec | 95 | 95 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 | | | |
| 6 | STUDY01 | EG | 2324-P0001 | 6 | 3 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 169 | msec | 169 | 169 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T15:32:13.3 | | | |
| 7 | STUDY01 | EG | 2324-P0001 | 7 | 3 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 | | | |
| 8 | STUDY01 | EG | 2324-P0001 | 8 | 3 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 90 | msec | 90 | 90 | msec | 12 LEAD STANDARD | LEAD II | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 | | | |
