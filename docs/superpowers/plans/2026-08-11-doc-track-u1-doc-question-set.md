# doc 轨 U1 — doc 侧 gold 题集与判据 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 `study_st01_docs` 的 114 个 doc chunk 造一把有判别力的检索尺子 —— 30 道计分题 + 四道程序化入池闸 + 一个可复现的 doc-only 上界基线 —— 使 U2 接线后能说出"好了没有"。

**Architecture:** gold 用 chunk 文件名, 判据逐字复用现有 `check_source_recall` (零改动)。四道闸做成一个确定性零 LLM 的模块 `eval/docs_gold_gates.py`, gold 唯一性委托给已有的 `eval/lint_gold.py` (**唯一实现, 不许有第二份**)。题集与笔记落在 `data/study/st01/eval/` (gitignored), 进 git 的只有闸代码、单测与收口证据。

**Tech Stack:** Python 3.13 · pytest · PyYAML · chromadb (只读) · poppler `pdftotext` (只在出题时读原页)

**依据 spec:** `docs/superpowers/specs/2026-08-11-doc-track-u1-doc-question-set-design.md` (2026-08-11 用户定稿)

## Global Constraints

- **数据红线**: 进 git 的一切内容**零真名零正文**。题集 / 锚串 / 笔记只许落在 `sdtm-rag/data/study/` 下 (该目录在 `.gitignore:10`)。研究一律代号 `st01`。
- **判据唯一实现**: gold 匹配语义只许有 `eval/run_eval.py: source_matches` 一份。任何闸都必须调用它或调用 `eval/lint_gold.py` —— **不许照着再写一遍** (2026-08-06 的 8 条假阳性就是这么来的)。
- **OR 组一题都不用**: `expected_sources_any` 结构上不进 lint, 用了等于把该题移出闸外。跨节聚合题一律用 AND。
- **自毁阈值不得修改**: doc-only 上界 ≥95% 或 ≤40% → 题集退回重写; 闸 D 筛掉 >50% → 当场停下报告用户。**触发时不许改阈值, 不许改判定规则。**
- **来源隔离**: 出题只读 `pdftotext` 逐页原文, **不读 `data/study/st01/docs/` 下的 chunk 产物**。定 gold 与锚串时才读 chunk。此闸机器查不了 —— 由执行者在 NOTES 里逐批声明, 并接受抽检方质询。
- **不碰的东西**: `test_set_study_v2.yml` (87.50% 必须逐题可比) · 生产检索配置 · `scripts/study/` 下的切分器 · 任何接线代码。
- **失败归档不删** (规则 B): 被闸打回的题归档到 `data/study/st01/eval/failures/` 而不是删除。
- 每个 task 结束跑 `.venv/bin/python -m pytest -p no:warnings -q`, 必须 **0 failed**。开工基线 **1036 passed**。

---

## File Structure

| 文件 | 责任 | 进 git |
|---|---|---|
| `sdtm-rag/eval/lint_gold.py` (改) | gold 唯一性 —— 增加 docs 侧全集来源, 逻辑不动 | 是 |
| `sdtm-rag/eval/docs_gold_gates.py` (新) | doc 侧四道入池闸 + CLI | 是 |
| `sdtm-rag/scripts/tests/test_docs_gold_gates.py` (新) | 四闸单测 + 变异测试 | 是 |
| `sdtm-rag/scripts/tests/test_lint_gold.py` (改) | docs 侧全集来源的测试 | 是 |
| `sdtm-rag/data/study/st01/eval/test_set_docs_v1.yml` (新) | 30 计分题 + L1 池 | **否** |
| `sdtm-rag/data/study/st01/eval/DOCS_V1_NOTES.md` (新) | 出题依据 / 逐题笔记 / 来源隔离声明 | **否** |
| `sdtm-rag/data/study/st01/eval/failures/` (新) | 被闸打回的题 (规则 B) | **否** |
| `sdtm-rag/evidence/checkpoints/doc_track_u1_question_set.md` (新) | 收口证据 | 是 |

---

## 题集 schema (Task 5 起使用)

`load_test_set` 要求顶层是 list, 且拒绝任何 `expected*` 未知键; 其他键自由。

```yaml
# schema 示例 —— 值为合成占位, 真题在本地 yml 里, 不进 git
- id: docs_v1_q01
  category: single_section       # single_section | cross_section | part_family | table
                                 # 用 `category` 而非自造键: run_eval 会免费给出
                                 # summary.source_recall_by_category, 即分型基线
  question: "……"                 # 日文自然问法, CRC/DM 口吻
  expected_sources: ["st01__doc01__s10_1.md"]
  expected_facts: ["12 文字以上の事実文字列", "OID 類は短くてよい"]
  anchor: "……20 文字以上の逐字アンカー……"   # 闸 B 的扫描串
  card_probe_terms: ["用語A", "用語B"]        # 闸 D: 人会拿去卡片上找答案的词, ≥2 个
  chapter: 10                    # 覆盖统计用
  note: "……"                     # 纯文档字段, 打分器不读
```

L1 池的题追加 `known_gap: true` 且 **不写 `expected_sources`** —— 但 `load_test_set` 会因"无非空 gold"报错, 故 L1 池**单独存一个文件** `test_set_docs_v1_l1pool.yml`, 不进任何评分命令, 只由闸脚本统计条数。

---

### Task 1: `lint_gold` 支持 docs 侧 gold 全集

**Files:**
- Modify: `sdtm-rag/eval/lint_gold.py:52-68` (`_load`), `:105-118` (`main`)
- Test: `sdtm-rag/scripts/tests/test_lint_gold.py`

**Interfaces:**
- Consumes: 无 (第一个 task)
- Produces: `lint_gold.lint_gold(test_set_path, catalog_path=None, max_matches=1, *, docs_dir=None) -> list[Finding]`;`lint_gold.doc_chunk_names(docs_dir: Path) -> list[str]`

- [ ] **Step 1: 写失败测试**

在 `scripts/tests/test_lint_gold.py` 末尾追加:

```python
def test_doc_chunk_names_returns_filenames_with_md(tmp_path):
    from eval.lint_gold import doc_chunk_names
    d = tmp_path / "docs"
    d.mkdir()
    (d / "st01__doc01__s10_1.md").write_text("x", encoding="utf-8")
    (d / "st01__doc01__s10_10.md").write_text("x", encoding="utf-8")
    assert doc_chunk_names(d) == ["st01__doc01__s10_1.md", "st01__doc01__s10_10.md"]


def test_doc_chunk_names_refuses_empty_dir(tmp_path):
    from eval.lint_gold import doc_chunk_names
    d = tmp_path / "docs"
    d.mkdir()
    with pytest.raises(ValueError, match="空全集"):
        doc_chunk_names(d)


def test_lint_gold_against_docs_dir(tmp_path):
    """docs 侧 gold 唯一性走同一份 lint 逻辑。"""
    from eval.lint_gold import lint_gold
    d = tmp_path / "docs"
    d.mkdir()
    for n in ("st01__doc01__s10_1.md", "st01__doc01__s10_10.md"):
        (d / n).write_text("x", encoding="utf-8")
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        "  expected_sources: ['st01__doc01__s10_1.md']\n"
        "- id: q2\n"
        "  expected_sources: ['st01__doc01__s10_1']\n",   # 不带 .md → 匹配 2 个
        encoding="utf-8",
    )
    findings = lint_gold(str(ts), docs_dir=d)
    assert [f.qid for f in findings] == ["q2"]
    assert findings[0].n_matches == 2


def test_lint_gold_requires_exactly_one_name_source(tmp_path):
    from eval.lint_gold import lint_gold
    ts = tmp_path / "ts.yml"
    ts.write_text("- id: q1\n  expected_sources: ['a.md']\n", encoding="utf-8")
    with pytest.raises(ValueError, match="catalog 与 docs-dir"):
        lint_gold(str(ts))
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_lint_gold.py -q -p no:warnings`
Expected: FAIL — `ImportError: cannot import name 'doc_chunk_names'`

- [ ] **Step 3: 实现**

在 `eval/lint_gold.py` 里, `_card_names` 之后加:

```python
def doc_chunk_names(docs_dir: Path | str) -> list[str]:
    """doc 侧 gold 全集 = docs/ 下的文件名 (带 `.md`)。

    与 retrieval 返回的 `source` 元数据逐字一致 (ingest_study 写的就是 `p.name`),
    所以这里和 catalog 侧一样, `.md` 参与匹配且有判别力。

    空目录必须响亮失败: 名字全集为空时"匹配数 != 1"对每条 gold 恒成立, 闸会
    全红看似严格; 但若将来有人把 0 匹配当成"跳过", 就变成恒绿。宁可现在炸。
    """
    names = sorted(p.name for p in Path(docs_dir).glob("*.md"))
    if not names:
        raise ValueError(f"docs_dir 无 md 文件, 空全集不可用作 gold 全集: {docs_dir}")
    return names
```

把 `_load` 改成:

```python
def _load(test_set_path, catalog_path=None, docs_dir=None) -> tuple[list[dict], list[str]]:
    if (catalog_path is None) == (docs_dir is None):
        raise ValueError("catalog 与 docs-dir 必须且只能给一个 —— 两个 gold 全集不可混用")
    if catalog_path is not None:
        names = _card_names(json.loads(Path(catalog_path).read_text(encoding="utf-8")))
    else:
        names = doc_chunk_names(docs_dir)
    data = yaml.safe_load(Path(test_set_path).read_text(encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data
    return [q for q in qs if not q.get("out_of_scope")], names
```

`lint_gold` / `or_groups` 的签名各加一个 keyword-only 参数并透传:

```python
def lint_gold(test_set_path, catalog_path=None, max_matches: int = 1, *, docs_dir=None) -> list[Finding]:
    qs, names = _load(test_set_path, catalog_path, docs_dir)
    ...   # 循环体一行不动


def or_groups(test_set_path, catalog_path=None, *, docs_dir=None) -> list[tuple[str, list[int]]]:
    qs, names = _load(test_set_path, catalog_path, docs_dir)
    ...   # 其余不动
```

`main` 里把 `--catalog required=True` 改成互斥组:

```python
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--catalog", help="card 侧 gold 全集来源")
    src.add_argument("--docs-dir", help="doc 侧 gold 全集来源 (章节 chunk 目录)")
```
并把两处调用改为 `lint_gold(args.test_set, args.catalog, args.max_matches, docs_dir=args.docs_dir)` / `or_groups(args.test_set, args.catalog, docs_dir=args.docs_dir)`。

在 `eval/lint_gold.py` 顶部确保 `from pathlib import Path` 已存在 (原文件已有)。

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_lint_gold.py -q -p no:warnings`
Expected: PASS (含原有全部用例 —— 卡片侧行为必须一字不变)

- [ ] **Step 5: 回归 + 提交**

```bash
.venv/bin/python -m pytest -p no:warnings -q
git add eval/lint_gold.py scripts/tests/test_lint_gold.py
git commit -m "feat(eval): lint_gold 支持 doc chunk 侧 gold 全集"
```

---

### Task 2: 闸 A (gold 唯一性) 与闸 B (锚串唯一性)

**Files:**
- Create: `sdtm-rag/eval/docs_gold_gates.py`
- Test: `sdtm-rag/scripts/tests/test_docs_gold_gates.py`

**Interfaces:**
- Consumes: `lint_gold.lint_gold(..., docs_dir=...)`, `lint_gold.doc_chunk_names`
- Produces:
  - `GateFinding(gate: str, qid: str, detail: str)` (frozen dataclass)
  - `ANCHOR_MIN_LEN = 20`
  - `chunk_bodies(docs_dir) -> dict[str, str]`
  - `gate_gold_unique(test_set_path, docs_dir) -> list[GateFinding]`
  - `gate_anchor_unique(questions, bodies) -> list[GateFinding]`

- [ ] **Step 1: 写失败测试**

新建 `scripts/tests/test_docs_gold_gates.py`:

```python
"""doc 侧四闸单测。

反装饰保证 (硬规矩 18) 的结构: **每道闸都有一对测试** —— 干净 fixture 必须返回 []
(`*_passes_*` / `*_accepts_*`), 脏 fixture 必须返回 finding (`*_flags_*`)。
后者就是"闸恒返回 [] 则变红"的断言, 不需要再写一条同义的 `test_mutation_*`
—— 那只是同一断言的复制。cap_recall 那轮 `hidden_loss_shadow` 之所以是装饰品,
正是因为当时**缺**脏 fixture 测试, 不是因为缺一个叫 mutation 的测试。

物理变异测试 (把闸函数改成 `return []` 跑全套) 由 Task 9 Step 2 第 3 条的
独立抽检方执行 —— 那是实现方自己做不了的独立性检查。
"""
import pytest

from eval.docs_gold_gates import (
    ANCHOR_MIN_LEN,
    chunk_bodies,
    gate_anchor_unique,
    gate_gold_unique,
)

FM = "---\nstudy: st01\nsection_number: '10.1'\n---\n"


def _docs(tmp_path, bodies: dict[str, str]):
    d = tmp_path / "docs"
    d.mkdir()
    for name, body in bodies.items():
        (d / name).write_text(FM + body, encoding="utf-8")
    return d


def test_chunk_bodies_strips_frontmatter(tmp_path):
    d = _docs(tmp_path, {"st01__doc01__s1_1.md": "BODY-TEXT\n"})
    assert chunk_bodies(d) == {"st01__doc01__s1_1.md": "BODY-TEXT\n"}


