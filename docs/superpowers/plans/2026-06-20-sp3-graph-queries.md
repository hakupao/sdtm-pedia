# SP3 — 关系/影响图查询 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 SP1 `meta.yaml` + SP2 `MetaStore` 之上加一个纯 Python 内存图引擎 (`GraphEngine`, 可换 `GraphBackend` seam), 交付影响/级联 · 跨域聚合 · 结构邻接 · 域间关系发现, 并经一个图答题器 (`GraphAnswerer`) 接入 SP2 答题通道 (NL)。

**Architecture:** 全加法、不碰检索层。`GraphEngine(store)` 用 `DictBackend(store)` (MetaStore 反向索引) 实现图原语遍历, 高层查询方法建在原语上。`GraphAnswerer(engine)` 做图意图检测 + 事实装配 → `StructuredFacts | None`。集成点用一个 `CompositeAnswerer` 把 SP2 `StructuredAnswerer` 与 SP3 `GraphAnswerer` 的 `resolve()` 合并 (`merge_facts`), 使 `app.state.answerer.resolve()` 返回合并事实 —— **router / ask_stream / run_eval 的每题循环零改动** (它们已调 `answerer.resolve` → `augment_context` → `apply_counting_gate`)。低保真 `relations_curated` 走 `StructuredFacts.advisory_block` (新增字段) + 独立 advisory header, 绝不进权威块或接地闸。

**Tech Stack:** Python 3.x, pydantic-settings, PyYAML, FastAPI/Starlette, pytest (`testpaths=["scripts/tests"]`)。工作目录 `branches/07_rag_kg/sdtm-rag/`, venv `.venv/bin/python`。

**关键约束 (spec §1 + 个人规则):**
- 零硬编 q-id / 特定变量名 (代码只有通用语言形状); 实体词表 = 全量 meta.yaml; must-fire / must-not-fire 电池 + held-out 探针。
- 接地闸只硬校验**基数** (impact/aggregate 的 N/M); 集合成员与 advisory 关系不硬校验。
- config flag `graph_answer_enabled` 初值 **False**, 验证后翻 True (env 可覆盖)。
- 规则 A: N=8 (4 能力族各 2)。规则 B: 失败归档 `evidence/failures/`。规则 C: `RETROSPECTIVE_sp3.md`。规则 D: 异 `subagent_type` 一轮独立审。

---

## File Structure

**新增:**
- `server/graph_engine.py` — `GraphBackend` (Protocol) + `DictBackend` + `GraphEngine` (查询 API)
- `server/graph_answer.py` — `detect_graph_intents()` + `GraphAnswerer` (意图检测 + 事实装配)
- `scripts/tests/test_graph_engine.py` — 引擎 vs meta.yaml 独立重导 (穷举)
- `scripts/tests/test_graph_answer.py` — 意图电池 + 装配 must-fire/not-fire
- `eval/prod_wirein/sp3_graph_probes.py` — held-out 探针 (引擎 vs meta.yaml + 140q 零污染)
- `eval/test_set_sp3_graph.yml` — 盲写图能力 NL 题集 (gold 从 meta.yaml 导)

**修改:**
- `server/meta_store.py` — `+same_class()` `+relations_curated()` 访问器 (纯加法)
- `server/structured_answer.py` — `StructuredFacts.advisory_block` 字段 + `augment_context` advisory header + `merge_facts()` + `CompositeAnswerer`
- `server/config.py` — `graph_answer_enabled: bool = False`
- `server/main.py` — `maybe_build_answerer` 组合 SP2+SP3 (gated)
- `eval/run_eval.py` — `--graph-answer` flag + 组合 answerer
- `scripts/tests/test_meta_store.py` / `test_structured_answer.py` — 新方法单测

---

# PHASE 1 — 图引擎 (数据层, 不碰 NL)

## Task 1: MetaStore `same_class` + `relations_curated` 访问器

**Files:**
- Modify: `server/meta_store.py` (新增 2 方法)
- Test: `scripts/tests/test_meta_store.py`

- [ ] **Step 1: 写失败测试**

```python
# append to scripts/tests/test_meta_store.py
def test_same_class_accessor(store: MetaStore):
    sc = store.same_class("AE")
    assert "MH" in sc and "CE" in sc          # AE (Events) shares class with MH/CE
    assert "AE" not in sc                       # never includes self
    assert store.same_class("ZZ") == []         # unknown -> empty, no raise
    assert store.same_class("ae") == sc          # case-insensitive

def test_relations_curated_accessor(store: MetaStore):
    rels = store.relations_curated("AE")
    assert isinstance(rels, list) and rels
    r = rels[0]
    assert {"target", "mechanism", "category", "note"} <= set(r)
    # returns a COPY: mutating must not corrupt the store
    rels.append({"x": 1})
    assert len(store.relations_curated("AE")) == len(rels) - 1
    assert store.relations_curated("ZZ") == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q -k "same_class or relations_curated"`
Expected: FAIL — `AttributeError: 'MetaStore' object has no attribute 'same_class'`

- [ ] **Step 3: 实现 (加到 MetaStore, 紧邻 `domain_info`)**

```python
# server/meta_store.py — add methods to MetaStore
    def same_class(self, dom: str) -> list[str]:
        """Domains in the same observation class as `dom` (excludes self), from
        meta.yaml `same_class`. Unknown domain -> []."""
        d = self._domain_by_code.get(dom.upper())
        return list(d["same_class"]) if d else []

    def relations_curated(self, dom: str) -> list[dict]:
        """Curated (LOW-fidelity, curated_prose) inter-domain relations for `dom`:
        list of {target, mechanism, category, note, fidelity}. Returns deep-ish copies
        so callers cannot mutate the store. Unknown domain -> []."""
        d = self._domain_by_code.get(dom.upper())
        return [dict(r) for r in d["relations_curated"]] if d else []
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q`
Expected: PASS (all).

- [ ] **Step 5: Commit**

```bash
git add server/meta_store.py scripts/tests/test_meta_store.py
git commit -m "SP3 Task1: MetaStore same_class + relations_curated accessors (TDD)"
```

---

## Task 2: `GraphBackend` Protocol + `DictBackend`

**Files:**
- Create: `server/graph_engine.py`
- Test: `scripts/tests/test_graph_engine.py`

- [ ] **Step 1: 写失败测试 (原语遍历)**

```python
# scripts/tests/test_graph_engine.py
from pathlib import Path

import pytest

from server.config import settings
from server.meta_store import MetaStore
from server.graph_engine import DictBackend


@pytest.fixture(scope="module")
def store() -> MetaStore:
    return MetaStore(settings.meta_path)


@pytest.fixture(scope="module")
def backend(store) -> DictBackend:
    return DictBackend(store)


def test_nodes_of_type(backend, store):
    assert len(backend.nodes_of_type("Domain")) == 63
    assert len(backend.nodes_of_type("Variable")) == 1523
    assert len(backend.nodes_of_type("Codelist")) == 1005
    assert set(backend.nodes_of_type("Class")) == {
        d_class for d_class in (store.domain_info(d)["class"] for d in store.known_domains)
    }
    assert backend.nodes_of_type("Bogus") == []


def test_out_neighbors_edges(backend, store):
    # HAS_VARIABLE / IN_DOMAIN are inverse
    assert "AETERM" in backend.out_neighbors("AE", "HAS_VARIABLE")
    assert "AE" in backend.out_neighbors("AETERM", "IN_DOMAIN")
    # USES_CT / CT_USED_BY
    assert "C66742" in backend.out_neighbors("AESER", "USES_CT")
    assert "AESER" in backend.out_neighbors("C66742", "CT_USED_BY")
    # CT_IN_DOMAIN matches MetaStore.domains_for_codelist exactly
    assert sorted(backend.out_neighbors("C66742", "CT_IN_DOMAIN")) == store.domains_for_codelist("C66742")
    # SAME_CLASS / class membership
    assert backend.out_neighbors("AE", "SAME_CLASS") == store.same_class("AE")
    assert "AE" in backend.out_neighbors(store.domain_info("AE")["class"], "CLASS_HAS")
    assert backend.out_neighbors("AE", "BELONGS_TO") == [store.domain_info("AE")["class"]]
    # RELATED_TO targets + edge_data
    tgts = backend.out_neighbors("AE", "RELATED_TO")
    assert tgts and all(isinstance(t, str) for t in tgts)
    ed = backend.edge_data("AE", tgts[0], "RELATED_TO")
    assert ed is not None and "mechanism" in ed
    # unknown node/edge -> [] / None, never raise
    assert backend.out_neighbors("ZZ", "HAS_VARIABLE") == []
    assert backend.edge_data("AE", "ZZ", "RELATED_TO") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.graph_engine'`

