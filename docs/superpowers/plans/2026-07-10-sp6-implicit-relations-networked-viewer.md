# SP6 — 隐性关系挖掘 + 网状富节点查看器 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 从 SDTMIG 散文挖出证据锚定的隐性跨域关系(数据流/显式链接/共现),并把 KG 查看器升级为网状点击展开 + 富节点,试点肿瘤评估簇。

**Architecture:** 离线管线 `mine_implicit_relations.py` 读 `knowledge_base/domains/<簇>/{assumptions,examples}.md`,三个抽取器(正则/计数/LLM)产出 `data/meta/implicit_relations.json`(advisory,永不写回 meta.yaml);数据流边过两道闸(逐字引文命中 + 对抗核验)。`build_kg_viewer.py` 同时内嵌 meta.yaml(硬)+ implicit_relations.json(软),查看器新增 explore 网状模式、两层边、富节点、RAG 按钮。

**Tech Stack:** Python 3.12 · pyyaml · litellm(deepseek 默认)· pytest · 原生 SVG/JS 查看器(零前端依赖)

## Global Constraints

- 所有命令从 `branches/07_rag_kg/sdtm-rag/` 运行;Python 用 `.venv/bin/python`。
- 测试:`.venv/bin/python -m pytest scripts/tests/`;lint/type:`ruff check . && mypy server/ scripts/`。
- `implicit_relations.json` 是 advisory 层,**绝不修改 `data/meta/meta.yaml`**。
- 数据流边默认置信阈值 **0.6**;每对域最多保留 **2** 条数据流边;展开上限 **K=12**。
- LLM 默认 `deepseek/deepseek-chat`,`temperature=0`;API key 从 `.env` 经 dotenv 载入(`OPENAI_API_KEY` 不需要——本管线不做 embedding)。
- 簇种子:`TU TR RS PR MI`;邻居 = 种子散文里用 RELREC/link/明确点名引用到的域,纳入一跳。
- 抽取(writer)与对抗核验(reviewer)是不同调用/不同 prompt(Rule D 隔离);被毙的边归档 `failures/`(Rule B),不删。

---

## File Structure

| 文件 | 职责 |
|---|---|
| `scripts/mine_implicit_relations.py` (新增) | 管线:簇解析、散文加载、三抽取器、两道闸、组装、CLI |
| `scripts/tests/test_mine_implicit_relations.py` (新增) | 管线单测(确定性部分 golden + LLM 部分 monkeypatch) |
| `scripts/tests/fixtures/sp6_prose/` (新增) | 迷你散文 fixture(可控输入,供确定性测试) |
| `data/meta/implicit_relations.json` (生成) | 产物:advisory 隐性关系边 |
| `evidence/checkpoints/implicit_relations_audit.md` (生成) | Rule A N=8 抽检留证 |
| `scripts/build_kg_viewer.py` (改) | 内嵌 implicit_relations.json + 富节点数据;新增 explore/两层边/RAG JS |
| `kg_viewer.html` (再生成) | 产物 |

数据模型(全程用普通 dict,匹配 JSON 契约):
```python
Edge = dict  # {id, source, target, kind, directed, relation,
             #  evidence:{quote, source_file, line}, confidence, extractor, verified, verify_note}
```

---

## Task 1: 管线骨架 — 簇解析 + 散文加载

**Files:**
- Create: `scripts/mine_implicit_relations.py`
- Create: `scripts/tests/test_mine_implicit_relations.py`
- Create: `scripts/tests/fixtures/sp6_prose/domains/{TU,PR}/examples.md`

**Interfaces:**
- Produces:
  - `KB_ROOT: Path` 默认 = `Path(__file__).resolve().parents[4] / "knowledge_base"`
  - `SEEDS = ["TU","TR","RS","PR","MI"]`
  - `resolve_cluster(kb_root: Path, seeds: list[str]) -> list[str]` — seeds + 一跳邻居(去重排序)
  - `load_prose(kb_root: Path, domains: list[str]) -> dict[str, dict[str, str]]` — `{dom: {"assumptions": str, "examples": str}}`(缺文件 → 空串)

- [ ] **Step 1: 写 fixture 散文**

`scripts/tests/fixtures/sp6_prose/domains/PR/examples.md`:
```markdown
# PR — Procedures

The tumor measurements obtained via the procedure are recorded in the TR dataset.
Records in PR are linked to TU via RELREC.
```
`scripts/tests/fixtures/sp6_prose/domains/TU/examples.md`:
```markdown
# TU — Tumor/Lesion Identification

Each identified tumor is later measured; see TR for results and RS for response.
```

- [ ] **Step 2: 写失败测试**

