# Rule A Verdict — P2 B-03c batch_103

> Round 09 batch_103 (LAST batch of round 09); v1.9.2 baseline 3rd round; §2.5 numbered H2 self-namespace × 2 cases.

## Inputs

- **Source**: `knowledge_base/domains/SE/examples.md` (82 lines)
- **Writer output**: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_103_md_atoms.jsonl` (50 atoms, a001–a050)

## Source grep cross-verify

| Metric | Expected | Actual | OK |
|---|---|---|---|
| `wc -l` | 82 | 82 | YES |
| `## ` count | 2 | 2 | YES |
| `### ` count | 0 | 0 | YES |

## Sample (8 boundary + 3 stratified = 11)

| atom_id | line | type | sample category | verdict |
|---|---|---|---|---|
| a001 | L1 | HEADING h1 | boundary (H1 root) | PASS |
| a002 | L3 | SENTENCE | boundary (L3 file-root intro before any H2) | PASS |
| a003 | L5 | HEADING h2 sib=1 | boundary (H2 self-namespace anchor #1) | PASS |
| a004 | L7 | SENTENCE | stratified (H2 child) | PASS |
| a012 | L23-24 | TABLE_HEADER | boundary (TH #1, Hook A1) | PASS |
| a013 | L25 | TABLE_ROW | stratified | PASS |
| a027 | L44-45 | TABLE_HEADER | boundary (TH #2, Hook A1) | PASS |
| a031 | L50 | HEADING h2 sib=2 | boundary (H2 self-namespace anchor #2) | PASS |
| a032 | L52 | SENTENCE | stratified (Example 2 child) | PASS |
| a038 | L64-65 | TABLE_HEADER | boundary (TH #3, Hook A1) | PASS |
| a048 | L79-80 | TABLE_HEADER | boundary (TH #4, Hook A1) | PASS |
| a050 | L82 | TABLE_ROW | boundary (last atom) | PASS |

(12 atoms verified — exceeds 11-sample minimum to capture all 4 TABLE_HEADERs.)

## §2.5 numbered-H2 self-namespace verification (critical)

| Constraint | Check | Result |
|---|---|---|
| L1 H1 | parent=`§SE [SE — Examples]` hl=1 sib=1 | PASS |
| L3 intro (pre-H2) | parent=`§SE [SE — Examples]` (NOT §SE.1) | PASS — §2.5 file-root pre-H2 case correct |
| L5 H2 (sib=1) | parent=`§SE [SE — Examples]` hl=2 sib=1 | PASS — H2 itself parents to root |
| L7-L48 children | parent=`§SE.1 [Example 1]` | PASS — children use self-namespace |
| L50 H2 (sib=2) | parent=`§SE [SE — Examples]` hl=2 sib=2 | PASS — sib increments, parents to root |
| L52-L82 children | parent=`§SE.2 [Example 2]` | PASS — children use self-namespace |

Spot-checked broader population beyond the 11-sample boundary set: a005-a011, a014-a026, a028-a030 all parent=§SE.1 (Example 1 scope L7-L48); a033-a047, a049 all parent=§SE.2 (Example 2 scope L52-L82). No leakage.

## Hook A1 (TABLE_HEADER 2-row span)

All 4 TABLE_HEADER atoms (a012, a027, a038, a048) have `line_end - line_start = 1` (2-row span: column header row + delimiter row). PASS universal.

## §E-rule sweep

- **§E-1 schema regression**: PASS (12/12 fields exact in all atoms; no extras, no missing)
- **§E-2 H1 hl=1 sib=1**: PASS (a001)
- **§E-3 TABLE_HEADER sib=null**: PASS (a012/a027/a038/a048 all sib=null)
- **§E-4 extracted_by object**: PASS (all 50 atoms carry full subagent_type + prompt_version=P0_writer_md_v1.9.2 + ts)
- **§E-5 non-HEADING explicit hl=null sib=null**: PASS (literal nulls, not omitted)

## Sequence + verbatim

- atom_id sequence a001…a050 contiguous (50 atoms, no gaps, no duplicates) — PASS
- Verbatim byte-exact spot checks (a001 L1, a002 L3, a013 L25, a050 L82) all match source byte-for-byte — PASS

## Verdict

```
RULE_A_BATCH_103: PASS raw=11/11 pct=100% halt=no
```

(Reported per the spec's 11-sample N; 12th atom a012 was an extra confirm of Hook A1 universality. No halt triggers fired: §E-1 clean / verbatim clean / §2.5 sub-namespace correct in both directions / L3 file-root parent correct / TABLE_HEADER sib=null universal.)

## Round 09 closure note

This is the final batch of round 09. Combined with prior round-09 batches, this confirms v1.9.2 §2.5 numbered-H2 self-namespace contract holds across the 2nd round of sustained validation, including the boundary case where pre-first-H2 file-root content (L3 intro) must NOT bleed into §SE.1.