- [ ] **Step 3: 实现 `GraphBackend` + `DictBackend`**

```python
# server/graph_engine.py
"""SP3 in-memory graph layer over the SP1 meta.yaml / SP2 MetaStore.

Pure Python, no networkx (that is the swappable backend's job). GraphEngine exposes the
high-level relationship/impact/aggregate query API; it traverses via a GraphBackend
(topology only — node metadata such as names/labels always comes from meta.yaml/MetaStore).
DictBackend implements the backend from MetaStore's reverse indices. A future networkx /
Neo4j backend reimplements only the three primitives; GraphEngine + NL + gate are unchanged.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from server.meta_store import MetaStore

# Edge types (string-typed so a non-dict backend can map them however it likes).
HAS_VARIABLE = "HAS_VARIABLE"   # Domain -> Variable
IN_DOMAIN = "IN_DOMAIN"         # Variable -> Domain
USES_CT = "USES_CT"             # Variable -> Codelist
CT_USED_BY = "CT_USED_BY"       # Codelist -> Variable
CT_IN_DOMAIN = "CT_IN_DOMAIN"   # Codelist -> Domain
BELONGS_TO = "BELONGS_TO"       # Domain -> Class
CLASS_HAS = "CLASS_HAS"         # Class -> Domain
SAME_CLASS = "SAME_CLASS"       # Domain -> Domain
DEFHOME = "DEFHOME"             # Variable -> model file
RELATED_TO = "RELATED_TO"       # Domain -> Domain (curated, LOW fidelity; carries edge_data)


@runtime_checkable
class GraphBackend(Protocol):
    def nodes_of_type(self, ntype: str) -> list[str]: ...
    def out_neighbors(self, node: str, edge_type: str) -> list[str]: ...
    def edge_data(self, src: str, dst: str, edge_type: str) -> dict | None: ...


class DictBackend:
    """GraphBackend backed by MetaStore reverse indices (topology only)."""

    def __init__(self, store: MetaStore):
        self.store = store
        self._classes = sorted({store.domain_info(d)["class"] for d in store.known_domains})
        self._class_to_domains: dict[str, list[str]] = {}
        for d in sorted(store.known_domains):
            self._class_to_domains.setdefault(store.domain_info(d)["class"], []).append(d)

    def nodes_of_type(self, ntype: str) -> list[str]:
        if ntype == "Domain":
            return sorted(self.store.known_domains)
        if ntype == "Variable":
            return sorted(self.store.known_variables)
        if ntype == "Codelist":
            return sorted(self.store.known_ctcodes)
        if ntype == "Class":
            return list(self._classes)
        return []

    def out_neighbors(self, node: str, edge_type: str) -> list[str]:
        s = self.store
        if edge_type == HAS_VARIABLE:
            return s.variables_in_domain(node)
        if edge_type == IN_DOMAIN:
            return s.domains_for_variable(node)
        if edge_type == USES_CT:
            return s.ct_codes_for_variable(node)
        if edge_type == CT_USED_BY:
            return s.variables_for_codelist(node)
        if edge_type == CT_IN_DOMAIN:
            return s.domains_for_codelist(node)
        if edge_type == SAME_CLASS:
            return s.same_class(node)
        if edge_type == BELONGS_TO:
            info = s.domain_info(node)
            return [info["class"]] if info else []
        if edge_type == CLASS_HAS:
            return list(self._class_to_domains.get(node, []))
        if edge_type == DEFHOME:
            f = s.model_defhome(node)
            return [f] if f else []
        if edge_type == RELATED_TO:
            return [r["target"] for r in s.relations_curated(node)]
        return []

    def edge_data(self, src: str, dst: str, edge_type: str) -> dict | None:
        if edge_type == RELATED_TO:
            for r in self.store.relations_curated(src):
                if r["target"] == dst:
                    return r
        return None
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/graph_engine.py scripts/tests/test_graph_engine.py
git commit -m "SP3 Task2: GraphBackend protocol + DictBackend over MetaStore (TDD)"
```

---

## Task 3: `GraphEngine` 影响/聚合/邻接 查询

**Files:**
- Modify: `server/graph_engine.py` (`GraphEngine` 类)
- Test: `scripts/tests/test_graph_engine.py`

- [ ] **Step 1: 写失败测试 (对齐 MetaStore ground truth)**

```python
# append to scripts/tests/test_graph_engine.py
from server.graph_engine import GraphEngine


@pytest.fixture(scope="module")
def engine(store) -> GraphEngine:
    return GraphEngine(store)


def test_impact_of_codelist(engine, store):
    imp = engine.impact_of_codelist("C66742")
    assert imp["name"] == store.codelist("C66742")["name"]
    assert imp["domains"] == store.domains_for_codelist("C66742")
    assert imp["variables"] == store.variables_for_codelist("C66742")
    assert imp["n_domains"] == len(imp["domains"])
    assert imp["n_variables"] == len(imp["variables"])
    assert engine.impact_of_codelist("C0000000") is None


def test_impact_of_variable(engine, store):
    imp = engine.impact_of_variable("TAETORD")
    assert imp["domains"] == store.domains_for_variable("TAETORD")
    assert imp["n_domains"] == 43
    assert engine.impact_of_variable("NOTAVAR") is None


def test_variables_in_min_domains(engine, store):
    res = dict(engine.variables_in_min_domains(40))
    # cross-checked against MetaStore directly
    truth = {v: len(store.domains_for_variable(v)) for v in store.known_variables}
    truth = {v: c for v, c in truth.items() if c >= 40}
    assert res == truth
    # sorted descending by count
    counts = [c for _v, c in engine.variables_in_min_domains(40)]
    assert counts == sorted(counts, reverse=True)


def test_domains_in_class_and_sizes(engine, store):
    events = engine.domains_in_class("Events")
    assert "AE" in events
    assert all(store.domain_info(d)["class"] == "Events" for d in events)
    sizes = engine.class_sizes()
    assert sum(sizes.values()) == 63
    assert sizes["Events"] == len(events)


def test_most_shared_codelists(engine, store):
    top = engine.most_shared_codelists(5)
    assert len(top) == 5
    nvs = [t["n_variables"] for t in top]
    assert nvs == sorted(nvs, reverse=True)
    assert top[0]["n_variables"] == max(
        len(store.variables_for_codelist(c)) for c in store.known_ctcodes
    )


def test_same_class_and_co_users(engine, store):
    assert engine.same_class_domains("AE") == store.same_class("AE")
    co = engine.codelist_co_users("AESER")
    for code, info in co.items():
        assert "AESER" not in info["others"]
        assert set(info["others"]) == set(store.variables_for_codelist(code)) - {"AESER"}
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q -k "impact or min_domains or class or shared or co_users"`
Expected: FAIL — `ImportError: cannot import name 'GraphEngine'`

