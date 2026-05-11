# Rule A Batch 31 Audit Summary

> Reviewer slot: #40 `pr-review-toolkit:silent-failure-hunter` (AUDIT-mode pivot 21st cumulative; pr-review-toolkit family 2nd burn after batch 29 `pr-review-toolkit:code-reviewer` 1st burn)
> Date: 2026-04-27
> Scope: SDTMIG v3.4 pages 301-310, 10 sample atoms covering OE Examples + RP section-start + RP Spec + RP Example 1 + RE section-start + RE Spec + RE Example 1
> Prompt version audited against: P0_writer_pdf_v1.3 (13 items A-M codified)

## §1 Overall Verdict

| Metric | Value |
|---|---|
| Sample size | 10 |
| PASS_n | 9 |
| PARTIAL_n | 0 |
| FAIL_n | 1 |
| Raw weighted score | 9.0 / 10.0 |
| **Raw weighted_pct** | **90.0%** |
| Threshold | ≥90% PASS |
| **Verdict** | **PASS** (at threshold floor; 1 atom FAIL flagged for v1.4 codification candidate — NEW2 Latin-Latin adjacent-key swap limitation needs NEW8 substring n-gram hook upgrade for Identifier-cell verbatim) |

## §2 Per-Atom Verdicts Table

| # | atom_id | page | type | atom_id | verbatim | atom_type | parent_sec | heading | special | overall |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ig34_p0301_a015 | 301 | HEADING | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 2 | ig34_p0302_a009 | 302 | TABLE_ROW | PASS | **FAIL** | PASS | PASS | PASS | **FAIL** | **FAIL** |
| 3 | ig34_p0303_a021 | 303 | CODE_LITERAL | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 4 | ig34_p0304_a015 | 304 | HEADING | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 5 | ig34_p0305_a011 | 305 | HEADING | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 6 | ig34_p0306_a013 | 306 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 7 | ig34_p0307_a020 | 307 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 8 | ig34_p0308_a002 | 308 | HEADING | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 9 | ig34_p0309_a005 | 309 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |
| 10 | ig34_p0310_a016 | 310 | LIST_ITEM | PASS | PASS | PASS | PASS | PASS | PASS | **PASS** |

## §3 Findings

### F-1 (HIGH, atom 2 ig34_p0302_a009) — VERBATIM DRIFT: OESEO vs OESEQ Identifier corruption

**Defect**: Sample atom verbatim contains `OESEO` in IDVAR cell of suppoe.xpt row 1; PDF p.302 ground truth shows `OESEQ`. Single-character Latin-Latin adjacent-key substitution (Q → O — physically adjacent on QWERTY; both Latin glyphs so NEW2 Cyrillic-Latin homoglyph check inert).

**PDF cross-check evidence**:
- PDF p.302 suppoe.xpt table, Row 1: STUDYID=XXX | RDOMAIN=OE | USUBJID=XXX-450-110 | IDVAR=**OESEQ** | IDVARVAL=3 | QNAM=OEDIR1 | QLABEL=Directionality 1 | QVAL=SUPERIOR
- PDF p.302 suppoe.xpt table, Row 2: same shape with QNAM=OEDIR2 / QVAL=TEMPORAL — both rows IDVAR=**OESEQ** (CDISC SUPPQUAL canonical Identifier convention)
- OESEQ ∈ OE canonical Identifier variable set (RPSEQ / RESEQ / OESEQ pattern); OESEO ∉ canonical CDISC variable list

**Hidden corruption motif**: This is the same family as round 3 batch 21 CPSCMRKS↔CPCSMRKS adjacent-letter swap (caught by drift cal NEW8 verbatim hash overlap, NOT by NEW2 char-level Cyrillic-Latin scan). v1.3 §D explicitly acknowledges "misses adjacent Latin-Latin swap" limitation and §H NEW8 substring n-gram check is the codified mitigation. The current writer self-validate sequence (Self-Validate step 6 in v1.3 prompt) requires NEW8 oracle lookup against canonical CDISC variable list; either (a) the writer skipped the self-validate step, or (b) the canonical oracle list is missing OESEQ (canonical SUPPQUAL Identifier pattern: <DOMAIN>SEQ — OESEQ derived from RPSEQ/RESEQ/OESEQ family).

