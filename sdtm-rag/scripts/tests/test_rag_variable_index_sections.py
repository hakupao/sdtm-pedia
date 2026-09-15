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
    eng.domain_definition_seat = True
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


def test_one_family_lost_fails_loud():
    """审查 HIGH-2: 只判 `not mapping` 会放过"一族改名"这个真会发生的情况。

    §一 与 §三 的 section 串由 chunkers/variable_index.py 两段独立代码生成, 只改一族
    完全现实。若 §一 变成没有 ": " 的形态, 24 个变量键全丢而 135 个 CT 键还在 → 非空
    → 不 raise → 变量锚点题静默回落 cosine, 分数无声退回改动前。"""
    ct_only = [{"source": VI_ABS, "section": "§三 CT 交叉引用: C99073"},
               {"source": VI_ABS, "section": "### ARM (Common Variable)"}]  # §一 改名后
    with pytest.raises(RuntimeError, match="两族"):
        _engine(metas=ct_only)._vi_section_map()

    var_only = [{"source": VI_ABS, "section": "§一 通用变量: ARM"}]
    with pytest.raises(RuntimeError, match="两族"):
        _engine(metas=var_only)._vi_section_map()


def test_duplicate_token_fails_loud():
    # 同尾 token 的两个 section = 命名约定歧义; Chroma get() 无顺序保证, 静默取第一个
    # 会让"选中哪个"随版本漂移 (审查 LOW-2)。
    dup = VI_METAS + [{"source": VI_ABS, "section": "§四 别的什么: C99073"}]
    with pytest.raises(RuntimeError, match="C99073"):
        _engine(metas=dup)._vi_section_map()


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
        # DM1 D2: 这些用例的问句不点名任何域 → 定义保底席不 fire (真实 lookup 同)
        domain_definition_targets=lambda q: [],
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
        domain_definition_targets=lambda q: [],
    )
    eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert all("$and" not in (w or {}) for _n, w, _e in log)


def test_unresolvable_anchors_do_not_consume_the_cap():
    """规则 A 抽检 D-1: 上限必须施加在 section 解析**之后**。

    known_variables 有 ~1500 个变量, VI §一 只有 24 个有 section。先截前 N 的话, 题面
    顺带提到的无 VI 条目变量会白占名额 —— 实证形态: q107 题面加一句 "our EXDOSU and
    CMDOSU mappings aside" 就把 ARMCD 挤出字面通道 (那次 recall 仍 1.00 只因 hybrid
    偶然捞回, 而该题改动前基线正是 0.50, 说明这条兜底不可靠)。"""
    eng = _inject_engine(["EXDOSU", "CMDOSU", "ARM", "ARMCD"])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.section for c in out] == ["§一 通用变量: ARM", "§一 通用变量: ARMCD"]


def test_cap_keeps_the_first_resolvable_sections_in_order():
    # 超上限时活下来的必须是**能解出 section 的前 N 个**, 不是"原锚点列表的前 N 个"。
    # 旧测试只断言 len==3, 正好是 D-1 的盲区。
    eng = _inject_engine(["ZZZ1", "C99073", "ZZZ2", "C66742", "ARM", "ARMCD"])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.section for c in out] == [
        "§三 CT 交叉引用: C99073", "§三 CT 交叉引用: C66742", "§一 通用变量: ARM",
    ]
    assert len(out) == rag_mod.RAGEngine._MAX_VI_SECTIONS


def test_injected_chunks_lead_and_cosine_tail_preserved():
    eng = _inject_engine(["C99073"])
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_structured_lookup("q", cosine, where=None, k=15, query_embedding=None)
    assert out[0].chunk_id == "vi:§三 CT 交叉引用: C99073"
    assert [c.chunk_id for c in out[1:]] == [f"c{i}" for i in range(14)]


def test_broken_map_does_not_break_the_no_anchor_path():
    """审查 MEDIUM-3: 无锚点时绝不能碰映射表。

    "fail-loud 不伤正常流量" 整个压在 `if not anchors:` 的早退上。若有人把
    `section_map = self._vi_section_map()` 上提到早退之前, 用健康 metas 的那条回落测试
    照样绿, 而生产会对每道无锚点 VI 题 raise。这里用一个建不出表的索引锁住它。"""
    eng = _inject_engine([], metas=[])
    out = eng._apply_structured_lookup("q", [], where=None, k=15, query_embedding=None)
    assert [c.chunk_id for c in out] == ["vi:cosine"]


# ---- KB <-> 索引漂移闸 (审查 HIGH-2 的 CI 半边) -------------------------------


def test_vi_section_map_matches_chunker_output():
    """映射表的键必须与 chunker 从 KB 实际生成的 §一/§三 section 一一对应。

    唯一事实源是 scripts/chunkers/variable_index.py —— 这里不硬编码 135/24, 而是现场
    跑 chunker 再比对, 所以 KB 增删 CT 码不会误报, 而任一族的 section 命名漂移会当场红。
    计划里那条一次性 shell 验证 (total=159 ct=135 var=24) 不在 CI 里, 不会再跑; 这条是
    它的常驻替身。"""
    import chromadb

    from scripts.chunkers.variable_index import VariableIndexChunker
    from server.config import settings

    kb_root = Path(settings.kb_root)
    vi_path = kb_root / "VARIABLE_INDEX.md"
    expected = {
        c.section.rsplit(": ", 1)[1].strip(): c.section
        for c in VariableIndexChunker(kb_root).chunk(vi_path)
        if c.section and ": " in c.section
    }

    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng.kb_root = kb_root
    try:
        eng.collection = chromadb.PersistentClient(
            path=str(settings.chroma_dir)).get_collection(settings.collection_name)
    except Exception:  # noqa: BLE001 — 打不开库的原因不重要, 都是"本机没索引"
        # data/chroma 被 gitignore 且本仓无 CI, 所以 clone 出来的机器上这条会红得
        # 莫名其妙 —— 而"红了不用管"一旦被学会, 这条闸就白设了。只在**打不开库**时
        # skip; 下面的 assert 本身绝不 skip, 任何能跑服务的机器上闸全效。
        pytest.skip("本机无索引; 跑 .venv/bin/python -m scripts.ingest 后此闸才生效")
    eng._vi_sections = None

    assert eng._vi_section_map() == expected, (
        "VARIABLE_INDEX 的 section 命名在 chunker 与索引之间漂移了 —— "
        "重灌索引 (scripts/ingest.py), 或 S1 字面通道会静默回落 cosine"
    )
