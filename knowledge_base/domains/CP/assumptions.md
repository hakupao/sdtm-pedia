# CP

## CP – Description/Overview

A findings domain that contains data related to the characterization of cell phenotype, lineage, and function based on expression of specific markers in single cell or particle suspensions.

The CP domain is modeled for use with disseminated tissue specimens (e.g., blood and other body fluids, bone marrow aspirates) and cell suspensions, and is not currently modeled for evaluations of solid tissue specimens.

The domain is intended to support tests associated with a cell phenotyping component based on the use of markers and is not intended for tests that are not associated with marker-based phenotyping, which are more appropriate to include in another domain (e.g., Immunogenicity Specimen Assessments (IS), Laboratory Test Results (LB), Microscopic Findings (MI)).

The CP domain is not intended to supplant use of the LB domain for routine lab hematology (e.g., blood cell differentials), nor is it intended for findings originating from microscopic assessment of cells, including those employing immunohistochemical (IHC) techniques.

The modeled use cases include measurement of

- cell populations identified, classified, and/or otherwise characterized based on the differential expression of phenotypic and/or cell state/function markers, as determined for both normal and abnormal cell populations;
- the level of marker expression;
- substances interacting with (e.g., binding to) a marker which is a target of interest (not limited to a pharmacologic target); and
- other cell properties based on characterization of expression marker(s) and/or substances that interact with the marker(s).

To provide the flexibility needed to report cell marker expression data, which can range widely in complexity, several new SDTM variables have been created.

Most of the new variables are permissible, and are available as needed to fully define a test and/or to prevent ambiguity that could lead to misunderstanding or difficulty in interpreting the data.

New variables include --SBMRKS (Sublineage Marker String), --CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BNDAGT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR (Marker String), --GATE (Gate Name), --GATEDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type).

Definitions and appropriate use of these variables are provided in the Specification and Assumptions sections of this guidance and are illustrated in the examples for selected use cases.

Data submitters should work closely with laboratory data providers, analysts, and data receivers/users to determine the appropriate set of permissible variables to include in a dataset (i.e., the variables needed to fully document tests and associated findings for a particular use case).

Sponsors that previously chose to submit cell phenotyping data in the LB domain, where LBTEST was often used to populate cell marker information (e.g., "CD4" to indicate helper T lymphocytes), should note that the new variable --MRKSTR should be used to house the full marker string information used to define the test in terms of markers; the --TEST variable is reserved for the name of the cell population.

Several of the new variables (i.e., --SBMRKS, --CELSTA, --CSMRKS) are used to further subdivide the population reported in --TEST into more granular unnamed subpopulations based on 1 or more additional markers.

This approach provides a more easily understood test name in the --TEST variable and enables development of controlled terminology for --TEST and --TESTCD.

The goal is to standardize, where possible, cell phenotype test names across studies so that it will be easier for users to understand and interpret the data (e.g., when different marker sets are used across labs to define the same cell population).

This approach also enhances the ability to integrate and compare data across studies in a practicable manner that (in addition to being less error-prone) preserves the often subtle differences between tests, which are essential for determining whether tests are truly comparable.

Used in accordance with this guidance, the complete marker sting information provided in the --MRKSTR variable reflects the operational (i.e., laboratory-specific) definition of the test measurement.

Together with the gating information provided in the --GATE and --GATEDEF variables, --MRKSTR values help to ensure that proper groupings and comparisons are made across tests by preserving nuanced details that may affect the interpretation of test results.

To facilitate these objectives and to enable accurate cross-study comparisons and data-mining efforts, it is recommended that --MRKSTR values conform as closely as possible to marker string formatting principles presented in the CP Assumptions section.

## CP – Assumptions

1. The Cell Phenotype domain captures cell phenotyping and related data based on cell expression markers and other indicators (e.g., stains/dyes) in disseminated tissue specimens and cell suspensions.

