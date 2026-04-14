# HO — Examples

## Example 1

In this example, a healthcare encounter CRF collects verbatim descriptions of the encounter.

**Rows 1-2:** Subject ABC123101 was hospitalized and then moved to a nursing home.

**Rows 3-5:** Subject ABC123102 was in a hospital in the general ward and then in the intensive care unit. This same subject was transferred to a rehabilitation facility.

**Rows 6-7:** Subject ABC123103 has 2 hospitalization records.

**Row 8:** Subject ABC123104 was seen in the cardiac catheterization laboratory.

**Rows 9-12:** Subject ABC123105 and subject ABC123106 were each seen in the cardiac catheterization laboratory and then transferred to another hospital.

**ho.xpt**

| Row | STUDYID | DOMAIN | USUBJID | HOSEQ | HOTERM | EPOCH | HOSTDTC | HOENDTC | HODUR |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|-------|
| 1 | ABC | HO | ABC123101 | 1 | HOSPITAL | TREATMENT | 2011-06-08 | 2011-06-13 | |
| 2 | ABC | HO | ABC123101 | 2 | NURSING HOME | TREATMENT | | | P6D |
| 3 | ABC | HO | ABC123102 | 1 | GENERAL WARD | TREATMENT | 2011-08-06 | 2011-08-08 | |
| 4 | ABC | HO | ABC123102 | 2 | INTENSIVE CARE | TREATMENT | 2011-08-08 | 2011-08-15 | |
| 5 | ABC | HO | ABC123102 | 3 | REHABILITATION FACILITY | TREATMENT | 2011-08-15 | 2011-08-20 | |
| 6 | ABC | HO | ABC123103 | 1 | HOSPITAL | TREATMENT | 2011-09-09 | 2011-09-11 | |
| 7 | ABC | HO | ABC123103 | 2 | HOSPITAL | TREATMENT | 2011-09-11 | 2011-09-15 | |
| 8 | ABC | HO | ABC123104 | 1 | CARDIAC CATHETERIZATION LABORATORY | TREATMENT | 2011-10-10 | 2011-10-10 | |
| 9 | ABC | HO | ABC123105 | 1 | CARDIAC CATHETERIZATION LABORATORY | TREATMENT | 2011-10-11 | 2011-10-11 | |
| 10 | ABC | HO | ABC123105 | 2 | HOSPITAL | TREATMENT | 2011-10-11 | 2011-10-15 | |
| 11 | ABC | HO | ABC123106 | 1 | CARDIAC CATHETERIZATION LABORATORY | FOLLOW-UP | 2011-11-07 | 2011-11-07 | |
| 12 | ABC | HO | ABC123106 | 2 | HOSPITAL | FOLLOW-UP | 2011-11-07 | 2011-11-09 | |

**Row 1:** For the first encounter recorded for subject ABC123101, the indication/medical condition for hospitalization was recorded.

**Row 2:** For the second encounter recorded for subject ABC123101, the reason for admission to a nursing home was for rehabilitation.

**Rows 3-4:** For the 2 encounters recorded for subject ABC123103, the names of the facilities were recorded.

**Row 5:** For the first encounter recorded for subject ABC123105, the indication/medical condition for the hospitalization was recorded.

**Row 6:** For the second encounter recorded for subject ABC123105, the name of the hospital was recorded.

**suppho.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | HO | ABC123101 | HOSEQ | 1 | HOINDC | Indication | CONGESTIVE HEART FAILURE | CRF | |
| 2 | ABC | HO | ABC123101 | HOSEQ | 2 | HOREAS | Reason | REHABILITATION | CRF | |
| 3 | ABC | HO | ABC123103 | HOSEQ | 1 | HONAM | Provider Name | GENERAL HOSPITAL | CRF | |
| 4 | ABC | HO | ABC123103 | HOSEQ | 2 | HONAM | Provider Name | EMERSON HOSPITAL | CRF | |
| 5 | ABC | HO | ABC123105 | HOSEQ | 1 | HOINDC | Indication | ATRIAL FIBRILLATION | CRF | |
| 6 | ABC | HO | ABC123105 | HOSEQ | 2 | HONAM | Provider Name | ROOSEVELT HOSPITAL | CRF | |

## Example 2

In this example, the dates of an initial hospitalization are collected as well as the date/time of ICU stay. Subsequent to discharge from the initial hospitalization, follow-up healthcare encounters, including admission to a rehabilitation facility, visits with healthcare providers, and home nursing visits were collected. Repeat hospitalizations are categorized separately.

**ho.xpt**

| Row | STUDYID | DOMAIN | USUBJID | HOSEQ | HOTERM | HOCAT | HOSTDTC | HOENDTC | HOENRTPT | HOENTPT |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|----------|---------|
| 1 | ABC | HO | ABC123101 | 1 | HOSPITAL | INITIAL HOSPITALIZATION | 2011-06-08 | 2011-06-12 | | |
| 2 | ABC | HO | ABC123101 | 2 | ICU | INITIAL HOSPITALIZATION | 2011-06-08T11:00 | 2011-06-09T14:30 | | |
| 3 | ABC | HO | ABC123101 | 3 | REHABILITATION FACILITY | FOLLOW-UP CARE | 2011-06-12 | 2011-06-22 | | |
| 4 | ABC | HO | ABC123101 | 4 | CARDIOLOGY UNIT | FOLLOW-UP CARE | 2011-06-25 | 2011-06-25 | | |
| 5 | ABC | HO | ABC123101 | 5 | OUTPATIENT PHYSICAL THERAPY | FOLLOW-UP CARE | 2011-06-27 | 2011-06-27 | | |
| 6 | ABC | HO | ABC123101 | 6 | OUTPATIENT PHYSICAL THERAPY | FOLLOW-UP CARE | 2011-07-12 | 2011-07-12 | | |
| 7 | ABC | HO | ABC123101 | 7 | HOSPITAL | REPEAT HOSPITALIZATION | 2011-07-23 | 2011-07-24 | | |
| 8 | ABC | HO | ABC123102 | 1 | HOSPITAL | INITIAL HOSPITALIZATION | 2011-06-19 | 2011-07-02 | | |
| 9 | ABC | HO | ABC123102 | 2 | ICU | INITIAL HOSPITALIZATION | 2011-06-19T22:00 | 2011-06-23T09:30 | | |
| 10 | ABC | HO | ABC123102 | 3 | ICU | INITIAL HOSPITALIZATION | 2011-06-25T17:00 | 2011-06-29T19:30 | | |
| 11 | ABC | HO | ABC123102 | 4 | SKILLED NURSING FACILITY | FOLLOW-UP CARE | 2011-07-02 | | ONGOING | END OF STUDY |

The indication/medical condition for subject ABC123101's repeat hospitalization was represented as a supplemental qualifier.

**suppho.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | HO | ABC123101 | HOSEQ | 7 | HOINDC | Indication | STROKE | CRF | |
