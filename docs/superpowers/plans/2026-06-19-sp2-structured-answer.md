# SP2 — 确定性结构化答题通道 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 SP1 产出的 `data/meta/meta.yaml` 之上加一条与检索层并行的确定性答题通道, 让计数/穷举/属性/CT 查找类问题走确定数据 (q103 TAETORD→43 / q104 VISITDY→36 翻绿), 再 (Phase 2) 把 `structured_lookup.py` 的脆弱正则影子 KG 退役改读 meta.yaml。

**Architecture:** 3 个新模块全是加法、互不干扰: `MetaStore` (载 meta.yaml + 内存反向索引 + 确定性查询 API) → `StructuredAnswerer` (实体锚定 + 意图线索 → `StructuredFacts` 或 None) → 运行时 `grounding` 接地闸 (校验 LLM 计数数字, 不符追加权威更正块)。`/api/ask` 与 `/api/ask_stream` 注入权威事实块到 context 前端、completion 后挂闸; `run_eval.py` 复用同一对纯函数 (`augment_context` / `apply_counting_gate`) 保证 eval/prod 同口径。Phase 1 完全不碰检索层; Phase 2 (Phase 1 独立验收后) 把 structured_lookup 的数据源从正则解析 KB markdown 换成 MetaStore, 意图/锚定逻辑不变, 既有 `test_structured_lookup.py` 全套 + retrieval-only paired eval 作零回归门。

**Tech Stack:** Python 3.x, pydantic-settings (config), PyYAML (`yaml.safe_load`), FastAPI/Starlette (router, SSE), litellm (completion), pytest (`testpaths=["scripts/tests"]`)。工作目录 `branches/07_rag_kg/sdtm-rag/`, 虚拟环境 `.venv/bin/python`。

**关键约束 (来自 spec §2 + 个人规则):**
- 零硬编 q-id / 特定变量名; 实体词表 = 全量 meta.yaml; must-fire / must-not-fire 电池 + held-out 探针证泛化。
- 接地闸 **Phase 1 只硬校验计数类数字** (域数/变量数); 穷举列表 best-effort 不硬闸。
- 规则 A: N=8 分层语义抽检 (4 类能力各 2)。规则 B: 失败归档 `evidence/failures/`。规则 C: 收尾 RETROSPECTIVE。规则 D: 异 `subagent_type` 独立审 (Phase 1 一轮 / Phase 2 一轮)。
- config flag 初值 **OFF** (`= False`), paired eval 验证后才翻 ON。

---

## File Structure

**新增 (Phase 1):**
- `server/meta_store.py` — `MetaStore` 类 + 内存反向索引 + 查询 API
- `server/structured_answer.py` — `StructuredFacts` / `CheckableCount` dataclass + `StructuredAnswerer` + `augment_context()`
- `server/grounding.py` — `apply_counting_gate()` 运行时接地闸 (eval 复用)
- `scripts/tests/test_meta_store.py` — MetaStore 索引/查询单测
- `scripts/tests/test_structured_answer.py` — StructuredAnswerer must-fire/must-not-fire 电池
- `scripts/tests/test_grounding.py` — 接地闸单测
- `eval/prod_wirein/heldout_probes.py` — held-out 探针电池 (非测试集变量/域/CT 对账 meta.yaml)

**修改 (Phase 1):**
- `server/config.py` — 加 `structured_answer_enabled: bool = False` (L87 后, guardrail 同段)
- `server/main.py:48-64` — 实例化 `app.state.meta_store` + `app.state.answerer` (gated)
- `server/router.py` — `ask()` (L95) + `ask_stream()` (L184) 接线
- `eval/run_eval.py` — 加 `--structured-answer` flag + 答案路径接线 (L199-227 段)

**修改 (Phase 2, Phase 1 验收后):**
- `server/structured_lookup.py` — 索引构建从正则解析 KB 改读 MetaStore (退役 `len(inner)==6` 等)
- `scripts/tests/test_structured_lookup.py` — 既有全套保持绿 (零回归)
- `server/main.py` / `server/rag.py` — `StructuredLookup` 构造改注入 MetaStore

---

# PHASE 1 — 答题通道 (不碰检索层)

## Task 1: `MetaStore` 载入 meta.yaml + 正向数据访问

**Files:**
- Create: `server/meta_store.py`
- Test: `scripts/tests/test_meta_store.py`

- [ ] **Step 1: 写失败测试 (load + 正向计数)**

```python
# scripts/tests/test_meta_store.py
from pathlib import Path

import pytest

from server.config import settings
from server.meta_store import MetaStore

META_PATH = settings.meta_path  # added in Task 7; until then use literal path below


@pytest.fixture(scope="module")
def store() -> MetaStore:
    return MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")


def test_loads_and_counts(store: MetaStore):
    # counts_toward_63 domains == 63 (DI stub excluded); 1523 unique vars / 1917 entries
    assert store.n_domains == 63
    assert store.n_unique_variables == 1523
    assert store.n_variable_entries == 1917
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.meta_store'`

- [ ] **Step 3: 写最小实现 (load + 正向数据 + 计数)**

```python
# server/meta_store.py
"""KG-lite data layer: load data/meta/meta.yaml (SP1 output) once, build in-memory
reverse indices, expose deterministic query API. No networkx (that is SP3); pure dict
indices. Forward data is read-only after init; reverse indices are derived, never
materialised back to meta.yaml (avoids double-write drift, SP1 spec §3 detail e)."""
from __future__ import annotations

from pathlib import Path

import yaml


class MetaStore:
    def __init__(self, meta_path: Path):
        data = yaml.safe_load(Path(meta_path).read_text(encoding="utf-8"))
        self.meta_version: int = data["meta_version"]
        self._domains: list[dict] = data["domains"]
        self._codelists: list[dict] = data["codelists"]
        self._model_defhome: dict[str, str] = data["model_defhome"]
        # only domains that count toward the canonical 63 (DI stub excluded)
        self._real_domains: list[dict] = [d for d in self._domains if d["counts_toward_63"]]
        self._build_indices()

    def _build_indices(self) -> None:  # filled in Task 2
        pass

    @property
    def n_domains(self) -> int:
        return len(self._real_domains)

    @property
    def n_variable_entries(self) -> int:
        return sum(len(d["variables"]) for d in self._real_domains)

    @property
    def n_unique_variables(self) -> int:
        names: set[str] = set()
        for d in self._real_domains:
            names.update(v["name"] for v in d["variables"])
        return len(names)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q`
Expected: PASS (3 assertions). If `n_unique_variables`/`n_variable_entries` mismatch, the reconcile anchors (1523/1917) are authoritative — debug the meta.yaml read, not the expected values.

- [ ] **Step 5: Commit**

```bash
git add server/meta_store.py scripts/tests/test_meta_store.py
git commit -m "SP2 Task1: MetaStore load meta.yaml + forward counts (TDD)"
```

---

## Task 2: `MetaStore` 反向索引 + 查询 API

**Files:**
- Modify: `server/meta_store.py` (`_build_indices` + query methods)
- Test: `scripts/tests/test_meta_store.py`

- [ ] **Step 1: 写失败测试 (q103/q104 靶子 + 各查询)**

