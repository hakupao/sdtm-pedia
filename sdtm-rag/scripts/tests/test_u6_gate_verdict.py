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


def mk_batch(gen, **kw):
    """一批三遍。任一 kwarg 传 3 元列表即**逐遍不同** —— 异质 fixture 是刚需:

    三遍数字全同质时, 「每遍都要满足」与「只看第一遍」、「三遍均值」与「取第一遍」在断言里
    完全同形, 聚合塌成一遍的变异会全数存活 (审查方实测 3/3 存活)。
    """
    def per_run(v, i):
        return v[i] if isinstance(v, list | tuple) else v

    return [mk_run(idx, gen=gen, **{k: per_run(v, idx - 1) for k, v in kw.items()})
            for idx in (1, 2, 3)]


def after_runs(**kw):
    return mk_batch("after", **kw)


def base_runs(**kw):
    return mk_batch("base", **{"fatal": 10, "dist_fatal": 2, "u1_fatal": 1, "dev": 6, **kw})


# 条款 4/7 的双列闸口径完全相同, 只是读不同的组 —— 边界与方向用例两条条款各跑一遍,
# 免得 clause7 一直蹭 clause4 的 _dual_gate 覆盖 (审查 Minor 3)。
DUAL = [("clause4", "dist_exact", "dist_fatal", 12), ("clause7", "u1_exact", "u1_fatal", 27)]


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


def test_input_validation_needs_three_in_the_after_batch_too():
    """三遍纪律是**两臂**的事。上一条只短了 baseline 一臂, 于是「after 臂 (正被判定的
    那一批) 传两份照样放行」这个方向从未被量 (finding F-03)。"""
    with pytest.raises(SystemExit, match="各需 3 份"):
        validate_inputs(BASE, after_runs()[:2])


def test_input_validation_needs_meta():
    b = copy.deepcopy(BASE)
    del b[0]["meta"]
    with pytest.raises(SystemExit, match="缺 meta"):
        validate_inputs(b, [mk_run(i, gen="a") for i in (1, 2, 3)])


@pytest.mark.parametrize("stamp", ["", "   "])
def test_input_validation_rejects_a_blank_generated_at(stamp):
    """meta 在场但没有跑批时刻, 后果不是错话术而是**直接放行** (抽检 B 探针 3 实测)。

    `generated_at` 是批内去重闸的全部原料: 三份里有一份为空、另两份时戳互不相同, 去重闸
    就不响, 一份没有跑批时刻的 run 被当成合法证据收下, 且此后它与任何一份 run 都「不重复」。
    """
    b = copy.deepcopy(BASE)
    b[0]["meta"]["generated_at"] = stamp
    with pytest.raises(SystemExit, match="缺 meta.generated_at"):
        validate_inputs(b, after_runs())


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


@pytest.mark.parametrize("clause,ekey,fkey,full", DUAL)
def test_dual_gate_exact_direction_not_reversed(clause, ekey, fkey, full):
    """**对调型**: `eb - ea <= 1` 写成 `ea - eb <= 1` 时, 下降 4 题会变 PASS 而
    改善 4 题会变触发 —— 与用途正好相反。两个方向都钉。"""
    dropped = verdict(base_runs(**{ekey: full}), after_runs(**{ekey: full - 4}))[0]
    gained = verdict(base_runs(**{ekey: full - 4}), after_runs(**{ekey: full}))[0]
    assert dropped[clause]["pass"] is False, "较基线下降 4 题必须触发"
    assert gained[clause]["pass"] is True, "较基线改善 4 题不得触发"


@pytest.mark.parametrize("clause,ekey,fkey,full", DUAL)
@pytest.mark.parametrize("drop,expected", [(0, True), (1, True), (2, False)])
def test_dual_gate_exact_allows_drop_of_exactly_one(clause, ekey, fkey, full, drop, expected):
    out, _ = verdict(base_runs(**{ekey: full}), after_runs(**{ekey: full - drop}))
    assert out[clause]["pass"] is expected


