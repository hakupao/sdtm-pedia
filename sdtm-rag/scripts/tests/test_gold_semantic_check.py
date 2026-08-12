"""gold 语义完整性自查的单测。

反装饰结构同 `test_docs_gold_gates.py`: 每条判据一对 (干净 → 不触发 / 脏 → 触发)。

**本文件最重要的一条是 `test_paraphrase_still_scores_high`** —— 它钉住的是这个模块
初版**实际失效**的那个原因, 不是假想风险: 初版把日文整段当一个 token, 于是
"换措辞表达同一事实"的 chunk 得分被压到触发线以下, 全批 0 触发, 而人工审题在同一
对象上判出真实的 gold 漏写。**长 token 恰好把本模块唯一要抓的东西滤掉了。**
"""
import pytest

from eval.gold_semantic_check import (
    THRESHOLD,
    coverage,
    fact_tokens,
    flagged,
    main,
    self_sufficient_golds,
)

FM = "---\nstudy: st01\n---\n"


def _docs(tmp_path, bodies: dict[str, str]):
    d = tmp_path / "docs"
    d.mkdir()
    for name, body in bodies.items():
        (d / name).write_text(FM + body, encoding="utf-8")
    return d


# ---- 切分单元 --------------------------------------------------------------


def test_fact_tokens_uses_char_ngrams_for_japanese():
    """日文按字符 n-gram 切, 不是整段黏连成一个长 token。"""
    toks = fact_tokens(["登録完了後は28日以内に開始"])
    assert "28" in toks                          # 数字整词
    assert all(len(t) <= 3 for t in toks if not t.isdigit())
    assert "登録完" in toks and "録完了" in toks   # 滑窗 trigram


def test_fact_tokens_keeps_latin_and_numbers_whole():
    toks = fact_tokens(["CTCAE v5.0 と 608 例"])
    assert "CTCAE" in toks
    assert "608" in toks


def test_fact_tokens_dedupes():
    """同一单元在多条 fact 里重复不得加权 —— 问的是覆盖了多少**种**要素。"""
    once = fact_tokens(["登録完了後"])
    twice = fact_tokens(["登録完了後", "登録完了後"])
    assert once == twice


def test_fact_tokens_keeps_short_run_whole():
    assert "登録" in fact_tokens(["登録"])


# ---- 覆盖率与触发 ----------------------------------------------------------


def test_paraphrase_still_scores_high(tmp_path):
    """**回归钉**: 换助词/语序表达同一事实的非 gold chunk 必须仍得高分。

    初版整段切分时这类 chunk 得分被压到触发线下 —— 本模块唯一要抓的就是它。
    """
    docs = _docs(tmp_path, {
        "st01__doc01__s1_1.md": "登録完了後は28日以内にプロトコール治療を開始する",
        # 同一事实, 换了助词与语序
        "st01__doc01__s2_1.md": "プロトコール治療は登録完了後28日以内に開始すること",
    })
    q = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"],
          "expected_facts": ["登録完了後は28日以内にプロトコール治療を開始する"]}]
    from eval.docs_gold_gates import chunk_bodies
    rows = {o.chunk: o.score for o in coverage(q, chunk_bodies(docs))}
    assert rows["st01__doc01__s1_1.md"] == 1.0
    assert rows["st01__doc01__s2_1.md"] >= THRESHOLD, (
        f"改写版只拿到 {rows['st01__doc01__s2_1.md']:.2f} — 切分单元又变长了")


def test_flagged_reports_non_gold_above_threshold(tmp_path):
    docs = _docs(tmp_path, {
        "st01__doc01__s1_1.md": "登録完了後は28日以内にプロトコール治療を開始する",
        "st01__doc01__s2_1.md": "プロトコール治療は登録完了後28日以内に開始すること",
    })
    q = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"],
          "expected_facts": ["登録完了後は28日以内にプロトコール治療を開始する"]}]
    from eval.docs_gold_gates import chunk_bodies
    f = flagged(q, chunk_bodies(docs))
    assert [(o.qid, o.chunk) for o in f] == [("q1", "st01__doc01__s2_1.md")]