```python
# append to scripts/tests/test_meta_store.py
def test_domains_for_variable_counts(store: MetaStore):
    # SP1 reconcile-verified anchors; these ARE the q103/q104 targets
    assert len(store.domains_for_variable("TAETORD")) == 43
    assert len(store.domains_for_variable("VISITDY")) == 36
    # case-insensitive entry point
    assert len(store.domains_for_variable("taetord")) == 43
    # unknown variable -> empty, never raises
    assert store.domains_for_variable("NOTAVAR") == []


def test_variable_attributes(store: MetaStore):
    attr = store.variable_attributes("TAETORD")
    assert attr["label"] == "Planned Order of Element within Arm"
    assert attr["role"] == "Timing"
    assert attr["type"] == "Num"
    assert attr["core"] in {"Req", "Exp", "Perm"}
    assert store.variable_attributes("NOTAVAR") is None


def test_variables_in_domain(store: MetaStore):
    ae_vars = store.variables_in_domain("AE")
    assert "AETERM" in ae_vars
    assert store.variables_in_domain("ZZ") == []


def test_codelist_lookup(store: MetaStore):
    cl = store.codelist("C66742")
    assert cl["name"] == "No Yes Response"
    assert cl["extensible"] is False
    assert isinstance(cl["term_count"], int)
    assert store.codelist("C0000000") is None


def test_ctcode_locations_and_known_vocab(store: MetaStore):
    locs = store.locations_for_codelist("C66742")  # [(domain, var), ...]
    assert any(var == "AEPRESP" and dom == "AE" for dom, var in locs)
    assert "AETERM" in store.known_variables
    assert "AE" in store.known_domains
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q`
Expected: FAIL — `AttributeError: 'MetaStore' object has no attribute 'domains_for_variable'`

- [ ] **Step 3: 实现 `_build_indices` + 查询 API**

```python
# replace the stub _build_indices in server/meta_store.py and add query methods
    def _build_indices(self) -> None:
        # var name -> sorted list of domain codes (counts_toward_63 domains only,
        # matching VARIABLE_INDEX coverage that reconcile verified TAETORD->43)
        self._var_to_domains: dict[str, list[str]] = {}
        # var name -> attribute dict (first occurrence; standard vars share a label
        # across domains, so first-seen is canonical for label/role/type/core)
        self._var_attrs: dict[str, dict] = {}
        # domain code -> ordered list of variable names
        self._domain_to_vars: dict[str, list[str]] = {}
        # ct_code -> list of (domain, var) where it is referenced
        self._ctcode_to_locations: dict[str, list[tuple[str, str]]] = {}
        tmp_var_domains: dict[str, set[str]] = {}
        for d in self._real_domains:
            dom = d["domain"]
            self._domain_to_vars[dom] = [v["name"] for v in d["variables"]]
            for v in d["variables"]:
                name = v["name"]
                tmp_var_domains.setdefault(name, set()).add(dom)
                self._var_attrs.setdefault(name, {
                    "label": v["label"], "role": v["role"], "type": v["type"],
                    "core": v["core"], "ct_codes": list(v["ct_codes"]),
                })
                for code in v["ct_codes"]:
                    self._ctcode_to_locations.setdefault(code, []).append((dom, name))
        self._var_to_domains = {k: sorted(v) for k, v in tmp_var_domains.items()}
        # codelist code -> codelist dict
        self._codelist_by_code: dict[str, dict] = {c["ct_code"]: c for c in self._codelists}
        self.known_variables: frozenset[str] = frozenset(self._var_to_domains)
        self.known_domains: frozenset[str] = frozenset(self._domain_to_vars)
        self.known_ctcodes: frozenset[str] = frozenset(self._codelist_by_code)

    # ── deterministic query API (Phase 1) ──
    def domains_for_variable(self, var: str) -> list[str]:
        return list(self._var_to_domains.get(var.upper(), []))

    def variable_attributes(self, var: str) -> dict | None:
        a = self._var_attrs.get(var.upper())
        return dict(a) if a is not None else None

    def variables_in_domain(self, dom: str) -> list[str]:
        return list(self._domain_to_vars.get(dom.upper(), []))

    def codelist(self, ct_code: str) -> dict | None:
        c = self._codelist_by_code.get(ct_code.upper())
        return dict(c) if c is not None else None

    def locations_for_codelist(self, ct_code: str) -> list[tuple[str, str]]:
        return list(self._ctcode_to_locations.get(ct_code.upper(), []))

    def domains_for_codelist(self, ct_code: str) -> list[str]:
        return sorted({dom for dom, _ in self.locations_for_codelist(ct_code)})

    def variables_for_codelist(self, ct_code: str) -> list[str]:
        return sorted({var for _, var in self.locations_for_codelist(ct_code)})

    def model_defhome(self, var: str) -> str | None:
        return self._model_defhome.get(var.upper())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q`
Expected: PASS (all). The two count assertions (43/36) are the core capability proof.

- [ ] **Step 5: Commit**

```bash
git add server/meta_store.py scripts/tests/test_meta_store.py
git commit -m "SP2 Task2: MetaStore reverse indices + query API (TAETORD->43/VISITDY->36 green)"
```

---

## Task 3: `StructuredFacts` / `CheckableCount` + 意图检测

**Files:**
- Create: `server/structured_answer.py`
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试 (意图检测 — 通用语言形状)**

```python
# scripts/tests/test_structured_answer.py
from server.structured_answer import detect_intents


def test_count_intent():
    assert "count" in detect_intents("how many domains include taetord?")
    assert "count" in detect_intents("what is the number of domains carrying visitdy")


def test_enumerate_intent():
    assert "enumerate" in detect_intents("which domains carry visitdy?")
    assert "enumerate" in detect_intents("list all domains that include taetord")


def test_attribute_intent():
    assert "attribute" in detect_intents("what is the label of aeterm?")
    assert "attribute" in detect_intents("what role and core is aeser")


def test_codelist_intent():
    assert "codelist" in detect_intents("what codelist does aesev use?")
    assert "codelist" in detect_intents("which controlled terminology applies to route")


def test_usage_question_has_no_capability_intent():
    # must-not-fire seed: a usage/how-to question names entities but no capability cue
    assert detect_intents("how is visitdy used in practice?") == set()
    assert detect_intents("explain the purpose of the ae domain") == set()
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.structured_answer'`

- [ ] **Step 3: 写 dataclass + 意图检测**

```python
# server/structured_answer.py
"""Deterministic structured-answer channel (SP2 Phase 1).

resolve(query) anchors known entities against the full meta.yaml vocabulary, detects
generic capability-intent cues, and assembles a StructuredFacts bundle of TRUE facts to
inject into the LLM context. Conservative by construction: zero hardcoded q-ids or
variable names; intent misfire is at worst recall-additive (extra true facts), never a
wrong answer; correctness of counts is back-stopped by the grounding gate, decoupled
from intent detection."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from server.meta_store import MetaStore

# Generic language shapes — NOT tied to any q-id or variable. Each cue gates firing.
_COUNT_CUES = ("how many", "number of", "count of", "how much")
_ENUM_CUES = ("which domain", "what domain", "list ", "all domains", "every domain",
              "which variables", "what variables", "enumerate")
_ATTR_CUES = ("label", "role", "core designation", " core ", "data type", " type ",
              "what is the label", "definition of")
_CODELIST_CUES = ("codelist", "controlled term", "ct code", "terminology", "code list")


def detect_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()
    if any(c in ql for c in _COUNT_CUES):
        intents.add("count")
    if any(c in ql for c in _ENUM_CUES):
        intents.add("enumerate")
    if any(c in ql for c in _ATTR_CUES):
        intents.add("attribute")
    if any(c in ql for c in _CODELIST_CUES):
        intents.add("codelist")
    return intents


@dataclass(frozen=True)
class CheckableCount:
    subject: str   # e.g. "TAETORD"
    kind: str      # "domains" | "variables"
    value: int     # e.g. 43


@dataclass
class StructuredFacts:
    text_block: str
    checkable_counts: list[CheckableCount] = field(default_factory=list)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: PASS (5 tests). Note `test_usage_question_has_no_capability_intent` is the must-not-fire seed.

- [ ] **Step 5: Commit**

```bash
git add server/structured_answer.py scripts/tests/test_structured_answer.py
git commit -m "SP2 Task3: StructuredFacts/CheckableCount + generic intent detection (TDD)"
```

---

## Task 4: `StructuredAnswerer.resolve()` — 实体锚定 + 事实装配

**Files:**
- Modify: `server/structured_answer.py` (`StructuredAnswerer` class)
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试 (must-fire + must-not-fire 电池)**

```python
# append to scripts/tests/test_structured_answer.py
from pathlib import Path

import pytest

