# PC — Examples

*Note: PC and PP share a combined examples section (6.3.5.9.3 Relating PP Records to PC Records). The PC concentration data table is shown here; see also PP examples for the derived pharmacokinetic parameters and the 4 RELREC methods for relating PC to PP.*

Due to space limitations, not all expected or permissible findings variables are included in the example for this domain.

## Example 1

This example shows concentration data for drug A and a metabolite of drug A from plasma and from urine samples collected pre-dose and after dosing on study days 1 and 11.

PCTPTREF is a text value of the description of a "zero" time (e.g., time of dosing). It should be meaningful. If there are multiple PK profiles being generated, the zero time for each will be different (e.g., a different dose such as first dose, second dose) and, as a result, values for PCTPTREF must be different. In this example, such values for PCTPTREF are required to make values of PCTPTNUM and PCTPT unique (see Section 4.4.10, Representing Time Points).

**Rows 1-2:** Show day 1 pre-dose drug and metabolite concentrations in plasma and urine.
**Rows 3-4:** Show day 1 pre-dose drug and metabolite concentrations in urine. Urine specimens may be collected over an interval; both PCDTC and PCENDTC have been populated with the same value to indicate that these specimens were collected at a point in time rather than over an interval.
**Rows 5-6:** Show specimen properties (VOLUME and PH) for the day 1 pre-dose urine specimens. These have a PCCAT value of "SPECIMEN PROPERTY".
**Rows 7-12:** Show day 1 post-dose drug and metabolite concentrations in plasma.
**Rows 13-16:** Show day 11 drug and metabolite concentrations in plasma.
**Rows 17-20:** Show day 11 drug and metabolite concentrations in urine specimens collected over an interval. The elapsed times for urine samples are calculated as the elapsed time (from the reference time point, PCTPTREF) to the end of the specimen collection interval. Elapsed time values that are the same for urine and plasma samples have been assigned the same value for PCTPT. For the urine samples, the value in PCEVLINT describes the planned evaluation (or collection) interval relative to the time point. The actual evaluation interval can be determined by subtracting PCDTC from PCENDTC.
**Rows 21-30:** Show additional drug and metabolite concentrations and specimen properties related to the day 11 dose.

