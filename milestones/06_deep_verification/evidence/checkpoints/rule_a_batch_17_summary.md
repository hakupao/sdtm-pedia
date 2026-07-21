# Rule A Batch 17 Audit Summary

> **Reviewer**: `vercel:ai-architect` (AUDIT-mode pivot, Rule D slot #26, 7th cumulative AUDIT-mode pivot, vercel-family 3rd burn)
> **Date**: 2026-04-26
> **Sample**: 10 atoms, 1/page p.161-p.170, type-stratified (4 TABLE_ROW + 3 HEADING + 1 CODE_LITERAL + 2 sample-design slots)
> **Seed**: 20260490
> **Source PDF**: `source/SDTMIG v3.4 (no header footer).pdf` p.161-170
> **Output**: `rule_a_batch_17_verdicts.jsonl` (10 lines) + this summary

---

## 1. Sample Design

| # | atom_id | page | sampled because... |
|---|---|---|---|
| 1 | ig34_p0161_a0022 | 161 | DS Examples L5 sib chain (R15 cross-batch, Example 6 sib=6 verify) |
| 2 | ig34_p0162_a0002 | 162 | dataset filename CODE_LITERAL (R9/NEW4 strict) |
| 3 | ig34_p0163_a0022 | 163 | TABLE_ROW te.xpt 8-cell (O-P1-26 outer-pipe + R11) |
| 4 | ig34_p0164_a0019 | 164 | TABLE_ROW dm.xpt 17-cell wide (R8 mid-empty + R11 trailing-empty) |
| 5 | ig34_p0165_a0028 | 165 | TABLE_ROW ds.xpt example main (R10 spec-table verbatim) |
| 6 | ig34_p0166_a0004 | 166 | TABLE_ROW te.xpt Row 3 (cross-batch transition zone p.166→167, NEW5) |
| 7 | ig34_p0167_a0017 | 167 | **§6.2.5 HO HEADING (NEW6/R15 critical, sib=5 cross-batch continuity)** |
| 8 | ig34_p0168_a0008 | 168 | TABLE_ROW HO spec table HOCAT row (R10 spec-table + NEW2 char-level) |
| 9 | ig34_p0169_a0012 | 169 | **HO – Examples HEADING L4 sib=4 (NEW7 deterministic L4 chain)** |
| 10 | ig34_p0170_a0010 | 170 | TABLE_ROW ho.xpt Row 6 (R8 mid-empty cell HOCAT, R11 trailing 2 empties) |

**Type strata coverage** (per 17 R-rules + 7 NEW candidates intent):
- TABLE_ROW: 5 (50%) — covers O-P1-26 / R8 / R10 / R11 / NEW2
- HEADING: 3 (30%) — covers R3 / R5 / R15 / NEW6 / NEW7
- CODE_LITERAL: 1 (10%) — covers R9 / NEW4
- TABLE_HEADER (implicit via TABLE_ROW cell counts): covered transitively
- TABLE_CAPTION (the "ds.xpt" before tables): covered via atom 2

---

## 2. Per-Atom Verdict Table

| atom_id | page | atom_type | verbatim | parent_section | heading_fields | overall |
|---|---|---|---|---|---|---|
| ig34_p0161_a0022 | 161 | PASS | PASS | PASS | PASS | **PASS** |
| ig34_p0162_a0002 | 162 | PASS | PASS | PASS | N/A | **PASS** |
| ig34_p0163_a0022 | 163 | PASS | PASS | PASS | N/A | **PASS** |
| ig34_p0164_a0019 | 164 | PASS | PASS | PASS | N/A | **PASS** |
| ig34_p0165_a0028 | 165 | PASS | PASS | PASS | N/A | **PASS** |
| ig34_p0166_a0004 | 166 | PASS | **FAIL** | PASS | N/A | **FAIL** |
| ig34_p0167_a0017 | 167 | PASS | PASS | PASS | PASS | **PASS** |
| ig34_p0168_a0008 | 168 | PASS | PASS | PASS | N/A | **PASS** |
| ig34_p0169_a0012 | 169 | PASS | PASS | PASS | PASS | **PASS** |
| ig34_p0170_a0010 | 170 | PASS | PASS | PASS | N/A | **PASS** |

Tally: **pass=9 partial=0 fail=1**
Weighted: 9.0 / 10 = **90.00%**

---

## 3. Findings

### F-B17-RA-1 — TABLE_ROW verbatim corruption on p.166 te.xpt Row 3 (HIGH severity)

**Atom**: `ig34_p0166_a0004`
**Severity**: HIGH (3 char-level errors in single row, including ISO 8601 duration corruption)
**R-rule violations**: R10 (spec-table verbatim wrap-cell preservation), NEW2 (char-level typo check)

**Discrepancies vs PDF p.166 te.xpt Row 3 ground truth**:

| Column | PDF ground truth | Atom value | Error type |
|---|---|---|---|
| ETCD | `ABC` | `ABC-` | Spurious trailing dash (likely picked up wrap-row separator) |
| TEENRL | `4 weeks after start of Element` | `3 weeks after start of Element` | Digit-character substitution (4 → 3) |
| TEDUR | `P4W` | `PAW` | Digit-letter swap (4 → A); breaks ISO 8601 duration validity |

**Root-cause hypothesis**: Wrap-row PDF text-extraction artifact at the te.xpt → TA narrative boundary on p.166 (Row 3 sits in the upper third where the te.xpt spans a wide multi-cell row). The "ABC-" trailing dash and "PAW" suggest character-position drift during PDF text reflow — the writer-family agent may have extracted from a slightly off-position OCR/text layer.

**Recommended fix — Option H repair**:
Rewrite verbatim to:
```
| 3 | DS10 | TE | ABC | Trt ABC | First dose of treatment Element, where treatment is AB +C | 4 weeks after start of Element | P4W |
```

**Recommended scope expansion (CONDITIONAL)**: Reviewer recommends main session run an Option E spot-check on the remaining 134 batch_17b atoms (writer-family) for similar wrap-row corruption patterns:
- Pattern 1: trailing-dash on short codes (e.g., `ABC` → `ABC-`)
- Pattern 2: ISO 8601 duration digit-letter swap (e.g., `P4W` → `PAW`, `P7D` → `PXD`)
- Pattern 3: digit substitution within numeric phrases (`3` ↔ `4`, `1` ↔ `7`)

If Option E spot-check (recommended N=10 of remaining 134) finds 0 additional corruptions, accept Option H single-atom fix; if ≥1 additional corruption, escalate to writer-family p.166 full-page rerun (precedent: 7 successful Option E full-page rerun precedents in P1 history).

---

## 4. R-Rule Compliance Summary

| Rule | Tested via atoms | Result |
|---|---|---|
| R1 (atom_id 4-digit format) | All 10 | PASS (all `ig34_pNNNN_aNNNN`) |
| R3 (HEADING vs LIST_ITEM TOC-anchored) | #1, #7, #9 | PASS |
| R5/NEW6 (parent_section canonical full-form) | All 10 | PASS (DS = `§6.2.4 Disposition (DS)` ✓; HO = `§6.2.5 Healthcare Encounters (HO)` ✓; §6.2.5 HEADING parent = `§6.2 [MODELS FOR EVENTS DOMAINS]` bracket form CORRECT per kickoff exception) |
| R8 (TABLE_ROW empty cell `\| \|` literal) | #4, #10 | PASS (mid-cell HOCAT empty + trailing 2 empties preserved) |
| R9/NEW4 (dataset filename CODE_LITERAL) | #2 | PASS (`ds.xpt`) |
| R10 (spec-table verbatim wrap-cell) | #5, #6, #8 | **PARTIAL — #6 FAIL** (te.xpt Row 3 char corruption); #5, #8 PASS |
| R11 (TABLE_ROW trailing empty cell preservation) | #4, #10 | PASS |
| R12 (transition page full-content discipline) | #6, #7 (p.166→167 chapter transition) | PASS (no content gap at p.167 §6.2.5 HO heading entry) |
| R13 (numbered list item discipline) | n/a in sample | not exercised |
| R14 (DONE atoms=N strict count match) | meta-level (writer self-validation) | not exercised in sample |
| R15 (cross-batch sibling continuity) | #1 (DS Examples sib=6 from batch 16 sib=4), #7 (§6.2.5 HO sib=5 from §6.2.4 DS sib=4) | PASS |
| O-P1-26 (TABLE_ROW outer-pipe convention) | #3, #4, #5, #6, #8, #10 | PASS |
| NEW2 (char-level typo check) | #6, #8 | **PARTIAL — #6 FAIL**; #8 PASS |
| NEW3 (explicit null heading_level/sibling_index) | All 10 | PASS (non-HEADING atoms have explicit `null`, not missing key) |
| NEW5 (chapter transition zone partitioning at p.167) | #6, #7 | PASS (§6.2.5 HEADING correctly placed at p.167, no DS-tail spillover into HO zone) |
| NEW6 (parent_section canonical full-form pin) | All 10 | PASS — including §6.2.5 HEADING atom whose parent §6.2 retains bracket per kickoff explicit exception |
| NEW7 (L4 sub-section sib chain deterministic) | #9 | PASS (HO – Examples sib=4 = Description=1/Specification=2/Assumptions=3/Examples=4 canonical order) |

---

## 5. Spot-Check Observations (outside the 10-atom sample)

**Observation 1 — HO domain spec table appears clean (sample atom #8 PASS)**:
The HOCAT row sample passed cleanly with all 7 cells matching PDF p.168 verbatim (incl. `*` Controlled Terms marker, `Perm` Core). This is encouraging signal that the writer-family extraction of the HO spec table (covering p.167-169 with 28 variables) is likely high-quality. However, the F-B17-RA-1 finding on a different table (te.xpt) means the failure mode is table-specific, not domain-wide.

**Observation 2 — §6.2.5 HO HEADING atom is the most critical NEW6 test in this batch**:
The parent_section convention is intentionally split:
- **§6.2.5 HEADING itself**: parent = `§6.2 [MODELS FOR EVENTS DOMAINS]` (bracket — the §6.2 chapter parent form established in earlier batches)
- **All atoms WITHIN §6.2.5**: parent = `§6.2.5 Healthcare Encounters (HO)` (full-form per NEW6)

Sample atoms #7, #8, #9, #10 collectively verify both halves of this convention. ✓

**Observation 3 — NEW7 L4 deterministic chain works at HO domain**:
Sample atom #9 confirms `HO – Examples sib=4` follows the canonical Description=1 / Specification=2 / Assumptions=3 / Examples=4 order, NOT mid-page emergence. This validates the post-batch-16 NEW7 prompt patch is holding.

**Observation 4 — Cross-batch sib continuity (R15) is solid in this sample**:
Both R15 critical atoms PASS:
- DS-Examples Example 6 sib=6 (continues batch 16's sib=4)
- §6.2.5 HO sib=5 (continues §6.2.4 DS sib=4)

No off-by-one or sib-restart errors observed.

**Observation 5 — No NEW3 violations** (all non-HEADING atoms have explicit `null` for heading_level/sibling_index, not missing keys). Schema discipline holding.

---

## 6. v1.3 Prompt Patch Candidates (NEW8+)

### NEW8 candidate — Wrap-row character-position drift guard (P0_writer_pdf v1.3)

**Trigger**: F-B17-RA-1 surfaced 3 char-level errors in te.xpt Row 3 of a single TABLE_ROW atom — the failure pattern (trailing dash + digit-letter swap + digit substitution) suggests PDF text-extraction position drift on wide wrap-cell rows.

**Proposed v1.3 prompt patch language** (add to writer_pdf prompt under "Spec/example table extraction discipline"):

> **WRAP-ROW POSITION VERIFICATION**: For any TABLE_ROW where the row spans visually-multiple lines in PDF (wrap row), perform a 3-point char-level cross-check before emitting the verbatim:
> 1. **Short-code suffix check**: Variable codes (≤4 chars) must NOT end in `-` (dash) unless explicitly part of code spec — flag `ABC-`, `XYZ-` patterns as suspect.
> 2. **ISO 8601 duration validity**: Any TEDUR/--DUR cell starting with `P` MUST follow `P[n]Y/M/W/D/T...` format with digits (0-9) only between `P` and unit letters (Y/M/W/D/H/S). Flag `PAW`, `PXD` patterns (digit-position substituted by letter).
> 3. **Numeric phrase consistency**: For phrases like "N weeks after start of Element" / "N week(s)", the digit N must match the row's TEDUR ISO 8601 value (e.g., `4 weeks` ↔ `P4W`; `1 week` ↔ `P7D` or similar). Flag mismatches.

**Evidence threshold**: Single-occurrence so far (F-B17-RA-1 only). NEW8 should be tracked as **CANDIDATE** in `v1.3_patch_candidates.md` with severity `LOW-but-clearly-correct`. Recommend escalation to v1.3 cut session if Option E spot-check on batch_17b finds ≥1 additional matching pattern.

### NEW9 candidate — Cross-context parent_section override for "supporting dataset" rows (DEFERRED)

**Trigger**: Atoms #3 (te.xpt) and #4 (dm.xpt) on p.163-164 are TABLE_ROW atoms from supporting datasets (TE/DM/EX/SE) under a DS Example, with parent_section=`§6.2.4 Disposition (DS)`. This is contextually correct (the rows belong to DS Example 10's supporting-dataset narrative), but a future v1.3 prompt could optionally add an `examples_supporting_dataset_origin` field to make the cross-domain origin explicit (e.g., `te.xpt`, `dm.xpt`) for downstream RAG/KG consumers.

**Severity**: LOW (current behavior is correct; this is a metadata-richness improvement, not a correctness fix). DEFERRED — do not block v1.3 cut on this.

---

## 7. Final Verdict

```
RULE_A_DONE pass=9 partial=0 fail=1 weighted=9.00
```

**Threshold policy** (per kickoff Step 5):
- Weighted ≥90% → **PASS** ✓
- Weighted 9.00 / 10 = **90.00%** = exactly at threshold → **PASS**

**Verdict**: **PASS** (at threshold, single FAIL is HIGH-severity but isolated to one atom; root cause is char-level PDF wrap-row extraction drift, not a systemic R-rule misapplication; no NEW6/NEW7/R15 critical-target failures; no schema/structure violations; no parent_section convention violations).

**Recommended next action for main session** (post-Rule-A):
1. Apply Option H repair to atom `ig34_p0166_a0004` (single-atom verbatim rewrite per F-B17-RA-1 fix recommendation).
2. **CONDITIONAL** Option E spot-check N=10 of remaining 134 batch_17b atoms for wrap-row corruption patterns (NEW8 trigger condition).
3. Log NEW8 candidate to `v1.3_patch_candidates.md` with severity LOW + evidence pointer to F-B17-RA-1 (do not block v1.3 cut on a single occurrence).
4. Mark batch 17 as `RULE_A_PASS_AT_THRESHOLD_WITH_1_OPTION_H` for reconciler intake.

---

## Appendix A — Reviewer self-disclosure (Rule D compliance)

- **Reviewer subagent_type**: `vercel:ai-architect` (slot #26 in cumulative Rule D pool, 7th AUDIT-mode pivot)
- **Pivot rationale**: AI-architecture domain expert pivoted to AUDIT-mode for PDF atomization quality audit (analogous role to `pr-review-toolkit:code-reviewer` / `feature-dev:code-reviewer`); zero AI-architecture / AI-SDK / Vercel-platform content emitted; pure JSONL atom record audit against PDF ground truth + 17 R-rules + 7 NEW candidates.
- **No collision**: Round 1 #22-#24 (deployment-expert, qa-tester, executor variants) + batch 16 #25 (workflow-architect) all distinct from #26 ai-architect.
- **Rule A satisfied**: Independent sample audit performed, 10 atoms verified against PDF, 4-dim verdicts emitted, summary written. Writer (executor + writer agents) and Reviewer (vercel:ai-architect) are different subagent_types per Rule D writer/reviewer isolation.
- **Rule B satisfied**: No failure attempts to archive (Rule A audit is read-only verification; the 1 FAIL atom is a finding for Option H repair, not a reviewer failure).
- **Rule C deferred**: Retro is project-level (P1 deep verification), not per-batch — handled by reconciler/wrap-up session.
- **Rule D satisfied**: Writer/Reviewer isolation maintained; #26 ai-architect distinct from all 25 prior burns.
- **No touched files outside output scope**: Did NOT modify root pdf_atoms.jsonl / audit_matrix.md / _progress.json / sister batch files / CLAUDE.md / project meta.
- **No git commit / push**: Confirmed.
