# Rule A Batch 29 Audit Summary

> Reviewer slot #38 (`pr-review-toolkit:code-reviewer`) — pr-review-toolkit family **first burn**, 19th AUDIT-mode pivot cumulative, full-tool variant.
> Sample: `evidence/checkpoints/rule_a_batch_29_sample.jsonl` (10 atoms, stratified seed=20260615, p.281-290).
> PDF source: `source/SDTMIG v3.4 (no header footer).pdf` p.281-290 (10 pages = batch 29 full coverage).

---

## §1 — Sample composition + per-page coverage

| Page | Region | atom_id | atom_type |
|------|--------|---------|-----------|
| 281 | middle | ig34_p0281_a036 | TABLE_ROW |
| 282 | bottom | ig34_p0282_a037 | TABLE_ROW |
| 283 | middle | ig34_p0283_a031 | TABLE_ROW |
| 284 | middle | ig34_p0284_a009 | SENTENCE |
| 285 | bottom | ig34_p0285_a013 | LIST_ITEM |
| 286 | top    | ig34_p0286_a005 | TABLE_ROW |
| 287 | middle | ig34_p0287_a018 | TABLE_ROW |
| 288 | bottom | ig34_p0288_a020 | LIST_ITEM |
| 289 | middle | ig34_p0289_a017 | TABLE_HEADER |
| 290 | middle | ig34_p0290_a011 | TABLE_ROW |

**atom_type distribution**: 6 TABLE_ROW / 2 LIST_ITEM / 1 SENTENCE / 1 TABLE_HEADER (matches kickoff prescription).
**Page coverage**: 1 atom per page across all 10 batch pages.
**Section coverage**: §6.3.5.9.3 PP-PC Relating (Examples 3+4 + PC-PP Conclusions) on p.281-284 / §6.3.7.1 Generic on p.285-286 / §6.3.7.2 CV on p.287-289 / §6.3.7.3 MK on p.290.

---

## §2 — Per-atom verdict table

| atom_id | page | atom_type | verdict | verbatim | atom_type | parent_section | atom_id | hl_sib | outer-pipe | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| ig34_p0281_a036 | 281 | TABLE_ROW | **FAIL** | FAIL | PASS | PASS | PASS | N/A | PASS | IDVAR field VALUE-HALLUCINATION (PCSEQ → should be PCGRPID per Method C row 2) |
| ig34_p0282_a037 | 282 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | N/A | PASS | Faithful to p.282 Method A row 2 (DY1DRGX_A no-underscore source-internal variant preserved) |
| ig34_p0283_a031 | 283 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | N/A | PASS | Method D row 19 PCSEQ=8 RELID=2 match |
| ig34_p0284_a009 | 284 | SENTENCE | **PARTIAL** | PASS | PASS | PARTIAL | PASS | N/A | N/A | parent_section L5 too generic — paragraph sits under L6 'PC-PP Conclusions'; cross-batch handoff under-claim motif |
| ig34_p0285_a013 | 285 | LIST_ITEM | PASS | PASS | PASS | PASS | PASS | N/A | N/A | §6.3.7.1 Generic Spec first bullet exact match |
| ig34_p0286_a005 | 286 | TABLE_ROW | **PARTIAL** | FAIL | PASS | PASS | PASS | N/A | PASS | 'Trial Summary **dataset**' vs PDF 'Trial Summary **domain**' — single-word writer paraphrase (NEW8 SENTENCE-trigram motif) |
| ig34_p0287_a018 | 287 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | N/A | PASS | CVSTRESU row exact match |
| ig34_p0288_a020 | 288 | LIST_ITEM | PASS | PASS | PASS | PASS | PASS | N/A | N/A | CV – Assumptions item 1 exact match |
| ig34_p0289_a017 | 289 | TABLE_HEADER | PASS | PASS | PASS | PASS | PASS | N/A | PASS | Example 2 cv.xpt 18-column header match (Row + 17 vars) |
| ig34_p0290_a011 | 290 | TABLE_ROW | PASS | PASS | PASS | PASS | PASS | N/A | PASS | MKSEQ row — correctly says 'Trial Summary domain' (contrast with atom 6) |

---

## §3 — Aggregate weighted % + threshold verdict

| Metric | Value |
|---|---|
| PASS_n | 7 |
| PARTIAL_n | 2 |
| FAIL_n | 1 |
| Weighted score | 7×1.0 + 2×0.5 + 1×0.0 = **8.0 / 10** |
| **Raw weighted %** | **80.0%** |
| Threshold (≥90% effective PASS) | **BELOW** |

