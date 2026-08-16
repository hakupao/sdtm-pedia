"""eval/rejudge_run.py 单测 — judge 全 mock, 零 LLM 调用."""
import json

import pytest

import eval.rejudge_run as rr


def _run(rows):
    return {"results": rows}


def _boom(*a):
    """judge 桩: 一被调用就红.

    双重作用 —— 既证明「这条路径不该打 judge」, 也保证被测守卫万一回归时,
    用例是零网络零费用地红, 而不是去打真实付费 API 把「零 LLM」变成守卫依赖式的巧合.
    """
    raise AssertionError("本用例不该调 judge (零 LLM 契约)")


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
    # 留在分母 (n=1) 但必须单列计数, 否则与「真分歧」混为一谈
    assert (out["n"], out["n_rejudge_parse_fail"]) == (1, 1)


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
    monkeypatch.setattr(rr, "check_fact_recall_judge", _boom)
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.4,
                 "judge_parse_ok": False}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert (out["n"], out["n_same"], out["same_rate"], out["n_orig_parse_fail"]) == (0, 0, 0.0, 1)
    assert out["rows"] == [{"id": "a", "orig_parse_fail": True}]


def test_missing_judge_parse_ok_key_excluded_and_never_judged(monkeypatch):
    # 钉死 fail-safe 默认值本身 (`.get(..., False)`): 旧版产物的行连 judge_parse_ok 键都
    # 没有, 不能证明 orig 是真语义分 -> 必须排除. 默认值若被写成 True 本例即红.
    monkeypatch.setattr(rr, "check_fact_recall_judge", _boom)
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.7}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert (out["n"], out["n_orig_parse_fail"]) == (0, 1)
    assert out["rows"] == [{"id": "a", "orig_parse_fail": True}]


def _write_min_pair(tmp_path, summary):
    """最小 run json + 最小题集 (零题面: question 一律 "?", id 只用 a)."""
    run_p = tmp_path / "run.json"
    run_p.write_text(json.dumps({
        "summary": summary,
        "results": [{"id": "a", "question": "?", "answer": "x",
                     "judge_fact_recall": 1.0, "judge_parse_ok": True}],
    }), encoding="utf-8")
    ts_p = tmp_path / "ts.yml"
    ts_p.write_text('- id: a\n  question: "?"\n  category: c\n'
                    '  expected_sources: ["x.md"]\n  expected_facts: ["f"]\n', encoding="utf-8")
    return [str(run_p), str(ts_p)]


def test_main_missing_judge_model_key_fails_loud(monkeypatch, tmp_path):
    # 钉死直接下标: summary 无 judge_model (非 --judge 产物) 必须 KeyError,
    # 不许静默回落成 a.judge_model —— 那等于假装模型对得上.
    # 桩顺带钉死「炸点在 judge 之前」: 守卫若回归, 本例零网络照样红 (而非去打真 API).
    monkeypatch.setattr(rr, "check_fact_recall_judge", _boom)
    argv = _write_min_pair(tmp_path, {}) + ["--output", str(tmp_path / "out.json")]
    with pytest.raises(KeyError):
        rr.main(argv)


# ── 抽检方 B 变异补网 (见 evidence/step_u5_audit_mutation.md) ──

def _recorder(monkeypatch, recall=1.0):
    """记录 judge 每次收到的实参, 供入参绑定类断言用."""
    seen = []

    def stub(q, a, f, model):
        seen.append((q, a, f, model))
        return (recall, [], [])

    monkeypatch.setattr(rr, "check_fact_recall_judge", stub)
    return seen


def test_judge_receives_question_answer_facts_model_in_that_order(monkeypatch):
    """入参对调 (question↔answer) 会让 judge 拿题面当答案评 —— 分数照样是个数,
    整个 I1 读数静默作废. 老用例的桩吃任意实参, 照不出来."""
    seen = _recorder(monkeypatch)
    run = _run([{"id": "a", "question": "Q", "answer": "A", "judge_fact_recall": 1.0,
                 "judge_parse_ok": True}])
    rr.rejudge(run, {"a": ["F"]}, "m")
    assert seen == [("Q", "A", ["F"], "m")]


def test_rejudged_recall_keeps_four_decimals(monkeypatch):
    """重判分的精度口径必须与 run 产物一致; 变粗一位就会把真分歧读成"复现"."""
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: (0.123456, [], []))
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.1235,
                 "judge_parse_ok": True}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert out["rows"][0]["rejudged"] == 0.1235
    assert (out["n"], out["n_same"]) == (1, 1)


def test_same_flag_polarity_on_asymmetric_fixture(monkeypatch):
    """1 同 1 异的老 fixture 里 same 判据取反后 n_same 仍是 1 —— 对调型的系统性盲区.
    改成 2 同 1 异后极性就照得出来; 顺带钉死 same_rate 的 round 口径."""
    _recorder(monkeypatch, recall=0.5)
    run = _run([
        {"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.5,
         "judge_parse_ok": True},
        {"id": "b", "question": "?", "answer": "x", "judge_fact_recall": 0.5,
         "judge_parse_ok": True},
        {"id": "c", "question": "?", "answer": "x", "judge_fact_recall": 1.0,
         "judge_parse_ok": True},
    ])
    out = rr.rejudge(run, {i: ["f"] for i in "abc"}, "m")
    assert [r["same"] for r in out["rows"]] == [True, True, False]
    assert (out["n"], out["n_same"], out["same_rate"]) == (3, 2, 0.6667)


def test_denominators_with_mixed_excluded_and_scored_rows(monkeypatch):
    """既有排除行又有计分行时, same_rate 分母与 n_orig_parse_fail 才互相独立.
    老用例要么全排除要么全计分, 两个口径改用 len(rows) 都照样绿."""
    _recorder(monkeypatch, recall=0.5)
    run = _run([
        {"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.4,
         "judge_parse_ok": False},
        {"id": "b", "question": "?", "answer": "x", "judge_fact_recall": 0.5,
         "judge_parse_ok": True},
        {"id": "c", "question": "?", "answer": "x", "judge_fact_recall": 1.0,
         "judge_parse_ok": True},
    ])
    out = rr.rejudge(run, {i: ["f"] for i in "abc"}, "m")
    assert (out["n"], out["n_same"], out["same_rate"]) == (2, 1, 0.5)
    assert out["n_orig_parse_fail"] == 1


def test_main_feeds_expected_facts_not_expected_sources(monkeypatch, tmp_path):
    """事实集取错字段 (expected_sources) 后 judge 照跑照出分, 只是评的东西不对."""
    seen = _recorder(monkeypatch)
    argv = _write_min_pair(tmp_path, {"judge_model": "m"}) + [
        "--judge-model", "m", "--output", str(tmp_path / "out.json")]
    assert rr.main(argv) == 0
    assert [s[2] for s in seen] == [["f"]]


def test_main_judge_model_mismatch_fails_loud(monkeypatch, tmp_path):
    # run 的 judge 模型 ≠ --judge-model = 测的是跨模型分歧, 不是同模型自噪声
    monkeypatch.setattr(rr, "check_fact_recall_judge", _boom)  # 同上: 炸点须在 judge 之前
    argv = _write_min_pair(tmp_path, {"judge_model": "model-a"}) + [
        "--judge-model", "model-b", "--output", str(tmp_path / "out.json")]
    with pytest.raises(SystemExit, match="judge model mismatch"):
        rr.main(argv)