- [ ] **Step 3: 实现 `GraphEngine` (only backend primitives + store for attrs)**

```python
# append to server/graph_engine.py
class GraphEngine:
    """High-level relationship/impact/aggregate queries over a GraphBackend.

    Topology comes from the backend (swappable); node metadata (names/labels) comes from
    the MetaStore. All methods are case-insensitive at entry and return None/[] for unknown
    entities (never raise)."""

    def __init__(self, store: MetaStore, backend: GraphBackend | None = None):
        self.store = store
        self.backend = backend if backend is not None else DictBackend(store)

    # ── impact / cascade ──
    def impact_of_codelist(self, code: str) -> dict | None:
        cl = self.store.codelist(code)
        if cl is None:
            return None
        c = code.upper()
        domains = sorted(self.backend.out_neighbors(c, CT_IN_DOMAIN))
        variables = sorted(self.backend.out_neighbors(c, CT_USED_BY))
        return {"code": c, "name": cl["name"], "domains": domains, "variables": variables,
                "n_domains": len(domains), "n_variables": len(variables)}

    def impact_of_variable(self, var: str) -> dict | None:
        v = var.upper()
        if v not in self.store.known_variables:
            return None
        domains = sorted(self.backend.out_neighbors(v, IN_DOMAIN))
        return {"var": v, "domains": domains, "n_domains": len(domains)}

    # ── cross-domain aggregates ──
    def variables_in_min_domains(self, n: int) -> list[tuple[str, int]]:
        out = []
        for v in self.backend.nodes_of_type("Variable"):
            cnt = len(self.backend.out_neighbors(v, IN_DOMAIN))
            if cnt >= n:
                out.append((v, cnt))
        out.sort(key=lambda t: (-t[1], t[0]))
        return out

    def domains_in_class(self, cls: str) -> list[str]:
        return sorted(self.backend.out_neighbors(cls, CLASS_HAS))

    def class_sizes(self) -> dict[str, int]:
        return {c: len(self.backend.out_neighbors(c, CLASS_HAS))
                for c in self.backend.nodes_of_type("Class")}

    def most_shared_codelists(self, k: int = 10) -> list[dict]:
        rows = []
        for c in self.backend.nodes_of_type("Codelist"):
            nv = len(self.backend.out_neighbors(c, CT_USED_BY))
            nd = len(self.backend.out_neighbors(c, CT_IN_DOMAIN))
            cl = self.store.codelist(c)
            rows.append({"code": c, "name": cl["name"] if cl else c,
                         "n_variables": nv, "n_domains": nd})
        rows.sort(key=lambda r: (-r["n_variables"], r["code"]))
        return rows[:k]

    # ── structural neighborhood / co-usage ──
    def same_class_domains(self, dom: str) -> list[str]:
        return self.backend.out_neighbors(dom.upper(), SAME_CLASS)

    def codelist_co_users(self, var: str) -> dict[str, dict]:
        v = var.upper()
        out: dict[str, dict] = {}
        for code in self.backend.out_neighbors(v, USES_CT):
            others = [x for x in self.backend.out_neighbors(code, CT_USED_BY) if x != v]
            cl = self.store.codelist(code)
            out[code] = {"name": cl["name"] if cl else code, "others": sorted(others)}
        return out
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q`
Expected: PASS (all).

- [ ] **Step 5: Commit**

```bash
git add server/graph_engine.py scripts/tests/test_graph_engine.py
git commit -m "SP3 Task3: GraphEngine impact/aggregate/neighborhood queries (TDD vs MetaStore)"
```

---

## Task 4: `GraphEngine.domain_relations` (HIGH 结构 + LOW curated)

**Files:**
- Modify: `server/graph_engine.py`
- Test: `scripts/tests/test_graph_engine.py`

- [ ] **Step 1: 写失败测试**

```python
# append to scripts/tests/test_graph_engine.py
def test_domain_relations(engine, store):
    rel = engine.domain_relations("AE")
    assert rel["structural"]["same_class"] == store.same_class("AE")
    curated = rel["curated"]
    assert curated == store.relations_curated("AE")  # advisory edges passed through verbatim
    # every curated edge is tagged LOW-fidelity for the answerer to mark advisory
    assert all(c.get("fidelity") for c in curated) or all("mechanism" in c for c in curated)
    assert engine.domain_relations("ZZ") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q -k domain_relations`
Expected: FAIL — `AttributeError: 'GraphEngine' object has no attribute 'domain_relations'`

- [ ] **Step 3: 实现**

```python
# append to server/graph_engine.py GraphEngine
    def domain_relations(self, dom: str) -> dict | None:
        d = dom.upper()
        if d not in self.store.known_domains:
            return None
        curated = []
        for t in self.backend.out_neighbors(d, RELATED_TO):
            ed = self.backend.edge_data(d, t, RELATED_TO) or {}
            curated.append(ed)
        return {"structural": {"same_class": self.backend.out_neighbors(d, SAME_CLASS)},
                "curated": curated}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/graph_engine.py scripts/tests/test_graph_engine.py
git commit -m "SP3 Task4: GraphEngine.domain_relations (structural HIGH + curated advisory)"
```

---

## Task 5: 引擎 vs meta.yaml 穷举独立重导 (反套套逻辑)

> 不复用 GraphEngine 自身代码, 直接从 `yaml.safe_load(meta.yaml)` 原始结构独立计算 ground truth, 全量对账。这是 SP3 程序门的核心 (沿用 SP1 reconcile / SP2 snapshot 思路)。

**Files:**
- Test: `scripts/tests/test_graph_engine.py`

- [ ] **Step 1: 写穷举对账测试**

```python
# append to scripts/tests/test_graph_engine.py
import yaml as _yaml
from collections import defaultdict


def _raw_meta():
    return _yaml.safe_load(settings.meta_path.read_text(encoding="utf-8"))


def test_exhaustive_impact_of_variable_vs_raw(engine):
    raw = _raw_meta()
    truth = defaultdict(set)
    for d in raw["domains"]:
        if not d["counts_toward_63"]:
            continue
        for v in d["variables"]:
            truth[v["name"]].add(d["domain"])
    for var, doms in truth.items():
        imp = engine.impact_of_variable(var)
        assert imp is not None and imp["n_domains"] == len(doms), var
        assert set(imp["domains"]) == doms, var


def test_exhaustive_impact_of_codelist_vs_raw(engine):
    raw = _raw_meta()
    dom_truth, var_truth = defaultdict(set), defaultdict(set)
    for d in raw["domains"]:
        if not d["counts_toward_63"]:
            continue
        for v in d["variables"]:
            for code in v["ct_codes"]:
                dom_truth[code].add(d["domain"])
                var_truth[code].add(v["name"])
    for code in {c["ct_code"] for c in raw["codelists"]}:
        imp = engine.impact_of_codelist(code)
        assert imp is not None, code
        assert set(imp["domains"]) == dom_truth.get(code, set()), code
        assert set(imp["variables"]) == var_truth.get(code, set()), code


def test_exhaustive_class_sizes_vs_raw(engine):
    raw = _raw_meta()
    truth = defaultdict(int)
    for d in raw["domains"]:
        if d["counts_toward_63"]:
            truth[d["class"]] += 1
    assert engine.class_sizes() == dict(truth)
```

- [ ] **Step 2: 跑测试**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_engine.py -q -k exhaustive`
Expected: PASS. If any FAIL, the engine disagrees with raw meta.yaml — fix the engine, not the truth.

- [ ] **Step 3: Commit**

```bash
git add scripts/tests/test_graph_engine.py
git commit -m "SP3 Task5: exhaustive engine-vs-raw-meta.yaml reconciliation (anti-tautology)"
```

---

# PHASE 2 — NL 答题集成

## Task 6: `StructuredFacts.advisory_block` + `augment_context` advisory header

> 低保真内容绝不能落在「authoritative, exhaustive」header 下。加一个可选字段 + 独立 header。SP2 既有行为在 `advisory_block=""` 时**逐字节不变**。

**Files:**
- Modify: `server/structured_answer.py`
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试**

```python
# append to scripts/tests/test_structured_answer.py
from server.structured_answer import augment_context, StructuredFacts


