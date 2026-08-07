"""层① 探针的统计口径。构造已知组成的假 chunk, 验统计正确 —— 探针自己也要被测。"""
import pytest

from eval.crowding_probe import (
    crowding_across_processes,
    crowding_stats,
    max_cluster_section_tied,
    sections_by_chunk_id,
    stats_distribution,
)


class _C:
    def __init__(self, source, section):
        self.source, self.section = source, section


def test_no_duplicates():
    chunks = [_C(f"f{i}.md", f"s{i}") for i in range(5)]
    st = crowding_stats(chunks)
    assert st["dup_seats"] == 0
    assert st["max_cluster"] == 1
    assert st["distinct_sections"] == 5


def test_single_cluster():
    # 4 条同名 section (跨不同 source) + 1 条独立
    chunks = [_C(f"d{i}/spec.md", "DOMAIN") for i in range(4)] + [_C("x.md", "Other")]
    st = crowding_stats(chunks)
    assert st["max_cluster"] == 4
    assert st["max_cluster_section"] == "DOMAIN"
    assert st["dup_seats"] == 3          # 4 席里 3 席是多余的
    assert st["distinct_sections"] == 2


def test_two_clusters_dup_seats_sums_both():
    chunks = ([_C(f"a{i}.md", "A") for i in range(3)]
              + [_C(f"b{i}.md", "B") for i in range(2)])
    st = crowding_stats(chunks)
    assert st["max_cluster"] == 3
    assert st["dup_seats"] == 3          # (3-1) + (2-1)


def test_empty():
    st = crowding_stats([])
    assert st == {"dup_seats": 0, "max_cluster": 0,
                  "max_cluster_section": None, "distinct_sections": 0}


def test_same_section_same_source_still_counts():
    """同一文件的两个同名 section 也算簇 —— 挤占看的是席位, 不问来源。"""
    chunks = [_C("same.md", "S"), _C("same.md", "S")]
    assert crowding_stats(chunks)["max_cluster"] == 2


# ---- 簇头 section 名的可引用性标记 (下游读的是 JSON, 禁忌必须 in-band) ------


def test_tied_flag_true_when_max_cluster_is_shared():
    """两个 section 并列最大 -> 簇头名由插入顺序(=排位)决定, 必须标 true。"""
    chunks = [_C("a.md", "A"), _C("b.md", "B"), _C("c.md", "A"), _C("d.md", "B")]
    assert crowding_stats(chunks)["max_cluster"] == 2
    assert max_cluster_section_tied(chunks) is True


def test_tied_flag_false_when_cluster_head_is_unique():
    chunks = [_C("a.md", "A"), _C("b.md", "A"), _C("c.md", "B")]
    assert max_cluster_section_tied(chunks) is False


def test_tied_flag_true_when_no_cluster_at_all():
    """max_cluster==1 时人人并列 —— 实测 140 题里有 49 题是这种, 那个 section 名纯属噪声。"""
    chunks = [_C(f"f{i}.md", f"s{i}") for i in range(5)]
    assert crowding_stats(chunks)["max_cluster"] == 1
    assert max_cluster_section_tied(chunks) is True


def test_tied_flag_edge_cases():
    assert max_cluster_section_tied([]) is False           # 没有簇头可言
    assert max_cluster_section_tied([_C("a.md", "A")]) is False   # 唯一条目不算并列


# ---- 跨进程验稳 (brief Step 4B; 这些数字会进证据, 探针自己先被测) ----------


class _FakeCollection:
    """按 id 返回 metadata; 未知 id **静默丢掉** —— 与 Chroma 的真实行为一致。"""

    def __init__(self, meta):
        self.meta = meta

    def get(self, ids, include=None):
        known = [i for i in ids if i in self.meta]
        return {"ids": known, "metadatas": [{"section": self.meta[i]} for i in known]}


