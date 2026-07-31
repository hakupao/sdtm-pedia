# Study RAG 确定性轨 (st01) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 st01 研究的 EDC ConfigurationReport (xlsx) 确定性地解析为 field catalog → field card markdown → 独立 chroma collection `study_st01`, 并用 golden questions 做检索评测, 中间经过 pilot → schema 冻结闸门。

**Architecture:** 零 LLM 的确定性管线 (openpyxl 解析 + 模板渲染), 全程机器可校验 (覆盖台账孤儿行=0); 产物全部落在 gitignore 的 `sdtm-rag/data/study/` 下; 复用现有 `RAGEngine` / `run_eval.py`, 只加 collection/kb-root 参数, 不动服务端 (联邦路由是 Plan B)。

**Tech Stack:** Python 3 (sdtm-rag venv), openpyxl, chromadb, litellm (text-embedding-3-small), pytest。

**Roadmap 上下文:** 本计划是 spec `docs/superpowers/specs/2026-07-31-study-rag-design.md` 的第一步。Plan B (服务端 multi-collection 路由 + webchat 开关) 与 Plan C (有损轨: protocol/workflow PDF → markdown 小批次) 在本计划 schema 冻结后另行编写。

## Global Constraints

- **红线 (spec §6)**: 真实研究名/真实字段数据**绝不进 git**。进 git 的只有: 代码、合成假数据的测试、纯统计的 evidence。真名只存在于 `source/study/` 与 `sdtm-rag/data/study/studies.local.yaml` (两者均 gitignore)。
- 研究一律以代号 `st01` 指代; collection 名 `study_st01`。
- 测试 fixture 一律用合成假数据 (FAKEFORM/FAKEITEM 等), 绝不从真实 xlsx 复制值。
- 确定性轨零 LLM: parser 与渲染不调用任何模型; embedding 仅在 ingest 步骤调用。
- 每个 commit 前执行 `git diff --cached | grep -ci <真实研究名>` 必须为 0 (执行者在本地用真名检查, 计划文档中不写出该名字)。
- 工作目录: 所有命令在 `/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag` 下执行; python/pytest 用 `.venv/bin/`。
- xlsx 事实 (已实测): 关键 sheet 三行表头 (行1 sheet名 / 行2 分组·空白需前向填充 / 行3 列名), 数据从行 4 起。`Items and Groups` 56 列 ~1091 行, `Code lists` 5 列 ~2401 行, `Forms` 15 列 ~26 行。新版报告是抜粋 (7 sheets), 旧版全量 (26 sheets, 多出 `Data checks`/`Functions and Conditions` 明细)。
- 失败 attempt 按规则 B 归档到 `sdtm-rag/failures/` (已有目录惯例); 归档内容同样不得含真名。

---

### Task 1: 数据目录红线 + 本地 study 注册表

**Files:**
- Modify: `sdtm-rag/.gitignore`
- Create (本地, 不进 git): `sdtm-rag/data/study/studies.local.yaml`, `sdtm-rag/data/study/st01/` 目录骨架

**Interfaces:**
- Produces: gitignore 规则 `data/study/`; 注册表 yaml 格式 (Task 2 的 `paths.py` 消费)。

- [ ] **Step 1: 加 gitignore 规则**

在 `sdtm-rag/.gitignore` 的 `data/uploads/` 行后追加:

```
data/study/
```

- [ ] **Step 2: 创建本地目录与注册表**

```bash
mkdir -p data/study/st01/cards data/study/st01/eval
```

创建 `data/study/studies.local.yaml` (**本地文件, 执行者把 `<...>` 占位替换为 `source/study/` 下的真实目录名与文件名**):

```yaml
st01:
  version_label_new: "V59"
  version_label_old: "V58"
  source_dir: "../source/study/<真实目录名>"        # 相对 sdtm-pedia 仓库根
  config_report_new: "<新版ConfigurationReport文件名>.xlsx"
  config_report_old: "<旧版ConfigurationReport文件名>.xlsx"
  demo_export: "<DEMO导出文件名>.xlsx"
```

- [ ] **Step 3: 验证红线生效**

```bash
git check-ignore data/study/studies.local.yaml && echo IGNORED
git status --short   # 应只显示 .gitignore 被修改
```

Expected: 输出 `IGNORED`; status 只有 `.gitignore`。

- [ ] **Step 4: Commit**

```bash
git add .gitignore
git commit -m "chore(study-rag): gitignore data/study/ — st01 本地数据红线"
```

---

### Task 2: openpyxl 依赖 + scripts/study 包 + 路径解析器

**Files:**
- Modify: `sdtm-rag/pyproject.toml` (dependencies 列表)
- Create: `sdtm-rag/scripts/study/__init__.py` (空文件), `sdtm-rag/scripts/study/paths.py`
- Test: `sdtm-rag/scripts/tests/test_study_paths.py`

**Interfaces:**
- Produces: `resolve_study(study_id: str, registry_path: Path | None = None) -> StudyPaths`; dataclass `StudyPaths(study_id, version_label_new, version_label_old, config_report_new: Path, config_report_old: Path | None, demo_export: Path | None, out_dir: Path, cards_dir: Path)`。后续所有 task 经它取路径。

- [ ] **Step 1: 加依赖**

`pyproject.toml` 的 `dependencies` 中 (pyyaml 行附近) 追加:

```toml
    "openpyxl>=3.1",
```

```bash
.venv/bin/pip install -e . --quiet && .venv/bin/python -c "import openpyxl; print(openpyxl.__version__)"
```

- [ ] **Step 2: 写失败测试**

`scripts/tests/test_study_paths.py`:

```python
from pathlib import Path

import pytest
import yaml

from scripts.study.paths import StudyPaths, resolve_study


def _write_registry(tmp_path: Path) -> Path:
    src = tmp_path / "src_study"
    src.mkdir()
    (src / "new.xlsx").touch()
    (src / "old.xlsx").touch()
    reg = tmp_path / "studies.local.yaml"
    reg.write_text(yaml.safe_dump({
        "st01": {
            "version_label_new": "VNEW",
            "version_label_old": "VOLD",
            "source_dir": str(src),
            "config_report_new": "new.xlsx",
            "config_report_old": "old.xlsx",
            "demo_export": None,
        }
    }), encoding="utf-8")
    return reg


def test_resolve_study_returns_paths(tmp_path):
    reg = _write_registry(tmp_path)
    sp = resolve_study("st01", registry_path=reg)
    assert isinstance(sp, StudyPaths)
    assert sp.config_report_new.name == "new.xlsx" and sp.config_report_new.exists()
    assert sp.config_report_old is not None and sp.config_report_old.exists()
    assert sp.demo_export is None
    assert sp.out_dir.name == "st01"
    assert sp.cards_dir == sp.out_dir / "cards"


def test_resolve_study_unknown_id_raises(tmp_path):
    reg = _write_registry(tmp_path)
    with pytest.raises(KeyError):
        resolve_study("st99", registry_path=reg)


def test_resolve_study_missing_file_raises(tmp_path):
    reg = _write_registry(tmp_path)
    data = yaml.safe_load(reg.read_text())
    data["st01"]["config_report_new"] = "absent.xlsx"
    reg.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(FileNotFoundError):
        resolve_study("st01", registry_path=reg)
```