**pc.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PCSEQ | PCGRPID | PCREFID | PCTESTCD | PCTEST | PCCAT | PCORRES | PCORRESU | PCSTRESC | PCSTRESN | PCSTRESU | PCSPEC | PCBLFL | PCLLOQ | PCSTAT | PCDTC | PCENDTC | PCDY | PCTPT | PCTPTNUM | PCTPTREF | PCRFDTC | PCELTM | PCEVLINT |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|--------|--------|--------|-------|---------|------|-------|----------|----------|---------|--------|---------|
| 1 | ABC-123 | PC | 1235154 | 1 | DRUGA_DAY1 | 625154 | DRUGX | Drug A | ANALYTE | 0.10 | ng/mL | 0.10 | 0.10 | ng/mL | PLASMA | Y | 0.10 | | 2001-02-25 | | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-25T08:00 | PT0M | |
| 2 | ABC-123 | PC | 1235154 | 2 | DRUGA_DAY1 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | BLQ | ng/mL | BLQ | | ng/mL | PLASMA | Y | 0.10 | | 2001-02-25 | | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-25T08:00 | PT0M | |
| 3 | ABC-123 | PC | 1235154 | 3 | DRUGA_DAY1 | 625154 | DRUGX | Drug A | ANALYTE | 0.10 | ng/mL | 0.10 | 0.10 | ng/mL | URINE | Y | 0.10 | | 2001-02-25 | 2001-02-25 | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-25T08:00 | PT0M | |
| 4 | ABC-123 | PC | 1235154 | 4 | DRUGA_DAY1 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | BLQ | ng/mL | BLQ | | ng/mL | URINE | Y | 0.10 | | 2001-02-25 | 2001-02-25 | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-25T08:00 | PT0M | |
| 5 | ABC-123 | PC | 1235154 | 5 | DRUGA_DAY1 | 625154 | VOLUME | Volume | SPECIMEN PROPERTY | 363 | mL | 363 | 363 | mL | URINE | | | | 2001-02-25 | 2001-02-25 | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-25T08:00 | PT0M | |
| 6 | ABC-123 | PC | 1235154 | 6 | DRUGA_DAY1 | 625154 | PH | PH | SPECIMEN PROPERTY | | | | | | URINE | | | | 2001-02-25 | 2001-02-25 | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-25T08:00 | PT0M | |
| 7 | ABC-123 | PC | 1235154 | 7 | DRUGA_DAY1 | 625154 | DRUGX | Drug A | ANALYTE | 0.74 | ng/mL | 0.74 | 0.74 | ng/mL | PLASMA | | 0.10 | | 2001-02-25 | | 1 | 5 min post | 0.083 | Day 1 Dose | 2001-02-25T08:00 | PT5M | |
| 8 | ABC-123 | PC | 1235154 | 8 | DRUGA_DAY1 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | BLQ | ng/mL | BLQ | | ng/mL | PLASMA | | 0.10 | | 2001-02-25 | | 1 | 5 min post | 0.083 | Day 1 Dose | 2001-02-25T08:00 | PT5M | |
| 9 | ABC-123 | PC | 1235154 | 9 | DRUGA_DAY1 | 625154 | DRUGX | Drug A | ANALYTE | 6.92 | ng/mL | 6.92 | 6.92 | ng/mL | PLASMA | | 0.10 | | 2001-02-25 | | 1 | 25 min post | 0.417 | Day 1 Dose | 2001-02-25T08:00 | PT25M | |
| 10 | ABC-123 | PC | 1235154 | 10 | DRUGA_DAY1 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 1.86 | ng/mL | 1.86 | 1.86 | ng/mL | PLASMA | | 0.10 | | 2001-02-25 | | 1 | 25 min post | 0.417 | Day 1 Dose | 2001-02-25T08:00 | PT25M | |
| 11 | ABC-123 | PC | 1235154 | 11 | DRUGA_DAY1 | 625154 | DRUGX | Drug A | ANALYTE | 5.19 | ng/mL | 5.19 | 5.19 | ng/mL | PLASMA | | 0.10 | | 2001-02-25 | | 1 | 75 min post | 1.25 | Day 1 Dose | 2001-02-25T08:00 | PT75M | |
| 12 | ABC-123 | PC | 1235154 | 12 | DRUGA_DAY1 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 6.10 | ng/mL | 6.10 | 6.10 | ng/mL | PLASMA | | 0.10 | | 2001-02-25 | | 1 | 75 min post | 1.25 | Day 1 Dose | 2001-02-25T08:00 | PT75M | |
| 13 | ABC-123 | PC | 1235154 | 13 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 1.75 | ng/mL | 1.75 | 1.75 | ng/mL | PLASMA | | 0.10 | | 2001-03-07 | | 11 | 100 min post | 1.667 | Day 11 Dose | 2001-03-07T08:00 | PT100M | |
| 14 | ABC-123 | PC | 1235154 | 14 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 1.18 | ng/mL | 1.18 | 1.18 | ng/mL | PLASMA | | 0.10 | | 2001-03-07 | | 11 | 100 min post | 1.667 | Day 11 Dose | 2001-03-07T08:00 | PT100M | |
| 15 | ABC-123 | PC | 1235154 | 15 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 265 | ng/mL | 265 | 265 | ng/mL | PLASMA | | 0.10 | | 2001-03-07 | | 11 | 2h post | 2 | Day 11 Dose | 2001-03-07T08:00 | PT2H | |
| 16 | ABC-123 | PC | 1235154 | 16 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 7.1 | ng/mL | 7.1 | 7.1 | ng/mL | PLASMA | | 0.10 | | 2001-03-07 | | 11 | 2h post | 2 | Day 11 Dose | 2001-03-07T08:00 | PT2H | |
| 17 | ABC-123 | PC | 1235154 | 17 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 380 | ng/mL | 380 | 380 | ng/mL | URINE | | 0.10 | | 2001-03-07 | 2001-03-07 | 11 | 12h post | 12 | Day 11 Dose | 2001-03-07T08:00 | PT12H | -PT12H |
| 18 | ABC-123 | PC | 1235154 | 18 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 380 | ng/mL | 380 | 380 | ng/mL | URINE | | 0.10 | | 2001-03-07 | 2001-03-07 | 11 | 12h post | 12 | Day 11 Dose | 2001-03-07T08:00 | PT12H | -PT12H |
| 19 | ABC-123 | PC | 1235154 | 19 | DRUGA_DAY11 | 625154 | VOLUME | Volume | SPECIMEN PROPERTY | 606 | mL | 606 | 606 | mL | URINE | | | | 2001-03-07 | 2001-03-07 | 11 | 12h post | 12 | Day 11 Dose | 2001-03-07T08:00 | PT12H | -PT12H |
| 20 | ABC-123 | PC | 1235154 | 20 | DRUGA_DAY11 | 625154 | PH | PH | SPECIMEN PROPERTY | 6.1 | | 6.1 | 6.1 | | URINE | | | | 2001-03-07 | 2001-03-07 | 11 | 12h post | 12 | Day 11 Dose | 2001-03-07T08:00 | PT12H | -PT12H |
| 21 | ABC-123 | PC | 1235154 | 21 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 2.4 | ng/mL | 2.4 | 2.4 | ng/mL | URINE | | 0.10 | | 2001-03-07 | 2001-03-18 | 11 | 24h post | 24 | Day 11 Dose | 2001-03-07T08:00 | PT24H | -PT12H |
| 22 | ABC-123 | PC | 1235154 | 22 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 2.4 | ng/mL | 2.4 | 2.4 | ng/mL | URINE | | 0.10 | | 2001-03-07 | 2001-03-18 | 11 | 24h post | 24 | Day 11 Dose | 2001-03-07T08:00 | PT24H | -PT12H |
| 23 | ABC-123 | PC | 1235154 | 23 | DRUGA_DAY11 | 625154 | VOLUME | Volume | SPECIMEN PROPERTY | 406 | mL | 406 | 406 | mL | URINE | | | | 2001-03-07 | 2001-03-18 | 11 | 24h post | 24 | Day 11 Dose | 2001-03-07T08:00 | PT24H | -PT12H |
| 24 | ABC-123 | PC | 1235154 | 24 | DRUGA_DAY11 | 625154 | PH | PH | SPECIMEN PROPERTY | | | | | | URINE | | | | 2001-03-07 | 2001-03-18 | 11 | 24h post | 24 | Day 11 Dose | 2001-03-07T08:00 | PT24H | -PT12H |
| 25 | ABC-123 | PC | 1235154 | 25 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 0.73 | ng/mL | 0.73 | 0.73 | ng/mL | PLASMA | | 0.10 | | 2001-03-17 | | 11 | 24h post | 24 | Day 11 Dose | 2001-03-07T08:00 | PT24H | |
| 26 | ABC-123 | PC | 1235154 | 26 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 0.80 | ng/mL | 0.80 | 0.80 | ng/mL | PLASMA | | 0.10 | | 2001-03-17 | | 11 | 24h post | 24 | Day 11 Dose | 2001-03-07T08:00 | PT24H | |
| 27 | ABC-123 | PC | 1235154 | 27 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | | ng/mL | | | ng/mL | PLASMA | | 0.10 | NOT DONE | 2001-03-18 | | 11 | 36h post | 36 | Day 11 Dose | 2001-03-07T08:00 | PT36H | |
| 28 | ABC-123 | PC | 1235154 | 28 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | | ng/mL | | | ng/mL | PLASMA | | 0.10 | NOT DONE | 2001-03-18 | | 11 | 36h post | 36 | Day 11 Dose | 2001-03-07T08:00 | PT36H | |
| 29 | ABC-123 | PC | 1235154 | 29 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 5.1 | | | | | PLASMA | | | | 2001-03-07 | | 11 | Pre-dose | -1 | Day 11 Dose | 2001-03-07T08:00 | PT0M | |
| 30 | ABC-123 | PC | 1235154 | 30 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | | | | | | PLASMA | | | | 2001-03-07 | | 11 | Pre-dose | -1 | Day 11 Dose | 2001-03-07T08:00 | PT0M | |
| 31 | ABC-123 | PC | 1235154 | 31 | DRUGA_DAY11 | 625154 | DRUGX | Drug A | ANALYTE | 6.28 | ng/mL | 6.28 | 6.28 | ng/mL | PLASMA | | 0.10 | | 2001-03-07 | | 11 | 5 min post | 0.083 | Day 11 Dose | 2001-03-07T08:00 | PT5M | |
| 32 | ABC-123 | PC | 1235154 | 32 | DRUGA_DAY11 | 625154 | DRUGXM | Drug A Metabolite | ANALYTE | 0.81 | ng/mL | 0.81 | 0.81 | ng/mL | PLASMA | | 0.10 | | 2001-03-07 | | 11 | 5 min post | 0.083 | Day 11 Dose | 2001-03-07T08:00 | PT5M | |

