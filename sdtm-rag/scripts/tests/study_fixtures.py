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
# 三个 workflow sheet: Events/Activities 三行表头 (has_section_row=True), Forms 两行表头 —
# 与真实 ConfigReport 及 parse_config_report.py 消费的列名一致 (build_catalog 无条件消费三表)
WORKFLOW_EVENTS_HEADER = [
    ("General", "Study event ID"), ("General", "Event name"),
    ("General", "Study event description"), ("General", "Event type"),
    ("Visibility", "Visibility condition"),
    ("Scheduling", "Reference"), ("Scheduling", "- days"), ("Scheduling", "+ days"),
]
WORKFLOW_ACTIVITIES_HEADER = [
    ("General", "Activity ID"), ("General", "Study event ID"),
    ("General", "Event name"), ("General", "Activity name"),
    ("General", "Activity description"), ("General", "Visibility condition"),
]
WORKFLOW_FORMS_HEADER = [
    ("Study workflow-Forms", "Event ID"), ("Study workflow-Forms", "Event name"),
    ("Study workflow-Forms", "Activity ID"), ("Study workflow-Forms", "Activity name"),
    ("Study workflow-Forms", "Form ID"), ("Study workflow-Forms", "Repeating"),
    ("Study workflow-Forms", "Item visibility"), ("Study workflow-Forms", "Hidden items"),
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
# 每张表末尾各含 1 条脚注行 (ID 列写成含空格的整句), 让 is_trailer 分支与
# build_catalog 的三个新 guard 在合成路径上也有覆盖. Forms 表引用 event/activity 存在的 id,
# 保持引用完整性 (即便当前既有测试未断言此闸, 也不让合成路径给 build_catalog 的闸误红).
DEFAULT_WORKFLOW_EVENTS = [
    ("EV_FAKE01", "偽イベント一", "偽説明一", "偽タイプA", "", "", "", ""),
    ("EV_FAKE02", "偽イベント二", "偽説明二", "偽タイプB", "", "", "", ""),
    ("偽脚注: this row is a synthetic footnote.", "", "", "", "", "", "", ""),
]
DEFAULT_WORKFLOW_ACTIVITIES = [
    ("AC_FAKE01", "EV_FAKE01", "偽イベント一", "偽アクティビティ一", "", ""),
    ("AC_FAKE02", "EV_FAKE02", "偽イベント二", "偽アクティビティ二", "", ""),
    ("偽脚注: this row is a synthetic footnote.", "", "", "", "", ""),
]
DEFAULT_WORKFLOW_FORMS = [
    ("EV_FAKE01", "偽イベント一", "AC_FAKE01", "偽アクティビティ一",
     "FAKEFORM1", "0", "偽可視性A", "FAKEIT2"),
    ("EV_FAKE02", "偽イベント二", "AC_FAKE02", "偽アクティビティ二",
     "FAKEFORM2", "0", "偽可視性B", ""),
    ("偽脚注: this row is a synthetic footnote.", "", "", "", "", "", "", ""),
]


def _write_sheet(wb, title: str, header: list[tuple], rows: list[tuple], *,
                 has_section_row: bool = True) -> None:
    ws = wb.create_sheet(title)
    ws.append([title] * len(header))                       # 行1: sheet 名
    if has_section_row:
        sections = [s for s, _ in header]
        ws.append([s if i == 0 or sections[i - 1] != s else ""  # 行2: 分组, 重复留空
                   for i, s in enumerate(sections)])
    ws.append([c for _, c in header])                       # 末行表头: 列名
    for r in rows:
        ws.append(list(r))


def build_config_report(path: Path, *, items_rows=None, forms_rows=None,
                        codelist_rows=None, events_rows=None,
                        activities_rows=None, workflow_forms_rows=None) -> Path:
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    _write_sheet(wb, "Forms", FORMS_HEADER, forms_rows or DEFAULT_FORMS)
    _write_sheet(wb, "Items and Groups", ITEMS_HEADER, items_rows or DEFAULT_ITEMS)
    _write_sheet(wb, "Code lists", CODELIST_HEADER, codelist_rows or DEFAULT_CODELISTS,
                 has_section_row=False)   # 真实 Code lists 是两行表头
    _write_sheet(wb, "Study workflow-Events", WORKFLOW_EVENTS_HEADER,
                 events_rows or DEFAULT_WORKFLOW_EVENTS)
    _write_sheet(wb, "Study workflow-Activities", WORKFLOW_ACTIVITIES_HEADER,
                 activities_rows or DEFAULT_WORKFLOW_ACTIVITIES)
    _write_sheet(wb, "Study workflow-Forms", WORKFLOW_FORMS_HEADER,
                 workflow_forms_rows or DEFAULT_WORKFLOW_FORMS,
                 has_section_row=False)   # 真实 Study workflow-Forms 是两行表头
    wb.save(path)
    return path
