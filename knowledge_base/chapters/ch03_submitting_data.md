# SDTMIG v3.4 — Chapter 3: Submitting Data in Standard Format

Source: SDTMIG v3.4, Section 3 (Pages 17-21)

## 3.1 Standard Metadata for Dataset Contents and Attributes

The SDTMIG provides standard descriptions of some of the most commonly used data domains, with metadata attributes. These include descriptive metadata attributes that should be included in a Define-XML document. In addition, the CDISC domain models include 2 shaded columns that are not sent to the FDA, but which assist sponsors:

- **CDISC Notes column** — information regarding the relevant use of each variable
- **Core column** — indicates how a variable is classified (see Section 4.1.5, SDTM Core Designations)

## 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata

The Define-XML document should describe each dataset included in the submission and describe the natural key structure of each dataset. Most studies will include Demographics (DM) and a set of safety domains — typically EX, CM, AE, DS, MH, LB, and VS.

Dataset definition metadata should include:
- Dataset filenames, descriptions, locations, structures, class, purpose, and keys

**Note:** "In the event that no records are present in a dataset (e.g., a small PK study where no subjects took concomitant medications), the empty dataset should not be submitted and should not be described in the Define-XML document."

### 3.2.1 Dataset-level Metadata

The Dataset-level Metadata table provides examples of dataset structures:

| Dataset | Description | Class | Structure | Purpose | Keys | Location |
|---------|-------------|-------|-----------|---------|------|----------|
| CO | Comments | Special Purpose | One record per comment per subject | Tabulation | STUDYID, USUBJID, IDVAR, COREF, COOTC | co.xpt |
| DM | Demographics | Special Purpose | One record per subject | Tabulation | STUDYID, USUBJID | dm.xpt |
| SE | Subject Elements | Special Purpose | One record per actual Element per subject | Tabulation | STUDYID, USUBJID, ETCD, SESTDTC | se.xpt |
| SM | Subject Disease Milestones | Special Purpose | One record per Disease Milestone per subject | Tabulation | STUDYID, USUBJID, MIDS | sm.xpt |
| SV | Subject Visits | Special Purpose | One record per actual or planned visit per subject | Tabulation | STUDYID, USUBJID, SVTERM | sv.xpt |
| AG | Procedure Agents | Interventions | One record per recorded intervention occurrence per subject | Tabulation | STUDYID, USUBJID, AGTRT, AGSTDTC | ag.xpt |
| CM | Concomitant/Prior Medications | Interventions | One record per recorded intervention occurrence or constant-dosing interval per subject | Tabulation | STUDYID, USUBJID, CMTRT, CMSTDTC | cm.xpt |
| EX | Exposure | Interventions | One record per protocol-specified study treatment, constant-dosing interval, per subject | Tabulation | STUDYID, USUBJID, EXTRT, EXSTDTC | ex.xpt |
| ... | (and 50+ more domains) | | | | | |

### Key Dataset Classes and Their Domains

| Class | Domains |
|-------|---------|
| **Special Purpose** | CO, DM, SE, SM, SV |
| **Interventions** | AG, CM, EC, EX, ML, PR, SU |
| **Events** | AE, BE, CE, DS, DV, HO, MH |
| **Findings** | BS, CP, CV, DA, DD, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SR, SS, TR, TU, UR, VS |
| **Trial Design** | TA, TD, TE, TI, TM, TS, TV |
| **Relationship** | RELREC, RELSPEC, RELSUB, SUPP-- |
| **Study Reference** | OI |

### 3.2.1.1 Primary Keys

The purpose of the Keys column is to aid reviewers in understanding the structure of a dataset. Keys should define uniqueness for records in a dataset.

**Definitions:**
- A **natural key** is a set of data (1 or more columns) that uniquely identifies an entity and distinguishes it from any other row. The advantage is that they exist already; the difficulty is that they may change.
- A **surrogate key** is a single-part, artificially established identifier. The --SEQ variable is an example of a surrogate key.

### 3.2.1.2 CDISC Submission Value-level Metadata

Findings data models are closely related to normalized, relational data models in a vertical structure of 1 record per observation. Because general observation class data structures are fixed, sometimes information that might appear as columns in a horizontal (denormalized) format will instead be represented as rows in an SDTM Findings structure.

**Example:** The Vital Signs (VS) domain could contain subject records related to diastolic and systolic blood pressure, height, weight, and body mass index (BMI). These data are all submitted in the normalized SDTM structure. VSTESTCD provides the key differentiator.

Value-level metadata should be provided in the Define-XML document to describe expected properties that differentiate these data types (e.g., data type, standard units, other attributes).
