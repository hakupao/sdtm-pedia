# 19_fnd_morphology_bs_cp_cv

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `19`
> - **Concept**: Findings: BS (biospecimens) + CP (clinical endpoint) + CV (cardiovascular)
> - **Merged files**: 9
> - **Words**: 16,007
> - **Chars**: 104,168
> - **Sources**:
>   - `domains/BS/spec.md`
>   - `domains/BS/assumptions.md`
>   - `domains/BS/examples.md`
>   - `domains/CP/spec.md`
>   - `domains/CP/assumptions.md`
>   - `domains/CP/examples.md`
>   - `domains/CV/spec.md`
>   - `domains/CV/assumptions.md`
>   - `domains/CV/examples.md`

---
## Source: `domains/BS/spec.md`

# BS — Biospecimen Findings

> Class: Findings | Structure: One record per measurement per biospecimen identifier per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### SPDEVID
- **Order:** 4
- **Label:** Sponsor Device Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a device.

### BSSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### BSGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### BSREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Internal or external identifier such as lab specimen ID.

### BSSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### BSTESTCD
- **Order:** 9
- **Label:** Biospecimen Test Short Name
- **Type:** Char
- **Controlled Terms:** C124300
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN.

### BSTEST
- **Order:** 10
- **Label:** Biospecimen Test Name
- **Type:** Char
- **Controlled Terms:** C124299
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for BSTESTCD. Examples: Volume, RNA Integrity Number.

### BSCAT
- **Order:** 11
- **Label:** Category for Biospecimen Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY.

### BSSCAT
- **Order:** 12
- **Label:** Subcategory for Biospecimen Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of BSCAT values.

### BSORRES
- **Order:** 13
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### BSORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Unit for BSORRES. Examples: mg, mL.

### BSSTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN.

### BSSTRESN
- **Order:** 16
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings.

### BSSTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for BSSTRESC and BSSTRESN.

### BSSTAT
- **Order:** 18
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE.

### BSREASND
- **Order:** 19
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with BSSTAT when value is NOT DONE.

### BSNAM
- **Order:** 20
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### BSSPEC
- **Order:** 21
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734; C111114
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE.

### BSANTREG
- **Order:** 22
- **Label:** Anatomical Region of Specimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA.

### BSSPCCND
- **Order:** 23
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC.

### BSMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS.

### BSBLFL
- **Order:** 25
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value.

### VISITNUM
- **Order:** 26
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 27
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### BSDTC
- **Order:** 29
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### BSDY
- **Order:** 30
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection relative to the sponsor-defined RFSTDTC.

### BSTPT
- **Order:** 31
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF.

### BSTPTNUM
- **Order:** 32
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of BSTPT used in sorting.

### BSELTM
- **Order:** 33
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.

### BSTPTREF
- **Order:** 34
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL.

### BSRFTDTC
- **Order:** 35
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by BSTPTREF.
---

## Cross References

### Controlled Terminology
- [Genetic Sample Type (C111114)](../../terminology/core/general_part2.md) — BSSPEC
- [Biospecimen Characteristics Test Name (C124299)](../../terminology/core/other_part1.md) — BSTEST
- [Biospecimen Characteristics Test Code (C124300)](../../terminology/core/other_part1.md) — BSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — BSBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — BSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — BSORRESU, BSSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — BSSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — BSSPEC
- [Method (C85492)](../../terminology/core/general_part3.md) — BSMETHOD