from server.meta_store import MetaStore
from server.structured_answer import StructuredAnswerer, CheckableCount


@pytest.fixture(scope="module")
def answerer() -> StructuredAnswerer:
    store = MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")
    return StructuredAnswerer(store)


def test_must_fire_count(answerer: StructuredAnswerer):
    facts = answerer.resolve("How many domains include TAETORD, and what is its label?")
    assert facts is not None
    assert "43" in facts.text_block
    assert "Planned Order of Element within Arm" in facts.text_block
    assert CheckableCount("TAETORD", "domains", 43) in facts.checkable_counts


def test_must_fire_enumerate_visitdy(answerer: StructuredAnswerer):
    facts = answerer.resolve("Which domains carry VISITDY?")
    assert facts is not None
    assert "36" in facts.text_block
    assert CheckableCount("VISITDY", "domains", 36) in facts.checkable_counts


def test_must_not_fire_unknown_entity(answerer: StructuredAnswerer):
    # count intent but no anchored SDTM entity and no corpus-total phrasing -> None
    assert answerer.resolve("How many patients are usually enrolled in a phase 3 study?") is None


def test_must_not_fire_usage_question(answerer: StructuredAnswerer):
    # names a known variable but no capability intent -> None (relevance guard)
    assert answerer.resolve("How is VISITDY used in a typical submission?") is None


def test_must_not_fire_bare_mention(answerer: StructuredAnswerer):
    # bare mention, no capability cue
    assert answerer.resolve("Tell me about the AE domain.") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: FAIL — `ImportError: cannot import name 'StructuredAnswerer'` (only dataclasses exist)

- [ ] **Step 3: 实现 `StructuredAnswerer`**

```python
# append to server/structured_answer.py
_VAR_TOKEN_RE = re.compile(r"\b(?:--)?[A-Z][A-Z0-9]{1,7}\b")
_CT_TOKEN_RE = re.compile(r"\bC\d{4,6}\b")


class StructuredAnswerer:
    def __init__(self, store: MetaStore):
        self.store = store

    def _anchored_variables(self, query: str) -> list[str]:
        # only uppercase tokens that are real meta.yaml variables (entity anchoring)
        return [t for t in _VAR_TOKEN_RE.findall(query) if t in self.store.known_variables]

    def _anchored_codelists(self, query: str) -> list[str]:
        return [c for c in _CT_TOKEN_RE.findall(query) if c in self.store.known_ctcodes]

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_intents(query)
        if not intents:
            return None  # must-not-fire: entity without capability intent
        variables = self._anchored_variables(query)
        codelists = self._anchored_codelists(query)
        if not variables and not codelists:
            return None  # must-not-fire: no anchored entity

        lines: list[str] = []
        counts: list[CheckableCount] = []
        for var in dict.fromkeys(variables):  # de-dupe, preserve order
            attr = self.store.variable_attributes(var)
            if attr is None:
                continue
            domains = self.store.domains_for_variable(var)
            n = len(domains)
            lines.append(
                f"- **{var}** — {attr['label']} "
                f"(Role: {attr['role']}; Type: {attr['type']}; Core: {attr['core']})."
            )
            lines.append(f"  Appears in exactly **{n}** SDTM domains: {', '.join(domains)}.")
            if attr["ct_codes"]:
                lines.append(f"  Controlled-terminology codes: {', '.join(attr['ct_codes'])}.")
            counts.append(CheckableCount(var, "domains", n))
        for code in dict.fromkeys(codelists):
            cl = self.store.codelist(code)
            if cl is None:
                continue
            doms = self.store.domains_for_codelist(code)
            lines.append(
                f"- **{code}** — codelist \"{cl['name']}\" "
                f"(extensible: {cl['extensible']}; {cl['term_count']} terms; file {cl['termfile']}). "
                f"Used in {len(doms)} domains: {', '.join(doms)}."
            )
            counts.append(CheckableCount(code, "domains", len(doms)))
        if not lines:
            return None
        return StructuredFacts(text_block="\n".join(lines), checkable_counts=counts)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: PASS (all). must-fire (count/enumerate) green; must-not-fire (unknown/usage/bare) returns None.

- [ ] **Step 5: Commit**

```bash
git add server/structured_answer.py scripts/tests/test_structured_answer.py
git commit -m "SP2 Task4: StructuredAnswerer.resolve entity-anchored fact assembly (must-fire/not-fire battery)"
```

---

## Task 4b: 域实体 + 总数 覆盖 (闭合 Q4 缺口)

> Q4 锁的能力含「域→#变量」「总域/变量数」「codelist→变量列表」, Task 4 只覆盖了变量+codelist→域。本任务补齐。域按**域代码**锚定 (Phase 1 不做长名匹配 — 那是 structured_lookup 检索侧已有的复杂逻辑, 答题侧靠代码足够; 长名锚定记为 SP3 可选增强)。总数为**注入式 best-effort** (不进 CheckableCount: 总数主语过泛, 接地闸的「主语邻近数字」启发式对它不稳; 硬闸保留给实体锚定计数, 即 q103/q104 这类最脆弱也最清晰的计数 — 落实 P2「只硬校验计数」的最稳子集, 此处显式说明不是静默收窄)。

**Files:**
- Modify: `server/meta_store.py` (`domain_info` + `_domain_by_code` 索引)
- Modify: `server/structured_answer.py` (`resolve` 加域锚定 + 总数分支 + codelist 变量列表)
- Test: `scripts/tests/test_meta_store.py` + `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试 (域计数/穷举 + 总数 + 总数需 corpus 短语)**

```python
# append to scripts/tests/test_meta_store.py
def test_domain_info(store: MetaStore):
    info = store.domain_info("AE")
    assert info["class"] == "Events"
    assert info["label"] == "Adverse Events"
    assert info["n_variables"] == len(store.variables_in_domain("AE"))
    assert store.domain_info("ZZ") is None
```

```python
# append to scripts/tests/test_structured_answer.py
def test_domain_entity_variable_count(answerer: StructuredAnswerer):
    facts = answerer.resolve("How many variables does the AE domain contain?")
    assert facts is not None
    nv = len(answerer.store.variables_in_domain("AE"))
    assert CheckableCount("AE", "variables", nv) in facts.checkable_counts
    assert str(nv) in facts.text_block


def test_domain_enumerate_variables(answerer: StructuredAnswerer):
    facts = answerer.resolve("Which variables are in the DM domain?")
    assert facts is not None
    assert "USUBJID" in facts.text_block  # a known DM variable, enumerated


def test_total_domain_count(answerer: StructuredAnswerer):
    facts = answerer.resolve("How many domains are defined in SDTM in total?")
    assert facts is not None
    assert "63" in facts.text_block


def test_total_count_requires_corpus_phrase(answerer: StructuredAnswerer):
    # count intent + "domains" but no entity and no corpus phrase -> None (conservative)
    assert answerer.resolve("How many domains do you recommend for a small study?") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py scripts/tests/test_structured_answer.py -q -k "domain_info or domain_entity or domain_enumerate or total"`
Expected: FAIL — `domain_info` missing / domain queries return None.

- [ ] **Step 3: 实现 (MetaStore.domain_info + resolve 扩展)**

```python
# server/meta_store.py — add to _build_indices (after _domain_to_vars is built):
        self._domain_by_code: dict[str, dict] = {d["domain"]: d for d in self._real_domains}

# add method:
    def domain_info(self, dom: str) -> dict | None:
        d = self._domain_by_code.get(dom.upper())
        if d is None:
            return None
        return {"domain": d["domain"], "class": d["class"], "label": d["label"],
                "structure": d["structure"], "n_variables": len(d["variables"])}
```

