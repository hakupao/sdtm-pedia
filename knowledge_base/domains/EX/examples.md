# EX — Examples

Note: Examples for EX and EC are shared in Section 6.1.3.3 of the SDTMIG. See also [EC Examples](../EC/examples.md).

## Example 1

This is an example of a double-blind study comparing drug X extended release (ER; 2 500-mg tablets once daily) vs. drug Z (2 250-mg tablets once daily). Per example CRFs, subject ABC1001 took 2 tablets from 2011-01-14 to 2011-01-28 and subject ABC2001 took 2 tablets within the same timeframe but missed dosing on 2011-01-24.

**CRF:**

**Subject: ABC1001**

| Bottle | Number of Tablets Taken Daily | Reason for Variation | Start Date | End Date |
|--------|-------------------------------|----------------------|------------|----------|
| A | 2 | | 2011-01-14 | 2011-01-28 |

**Subject: ABC2001**

| Bottle | Number of Tablets Taken Daily | Reason for Variation | Start Date | End Date |
|--------|-------------------------------|----------------------|------------|----------|
| A | 2 | | 2011-01-14 | 2011-01-23 |
| A | 0 | Patient mistake | 2011-01-24 | 2011-01-24 |
| A | 2 | | 2011-01-25 | 2011-01-28 |

Upon unmasking, it became known that subject ABC1001 received drug X and Subject ABC2001 received drug Z. The EC dataset shows the administrations of study treatment as collected.

**Rows 1-2, 4:** Show treatments administered.

**Row 3:** Shows that the zero for Number of Tablets Taken Daily on the CRF was represented as ECOCCUR = "N". The reason this treatment did not occur is represented in ECREASOC.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECREASOC | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|-----|---------|--------|---------|-------|---------|-------|---------|---------|----------|--------|--------|----------|-------|---------|---------|--------|--------|
| 1 | ABC | EC | ABC1001 | 1 | A2-20110114 | BOTTLE A | Y | Y | | 2 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |
| 2 | ABC | EC | ABC2001 | 1 | A2-20110114 | BOTTLE A | Y | Y | | 2 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-23 | 1 | 10 |
| 3 | ABC | EC | ABC2001 | 2 | A0-20110124 | BOTTLE A | Y | N | PATIENT MISTAKE | | TABLET | QD | TREATMENT | 2011-01-24 | 2011-01-24 | 11 | 11 |
| 4 | ABC | EC | ABC2001 | 3 | A2-20110125 | BOTTLE A | Y | Y | | 2 | TABLET | QD | TREATMENT | 2011-01-25 | 2011-01-28 | 12 | 15 |

The EX dataset shows the unmasked administrations. Two tablets from bottle A became 1000 mg of drug X extended release for subject ABC1001, but 500 mg of drug Z for subject ABC2001. Note that there is no record in the EX dataset for non-occurrence of study treatment. The non-occurrence of study drug for subject ABC2001 is reflected in the gap in time between the 2 EX records.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXLNKID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|-----|---------|--------|---------|-------|---------|-------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|
| 1 | ABC | EX | ABC1001 | 1 | A2-20110114 | DRUG X | 1000 | mg | TABLET, EXTENDED RELEASE | QD | ORAL | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |
| 2 | ABC | EX | ABC2001 | 1 | A2-20110114 | DRUG Z | 500 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-14 | 2011-01-23 | 1 | 10 |
| 3 | ABC | EX | ABC2001 | 2 | A2-20110125 | DRUG Z | 500 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-25 | 2011-01-28 | 12 | 15 |

The relrec.xpt example reflects a one-to-one dataset-level relationship between EC and EX using --LNKID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | EC | | ECLNKID | | ONE | 1 |
| 2 | ABC | EX | | EXLNKID | | ONE | 1 |

## Example 2

This example shows data from an open-label study. A subject received drug X as a 20 mg/mL solution administered across 3 injection sites to deliver a total dose of 3 mg/kg. The subject's weight was 100 kg.

**CRF:**

