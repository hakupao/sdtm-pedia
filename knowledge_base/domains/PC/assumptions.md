# PC — Assumptions

## 6.3.5.9 Pharmacokinetics Domains

This section covers the Pharmacokinetics Concentration (PC) and Pharmacokinetics Parameters (PP) domains.

## PC – Assumptions

1. This domain can be used to represent specimen properties (e.g., volume, pH) in addition to drug and metabolite concentration measurements.

2. CDISC Controlled Terminology Rules for Pharmacokinetics are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PC domain, but the following Qualifiers would not generally be used: --BODSYS, --SEV.

## §6.3.5.9.3 Relating PP Records to PC Records

Sponsors must document the concentrations used to calculate each parameter. This may be done in analysis dataset metadata or by documenting relationships between records in the Pharmacokinetics Parameters (PP) and Pharmacokinetics Concentrations (PC) datasets in a RELREC dataset (see Section 8.2, Relating Peer Records, and Section 8.3, Relating Datasets).

### PC-PP – Relating Datasets

If all time-point concentrations in PC are used to calculate all parameters for all subjects, then the relationship between the 2 datasets can be documented as shown in this table:

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-123 | PC | | PCGRPID | | MANY | A |
| 2 | ABC-123 | PP | | PPGRPID | | MANY | A |

Note that the reference time point and the analyte are part of the natural key (see Section 3.2.1.1, Primary Keys) for both datasets. In this relationship, --GRPID is a surrogate key, and must be populated so that each combination of analyte and reference time point has a separate value of --GRPID.

### PC-PP – Relating Records

This section illustrates 4 methods for representing relationships between PC and PP records under 4 different circumstances. All these examples are based on the same PC and PP data for 1 drug (i.e., drug X).

The different methods for representing relationships are based on which linking variables are used in RELREC.

- Method A (many to many, using PCGRPID and PPGRPID)
- Method B (one to many, using PCSEQ and PPGRPID)
- Method C (many to one, using PCGRPID and PPSEQ)
- Method D (one to one, using PCSEQ and PPSEQ)

The different examples illustrate situations in which different subsets of the pharmacokinetic concentration data were used in calculating the pharmacokinetic parameters. As in the example above, --GRPID values must take into account all the combinations of analytes and reference time points; both are part of the natural key for both datasets. For each example, PCGRPID and PPGRPID were used to group related records within each respective dataset. The exclusion of some concentration values from the calculation of some parameters affects the values of PCGRPID and PPGRPID for the different situations. To conserve space, the PC and PP domains appear only once, but with 4 --GRPID columns, 1 for each of the example situations.

Note that a submission dataset would contain only 1 --GRPID column with a set of values such as those shown in 1 of the 4 columns in the PC and PP datasets.

Pharmacokinetic Concentrations (PC) Dataset for All Examples

