# SDTM v2.0 — Chapter 4: Associated Persons Data

Source: SDTM v2.0, Section 4 (Page 50)

## Overview

Studies sometimes include data about "associated persons" who are not study subjects. These data are represented in domains based on the domains used to represent data about study subjects. The structure of these domains is described in this section.

Associated Persons (AP) data follow the same general observation class structure as study subject data, with the following key differences:

### AP Domain Rules

1. **Prefix convention:** AP domains use the domain code prefix `AP` followed by the relevant domain code. For example, associated persons demographics would use `APDM`.

2. **APID:** The variable APID is used as an identifier in AP domains (instead of USUBJID for subjects). APID was removed from Section 3.1.4 (Identifiers for All Classes) because APID is only allowed in AP domains. It is still listed in Section 3 as an identifier.

3. **Linking variables:**
   - **RSUBJID** — Related Subject Identifier: links the associated person record to a study subject
   - **RDEVID** — Related Device Identifier: links to a device when applicable
   - **SREL** — Subject Relationship: describes the relationship between the associated person and the study subject (e.g., "MOTHER", "FATHER", "SPOUSE", "CAREGIVER")

### Key Principles

- AP domains conform to the same general observation class models (Interventions, Events, Findings) used for subject data
- The same variables, roles, and controlled terminology apply
- Additional guidance for implementing AP domains is provided in the SDTM Implementation Guide: Associated Persons (SDTMIG-AP)
- AP domains are not part of the core SDTMIG for human clinical trials

### Variables Used in Associated Persons Data

The table of variables used in Associated Persons Data includes all variables from the general observation classes, with the addition of AP-specific identifiers:

| Variable | Label | Type | Role | Notes |
|----------|-------|------|------|-------|
| APID | Associated Persons Identifier | Char | Identifier | Unique identifier for the associated person |
| RSUBJID | Related Subject Identifier | Char | Identifier | Links to the study subject (USUBJID) |
| RDEVID | Related Device Identifier | Char | Identifier | Links to a device identifier |
| SREL | Subject Relationship | Char | Record Qualifier | Describes the relationship to the subject |
