# Rule A Verdict — P2 B-03c round 09 batch_101

## Inputs

- Source: `knowledge_base/domains/SC/examples.md` (49 lines)
- Writer output: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_101_md_atoms.jsonl` (32 atoms)
- Prompt baseline: P0_writer_md_v1.9.2 (3rd round, **§2.5 numbered H2 self-namespace × 3 cases**)

## Cross-verification (grep)

| Metric | Expected | Actual | Match |
|---|---|---|---|
| Source line count | 49 | `wc -l` = 49 | PASS |
| H2 count (`^## `) | 3 | `grep -c` = 3 | PASS |
| H3 count (`^### `) | 0 | `grep -c` = 0 | PASS |
| Atom count | 32 | `wc -l` jsonl = 32 | PASS |

## Sampling (8 boundary + 3 stratified = 11)

| atom_id | line(s) | role | sample type |
|---|---|---|---|
| a001 | 1 | H1 boundary | boundary |
| a002 | 3 | H2 sib=1 boundary | boundary |
| a003 | 5 | Ex1 SENTENCE | stratified |
| a005 | 9-10 | TABLE_HEADER (Ex1) | boundary |
| a014 | 20 | H2 sib=2 boundary | boundary |
| a015 | 22 | Ex2 SENTENCE | stratified |
| a019 | 30-31 | TABLE_HEADER (Ex2) | boundary |
| a023 | 36 | H2 sib=3 boundary | boundary |
| a026 | 42-43 | TABLE_HEADER (Ex3) | boundary |
| a027 | 44 | Ex3 TABLE_ROW | stratified |
| a032 | 49 | last atom | boundary |

## §2.5 numbered H2 self-namespace verification

| Cluster | atom range | parent_section | Expected | Result |
|---|---|---|---|---|
| H1 + 3 H2 | a001, a002, a014, a023 | `§SC [SC — Examples]` | H1 namespace | PASS (4/4) |
| Ex1 children (L5-L18) | a003-a013 | `§SC.1 [Example 1]` | numbered subnamespace | PASS (verified a003, a005) |
| Ex2 children (L22-L34) | a015-a022 | `§SC.2 [Example 2]` | numbered subnamespace | PASS (verified a015, a019) |
| Ex3 children (L38-L49) | a024-a032 | `§SC.3 [Example 3]` | numbered subnamespace | PASS (verified a026, a027, a032) |

## Per-atom check matrix (11/11)

| atom_id | schema 12/12 | E-1 | E-3/E-5 | verbatim | §2.5 namespace | Hook A1 | verdict |
|---|---|---|---|---|---|---|---|
| a001 | PASS | PASS | n/a (H1) | PASS | PASS | n/a | PASS |
| a002 | PASS | PASS | n/a (H2) | PASS | PASS | n/a | PASS |
| a003 | PASS | PASS | E-5 PASS | PASS | PASS | n/a | PASS |
| a005 | PASS | PASS | E-3 PASS | PASS | PASS | PASS (diff=1) | PASS |
| a014 | PASS | PASS | n/a (H2) | PASS | PASS | n/a | PASS |
| a015 | PASS | PASS | E-5 PASS | PASS | PASS | n/a | PASS |
| a019 | PASS | PASS | E-3 PASS | PASS | PASS | PASS (diff=1) | PASS |
| a023 | PASS | PASS | n/a (H2) | PASS | PASS | n/a | PASS |
| a026 | PASS | PASS | E-3 PASS | PASS | PASS | PASS (diff=1) | PASS |
| a027 | PASS | PASS | E-5 PASS | PASS | PASS | n/a | PASS |
| a032 | PASS | PASS | E-5 PASS | PASS | PASS | n/a | PASS |

## Halt checks

- §E-1 schema regression: clean (12-field schema, extracted_by object, prompt_version=v1.9.2)
- Verbatim byte-exact: all 11 sampled atoms match source
- §2.5 sub-namespace: all 4 clusters correct (H1 parent for H2; §SC.{1,2,3} for H2 children)
- TABLE_HEADER sib≠null: none found (all 3 sib=null universal)
- Halt: no

## Result

```
RULE_A_BATCH_101: PASS raw=11/11 pct=100% halt=no
```

Sustained §2.5 numbered H2 self-namespace 3rd-case proof under v1.9.2 (after batch_099 §2.7 + batch_100 §2.5 single-case PASS).