## Relating PC and PP — Overview

Sponsors must document the concentrations used to calculate each parameter. This may be done in analysis dataset metadata or by documenting relationships between records in the Pharmacokinetics Parameters (PP) and Pharmacokinetics Concentrations (PC) datasets in a RELREC dataset (see Section 8.2, Relating Peer Records, and Section 8.3, Relating Datasets).

### PC-PP Relating Datasets

If all time-point concentrations in PC are used to calculate all parameters for all subjects, then the relationship between the 2 datasets can be documented as shown in this table:

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | | PCGRPID | | MANY | A |
| 2 | ABC-123 | PP | | PPGRPID | | MANY | A |

Note that the reference time point and the analyte are part of the natural key (see Section 3.2.1.1, Primary Keys) for both datasets. In this relationship, --GRPID is a surrogate key, and must be populated so that each combination of analyte and reference time point has a separate value of --GRPID.

### PC-PP Relating Records

This section illustrates 4 methods for representing relationships between PC and PP records under 4 different circumstances. All these examples are based on the same PC and PP data for 1 drug (i.e., drug X).

The different methods for representing relationships are based on which linking variables are used in RELREC:
- **Method A** (many to many, using PCGRPID and PPGRPID)
- **Method B** (one to many, using PCSEQ and PPGRPID)
- **Method C** (many to one, using PCGRPID and PPSEQ)
- **Method D** (one to one, using PCSEQ and PPSEQ)