### Related Domains
- **Same class (Findings):** CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Event:** [BE](../BE/) — biospecimen events
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/BS/assumptions.md`

# BS — Assumptions

1. The BS domain is used to store findings related to specimen handling and specimen characteristics such as type, amount, or size. BS is not restricted to PGx-related specimens.

2. For biospecimens of genetic material, BSSPEC values are drawn from the GENSMP (C111114) codelist.

3. Non-genetic BSSPEC values are drawn from the SPEC (C77529) codelist, which is part of the SEND terminology listing. BSANTREG is used to further define BSSPEC when it is desirable to identify a specific region within an organ.

4. To adapt BS for use with the SDTMIG, use the SPECTYPE (C78734) codelist in BSSPEC, add --LOC, --LAT, --DIR, and --PORTOT as applicable, and remove BSANTREG. Values that would otherwise have gone in BSANTREG may be placed in a supplemental qualifier that is almost identical to that variable, but which further qualifies BSLOC instead of BSSPEC.

5. The following variables generally would not be used in BS: --POS, --ORNLO, --ORNHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --ACPTFL, --FAST, --TOX, --TOXGR, --SEV, --DTHREL.

## Source: `domains/BS/examples.md`

# BS — Examples

## Example 1

This example shows data about RNA integrity. The data collected focus on the quality of the RNA sample being collected. It has been shown that improper storage or isolation methods might compromise the usability of a sample.

**Rows 1-2:** The A260/A280 and A260/A230 ratios are used to determine the purity of the RNA sample. Any ratios outside of the accepted values may indicate contamination with protein or reagents used during the extraction process.

**Row 3:** The amounts of both 28S and 18S ribosomal RNA are measured and then a ratio is calculated. Because values in --TESTCD cannot begin with a number, the test code has been prefixed with an "I" for integrity.

**Row 4:** The RNA integrity number is a quality measurement calculated using a special algorithm and used to determine the usability of the RNA sample.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSSTRESC | BSSTRESN | BSXFN | BSNAM | BSSPEC | BSMETHOD | BSRUNID | VISIT | VISITNUM | VISITDY | BSDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|-------|-------|--------|----------|---------|-------|----------|---------|-------|
| 1 | A12345 | BS | 43871 | 1 | 1148.26704 | A260/A230 | A260/A230 | QUALITY CONTROL | 2.05 | 2.05 | 2.05 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | SPECTROPHOTOMETRY | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 2 | A12345 | BS | 43871 | 2 | 1148.26704 | A260/A280 | A260/A280 | QUALITY CONTROL | 2 | 2 | 2 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | SPECTROPHOTOMETRY | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 3 | A12345 | BS | 43871 | 3 | 1148.26704 | 28S/18S | 28S/18S | QUALITY CONTROL | 1.2 | 1.2 | 1.2 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | ELECTROPHORESIS | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 4 | A12345 | BS | 43871 | 4 | 1148.26704 | RIN | RNA INTEGRITY NUMBER | QUALITY CONTROL | 9.5 | 9.5 | 9.5 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | ELECTROPHORESIS | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |

## Source: `domains/CP/spec.md`

# CP — Cell Phenotype Findings

> Class: Findings | Structure: One record per test per specimen per timepoint per visit per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### CPSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records within a domain. May be any valid number.

### CPGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### CPREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier.

### CPSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the lab page.

### CPLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### CPLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### CPTESTCD
- **Order:** 10
- **Label:** Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C181173
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in CPTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). CPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MONO", "MNS".

### CPTEST
- **Order:** 11
- **Label:** Name of Measurement, Test or Examination
- **Type:** Char
- **Controlled Terms:** C181174
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for CPTESTCD. For cell phenotyping, the name (often abbreviated) of the cell population, as it is generally accepted by the scientific community, is populated (rather than a colloquial designation based on a primary marker, e.g., TLym Help rather than CD4). When the test is for a sublineage which can only be identified by specifying additional markers (i.e., has not been given a name) or which is further restricted to a subpopulation based on a particular cell state (e.g., activated, proliferating, apoptotic), the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) variables are additionally populated and the value in CPTEST is suffixed with "Sub" to denote that it is a subset of the population identified in CPTEST (e.g., Monocytes Sub).  The value in CPTEST cannot be longer than 40 characters.

### CPSBMRKS
- **Order:** 12
- **Label:** Sublineage Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to further subset the cell population identified in CPTEST based on the use of additional marker(s) that define a sublineage. The value in CPSBMRKS is used in combination with values in CPTEST and CPCELSTA to fully describe the cell population being measured. As such, it is an essential component of the full test name.  For example, three unnamed sublineages of monocytes have been identified as: CCR2+CD16-, CCR2-CD16+, and CCR2+CD16+. Whereas the entire monocyte cell population can be defined as CD14+ cells, the additional CCR2 and CD16 markers are used to differentiate one sublineage from another. As none of these sublineages have been given names, they are only known by the CCR2 and CD16 marker combinations. By associating the CPTEST value of "Monocytes Sub" with, for example, a value of "CCR2+CD16-" in CPSBMRKS, the full test is defined to be the CCR2+CD16- monocyte subpopulation.

### CPCELSTA
- **Order:** 13
- **Label:** Cell State
- **Type:** Char
- **Controlled Terms:** C181172
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When populated, the values in CPCELSTA and CPSMRKS, in combination with the values in CPTEST and CPSBMRKS, fully describe the cell population being measured.

### CPCSMRKS
- **Order:** 14
- **Label:** Cell State Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA).  For example, when Ki67 expression is used to determine that a cell population is in a proliferating state (i.e., CPCELSTA value="PROLIFERATING"), the value "Ki67+" in CPCSMRKS indicates that positive expression of Ki67 was used to define the population as proliferating. Similarly, a value of "Ki67-" in CPCSMRKS would indicate that lack of expression of Ki67 defined the "NON-PROLIFERATING" cell state in CPCELSTA. The CPCSMRKS value is useful for quickly determining which marker(s) were used to classify (i.e., operationally define) a cell population based on a functional/biological state.

### CPTSTCND
- **Order:** 15
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. --TSTCND is generally used to distinguish between two or more records where the same assay is performed under varying (as opposed to fixed) conditions, usually for the purpose of making a comparison. For example, when the same assay (identified in --TEST) is performed under stimulated and non-stimulated conditions, the --TSTCND variable is used distinguish between the records.

### CPCNDAGT
- **Order:** 16
- **Label:** Test Condition Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent, if applicable, used to impose the condition identified in CPTSTCND. For example, records might be produced for the same assay run under stimulating (CPTSTCND value = "STIMULATED") conditions produced by different stimulating agents (e.g., phorbol myristate acetate, concanavalin A, PHA-P, TNF-alpha, Ionomycin, candida antigen).

### CPBDAGNT
- **Order:** 17
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent that is binding to the entity in the CPTEST variable. The CPBDAGNT variable is used to indicate that there is a binding relationship between the entities in the CPTEST and CPBDAGNT variables, regardless of direction.  The binding agent may be, but is not limited to, a test article; a portion of a test article; a substance related to a test article; an endogenous molecule; an allergen; an infectious agent; or a reagent (e.g., primary antibody) that confers the binding specificity for the measurement defined in CPTEST when it is needed to uniquely identify the test.

### CPABCLID
- **Order:** 18
- **Label:** Antibody Clone Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the antibody clone (e.g., supplier-provided catalog name) used to confer specificity for the binding agent specified in CPBDAGNT.

### CPMRKSTR
- **Order:** 19
- **Label:** Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** The text string identifying the full set of markers/indicators used by the laboratory to operationally define the complete test based on the combination of CPTEST, CPSBMRKS, and CPCELSTA. Because laboratories often use different markers/indicators to identify a cell population, the relationship between a named cell population in CPTEST (as combined with CPSBMRKS and CPCELSTA values) and the set of markers used to identify that population is many-to-one. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different sets of markers, it is necessary to operationally define the test in terms of the complete set of markers/indicators used to perform that test.

### CPGATE
- **Order:** 20
- **Label:** Gate
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The sponsor-defined name assigned to a gate. Gates are electronic (i.e., a device setting or software-defined) boundaries set by a user to virtually parse a specimen into discrete populations based on a set of defined characteristics (e.g., presence, absence, or intensity of expression of various markers; physical size; internal complexity or granularity). Gates are used to constrain data collection or analysis to a specific cell population or region of interest within the specimen.

### CPGATDEF
- **Order:** 21
- **Label:** Gate Definition
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The text string identifying the set of parameters and the order in which they are applied to define the gating strategy. In practice, a series of 2-dimensional sub-gates based on different cell characteristics (i.e., markers/indicators/physical properties) are most often combined until the cell population of interest is sufficiently resolved (i.e., electronically isolated) from other cell populations contained within the specimen.  For complex analyses, differences in gating strategies can produce subtle differences in results obtained for a test. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different gating strategies, it is often necessary to qualify the test in terms of the gating strategy. For some purposes, however, and at the discretion of the sponsor, only the ultimate or penultimate gate is identified. When specifying the gating strategy in CPGATDEF, each sub-gate should be listed in the order it was applied and separated from the next sub-gate using the pipe/vertical line ("|") character.

### CPSPTSTD
- **Order:** 22
- **Label:** Sponsor Test Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor's description of a test. The variable is intended to contain highly structured test description metadata used by a sponsor to unambiguously define (label) a test. Such values generally reside in a sponsor/laboratory test metadata repository. CPSPTSTD is not intended for unstructured (spontaneous) free text.  An example of appropriate usage is when it is necessary to include identifying information for a target cell population on which a test is conducted when the target population is not part of the test name, e.g., tests for quantitative expression of a particular marker on a specific cell population.

### CPCAT
- **Order:** 23
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** C181171
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects. Examples: "IMMUNOPHENOTYPING", "CELL FUNCTION", "TARGET ENGAGEMENT".

### CPSCAT
- **Order:** 24
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of CPCAT.

### CPTSTPNL
- **Order:** 25
- **Label:** Test Panel
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined textual description used to group tests run together as part of a test panel. Can be used with --GRPID to ensure that relationships between associated tests are accurately identified.

### CPORRES
- **Order:** 26
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### CPORRESU
- **Order:** 27
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for CPORRES. Examples: "10^6/L", "%", "MESF".

### CPRESSCL
- **Order:** 28
- **Label:** Result Scale
- **Type:** Char
- **Controlled Terms:** C177910
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the scale of the original result value with respect to whether the result is quantitative, ordinal, nominal, or narrative.

### CPRESTYP
- **Order:** 29
- **Label:** Result Type
- **Type:** Char
- **Controlled Terms:** C179588
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the kind of result (i.e., property type) originally reported for the test. Examples: "NUMBER CONCENTRATION", "NUMBER FRACTION", "RATIO".

### CPCOLSRT
- **Order:** 30
- **Label:** Collected Summary Result Type
- **Type:** Char
- **Controlled Terms:** C177908
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived using individual source data records, this summary result should be represented in ADaM. If a sponsor has both a collected summary result and a derived summary result, the collected summary result should be represented in SDTM and the derived summary result should be represented in ADaM.

### CPORNRLO
- **Order:** 31
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### CPORNRHI
- **Order:** 32
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### CPSTRESC
- **Order:** 33
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from CPORRES in a standard format or in standard units. CPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CPSTRESN.

### CPSTRESN
- **Order:** 34
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from CPSTRESC. CPSTRESN should store all numeric test results or findings.

### CPSTRESU
- **Order:** 35
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for CPSTRESC or CPSTRESN.

### CPSTNRLO
- **Order:** 36
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of reference range for continuous measurements for CPSTRESC/CPSTRESN in standardized units. Should be populated only for continuous results.

### CPSTNRHI
- **Order:** 37
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### CPNRIND
- **Order:** 38
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by CPORNRLO and CPORNRHI, CPSTNRLO and CPSTNRHI, or by CPSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether CPNRIND refers to the original or standard reference ranges and results. CPNRIND should not be used to indicate clinical significance.

### CPSTAT
- **Order:** 39
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the test was not performed or that it was attempted but did not generate a result. Should be null if a result exists in CPORRES.

### CPREASND
- **Order:** 40
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a test was not performed, e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED", "SPECIMEN LOST". Used in conjunction with CPSTAT when value is "NOT DONE".

### CPNAM
- **Order:** 41
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the laboratory that performed the test.

### CPLOINC
- **Order:** 42
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** LOINC
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Code for the test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.

### CPSPEC
- **Order:** 43
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "BLOOD", "BONE MARROW".

### CPSPCCND
- **Order:** 44
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The physical state or quality of a specimen for an assessment. Example: "CLOTTED".

### CPMETHOD
- **Order:** 45
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Example: "FLOW CYTOMETRY".

### CPANMETH
- **Order:** 46
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result.

### CPLOBXFL
- **Order:** 47
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### CPBLFL
- **Order:** 48
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null.

### CPDRVFL
- **Order:** 49
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If CPDRVFL = "Y", then CPORRES may be null, with CPSTRESC and (if numeric) CPSTRESN having the derived value.

### CPCLSIG
- **Order:** 50
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgement.

### VISITNUM
- **Order:** 51
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 52
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 53
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.

### TAETORD
- **Order:** 54
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 55
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### CPDTC
- **Order:** 56
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format.

### CPDY
- **Order:** 57
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC value in Demographics.

### CPTPT
- **Order:** 58
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a specimen is to be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF). Example: "1 hour post".

### CPTPTNUM
- **Order:** 59
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of CPTPT to aid in sorting. When CPTPT is represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF), the values in CPTPTNUM should be assigned in ascending order relative to the value in CPTPTREF. For example, records for time points where CPTPT = "5 minutes post", 1 hour post", and "4 hours post" could be represented in CPTPTNUM as "1", "2", and "3", which maintains the order between CPTPT and CPTPTNUM with respect to the fixed time point reference in CPTPTREF.

### CPELTM
- **Order:** 60
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to the planned fixed reference value in CPTPTREF, represented in ISO 8601 duration format. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by CPTPTREF, "T8H" to represent 8 hours after the reference time point represented by CPTPTREF.

### CPTPTREF
- **Order:** 61
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Descriptive name of the fixed reference point referred to by CPTPT, CPTPTNUM, and CPELTM. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### CPRFTDTC
- **Order:** 62
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by CPTPTREF.
---

## Cross References

### Controlled Terminology
- [Collected Summarized Value Type Response (C177908)](../../terminology/core/general_part2.md) — CPCOLSRT
- [Result Scale Response (C177910)](../../terminology/core/general_part4.md) — CPRESSCL
- [Result Type Response (C179588)](../../terminology/core/general_part4.md) — CPRESTYP
- [Category for Cell Phenotyping (C181171)](../../terminology/core/cp_part1.md) — CPCAT
- [Cell State Response (C181172)](../../terminology/core/cp_part2.md) — CPCELSTA
- [Cell Phenotyping Test Code (C181173)](../../terminology/core/cp_part1.md) — CPTESTCD
- [Cell Phenotyping Test Name (C181174)](../../terminology/core/cp_part2.md) — CPTEST
- [Test Condition Response (C181175)](../../terminology/core/general_part4.md) — CPTSTCND
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — CPLOBXFL, CPBLFL, CPDRVFL, CPCLSIG
- [Not Done (C66789)](../../terminology/core/general_part4.md) — CPSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — CPORRESU, CPSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — CPSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — CPSPEC
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — CPNRIND
- [Method (C85492)](../../terminology/core/general_part3.md) — CPMETHOD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [LB](../LB/) — cardiac electrophysiology vs lab tests

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/CP/assumptions.md`