| | |
|---|---|
| Visit | 3 |
| Date | 2009-05-10 |
| **Injection 1** | |
| Volume Given (mL) | 5 |
| Location | ABDOMEN |
| Side | LEFT |
| **Injection 2** | |
| Volume Given (mL) | 5 |
| Location | ABDOMEN |
| Side | CENTER |
| **Injection 3** | |
| Volume Given (mL) | 5 |
| Location | ABDOMEN |
| Side | RIGHT |

The collected administration amounts, in mL, and their locations are represented in the EC dataset.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECSPID | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | ECLOC | ECLAT | VISIT | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|-----|---------|--------|---------|-------|--------|---------|-------|---------|---------|--------|--------|----------|----------|---------|-------|-------|-------|-------|---------|---------|--------|--------|
| 1 | ABC | EC | ABC3001 | 1 | INJ1 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | LEFT | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |
| 2 | ABC | EC | ABC3001 | 2 | INJ2 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | CENTER | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |
| 3 | ABC | EC | ABC3001 | 3 | INJ3 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | RIGHT | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |

The sponsor considered the 3 injections to constitute a single administration, so the EX dataset shows the total dose given in the protocol-specified unit, mg/kg. EXLOC = "ABDOMEN" is included because the location was common to all injections, but EXLAT was not included. If the sponsor had chosen to represent laterality in the EX record, this would have been handled as described in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXSPID | EXLNKID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EXLOC | VISITNUM | VISIT | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|--------|----------|----------|---------|-------|----------|-------|-------|---------|---------|--------|--------|
| 1 | ABC | EX | ABC3001 | 1 | | V3 | DRUG X | 3 | mg/kg | INJECTION | ONCE | SUBCUTANEOUS | ABDOMEN | 3 | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |

The relrec.xpt example reflects a many-to-one dataset-level relationship between EC and EX using --LNKID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | EC | | ECLNKID | | MANY | 1 |
| 2 | ABC | EX | | EXLNKID | | ONE | 1 |

## Example 3

The study in this example was a double-blind study comparing 10, 20, and 30 mg of Drug X once daily vs. placebo. Study treatment was given as 1 tablet each from bottles A, B, and C taken together once daily. The subject in this example took:

- 1 tablet from bottles A, B and C from 2011-01-14 to 2011-01-20
- 0 tablets from bottle B on 2011-01-21, then 2 tablets on 2011-01-22
- 1 tablet from bottles A and C on 2011-01-21 and 2011-01-22
- 1 tablet from bottles A, B and C from 2011-01-23 to 2011-01-28

The EC dataset shows administrations as collected, in tablets.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|-----|---------|--------|---------|-------|-------|---------|---------|--------|--------|----------|-------|---------|---------|--------|--------|
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

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|-----|---------|--------|---------|-------|-------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|
| 1 | ABC | EX | ABC4001 | 1 | DRUG X | 20 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-14 | 2011-01-20 | 1 | 7 |
| 2 | ABC | EX | ABC4001 | 2 | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-21 | 2011-01-21 | 8 | 8 |
| 3 | ABC | EX | ABC4001 | 3 | DRUG X | 30 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-22 | 2011-01-22 | 9 | 9 |
| 4 | ABC | EX | ABC4001 | 4 | DRUG X | 20 | mg | TABLET | QD | ORAL | TREATMENT | 2011-01-23 | 2011-01-28 | 10 | 15 |

## Example 4

The study in this example was an open-label study examining the tolerability of different doses of drug A. The study drug was taken orally, daily for 3 months. Dose adjustments were allowed as needed in response to tolerability or efficacy issues.

The EX dataset shows administrations collected in the protocol-specified unit, mg. No EC dataset was needed because the open-label administrations were collected in the protocol-specified unit; EC would be an exact duplicate of the entire EX domain.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EXADJ | EPOCH | EXSTDTC | EXENDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|----------|----------|---------|-------|-------|---------|---------|
| 1 | 37841 | EX | 37841001 | 1 | DRUG A | 20 | mg | TABLET | QD | ORAL | | TREATMENT | 2002-07-01 | 2002-10-01 |
| 2 | 37841 | EX | 37841002 | 1 | DRUG A | 20 | mg | TABLET | QD | ORAL | | TREATMENT | 2002-04-02 | 2002-04-21 |
| 3 | 37841 | EX | 37841002 | 2 | DRUG A | 15 | mg | TABLET | QD | ORAL | Reduced due to toxicity | TREATMENT | 2002-04-22 | 2002-07-01 |
| 4 | 37841 | EX | 37841003 | 1 | DRUG A | 20 | mg | TABLET | QD | ORAL | | TREATMENT | 2002-05-09 | 2002-06-01 |
| 5 | 37841 | EX | 37841003 | 2 | DRUG A | 25 | mg | TABLET | QD | ORAL | Increased due to suboptimal efficacy | TREATMENT | 2002-06-02 | 2002-07-01 |
| 6 | 37841 | EX | 37841003 | 3 | DRUG A | 30 | mg | TABLET | QD | ORAL | Increased due to suboptimal efficacy | TREATMENT | 2002-07-02 | 2002-08-01 |

