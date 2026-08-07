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
def ch02_chunks(chunker):
    return chunker.chunk(CHAPTERS_DIR / "ch02_fundamentals.md")


@pytest.fixture(scope="module")
def ch03_chunks(chunker):
    return chunker.chunk(CHAPTERS_DIR / "ch03_submitting_data.md")


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
# ch01/ch02/ch03 (11-20KB): H2 split
#
# 2026-08-07 策略变更: 原第三档 "≤20KB → 整文件单块" 取消。原来锁死该档的两条测试
# (test_ch01_produces_1_chunk / test_ch01_section_is_whole_file) 被下面这组替换 ——
# 测试是策略的编码, 策略变了测试就该跟着变, 但必须留下等强度的新锁。
# ---------------------------------------------------------------------------

def test_ch01_splits_by_h2(ch01_chunks):
    """2026-08-07: "≤20KB → 整文件单块" 这一档取消, ch01 (11KB, 5 个 H2) 按 H2 切。

    原策略把 ch01/ch02/ch03 各压成 1 个 chunk, 整章共用一个向量 -> 语义稀释。
    q38 诊断实测: ch02 的 whole_file 块在 dense 检索排 #71 (sim 0.5613), 而回答
    同一问题的 ch04 §4.2.2 是 #1 (sim 0.6970) —— 后者是被 H3 切出来的小节。
    证据 evidence/checkpoints/chapters_chunking.md。
    """
    assert len(ch01_chunks) == 5
    assert all(c.section != "whole_file" for c in ch01_chunks)


def test_ch01_sections_carry_real_headings(ch01_chunks):
    secs = [c.section for c in ch01_chunks]
    assert any("1.1" in (s or "") for s in secs), secs
    assert any("1.5" in (s or "") for s in secs), secs


def test_ch02_splits_by_h2(ch02_chunks):
    """ch02 (18KB, 9 个 H2) —— q38 的 gold 章节, 原为整文件单块。"""
    assert len(ch02_chunks) == 9
    assert all(c.section != "whole_file" for c in ch02_chunks)
    # §2.6 Creating a New Domain 含 "Determine the domain code" —— q38 要的那一半
    assert any("2.6" in (c.section or "") for c in ch02_chunks), \
        [c.section for c in ch02_chunks]


def test_ch03_splits_by_h2(ch03_chunks):
    """ch03 (19KB, 3 个 H2) —— 原落在被取消的整块档 (19708 B 差 700 B 就进 H2 档)。"""
    assert len(ch03_chunks) == 3
    assert all(c.section != "whole_file" for c in ch03_chunks)


def test_file_without_headings_still_falls_back_to_whole_file(chunker, tmp_path):
    """无 H2 时仍回落整文件单块 —— 该回落分支是原整块档取消后的唯一兜底。"""
    f = tmp_path / "ch99_noheading.md"
    f.write_text("plain text with no markdown headings at all\n" * 20, encoding="utf-8")
    chunks = chunker.chunk(f)
    assert len(chunks) == 1
    assert chunks[0].section == "whole_file"


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


def test_large_chapter_still_splits_by_h3(ch04_chunks):
    """L-4 锁不得被本次改动破坏: >50KB 仍按 ### 切。"""
    assert len(ch04_chunks) == 47
    assert any("4.2.2" in (c.section or "") for c in ch04_chunks)


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
    "ch02_fundamentals.md",
    "ch03_submitting_data.md",
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
