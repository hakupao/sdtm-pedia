"""稳定性统计的口径。构造已知的多次运行结果, 验统计正确。"""
from eval.jitter_probe import min_adjacent_gap, pair_margins, stability_report


def test_all_runs_identical():
    runs = [["a", "b", "c"]] * 4
    r = stability_report(runs)
    assert r["n_runs"] == 4
    assert r["distinct_sets"] == 1
    assert r["distinct_orders"] == 1
    assert r["stable_prefix"] == 3
    assert r["always"] == 3
    assert r["sometimes"] == 0


def test_tail_swap_same_set():
    """成分相同、顺序不同 —— 集合数 1 但顺序数 2。"""
    runs = [["a", "b", "c"], ["a", "c", "b"]]
    r = stability_report(runs)
    assert r["distinct_sets"] == 1
    assert r["distinct_orders"] == 2
    assert r["stable_prefix"] == 1
    assert r["sometimes"] == 0


def test_membership_churn():
    runs = [["a", "b", "c"], ["a", "b", "d"]]
    r = stability_report(runs)
    assert r["distinct_sets"] == 2
    assert r["stable_prefix"] == 2
    assert r["always"] == 2      # a, b
    assert r["sometimes"] == 2   # c, d


def test_identifiers_must_be_distinguishable():
    """探针自身的护栏: 全同标识说明标识选错了 (控制器踩过 —— 63 个 spec.md#DOMAIN
    塌缩成 1 个 key, 探针于是假装稳定)。"""
    import pytest
    with pytest.raises(ValueError, match="indistinguishable"):
        stability_report([["x", "x", "x"], ["x", "x", "x"]])


# ---- brief 之外补的两项 (探针自己也要被测: 这两个函数产出的数字会进证据) ----


def test_min_adjacent_gap():
    assert round(min_adjacent_gap([0.9, 0.8, 0.79]), 6) == 0.01   # 取最小的那一对
    assert min_adjacent_gap([0.5, 0.5]) == 0.0    # 全精度并列
    assert min_adjacent_gap([0.5]) is None        # 不足一对


def test_pair_margins_detects_real_flip():
    """第 2 次运行里 b 反超 a —— 该对必须被记成 flipped, min_margin 为负。"""
    orders = [["a", "b"], ["b", "a"]]
    sims = [{"a": 0.50, "b": 0.49}, {"a": 0.49, "b": 0.50}]
    m = pair_margins(orders, sims)
    assert m["n_flipped_pairs"] == 1
    assert m["pairs"][0]["flipped"] is True
    assert m["min_margin"] < 0


def test_pair_margins_absolute_drift_vs_differential_drift():
    """同向平移: 两条 sim 各漂 0.01, 但**差值**纹丝不动 —— 顺序不受影响。
    只拿绝对漂移和间隔比大小会高估翻转风险, 这个用例锁住这个区别。"""
    orders = [["a", "b"], ["a", "b"]]
    sims = [{"a": 0.50, "b": 0.499}, {"a": 0.51, "b": 0.509}]
    m = pair_margins(orders, sims)
    assert m["n_flipped_pairs"] == 0
    assert round(m["max_abs_sim_drift"], 6) == 0.01      # 单值漂 0.01
    assert round(m["max_pair_diff_drift"], 6) == 0.0     # 差值不漂
    assert m["tied_pairs"] == 0
