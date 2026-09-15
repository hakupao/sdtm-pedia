"""DM1 D3: 域码确定性扩写 —— 只喂 dense/BM25, 不改 LLM 看见的问题。

embedding-free: 扩写器本身只读 meta.yaml + StructuredLookup 的域识别 (零 chroma、零
OpenAI); `retrieve` 的接线用假引擎 (`__new__` + stub 检索方法) 测"谁拿到扩写文本"。
"""
from pathlib import Path

import pytest

import server.rag as rag_mod
from server.config import settings
from server.domain_expand import DomainExpander
from server.meta_store import MetaStore
from server.structured_lookup import StructuredLookup

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"


@pytest.fixture(scope="module")
def expander():
    store = MetaStore(settings.meta_path)
    return DomainExpander(store, StructuredLookup(KB_ROOT, store))


def test_ds_lowercase_expands_with_the_domain_label(expander):
    q = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
    out = expander.expand(q)
    assert out.startswith(q)
    assert "Disposition" in out  # from meta.yaml label field


def test_the_record_structure_is_never_appended(expander):
    """attempt 1 追加过 meta.yaml 的 `structure`, 实测 140q 的 q47 从 recall 1.0 掉到
    0.5 —— "One record per ... per subject" 是**跨域通用**的记录粒度模板, 追加它会让
    "讲记录粒度的块"整体上浮, 挤掉问句真正问的那条
    (evidence/failures/dm1_task5_attempt_1.md)。把那次回归钉成不变量。"""
    q = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
    out = expander.expand(q)
    assert "protocol milestone" not in out
    assert "One record per" not in out


def test_no_domain_returns_query_unchanged(expander):
    q = "What does AETERM contain?"
    assert expander.expand(q) == q


def test_expansion_is_capped_and_deterministic(expander):
    """5 个域码只追加前 3 个的 label。数"("那种写法在 label-only 下恒为 0, 量不到任何
    东西 —— 这里改成点名第 4/5 个域的 label 必须缺席。"""
    q = "compare AE, CM, EX, LB and VS for our study"
    a, b = expander.expand(q), expander.expand(q)
    assert a == b
    assert "Adverse Events" in a and "Exposure" in a          # 前 3 个 (AE, CM, EX)
    assert "Laboratory Test Results" not in a                 # 第 4 个 (LB)
    assert "Vital Signs" not in a                             # 第 5 个 (VS)


def test_expansion_never_adds_uppercase_variable_tokens(expander):
    """The appended text must not create new S1 variable hits if someone feeds it
    back into resolve(): labels/structures are prose, but guard the invariant."""
    import re
    q = "what belongs in the DS domain"
    extra = expander.expand(q)[len(q):]
    assert not re.search(r"\b[A-Z][A-Z0-9]{2,}\b", extra)


def test_unknown_domain_code_is_skipped_not_crashed(expander, monkeypatch):
    """`MetaStore.domain_info` 返回 `dict | None`。识别与 meta 表由两份数据驱动
    (domain_to_spec 来自 KB 目录, domain_info 来自 meta.yaml), 只要有一天一边有而
    另一边没有, 无保护的 `info.get(...)` 就是请求期 AttributeError。"""
    monkeypatch.setattr(expander._lookup, "_query_domains", lambda q: ["ZZ"])
    q = "what belongs in the ZZ domain"
    assert expander.expand(q) == q


# ───────────────────────── retrieve 接线 (谁拿到扩写文本) ─────────────────────────

class _RecordingEngine:
    """RAGEngine 的最小可跑壳: 记录每个检索入口实际收到的 query 文本。"""

    def __init__(self, expander, *, hybrid=True, structured=True):
        eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
        eng.top_k = 5
        eng.kb_root = Path("/kb")
        eng.query_expansion = "none"
        eng.hybrid_enabled = hybrid
        eng.hybrid_pool = 30
        eng.hybrid_fusion = "rrf"
        eng.rerank_enabled = False
        eng.rerank_candidates = 100
        eng.domain_expander = expander
        eng._structured_lookup = object() if structured else None
        eng._study_lookup = None
        self.seen: dict[str, str] = {}
        eng._embed_query = lambda q: self.seen.setdefault("embed", q) and [0.0]
        eng._search = lambda q, k, where, query_embedding=None: (
            self.seen.setdefault("dense", q), [])[1]
        eng._bm25_search = lambda q, k, where: (self.seen.setdefault("bm25", q), [])[1]
        eng._hybrid_fuse = lambda d, b, k: []
        eng._build_where = lambda d, f: None
        eng._apply_structured_lookup = lambda q, cosine, where, k, query_embedding=None: (
            self.seen.setdefault("s1", q), [])[1]
        self.eng = eng


QUERY = "what belongs in the DS domain"


def test_dense_and_bm25_see_the_expanded_query(expander):
    r = _RecordingEngine(expander)
    r.eng.retrieve(QUERY)
    assert r.seen["dense"].startswith(QUERY) and "Disposition" in r.seen["dense"]
    assert r.seen["bm25"] == r.seen["dense"]


def test_the_precomputed_embedding_is_of_the_text_actually_searched(expander):
    """向量与 `_search` 的文本必须同源。不同源时症状是静默的: 稠密检索按原问题的向量
    跑, 而屏幕/落盘都显示扩写开着。"""
    r = _RecordingEngine(expander)
    r.eng.retrieve(QUERY)
    assert r.seen["embed"] == r.seen["dense"]


def test_structured_lookup_still_sees_the_original_query(expander):
    """S1 的 resolve 是 token 级的; 追加的英文散文会造出新的域/长名命中。"""
    r = _RecordingEngine(expander)
    r.eng.retrieve(QUERY)
    assert r.seen["s1"] == QUERY


def test_no_expander_leaves_every_entry_point_on_the_original(expander):
    r = _RecordingEngine(None)
    r.eng.retrieve(QUERY)
    assert set(r.seen.values()) == {QUERY}
