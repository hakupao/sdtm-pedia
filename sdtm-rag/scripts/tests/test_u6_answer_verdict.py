"""eval/u6_answer_verdict.py 单测 — 全合成 fixture (spec §4.3: 修订后判定脚本不许沿用
旧脚本原样重测, 合成 fixture 测试先行).

每条判据的两半都单独钉死: 支配的 cost/gain 两向 · E4 并集的两臂 · divergent 的两种符号
· 结论词的三条抑制路径 · 四道产物闸的逐遍覆盖.
"""
import json

import pytest

from eval.u5_verdict import EXPECTED_N, I1_MIN_SAME_RATE
from eval.u6_answer_verdict import (
    CHEAP_WORD,
    E4_MAX_UNION,
    compare_arms,
    main,
    verdict_rc,
)


def mk_answer_run(scores: dict, n: int | None = None, judge_model: str = "stub-judge") -> dict:
    """scores: id -> float (judge 分) | None (parse 失败). n 缺省 = 计分行数."""
    return {"summary": {"n_questions": len(scores) if n is None else n,
                        "judge_model": judge_model},
            "results": [{"id": i, "judge_fact_recall": (s if s is not None else 0.0),
                         "judge_parse_ok": s is not None} for i, s in scores.items()]}


def runs(*score_maps, **kw):
    """每 map = 一遍; None = parse fail."""
    return [mk_answer_run(m, **kw) for m in score_maps]


def _same(scores: dict):
    """三遍同分的一臂, 题量 = 行数 (小合成集; 调用方以 expected_n 覆盖家族题量)."""
    return runs(scores, scores, scores)


def _pad(scores: dict, fam: str) -> dict:
    """补足到 EXPECTED_N[fam] 行. 填充题两臂同为 1.0 —— 对 cost/gain 与稳定性计数皆中性,
    只为满足行数闸 (沿 U5 测试的 _pad)."""
    out = dict(scores)
    i = 0
    while len(out) < EXPECTED_N[fam]:
        out.setdefault(f"_pad{i}", 1.0)
        i += 1
    return out


def _flat(scores: dict, fam: str = "cards"):
    """三遍同分且行数补满家族题量的一臂 (走家族默认分母的 fixture 用)."""
    padded = _pad(scores, fam)
    return runs(padded, padded, padded, n=EXPECTED_N[fam])


def _unstable_arm(flip_ids, steady_ids, fam="cards"):
    """本臂三遍: flip_ids 中间一遍翻分 (→不稳定), steady_ids 恒定 (→稳定)."""
    base = {i: 1.0 for i in [*flip_ids, *steady_ids]}
    flip = {**base, **{i: 0.0 for i in flip_ids}}
    return runs(base, flip, base, n=EXPECTED_N[fam])


def _write(tmp_path, name: str, obj) -> str:
    p = tmp_path / f"{name}.json"
    p.write_text(json.dumps(obj), encoding="utf-8")
    return str(p)


def _argv(tmp_path, arm_a, arm_b, family="cards", expected_n=None, probe=None, out="v"):
    argv = ["--arm-a", *[_write(tmp_path, f"{out}_a{i}", r) for i, r in enumerate(arm_a)],
            "--arm-b", *[_write(tmp_path, f"{out}_b{i}", r) for i, r in enumerate(arm_b)],
            "--family", family, "--output", str(tmp_path / f"{out}.json")]
    if expected_n is not None:
        argv += ["--expected-n", str(expected_n)]
    if probe is not None:
        argv += ["--probe", _write(tmp_path, f"{out}_probe", probe)]
    return argv


# ── 冻结判据 ───────────────────────────────────────────────────────────────

def test_frozen_thresholds_are_literal():
    """spec §4.3 冻结: 阈值被改必须有人看见 (测试 import 常量 ⇒ 常量自身无守卫)."""
    assert E4_MAX_UNION == {"cards": 9, "docs": 6}          # = 20% of 48 / 30
    assert I1_MIN_SAME_RATE == 0.95
    # 词面自带池限定 (U5 §9-1): 判词被单独摘出来引用时也不会读成"整体便宜"
    assert CHEAP_WORD == "cheap_on_this_ruler_comparable_pool"


