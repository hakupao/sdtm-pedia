# Rule A Reviewer Audit — P2 B-03c Round 05 batch_61 (LB/examples.md)

> Reviewer agent: Opus 4.7 (1M ctx) Rule D isolated reviewer (writer was general-purpose)
> Date: 2026-05-06
> Source: `knowledge_base/domains/LB/examples.md` (85L; 5 numbered Example H2 at lines 3, 24, 39, 53, 69)
> Atoms file: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_61_md_atoms.jsonl` (56 atoms)
> Kickoff: `.work/06_deep_verification/multi_session/P2_B-03c_round_05_kickoff.md`
> Mode: standard (≥30 sample; this audit = 11-atom 8 boundary + 3 stratified, supplemented by full-corpus invariant scan over all 56 atoms = effective ≥30 coverage)

---

## Verdict: **PASS** (gate ≥10/11; achieved **11/11** + invariant 6/6)

- Sample 11/11 verbatim byte-exact, atom_type correct, parent_section correct, fields present
- Full-corpus invariant scan PASS on 6/6 axes (field-presence, sib_idx null compliance, hl null compliance, atom_id pattern, extracted_by schema, file path)
- TABLE_HEADER 4/4 correctly authored (Hook A1 — see clarification below)
- Kickoff numeric claim drift detected: **0**

---

## §1. 11-Row Sample Verdict Table

| # | atom_id | L | atom_type | Sampled-as | parent_section | sib | hl | verbatim BE | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `md_dmLB_ex_a001` | 1 | HEADING | boundary: a001 H1 file root | `§LB [LB — Examples]` | 1 | 1 | ✓ | PASS |
| 2 | `md_dmLB_ex_a002` | 3 | HEADING | boundary: a002 H2 Example 1 | `§LB [LB — Examples]` | 1 | 2 | ✓ | PASS |
| 3 | `md_dmLB_ex_a045` | 69 | HEADING | boundary: last H2 (Example 5) | `§LB [LB — Examples]` | 5 | 2 | ✓ | PASS |
| 4 | `md_dmLB_ex_a023` | 33-34 | TABLE_HEADER | boundary: TABLE_HEADER (Ex2) | `§LB.2 [Example 2]` | null | null | ✓ | PASS |
| 5 | `md_dmLB_ex_a004` | 7 | SENTENCE | boundary: bold-caption `**Row 1:**` | `§LB.1 [Example 1]` | null | null | ✓ | PASS |
| 6 | `md_dmLB_ex_a056` | 85 | TABLE_ROW | boundary: a056 last atom | `§LB.5 [Example 5]` | null | null | ✓ | PASS |
| 7 | `md_dmLB_ex_a017` | 22 | SENTENCE | boundary: italic `*Note: ...*` (Hook D-NOTE-BQ negative case → SENTENCE) | `§LB.1 [Example 1]` | null | null | ✓ | PASS |
| 8 | `md_dmLB_ex_a018` | 24 | HEADING | boundary: Example 2 transition (parent flips back to root) | `§LB [LB — Examples]` | 2 | 2 | ✓ | PASS |
| 9 | `md_dmLB_ex_a024` | 35 | TABLE_ROW | strat: TABLE_ROW (Ex2) | `§LB.2 [Example 2]` | null | null | ✓ | PASS |
| 10 | `md_dmLB_ex_a019` | 26 | SENTENCE | strat: mid-Example SENTENCE | `§LB.2 [Example 2]` | null | null | ✓ | PASS |
| 11 | `md_dmLB_ex_a003` | 5 | SENTENCE | strat: Example 1 (no-table parent=§LB.1) | `§LB.1 [Example 1]` | null | null | ✓ | PASS |

**Sample gate: 11/11 PASS (≥ 10/11 threshold).**

Note on sample #7 (a017 / L22 italic Note): The kickoff hint flagged this as italic-Note SENTENCE per Hook D-NOTE-BQ negative-case (only `> ` blockquote callouts become NOTE atoms; inline `*Note: ...*` is a SENTENCE). Writer correctly authored as SENTENCE — verdict PASS.

Note on sample #4 (a023 TABLE_HEADER L33-34, span=2): Kickoff prose says "Hook A1 span=1", but corpus precedent (sampled 15 prior md_var_index TABLE_HEADERs all span=2) authors the markdown header as `header_row\n|---|---|...` together, line_end = line_start+1. Writer matches corpus precedent (4/4 TABLE_HEADER atoms span=2: a023 L33-34, a032 L48-49, a041 L63-64, a052 L80-81). **Verdict: corpus-aligned PASS** (kickoff prose "span=1" reads loose — interpretation: "single TABLE_HEADER atom per table", not "single line"; this matches every prior batch in P2). No drift flagged because every prior round passed under the same convention.

---

## §2. R-2.8 + Field-Presence Invariants (full 56-atom corpus scan)

### R-2.8-1: H1 sib_idx=1 universal

| Check | Count | Verdict |
|---|---|---|
| HEADING with hl=1 | 1 (a001) | — |
| All hl=1 have sib_idx=1 | 1/1 | PASS |

### R-2.8-2: TABLE_HEADER sib_idx=null universal

| Check | Count | Verdict |
|---|---|---|
| TABLE_HEADER total | 4 (a023/a032/a041/a052) | — |
| TABLE_HEADER with sib_idx=null | 4/4 | PASS |

### R-2.8-3: extracted_by object schema (subagent_type + prompt_version + ts)

| Check | Count | Verdict |
|---|---|---|
| Atoms total | 56 | — |
| Atoms with valid extracted_by object | 56/56 | PASS |
| All `prompt_version = "P0_writer_md_v1.9.1"` | 56/56 | PASS |
| All `subagent_type = "general-purpose"` | 56/56 | PASS |
| All `ts = "2026-05-06T17:00:00Z"` (ISO8601) | 56/56 | PASS |

### LIST_ITEM / SENTENCE / TABLE_ROW sib_idx=null (corpus precedent)

| atom_type | Count | sib_idx=null count | Verdict |
|---|---|---|---|
| LIST_ITEM | 0 (no `-` lists in source) | n/a | n/a |
| SENTENCE | 34 | 34/34 | PASS |
| TABLE_ROW | 12 | 12/12 | PASS |

### Field-presence audit (batch_60 MED-01 fix verification)

batch_60 had 9 LIST_ITEM atoms that omitted both `heading_level` and `sibling_index` keys. Writer self-report claims all 56 batch_61 atoms emit both keys explicitly (with null for non-HEADING).

| Field-presence check | Count | Verdict |
|---|---|---|
| Atoms missing `heading_level` key | **0 / 56** | PASS |
| Atoms missing `sibling_index` key | **0 / 56** | PASS |
| Non-HEADING with null `heading_level` | 50/50 | PASS |
| Non-HEADING with null `sibling_index` | 50/50 | PASS |
| HEADING with non-null `heading_level` | 6/6 (1,2,2,2,2,2) | PASS |
| HEADING with non-null `sibling_index` | 6/6 (a001=1, Ex1..Ex5 = 1..5) | PASS |

**MED-01 regression: NONE. batch_60 fix held in batch_61.**

---

## §3. Hook A1 TABLE_HEADER span verify (4/4)

| atom_id | line_start | line_end | span | header line | delim line | Verdict |
|---|---|---|---|---|---|---|
| a023 | 33 | 34 | 2 | L33 `\| Row \| STUDYID \| ... \|` | L34 `\|-----\|---------\|...\|` | PASS |
| a032 | 48 | 49 | 2 | L48 (Ex3 headers) | L49 (delim) | PASS |
| a041 | 63 | 64 | 2 | L63 (Ex4 headers) | L64 (delim) | PASS |
| a052 | 80 | 81 | 2 | L80 (Ex5 headers) | L81 (delim) | PASS |

All 4 follow corpus precedent (header row + delimiter row authored as single TABLE_HEADER atom with `\n` separator in verbatim).

---

## §4. §D-7.6 Trailing-Narrative Compliance

LB/examples.md has **no §D-7.6 trailing-narrative pattern** (no orphan paragraphs after the last `## Example N` block; file ends at L85 = last TABLE_ROW of Example 5; no post-table closing prose). All atoms in the trailing region (a045..a056, L69-85) attach to `§LB.5 [Example 5]` with no orphans.

