# 检索同质簇挤占 + gold 完整性 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修正 q38 的 gold 完整性缺陷 (pattern 层, 非单题), 用可证伪的实验判定同质簇挤占是否有害并据此决定是否修检索层, 最后收敛 chapters 整文件单块策略。

**Architecture:** 三段按依赖串行。段① 把判据修准 (含把 `check_source_recall` 的匹配逻辑提成共享函数, 让扫描工具与判据"同语义"成为结构保证)。段② 先落一把确定性结构探针 (层①), 再用 A/B1/B2 三组 context 对照 + LLM judge 作外部锚 (层②) 判定挤占有害与否 —— **判定规则先写死, 允许结论是"不修"**。段③ 调整 chapters chunker 阈值并重灌索引。

**Tech Stack:** Python 3.14 / pytest / ChromaDB / litellm (Bedrock `jp.anthropic.*` 答题, `deepseek/deepseek-chat` judge) / 现有 `server/rag.py` `RAGEngine` + `eval/run_eval.py`

**Spec:** `docs/superpowers/specs/2026-08-07-retrieval-crowding-and-gold-integrity-design.md`

## Global Constraints

- 工作目录一律 `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag`; 解释器一律 `.venv/bin/python` (勿用系统 python)。
- 基线: **862 passed** (`.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml` 后读 xml 的 `tests/failures/errors/skipped`)。该 repo 的 pytest 配置**吞掉末行统计**, 不要靠肉眼找 "N passed" 那一行。
- 每个 task 结束时 `pytest` 必须全绿, 且 passed 数只增不减。
- **写「实测」必须附可复跑的一行命令, 且数字必须真的从那条命令跑出来、单位对齐** (硬规矩 2)。尤其是要写进源码注释的数字。
- **三方隔离 (规则 D)**: 改 gold 的 agent ≠ 实施检索改动的 agent ≠ 抽检验收的 agent, 三个不同 `subagent_type`。
- **规则 A**: 抽样总体 = 本轮实际变更集合 (改动的 gold 条目 + 改动的检索行为), 不是变更后全集。
- **规则 B**: 任何失败 attempt 归档到 `sdtm-rag/evidence/failures/`, 不删。
- 红线: 真实 study 的 form/field OID / label / 题面 / 别名词只允许存在于 `sdtm-rag/data/study/` (gitignored)。本轮不碰 study 库, 但任何产出仍走程序化复扫。
- 现有已知限制不得在本轮"顺手调绿": `q126` 是永久 known limit; `eval/test_set_vi_completeness.yml` 的 `vic01` 在 `--judge` 口径下故意保留失分 0.5。

---

### Task 1: q38 判据订正 (段①1a)

**Files:**
- Modify: `eval/test_set_v3.yml` (q38 条目, 约 399 行)
- Test: `scripts/tests/test_gold_q38_integrity.py` (新建)

**Interfaces:**
- Consumes: `eval.run_eval.check_source_recall(retrieved_sources, expected_sources, any_of=None, retrieved_sections=None) -> tuple[float, list[str], list[str]]`
- Produces: 无新接口; 仅数据改动。后续 Task 依赖 q38 的 gold 变为两条 AND。

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_gold_q38_integrity.py`:

```python
"""q38 gold 完整性: 题干两问需要两个不可互相替代的源。

背景: 原 gold 只有 chapters/ch02, 而字面回答"two-character 规则"的是
ch04 §4.2.2 (dense 检索 #1)。原判据把一次正确检索判成 0.0 (假失分)。
"""
import yaml

from eval.run_eval import check_source_recall

TEST_SET = "eval/test_set_v3.yml"


def _q38():
    for q in yaml.safe_load(open(TEST_SET)):
        if q["id"] == "q38":
            return q
    raise AssertionError("q38 not found in " + TEST_SET)


def test_q38_gold_requires_both_sources():
    q = _q38()
    assert q.get("expected_sources_any") is None, "两问都要, 必须 AND 而非 OR"
    assert q["expected_sources"] == [
        "chapters/ch02",
        "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$",
    ]


def test_q38_gold_ch04_section_needs_exact_section_match():
    """§4.2.2 用 `$` 精确匹配: 不带 $ 时 '4.2.2 Two-character Domain Identifier'
    是子串语义, 而 ch04 里不存在更长的兄弟 section —— 但标识符+子串是通用隐患,
    统一按精确写。这条测试锁住"召回了 4.2 或 4.2.3 不算命中"。"""
    q = _q38()
    gold = q["expected_sources"]
    srcs = ["knowledge_base/chapters/ch04_general_assumptions.md"]

    recall, _, _ = check_source_recall(
        srcs, gold, retrieved_sections=["4.2.3 Use of \"Subject\" and USUBJID"]
    )
    assert recall == 0.0, "邻节不得冒名命中"

    recall, hits, _ = check_source_recall(
        srcs + ["knowledge_base/chapters/ch02_fundamentals.md"],
        gold,
        retrieved_sections=["4.2.2 Two-character Domain Identifier", "whole_file"],
    )
    assert recall == 1.0, hits
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_gold_q38_integrity.py -v`
Expected: FAIL — `test_q38_gold_requires_both_sources` 断言不等 (现 gold 只有一条 `chapters/ch02`)

- [ ] **Step 3: 改 gold**

`eval/test_set_v3.yml` 里 q38 的:

```yaml
  expected_sources:
  - chapters/ch02
```

改为:

```yaml
  expected_sources:
  - chapters/ch02
  - chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$
```

**只改 `test_set_v3.yml`。** `test_set_v1.yml` / `v2.yml` 是历史口径题集, 保持原样 —— 改它们会让历史 run 不可对接。

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_gold_q38_integrity.py -v`
Expected: 2 passed

- [ ] **Step 5: 跑全集看 q38 现在什么分**

Run:
```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output evidence/checkpoints/crowding_gold_after_q38.json
```
Expected: q38 recall = **0.0**。

**⚠️ 本条预期于 2026-08-07 由 Task 1 实测订正 (原写 0.5, 是错的)**:

| 口径 | q38 recall | 说明 |
|---|---|---|
| dense-only | **0.5** | ch04 §4.2.2 命中 (dense #1), ch02 未召回 |
| **hybrid + S1 (本命令 / 生产口径)** | **0.0** | §4.2.2 **被挤出 top-15**, 两条 gold 都没命中 |

原预期 0.5 出自 dense-only 诊断, 而本命令是 hybrid 口径 —— 二者不是一回事。
hybrid 下 14 条 domain spec 的 `§DOMAIN` chunk 占满 top-15, 把 dense 排**第 1** 的
§4.2.2 直接挤掉。

**这是预期结果, 不是失败, 且比原诊断更严重**: 挤占不是"让 gold 排不进来",
而是"把已经排第 1 的正确 chunk 挤掉"。**不许为了让 q38 变好看去动检索或再放宽 gold。**

- [ ] **Step 6: Commit**

```bash
git add eval/test_set_v3.yml scripts/tests/test_gold_q38_integrity.py \
        evidence/checkpoints/crowding_gold_after_q38.json
git commit -m "fix(eval): q38 gold 补 ch04 §4.2.2 — 原判据把 dense #1 的正确召回判成 0.0"
```

---

### Task 2: 把判据匹配逻辑提成共享函数 (段①1b 前置)

**Files:**
- Modify: `eval/run_eval.py:75-163` (`check_source_recall` 内的 `_matches` 闭包)
- Test: `scripts/tests/test_source_match_shared.py` (新建)

**Interfaces:**
- Produces: `eval.run_eval.source_matches(expected: str, retrieved_sources: list[str], retrieved_sections: list[str | None] | None = None) -> bool` — 模块级, 供 `check_source_recall` 与 Task 3 的扫描工具共用。

**为什么**: 硬规矩 1 要求"判据检查工具必须与被检查的判据**逐字同语义**"。上一轮 lint 靠"照着写一遍"来同语义, 制造了 8 条假阳性并连锁导致出题人删掉合法 gold。**同语义必须是结构保证 (同一个函数), 不是约定。**

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_source_match_shared.py`:

```python
"""source_matches 是 check_source_recall 与扫描工具的唯一匹配实现。

硬规矩 1: 判据检查工具与判据必须逐字同语义。上一轮靠"照着再写一遍"来保证,
制造了 8 条假阳性。这里把同语义变成结构保证, 并用测试锁住"两者调用同一个函数"。
"""
import inspect

import pytest

from eval.run_eval import check_source_recall, source_matches


def test_path_only_gold_is_substring_match():
    assert source_matches("chapters/ch02", ["kb/chapters/ch02_fundamentals.md"])
    assert not source_matches("chapters/ch09", ["kb/chapters/ch02_fundamentals.md"])


def test_section_gold_requires_same_entry():
    srcs = ["kb/chapters/ch04.md", "kb/chapters/ch02.md"]
    secs = ["4.1 Other", "4.2.2 Two-character Domain Identifier"]
    # 路径命中的是 #0, 但 section 命中的是 #1 -> 不同条目, 不算命中
    assert not source_matches("chapters/ch04.md#4.2.2", srcs, secs)
    assert source_matches("chapters/ch02.md#4.2.2", srcs, secs)


def test_exact_section_marker():
    srcs = ["kb/VARIABLE_INDEX.md"]
    assert source_matches("VARIABLE_INDEX.md#§一 通用变量: ARM", srcs, ["§一 通用变量: ARMCD"])
    assert not source_matches("VARIABLE_INDEX.md#§一 通用变量: ARM$", srcs, ["§一 通用变量: ARMCD"])


def test_empty_section_raises():
    with pytest.raises(ValueError, match="empty section"):
        source_matches("chapters/ch04.md#", ["kb/chapters/ch04.md"], ["4.1"])


def test_section_gold_without_sections_raises():
    with pytest.raises(ValueError, match="retrieved_sections"):
        source_matches("chapters/ch04.md#4.2.2", ["kb/chapters/ch04.md"])


def test_none_section_never_matches_section_gold():
    assert not source_matches("chapters/ch04.md#4.2.2", ["kb/chapters/ch04.md"], [None])


def test_check_source_recall_delegates_to_source_matches():
    """结构锁: check_source_recall 不得自带第二份匹配实现。"""
    src = inspect.getsource(check_source_recall)
    assert "source_matches(" in src, "check_source_recall 必须调用 source_matches"
    assert "def _matches" not in src, "不得保留内部匹配闭包 (会与共享实现漂移)"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_source_match_shared.py -v`
Expected: FAIL — `ImportError: cannot import name 'source_matches'`

- [ ] **Step 3: 重构**

在 `eval/run_eval.py` 中, 把 `check_source_recall` 里的 `_matches` 闭包整体提到模块级 (放在 `check_source_recall` 定义之前):

```python
def source_matches(
    expected: str,
    retrieved_sources: list[str],
    retrieved_sections: list[str | None] | None = None,
) -> bool:
    """单条 gold 的匹配判定 —— check_source_recall 与判据扫描工具的**唯一**实现。

    硬规矩 1 (2026-08-06 的教训): 判据检查工具与判据必须逐字同语义。上一轮用
    "照着再写一遍"来保证, lint 剥 `.md` 后匹配、严于真实判据, 制造 8 条假阳性,
    并连锁导致出题人删掉合法 gold。故同语义在此是**结构保证**: 谁都不许有第二份实现。

    语法与语义 (完整背景见 check_source_recall 的 docstring):
      - `路径`         -> 对 retrieved_sources 做子串匹配
      - `路径#节`      -> 双条件: 路径子串命中某条目 **且** 节子串命中**同一条目**的 section
      - `路径#节$`     -> 同上, 但 section 要求**精确相等** (对付互为子串的兄弟 section)
      - `路径#` (空节) -> ValueError (空 sec 下子串恒真, 会静默放宽判据)
      - 含 `#` 但未传 retrieved_sections -> ValueError (静默降级为路径匹配属测量缺陷)
      - section 为 None 的条目永不命中 section 级 gold
    """
    if "#" in expected:
        path, sec = expected.split("#", 1)
        exact = sec.endswith("$")
        if exact:
            sec = sec[:-1]
        if not sec.strip():
            raise ValueError(
                f"section-level gold {expected!r} has an empty section — 写全 `路径#节`, "
                "或改回纯路径写法。空 section 会静默退化成路径匹配 (判据比声称的宽)"
            )
        if retrieved_sections is None:
            raise ValueError(
                f"section-level gold {expected!r} requires retrieved_sections "
                "(caller must pass [c.section for c in chunks])"
            )
        if len(retrieved_sections) != len(retrieved_sources):
            raise ValueError("retrieved_sections length mismatch")
        return any(
            path in src and (s == sec if exact else sec in (s or ""))
            for src, s in zip(retrieved_sources, retrieved_sections)
        )
    return any(expected in src for src in retrieved_sources)
```

然后把 `check_source_recall` 体内的 `def _matches(exp): ...` 整块删掉, 并把两处 `_matches(exp)` / `_matches(e)` 调用改为:

```python
        found = source_matches(exp, retrieved_sources, retrieved_sections)
```
```python
        matched = [e for e in any_of if source_matches(e, retrieved_sources, retrieved_sections)]
```

`check_source_recall` 原 docstring 全文保留 (它是这套语法的权威说明), 在开头加一行:

```python
    """expected_sources 是 AND (每条都要命中); any_of 是 OR (任一命中即满足该组).

    单条匹配委托给模块级 `source_matches` —— 判据扫描工具共用同一实现 (硬规矩 1)。
```

- [ ] **Step 4: 跑测试确认通过 + 全集零回归**

Run: `.venv/bin/python -m pytest scripts/tests/test_source_match_shared.py -v`
Expected: 7 passed

Run 全量:
```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml >/dev/null 2>&1
.venv/bin/python -c "import xml.etree.ElementTree as ET;a=ET.parse('/tmp/j.xml').getroot().find('testsuite').attrib;print(a['tests'],'tests',a['failures'],'failures',a['errors'],'errors')"
```
Expected: failures=0 errors=0, tests ≥ 871 (862 + Task1 的 2 + 本 task 的 7)

**纯重构零行为改变的证明**: 重跑 Task 1 Step 5 那条 eval 命令, 输出与 `crowding_gold_after_q38.json` **逐题 Δ0**:

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output /tmp/after_refactor.json
.venv/bin/python -c "
import json
a=json.load(open('evidence/checkpoints/crowding_gold_after_q38.json'))
b=json.load(open('/tmp/after_refactor.json'))
ra={x['id']:x['source_recall'] for x in (a if isinstance(a,list) else a['results'])}
rb={x['id']:x['source_recall'] for x in (b if isinstance(b,list) else b['results'])}
d=[k for k in ra if ra[k]!=rb.get(k)]
print('逐题 Δ0' if not d else f'DIFF {d}')"
```
Expected: `逐题 Δ0`

- [ ] **Step 5: Commit**

```bash
git add eval/run_eval.py scripts/tests/test_source_match_shared.py
git commit -m "refactor(eval): 判据匹配提为共享 source_matches — 同语义变结构保证"
```

---

### Task 3: gold 完整性反例扫描 (段①1b)

**Files:**
- Create: `eval/scan_gold_gaps.py`
- Create: `scripts/tests/test_scan_gold_gaps.py`
- Modify: `eval/test_set_v3.yml` (仅在独立审判定为遗漏时)

**Interfaces:**
- Consumes: `eval.run_eval.source_matches` (Task 2), `server.rag.RAGEngine`
- Produces: `evidence/checkpoints/gold_gap_scan.json` — 每题一条 `{id, question, gold, unmatched_top3: [{source, section, sim, rank}]}`

**为什么**: 只改 q38 一题 = example-level 对症下药 (用户明确反对)。必须做 pattern 层扫描, 找出**同类**的 gold 遗漏。

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_scan_gold_gaps.py`:

```python
"""扫描器只做一件事: 列出 top-N 里不被任何 gold 匹配的条目。判定留给人/独立 agent。"""
from eval.scan_gold_gaps import unmatched_in_top_n


class _C:
    def __init__(self, source, section, sim):
        self.source, self.section, self.similarity = source, section, sim


def test_lists_entries_no_gold_matches():
    chunks = [
        _C("kb/chapters/ch04.md", "4.2.2 Two-character Domain Identifier", 0.70),
        _C("kb/chapters/ch02_fundamentals.md", "whole_file", 0.56),
    ]
    out = unmatched_in_top_n(chunks, ["chapters/ch02"], n=3)
    assert [o["source"] for o in out] == ["kb/chapters/ch04.md"]
    assert out[0]["rank"] == 1


def test_respects_section_level_gold():
    chunks = [_C("kb/VARIABLE_INDEX.md", "§一 通用变量: ARMCD", 0.6)]
    # section 级 gold 未命中 -> 该条目算 unmatched
    assert unmatched_in_top_n(chunks, ["VARIABLE_INDEX.md#§一 通用变量: ARM$"], n=3)
    # 命中 -> 不算
    assert not unmatched_in_top_n(chunks, ["VARIABLE_INDEX.md#§一 通用变量: ARMCD$"], n=3)


def test_n_truncates():
    chunks = [_C(f"kb/f{i}.md", "s", 0.5) for i in range(10)]
    assert len(unmatched_in_top_n(chunks, ["nothing"], n=3)) == 3


def test_or_group_gold_counts_as_matched():
    chunks = [_C("kb/domains/DM/spec.md", "DOMAIN", 0.6)]
    assert not unmatched_in_top_n(chunks, [], n=3, any_of=["domains/DM/spec.md"])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_scan_gold_gaps.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'eval.scan_gold_gaps'`

- [ ] **Step 3: 实现扫描器**

新建 `eval/scan_gold_gaps.py`:

```python
"""gold 完整性反例扫描: 列出每题 top-N 中"不被任何 gold 匹配"的检索条目。

用途: 找 q38 那类**判据遗漏**——检索找对了权威源, 但 gold 里没写, 于是被判 miss
(假失分), 或虽然别的 gold 命中了、真正的权威源却从未被判据看见 (判据视野盲区)。

本工具**只描述, 不判定**: 输出交独立 agent 逐条审"这是不是该题遗漏的权威源"。
匹配一律走 eval.run_eval.source_matches, 不自带第二份实现 (硬规矩 1)。
"""
from __future__ import annotations

import argparse
import json

import yaml

from eval.run_eval import source_matches


def unmatched_in_top_n(chunks, expected_sources, n=3, any_of=None):
    """返回 top-n 里不被任何 gold (AND 组 + OR 组合并看) 匹配的条目。

    逐条判定 (每条自成一个单元素列表) 而非整体判定: 我们要的是"**这一条**有没有
    被某条 gold 认领", 而 source_matches 的语义是"gold 在**整个列表**里有没有命中"。
    传整个列表会让 rank1 因为 rank3 命中而被误判为已认领。
    """
    golds = list(expected_sources or []) + list(any_of or [])
    out = []
    for rank, c in enumerate(list(chunks)[:n], 1):
        sec = getattr(c, "section", None)
        if any(source_matches(g, [c.source], [sec]) for g in golds):
            continue
        out.append({
            "rank": rank,
            "source": c.source,
            "section": sec,
            "sim": round(c.similarity, 4),
        })
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description="扫描 gold 完整性反例")
    p.add_argument("test_set")
    p.add_argument("--top-n", type=int, default=3)
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)

    from server.config import settings
    from server.rag import RAGEngine

    rag = RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=args.top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
    )

    rows = []
    qs = yaml.safe_load(open(args.test_set))
    for i, q in enumerate(qs, 1):
        chunks = rag.retrieve(q["question"], top_k=args.top_k)
        um = unmatched_in_top_n(
            chunks, q.get("expected_sources", []), n=args.top_n,
            any_of=q.get("expected_sources_any"),
        )
        rows.append({
            "id": q["id"], "category": q["category"], "question": q["question"],
            "gold": q.get("expected_sources", []),
            "gold_any": q.get("expected_sources_any"),
            "unmatched_top3": um,
        })
        print(f"[{i}/{len(qs)}] {q['id']} unmatched={len(um)}", flush=True)

    json.dump(rows, open(args.output, "w"), ensure_ascii=False, indent=1)
    n_any = sum(1 for r in rows if r["unmatched_top3"])
    print(f"\n{n_any}/{len(rows)} 题的 top-{args.top_n} 含未被 gold 匹配的条目")
    print(f"明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_scan_gold_gaps.py -v`
Expected: 4 passed

- [ ] **Step 5: 跑全集扫描**

Run:
```bash
.venv/bin/python -m eval.scan_gold_gaps eval/test_set_v3.yml \
  --output evidence/checkpoints/gold_gap_scan.json
```
Expected: 输出 140 行 + 汇总; 生成 `gold_gap_scan.json`

- [ ] **Step 6: 独立审 (规则 D — 必须换 subagent_type)**

派一个**与执行本 plan 不同**的 `subagent_type` (建议 `oh-my-claudecode:critic` 或 `oh-my-claudecode:scientist`), 交给它:

- 输入: `evidence/checkpoints/gold_gap_scan.json` + `knowledge_base/` 只读访问
- 任务: 对每条 `unmatched_top3` 条目判定 **"该条目是否为本题的权威答案源、而 gold 遗漏了它"**
- 要求: 逐条给 `verdict ∈ {遗漏_应补, 相关但非权威_不补, 不相关_不补}` + 一句理由 + 支撑正文的行号
- 禁止: 该 agent **不得**修改任何 gold, 只出判定
- 输出落到 `evidence/checkpoints/gold_gap_verdicts.md`

**注意**: 判定为"遗漏_应补"的, 才在 Step 7 补。判定门槛写死: **该条目正文必须字面回答题干的某一问**, 光"主题相关"不够 —— 这是 `any_of` 使用纪律第 2 条 (判据是"被召回的 chunk 能否回答", 不是"文件里有没有这段文字") 的直接套用。

- [ ] **Step 7: 按判定补 gold**

对每条"遗漏_应补", 在 `eval/test_set_v3.yml` 补进 `expected_sources` (section 级写法 `路径#节$`)。
每补一条, 在 `evidence/checkpoints/gold_gap_verdicts.md` 记前后 diff。

**若判定结果是"零条应补"**, 那也是合法结论 —— 说明 q38 是孤例, 照实记录, 不许为凑数硬补。

- [ ] **Step 8: 重跑全集 + 记录口径断裂**

Run:
```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output evidence/checkpoints/gold_integrity_after.json
```

把新分数记入证据, **必须写明**: 此分数与历史 98.93% (section 级) **换了一把尺子, 不可比**;
引用时必须带口径 "含 gold 完整性修复后"。

- [ ] **Step 9: Commit**

```bash
git add eval/scan_gold_gaps.py scripts/tests/test_scan_gold_gaps.py \
        eval/test_set_v3.yml evidence/checkpoints/gold_gap_scan.json \
        evidence/checkpoints/gold_gap_verdicts.md \
        evidence/checkpoints/gold_integrity_after.json
git commit -m "fix(eval): gold 完整性 pattern 层扫描 + 独立审补漏"
```

---

### Task 3C: section 级 gold 存在性闸 (Task 1 评审的 Important 2)

**Files:**
- Create: `scripts/tests/test_section_gold_exists.py`

**Interfaces:**
- Consumes: `eval.run_eval.source_matches` (Task 2), chroma collection

**为什么**: 用 `#节$` 精确匹配后, gold 与 chunker 的 section 命名**强耦合**。重建索引时命名
一变 (加前缀 / 重编号 / 去引号), 这条 gold 就**静默变成永不命中**, 题目继续显示低分,
而没人分得清是判据坏了还是检索坏了。这正是 `check_source_recall` docstring 警告的
"打错的 gold 恒 miss, 比多匹配更隐蔽"。**Task 8 要重灌索引, 所以这个闸必须在它之前就位。**

现状实测 (`2026-08-07`): `eval/test_set_v3.yml` 共 **20** 条 section 级 gold,
其中指向 `chapters/` 的只有 **1** 条 (q38 的 `ch04...#4.2.2...$`, ch04 走 H3 不受 Task 8 影响);
**无任何 gold 引用 `whole_file`**。故当前风险低 —— 但闸是给将来的。

- [ ] **Step 1: 写失败测试 (先确认它真能抓到问题)**

新建 `scripts/tests/test_section_gold_exists.py`:

```python
"""section 级 gold 必须在索引里真实存在 —— 否则静默恒 miss。

用 `路径#节$` 精确匹配后, gold 与 chunker 的 section 命名强耦合。重灌索引若改了
命名, gold 会无声失效: 题目一直低分, 而看不出是判据坏了还是检索坏了。
"""
import yaml

TEST_SET = "eval/test_set_v3.yml"


def _section_golds():
    with open(TEST_SET, encoding="utf-8") as f:
        qs = yaml.safe_load(f)
    out = []
    for q in qs:
        golds = (q.get("expected_sources") or []) + (q.get("expected_sources_any") or [])
        for g in golds:
            if "#" in str(g):
                out.append((q["id"], g))
    return out


def test_there_are_section_golds_to_check():
    """护栏的护栏: 若这里变成 0, 上面的解析八成坏了, 而下面的测试会空转通过。"""
    assert len(_section_golds()) >= 15


def test_every_section_gold_exists_in_index():
    import pytest

    from server.config import settings
    from server.rag import RAGEngine

    try:
        rag = RAGEngine(
            chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
            collection_name=settings.collection_name,
            embedding_model=settings.embedding_model, top_k=1,
        )
        got = rag.collection.get(include=["metadatas"])
    except Exception as exc:  # 无索引的环境跳过, 与既有集成测试同策
        pytest.skip(f"needs live index: {exc}")

    pairs = {(m.get("source") or "", m.get("section")) for m in got["metadatas"]}

    missing = []
    for qid, gold in _section_golds():
        path, sec = gold.split("#", 1)
        exact = sec.endswith("$")
        if exact:
            sec = sec[:-1]
        hit = any(
            path in src and (s == sec if exact else sec in (s or ""))
            for src, s in pairs
        )
        if not hit:
            missing.append(f"{qid}: {gold}")

    assert not missing, (
        "以下 section 级 gold 在索引里不存在 —— 它们会静默恒 miss:\n  "
        + "\n  ".join(missing)
    )
```

- [ ] **Step 2: 跑测试, 确认当前全绿**

Run: `.venv/bin/python -m pytest scripts/tests/test_section_gold_exists.py -v`
Expected: 2 passed

**若有 gold 被报为不存在**: 那就是抓到真问题了 —— 逐条查明是 gold 写错还是索引变了,
在报告里列出并**据实修 gold**(不许改闸来迁就)。

- [ ] **Step 3: 反向验证闸真的会红 (不许只看它绿)**

临时把某条 section gold 改成一个不存在的 section (例如把 q38 那条的 `4.2.2` 改成 `4.2.2X`),
重跑测试, **确认它 FAIL 并在消息里点名 q38**; 然后**改回来**再跑一次确认绿。
把这两次的原始输出贴进报告。

**理由**: 一个从没红过的闸, 和没有闸是一回事。上一轮 VI 那次就是断言恒绿而缺陷照样溜过去。

- [ ] **Step 4: Commit**

```bash
git add scripts/tests/test_section_gold_exists.py
git commit -m "test(eval): section 级 gold 存在性闸 — 防重灌索引后判据静默失效"
```

---

### Task 3B: top-k 抖动的量化与探针稳健化 (Task 1 评审发现, plan 原本没有)

**Files:**
- Create: `evidence/checkpoints/topk_jitter.md`
- Create: `eval/jitter_probe.py`
- Create: `scripts/tests/test_jitter_probe.py`

**Interfaces:**
- Produces: `eval.jitter_probe.stability_report(runs: list[list[str]]) -> dict` —
  返回 `{n_runs, distinct_sets, distinct_orders, stable_prefix, always, sometimes}`
- Produces: 一个二值结论 `JITTER_AFFECTS_STATS ∈ {true, false}`, 决定 Task 4 探针是否必须多次取样

**为什么 (来源: Task 1 评审的额外发现, 非 plan 原有)**

评审同 query 同参数连跑两次, top-15 **第 9 位起成分变化** (run1 第 9 位 BS / run2 第 9 位 TE)。
控制器随后用 chunk_id 跑 5 次却**全稳定** (逐位 15/15) —— 说明抖动**偶发**而非必然。
同一次探测实测到根因线索: **embedding API 重复调用返回的向量不逐位相同**
(`len(set(embs)) == 1` 为 **False**)。`§DOMAIN` 簇 61 条挤在 sim [0.6689, 0.6851],
簇内相邻间隔极小, 浮点抖动足以翻转尾部顺序。

**这威胁的是层① 的全部数字** (`max_cluster` / `dup_seats` / "28.6%"), 它们都出自单次 top-15
且要写进证据。**在量化清楚之前, 层① 的数字不许当作稳定事实引用。**

⚠️ **控制器踩过的坑, 别重蹈**: 首版抖动探针用 `文件名#section` 作条目标识,
而 63 个域的文件名都是 `spec.md`、section 都是 `DOMAIN` → 14 条塌缩成 1 个字符串,
探针于是"证明"了稳定性。**标识必须用 `chunk_id`**。症状是"每次都在的"只有 2 条 —— 
凡稳定性探针, 先验证它区分得开你要区分的东西。

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_jitter_probe.py`:

```python
"""稳定性统计的口径。构造已知的多次运行结果, 验统计正确。"""
from eval.jitter_probe import stability_report


def test_all_runs_identical():
    runs = [["a", "b", "c"]] * 4
    r = stability_report(runs)
    assert r["n_runs"] == 4
    assert r["distinct_sets"] == 1
    assert r["distinct_orders"] == 1
    assert r["stable_prefix"] == 3
    assert r["always"] == 3
    assert r["sometimes"] == 0


def test_tail_swap_same_set():
    """成分相同、顺序不同 —— 集合数 1 但顺序数 2。"""
    runs = [["a", "b", "c"], ["a", "c", "b"]]
    r = stability_report(runs)
    assert r["distinct_sets"] == 1
    assert r["distinct_orders"] == 2
    assert r["stable_prefix"] == 1
    assert r["sometimes"] == 0


def test_membership_churn():
    runs = [["a", "b", "c"], ["a", "b", "d"]]
    r = stability_report(runs)
    assert r["distinct_sets"] == 2
    assert r["stable_prefix"] == 2
    assert r["always"] == 2      # a, b
    assert r["sometimes"] == 2   # c, d


def test_identifiers_must_be_distinguishable():
    """探针自身的护栏: 全同标识说明标识选错了 (控制器踩过 —— 63 个 spec.md#DOMAIN
    塌缩成 1 个 key, 探针于是假装稳定)。"""
    import pytest
    with pytest.raises(ValueError, match="indistinguishable"):
        stability_report([["x", "x", "x"], ["x", "x", "x"]])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_jitter_probe.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'eval.jitter_probe'`

- [ ] **Step 3: 实现探针**

新建 `eval/jitter_probe.py`, 含 `stability_report(runs)` 与一个跑批 `main`。
`main` 要求:

- 用 **`chunk_id`** 作条目标识 (不是文件名, 不是 section)
- 默认 `--runs 12`, 每次**新建 RAGEngine** 并重新 embed (模拟真实调用)
- 支持 `--config hybrid|dense|both`
- 额外测量并输出:
  - embedding 重复调用的**最大逐位差值**与 L2 距离 (证明抖动源)
  - top-15 内**相邻 similarity 的最小间隔** (证明为什么这点抖动足以翻转顺序)
- `stability_report` 在所有 run 的所有标识去重后**总数 ≤ 1** 时抛
  `ValueError("indistinguishable identifiers: ...")`

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_jitter_probe.py -v`
Expected: 4 passed

- [ ] **Step 5: 对挤占最重的题跑抖动实测**

对 q38 + 层① 榜上 max_cluster ≥5 的题各跑 `--runs 12`:

```bash
.venv/bin/python -m eval.jitter_probe --runs 12 --config both \
  --output evidence/checkpoints/topk_jitter.json
```

- [ ] **Step 6: 判定 + 写证据**

写 `evidence/checkpoints/topk_jitter.md`, 含完整命令 + 原始输出 + 结论:

| 观察 | 结论 | 对 Task 4 的要求 |
|---|---|---|
| 12 次 `distinct_orders == 1` 且 `sometimes == 0` | 抖动不影响 top-15 | `JITTER_AFFECTS_STATS = false`, Task 4 单次取样即可, 但证据里要写明"已用 12 次验稳" |
| 顺序变但成分不变 (`sometimes == 0`) | 只影响排序 | `max_cluster`/`dup_seats` **不受影响** (它们是集合统计) → false, 但须在证据里点明"顺序不可复现, 任何按排位下的结论无效" |
| 成分变 (`sometimes > 0`) | 影响集合统计 | `JITTER_AFFECTS_STATS = true` → **Task 4 探针必须跑 N 次取交集/众数, 并报告每题的稳定性**; 层① 已发布的数字须重算 |

**无论结论如何**, 层① 证据里必须附一句可复现性声明, 说明数字是单次还是 N 次取样。

- [ ] **Step 7: Commit**

```bash
git add eval/jitter_probe.py scripts/tests/test_jitter_probe.py \
        evidence/checkpoints/topk_jitter.md evidence/checkpoints/topk_jitter.json
git commit -m "test(eval): top-k 抖动量化 — embedding 非确定性对同质簇尾部的影响"
```

---

### Task 4: 层① 挤占结构探针落库 (段②2a)

**Files:**
- Create: `eval/crowding_probe.py`
- Create: `scripts/tests/test_crowding_probe.py`

**Interfaces:**
- Produces: `eval.crowding_probe.crowding_stats(chunks) -> dict` — 返回 `{dup_seats, max_cluster, max_cluster_section, distinct_sections}`; CLI 产出 `evidence/checkpoints/crowding_layer1.json`

**为什么**: 探针**只描述结构, 不判定好坏**。好坏归层② (Task 6)。

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_crowding_probe.py`:

```python
"""层① 探针的统计口径。构造已知组成的假 chunk, 验统计正确 —— 探针自己也要被测。"""
from eval.crowding_probe import crowding_stats


class _C:
    def __init__(self, source, section):
        self.source, self.section = source, section


def test_no_duplicates():
    chunks = [_C(f"f{i}.md", f"s{i}") for i in range(5)]
    st = crowding_stats(chunks)
    assert st["dup_seats"] == 0
    assert st["max_cluster"] == 1
    assert st["distinct_sections"] == 5


def test_single_cluster():
    # 4 条同名 section (跨不同 source) + 1 条独立
    chunks = [_C(f"d{i}/spec.md", "DOMAIN") for i in range(4)] + [_C("x.md", "Other")]
    st = crowding_stats(chunks)
    assert st["max_cluster"] == 4
    assert st["max_cluster_section"] == "DOMAIN"
    assert st["dup_seats"] == 3          # 4 席里 3 席是多余的
    assert st["distinct_sections"] == 2


def test_two_clusters_dup_seats_sums_both():
    chunks = ([_C(f"a{i}.md", "A") for i in range(3)]
              + [_C(f"b{i}.md", "B") for i in range(2)])
    st = crowding_stats(chunks)
    assert st["max_cluster"] == 3
    assert st["dup_seats"] == 3          # (3-1) + (2-1)


def test_empty():
    st = crowding_stats([])
    assert st == {"dup_seats": 0, "max_cluster": 0,
                  "max_cluster_section": None, "distinct_sections": 0}


def test_same_section_same_source_still_counts():
    """同一文件的两个同名 section 也算簇 —— 挤占看的是席位, 不问来源。"""
    chunks = [_C("same.md", "S"), _C("same.md", "S")]
    assert crowding_stats(chunks)["max_cluster"] == 2
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_crowding_probe.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'eval.crowding_probe'`

- [ ] **Step 3: 实现探针**

新建 `eval/crowding_probe.py` —— 把 scratchpad 版本落库, 统计逻辑提为可测函数:

```python
"""层①: top-k 同质簇挤占的结构量化 (确定性, 零 LLM)。

同质簇 = top-k 里 section 名字面相同的多个条目。它们通常是模板化内容
(63 个域的同名变量行: DOMAIN / STUDYID / USUBJID / VISIT / EPOCH …),
正文逐字近似, 会对含该字面的问句齐刷刷高分, 占满 top-k。

**本探针只描述结构, 不判定好坏。** 挤占是否有害由层② 的 context A/B + judge 判定
(evidence/checkpoints/crowding_layer2.md) —— 用 gold 判据永远判不出来, 因为 S1
前置注入已经确定性地钉死了 gold recall。

已知限制: "同质"只按 section 名字面相同认定, 不含语义近似 (不同域的
`Related Domains` vs `Overview` 这类照不出来)。刻意的确定性取舍。
"""
from __future__ import annotations

import argparse
import json
from collections import Counter


def crowding_stats(chunks) -> dict:
    """top-k 组成的挤占统计。dup_seats = 同名 section 占用的**多余**席位总数。"""
    cnt = Counter(getattr(c, "section", None) for c in chunks)
    if not cnt:
        return {"dup_seats": 0, "max_cluster": 0,
                "max_cluster_section": None, "distinct_sections": 0}
    top_sec, top_n = cnt.most_common(1)[0]
    return {
        "dup_seats": sum(n - 1 for n in cnt.values() if n > 1),
        "max_cluster": top_n,
        "max_cluster_section": top_sec,
        "distinct_sections": len(cnt),
    }


def main(argv=None):
    p = argparse.ArgumentParser(description="层① 同质簇挤占结构探针")
    p.add_argument("test_set", nargs="?", default="eval/test_set_v3.yml")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--output", default="evidence/checkpoints/crowding_layer1.json")
    args = p.parse_args(argv)

    import yaml

    from server.config import settings
    from server.rag import RAGEngine

    rag = RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=args.top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
    )

    qs = yaml.safe_load(open(args.test_set))
    rows = []
    for i, q in enumerate(qs, 1):
        chunks = rag.retrieve(q["question"], top_k=args.top_k)
        st = crowding_stats(chunks)
        rows.append({
            "id": q["id"], "category": q["category"], "n": len(chunks), **st,
            "composition": [
                {"source": c.source, "section": c.section,
                 "sim": round(c.similarity, 4),
                 "via_lookup": bool(getattr(c, "via_lookup", False))}
                for c in chunks
            ],
        })
        print(f"[{i}/{len(qs)}] {q['id']} dup={st['dup_seats']} "
              f"max={st['max_cluster']}(§{st['max_cluster_section']})", flush=True)

    json.dump(rows, open(args.output, "w"), ensure_ascii=False, indent=1)

    n = len(rows)
    print(f"\n===== 层① 汇总 (题数 {n}, k={args.top_k}) =====")
    for thr in (3, 5, 8):
        m = sum(1 for r in rows if r["max_cluster"] >= thr)
        print(f"  最大同名 section 簇 >= {thr:2d} 席: {m:3d} 题 ({m / n * 100:.1f}%)")
    print(f"  平均 dup_seats: {sum(r['dup_seats'] for r in rows) / n:.2f} / {args.top_k}")
    print(f"  平均 distinct_sections: {sum(r['distinct_sections'] for r in rows) / n:.2f}")
    print("\n-- 挤占最重的 15 题:")
    for r in sorted(rows, key=lambda x: -x["max_cluster"])[:15]:
        print(f"  {r['id']:>6} {r['category']:<13} max={r['max_cluster']:2d} "
              f"§{r['max_cluster_section']}  dup={r['dup_seats']}")
    print(f"\n明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_crowding_probe.py -v`
Expected: 5 passed

- [ ] **Step 5: 跑落库版, 与 spec §0 数字核对**

Run: `.venv/bin/python -m eval.crowding_probe --output evidence/checkpoints/crowding_layer1.json`

Expected (spec §0 由 scratchpad 版跑出的值, 落库版应一致或仅因 Task 1/3 的 gold 改动而**完全不变** ——
gold 不参与本探针任何计算, 故**必须逐值相同**):

| 指标 | 期望 |
|---|---|
| max_cluster ≥3 | 40 题 (28.6%) |
| ≥5 | 11 题 (7.9%) |
| ≥8 | 3 题 (2.1%) |
| 平均 dup_seats | 1.73 |
| 平均 distinct_sections | 13.27 |
| 榜首 | q38 max=14 §DOMAIN |

**若有出入**: 说明落库时改变了口径, 必须查清并以落库版为准, 同时回头订正 spec §0 的数字
(硬规矩 2: 标"实测"的数字必须真的从那条附上的命令跑出来)。差异记入
`evidence/failures/` (规则 B)。

- [ ] **Step 6: Commit**

```bash
git add eval/crowding_probe.py scripts/tests/test_crowding_probe.py \
        evidence/checkpoints/crowding_layer1.json
git commit -m "test(eval): 层① 同质簇挤占结构探针落库 + 统计口径单测"
```

---

### Task 5: 池深度不变性验证 (段②2b 前置)

**Files:**
- Create: `evidence/checkpoints/pool_depth_invariance.md`

**Interfaces:**
- Produces: 一个二值结论 `POOL_DEEP_OK ∈ {true, false}`, 决定 Task 6 的 A/B 池策略。

**为什么**: `_hybrid_fuse(dense, bm25, k)` **已截到 k**, 而生产 `hybrid_pool=30`。
Task 6 的 B 组要"腾出席位由池中下一位补足到 15", 需要比 15 深的池。
若直接给 B 组加深池而 A 组不加, A/B 差异就混入了**池深度**这个额外变量 —— 实验作废。

RRF 分数 `Σ 1/(60+rank+1)` 只由 rank 决定, 加深池只加入分数更低的项。**但**一个 chunk 可能
在 dense 池外、bm25 池内, 加深 dense 池后它获得额外一项分数, 可能挤进 top-15。
**所以这是必须实测的经验问题, 不能靠推理断言。**

- [ ] **Step 1: 实测 A 组在 pool=30 vs pool=200 下的 top-15 是否逐位相同**

Run:
```bash
.venv/bin/python - <<'PY'
import json
from server.config import settings
from server.rag import RAGEngine
import yaml

rows = json.load(open("evidence/checkpoints/crowding_layer1.json"))
target = [r["id"] for r in sorted(rows, key=lambda x: -x["max_cluster"])[:11]]
if "q38" not in target:
    target.append("q38")
qs = {q["id"]: q for q in yaml.safe_load(open("eval/test_set_v3.yml"))}

def engine(pool):
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=15,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=pool,
    )

shallow, deep = engine(30), engine(200)
diff = []
for qid in target:
    q = qs[qid]["question"]
    a = [c.chunk_id for c in shallow.retrieve(q, top_k=15)]
    b = [c.chunk_id for c in deep.retrieve(q, top_k=15)]
    if a != b:
        diff.append((qid, sum(1 for x, y in zip(a, b) if x != y)))
print("题数", len(target))
print("POOL_DEEP_OK =", not diff)
print("差异题:", diff or "无")
PY
```

- [ ] **Step 2: 记录结论并据此定 Task 6 的池策略**

写 `evidence/checkpoints/pool_depth_invariance.md`, 含上面那条完整命令 + 原始输出。

- **若 `POOL_DEEP_OK = true`**: Task 6 三组统一用 `hybrid_pool=200`。B 组能补满 15 席,
  A 组与生产 top-15 逐位相同 —— 实验干净。
- **若 `POOL_DEEP_OK = false`**: Task 6 三组统一用生产 `hybrid_pool=30`, 且
  **B 组允许不足 15 席**。此时必须在证据里声明: "B 组 context 比 A 组短, 这是配额的
  真实效果, 但也意味着 A/B 差异含 context 长度这一混杂因素", 并记录每题 B 组实际席位数。

**不许**为了让实验好看而给 A/B 用不同池深。

- [ ] **Step 3: Commit**

```bash
git add evidence/checkpoints/pool_depth_invariance.md
git commit -m "test(eval): 池深度不变性实测 — 定 A/B 对照的池策略"
```

---

### Task 6: 层② context A/B1/B2 损害判定 (段②2b)

**Files:**
- Create: `server/diversity.py` (配额语义的**唯一**实现)
- Create: `eval/crowding_ab.py` (实验跑批)
- Create: `scripts/tests/test_crowding_ab.py`
- Create: `evidence/checkpoints/crowding_layer2.md`

**Interfaces:**
- Consumes: `eval.crowding_probe.crowding_stats`, `eval.run_eval.check_fact_recall_judge`, Task 5 的池策略
- Produces: `server.diversity.apply_section_cap(chunks, cap, exempt_lookup=True) -> list` — 供 Task 7 的生产代码复用同一份配额语义

**为什么配额函数放 `server/` 而不是 `eval/`**: Task 7 要让 `server/rag.py` 用它。
生产代码 import `eval/` 是层次倒置 (eval 依赖 server, 反向依赖会成环, 且把实验脚本
变成生产依赖)。故配额语义从一开始就落在 `server/diversity.py`, eval 侧 import 它 ——
而不是先写在 eval 里、Task 7 再搬家。

**为什么**: gold 判据对挤占结构性失明 (S1 钉死 recall), 必须换外部锚 = 答案正确性。

**Task 1 带来的口径修正 (必读)**: q38 在 **dense-only** 下补完 gold 得 0.5, 在**生产口径
(hybrid + S1)** 下仍是 **0.0** —— hybrid RRF 把 dense 排**第 1** 的 `ch04 §4.2.2` 挤出了 top-15。
故挤占的形态是"把已排第 1 的正确 chunk 挤掉", 比 spec 初稿描述的更严重。

**Task 1 提出的待验假设 (段② 应独立证伪, 不许当成已知事实引用)**:
> hybrid 的 BM25 侧在 `domain` / `code` 这类高频标识符词上, 召回被 63 个同构 chunk
> (每个域各一条 `§DOMAIN` 节) **摊平**, 于是 RRF 融合后同构簇整体上浮, 挤掉 dense 的头名。

验证方法: 对 q38 分别取 dense-only / BM25-only / hybrid 三路的 top-15,
看 `§DOMAIN` 簇在各路的席位数与排名。若 BM25-only 里该簇席位显著多于 dense-only,
假设成立。**结果无论正反都要写进 `crowding_layer2.md`** —— 若证伪, 说明挤占源在 dense 侧,
per-section 配额仍适用但归因描述要改。

**判定规则 (spec §2.2b, 先写死, 不许看到数据再改)**:

对每组 B 与 A 逐题比 judge 分: `improved` = B>A 的题数, `regressed` = B<A 的题数,
`净改善 = improved − regressed`。门槛 **净改善 ≥ 3 且 regressed ≤ 1**。

| 结果 | 结论 |
|---|---|
| B1、B2 均过门槛 | 有害 → Task 7 实施, N 取净改善更高者; 并列取 **N=2** |
| 仅 B2 过门槛 | **N=2** |
| 仅 B1 过门槛 | **N=1**, 证据里单列 B2 为何不够 |
| 均不过且 `regressed` 均 ≤1 | **挤占存在但无害 → 跳过 Task 7**, 探针留作常驻监控 |
| 任一组 `regressed ≥ 4` | 同质簇是有效信号 → 不修, 并在证据里**更正 spec 的假设** |

A/B 同分题计入分母但不计 improved/regressed。**若同分题 ≥ 8/12, 整个层② 判定作废** ——
锤子选错, 换锚重做, 不许顺着读结论。

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_crowding_ab.py`:

```python
"""配额语义: 同名 section 限 cap 席, 腾出的席位由池中下一位依次补足。"""
from server.diversity import apply_section_cap


class _C:
    def __init__(self, cid, section, via_lookup=False):
        self.chunk_id, self.section = cid, section
        self.source = f"src/{cid}.md"
        self.via_lookup = via_lookup


def test_cap_keeps_first_n_of_each_cluster():
    pool = [_C(i, "DOMAIN") for i in range(5)] + [_C(90 + i, "Other") for i in range(3)]
    out = apply_section_cap(pool, cap=2)
    assert [c.chunk_id for c in out] == [0, 1, 90, 91, 92]


def test_cap_preserves_relative_order():
    pool = [_C(0, "A"), _C(1, "B"), _C(2, "A"), _C(3, "A"), _C(4, "B")]
    out = apply_section_cap(pool, cap=1)
    assert [c.chunk_id for c in out] == [0, 1]


def test_lookup_chunks_exempt_from_cap():
    """S1 注入是确定性 gold, 不属被检验对象 —— 三组一律豁免。"""
    pool = [_C(0, "VISIT", via_lookup=True), _C(1, "VISIT", via_lookup=True),
            _C(2, "VISIT", via_lookup=True), _C(3, "VISIT"), _C(4, "VISIT"), _C(5, "X")]
    out = apply_section_cap(pool, cap=1)
    assert [c.chunk_id for c in out] == [0, 1, 2, 3, 5]


def test_cap_none_is_identity():
    pool = [_C(i, "A") for i in range(4)]
    assert [c.chunk_id for c in apply_section_cap(pool, cap=None)] == [0, 1, 2, 3]


def test_none_sections_are_not_clustered_together():
    """section=None 不是一个'簇名' —— 缺元数据不该被当成同质。"""
    pool = [_C(i, None) for i in range(4)]
    assert len(apply_section_cap(pool, cap=1)) == 4
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_crowding_ab.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'eval.crowding_ab'`

- [ ] **Step 3a: 实现配额 (生产侧)**

新建 `server/diversity.py`:

```python
"""检索结果多样性: per-section 配额。

治的是模板化同质簇 —— 63 个域的同名变量行 (DOMAIN / STUDYID / USUBJID / VISIT /
EPOCH …) 正文逐字近似, 对含该字面的问句齐刷刷高分, 会占满 top-k。
q38 实测: top-15 里 14 席是 §DOMAIN, 只剩 1 席给别的内容。

是否启用由证据决定, 见 evidence/checkpoints/crowding_layer2.md。
"""
from __future__ import annotations

from collections import Counter


def apply_section_cap(chunks, cap, exempt_lookup=True):
    """同名 section 最多保留 cap 席, 其余丢弃; 相对顺序不变。cap=None 为恒等。

    section=None 的条目不参与聚簇 (缺元数据不等于同质)。
    via_lookup=True 的条目在 exempt_lookup 下豁免且**不计入**簇计数 ——
    它们是 S1/S2 的确定性 gold 注入, 不属被检验对象。
    """
    if cap is None:
        return list(chunks)
    seen: Counter = Counter()
    out = []
    for c in chunks:
        if exempt_lookup and getattr(c, "via_lookup", False):
            out.append(c)
            continue
        sec = getattr(c, "section", None)
        if sec is None:
            out.append(c)
            continue
        if seen[sec] >= cap:
            continue
        seen[sec] += 1
        out.append(c)
    return out
```

- [ ] **Step 3b: 实现 A/B 跑批**

新建 `eval/crowding_ab.py`:

```python
"""层②: context A/B1/B2 对照 —— 判定同质簇挤占是否**有害**。

层① 只能证明挤占存在。它是否有害, 用 gold 判据永远判不出来: S1 前置注入
(_merge_lookup_first) 已经确定性地保证了 gold 恒在 top-k, 判据因而对
"剩余席位的质量"结构性失明。故本模块的锚是**答案正确性** (LLM judge),
它在 section 名这个代理量之外 (硬规矩 6)。

三组同池同序, 唯一差别是配额:
  A  = 无配额 (生产现状)
  B1 = 同名 section 限 1 席
  B2 = 同名 section 限 2 席
S1 注入的 chunk 三组一律豁免 (确定性 gold, 不属被检验对象)。
配额语义来自 server.diversity.apply_section_cap —— Task 7 的生产代码用同一份, 不重写。
"""
from __future__ import annotations

import argparse
import json

from server.diversity import apply_section_cap


def main(argv=None):
    p = argparse.ArgumentParser(description="层② context A/B1/B2 对照")
    p.add_argument("--layer1", default="evidence/checkpoints/crowding_layer1.json")
    p.add_argument("--test-set", default="eval/test_set_v3.yml")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--pool", type=int, required=True,
                   help="Task 5 定的池深 (POOL_DEEP_OK=true 用 200, 否则 30)")
    p.add_argument("--model", default=None, help="答题模型; 默认 settings.default_model")
    p.add_argument("--output", default="evidence/checkpoints/crowding_layer2.json")
    args = p.parse_args(argv)

    import litellm
    import yaml

    from eval.run_eval import DEFAULT_JUDGE_MODEL, check_fact_recall_judge
    from server.config import settings
    from server.rag import RAGEngine

    rows = json.load(open(args.layer1))
    target = [r["id"] for r in sorted(rows, key=lambda x: -x["max_cluster"])[:11]]
    if "q38" not in target:
        target.append("q38")
    qs = {q["id"]: q for q in yaml.safe_load(open(args.test_set))}
    model = args.model or settings.default_model

    rag = RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=args.top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=args.pool,
    )

    results = []
    for i, qid in enumerate(target, 1):
        q = qs[qid]
        # 一次检索, 三组共用 —— 保证同池同序, 唯一变量是配额
        pool_chunks = rag.retrieve(q["question"], top_k=max(args.pool, args.top_k))
        arms = {}
        for arm, cap in (("A", None), ("B1", 1), ("B2", 2)):
            capped = apply_section_cap(pool_chunks, cap)[: args.top_k]
            ctx = rag.format_context(capped)
            msgs = rag.build_messages(q["question"], ctx)
            resp = litellm.completion(model=model, messages=msgs, temperature=0.0)
            answer = resp.choices[0].message.content or ""
            judged = check_fact_recall_judge(
                q["question"], answer, q.get("expected_facts", []), DEFAULT_JUDGE_MODEL
            )
            arms[arm] = {
                "seats": len(capped),
                "score": judged[0] if judged else None,
                "judge_parse_ok": judged is not None,
                "answer": answer,
                "composition": [{"source": c.source, "section": c.section} for c in capped],
            }
            print(f"[{i}/{len(target)}] {qid} {arm}: seats={len(capped)} "
                  f"score={arms[arm]['score']}", flush=True)
        results.append({"id": qid, "question": q["question"], "arms": arms})

    json.dump(results, open(args.output, "w"), ensure_ascii=False, indent=1)

    print("\n===== 层② 判定 =====")
    n_unparsed = sum(1 for r in results for a in r["arms"].values() if not a["judge_parse_ok"])
    if n_unparsed:
        print(f"⚠ judge 未解析 {n_unparsed} 次 —— 这些臂的分数不可用, 逐条查明再判")
    ties = 0
    for arm in ("B1", "B2"):
        imp = reg = tie = 0
        for r in results:
            a, b = r["arms"]["A"]["score"], r["arms"][arm]["score"]
            if a is None or b is None:
                continue
            if b > a:
                imp += 1
            elif b < a:
                reg += 1
            else:
                tie += 1
        ties = max(ties, tie)
        net = imp - reg
        ok = net >= 3 and reg <= 1
        print(f"  {arm}: improved={imp} regressed={reg} tie={tie} 净改善={net} "
              f"-> {'过门槛' if ok else '不过门槛'}")
    print(f"\n同分题最多 {ties}/{len(results)}"
          + ("  ⚠ ≥8 -> 层② 判定作废, 换锚重做" if ties >= 8 else ""))
    print(f"明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_crowding_ab.py -v`
Expected: 5 passed

- [ ] **Step 5: 跑实验**

用 Task 5 定的池深 (下面按 `POOL_DEEP_OK=true` 写; false 则把 200 换成 30):

```bash
.venv/bin/python -m eval.crowding_ab --pool 200 \
  --output evidence/checkpoints/crowding_layer2.json
```

- [ ] **Step 6: 按写死的规则判定, 写证据**

写 `evidence/checkpoints/crowding_layer2.md`, **必须包含**:
- 完整可复跑命令 + 原始输出
- 三组逐题分数表
- 按上面的表得出的结论 (含 "不修" 这个可能)
- **已知限制**: n=12 且为按 `max_cluster` 选出的**极端样本, 不是随机样本**,
  结论只能推广到"重挤占题", 不能推广到全 140 题
- 若 Task 5 判 `POOL_DEEP_OK=false`: 补声明 B 组 context 更短这一混杂因素 + 每题实际席位数
- judge 未解析的次数 (若 >0, 逐条说明)

- [ ] **Step 7: Commit**

```bash
git add eval/crowding_ab.py scripts/tests/test_crowding_ab.py \
        evidence/checkpoints/crowding_layer2.json evidence/checkpoints/crowding_layer2.md
git commit -m "test(eval): 层② context A/B1/B2 —— 用答案质量作外部锚判定挤占是否有害"
```

---

### Task 7: 检索层 per-section 配额 (段②2c — **条件性**)

> **只在 Task 6 判定"有害"时执行。** 若判定为"不修", 跳过本 task,
> 在 `evidence/checkpoints/crowding_layer2.md` 记明"按写死规则跳过 Task 7", 直接进 Task 8。

**Files:**
- Modify: `server/rag.py` (`__init__` 加参数; `retrieve` 的 hybrid 分支)
- Modify: `eval/run_eval.py` (加 `--section-cap` 开关)
- Test: `scripts/tests/test_section_cap_retrieval.py` (新建)

**Interfaces:**
- Consumes: `server.diversity.apply_section_cap` (Task 6 —— **复用同一份配额语义, 不重写**)
- Produces: `RAGEngine(..., section_cap: int | None = None)`; 默认 `None` = 行为逐字节不变

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_section_cap_retrieval.py`:

```python
"""检索层 per-section 配额。默认 None = 关闭, 保证不改变任何现有行为。"""
from server.rag import RetrievedChunk


def _chunk(cid, section, source="kb/x.md"):
    return RetrievedChunk(chunk_id=cid, source=source, domain=None, file_type=None,
                          section=section, similarity=0.5, text="t")


def test_default_is_off(monkeypatch):
    from server.rag import RAGEngine
    assert "section_cap" in RAGEngine.__init__.__code__.co_varnames
    import inspect
    sig = inspect.signature(RAGEngine.__init__)
    assert sig.parameters["section_cap"].default is None


def test_cap_applied_between_fusion_and_lookup():
    """配额必须在 fusion 之后、S1 注入之前 —— S1 注入不受影响。"""
    from server.diversity import apply_section_cap
    pool = [_chunk(i, "DOMAIN") for i in range(5)] + [_chunk(90, "Other")]
    assert [c.chunk_id for c in apply_section_cap(pool, 2)] == [0, 1, 90]
```

补一条真引擎的集成测试 (标记为需要 chroma, 与既有测试同风格):

```python
def test_engine_with_cap_reduces_cluster(tmp_path):
    """真引擎: 开配额后 q38 的 §DOMAIN 席位应 <= cap。"""
    import pytest
    from server.config import settings
    from server.rag import RAGEngine
    from eval.crowding_probe import crowding_stats

    q = ("How are SDTM domain abbreviation codes assigned? "
         "What are the rules for the two-character domain code?")
    try:
        rag = RAGEngine(
            chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
            collection_name=settings.collection_name,
            embedding_model=settings.embedding_model, top_k=15,
            structured_lookup_enabled=True, hybrid_enabled=True,
            hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
            hybrid_pool=settings.hybrid_pool, section_cap=2,
        )
        chunks = rag.retrieve(q, top_k=15)
    except Exception as exc:  # 无索引/无 API key 的环境跳过, 与既有集成测试同策
        pytest.skip(f"needs live index: {exc}")
    st = crowding_stats(chunks)
    assert st["max_cluster"] <= 2, st
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_section_cap_retrieval.py -v`
Expected: FAIL — `RAGEngine.__init__` 无 `section_cap`

- [ ] **Step 3: 实现**

`server/rag.py` 顶部 import 区加:

```python
from server.diversity import apply_section_cap
```

`__init__` 参数列表末尾加 (紧跟 `prompt_guardrail_enabled` 之后):

```python
        section_cap: int | None = None,
```

并在 `__init__` 体内保存:

```python
        # per-section 配额: 同名 section 在 top-k 里最多占 N 席。None = 关闭 (默认)。
        # 治的是模板化同质簇 (63 个域的同名变量行) 占满 top-k 的问题 ——
        # 证据 evidence/checkpoints/crowding_layer2.md。配额语义与层② 实验共用
        # eval.crowding_ab.apply_section_cap, 不另写一份 (两份必漂移)。
        if section_cap is not None and section_cap < 1:
            raise ValueError(f"section_cap must be >= 1 or None, got {section_cap}")
        self.section_cap = section_cap
```

`retrieve` 的 hybrid 分支改为先拿深池再配额再截 k:

```python
        elif self.hybrid_enabled:
            pool = max(k, self.hybrid_pool)
            dense = self._search(query, pool, where, query_embedding=q_emb)
            bm25 = self._bm25_search(query, pool, where)
            if self.section_cap is None:
                cosine = self._hybrid_fuse(dense, bm25, k)
            else:
                # 先融合到池深再配额, 否则配额腾出的席位无处可补
                fused = self._hybrid_fuse(dense, bm25, pool)
                cosine = apply_section_cap(fused, self.section_cap)[:k]
```

`eval/run_eval.py` 加 CLI 开关 (放在 `--hybrid-pool` 附近):

```python
    parser.add_argument(
        "--section-cap",
        type=int,
        default=None,
        help="per-section 配额: 同名 section 在 top-k 里最多 N 席 (默认关闭)",
    )
```

并传给两处 `RAGEngine(...)` 构造 (主引擎 + 联邦的 study 引擎):

```python
        section_cap=args.section_cap,
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_section_cap_retrieval.py -v`
Expected: 3 passed (或含 1 skipped, 若无 live index)

- [ ] **Step 5: 全集零回归 + 效果**

关配额 (必须与 Task 3 Step 8 的结果**逐题 Δ0** —— 证明默认路径没被动过):

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output /tmp/cap_off.json
.venv/bin/python -c "
import json
a=json.load(open('evidence/checkpoints/gold_integrity_after.json'))
b=json.load(open('/tmp/cap_off.json'))
ra={x['id']:x['source_recall'] for x in (a if isinstance(a,list) else a['results'])}
rb={x['id']:x['source_recall'] for x in (b if isinstance(b,list) else b['results'])}
d=[k for k in ra if ra[k]!=rb.get(k)]
print('关配额逐题 Δ0' if not d else f'DIFF {d}')"
```

开配额 (N 取 Task 6 判定值):

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --section-cap <N> \
  --output evidence/checkpoints/section_cap_on.json
```

逐题对照两者, 列出升/降题目。**任何一题下降都必须逐题说明原因**, 不许只报平均分。

- [ ] **Step 6: 层② 复跑确认改善成立**

```bash
.venv/bin/python -m eval.crowding_ab --pool <Task5 池深> \
  --output evidence/checkpoints/crowding_layer2_recheck.json
```

- [ ] **Step 7: Commit**

```bash
git add server/rag.py eval/run_eval.py scripts/tests/test_section_cap_retrieval.py \
        evidence/checkpoints/section_cap_on.json \
        evidence/checkpoints/crowding_layer2_recheck.json
git commit -m "feat(rag): per-section 配额治同质簇挤占 (默认关, 证据见 layer2)"
```

---

### Task 8: chapters 切分策略 (段③)

**Files:**
- Modify: `scripts/chunkers/chapters.py`
- Modify: `scripts/tests/test_chapters.py` (**既有文件 —— 有两条测试会被本改动打破, 见 Step 2**)

**Interfaces:**
- Consumes: `scripts.chunkers.chapters.ChaptersChunker(kb_root).chunk(file_path) -> list[Chunk]`
  (**构造器需要 kb_root 参数**, 既有测试用 `KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"`)
- Produces: 行为改变 —— ch01/ch02/ch03 由 1 块变多块; `chunk_count` 从 4315 变化

**⚠ 既有测试冲突 (pre-flight 扫描发现)**: `scripts/tests/test_chapters.py` 现有两条测试
把"≤20KB → 整文件单块"这一档**锁死**了:

- `test_ch01_produces_1_chunk` — `assert len(ch01_chunks) == 1`
- `test_ch01_section_is_whole_file` — `assert ch01_chunks[0].section == "whole_file"`

本 task 取消该档, 这两条**必然失败**。改它们是正当的 (测试是策略的编码, 策略变了测试就该变),
但**必须显式改、写明理由, 并用新测试锁住新策略** —— 不许"看到红就删测试"。
`test_ch04_produces_47_chunks` / `test_ch08_produces_19_chunks` 等 L-4 锁**不许动**。

- [ ] **Step 1: 先记录现状 (改之前必须有基线)**

```bash
.venv/bin/python -c "
from pathlib import Path
from scripts.chunkers.chapters import ChaptersChunker
kb = Path('../knowledge_base').resolve()
ck = ChaptersChunker(kb)
for f in sorted((kb / 'chapters').glob('*.md')):
    n_h2 = sum(1 for line in f.read_text(encoding='utf-8').splitlines() if line.startswith('## '))
    print(f'{f.name:35s} {f.stat().st_size:7d} B  H2={n_h2:2d}  -> {len(ck.chunk(f)):3d} chunks')"
```
Expected (2026-08-07 实测): ch01 11070 B H2=5 →1 · ch02 18141 B H2=9 →1 · ch03 19708 B H2=3 →1 ·
ch04 130532 B →47 · ch08 51764 B →19 · ch10 30233 B →多

把输出贴进 `evidence/checkpoints/chapters_chunking.md` 作为 before。

- [ ] **Step 2: 改既有的两条 ch01 测试 + 写新测试**

在 `scripts/tests/test_chapters.py` 中, 把这两条**替换**掉 (它们锁的是被取消的那一档):

```python
def test_ch01_produces_1_chunk(ch01_chunks):
    """ch01 (11KB ≤ 20KB) produces exactly 1 chunk (whole_file tier)."""
    assert len(ch01_chunks) == 1


def test_ch01_section_is_whole_file(ch01_chunks):
    """ch01 single chunk has section == 'whole_file'."""
    assert ch01_chunks[0].section == "whole_file"
```

替换为:

```python
def test_ch01_splits_by_h2(ch01_chunks):
    """2026-08-07: "≤20KB → 整文件单块" 这一档取消, ch01 (11KB, 5 个 H2) 按 H2 切。

    原策略把 ch01/ch02/ch03 各压成 1 个 chunk, 整章共用一个向量 -> 语义稀释。
    q38 诊断实测: ch02 的 whole_file 块在 dense 检索排 #71 (sim 0.5613), 而回答
    同一问题的 ch04 §4.2.2 是 #1 (sim 0.6970) —— 后者是被 H3 切出来的小节。
    证据 evidence/checkpoints/chapters_chunking.md。
    """
    assert len(ch01_chunks) == 5
    assert all(c.section != "whole_file" for c in ch01_chunks)


def test_ch01_sections_carry_real_headings(ch01_chunks):
    secs = [c.section for c in ch01_chunks]
    assert any("1.1" in (s or "") for s in secs), secs
    assert any("1.5" in (s or "") for s in secs), secs
```

并追加新测试:

```python
def test_ch02_splits_by_h2(chunker):
    """ch02 (18KB, 9 个 H2) —— q38 的 gold 章节, 原为整文件单块。"""
    chunks = chunker.chunk(CHAPTERS_DIR / "ch02_fundamentals.md")
    assert len(chunks) == 9
    assert all(c.section != "whole_file" for c in chunks)
    # §2.6 Creating a New Domain 含 "Determine the domain code" —— q38 要的那一半
    assert any("2.6" in (c.section or "") for c in chunks), [c.section for c in chunks]


def test_ch03_splits_by_h2(chunker):
    chunks = chunker.chunk(CHAPTERS_DIR / "ch03_submitting_data.md")
    assert len(chunks) == 3
    assert all(c.section != "whole_file" for c in chunks)


def test_file_without_headings_still_falls_back_to_whole_file(chunker, tmp_path):
    """无 H2 时仍回落整文件单块 —— 该回落分支是原整块档取消后的唯一兜底。"""
    f = tmp_path / "ch99_noheading.md"
    f.write_text("plain text with no markdown headings at all\n" * 20, encoding="utf-8")
    chunks = chunker.chunk(f)
    assert len(chunks) == 1
    assert chunks[0].section == "whole_file"


def test_large_chapter_still_splits_by_h3(ch04_chunks):
    """L-4 锁不得被本次改动破坏: >50KB 仍按 ### 切。"""
    assert len(ch04_chunks) == 47
    assert any("4.2.2" in (c.section or "") for c in ch04_chunks)
```

**若 ch01/ch02/ch03 的实际块数与 5/9/3 不符** (例如首个 H2 之前的前言另成一块),
以 Step 1 基线命令重跑出的真实值为准并订正断言 —— **但必须在证据里写明实际值与原因**,
不许把断言改成 `> 1` 了事 (那就失去了锁的意义)。

- [ ] **Step 3: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_chapters.py -v`
Expected: `test_ch01_splits_by_h2` / `test_ch01_sections_carry_real_headings` /
`test_ch02_splits_by_h2` / `test_ch03_splits_by_h2` 全 FAIL (当前都是 1 块);
L-4 那几条 (ch04 47 / ch08 19) 仍 PASS

- [ ] **Step 4: 改 chunker**

`scripts/chunkers/chapters.py` 的 `chunk` 方法, 把三档改为两档 + 回落:

```python
        if size_bytes > 50 * 1024:
            level = 3  # ★ L-4 lock: >50KB MUST split by ### (ch04 case)
        else:
            level = 2
```

并删掉 `size_bytes <= 20 * 1024` 那个提前 return 的整块分支 (下方"无该级标题 → 回落整文件"
的分支**保留不动**, 它现在承担了原整块档的职责)。

同步更新模块 docstring 的策略描述:

```
L-4 (locked by 1A.0.c HIGH): chapters/ ≥ 50KB 强制 `^### ` 切 (ch04 §4.4 alone = 9598
cl100k tokens > 8191 embedding limit). Two-tier size policy:
  - size_bytes > 50KB → split by `^### ` (H3)
  - otherwise         → split by `^## ` (H2); 无 H2 时回落整文件单块

