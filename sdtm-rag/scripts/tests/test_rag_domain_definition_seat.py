"""DM1 D2: 域级定义保底席 —— S1 命中域且问法是域级时, 该域 assumptions.md 的定义块
(section item_1, 回落 overview) 占注入首席。

embedding-free: 用假 collection + 假 _lookup_chunks_for_file, 只测席位算术与选块规则,
不碰 chroma / OpenAI。
"""
from pathlib import Path

import pytest

import server.rag as rag_mod
from server.rag import RetrievedChunk

KB = Path("/kb")
ABS = str((KB / "domains/DS/assumptions.md").resolve())


class _FakeCollection:
    def __init__(self, rows):
        self.rows = rows  # list of (id, doc, meta)

    def get(self, where=None, include=None, **_):
        def val(v):
            # chroma 的 {"$eq": x} 与裸 x 等价 (见 rag.py:648-649 的既有写法)
            return v["$eq"] if isinstance(v, dict) and "$eq" in v else v

        def ok(meta):
            conds = where.get("$and", [where]) if where else []
            return all(meta.get(k) == val(v) for c in conds for k, v in c.items())

        sel = [r for r in self.rows if ok(r[2])]
        return {"ids": [r[0] for r in sel], "documents": [r[1] for r in sel],
                "metadatas": [r[2] for r in sel]}


def _engine(rows):
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng.kb_root = KB
    eng.collection = _FakeCollection(rows)
    eng.domain_definition_seat = True
    return eng


def _chunk(cid, text="x", **meta):
    return RetrievedChunk(chunk_id=cid, source=meta.get("source", "s"), domain=meta.get("domain"),
                          file_type=meta.get("file_type"), section=meta.get("section"),
                          similarity=0.5, text=text)


ROWS = [
    ("domains/DS/assumptions.md#0", "DS — Assumptions", {"source": ABS, "domain": "DS", "file_type": "assumptions", "section": "overview"}),
    ("domains/DS/assumptions.md#1", "The Disposition (DS) dataset provides an accounting ...", {"source": ABS, "domain": "DS", "file_type": "assumptions", "section": "item_1"}),
]


def test_definition_chunk_prefers_item_1():
    ch = _engine(ROWS)._definition_chunk("domains/DS/assumptions.md")
    assert ch.chunk_id == "domains/DS/assumptions.md#1" and ch.via_lookup and ch.section == "item_1"


def test_definition_chunk_falls_back_to_overview():
    ch = _engine(ROWS[:1])._definition_chunk("domains/DS/assumptions.md")
    assert ch.chunk_id == "domains/DS/assumptions.md#0"


def test_definition_chunk_none_when_file_has_no_chunks():
    assert _engine([])._definition_chunk("domains/DS/assumptions.md") is None


def test_single_spec_seat_count_is_unchanged(monkeypatch):
    """1 definition + (N-1) spec rows == N seats: the seat comes out of S1's own quota."""
    eng = _engine(ROWS)

    class _SL:
        _MAX_DOMAIN_SPECS = 3

        def resolve(self, q):
            return ["domains/DS/spec.md"]

        def domain_definition_targets(self, q):
            return ["domains/DS/assumptions.md"]

    eng._structured_lookup = _SL()
    seen = {}

    def fake_file_lookup(query, rel_path, n, query_embedding=None):
        seen["n"] = n
        return [_chunk(f"{rel_path}#{i}", source=rel_path) for i in range(n)]

    eng._lookup_chunks_for_file = fake_file_lookup
    eng._lookup_chunks_for_variable_index = lambda *a, **k: []
    cosine = [_chunk(f"c{i}") for i in range(20)]
    out = eng._apply_structured_lookup("哪些数据进 DS domain", cosine, None, 15)
    assert seen["n"] == rag_mod.RAGEngine._SINGLE_DOMAIN_SPEC_CHUNKS - 1
    assert out[0].chunk_id == "domains/DS/assumptions.md#1"
    assert sum(c.via_lookup for c in out) == rag_mod.RAGEngine._SINGLE_DOMAIN_SPEC_CHUNKS
    assert len(out) == 15


class _SL:
    _MAX_DOMAIN_SPECS = 3

    def resolve(self, q):
        return ["domains/DS/spec.md"]

    def domain_definition_targets(self, q):
        return ["domains/DS/assumptions.md"]


def _seat_engine():
    eng = _engine(ROWS)
    eng._structured_lookup = _SL()
    eng._lookup_chunks_for_file = lambda query, rel_path, n, query_embedding=None: [
        _chunk(f"{rel_path}#{i}") for i in range(n)
    ]
    eng._lookup_chunks_for_variable_index = lambda *a, **k: []
    return eng


@pytest.mark.parametrize("where", [
    {"file_type": "spec"},                                    # 单过滤器 -> 扁平 (_build_where)
    {"file_type": {"$eq": "spec"}},                           # 扁平 + $eq
    {"$and": [{"domain": "DS"}, {"file_type": "spec"}]},      # 双过滤器 -> $and (_build_where)
    {"$and": [{"domain": {"$eq": "DS"}},
              {"file_type": {"$eq": "spec"}}]},               # $and + $eq
])
def test_file_type_filter_other_than_assumptions_skips_seat(where):
    """T4 fix 4: 守卫必须看穿 `_build_where` 的**两种**形状。

    分辨力: 只读扁平 `where["file_type"]` 的实现在后两个 `$and` 参数上会漏读成 None,
    于是把 assumptions 注进一个明确只要 spec 的检索里 —— 静默违反调用方的过滤器。
    """
    out = _seat_engine()._apply_structured_lookup("q DS domain", [_chunk("c")], where, 15)
    assert all("assumptions" not in c.chunk_id for c in out)


@pytest.mark.parametrize("where", [
    None,
    {"domain": "DS"},                                   # 有过滤器但不是 file_type
    {"file_type": "assumptions"},
    {"$and": [{"domain": "DS"}, {"file_type": "assumptions"}]},
])
def test_seat_still_fires_when_file_type_allows_assumptions(where):
    out = _seat_engine()._apply_structured_lookup("q DS domain", [_chunk("c")], where, 15)
    assert out[0].chunk_id == "domains/DS/assumptions.md#1"


@pytest.mark.parametrize("where,expected", [
    (None, None),
    ({}, None),
    ({"domain": "DS"}, None),
    ({"file_type": "spec"}, "spec"),
    ({"file_type": {"$eq": "spec"}}, "spec"),
    ({"$and": [{"domain": "DS"}, {"file_type": "spec"}]}, "spec"),
    ({"$and": [{"domain": {"$eq": "DS"}}, {"file_type": {"$eq": "spec"}}]}, "spec"),
    ({"$and": [{"domain": "DS"}]}, None),
])
def test_where_file_type_reads_both_shapes(where, expected):
    assert rag_mod.RAGEngine._where_file_type(where) == expected


def test_definition_chunk_source_is_kb_relative():
    """T4 fix 2: source 必须与 `_search` / `_bm25_search` 同口径归一化成 KB 相对路径。

    分辨力: 直接用元数据里的绝对路径会让本机路径漏进引用头 / API sources / 落盘报告。
    """
    ch = _engine(ROWS)._definition_chunk("domains/DS/assumptions.md")
    assert ch.source == "domains/DS/assumptions.md"
    assert not ch.source.startswith("/")


def test_seat_flag_off_skips_seat():
    eng = _seat_engine()
    eng.domain_definition_seat = False
    out = eng._apply_structured_lookup("q DS domain", [_chunk("c")], None, 15)
    assert all("assumptions" not in c.chunk_id for c in out)