- [ ] **Step 3: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_study_paths.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'scripts.study'`。

- [ ] **Step 4: 实现 paths.py**

`scripts/study/paths.py`:

```python
"""st01 研究路径解析: 真名只存在于本地 studies.local.yaml, 代码只认代号."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

SDTM_RAG_ROOT = Path(__file__).resolve().parent.parent.parent
STUDY_DATA_ROOT = SDTM_RAG_ROOT / "data" / "study"
DEFAULT_REGISTRY = STUDY_DATA_ROOT / "studies.local.yaml"


@dataclass(frozen=True)
class StudyPaths:
    study_id: str
    version_label_new: str
    version_label_old: str | None
    config_report_new: Path
    config_report_old: Path | None
    demo_export: Path | None
    out_dir: Path
    cards_dir: Path


def resolve_study(study_id: str, registry_path: Path | None = None) -> StudyPaths:
    reg_path = registry_path or DEFAULT_REGISTRY
    if not reg_path.exists():
        raise FileNotFoundError(f"study registry not found: {reg_path}")
    registry = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
    if study_id not in registry:
        raise KeyError(f"unknown study_id: {study_id} (known: {sorted(registry)})")
    ent = registry[study_id]
    source_dir = Path(ent["source_dir"])
    if not source_dir.is_absolute():
        source_dir = (reg_path.parent / source_dir).resolve()

    def _file(key: str, required: bool) -> Path | None:
        name = ent.get(key)
        if not name:
            if required:
                raise KeyError(f"{study_id}: registry missing required key {key}")
            return None
        p = source_dir / name
        if not p.exists():
            raise FileNotFoundError(f"{study_id}: {key} not found: {p}")
        return p

    out_dir = (registry_path.parent if registry_path else STUDY_DATA_ROOT) / study_id
    return StudyPaths(
        study_id=study_id,
        version_label_new=ent["version_label_new"],
        version_label_old=ent.get("version_label_old"),
        config_report_new=_file("config_report_new", required=True),
        config_report_old=_file("config_report_old", required=False),
        demo_export=_file("demo_export", required=False),
        out_dir=out_dir,
        cards_dir=out_dir / "cards",
    )
```

注意: `source_dir` 相对路径以注册表所在目录为基准 (真实注册表在 `data/study/`, 故写 `../../../source/study/<名>`; Task 1 模板按此更正 — 执行时以 `git check-ignore` + 实际解析成功为准)。

- [ ] **Step 5: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_study_paths.py -v
```

Expected: 3 passed。

- [ ] **Step 6: 真实注册表冒烟 (本地)**

```bash
.venv/bin/python -c "from scripts.study.paths import resolve_study; sp = resolve_study('st01'); print(sp.study_id, sp.config_report_new.exists(), sp.version_label_new)"
```

Expected: `st01 True V59`。若 source_dir 相对层级不对, 修正 `data/study/studies.local.yaml` (本地文件) 直到通过。

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml scripts/study/__init__.py scripts/study/paths.py scripts/tests/test_study_paths.py
git commit -m "feat(study-rag): scripts/study 包 + st01 路径解析器 (真名仅存本地注册表)"
```

---

### Task 3: 三行表头通用 sheet 读取器

**Files:**
- Create: `sdtm-rag/scripts/study/parse_config_report.py`
- Test: `sdtm-rag/scripts/tests/study_fixtures.py`, `sdtm-rag/scripts/tests/test_parse_config_report.py`

**Interfaces:**
- Produces: `read_sheet_records(ws) -> list[dict[str, object]]` — key 为 `"<分组>::<列名>"`, 分组空白前向填充; 每条记录附 `"_row": int` (1-based xlsx 行号, 溯源用)。空行跳过。
- Produces (fixture): `build_config_report(path: Path, *, items_rows: list[tuple] | None = None) -> Path` — 合成假 workbook, 后续所有 parser 测试复用。

- [ ] **Step 1: 写合成 fixture builder**

`scripts/tests/study_fixtures.py` (**全部假数据, 结构仿真实 3 行表头**):

```python
"""合成 ConfigurationReport fixture — 结构仿真, 数据全假 (红线: 不得复制真实值)."""
from pathlib import Path

import openpyxl

FORMS_HEADER = [
    ("General", "Id"), ("General", "Name"), ("General", "Summary format"),
    ("General", "Description"), ("General", "In use"),
]
ITEMS_HEADER = [
    ("Type and container", "Form ID"), ("Type and container", "Form Name"),
    ("Type and container", "Field type"), ("Type and container", "Item group ID"),
    ("Type and container", "Item group name"),
    ("Validation", "Item ID"), ("Validation", "Data type"),
    ("Validation", "Required field"), ("Validation", "Minimum length"),
    ("Validation", "Max length"), ("Validation", "Data checks"),
    ("Validation", "System checks"),
    ("General", "Field label"), ("General", "Control Type"),
    ("General", "Choices"), ("General", "Measurement Unit"),
    ("General", "Description"), ("General", "Instructions for user"),
    ("Visibility", "Show on simple condition"),
    ("Output", "Output Field ID"), ("Output", "Output Field Label"),
]
CODELIST_HEADER = [
    ("Code lists", "OID"), ("Code lists", "Format name"),
    ("Code lists", "Data Type"), ("Code lists", "Code value"),
    ("Code lists", "Code text"),
]

DEFAULT_ITEMS = [
    ("FAKEFORM1", "偽フォーム一", "Item group", "FG1", "グループ甲",
     "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
    ("FAKEFORM1", "偽フォーム一", "Item", "FG1", "",
     "FAKEIT1", "integer", "X", "1", "", "DC01", "", "偽項目ラベル一", "Radio buttons",
     "CL_FAKE1", "", "", "", "", "OUT1", "出力一"),
    ("FAKEFORM1", "偽フォーム一", "Item", "FG1", "",
     "FAKEIT2", "text", "", "", "200", "", "SC01", "偽項目ラベル二", "Text box",
     "", "kg", "説明テキスト", "入力指示", "COND1", "", ""),
    ("FAKEFORM2", "偽フォーム二", "Item", "FG2", "グループ乙",
     "FAKEIT3", "date", "X", "", "", "", "", "偽日付項目", "Date picker",
     "", "", "", "", "", "", ""),
]
DEFAULT_FORMS = [
    ("FAKEFORM1", "偽フォーム一", "{FAKEIT1}", "", "2"),
    ("FAKEFORM2", "偽フォーム二", "", "説明", "1"),
]
DEFAULT_CODELISTS = [
    ("CL_FAKE1", "", "integer", "1", "偽選択肢はい"),
    ("CL_FAKE1", "", "integer", "0", "偽選択肢いいえ"),
    ("CL_UNUSED", "", "text", "A", "未参照リスト"),
]


def _write_sheet(wb, title: str, header: list[tuple], rows: list[tuple]) -> None:
    ws = wb.create_sheet(title)
    ws.append([title] * len(header))                       # 行1: sheet 名
    sections = [s for s, _ in header]
    ws.append([s if i == 0 or sections[i - 1] != s else "" # 行2: 分组, 重复留空
               for i, s in enumerate(sections)])
    ws.append([c for _, c in header])                       # 行3: 列名
    for r in rows:
        ws.append(list(r))


def build_config_report(path: Path, *, items_rows=None, forms_rows=None,
                        codelist_rows=None) -> Path:
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    _write_sheet(wb, "Forms", FORMS_HEADER, forms_rows or DEFAULT_FORMS)
    _write_sheet(wb, "Items and Groups", ITEMS_HEADER, items_rows or DEFAULT_ITEMS)
    _write_sheet(wb, "Code lists", CODELIST_HEADER, codelist_rows or DEFAULT_CODELISTS)
    wb.save(path)
    return path
```

- [ ] **Step 2: 写失败测试**

`scripts/tests/test_parse_config_report.py`:

```python
from pathlib import Path

import openpyxl
import pytest

from scripts.tests.study_fixtures import build_config_report
from scripts.study.parse_config_report import read_sheet_records


@pytest.fixture()
def report(tmp_path) -> Path:
    return build_config_report(tmp_path / "fake_report.xlsx")


def test_read_sheet_records_keys_and_forward_fill(report):
    wb = openpyxl.load_workbook(report, read_only=True)
    recs = read_sheet_records(wb["Items and Groups"])
    assert len(recs) == 4
    first = recs[0]
    assert first["Type and container::Form ID"] == "FAKEFORM1"
    # 分组前向填充: 第 2 列同属 Type and container
    assert first["Type and container::Form Name"] == "偽フォーム一"
    assert recs[1]["Validation::Item ID"] == "FAKEIT1"
    assert recs[1]["General::Choices"] == "CL_FAKE1"


def test_read_sheet_records_row_numbers(report):
    wb = openpyxl.load_workbook(report, read_only=True)
    recs = read_sheet_records(wb["Items and Groups"])
    assert recs[0]["_row"] == 4          # 数据从 xlsx 行 4 起
    assert recs[3]["_row"] == 7


def test_read_sheet_records_skips_blank_rows(tmp_path):
    p = build_config_report(tmp_path / "r.xlsx",
                            items_rows=[("", "") + ("",) * 19])
    wb = openpyxl.load_workbook(p, read_only=True)
    assert read_sheet_records(wb["Items and Groups"]) == []
```

- [ ] **Step 3: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_parse_config_report.py -v
```

Expected: FAIL — `ModuleNotFoundError` / `ImportError: read_sheet_records`。

- [ ] **Step 4: 实现 read_sheet_records**

`scripts/study/parse_config_report.py`:

```python
"""ConfigurationReport (Viedoc 导出 xlsx) 确定性解析器. 零 LLM."""
from __future__ import annotations

from typing import Any


def _cell(v: Any) -> str:
    return "" if v is None else str(v).strip()


def read_sheet_records(ws) -> list[dict[str, Any]]:
    """三行表头 (sheet名/分组/列名) → [{'分组::列名': str, '_row': int}]; 全空行跳过."""
    rows = ws.iter_rows(values_only=True)
    next(rows)                                   # 行1: sheet 名, 丢弃
    sections_raw = next(rows)
    colnames = next(rows)
    keys: list[str] = []
    cur = ""
    for s, c in zip(sections_raw, colnames):
        if _cell(s):
            cur = _cell(s)
        keys.append(f"{cur}::{_cell(c)}")
    records: list[dict[str, Any]] = []
    for i, row in enumerate(rows, start=4):
        values = [_cell(v) for v in row[: len(keys)]]
        if not any(values):
            continue
        rec: dict[str, Any] = dict(zip(keys, values))
        rec["_row"] = i
        records.append(rec)
    return records
```

- [ ] **Step 5: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_parse_config_report.py -v
```

Expected: 3 passed。

- [ ] **Step 6: Commit**

```bash
git add scripts/study/parse_config_report.py scripts/tests/study_fixtures.py scripts/tests/test_parse_config_report.py
git commit -m "feat(study-rag): 三行表头 sheet 读取器 + 合成 fixture (零真实数据)"
```

---

### Task 4: Forms / Items / Codelists 结构化解析

**Files:**
- Modify: `sdtm-rag/scripts/study/parse_config_report.py`
- Test: `sdtm-rag/scripts/tests/test_parse_config_report.py` (追加)

**Interfaces:**
- Produces:
  - `@dataclass FormDef(oid, name, summary_format, description, in_use, row)`
  - `@dataclass ItemRow(row, form_oid, form_name, row_type, group_oid, group_name, item_oid, data_type, required: bool, min_length, max_length, data_checks, system_checks, label, control_type, choices, unit, description, instructions, visible_condition, output_field_id, output_field_label, raw: dict)`
  - `@dataclass Codelist(oid, data_type, entries: list[tuple[str, str]])`
  - `parse_forms(path) -> list[FormDef]` / `parse_items(path) -> list[ItemRow]` / `parse_codelists(path) -> dict[str, Codelist]`
- Consumes: Task 3 的 `read_sheet_records`。

- [ ] **Step 1: 写失败测试 (追加到 test_parse_config_report.py)**

```python
from scripts.study.parse_config_report import (
    parse_codelists, parse_forms, parse_items,
)


def test_parse_forms(report):
    forms = parse_forms(report)
    assert [f.oid for f in forms] == ["FAKEFORM1", "FAKEFORM2"]
    assert forms[0].name == "偽フォーム一"


def test_parse_items_types_and_fields(report):
    items = parse_items(report)
    assert [r.row_type for r in items] == ["Item group", "Item", "Item", "Item"]
    it1 = items[1]
    assert (it1.form_oid, it1.item_oid, it1.data_type) == ("FAKEFORM1", "FAKEIT1", "integer")
    assert it1.required is True
    assert it1.choices == "CL_FAKE1"
    assert it1.label == "偽項目ラベル一"
    assert items[2].required is False
    assert items[2].visible_condition == "COND1"
    # group 行继承上下文: group_name 在后续 Item 行为空, 保留原值即可
    assert items[0].group_name == "グループ甲"
    # raw 保留全部列 (不丢信息)
    assert it1.raw["Output::Output Field ID"] == "OUT1"


def test_parse_codelists_grouping(report):
    cls = parse_codelists(report)
    assert set(cls) == {"CL_FAKE1", "CL_UNUSED"}
    assert cls["CL_FAKE1"].entries == [("1", "偽選択肢はい"), ("0", "偽選択肢いいえ")]
    assert cls["CL_FAKE1"].data_type == "integer"


def test_parse_items_missing_column_raises(tmp_path):
    import openpyxl as _o
    p = tmp_path / "bad.xlsx"
    wb = _o.Workbook(); ws = wb.active; ws.title = "Items and Groups"
    ws.append(["Items and Groups"] * 2)
    ws.append(["Type and container", ""])
    ws.append(["Form ID", "Form Name"])
    ws.append(["F1", "n1"])
    wb.save(p)
    with pytest.raises(KeyError, match="Validation::Item ID"):
        parse_items(p)
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_parse_config_report.py -v
```

Expected: 新增 4 个 FAIL (ImportError)。

- [ ] **Step 3: 实现三个 parser (追加到 parse_config_report.py)**

```python
from dataclasses import dataclass, field
from pathlib import Path

import openpyxl


@dataclass(frozen=True)
class FormDef:
    oid: str
    name: str
    summary_format: str
    description: str
    in_use: str
    row: int


@dataclass(frozen=True)
class ItemRow:
    row: int
    form_oid: str
    form_name: str
    row_type: str          # 'Item group' | 'Item'
    group_oid: str
    group_name: str
    item_oid: str
    data_type: str
    required: bool
    min_length: str
    max_length: str
    data_checks: str
    system_checks: str
    label: str
    control_type: str
    choices: str
    unit: str
    description: str
    instructions: str
    visible_condition: str
    output_field_id: str
    output_field_label: str
    raw: dict = field(repr=False)


@dataclass(frozen=True)
class Codelist:
    oid: str
    data_type: str
    entries: list


def _req(rec: dict, key: str) -> str:
    if key not in rec:
        raise KeyError(f"{key} (available: {sorted(k for k in rec if k != '_row')[:8]}...)")
    return rec[key]


def parse_forms(path: Path) -> list[FormDef]:
    wb = openpyxl.load_workbook(path, read_only=True)
    return [
        FormDef(
            oid=_req(r, "General::Id"), name=r.get("General::Name", ""),
            summary_format=r.get("General::Summary format", ""),
            description=r.get("General::Description", ""),
            in_use=r.get("General::In use", ""), row=r["_row"],
        )
        for r in read_sheet_records(wb["Forms"])
    ]


def parse_items(path: Path) -> list[ItemRow]:
    wb = openpyxl.load_workbook(path, read_only=True)
    out: list[ItemRow] = []
    for r in read_sheet_records(wb["Items and Groups"]):
        out.append(ItemRow(
            row=r["_row"],
            form_oid=_req(r, "Type and container::Form ID"),
            form_name=r.get("Type and container::Form Name", ""),
            row_type=r.get("Type and container::Field type", ""),
            group_oid=r.get("Type and container::Item group ID", ""),
            group_name=r.get("Type and container::Item group name", ""),
            item_oid=_req(r, "Validation::Item ID"),
            data_type=r.get("Validation::Data type", ""),
            required=r.get("Validation::Required field", "") == "X",
            min_length=r.get("Validation::Minimum length", ""),
            max_length=r.get("Validation::Max length", ""),
            data_checks=r.get("Validation::Data checks", ""),
            system_checks=r.get("Validation::System checks", ""),
            label=r.get("General::Field label", ""),
            control_type=r.get("General::Control Type", ""),
            choices=r.get("General::Choices", ""),
            unit=r.get("General::Measurement Unit", ""),
            description=r.get("General::Description", ""),
            instructions=r.get("General::Instructions for user", ""),
            visible_condition=r.get("Visibility::Show on simple condition", ""),
            output_field_id=r.get("Output::Output Field ID", ""),
            output_field_label=r.get("Output::Output Field Label", ""),
            raw={k: v for k, v in r.items() if k != "_row"},
        ))
    return out


def parse_codelists(path: Path) -> dict[str, Codelist]:
    wb = openpyxl.load_workbook(path, read_only=True)
    grouped: dict[str, Codelist] = {}
    for r in read_sheet_records(wb["Code lists"]):
        oid = _req(r, "Code lists::OID")
        cl = grouped.setdefault(
            oid, Codelist(oid=oid, data_type=r.get("Code lists::Data Type", ""), entries=[])
        )
        cl.entries.append((r.get("Code lists::Code value", ""), r.get("Code lists::Code text", "")))
    return grouped
```

注意 `_req` 对 `Validation::Item ID` 的强制: fixture 的 group 行该列为空字符串 (列存在), 缺列才报错 — 与测试语义一致。

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_parse_config_report.py -v
```

Expected: 7 passed。

- [ ] **Step 5: 真实文件冒烟 (本地, 输出只看统计)**

```bash
.venv/bin/python -c "
from scripts.study.paths import resolve_study
from scripts.study.parse_config_report import parse_forms, parse_items, parse_codelists
sp = resolve_study('st01')
f, i, c = parse_forms(sp.config_report_new), parse_items(sp.config_report_new), parse_codelists(sp.config_report_new)
items = [r for r in i if r.row_type == 'Item']
print('forms:', len(f), '| rows:', len(i), '| items:', len(items), '| codelists:', len(c))
print('labelled:', sum(1 for r in items if r.label), '| with-choices:', sum(1 for r in items if r.choices))
"
```

Expected: 无异常; forms ≈ 23, rows ≈ 1088。若真实表头与假设不符 (KeyError), 修 parser 或 fixture 后重跑测试 — **不得**改成绕过列名。

- [ ] **Step 6: Commit**

```bash
git add scripts/study/parse_config_report.py scripts/tests/test_parse_config_report.py
git commit -m "feat(study-rag): Forms/Items/Codelists 结构化解析 (56 列保全于 raw)"
```

---

### Task 5: catalog 组装 + 覆盖台账 + 新旧版 diff

**Files:**
- Create: `sdtm-rag/scripts/study/build_catalog.py`
- Test: `sdtm-rag/scripts/tests/test_build_catalog.py`

**Interfaces:**
- Consumes: Task 4 的 parser 与 dataclass; Task 2 的 `StudyPaths`。
- Produces:
  - `build_catalog(sp: StudyPaths) -> dict` — keys: `study, version_new, version_old, forms: list[dict], items: list[dict], codelists: dict, diffs: dict[item_oid, list[str]], new_items: list[str], removed_items: list[str], ledger: list[dict]`
  - `write_catalog(catalog: dict, out_dir: Path) -> None` — 写 `catalog.json` + `coverage_ledger.csv`
  - 台账行: `{"sheet": str, "row": int, "status": "mapped"|"unreferenced", "target": str}`; **孤儿 (无 target) 直接 raise**。
  - CLI: `python -m scripts.study.build_catalog --study st01`

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_build_catalog.py`:

```python
import csv
import json
from pathlib import Path

import pytest

from scripts.tests.study_fixtures import build_config_report
from scripts.study.build_catalog import build_catalog, write_catalog
from scripts.study.paths import StudyPaths


@pytest.fixture()
def sp(tmp_path) -> StudyPaths:
    new = build_config_report(tmp_path / "new.xlsx")
    old_items = [
        # FAKEIT1 在旧版 label 不同 → diff; FAKEIT3 不存在 → new_items; FAKEOLD 只在旧版 → removed
        ("FAKEFORM1", "偽フォーム一", "Item", "FG1", "",
         "FAKEIT1", "integer", "X", "1", "", "DC01", "", "旧ラベル一", "Radio buttons",
         "CL_FAKE1", "", "", "", "", "OUT1", "出力一"),
        ("FAKEFORM1", "偽フォーム一", "Item", "FG1", "",
         "FAKEIT2", "text", "", "", "200", "", "SC01", "偽項目ラベル二", "Text box",
         "", "kg", "説明テキスト", "入力指示", "COND1", "", ""),
        ("FAKEFORM1", "偽フォーム一", "Item", "FG1", "",
         "FAKEOLD", "text", "", "", "", "", "", "旧のみ項目", "Text box",
         "", "", "", "", "", "", ""),
    ]
    old = build_config_report(tmp_path / "old.xlsx", items_rows=old_items)
    out = tmp_path / "st01"
    return StudyPaths(
        study_id="st01", version_label_new="VNEW", version_label_old="VOLD",
        config_report_new=new, config_report_old=old, demo_export=None,
        out_dir=out, cards_dir=out / "cards",
    )


def test_build_catalog_core(sp):
    cat = build_catalog(sp)
    assert cat["study"] == "st01" and cat["version_new"] == "VNEW"
    assert [f["oid"] for f in cat["forms"]] == ["FAKEFORM1", "FAKEFORM2"]
    item_oids = [i["item_oid"] for i in cat["items"]]
    assert item_oids == ["FAKEIT1", "FAKEIT2", "FAKEIT3"]   # 只含 Item 行
    assert cat["new_items"] == ["FAKEIT3"]
    assert cat["removed_items"] == ["FAKEOLD"]
    assert any("旧ラベル一" in d for d in cat["diffs"]["FAKEIT1"])
    # group 上下文折进 item
    assert cat["items"][0]["group_name"] == "グループ甲"


def test_ledger_full_coverage(sp):
    cat = build_catalog(sp)
    by_status = {}
    for row in cat["ledger"]:
        by_status.setdefault(row["status"], []).append(row)
    # 新版报告所有数据行都有落点; 未被引用的 codelist 标 unreferenced
    assert all(r["target"] for r in cat["ledger"])
    assert any(r["target"] == "codelist:CL_UNUSED" for r in by_status["unreferenced"])
    mapped_targets = [r["target"] for r in by_status["mapped"]]
    assert "card:st01__FAKEFORM1__FAKEIT1" in mapped_targets
    assert "form:FAKEFORM1" in mapped_targets
    assert "group:FAKEFORM1/FG1" in mapped_targets


def test_write_catalog_outputs(sp, tmp_path):
    cat = build_catalog(sp)
    write_catalog(cat, sp.out_dir)
    data = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    assert data["study"] == "st01"
    with (sp.out_dir / "coverage_ledger.csv").open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert {"sheet", "row", "status", "target"} <= set(rows[0])
    assert len(rows) == len(cat["ledger"])
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_build_catalog.py -v
```

Expected: FAIL (ModuleNotFoundError)。

- [ ] **Step 3: 实现 build_catalog.py**

```python
"""catalog 组装 + 覆盖台账 (孤儿=0 强制) + 新旧版 diff. 零 LLM."""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict
from pathlib import Path

from scripts.study.parse_config_report import (
    ItemRow, parse_codelists, parse_forms, parse_items,
)
from scripts.study.paths import StudyPaths, resolve_study

_DIFF_FIELDS = ("data_type", "required", "label", "choices", "data_checks",
                "system_checks", "min_length", "max_length", "control_type")


def _diff_items(new: dict[str, ItemRow], old: dict[str, ItemRow]):
    diffs: dict[str, list[str]] = {}
    for oid in new.keys() & old.keys():
        changes = [
            f"{f}: {getattr(old[oid], f)} → {getattr(new[oid], f)}"
            for f in _DIFF_FIELDS if getattr(old[oid], f) != getattr(new[oid], f)
        ]
        if changes:
            diffs[oid] = changes
    return (diffs, sorted(new.keys() - old.keys()), sorted(old.keys() - new.keys()))


def build_catalog(sp: StudyPaths) -> dict:
    forms = parse_forms(sp.config_report_new)
    rows = parse_items(sp.config_report_new)
    codelists = parse_codelists(sp.config_report_new)
    items = [r for r in rows if r.row_type == "Item"]
    groups = {(r.form_oid, r.group_oid): r for r in rows if r.row_type == "Item group"}

    old_index: dict[str, ItemRow] = {}
    if sp.config_report_old is not None:
        old_index = {r.item_oid: r
                     for r in parse_items(sp.config_report_old) if r.row_type == "Item"}
    diffs, new_items, removed = _diff_items({r.item_oid: r for r in items}, old_index) \
        if old_index else ({}, [], [])

    referenced = {r.choices for r in items if r.choices}
    ledger: list[dict] = []
    for f in forms:
        ledger.append({"sheet": "Forms", "row": f.row, "status": "mapped",
                       "target": f"form:{f.oid}"})
    for r in rows:
        if r.row_type == "Item":
            target = f"card:{sp.study_id}__{r.form_oid}__{r.item_oid}"
        elif r.row_type == "Item group":
            target = f"group:{r.form_oid}/{r.group_oid}"
        else:
            raise ValueError(f"orphan row {r.row} in Items and Groups: "
                             f"unknown Field type {r.row_type!r}")
        ledger.append({"sheet": "Items and Groups", "row": r.row,
                       "status": "mapped", "target": target})
    for oid, cl in codelists.items():
        status = "mapped" if oid in referenced else "unreferenced"
        for i, _ in enumerate(cl.entries):
            ledger.append({"sheet": "Code lists", "row": -1 if i else 0,
                           "status": status, "target": f"codelist:{oid}"})

    item_dicts = []
    for r in items:
        d = asdict(r)
        if not r.group_name:  # group 名折进 item (group 行携带)
            g = groups.get((r.form_oid, r.group_oid))
            d["group_name"] = g.group_name if g else ""
        item_dicts.append(d)

    return {
        "study": sp.study_id,
        "version_new": sp.version_label_new,
        "version_old": sp.version_label_old,
        "forms": [asdict(f) for f in forms],
        "items": item_dicts,
        "codelists": {oid: {"data_type": c.data_type, "entries": c.entries}
                      for oid, c in codelists.items()},
        "diffs": diffs, "new_items": new_items, "removed_items": removed,
        "ledger": ledger,
    }


def write_catalog(catalog: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=1), encoding="utf-8")
    with (out_dir / "coverage_ledger.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["sheet", "row", "status", "target"])
        w.writeheader()
        w.writerows(catalog["ledger"])


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    cat = build_catalog(sp)
    write_catalog(cat, sp.out_dir)
    n_status: dict[str, int] = {}
    for r in cat["ledger"]:
        n_status[r["status"]] = n_status.get(r["status"], 0) + 1
    print(f"forms={len(cat['forms'])} items={len(cat['items'])} "
          f"codelists={len(cat['codelists'])} diffs={len(cat['diffs'])} "
          f"new={len(cat['new_items'])} removed={len(cat['removed_items'])} "
          f"ledger={n_status}")


if __name__ == "__main__":
    main()
```

Code lists 台账注: 逐 entry 记行会翻倍文件且 entry 无独立行号语义, 故每 codelist 首 entry 记 `row=0`、后续 `-1` 占位——若执行时觉得别扭, 可改为每 codelist 一行 (`row` 取首个 entry 的 `_row`); 测试只约束 target/status, 两种实现均可过。

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_build_catalog.py -v
```

Expected: 3 passed。

- [ ] **Step 5: 真实数据全量跑 (本地)**

```bash
.venv/bin/python -m scripts.study.build_catalog --study st01
ls data/study/st01/
```

Expected: 打印统计 (items ≈ 700-900, diffs/new/removed 为若干); 生成 `catalog.json` + `coverage_ledger.csv`; **无 orphan 异常**。若真实数据出现未知 `Field type` 值 → 这是台账机制在工作: 补映射规则再跑, 失败记录归档 `failures/study_catalog_attempt_1.md` (不含真名)。

- [ ] **Step 6: Commit**

```bash
git add scripts/study/build_catalog.py scripts/tests/test_build_catalog.py
git commit -m "feat(study-rag): catalog 组装 + 覆盖台账 (孤儿即抛错) + 新旧版 diff"
```

---

### Task 6: DEMO 导出实例值采样

**Files:**
- Create: `sdtm-rag/scripts/study/parse_demo.py`
- Test: `sdtm-rag/scripts/tests/test_parse_demo.py`

**Interfaces:**
- Consumes: `StudyPaths.demo_export`。
- Produces: `sample_demo_values(demo_path: Path, known_item_oids: set[str], max_per_item: int = 5) -> tuple[dict[str, list[str]], list[str]]` — 返回 (item_oid → 去重实例值列表, 未匹配列名列表)。
- **结构假设 (pilot 验证项)**: DEMO 导出的每个 form sheet 首行为列头, 部分列头与 Item OID 一致; `README`/`Items`/`CodeLists` sheet 跳过。假设不成立时在 pilot (Task 8) 修正。

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_parse_demo.py`:

```python
from pathlib import Path

import openpyxl
import pytest

from scripts.study.parse_demo import sample_demo_values


@pytest.fixture()
def demo(tmp_path) -> Path:
    p = tmp_path / "fake_demo.xlsx"
    wb = openpyxl.Workbook()
    wb.active.title = "README"
    ws = wb.create_sheet("FAKEFORM1")
    ws.append(["SubjectId", "FAKEIT1", "FAKEIT2"])
    for r in [("S1", 1, "値甲"), ("S2", 0, "値乙"), ("S3", 1, ""), ("S4", 1, "値甲")]:
        ws.append(r)
    wb.create_sheet("Items")     # 字典 sheet, 应跳过
    wb.save(p)
    return p


def test_sample_demo_values(demo):
    samples, unmatched = sample_demo_values(demo, {"FAKEIT1", "FAKEIT2", "FAKEIT3"})
    assert samples["FAKEIT1"] == ["1", "0"]          # 去重保序
    assert samples["FAKEIT2"] == ["値甲", "値乙"]     # 空值跳过
    assert "FAKEIT3" not in samples                   # DEMO 里没有的项目不出现
    assert unmatched == ["SubjectId"]                 # 非 OID 列记录在案


def test_max_per_item(demo):
    samples, _ = sample_demo_values(demo, {"FAKEIT1"}, max_per_item=1)
    assert samples["FAKEIT1"] == ["1"]
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_parse_demo.py -v
```

Expected: FAIL (ModuleNotFoundError)。

- [ ] **Step 3: 实现 parse_demo.py**

```python
"""DEMO 导出 xlsx → item 实例值采样 (去重保序, 空值跳过). 零 LLM."""
from __future__ import annotations

from pathlib import Path

import openpyxl

_SKIP_SHEETS = {"README", "Items", "CodeLists"}


def sample_demo_values(
    demo_path: Path, known_item_oids: set[str], max_per_item: int = 5,
) -> tuple[dict[str, list[str]], list[str]]:
    wb = openpyxl.load_workbook(demo_path, read_only=True)
    samples: dict[str, list[str]] = {}
    unmatched: list[str] = []
    for ws in wb.worksheets:
        if ws.title in _SKIP_SHEETS:
            continue
        rows = ws.iter_rows(values_only=True)
        header = [str(c) if c is not None else "" for c in next(rows, [])]
        col_oids: list[str | None] = []
        for name in header:
            if name in known_item_oids:
                col_oids.append(name)
            else:
                if name:
                    unmatched.append(name)
                col_oids.append(None)
        for row in rows:
            for oid, v in zip(col_oids, row):
                if oid is None or v is None or str(v).strip() == "":
                    continue
                bucket = samples.setdefault(oid, [])
                sv = str(v).strip()
                if sv not in bucket and len(bucket) < max_per_item:
                    bucket.append(sv)
    return samples, sorted(set(unmatched))
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_parse_demo.py -v
```

Expected: 2 passed。

- [ ] **Step 5: 真实 DEMO 冒烟 (本地, 只看统计)**

```bash
.venv/bin/python -c "
import json
from scripts.study.paths import resolve_study
from scripts.study.parse_demo import sample_demo_values
sp = resolve_study('st01')
cat = json.loads((sp.out_dir / 'catalog.json').read_text(encoding='utf-8'))
oids = {i['item_oid'] for i in cat['items']}
samples, unmatched = sample_demo_values(sp.demo_export, oids)
print('matched-items:', len(samples), '/', len(oids), '| unmatched-cols:', len(unmatched))
"
```

Expected: matched-items 显著 > 0。若为 0 → 列头≠OID 的结构假设不成立, 记入 Task 8 pilot 待修清单, 不阻塞本 task。

- [ ] **Step 6: Commit**

```bash
git add scripts/study/parse_demo.py scripts/tests/test_parse_demo.py
git commit -m "feat(study-rag): DEMO 实例值采样 (列头=OID 假设, pilot 验证)"
```

---

### Task 7: field card 渲染 + INDEX/ROUTING 生成

**Files:**
- Create: `sdtm-rag/scripts/study/build_field_cards.py`
- Test: `sdtm-rag/scripts/tests/test_build_field_cards.py`

**Interfaces:**
- Consumes: Task 5 catalog dict; Task 6 samples dict。
- Produces:
  - `render_field_card(item: dict, form: dict, codelist: dict | None, samples: list[str], diff: list[str], *, study: str, version: str) -> str`
  - `build_cards(catalog: dict, samples: dict[str, list[str]], cards_dir: Path, *, forms_filter: set[str] | None = None) -> list[Path]` — 每 Item 一个 `{study}__{form_oid}__{item_oid}.md`; 同时生成 `INDEX.md` / `ROUTING.md` (满足 `RAGEngine` 对 kb_root 的硬性要求 rag.py:132-137)
  - CLI: `python -m scripts.study.build_field_cards --study st01 [--forms FAKEFORM1,FAKEFORM2]`
- 卡片 frontmatter keys (Task 9 ingest 消费): `study, version, doc_type: field_card, form_oid, field_oid, source_sheet, source_row`。

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_build_field_cards.py`:

```python
import pytest

from scripts.tests.study_fixtures import build_config_report
from scripts.study.build_catalog import build_catalog
from scripts.study.build_field_cards import build_cards, render_field_card
from scripts.study.paths import StudyPaths


@pytest.fixture()
def catalog(tmp_path):
    new = build_config_report(tmp_path / "new.xlsx")
    out = tmp_path / "st01"
    sp = StudyPaths(study_id="st01", version_label_new="VNEW", version_label_old=None,
                    config_report_new=new, config_report_old=None, demo_export=None,
                    out_dir=out, cards_dir=out / "cards")
    return build_catalog(sp), sp


def test_render_field_card_content(catalog):
    cat, _ = catalog
    item = cat["items"][0]                    # FAKEIT1
    form = cat["forms"][0]
    card = render_field_card(item, form, cat["codelists"].get(item["choices"]),
                             ["1", "0"], [], study="st01", version="VNEW")
    head, body = card.split("---\n", 2)[1:]
    assert "study: st01" in head and "doc_type: field_card" in head
    assert "form_oid: FAKEFORM1" in head and "field_oid: FAKEIT1" in head
    assert f"source_row: {item['row']}" in head
    assert "# [偽フォーム一 FAKEFORM1] 偽項目ラベル一 (FAKEIT1)" in body
    assert "integer" in body and "必須" in body
    assert "1 = 偽選択肢はい" in body                 # codelist 展开
    assert "DEMO 実例値: 1 / 0" in body
    assert "旧→新版差分: なし" in body


def test_build_cards_files_and_index(catalog):
    cat, sp = catalog
    paths = build_cards(cat, {}, sp.cards_dir)
    names = sorted(p.name for p in paths)
    assert names == ["st01__FAKEFORM1__FAKEIT1.md", "st01__FAKEFORM1__FAKEIT2.md",
                     "st01__FAKEFORM2__FAKEIT3.md"]
    index = (sp.cards_dir / "INDEX.md").read_text(encoding="utf-8")
    assert "FAKEFORM1" in index and "2" in index    # form + 项目数
    assert (sp.cards_dir / "ROUTING.md").exists()


def test_build_cards_forms_filter(catalog):
    cat, sp = catalog
    paths = build_cards(cat, {}, sp.cards_dir, forms_filter={"FAKEFORM2"})
    assert [p.name for p in paths] == ["st01__FAKEFORM2__FAKEIT3.md"]
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_build_field_cards.py -v
```

Expected: FAIL (ModuleNotFoundError)。

- [ ] **Step 3: 实现 build_field_cards.py**

```python
"""catalog → field card markdown (spec §3.1 模板). 模板拼装, 零 LLM."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from scripts.study.parse_demo import sample_demo_values
from scripts.study.paths import resolve_study


