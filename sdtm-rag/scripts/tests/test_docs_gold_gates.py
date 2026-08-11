"""doc 侧四闸单测。

反装饰保证 (硬规矩 18) 的结构: **每道闸都有一对测试** —— 干净 fixture 必须返回 []
(`*_passes_*` / `*_accepts_*`), 脏 fixture 必须返回 finding (`*_flags_*`)。
后者就是"闸恒返回 [] 则变红"的断言, 不需要再写一条同义的 `test_mutation_*`
—— 那只是同一断言的复制。cap_recall 那轮 `hidden_loss_shadow` 之所以是装饰品,
正是因为当时**缺**脏 fixture 测试, 不是因为缺一个叫 mutation 的测试。

物理变异测试 (把闸函数改成 `return []` 跑全套) 由 Task 9 Step 2 第 3 条的
独立抽检方执行 —— 那是实现方自己做不了的独立性检查。
"""
import pytest

from eval.docs_gold_gates import (
    ANCHOR_MIN_LEN,
    chunk_bodies,
    gate_anchor_unique,
    gate_gold_unique,
)

FM = "---\nstudy: st01\nsection_number: '10.1'\n---\n"


def _docs(tmp_path, bodies: dict[str, str]):
    d = tmp_path / "docs"
    d.mkdir()
    for name, body in bodies.items():
        (d / name).write_text(FM + body, encoding="utf-8")
    return d


def test_chunk_bodies_strips_frontmatter(tmp_path):
    d = _docs(tmp_path, {"st01__doc01__s1_1.md": "BODY-TEXT\n"})
    assert chunk_bodies(d) == {"st01__doc01__s1_1.md": "BODY-TEXT\n"}


def test_gate_gold_unique_passes_when_gold_locates_one_chunk(tmp_path):
    """闸 A 的干净半边 (硬规矩 18 的"一对"): 唯一定位的 gold 不得报。

    没有这一半时, 一个对每条 gold 都吐 finding 的恒红闸能全绿通过。恒红比恒绿温和,
    但它的下场通常是被人关掉。
    """
    d = _docs(tmp_path, {"st01__doc01__s1_1.md": "a", "st01__doc01__s1_10.md": "b"})
    ts = tmp_path / "ts.yml"
    ts.write_text("- id: q1\n  expected_sources: ['st01__doc01__s1_1.md']\n", encoding="utf-8")
    assert gate_gold_unique(str(ts), d) == []


def test_gate_gold_unique_flags_multi_match(tmp_path):
    d = _docs(tmp_path, {"st01__doc01__s1_1.md": "a", "st01__doc01__s1_10.md": "b"})
    ts = tmp_path / "ts.yml"
    ts.write_text("- id: q1\n  expected_sources: ['st01__doc01__s1_1']\n", encoding="utf-8")
    f = gate_gold_unique(str(ts), d)
    assert [x.qid for x in f] == ["q1"]
    assert f[0].gate == "gold_unique"


def test_gate_anchor_unique_passes_when_count_equals_gold_count(tmp_path):
    anchor = "X" * ANCHOR_MIN_LEN
    bodies = {"st01__doc01__s1_1.md": anchor, "st01__doc01__s1_2.md": "other"}
    qs = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"], "anchor": anchor}]
    assert gate_anchor_unique(qs, bodies) == []


def test_gate_anchor_unique_flags_when_anchor_appears_in_extra_chunk(tmp_path):
    anchor = "X" * ANCHOR_MIN_LEN
    bodies = {"st01__doc01__s1_1.md": anchor, "st01__doc01__s1_2.md": anchor}
    qs = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"], "anchor": anchor}]
    f = gate_anchor_unique(qs, bodies)
    assert [x.qid for x in f] == ["q1"]
    assert "2 != 1" in f[0].detail


def test_gate_anchor_unique_flags_short_anchor():
    anchor = "X" * (ANCHOR_MIN_LEN - 1)
    qs = [{"id": "q1", "expected_sources": ["a.md"], "anchor": anchor}]
    f = gate_anchor_unique(qs, {"a.md": anchor})
    assert [x.gate for x in f] == ["anchor_unique"]
    assert "短すぎ" in f[0].detail or "过短" in f[0].detail


def test_gate_anchor_unique_flags_missing_anchor():
    qs = [{"id": "q1", "expected_sources": ["a.md"]}]
    f = gate_anchor_unique(qs, {"a.md": "body"})
    assert [x.qid for x in f] == ["q1"]


def test_gate_anchor_unique_counts_multi_gold(tmp_path):
    """跨节题: gold 2 个, 锚串必须正好出现 2 次。"""
    anchor = "Y" * ANCHOR_MIN_LEN
    bodies = {"a.md": anchor, "b.md": anchor, "c.md": "z"}
    qs = [{"id": "q1", "expected_sources": ["a.md", "b.md"], "anchor": anchor}]
    assert gate_anchor_unique(qs, bodies) == []
