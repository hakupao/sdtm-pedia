"""doc 侧四闸单测。

反装饰保证 (硬规矩 18) 的结构: **每道闸都有一对测试** —— 干净 fixture 必须返回 []
(`*_passes_*` / `*_accepts_*`), 脏 fixture 必须返回 finding (`*_flags_*`)。
后者就是"闸恒返回 [] 则变红"的断言, 不需要再写一条同义的 `test_mutation_*`
—— 那只是同一断言的复制。cap_recall 那轮 `hidden_loss_shadow` 之所以是装饰品,
正是因为当时**缺**脏 fixture 测试, 不是因为缺一个叫 mutation 的测试。

物理变异测试 (把闸函数改成 `return []` 跑全套) 由 Task 9 Step 2 第 3 条的
独立抽检方执行 —— 那是实现方自己做不了的独立性检查。
"""
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


def test_anchor_min_len_is_20():
    """钉住字面值 (M1): 没有这条, 把 20 改成 3 全套仍绿, 阈值等于没设。"""
    assert ANCHOR_MIN_LEN == 20


def test_gate_anchor_unique_passes_when_anchor_lands_on_gold_only(tmp_path):
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
    # membership 口径下报的是**哪个** chunk 溢出, 不再是数量差 (旧文案 "2 != 1")
    assert "st01__doc01__s1_2.md" in f[0].detail


def test_gate_anchor_unique_flags_short_anchor():
    anchor = "X" * (ANCHOR_MIN_LEN - 1)
    qs = [{"id": "q1", "expected_sources": ["a.md"], "anchor": anchor}]
    f = gate_anchor_unique(qs, {"a.md": anchor})
    assert [x.gate for x in f] == ["anchor_unique"]
    assert "过短" in f[0].detail


def test_gate_anchor_unique_flags_missing_anchor():
    qs = [{"id": "q1", "expected_sources": ["a.md"]}]
    f = gate_anchor_unique(qs, {"a.md": "body"})
    assert [x.qid for x in f] == ["q1"]


def test_gate_anchor_unique_accepts_multi_gold(tmp_path):
    """跨节题: 锚串落在两个 gold chunk 里, 且不溢出到第三个。"""
    anchor = "Y" * ANCHOR_MIN_LEN
    bodies = {"a.md": anchor, "b.md": anchor, "c.md": "z"}
    qs = [{"id": "q1", "expected_sources": ["a.md", "b.md"], "anchor": anchor}]
    assert gate_anchor_unique(qs, bodies) == []


# ---- 闸 B fail-open 回归 (复审复现的四条恒绿) -----------------------------
# 四条的共同病根: 旧实现只比"含锚串的 chunk 数 == len(expected_sources)"。
# 数量相等不等于指向同一批 chunk, 而 n_gold==0 时 0==0 恒成立 ——
# "锚串根本不在语料里"正是这道闸存在的唯一理由, 却恰好是它看不见的那一格。


def test_gate_anchor_unique_flags_or_only_gold_with_fabricated_anchor():
    """① OR-only 题 + 捏造锚串。

    旧实现只数 expected_sources, OR-only 题 n_gold==0, 捏造锚串 hits==0 → 判绿。
    闸 A 经 lint_gold 是 AND/OR 两侧都查的, 闸 B 只看 AND 侧属两闸口径不一致。
    """
    anchor = "F" * ANCHOR_MIN_LEN          # 语料里没有
    bodies = {"a.md": "R" * ANCHOR_MIN_LEN, "b.md": "z"}
    qs = [{"id": "q1", "expected_sources_any": ["a.md"], "anchor": anchor}]
    assert [x.qid for x in gate_anchor_unique(qs, bodies)] == ["q1"]


def test_gate_anchor_unique_flags_question_without_any_gold():
    """② 完全无 gold + 捏造锚串 —— 必须报"无 gold"。

    闸 A 对没有 gold 键的题零迭代也不报, 所以两闸叠加后, 一道完全没有尺子的坏题
    能四闸全绿入池。这正是 LLM 出题最典型的坏题形态。
    """
    anchor = "F" * ANCHOR_MIN_LEN
    f = gate_anchor_unique([{"id": "q1", "anchor": anchor}], {"a.md": "z"})
    assert [x.qid for x in f] == ["q1"]
    assert "无 gold" in f[0].detail


def test_gate_anchor_unique_flags_anchor_in_wrong_chunk():
    """③ gold=[a] 但锚串只在 b —— 数量相等 (1==1), 指向完全错位。

    最致命的一条: 该题的 gold 与它的答案证据指向不同 chunk, 检索命中 gold 也答不出。
    """
    anchor = "R" * ANCHOR_MIN_LEN
    bodies = {"a.md": "z", "b.md": anchor}
    qs = [{"id": "q1", "expected_sources": ["a.md"], "anchor": anchor}]
    f = gate_anchor_unique(qs, bodies)
    assert [x.qid for x in f] == ["q1"]
    assert "a.md" in f[0].detail and "b.md" in f[0].detail


def test_gate_anchor_unique_flags_misaligned_multi_gold():
    """④ gold=[a,c] 但锚串在 a,b —— 数量相等 (2==2), 半数错位。

    与 test_gate_anchor_unique_accepts_multi_gold 共用同一 bodies, 只把 gold 的
    第二个成员由 b 换成 c: 干净/脏两侧只差这一处, 排除 fixture 其他差异的干扰。
    """
    anchor = "Y" * ANCHOR_MIN_LEN
    bodies = {"a.md": anchor, "b.md": anchor, "c.md": "z"}
    qs = [{"id": "q1", "expected_sources": ["a.md", "c.md"], "anchor": anchor}]
    assert [x.qid for x in gate_anchor_unique(qs, bodies)] == ["q1"]
