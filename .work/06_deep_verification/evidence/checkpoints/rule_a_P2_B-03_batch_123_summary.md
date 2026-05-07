# Rule A Audit Summary — batch_123 TA/examples.md slice A (L1-L344)

> Reviewer: oh-my-claudecode:executor (independent subagent_type, ≠ writer general-purpose) per Rule D
> Prompt: P0_reviewer_v1.9.3 (35 hooks)
> Audit timestamp: 2026-05-07
> Verdict: **PASS** (12/12 = 100.00%)

---

## §0 Sample (N=12, stratified, seed=20260507)

Per v1.9.3 reviewer rubric (113 atoms → N=12) + Rule A weighted ≥70%; stratified across atom_type + parent_section namespace.

| atom_id | atom_type | line_range | parent_section |
|---------|-----------|-----------|----------------|
| md_dmTA_ex_a001 | HEADING (H1) | L1-L1 | §TA [TA — Examples] |
| md_dmTA_ex_a004 | SENTENCE | L5-L5 | §TA [TA — Examples] |
| md_dmTA_ex_a009 | LIST_ITEM | L12-L12 | §TA [TA — Examples] |
| md_dmTA_ex_a013 | HEADING (H2 sib=1) | L18-L18 | §TA [TA — Examples] |
| md_dmTA_ex_a022 | FIGURE | L60-L80 | §TA.1 [Example 1] |
| md_dmTA_ex_a028 | TABLE_ROW | L103-L103 | §TA.1 [Example 1] |
| md_dmTA_ex_a043 | SENTENCE (split) | L122-L122 | §TA.2 [Example 2] |
| md_dmTA_ex_a047 | FIGURE | L137-L177 | §TA.2 [Example 2] |
| md_dmTA_ex_a064 | TABLE_ROW | L227-L227 | §TA.2 [Example 2] |
| md_dmTA_ex_a086 | FIGURE | L251-L265 | §TA.3 [Example 3] |
| md_dmTA_ex_a095 | TABLE_HEADER | L320-L321 | §TA.3 [Example 3] |
| md_dmTA_ex_a113 | TABLE_ROW | L342-L342 | §TA.3 [Example 3] |

Stratification check (per requirement):
- HEADING ≥1 (H1 + numbered H2): 2 ✓
- FIGURE ≥3: 3 ✓ (one per Example 1/2/3)
- TABLE_ROW ≥2: 3 ✓
- TABLE_HEADER ≥1: 1 ✓
- SENTENCE ≥2: 2 ✓
- LIST_ITEM ≥1: 1 ✓
- ≥1 atom per parent_section namespace (4 ns): all 4 covered ✓ (§TA=4, §TA.1=2, §TA.2=3, §TA.3=3)

---

## §1 Per-dimension PASS rate

| Dimension | PASS | Rate |
|-----------|------|------|
| Verbatim fidelity | 12/12 | 100.00% |
| Schema (12-field, atom_type enum, sib rules) | 12/12 | 100.00% |
| parent_section (§2.5 + H1/H2 rules) | 12/12 | 100.00% |
| Hooks (§E-1..E-5, §2.6, §2.9, Hook D-NOTE-BQ) | 12/12 | 100.00% |

Notes:
- a043 SENTENCE (L122) initial mechanical comparison flagged FAIL — but this is a **sentence-split atom** per `atom_schema.json` notes (`sentence_not_paragraph`: a paragraph with N sentences → N SENTENCE atoms). Verified a042+a043 byte-exact reconstruct L122 source (joined with " " separator). Both PASS.
- All 12 atoms 12 fields explicit (incl. null for non-applicable per §E-1/E-5).
- a001 H1 sib=1 ✓ (§E-2). a013 H2 sib=1 ✓ (§2.5 self-namespace). a095 TABLE_HEADER sib=null ✓ (§E-3).
- All non-HEADING atoms in sample have heading_level=null + sibling_index=null ✓ (§E-5).

---

## §2 Weighted overall

Weighted PASS rate (Rule A 4-of-4 strict): **12/12 = 100.00%** (≥ threshold 90%).

Per-dim equal weighting: (1.00 + 1.00 + 1.00 + 1.00) / 4 = 1.000.

---

## §3 Findings

**HIGH severity**: 0
**MED severity**: 0
**LOW/INFO**: 1 — see §4

### Inconsistencies between writer report and JSONL (informational, no rule violation)

Writer report §0 / §2 contained drafting errors in atom_id mapping commentary (e.g. report claimed a012=H2 Example 1 / a040=H2 Example 2 / a080=H2 Example 3, but actual JSONL has a013=H2 Example 1 sib=1 / a041=H2 Example 2 sib=2 / a081=H2 Example 3 sib=3). These are **report-text errors, not data errors** — JSONL ground truth is consistent and audit-PASS. Recommend writer report regeneration carry-forward to round 12 retro (no schema/data impact, INFO only).

---