def test_verdict_archives_the_thresholds_it_judged_by():
    """产物必须自带判据: 阈值只活在代码里的话, 归档 json 事后无法自证按什么判的."""
    a = _same({"q1": 1.0})
    out = compare_arms(a, a, n_scored=1, family="cards", expected_n=1)
    assert out["thresholds"] == {"E4_union_max": E4_MAX_UNION,
                                 "I1_min_same_rate": I1_MIN_SAME_RATE}


# ── E1: 稳定半 (沿 U5) ∪ 支配题 ────────────────────────────────────────────

def test_dominance_unstable_but_robust_counts_as_cost():
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 0.9, "q2": 1.0})
    b = runs({"q1": 0.5, "q2": 1.0}, {"q1": 0.6, "q2": 1.0}, {"q1": 0.4, "q2": 1.0})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    assert "q1" in out["E1"]["confirmed_cost_ids"] and "q1" in out["E1"]["dominance_ids"]


def test_dominance_amount_is_the_three_run_mean_gap():
    """支配题额 = 三遍均值差 (不是最坏界差 0.3, 也不是首遍差 0.5) —— 三者在此 fixture
    上各不相同, 换成任一种都必须红."""
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 0.9, "q2": 1.0})
    b = runs({"q1": 0.5, "q2": 1.0}, {"q1": 0.6, "q2": 1.0}, {"q1": 0.4, "q2": 1.0})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    gap = (1.0 + 1.0 + 0.9) / 3 - (0.5 + 0.6 + 0.4) / 3
    assert out["E1"]["confirmed_cost_pt"] == round(100 * gap / 2, 2)
    assert out["E1"]["confirmed_gain_ids"] == []


def test_dominance_is_two_sided_swap_flips_cost_and_gain():
    """对调型守卫: 两臂对调后, 同一题必须从代价变成收益 (集合断言的系统性盲区)."""
    a = runs({"q1": 1.0}, {"q1": 1.0}, {"q1": 0.9})
    b = runs({"q1": 0.5}, {"q1": 0.6}, {"q1": 0.4})
    cost_side = compare_arms(a, b, n_scored=1, family="cards", expected_n=1)["E1"]
    gain_side = compare_arms(b, a, n_scored=1, family="cards", expected_n=1)["E1"]
    assert cost_side["confirmed_cost_ids"] == gain_side["confirmed_gain_ids"] == ["q1"]
    assert cost_side["confirmed_gain_ids"] == gain_side["confirmed_cost_ids"] == []
    # 额是绝对值口径: 收益方向不得落成负数
    assert gain_side["confirmed_gain_pt"] == cost_side["confirmed_cost_pt"] > 0


@pytest.mark.parametrize(("b_hi", "expect_cost"), [(0.9, False), (0.8999, True)])
def test_dominance_boundary_is_strict(b_hi, expect_cost):
    """`max(B) < min(A)` 是严格小于: 两臂区间贴边相等不算支配 —— 松成 <= 会把
    "最好值恰等于对臂最差值"的题也判成已确证代价."""
    a = runs({"q1": 1.0}, {"q1": 1.0}, {"q1": 0.9})
    b = runs({"q1": b_hi}, {"q1": 0.5}, {"q1": 0.4})
    out = compare_arms(a, b, n_scored=1, family="cards", expected_n=1)
    assert (out["E1"]["confirmed_cost_ids"] == ["q1"]) is expect_cost
    assert (out["E1"]["dominance_ids"] == ["q1"]) is expect_cost


def test_dominance_requires_all_six_values_parse_ok():
    """六值有一个 parse 失败 ⇒ 该题不进支配 (兜底 0.0 不可信, 区间无意义). 数据与
    test_dominance_unstable_but_robust_counts_as_cost 只差 B 第三遍那一格."""
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 0.9, "q2": 1.0})
    b = runs({"q1": 0.5, "q2": 1.0}, {"q1": 0.6, "q2": 1.0}, {"q1": None, "q2": 1.0})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    assert out["E1"]["confirmed_cost_ids"] == [] and out["E1"]["dominance_ids"] == []
    assert "q1" in out["E4"]["union"]


