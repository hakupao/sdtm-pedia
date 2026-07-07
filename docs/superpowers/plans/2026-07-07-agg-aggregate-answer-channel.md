# AGG 独立答题通道 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 aggregate 聚合能力 (variables_in_min_domains / most_shared_codelists) 从 SP3 graph_answer 拆成独立 `AggregateAnswerer` 通道, 用 pattern-level 触发检测把 fire-rate 从 2/10 提到 held-out ≥80%, 五道验收门全过后默认 ON。

**Architecture:** 新 `server/aggregate_answer.py` (检测 + 装配, 装配逐字平移自 graph_answer) 注册进 CompositeAnswerer (顺序 SP2 → AGG → SP3); graph_answer 删 aggregate 分支回归纯图; SP2 `StructuredAnswerer` 零改动。Spec: `docs/superpowers/specs/2026-07-07-aggregate-answer-widening-design.md` (已批准)。

**Tech Stack:** Python 3.12 (`.venv`), pydantic-settings, pytest, run_eval.py 评测框架, deepseek API (端到端臂)。

## Global Constraints

- 工作目录: 所有相对路径以 `branches/07_rag_kg/sdtm-rag/` 为根, 除非写明 repo-root。命令都从 `branches/07_rag_kg/sdtm-rag/` 执行。
- Python 一律 `.venv/bin/python`; pytest 一律 `.venv/bin/python -m pytest`。
- **反过拟合硬纪律**: `server/` 代码零硬编 q-id / 特定变量名; **kgval 40 题 (eval/test_set_kg_value.yml) 不得作为 pattern 设计输入**, 只作回归对照; held-out 题必须盲写 (写手不见触发词表 / 不见 server 代码 / 不见 kgval 题)。
- **注入行文 byte-identical**: threshold / most-shared 两种事实行的 f-string 格式必须与 SP3 遗留格式逐字相同 (Task 2 golden 单测钉死)。
- **只做下界**: 引擎只有 `variables_in_min_domains` (≥ 语义); 上界表达 ("fewer than"/"at most"/"no more than"/"or fewer") 必须不触发。
- config flag `aggregate_answer_enabled` 初值 **False**, 仅 Task 8 全门过后翻 True。
- 每个 task 结尾 commit; 失败 attempt 按规则 B 归档 `branches/07_rag_kg/sdtm-rag/evidence/failures/agg_attempt_N.md`, 不删。
- Tier 2 流程: Rule D (Task 9, 异 subagent_type) + Rule A (Task 9, N=6 独立抽检) 是硬门, 不可跳。

---

### Task 1: 触发检测模块 `detect_aggregate_intents` (TDD)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/server/aggregate_answer.py` (本 task 只有检测部分)
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_aggregate_answer.py`

**Interfaces:**
- Consumes: `server.structured_answer._CODELIST_CUES` (既有常量: `("codelist", "controlled term", "ct code", "terminology", "code list")`)
- Produces: `detect_aggregate_intents(query: str) -> set[str]`, 返回值 ⊆ `{"threshold", "superlative"}`; 模块级 regex `_THRESH_STRICT_RE` / `_THRESH_INCL_PRE_RE` / `_THRESH_INCL_POST_RE` (Task 2 resolve 复用, 捕获组 1 = 数字)

- [ ] **Step 1: 写失败测试 (检测电池)**

创建 `scripts/tests/test_aggregate_answer.py`:

```python
# scripts/tests/test_aggregate_answer.py
import pytest

from server.aggregate_answer import AggregateAnswerer, detect_aggregate_intents
from server.config import settings
from server.graph_engine import GraphEngine
from server.meta_store import MetaStore

# ── detection: must-fire, 每个语言形状家族 ≥3 例 ──────────────────────────────


def test_threshold_prefix_strict_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in more than 30 domains?")
    assert "threshold" in detect_aggregate_intents(
        "List the variables found in greater than 10 SDTM domains.")
    assert "threshold" in detect_aggregate_intents(
        "Are there variables used in over 20 domains?")
    assert "threshold" in detect_aggregate_intents(
        "Which variables exceed 15 domains in terms of variable usage?")


def test_threshold_prefix_inclusive_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in at least 40 domains?")
    assert "threshold" in detect_aggregate_intents(
        "Show the variables present in a minimum of 5 domains.")
    assert "threshold" in detect_aggregate_intents(
        "Which variables occur in no fewer than 8 domains?")


def test_threshold_postfix_inclusive_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables show up in 3 or more domains?")
    assert "threshold" in detect_aggregate_intents(
        "Any variables used across 40+ domains?")
    assert "threshold" in detect_aggregate_intents(
        "Which variables span 10 or greater domains?")


def test_superlative_fires():
    assert "superlative" in detect_aggregate_intents(
        "What is the most shared codelist?")
    assert "superlative" in detect_aggregate_intents(
        "Which codelist is most widely used across domains?")
    assert "superlative" in detect_aggregate_intents(
        "What's the most reused controlled terminology?")
    assert "superlative" in detect_aggregate_intents(
        "Which code list is used by the largest number of variables?")


# ── detection: must-not-fire ─────────────────────────────────────────────────


def test_upper_bound_must_not_fire():
    # 引擎只有 >= 语义; 上界触发会注入方向错误的事实
    assert detect_aggregate_intents("Which variables appear in fewer than 5 domains?") == set()
    assert detect_aggregate_intents("Which variables are in at most 3 domains?") == set()
    assert detect_aggregate_intents("Variables in no more than 10 domains?") == set()
    assert detect_aggregate_intents("Which variables appear in 5 or fewer domains?") == set()
    assert detect_aggregate_intents("Variables in not more than 6 domains?") == set()


def test_sp2_territory_must_not_fire():
    assert detect_aggregate_intents("How many domains include TAETORD?") == set()
    assert detect_aggregate_intents("Which domains use the VISITNUM variable?") == set()


def test_prose_superlative_without_codelist_cue_must_not_fire():
    assert detect_aggregate_intents("What are the most common adverse events?") == set()
    assert detect_aggregate_intents("Which domain is most frequently used in trials?") == set()


def test_threshold_without_number_or_context_must_not_fire():
    assert detect_aggregate_intents("Which variables appear in many domains?") == set()
    # 有数字有 variable 但无 "domain" → 不触发 (沿用 SP3 双词共现门语义)
    assert detect_aggregate_intents("How many variables are in more than 5 records?") == set()
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_aggregate_answer.py -v`
Expected: 全部 FAIL, `ModuleNotFoundError: No module named 'server.aggregate_answer'` (或 ImportError)

- [ ] **Step 3: 写检测实现**

创建 `server/aggregate_answer.py`:

```python
"""AGG channel: aggregate metadata queries (variables-in-min-domains / most-shared
codelists) as an independent deterministic answerer.

Split out of SP3 graph_answer (KG value eval 2026-06-21: aggregate was SP3's only
positive niche, +11~17pp when fired, but the legacy cue set fired on just 2/10 natural
phrasings). Detection is pattern-level over English quantity-threshold and superlative
shapes — zero hardcoded q-ids, no phrases lifted from any eval set.

Safety model matches SP2/SP3: a misfire injects at worst recall-additive TRUE facts.
Lower-bound thresholds only: the engine exposes variables_in_min_domains (>= semantics);
upper-bound phrasings ("fewer than", "at most", "no more than", "or fewer") MUST NOT
fire — they would inject facts answering the wrong direction.
"""
from __future__ import annotations

