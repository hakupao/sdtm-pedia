# Rule A Batch 43 Reviewer Notes — Tracer Flavor
# Slot #55 oh-my-claudecode:tracer, AUDIT pivot 36th cumulative
# omc-family 12th burn intra-family depth — "tracer-strategist" 1st live-fire

## Trace Report

### Observation

10 atoms from batch 43 (p.421-430, seed=20260429) were audited for verbatim byte-exact PDF fidelity, atom_type classification correctness, parent_section canonical accuracy, and schema completeness. Two main-session pre-flagged observations were investigated with independent chain-of-evidence: OBS-A (hyphen vs en-dash discrimination in RELREC heading verbatim) and OBS-B (§8 L1 HEADING parent_section using sibling §7 as parent instead of document root sentinel).

All 10 sample atoms returned PASS. One LOW finding was raised (O-P1-149) from the OBS-B investigation — the §8 L1 HEADING atom outside the sample has an incorrect parent_section. OBS-A resolved as FALSE POSITIVE.

---

### Hypothesis Table — OBS-A (RELREC dash discrimination)

| Rank | Hypothesis | Confidence | Evidence Strength | Why it remains plausible |
|------|------------|------------|-------------------|--------------------------|
| 1 | PDF itself uses mixed dash types (hyphen for Description, en-dash for Specification); writer correctly preserved both | High | Strong (Tier 2 — byte-level xxd of PDF source) | xxd shows `0x2D` at line 25 and `0xE2 0x80 0x93` at line 28; writer atoms match exactly |
| 2 | Writer used inconsistent dash transcription; PDF is uniform | Eliminated | Contradicted by Tier-2 evidence | Falsified by xxd — PDF has two distinct byte sequences for the two headings |

### Evidence For

- **H1**: `pdftotext -layout -f 429 -l 429 ... | grep RELREC | xxd` at offset `0x0290`: line 25 bytes `52 45 4c 52 45 43 20 2d 20 44` = `RELREC - D` (ASCII hyphen 0x2D); line 28 bytes `52 45 4c 52 45 43 20 e2 80 93 20 53` = `RELREC – S` (UTF-8 en-dash 0xE2 0x80 0x93). Atom `ig34_p0429_a017` verbatim contains ASCII `-`; atom `ig34_p0429_a019` verbatim contains Unicode `–`. Both match the PDF source byte-for-byte.

### Evidence Against / Gaps

- **H1 (against)**: None. The byte-level evidence is unambiguous. The only prior uncertainty was that both heading names looked similar enough to trigger human suspicion. That suspicion is understandable but the evidence resolves it.
- **H2**: Directly falsified by xxd output. The PDF source has two distinct byte sequences. H2 cannot survive the discriminating probe.

### Rebuttal Round

- **Best challenge to H1**: Could pdftotext have introduced encoding artifacts, misrepresenting the actual PDF glyph? A PDF could use the same glyph visually rendered by two different code points via font mapping.
- **Why H1 still stands**: pdftotext with `-layout` flag performs Unicode mapping from PDF font encoding. For a document in standard Latin encoding (ISO-8859-1 or UTF-8), ASCII hyphen and en-dash are distinct in the font metrics. The document uses standard SDTMIG PDF formatting with no unusual font encoding observed in other pages. No other atoms in batch 43 show encoding artifacts. The xxd evidence at byte level is decisive.

### Convergence / Separation Notes

H2 (writer inconsistency) collapses entirely into H1 (PDF-native mixed usage). There is no residual uncertainty.

### Current Best Explanation — OBS-A

The PDF source document uses an ASCII hyphen in "RELREC - Description/Overview" and a typographic en-dash in "RELREC – Specification". This is a typographic inconsistency in the original CDISC PDF, not a writer error. The writer (oh-my-claudecode:executor) correctly reproduced both characters byte-for-byte. OBS-A is a FALSE POSITIVE — the main-session flagging was appropriate precaution but the evidence eliminates the concern.

### Critical Unknown — OBS-A

None remaining. The byte-level evidence fully resolves the question.

### Discriminating Probe — OBS-A (retrospective)

The probe `pdftotext -layout -f 429 -l 429 ... | grep RELREC | xxd` was the single highest-value probe — it returned byte-level character encoding and uniquely discriminated between the two hypotheses in one step. This probe pattern (pdftotext + grep + xxd pipeline) is the recommended standard for future dash-discrimination questions in SDTMIG PDF atoms.