## Example 5

This is an example of a double-blind study design comparing 10 and 20 mg of drug X vs. placebo taken daily, morning and evening, for a week.

**CRF:**

**Subject ABC5001**

| Bottle | Time Point | Number of Tablets Taken | Start Date | End Date |
|--------|------------|-------------------------|------------|----------|
| A | AM | 1 | 2012-01-01 | 2012-01-08 |
| B | PM | 1 | 2012-01-01 | 2012-01-08 |

**Subject ABC5002**

| Bottle | Time Point | Number of Tablets Taken | Start Date | End Date |
|--------|------------|-------------------------|------------|----------|
| A | AM | 1 | 2012-02-01 | 2012-02-08 |
| B | PM | 1 | 2012-02-01 | 2012-02-08 |

**Subject ABC5003**

| Bottle | Time Point | Number of Tablets Taken | Start Date | End Date |
|--------|------------|-------------------------|------------|----------|
| A | AM | 1 | 2012-03-01 | 2012-03-08 |
| B | PM | 1 | 2012-03-01 | 2012-03-08 |

The EC dataset shows the administrations as collected. The time-point variables ECTPT and ECTPTNUM were used to describe the time of day of administration. This use of time-point variables is novel, representing data about multiple time points, 1 on each day of administration, rather than data for a single time point.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECTPTNUM |
|-----|---------|--------|---------|-------|---------|-------|---------|---------|--------|--------|----------|-------|---------|---------|--------|--------|-------|----------|
| 1 | ABC | EC | ABC5001 | 1 | 20120101-20120108-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | AM | 1 |
| 2 | ABC | EC | ABC5001 | 2 | 20120101-20120108-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | PM | 2 |
| 3 | ABC | EC | ABC5002 | 1 | 20120201-20120208-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | AM | 1 |
| 4 | ABC | EC | ABC5002 | 2 | 20120201-20120208-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | PM | 2 |
| 5 | ABC | EC | ABC5003 | 1 | 20120301-20120308-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | AM | 1 |
| 6 | ABC | EC | ABC5003 | 2 | 20120301-20120308-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | PM | 2 |

The EX dataset shows the unmasked administrations in the protocol-specified unit, mg. Amount of placebo was represented as 0 mg. The sponsor chose to represent the administrations at the time-point level.

**Rows 1-2:** Show administrations for a subject who was randomized to the 20 mg drug X arm.

**Rows 3-4:** Show administrations for a subject who was randomized to the 10 mg drug X arm.

**Rows 5-6:** Show administrations for a subject who was randomized to the placebo arm.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXLNKID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY | EXTPT | EXTPTNUM |
|-----|---------|--------|---------|-------|---------|-------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|-------|----------|
| 1 | ABC | EX | ABC5001 | 1 | 20120101-20120108-AM | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | AM | 1 |
| 2 | ABC | EX | ABC5001 | 2 | 20120101-20120108-PM | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | PM | 2 |
| 3 | ABC | EX | ABC5002 | 1 | 20120201-20120208-AM | DRUG X | 10 | mg | TABLET | QD | ORAL | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | AM | 1 |
| 4 | ABC | EX | ABC5002 | 2 | 20120201-20120208-PM | PLACEBO | 0 | mg | TABLET | QD | ORAL | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | PM | 2 |
| 5 | ABC | EX | ABC5003 | 1 | 20120301-20120308-AM | PLACEBO | 0 | mg | TABLET | QD | ORAL | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | AM | 1 |
| 6 | ABC | EX | ABC5003 | 2 | 20120301-20120308-PM | PLACEBO | 0 | mg | TABLET | QD | ORAL | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | PM | 2 |