import re

from server.graph_engine import GraphEngine
from server.structured_answer import _CODELIST_CUES, StructuredFacts

# Lower-bound threshold shapes. Strict (exclusive) -> engine threshold n+1; inclusive
# -> n. Fixed-width lookbehinds keep "no more than 5" / "not more than 5" (upper
# bounds) out of the strict family. Group 1 is always the number.
_THRESH_STRICT_RE = re.compile(
    r"\b(?:(?<!no )(?<!not )more than|greater than|over|exceeds?|exceeding)\s+(\d{1,3})\b",
    re.IGNORECASE)
_THRESH_INCL_PRE_RE = re.compile(
    r"\b(?:at least|a minimum of|no fewer than|no less than)\s+(\d{1,3})\b",
    re.IGNORECASE)
_THRESH_INCL_POST_RE = re.compile(
    r"\b(\d{1,3})\s*(?:or more|or greater|and above|\+)",
    re.IGNORECASE)

# Superlative shapes for most-shared codelists: "most shared/used/reused/common ...",
# optionally with an -ly adverb ("most widely used"), plus "largest number of" style.
_SUPERLATIVE_RE = re.compile(
    r"\bmost\s+(?:\w+ly\s+)?(?:shared|used|reused|common\w*|frequent\w*|prevalent|popular)\b"
    r"|\b(?:largest|highest|greatest|biggest)\s+number\s+of\b",
    re.IGNORECASE)


def detect_aggregate_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()
    # threshold: a lower-bound quantity shape AND both context words (co-occurrence
    # gate, carried over from the SP3 semantics)
    if ("variable" in ql and "domain" in ql and (
            _THRESH_STRICT_RE.search(query)
            or _THRESH_INCL_PRE_RE.search(query)
            or _THRESH_INCL_POST_RE.search(query))):
        intents.add("threshold")
    # superlative: a superlative shape AND a codelist context cue (blocks prose like
    # "most common adverse events")
    if _SUPERLATIVE_RE.search(query) and any(c in ql for c in _CODELIST_CUES):
        intents.add("superlative")
    return intents


class AggregateAnswerer:
    """Deterministic aggregate answerer over GraphEngine (read-only, stateless).
    resolve() is implemented in Task 2."""

    def __init__(self, engine: GraphEngine):
        self.engine = engine

    def resolve(self, query: str) -> StructuredFacts | None:
        raise NotImplementedError  # Task 2
```

- [ ] **Step 4: 跑检测测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_aggregate_answer.py -v`
Expected: 8 个检测测试 PASS (resolve 类测试尚未写)

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/aggregate_answer.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_aggregate_answer.py
git commit -m "feat(agg): pattern-level aggregate intent detection (threshold/superlative, lower-bound only)"
```

---

### Task 2: `AggregateAnswerer.resolve` 装配 + golden 等价 (TDD)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/aggregate_answer.py` (补 resolve)
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_aggregate_answer.py` (追加)

**Interfaces:**
- Consumes: `GraphEngine.variables_in_min_domains(n: int) -> list[tuple[str, int]]`; `GraphEngine.most_shared_codelists(k: int = 10) -> list[dict]` (keys: code/name/n_variables/n_domains); Task 1 的三个 threshold regex
- Produces: `AggregateAnswerer.resolve(query: str) -> StructuredFacts | None` — `checkable_counts` 恒为 `[]`, `advisory_block` 恒为 `""` (spec §4: 不新增 grounding kind)

- [ ] **Step 1: 写失败测试 (resolve 电池 + golden)**

追加到 `scripts/tests/test_aggregate_answer.py`:

```python
# ── resolve() battery ────────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def agg() -> AggregateAnswerer:
    return AggregateAnswerer(GraphEngine(MetaStore(settings.meta_path)))


def test_threshold_strict_excludes_exact_boundary(agg):
    # "more than 40" 严格 (>40): 恰好 40 域的变量必须不出现
    facts = agg.resolve("Which variables appear in more than 40 domains?")
    assert facts is not None
    exact40 = [v for v, c in agg.engine.variables_in_min_domains(40) if c == 40]
    for v in exact40:
        assert v not in facts.text_block


def test_threshold_inclusive_includes_exact_boundary(agg):
    facts = agg.resolve("Which variables appear in at least 40 domains?")
    assert facts is not None
    exact40 = [v for v, c in agg.engine.variables_in_min_domains(40) if c == 40]
    if exact40:
        assert any(v in facts.text_block for v in exact40)


def test_threshold_n_from_expression_not_first_digit(agg):
    # 旧 graph_answer 抓 query 里第一个裸数字 (此例会错抓 5); 新装配必须从阈值表达取数
    facts = agg.resolve("List 5 variables that appear in more than 40 domains.")
    assert facts is not None
    n_gt40 = len(agg.engine.variables_in_min_domains(41))
    assert f"**{n_gt40}**" in facts.text_block
    assert ">40" in facts.text_block


def test_postfix_threshold_resolves(agg):
    facts = agg.resolve("Which variables show up in 30 or more domains?")
    assert facts is not None
    n = len(agg.engine.variables_in_min_domains(30))
    assert f"**{n}**" in facts.text_block
    assert "≥30" in facts.text_block


def test_superlative_top5_matches_engine(agg):
    facts = agg.resolve("What is the most shared codelist?")
    assert facts is not None
    for t in agg.engine.most_shared_codelists(5):
        assert t["code"] in facts.text_block


def test_no_counts_no_advisory(agg):
    facts = agg.resolve("Which variables appear in at least 30 domains?")
    assert facts is not None
    assert facts.checkable_counts == []
    assert facts.advisory_block == ""


def test_resolve_none_when_no_intent(agg):
    assert agg.resolve("How many domains include TAETORD?") is None
    assert agg.resolve("What are the most common adverse events?") is None


# ── golden: 注入行文与 SP3 遗留格式逐字相同 (kgval 已证有效, 格式不许漂移) ──────


def test_golden_threshold_line_format(agg):
    res = agg.engine.variables_in_min_domains(41)
    listed = ", ".join(f"{v} ({c})" for v, c in res[:50])
    expected = f"- **{len(res)}** variables appear in >40 domains: {listed}."
    facts = agg.resolve("Which variables appear in more than 40 domains?")
    assert facts.text_block == expected


