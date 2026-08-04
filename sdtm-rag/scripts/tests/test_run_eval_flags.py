"""Unit tests for eval/run_eval.py --collection / --kb-root wiring.

RAGEngine / run_evaluation / print_summary are stubbed, so no chroma dir is
opened and no API is called. The point is the construction kwargs: the default
path must stay byte-identical to pre-flag behaviour, and --collection must
force structured-lookup off (the S1 gold map is CDISC-specific).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from eval import run_eval
from server.config import settings


@pytest.fixture
def captured(tmp_path, monkeypatch):
    """Run main() with all heavy collaborators stubbed; return RAGEngine kwargs."""
    test_set = tmp_path / "ts.yml"
    test_set.write_text(
        "- id: q1\n  question: hi\n  expected_facts: []\n  expected_sources: []\n",
        encoding="utf-8",
    )
    calls: dict = {}

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            calls.update(kwargs)
            self.collection = FakeCollection()
            self.rerank_model = kwargs["rerank_model"]
            self.rerank_candidates = kwargs["rerank_candidates"]
            self.query_expansion = kwargs["query_expansion"]
            self.expansion_model = kwargs["expansion_model"]
            self.expansion_n_queries = kwargs["expansion_n_queries"]
            self.hybrid_fusion = kwargs["hybrid_fusion"]
            self.hybrid_alpha = kwargs["hybrid_alpha"]

    monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
    monkeypatch.setattr(run_eval, "run_evaluation", lambda *a, **k: [])
    monkeypatch.setattr(
        run_eval, "print_summary", lambda *a, **k: {"verdict": "PASS"}
    )

    def _run(extra_args: list[str]) -> dict:
        run_eval.main([str(test_set), "--retrieval-only", *extra_args])
        return calls

    return _run


def test_default_path_uses_settings(captured):
    kwargs = captured([])
    assert kwargs["collection_name"] == settings.collection_name
    assert kwargs["kb_root"] == settings.kb_root
    assert kwargs["structured_lookup_enabled"] is False
    assert kwargs["chroma_dir"] == settings.chroma_dir


def test_default_path_keeps_structured_lookup_flag(captured):
    kwargs = captured(["--structured-lookup"])
    assert kwargs["collection_name"] == settings.collection_name
    assert kwargs["structured_lookup_enabled"] is True


def test_collection_override_forces_structured_lookup_off(captured):
    kwargs = captured(["--collection", "study_st01", "--structured-lookup"])
    assert kwargs["collection_name"] == "study_st01"
    assert kwargs["structured_lookup_enabled"] is False
    # kb_root untouched when only --collection is given
    assert kwargs["kb_root"] == settings.kb_root


def test_kb_root_override(captured):
    kwargs = captured(["--kb-root", "data/study/st01/cards"])
    assert kwargs["kb_root"] == Path("data/study/st01/cards")
    assert kwargs["collection_name"] == settings.collection_name


def test_kb_root_alone_does_not_disable_structured_lookup(captured):
    kwargs = captured(["--kb-root", "data/study/st01/cards", "--structured-lookup"])
    assert kwargs["structured_lookup_enabled"] is True


def test_collection_without_kb_root_warns(captured, capsys):
    captured(["--collection", "study_st01"])
    out = capsys.readouterr().out
    assert "warning" in out.lower()
    assert "--kb-root" in out


def test_collection_with_kb_root_no_warning(captured, capsys):
    captured(["--collection", "study_st01", "--kb-root", "data/study/st01/cards"])
    out = capsys.readouterr().out
    assert "warning: --collection" not in out


# ---- P2 (M-2): 空串拒绝 / P3 (T12): 报告层断言 ----

def test_empty_collection_rejected(captured):
    with pytest.raises(SystemExit) as ei:
        captured(["--collection", ""])
    assert ei.value.code == 2      # argparse usage error, 而非静默回落默认库


def test_empty_kb_root_rejected(captured):
    with pytest.raises(SystemExit) as ei:
        captured(["--kb-root", ""])
    assert ei.value.code == 2


def test_summary_records_collection(captured, tmp_path):
    """报告层: --collection 必须落进 output JSON 的 summary (评测可溯源)."""
    import json
    out_file = tmp_path / "out.json"
    captured(["--collection", "study_st01",
              "--kb-root", "data/study/st01/cards", "--output", str(out_file)])
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert saved["summary"]["collection"] == "study_st01"
    assert saved["summary"]["top_k"] == 15


def test_collection_whitespace_stripped(captured):
    kwargs = captured(["--collection", "  study_st01  ",
                       "--kb-root", "data/study/st01/cards"])
    assert kwargs["collection_name"] == "study_st01"
