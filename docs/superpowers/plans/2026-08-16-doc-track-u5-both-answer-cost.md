# doc 轨 U5 — both 答题侧代价 + 答题侧仪器 实施 Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建成答题侧仪器 (逐题稳定性 + judge 噪声分解 + 双向对照), 用它量 `both` 档两个方向的
答题侧代价, 并把 auto 档触发分布从演绎升级为逐题观测。

**Architecture:** 三件确定性工具先行 (观测字段 / rejudge 探针 / u5_verdict 判定脚本, 全部
TDD), 然后 4 配置 × 3 遍答题矩阵 + 判定脚本一次性给出 I/E 结论; 规则 D 五方核验后收口。

**Tech Stack:** Python 3 (`sdtm-rag/.venv`), pytest, litellm (答题走生产 Router = Bedrock jp,
judge = deepseek/deepseek-chat), chromadb 检索。

**Spec:** `docs/superpowers/specs/2026-08-16-doc-track-u5-both-answer-cost-design.md`
(含修正案 1: `federation.py` 观测属性; 修正案 2: I3 阈值 = U2 冻结判据 0.80/0.20)

## Global Constraints (每个 task 隐含遵守)

1. **数据红线**: 题面 / 语料 / run 产物 / 跑批日志全在 `data/study/` (gitignored)。
   **进 git 的文件零题面零真名零 `st01__` 前缀 id** — 只许题号 (`st01_v2_q14` 式) 与数字。
2. **只量不改**: 除 spec §2 列的三件 eval 工具 + `federation.py` 2 行观测属性外,
   `server/` / router prompt / 席位 / gold / 阈值 / `score_run` 一律不动。
3. **阈值冻结**: `I1_MIN_SAME_RATE=0.95` · `I2_MAX_UNSTABLE={"cards":7,"docs":4}` ·
   `I3_POS_MIN=0.80, I3_NEG_MAX=0.20`。看过任何跨配置数字后一字不许改 (spec §5.3)。
4. **写「实测」必附可复跑命令**; 数字对不上先查口径; `run_eval` 分数低于阈值 rc=1
   **不是跑批失败** — 看产物, 不看 rc, 不看日志里的 "done"。
5. 工作分支 `doc-track-u5`, 从 `main` 切出; 每 task 独立 commit。
6. 答题命令模板与 U2 逐字同源: `--hybrid --study-lookup --federated --corpus <档>
   --study-docs --judge --temperature 0` (不传 `--model` = 走生产 Router; judge 内部恒 temp=0)。
7. 任何 I 闸触发: 失败归档到 `sdtm-rag/evidence/failures/u5_attempt_1.md` (规则 B) +
   停下上报用户, 不许静默绕过。

---

### Task 0: 开工自检 + 分支

**Files:** 无 (只读)

- [ ] **Step 1: 三条自检**

```bash
cd sdtm-rag
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2        # → 1275 passed
./.venv/bin/python -c "
import chromadb; cl = chromadb.PersistentClient(path='data/chroma')
print({c.name: c.count() for c in cl.list_collections()})"            # 4329 / 959 / 114
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/u5_chk.json  # 87.5%
```

对不上 = 先查环境, 不开工。

- [ ] **Step 2: 切分支**

```bash
git checkout -b doc-track-u5
mkdir -p data/study/st01/eval/logs/u5
```

---

### Task 1: 逐题 routed/fallback 观测字段

**Files:**
- Modify: `server/federation.py` (`FederatedEngine.__init__` + `retrieve`, 共 ~3 行)
- Modify: `eval/run_eval.py` (`_FederatedAdapter` + 新函数 `attach_routing_fields` + main 的
  `if args.federated:` 块)
- Test: `scripts/tests/test_federation.py` (追加), `scripts/tests/test_run_eval_federated.py` (追加)

**Interfaces:**
- Produces: `FederatedEngine.last_route_fallback: bool | None` (auto 档 = 本次判库的
  fallback 标志; 强制档恒 None); run 产物 `results[*]["routed"]: str` 与
  `results[*]["routed_fallback"]: bool | None`; 函数
  `attach_routing_fields(results: list[dict], retriever: _FederatedAdapter) -> None` (长度不齐 raise RuntimeError)。
- Consumes: 现有 `_FederatedAdapter.routed: list[str]`。

- [ ] **Step 1: 写失败测试 (federation 侧)** — 追加到 `scripts/tests/test_federation.py`:

```python
class _U5StubEngine:
    def retrieve(self, question, *, top_k=None, **kw):
        return []


def _u5_fed():
    from server.federation import FederatedEngine
    return FederatedEngine(cdisc=_U5StubEngine(), study=_U5StubEngine(), llm_router=object())


def test_last_route_fallback_none_on_forced_corpus():
    fed = _u5_fed()
    fed.retrieve("q", corpus="study")
    assert fed.last_route_fallback is None


def test_last_route_fallback_records_auto_and_clears_on_forced(monkeypatch):
    fed = _u5_fed()
    monkeypatch.setattr("server.federation.route_corpus", lambda r, q: ("study", True))
    fed.retrieve("q", corpus="auto")
    assert fed.last_route_fallback is True
    fed.retrieve("q", corpus="both")  # 强制档必须清掉上一题的标志, 否则串题
    assert fed.last_route_fallback is None
```

- [ ] **Step 2: 跑测试确认失败**

```bash
./.venv/bin/python -m pytest scripts/tests/test_federation.py -q 2>&1 | tail -3
```
预期: 2 failed (`AttributeError: last_route_fallback`)。

- [ ] **Step 3: federation.py 最小实现** — `__init__` 末尾加:

```python
        # U5 观测属性: 最近一次 retrieve 的判库 fallback 标志 (auto 档才有意义;
        # 强制档恒 None)。只写不读, 供 eval 侧记逐题取证 (both_ruler §5-11 缺口)。
        self.last_route_fallback: bool | None = None
```

`retrieve` 里 `routed = corpus` 之后、`if corpus == "auto":` 分支改为:

```python
        routed = corpus
        self.last_route_fallback = None
        if corpus == "auto":
            routed, fallback = route_corpus(self.llm_router, question)
            self.last_route_fallback = fallback
            log.info("federation_routed", corpus=routed, fallback=fallback)
```

- [ ] **Step 4: 跑测试确认过** — 同 Step 2 命令, 预期 all passed。

- [ ] **Step 5: 写失败测试 (adapter + attach)** — 追加到
  `scripts/tests/test_run_eval_federated.py` (文件顶部 import 行补 `attach_routing_fields`):

```python
def test_adapter_records_fallback_flag_per_question():
    fed = _FakeFed()
    fed.last_route_fallback = False
    a = _FederatedAdapter(fed)
    a.retrieve("q")
    fed.last_route_fallback = True
    a.retrieve("q2")
    assert a.routed_fallback == [False, True]


def test_adapter_fallback_defaults_none_when_engine_lacks_attr():
    a = _FederatedAdapter(_FakeFed())
    a.retrieve("q")
    assert a.routed_fallback == [None]


def test_attach_routing_fields_writes_per_question_observations():
    results = [{"id": "a"}, {"id": "b"}]
    a = _FederatedAdapter(_FakeFed(["study", "both"]))
    a.retrieve("q1")
    a.retrieve("q2")
    attach_routing_fields(results, a)
    assert [r["routed"] for r in results] == ["study", "both"]
    assert results[0]["routed_fallback"] is None


def test_attach_routing_fields_fails_loud_on_length_mismatch():
    a = _FederatedAdapter(_FakeFed())
    a.retrieve("q")
    with pytest.raises(RuntimeError):
        attach_routing_fields([], a)
```

- [ ] **Step 6: 跑测试确认失败** (`ImportError` / `AttributeError`):

```bash
./.venv/bin/python -m pytest scripts/tests/test_run_eval_federated.py -q 2>&1 | tail -3
```

- [ ] **Step 7: run_eval.py 最小实现** — `_FederatedAdapter.__init__` 加
  `self.routed_fallback: list[bool | None] = []`; `retrieve` 里 `self.routed.append(routed)`
  之后加 `self.routed_fallback.append(getattr(self.fed, "last_route_fallback", None))`;
  `_FederatedAdapter` 类定义后加模块级函数:

```python
def attach_routing_fields(results: list[dict], retriever: "_FederatedAdapter") -> None:
    """逐题判库观测写进产物 (both_ruler §5-8/§5-11 缺口). 长度不齐 = 取证链断了, fail loud."""
    if len(retriever.routed) != len(results):
        raise RuntimeError(
            f"routed({len(retriever.routed)}) != results({len(results)}): "
            "per-question routing evidence broken; refusing to write partial fields")
    for r, routed, fb in zip(results, retriever.routed, retriever.routed_fallback, strict=True):
        r["routed"] = routed
        r["routed_fallback"] = fb
```

main 的 `if args.federated:` 块 (现在只写 summary["routing"]) 首行加调用:

```python
    if args.federated:
        attach_routing_fields(results, retriever)
        routing = dict(Counter(retriever.routed))
```

- [ ] **Step 8: 跑测试确认过 + 全量回归**

```bash
./.venv/bin/python -m pytest scripts/tests/test_run_eval_federated.py scripts/tests/test_federation.py -q 2>&1 | tail -3
./.venv/bin/python -m pytest -p no:warnings --tb=short 2>&1 | tail -2   # 1275 + 6 = 1281 passed
```

- [ ] **Step 9: 端到端冒烟 (真检索, 零 LLM)** — 新字段在真产物里长什么样:

```bash
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid --study-lookup --federated --corpus study --study-docs \
  --output /tmp/u5_smoke.json
./.venv/bin/python -c "
import json; d = json.load(open('/tmp/u5_smoke.json'))
rows = d['results']
assert all('routed' in r and 'routed_fallback' in r for r in rows), 'missing fields'
print('rows:', len(rows), '| routed set:', {r['routed'] for r in rows},
      '| fallback set:', {r['routed_fallback'] for r in rows})"
# 预期: rows: 30 | routed set: {'study'} | fallback set: {None}  (强制档无 fallback 语义)
```

- [ ] **Step 10: Commit**

```bash
git add server/federation.py eval/run_eval.py scripts/tests/test_federation.py \
  scripts/tests/test_run_eval_federated.py
git commit -m "feat(u5): 逐题 routed/fallback 观测字段 (federation 观测属性 + run 产物取证)"
```

---

### Task 2: rejudge 探针工具

**Files:**
- Create: `eval/rejudge_run.py`
- Test: `scripts/tests/test_rejudge_run.py`

**Interfaces:**
- Produces: CLI `python -m eval.rejudge_run <run.json> <test_set.yml> --output out.json
  [--judge-model M]`; 函数 `rejudge(run: dict, facts_by_id: dict[str, list[str]],
  judge_model: str) -> dict` 返回 `{"n", "n_same", "same_rate", "rows"}`,
  rows 元素 = `{"id", "orig", "rejudged", "same", "parse_fail"}` (零题面)。
- Consumes: `eval.run_eval.check_fact_recall_judge` (签名
  `(question, answer, expected_facts, judge_model, temperature=0.0)`, 返回
  `(recall, hits, misses) | None`), `eval.run_eval.load_test_set`,
  `eval.run_eval.DEFAULT_JUDGE_MODEL`; run json 须含 `results[*]["answer"]`
  (`--full-answers` 产物, `run_eval.py:397`)。

- [ ] **Step 1: 写失败测试** — `scripts/tests/test_rejudge_run.py` 全文:

```python
"""eval/rejudge_run.py 单测 — judge 全 mock, 零 LLM 调用."""
import pytest

import eval.rejudge_run as rr


def _run(rows):
    return {"results": rows}


def test_same_and_diff_counted(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda q, a, f, m: (0.5, [], []))
    run = _run([
        {"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 0.5},
        {"id": "b", "question": "?", "answer": "x", "judge_fact_recall": 1.0},
    ])
    out = rr.rejudge(run, {"a": ["f"], "b": ["f"]}, "m")
    assert (out["n"], out["n_same"], out["same_rate"]) == (2, 1, 0.5)


def test_out_of_scope_skipped(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: (1.0, [], []))
    assert rr.rejudge(_run([{"id": "a", "out_of_scope": True}]), {}, "m")["n"] == 0


def test_missing_full_answer_fails_loud():
    run = _run([{"id": "a", "question": "?", "judge_fact_recall": 1.0}])
    with pytest.raises(SystemExit):
        rr.rejudge(run, {"a": ["f"]}, "m")


def test_parse_fail_counts_as_not_same(monkeypatch):
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: None)
    run = _run([{"id": "a", "question": "?", "answer": "x", "judge_fact_recall": 1.0}])
    out = rr.rejudge(run, {"a": ["f"]}, "m")
    assert out["rows"][0]["parse_fail"] is True and out["n_same"] == 0


def test_unknown_id_fails_loud(monkeypatch):
    # facts_by_id 缺题 = run 与题集对不上, 必须 KeyError 而非静默跳过
    monkeypatch.setattr(rr, "check_fact_recall_judge", lambda *a: (1.0, [], []))
    run = _run([{"id": "ghost", "question": "?", "answer": "x", "judge_fact_recall": 1.0}])
    with pytest.raises(KeyError):
        rr.rejudge(run, {"a": ["f"]}, "m")
```

- [ ] **Step 2: 跑测试确认失败** (`ModuleNotFoundError: eval.rejudge_run`):

```bash
./.venv/bin/python -m pytest scripts/tests/test_rejudge_run.py -q 2>&1 | tail -3
```

- [ ] **Step 3: 实现 `eval/rejudge_run.py`** 全文:

```python
"""对已落盘 run json 的存量答案重跑 judge (不重新答题) — U5 仪器闸 I1 的探针.

把「judge 自身噪声」从「答题噪声」里分解出来. 输入 run 必须带全文答案
(--full-answers 跑出的 "answer" 字段), 否则 fail loud. 产物零题面: 只存 id 与数字.
"""
from __future__ import annotations

import argparse
import json

from eval.run_eval import DEFAULT_JUDGE_MODEL, check_fact_recall_judge, load_test_set


def rejudge(run: dict, facts_by_id: dict[str, list[str]], judge_model: str) -> dict:
    rows = []
    for r in run["results"]:
        if r.get("out_of_scope"):
            continue
        if "answer" not in r:
            raise SystemExit(
                f"{r['id']}: run json 无全文答案 — 不是 --full-answers 跑出的, I1 探针无法执行")
        verdict = check_fact_recall_judge(
            r["question"], r["answer"], facts_by_id[r["id"]], judge_model)
        if verdict is None:
            rows.append({"id": r["id"], "orig": r["judge_fact_recall"],
                         "rejudged": None, "same": False, "parse_fail": True})
            continue
        recall = round(verdict[0], 4)
        rows.append({"id": r["id"], "orig": r["judge_fact_recall"],
                     "rejudged": recall, "same": recall == r["judge_fact_recall"],
                     "parse_fail": False})
    n_same = sum(r["same"] for r in rows)
    return {"n": len(rows), "n_same": n_same,
            "same_rate": round(n_same / len(rows), 4) if rows else 0.0, "rows": rows}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("run_json")
    p.add_argument("test_set")
    p.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    p.add_argument("--output", required=True)
    a = p.parse_args(argv)
    with open(a.run_json, encoding="utf-8") as f:
        run = json.load(f)
    facts_by_id = {q["id"]: q["expected_facts"] for q in load_test_set(a.test_set)}
    out = rejudge(run, facts_by_id, a.judge_model)
    print(f"rejudge n={out['n']} same={out['n_same']} same_rate={out['same_rate']:.4f}")
    with open(a.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

⚠ 若 Step 4 发现题集行无 `expected_facts` 键 (KeyError from `q["expected_facts"]`),
先看 `load_test_set` 的行结构再决定 (预期两个题集每计分题都有该键; U1 79 fact / v2 继承),
**不许**默默改成 `q.get(..., [])` — 空 facts 会让 judge 恒 1.0, 探针变装饰。

- [ ] **Step 4: 跑测试确认过 + 全量回归**

```bash
./.venv/bin/python -m pytest scripts/tests/test_rejudge_run.py -q 2>&1 | tail -3   # 5 passed
./.venv/bin/python -m pytest -p no:warnings --tb=no 2>&1 | tail -2                  # 1286 passed
```

- [ ] **Step 5: Commit**

```bash
git add eval/rejudge_run.py scripts/tests/test_rejudge_run.py
git commit -m "feat(u5): rejudge 探针 (judge 噪声与答题噪声分解, I1 仪器闸)"
```

---

### Task 3: u5_verdict 确定性判定脚本 (先于任何矩阵数据)

**Files:**
- Create: `eval/u5_verdict.py`
- Test: `scripts/tests/test_u5_verdict.py`

**Interfaces:**
- Produces: CLI `python -m eval.u5_verdict --cards-study A B C --cards-both A B C
  --docs-study A B C --docs-both A B C --probe-cards P --probe-docs P
  --controls DP DN CP CN --output out.json`; rc: 0 全过 / 2 = I2 或 I3 触发 /
  3 = I1 降级 (advisory)。
  **⚠ 实现后契约已变 (审查 M5)**: `--controls` 四位置参已改为四个具名 required flag
  `--controls-docs-pos/--controls-docs-neg/--controls-cards-pos/--controls-cards-neg`,
  本段与下方参考实现的旧形态仅作冻结史料, 拼命令以 Task 7 调用块为准。
- 纯函数 (供测试与抽检方复算): `scores_by_id(run) -> dict[str, float | None]` ·
  `stability(runs: list[dict]) -> (stable: dict[str, float], unstable: list[str])` ·
  `paired_effect(stable_a, stable_b, n_scored) -> dict` ·
  `build_verdict(runs, probes, controls) -> (verdict: dict, rc: int)`。
- Consumes: run json (`summary.n_questions` + `results[*]` 的 `id/out_of_scope/`
  `judge_fact_recall/judge_parse_ok`), rejudge 产物 (`same_rate`), judge_controls 产物 (`avg`)。

- [ ] **Step 1: 写失败测试** — `scripts/tests/test_u5_verdict.py` 全文:

```python
"""eval/u5_verdict.py 单测 — 全合成 fixture, 判定逻辑逐条钉死 (U3 §6-10 教训:
判定脚本零测试 = 结论可翻不留痕). 变异集含对调型 (U2 §4.1 方向③)."""
import pytest