def test_advisory_block_default_empty_is_sp2_identical():
    f = StructuredFacts(text_block="- **X** — fact.")
    out = augment_context(f, "CTX")
    assert out.startswith("## Structured Facts (authoritative, exhaustive")
    assert "non-exhaustive" not in out   # no advisory header when advisory_block empty
    assert out.endswith("CTX")


def test_advisory_block_renders_under_separate_header():
    f = StructuredFacts(text_block="- **C66742** — used by 41 vars.",
                        advisory_block="- AE is related to CM (RELREC).")
    out = augment_context(f, "CTX")
    assert "## Structured Facts (authoritative, exhaustive" in out
    assert "curated, non-exhaustive" in out          # advisory header present
    assert "AE is related to CM" in out
    # advisory content appears AFTER the authoritative block, not under its header
    assert out.index("authoritative, exhaustive") < out.index("curated, non-exhaustive")
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q -k advisory`
Expected: FAIL — `TypeError: ... unexpected keyword argument 'advisory_block'`

- [ ] **Step 3: 实现 (改 dataclass + augment_context)**

```python
# server/structured_answer.py — extend the dataclass
@dataclass
class StructuredFacts:
    text_block: str
    checkable_counts: list[CheckableCount] = field(default_factory=list)
    advisory_block: str = ""  # SP3: non-authoritative, non-exhaustive (curated relations)


# replace augment_context
_ADVISORY_HEADER = ("## Related context (curated, non-exhaustive — derived from prose, "
                    "may be incomplete; do not claim this list is complete)")


def augment_context(facts: StructuredFacts | None, context: str) -> str:
    """Prepend the authoritative facts block (+ optional advisory block) ahead of the
    retrieved context. Shared by router.py (prod) and run_eval.py (eval)."""
    if facts is None:
        return context
    out = f"{_FACTS_HEADER}\n\n{facts.text_block}"
    if facts.advisory_block:
        out += f"\n\n{_ADVISORY_HEADER}\n\n{facts.advisory_block}"
    return f"{out}\n\n---\n\n{context}"
```

- [ ] **Step 4: 跑测试确认通过 + SP2 回归**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: PASS (all, incl. existing SP2 augment_context tests — advisory_block default keeps them green).

- [ ] **Step 5: Commit**

```bash
git add server/structured_answer.py scripts/tests/test_structured_answer.py
git commit -m "SP3 Task6: StructuredFacts.advisory_block + separate advisory header (SP2 back-compat)"
```

---

## Task 7: `merge_facts()` (合并 SP2 + SP3 事实, 去重)

**Files:**
- Modify: `server/structured_answer.py`
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试**

```python
# append to scripts/tests/test_structured_answer.py
from server.structured_answer import merge_facts, CheckableCount


def test_merge_none_and_single():
    assert merge_facts(None, None) is None
    f = StructuredFacts(text_block="- a")
    assert merge_facts(f, None) is f          # single present -> returned as-is


def test_merge_dedups_lines_counts_and_advisory():
    a = StructuredFacts(text_block="- shared\n- only-a",
                        checkable_counts=[CheckableCount("C66742", "domains", 41)],
                        advisory_block="- adv-a")
    b = StructuredFacts(text_block="- shared\n- only-b",
                        checkable_counts=[CheckableCount("C66742", "domains", 41),  # dup
                                          CheckableCount("AE", "variables", 30)],
                        advisory_block="- adv-b")
    m = merge_facts(a, b)
    assert m.text_block.split("\n") == ["- shared", "- only-a", "- only-b"]   # line de-dup
    assert m.checkable_counts == [CheckableCount("C66742", "domains", 41),
                                  CheckableCount("AE", "variables", 30)]       # count de-dup
    assert m.advisory_block.split("\n") == ["- adv-a", "- adv-b"]
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q -k merge`
Expected: FAIL — `ImportError: cannot import name 'merge_facts'`

- [ ] **Step 3: 实现**

```python
# append to server/structured_answer.py
def merge_facts(*facts: StructuredFacts | None) -> StructuredFacts | None:
    """Merge several StructuredFacts (SP2 + SP3) into one, de-duping text lines (exact),
    checkable_counts (by subject/kind/value), and advisory lines. Order = first-seen.
    Returns None if all None; returns the single object unchanged if only one present."""
    present = [f for f in facts if f is not None]
    if not present:
        return None
    if len(present) == 1:
        return present[0]

    def _dedup_lines(blocks: list[str]) -> str:
        seen: set[str] = set()
        out: list[str] = []
        for block in blocks:
            for ln in block.split("\n"):
                if ln not in seen:
                    seen.add(ln)
                    out.append(ln)
        return "\n".join(out)

    counts: list[CheckableCount] = []
    seen_c: set[tuple] = set()
    for f in present:
        for c in f.checkable_counts:
            key = (c.subject, c.kind, c.value)
            if key not in seen_c:
                seen_c.add(key)
                counts.append(c)
    return StructuredFacts(
        text_block=_dedup_lines([f.text_block for f in present]),
        checkable_counts=counts,
        advisory_block=_dedup_lines([f.advisory_block for f in present if f.advisory_block]),
    )
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/structured_answer.py scripts/tests/test_structured_answer.py
git commit -m "SP3 Task7: merge_facts (SP2+SP3 fact merge with de-dup)"
```

---

## Task 8: `detect_graph_intents()` (通用语言形状, 反过拟合)

**Files:**
- Create: `server/graph_answer.py`
- Test: `scripts/tests/test_graph_answer.py`

- [ ] **Step 1: 写失败测试 (must-fire + must-not-fire, 含 SP2 不相交)**

```python
# scripts/tests/test_graph_answer.py
from server.graph_answer import detect_graph_intents


def test_impact_intent():
    assert "impact" in detect_graph_intents("what is affected if C66742 changes?")
    assert "impact" in detect_graph_intents("which domains are impacted by changing VSORRESU?")
    assert "impact" in detect_graph_intents("what downstream variables depend on EPOCH?")


def test_relationship_intent():
    assert "relationship" in detect_graph_intents("how is AE related to other domains?")
    assert "relationship" in detect_graph_intents("what domains are linked to DM?")


def test_aggregate_intent():
    assert "aggregate" in detect_graph_intents("which variables appear in more than 30 domains?")
    assert "aggregate" in detect_graph_intents("what is the most shared codelist?")
    assert "aggregate" in detect_graph_intents("how many domains are in the Events class?")


def test_must_not_fire_sp2_and_plain():
    # SP2 territory (counting/dist) -> NO graph intent (disjoint by design)
    assert detect_graph_intents("how many domains include TAETORD?") == set()
    assert detect_graph_intents("which domains use the VISITNUM variable?") == set()
    # plain concept / how-to -> nothing
    assert detect_graph_intents("how should missing values be represented?") == set()
    assert detect_graph_intents("what is the structure of the DM domain?") == set()
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_answer.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.graph_answer'`

- [ ] **Step 3: 实现意图检测**