def render_field_card(item: dict, form: dict, codelist: dict | None,
                      samples: list[str], diff: list[str], *,
                      study: str, version: str) -> str:
    fm = "\n".join([
        "---",
        f"study: {study}",
        f"version: {version}",
        "doc_type: field_card",
        f"form_oid: {item['form_oid']}",
        f"field_oid: {item['item_oid']}",
        "source_sheet: Items and Groups",
        f"source_row: {item['row']}",
        "generated_by: build_field_cards.py",
        "---",
    ])
    length = "/".join(x for x in (item["min_length"], item["max_length"]) if x)
    type_bits = item["data_type"] or "?"
    if length:
        type_bits += f" (len {length})"
    type_bits += " / 必須" if item["required"] else " / 任意"
    if codelist:
        cl_lines = "\n".join(f"  - {code} = {text}" for code, text in codelist["entries"])
        cl_block = f"{item['choices']}\n{cl_lines}"
    else:
        cl_block = item["choices"] or "なし (自由記述)"
    checks = " / ".join(x for x in (item["data_checks"], item["system_checks"]) if x) or "—"
    lines = [
        f"# [{item['form_name']} {item['form_oid']}] {item['label']} ({item['item_oid']})",
        f"- Form: {item['form_name']} ({item['form_oid']})",
        f"- Item group: {item['group_name']} ({item['group_oid']})",
        f"- 型: {type_bits}",
        f"- Control: {item['control_type'] or '—'}"
        + (f" / 単位: {item['unit']}" if item["unit"] else ""),
        f"- Codelist: {cl_block}",
        f"- Edit checks: {checks}",
        f"- 表示条件: {item['visible_condition'] or '常時表示'}",
        f"- DEMO 実例値: {' / '.join(samples) if samples else '—'}",
        f"- 旧→新版差分: {'; '.join(diff) if diff else 'なし'}",
    ]
    if item["output_field_id"]:
        lines.append(f"- Output: {item['output_field_id']} ({item['output_field_label']})")
    for label, key in (("説明", "description"), ("入力指示", "instructions")):
        if item[key]:
            lines.append(f"- {label}: {item[key]}")
    return fm + "\n\n" + "\n".join(lines) + "\n"


