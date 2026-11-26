# PP — Examples

*Note: PC and PP share a combined examples section (6.3.5.9.3 Relating PP Records to PC Records). The PP parameter data tables are shown here; see also PC examples for the concentration data and detailed RELREC method descriptions.*

Due to space limitations, not all expected or permissible findings variables are included in the example for this domain.

## Example 1

This example shows PK parameters calculated from time-concentration profiles for the parent drug and 1 metabolite in plasma and urine for one subject. Note that PPRFTDTC is populated in order to link the PP records to the respective PC records. In this example, PPSPEC is null for observed total clearance (PPTESTCD = "CLO") records because it is calculated from multiple specimen sources (i.e., plasma and urine).

**Rows 1-12:** Show parameters for day 1.
**Rows 13-24:** Show parameters for day 11.

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFTDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|
| 1 | ABC-123 | PP | ABC-123-0001 | 1 | DAY1_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.87 | h | 1.87 | 1.87 | H | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 2 | ABC-123 | PP | ABC-123-0001 | 2 | DAY1_PAR | CMAX | Max Conc | DRUG A PARENT | 44.5 | ug/L | 44.5 | 44.5 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 3 | ABC-123 | PP | ABC-123-0001 | 3 | DAY1_PAR | AUCALL | AUC All | DRUG A PARENT | 294.7 | h*mg/L | 294.7 | 294.7 | h*mg/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 4 | ABC-123 | PP | ABC-123-0001 | 4 | DAY1_PAR | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 0.75 | h | 0.75 | 0.75 | H | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 5 | ABC-123 | PP | ABC-123-0001 | 5 | DAY1_PAR | VZO | Vz Obs | DRUG A PARENT | 10.9 | L | 10.9 | 10.9 | L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 6 | ABC-123 | PP | ABC-123-0001 | 6 | DAY1_PAR | CLO | Total CL Obs | DRUG A PARENT | 1.68 | L/h | 1.68 | 1.68 | L/h | | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 7 | ABC-123 | PP | ABC-123-0001 | 7 | DAY1_MET | TMAX | Time of CMAX | DRUG A METABOLITE | 0.94 | h | 0.94 | 0.94 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 8 | ABC-123 | PP | ABC-123-0001 | 8 | DAY1_MET | CMAX | Max Conc | DRUG A METABOLITE | 22.27 | ug/L | 22.27 | 22.27 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 9 | ABC-123 | PP | ABC-123-0001 | 9 | DAY1_MET | AUCALL | AUC All | DRUG A METABOLITE | 147.35 | h*mg/L | 147.35 | 147.35 | h*mg/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 10 | ABC-123 | PP | ABC-123-0001 | 10 | DAY1_MET | LAMZHL | Half-Life Lambda z | DRUG A METABOLITE | 0.38 | h | 0.38 | 0.38 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 11 | ABC-123 | PP | ABC-123-0001 | 11 | DAY1_MET | VZO | Vz Obs | DRUG A METABOLITE | 5.45 | L | 5.45 | 5.45 | L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 12 | ABC-123 | PP | ABC-123-0001 | 12 | DAY1_MET | CLO | Total CL Obs | DRUG A METABOLITE | 0.84 | L/h | 0.84 | 0.84 | L/h | | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 13 | ABC-123 | PP | ABC-123-0001 | 13 | DAY11_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.91 | h | 1.91 | 1.91 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 14 | ABC-123 | PP | ABC-123-0001 | 14 | DAY11_PAR | CMAX | Max Conc | DRUG A PARENT | 46.0 | ug/L | 46.0 | 46.0 | ug/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 15 | ABC-123 | PP | ABC-123-0001 | 15 | DAY11_PAR | AUCALL | AUC All | DRUG A PARENT | 289.0 | h*mg/L | 289.0 | 289.0 | h*mg/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 16 | ABC-123 | PP | ABC-123-0001 | 16 | DAY11_PAR | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 0.77 | h | 0.77 | 0.77 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 17 | ABC-123 | PP | ABC-123-0001 | 17 | DAY11_PAR | VZO | Vz Obs | DRUG A PARENT | 10.7 | L | 10.7 | 10.7 | L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 18 | ABC-123 | PP | ABC-123-0001 | 18 | DAY11_PAR | CLO | Total CL Obs | DRUG A PARENT | 1.75 | L/h | 1.75 | 1.75 | L/h | | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 19 | ABC-123 | PP | ABC-123-0001 | 19 | DAY11_MET | TMAX | Time of CMAX | DRUG A METABOLITE | 0.96 | h | 0.96 | 0.96 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 20 | ABC-123 | PP | ABC-123-0001 | 20 | DAY11_MET | CMAX | Max Conc | DRUG A METABOLITE | 23.00 | ug/L | 23.00 | 23.00 | ug/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 21 | ABC-123 | PP | ABC-123-0001 | 21 | DAY11_MET | AUCALL | AUC All | DRUG A METABOLITE | 144.50 | h*mg/L | 144.50 | 144.50 | h*mg/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 22 | ABC-123 | PP | ABC-123-0001 | 22 | DAY11_MET | LAMZHL | Half-Life Lambda z | DRUG A METABOLITE | 0.39 | h | 0.39 | 0.39 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 23 | ABC-123 | PP | ABC-123-0001 | 23 | DAY11_MET | VZO | Vz Obs | DRUG A METABOLITE | 5.35 | L | 5.35 | 5.35 | L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 24 | ABC-123 | PP | ABC-123-0001 | 24 | DAY11_MET | CLO | Total CL Obs | DRUG A METABOLITE | 0.88 | L/h | 0.88 | 0.88 | L/h | | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |

## Example 2

This example shows various AUCs calculated using sponsor-defined formulas or the linear-log trapezoidal method.

**Rows 1-3:** Show the "AUC from T1 to T2" measurements for Drug Parent (row 1), Drug Metabolite 1 (row 2) and Drug Metabolite 2 (row 3). These parameters are calculated using the LIN-LOG TRAPEZOIDAL METHOD which is in PPANMETH.
**Row 4:** Shows the "Ratio AUC" measurement of Drug Metabolite 1 to Drug Parent. Instead of pre-coordinating "Ratio AUC of Drug Metabolite 1 to Drug Parent" all into the PPTEST, PPANMETH is used to describe the numerator (Drug Metabolite 1) and the denominator (Drug Parent) values that contribute to the Ratio AUC calculation in PPTEST. This post-coordination approach liberates the PPTEST variable from having to house hyper-specific, pre-coordinated PK parameter values.
**Row 5:** Shows the "Ratio AUC" measurement of Drug Metabolite 2 to Drug Metabolite 1. Note the PPTEST is Ratio AUC, whereas DRUG METABOLITE 2 TO METABOLITE 1 is in PPANMETH.
**Rows 6-7:** Show AUC Infinity Obs and AUC Infinity Pred for the DRUG PARENT. Both are calculated using the LIN-LOG TRAPEZOIDAL METHOD which is in PPANMETH.

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPRFID | PPTESTCD | PPTEST | PPCAT | PPSCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | PPANMETH | PPFAST | PPNOMDY | PPRFTDTC |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|--------|---------|----------|----------|----------|----------|--------|----------|--------|---------|---------|
| 1 | ABC-123 | PP | 123-1001 | 1 | B2222 | AUCINT | AUC from T1 to T2 | DRUG PARENT | NCA | 154.1 | h*ng/L | 154.1 | 154.1 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 2 | ABC-123 | PP | 123-1001 | 2 | B2222 | AUCINT | AUC from T1 to T2 | DRUG METABOLITE 1 | NCA | 144.5 | h*ng/L | 144.5 | 144.5 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 3 | ABC-123 | PP | 123-1001 | 3 | B2222 | AUCINT | AUC from T1 to T2 | DRUG METABOLITE 2 | NCA | 294.7 | h*ng/L | 294.7 | 294.7 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 4 | ABC-123 | PP | 123-1001 | 4 | B2222 | RAAUC | Ratio AUC | DRUG METABOLITE 1 | NCA | 1.07 | | 1.07 | 1.07 | | PLASMA | DRUG METABOLITE 1 TO DRUG PARENT | Y | 1 | 2001-02-01T12:00 |
| 5 | ABC-123 | PP | 123-1001 | 5 | B2222 | RAAUC | Ratio AUC | DRUG METABOLITE 2 | NCA | 0.52 | | 0.52 | 0.52 | | PLASMA | DRUG METABOLITE 2 TO METABOLITE 1 | Y | 1 | 2001-02-01T12:00 |
| 6 | ABC-123 | PP | 123-1001 | 6 | B2222 | AUCIFO | AUC Infinity Obs | DRUG PARENT | NCA | 520 | h*ng/L | 520 | 520 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 7 | ABC-123 | PP | 123-1001 | 7 | B2222 | AUCIFP | AUC Infinity Pred | DRUG PARENT | NCA | 510 | h*ng/L | 510 | 510 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |

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
| 7 | ABC-123 | PP | 123-1001 | PPSEQ | 7 | PKCOND | Condition of PK Analysis | SINGLE DOSE | | |

