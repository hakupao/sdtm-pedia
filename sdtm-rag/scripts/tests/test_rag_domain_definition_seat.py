"""DM1 D2: 域级定义保底席 —— S1 命中域且问法是域级时, 该域 assumptions.md 的定义块
(section item_1, 回落 overview) 占注入首席。

embedding-free: 用假 collection + 假 _lookup_chunks_for_file, 只测席位算术与选块规则,
不碰 chroma / OpenAI。
"""
from pathlib import Path

import server.rag as rag_mod
from server.rag import RetrievedChunk

KB = Path("/kb")
ABS = str((KB / "domains/DS/assumptions.md").resolve())


class _FakeCollection:
    def __init__(self, rows):
        self.rows = rows  # list of (id, doc, meta)

    def get(self, where=None, include=None, **_):
        def ok(meta):
            conds = where.get("$and", [where]) if where else []
            return all(meta.get(k) == v for c in conds for k, v in c.items())

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


def test_file_type_filter_other_than_assumptions_skips_seat():
    eng = _engine(ROWS)

    class _SL:
        _MAX_DOMAIN_SPECS = 3

        def resolve(self, q):
            return ["domains/DS/spec.md"]

        def domain_definition_targets(self, q):
            return ["domains/DS/assumptions.md"]

    eng._structured_lookup = _SL()
    eng._lookup_chunks_for_file = lambda query, rel_path, n, query_embedding=None: [_chunk(f"{rel_path}#{i}") for i in range(n)]
    eng._lookup_chunks_for_variable_index = lambda *a, **k: []
    out = eng._apply_structured_lookup("q DS domain", [_chunk("c")], {"file_type": "spec"}, 15)
    assert all("assumptions" not in c.chunk_id for c in out)
