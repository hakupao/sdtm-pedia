"""Tests for ChaptersChunker. CRITICAL: L-4 size-aware split lock.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers.chapters import ChaptersChunker

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"
CHAPTERS_DIR = KB_ROOT / "chapters"


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def chunker(kb_root):
    return ChaptersChunker(kb_root)


@pytest.fixture(scope="module")
def ch01_chunks(chunker):
    return chunker.chunk(CHAPTERS_DIR / "ch01_introduction.md")


@pytest.fixture(scope="module")
def ch04_chunks(chunker):
    return chunker.chunk(CHAPTERS_DIR / "ch04_general_assumptions.md")


@pytest.fixture(scope="module")
def ch08_chunks(chunker):
    return chunker.chunk(CHAPTERS_DIR / "ch08_relationships.md")


@pytest.fixture(scope="module")
def ch10_chunks(chunker):
    return chunker.chunk(CHAPTERS_DIR / "ch10_appendices.md")


# ---------------------------------------------------------------------------
# ch01 (~11KB, ≤20KB tier): 1 chunk, section == "whole_file"
# ---------------------------------------------------------------------------

def test_ch01_produces_1_chunk(ch01_chunks):
    """ch01 (11KB ≤ 20KB) produces exactly 1 chunk (whole_file tier)."""
    assert len(ch01_chunks) == 1


def test_ch01_section_is_whole_file(ch01_chunks):
    """ch01 single chunk has section == 'whole_file'."""
    assert ch01_chunks[0].section == "whole_file"


def test_ch01_file_type_is_chapter(ch01_chunks):
    """ch01 chunk has file_type == 'chapter'."""
    assert ch01_chunks[0].file_type == "chapter"


def test_ch01_domain_is_none(ch01_chunks):
    """ch01 chunk has domain == None (chapters are not domain-specific)."""
    assert ch01_chunks[0].domain is None


# ---------------------------------------------------------------------------
# ch04 (~130KB, >50KB tier): L-4 lock — must use ### split, max tokens < 8000
# ---------------------------------------------------------------------------

def test_ch04_produces_47_chunks(ch04_chunks):
    """ch04 (130KB > 50KB) produces exactly 47 chunks via ### split (L-4 lock)."""
    assert len(ch04_chunks) == 47


def test_ch04_l4_lock_max_chunk_size_tokens_under_8000(ch04_chunks):
    """L-4 HARD REQUIREMENT: all ch04 chunks have chunk_size_tokens < 8000.

    This directly verifies the fix for ch04 §4.4 = 9598 tokens (over embedding limit)
    when split at ## level. ### split keeps max at 3852 (1A.3 verified).
    """
    max_tokens = max(c.chunk_size_tokens for c in ch04_chunks)
    assert max_tokens < 8000, (
        f"L-4 VIOLATION: ch04 has chunk with {max_tokens} tokens >= 8000. "
        "The ### split must be used for >50KB chapters."
    )


def test_ch04_all_file_type_chapter(ch04_chunks):
    """All ch04 chunks have file_type == 'chapter'."""
    for chunk in ch04_chunks:
        assert chunk.file_type == "chapter"


def test_ch04_all_domain_none(ch04_chunks):
    """All ch04 chunks have domain == None."""
    for chunk in ch04_chunks:
        assert chunk.domain is None


def test_ch04_chunk_indices_sequential(ch04_chunks):
    """ch04 chunk indices are sequential starting at 0."""
    for i, chunk in enumerate(ch04_chunks):
        assert chunk.chunk_index == i


def test_ch04_first_chunk_has_cdisc_section_id(ch04_chunks):
    """First ch04 chunk has a cdisc_section_id parsed from the ### heading."""
    # ch04 headings are like "### 4.1.1 Title" → section_id = "4.1.1"
    assert ch04_chunks[0].cdisc_section_id is not None
    assert "." in ch04_chunks[0].cdisc_section_id  # e.g. "4.1.1"


# ---------------------------------------------------------------------------
# ch08 (~52KB, >50KB tier): 19 ### chunks
# ---------------------------------------------------------------------------

def test_ch08_produces_19_chunks(ch08_chunks):
    """ch08 (52KB > 50KB) produces exactly 19 chunks via ### split."""
    assert len(ch08_chunks) == 19


def test_ch08_file_type_chapter(ch08_chunks):
    """All ch08 chunks have file_type == 'chapter'."""
    for chunk in ch08_chunks:
        assert chunk.file_type == "chapter"


def test_ch08_max_tokens_under_8000(ch08_chunks):
    """All ch08 chunks stay under 8000 tokens (embedding limit safety)."""
    max_tokens = max(c.chunk_size_tokens for c in ch08_chunks)
    assert max_tokens < 8000, f"ch08 chunk max tokens = {max_tokens}"


# ---------------------------------------------------------------------------
# ch10 (~30KB, 20-50KB tier): uses ^## split (level 2)
# ---------------------------------------------------------------------------

def test_ch10_uses_h2_split_producing_multiple_chunks(ch10_chunks):
    """ch10 (30KB, 20-50KB tier) uses ## split and produces more than 1 chunk."""
    # ch10 is in the 20-50KB tier → ## split
    assert len(ch10_chunks) > 1, (
        f"ch10 expected >1 chunks from ## split, got {len(ch10_chunks)}"
    )


def test_ch10_file_type_chapter(ch10_chunks):
    """All ch10 chunks have file_type == 'chapter'."""
    for chunk in ch10_chunks:
        assert chunk.file_type == "chapter"


def test_ch10_domain_is_none(ch10_chunks):
    """All ch10 chunks have domain == None."""
    for chunk in ch10_chunks:
        assert chunk.domain is None


# ---------------------------------------------------------------------------
# All chapter chunk size tokens > 0
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fname", [
    "ch01_introduction.md",
    "ch04_general_assumptions.md",
    "ch08_relationships.md",
    "ch10_appendices.md",
])
def test_chapter_chunk_size_tokens_positive(chunker, fname):
    """All chunks from each chapter file have chunk_size_tokens > 0."""
    chunks = chunker.chunk(CHAPTERS_DIR / fname)
    for chunk in chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0