# CP — Assumptions

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

## Source: `domains/CP/examples.md`

# CP — Examples

The CP domain includes use of several new qualifier variables. The primary intent of the following examples is to demonstrate the appropriate use of these new variables based on a selection of use cases for which they would ordinarily be included in a well-structured CP dataset. Secondarily, the examples illustrate standardized formatting concepts for variables that are not associated with a formal Controlled Terminology codelist. Although not controlled, the standardized formatting of content for these variables significantly aids understanding of the test and associated data, making data review and comparisons much easier. To make the examples as easy to understand as possible, many of the other SDTM variables that would normally be included in the dataset and which are already familiar to the reader have not been included.

The following new SDTM variables are included in the examples: CPSBMRKS (Sublineage Marker String), CPCELSTA (Cell State), CPCSMRKS (Cell State Marker String), CPTSTCND (Test Condition), CPCNDAGT (Test Condition Agent), CPBDAGNT (Binding Agent), CPABCLID (Antibody Clone Identifier), CPMRKSTR (Marker String), CPGATE (Gate Name), CPGATDEF (Gate Definition), CPSPTSTD (Sponsor Test Description), CPTSTPNL (Test Panel), CPRESSCL (Result Scale), CPRESTYP (Result Type), and CPCOLSRT (Collected Summary Result Type). The proper use of each of these variables is illustrated in 1 or more of the examples, based on the identified use case.

