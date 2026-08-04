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


# ---- golden set v1.1: out_of_scope 题不计入 recall 统计 ----

def _mk_result(qid, cat, recall, **extra):
    return {"id": qid, "category": cat, "question": "q", "source_recall": recall,
            "source_hits": [], "source_misses": [], "top5_sources": [],
            "top5_similarities": [], **extra}


def test_out_of_scope_excluded_from_average(capsys):
    """out_of_scope 题在 harness 里无判别力 (无答案可判), 必须排除出平均值."""
    from eval.run_eval import print_summary
    results = [
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("b", "field_lookup", 0.0),
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ]
    summary = print_summary(results, retrieval_only=True)
    assert summary["n_scored"] == 2
    assert summary["source_recall_avg"] == 0.5   # 不是 (1+0+1)/3 = 0.667
    assert summary["n_out_of_scope"] == 1


def test_out_of_scope_listed_separately(capsys):
    from eval.run_eval import print_summary
    print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ], retrieval_only=True)
    out = capsys.readouterr().out
    assert "out_of_scope" in out and "z" in out


def test_no_out_of_scope_keeps_old_behaviour(capsys):
    from eval.run_eval import print_summary
    summary = print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("b", "field_lookup", 0.0),
    ], retrieval_only=True)
    assert summary["source_recall_avg"] == 0.5
    assert summary["n_scored"] == 2
    assert summary.get("n_out_of_scope", 0) == 0


def test_run_evaluation_propagates_out_of_scope():
    """yml 的 out_of_scope 必须原样带进 result, 否则 print_summary 看不到."""
    from eval.run_eval import run_evaluation

    class _Chunk:
        source, similarity = "st01__X__Y.md", 0.5

    class _Rag:
        def retrieve(self, q, top_k=None):
            return [_Chunk()]

    res = run_evaluation(
        [{"id": "z", "category": "negative", "question": "q",
          "expected_sources": [], "out_of_scope": True}],
        _Rag(), retrieval_only=True,
    )
    assert res[0]["out_of_scope"] is True


def test_summary_reports_total_and_scored_separately():
    """n_questions 在 out_of_scope 过滤后语义已变 → 必须同时给出总题数, 否则读者被误导."""
    from eval.run_eval import print_summary
    summary = print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ], retrieval_only=True)
    assert summary["n_scored"] == 1
    assert summary["n_total"] == 2


def test_all_out_of_scope_does_not_divide_by_zero():
    from eval.run_eval import print_summary
    summary = print_summary([
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ], retrieval_only=True)
    assert summary["n_scored"] == 0
    assert summary["source_recall_avg"] == 0.0