```python
# server/structured_answer.py — add helper + extend resolve()
    def _anchored_domains(self, query: str) -> list[str]:
        return [t for t in _VAR_TOKEN_RE.findall(query) if t in self.store.known_domains]

# inside resolve(), AFTER the variables loop and codelists loop, BEFORE `if not lines`:
        for dom in dict.fromkeys(self._anchored_domains(query)):
            info = self.store.domain_info(dom)
            if info is None:
                continue
            nv = info["n_variables"]
            lines.append(
                f"- Domain **{dom}** — {info['label']} "
                f"(Class: {info['class']}; Structure: {info['structure']}). "
                f"Contains exactly **{nv}** variables."
            )
            counts.append(CheckableCount(dom, "variables", nv))
            if "enumerate" in intents:
                lines.append(f"  Variables: {', '.join(self.store.variables_in_domain(dom))}.")

        if not lines:
            # corpus-total fallback: explicit SDTM-wide count, no specific entity anchored
            ql = query.lower()
            corpus = any(p in ql for p in ("sdtm", "in total", "altogether", "the model"))
            if corpus and ("count" in intents or "enumerate" in intents):
                if "domain" in ql:
                    lines.append(f"- SDTM defines exactly **{self.store.n_domains}** domains.")
                if "variable" in ql:
                    lines.append(
                        f"- SDTM defines **{self.store.n_unique_variables}** unique variables "
                        f"({self.store.n_variable_entries} variable entries across all domains)."
                    )
        if not lines:
            return None
        return StructuredFacts(text_block="\n".join(lines), checkable_counts=counts)
```

> Also extend the codelist branch (Task 4) to append a variables list when `"enumerate" in intents` (codelist→variables capability): `lines.append(f"  Variables using it: {', '.join(self.store.variables_for_codelist(code))}.")`. Remove the duplicate trailing `if not lines: return None` from Task 4's version — the single pair above is now the only terminator.

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py scripts/tests/test_structured_answer.py -q`
Expected: PASS (all, including the existing must-fire/must-not-fire from Task 4). Confirm `test_must_not_fire_*` still green (domain anchoring must not break them — they have no capability intent).

- [ ] **Step 5: Commit**

```bash
git add server/meta_store.py server/structured_answer.py scripts/tests/test_meta_store.py scripts/tests/test_structured_answer.py
git commit -m "SP2 Task4b: domain-entity + corpus-total + codelist->variables coverage (closes Q4)"
```

---

## Task 5: `augment_context()` — 权威事实块前置

**Files:**
- Modify: `server/structured_answer.py` (module-level helper)
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试**

```python
# append to scripts/tests/test_structured_answer.py
from server.structured_answer import augment_context, StructuredFacts


def test_augment_context_prepends_block():
    facts = StructuredFacts(text_block="- **X** — fact.", checkable_counts=[])
    out = augment_context(facts, "### [1] some_chunk\n\nbody")
    assert out.startswith("## Structured Facts (authoritative, exhaustive, from SDTM metadata)")
    assert "- **X** — fact." in out
    assert "### [1] some_chunk" in out  # original context preserved after the block


def test_augment_context_none_is_passthrough():
    assert augment_context(None, "ctx") == "ctx"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: FAIL — `ImportError: cannot import name 'augment_context'`

- [ ] **Step 3: 实现 helper**

```python
# append to server/structured_answer.py
_FACTS_HEADER = "## Structured Facts (authoritative, exhaustive, from SDTM metadata)"


def augment_context(facts: StructuredFacts | None, context: str) -> str:
    """Prepend the authoritative facts block ahead of the retrieved context.
    Shared by router.py (prod) and run_eval.py (eval) for identical wire-in."""
    if facts is None:
        return context
    return f"{_FACTS_HEADER}\n\n{facts.text_block}\n\n---\n\n{context}"
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add server/structured_answer.py scripts/tests/test_structured_answer.py
git commit -m "SP2 Task5: augment_context authoritative-block prepend helper (shared prod/eval)"
```

---

## Task 6: 计数接地闸 `apply_counting_gate()`

**Files:**
- Create: `server/grounding.py`
- Test: `scripts/tests/test_grounding.py`

- [ ] **Step 1: 写失败测试**

```python
# scripts/tests/test_grounding.py
from server.grounding import apply_counting_gate
from server.structured_answer import StructuredFacts, CheckableCount


def _facts():
    return StructuredFacts(text_block="(facts)", checkable_counts=[CheckableCount("TAETORD", "domains", 43)])


def test_correct_count_no_change():
    ans = "TAETORD appears in 43 domains."
    out, viol = apply_counting_gate(ans, _facts())
    assert out == ans
    assert viol == []


def test_wrong_count_appends_correction():
    ans = "TAETORD appears in 41 domains."
    out, viol = apply_counting_gate(ans, _facts())
    assert out != ans
    assert "Authoritative correction" in out
    assert "43" in out
    assert len(viol) == 1
    assert viol[0]["subject"] == "TAETORD" and viol[0]["expected"] == 43


def test_no_stated_number_no_violation():
    # answer does not state a count for the subject -> not a contradiction (conservative)
    ans = "TAETORD is a timing variable used across several domains."
    out, viol = apply_counting_gate(ans, _facts())
    assert out == ans
    assert viol == []


def test_no_facts_passthrough():
    assert apply_counting_gate("anything", None) == ("anything", [])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_grounding.py -q`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.grounding'`

- [ ] **Step 3: 实现接地闸**

```python
# server/grounding.py
"""Deterministic counting grounding gate (SP2 Phase 1), modelled on
eval/prod_wirein/check_code_grounding.py. Phase 1 hard-checks ONLY count-class numbers
(domain/variable counts) — the most fragile facts (q103/q104). Enumeration lists are
best-effort (injected, not gated; P2 decision). Behaviour is NON-DESTRUCTIVE (Q5): on a
contradicting number it appends an authoritative correction block, never edits the
model's original text. The same function is called at runtime (router) and in eval (to
record the violation metric) — one source of truth, no eval/prod drift."""
from __future__ import annotations

import re

from server.structured_answer import StructuredFacts

_CORRECTION_HEADER = "**Authoritative correction (SDTM metadata):**"


def _stated_numbers_near(answer: str, subject: str) -> set[int]:
    """Integers stated in sentences that mention the subject (case-insensitive).
    Conservative: only sentences naming the subject count, so an unrelated number
    elsewhere in the answer never triggers a false violation."""
    found: set[int] = set()
    subj = subject.lower()
    for sentence in re.split(r"(?<=[.!?\n])\s+", answer):
        if subj in sentence.lower():
            for m in re.findall(r"\b(\d{1,4})\b", sentence):
                found.add(int(m))
    return found


def apply_counting_gate(answer: str, facts: StructuredFacts | None) -> tuple[str, list[dict]]:
    if facts is None or not facts.checkable_counts:
        return answer, []
    violations: list[dict] = []
    corrections: list[str] = []
    for cc in facts.checkable_counts:
        stated = _stated_numbers_near(answer, cc.subject)
        # only a CONTRADICTION (a different explicit number for the subject) is a
        # violation; a missing number is not (the facts block already supplied it).
        if stated and cc.value not in stated:
            violations.append({"subject": cc.subject, "kind": cc.kind,
                               "expected": cc.value, "stated": sorted(stated)})
            corrections.append(
                f"- {cc.subject} appears in exactly {cc.value} {cc.kind}."
            )
    if not corrections:
        return answer, violations
    block = f"\n\n---\n\n{_CORRECTION_HEADER}\n" + "\n".join(corrections)
    return answer + block, violations
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_grounding.py -q`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add server/grounding.py scripts/tests/test_grounding.py
git commit -m "SP2 Task6: counting grounding gate — non-destructive correction, counts-only (TDD)"
```

---

## Task 7: config flag `structured_answer_enabled` + `meta_path`

**Files:**
- Modify: `server/config.py` (after L87 guardrail block; add `meta_path` property near `kb_root`)

- [ ] **Step 1: 写失败测试 (config + meta_path)**

```python
# append to scripts/tests/test_meta_store.py
def test_settings_meta_path_exists():
    from server.config import settings
    assert settings.meta_path.exists()
    assert settings.meta_path.name == "meta.yaml"