def test_golden_most_shared_line_format(agg):
    top = agg.engine.most_shared_codelists(5)
    listed = ", ".join(f"{t['code']} ({t['name']}, {t['n_variables']} vars)" for t in top)
    expected = f"- Most-shared codelists: {listed}."
    facts = agg.resolve("What is the most shared codelist?")
    assert facts.text_block == expected
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_aggregate_answer.py -v`
Expected: Task 1 测试 PASS; 新增 resolve/golden 测试 FAIL with `NotImplementedError`

- [ ] **Step 3: 实现 resolve (装配逐字平移自 graph_answer.py:136-156)**

替换 `server/aggregate_answer.py` 里 `AggregateAnswerer` 类:

```python
class AggregateAnswerer:
    """Deterministic aggregate answerer over GraphEngine (read-only, stateless)."""

    def __init__(self, engine: GraphEngine):
        self.engine = engine

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_aggregate_intents(query)
        if not intents:
            return None
        lines: list[str] = []

        if "threshold" in intents:
            # Strict beats inclusive when both shapes appear; n comes from the matched
            # threshold expression itself (NOT the first bare digit in the query — the
            # legacy branch had that bug).
            m = _THRESH_STRICT_RE.search(query)
            if m:
                n = int(m.group(1))
                threshold, wording = n + 1, f">{n}"
            else:
                m = _THRESH_INCL_PRE_RE.search(query) or _THRESH_INCL_POST_RE.search(query)
                n = int(m.group(1))
                threshold, wording = n, f"≥{n}"
            res = self.engine.variables_in_min_domains(threshold)
            if res:
                listed = ", ".join(f"{v} ({c})" for v, c in res[:50])
                lines.append(
                    f"- **{len(res)}** variables appear in {wording} domains: {listed}."
                )

        if "superlative" in intents:
            top = self.engine.most_shared_codelists(5)
            listed = ", ".join(
                f"{t['code']} ({t['name']}, {t['n_variables']} vars)" for t in top)
            lines.append(f"- Most-shared codelists: {listed}.")

        if not lines:
            return None
        return StructuredFacts(text_block="\n".join(lines), checkable_counts=[])
```

- [ ] **Step 4: 跑测试确认全过**

Run: `.venv/bin/python -m pytest scripts/tests/test_aggregate_answer.py -v`
Expected: 全部 PASS

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/aggregate_answer.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_aggregate_answer.py
git commit -m "feat(agg): AggregateAnswerer.resolve — assembly migrated verbatim from SP3, golden-pinned"
```

---

### Task 3: graph_answer 删 aggregate 分支 + 测试迁移 + 探针更新

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/graph_answer.py`
- Modify: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_answer.py`
- Modify: `branches/07_rag_kg/sdtm-rag/eval/prod_wirein/sp3_graph_probes.py`

**Interfaces:**
- Consumes: Task 2 的 `AggregateAnswerer` (探针里实例化)
- Produces: `detect_graph_intents` 不再返回 `"aggregate"`; `GraphAnswerer.resolve` 对 aggregate 措辞恒 None; 探针含 GA+AGG 双通道 140q 零污染

- [ ] **Step 1: 先写/改失败测试**

`scripts/tests/test_graph_answer.py` 改动:

(a) 替换 `test_aggregate_intent` (line 22-26) 为:

```python
def test_aggregate_moved_out_of_graph_surface():
    # aggregate NL 面已迁移到 server/aggregate_answer.py (AGG 通道)
    assert "aggregate" not in detect_graph_intents(
        "which variables appear in more than 30 domains?")
    assert "aggregate" not in detect_graph_intents("what is the most shared codelist?")
    assert "aggregate" not in detect_graph_intents(
        "how many domains are in the Events class?")
```

(b) 删除以下三个测试 (已由 test_aggregate_answer.py 覆盖): `test_aggregate_min_domains_fires` (line 69-78), `test_aggregate_at_least_includes_exact` (line 81-89), `test_must_not_fire_min_domains_without_domain_context` (line 111-113)。

(c) 在 `test_must_not_fire_class_roster` 后追加:

```python
def test_graph_resolve_none_on_aggregate_wordings(ga):
    # 整条 aggregate 措辞归 AGG 通道; graph 必须静默 (防双注入)
    assert ga.resolve("Which variables appear in more than 40 domains?") is None
    assert ga.resolve("What is the most shared codelist?") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_answer.py -v`
Expected: `test_aggregate_moved_out_of_graph_surface` 和 `test_graph_resolve_none_on_aggregate_wordings` FAIL (旧代码仍触发 aggregate)

- [ ] **Step 3: 删 graph_answer.py 的 aggregate 分支**

三处修改:

(a) docstring: 把 `NL surface covers three intent families:` 一段的 aggregate 行删掉, 改为:

```
NL surface covers two intent families:
  impact       — codelist/variable cascade ("affected if X changes", "downstream of X")
  relationship — single-domain discovery ("how is AE related to other domains?")

Aggregate queries (variables-in-min-domains / most-shared codelists) moved to the
dedicated AGG channel (server/aggregate_answer.py) after the KG value eval.
```

(b) `detect_graph_intents` 删除 aggregate 检测 (原 line 60-66, 即 `# Aggregate — two safe sub-intents...` 注释起到 `intents.add("aggregate")` 第二处止)。