def test_flagged_stays_silent_when_no_other_chunk_carries_the_answer(tmp_path):
    """干净维: 别的 chunk 与答案无关时不得触发 (否则整条变噪声)。"""
    docs = _docs(tmp_path, {
        "st01__doc01__s1_1.md": "登録完了後は28日以内にプロトコール治療を開始する",
        "st01__doc01__s2_1.md": "放射線治療装置は6-15MVのX線発生装置を用いる",
    })
    q = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"],
          "expected_facts": ["登録完了後は28日以内にプロトコール治療を開始する"]}]
    from eval.docs_gold_gates import chunk_bodies
    assert flagged(q, chunk_bodies(docs)) == []


def test_gold_chunk_is_never_flagged(tmp_path):
    """gold 自己得 1.00 也不该出现在触发列表里 —— 它本来就该含答案。"""
    docs = _docs(tmp_path, {"st01__doc01__s1_1.md": "登録完了後は28日以内に開始する"})
    q = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"],
          "expected_facts": ["登録完了後は28日以内に開始する"]}]
    from eval.docs_gold_gates import chunk_bodies
    bodies = chunk_bodies(docs)
    assert [o.score for o in coverage(q, bodies) if o.is_gold] == [1.0]
    assert flagged(q, bodies) == []


# ---- CLI: 触发器不是闸 ------------------------------------------------------


