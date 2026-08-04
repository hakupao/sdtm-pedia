"""CJK 字符 bigram 切词 (BM25 稀疏通道的日文修复).

背景: bm25s 默认 token_pattern `(?u)\\b\\w\\w+\\b` 在 Unicode 下把整个日文连续串当成
**一个 token** —— 空白のない日本語クエリは語彙に一致せず, BM25 は近似常量の無関係集合を
返し, RRF 融合で真の dense 命中を押し出す。字符 bigram は CJK 検索の定石 (辞書不要・
決定的・未知語に強い)。

安全性の要: 変換は CJK 連続串にのみ作用 → 英文 (CDISC 主库) はバイト同一, 無条件適用可。
"""
from __future__ import annotations

import bm25s

from server.ja_tokenize import cjk_bigrams


# ---- 安全性: 英文は不変 (CDISC 主库の回帰防止) ----

def test_ascii_text_unchanged():
    s = "SDTM AE domain variable AETERM (Adverse Event Term), see IG 3.2."
    assert cjk_bigrams(s) == s


def test_empty_and_symbols_unchanged():
    assert cjk_bigrams("") == ""
    assert cjk_bigrams("--- 123 / 4.5 ---") == "--- 123 / 4.5 ---"


# ---- CJK 連続串 → 重疊 bigram ----

def test_japanese_run_becomes_overlapping_bigrams():
    # 4 文字 → 3 個の重疊 bigram
    assert cjk_bigrams("偽秘匿ラベル06").split() == ["偽秘", "秘匿", "匿ラ"]


def test_single_cjk_char_preserved():
    """長さ 1 の CJK 串は bigram が取れない → 原字を残す (欠落させない)."""
    assert cjk_bigrams("回").split() == ["回"]


def test_latin_survives_whole_in_mixed_text():
    out = cjk_bigrams("AE domain の変数").split()
    assert "AE" in out and "domain" in out      # 拉丁語は分割しない
    assert "の変" in out and "変数" in out        # CJK 側は bigram


def test_kana_and_kanji_in_same_run():
    """ひらがな・カタカナ・漢字は同一 CJK 走査単位 (境界で切らない)."""
    out = cjk_bigrams("偽秘匿ラベル01").split()
    assert "偽秘" in out and "偽名" in out and "偽名" in out


# ---- 実効性: 変換後は query と doc の token が交差する ----

def test_bigrams_make_query_and_doc_share_tokens():
    doc = "放射線を何回に分けて当てたかを記録する項目"
    query = "偽秘匿ラベル06はどの項目ですか"

    def vocab(text):
        return set(bm25s.tokenize(text, show_progress=False).vocab)

    # 現行 (未変換): 空白なし日本語は 1 token ずつ → 交差ゼロ
    assert not (vocab(doc) & vocab(query))
    # bigram 変換後: 共通語 (項目 等) が一致する
    assert vocab(cjk_bigrams(doc)) & vocab(cjk_bigrams(query))


# ---- RAGEngine 接线: index 与 query 两侧必须同时变换 (只变一侧 = 恒不匹配) ----

def test_rag_applies_bigrams_on_both_index_and_query(monkeypatch):
    """索引侧与查询侧必须用同一变换; 任一侧漏掉, 日文检索恒零命中."""
    import server.rag as rag_mod

    seen: list[str] = []
    real_tokenize = bm25s.tokenize

    def spy(texts, **kw):
        seen.extend([texts] if isinstance(texts, str) else list(texts))
        return real_tokenize(texts, **kw)

    # bm25s は関数内 lazy import → モジュールオブジェクト自体を差し替える
    monkeypatch.setattr(bm25s, "tokenize", spy)

    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng.collection = _FakeCollection(["# 偽秘匿ラベル06 (REDACTED_OID_04)"], ["c1"])
    eng.kb_root = __import__("pathlib").Path("/tmp")
    eng._bm25 = None
    eng._bm25_chunk_ids = []
    eng._bm25_chunk_meta = {}
    eng._build_bm25_index()
    assert any("偽秘 秘匿" in s for s in seen), "索引侧未做 bigram 变换"

    seen.clear()
    eng._bm25_search("偽秘匿ラベル06はどれですか", 5, None)
    assert any("偽秘 秘匿" in s for s in seen), "查询侧未做 bigram 变换"


class _FakeCollection:
    def __init__(self, docs, ids):
        self._docs, self._ids = docs, ids

    def get(self, include=None):
        return {"ids": self._ids, "documents": self._docs,
                "metadatas": [{"source": "x.md", "domain": "AE"}] * len(self._ids)}
