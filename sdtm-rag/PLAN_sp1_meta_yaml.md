# SP1 — `meta.yaml` 元数据层 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 用一个确定性脚本从只读 KB 自动生成一份机生成的 `data/meta/meta.yaml`（64 域结构化元数据），并用独立锚对账 + N=8 分层 Rule A 抽检验证它，作为 SP2/SP3 的硬前置数据层。

**Architecture:** `scripts/build_meta.py` 在已有的 `scripts/spec_loader.py`（SpecLoader）之上组装 per-domain dict（标量 + 变量 + ct 分流 + same_class + relations_curated + model_defhome + codelists），`yaml.safe_dump` 落 `data/meta/meta.yaml`，全程无 LLM。`scripts/reconcile_meta.py` **不复用** spec_loader，改从 `VARIABLE_INDEX.md`/`INDEX.md` 文本 + 裸 `Order:` grep（对条目数的第二独立锚，非第三个独立量）复现总数，与 meta.yaml 派生数对账（破生成器套套逻辑）。

**Tech Stack:** Python 3.11, `pyyaml`, `pytest`（测试在 `scripts/tests/`，`testpaths` 已配）。导入风格 `from scripts.spec_loader import SpecLoader`；KB 真路径 `Path(__file__).resolve().parents[5] / "knowledge_base"`。

---

## 设计来源 & 范围

- Spec: `branches/07_rag_kg/sdtm-rag/SP1_meta_yaml_design.md`（用户已批准 2026-06-16）。
- **范围 = 纯数据层**。不答题、不翻 eval、不碰 `server/structured_lookup.py`（退役那段 `len==6` 解析是 **SP2**）、不碰 `knowledge_base/`（只读）。
- **spec 路径校正**: spec §7 写的 `tests/test_build_meta.py` 实际应落 `scripts/tests/test_build_meta.py`（项目 `testpaths=["scripts/tests"]`）。本计划以此为准。

## File Structure（先锁分解）

| 文件 | 职责 | 动作 |
|------|------|------|
| `scripts/build_meta.py` | 生成器：KB → meta dict → `meta.yaml`。纯函数 + `main()` | Create |
| `scripts/reconcile_meta.py` | 独立锚对账器（不用 spec_loader） | Create |
| `scripts/tests/test_build_meta.py` | build_meta 单测 + reconcile 集成测 | Create |
| `data/meta/meta.yaml` | 生成产物（Task 7 起出现） | Generated |
| `evidence/checkpoints/sp1_meta_audit.md` | N=8 手检证据（Task 9） | Create（手写） |
| `branches/07_rag_kg/sdtm-rag/SP1_meta_yaml_design.md` | spec（已存在） | — |

每个 `build_meta` 子功能是一个纯函数 + 一个 TDD 任务，互相独立可测。

## 约定（每个 Task 都遵守）

- 导入：`from scripts.spec_loader import SpecLoader, VariableSpec, DomainSpec, Codelist`。
- 测试文件头部固定：

```python
from __future__ import annotations
from pathlib import Path
import pytest
from scripts.build_meta import (
    build_meta, _split_ct, _parse_label, _same_class_map,
    _relations_curated, _model_defhome, _codelists,
)

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"

@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT

@pytest.fixture(scope="module")
def meta(kb_root):
    return build_meta(kb_root)
```

- 跑测试：`cd branches/07_rag_kg/sdtm-rag && python -m pytest scripts/tests/test_build_meta.py -v`
- 每个 Task 末尾 commit；commit message 末行加 `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`。
- Rule B：任何失败 attempt 归 `failures/`，不删。

---

### Task 1: 脚手架 + 域标量（domain/class/label/structure + SUPPQUAL flag）

**Files:**
- Create: `scripts/build_meta.py`
- Test: `scripts/tests/test_build_meta.py`

- [ ] **Step 1: 写失败测试**（建测试文件，含上面"约定"的头部，再加）