**pc.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PCSEQ | PCGRPID (Example 1) | PCGRPID (Example 2) | PCGRPID (Example 3) | PCGRPID (Example 4) | PCREFID | PCTESTCD | PCTEST | PCCAT | PCORRES | PCORRESU | PCSTRESC | PCSTRESN | PCSTRESU | PCSPEC | PCBLFL | PCLLOQ | PCDTC | PCDY | PCNOMDY | PCTPT | PCTPTNUM | PCELTM | PCTPTREF | PCRFTDTC |
|-----|---------|--------|---------|-------|---------------------|---------------------|---------------------|---------------------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|--------|--------|-------|------|---------|-------|----------|--------|----------|----------|
| 1 | ABC-123 | PC | ABC-123-0001 | 1 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-01 | DRUG X | STUDYDRUG | ANALYTE | 9 | ug/mL | 9 | 9 | ug/mL | PLASMA | | 1.00 | 2001-02-01T08:35 | 1 | 1 | 5 min | 1 | PT5M | Day 1 Dose | 2001-02-01T08:30 |
| 2 | ABC-123 | PC | ABC-123-0001 | 2 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-02 | DRUG X | STUDYDRUG | ANALYTE | 20 | ug/mL | 20 | 20 | ug/mL | PLASMA | | 1.00 | 2001-02-01T08:55 | 1 | 1 | 25 min | 2 | PT25M | Day 1 Dose | 2001-02-01T08:30 |
| 3 | ABC-123 | PC | ABC-123-0001 | 3 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-03 | DRUG X | STUDYDRUG | ANALYTE | 31 | ug/mL | 31 | 31 | ug/mL | PLASMA | | 1.00 | 2001-02-01T09:00 | 1 | 1 | 50 min | 3 | PT50M | Day 1 Dose | 2001-02-01T08:30 |
| 4 | ABC-123 | PC | ABC-123-0001 | 4 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-04 | DRUG X | STUDYDRUG | ANALYTE | 38 | ug/mL | 38 | 38 | ug/mL | PLASMA | | 1.00 | 2001-02-01T09:45 | 1 | 1 | 75 min | 4 | PT1H15M | Day 1 Dose | 2001-02-01T08:30 |
| 5 | ABC-123 | PC | ABC-123-0001 | 5 | DY1_DRGX | DY1_DRGX | DY1_DRGX_B | DY1_DRGX | 123-0001-05 | DRUG X | STUDYDRUG | ANALYTE | 45 | ug/mL | 45 | 45 | ug/mL | PLASMA | | 1.00 | 2001-02-01T10:10 | 1 | 1 | 100 min | 5 | PT1H40M | Day 1 Dose | 2001-02-01T08:30 |
| 6 | ABC-123 | PC | ABC-123-0001 | 6 | DY1_DRGX | DY1_DRGX | DY1_DRGX_C | DY1_DRGX | 123-0001-06 | DRUG X | STUDYDRUG | ANALYTE | 48 | ug/mL | 48 | 48 | ug/mL | PLASMA | | 1.00 | 2001-02-01T10:35 | 1 | 1 | 125 min | 6 | PT2H5M | Day 1 Dose | 2001-02-01T08:30 |
| 7 | ABC-123 | PC | ABC-123-0001 | 7 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-07 | DRUG X | STUDYDRUG | ANALYTE | 41 | ug/mL | 41 | 41 | ug/mL | PLASMA | | 1.00 | 2001-02-01T11:00 | 1 | 1 | 150 min | 7 | PT2H30M | Day 1 Dose | 2001-02-01T08:30 |
| 8 | ABC-123 | PC | ABC-123-0001 | 8 | DY1_DRGX | EXCLUDE | DY1_DRGX_B | DY1_DRGX | 123-0001-08 | DRUG X | STUDYDRUG | ANALYTE | 35 | ug/mL | 35 | 35 | ug/mL | PLASMA | | 1.00 | 2001-02-01T11:30 | 1 | 1 | 200 min | 8 | PT3H20M | Day 1 Dose | 2001-02-01T08:30 |
| 9 | ABC-123 | PC | ABC-123-0001 | 9 | DY1_DRGX | EXCLUDE | DY1_DRGX_B | DY1_DRGX | 123-0001-09 | DRUG X | STUDYDRUG | ANALYTE | 31 | ug/mL | 31 | 31 | ug/mL | PLASMA | | 1.00 | 2001-02-01T11:50 | 1 | 1 | 250 min | 9 | PT4H10M | Day 1 Dose | 2001-02-01T08:30 |
| 10 | ABC-123 | PC | ABC-123-0001 | 10 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-10 | DRUG X | STUDYDRUG | ANALYTE | 25 | ug/mL | 25 | 25 | ug/mL | PLASMA | | 1.00 | 2001-02-01T14:45 | 1 | 1 | 375 min | 10 | PT6H15M | Day 1 Dose | 2001-02-01T08:30 |
| 11 | ABC-123 | PC | ABC-123-0001 | 11 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX | 123-0001-11 | DRUG X | STUDYDRUG | ANALYTE | 18 | ug/mL | 18 | 18 | ug/mL | PLASMA | | 1.00 | 2001-02-01T18:50 | 1 | 1 | 500 min | 11 | PT8H20M | Day 1 Dose | 2001-02-01T08:30 |
| 12 | ABC-123 | PC | ABC-123-0001 | 12 | DY1_DRGX | DY1_DRGX | DY1_DRGX_D | DY1_DRGX | 123-0001-12 | DRUG X | STUDYDRUG | ANALYTE | 12 | ug/mL | 12 | 12 | ug/mL | PLASMA | | 1.00 | 2001-02-01T18:30 | 1 | 1 | 600 min | 12 | PT10H | Day 1 Dose | 2001-02-01T08:30 |
| 13 | ABC-123 | PC | ABC-123-0001 | 13 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-13 | DRUG X | STUDYDRUG | ANALYTE | 10 | ug/mL | 10 | 10 | ug/mL | PLASMA | | 1.00 | 2001-02-08T08:35 | 8 | 8 | 5 min | 1 | PT5M | Day 8 Dose | 2001-02-08T08:30 |
| 14 | ABC-123 | PC | ABC-123-0001 | 14 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-14 | DRUG X | STUDYDRUG | ANALYTE | 21 | ug/mL | 21 | 21 | ug/mL | PLASMA | | 1.00 | 2001-02-08T08:55 | 8 | 8 | 25 min | 2 | PT25M | Day 8 Dose | 2001-02-08T08:30 |
| 15 | ABC-123 | PC | ABC-123-0001 | 15 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-15 | DRUG X | STUDYDRUG | ANALYTE | 32 | ug/mL | 32 | 32 | ug/mL | PLASMA | | 1.00 | 2001-02-08T09:20 | 8 | 8 | 50 min | 3 | PT50M | Day 8 Dose | 2001-02-08T08:30 |
| 16 | ABC-123 | PC | ABC-123-0001 | 16 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-16 | DRUG X | STUDYDRUG | ANALYTE | 39 | ug/mL | 39 | 39 | ug/mL | PLASMA | | 1.00 | 2001-02-08T09:45 | 8 | 8 | 75 min | 4 | PT1H15M | Day 8 Dose | 2001-02-08T08:30 |
| 17 | ABC-123 | PC | ABC-123-0001 | 17 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-17 | DRUG X | STUDYDRUG | ANALYTE | 46 | ug/mL | 46 | 46 | ug/mL | PLASMA | | 1.00 | 2001-02-08T10:10 | 8 | 8 | 100 min | 5 | PT1H40M | Day 8 Dose | 2001-02-08T08:30 |
| 18 | ABC-123 | PC | ABC-123-0001 | 18 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-18 | DRUG X | STUDYDRUG | ANALYTE | 48 | ug/mL | 48 | 48 | ug/mL | PLASMA | | 1.00 | 2001-02-08T10:10 | 8 | 8 | 100 min | 6 | PT2H5M | Day 8 Dose | 2001-02-08T08:30 |
| 19 | ABC-123 | PC | ABC-123-0001 | 19 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-19 | DRUG X | STUDYDRUG | ANALYTE | 40 | ug/mL | 40 | 40 | ug/mL | PLASMA | | 1.00 | 2001-02-08T11:00 | 8 | 8 | 150 min | 7 | PT2H30M | Day 8 Dose | 2001-02-08T08:30 |
| 20 | ABC-123 | PC | ABC-123-0001 | 20 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-20 | DRUG X | STUDYDRUG | ANALYTE | 35 | ug/mL | 35 | 35 | ug/mL | PLASMA | | 1.00 | 2001-02-08T11:50 | 8 | 8 | 200 min | 8 | PT3H20M | Day 8 Dose | 2001-02-08T08:30 |
| 21 | ABC-123 | PC | ABC-123-0001 | 21 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-21 | DRUG X | STUDYDRUG | ANALYTE | 30 | ug/mL | 30 | 30 | ug/mL | PLASMA | | 1.00 | 2001-02-08T12:40 | 8 | 8 | 250 min | 9 | PT4H10M | Day 8 Dose | 2001-02-08T08:30 |
| 22 | ABC-123 | PC | ABC-123-0001 | 22 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-22 | DRUG X | STUDYDRUG | ANALYTE | 24 | ug/mL | 24 | 24 | ug/mL | PLASMA | | 1.00 | 2001-02-08T14:45 | 8 | 8 | 375 min | 10 | PT6H15M | Day 8 Dose | 2001-02-08T08:30 |
| 23 | ABC-123 | PC | ABC-123-0001 | 23 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-23 | DRUG X | STUDYDRUG | ANALYTE | 17 | ug/mL | 17 | 17 | ug/mL | PLASMA | | 1.00 | 2001-02-08T16:50 | 8 | 8 | 500 min | 11 | PT8H20M | Day 8 Dose | 2001-02-08T08:30 |
| 24 | ABC-123 | PC | ABC-123-0001 | 24 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-24 | DRUG X | STUDYDRUG | ANALYTE | 11 | ug/mL | 11 | 11 | ug/mL | PLASMA | | 1.00 | 2001-02-08T18:30 | 8 | 8 | 600 min | 12 | PT10H | Day 8 Dose | 2001-02-08T08:30 |

