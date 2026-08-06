# S1 VARIABLE_INDEX 字面 section 定位 — 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 让 S1 在 `VARIABLE_INDEX.md` 内部按题面点名的 CT 码 / 变量名**字面定位 section**, 取代今天的文件内 cosine 选块, 修掉 section 级判据暴露的 4 道假命中 + 1 道半命中。

**Architecture:** 锚点抽取放 `StructuredLookup` (纯字符串, 无索引依赖); 锚点→section 的映射由 `RAGEngine` 在首次使用时**从 Chroma 元数据反建**并缓存 (不拼格式串); 注入走 `{"$and": [source, section]}` 精确过滤, 复用已算好的 query embedding。任一环节落空 → 回落今天的 cosine 选块; 映射表整个建不出来 → fail-loud。

**Tech Stack:** Python 3.12 · Chroma (PersistentClient) · pytest · `sdtm-rag/.venv`

## Global Constraints

- 工作目录一律 `sdtm-rag/`; Python 一律 `.venv/bin/python` (不用系统 python)。
- 覆盖 `§一 通用变量: <VAR>` 与 `§三 CT 交叉引用: C<code>` 两族; **域变量表 (`AE — Adverse Events (Events)` 形态, 63 块) 不做**。
- 新通道**只能赢不能输**: 锚点解不出 / section 不在索引 → 逐字节回落 `_lookup_chunks_for_file` 今日行为。
- **零新增 embedding round-trip**: 所有 `_search` 调用必须透传 `query_embedding`。
- 非 `VARIABLE_INDEX.md` 的 target 行为**逐字节不变**。
- 锚点注入上限 3 (`_MAX_VI_ANCHORS`)。
- 验收口径两个数, **不接受"总分没掉"**: 18 题子集 75.00% → 100.00% + 其余 122 题逐位 Δ0。全集上限 98.57% (q38/q126 不在范围)。
- 规则 D: 实现 / 审查 / 抽检三方各用不同 `subagent_type`, 不自审。
- 写"实测"必须附可复跑的一行命令。

---

### Task 1: 锚点抽取 (`StructuredLookup.variable_index_anchors`)

**Files:**
- Modify: `server/structured_lookup.py` (类常量区 ~179 行; `resolve` 之前的 `# ---- resolve ----` 段内新增方法)
- Test: `scripts/tests/test_structured_lookup.py`

**Interfaces:**
- Consumes: 既有 `_QUERY_CT_RE` (`server/structured_lookup.py:59`)、`_query_variables` (`:333`)。
- Produces: `StructuredLookup.variable_index_anchors(query: str) -> list[str]` — 返回**锚点 token**
  (如 `["C99073"]`、`["ARM", "ARMCD"]`), **不是 section 串**; CT 码在前、变量在后, 去重保序,
  最多 `StructuredLookup._MAX_VI_ANCHORS` (=3) 个。无锚点返回 `[]`。
- Produces: `StructuredLookup._MAX_VI_ANCHORS = 3`

- [ ] **Step 1: 写失败测试**

追加到 `scripts/tests/test_structured_lookup.py` 末尾:

```python
# ---- VI 锚点抽取 (S1 字面 section 定位) --------------------------------------

class TestVariableIndexAnchors:
    def test_ct_code_anchor(self, lookup):
        assert lookup.variable_index_anchors(
            "Which domains use codelist C99073 for laterality?"
        ) == ["C99073"]

    def test_variable_anchor(self, lookup):
        assert lookup.variable_index_anchors(
            "In how many domains does TAETORD appear?"
        ) == ["TAETORD"]

    def test_ct_codes_come_before_variables(self, lookup):
        # 混合题: CT 码是更具体的锚点, 必须排在变量前 (否则 3 个名额可能被变量占满)
        out = lookup.variable_index_anchors(
            "Which domains share codelist C66742 through the RDOMAIN variable?"
        )
        assert out[0] == "C66742"
        assert "RDOMAIN" in out

    def test_two_variable_anchors_preserved(self, lookup):
        # q107 形态: 一题要两节 (ARM + ARMCD), 这正是"1 文件只注 1 块"限制的解除点
        out = lookup.variable_index_anchors("What are the labels of ARM and ARMCD?")
        assert "ARM" in out and "ARMCD" in out

    def test_dedup_preserves_order(self, lookup):
        assert lookup.variable_index_anchors(
            "codelist C66742 and again C66742"
        ) == ["C66742"]

    def test_capped_at_max(self, lookup):
        out = lookup.variable_index_anchors(
            "codelists C66742, C66734, C99073, C78735 and C71620"
        )
        assert len(out) == StructuredLookup._MAX_VI_ANCHORS

    def test_no_anchor_returns_empty(self, lookup):
        assert lookup.variable_index_anchors("What is an SDTM domain?") == []

    def test_unknown_variable_token_is_not_an_anchor(self, lookup):
        # 未知大写 token 不是变量 → 不得当锚点 (否则会去查一个不存在的 section)
        assert lookup.variable_index_anchors("What does ZZZQQQ mean?") == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py::TestVariableIndexAnchors -v`