```python
def test_domain_count_and_special_flag(meta):
    domains = {d["domain"]: d for d in meta["domains"]}
    # 64 个目录；缺 spec.md 的 DI 是桩域，只 63 个（含 SUPPQUAL）计入标准域
    assert len(domains) == 64
    assert sum(1 for d in meta["domains"] if d["counts_toward_63"]) == 63
    # DI 仅有 assumptions.md（无 spec.md/无变量）-> 桩域
    assert domains["DI"]["is_special"] is True
    assert domains["DI"]["counts_toward_63"] is False
    # SUPPQUAL 有完整 spec/assumptions/examples 且在 VARIABLE_INDEX 的 63 域内
    assert domains["SUPPQUAL"]["is_special"] is False
    assert domains["SUPPQUAL"]["counts_toward_63"] is True
    assert domains["AE"]["counts_toward_63"] is True

def test_domain_scalars(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    assert ae["class"] == "Events"
    assert ae["label"] == "Adverse Events"
    assert ae["structure"] == "One record per adverse event per subject"

def test_parse_label_unit():
    assert _parse_label("# AE — Adverse Events") == "Adverse Events"
    assert _parse_label("# LB — Laboratory Test Results") == "Laboratory Test Results"
    assert _parse_label("no title here") == ""
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'scripts.build_meta'`

- [ ] **Step 3: 写最小实现**（建 `scripts/build_meta.py`）

```python
"""Generate data/meta/meta.yaml — the SP1 deterministic metadata layer.

Builds a per-domain structured registry from the read-only knowledge base
(spec.md + Cross References + terminology + model). No LLM. Idempotent.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

from scripts.spec_loader import SpecLoader

# The 63 authoritative domains = directories WITH a spec.md (this includes
# SUPPQUAL, which has a full spec/assumptions/examples and appears in
# VARIABLE_INDEX). DI is the lone stub dir (assumptions.md only, no spec.md,
# no variables) -> not counted. So counts_toward_63 = (spec.md exists).

_LABEL_RE = re.compile(r"^#\s+\w+\s*—\s*(.+?)\s*$")


def _parse_label(h1_line: str) -> str:
    """Extract the domain label from the spec.md H1, e.g.
    '# AE — Adverse Events' -> 'Adverse Events'. Returns '' if not a title."""
    m = _LABEL_RE.match(h1_line)
    return m.group(1).strip() if m else ""


def _domain_label(kb_root: Path, domain: str) -> str:
    spec = kb_root / "domains" / domain / "spec.md"
    if not spec.exists():
        return ""
    for line in spec.read_text(encoding="utf-8").split("\n")[:3]:
        if line.startswith("# "):
            return _parse_label(line)
    return ""


def build_meta(kb_root: Path) -> dict:
    loader = SpecLoader(kb_root)
    domains_dir = kb_root / "domains"
    # Enumerate dirs directly (NOT loader.known_domains(), which skips DI for
    # lacking spec.md) so the stub domain DI is still represented.
    domains_out: list[dict] = []
    for domain_dir in sorted(p for p in domains_dir.iterdir() if p.is_dir()):
        name = domain_dir.name.upper()
        has_spec = (domain_dir / "spec.md").exists()
        ds = loader.get_domain(name)  # None when no spec.md (e.g. DI)
        domains_out.append(
            {
                "domain": name,
                "class": ds.domain_class if ds else "",
                "label": _domain_label(kb_root, name),
                "structure": ds.structure if ds else "",
                "is_special": not has_spec,        # DI = stub (no spec.md)
                "counts_toward_63": has_spec,      # 63 真域（含 SUPPQUAL）
            }
        )
    return {
        "meta_version": 1,
        "generated_from": "knowledge_base/",
        "domains": domains_out,
    }
```

- [ ] **Step 4: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS（3 个测试）

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task1: build_meta 域标量 + SUPPQUAL flag (TDD)"
```

---

### Task 2: 变量 + ct_codes/ct_dict 分流

**Files:**
- Modify: `scripts/build_meta.py`（给每个域加 `variables`）
- Test: `scripts/tests/test_build_meta.py`

- [ ] **Step 1: 写失败测试**

```python
def test_split_ct_unit():
    assert _split_ct("C66742") == (["C66742"], [])
    assert _split_ct("C85494; C128684; C128683") == (["C85494", "C128684", "C128683"], [])
    assert _split_ct("MedDRA") == ([], ["MedDRA"])
    assert _split_ct("ISO 8601 datetime or interval") == ([], ["ISO 8601 datetime or interval"])
    assert _split_ct("") == ([], [])

