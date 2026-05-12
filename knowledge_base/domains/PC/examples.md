# PC — Examples

*Note: PC and PP share a combined examples section (§6.3.5.9.3 Relating PP Records to PC Records). The shared PC/PP datasets, dataset-level RELREC discussion, conclusions, and implementation suggestions are in `PC/assumptions.md`. This file contains the 4 worked Examples (1–4) illustrating the 4 RELREC methods (A/B/C/D) for relating PC to PP records.*

Due to space limitations, not all expected or permissible findings variables are included in the example for this domain.

## §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples

### Example 1

All PC records used to calculate all pharmacokinetic parameters.

This example uses --GRPID values in the PCGRPID (Example 1) and PPGRPID (Example 1) columns.

#### Method A (Many to Many, Using PCGRPID and PPGRPID)

- Rows 1-2: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX".
- Rows 3-4: The relationship with RELID "2" includes all PC records with GRPID = "DY8_DRGX" and all PP records with GRPID = "DY8DRGX".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX | | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY8_DRGX | | 2 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY8DRGX | | 2 |

#### Method B (One to Many, Using PCSEQ and PPGRPID)

- Rows 1-13: The relationship with RELID "1" includes the individual PC records with PCSEQ values "1" to "12" and all PP records with PPGRPID = "DY1DRGX".
- Rows 14-26: The relationship with RELID "2" includes the individual PC records with PCSEQ values "13" to "24" and all PP records with PPGRPID = "DY8DRGX".

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
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 | | 1 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 14 | | 1 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 15 | | 1 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 16 | | 1 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 17 | | 1 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 18 | | 1 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 19 | | 1 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 20 | | 1 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 21 | | 1 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 22 | | 1 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 23 | | 1 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 24 | | 1 |
| 26 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |

#### Method C (Many to One, Using PCGRPID and PPSEQ)

- Rows 1-8: The relationship with RELID = "1" includes all PC records with a PCGRPID = "DY1_DRGX" and PP records with PPSEQ values "1" through "7".
- Rows 9-16: The relationship with RELID = "2" includes all PC records with a PCGRPID = "DY8_DRGX" and PP records with PPSEQ values of "8" through "14".

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

#### Method D (One to One, Using PCSEQ and PPSEQ)

- Rows 1-19: The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "12" and "10" through "12" and individual PP records with PPSEQ values "1 through 7".
- Rows 20-38: The relationship with RELID "2" includes individual PC records with PCSEQ values "13" through "24" and PP records with PPSEQ values "8" through "14".

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

### Example 2

Only some records in PC were used to calculate all pharmacokinetic parameters; time points 8 and 9 on day 1 were not used for any pharmacokinetic parameters.

This example uses --GRPID values in the PCGRPID (Example 2) and PPGRPID (Example 2) columns. Note that for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".

All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

#### Method A (Many to Many, Using PCGRPID and PPGRPID)

The relationship with RELID "1" includes PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX". PC records with PCGRPID = "EXCLUDE" are not included in this relationship.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX | | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |

#### Method B (One to Many, Using PCSEQ and PPGRPID)

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
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 | | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 | | 1 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1 |

#### Method C (Many to One, Using PCGRPID and PPSEQ)

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

#### Method D (One to One, Using PCSEQ and PPSEQ)

The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "7" and "10" through "12" and individual PP records with PPSEQ values "1 through 7".

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

### Example 3

Only some records in PC were used to calculate some parameters; time points 8 and 9 on day 1 were not used for half-life calculations, but were used for other parameters.

This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID = "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DYDRGX_HALF", whereas the other PP records have PPGRPID = "DY1DRGX_A".

All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

#### Method A (Many to Many, Using PCGRPID and PPGRPID)

- Rows 1-3: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all PP records with PPGRPID = "DYIDRGX_A".
- Rows 4-6: The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and all PP records with PPGRPID = "DYIDRGX_HALF".

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A | | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_B | | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DYIDRGX_A | | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A | | 2 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_HALF | | 2 |

#### Method B (One to Many, Using PCSEQ and PPGRPID)

- Rows 1-13: The relationship with RELID "1" includes PP records with PCSEQ values "1" through "12" and PP records with PPGRPID = "DY1DRGX_A".
- Rows 14-24: The relationship with RELID "2" includes PP records with PCSEQ values "1" through "7" and "10" through "12" and PP records with PPGRPID = "DY1DRGX_HALF".

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

#### Method C (Many to One, Using PCGRPID and PPSEQ)

- Rows 1-7: The relationship with RELID "1" includes all PP records with PGRPID values "DY1_DRGX_A" and "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
- Rows 8-10: The relationship with RELID "2" includes all PP records with PGRPID value "DY1_DRGX_A" and PP records with PPSEQ values "4" and "5".

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

#### Method D (One to One, Using PCSEQ and PPSEQ)

- Rows 1-17: The relationship with RELID "1" includes PC records with PCSEQ values of "1" through "12" and PP records with PPSEQ values "1" through "3" and "6" and "7".
- Rows 18-29: The relationship with RELID "2" includes PC records with PCSEQ values of "1" through "7" and "10" through "12" and PP records with PPSEQ values "4" and "5".

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

### Example 4

Only some records in PC were used to calculate parameters; time point 5 was excluded from Tmax, time point 6 from Cmax, and time points 11 and 12 from AUC.

This example uses --GRPID values in the PCGRPID (Example 4) and PPGRPID (Example 4) columns. Note that 4 values of PCGRPID and 4 values of PPGRPID were used.

Because of the complexity of this example, only methods A and D are illustrated.

#### Method A (Many to Many, Using PCGRPID and PPGRPID)

- Rows 1-4: The relationship with RELID "1" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_C", and "DY1DRGX_D" and the one PP record with PPGRPID = "TMAX".
- Rows 5-8: The relationship with RELID "2" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_D" and the one PP record with PPGRPID = "CMAX".
- Rows 9-12: The relationship with RELID "3" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_C" and the one PP record with PPGRPID = "AUC".
- Rows 13-17: The relationship with RELID "4" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", "DY1DRGX_C", and "DY1DRGX_D" (in this case, all PC records) and all PP records with PPGRPID = "OTHER".

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

Note that in the RELREC table for method A, the single records in rows 1, 3, 5, 7, and 9, represented by their PPGRPID values, could have been referenced by their PPSEQ values; both identify the records sufficiently.

At least 2 other hybrid approaches would also be acceptable:

- Using PPSEQ values; use PCGRPID values wherever possible
- Using PPGRPID values wherever possible; use PCSEQ values

Method D uses only PCSEQ and PPSEQ values.

#### Method D (One to One, Using PCSEQ and PPSEQ)

- Rows 1-12: The relationship with RELID "1" includes PC records with PCSEQ values "1" through "4" and "6" through "12" and PP records with PPSEQ = "1".
- Rows 13-24: The relationship with RELID "2" includes PC records with PCSEQ values "1" through "5" and "7" through "12" and PP records with PPSEQ = "2".
- Rows 24-35: The relationship with RELID "3" includes PC records with PCSEQ values "1" through "10" and PP records with PPSEQ = "3".
- Rows 36-51: The relationship with RELID "4" includes PC records with PCSEQ values "1" through "12" and PP records with PPSEQ values "4" through "7".

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
