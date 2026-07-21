# Rule A audit — P2 B-03c round 11 batch_117 (SUPPQUAL/examples.md)

> Reviewer: `pr-review-toolkit:code-reviewer` (Rule D distinct from writer `general-purpose`)
> Prompt version: P0_reviewer_v1.9.3 (35 hooks)
> Audit date: 2026-05-07
> Verdict: **PASS**

---

## Audit inputs

- Writer output: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_117_md_atoms.jsonl` (17 atoms a001..a017)
- Source: `knowledge_base/domains/SUPPQUAL/examples.md` (29 lines)
- Atom_type distribution: HEADING=3, SENTENCE=6, TABLE_HEADER=2, TABLE_ROW=6 (total 17)

## Hook results (35/35 PASS)

### Hook A1 byte-exact verbatim

| # | Result | Notes |
|---|---|---|
| Verbatim line-range match | **PASS 17/17** | Including 2 multi-line TABLE_HEADER atoms (a006 L11-12 + a012 L22-23 joined with `\n`) |

### §R-E1 schema regression sweep (PRIORITY 1)

| # | Result | Notes |
|---|---|---|
| 12 required fields per atom | **PASS 17/17** | No missing/extra fields; full v1.9.3 schema |
| extracted_by object schema | **PASS 17/17** | All atoms have `subagent_type` + `prompt_version` + `ts` |

### §R-E2 H1 sib=1 universal verify (HIGH)

| Atom | hl | sib | parent_section | PASS? |
|---|---|---|---|---|
| a001 (L1 `# SUPPQUAL — Examples`) | 1 | 1 | `§SUPPQUAL [SUPPQUAL — Examples]` | ✓ |

### §R-E3 TABLE_HEADER sib=null + hl=null universal verify (HIGH)

| Atom | Lines | hl | sib | PASS? |
|---|---|---|---|---|
| a006 (Example 1 table header) | L11-12 | null | null | ✓ |
| a012 (Example 2 table header) | L22-23 | null | null | ✓ |

Both TABLE_HEADER atoms multi-line (header row + alignment delimiter joined `\n`); byte-exact verified.

### §R-E4 extracted_by object schema (HIGH)

PASS 17/17 — all atoms include the required object subfields.

### §R-E5 non-HEADING field-explicit-null (MED)

| atom_type | count | hl=null sib=null all explicit | PASS? |
|---|---|---|---|
| SENTENCE | 6 | yes (a002, a004, a005, a010, a011, a017) | ✓ |
| TABLE_HEADER | 2 | yes (a006, a012) | ✓ |
| TABLE_ROW | 6 | yes (a007, a008, a013, a014, a015, a016) | ✓ |

All non-HEADING atoms have explicit `"heading_level": null, "sibling_index": null` per §2.10 / §R-E5; 0 omission found.

### §R-E6 LOW FIGURE-vs-CODE_LITERAL boundary

N/A — batch_117 contains no FIGURE / CODE_LITERAL atoms.

### §2.5 numbered H2 ×2 sub-namespace verify

| H2 | Line | sib | parent_section | Children scope | Children parent | PASS? |
|---|---|---|---|---|---|---|
| `## Example 1` (a003) | L5 | 1 | `§SUPPQUAL [SUPPQUAL — Examples]` (file-root) | a004-a008 (L7-L14) | `§SUPPQUAL.1 [Example 1]` | ✓ |
| `## Example 2` (a009) | L16 | 2 | `§SUPPQUAL [SUPPQUAL — Examples]` (file-root) | a010-a017 (L18-L29) | `§SUPPQUAL.2 [Example 2]` | ✓ |

Pre-H2 atom a002 (L3 SENTENCE) sits at file-root scope before `## Example 1`, parent `§SUPPQUAL [SUPPQUAL — Examples]` ✓.

### Trailing-sentence scope decision (a017 L29)

L29 SENTENCE follows last H2 (`## Example 2` L16) without intervening H2. Writer assigned `§SUPPQUAL.2 [Example 2]` parent (Example 2 scope). This is the correct §2.5 numbered H2 self-namespace inheritance pattern: trailing content under a numbered H2 inherits that H2 sub-namespace until next H2 / EOF. PASS.

### atom_id uniqueness + sequential

| Check | Result |
|---|---|
| Unique | **17/17** |
| Sequential a001..a017 | **PASS** (no gap, no collision) |
| Prefix uniformity | **PASS** all `md_dmSUPPQUAL_ex_aXXX` |