def test_stable_half_still_counts_and_is_reported_separately():
    """U5 的稳定半口径原样保留 (本件只在其上并入支配题), 且 stable_half 子块单独归档
    —— 判词有多少压在最坏界尺子上, 读者要能拆开看 (U5 §9-1)."""
    a = _flat({"q1": 1.0, "q2": 1.0})
    b = _flat({"q1": 0.5, "q2": 1.0})
    out = compare_arms(a, b, n_scored=EXPECTED_N["cards"], family="cards")
    assert out["E1"]["confirmed_cost_ids"] == ["q1"]
    assert out["E1"]["stable_half"]["confirmed_cost_ids"] == ["q1"]
    assert out["E1"]["stable_half"]["confirmed_cost_pt"] == round(100 * 0.5 / 48, 2)
    assert out["E1"]["stable_half"]["n_compared"] == EXPECTED_N["cards"]
    assert out["E1"]["dominance_only_ids"] == []        # 稳定半已收的题不算支配额外带进来的


def test_stable_half_carries_a_caliber_marker():
    """stable_half 与顶层 E1 同名同形 (confirmed_cost_ids 等) = C1 型双口径误读隐患:
    单独摘出这块引用会把有代价的批次读成"无代价". 标记键把"这只是 U5 稳定半子集"
    钉在数据里, 不靠读者记性 —— 判词与代价额只引顶层 E1."""
    a = runs({"q1": 1.0}, {"q1": 1.0}, {"q1": 0.9})     # 仅支配纳入, 稳定半为空
    b = runs({"q1": 0.5}, {"q1": 0.6}, {"q1": 0.4})
    out = compare_arms(a, b, n_scored=1, family="cards", expected_n=1)
    assert out["E1"]["stable_half"]["caliber"] == "u5_stable_only_subset"
    # 正是这一格能骗人: 子块说"无代价", 顶层 E1 说有 —— 两者都为真, 口径不同
    assert out["E1"]["stable_half"]["confirmed_cost_ids"] == []
    assert out["E1"]["confirmed_cost_ids"] == ["q1"]
    assert out["verdict_word"] == "cost_reported"


def test_dominance_only_ids_names_what_the_worst_bound_ruler_added():
    """dominance_only_ids = 支配纳入里稳定半没收的那些. 它若和 dominance_ids 混成一格,
    读者无从知道判词的哪部分靠最坏界 (q2 两侧都稳定也满足支配, 不该算"额外")."""
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 0.9, "q2": 1.0})
    b = runs({"q1": 0.5, "q2": 0.5}, {"q1": 0.6, "q2": 0.5}, {"q1": 0.4, "q2": 0.5})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    assert out["E1"]["confirmed_cost_ids"] == ["q1", "q2"]
    assert out["E1"]["dominance_ids"] == ["q1", "q2"]
    assert out["E1"]["dominance_only_ids"] == ["q1"]


def test_e1_counts_the_all_parse_ok_pool_it_could_dominate_over():
    """n_all_parse_ok 是支配尺子的可比池分母 —— 判词的"可比池"限定要有数字支撑."""
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": None})
    b = _same({"q1": 1.0, "q2": 1.0})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    assert out["E1"]["n_all_parse_ok"] == 1


def test_e1_id_lists_are_deterministically_sorted():
    """去掉 sorted 的变异只在某些 hash seed 下才红 —— 用 12 题把这条钉成确定性的."""
    ids = [f"z{i:02d}" for i in range(12)]
    a = _flat({i: 1.0 for i in ids})
    b = _flat({i: 0.5 for i in ids})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["E1"]["confirmed_cost_ids"] == sorted(ids)
    assert out["E1"]["dominance_ids"] == sorted(ids)


# ── E4: 跨臂并集闸 ─────────────────────────────────────────────────────────

def test_e4_union_gate_trips(tmp_path):
    ids = [f"q{i:02d}" for i in range(48)]
    a = _unstable_arm(ids[:10], ids[10:])            # 10 题不稳定 (>9)
    b = _flat({i: 1.0 for i in ids})
    out = compare_arms(a, b, n_scored=48, family="cards")
    rc = main(_argv(tmp_path, a, b, family="cards"))
    assert not out["E4"]["gate_pass"]
    assert out["E4"]["n_union"] == 10 and out["E4"]["max"] == 9
    assert rc == 2 and verdict_rc(out) == 2
    # 闸响 ⇒ 不下结论词 (spec §4.3)
    assert out["verdict_word"] is None
    assert out["verdict_suppressed_by"] == ["E4_union_gate"]
    assert "cheap" not in json.dumps(out)


