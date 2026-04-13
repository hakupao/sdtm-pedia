# PP — Examples

*Note: PC and PP share a combined examples section (6.3.5.9.3 Relating PP Records to PC Records). The PP parameter data tables are shown here; see also PC examples for the concentration data and detailed RELREC method descriptions.*

Due to space limitations, not all expected or permissible findings variables are included in the example for this domain.

## Example 1

This example shows PK parameters calculated from time-concentration profiles for the parent drug and 1 metabolite in plasma and urine for one subject. Note that PPRFDTC is populated in order to link the PP records to the respective PC records. In this example, PPSPEC is null for observed total clearance (PPTESTCD = "CLO") records because it is calculated from multiple specimen sources (i.e., plasma and urine).

**Rows 1-12:** Show parameters for day 1.
**Rows 13-24:** Show parameters for day 11.

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|---------|
| 1 | ABC-123 | PP | ABC-123-001 | 1 | DRUGA_DAY1 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 2 | ABC-123 | PP | ABC-123-001 | 2 | DRUGA_DAY1 | CMAX | Max Conc | DRUG A PARENT | 6.92 | ng/mL | 6.92 | 6.92 | ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 3 | ABC-123 | PP | ABC-123-001 | 3 | DRUGA_DAY1 | AUCALL | AUC All | DRUG A PARENT | 45.5 | h*ng/mL | 45.5 | 45.5 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 4 | ABC-123 | PP | ABC-123-001 | 4 | DRUGA_DAY1 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 43.6 | h*ng/mL | 43.6 | 43.6 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 5 | ABC-123 | PP | ABC-123-001 | 5 | DRUGA_DAY1 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.74 | h | 7.74 | 7.74 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 6 | ABC-123 | PP | ABC-123-001 | 6 | DRUGA_DAY1 | VZFO | Vz Obs by F | DRUG A PARENT | 256 | L | 256000 | 256 | L | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 7 | ABC-123 | PP | ABC-123-001 | 7 | DRUGA_DAY1 | CLFO | Total CL Obs by F | DRUG A PARENT | 20.2 | L/hr | 20200 | 20.2 | L/h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 |
| 8 | ABC-123 | PP | ABC-123-001 | 8 | DRUGA_DAY14 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 9 | ABC-123 | PP | ABC-123-001 | 9 | DRUGA_DAY14 | CMAX | Max Conc | DRUG A PARENT | 6.51 | ng/mL | 6.51 | 6.51 | ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 10 | ABC-123 | PP | ABC-123-001 | 10 | DRUGA_DAY14 | AUCALL | AUC All | DRUG A PARENT | 34.2 | h*ng/mL | 34.2 | 34.2 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 11 | ABC-123 | PP | ABC-123-001 | 11 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 35.6 | h*ng/mL | 35.6 | 35.6 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 12 | ABC-123 | PP | ABC-123-001 | 12 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 38.4 | h*ng/mL | 38.4 | 38.4 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 13 | ABC-123 | PP | ABC-123-001 | 13 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 2.78 | h*ng/mL | 2.78 | 2.78 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 14 | ABC-123 | PP | ABC-123-001 | 14 | DRUGA_DAY14 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.6 | h | 7.6 | 7.6 | h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 15 | ABC-123 | PP | ABC-123-001 | 15 | DRUGA_DAY14 | VZFO | Vz Obs by F | DRUG A PARENT | 283 | L | 283 | 283 | L | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |
| 16 | ABC-123 | PP | ABC-123-001 | 16 | DRUGA_DAY14 | CLFO | Total CL Obs by F | DRUG A PARENT | 28.1 | L/h | 28.1 | 28.1 | L/h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-25 15T08:00 |

The SUPPPP dataset example shows the specific condition under which the PK analysis was performed.

**supppp.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC-123 | PP | 123-1001 | PPSEQ | 1 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |
| 2 | ABC-123 | PP | 123-1001 | PPSEQ | 2 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |
| 3 | ABC-123 | PP | 123-1001 | PPSEQ | 3 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |
| 4 | ABC-123 | PP | 123-1001 | PPSEQ | 4 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |
| 5 | ABC-123 | PP | 123-1001 | PPSEQ | 5 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |
| 6 | ABC-123 | PP | 123-1001 | PPSEQ | 6 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |
| 7 | ABC-123 | PP | 123-1001 | PPSEQ | 7 | PKCOND | Condition of PK Analysis | SINGLE DOSE | Collected | |

## Example 2

This example shows various AUCs calculated using sponsor-defined formulas or the linear-log trapezoidal method.