## Example 3

This example shows the use of PPSTINT and PPENINT to describe the AUC segments for the test code "AUCINT", the area under the curve from time T1 to time T2. Time T1 is represented in PPSTINT as the elapsed time since PPRFTDTC and time T2 is represented in PPENINT as the elapsed time since PPRFTDTC.

**Rows 1-7:** Show parameters for day 1.
**Rows 8-14:** Show parameters for day 14.

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFTDTC | PPSTINT | PPENINT |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|---------|---------|---------|
| 1 | ABC-123 | PP | ABC-123-001 | 1 | DRUGA_DAY1 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | | |
| 2 | ABC-123 | PP | ABC-123-001 | 2 | DRUGA_DAY1 | CMAX | Max Conc | DRUG A PARENT | 6.92 | ng/mL | 6.92 | 6.92 | ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | | |
| 3 | ABC-123 | PP | ABC-123-001 | 3 | DRUGA_DAY1 | AUCALL | AUC All | DRUG A PARENT | 45.5 | h*ng/mL | 45.5 | 45.5 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | | |
| 4 | ABC-123 | PP | ABC-123-001 | 4 | DRUGA_DAY1 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 43.6 | h*ng/mL | 43.6 | 43.6 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | PT0M | PT24H |
| 5 | ABC-123 | PP | ABC-123-001 | 5 | DRUGA_DAY1 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.74 | h | 7.74 | 7.74 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | | |
| 6 | ABC-123 | PP | ABC-123-001 | 6 | DRUGA_DAY1 | VZFO | Vz Obs by F | DRUG A PARENT | 256 | L | 256000 | 256 | L | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | | |
| 7 | ABC-123 | PP | ABC-123-001 | 7 | DRUGA_DAY1 | CLFO | Total CL Obs by F | DRUG A PARENT | 20.2 | L/hr | 20200 | 20.2 | L/h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | | |
| 8 | ABC-123 | PP | ABC-123-001 | 15 | DRUGA_DAY14 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | | |
| 9 | ABC-123 | PP | ABC-123-001 | 16 | DRUGA_DAY14 | CMAX | Max Conc | DRUG A PARENT | 6.51 | ng/mL | 6.51 | 6.51 | ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | | |
| 10 | ABC-123 | PP | ABC-123-001 | 17 | DRUGA_DAY14 | AUCALL | AUC All | DRUG A PARENT | 34.2 | h*ng/mL | 34.2 | 34.2 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | | |
| 11 | ABC-123 | PP | ABC-123-001 | 18 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 35.6 | h*ng/mL | 35.6 | 35.6 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | PT0M | PT24H |
| 12 | ABC-123 | PP | ABC-123-001 | 19 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 38.4 | h*ng/mL | 38.4 | 38.4 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | PT0M | PT48H |
| 13 | ABC-123 | PP | ABC-123-001 | 20 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 2.78 | h*ng/mL | 2.78 | 2.78 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | PT24H | PT48H |
| 14 | ABC-123 | PP | ABC-123-001 | 21 | DRUGA_DAY14 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.6 | h | 7.6 | 7.6 | h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | | |
| 15 | ABC-123 | PP | ABC-123-001 | 22 | DRUGA_DAY14 | VZFO | Vz Obs by F | DRUG A PARENT | 283 | L | 283 | 283 | L | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | | |
| 16 | ABC-123 | PP | ABC-123-001 | 23 | DRUGA_DAY14 | CLFO | Total CL Obs by F | DRUG A PARENT | 28.1 | L/h | 28.1 | 28.1 | L/h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | | |

## Pharmacokinetic Parameters (PP) Dataset for All Examples

The shared PP dataset contains 12 rows showing PK parameters (TMAX, CMAX, AUCALL, LAMZHL, VZO, CLO) for Drug X (STUDYDRUG analyte) across Day 1 and Day 8, with 4 PPGRPID columns showing the grouping values for the 4 RELREC method examples described in the PC examples section.

> See [PC/assumptions.md](../PC/assumptions.md#pc-pp--relating-records) for this table.

*See PC examples for the full description of RELREC Methods A through D and their corresponding relrec.xpt tables.*

## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)

The full 4 worked Examples (1-4) with complete `relrec.xpt` tables for all 4 Methods (A/B/C/D) appear in `PC/examples.md` (the shared §6.3.5.9.3 host). This section gives a PP-domain-focused quick reference of how each Method appears on the PP side, plus one abbreviated `relrec.xpt` showing the actual PP rows for Method C.

### Method label mapping (anti-drift anchor)

| Method | Cardinality | PC-side IDVAR | PP-side IDVAR |
|--------|-------------|---------------|---------------|
| **A** | Many-to-Many | `PCGRPID` | `PPGRPID` |
| **B** | One-to-Many | `PCSEQ` | `PPGRPID` |
| **C** | Many-to-One | `PCGRPID` | `PPSEQ` |
| **D** | One-to-One | `PCSEQ` | `PPSEQ` |

These four pairs are the canonical mappings from SDTMIG v3.4 §6.3.5.9.3. When answering Method-label questions, cite this table directly — do not infer labels from cardinality alone.

### Method A — Many to Many, Using PCGRPID and PPGRPID (p277)

PP-side row form: `IDVAR = PPGRPID`, `IDVARVAL = <ppgrpid-value>` (e.g., `DY1DRGX`).

- Rows 1-2: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX".
- Rows 3-4: The relationship with RELID "2" includes all PC records with PCGRPID = "DY8_DRGX" and all PP records with PPGRPID = "DY8DRGX".

### Method B — One to Many, Using PCSEQ and PPGRPID (pp 277-278)

PP-side row form: `IDVAR = PPGRPID` (one PP-side row collects an entire PP group per RELID).

- Rows 1-13: The relationship with RELID "1" includes individual PC records with PCSEQ values "1" to "12" and all PP records with PPGRPID = "DY1DRGX".
- Rows 14-26: The relationship with RELID "2" includes individual PC records with PCSEQ values "13" to "24" and all PP records with PPGRPID = "DY8DRGX".

### Method C — Many to One, Using PCGRPID and PPSEQ (p278)

PP-side row form: `IDVAR = PPSEQ`, `IDVARVAL = <ppseq>` (one PP-side row per individual PP record).

- Rows 1-8: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and PP records with PPSEQ values "1" through "7".
- Rows 9-16: The relationship with RELID "2" includes all PC records with PCGRPID = "DY8_DRGX" and PP records with PPSEQ values "8" through "14".

**relrec.xpt (Method C, abbreviated to show PP-side rows for RELID = "1"; full table in `PC/examples.md`)**

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

Reading the PP-side rows: each individual PP record (PPSEQ 1 through 7) carries its own row in `relrec.xpt`, pointing back to the same `RELID = "1"` as the PC group `PCGRPID = "DY1_DRGX"`.

### Method D — One to One, Using PCSEQ and PPSEQ (pp 278-279)

PP-side row form: `IDVAR = PPSEQ`, one PP-side row per PP record, paired with one PC-side row per PC record (the most verbose form).

- The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "12" and individual PP records with PPSEQ values "1" through "7".
- The relationship with RELID "2" includes individual PC records with PCSEQ values "13" through "24" and individual PP records with PPSEQ values "8" through "14".