@pytest.mark.parametrize(("fam", "n_unstable", "expect_pass"),
                         [("cards", 9, True), ("cards", 10, False),
                          ("docs", 6, True), ("docs", 7, False)])
def test_e4_threshold_boundary_per_family(fam, n_unstable, expect_pass):
    """两族阈值各自钉边界: 查表写死成 cards(9) 或只判一族, 单族 fixture 全绿."""
    ids = [f"q{i:02d}" for i in range(EXPECTED_N[fam])]
    a = _unstable_arm(ids[:n_unstable], ids[n_unstable:], fam)
    b = _flat({i: 1.0 for i in ids}, fam)
    out = compare_arms(a, b, n_scored=EXPECTED_N[fam], family=fam)
    assert out["E4"]["n_union"] == n_unstable
    assert out["E4"]["gate_pass"] is expect_pass
    assert verdict_rc(out) == (0 if expect_pass else 2)


def test_e4_union_deduplicates_overlapping_ids_at_the_gate_boundary():
    """并集是**集合**并, 不是两臂清单相加: 同一题两臂都不稳定只占一格.

    构造刻意落在闸边界上 —— A 不稳定 7 题 (q00-q06), B 不稳定 4 题 (q05-q08), 重叠 2 题:
    去重后 9 = 闸值 ⇒ PASS; 按 concat 双计是 11 > 9 ⇒ 假触发不可判。
    `sorted(unstable_a + unstable_b)` 这条变异在"两臂不稳定题互斥或单臂"的 fixture 上
    全绿, 只有重叠 + 边界这一格能杀它 (审查方检出)。
    """
    ids = [f"q{i:02d}" for i in range(48)]
    a = _unstable_arm(ids[:7], ids[7:])
    b = _unstable_arm(ids[5:9], [*ids[:5], *ids[9:]])
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert len(out["E4"]["unstable_a"]) == 7 and len(out["E4"]["unstable_b"]) == 4
    assert out["E4"]["union"] == sorted(ids[:9])
    assert out["E4"]["n_union"] == 9                 # 拼接求和会是 11
    assert out["E4"]["n_union"] < len(out["E4"]["unstable_a"]) + len(out["E4"]["unstable_b"])
    assert out["E4"]["gate_pass"] is True            # 恰在闸值上; 双计会假触发成 False
    assert verdict_rc(out) == 0 and out["verdict_word"] is not None


def test_e4_is_a_union_not_a_per_arm_check():
    """两臂各 5 题不稳定且互不相同 ⇒ 并集 10 > 9 触发, 而任一臂单看都 ≤ 9. 并集改成
    max(单臂) / 交集 / 只看某一臂 —— 三种改法在"两臂同不稳定题"的 fixture 上全绿."""
    ids = [f"q{i:02d}" for i in range(48)]
    a = _unstable_arm(ids[:5], ids[5:])
    b = _unstable_arm(ids[5:10], [*ids[:5], *ids[10:]])
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["E4"]["unstable_a"] == sorted(ids[:5])
    assert out["E4"]["unstable_b"] == sorted(ids[5:10])
    assert out["E4"]["union"] == sorted(ids[:10])
    assert out["E4"]["gate_pass"] is False


# ── divergent_readings ────────────────────────────────────────────────────

def _divergent_arms():
    """配对净额为正 (q_gain 两侧稳定, +0.5) 而全池均值差为负 (d1-d3 各 -0.3, 但 A 侧
    档内不稳定且两臂区间重叠 ⇒ 既非稳定半也非支配, 进不了 E1)."""
    a_maps: list[dict] = [{"q_gain": 0.5}, {"q_gain": 0.5}, {"q_gain": 0.5}]
    b_maps: list[dict] = [{"q_gain": 1.0}, {"q_gain": 1.0}, {"q_gain": 1.0}]
    for d in ("d1", "d2", "d3"):
        for m, v in zip(a_maps, (1.0, 1.0, 0.4), strict=True):
            m[d] = v                       # mean 0.8, min 0.4 — 不稳定
        for m in b_maps:
            m[d] = 0.5                     # mean 0.5, max 0.5 > min(A)=0.4 — 不支配
    return runs(*a_maps), runs(*b_maps)


