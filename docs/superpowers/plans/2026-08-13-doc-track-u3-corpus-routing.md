# doc 轨 U3 判库侧收口 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 doc 轨生产档丢掉的 10.00pt 判库损耗修回来 —— 先给 `both` 档建确定性尺子、把路由 gold 扩到手順書型,再改 `_ROUTER_SYSTEM` 规则 2 一处。

**Architecture:** 尺子先于修法。T1-T2 建量具(`eval/compare_runs.py` + 路由 gold 分组),T3 冻结改动前基线,T4 只看 dev 改 prompt,T5 用 held-out 验收。全程 `q15`/`q17`/`q53` 封存。

**Tech Stack:** Python 3.11 / pytest / PyYAML / chromadb / structlog;LLM router 走 Bedrock `jp.anthropic.*`(light 档)。

**Spec:** `docs/superpowers/specs/2026-08-13-doc-track-u3-corpus-routing-design.md`

## Global Constraints

- **数据红线**: 一切进 git 的内容**零真名零正文**。手順書题面 / 逐题明细一律落 `data/study/`(`.gitignore:10`)。stdout 与进 git 的文档只许出现 **id 与数字**。
- **工作目录**: 所有命令在 `sdtm-rag/` 下跑,Python 一律用 `./.venv/bin/python`。
- **开工基线**: `1189 passed / 0 failed / 0 errors / 0 skipped`;collections `sdtm_kb_v1 4329 / study_st01 959 / study_st01_docs 114`。对不上先查环境。
- **不要再加 `-q`**:`pyproject.toml` 的 `addopts` 已含 `-q`,再加一个就是 `-qq`,pytest 会**吞掉 `N passed` 汇总行**(本仓踩过)。用 `pytest -p no:warnings --tb=no | tail -2` 即可看到计数。
- **连跑 3 遍**: 任何检索跑批都连跑 3 遍(U2 §5-1:非确定性源在 embedding API)。三遍不一致的题必须逐题点名。
- **rc=1 ≠ 跑批失败**: `run_eval` 与 `run_routing_eval` 在不达标时返回 1。**去看产物,不要看日志**(U2 自己栽过:shell 变量未加引号致 6 次跑批全失败而 `echo` 照打 6 次 "done")。
- **自毁条款阈值不许改**: spec §7 六条。`LEGACY_EXACT_FLOOR = 178`;条款 2 间距 `25.0pt`;条款 3 `10/12`;条款 4 `≤ 1 题`。
- **规则 D**: 实现 / 审查 / 抽检 / 出题 / 划分 必须是不同 `subagent_type` 的不同 session。派 agent 时要求**边做边落盘**;拿不到报告就当那一环没发生并在证据里点名(硬规矩 17)。
- **规则 B**: 任何失败 attempt 归档到 `sdtm-rag/evidence/failures/`,不删。

---

## 文件结构

| 文件 | 责任 | 动作 |
|---|---|---|
| `eval/compare_runs.py` | `run_eval` 产物的逐题比对与跨遍稳定性 | **新建** |
| `scripts/tests/test_compare_runs.py` | 上者的测试 | **新建** |
| `eval/run_routing_eval.py` | 路由闸:+ 第 4/5 个 gold 来源、分组计分、条款 1 判定 | 改 |
| `scripts/tests/test_run_routing_eval.py` | 上者的测试 | 改 |
| `data/study/st01/eval/routing_gold_docs_draft.yml` | 出题方产物(42 题,无 group) | **新建 · gitignored** |
| `data/study/st01/eval/routing_gold_docs.yml` | 划分方产物(42 题,带 group) | **新建 · gitignored** |
| `server/federation.py` | `_ROUTER_SYSTEM` 规则 2 增补(**唯一生产改动**) | 改 |
| `evidence/checkpoints/doc_track_u3_corpus_routing.md` | 收口证据 | **新建** |

---

## Task 1: `eval/compare_runs.py` — 确定性 run 比对器

**Files:**
- Create: `eval/compare_runs.py`
- Test: `scripts/tests/test_compare_runs.py`

**Interfaces:**
- Consumes: `run_eval` 的 `--output` 产物(`{"summary": {...}, "results": [{"id", "source_recall", ...}]}`)
- Produces:
  - `load_scores(path) -> dict[str, float]`
  - `diff_scores(a: dict, b: dict) -> dict[str, tuple[float | None, float | None]]`
  - `unstable_ids(runs: list[dict]) -> dict[str, list[float | None]]`

**为什么要它**: U2 §5-1 实测检索有非确定性,任何「逐题 Δ0」都必须连跑 3 遍。此前各单元的逐题比对全是一次性 ad hoc 脚本,**没有测试守护** —— 而比对器自己出错的表现是「静默报无差异」。

- [ ] **Step 1: 写失败测试**

```python
# scripts/tests/test_compare_runs.py
"""U3 Task 1: run_eval 产物比对器. 每条断言对应一种「静默报无差异」的失败形态."""
import json

import pytest

from eval.compare_runs import diff_scores, load_scores, unstable_ids


def _write(tmp_path, name, results):
    p = tmp_path / name
    p.write_text(json.dumps({"summary": {}, "results": results}), encoding="utf-8")
    return p


def test_load_scores_reads_id_and_recall(tmp_path):
    p = _write(tmp_path, "r.json", [{"id": "a", "source_recall": 1.0},
                                    {"id": "b", "source_recall": 0.5}])
    assert load_scores(p) == {"a": 1.0, "b": 0.5}


def test_load_scores_rejects_empty_results(tmp_path):
    # 空产物比对恒等于「无差异」—— 最危险的假绿灯
    p = _write(tmp_path, "empty.json", [])
    with pytest.raises(ValueError):
        load_scores(p)


def test_load_scores_rejects_duplicate_id(tmp_path):
    # 后者覆盖前者 = 静默改变比对结果
    p = _write(tmp_path, "dup.json", [{"id": "a", "source_recall": 1.0},
                                      {"id": "a", "source_recall": 0.0}])
    with pytest.raises(ValueError):
        load_scores(p)


def test_diff_empty_when_identical():
    assert diff_scores({"a": 1.0}, {"a": 1.0}) == {}


def test_diff_reports_value_change():
    assert diff_scores({"a": 1.0}, {"a": 0.5}) == {"a": (1.0, 0.5)}


def test_diff_detects_missing_key_on_either_side():
    # 「一边少了几题」被读成「无差异」是本仓反复吃过的亏
    assert diff_scores({"a": 1.0, "b": 1.0}, {"a": 1.0}) == {"b": (1.0, None)}
    assert diff_scores({"a": 1.0}, {"a": 1.0, "b": 1.0}) == {"b": (None, 1.0)}


def test_unstable_ids_flags_varying_question():
    runs = [{"a": 1.0, "b": 1.0}, {"a": 1.0, "b": 0.5}, {"a": 1.0, "b": 1.0}]
    assert unstable_ids(runs) == {"b": [1.0, 0.5, 1.0]}


def test_unstable_ids_empty_when_all_runs_agree():
    runs = [{"a": 1.0}, {"a": 1.0}, {"a": 1.0}]
    assert unstable_ids(runs) == {}


def test_unstable_ids_requires_two_runs():
    # 单遍谈不上稳定性; 返回 {} 会被读成「三遍一致」
    with pytest.raises(ValueError):
        unstable_ids([{"a": 1.0}])


def test_unstable_ids_flags_key_present_in_only_some_runs():
    runs = [{"a": 1.0, "b": 1.0}, {"a": 1.0}]
    assert unstable_ids(runs) == {"b": [1.0, None]}
```

- [ ] **Step 2: 跑测试确认它红**

```bash
./.venv/bin/python -m pytest scripts/tests/test_compare_runs.py -p no:warnings --tb=short
```
Expected: FAIL —— `ModuleNotFoundError: No module named 'eval.compare_runs'`

- [ ] **Step 3: 写最小实现**

