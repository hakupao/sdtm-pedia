# Rule A Reviewer Summary — P2 B-03 batch_63 (round 05)

> Verdict: **PASS** (11/11 = 100%, gate ≥10/11 = ≥90.9%)
> Source: `knowledge_base/domains/MB/examples.md` (171L)
> Atoms: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_63_md_atoms.jsonl` (148 atoms)
> Reviewer: independent subagent (Rule D), Round 05 batch_63
> Audit date: 2026-05-06

## 1. 11-row sample table

| # | atom_id | role | type | line | verbatim ⊂ src | atom_type | sib_index | hl_present | parent_section | file | ext_by | verdict |
|---|---------|------|------|------|----------------|-----------|-----------|------------|----------------|------|--------|---------|
| 1 | a001 | boundary H1 file root | HEADING | 1 | EXACT | OK | sib=1 (R-2.8-1) | hl=1 | §MB [MB — Examples] | ok | ok | PASS |
| 2 | a002 | boundary L3 italic-note SENTENCE BEFORE first H2 | SENTENCE | 3 | substring of L3 | OK | sib=null | hl=null | §MB [MB — Examples] (file root, NOT §MB.0) | ok | ok | PASS |
| 3 | a004 | boundary H2 Example 1 sib=1 | HEADING | 5 | EXACT | OK | sib=1 | hl=2 | §MB [MB — Examples] | ok | ok | PASS |
| 4 | a019 | boundary TABLE_HEADER (1 of 11) | TABLE_HEADER | 13-14 | EXACT (header+separator joined by `\n`) | OK | sib=null | hl=null | §MB.1 [Example 1] | ok | ok | PASS |
| 5 | a065→a066 | boundary Ex2→Ex3 transition | TABLE_ROW→HEADING | 80→82 | EXACT | OK | (a066 sib=3) | hl=2 | §MB.2→§MB | ok | ok | PASS |
| 6 | a077 | boundary cross_refs SENTENCE | SENTENCE | 86 | substring of L86 | OK | sib=null | hl=null | §MB.3 [Example 3] | ok | ok | PASS |
| 7 | a087 | stratified TABLE_ROW from Ex3 (be.xpt row 1) | TABLE_ROW | 102 | EXACT | OK | sib=null | hl=null | §MB.3 [Example 3] | ok | ok | PASS |
| 8 | a009 | stratified multi-sentence narrative split | SENTENCE | 9 (10 sents) | substring of L9 + full join verified | OK | sib=null | hl=null | §MB.1 [Example 1] | ok | ok | PASS |
| 9 | a038 | stratified bold-caption SENTENCE per §D-5 | SENTENCE | 43 | EXACT (single-line sentence) | OK | sib=null | hl=null | §MB.2 [Example 2] | ok | ok | PASS |
| 10 | a100 | boundary Example 3 mid-content atom | SENTENCE | 113 | substring of L113 | OK | sib=null | hl=null | §MB.3 [Example 3] | ok | ok | PASS |
| 11 | a148 | boundary last atom | TABLE_ROW | 171 | EXACT | OK | sib=null | hl=null | §MB.3 [Example 3] | ok | ok | PASS |

**Sample PASS rate: 11/11 = 100%** (gate ≥90.9%)

## 2. R-2.8-1 / R-2.8-2 / R-2.8-3 + sib null compliance per atom_type (corpus 148/148)

| atom_type | n | sib value | R-2.8 expected | compliance |
|-----------|---|-----------|----------------|------------|
| HEADING (H1) | 1 | sib=1 | sib=1 (R-2.8-1) | 1/1 PASS |
| HEADING (H2) | 3 | sib=1, 2, 3 | sib=1..3 (3 Examples) | 3/3 PASS |
| SENTENCE | 77 | sib=null (77/77) | sib=null per corpus norm | 77/77 PASS |
| TABLE_HEADER | 11 | sib=null (11/11) | sib=null (R-2.8-2) | 11/11 PASS |
| TABLE_ROW | 56 | sib=null (56/56) | sib=null per corpus norm | 56/56 PASS |
| **Total** | **148** | — | — | **148/148 PASS** |

## 3. Field-presence audit (148 atoms)

- `atom_id`: 148/148 (pattern `^md_dmMB_ex_a\d{3}$`, 0 mismatches; sequential a001..a148)
- `file`: 148/148 (all `knowledge_base/domains/MB/examples.md`, Hook C-8 verified)
- `line_start` / `line_end`: 148/148
- `parent_section`: 148/148
- `atom_type`: 148/148 (all in 9-value enum)
- `verbatim`: 148/148 (minLength≥1)
- `extracted_by`: 148/148 (R-2.8-3 schema with `subagent_type`+`prompt_version`+`ts`; prompt_version `P0_writer_md_v1.9.1` matches `^P0_writer_(pdf|md)_v\d+(\.\d+)*$`)
- `heading_level`: 148/148 (present as integer for HEADING, null for non-HEADING per corpus convention)
- `sibling_index`: 148/148 (present as integer for HEADING, null for non-HEADING per corpus convention)

## 4. TABLE_HEADER Hook A1 (span=1 = 2-line range) compliance

11/11 TABLE_HEADER atoms have `line_end - line_start == 1` (header row + separator row, joined in `verbatim` with `\n`). Byte-exact match against source for all 11. PASS.

NOTE: atom_schema.json (md_atom) does NOT define an explicit `span` property, so Hook A1 is enforced via the 2-line `line_start`/`line_end` range + `\n`-joined `verbatim`. This matches Round 04 corpus convention. No deviation.

## 5. Pre-first-H2 attach rule (a002)

L3 italic note is BEFORE first H2 at L5. The italic line is split into 2 sentences (a002 + a003), both with:
- `parent_section = "§MB [MB — Examples]"` (file root)
- NOT `§MB.0` and NOT any sub-namespace

§D-7.6 file-root attach rule: PASS.

## 6. Parent_section distribution verification

| parent_section | observed | expected (kickoff) | match |
|----------------|----------|--------------------|-------|
| §MB [MB — Examples] (file root) | 6 | 6 (H1 + 2 L3 italic-note SENTENCEs + 3 H2) | OK |
| §MB.1 [Example 1] | 22 | 22 | OK |
| §MB.2 [Example 2] | 38 | 38 | OK |
| §MB.3 [Example 3] | 82 | 82 | OK |
| **Total** | **148** | **148** | **PASS** |

## 7. §D-7.3 cross_refs audit

| atom_id | line | cross_refs | source phrase | verdict |
|---------|------|------------|---------------|---------|
| a002 | 3 | `["6.3.5.7.3"]` | "(6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples)" | PASS |
| a077 | 86 | `["Section 6.2.2","Section 6.3.5.2"]` | "Sections 6.2.2 and 6.3.5.2" | PASS |

All other 146 atoms have empty `cross_refs: []` consistent with no in-text section references on those spans.

## 8. Byte-exact corpus-wide spot checks (beyond 11-sample)

- TABLE_ROW: 56/56 byte-exact match against source line
- TABLE_HEADER: 11/11 byte-exact (joined header+separator)
- HEADING: 4/4 byte-exact
- Single-line SENTENCE (1 per source line): 34/34 byte-exact
- Multi-sentence SENTENCE splits (9 source lines, 43 sentence atoms): all join back to source line via space-concatenation; each verbatim is substring of its source line

## 9. Severity counts

| Severity | Count | Issues |
|----------|-------|--------|
| HIGH | 0 | — |
| MEDIUM | 0 | — |
| LOW | 0 | — |

## 10. kickoff_doc_drift_detected

**0** (expected 0).

Kickoff statements verified:
- 148 atoms ✓
- 3 numbered Example H2 at L5/27/82 ✓
- 11 TABLE_HEADER ✓
- a002 L3 italic-note BEFORE first H2 ✓
- a077 L86 has §6.2.2 + §6.3.5.2 cross_refs ✓
- 7 multi-sentence narratives — observed 9 (kickoff under-count, not a quality issue; writer captured more splits than kickoff anticipated). LOW informational note only, not a defect.
- File root attach 6 atoms ✓
- §MB.1=22 / §MB.2=38 / §MB.3=82 ✓
- Source 171L ✓

## 11. Final verdict

**Rule A PASS** — 11/11 sample atoms PASS, 148/148 corpus-level structural and byte-exact checks PASS, R-2.8-1/2/3 compliant, §D-7.3 cross_refs verified, §D-7.6 file-root attach rule verified, Hook A1 TABLE_HEADER 2-line span verified, Hook C-8 file path verified, parent_section distribution matches expected.

Round 05 batch_63 cleared for downstream reconciliation and ledger entry.