The relrec.xpt example reflects a one-to-one dataset-level relationship between EC and EX using --LNKID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | EC | | ECLNKID | | ONE | 1 |
| 2 | ABC | EX | | EXLNKID | | ONE | 1 |

## Example 6

The study in this example was a single-crossover study comparing once-daily oral administration of drug A 20 mg capsules with drug B 30 mg coated tablets. The study drug was taken for 3 consecutive mornings, 30 minutes prior to a standardized breakfast. There was a 6-day washout period between treatments.

**CRF:**

**Subject 56789001**

| | Period 1 | | | | | Period 2 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time | Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time |
| 1 | 1 | 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 1 | 2002-07-09T07:30 | 2002-07-09T07:30 |
| 2 | 1 | 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 1 | 1 | 2002-07-10T07:30 | 2002-07-10T07:30 |
| 3 | 1 | 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 1 | 1 | 2002-07-11T07:34 | 2002-07-11T07:34 |

**Subject 56789003**

| | Period 1 | | | | | Period 2 | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time | Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time |
| 1 | 1 | 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 1 | 2002-07-11T07:30 | 2002-07-11T07:30 |
| 2 | 1 | 1 | 2002-07-04T07:24 | 2002-07-04T07:24 | 2 | 1 | 1 | 2002-07-12T07:43 | 2002-07-12T07:43 |
| 3 | 1 | 1 | 2002-07-05T07:24 | 2002-07-05T07:24 | 3 | 1 | 1 | 2002-07-13T07:38 | 2002-07-13T07:38 |

The EC dataset shows administrations as collected.

**Rows 1-12:** Unblinding revealed that subject 56789001 received placebo-coated tablets during the first treatment epoch and placebo capsules during the second treatment epoch.

**Rows 13-24:** Unblinding revealed that subject 56789003 received placebo capsules during the first treatment epoch and placebo-coated tablets during the second treatment epoch.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECELTM | ECTPTREF |
|-----|---------|--------|---------|-------|-------|---------|---------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|-------|--------|----------|
| 1 | 56789 | EC | 56789001 | 1 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 2 | 56789 | EC | 56789001 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 3 | 56789 | EC | 56789001 | 3 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 4 | 56789 | EC | 56789001 | 4 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 5 | 56789 | EC | 56789001 | 5 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 6 | 56789 | EC | 56789001 | 6 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 7 | 56789 | EC | 56789001 | 7 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-09T07:30 | 2002-07-09T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 8 | 56789 | EC | 56789001 | 8 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-09T07:30 | 2002-07-09T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 9 | 56789 | EC | 56789001 | 9 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-10T07:30 | 2002-07-10T07:30 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 10 | 56789 | EC | 56789001 | 10 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-10T07:30 | 2002-07-10T07:30 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 11 | 56789 | EC | 56789001 | 11 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:34 | 2002-07-11T07:34 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 12 | 56789 | EC | 56789001 | 12 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:34 | 2002-07-11T07:34 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 13 | 56789 | EC | 56789003 | 1 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 14 | 56789 | EC | 56789003 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 15 | 56789 | EC | 56789003 | 3 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-04T07:24 | 2002-07-04T07:24 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 16 | 56789 | EC | 56789003 | 4 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-04T07:24 | 2002-07-04T07:24 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 17 | 56789 | EC | 56789003 | 5 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-05T07:24 | 2002-07-05T07:24 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 18 | 56789 | EC | 56789003 | 6 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-05T07:24 | 2002-07-05T07:24 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 19 | 56789 | EC | 56789003 | 7 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:30 | 2002-07-11T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 20 | 56789 | EC | 56789003 | 8 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11T07:30 | 2002-07-11T07:30 | 9 | 9 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 21 | 56789 | EC | 56789003 | 9 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-12T07:43 | 2002-07-12T07:43 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 22 | 56789 | EC | 56789003 | 10 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-12T07:43 | 2002-07-12T07:43 | 10 | 10 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 23 | 56789 | EC | 56789003 | 11 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-13T07:38 | 2002-07-13T07:38 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 24 | 56789 | EC | 56789003 | 12 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-13T07:38 | 2002-07-13T07:38 | 11 | 11 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |

The EX dataset shows the unblinded administrations.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY | EXTPT | EXTPTREF |
|-----|---------|--------|---------|-------|-------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|-------|----------|
| 1 | 56789 | EX | 56789001 | 1 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01 | 2002-07-03 | 1 | 3 | 30 MINUTES PRIOR | STD BREAKFAST |
| 2 | 56789 | EX | 56789001 | 2 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-01 | 2002-07-03 | 1 | 3 | 30 MINUTES PRIOR | STD BREAKFAST |
| 3 | 56789 | EX | 56789001 | 3 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-09 | 2002-07-11 | 9 | 11 | 30 MINUTES PRIOR | STD BREAKFAST |
| 4 | 56789 | EX | 56789001 | 4 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-09 | 2002-07-11 | 9 | 11 | 30 MINUTES PRIOR | STD BREAKFAST |
| 5 | 56789 | EX | 56789003 | 1 | PLACEBO | 0 | mg | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03 | 2002-07-05 | 1 | 3 | 30 MINUTES PRIOR | STD BREAKFAST |
| 6 | 56789 | EX | 56789003 | 2 | DRUG B | 30 | mg | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-03 | 2002-07-05 | 1 | 3 | 30 MINUTES PRIOR | STD BREAKFAST |
| 7 | 56789 | EX | 56789003 | 3 | DRUG A | 20 | mg | CAPSULE | QD | ORAL | TREATMENT 2 | 2002-07-11 | 2002-07-13 | 9 | 11 | 30 MINUTES PRIOR | STD BREAKFAST |
| 8 | 56789 | EX | 56789003 | 4 | PLACEBO | 0 | mg | TABLET, COATED | QD | ORAL | TREATMENT 2 | 2002-07-11 | 2002-07-13 | 9 | 11 | 30 MINUTES PRIOR | STD BREAKFAST |

## Example 7

The study in this example involved weekly infusions of drug Z 10 mg/kg. If a subject experienced a dose-limiting toxicity (DLT), the intended dose could be reduced to 7.5 mg/kg. The example CRF below was for subject ABC123-0201, who weighed 55 kg. The CRF shows that:

- The subject's first administration of drug Z was on 2009-02-13; the intended dose was 10 mg/kg, but the actual amount given was 99 mL at 5.5 mg/mL, so the actual dose was 9.9 mg/kg.
- The subject's second administration of drug Z occurred on 2009-02-20; the intended dose was reduced to 7.5 mg/kg due to dose-limiting toxicity, and the infusion was stopped early due to an injection site reaction. However, the actual amount given was 35 mL at a concentration of 4.12 mg/mL, so the calculated actual dose was 2.6 mg/kg.
- The subject's third administration was intended to occur on 2009-02-27; the intended dose was 7.5 mg/kg but, due to a personal reason, the administration did not occur.

**CRF:**

**Subject ABC123-0201**

| | Visit 1 | Visit 2 | Visit 3 |
|---|---|---|---|
| Intended Dose | 10 mg/kg | 10 mg/kg / 7.5 mg/kg | 10 mg/kg / 7.5 mg/kg |
| Reason for Dose Adjustment | | Dose-limiting toxicity | Dose-limiting toxicity |
| Dose Administered | Yes | Yes | Yes |
| Date | 13-FEB-2009 | 20-FEB-2009 | 27-FEB-2009 |
| Start Time (24 hour clock) | 10:00 | 11:00 | |
| End Time (24 hour clock) | 10:45 | 11:20 | |
| Amount (mL) | 99 mL | 35 mL | 0 mL |
| Concentration | 5.5 mg/mL | 4.12 mg/mL | 4.12 mg/mL |
| If dose was adjusted, what was the reason | | Injection site reaction | Injection site reaction / Personal reason |

The EC dataset shows both intended and actual doses of Drug Z, as collected.

**Rows 1, 3, 5:** Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED". Scheduled dose is represented in mg/mL.

**Rows 2, 4:** Show the collected actual administration amounts (mL) and ECMOOD is "PERFORMED". Actual doses are represented using dose in mL and concentration (pharmaceutical strength) in mg/mL.