def test_divergent_readings_flag():
    a, b = _divergent_arms()
    out = compare_arms(a, b, n_scored=4, family="cards", expected_n=4)
    assert out["divergent_readings"] is True
    # 两个读数都必须落盘 (spec §4.3: verdict 同时落盘聚合均值差与配对净额)
    assert out["paired_net_pt"] == round(100 * 0.5 / 4, 2)                  # +12.5
    assert out["aggregate_mean_diff_pt"] == round(100 * (0.5 - 0.9) / 4, 2)  # -10.0
    assert out["aggregate_n"] == 4
    assert out["E1"]["confirmed_cost_ids"] == [] and out["E1"]["confirmed_gain_ids"] == ["q_gain"]


def test_divergent_false_when_both_readings_agree():
    a = _flat({"q1": 1.0, "q2": 1.0})
    b = _flat({"q1": 0.5, "q2": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["paired_net_pt"] < 0 and out["aggregate_mean_diff_pt"] < 0
    assert out["divergent_readings"] is False


def test_divergent_false_when_one_reading_is_zero():
    """"符号相反"要求两个读数都非 0: 一边为 0 不是分歧, 是那把尺子没读到信号.
    条件从 and 松成 or / 去掉非 0 判 —— 这里必须红."""
    ids = [f"q{i:02d}" for i in range(48)]
    a = _unstable_arm(ids[:2], ids[2:])       # 只有不稳定, 无任何已确证分差
    b = _flat({i: 1.0 for i in ids})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["paired_net_pt"] == 0.0
    assert out["aggregate_mean_diff_pt"] != 0.0
    assert out["divergent_readings"] is False


def test_aggregate_excludes_questions_with_any_parse_failure():
    """聚合读数只含双臂全 parse_ok 题: 兜底 0.0 混进均值会把 parse 失败读成"答错"."""
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": None})
    b = _same({"q1": 0.5, "q2": 1.0})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    assert out["aggregate_n"] == 1                                   # q2 被排除
    assert out["aggregate_mean_diff_pt"] == round(100 * (0.5 - 1.0), 2)


def test_aggregate_is_b_minus_a_oriented_like_paired_net():
    """两个读数必须同向 (B−A, 正 = 修法更好), 否则 divergent 判据恒真/恒假."""
    a = _flat({"q1": 0.5})
    b = _flat({"q1": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["aggregate_mean_diff_pt"] > 0 and out["paired_net_pt"] > 0


# ── I-1 抑制与结论词 ───────────────────────────────────────────────────────

def test_i1_fail_suppresses_verdict_word():
    a = _same({"q1": 1.0, "q2": 1.0})
    b = _same({"q1": 1.0, "q2": 1.0})
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2,
                       probe={"same_rate": 0.5, "n": 9, "n_orig_parse_fail": 0})
    assert out["verdict_word"] == "advisory_no_verdict"
    assert "cheap" not in json.dumps(out)


@pytest.mark.parametrize(("same_rate", "expect_pass"), [(0.95, True), (0.9499, False)])
def test_i1_threshold_boundary(same_rate, expect_pass):
    a = _flat({"q1": 1.0})
    out = compare_arms(a, a, n_scored=48, family="cards",
                       probe={"same_rate": same_rate, "n": 48, "n_orig_parse_fail": 0})
    assert out["I1"]["pass"] is expect_pass
    assert out["verdict_word"] == (CHEAP_WORD if expect_pass else "advisory_no_verdict")


def test_i1_records_denominator_and_parse_fail():
    """same_rate 单看无意义 —— 分母与被排除行数必须同落盘 (U5 审查 M2)."""
    a = _flat({"q1": 1.0})
    out = compare_arms(a, a, n_scored=48, family="cards",
                       probe={"same_rate": 1.0, "n": 46, "n_orig_parse_fail": 2})
    assert out["I1"] == {"same_rate": 1.0, "n": 46, "n_orig_parse_fail": 2, "pass": True}


def test_no_probe_means_no_i1_block_and_no_suppression():
    a = _flat({"q1": 1.0})
    out = compare_arms(a, a, n_scored=48, family="cards")
    assert out["I1"] is None and out["verdict_suppressed_by"] == []
    assert out["verdict_word"] == CHEAP_WORD


def test_probe_n_zero_is_rejected():
    """rejudge_run 在 scored 为空时吐 same_rate=0.0 —— 那是无意义值, 不是 I1 失守."""
    a = _flat({"q1": 1.0})
    with pytest.raises(SystemExit):
        compare_arms(a, a, n_scored=48, family="cards",
                     probe={"same_rate": 0.0, "n": 0, "n_orig_parse_fail": 48})


def test_probe_missing_parse_fail_count_raises():
    """缺 n_orig_parse_fail 必须炸, 不能静默落 None 进归档 (U5 复审 LOW)."""
    a = _flat({"q1": 1.0})
    with pytest.raises(KeyError):
        compare_arms(a, a, n_scored=48, family="cards", probe={"same_rate": 1.0, "n": 48})


def test_verdict_word_cost_reported_when_cost_ids_non_empty():
    a = _flat({"q1": 1.0, "q2": 1.0})
    b = _flat({"q1": 0.5, "q2": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["verdict_word"] == "cost_reported"


def test_cost_reported_even_when_pt_rounds_to_zero():
    """判 cheap 的依据是"已确证代价集合为空", 不是 pt 读数 —— 否则产物自相矛盾
    (cost_ids 非空却判 cheap; U5 审查 M1)."""
    a = _flat({"q1": 1.0, "q2": 1.0})
    b = _flat({"q1": 0.999, "q2": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["E1"]["confirmed_cost_pt"] == 0.0
    assert out["E1"]["confirmed_cost_ids"] == ["q1"]
    assert out["verdict_word"] == "cost_reported"


def test_cheap_rests_on_an_empty_cost_set_not_on_a_non_negative_net():
    """一题赔 0.5 + 一题赚 0.5 ⇒ 净额 0 而代价集合非空, 判词必须是 cost_reported.
    判据若改看净额 (变异 M24), "赔一题赚一题"会被读成"没代价" —— 这正是 U5 §9-1
    要防的读法: cheap 说的是可比池里没有已确证代价, 不是收支相抵."""
    a = _flat({"q1": 1.0, "q2": 0.5})
    b = _flat({"q1": 0.5, "q2": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["paired_net_pt"] == 0.0
    assert out["E1"]["confirmed_cost_ids"] == ["q1"]
    assert out["E1"]["confirmed_gain_ids"] == ["q2"]
    assert out["verdict_word"] == "cost_reported"


def test_pt_denominator_is_n_scored_not_expected_n():
    """两个入参各管一件事: expected_n 是产物闸的行数期望, n_scored 是 pt 分母.
    合成 fixture 里二者常相等, 混用当场看不出来 (变异 M40) —— 这里刻意拆开."""
    a = _same({"q1": 1.0, "q2": 1.0})
    b = _same({"q1": 0.5, "q2": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards", expected_n=2)
    assert out["n_scored"] == 48 and out["expected_n"] == 2
    assert out["E1"]["confirmed_cost_pt"] == round(100 * 0.5 / 48, 2)
    assert out["E1"]["stable_half"]["confirmed_cost_pt"] == round(100 * 0.5 / 48, 2)


def test_gain_alone_still_reads_cheap_on_the_comparable_pool():
    """只有收益没有代价 = 判词仍是 cheap (代价集合空); 判词若改看 net 就会在这里翻面."""
    a = _flat({"q1": 0.5})
    b = _flat({"q1": 1.0})
    out = compare_arms(a, b, n_scored=48, family="cards")
    assert out["E1"]["confirmed_gain_ids"] == ["q1"] and out["E1"]["confirmed_cost_ids"] == []
    assert out["verdict_word"] == CHEAP_WORD


def test_e4_trip_outranks_i1_and_both_reasons_are_recorded():
    """两条抑制路径同时触发: 结论词按更强的那条 (E4 → 无词), 但两个理由都要留痕."""
    ids = [f"q{i:02d}" for i in range(48)]
    a = _unstable_arm(ids[:10], ids[10:])
    b = _flat({i: 1.0 for i in ids})
    out = compare_arms(a, b, n_scored=48, family="cards",
                       probe={"same_rate": 0.5, "n": 48, "n_orig_parse_fail": 0})
    assert out["verdict_word"] is None
    assert out["verdict_suppressed_by"] == ["E4_union_gate", "I1_rejudge"]


# ── 产物闸 (沿 U5 的四道): 仪器坏了必须炸, 不许静默误诊 ────────────────────

def test_rejects_arm_without_three_runs():
    a = _flat({"q1": 1.0})
    with pytest.raises(SystemExit):
        compare_arms(a[:2], a, n_scored=48, family="cards")
    with pytest.raises(SystemExit):
        compare_arms(a, a[:2], n_scored=48, family="cards")


@pytest.mark.parametrize("bad_idx", [0, 1, 2])
def test_rejects_wrong_n_questions_in_any_run(bad_idx):
    """三道产物闸逐遍跑; 只验首遍的变异在"三遍同一份"的 fixture 上全绿 (U5 复审)."""
    good = mk_answer_run({f"q{i:02d}": 1.0 for i in range(48)}, n=48)
    bad = json.loads(json.dumps(good))
    bad["summary"]["n_questions"] = 47
    trio = [good, good, good]
    trio[bad_idx] = bad
    with pytest.raises(SystemExit):
        compare_arms(trio, [good] * 3, n_scored=48, family="cards")


def test_rejects_row_count_mismatch():
    """表头 n_questions 对但实际计分行数不对 = 产物残缺 (U5 审查 M3). 两臂同样残缺 ——
    只让一臂短的话, 跨臂题集闸会先炸, 行数闸删掉也照样红 (变异 M34)."""
    short = mk_answer_run({"q1": 1.0}, n=48)
    with pytest.raises(SystemExit):
        compare_arms([short] * 3, [short] * 3, n_scored=48, family="cards")


def test_rejects_run_without_judge():
    """漏 --judge 的 run 全行无 judge_parse_ok → 会被读成全不稳定 → 误诊 (U5 审查 M4)."""
    a = _flat({"q1": 1.0})
    bad = json.loads(json.dumps(a[0]))
    del bad["summary"]["judge_model"]
    with pytest.raises(SystemExit):
        compare_arms([bad, a[1], a[2]], a, n_scored=48, family="cards")


def test_rejects_mismatched_question_sets_within_an_arm():
    r1 = mk_answer_run({"q1": 1.0})
    r2 = mk_answer_run({"q2": 1.0})
    with pytest.raises(SystemExit):
        compare_arms([r1, r2, r1], [r1] * 3, n_scored=1, family="cards", expected_n=1)


def test_rejects_mismatched_question_sets_across_arms():
    """两臂题集不同 = 拿两把尺子相减: 支配与聚合都会静默只算交集, 判词照出."""
    a = _same({"q1": 1.0, "q2": 1.0})
    b = _same({"q1": 1.0, "q3": 1.0})
    with pytest.raises(SystemExit):
        compare_arms(a, b, n_scored=2, family="cards", expected_n=2)


def test_rejects_unknown_family():
    a = _flat({"q1": 1.0})
    with pytest.raises(SystemExit):
        compare_arms(a, a, n_scored=48, family="jp")


# ── CLI ───────────────────────────────────────────────────────────────────

def test_main_happy_writes_output_and_returns_zero(tmp_path):
    ids = [f"q{i:02d}" for i in range(48)]
    a = _flat({i: 1.0 for i in ids})
    assert main(_argv(tmp_path, a, a, family="cards")) == 0
    v = json.loads((tmp_path / "v.json").read_text(encoding="utf-8"))
    assert v["verdict_word"] == CHEAP_WORD
    assert v["family"] == "cards" and v["n_scored"] == 48 and v["expected_n"] == 48


def test_main_binds_arm_identity(tmp_path):
    """A/B 两臂在 main 里对调 = 代价与收益整体翻面 (对调型); 两臂同分的 fixture 照不出来."""
    a = _flat({"q1": 1.0, "q2": 1.0})
    b = _flat({"q1": 0.5, "q2": 1.0})
    assert main(_argv(tmp_path, a, b, family="cards")) == 0
    v = json.loads((tmp_path / "v.json").read_text(encoding="utf-8"))
    assert v["E1"]["confirmed_cost_ids"] == ["q1"] and v["E1"]["confirmed_gain_ids"] == []
    assert main(_argv(tmp_path, b, a, family="cards", out="w")) == 0
    w = json.loads((tmp_path / "w.json").read_text(encoding="utf-8"))
    assert w["E1"]["confirmed_gain_ids"] == ["q1"] and w["E1"]["confirmed_cost_ids"] == []


def test_main_expected_n_override_also_moves_the_pt_denominator(tmp_path):
    a = _same({"q1": 1.0, "q2": 1.0})
    b = _same({"q1": 0.5, "q2": 1.0})
    assert main(_argv(tmp_path, a, b, family="cards", expected_n=2)) == 0
    v = json.loads((tmp_path / "v.json").read_text(encoding="utf-8"))
    assert v["expected_n"] == 2 and v["n_scored"] == 2
    assert v["E1"]["confirmed_cost_pt"] == round(100 * 0.5 / 2, 2)


def test_main_wires_the_probe(tmp_path):
    a = _flat({"q1": 1.0})
    argv = _argv(tmp_path, a, a, family="cards",
                 probe={"same_rate": 0.5, "n": 48, "n_orig_parse_fail": 0})
    assert main(argv) == 0                       # I-1 不改 rc (spec §4.3 出口口径)
    v = json.loads((tmp_path / "v.json").read_text(encoding="utf-8"))
    assert v["verdict_word"] == "advisory_no_verdict" and v["I1"]["pass"] is False


def test_main_requires_exactly_three_runs_per_arm(tmp_path):
    a = _flat({"q1": 1.0})
    argv = _argv(tmp_path, a, a, family="cards")
    del argv[argv.index("--arm-a") + 1]
    with pytest.raises(SystemExit):
        main(argv)


def test_main_rejects_unknown_family(tmp_path):
    a = _flat({"q1": 1.0})
    argv = _argv(tmp_path, a, a, family="cards")
    argv[argv.index("--family") + 1] = "jp"
    with pytest.raises(SystemExit):
        main(argv)


def test_main_prints_the_verdict_and_rc(tmp_path, capsys):
    """rc 给跑批脚本读, 终端回显给人读 —— 两条出口都得钉住."""
    ids = [f"q{i:02d}" for i in range(48)]
    a = _unstable_arm(ids[:10], ids[10:])
    b = _flat({i: 1.0 for i in ids})
    assert main(_argv(tmp_path, a, b, family="cards")) == 2
    out = capsys.readouterr().out
    assert "gate_pass=False" in out
    assert "verdict_word=None" in out and "rc=2" in out


def test_output_carries_zero_question_text(tmp_path, capsys):
    """红线: run json 的 results 行里带 question, 判定产物是要进 checkpoint 的 ——
    两者之间这道过滤只有这一层. 产物里只许有 id 与数字.

    落盘文件与 stdout **两路都要钉**: 终端回显常被整段贴进 checkpoint, 只钉文件的话
    print 里多带一个题面字段就悄悄泄漏 (审查方检出)."""
    secret = "WHAT IS THE PERMISSIBLE VALUE OF AESEV"
    a = _flat({"q1": 1.0, "q2": 1.0})
    b = _flat({"q1": 0.5, "q2": 1.0})
    for arm in (a, b):
        for r in arm:
            for row in r["results"]:
                row["question"] = secret
                row["answer"] = secret
    assert main(_argv(tmp_path, a, b, family="cards")) == 0
    dumped = (tmp_path / "v.json").read_text(encoding="utf-8")
    assert secret not in dumped and "question" not in dumped and "answer" not in dumped
    printed = capsys.readouterr().out
    assert secret not in printed
    assert "question" not in printed and "answer" not in printed