**Rows 1-3:** Show the "AUC from T1 to T2" measurements for Drug Parent (row 1), Drug Metabolite 1 (row 2) and Drug Metabolite 2 (row 3). These parameters are calculated using the LIN-LOG TRAPEZOIDAL METHOD which is in PPANMETH.
**Row 4:** Shows the "Ratio AUC" measurement of Drug Metabolite 1 to Drug Parent. Instead of pre-coordinating "Ratio AUC of Drug Metabolite 1 to Drug Parent" all into the PPTEST, PPANMETH is used to describe the numerator (Drug Metabolite 1) and the denominator (Drug Parent) values that contribute to the Ratio AUC calculation in PPTEST. This post-coordination approach liberates the PPTEST variable from having to house hyper-specific, pre-coordinated PK parameter values.
**Row 5:** Shows the "Ratio AUC" measurement of Drug Metabolite 2 to Drug Metabolite 1. Note the PPTEST is Ratio AUC, whereas DRUG METABOLITE 2 TO METABOLITE 1 is in PPANMETH.
**Rows 6-7:** Show AUC Infinity Obs and AUC Infinity Pred for the DRUG PARENT. Both are calculated using the LIN-LOG TRAPEZOIDAL METHOD which is in PPANMETH.

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPRFID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | PPANMETH | PPFAST | PPNOMDY | PPRFDTC |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|--------|---------|---------|
| 1 | ABC-123 | PP | 123-1001 | 1 | B2222 | AUCINT | AUC from T1 to T2 | DRUG PARENT | 154.1 | h*ng/L | 154.1 | 154.1 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 2 | ABC-123 | PP | 123-1001 | 2 | B2222 | AUCINT | AUC from T1 to T2 | DRUG METABOLITE 1 | 144.5 | h*ng/L | 144.5 | 144.5 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 3 | ABC-123 | PP | 123-1001 | 3 | B2222 | AUCINT | AUC from T1 to T2 | DRUG METABOLITE 2 | 294.7 | h*ng/L | 294.7 | 294.7 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 4 | ABC-123 | PP | 123-1001 | 4 | B2222 | RAAUC | Ratio AUC | DRUG METABOLITE 1 | 1.07 | | 1.07 | 1.07 | | PLASMA | DRUG METABOLITE 1 TO DRUG PARENT | Y | 1 | 2001-02-01T12:00 |
| 5 | ABC-123 | PP | 123-1001 | 5 | B2222 | RAAUC | Ratio AUC | DRUG METABOLITE 2 | 0.52 | | 0.52 | 0.52 | | PLASMA | DRUG METABOLITE 2 TO METABOLITE 1 | Y | 1 | 2001-02-01T12:00 |
| 6 | ABC-123 | PP | 123-1001 | 6 | B2222 | AUCIFO | AUC Infinity Obs | DRUG PARENT | 520 | h*ng/L | 520 | 520 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 7 | ABC-123 | PP | 123-1001 | 7 | B2222 | AUCIFP | AUC Infinity Pred | DRUG PARENT | 510 | h*ng/L | 510 | 510 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |

## Example 3

This example shows the use of PPSTINT and PPENINT to describe the AUC segments for the test code "AUCINT", the area under the curve from time T1 to time T2. Time T1 is represented in PPSTINT as the elapsed time since PPRFDTC and time T2 is represented in PPENINT as the elapsed time since PPRFDTC.

**Rows 1-7:** Show parameters for day 1.
**Rows 8-14:** Show parameters for day 14.

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFDTC | PPSTINT | PPENINT |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|---------|---------|---------|
| 1 | ABC-123 | PP | ABC-123-001 | 1 | DRUGA_DAY1 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | | |
| 2 | ABC-123 | PP | ABC-123-001 | 2 | DRUGA_DAY1 | CMAX | Max Conc | DRUG A PARENT | 6.92 | ng/mL | 6.92 | 6.92 | ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | | |
| 3 | ABC-123 | PP | ABC-123-001 | 3 | DRUGA_DAY1 | AUCALL | AUC All | DRUG A PARENT | 45.5 | h*ng/mL | 45.5 | 45.5 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | | |
| 4 | ABC-123 | PP | ABC-123-001 | 4 | DRUGA_DAY1 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 43.6 | h*ng/mL | 43.6 | 43.6 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | PT0M | PT24H |
| 5 | ABC-123 | PP | ABC-123-001 | 5 | DRUGA_DAY1 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.74 | h | 7.74 | 7.74 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | | |
| 6 | ABC-123 | PP | ABC-123-001 | 6 | DRUGA_DAY1 | VZFO | Vz Obs by F | DRUG A PARENT | 256 | L | 256000 | 256 | L | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | | |
| 7 | ABC-123 | PP | ABC-123-001 | 7 | DRUGA_DAY1 | CLFO | Total CL Obs by F | DRUG A PARENT | 20.2 | L/h | 20200 | 20.2 | L/h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-25 01T08:00 | | |

*Rows 8-14 follow the same pattern for DRUGA_DAY14 with additional PPSTINT/PPENINT values for AUCINT records (e.g., PT0M/PT24H, PT0M/PT48H).*

## Shared PP Dataset for RELREC Examples

The shared PP dataset contains 14 rows showing PK parameters (TMAX, CMAX, AUC, AUCALL, AUCINT, LAMZHL, VZO, CLO) for Drug X across Day 1 and Day 8, with 4 PPGRPID columns showing the grouping values for the 4 RELREC method examples described in the PC examples section.

*See PC examples for the full description of RELREC Methods A through D and their corresponding relrec.xpt tables.*
