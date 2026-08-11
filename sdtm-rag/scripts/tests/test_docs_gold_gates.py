"""doc 侧四闸单测。

反装饰保证 (硬规矩 18) 的结构: **每道闸都有一对测试** —— 干净 fixture 必须返回 []
(`*_passes_*` / `*_accepts_*`), 脏 fixture 必须返回 finding (`*_flags_*`)。
后者就是"闸恒返回 [] 则变红"的断言, 不需要再写一条同义的 `test_mutation_*`
—— 那只是同一断言的复制。cap_recall 那轮 `hidden_loss_shadow` 之所以是装饰品,
正是因为当时**缺**脏 fixture 测试, 不是因为缺一个叫 mutation 的测试。

物理变异测试 (把闸函数改成 `return []` 跑全套) 由 Task 9 Step 2 第 3 条的
独立抽检方执行 —— 那是实现方自己做不了的独立性检查。
"""
import json

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
    main,
    run_all_gates,
)
from eval.lint_gold import load_questions

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

    白名单是闸 C **已知限制的入口** —— 没有这条, 把量词 `{2,}` 降成 `{1,}` 全套仍绿,
    已知限制就能在无人察觉时继续扩大。这里不用 `YES`: 3 字符全大写今天就是放行的,
    属已裁定的已知限制; 用长 2 的 `YE` 才钉得住下限。

    **别拿 `^[A-Z]` 当验证配方** (本条初版就是这么写的, 实测为假): 判定用的是
    `fullmatch`, 所以 `^[A-Z]` 只匹配**单字符**串 —— 它不是放宽而是**收紧**, 连
    `C66742` 都不再放行, 于是打红的是**干净侧**的 `accepts_short_oid_shaped_fact`
    (`1 failed`), 对本条零载荷。照那条配方复验的人会得到与描述相反的结果, 可能据此
    误判本条是装饰品而删掉它。`fullmatch` 下的等价放宽只有降低量词。
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


def test_card_texts_excludes_kb_navigation_files(tmp_path):
    """`INDEX.md` / `ROUTING.md` 是 kb_root 的导航文件, **不在检索语料里**。

    实测 (2026-08-11): `cards/*.md` = 961, 含 `__` = 959, chroma `study_st01` = 959
    —— 逐一相等, 即导航文件确实不可检索。闸 D 的口径是"没有任何一张 **field card**
    同时含全部 probe 词", 扫导航文件量的就不是那件事。
    """
    d = tmp_path / "cards"
    d.mkdir()
    (d / "st01__F__I.md").write_text("label: ABC", encoding="utf-8")
    (d / "INDEX.md").write_text("form list", encoding="utf-8")
    (d / "ROUTING.md").write_text("routing", encoding="utf-8")
    assert card_texts(d) == {"st01__F__I.md": "label: ABC"}


def test_gate_card_unanswerable_ignores_navigation_file_but_still_flags_field_card(tmp_path):
    """闸 D 不得因导航文件报, 但**仍须**因真实 field card 报。

    两个方向一起断言, 因为单测方向一 (不报) 时, 把 `card_texts` 改成恒返回 `{}`
    也能让它绿 —— 那是把闸拆了而不是修好。方向二钉住闸本身还活着。

    这条洞的真实后果 (spec §7): 闸 D 的筛掉率喂给 >50% 停止条款, 该条款用来**否掉
    C1 的整个价值假设**。`INDEX.md` 是列全部 form 名的表, 任意两个 form 级词都会在
    它里面双双命中 ⇒ 虚高的分子 ⇒ "文档与卡片高度重叠、C1 没价值"的错误结论。
    """
    d = tmp_path / "cards"
    d.mkdir()
    # 导航文件同时含两个 probe 词 —— 修好后不得触发闸 D
    (d / "INDEX.md").write_text("TERM_A and TERM_B together", encoding="utf-8")
    (d / "st01__F__CLEAN.md").write_text("TERM_A only", encoding="utf-8")
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "TERM_B"]}]
    assert gate_card_unanswerable(qs, card_texts(d)) == []

    # 同样两个词落在**真实 field card** 上时, 闸 D 必须照报
    (d / "st01__F__DIRTY.md").write_text("TERM_A and TERM_B together", encoding="utf-8")
    f = gate_card_unanswerable(qs, card_texts(d))
    assert [x.qid for x in f] == ["q1"]
    assert "st01__F__DIRTY.md" in f[0].detail


def test_card_texts_rejects_dir_with_only_navigation_files(tmp_path):
    """只有导航文件 = 没有 field card = 空语料, 守卫必须在过滤**之后**。

    否则 961 个文件里滤剩 0 张卡时, `out` 非空判断用的是过滤前的集合, 闸 D 白送。
    """
    d = tmp_path / "cards"
    d.mkdir()
    (d / "INDEX.md").write_text("x", encoding="utf-8")
    (d / "ROUTING.md").write_text("y", encoding="utf-8")
    with pytest.raises(ValueError):
        card_texts(d)


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


# ---- 汇总 CLI --------------------------------------------------------------


