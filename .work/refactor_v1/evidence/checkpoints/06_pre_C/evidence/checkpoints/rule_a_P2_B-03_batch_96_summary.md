# Rule A Audit Summary — batch_96 RP/assumptions.md

**Batch**: P2 B-03c round 09 batch_96
**Source**: `knowledge_base/domains/RP/assumptions.md` (10 lines)
**Writer output**: `P2_B-03_batch_96_md_atoms.jsonl` (6 atoms)
**Prompt baseline**: P0_writer_md_v1.9.2 (3rd post-cut round)
**Reviewer**: Rule A independent reviewer (Rule D isolation, subagent_type ≠ writer's general-purpose-with-writer-prompt)
**Audit date**: 2026-05-07

## §0.5 Grep Cross-Verify (source structure)

```
$ wc -l knowledge_base/domains/RP/assumptions.md
      10 knowledge_base/domains/RP/assumptions.md
$ grep -c '^# '   → 1   (H1)
$ grep -c '^## '  → 0   (H2)
$ grep -c '^### ' → 0   (H3)
```

Source structure: file-root H1 only, no H2/H3, single numbered list with one nested sub-bullet (3a). 10 atoms expected upper bound; writer produced 6 (1 H1 + 5 list items). Sampling **ALL 6 atoms** (N<11 small-batch rule).

## Sampling

- Atoms total: **6**
- Audited: **6** (full file given small size, N<11 → audit all)
- §2.5 single-anchor lock cases: **0** (no H2/H3 in file)
- §2.7 LIST in HEADING-only file lock cases: **N/A** (file has 1 H1 + list items; this is normal LIST_ITEM under H1)
- §2.11 Plan B sub-namespace: **N/A** (no domain-section headings)

## Per-Check Matrix

| Atom | a001 | a002 | a003 | a004 | a005 | a006 |
|------|------|------|------|------|------|------|
| Schema 12/12 fields | PASS | PASS | PASS | PASS | PASS | PASS |
| §E-1 no regression (no `verbatim_text`, no "H1"/"H2") | PASS | PASS | PASS | PASS | PASS | PASS |
| §E-2 H1 hl=1 sib=1 | PASS | N/A | N/A | N/A | N/A | N/A |
| §E-4 extracted_by object (3 sub-fields) | PASS | PASS | PASS | PASS | PASS | PASS |
| §E-5 non-HEADING explicit null literal | N/A | PASS | PASS | PASS | PASS | PASS |
| Verbatim byte-exact vs source line | PASS | PASS | PASS | PASS | PASS | PASS |
| parent_section = `§RP [RP — Assumptions]` | PASS | PASS | PASS | PASS | PASS | PASS |
| atom_type correct (HEADING/LIST_ITEM) | PASS | PASS | PASS | PASS | PASS | PASS |
| atom_id contiguous a001-a006 | PASS | PASS | PASS | PASS | PASS | PASS |

## Detailed Verbatim Cross-Check

| Atom | Source line | Verbatim match |
|------|-------------|----------------|
| a001 | L1 `# RP — Assumptions` | exact (em dash U+2014 preserved) |
| a002 | L3 `1. Reproductive System Findings domain contains information regarding a subject's reproductive ability and reproductive history (e.g., number of previous pregnancies, number of births, pregnant during the study).` | exact |
| a003 | L5 `2. Information on medications related to reproduction (e.g., contraceptives, fertility treatments) should be included in the Concomitant/Prior Medications (CM) domain; see Section 6.1.2.` | exact |
| a004 | L7 `3. There are separate codelists for RP tests, responses, and units.` | exact |
| a005 | L8 `   a. Associations between RP tests and response codelists are described in the RP Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.` | exact (3-space indent preserved literally) |
| a006 | L10 `4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the RP domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.` | exact (8 qualifier tokens preserved) |

## Schema-field Verification (§E-1)

All 6 atoms carry exactly the 12 frozen field names: `atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by`. No `verbatim_text` legacy aliases. No "H1"/"H2" string literals (atom_type uses `HEADING`/`LIST_ITEM`). All non-HEADING atoms carry literal `"heading_level":null,"sibling_index":null` (not omitted, not "N/A").

## §E-4 extracted_by Object Form

All 6 atoms: `{"subagent_type":"general-purpose","prompt_version":"P0_writer_md_v1.9.2","ts":"2026-05-07T00:00:00Z"}` — 3 sub-fields, no flat-string regression.

## Sub-bullet Handling Notes

a005 (source L8 `   a. ...`) is correctly classified as `LIST_ITEM` with parent_section pointing to file-root §RP (no intermediate H2/H3 anchor exists). Verbatim preserves leading 3 spaces literally as written. parent_section choice is consistent — file-root anchor is the only valid container.

## parent_section Cohesion

All 6 atoms use `§RP [RP — Assumptions]` (file-root anchor since no H2 exists). Consistent. The H1 atom itself also uses this parent_section value, which is the established convention for the file-defining heading (it announces its own §-anchor).

## Findings

None. No regressions, no verbatim drift, no schema drift, no §E-5 literal-null misses, no atom_id sequence gaps.

## Verdict

- Raw pass: **6 / 6 = 100.0%**
- §E-1 regression: 0
- Verbatim drift: 0
- Halt threshold (>= 90% pass + zero high-severity): MET
- HALT: no

---

`RULE_A_BATCH_96: PASS raw=6/6 pct=100.0% halt=no`