(c) `resolve` 删除 `if "aggregate" in intents:` 整块 (原 line 136-156)。

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_answer.py scripts/tests/test_aggregate_answer.py -v`
Expected: 全部 PASS

- [ ] **Step 5: 更新探针 (GA+AGG 双通道)**

`eval/prod_wirein/sp3_graph_probes.py` 全文件替换为:

```python
"""SP3+AGG anti-overfitting probes:
(A) held-out queries over entities NOT in eval test sets — channel facts must match
    the GraphEngine ground truth (test_graph_engine pins the engine to raw meta.yaml).
(B) 140q zero-pollution — GraphAnswerer.resolve() AND AggregateAnswerer.resolve() must
    return None for EVERY question in test_set_v3.yml (SP1/SP2/retrieval questions;
    graph/aggregate must not inject into them).
Run: .venv/bin/python eval/prod_wirein/sp3_graph_probes.py"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.aggregate_answer import AggregateAnswerer  # noqa: E402
from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

GRAPH_HELD_OUT = [
    ("What is affected if codelist C66728 changes?", "C66728", "impacted_domains"),
    ("Which domains are impacted by changing AGE?", "AGE", "impacted_domains"),
    ("How is DM related to other domains?", None, None),
]
AGG_HELD_OUT = [
    "Which variables appear in at least 30 domains?",
    "Any variables used across 20+ domains?",
    "What's the most reused controlled terminology?",
]


def main() -> int:
    store = MetaStore(settings.meta_path)
    engine = GraphEngine(store)
    ga = GraphAnswerer(engine)
    agg = AggregateAnswerer(engine)
    fails = 0

    # (A) graph held-out facts present + cardinality matches engine
    for q, subj, kind in GRAPH_HELD_OUT:
        facts = ga.resolve(q)
        if facts is None:
            print(f"FAIL (A) graph resolve None: {q}")
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
            print(f"PASS (A) graph fired: {q}")

    # (A') AGG held-out fires
    for q in AGG_HELD_OUT:
        ok = agg.resolve(q) is not None
        print(f"{'PASS' if ok else 'FAIL'} (A') agg fired: {q}")
        fails += 0 if ok else 1

    # (B) zero-pollution over the 140q — BOTH channels silent
    raw = yaml.safe_load((Path(__file__).resolve().parents[2] / "eval" / "test_set_v3.yml").read_text())
    polluted: list[tuple[str, str]] = []

    def walk(node):
        if isinstance(node, dict):
            q = node.get("question")
            if isinstance(q, str):
                if ga.resolve(q) is not None:
                    polluted.append(("graph", q))
                if agg.resolve(q) is not None:
                    polluted.append(("agg", q))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(raw)
    if polluted:
        fails += len(polluted)
        print(f"FAIL (B) fired on {len(polluted)} non-graph q (first 5): {polluted[:5]}")
    else:
        print("PASS (B) 140q zero-pollution: graph AND aggregate silent on all test_set_v3 questions")

    print(f"\nSP3+AGG PROBES: {'ALL PASS' if fails == 0 else str(fails) + ' FAIL'}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 6: 跑探针**

Run: `.venv/bin/python eval/prod_wirein/sp3_graph_probes.py`
Expected: `SP3+AGG PROBES: ALL PASS` (若 (B) 有 polluted: 停下, 按规则 B 归档 attempt, 收紧 pattern 后重来 — 140q 是硬门 0 容忍)

- [ ] **Step 7: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/graph_answer.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_answer.py branches/07_rag_kg/sdtm-rag/eval/prod_wirein/sp3_graph_probes.py
git commit -m "refactor(agg): strip aggregate from SP3 graph surface; probes cover GA+AGG zero-pollution"
```

---

### Task 4: config flag + main.py 接线 + run_eval `--aggregate-answer` (TDD)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/config.py` (在 `graph_answer_enabled: bool = True` 即 line 102 后加)
- Modify: `branches/07_rag_kg/sdtm-rag/server/main.py:34-54` (`maybe_build_answerer`)
- Modify: `branches/07_rag_kg/sdtm-rag/eval/run_eval.py` (argparse ~line 521 + answerer 块 ~line 587 + summary ~line 641)
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_aggregate_answer.py` (追加)

**Interfaces:**
- Consumes: `server.config.Settings` (pydantic, env_prefix `SDTM_RAG_`); Task 2 `AggregateAnswerer`
- Produces: `Settings.aggregate_answer_enabled: bool = False`; `maybe_build_answerer` 三通道注册顺序 SP2 → AGG → SP3; run_eval flag `--aggregate-answer`

- [ ] **Step 1: 写失败测试**

追加到 `scripts/tests/test_aggregate_answer.py`:

```python
# ── wiring: maybe_build_answerer 按 flag 注册 AGG ─────────────────────────────


def test_maybe_build_answerer_includes_agg():
    from server.config import Settings
    from server.main import maybe_build_answerer
    a = maybe_build_answerer(Settings(structured_answer_enabled=False,
                                      graph_answer_enabled=False,
                                      aggregate_answer_enabled=True))
    assert a is not None
    assert a.resolve("Which variables appear in at least 30 domains?") is not None
    assert a.resolve("How many domains include TAETORD?") is None  # SP2 off → AGG 静默
    assert maybe_build_answerer(Settings(structured_answer_enabled=False,
                                         graph_answer_enabled=False,
                                         aggregate_answer_enabled=False)) is None


def test_maybe_build_answerer_full_composite():
    from server.config import Settings
    from server.main import maybe_build_answerer
    from server.structured_answer import CompositeAnswerer
    a = maybe_build_answerer(Settings(structured_answer_enabled=True,
                                      graph_answer_enabled=True,
                                      aggregate_answer_enabled=True))
    assert isinstance(a, CompositeAnswerer)
    # 三通道各自的代表 query 都能出事实
    assert a.resolve("How many domains include TAETORD?") is not None      # SP2
    assert a.resolve("Which variables appear in 3 or more domains?") is not None  # AGG
    assert a.resolve("What is affected if codelist C66742 changes?") is not None  # SP3
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_aggregate_answer.py -v`
Expected: 两个 wiring 测试 FAIL (`Settings` 无 `aggregate_answer_enabled` 字段 → pydantic ValidationError 或 TypeError)

- [ ] **Step 3: 实现**

(a) `server/config.py`, 在 `graph_answer_enabled: bool = True` 之后加:

```python
    # AGG: aggregate metadata channel (variables-in-min-domains / most-shared
    # codelists), split out of SP3 after the KG value eval (its only positive niche).
    # OFF until the five AGG gates pass (spec 2026-07-07); env override:
    # SDTM_RAG_AGGREGATE_ANSWER_ENABLED.
    aggregate_answer_enabled: bool = False
```

(b) `server/main.py` 的 `maybe_build_answerer` 整函数替换为:

```python
def maybe_build_answerer(s):
    """Build the SP2 structured answerer, the AGG aggregate answerer, and the SP3
    graph answerer (each flag-gated), composed so resolve() returns merged facts.
    Returns None if all are off. Kept tiny/pure so it unit-tests without spinning up
    FastAPI/RAGEngine."""
    answerers = []
    if s.structured_answer_enabled or s.graph_answer_enabled or s.aggregate_answer_enabled:
        from server.meta_store import MetaStore
        store = MetaStore(s.meta_path)
        engine = None
        if s.aggregate_answer_enabled or s.graph_answer_enabled:
            from server.graph_engine import GraphEngine
            engine = GraphEngine(store)
        if s.structured_answer_enabled:
            from server.structured_answer import StructuredAnswerer
            answerers.append(StructuredAnswerer(store))
        if s.aggregate_answer_enabled:
            from server.aggregate_answer import AggregateAnswerer
            answerers.append(AggregateAnswerer(engine))
        if s.graph_answer_enabled:
            from server.graph_answer import GraphAnswerer
            answerers.append(GraphAnswerer(engine))
    if not answerers:
        return None
    if len(answerers) == 1:
        return answerers[0]
    from server.structured_answer import CompositeAnswerer
    return CompositeAnswerer(answerers)
```

(c) `eval/run_eval.py` 三处:

argparse (紧跟 `--graph-answer` 定义后; 同时把 `--graph-answer` 的 help 里 `relationship/impact/aggregate` 改为 `relationship/impact`):

```python
    parser.add_argument(
        "--aggregate-answer",
        action="store_true",
        help="AGG: add deterministic aggregate facts (variables-in-min-domains / "
             "most-shared codelists; split out of the SP3 graph channel)",
    )
```

answerer 构建块 (原 `if args.structured_answer or args.graph_answer:` 整块) 替换为:

```python
    answerer = None
    if args.structured_answer or args.graph_answer or args.aggregate_answer:
        from server.meta_store import MetaStore
        store = MetaStore(settings.meta_path)
        engine = None
        if args.graph_answer or args.aggregate_answer:
            from server.graph_engine import GraphEngine
            engine = GraphEngine(store)
        parts = []
        if args.structured_answer:
            from server.structured_answer import StructuredAnswerer
            parts.append(StructuredAnswerer(store))
        if args.aggregate_answer:
            from server.aggregate_answer import AggregateAnswerer
            parts.append(AggregateAnswerer(engine))
        if args.graph_answer:
            from server.graph_answer import GraphAnswerer
            parts.append(GraphAnswerer(engine))
        if len(parts) == 1:
            answerer = parts[0]
        else:
            from server.structured_answer import CompositeAnswerer
            answerer = CompositeAnswerer(parts)
        print("Structured-answer channel: ON (meta.yaml facts + counting gate)"
              + (", aggregate-answer: ON" if args.aggregate_answer else "")
              + (", graph-answer: ON" if args.graph_answer else ""))
```

summary 字段 (紧跟 `summary["graph_answer"] = args.graph_answer` 后):

```python
    summary["aggregate_answer"] = args.aggregate_answer
```

- [ ] **Step 4: 跑测试 + 冒烟**

Run: `.venv/bin/python -m pytest scripts/tests/test_aggregate_answer.py scripts/tests/test_structured_answer.py -v`
Expected: 全 PASS (含既有 `test_maybe_build_answerer_gated` 不回归)

Run: `.venv/bin/python eval/run_eval.py --help | grep -A2 aggregate-answer`
Expected: 打印新 flag help

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/config.py branches/07_rag_kg/sdtm-rag/server/main.py branches/07_rag_kg/sdtm-rag/eval/run_eval.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_aggregate_answer.py
git commit -m "feat(agg): aggregate_answer_enabled flag (OFF) + maybe_build_answerer + run_eval --aggregate-answer"
```

---

### Task 5: held-out 盲写题集 (candidates → 盲写 → assemble → 独立核)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/eval/gen_agg_heldout.py` (candidates 生成 + gold 装配一体)
- Create: `branches/07_rag_kg/sdtm-rag/eval/agg_heldout_candidates.json` (中间产物, 提交)
- Create: `branches/07_rag_kg/sdtm-rag/eval/test_set_agg_heldout.yml` (16 题)
- Create: `branches/07_rag_kg/sdtm-rag/eval/test_set_agg_e2e.yml` (heldout 16 + kgval aggregate 10 回归)

**Interfaces:**
- Consumes: `GraphEngine.variables_in_min_domains` / `most_shared_codelists` (gold 程序导); `eval/test_set_kg_value.yml` 里 id 为 `ag01-ag05`/`ms01-ms05` 的 10 条 (逐字拷贝作回归)
- Produces: yml 条目 schema 与 kgval 一致: `{id, category, question, expected_facts, expect_count, card_applies}`; heldout id 前缀 `ah`(threshold)/`as`(superlative); e2e 文件里 kgval 回归条目加 `regression: true`

- [ ] **Step 1: 写 `eval/gen_agg_heldout.py`**

```python
"""AGG held-out set builder. Two modes:
  --candidates   emit agg_heldout_candidates.json (information-need cards for the
                 blind writers; NO trigger vocabulary, NO kgval questions)
  --assemble Q.json
                 take writer output (ref -> question wording), re-pin gold to the final
                 wording (strict vs inclusive), write test_set_agg_heldout.yml +
                 test_set_agg_e2e.yml (heldout + kgval aggregate regression rows).