**Row 6:** Shows a dose that was not given. ECREASOC shows the reason that ECOCCUR = "N", and ECDOSE is null.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECLNKGRP | ECTRT | ECMOOD | ECPRESP | ECOCCUR | ECREASOC | ECDOSE | ECDOSU | ECPSTRG | ECPSTRGU | ECADJ | EPOCH | VISITNUM | VISIT | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|-----|---------|--------|---------|-------|---------|----------|-------|--------|---------|---------|----------|--------|--------|---------|----------|-------|-------|----------|-------|---------|---------|--------|--------|
| 1 | ABC123 | EC | ABC123-0201 | 1 | | V1 | DRUG Z | SCHEDULED | | | | 10 | mg/kg | | | | VISIT TREATMENT | 1 | VISIT 1 | 2009-02-13 | 2009-02-13 | 1 | 1 |
| 2 | ABC123 | EC | ABC123-0201 | 2 | 20090213 | V1 | DRUG Z | PERFORMED | Y | Y | | 99 | mL | 5.5 | mg/mL | | VISIT TREATMENT | 1 | VISIT 1 | 2009-02-13T10:00 | 2009-02-13T10:45 | 1 | 1 |
| 3 | ABC123 | EC | ABC123-0201 | 3 | | V2 | DRUG Z | SCHEDULED | | | | 7.5 | mg/kg | | | Dose limiting toxicity | VISIT TREATMENT | 2 | VISIT 2 | 2009-02-20 | 2009-02-20 | 8 | 8 |
| 4 | ABC123 | EC | ABC123-0201 | 4 | 20090220 | V2 | DRUG Z | PERFORMED | Y | Y | | 35 | mL | 4.12 | mg/mL | | VISIT TREATMENT | 2 | VISIT 2 | 2009-02-20T11:00 | 2009-02-20T11:20 | 8 | 8 |
| 5 | ABC123 | EC | ABC123-0201 | 5 | | V3 | DRUG Z | SCHEDULED | | | | 7.5 | mg/kg | | | | VISIT TREATMENT | 3 | VISIT 3 | 2009-02-27 | 2009-02-27 | 15 | 15 |
| 6 | ABC123 | EC | ABC123-0201 | 6 | 20090227 | V3 | DRUG Z | PERFORMED | Y | N | PERSONAL REASON | | mL | 4.12 | mg/mL | | VISIT TREATMENT | 3 | VISIT 3 | 2009-02-27 | 2009-02-27 | 15 | 15 |

The EX dataset shows the administrations in protocol-specified unit (mg/kg). There is no record for the intended third dose that was not given. Intended doses in EC (records with ECMOOD = "SCHEDULED") can be compared with actual doses in EX.

**Row 1:** Shows the subject's first dose.

**Row 2:** Shows the subject's second dose. The collected explanation for the adjusted dose amount administered at visit 2 is in EXADJ.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXLNKID | EXLNKGRP | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EXADJ | VISITNUM | VISIT | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|-----|---------|--------|---------|-------|---------|----------|-------|--------|--------|----------|----------|---------|-------|----------|-------|-------|---------|---------|--------|--------|
| 1 | ABC123 | EX | ABC123-0201 | 1 | 20090213T1000 | V1 | DRUG Z | 9.9 | mg/kg | SOLUTION | CONTINUOUS | INTRAVENOUS | | 1 | VISIT 1 | TREATMENT | 2009-02-13T10:00 | 2009-02-13T10:00 | 1 | 1 |
| 2 | ABC123 | EX | ABC123-0201 | 2 | 20090220T1100 | V2 | DRUG Z | 2.6 | mg/kg | SOLUTION | CONTINUOUS | INTRAVENOUS | Injection site reaction | 2 | VISIT 2 | TREATMENT | 2009-02-20T11:00 | 2009-02-20T11:00 | 8 | 8 |

To complete this example the relevant records from the Vital Signs domain are represented below, to show the collected weight of the subject which was used for the dosing calculations.

