---
lang: en
slug: known-limitations
order: 50
title: "Known Limitations"
---

# Known Limitations

This page explains the boundaries of v1.1. These are not simply defects; they help users decide which questions are suitable for direct lookup and which require official-source or internal-process confirmation.

## 0. v1.1 Audit Scope (added 2026-05-15)

v1.1 rebuilds platform upload bundles from a KB that incorporates the 06 deep verification fixes (43 KB files refined, +1,405 / -234 lines; DI domain added). The rebuild was verified by an independent Rule D reviewer (5/5 evaluations PASS, including a Rule A semantic spot-check of 5 KB files × 4 platforms = 20 grep hits, zero miss). Areas **not re-evaluated** in v1.1 (deferred to v1.2):

- SMOKE_V4 has not been re-run against the v1.1 deployments; baseline scores from v1.0 (Claude 17/17, ChatGPT 16.5/17, Gemini 16/17 R2, NotebookLM 15/17) are presumed unchanged but not confirmed under v1.1 content.
- Rule A spot-check used N=5 KB files (not N=20+); per-bucket semantic audit was not performed on all 22 changed NotebookLM buckets.
- Gemini's `04_business_scenarios_and_cross_domain.md` is writer-authored (not KB-derived) and was not re-audited against the new PC §6.3.5.9 RELREC content.
- The 437 `UNSOURCED_MANUAL` atoms from 06 P5 remain unclassified (06 RETROSPECTIVE § 二.4); they do not affect deployed answers but represent KB content whose source-of-truth lineage is unverified.
- Approximately **166 KB sections (56 with missing sibling nodes, 110 with truncated content)** were not fully repaired in the 06 deep verification pass. The project reached its coverage gate (99.02%) with Tier A (HIGH-priority) repairs only; Tier B (MEDIUM-priority) was deferred. Answers in these sections may be less complete than other areas. The affected sections are scattered across deep-chapter content rather than concentrated in any single domain. Tier B repair is planned for a future KB pass.

## 1. Not a Replacement for Official Standards

SDTM Pedia is a reference aid. Regulatory submission decisions, standards interpretation, terminology version confirmation, and critical mapping decisions should use CDISC publications, NCI EVS, licensed MedDRA resources, regulatory requirements, and internal SOPs.

## 2. Real-Time External Updates Are Not Guaranteed

This release reflects the knowledge scope prepared at release time. For later changes, such as new CDISC versions, Pinnacle 21 rule updates, Dataset-JSON status, or external database changes, check the relevant official source.

## 3. Long-Tail Terminology May Require Official Lookup

Some very large codelists and long-tail questionnaire terminology are not fully expanded on every platform. A good answer should state the boundary and point you back to NCI EVS or another authoritative source rather than generating an unverified full term list.

## 4. Platform Answer Styles Differ

Claude, ChatGPT, Gemini, and NotebookLM differ in style, citation display, and conservatism. NotebookLM tends to stay closest to the uploaded source set; other platforms may be better for explanation and synthesis, but still require human judgment.

## 5. Internal Organization Rules Are Not Covered

Sponsors, CROs, and data standards teams may have internal mapping conventions, Define-XML practices, Reviewers Guide wording, and quality workflows. SDTM Pedia can help with standards lookup, but it does not replace those conventions.

## 6. High-Risk Scenarios Require Human Review

Use human review for:

- Decisions affecting formal submission structure or variable mapping.
- Medical coding, serious adverse events, death, discontinuation, or other critical clinical concepts.
- Project-specific CRFs, SAPs, data management plans, or sponsor standards.
- Answers without clear support, or answers that conflict with team standards.

If you find an apparent error or gap, record the question, platform, answer, and expected source so maintainers can review it.
