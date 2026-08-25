# study 轨 workflow 事件层 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 ConfigReport 里三个从未被解析的 workflow sheet 接进 catalog, 让事件/活动/表单分配可确定性查询, 并修掉卡片 `適用範囲` 行的语义反转缺陷。

**Architecture:** 复用既有确定性解析栈 —— `read_sheet_records` 已支持两种表头形态 (`has_section_row` 开关), `is_trailer` 脚注过滤已有既定写法。新增三个 dataclass + 三个 parse 函数, 产物进同一个 `catalog.json` 的三个新池 (同源同 xlsx, 不新建独立文件)。item 的真实采集范围由 (form 被分配到的 activity 集合) 减去 (item 的 hidden activity 集合) 确定性推导。零 LLM, 零 PDF, 零有损转换。

**Tech Stack:** Python 3 / openpyxl / pytest / 既有 `scripts/study/*` 管线 / `server/study_lookup.py`

**Spec:** `docs/superpowers/specs/2026-08-25-study-workflow-events-design.md`

## Global Constraints

- **零真名**: 一切进 git 的内容 (代码/测试/题集/证据/报告/commit message) 零真实 form/field/event/activity OID 与 label; 研究一律代号 `st01`。测试 fixture 用 `偽` 前缀伪值 (既有惯例见 `test_build_field_cards.py`)。
- **红线检查必须程序化**: 与 `data/study/st01/catalog.json` 双向比对 (catalog 值→文档 / 文档日文串→catalog), 不许「我觉得这个不算」。
- **零 LLM 调用, 零配额**。
- **不碰任何 PDF** (Plan C 已判 DROP, 见 `sdtm-rag/evidence/checkpoints/c2_pre_survey.md` §8)。
- **规则 D**: writer / reviewer 走不同 `subagent_type`, 不许同 context 自审。
- **规则 B**: 任何失败 attempt 归档 `sdtm-rag/evidence/failures/`, 不删。
- **判据先于数据**: 本计划所有期望值 (110/21/109/1、61/61、14/77/110) 已在计划written 时冻结, 实现期**不许**为迁就实现而调整; 不吻合 = 停 (spec §6 S1/S2)。
- 所有命令的工作目录是 `sdtm-rag/`, Python 解释器一律 `.venv/bin/python`。

---

## File Structure

| 文件 | 责任 | 动作 |
|---|---|---|
| `scripts/study/parse_config_report.py` | ConfigReport 确定性解析器 | **Modify** — 新增 3 个 dataclass + 3 个 parse 函数 |
| `scripts/study/build_catalog.py` | catalog 组装 + 台账 | **Modify** — 三池入 catalog + ledger 扩展 + 三闸 |
| `scripts/study/build_field_cards.py` | catalog → 卡片 markdown | **Modify** — 修标签 (T1) + 新增采集范围行 (T4) |
| `server/study_lookup.py` | 确定性直查层 | **Modify** — 新增事件查询通道 (T6) |
| `scripts/tests/test_parse_workflow_sheets.py` | 三表解析单测 | **Create** (T2) |
| `scripts/tests/test_catalog_workflow_pools.py` | 三池 + 三闸单测 | **Create** (T3) |
| `scripts/tests/test_build_field_cards.py` | 卡片渲染单测 | **Modify** — T1 改 3 处断言, T4 加断言 |
| `scripts/tests/test_study_lookup_events.py` | 事件通道单测 | **Create** (T6) |
| `data/study/st01/eval/test_set_events_v1.yml` | event 侧 gold (**gitignored**) | **Create** (T5) |
| `sdtm-rag/evidence/checkpoints/study_workflow_events.md` | 收口证据 | **Create** (T6) |

---

## Task 1: 修 `適用範囲` 语义反转

**Files:**
- Modify: `scripts/study/build_field_cards.py:16`, `:93-96`
- Test: `scripts/tests/test_build_field_cards.py:65`, `:69-78`

**Interfaces:**
- Consumes: 无 (独立缺陷修复, 不依赖其他任务)
- Produces: 卡片行标签由 `- 適用範囲:` 改为 `- 非表示アクティビティ:`; 后续 Task 4 会在其**下方**新增 `- 収集アクティビティ:` 行

**背景 (给零上下文的实现者)**: `Visibility::Hidden in activity` 是 ConfigReport 的**隐藏**清单 (该字段在这些 activity 里**不显示**), 现被渲染成 `適用範囲` (=适用范围), 语义相反。961 张卡中 231 张带此行。已确认没有任何 gold 题依赖该行, 故不影响既有评分。判定依据见 spec §4 F3 (与 `Study workflow-Forms` 的 `Hidden items` 列互为精确转置, 61/61)。