def _write_index(catalog: dict, cards_dir: Path, per_form: dict[str, int]) -> None:
    rows = ["# st01 Field Card Index", "",
            f"Study: {catalog['study']} / version {catalog['version_new']}", "",
            "| Form | 名称 | 項目数 |", "|---|---|---|"]
    for f in catalog["forms"]:
        rows.append(f"| {f['oid']} | {f['name']} | {per_form.get(f['oid'], 0)} |")
    (cards_dir / "INDEX.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    routing = (
        "# Routing\n\n"
        f"本 KB は研究 {catalog['study']} の EDC 画面項目カード集 (1 項目 = 1 card)。\n"
        "画面名/フォーム名/項目ラベル/Item OID で検索する。SDTM 標準の規則は別 KB (cdisc)。\n"
    )
    (cards_dir / "ROUTING.md").write_text(routing, encoding="utf-8")


def build_cards(catalog: dict, samples: dict[str, list], cards_dir: Path, *,
                forms_filter: set[str] | None = None) -> list[Path]:
    if cards_dir.exists():
        shutil.rmtree(cards_dir)          # 幂等: 全量重生成, 勿手改产物
    cards_dir.mkdir(parents=True)
    forms_by_oid = {f["oid"]: f for f in catalog["forms"]}
    out: list[Path] = []
    per_form: dict[str, int] = {}
    for item in catalog["items"]:
        if forms_filter and item["form_oid"] not in forms_filter:
            continue
        card = render_field_card(
            item, forms_by_oid.get(item["form_oid"], {}),
            catalog["codelists"].get(item["choices"]),
            samples.get(item["item_oid"], []),
            catalog["diffs"].get(item["item_oid"], []),
            study=catalog["study"], version=catalog["version_new"],
        )
        p = cards_dir / f"{catalog['study']}__{item['form_oid']}__{item['item_oid']}.md"
        p.write_text(card, encoding="utf-8")
        out.append(p)
        per_form[item["form_oid"]] = per_form.get(item["form_oid"], 0) + 1
    _write_index(catalog, cards_dir, per_form)
    return out


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    ap.add_argument("--forms", help="逗号分隔 form OID, 缺省全量")
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    catalog = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    samples: dict[str, list] = {}
    if sp.demo_export is not None:
        oids = {i["item_oid"] for i in catalog["items"]}
        samples, _ = sample_demo_values(sp.demo_export, oids)
    flt = set(args.forms.split(",")) if args.forms else None
    paths = build_cards(catalog, samples, sp.cards_dir, forms_filter=flt)
    print(f"cards={len(paths)} dir={sp.cards_dir}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_build_field_cards.py -v
```

Expected: 3 passed (含 Task 3-6 全套回归: `.venv/bin/pytest scripts/tests/ -v -k study`)。

- [ ] **Step 5: Commit**

```bash
git add scripts/study/build_field_cards.py scripts/tests/test_build_field_cards.py
git commit -m "feat(study-rag): field card 渲染 + INDEX/ROUTING 生成 (模板拼装零 LLM)"
```

---

### Task 8: Pilot 试跑 (2 form 端到端) — ⛔ CHECKPOINT

**Files:**
- Create (本地): `data/study/st01/cards/` 下 2 个 form 的卡片
- Create: `sdtm-rag/evidence/checkpoints/study_rag_pilot.md` (纯统计, 无真名)

**Interfaces:**
- Consumes: Task 5-7 的 CLI。
- Produces: schema 冻结决定; DEMO 结构假设结论; golden questions 素材。

- [ ] **Step 1: 选 2 个代表性 form 跑 pilot (本地)**

选择标准: 一个字段多且带 codelist 的 form + 一个含日期/条件显示的 form (从 catalog.json 统计里选, 执行时定)。

```bash
.venv/bin/python -m scripts.study.build_catalog --study st01
.venv/bin/python -m scripts.study.build_field_cards --study st01 --forms <FORM_A>,<FORM_B>
ls data/study/st01/cards/ | head
```

- [ ] **Step 2: 人工核卡 (规则 A 精神, 抽 10 张)**

对照原 xlsx 逐项核对 10 张卡: label/型/必填/codelist/check/实例值/差分是否与源一致。发现不符 → 修 parser/模板 → 重跑 → 记录到 `failures/study_pilot_attempt_N.md` (不含真名)。

- [ ] **Step 3: 写 pilot 证据 (纯统计)**

`evidence/checkpoints/study_rag_pilot.md`: 卡片数、抽检数/不符数、DEMO 匹配率、覆盖台账状态、发现的问题清单 (用 OID 代称亦不可 — 只写"某日期项目"级别的描述)。

- [ ] **Step 4: ⛔ 向用户汇报, 请求 schema 冻结批准**

汇报: 抽检结果 + 卡片样例 (口头/本地查看, 不贴进 git 文档) + 待决问题 (DEMO 假设、Code lists 台账行格式等)。**用户批准后才进入 Task 9-12; 若粒度不对, 回改 Task 7 模板重新 pilot。**

- [ ] **Step 5: Commit (仅 evidence)**

```bash
git add evidence/checkpoints/study_rag_pilot.md
git commit -m "docs(study-rag): pilot 证据 checkpoint (2 form 端到端, 统计与问题清单)"
```

---

### Task 9: embedding 复用重构 (ingest.py 抽 embed_texts)

**Files:**
- Modify: `sdtm-rag/scripts/ingest.py` (`embed_chunks` 函数, ingest.py:226 起)
- Test: `sdtm-rag/scripts/tests/test_ingest_embed.py`

**Interfaces:**
- Produces: `embed_texts(texts: list[str]) -> list[list[float]]` — 含截断 (`_truncate_for_embedding`)、batch=100、429 退避、维度断言; `embed_chunks(chunks)` 变为 `return embed_texts([c.text for c in chunks])`。Task 10 消费。

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_ingest_embed.py`:

```python
from unittest.mock import patch

from scripts.ingest import EMBED_DIM, embed_texts


class _FakeResp:
    def __init__(self, n):
        self.data = [{"embedding": [0.0] * EMBED_DIM} for _ in range(n)]


def test_embed_texts_batches_of_100():
    calls = []

    def fake_embedding(model, input):
        calls.append(len(input))
        return _FakeResp(len(input))

    with patch("scripts.ingest.litellm.embedding", side_effect=fake_embedding):
        out = embed_texts([f"t{i}" for i in range(150)])
    assert len(out) == 150 and calls == [100, 50]
    assert all(len(v) == EMBED_DIM for v in out)
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_ingest_embed.py -v
```

Expected: FAIL — `ImportError: embed_texts` (若常量名非 `EMBED_DIM`, 以 ingest.py:49-52 实际名为准改测试)。

- [ ] **Step 3: 重构**

把 `embed_chunks` (ingest.py:226-300) 的循环体提为 `embed_texts(texts: list[str])`(逻辑原样搬移: 截断、batch、退避、维度断言), `embed_chunks` 改为一行委托。不改任何行为。

- [ ] **Step 4: 跑测试 + 全量回归**

```bash
.venv/bin/pytest scripts/tests/ -v
```

Expected: 全部 passed (含既有测试无回归)。

- [ ] **Step 5: Commit**

```bash
git add scripts/ingest.py scripts/tests/test_ingest_embed.py
git commit -m "refactor(ingest): 抽出 embed_texts 供 study ingest 复用 (行为不变)"
```

---

### Task 10: study 卡片 ingest → collection study_st01

**Files:**
- Create: `sdtm-rag/scripts/study/ingest_study.py`
- Test: `sdtm-rag/scripts/tests/test_ingest_study.py`

**Interfaces:**
- Consumes: Task 7 卡片 (frontmatter); Task 9 `embed_texts`。
- Produces:
  - `load_cards(cards_dir: Path) -> list[dict]` — 每卡 `{"id": 文件名 stem, "text": 全文, "metadata": {study, version, file_type: 'field_card', domain: form_oid, field_oid, section, source}}`; `INDEX.md`/`ROUTING.md` 跳过。`domain`=form_oid、`file_type`=doc_type 是有意映射 — 复用 `RAGEngine._build_where` 的现有过滤键。
  - `persist_study(chroma_dir: Path, collection: str, cards: list[dict], embeddings) -> None` — **只** delete/create 自己的 collection, 绝不动目录。
  - CLI: `python -m scripts.study.ingest_study --study st01 [--dry-run]`; collection 名 `f"study_{study_id}"`。

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_ingest_study.py`:

```python
from pathlib import Path

import chromadb
import pytest

from scripts.study.ingest_study import load_cards, persist_study

CARD = """---
study: st01
version: VNEW
doc_type: field_card
form_oid: FAKEFORM1
field_oid: FAKEIT1
source_sheet: Items and Groups
source_row: 5
generated_by: build_field_cards.py
---

# [偽フォーム一 FAKEFORM1] 偽項目ラベル一 (FAKEIT1)
- 型: integer / 必須
"""


@pytest.fixture()
def cards_dir(tmp_path) -> Path:
    d = tmp_path / "cards"
    d.mkdir()
    (d / "st01__FAKEFORM1__FAKEIT1.md").write_text(CARD, encoding="utf-8")
    (d / "INDEX.md").write_text("# idx", encoding="utf-8")
    (d / "ROUTING.md").write_text("# r", encoding="utf-8")
    return d


def test_load_cards_metadata(cards_dir):
    cards = load_cards(cards_dir)
    assert len(cards) == 1                      # INDEX/ROUTING 跳过
    c = cards[0]
    assert c["id"] == "st01__FAKEFORM1__FAKEIT1"
    assert c["metadata"]["domain"] == "FAKEFORM1"
    assert c["metadata"]["file_type"] == "field_card"
    assert c["metadata"]["field_oid"] == "FAKEIT1"
    assert "偽項目ラベル一" in c["text"]


def test_persist_study_leaves_other_collections(tmp_path, cards_dir):
    client = chromadb.PersistentClient(path=str(tmp_path / "chroma"))
    other = client.create_collection("sdtm_kb_v1", metadata={"hnsw:space": "cosine"})
    other.add(ids=["x"], documents=["doc"], embeddings=[[0.0] * 3])
    cards = load_cards(cards_dir)
    persist_study(tmp_path / "chroma", "study_st01", cards,
                  [[0.1] * 3 for _ in cards])
    client2 = chromadb.PersistentClient(path=str(tmp_path / "chroma"))
    assert client2.get_collection("sdtm_kb_v1").count() == 1     # 未被破坏
    col = client2.get_collection("study_st01")
    assert col.count() == 1
    got = col.get(ids=["st01__FAKEFORM1__FAKEIT1"], include=["metadatas"])
    assert got["metadatas"][0]["form_oid"] == "FAKEFORM1"
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_ingest_study.py -v
```

Expected: FAIL (ModuleNotFoundError)。

- [ ] **Step 3: 实现 ingest_study.py**

```python
"""study field cards → chroma collection study_<id>. 只动自己的 collection."""
from __future__ import annotations

import argparse
from pathlib import Path

import chromadb

from scripts.ingest import embed_texts
from scripts.study.paths import resolve_study

_SKIP = {"INDEX.md", "ROUTING.md"}


def _parse_frontmatter(text: str) -> dict[str, str]:
    parts = text.split("---\n")
    meta: dict[str, str] = {}
    if len(parts) >= 3:
        for line in parts[1].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta


def load_cards(cards_dir: Path) -> list[dict]:
    cards: list[dict] = []
    for p in sorted(cards_dir.glob("*.md")):
        if p.name in _SKIP:
            continue
        text = p.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        cards.append({
            "id": p.stem,
            "text": text,
            "metadata": {
                "study": fm.get("study", ""),
                "version": fm.get("version", ""),
                "file_type": fm.get("doc_type", "field_card"),
                "domain": fm.get("form_oid", ""),
                "form_oid": fm.get("form_oid", ""),
                "field_oid": fm.get("field_oid", ""),
                "section": fm.get("form_oid", ""),
                "source": f"{fm.get('source_sheet', '')}#row{fm.get('source_row', '')}",
            },
        })
    return cards


def persist_study(chroma_dir: Path, collection: str, cards: list[dict],
                  embeddings: list[list[float]]) -> None:
    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        client.delete_collection(collection)
    except Exception:
        pass
    col = client.create_collection(name=collection, metadata={"hnsw:space": "cosine"})
    for i in range(0, len(cards), 1000):
        batch = cards[i : i + 1000]
        col.add(
            ids=[c["id"] for c in batch],
            documents=[c["text"] for c in batch],
            embeddings=embeddings[i : i + 1000],
            metadatas=[c["metadata"] for c in batch],
        )


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    cards = load_cards(sp.cards_dir)
    collection = f"study_{sp.study_id}"
    print(f"cards={len(cards)} → collection={collection}")
    if args.dry_run:
        return
    embeddings = embed_texts([c["text"] for c in cards])
    from scripts.ingest import CHROMA_DIR  # data/chroma, 与主库同目录不同 collection
    persist_study(CHROMA_DIR, collection, cards, embeddings)
    (sp.out_dir / "ingested_at.txt").write_text(
        f"cards={len(cards)}\n", encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
```

注: `CHROMA_DIR` 以 ingest.py:37 实际常量名为准 (若为局部推导, 在 ingest.py 顶部补一个模块常量并让原代码引用它)。

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/pytest scripts/tests/test_ingest_study.py -v
```

Expected: 2 passed。

- [ ] **Step 5: Commit**

```bash
git add scripts/study/ingest_study.py scripts/tests/test_ingest_study.py
git commit -m "feat(study-rag): study 卡片 ingest → study_st01 (collection 级隔离)"
```

---

### Task 11: 拆弹 — CDISC ingest 的整目录 reset 不再殃及 study collection

**Files:**
- Modify: `sdtm-rag/scripts/ingest.py` (`reset_chroma_dir` ingest.py:127 及 `main` 中调用点)
- Test: `sdtm-rag/scripts/tests/test_ingest_reset.py`

**Interfaces:**
- Produces: `reset_collection(chroma_dir: Path, name: str) -> None` (只删同名 collection); `main` 默认走 collection 级 reset, 新增 `--full-reset` 保留旧的整目录清空行为 (显式选择才破坏)。

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_ingest_reset.py`:

```python
from pathlib import Path

import chromadb

from scripts.ingest import reset_collection


def test_reset_collection_spares_others(tmp_path):
    cdir = tmp_path / "chroma"
    client = chromadb.PersistentClient(path=str(cdir))
    client.create_collection("sdtm_kb_v1")
    study = client.create_collection("study_st01")
    study.add(ids=["a"], documents=["d"], embeddings=[[0.0] * 3])
    reset_collection(cdir, "sdtm_kb_v1")
    c2 = chromadb.PersistentClient(path=str(cdir))
    assert c2.get_collection("study_st01").count() == 1
    names = {c.name for c in c2.list_collections()}
    assert "sdtm_kb_v1" not in names


def test_reset_collection_missing_is_noop(tmp_path):
    reset_collection(tmp_path / "chroma", "absent")   # 不抛异常
```

- [ ] **Step 2: 跑测试确认失败**

```bash
.venv/bin/pytest scripts/tests/test_ingest_reset.py -v
```

Expected: FAIL (ImportError)。

- [ ] **Step 3: 实现**

在 ingest.py 增加:

```python
def reset_collection(chroma_dir: Path, name: str) -> None:
    """只删除指定 collection; 其他 collection (如 study_*) 不受影响."""
    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        client.delete_collection(name)
    except Exception:
        pass
```

`main` 中原 `reset_chroma_dir(chroma_dir)` 调用改为:

```python
    if args.full_reset:
        reset_chroma_dir(chroma_dir)
    else:
        reset_collection(chroma_dir, COLLECTION_NAME)
```

argparse 增加 `parser.add_argument("--full-reset", action="store_true", help="旧行为: 整目录清空 (会删除 study_* collection)")`。`backup_existing_chroma` 调用保持不变。

- [ ] **Step 4: 跑测试 + 全量回归**

```bash
.venv/bin/pytest scripts/tests/ -v
```

Expected: 全部 passed。

- [ ] **Step 5: Commit**

```bash
git add scripts/ingest.py scripts/tests/test_ingest_reset.py
git commit -m "fix(ingest): reset 改 collection 级, CDISC 重灌不再抹掉 study_* (--full-reset 保留旧行为)"
```

---

### Task 12: run_eval 支持 --collection/--kb-root + golden questions + pilot 检索评测 — ⛔ CHECKPOINT

**Files:**
- Modify: `sdtm-rag/eval/run_eval.py` (argparse ~:411-533, RAGEngine 构造 ~:541-567)
- Create (本地, 不进 git): `data/study/st01/eval/test_set_study_v0.yml`
- Modify: `sdtm-rag/evidence/checkpoints/study_rag_pilot.md` (追加评测结果)

**Interfaces:**
- Produces: `run_eval.py` 新 flags `--collection NAME` / `--kb-root PATH`; 提供 `--collection` 时强制 `structured_lookup_enabled=False` (S1/(d) 通道是 CDISC 专用 gold map)。

- [ ] **Step 1: 加 flags**

argparse 段追加:

```python
    parser.add_argument("--collection", default=None,
                        help="覆盖 settings.collection_name (如 study_st01)")
    parser.add_argument("--kb-root", default=None,
                        help="覆盖 settings.kb_root (需含 INDEX.md/ROUTING.md)")
```

RAGEngine 构造处 (run_eval.py:541-567) 改为:

```python
    collection_name = args.collection or settings.collection_name
    kb_root = Path(args.kb_root) if args.kb_root else settings.kb_root
    structured_lookup = args.structured_lookup and args.collection is None
```

并把这三个变量传入原构造参数位 (`collection_name=collection_name, kb_root=kb_root, structured_lookup_enabled=structured_lookup`; 其余参数不动。`args.structured_lookup` 的实际变量名以现文件为准)。

- [ ] **Step 2: 冒烟验证 flag 存在**

```bash
.venv/bin/python eval/run_eval.py --help | grep -A1 -e collection -e kb-root
```

Expected: 两个新 flag 出现在 help。

- [ ] **Step 3: ⛔ 与用户共写 golden questions (本地文件)**

`data/study/st01/eval/test_set_study_v0.yml` — 与用户一起写 ~10 题真实 mapping 风格问题 (日文画面/項目提问), 格式沿用 eval/test_set_v3.yml:

```yaml
- id: st01_q01
  category: field_lookup        # field_lookup | form_overview | mapping
  question: "<某画面>の<某項目>はどのフォームのどの項目か、型と選択肢は?"
  expected_facts:
    - "<期待出现在答案里的事实子串>"
  expected_sources:
    - "st01__<FORM>__<ITEM>"    # 命中卡片 id
```

**此文件含真实字段信息, 永不离开 data/study/ (Task 1 已 gitignore)。**

- [ ] **Step 4: pilot 检索评测 (本地)**

先完成 pilot 范围 ingest:

```bash
.venv/bin/python -m scripts.study.ingest_study --study st01
.venv/bin/python eval/run_eval.py data/study/st01/eval/test_set_study_v0.yml \
  --retrieval-only --collection study_st01 --kb-root data/study/st01/cards --tag study_pilot
```

Expected: 跑通; source recall 有分数。目标 top-k 命中 ≥ 8/10; 不达标 → 分析漏检原因 (日文 embedding? 卡片措辞?) → 调整 (如卡片加英文别名行) → 重跑。结论追加进 `evidence/checkpoints/study_rag_pilot.md` (只写分数与结论)。

- [ ] **Step 5: ⛔ 用户复核评测结果 → 批准全量**

- [ ] **Step 6: Commit**

```bash
git add eval/run_eval.py evidence/checkpoints/study_rag_pilot.md
git commit -m "feat(eval): --collection/--kb-root 支持第二 collection; study pilot 检索评测录入"
```

---

### Task 13: 全量跑 + 验收 + 收尾

**Files:**
- Create: `sdtm-rag/evidence/checkpoints/study_rag_full_run.md`
- Modify (本地): `data/study/st01/` 全量产物

**Interfaces:**
- Consumes: Task 5-12 全部。
- Produces: spec §7 验收清单逐条证据。

- [ ] **Step 1: 全量重生成 (本地)**

```bash
.venv/bin/python -m scripts.study.build_catalog --study st01
.venv/bin/python -m scripts.study.build_field_cards --study st01
.venv/bin/python -m scripts.study.ingest_study --study st01
```

Expected: 无 orphan 异常; cards ≈ items 数; ingest done。

- [ ] **Step 2: 验收清单逐条核对 (spec §7)**

```bash
# 1. 覆盖台账全绿
.venv/bin/python -c "
import csv
rows = list(csv.DictReader(open('data/study/st01/coverage_ledger.csv')))
from collections import Counter
print(Counter(r['status'] for r in rows))
assert all(r['target'] for r in rows), 'orphan!'
print('ledger OK')
"
# 2. golden questions 全量复跑
.venv/bin/python eval/run_eval.py data/study/st01/eval/test_set_study_v0.yml \
  --retrieval-only --collection study_st01 --kb-root data/study/st01/cards --tag study_full
# 3. 测试全绿
.venv/bin/pytest scripts/tests/ -v
# 4. git 安全
git status --short | grep -c "data/study" ; git ls-files | grep -c "data/study"
```

Expected: ledger OK; eval 分数 ≥ pilot; 测试全 passed; 最后两个 grep 均为 0。(验收项 3 有损轨抽检与项 4 联邦路由属 Plan C / Plan B, 不在本计划。)

- [ ] **Step 3: 写全量证据**

`evidence/checkpoints/study_rag_full_run.md`: forms/items/cards/codelists 数、ledger 状态计数、diff/new/removed 计数、eval 分数、测试计数。**纯统计, 无真名无字段内容。**

- [ ] **Step 4: Commit + 汇报**

```bash
git add evidence/checkpoints/study_rag_full_run.md
git commit -m "docs(study-rag): 确定性轨全量收口 — 台账全绿 + golden questions 评测"
```

向用户汇报, 触发 session 收尾流程 (worklog/PROGRESS/CLAUDE.md Key Paths 按 wrap-up checklist 走), 并提议下一步: Plan B (联邦路由) 或 Plan C (protocol 有损轨)。

---

## Self-Review 记录

- **Spec coverage**: §2 in-scope 的 ConfigReport/DEMO/collection/评测 → Task 3-13 ✔; protocol/aCRF/路由 → 明确移交 Plan B/C ✔; §4.1 五条约束 → pilot(T8)/溯源(T7)/台账(T5)/幂等(T7 rmtree 重生成)/小批次(有损轨在 Plan C) ✔; §6 红线 → T1 + 各 task 本地文件纪律 ✔; §7 验收 1/2/5 → T13, 3/4 → Plan C/B ✔。
- **Placeholder scan**: 计划内 `<FORM_A>`/`<真实目录名>` 等尖括号是**故意的红线占位** (真名不得写入本文档), 由执行者在本地文件/命令行填充 — 非未完成内容。
- **Type consistency**: `StudyPaths` 字段在 T2 定义、T5/T7/T10 消费一致; catalog dict keys 在 T5 产出、T7 消费一致; 卡片 frontmatter keys T7 产出、T10 `load_cards` 消费一致; `embed_texts` T9 定义、T10 导入一致。
- 已知留白 (pilot 决议项, 有意为之): DEMO 列头=OID 假设 (T6→T8); Code lists 台账行粒度 (T5 注); 真实 56 列中未入 dataclass 的列全部保存在 `raw` 并随 catalog.json 留痕, 不丢信息。
