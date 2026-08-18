"""U6 修订判据判定脚本 (eval/u6_gate_verdict.py) 的七条条款 + 输入校验.

**为什么这个文件存在**: U3 的同类脚本 (`eval/u3_task8_verdict.py`) 此前零测试, 抽检方 B
实测**五个变异全部存活** (见 `test_u3_task8_verdict.py` 文件头), 其中两个是「对调型」——
两侧同形状的数, 差一个减号方向, 眼睛读不出来。本脚本是 U6 全闸 rc 的唯一出处, 且条款 4/7
把这个形态**翻倍** (fatal 列 + exact 列, 各自 base 与 after 对减), 故每一列各配一条对调型
用例, 外加一条「两条条款别读同一组」的交叉接线用例。

做法: 合成 run fixture (`mk_run`), 零真实题面 —— `question` 字段一律占位串, 用来钉红线
(判定产物与 stdout 都不许带题面)。不读真实产物, 不发任何 LLM 请求。
"""
import copy
import json

import pytest

from eval.u6_gate_verdict import main, validate_inputs, verdict

# 红线哨兵: 只要它出现在 verdict 产物 / stdout 里, 就是题面泄漏的形态
QMARK = "PLACEHOLDER-QUESTION-TEXT-DO-NOT-EMIT"


def mk_run(idx, *, fatal=0, legacy=179, dist_exact=12, dist_fatal=0,
           u1_exact=27, u1_fatal=0, dev=12, heldout=12, gen="t0",
           git_rev="abc1234", preds=None):
    """一遍 run 的合成产物 (结构照 Task 1 修缮后的 run_routing_eval 落盘形状)。

    `preds` 给条款 6 用: {题号: 该遍的 pred}; 不给时只放一条 final 题。
    """
    detail = [{"id": "final_x", "group": "final", "gold": "study", "pred": "cdisc",
               "question": QMARK}]
    detail += [{"id": qid, "group": "dev", "gold": "study", "pred": pred, "question": QMARK}
               for qid, pred in (preds or {}).items()]
    return {"meta": {"generated_at": f"{gen}-{idx}", "git_rev": git_rev, "runs_arg": 3,
                     "run_index": idx, "n_gold": 254, "out_prefix": "x"},
            "summary": {"fatal_excl_final": fatal, "fatal_ids_excl_final": [],
                        "legacy_exact": legacy, "legacy_floor": 178,
                        "by_group": {"legacy": {"n": 181, "exact": legacy, "fatal": fatal},
                                     "dev": {"n": 12, "exact": dev, "fatal": 0},
                                     "heldout": {"n": 12, "exact": heldout, "fatal": 0},
                                     "distractor_cdisc": {"n": 12, "exact": dist_exact,
                                                          "fatal": dist_fatal},
                                     "u1_doc": {"n": 27, "exact": u1_exact, "fatal": u1_fatal},
                                     "final": {"n": 4, "exact": 0, "fatal": 4}}},
            "detail": detail}


BASE = [mk_run(i, fatal=10, dist_fatal=2, u1_fatal=1, dev=6, gen="base") for i in (1, 2, 3)]


def after_runs(**kw):
    return [mk_run(i, gen="after", **kw) for i in (1, 2, 3)]


def base_runs(**kw):
    kw = {"fatal": 10, "dist_fatal": 2, "u1_fatal": 1, "dev": 6, **kw}
    return [mk_run(i, gen="base", **kw) for i in (1, 2, 3)]


# --------------------------------------------------------------------------- brief 的七条