Pharmacokinetic Parameters (PP) Dataset for All Examples

**pp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID (Example 1) | PPGRPID (Example 2) | PPGRPID (Example 3) | PPGRPID (Example 4) | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | PPNOMDY | PPRFTDTC |
|-----|---------|--------|---------|-------|---------------------|---------------------|---------------------|---------------------|----------|--------|-------|---------|----------|----------|----------|----------|--------|---------|----------|
| 1 | ABC-123 | PP | ABC-123-0001 | 1 | DY1DRGX | DY1DRGX | DY1DRGX_A | DY1DRGX | TMAX | Time of CMAX | DRUG X | 1.87 | h | 1.87 | 1.87 | h | PLASMA | 1 | 2001-02-01T08:35 |
| 2 | ABC-123 | PP | ABC-123-0001 | 2 | DY1DRGX | DY1DRGX | DY1DRGX_A | DY1DRGX | CMAX | Max Conc | DRUG X | 44.5 | ng/mL | 44.5 | 44.5 | ng/mL | PLASMA | 1 | 2001-02-01T08:35 |
| 3 | ABC-123 | PP | ABC-123-0001 | 3 | DY1DRGX | DY1DRGX | DY1DRGX_A | DY1DRGX | AUCALL | AUC All | DRUG X | 294.7 | h*ug/mL | 294.7 | 294.7 | h*ug/mL | PLASMA | 1 | 2001-02-01T08:35 |
| 4 | ABC-123 | PP | ABC-123-0001 | 4 | DY1DRGX | DY1DRGX | DY1DRGX_HALF | DY1DRGX | LAMZHL | Half-Life Lambda z | DRUG X | 4.69 | h | 4.69 | 4.69 | h | PLASMA | 1 | 2001-02-01T08:35 |
| 5 | ABC-123 | PP | ABC-123-0001 | 5 | DY1DRGX | DY1DRGX | DY1DRGX_A | DY1DRGX | VZO | Vz Obs | DRUG X | 10.9 | L | 10.9 | 10.9 | L | PLASMA | 1 | 2001-02-01T08:35 |
| 6 | ABC-123 | PP | ABC-123-0001 | 6 | DY1DRGX | DY1DRGX | DY1DRGX_A | DY1DRGX | CLO | Total CL Obs | DRUG X | 1.68 | L/h | 1.68 | 1.68 | L/h | PLASMA | 1 | 2001-02-01T08:35 |
| 7 | ABC-123 | PP | ABC-123-0001 | 7 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | TMAX | Time of CMAX | DRUG X | 1.91 | h | 1.91 | 1.91 | h | PLASMA | 8 | 2001-02-08T08:35 |
| 8 | ABC-123 | PP | ABC-123-0001 | 8 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | CMAX | Max Conc | DRUG X | 46.0 | ng/mL | 46.0 | 46.0 | ng/mL | PLASMA | 8 | 2001-02-08T08:35 |
| 9 | ABC-123 | PP | ABC-123-0001 | 9 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | AUCALL | AUC All | DRUG X | 289.0 | h*ug/mL | 289.0 | 289.0 | h*ug/mL | PLASMA | 8 | 2001-02-08T08:35 |
| 10 | ABC-123 | PP | ABC-123-0001 | 10 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | LAMZHL | Half-Life Lambda z | DRUG X | 4.50 | h | 4.50 | 4.50 | h | PLASMA | 8 | 2001-02-08T08:35 |
| 11 | ABC-123 | PP | ABC-123-0001 | 11 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | VZO | Vz Obs | DRUG X | 10.7 | L | 10.7 | 10.7 | L | PLASMA | 8 | 2001-02-08T08:35 |
| 12 | ABC-123 | PP | ABC-123-0001 | 12 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | CLO | Total CL Obs | DRUG X | 1.75 | L/h | 1.75 | 1.75 | L/h | PLASMA | 8 | 2001-02-08T08:35 |

