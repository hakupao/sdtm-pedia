# Batch A — Completion Note

Phase 1A.3 Batch A executor (claude-sonnet-4-6). Date: 2026-05-22.

## Files Created

| File | Size |
|------|------|
| `scripts/chunkers/spec.py` | 1 276 bytes |
| `scripts/chunkers/assumptions.py` | 2 211 bytes |
| `scripts/chunkers/model.py` | 1 706 bytes |
| `scripts/chunkers/_smoke_batch_a.py` | 2 893 bytes |

## Smoke Results (python3, Mac arm64, Py 3.9.6)

| Chunker | Sample file | Chunks | First section | Notes |
|---------|-------------|--------|---------------|-------|
| `SpecChunker` | `domains/AE/spec.md` | 64 | `STUDYID` | tokens 19–232 |
| `AssumptionsChunker` | `domains/AE/assumptions.md` | 13 | `overview` + items 1–12 sequential | tables preserved within item slices |
| `ModelChunker` | `model/01_concepts_and_terms.md` | 2 | `2.1 Model Concepts and Terms — Variables` | tokens 292–1 434 |

`to_metadata()` verified on all chunks: `text` excluded, `cdisc_class` renamed to `class`. ALL ASSERTIONS PASSED.

## Deviations from PLAN §6

**spec.py — 64 chunks vs ~50 expected for AE:**
AE spec.md contains H3 headings beyond variable entries (e.g. `### Model Definition` at the bottom). The plan estimated ~50 based on variable count; the actual file has 64 H3s. No code change needed — slicing on all H3s is correct per spec ("chunk by `^### `"). The extra headings are legitimate content.

**assumptions.py — 13 chunks for AE (overview + 12 items):**
AE assumptions.md has 12 numbered items (verified by sequential assert). Overview chunk is chunk_index=0 with section="overview". Item chunks are section="item_1" through "item_12".

**model.py — fallback for no H2s:**
Added a single-chunk fallback if a model file contains no H2 headings. This is defensive; all 6 current model files have H2s. No PLAN deviation.

## Contract Compliance

- All files use `from __future__ import annotations` (line 1).
- All chunks constructed via `self._new_chunk(**fields)` — auto-fills `kb_commit_sha`, `ingest_at`, `chunk_size_tokens` (tiktoken cl100k_base, L-3 compliant).
- All 18 Chunk fields explicitly set (None where not applicable, per F-15 / schema lock).
- `file_type` class attribute set correctly on each subclass.
- `domain` = parent dir name for spec/assumptions; `None` for model (not domain-specific).
- No modifications to `base.py`, `__init__.py`, or any Batch B/C files.
- Importable under Py 3.9 host: no `match` statement, no bare `X | Y` union annotations
  outside `from __future__ import annotations` guard.

## TODOs for 1A.4 Test-Engineer

1. **spec.py**: Test that H3s inside mermaid/code fences are not double-counted (base `heading_positions` does not filter protected blocks; spec files don't appear to have H3s in fences, but a regression test on a crafted fixture would confirm).
2. **assumptions.py**: Test a file with no overview text (first line is already `1. ...`) — overview chunk should be omitted.
3. **assumptions.py**: Test `item_num` non-contiguous numbering (e.g. items 1, 2, 10) — `section` should reflect actual number, sequential assert in smoke only checks AE.
4. **assumptions.py**: Test table preservation — a numbered item containing a GFM pipe-table should appear intact in the chunk text (no mid-table slice).
5. **model.py**: Test the no-H2 fallback path returns exactly 1 chunk with `section=None`.
6. **All chunkers**: Test `chunk_size_tokens` is non-zero and consistent with `count_tokens(text)` for a known fixture.
7. **All chunkers**: Test `to_metadata()` output keys match Chroma field expectations (no `text`, `class` present, all other fields present including None values).
