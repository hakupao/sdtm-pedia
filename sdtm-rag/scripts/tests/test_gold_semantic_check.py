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
