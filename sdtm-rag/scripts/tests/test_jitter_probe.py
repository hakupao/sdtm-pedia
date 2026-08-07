"""稳定性统计的口径。构造已知的多次运行结果, 验统计正确。"""
import contextlib
import math

import pytest

from eval.jitter_probe import (
    min_adjacent_gap,
    pair_margins,
    perturbed_vectors,
    retrieve_under_perturbation,
    stability_across_processes,
    stability_report,
)


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


# ---- 扰动注入: Task 4 要靠它验每题统计的稳定性, 所以它自己必须先被验 ----


def test_perturbed_vectors_hits_requested_distance():
    """扰动幅度必须**恰好**是请求的 L2 —— 这个数字直接决定结论的量纲。"""
    base = [0.1, -0.2, 0.3, 0.4]
    out = perturbed_vectors(base, l2=1e-3, n=5)
    assert len(out) == 5
    for v in out:
        d = math.sqrt(sum((a - b) ** 2 for a, b in zip(base, v, strict=True)))
        assert abs(d - 1e-3) < 1e-12
    assert base == [0.1, -0.2, 0.3, 0.4]          # 不许就地改输入
    assert len({tuple(v) for v in out}) == 5      # 5 个不同方向


def test_perturbed_vectors_is_deterministic_given_seed():
    """证据要可复跑: 同 seed 必须逐位重现, 否则复跑得不到同一批数字。"""
    base = [0.5, 0.5]
    assert perturbed_vectors(base, 1e-3, 3, seed=7) == perturbed_vectors(base, 1e-3, 3, seed=7)
    assert perturbed_vectors(base, 1e-3, 3, seed=7) != perturbed_vectors(base, 1e-3, 3, seed=8)


class _FakeRag:
    """只记录被喂进来的向量, 并按向量返回可区分的结果。"""

    def __init__(self):
        self.seen = []
        self._embed_query = lambda text: [0.0, 0.0]

    def retrieve(self, question, top_k=None):
        v = self._embed_query(question)
        self.seen.append(v)
        return [f"chunk-{round(v[0], 6)}"]


def test_retrieve_under_perturbation_feeds_each_vector_and_restores_embed():
    rag = _FakeRag()
    original = rag._embed_query
    out = retrieve_under_perturbation(rag, "q", [[1.0, 0.0], [2.0, 0.0]], top_k=15)
    assert rag.seen == [[1.0, 0.0], [2.0, 0.0]]   # 每个向量都真被用上
    assert out == [["chunk-1.0"], ["chunk-2.0"]]
    assert rag._embed_query is original           # 用完必须还原, 否则污染后续调用


def test_retrieve_under_perturbation_restores_embed_on_error():
    """检索中途抛错也必须还原 —— 否则引擎会被永久钉在某个假向量上。"""
    rag = _FakeRag()
    original = rag._embed_query

    def boom(question, top_k=None):
        raise RuntimeError("retrieval failed")

    rag.retrieve = boom
    with contextlib.suppress(RuntimeError):
        retrieve_under_perturbation(rag, "q", [[1.0, 0.0]], top_k=15)
    assert rag._embed_query is original


# ---- 跨进程稳定性: 第一版漏掉的那一维 ----


def test_stability_across_processes_rejects_single_process():
    """1 个进程量不到跨进程差异 —— 必须响亮拒绝, 而不是返回一个"很稳"的假结论。
    第一版探针的教训就是"样本数看着大、独立样本数其实是 1"。"""
    import pytest
    with pytest.raises(ValueError, match="至少要 2 个进程"):
        stability_across_processes("q", n_procs=1)


def test_stability_across_processes_aggregates_runner_output():
    """注入 runner 验聚合口径: 3 个进程里有一个换了人, 必须报成分不稳。"""
    def fake_runner(fn, payload):
        assert len(payload) == 3
        assert all(p[0] == "q38?" for p in payload)      # 每个进程拿到同一个问题
        assert all(p[3] == [0.1, 0.2] for p in payload)  # 固定向量被透传
        return [["a", "b", "c"], ["a", "b", "c"], ["a", "b", "d"]]

    r = stability_across_processes(
        "q38?", n_procs=3, vector=[0.1, 0.2], runner=fake_runner)
    assert r["n_procs"] == 3
    assert r["vector_fixed"] is True
    assert r["distinct_sets"] == 2
    assert r["sometimes"] == 2      # c, d
    assert r["always"] == 2         # a, b


@pytest.mark.slow
def test_stability_across_processes_real_subprocess_smoke():
    """真子进程路径的冒烟测试 (n_procs=2)。

    上面两条跨进程测试都注入 fake runner, 只验聚合口径与参数透传; 而**改判整个压在
    真实子进程这条路径上** —— 它若因为 cwd / 模块名 / pickling 之类的原因起不来,
    上面两条一条都不会红。这里就用最小规模真起两个进程, 换 API 与 Chroma 的真实开销。

    只断言"路径能跑通且形状对", 不断言稳定性: 2 个进程的结果本来就可能同也可能不同。
    """
    from server.config import settings

    rep = stability_across_processes(
        "What is the DOMAIN variable?", n_procs=2,
        config="hybrid", top_k=settings.top_k,
    )
    assert rep["n_procs"] == 2
    assert len(rep["runs"]) == 2
    assert all(len(r) > 0 for r in rep["runs"])          # 真检索回了东西
    assert all(isinstance(c, str) for r in rep["runs"] for c in r)
    assert rep["distinct_sets"] in (1, 2)