```python
# eval/compare_runs.py
"""U3 Task 1: run_eval 产物的逐题比对与跨遍稳定性 (spec 2026-08-13 §4).

为什么要它: U2 §5-1 实测检索有非确定性 (源在 embedding API, 同一 query 6 次得 2 种向量),
任何「逐题 Δ0」都必须连跑 3 遍才有意义。此前各单元的逐题比对都是一次性 ad hoc 脚本,
没有测试守护 —— 而比对器自己出错的表现是**静默报无差异**, 与「真的没差异」不可区分。

红线: 只吐 id 与分数, 不吐 question 文本 (id 形如 docs_v1_qNN, 不含语料内容)。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_scores(path: str | Path) -> dict[str, float]:
    """读 run_eval 产物, 返回 {question_id: source_recall}."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    results = data["results"]
    if not results:  # 空产物比对恒等于「无差异」
        raise ValueError(f"{path}: results 为空 —— 空比对恒真, 拒绝继续")
    out: dict[str, float] = {}
    for r in results:
        if r["id"] in out:  # 后者覆盖前者 = 静默改变比对
            raise ValueError(f"{path}: id 重复 {r['id']!r}")
        out[r["id"]] = r["source_recall"]
    return out


def diff_scores(a: dict[str, float],
                b: dict[str, float]) -> dict[str, tuple[float | None, float | None]]:
    """逐题差异 {id: (a, b)}; 只含不相等的题, 缺席一侧记 None.

    键集合取并集而非交集: 「一边少了几题」必须表现为差异, 不许被读成无差异。
    """
    return {k: (a.get(k), b.get(k))
            for k in sorted(set(a) | set(b))
            if a.get(k) != b.get(k)}


def unstable_ids(runs: list[dict[str, float]]) -> dict[str, list[float | None]]:
    """跨 N 遍不稳定的题 {id: [每遍分数]}. 少于 2 遍拒绝 —— 单遍返回 {} 会被读成「一致」."""
    if len(runs) < 2:
        raise ValueError(f"稳定性需要 >= 2 遍, 收到 {len(runs)} 遍")
    keys: set[str] = set().union(*runs)
    out: dict[str, list[float | None]] = {}
    for k in sorted(keys):
        vals = [r.get(k) for r in runs]
        if len(set(vals)) > 1:
            out[k] = vals
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="run_eval 产物逐题比对 (只吐 id, 不吐题面)")
    p.add_argument("runs", nargs="+", help="两个或以上 run_eval --output 产物")
    args = p.parse_args(argv)
    scored = [load_scores(f) for f in args.runs]
    for i, f in enumerate(args.runs, 1):
        vals = list(scored[i - 1].values())
        print(f"run {i}: n={len(vals)} avg={sum(vals) / len(vals):.4f}  {f}")
    unstable = unstable_ids(scored)
    print(f"unstable across {len(scored)} runs: {len(unstable)}")
    for k, vals in unstable.items():
        print(f"  {k}: {vals}")
    if len(scored) == 2:
        d = diff_scores(scored[0], scored[1])
        print(f"pairwise diff: {len(d)}")
        for k, (va, vb) in d.items():
            print(f"  {k}: {va} -> {vb}")
    return 1 if unstable else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 跑测试确认它绿**

```bash
./.venv/bin/python -m pytest scripts/tests/test_compare_runs.py -p no:warnings --tb=short
```
Expected: 10 passed

- [ ] **Step 5: 变异验证(证明断言不是装饰)**

手动改 `diff_scores` 的 `set(a) | set(b)` 为 `set(a) & set(b)`,重跑测试。
Expected: `test_diff_detects_missing_key_on_either_side` **变红**。改回来。

再把 `unstable_ids` 的 `len(runs) < 2` 改成 `len(runs) < 1`,重跑。
Expected: `test_unstable_ids_requires_two_runs` **变红**。改回来。

两条都不红 ⇒ 断言是装饰,当场补断言,不许往下走。

- [ ] **Step 6: 全量回归 + commit**

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2
```
Expected: `1199 passed`(1189 + 10)

```bash
git add eval/compare_runs.py scripts/tests/test_compare_runs.py
git commit -m "feat(doc-track): U3 Task 1 — run_eval 产物比对器 (逐题 + 跨遍稳定性)"
```

---

## Task 2: `both` 档尺子(只量不改)

**Files:**
- Create: `data/study/st01/eval/runs/u3_both_{docs,cards}_r{1,2,3}.json`(gitignored)
- Create: `data/study/st01/eval/runs/u3_study_docs_n8_r{1,2,3}.json`(gitignored)
- Create: `evidence/checkpoints/doc_track_u3_both_ruler.md`

**Interfaces:**
- Consumes: Task 1 的 `eval.compare_runs`
- Produces: 三个档的均值与逐题明细,供 Task 10 收口引用

**无生产代码改动** —— `eval/run_eval.py:739` 已支持 `--corpus both`。

- [ ] **Step 1: 开工自检(对不上就停)**

```bash
./.venv/bin/python -c "
import chromadb; cl = chromadb.PersistentClient(path='data/chroma')
print({c.name: c.count() for c in cl.list_collections()})"
```
Expected: `{'sdtm_kb_v1': 4329, 'study_st01': 959, 'study_st01_docs': 114}`

- [ ] **Step 2: 跑 B1 —— doc 30 题 @ `both`,3 遍**

```bash
for i in 1 2 3; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus both --study-docs \
    --output "data/study/st01/eval/runs/u3_both_docs_r${i}.json"
done
```
⚠ 变量必须加引号(U2 栽过的那一次)。rc=1 不是失败。

- [ ] **Step 3: 跑 B2 —— cards 48 题 @ `both`,3 遍**

```bash
for i in 1 2 3; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus both --study-docs \
    --output "data/study/st01/eval/runs/u3_both_cards_r${i}.json"
done
```

- [ ] **Step 4: 跑 B3 —— doc 30 题 @ `study` N=8,3 遍(隔离「cards 减半」的效应)**

```bash
for i in 1 2 3; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus study --study-docs \
    --doc-seats 8 --output "data/study/st01/eval/runs/u3_study_docs_n8_r${i}.json"
done
```

- [ ] **Step 5: 去看产物,不要看日志**

```bash
./.venv/bin/python -c "
import json, glob
fs = sorted(glob.glob('data/study/st01/eval/runs/u3_*_r?.json'))
assert len(fs) == 9, f'期望 9 个产物, 实得 {len(fs)}: {fs}'
for f in fs:
    d = json.load(open(f))['summary']
    print(f, d['n_questions'], d['source_recall_avg'], d.get('routing'))
"
```
Expected: 9 行;`u3_both_*` 的 `routing` 为 `None` 或不含 LLM 判库(强制 corpus 时不判库)。
B1/B3 的 `n_questions` = 30,B2 = 48。**9 个文件缺一个就停下查,不许往下走。**

- [ ] **Step 6: 三遍稳定性 + 关键比对**

```bash
# 各档三遍稳定性 (期望 unstable = 0; 非 0 则逐题点名, 不得隐藏)
./.venv/bin/python -m eval.compare_runs data/study/st01/eval/runs/u3_both_docs_r{1,2,3}.json
./.venv/bin/python -m eval.compare_runs data/study/st01/eval/runs/u3_both_cards_r{1,2,3}.json
./.venv/bin/python -m eval.compare_runs data/study/st01/eval/runs/u3_study_docs_n8_r{1,2,3}.json

# B2 vs U2 已落盘的 study 档 (0.8750) —— 这就是「cards 15 席 → 8 席」的代价
./.venv/bin/python -m eval.compare_runs \
  data/study/st01/eval/runs/u2_cards_docon_N8_r1.json \
  data/study/st01/eval/runs/u3_both_cards_r1.json

# B1 vs B3 —— doc 侧在 both 下是否受影响 (两者 doc 席位都是 8)
./.venv/bin/python -m eval.compare_runs \
  data/study/st01/eval/runs/u3_study_docs_n8_r1.json \
  data/study/st01/eval/runs/u3_both_docs_r1.json
```

- [ ] **Step 7: 写 `both` 尺子证据并 commit**

创建 `evidence/checkpoints/doc_track_u3_both_ruler.md`,必须含:
1. 三档均值(各三遍,逐遍列出,**不许只报一遍**)
2. 三遍不稳定题的 id 清单(为空则明写「三遍全一致」并附复跑命令)
3. B2 相对 0.8750 的差值 + 逐题降级清单(id + 前后分数)
4. B1 vs B3 的逐题 diff
5. **席位不对称的记录(不动)**:`federation.py:129` 的 `k_each=8` 只作用于 cards,`study_corpus.py:47` 的 `doc_seats` 不随 k 缩放 ⇒ doc 在 study 半边占比 35% → 50%。写明**本单元不改**及理由。
6. **它看不见什么**(硬规矩 19):只量检索侧 source recall;答题侧未测;`both` 的真实触发率未测(doc 30 题在 `auto` 下从不触发 `both`)。

```bash
git add evidence/checkpoints/doc_track_u3_both_ruler.md
git commit -m "evidence(doc-track): U3 Task 2 — both 档确定性尺子 (只量不改)"
```

---

## Task 3: `run_routing_eval.py` 支持手順書 gold 与分组计分

**Files:**
- Modify: `eval/run_routing_eval.py`
- Modify: `scripts/tests/test_run_routing_eval.py`

**Interfaces:**
- Consumes: `score_run(gold, predictions) -> dict`(已有,**不改**)
- Produces:
  - `FINAL_IDS = ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")`
  - `LEGACY_EXACT_FLOOR = 178`
  - `GROUPS: tuple[str, ...]`
  - `load_u1_doc_gold(path: Path) -> list[dict]`(每项含 `id/question/gold/group`)
  - `load_docs_routing_gold(path: Path) -> list[dict]`(同上)
  - `score_by_group(gold, predictions) -> dict[str, dict]`
  - `gate_verdict(gold, predictions) -> dict`(键:`fatal_excl_final` / `legacy_exact` / `by_group` / `passed`)

