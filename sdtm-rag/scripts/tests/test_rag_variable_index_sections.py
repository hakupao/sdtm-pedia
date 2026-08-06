"""S1 VARIABLE_INDEX 字面 section 定位 — 映射反建 + 注入契约。

RAGEngine.__new__ + 桩 collection/_search: 不建 Chroma / 不发 embedding。
"""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from server import rag as rag_mod


VI_ABS = "/kb/VARIABLE_INDEX.md"

VI_METAS = [
    {"source": VI_ABS, "section": "§三 CT 交叉引用: C99073"},
    {"source": VI_ABS, "section": "§三 CT 交叉引用: C66742"},
    {"source": VI_ABS, "section": "§一 通用变量: ARM"},
    {"source": VI_ABS, "section": "§一 通用变量: ARMCD"},
    {"source": VI_ABS, "section": "AE — Adverse Events (Events)"},  # 域变量表: 不进表
    {"source": VI_ABS, "section": None},                            # 无 section: 不进表
]


class _FakeCollection:
    def __init__(self, metas):
        self._metas = metas
        self.get_calls = []

    def get(self, where=None, include=None):
        self.get_calls.append(where)
        return {"metadatas": list(self._metas)}


def _engine(metas=VI_METAS):
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng.kb_root = Path("/kb")
    eng.collection = _FakeCollection(metas)
    eng._vi_sections = None
    return eng


def test_map_keys_are_ct_codes_and_variables():
    m = _engine()._vi_section_map()
    assert m["C99073"] == "§三 CT 交叉引用: C99073"
    assert m["ARMCD"] == "§一 通用变量: ARMCD"


def test_domain_table_and_none_sections_excluded():
    m = _engine()._vi_section_map()
    assert set(m) == {"C99073", "C66742", "ARM", "ARMCD"}


def test_map_is_cached_after_first_build():
    eng = _engine()
    eng._vi_section_map()
    eng._vi_section_map()
    assert len(eng.collection.get_calls) == 1


def test_map_query_filters_on_variable_index_source():
    eng = _engine()
    eng._vi_section_map()
    assert eng.collection.get_calls[0] == {"source": str(Path("/kb/VARIABLE_INDEX.md"))}


def test_empty_map_fails_loud():
    # VI 在索引里没有可解析的 section = 索引/命名约定已崩。静默降级会把"检索退化"
    # 伪装成"没有回归" (偏差方向朝下且无声, 任何闸都拦不住), 故必须响亮失败。
    eng = _engine(metas=[{"source": VI_ABS, "section": "AE — Adverse Events (Events)"}])
    with pytest.raises(RuntimeError, match="VARIABLE_INDEX"):
        eng._vi_section_map()


def test_no_chunks_at_all_fails_loud():
    eng = _engine(metas=[])
    with pytest.raises(RuntimeError, match="VARIABLE_INDEX"):
        eng._vi_section_map()


# ---- 注入契约 ---------------------------------------------------------------


def _chunk(cid, source, section=None):
    return SimpleNamespace(chunk_id=cid, source=source, section=section, via_lookup=False)


def _inject_engine(anchors, metas=VI_METAS, search_log=None):
    eng = _engine(metas)
    eng.top_k = 15
    eng._structured_lookup = SimpleNamespace(
        resolve=lambda q: ["VARIABLE_INDEX.md"],
        variable_index_anchors=lambda q: list(anchors),
    )

    def fake_search(query, n, where=None, query_embedding=None):
        if search_log is not None:
            search_log.append((n, where, query_embedding))
        sec = None
        if where and "$and" in where:
            sec = where["$and"][1]["section"]["$eq"]
        if sec and sec in {m.get("section") for m in metas}:
            return [_chunk(f"vi:{sec}", VI_ABS, sec)]
        if where and "source" in where:          # _lookup_chunks_for_file 回落路径
            return [_chunk("vi:cosine", VI_ABS, "§三 CT 交叉引用: C66734")]
        return []

    eng._search = fake_search
    return eng


def test_ct_anchor_injects_exact_section():
    log = []
    eng = _inject_engine(["C99073"], search_log=log)
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=[0.1])
    assert [c.chunk_id for c in out] == ["vi:§三 CT 交叉引用: C99073"]
    assert out[0].via_lookup
    assert log[0][0] == 1
    assert log[0][1] == {"$and": [{"source": {"$eq": str(Path(VI_ABS))}},
                                  {"section": {"$eq": "§三 CT 交叉引用: C99073"}}]}
    assert log[0][2] == [0.1]      # 复用已算好的 embedding, 零新增 round-trip


def test_two_anchors_inject_two_sections():
    # q107 形态: ARM + ARMCD 各注一块 (今天的单块注入天然给不出两节)
    eng = _inject_engine(["ARM", "ARMCD"])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.section for c in out] == ["§一 通用变量: ARM", "§一 通用变量: ARMCD"]


def test_unknown_anchor_skipped_others_still_injected():
    eng = _inject_engine(["C00000", "C99073"])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.section for c in out] == ["§三 CT 交叉引用: C99073"]


def test_no_anchor_falls_back_to_cosine_chunk():
    eng = _inject_engine([])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.chunk_id for c in out] == ["vi:cosine"]


def test_all_anchors_miss_falls_back_to_cosine_chunk():
    eng = _inject_engine(["C00000"])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.chunk_id for c in out] == ["vi:cosine"]


def test_non_vi_target_unaffected():
    # 非 VI target 逐字节走原路径: 不查 section 映射, 不发 $and 过滤
    log = []
    eng = _inject_engine(["C99073"], search_log=log)
    eng._structured_lookup = SimpleNamespace(
        resolve=lambda q: ["domains/DM/spec.md"],
        variable_index_anchors=lambda q: ["C99073"],
    )
    eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert all("$and" not in (w or {}) for _n, w, _e in log)


def test_injected_chunks_lead_and_cosine_tail_preserved():
    eng = _inject_engine(["C99073"])
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_structured_lookup("q", cosine, where=None, k=15, query_embedding=None)
    assert out[0].chunk_id == "vi:§三 CT 交叉引用: C99073"
    assert [c.chunk_id for c in out[1:]] == [f"c{i}" for i in range(14)]
