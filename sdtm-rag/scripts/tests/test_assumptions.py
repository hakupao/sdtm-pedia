"""Tests for AssumptionsChunker.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers.assumptions import AssumptionsChunker

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def ae_chunks(kb_root):
    chunker = AssumptionsChunker(kb_root)
    return chunker.chunk(kb_root / "domains" / "AE" / "assumptions.md")


@pytest.fixture(scope="module")
def dm_chunks(kb_root):
    chunker = AssumptionsChunker(kb_root)
    return chunker.chunk(kb_root / "domains" / "DM" / "assumptions.md")


@pytest.fixture(scope="module")
def di_chunks(kb_root):
    chunker = AssumptionsChunker(kb_root)
    return chunker.chunk(kb_root / "domains" / "DI" / "assumptions.md")


# ---------------------------------------------------------------------------
# AE/assumptions.md: 13 chunks (1 overview + 12 items)
# ---------------------------------------------------------------------------

def test_ae_assumptions_produces_13_chunks(ae_chunks):
    """AE/assumptions.md produces exactly 13 chunks (1 overview + 12 items)."""
    assert len(ae_chunks) == 13


def test_ae_assumptions_first_chunk_section_is_overview(ae_chunks):
    """First AE assumptions chunk has section == 'overview'."""
    assert ae_chunks[0].section == "overview"


def test_ae_assumptions_subsequent_chunks_section_item_n(ae_chunks):
    """Chunks 1..12 have section == 'item_N' for N = 1..12."""
    for chunk in ae_chunks[1:]:
        assert chunk.section is not None
        assert chunk.section.startswith("item_")
        num_str = chunk.section[len("item_"):]
        assert num_str.isdigit(), f"Non-numeric item suffix: {chunk.section!r}"


def test_ae_assumptions_item_sections_cover_1_to_12(ae_chunks):
    """AE assumptions item chunks cover items 1 through 12 (no gaps)."""
    item_nums = sorted(
        int(c.section[len("item_"):]) for c in ae_chunks[1:]
    )
    assert item_nums == list(range(1, 13))


def test_ae_assumptions_all_file_type_assumptions(ae_chunks):
    """All AE assumptions chunks have file_type == 'assumptions'."""
    for chunk in ae_chunks:
        assert chunk.file_type == "assumptions"


def test_ae_assumptions_all_domain_ae(ae_chunks):
    """All AE assumptions chunks have domain == 'AE'."""
    for chunk in ae_chunks:
        assert chunk.domain == "AE"


def test_ae_assumptions_chunk_size_tokens_positive(ae_chunks):
    """All AE assumptions chunks have chunk_size_tokens > 0."""
    for chunk in ae_chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0


def test_ae_assumptions_chunk_indices_sequential(ae_chunks):
    """AE assumptions chunk indices are sequential starting at 0."""
    for i, chunk in enumerate(ae_chunks):
        assert chunk.chunk_index == i


# ---------------------------------------------------------------------------
# DI/assumptions.md: DI Issue 15 fix — only has assumptions, no spec/examples
# ---------------------------------------------------------------------------

def test_di_assumptions_produces_nonzero_chunks(di_chunks):
    """DI/assumptions.md produces at least 1 chunk (DI only has assumptions file)."""
    assert len(di_chunks) > 0


def test_di_assumptions_domain_is_di(di_chunks):
    """All DI assumptions chunks have domain == 'DI'."""
    for chunk in di_chunks:
        assert chunk.domain == "DI"


# ---------------------------------------------------------------------------
# DM/assumptions.md: multi-domain smoke
# ---------------------------------------------------------------------------

def test_dm_assumptions_produces_nonzero_chunks(dm_chunks):
    """DM/assumptions.md produces at least 1 chunk."""
    assert len(dm_chunks) > 0


def test_dm_assumptions_domain_is_dm(dm_chunks):
    """All DM assumptions chunks have domain == 'DM'."""
    for chunk in dm_chunks:
        assert chunk.domain == "DM"


# ---------------------------------------------------------------------------
# Edge: file with no overview (first line is already a numbered item)
# ---------------------------------------------------------------------------

def test_overview_chunk_omitted_when_file_starts_with_numbered_item(kb_root, tmp_path):
    """When file starts directly with '1. ...', no overview chunk is emitted."""
    fake_file = tmp_path / "fake" / "assumptions.md"
    fake_file.parent.mkdir(parents=True)
    fake_file.write_text(
        "1. First item text here.\n\n2. Second item text here.\n",
        encoding="utf-8",
    )
    chunker = AssumptionsChunker(kb_root)
    chunks = chunker.chunk(fake_file)
    sections = [c.section for c in chunks]
    assert "overview" not in sections
    assert all(s.startswith("item_") for s in sections)


# ---------------------------------------------------------------------------
# Edge: non-contiguous item numbering
# ---------------------------------------------------------------------------

def test_item_section_reflects_actual_number_not_sequential_index(kb_root, tmp_path):
    """section='item_N' uses the actual number in the text, not a sequential counter."""
    fake_file = tmp_path / "fake2" / "assumptions.md"
    fake_file.parent.mkdir(parents=True)
    fake_file.write_text(
        "Overview text.\n\n1. First item.\n\n2. Second item.\n\n10. Tenth item.\n",
        encoding="utf-8",
    )
    chunker = AssumptionsChunker(kb_root)
    chunks = chunker.chunk(fake_file)
    sections = [c.section for c in chunks]
    assert "item_1" in sections
    assert "item_2" in sections
    assert "item_10" in sections


# ---------------------------------------------------------------------------
# Edge: table preserved within a numbered item (no mid-table slice)
# ---------------------------------------------------------------------------

def test_gfm_table_preserved_within_item_chunk(kb_root, tmp_path):
    """A GFM pipe-table inside a numbered item remains intact in that item's chunk text."""
    table = "| Col A | Col B |\n|-------|-------|\n| val1  | val2  |\n| val3  | val4  |\n"
    fake_file = tmp_path / "fake3" / "assumptions.md"
    fake_file.parent.mkdir(parents=True)
    fake_file.write_text(
        f"Overview text.\n\n1. Item with a table:\n\n{table}\n2. Next item.\n",
        encoding="utf-8",
    )
    chunker = AssumptionsChunker(kb_root)
    chunks = chunker.chunk(fake_file)
    item1_chunk = next(c for c in chunks if c.section == "item_1")
    assert "| Col A | Col B |" in item1_chunk.text
    assert "| val3  | val4  |" in item1_chunk.text
