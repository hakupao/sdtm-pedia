"""Tests for base.py helpers: Chunk schema, count_tokens, find_mermaid_blocks,
find_table_blocks, heading_positions, kb_commit_sha.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import tiktoken

from scripts.chunkers.base import (
    Chunk,
    count_tokens,
    find_mermaid_blocks,
    find_table_blocks,
    heading_positions,
    kb_commit_sha,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"
TA_EXAMPLES = KB_ROOT / "domains" / "TA" / "examples.md"
PC_EXAMPLES = KB_ROOT / "domains" / "PC" / "examples.md"


@pytest.fixture(scope="module")
def ta_text() -> str:
    return TA_EXAMPLES.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def pc_text() -> str:
    return PC_EXAMPLES.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Chunk dataclass: 18 fields + to_metadata()
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = [
    "source", "text", "chunk_index", "file_type",
    "domain", "cdisc_class", "section", "cdisc_section_id",
    "example_index", "sub_label", "has_mermaid", "has_table",
    "ct_code", "ct_extensible", "part_index", "table_chunk_idx",
    "chunk_size_tokens", "kb_commit_sha", "ingest_at",
]


def _minimal_chunk(**overrides) -> Chunk:
    defaults = dict(
        source="test.md",
        text="hello world",
        chunk_index=0,
        file_type="spec",
        domain=None,
        cdisc_class=None,
        section=None,
        cdisc_section_id=None,
        example_index=None,
        sub_label=None,
        has_mermaid=None,
        has_table=None,
        ct_code=None,
        ct_extensible=None,
        part_index=None,
        table_chunk_idx=None,
        chunk_size_tokens=2,
        kb_commit_sha=None,
        ingest_at="2026-05-22",
    )
    defaults.update(overrides)
    return Chunk(**defaults)


def test_chunk_has_exactly_19_fields():
    """Chunk dataclass exposes exactly 19 field names (18 metadata + text)."""
    chunk = _minimal_chunk()
    d = chunk.__dataclass_fields__
    assert len(d) == 19, f"Expected 19 fields, got {len(d)}: {list(d)}"


def test_chunk_all_required_fields_present():
    """All 19 expected field names exist on the Chunk dataclass."""
    chunk = _minimal_chunk()
    for field in REQUIRED_FIELDS:
        assert hasattr(chunk, field), f"Missing field: {field}"


def test_to_metadata_drops_text():
    """to_metadata() must not include 'text' key."""
    chunk = _minimal_chunk(text="some content here")
    meta = chunk.to_metadata()
    assert "text" not in meta


def test_to_metadata_renames_cdisc_class_to_class():
    """to_metadata() renames cdisc_class -> 'class'."""
    chunk = _minimal_chunk(cdisc_class="Events")
    meta = chunk.to_metadata()
    assert "class" in meta
    assert "cdisc_class" not in meta
    assert meta["class"] == "Events"


def test_to_metadata_has_18_keys():
    """to_metadata() returns exactly 18 keys (text dropped, cdisc_class renamed to class)."""
    chunk = _minimal_chunk()
    meta = chunk.to_metadata()
    assert len(meta) == 18, f"Expected 18, got {len(meta)}: {list(meta)}"


def test_to_metadata_none_values_preserved():
    """to_metadata() keeps None values; None != absent key (Chroma behavior contract)."""
    chunk = _minimal_chunk(domain=None, ct_code=None)
    meta = chunk.to_metadata()
    assert "domain" in meta
    assert meta["domain"] is None


# ---------------------------------------------------------------------------
# count_tokens: L-3 tiktoken cl100k_base (not char/4)
# ---------------------------------------------------------------------------

def test_count_tokens_matches_tiktoken_directly():
    """count_tokens result equals tiktoken cl100k_base encode length for known string."""
    enc = tiktoken.get_encoding("cl100k_base")
    test_string = "STUDYID is a required identifier variable in SDTM datasets."
    expected = len(enc.encode(test_string))
    assert count_tokens(test_string) == expected


def test_count_tokens_not_char_divided_by_4():
    """count_tokens deviates from char/4 for dense GFM table text (L-3 lock evidence)."""
    # Dense GFM pipe-table row — char/4 is known to undercount by ~23.6% (1A.0.c C2)
    dense_table = "| " + " | ".join([f"val{i:03d}" for i in range(20)]) + " |\n" * 50
    char4_estimate = len(dense_table) // 4
    actual = count_tokens(dense_table)
    # They should differ by more than 5%
    ratio = abs(actual - char4_estimate) / max(char4_estimate, 1)
    assert ratio > 0.05, (
        f"count_tokens ({actual}) too close to char/4 ({char4_estimate}); "
        "L-3 lock requires tiktoken, not char/4"
    )


def test_count_tokens_returns_positive_for_nonempty_string():
    """count_tokens returns a positive integer for any non-empty string."""
    assert count_tokens("hello") > 0


def test_count_tokens_returns_zero_for_empty_string():
    """count_tokens returns 0 for empty string."""
    assert count_tokens("") == 0


# ---------------------------------------------------------------------------
# find_mermaid_blocks: L-1 state machine
# ---------------------------------------------------------------------------

def test_find_mermaid_blocks_ta_returns_20(ta_text):
    """TA/examples.md has exactly 20 mermaid blocks (matches 1A.0.b finding)."""
    blocks = find_mermaid_blocks(ta_text)
    assert len(blocks) == 20


def test_find_mermaid_blocks_returns_tuples_with_valid_offsets(ta_text):
    """Each mermaid block is a (start, end) tuple with start < end."""
    blocks = find_mermaid_blocks(ta_text)
    for start, end in blocks:
        assert isinstance(start, int)
        assert isinstance(end, int)
        assert start < end


def test_find_mermaid_blocks_none_in_non_mermaid_text():
    """Text with no mermaid blocks returns empty list."""
    text = "# Title\n\nSome prose without code fences.\n\n| a | b |\n|---|---|\n| 1 | 2 |\n"
    assert find_mermaid_blocks(text) == []


def test_find_mermaid_blocks_single_block():
    """Single mermaid block is correctly detected."""
    text = "Before\n```mermaid\ngraph TD\n  A-->B\n```\nAfter\n"
    blocks = find_mermaid_blocks(text)
    assert len(blocks) == 1
    start, end = blocks[0]
    assert text[start:end].startswith("```mermaid")
    assert text[start:end].rstrip().endswith("```")


def test_find_mermaid_blocks_no_false_positive_for_code_fence():
    """Plain ``` code fence without 'mermaid' is not detected as mermaid block."""
    text = "```python\nx = 1\n```\n"
    assert find_mermaid_blocks(text) == []


def test_find_mermaid_blocks_content_between_fences_is_captured():
    """Block start/end offsets capture content between opening and closing fence."""
    inner = "graph TD\n  A-->B\n  B-->C\n"
    text = f"```mermaid\n{inner}```\n"
    blocks = find_mermaid_blocks(text)
    assert len(blocks) == 1
    block_text = text[blocks[0][0]:blocks[0][1]]
    assert "graph TD" in block_text


# ---------------------------------------------------------------------------
# find_table_blocks: L-2 GFM pipe-table
# ---------------------------------------------------------------------------

def test_find_table_blocks_pc_examples_returns_nonzero(pc_text):
    """PC/examples.md contains at least one GFM pipe-table block."""
    blocks = find_table_blocks(pc_text)
    assert len(blocks) > 0


def test_find_table_blocks_simple_table():
    """Simple 2-column GFM table is detected as one block."""
    text = "| Header A | Header B |\n|-----------|----------|\n| val1 | val2 |\n| val3 | val4 |\n"
    blocks = find_table_blocks(text)
    assert len(blocks) == 1


def test_find_table_blocks_no_false_positive_for_prose():
    """Plain prose with no pipe-tables returns empty list."""
    text = "# Title\n\nThis is a paragraph without tables.\n\nAnother paragraph.\n"
    assert find_table_blocks(text) == []


def test_find_table_blocks_requires_separator_row():
    """Two consecutive pipe rows without a separator row are not detected as a table."""
    text = "| a | b |\n| c | d |\n"  # no |---|---| separator
    blocks = find_table_blocks(text)
    assert len(blocks) == 0


def test_find_table_blocks_two_separate_tables():
    """Two separate tables in the same text are detected as two separate blocks."""
    table = "| A | B |\n|---|---|\n| 1 | 2 |\n"
    text = table + "\nSome prose.\n\n" + table
    blocks = find_table_blocks(text)
    assert len(blocks) == 2


# ---------------------------------------------------------------------------
# heading_positions
# ---------------------------------------------------------------------------

def test_heading_positions_ta_examples_h2_count_equals_8(ta_text):
    """TA/examples.md has exactly 8 H2 headings."""
    h2s = heading_positions(ta_text, 2)
    assert len(h2s) == 8


def test_heading_positions_returns_sorted_offsets(ta_text):
    """heading_positions returns headings in ascending byte-offset order."""
    h2s = heading_positions(ta_text, 2)
    offsets = [pos for pos, _ in h2s]
    assert offsets == sorted(offsets)


def test_heading_positions_extracts_heading_text():
    """heading_positions extracts the heading text without # prefix."""
    text = "## My Section Title\n\nSome content.\n"
    h2s = heading_positions(text, 2)
    assert len(h2s) == 1
    assert h2s[0][1] == "My Section Title"


def test_heading_positions_level_3_in_spec():
    """heading_positions at level 3 finds H3 headings correctly."""
    text = "### STUDYID\n\nContent.\n\n### DOMAIN\n\nContent.\n"
    h3s = heading_positions(text, 3)
    assert len(h3s) == 2
    assert h3s[0][1] == "STUDYID"
    assert h3s[1][1] == "DOMAIN"


# ---------------------------------------------------------------------------
# kb_commit_sha
# ---------------------------------------------------------------------------

def test_kb_commit_sha_returns_40_char_sha_or_unknown():
    """kb_commit_sha returns a 40-char hex SHA or 'unknown' — never crashes."""
    sha = kb_commit_sha(KB_ROOT)
    assert sha == "unknown" or (len(sha) == 40 and re.fullmatch(r"[0-9a-f]{40}", sha)), (
        f"Unexpected sha value: {sha!r}"
    )


def test_kb_commit_sha_nonexistent_path_returns_unknown():
    """kb_commit_sha on a non-existent path returns 'unknown' gracefully."""
    sha = kb_commit_sha(Path("/tmp/nonexistent_kb_path_abc123"))
    assert sha == "unknown"