def test_variables_present_and_ct(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    by_name = {v["name"]: v for v in ae["variables"]}
    aeser = by_name["AESER"]
    assert aeser["role"] == "Record Qualifier"
    assert aeser["type"] == "Char"
    assert aeser["core"] == "Exp"
    assert aeser["label"] == "Serious Event"
    assert aeser["ct_codes"] == ["C66742"]
    assert aeser["ct_dict"] == []
    # STUDYID has no controlled terms
    assert by_name["STUDYID"]["ct_codes"] == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_split_ct_unit -v`
Expected: FAIL — `cannot import name '_split_ct'`

- [ ] **Step 3: 写实现**（在 `build_meta.py` 加 `_split_ct`，并在 `build_meta` 的域 dict 里加 `variables`）

```python
_CT_CODE_RE = re.compile(r"^C\d+$")


def _split_ct(controlled_terms: str) -> tuple[list[str], list[str]]:
    """Split a spec.md 'Controlled Terms' field into (C-codes, dict-tokens).
    Values are '; '-separated: a token is a CDISC C-code (^C\\d+$) or an
    external-dictionary/format token (MedDRA, LOINC, ISO 8601 ..., etc.)."""
    ct_codes: list[str] = []
    ct_dict: list[str] = []
    for tok in (t.strip() for t in controlled_terms.split(";")):
        if not tok:
            continue
        (ct_codes if _CT_CODE_RE.match(tok) else ct_dict).append(tok)
    return ct_codes, ct_dict


def _variables(ds) -> list[dict]:
    out: list[dict] = []
    for v in ds.variables:
        ct_codes, ct_dict = _split_ct(v.controlled_terms)
        out.append(
            {
                "name": v.name,
                "label": v.label,
                "role": v.role,
                "type": v.var_type,
                "core": v.core,
                "ct_codes": ct_codes,
                "ct_dict": ct_dict,
            }
        )
    return out
```

在 `build_meta` 的域 dict 里追加一行：`"variables": _variables(ds),`

- [ ] **Step 4: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS（含新 2 个）

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task2: 变量 + ct_codes/ct_dict 分流 (TDD)"
```

---

### Task 3: `same_class`（按 Class group-by，确定性完整）

**Files:**
- Modify: `scripts/build_meta.py`
- Test: `scripts/tests/test_build_meta.py`

- [ ] **Step 1: 写失败测试**

```python
def test_same_class(meta):
    by_name = {d["domain"]: d for d in meta["domains"]}
    ae_sib = set(by_name["AE"]["same_class"])
    # 策划 bullet 列的 Events 兄弟必须都在（group-by 是完整真源）
    assert {"BE", "CE", "DS", "DV", "HO", "MH"} <= ae_sib
    assert "AE" not in ae_sib                      # 不含自己
    assert all(by_name[s]["class"] == "Events" for s in ae_sib)  # 同类
    assert "AE" in by_name["BE"]["same_class"]     # 对称
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_same_class -v`
Expected: FAIL — `KeyError: 'same_class'`

- [ ] **Step 3: 写实现**（加 `_same_class_map`，在 `build_meta` 里调用并写入每个域）

```python
def _same_class_map(domains_out: list[dict]) -> dict[str, list[str]]:
    """Group domains by class; same_class[d] = sorted siblings (excl. self).
    Deterministic and COMPLETE (the curated 'Same class' prose may omit some)."""
    by_class: dict[str, list[str]] = defaultdict(list)
    for d in domains_out:
        if d["class"]:
            by_class[d["class"]].append(d["domain"])
    result: dict[str, list[str]] = {}
    for d in domains_out:
        sibs = [x for x in by_class.get(d["class"], []) if x != d["domain"]]
        result[d["domain"]] = sorted(sibs)
    return result
```

在 `build_meta` 里，构造完 `domains_out`（含 class）后、return 前：

```python
    sc = _same_class_map(domains_out)
    for d in domains_out:
        d["same_class"] = sc[d["domain"]]
```

- [ ] **Step 4: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task3: same_class 按 Class group-by (TDD)"
```

---

### Task 4: `relations_curated`（解析 Related Domains 跨类边，机制仅字面）

**Files:**
- Modify: `scripts/build_meta.py`
- Test: `scripts/tests/test_build_meta.py`

- [ ] **Step 1: 写失败测试**

```python
def test_relations_curated(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    rels = {r["target"]: r for r in ae["relations_curated"]}
    # CM/PR 字面写了 "via RELREC"
    assert rels["CM"]["category"] == "Treatment"
    assert rels["CM"]["mechanism"] == "RELREC"
    assert rels["PR"]["mechanism"] == "RELREC"
    # FA 无机制词 -> null（None）
    assert rels["FA"]["category"] == "Findings About"
    assert rels["FA"]["mechanism"] is None
    # 全部标记来源
    assert all(r["fidelity"] == "curated_prose" for r in ae["relations_curated"])
    # "Same class" bullet（无链接）不应混进来
    assert "BE" not in rels
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_relations_curated -v`
Expected: FAIL — `KeyError: 'relations_curated'`

- [ ] **Step 3: 写实现**（加 `_relations_curated`，在 `build_meta` 写入每个域）

```python
# 跨类策划边: "- **Treatment:** [CM](../CM/) — concomitant ... via RELREC"
# 必须有 [link]，从而排除无链接的 "**Same class (X):**" bullet。
_REL_RE = re.compile(
    r"^- \*\*(?P<cat>[^:]+):\*\*\s*\[(?P<tgt>[A-Z0-9]+)\]\([^)]*\)\s*[—-]\s*(?P<note>.*)$"
)
# 机制只在散文字面出现时才填，否则 None。
_MECH_RE = re.compile(r"\b(RELREC|RELSPEC|RELSUB|SUPPQUAL|SUPP)\b")


def _relations_curated(kb_root: Path, domain: str) -> list[dict]:
    spec = kb_root / "domains" / domain / "spec.md"
    if not spec.exists():
        return []
    lines = spec.read_text(encoding="utf-8").split("\n")
    # 只在 "### Related Domains" 小节内扫
    out: list[dict] = []
    in_section = False
    for line in lines:
        if line.startswith("### Related Domains"):
            in_section = True
            continue
        if in_section and line.startswith("### "):
            break
        if not in_section:
            continue
        m = _REL_RE.match(line)
        if not m:
            continue
        note = m.group("note").strip()
        mech = _MECH_RE.search(note)
        out.append(
            {
                "target": m.group("tgt"),
                "category": m.group("cat").strip(),
                "mechanism": mech.group(1) if mech else None,
                "note": note,
                "fidelity": "curated_prose",
            }
        )
    return out
```

在 `build_meta` 里：`d["relations_curated"] = _relations_curated(kb_root, d["domain"])`（在已知 domain 后）。

- [ ] **Step 4: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task4: relations_curated 机制仅字面 (TDD)"
```

---

### Task 5: `model_defhome`（复刻 `len==6` 判别器，退役依据）

**Files:**
- Modify: `scripts/build_meta.py`
- Test: `scripts/tests/test_build_meta.py`

> 复刻 `server/structured_lookup.py::_build_model_defhome_index` 的逻辑（6 列定义表判别器 + 单 home + 排除 `--`），**只产数据**，不碰那个文件。

- [ ] **Step 1: 写失败测试**

```python
def test_model_defhome(meta):
    mdh = meta["model_defhome"]
    assert mdh["RDOMAIN"] == "model/06_relationship_datasets.md"
    assert "EPOCH" in mdh                       # 单 home 变量在
    assert "DOMAIN" not in mdh                  # 跨多文件 -> 丢弃
    assert "USUBJID" not in mdh
    assert not any(k.startswith("--") for k in mdh)  # 排除 -- 前缀
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_model_defhome -v`
Expected: FAIL — `KeyError: 'model_defhome'`

- [ ] **Step 3: 写实现**（加 `_model_defhome`，在 `build_meta` 顶层写入）

```python
def _model_defhome(kb_root: Path) -> dict[str, str]:
    """var -> model/*.md definition home. The 6-col definition table
    `| # | VAR | Label | Type | Role | Notes |` is isolated by len(inner)==6
    (the 5-col usage table's last cell is Role, not Notes). Keep only vars whose
    Notes-bearing 6-col rows live in EXACTLY ONE file; drop generic '--' vars."""
    model_dir = kb_root / "model"
    if not model_dir.exists():
        return {}
    tmp: dict[str, set[str]] = defaultdict(set)
    for f in sorted(model_dir.glob("*.md")):
        rel = f.relative_to(kb_root).as_posix()
        for raw in f.read_text(encoding="utf-8").splitlines():
            if "|" not in raw:
                continue
            cells = [c.strip() for c in raw.split("|")]
            inner = cells[1:-1]
            if len(inner) != 6:
                continue  # load-bearing discriminator (do NOT relax)
            num, var, _label, _type, _role, notes = inner
            if not num.isdigit():
                continue
            if not re.fullmatch(r"(?:--)?[A-Z][A-Z0-9]*", var):
                continue
            if not notes:
                continue
            tmp[var].add(rel)
    return {
        var: next(iter(files))
        for var, files in sorted(tmp.items())
        if len(files) == 1 and not var.startswith("--")
    }
```

在 `build_meta` 的 return dict 里加：`"model_defhome": _model_defhome(kb_root),`

- [ ] **Step 4: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task5: model_defhome 复刻 len==6 判别器 (TDD)"
```

---

### Task 6: `codelists`（遍历 terminology：code/name/extensible/term_count/termfile）

**Files:**
- Modify: `scripts/build_meta.py`
- Test: `scripts/tests/test_build_meta.py`

- [ ] **Step 1: 写失败测试**

```python
def test_codelists(meta):
    cls = {c["ct_code"]: c for c in meta["codelists"]}
    assert len(meta["codelists"]) == 1005
    c = cls["C66742"]
    assert c["name"] == "No Yes Response"
    assert c["extensible"] is False
    assert c["term_count"] == 2                 # N, Y
    assert c["termfile"] == "terminology/core/general_part4.md"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_codelists -v`
Expected: FAIL — `KeyError: 'codelists'`

- [ ] **Step 3: 写实现**（加 `_codelists`；复用 SpecLoader 解析的 codelist 数据 + 自建 code→termfile 文件映射）

```python
_CL_HEADING_RE = re.compile(r"^##\s+(.+?)\s*\(([Cc]\d+)\)")


def _codelist_files(kb_root: Path) -> dict[str, str]:
    """ct_code -> kb-relative termfile path (first file whose heading defines it)."""
    out: dict[str, str] = {}
    term_dir = kb_root / "terminology"
    if not term_dir.exists():
        return out
    for f in sorted(term_dir.rglob("*.md")):
        rel = f.relative_to(kb_root).as_posix()
        for line in f.read_text(encoding="utf-8").splitlines():
            m = _CL_HEADING_RE.match(line)
            if m:
                out.setdefault(m.group(2).upper(), rel)
    return out


def _codelists(kb_root: Path) -> list[dict]:
    loader = SpecLoader(kb_root)
    files = _codelist_files(kb_root)
    out: list[dict] = []
    for code, cl in sorted(loader.codelists.items()):
        out.append(
            {
                "ct_code": code,
                "name": cl.name,
                "extensible": cl.extensible,
                "term_count": len(cl.submission_values),
                "termfile": files.get(code, ""),
            }
        )
    return out
```

在 `build_meta` 的 return dict 里加：`"codelists": _codelists(kb_root),`

> 注：term 全表（37939 个 term 文本）**不材化**，只存 `term_count`。

- [ ] **Step 4: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task6: codelists 遍历 terminology + termfile (TDD)"
```

---

### Task 7: 落盘 `meta.yaml` + 幂等 + CLI

**Files:**
- Modify: `scripts/build_meta.py`（加 `main()` 写盘）
- Create: `data/meta/meta.yaml`（运行产物）
- Test: `scripts/tests/test_build_meta.py`

- [ ] **Step 1: 写失败测试**

```python
def test_idempotent_and_keys(meta, kb_root):
    again = build_meta(kb_root)
    assert meta == again                         # 同输入同输出
    assert set(meta.keys()) == {
        "meta_version", "generated_from", "domains", "model_defhome", "codelists",
    }
    d0 = meta["domains"][0]
    assert set(d0.keys()) == {
        "domain", "class", "label", "structure", "is_special",
        "counts_toward_63", "variables", "same_class", "relations_curated",
    }

def test_yaml_roundtrip_stable(tmp_path, kb_root):
    import yaml
    from scripts.build_meta import dump_meta
    m = build_meta(kb_root)
    p = tmp_path / "meta.yaml"
    dump_meta(m, p)
    a = p.read_bytes()
    dump_meta(m, p)
    b = p.read_bytes()
    assert a == b                                # 落盘字节稳定
    assert yaml.safe_load(p.read_text()) == m    # 可往返
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_yaml_roundtrip_stable -v`
Expected: FAIL — `cannot import name 'dump_meta'`

- [ ] **Step 3: 写实现**（在 `build_meta.py` 末尾加 `dump_meta` + `main`）

```python
def dump_meta(meta: dict, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        yaml.safe_dump(meta, sort_keys=True, allow_unicode=True, width=1000),
        encoding="utf-8",
    )


def main() -> None:
    # scripts -> sdtm-rag -> 07_rag_kg -> branches -> sdtm-pedia
    kb_root = Path(__file__).resolve().parents[4] / "knowledge_base"
    out = Path(__file__).resolve().parents[1] / "data" / "meta" / "meta.yaml"
    meta = build_meta(kb_root)
    dump_meta(meta, out)
    print(f"wrote {out} ({len(meta['domains'])} domains, "
          f"{len(meta['codelists'])} codelists)")


if __name__ == "__main__":
    main()
```

> 路径核对：`scripts/build_meta.py` → `parents[1]`=sdtm-rag、`parents[2]`=07_rag_kg、`parents[3]`=branches、`parents[4]`=sdtm-pedia。**实现时若 `main()` 的 kb_root 路径算错会在 Step 4 暴露**，按实际层级修正（KB 真路径 = `…/sdtm-pedia/knowledge_base`）。

- [ ] **Step 4: 跑测试 + 真生成**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS（全部）
Run: `python -m scripts.build_meta`
Expected: 打印 `wrote .../data/meta/meta.yaml (64 domains, 1005 codelists)`，文件生成。

- [ ] **Step 5: commit**

```bash
git add scripts/build_meta.py scripts/tests/test_build_meta.py data/meta/meta.yaml
git commit -m "SP1 Task7: 落盘 meta.yaml + 幂等 + CLI (TDD)"
```

---

### Task 8: `reconcile_meta.py` — 独立锚对账（破套套逻辑）

**Files:**
- Create: `scripts/reconcile_meta.py`
- Test: `scripts/tests/test_build_meta.py`

> **关键**：对账器**不导入 spec_loader / build_meta 的解析**，只读 meta.yaml（待验对象）+ 从 `VARIABLE_INDEX.md`/`INDEX.md` 文本独立复现 + 裸 `Order:` grep（条目数的第二独立锚）。anchor 正则 drift 必须 loud-fail（命名 anchor + 文件），不可 opaque 崩。

- [ ] **Step 1: 写失败测试**

```python
def test_reconcile_all_pass(kb_root, tmp_path):
    from scripts.build_meta import dump_meta
    from scripts.reconcile_meta import reconcile
    m = build_meta(kb_root)
    p = tmp_path / "meta.yaml"
    dump_meta(m, p)
    report = reconcile(p, kb_root)
    failed = [c for c in report if not c["ok"]]
    assert failed == [], f"reconcile mismatches: {failed}"
    checks = {c["check"]: c for c in report}
    assert checks["domains_counts_toward_63"]["expected"] == 63
    assert checks["variable_entries_total"]["expected"] == 1917
    assert checks["unique_variable_names"]["expected"] == 1523
    assert checks["codelists_total"]["expected"] == 1005
    assert checks["terms_total"]["expected"] == 37939
    assert checks["TAETORD_domain_count"]["expected"] == 43
    assert checks["VISITDY_domain_count"]["expected"] == 36
    assert checks["raw_order_line_count"]["expected"] == 1917  # 条目数第二独立锚(裸 grep vs header)
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_build_meta.py::test_reconcile_all_pass -v`
Expected: FAIL — `No module named 'scripts.reconcile_meta'`

- [ ] **Step 3: 写实现**（建 `scripts/reconcile_meta.py`）

```python
"""Independent-anchor reconciliation for data/meta/meta.yaml.

Does NOT reuse spec_loader / build_meta parsing — re-derives authoritative
totals from VARIABLE_INDEX.md / INDEX.md text + a third raw Order-line count,
to break the tautology trap. Exit 1 on any mismatch.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


def _meta_derived(meta: dict) -> dict:
    domains = meta["domains"]
    all_var_names: list[str] = []
    taetord = visitdy = 0
    for d in domains:
        names = [v["name"] for v in d["variables"]]
        all_var_names.extend(names)
        if "TAETORD" in names:
            taetord += 1
        if "VISITDY" in names:
            visitdy += 1
    return {
        "domains_counts_toward_63": sum(1 for d in domains if d["counts_toward_63"]),
        "variable_entries_total": len(all_var_names),
        "unique_variable_names": len(set(all_var_names)),
        "codelists_total": len(meta["codelists"]),
        "terms_total": sum(c["term_count"] for c in meta["codelists"]),
        "TAETORD_domain_count": taetord,
        "VISITDY_domain_count": visitdy,
    }


def _anchors(kb_root: Path) -> dict:
    vidx = (kb_root / "VARIABLE_INDEX.md").read_text(encoding="utf-8")
    index = (kb_root / "INDEX.md").read_text(encoding="utf-8")

    hdr = re.search(r"唯一变量数:\s*(\d+)\s*\|\s*条目总数:\s*(\d+)\s*\|\s*覆盖域:\s*(\d+)", vidx)
    uniq, entries, _cov = (int(hdr.group(i)) for i in (1, 2, 3))

    def _domain_count(var: str) -> int:
        m = re.search(rf"^\|\s*{var}\s*\|\s*(\d+)\s*\|", vidx, re.MULTILINE)
        return int(m.group(1))

    cl = re.search(r"\(([\d,]+)\s*codelists,\s*([\d,]+)\s*terms\)", index)
    codelists = int(cl.group(1).replace(",", ""))
    terms = int(cl.group(2).replace(",", ""))

    # 第三独立源：裸数 spec.md 的 '- **Order:**' 行
    order_re = re.compile(r"^- \*\*Order:\*\*", re.MULTILINE)
    raw_order = sum(
        len(order_re.findall(p.read_text(encoding="utf-8")))
        for p in sorted((kb_root / "domains").glob("*/spec.md"))
    )
    return {
        "domains_counts_toward_63": 63,
        "variable_entries_total": entries,
        "unique_variable_names": uniq,
        "codelists_total": codelists,
        "terms_total": terms,
        "TAETORD_domain_count": _domain_count("TAETORD"),
        "VISITDY_domain_count": _domain_count("VISITDY"),
        "raw_order_line_count": raw_order,
    }


def reconcile(meta_path: Path, kb_root: Path) -> list[dict]:
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    derived = _meta_derived(meta)
    anchors = _anchors(kb_root)
    # raw_order 是第三源，和 entries 对的是同一个量（meta 的 variable_entries_total）
    derived["raw_order_line_count"] = derived["variable_entries_total"]
    report: list[dict] = []
    for check, expected in anchors.items():
        actual = derived.get(check)
        report.append(
            {"check": check, "expected": expected, "actual": actual,
             "ok": actual == expected}
        )
    return report


def main() -> None:
    here = Path(__file__).resolve()
    kb_root = here.parents[4] / "knowledge_base"   # scripts->sdtm-rag->07_rag_kg->branches->sdtm-pedia
    meta_path = here.parents[1] / "data" / "meta" / "meta.yaml"
    report = reconcile(meta_path, kb_root)
    for c in report:
        flag = "OK " if c["ok"] else "FAIL"
        print(f"[{flag}] {c['check']}: expected={c['expected']} actual={c['actual']}")
    if any(not c["ok"] for c in report):
        sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: 跑测试 + 真对账**

Run: `python -m pytest scripts/tests/test_build_meta.py -v`
Expected: PASS（全部）
Run: `python -m scripts.reconcile_meta`
Expected: 每行 `[OK ]`，退出码 0。
> 若某行 `FAIL`：**不要改 meta 去迁就锚**，先查是 meta.yaml 错还是 VARIABLE_INDEX/INDEX 漂移（2026-04-16 生成，可能过期）；失败 attempt 归 `failures/`。

- [ ] **Step 5: commit**

```bash
git add scripts/reconcile_meta.py scripts/tests/test_build_meta.py
git commit -m "SP1 Task8: 独立锚对账 reconcile_meta (破套套逻辑, TDD)"
```

---

### Task 9: N=8 分层 Rule A 手检 + Rule D 异 type 代码审

> 非代码任务。两件：① 手工语义抽检（Rule A）② 审阅隔离（Rule D）。

- [ ] **Step 1: 选定 8 个分层样本**（写进 evidence 文件头）

8 槽：1) tiny 域 `TE` 2) tiny 域 `TD` 3) medium `VS` 4) large `LB` 5) 特殊目的 `DM` 6) 关系域 `RELREC` 7) 特殊结构 `SUPPQUAL`（验 is_special + 变量收录）8) ct 多码变量一例（在 meta.yaml 搜含 2+ `ct_codes` 的变量）。