---

### Hypothesis Table — OBS-B (§8 L1 HEADING parent_section)

| Rank | Hypothesis | Confidence | Evidence Strength | Why it remains plausible |
|------|------------|------------|-------------------|--------------------------|
| 1 | parent_section for §8 L1 HEADING should be `"(SDTMIG v3.4)"` root sentinel, not `"§7 [TRIAL DESIGN MODEL DATASETS]"` | High | Strong (Tier 2 — direct primary artifact ig34_p0382_a001 with tight provenance) | §7 L1 HEADING uses `"(SDTMIG v3.4)"` establishing the convention; §8 is a sibling of §7 not a child |
| 2 | Using the prior L1 chapter as parent is a legitimate "nearest prior heading" sliding-window convention | Low | Weak (Tier 5 — spatial proximity / heuristic analogy) | Writer may have applied a sliding-window nearest-heading rule without distinction between sibling vs parent relationships |

### Evidence For

- **H1**: Atom `ig34_p0382_a001` (batch_39a.jsonl, p.382): `{"atom_type": "HEADING", "verbatim": "7  Trial Design Model Datasets", "heading_level": 1, "parent_section": "(SDTMIG v3.4)"}`. This is a Tier-2 primary artifact with full provenance establishing that L1 chapter headings use document root sentinel `"(SDTMIG v3.4)"` as parent_section.
- **H1**: Semantic structure: §7 and §8 are both L1 siblings under the SDTMIG v3.4 document. A heading tree cannot have a sibling as parent without creating a false nesting that contradicts the document structure.
- **H1**: Downstream impact: P4b tree build uses parent_section to establish heading ancestry chains. If `ig34_p0427_a001` (§8 L1 HEADING) has parent=`"§7 [TRIAL DESIGN MODEL DATASETS]"`, retrieval queries for §8 content would incorrectly traverse through the §7 branch.

- **H2**: Atom `ig34_p0427_a001` is the first §8 atom encountered; the writer's extraction window on p.427 begins after the §7 content concluded. The nearest prior heading in the text stream is the §7 L1 heading. A sliding-window "nearest heading up the stack" heuristic could produce this assignment.

### Evidence Against / Gaps

- **H1 (against)**: The pattern is internally consistent within batch 43b — all §8 content atoms correctly use `"§8 [REPRESENTING RELATIONSHIPS AND DATA]"` as parent, meaning the writer correctly recognized §8 as an L1 heading and applied its short-bracket form for all subsequent atoms. The error is specifically localized to the heading atom itself (its own parent_section, not the parent_section it defines for children).
- **H2 (against)**: The §7 L1 HEADING itself (ig34_p0382_a001) did NOT use the prior L6 section heading as parent — it used the document root. This shows the extraction protocol does distinguish root-level headings. H2 requires assuming the writer applied a different rule for §8 than for §7, which needs an ad hoc explanation.

### Rebuttal Round

- **Best challenge to H1**: Could there be a batch-boundary effect? Batch 43 starts at p.421, within the §7 content region. By the time the writer reaches §8 at p.427, the §7 heading is the last L1 heading seen within the batch window. Perhaps the convention `"(SDTMIG v3.4)"` applies only when the L1 heading appears at the start of a fresh batch with no prior L1 context, not when it appears mid-batch after a sibling.
- **Why H1 still stands**: The rebuttal is plausible as a mechanism but not as a justification. The schema requires parent_section to reflect structural hierarchy, not extraction-window context. The §7 L1 HEADING was at the start of batch 39b's window (p.382 = first page of that batch) and correctly used `"(SDTMIG v3.4)"`. If the §8 L1 HEADING had appeared at the start of a fresh batch, it would likely also use the root sentinel. The fact that it appears mid-batch (p.427) after §7 content explains the writer's heuristic but does not make the resulting parent_section structurally correct. The fix is straightforward: `"(SDTMIG v3.4)"` regardless of batch context.

### Convergence / Separation Notes

H1 and H2 do not converge — they imply different root causes: H1 implies a writer logic error at L1 chapter boundaries mid-batch; H2 implies the convention is legitimately ambiguous at batch seams. They remain genuinely distinct. The evidence strongly favors H1. H2 has no Tier-1 or Tier-2 support.

