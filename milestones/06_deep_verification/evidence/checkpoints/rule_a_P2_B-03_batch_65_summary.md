# Rule A Reviewer — P2 B-03c Round 05 batch_65 (MH/examples.md)

> Verdict: **PASS** (11/11 sample atoms PASS; gate ≥10/11)
> Source: `knowledge_base/domains/MH/examples.md` (109 lines, 1 H1 + 5 numbered Example H2 + 5 tables + 3 list items)
> Atom file: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_65_md_atoms.jsonl` (102 atoms)
> Schema: P0_writer_md_v1.9.1, R-2.8 / Hook A1 / Hook C-8 / §D-7.3
> kickoff_doc_drift_detected: **0**

## 1. Sample Verdict Table (8 boundary + 3 stratified = 11 atoms)

| # | atom_id | role | type | line | parent_section | sib | hl | verbatim | verdict |
|---|---------|------|------|------|----------------|-----|----|----------|---------|
| 1 | a001 | boundary: H1 root | HEADING | 1 | §MH [MH — Examples] | 1 | 1 | byte-exact `# MH — Examples` | PASS |
| 2 | a002 | boundary: H2 Example 1 (sib=1) | HEADING | 3 | §MH [MH — Examples] | 1 | 2 | byte-exact `## Example 1` | PASS |
| 3 | a012 | boundary: cross_refs §4.4.7 (Ex1) | SENTENCE | 7 | §MH.1 [Example 1] | null | null | byte-exact L7 fragment | PASS |
| 4 | a017 | stratified: bold-caption `**mh.xpt**` | SENTENCE | 11 | §MH.1 [Example 1] | null | null | byte-exact `**mh.xpt**` | PASS |
| 5 | a018 | boundary: TABLE_HEADER (Ex1) Hook A1 | TABLE_HEADER | 13–14 | §MH.1 [Example 1] | null | null | header+separator concatenated | PASS |
| 6 | a019 | stratified: TABLE_ROW (Ex1 row 1) | TABLE_ROW | 15 | §MH.1 [Example 1] | null | null | byte-exact L15 | PASS |
| 7 | a023 | boundary: last TABLE_ROW Ex1 | TABLE_ROW | 19 | §MH.1 [Example 1] | null | null | byte-exact L19 | PASS |
| 8 | a024 | boundary: parent transition Ex1→Ex2 | HEADING | 21 | §MH [MH — Examples] | 2 | 2 | byte-exact `## Example 2`; parent reverts to file root | PASS |
| 9 | a036 | boundary: cross_refs §4.4.7 (Ex2) | SENTENCE | 31 | §MH.2 [Example 2] | null | null | byte-exact L31 fragment | PASS |
|10 | a088 | boundary: last H2 Example 5 (sib=5) | HEADING | 90 | §MH [MH — Examples] | 5 | 2 | byte-exact `## Example 5` | PASS |
|11 | a102 | boundary: last atom of batch | TABLE_ROW | 109 | §MH.5 [Example 5] | null | null | byte-exact L109 | PASS |

LIST_ITEM stratified note: writer reports 3 LIST_ITEM atoms (a026/a027/a028 at L25/26/27). All inspected via jq: sib=null, parent §MH.2, verbatim begins with `- ` and matches source L25-27. Compliance verified within stratified pass.

## 2. R-2.8 Compliance per atom_type (R-2.8-1 / -2 / -3)

| atom_type | count | sib expected | sib actual | hl expected | hl actual | R-2.8 verdict |
|-----------|-------|--------------|------------|-------------|-----------|---------------|
| HEADING (H1) | 1 | 1 | 1 | 1 | 1 | PASS R-2.8-1 |
| HEADING (H2) | 5 | 1..5 sequential | 1,2,3,4,5 | 2 | 2 (×5) | PASS R-2.8-1 |
| SENTENCE | 57 | null | 57/57 null | null | null | PASS (corpus rule) |
| LIST_ITEM | 3 | null (round 03 lock) | 3/3 null | null | null | PASS round-03 lock |
| TABLE_HEADER | 5 | null | 5/5 null | null | null | PASS R-2.8-2 |
| TABLE_ROW | 31 | null | 31/31 null | null | null | PASS (corpus rule) |
| **total** | **102** | — | **0 violations** | — | — | **PASS** |