- [ ] **Step 1: 记录基线 (必须先跑, 后面每一步都对照它)**

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
ls data/study/st01/cards/*.md | wc -l
grep -l "適用範囲" data/study/st01/cards/*.md | wc -l
```

Expected: `1699 passed` / `961` / `231`。**若三个数任一对不上, 停下来先查为什么, 不要继续。**

- [ ] **Step 2: 先把卡片目录做一份基线副本 (Task 结束时逐字对比用)**

```bash
cd sdtm-rag
rm -rf /tmp/cards_baseline_t1 && cp -R data/study/st01/cards /tmp/cards_baseline_t1
ls /tmp/cards_baseline_t1/*.md | wc -l    # 期望 961
```

- [ ] **Step 3: 改测试断言 (TDD: 先让测试表达新期望)**

在 `scripts/tests/test_build_field_cards.py` 中做三处替换:

第 65 行附近:
```python
    assert "非表示アクティビティ" not in card   # Hidden in activity 空 → 无该行
```

第 69-78 行的整个测试函数替换为:
```python
def test_render_hidden_activity_row(catalog):
    """非表示アクティビティ 独立行: Hidden in activity 原值展开, 且与 visible_condition 并存 (27 项).

    列名是 'Hidden in activity' = 该字段在这些 activity 中**被隐藏**; 旧标签 '適用範囲'
    (=适用范围) 语义相反, 2026-08-25 修正. 与 Study workflow-Forms 的 'Hidden items'
    列互为精确转置 (实测 61/61 逐键相同).
    """
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["visible_condition"] = "FAKEIT3 != ''"
    item["raw"] = {**item["raw"], "Visibility::Hidden in activity": "偽アクティビティ甲, 偽乙"}
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert "- 表示条件: FAKEIT3 != ''" in card
    assert "- 非表示アクティビティ: 偽アクティビティ甲, 偽乙" in card   # 不混入表示条件
    assert "適用範囲" not in card                                    # 旧标签彻底消失
    assert "条件あり" not in card
```

- [ ] **Step 4: 运行测试, 确认失败**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_build_field_cards.py -p no:warnings -q 2>&1 | tail -5
```

Expected: FAIL — `assert "- 非表示アクティビティ: 偽アクティビティ甲, 偽乙" in card` 不成立 (当前渲染的还是 `適用範囲`)。

- [ ] **Step 5: 改实现**

`scripts/study/build_field_cards.py` 第 16 行注释改为:
```python
# hidden-in-activity 是 activity 名单 (231 项, 最长 499 字符) → 单独 非表示アクティビティ 行, 非显示条件.
```

第 93-96 行改为:
```python
    # 非表示アクティビティ (activity 名单) 与显示条件正交, 独立行 — 231 项, 其中 27 项与
    # visible_condition 并存, 混进表示条件会被 if-not 短路吞掉。
    # ⚠ 语义: 列名是 'Hidden in activity' = 在这些 activity 中**被隐藏**。
    # 旧标签 '適用範囲' (=适用范围) 语义相反, 2026-08-25 修正。
    if item["raw"].get(_SCOPE_KEY):
        lines.append(f"- 非表示アクティビティ: {_flat(item['raw'][_SCOPE_KEY])}")
```

同时把变量名 `_SCOPE_KEY` 改为 `_HIDDEN_ACT_KEY` (全文件替换, 共 2 处: 定义处与使用处), 因为 "SCOPE" 这个名字本身就是那个错误理解的残留:
```python
_HIDDEN_ACT_KEY = "Visibility::Hidden in activity"
```

- [ ] **Step 6: 运行测试, 确认通过**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_build_field_cards.py -p no:warnings -q 2>&1 | tail -3
```

Expected: 19 passed。

- [ ] **Step 7: 重渲染 961 张卡片**

```bash
cd sdtm-rag
.venv/bin/python -m scripts.study.build_field_cards --study st01
ls data/study/st01/cards/*.md | wc -l
```

Expected: `961`。

- [ ] **Step 8: 回归闸 — 逐卡 diff, 只允许那一行变化 (spec §5.D 第 1 条)**

```bash
cd sdtm-rag
.venv/bin/python - <<'PY'
import pathlib, difflib
base = pathlib.Path('/tmp/cards_baseline_t1')
new  = pathlib.Path('data/study/st01/cards')
bn = {p.name for p in base.glob('*.md')}
nn = {p.name for p in new.glob('*.md')}
assert bn == nn, f"卡片集合变了: 多 {sorted(nn-bn)[:5]} 少 {sorted(bn-nn)[:5]}"
changed = unexpected = 0
for name in sorted(bn):
    a = (base/name).read_text(encoding='utf-8').splitlines()
    b = (new/name).read_text(encoding='utf-8').splitlines()
    if a == b:
        continue
    changed += 1
    for line in difflib.unified_diff(a, b, lineterm='', n=0):
        if line.startswith(('---', '+++', '@@')):
            continue
        body = line[1:]
        ok = body.startswith('- 適用範囲: ') if line[0] == '-' else body.startswith('- 非表示アクティビティ: ')
        if not ok:
            unexpected += 1
            print("UNEXPECTED", name, repr(line[:80]))
print(f"变化卡片 {changed} (期望 231) / 非预期行变化 {unexpected} (期望 0)")
assert changed == 231, f"变化卡片数 {changed} != 231"
assert unexpected == 0, "出现非预期行变化 → 按 spec §6 S3 退回"
print("PASS: 只有那一行变了")
PY
```

Expected: `变化卡片 231 (期望 231) / 非预期行变化 0 (期望 0)` + `PASS`。
**若 unexpected > 0 或 changed != 231 → 按 spec §6 S3 退回本任务的卡片改动, 归档到 `evidence/failures/`。**

- [ ] **Step 9: 全量测试**

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
```

Expected: `passed=1699` (本任务改断言不增减测试数)。

- [ ] **Step 10: 提交**

```bash
cd sdtm-rag
git add scripts/study/build_field_cards.py scripts/tests/test_build_field_cards.py
git commit -m "fix(study-cards): 適用範囲 -> 非表示アクティビティ — 修语义反转

Visibility::Hidden in activity 是隐藏清单, 旧标签 適用範囲 (=适用范围) 语义相反。
231/961 张卡受影响; 逐卡 diff 闸确认只有该行变化, 无非预期变更。
判定依据: 与 Study workflow-Forms 的 Hidden items 列互为精确转置 (61/61)。
已确认无 gold 题依赖该行, 不影响既有评分。"
```

---

## Task 2: 三个 workflow sheet 的解析器

**Files:**
- Modify: `scripts/study/parse_config_report.py` (在 `parse_codelists` 之后追加)
- Test: `scripts/tests/test_parse_workflow_sheets.py` (**Create**)

**Interfaces:**
- Consumes: 既有 `read_sheet_records(ws, *, has_section_row)` 与 `_req(rec, key)`
- Produces:
  - `EventDef(oid: str, name: str, description: str, event_type: str, visibility_condition: str, sched_reference: str, sched_minus_days: str, sched_plus_days: str, row: int, is_trailer: bool)`
  - `ActivityDef(oid: str, event_oid: str, event_name: str, name: str, description: str, visibility_condition: str, row: int, is_trailer: bool)`
  - `FormAssignment(event_oid: str, event_name: str, activity_oid: str, activity_name: str, form_oid: str, repeating: str, item_visibility: str, hidden_items: str, row: int, is_trailer: bool)`
  - `parse_events(path: Path) -> list[EventDef]`
  - `parse_activities(path: Path) -> list[ActivityDef]`
  - `parse_form_assignments(path: Path) -> list[FormAssignment]`
  - 三个函数均**返回全部行 (含 trailer)**, 由调用方过滤 —— 与既有 `parse_forms` 惯例一致 (台账要记脚注行)

**已实测的表头形态与精确 key (实现者不必自己去探)**:

| sheet | `has_section_row` | 记录数 | trailer 判据 |
|---|---|---|---|
| `Study workflow-Events` | `True` | 17 (真 14 + 脚注 3) | `General::Study event ID` 空或含空格 |
| `Study workflow-Activities` | `True` | 80 (真 77 + 脚注 3) | `General::Activity ID` 空或含空格 |
| `Study workflow-Forms` | `False` | 112 (真 110 + 脚注 2) | `Study workflow-Forms::Form ID` 为空 |

精确 key 名 (**全部实测得来**):
- Events: `General::Study event ID` · `General::Event name` · `General::Study event description` · `General::Event type` · `Visibility::Visibility condition` · `Scheduling::Reference` · `Scheduling::- days` · `Scheduling::+ days`
- Activities: `General::Study event ID` · `General::Event name` · `General::Activity ID` · `General::Activity name` · `General::Activity description` · `General::Visibility condition`
- Forms: `Study workflow-Forms::Event ID` · `::Event name` · `::Activity ID` · `::Activity name` · `::Form ID` · `::Repeating` · `::Item visibility` · `::Hidden items`

⚠ **不要**取 `Scheduling::Days` / `Scheduling::After` / `Scheduling::Enable recurrence` / `Timing::*` —— 实测这些列在本研究**全空** (非空 0), 取了只会造出恒空字段。时点语义实际承载在 `Activity name` 自由文本里。

- [ ] **Step 1: 写失败的测试**

Create `scripts/tests/test_parse_workflow_sheets.py`:

```python
"""Study workflow-{Events,Activities,Forms} 三表解析. 零真名: 断言只用计数与形态."""
import pytest

from scripts.study.parse_config_report import (
    parse_activities,
    parse_events,
    parse_form_assignments,
)
from scripts.study.paths import resolve_study


@pytest.fixture(scope="module")
def cfg_path():
    return resolve_study("st01").config_report_new


def test_parse_events_counts(cfg_path):
    evs = parse_events(cfg_path)
    assert len(evs) == 17                                   # 含脚注
    real = [e for e in evs if not e.is_trailer]
    assert len(real) == 14
    assert all(e.oid and " " not in e.oid for e in real)


def test_parse_events_type_distribution(cfg_path):
    real = [e for e in parse_events(cfg_path) if not e.is_trailer]
    kinds = {}
    for e in real:
        kinds[e.event_type] = kinds.get(e.event_type, 0) + 1
    assert sorted(kinds.values()) == [1, 13]                # 13 + 1, 不写死日文取值


def test_parse_activities_counts(cfg_path):
    acs = parse_activities(cfg_path)
    assert len(acs) == 80
    real = [a for a in acs if not a.is_trailer]
    assert len(real) == 77
    assert all(a.oid and a.event_oid for a in real)


def test_parse_form_assignments_counts(cfg_path):
    fms = parse_form_assignments(cfg_path)
    assert len(fms) == 112
    real = [f for f in fms if not f.is_trailer]
    assert len(real) == 110
    assert len({f.form_oid for f in real}) == 21


def test_repeating_values(cfg_path):
    real = [f for f in parse_form_assignments(cfg_path) if not f.is_trailer]
    counts = {}
    for f in real:
        counts[f.repeating] = counts.get(f.repeating, 0) + 1
    assert counts == {"0": 106, "Unlimited": 4}


def test_scheduling_columns_are_sparse_by_design(cfg_path):
    """本研究 Scheduling 只有 Reference/±days 各 2 条非空 — 钉死, 防未来静默变化."""
    real = [e for e in parse_events(cfg_path) if not e.is_trailer]
    assert sum(1 for e in real if e.sched_reference) == 2
    assert sum(1 for e in real if e.sched_minus_days) == 2
    assert sum(1 for e in real if e.sched_plus_days) == 2


def test_row_numbers_are_physical(cfg_path):
    """row 必须是可溯源物理行号 (Events 数据自第 4 行起)."""
    evs = parse_events(cfg_path)
    assert evs[0].row == 4
    assert evs[-1].row == 22
```

- [ ] **Step 2: 运行测试, 确认失败**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_parse_workflow_sheets.py -p no:warnings -q 2>&1 | tail -5
```

Expected: FAIL — `ImportError: cannot import name 'parse_events'`。

- [ ] **Step 3: 写实现**

在 `scripts/study/parse_config_report.py` 末尾追加:

```python
# ── Study workflow 三表 ────────────────────────────────────────────────
# 三个 sheet 在同一个 ConfigReport 里, 但表头形态不同 (实测):
#   Events / Activities  = 三行表头 (has_section_row=True),  数据自行 4 起
#   Forms                = 两行表头 (has_section_row=False), 数据自行 3 起
# 三表末尾均有 Viedoc 说明性脚注行, 形态: ID 列为空或含空格 (真 OID 无空格)。
# 与 FormDef.is_trailer 同惯例: 解析器**返回全部行**, 过滤交给调用方 (台账要记脚注)。


@dataclass(frozen=True)
class EventDef:
    oid: str
    name: str
    description: str
    event_type: str
    visibility_condition: str
    sched_reference: str
    sched_minus_days: str
    sched_plus_days: str
    row: int
    is_trailer: bool = False


@dataclass(frozen=True)
class ActivityDef:
    oid: str
    event_oid: str
    event_name: str
    name: str
    description: str
    visibility_condition: str
    row: int
    is_trailer: bool = False


@dataclass(frozen=True)
class FormAssignment:
    event_oid: str
    event_name: str
    activity_oid: str
    activity_name: str
    form_oid: str
    repeating: str
    item_visibility: str
    hidden_items: str
    row: int
    is_trailer: bool = False


def _read(path: Path, sheet: str, *, has_section_row: bool) -> list[dict]:
    wb = openpyxl.load_workbook(path, read_only=True)
    try:
        return read_sheet_records(wb[sheet], has_section_row=has_section_row)
    finally:
        wb.close()      # read_only 模式持有文件句柄


def _is_footnote(oid: str) -> bool:
    """脚注判据: ID 列为空或含空格。真 OID 是无空格标识符, 脚注是整句说明文字。"""
    return (not oid) or (" " in oid)


def parse_events(path: Path) -> list[EventDef]:
    out: list[EventDef] = []
    for r in _read(path, "Study workflow-Events", has_section_row=True):
        oid = _req(r, "General::Study event ID")
        out.append(EventDef(
            oid=oid,
            name=r.get("General::Event name", ""),
            description=r.get("General::Study event description", ""),
            event_type=r.get("General::Event type", ""),
            visibility_condition=r.get("Visibility::Visibility condition", ""),
            sched_reference=r.get("Scheduling::Reference", ""),
            sched_minus_days=r.get("Scheduling::- days", ""),
            sched_plus_days=r.get("Scheduling::+ days", ""),
            row=r["_row"],
            is_trailer=_is_footnote(oid),
        ))
    return out


def parse_activities(path: Path) -> list[ActivityDef]:
    out: list[ActivityDef] = []
    for r in _read(path, "Study workflow-Activities", has_section_row=True):
        oid = _req(r, "General::Activity ID")
        out.append(ActivityDef(
            oid=oid,
            event_oid=r.get("General::Study event ID", ""),
            event_name=r.get("General::Event name", ""),
            name=r.get("General::Activity name", ""),
            description=r.get("General::Activity description", ""),
            visibility_condition=r.get("General::Visibility condition", ""),
            row=r["_row"],
            is_trailer=_is_footnote(oid),
        ))
    return out


def parse_form_assignments(path: Path) -> list[FormAssignment]:
    out: list[FormAssignment] = []
    for r in _read(path, "Study workflow-Forms", has_section_row=False):
        form_oid = _req(r, "Study workflow-Forms::Form ID")
        out.append(FormAssignment(
            event_oid=r.get("Study workflow-Forms::Event ID", ""),
            event_name=r.get("Study workflow-Forms::Event name", ""),
            activity_oid=r.get("Study workflow-Forms::Activity ID", ""),
            activity_name=r.get("Study workflow-Forms::Activity name", ""),
            form_oid=form_oid,
            repeating=r.get("Study workflow-Forms::Repeating", ""),
            item_visibility=r.get("Study workflow-Forms::Item visibility", ""),
            hidden_items=r.get("Study workflow-Forms::Hidden items", ""),
            row=r["_row"],
            # Forms 表脚注行的 Form ID 为空 (Event ID 列反而是整句说明文字)
            is_trailer=_is_footnote(form_oid),
        ))
    return out
```

- [ ] **Step 4: 运行测试, 确认通过**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_parse_workflow_sheets.py -p no:warnings -q 2>&1 | tail -3
```

Expected: `7 passed`。

- [ ] **Step 5: 全量测试**

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
```

Expected: `passed=1706` (1699 + 7)。

- [ ] **Step 6: 提交**

```bash
cd sdtm-rag
git add scripts/study/parse_config_report.py scripts/tests/test_parse_workflow_sheets.py
git commit -m "feat(study-parse): 解析 Study workflow-{Events,Activities,Forms} 三表

三个 sheet 此前从未被任何管线读过。复用 read_sheet_records 的两种表头形态
(Events/Activities 三行表头, Forms 两行表头) 与 is_trailer 脚注惯例。
计数钉死: 17/14 · 80/77 · 112/110, form 21 个, Repeating 0x106 + Unlimited x4。
刻意不取 Scheduling::Days/After/recurrence 与 Timing::* (本研究全空)。"
```

---

## Task 3: 三池进 catalog + 三道验收闸

**Files:**
- Modify: `scripts/study/build_catalog.py` (`build_catalog` 函数 + `main` 的打印行)
- Test: `scripts/tests/test_catalog_workflow_pools.py` (**Create**, 7 个测试)

**Interfaces:**
- Consumes: Task 2 的 `parse_events` / `parse_activities` / `parse_form_assignments` 与三个 dataclass
- Produces: `catalog.json` 新增三个顶层 key —
  - `events`: `list[dict]` (EventDef 的 asdict, 已滤 trailer, 期望 14 条)
  - `activities`: `list[dict]` (ActivityDef 的 asdict, 已滤 trailer, 期望 77 条)
  - `assignments`: `list[dict]` (FormAssignment 的 asdict, 已滤 trailer, 期望 110 条)
  - `ledger` 新增三个 sheet 的记账行 (每行一条, trailer 记 `trailer:footnote`)

- [ ] **Step 1: 写失败的测试**

Create `scripts/tests/test_catalog_workflow_pools.py`:

```python
"""catalog 三池 + spec §5.A/B/C 三闸. 零真名: 只断言计数/集合关系."""
import collections

import pytest

from scripts.study.build_catalog import build_catalog
from scripts.study.paths import resolve_study


@pytest.fixture(scope="module")
def cat():
    return build_catalog(resolve_study("st01"))


def test_three_pools_exist_with_expected_sizes(cat):
    assert len(cat["events"]) == 14
    assert len(cat["activities"]) == 77
    assert len(cat["assignments"]) == 110


def test_gate_a_cross_check_against_design_summary(cat):
    """spec §5.A: 四条数字必须与 ConfigReport 设计摘要吻合 (已由 PDF 封面独立确认)."""
    asg = cat["assignments"]
    assert len(asg) == 110
    assert len({a["form_oid"] for a in asg}) == 21
    by_type = {e["oid"]: e["event_type"] for e in cat["events"]}
    counts = collections.Counter(by_type[a["event_oid"]] for a in asg)
    assert sorted(counts.values()) == [1, 109]


def test_gate_b_referential_integrity(cat):
    """spec §5.B: 四条引用完整性."""
    ev_ids = {e["oid"] for e in cat["events"]}
    ac_ids = {a["oid"] for a in cat["activities"]}
    form_ids = {f["oid"] for f in cat["forms"]}
    assert {a["event_oid"] for a in cat["activities"]} <= ev_ids
    assert {a["event_oid"] for a in cat["assignments"]} <= ev_ids
    assert {a["activity_oid"] for a in cat["assignments"]} <= ac_ids
    assert {a["form_oid"] for a in cat["assignments"]} <= form_ids


def test_gate_c_transpose_consistency(cat):
    """spec §5.C: assignments.hidden_items 与 items 的 Hidden in activity 互为精确转置.

    这是解析正确性的**独立参照物** —— 两处表示由 Viedoc 分别导出, 一致即互证。
    不一致 ⇒ spec §6 S2 触发, 停。
    """
    fwd = collections.defaultdict(set)
    for a in cat["assignments"]:
        if not a["hidden_items"].strip():
            continue
        for x in a["hidden_items"].replace("\n", ",").split(","):
            if x.strip():
                fwd[a["activity_oid"]].add(x.strip())
    bwd = collections.defaultdict(set)
    for it in cat["items"]:
        raw = str(it["raw"].get("Visibility::Hidden in activity") or "")
        for x in raw.replace("\n", ",").split(","):
            if x.strip():
                bwd[x.strip()].add(it["item_oid"])
    assert set(fwd) == set(bwd), "两侧 activity 键集不同"
    assert len(fwd) == 61
    mismatched = [k for k in fwd if fwd[k] != bwd[k]]
    assert mismatched == [], f"{len(mismatched)} 个 activity 的 item 集合不一致"


def test_hidden_activities_subset_of_activities(cat):
    """items 引用的 activity 必须全部在 activities 池里 (否则采集范围推导会静默丢)."""
    ac_ids = {a["oid"] for a in cat["activities"]}
    used = set()
    for it in cat["items"]:
        raw = str(it["raw"].get("Visibility::Hidden in activity") or "")
        for x in raw.replace("\n", ",").split(","):
            if x.strip():
                used.add(x.strip())
    assert len(used) == 61
    assert used <= ac_ids


def test_ledger_covers_workflow_sheets(cat):
    sheets = collections.Counter(r["sheet"] for r in cat["ledger"])
    assert sheets["Study workflow-Events"] == 17
    assert sheets["Study workflow-Activities"] == 80
    assert sheets["Study workflow-Forms"] == 112


def test_no_consumed_column_is_silently_empty(cat):
    """键名守卫 (控制方 Ruling I-2, 源自 Task 2 审查 I-1)。

    三个 parse 函数只有 ID 列走 `_req()`; 其余字段用 `r.get(key, "")` —— 上游改列名时
    **不报错, 静默给 ""**, 而 Task 2 的测试仍全绿。本条钉死"每个被消费的必填字段至少有值",
    用 `> 0` 而非精确计数: 精确计数需要先看数据再定判据, 违反判据先于数据。
    注: `hidden_items` 这一最关键字段另有闸 C (转置 61/61) 兜底, 静默全空会让闸 C 先红。
    刻意不含 description / visibility_condition —— 它们**合法地**稀疏。
    """
    required = [
        ("events", ["oid", "name", "event_type"]),
        ("activities", ["oid", "event_oid", "name"]),
        ("assignments", ["event_oid", "activity_oid", "form_oid",
                         "repeating", "item_visibility", "hidden_items"]),
    ]
    for pool, fields in required:
        for f in fields:
            n = sum(1 for r in cat[pool] if str(r[f]).strip())
            assert n > 0, f"{pool}.{f} 全空 — 列名可能已改, .get() 静默返回 ''"
```

- [ ] **Step 2: 运行测试, 确认失败**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_catalog_workflow_pools.py -p no:warnings -q 2>&1 | tail -5
```

Expected: FAIL — `KeyError: 'events'`。

- [ ] **Step 3: 写实现**

在 `scripts/study/build_catalog.py` 顶部 import 处追加:
```python
from scripts.study.parse_config_report import (
    parse_activities,
    parse_events,
    parse_form_assignments,
)
```
(与既有 `parse_forms` / `parse_items` / `parse_codelists` 的 import 合并成一条。)

在 `build_catalog` 里, `referenced = {...}` 那一行**之前**插入:
```python
    all_events = parse_events(sp.config_report_new)
    all_activities = parse_activities(sp.config_report_new)
    all_assignments = parse_form_assignments(sp.config_report_new)
    # ⛔ 控制方 Ruling C1 (2026-08-25, 源自 Task 3 审查): 下面两道闸**曾**被写成
    #    `is_trailer and oid and " " not in oid` —— 那是**死代码**。因为
    #    `is_trailer = (not oid) or (" " in oid)`, oid 非空即蕴含 `" " in oid`,
    #    三个合取项不可满足。Forms 的同形闸能触发, 是因为 FormDef.is_trailer 另有
    #    析取项 `not in_use`, 与 oid 形态解耦; workflow 三表没有, 故必须换判据。
    #    真正可达且必须响亮失败的形态是「ID 空但其他列有载荷」(Forms 侧 :74 已有同款闸)。
    for e in all_events:
        if e.is_trailer and not e.oid and (e.name or e.event_type or e.description):
            raise ValueError(f"workflow Events row {e.row}: blank Id with payload "
                             f"— 未知行形态, 不能静默归为脚注")
    for a in all_activities:
        if a.is_trailer and not a.oid and (a.name or a.event_oid or a.description):
            raise ValueError(f"workflow Activities row {a.row}: blank Id with payload "
                             f"— 未知行形态, 不能静默归为脚注")
    for f in all_assignments:
        if f.is_trailer and (f.activity_oid and " " not in f.activity_oid):
            raise ValueError(f"workflow Forms row {f.row}: 空 Form ID 但 Activity ID "
                             f"{f.activity_oid!r} 是 OID 形态 — 未知行形态, 不能静默归为脚注")
        if f.is_trailer and f.event_oid and " " not in f.event_oid:
            raise ValueError(f"workflow Forms row {f.row}: 空 Form ID 但 Event ID "
                             f"{f.event_oid!r} 是 OID 形态 — 未知行形态")
    events = [e for e in all_events if not e.is_trailer]
    activities = [a for a in all_activities if not a.is_trailer]
    assignments = [f for f in all_assignments if not f.is_trailer]
```

在 ledger 组装段 (`for oid, cl in codelists.items():` 那个循环**之后**) 追加:
```python
    for e in all_events:
        ledger.append({"sheet": "Study workflow-Events", "row": e.row, "status": "mapped",
                       "target": "trailer:footnote" if e.is_trailer else f"event:{e.oid}"})
    for a in all_activities:
        ledger.append({"sheet": "Study workflow-Activities", "row": a.row, "status": "mapped",
                       "target": "trailer:footnote" if a.is_trailer
                                 else f"activity:{a.event_oid}/{a.oid}"})
    for f in all_assignments:
        ledger.append({"sheet": "Study workflow-Forms", "row": f.row, "status": "mapped",
                       "target": "trailer:footnote" if f.is_trailer
                                 else f"assignment:{f.event_oid}/{f.activity_oid}/{f.form_oid}"})
```

在返回的 dict 里, `"codelists": {...}` 那一项**之后**追加三行:
```python
        "events": [asdict(e) for e in events],
        "activities": [asdict(a) for a in activities],
        "assignments": [asdict(f) for f in assignments],
```

`main` 的 print 改为:
```python
    print(f"forms={len(cat['forms'])} items={len(cat['items'])} "
          f"codelists={len(cat['codelists'])} events={len(cat['events'])} "
          f"activities={len(cat['activities'])} assignments={len(cat['assignments'])} "
          f"diffs={len(cat['diffs'])} "
          f"new={len(cat['new_items'])} removed={len(cat['removed_items'])} "
          f"ledger={n_status}")
```

- [ ] **Step 4: 运行测试, 确认通过**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_catalog_workflow_pools.py -p no:warnings -q 2>&1 | tail -3
```

Expected: `7 passed`。**若 `test_gate_c_transpose_consistency` 失败 → spec §6 S2 触发, 停止本计划, 归档 `evidence/failures/`, 不要继续 Task 4 (采集范围推导整个建立在该语义之上)。**

- [ ] **Step 5: 重生成 catalog 并核对台账**

```bash
cd sdtm-rag
cp data/study/st01/catalog.json /tmp/catalog_before_t3.json
.venv/bin/python -m scripts.study.build_catalog --study st01
```

Expected 输出含: `events=14 activities=77 assignments=110`。

```bash
cd sdtm-rag
.venv/bin/python - <<'PY'
import json, pathlib
old = json.loads(pathlib.Path('/tmp/catalog_before_t3.json').read_text())
new = json.loads(pathlib.Path('data/study/st01/catalog.json').read_text())
added = set(new) - set(old)
assert added == {"events", "activities", "assignments"}, f"新增 key 异常: {added}"
for k in old:
    if k == "ledger":
        continue
    assert old[k] == new[k], f"既有池 {k} 被改动 — 本任务只应新增"
print("PASS: 既有池逐字未动, 只新增三池")
print("ledger:", len(old["ledger"]), "->", len(new["ledger"]), "(期望 +209)")
assert len(new["ledger"]) - len(old["ledger"]) == 209
PY
```

Expected: `PASS` + `ledger: 3508 -> 3717 (期望 +209)` (17+80+112=209)。

- [ ] **Step 6: 全量测试**

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
```

Expected: `passed=1713` (1706 + 7)。

- [ ] **Step 7: 提交**

```bash
cd sdtm-rag
git add scripts/study/build_catalog.py scripts/tests/test_catalog_workflow_pools.py
git commit -m "feat(study-catalog): workflow 三池进 catalog + 三道验收闸

events=14 activities=77 assignments=110; ledger +209 行 (含脚注记账)。
闸 A: 110/21/109+1 与 ConfigReport 设计摘要吻合 (PDF 封面独立确认过同四数)。
闸 B: 四条引用完整性。
闸 C: assignments.hidden_items 与 items 的 Hidden in activity 互为精确转置 61/61
      —— 两处独立导出互证, 是解析正确性在解析器之外的参照物。
既有池逐字未动。"
```

---

## Task 4: item 真实采集范围推导 + 卡片新增行

> ⛔ **执行结果: spec §6 S3 触发, 用户 2026-08-25 裁定执行退回。**
> 卡片渲染该行的实测后果: study golden v2 **87.50% → 84.38%**, q14/q21 两题回归 (三遍逐题稳定, 非抖动)。
> 归因实验: A 臂 (仅 Task 1 标签改动) = **87.50% 逐题 Δ0** ⇒ 致害**全部**来自本行。
> 机制: 959 卡的该行**仅 46 种取值**, 最大簇 **175 卡 (18.2%) 逐字相同**; 两道回归题本就在
> **rank 15/15** 压线, 被同簇兄弟卡挤出 top-k (q14 顶替者仅赢 0.0002 sim)。
> **这正是 spec §2 Out of scope 早已点名的机制**「事件层进向量库切 chunk (增量是关系型,
> 走确定性通道)」—— 回归是违反自家原则的可预期后果。
> **终态**: `collect_scope` 推导与单测**保留** (spec §2.3 仍 in-scope, 数据经 catalog 三池
> 由 Task 6 的 `study_lookup` 直查交付); 生产 `build_cards` 传 `assignments=None`, **不渲染该行**。
> 完整归档 → `sdtm-rag/evidence/failures/t4_step7_retrieval_regression.md`
> **引用纪律: 一律写「S3 触发, 用户裁定执行退回」, 不得写成「未触发」或「验收通过」。**


**Files:**
- Modify: `scripts/study/build_field_cards.py` (新增推导函数 + 渲染行 + 调用处传参)
- Test: `scripts/tests/test_build_field_cards.py` (追加 3 个测试)

**Interfaces:**
- Consumes: Task 3 的 `catalog["assignments"]`; Task 1 的 `_HIDDEN_ACT_KEY`
- Produces:
  - `collect_scope(item: dict, assignments: list[dict]) -> list[str]` — 返回该 item 实际被采集的 activity OID 有序列表 (按 assignments 出现顺序去重)
  - 卡片新增一行 `- 収集アクティビティ: <逗号分隔>` 或 `- 収集アクティビティ: —`, 位置在 `- 非表示アクティビティ:` 行**之后**

**推导规则 (spec §2.3)**:
```
collect_scope(item) = { a.activity_oid | a ∈ assignments, a.form_oid == item.form_oid }
                    − { item 的 Hidden in activity 集合 }
```

- [ ] **Step 1: 写失败的测试**

⚠ **顺带修一处 Minor (控制方 Ruling M-2)**: 本文件第 72 行 docstring 里的
`(实测 61/61 逐键相同)` 缺出处, 违反本仓「『实测』须附可复跑来源」的规矩。改为:
`(实测 61/61 逐键相同 — 见 spec §4 F3 与 evidence/checkpoints/c2_pre_survey.md §8-5)`。

在 `scripts/tests/test_build_field_cards.py` 末尾追加:

```python
def test_collect_scope_subtracts_hidden():
    """采集范围 = form 被分配到的 activity - 该 item 被隐藏的 activity."""
    from scripts.study.build_field_cards import collect_scope
    assignments = [
        {"form_oid": "偽F", "activity_oid": "偽A1"},
        {"form_oid": "偽F", "activity_oid": "偽A2"},
        {"form_oid": "偽F", "activity_oid": "偽A3"},
        {"form_oid": "偽G", "activity_oid": "偽A9"},   # 别的 form, 不算
    ]
    item = {"form_oid": "偽F",
            "raw": {"Visibility::Hidden in activity": "偽A2"}}
    assert collect_scope(item, assignments) == ["偽A1", "偽A3"]


def test_collect_scope_empty_hidden_keeps_all():
    from scripts.study.build_field_cards import collect_scope
    assignments = [{"form_oid": "偽F", "activity_oid": "偽A1"},
                   {"form_oid": "偽F", "activity_oid": "偽A1"}]   # 重复 → 去重
    item = {"form_oid": "偽F", "raw": {}}
    assert collect_scope(item, assignments) == ["偽A1"]


def test_render_collect_scope_row(catalog):
    """卡片新增 収集アクティビティ 行, 位于 非表示アクティビティ 之后."""
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["raw"] = {**item["raw"], "Visibility::Hidden in activity": "偽アクティビティ甲"}
    assignments = [{"form_oid": item["form_oid"], "activity_oid": "偽アクティビティ甲"},
                   {"form_oid": item["form_oid"], "activity_oid": "偽乙"}]
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW", assignments=assignments)
    assert "- 収集アクティビティ: 偽乙" in card
    lines = card.splitlines()
    i_hidden = next(i for i, l in enumerate(lines) if l.startswith("- 非表示アクティビティ:"))
    i_scope = next(i for i, l in enumerate(lines) if l.startswith("- 収集アクティビティ:"))
    assert i_scope == i_hidden + 1
```

- [ ] **Step 2: 运行测试, 确认失败**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_build_field_cards.py -p no:warnings -q 2>&1 | tail -5
```

Expected: FAIL — `ImportError: cannot import name 'collect_scope'`。

- [ ] **Step 3: 备份卡片基线**

```bash
cd sdtm-rag
rm -rf /tmp/cards_baseline_t4 && cp -R data/study/st01/cards /tmp/cards_baseline_t4
```

- [ ] **Step 4: 写实现**

在 `scripts/study/build_field_cards.py` 中, `render_field_card` 之前新增:

```python
def collect_scope(item: dict, assignments: list[dict]) -> list[str]:
    """item 实际被采集的 activity OID (有序去重).

    = (该 item 所属 form 被分配到的 activity) − (该 item 的 Hidden in activity)
    两个输入都出自同一份 ConfigReport, 故本推导是确定性的, 无推断成分。
    """
    hidden = {
        x.strip()
        for x in str(item["raw"].get(_HIDDEN_ACT_KEY) or "").replace("\n", ",").split(",")
        if x.strip()
    }
    out: list[str] = []
    for a in assignments:
        if a["form_oid"] != item["form_oid"]:
            continue
        oid = a["activity_oid"]
        if oid and oid not in hidden and oid not in out:
            out.append(oid)
    return out
```

`render_field_card` 的签名追加关键字参数 `assignments: list[dict] | None = None`。
在 Task 1 改过的那个 `if item["raw"].get(_HIDDEN_ACT_KEY):` 块**之后**追加:

```python
    # 収集アクティビティ = form 分配 − item 隐藏 (spec §2.3)。恒输出该行 (含 '—'),
    # 因为"哪里都不采集"与"没算过"必须可区分 —— 缺席会被读成前者。
    if assignments is not None:
        scope = collect_scope(item, assignments)
        lines.append(f"- 収集アクティビティ: {', '.join(scope) if scope else '—'}")
```

在本文件里调用 `render_field_card` 的地方 (`main` 内的循环), 把 catalog 的 assignments 传进去:
```python
        card = render_field_card(item, form, group, samples, diff,
                                 study=study, version=version,
                                 assignments=cat.get("assignments", []))
```
⚠ 实现者注意: 上面这一行的**前 6 个位置参数照抄当前文件里已有的调用**, 只追加 `assignments=` 这一个关键字参数。不要改动既有参数顺序。

- [ ] **Step 5: 运行测试, 确认通过**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_build_field_cards.py -p no:warnings -q 2>&1 | tail -3
```

Expected: `22 passed` (19 + 3)。

- [ ] **Step 6: 重渲染 + 回归闸**

```bash
cd sdtm-rag
.venv/bin/python -m scripts.study.build_field_cards --study st01
.venv/bin/python - <<'PY'
import pathlib
base = pathlib.Path('/tmp/cards_baseline_t4'); new = pathlib.Path('data/study/st01/cards')
assert {p.name for p in base.glob('*.md')} == {p.name for p in new.glob('*.md')}
unexpected = 0; changed = 0
NEW = '- 収集アクティビティ: '
for p in sorted(new.glob('*.md')):
    a = (base/p.name).read_text(encoding='utf-8').splitlines()
    b = p.read_text(encoding='utf-8').splitlines()
    if a == b:
        continue
    changed += 1
    # 从新卡剔除所有新增行, 结果必须与基线逐行逐字相等 (顺序敏感, 无 diff 标记碰撞)
    if [l for l in b if not l.startswith(NEW)] != a:
        unexpected += 1
        print("UNEXPECTED", p.name)
    elif sum(1 for l in b if l.startswith(NEW)) != 1:
        unexpected += 1
        print("NOT-EXACTLY-ONE", p.name)
print(f"变化卡片 {changed} (期望 959 = 全部 field card 都加了新行) / 非预期变化 {unexpected} (期望 0)")
assert changed == 959 and unexpected == 0
print("PASS: 每张卡只新增了一行")
PY
```

Expected: `变化卡片 959 ... / 非预期变化 0` + `PASS`。
⚠ **959 不是 961**: `cards/` 下另有 `INDEX.md` 与 `ROUTING.md` 两个索引文件, 它们不是 field card, 不获得新行 (实测 959 张 `st01__` 前缀卡 = catalog items 数)。
**任何非预期变化 → spec §6 S3 触发, 退回本任务卡片改动。**

- [ ] **Step 7: 检索侧回归 (spec §5.D 第 2/3 条) — ⚠ 本步同时了结 Task 1 与 Task 4 两次卡片改动**

> **控制方 Ruling I-1 (2026-08-25)**: Task 1 的标签修复只到了生成器与磁盘卡片, **没到线上索引**
> (实证: 重灌前 `chroma.sqlite3` 内旧标签 943 处 / 新标签 0 处; `server/` 无任何读 `cards/*.md`
> 的代码路径, 线上文本全部来自 chroma 落盘)。spec §5.D 的 D.2/D.3 在 T1 **未执行**。
> **本步骤是这两次改动共同的 §5.D.2/D.3 验收点 —— 不得默认「T1 已闭合 §5.D」。**
> 重灌索引后确认旧标签已从索引消失。⛔ **不要对 chroma.sqlite3 做 raw grep** ——
> 控制方实测: 那样会看到**已删除但未 vacuum 的空闲页残留** (重灌后 raw grep 仍得 4,
> 而逻辑内容实为 0)。必须走 chromadb API 查真实文档:
> ```bash
> cd sdtm-rag
> .venv/bin/python - <<'PY'
> import chromadb
> c = chromadb.PersistentClient(path='data/chroma')
> for name in ('study_st01', 'study_st01_docs', 'sdtm_kb_v1'):
>     docs = c.get_collection(name).get(include=['documents'])['documents'] or []
>     f = lambda s: sum(1 for d in docs if d and s in d)
>     print(f"{name:18s} n={len(docs):5d} 旧={f('適用範囲'):4d} 非表示={f('非表示アクティビティ'):4d} 収集={f('収集アクティビティ'):4d}")
> PY
> ```
> 期望 (**S3 退回后的终态**): `study_st01` → 旧=**0** · 非表示=**231** · 収集=**0**;
> 另两个 collection 三项皆 0。
> ⚠ **収集 期望是 0 不是 959** —— 用户裁定执行 S3 后生产不渲染该行, 故它不入向量库。
> (若将来有人重新开启该行, 那时才应为 959, 但开启前必须先解决同质簇挤占, 见 Task 4 顶部横幅。)
> (231 与 959 分别对上"有 hidden 列表的卡数"与"全部 field card 数", 是索引侧与磁盘侧的交叉核对。)

> ⛔ **必须先停线上服务再重灌 (控制方 Ruling T4-launchd)**: `ingest_study` 用
> `client.delete_collection()` 删除后重建 collection, 而 `server/rag.py:92-93` 在 lifespan
> 启动时就 `get_collection()` **持有句柄** —— 边跑边灌会让线上句柄指向已删除的 collection。
> 实测线上 `com.sdtmrag.api` 正在运行 (`/api/health` = 200)。

```bash
cd sdtm-rag
launchctl bootout gui/$(id -u)/com.sdtmrag.api 2>/dev/null || launchctl stop com.sdtmrag.api
.venv/bin/python -m scripts.study.ingest_study --study st01
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api
sleep 5
curl -s -o /dev/null -w 'health=%{http_code}\n' --max-time 5 http://localhost:8000/api/health
for i in 1 2 3; do
  .venv/bin/python -m eval.run_eval --test-set data/study/st01/eval/test_set_study_v2.yml \
    --retrieval-only --out /tmp/t4_run_$i.json
done
.venv/bin/python - <<'PY'
import json
runs = [json.load(open(f'/tmp/t4_run_{i}.json')) for i in (1, 2, 3)]
def per_q(r):
    return {q['id']: q.get('source_recall') for q in r['questions']}
a, b, c = map(per_q, runs)
assert a == b == c, "三遍不稳定"
overall = runs[0].get('overall_source_recall')
print(f"三遍逐题稳定 ✓  overall={overall}")
print("对照基线 87.50% — 必须逐题 Δ0")
PY
```

Expected: 三遍逐题稳定, overall 与基线 **87.50%** 一致。
⚠ 实现者注意: `run_eval` 的实际 flag 名以 `.venv/bin/python -m eval.run_eval --help` 为准; 上面是既有 study 轨评测的惯用形态。**若 overall ≠ 87.50% 或出现任何逐题回归 → spec §6 S3 触发, 退回。**

- [ ] **Step 8: 全量测试 + 提交**

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
git add scripts/study/build_field_cards.py scripts/tests/test_build_field_cards.py
git commit -m "feat(study-cards): 新增 収集アクティビティ 行 — item 真实采集范围确定性推导

collect_scope = (form 被分配到的 activity) - (item 的 Hidden in activity)。
两个输入同出一份 ConfigReport, 零推断。959 张 field card 各新增一行 (无采集范围输出 '—',
与'没算过'可区分)。逐卡 diff 闸: 只新增该行, 非预期变化 0。
检索侧三遍逐题稳定, study golden v2 逐题 Δ0。"
```

Expected: `passed=1713` → `passed=1716`。

---

## Task 5: event 侧 gold 题集 (尺子先于接线)

**Files:**
- Create: `data/study/st01/eval/test_set_events_v1.yml` (**gitignored — 含真实 OID/题面**)
- Create: `data/study/st01/eval/EVENTS_V1_NOTES.md` (**gitignored** — 逐题裁定笔记)
- Modify: `eval/lint_gold.py` (新增 `--events-catalog` 全集来源)
- Test: `scripts/tests/test_lint_gold_events.py` (**Create**, 用伪值 fixture)

**Interfaces:**
- Consumes: Task 3 的 `catalog["events"]` / `["activities"]` / `["assignments"]`
- Produces: 冻结的 event 侧题集 + 可执行 lint 闸

**硬顺序 (spec §5.E)**: 本任务必须在 Task 6 **之前**完成并冻结。

**出题纪律 (照抄 study golden v2 的既有做法)**:
- 出题时**不看** `cards/*.md`, 不跑检索系统
- 依据 = `catalog["events"]/["activities"]/["assignments"]` 的结构 + 临床自然问法
- gold 唯一性必须过 lint (退出码 0)
- **逐题重新裁定**: `evidence/checkpoints/c2_pre_survey.md` §7-4 那 10 道候选可作起点, 但它们当初的判据是「961 张卡片答不出」, 现在语义已变成「workflow 三池能不能答出」——**每一题都要重新判, 不许整批搬运**

- [ ] **Step 1: 写 lint 扩展的失败测试**

Create `scripts/tests/test_lint_gold_events.py`:

```python
"""event 侧 gold 的唯一性闸. 零真名: 全部用伪 OID."""
import json

import pytest

from eval.lint_gold import event_target_names


def test_event_target_names_covers_three_pools(tmp_path):
    cat = {
        "events": [{"oid": "偽EV1"}, {"oid": "偽EV2"}],
        "activities": [{"oid": "偽AC1", "event_oid": "偽EV1"}],
        "assignments": [{"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"}],
    }
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps(cat), encoding="utf-8")
    names = event_target_names(p)
    assert "event:偽EV1" in names
    assert "event:偽EV2" in names
    assert "activity:偽EV1/偽AC1" in names
    assert "assignment:偽EV1/偽AC1/偽F" in names
    assert len(names) == 4


def test_event_target_names_are_unique(tmp_path):
    cat = {"events": [{"oid": "偽EV1"}, {"oid": "偽EV1"}],
           "activities": [], "assignments": []}
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps(cat), encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate"):
        event_target_names(p)
```

- [ ] **Step 2: 运行测试, 确认失败**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_lint_gold_events.py -p no:warnings -q 2>&1 | tail -5
```

Expected: FAIL — `ImportError: cannot import name 'event_target_names'`。

- [ ] **Step 3: 写实现**

在 `eval/lint_gold.py` 中, `doc_chunk_names` 函数之后追加:

```python
def event_target_names(catalog_path: Path | str) -> list[str]:
    """event 侧 gold 的全集: 三池各自的目标名 (与 catalog ledger 的 target 同构).

    命名与 build_catalog 的 ledger target 保持一致, 让 gold 可直接对照台账溯源。
    """
    cat = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
    names: list[str] = []
    for e in cat.get("events", []):
        names.append(f"event:{e['oid']}")
    for a in cat.get("activities", []):
        names.append(f"activity:{a['event_oid']}/{a['oid']}")
    for s in cat.get("assignments", []):
        names.append(f"assignment:{s['event_oid']}/{s['activity_oid']}/{s['form_oid']}")
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        raise ValueError(f"duplicate event target names: {sorted(dupes)[:5]}")
    return names
```

在 `main` 的参数组 `src` 中追加一个互斥选项:
```python
    src.add_argument("--events-catalog", help="event 侧 gold 全集来源 (catalog.json 三池)")
```
并在 `_load` 里按同样方式接上 (照抄 `--docs-dir` 那一支的写法, 把 `doc_chunk_names` 换成 `event_target_names`)。

- [ ] **Step 4: 运行测试, 确认通过**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_lint_gold_events.py -p no:warnings -q 2>&1 | tail -3
```

Expected: `2 passed`。

- [ ] **Step 5: 出题 (人工, 逐题裁定)**

写 `data/study/st01/eval/test_set_events_v1.yml`, 沿用 `test_set_study_v2.yml` 的字段结构 (`id` / `question` / `expected_sources` / `expected_facts`)。

**题型配比 (至少覆盖)**:
1. 事件时点定义 (答案落在 `activities[].name`)
2. 事件下的表单分配 (答案落在 `assignments`)
3. 重复规则 (`assignments[].repeating == "Unlimited"` 的那 4 条)
4. 条件付き实施 (`events[].visibility_condition` 非空的那 6 条)
5. **OID ↔ 人类可读名双向** (给 OID 问名称 / 给名称问 OID)
6. **item 采集范围** (Task 4 的 `収集アクティビティ`)

**每题必须在 `EVENTS_V1_NOTES.md` 记录**: 出题依据、答案在哪一池哪一行、以及**为什么认为现实中会有人问**(这是 `c2_pre_survey.md` §7-4 没做的那一层)。

题量建议 **20-30 道**。**不足 20 道就说明这一层没有足够可问的东西, 按 spec §6 S4 的精神停下来问用户。**

- [ ] **Step 6: 过 lint 闸**

```bash
cd sdtm-rag
.venv/bin/python -m eval.lint_gold data/study/st01/eval/test_set_events_v1.yml \
  --events-catalog data/study/st01/catalog.json
echo "exit=$?"
```

Expected: `exit=0`。非 0 则改 gold, **不许改 lint 迁就 gold**。

- [ ] **Step 7: 红线扫描 + 提交**

```bash
cd sdtm-rag
git status --porcelain data/study/    # 期望空 —— data/study/ 已 gitignore
git add eval/lint_gold.py scripts/tests/test_lint_gold_events.py
git commit -m "feat(eval): lint_gold 支持 event 侧 gold 全集 (--events-catalog)

三池目标名与 build_catalog 的 ledger target 同构, 便于 gold 对照台账溯源。
题集本体在 data/study/ (gitignored, 零进 git)。"
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
```

Expected: `passed=1718` (1716 + 2)。

---

## Task 6: 接 `study_lookup` 事件通道 + 实测 + 规则 D 收口

**Files:**
- Modify: `server/study_lookup.py`
- Test: `scripts/tests/test_study_lookup_events.py` (**Create**)
- Create: `sdtm-rag/evidence/checkpoints/study_workflow_events.md`

**Interfaces:**
- Consumes: Task 3 的三池; Task 5 的题集与 lint 闸
- Produces: `StudyLookup.resolve_events(query: str) -> list[str]` — 返回命中的 event/activity 目标名 (与 Task 5 的 `event_target_names` 同命名空间), 上限 `_MAX_EVENTS_TOTAL = 8`

- [ ] **Step 1: 写失败的测试**

Create `scripts/tests/test_study_lookup_events.py`:

```python
"""事件通道: OID 与名称双向命中. 零真名: 全部伪值."""
from server.study_lookup import StudyLookup

CAT = {
    "study": "st01",
    "items": [{"form_oid": "偽F", "item_oid": "偽IT_A", "label": "偽ラベル甲",
               "raw": {}}],
    "events": [{"oid": "偽EV1", "name": "偽イベント名甲", "event_type": "偽型",
                "description": "", "visibility_condition": "",
                "sched_reference": "", "sched_minus_days": "", "sched_plus_days": ""}],
    "activities": [{"oid": "偽AC1", "event_oid": "偽EV1", "name": "偽活動名乙",
                    "event_name": "偽イベント名甲", "description": "",
                    "visibility_condition": ""}],
    "assignments": [{"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F",
                     "event_name": "偽イベント名甲", "activity_name": "偽活動名乙",
                     "repeating": "0", "item_visibility": "", "hidden_items": ""}],
}


def test_resolve_events_by_oid():
    lk = StudyLookup(CAT)
    assert "event:偽EV1" in lk.resolve_events("偽EV1 について教えて")


def test_resolve_events_by_name():
    lk = StudyLookup(CAT)
    assert "event:偽EV1" in lk.resolve_events("偽イベント名甲 はいつ実施しますか")


def test_resolve_activity_by_name():
    lk = StudyLookup(CAT)
    assert "activity:偽EV1/偽AC1" in lk.resolve_events("偽活動名乙 のタイミングは")


def test_resolve_events_empty_on_no_hit():
    lk = StudyLookup(CAT)
    assert lk.resolve_events("まったく無関係な質問") == []


def test_resolve_events_missing_pools_degrades_quietly():
    """老 catalog (无三池) 不许炸 —— 三池是新增, 旧数据要能跑."""
    lk = StudyLookup({"study": "st01", "items": CAT["items"]})
    assert lk.resolve_events("偽EV1") == []
```

- [ ] **Step 2: 运行测试, 确认失败**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_study_lookup_events.py -p no:warnings -q 2>&1 | tail -5
```

Expected: FAIL — `AttributeError: 'StudyLookup' object has no attribute 'resolve_events'`。

- [ ] **Step 3: 写实现**

在 `server/study_lookup.py` 顶部常量区追加:
```python
_MAX_EVENTS_TOTAL = 8      # 事件命中上限 (与 _MAX_CARDS_TOTAL 同精神: 超出=不具判别力)
_MIN_EVENT_NAME_LEN = 3    # 名称索引最短长度, 防短名命中一切
```

在 `StudyLookup.__init__` 末尾追加:
```python
        # 事件层索引 (三池是 2026-08-25 新增, 老 catalog 无此 key → 空索引, 静默降级)
        self._event_index: dict[str, list[str]] = defaultdict(list)
        for e in catalog.get("events", []):
            target = f"event:{e['oid']}"
            self._event_index[_norm(e["oid"])].append(target)
            n = _norm(e.get("name", ""))
            if len(n) >= _MIN_EVENT_NAME_LEN:
                self._event_index[n].append(target)
        for a in catalog.get("activities", []):
            target = f"activity:{a['event_oid']}/{a['oid']}"
            self._event_index[_norm(a["oid"])].append(target)
            n = _norm(a.get("name", ""))
            if len(n) >= _MIN_EVENT_NAME_LEN:
                self._event_index[n].append(target)
```

新增方法:
```python
    def resolve_events(self, query: str) -> list[str]:
        """事件层命中: OID 与名称双向, 子串匹配, 有序去重, 上限 _MAX_EVENTS_TOTAL。

        与 resolve() 分开是刻意的 —— 事件目标名不是卡名, 混进 cards 会让调用方
        把它当 chunk 去取, 那是静默的类型错误。
        """
        qn = _norm(query)
        out: list[str] = []
        for key, targets in self._event_index.items():
            if key and key in qn:
                for t in targets:
                    if t not in out:
                        out.append(t)
        return out[:_MAX_EVENTS_TOTAL]
```

- [ ] **Step 4: 运行测试, 确认通过**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_study_lookup_events.py -p no:warnings -q 2>&1 | tail -3
```

Expected: `5 passed`。

- [ ] **Step 5: 全量测试 + 既有回归**

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/dev/null 2>&1; echo "rc=$?"
.venv/bin/python -c "
import xml.etree.ElementTree as ET
r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
"
```

Expected: `passed=1723` (1718 + 5)。**既有 1699 条一条都不许红。**

- [ ] **Step 6: 用 Task 5 的题集实测**

```bash
cd sdtm-rag
.venv/bin/python - <<'PY'
import json, pathlib, yaml
from server.study_lookup import StudyLookup
cat = json.loads(pathlib.Path('data/study/st01/catalog.json').read_text())
qs = yaml.safe_load(pathlib.Path('data/study/st01/eval/test_set_events_v1.yml').read_text())
lk = StudyLookup(cat)
hit = tot = 0
misses = []
for q in (qs["questions"] if isinstance(qs, dict) else qs):
    got = set(lk.resolve_events(q["question"]))
    want = set(q["expected_sources"])
    tot += 1
    if want & got:
        hit += 1
    else:
        misses.append(q["id"])
print(f"事件通道命中率: {hit}/{tot} = {100*hit/tot:.2f}%")
print(f"未命中: {misses}")
PY
```

记录该数字。**这是本单元的主结果, 不许只报一个总分 —— 未命中题必须逐题写进证据。**

- [ ] **Step 7: 卡片侧不回归确认 (spec §5.D)**

```bash
cd sdtm-rag
for i in 1 2 3; do
  .venv/bin/python -m eval.run_eval --test-set data/study/st01/eval/test_set_study_v2.yml \
    --retrieval-only --out /tmp/t6_run_$i.json
done
.venv/bin/python - <<'PY'
import json
runs = [json.load(open(f'/tmp/t6_run_{i}.json')) for i in (1, 2, 3)]
per = [{q['id']: q.get('source_recall') for q in r['questions']} for r in runs]
assert per[0] == per[1] == per[2], "三遍不稳定"
print("三遍逐题稳定 ✓ overall =", runs[0].get('overall_source_recall'), "(基线 87.50%)")
PY
```

- [ ] **Step 8: 写收口证据**

Create `sdtm-rag/evidence/checkpoints/study_workflow_events.md`, 必含:
- 各闸实测值 (A: 110/21/109/1 · B: 四条 · C: 61/61 · D: 逐卡 diff 与三遍稳定 · E: lint exit=0)
- Task 6 Step 6 的命中率 + **逐题未命中清单**
- 测试数 1699 → 1722
- **已知限制**至少含: ① `Scheduling::Days/After/recurrence` 与 `Timing::*` 本研究全空, 时点语义承载在 `Activity name` 自由文本, 故"结构化调度"不成立; ② 脚注判据是启发式 (ID 空或含空格), 换研究/换版本可能失效, 由闸 A 四条数字看守; ③ `resolve_events` 是子串匹配, 与 `resolve()` 的四通道不同源, 未做挤占分析
- **引用纪律**: 本单元不得写「SDTM 映射已支持」—— TA/TE/TV/SV 映射是 spec §2 明确 out of scope

- [ ] **Step 9: 规则 D 三方核验 (不许自审)**

派两个**不同 `subagent_type`** 的 agent (与实现方均不同):
1. **抽检方**: 独立重跑闸 A/B/C 的全部数字, 用**非自洽写法**复算 (不复用本计划的脚本), 报告是否逐位吻合
2. **审查方**: 对抗性复核 —— 重点查 `collect_scope` 的减法是否有边界遗漏、`resolve_events` 的子串匹配会不会误命中、证据文件的引用纪律

两方报告落盘 `sdtm-rag/evidence/step_workflow_events_audit{,_review}.md`。**拿不到报告就当那一环没发生并在证据里点名** (kickoff 硬规矩 17)。

- [ ] **Step 10: 红线扫描 + 提交**

```bash
cd sdtm-rag
.venv/bin/python - <<'PY'
import json, pathlib, re, glob, unicodedata, subprocess
d = json.loads(pathlib.Path('data/study/st01/catalog.json').read_text())
def norm(s): return re.sub(r'\s+', '', unicodedata.normalize('NFKC', str(s))).lower()
corp = []
for pool in ('items', 'forms', 'events', 'activities', 'assignments'):
    for r in d.get(pool, []):
        for k, v in r.items():
            if k == 'raw' and isinstance(v, dict): corp += [str(x) for x in v.values()]
            else: corp.append(str(v))
for cl in d['codelists'].values():
    for e in cl['entries']: corp += [str(x) for x in (e if isinstance(e, list) else [e])]
CAT = norm(' '.join(corp))
CARDS = norm(' '.join(pathlib.Path(p).read_text() for p in glob.glob('data/study/st01/cards/*.md')))
SRC = norm(subprocess.run(['git', 'grep', '-h', '', '--', '*.py'], capture_output=True, text=True).stdout)
bad = []
for f in ['evidence/checkpoints/study_workflow_events.md',
          'scripts/tests/test_parse_workflow_sheets.py',
          'scripts/tests/test_catalog_workflow_pools.py',
          'scripts/tests/test_study_lookup_events.py',
          'scripts/tests/test_lint_gold_events.py']:
    p = pathlib.Path(f)
    if not p.exists(): continue
    doc = p.read_text()
    for r in set(re.findall(r'[぀-ヿ一-鿿]{3,}', doc)):
        if (norm(r) in CAT or norm(r) in CARDS) and norm(r) not in SRC:
            bad.append((f, r))
print("红线渗漏:", bad if bad else "0 ✅")
assert not bad
PY
git add scripts/tests/test_study_lookup_events.py server/study_lookup.py \
        evidence/checkpoints/study_workflow_events.md evidence/step_workflow_events_audit*.md
git commit -m "feat(study-lookup): 事件层确定性查询通道 + 单元收口

resolve_events: OID 与名称双向子串命中, 与 resolve() 分开 (事件目标名不是卡名,
混进 cards 是静默类型错误)。老 catalog 无三池时静默降级为空索引。
1699 -> 1722 passed; 卡片侧三遍逐题稳定, study golden v2 无回归。
规则 D 三方核验齐备。"
```

---

## Self-Review

**1. Spec coverage**

| spec 条目 | 落在哪个 Task |
|---|---|
| §2 In scope 1 事件层入 catalog | T2 (解析) + T3 (入池) |
| §2 In scope 2 OID ↔ 名称打通 | T6 `resolve_events` 双向索引 |
| §2 In scope 3 item 采集范围推导 | T4 `collect_scope` |
| §2 In scope 4 修 `適用範囲` 缺陷 | T1 |
| §2 In scope 5 event 侧 gold | T5 |
| §2 In scope 6 接 `study_lookup` | T6 |
| §2 Out of scope (PDF / SDTM 映射 / 切 chunk / LLM) | Global Constraints + T6 Step 8 引用纪律 |
| §3 数据模型三池 + ledger 扩展 | T3 Step 3 |
| §5.A 交叉核对闸 | T3 `test_gate_a_cross_check_against_design_summary` |
| §5.B 引用完整性闸 | T3 `test_gate_b_referential_integrity` |
| §5.C 转置一致性闸 | T3 `test_gate_c_transpose_consistency` |
| §5.D 卡片侧回归闸 (3 条) | T1 Step 8 · T4 Step 6 · T4 Step 7 / T6 Step 7 |
| §5.E 尺子先于接线 | T5 在 T6 之前 (硬顺序, 已在 T5 标注) |
| §6 S1 | T3 Step 4 (闸 A 失败即停) |
| §6 S2 | T3 Step 4 显式指示: 闸 C 失败停止且不得进 T4 |
| §6 S3 | T1 Step 8 · T4 Step 6/7 均写明退回 |
| §6 S4 | T5 Step 5 (题量不足 20 即停下问用户) |
| §8 红线/规则 D/规则 B | Global Constraints + T6 Step 9/10 |
| §9.1 改动面风险 | T1/T4 的备份 + 逐卡 diff 闸 |
| §9.3 脚注启发式风险 | T2 `_is_footnote` + T3 三个响亮失败 guard + 闸 A 看守 |

**计划相对 spec §7 的一处扩展**: spec 的四步表把 §2.3 的采集范围推导折在任务 1 里未单列。本计划展开为 6 个 Task (解析与入池拆开、采集范围独立成 T4), 理由是各自有独立测试周期且可被独立驳回。**范围未变**, 全部落在 spec §2 In scope 内。

**2. Placeholder scan**: 全部步骤含可执行命令或完整代码块; 无 TBD/TODO/"类似 Task N"。T4 Step 4 与 T4 Step 7 各有一处 ⚠ 提示实现者以文件现状/`--help` 为准, 这是**已知不确定性的显式标注**, 非占位符。

**3. Type consistency**: `collect_scope(item, assignments)` 在 T4 定义与调用一致; `event_target_names` 在 T5 定义、T6 Step 6 沿用同一命名空间 (`event:` / `activity:` / `assignment:`), 与 T3 的 ledger `target` 同构; `_HIDDEN_ACT_KEY` 在 T1 改名后 T4 沿用; `resolve_events` 返回 `list[str]` 与 T6 测试一致。