### Current Best Explanation — OBS-B

The §8 L1 HEADING atom `ig34_p0427_a001` has an incorrect parent_section (`"§7 [TRIAL DESIGN MODEL DATASETS]"` instead of `"(SDTMIG v3.4)"`). The writer's extraction heuristic assigned the most recently seen L1 heading (§7) as parent when encountering the §8 L1 heading mid-batch. The established convention (evidenced by §7 at p.382 in batch_39a) is to use the document root sentinel `"(SDTMIG v3.4)"` for all L1 chapter headings. This is a LOW severity structural error — verbatim content is correct, atom_type is correct, the error affects only the heading atom's parent_section field and does not propagate to the content atoms under §8 (which all correctly use `"§8 [REPRESENTING RELATIONSHIPS AND DATA]"`).

**Finding O-P1-149 LOW** filed. Option H single-atom fix recommended.

### Critical Unknown — OBS-B

Whether this L1 mid-batch parent_section error is isolated to `ig34_p0427_a001` or also affects other L1 heading atoms in batches 41 and 42 (which also contain cross-chapter boundary transitions). If batches 41-42 contain L1 chapter HEADING atoms, their parent_section fields should be independently verified against the `"(SDTMIG v3.4)"` convention.

### Discriminating Probe — OBS-B (for future batches)

Search all L1 HEADING atoms (`heading_level: 1`) across all batch files for atoms where `parent_section` is not `"(SDTMIG v3.4)"`:
```
grep "heading_level.*1" pdf_atoms_batch_*.jsonl | grep -v "(SDTMIG v3.4)"
```
This single probe would enumerate all L1 HEADING atoms with non-root parent_section and reveal whether O-P1-149 is isolated or systematic.

---

### Cross-Cutting Observations (batch 43 overall)

**N19 WARN — ig34_p0429_a021**: Atom verbatim `"relrec.xpt, Related Records — Relationship. One record per related record, group of records or dataset, Tabulation."` matches regex `\.\s+[A-Z]` (". One"). However, this is a spec-table preamble line — the full text is the RELREC dataset descriptor that precedes the specification table. In SDTMIG PDF format, this descriptor appears as a single typographic line before the column headers. Classifying it as SENTENCE is defensible (it is a single structured assertion), but NOTE or a HEADING sub-variant might be more semantically precise. The N19 WARN is registered; not a finding at this stage.

**Tracer-mode observation on atom_type borderline cases (batch 43 specific)**:

The batch 43 content span crosses three structural zones:
1. p.421-423: TS Examples (TABLE_ROW-dominant, executor mandatory per N18.a)
2. p.424-426: §7.4.2.1 + §7.5 (SENTENCE + LIST_ITEM-dominant, NullFlavor hierarchy table is spec-table)
3. p.427-430: §8 intro + §8.1-8.2 (SENTENCE-dominant with transition to RELREC spec + examples)

The writer correctly applied different atom_type patterns across these zones. No zone-boundary misclassification detected in the 10-atom sample. The RELREC spec table on p.429-430 is particularly dense (HEADING → SENTENCE → HEADING → TABLE_HEADER → TABLE_ROW sequence) and the executor handled the transition correctly.

**Recommended monitoring flag**: The `ig34_p0429_a021` SENTENCE (spec preamble "relrec.xpt, Related Records — Relationship...") should be reviewed in the reconciler sweep to determine if equivalent spec-preamble atoms in earlier batches (e.g., preceding TABLE_HEADER atoms for other datasets) were classified consistently. If prior spec-preambles are classified as HEADING (L5/L6 sub-heading variants) or NOTE, then ig34_p0429_a021 may need reclassification for consistency.

---

### Uncertainty Notes

- All 10 sample atom verdicts are at high confidence (Tier-2 evidence from direct PDF extraction).
- OBS-A: fully resolved, no residual uncertainty.
- OBS-B: resolved as real finding with HIGH confidence in diagnosis; severity assessment at LOW is well-supported by scope analysis (single atom, does not propagate to content atoms).
- N19 ig34_p0429_a021: LOW uncertainty on atom_type classification; WARN-mode only, no blocking impact.
- The question of whether ig34_p0427_a001's parent_section error is isolated or systematic requires the discriminating probe (grep L1 headings across batches 41-42).