Expected: FAIL — `AttributeError: 'StructuredLookup' object has no attribute 'variable_index_anchors'`

- [ ] **Step 3: 最小实现**

在 `server/structured_lookup.py` 的 `_MAX_DOMAIN_SPECS = 3` 下方加常量:

```python
    # Cap on VARIABLE_INDEX sections union-added from one query. Same value as
    # _MAX_DOMAIN_SPECS: with top_k=15, three injected chunks leave the cosine
    # tail intact. A question naming five codelists must not flood the merge.
    _MAX_VI_ANCHORS = 3
```

在 `resolve` 方法之前加:

```python
    def variable_index_anchors(self, query: str) -> list[str]:
        """VARIABLE_INDEX 内部定位用的**字面锚点** (CT 码 + 已知变量名), CT 码在前,
        去重保序, 截到 _MAX_VI_ANCHORS。

        返回的是 token 而非 section 串: section 的命名格式只有索引自己知道, 在这里拼
        格式串等于把同一份格式定义写两遍 (chunker 改名时会静默全 miss)。映射交给
        RAGEngine 从索引反建。无锚点时返回 [] → 调用方回落 cosine 选块。"""
        anchors: list[str] = []
        for tok in _QUERY_CT_RE.findall(query) + self._query_variables(query):
            if tok not in anchors:
                anchors.append(tok)
        return anchors[: self._MAX_VI_ANCHORS]
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -v`
Expected: 全部 PASS (新增 8 条 + 既有全绿)

- [ ] **Step 5: 提交**

```bash
git add sdtm-rag/server/structured_lookup.py sdtm-rag/scripts/tests/test_structured_lookup.py
git commit -m "feat(s1): VARIABLE_INDEX 字面锚点抽取 (CT 码 + 变量名, 上限 3)"
```

---

### Task 2: 锚点→section 映射从索引反建 (`RAGEngine._vi_section_map`)

**Files:**
- Modify: `server/rag.py` (类常量区 `:43-46`; `_lookup_chunks_for_file` `:401` 附近新增方法)
- Test: `scripts/tests/test_rag_variable_index_sections.py` (Create)

**Interfaces:**
- Consumes: `self.collection` (Chroma collection)、`self.kb_root`。
- Produces: `RAGEngine._VARIABLE_INDEX_REL = "VARIABLE_INDEX.md"`
- Produces: `RAGEngine._vi_section_map() -> dict[str, str]` — `锚点 token -> section 全名`,
  首次调用后缓存在 `self._vi_sections`。表建不出来时 `raise RuntimeError`。

**反建规则 (只假设"section 以 `: <TOKEN>` 结尾", 不假设中文前缀):**
取 section 最后一个 `": "` 之后的部分:
- 匹配 `^C\d{4,6}$` → CT 码键 (`§三 CT 交叉引用: C99073` → `C99073`)
- 匹配 `^[A-Z][A-Z0-9]{1,}$` → 变量键 (`§一 通用变量: STUDYID` → `STUDYID`)
- 其余 (域变量表 `AE — Adverse Events (Events)` 无 `": "`) → 跳过

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_rag_variable_index_sections.py`:

```python
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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_rag_variable_index_sections.py -v`
Expected: FAIL — `AttributeError: ... '_vi_section_map'`

- [ ] **Step 3: 最小实现**

`server/rag.py` 顶部 import 区确认有 `import re` (没有则加)。类常量区 `_STUDY_MAX_CARDS` 下方加:

```python
    _VARIABLE_INDEX_REL = "VARIABLE_INDEX.md"

    # VARIABLE_INDEX 的 section 尾部 token: `§三 CT 交叉引用: C99073` -> C99073,
    # `§一 通用变量: STUDYID` -> STUDYID。域变量表 (`AE — Adverse Events (Events)`)
    # 没有 ": " 尾部, 自然落选 —— 那族由 domains/<CODE>/spec.md 通道承接。
    _VI_ANCHOR_RE = re.compile(r"^(C\d{4,6}|[A-Z][A-Z0-9]{1,})$")
