"""U2: StudyCorpusEngine — cards + 手順書章节 的组合器 (spec §4.1-4.2)。

引擎侧全用 stub (duck-typed), 不碰 chroma / 不发 embedding。
"""
from server.rag import RetrievedChunk
from server.study_corpus import StudyCorpusEngine


def _chunk(cid, file_type, sim=0.5):
    return RetrievedChunk(chunk_id=cid, source=f"{cid}.md", domain=None,
                          file_type=file_type, section=None, similarity=sim, text=f"t-{cid}")


class _Stub:
    def __init__(self, name, file_type, n=20):
        self.name, self.system_prompt = name, f"SYS-{name}"
        self._chunks = [_chunk(f"{name}-{i}", file_type, 0.9 - i * 0.01) for i in range(n)]
        self.calls = []

    def retrieve(self, q, *, top_k=None, **kw):
        self.calls.append(top_k)
        return self._chunks[: (top_k or 15)]

    def format_context(self, chunks):
        return f"CTX-{self.name}({len(chunks)})"

    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"{ctx}\n{q}"}]


def _engine(doc_seats=5, n_cards=20, n_docs=20):
    cards = _Stub("card", "field_card", n_cards)
    docs = _Stub("doc", "protocol_section", n_docs)
    return StudyCorpusEngine(cards, docs, doc_seats=doc_seats), cards, docs


def test_cards_keep_full_top_k_and_docs_are_appended():
    """doc 是加席不是抢席: cards 拿满 top_k, doc 追加在后, 总长 = top_k + seats。"""
    eng, cards, docs = _engine(doc_seats=5)
    got = eng.retrieve("q", top_k=15)
    assert cards.calls == [15]          # cards 的 top_k 原样传下去, 一席不减
    assert docs.calls == [5]
    assert len(got) == 20
    assert [c.file_type for c in got[:15]] == ["field_card"] * 15
    assert [c.file_type for c in got[15:]] == ["protocol_section"] * 5


def test_doc_seats_zero_means_channel_off():
    """seats=0 时 docs 引擎一次都不该被打 (零开销回落, 与通道 OFF 逐位相同)。"""
    eng, cards, docs = _engine(doc_seats=0)
    got = eng.retrieve("q", top_k=15)
    assert docs.calls == []
    assert len(got) == 15


def test_per_call_doc_seats_overrides_default():
    eng, _, docs = _engine(doc_seats=5)
    eng.retrieve("q", top_k=15, doc_seats=8)
    assert docs.calls == [8]


def test_duplicate_chunk_ids_are_deduped_cards_win():
    cards = _Stub("x", "field_card", 3)
    docs = _Stub("x", "protocol_section", 3)   # 同名 chunk_id
    eng = StudyCorpusEngine(cards, docs, doc_seats=3)
    got = eng.retrieve("q", top_k=3)
    assert [c.chunk_id for c in got] == ["x-0", "x-1", "x-2"]
    assert all(c.file_type == "field_card" for c in got)


def test_format_context_groups_the_two_source_kinds():
    eng, _, _ = _engine(doc_seats=2)
    ctx = eng.format_context(eng.retrieve("q", top_k=3))
    assert "CTX-card(3)" in ctx and "CTX-doc(2)" in ctx
    assert ctx.index("CTX-card(3)") < ctx.index("CTX-doc(2)")


def test_format_context_omits_absent_group():
    """只有卡片时不许打出空的手順書小节 (空标题会让答题方以为检索过而没找到)。"""
    eng, _, _ = _engine(doc_seats=0)
    ctx = eng.format_context(eng.retrieve("q", top_k=3))
    assert "CTX-doc" not in ctx


def test_system_prompt_comes_from_cards_engine_never_docs():
    """docs 引擎的 kb_root 指的是 cards/ ⇒ 它的 system_prompt 描述的是卡片库, 用了就是错的。"""
    eng, _, docs = _engine()
    docs.system_prompt = "POISON-must-never-be-read"
    assert "POISON" not in eng.system_prompt
    assert "SYS-card" in eng.system_prompt


def test_negative_doc_seats_fails_loud():
    import pytest
    with pytest.raises(ValueError, match="doc_seats"):
        _engine(doc_seats=-1)
