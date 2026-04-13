# Phase 3 Validation Scripts Implementation Plan

## Goal

Add three reusable validation scripts for Phase 3 outputs:

1. inventory validator
2. assumptions structural audit
3. examples structural/signature audit

The scripts should produce repeatable Markdown reports and lightweight machine-readable summaries so later re-runs are cheap.

---

## Scope

### Script 1: `audit_phase3_inventory.py`

Purpose:

- verify every domain in `.work/page_index.json` has both:
  - `assumptions.md`
  - `examples.md`
- detect empty or suspiciously tiny files
- verify shared-example pairs are all present

Inputs:

- `.work/page_index.json`
- `knowledge_base/domains/*`

Outputs:

- `.codex/reports/phase3-inventory-validation.md`
- summary counts + error/warning lists

Core checks:

- domain coverage
- file existence
- empty file detection
- configurable minimum-size warning
- shared pair presence (`EX/EC`, `MB/MS`, `PC/PP`, `TU/TR`)

---

### Script 2: `audit_assumptions_pdf_vs_md.py`

Purpose:

- compare assumptions PDF ranges vs markdown outputs at the structural level

Inputs:

- `.work/page_index.json`
- `source/SDTMIG v3.4 (no header footer).pdf`
- `knowledge_base/domains/*/assumptions.md`

Outputs:

- `.codex/reports/phase3-assumptions-validation.md`
- per-domain metrics and flagged mismatches

Comparison strategy:

- use `pdftotext` page extraction
- normalize PDF / Markdown text
- compare:
  - numbered-item count
  - nested-item signals
  - anchor-token recall
  - similarity score

High-signal anchor extraction:

- domain code
- variable-like tokens
- uppercase SDTM terms
- numbered heading/paragraph markers

Key principle:

- do not attempt brittle exact-text comparison
- detect likely omissions and hierarchy loss

---

### Script 3: `audit_examples_pdf_vs_md.py`

Purpose:

- compare example structure from PDF vs markdown output

Inputs:

- `.work/page_index.json`
- `source/SDTMIG v3.4 (no header footer).pdf`
- `knowledge_base/domains/*/examples.md`

Outputs:

- `.codex/reports/phase3-examples-validation.md`
- per-domain signatures and mismatch summaries

Comparison strategy:

- use `pdftotext -layout`
- parse Markdown into:
  - example headings
  - dataset block names
  - markdown table headers
  - row counts
  - key token signatures
- compare against normalized PDF text using signatures

Key checks:

- example count
- dataset name presence
- table header presence
- row count heuristics
- key value recall
- shared-example note presence

---

## Implementation Order

1. add tests for pure parsing/comparison helpers first
2. implement inventory script first (lowest risk, gives immediate signal)
3. implement assumptions audit second
4. implement examples audit third
5. run tests
6. run scripts to generate first reports

---

## Test Strategy

Extend `.codex/tests/test_validation_scripts.py` with:

- inventory coverage / missing-file tests
- assumptions normalization + numbering extraction tests
- assumptions anchor recall / similarity tests
- examples heading extraction tests
- examples dataset/table parsing tests
- examples signature comparison tests

Prefer unit tests for helper functions over full PDF integration tests.

---

## Non-Goals (first version)

- perfect OCR-safe PDF semantic reconstruction
- full table cell-by-cell equality against PDF
- automatic content repair

The first version is a risk detector, not a fully lossless proof engine.

---

## Acceptance Criteria

- all three scripts exist in `.codex/scripts/`
- unit tests cover their core parsing/comparison logic
- scripts run locally against current repo layout
- reports are emitted under `.codex/reports/`
- outputs are useful enough to identify which domains need manual review