**vs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | VSSEQ | VSLNKID | VSLNKGRP | VSTESTCD | VSTEST | VSORRES | VSORRESU | VSSTRESC | VSSTRESN | VSSTRESU | VSLOBXFL | VISITNUM | VISIT | VSDTC | EPOCH |
|-----|---------|--------|---------|-------|---------|----------|----------|--------|---------|----------|----------|----------|----------|----------|----------|-------|-------|-------|
| 1 | ABC123 | VS | ABC123-0201 | 1 | 20090213T1000 | V1 | WEIGHT | Weight | 55 | kg | 55 | 55 | kg | Y | 1 | VISIT 1 | 2009-02-13 | TREATMENT |
| 2 | ABC123 | VS | ABC123-0201 | 2 | 20090220T1100 | V2 | WEIGHT | Weight | 55 | kg | 55 | 55 | kg | | 2 | VISIT 2 | 2009-02-20 | TREATMENT |

The RELREC dataset represents relationships between EC, EX, and VS.

**Rows 1-3:** Represent the one-to-one-to-one relationship between "PERFORMED" records in EC, records in EX, and records in VS using --LNKID.

**Rows 4-6:** Represent the many-to-one-to-one relationship between many records in EC (both "SCHEDULED" and "PERFORMED"), one record in EX, and one record in VS (for each visit), using --LNKGRP.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | EC | | ECLNKID | | ONE | 1 |
| 2 | ABC123 | EX | | EXLNKID | | ONE | 1 |
| 3 | ABC123 | VS | | VSLNKID | | ONE | 1 |
| 4 | ABC123 | EC | | ECLNKGRP | | MANY | 2 |
| 5 | ABC123 | EX | | EXLNKGRP | | ONE | 2 |
| 6 | ABC123 | VS | | VSLNKGRP | | ONE | 2 |

## Example 8

In this example, a 100 mg tablet is scheduled to be taken daily. Start and end of dosing were collected, along with deviations from the planned daily dosing. Note: This method of data collection design is not consistent with current CDASH standards.

**CRF:**

| First Dose Date | Last Dose Date |
|-----------------|----------------|
| 2012-01-13 | 2012-01-20 |

| Date | Number of Doses Daily If/When Deviated from Plan |
|------|--------------------------------------------------|
| 2012-01-15 | 0 |
| 2012-01-16 | 2 |

The EC dataset shows administrations as collected.

**Row 1:** Shows the overall dosing interval from first dose date to last dose date.

**Row 2:** Shows the missed dose on 2012-01-15, which falls within the overall dosing interval.

**Row 3:** Shows a doubled dose on 2012-01-16, which also falls within the overall dosing interval.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECCAT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|-----|---------|--------|---------|-------|-------|-------|---------|---------|--------|--------|----------|-------|---------|---------|--------|--------|
| 1 | ABC | EC | ABC7001 | 1 | BOTTLE A | FIRST TO LAST DOSE INTERVAL | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-13 | 2012-01-20 | 1 | 8 |
| 2 | ABC | EC | ABC7001 | 2 | BOTTLE A | EXCEPTION DOSE | Y | N | | TABLET | QD | TREATMENT | 2012-01-15 | 2012-01-15 | 3 | 3 |
| 3 | ABC | EC | ABC7001 | 3 | BOTTLE A | EXCEPTION DOSE | Y | Y | 2 | TABLET | QD | TREATMENT | 2012-01-16 | 2012-01-16 | 4 | 4 |

The EX dataset shows the unmasked treatment for this subject, "DRUG X", and represents dosing in nonoverlapping intervals of time. There is no EX record for the missed dose, but the missed dose is reflected in a gap between dates in the EX records.

**Row 1:** Shows the administration from first dose date to the day before the missed dose.

**Row 2:** Shows the doubled dose.

**Row 3:** Shows the remaining administrations to the last dose date.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC | EXSTDY | EXENDY |
|-----|---------|--------|---------|-------|-------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|
| 1 | ABC | EX | ABC7001 | 1 | DRUG X | 100 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-13 | 2012-01-14 | 1 | 2 |
| 2 | ABC | EX | ABC7001 | 2 | DRUG X | 200 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-16 | 2012-01-16 | 4 | 4 |
| 3 | ABC | EX | ABC7001 | 3 | DRUG X | 100 | mg | TABLET | QD | ORAL | TREATMENT | 2012-01-17 | 2012-01-20 | 5 | 8 |
