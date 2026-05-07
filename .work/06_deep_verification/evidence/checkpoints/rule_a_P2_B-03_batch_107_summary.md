# Rule A Reviewer Summary — P2 B-03c batch_107 (round 10)

> Reviewer: pr-review-toolkit:code-reviewer (Rule D isolated from writer general-purpose)
> Reviewer baseline: P0_reviewer_v1.9.3
> Source: `knowledge_base/domains/RELSUB/examples.md` (38L, 1 numbered H2 L3 §2.5, 2 tables L15+L31)
> Atoms file: `evidence/checkpoints/P2_B-03_batch_107_md_atoms.jsonl` (23 atoms)

## Overall verdict

**PASS** — 23/23 atoms PASS Rule A (100.0%).

## Schema regression sweep (§R-E1, PRIORITY 1)

**CLEAN** — no regression detected.

| Check | Result |
|-------|--------|
| 12 fields per atom | 23/23 OK |
| atom_id sequential a001..a023, 0 collision | OK |
| atom_type ∈ 9 valid types | OK (HEADING×2 + SENTENCE×10 + TABLE_HEADER×2 + TABLE_ROW×9) |
| §E-2 a001 HEADING heading_level=1 sibling_index=1 | OK |
| §E-2 a002 HEADING heading_level=2 sibling_index=1 | OK |
| §E-3 TABLE_HEADER sib_idx=null hl=null explicit (a008, a017) | 2/2 OK |
| §E-5 non-HEADING explicit hl=null AND sib=null | 21/21 OK |
| §E-4 extracted_by object {subagent_type, prompt_version, ts} | 23/23 OK |
| prompt_version = "P0_writer_md_v1.9.3" | 23/23 OK |
| line ranges within [1,38] | 23/23 OK |
| TABLE separator lines L16/L32 NOT atomized | OK (skipped) |

## §2.5 namespace correctness

**21/21 PASS** for sub-namespace atoms (a003-a023). All carry `parent_section = "§RELSUB.1 [Example 1]"` consistent with §2.5 numbered H2 self-namespace lock (L3 `## Example 1`).

- a001 (H1 L1) → `§RELSUB [RELSUB — Examples]` (file-root) — OK
- a002 (H2 L3) → `§RELSUB [RELSUB — Examples]` (file-root for the H2 itself) — OK
- a003-a023 (body L5-L38) → `§RELSUB.1 [Example 1]` — 21/21 OK

## Verbatim byte-exact spot-check (2 random atoms)

- **a012 (line 21)**: `awk 'NR==21'` → `The RELSUB table is for the 3 subjects whose demography data is shown in the preceding table.` → **byte-exact match** with atom verbatim.
- **a018 (line 33)**: `awk 'NR==33'` → `| 1 | HEM021 | HEM021-001 | HEM021-002 | MOTHER, BIOLOGICAL |` → **byte-exact match** including pipe delimiters and comma-space inside MOTHER, BIOLOGICAL preserved.

## Table separator skip verification

| Line | Source content | Atomized? |
|------|---------------|-----------|
| L16 | `\|-----\|---------\|--------\|---------\|---------\|-----\|------\|-----\|` | **NOT atomized** OK |
| L32 | `\|-----\|---------\|---------\|---------\|------\|` | **NOT atomized** OK |

Both separator rows correctly skipped per Markdown table convention. Header L15→a008, header L31→a017; data rows L17-L19→a009-a011 and L33-L38→a018-a023.

## cross_refs sanity (DM domain ref in dm.xpt section)

| Atom | Line | Section | Claimed | Verdict |
|------|------|---------|---------|---------|
| a007 | L13 | dm.xpt header | `["DM"]` | OK (literal `**dm.xpt**`) |
| a008 | L15 | dm.xpt header row | `["DM"]` | OK (DOMAIN col contains "DM") |
| a009-a011 | L17-19 | dm.xpt data rows | `["DM"]` each | OK (DOMAIN value "DM" in each row) |
| a016 | L29 | relsub.xpt header | `[]` | OK (no foreign domain ref; relsub.xpt is current domain) |
| a017-a023 | L31-38 | relsub.xpt header+data | `[]` each | OK (intra-domain) |

DM cross_ref correctly applied to 5 atoms in dm.xpt section (a007-a011); not propagated to relsub.xpt section atoms (a016-a023). Sound boundary.

## §F-3 INFO observation: kickoff atom estimate calibration

Kickoff §1 estimated 22-32 atoms; actual = **23**. Delta within 5% of low end → **calibration accurate**. Mid-band would have been ~27; actual sits at low-mid of range, consistent with an examples.md file dominated by 1 long table (9 data rows) rather than dense prose.

## §F-2 INFO observation (non-blocking)

ratio = 23 atoms / 38 lines = **0.605** — **in band** 0.59-0.85 (lower-mid). v1.9.3 §F-2 9-round sustained band continues to hold. Driver: 9 blank-line separators (L2/L4/L6/L8/L10/L12/L14/L20/L22/L24/L26/L28/L30) + 2 table-separator lines (L16/L32) reduce atom-bearing line count; effective atom-bearing-line count is ~25, giving 23/25 = 0.92 of bearable lines extracted. INFO only — no remediation.

## HIGH findings

**None.** No halt triggers fired:
- PASS rate 100% (≥ 90% threshold)
- 0 HIGH severity
- 0 schema regression
- 0 atom_id collision
- 0 separator atomized
- §2.5 namespace lock sustained
- §F-2 ratio in band

## Halt status

**NO HALT** — proceed to batch_108 SM/ass.
