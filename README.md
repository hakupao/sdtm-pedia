<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=40&pause=1000&color=36BCF7&center=true&vCenter=true&random=false&width=600&height=80&lines=SDTM+Pedia" alt="SDTM Pedia" />
</a>

<p><strong>Turn unreadable PDFs into an AI-ready, instantly searchable SDTM knowledge base.</strong></p>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![SDTM IG](https://img.shields.io/badge/SDTM_IG-v3.4-blue.svg)]()
[![SDTM](https://img.shields.io/badge/SDTM-v2.0-blue.svg)]()
[![Domains](https://img.shields.io/badge/Domains-63-green.svg)]()
[![Files](https://img.shields.io/badge/Files-293-green.svg)]()
[![Codelists](https://img.shields.io/badge/Codelists-1%2C005-orange.svg)]()
[![Terms](https://img.shields.io/badge/Terms-37%2C939-orange.svg)]()

[English](README.md) | [中文](README_CN.md)

</div>

---

## About

CDISC SDTM standards are locked inside dense PDFs and sprawling Excel files — hard to search, hard to cross-reference, and nearly impossible for AI to use reliably.

**SDTM Pedia** converts these source documents into **293 structured Markdown files**, organized by domain, terminology, and conceptual model. The result is a knowledge base that both humans and AI can navigate instantly — no vector database required.

## Features

| Feature | Description |
|---------|-------------|
| **PDF → Markdown** | Transforms 535+ pages of SDTM PDF specifications into structured, searchable Markdown |
| **63 Domains** | Every SDTM IG v3.4 domain covered with `spec.md` + `assumptions.md` + `examples.md` |
| **37,939 Terms** | Complete CDISC Controlled Terminology — 1,005 codelists, fully indexed |
| **AI-Ready** | Designed as a knowledge base for LLMs — works directly with Claude Projects, Cursor, etc. |
| **Zero Infrastructure** | No vector database, no embedding pipeline — just files and directory structure |
| **Actively Maintained** | Ongoing iteration to improve retrieval precision and cross-referencing |

## Architecture

```mermaid
graph LR
    subgraph Sources
        A[SDTMIG v3.4 PDF<br/>461 pages]
        B[SDTM v2.0 PDF<br/>74 pages]
        C[SDTMIG v3.4 xlsx<br/>63 domains]
        D[Terminology xlsx<br/>1,005 codelists]
    end

    subgraph Pipeline
        E[Python Scripts<br/>generate & validate]
        F[AI-Assisted Extraction<br/>assumptions & examples]
    end

    subgraph Knowledge Base
        G[model/<br/>6 files]
        H[chapters/<br/>6 files]
        I[domains/<br/>63 × 3 files]
        J[terminology/<br/>91 files]
        K[INDEX.md]
    end

    subgraph Consumers
        L[Claude Project]
        M[Claude Code]
        N[Other LLMs]
    end

    A --> E
    B --> F
    C --> E
    D --> E
    A --> F
    E --> G
    E --> J
    F --> H
    F --> I
    E --> I
    G --> K
    H --> K
    I --> K
    J --> K
    K --> L
    K --> M
    K --> N
```

## Project Structure

```
sdtm-pedia/
├── knowledge_base/              # The knowledge base (293 files)
│   ├── INDEX.md                 # Master index — navigation entry point
│   ├── model/                   # SDTM v2.0 conceptual model (6 files)
│   │   ├── concepts_and_terms.md
│   │   ├── observation_classes.md
│   │   ├── special_purpose_domains.md
│   │   ├── associated_persons.md
│   │   ├── study_level_data.md
│   │   └── relationship_datasets.md
│   ├── chapters/                # SDTMIG v3.4 general chapters (6 files)
│   │   ├── ch01_introduction.md
│   │   ├── ch02_fundamentals.md
│   │   ├── ch03_submitting_data.md
│   │   ├── ch04_general_assumptions.md
│   │   ├── ch08_relationships.md
│   │   └── ch10_appendices.md
│   ├── domains/                 # 63 domains × 3 files each
│   │   ├── AE/
│   │   │   ├── spec.md          # Variable specification table
│   │   │   ├── assumptions.md   # Domain-specific business rules
│   │   │   └── examples.md      # Implementation examples with data
│   │   ├── CM/
│   │   ├── DM/
│   │   ├── LB/
│   │   └── ...                  # 63 domains total
│   └── terminology/             # CDISC Controlled Terminology (91 files)
│       ├── core/                # Core codelists (42 files)
│       ├── questionnaires/      # Questionnaire codelists (43 files)
│       └── supplementary/       # Supplementary codelists (6 files)
│
├── source/                      # Original CDISC source files
│   ├── SDTMIG v3.4 (no header footer).pdf
│   ├── SDTMIG_v3.4.xlsx
│   ├── SDTM_v2.0.pdf
│   └── SDTM Terminology.xlsx
│
├── .work/                       # Build workspace
│   ├── analysis/                # Design documents
│   ├── scripts/                 # Python generation & validation scripts
│   ├── todo.md                  # Roadmap
│   ├── page_index.json          # PDF page index for extraction
│   └── worklog.md               # Build log
│
├── SDTM_Project_Instructions.md # Claude Project instruction template
├── SDTM_Project_Setup_Guide.md  # Step-by-step setup guide
└── PROGRESS.md                  # Build progress dashboard
```

## Domain Coverage

<details>
<summary><b>Special-Purpose Domains (5)</b></summary>

| Domain | Name |
|--------|------|
| CO | Comments |
| DM | Demographics |
| SE | Subject Elements |
| SM | Subject Disease Milestones |
| SV | Subject Visits |

</details>

<details>
<summary><b>Interventions Domains (7)</b></summary>

| Domain | Name |
|--------|------|
| AG | Procedure Agents |
| CM | Concomitant/Prior Medications |
| EC | Exposure as Collected |
| EX | Exposure |
| ML | Meal Data |
| PR | Procedures |
| SU | Substance Use |

</details>

<details>
<summary><b>Events Domains (7)</b></summary>

| Domain | Name |
|--------|------|
| AE | Adverse Events |
| BE | Biospecimen Events |
| CE | Clinical Events |
| DS | Disposition |
| DV | Protocol Deviations |
| HO | Healthcare Encounters |
| MH | Medical History |

</details>

<details>
<summary><b>Findings Domains (31)</b></summary>

| Domain | Name |
|--------|------|
| BS | Biospecimen Findings |
| CP | Cell Phenotype Findings |
| CV | Cardiovascular System Findings |
| DA | Product Accountability |
| DD | Death Details |
| EG | ECG Test Results |
| FA | Findings About Events or Interventions |
| FT | Functional Tests |
| GF | Genomics Findings |
| IE | Inclusion/Exclusion Criteria Not Met |
| IS | Immunogenicity Specimen Assessments |
| LB | Laboratory Test Results |
| MB | Microbiology Specimen |
| MI | Microscopic Findings |
| MK | Musculoskeletal System Findings |
| MS | Microbiology Susceptibility |
| NV | Nervous System Findings |
| OE | Ophthalmic Examinations |
| PC | Pharmacokinetics Concentrations |
| PE | Physical Examination |
| PP | Pharmacokinetics Parameters |
| QS | Questionnaires |
| RE | Respiratory System Findings |
| RP | Reproductive System Findings |
| RS | Disease Response and Clin Classification |
| SC | Subject Characteristics |
| SR | Skin Response |
| SS | Subject Status |
| TR | Tumor/Lesion Results |
| TU | Tumor/Lesion Identification |
| UR | Urinary System Findings |
| VS | Vital Signs |

</details>

<details>
<summary><b>Trial Design Domains (7)</b></summary>

| Domain | Name |
|--------|------|
| TA | Trial Arms |
| TD | Trial Disease Assessments |
| TE | Trial Elements |
| TI | Trial Inclusion/Exclusion Criteria |
| TM | Trial Disease Milestones |
| TS | Trial Summary |
| TV | Trial Visits |

</details>

<details>
<summary><b>Relationship & Study Reference Domains (5)</b></summary>

| Domain | Name |
|--------|------|
| OI | Non-host Organism Identifiers |
| RELREC | Related Records |
| RELSPEC | Related Specimens |
| RELSUB | Related Subjects |
| SUPPQUAL | Supplemental Qualifiers |

</details>

## Quick Start

### Use with Claude Project

The fastest way to use SDTM Pedia is as a Claude Project knowledge base.

1. **Clone the repo**
   ```bash
   git clone https://github.com/hakupao/stdm-pedia.git
   cd stdm-pedia
   ```

2. **Create a Claude Project** at [claude.ai](https://claude.ai) → Projects → Create project

3. **Set Instructions** — Copy the contents of `SDTM_Project_Instructions.md` into the project instructions

4. **Upload files** from `knowledge_base/` — See `SDTM_Project_Setup_Guide.md` for the recommended upload priority

5. **Start querying**
   ```
   AE domain has which Required variables?
   How should DM's RFSTDTC be populated?
   What are the allowed values for SEX codelist?
   ```

> For detailed setup instructions, see [SDTM_Project_Setup_Guide.md](SDTM_Project_Setup_Guide.md)

### Use with Claude Code

Point Claude Code at the `knowledge_base/` directory — it will use `INDEX.md` to navigate and read relevant files on demand.

### Use with Other LLMs

The knowledge base is plain Markdown — it works with any LLM that supports file-based context (Cursor, Windsurf, GitHub Copilot, etc.).

## Source Documents

| Document | Version | Content |
|----------|---------|---------|
| SDTM Implementation Guide | v3.4 | 461 pages — domain specs, assumptions, examples |
| SDTM (Study Data Tabulation Model) | v2.0 Final (2021-11-29) | 74 pages — conceptual model |
| SDTMIG v3.4 xlsx | — | 1,917 variables across 63 domains |
| SDTM Terminology xlsx | — | 1,005 codelists / 37,939 terms |

## Roadmap

- [x] Phase 1 — xlsx auto-generation (spec.md + terminology)
- [x] Phase 2 — PDF page indexing
- [x] Phase 3 — PDF batch extraction (assumptions + examples)
- [x] Phase 4 — Supplementary content (model + chapters)
- [x] Phase 5 — Validation & INDEX.md
- [ ] Phase 6.1 — Query routing index (ROUTING.md)
- [ ] Phase 6.2 — Cross-references between domains
- [ ] Phase 6.3 — Variable-level reverse index
- [ ] Phase 6.4 — Structured metadata (YAML/JSON)

## Disclaimer

The knowledge base content is derived from CDISC published standards. **CDISC** is a registered trademark of the Clinical Data Interchange Standards Consortium. This project is **NOT** affiliated with, endorsed by, or sponsored by CDISC.

- The original CDISC source files (PDFs/xlsx) are **NOT** included in this repository due to copyright restrictions
- This knowledge base should **NOT** be considered a substitute for official CDISC publications
- For regulatory submissions, always refer to the original CDISC standards

For the full disclaimer, see [DISCLAIMER.md](DISCLAIMER.md).

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). This license applies only to the original structuring and formatting work — the underlying standard definitions remain the intellectual property of CDISC.

## Acknowledgements

- [CDISC](https://www.cdisc.org/) — For developing and publishing the SDTM standards
- [Claude](https://claude.ai/) — AI-assisted extraction and validation pipeline

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=hakupao/stdm-pedia&type=Date)](https://star-history.com/#hakupao/stdm-pedia)

<a href="https://github.com/hakupao/stdm-pedia/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hakupao/stdm-pedia" />
</a>

<br/>

**If this project helps your SDTM work, a star would be appreciated!**

</div>

<p align="right">(<a href="#top">back to top</a>)</p>
