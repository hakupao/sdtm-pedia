# Checkpoint A4 — NotebookLM instructions v3 writer

> Phase: A4
> Date: 2026-05-20
> Writer subagent: executor (A4, parallel with A1/A2/A3)
> Status: **WRITER_PASS_REVIEWER_PENDING**

---

## Outputs produced

| File | Lines | Notes |
|---|---|---|
| `ai_platforms/notebooklm/dev/v3_draft/instructions_v3.md` | 156 | v3 clean rewrite |
| `ai_platforms/notebooklm/dev/v3_draft/v3_design_rationale.md` | — | design rationale + diff summary |
| `evidence/checkpoints/a4_notebooklm_v3_writer.md` | — | this file |

---

## Rule A self-spot-check (5/5 PASS)

| Probe | Check | Result |
|---|---|---|
| 1 | R1-R5 all present | PASS — R1 L19, R2 L25, R3 L36, R4 L49, R5 L61 |
| 2 | regex-gated CO-N 4 triggers present | PASS — biospecimen L42, file-format L43, IS scope L44, SDTM-var L45 |
| 3 | 0 fossil annotation | PASS — grep returns 0 matches for fossil patterns |
| 4 | NotebookLM carry-over: footer Sources style + 42-bucket routing + source-chip non-duplication | PASS — footer Sources at L53-57; 42-bucket inventory L5-14; source-chip note L53 |
| 5 | Line count 80-156L | PASS — 156 lines (within band) |

---

## v2 → v3 line delta

| Metric | v2 | v3 |
|---|---|---|
| Total lines | 157 | 156 |
| Fossil annotations | 0 | 0 |
| Essential rules (R1-R5) | absent (14 §§ structure) | present |
| Regex-gated CO-N table | absent | present (4 triggers) |
| Footer Sources citation style | present | preserved |

---

## Design decisions

1. v2 already had 0 fossil annotations (citation refactor shipped in v1.3). v3 restructures the 14-section format into R1-R5 framework per design spec § 2.4, preserving all substantive content.
2. AHP-V1/V2/V3 anti-hallucination logic was implicit in v2 §1; made explicit as R2 with negation list per design spec § 1.
3. Regex trigger table (R3) is new structure — v2 had no explicit regex table; logic was distributed across §§ 1, 6, 7, 8.
4. Footer Sources citation style (v1.3 carry) preserved verbatim in R4; source-chip sidebar non-duplication note preserved.
5. 42-bucket source inventory preserved in header section (lines 5-14).

---

## Files NOT modified

- `ai_platforms/notebooklm/current/*` — untouched
- `knowledge_base/*` — untouched
- Other platform dev drafts — untouched

---

## Next step

Reviewer subagent (Rule D slot #25, `oh-my-claudecode:verifier`) to audit this draft independently.
