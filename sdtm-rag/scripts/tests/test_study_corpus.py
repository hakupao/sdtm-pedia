"""U2: StudyCorpusEngine — cards + 手順書章节 的组合器 (spec §4.1-4.2)。

引擎侧全用 stub (duck-typed), 不碰 chroma / 不发 embedding。
"""
import pytest

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


def test_both_mode_halves_cards_but_never_shrinks_doc_seats():
    """both 判库下 cards 只拿 ceil(15/2)=8 席 (federation.py:129), doc 仍取满 N。

    spec §4.2 逐字禁止在 both 下缩 doc 席位 (缩了则 both 题与 study 题的 doc 召回不可比)。
    这里刻意取 N=10 > top_k=8: 本断言是 `seats = min(doc_seats, top_k)` 那类"顺手修"
    (见 evidence/step_u2_mutation.md 已知限制 b) 的唯一守卫, N ≤ top_k 时它守不住。
    """
    eng, cards, docs = _engine(doc_seats=10)
    got = eng.retrieve("q", top_k=8)
    assert cards.calls == [8]
    assert docs.calls == [10]
    assert len(got) == 18


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


def test_docs_internal_duplicates_are_deduped_too():
    """docs 引擎自己返回重复 chunk_id 时也要去重。

    上一条测试里 docs 的 id 全被 cards 的 seen 挡在 `continue`, 从没走到 `seen.add(d.chunk_id)`
    那行 —— 去掉 seen.add 也不会红。这条专门走那行。
    """
    cards = _Stub("card", "field_card", 2)
    docs = _Stub("doc", "protocol_section", 1)
    docs._chunks = [_chunk("doc-0", "protocol_section")] * 3   # 同一条重复 3 次
    eng = StudyCorpusEngine(cards, docs, doc_seats=3)
    got = eng.retrieve("q", top_k=2)
    assert [c.chunk_id for c in got] == ["card-0", "card-1", "doc-0"]


def test_retrieve_never_mutates_the_cards_engine_result():
    """`list(...)` 那层拷贝: 组合器往结果里 append doc, 不许改到上游引擎手上的列表。

    今天所有 RAGEngine.retrieve 的 return 都是切片/新建 list (rag.py 的 `cosine[:k]` 一族),
    所以去掉拷贝当下看不出差别 —— 正因如此它需要一条断言, 否则将来有人加一条返回内部
    缓存列表的路径时, cards 引擎会被本类静默污染, 且症状出现在别处。
    """
    class _Aliasing(_Stub):
        def retrieve(self, q, *, top_k=None, **kw):
            self.calls.append(top_k)
            return self._chunks          # 返回内部列表本身, 不是切片

    cards = _Aliasing("card", "field_card", 3)
    eng = StudyCorpusEngine(cards, _Stub("doc", "protocol_section", 3), doc_seats=2)
    eng.retrieve("q", top_k=3)
    assert [c.chunk_id for c in cards._chunks] == ["card-0", "card-1", "card-2"]


def test_format_context_groups_the_two_source_kinds():
    eng, _, _ = _engine(doc_seats=2)
    ctx = eng.format_context(eng.retrieve("q", top_k=3))
    assert "CTX-card(3)" in ctx and "CTX-doc(2)" in ctx
    assert ctx.index("CTX-card(3)") < ctx.index("CTX-doc(2)")
    # 分组标题是 spec §4.2 的交付物本身 (答题方靠它分辨引用的是卡片还是手順書)。
    # 连同前导空行一起钉: 少了 \n\n 则 ## 不在行首, markdown 标题失效。
    assert ctx.startswith("## 【EDC 項目カード】\n")
    assert "\n\n## 【手順書章節】\n" in ctx


def test_format_context_omits_absent_group():
    """只有卡片时不许打出空的手順書小节 (空标题会让答题方以为检索过而没找到)。"""
    eng, _, _ = _engine(doc_seats=0)
    ctx = eng.format_context(eng.retrieve("q", top_k=3))
    assert "CTX-doc" not in ctx
    assert "手順書章節" not in ctx


def test_unknown_file_type_is_grouped_with_cards_never_dropped():
    """未知 file_type 宁可误标进卡片组, 也不许从 context 里消失。

    分组用反选 (`!= DOC_FILE_TYPE`) 而非正选 (`== CARD_FILE_TYPE`) 就是为了这个: 正选下
    file_type=None 的 chunk 两组都不进 = 检索到了却不出现在 context 里, 且完全静默。
    """
    eng, _, _ = _engine(doc_seats=1)
    ctx = eng.format_context([_chunk("u-0", None), _chunk("d-0", "protocol_section")])
    assert "CTX-card(1)" in ctx and "CTX-doc(1)" in ctx


def test_system_prompt_comes_from_cards_engine_never_docs():
    """docs 引擎的 kb_root 指的是 cards/ ⇒ 它的 system_prompt 描述的是卡片库, 用了就是错的。"""
    eng, _, docs = _engine()
    docs.system_prompt = "POISON-must-never-be-read"
    assert "POISON" not in eng.system_prompt
    assert "SYS-card" in eng.system_prompt


def test_system_prompt_names_both_source_kinds_and_keeps_section_numbers():
    """这段规则是唯一告诉答题方"有两类来源、引用要保留節番号"的东西。

    它没了, 答题侧双臂的差值会被误读成席位挤占 (实际是答题方分不清来源)。
    """
    sp = _engine()[0].system_prompt
    assert "【EDC 項目カード】" in sp and "【手順書章節】" in sp
    assert "節番号" in sp


def test_engine_builds_no_messages_of_its_own():
    """答题消息由 FederatedEngine 走 cdisc 引擎产出 (federation.py:148), 本类只被读
    system_prompt (:156/158)。自带一份 build_messages = 零测试守护的死代码; 删掉后
    真有人调它会 AttributeError 响亮失败。全仓 grep 已确认无调用方。
    """
    assert not hasattr(_engine()[0], "build_messages")


def test_negative_doc_seats_fails_loud():
    with pytest.raises(ValueError, match="doc_seats"):
        _engine(doc_seats=-1)


def test_negative_per_call_doc_seats_fails_loud_before_any_retrieval():
    """__init__ 有闸而 per-call 没有 = 同一个非法值走两条路两种结局 (后者静默当 0)。"""
    eng, cards, docs = _engine(doc_seats=5)
    with pytest.raises(ValueError, match="doc_seats"):
        eng.retrieve("q", top_k=15, doc_seats=-1)
    assert cards.calls == [] and docs.calls == []   # 失败要发生在花掉任何一次检索之前


def test_unknown_kwarg_fails_loud_not_silently_swallowed():
    """`**kw` 会把 `doc_seat=8` 这类拼写错吞成默认席位 —— 而席位数是本单元唯一的自变量。

    仓内先例 `_FederatedAdapter.retrieve` (eval/run_eval.py:559) 同样不带 `**kw`;
    联邦从不给 study 引擎传 domain/file_type (federation.py:122/129), 故删掉零风险。
    """
    eng, _, _ = _engine(doc_seats=5)
    with pytest.raises(TypeError):
        eng.retrieve("q", top_k=15, doc_seat=8)
