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
    FACT_MIN_LEN,
    card_texts,
    chunk_bodies,
    gate_anchor_unique,
    gate_card_unanswerable,
    gate_fact_length,
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


# ---- 闸 C fact 长度 --------------------------------------------------------


def test_fact_min_len_is_12():
    """钉住字面值 (M1, 与 test_anchor_min_len_is_20 同构)。

    干净用例写的是 `"あ" * FACT_MIN_LEN` —— 长度引用常量, 会跟着常量一起漂:
    把 12 改成 3, 干净用例仍绿 (长 3 >= 3), 脏用例 `"短い"` 长 2 仍 < 3 照报,
    全套照绿而阈值等于没设。这一条是唯一挡住该漂移的断言。
    """
    assert FACT_MIN_LEN == 12


def test_gate_fact_length_accepts_long_fact():
    qs = [{"id": "q1", "expected_facts": ["あ" * FACT_MIN_LEN]}]
    assert gate_fact_length(qs) == []


def test_gate_fact_length_flags_short_fact():
    qs = [{"id": "q1", "expected_facts": ["短い"]}]
    f = gate_fact_length(qs)
    assert [x.gate for x in f] == ["fact_length"]


def test_gate_fact_length_accepts_short_oid_shaped_fact():
    """OID / codelist ID 天生短, 但不是碎片 —— 放行。

    两个串都是**合成**的: `C66742` 是公开 CDISC NCI 码, `XXTERM_99` 对 `data/study/`
    零命中。初版这里写的是真实 item OID, 属数据红线事故 (复审 C1)。
    """
    qs = [{"id": "q1", "expected_facts": ["C66742", "XXTERM_99"]}]
    assert gate_fact_length(qs) == []


def test_gate_fact_length_flags_missing_facts():
    qs = [{"id": "q1"}]
    assert [x.qid for x in gate_fact_length(qs)] == ["q1"]


def test_gate_fact_length_flags_two_char_upper_fragment():
    """钉住 `_ID_SHAPED` 的 `{2,}` 下限 (复审 m2)。

    白名单是闸 C **已知限制的入口** —— 没有这条, 把它放宽成 `^[A-Z]` 全套仍绿,
    已知限制就能在无人察觉时继续扩大。这里不用 `YES`: 3 字符全大写今天就是放行的,
    属已裁定的已知限制; 用长 2 的 `YE` 才钉得住下限。
    """
    qs = [{"id": "q1", "expected_facts": ["YE"]}]
    assert [x.qid for x in gate_fact_length(qs)] == ["q1"]


def test_gate_fact_length_flags_id_shaped_with_trailing_newline():
    """`$` 会匹配末尾换行, 故判定用 `fullmatch` (复审 m2)。

    `"C66742\\n"` 在 `.match` 下算 ID 形态被放行 —— YAML 块标量很容易带出这个尾巴。
    """
    qs = [{"id": "q1", "expected_facts": ["C66742\n"]}]
    assert [x.qid for x in gate_fact_length(qs)] == ["q1"]


# ---- 闸 D 卡片答不出 -------------------------------------------------------


def test_card_texts_reads_cards(tmp_path):
    d = tmp_path / "cards"
    d.mkdir()
    (d / "st01__F__I.md").write_text("label: ABC", encoding="utf-8")
    (d / "ignore.txt").write_text("x", encoding="utf-8")
    assert card_texts(d) == {"st01__F__I.md": "label: ABC"}


def test_card_texts_rejects_empty_dir(tmp_path):
    """空语料必须响亮失败 (复审 I1), 与 `lint_gold.doc_chunk_names` 同一处理。

    静默返回 `{}` 时闸 D 整闸白送: 没有卡片可撞 ⇒ 每题判绿。同一系列里两个语料装载器
    对空目录给相反处理是最坏的形态, 而先写的那个 (`doc_chunk_names`) 选的是炸。
    """
    d = tmp_path / "cards"
    d.mkdir()
    with pytest.raises(ValueError):
        card_texts(d)


def test_card_texts_rejects_missing_dir(tmp_path):
    """路径打错是这条洞的现实触发方式: `Path.glob` 对不存在的目录不报错, 只给空迭代。

    Task 4 的 `main` 把 `--cards-dir` 暴露到命令行后, 一个拼错的路径就让闸 D 变 no-op
    并以退出码 0 全绿收工。
    """
    with pytest.raises(ValueError):
        card_texts(tmp_path / "no_such_dir")


def test_gate_card_unanswerable_passes_when_no_card_has_all_terms():
    cards = {"a.md": "TERM_A only", "b.md": "TERM_B only"}
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "TERM_B"]}]
    assert gate_card_unanswerable(qs, cards) == []


def test_gate_card_unanswerable_flags_card_covering_all_terms():
    cards = {"a.md": "TERM_A and TERM_B together"}
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "TERM_B"]}]
    f = gate_card_unanswerable(qs, cards)
    assert [x.qid for x in f] == ["q1"]
    assert "a.md" in f[0].detail


def test_gate_card_unanswerable_is_case_insensitive():
    cards = {"a.md": "term_a and TERM_b"}
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "term_B"]}]
    assert [x.qid for x in gate_card_unanswerable(qs, cards)] == ["q1"]


def test_gate_card_unanswerable_requires_two_terms():
    """单个词太容易不撞卡 —— 闸会变成白送。"""
    qs = [{"id": "q1", "card_probe_terms": ["ONLY_ONE"]}]
    f = gate_card_unanswerable(qs, {"a.md": "x"})
    assert [x.qid for x in f] == ["q1"]
    assert "2" in f[0].detail


def test_gate_card_unanswerable_flags_scalar_probe_terms():
    """YAML 写成标量而非列表时必须报 (复审 m1)。

    字符串长度 >= 2 会滑过 `len(terms) < 2` 守卫, 随后**每个字符**被当成一个 probe 词
    —— 单字符几乎撞不上"全部命中", 于是静默判绿。同样的手滑闸 C 是吵闹地红
    (`len(fact)` 对字符串有意义), 闸 D 是安静地绿。题集 YAML 由出题批手写, 是典型手滑。
    """
    qs = [{"id": "q1", "card_probe_terms": "TERM_A"}]
    f = gate_card_unanswerable(qs, {"a.md": "x"})
    assert [x.qid for x in f] == ["q1"]
    assert "列表" in f[0].detail