## Example 1

Example 1a illustrates use of the CPMRKSTR variable for an assay panel that enumerates several of the major named cell subpopulations of leukocytes. For most cases involving simple phenotyping, and when used in accordance with CP domain guidance, the CPMRKSTR variable is sufficient for providing the marker information needed to fully describe a test. As such, CPMRKSTR is the only new CP test qualifier variable having a Core designation of "Expected". In such a case, the sponsor may determine whether to include other permissible CP test qualifier variables, based on the needs of the data recipient. This example presents records that might typically be reported for a panel of tests quantifying T-cell, B-cell, monocyte, and natural killer (NK) cell populations, and for subtyping T-cells. In this example, the sponsor determined that none of the permissible CP test qualifier variables were needed to accurately comprehend or distinguish among tests in the dataset, so chose to include only the CPMRKSTR (complete markers string) information.

Example 1b, in addition to including the expected CPMRKSTR variable, introduces 2 additional variables: CPGATE and CPGATDEF. These variables convey gating information used in data collection and/or analyses, and are often needed to fully understand a test. Typically, either the full gating strategy or the penultimate gate is identified. Because different gating strategies for the same test can yield somewhat different test results, the CPGATE and CPGATDEF variables provide the means for transmitting this information at the test (i.e., record) level.

### Example 1a

**Rows 1-3:** The total leukocyte population is determined using positive expression of the CD45 marker as the operational definition of the test (CD45+ in the CPMRKSTR variable). The total leukocyte count is reported because it contains the value used as the denominator in several subsequent tests for leukocyte subpopulations. Row 2 contains the total lymphocyte count which, in addition to CD45, used Forward (FSC) and Side (SSC) Light Scatter properties to define the lymphocyte subpopulation of leukocytes. Row 3 shows the proportion of lymphocytes as a percentage of total leukocytes. Note that the value in CPMRKSTR used a forward slash ("/") to separate the numerator marker string from the denominator marker string.

**Rows 4-5:** The B-lymphocyte lineage of lymphocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD19+) and negative (i.e., CD3-, CD14-, and CD56-) marker expression.

**Rows 6-7:** The T-lymphocyte lineage of lymphocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD3+) and negative (i.e., CD19-, CD14-, and CD56-) marker expression.

**Rows 8-11:** The T-lymphocyte lineage is divided further into T helper and T cytotoxic sublineages. Using CPMRKSTR, the numerator is the marker string used to define the T helper subpopulation (as shown in row 8) or the T cytotoxic subpopulation (as shown in row 10), and the denominator consists of the marker string used to define the total T-lymphocyte population (as shown in row 6). A forward slash "/" is used to separate the numerator from denominator.

**Rows 12-13:** The monocyte lineage of leukocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD14+) and negative (i.e., CD3-, CD19-, and CD56-) marker expression.

**Rows 14-15:** The NK cell lineage of leukocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD56+) and negative (i.e., CD3-, CD19-, and CD14-) marker expression.

**Row 16:** The ratio of T helper to T cytotoxic lymphocytes is calculated from the T helper (CD4+) cell count in row 8 and the T cytotoxic (CD8+) cell count in row 10 and a unit of measure is not included because it is not reported by the lab for this type of test.

**cp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPMRKSTR | CPCAT | CPORRES | CPORRESU | CPSTRESC | CPSTRESN | CPRESU | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
|-----|---------|--------|---------|-------|----------|--------|----------|-------|---------|----------|----------|----------|--------|----------|----------|--------|----------|-------|
| 1 | ABCD | CP | ABCD-001-001 | 1 | WBC | Leukocytes | CD45+ | IMMUNOPHENOTYPING | 6630 | 10^6/L | 6630 | 6630 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 2 | ABCD | CP | ABCD-001-001 | 2 | LYM | Lymphocytes | CD45+FSC SSC | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 1710 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 3 | ABCD | CP | ABCD-001-001 | 3 | LYMLE | Lymphocytes/Leukocytes | CD45+FSC SSC/CD45+ | IMMUNOPHENOTYPING | 25.8 | % | 25.8 | 25.8 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 4 | ABCD | CP | ABCD-001-001 | 4 | BLYCE | B-Lymphocytes | CD45+CD3-CD19+CD14-CD56- | IMMUNOPHENOTYPING | 104 | 10^6/L | 104 | 104 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 5 | ABCD | CP | ABCD-001-001 | 5 | BLYCELY | B-Lymphocytes/Lymphocytes | CD45+CD3-CD19+CD14-CD56-/CD45+FSC SSC | IMMUNOPHENOTYPING | 6.1 | % | 6.1 | 6.1 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 6 | ABCD | CP | ABCD-001-001 | 6 | TLYCE | T-Lymphocytes | CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 1108 | 10^6/L | 1108 | 1108 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 7 | ABCD | CP | ABCD-001-001 | 7 | TLYLY | TLym/Lym | CD45+CD3+CD19-CD14-CD56-/CD45+FSC SSC | IMMUNOPHENOTYPING | 64.8 | % | 64.8 | 64.8 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 8 | ABCD | CP | ABCD-001-001 | 8 | TLYH | TLym Help | CD45+CD3+CD4+CD8-/CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 425 | 10^6/L | 425 | 425 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 9 | ABCD | CP | ABCD-001-001 | 9 | TLYHTLY | TLym Help/TLym | CD45+CD3+CD19+CD4+CD8-/CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 38.4 | % | 38.4 | 38.4 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 10 | ABCD | CP | ABCD-001-001 | 10 | TLC | TLym Cytx | CD45+CD3+CD4-CD8+ | IMMUNOPHENOTYPING | 682 | 10^6/L | 682 | 682 | | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 11 | ABCD | CP | ABCD-001-001 | 11 | TLYCTLY | TLym Cytx/TLym | CD45+CD3+CD4-CD8+/CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 61.6 | % | 61.6 | 61.6 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 12 | ABCD | CP | ABCD-001-001 | 12 | MONO | Monocytes | CD45+CD3-CD19-CD14+CD56- | IMMUNOPHENOTYPING | 613 | 10^6/L | 613 | 613 | | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 13 | ABCD | CP | ABCD-001-001 | 13 | MONOCLE | Monocytes/Leukocytes | CD45+CD3-CD19-CD14+CD56-/FSC SSC/CD45+ | IMMUNOPHENOTYPING | 9.3 | % | 9.3 | 9.3 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 14 | ABCD | CP | ABCD-001-001 | 14 | NKCE | Natural Killer Cells | CD45+CD3-CD19-CD14-CD56+FSC SSC | IMMUNOPHENOTYPING | 230 | 10^6/L | 230 | 230 | | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 15 | ABCD | CP | ABCD-001-001 | 15 | NKLE | NK Cells/Leuk | CD45+CD3-CD19-CD14-CD56+FSC SSC/CD45+ | IMMUNOPHENOTYPING | 3.5 | % | 3.5 | 3.5 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 16 | ABCD | CP | ABCD-001-001 | 16 | TLYHTLYC | TLym Help/TLym Cytx | CD45+CD3+CD4+CD8-/CD45+CD3+CD4-CD8+ | IMMUNOPHENOTYPING | 0.62 | | 0.62 | 0.62 | | QUANTITATIVE | RATIO | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |

### Example 1b

**Row 1:** The total leukocyte count is reported for a whole blood specimen in which the CD45 marker is used to identify the leukocyte population. FSC and SSC are used to exclude debris and non-singlets from data collection events.

**Rows 2-3:** The total lymphocyte subpopulation of leukocytes is reported in row 2 as an absolute cell count, and in row 3 as a percentage of leukocytes. In these cases, FSC and SSC were used as subgates to isolate the lymphocyte lineage within the leukocyte (CD45+) population. Because FSC and SSC (in addition to the CD45 leukocyte marker) are used to define the lymphocyte lineage, they are included in CPMRKSTR.

**Row 4:** Illustrates an alternative way a sponsor chose to construct the value of CPMRKSTR using the gate name in CPGATE (operationally defined in CPGATDEF) as the denominator.

**cp.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPORRES | CPORRESU | CPSTRESC | CPSTRESN | CPRESU | CPRESSCL | CPRESTYP | CPMETHOD | CPSPEC | CPDTC |
|-----|---------|--------|---------|-------|----------|--------|----------|--------|----------|-------|---------|----------|----------|----------|--------|----------|----------|----------|--------|-------|
| 1 | ABCD | CP | ABCD-001-001 | 1 | WBC | Leukocytes | CD45+ | FSC SSC | IMMUNOPHENOTYPING | 6630 | 10^6/L | 6630 | 6630 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | FLOW CYTOMETRY | BLOOD | 2021-08-16T04:20 |
| 2 | ABCD | CP | ABCD-001-001 | 2 | LYM | Lymphocytes | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 1710 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | FLOW CYTOMETRY | BLOOD | 2021-08-16T04:20 |
| 3 | ABCD | CP | ABCD-001-001 | 3 | LYMLE | Lymphocytes/Leukocytes | CD45+FSC SSC/CD45+ | | | IMMUNOPHENOTYPING | 25.8 | % | 25.8 | 25.8 | | QUANTITATIVE | NUMBER FRACTION | FLOW CYTOMETRY | BLOOD | 2021-08-16T04:20 |
| 4 | ABCD | CP | ABCD-001-001 | 4 | LYM | Lymphocytes | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 1710 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | FLOW CYTOMETRY | BLOOD | 2021-08-16T04:20 |

## Example 2

This example shows data from a lymphocyte apoptosis assay and how the new permissible variables CPCELSTA and CPCSMRKS are used to indicate the biological state of the cell population measured in the test (e.g., viable, apoptotic, activated, exhausted, senescent, proliferating). Although in most cases only viable cells are measured in a test, making it unnecessary to specifically indicate their viability status in the test, there are other situations (e.g., when the ratio of viable to non-viable cells is of particular interest) when each cell state needs to be explicitly indicated in order to differentiate the tests. The principles illustrated in the example using CPCELSTA and CPCSMRKS variables also apply to more complex tests when the biological state of the cell population is considered to be integral to the test.

**Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD-. This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate (CPGATE).

**Rows 3-4:** Illustrate using CPCELSTA and CPCSMRKS to provide (1) the cell state descriptor in CPCELSTA, and (2) the markers used to define the cell state in CPCSMRKS. These variables further define CPTEST to be a subset of cells named in CPTEST; therefore the suffix "Sub" is appended to the value in CPTEST. In this example, the sponsor is interested in contrasting viable cells with those in the process of dying (non-viable), so each population is reported and the records differentiated using CPCELSTA and CPCSMRKS.

**Rows 5-6:** Illustrate using CPCELSTA and CPCSMRKS for the apoptotic lymphocyte subpopulation, both as a cell count (row 5) and as a percentage of total lymphocytes (row 6). The apoptotic cell state in CPCELSTA is defined as cells that are ANXV+ in CPCSMRKS. As in rows 3 and 4, the suffix "Sub" is added to the value of CPTEST to indicate it is a subpopulation of lymphocytes (i.e., apoptotic, being defined).

**Rows 7-8:** Illustrate using CPTEST, CPCELSTA, and CPCSMRKS variables to present findings when the cell population has more than a single cell state of interest (e.g., both viable and apoptotic). In this case, viability marker 7AAD is used in combination with apoptosis marker ANXV.

**Rows 9-11:** Illustrate a need to pre-coordinate information into the test name when the test incorporates results from two or more records (e.g., a ratio) in which key component(s) of the test are split across multiple variables. In the example, rows 9 and 10 use the CPCELSTA variable to indicate that the measured lymphocyte subpopulation includes only viable cells (row 9) or dying (non-viable cells, row 10). The ratio of viable to nonviable lymphocytes in row 11 is calculated using data from rows 9 and 10.

*(Due to extreme table width, the cp.xpt table for this example contains columns: Row, STUDYID, DOMAIN, USUBJID, CPSEQ, CPGRPID, CPTESTCD, CPTEST, CPSBMRKS, CPCELSTA, CPCSMRKS, CPGATE, CPGATDEF, CPCAT, CPORRES, CPORRESU, CPSTRESC, CPSTRESN, CPRESU, CPRESSCL, CPRESTYP, CPMETHOD, CPSPEC, CPDTC — with 11 rows of data.)*

