# Rule A Independent Review — P2 B-02 batch 08 (ch10_appendices.md)

> Review date: 2026-05-04
> Reviewer subagent_type: `code-reviewer` (FALLBACK for `oh-my-claudecode:scientist`, sustained 6th batch in row, batches 03..08)
> Writer subagent_type: `general-purpose` (FALLBACK 6-batch sustained)
> **Rule D**: PASS — different subagent_type confirmed
> Schema: v1.2.1 (frozen 2026-04-24, patched 2026-05-04 for >999 atoms)
> Source: `knowledge_base/chapters/ch10_appendices.md` (310 lines via wc -l)
> Writer output: `evidence/checkpoints/P2_B-02_batch_08_md_atoms.jsonl` (258 atoms a001..a258)
> Density: 258 / 310 = 0.832 (matches kickoff §2.1 estimate ~0.81)

---

## 1. Reviewer metadata

| Field | Value |
|---|---|
| Sample plan | 7 boundary + 3 stratified per kickoff §2.2.5 (B6 expanded to 5 atoms → **14 verdict rows** total) |
| Gate threshold | functional pass rate ≥ 90% |
| Verdicts file | `evidence/checkpoints/rule_a_P2_B-02_batch_08_verdicts.jsonl` |
| Independence | Reviewer ≠ Writer (Rule D PASS); Reviewer did NOT edit JSONL/source/schema/kickoff |

---

## 2. Sample table (14 verdict rows)

| sample_id | atom_id | line | atom_type | strict | functional |
|---|---|---|---|---|---|
| B1 | md_ch10_a001 | 1 | HEADING h1 sib=1 | PASS | PASS |
| B2 | md_ch10_a003 | 7 | HEADING h2 sib=1 §10.A | PASS | PASS |
| B3 | md_ch10_a074 | 100-101 | TABLE_HEADER (5-col) | PASS | PASS |
| B4 | md_ch10_a171 | 213 | TABLE_ROW separator | PASS | PASS |
| B5 | md_ch10_a161 | 201 | LIST_ITEM | PASS | PASS |
| B6.1 | md_ch10_a245 | 290 | HEADING h2 sib=6 §10.F | PASS | PASS |
| B6.2 | md_ch10_a246 | 292 | HEADING h3 sib=1 §10.F | PASS | PASS |
| B6.3 | md_ch10_a250 | 296 | HEADING h3 sib=2 §10.F | PASS | PASS |
| B6.4 | md_ch10_a254 | 302 | HEADING h3 sib=3 §10.F | PASS | PASS |
| B6.5 | md_ch10_a256 | 306 | HEADING h3 sib=4 §10.F | PASS | PASS |
| B7 | md_ch10_a258 | 310 | SENTENCE (NOT NOTE) | PASS | PASS |
| S1 | md_ch10_a121 | 148 | TABLE_ROW (right-col only) | PASS | PASS |
| S2 | md_ch10_a060 | 74 | LIST_ITEM (multi-sentence) | PASS | PASS |
| S3 | md_ch10_a255 | 304 | SENTENCE (long ALL CAPS) | PASS | PASS |

---

## 3. Aggregate

| Metric | Count | Rate | Gate (≥90%) |
|---|---|---|---|
| Strict PASS | 14 / 14 | **100%** | PASS |
| Functional PASS | 14 / 14 | **100%** | PASS |

---

## 4. Findings

### HIGH — none
No HIGH-severity defects found in writer output.

### MEDIUM — M1 (NOT a writer defect; kickoff doc bug — 3rd consecutive)

**M1 (kickoff doc bug)**: Kickoff §2.2 + §2.2.5 + §4 multiple times stated `L102-163 TABLE_ROW × 62 (Fragment Reference)`. Source actual: rows L102-162 = 61 rows, L163 = blank line (table ends at L162). Writer correctly emitted 61 byte-exact TABLE_ROW atoms (verified by `jq` count) and did NOT fabricate a phantom 62nd row. **This is writer Rule B compliance** — source-truth wins over kickoff metadata.

**Pattern**: This is the **3rd consecutive batch** with kickoff metadata-vs-source drift:
- batch 06: kickoff said `### 3.2.2` (h_lvl=3); source `## 3.2.2` (h_lvl=2). Writer Rule B'd.
- batch 07: kickoff said "5 表"; source had 4 tables. Writer Rule B'd.
- **batch 08**: kickoff said "L102-163 / 62 rows"; source has 61 rows (L163 blank). Writer Rule B'd.