def test_structured_answer_flag_default_off():
    from server.config import Settings
    assert Settings().structured_answer_enabled is False  # build-time OFF until paired-eval validated
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q -k "settings or flag"`
Expected: FAIL — `AttributeError: 'Settings' object has no attribute 'structured_answer_enabled'`

- [ ] **Step 3: 加 flag + meta_path**

```python
# in server/config.py, after the prompt_guardrail_enabled block (~L87):

    # ── Structured answer channel (SP2): deterministic count/enumerate/attribute/CT
    # answers from data/meta/meta.yaml, injected as an authoritative context block +
    # a counting grounding gate. Orthogonal to retrieval (Phase 1 never touches
    # retrieve()). Env-overridable (SDTM_RAG_STRUCTURED_ANSWER_ENABLED=true). Ships
    # OFF until the OFF-vs-ON paired eval (v3 140q) validates q103/q104 green + zero
    # regression + 0 gate violations; then default flips to True.
    structured_answer_enabled: bool = False
```

```python
# add property next to kb_root (~L191):
    @property
    def meta_path(self) -> Path:
        return _SDTM_RAG_ROOT / "data" / "meta" / "meta.yaml"
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_meta_store.py -q -k "settings or flag"`
Expected: PASS. Now update the `META_PATH` line at the top of test_meta_store.py to `settings.meta_path` (it was a literal before) and re-run the full file to confirm still green.

- [ ] **Step 5: Commit**

```bash
git add server/config.py scripts/tests/test_meta_store.py
git commit -m "SP2 Task7: config structured_answer_enabled (default OFF) + settings.meta_path"
```

---

## Task 8: app 启动实例化 `StructuredAnswerer` (gated)

> **重要 (来自代码核实)**: `server/main.py` 用 `create_app` factory + `lifespan` (asynccontextmanager); `RAGEngine`/`llm_router` 在 **`lifespan` 内** (L48-64) 构造, 不在 `create_app`。直接 `create_app()` 不会跑 lifespan, 且真 `RAGEngine` init 很重 (载 chroma + 建 BM25)。所以: 把实例化逻辑抽成轻量 helper `maybe_build_answerer(s)` 单测 (快, 不碰 FastAPI), lifespan 只调它。既有测试套 (`conftest.py`) 也**绕开 lifespan**, 用裸 `FastAPI()` + 手设 `app.state.*` fake — Task 9/10 沿用此范式。

**Files:**
- Modify: `server/main.py` (`maybe_build_answerer` helper + `lifespan` 内调用)
- Test: `scripts/tests/test_structured_answer.py`

- [ ] **Step 1: 写失败测试 (helper gated)**

```python
# append to scripts/tests/test_structured_answer.py
def test_maybe_build_answerer_gated():
    from server.config import Settings
    from server.main import maybe_build_answerer
    assert maybe_build_answerer(Settings(structured_answer_enabled=False)) is None
    a = maybe_build_answerer(Settings(structured_answer_enabled=True))
    assert a is not None
    assert a.resolve("How many domains include TAETORD?") is not None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q -k maybe_build`
Expected: FAIL — `ImportError: cannot import name 'maybe_build_answerer'`

- [ ] **Step 3: 实现 helper + lifespan 接线**

```python
# server/main.py — module-level helper (testable without the app):
def maybe_build_answerer(s):
    """Build the structured-answer channel when enabled, else None. Kept tiny and
    pure so it unit-tests without spinning up FastAPI/RAGEngine (lifespan is heavy)."""
    if not s.structured_answer_enabled:
        return None
    from server.meta_store import MetaStore
    from server.structured_answer import StructuredAnswerer
    return StructuredAnswerer(MetaStore(s.meta_path))

# inside lifespan(), right after `app.state.llm_router = create_router(s)` (L64):
    app.state.answerer = maybe_build_answerer(s)
    if app.state.answerer is not None:
        log.info("structured_answer_enabled")
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_answer.py -q -k maybe_build`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add server/main.py scripts/tests/test_structured_answer.py
git commit -m "SP2 Task8: maybe_build_answerer helper + lifespan wiring (gated, testable)"
```

---

## Task 9: `ask()` 接线 — 注入事实块 + 接地闸

**Files:**
- Modify: `server/router.py` `ask()` (L95-169)
- Test: `scripts/tests/test_integration.py` (or a new `test_router_structured.py`)

- [ ] **Step 1: 写失败测试 (conftest 裸 app 范式 — 手设 app.state, 同步 fake router)**

```python
# scripts/tests/test_router_structured.py
# Mirrors conftest.py: bare FastAPI + manual app.state.* fakes (NO lifespan/create_app).
# _CtxRAG.build_messages propagates the (possibly augmented) context into messages so we
# can assert the facts block reached the LLM. The fake completion emits a WRONG count (41)
# to exercise the counting gate.
from pathlib import Path
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.meta_store import MetaStore
from server.router import api_router
from server.structured_answer import StructuredAnswerer

_META = Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"


class _CtxRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9, text="ctx")]
    def format_context(self, chunks):
        return "RETRIEVED_CTX"
    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": "sys"}, {"role": "user", "content": ctx}]


class _SyncRouter:
    def completion(self, model, messages, **kw):
        ctx = messages[-1]["content"]
        saw = "Structured Facts (authoritative" in ctx
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(
                content=f"[saw_facts={saw}] TAETORD appears in 41 domains."))],
            usage=None, model="stub")


def _app():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _CtxRAG()
    app.state.llm_router = _SyncRouter()
    app.state.settings = Settings()
    app.state.answerer = StructuredAnswerer(MetaStore(_META))
    return app


def test_ask_injects_facts_and_gate_corrects():
    r = TestClient(_app()).post("/api/ask", json={"question": "How many domains include TAETORD?"})
    assert r.status_code == 200
    ans = r.json()["answer"]
    assert "[saw_facts=True]" in ans          # facts block prepended to context
    assert "Authoritative correction" in ans  # gate caught the wrong 41 -> appends 43
    assert "43" in ans


def test_ask_passthrough_when_no_entity():
    r = TestClient(_app()).post("/api/ask", json={"question": "Give an overview of clinical trials."})
    assert r.status_code == 200
    assert "[saw_facts=False]" in r.json()["answer"]  # resolve()->None, no injection
```

> If `/api/ask` returns 422 on model validation (`AskRequest.model` defaults to `"default"`), add `"model": <an entry from router.py VALID_MODELS>` to the POST json.

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_router_structured.py -q`
Expected: FAIL — facts not injected (`saw_facts=False`), no correction block.

- [ ] **Step 3: 接线 `ask()`**

```python
# in server/router.py ask(), between format_context (L122) and build_messages (L123):
    answerer = getattr(request.app.state, "answerer", None)
    facts = answerer.resolve(body.question) if answerer is not None else None

    context = rag.format_context(chunks)
    if facts is not None:
        from server.structured_answer import augment_context
        context = augment_context(facts, context)

    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    messages = rag.build_messages(body.question, context, history_dicts or None)
    # ... existing completion call (L127) unchanged ...
    answer = response.choices[0].message.content or ""

    # grounding gate (after answer extraction, L132):
    if facts is not None:
        from server.grounding import apply_counting_gate
        answer, violations = apply_counting_gate(answer, facts)
        if violations:
            log.warning("structured_count_violation", violations=violations)
```

> Keep imports at module top per repo style if the linter prefers; inline shown for locality. The `sources`/`AskResponse` return (L142-169) is unchanged.

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_router_structured.py -q`
Expected: PASS (both). Also run full suite: `.venv/bin/python -m pytest scripts/tests -q` — zero regressions.

- [ ] **Step 5: Commit**

```bash
git add server/router.py scripts/tests/test_router_structured.py
git commit -m "SP2 Task9: wire structured-answer into /api/ask (inject facts + gate)"
```

---

## Task 10: `ask_stream()` 接线 — 累积全文后挂闸

**Files:**
- Modify: `server/router.py` `ask_stream()` (L184-260)
- Test: `scripts/tests/test_ask_stream.py` (existing file; add cases)

