# Rule A Audit — batch_94 RELREC/assumptions.md

> Round: P2 B-03c round 09 (v1.9.2 baseline 3rd round)
> Reviewer: independent subagent (Rule D isolation from writer)
> Source: `knowledge_base/domains/RELREC/assumptions.md`
> Writer output: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_94_md_atoms.jsonl`

## Counts

- Atoms total: **19**
- Audited: **11** (8 boundary + 3 stratified)
- PASS: **11/11**
- FAIL: **0/11**
- Pass rate: **100.0%**

## §0.5 Grep Cross-Verify (3 facts, all PASS)

| Fact | Command | Expected | Actual | Verdict |
|------|---------|----------|--------|---------|
| Total lines | `wc -l knowledge_base/domains/RELREC/assumptions.md` | 32 | 32 | PASS |
| H2 count | `grep -cE "^## " knowledge_base/domains/RELREC/assumptions.md` | 2 | 2 | PASS |
| H3 count | `grep -cE "^### " knowledge_base/domains/RELREC/assumptions.md` | 0 | 0 | PASS |

## Audit Sample Selection

**Boundary (8)**:
- a001 — first atom (H1, L1)
- a019 — last atom (LIST_ITEM, L32)
- a004 — H2 boundary "## Relating Peer Records" (L7)
- a013 — H2 boundary "## Relating Datasets" (L20)
- a003 — atom right BEFORE a004 H2 (L5, SENTENCE)
- a012 — atom right BEFORE a013 H2 (L18, LIST_ITEM)
- a005 — atom right AFTER a004 H2 (L9, SENTENCE)
- a014 — atom right AFTER a013 H2 (L22, SENTENCE)

**Stratified (3)** — distinct from boundary, one per atom_type bucket where possible:
- HEADING bucket — all 3 HEADING atoms (a001/a004/a013) already in boundary set; bucket exhausted.
- SENTENCE — a015 (L24)
- LIST_ITEM — a010 (L16, random) and a017 (L28)

Final audited set (11): a001, a003, a004, a005, a010, a012, a013, a014, a015, a017, a019.

## Per-Check Matrix (10 checks × 11 atoms)

| atom_id | schema12 | E1_noregr | E2_H1sib | E3_TH_null | E4_extby_obj | E5_expl_null | verbatim | §2.7 file-root | atom_type | id_seq |
|---------|----------|-----------|----------|------------|--------------|--------------|----------|----------------|-----------|--------|
| a001 | PASS | PASS | PASS | N/A | PASS | N/A_H | PASS | PASS | PASS | PASS |
| a003 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a004 | PASS | PASS | N/A | N/A | PASS | N/A_H | PASS | PASS | PASS | PASS |
| a005 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a010 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a012 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a013 | PASS | PASS | N/A | N/A | PASS | N/A_H | PASS | PASS | PASS | PASS |
| a014 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a015 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a017 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |
| a019 | PASS | PASS | N/A | N/A | PASS | PASS | PASS | PASS | PASS | PASS |

Legend: `N/A_H` = HEADING atom, E5 explicit-null check does not apply (heading_level/sibling_index intentionally non-null). `N/A` for E2_H1sib applies to non-H1 atoms; `N/A` for E3_TH_null applies — batch_94 has 0 TABLE_HEADER atoms.

## Spot-Check Details

### §2.7 H2-children file-root parent_section

- a004 (H2 "## Relating Peer Records", L7) parent_section = `§RELREC [RELREC — Assumptions]` ✓ (file-root, NOT `§RELREC.1`)
- a005 (child of a004, L9 SENTENCE) parent_section = `§RELREC [RELREC — Assumptions]` ✓
- a013 (H2 "## Relating Datasets", L20) parent_section = `§RELREC [RELREC — Assumptions]` ✓ (file-root, NOT `§RELREC.2`)
- a014 (child of a013, L22 SENTENCE) parent_section = `§RELREC [RELREC — Assumptions]` ✓

§2.7 file-root convention correctly applied for numberless H2.

### Verbatim byte-exact spot checks

- a001 L1: `# RELREC — Assumptions` matches source byte-exact (em-dash U+2014 preserved).
- a004 L7: `## Relating Peer Records` matches source byte-exact.
- a013 L20: `## Relating Datasets` matches source byte-exact.
- a017 L28: bold markdown `**ONE and ONE.**` and `**NO**` preserved byte-exact.
- a019 L32: bold markdown `**MANY and MANY.**`, em-dash absent (source uses regular `,`), Section reference `Section 6.3.5.9.3, Relating PP Records to PC Records.` preserved byte-exact.

### atom_type appropriateness

- HEADING (3): a001 (`#`), a004 (`##`), a013 (`##`) — all match `^#{1,6}\s+`.
- LIST_ITEM (8): a007/a008/a010/a011/a012 (`-` bullets), a017/a018/a019 (`N.` numbered) — all match `^[-*]\s+` or `^\d+\.\s+`.
- SENTENCE (8): a002/a003/a005/a006/a009/a014/a015/a016 — full paragraph as one atom, no list/heading prefix.

### atom_id sequence

a001 → a019 sequential, no gaps. 19 atoms total.

## Findings

None.

## HALT Conditions Check

- §E-1 schema regression (verbatim_text / wrong atom_type / missing fields): NOT DETECTED → no HALT
- Verbatim byte mismatch ≥1 atom: NOT DETECTED → no HALT
- §2.7 misapplication (sub-namespace where file-root expected): NOT DETECTED → no HALT
- Rule A pass rate <90%: 100% ≥ 90% → no HALT

## Final Verdict

RULE_A_BATCH_94: PASS raw=11/11 pct=100.0% halt=no