The different examples illustrate situations in which different subsets of the pharmacokinetic concentration data were used in calculating the pharmacokinetic parameters. As in the example above, --GRPID values must take into account all the combinations of analytes and reference time points; both are part of the natural key for both datasets. For each example, PCGRPID and PPGRPID were used to group related records within each respective dataset. The exclusion of some concentration values from the calculation of some parameters affects the values of PCGRPID and PPGRPID for the different situations. To conserve space, the PC and PP domains appear only once, but with 4 --GRPID columns, 1 for each of the example situations.

Note that a submission dataset would contain only 1 --GRPID column with a set of values such as those shown in 1 of the 4 columns in the PC and PP datasets.

### Shared PC Dataset for All Examples

**pc.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PCSEQ | PCGRPID (Example 1) | PCGRPID (Example 2) | PCGRPID (Example 3) | PCGRPID (Example 4) | PCTESTCD | PCTEST | PCCAT | PCORRES | PCORRESU | PCSTRESC | PCSTRESN | PCSTRESU | PCSPEC | PCBLFL | PCLLOQ | PCSTAT | VISITNUM | VISIT | VISITDY | PCDTC | PCENDTC | PCDY | PCTPT | PCTPTNUM | PCTPTREF | PCRFDTC | PCELTM | PCEVLINT |
|-----|---------|--------|---------|-------|---------------------|---------------------|---------------------|---------------------|----------|--------|-------|---------|----------|----------|----------|----------|--------|--------|--------|--------|----------|-------|---------|-------|---------|------|-------|----------|----------|---------|--------|---------|
| 1 | ABC-123 | PC | ABC-123-0001 | 1 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | q | | | | | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | Pre-dose | -1 | Day 1 Dose | 2001-02-01T08:35 | PT0M | |
| 2 | ABC-123 | PC | ABC-123-0001 | 2 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 5 | ng/mL | 5 | 5 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 5 min post | 0.083 | Day 1 Dose | 2001-02-01T08:35 | PT5M | |
| 3 | ABC-123 | PC | ABC-123-0001 | 3 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 38 | ng/mL | 38 | 38 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 30 min post | 0.5 | Day 1 Dose | 2001-02-01T08:35 | PT30M | |
| 4 | ABC-123 | PC | ABC-123-0001 | 4 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 38 | ng/mL | 38 | 38 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 1h post | 1 | Day 1 Dose | 2001-02-01T08:35 | PT1H | |
| 5 | ABC-123 | PC | ABC-123-0001 | 5 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_C | STUDYDRUG | STUDYDRUG | ANALYTE | 30 | ng/mL | 30 | 30 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 2h post | 2 | Day 1 Dose | 2001-02-01T08:35 | PT2H | |
| 6 | ABC-123 | PC | ABC-123-0001 | 6 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_B | STUDYDRUG | STUDYDRUG | ANALYTE | 22 | ng/mL | 22 | 22 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 3h post | 3 | Day 1 Dose | 2001-02-01T08:35 | PT3H | |
| 7 | ABC-123 | PC | ABC-123-0001 | 7 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 16 | ng/mL | 16 | 16 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 4h post | 4 | Day 1 Dose | 2001-02-01T08:35 | PT4H | |
| 8 | ABC-123 | PC | ABC-123-0001 | 8 | DY1_DRGX | EXCLUDE | DY1_DRGX_B | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 12 | ng/mL | 12 | 12 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 6h post | 6 | Day 1 Dose | 2001-02-01T08:35 | PT6H | |
| 9 | ABC-123 | PC | ABC-123-0001 | 9 | DY1_DRGX | EXCLUDE | DY1_DRGX_B | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 9 | ng/mL | 9 | 9 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 8h post | 8 | Day 1 Dose | 2001-02-01T08:35 | PT8H | |
| 10 | ABC-123 | PC | ABC-123-0001 | 10 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 6 | ng/mL | 6 | 6 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 10h post | 10 | Day 1 Dose | 2001-02-01T08:35 | PT10H | |
| 11 | ABC-123 | PC | ABC-123-0001 | 11 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_A | STUDYDRUG | STUDYDRUG | ANALYTE | 4 | ng/mL | 4 | 4 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 12h post | 12 | Day 1 Dose | 2001-02-01T08:35 | PT12H | |
| 12 | ABC-123 | PC | ABC-123-0001 | 12 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1DRGX_D | STUDYDRUG | STUDYDRUG | ANALYTE | 3 | ng/mL | 3 | 3 | ng/mL | PLASMA | | 0.10 | | 1 | Day 1 | 1 | 2001-02-01 | | 1 | 15h post | 15 | Day 1 Dose | 2001-02-01T08:35 | PT15H | |
| 13 | ABC-123 | PC | ABC-123-0001 | 13 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | q | | | | | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | Pre-dose | -1 | Day 8 Dose | 2001-02-08T08:35 | PT0M | |
| 14 | ABC-123 | PC | ABC-123-0001 | 14 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 6 | ng/mL | 6 | 6 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 5 min post | 0.083 | Day 8 Dose | 2001-02-08T08:35 | PT5M | |
| 15 | ABC-123 | PC | ABC-123-0001 | 15 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 40 | ng/mL | 40 | 40 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 30 min post | 0.5 | Day 8 Dose | 2001-02-08T08:35 | PT30M | |
| 16 | ABC-123 | PC | ABC-123-0001 | 16 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 40 | ng/mL | 40 | 40 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 1h post | 1 | Day 8 Dose | 2001-02-08T08:35 | PT1H | |
| 17 | ABC-123 | PC | ABC-123-0001 | 17 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 32 | ng/mL | 32 | 32 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 2h post | 2 | Day 8 Dose | 2001-02-08T08:35 | PT2H | |
| 18 | ABC-123 | PC | ABC-123-0001 | 18 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 22 | ng/mL | 22 | 22 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 3h post | 3 | Day 8 Dose | 2001-02-08T08:35 | PT3H | |
| 19 | ABC-123 | PC | ABC-123-0001 | 19 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 16 | ng/mL | 16 | 16 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 4h post | 4 | Day 8 Dose | 2001-02-08T08:35 | PT4H | |
| 20 | ABC-123 | PC | ABC-123-0001 | 20 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 12 | ng/mL | 12 | 12 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 6h post | 6 | Day 8 Dose | 2001-02-08T08:35 | PT6H | |
| 21 | ABC-123 | PC | ABC-123-0001 | 21 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 9 | ng/mL | 9 | 9 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 8h post | 8 | Day 8 Dose | 2001-02-08T08:35 | PT8H | |
| 22 | ABC-123 | PC | ABC-123-0001 | 22 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 6 | ng/mL | 6 | 6 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 10h post | 10 | Day 8 Dose | 2001-02-08T08:35 | PT10H | |
| 23 | ABC-123 | PC | ABC-123-0001 | 23 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 4 | ng/mL | 4 | 4 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 12h post | 12 | Day 8 Dose | 2001-02-08T08:35 | PT12H | |
| 24 | ABC-123 | PC | ABC-123-0001 | 24 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8DRGX | STUDYDRUG | STUDYDRUG | ANALYTE | 3 | ng/mL | 3 | 3 | ng/mL | PLASMA | | 0.10 | | 8 | Day 8 | 8 | 2001-02-08 | | 8 | 15h post | 15 | Day 8 Dose | 2001-02-08T08:35 | PT15H | |