def test_sections_by_chunk_id_maps_from_index():
    col = _FakeCollection({"a#1": "DOMAIN", "b#2": None})
    assert sections_by_chunk_id(col, ["b#2", "a#1", "a#1"]) == {"a#1": "DOMAIN",
                                                               "b#2": None}
    assert sections_by_chunk_id(col, []) == {}


def test_sections_by_chunk_id_raises_on_unknown_id():
    """Chroma 对不存在的 id 静默返回空 —— 若跟着静默, 统计里会凭空多出一个 None 簇
    (同时抬高 dup_seats、压低 distinct_sections)。宁可红。"""
    col = _FakeCollection({"a#1": "DOMAIN"})
    with pytest.raises(KeyError, match="索引里没有这些 chunk_id"):
        sections_by_chunk_id(col, ["a#1", "ghost#9"])


def test_stats_distribution_reports_every_value_not_just_mode():
    """q47 那种接近四六开的题, 报众数就等于把不稳定写成了确定值。"""
    runs = [["a", "b"]] * 3 + [["a", "c"]] * 2
    d = stats_distribution(runs, {"a": "S", "b": "S", "c": "T"})
    assert d["n_runs"] == 5
    assert d["n_distinct_values"] == 2
    assert d["values"] == [
        {"max_cluster": 2, "dup_seats": 1, "distinct_sections": 1, "n_procs": 3},
        {"max_cluster": 1, "dup_seats": 0, "distinct_sections": 2, "n_procs": 2},
    ]


def test_stats_distribution_key_ignores_max_cluster_section():
    """两次运行的簇头 section 名不同但三个集合统计相同 -> 只算 1 种取值。

    并列时 `max_cluster_section` 的胜者由插入顺序 (= 排位) 决定, 而排位不可复现。
    把它算进分布键, 会把排位噪声伪装成"统计量不稳"。
    """
    runs = [["a", "b"], ["b", "a"]]
    d = stats_distribution(runs, {"a": "A", "b": "B"})
    assert d["n_distinct_values"] == 1
    assert d["values"][0]["n_procs"] == 2


def test_stats_distribution_order_is_deterministic():
    """证据要能逐字复跑: 次数相同的取值之间也必须有稳定先后。"""
    runs = [["a", "b"], ["c", "d"]]
    sections = {"a": "S", "b": "S", "c": "X", "d": "Y"}
    assert (stats_distribution(runs, sections)
            == stats_distribution(list(reversed(runs)), sections))


def test_crowding_across_processes_delegates_sampling_and_aggregates():
    """取样必须走 jitter_probe 的跨进程实现 (注入 runner 验参数透传与聚合口径)。
    进程内循环不算独立样本 —— 本项目不许有第二份跨进程逻辑。"""
    seen = {}

    def fake_runner(fn, payload):
        seen["payload"] = payload
        return [["a", "b"], ["a", "b"], ["a", "c"]]

    rep = crowding_across_processes(
        "q47?", n_procs=3, top_k=15,
        sections_of=lambda ids: {i: {"a": "S", "b": "S", "c": "T"}[i] for i in ids},
        runner=fake_runner,
    )
    assert len(seen["payload"]) == 3                     # 真起了 3 个样本
    assert all(p[0] == "q47?" for p in seen["payload"])  # 同一个问题
    assert rep["n_procs"] == 3
    assert rep["distinct_sets"] == 2                     # 成分换过人
    assert rep["n_distinct_values"] == 2
    assert rep["values"][0] == {"max_cluster": 2, "dup_seats": 1,
                                "distinct_sections": 1, "n_procs": 2}


def test_crowding_across_processes_rejects_single_process():
    """1 个进程量不到任何跨进程差异 —— 必须响亮拒绝 (由 jitter_probe 的护栏兜底)。"""
    with pytest.raises(ValueError, match="至少要 2 个进程"):
        crowding_across_processes("q", n_procs=1, sections_of=dict)