```python
# server/graph_answer.py
"""SP3 graph answer channel: detect relationship/impact/aggregate intent + assemble
authoritative graph facts (and an advisory block for curated relations) for injection.
Conservative by construction: zero hardcoded q-ids/variables; misfire is at worst recall-
additive true facts; correctness of cardinalities is back-stopped by the grounding gate.
Intent vocab is deliberately DISJOINT from SP2's distribution/count vocab (use/include/
which-domains) so plain SP2 queries never trip the graph channel (spec §5.4)."""
from __future__ import annotations

import re

from server.graph_engine import GraphEngine
from server.structured_answer import CheckableCount, StructuredFacts

_VAR_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,7}\b")
_CT_TOKEN_RE = re.compile(r"\bC\d{4,6}\b")

# Impact/cascade — distinct from SP2 dist verbs (use/include/appear/carry/share).
_IMPACT_CUES = ("affect", "affects", "affected", "impact", "impacts", "impacted",
                "change", "changes", "changing", "depend", "depends", "depending",
                "cascade", "downstream", "knock-on", "ripple")
# Relationship discovery.
_REL_CUES = ("related to", "relationship", "relationships", "linked", "connected",
             "connection", "associated with", "association")
# Cross-domain aggregate (graph-wide, not SP2 per-entity counts).
_AGG_CUES = ("more than", "at least", "most shared", "most common", "most widely used",
             "in the events class", "in the findings class", "in the interventions class",
             "in the special-purpose class", "in the trial design class",
             "in the relationship class", " class?", " class ")


def detect_graph_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()
    if any(c in ql for c in _IMPACT_CUES):
        intents.add("impact")
    if any(c in ql for c in _REL_CUES):
        intents.add("relationship")
    if any(c in ql for c in _AGG_CUES):
        intents.add("aggregate")
    return intents
```

> NOTE for implementer: the `_AGG_CUES` "class" handling is the trickiest over/under-fire surface. Make the must-fire/must-not-fire battery (Task 9) the contract and tune `_AGG_CUES` (e.g. require a class name token, or `how many domains ... class`) until it passes WITHOUT hardcoding question strings. Prefer a generic shape (class name ∈ the 7 classes) over enumerated phrases if the enumerated list feels brittle.

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_answer.py -q`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add server/graph_answer.py scripts/tests/test_graph_answer.py
git commit -m "SP3 Task8: detect_graph_intents (generic shapes, disjoint from SP2)"
```

---

## Task 9: `GraphAnswerer.resolve()` — 锚定 + 事实装配 + advisory

**Files:**
- Modify: `server/graph_answer.py`
- Test: `scripts/tests/test_graph_answer.py`

- [ ] **Step 1: 写失败测试 (must-fire + must-not-fire 电池)**

```python
# append to scripts/tests/test_graph_answer.py
from pathlib import Path

import pytest

from server.config import settings
from server.meta_store import MetaStore
from server.graph_engine import GraphEngine
from server.graph_answer import GraphAnswerer
from server.structured_answer import CheckableCount


@pytest.fixture(scope="module")
def ga() -> GraphAnswerer:
    return GraphAnswerer(GraphEngine(MetaStore(settings.meta_path)))


def test_impact_codelist_fires_with_cardinality(ga):
    facts = ga.resolve("What is affected if codelist C66742 changes?")
    assert facts is not None
    n = len(ga.engine.impact_of_codelist("C66742")["domains"])
    assert str(n) in facts.text_block
    assert CheckableCount("C66742", "impacted_domains", n) in facts.checkable_counts


def test_impact_variable_fires(ga):
    facts = ga.resolve("Which domains are impacted by changing TAETORD?")
    assert facts is not None
    assert CheckableCount("TAETORD", "impacted_domains", 43) in facts.checkable_counts


def test_relationship_fires_advisory_only(ga):
    facts = ga.resolve("How is AE related to other domains?")
    assert facts is not None
    # curated relations go to advisory_block, NOT the authoritative text_block / counts
    assert facts.advisory_block
    assert "same class" in facts.text_block.lower() or facts.text_block == ""
    assert all("RELATED" not in c.kind for c in facts.checkable_counts)


def test_aggregate_min_domains_fires(ga):
    facts = ga.resolve("Which variables appear in more than 40 domains?")
    assert facts is not None
    assert "TAETORD" in facts.text_block or "VISITDY" in facts.text_block


def test_must_not_fire_no_anchor(ga):
    # impact cue but no anchored entity -> None
    assert ga.resolve("what is affected by a protocol amendment?") is None


def test_must_not_fire_sp2_query(ga):
    # SP2 territory, no graph intent -> None (no double injection)
    assert ga.resolve("How many domains include TAETORD?") is None
    assert ga.resolve("Which domains use VISITNUM?") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_answer.py -q -k "fires or must_not"`
Expected: FAIL — `ImportError: cannot import name 'GraphAnswerer'`

- [ ] **Step 3: 实现 `GraphAnswerer`**

```python
# append to server/graph_answer.py
class GraphAnswerer:
    def __init__(self, engine: GraphEngine):
        self.engine = engine
        self.store = engine.store

    def _vars(self, q: str) -> list[str]:
        return [t for t in _VAR_TOKEN_RE.findall(q) if t in self.store.known_variables]

    def _codelists(self, q: str) -> list[str]:
        return [c for c in _CT_TOKEN_RE.findall(q) if c in self.store.known_ctcodes]

    def _domains(self, q: str) -> list[str]:
        ql = q.lower()
        if "domain" not in ql and "sdtm" not in ql:   # SP2-style context guard vs PR/DM collisions
            return []
        return [t for t in _VAR_TOKEN_RE.findall(q) if t in self.store.known_domains]

    def _classes(self, q: str) -> list[str]:
        ql = q.lower()
        return [c for c in self.engine.class_sizes() if c.lower() in ql]

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_graph_intents(query)
        if not intents:
            return None
        lines: list[str] = []
        adv: list[str] = []
        counts: list[CheckableCount] = []

        if "impact" in intents:
            for code in dict.fromkeys(self._codelists(query)):
                imp = self.engine.impact_of_codelist(code)
                if imp:
                    lines.append(
                        f"- Changing codelist **{code}** ({imp['name']}) affects "
                        f"**{imp['n_variables']}** variables across **{imp['n_domains']}** "
                        f"domains: {', '.join(imp['domains'])}.")
                    counts.append(CheckableCount(code, "impacted_domains", imp["n_domains"]))
                    counts.append(CheckableCount(code, "impacted_variables", imp["n_variables"]))
            for var in dict.fromkeys(self._vars(query)):
                imp = self.engine.impact_of_variable(var)
                if imp:
                    lines.append(
                        f"- Changing variable **{var}** affects **{imp['n_domains']}** "
                        f"domains: {', '.join(imp['domains'])}.")
                    counts.append(CheckableCount(var, "impacted_domains", imp["n_domains"]))

        if "relationship" in intents:
            for dom in dict.fromkeys(self._domains(query)):
                rel = self.engine.domain_relations(dom)
                if not rel:
                    continue
                sc = rel["structural"]["same_class"]
                if sc:
                    lines.append(f"- Domain **{dom}** is in the same class as: {', '.join(sc)}.")
                for c in rel["curated"]:
                    mech = f" via {c['mechanism']}" if c.get("mechanism") else ""
                    note = f" — {c['note']}" if c.get("note") else ""
                    adv.append(f"- {dom} → {c['target']}{mech}{note}")

        if "aggregate" in intents:
            m = re.search(r"\b(\d{1,3})\b", query)
            if m and ("variable" in query.lower()):
                n = int(m.group(1))
                res = self.engine.variables_in_min_domains(n)
                if res:
                    listed = ", ".join(f"{v} ({c})" for v, c in res[:50])
                    lines.append(f"- **{len(res)}** variables appear in ≥ {n} domains: {listed}.")
            for cls in dict.fromkeys(self._classes(query)):
                doms = self.engine.domains_in_class(cls)
                lines.append(f"- The **{cls}** class has **{len(doms)}** domains: {', '.join(doms)}.")
                counts.append(CheckableCount(cls, "class_domains", len(doms)))
            if "most shared" in query.lower() or "most common" in query.lower():
                top = self.engine.most_shared_codelists(5)
                listed = ", ".join(f"{t['code']} ({t['name']}, {t['n_variables']} vars)" for t in top)
                lines.append(f"- Most-shared codelists: {listed}.")

        if not lines and not adv:
            return None
        return StructuredFacts(text_block="\n".join(lines),
                               checkable_counts=counts,
                               advisory_block="\n".join(adv))
```