- [ ] **Step 1: 写失败测试 (SSE: 注入 + done 前更正 token; conftest 裸 app 范式)**

```python
# append to scripts/tests/test_ask_stream.py — mirrors the _FakeRAG/_FakeRouter pattern
# already in conftest.py / this file (bare FastAPI + manual app.state, NO lifespan).
def test_stream_injects_facts_and_appends_correction():
    from pathlib import Path
    from types import SimpleNamespace

    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from server.config import Settings
    from server.meta_store import MetaStore
    from server.router import api_router
    from server.structured_answer import StructuredAnswerer

    class _CtxRAG:
        def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
            return [SimpleNamespace(chunk_id="c1", source="s", domain="AE", file_type="spec",
                                    section="§1", similarity=0.9, text="ctx")]
        def format_context(self, chunks):
            return "RETRIEVED_CTX"
        def build_messages(self, q, ctx, history=None):
            return [{"role": "system", "content": "sys"}, {"role": "user", "content": ctx}]

    class _StreamRouter:
        async def acompletion(self, model, messages, stream=False, **kw):
            saw = "Structured Facts (authoritative" in messages[-1]["content"]
            async def agen():
                yield SimpleNamespace(model="stub", usage=None,
                    choices=[SimpleNamespace(delta=SimpleNamespace(
                        content=f"[saw={saw}] TAETORD appears in 41 domains."))])
            return agen()

    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _CtxRAG()
    app.state.llm_router = _StreamRouter()
    app.state.settings = Settings()
    app.state.answerer = StructuredAnswerer(
        MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml"))

    body = TestClient(app).post(
        "/api/ask_stream", json={"question": "How many domains include TAETORD?", "history": []}
    ).text
    assert "[saw=True]" in body
    assert "Authoritative correction" in body  # correction emitted as token(s) before done
    assert "43" in body
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_ask_stream.py -q -k structured`
Expected: FAIL — no facts injected, no correction in stream.

- [ ] **Step 3: 接线 `ask_stream()`**

```python
# in server/router.py ask_stream(), after format_context (L203) — mirror ask():
    answerer = getattr(request.app.state, "answerer", None)
    facts = answerer.resolve(body.question) if answerer is not None else None
    context = rag.format_context(chunks)
    if facts is not None:
        from server.structured_answer import augment_context
        context = augment_context(facts, context)
    # ... build_messages unchanged ...

# inside gen(), accumulate the streamed answer and run the gate before "done":
    async def gen():
        yield sse("sources", {"sources": sources})
        model_used = None
        usage = None
        parts: list[str] = []          # NEW: accumulate for the gate
        try:
            resp = await asyncio.wait_for(_open_stream(), timeout=s.request_timeout_s)
            async for chunk in resp:
                choices = getattr(chunk, "choices", None)
                if choices:
                    text = getattr(choices[0].delta, "content", None)
                    if text:
                        parts.append(text)          # NEW
                        yield sse("token", {"text": text})
                    model_used = getattr(chunk, "model", None) or model_used
                cu = getattr(chunk, "usage", None)
                if cu:
                    usage = {"prompt_tokens": cu.prompt_tokens,
                             "completion_tokens": cu.completion_tokens,
                             "total_tokens": cu.total_tokens}
            # NEW: counting gate on the assembled answer; emit correction as token(s)
            if facts is not None:
                from server.grounding import apply_counting_gate
                full = "".join(parts)
                corrected, violations = apply_counting_gate(full, facts)
                if violations:
                    log.warning("structured_count_violation_stream", violations=violations)
                    yield sse("token", {"text": corrected[len(full):]})  # only the appended block
            yield sse("done", {"model_used": model_used or "default", "usage": usage})
        except Exception as e:  # noqa: BLE001
            log.error("stream_failed", error=str(e), exc_info=True)
            yield sse("error", {"message": "LLM stream failed"})
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_ask_stream.py -q`
Expected: PASS (new + existing stream tests). Full suite: `.venv/bin/python -m pytest scripts/tests -q`.

- [ ] **Step 5: Commit**

```bash
git add server/router.py scripts/tests/test_ask_stream.py
git commit -m "SP2 Task10: wire structured-answer into /api/ask_stream (accumulate + gate before done)"
```

---

## Task 11: `run_eval.py` 接线 — `--structured-answer` flag

**Files:**
- Modify: `eval/run_eval.py` (arg parser; answer path L199-227; RAGEngine block L516-541 for parity)
- Test: `scripts/tests/test_run_eval_judge.py` (existing; add a wiring smoke test) — or a focused unit test of the eval answer-builder.

- [ ] **Step 1: 写失败测试 (eval answer path 注入事实块)**

```python
# append to scripts/tests/test_run_eval_judge.py — assert eval applies the same channel
def test_eval_answer_path_injects_facts(monkeypatch, tmp_path):
    # Build the structured-answer helper the same way run_eval will, and assert the
    # eval context-builder prepends facts identically to prod (parity check).
    from pathlib import Path
    from server.meta_store import MetaStore
    from server.structured_answer import StructuredAnswerer, augment_context

    store = MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")
    answerer = StructuredAnswerer(store)
    facts = answerer.resolve("How many domains include TAETORD?")
    ctx = augment_context(facts, "### [1] chunk\n\nbody")
    assert "Structured Facts (authoritative" in ctx and "43" in ctx
```

> This locks the parity contract (eval uses the SAME `augment_context` + `apply_counting_gate`). The CLI flag wiring below is then mechanical.

- [ ] **Step 2: 跑测试确认失败 → 通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_run_eval_judge.py -q -k injects_facts`
Expected: PASS immediately (helpers already exist from Tasks 4-6) — this test guards parity, not new code.

- [ ] **Step 3: 加 CLI flag + 答案路径接线 (run_evaluation 加显式 `answerer` 参数)**

`run_evaluation` 现签名 (核实, L181): `run_evaluation(test_set, rag, router=None, retrieval_only=False, direct_model=None, top_k=TOP_K, temperature=None, full_answers=False, judge=False, judge_model=DEFAULT_JUDGE_MODEL)` — 不收 `args`。加一个显式 `answerer` 参数, 由 `main()` (持 args, 调用点 L570) 构造并传入。

```python
# eval/run_eval.py — argparser (near --structured-lookup / --hybrid / --guardrail):
    parser.add_argument("--structured-answer", action="store_true",
                        help="SP2: inject meta.yaml authoritative facts + counting gate")

# run_evaluation signature: add `answerer=None` (keyword, default None — retrieval-only
# and legacy callers unaffected):
def run_evaluation(test_set, rag, router=None, retrieval_only=False, direct_model=None,
                   top_k=TOP_K, temperature=None, full_answers=False, judge=False,
                   judge_model=DEFAULT_JUDGE_MODEL, answerer=None) -> list[dict]:

# in the answer path, replace L218-219 (context/messages build):
            context = rag.format_context(chunks)
            facts = answerer.resolve(q["question"]) if answerer is not None else None
            if facts is not None:
                from server.structured_answer import augment_context
                context = augment_context(facts, context)
            messages = rag.build_messages(q["question"], context)
            # ... existing completion retry loop (L221-232) unchanged ...
            # AFTER answer is extracted from response.choices[0].message.content:
            if facts is not None:
                from server.grounding import apply_counting_gate
                answer, _viol = apply_counting_gate(answer, facts)

# in main(), build answerer from args and pass at the L570 call site:
    answerer = None
    if args.structured_answer:
        from server.meta_store import MetaStore
        from server.structured_answer import StructuredAnswerer
        answerer = StructuredAnswerer(MetaStore(settings.meta_path))
    results = run_evaluation(test_set, rag, router=router, ..., answerer=answerer)  # add kwarg

# summary block (near L594-601):
    summary["structured_answer"] = args.structured_answer