### Example 1 (All PC records used)

All PC records used to calculate all pharmacokinetic parameters.

This example uses --GRPID values in the PCGRPID (Example 1) and PPGRPID (Example 1) columns.

**Method A (Many to Many, Using PCGRPID and PPGRPID)**

**Rows 1-2:** The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX".
**Rows 3-4:** The relationship with RELID "2" includes all PC records with GRPID = "DY8_DRGX" and all PP records with GRPID = "DY8DRGX".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX | | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PPGRPID | DY8_DRGX | | 2 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY8DRGX | | 2 |

**Method B (One to Many, Using PCSEQ and PPGRPID)**

**Rows 1-13:** The relationship with RELID "1" includes the individual PC records with PCSEQ values "1" to "12" and all PP records with PPGRPID = "DY1DRGX".
**Rows 14-26:** The relationship with RELID "2" includes the individual PC records with PCSEQ values "13" to "24" and all PP records with PPGRPID = "DY8DRGX".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 | | 2 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 14 | | 2 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 15 | | 2 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 16 | | 2 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 17 | | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 18 | | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 19 | | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 20 | | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 21 | | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 22 | | 2 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 23 | | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 24 | | 2 |
| 26 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY8DRGX | | 2 |

**Method C (Many to One, Using PCGRPID and PPSEQ)**