```

`__init__` 里 `self._structured_lookup = None` 附近加一行缓存位:

```python
        self._vi_sections: dict[str, str] | None = None
```

`_lookup_chunks_for_file` 之前加方法:

```python
    def _vi_section_map(self) -> dict[str, str]:
        """`锚点 token -> VARIABLE_INDEX 的 section 全名`, 从索引元数据反建并缓存。

        不拼格式串: section 的命名只有 ingest 侧知道, 拼串等于把同一份格式定义写两遍,
        chunker 改名时新通道会静默全 miss 并回落 cosine —— 分数无声退回改动前, 任何闸
        都拦不住。这里只假设 section 以 `: <TOKEN>` 结尾, 并从实际索引取值。"""
        if self._vi_sections is not None:
            return self._vi_sections

        abs_source = str((self.kb_root / self._VARIABLE_INDEX_REL).resolve())
        rows = self.collection.get(where={"source": abs_source}, include=["metadatas"])
        mapping: dict[str, str] = {}
        for meta in rows.get("metadatas") or []:
            section = (meta or {}).get("section")
            if not section or ": " not in section:
                continue
            token = section.rsplit(": ", 1)[1].strip()
            if self._VI_ANCHOR_RE.match(token):
                mapping.setdefault(token, section)

        if not mapping:
            raise RuntimeError(
                f"VARIABLE_INDEX section map is empty ({abs_source}) — 索引缺该文件, "
                "或 ingest 侧 section 命名已改。静默回落 cosine 会把检索退化伪装成无回归。"
            )
        self._vi_sections = mapping
        return mapping
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_rag_variable_index_sections.py -v`
Expected: 6 passed

- [ ] **Step 5: 对真索引验证反建结果 (实测, 附命令)**

Run:
```bash
.venv/bin/python - <<'PY'
from pathlib import Path
import chromadb
from server.config import settings
from server.rag import RAGEngine
eng = RAGEngine.__new__(RAGEngine)
eng.kb_root = Path(settings.kb_root)
eng.collection = chromadb.PersistentClient(
    path=str(settings.chroma_dir)).get_collection(settings.collection_name)
eng._vi_sections = None
m = eng._vi_section_map()
ct = {k for k in m if k.startswith("C") and k[1:].isdigit()}
print(f"total={len(m)} ct={len(ct)} var={len(m) - len(ct)}")
assert len(ct) == 135 and len(m) - len(ct) == 24, "与索引实测 135 CT + 24 变量不符"
print("OK", m["C99073"], "|", m["ARMCD"])
PY
```
Expected: `total=159 ct=135 var=24` + `OK §三 CT 交叉引用: C99073 | §一 通用变量: ARMCD`
(135 / 24 两个数来自本轮索引实测: `VI 222 chunk = §三 135 + §一 24 + 域变量表 63`。)

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/server/rag.py sdtm-rag/scripts/tests/test_rag_variable_index_sections.py
git commit -m "feat(s1): VARIABLE_INDEX section 映射从索引反建 (空表 fail-loud)"
```

---

### Task 3: 注入路径接线 (`_apply_structured_lookup` 走字面通道)

**Files:**
- Modify: `server/rag.py:309-349` (`_apply_structured_lookup`) + 新增 `_lookup_chunks_for_variable_index`
- Test: `scripts/tests/test_rag_variable_index_sections.py` (追加)

**Interfaces:**
- Consumes: Task 1 的 `variable_index_anchors`、Task 2 的 `_vi_section_map`、既有 `_search` / `_lookup_chunks_for_file` / `_merge_lookup_first`。
- Produces: `RAGEngine._lookup_chunks_for_variable_index(query, query_embedding) -> list[RetrievedChunk]`

- [ ] **Step 1: 写失败测试**

追加到 `scripts/tests/test_rag_variable_index_sections.py`:

```python
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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_rag_variable_index_sections.py -v`
Expected: 新增 7 条 FAIL (旧 6 条仍 PASS)

- [ ] **Step 3: 最小实现**

`server/rag.py` 的 `_apply_structured_lookup` 循环体改为 (只加 VI 分支, 其余不动):

