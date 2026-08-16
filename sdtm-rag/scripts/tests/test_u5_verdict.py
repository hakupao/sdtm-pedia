"""eval/u5_verdict.py 单测 — 全合成 fixture, 判定逻辑逐条钉死 (U3 §6-10 教训:
判定脚本零测试 = 结论可翻不留痕). 变异集含对调型 (U2 §4.1 方向③)."""
import pytest

from eval.u5_verdict import (FRAGILE_4, build_verdict, paired_effect,
                             scores_by_id, stability)


def _mkrun(scores: dict, n: int):
    """scores: id -> float (judge 分) | None (parse 失败)."""
    return {"summary": {"n_questions": n},
            "results": [{"id": i, "judge_fact_recall": (s if s is not None else 0.0),
                         "judge_parse_ok": s is not None} for i, s in scores.items()]}


def test_scores_by_id_none_on_parse_fail_and_skips_oos():
    run = _mkrun({"a": 1.0, "b": None}, n=2)
    run["results"].append({"id": "c", "out_of_scope": True, "judge_fact_recall": 1.0,
                          "judge_parse_ok": True})
    assert scores_by_id(run) == {"a": 1.0, "b": None}


def test_stability_flags_flip_and_parse_fail():
    r_ok = _mkrun({"a": 1.0, "b": 0.5, "c": 1.0}, n=48)
    r_flip = _mkrun({"a": 1.0, "b": 1.0, "c": 1.0}, n=48)      # b 翻转
    r_pf = _mkrun({"a": 1.0, "b": 0.5, "c": None}, n=48)       # c parse 失败
    stable, unstable = stability([r_ok, r_flip, r_pf])
    assert stable == {"a": 1.0}
    assert unstable == ["b", "c"]


def test_stability_rejects_mismatched_question_sets():
    with pytest.raises(AssertionError):
        stability([_mkrun({"a": 1.0}, n=48), _mkrun({"b": 1.0}, n=48),
                   _mkrun({"a": 1.0}, n=48)])


def test_paired_effect_two_sided_and_pt_math():
    a = {"q1": 1.0, "q2": 1.0, "q3": 0.5}
    b = {"q1": 0.5, "q2": 1.0, "q3": 1.0}
    e = paired_effect(a, b, n_scored=48)
    assert e["confirmed_cost_ids"] == ["q1"] and e["confirmed_gain_ids"] == ["q3"]
    assert e["confirmed_cost_pt"] == round(100 * 0.5 / 48, 2)   # 1.04pt
    assert e["confirmed_gain_pt"] == round(100 * 0.5 / 48, 2)


def test_paired_effect_swap_symmetry():
    # 对调型守卫: 输入对调后 cost/gain 必须互换 (集合断言的系统性盲区)
    a, b = {"q1": 1.0}, {"q1": 0.0}
    assert paired_effect(a, b, 48)["confirmed_cost_ids"] == \
           paired_effect(b, a, 48)["confirmed_gain_ids"] == ["q1"]


def _happy_inputs(cards_both_scores=None):
    cs = {f"q{i}": 1.0 for i in range(4)}
    cb = cards_both_scores or dict(cs)
    ds = {f"d{i}": 1.0 for i in range(3)}
    runs = {"cards_study": [_mkrun(cs, 48)] * 3, "cards_both": [_mkrun(cb, 48)] * 3,
            "docs_study": [_mkrun(ds, 30)] * 3, "docs_both": [_mkrun(ds, 30)] * 3}
    probes = {"cards": {"same_rate": 1.0, "n": 48}, "docs": {"same_rate": 1.0, "n": 30}}
    controls = {"docs_positive": {"avg": 1.0}, "docs_negative": {"avg": 0.0},
                "cards_positive": {"avg": 1.0}, "cards_negative": {"avg": 0.0}}
    return runs, probes, controls


def test_build_verdict_happy_path_cheap():
    v, rc = build_verdict(*_happy_inputs())
    assert rc == 0 and v["E2_verdict"] == "cheap_on_this_ruler"
    assert v["I1"]["pass"] and v["I2"]["pass"] and v["I3"]["pass"]
    assert v["advisory_only"] is False


def test_build_verdict_cost_reported():
    cb = {"q0": 0.5, "q1": 1.0, "q2": 1.0, "q3": 1.0}
    v, rc = build_verdict(*_happy_inputs(cards_both_scores=cb))
    assert rc == 0 and v["E2_verdict"] == "cost_reported"
    assert v["E"]["cards"]["confirmed_cost_ids"] == ["q0"]


def test_build_verdict_i2_trigger_blocks_e():
    runs, probes, controls = _happy_inputs()
    # cards 阈值是绝对数 7 — 用 8 题全翻钉死触发:
    big = {f"q{i}": 1.0 for i in range(8)}
    big_flip = {f"q{i}": 0.0 for i in range(8)}
    runs["cards_study"] = [_mkrun(big, 48), _mkrun(big_flip, 48), _mkrun(big, 48)]
    runs["cards_both"] = [_mkrun(big, 48)] * 3
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 2 and v["E"] is None and v["E2_verdict"] == "instrument_unusable"


def test_build_verdict_i3_trigger():
    runs, probes, controls = _happy_inputs()
    controls["cards_negative"] = {"avg": 0.5}                   # 阴性对照失守
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 2 and v["E2_verdict"] == "controls_failed" and v["E"] is None


def test_build_verdict_i1_degrades_to_advisory():
    runs, probes, controls = _happy_inputs()
    probes["docs"] = {"same_rate": 0.90, "n": 30}
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 3 and v["advisory_only"] is True and v["E"] is not None


def test_build_verdict_rejects_probe_n_zero():
    """probe n=0 时 rejudge_run 会吐 same_rate=0.0 (无意义值) — 必须炸而不是当 I1 失守.
    (Task 2 复审遗留: same_rate 读数须与 n 同看)"""
    runs, probes, controls = _happy_inputs()
    probes["docs"] = {"same_rate": 0.0, "n": 0}
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_wrong_n():
    runs, probes, controls = _happy_inputs()
    runs["cards_study"] = [_mkrun({"q0": 1.0}, 47)] * 3        # 题集变了 = 阈值失义
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_fragile_and_undecidable_reported():
    runs, probes, controls = _happy_inputs()
    cs = {FRAGILE_4[0]: 1.0, "x": 1.0}
    cb = {FRAGILE_4[0]: 0.5, "x": 1.0}
    runs["cards_study"] = [_mkrun(cs, 48)] * 3
    runs["cards_both"] = [_mkrun(cb, 48)] * 3
    v, _ = build_verdict(runs, probes, controls)
    f = v["E3_fragile"][FRAGILE_4[0]]
    assert (f["study"], f["both"], f["stable_study"], f["stable_both"]) == (1.0, 0.5, True, True)
    assert v["E4_undecidable"] == {"cards": [], "docs": []}