- [ ] **Step 2: 逐槽手核**，对照打开 `data/meta/meta.yaml` 条目 ↔ KB 源（`knowledge_base/domains/<D>/spec.md` / `terminology/*.md`），逐字段（role/type/core/ct_codes/label）+ same_class + relations_curated（确认 mechanism 没臆造）。每槽记 PASS/FAIL + 证据行。

- [ ] **Step 3: 写证据**（`evidence/checkpoints/sp1_meta_audit.md`，含 8 槽结果 + Gate 1 reconcile 输出粘贴 + 任何发现）。Rule A 要求 N 写进计划（=8）、证据留档——本步即兑现。

- [ ] **Step 4: Rule D 代码审（审阅隔离）** — 派 **异 `subagent_type`** 独立审 `build_meta.py` + `reconcile_meta.py`（建议 `oh-my-claudecode:code-reviewer` 或 `feature-dev:code-reviewer`，**不可**同 context 自审）。重点：reconcile 是否真独立于生成器解析（套套逻辑）、relations mechanism 是否只字面、`len==6` 复刻是否忠实、幂等 sort_keys 是否稳。findings 全处理。

- [ ] **Step 5: commit**

```bash
git add evidence/checkpoints/sp1_meta_audit.md
git commit -m "SP1 Task9: N=8 Rule A 手检 + Rule D 异 type 代码审证据"
```

