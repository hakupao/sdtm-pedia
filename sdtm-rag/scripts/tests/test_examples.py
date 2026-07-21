"""Tests for ExamplesChunker. CRITICAL: L-1 mermaid + L-2 table protection.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers.examples import ExamplesChunker
from scripts.chunkers.base import find_mermaid_blocks, find_table_blocks

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"
DOMAINS_DIR = KB_ROOT / "domains"


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def chunker(kb_root):
    return ExamplesChunker(kb_root)


@pytest.fixture(scope="module")
def ta_chunks(chunker):
    return chunker.chunk(DOMAINS_DIR / "TA" / "examples.md")


@pytest.fixture(scope="module")
def pc_chunks(chunker):
    return chunker.chunk(DOMAINS_DIR / "PC" / "examples.md")


@pytest.fixture(scope="module")
def is_chunks(chunker):
    return chunker.chunk(DOMAINS_DIR / "IS" / "examples.md")


@pytest.fixture(scope="module")
def ds_chunks(chunker):
    return chunker.chunk(DOMAINS_DIR / "DS" / "examples.md")


# ---------------------------------------------------------------------------
# TA/examples.md: exactly 8 chunks
# ---------------------------------------------------------------------------

def test_ta_examples_produces_8_chunks(ta_chunks):
    """TA/examples.md produces exactly 8 chunks (H2 flat mode)."""
    assert len(ta_chunks) == 8


def test_ta_examples_all_domain_ta(ta_chunks):
    """All TA examples chunks have domain == 'TA'."""
    for chunk in ta_chunks:
        assert chunk.domain == "TA"


def test_ta_examples_file_type_examples(ta_chunks):
    """All TA examples chunks have file_type == 'examples'."""
    for chunk in ta_chunks:
        assert chunk.file_type == "examples"


# ---------------------------------------------------------------------------
# PC/examples.md: exactly 14 chunks (H4 nested; Example 4 = Method A+D only)
# ---------------------------------------------------------------------------

def test_pc_examples_produces_14_chunks(pc_chunks):
    """PC/examples.md produces exactly 14 chunks (4+4+4+2; Example 4 = Method A+D only)."""
    assert len(pc_chunks) == 14


def test_pc_examples_all_have_sub_label_method(pc_chunks):
    """All PC chunks have sub_label matching 'Method [A-D]' pattern."""
    for chunk in pc_chunks:
        assert chunk.sub_label is not None
        assert chunk.sub_label.startswith("Method ")


def test_pc_examples_sub_labels_are_valid_methods(pc_chunks):
    """PC chunk sub_labels are only 'Method A', 'Method B', 'Method C', or 'Method D'."""
    valid = {"Method A", "Method B", "Method C", "Method D"}
    for chunk in pc_chunks:
        assert chunk.sub_label in valid, f"Unexpected sub_label: {chunk.sub_label!r}"


def test_pc_examples_all_have_example_index(pc_chunks):
    """All PC chunks have a non-None example_index."""
    for chunk in pc_chunks:
        assert chunk.example_index is not None


def test_pc_examples_example_indices_range_1_to_4(pc_chunks):
    """PC example_index values are all within 1..4."""
    for chunk in pc_chunks:
        assert 1 <= chunk.example_index <= 4, (
            f"example_index {chunk.example_index} out of range [1,4]"
        )


def test_pc_examples_all_have_cdisc_section_id(pc_chunks):
    """All PC chunks have cdisc_section_id == '§6.3.5.9.3'."""
    for chunk in pc_chunks:
        assert chunk.cdisc_section_id == "§6.3.5.9.3", (
            f"Expected §6.3.5.9.3, got {chunk.cdisc_section_id!r}"
        )


def test_pc_examples_example_4_has_only_method_a_and_d(pc_chunks):
    """PC Example 4 has exactly Method A and Method D (not all 4 methods)."""
    ex4_chunks = [c for c in pc_chunks if c.example_index == 4]
    ex4_labels = {c.sub_label for c in ex4_chunks}
    assert ex4_labels == {"Method A", "Method D"}, (
        f"PC Example 4 sub_labels: {ex4_labels}"
    )


# ---------------------------------------------------------------------------
# IS/examples.md: 11 chunks, all has_table=True
# ---------------------------------------------------------------------------

def test_is_examples_produces_11_chunks(is_chunks):
    """IS/examples.md produces exactly 11 chunks."""
    assert len(is_chunks) == 11


def test_is_examples_all_has_table_true(is_chunks):
    """All IS examples chunks have has_table == True."""
    for chunk in is_chunks:
        assert chunk.has_table is True, f"chunk {chunk.chunk_index} has_table={chunk.has_table}"


# ---------------------------------------------------------------------------
# DS/examples.md: 11 chunks, no mermaid
# ---------------------------------------------------------------------------

def test_ds_examples_produces_11_chunks(ds_chunks):
    """DS/examples.md produces exactly 11 chunks."""
    assert len(ds_chunks) == 11


def test_ds_examples_no_mermaid(ds_chunks):
    """No DS examples chunk has has_mermaid == True."""
    for chunk in ds_chunks:
        assert chunk.has_mermaid is not True, (
            f"chunk {chunk.chunk_index} unexpectedly has mermaid"
        )


# ---------------------------------------------------------------------------
# L-1: mermaid block protection — no chunk boundary inside a mermaid block
# ---------------------------------------------------------------------------

def test_l1_mermaid_protection_ta_no_chunk_boundary_inside_mermaid_block():
    """L-1: For each TA mermaid block, both its start and end are within the same chunk.

    This verifies that no chunk split point lands inside a ```mermaid ... ``` block.
    """
    ta_file = DOMAINS_DIR / "TA" / "examples.md"
    text = ta_file.read_text(encoding="utf-8")
    chunker = ExamplesChunker(KB_ROOT)
    chunks = chunker.chunk(ta_file)
    mermaid_blocks = find_mermaid_blocks(text)

    # Build chunk byte ranges
    chunk_ranges = []
    for chunk in chunks:
        # Reconstruct byte range from source text by matching chunk text
        # More reliable: use the chunk_index ordering with heading positions
        pass

    # Alternative approach: verify via text slicing
    # Get chunk boundaries from the actual text splits
    # We know chunks are ordered and non-overlapping
    # Re-derive boundaries by finding each chunk's text position
    chunk_starts = []
    pos = 0
    for chunk in chunks:
        idx = text.find(chunk.text, pos)
        assert idx != -1, f"Could not find chunk text in source (chunk_index={chunk.chunk_index})"
        chunk_starts.append(idx)
        pos = idx  # allow overlap detection

    chunk_boundaries = []
    for i, start in enumerate(chunk_starts):
        end = chunk_starts[i + 1] if i + 1 < len(chunk_starts) else len(text)
        chunk_boundaries.append((start, end))

    violations = []
    for mb_start, mb_end in mermaid_blocks:
        # Find which chunk(s) contain this mermaid block's start and end
        start_chunk = None
        end_chunk = None
        for ci, (cs, ce) in enumerate(chunk_boundaries):
            if cs <= mb_start < ce:
                start_chunk = ci
            if cs < mb_end <= ce:
                end_chunk = ci
        if start_chunk != end_chunk:
            violations.append((mb_start, mb_end, start_chunk, end_chunk))

    assert violations == [], (
        f"L-1 VIOLATION: mermaid blocks cross chunk boundaries: {violations}"
    )


# ---------------------------------------------------------------------------
# L-2: table block protection — no chunk boundary inside a table block
# ---------------------------------------------------------------------------

def test_l2_table_protection_pc_no_chunk_boundary_inside_table_block():
    """L-2: For each PC table block, both its start and end are within the same chunk."""
    pc_file = DOMAINS_DIR / "PC" / "examples.md"
    text = pc_file.read_text(encoding="utf-8")
    chunker = ExamplesChunker(KB_ROOT)
    chunks = chunker.chunk(pc_file)
    table_blocks = find_table_blocks(text)

    chunk_starts = []
    pos = 0
    for chunk in chunks:
        idx = text.find(chunk.text, pos)
        assert idx != -1
        chunk_starts.append(idx)
        pos = idx

    chunk_boundaries = []
    for i, start in enumerate(chunk_starts):
        end = chunk_starts[i + 1] if i + 1 < len(chunk_starts) else len(text)
        chunk_boundaries.append((start, end))

    violations = []
    for tb_start, tb_end in table_blocks:
        start_chunk = None
        end_chunk = None
        for ci, (cs, ce) in enumerate(chunk_boundaries):
            if cs <= tb_start < ce:
                start_chunk = ci
            if cs < tb_end <= ce:
                end_chunk = ci
        if start_chunk != end_chunk:
            violations.append((tb_start, tb_end, start_chunk, end_chunk))

    assert violations == [], (
        f"L-2 VIOLATION: table blocks cross chunk boundaries: {violations}"
    )


# ---------------------------------------------------------------------------
# L-1 defensive: heading inside a fenced block is filtered out
# ---------------------------------------------------------------------------

def test_l1_heading_inside_mermaid_fence_is_not_chunked(kb_root, tmp_path):
    """Heading text inside a mermaid fence is not treated as a split point."""
    # Craft a synthetic examples.md with a heading inside a mermaid block
    content = (
        "## Example 1\n\nProse.\n\n"
        "```mermaid\ngraph TD\n  ## Fake heading inside fence\n  A-->B\n```\n\n"
        "## Example 2\n\nMore prose.\n"
    )
    fake_file = tmp_path / "TA" / "examples.md"
    fake_file.parent.mkdir(parents=True)
    fake_file.write_text(content, encoding="utf-8")
    chunker = ExamplesChunker(kb_root)
    chunks = chunker.chunk(fake_file)
    # Should be 2 chunks (Example 1 + Example 2), not 3
    assert len(chunks) == 2, (
        f"Expected 2 chunks; got {len(chunks)}. Heading inside mermaid was not filtered."
    )


# ---------------------------------------------------------------------------
# Edge: missing examples.md returns [] without crash
# ---------------------------------------------------------------------------

def test_empty_or_no_h2_examples_returns_empty_list(kb_root, tmp_path):
    """An examples.md with no H2 or H4 headings returns [] without raising."""
    fake_file = tmp_path / "TS" / "examples.md"
    fake_file.parent.mkdir(parents=True)
    fake_file.write_text("No headings here, just prose.\n", encoding="utf-8")
    chunker = ExamplesChunker(kb_root)
    chunks = chunker.chunk(fake_file)
    assert chunks == []


def test_relrec_examples_no_crash(chunker):
    """RELREC/examples.md (if exists and is small) does not raise; may return []."""
    relrec_file = DOMAINS_DIR / "RELREC" / "examples.md"
    if not relrec_file.exists():
        pytest.skip("RELREC/examples.md does not exist")
    chunks = chunker.chunk(relrec_file)
    assert isinstance(chunks, list)