**关键口径(spec §7)**:条款 1 的 fatal 口径 = **全集减去 `final` 组**。`final` 组三题按条款 5 只报告。

- [ ] **Step 1: 写失败测试**

追加到 `scripts/tests/test_run_routing_eval.py` 末尾:

```python
# ── U3: 手順書 gold + 分组计分 (spec 2026-08-13 §5/§7) ──────────────
from eval.run_routing_eval import gate_verdict, score_by_group  # noqa: E402

_DOCS_QUESTION_YML = """
- id: docs_v1_q15
  question: dummy doc question 15
  expected_sources: [st01_doc_a]
- id: docs_v1_q17
  question: dummy doc question 17
  expected_sources: [st01_doc_b]
- id: docs_v1_q53
  question: dummy doc question 53
  expected_sources: [st01_doc_c]
- id: docs_v1_q01
  question: dummy doc question 01
  expected_sources: [st01_doc_d]
"""
_DOCS_ROUTING_YML = """
- id: u3_dev_01
  question: dummy authored doc-routing question
  gold: study
  group: dev
- id: u3_hold_01
  question: dummy held-out doc-routing question
  gold: study
  group: heldout
- id: u3_dist_01
  question: dummy cdisc distractor
  gold: cdisc
  group: distractor_cdisc
- id: u3_amb_01
  question: dummy genuinely ambiguous question
  gold: both
  group: ambiguous_both
"""


def _wire_u3(tmp_path, monkeypatch, *, docs_q=_DOCS_QUESTION_YML, docs_r=_DOCS_ROUTING_YML):
    _wire(tmp_path, monkeypatch)
    dq = tmp_path / "docs_q.yml"
    dq.write_text(docs_q, encoding="utf-8")
    dr = tmp_path / "docs_r.yml"
    dr.write_text(docs_r, encoding="utf-8")
    monkeypatch.setattr(run_routing_eval, "DOCS_QUESTION_SET", dq)
    monkeypatch.setattr(run_routing_eval, "DOCS_ROUTING_SET", dr)
    return dq, dr


def test_load_gold_tags_every_item_with_a_group(tmp_path, monkeypatch):
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    assert all(g["group"] in run_routing_eval.GROUPS for g in gold)
    by = {g["id"]: g["group"] for g in gold}
    assert by["c1"] == "legacy" and by["st_s1"] == "legacy" and by["ja_supp_01"] == "legacy"
    assert by["docs_v1_q15"] == "final" and by["docs_v1_q01"] == "u1_doc"
    assert by["u3_dev_01"] == "dev" and by["u3_hold_01"] == "heldout"


def test_u1_doc_questions_are_all_gold_study(tmp_path, monkeypatch):
    # spec §5.2: 统一标签消掉「标签被结果反向塑造」这个作弊面
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    docs = [g for g in gold if g["group"] in ("final", "u1_doc")]
    assert len(docs) == 4 and {g["gold"] for g in docs} == {"study"}


def test_missing_final_id_raises(tmp_path, monkeypatch):
    # 三题被改名/删掉而闸照跑 = 条款 5 的报告对象静默消失
    _wire_u3(tmp_path, monkeypatch,
             docs_q="- id: docs_v1_q01\n  question: q\n  expected_sources: [x]\n")
    with pytest.raises(ValueError, match="FINAL_IDS"):
        run_routing_eval.load_gold()


def test_docs_routing_gold_rejects_bad_group(tmp_path, monkeypatch):
    _wire_u3(tmp_path, monkeypatch,
             docs_r="- id: u3_x\n  question: q\n  gold: study\n  group: devv\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


def test_docs_routing_gold_rejects_legacy_group(tmp_path, monkeypatch):
    # 新题自称 legacy 会污染回归条款 1 的参照物
    _wire_u3(tmp_path, monkeypatch,
             docs_r="- id: u3_x\n  question: q\n  gold: study\n  group: legacy\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


@pytest.mark.parametrize("body", ["", "# 题全被删了\n"])
def test_empty_docs_routing_gold_raises(tmp_path, monkeypatch, body):
    _wire_u3(tmp_path, monkeypatch, docs_r=body)
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


def test_missing_docs_routing_gold_raises(tmp_path, monkeypatch):
    _wire_u3(tmp_path, monkeypatch)
    monkeypatch.setattr(run_routing_eval, "DOCS_ROUTING_SET", tmp_path / "nope.yml")
    with pytest.raises(FileNotFoundError):
        run_routing_eval.load_gold()


_G = [{"id": "L1", "gold": "cdisc", "group": "legacy"},
      {"id": "L2", "gold": "study", "group": "legacy"},
      {"id": "F1", "gold": "study", "group": "final"},
      {"id": "D1", "gold": "study", "group": "dev"},
      {"id": "H1", "gold": "study", "group": "heldout"}]


def test_score_by_group_slices_independently():
    preds = {"L1": "cdisc", "L2": "study", "F1": "cdisc", "D1": "study", "H1": "cdisc"}
    by = score_by_group(_G, preds)
    assert by["legacy"]["exact"] == 2 and by["legacy"]["fatal"] == 0
    assert by["dev"]["exact"] == 1
    assert by["heldout"]["exact"] == 0 and by["heldout"]["fatal"] == 1


def test_score_by_group_rejects_unknown_group():
    with pytest.raises(ValueError, match="未知 group"):
        score_by_group([{"id": "X", "gold": "cdisc", "group": "mystery"}], {"X": "cdisc"})


def test_gate_verdict_excludes_final_from_fatal(monkeypatch):
    # spec §7: 条款 1 与条款 5 会互相打架, 口径写死 = 全集减 final 组
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "cdisc", "L2": "study", "F1": "cdisc", "D1": "study", "H1": "study"}
    v = gate_verdict(_G, preds)
    assert v["fatal_excl_final"] == 0          # F1 判错但不计入
    assert v["by_group"]["final"]["fatal"] == 1  # 仍然如实报告
    assert v["passed"] is True


def test_gate_verdict_counts_non_final_fatal(monkeypatch):
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "cdisc", "L2": "study", "F1": "study", "D1": "cdisc", "H1": "study"}
    v = gate_verdict(_G, preds)
    assert v["fatal_excl_final"] == 1 and v["passed"] is False


def test_gate_verdict_fails_when_legacy_below_floor(monkeypatch):
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "both", "L2": "study", "F1": "study", "D1": "study", "H1": "study"}
    v = gate_verdict(_G, preds)          # L1 判 both: 非 fatal 但不 exact
    assert v["fatal_excl_final"] == 0 and v["legacy_exact"] == 1
    assert v["passed"] is False


def test_gate_verdict_raises_without_legacy_subset():
    # 回归条款 1 没有参照物时必须拒绝给结论, 而不是默认放行
    with pytest.raises(ValueError, match="legacy"):
        gate_verdict([{"id": "D1", "gold": "study", "group": "dev"}], {"D1": "study"})


def test_gate_verdict_does_not_print_question_text(tmp_path, monkeypatch, capsys):
    # 红线: stdout 只许出现 id 与数字
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    v = gate_verdict(gold, {g["id"]: g["gold"] for g in gold})
    assert "dummy" not in json.dumps(v, ensure_ascii=False)
```

在该测试文件顶部补 `import json`。

- [ ] **Step 2: 跑测试确认它红**

```bash
./.venv/bin/python -m pytest scripts/tests/test_run_routing_eval.py -p no:warnings --tb=short
```
Expected: FAIL —— `ImportError: cannot import name 'gate_verdict'`

- [ ] **Step 3: 改 `eval/run_routing_eval.py`**

在模块常量区(`EXACT_THRESHOLD` 附近)加:

```python
DOCS_QUESTION_SET = Path("data/study/st01/eval/test_set_docs_v1.yml")
DOCS_ROUTING_SET = Path("data/study/st01/eval/routing_gold_docs.yml")

# spec §7 条款 5: 这三题只报告不作 PASS 条件, 单独分组。硬编码 id (非题面) 入库是有意的 ——
# 它们必须可被 code review 看见, 否则「哪三题被豁免」就成了口头约定。
FINAL_IDS = ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")
# spec §7 条款 1: U2 收口实测三遍稳定 179/181, 留 1 题噪声余量。**不许下调。**
LEGACY_EXACT_FLOOR = 178
NEW_GROUPS = ("u1_doc", "final", "dev", "heldout", "distractor_cdisc", "ambiguous_both")
GROUPS = ("legacy", *NEW_GROUPS)
```

新增两个加载器(放在 `load_supplement` 之后):