def test_gate_gold_unique_flags_multi_match(tmp_path):
    d = _docs(tmp_path, {"st01__doc01__s1_1.md": "a", "st01__doc01__s1_10.md": "b"})
    ts = tmp_path / "ts.yml"
    ts.write_text("- id: q1\n  expected_sources: ['st01__doc01__s1_1']\n", encoding="utf-8")
    f = gate_gold_unique(str(ts), d)
    assert [x.qid for x in f] == ["q1"]
    assert f[0].gate == "gold_unique"


def test_gate_anchor_unique_passes_when_count_equals_gold_count(tmp_path):
    anchor = "X" * ANCHOR_MIN_LEN
    bodies = {"st01__doc01__s1_1.md": anchor, "st01__doc01__s1_2.md": "other"}
    qs = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"], "anchor": anchor}]
    assert gate_anchor_unique(qs, bodies) == []


def test_gate_anchor_unique_flags_when_anchor_appears_in_extra_chunk(tmp_path):
    anchor = "X" * ANCHOR_MIN_LEN
    bodies = {"st01__doc01__s1_1.md": anchor, "st01__doc01__s1_2.md": anchor}
    qs = [{"id": "q1", "expected_sources": ["st01__doc01__s1_1.md"], "anchor": anchor}]
    f = gate_anchor_unique(qs, bodies)
    assert [x.qid for x in f] == ["q1"]
    assert "2 != 1" in f[0].detail


def test_gate_anchor_unique_flags_short_anchor():
    anchor = "X" * (ANCHOR_MIN_LEN - 1)
    qs = [{"id": "q1", "expected_sources": ["a.md"], "anchor": anchor}]
    f = gate_anchor_unique(qs, {"a.md": anchor})
    assert [x.gate for x in f] == ["anchor_unique"]
    assert "短すぎ" in f[0].detail or "过短" in f[0].detail


def test_gate_anchor_unique_flags_missing_anchor():
    qs = [{"id": "q1", "expected_sources": ["a.md"]}]
    f = gate_anchor_unique(qs, {"a.md": "body"})
    assert [x.qid for x in f] == ["q1"]


def test_gate_anchor_unique_counts_multi_gold(tmp_path):
    """跨节题: gold 2 个, 锚串必须正好出现 2 次。"""
    anchor = "Y" * ANCHOR_MIN_LEN
    bodies = {"a.md": anchor, "b.md": anchor, "c.md": "z"}
    qs = [{"id": "q1", "expected_sources": ["a.md", "b.md"], "anchor": anchor}]
    assert gate_anchor_unique(qs, bodies) == []

```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_docs_gold_gates.py -q -p no:warnings`
Expected: FAIL — `ModuleNotFoundError: No module named 'eval.docs_gold_gates'`

- [ ] **Step 3: 实现**

新建 `eval/docs_gold_gates.py`:

```python
"""doc 侧题集的入池闸 —— 全部确定性, 零 LLM。

存在的理由: doc chunk 接线前必须先有尺子, 而"尺子本身是否有判别力"必须也是可执行的,
不能靠出题人自述。四道闸对应 spec §4:

  A gold_unique    gold 在 114 个 chunk 名里唯一定位 (委托 eval.lint_gold, 唯一实现)
  B anchor_unique  答案锚串在全集出现次数 == gold 数
  C fact_length    每条 expected_facts 够长 (1-2 词碎片会让 fact-recall 顶格失明)
  D card_unanswerable  没有任何一张 field card 同时含全部 card_probe_terms

**闸 B 的口径边界 (硬规矩 19, 引用绿灯时必须同时写)**: 锚串唯一 != 语义唯一。
别的 chunk 可能换措辞表达同一事实, 本闸看不见。它只挡字面。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from eval.lint_gold import doc_chunk_names, lint_gold

ANCHOR_MIN_LEN = 20
_FM_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


@dataclass(frozen=True)
class GateFinding:
    gate: str
    qid: str
    detail: str


def chunk_bodies(docs_dir: Path | str) -> dict[str, str]:
    """文件名 → 正文 (剥掉 frontmatter)。

    剥 frontmatter 而不是整文件扫: frontmatter 里只有编号/页码, 让它参与锚串计数
    只会制造与内容无关的假命中。用锚定正则一次性剥, 不用 `split('---')`
    —— C1 复核时正是那个写法多留了换行, 把 66,200 算成 66,086。
    """
    out: dict[str, str] = {}
    for name in doc_chunk_names(docs_dir):
        text = (Path(docs_dir) / name).read_text(encoding="utf-8")
        out[name] = _FM_RE.sub("", text, count=1)
    return out


# ⚠ 本函数已于 Task 2 fix round 1 移入 `eval/lint_gold.py` 并提为公开函数 ——
# 它与 `lint_gold._load` 的题集口径原本三行逐字相同, 两道闸将来会判不同题集且不报错。
# 下游一律 `from eval.lint_gold import load_questions`, 不要在本文件重新定义。


def gate_gold_unique(test_set_path: Path | str, docs_dir: Path | str) -> list[GateFinding]:
    return [
        GateFinding("gold_unique", f.qid,
                    f"[{f.side}] {f.gold!r} 匹配 {f.n_matches} 个 chunk — 期望唯一定位")
        for f in lint_gold(str(test_set_path), docs_dir=docs_dir)
    ]


def gate_anchor_unique(questions: list[dict], bodies: dict[str, str]) -> list[GateFinding]:
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        anchor = q.get("anchor")
        n_gold = len(q.get("expected_sources") or [])
        if not anchor:
            findings.append(GateFinding("anchor_unique", qid, "缺 anchor 字段"))
            continue
        if len(anchor) < ANCHOR_MIN_LEN:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"anchor 过短 {len(anchor)} < {ANCHOR_MIN_LEN} — 短串会碰巧命中"))
            continue
        hits = sum(1 for body in bodies.values() if anchor in body)
        if hits != n_gold:
            findings.append(GateFinding(
                "anchor_unique", qid,
                f"anchor 在全集出现 {hits} 次, gold 数 {n_gold} — {hits} != {n_gold}"))
    return findings
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_docs_gold_gates.py -q -p no:warnings`
Expected: PASS (7 passed)

- [ ] **Step 5: 提交**

```bash
git add eval/docs_gold_gates.py scripts/tests/test_docs_gold_gates.py
git commit -m "feat(eval): doc 侧闸 A gold 唯一性 + 闸 B 锚串唯一性"
```

---

### Task 3: 闸 C (fact 长度) 与闸 D (卡片答不出)

**Files:**
- Modify: `sdtm-rag/eval/docs_gold_gates.py`
- Test: `sdtm-rag/scripts/tests/test_docs_gold_gates.py`

**Interfaces:**
- Consumes: Task 2 的 `GateFinding`
- Produces: `FACT_MIN_LEN = 12`; `card_texts(cards_dir) -> dict[str, str]`; `gate_fact_length(questions) -> list[GateFinding]`; `gate_card_unanswerable(questions, cards) -> list[GateFinding]`

