---
lang: en
slug: known-limitations
order: 50
title: "Known Limitations"
---

# Known Limitations

This page explains the boundaries of v1.0. These are not simply defects; they help users decide which questions are suitable for direct lookup and which require official-source or internal-process confirmation.

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