```python
def load_u1_doc_gold(path: Path) -> list[dict]:
    """U1 的 30 道 doc 题, gold 一律 study (spec §5.2)。

    统一标签而非逐题裁定 —— 逐题裁定意味着标签可以被路由结果反向塑造。
    手順書内容 CDISC 结构上答不了, 这个统一是有实据的 (U1 各题 note 均记录反向查卡 0 命中)。
    """
    if not path.exists():
        raise FileNotFoundError(f"U1 doc 题集缺失: {path} —— 闸口不完整, 拒绝继续")
    items = load_test_set(str(path))
    if not items:
        raise ValueError(f"U1 doc 题集为空: {path} —— 闸口不完整, 拒绝继续")
    ids = {q["id"] for q in items}
    missing = sorted(set(FINAL_IDS) - ids)
    if missing:  # 三题被改名/删掉而闸照跑 = 条款 5 的报告对象静默消失
        raise ValueError(f"{path}: FINAL_IDS 缺失 {missing} —— 条款 5 无报告对象, 拒绝继续")
    return [{"id": q["id"], "question": q["question"], "gold": "study",
             "group": "final" if q["id"] in FINAL_IDS else "u1_doc"}
            for q in items]


def load_docs_routing_gold(path: Path) -> list[dict]:
    """U3 新写的 42 道路由题 (自带 gold + group)。缺文件/空文件 raise —— 同 load_supplement。"""
    if not path.exists():
        raise FileNotFoundError(f"U3 手順書路由 gold 缺失: {path} —— 闸口不完整, 拒绝继续")
    items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not items:
        raise ValueError(f"U3 手順書路由 gold 为空: {path} —— 闸口不完整, 拒绝继续")
    out = []
    for q in items:
        if not q.get("id") or not q.get("question"):
            raise ValueError(f"{path}: 条目缺 id/question: {q!r}")
        if q.get("gold") not in VALID_GOLD:
            raise ValueError(f"{path}: {q['id']} 的 gold={q.get('gold')!r} 非法")
        # legacy 被排除在外: 新题自称 legacy 会污染回归条款 1 的参照物
        if q.get("group") not in NEW_GROUPS:
            raise ValueError(
                f"{path}: {q['id']} 的 group={q.get('group')!r} 非法, 应属 {NEW_GROUPS}")
        out.append({"id": q["id"], "question": q["question"],
                    "gold": q["gold"], "group": q["group"]})
    return out
```

改 `load_gold()`:

```python
def load_gold() -> list[dict]:
    items = [{"id": q["id"], "question": q["question"], "gold": "cdisc", "group": "legacy"}
             for q in load_test_set(str(CDISC_SET))]
    items += [{"id": f"st_{q['id']}", "question": q["question"], "gold": "study",
               "group": "legacy"}
              for q in load_test_set(str(STUDY_SET)) if not q.get("out_of_scope")]
    items += [{**q, "group": "legacy"} for q in load_supplement(JA_SUPP_SET)]
    items += load_u1_doc_gold(DOCS_QUESTION_SET)
    items += load_docs_routing_gold(DOCS_ROUTING_SET)
    ids = [g["id"] for g in items]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:  # predictions 以 id 为键, 重名会互相覆盖 → 静默改变计分
        raise ValueError(f"gold id 重复: {dupes}")
    return items
```

新增计分函数(放在 `score_run` 之后):

```python
def score_by_group(gold: list[dict], predictions: dict[str, str]) -> dict[str, dict]:
    """按 group 切片各自 score_run。未知 group 直接 raise —— 分组口径写死在 spec §7。"""
    unknown = sorted({g.get("group") for g in gold} - set(GROUPS))
    if unknown:
        raise ValueError(f"未知 group: {unknown} —— 口径写死在 spec §7, 不许实施时新增")
    out = {}
    for name in GROUPS:
        subset = [g for g in gold if g.get("group") == name]
        if subset:
            out[name] = score_run(subset, predictions)
    return out


def gate_verdict(gold: list[dict], predictions: dict[str, str]) -> dict:
    """spec §7 条款 1 的判定。

    fatal 口径 = **全集减去 final 组** —— final 三题的 gold 是 study, 判去 cdisc 按
    score_run 就是 fatal; 若计入, 条款 1 会与条款 5 (只报告不作判据) 互相打架。
    """
    by_group = score_by_group(gold, predictions)
    if "legacy" not in by_group:  # 没有参照物时拒绝给结论, 而不是默认放行
        raise ValueError("legacy 子集缺失 —— 回归条款 1 无参照物, 拒绝给结论")
    non_final = [g for g in gold if g.get("group") != "final"]
    overall = score_run(non_final, predictions)
    legacy_exact = by_group["legacy"]["exact"]
    return {
        "n_scored_excl_final": overall["n"],
        "fatal_excl_final": overall["fatal"],
        "fatal_ids_excl_final": sorted(f["id"] for f in overall["fatal_items"]),
        "legacy_exact": legacy_exact,
        "legacy_floor": LEGACY_EXACT_FLOOR,
        "by_group": {k: {kk: vv for kk, vv in v.items() if kk != "fatal_items"}
                     for k, v in by_group.items()},
        "passed": overall["fatal"] == 0 and legacy_exact >= LEGACY_EXACT_FLOOR,
    }
```

改 `main()` 的打分与打印(替换 `s = score_run(gold, preds)` 那一段):

```python
        v = gate_verdict(gold, preds)
        per_run_preds.append(preds)
        detail = [{**g, "pred": preds[g["id"]]} for g in gold]
        (RUNS_DIR / f"routing_run_{run_i}.json").write_text(
            json.dumps({"summary": v, "detail": detail}, ensure_ascii=False, indent=1))
        groups = "  ".join(
            f"{k}:{s['exact']}/{s['n']}" for k, s in v["by_group"].items())
        print(f"run {run_i}: legacy {v['legacy_exact']}/{v['by_group']['legacy']['n']} "
              f"(floor {v['legacy_floor']})  fatal_excl_final={v['fatal_excl_final']}  "
              f"fallback={n_fallback}  {'PASS' if v['passed'] else 'FAIL'}")
        print(f"         groups: {groups}")
        if v["fatal_ids_excl_final"]:
            print(f"         fatal ids: {v['fatal_ids_excl_final']}")
        all_passed &= v["passed"]
```

⚠ `detail`(含题面)写进 `RUNS_DIR`(gitignored)不变;stdout 只打 id 与数字。

- [ ] **Step 4: 跑测试确认它绿**

```bash
./.venv/bin/python -m pytest scripts/tests/test_run_routing_eval.py -p no:warnings --tb=short
```
Expected: 全绿(原 11 条 + 新增 14 条 = 25 passed)

- [ ] **Step 5: 变异验证 —— 三个方向都跑**

| 方向 | 变异 | 期望变红的测试 |
|---|---|---|
| ①从断言出发 | `LEGACY_EXACT_FLOOR` 改 0 | `test_gate_verdict_fails_when_legacy_below_floor` |
| ②从代码行出发 | 删掉 `load_gold` 里 `items += load_docs_routing_gold(...)` 整行 | `test_load_gold_tags_every_item_with_a_group` |
| ③从断言的逻辑形状出发(**对调型**) | `gate_verdict` 里把 `!= "final"` 改成 `== "final"` | `test_gate_verdict_counts_non_final_fatal` |
| ③对调型之二 | `score_by_group` 里 `by_group["legacy"]` 换成任一其他组 | `test_gate_verdict_raises_without_legacy_subset` |

U2 §4.1 实证:**对调型是集合/差集类断言的系统性盲区,本仓已命中 5 次**。四条变异有任一不红 ⇒ 当场补断言,不许往下走。每条变异后**改回来**再跑下一条。