The strict/inclusive wording classifier here is DELIBERATELY separate code from
server/aggregate_answer.py (no import) so a detection-regex bug cannot silently
propagate into gold. Anti-overfitting: thresholds differ from kgval's [3,4,5,10,40].
Run: .venv/bin/python eval/gen_agg_heldout.py --candidates
     .venv/bin/python eval/gen_agg_heldout.py --assemble eval/agg_heldout_authored.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from server.config import settings  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

CAND = ROOT / "eval" / "agg_heldout_candidates.json"
HELDOUT = ROOT / "eval" / "test_set_agg_heldout.yml"
E2E = ROOT / "eval" / "test_set_agg_e2e.yml"
KGVAL = ROOT / "eval" / "test_set_kg_value.yml"

# held-out thresholds — disjoint from kgval's [3, 4, 5, 10, 40]
THRESHOLDS = [2, 6, 9, 12, 18, 25, 30, 38]

SUPERLATIVE_CARDS = [
    ("as01", "the single codelist that is attached to the largest number of variables", 1),
    ("as02", "the codelist reused across the widest spread of SDTM domains", 1),
    ("as03", "which controlled-terminology set gets recycled most often between variables", 1),
    ("as04", "the top few codelists ranked by how many variables draw on them", 5),
    ("as05", "the three codelists shared by the greatest count of variables", 3),
    ("as06", "the four most heavily reused codelists in the standard", 4),
    ("as07", "which codelist would you call the workhorse — used by more variables than any other", 1),
    ("as08", "the champion codelist by variable usage", 1),
]

_STRICT_WORDS = re.compile(
    r"\b(?<!no )(?<!not )(more than|greater than|over|exceed)", re.IGNORECASE)


def build_candidates() -> None:
    eng = GraphEngine(MetaStore(settings.meta_path))
    cards = []
    for i, n in enumerate(THRESHOLDS, 1):
        cards.append({
            "ref": f"ah{i:02d}", "subtype": "threshold", "threshold": n,
            "need": (f"which SDTM variables occur in {n} SDTM domains or in even more "
                     f"domains than that (express the quantity requirement in your own "
                     f"natural English)"),
        })
    for ref, need, k in SUPERLATIVE_CARDS:
        cards.append({"ref": ref, "subtype": "superlative", "top_k": k, "need": need})
    # gold snapshots stored alongside so --assemble never re-reads a changed KB silently
    for c in cards:
        if c["subtype"] == "threshold":
            n = c["threshold"]
            c["gold_inclusive"] = [v for v, _ in eng.variables_in_min_domains(n)]
            c["gold_strict"] = [v for v, _ in eng.variables_in_min_domains(n + 1)]
        else:
            top = eng.most_shared_codelists(c["top_k"])
            c["gold_codes"] = [t["code"] for t in top]
            c["gold_names"] = [t["name"] for t in top]
    CAND.write_text(json.dumps(cards, indent=2), encoding="utf-8")
    print(f"Wrote {len(cards)} candidate cards -> {CAND}")


def assemble(authored_path: str) -> None:
    authored = json.loads(Path(authored_path).read_text())  # {ref: question}
    cards = {c["ref"]: c for c in json.loads(CAND.read_text())}
    rows = []
    for ref, question in sorted(authored.items()):
        c = cards[ref]
        if c["subtype"] == "threshold":
            strict = bool(_STRICT_WORDS.search(question))
            gold = c["gold_strict"] if strict else c["gold_inclusive"]
            rows.append({
                "id": ref, "category": "aggregate_threshold", "question": question,
                "expected_facts": gold, "expect_count": len(gold),
                "card_applies": True,
                "gold_reading": "strict" if strict else "inclusive",
            })
        else:
            rows.append({
                "id": ref, "category": "aggregate_superlative", "question": question,
                "expected_facts": c["gold_codes"][:c["top_k"]],
                "expect_count": None, "card_applies": False,
            })
    HELDOUT.write_text(yaml.safe_dump(rows, sort_keys=False, allow_unicode=True),
                       encoding="utf-8")
    print(f"Wrote {len(rows)} held-out questions -> {HELDOUT}")

    kg = yaml.safe_load(KGVAL.read_text())
    reg = [dict(q, regression=True) for q in kg
           if q["id"].startswith(("ag", "ms")) and q["category"] == "aggregate"]
    E2E.write_text(yaml.safe_dump(rows + reg, sort_keys=False, allow_unicode=True),
                   encoding="utf-8")
    print(f"Wrote {len(rows) + len(reg)} e2e questions -> {E2E}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--candidates", action="store_true")
    p.add_argument("--assemble", metavar="AUTHORED_JSON")
    a = p.parse_args()
    if a.candidates:
        build_candidates()
    elif a.assemble:
        assemble(a.assemble)
    else:
        p.print_help()