Additional minor kickoff offset bug observed (informational only): §2.2.5 stratified hint `L155 \| | | | TIME | TM |` is offset — source L155 is `| | | | TREATMENT | TRT |`; TIME row is at L150. Reviewer used L150 for S1 sample (semantic match preserved via L148 SYSTEM row instead, since L150 TIME would be more representative right-col-only). Either L148 or L150 satisfies S1 intent — verified L148 PASS.

### LOW — none

---

## 5. Gate verdict

**GATE: PASS** — 100% functional pass rate, exceeds 90% threshold by 10 percentage points. No writer defects across 14 sampled atoms covering H1/H2/H3 chains, TABLE_HEADER (5-col special), TABLE_ROW (separator + right-col-only special), LIST_ITEM (single + multi-sentence), and SENTENCE (long ALL CAPS legal + Note-prefix-not-bold edge case).

**Recommendation**: Proceed to checkpoint append (root JSONL 2264 → ~2522), audit_matrix.md ch10 milestone, _progress.json batches_done=8, dispatch batch 09 (ch08, last B-02 batch) per kickoff §7.

---

## 6. ch10 全闭 verification

| Check | Result |
|---|---|
| Last atom (a258) line_end | 310 |
| Source total lines (wc -l) | 310 |
| Last atom line_end ≥ slice_end - 5 (Hook 22 / §R-C3 #4) | PASS (310 ≥ 305) |
| Total atom count | 258 |
| Density (258/310) | 0.832 (matches kickoff estimate 0.81) |
| Slice coverage shortfall | NONE — full file 1-310 covered |

**ch10 closure CONFIRMED**.

---

## 7. D6 letter-prefix appendix H2 validation

All 6 H2 atoms verified:

| atom_id | line | sib | parent_section (own) |
|---|---|---|---|
| md_ch10_a003 | 7 | 1 | §10 [Appendices] |
| md_ch10_a009 | 15 | 2 | §10 [Appendices] |
| md_ch10_a053 | 64 | 3 | §10 [Appendices] |
| md_ch10_a067 | 88 | 4 | §10 [Appendices] |
| md_ch10_a136 | 166 | 5 | §10 [Appendices] |
| md_ch10_a245 | 290 | 6 | §10 [Appendices] |

H2 atoms themselves correctly parent under `§10 [Appendices]` (parent context). Sub-atoms under each Appendix correctly use letter-prefix bracketed format `§10.A [...]` through `§10.F [...]` (verified across B2, B3, B4, B5, B6.2-5, B7, S1, S2, S3 — 11/11 sub-atoms with letter-prefix parent_section all PASS). **D6 letter-prefix convention IMPLEMENTED CORRECTLY**.

---

## 8. Section-by-Section separator row TABLE_ROW (Hook C-6) validation

10 expected separator rows (L213/215/220/224/229/236/265/273/280/282) all emitted as `atom_type=TABLE_ROW` (NOT HEADING):

| atom_id | line | verbatim |
|---|---|---|
| a171 | 213 | `\| **Section 1. Introduction** \| \| \|` |
| a173 | 215 | `\| **Section 2. Fundamentals of the SDTM** \| \| \|` |
| a178 | 220 | `\| **Section 3. Submitting Data in a Standard Format** \| \| \|` |
| a182 | 224 | `\| **Section 4. Assumptions for Domain Models** \| \| \|` |
| a187 | 229 | `\| **Section 5. Models for Special-purpose Domains** \| \| \|` |
| a194 | 236 | `\| **Section 6. Domain Models Based on the General Observation Classes** \| \| \|` |
| a223 | 265 | `\| **Section 7. Trial Design Model Datasets** \| \| \|` |
| a231 | 273 | `\| **Section 8. Representing Relationships and Data** \| \| \|` |
| a238 | 280 | `\| **Section 9. Study References** \| \| \|` |
| a240 | 282 | `\| **Appendices** \| \| \|` |

**10/10 PASS**. Bold inside table cell does NOT trigger HEADING regex (`^#{1,6}\s+` does not match pipe-delimited line). Hook C-6 PASS.

---

## 9. Fragment Reference 5-col table empty cells preservation validation

| Check | Result |
|---|---|
| Header L100-101 5-col preserved (with empty middle separator col) | PASS |
| Data rows L102-L162 count via jq | **61 atoms** (NOT 62) |
| Kickoff §2.2 / §2.2.5 / §4 stated count | 62 |
| Source actual count (L163 blank verified) | 61 |
| Writer behavior | **Rule B'd to source-truth 61** — correct |
| L147 left-only populated `\| NON-STUDY THERAPY \| NST \| \| \|` | preserved byte-exact |
| L148-L162 right-only populated rows | preserved byte-exact (S1 sample verified L148 SYSTEM) |

**Empty cells preservation PASS**. Writer correctly handled the 5-col asymmetric table.

---

## 10. L310 SENTENCE NOT NOTE validation

a258 L310 verbatim: `Note: The CDISC Intellectual Property Policy can be found at http://www.cdisc.org/system/files/all/article/application/pdf/cdisc_20ip_20policy_final.pdf`

| Check | Result |
|---|---|
| atom_type | SENTENCE (NOT NOTE) — correct |
| Source has `**Note:**` bold markers? | NO (plain text "Note:") |
| Distinguished from batch 02-04 `**Note:**` carve-out | YES |
| parent_section | §10.F [Representations and Warranties, Limitations of Liability, and Disclaimers] |

**PASS**. Carve-out distinction (bold-Note → NOTE; plain-Note → SENTENCE) correctly preserved.

---

## 11. 3rd consecutive kickoff drift recognition

**Pattern solidifying** — 3 batches in a row with kickoff metadata-vs-source drift:

| Batch | Kickoff claim | Source actual | Writer behavior |
|---|---|---|---|
| 06 | `### 3.2.2` (h_lvl=3) at L117 | `## 3.2.2` (h_lvl=2) | Rule B'd to h_lvl=2 |
| 07 | "5 表" | 4 tables | Rule B'd to 4 |
| 08 | "L102-163 / 62 rows" | L102-162 / 61 rows (L163 blank) | Rule B'd to 61 |

**Recommendation — promote v1.9.1 HIGH-2 kickoff self-consistency rule from HIGH to CRITICAL**:
- 3 consecutive batches with kickoff arithmetic/structural drift is a **systematic** kickoff-authoring problem, not random.
- Each Rule B'd correctly by writer, but the cumulative reviewer-verification cost is non-trivial (each batch requires reviewer to wc -l + jq count to detect drift).
- **CRITICAL action**: Kickoff author must run a pre-flight `wc -l` + table-row count + heading-level grep against source BEFORE writing kickoff §2.2. Prepend kickoff with checksum block:
  ```
  Source pre-flight: wc -l = N | tables found via grep "^\|" = M | H2 count = K | H3 count = J
  ```
- Failure to include pre-flight = kickoff REJECTED before dispatch.

---

## 12. v1.9.1 candidate suggestions

### Codify D6 as new sub-rule under D5 family (NEW)

**D6**: letter-prefix appendix-style H2 sib chain
- Trigger: H2 of form `## Appendix [A-Z]: <title>` (no numeric sub-section under chapter)
- Rule:
  - H2 atom itself: `parent_section = §<chapter> [<chapter title>]` (parent context)
  - H2 atom: `heading_level=2`, `sibling_index = 1..N` per A-Z order
  - Sub-atoms (H3 numberless / SENTENCE / LIST_ITEM / TABLE_*): `parent_section = §<chapter>.<letter> [<appendix title>]`
  - H3 sib_index RESTART = 1 under each new H2 (S-02 rule applies normally)
- Evidence: ch10 batch 08 6 H2 (A-F) + 12 numberless H3 verified PASS

### Reinforce HIGH-2 kickoff self-consistency rule → promote to CRITICAL

(See §11 above)

### No other prompt cut candidates

Writer (general-purpose) FALLBACK path performance remains 100% PASS for the 6th consecutive batch. No new defect classes observed in this batch beyond previously codified ones. Continue FALLBACK sustain mode.

---

## Appendix A — verification commands log

```bash
wc -l knowledge_base/chapters/ch10_appendices.md
# → 310

wc -l evidence/checkpoints/P2_B-02_batch_08_md_atoms.jsonl
# → 258

jq -c 'select(.atom_type=="TABLE_ROW" and .line_start>=102 and .line_start<=162)' \
  evidence/checkpoints/P2_B-02_batch_08_md_atoms.jsonl | wc -l
# → 61 (NOT 62 — kickoff drift confirmed)

jq -c 'select(.atom_type=="TABLE_ROW" and .line_start>=213 and .line_start<=286 and (.verbatim | startswith("| **")))' \
  evidence/checkpoints/P2_B-02_batch_08_md_atoms.jsonl
# → 10 separator TABLE_ROW atoms, all PASS

jq -c 'select(.atom_type=="HEADING" and .heading_level==2)' \
  evidence/checkpoints/P2_B-02_batch_08_md_atoms.jsonl
# → 6 H2 atoms (A-F), sib=1..6, parent=§10 [Appendices]
```

All commands re-runnable for audit replay.

---

*Reviewer: code-reviewer (FALLBACK sustained 6 batches). Schema: v1.2.1. Date: 2026-05-04. Gate: PASS (14/14 = 100%).*