## Example 3

This example shows data from a monocyte subset assay to highlight the use of new CP domain variables to capture cell sublineage information in CPSBMRKS, CPCELSTA and CPCSMRKS, and to illustrate how CPTEST is qualified by the context of those variables.

CPTEST is used to identify named cell populations (i.e., those cell types assigned names established by the scientific community). However, simply naming a cell type in CPTEST is often not sufficient for identifying or distinguishing among further subpopulations within that named population. In those cases, CPTEST alone does not contain the full complement of information needed to accurately define a test. 3 new variables that qualify CPTEST have been added to the CP domain specification for use when needed. Two of the variables, CPCELSTA and CPCSMRKS, support identifying a cell state, and the third variable, CPSBMRKS, supports identifying additional markers needed to subdivide the named population in CPTEST into further sublineages.

**Rows 1-3:** Show use of CPCELSTA and CPCSMRKS to further subset the named cell population in CPTEST. In row 1, the total monocyte population, based on expression of CD14, is measured without any further subsetting. Rows 2 and 3 show that the monocyte population is further subdivided, based on the cell state, into "proliferating" and "non-proliferating" subpopulations as indicated by CPCELSTA value. The value "Monocytes" in CPTEST for these rows is appended with "Sub" to "Monocytes Sub" to indicate that the second record pertains to a subpopulation of monocytes (i.e., proliferating or non-proliferating). CPCSMRKS is used to indicate that positive expression of the Ki67 marker (i.e., Ki67+) is used to identify the proliferating subpopulation and cells that do not express the Ki67 marker (i.e., Ki67-) is used to identify the non-proliferating subpopulation.

**Rows 4-5:** Show the proliferating (from row 2) and non-proliferating (from row 3) monocyte subpopulations expressed as a percentage of total monocytes (from row 1).

**Row 6:** Shows the ratio of the proliferating monocyte subpopulation to the non-proliferating monocyte subpopulation.

**Rows 7-9:** Show use of CPSBMRKS to further subset the named cell population in CPTEST into sublineages based on expression of additional markers CDxx and CDyy.

**Rows 10-11:** Show the monocyte sublineages defined in rows 8-9 expressed as a percentage of total monocytes (row 7).

**Row 12:** Demonstrates how CPSBMRKS, CPCELSTA, and CPCSMRKS work in combination with CPTEST to further define cell subpopulations based on any additional sublineage and cell state markers. The model allows for many combinations of values using these variables, thereby providing the flexibility to precisely specify a test. In all cases, the full complement of markers used for a test are populated into the CPMRKSTR variable.

*(Due to extreme table width, the cp.xpt table for this example contains 12 rows of data with columns including CPSBMRKS, CPCELSTA, CPCSMRKS, CPGRPID, and other standard CP variables.)*

## Example 4

This example shows data from a CCR5 cytotoxic T helper assay where test condition, stimulating agent, and replicate information is included to illustrate use of CPTSTCND, CPCNDAGT, CPREPNUM, and CPCOLSRT.

**Rows 1-3:** Illustrate how the test condition (CPTSTCND), replicates (REPNUM) and collected summary result type (CPCOLSRT) are used for a test system involving unstimulated CCR5+ cytotoxic T-lymphocytes. The two replicates and mean of the unstimulated condition are reported.

**Rows 4-6:** Illustrate the association between CPTSTCND, which identifies the condition applied to the assay system at runtime, and CPCNDAGT, which identifies the agent (if appropriate) used to impose the condition. CPREPNUM and CPCOLSRT are used as described for rows 1-3.

**Row 7:** Shows the record for the ratio of the stimulated to unstimulated populations based on mean results (i.e., records with CPCOLSRT = "MEAN"). The CPANMETH variable is populated with the formula used to calculate the result.

*(cp.xpt table contains 7 rows with columns including CPTSTCND, CPCNDAGT, CPREPNUM, CPCOLSRT, CPANMETH.)*

## Example 5

This example shows data from a B-lymphocyte activation assay with single-marker quantitation of a cell state marker using the formatting guidance for CPTEST and CPMRKSTR. It also demonstrates the use of CPGATE and CPGATDEF for reporting a full gating strategy and for reporting the total number of events counted within a gate.

**Rows 1-3:** Incorporates both standard proportion analysis and single marker expression for a cell state marker in the B lymphocyte assay using CPGRPID to group the related record. In accordance with CP guidance for quantitative single marker expression, row 3 contains the marker being measured followed by "Expression". CPMRKSTR uses the recommended format of listing the marker being measured first, followed by the unit in which expression was quantified (median fluorescence intensity, MdFI in the example), and lastly by the complete marker string of the cell population on which expression was measured. GATE and GATEDEF show the gating strategy so it is clear which gate was used to make the quantitative measurement of expression.

**Rows 4-8:** Show a set of tests similar to those in rows 1-3, except that the marker being quantified is more narrowly restricted to a subpopulation of B lymphocytes (i.e., naive B cells), which are identified using a richer set of markers. The sponsor chose, in row 6, to include the total number of events counted in the final gate to document that the data are reliable based on a sample size sufficient to reduce error to an appropriate level (e.g. 2-sigma).

*(cp.xpt table contains 8 rows with columns including CPGATE, CPGATDEF, and detailed marker string information.)*

## Example 6

This example shows use of CPSPTSTD for the lab/sponsor to describe a test in detail using internal data repository/dictionary nomenclature which has been developed for the test. The example uses a complex dendritic cell (DC) assay panel to illustrate information appropriate for this variable.

**Rows 1-6:** Illustrate how the sponsor uses CPSPTSTD to combine details of a test into a single variable to align with the lab/sponsor data repository or dictionary and to aid understanding of the test. Rows 1-4 introduce CPSPTSTD using simple tests for dendritic cells to set the stage for the more complex tests shown in rows 5-6.

**Rows 7-10:** Illustrate how CPSPTSTD might preface the name of a cell population with cell state marker(s) (e.g., CD83+ in rows 7-8) in addition to non-cell state, non-sublineage marker(s).

**Rows 11-14:** Same as rows 7-10, except here the cell state activation marker for the CD303+ pDC cell subset and the single marker expression measurement is CD80.

**Rows 15-18:** Illustrate how CPSPTSTD might preface the name of a cell population with cell sublineage marker(s) (e.g., CD40+ in rows 15-16) in addition to non-cell state, non-sublineage marker(s).

