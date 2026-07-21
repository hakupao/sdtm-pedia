"""Integration tests using CHUNKER_REGISTRY dispatch.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers import CHUNKER_REGISTRY

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"

_EXPECTED_META_KEYS = {
    "source", "chunk_index", "file_type", "domain", "class",
    "section", "cdisc_section_id", "example_index", "sub_label",
    "has_mermaid", "has_table", "ct_code", "ct_extensible",
    "part_index", "table_chunk_idx", "chunk_size_tokens",
    "kb_commit_sha", "ingest_at",
}


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


# ---------------------------------------------------------------------------
# CHUNKER_REGISTRY smoke: all 7 file_types are registered
# ---------------------------------------------------------------------------

def test_registry_has_7_chunker_types():
    """CHUNKER_REGISTRY contains exactly 7 file_type keys."""
    assert len(CHUNKER_REGISTRY) == 7


def test_registry_has_all_expected_file_types():
    """CHUNKER_REGISTRY contains all 7 expected file_type keys."""
    expected = {"spec", "assumptions", "model", "examples", "chapter", "terminology", "variable_index"}
    assert set(CHUNKER_REGISTRY.keys()) == expected


# ---------------------------------------------------------------------------
# Registry dispatch samples: (file_type, relative path inside kb_root)
# ---------------------------------------------------------------------------

_REGISTRY_SAMPLES = [
    ("spec",         "domains/AE/spec.md"),
    ("assumptions",  "domains/AE/assumptions.md"),
    ("model",        "model/01_concepts_and_terms.md"),
    ("examples",     "domains/TA/examples.md"),
    ("chapter",      "chapters/ch01_introduction.md"),
    ("terminology",  "terminology/core/ae.md"),
    ("variable_index", "VARIABLE_INDEX.md"),
]


@pytest.mark.parametrize("file_type,rel_path", _REGISTRY_SAMPLES)
def test_registry_dispatch_produces_nonzero_chunks(kb_root, file_type, rel_path):
    """CHUNKER_REGISTRY dispatch produces at least 1 chunk for each sample."""
    chunker_cls = CHUNKER_REGISTRY[file_type]
    chunker = chunker_cls(kb_root)
    chunks = chunker.chunk(kb_root / rel_path)
    assert len(chunks) > 0, f"No chunks for {rel_path}"


@pytest.mark.parametrize("file_type,rel_path", _REGISTRY_SAMPLES)
def test_registry_dispatch_all_chunks_have_18_metadata_keys(kb_root, file_type, rel_path):
    """All chunks from registry dispatch have exactly 18 keys in to_metadata()."""
    chunker_cls = CHUNKER_REGISTRY[file_type]
    chunker = chunker_cls(kb_root)
    chunks = chunker.chunk(kb_root / rel_path)
    for chunk in chunks:
        meta = chunk.to_metadata()
        assert set(meta.keys()) == _EXPECTED_META_KEYS, (
            f"{rel_path} chunk {chunk.chunk_index}: metadata keys mismatch: "
            f"extra={set(meta.keys()) - _EXPECTED_META_KEYS}, "
            f"missing={_EXPECTED_META_KEYS - set(meta.keys())}"
        )


@pytest.mark.parametrize("file_type,rel_path", _REGISTRY_SAMPLES)
def test_registry_dispatch_all_chunks_size_tokens_positive(kb_root, file_type, rel_path):
    """All chunks from registry dispatch have chunk_size_tokens > 0 (tiktoken L-3)."""
    chunker_cls = CHUNKER_REGISTRY[file_type]
    chunker = chunker_cls(kb_root)
    chunks = chunker.chunk(kb_root / rel_path)
    for chunk in chunks:
        assert chunk.chunk_size_tokens is not None, (
            f"{rel_path} chunk {chunk.chunk_index} has chunk_size_tokens=None"
        )
        assert chunk.chunk_size_tokens > 0, (
            f"{rel_path} chunk {chunk.chunk_index} has chunk_size_tokens={chunk.chunk_size_tokens}"
        )


@pytest.mark.parametrize("file_type,rel_path", _REGISTRY_SAMPLES)
def test_registry_dispatch_file_type_matches_registry_key(kb_root, file_type, rel_path):
    """Each chunk's file_type field matches the registry dispatch key."""
    chunker_cls = CHUNKER_REGISTRY[file_type]
    chunker = chunker_cls(kb_root)
    chunks = chunker.chunk(kb_root / rel_path)
    for chunk in chunks:
        assert chunk.file_type == file_type, (
            f"{rel_path}: chunk.file_type={chunk.file_type!r} != registry key {file_type!r}"
        )


# ---------------------------------------------------------------------------
# Idempotence: calling chunk() twice returns same count
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("file_type,rel_path", _REGISTRY_SAMPLES)
def test_registry_dispatch_idempotent(kb_root, file_type, rel_path):
    """Calling chunk() twice on the same file produces the same number of chunks."""
    chunker_cls = CHUNKER_REGISTRY[file_type]
    chunker = chunker_cls(kb_root)
    path = kb_root / rel_path
    count1 = len(chunker.chunk(path))
    count2 = len(chunker.chunk(path))
    assert count1 == count2, (
        f"{rel_path}: first call={count1}, second call={count2} (non-idempotent)"
    )


# ---------------------------------------------------------------------------
# Cross-check: individual chunker calls vs registry dispatch match
# ---------------------------------------------------------------------------

def test_registry_individual_vs_registry_spec_chunk_count(kb_root):
    """SpecChunker direct call produces same count as CHUNKER_REGISTRY['spec'] dispatch."""
    from scripts.chunkers.spec import SpecChunker
    path = kb_root / "domains" / "AE" / "spec.md"
    direct = SpecChunker(kb_root).chunk(path)
    via_registry = CHUNKER_REGISTRY["spec"](kb_root).chunk(path)
    assert len(direct) == len(via_registry)


def test_registry_individual_vs_registry_chapters_chunk_count(kb_root):
    """ChaptersChunker direct call produces same count as CHUNKER_REGISTRY['chapter'] dispatch."""
    from scripts.chunkers.chapters import ChaptersChunker
    path = kb_root / "chapters" / "ch04_general_assumptions.md"
    direct = ChaptersChunker(kb_root).chunk(path)
    via_registry = CHUNKER_REGISTRY["chapter"](kb_root).chunk(path)
    assert len(direct) == len(via_registry)


def test_registry_individual_vs_registry_variable_index_chunk_count(kb_root):
    """VariableIndexChunker direct call produces same count as registry dispatch."""
    from scripts.chunkers.variable_index import VariableIndexChunker
    path = kb_root / "VARIABLE_INDEX.md"
    direct = VariableIndexChunker(kb_root).chunk(path)
    via_registry = CHUNKER_REGISTRY["variable_index"](kb_root).chunk(path)
    assert len(direct) == len(via_registry)