- [ ] **Step 6: 提交(此时 `routing_gold_docs.yml` 还不存在,`load_gold()` 会 raise —— 这是设计,不是 bug)**

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2
```
Expected: `1213 passed`(1199 + 14)

```bash
git add eval/run_routing_eval.py scripts/tests/test_run_routing_eval.py
git commit -m "feat(doc-track): U3 Task 3 — 路由闸支持手順書 gold + 分组计分 (条款 1 口径写死)"
```

---

## Task 4: 出题(规则 D 隔离,42 道新题)

**Files:**
- Create: `data/study/st01/eval/routing_gold_docs_draft.yml`(gitignored)

**Interfaces:**
- Consumes: `data/study/doc_chunks/`(C1 产出的 114 个章节 chunk)
- Produces: 42 条 `{id, question, gold, chapter}` —— **不含 `group`**(划分是 Task 5 的事)

**这一步必须派独立 subagent**(`subagent_type: oh-my-claudecode:scientist`),不许 controller 自己写题。

- [ ] **Step 1: 确认 chunk 语料位置与章分布**

```bash
./.venv/bin/python -c "
import glob, collections, re, os
fs = sorted(glob.glob('data/study/st01/docs/*.md'))
ch = collections.Counter(re.search(r'__s(\d+)', os.path.basename(f)).group(1) for f in fs)
print('n_chunks =', len(fs), '| chapters =', len(ch))
print(sorted(((int(k), v) for k, v in ch.items())))
"
```
Expected(controller 已实测): `n_chunks = 114 | chapters = 20`,分布
`[(2,7),(3,10),(4,2),(5,4),(6,14),(7,6),(8,6),(9,4),(10,5),(11,2),(12,11),(13,7),(14,4),(16,3),(17,2),(18,2),(19,3),(20,18),(21,2),(22,2)]`。

⚠ **语料是 20 章**;别处常见的「17 章」是 **U1 那 30 道题的覆盖章数**,不是语料章数。
出题按 20 章分层,不是 17。

- [ ] **Step 2: 派出题 subagent(prompt 逐字如下)**

> 你在为一个日语临床研究文档的**检索语料路由器**出题。任务是写 42 道题,只用于判断
> 「这个问题该查哪个语料库」,**不做检索打分**。
>
> **两个语料库**:
> - `cdisc`:公开的 CDISC SDTM 标准 —— 域(DM/AE/VS…)、变量、受控术语、实施指南章节。
> - `study`:某一个具体临床研究自己的产物 —— ① EDC 项目卡片(表单/画面/字段标签/选择肢/单位)
>   ② **该研究自己的手順書・計画文書的章节**(适格性、治療スケジュール、評価、統計解析計画)。
>
> **语料在** `data/study/st01/docs/*.md`(114 个章节 chunk,**跨 20 章**)。先读它们。
>
> **要写的四组**:
>
> | 组 | n | gold | 要求 |
> |---|---|---|---|
> | 手順書型 | 24 | `study` | 答案落在手順書章节里。**按章分层**,尽量覆盖多的章,同章不超过 3 题 |
> | 近似干扰 | 12 | `cdisc` | **听起来像临床规约,问的其实是 SDTM 标准**。用日语写 |
> | 真两可 | 6 | `both` | 缺任一侧都答不了,且**不含「標準」「SDTM」这类显式标准侧标记**(只凭主题就该判 both) |
>
> **硬纪律(违反即作废重来)**:
> 1. **不许运行或调用路由器**,不许读 `server/federation.py`。先探路由器判什么再照着写 = 给规则送分。
> 2. 与 `data/study/st01/eval/test_set_docs_v1.yml` 里已有的 30 道题**不得重叠**(先读它,避开)。
> 3. 每条必须带 `chapter: <章号整数>`(干扰题与两可题填 `chapter: 0`)。
> 4. id 用 `u3_doc_NN` / `u3_dist_NN` / `u3_amb_NN`。
> 5. 文件头写**前置声明**:出题依据、每组的形态、**以及本文件没覆盖什么**(照抄
>    `eval/routing_gold_ja_supplement.yml` 文件头「审阅 I-2 修正」那种诚实写法)。
> 6. **边做边落盘**到 `data/study/st01/eval/routing_gold_docs_draft.yml`,不要只在回复里给结果。
>
> 输出格式(YAML 列表):
> ```yaml
> - id: u3_doc_01
>   question: "……"
>   gold: study
>   chapter: 3
> ```

⚠ **不要在 prompt 里提** `docs_v1_q15`/`q17`/`q53`、也不要提它们的题型(解剖学定義 / 判定基準 /
分類体系)—— 泄漏任何一条,held-out 当场失效(spec §5.3 第 1 条)。

- [ ] **Step 3: 去看产物,不要看摘要(硬规矩 17)**

```bash
./.venv/bin/python -c "
import yaml, collections
d = yaml.safe_load(open('data/study/st01/eval/routing_gold_docs_draft.yml'))
print('n =', len(d))
print(collections.Counter(x['gold'] for x in d))
print('ids unique:', len({x['id'] for x in d}) == len(d))
print('chapters:', sorted(collections.Counter(
    x['chapter'] for x in d if x['gold']=='study').items()))
missing = [x['id'] for x in d if not all(k in x for k in ('id','question','gold','chapter'))]
print('missing fields:', missing)
"
```
Expected: `n = 42`;`Counter({'study': 24, 'cdisc': 12, 'both': 6})`;`ids unique: True`;
`missing fields: []`。**对不上就退回重出,不许自己补。**

- [ ] **Step 4: 与 U1 30 题的不重叠检查**

```bash
./.venv/bin/python -c "
import yaml
new = [x['question'] for x in yaml.safe_load(
    open('data/study/st01/eval/routing_gold_docs_draft.yml'))]
old = [q['question'] for q in yaml.safe_load(
    open('data/study/st01/eval/test_set_docs_v1.yml'))]
dupes = sorted(set(new) & set(old))
print('exact overlap:', len(dupes), dupes[:3])
assert not dupes, '与 U1 题面逐字重复, 退回重出'
print('OK')
"
```

- [ ] **Step 5: 归档出题 prompt(Tier 3 纪律)**

把 Step 2 的完整 prompt 存到 `evidence/subagent_prompts/u3_task4_authoring.md`(可入 git —— prompt 本身零语料内容)。

```bash
git add evidence/subagent_prompts/u3_task4_authoring.md
git commit -m "chore(doc-track): U3 Task 4 — 出题 subagent prompt 归档 (题集本身 gitignored)"
```

---

## Task 5: 确定性划分 dev/held-out + 生成最终 gold

**Files:**
- Create: `data/study/st01/eval/routing_gold_docs.yml`(gitignored)
- Create: `scripts/tests/test_u3_gold_redline.py`

**Interfaces:**
- Consumes: `routing_gold_docs_draft.yml`(Task 4)
- Produces: `routing_gold_docs.yml` —— 42 条带 `group`;`load_docs_routing_gold` 可读

**划分规则(spec §5.3 第 4 条,写死)**:24 道手順書型题**按 `chapter` 升序、同章内按 `id` 升序**排序后,**取偶数位(0-based)为 `dev`、奇数位为 `heldout`**。恰好 12/12 且跨章对称。
干扰题一律 `distractor_cdisc`,两可题一律 `ambiguous_both`。

**这一步由 Task 4 之外的 session 执行**(spec §8「划分方」)。

- [ ] **Step 1: 写划分脚本并当场执行(一次性,产物即证据)**

```bash
./.venv/bin/python - <<'PY'
import yaml
src = 'data/study/st01/eval/routing_gold_docs_draft.yml'
dst = 'data/study/st01/eval/routing_gold_docs.yml'
items = yaml.safe_load(open(src, encoding='utf-8'))
assert len(items) == 42, len(items)

docs = sorted([x for x in items if x['gold'] == 'study'],
              key=lambda x: (int(x['chapter']), x['id']))
assert len(docs) == 24, len(docs)
for i, x in enumerate(docs):
    x['group'] = 'dev' if i % 2 == 0 else 'heldout'

for x in items:
    if x['gold'] == 'cdisc':
        x['group'] = 'distractor_cdisc'
    elif x['gold'] == 'both':
        x['group'] = 'ambiguous_both'

out = [{'id': x['id'], 'question': x['question'], 'gold': x['gold'],
        'group': x['group'], 'chapter': x['chapter']} for x in items]
header = (
    "# U3 手順書型路由 gold (spec 2026-08-13 §5)\n"
    "# 划分规则 (确定性, 由出题方之外的 session 执行):\n"
    "#   24 道 gold=study 题按 (chapter, id) 升序排序, 偶数位(0-based)=dev / 奇数位=heldout。\n"
    "#   该规则保证恰好 12/12 且跨章对称; 「按章号奇偶」做不到 (17 章分布不均)。\n"
    "# 出题依据与形态覆盖的诚实说明: 见 routing_gold_docs_draft.yml 文件头 (出题方所写)。\n"
    "# 红线: 本文件 gitignored, 题面不入 git。\n")
open(dst, 'w', encoding='utf-8').write(
    header + yaml.safe_dump(out, allow_unicode=True, sort_keys=False))

import collections
print(collections.Counter(x['group'] for x in out))
print('dev chapters  :', sorted(int(x['chapter']) for x in out if x['group'] == 'dev'))
print('hold chapters :', sorted(int(x['chapter']) for x in out if x['group'] == 'heldout'))
PY
```
Expected: `Counter({'dev': 12, 'heldout': 12, 'distractor_cdisc': 12, 'ambiguous_both': 6})`

- [ ] **Step 2: 写红线测试**

```python
# scripts/tests/test_u3_gold_redline.py
"""U3: gold 文件的红线与完整性闸.

这两条不是「代码正确性」测试, 是**数据红线**测试 —— 手順書题面一旦进 git 就撤不回来了。
"""
import subprocess
from pathlib import Path

import pytest
import yaml

DRAFT = Path("data/study/st01/eval/routing_gold_docs_draft.yml")
FINAL = Path("data/study/st01/eval/routing_gold_docs.yml")


@pytest.mark.parametrize("path", [DRAFT, FINAL])
def test_gold_file_is_gitignored(path):
    """红线: 两个题集文件都必须被 gitignore 覆盖."""
    assert path.exists(), f"{path} 不存在 —— Task 4/5 未完成"
    rc = subprocess.run(["git", "check-ignore", "-q", str(path)]).returncode
    assert rc == 0, f"{path} 未被 gitignore 覆盖 —— 手順書题面会进 git"


@pytest.mark.parametrize("path", [DRAFT, FINAL])
def test_gold_file_is_not_tracked(path):
    """红线补强: 就算 gitignore 写对了, 文件也可能已被 `git add -f` 跟踪过."""
    rc = subprocess.run(["git", "ls-files", "--error-unmatch", str(path)],
                        capture_output=True).returncode
    assert rc != 0, f"{path} 已被 git 跟踪 —— 必须 git rm --cached"


def test_final_gold_group_counts():
    """划分规则的产物必须是 12/12/12/6 —— 数量漂了则条款 2/3/4 的分母就错了."""
    items = yaml.safe_load(FINAL.read_text(encoding="utf-8"))
    counts = {}
    for x in items:
        counts[x["group"]] = counts.get(x["group"], 0) + 1
    assert counts == {"dev": 12, "heldout": 12,
                      "distractor_cdisc": 12, "ambiguous_both": 6}


def test_dev_and_heldout_cover_disjoint_ids():
    items = yaml.safe_load(FINAL.read_text(encoding="utf-8"))
    dev = {x["id"] for x in items if x["group"] == "dev"}
    hold = {x["id"] for x in items if x["group"] == "heldout"}
    assert dev and hold and not (dev & hold)


def test_final_gold_preserves_draft_questions():
    """划分只许加 group, 不许改题面 —— 改题面等于绕过 Task 4 的出题隔离."""
    draft = {x["id"]: x["question"]
             for x in yaml.safe_load(DRAFT.read_text(encoding="utf-8"))}
    final = {x["id"]: x["question"]
             for x in yaml.safe_load(FINAL.read_text(encoding="utf-8"))}
    assert final == draft
```

- [ ] **Step 3: 跑测试**

```bash
./.venv/bin/python -m pytest scripts/tests/test_u3_gold_redline.py -p no:warnings --tb=short
```
Expected: 7 passed

- [ ] **Step 4: 确认路由闸能加载全 253 题**

```bash
./.venv/bin/python -c "
import sys, collections; sys.path.insert(0,'.')
from eval.run_routing_eval import load_gold
g = load_gold()
print('total =', len(g))
print('gold  =', collections.Counter(x['gold'] for x in g))
print('group =', collections.Counter(x['group'] for x in g))
assert len(g) == 253, len(g)
"
```
Expected: `total = 253`;
`group = Counter({'legacy': 181, 'dev': 12, 'heldout': 12, 'distractor_cdisc': 12, 'u1_doc': 27, 'ambiguous_both': 6, 'final': 3})`

- [ ] **Step 5: 全量回归 + commit**

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2
```
Expected: `1220 passed`(1213 + 7)

```bash
git add scripts/tests/test_u3_gold_redline.py
git commit -m "test(doc-track): U3 Task 5 — gold 红线闸 + 确定性 dev/heldout 划分 (12/12/12/6)"
```

---

## Task 6: T3 冻结改动前基线

**Files:**
- Create: `data/study/st01/eval/runs/routing_run_{1,2,3}.json` → 立即另存为 `u3_baseline_run_{1,2,3}.json`
- Create: `evidence/checkpoints/doc_track_u3_baseline.md`

**Interfaces:**
- Consumes: Task 3 的 `gate_verdict`、Task 5 的 253 题 gold
- Produces: 改 prompt 之前的六条条款各自的基线数字

**⚠ 本任务必定 FAIL 且 rc=1** —— prompt 还没改,手順書题大面积判错。**rc=1 不是跑批失败**;
T3 的产出是**落盘的基线数字**,不是绿灯。

- [ ] **Step 1: 跑三遍**

```bash
./.venv/bin/python -m eval.run_routing_eval --runs 3 2>&1 | tee /tmp/u3_baseline.log
echo "rc=${PIPESTATUS[0]} (1 = 未达标, 不是跑批失败)"
```

- [ ] **Step 2: 去看产物,立即另存(下一次跑批会覆盖 `routing_run_*.json`)**

```bash
for i in 1 2 3; do
  cp "data/study/st01/eval/runs/routing_run_${i}.json" \
     "data/study/st01/eval/runs/u3_baseline_run_${i}.json"
done
./.venv/bin/python -c "
import json
for i in (1,2,3):
    d = json.load(open(f'data/study/st01/eval/runs/u3_baseline_run_{i}.json'))
    s = d['summary']
    assert len(d['detail']) == 253, len(d['detail'])
    print(i, 'legacy', s['legacy_exact'], 'fatal_excl_final', s['fatal_excl_final'],
          {k: (v['exact'], v['n']) for k, v in s['by_group'].items()})
"
```
Expected: 3 行;每行 `detail` 长度 253。**少一个文件就停下查。**

- [ ] **Step 3: 记基线数字**

创建 `evidence/checkpoints/doc_track_u3_baseline.md`,逐条填(**只填数字与 id,不填题面**):

| 条款 | 基线口径 | 三遍值 |
|---|---|---|
| 1 | `legacy_exact` / `fatal_excl_final` | _r1 / r2 / r3_ |
| 2 | `heldout` 组 exact/12 | |
| 3 | `dev` 组 exact/12 | |
| 4 | `distractor_cdisc` 组 exact/12 | |
| 5 | `final` 组 exact/3 + 各自 pred | |
| — | `u1_doc` 组 exact/27、`ambiguous_both` 组 exact/6 | |

再加一段**三遍稳定性**:三遍中判定不一致的 id 清单(为空则明写「三遍全一致」)。

```bash
./.venv/bin/python -c "
import json
runs = [json.load(open(f'data/study/st01/eval/runs/u3_baseline_run_{i}.json'))
        for i in (1,2,3)]
preds = [{d['id']: d['pred'] for d in r['detail']} for r in runs]
ids = sorted(preds[0])
unstable = {i: [p[i] for p in preds] for i in ids if len({p[i] for p in preds}) > 1}
print('unstable:', len(unstable)); [print(' ', k, v) for k, v in unstable.items()]
"
```

- [ ] **Step 4: commit**

```bash
git add evidence/checkpoints/doc_track_u3_baseline.md
git commit -m "evidence(doc-track): U3 Task 6 — T3 改动前基线冻结 (253 题三遍, rc=1 是预期)"
```

---

## Task 7: 改 `_ROUTER_SYSTEM` 规则 2(只看 dev)

**Files:**
- Modify: `server/federation.py:37-50`(规则 2 段)

**Interfaces:**
- Consumes: Task 6 的 `dev` 组基线
- Produces: 改动后的 `_ROUTER_SYSTEM`;下游全部经 `route_corpus` 消费,签名不变

**⚠ 这是本单元唯一的生产改动,且 `_ROUTER_SYSTEM` 没有开关。回滚手段 = `git revert`。**

**实现方硬纪律**:
- **只许看** `dev` 组 12 题(`group == "dev"`)。
- **不许打开** `heldout` 组、`final` 组、`u1_doc` 组的任何题面。
- **规则文本写 pattern 不写 example**:不得出现来自任何具体题的临床概念(解剖部位名 / 特定评价体系名 / 特定测量阈值 / 具体域码)。

- [ ] **Step 1: 只导出 dev 12 题(其余组不落到实现方眼前)**

```bash
./.venv/bin/python -c "
import json
d = json.load(open('data/study/st01/eval/runs/u3_baseline_run_1.json'))
dev = [x for x in d['detail'] if x['group'] == 'dev']
assert len(dev) == 12, len(dev)
open('/tmp/u3_dev_only.json','w').write(json.dumps(
    [{'id':x['id'],'question':x['question'],'gold':x['gold'],'pred':x['pred']}
     for x in dev], ensure_ascii=False, indent=1))
print('wrote 12 dev questions')
"
```

- [ ] **Step 2: 改规则 2**

在 `server/federation.py` 规则 2 的结尾(`Rule 3 in turn outranks rule 2` 那句**之前**)插入:

```
Rule 2 also covers this study's own 手順書 / 計画文書: when the question asks for a
classification scheme, a judgement criterion, a definition, a schedule, or an assessment
procedure **as this study defines it** (何段階に分類されるか / どう判定するか / どう定義
されているか / いつ実施するか), the answer lives in that study's own document sections,
not in the public standard. The standard defines how to *submit* such data — which
variable, which domain, which controlled term — but never what one particular study's
protocol decided those categories, thresholds or definitions to be. So a question naming
a clinical concept the standard also covers is still rule 2 whenever what it asks for is
this study's own scheme rather than the standard's structure; the discriminator is the
**object of the question** (this study's decision vs the standard's representation), not
the clinical topic.
```

同时**修正规则 1 那句排除条款的口径**(它现在把整类手順書问题一并收走):把
`does not [make it study]` 那半句改成明确只对「问标准结构」成立:

```
merely naming a clinical concept the standard happens to cover (adverse events, severity
grading, lab results, dosing) does not by itself make a question rule 1 either — what makes
it rule 1 is that the thing being asked for is the standard's own structure or representation.
```

- [ ] **Step 3: 只对 dev 12 题验(不许跑全闸)**

```bash
./.venv/bin/python -c "
import json, sys; sys.path.insert(0,'.')
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router
llm = create_router(settings)
dev = json.load(open('/tmp/u3_dev_only.json'))
ok = 0
for q in dev:
    c, fb = route_corpus(llm, q['question'])
    ok += (c == q['gold'])
    print(q['id'], q['gold'], '->', c, 'fallback' if fb else '')
print(f'dev exact = {ok}/12')
"
```
Expected(spec §7 条款 3): `dev exact >= 10/12`。达不到就继续改**规则文本**,
**不许**看 held-out、**不许**改阈值。

- [ ] **Step 4: 单测护住 prompt 不被静默改坏**

追加到 `scripts/tests/test_federation.py`:

```python
def test_router_prompt_covers_study_own_documents():
    """规则 2 必须显式提到本研究自身的手順書/計画文書 —— 删掉它 doc 题会集体回到 cdisc."""
    from server.federation import _ROUTER_SYSTEM
    assert "手順書" in _ROUTER_SYSTEM or "手順" in _ROUTER_SYSTEM
    assert "計画文書" in _ROUTER_SYSTEM
    # pattern 而非 example: 判别器必须是「问的对象」, 不是某个临床主题
    assert "object of the question" in _ROUTER_SYSTEM


def test_router_prompt_carries_no_heldout_clinical_terms():
    """反对症下药闸: 规则文本不得出现 held-out 题的临床概念 (spec §6.1).

    词表**不写在这里** —— 把它写进 tracked 的测试文件, 等于把「held-out 是关于什么的」
    交给任何读这个测试的人 (包括本任务的实现方), 那正是本闸要防的事。
    词表由 controller 事先落在 gitignored 的 `data/study/st01/eval/heldout_banned_terms.txt`,
    每行一个词, `#` 开头为注释。**实现方不需要、也不许打开那个文件。**
    """
    from pathlib import Path

    from server.federation import _ROUTER_SYSTEM

    p = Path("data/study/st01/eval/heldout_banned_terms.txt")
    assert p.exists(), f"{p} 缺失 —— 本闸无词表则恒绿, 拒绝静默通过"
    banned = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
              if ln.strip() and not ln.startswith("#")]
    assert banned, f"{p} 为空 —— 空词表恒绿, 拒绝静默通过"
    hit = [w for w in banned if w in _ROUTER_SYSTEM]
    assert not hit, f"规则文本泄漏 held-out 概念 ({len(hit)} 个, 内容不打印以免二次泄漏)"
```

⚠ **给实现方的话**:上面这个测试你照抄即可。词表文件**已由 controller 备好**,
你**不需要也不许**打开 `heldout_banned_terms.txt` —— 打开它就等于看了 held-out,
本单元条款 2 的比较会因此失效(spec §6.2 防线 2)。

```bash
./.venv/bin/python -m pytest scripts/tests/test_federation.py -p no:warnings --tb=short
```
Expected: 全绿

- [ ] **Step 5: 变异验证**

删掉 Step 2 新插入的整段规则文本,跑 `test_router_prompt_covers_study_own_documents`。
Expected: **变红**。加回来。

在 `_ROUTER_SYSTEM` 里插一句含**词表第一行那个词**的例子,跑
`test_router_prompt_carries_no_heldout_clinical_terms`。Expected: **变红**。删掉。
⚠ 这一条由 **controller 代跑**(实现方不得读词表);实现方跑前两条即可,
并在报告里写「第三条变异由 controller 执行」。

- [ ] **Step 6: commit**

```bash
git add server/federation.py scripts/tests/test_federation.py
git commit -m "feat(doc-track): U3 Task 7 — router 规则 2 增补手順書触发条件 (pattern-level, 只看 dev)"
```

---

## Task 8: T5 验收 —— 六条条款逐条判定

**Files:**
- Create: `data/study/st01/eval/runs/u3_after_run_{1,2,3}.json`
- Create: `evidence/checkpoints/doc_track_u3_corpus_routing.md`(收口证据,Task 10 继续补)

**Interfaces:**
- Consumes: Task 6 的基线、Task 7 的新 prompt
- Produces: 六条条款的逐条 触发/未触发 判定

- [ ] **Step 1: 跑三遍全闸**

```bash
./.venv/bin/python -m eval.run_routing_eval --runs 3 2>&1 | tee /tmp/u3_after.log
echo "rc=${PIPESTATUS[0]}"
for i in 1 2 3; do
  cp "data/study/st01/eval/runs/routing_run_${i}.json" \
     "data/study/st01/eval/runs/u3_after_run_${i}.json"
done
```

- [ ] **Step 2: 去看产物**

```bash
./.venv/bin/python -c "
import json
for i in (1,2,3):
    d = json.load(open(f'data/study/st01/eval/runs/u3_after_run_{i}.json'))
    assert len(d['detail']) == 253, len(d['detail'])
    s = d['summary']
    print(i, 'passed', s['passed'], 'legacy', s['legacy_exact'],
          'fatal_excl_final', s['fatal_excl_final'],
          {k: (v['exact'], v['n']) for k, v in s['by_group'].items()})
"
```
3 行,每行 253。

- [ ] **Step 3: 逐条判定六条条款(判定脚本,不许口算)**

```bash
./.venv/bin/python - <<'PY'
import json
after = [json.load(open(f'data/study/st01/eval/runs/u3_after_run_{i}.json')) for i in (1,2,3)]
base  = [json.load(open(f'data/study/st01/eval/runs/u3_baseline_run_{i}.json')) for i in (1,2,3)]

def g(run, name, key='exact'):
    return run['summary']['by_group'][name][key]

print('=== 条款 1: 三遍每一遍 fatal_excl_final==0 且 legacy_exact>=178 ===')
c1 = all(r['summary']['fatal_excl_final'] == 0 and r['summary']['legacy_exact'] >= 178
         for r in after)
for i, r in enumerate(after, 1):
    print(f'  r{i}: fatal={r["summary"]["fatal_excl_final"]} '
          f'legacy={r["summary"]["legacy_exact"]}/181 '
          f'fatal_ids={r["summary"]["fatal_ids_excl_final"]}')
print('  条款 1:', '未触发 (PASS)' if c1 else '⛔ 触发')

print('=== 条款 2: heldout% >= dev% - 25.0pt (三遍均值) ===')
dev  = sum(g(r,'dev')  for r in after) / 3 / 12 * 100
hold = sum(g(r,'heldout') for r in after) / 3 / 12 * 100
print(f'  dev={dev:.2f}%  heldout={hold:.2f}%  gap={dev-hold:.2f}pt')
print('  条款 2:', '未触发 (PASS)' if hold >= dev - 25.0 else '⛔ 触发')

print('=== 条款 3: dev exact >= 10/12 (三遍均值) ===')
print(f'  dev 均值 = {sum(g(r,"dev") for r in after)/3:.2f}/12')
print('  条款 3:', '未触发 (PASS)' if sum(g(r,'dev') for r in after)/3 >= 10 else '⛔ 触发')

print('=== 条款 4: distractor_cdisc 较基线下降 <= 1 题 ===')
b = sum(g(r,'distractor_cdisc') for r in base)/3
a = sum(g(r,'distractor_cdisc') for r in after)/3
print(f'  基线 {b:.2f}/12 → 改动后 {a:.2f}/12  drop={b-a:.2f}')
print('  条款 4:', '未触发 (PASS)' if b - a <= 1 else '⛔ 触发')

print('=== 条款 5: final 三题只报告, 不作判据 ===')
for i, r in enumerate(after, 1):
    fin = {d['id']: d['pred'] for d in r['detail'] if d['group'] == 'final'}
    print(f'  r{i}: {fin}')
print('  ⚠ 看到这三题结果后不许回头改 prompt (spec §7 条款 5)')

print('=== 条款 6: 三遍稳定性 ===')
preds = [{d['id']: d['pred'] for d in r['detail']} for r in after]
uns = {k: [p[k] for p in preds] for k in preds[0] if len({p[k] for p in preds}) > 1}
print(f'  unstable = {len(uns)}')
for k, v in uns.items():
    print('   ', k, v)
PY
```

- [ ] **Step 4: 任一条款触发 → 停下上报,不许自行放宽**

若条款 1/2/3/4 任一触发:按 spec §7 的「触发后果」列执行(退回重写 / 不许上生产),
把该次 attempt 归档到 `evidence/failures/u3_task8_attempt_N.md`(规则 B:含输入 / 产物 /
技术判定 / 业务判定 / 下一 attempt 输入),**然后上报用户**。
**阈值一个字都不许改** —— U1/U2 各触发过一次,都是用户裁定豁免,不是自己放行。

- [ ] **Step 5: 写收口证据骨架 + commit**

创建 `evidence/checkpoints/doc_track_u3_corpus_routing.md`,先落这几段(数字全部来自 Step 3 输出):
§1 架构改动面 · §2 数字(三档 `both` 尺子 + 六条条款逐条) · §3 触发/豁免(如有)。

```bash
git add evidence/checkpoints/doc_track_u3_corpus_routing.md
git commit -m "evidence(doc-track): U3 Task 8 — 六条条款逐条判定 (三遍全闸)"
```

---

## Task 9: 三方核验(规则 D,五方不同 session)

**Files:**
- Create: `evidence/step_u3_audit.md`(抽检方 A)
- Create: `evidence/step_u3_audit_mutation.md`(抽检方 B)

**Interfaces:**
- Consumes: Task 1-8 全部产物
- Produces: 两份独立核验报告 + controller 的非自洽复算

**硬规矩 17**:派 agent 时要求**边做边落盘**;拿不到报告就当那一环没发生并在证据里点名。

- [ ] **Step 1: 派审查方(`subagent_type: oh-my-claudecode:code-reviewer`)**

审查范围:`eval/compare_runs.py` / `eval/run_routing_eval.py` 的改动 / `server/federation.py` 的规则文本。
必答三问:
1. 规则文本是 **pattern-level 还是 example-level**?举出它会误分类的一类问题。
2. `gate_verdict` 的 fatal 口径(减 `final` 组)有没有让某类真实回归逃过闸?
3. 有没有哪个新断言**该红不红**(U2 §4.2 的母题)?

- [ ] **Step 2: 派抽检方 A(`subagent_type: oh-my-claudecode:debugger`)**

任务:**独立复算** Task 8 Step 3 的每一个数字,**不许读 controller 的判定脚本输出**,
只从 `u3_{baseline,after}_run_{1,2,3}.json` 重算。逐条给「复现 / 不复现」。
额外要求:算 `dev` 与 `heldout` 的**逐题**判定表(id 级),点名任何 dev 全对而 heldout 全错的章。
落盘 `evidence/step_u3_audit.md`。

- [ ] **Step 3: 派抽检方 B(`subagent_type: oh-my-claudecode:test-engineer`)**

任务:对本单元新增的**全部**断言做变异测试,**三个搜索方向都要跑**(U2 §4.1):
① 从断言出发 ② **从代码行出发**(问「这行改坏了谁会红」——U2 用它抓到删光 27 行装配块测试一条不红)
③ **从断言的逻辑形状出发,变异集里必须有对调型**(U2 实证:对调型是集合/差集类断言的系统性盲区,本仓已命中 5 次)。
逐条给 KILLED / SURVIVED,SURVIVED 的当场补断言并复验。落盘 `evidence/step_u3_audit_mutation.md`。

- [ ] **Step 4: controller 非自洽复算(硬规矩 17b)**

关键数字用**与实现不同的写法**复算一遍:
```bash
# 253 = 181 + 27 + 3 + 12 + 12 + 12 + 6, 用 detail 直接数而不是读 summary
./.venv/bin/python -c "
import json, collections
d = json.load(open('data/study/st01/eval/runs/u3_after_run_1.json'))
c = collections.Counter(x['group'] for x in d['detail'])
print(c, sum(c.values()))
assert sum(c.values()) == 253
# legacy exact 用 detail 逐题重算, 不读 summary['legacy_exact']
lg = [x for x in d['detail'] if x['group'] == 'legacy']
print('legacy exact recomputed =', sum(x['pred'] == x['gold'] for x in lg), '/', len(lg))
"
```

- [ ] **Step 5: 全量回归 + commit**

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2
```
Expected: `N passed`,0 failed / 0 error / 0 skipped

```bash
git add evidence/step_u3_audit.md evidence/step_u3_audit_mutation.md
git commit -m "evidence(doc-track): U3 Task 9 — 三方核验 (规则 D 五方不同 session)"
```

---

## Task 10: 收口

**Files:**
- Modify: `evidence/checkpoints/doc_track_u3_corpus_routing.md`(补完)
- Modify: `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` §0′
- Modify: `docs/PROGRESS.md`
- Modify: `.work/meta/worklog/phase_07_rag_kg.md`
- Modify: `CLAUDE.md` Key Paths(仅当新 key path 需要)

- [ ] **Step 1: 补完收口证据**

`evidence/checkpoints/doc_track_u3_corpus_routing.md` 必须含:
- §1 架构 · §2 数字(`both` 三档 + 六条条款) · §3 触发与豁免(**若触发,必须写「触发了,用户裁定豁免」,不得写成「未触发」「验收通过」**)
- §4 三方核验表 · §5 **已知限制,每条注明它看不见什么**(至少:席位不对称未改 / held-out 只有 12 题 / 答题侧未测 / `both` 真实触发率未测 / `final` 三题不计入 fatal 口径)
- §6 **本单元不能证明什么**(照抄 spec §9)· §7 复跑命令(逐字)· §8 给下一单元的硬约束

- [ ] **Step 2: 更新 kickoff §0′ 下一单元表**

把 #1 与 #3 标为已完成(或「有条件完成」),剩余候选重排,并更新路由词指向。

- [ ] **Step 3: 更新 PROGRESS + worklog(Chain B)**

`docs/PROGRESS.md`:更新「最后更新」段与 milestone 列表;**顺手把陈旧的 `1181 passed` 更正为本单元的实测值**。
`.work/meta/worklog/phase_07_rag_kg.md`:append 本 session work record。

- [ ] **Step 4: 更新 AGENT_GUIDE 路由词**

`.work/AGENT_GUIDE.md` 的「doc 轨 开始任务」行:更新为剩余候选。

- [ ] **Step 5: Prune CLAUDE.md + commit**

按 CLAUDE.md「写作规则」扫一遍,删掉本阶段已关闭的进度状态,总行数控制在 150 行内。

```bash
git add -A
git commit -m "docs(doc-track): U3 收口 — kickoff/PROGRESS/worklog/AGENT_GUIDE 同步"
git push
```

---

## Self-Review

**1. Spec 覆盖**

| spec 段 | 对应 task |
|---|---|
| §2 单元边界(做/不做) | Task 2 §5 记录席位不对称不动;Task 7 只改 prompt |
| §3 顺序 T1-T7 + 双口径 | Task 2(T1)/ 4-5(T2)/ 6(T3)/ 7(T4)/ 8(T5)/ 9(T6)/ 10(T7);双口径见 Task 3 `gate_verdict` |
| §4 `both` 尺子 B1/B2/B3 各三遍 | Task 2 Step 2-4 |
| §5.1 文件位置与红线 | Task 5 Step 2 的 `test_gold_file_is_gitignored` / `_is_not_tracked` |
| §5.2 题量配比 24/12/6 + U1 30 一律 study | Task 4 Step 3;Task 3 `load_u1_doc_gold` + `test_u1_doc_questions_are_all_gold_study` |
| §5.3 出题纪律四条 | Task 4 Step 2 的 prompt + Step 5 归档 |
| §5.3 第 4 条确定性划分 | Task 5 Step 1 脚本 + `test_final_gold_group_counts` |
| §6.1 只改规则 2、写 pattern | Task 7 Step 2 + `test_router_prompt_carries_no_heldout_clinical_terms` |
| §6.2 三道防线 | Task 6(防线 1)/ Task 7 Step 1 只导 dev(防线 2)/ Task 3 `LEGACY_EXACT_FLOOR`(防线 3) |
| §6.3 无开关风险 | Task 7 抬头点名 |
| §7 六条条款 + fatal 口径 | Task 3 `gate_verdict` + Task 8 Step 3 判定脚本 |
| §8 五方核验 | Task 9 |
| §9 不能证明什么 | Task 10 Step 1 §6 |

**2. 占位符扫描**:无 TBD/TODO;每个代码步骤都给了完整代码块;每个命令都可逐字复制。

**3. 类型一致性**:
- `load_scores` / `diff_scores` / `unstable_ids` 在 Task 1 定义,Task 2 Step 6 按同名调用 ✓
- `gate_verdict` 返回键 `fatal_excl_final` / `legacy_exact` / `by_group` / `fatal_ids_excl_final` / `passed` 在 Task 3 定义,Task 6 Step 2、Task 8 Step 2-3 按同名读取 ✓
- `GROUPS` / `NEW_GROUPS` / `FINAL_IDS` / `LEGACY_EXACT_FLOOR` 在 Task 3 定义,Task 5 Step 4、Task 8 Step 3 引用 ✓
- gold 条目统一形状 `{id, question, gold, group}`(`routing_gold_docs.yml` 另带 `chapter`,加载器忽略)✓

**4. 测试计数链**:1189(基线)→ 1199(T1 +10)→ 1213(T3 +14)→ 1220(T5 +7)→ Task 7 再 +2 = **1222**。
Task 9 Step 5 只验「全 passed、0 failed/error/skipped」,不写死总数(抽检方 B 会补断言,总数会涨)。