> NOTE for implementer: keep the must-not-fire tests green — if a refinement makes a SP2-style query fire, narrow the cue/anchor, do NOT special-case the question. Record any failed attempt in `evidence/failures/`.

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_answer.py -q`
Expected: PASS (all must-fire + must-not-fire).

- [ ] **Step 5: Commit**

```bash
git add server/graph_answer.py scripts/tests/test_graph_answer.py
git commit -m "SP3 Task9: GraphAnswerer.resolve — anchored graph-fact assembly + advisory (battery)"
```

---

## Task 10: 接地闸覆盖 impact 基数 (验证, 大概率零代码)

**Files:**
- Test: `scripts/tests/test_grounding.py`
- (Possibly) Modify: `server/grounding.py` (仅当 impact kind 未被覆盖)

- [ ] **Step 1: 写失败/确认测试 (impact 基数被答错 → 追加更正)**

```python
# append to scripts/tests/test_grounding.py
from server.grounding import apply_counting_gate
from server.structured_answer import StructuredFacts, CheckableCount


def test_impact_count_violation_corrected():
    facts = StructuredFacts(text_block="(facts)",
                            checkable_counts=[CheckableCount("C66742", "impacted_domains", 41)])
    out, viol = apply_counting_gate("Changing C66742 affects 12 domains.", facts)
    assert "Authoritative correction" in out and "41" in out
    assert viol and viol[0]["subject"] == "C66742" and viol[0]["expected"] == 41


def test_advisory_relations_not_gated():
    # advisory content carries no checkable_counts -> gate is a no-op
    facts = StructuredFacts(text_block="(facts)", checkable_counts=[],
                            advisory_block="- AE → CM via RELREC")
    out, viol = apply_counting_gate("AE relates to many domains.", facts)
    assert out == "AE relates to many domains." and viol == []
```

- [ ] **Step 2: 跑测试**

Run: `.venv/bin/python -m pytest scripts/tests/test_grounding.py -q`
Expected: PASS without code change (the gate is kind-agnostic — it checks any CheckableCount's subject+value). If it FAILS because the gate special-cases SP2 kinds, generalise `apply_counting_gate` to treat every CheckableCount uniformly (subject-adjacent number contradiction), keeping SP2 behaviour identical.

- [ ] **Step 3: Commit**

```bash
git add scripts/tests/test_grounding.py server/grounding.py
git commit -m "SP3 Task10: grounding gate covers impact/aggregate cardinalities (kind-agnostic)"
```

---

# PHASE 3 — 接线 + flag

## Task 11: config flag + `CompositeAnswerer` + `maybe_build_answerer` 组合

**Files:**
- Modify: `server/config.py`, `server/structured_answer.py` (CompositeAnswerer), `server/main.py`
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试**

```python
# append to scripts/tests/test_structured_answer.py
def test_graph_answer_flag_default_off():
    from server.config import Settings
    assert Settings().graph_answer_enabled is False


def test_composite_answerer_merges():
    from pathlib import Path
    from server.config import settings
    from server.meta_store import MetaStore
    from server.structured_answer import StructuredAnswerer, CompositeAnswerer
    from server.graph_engine import GraphEngine
    from server.graph_answer import GraphAnswerer
    store = MetaStore(settings.meta_path)
    comp = CompositeAnswerer([StructuredAnswerer(store), GraphAnswerer(GraphEngine(store))])
    # SP2 count query still answered
    assert comp.resolve("How many domains include TAETORD?") is not None
    # SP3 impact query answered
    assert comp.resolve("What is affected if C66742 changes?") is not None
    # neither -> None
    assert comp.resolve("How should missing values be represented?") is None


def test_maybe_build_answerer_graph_gated():
    from server.config import Settings
    from server.main import maybe_build_answerer
    a = maybe_build_answerer(Settings(structured_answer_enabled=True, graph_answer_enabled=True))
    assert a.resolve("What is affected if C66742 changes?") is not None
    b = maybe_build_answerer(Settings(structured_answer_enabled=True, graph_answer_enabled=False))
    assert b.resolve("What is affected if C66742 changes?") is None   # graph off
    assert b.resolve("How many domains include TAETORD?") is not None  # SP2 on
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q -k "graph_answer_flag or composite or maybe_build_answerer_graph"`
Expected: FAIL — missing flag / CompositeAnswerer.

- [ ] **Step 3: 实现**

```python
# server/config.py — after structured_answer_enabled (~L96):
    # SP3: deterministic relationship/impact/aggregate graph answers from meta.yaml,
    # merged into the structured-answer injection. Ships OFF until validated; then -> True.
    graph_answer_enabled: bool = False
```

```python
# server/structured_answer.py — append
class CompositeAnswerer:
    """Merge several answerers' resolve() outputs (SP2 StructuredAnswerer + SP3
    GraphAnswerer) so app.state.answerer.resolve() returns one merged StructuredFacts —
    router/eval call sites are unchanged."""

    def __init__(self, answerers: list):
        self._answerers = answerers

    def resolve(self, query: str) -> StructuredFacts | None:
        return merge_facts(*[a.resolve(query) for a in self._answerers])
```

```python
# server/main.py — replace maybe_build_answerer body
def maybe_build_answerer(s):
    """Build the SP2 structured answerer and (if enabled) the SP3 graph answerer, composed
    so resolve() returns merged facts. Returns None if both are off. Kept tiny/pure so it
    unit-tests without spinning up FastAPI/RAGEngine."""
    answerers = []
    if s.structured_answer_enabled or s.graph_answer_enabled:
        from server.meta_store import MetaStore
        store = MetaStore(s.meta_path)
        if s.structured_answer_enabled:
            from server.structured_answer import StructuredAnswerer
            answerers.append(StructuredAnswerer(store))
        if s.graph_answer_enabled:
            from server.graph_answer import GraphAnswerer
            from server.graph_engine import GraphEngine
            answerers.append(GraphAnswerer(GraphEngine(store)))
    if not answerers:
        return None
    if len(answerers) == 1:
        return answerers[0]
    from server.structured_answer import CompositeAnswerer
    return CompositeAnswerer(answerers)
```

- [ ] **Step 4: 跑测试 + 全套**

Run: `.venv/bin/python -m pytest scripts/tests -q -p no:warnings`
Expected: PASS (all; SP2 maybe_build_answerer tests still green — single-answerer path unchanged when graph off).

- [ ] **Step 5: Commit**

```bash
git add server/config.py server/structured_answer.py server/main.py scripts/tests/test_structured_answer.py
git commit -m "SP3 Task11: graph_answer_enabled flag + CompositeAnswerer + maybe_build_answerer compose"
```

---

## Task 12: `run_eval.py` `--graph-answer` 接线 (eval/prod 同口径)

**Files:**
- Modify: `eval/run_eval.py`
- Test: `scripts/tests/test_run_eval_judge.py`

- [ ] **Step 1: 写失败测试 (eval 用同样的 composite)**

```python
# append to scripts/tests/test_run_eval_judge.py
def test_eval_graph_answer_composite_parity():
    from pathlib import Path
    from server.meta_store import MetaStore
    from server.config import settings
    from server.structured_answer import StructuredAnswerer, CompositeAnswerer, augment_context
    from server.graph_engine import GraphEngine
    from server.graph_answer import GraphAnswerer
    store = MetaStore(settings.meta_path)
    comp = CompositeAnswerer([StructuredAnswerer(store), GraphAnswerer(GraphEngine(store))])
    facts = comp.resolve("What is affected if C66742 changes?")
    ctx = augment_context(facts, "### [1] chunk\n\nbody")
    assert "affected if" not in ctx  # sanity: it's the answer-side, not echoing the question
    assert "Structured Facts (authoritative" in ctx
