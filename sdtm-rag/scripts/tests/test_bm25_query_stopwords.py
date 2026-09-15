"""DM1 D5: query-side BM25 stopwords for corpus-generic words.

`sdtm` / `cdisc` / `domain` / `dataset` appear in almost every CDISC chunk — they
carry no lexical signal but out-rank the one informative token in short questions.
This filter only touches the QUERY tokenization; the index itself is untouched.
"""
from __future__ import annotations
from pathlib import Path

import bm25s

import server.rag as rag_mod


def test_stopword_list_contains_generic_corpus_words():
    sw = set(rag_mod._BM25_QUERY_STOPWORDS)
    assert {"sdtm", "cdisc", "domain", "dataset", "the"} <= sw
    assert "disposition" not in sw


def test_stopword_list_matches_bm25s_english_defaults_plus_corpus_words():
    """The base list must be bm25s's own English stopwords, not a hand-copied
    approximation that silently drifts from the library on an upgrade."""
    sw = set(rag_mod._BM25_QUERY_STOPWORDS)
    base = set(bm25s.stopwords.STOPWORDS_EN)
    extra = {"sdtm", "sdtmig", "cdisc", "domain", "domains", "dataset", "datasets"}
    assert sw == base | extra


def test_all_stopword_query_yields_no_bm25_hits():
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._bm25_chunk_ids = ["a"]
    eng._bm25_chunk_meta = {"a": {"meta": {}, "text": "x"}}
    eng.bm25_query_stopwords = True

    class _Idx:
        def retrieve(self, *a, **k):
            raise AssertionError("must not be called for an empty query")

    eng._bm25 = _Idx()
    assert eng._bm25_search("the sdtm domain dataset", 5, None) == []


def test_disabled_lever_falls_back_to_plain_english_stopwords():
    """bm25_query_stopwords=False must NOT strip the corpus-generic words —
    a query of only those words should still reach `_bm25.retrieve`."""
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._bm25_chunk_ids = ["a"]
    eng._bm25_chunk_meta = {"a": {"meta": {}, "text": "x"}}
    eng.bm25_query_stopwords = False
    eng.kb_root = Path(".")

    calls = []

    class _Idx:
        def retrieve(self, tokens, k, show_progress):
            calls.append(tokens)
            return [[0]], [[1.23]]

    eng._bm25 = _Idx()
    out = eng._bm25_search("sdtm domain dataset", 5, None)
    assert len(calls) == 1
    assert len(out) == 1