def test_main_exit_code_is_zero_even_with_flags(tmp_path, capsys):
    """**触发器不是闸**: 有触发也必须退出码 0, 否则它就成了阈值闸。

    这条钉的是一个未来的错误 —— 看到 [FLAG] 就想把它变成红灯。高分不等于错:
    相邻节复述同一规则是 protocol 的常态, 合法的跨节聚合题天然有多个高分 chunk。
    """
    docs = _docs(tmp_path, {
        "st01__doc01__s1_1.md": "登録完了後は28日以内にプロトコール治療を開始する",
        "st01__doc01__s2_1.md": "プロトコール治療は登録完了後28日以内に開始すること",
    })
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        "  expected_sources: ['st01__doc01__s1_1.md']\n"
        "  expected_facts: ['登録完了後は28日以内にプロトコール治療を開始する']\n",
        encoding="utf-8")
    rc = main([str(ts), "--docs-dir", str(docs)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "[FLAG] q1" in out
    assert "st01__doc01__s2_1.md" in out
    assert "触发人工复核" in out


def test_main_output_carries_no_prose(tmp_path, capsys):
    """输出会贴进进 git 的 evidence, 且 chunk 正文实测含研究者姓名/联系方式。

    故只许出现 qid / 文件名 / 分数 —— 不得回显 fact 原文或 chunk 正文。
    """
    docs = _docs(tmp_path, {"st01__doc01__s1_1.md": "登録完了後は28日以内に開始する"})
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        "  expected_sources: ['st01__doc01__s1_1.md']\n"
        "  expected_facts: ['登録完了後は28日以内に開始する']\n",
        encoding="utf-8")
    main([str(ts), "--docs-dir", str(docs)])
    out = capsys.readouterr().out
    assert "登録完了後" not in out


def test_threshold_default_is_0_7():
    """审题方 2026-08-11 给的复核触发线, 改动要显式。"""
    assert THRESHOLD == pytest.approx(0.7)


# ---- 单 gold 自足性 (多 gold 题专用) ----------------------------------------
#
# `flagged()` 按设计豁免 gold, 所以它**结构上**看不见"两个 gold 里有一个其实自足"。
# 而多 gold 题正是跨节探针的题型 ⇒ 那道判据对最需要它的题型覆盖率恒为 0。
#
# 下面这批 fixture 用无意义拉丁词而不是日文, 是为了让**逐 fact 分数是可手算的整分数**
# (每条 fact 4 个 token ⇒ 命中 2 个恰好 0.50), 阈值边界与"逐 fact vs 合并"两条判据
# 才能钉死在精确值上; 日文 n-gram 那条口径另有一条改写回归钉 (见本节最后一条)。

S1 = "st01__doc01__s1_1.md"
S2 = "st01__doc01__s2_1.md"
S3 = "st01__doc01__s3_1.md"

F1 = "alpha bravo charlie delta"      # 4 个可计数单元
F2 = "echo foxtrot golf hotel"        # 4 个, 与 F1 无公共子串
F2_HALF = "echo foxtrot"              # F2 的一半 ⇒ 该 fact 覆盖率 0.50


def _bodies(tmp_path, files: dict[str, str]):
    from eval.docs_gold_gates import chunk_bodies
    return chunk_bodies(_docs(tmp_path, files))


def _q(golds: list[str], facts: list[str], any_golds: list[str] | None = None) -> list[dict]:
    q = {"id": "q1", "expected_sources": golds, "expected_facts": facts}
    if any_golds:
        q["expected_sources_any"] = any_golds
    return [q]


def test_selfsuff_flags_gold_that_alone_covers_every_fact(tmp_path):
    """脏维: 一个 gold 独自扛下每一条 fact ⇒ 另一个 gold 疑似冗余, 必须报。"""
    b = _bodies(tmp_path, {S1: f"{F1} / {F2}", S2: F2})
    rows = self_sufficient_golds(_q([S1, S2], [F1, F2]), b)
    assert [(r.qid, r.chunk) for r in rows] == [("q1", S1)]
    assert rows[0].per_fact == (1.0, 1.0)


def test_selfsuff_silent_when_golds_split_the_facts(tmp_path):
    """干净维: 两个 gold 各扛一条 fact (真跨节) ⇒ 一条都不报, 否则整项变噪声。"""
    b = _bodies(tmp_path, {S1: F1, S2: F2})
    assert self_sufficient_golds(_q([S1, S2], [F1, F2]), b) == []


def test_selfsuff_skips_single_gold_questions(tmp_path):
    """单 gold 题按定义就自足, 报它是纯噪声 (脏半边见上面第一条: 同样正文两个 gold 就报)。"""
    b = _bodies(tmp_path, {S1: f"{F1} {F2}"})
    assert self_sufficient_golds(_q([S1], [F1, F2]), b) == []


def test_selfsuff_is_per_fact_not_aggregate(tmp_path):
    """干净维 + **判别力证明**: 合并口径会放行的同一份数据, 逐 fact 口径必须不报。

    S1 命中 F1 全部 4 个单元 + F2 的 2 个 ⇒ 合并 6/8 = 0.75 >= 触发线, 但逐 fact
    是 [1.00, 0.50] —— 它答不全第二条 fact, 不是自足。若哪天有人把本函数改成
    "合并覆盖率 >= 阈值", 这条会红。
    """
    b = _bodies(tmp_path, {S1: f"{F1} {F2_HALF}", S2: F2})
    q = _q([S1, S2], [F1, F2])
    assert {o.chunk: o.score for o in coverage(q, b)}[S1] >= THRESHOLD
    assert self_sufficient_golds(q, b) == []


def test_selfsuff_flags_once_the_weak_fact_is_also_covered(tmp_path):
    """脏半边: 与上一条**只差**把那半条 fact 补全, 结果必须翻成报。"""
    b = _bodies(tmp_path, {S1: f"{F1} {F2}", S2: F2})
    assert [r.chunk for r in self_sufficient_golds(_q([S1, S2], [F1, F2]), b)] == [S1]


def test_selfsuff_threshold_boundary_is_inclusive(tmp_path):
    """边界含等号, 且两个 gold 同时自足时两个都报 (互为冗余, 谁多余要人判)。"""
    b = _bodies(tmp_path, {S1: "alpha bravo", S2: "charlie delta"})
    q = _q([S1, S2], [F1])
    assert [r.chunk for r in self_sufficient_golds(q, b, threshold=0.5)] == [S1, S2]
    assert self_sufficient_golds(q, b, threshold=0.51) == []


def test_selfsuff_ignores_non_gold_chunks(tmp_path):
    """非 gold 含全部答案是 `flagged()` 的活, 不是本函数的 —— 两条判据不许互相顶替。

    脏半边由同一份 fixture 的 `flagged()` 断言给出: 它确实看得见那个非 gold chunk,
    所以本函数的 `[]` 是"分工不同", 不是"两边都瞎"。
    """
    b = _bodies(tmp_path, {S1: F1, S2: F2, S3: f"{F1} {F2}"})
    q = _q([S1, S2], [F1, F2])
    assert self_sufficient_golds(q, b) == []
    assert [o.chunk for o in flagged(q, b)] == [S3]


def test_selfsuff_does_not_treat_or_side_as_multi_gold(tmp_path):
    """OR 组按定义就是"任一成员即可自足", 拿它当多 gold 会把设计意图报成缺陷。"""
    b = _bodies(tmp_path, {S1: f"{F1} {F2}", S2: f"{F1} {F2}"})
    assert self_sufficient_golds(_q([S1], [F1, F2], any_golds=[S2]), b) == []
    assert len(self_sufficient_golds(_q([S1, S2], [F1, F2]), b)) == 2


def test_selfsuff_skips_facts_with_no_countable_unit(tmp_path):
    """无可计数单元的 fact (纯符号) 不参与 —— 否则 0 除; 全无单元则整题跳过。"""
    b = _bodies(tmp_path, {S1: F1, S2: F2})
    assert self_sufficient_golds(_q([S1, S2], ["!!", "??"]), b) == []
    rows = self_sufficient_golds(_q([S1, S2], [F1, "!!"]), b)
    assert [(r.chunk, r.per_fact) for r in rows] == [(S1, (1.0,))]


def test_selfsuff_counts_paraphrased_gold(tmp_path):
    """**回归钉**: 换措辞承载同一 fact 的 gold 也算自足 —— 必须与 `flagged()` 同一套
    切分口径 (`fact_tokens`)。另写一份"逐字包含"的判据会让这条红。"""
    b = _bodies(tmp_path, {
        S1: "プロトコール治療は登録完了後28日以内に開始すること",
        S2: "放射線治療装置は6-15MVのX線発生装置を用いる",
    })
    q = _q([S1, S2], ["登録完了後は28日以内にプロトコール治療を開始する"])
    assert [r.chunk for r in self_sufficient_golds(q, b)] == [S1]


# ---- CLI: 新模式同样是触发器不是闸 ------------------------------------------


def _ts(tmp_path, golds: list[str], facts: list[str]):
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        f"  expected_sources: {golds!r}\n"
        f"  expected_facts: {facts!r}\n",
        encoding="utf-8")
    return ts