```

- [ ] **Step 2: 跑测试确认通过 (helpers 已存在, 守 parity)**

Run: `.venv/bin/python -m pytest scripts/tests/test_run_eval_judge.py -q -k graph_answer_composite`
Expected: PASS immediately (composite/augment already exist; this locks eval parity).

- [ ] **Step 3: 加 CLI flag + 组合 answerer**

```python
# eval/run_eval.py — argparser, near --structured-answer:
    parser.add_argument("--graph-answer", action="store_true",
                        help="SP3: add deterministic graph (relationship/impact/aggregate) facts")

# in main(), replace the answerer-construction block (currently L581-585):
    answerer = None
    if args.structured_answer or args.graph_answer:
        from server.meta_store import MetaStore
        store = MetaStore(settings.meta_path)
        parts = []
        if args.structured_answer:
            from server.structured_answer import StructuredAnswerer
            parts.append(StructuredAnswerer(store))
        if args.graph_answer:
            from server.graph_answer import GraphAnswerer
            from server.graph_engine import GraphEngine
            parts.append(GraphAnswerer(GraphEngine(store)))
        if len(parts) == 1:
            answerer = parts[0]
        else:
            from server.structured_answer import CompositeAnswerer
            answerer = CompositeAnswerer(parts)

# summary block (near the structured_answer summary line):
    summary["graph_answer"] = args.graph_answer