- [ ] **Step 1: 写失败测试**

追加到 `scripts/tests/test_docs_gold_gates.py`:

```python
from eval.docs_gold_gates import (
    FACT_MIN_LEN,
    card_texts,
    gate_card_unanswerable,
    gate_fact_length,
)


def test_gate_fact_length_accepts_long_fact():
    qs = [{"id": "q1", "expected_facts": ["あ" * FACT_MIN_LEN]}]
    assert gate_fact_length(qs) == []


def test_gate_fact_length_flags_short_fact():
    qs = [{"id": "q1", "expected_facts": ["短い"]}]
    f = gate_fact_length(qs)
    assert [x.gate for x in f] == ["fact_length"]


def test_gate_fact_length_accepts_short_oid_shaped_fact():
    """OID / codelist ID 天生短, 但不是碎片 —— 放行。"""
    qs = [{"id": "q1", "expected_facts": ["C66742", "REDACTED_OID_02"]}]
    assert gate_fact_length(qs) == []


def test_gate_fact_length_flags_missing_facts():
    qs = [{"id": "q1"}]
    assert [x.qid for x in gate_fact_length(qs)] == ["q1"]


def test_card_texts_reads_cards(tmp_path):
    d = tmp_path / "cards"
    d.mkdir()
    (d / "st01__F__I.md").write_text("label: ABC", encoding="utf-8")
    (d / "ignore.txt").write_text("x", encoding="utf-8")
    assert card_texts(d) == {"st01__F__I.md": "label: ABC"}


def test_gate_card_unanswerable_passes_when_no_card_has_all_terms():
    cards = {"a.md": "TERM_A only", "b.md": "TERM_B only"}
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "TERM_B"]}]
    assert gate_card_unanswerable(qs, cards) == []


def test_gate_card_unanswerable_flags_card_covering_all_terms():
    cards = {"a.md": "TERM_A and TERM_B together"}
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "TERM_B"]}]
    f = gate_card_unanswerable(qs, cards)
    assert [x.qid for x in f] == ["q1"]
    assert "a.md" in f[0].detail


def test_gate_card_unanswerable_is_case_insensitive():
    cards = {"a.md": "term_a and TERM_b"}
    qs = [{"id": "q1", "card_probe_terms": ["TERM_A", "term_B"]}]
    assert [x.qid for x in gate_card_unanswerable(qs, cards)] == ["q1"]


def test_gate_card_unanswerable_requires_two_terms():
    """单个词太容易不撞卡 —— 闸会变成白送。"""
    qs = [{"id": "q1", "card_probe_terms": ["ONLY_ONE"]}]
    f = gate_card_unanswerable(qs, {"a.md": "x"})
    assert [x.qid for x in f] == ["q1"]
    assert "2" in f[0].detail

```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_docs_gold_gates.py -q -p no:warnings`
Expected: FAIL — `ImportError: cannot import name 'FACT_MIN_LEN'`

- [ ] **Step 3: 实现**

追加到 `eval/docs_gold_gates.py`:

```python
FACT_MIN_LEN = 12
# OID / codelist ID / 项目コード 形态: 全大写+数字+下划线, 长度 >= 3。
# 它们天生短但不是碎片 —— check_fact_recall 对它们有判别力 (v2 已验证)。
_ID_SHAPED = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")


def card_texts(cards_dir: Path | str) -> dict[str, str]:
    """field card 全文语料。

    用卡片全文而不是 catalog 派生串: audit_v2 记过一次口径事故 —— 出题人用 catalog
    近似语料、审题人用卡片全文, 数字差几个百分点。以卡片全文为准。
    """
    return {p.name: p.read_text(encoding="utf-8")
            for p in sorted(Path(cards_dir).glob("*.md"))}


def gate_fact_length(questions: list[dict]) -> list[GateFinding]:
    findings: list[GateFinding] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        facts = q.get("expected_facts") or []
        if not facts:
            findings.append(GateFinding("fact_length", qid, "缺 expected_facts"))
            continue
        for fact in facts:
            if len(fact) >= FACT_MIN_LEN or _ID_SHAPED.match(fact):
                continue
            findings.append(GateFinding(
                "fact_length", qid,
                f"fact {fact!r} 长 {len(fact)} < {FACT_MIN_LEN} 且非 ID 形态 — "
                "1-2 词碎片会让 fact-recall 顶格失明"))
    return findings


def gate_card_unanswerable(questions: list[dict], cards: dict[str, str]) -> list[GateFinding]:
    """闸 D: 没有任何一张 field card 同时含全部 probe 词。

    口径边界 (硬规矩 19): 这是**字面**筛。语义等价的卡片本闸看不见, 故 spec §4 要求
    另抽 N=6 分层样本走实测复核。单词数 < 2 直接报 —— 一个词太容易不撞卡, 闸会白送。
    """
    findings: list[GateFinding] = []
    lowered = {name: text.lower() for name, text in cards.items()}
    for q in questions:
        qid = q.get("id", "<no id>")
        terms = q.get("card_probe_terms") or []
        if len(terms) < 2:
            findings.append(GateFinding(
                "card_unanswerable", qid,
                f"card_probe_terms 只有 {len(terms)} 个, 需 >= 2 — 单词筛会白送"))
            continue
        low = [t.lower() for t in terms]
        hit = [name for name, text in lowered.items() if all(t in text for t in low)]
        if hit:
            findings.append(GateFinding(
                "card_unanswerable", qid,
                f"卡片 {sorted(hit)[:3]} 同时含全部 probe 词 — 该题卡片可能答得出"))
    return findings
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_docs_gold_gates.py -q -p no:warnings`
Expected: PASS (17 passed)

- [ ] **Step 5: 提交**

```bash
git add eval/docs_gold_gates.py scripts/tests/test_docs_gold_gates.py
git commit -m "feat(eval): doc 侧闸 C fact 长度 + 闸 D 卡片答不出"
```

---

### Task 4: 四闸 CLI 汇总

**Files:**
- Modify: `sdtm-rag/eval/docs_gold_gates.py`
- Test: `sdtm-rag/scripts/tests/test_docs_gold_gates.py`

**Interfaces:**
- Consumes: Task 2/3 的四个 gate 函数
- Produces: `run_all_gates(test_set_path, docs_dir, cards_dir) -> list[GateFinding]`; `main(argv=None) -> int` (0 = 全绿, 1 = 有 finding)

- [ ] **Step 1: 写失败测试**

追加:

```python
from eval.docs_gold_gates import main, run_all_gates


