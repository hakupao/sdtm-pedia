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

*Note: The PC Example 1 table contains 32 rows and over 25 columns including STUDYID, DOMAIN, USUBJID, PCSEQ, PCGRPID, PCREFID, PCTESTCD, PCTEST, PCCAT, PCORRES, PCORRESU, PCSTRESC, PCSTRESN, PCSTRESU, PCSPEC, PCBLFL, PCLLOQ, PCSTAT, PCDTC, PCENDTC, PCDY, PCTPT, PCTPTNUM, PCTPTREF, PCRFDTC, PCELTM, PCEVLINT. Representative data includes Drug X and Drug A Metabolite concentrations in PLASMA and URINE at multiple time points (pre-dose, 5 min, 25 min, 75 min, 100 min, 2h, 4h, 6h, 8h, 10h, 12h, 15h, 20h, 24h) across Day 1 Dose and Day 11 Dose, plus VOLUME and PH specimen properties for urine samples.*

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

The shared PC dataset contains 24 rows of Drug X concentration data (STUDYDRUG analyte) at various time points across Day 1 Dose and Day 8 Dose, with 4 PCGRPID columns showing the grouping values for Examples 1-4.

### Example 1 (All PC records used)

All PC records used to calculate all pharmacokinetic parameters. This example uses --GRPID values in the PCGRPID (Example 1) and PPGRPID (Example 1) columns.

**Method A (Many to Many, Using PCGRPID and PPGRPID):** The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX". The relationship with RELID "2" includes all PC records with GRPID = "DY8_DRGX" and all PP records with GRPID = "DY8DRGX".

**Method B (One to Many, Using PCSEQ and PPGRPID):** The relationship with RELID "1" includes the individual PC records with PCSEQ values "1" to "12" and all PP records with PPGRPID = "DY1DRGX". The relationship with RELID "2" includes the individual PC records with PCSEQ values "13" to "24" and all PP records with PPGRPID = "DY8DRGX".

**Method C (Many to One, Using PCGRPID and PPSEQ):** The relationship with RELID "1" includes all PC records with a PCGRPID = "DY1_DRGX" and PP records with PPSEQ values "1" through "7". The relationship with RELID "2" includes all PC records with a PCGRPID = "DY8_DRGX" and PP records with PPSEQ values "8" through "14".

**Method D (One to One, Using PCSEQ and PPSEQ):** The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "12" and PP records with PPSEQ = "1". The relationship with RELID "2" includes individual PC records with PCSEQ values "13" through "24" and PP records with PPSEQ values "8" through "14".

### Example 2 (Some PC records excluded)

Only some records in PC were used to calculate all pharmacokinetic parameters; time points 8 and 9 on day 1 were not used for any pharmacokinetic parameters.

This example uses --GRPID values in the PCGRPID (Example 2) and PPGRPID (Example 2) columns. Note that for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".

All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

Methods A, B, C, and D RELREC tables follow the same pattern as Example 1, but with the excluded records omitted from the relationships.

### Example 3 (Inconsistent PC usage across parameters)

Only some records in PC were used to calculate some parameters; time points 8 and 9 on day 1 were not used for half-life calculations, but were used for other parameters.

This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID = "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DY1DRGX_HALF", whereas the other PP records have PPGRPID = "DY1DRGX_A".

Methods A, B, C, and D RELREC tables show the split between the two groups of PC records and their corresponding PP records.

### Example 4 (Complex exclusions)

Only some records in PC were used to calculate parameters; time point 5 was excluded from Tmax, time point 6 from Cmax, and time points 11 and 12 from AUC.

This example uses --GRPID values in the PCGRPID (Example 4) and PPGRPID (Example 4) columns. Note that 4 values of PCGRPID and 4 values of PPGRPID were used.

Because of the complexity of this example, only methods A and D are illustrated.

**Method A (Many to Many, Using PCGRPID and PPGRPID):**
- **Rows 1-4:** The relationship with RELID "1" includes all PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_C", and "DY1DRGX_D" and the one PP record with PPGRPID = "TMAX".
- **Rows 5-8:** The relationship with RELID "2" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_D" and the one PP record with PPGRPID = "CMAX".
- **Rows 9-12:** The relationship with RELID "3" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_C" and the one PP record with PPGRPID = "AUC".
- **Rows 13-17:** The relationship with RELID "4" includes all PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", "DY1DRGX_C", and "DY1DRGX_D" (in this case, all PC records) and all PP records with PPGRPID = "OTHER".

## PC-PP Conclusions

Relating the datasets (as described in Section 8, Representing Relationships and Data) is the simplest method; however, all time-point concentrations in PC must be used to calculate all parameters for all subjects. If datasets cannot be related, then individual subject records must be related. In either case, the values of PCGRPID and PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.

Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require the assignment of --GRPID values (which are optional) in both the PC and PP datasets. Method D, in contrast, does not require the assignment of --GRPID values, relying instead on the required --SEQ values in both datasets to relate the records. Although Method D results in the largest number of RELREC records compared to the other methods, it may be the easiest to implement consistently across the range of complexities shown in the examples. Two additional methods, methods B and C, are also shown for Examples 1-3. They represent hybrid approaches, using --GRPID values in only 1 dataset (PP and PC, respectively) and --SEQ values for the other. These methods are best suited for sponsors who want to minimize the number of RELREC records while not having to assign --GRPID values in both domains. Methods B and C would not be ideal, however, if one expected complex scenarios as shown in Example 4.

## PC-PP — Suggestions for Implementing RELREC in the Submission of PK Data

Determine which of the scenarios best reflects how PP data are related to PC data. Questions that should be considered include:

1. Do all parameters for each PK profile use all concentrations for all subjects? If so, create a PPGRPID value for all PP records and a PCGRPID value for all PC records for each profile for each subject, analyte, and reference time point. Decide whether to relate datasets or records. If choosing the latter, create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

2. Do all parameters use the same concentrations, although maybe not all of them (Example 2)? If so, create a single PPGRPID value for all PP records, and 2 PCGRPID values for the PC records: a PCGRPID value for ones that were used and a PCGRPID value for those that were not used. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

3. Do any parameters use the same concentrations, but not as consistently as shown in Examples 1 and 2? If so, refer to Example 3. Assign a GRPID value to the PP records that use the same concentrations. More than 1 PPGRPID value may be necessary. Assign as many PCGRPID values in the PC domain as needed to group these records. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

4. If none of the above applies, or the data become difficult to group, then start with Example 4, and decide which RELREC method would be easiest to implement and represent.
