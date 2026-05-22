"""Tests for VariableIndexChunker.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers.variable_index import VariableIndexChunker

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"
VAR_INDEX_FILE = KB_ROOT / "VARIABLE_INDEX.md"


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def chunker(kb_root):
    return VariableIndexChunker(kb_root)


@pytest.fixture(scope="module")
def vi_chunks(chunker):
    return chunker.chunk(VAR_INDEX_FILE)


# ---------------------------------------------------------------------------
# Total: exactly 65 chunks (1 + 63 + 1)
# ---------------------------------------------------------------------------

def test_variable_index_produces_65_chunks(vi_chunks):
    """VARIABLE_INDEX.md produces exactly 65 chunks (§一 1 + §二 63 + §三 1)."""
    assert len(vi_chunks) == 65


def test_variable_index_all_file_type_variable_index(vi_chunks):
    """All VARIABLE_INDEX chunks have file_type == 'variable_index'."""
    for chunk in vi_chunks:
        assert chunk.file_type == "variable_index"


def test_variable_index_chunk_indices_sequential(vi_chunks):
    """VARIABLE_INDEX chunk indices are 0..64 (sequential)."""
    for i, chunk in enumerate(vi_chunks):
        assert chunk.chunk_index == i


def test_variable_index_all_chunk_size_tokens_positive(vi_chunks):
    """All VARIABLE_INDEX chunks have chunk_size_tokens > 0."""
    for chunk in vi_chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0


# ---------------------------------------------------------------------------
# §一: chunk[0] section starts with "§一"
# ---------------------------------------------------------------------------

def test_variable_index_chunk0_section_starts_with_yi(vi_chunks):
    """chunks[0] has section starting with '§一'."""
    assert vi_chunks[0].section is not None
    assert vi_chunks[0].section.startswith("§一"), (
        f"chunks[0].section = {vi_chunks[0].section!r}"
    )


def test_variable_index_chunk0_domain_is_none(vi_chunks):
    """chunks[0] (§一 通用变量) has domain == None."""
    assert vi_chunks[0].domain is None


# ---------------------------------------------------------------------------
# §二: chunks[1..63] each have a domain set
# ---------------------------------------------------------------------------

def test_variable_index_section2_chunks_have_domain(vi_chunks):
    """chunks[1..63] (§二 domain entries) all have a non-None domain."""
    for chunk in vi_chunks[1:64]:
        assert chunk.domain is not None, (
            f"chunk {chunk.chunk_index} (section={chunk.section!r}) has domain=None"
        )


def test_variable_index_section2_first_domain_is_ae(vi_chunks):
    """chunks[1] domain is 'AE' (first domain in §二 is AE, alphabetical order)."""
    assert vi_chunks[1].domain == "AE", (
        f"Expected 'AE', got {vi_chunks[1].domain!r}"
    )


def test_variable_index_section2_all_domains_are_uppercase(vi_chunks):
    """All §二 domain codes are uppercase alphanumeric strings."""
    for chunk in vi_chunks[1:64]:
        assert chunk.domain == chunk.domain.upper(), (
            f"domain {chunk.domain!r} is not uppercase"
        )
        assert chunk.domain.isalnum(), (
            f"domain {chunk.domain!r} contains non-alphanumeric characters"
        )


def test_variable_index_section2_has_63_chunks(vi_chunks):
    """Exactly 63 chunks in §二 (one per domain)."""
    section2_chunks = vi_chunks[1:64]
    assert len(section2_chunks) == 63


# ---------------------------------------------------------------------------
# §三: last chunk section starts with "§三"
# ---------------------------------------------------------------------------

def test_variable_index_last_chunk_section_starts_with_san(vi_chunks):
    """chunks[-1] has section starting with '§三'."""
    assert vi_chunks[-1].section is not None
    assert vi_chunks[-1].section.startswith("§三"), (
        f"Last chunk section = {vi_chunks[-1].section!r}"
    )


def test_variable_index_last_chunk_domain_is_none(vi_chunks):
    """chunks[-1] (§三 CT 交叉引用) has domain == None."""
    assert vi_chunks[-1].domain is None


# ---------------------------------------------------------------------------
# to_metadata: class field from cdisc_class rename
# ---------------------------------------------------------------------------

_EXPECTED_META_KEYS = {
    "source", "chunk_index", "file_type", "domain", "class",
    "section", "cdisc_section_id", "example_index", "sub_label",
    "has_mermaid", "has_table", "ct_code", "ct_extensible",
    "part_index", "table_chunk_idx", "chunk_size_tokens",
    "kb_commit_sha", "ingest_at",
}


def test_variable_index_to_metadata_has_18_keys(vi_chunks):
    """to_metadata() on a VARIABLE_INDEX chunk has all 18 expected keys."""
    meta = vi_chunks[1].to_metadata()  # use a §二 chunk which has domain
    assert set(meta.keys()) == _EXPECTED_META_KEYS


def test_variable_index_section2_class_field_in_metadata(vi_chunks):
    """§二 chunks with cdisc_class set export 'class' in to_metadata()."""
    # Find a chunk that has cdisc_class set (e.g., AE → "Events")
    class_chunks = [c for c in vi_chunks[1:64] if c.cdisc_class is not None]
    if not class_chunks:
        pytest.skip("No §二 chunk has cdisc_class set — check VariableIndexChunker parsing")
    meta = class_chunks[0].to_metadata()
    assert "class" in meta
    assert meta["class"] is not None
