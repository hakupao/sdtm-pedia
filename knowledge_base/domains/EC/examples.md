# EC — Examples

Note: Examples for EX and EC are shared in Section 6.1.3.3 of the SDTMIG. See also [EX Examples](../EX/examples.md).

## Example 1

This is an example of a double-blind study comparing drug X extended release (ER; 2 500-mg tablets once daily) vs. drug Z (2 250-mg tablets once daily). Per example CRFs, subject ABC1001 took 2 tablets from 2011-01-14 to 2011-01-28 and subject ABC2001 took 2 tablets within the same timeframe but missed dosing on 2011-01-24.

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

## Example 2

This example shows data from an open-label study. A subject received drug X as a 20 mg/mL solution administered across 3 injection sites to deliver a total dose of 3 mg/kg. The subject's weight was 100 kg.

The collected administration amounts, in mL, and their locations are represented in the EC dataset.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECSPID | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | ECLOC | ECLAT | VISIT | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY |
|-----|---------|--------|---------|-------|--------|---------|-------|---------|---------|--------|--------|----------|----------|---------|-------|-------|-------|-------|---------|---------|--------|--------|
| 1 | ABC | EC | ABC3001 | 1 | INJ1 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | LEFT | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |
| 2 | ABC | EC | ABC3001 | 2 | INJ2 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | CENTER | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |
| 3 | ABC | EC | ABC3001 | 3 | INJ3 | V3 | DRUG X | Y | Y | 5 | mL | INJECTION | ONCE | SUBCUTANEOUS | ABDOMINAL CAVITY | RIGHT | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |

## Example 3

The study in this example was a double-blind study comparing 10, 20, and 30 mg of Drug X once daily vs. placebo. Study treatment was given as 1 tablet each from bottles A, B, and C taken together once daily.

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

## Example 5

This is an example of a double-blind study design comparing 10 and 20 mg of drug X vs. placebo taken daily, morning and evening, for a week.

The EC dataset shows the administrations as collected. The time-point variables ECTPT and ECTPTNUM were used to describe the time of day of administration.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECLNKID | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRQ | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECTPTNUM |
|-----|---------|--------|---------|-------|---------|-------|---------|---------|--------|--------|----------|-------|---------|---------|--------|--------|-------|----------|
| 1 | ABC | EC | ABC5001 | 1 | 20120101-20120108-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | AM | 1 |
| 2 | ABC | EC | ABC5001 | 2 | 20120101-20120108-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-01-01 | 2012-01-08 | 1 | 8 | PM | 2 |
| 3 | ABC | EC | ABC5002 | 1 | 20120201-20120208-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | AM | 1 |
| 4 | ABC | EC | ABC5002 | 2 | 20120201-20120208-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-02-01 | 2012-02-08 | 1 | 8 | PM | 2 |
| 5 | ABC | EC | ABC5003 | 1 | 20120301-20120308-AM | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | AM | 1 |
| 6 | ABC | EC | ABC5003 | 2 | 20120301-20120308-PM | BOTTLE B | Y | Y | 1 | TABLET | QD | TREATMENT | 2012-03-01 | 2012-03-08 | 1 | 8 | PM | 2 |

## Example 6

The study in this example was a single-crossover study comparing once-daily oral administration of drug A 20 mg capsules with drug B 30 mg coated tablets. The study drug was taken for 3 consecutive mornings, 30 minutes prior to a standardized breakfast. There was a 6-day washout period between treatments.

The EC dataset shows administrations as collected.

**Rows 1-12:** Unblinding revealed that subject 56789001 received placebo-coated tablets during the first treatment epoch and placebo capsules during the second treatment epoch.

**Rows 13-24:** Unblinding revealed that subject 56789003 received placebo capsules during the first treatment epoch and placebo-coated tablets during the second treatment epoch.

**ec.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECELTM | ECTPTREF |
|-----|---------|--------|---------|-------|-------|---------|---------|--------|--------|----------|----------|---------|-------|---------|---------|--------|--------|-------|--------|----------|
| 1 | 56789 | EC | 56789001 | 1 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 2 | 56789 | EC | 56789001 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 3-12 | ... | EC | 56789001 | 3-12 | BOTTLE 1/2 | Y | Y | 1 | ... | ... | QD | ORAL | TREATMENT 1/2 | ... | ... | ... | ... | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 13 | 56789 | EC | 56789003 | 1 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:30 | 2002-07-03T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
| 14-24 | ... | EC | 56789003 | 2-12 | BOTTLE 1/2 | Y | Y | 1 | ... | ... | QD | ORAL | TREATMENT 1/2 | ... | ... | ... | ... | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |

See [EX Examples](../EX/examples.md) Example 6 for the complete EC and EX datasets.

## Example 7

The study in this example involved weekly infusions of drug Z 10 mg/kg. If a subject experienced a dose-limiting toxicity (DLT), the intended dose could be reduced to 7.5 mg/kg.

The EC dataset shows both intended and actual doses of Drug Z, as collected.

**Rows 1, 3, 5:** Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED".

**Rows 2, 4:** Show the collected actual administration amounts (mL) and ECMOOD is "PERFORMED".

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

## Example 8

In this example, a 100 mg tablet is scheduled to be taken daily. Start and end of dosing were collected, along with deviations from the planned daily dosing.

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
