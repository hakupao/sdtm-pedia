"""池深度不变性判据的口径。构造已知的进程结果, 验聚合与 verdict 正确。

重点在**判据本身不能说谎**: A/B 有差异但 A/A 同样有差异时, 不许把差异归给池深度。
"""
import pytest

from eval.pool_depth_probe import (
    AA_PAIRS,
    AB_PAIRS,
    aggregate,
    compact_raw,
    cross_process_stability,
    expand_raw,
    pair_stats,
    positional_diff,
    verdict,
)


def test_positional_diff_identical():
    assert positional_diff(["a", "b", "c"], ["a", "b", "c"]) == 0


def test_positional_diff_same_set_different_order():
    """集合相同、顺序不同仍算差异 —— 顺序变了, 下游 context 就是另一份输入。"""
    assert positional_diff(["a", "b", "c"], ["a", "c", "b"]) == 2


def test_positional_diff_length_mismatch_counts_missing_seats():
    assert positional_diff(["a", "b", "c"], ["a"]) == 2


def test_pair_stats_counts_only_mismatched_pairs():
    seqs = [["a"], ["a"], ["b"], ["a"]]
    r = pair_stats(seqs, [(0, 1), (0, 2)])
    assert r["n_pairs"] == 2
    assert r["n_mismatched"] == 1
    assert r["max_positional_diff"] == 1


def test_cross_process_stability_rejects_collapsed_identifiers():
    """全部条目去重后只剩 1 种 = 标识选错了, 探针会假装稳定, 必须抛。"""
    with pytest.raises(ValueError, match="indistinguishable"):
        cross_process_stability([["spec.md"], ["spec.md"]])


def test_cross_process_stability_counts_orders_and_sets():
    r = cross_process_stability([["a", "b"], ["b", "a"], ["a", "c"]])
    assert r["n_runs"] == 3
    assert r["distinct_orders"] == 3
    assert r["distinct_sets"] == 2
    assert r["sometimes"] == 2  # b 与 c 都不是每次都在


def _row(qid, e2e, *, fuse30, fuse200, d30, ddeep, b30, bdeep,
         fuse_out_k=None, fuse_out_deep=None, e2e_deep_fuse=None):
    return {
        "id": qid, "e2e": e2e,
        "e2e_deep_fuse": e2e_deep_fuse if e2e_deep_fuse is not None else e2e[0],
        "fuse_out_k": fuse_out_k if fuse_out_k is not None else fuse30,
        "fuse_out_deep": fuse_out_deep if fuse_out_deep is not None else fuse30 + ["z"],
        "fuse_30": fuse30, "fuse_200": fuse200,
        "dense_30": d30, "dense_deep_head": ddeep,
        "bm25_30": b30, "bm25_deep_head": bdeep,
        "n_dense_deep": 200, "n_bm25_deep": 200,
    }


def _clean_row(qid="q1"):
    """一切都不变的理想题: 三条臂零差异。"""
    return _row(
        qid, [["a", "b"]] * 4,
        fuse30=["a", "b"], fuse200=["a", "b"],
        d30=["a", "b"], ddeep=["a", "b"], b30=["a", "b"], bdeep=["a", "b"],
    )


def test_verdict_true_when_nothing_moves():
    agg = aggregate([[_clean_row()], [_clean_row()]])
    v = agg["verdict"]
    assert v["POOL_DEEP_OK"] is True
    assert v["FUSE_OUT_DEEP_OK"] is True
    assert agg["e2e"]["ab"]["n_mismatched"] == 0


def test_verdict_false_when_pool_depth_moves_topk():
    """A/A 全同、A/B 有差 —— 差异只能归给池深度。"""
    row = _row(
        "q1", [["a", "b"], ["b", "a"], ["a", "b"], ["b", "a"]],
        fuse30=["a", "b"], fuse200=["b", "a"],
        d30=["a", "b"], ddeep=["a", "b"], b30=["a", "b"], bdeep=["a", "b"],
    )
    agg = aggregate([[row], [row]])
    assert agg["e2e"]["aa"]["n_mismatched"] == 0
    assert agg["e2e"]["ab"]["n_mismatched"] == len(AB_PAIRS) * 2
    assert agg["verdict"]["POOL_DEEP_OK"] is False
    assert agg["verdict"]["algebraic_ok"] is False


def test_ab_difference_not_blamed_on_pool_when_aa_differs_too():
    """本 task 的核心护栏: 同参数重跑 (A/A) 也不一致时, A/B 的不一致是抖动,
    不是池深度 —— e2e 这一维不许判 fail。"""
    # 四次调用两两不同, A/A 与 A/B 的不一致数按对数成比例
    row = _row(
        "q1", [["a", "b"], ["b", "a"], ["b", "a"], ["a", "b"]],
        fuse30=["a", "b"], fuse200=["a", "b"],
        d30=["a", "b"], ddeep=["a", "b"], b30=["a", "b"], bdeep=["a", "b"],
    )
    agg = aggregate([[row]])
    # AA 对 (0,2) (1,3) 都不同 -> 2; AB 对 (0,1)(2,3)(1,2)(0,3): 不同的是 (0,1)(2,3) -> 2
    assert agg["e2e"]["aa"]["n_mismatched"] == 2
    assert agg["e2e"]["ab"]["n_mismatched"] == 2
    assert agg["verdict"]["e2e_ok"] is True  # ab <= aa, 归给抖动
    assert agg["verdict"]["POOL_DEEP_OK"] is True  # 另两条臂干净