def _fixture(tmp_path, *, clean: bool):
    """clean=False 必须让**四道闸同时**报。

    只弄脏一维 (原设计只脏卡片) 时, `run_all_gates` 漏掉 A/B/C 中任意一个甚至全部三个,
    四条用例仍全绿 —— 缺失的加数在那个 fixture 上恒贡献 [], 断言原理上看不见它在不在。
    这个洞比单闸缺半边严重: 单闸缺 clean 半边只放过**恒红**闸 (吵, 会被发现), 聚合器
    缺口放过的是**恒绿** —— 而 Task 5-7 出题跑的就是这个 CLI, 漏掉的闸对每道新题静默
    返回"无 finding", 题照常入池, 「四闸全绿」还会被后续证据引用成"尺子有判别力"。
    """
    anchor = "A" * 30
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "st01__doc01__s1_1.md").write_text(FM + anchor, encoding="utf-8")
    # 脏: 第二个 chunk 也含同一锚串 → 锚串出现 2 次而 gold 数 1
    (docs / "st01__doc01__s1_10.md").write_text(
        FM + ("other body" if clean else anchor), encoding="utf-8")
    cards = tmp_path / "cards"
    cards.mkdir()
    # 脏: 同一张卡同时含全部 probe 词
    (cards / "st01__F__I.md").write_text(
        "TERM_A only" if clean else "TERM_A TERM_B", encoding="utf-8")
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        # 脏: gold 不带 .md → 同时命中 s1_1.md 与 s1_10.md
        f"  expected_sources: ['st01__doc01__s1_1{'.md' if clean else ''}']\n"
        # 脏: fact 过短且非 ID 形态
        f"  expected_facts: ['{'x' * 20 if clean else '短'}']\n"
        f"  anchor: '{anchor}'\n"
        "  card_probe_terms: ['TERM_A', 'TERM_B']\n",
        encoding="utf-8")
    return ts, docs, cards


def test_run_all_gates_clean_fixture_has_no_findings(tmp_path):
    ts, docs, cards = _fixture(tmp_path, clean=True)
    assert run_all_gates(str(ts), docs, cards) == []


def test_run_all_gates_reports_every_gate(tmp_path):
    """聚合器漏掉任一加数本用例必红 —— 断言的是 gate 集合, 不是某一个。"""
    ts, docs, cards = _fixture(tmp_path, clean=False)
    f = run_all_gates(str(ts), docs, cards)
    assert sorted({x.gate for x in f}) == [
        "anchor_unique", "card_unanswerable", "fact_length", "gold_unique"]


def test_main_exit_code_0_when_clean(tmp_path, capsys):
    ts, docs, cards = _fixture(tmp_path, clean=True)
    rc = main([str(ts), "--docs-dir", str(docs), "--cards-dir", str(cards)])
    assert rc == 0
    assert "0 条" in capsys.readouterr().out


