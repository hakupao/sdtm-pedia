# Phase 3 Accuracy Validation Plan

## Context

After reviewing:

- `.codex/`
- `.work/worklog.md`
- current `knowledge_base/domains/*`

the current best understanding is:

- Phase 3 worklog says extraction is complete
- actual filesystem now also shows `63/63` domains all contain:
  - `spec.md`
  - `assumptions.md`
  - `examples.md`
- some `.codex` context files are stale and still describe an earlier incomplete snapshot

Therefore, Phase 3 review must separate:

1. **content accuracy**
2. **status-document accuracy**

---

## Goal

Validate whether Phase 3 (`PDF -> assumptions.md + examples.md`) has any meaningful precision loss.

Precision loss includes:

- missing assumptions sections or numbered items
- missing examples
- missing dataset blocks
- missing table columns / rows
- altered variable names / code values / dates / numbers
- broken hierarchy
- weakened or lost shared-example relationships

---

## Immediate Baseline Fix

Before formal validation, update stale status documents so future reports align with reality:

- `.codex/project-context.md`
- `.codex/reports/latest-validation-summary.md`

Reason:

- current Phase 3 actual output is complete
- but those files still reflect an older partial state

---

## Validation Layers

### 1. Inventory Audit

Purpose:

- confirm all expected Phase 3 outputs exist
- confirm file completeness matches `page_index.json`

Checks:

- every domain in `.work/page_index.json` has:
  - `knowledge_base/domains/<domain>/assumptions.md`
  - `knowledge_base/domains/<domain>/examples.md`
- no empty files
- no obviously abnormal tiny files
- shared-example domain pairs are all present:
  - `EX/EC`
  - `MB/MS`
  - `PC/PP`
  - `TU/TR`

Suggested script:

- `.codex/scripts/audit_phase3_inventory.py`

Suggested report:

- `.codex/reports/phase3-inventory-validation.md`

Pass condition:

- `63/63` domains complete
- no empty outputs
- no missing shared-example partner files

---

### 2. Assumptions Structural Audit

Purpose:

- verify assumptions prose did not lose structure or key content

Why this matters:

- assumptions content comes from PDF
- risks are mainly omitted bullets, collapsed hierarchy, or lost constraints

Suggested script:

- `.codex/scripts/audit_assumptions_pdf_vs_md.py`

Method:

1. use `.work/page_index.json` to locate assumptions page ranges
2. extract PDF text with `pdftotext`
3. normalize both PDF text and Markdown:
   - strip layout noise
   - normalize whitespace
   - normalize quotes/dashes
4. compare structural signals instead of raw text:
   - count top-level numbered items
   - detect nested sub-items
   - compare anchor sentences / anchor tokens
   - compare key terminology presence

Suggested output fields:

- `missing_sections`
- `numbering_mismatches`
- `missing_anchor_tokens`
- `low_similarity_domains`

High-risk domains for priority review:

- `DM`
- `AE`
- `DS`
- `CP`
- `RS`
- `FA`
- `TA`
- `TE`
- `TS`
- `TU`

Pass condition:

- no unresolved P0/P1 omissions
- no major hierarchy-loss cases

---

### 3. Examples Data Audit

Purpose:

- verify examples content retained example counts, dataset blocks, table structure, and key values

Suggested script:

- `.codex/scripts/audit_examples_pdf_vs_md.py`

Method:

1. extract example page ranges using `pdftotext -layout`
2. parse markdown examples into structured blocks:
   - example titles
   - dataset block names (`dm.xpt`, `ex.xpt`, etc.)
   - table headers
   - row counts
   - high-signal tokens
3. compare using signatures rather than fragile literal text matches

Signature dimensions:

- `example_count`
- `dataset_names`
- `column_names`
- `row_count`
- `key_values`

Recommended key values to track:

- variable names
- dates / datetimes
- coded values
- drug names / clinical terms
- linking keys such as:
  - `RELID`
  - `IDVAR`
  - `IDVARVAL`
  - `TRLNKID`

High-risk domains for priority review:

- `DM`
- `DS`
- `EX`
- `EC`
- `MB`
- `MS`
- `PC`
- `PP`
- `RS`
- `FA`
- `TU`
- `TR`

Pass condition:

- no missing example
- no missing dataset block
- no column-loss / row-loss / key-value distortion left unresolved

---

### 4. Manual Review Lane

Purpose:

- manually close only the suspicious cases surfaced by automation

Manual priority scenarios:

- wide tables
- cross-page tables
- CRF mockup content
- deeply nested assumptions
- shared examples
- multi-domain linked examples

Suggested findings log:

- `.work/findings.md`

Suggested fields per finding:

- domain
- file
- page range
- suspicion type
- confirmed issue? (`yes/no`)
- fix status
- disposition (`fixed` / `acceptable difference`)

---

## Severity Model

### P0 — Must Fix

- missing example
- missing dataset block
- missing assumptions section
- broken shared-example relationship

### P1 — Should Fix

- missing columns
- row-count mismatch
- changed date / variable / code value
- hierarchy collapse that changes meaning

### P2 — Acceptable Differences

- formatting-only markdown changes
- whitespace / line-wrap differences
- wording changes that preserve meaning

---

## Recommended Execution Order

### Round 1 — Fast automated screening

1. update stale `.codex` status files
2. run Phase 3 inventory audit
3. run assumptions structural audit
4. run examples signature audit

### Round 2 — Focused human review

- inspect only flagged domains / files

### Round 3 — Final summary

Produce:

- `.codex/reports/phase3-assumptions-validation.md`
- `.codex/reports/phase3-examples-validation.md`
- `.codex/reports/phase3-validation-summary.md`

---

## Definition of Done

Phase 3 can be considered accuracy-validated only when:

- all `63` domains have `assumptions.md` and `examples.md`
- assumptions audit has no unresolved P0/P1 issues
- examples audit has no unresolved P0/P1 issues
- all high-risk shared-example domains are manually reviewed
- every issue has a recorded disposition

---

## Recommended Next Step

Do **not** move on to Phase 4 first.

Instead, build the minimum validation toolchain for Phase 3:

1. `audit_phase3_inventory.py`
2. `audit_assumptions_pdf_vs_md.py`
3. `audit_examples_pdf_vs_md.py`

This creates a reusable quality gate for current outputs and later maintenance.
