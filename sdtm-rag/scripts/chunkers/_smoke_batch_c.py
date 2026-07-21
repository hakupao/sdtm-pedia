"""Self-smoke for Batch C chunkers: chapters, terminology, variable_index.

Run from repo root:
    python sdtm-rag/scripts/chunkers/_smoke_batch_c.py

Or from sdtm-rag/:
    python scripts/chunkers/_smoke_batch_c.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure sdtm-rag/ is on sys.path so `scripts.chunkers` resolves
_HERE = Path(__file__).resolve()
_SDTM_RAG = _HERE.parents[2]  # sdtm-rag/
sys.path.insert(0, str(_SDTM_RAG))

from scripts.chunkers.chapters import ChaptersChunker
from scripts.chunkers.terminology import TerminologyChunker
from scripts.chunkers.variable_index import VariableIndexChunker

# KB root is 4 levels up:
#   _smoke_batch_c.py -> chunkers/ -> scripts/ -> sdtm-rag/ -> sdtm-pedia/
_KB_ROOT = _HERE.parents[3] / "knowledge_base"
assert _KB_ROOT.exists(), f"KB root not found: {_KB_ROOT}"

print(f"KB root: {_KB_ROOT}")
print()


def _row(label: str, expected: object, actual: object, ok: bool) -> str:
    mark = "PASS" if ok else "FAIL"
    return f"  [{mark}] {label:<48} expected={expected!s:<20} actual={actual!s}"


_failures: list[str] = []


def _check(label: str, expected: object, actual: object) -> None:
    ok = (expected == actual)
    print(_row(label, expected, actual, ok))
    if not ok:
        _failures.append(label)


def _check_ge(label: str, lo: int, actual: int) -> None:
    ok = actual >= lo
    print(_row(label, f">={lo}", actual, ok))
    if not ok:
        _failures.append(label)


# ── ChaptersChunker ──────────────────────────────────────────────────────────
print("=== ChaptersChunker ===")
ch_chunker = ChaptersChunker(kb_root=_KB_ROOT.parent)

ch01 = _KB_ROOT / "chapters" / "ch01_introduction.md"
ch04 = _KB_ROOT / "chapters" / "ch04_general_assumptions.md"
ch08 = _KB_ROOT / "chapters" / "ch08_relationships.md"
for p in (ch01, ch04, ch08):
    assert p.exists(), f"missing chapter: {p}"

ch01_chunks = ch_chunker.chunk(ch01)
ch04_chunks = ch_chunker.chunk(ch04)
ch08_chunks = ch_chunker.chunk(ch08)

# ch01 ≤20KB → whole_file, 1 chunk
_check("ch01 chunk count (≤20KB → 1 whole)", 1, len(ch01_chunks))
_check("ch01 chunk[0].section", "whole_file", ch01_chunks[0].section)

# ch04 >50KB → ### split, 47 chunks per grep -c '^### ' (counted earlier)
_check("ch04 chunk count (>50KB → ### split = 47)", 47, len(ch04_chunks))
# ch04 first ### is "4.1.1 Review Study Data Tabulation Model and Implementation Guide"
_check_ge("ch04 chunk[0].section starts with '4.1.1'",
          1, int(ch04_chunks[0].section.startswith("4.1.1")))
_check("ch04 chunk[0].cdisc_section_id", "4.1.1", ch04_chunks[0].cdisc_section_id)

# ch08 ≈52KB >50KB → ### split (grep gave 19)
_check("ch08 chunk count (>50KB → ### split = 19)", 19, len(ch08_chunks))

# Common chapter invariants
for c in ch01_chunks + ch04_chunks + ch08_chunks:
    assert c.file_type == "chapter", f"file_type mismatch: {c.file_type}"
    assert c.domain is None, f"domain not None for chapter chunk: {c.domain}"
    assert c.chunk_size_tokens is not None, "missing chunk_size_tokens"

# ch04 invariant: every chunk should be < 8K tokens (L-4 sanity)
max_ch04 = max(c.chunk_size_tokens for c in ch04_chunks)
_check_ge("ch04 max chunk token < 8000", 1, int(max_ch04 < 8000))
print(f"  ch04 token range: {min(c.chunk_size_tokens for c in ch04_chunks)}–{max_ch04}")
print()


# ── TerminologyChunker ───────────────────────────────────────────────────────
print("=== TerminologyChunker ===")
tm_chunker = TerminologyChunker(kb_root=_KB_ROOT.parent)

ae = _KB_ROOT / "terminology" / "core" / "ae.md"
lb1 = _KB_ROOT / "terminology" / "core" / "lb_part1.md"
lb4 = _KB_ROOT / "terminology" / "core" / "lb_part4.md"
q1 = _KB_ROOT / "terminology" / "questionnaires" / "questionnaires_part1.md"
for p in (ae, lb1, lb4, q1):
    assert p.exists(), f"missing terminology: {p}"

ae_chunks = tm_chunker.chunk(ae)
lb1_chunks = tm_chunker.chunk(lb1)
lb4_chunks = tm_chunker.chunk(lb4)
q1_chunks = tm_chunker.chunk(q1)

# ae: 4 H2 codelists → 4 chunks codelist mode
_check("ae.md chunk count (4 H2 codelist)", 4, len(ae_chunks))
_check("ae.md chunk[0].ct_code", "C66767", ae_chunks[0].ct_code)
_check("ae.md chunk[0].section",
       "Action Taken with Study Treatment", ae_chunks[0].section)
_check("ae.md chunk[0].part_index (no _part suffix)", None, ae_chunks[0].part_index)

# lb_part1: 1 H2 + _part1 name → part mode, 1 chunk
_check("lb_part1.md chunk count (1 H2, _part1 → part mode)", 1, len(lb1_chunks))
_check("lb_part1.md chunk[0].part_index", 1, lb1_chunks[0].part_index)
_check("lb_part1.md chunk[0].section (stem)", "lb_part1", lb1_chunks[0].section)
_check("lb_part1.md chunk[0].ct_code (None in part mode)", None, lb1_chunks[0].ct_code)

# lb_part4: 2 H2 → codelist mode (HARD requirement)
_check("lb_part4.md chunk count (2 H2 → codelist mode)", 2, len(lb4_chunks))
_check("lb_part4.md chunk[0].ct_code", "C102580", lb4_chunks[0].ct_code)
_check("lb_part4.md chunk[1].ct_code", "C179589", lb4_chunks[1].ct_code)
_check("lb_part4.md chunk[0].part_index (filename has _part4)",
       4, lb4_chunks[0].part_index)

# questionnaires_part1: 66 H2 → codelist mode, 66 chunks
_check("questionnaires_part1.md chunk count (66 H2)", 66, len(q1_chunks))

for c in ae_chunks + lb1_chunks + lb4_chunks + q1_chunks:
    assert c.file_type == "terminology", f"file_type mismatch: {c.file_type}"
    assert c.chunk_size_tokens is not None, "missing chunk_size_tokens"
print()


# ── VariableIndexChunker ─────────────────────────────────────────────────────
print("=== VariableIndexChunker ===")
vi_chunker = VariableIndexChunker(kb_root=_KB_ROOT.parent)
vi = _KB_ROOT / "VARIABLE_INDEX.md"
assert vi.exists(), f"missing: {vi}"

vi_chunks = vi_chunker.chunk(vi)
# 1 (§一) + 63 (§二) + 1 (§三 single chunk) = 65
_check("VARIABLE_INDEX total chunks (1 + 63 + 1 = 65)", 65, len(vi_chunks))

# Chunk[0] is §一
_check_ge("VARIABLE_INDEX chunk[0].section starts with '§一'",
          1, int(vi_chunks[0].section.startswith("§一")))
# Chunks 1..63 are §二 H3 sections; first one should be AE
_check("VARIABLE_INDEX chunk[1].domain (first §二, AE)", "AE", vi_chunks[1].domain)
_check("VARIABLE_INDEX chunk[1].cdisc_class (AE Events)", "Events", vi_chunks[1].cdisc_class)
# Chunk[-1] is §三
_check_ge("VARIABLE_INDEX chunk[-1].section starts with '§三'",
          1, int(vi_chunks[-1].section.startswith("§三")))

# All §二 chunks must have a domain set (positions 1..-2 inclusive)
er_chunks = vi_chunks[1:-1]
_check("VARIABLE_INDEX §二 chunk count (= 63)", 63, len(er_chunks))
all_with_domain = all(c.domain for c in er_chunks)
_check("VARIABLE_INDEX all §二 chunks have domain set",
       True, all_with_domain)

for c in vi_chunks:
    assert c.file_type == "variable_index", f"file_type mismatch: {c.file_type}"
    assert c.chunk_size_tokens is not None, "missing chunk_size_tokens"

# Cross-check to_metadata()
for c in ch01_chunks + ch04_chunks + ae_chunks + lb1_chunks + lb4_chunks + vi_chunks:
    meta = c.to_metadata()
    assert "text" not in meta
    assert "class" in meta

print()
print("=" * 70)
if _failures:
    print(f"FAILURES ({len(_failures)}):")
    for f in _failures:
        print(f"  - {f}")
    sys.exit(1)
print("ALL ASSERTIONS PASSED")