def test_main_selfsuff_mode_exits_zero_with_findings(tmp_path, capsys):
    """有触发也必须退出码 0 —— 与 `flagged` 同取向, 高分不等于错。"""
    docs = _docs(tmp_path, {S1: f"{F1} {F2}", S2: F2})
    rc = main([str(_ts(tmp_path, [S1, S2], [F1, F2])),
               "--docs-dir", str(docs), "--mode", "selfsuff"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "[SELF] q1" in out and S1 in out
    assert "[FLAG]" not in out          # 两个模式互不串台


def test_main_default_mode_prints_no_selfsuff(tmp_path, capsys):
    """既有默认行为一字不动: 不点名新模式就不该多出任何一行。"""
    docs = _docs(tmp_path, {S1: f"{F1} {F2}", S2: F2})
    main([str(_ts(tmp_path, [S1, S2], [F1, F2])), "--docs-dir", str(docs)])
    out = capsys.readouterr().out
    assert "[SELF]" not in out
    assert "[cover] q1" in out


def test_main_selfsuff_output_carries_no_prose(tmp_path, capsys):
    """输出要贴进进 git 的 evidence: 只许 qid / 文件名 / 分数。"""
    docs = _docs(tmp_path, {
        S1: "プロトコール治療は登録完了後28日以内に開始すること",
        S2: "放射線治療装置は6-15MVのX線発生装置を用いる",
    })
    fact = "登録完了後は28日以内にプロトコール治療を開始する"
    main([str(_ts(tmp_path, [S1, S2], [fact])), "--docs-dir", str(docs), "--mode", "selfsuff"])
    out = capsys.readouterr().out
    assert "[SELF] q1" in out
    assert "登録完了後" not in out