**Verdict**: BELOW 90% raw threshold (80% weighted) — **Option E full-batch rerun candidate** OR targeted per-atom repair (atoms 1, 4, 6) recommended pending main-session adjudication.

The two TRUE-POSITIVE verbatim divergences (atom 1 PCSEQ vs PCGRPID, atom 6 dataset vs domain) are both writer-family value-substitution motifs. Atom 1 is a HIGH severity hallucination (semantically impossible PCSEQ=DY1_DRGX_B); atom 6 is a MEDIUM severity single-word paraphrase (semantic equivalent dataset/domain but R10 strict violation). Atom 4 is a parent_section under-specification only — non-blocking but noted.

---

## §4 — Cross-batch sibling continuity observations (NEW7 chain)

### Heading-level sibling chain (28b → 29a → 29b boundary)

The sample contains 0 HEADING atoms (per stratified design — TABLE_ROW/LIST_ITEM/SENTENCE/TABLE_HEADER only). Sibling continuity for L4-L7 must be inferred from parent_section assignments:

- **L5/L6 PP-PC Relating chain (p.281-284)** — Atoms 1-4 all carry parent_section anchored at `§6.3.5.9.3 Relating PP Records to PC Records`. PDF p.281-283 contain Example 3 Methods B/C/D (L7 hl=7 sib=2/3/4 RESTART under Example 3) + Example 4 Method A (L7 hl=7 sib=1 RESTART under Example 4). PDF p.284 contains Method D for Example 4 + PC-PP Conclusions (L6 sib=7) + PC-PP Suggestions (L6 sib=8). Atoms 1-3 use ` — Example 3` / ` — Example 4` dual-form acceptable. **Atom 4 (PARTIAL) flags potential L6 PC-PP Conclusions sibling drift** — the SENTENCE belongs under PC-PP Conclusions L6 heading but parent points to L5 only. NEW7 L6 sub-batch context drift motif (round 3 batch 23 + round 4 batch 25 + round 5 reconciler O-P1-92 = 3rd CROSS-batch recurrence). Round 6 codification CONFIRMED needed.

- **§6.3.6/§6.3.7 L3 transition (p.285)** — Atom 5 sits under §6.3.7.1 Generic, post §6.3.6 MO decommissioning + §6.3.7 Morph/Phys group container header. L3 sib=6/7 RESTART convention upheld (parent_section §6.3.7.1 is L4 sib=1 under §6.3.7 group). NEW7 L4 group-container precedent (round 4 batch 25 §6.3.5.7.1 MB) extends here cleanly — Generic Spec L4 sib=1, CV L4 sib=2, MK L4 sib=3 RESTART per group container.

- **§6.3.7.2 CV L4 sib=2 (p.286-289)** — Atoms 6/7/8/9 all parent §6.3.7.2 CV. Atom 9 (TABLE_HEADER) at p.289 belongs to Example 2 (L6) cv.xpt second table — proper L6 sib continuity inferred.

- **§6.3.7.3 MK L4 sib=3 (p.290)** — Atom 10 parents §6.3.7.3 MK Description+Specification region. L4 sibling RESTART under §6.3.7 group container correctly upheld.

### Cross-batch handoff (28b → 29a)

Per kickoff inline-prepended state from round 5 batch 28b 终态: §6.3.5.9.3 PP-PC Relating L5 sib=3 / Examples L5 sib=4 / Example 3 L6 sib=3 / Method D L7 sib=4 at p.280. Batch 29a then opens at p.281 with **Method B for Example 3** which would be L7 sib=2 RESTART under Example 3 L6 sib=3. Need to verify in root pdf_atoms.jsonl that the L7 transition properly RESTARTs (cannot verify directly from sample — flag for reconciler-side sibling_continuity_sweep pass).

### Cross-batch handoff (29a → 29b)

Per task header: 29a covers p.281-285 (196 atoms, post Option E rerun) and 29b covers p.286-290 (116 atoms, clean first-attempt). The L4 transition §6.3.7.1 Generic (p.285 end) → §6.3.7.2 CV (p.286-289) → §6.3.7.3 MK (p.290) crosses the 29a→29b boundary at p.285→p.286. Atoms 5 (p.285 a013) and 6 (p.286 a005) parent the L4 anchors correctly, suggesting the cross-sub-batch handoff for L4 group-container chain succeeded.

---

## §5 — Adjudication notes & recommendations

### True-positive findings (recommend main-session action)