```

注意: 跑 `--assemble` 前先确认 kgval aggregate 条目的 `category` 字段值 — 打开 `eval/test_set_kg_value.yml` 看 `ag01` 的 category (可能是 `aggregate`); 若不同, 改 `assemble()` 里的过滤条件为实际值。

- [ ] **Step 2: 生成 candidates**

Run: `.venv/bin/python eval/gen_agg_heldout.py --candidates`
Expected: `Wrote 16 candidate cards -> .../agg_heldout_candidates.json`

- [ ] **Step 3: 派 2 个盲写 writer subagent**

用 Agent 工具派 **2 个 fresh `general-purpose` subagent** (各 8 张卡: writer-A 拿 ah01-04+as01-04, writer-B 拿 ah05-08+as05-08)。Prompt 逐字如下 (替换 `<CARDS>` 为该 writer 的卡片 JSON, 只含 ref/need 两字段 — **不含 gold/threshold/top_k 字段**):

```
You are writing natural-language eval questions for an SDTM (clinical data standard)
question-answering system. For EACH information-need card below, write ONE natural
English question a pharma data manager might genuinely ask.

Rules:
- Express each need in your own words; vary sentence structure and vocabulary between
  questions (don't reuse the same phrasing twice).
- For quantity requirements, phrase the quantity naturally in your own way.
- Do NOT enumerate or list answer values; just ask the question.
- Output STRICT JSON only: {"<ref>": "<question>", ...} for every card.

Cards:
<CARDS>
```

写手产出合并成 `eval/agg_heldout_authored.json` (`{ref: question}` 16 条)。**主 session 不得改写措辞** (盲写纪律); 只允许剔除明显跑题的卡并记录。

- [ ] **Step 4: assemble + 独立核 (Rule D lane)**

Run: `.venv/bin/python eval/gen_agg_heldout.py --assemble eval/agg_heldout_authored.json`
Expected: 16 题 heldout + 26 题 e2e 两个 yml

派 1 个 **异 type reviewer subagent** (如 `feature-dev:code-reviewer`), prompt 要求逐题核验 `test_set_agg_heldout.yml`: (1) 用**独立路径** (直接 raw 解析 `data/meta/meta.yaml`, 不 import server 代码) 重导每题 gold 并对比 expected_facts; (2) 核 strict/inclusive gold_reading 与题目措辞一致 (kgval MAJOR-3 教训: gold 按问法钉定); (3) 输出逐题 verdict JSON。任何 mismatch → 修 assemble 逻辑或 gold, 重跑本 step。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/eval/gen_agg_heldout.py branches/07_rag_kg/sdtm-rag/eval/agg_heldout_candidates.json branches/07_rag_kg/sdtm-rag/eval/agg_heldout_authored.json branches/07_rag_kg/sdtm-rag/eval/test_set_agg_heldout.yml branches/07_rag_kg/sdtm-rag/eval/test_set_agg_e2e.yml
git commit -m "eval(agg): blind-authored held-out set (16q) + e2e set (+kgval aggregate regression), gold reviewed"
```

---

### Task 6: fire-rate 门

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/eval/prod_wirein/agg_fire_probe.py`

**Interfaces:**
- Consumes: Task 5 的两个 yml; SP2/AGG/SP3 三通道
- Produces: `eval/prod_wirein/agg_fire_<setname>.json` + per-category fire 表; **门: heldout AGG fired ≥ 13/16 (81%)**

- [ ] **Step 1: 写探针 (模式沿 kgval_fire_probe.py, test-set 参数化)**

```python
"""AGG fire-rate probe: for every question in a test set, record whether SP2 / AGG /
SP3 channels fire (resolve() not None). Gate for the held-out set: AGG >= 13/16.
Run: .venv/bin/python eval/prod_wirein/agg_fire_probe.py eval/test_set_agg_heldout.yml"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from server.aggregate_answer import AggregateAnswerer  # noqa: E402
from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402


def main() -> int:
    test_set = Path(sys.argv[1])
    store = MetaStore(settings.meta_path)
    engine = GraphEngine(store)
    from server.structured_answer import StructuredAnswerer
    sp2, agg, sp3 = StructuredAnswerer(store), AggregateAnswerer(engine), GraphAnswerer(engine)
    qs = yaml.safe_load(test_set.read_text(encoding="utf-8"))

    rows = []
    for q in qs:
        rows.append({"id": q["id"], "category": q["category"],
                     "fired_sp2": sp2.resolve(q["question"]) is not None,
                     "fired_agg": agg.resolve(q["question"]) is not None,
                     "fired_sp3": sp3.resolve(q["question"]) is not None})

    out = ROOT / "eval" / "prod_wirein" / f"agg_fire_{test_set.stem}.json"
    out.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_cat[r["category"]].append(r)
    print(f"{'category':<24} {'n':>3} {'SP2':>8} {'AGG':>8} {'SP3':>8}")
    for cat in sorted(by_cat):
        g = by_cat[cat]
        n = len(g)
        f = [sum(r[k] for r in g) for k in ("fired_sp2", "fired_agg", "fired_sp3")]
        print(f"{cat:<24} {n:>3} {f[0]:>4}/{n} {f[1]:>4}/{n} {f[2]:>4}/{n}")
    n = len(rows)
    n_agg = sum(r["fired_agg"] for r in rows)
    silent = [r["id"] for r in rows if not r["fired_agg"]]
    print(f"\nAGG fired {n_agg}/{n}; silent: {silent}")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: 跑 held-out 门**

Run: `.venv/bin/python eval/prod_wirein/agg_fire_probe.py eval/test_set_agg_heldout.yml`
Expected: `AGG fired >= 13/16`。**若 <13**: 这是 held-out 泛化失败 → 规则 B 归档 `evidence/failures/agg_attempt_1.md` (含 silent 题措辞 + 未命中的语言形状分析); 只允许按**形状类**补 pattern (不许按题补词), 补后**重新盲写一批新题**再测 (原 held-out 已烧掉, 不能复用作门)。

- [ ] **Step 3: 跑 kgval 回归参考**

Run: `.venv/bin/python eval/prod_wirein/agg_fire_probe.py eval/test_set_kg_value.yml`
Expected: aggregate family AGG fired ≥ 8/10 (旧 SP3 是 2/10; 此为参考报告, 不是设计输入)

- [ ] **Step 4: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/eval/prod_wirein/agg_fire_probe.py branches/07_rag_kg/sdtm-rag/eval/prod_wirein/agg_fire_*.json
git commit -m "eval(agg): fire-rate gate — held-out >=13/16 PASS + kgval regression report"
```

---

### Task 7: ds 迷你端到端 (OFF vs ON, Δ ≥ +10pp 门)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/eval/prod_wirein/analyze_agg_e2e.py`
- Output: `eval/prod_wirein/agg_e2e_{off,on}.json`

**Interfaces:**
- Consumes: run_eval 输出 JSON (`data["results"]`, 每条 `{"id", ..., "answer"}` — `--full-answers` 提供未截断 answer); gold 从 `test_set_agg_e2e.yml` 读 (`expected_facts` / `expect_count`); `analyze_kgval.fact_present` / `card_present` (同一度量码路)
- Produces: 两臂 JSON + 分析表; **门: held-out 子集 set_recall Δ(ON−OFF) ≥ +10pp**

- [ ] **Step 1: 确认臂命令与 kgval 口径一致**

打开 `branches/07_rag_kg/sdtm-rag/KG_VALUE_EVAL_PLAN.md`, 找到 arm1/arm2 的 run_eval 完整命令行 (retrieval levers / judge / temperature 口径), 下两步的命令按它镜像, 只增删 `--aggregate-answer` 一个差异。若与下方模板 flag 有出入, 以 KG_VALUE_EVAL_PLAN.md 为准并记录差异。

- [ ] **Step 2: 跑 OFF 臂 (生产减 AGG = SP2+SP3)**

```bash
.venv/bin/python eval/run_eval.py eval/test_set_agg_e2e.yml \
  --model deepseek/deepseek-chat --temperature 0 \
  --structured-lookup --hybrid --guardrail \
  --structured-answer --graph-answer \
  --judge --full-answers --tag agg_off \
  --output eval/prod_wirein/agg_e2e_off.json
```

Expected: 26 题跑完, JSON 落盘 (API 失败题: 重试一次; 仍失败则记录并在分析中剔除该题两臂)

- [ ] **Step 3: 跑 ON 臂 (生产 = SP2+AGG+SP3)**

```bash
.venv/bin/python eval/run_eval.py eval/test_set_agg_e2e.yml \
  --model deepseek/deepseek-chat --temperature 0 \
  --structured-lookup --hybrid --guardrail \
  --structured-answer --aggregate-answer --graph-answer \
  --judge --full-answers --tag agg_on \
  --output eval/prod_wirein/agg_e2e_on.json
```

- [ ] **Step 4: 写分析脚本**

```python
"""AGG mini e2e analysis: OFF (SP2+SP3) vs ON (SP2+AGG+SP3), deepseek temp=0.
Gate: held-out subset set_recall Δ(ON−OFF) >= +10pp. Per-question regressions are
listed for causal triage, NOT auto-failed (kgval rl05 lesson: temp=0 still rewrites).
Run: .venv/bin/python eval/prod_wirein/analyze_agg_e2e.py"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

PW = Path(__file__).resolve().parent
sys.path.insert(0, str(PW))
from analyze_kgval import card_present, fact_present  # noqa: E402

ROOT = PW.parents[1]
GOLD = {q["id"]: q for q in yaml.safe_load(
    (ROOT / "eval" / "test_set_agg_e2e.yml").read_text(encoding="utf-8"))}


def load(arm: str) -> dict[str, dict]:
    data = json.loads((PW / f"agg_e2e_{arm}.json").read_text())
    return {r["id"]: r for r in data["results"]}


def set_recall(qid: str, res: dict) -> float:
    facts = GOLD[qid].get("expected_facts") or []
    ans = res.get("answer") or res.get("answer_preview") or ""
    if not facts:
        return 1.0
    return sum(fact_present(f, ans) for f in facts) / len(facts)


def main() -> int:
    off, on = load("off"), load("on")
    ids = [i for i in GOLD if i in off and i in on]
    rows = []
    for qid in ids:
        r_off, r_on = set_recall(qid, off[qid]), set_recall(qid, on[qid])
        rows.append({"id": qid, "heldout": not GOLD[qid].get("regression"),
                     "off": r_off, "on": r_on, "delta": r_on - r_off})

    def avg(sel):
        xs = [r for r in rows if sel(r)]
        return (sum(r["off"] for r in xs) / len(xs), sum(r["on"] for r in xs) / len(xs))

    ho_off, ho_on = avg(lambda r: r["heldout"])
    rg_off, rg_on = avg(lambda r: not r["heldout"])
    print(f"held-out   set_recall: OFF {ho_off:.1%} -> ON {ho_on:.1%}  Δ {ho_on-ho_off:+.1%}")
    print(f"regression set_recall: OFF {rg_off:.1%} -> ON {rg_on:.1%}  Δ {rg_on-rg_off:+.1%}")
    regressions = [r for r in rows if r["delta"] < 0]
    for r in regressions:
        print(f"  REGRESSION {r['id']}: {r['off']:.2f} -> {r['on']:.2f}  (needs causal triage)")
    (PW / "agg_e2e_analysis.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    gate = (ho_on - ho_off) >= 0.10
    print(f"\nGATE held-out Δ>=+10pp: {'PASS' if gate else 'FAIL'}")
    return 0 if gate else 1


if __name__ == "__main__":
    sys.exit(main())
```

跑之前先 `head -30 eval/prod_wirein/agg_e2e_off.json` 核对 results 条目字段名 (`id`/`answer`); 与 `analyze_kgval.py` 同 schema, 不一致则改 `load`/`set_recall` 的取值键。

- [ ] **Step 5: 跑分析 + 退化题 triage**

Run: `.venv/bin/python eval/prod_wirein/analyze_agg_e2e.py`
Expected: `GATE held-out Δ>=+10pp: PASS`

每条 REGRESSION 逐题 triage (kgval rl05 教训): 查该题 `agg_fire_heldout` 记录 — 若 AGG 未触发则两臂 context 相同, 差异 = 解码变异, 记录后放行; 若 AGG 真触发且答案变差, 对比两臂注入块与答案, 判因果。**真·通道致害 ≥1 题 = 门 FAIL** → 规则 B 归档 + 修复重跑。

- [ ] **Step 6: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/eval/prod_wirein/analyze_agg_e2e.py branches/07_rag_kg/sdtm-rag/eval/prod_wirein/agg_e2e_*.json
git commit -m "eval(agg): ds mini e2e OFF vs ON — held-out set_recall gate PASS"
```

---

### Task 8: 全量质量门 + 翻默认 ON + boot 冒烟

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/config.py` (flag False → True)

**Interfaces:**
- Produces: `aggregate_answer_enabled: bool = True` (生产默认三通道全 ON)

- [ ] **Step 1: 全套测试 + lint**

```bash
.venv/bin/python -m pytest scripts/tests/ -q
.venv/bin/python -m ruff check server/aggregate_answer.py server/graph_answer.py server/main.py server/config.py eval/run_eval.py eval/gen_agg_heldout.py eval/prod_wirein/agg_fire_probe.py eval/prod_wirein/analyze_agg_e2e.py eval/prod_wirein/sp3_graph_probes.py
.venv/bin/python -m mypy server/aggregate_answer.py
```

Expected: pytest 全绿 (基线 414+ 新增), ruff/mypy clean

- [ ] **Step 2: 翻默认 ON**

`server/config.py` 该行改为:

```python
    # AGG: aggregate metadata channel (variables-in-min-domains / most-shared
    # codelists), split out of SP3 after the KG value eval (its only positive niche).
    # Default ON since 2026-07-07 (five AGG gates passed, see
    # evidence/checkpoints/agg_channel_summary.md); env override:
    # SDTM_RAG_AGGREGATE_ANSWER_ENABLED.
    aggregate_answer_enabled: bool = True
```

- [ ] **Step 3: 生产默认冒烟 + 探针重跑**

```bash
.venv/bin/python -c "
from server.config import Settings
from server.main import maybe_build_answerer
a = maybe_build_answerer(Settings())
print(type(a).__name__)
print('AGG fires:', a.resolve('Which variables appear in at least 40 domains?') is not None)
print('140q-style silent:', a.resolve('What is the purpose of the DM domain?') is None)"
.venv/bin/python eval/prod_wirein/sp3_graph_probes.py
```

Expected: `CompositeAnswerer` / `AGG fires: True` / `140q-style silent: True`; 探针 ALL PASS

- [ ] **Step 4: 跑全套 pytest (翻 ON 后再确认一次)**

Run: `.venv/bin/python -m pytest scripts/tests/ -q`
Expected: 全绿 (若有测试依赖默认 OFF 需修正测试为显式 Settings)

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/config.py
git commit -m "feat(agg): flip aggregate_answer_enabled default ON (all five gates green)"
```

---

### Task 9: Rule D 全量审 + Rule A 独立抽检 (N=6)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/agg_ruleD_review.md`
- Create: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/agg_ruleA_audit.md`

**Interfaces:**
- Consumes: Task 1-8 全部 diff + 证据 JSON
- Produces: 两份 verdict 文档; findings 修复后全门重绿

- [ ] **Step 1: Rule D — 派异 type reviewer 全量审**

派 1 个 `feature-dev:code-reviewer` subagent, prompt 给出: spec 路径 + 全 diff 范围 (`git diff <task1 前的 commit>..HEAD -- branches/07_rag_kg/sdtm-rag/`) + 审查重点: (1) 检测 regex 的 must-not-fire 盲区 (对抗式造句); (2) golden 等价与 SP3 遗留格式; (3) 零污染门与 flag 接线; (4) held-out 纪律有没有被违反 (pattern 是否对题调参)。产出 verdict + findings 清单写入 `evidence/checkpoints/agg_ruleD_review.md`。BLOCKER/HIGH 必修, MED/LOW 逐条决策记录。

- [ ] **Step 2: Rule A — 派独立 scientist 抽检 N=6**

派 1 个 fresh `general-purpose` subagent (与实现/审查不同 lane), 指令: **不 import server 代码**, 直接 raw 解析 `data/meta/meta.yaml`, 对 6 个样本做双源核验 — 4 个触发样本 (2 threshold [从 held-out 已触发题里抽] + 2 superlative) 核对 ON 臂注入事实的变量集合/基数/top-k 与 raw yaml 一致; 2 个端到端样本核 `analyze_agg_e2e` 的 set_recall 打分是否与人工判读一致。产出写 `evidence/checkpoints/agg_ruleA_audit.md`。任何 mismatch = 业务门 FAIL → 修复重跑相关门。

- [ ] **Step 3: findings 修复后重绿**

如有代码改动: 重跑 Task 8 Step 1/3/4 全部命令, 全绿。

- [ ] **Step 4: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/evidence/checkpoints/agg_rule*.md
git commit -m "audit(agg): Rule D review + Rule A N=6 independent audit PASS"
```

---

### Task 10: 收口 — 证据 checkpoint + Chain 07_RAG 文档链

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/agg_channel_summary.md`
- Modify: `branches/07_rag_kg/sdtm-rag/KG_ROADMAP.md`
- Modify: `.work/meta/worklog/phase_07_rag_kg.md` (repo-root)
- Modify: `docs/PROGRESS.md` (repo-root, 最后更新行)
- Modify: `branches/07_rag_kg/_progress.json` (若存在, Tier 2 schema 追加)

- [ ] **Step 1: 写 `agg_channel_summary.md`**

模板 (数字填实测值):

```markdown
# AGG 通道 — 五门验收 checkpoint

> 2026-07-07 · spec docs/superpowers/specs/2026-07-07-aggregate-answer-widening-design.md
> aggregate 从 SP3 拆出独立通道 + pattern-level 触发; 默认 ON。

| 门 | 结果 |
|----|------|
| 1 单测电池 | must-fire N/N + must-not-fire N/N + golden 等价 + 全套 pytest NNN passed |
| 2 140q 零污染 | GA+AGG 双通道 0/140 (sp3_graph_probes ALL PASS) |
| 3 fire-rate | held-out X/16 (≥13 门 PASS); kgval aggregate 回归 X/10 (旧 2/10) |
| 4 ds 端到端 | held-out set_recall OFF X% → ON X% (Δ +Xpp ≥ +10pp PASS); 退化题 triage: ... |
| 5 质量 | ruff/mypy clean; Rule D verdict ...; Rule A 6/6 ... |

限制/诚实缺口: (单模型 ds / 单臂对照 / held-out N=16 ...)
```

- [ ] **Step 2: KG_ROADMAP.md 更新**

(a) 头部时间线加一行 (置于 2026-06-21 条目后): `> 2026-07-07 · **AGG (aggregate 独立通道) DONE ✅ 默认 ON** — 价值 eval 两条榨值建议落地: 触发面 2/10→held-out X/16, ds 端到端 Δ+Xpp。详见「AGG DONE」段。`
(b) 「下一步 — SP4/SP5」段 (§67-73) 里删掉 "① 拓宽 SP3 NL 触发面 ② 把 aggregate 并入 SP2" 两条已完成项, 注明 AGG DONE; 保留 SP4/SP5 与其余 backlog。
(c) 在「KG 价值 eval DONE」段后加「AGG DONE (2026-07-07)」段: 产出文件清单 + 五门结果 + 证据指针 (照 SP1-SP3 段落格式)。

- [ ] **Step 3: worklog + PROGRESS + _progress**

- `.work/meta/worklog/phase_07_rag_kg.md` 末尾 append 本单元 work record (照 SP3 条目格式: 做了什么/验收/产出/next)。
- `docs/PROGRESS.md` 「最后更新」行改为 AGG DONE 摘要 (原最后更新内容退为 "前:")。
- `branches/07_rag_kg/_progress.json` 存在则按 Tier 2 schema 追加条目。

- [ ] **Step 4: 终 commit + push**

```bash
git add -A
git commit -m "AGG DONE: aggregate 独立通道默认 ON (五门全过: 零污染 0/140 + held-out fire X/16 + ds e2e Δ+Xpp + Rule A/D PASS)"
git push origin main
```

- [ ] **Step 5: 汇报**

向用户一行汇报五门结果 + 提示下一单元: SP4/SP5 (KG 重启) 需另起 brainstorm。

---

## Self-Review 记录 (写计划时已跑)

- **Spec coverage**: §1 Q1→Task 1/3 (只动 aggregate); Q2→Task 5/6/7 (三档验收); Q3→Task 1/2/4 (独立 answerer); spec §3 pattern 家族→Task 1; §3a 上界不触发→Task 1 must-not-fire; §4 golden/收窄→Task 2/3; §5 五门→Task 6 (fire-rate) / Task 3+8 (零污染) / Task 1-4 (单测) / Task 7 (ds e2e) / Task 8-9 (质量+Rule A/D); §6 交付→Task 10。无缺口。
- **Placeholder scan**: 无 TBD/TODO; 两处「按实际文件核对字段/命令」是对既有文件 (KG_VALUE_EVAL_PLAN.md / run_eval 输出) 的镜像指令, 附带默认模板可直接执行。
- **Type consistency**: `detect_aggregate_intents -> set[str]` ⊆ {threshold, superlative} 全文一致; `AggregateAnswerer(engine: GraphEngine)` 一致; regex 名 `_THRESH_*_RE`/`_SUPERLATIVE_RE` 在 Task 1 定义 Task 2 复用一致; yml 字段 (id/category/question/expected_facts/expect_count/card_applies/regression) Task 5/6/7 一致。