from eval.u5_verdict import (FRAGILE_4, build_verdict, paired_effect,
                             scores_by_id, stability)


def _mkrun(scores: dict, n: int):
    """scores: id -> float (judge 分) | None (parse 失败)."""
    return {"summary": {"n_questions": n},
            "results": [{"id": i, "judge_fact_recall": (s if s is not None else 0.0),
                         "judge_parse_ok": s is not None} for i, s in scores.items()]}


def test_scores_by_id_none_on_parse_fail_and_skips_oos():
    run = _mkrun({"a": 1.0, "b": None}, n=2)
    run["results"].append({"id": "c", "out_of_scope": True, "judge_fact_recall": 1.0,
                          "judge_parse_ok": True})
    assert scores_by_id(run) == {"a": 1.0, "b": None}


def test_stability_flags_flip_and_parse_fail():
    r_ok = _mkrun({"a": 1.0, "b": 0.5, "c": 1.0}, n=48)
    r_flip = _mkrun({"a": 1.0, "b": 1.0, "c": 1.0}, n=48)      # b 翻转
    r_pf = _mkrun({"a": 1.0, "b": 0.5, "c": None}, n=48)       # c parse 失败
    stable, unstable = stability([r_ok, r_flip, r_pf])
    assert stable == {"a": 1.0}
    assert unstable == ["b", "c"]


def test_stability_rejects_mismatched_question_sets():
    with pytest.raises(AssertionError):
        stability([_mkrun({"a": 1.0}, n=48), _mkrun({"b": 1.0}, n=48),
                   _mkrun({"a": 1.0}, n=48)])


def test_paired_effect_two_sided_and_pt_math():
    a = {"q1": 1.0, "q2": 1.0, "q3": 0.5}
    b = {"q1": 0.5, "q2": 1.0, "q3": 1.0}
    e = paired_effect(a, b, n_scored=48)
    assert e["confirmed_cost_ids"] == ["q1"] and e["confirmed_gain_ids"] == ["q3"]
    assert e["confirmed_cost_pt"] == round(100 * 0.5 / 48, 2)   # 1.04pt
    assert e["confirmed_gain_pt"] == round(100 * 0.5 / 48, 2)


def test_paired_effect_swap_symmetry():
    # 对调型守卫: 输入对调后 cost/gain 必须互换 (集合断言的系统性盲区)
    a, b = {"q1": 1.0}, {"q1": 0.0}
    assert paired_effect(a, b, 48)["confirmed_cost_ids"] == \
           paired_effect(b, a, 48)["confirmed_gain_ids"] == ["q1"]


def _happy_inputs(cards_both_scores=None):
    cs = {f"q{i}": 1.0 for i in range(4)}
    cb = cards_both_scores or dict(cs)
    ds = {f"d{i}": 1.0 for i in range(3)}
    runs = {"cards_study": [_mkrun(cs, 48)] * 3, "cards_both": [_mkrun(cb, 48)] * 3,
            "docs_study": [_mkrun(ds, 30)] * 3, "docs_both": [_mkrun(ds, 30)] * 3}
    probes = {"cards": {"same_rate": 1.0}, "docs": {"same_rate": 1.0}}
    controls = {"docs_positive": {"avg": 1.0}, "docs_negative": {"avg": 0.0},
                "cards_positive": {"avg": 1.0}, "cards_negative": {"avg": 0.0}}
    return runs, probes, controls


def test_build_verdict_happy_path_cheap():
    v, rc = build_verdict(*_happy_inputs())
    assert rc == 0 and v["E2_verdict"] == "cheap_on_this_ruler"
    assert v["I1"]["pass"] and v["I2"]["pass"] and v["I3"]["pass"]
    assert v["advisory_only"] is False


def test_build_verdict_cost_reported():
    cb = {"q0": 0.5, "q1": 1.0, "q2": 1.0, "q3": 1.0}
    v, rc = build_verdict(*_happy_inputs(cards_both_scores=cb))
    assert rc == 0 and v["E2_verdict"] == "cost_reported"
    assert v["E"]["cards"]["confirmed_cost_ids"] == ["q0"]


def test_build_verdict_i2_trigger_blocks_e():
    runs, probes, controls = _happy_inputs()
    # cards 阈值是绝对数 7 — 用 8 题全翻钉死触发:
    big = {f"q{i}": 1.0 for i in range(8)}
    big_flip = {f"q{i}": 0.0 for i in range(8)}
    runs["cards_study"] = [_mkrun(big, 48), _mkrun(big_flip, 48), _mkrun(big, 48)]
    runs["cards_both"] = [_mkrun(big, 48)] * 3
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 2 and v["E"] is None and v["E2_verdict"] == "instrument_unusable"


def test_build_verdict_i3_trigger():
    runs, probes, controls = _happy_inputs()
    controls["cards_negative"] = {"avg": 0.5}                   # 阴性对照失守
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 2 and v["E2_verdict"] == "controls_failed" and v["E"] is None


def test_build_verdict_i1_degrades_to_advisory():
    runs, probes, controls = _happy_inputs()
    probes["docs"] = {"same_rate": 0.90}
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 3 and v["advisory_only"] is True and v["E"] is not None


