"""eval/rejudge_run.py 单测 — judge 全 mock, 零 LLM 调用."""
import pytest

import eval.rejudge_run as rr


def _run(rows):
    return {"results": rows}


def test_same_and_diff_counted(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda q, a, f, m: (0.5, [], []))
    run = _run([
        {"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.5},
        {"id": "b", "question": "?", "answer": "x", "judge_fact_recall": 1.0},
    ])
    out = rr.rejudge(run, {"a": ["f"], "b": ["f"]}, "m")
    assert (out["n"], out["n_same"], out["same_rate"]) == (2, 1, 0.5)


def test_out_of_scope_skipped(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: (1.0, [], []))
    assert rr.rejudge(_run([{"id": "a", "out_of_scope": True}]), {}, "m")["n"] == 0


def test_missing_full_answer_fails_loud():
    run = _run([{"id": "a", "question": "?", "judge_fact_recall": 1.0}])
    with pytest.raises(SystemExit):
        rr.rejudge(run, {"a": ["f"]}, "m")


def test_parse_fail_counts_as_not_same(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: None)
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 1.0}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert out["rows"][0]["parse_fail"] is True and out["n_same"] == 0


def test_unknown_id_fails_loud(monkeypatch):
    # facts_by_id 缺题 = run 与题集对不上, 必须 KeyError 而非静默跳过
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: (1.0, [], []))
    run = _run([{"id": "ghost", "question": "?", "answer": "x", "judge_fact_recall": 1.0}])
    with pytest.raises(KeyError):
        rr.rejudge(run, {"a": ["f"]}, "m")
