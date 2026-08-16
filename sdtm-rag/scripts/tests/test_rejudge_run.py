"""eval/rejudge_run.py 单测 — judge 全 mock, 零 LLM 调用."""
import json

import pytest

import eval.rejudge_run as rr


def _run(rows):
    return {"results": rows}


def test_same_and_diff_counted(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda q, a, f, m: (0.5, [], []))
    run = _run([
        {"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.5,
         "judge_parse_ok": True},
        {"id": "b", "question": "?", "answer": "x", "judge_fact_recall": 1.0,
         "judge_parse_ok": True},
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
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 1.0,
                 "judge_parse_ok": True}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert out["rows"][0]["parse_fail"] is True and out["n_same"] == 0


def test_unknown_id_fails_loud(monkeypatch):
    # facts_by_id 缺题 = run 与题集对不上, 必须 KeyError 而非静默跳过
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: (1.0, [], []))
    run = _run([{"id": "ghost", "question": "?", "answer": "x", "judge_fact_recall": 1.0,
                 "judge_parse_ok": True}])
    with pytest.raises(KeyError):
        rr.rejudge(run, {"a": ["f"]}, "m")


def test_orig_parse_fail_excluded_and_never_judged(monkeypatch):
    # 原 run judge parse 失败的行, judge_fact_recall 是回落的 substring 分 (系统性低估):
    # 拿它当 orig 比几乎必然 not-same, 会把 same_rate 压低却被读成 judge 噪声.
    # 该行必须整行排除出分母, 且**不打 judge** (会 raise 的 mock 证明没打).
    def _boom(*a):
        raise AssertionError("orig parse-fail 行不该调 judge")

    monkeypatch.setattr(rr, "check_fact_recall_judge", _boom)
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.4,
                 "judge_parse_ok": False}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert (out["n"], out["n_same"], out["same_rate"], out["n_orig_parse_fail"]) == (0, 0, 0.0, 1)
    assert out["rows"] == [{"id": "a", "orig_parse_fail": True}]


def test_main_judge_model_mismatch_fails_loud(tmp_path):
    # run 的 judge 模型 ≠ --judge-model = 测的是跨模型分歧, 不是同模型自噪声
    run_p = tmp_path / "run.json"
    run_p.write_text(json.dumps({
        "summary": {"judge_model": "model-a"},
        "results": [{"id": "a", "question": "?", "answer": "x",
                     "judge_fact_recall": 1.0, "judge_parse_ok": True}],
    }), encoding="utf-8")
    ts_p = tmp_path / "ts.yml"
    ts_p.write_text('- id: a\n  question: "?"\n  category: c\n'
                    '  expected_sources: ["x.md"]\n  expected_facts: ["f"]\n', encoding="utf-8")
    with pytest.raises(SystemExit, match="judge model mismatch"):
        rr.main([str(run_p), str(ts_p), "--judge-model", "model-b",
                 "--output", str(tmp_path / "out.json")])
