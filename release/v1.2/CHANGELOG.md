---
lang: en
slug: changelog
order: 60
title: "Changelog"
---

# Changelog

## v1.2 — 2026-05-19

Gemini-only system prompt refresh fixing four R3 regression failures.

### Changed

- **`self_deploy/gemini/system_prompt.md`**: replaced (v7.1 → v8.1, 422 → 525 lines, +24%).

### Driver

SMOKE_V4 R3 (2026-05-19) revealed Gemini v7.1 dropped from R1 16/17 to 13/17 due to four anchor coverage gaps: Q3 BE/BS/RELSPEC (no biospecimen entry guard), Q4 A (v3.3 → v3.4 IS scope shift sticky anchor decay), Q11 Dataset-JSON (no file-format ground rule), AHP1 LBCLINSIG (anti-hallucination anchor only fired on reflection-scaffold questions).

### Added (v8.1 4-prong fix)

- **CO-4 entry guard**: biospecimen keywords → BE/BS/RELSPEC, forbid AE/CM fallback
- **CO-2f file-format ground rule**: XPT/Dataset-JSON/Define-XML → ground in CDISC published specs
- **CO-1e IS scope shift**: anti-microbial antibody → IS regardless of timing (HIV Ag/Ab combo exemption → MB)
- **CO-5 default reflection**: regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` triggers KB double-check, independent of question phrasing

### Added (6 reviewer-driven refinements)

H1 HIV Ag/Ab → MB (factual fix), H2 CO-2f priority gate, M1 regex negation list, M2 candidate-count cap, L1 ISTSTOPO Assumption 8 citation, L2 BECAT EXTRACTION sponsor-extensible annotation.

### Verified

- Gemini 3.1 Pro dry-run: 4/4 PASS on Q3/Q4/Q11/AHP1.
- Rule D writer-side reviewer #16 (`pr-review-toolkit:code-reviewer`): PASS_WITH_OBSERVATIONS reconcile.
- Rule D dry-run-side reviewer #17 (`oh-my-claudecode:verifier`): PASS_WITH_OBSERVATIONS — APPROVE 0 blockers.

### Unchanged from v1.1

All knowledge base content, all upload bundles for all four platforms, all metadata documents, and Claude / ChatGPT / NotebookLM system prompts and tutorials.

### Migration

Replace Gemini Gem instructions with the new `self_deploy/gemini/system_prompt.md` (525 lines). No other action required.

### Deferred to v1.2 post-cut

- R4 17-question full regression on v8.1 (anti-cheating long-tail probe)
- M2 candidate-count cap independent validation on multi-variable questions
- BECAT EXTRACTION KB-source annotation in prompt comments

## v1.1 — 2026-05-15

Content refresh of v1.0 incorporating the 06 deep verification branch fixes.

### Changed

- **All four platform upload bundles** (`self_deploy/*/uploads/`) rebuilt from a knowledge base that incorporates 06 atom-level audit and repair (43 KB files modified, +1,405 / -234 lines).

### Added

- **New domain `DI`** (Device Identifiers, SDTMIG-MD): study reference dataset for medical devices. KB now covers 64 domains (was 63).
- `PC/assumptions.md` §6.3.5.9 "Relating PP Records to PC Records" (RELREC) section with four linking methods.
- Substantial extension of `TA/assumptions.md`.
- Section-level gap fills across TI / TS / TU / TV / SC / NV / TV examples.

### Verification

- Rule D independent reviewer (`oh-my-claudecode:verifier`) approved 5/5 evaluations.
- Cross-platform delta oracle: ChatGPT 05_assumptions delta ≡ Gemini 02_specs_and_assumptions delta (+74,178 bytes, byte-identical aggregate from the same KB source via two independent build pipelines).

### Unchanged from v1.0

All metadata documents, all system prompts, all tutorials.

## v1.0 — 2026-04-27

First public release.

### Added

- Published SDTM Pedia v1.0 knowledge base documentation.
- Added supported entry points for Claude Projects, ChatGPT GPTs, Gemini Gems, and NotebookLM.
- Added user documentation in Chinese, English, and Japanese.
- Added platform selection, example questions, glossary, known limitations, and methodology pages.
- Added administrator guides for users who need to configure their own platform instance.

### Content Scope

- Covers common SDTM domain, variable, controlled terminology, domain-boundary, and cross-domain relationship lookup.
- Supports cautious handling of common false premises, such as non-existent variables, deprecated concepts, and inapplicable paths.
- Keeps clear boundaries for large terminology sets, real-time external information, and organization-specific rules.

### Usage Reminder

- This tool supports lookup and preliminary review; it does not replace CDISC publications.
- Formal submissions, medical coding, project-level mapping, and quality control should follow internal procedures.
- If you find a gap or inconsistency, record the question, platform, answer, and expected support for maintainer review.