2. The CP domain is only used for tests which include a phenotyping component that relies on using cell markers to identify a specific population of cells (e.g., quantitative cell phenotyping), or on which the test is conducted (e.g., quantitative single marker expression, target/receptor occupancy). For example, a test which measures gamma-interferon expression in helper T lymphocytes defined as the CD45+CD3+CD4+CD8- population is an appropriate test for including in CP, whereas a test which measures gamma interferon secretion in an undefined "PBMC" (peripheral blood mononuclear cell) population is not appropriate.

3. A value which is calculated and reported by a lab according to its procedures is considered collected rather than derived; the Derived Flag (CPDRVFL) should be null for these results.

4. CPCELSTA is used in conjunction with CPCSMRKS. When CPCELSTA is populated, CPCSMRKS must also be populated. Conversely, when CPCSMRKS is populated, CPCELSTA must be populated.

5. The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated, the Test Name (CPTEST) must be populated with the test name variant containing the "Sub" suffix to indicate that the finding/result pertains to a subpopulation of the cell type named in CPTEST.

6. Populating the CPTEST and CPMRKSTR variables: The general structure of CPTEST and CPMRKSTR depends on the use case (e.g., immunophenotyping, quantitative marker expression, target/receptor occupancy), which is generally conveyed by the CPCAT and/or CPSCAT value(s). Currently, CP supports the following use cases for which guidance on CPTEST and CPMRKSTR values are given:
   a. Immunophenotyping
      i. CPTEST is populated with the name of the cell type being measured, not with the set of markers used to define the cell type.
      ii. It is expected that CPMRKSTR is populated, and that it contains the entire set of markers used to define the test, including those that are also present in CPSBMRKS and/or CPCSMRKS.
      iii. Marker strings follow, as closely as possible, formatting recommendations presented in assumption 8.
   b. Quantitative single-marker expression
      i. CPTEST begins with the identity of the marker (e.g., CD99), followed by the word "Expression" (e.g., "CD99 Expression").
      ii. It is expected that CPMRKSTR is populated, and that it starts by identifying the marker being quantified (e.g. "CD99"). This is followed by a delimiter (described below) and then the entire marker string used to define the cell population on which the marker is measured, including the marker being quantified, since it also defines the cell population.
      iii. The general form of the delimiter used to separate the marker being quantified from the cell population on which it is measured is "<space>xxxx<space>", where "xxxx" represents a character string used as delimiting text. It is recommended that the delimiting text is the abbreviation for the unit of measure used to report the level of expression of the quantified marker (e.g., "MESF", "MdFI"). An example which follows this guidance is: CPTEST = "CD99 Expression" and CPMRKSTR = "CD99 MESF CD45+CD3-CD19+CD99+", where "MESF" is the text delimiter and is followed by the entire marker string defining the cell population on which CD99 was measured, which includes the CD99 marker itself.
      iv. Marker strings follow, as closely as possible, formatting recommendations presented in assumption 8.
   c. Other use cases (e.g., target/receptor occupancy), refer to the examples section and to published Controlled Terminology supporting CP. In the case of target/receptor occupancy a more generalized test value is populated into CPTEST (e.g., "Total Bound") and the identity of the target/receptor is included in another variable, such as CPBNDAGT and/or CPTSTPNL (refer to examples). CDISC will continue to develop examples for other use cases as they are identified and modeled.

7. Specifying viability:
   a. Because the majority of cell phenotyping tests of interest are for viable cells, the word "Viable" is not generally included in the test name (CPTEST) and usually does not need to be explicitly stated in CPCELSTA. Because populating CPCELSTA and CSMRKS with viability information necessitates appending the "Sub" suffix to the value in CPTEST (assumption 5), it is recommended that CPCELSTA and CPCSMRKS generally not be used unless a selective viability stain was included in the test in order to differentiate the record for viable cells from record(s) for cells in a different vital state. For example, when viable cells are being compared to apoptotic and/or non-viable cells, it is necessary to differentiate those records using CPCELSTA and CPCSMRKS. In such cases where CPCELSTA and CPCSMRKS are populated, the "Sub" suffix is appended to the value in CPTEST (assumption 5).
   b. Viability marker(s) used to define a test are included in the full marker string in CPMRKSTR regardless of whether the viability status is stated explicitly in CPCELSTA. Moreover, if viability is explicitly stated in CPGATE, marker(s) used to designate viability are included in CPGATDEF. For example, if the value in CPGATE is "Lymphocytes, Viable" and 7AAD- was used to define the viable state, 7AAD- is included in CPGATDEF, in addition to being included in the complete marker string in CPMRKSTR.

8. Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS: The marker string variables provide critical information for defining a test. Although there are no current plans to control their values through CDISC Controlled Terminology codelists, adherence to the following formatting guidelines helps to preclude ambiguities that can lead to uncertainty in uniquely understanding a test and its associated result.
   a. Marker strings do not contain delimiting characters (e.g., ",", space, "/", ")") to separate individual markers within the string, nor do they contain punctuation (e.g., hyphens) within individual markers, as these can be confused with symbols used to designate levels of expression and/or make it difficult to distinguish between the individual markers that comprise the string. For example, although the scientific literature often uses "HLA-DR", this is represented in CP marker strings as "HLADR".
   b. Forward slash "/" is only used to separate the portion of the marker string defining a numerator from the portion defining a denominator.
   c. When referring to a marker using the cluster of differentiation (CD) designation, "CD" should be included as part of the marker reference. For example, a marker string for helper T lymphocytes comprising CD45, CD3, CD4, and CD8 markers would be "CD45+CD3+CD4+CD8-" (rather than "45+3+4+8-").
   d. The order of markers within a string is consistent across similar tests, generally proceeding in the order that defines the cell hierarchy from highest to lowest, followed by additional non-lineage-defining markers, and ending with cell state and viability markers. This order maintains alignment with how a test is identified using the ordered combination of CPTEST, CPSMRKS, and CPCELSTA. For example, a test for proliferating viable activated central memory helper T-lymphocytes would be operationally defined in CPMRKSTR as similar to "CD45+CD3+CD19-CD4+CD8-CD197+CD45RA-CD278+Ki67+7AAD-", where the order of markers in the string is "CD45" (leukocyte), "CD3+CD19-" (T lymphocyte), "CD4+CD8-" (helper), "CD197+CD45RA-" (central memory), "CD278+" (activated), Ki67+ (proliferating), 7AAD- (viable). Corresponding to this marker-based definition of the test, and using the appropriate Controlled Terminology terms, CPTEST is "TLym Help Cen Mem Sub", CPCELSTA is "ACTIVATED; PROLIFERATING", and CPCSMRKS is "CD278+Ki67+". If the sponsor also chose to include the viability status as a cell state in addition to the activation and proliferative states, CPCELSTA would be similar to "ACTIVATED; PROLIFERATING; VIABLE" and the corresponding CPCSMRKS value would be "CD278+Ki67+7AAD-". In this example, the named cell population in CPTEST has not been further divided into an unnamed sublineage based on additional sublineage markers; therefore, CPSBMRKS is null.
   e. Forward (FSC) and Side (SSC) light scatter: These parameters are generally used to perform initial gating to exclude debris non-singlets and are often reapplied to differentiate cell subpopulations in the "inclusion" gate. However, FSC and SSC are often not included in marker string definitions as it is generally taken for granted that they were used. In contrast, they are usually included in a descriptions of a gating strategy, and would generally be included in CPGATDEF when the full gating strategy is shown. Labs/sponsors may choose whether to include FSC and SSC parameters in CPMRKSTR. It is recommended to include them when they are needed to differentiate one test from another. For example, because there is no universal expression marker specific for lymphocytes, FSC and SSC are used to define the lymphocyte subpopulation within a CD45+ leukocyte population. A test of "Lymphocytes/Leukocytes" defined only in terms of CD45 expression would not make sense as it would be "CD45+/CD45+". In this case, it makes sense to define lymphocytes as "CD45+SSClo" so that the value in CPMRKSTR is "CD45+SSClo/CD45+".
   f. Indicating the expression level of individual markers included in a marker string: A variety of formats are used in the scientific literature for indicating the level of expression of a marker on or within a cell. For example, after identifying a marker such as CD4, its level of expression might be represented as 1 of the following:
      i. neg, min, or - to denote the absence or minimal expression (e.g., CD4neg, CD4min, CD4-)
      ii. pos or + to denote that the marker is expressed (e.g., CD4pos, CD4+)
      iii. high, hi, or ++ to denote that the marker is expressed at a very high level relative to simply being "positive" (e.g., CD4high, CD4hi, CD4++)
      iv. other formats (e.g., -/low, -/lo, low, lo, mid, -/+, +++)
   g. Because categories for expression levels are subjective in the sense that they are relative to one another, various formats often overlap, which can create ambiguities. Some degree of consistency in formats used to represent relative expression levels is warranted to mitigate ambiguity, at least to the extent that relative expression levels used to define cell lineages/sublineages are similar across studies and laboratories in order to enable comparisons. Five designations are recommended for use in SDTM datasets:
      i. "-" (the marker is not expressed; at times, the use of "-lo" may be justified to indicate that the marker is either not expressed or is present in a negligible amount)
      ii. "lo" (the marker is expressed at a low level)
      iii. "mid" (the marker is expressed somewhere between a low and "normal" positive level for that cell type)
      iv. "+" (the marker is expressed at a normal positive level for that cell type)
      v. "hi" (the marker is expressed at a distinctly higher level than in cells that are "+", such that they are distinguishable from the "+" population and define their own subpopulation)
      vi. Although these designations are expected to be useful in the majority of cases, it is recognized that designations not listed here may be more appropriate in some cases. The data provider must determine the best way to designate an expression level suited to the purpose of the test, while striving to mitigate ambiguities resulting from lack of consistency of use.
   h. Explicitly indicating the cellular sublocation for a marker: In most cases, the location of a marker on or within a cell is not necessary; however, there are situations in which a marker can be expressed in more than a single cellular compartment and there is a need for the test to distinguish between marker expression in one compartment versus another. To accommodate this, using a lowercase letter in front of the marker is recommended. The cell sublocations are usually related to the cell surface (plasma membrane), cytoplasm, and nucleus. Use m, c, or n in front of the marker to denote "membrane", "cytoplasm", and "nucleus", respectively. An example of a marker often associated with a need to indicate cell location is CD152 (CTLA4), where cytoplasmic expression may define a test to distinguish it from whole cell expression. In this case, "cCD152" is used to denote that it is the cytoplasmic expression of CD152 that is measured for the test.

