# Phase 1A.3 Batch B — Done Note (examples.py)

> Date: 2026-05-22
> Owner: executor subagent (Batch B)
> Files: `examples.py` (7,792 bytes) + `_smoke_batch_b.py` (7,253 bytes)
> Status: ✅ ALL PASS (4/4 samples, L-1 + L-2 verified)

---

## 1. examples.py — Algorithm summary

- **File type**: `examples` (BaseChunker subclass `ExamplesChunker`).
- **Size**: 7,792 bytes / ~210 LOC.
- **Domain-aware heading-level detection rule** (single-pass heuristic):
  - If **H4 count >= 2 AND any H4 text starts with "Method "** → use H4 level (PC nested mode).
  - Else → use H2 level (flat mode — TA / IS / DS / EX / DM / MB / ...).
- **Mode dispatch**:
  - `_chunk_h2_flat()` — TA / IS / DS style. 1 chunk per H2. `cdisc_section_id` from H2 text if it starts with `§N.N.N` (rare in flat mode; usually None).
  - `_chunk_h4_nested()` — PC only. 1 chunk per H4 Method. `cdisc_section_id` from the first H2 (PC has 1: `§6.3.5.9.3`). `example_index` derived from the parent H3 ("Example N") containing the H4 by byte range. `sub_label` parsed as `Method <Letter>` from H4 text.
- **Protected-block defense**: Headings that fall inside any mermaid or table block are filtered out before chunking (`_filter_protected`). 1A.0.b confirmed 0 nesting + 0 H4-inside-table cases in KB, so this is purely defensive insurance.
- **Metadata filled per F-15 v0.2 (`None` for non-applicable)**:
  - `domain`: parent dir name (TA / PC / IS / DS / ...).
  - `section`: heading text without `#` prefix.
  - `cdisc_section_id`: e.g., `§6.3.5.9.3` for PC, None for flat.
  - `example_index`: int parsed from `Example N` regex.
  - `sub_label`: `Method A/B/C/D` for PC, None otherwise.
  - `has_mermaid` / `has_table`: bool, computed by overlap of chunk byte range with `find_mermaid_blocks` / `find_table_blocks` outputs.
- **Token counting**: inherited from `BaseChunker._new_chunk()` → `count_tokens()` → tiktoken `cl100k_base` (L-3 lock).

## 2. Smoke results (4 samples)

| sample | expected | actual | pass | mermaid_chunks | table_chunks | tokens range |
|--------|---------:|-------:|------|---------------:|-------------:|-------------:|
| TA/examples.md | 8 | **8** | ✅ | 7/8 | 7/8 | 281 – 1854 |
| PC/examples.md | 14 | **14** | ✅ | 0/14 | 14/14 | 183 – 1619 |
| IS/examples.md | 11 | **11** | ✅ | 0/11 | 11/11 | 695 – 1520 (Ex 1-3 sample) |
| DS/examples.md | 11 | **11** | ✅ | 0/11 | 11/11 | 323 – 1703 (Ex 1-3 sample) |

- **TA**: 7 Examples have mermaid (4 mermaid each × 5 examples + variations); the 8th chunk = "Trial Arms Issues" correctly has no mermaid + no table.
- **PC**: 14 chunks confirmed (4+4+4+2). Example 4 only has Method A + Method D, matching `chunker_feasibility §3.2` ground truth. All `sub_label`s = `{"Method A", "Method B", "Method C", "Method D"}`. All `example_index` = `{1,2,3,4}`. `cdisc_section_id` = `§6.3.5.9.3` on all 14 chunks.
- **IS / DS**: 11 flat H2 Examples each. All chunks have table (IS has dense ADA test data tables; DS has disposition tables).

All chunk token counts are well under the 8191 embedding limit (max observed = 1854 in TA Example 2).

## 3. L-1 mermaid + L-2 table protection — verification

Byte-range overlap check confirmed (in `_smoke_batch_b.py::split_points_inside_blocks`):