`scripts/tests/test_mine_implicit_relations.py`:
```python
from pathlib import Path
from scripts import mine_implicit_relations as M

FIX = Path(__file__).parent / "fixtures" / "sp6_prose"

def test_load_prose_reads_examples():
    prose = M.load_prose(FIX, ["PR", "TU"])
    assert "recorded in the TR dataset" in prose["PR"]["examples"]
    assert prose["TU"]["assumptions"] == ""  # 缺文件 -> 空串

def test_resolve_cluster_adds_named_neighbors():
    # PR 散文点名 TR/TU;TU 点名 TR/RS -> 邻居并入
    cluster = M.resolve_cluster(FIX, ["PR", "TU"])
    assert {"PR", "TU", "TR", "RS"} <= set(cluster)
    assert cluster == sorted(cluster)
```

- [ ] **Step 3: 运行,确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q`
Expected: FAIL(`ModuleNotFoundError` / `AttributeError`)

- [ ] **Step 4: 写最小实现**

`scripts/mine_implicit_relations.py`:
```python
"""SP6: mine implicit cross-domain relations from IG prose (advisory layer).

Reads knowledge_base/domains/<D>/{assumptions,examples}.md for a cluster and
emits data/meta/implicit_relations.json. NEVER writes meta.yaml. Deterministic
where possible (explicit links, co-occurrence); LLM only for data-flow, with a
verbatim-quote gate + adversarial verification.
"""
from __future__ import annotations

import re
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parents[4] / "knowledge_base"
SEEDS = ["TU", "TR", "RS", "PR", "MI"]
CONF_THRESHOLD = 0.6
MAX_FLOW_PER_PAIR = 2

_DOMAIN_TOKEN = re.compile(r"\b([A-Z]{2,4})\b")