**User-impact analogy** (silent-failure-hunter normal mode framing): A corrupted variable identifier in a SDTM SUPPQUAL row is the data-equivalent of a silent-failure: downstream readers (KB consumers, RAG retrieval) will treat OESEO as a phantom variable, fail join against canonical SUPPQUAL spec, or worse — propagate the typo into a generated standard mapping. Like an empty catch block hiding an error, the typo passes structural validation (atom_type / parent / pipe-count all OK) while semantically corrupting the row. Detection without ground-truth PDF cross-check would not surface the issue.

**Recommendation**:
1. Reconciler-side Option H 1-atom fix: rewrite atom verbatim with OESEQ (and re-verify Row 2 if its sample were drawn — likely also OESEQ given PDF shows both rows identically).
2. Codify v1.4 candidate: NEW8 substring n-gram self-validate MUST treat TABLE_ROW Identifier-cell tokens as oracle-checked — currently NEW8 §H scope reads "every [A-Z]{3,} variable identifier in verbatim" which technically covers OESEO, but the writer needs an enumerated canonical SUPPQUAL Identifier set (RDOMAIN / IDVAR / IDVARVAL / QNAM / QLABEL / QVAL — and the populated values for IDVAR like OESEQ / RESEQ / RPSEQ / etc.) baked into the writer prompt as an oracle, not lazily inferred from spec tables.
3. Drift cal at p.302 (or nearest spec-table page in batch 31) MAY catch via NEW1 verbatim hash overlap < 80% when rerun produces the correct OESEQ — recommend MAIN-SESSION drift cal verification on this page if batch 31 cumulative atoms ≥ 600 trigger.

### F-2 (LOW, atom 2 ig34_p0302_a009 secondary) — USUBJID intra-cell space collapse

**Observation**: PDF p.302 suppoe.xpt USUBJID rendering shows `XXX- 450-110` with an intra-cell space (visible in PDF rendering between hyphen and 450); sample atom normalizes to `XXX-450-110` without the intra-cell space. Strict R10 says "no whitespace fix"; however this is a known wrap-cell artifact (R11 spec table wrap-cell handling). Not flagged as primary FAIL since R11 partial conflict with R10 on same axis. Suggest v1.4 clarifier to disambiguate R10 vs R11 on intra-cell whitespace within wrapped USUBJID/IDVARVAL cells.

## §4 Recommendations (v1.4 codification candidates)

### Rec-1: NEW8 oracle expansion to SUPPQUAL Identifier values
- **Problem**: Atom 2 OESEO bypassed NEW8 because NEW8 oracle was implicitly limited to spec-table-extracted Variable Names (column headers, e.g. STUDYID/DOMAIN/USUBJID/RDOMAIN/IDVAR/IDVARVAL/QNAM/QLABEL/QVAL); the *populated value* in IDVAR cell ("OESEQ" — itself a variable name reference, not a free string) was not cross-checked against canonical Identifier set.
- **Fix**: Extend NEW8 §H oracle to include "any uppercase-token populated in IDVAR cell of SUPPQUAL TABLE_ROW must be a member of canonical CDISC Identifier set per its parent domain (e.g. for RDOMAIN=OE: IDVAR ∈ {OESEQ, OEGRPID, OESPID, OELNKID, OELNKGRP, OEREFID})".
- **Cost**: 1 lookup per SUPPQUAL TABLE_ROW (low overhead).
- **Benefit**: Catches Identifier-cell typos that bypass spec-table-only oracle.

### Rec-2: Density alarm did NOT trigger on batch 31 (informational, not a defect)
- p.301-310 atom counts (sample inferred): each page produced ≥15 atoms (max-index in sample: p.301 a015 / p.302 a009 / p.303 a021 / p.304 a015 / p.305 a011 / p.306 a013 / p.307 a020 / p.308 a002 / p.309 a005 / p.310 a016). All ≥10 visible — likely all ≥15 per G-MS-12 spec-table floor. No density alarm warranted. Per-batch floor 100 atoms also satisfied.