@pytest.mark.parametrize("clause,ekey,fkey,full", DUAL)
@pytest.mark.parametrize("after_fatal,expected", [(1, True), (2, True), (3, False)])
def test_dual_gate_fatal_allows_equal_but_not_increase(clause, ekey, fkey, full,
                                                      after_fatal, expected):
    """**对调型 + 边界**: fatal 半是「不得增加」, 持平放行, 多 1 个就拦。"""
    out, _ = verdict(base_runs(**{fkey: 2}), after_runs(**{fkey: after_fatal}))
    assert out[clause]["pass"] is expected


def test_dual_gate_columns_are_independent():
    """fatal 改善不许把 exact 下降盖掉 (双列是 AND, 不是「综合看」)。"""
    out, rc = verdict(base_runs(dist_fatal=5, dist_exact=12),
                      after_runs(dist_fatal=0, dist_exact=8))
    assert out["clause4"]["fatal"] == {"base": 5.0, "after": 0.0}
    assert out["clause4"]["pass"] is False and rc == 1


# ------------------------------------------------------------------- 三遍语义 (异质 fixture)
#
# 以下每条都造成「第一遍干净, 第二/三遍才出事」的形状 —— 把聚合塌成第一遍的变异会给出与
# 真实判定**相反**的结果。三遍数字同质时这类变异 3/3 存活 (审查方实测: 条款 1 的 all(...)
# 改 after[:1] / _dual_gate 均值改 [0] / 条款 2·3 均值改第一遍, 48 条照样全绿)。


def test_clause1_reads_every_run_not_just_the_first():
    """条款 1 的口径是「三遍**每一遍**」: 第 2 遍跌破 floor、第 3 遍冒出 fatal, 都得红。"""
    assert verdict(BASE, after_runs(legacy=[179, 177, 179]))[0]["clause1"]["pass"] is False
    assert verdict(BASE, after_runs(fatal=[0, 0, 2]))[0]["clause1"]["pass"] is False
    # 反向: 三遍逐遍不同但都合格, 不得误红
    assert verdict(BASE, after_runs(legacy=[179, 178, 181]))[0]["clause1"]["pass"] is True


def test_clause3_reads_the_three_run_mean_not_the_first_run():
    # dev 三遍 12/12/3 → 均值 9 < 10 触发; 取第一遍 (12) 则 PASS
    out, _ = verdict(BASE, after_runs(dev=[12, 12, 3]))
    assert out["clause3"]["dev_mean"] == 9.0 and out["clause3"]["pass"] is False


def test_clause2_reads_the_three_run_mean_not_the_first_run():
    # heldout 三遍 12/12/0 → 均值 8/12 = 66.67% vs dev 100% → 33.3pt 触发; 取第一遍则 PASS
    out, _ = verdict(BASE, after_runs(heldout=[12, 12, 0]))
    assert out["clause2"]["heldout_pct"] == 66.67 and out["clause2"]["pass"] is False


@pytest.mark.parametrize("clause,ekey,fkey,full", DUAL)
def test_dual_gate_exact_reads_the_three_run_mean(clause, ekey, fkey, full):
    """after 三遍 full/full/(full-6) → 均值 full-2, 掉 2 题必须触发; 只看第一遍则 full vs full。"""
    out, rc = verdict(base_runs(**{ekey: full}), after_runs(**{ekey: [full, full, full - 6]}))
    assert out[clause]["exact"] == {"base": float(full), "after": float(full) - 2}
    assert out[clause]["pass"] is False and rc == 1


@pytest.mark.parametrize("clause,ekey,fkey,full", DUAL)
def test_dual_gate_fatal_reads_the_three_run_mean(clause, ekey, fkey, full):
    """基线零 fatal, after 只在第三遍冒 3 个 → 均值 1.0 > 0 必须触发 (第一遍看不见)。"""
    out, _ = verdict(base_runs(**{fkey: 0}), after_runs(**{fkey: [0, 0, 3]}))
    assert out[clause]["fatal"] == {"base": 0.0, "after": 1.0}
    assert out[clause]["pass"] is False