R-2.8-3 extracted_by schema: 102/102 atoms have `{subagent_type, prompt_version, ts}` keys — PASS.

## 3. Field-Presence Audit (heading_level + sibling_index on all 102 atoms)

- atoms missing `heading_level` field: **0 / 102**
- atoms missing `sibling_index` field: **0 / 102**
- field-presence: **102/102 PASS**

## 4. Hook A1 — TABLE_HEADER span Verify (5/5)

| atom | line_start | line_end | span (le−ls) | Hook A1 |
|------|-----------:|---------:|-------------:|---------|
| a018 | 13 | 14 | 1 | PASS |
| a044 | 39 | 40 | 1 | PASS |
| a063 | 60 | 61 | 1 | PASS |
| a083 | 83 | 84 | 1 | PASS |
| a098 | 104 | 105 | 1 | PASS |

5/5 PASS. Each TABLE_HEADER concatenates the header row + dash-separator row (verified verbatim on a018).

## 5. Parent_section Distribution vs Writer Claim

| parent_section | writer claim | actual | match |
|---|---:|---:|---|
| §MH [MH — Examples] (file root: 1 H1 + 5 H2) | 6 | 6 | PASS |
| §MH.1 [Example 1] | 21 | 21 | PASS |
| §MH.2 [Example 2] | 28 | 28 | PASS |
| §MH.3 [Example 3] | 20 | 20 | PASS |
| §MH.4 [Example 4] | 13 | 13 | PASS |
| §MH.5 [Example 5] | 14 | 14 | PASS |
| **total** | **102** | **102** | **PASS** |

6+21+28+20+13+14 = 102 — matches writer's distribution exactly.

## 6. §D-7.3 cross_refs Audit

| atom | cross_refs | source line | verdict |
|------|------------|------------:|---------|
| a012 | `["§4.4.7"]` | L7 (`See Section 4.4.7, Use of Relative Timing Variables, for further guidance.`) | PASS |
| a036 | `["§4.4.7"]` | L31 (same sentence, Ex2 context) | PASS |

Total cross_refs atoms in batch: 2 (a012 + a036). Both PASS §D-7.3 (canonical `§N.N.N` form, single-element array).

## 7. atom_id Sequence + Hook C-8 file path

- `atom_id` pattern `md_dmMH_ex_a\d{3}` sequential a001..a102: **PASS** (verified by sed+awk monotonic check, "sequence OK 1..102 (102 lines)")
- `file` field on every atom: `knowledge_base/domains/MH/examples.md` — Hook C-8 PASS (0/102 deviations)

## 8. Severity Counts

- HIGH: **0**
- MEDIUM: **0**
- LOW: **0**

No issues raised.

## 9. kickoff_doc_drift_detected

**0** — kickoff §4 counts (102 atoms / 109 lines / 5 H2 / 6 parent_section buckets / 6+21+28+20+13+14 distribution / 5 TABLE_HEADER / 3 LIST_ITEM / 2 cross_refs §4.4.7) all match actuals.

## 10. Final Verdict

**PASS — gate ≥10/11 (actual 11/11).**

All R-2.8-1/-2/-3 rules upheld. Hook A1 5/5 PASS. Parent_section distribution byte-aligned with writer claim (6/21/28/20/13/14=102). Field presence 102/102 on heading_level and sibling_index. Cross_refs canonical (§4.4.7 ×2). atom_id sequence contiguous a001..a102. No drift vs kickoff §4. Batch may CLOSE.

— Reviewer: code-reviewer (Opus 4.7), independent of writer subagent (Rule D PASS).
— Audit timestamp: 2026-05-06.