def test_build_verdict_rejects_wrong_n():
    runs, probes, controls = _happy_inputs()
    runs["cards_study"] = [_mkrun({"q0": 1.0}, 47)] * 3        # 题集变了 = 阈值失义
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_fragile_and_undecidable_reported():
    runs, probes, controls = _happy_inputs()
    cs = {FRAGILE_4[0]: 1.0, "x": 1.0}
    cb = {FRAGILE_4[0]: 0.5, "x": 1.0}
    runs["cards_study"] = [_mkrun(cs, 48)] * 3
    runs["cards_both"] = [_mkrun(cb, 48)] * 3
    v, _ = build_verdict(runs, probes, controls)
    f = v["E3_fragile"][FRAGILE_4[0]]
    assert (f["study"], f["both"], f["stable_study"], f["stable_both"]) == (1.0, 0.5, True, True)
    assert v["E4_undecidable"] == {"cards": [], "docs": []}
```

- [ ] **Step 2: 跑测试确认失败** (`ModuleNotFoundError`):

```bash
./.venv/bin/python -m pytest scripts/tests/test_u5_verdict.py -q 2>&1 | tail -3
```

- [ ] **Step 3: 实现 `eval/u5_verdict.py`** 全文:

```python
"""U5 六段判定 (spec §5, 阈值冻结): I1 judge 重判 / I2 逐题稳定性 / I3 双向对照 /
E1 逐题配对双向效应 / E2 判定 / E3 脆弱 4 题 + E4 不可判池.

确定性脚本: 同输入恒同输出; 人不许手算改判 (spec §5.3-3). 产物零题面.
rc: 0 全过 · 2 = I2/I3 触发 (自毁/停下上报) · 3 = I1 降级 (advisory only).
"""
from __future__ import annotations

import argparse
import json

I1_MIN_SAME_RATE = 0.95
I2_MAX_UNSTABLE = {"cards": 7, "docs": 4}      # ≤15% of 48 / 30 (spec §5.1)
I3_POS_MIN, I3_NEG_MAX = 0.80, 0.20            # U2 冻结判据 (spec 修正案 2)
EXPECTED_N = {"cards": 48, "docs": 30}
FRAGILE_4 = ("st01_v11_q19", "st01_v2_q14", "st01_v2_q15", "st01_v2_q21")


def scores_by_id(run: dict) -> dict:
    """scored 行的 judge 分; parse 失败记 None (该遍分数来自子串兜底, 不可信)."""
    out = {}
    for r in run["results"]:
        if r.get("out_of_scope"):
            continue
        out[r["id"]] = r["judge_fact_recall"] if r.get("judge_parse_ok", False) else None
    return out


def stability(runs: list) -> tuple:
    """三遍 → (稳定题 id→分, 不稳定/不可信 id 清单). 稳定 = 三遍同分且全 parse_ok."""
    maps = [scores_by_id(r) for r in runs]
    ids = set(maps[0])
    assert all(set(m) == ids for m in maps), "三遍题集不一致"
    stable, unstable = {}, []
    for i in ids:
        vals = [m[i] for m in maps]
        if None in vals or len(set(vals)) != 1:
            unstable.append(i)
        else:
            stable[i] = vals[0]
    return stable, sorted(unstable)


def paired_effect(stable_a: dict, stable_b: dict, n_scored: int) -> dict:
    """E1: 两侧都稳定的题里 a(study) vs b(both). 双向对称 — 单向口径既漏真回归
    又杀真改善 (U3 §6-6 实测教训)."""
    common = set(stable_a) & set(stable_b)
    cost = {i: stable_a[i] - stable_b[i] for i in common if stable_a[i] > stable_b[i]}
    gain = {i: stable_b[i] - stable_a[i] for i in common if stable_b[i] > stable_a[i]}
    return {"confirmed_cost_pt": round(100 * sum(cost.values()) / n_scored, 2),
            "confirmed_cost_ids": sorted(cost),
            "confirmed_gain_pt": round(100 * sum(gain.values()) / n_scored, 2),
            "confirmed_gain_ids": sorted(gain),
            "n_compared": len(common)}


