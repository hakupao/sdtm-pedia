"""Tests for TerminologyChunker. CRITICAL: L-5 part vs codelist mode.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from scripts.chunkers.terminology import TerminologyChunker

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"
CORE_DIR = KB_ROOT / "terminology" / "core"
QUEST_DIR = KB_ROOT / "terminology" / "questionnaires"
SUPP_DIR = KB_ROOT / "terminology" / "supplementary"


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def chunker(kb_root):
    return TerminologyChunker(kb_root)


@pytest.fixture(scope="module")
def ae_chunks(chunker):
    return chunker.chunk(CORE_DIR / "ae.md")


@pytest.fixture(scope="module")
def lb_part1_chunks(chunker):
    return chunker.chunk(CORE_DIR / "lb_part1.md")


@pytest.fixture(scope="module")
def lb_part4_chunks(chunker):
    return chunker.chunk(CORE_DIR / "lb_part4.md")


@pytest.fixture(scope="module")
def questionnaires_part1_chunks(chunker):
    return chunker.chunk(QUEST_DIR / "questionnaires_part1.md")


@pytest.fixture(scope="module")
def supplementary_part1_chunks(chunker):
    return chunker.chunk(SUPP_DIR / "supplementary_part1.md")


# ---------------------------------------------------------------------------
# ae.md (4 H2): 4 chunks, codelist mode, each has ct_code (C\d+ format)
# ---------------------------------------------------------------------------

def test_ae_terminology_produces_4_chunks(ae_chunks):
    """ae.md (4 H2) produces exactly 4 chunks in codelist mode."""
    assert len(ae_chunks) == 4


def test_ae_terminology_all_file_type_terminology(ae_chunks):
    """All ae.md chunks have file_type == 'terminology'."""
    for chunk in ae_chunks:
        assert chunk.file_type == "terminology"


def test_ae_terminology_all_domain_none(ae_chunks):
    """All ae.md chunks have domain == None (codelists are not domain-specific)."""
    for chunk in ae_chunks:
        assert chunk.domain is None


def test_ae_terminology_all_have_ct_code(ae_chunks):
    """All ae.md chunks have a non-None ct_code."""
    for chunk in ae_chunks:
        assert chunk.ct_code is not None, f"chunk {chunk.chunk_index} missing ct_code"


def test_ae_terminology_ct_code_format_c_digits(ae_chunks):
    """All ae.md ct_code values match the C\\d+ format (e.g., C66767)."""
    pattern = re.compile(r"^C\d+$")
    for chunk in ae_chunks:
        assert pattern.match(chunk.ct_code), (
            f"ct_code {chunk.ct_code!r} does not match C\\d+ format"
        )


def test_ae_terminology_ct_extensible_is_none(ae_chunks):
    """All ae.md chunks have ct_extensible == None (deferred, no reliable signal)."""
    for chunk in ae_chunks:
        assert chunk.ct_extensible is None


# ---------------------------------------------------------------------------
# lb_part1.md (1 H2 + _part1 name): 1 chunk, part mode, part_index == 1
# ---------------------------------------------------------------------------

def test_lb_part1_produces_1_chunk(lb_part1_chunks):
    """lb_part1.md (H2=1 + _part1) produces exactly 1 chunk in part mode."""
    assert len(lb_part1_chunks) == 1


def test_lb_part1_part_index_is_1(lb_part1_chunks):
    """lb_part1.md chunk has part_index == 1."""
    assert lb_part1_chunks[0].part_index == 1


def test_lb_part1_section_is_lb_part1(lb_part1_chunks):
    """lb_part1.md chunk has section == 'lb_part1' (filename stem)."""
    assert lb_part1_chunks[0].section == "lb_part1"


def test_lb_part1_ct_code_is_none(lb_part1_chunks):
    """lb_part1.md part mode chunk has ct_code == None (no H2 codelist parse)."""
    assert lb_part1_chunks[0].ct_code is None


# ---------------------------------------------------------------------------
# lb_part2.md: part mode, 1 chunk — document if chunk_size_tokens > 8191 (known finding)
# ---------------------------------------------------------------------------

def test_lb_part2_produces_1_chunk(chunker):
    """lb_part2.md (H2=1 + _part2, 378KB) produces exactly 1 chunk in part mode."""
    chunks = chunker.chunk(CORE_DIR / "lb_part2.md")
    assert len(chunks) == 1


def test_lb_part2_part_index_is_2(chunker):
    """lb_part2.md chunk has part_index == 2."""
    chunks = chunker.chunk(CORE_DIR / "lb_part2.md")
    assert chunks[0].part_index == 2


@pytest.mark.xfail(
    reason=(
        "Known finding (1A.3 Batch C / 1A.4): lb_part2 (378KB) is a single part-mode chunk. "
        "chunk_size_tokens likely >> 8191 embedding limit. "
        "Fix deferred to 1A.5: N=100 row table-chunk slicing + table_chunk_idx metadata."
    ),
    strict=False,
)
def test_lb_part2_chunk_size_tokens_under_8192(chunker):
    """lb_part2.md single chunk should be under 8192 tokens (expected to FAIL — known finding)."""
    chunks = chunker.chunk(CORE_DIR / "lb_part2.md")
    assert chunks[0].chunk_size_tokens <= 8191


# ---------------------------------------------------------------------------
# lb_part3.md: part mode, 1 chunk, similar to lb_part2
# ---------------------------------------------------------------------------

def test_lb_part3_produces_1_chunk(chunker):
    """lb_part3.md (H2=1 + _part3, 417KB) produces exactly 1 chunk in part mode."""
    chunks = chunker.chunk(CORE_DIR / "lb_part3.md")
    assert len(chunks) == 1


def test_lb_part3_part_index_is_3(chunker):
    """lb_part3.md chunk has part_index == 3."""
    chunks = chunker.chunk(CORE_DIR / "lb_part3.md")
    assert chunks[0].part_index == 3


@pytest.mark.xfail(
    reason=(
        "Known finding: lb_part3 (417KB) single chunk likely >> 8191 token limit. "
        "Fix deferred to 1A.5."
    ),
    strict=False,
)
def test_lb_part3_chunk_size_tokens_under_8192(chunker):
    """lb_part3.md single chunk should be under 8192 tokens (expected to FAIL — known finding)."""
    chunks = chunker.chunk(CORE_DIR / "lb_part3.md")
    assert chunks[0].chunk_size_tokens <= 8191


# ---------------------------------------------------------------------------
# lb_part4.md (2 H2 + _part4 name): L-5 CRITICAL EDGE
# H2 > 1 → codelist mode (NOT part mode), produces 2 chunks
# ---------------------------------------------------------------------------

def test_lb_part4_produces_2_chunks(lb_part4_chunks):
    """lb_part4.md (H2=2, _part4) produces exactly 2 chunks in CODELIST mode (L-5 edge)."""
    assert len(lb_part4_chunks) == 2


def test_lb_part4_is_codelist_mode_not_part_mode(lb_part4_chunks):
    """lb_part4.md uses codelist mode: each chunk has a ct_code (not None)."""
    # In codelist mode, chunks are parsed per H2 codelist heading with C\d+ code
    for chunk in lb_part4_chunks:
        assert chunk.ct_code is not None, (
            f"lb_part4 chunk {chunk.chunk_index} has no ct_code — likely wrong mode (part vs codelist)"
        )


def test_lb_part4_part_index_still_set_to_4(lb_part4_chunks):
    """lb_part4.md codelist mode chunks still have part_index == 4 (cross-part reassembly metadata)."""
    for chunk in lb_part4_chunks:
        assert chunk.part_index == 4


def test_lb_part4_ct_code_format(lb_part4_chunks):
    """lb_part4.md ct_codes match C\\d+ format."""
    pattern = re.compile(r"^C\d+$")
    for chunk in lb_part4_chunks:
        assert pattern.match(chunk.ct_code), (
            f"lb_part4 ct_code {chunk.ct_code!r} doesn't match C\\d+"
        )


# ---------------------------------------------------------------------------
# questionnaires_part1.md: 66 chunks, codelist mode
# ---------------------------------------------------------------------------

def test_questionnaires_part1_produces_66_chunks(questionnaires_part1_chunks):
    """questionnaires_part1.md produces exactly 66 chunks in codelist mode."""
    assert len(questionnaires_part1_chunks) == 66


def test_questionnaires_part1_all_file_type_terminology(questionnaires_part1_chunks):
    """All questionnaires_part1 chunks have file_type == 'terminology'."""
    for chunk in questionnaires_part1_chunks:
        assert chunk.file_type == "terminology"


# ---------------------------------------------------------------------------
# supplementary_part1.md: 27 chunks, codelist mode
# ---------------------------------------------------------------------------

def test_supplementary_part1_produces_27_chunks(supplementary_part1_chunks):
    """supplementary_part1.md produces exactly 27 chunks in codelist mode."""
    assert len(supplementary_part1_chunks) == 27


def test_supplementary_part1_all_terminology(supplementary_part1_chunks):
    """All supplementary_part1 chunks have file_type == 'terminology'."""
    for chunk in supplementary_part1_chunks:
        assert chunk.file_type == "terminology"


# ---------------------------------------------------------------------------
# chunk_size_tokens positive for all
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fname,subdir", [
    ("ae.md", "core"),
    ("lb_part1.md", "core"),
    ("lb_part4.md", "core"),
])
def test_terminology_chunk_size_tokens_positive(chunker, fname, subdir):
    """Terminology chunks have chunk_size_tokens > 0 (tiktoken L-3)."""
    path = KB_ROOT / "terminology" / subdir / fname
    chunks = chunker.chunk(path)
    for chunk in chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0