def test_main_exit_code_1_when_findings(tmp_path):
    ts, docs, cards = _fixture(tmp_path, clean=False)
    assert main([str(ts), "--docs-dir", str(docs), "--cards-dir", str(cards)]) == 1
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_docs_gold_gates.py -q -p no:warnings`
Expected: FAIL — `ImportError: cannot import name 'run_all_gates'`

- [ ] **Step 3: 实现**

追加到 `eval/docs_gold_gates.py`。**先补顶部 import**(到这一步它们才真正被用上,
Task 2 按 ruff 裁定删掉/未提前加):

```python
import argparse
import json
import sys
from eval.lint_gold import doc_chunk_names, load_questions, match_names   # 后两个是 Task 2 fix 移过去的
```

⚠ 漏掉 `load_questions` 会让 `run_all_gates` 与 `main` 直接 NameError —— Task 2 已把它
从 `docs_gold_gates` 移进 `lint_gold`(消除逐字复制的题集口径),本文件不再自带定义。

```python
def run_all_gates(test_set_path: Path | str, docs_dir: Path | str,
                  cards_dir: Path | str) -> list[GateFinding]:
    questions = load_questions(test_set_path)
    bodies = chunk_bodies(docs_dir)
    cards = card_texts(cards_dir)
    return (gate_gold_unique(test_set_path, docs_dir)
            + gate_anchor_unique(questions, bodies)
            + gate_fact_length(questions)
            + gate_card_unanswerable(questions, cards))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="doc 侧题集四道入池闸 (确定性, 零 LLM)")
    ap.add_argument("test_set")
    ap.add_argument("--docs-dir", required=True)
    ap.add_argument("--cards-dir", required=True)
    ap.add_argument("--json", help="把 findings 另存为 JSON (收口证据用)")
    args = ap.parse_args(argv)

    findings = run_all_gates(args.test_set, args.docs_dir, args.cards_dir)
    n_q = len(load_questions(args.test_set))
    for f in findings:
        print(f"[{f.gate}] {f.qid}: {f.detail}")
    if args.json:
        Path(args.json).write_text(
            json.dumps([f.__dict__ for f in findings], ensure_ascii=False, indent=2),
            encoding="utf-8")
    print(f"\n计分题 {n_q} 道 · {len(findings)} 条 finding "
          f"(闸 B 只挡字面, 语义等价看不见 — 引用绿灯时必须同时写这句)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_docs_gold_gates.py -q -p no:warnings`
Expected: PASS (21 passed)

- [ ] **Step 5: 全量回归 + 提交**

```bash
.venv/bin/python -m pytest -p no:warnings -q     # 0 failed, 总数 >= 1060
git add eval/docs_gold_gates.py scripts/tests/test_docs_gold_gates.py
git commit -m "feat(eval): doc 侧四闸 CLI 汇总 + 退出码语义"
```

---

### Task 5: 出题批 1 — 单节可答 12 题

**Files:**
- Create: `sdtm-rag/data/study/st01/eval/test_set_docs_v1.yml` (**不进 git**)
- Create: `sdtm-rag/data/study/st01/eval/DOCS_V1_NOTES.md` (**不进 git**)
- Create: `sdtm-rag/data/study/st01/eval/failures/` (**不进 git**)

**Interfaces:**
- Consumes: Task 4 的 `python -m eval.docs_gold_gates` CLI
- Produces: 12 道 `category: single_section` 题, 全部过四闸

> **分批不是探针。** spec §7 的三条阈值已于定稿写死, **不因任何批次的数据改动**。分批的唯一目的是让闸 D 的筛掉率若超 50% 能更早触发停止条款, 而不是拿早期数据回头调闸。

- [ ] **Step 1: 取原页文本 (来源隔离)**

```bash
.venv/bin/python -c "
from scripts.study.paths import resolve_study
from scripts.study.pdf_text import extract_pages
sp = resolve_study('st01')
pages = extract_pages(sp.doc_pdfs[0])
import pathlib
pathlib.Path('/tmp/st01_doc01_pages').mkdir(exist_ok=True)
for i, t in enumerate(pages, 1):
    pathlib.Path(f'/tmp/st01_doc01_pages/p{i:03d}.txt').write_text(t, encoding='utf-8')
print('pages:', len(pages))"
```
Expected: `pages: 113`

**只读 `/tmp/st01_doc01_pages/`, 不读 `data/study/st01/docs/`** —— 这是闸 1。
(`/tmp` 是本机临时目录, 不进 git; 本 task 结束时删除。)

- [ ] **Step 2: 读 p017–p060 并起草 12 题**

用 CRC/DM 的自然问法, 每题答案必须完整落在**单一节**内。逐题写:
`id` / `category: single_section` / `question` / `expected_facts` (≥12 字符或 ID 形态) /
`anchor` (从原页逐字抄, ≥20 字符) / `card_probe_terms` (≥2 个) / `chapter` / `note`。

`expected_sources` 此步先留空 —— **定 gold 要读 chunk, 属 Step 3**。

答案落在 p001–p016 (卷首 + 目录 + 第 1 章前段) 的题, 写进
`test_set_docs_v1_l1pool.yml` 并标 `known_gap: true`, **不进计分池**。

- [ ] **Step 3: 定 gold (此时才读 chunk 产物)**

```bash
.venv/bin/python -c "
import pathlib, re, sys
anchor = sys.argv[1]
d = pathlib.Path('data/study/st01/docs')
FM = re.compile(r'\A---\n.*?\n---\n', re.DOTALL)
hits = [p.name for p in sorted(d.glob('*.md'))
        if anchor in FM.sub('', p.read_text(encoding='utf-8'), count=1)]
print(len(hits), hits)" '<锚串>'
```
出现次数 != 1 → 改锚串 (加长/换段), 不要改闸。把命中的文件名填进 `expected_sources`。

- [ ] **Step 4: 跑四闸**

```bash
.venv/bin/python -m eval.docs_gold_gates \
  data/study/st01/eval/test_set_docs_v1.yml \
  --docs-dir data/study/st01/docs \
  --cards-dir data/study/st01/cards
```
Expected: `0 条 finding`, 退出码 0

- [ ] **Step 5: 处理被闸打回的题 (规则 B)**

任何被打回的题 **不删**, 整条挪进 `data/study/st01/eval/failures/batch1_<qid>.md`,
写明: 原题面 / 触发哪道闸 / 闸给的 detail / 判定 (改锚串? 换题? 属 L1 池?) / 下一版输入。

**闸 D 停止条款**: 若本批被闸 D 打回的题数 > 本批起草总数的 50%, **立刻停下, 不要继续出题**,
把数字报告用户 —— 那意味着 doc 与卡片信息重叠远超预期, C1 的价值假设与 C2 同一种死法。

- [ ] **Step 6: 记录来源隔离声明 + 清理**

在 `DOCS_V1_NOTES.md` 写批 1 段: 读了哪些页区间、起草几题、过闸几题、打回几题及去向,
并逐字写一句「本批题面在 Step 2 阶段只依据 `/tmp/st01_doc01_pages/`, 未打开 `docs/`」。

```bash
rm -rf /tmp/st01_doc01_pages
git status --porcelain data/study     # 必须为空 —— 题集不得进 git
```

---

### Task 6: 出题批 2 — 跨节聚合 8 题 + part 家族 5 题

**Files:**
- Modify: `sdtm-rag/data/study/st01/eval/test_set_docs_v1.yml` (**不进 git**)
- Modify: `sdtm-rag/data/study/st01/eval/DOCS_V1_NOTES.md` (**不进 git**)

**Interfaces:**
- Consumes: Task 5 的题集文件与四闸 CLI
- Produces: 累计 25 道计分题 (12 单节 + 8 跨节 + 5 part 家族)

- [ ] **Step 1: 重新取原页文本**

同 Task 5 Step 1 的命令 (闸 1 每批都要守)。

- [ ] **Step 2: 起草 8 道跨节题**

答案需要**两个及以上节**才能完整回答。`expected_sources` 写全部相关 chunk (AND),
`anchor` 选一条在**这些 gold 里正好出现 N 次**的串 —— 若找不到这样的串,
说明该题其实单节可答, 改题或降型, 别放宽闸。

**禁用 `expected_sources_any`** (Global Constraints)。

- [ ] **Step 3: 起草 5 道 part 家族题**

覆盖两个家族:

```bash
ls data/study/st01/docs | grep -E "__part"
# → st01__doc01__s22_1__part01.md / __part02.md
#   st01__doc01__s8_2__part01.md / __part02.md / __part03.md
```

判据按答案落点定, **不设全局政策**:
- 答案完整落在某一份 → `expected_sources` 单份
- 答案被切点劈开 → `expected_sources` 两份 AND —— **这是 L6 探针本身**

5 题里**至少 2 题**必须是"被切点劈开"型 (`8.2` 的 2→3 与 `22.1` 的 1→2 各一),
否则 U4 拿不到"表格被切是否真伤"的证据。在 `note` 里标 `L6_probe: true`。

- [ ] **Step 4: 跑四闸**

```bash
.venv/bin/python -m eval.docs_gold_gates \
  data/study/st01/eval/test_set_docs_v1.yml \
  --docs-dir data/study/st01/docs --cards-dir data/study/st01/cards
```
Expected: `0 条 finding`, 退出码 0

- [ ] **Step 5: 归档打回题 + 记录 + 清理**

同 Task 5 Step 5/6 (failures 文件名前缀改 `batch2_`)。闸 D 停止条款同样适用。

```bash
rm -rf /tmp/st01_doc01_pages
git status --porcelain data/study     # 必须为空
```

---

### Task 7: 出题批 3 — 表格类 5 题 + L1 池收口

**Files:**
- Modify: `sdtm-rag/data/study/st01/eval/test_set_docs_v1.yml` (**不进 git**)
- Create: `sdtm-rag/data/study/st01/eval/test_set_docs_v1_l1pool.yml` (**不进 git**)
- Modify: `sdtm-rag/data/study/st01/eval/DOCS_V1_NOTES.md` (**不进 git**)

**Interfaces:**
- Consumes: Task 5/6 的题集
- Produces: 30 道计分题 (12/8/5/5) + L1 池条数统计

- [ ] **Step 1: 重新取原页文本** (同前, 闸 1)

- [ ] **Step 2: 起草 5 道表格类题**

答案落在多列/表格形态区。至少 2 题瞄准 L6 那两个疑似被切断的表格
(`8.2` 的 2→3 切点、`22.1` 的 1→2 切点), `note` 标 `L6_probe: true`。
表格题的 `anchor` 用**单元格内的连续文本**, 不要跨列拼 —— `-layout` 的列间空格数不稳定。

- [ ] **Step 3: L1 池收口**

把三批里所有"答案落在首锚点之前"的题汇总进 `test_set_docs_v1_l1pool.yml`,
每题带 `known_gap: true` 与 `page` 字段。统计条数:

```bash
.venv/bin/python -c "
import yaml, pathlib
p = pathlib.Path('data/study/st01/eval/test_set_docs_v1_l1pool.yml')
qs = yaml.safe_load(p.read_text(encoding='utf-8')) if p.exists() else []
print('L1 池题数:', len(qs))"
```

这个数字是 kickoff §3「卷首+第 1 章 (≈16,880 字符) 要不要成 chunk」的裁定依据。
**不替用户裁定** —— 只在证据里写数字与它意味着什么。

- [ ] **Step 4: 全量四闸 + 配比核对**

```bash
.venv/bin/python -m eval.docs_gold_gates \
  data/study/st01/eval/test_set_docs_v1.yml \
  --docs-dir data/study/st01/docs --cards-dir data/study/st01/cards \
  --json /tmp/docs_v1_gates.json

.venv/bin/python -c "
import yaml, collections, pathlib
qs = yaml.safe_load(pathlib.Path('data/study/st01/eval/test_set_docs_v1.yml').read_text(encoding='utf-8'))
print('计分题:', len(qs))
print('配比:', collections.Counter(q['category'] for q in qs))
print('章覆盖:', len({q['chapter'] for q in qs}), sorted({q['chapter'] for q in qs}))
print('L6 探针:', sum(1 for q in qs if 'L6_probe' in str(q.get('note',''))))"
```
Expected: `计分题: 30` · 配比 `single_section 12 / cross_section 8 / part_family 5 / table 5` ·
`L6 探针 >= 4` · 四闸 `0 条 finding`

章覆盖数**记录即可, 不是 PASS 闸** (spec §5)。

- [ ] **Step 5: 记录 + 清理**

```bash
rm -rf /tmp/st01_doc01_pages
git status --porcelain data/study     # 必须为空
```

---

### Task 8: doc-only 上界基线 + 自毁条款裁定

**Files:**
- Create: `sdtm-rag/data/study/st01/eval/runs/docs_v1_upper_bound.json`, `data/study/st01/eval/runs/docs_v1_upper_bound_rerun.json` (**不进 git**, `runs/` 已忽略)

**Interfaces:**
- Consumes: Task 7 的 30 题题集
- Produces: doc-only 上界数字 (逐题 + 均值), 供 Task 10 写进证据、供 U2 作对照上界

- [ ] **Step 1: 跑第一遍**

```bash
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_upper_bound.json
```

> `--kb-root cards/` **不是混库**: `RAGEngine.__init__` 硬要求 kb_root 下有 `ROUTING.md`
> 与 `INDEX.md` (docs/ 没有), 而 retrieval-only 下 kb_root 只进 system prompt 不参与检索;
> hybrid 的 BM25 索引从 **collection 自身**建 (`_build_bm25_index`)。
> 这句话必须原样进 NOTES 与证据 —— 否则下一个人会读成混库。

- [ ] **Step 2: 跑第二遍并逐题比对**

```bash
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_upper_bound_rerun.json

.venv/bin/python -c "
import json
a = json.load(open('data/study/st01/eval/runs/docs_v1_upper_bound.json'))
b = json.load(open('data/study/st01/eval/runs/docs_v1_upper_bound_rerun.json'))
ra = {r['id']: r['source_recall'] for r in a['results']}
rb = {r['id']: r['source_recall'] for r in b['results']}
diff = {k: (ra[k], rb[k]) for k in ra if ra[k] != rb[k]}
print('逐题差异:', diff or 'NONE')
print('avg run1:', a['summary']['source_recall_avg'])
print('avg run2:', b['summary']['source_recall_avg'])"
```
Expected: `逐题差异: NONE`, 两个均值相等

- [ ] **Step 3: 裁定三条自毁条款**

| 实测 | 动作 |
|---|---|
| 均值 ≥ 0.95 | **停**: 题集退回重写加难; 归档本版到 `failures/`; 报告用户; **不许改阈值** |
| 均值 ≤ 0.40 | **停**: 题/锚串脱离 chunk 实际, 退回重写; 同上归档 |
| 0.40 < 均值 < 0.95 | 继续 Task 9 |

闸 D 累计筛掉率同样在此复核:

```bash
ls data/study/st01/eval/failures/ | wc -l   # 与 NOTES 记录的起草总数比
```
筛掉率 > 50% → 停下报告用户 (与批次内的即时条款同判据)。

- [ ] **Step 4: 卡片侧零回归复核**

doc 题集不改任何生产配置, 但必须证明这一点:

```bash
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/v2_after_u1.json
.venv/bin/python -c "
import json; print(json.load(open('/tmp/v2_after_u1.json'))['summary']['source_recall_avg'])"
```
Expected: `0.875` (与开工基线逐题相同)

- [ ] **Step 5: 把三个数字记进 NOTES**

doc-only 上界均值 / 逐题分布 / 卡片侧 87.5% 复核结果。此时**不写证据文件** (Task 10 写)。

---

### Task 9: 闸 D 实测复核 (N=6) + 规则 A 独立抽检 (N=8)

**Files:**
- Create: `sdtm-rag/evidence/step_u1_audit.md` (由抽检方写, 进 git —— **零真名零正文**)
- Modify: `sdtm-rag/data/study/st01/eval/DOCS_V1_NOTES.md` (**不进 git**)

**Interfaces:**
- Consumes: Task 7 的题集、Task 8 的基线
- Produces: 抽检判定 (PASS / 有条件 PASS / FAIL) + 抽检方发现的限制清单

- [ ] **Step 1: 闸 D 实测复核, 分层抽 N=6**

抽样: 单节 2 / 跨节 2 / part 1 / 表格 1 (**不是取前 6**)。对每题在**卡片库**上跑:

```bash
.venv/bin/python -m eval.run_eval <只含这6题的临时 yml> \
  --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards \
  --output /tmp/u1_card_probe.json
```
判据: 答案里**不含**该题的 `expected_facts`, 即卡片库确实答不出。
任一题答得出 → 该题从计分池移除并归档 `failures/`, 且**必须重跑 Task 8 的基线**
(题数变了, 旧均值作废)。

- [ ] **Step 2: 派独立抽检方 (规则 D: 不同 `subagent_type` + 不同 session)**

抽检方任务书要点 (写进派发 prompt):
1. **不许 import `eval.docs_gold_gates`** —— 自建参照物, 自己调 poppler 与文件读取
2. 抽 N=8 题 (按 category 分层), 逐题核验三元组: ① `anchor` 在原页里逐字存在
   ② `anchor` 在 114 chunk 正文中的出现次数 == `expected_sources` 数
   ③ `expected_sources` 里的 chunk 页区间覆盖该 anchor 所在原页
3. 对四道闸各做一次**变异测试**: 把闸函数改成恒返回 `[]`, 确认对应单测变红。
   有任何一道闸变异后仍全绿 → 该闸是装饰品, 当场点名 (硬规矩 18)
4. **边做边落盘** `evidence/step_u1_audit.md` —— 「派了审查」≠「审过了」(硬规矩 17);
   拿不到报告就当那一环没发生, 并在收口证据里点名
5. 抽检期间**不改产物目录**; 开工与收工各记一次 `docs/` 目录 sha256 (C1 的并发隔离教训)

```bash
find data/study/st01/docs -name '*.md' | sort | xargs shasum -a 256 | shasum -a 256
```

- [ ] **Step 3: 实现方独立复核抽检结论 (硬规矩 17b)**

抽检方也会算错 (C1 里 66,200 vs 66,086)。对抽检报告里的**每个关键数字**,
用**非自洽写法**复算一遍 —— 例如锚串计数不要复用抽检方的扫描函数, 改用
`grep -c` 对 `docs/*.md` 直接数, 两条路对上才算数。

- [ ] **Step 4: 归档失败与限制**

抽检方发现的每条限制进 NOTES 的「已知限制」段, 并标注它**看不见什么** (硬规矩 19)。
至少要有: 闸 B 只挡字面 / 闸 D 只挡字面 / PDF 文本层忠实性无法用本轨手段证伪 (C1 L9)。

---

### Task 10: 收口证据 + 索引链

**Files:**
- Create: `sdtm-rag/evidence/checkpoints/doc_track_u1_question_set.md` (进 git)
- Modify: `.work/meta/worklog/phase_07_rag_kg.md`, `docs/PROGRESS.md`
- Modify: `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` (U1 标 DONE, U2 成为下一单元)

**Interfaces:**
- Consumes: Task 8 的数字、Task 9 的抽检判定
- Produces: U2 可直接引用的对照上界与限制清单

- [ ] **Step 1: 写收口证据**

必含段落 (照 C1 证据的骨架):
1. 一句话结论
2. 数字表: 计分题 30 / 配比 / 章覆盖 / L1 池条数 / doc-only 上界均值 / 卡片侧 87.5% 复核 / pytest 数
3. 四道闸各自的**参照物**与结果, 每道闸后面紧跟**它看不见什么** (硬规矩 19)
4. 三条自毁条款的实测取值与裁定
5. 已知限制表 (含闸 B/D 的字面边界、C1 L9 盲点、L1 覆盖缺口对本题集的影响)
6. 复跑命令 (逐条可执行)
7. 红线复扫: `catalog` 标识符 × 本轮新增 git 文件 = 0 命中

```bash
git status --porcelain data/study    # 空
git diff --stat HEAD                 # 只应有 eval/ scripts/tests/ evidence/ docs/ .work/
```

- [ ] **Step 2: 红线程序化复扫**

```bash
.venv/bin/python -c "
import json, subprocess, pathlib
cat = json.load(open('data/study/st01/catalog.json'))
vals = {str(i[k]) for i in cat['items'] for k in ('label','item_oid','form_name') if i.get(k)}
vals = {v for v in vals if len(v) >= 4}
files = subprocess.run(['git','ls-files'], capture_output=True, text=True).stdout.split()
hits = []
for f in files:
    p = pathlib.Path(f)
    if not p.is_file(): continue
    try: t = p.read_text(encoding='utf-8')
    except Exception: continue
    for v in vals:
        if v in t: hits.append((f, v))
print('命中:', len(hits))
for h in hits[:20]: print(' ', h)"
```
Expected: 只剩 C1 已记录的 4 条存量命中 (`eval/routing_gold_ja_supplement.yml` 2 条 /
`scripts/tests/test_ja_tokenize.py` 2 条)。**本轮新增文件必须 0 命中**; 若有新增, 当场删改。

- [ ] **Step 3: 更新索引链 (Chain B)**

- `.work/meta/worklog/phase_07_rag_kg.md` — append 本 session 记录
- `docs/PROGRESS.md` — Phase 7 行更新 (U1 DONE, 下一单元 U2 接线)
- `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` — §2 U1 标 DONE 并指向证据; U2 成为路由词的落点
- `CLAUDE.md` Key Paths — 加一行 U1 证据指针 (≤ 80 字符)

- [ ] **Step 4: 全量回归 + 提交**

```bash
.venv/bin/python -m pytest -p no:warnings -q      # 0 failed
git add -A
git commit -m "feat(study): doc 轨 U1 题集与四闸收口 + doc-only 上界基线"
```

- [ ] **Step 5: 报告用户**

一段话: doc-only 上界数字 / 自毁条款是否触发 / 抽检判定 / L1 池条数 (等你裁定卷首 chunk) /
U2 的三个接线选项现在有尺子可比了。

---

## Self-Review

**Spec 覆盖核对**

| spec 段 | 落在哪个 task |
|---|---|
| §3 判据粒度 = chunk 文件名 | Task 1 (`doc_chunk_names`) + Task 2 (闸 A) |
| §4 闸 1 来源隔离 | Task 5/6/7 Step 1-2 + NOTES 声明 (**机器查不了, 已在 Global Constraints 写明**) |
| §4 闸 2 卡片答不出 (确定性 + N=6 实测) | Task 3 (`gate_card_unanswerable`) + Task 9 Step 1 |
| §4 闸 3 锚串唯一 ≥20 字符 | Task 2 (`gate_anchor_unique`, `ANCHOR_MIN_LEN`) |
| §4 闸 4 fact ≥12 字符 | Task 3 (`gate_fact_length`, `FACT_MIN_LEN`) |
| §5 配比 12/8/5/5 + part 按落点定 + L6 探针 | Task 5/6/7, 配比核对在 Task 7 Step 4 |
| §5 L1 池不计分 + 计数作裁定依据 | Task 7 Step 3 |
| §5 OR 组一题都不用 | Global Constraints + Task 6 Step 2 |
| §6 产物 1-5 | Task 5 (1,2) · Task 1-4 (3,4) · Task 10 (5) |
| §6.1 doc-only 上界 + kb-root 不是混库 | Task 8 Step 1-2 |
| §6.2 规则 A 抽检 N=8 + 边做边落盘 + 不改产物目录 | Task 9 Step 2 |
| §7 PASS 三条 + 自毁三条 | Task 7 Step 4 (闸) · Task 8 Step 2 (可复现) · Task 8 Step 3 (自毁) · Task 9 (抽检) |
| §8 不能证明什么 | Task 10 Step 1 第 5 段 |
| §9 开工自检 | 本 session 已实跑三条全绿 (1036 / 4329·959·114 / 0.875) |

**占位符扫描**: 无 TBD/TODO; 每个代码步骤都有可执行代码; 出题步骤给了确切页区间来源、
判据与打回处置, 题面本身是这个 task 的产出而非占位符。

**类型一致性**: `GateFinding(gate, qid, detail)` 三字段在 Task 2/3/4 一致;
`doc_chunk_names` 在 Task 1 定义、Task 2 使用; `lint_gold(..., docs_dir=)` 在 Task 1 定义、
Task 2 `gate_gold_unique` 调用; `chunk_bodies` 返回 `dict[str, str]` 与
`gate_anchor_unique(questions, bodies)` 的第二参数类型一致; `card_texts` 同理。
`run_eval` 结果 JSON 的 `summary.source_recall_avg` 与 `results[].source_recall`
键名已在本 session 实跑确认。