9. CPNRIND can be added to indicate where a result falls with respect to a reference range defined by CPORNRLO and CPORNRHI (e.g., "HIGH", "LOW").

10. The variable CPORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing unit and submit their lab values using that unit. If this is not the case, then a request for a new term (see https://ncitermform.nci.nih.gov/) should be submitted.

## CP – Example Narrative Atoms (Verbatim from SDTMIG v3.4)

The following verbatim row-description and narrative atoms accompany the CP examples in §6.3.5.3 of SDTMIG v3.4. They are provided here for verification and traceability against the source PDF.

### Example 1a (p209)

**[ig34_p0209_a002] Rows 4-5:** The B-lymphocyte lineage of lymphocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD19+) and negative (i.e., CD3-, CD14-, and CD56-) marker expression. Following a common convention and CP domain guidance for ordering markers in CPMRKSTR, the marker(s) used to define the highest level of the lineage hierarchy are placed first (i.e., CD45+ defining the leukocyte population), followed by marker(s) that define each subsequently lower level of the hierarchy. The example also follows a convention whereby the set of positive and negative markers used to identify the major lineages of leukocytes are ordered by T-cell, B-cell, monocyte, and NK cell. In row 4, B lymphocytes are defined as leukocytes (CD45+), non-T-cell (CD3-), B-cell (CD19+), non-monocyte (CD14-), and non-NK cell (CD56-), resulting in a CPMRKSTR value of "CD45+CD3-CD19+CD14-CD56-". Row 5 shows that CPMRKSTR contains the full set of markers used to define both the numerator and the denominator, separated by a forward slash "/".

