# SDTMIG v3.4 — Chapter 4: Assumptions for Domain Models

Source: SDTMIG v3.4, Section 4 (Pages 22-59)

## Overview

This section describes basic concepts, business rules, and assumptions that should be taken into consideration before applying the domain models. It covers general domain assumptions, general variable assumptions, coding and controlled terminology assumptions, actual and relative time assumptions, and other assumptions.

---

## 4.1 General Domain Assumptions

### 4.1.1 Splitting Domains

- The general rule is that data should **not** be split across multiple datasets based on when data were collected. For example, prior and concomitant medications should both be in CM.
- **Exceptions:** Adverse Events (AE) and Medical History (MH) are separate for regulatory reporting needs
- Questionnaires should be split into separate datasets when the questionnaires are independent instruments (e.g., separate datasets for BDI-II vs. HAM-D)

### 4.1.2 Origin Metadata

Origin metadata describes the source of data values. Origin metadata is provided at the variable level in the Define-XML document. Traceability is an important concept — data should be traceable from analysis datasets back to SDTM datasets and from SDTM datasets back to source data.

### 4.1.3 Assigning Natural Keys in the Metadata

Sponsors should assign natural keys that define uniqueness for records. Natural keys should be listed in the Define-XML. In some instances, a supplemental qualifier (SUPP--) variable might contribute to the natural key of a record.

### 4.1.4 Standardizing SDTM Datasets

Standard datasets should follow the SDTM data structures. Variable order should match the order defined in the SDTM for the general observation class.

### 4.1.5 SDTM Core Designations

| Core Value | Meaning | Rule |
|------------|---------|------|
| **Req** (Required) | Must be included in the dataset | Must always be populated; dataset is non-conformant without it |
| **Exp** (Expected) | Must be included in the dataset | Value should be populated when available; null values expected when data not collected/applicable |
| **Perm** (Permissible) | May be included in the dataset | Include only when the study collects the data; do not include empty columns |

---

## 4.2 General Variable Assumptions

### 4.2.1 Sequence Variables (--SEQ)

- --SEQ provides a unique number for each record per subject per domain
- It is a surrogate key, not a natural key
- Values must be positive integers
- Should not be used as an implicit sort or temporal order

### 4.2.2 Grouping Variables (--GRPID)

- Used to link related records within the same domain
- Example: linking multiple CM records for a combination therapy

### 4.2.3 Reference Variables (--REFID)

- Internal or external identifier (e.g., specimen ID, ECG trace ID)

### 4.2.4 Sponsor-Defined Variables (--SPID)

- Sponsor-defined reference number (e.g., line number on a CRF page)

### 4.2.5 Study Identifier (STUDYID)

- Unique identifier for a study; same across all datasets in a submission

### 4.2.6 Unique Subject Identifier (USUBJID)

- Must be unique for each subject across all studies for the same compound
- CDISC does not recommend any specific format; only requires uniqueness across all subjects
- Many sponsors concatenate Study, Site, and Subject into USUBJID, but this is not required

### 4.2.7 Variable-Naming Conventions

- Variable names are limited to 8 characters (SAS v5 transport format)
- `--` prefix is replaced by 2-character domain code
- Variables without `--` prefix (e.g., STUDYID, USUBJID) are used as-is across all domains

#### 4.2.7.1 --TEST and --TESTCD Conventions (Findings)

- --TESTCD: up to 8 characters, standardized or dictionary-derived short sequence
- --TEST: full descriptive name of the test
- Both are subject to controlled terminology where available

#### 4.2.7.2 --TRT Conventions (Interventions)

- Contains the verbatim name of the treatment, drug, procedure, or therapy
- Should represent the name as reported on the CRF

#### 4.2.7.3 --TERM Conventions (Events)

- Contains the verbatim or prespecified name of the event
- Should represent the term as reported on the CRF

#### 4.2.7.4 "Specify" Values for --OBJ

- When FAOBJ represents a "Specify" value, the actual specified text should be used

### 4.2.8 Topic Variable Formats

The topic variables for each GOC:

| GOC | Topic Variable | Description |
|-----|---------------|-------------|
| Interventions | --TRT | Name of Treatment |
| Events | --TERM | Reported Term |
| Findings | --TESTCD | Short Name of Test |

### 4.2.9 Character Restrictions

- ASCII characters are recommended for variable names and values
- Non-ASCII characters may be used in data values when necessary but should be documented

---

## 4.3 Coding and Controlled Terminology Assumptions

### Overview

CDISC Controlled Terminology (CT) is centrally managed by the CDISC Controlled Terminology Team. Key principles:

- Variables subject to CT are indicated in domain specification tables
- An asterisk (*) next to a codelist name means the variable **may** be subject to CT (sponsor-defined values also acceptable)
- CT is updated quarterly; sponsors should check the CDISC CT website for the latest version
- The NCI Enterprise Vocabulary Services (NCI-EVS) website is the authoritative source