**Rows 19-32:** No new concepts are introduced in these rows, but they are additional illustrations of using CPSBMRKS, CPCELSTA, CPCSMRKR and CPSPTSTD for a subset of pDC in which CD123+ is a marker of interest which is neither a cell sublineage nor cell state marker. These rows are included to reinforce the principles illustrated in rows 1-18.

*(cp.xpt table contains 32 rows with extensive use of CPSPTSTD and marker string variables.)*

## Example 7

This example shows data from a monocyte target occupancy assay for which a cell surface marker of interest is bound to its specific protein or ligand (identified in CPBDAGNT) upon sample collection. In addition, three different ways for populating CPGATE and CPGATDEF are shown in the example.

Principles related to cell phenotyping are often used to measure the extent of binding between two molecules of interest (e.g., ligand-receptor or protein-protein interactions). Substances involved in the binding interaction can represent naturally occurring, pathological (i.e., disease-related), or therapeutic intervention processes. Quantification of these types of interactions is often used: (1) to aid in diagnosis and/or tracking disease progression; (2) to determine whether a therapy operating through a binding mechanism works as intended at selected doses; and (3) to assess whether potential off-target interactions, particularly those associated with undesirable side effects or safety risks, are likely to be a concern.

**Row 1:** The sponsor chose to submit only the final calculated result for target occupancy as reported by the lab, i.e., records used for the calculation were not submitted. The CPMRKSTR variable includes markers identifying the cell population (CD45+CD14+) and the target of interest (CDxx) on which occupancy was measured. CPGATE contains the name of the gate used to virtually isolate the cell population of interest and CPGATDEF contains the gate definition or gating strategy.

**Row 2:** Same as row 1 except that the sponsor chose to use CPGATE and CPGATDEF to report information for the final gate rather than the penultimate gate.

**Row 3:** The target of interest is also a marker needed to identify the named portion of the cell population on which the occupancy was measured. For example, proinflammatory monocytes are distinguished from monocytes based on additional marker expression criteria as CD16+HLADRhi.

*(cp.xpt table contains 3 rows with columns including CPBDAGNT, CPGATE, CPGATDEF.)*

## Example 8

This example is a use case for data from a receptor occupancy study based on a direct cell-binding assay method to illustrate the use of several new variables.

In the example, target engagement is assessed by measuring the extent to which a cell-associated target protein (the hypothetical cell marker CDxx) is occupied by a therapeutic antibody (CDxx antibody) intended to interact with it. The assay uses a labeled detection antibody to the therapeutic antibody to measure the proportion of the target bound by the therapeutic antibody in an unaltered specimen (numerator), as compared to the total amount of target available for binding (denominator). The total target available for binding is assessed by saturating the specimen with the therapeutic antibody before measuring the labeled detection antibody.

**Rows 1-3:** Illustrate how the test name (CPTEST), marker string (CPMRKSTR), binding agent (CPBDAGNT), replicates (CPREPNUM), and summary result type (CPCOLSRT) are populated for data from an assay used to assess target engagement by measuring the occupancy of the CDxx cell-associated target protein expressed on cytotoxic T-lymphocytes (defined as CD45+CD3+CD8+CDxx+). In this direct assay, CPBDAGNT identifies the CDxx antibody (therapeutic antibody) as the target-bound substance of interest. Two replicate determinations and the mean of CDxx bound in the unaltered specimen are indicated using CPREPNUM and CPCOLSRT.

**Rows 4-6:** CPTEST, CPBDAGNT, REPNUM, and CPCOLSRT are used the same manner as they are in rows 1-3, except that CPTSTCND is now also used to indicate that the assay was conducted under a saturating condition of CDxx antibody by adding an excess of this therapeutic antibody to the assay system.

**Rows 7-8:** Show values for background (i.e. non-specific) binding of the labeled detection antibody to the CDxx-expressing cells of interest by using an isotype control belonging to the same immunoglobulin class/subclass as the therapeutic antibody.

**Rows 9-11:** Rows 9 and 10 show values for specific binding of the therapeutic antibody (CDxx antibody) in the unaltered (native) specimen (Row 9) and the specimen to which excess CDxx antibody was added (saturated assay condition) (Row 10). Specific binding was determined by subtracting the appropriate background measured in Rows 7 and 8 from the mean target bound (Row 3) and mean target total (Row 6). Row 11 shows the final result for CDxx antibody occupancy on the CDxx target protein as the quotient of the specific binding in the native specimen (Row 9) to the specific binding measuring the total CDxx available for binding (Row 10).

*(cp.xpt table contains 11 rows with columns including CPBDAGNT, CPTSTCND, CPREPNUM, CPCOLSRT.)*

## Example 9

This example shows data from a monocyte receptor occupancy indirect detection assay for a target of interest relying upon externally applied assay conditions and several binding agents to measure the parameters reported.

Under certain circumstances, assessment of changes to free or unoccupied receptor (target) binding over the time-course of drug therapy or use of an indirect assay format may be more appropriate than direct detection of a binding agent (e.g., drug, small molecule ligand, protein) to obtain information on the extent of target engagement. Indirect assays of this sort rely on measuring remaining free (unbound) binding site using a labeled competitive detection probe (e.g., antibody or other ligand) that binds to the remaining available sites on the target; that is, those sites not already occupied by treating with the therapeutic. (Occupancy of the target by the therapeutic agent is then calculated as the difference between the total number of binding sites and the number of free binding sites detected by the probe.)

Sponsors may choose to report a single test for the final calculated occupancy, such as shown in row 1, or may elect to include results for the entire set of tests conducted which were then used to calculate the final occupancy result, such as shown in rows 2 through 14.

**Row 1:** The sponsor chose to submit only the final calculated result for target occupancy as reported by the lab; the data used in the calculation were not submitted. CPMRKSTR includes markers identifying the cell population (CD45+CD14+) and the target of interest (CD99) on which occupancy was measured. CPGATE contains the name of the gate used to virtually isolate the cell population of interest and CPGATDEF contains the gate definition.

*(cp.xpt table contains 14 rows illustrating indirect receptor occupancy detection with multiple binding agents, assay conditions, and calculated results.)*

## Source: `domains/CV/spec.md`

# CV — Cardiovascular System Findings

> Class: Findings | Structure: One record per finding or result per time point per visit per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### CVSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### CVGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### CVREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier.

### CVSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: a preprinted line identifier on a CRF.

### CVLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### CVLNKGRP
- **Order:** 9
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### CVTESTCD
- **Order:** 10
- **Label:** Short Name of Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** C101847
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in CVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" would not be valid). CVTESTCD cannot contain characters other than letters, numbers, or underscores.