def _fixture(tmp_path, *, clean: bool):
    """clean=False 必须让**四道闸同时**报, 每道闸各有一个**独立**的脏维度。

    只弄脏一维时, `run_all_gates` 漏掉 A/B/C 中任意一个甚至全部三个, 四条用例仍全绿
    —— 缺失的加数在那个 fixture 上恒贡献 [], 断言原理上看不见它在不在。这个洞比单闸
    缺半边严重: 单闸缺 clean 半边只放过**恒红**闸 (吵, 会被发现), 聚合器缺口放过的是
    **恒绿** —— 而 Task 5-7 出题跑的就是这个 CLI, 漏掉的闸对每道新题静默返回"无
    finding", 题照常入池, 「四闸全绿」还会被后续证据引用成"尺子有判别力"。

    **闸 B 的脏维度必须是第三个 chunk, 不能是 s1_10 也含锚串** (实测, 别改回去):
    plan 初稿把闸 B 弄脏成"第二个 chunk 也含同一锚串 → 锚串出现 2 次而 gold 数 1",
    那是照着**旧的计数版**闸 B 写的。Task 3 复审已把闸 B 改成 membership 口径, 于是
    两个脏维度**互相抵消**: 不带 `.md` 的脏 gold 让 s1_10 也成了合法 target, 锚串落在
    两个 target 里既不 missing 也不 extra ⇒ 闸 B 返回 []。结果是这份 fixture 恰好对
    闸 B 恒绿, 聚合器漏掉闸 B 也测不出来 —— 正是本 fixture 要防的那个洞, 出现在防它的
    fixture 自己身上。故锚串溢出到一个 gold **解析不到**的 chunk (doc02)。

    **闸 B 在脏侧是双因致红, 两因冗余** (复审 Q3 实测, 别照着旧说法"该维度与 gold
    脏不脏无关"理解整条闸):

      baseline (doc02 脏)   → missing=['…s1_10.md']  extra=['…doc02__s9_1.md']  红
      wash_b   (doc02 干净) → missing=['…s1_10.md']  extra=[]                   仍红
      wash_a   (gold 带 .md)→ missing=[]             extra=['…doc02__s9_1.md']  仍红

    `extra` 那半确实与 gold 脏度无关, 但 `missing` 那半是**闸 A 脏维的副产物**: 不带
    `.md` 的 gold 经 `match_names` 子串匹配把 `s1_10.md` 也拉成 target, 而它正文
    `"other body"` 不含锚串。所以只断言"闸 B 报了"时, 把 doc02 洗干净甚至删掉, 全套照绿
    —— 与 I-1 在 C 维上的病同型, 换了个方向。故下面那条用例**额外断言 detail 里出现
    doc02**, 把闸 B 专属的那一维单独钉住。

    (真正的正交要把脏 gold 挪到第二道题, fixture 复杂度上升且 `计分题 1 道` 系列断言
    要改成 2 道 —— 不划算, 按复审裁定不做。)
    """
    anchor = "A" * 30
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "st01__doc01__s1_1.md").write_text(FM + anchor, encoding="utf-8")
    (docs / "st01__doc01__s1_10.md").write_text(FM + "other body", encoding="utf-8")
    # 脏 (闸 B 维, extra 半): 锚串溢出到 gold 解析不到的 chunk
    (docs / "st01__doc02__s9_1.md").write_text(
        FM + ("unrelated" if clean else anchor), encoding="utf-8")
    cards = tmp_path / "cards"
    cards.mkdir()
    # 脏 (闸 D 维): 同一张卡同时含全部 probe 词
    (cards / "st01__F__I.md").write_text(
        "TERM_A only" if clean else "TERM_A TERM_B", encoding="utf-8")
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        # 脏 (闸 A 维): gold 不带 .md → 同时命中 s1_1.md 与 s1_10.md
        f"  expected_sources: ['st01__doc01__s1_1{'.md' if clean else ''}']\n"
        # 脏 (闸 C 维): fact 过短且非 ID 形态
        f"  expected_facts: ['{'x' * 20 if clean else '短'}']\n"
        f"  anchor: '{anchor}'\n"
        "  card_probe_terms: ['TERM_A', 'TERM_B']\n",
        encoding="utf-8")
    return ts, docs, cards