**Rows 1-8:** The relationship with RELID "1" includes all PC records with a PCGRPID = "DY1_DRGX" and PP records with PPSEQ values "1" through "7".
**Rows 9-16:** The relationship with RELID "2" includes all PC records with a PCGRPID = "DY8_DRGX" and PP records with PPSEQ values "8" through "14".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX | | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 1 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1 |
| 6 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 1 |
| 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1 |
| 8 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY8_DRGX | | 2 |
| 10 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 8 | | 2 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 9 | | 2 |
| 12 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 10 | | 2 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 11 | | 2 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 12 | | 2 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 13 | | 2 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 14 | | 2 |

**Method D (One to One, Using PCSEQ and PPSEQ)**

**Rows 1-19:** The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "12" and PP records with PPSEQ values "1" through "7".
**Rows 20-38:** The relationship with RELID "2" includes individual PC records with PCSEQ values "13" through "24" and PP records with PPSEQ values "8" through "14".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 1 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 1 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1 |
| 17 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 1 |
| 18 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1 |
| 19 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 1 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 | | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 14 | | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 15 | | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 16 | | 2 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 17 | | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 18 | | 2 |
| 26 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 19 | | 2 |
| 27 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 20 | | 2 |
| 28 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 21 | | 2 |
| 29 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 22 | | 2 |
| 30 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 23 | | 2 |
| 31 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 24 | | 2 |
| 32 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 8 | | 2 |
| 33 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 9 | | 2 |
| 34 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 10 | | 2 |
| 35 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 11 | | 2 |
| 36 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 12 | | 2 |
| 37 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 13 | | 2 |
| 38 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 14 | | 2 |

### Example 2 (Some PC records excluded)

Only some records in PC were used to calculate all pharmacokinetic parameters; time points 8 and 9 on day 1 were not used for any pharmacokinetic parameters.

This example uses --GRPID values in the PCGRPID (Example 2) and PPGRPID (Example 2) columns. Note that for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".

All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

**Method A (Many to Many, Using PCGRPID and PPGRPID)**

The relationship with RELID "1" includes PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX". PC records with PCGRPID = "EXCLUDE" are not included in this relationship.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX | | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |

**Method B (One to Many, Using PCSEQ and PPGRPID)**

The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "7" and "10" through "12", and all the PP records with PPGRPID = "DY1DRGX".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |

**Method C (Many to One, Using PCGRPID and PPSEQ)**

The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and individual PP records with PPSEQ values "1" through "7".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX | | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 1 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1 |
| 6 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 1 |
| 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1 |
| 8 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 1 |

**Method D (One to One, Using PCSEQ and PPSEQ)**

The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "7" and "10" through "12" and individual PP records with PPSEQ values "1" through "7".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 12 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 1 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 1 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1 |
| 17 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 1 |

### Example 3 (Inconsistent PC usage across parameters)

Only some records in PC were used to calculate some parameters; time points 8 and 9 on day 1 were not used for half-life calculations, but were used for other parameters.

This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID = "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DY1DRGX_HALF", whereas the other PP records have PPGRPID = "DY1DRGX_A".

All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

**Method A (Many to Many, Using PCGRPID and PPGRPID)**

**Rows 1-3:** The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all PP records with PPGRPID = "DY1DRGX_A".
**Rows 4-6:** The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and all PP records with PPGRPID = "DY1DRGX_HALF".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_B | | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_A | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A | | 2 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_HALF | | 2 |

**Method B (One to Many, Using PCSEQ and PPGRPID)**

**Rows 1-13:** The relationship with RELID "1" includes PP records with PCSEQ values "1" through "12" and PP records with PPGRPID = "DY1DRGX_A".
**Rows 14-24:** The relationship with RELID "2" includes PC records with PCSEQ values "1" through "7" and "10" through "12" and PP records with PPGRPID = "DY1DRGX_HALF".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_A | | 1 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 2 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 2 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 2 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 2 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 2 |
| 24 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_HALF | | 2 |

**Method C (Many to One, Using PCGRPID and PPSEQ)**

**Rows 1-7:** The relationship with RELID "1" includes all PP records with PPGRPID values "DY1_DRGX_A" and "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6" and "7".
**Rows 8-10:** The relationship with RELID "2" includes all PP records with PPGRPID value "DY1_DRGX_A" and PP records with PPSEQ values "4" and "5".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_B | | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 1 |
| 6 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1 |
| 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A | | 2 |
| 9 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 2 |
| 10 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 2 |

**Method D (One to One, Using PCSEQ and PPSEQ)**

**Rows 1-17:** The relationship with RELID "1" includes PC records with PCSEQ values of "1" through "12" and PP records with PPSEQ values "1" through "3", "6" and "7".
**Rows 18-29:** The relationship with RELID "2" includes PC records with PCSEQ values of "1" through "7" and "10" through "12" and PP records with PPSEQ values "4" and "5".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 1 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 1 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1 |
| 17 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 1 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 2 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 2 |
| 26 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 2 |
| 27 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 2 |
| 28 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 2 |
| 29 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 2 |

### Example 4 (Complex exclusions)

Only some records in PC were used to calculate parameters; time point 5 was excluded from Tmax, time point 6 from Cmax, and time points 11 and 12 from AUC.

This example uses --GRPID values in the PCGRPID (Example 4) and PPGRPID (Example 4) columns. Note that 4 values of PCGRPID and 4 values of PPGRPID were used.

Because of the complexity of this example, only methods A and D are illustrated.

**Method A (Many to Many, Using PCGRPID and PPGRPID)**

**Rows 1-4:** The relationship with RELID "1" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_C", and "DY1DRGX_D" and the one PP record with PPGRPID = "TMAX".
**Rows 5-8:** The relationship with RELID "2" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_D" and the one PP record with PPGRPID = "CMAX".
**Rows 9-12:** The relationship with RELID "3" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_C" and the one PP record with PPGRPID = "AUC".
**Rows 13-17:** The relationship with RELID "4" includes all PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", "DY1DRGX_C", and "DY1DRGX_D" (in this case, all PC records) and all PP records with PPGRPID = "OTHER".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PP | ABC-123-0001 | PPGRPID | TMAX | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_C | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_D | | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPGRPID | CMAX | | 2 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A | | 2 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_B | | 2 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_D | | 2 |
| 9 | ABC-123 | PP | ABC-123-0001 | PPGRPID | AUC | | 3 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A | | 3 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_B | | 3 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_C | | 3 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | OTHER | | 4 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A | | 4 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_B | | 4 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_C | | 4 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_D | | 4 |

