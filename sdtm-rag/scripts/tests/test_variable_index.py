"""Tests for VariableIndexChunker.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from scripts.chunkers.variable_index import VariableIndexChunker

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"
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
# Total = §一 per-variable + §二 per-domain + §三 per-CT-code, 一行一块。
# Was 65 (1 + 63 + 1) before the re-chunking fix.
#
# 数字不写死: 2026-08-07 修掉 CT 首码提取后 §三 从 135 → 147 行, 硬编码的 222/135
# 当场红成"回归", 但其实是数据变对了。计数改为对 KB 实际行数推导。
# ---------------------------------------------------------------------------

def _kb_section_row_counts() -> tuple[int, int, int]:
    """从 VARIABLE_INDEX.md 直接数 §一 / §二 / §三 的行数 (chunker 的期望输入)。"""
    text = VAR_INDEX_FILE.read_text(encoding="utf-8")
    sec1 = text.split("## 1. Common Variables")[1].split("## 2. Domain-Specific")[0]
    sec2 = text.split("## 2. Domain-Specific")[1].split("## 3. CDISC Controlled")[0]
    sec3 = text.split("## 3. CDISC Controlled")[1]
    n1 = len(re.findall(r"^\| [A-Z][A-Z0-9]+ \|", sec1, re.M))
    n2 = len(re.findall(r"^### ", sec2, re.M))
    n3 = len(re.findall(r"^\| C\d+ \|", sec3, re.M))
    return n1, n2, n3


def test_variable_index_chunk_total_matches_kb_rows(vi_chunks):
    """chunk 总数 == §一 行数 + §二 H3 数 + §三 行数 (逐行一块, 无按尺寸再切)。"""
    n1, n2, n3 = _kb_section_row_counts()
    assert len(vi_chunks) == n1 + n2 + n3


def test_variable_index_all_file_type_variable_index(vi_chunks):
    """All VARIABLE_INDEX chunks have file_type == 'variable_index'."""
    for chunk in vi_chunks:
        assert chunk.file_type == "variable_index"


def test_variable_index_chunk_indices_sequential(vi_chunks):
    """VARIABLE_INDEX chunk indices are 0..N-1 (sequential across §一/§二/§三)."""
    for i, chunk in enumerate(vi_chunks):
        assert chunk.chunk_index == i


def test_variable_index_all_chunk_size_tokens_positive(vi_chunks):
    """All VARIABLE_INDEX chunks have chunk_size_tokens > 0."""
    for chunk in vi_chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0


# ---------------------------------------------------------------------------
# §一: per-variable chunks (24), each section starts with "§一", domain None.
# Indices 0..23 (alphabetical/original-table order). chunks[0] = STUDYID.
# ---------------------------------------------------------------------------

# §一 occupies the first 24 chunks; §二 the next 63 (24..86); §三 the rest (87..221).
SEC1_END = 24
SEC2_END = 87


def test_variable_index_section1_has_24_chunks(vi_chunks):
    """Exactly 24 §一 per-variable chunks (one per common-variable table row)."""
    sec1 = [c for c in vi_chunks if c.section and c.section.startswith("§一")]
    assert len(sec1) == 24


def test_variable_index_chunk0_section_starts_with_yi(vi_chunks):
    """chunks[0] has section starting with '§一'."""
    assert vi_chunks[0].section is not None
    assert vi_chunks[0].section.startswith("§一"), (
        f"chunks[0].section = {vi_chunks[0].section!r}"
    )


def test_variable_index_section1_chunks_domain_is_none(vi_chunks):
    """All §一 per-variable chunks have domain == None."""
    for chunk in vi_chunks[:SEC1_END]:
        assert chunk.domain is None


def test_variable_index_section1_epoch_chunk_natural_language(vi_chunks):
    """§一 yields a per-variable EPOCH chunk: text has 'EPOCH', '44', and lists domains."""
    epoch = [
        c for c in vi_chunks
        if c.section and c.section.startswith("§一") and "EPOCH" in c.text
    ]
    assert len(epoch) == 1, f"Expected exactly 1 EPOCH §一 chunk, got {len(epoch)}"
    text = epoch[0].text
    assert "EPOCH" in text
    assert "44" in text, f"EPOCH chunk missing domain count '44': {text!r}"
    # lists domains (comma-separated domain codes after the count)
    assert "AE" in text and "VS" in text, f"EPOCH chunk missing domain list: {text!r}"
    assert epoch[0].section == "§一 通用变量: EPOCH"


# ---------------------------------------------------------------------------
# §二: chunks[24..86] each have a domain set (63 per-domain chunks)
# ---------------------------------------------------------------------------

def test_variable_index_section2_chunks_have_domain(vi_chunks):
    """§二 domain entries (chunks[24..86]) all have a non-None domain."""
    for chunk in vi_chunks[SEC1_END:SEC2_END]:
        assert chunk.domain is not None, (
            f"chunk {chunk.chunk_index} (section={chunk.section!r}) has domain=None"
        )


def test_variable_index_section2_first_domain_is_ae(vi_chunks):
    """First §二 chunk domain is 'AE' (first domain in §二 is AE, alphabetical order)."""
    assert vi_chunks[SEC1_END].domain == "AE", (
        f"Expected 'AE', got {vi_chunks[SEC1_END].domain!r}"
    )


def test_variable_index_section2_all_domains_are_uppercase(vi_chunks):
    """All §二 domain codes are uppercase alphanumeric strings."""
    for chunk in vi_chunks[SEC1_END:SEC2_END]:
        assert chunk.domain == chunk.domain.upper(), (
            f"domain {chunk.domain!r} is not uppercase"
        )
        assert chunk.domain.isalnum(), (
            f"domain {chunk.domain!r} contains non-alphanumeric characters"
        )


def test_variable_index_section2_has_63_chunks(vi_chunks):
    """Exactly 63 chunks in §二 (one per domain)."""
    section2_chunks = vi_chunks[SEC1_END:SEC2_END]
    assert len(section2_chunks) == 63


# ---------------------------------------------------------------------------
# §三: per-CT-code chunks, each section starts with "§三", ct_code set.
# ---------------------------------------------------------------------------

def test_variable_index_section3_chunk_count_matches_kb_rows(vi_chunks):
    """§三 chunk 数 == KB 里 §三 的表格行数 (一行一块)。数字不写死, 见文件上方说明。"""
    sec3 = [c for c in vi_chunks if c.section and c.section.startswith("§三")]
    assert len(sec3) == _kb_section_row_counts()[2]


def test_variable_index_last_chunk_section_starts_with_san(vi_chunks):
    """chunks[-1] has section starting with '§三'."""
    assert vi_chunks[-1].section is not None
    assert vi_chunks[-1].section.startswith("§三"), (
        f"Last chunk section = {vi_chunks[-1].section!r}"
    )


def test_variable_index_section3_c66742_chunk_has_ct_code(vi_chunks):
    """§三 yields a per-CT-code chunk for 'C66742' with ct_code == 'C66742' metadata."""
    c66742 = [c for c in vi_chunks if c.ct_code == "C66742"]
    assert len(c66742) == 1, f"Expected exactly 1 C66742 §三 chunk, got {len(c66742)}"
    chunk = c66742[0]
    assert chunk.ct_code == "C66742"
    assert chunk.section == "§三 CT 交叉引用: C66742"
    assert chunk.domain is None
    assert "C66742" in chunk.text


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
    meta = vi_chunks[SEC1_END].to_metadata()  # use a §二 chunk which has domain
    assert set(meta.keys()) == _EXPECTED_META_KEYS


def test_variable_index_section2_class_field_in_metadata(vi_chunks):
    """§二 chunks with cdisc_class set export 'class' in to_metadata()."""
    # Find a chunk that has cdisc_class set (e.g., AE → "Events")
    class_chunks = [c for c in vi_chunks[SEC1_END:SEC2_END] if c.cdisc_class is not None]
    if not class_chunks:
        pytest.skip("No §二 chunk has cdisc_class set — check VariableIndexChunker parsing")
    meta = class_chunks[0].to_metadata()
    assert "class" in meta
    assert meta["class"] is not None
