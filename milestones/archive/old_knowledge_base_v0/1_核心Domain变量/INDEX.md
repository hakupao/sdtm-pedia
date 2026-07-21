# SDTM Knowledge Base Index

Welcome to the SDTM Reference Knowledge Base optimized for Claude Project retrieval. This comprehensive collection includes datasets, variables, terminology, and complete reference documents.

## Overview

This knowledge base contains SDTM (Study Data Tabulation Model) reference materials converted from official FDA/CDISC documents into markdown format for optimal LLM retrieval and search.

**Total Files:** 71

---

## Document Categories

### 1. Datasets Reference (SDTM IG v3.4)

**File:** `SDTMIG34_Datasets.md`

Complete listing of all SDTM domains organized by class:
- **Interventions:** AG, CM, EC, EX, ML, PR, SU
- **Events:** AE, BE, CE, DS, DV, HO, MH
- **Findings:** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Findings About:** FA, SR
- **Special-Purpose:** CO, DM, SE, SM, SV
- **Trial Design:** TA, TD, TE, TI, TM, TS, TV
- **Study Reference:** OI
- **Relationship:** RELREC, RELSPEC, RELSUB, SUPPQUAL

---

### 2. Variables Reference (SDTM IG v3.4)

Detailed variable specifications organized by domain. Each domain has its own file with complete variable definitions.

**Files:** `SDTMIG34_Variables_[DOMAIN].md`

Total files: 63

**Domains included:**
AE, AG, BE, BS, CE, CM, CO, CP, CV, DA, DD, DM, DS, DV, EC, EG, EX, FA, FT, GF, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, OI, PC, PE, PP, PR, QS, RE, RELREC, RELSPEC, RELSUB, RP, RS, SC, SE, SM, SR, SS, SU, SUPPQUAL, SV, TA, TD, TE, TI, TM, TR, TS, TU, TV, UR, VS

Each file contains:
- Variable name and label
- Type (Char/Num)
- Core status (Required/Conditional/Optional)
- Role (Identifier/Qualifier/Timing/Value/etc.)
- CDISC Notes and specifications

---

### 3. Terminology Reference

SDTM Controlled Terminology codelists organized by grouping for efficient search.

**Files:** `SDTM_Terminology_[GROUP].md`

Total files: 5

**Groupings:**
- A_C: Codelists starting with letters A-C (and numeric codes)
- G_L: Codelists starting with letters G-L
- GENERIC: Generic/other codelists
- U: Codelists starting with U
- C: Additional C codelists

Each codelist includes:
- Codelist code (e.g., C12345)
- Submission values
- Synonyms and variations
- All valid terms for the codelist

**Total codelist entries:** ~39,000 terms across ~1,000 codelists

---

### 4. SDTM Implementation Guide v3.4 (Complete Text)

**File:** `SDTMIG34_FullText.md` (2.6MB)

Complete text extraction from the official SDTM IG v3.4 PDF document.

Contains:
- All implementation guidance
- Domain specifications and requirements
- Variable definitions and specifications
- Controlled terminology references
- Technical requirements and constraints
- Examples and guidance notes

Raw text also available in: `SDTMIG34_RawText.txt`

---

### 5. SDTM Standard v2.0 (Complete Text)

**File:** `SDTM20_FullText.md` (468KB)

Complete text extraction from the SDTM v2.0 specification document.

Contains:
- Core SDTM concepts
- Domain definitions
- Fundamental requirements
- Data structure specifications

Raw text also available in: `SDTM20_RawText.txt`

---

## How to Use This Knowledge Base

### For Domain/Variable Lookup
Use the individual domain files (e.g., `SDTMIG34_Variables_AE.md`) for quick reference on specific domains.

Example queries:
- "What variables are in the AE domain?"
- "What is the structure of the LB domain?"
- "Show me all DM domain variables"

### For Terminology/Codelist Lookup
Use the terminology files to find valid codes and their meanings.

Example queries:
- "What are valid codes in the AESTATUS codelist?"
- "Show me pregnancy-related codelists"
- "What codes are valid for adverse event outcomes?"

### For Comprehensive Reference
Use the complete text files for detailed guidance, examples, and context.

Example queries:
- "How should I structure an AE domain dataset?"
- "What are the implementation requirements for pharmacokinetics?"
- "Explain the SDTM general structure requirements"

### For Datasets Overview
Use `SDTMIG34_Datasets.md` to understand the overall SDTM domain structure.

Example queries:
- "What are all the SDTM event domains?"
- "List all interventions domains"
- "What is the structure of the Demographics domain?"

---

## File Organization

```
project_knowledge_base/
├── Datasets Reference
│   └── SDTMIG34_Datasets.md
│
├── Variables Reference (63 files)
│   ├── SDTMIG34_Variables_AE.md
│   ├── SDTMIG34_Variables_DM.md
│   ├── SDTMIG34_Variables_LB.md
│   └── ... (one file per domain)
│
├── Terminology Reference (5 files)
│   ├── SDTM_Terminology_A_C.md
│   ├── SDTM_Terminology_G_L.md
│   ├── SDTM_Terminology_GENERIC.md
│   ├── SDTM_Terminology_U.md
│   └── SDTM_Terminology_C.md
│
├── Complete Documents
│   ├── SDTMIG34_FullText.md (complete IG v3.4)
│   ├── SDTM20_FullText.md (complete SDTM v2.0)
│   ├── SDTMIG34_RawText.txt (raw PDF extraction)
│   └── SDTM20_RawText.txt (raw PDF extraction)
│
└── INDEX.md (this file)
```

---

## Search Tips for Claude Projects

1. **Exact Domain Queries:** Reference the specific domain file (e.g., "From SDTMIG34_Variables_AE.md...")
2. **Multiple Domains:** Search terminology files for codes that span multiple domains
3. **Implementation Guidance:** Use the FullText files for detailed "how-to" questions
4. **Quick Reference:** Use individual domain files for quick lookups
5. **Related Concepts:** Cross-reference between variables and terminology files

---

## Document Metadata

**Source Documents:**
- SDTMIG_v3.4_Datasets.csv (v3.4)
- SDTMIG_v3.4_Variables.csv (1,917 variables across 63 domains)
- SDTM Terminology.csv (38,953 entries, 1,006 codelists)
- SDTMIG v3.4-FINAL_2022-07-21.pdf (2.6MB, complete implementation guide)
- SDTM_v2.0.pdf (specification document)

**Conversion Date:** 2026-04-07

**Format:** Markdown optimized for LLM retrieval via Claude Projects

---

## Quick Domain Reference

### Common Queries

**"Show me the DM domain variables"**
→ See: SDTMIG34_Variables_DM.md

**"What variables are in the AE domain?"**
→ See: SDTMIG34_Variables_AE.md

**"What are valid AESTATUS values?"**
→ See: SDTM_Terminology_A_C.md (search for AESTATUS)

**"How many domains are there?"**
→ See: SDTMIG34_Datasets.md (39 total domains)

**"What's the structure of the LB domain?"**
→ See: SDTMIG34_Variables_LB.md

**"What are the core variables?"**
→ See any SDTMIG34_Variables_[DOMAIN].md file (marked with "Req")

---

## Additional Resources

All raw PDF text extracts are available in TXT format for full-text search:
- `SDTMIG34_RawText.txt` - Original PDF content
- `SDTM20_RawText.txt` - SDTM v2.0 original content

For more information on SDTM standards, visit the official CDISC website.

---

**Version:** 1.0
**Last Updated:** 2026-04-07
**Format:** Markdown for Claude Project Knowledge Base