```

> The per-question answer path (L220-247) is UNCHANGED — it already calls `answerer.resolve` → `augment_context` → `apply_counting_gate`, which work on the merged facts.

- [ ] **Step 4: 跑测试 + 2 题 smoke**

Run: `.venv/bin/python -m pytest scripts/tests/test_run_eval_judge.py -q`
Then (cheap, retrieval-only, no judge): `.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --structured-lookup --hybrid --graph-answer --output /tmp/sp3_smoke.json` and confirm it runs + `"graph_answer": true` in the JSON.

- [ ] **Step 5: Commit**

```bash
git add eval/run_eval.py scripts/tests/test_run_eval_judge.py
git commit -m "SP3 Task12: run_eval --graph-answer wiring (composite, eval/prod parity)"
```

---

## Task 13: held-out 探针 + 140q 零污染

**Files:**
- Create: `eval/prod_wirein/sp3_graph_probes.py`

- [ ] **Step 1: 写探针 (引擎 vs meta.yaml held-out + 140q must-not-fire)**

```python
# eval/prod_wirein/sp3_graph_probes.py
"""SP3 anti-overfitting probes:
(A) held-out graph queries over entities NOT in eval test sets — GraphAnswerer facts must
    match the GraphEngine ground truth (which test_graph_engine already pins to raw meta.yaml).
(B) 140q zero-pollution — GraphAnswerer.resolve() must return None for EVERY question in
    test_set_v3.yml (those are SP1/SP2/retrieval questions; graph must not inject into them).
Run: .venv/bin/python eval/prod_wirein/sp3_graph_probes.py"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

HELD_OUT = [
    ("What is affected if codelist C66728 changes?", "C66728", "impacted_domains"),
    ("Which domains are impacted by changing AGE?", "AGE", "impacted_domains"),
    ("Which variables appear in at least 30 domains?", None, None),
    ("How is DM related to other domains?", None, None),
]


def main() -> int:
    store = MetaStore(settings.meta_path)
    ga = GraphAnswerer(GraphEngine(store))
    fails = 0

    # (A) held-out facts present + cardinality matches engine
    for q, subj, kind in HELD_OUT:
        facts = ga.resolve(q)
        if facts is None:
            print(f"FAIL (A) resolve None: {q}")
            fails += 1
            continue
        if subj and kind:
            truth = store.domains_for_codelist(subj) if subj.startswith("C") \
                else store.domains_for_variable(subj)
            cc = [c for c in facts.checkable_counts if c.subject == subj and c.kind == kind]
            ok = cc and cc[0].value == len(truth)
            print(f"{'PASS' if ok else 'FAIL'} (A) {subj} {kind}={len(truth)}")
            fails += 0 if ok else 1
        else:
            print(f"PASS (A) fired: {q}")

    # (B) zero-pollution over the 140q
    raw = yaml.safe_load((Path(__file__).resolve().parents[2] / "eval" / "test_set_v3.yml").read_text())
    polluted = []

    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("question"), str) and ga.resolve(node["question"]) is not None:
                polluted.append(node["question"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(raw)
    if polluted:
        fails += len(polluted)
        print(f"FAIL (B) graph fired on {len(polluted)} non-graph q (first 5): {polluted[:5]}")
    else:
        print("PASS (B) 140q zero-pollution: GraphAnswerer silent on all test_set_v3 questions")

    print(f"\nSP3 PROBES: {'ALL PASS' if fails == 0 else str(fails) + ' FAIL'}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: 跑探针**

Run: `.venv/bin/python eval/prod_wirein/sp3_graph_probes.py`
Expected: `SP3 PROBES: ALL PASS`. If (B) fails, a graph cue is firing on an SP1/SP2 question — narrow the cue/anchor in `graph_answer.py` (do NOT special-case), re-run, archive the failed attempt to `evidence/failures/`.

- [ ] **Step 3: Commit**

```bash
git add eval/prod_wirein/sp3_graph_probes.py
git commit -m "SP3 Task13: held-out probes + 140q zero-pollution gate"
```

---

## Task 14: 盲写图能力 NL 题集 + 端到端 smoke

**Files:**
- Create: `eval/test_set_sp3_graph.yml`

- [ ] **Step 1: 盲写 8-12 道图能力 NL 题 (4 族各 2-3, gold 从 meta.yaml 导)**

每题: `id / category(impact|aggregate|structural|relationship) / question / expected_facts`(从 meta.yaml 程序导出的真值, 如 impacted 域数/集合)。**盲写 = 措辞自然、不照抄 GraphAnswerer 的 cue 词**, 用来证泛化。示例骨架 (实现者据 meta.yaml 真值补全):

```yaml
# eval/test_set_sp3_graph.yml — SP3 graph capability NL probes (gold derived from meta.yaml)
- id: g01
  category: impact
  question: "If we revise the controlled terminology codelist C66742, which domains and variables would be touched?"
  expect_subject: C66742
  expect_kind: impacted_domains   # value asserted at runtime == len(store.domains_for_codelist('C66742'))
- id: g02
  category: impact
  question: "Changing the TAETORD timing variable would ripple into how many domains?"
  expect_subject: TAETORD
  expect_kind: impacted_domains
- id: g03
  category: aggregate
  question: "Which SDTM variables are the most widespread — showing up in at least 40 different domains?"
  expect_min_domains: 40
- id: g04
  category: aggregate
  question: "How many domains make up the Events observation class?"
  expect_subject: Events
  expect_kind: class_domains
- id: g05
  category: structural
  question: "Beyond Adverse Events itself, which domains sit in the same observation class as AE?"
  expect_same_class: AE
- id: g06
  category: relationship
  question: "What other domains does the AE domain have noted relationships with?"
  expect_advisory: AE       # advisory block non-empty; not gated
# implementer: add g07-g10 covering codelist co-users + most-shared-codelist + impact_of_variable
#   for a non-test-set var + a relationship for a non-AE domain. All gold from meta.yaml.
```

- [ ] **Step 2: 端到端 smoke — fire-through + 基数对账 meta.yaml (gold 闭环)**

```bash
.venv/bin/python - <<'PY'
import yaml
from server.config import settings
from server.meta_store import MetaStore
from server.structured_answer import StructuredAnswerer, CompositeAnswerer
from server.graph_engine import GraphEngine
from server.graph_answer import GraphAnswerer
store = MetaStore(settings.meta_path)
comp = CompositeAnswerer([StructuredAnswerer(store), GraphAnswerer(GraphEngine(store))])

def truth(subj, kind):
    if kind == "impacted_domains":
        return len(store.domains_for_codelist(subj) if subj.startswith("C")
                   else store.domains_for_variable(subj))
    if kind == "class_domains":
        return sum(1 for d in store.known_domains if store.domain_info(d)["class"] == subj)
    raise AssertionError(kind)

for q in yaml.safe_load(open("eval/test_set_sp3_graph.yml")):
    f = comp.resolve(q["question"])
    assert f is not None, f"{q['id']} did not fire"
    if "expect_subject" in q:                       # count-bearing: assert == meta.yaml truth
        want = truth(q["expect_subject"], q["expect_kind"])
        got = [c.value for c in f.checkable_counts
               if c.subject == q["expect_subject"] and c.kind == q["expect_kind"]]
        assert got and got[0] == want, f"{q['id']}: {q['expect_kind']}={got} != truth {want}"
    if "expect_advisory" in q:
        assert f.advisory_block, f"{q['id']}: advisory expected"
    print(q["id"], q["category"], "OK")
print("SP3 NL SET: all fire + cardinalities match meta.yaml")
PY
```
Expected: every g0x fires; every count-bearing question's injected cardinality equals the meta.yaml ground truth; relationship ones populate `advisory_block`. (This closes the gold loop — the `expect_*` fields are asserted, not just documented.)

- [ ] **Step 3: Commit**

```bash
git add eval/test_set_sp3_graph.yml
git commit -m "SP3 Task14: blind-authored graph NL probe set (gold from meta.yaml) + e2e smoke"
```

---

# PHASE 4 — 验收 (三门)

## Task 15: flag 翻 ON + 全套 + ruff/mypy + 运行时 smoke + Rule D

**Files:** `server/config.py`, `evidence/checkpoints/sp3_ruleD_review.md`

- [ ] **Step 1: 翻 flag ON**

```python
# server/config.py: graph_answer_enabled: bool = True  # validated: probes + battery + zero-pollution
```

- [ ] **Step 2: 全套 + lint + 运行时 smoke**

Run:
```bash
.venv/bin/python -m pytest scripts/tests -q -p no:warnings
.venv/bin/ruff check server/graph_engine.py server/graph_answer.py server/structured_answer.py server/meta_store.py scripts/tests/test_graph_engine.py scripts/tests/test_graph_answer.py
.venv/bin/mypy server/graph_engine.py server/graph_answer.py server/structured_answer.py server/meta_store.py
.venv/bin/python eval/prod_wirein/sp3_graph_probes.py
```
Expected: all green; probes ALL PASS. Plus a real `RAGEngine`-path smoke: build app via `maybe_build_answerer(Settings(graph_answer_enabled=True))`, confirm a graph query resolves through it.

- [ ] **Step 3: Rule D — 异 subagent_type 独立审**

派 `oh-my-claudecode:code-reviewer` (或 `feature-dev:code-reviewer`, ≠ writer) 审 SP3 全部新代码 + 接线。重点攻击: ① GraphEngine 是否真等于 meta.yaml ground truth (impact/aggregate)? ② 意图 over/under-fire — 有无 SP2 query 被图通道劫持 (140q 零污染真的零?)? ③ advisory 关系会不会被 LLM 当权威 (header/措辞够不够)? ④ merge_facts 去重有无丢真事实 / CompositeAnswerer 是否破坏 SP2 单通道行为? ⑤ 接地闸对 impact 基数是否正确硬校验、对 advisory 不校验? 0 BLOCKER/HIGH 才过; finding 全修后记 `sp3_ruleD_review.md`。

- [ ] **Step 4: Commit**

```bash
git add server/config.py evidence/checkpoints/sp3_ruleD_review.md
git commit -m "SP3 Task15: flag default ON (validated) + Rule D APPROVE"
```

> **GATE**: 三门 (程序门 + Rule D + Rule A Task16) 全过才算 DONE。

---

## Task 16: Rule A N=8 + 收尾 (RETROSPECTIVE + 索引 + push)

**Files:** `evidence/checkpoints/sp3_ruleA_audit.md`, `RETROSPECTIVE_sp3.md`, `KG_ROADMAP.md`, `docs/PROGRESS.md`, `.work/meta/worklog/phase_07_rag_kg.md`, `.work/AGENT_GUIDE.md`, `CLAUDE.md`, memory `project_kg_decision`

- [ ] **Step 1: Rule A — N=8 分层语义抽检 (独立 session/agent)**

8 槽 (4 能力族各 2): ①影响 (codelist C66742 / 变量 TAETORD: impacted 域集合 + 基数 vs meta.yaml + KB) ②聚合 (variables_in_min_domains(40) / class_sizes vs 原始扫描) ③结构 (same_class AE / codelist_co_users AESER vs meta.yaml) ④关系 (domain_relations AE: advisory 是否如实标注、未声称穷尽)。每槽打开 GraphAnswerer 整段输出 ↔ meta.yaml + KB 逐字段手核。记 `sp3_ruleA_audit.md`。**独立执行 (非 writer 自证)**。

- [ ] **Step 2: 写 `RETROSPECTIVE_sp3.md` (规则 C 三段)**

保留下来的做法 / 必须补上的缺口 / 关键决策复盘 (含: 意图 disjoint-from-SP2 设计是否够稳? advisory 政策有无被 LLM 突破? CompositeAnswerer 零改 router 的取舍? networkx seam 留得是否合理?)。

- [ ] **Step 3: 更新索引 (Chain B)**

- `KG_ROADMAP.md`: SP3 标 DONE; next = SP4 (可选 Neo4j) / SP5 (可选 校验器)。
- `docs/PROGRESS.md`: SP3 状态 + milestone。
- `.work/meta/worklog/phase_07_rag_kg.md`: append SP3 work record。
- `.work/AGENT_GUIDE.md` + `CLAUDE.md` Key Paths: 路由词「KG 重启 开始任务」→ SP4/SP5 (均可选; 若用户不要可视化/校验器则 KG 主线完成)。
- memory `project_kg_decision`: SP3 DONE。

- [ ] **Step 4: Commit + push**

```bash
git add -A && git commit -m "SP3 DONE 收尾: RETROSPECTIVE + Rule A N=8 + 索引更新 (next SP4/SP5 可选)" && git push
```

---

## 验收三门总览 (沿用 SP1/SP2)

| 门 | SP3 |
|----|-----|
| 程序门 | 引擎 vs raw meta.yaml 穷举对账 (Task5) + 意图 must-fire/not-fire 电池 (Task8/9) + 140q 零污染 (Task13) + 接地闸单测 (Task10) + 盲写 NL 题集端到端 (Task14) + 全套绿 + ruff/mypy + 运行时 smoke (Task15) |
| 规则 D | 异 type 独立审 APPROVE 0 BLOCKER/HIGH (Task15) |
| 规则 A | N=8 分层语义抽检 4 能力族各 2 (Task16) |

**反过拟合硬纪律 (贯穿)**: 零 q-id / 特定变量硬编 (代码只有通用语言形状 + 类名∈7 类); 实体词表 = 全量 meta.yaml; must-not-fire 电池 + held-out 探针 + 140q 零污染; Rule A 独立样本核验。