2026-08-07: 原第三档 "≤20KB → 整文件单块" 取消。ch01/ch02/ch03 落在该档,
18KB 的 ch02 整块被稀释 (q38 诊断: ch02 whole_file dense #71 sim 0.5613,
而回答同一问题的 ch04 §4.2.2 是 #1 sim 0.6970)。
证据 evidence/checkpoints/chapters_chunking.md。
```

- [ ] **Step 5: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_chapters.py -v`
Expected: 全 passed (含未动的 L-4 锁 ch04=47 / ch08=19)

- [ ] **Step 6: 重灌索引**

```bash
.venv/bin/python -m scripts.ingest 2>&1 | tail -20
curl -s localhost:8000/api/info | .venv/bin/python -m json.tool | head -20
```

记录新的 `chunk_count` (原 4315)。**`index_fresh` 必须为 true。**
服务若在跑, 需按 `deploy/README.md` 重启使其加载新索引。

- [ ] **Step 7: 全集零回归 + 层① 复跑**

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output evidence/checkpoints/chapters_split_after.json
.venv/bin/python -m eval.crowding_probe --output evidence/checkpoints/crowding_layer1_after_split.json
```

逐题对照切分前后。**层① 复跑的目的**: 确认切分没制造**新的**同质簇 ——
ch02 切成 8 块后 `§whole_file` 这个簇头会消失, 但要确认没换成别的簇头。

- [ ] **Step 8: 跑完整测试套 + 索引断言同步**

```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml >/dev/null 2>&1
.venv/bin/python -c "import xml.etree.ElementTree as ET;a=ET.parse('/tmp/j.xml').getroot().find('testsuite').attrib;print(a)"
.venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -q
```

全库搜 `4315` 这个数字, 凡断言/文档引用的都要同步:

```bash
grep -rn "4315" --include=*.py --include=*.md . | grep -v evidence/failures
```

- [ ] **Step 9: Commit**

```bash
git add scripts/chunkers/chapters.py scripts/tests/test_chunkers_chapters.py \
        evidence/checkpoints/chapters_chunking.md \
        evidence/checkpoints/chapters_split_after.json \
        evidence/checkpoints/crowding_layer1_after_split.json
git commit -m "feat(kb): chapters 取消整文件单块档 — ch01/02/03 按 H2 切 + 重灌索引"
```

---

### Task 9: 收口 — 证据、规则 A 抽检、索引三件套、retro

**Files:**
- Create: `evidence/checkpoints/crowding_and_gold_integrity.md` (总收口)
- Create: `docs/superpowers/2026-08-07-crowding-gold-RETROSPECTIVE.md`
- Modify: `docs/PROGRESS.md`, `.work/meta/worklog/phase_07_rag_kg.md`, `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`

- [ ] **Step 1: 规则 A 语义抽检 (独立 agent, 第三个 subagent_type)**

抽样总体 = **本轮实际变更集合**: 改动的 gold 条目 + 改动的检索行为 + 切分改动的三个 chapters 文件。
**不是变更后全集** (规则 A / kickoff §3.5)。

N 写死为 **8**, 由**第三个** `subagent_type` (既非改 gold 方, 亦非实施方) 独立核验:
- 改的每条 gold: 该源正文是否真的字面回答题干那一问 (给行号)
- 开配额后升/降的题: 逐题看 context 组成变化是否解释得通
- 切分后的 chapters chunk: 抽 3 块看有没有把一个语义单元切断

结果落 `evidence/step_09_audit.md`。**Writer 说 PASS + Reviewer 说 PASS ≠ 业务 PASS。**

- [ ] **Step 2: 写总收口证据**

`evidence/checkpoints/crowding_and_gold_integrity.md` 必须含:
- 每个结论的**可复跑命令 + 该命令的原始输出** (硬规矩 2)
- 三段各自的前后数字, 每个数字**带口径**
- **口径断裂声明**: gold 改动后 CDISC 分数与历史 98.93% (section 级) 不可比
- 已知限制全表 (层② n=12 极端样本 / 层① 只认 section 名字面 / CDISC 尺子剩余寿命有限 / q126 未动)
- 若 Task 7 被跳过: 明确写"按写死规则判定挤占无害, 跳过检索层改动"

- [ ] **Step 3: 写 retro (规则 C)**

`docs/superpowers/2026-08-07-crowding-gold-RETROSPECTIVE.md`, 至少三段:
保留下来的做法 / 必须补上的缺口 / 关键决策复盘。

**本轮必须点名的事** (不许粉饰):
- kickoff §2.A 写的 q38 根因是**错的**, 且它是上一轮收口时写下的 —— 根因写进 kickoff 前没做诊断验证
- "S1 前置注入使 gold 判据对剩余席位结构性失明" 是硬规矩 6 的**新变体**:
  参照物不仅不能来自生成器内部, 也不能被系统的另一个组件确定性保证
- CDISC 140 题尺子已接近饱和 (修完只剩 q126), 长期需要新题源

- [ ] **Step 4: 更新 kickoff + 索引三件套**

- `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`: §2.A 标 DONE 并**订正根因描述**
  (原文"整文件单块导致语义稀释"是错的, 要写明推翻它的证据); §3 追加本轮新立的硬规矩;
  §1 基线表加新口径行 (带"含 gold 完整性修复后"标注)
- `.work/meta/worklog/phase_07_rag_kg.md`: append 本 session 工作记录
- `docs/PROGRESS.md`: 更新 Phase 7 行 + milestone 列表
- `CLAUDE.md` Key Paths: 仅当新增 key path 才加行 (≤80 字符)

- [ ] **Step 5: 红线程序化复扫**

本轮不碰 study 库, 但仍按硬规矩 3 程序化复扫待提交文件:

```bash
git diff --cached --name-only | while read f; do
  [ -f "$f" ] && .venv/bin/python -c "
import json,sys
cat=json.load(open('data/study/st01/catalog.json'))
names=set()
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in ('form_oid','field_oid','label','alias','question'): names.add(str(v))
            walk(v)
    elif isinstance(o,list):
        for x in o: walk(x)
walk(cat)
txt=open('$f',encoding='utf-8',errors='ignore').read()
hit=[n for n in names if n and len(n)>3 and n in txt]
if hit: print('RED LINE in $f:',hit[:5]); sys.exit(1)
" || echo "CHECK FAILED: $f"
done
```

**不许用"我觉得这个不算"豁免。**

- [ ] **Step 6: 最终全绿确认 + commit + push**

```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml >/dev/null 2>&1
.venv/bin/python -c "import xml.etree.ElementTree as ET;a=ET.parse('/tmp/j.xml').getroot().find('testsuite').attrib;print(a)"
.venv/bin/python -m eval.lint_gold data/study/st01/eval/test_set_study_v2.yml --catalog data/study/st01/catalog.json
.venv/bin/python data/study/st01/eval/audit_v2.py
curl -s localhost:8000/api/info
```

全绿后单次 commit + push to main。

---

## Self-Review

**Spec 覆盖**: 段①1a→Task 1 · 段①1b→Task 2+3 · 段②2a→Task 4 · 段②2b→Task 5+6 ·
段②2c→Task 7 (条件性) · 段③→Task 8 · 硬规矩/已知限制/规则 A-D→Task 9。
spec §5 "不在本轮范围"的四项在本 plan 中无任务, 符合预期。

**类型一致性**: `source_matches` (Task 2 定义) 被 Task 3 消费, 签名一致;
`apply_section_cap` (Task 6 定义) 被 Task 7 复用, 签名一致 (`chunks, cap, exempt_lookup`);
`crowding_stats` (Task 4 定义) 被 Task 7 的集成测试消费, 返回键一致。

**条件性依赖**: Task 7 是本 plan 唯一条件性任务, 其跳过条件在 Task 6 判定表里写死。
Task 8 不依赖 Task 7 的产出, 故跳过 Task 7 不影响后续。