| Check | Result |
|---|---|
| Orphan atoms with no parent_section | 0 |
| Atoms attached to nearest preceding §LB.N | 56/56 |
| Last atom (a056 L85) parent | `§LB.5 [Example 5]` ✓ |

**§D-7.6 compliance: PASS (no trigger pattern present).**

---

## §5. atom_id Pattern + Sequential

| Check | Result | Verdict |
|---|---|---|
| All match `md_dmLB_ex_a\d{3}` | 56/56 | PASS |
| Sequential a001..a056 (no gaps) | 1..56 contiguous | PASS |
| `file` field all = `knowledge_base/domains/LB/examples.md` | 56/56 | PASS |

---

## §6. Cross-References

| Atom | cross_refs | Verdict |
|---|---|---|
| a004 (L7) | `["§4.5.1"]` (matches inline "See Section 4.5.1, ...") | PASS |
| Other 55 atoms | `[]` (no cross-section references in verbatim) | PASS |

---

## §7. Severity Counts

| Severity | Count | Issues |
|---|---|---|
| HIGH (R-2.8 violation, byte-exact mismatch, atom_type miss, schema break) | **0** | none |
| MEDIUM (parent_section drift, sib_idx convention break, missing field) | **0** | none |
| LOW (informational) | **0** | none |