- **TA Example 1** chunk byte range `[2712, 7438)` fully contains all 4 mermaid blocks (`[4668, 5044)`, `[5067, 5361)`, `[5386, 5771)`, `[5790, 6020)`). No chunk boundary is strictly inside any mermaid block.
- **TA Example 2** chunk `[7438, 12028)` contains 3 mermaid blocks (`[7699, 8074)`, `[8097, 8954)`, `[9163, 9624)`) fully nested.
- 0 L-1 violations + 0 L-2 violations across all 4 samples (TA / PC / IS / DS).
- DS has 21 table blocks across 11 chunks (some Examples have ds.xpt + co.xpt + ds_revised.xpt tables, multiple per chunk); all stay within chunk boundaries.
- PC has 14 table blocks distributed across 14 chunks (one table per Method, mostly ds.xpt + relrec.xpt or pp.xpt).

The protection works because chunking happens at heading start positions, which are line-anchored ATX `## ` / `### ` / `#### ` patterns that never appear inside a fenced ` ```mermaid ` block or a `|...|` table row.

## 4. TODOs for 1A.4 test-engineer (corner cases)

Items deferred from this Batch B (not blocking for 1A.3 close):

1. **TS/examples.md edge case** — Trial Summary likely has no examples.md (it's metadata-only). Check whether `examples.md` exists at all; if not, the chunker should be skipped by the ingest loop, not by the chunker itself.
2. **RELREC / RELSPEC / RELSUB examples.md** — possibly empty or PUNT (per 06 P7 audit). If `h2s` is empty AND no H4 nested → chunker returns `[]` (current behavior). Test ingest layer skips 0-chunk files cleanly.
3. **DM/examples.md mermaid** (4 mermaid per chunker_feasibility §2.1) — not in this Batch B smoke. Should be H2 flat with mermaid; expected to behave identically to TA. Add to 1A.4 expanded smoke.
4. **TD / TV / RELSPEC examples.md** also have mermaid (3 / 1 / 1 blocks per phase_1a_0_sanity §2.1). Expand 1A.4 smoke to cover.
5. **Multi-H1 / no-H1 files** — current chunker doesn't gate on H1 presence; if a file has neither H2 nor H4 it returns `[]`. Consider whether to fall back to "whole file as 1 chunk" in 1A.4 review.
6. **Pathological heading inside fence** — verified 0 cases in KB by 1A.0.b, but the `_filter_protected()` defense is in place. Add an explicit unit test in 1A.4 with a synthetic file: ` ```\n## Fake heading inside fence\n``` ` to confirm the filter drops it.
7. **Mixed level files** — if any other domain (besides PC) uses H4 Method nesting, the heuristic `len(h4s) >= 2 AND any "Method "` will catch it. If any domain uses H3 nesting (no H4) → currently falls to H2 flat mode. 1A.4 should grep `'^### Example'` across all 63 examples.md to confirm no orphan H3-only files.

## 5. Confirmation: ALL steps done

- [x] examples.py written (7,792 B, BaseChunker subclass).
- [x] _smoke_batch_b.py written (7,253 B, hard-asserts 8/14/11/11 + PC sub_labels + L-1/L-2 protection).
- [x] Smoke run: exit code 0, RESULT: ALL PASS.
- [x] Byte-range mermaid protection verified (TA examples 1-3).
- [x] PC 14-chunk hard requirement met (Example 4 = Method A + D only).
- [x] Progress note (this file) written.
- [x] No commit (per Step 4 constraint).

## 6. Anomalies for main session

None blocking. Two minor observations:

- **DS chunk[0]** (Example 1) is 1703 tokens — largest DS chunk, still well under 8K. Composed of long preamble + 21-row ds.xpt table. No risk.
- **TA chunk[1]** (Example 2) is the largest TA chunk at 1854 tokens (3 mermaid + 2 tables). No risk.
- **No `cdisc_section_id` parsed for flat H2 mode**, because TA/IS/DS H2 headings are pure `## Example N` without `§N.N.N` prefix. Only PC nested mode produces a non-None `cdisc_section_id`. This is correct per chunker_feasibility §3.2 — only PC has the `§6.3.5.9.3` parent H2.
