# Rule A Batch 40 Reviewer Notes (cross-cutting observations)

## Cross-cutting observations

### 1. SENTENCE atomicity — md vs PDF asymmetry (candidate v1.6 hook)

Atom `ig34_p0391_a002` concatenated 2 distinct sentences ("The following table illustrates..." + "It corresponds closely...") into a single SENTENCE atom. Per atom_schema.json `sentence_not_paragraph` note, the rule "md 一段含 N 句 → 必拆 N 个 SENTENCE 原子" is codified for md atoms but NOT explicitly for PDF atoms.

Observation: PDF prose extracted from running paragraphs may quietly accumulate multi-sentence concatenations under writer interpretation latitude. Round 5+6+7+8 drift cal motifs all flag SENTENCE-level paraphrase / value-hallucination but not multi-sentence-fusion specifically.

Candidate v1.6 hook: extend `sentence_not_paragraph` rule to PDF atoms explicitly, with Self-Validate Hook 18 (split-on-period-or-semicolon-followed-by-uppercase pre-DONE check). Light-implementation, no new tooling, parallels Hook 14-17 family.

Severity if codified: prevents under-counting per-page atom totals (1 fused atom vs N sentence atoms = N-1 atom undercount per fusion event). Density-alarm floor calculations would also stabilize (G-MS-12 LIST_ITEM-heavy floor 8 vs Examples-narrative floor 12 — fused SENTENCE atoms would push some pages below floor falsely).

Defer to v1.6 candidate stack alongside OBS-1/OBS-2/OBS-3.

### 2. TABLE_ROW outer-pipe convention — clean in batch 40

All 3 TABLE_ROW atoms sampled (p.394_a013 / p.397_a019 / p.399_a011) honored:
- Outer pipe convention N+1 (12 pipes for 11 columns) per O-P1-26
- Empty cell preservation (TABRANCH and TATRANS empty cells rendered as `| |` not `||` collapsed) per N5 G-MS-NEW-6-1
- No value hallucination (IDVAR/QNAM not applicable here as TA dataset; ARMCD + ELEMENT + EPOCH all match PDF source byte-exactly)

Round 5+6+7+8 4 cumulative writer-direction VALUE HALLUCINATION recurrences NOT observed in this 3-atom TABLE_ROW sample. N16 writer-family ban for Examples-narrative + spec-table content type appears EFFECTIVE — both 40a + 40b writers were oh-my-claudecode:executor (writer-family banned per N16), and TABLE_ROW byte-exactness held.

### 3. FIGURE description verbosity — within bounds

Both FIGURE atoms (p.393_a002 + p.395_a005) used the `[FIGURE: ...]` description convention per atom_schema.json `figure_verbatim_convention` note. Descriptions captured:
- p.393: 4 retrospective branches with epoch labels + arm assignments
- p.395: Cyclical chemo with "if disease progression" skip arrows + 4-cycle Drug A/B pattern

No OCR fabrication, no Mermaid promotion to imaginary-detail level. figure_ref convention `pdf_p<NNN>+<region>` honored both times.

### 4. parent_section canonical form discipline — fully clean

All 10 atoms used the `§7.2.1 Trial Arms (TA) – Example N` or `– Examples` canonical form. No L2 short-bracket violations (`§7 [TRIAL DESIGN MODEL DATASETS]` parent-skip per N8 NEW9), no .xpt-parent violations (`ta.xpt` as parent_section per N15 .xpt-parent FORBID), no L4 self-parent violations.

This is a clean signal — N15 + N8 codifications appear to be holding at this depth (p.391-400 deep interior of §7.2.1).

### 5. AGENT-vs-SKILL roster — no gaps observed

`general-purpose` is correctly listed in §0 Registered AGENTS list (Task tool dispatchable). No SKILL-vs-AGENT pre-allocation lint hits this audit. Roster doc §0 v1.5 codification (per V1) appears complete for this slot.

### 6. round 9 multi-session protocol — observation

Batch 40 = round 9 Session D, 1st batch of round 9 multi-session. Pre-Rule-A schema sweep reported 0 violations across 204 atoms (clean baseline). This audit (10/204 = ~4.9% sample) confirms the schema sweep at narrow depth — 0 schema violations + 0 verbatim violations + 0 atom_type violations + 0 parent_section violations across the sample. Round 9 protocol is functioning as designed.

## v1.6 candidate stack additions (this audit)

| ID | Severity | Candidate |
|---|---|---|
| OBS-4 | LOW | Extend `sentence_not_paragraph` rule from md-only to PDF atoms (Self-Validate Hook 18 split-on-period-followed-by-uppercase pre-DONE check). Light implementation. Per atom 1 PARTIAL observation. |

OBS-1/OBS-2/OBS-3 from v1.5 cut reviewer slot #48 carry forward unchanged.

## Reviewer slot #51 metadata

- subagent_type: `general-purpose`
- AUDIT pivot: 32nd cumulative
- Family burn: 3rd extension (post round 5 inaugural + round 7 G-MS-4 fallback)
- Recipe validation: family-agnostic AUDIT-mode protocol VALIDATED at 3-burn intra-family depth scale
- Branch used: Branch A (Write tool available)
- Rule D independence: preserved (writer family `oh-my-claudecode:executor` ≠ reviewer family `general-purpose`)
- Output independence: 3 files written into `evidence/checkpoints/` without modifying any atom file or root ledger