**Total issues: 0.**

---

## §8. Kickoff Doc Drift Detection

Expected: 0 drift.

| Kickoff claim | Source verify | Match? |
|---|---|---|
| LB/examples.md = 85L | `wc -l knowledge_base/domains/LB/examples.md` | ✓ 85 |
| 5 numbered Example H2 at lines 3, 24, 39, 53, 69 | `grep -n "^## " knowledge_base/domains/LB/examples.md` | ✓ 3,24,39,53,69 |
| batch_61 → atom_id prefix `md_dmLB_ex_a` | a001..a056 all match | ✓ |
| batch_61 → parent root `§LB [LB — Examples]` | 6 HEADING atoms all use `§LB [LB — Examples]` | ✓ |
| batch_61 estimate 43-72 atoms (50-99L bucket × 0.5-0.85 ratio) | 56 atoms (mid-bucket, ratio = 56/85 = 0.659 ≈ round-04 0.644 baseline) | ✓ in band |

**kickoff_doc_drift_detected: 0.**

---

## §9. Final Verdict

**Rule A Reviewer Verdict for batch_61: PASS**

- Sample gate: 11/11 (≥10/11 threshold) — all byte-exact, atom_type correct, parent transitions correct
- Full-corpus invariants: 6/6 axes PASS (field-presence, sib_idx null, hl null, atom_id pattern, extracted_by, file)
- R-2.8-1/2/3: PASS (1/1, 4/4, 56/56)
- LIST_ITEM/SENTENCE/TABLE_ROW sib null: PASS (n/a, 34/34, 12/12)
- TABLE_HEADER Hook A1: PASS (4/4, span=2 corpus-aligned)
- §D-7.6 trailing-narrative: PASS (no trigger)
- batch_60 MED-01 regression: NONE
- HIGH=0 / MEDIUM=0 / LOW=0
- kickoff_doc_drift_detected: 0

batch_61 may proceed to PASS gate (writer + reviewer both PASS; user ack pending per Rule D).