### 4.3.1 MedDRA Coding (Events)

- MedDRA is the standard dictionary for coding adverse events, medical history, and other event terms
- Coded terms populate --DECOD (Preferred Term), --LLT, --HLT, --HLGT, --SOC, --BODSYS and their corresponding code variables

### 4.3.2 WHODrug Coding (Interventions)

- WHODrug is the standard dictionary for coding concomitant medications
- Coded terms populate --DECOD (generic drug name), --CLAS, --CLASCD

---

## 4.4 Actual and Relative Time Assumptions

### 4.4.1 Date/Time Variables

- All date/time variables use **ISO 8601** format
- Character type (not numeric)
- Partial dates are supported: `2003`, `2003-06`, `2003-06-15`, `2003-06-15T13:15:17`
- The precision of the date/time reflects the precision of the collected data

### 4.4.2 Study Day Variables

- --DY is calculated as: `--DTC - RFSTDTC` (with no day 0)
- If --DTC is on or after RFSTDTC: DY = date portion of --DTC − date portion of RFSTDTC + 1
- If --DTC is before RFSTDTC: DY = date portion of --DTC − date portion of RFSTDTC
- Partial dates should not be used to derive study day

### 4.4.3 Study Reference Dates (DM Domain)

| Variable | Description |
|----------|-------------|
| RFSTDTC | Subject Reference Start Date/Time (basis for --DY) |
| RFENDTC | Subject Reference End Date/Time |
| RFXSTDTC | Date/Time of First Study Treatment |
| RFXENDTC | Date/Time of Last Study Treatment |
| RFCSTDTC | Date/Time of First Study Contact |
| RFCENDTC | Date/Time of Last Study Contact |
| RFICDTC | Date/Time of Informed Consent |
| RFPENDTC | Date/Time of End of Participation |
| DTHDTC | Date/Time of Death |

### 4.4.4 Intervals and Duration

- **Intervals** (--STDTC to --ENDTC): represented as 2 separate variables or a single ISO 8601 interval
- **Duration** (--DUR): ISO 8601 duration format (e.g., "P2D" = 2 days, "PT6H" = 6 hours)
- Duration should be collected directly, not derived from start/end dates (unless documented)

### 4.4.5 Clinical Encounters and Visits

- **VISITNUM**: numeric version of VISIT used for sorting
- **VISIT**: character name of the visit from the protocol
- There must be a **one-to-one relationship** between VISIT and VISITNUM
- Unplanned visits should use VISITNUM values that sort between planned visits (e.g., 1.1 between VISITNUM 1 and 2)

### 4.4.6 Representing Additional Study Days

- --XSTDY and --CHSTDY may be used for study designs with multiple reference start dates (e.g., crossover studies)

### 4.4.7 Use of Relative Timing Variables

| Variable | Values | Purpose |
|----------|--------|---------|
| --STRF | BEFORE, DURING, DURING/AFTER, AFTER, UNKNOWN | Start relative to the sponsor-defined reference period |
| --ENRF | BEFORE, DURING, DURING/AFTER, AFTER, UNKNOWN | End relative to the sponsor-defined reference period |
| --STRTPT | BEFORE, COINCIDENT, AFTER, UNKNOWN | Start relative to a specific reference time point |
| --STTPT | (free text) | Description of the reference time point for --STRTPT |
| --ENRTPT | BEFORE, COINCIDENT, AFTER, ONGOING, UNKNOWN | End relative to a specific reference time point |
| --ENTPT | (free text) | Description of the reference time point for --ENRTPT |

**Example applications:**
- **Medical History:** --STRTPT = "BEFORE", --STTPT = "INFORMED CONSENT"
- **Concomitant Medications:** --STRF = "BEFORE", --ENRF = "DURING"
- **Adverse Events:** --ENRTPT = "ONGOING", --ENTPT = "DATE OF LAST DOSE"

### 4.4.8 Date and Time in Findings

| Scenario | Variables Used |
|----------|---------------|
| Single point in time (e.g., lab draw) | --DTC |
| Assessment interval (e.g., time period) | --STDTC, --ENDTC |

**Note:** --STDTC is not used in Findings class domains for single-point-in-time observations; --DTC is the primary date variable.

### 4.4.9 Use of Dates as Result Variables

Dates should be used with caution as result values in --ORRES. When dates are the result of an observation (e.g., "Date of Last Menstrual Period"), they should be placed in --ORRES with the date in ISO 8601 format.

### 4.4.10 Representing Time Points

Time points are protocol-defined measurement times within a visit:

| Variable | Purpose |
|----------|---------|
| --TPT | Planned Time Point Name (e.g., "1 HOUR POST-DOSE") |
| --TPTNUM | Planned Time Point Number (for sorting) |
| --ELTM | Planned Elapsed Time from Reference (ISO 8601 duration) |
| --TPTREF | Time Point Reference description (e.g., "DOSE 1 OF TREATMENT A") |
| --RFTDTC | Date/Time of Reference Time Point |

For crossover trials, 2 options are available:
- **Option 1:** Use the same --TPTNUM across periods; differentiate by VISIT
- **Option 2:** Use unique --TPTNUM values across all periods

### 4.4.11 Disease Milestones

Disease Milestones (defined in TM, recorded in SM) provide a way to anchor observations to clinically significant time points:

| Variable | Purpose |
|----------|---------|
| MIDS | Disease Milestone Instance Name |
| RELMIDS | Relationship to Disease Milestone Instance |
| MIDSDTC | Disease Milestone Instance Date |

**Linking guidance:** Observations can reference disease milestones using MIDS, RELMIDS, and MIDSDTC in the general observation class timing variables.

---

## 4.5 Other Assumptions

### 4.5.1 Original and Standardized Results

The SDTM provides a 3-level result framework for Findings:

```
ORRES (Original) → STRESC (Standardized Character) → STRESN (Standardized Numeric)
```

**Key rules:**
- --ORRES: always the originally collected/reported value
- --STRESC: standardized character result (may equal --ORRES if no standardization needed)
- --STRESN: numeric version of --STRESC (null when result is non-numeric)
- --ORRESU / --STRESU: original and standard units

**Tests Not Done:**
- When a test is not performed: --STAT = "NOT DONE", --REASND = reason
- --ORRES, --STRESC, --STRESN must all be null when --STAT = "NOT DONE"
- --ORRESU and --STRESU should also be null

### 4.5.2 Linking Multiple Observations

Use --GRPID to link records within the same domain, and RELREC to link records across domains.

### 4.5.3 Text Strings Longer than Maximum Length

| Scenario | Solution |
|----------|----------|
| --TEST value > 40 characters | Use a shorter --TEST label; the full descriptive name goes in Define-XML |
| Text value > 200 characters | Split into SUPP-- with multiple QVAL entries, or truncate with documentation |
| Domain-specific long text | CO.COVAL, IE.IETEST, TS.TSVAL, TI.IETEST: variable lengths of 200 or 500+ characters may be supported |

### 4.5.4 Evaluators in Interventions and Events

When evaluator information needs to be captured for Interventions or Events domains (which do not have --EVAL), use SUPP-- datasets.

**Example:** SUPPAE with QNAM = "AEEVAL", QLABEL = "Evaluator", QVAL = "INVESTIGATOR"

### 4.5.5 Clinical Significance (--CLSIG)

- --CLSIG is a standard variable in Findings domains
- Used to indicate whether a finding is clinically significant
- Values are subject to controlled terminology

### 4.5.6 Supplemental Reason Variables (--REASOC)

- --REASOC represents the reason for the value in --OCCUR
- --REASOC does not replace --INDC
- Used in both Events and Interventions classes

**Example:** SUPPHO with QNAM = "HOREASOC" for reason in Healthcare Encounters

### 4.5.7 Presence/Absence of Pre-specified Events and Interventions

| Variable | Purpose | Valid Values |
|----------|---------|-------------|
| --PRESP | Pre-Specified | "Y" (prespecified) or null (spontaneously reported) |
| --OCCUR | Occurrence Indicator | "Y" (occurred) or "N" (did not occur) |
| --STAT | Completion Status | "NOT DONE" or null |

**Rules:**
- If --PRESP = "Y" and --OCCUR = "N": the prespecified item did not occur
- If --PRESP = "Y" and --OCCUR = "Y": the prespecified item occurred
- If --PRESP is null: the observation was spontaneously reported (not prespecified)
- --OCCUR and --STAT should not both be populated on the same record

### 4.5.8 Long-term Follow-up

For studies with long-term follow-up (e.g., oncology), a 6-step approach is recommended:

1. Define the reference period (typically first dose to last dose)
2. Collect data during the reference period using standard domains
3. Define a follow-up period after the reference period
4. Continue collecting data in standard domains during follow-up
5. Use --STRF/--ENRF relative timing variables to indicate relationship to reference period
6. Consider using --EPOCH to distinguish treatment from follow-up periods

### 4.5.9 Baseline Values

| Variable | Scope | Use |
|----------|-------|-----|
| --LOBXFL | Last Observation Before Exposure Flag | Identifies the last non-null result before first exposure |
| ABLFL | Analysis Baseline Flag | ADaM analysis baseline indicator |
| --BLFL | Baseline Flag | Proposed for future SDTM use; identifies the baseline value in SDTM (not yet standard) |

**Note:** --LOBXFL is the SDTM variable for flagging the last observation before first exposure. The actual baseline determination for analysis purposes should be done in ADaM using ABLFL.