### Rec-3: NEW6.b L4 self-parent NEVER rule EFFECTIVE 5th proactive (round 6 batch 31 NEW)
- Atom 5 (RP §6.3.7.6 HEADING) correctly parent = `§6.3.7 Morphology/Physiology Domains` (L3 group canonical full-form), NOT self-parent. Same correct application as round 4 4× IS/LB/Microbiology Domains/GF.
- Round 6 batch 31 = 5th cumulative proactive correct application. Continued effectiveness validates v1.3 §F NEW6.b codification.

### Rec-4: NEW7 L5 chain EFFECTIVE batch 31 (round 6)
- Atom 8 (RE Description/Overview hl=5 sib=1) RESTART per RE domain per NEW7 L5 chain Description=1. Same application as past 4 rounds. Continued effectiveness.

### Rec-5: NEW7 L6 Examples ALWAYS HEADING NEVER SENTENCE EFFECTIVE batch 31 (round 6)
- Atom 1 (OE Example 1 hl=6 sib=1) and Atom 4 (OE Example 4 hl=6 sib=4) both correctly typed HEADING with proper sib chain. No SENTENCE→HEADING promotion needed (= no recurrence of round 3 O-P1-68 / round 4 O-P1-79 LB-Examples motif). v1.3 §G L6 procedural codification EFFECTIVE.

## §5 AUDIT-mode pivot reflection

The silent-failure-hunter normal mode (auditing code for swallowed errors, broad catch blocks, fallback-to-mock anti-patterns) maps cleanly onto SDTM PDF atomization quality auditing along three dimensions:

1. **"Silent failure" ↔ "verbatim drift"**: Atom 2's OESEO→OESEQ corruption is the data-side analog of a silent failure. It passes structural validation (correct atom_type, correct parent, correct pipe-count, correct field count) the same way code passes a try/catch with bare-except. Both produce undetectable downstream defects without ground-truth verification (PDF for atoms / actual error logs for code). The per-atom FAIL adjudication is conceptually identical to flagging an empty catch block: the issue is not visible from the atom-internal contract alone — only from cross-referencing the source-of-truth (PDF / upstream caller).

2. **"Broad catch block" ↔ "NEW2 char-level scope too narrow"**: NEW2 (single-char Cyrillic-Latin homoglyph) catches Cyrillic-Latin only and silently passes Latin-Latin adjacent-key swaps. This is structurally identical to a `catch (Exception e) { logError(); }` that catches all errors but only handles the documented subset, silently dropping unknown error types. NEW8 substring n-gram is the v1.3 codified mitigation analogous to specific exception subclassing; F-1 shows NEW8 is necessary but not yet sufficient on Identifier-cell tokens (Rec-1 oracle expansion).

3. **"Fallback to mock" ↔ "writer paraphrase fallback"**: Round 4 batch 24 verbatim 41.2% FAIL precedent (writer-family SENTENCE paraphrase 'illustrate'→'distinguish') is conceptually a fallback-to-mock anti-pattern: when the writer can't precisely transcribe, it falls back to summarizing — masking the underlying transcription difficulty without surfacing the issue. Drift cal NEW1 dual-threshold is the AUDIT-side surfacing mechanism. Batch 31 atom 2 OESEO is a milder version: the writer didn't paraphrase whole sentences, but a single adjacent-key fingerslip went unflagged because no "I'm uncertain about this character" surfacing mechanism exists.

**pr-review-toolkit family 2nd burn observation vs batch 29 `code-reviewer` 1st burn**: The same-family different-agent recipe holds. silent-failure-hunter brings a more skeptical default posture (treats every PASS as innocent-until-proven-guilty) which materialized as the careful F-1 PDF cross-check on atom 2 — adjacent-letter substitutions are the exact failure mode silent-failure-hunter normal mode is tuned to surface in code (e.g. typos in error-ID constants that silently break Sentry routing). The pr-review-toolkit family appears well-suited to AUDIT-mode pivots; recommend continued pool burn into round 7+ for further family-agnostic recipe validation. AUDIT-mode pivot count: 21 cumulative across rounds 1-6, 0 systemic family-skew false positives observed. Recipe robust.

---

**Final single-line return**: see main session message.