---

## Self-Review（写计划后对 spec 逐条核）

- **Spec coverage**: §3 schema 全字段 → Task1(标量)/2(变量+ct)/3(same_class)/4(relations_curated)/5(model_defhome)/6(codelists)；§3 开放细节 a(SUPPQUAL flag)→T1、b(ct_dict)→T2、c(单文件)→T7、d(model_defhome)→T5、e(反向索引不落盘)→设计如此未建任务✅；§5 Gate1 独立锚→T8、Gate2 N=8→T9、Rule D→T9 Step4、Rule B→约定+T8 Step4 注；§7 交付物全覆盖；§8 YAGNI（不材化反向索引/37939 term/不碰 structured_lookup/不碰 KB）→各 Task 注明遵守。
- **Placeholder scan**: 无 TBD/TODO；每个 code step 给完整代码；`main()` 路径层级显式标注并约定 Step4 暴露即修。
- **Type consistency**: `build_meta`/`dump_meta`/`reconcile` 签名跨 Task 一致；`_split_ct` 返回 `(list,list)` T2 定义 T2 用；meta dict 顶层 key 集合 T7 测试与 T1/5/6 写入一致（meta_version/generated_from/domains/model_defhome/codelists）；域 dict key 集合 T7 测试与 T1-4 写入一致。
- **已知风险**: T7 `main()` kb_root 相对层级、T6 `term_count==2`（C66742）、T1 `64 域`——若真实 KB 与 grounding 有出入，对应 Step4 测试会立即暴露，按实际修正（不改锚迁就）。

## Execution Handoff（见计划末，待用户选执行方式）