def test_all_pass_rc0():
    after = [mk_run(i, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 0 and out["clause1"]["pass"] and out["clause4"]["pass"] and out["clause7"]["pass"]


def test_clause4_fatal_column_trips():       # 非致命→致命 (exact 持平也要拦; U3 尺子盲区)
    after = [mk_run(i, dist_fatal=3, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 1 and not out["clause4"]["pass"] and out["clause4"]["fatal"] == {"base": 2.0,
                                                                                 "after": 3.0}


def test_clause4_exact_column_trips():
    after = [mk_run(i, dist_exact=10, dist_fatal=0, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 1 and not out["clause4"]["pass"]


def test_clause7_u1doc_drift_trips():        # I-3 真空修复: u1_doc exact 掉 2 就拦
    after = [mk_run(i, u1_exact=25, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 1 and not out["clause7"]["pass"]


def test_input_validation_same_content_rejected():   # I-2: baseline=after 拷贝错
    after = copy.deepcopy(BASE)
    with pytest.raises(SystemExit, match="baseline 与 after 内容相同"):
        validate_inputs(BASE, after)


def test_input_validation_needs_three_each():
    with pytest.raises(SystemExit, match="各需 3 份"):
        validate_inputs(BASE[:2], BASE)


def test_input_validation_needs_meta():
    b = copy.deepcopy(BASE)
    del b[0]["meta"]
    with pytest.raises(SystemExit, match="缺 meta"):
        validate_inputs(b, [mk_run(i, gen="a") for i in (1, 2, 3)])


# --------------------------------------------------------------------------- 条款 1/2/3


@pytest.mark.parametrize("legacy,expected", [(177, False), (178, True), (179, True)])
def test_clause1_legacy_floor_is_178(legacy, expected):
    """178 是 spec §7「不许下调」的那个数 —— 两侧边界都钉, 防「floor 下调」型变异。"""
    out, _ = verdict(BASE, after_runs(legacy=legacy))
    assert out["clause1"]["pass"] is expected


def test_clause1_any_non_final_fatal_trips():
    """变异形态: `== 0` 写成 `>= 0` 即恒真。fixture 的 final 组恒有 4 个 fatal,
    条款 1 却仍须 PASS —— 口径是「全集减 final 组」。"""
    assert verdict(BASE, after_runs(fatal=1))[0]["clause1"]["pass"] is False
    assert verdict(BASE, after_runs())[0]["clause1"]["pass"] is True


def test_clause2_measures_heldout_against_dev_not_the_reverse():
    """**对调型**: dev 满分而 heldout 零分, 是条款 2 要抓的那一格 (泛化崩了)。

    `hold >= dev - 25` 对调成 `dev >= hold - 25` 时, 这组数据会变成 PASS。
    """
    out, rc = verdict(BASE, after_runs(dev=12, heldout=0))
    assert rc == 1 and out["clause2"]["pass"] is False
    assert out["clause1"]["pass"] and out["clause3"]["pass"], "只该条款 2 红, 否则归因不成立"


def test_clause2_does_not_trip_when_heldout_beats_dev():
    # 反向: heldout 高于 dev 永远不该触发 (条款 2 只看泛化掉多少)
    out, _ = verdict(BASE, after_runs(dev=10, heldout=12))
    assert out["clause2"]["pass"] is True


def test_clause2_gap_boundary_is_25pt():
    # 12→9 = 25.0pt 差, 恰在界上 (PASS); 8 → 33.3pt 触发
    assert verdict(BASE, after_runs(dev=12, heldout=9))[0]["clause2"]["pass"] is True
    assert verdict(BASE, after_runs(dev=12, heldout=8))[0]["clause2"]["pass"] is False


@pytest.mark.parametrize("dev,expected", [(9, False), (10, True)])
def test_clause3_dev_floor_is_10(dev, expected):
    out, _ = verdict(BASE, after_runs(dev=dev, heldout=dev))
    assert out["clause3"]["pass"] is expected
    assert out["clause1"]["pass"], "只该条款 3 红, 否则归因不成立"


def test_clause2_carries_the_majority_baseline_sentence():
    """抽检 A-2: 条款 2/3 单独看零判别力 (多数类 100%)。整句必须在产物里, 且带数值。"""
    out, _ = verdict(BASE, after_runs())
    note = out["clause2"]["majority_note"]
    assert "100%" in note and "不得单独引用" in note


# --------------------------------------------------------------------------- 条款 4/7 双列


@pytest.mark.parametrize("clause,group", [("clause4", "distractor_cdisc"), ("clause7", "u1_doc")])
def test_dual_gate_reports_both_columns(clause, group):
    out, _ = verdict(BASE, after_runs())
    assert out[clause]["group"] == group
    assert set(out[clause]) == {"group", "fatal", "exact", "pass", "note"}
    # 诚实声明必须跟着数字走 (spec §4.2): 判别力在 exact 半, fatal 半由构造保证
    assert "widen-only" in out[clause]["note"] and "exact" in out[clause]["note"]


def test_clause4_and_clause7_do_not_read_the_same_group():
    """交叉接线防护: 只动 distractor 组, 条款 7 必须不动 (反之亦然)。"""
    only_dist, _ = verdict(BASE, after_runs(dist_exact=8))
    assert only_dist["clause4"]["pass"] is False and only_dist["clause7"]["pass"] is True
    only_u1, _ = verdict(BASE, after_runs(u1_exact=20))
    assert only_u1["clause7"]["pass"] is False and only_u1["clause4"]["pass"] is True


@pytest.mark.parametrize("clause,base_kw,after_kw", [
    ("clause4", {"dist_exact": 12}, {"dist_exact": 12}),
    ("clause7", {"u1_exact": 27}, {"u1_exact": 27}),
])
def test_dual_gate_exact_direction_not_reversed(clause, base_kw, after_kw):
    """**对调型**: `eb - ea <= 1` 写成 `ea - eb <= 1` 时, 下降 4 题会变 PASS 而
    改善 4 题会变触发 —— 与用途正好相反。两个方向都钉。"""
    drop_key, = after_kw
    dropped = verdict(base_runs(**base_kw), after_runs(**{drop_key: after_kw[drop_key] - 4}))[0]
    gained = verdict(base_runs(**{drop_key: base_kw[drop_key] - 4}), after_runs(**after_kw))[0]
    assert dropped[clause]["pass"] is False, "较基线下降 4 题必须触发"
    assert gained[clause]["pass"] is True, "较基线改善 4 题不得触发"


@pytest.mark.parametrize("after_exact,expected", [(12, True), (11, True), (10, False)])
def test_dual_gate_exact_allows_drop_of_exactly_one(after_exact, expected):
    out, _ = verdict(base_runs(dist_exact=12), after_runs(dist_exact=after_exact))
    assert out["clause4"]["pass"] is expected


@pytest.mark.parametrize("after_fatal,expected", [(1, True), (2, True), (3, False)])
def test_dual_gate_fatal_allows_equal_but_not_increase(after_fatal, expected):
    """**对调型 + 边界**: fatal 半是「不得增加」, 持平放行, 多 1 个就拦。"""
    out, _ = verdict(base_runs(dist_fatal=2), after_runs(dist_fatal=after_fatal))
    assert out["clause4"]["pass"] is expected


def test_dual_gate_columns_are_independent():
    """fatal 改善不许把 exact 下降盖掉 (双列是 AND, 不是「综合看」)。"""
    out, rc = verdict(base_runs(dist_fatal=5, dist_exact=12),
                      after_runs(dist_fatal=0, dist_exact=8))
    assert out["clause4"]["fatal"] == {"base": 5.0, "after": 0.0}
    assert out["clause4"]["pass"] is False and rc == 1


# --------------------------------------------------------------------------- 条款 5/6 + rc


def test_clause5_final_group_is_report_only():
    """fixture 每遍 final 组都有 4 个 fatal / 0 exact, 全 PASS 用例仍须 rc=0。"""
    out, rc = verdict(BASE, after_runs())
    assert rc == 0
    assert out["clause5_final_report_only"] == [{"final_x": "cdisc"}] * 3
    assert "pass" not in out["clause5_final_report_only"][0]


def test_clause6_flags_only_the_unstable_ids():
    after = [mk_run(i, gen="after", preds={"q_stable": "study", "q_flappy": p})
             for i, p in zip((1, 2, 3), ("study", "both", "study"), strict=True)]
    out, rc = verdict(BASE, after)
    assert out["clause6_unstable"] == ["q_flappy"]
    assert rc == 0, "条款 6 只报告, 不进 rc"


@pytest.mark.parametrize("kw,red", [
    ({"legacy": 100}, "clause1"),
    ({"dev": 12, "heldout": 0}, "clause2"),
    ({"dev": 3, "heldout": 3}, "clause3"),
    ({"dist_exact": 5}, "clause4"),
    ({"u1_exact": 5}, "clause7"),
])
def test_rc_is_1_when_any_gating_clause_trips(kw, red):
    out, rc = verdict(BASE, after_runs(**kw))
    assert rc == 1 and out[red]["pass"] is False


# --------------------------------------------------------------------------- 输入校验 (I-2 等)


def test_same_summary_but_different_run_is_not_rejected():
    """确定性跑批下两批 summary 可以逐字相同; I-2 只拦「连 meta 都一样」的拷贝错。"""
    after = [copy.deepcopy(r) for r in BASE]
    for i, r in enumerate(after, 1):
        r["meta"]["generated_at"] = f"after-{i}"
    validate_inputs(BASE, after)      # 不抛


def test_missing_group_is_rejected():
    after = after_runs()
    del after[0]["summary"]["by_group"]["u1_doc"]
    with pytest.raises(SystemExit, match="缺 group"):
        validate_inputs(BASE, after)


def test_dual_gate_group_size_mismatch_is_rejected():
    """两把不同长度的尺子相减 = 静默翻结论 (27 题组缩到 20 题, exact 差值照样算得出)。"""
    after = after_runs()
    for r in after:
        r["summary"]["by_group"]["u1_doc"] = {"n": 20, "exact": 20, "fatal": 0}
    with pytest.raises(SystemExit, match="组量在六份 run 间不一致"):
        validate_inputs(BASE, after)


def test_dev_group_size_must_match_the_percentage_denominator():
    after = after_runs()
    after[1]["summary"]["by_group"]["dev"] = {"n": 11, "exact": 11, "fatal": 0}
    with pytest.raises(SystemExit, match="组量"):
        validate_inputs(BASE, after)


def test_dirty_git_rev_warns_but_does_not_fail(capsys):
    after = [mk_run(i, gen="after", git_rev="v1.4-7-gdeadbee-dirty") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 0, "脏树只告警, 不拦"
    assert capsys.readouterr().out.count("脏工作树") == 3


def test_shared_git_rev_between_base_and_after_warns(capsys):
    # fixture 两批同为 abc1234 → 告警; 尾段比对 (describe 串 vs 裸 sha) 也须认得
    verdict(BASE, [mk_run(i, gen="after", git_rev="v1.4-7-gabc1234") for i in (1, 2, 3)])
    assert "共用 git_rev" in capsys.readouterr().out


def test_unknown_git_rev_does_not_trigger_shared_warning(capsys):
    base = [mk_run(i, fatal=10, dist_fatal=2, u1_fatal=1, dev=6, gen="base", git_rev="unknown")
            for i in (1, 2, 3)]
    verdict(base, [mk_run(i, gen="after", git_rev="unknown") for i in (1, 2, 3)])
    assert "共用 git_rev" not in capsys.readouterr().out


# --------------------------------------------------------------------------- 红线 + CLI


def test_verdict_output_never_carries_question_text():
    out, _ = verdict(BASE, after_runs(preds={"q1": "study"}))
    assert QMARK not in json.dumps(out, ensure_ascii=False)


def _write(tmp_path, name, runs):
    paths = []
    for i, r in enumerate(runs, 1):
        p = tmp_path / f"{name}_{i}.json"
        p.write_text(json.dumps(r, ensure_ascii=False), encoding="utf-8")
        paths.append(str(p))
    return paths


def test_main_cli_writes_output_and_returns_rc(tmp_path, capsys):
    b = _write(tmp_path, "base", BASE)
    a = _write(tmp_path, "after", after_runs())
    out_path = tmp_path / "verdict.json"
    rc = main(["--baseline", *b, "--after", *a, "--output", str(out_path)])
    printed = capsys.readouterr().out
    assert rc == 0 and "rc=0" in printed
    saved = json.loads(out_path.read_text(encoding="utf-8"))
    assert saved["clause4"]["pass"] and saved["clause7"]["pass"]
    assert QMARK not in printed and QMARK not in out_path.read_text(encoding="utf-8")


def test_main_cli_prints_clause1_per_run_numbers(tmp_path, capsys):
    """主闸的逐遍原料不许只活在 --output 的 json 里 (stdout 那行被 per_run 过滤成空 {})。"""
    b = _write(tmp_path, "base", BASE)
    a = _write(tmp_path, "after", after_runs(legacy=181))
    main(["--baseline", *b, "--after", *a])
    printed = capsys.readouterr().out
    assert printed.count("legacy=181 (floor 178)") == 3
    assert QMARK not in printed


def test_main_cli_returns_1_and_names_the_tripped_clause(tmp_path, capsys):
    b = _write(tmp_path, "base", BASE)
    a = _write(tmp_path, "after", after_runs(u1_exact=20))
    rc = main(["--baseline", *b, "--after", *a])
    printed = capsys.readouterr().out
    assert rc == 1 and "rc=1" in printed
    assert "clause7 ⛔" in printed and "clause4 PASS" in printed


def test_main_cli_rejects_two_baselines(tmp_path):
    b = _write(tmp_path, "base", BASE)
    a = _write(tmp_path, "after", after_runs())
    with pytest.raises(SystemExit):     # argparse nargs=3 → rc 2
        main(["--baseline", *b[:2], "--after", *a])
