---
lang: en
slug: methodology
order: 15
title: "Methodology"
---

# Methodology and Verification Statement

> Last updated: 2026-04-29 · Maintained alongside the build process. The status reported below reflects the current state of the verification track.

## Purpose

This document specifies how the SDTM knowledge base in this repository was constructed, the controls that govern its accuracy, and the procedures by which any individual claim can be independently audited against the source publications. It is published in this form so that users who rely on the knowledge base in regulated work — FDA, PMDA, or EMA submissions; SDTM data programming; mapping quality control — can establish, and re-establish, the level of trust they require.

The structure of the statement follows a verification logic familiar in clinical IT: declared sources of truth (§1), a defined construction pipeline (§2), an end-to-end traceability map (§3), a public record of identified non-conformances and their closure (§4), the standing controls the project enforces (§5), and the boundaries within which the artifact may be used (§6). Readers conducting a focused review may begin with [§4](#4-non-conformances-identified-and-closed).

## Compliance framing

The knowledge base derives from CDISC SDTM publications mandated by the U.S. Food and Drug Administration, recognized by the Japanese Pharmaceuticals and Medical Devices Agency, and accepted by the European Medicines Agency for clinical study data submissions. Work performed *using* this knowledge base is typically governed by ICH E6 (R3) Good Clinical Practice and the data-integrity principles consolidated as ALCOA+ (FDA, MHRA, WHO).

The construction methodology described below adopts a risk-based verification approach informed by GAMP 5 (ISPE) — declared specification, executed verification, independent review, and a documented anomaly trail — without claiming formal categorization or certification under those frameworks. Each control in §5 is mapped to its corresponding ALCOA+ dimension, and the verification evidence is retained in the repository for re-audit.

## 1. Authoritative sources

Every artifact under `knowledge_base/` is traceable to one of four official CDISC publications. No content in this repository is generated from third-party summaries or paraphrased renditions of the standard. AI-assisted components produce only source-grounded extractions; ungrounded generation is not permitted in the pipeline.

| Source | Version | Scope |
|---|---|---|
| SDTM Implementation Guide (PDF) | v3.4 (2021-11-29) | 461 pages — domain specifications, assumptions, examples |
| SDTM Model (PDF) | v2.0 Final (2021-11-29) | 74 pages — conceptual model |
| SDTMIG (xlsx) | v3.4 | 1,917 variables across 63 domains |
| CDISC Controlled Terminology (xlsx) | 2024 release | 1,005 codelists / 37,939 terms |

The original publications are not redistributed in this repository; CDISC retains copyright. See the [project disclaimer](https://github.com/hakupao/sdtm-pedia/blob/main/DISCLAIMER.md).

## 2. Construction pipeline

The knowledge base was produced through a seven-phase pipeline. Each phase is documented as a separate work package — a phase plan, an execution log, and a verification record — held under [`.work/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work) in the repository, which forms part of the auditable source rather than a separate documentation product.

| Phase | Activity | Primary output |
|---|---|---|
| 1 | Programmatic conversion of xlsx specifications to Markdown (Python) | 63 `spec.md` files; terminology indices |
| 2 | Programmatic PDF page indexing (no visual estimation) | `page_index.json` |
| 3 | AI-assisted extraction from the SDTMIG PDF, executed in 11 batches with per-batch verification | per-domain `assumptions.md`, `examples.md` |
| 4 | Supplementary content extraction (model and chapter level) | 6 model files; 6 chapter files |
| 5 | Full-pass validation with master indexing | `INDEX.md`; validation reports |
| 6 | Retrieval optimization (routing layer; reverse variable index) | `ROUTING.md`; `VARIABLE_INDEX.md` (1,523 variables) |
| 6.5 | AI platform deployment | Four-platform release bundle |

In parallel with the seven-phase pipeline, an independent **atom-level literal verification audit** is being executed as a continuing work track. Each atomic claim in the knowledge base is reconciled against the source PDF on a page-by-page basis. As of 2026-04-29 the audit covers **97% of the in-scope pages** and remains active. Per-batch evidence is published under [`.work/06_deep_verification/evidence/checkpoints/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work/06_deep_verification/evidence/checkpoints).

## 3. Traceability — auditing an individual answer

The repository is structured so that any single answer can be reconciled against the source publication within seconds, supporting the *Attributable* and *Accurate* dimensions of ALCOA+.

**Verification of a domain-level claim:**

1. Identify the domain code in the answer (`AE`, `LB`, `DM`, …).
2. Open `knowledge_base/domains/<DOMAIN>/`:
   - `spec.md` — variable-level specification (sourced from xlsx; Core, type, and codelist binding)
   - `assumptions.md` — domain-specific assumptions (sourced from PDF)
   - `examples.md` — implementation examples (sourced from PDF)
3. Each file's header carries the corresponding PDF page range. Reconcile against the SDTMIG v3.4 PDF.
4. Variable Core and codelist bindings can be verified against the SDTMIG xlsx where available.

**Verification of a chapter-level claim:** open `knowledge_base/chapters/chXX_*.md`. Page ranges and section numbers correspond directly to the SDTMIG table of contents.

**Verification of a controlled-terminology claim:** every codelist file under `knowledge_base/terminology/` carries the assigned CDISC C-code (for example `C66731`), enabling cross-reference against the NCI EVS Browser.

The complete source-to-output mapping is published as the [traceability matrix](https://github.com/hakupao/sdtm-pedia/blob/main/docs/TRACEABILITY.md) (`docs/TRACEABILITY.md`).

## 4. Non-conformances identified and closed

Two systemic non-conformances were identified during the validation phase. Both are publicly documented; their disclosure is a structural feature of the methodology, in line with the audit-trail expectations applied to electronic records in regulated clinical-IT environments.

### NCR-001 — Page-index drift (closed 2026-04-15)

The first iteration of the PDF figure-and-image index relied on AI components identifying page numbers by visual inspection. A sampling review by a domain expert determined that the page reference for the TD example was offset by four pages, with comparable drift of ±2 to ±4 pages distributed across approximately 60 figures.

**Root cause.** AI components performing visual reading of PDF cannot reliably observe page boundaries; they estimate. The pipeline did not, at that point, distinguish *exact* values from *estimated* values.

**Corrective action.** The page index was rebuilt programmatically. `page_index.json` is now the single authoritative source; all downstream files reference it; any AI-produced page reference that cannot be confirmed programmatically is labelled `(estimated)` and is not written into the authoritative index.

Investigation record: [`.work/03_verification/issue1_investigation.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issue1_investigation.md).

### NCR-002 — Skeleton content accepted as PASS (closed 2026-04-15)

`ch04_general_assumptions.md` was assigned a PASS verdict in the first validation pass although approximately 30% of its subsections contained only one or two sentences of placeholder text marked with `<!-- 待补全 -->`. The corresponding chapter of the SDTMIG comprises 38 pages of detailed rules; the file at the time of the original PASS averaged approximately 9 lines per page, against approximately 17 lines per page after remediation.

**Root cause.** The PASS criterion accepted *"missing content has been clearly marked as missing"* as a substitute for *"content is complete."* In addition, the agent that authored the file also approved it; no independent reviewer read the source PDF.

**Corrective action.** Every flagged subsection was reconstructed from the source PDF. The PASS criterion was rewritten to require quantitative coverage: a defined minimum lines-per-page ratio against a baseline; zero placeholder markers; ≥ 95% point coverage. Author–approver separation became a standing control (rule 2 in §5).

Closure record: [`.work/03_verification/issues_found.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issues_found.md).

### Standing limitations

Certain limitations cannot be fully resolved within the current AI-platform deployment form — for example, large codelists stored as stubs, and real-time external lookups not embedded. These are tracked separately and disclosed in the deployment artifact: [Known Limitations](./known-limitations/).

## 5. Standing verification controls

The two non-conformances above resulted in four standing controls. They apply to every phase of every track in the repository, and their evidence is retained for re-audit.

| # | Control | ALCOA+ dimension |
|---|---|---|
| 1 | **Quantitative PASS criteria.** Coverage ratios, lines-per-page ratios, zero placeholder markers; subjective acceptance ("looks correct") is not permitted. | Complete · Accurate |
| 2 | **Author–approver separation.** The agent or process that authored a file may not approve it. The reviewer reads the source PDF independently and produces a structured coverage report. | Attributable |
| 3 | **AI estimates are labelled.** Any value the AI cannot programmatically confirm is labelled `(estimated)` and is excluded from the authoritative index. | Original · Accurate |
| 4 | **Human sampling review at every phase close.** A randomized sample is reconciled against the source PDF at the close of every phase, not as a post-hoc remedy. | Accurate · Available |

The four controls and their originating non-conformances are documented in full at [`.work/meta/retrospective.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/meta/retrospective.md).

The verification track is iterative. As of the date of this statement, the deep-verification audit referenced in §2 has completed 14 review rounds; each round is preserved as evidence, and any discrepancy identified in a round is fed back into the knowledge base.

## 6. Implications and boundaries

- **Independent review is supported by design.** A user may locate the source page of a stated value within seconds and verify it directly against the SDTMIG PDF. Discrepancies should be reported via [GitHub issues](https://github.com/hakupao/sdtm-pedia/issues); the audit track is open-ended and accepts external findings.
- **Use within the regulated chain of evidence.** The knowledge base may be used as a working reference for SDTM data programming, mapping review, and SDTM training. It is not itself a 21 CFR Part 11 / PMDA-grade electronic record and does not replace organizational standard operating procedures governing such records.
- **Not a substitute for the official standard.** For regulatory submissions, the authoritative reference is the corresponding CDISC publication (SDTMIG, SDTM Model, Controlled Terminology). Where this knowledge base and the official publication appear to differ, the official publication governs.

---

**Repository:** [github.com/hakupao/sdtm-pedia](https://github.com/hakupao/sdtm-pedia) · **License:** CC BY 4.0
