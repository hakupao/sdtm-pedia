---
lang: en
slug: known-limitations
order: 50
title: "Known Limitations"
---

# Known Limitations

This page explains the boundaries of v1.2. These are not simply defects; they help users decide which questions are suitable for direct lookup and which require official-source or internal-process confirmation.

## 0. v1.2 Audit Scope (updated 2026-05-19)

v1.2 is a Gemini-only system prompt refresh of v1.1 (v7.1 → v8.1, 422 → 525 lines). The knowledge base, all four upload bundles, all metadata documents, and Claude / ChatGPT / NotebookLM prompts inherit byte-identical from v1.1.

### What was verified in v1.2

- **SMOKE_V4 R3 (2026-05-19)** — full 4-platform × 17-question regression test on the v1.1 deployments. Results: Claude 17/17, ChatGPT 17/17, NotebookLM 15.5/17 (Q9 PUNT and Q11 PARTIAL are RAG architectural limits), **Gemini v7.1: 13/17 with four FAIL** (Q3 BE/BS/RELSPEC off-topic to AE; Q4 Scenario A routed to LB instead of IS; Q11 Dataset-JSON off-topic to AE/CM; AHP1 LBCLINSIG off-topic to CM/MH). Independent reviewer (`oh-my-claudecode:scientist`, Rule D #15) confirmed 68/68 cells.
- **Gemini v8.1 dry-run on the four R3 failures (2026-05-19 16:35-16:40 PM)** — all four now PASS on Gemini 3.1 Pro (same model as R3 baseline). Q3/Q4/Q11/AHP1 verified by Rule D #17 reviewer (`oh-my-claudecode:verifier`) APPROVE 0 blockers.
- **Rule A coverage extended** — Rule A semantic spot-check of v1.1 had used N=5 KB files (deferred from v1.1 audit). The post-v1.1 audit pass (2026-05-16) raised this to **N=20 KB files × 4 platforms = 124 grep probes, 100% PASS**.

### Areas not re-evaluated in v1.2 (deferred to v1.2 post-cut)

- **R4 17-question full regression on Gemini v8.1** — Only the four v7.1 FAIL questions were re-tested. The 13 v7.1 PASS questions on Gemini were not tested under v8.1; the CO-5 default-reflection regex and candidate-count cap are not yet independently validated on multi-variable questions. Risk: low (the v8.1 changes are anchor extensions that do not modify the core rules for those PASS questions), but full confirmation requires R4.
- **M2 candidate-count cap independent validation** — The four-question dry-run had fewer than five SDTM-shaped candidates per question, so the cap's threshold was not exercised. Planned for R4.
- **BECAT EXTRACTION KB-prompt note** — v8.1 prompt L272 lists `"EXTRACTION"` among BECAT examples; KB BE / spec L111 only inlines three canonical examples (`COLLECTION`, `PREPARATION`, `TRANSPORT`). The deployed response correctly annotates it as sponsor-extensible, but a future prompt revision may add an explicit source citation to avoid prompt-KB drift.
- **Gemini's `04_business_scenarios_and_cross_domain.md`** — writer-authored, unchanged in v1.2 and audited in the 2026-05-16 post-v1.1 audit pass; no further action required.
- **437 `UNSOURCED_MANUAL` atoms from 06 P5** — still unclassified. Does not affect deployed answers but represents KB content whose source-of-truth lineage is unverified.
- **166 KB sections Tier B deferred** — 56 with missing sibling nodes, 110 with truncated content. The 06 deep verification pass reached its 99.02% coverage gate with Tier A (HIGH-priority) repairs only. Answers in these sections may be less complete than other areas. Tier B repair is planned for a future KB pass.

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
