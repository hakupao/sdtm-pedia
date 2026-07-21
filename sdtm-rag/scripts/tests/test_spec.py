"""Tests for SpecChunker.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers.spec import SpecChunker

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def ae_chunks(kb_root):
    chunker = SpecChunker(kb_root)
    return chunker.chunk(kb_root / "domains" / "AE" / "spec.md")


@pytest.fixture(scope="module")
def dm_chunks(kb_root):
    chunker = SpecChunker(kb_root)
    return chunker.chunk(kb_root / "domains" / "DM" / "spec.md")


@pytest.fixture(scope="module")
def lb_chunks(kb_root):
    chunker = SpecChunker(kb_root)
    return chunker.chunk(kb_root / "domains" / "LB" / "spec.md")


# ---------------------------------------------------------------------------
# AE/spec.md: 64 chunks (matches 1A.3 integration smoke)
# ---------------------------------------------------------------------------

def test_ae_spec_produces_64_chunks(ae_chunks):
    """AE/spec.md produces exactly 64 chunks (verified by 1A.3 smoke)."""
    assert len(ae_chunks) == 64


def test_ae_spec_all_file_type_is_spec(ae_chunks):
    """All AE spec chunks have file_type == 'spec'."""
    for chunk in ae_chunks:
        assert chunk.file_type == "spec"


def test_ae_spec_all_domain_is_ae(ae_chunks):
    """All AE spec chunks have domain == 'AE'."""
    for chunk in ae_chunks:
        assert chunk.domain == "AE"


def test_ae_spec_all_have_section(ae_chunks):
    """All AE spec chunks have a non-empty section (H3 heading text)."""
    for chunk in ae_chunks:
        assert chunk.section is not None
        assert len(chunk.section.strip()) > 0


def test_ae_spec_chunk_size_tokens_positive_tiktoken(ae_chunks):
    """All AE spec chunks have chunk_size_tokens > 0 (tiktoken not char/4, L-3)."""
    for chunk in ae_chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0


def test_ae_spec_chunk_size_tokens_consistent_with_text(ae_chunks):
    """chunk_size_tokens matches count_tokens(text) for first 5 AE chunks."""
    from scripts.chunkers.base import count_tokens
    for chunk in ae_chunks[:5]:
        assert chunk.chunk_size_tokens == count_tokens(chunk.text)


def test_ae_spec_chunk_indices_sequential(ae_chunks):
    """AE spec chunk indices are 0, 1, 2, ... (sequential, no gaps)."""
    for i, chunk in enumerate(ae_chunks):
        assert chunk.chunk_index == i


# ---------------------------------------------------------------------------
# Multi-domain: DM and LB
# ---------------------------------------------------------------------------

def test_dm_spec_produces_nonzero_chunks(dm_chunks):
    """DM/spec.md produces at least 1 chunk."""
    assert len(dm_chunks) > 0


def test_dm_spec_domain_is_dm(dm_chunks):
    """All DM spec chunks have domain == 'DM'."""
    for chunk in dm_chunks:
        assert chunk.domain == "DM"


def test_lb_spec_produces_nonzero_chunks(lb_chunks):
    """LB/spec.md produces at least 1 chunk."""
    assert len(lb_chunks) > 0


def test_lb_spec_domain_is_lb(lb_chunks):
    """All LB spec chunks have domain == 'LB'."""
    for chunk in lb_chunks:
        assert chunk.domain == "LB"


# ---------------------------------------------------------------------------
# 18-field metadata completeness
# ---------------------------------------------------------------------------

_EXPECTED_META_KEYS = {
    "source", "chunk_index", "file_type", "domain", "class",
    "section", "cdisc_section_id", "example_index", "sub_label",
    "has_mermaid", "has_table", "ct_code", "ct_extensible",
    "part_index", "table_chunk_idx", "chunk_size_tokens",
    "kb_commit_sha", "ingest_at",
}


def test_ae_spec_to_metadata_has_all_18_keys(ae_chunks):
    """to_metadata() on AE spec chunk has all 18 expected keys."""
    meta = ae_chunks[0].to_metadata()
    assert set(meta.keys()) == _EXPECTED_META_KEYS