def test_candidate_prefix_arm_catches_depth_dependent_candidates():
    """_search(30) != _search(200)[:30] —— 候选列表本身依赖请求深度。"""
    row = _row(
        "q1", [["a", "b"]] * 4,
        fuse30=["a", "b"], fuse200=["a", "b"],
        d30=["a", "b"], ddeep=["a", "b"],
        b30=["a", "b"], bdeep=["a", "c"],
    )
    agg = aggregate([[row]])
    assert agg["candidate_prefix"]["mismatched"] == ["q1"]
    assert agg["verdict"]["POOL_DEEP_OK"] is False


def test_fuse_output_depth_arm_independent_of_pool_verdict():
    """放长融合输出改了前 k 名 -> FUSE_OUT_DEEP_OK 假, 但 POOL_DEEP_OK 不受牵连。"""
    row = _row(
        "q1", [["a", "b"]] * 4,
        fuse30=["a", "b"], fuse200=["a", "b"],
        d30=["a", "b"], ddeep=["a", "b"], b30=["a", "b"], bdeep=["a", "b"],
        fuse_out_k=["a", "b"], fuse_out_deep=["b", "a", "z"],
    )
    agg = aggregate([[row]])
    assert agg["verdict"]["POOL_DEEP_OK"] is True
    assert agg["verdict"]["FUSE_OUT_DEEP_OK"] is False
    assert agg["fuse_output_depth"]["min_fuse_candidates"] == 3


def test_fuse_output_depth_arm_catches_e2e_drift():
    """前 k 名一致但整条生产链 (S1 直查之后) 变了, 同样要判假。"""
    row = _row(
        "q1", [["a", "b"]] * 4,
        fuse30=["a", "b"], fuse200=["a", "b"],
        d30=["a", "b"], ddeep=["a", "b"], b30=["a", "b"], bdeep=["a", "b"],
        e2e_deep_fuse=["a", "c"],
    )
    agg = aggregate([[row]])
    assert agg["fuse_output_depth"]["n_mismatched_questions"] == 0
    assert agg["fuse_output_depth"]["e2e_mismatched"] == ["q1"]
    assert agg["verdict"]["FUSE_OUT_DEEP_OK"] is False


def test_aggregate_pairs_are_the_documented_ones():
    """配对定义是判据的一半, 改了就不再是 A/A vs A/B 对照 —— 钉住。"""
    assert AA_PAIRS == [(0, 2), (1, 3)]
    assert AB_PAIRS == [(0, 1), (2, 3), (1, 2), (0, 3)]


def test_compact_raw_round_trips():
    """折叠存盘不许丢信息 —— 还原后必须逐字节等于原始结果。"""
    a, b = _clean_row("q1"), _clean_row("q2")
    procs = [[a, b], [a, b], [a, b]]
    packed = compact_raw(procs)
    assert packed[1] == [{"id": "q1", "same_as_proc0": True},
                         {"id": "q2", "same_as_proc0": True}]
    assert expand_raw(packed) == procs


def test_compact_raw_keeps_differing_rows_verbatim():
    """差异行是要人肉核对的那些, 一条都不许折掉。"""
    a = _clean_row("q1")
    diff = _row("q1", [["x", "y"]] * 4,
                fuse30=["x"], fuse200=["x"], d30=["x"], ddeep=["x"],
                b30=["x"], bdeep=["x"])
    packed = compact_raw([[a], [diff]])
    assert packed[1][0] == diff
    assert expand_raw(packed) == [[a], [diff]]


def test_aggregate_accepts_expanded_raw():
    procs = [[_clean_row()], [_clean_row()]]
    assert aggregate(expand_raw(compact_raw(procs))) == aggregate(procs)


def test_verdict_reads_all_three_arms():
    base = {
        "algebraic": {"n_mismatched_questions": 0},
        "candidate_prefix": {"n_mismatched_questions": 0},
        "fuse_output_depth": {"n_mismatched_questions": 0,
                              "e2e_n_mismatched_questions": 0},
        "e2e": {"aa": {"n_mismatched": 0}, "ab": {"n_mismatched": 0}},
    }
    assert verdict(base)["POOL_DEEP_OK"] is True
    for arm in ("algebraic", "candidate_prefix"):
        bad = {k: dict(v) for k, v in base.items()}
        bad[arm] = {"n_mismatched_questions": 1}
        assert verdict(bad)["POOL_DEEP_OK"] is False, arm
    bad = {k: dict(v) for k, v in base.items()}
    bad["e2e"] = {"aa": {"n_mismatched": 0}, "ab": {"n_mismatched": 3}}
    assert verdict(bad)["POOL_DEEP_OK"] is False