1. **Atom 1 (p.281 a036) HIGH** — IDVAR=PCSEQ should be PCGRPID per PDF p.281 Method C row 2. **Recommended action**: targeted per-atom repair (single-atom edit) preferable to full-page rerun since this is a localized writer copy-paste error, not systemic. If similar pattern recurs in other Method C rows in batch 29a (rows 1, 8 of Method C also PCGRPID), recommend Option E full sub-batch rerun verification of all Method C atoms in 29a. Finding ID candidate: **O-P1-93 HIGH VALUE-HALLUCINATION** — IDVAR field substitution (PCSEQ↔PCGRPID swap). New motif extension to NEW1 dual-threshold cal CATASTROPHIC FAIL precedent (round 5 batch 27 5th time). Drift-cal reviewer candidates may want to flag this whole sub-batch p.281 cross-table.

2. **Atom 6 (p.286 a005) MEDIUM** — 'dataset' vs 'domain' single-word substitution in generic --SEQ row CDISC Notes. Atom 10 (p.290 MKSEQ) on the same boilerplate template correctly uses 'domain'. **Recommended action**: targeted per-atom repair. Finding ID candidate: **O-P1-94 MEDIUM SENTENCE-trigram paraphrase** (writer-family NEW8.b motif extension). Cross-validation table check: atom 10 same template = correct → atom 6 is the one divergence, not atom 10.

3. **Atom 4 (p.284 a009) LOW** — parent_section under-specified (L5 instead of L6 PC-PP Conclusions). **Recommended action**: parent_section field-only patch (no verbatim re-extraction needed). Finding ID candidate: **O-P1-95 LOW NEW7 L6 sub-batch context drift CROSS-batch 4th recurrence** — extending the round 3+4+5 series. **Round 6 round-level signal**: NEW7 L6 cross-batch handoff codification round 6 mandatory was triggered AGAIN even with kickoff inline-prepend protocol, suggesting prepend alone insufficient — may need stronger structural validation pass at reconciler stage.

### False-positive flags (none)

No false-positive risk identified. All verdicts traceable to PDF char-by-char comparison.

### Anomalies / observations

- **Source-internal inconsistency** (atoms 1 vs 2): PDF p.281 Method C uses `DY1_DRGX_A` (with underscore between Y and DRGX) while p.282 Method A uses `DY1DRGX_A` (no underscore). Both atoms preserve the page-specific source form. This is faithful extraction, not a writer bug.
- **Atom 8 numbered list prefix preserved**: atom_type=LIST_ITEM with verbatim starting "1. The Cardiovascular...". Per R8/R10 strict, the "1. " prefix should be retained as part of the list-item content. PASS — atom honors numbered list convention.
- **Atom 9 TABLE_HEADER 18-column**: Successfully passes NEW8.c TABLE_HEADER column-set codification (round 5 batch 27 motif extension). Wide-table corruption risk LOW since header was extracted as single atom rather than mis-fragmented.

### Recommendations for main session

1. **Apply targeted per-atom repairs** to atoms 1, 4, 6 (or escalate to Option E full sub-batch 29a rerun if writer-family systemic motif suspected — recommend cross-checking ALL Method C TABLE_ROW atoms in 29a + ALL --SEQ-template TABLE_ROW atoms in 29a/29b for 'dataset' vs 'domain' divergence).
2. **Open 3 findings**: O-P1-93 HIGH (atom 1), O-P1-94 MEDIUM (atom 6), O-P1-95 LOW (atom 4).
3. **Sibling continuity sweep** (reconciler pass): verify L7 Method B/C/D sib chain RESTART under Example 3 L6 sib=3 at p.281 boundary, AND verify PC-PP Conclusions L6 sib=7 / PC-PP Suggestions L6 sib=8 at p.284 boundary.
4. **Round 6 NEW7 L6 cross-batch motif 4th recurrence (atom 4)** — confirms G-MS-7 NEW7 L6 sub-batch handoff codification round 6 mandatory; recommend v1.4 candidate for reconciler-side structural validator pass (programmatic check that every SENTENCE/LIST_ITEM under L6 leaf heading carries L6 parent_section, not L4/L5 ancestor).
5. **Drift cal touch-point**: atom 1 IDVAR hallucination is a NEW VALUE-HALLUCINATION motif (column-shift adjacent — IDVAR shifted left/right, not just paraphrased). Could feed into batch 30 mandatory drift cal (5th-time CATASTROPHIC FAIL extension watch).

### Aggregate verdict

**Rule A batch 29 BELOW 90% threshold (80% weighted, 7P/2PA/1F)** — recommend main session decision: (a) targeted per-atom repair × 3 atoms (efficient, ~5 min), or (b) Option E full sub-batch 29a rerun if writer-family systemic risk suspected (~30-60 min). Recommendation favors (a) since 2 of 3 issues are localized and atom 10 demonstrates the boilerplate template is mostly correctly extracted.