### TABLE_ROW per R-2.8-2

6 TABLE_ROW atoms (a007, a008, a013, a014, a015, a016) all have `hl=null, sib=null` ✓.

### parent_section consistency

17/17 atoms match expected §2.5 sub-namespace topology — see "§2.5 numbered H2 ×2 sub-namespace verify" table above.

### cross_refs convention

| Atom | cross_refs | PASS? |
|---|---|---|
| a017 (L29 trailing SENTENCE) | `["Section 5.2", "Section 6.3.3", "Section 6.3.5.6"]` | ✓ |

a017 source text:
> "Additional examples may be found in the domain examples such as Section 5.2, Demographics, Examples 3 and 4, in Section 6.3.3, ECG Test Results, Example 1, and in Section 6.3.5.6, Laboratory Test Results, Example 1."

3 distinct `Section X.Y` refs all captured. **Convention follows batch_114 a011 precedent (include `Section X.Y` text refs in cross_refs).** This is consistent with the include-convention; batch_117 does NOT exhibit the drift previously flagged in INFO-B115-01. INFO carry forward — convention sustained on round 11 batch_117.

Other atoms (a001-a016): cross_refs=[] (no inline `Section X.Y` text references in source) ✓.

## §R-F-1 §2.11 Plan B verification

**Trigger detection**: 0 H3 atoms in batch_117; 0 numberless H2 (both H2 are `## Example N` numbered §2.5).
**Verdict**: §F-1 trigger N/A. **PASS** (no §2.11 Plan B sub-namespace required; batch_117 uses §2.5 numbered H2 self-namespace exclusively).
Backward compatibility note: round 07 PC/ex + round 09 RELREC/RS sub-namespace atoms unaffected (different files).

## §R-F-2 ratio retrospective (LOW INFO)

| Metric | Value |
|---|---|
| Source lines | 29 |
| Atoms | 17 |
| Ratio | **0.586** |
| Empirical band | 0.59-0.85 |
| Status | **0.004 below lower band** |

INFO finding (NOT halt) — consistent with batch_116 (SUPPQUAL/ass) at 0.577. Round 11 lower-edge trend continues. Drivers: small examples.md file (29L) with dense table content (8 table rows + 2 table headers = 10/17 = 58.8% structural compression). Same lower-edge driver pattern as round 10 (0.591). Acceptable per round-close cumulative re-check; no halt.

## §R-F-3 kickoff atom estimate calibration retrospective (LOW INFO)

| Metric | Value |
|---|---|
| Kickoff est range | 10-15 |
| Kickoff est mid | 12.5 |
| Actual atoms | 17 |
| Delta % | **+36.0%** (within ±50% threshold) |
| Status | **PASS** within calibration tolerance |

INFO finding — estimate-too-low by 36% but within ±50% threshold. Driver: kickoff estimate did not fully account for trailing SENTENCE a017 + 2 strong-emphasis label SENTENCEs (a005 `**suppae.xpt**` + a011 `**suppqs.xpt**`) which writer correctly atomized as standalone. No halt. Carry-forward to round-close mini-audit.

## Findings summary

| Severity | Count | Items |
|---|---|---|
| HIGH | **0** | — |
| MED | 0 | — |
| LOW | 0 | — |
| INFO | 2 | §R-F-2 ratio 0.586 (0.004 below band) ; §R-F-3 estimate delta +36% (within ±50%) |

## Verdict

**PASS** — 35/35 hooks PASS, 0 HIGH severity findings, 2 INFO carry-forward notes (ratio + estimate calibration). batch_117 ready to merge into `md_atoms.jsonl`.

## Hook tally

- v1.7 hooks 1-18: PASS (verbatim, atom_id, schema, atom_type, parent_section, etc.)
- v1.9 R22+R23: PASS
- v1.9.1 R24+R-D2..D-6: PASS
- v1.9.2 R25+R-E2..E-6: PASS (incl. CRITICAL Hook 22c gold reference + HIGH R-2.8 trio + MED-01 + LOW E-6)
- v1.9.3 R-F-1 (§2.11 Plan B verify, HIGH): N/A trigger PASS
- v1.9.3 R-F-2 (ratio band INFO): PASS with INFO note
- v1.9.3 R-F-3 (estimate calibration INFO): PASS with INFO note

**Total: 35/35 hooks PASS**.