def test_dual_gate_reads_the_baseline_mean_too():
    """基线侧同样是三遍均值: 基线 6/12/12 的均值是 10, 不是第一遍那个 6。

    这一格 after 是改善 (不触发), 故只有归档下来的数字能揭穿塌遍 —— 而那个数字要进 checkpoint。
    """
    out, _ = verdict(base_runs(dist_exact=[6, 12, 12]), after_runs(dist_exact=12))
    assert out["clause4"]["exact"] == {"base": 10.0, "after": 12.0}
    assert out["clause4"]["pass"] is True


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


def test_shared_generated_at_alone_is_not_a_copy_error():
    """I-2 是**合取**: summary 逐字相同 **且** meta 撞上才算拷贝错。

    上一条覆盖了 meta 半 (summary 同而 meta 不同 ⇒ 不拦); 这一条是另一半 —— 两批时戳撞上
    而 summary 不同, 同样不该拦 (finding F-13)。丢掉 summary 半的实现会在这里误拦。
    """
    after = after_runs()
    after[0]["meta"]["generated_at"] = BASE[0]["meta"]["generated_at"]
    validate_inputs(BASE, after)      # 不抛


def test_duplicate_run_within_the_after_batch_is_rejected():
    """同一份 after 喂三遍: 条款 1 的「每遍」与均值全都恒等于那一遍, clause6 还会报
    「三遍全稳」—— 不拦的话这是全绿产物里最有欺骗性的一格。"""
    one = after_runs()[0]
    triple = [one, copy.deepcopy(one), copy.deepcopy(one)]
    with pytest.raises(SystemExit, match="generated_at 有重复"):
        validate_inputs(BASE, triple)
    with pytest.raises(SystemExit, match="generated_at 有重复"):   # verdict 也走同一道闸
        verdict(BASE, triple)


def test_duplicate_run_within_the_baseline_batch_is_rejected():
    one = BASE[0]
    with pytest.raises(SystemExit, match="generated_at 有重复"):
        validate_inputs([one, copy.deepcopy(one), copy.deepcopy(one)], after_runs())


def test_three_distinct_runs_are_not_rejected():
    validate_inputs(BASE, after_runs())      # 反向闸: 去重闸不许把正常三遍拦掉


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


@pytest.mark.parametrize("name", ["dev", "heldout"])
@pytest.mark.parametrize("n", [11, 13])
def test_group_size_gate_covers_both_groups_and_both_directions(name, n):
    """条款 2 的百分比分母写死 GROUP_N=12, 两个组各是分子/分母的一侧 —— 只查 dev 会让
    heldout 漂移无人拦, 只查「变小」会让组**变大**无人拦 (finding F-02)。恒等判 `!=`,
    故两个方向各配一格。
    """
    after = after_runs()
    after[1]["summary"]["by_group"][name] = {"n": n, "exact": min(n, 12), "fatal": 0}
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


def test_distinct_git_revs_do_not_trigger_the_shared_warning(capsys):
    """告警的阴性对照: 两批 sha 不同 ⇒ 不告警。

    交集写成并集后, 只要两批各自有版本号告警就恒响 —— 而一条恒响的告警等于没有告警,
    它正是 I-2 (拷贝错文件) 的弱形态探测器 (finding F-11)。
    """
    base = [mk_run(i, fatal=10, dist_fatal=2, u1_fatal=1, dev=6, gen="base", git_rev="aaa1111")
            for i in (1, 2, 3)]
    verdict(base, [mk_run(i, gen="after", git_rev="bbb2222") for i in (1, 2, 3)])
    assert "共用 git_rev" not in capsys.readouterr().out


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