def test_fixture_dirty_side_trips_each_gate_individually(tmp_path):
    """钉住"四个脏维度互相独立"这件事本身 —— fixture 是这批用例的唯一判别力来源。

    上面那场互相抵消的事故说明: fixture 某一维**看着**脏、实际对该闸恒绿, 是会真实发生的,
    且发生时四条聚合用例照绿 (因为它们只看聚合结果, 抵消掉的那维在聚合里也不出现)。
    这条把每道闸单独喂脏 fixture 各跑一次, 让"这一维真的脏"成为可执行断言而非注释里的声明。

    **四道闸的输入必须全部取自 fixture** (复审 I-1): 初版 B/C/D 喂的是手抄的 questions
    字面量, 于是闸 C 的脏维度 (题侧的 `'短'`) 住在手抄件里、不住在 fixture 里。实测把
    `_fixture` 的 fact 改长: 本用例照绿 (手抄件恒脏), 而 `run_all_gates` 的 gate 集合已
    掉成 `['anchor_unique', 'card_unanswerable', 'gold_unique']`。那样 C 维的脏度就只剩
    `test_run_all_gates_reports_every_gate` 间接背书 —— 而后者正是本用例要独立验证的对象,
    绕回了本用例本来要打断的循环 (聚合用例的判别力由聚合用例自己背书)。
    闸 A 收路径、B/C/D 收 `load_questions(ts)`, 与 `run_all_gates` 内部逐字同源。
    """
    ts, docs, cards = _fixture(tmp_path, clean=False)
    questions = load_questions(str(ts))
    assert [x.gate for x in gate_gold_unique(str(ts), docs)] == ["gold_unique"]
    b = gate_anchor_unique(questions, chunk_bodies(docs))
    assert [x.gate for x in b] == ["anchor_unique"]
    # 闸 B 专属那一维 (extra). 只断言"报了"的话, `missing` 半 (来自闸 A 脏维) 独力
    # 就能让它红 ⇒ 洗掉甚至删掉 doc02 全套照绿, 这条声明就没有执行力 (复审 Q3)。
    assert "st01__doc02__s9_1.md" in b[0].detail
    assert [x.gate for x in gate_fact_length(questions)] == ["fact_length"]
    assert [x.gate for x in gate_card_unanswerable(
        questions, card_texts(cards))] == ["card_unanswerable"]


def test_run_all_gates_clean_fixture_has_no_findings(tmp_path):
    ts, docs, cards = _fixture(tmp_path, clean=True)
    assert run_all_gates(str(ts), docs, cards) == []


def test_run_all_gates_reports_every_gate(tmp_path):
    """聚合器漏掉任一加数本用例必红 —— 断言的是 gate 集合, 不是某一个。"""
    ts, docs, cards = _fixture(tmp_path, clean=False)
    f = run_all_gates(str(ts), docs, cards)
    assert sorted({x.gate for x in f}) == [
        "anchor_unique", "card_unanswerable", "fact_length", "gold_unique"]


def test_main_exit_code_0_when_clean(tmp_path, capsys):
    ts, docs, cards = _fixture(tmp_path, clean=True)
    rc = main([str(ts), "--docs-dir", str(docs), "--cards-dir", str(cards)])
    assert rc == 0
    out = capsys.readouterr().out
    # 整句匹配, 不是 `"0 条"` 也不是 `"0 条 finding"` (复审 M-1 + 它自身的同款缺陷):
    # 两者都是 `"10 条 finding"` 的子串, 断言的就成了"报了"而非"报对了"。计分题数一并钉住。
    assert "计分题 1 道 · 0 条 finding" in out
    # 闸 B 的口径边界句 (硬规矩 19 明令"引用绿灯时必须同时写") 靠 main 无条件打印落实。
    # 没有这条断言, 把它从 main 删掉全套照绿 —— 设计对但没人守。
    assert "只挡字面" in out


def test_main_exit_code_1_when_findings(tmp_path, capsys):
    """退出码之外, `main` 的输出面也要有断言 (复审 M-1)。

    只断言 `rc == 1` 时, 把逐条打印循环删掉、把 `--json` 整个删掉, 全套照绿 ——
    而 `--json` 正是 Task 10 收口证据要引用的出口, 目前零覆盖。
    """
    ts, docs, cards = _fixture(tmp_path, clean=False)
    out_json = tmp_path / "findings.json"
    rc = main([str(ts), "--docs-dir", str(docs), "--cards-dir", str(cards),
               "--json", str(out_json)])
    assert rc == 1
    out = capsys.readouterr().out
    assert "计分题 1 道 · 4 条 finding" in out
    gates = ["anchor_unique", "card_unanswerable", "fact_length", "gold_unique"]
    assert all(g in out for g in gates)                     # 逐条打印循环
    dumped = json.loads(out_json.read_text(encoding="utf-8"))
    assert sorted({d["gate"] for d in dumped}) == gates      # --json 出口的内容
    assert all(d["qid"] == "q1" and d["detail"] for d in dumped)


def test_all_gates_see_the_same_question_set(tmp_path):
    """out_of_scope 题必须被四道闸**一致**跳过。

    闸 A 走路径、闸 B/C/D 走列表, 是两条加载路径。任一侧将来加了跳过标志而另一侧没加,
    两道闸就会判不同的题集且不报错 —— 与 lint_gold 那句"两个 gold 全集不可混用"同类,
    只是从"全集"挪到了"题集"。
    """
    ts, docs, cards = _fixture(tmp_path, clean=False)     # 四维全脏
    dirty = ts.read_text(encoding="utf-8") + "  out_of_scope: true\n"
    ts.write_text(dirty, encoding="utf-8")
    assert run_all_gates(str(ts), docs, cards) == []       # 全脏但被跳过 ⇒ 四闸都没看它
