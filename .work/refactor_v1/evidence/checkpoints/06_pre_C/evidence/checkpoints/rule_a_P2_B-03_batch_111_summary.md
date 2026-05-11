# Rule A Reviewer Summary — P2 B-03c Round 10 batch_111 SR/examples.md

> Reviewer: pr-review-toolkit:code-reviewer (Rule D isolated, ≠ writer general-purpose)
> Prompt baseline: `subagent_prompts/P0_reviewer_v1.9.3.md`
> Source: `knowledge_base/domains/SR/examples.md` (116 lines, 3 numbered H2 §2.5×3, 7 tables across Ex1+Ex2+Ex3)
> Atoms: `evidence/checkpoints/P2_B-03_batch_111_md_atoms.jsonl` (82 atoms; LARGEST in round 10)
> Date: 2026-05-07

## Verdict

**PASS** — 82/82 atoms PASS Rule A audit (100.0%); 0 HIGH; 0 schema regression; 0 collision.

## §R-E1 Schema regression sweep (PRIORITY 1)

| Check | Result |
|---|---|
| 12 fields per atom | 82/82 PASS |
| atom_id sequential `md_dmSR_ex_a001..a082` | PASS (0 collision) |
| file path `knowledge_base/domains/SR/examples.md` | PASS (single distinct value) |
| line range [1, 116] | 82/82 in range |
| atom_type ∈ 9 valid types | 82/82 PASS (HEADING=4, SENTENCE=21, TABLE_HEADER=7, TABLE_ROW=50) |
| atom_type distribution vs claim (H=4, SEN=21, THDR=7, TROW=50) | EXACT MATCH |
| extracted_by object schema (subagent_type/prompt_version/ts) | 82/82 PASS |
| prompt_version = "P0_writer_md_v1.9.3" | 82/82 PASS |

## §R-E2/E-3/E-5 sib_idx + hl_level rules

| Rule | Result |
|---|---|
| §R-E2 H1 sib=1 (a001) | PASS hl=1 sib=1 |
| §E-2 H2 sib=1/2/3 sequential per file | PASS (a002 sib=1, a017 sib=2, a064 sib=3) |
| §R-E3 TABLE_HEADER hl=null sib=null EXPLICIT | 7/7 PASS |
| §R-E5 non-HEADING (SENTENCE+TABLE_ROW+TABLE_HEADER) hl=null sib=null EXPLICIT | 78/78 PASS |

## §2.5 numbered-H2 self-namespace verify (4-bucket)

| parent_section | Count | Expected | Match |
|---|---|---|---|
| `§SR [SR — Examples]` (file-root: H1 + 3 H2 atoms) | 4 | 4 | ✓ |
| `§SR.1 [Example 1]` | 14 | 14 | ✓ |
| `§SR.2 [Example 2]` | 46 | 46 | ✓ |
| `§SR.3 [Example 3]` | 18 | 18 | ✓ |
| **Total** | **82** | **82** | ✓ |

## Table separator skip verify (§E-5 / writer §2.x)

Lines L15, L35, L52, L65, L96, L106, L114 (7 separators) → **0 atoms** (PASS, all skipped correctly).

## Spot-check verbatim byte-exact (3 random)

| atom_id | Line | match |
|---|---|---|
| md_dmSR_ex_a004 | L7 | ✓ `**Rows 1-4:** Show responses associated with the administration of a histamine control.` |
| md_dmSR_ex_a015 | L22 | ✓ `\| 7 \| SPI-001 \| SR \| SPI-001-11035 \| SITE7 \|` ... (TABLE_ROW exact) |
| md_dmSR_ex_a082 | L116 | ✓ `\| 2 \| ABC \| AG \| ABC-001 \| AGSEQ \| 1 \|  \| R1 \|` (TABLE_ROW exact) |

## cross_refs sanity

| Domain | Where attached | Sanity |
|---|---|---|
| EX | Ex2 narrative + ex.xpt table block (a018, a035-a042) | ✓ correct |
| RELREC | Ex2 narrative + relrec.xpt table block (a018, a043-a063) + Ex3 (a078-a082) | ✓ correct |
| AG | Ex3 narrative + ag.xpt table block (a065, a074-a077, a078, a082) | ✓ correct |
| SR (self) | 0 atoms | ✓ self-excluded |

## §F-1 §2.11 Plan B verification

**N/A** — batch_111 has 0 H3, 3 numbered H2 (all §2.5 self-namespace). No §F-1 trigger; baseline 5 cumulative cases (round 07+09) unchanged.

## §F-2 atoms/line ratio retrospective (INFO non-blocking)

- batch_111: 82 atoms / 116 source lines = **0.7069** — within empirical band 0.59-0.85 ✓ (mid-upper region; consistent with dense Examples table content).

## §F-3 kickoff atom estimate calibration retrospective (INFO non-blocking)

- Kickoff §0.5 row 25 / §1 estimate: 70-100 atoms (mid 85)
- Actual: 82 atoms
- delta_pct = abs(82 − 85)/85 = **3.5%** (well below 50% threshold) — excellent calibration

## HIGH findings: NONE

## Halt status: NONE

- PASS rate 100.0% ≥ 90% ✓
- 0 HIGH severity finding ✓
- 0 schema regression ✓
- 0 atom_id collision ✓

## Conclusion

batch_111 (LARGEST in round 10) PASS all 14 Rule A check categories per kickoff prompt. v1.9.3 §R-E1..E-6 + §R-F-1..F-3 + §2.5 4-bucket namespace + table separator skip + cross_refs sanity all sustained. Reviewer recommends advance to batch_112 dispatch.