def build_verdict(runs: dict, probes: dict, controls: dict) -> tuple:
    i3 = {k: c["avg"] for k, c in controls.items()}
    i3_pass = (all(v >= I3_POS_MIN for k, v in i3.items() if k.endswith("positive"))
               and all(v <= I3_NEG_MAX for k, v in i3.items() if k.endswith("negative")))
    i1 = {k: p["same_rate"] for k, p in probes.items()}
    i1_pass = all(v >= I1_MIN_SAME_RATE for v in i1.values())

    stab, unstable = {}, {}
    for cfg, rs in runs.items():
        fam = cfg.split("_")[0]
        for r in rs:
            n = r["summary"]["n_questions"]
            if n != EXPECTED_N[fam]:
                raise SystemExit(f"{cfg}: n_questions {n} != {EXPECTED_N[fam]} — 题集变了, 阈值失义")
        stab[cfg], unstable[cfg] = stability(rs)

    i2_pass = all(len(v) <= I2_MAX_UNSTABLE[cfg.split("_")[0]] for cfg, v in unstable.items())
    out = {"thresholds": {"I1": I1_MIN_SAME_RATE, "I2": I2_MAX_UNSTABLE,
                          "I3": [I3_POS_MIN, I3_NEG_MAX]},
           "I1": {"same_rate": i1, "pass": i1_pass},
           "I2": {"counts": {c: len(v) for c, v in unstable.items()},
                  "unstable": unstable, "pass": i2_pass},
           "I3": {"avg": i3, "pass": i3_pass},
           "advisory_only": not i1_pass}
    if not (i3_pass and i2_pass):
        out["E"] = None
        out["E2_verdict"] = "controls_failed" if not i3_pass else "instrument_unusable"
        return out, 2

    out["E"] = {"cards": paired_effect(stab["cards_study"], stab["cards_both"], EXPECTED_N["cards"]),
                "docs": paired_effect(stab["docs_study"], stab["docs_both"], EXPECTED_N["docs"])}
    cheap = (out["E"]["cards"]["confirmed_cost_pt"] == 0
             and out["E"]["docs"]["confirmed_cost_pt"] == 0)
    out["E2_verdict"] = "cheap_on_this_ruler" if cheap else "cost_reported"
    out["E3_fragile"] = {q: {"study": stab["cards_study"].get(q),
                             "both": stab["cards_both"].get(q),
                             "stable_study": q in stab["cards_study"],
                             "stable_both": q in stab["cards_both"]} for q in FRAGILE_4}
    out["E4_undecidable"] = {
        "cards": sorted(set(unstable["cards_study"]) | set(unstable["cards_both"])),
        "docs": sorted(set(unstable["docs_study"]) | set(unstable["docs_both"]))}
    return out, (3 if not i1_pass else 0)


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    for cfg in ("cards-study", "cards-both", "docs-study", "docs-both"):
        p.add_argument(f"--{cfg}", nargs=3, required=True, metavar="RUN")
    p.add_argument("--probe-cards", required=True)
    p.add_argument("--probe-docs", required=True)
    p.add_argument("--controls", nargs=4, required=True,
                   metavar=("DOCS_POS", "DOCS_NEG", "CARDS_POS", "CARDS_NEG"))
    p.add_argument("--output", required=True)
    a = p.parse_args(argv)
    runs = {cfg.replace("-", "_"): [_load(x) for x in getattr(a, cfg.replace("-", "_"))]
            for cfg in ("cards-study", "cards-both", "docs-study", "docs-both")}
    probes = {"cards": _load(a.probe_cards), "docs": _load(a.probe_docs)}
    keys = ("docs_positive", "docs_negative", "cards_positive", "cards_negative")
    controls = dict(zip(keys, (_load(x) for x in a.controls), strict=True))
    verdict, rc = build_verdict(runs, probes, controls)
    with open(a.output, "w", encoding="utf-8") as f:
        json.dump(verdict, f, ensure_ascii=False, indent=1)
    print(f"I1 pass={verdict['I1']['pass']} {verdict['I1']['same_rate']}")
    print(f"I2 pass={verdict['I2']['pass']} counts={verdict['I2']['counts']}")
    print(f"I3 pass={verdict['I3']['pass']}")
    print(f"E2_verdict={verdict['E2_verdict']}  advisory_only={verdict['advisory_only']}")
    if verdict["E"]:
        for d in ("cards", "docs"):
            e = verdict["E"][d]
            print(f"  {d}: cost {e['confirmed_cost_pt']}pt {e['confirmed_cost_ids']}"
                  f" | gain {e['confirmed_gain_pt']}pt {e['confirmed_gain_ids']}")
    print(f"rc={rc}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 跑测试确认过 + 全量回归**

```bash
./.venv/bin/python -m pytest scripts/tests/test_u5_verdict.py -q 2>&1 | tail -3   # 12 passed
./.venv/bin/python -m pytest -p no:warnings --tb=no 2>&1 | tail -2                 # 1298 passed
```

- [ ] **Step 5: Commit**

```bash
git add eval/u5_verdict.py scripts/tests/test_u5_verdict.py
git commit -m "feat(u5): u5_verdict 确定性判定 (I1/I2/I3 + E1-E4, 阈值冻结, 12 case 钉死)"
```

---

### Task 4: I3 双向对照 (不过则停)

**Files:** 无代码; 产物 `data/study/st01/eval/runs/u5_ctrl_{docs,cards}_{positive,negative}.json`

- [ ] **Step 1: 跑 4 个对照** (LLM: judge 24 次调用):

```bash
cd sdtm-rag
for M in positive negative; do
  ./.venv/bin/python -m eval.judge_controls data/study/st01/eval/test_set_docs_v1.yml \
    --mode $M --n 6 --output "data/study/st01/eval/runs/u5_ctrl_docs_${M}.json"
  ./.venv/bin/python -m eval.judge_controls data/study/st01/eval/test_set_study_v2.yml \
    --mode $M --n 6 --output "data/study/st01/eval/runs/u5_ctrl_cards_${M}.json"
done
```

- [ ] **Step 2: 闸判定 (看产物不看回显)**

```bash
./.venv/bin/python -c "
import json
for name in ['u5_ctrl_docs_positive','u5_ctrl_docs_negative','u5_ctrl_cards_positive','u5_ctrl_cards_negative']:
    print(name, json.load(open(f'data/study/st01/eval/runs/{name}.json'))['avg'])"
```

判据 (冻结): 阳性 ≥ 0.80 且 阴性 ≤ 0.20 (U2 实测 1.0000/0.0000, 期望复现)。
**任一不满足 = I3 触发**: 归档 `evidence/failures/u5_attempt_1.md` + 停下上报, 不跑 Task 5。

- [ ] **Step 3: 记录** — 四个 avg 值 + 复跑命令记入工作笔记 (进 checkpoint §复跑命令)。

---

### Task 5: 4×3 答题矩阵 + rejudge 探针

**Files:** 产物 `data/study/st01/eval/runs/u5_{cards,docs}_{study,both}_r{1,2,3}.json` (12 个)
+ `u5_probe_{cards,docs}.json`; 日志 `data/study/st01/eval/logs/u5/` (gitignored, 含题面不进 git)

**Interfaces:**
- Consumes: Task 1 的观测字段 (产物自动带); U2 同款答题命令 (Global Constraint 6)。
- Produces: Task 7 判定的全部输入。

- [ ] **Step 1: 跑 12 个矩阵 run** (答题 468 次 + judge 468 次, 数小时, 建议 nohup 后台;
  **逐个跑完看产物再跑下一个不是必须, 但每完成一个配置 (3 遍) 应立即验产物**):

```bash
cd sdtm-rag
for i in 1 2 3; do
  for C in study both; do
    ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
      --hybrid --study-lookup --federated --corpus $C --study-docs --judge --temperature 0 \
      --full-answers --output "data/study/st01/eval/runs/u5_cards_${C}_r${i}.json" \
      > "data/study/st01/eval/logs/u5/cards_${C}_r${i}.log" 2>&1
    ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
      --hybrid --study-lookup --federated --corpus $C --study-docs --judge --temperature 0 \
      --full-answers --output "data/study/st01/eval/runs/u5_docs_${C}_r${i}.json" \
      > "data/study/st01/eval/logs/u5/docs_${C}_r${i}.log" 2>&1
  done
done
```

⚠ U2 栽过: shell 循环里 6 次跑批全失败而 echo 照打 done。**验收看产物** (Step 2), 不看日志。
⚠ `run_eval` 低于阈值 rc=1 是预期 (不是失败)。

- [ ] **Step 2: 产物验收 (12/12)**

```bash
./.venv/bin/python -c "
import json, itertools
for fam, n in (('cards', 48), ('docs', 30)):
    for c, i in itertools.product(('study', 'both'), (1, 2, 3)):
        p = f'data/study/st01/eval/runs/u5_{fam}_{c}_r{i}.json'
        d = json.load(open(p))
        s = d['summary']
        assert s['n_questions'] == n, (p, s['n_questions'])
        assert s['judge_model'] == 'deepseek/deepseek-chat', p
        assert all('answer' in r for r in d['results'] if not r.get('out_of_scope')), p
        assert all('routed' in r for r in d['results']), p
        routing = s['routing']
        assert routing == {c: s['n_total']}, (p, routing)   # 强制档: 全部题走该档
        pf = s['judge_parse_failures']
        print(p.split('/')[-1], 'judge_avg=', s['judge_fact_recall_avg'], 'parse_fail=', pf)
print('ALL 12 OK')"
```

任何 assert 炸 = 该 run 重跑 (删产物重来, 不许改验收)。

- [ ] **Step 3: rejudge 探针 (I1, 2 次重判)** — 探针文件按 spec §3.2 取 M2 r1 与 M4 r1:

```bash
./.venv/bin/python -m eval.rejudge_run data/study/st01/eval/runs/u5_cards_both_r1.json \
  data/study/st01/eval/test_set_study_v2.yml \
  --output data/study/st01/eval/runs/u5_probe_cards.json
./.venv/bin/python -m eval.rejudge_run data/study/st01/eval/runs/u5_docs_both_r1.json \
  data/study/st01/eval/test_set_docs_v1.yml \
  --output data/study/st01/eval/runs/u5_probe_docs.json
```

- [ ] **Step 4: 中途红线自查** — 12+2 个产物都在 gitignored 路径, `git status --short`
  必须**不出现** `data/study/` 任何文件; 出现 = 立刻停, 查 `.gitignore`。

---

### Task 6: auto 触发分布观测 (零 LLM 答题, 依赖 Task 1)

**Files:** 产物 `data/study/st01/eval/runs/u5_auto_{docs,cards}_r{1,2,3}.json`

- [ ] **Step 1: 6 个 retrieval-only auto run** (走 LLM 判库, 但零答题):

```bash
for i in 1 2 3; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --study-docs \
    --output "data/study/st01/eval/runs/u5_auto_docs_r${i}.json"
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
    --retrieval-only --hybrid --study-lookup --federated --study-docs \
    --output "data/study/st01/eval/runs/u5_auto_cards_r${i}.json"
done
```

- [ ] **Step 2: 观测分析 (直接观测, 不再演绎)** — 逐题 routed 现在在产物里:

```bash
./.venv/bin/python -c "
import json
from collections import Counter
FRAGILE = ['st01_v11_q19', 'st01_v2_q14', 'st01_v2_q15', 'st01_v2_q21']
for fam in ('docs', 'cards'):
    for i in (1, 2, 3):
        d = json.load(open(f'data/study/st01/eval/runs/u5_auto_{fam}_r{i}.json'))
        rows = d['results']
        dist = Counter(r['routed'] for r in rows)
        fb = Counter(r['routed_fallback'] for r in rows)
        line = f'{fam} r{i}: dist={dict(dist)} fallback={dict(fb)}'
        if fam == 'cards':
            dest = {r['id']: r['routed'] for r in rows if r['id'] in FRAGILE}
            line += f' fragile4={dest}'
        print(line)"
```

记录判读 (进 checkpoint):
- 分布对照 U3 both_ruler §4.1 (cards 45/5/1 · docs 27/0/3) — 一致/漂移都照录;
- **fallback 全 False 是前提** (非零 = router 稳定性问题, 停下上报, 触发率数字作废);
- 脆弱 4 题去向: U3 §4.2 只能演绎「都没被判到 both」, 本步是**直接观测**, 结论写明升级;
- 三遍间分布是否一致 (LLM 判库非确定性的直接读数)。

---

### Task 7: 判定执行 + E3 传导分析

**Files:** 产物 `data/study/st01/eval/runs/u5_verdict.json`

- [ ] **Step 1: 跑判定脚本**

```bash
R=data/study/st01/eval/runs
./.venv/bin/python -m eval.u5_verdict \
  --cards-study $R/u5_cards_study_r1.json $R/u5_cards_study_r2.json $R/u5_cards_study_r3.json \
  --cards-both  $R/u5_cards_both_r1.json  $R/u5_cards_both_r2.json  $R/u5_cards_both_r3.json \
  --docs-study  $R/u5_docs_study_r1.json  $R/u5_docs_study_r2.json  $R/u5_docs_study_r3.json \
  --docs-both   $R/u5_docs_both_r1.json   $R/u5_docs_both_r2.json   $R/u5_docs_both_r3.json \
  --probe-cards $R/u5_probe_cards.json --probe-docs $R/u5_probe_docs.json \
  --controls-docs-pos  $R/u5_ctrl_docs_positive.json \
  --controls-docs-neg  $R/u5_ctrl_docs_negative.json \
  --controls-cards-pos $R/u5_ctrl_cards_positive.json \
  --controls-cards-neg $R/u5_ctrl_cards_negative.json \
  --output $R/u5_verdict.json; echo "rc=$?"
```

rc=2 ⇒ 按 spec §5.3 执行 (归档 + 停下上报, **不写 E 结论**); rc=3 ⇒ E 结论全部
带 advisory 标注; rc=0 ⇒ 正常收口。

- [ ] **Step 2: 历史锚点并排 (只记录, 不判定)** — M1 (cards@study) 三遍均值与 U2 ON 臂
  (0.8542 / 0.8819) 并排写进 checkpoint; 差异照录不解释 (答题侧非确定, 无 exact 期望)。

- [ ] **Step 3: E3 传导分析写成文字** — 对 4 道脆弱题逐题回答: 检索侧丢分
  (q19 −0.5 / q14 −1.0 / q15 −0.5 / q21 −0.5, both_ruler §2.3) 在答题侧是
  传导 / 未传导 / 不可判 (E4)。`st01_v2_q14` (检索 gold 全丢) 单独一段。
  只用题号与数字, 零题面。

---

### Task 8: 三方核验 (规则 D, 五方不同 session)

**Files:**
- Create: `evidence/step_u5_audit.md` (抽检方 A, 进 git, 零题面)
- Create: `evidence/step_u5_audit_mutation.md` (抽检方 B, 进 git, 零题面)
- 审查方报告本地落盘 (gitignored), 结论摘录进 checkpoint

**Interfaces:** 三方均要求**边做边落盘** (硬规矩 17: 拿不到报告 = 那一环没发生)。

- [ ] **Step 1: 派审查方** (`subagent_type=oh-my-claudecode:code-reviewer`, opus) — 审:
  Task 1-3 diff (观测属性是否真零行为 / attach 长度闸 / rejudge fail-loud / verdict 与
  spec §5 阈值逐条对照) + 判定脚本对 spec 的偏离清单。必答: 「verdict 脚本里哪条断言
  删掉后 12 个 case 仍全绿?」

- [ ] **Step 2: 派抽检方 A** (`subagent_type=oh-my-claudecode:debugger`, opus) — 用**非自洽
  写法**复算 (硬规矩 17b): 不 import `eval.u5_verdict`, 自己从 12 个 run json 重新算
  稳定集 / E1 清单 / I2 计数, 与 `u5_verdict.json` 逐项对; 复算 I1 same_rate 与 I3 avg;
  验 12 产物的 `routing` 计数与强制档一致; 报告落 `evidence/step_u5_audit.md`。

- [ ] **Step 3: 派抽检方 B** (`subagent_type=oh-my-claudecode:test-engineer`, opus) — 变异
  测试三方向 (U2 §4.1): 从断言 / 从代码行 (新增三文件逐行) / 从断言逻辑形状,
  **变异集必须含对调型** (study/both 输入对调 · cost/gain 定义对调 · probes 两文件对调);
  SURVIVED 变异当场补断言杀掉; 报告落 `evidence/step_u5_audit_mutation.md`。

- [ ] **Step 4: controller 非自洽复算** — 抽两条 A/B 的关键数字亲手复现; 红线扫描:

```bash
grep -n "st01__" evidence/step_u5_audit.md evidence/step_u5_audit_mutation.md; echo "rc=$? (1=clean)"
./.venv/bin/python -c "
import re
for p in ['evidence/step_u5_audit.md', 'evidence/step_u5_audit_mutation.md']:
    t = open(p, encoding='utf-8').read()
    hits = re.findall(r'[぀-ヿ一-鿿]{12,}', t)
    bad = [h for h in hits if not any(k in h for k in ('已知限制', '不能证明'))]
    print(p, 'CJK12+ runs:', len(hits))"
```

(≥12 字连续 CJK 串人工过目 — 中文行文正常命中, 要排除的是**语料原文**; 判读记录进 checkpoint。)

- [ ] **Step 5: Commit**

```bash
git add evidence/step_u5_audit.md evidence/step_u5_audit_mutation.md
git commit -m "evidence(u5): 三方核验 (规则 D) — 审查/抽检 A 复算/抽检 B 变异"
```

---

### Task 9: 收口

**Files:**
- Create: `evidence/checkpoints/doc_track_u5_both_answer_cost.md`
- Modify: `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` §0′ (候选表)
- Modify: `docs/PROGRESS.md` (最后更新行 + Phase 7 单元格追加)
- Modify: `.work/meta/worklog/phase_07_rag_kg.md` (append)
- Modify: `CLAUDE.md` Key Paths (doc 轨行更新为 U1-U5, ≤80 字符)

- [ ] **Step 1: 写 checkpoint** — 结构对齐 U2/U3 收口件, 必含:
  0 一句话 / 1 改动面 (三件工具 + federation 2 行, 测试计数前后) / 2 数字 (I1/I2/I3 读数 ·
  E1 双向清单 · E2 判定 · E3 逐题 · E4 池 · auto 触发分布 · 生产日志事实照录
  (7 条 federation_routed / 0 both / 全 fallback=False, 2026-08-04~07, 无结论可下) ·
  历史锚点并排) /
  3 触发与豁免 (如有, 两句话分开写的纪律) / 4 三方核验表 / 5 已知限制 (**每条注明看不见
  什么**, 至少: 单模型单温度单 judge · judge 粗网格未修 · 收益侧未测 · 线上触发率无数据 ·
  eval 题集分布 ≠ 线上 · E2「便宜」只在此尺上) / 6 不能证明什么 (spec §8 逐条) /
  7 复跑命令逐字 / 8 任务台账。
  **引用纪律预写**: 若 E2 = cheap_on_this_ruler, 必须写「在此尺上便宜」不得写「无代价」;
  若任何闸触发过, 必须写「触发了, 处置是 X」。

- [ ] **Step 2: 改 kickoff §0′** — 候选表删 #3/#4 行, 补一行 U5 收口指针与结论一句话;
  #1 (判库重启) 的硬前置状态更新 (both 答题侧代价已测 ⇒ 该前置已补, 其余前置照旧)。

- [ ] **Step 3: PROGRESS / worklog / CLAUDE.md** — 按 Chain B: worklog append 本单元记录;
  PROGRESS 最后更新行重写 (U5 一段) + Phase 7 单元格追加一句; CLAUDE.md doc 轨 Key Paths
  行改为 `U1-U5 收口` 并保持 ≤80 字符。

- [ ] **Step 4: 全量回归 + 合并**

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no 2>&1 | tail -2   # 预期 1298+ passed
git checkout main && git merge --no-ff doc-track-u5 -m "merge(u5): doc 轨 U5 both 答题侧代价 + 答题侧仪器"
git push
```

- [ ] **Step 5: 汇报** — 一行: E2 判定 + 已确证代价/收益数字 + 触发过的闸 + 收口件路径。