### PC-PP Conclusions

Relating the datasets (as described in Section 8, Representing Relationships and Data) is the simplest method; however, all time-point concentrations in PC must be used to calculate all parameters for all subjects. If datasets cannot be related, then individual subject records must be related. In either case, the values of PCGRPID and PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.

Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require the assignment of --GRPID values (which are optional) in both the PC and PP datasets. Method D, in contrast, does not require the assignment of --GRPID values, relying instead on the required --SEQ values in both datasets to relate the records. Although Method D results in the largest number of RELREC records compared to the other methods, it may be the easiest to implement consistently across the range of complexities shown in the examples. Two additional methods, methods B and C, are also shown for Examples 1-3. They represent hybrid approaches, using --GRPID values in only 1 dataset (PP and PC, respectively) and --SEQ values for the other. These methods are best suited for sponsors who want to minimize the number of RELREC records while not having to assign --GRPID values in both domains. Methods B and C would not be ideal, however, if one expected complex scenarios as shown in Example 4.

Note that an attempt has been made to approximate real pharmacokinetic data; however, the example values are not intended to reflect data used for actual analysis. When certain time-point concentrations have been omitted from PP calculations in Examples 2-4, the actual parameter values in the PP dataset have not been recalculated from those in Example 1 to reflect those omissions.

### PC-PP – Suggestions for Implementing RELREC in the Submission of PK Data

Determine which of the scenarios best reflects how PP data are related to PC data. Questions that should be considered include:

1. Do all parameters for each PK profile use all concentrations for all subjects? If so, create a PPGRPID value for all PP records and a PCGRPID value for all PC records for each profile for each subject, analyte, and reference time point. Decide whether to relate datasets or records. If choosing the latter, create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

2. Do all parameters use the same concentrations, although maybe not all of them (Example 2)? If so, create a single PPGRPID value for all PP records, and 2 PCGRPID values for the PC records: a PCGRPID value for ones that were used and a PCGRPID value for those that were not used. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

3. Do any parameters use the same concentrations, but not as consistently as shown in Examples 1 and 2? If so, refer to Example 3. Assign a GRPID value to the PP records that use the same concentrations. More than 1 PPGRPID value may be necessary. Assign as many PCGRPID values in the PC domain as needed to group these records. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.

4. If none of the above applies, or the data become difficult to group, then start with Example 4, and decide which RELREC method would be easiest to implement and represent.