### CVTEST
- **Order:** 11
- **Label:** Name of Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** C101846
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name For CVTESTCD. The value in CVTEST cannot be longer than 40 characters.

### CVCAT
- **Order:** 12
- **Label:** Category for Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### CVSCAT
- **Order:** 13
- **Label:** Subcategory for Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of CVCAT values.

### CVPOS
- **Order:** 14
- **Label:** Position of Subject During Observation
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### CVORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### CVORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. Unit for CVORRES.

### CVSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived, from CVORRES in a standard format or in standard units. CVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CVSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in CVORRES and these results effectively have the same meaning, they could be represented in standard format in CVSTRESC as "NEGATIVE".

### CVSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from CVSTRESC. CVSTRESN should store all numeric test results or findings.

### CVSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for CVSTRESC and CVSTRESN.

### CVSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### CVREASND
- **Order:** 21
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed (e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED"). Used in conjunction with CVSTAT when value is "NOT DONE".

### CVLOC
- **Order:** 22
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "HEART", "LEFT VENTRICLE".

### CVLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL", "UNILATERAL".

### CVDIR
- **Order:** 24
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### CVMETHOD
- **Order:** 25
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method used to create the result.

### CVLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### CVBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that CVBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### CVDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (i.e., a record that represents the average of other records, such as a computed baseline). Should be "Y" or null.

### CVEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", " INDEPENDENT ASSESSOR", "RADIOLOGIST".

### CVEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in CVEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### CVDTC
- **Order:** 36
- **Label:** Date/Time of Test
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### CVDY
- **Order:** 37
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CVTPT
- **Order:** 38
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See CVTPTNUM and CVTPTREF.

### CVTPTNUM
- **Order:** 39
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### CVELTM
- **Order:** 40
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (CVTPTREF). Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### CVTPTREF
- **Order:** 41
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by CVELTM, CVTPTNUM, and CVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### CVRFTDTC
- **Order:** 42
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by CVTPTREF.
---

## Cross References

### Controlled Terminology
- [Cardiovascular Test Name (C101846)](../../terminology/core/other_part1.md) — CVTEST
- [Cardiovascular Test Code (C101847)](../../terminology/core/other_part1.md) — CVTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — CVLOBXFL, CVBLFL, CVDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — CVSTAT
- [Position (C71148)](../../terminology/core/interventions.md) — CVPOS
- [Unit (C71620)](../../terminology/core/general_part5.md) — CVORRESU, CVSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — CVLOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — CVEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — CVMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — CVEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — CVLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — CVDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/CV/assumptions.md`

# CV — Assumptions

1. The Cardiovascular System Findings domain is used to represent results and findings of cardiovascular diagnostic procedures. Information about the conduct of the procedure(s), if collected, is submitted in the Procedures (PR) domain.

2. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the CV domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, --FAST, --ORNRLO, --ORNRHI, --TNRLO, --STNRHI, and --LOINC.

## Source: `domains/CV/examples.md`

# CV — Examples

## Example 1

This example shows various findings related to the aortic artery, along with evaluation for the presence or absence of abdominal aortic aneurysms. The suprarenal, infrarenal, and thoracic sections of the aorta were examined for aneurysms. This level of anatomical location detail can be found in CVLOC. The records in rows 1 to 3 are related assessments regarding an aneurysm in the thoracic aorta and are grouped together using the CVGRPID variable.

**cv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CVSEQ | CVGRPID | CVTESTCD | CVTEST | CVORRES | CVSTRESC | CVLOC | CVMETHOD | VISITNUM | VISIT | CVDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|-------|----------|----------|-------|-------|
| 1 | ABC123 | CV | 002-2004 | 1 | 2 | ANEURIND | Aneurysm Indicator | Y | Y | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 2 | ABC123 | CV | 002-2004 | 2 | 2 | DISECIND | Dissection Indicator | Y | Y | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 3 | ABC123 | CV | 002-2004 | 3 | 2 | STANFADC | Stanford AoD Classification | CLASS A | CLASS A | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 4 | ABC123 | CV | 002-2004 | 4 | | ANEURIND | Aneurysm Indicator | N | N | SUPRARENAL AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 5 | ABC123 | CV | 002-2004 | 5 | | ANEURIND | Aneurysm Indicator | N | N | INFRARENAL AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |

## Example 2

In this example CVTEST represents the structure of the aortic valve evaluated during a transthoracic echocardiography procedure.

**cv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CVSEQ | CVTESTCD | CVTEST | CVCAT | CVORRES | CVORRESU | CVSTRESC | CVSTRESN | CVSTRESU | CVLOC | CVMETHOD | VISITNUM | VISIT | CVDTC |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|-------|----------|----------|-------|-------|
| 1 | ABC123 | CV | 1001 | 1 | NCVALTYP | Native Cardiac Valve Structure Without Intervention Type | VALVULAR STRUCTURE, COMMON | NATIVE, WITHOUT INTERVENTION | | NATIVE, WITHOUT INTERVENTION | | | AORTIC VALVE | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 2 | ABC123 | CV | 1001 | 2 | SIZE | Size | VALVULAR STRUCTURE, COMMON | REDUCED | | REDUCED | | | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 3 | ABC123 | CV | 1001 | 3 | MNDIAEVS | Minor Axis Cross-sec Diameter, EVS | VALVULAR STRUCTURE, COMMON | 2.18 | cm | 2.18 | 2.18 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 4 | ABC123 | CV | 1001 | 4 | MJDIAEVS | Major Axis Cross-sec Diameter, EVS | VALVULAR STRUCTURE, COMMON | 2.48 | cm | 2.48 | 2.48 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 5 | ABC123 | CV | 1001 | 5 | MNDIAEVD | Minor Axis Cross-sec Diameter, EVD | VALVULAR STRUCTURE, COMMON | 1.92 | cm | 1.92 | 1.92 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 6 | ABC123 | CV | 1001 | 6 | MJDIAEVD | Major Axis Cross-sec Diameter, EVD | VALVULAR STRUCTURE, COMMON | 2.58 | cm | 2.58 | 2.58 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 7 | ABC123 | CV | 1001 | 7 | MNDIAMVS | Minor Axis Cross-sec Diameter, MVS | VALVULAR STRUCTURE, COMMON | 2.11 | cm | 2.11 | 2.11 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 8 | ABC123 | CV | 1001 | 8 | MJDIAMVS | Major Axis Cross-sec Diameter, MVS | VALVULAR STRUCTURE, COMMON | 2.39 | cm | 2.39 | 2.39 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