### Example 7 (p217)

**[ig34_p0217_a016] Row 2:** Same as row 1 except that the sponsor chose to use CPGATE and CPGATEDEF to report information for the final gate rather than the penultimate gate, as in row 1.

### Example 8 (p218)

**[ig34_p0218_a012]** Although sponsors may elect to only report the final calculated receptor occupancy (proportion of bound/total target occupied) as in Example 7, this example includes the various measured parameters generated in the assay which are then used to make calculations for the final Receptor Occupancy value.

**[ig34_p0218_a013]** Since the example is measuring binding and not a cell population per se, the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) are not used and are not included.

**[ig34_p0218_a014]** Other variables such as CPMRKSTR, CPGATE, and CPGATEDEF are used to identify the cell population on which the binding of interest was measured.

**[ig34_p0218_a015]** In addition, the Sponsor Test Description (CPSPTSTD) and Test Panel (CPTSTPNL) variables may be helpful for identifying a specific cell population.

### Example 9 (p219-220)

**[ig34_p0219_a018]** In the example showing the full set of tests, data are reported for free and total binding, background (non-specific) binding, and specific binding. CPBDAGNT is used to identify the probe (detection) antibody for each type of test (HA5-PE or 2D4-APC). Specific free binding (Target Free, Delta Free Background) is calculated as the difference in the probe signal (measured as MESF) between an untreated assay tube to a tube treated with unlabeled probe antibody under saturating concentrations (to measure non-specific binding, which is not diminished under saturating conditions). CPTSTCND is used to capture the saturated condition imposed on the assay at runtime. Receptor Occupancy is calculated as the difference between pre- and post-treatment binding of the labeled competitive probe (HA5) normalized to pre-treatment binding.

**[ig34_p0220_a001] Row 1 (cont.):** CPGATEDEF contains the gate definition/gating strategy. Note that in this example the CD99 marker, although it is the target of interest for the test, is not part of the marker string used to identify the named portion of the cell population on which the test was performed.

**[ig34_p0220_a002] Row 1 (cont.):** As a result, the sponsor chose to report the penultimate gate, which does not include the target marker of interest (CD99). Because the target of interest for which occupancy was measured is not part of the test name (CPTEST), it is identified using CPBDAGNT and/or as part of the panel name in CPTSTPNL. The CPCAT and CPSCAT variables are used to indicate that the assay is intended for target engagement and that the assay is measuring receptor occupancy.

**[ig34_p0220_a003] Rows 2-7:** The CD99 marker is identified as the target of interest for measuring occupancy. Because the target of interest for which occupancy was measured is not part of the test name (CPTEST), it is identified using CPBDAGNT and/or CPTSTPNL. The CPTSTCND variable defines the condition imposed on the assay at runtime to for measuring background binding. CPGRPID groups individual measured tests to the calculated test value derived from them. Because final results involve comparing specific binding of free or total receptor for the baseline occupancy to a 24-hour post-treatment set of results (rows 8-14), time point information for specimen collection is included in CPTPT and CPTPTNUM. Rows 2-4 show results for measurement of free target using a labeled competitive antibody probe (HA5) and rows 5-7 show results for measurement of total CD99 on the monocyte cell target population using a labeled non-competitive antibody probe (2D4). The total CD99 measurement is a control to monitor for any difference in CD99 expression that might exist between the pre-dose and post-dose specimens that could bias the relative occupancy. They are not used to calculate occupancy of the CD99 target, as the relative expression of CD99 at the post-dose time point is comparable to the pre-dose expression (7253 vs 7530 MESF).

**[ig34_p0220_a004] Rows 8-14:** Show the same set of tests collected for baseline (rows 2-7) but measured 24 hours after treatment with the therapeutic drug, which binds in situ to CD99. The reported receptor occupancy is for the 24-hour post-treatment time point relative to pre-dose with the therapeutic CD99 binding drug.