def load_prose(kb_root: Path, domains: list[str]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for d in domains:
        base = kb_root / "domains" / d
        out[d] = {
            kind: (base / f"{kind}.md").read_text(encoding="utf-8")
            if (base / f"{kind}.md").exists() else ""
            for kind in ("assumptions", "examples")
        }
    return out


def resolve_cluster(kb_root: Path, seeds: list[str]) -> list[str]:
    """seeds + one-hop: any known domain code literally named in a seed's prose."""
    known = {p.name for p in (kb_root / "domains").iterdir() if p.is_dir()}
    prose = load_prose(kb_root, seeds)
    found: set[str] = set(seeds)
    for d in seeds:
        text = prose[d]["assumptions"] + "\n" + prose[d]["examples"]
        for tok in _DOMAIN_TOKEN.findall(text):
            if tok in known and tok != d:
                found.add(tok)
    return sorted(found)
```

- [ ] **Step 5: 运行,确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q`
Expected: PASS(2 passed)

- [ ] **Step 6: Commit**

```bash
git add scripts/mine_implicit_relations.py scripts/tests/test_mine_implicit_relations.py scripts/tests/fixtures/sp6_prose
git commit -m "feat(sp6): mining pipeline skeleton — cluster resolution + prose loading"
```

---

## Task 2: 抽取器 — 显式链接(确定性正则)

**Files:**
- Modify: `scripts/mine_implicit_relations.py`
- Modify: `scripts/tests/test_mine_implicit_relations.py`

**Interfaces:**
- Consumes: `load_prose` 输出
- Produces: `extract_explicit_links(prose: dict, domains: list[str]) -> list[Edge]`
  — 对每行含 `RELREC`/`--LNKID`/`SUPP<dom>` 且点名另一域的句子产一条 `kind="explicit_link"`, `directed=False`, `relation=机制词`, `extractor="regex"`, `verified=True`。

- [ ] **Step 1: 写失败测试**

追加到测试文件:
```python
def test_explicit_links_finds_relrec():
    prose = M.load_prose(M.Path(__file__).parent.joinpath("fixtures","sp6_prose"), ["PR","TU"])
    edges = M.extract_explicit_links(prose, ["PR","TU","TR","RS"])
    relrec = [e for e in edges if e["relation"] == "RELREC"]
    assert any({e["source"], e["target"]} == {"PR","TU"} for e in relrec)
    e = relrec[0]
    assert e["kind"] == "explicit_link" and e["extractor"] == "regex"
    assert e["verified"] is True and e["directed"] is False
    assert "RELREC" in e["evidence"]["quote"]
```

- [ ] **Step 2: 运行,确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py::test_explicit_links_finds_relrec -q`
Expected: FAIL(`AttributeError: extract_explicit_links`)

- [ ] **Step 3: 写实现**

追加到 `mine_implicit_relations.py`:
```python
_MECH = re.compile(r"\b(RELREC|RELSPEC|RELSUB|SUPPQUAL|SUPP[A-Z]{2})\b")


def _edge(src, tgt, kind, directed, relation, quote, src_file, line, conf,
          extractor, verified, note="") -> dict:
    return {
        "id": f"{kind[:4]}:{src}>{tgt}:{line}",
        "source": src, "target": tgt, "kind": kind, "directed": directed,
        "relation": relation,
        "evidence": {"quote": quote.strip(), "source_file": src_file, "line": line},
        "confidence": conf, "extractor": extractor,
        "verified": verified, "verify_note": note,
    }


def extract_explicit_links(prose: dict, domains: list[str]) -> list[dict]:
    dom_set = set(domains)
    out: list[dict] = []
    for d, kinds in prose.items():
        for kind in ("assumptions", "examples"):
            src_file = f"knowledge_base/domains/{d}/{kind}.md"
            for i, line in enumerate(kinds[kind].split("\n"), 1):
                m = _MECH.search(line)
                if not m:
                    continue
                mech = m.group(1)
                for other in _DOMAIN_TOKEN.findall(line):
                    if other in dom_set and other != d and not _MECH.match(other):
                        out.append(_edge(d, other, "explicit_link", False, mech,
                                         line, src_file, i, 0.95, "regex", True))
    return out
```

- [ ] **Step 4: 运行,确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q`
Expected: PASS(3 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/mine_implicit_relations.py scripts/tests/test_mine_implicit_relations.py
git commit -m "feat(sp6): explicit-link extractor (deterministic RELREC/link regex)"
```

---

## Task 3: 抽取器 — 共现(确定性计数)

**Files:**
- Modify: `scripts/mine_implicit_relations.py`, test 文件

**Interfaces:**
- Produces: `extract_cooccurrence(prose: dict, domains: list[str], min_count: int = 2) -> list[Edge]`
  — 两域在同一域的散文里互相点名的次数 ≥ min_count → 一条 `kind="co_occurrence"`, `directed=False`, `confidence=min(0.5+0.1*count,0.9)`, `extractor="count"`, `verified=True`。无向去重(source<target)。

- [ ] **Step 1: 写失败测试**
```python
def test_cooccurrence_counts_and_dedups():
    prose = {
        "PR": {"assumptions": "PR relates to TR. See TR again. TR TR.", "examples": ""},
        "TR": {"assumptions": "TR mentions PR here.", "examples": ""},
    }
    edges = M.extract_cooccurrence(prose, ["PR", "TR"], min_count=2)
    co = [e for e in edges if e["kind"] == "co_occurrence"]
    assert len(co) == 1                       # 无向, 只一条
    assert co[0]["source"] == "PR" and co[0]["target"] == "TR"  # source<target
    assert co[0]["directed"] is False and co[0]["extractor"] == "count"
```

- [ ] **Step 2: 运行,确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py::test_cooccurrence_counts_and_dedups -q`
Expected: FAIL

- [ ] **Step 3: 写实现**
```python
def extract_cooccurrence(prose: dict, domains: list[str], min_count: int = 2) -> list[dict]:
    dom_set = set(domains)
    pair_count: dict[tuple[str, str], int] = {}
    for d, kinds in prose.items():
        text = kinds["assumptions"] + "\n" + kinds["examples"]
        for other in _DOMAIN_TOKEN.findall(text):
            if other in dom_set and other != d:
                key = tuple(sorted((d, other)))
                pair_count[key] = pair_count.get(key, 0) + 1
    out: list[dict] = []
    for (a, b), c in sorted(pair_count.items()):
        if c >= min_count:
            out.append(_edge(a, b, "co_occurrence", False, "",
                             f"{a}/{b} co-mentioned {c}x", "(co-occurrence)", c,
                             min(0.5 + 0.1 * c, 0.9), "count", True))
    return out
```

- [ ] **Step 4: 运行,确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q`
Expected: PASS(4 passed)

- [ ] **Step 5: Commit**
```bash
git add scripts/mine_implicit_relations.py scripts/tests/test_mine_implicit_relations.py
git commit -m "feat(sp6): co-occurrence extractor (deterministic count, undirected)"
```

---

## Task 4: 抽取器 — 数据流(LLM)+ 闸 1 逐字引文校验

**Files:**
- Modify: `scripts/mine_implicit_relations.py`, test 文件

**Interfaces:**
- Produces:
  - `_complete_json(prompt: str, model: str) -> list[dict]` — 调 litellm,解析 JSON 数组(健壮:剥 ```json 围栏)
  - `extract_data_flow(prose: dict, domains: list[str], model: str, complete=_complete_json) -> list[dict]`
    — 每对域调一次 LLM,产候选有向边;`complete` 可注入(测试 monkeypatch)
  - `quote_in_source(edge: dict, kb_root: Path) -> bool` — 闸1:`evidence.quote` 逐字为 `source_file` 子串

- [ ] **Step 1: 写失败测试(monkeypatch LLM,不打真实 API)**
```python
def test_data_flow_uses_injected_completer_and_marks_directed():
    prose = M.load_prose(M.Path(__file__).parent.joinpath("fixtures","sp6_prose"), ["PR","TR"])
    fake = lambda prompt, model: [{
        "source": "PR", "target": "TR", "relation": "measurements recorded in",
        "quote": "The tumor measurements obtained via the procedure are recorded in the TR dataset.",
        "confidence": 0.82,
    }]
    edges = M.extract_data_flow(prose, ["PR","TR"], model="x", complete=fake)
    assert edges and edges[0]["kind"] == "data_flow" and edges[0]["directed"] is True
    assert edges[0]["extractor"] == "llm"

def test_quote_in_source_gate():
    fix = M.Path(__file__).parent.joinpath("fixtures","sp6_prose")
    good = {"evidence": {"quote": "recorded in the TR dataset",
                         "source_file": "domains/PR/examples.md"}}
    bad  = {"evidence": {"quote": "THIS SENTENCE IS FABRICATED",
                         "source_file": "domains/PR/examples.md"}}
    assert M.quote_in_source(good, fix) is True
    assert M.quote_in_source(bad, fix) is False
```

- [ ] **Step 2: 运行,确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -k "data_flow or quote_in_source" -q`
Expected: FAIL

- [ ] **Step 3: 写实现**
```python
import json

_FLOW_PROMPT = """You are analyzing SDTM Implementation Guide prose for two domains.
Domain {A} text:
---
{TA}
---
Domain {B} text:
---
{TB}
---
Identify DIRECTED data-flow relations between {A} and {B} that the text SUPPORTS
(e.g. "{A} measurements are recorded in {B}"). For each, return an object:
{{"source": "<{A} or {B}>", "target": "<the other>", "relation": "<short phrase>",
  "quote": "<VERBATIM sentence copied exactly from the text above that supports it>",
  "confidence": <0..1>}}
Rules: quote MUST be copied verbatim from the text; if nothing is clearly supported,
return []. Return ONLY a JSON array."""


def _complete_json(prompt: str, model: str) -> list[dict]:
    import litellm
    resp = litellm.completion(model=model, temperature=0,
                              messages=[{"role": "user", "content": prompt}])
    txt = resp["choices"][0]["message"]["content"].strip()
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    try:
        data = json.loads(txt)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def extract_data_flow(prose: dict, domains: list[str], model: str,
                      complete=_complete_json) -> list[dict]:
    out: list[dict] = []
    doms = sorted(domains)
    for i, a in enumerate(doms):
        for b in doms[i + 1:]:
            ta = prose.get(a, {}).get("assumptions", "") + prose.get(a, {}).get("examples", "")
            tb = prose.get(b, {}).get("assumptions", "") + prose.get(b, {}).get("examples", "")
            if not ta or not tb:
                continue
            cands = complete(_FLOW_PROMPT.format(A=a, B=b, TA=ta[:6000], TB=tb[:6000]), model)
            for c in cands[:MAX_FLOW_PER_PAIR * 2]:
                s, t = c.get("source"), c.get("target")
                if {s, t} != {a, b}:
                    continue
                src_file = f"knowledge_base/domains/{s}/examples.md"
                out.append(_edge(s, t, "data_flow", True, c.get("relation", ""),
                                 c.get("quote", ""), src_file, 0,
                                 float(c.get("confidence", 0.0)), "llm", False))
    return out


def quote_in_source(edge: dict, kb_root: Path) -> bool:
    q = edge["evidence"]["quote"].strip()
    rel = edge["evidence"]["source_file"].replace("knowledge_base/", "")
    for kind in ("examples", "assumptions"):
        # try the declared file, then the sibling kind (LLM may misattribute)
        cand = kb_root / (rel if rel.endswith(".md") else rel)
        for p in {cand, cand.with_name(f"{kind}.md")}:
            if p.exists() and q and q in p.read_text(encoding="utf-8"):
                return True
    return False
```

- [ ] **Step 4: 运行,确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q`
Expected: PASS(6 passed)

- [ ] **Step 5: Commit**
```bash
git add scripts/mine_implicit_relations.py scripts/tests/test_mine_implicit_relations.py
git commit -m "feat(sp6): data-flow LLM extractor + verbatim-quote gate (gate 1)"
```

---

## Task 5: 闸 2 对抗核验 + 组装

**Files:**
- Modify: `scripts/mine_implicit_relations.py`, test 文件

**Interfaces:**
- Produces:
  - `verify_data_flow_edge(edge: dict, model: str, judge=_complete_json) -> dict` — 返回 `{"verified": bool, "note": str}`;对抗 prompt 让裁判尽力反驳
  - `build_implicit_relations(kb_root: Path, seeds: list[str], model: str, complete=_complete_json, judge=_complete_json) -> dict` — 跑全流程,数据流边过闸1+闸2,组装成 §4 JSON;被毙边进 `result["_rejected"]`

- [ ] **Step 1: 写失败测试(monkeypatch judge)**
```python
def test_verify_rejects_when_judge_refutes():
    edge = {"source":"PR","target":"TR","relation":"x",
            "evidence":{"quote":"q","source_file":"f"}}
    refute = lambda prompt, model: [{"refuted": True, "reason": "quote does not support direction"}]
    v = M.verify_data_flow_edge(edge, "x", judge=refute)
    assert v["verified"] is False and "support" in v["note"]

def test_build_assembles_and_gates(monkeypatch, tmp_path):
    fix = M.Path(__file__).parent.joinpath("fixtures","sp6_prose")
    flow = lambda prompt, model: [{"source":"PR","target":"TR","relation":"recorded in",
        "quote":"The tumor measurements obtained via the procedure are recorded in the TR dataset.",
        "confidence":0.82}]
    accept = lambda prompt, model: [{"refuted": False, "reason": "ok"}]
    res = M.build_implicit_relations(fix, ["PR","TU"], "x", complete=flow, judge=accept)
    kinds = {e["kind"] for e in res["edges"]}
    assert "data_flow" in kinds and "explicit_link" in kinds
    df = [e for e in res["edges"] if e["kind"]=="data_flow"]
    assert df and df[0]["verified"] is True     # 引文命中 + 裁判通过
    assert res["meta"]["confidence_threshold"] == M.CONF_THRESHOLD
```

- [ ] **Step 2: 运行,确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -k "verify or build_assembles" -q`
Expected: FAIL

- [ ] **Step 3: 写实现**
```python
_VERIFY_PROMPT = """A relation was extracted from SDTM IG prose:
  {S} --[{R}]--> {T}   (directed)
Supporting quote: "{Q}"
Try hard to REFUTE it. Does the quote actually support THIS directed relation
(right direction, right domains)? If uncertain, refute. Return ONLY:
[{{"refuted": <true|false>, "reason": "<short>"}}]"""


def verify_data_flow_edge(edge: dict, model: str, judge=_complete_json) -> dict:
    out = judge(_VERIFY_PROMPT.format(S=edge["source"], T=edge["target"],
                R=edge["relation"], Q=edge["evidence"]["quote"]), model)
    verdict = out[0] if out else {"refuted": True, "reason": "no verdict"}
    return {"verified": not bool(verdict.get("refuted", True)),
            "note": str(verdict.get("reason", ""))}


def build_implicit_relations(kb_root: Path, seeds: list[str], model: str,
                             complete=_complete_json, judge=_complete_json) -> dict:
    cluster = resolve_cluster(kb_root, seeds)
    prose = load_prose(kb_root, cluster)
    edges = extract_explicit_links(prose, cluster) + extract_cooccurrence(prose, cluster)
    rejected: list[dict] = []
    per_pair: dict[tuple, int] = {}
    for e in extract_data_flow(prose, cluster, model, complete=complete):
        if not quote_in_source(e, kb_root):
            e["verify_note"] = "gate1: quote not found in source"; rejected.append(e); continue
        v = verify_data_flow_edge(e, model, judge=judge)
        e["verified"], e["verify_note"] = v["verified"], v["note"]
        key = tuple(sorted((e["source"], e["target"])))
        if not v["verified"] or e["confidence"] < CONF_THRESHOLD \
           or per_pair.get(key, 0) >= MAX_FLOW_PER_PAIR:
            rejected.append(e); continue
        per_pair[key] = per_pair.get(key, 0) + 1
        edges.append(e)
    return {
        "meta": {"version": 1, "cluster_seeds": seeds, "domains": cluster,
                 "generated_from": "knowledge_base/domains/<D>/{assumptions,examples}.md",
                 "confidence_threshold": CONF_THRESHOLD},
        "edges": sorted(edges, key=lambda e: (e["kind"], e["source"], e["target"])),
        "_rejected": rejected,
    }
```

- [ ] **Step 4: 运行,确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q`
Expected: PASS(8 passed)

- [ ] **Step 5: Commit**
```bash
git add scripts/mine_implicit_relations.py scripts/tests/test_mine_implicit_relations.py
git commit -m "feat(sp6): adversarial verify (gate 2) + assembly with thresholds"
```

---

## Task 6: CLI + 产物 + 证据审计

**Files:**
- Modify: `scripts/mine_implicit_relations.py`

**Interfaces:**
- Produces:
  - `write_outputs(result: dict, out_json: Path, audit_md: Path, failures_dir: Path) -> None`
  - `main() -> None`(argparse:`--model`(默认 deepseek/deepseek-chat)、`--out`、`--dry-run`)

- [ ] **Step 1: 写实现(此任务产物是真实数据文件,验证靠真跑而非单测)**
```python
def write_outputs(result: dict, out_json: Path, audit_md: Path, failures_dir: Path) -> None:
    rejected = result.pop("_rejected", [])
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if rejected:
        failures_dir.mkdir(parents=True, exist_ok=True)
        (failures_dir / "sp6_rejected_edges.json").write_text(
            json.dumps(rejected, ensure_ascii=False, indent=2), encoding="utf-8")
    by_kind: dict[str, int] = {}
    for e in result["edges"]:
        by_kind[e["kind"]] = by_kind.get(e["kind"], 0) + 1
    lines = ["# SP6 隐性关系抽检 (Rule A)\n",
             f"> 生成: 见 git;域: {', '.join(result['meta']['domains'])}\n",
             f"边计数: {by_kind};被毙: {len(rejected)}\n\n## N=8 分层抽检\n",
             "| # | 边 | 类型 | 引文命中? | 关系/方向对? | 判定 |\n|--|--|--|--|--|--|\n"]
    sample = result["edges"][:8]
    for i, e in enumerate(sample, 1):
        lines.append(f"| {i} | {e['source']}→{e['target']} | {e['kind']} | 待核 | 待核 | 待填 |\n")
    audit_md.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    import argparse
    from dotenv import load_dotenv
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env")
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="deepseek/deepseek-chat")
    ap.add_argument("--out", default=str(root / "data" / "meta" / "implicit_relations.json"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    result = build_implicit_relations(KB_ROOT, SEEDS, args.model)
    n = len(result["edges"])
    if args.dry_run:
        print(f"[dry-run] {n} edges, {len(result['_rejected'])} rejected"); return
    write_outputs(result, Path(args.out),
                  root / "evidence" / "checkpoints" / "implicit_relations_audit.md",
                  root / "failures")
    print(f"wrote {args.out} ({n} edges)")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 全套测试 + lint/type**

Run: `.venv/bin/python -m pytest scripts/tests/test_mine_implicit_relations.py -q && ruff check scripts/mine_implicit_relations.py && mypy scripts/mine_implicit_relations.py`
Expected: PASS / no errors

- [ ] **Step 3: 真实跑一次(花 token,产出真实数据)**

Run: `.venv/bin/python scripts/mine_implicit_relations.py`
Expected: `wrote .../implicit_relations.json (N edges)`;打开 JSON 核对 PR/TR/RS/MI/TU 有边、每条 data_flow 有 quote。

- [ ] **Step 4: Rule A 人工抽检(Rule D 隔离)**

派**独立 subagent**逐条核对 `implicit_relations.json` 的 8 条抽样:引文是否逐字在源文件、有向关系方向是否对;把判定填进 `evidence/checkpoints/implicit_relations_audit.md`。任何 FAIL → 记录、调 prompt/阈值重跑。

- [ ] **Step 5: Commit**
```bash
git add scripts/mine_implicit_relations.py data/meta/implicit_relations.json evidence/checkpoints/implicit_relations_audit.md
git commit -m "feat(sp6): CLI + implicit_relations.json for tumor cluster + Rule A audit"
```

---

## Task 7: 查看器 — 内嵌两层边数据

**Files:**
- Modify: `scripts/build_kg_viewer.py`(`build_data()` + 模板 DATA 注入)

**Interfaces:**
- Consumes: `data/meta/implicit_relations.json`
- Produces: 内嵌 `DATA.implicit = {domains, edges}`;`build_data()` 新增读取(文件不存在则 `implicit=None`,查看器优雅降级)

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_build_kg_viewer.py`(新增):
```python
import json
from pathlib import Path
from scripts import build_kg_viewer as V

def test_build_data_includes_implicit(tmp_path, monkeypatch):
    fake = {"meta": {"domains": ["PR","TR"]},
            "edges": [{"source":"PR","target":"TR","kind":"data_flow","directed":True,
                       "relation":"x","confidence":0.8,"verified":True,
                       "evidence":{"quote":"q","source_file":"f","line":1}}]}
    p = V.ROOT / "data" / "meta" / "implicit_relations.json"
    existed = p.exists(); backup = p.read_text() if existed else None
    p.write_text(json.dumps(fake), encoding="utf-8")
    try:
        data = V.build_data()
        assert data["implicit"]["edges"][0]["kind"] == "data_flow"
    finally:
        if existed: p.write_text(backup)
        elif p.exists(): p.unlink()
```

- [ ] **Step 2: 运行,确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q`
Expected: FAIL(`KeyError: 'implicit'`)

- [ ] **Step 3: 写实现**

在 `build_kg_viewer.py` 的 `build_data()` return 前加:
```python
    impl_path = ROOT / "data" / "meta" / "implicit_relations.json"
    implicit = None
    if impl_path.exists():
        raw = json.loads(impl_path.read_text(encoding="utf-8"))
        implicit = {"domains": raw["meta"]["domains"],
                    "edges": [e for e in raw["edges"]]}  # 已含 evidence/confidence/kind
```
并在返回 dict 加一行 `"implicit": implicit,`。

- [ ] **Step 4: 运行,确认通过 + 再生成**

Run: `.venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q && .venv/bin/python scripts/build_kg_viewer.py`
Expected: PASS;`wrote .../kg_viewer.html`

- [ ] **Step 5: Commit**
```bash
git add scripts/build_kg_viewer.py scripts/tests/test_build_kg_viewer.py kg_viewer.html
git commit -m "feat(sp6): embed implicit_relations into viewer data (graceful if absent)"
```

---

## Task 8: 查看器 — explore 网状模式 + 两层边渲染

**Files:**
- Modify: `scripts/build_kg_viewer.py`(模板 JS/CSS)

**Interfaces:**
- Consumes: `DATA.implicit`
- Produces: JS 新增 `viewExplore(seed)`(增量展开)、`expandNode(id)`、边渲染按 `layer`(hard/flow/link/cooc)配线型 + `defs` 箭头 marker;新增图层开关 chips + 置信滑条(复用 Task 8 mockup 的样式常量)

> 注:UI 无法单测。验证方式 = 生成 + `python -m http.server` + 浏览器截图逐项核对(项目既有模式)。

- [ ] **Step 1: 加两层边样式 + 箭头 marker**

在 `<style>` 加(取自已验证 mockup 的配色):
```css
.iedge{fill:none}
.iedge.flow{stroke:var(--flow,#2a78d6);stroke-width:2.2}
.iedge.link{stroke:var(--link,#1baf7a);stroke-width:2.2;stroke-dasharray:5 3}
.iedge.cooc{stroke:var(--cooc,#7a52c7);stroke-width:2;stroke-dasharray:1 5;stroke-linecap:round}
```
在 `<svg>` 内 `<defs>` 加 `<marker id="arrow" ...>`(见 mockup 文件同名 marker)。

- [ ] **Step 2: 加 explore 视图构建器**

在 JS 视图构建区加:
```js
function vExplore(seed){
  const shown=new Set([seed]); window.__expanded=window.__expanded||new Set();
  window.__expanded.forEach(x=>shown.add(x));
  const nodes=[], edges=[], have=new Set();
  const add=(id,type,label,cls)=>{ if(!have.has(id)){have.add(id);nodes.push({id,type,label,cls,r:type==='domain'?12:9});}};
  for(const code of shown){ const d=domByCode.get(code); if(d)add('D:'+code,'domain',code,d.cls); }
  // 硬结构: RELATED_TO(curated) among shown
  for(const [s,list] of relBySrc) if(shown.has(s)) for(const r of list) if(shown.has(r.d)){
    add('D:'+r.d,'domain',r.d,(domByCode.get(r.d)||{}).cls); edges.push({s:'D:'+s,t:'D:'+r.d,layer:'hard'}); }
  // 推断层
  for(const e of (DATA.implicit?DATA.implicit.edges:[])) if(shown.has(e.source)&&shown.has(e.target)){
    const map={data_flow:'flow',explicit_link:'link',co_occurrence:'cooc'};
    edges.push({s:'D:'+e.source,t:'D:'+e.target,layer:map[e.kind],dir:e.directed,ev:e}); }
  return {nodes,edges,title:'explore · 从 '+seed+' 展开('+shown.size+' 域)'};
}
function expandNode(code){ (window.__expanded=window.__expanded||new Set()).add(code);
  for(const e of (DATA.implicit?DATA.implicit.edges:[])){ if(e.source===code)window.__expanded.add(e.target); if(e.target===code)window.__expanded.add(e.source); }
  cur.v='explore'; render(); }
```
在 `build()` 的边渲染:若 `e.layer` 属推断类,用 `<path class="iedge <layer>">` + 有向加 `marker-end`;硬边保持原 `.edge`。在节点 click(startDrag 的 moved<4 分支)对 explore 模式调 `expandNode(code)` 而非 openPanel(或面板里加"展开"按钮)。

- [ ] **Step 3: 加图层开关 + explore 入口按钮**

`#views` 加一个 `<button data-v="explore">网状探索</button>`;header 加 4 个图层 chip(id `#layers`),点击 toggle `document.querySelectorAll('.iedge.<layer>')` 的 display。`render()` 的 `cur.v==='explore'` 分支调 `vExplore(cur.dom||'TU')`。

- [ ] **Step 4: 生成 + 浏览器验证(截图)**

Run:
```bash
.venv/bin/python scripts/build_kg_viewer.py
.venv/bin/python -m http.server 8899 --bind 127.0.0.1 &
```
浏览器开 `http://127.0.0.1:8899/kg_viewer.html` → 点"网状探索" → 从 TU 展开 → **截图核对**:出现蓝箭头(数据流)/绿虚线(链接)/紫点线(共现);点节点继续展开;图层开关生效。关服务器 `pkill -f "http.server 8899"`。

- [ ] **Step 5: Commit**
```bash
git add scripts/build_kg_viewer.py kg_viewer.html
git commit -m "feat(sp6): viewer explore mode — click-to-expand network + two-layer edges"
```

---

## Task 9: 查看器 — 富节点混合详情 + RAG 按钮 + 边证据弹窗

**Files:**
- Modify: `scripts/build_kg_viewer.py`(模板 JS/CSS)

**Interfaces:**
- Consumes: `DATA`(域详情)、`DATA.implicit.edges`(边证据)、可选 `:8000/api/health`
- Produces: 面板新增"关系分层"区(硬/推断带标签+置信+✓)、"深入解释"按钮(探活后调 `/api/ask`)、点推断边弹证据框

- [ ] **Step 1: 富节点面板加"关系分层"**

在 `openPanel()` 的 domain 分支追加:遍历 `DATA.implicit.edges` 中 `source==code||target==code`,按 kind 分组渲染,带 `tag`(flow/link/cooc)+ `置信 e.confidence` + (e.verified?'✓':'') + `e.relation`;点某条 → `openEvidence(e)`。

- [ ] **Step 2: RAG 按钮 + 探活**
```js
let RAG_OK=false;
fetch('http://127.0.0.1:8000/api/health').then(r=>r.ok&&(RAG_OK=true)).catch(()=>{});
function ragExplain(a,b){ if(!RAG_OK)return;
  fetch('http://127.0.0.1:8000/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({question:`In SDTM, explain how domain ${a} relates to ${b} and why.`})})
   .then(r=>r.json()).then(d=>{ /* 把 d.answer 塞进面板 */ }); }
```
面板底部按钮仅当 `RAG_OK` 显示,否则隐藏(混合:离线也能用)。

- [ ] **Step 3: 边证据弹窗**
```js
function openEvidence(e){ const P=$('#panel');
  P.innerHTML='<div class="ph"><div><div class="pty">推断边 · '+e.kind+'</div><div class="pt">'+e.source+(e.directed?' → ':' — ')+e.target+'</div></div><button class="x" id="pClose">×</button></div>'
   +'<div class="kv">'+esc(e.relation||'')+'</div>'
   +'<div class="q">'+esc(e.evidence.quote)+'</div>'
   +'<div class="m">来源: '+esc(e.evidence.source_file)+':'+e.evidence.line+'</div>'
   +'<div class="m">置信 '+e.confidence+(e.verified?' · ✓ 已核验':' · 未核验')+'</div>'; P.classList.remove('hide'); }
```
加 `.q` CSS(左边框引用样式,同 mockup)。

- [ ] **Step 4: 生成 + 浏览器验证(截图)**

Run: 同 Task 8 起服务;点域节点看面板"关系分层";点一条推断边看证据弹窗(引文+来源+置信+核验);(若 :8000 在线)点"深入解释"看 RAG 回答。**截图留证**。

- [ ] **Step 5: Commit**
```bash
git add scripts/build_kg_viewer.py kg_viewer.html
git commit -m "feat(sp6): rich hybrid nodes — layered relations, RAG deep-explain, edge evidence"
```

---

## Self-Review

**Spec 覆盖**:定位/证据锚定→Task4-5(quote gate + verify);三类关系→Task2/3/4;试点簇→Task1 resolve_cluster + Task6 真跑;硬软分层→Task7(独立文件,不碰 meta.yaml);网状展开→Task8;富节点混合详情/RAG/边证据→Task9;Rule A/D→Task6 Step4;Rule B(失败归档)→Task5/6 `_rejected`→`failures/`。✅ 无遗漏。

**占位符扫描**:审计表模板的"待核/待填"是 Rule A 人工填的字段,非代码占位;其余步骤均有真实代码/命令。✅

**类型一致**:`_edge(...)` 字段与 §4 schema 一致;`extract_*` 返回 `list[dict]`;`build_implicit_relations` 用 `_rejected` 并在 `write_outputs` pop;viewer `DATA.implicit.edges[].kind ∈ {data_flow,explicit_link,co_occurrence}` 与 JS `map` 一致。✅

**风险**:LLM 抽取质量依赖 prompt——Task6 真跑后必过 Rule A,不达标就调 prompt/阈值重跑(spec §11 允许)。UI 任务靠截图验证(项目既有模式)。
