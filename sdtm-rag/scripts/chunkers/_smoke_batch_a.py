"""Self-smoke for Batch A chunkers: spec, assumptions, model.

Run from repo root:
    python branches/07_rag_kg/sdtm-rag/scripts/chunkers/_smoke_batch_a.py

Or from sdtm-rag/:
    python scripts/chunkers/_smoke_batch_a.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure sdtm-rag/ is on sys.path so `scripts.chunkers` resolves
_HERE = Path(__file__).resolve()
_SDTM_RAG = _HERE.parents[2]  # sdtm-rag/
sys.path.insert(0, str(_SDTM_RAG))

from scripts.chunkers.assumptions import AssumptionsChunker
from scripts.chunkers.model import ModelChunker
from scripts.chunkers.spec import SpecChunker

# KB root is 4 levels up from this file:
#   _smoke_batch_a.py -> chunkers/ -> scripts/ -> sdtm-rag/ -> branches/07_rag_kg/ -> sdtm-pedia/
# knowledge_base/ lives at sdtm-pedia/knowledge_base/
_KB_ROOT = _HERE.parents[5] / "knowledge_base"
assert _KB_ROOT.exists(), f"KB root not found: {_KB_ROOT}"

print(f"KB root: {_KB_ROOT}")
print()

# ── SpecChunker ──────────────────────────────────────────────────────────────
spec_chunker = SpecChunker(kb_root=_KB_ROOT.parent)  # repo root as kb_root arg
ae_spec = _KB_ROOT / "domains" / "AE" / "spec.md"
assert ae_spec.exists(), f"Not found: {ae_spec}"

spec_chunks = spec_chunker.chunk(ae_spec)
assert len(spec_chunks) > 30, f"AE spec expected >30 chunks, got {len(spec_chunks)}"
assert all(c.file_type == "spec" for c in spec_chunks), "file_type mismatch in spec chunks"
assert all(c.domain == "AE" for c in spec_chunks), "domain mismatch in spec chunks"
assert all(c.chunk_size_tokens is not None for c in spec_chunks), "missing chunk_size_tokens"

print(f"[spec]  AE spec.md  → {len(spec_chunks)} chunks")
print(f"        first section : {spec_chunks[0].section!r}")
print(f"        last  section : {spec_chunks[-1].section!r}")
print(f"        tokens range  : {min(c.chunk_size_tokens for c in spec_chunks)}"
      f"–{max(c.chunk_size_tokens for c in spec_chunks)}")
print()

# ── AssumptionsChunker ───────────────────────────────────────────────────────
assump_chunker = AssumptionsChunker(kb_root=_KB_ROOT.parent)
ae_assump = _KB_ROOT / "domains" / "AE" / "assumptions.md"
assert ae_assump.exists(), f"Not found: {ae_assump}"

assump_chunks = assump_chunker.chunk(ae_assump)
assert len(assump_chunks) > 1, f"AE assumptions expected >1 chunks, got {len(assump_chunks)}"
assert all(c.file_type == "assumptions" for c in assump_chunks), "file_type mismatch in assumptions chunks"
assert all(c.domain == "AE" for c in assump_chunks), "domain mismatch in assumptions chunks"
assert assump_chunks[0].section in ("overview", "item_1"), \
    f"Unexpected first section: {assump_chunks[0].section!r}"

print(f"[assumptions]  AE assumptions.md  → {len(assump_chunks)} chunks")
print(f"               first section : {assump_chunks[0].section!r}")
print(f"               last  section : {assump_chunks[-1].section!r}")
# Check that item numbers are sequential
item_chunks = [c for c in assump_chunks if c.section and c.section.startswith("item_")]
item_nums = [int(c.section.split("_")[1]) for c in item_chunks]
assert item_nums == list(range(1, len(item_nums) + 1)), \
    f"Non-sequential item numbers: {item_nums}"
print(f"               item sections : {item_nums[0]}–{item_nums[-1]} (sequential ✓)")
print()

# ── ModelChunker ─────────────────────────────────────────────────────────────
model_chunker = ModelChunker(kb_root=_KB_ROOT.parent)
model_file = _KB_ROOT / "model" / "01_concepts_and_terms.md"
assert model_file.exists(), f"Not found: {model_file}"

model_chunks = model_chunker.chunk(model_file)
assert len(model_chunks) > 0, f"model chunks expected >0, got {len(model_chunks)}"
assert all(c.file_type == "model" for c in model_chunks), "file_type mismatch in model chunks"
assert all(c.domain is None for c in model_chunks), "model chunks should have domain=None"

print(f"[model]  01_concepts_and_terms.md  → {len(model_chunks)} chunks")
print(f"         first section : {model_chunks[0].section!r}")
print(f"         last  section : {model_chunks[-1].section!r}")
print(f"         tokens range  : {min(c.chunk_size_tokens for c in model_chunks)}"
      f"–{max(c.chunk_size_tokens for c in model_chunks)}")
print()

# ── Cross-check: to_metadata() works for all chunks ─────────────────────────
for c in spec_chunks + assump_chunks + model_chunks:
    meta = c.to_metadata()
    assert "text" not in meta, "to_metadata() must exclude text field"
    assert "class" in meta, "to_metadata() must rename cdisc_class -> class"

print("to_metadata() OK for all chunks ✓")
print()
print("ALL ASSERTIONS PASSED ✓")