## §4 §F-2 ratio verdict (schema-issue vs source-style-outlier)

**Verdict: SOURCE-STYLE OUTLIER (INFO carry-forward, not schema issue).**

### Evidence

1. **Coverage sweep**: 1 uncovered non-blank line (L344 `## Example 4`) — correctly excluded as slice B boundary, NOT a missed atom.
2. **TABLE_ROW count plausibility**: source `wc -l` of pipe-rows (excluding separators + headers) = **52 source rows** ≡ 52 atoms. 0 missing.
3. **TABLE_HEADER count**: source = **6 header rows** (3 TDM + 3 ta.xpt) ≡ 6 atoms. 0 missing.
4. **HEADING count**: source = 5 heading lines (1 H1 + 4 H2 incl. L344 boundary); 4 atoms in slice (H1 + 3 H2) — L344 H2 correctly slice B's. 0 missing.
5. **LIST_ITEM count**: source = 6 list items (L9-14) ≡ 6 atoms. 0 missing.
6. **FIGURE compression**: 10 mermaid blocks span **194 source lines** (each block 12-41 lines) → 10 atoms. This is the dominant ratio driver.

### Properly-computed de-figure ratio

Writer report used `~120L mermaid compression` heuristic giving 0.460 below band. Actual measurement:
- FIGURE absorbed lines = sum of `(line_end - line_start + 1)` for 10 FIGUREs = **194 lines**
- De-figure adjusted denominator = 344 − 194 + 10 (replace fig lines with 10 atoms) = **160 lines**
- De-figure ratio = 113 / 160 = **0.706**
- **0.706 ∈ [0.59, 0.85] band — IN BAND**

Conclusion: writer's de-figure heuristic underestimated FIGURE absorption (used 120L vs actual 194L). When properly computed, slice A is in band. Naive 0.328 outlier is purely the FIGURE-heavy nature (194/344 = 56% of slice is mermaid). No atom is missing or merged incorrectly.

### Recommendation

- INFO finding (non-blocking) — carry forward to round 12 mini-audit + v1.9.4 §F-3 codification candidate
- Potential v1.9.4 patch: codify de-figure ratio formula `113 / (total_lines − Σ(fig.line_end − fig.line_start + 1) + N_figures)` to replace heuristic estimate
- Aggregate evaluation across 3 TA/ex slices (batch_123 + 124 + 125) at round-close mini-audit; combined ratio likely well within band

---

## §5 §2.6 FIGURE byte-exact spot-check

**All 10 FIGURE atoms verified byte-exact against source.**

| atom_id | line range | source bytes | atom bytes | match | open `\`\`\`mermaid` | close `\`\`\` ` | verdict |
|---------|-----------|------|-----------|-------|---------|---------|---------|
| a018 | L24-L35 | 375 | 375 | ✓ | ✓ | ✓ | PASS |
| a020 | L39-L56 | 293 | 293 | ✓ | ✓ | ✓ | PASS |
| a022 | L60-L80 | 384 | 384 | ✓ | ✓ | ✓ | PASS |
| a024 | L84-L96 | 229 | 229 | ✓ | ✓ | ✓ | PASS |
| a045 | L126-L133 | 374 | 374 | ✓ | ✓ | ✓ | PASS |
| a047 | L137-L177 | 856 | 856 | ✓ | ✓ | ✓ | PASS |
| a052 | L185-L209 | 460 | 460 | ✓ | ✓ | ✓ | PASS |
| a086 | L251-L265 | 476 | 476 | ✓ | ✓ | ✓ | PASS |
| a088 | L269-L293 | 494 | 494 | ✓ | ✓ | ✓ | PASS |
| a093 | L301-L316 | 278 | 278 | ✓ | ✓ | ✓ | PASS |

**FIGURE byte-exact: 10/10 PASS** (sampled 3 in audit + verified all 10 for completeness).

---

## §6 Halt-condition check (no halts triggered)

- Overall PASS rate < 90%: NO (100.00% ≥ 90%)
- FIGURE byte-exact mismatch: NO (10/10 PASS)
- §2.5 numbered-H2 parent_section drift: NO (a013/a041/a081 all parent §TA file-root + sib=1/2/3)
- Schema regression / atom_id collision: NO (113 unique a001-a113 + all 12 fields explicit)
- §F-1 §2.11 Plan B trigger: N/A (slice A 0 numberless H2 with H3 children)
- Hook 22b/22c grep verify: trusted from kickoff
- Rule D writer ≠ reviewer subagent_type: ✓ (writer=general-purpose / reviewer=executor)

---

## DONE Marker

REVIEWER_123_DONE pass_rate=100.00%_12_of_12 dim_verbatim=12/12 dim_schema=12/12 dim_parent_section=12/12 dim_hooks=12/12 figure_byte_exact=10/10 findings_HIGH=0 findings_MED=0 findings_LOW=1 f2_verdict=source_outlier
