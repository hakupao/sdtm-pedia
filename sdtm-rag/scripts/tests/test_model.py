"""Tests for ModelChunker.

Phase 1A.4 test-engineer.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.chunkers.model import ModelChunker

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"
MODEL_DIR = KB_ROOT / "model"

MODEL_FILES = [
    "01_concepts_and_terms.md",
    "02_observation_classes.md",
    "03_special_purpose_domains.md",
    "04_associated_persons.md",
    "05_study_level_data.md",
    "06_relationship_datasets.md",
]


@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT


@pytest.fixture(scope="module")
def chunker(kb_root):
    return ModelChunker(kb_root)


# ---------------------------------------------------------------------------
# All 6 model files: produce > 0 chunks, file_type == "model", domain == None
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fname", MODEL_FILES)
def test_model_file_produces_nonzero_chunks(chunker, fname):
    """Each model file produces at least 1 chunk."""
    chunks = chunker.chunk(MODEL_DIR / fname)
    assert len(chunks) > 0, f"{fname} produced 0 chunks"


@pytest.mark.parametrize("fname", MODEL_FILES)
def test_model_file_type_is_model(chunker, fname):
    """All chunks from model files have file_type == 'model'."""
    chunks = chunker.chunk(MODEL_DIR / fname)
    for chunk in chunks:
        assert chunk.file_type == "model", f"{fname}: unexpected file_type {chunk.file_type!r}"


@pytest.mark.parametrize("fname", MODEL_FILES)
def test_model_domain_is_none(chunker, fname):
    """All model chunks have domain == None (model files are not domain-specific)."""
    chunks = chunker.chunk(MODEL_DIR / fname)
    for chunk in chunks:
        assert chunk.domain is None, f"{fname}: expected domain=None, got {chunk.domain!r}"


@pytest.mark.parametrize("fname", MODEL_FILES)
def test_model_chunk_size_tokens_positive(chunker, fname):
    """All model chunks have chunk_size_tokens > 0 (tiktoken L-3)."""
    chunks = chunker.chunk(MODEL_DIR / fname)
    for chunk in chunks:
        assert chunk.chunk_size_tokens is not None
        assert chunk.chunk_size_tokens > 0


@pytest.mark.parametrize("fname", MODEL_FILES)
def test_model_chunk_indices_sequential(chunker, fname):
    """Model chunk indices are 0, 1, 2, ... for each file."""
    chunks = chunker.chunk(MODEL_DIR / fname)
    for i, chunk in enumerate(chunks):
        assert chunk.chunk_index == i


# ---------------------------------------------------------------------------
# No-H2 fallback: returns exactly 1 chunk with section == None
# ---------------------------------------------------------------------------

def test_model_no_h2_fallback_returns_1_chunk(kb_root, tmp_path):
    """A model file with no H2 headings returns exactly 1 chunk (fallback path)."""
    fake_model = tmp_path / "model_noheadings.md"
    fake_model.write_text(
        "# Title Only\n\nThis file has no H2 headings.\n\nJust prose content.\n",
        encoding="utf-8",
    )
    chunker = ModelChunker(kb_root)
    chunks = chunker.chunk(fake_model)
    assert len(chunks) == 1


def test_model_no_h2_fallback_section_is_none(kb_root, tmp_path):
    """No-H2 fallback chunk has section == None."""
    fake_model = tmp_path / "model_noheadings2.md"
    fake_model.write_text(
        "Some content without H2 headings.\n",
        encoding="utf-8",
    )
    chunker = ModelChunker(kb_root)
    chunks = chunker.chunk(fake_model)
    assert chunks[0].section is None


# ---------------------------------------------------------------------------
# to_metadata: all 18 keys present on model chunk
# ---------------------------------------------------------------------------

_EXPECTED_META_KEYS = {
    "source", "chunk_index", "file_type", "domain", "class",
    "section", "cdisc_section_id", "example_index", "sub_label",
    "has_mermaid", "has_table", "ct_code", "ct_extensible",
    "part_index", "table_chunk_idx", "chunk_size_tokens",
    "kb_commit_sha", "ingest_at",
}


def test_model_to_metadata_has_all_18_keys(chunker):
    """to_metadata() on a model chunk has all 18 expected keys."""
    chunks = chunker.chunk(MODEL_DIR / MODEL_FILES[0])
    meta = chunks[0].to_metadata()
    assert set(meta.keys()) == _EXPECTED_META_KEYS