```

> Find the exact name the answer-extraction variable uses at L227-232 (the `response.choices[0].message.content` assignment) and apply the gate immediately after it, before the result dict is appended.

- [ ] **Step 4: 跑测试 + smoke**

Run: `.venv/bin/python -m pytest scripts/tests/test_run_eval_judge.py -q`
Then a 2-question smoke (no judge, cheap): `.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --structured-answer --temperature 0 --full-answers --output /tmp/sp2_smoke.json` then confirm `/tmp/sp2_smoke.json` has `"structured_answer": true` and q103/q104 answers contain 43/36. (If a full 140q run is too costly here, slice to q103/q104 per the existing eval's question-filter mechanism.)

- [ ] **Step 5: Commit**

```bash
git add eval/run_eval.py scripts/tests/test_run_eval_judge.py
git commit -m "SP2 Task11: run_eval --structured-answer wiring (eval/prod parity via shared helpers)"
```

---

## Task 12: Held-out 探针电池 (反过拟合)

**Files:**
- Create: `eval/prod_wirein/heldout_probes.py`
- Test: (the probe script IS the test; it asserts against reconcile-verified meta.yaml)

- [ ] **Step 1: 写探针脚本 (非测试集变量/域/CT, 四类能力)**

```python
# eval/prod_wirein/heldout_probes.py
"""Held-out anti-overfitting probe battery: count/enumerate/attribute/CT queries over
variables/domains/CT codes that are NOT in test_set_v3 (q103/q104 et al.), asserting the
StructuredAnswerer's facts match the reconcile-verified meta.yaml. Proves pattern-level
generalisation, not memorised q-ids. Run: .venv/bin/python eval/prod_wirein/heldout_probes.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.meta_store import MetaStore  # noqa: E402
from server.structured_answer import StructuredAnswerer, CheckableCount  # noqa: E402

# Held-out entities — chosen because they are NOT the eval test-set targets (TAETORD/
# VISITDY). Truth values come from meta.yaml itself, so this self-checks consistency of
# the answerer vs the store across many entities (not a single example).
PROBES = [
    ("How many domains include EPOCH?", "EPOCH", "domains"),
    ("Which domains carry USUBJID?", "USUBJID", "domains"),
    ("What is the label and role of DTHFL?", "DTHFL", None),
    ("How many domains use codelist C66742?", "C66742", "domains"),
]


def main() -> int:
    store = MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")
    ans = StructuredAnswerer(store)
    failures = 0
    for query, subject, kind in PROBES:
        facts = ans.resolve(query)
        if facts is None:
            print(f"FAIL  resolve()=None for: {query}")
            failures += 1
            continue
        if kind == "domains":
            if subject.startswith("C"):
                truth = len(store.domains_for_codelist(subject))
            else:
                truth = len(store.domains_for_variable(subject))
            cc = CheckableCount(subject, "domains", truth)
            ok = cc in facts.checkable_counts and str(truth) in facts.text_block
            print(f"{'PASS' if ok else 'FAIL'}  {subject} domains={truth}")
            failures += 0 if ok else 1
        else:  # attribute probe
            attr = store.variable_attributes(subject)
            ok = attr is not None and attr["label"] in facts.text_block
            print(f"{'PASS' if ok else 'FAIL'}  {subject} attribute label present={ok}")
            failures += 0 if ok else 1
    print(f"\nHELD-OUT PROBES: {len(PROBES)-failures}/{len(PROBES)} PASS")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: 跑探针**

Run: `.venv/bin/python eval/prod_wirein/heldout_probes.py`
Expected: all PASS (`HELD-OUT PROBES: 4/4 PASS`). If any FAIL, the answerer/store disagree — fix before proceeding (this is the generalisation gate).

- [ ] **Step 3: Commit**

```bash
git add eval/prod_wirein/heldout_probes.py
git commit -m "SP2 Task12: held-out anti-overfitting probe battery (non-test-set entities)"
```

---

## Task 13: Phase 1 OFF-vs-ON paired eval + 接地闸 0 violation

**Files:** none (verification task — produces evidence)

- [ ] **Step 1: 跑 OFF arm (baseline, structured-answer 关)**

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
  --model deepseek/deepseek-chat --temperature 0 --structured-lookup --hybrid \
  --full-answers --output eval/prod_wirein/v3_sp2_off_t0.json
```

- [ ] **Step 2: 跑 ON arm (structured-answer 开)**

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
  --model deepseek/deepseek-chat --temperature 0 --structured-lookup --hybrid \
  --structured-answer \
  --full-answers --output eval/prod_wirein/v3_sp2_on_t0.json
```

- [ ] **Step 3: paired 分析 + judge + q103/q104 翻绿确认**

```bash
.venv/bin/python eval/prod_wirein/analyze_paired.py \
  eval/prod_wirein/v3_sp2_off_t0.json eval/prod_wirein/v3_sp2_on_t0.json \
  | tee eval/prod_wirein/v3_sp2_paired_t0.log
```
检查 (写进 evidence): q103 facts 含 "43"+label / q104 含 "36"+label 翻绿; 全类目 paired **零回归** (任何类目 ON < OFF 即阻塞, 须诊断); 其余题不被注入污染 (must-not-fire 抽查)。

- [ ] **Step 4: 接地闸 0 violation**

```bash
.venv/bin/python eval/prod_wirein/check_code_grounding.py eval/prod_wirein/v3_sp2_on_t0.json on
# AND run the counting gate over the ON arm answers; assert 0 count violations.
```
把 ON arm 每题答案过 `apply_counting_gate` (写个 5 行 driver 或扩展 check 脚本), 断言 count violation 总数 == 0。

- [ ] **Step 5: 归档证据 + 失败归档**

写 `evidence/checkpoints/sp2_phase1_paired_eval.md` (OFF/ON 数字表 + q103/q104 翻绿截图行 + 零回归确认 + 0 violation)。任何 attempt 失败 → `evidence/failures/step_13_attempt_X.md` (规则 B)。

```bash
git add eval/prod_wirein/v3_sp2_*.json eval/prod_wirein/v3_sp2_paired_t0.log evidence/checkpoints/sp2_phase1_paired_eval.md
git commit -m "SP2 Task13: Phase1 OFF-vs-ON paired eval — q103/q104 green, zero regression, 0 violations"
```

---

## Task 14: Phase 1 验收 — 规则 D 独立审 + 规则 A N=8

**Files:** `evidence/checkpoints/sp2_phase1_ruleA_audit.md`, `evidence/checkpoints/sp2_phase1_ruleD_review.md`

- [ ] **Step 1: 翻 flag 默认 ON (验证已过)**

```python
# server/config.py: structured_answer_enabled: bool = True  # paired eval validated (Task13)
```
Run full suite: `.venv/bin/python -m pytest scripts/tests -q` + `ruff check .` + `mypy server/` — all clean.

- [ ] **Step 2: 规则 D — 异 subagent_type 独立代码审 (Phase 1)**

派 `oh-my-claudecode:code-reviewer` (或 `feature-dev:code-reviewer`) 审 Phase 1 全部新代码 (meta_store / structured_answer / grounding / router 接线 / eval 接线)。Writer ≠ reviewer。0 BLOCKER/HIGH 才过; finding 全修后记 `sp2_phase1_ruleD_review.md`。

- [ ] **Step 3: 规则 A — N=8 分层语义抽检**

8 槽 (4 类能力各 2): ①计数 TAETORD/VISITDY ②穷举 (变量→域列表 vs meta.yaml; codelist→域列表) ③属性 (label/role/type/core 对 spec.md) ④CT (变量→ct_codes / codelist 元数据)。每槽打开 answerer 输出 ↔ 打开 meta.yaml + KB source 逐字段手核, 证「用户看到的整段答案」语义对。记 `sp2_phase1_ruleA_audit.md`。**独立 session/agent 执行 (规则 A 要求独立样本核验, 非 writer 自证)**。

- [ ] **Step 4: Commit Phase 1 收口**

```bash
git add server/config.py evidence/checkpoints/sp2_phase1_*.md
git commit -m "SP2 Phase1 DONE: flag default ON; Rule D APPROVE + Rule A N=8 PASS"
```

> **GATE**: Phase 1 三门全过才开 Phase 2。未过则迭代, 不前进。

---

# PHASE 2 — 退役正则影子 KG (Phase 1 验收后)

> 把 `structured_lookup.py` 的数据源从「正则解析 KB markdown」换成 MetaStore/meta.yaml, **意图检测 / 锚定 / resolve 逻辑全不变**。既有 `test_structured_lookup.py` (canaries RDOMAIN→model/06, EPOCH→model/03, gating, collision, hygiene) + retrieval-only paired eval 作零回归门。

## Task 15: `StructuredLookup` 索引改由 MetaStore 供数 (行为等价)

**Files:**
- Modify: `server/structured_lookup.py` (`__init__` 接受 MetaStore; `_build_*_index` 改读 MetaStore)
- Test: `scripts/tests/test_structured_lookup.py` (既有全套, 不改断言 — 零回归证)

- [ ] **Step 1: 确认既有测试基线全绿 (改前快照)**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q`
Expected: PASS (记下数量, 如 35 passed)。这是 Phase 2 的回归靶。

- [ ] **Step 2: 让 `StructuredLookup` 接受 MetaStore, 索引从它派生**

逐个替换 (每个 build 方法一个 commit, 每步后跑全套测试保持绿):
- `var_to_model_defhome` ← `MetaStore._model_defhome` (**退役 `len(inner)==6` 正则解析 model/*.md**; canary `test_defhome_canary_rdomain`/`epoch_six_col_isolation` 守等价)。
- `ctcode_to_termfile` ← `{c: cl["termfile"] for c, cl in MetaStore._codelist_by_code}`。
- `var_to_termfiles` ← 组合 `MetaStore.variable_attributes(var)["ct_codes"]` × codelist termfile (退役 spec.md Cross-References 正则 + `_cross_check_vars` 截断尾修补)。
- `domain_to_spec` ← `{dom: f"domains/{dom}/spec.md" for dom in MetaStore.known_domains}`。
- `ctcode_to_vars` ← `MetaStore.variables_for_codelist` (或 locations)。
- `known_variables` ← `MetaStore.known_variables`。
- `domain_longname_to_code` ← `{d["label"].lower(): d["domain"]}` from MetaStore (longname 匹配/anchor/slash-variant 逻辑**保留**, 仅数据源换)。
- `general_assumptions_file` (ch04): meta.yaml 不覆盖 → **保留现有 ch04 glob** (注释说明这是 meta.yaml 未涵盖的唯一保留 glob)。

```python
# server/structured_lookup.py __init__ signature change:
    def __init__(self, kb_root: Path, store: MetaStore):
        self.kb_root = kb_root
        self.store = store
        # ... build indices from store, not regex; keep ch04 glob ...
```

- [ ] **Step 3: 每替换一个索引跑全套测试**

Run after EACH index migration: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q`
Expected: PASS, same count as Step 1 baseline. **任何 canary 红 = 行为不等价, 立即回退该步** (规则 B 归档失败 attempt)。

- [ ] **Step 4: 删除已死的正则解析代码**

`len(inner)==6` 块 / `_cross_check_vars` / spec.md xref 正则 / model/*.md 解析 全部删除 (确认无引用)。再跑全套 + `ruff` + `mypy`。

- [ ] **Step 5: Commit (每索引一 commit, 收口一 commit)**

```bash
git add server/structured_lookup.py server/main.py server/rag.py
git commit -m "SP2 Task15: structured_lookup data source meta.yaml-backed; retire len==6 regex (tests green)"
```

---

## Task 16: Phase 2 retrieval-only paired eval (零回归)

**Files:** `evidence/checkpoints/sp2_phase2_paired_eval.md`

- [ ] **Step 1: retrieval-only paired (现状 vs meta.yaml-backed)**

```bash
# baseline 已有 (现 99%); 重跑 meta.yaml-backed arm:
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
  --model deepseek/deepseek-chat --temperature 0 --structured-lookup --hybrid \
  --full-answers --output eval/prod_wirein/v3_sp2p2_on_t0.json
.venv/bin/python eval/prod_wirein/analyze_paired.py \
  eval/prod_wirein/v3_full_on_t0.json eval/prod_wirein/v3_sp2p2_on_t0.json \
  | tee eval/prod_wirein/v3_sp2p2_paired.log
```
断言: ≥ 现 99% **零回归** (retrieval 检索质量不动)。

- [ ] **Step 2: 反过拟合探针电池不变 + 既有 test_structured_lookup 全绿**

Run: `.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q` + `.venv/bin/python eval/prod_wirein/heldout_probes.py`

- [ ] **Step 3: 归档 + Commit**

```bash
git add eval/prod_wirein/v3_sp2p2_*.json eval/prod_wirein/v3_sp2p2_paired.log evidence/checkpoints/sp2_phase2_paired_eval.md
git commit -m "SP2 Task16: Phase2 retrieval-only paired — zero regression vs 99%"
```

---

## Task 17: Phase 2 验收 — 规则 D 独立审

**Files:** `evidence/checkpoints/sp2_phase2_ruleD_review.md`

- [ ] **Step 1: 异 subagent_type 独立审 Phase 2 改动**

派 reviewer agent 审 structured_lookup 迁移 (尤其: `len==6` 退役行为是否真等价? meta.yaml 派生的 var_to_termfiles 是否漏 termfile? ch04 glob 保留是否合理?)。0 BLOCKER/HIGH 才过。

- [ ] **Step 2: Commit**

```bash
git add evidence/checkpoints/sp2_phase2_ruleD_review.md
git commit -m "SP2 Phase2 DONE: Rule D APPROVE (len==6 retirement behavior-equivalent)"
```

---

## Task 18: 收尾 — RETROSPECTIVE (规则 C) + 索引更新

**Files:** `RETROSPECTIVE_sp2.md`, `KG_ROADMAP.md`, `SP2_structured_answer_design.md`, `docs/PROGRESS.md`, `.work/meta/worklog/phase07.md`

- [ ] **Step 1: 写 RETROSPECTIVE_sp2.md (规则 C 三段)**

保留下来的做法 / 必须补上的缺口 / 关键决策复盘 (含: 接地闸只校验计数是否够? must-not-fire 设计是否漏案例? Phase 2 len==6 退役有无惊喜?)。

- [ ] **Step 2: 更新索引 (Chain B)**

- `KG_ROADMAP.md`: SP2 标 DONE; 指向 spec/plan/evidence; next = SP3 (内存图遍历)。
- `SP2_structured_answer_design.md` draft → 指向定稿 spec, 或归档。
- `docs/PROGRESS.md`: SP2 状态。
- `.work/meta/worklog/phase07.md`: append SP2 work record。
- memory `project_kg_decision`: SP2 DONE。

- [ ] **Step 3: Commit + push**

```bash
git add -A && git commit -m "SP2 收尾: RETROSPECTIVE + 索引更新 (SP2 DONE, next SP3)" && git push
```

---

## 验收三门总览 (沿用 SP1)

| 门 | Phase 1 | Phase 2 |
|----|---------|---------|
| 程序门 | OFF-vs-ON paired (q103/q104 翻绿, 零回归) + held-out 探针 + 单测全绿 + 接地闸 0 violation | retrieval-only paired ≥99% 零回归 + test_structured_lookup 全绿 + 探针不变 |
| 规则 D | 异 type 独立审 APPROVE (Task14) | 异 type 独立审 APPROVE (Task17) |
| 规则 A | N=8 分层语义抽检 (Task14) | (Phase 2 无新答题语义, 检索零回归即证) |

**反过拟合硬纪律 (贯穿)**: 零 q-id/特定变量硬编 (代码里只有通用语言形状); 实体词表=全量 meta.yaml; must-not-fire 电池 (Task4) + held-out 探针 (Task12); 规则 A 独立样本核验。
</content>
</invoke>