```python
        lookup_chunks: list[RetrievedChunk] = []
        for rel_path in targets:
            if rel_path == self._VARIABLE_INDEX_REL:
                chunks = self._lookup_chunks_for_variable_index(
                    query, query_embedding=query_embedding
                )
            else:
                n = self._SINGLE_DOMAIN_SPEC_CHUNKS if single_spec else 1
                chunks = self._lookup_chunks_for_file(
                    query, rel_path, n, query_embedding=query_embedding
                )
            for chunk in chunks:
                chunk.via_lookup = True
                lookup_chunks.append(chunk)
```

新增方法 (放在 `_lookup_chunks_for_file` 之后):

```python
    def _lookup_chunks_for_variable_index(
        self, query: str, query_embedding: list[float] | None = None
    ) -> list[RetrievedChunk]:
        """VARIABLE_INDEX 内部按题面点名的 CT 码 / 变量名**字面**取 section。

        该文件的 222 个 chunk 是极短结构化单行, 对自然语言问句的 embedding 相似度近似
        噪声 —— 文件内 cosine 选块实测基本随机 (4 道题完全打偏)。题面已经点名了码, 不必猜。

        新通道只能赢不能输: 锚点解不出 / 该 section 不在索引 → 回落原来的 cosine 选块。"""
        anchors = self._structured_lookup.variable_index_anchors(query)
        if not anchors:
            return self._lookup_chunks_for_file(
                query, self._VARIABLE_INDEX_REL, 1, query_embedding=query_embedding
            )

        abs_source = str((self.kb_root / self._VARIABLE_INDEX_REL).resolve())
        section_map = self._vi_section_map()
        out: list[RetrievedChunk] = []
        for anchor in anchors:
            section = section_map.get(anchor)
            if section is None:
                continue
            out.extend(self._search(
                query, 1,
                {"$and": [{"source": {"$eq": abs_source}},
                          {"section": {"$eq": section}}]},
                query_embedding=query_embedding,
            ))
        if not out:
            return self._lookup_chunks_for_file(
                query, self._VARIABLE_INDEX_REL, 1, query_embedding=query_embedding
            )
        return out
```

- [ ] **Step 4: 跑测试确认通过 + 全量零回归**

Run: `.venv/bin/python -m pytest scripts/tests/test_rag_variable_index_sections.py -v`
Expected: 13 passed

Run: `.venv/bin/python -m pytest -q`
Expected: 全绿, 通过数 = 改动前 + 21 (Task1 的 8 + Task2 的 6 + Task3 的 7)

- [ ] **Step 5: 提交**

```bash
git add sdtm-rag/server/rag.py sdtm-rag/scripts/tests/test_rag_variable_index_sections.py
git commit -m "feat(s1): VARIABLE_INDEX 注入改字面 section 定位 (回落 cosine 不变)"
```

---

### Task 4: 配对 diff 验收 + 证据收口

**Files:**
- Create: `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md`
- Modify: `docs/PROGRESS.md`、`.work/meta/worklog/phase_07_rag_kg.md`、`milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`

**Interfaces:**
- Consumes: Task 3 落地后的检索行为。
- Produces: 收口 checkpoint (含新基线口径、18 题逐题表、已知限制)。

- [ ] **Step 1: 跑改动后的 CDISC 全集检索闸**

Run:
```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
    --retrieval-only --hybrid --structured-lookup \
    --output /tmp/v3_after_literal_section.json
```
Expected: 总分 ≥ 95.71%; 目标是 **98.57%** (18 题子集 100%, 余下 q38 / q126 两道既有 miss)。

- [ ] **Step 2: 逐题配对 diff (不接受"总分没掉"作为证据)**

Run:
```bash
.venv/bin/python - <<'PY'
import json, subprocess
after = {r["id"]: r["source_recall"] for r in json.load(open("/tmp/v3_after_literal_section.json"))["results"]}
before = {   # 改动前实测, 见 evidence/checkpoints/cdisc_gold_section_granularity.md §4
    "q107": 0.5, "q108": 0.0, "q109": 0.0, "q110": 0.0, "q112": 0.0,
}
VI18 = ["q07","q34","q66","q67","q68","q69","q71","q77","q103","q104","q105","q106",
        "q107","q108","q109","q110","q111","q112"]
print("18 题子集:", round(sum(after[q] for q in VI18) / len(VI18) * 100, 2), "%")
for q in VI18:
    print(f"  {q}: {before.get(q, 1.0):.2f} -> {after[q]:.2f}")
PY
```
Expected: 18 题全部 1.00; q107/108/109/110/112 五题上升; **另 13 题保持 1.00**。