Note that in the RELREC table for method A, the single records in rows 1, 5, 7, and 9, represented by their PPGRPID values, could have been referenced by their PPSEQ values; both identify the records sufficiently.

At least 2 other hybrid approaches would also be acceptable:
- Using PPSEQ values; use PCGRPID values wherever possible
- Using PPGRPID values wherever possible; use PCSEQ values

Method D uses only PCSEQ and PPSEQ values.

**Method D (One to One, Using PCSEQ and PPSEQ)**

**Rows 1-12:** The relationship with RELID "1" includes PC records with PCSEQ values "1" through "4" and "6" through "12" and PP records with PPSEQ = "1".
**Rows 13-24:** The relationship with RELID "2" includes PC records with PCSEQ values "1" through "5" and "7" through "12" and PP records with PPSEQ = "2".
**Rows 24-35:** The relationship with RELID "3" includes PC records with PCSEQ values "1" through "10" and PP records with PPSEQ = "3".
**Rows 36-51:** The relationship with RELID "4" includes PC records with PCSEQ values "1" through "12" and PP records with PPSEQ values "4" through "7".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 12 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1 |
| 13 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 2 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 2 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 2 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 2 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 2 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 2 |
| 24 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 | | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 3 |
| 26 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 3 |
| 27 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 3 |
| 28 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 3 |
| 29 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 3 |
| 30 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 3 |
| 31 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 3 |
| 32 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 3 |
| 33 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 3 |
| 34 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 3 |
| 35 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 | | 3 |
| 36 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 | | 4 |
| 37 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 | | 4 |
| 38 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 | | 4 |
| 39 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 | | 4 |
| 40 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 4 |
| 41 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 | | 4 |
| 42 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 | | 4 |
| 43 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 4 |
| 44 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 | | 4 |
| 45 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 | | 4 |
| 46 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 4 |
| 47 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 4 |
| 48 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 4 |
| 49 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 | | 4 |
| 50 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 4 |
| 51 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 | | 4 |

## PC-PP Conclusions

Relating the datasets (as described in Section 8, Representing Relationships and Data) is the simplest method; however, all time-point concentrations in PC must be used to calculate all parameters for all subjects. If datasets cannot be related, then individual subject records must be related. In either case, the values of PCGRPID and PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.

Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require the assignment of --GRPID values (which are optional) in both the PC and PP datasets. Method D, in contrast, does not require the assignment of --GRPID values, relying instead on the required --SEQ values in both datasets to relate the records. Although Method D results in the largest number of RELREC records compared to the other methods, it may be the easiest to implement consistently across the range of complexities shown in the examples. Two additional methods, methods B and C, are also shown for Examples 1-3. They represent hybrid approaches, using --GRPID values in only 1 dataset (PP and PC, respectively) and --SEQ values for the other. These methods are best suited for sponsors who want to minimize the number of RELREC records while not having to assign --GRPID values in both domains. Methods B and C would not be ideal, however, if one expected complex scenarios as shown in Example 4.

## PC-PP — Suggestions for Implementing RELREC in the Submission of PK Data

Determine which of the scenarios best reflects how PP data are related to PC data. Questions that should be considered include:

1. Do all parameters for each PK profile use all concentrations for all subjects? If so, create a PPGRPID value for all PP records and a PCGRPID value for all PC records for each profile for each subject, analyte, and reference time point. Decide whether to relate datasets or records. If choosing the latter, create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

2. Do all parameters use the same concentrations, although maybe not all of them (Example 2)? If so, create a single PPGRPID value for all PP records, and 2 PCGRPID values for the PC records: a PCGRPID value for ones that were used and a PCGRPID value for those that were not used. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

3. Do any parameters use the same concentrations, but not as consistently as shown in Examples 1 and 2? If so, refer to Example 3. Assign a GRPID value to the PP records that use the same concentrations. More than 1 PPGRPID value may be necessary. Assign as many PCGRPID values in the PC domain as needed to group these records. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

4. If none of the above applies, or the data become difficult to group, then start with Example 4, and decide which RELREC method would be easiest to implement and represent.