若有任一 VI 题从 1.00 掉下来: **停下**, 这是新通道打输了原 cosine, 属回归, 必须先定位再继续。

- [ ] **Step 3: 其余 122 题逐位 Δ0 核对**

Run:
```bash
.venv/bin/python - <<'PY'
import json
after = {r["id"]: r["source_recall"] for r in json.load(open("/tmp/v3_after_literal_section.json"))["results"]}
VI18 = {"q07","q34","q66","q67","q68","q69","q71","q77","q103","q104","q105","q106",
        "q107","q108","q109","q110","q111","q112"}
rest = {k: v for k, v in after.items() if k not in VI18}
print("其余", len(rest), "题均值:", round(sum(rest.values()) / len(rest) * 100, 2), "%")
print("非满分:", {k: v for k, v in rest.items() if v < 1.0})
PY
```
Expected: 其余 122 题 **98.77%** (与 `cdisc_gold_section_granularity.md` §4 记录逐位相同), 非满分只有 `q38: 0.0` 与 `q126: 0.5`。

- [ ] **Step 4: 生产冒烟 (服务侧真的通电)**

Run:
```bash
curl -s -X POST localhost:8000/api/search -H 'content-type: application/json' \
  -d '{"query":"Which domains use codelist C99073 for laterality?","top_k":5}' \
  | .venv/bin/python -c "import sys,json;print([c['section'] for c in json.load(sys.stdin)['chunks'][:3]])"
```
Expected: 首块 section 为 `§三 CT 交叉引用: C99073`。
(若 `/api/search` 的请求/响应字段名不同, 以 `server/main.py` 的实际路由为准调整; 关键是**注入的首块 section 是字面命中的那一节**。)

- [ ] **Step 5: 写收口 checkpoint**

新建 `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md`, 必含:
- 新旧基线并列 + 口径限定词 ("section 级判据"), 明写**上限是 98.57% 不是 100%**;
- 18 题逐题 before → after 表;
- 其余 122 题 Δ0 的证据 (Step 3 输出);
- 已知限制: ① 域变量表族未覆盖 (63 chunk) ② 锚点上限 3, 超 3 个码的题会漏 ③ 变量锚点用 `_query_variables` 的已知变量表, 表外变量不 fire ④ 回落路径仍是 cosine, 即"未 fire 的题维持旧缺陷";
- 复跑命令 (Step 1-4 原样)。

- [ ] **Step 6: 索引三件套 + kickoff 同步**

- `docs/PROGRESS.md`: Phase 7 行更新检索基线 (CDISC section 级判据 95.71% → 新值), 加 milestone 条目。
- `.work/meta/worklog/phase_07_rag_kg.md`: append 本次 work record。
- `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`: §2.D.2 标 DONE 并指向新 checkpoint; §1 基线表更新 CDISC 行。

- [ ] **Step 7: 提交**

```bash
git add -A
git commit -m "feat(s1): VARIABLE_INDEX 字面 section 定位收口 — 18 题子集 75% -> 100%"
```

---

### Task 5: 规则 D 三方隔离审查

**Files:** 无代码改动 (审查产出写入 Task 4 的 checkpoint)

**Interfaces:**
- Consumes: Task 1-4 的全部改动 (`git diff`)。
- Produces: 审查裁定 (APPROVE / REVISE) + 抽检报告, 附在 checkpoint 末尾。

- [ ] **Step 1: 审查方 (与实现方不同 `subagent_type`)**

审 `git diff` 全量, 重点: ① 回落路径是否真的逐字节保持旧行为 ② fail-loud 是否会在生产查询里误触发 ③ 锚点顺序 (CT 先) 是否有反例 ④ 测试是否只锁了 happy path。

- [ ] **Step 2: 抽检方 (第三个 `subagent_type`, 规则 A)**

抽样总体 = **本轮实际变更集合 = 18 题 VI 子集**, 不是 140 题全集。独立复跑 Task 4 Step 2 的逐题表, 对 N≥5 题人工核验"注入的 section 正文确实能回答该题" (不是只看 recall 数字)。

- [ ] **Step 3: 裁定入档 + 提交**

```bash
git add -A
git commit -m "docs(s1): 规则 D 三方隔离审查裁定入档"
```
