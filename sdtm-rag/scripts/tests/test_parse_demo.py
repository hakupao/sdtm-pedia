"""parse_demo v3: 双表头行 (行1 label / 行2 OID) + 三路佐证 + 反回声. 全合成数据.

v2 误把行 2 (OID 表头) 当唯一数据行采样, 671 个"示例值"全是自身 OID 回声 —— 本文件的
fixture 结构按真实 DEMO 双表头重建, 并把反回声做成断言。
"""
from pathlib import Path

import openpyxl
import pytest

from scripts.study.parse_demo import sample_demo_values

CATALOG_ITEMS = [
    {"item_oid": "FAKEIT1", "form_oid": "FAKEFORM1", "label": "ラベル壱"},
    {"item_oid": "FAKEIT2", "form_oid": "FAKEFORM1", "label": "ラベル弐"},
    {"item_oid": "FAKEIT3", "form_oid": "FAKEFORM1", "label": "ラベル参"},
    {"item_oid": "FAKEIT4", "form_oid": "FAKEFORM1", "label": "ラベル肆"},
    {"item_oid": "FAKEIT5", "form_oid": "FAKEFORM1", "label": "ダブり"},
    {"item_oid": "FAKEIT6", "form_oid": "FAKEFORM1", "label": "ダブり"},
    {"item_oid": "FAKEIT7", "form_oid": "OTHERFORM", "label": "ラベル漆"},
    {"item_oid": "FAKEIT8", "form_oid": "FAKEFORM1", "label": "字典歧義"},
    {"item_oid": "FAKEIT9", "form_oid": "FAKEFORM1", "label": "ラベル玖"},
]

# 行1 = 日文 label 表头; 行2 = Item OID 表头 (系统列位置放系统列 ID, 同真实 DEMO)
_LABEL_ROW = ["被験者ID", "ラベル壱", "ラベル弐", "デモ側ラベル肆", "ダブり", "ラベル漆"]
_OID_ROW = ["SubjectId", "FAKEIT1", "FAKEIT2", "FAKEIT4", "FAKEIT5", "FAKEIT7"]
_DATA_ROWS = [
    ("S1", "1", "値甲", "X1", "d1", "z1"),
    ("S2", "0", "値乙", "X1", "d2", "z2"),
    ("S3", "1", "", "X2", "d3", "z3"),
    ("S4", "1", "値甲", "X2", "d4", "z4"),
]


def _add_items_sheet(wb, extra: list[tuple[str, str]] | None = None) -> None:
    it = wb.create_sheet("Items")          # DEMO 侧列名字典, 单行表头
    it.append(["ID", "Label", "Data Type"])
    it.append(["FAKEIT4", "デモ側ラベル肆", "text"])
    it.append(["FAKEUNKNOWN", "無関係", "text"])       # ID 不在 catalog, 应忽略
    it.append(["SubjectId", "被験者ID", "text"])        # 系统列也在字典里 (同真实 DEMO)
    for oid, label in extra or []:
        it.append([oid, label, "text"])


def _write_demo(path: Path, *, with_items_sheet: bool = True,
                data_rows: list[tuple] | None = None) -> Path:
    wb = openpyxl.Workbook()
    wb.active.title = "README"
    ws = wb.create_sheet("FAKEFORM1")
    ws.append(_LABEL_ROW)
    ws.append(_OID_ROW)
    for r in (_DATA_ROWS if data_rows is None else data_rows):
        ws.append(r)
    if with_items_sheet:
        _add_items_sheet(wb)
    wb.create_sheet("CodeLists")           # 字典 sheet, 应跳过
    wb.save(path)
    return path


@pytest.fixture()
def demo(tmp_path) -> Path:
    return _write_demo(tmp_path / "fake_demo.xlsx")


# --- 行2 OID 表头识别 + 数据自行3起 ---------------------------------------

def test_row2_oid_header_detected_data_starts_row3(demo):
    samples, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert stats["oid_header_sheets"] == 1
    assert stats["data_rows"] == 4          # 行2 不计入数据行
    assert samples["FAKEIT1"] == ["1", "0"]         # 去重保序
    assert samples["FAKEIT2"] == ["値甲", "値乙"]    # 空值跳过
    assert samples["FAKEIT4"] == ["X1", "X2"]


def test_row2_oid_is_authoritative_layer(demo):
    _, stats = sample_demo_values(demo, CATALOG_ITEMS)
    # SubjectId (系统列, 不在 catalog) 与 FAKEIT7 (属他 form) 落 unmatched
    assert stats["resolved_row2_oid"] == 4
    assert stats["unmatched"] == 2


def test_row2_resolves_column_that_label_path_finds_ambiguous(demo):
    """真实数据 201 个 label 歧义列全靠行2 OID 定案, 此处同构复现."""
    samples, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert samples["FAKEIT5"] == ["d1", "d2", "d3", "d4"]   # label 'ダブり' 本是二义
    assert "FAKEIT6" not in samples
    assert stats["ambiguous"] == 0          # 行2 定案后不再计歧义


def test_label_paths_corroborate_row2(demo):
    _, stats = sample_demo_values(demo, CATALOG_ITEMS)
    # ラベル壱/ラベル弐 走 (c), デモ側ラベル肆 走 (b); ダブり 二义故不构成佐证
    assert stats["corroborated"] == 3
    assert stats["conflict_row2_label"] == 0


def test_conflict_between_row2_and_label_is_counted(tmp_path):
    """行2 与 label 路指向不同 item → 必须计冲突, 这是映射层的安全网."""
    p = tmp_path / "conflict.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "FAKEFORM1"
    ws.append(["ラベル壱"])         # label 指向 FAKEIT1
    ws.append(["FAKEIT2"])          # 行2 OID 却指向 FAKEIT2
    ws.append(("v1",))
    _add_items_sheet(wb)
    wb.save(p)
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["conflict_row2_label"] == 1
    assert samples == {"FAKEIT2": ["v1"]}   # 以行2 为准


# --- 零数据行 (当前真实 DEMO 形态) ----------------------------------------

def test_zero_data_rows_yields_empty_samples(tmp_path):
    p = _write_demo(tmp_path / "no_data.xlsx", data_rows=[])
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert samples == {}                    # 全部卡片 DEMO 例値 = '—'
    assert stats["data_rows"] == 0
    assert stats["resolved_row2_oid"] == 4  # 映射关系仍然有效


# --- 反回声 ---------------------------------------------------------------

def test_value_equal_to_own_oid_is_dropped_as_echo(tmp_path):
    """采样值 == 自身 OID 即解析失败 (v2 的 671 个假示例值就是这个形态)."""
    p = _write_demo(tmp_path / "echo.xlsx",
                    data_rows=[("S1", "FAKEIT1", "値甲", "X1", "d1", "z1")])
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["echo_dropped"] == 1
    assert "FAKEIT1" not in samples
    assert samples["FAKEIT2"] == ["値甲"]   # 其余列不受影响


# --- 行2 非 OID 表头时退化为数据行 ----------------------------------------

def test_row2_not_oid_header_is_treated_as_data(tmp_path):
    """防未来导出真有数据从行2 开始: 行2 不像 OID 表头就当数据."""
    p = tmp_path / "plain.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "FAKEFORM1"
    ws.append(["ラベル壱", "ラベル弐"])
    ws.append(("値甲", "値乙"))            # 普通数据, 不是 OID
    ws.append(("値丙", "値丁"))
    _add_items_sheet(wb)
    wb.save(p)
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["oid_header_sheets"] == 0
    assert stats["data_rows"] == 2          # 行2 计入数据
    assert samples["FAKEIT1"] == ["値甲", "値丙"]
    assert stats["resolved_label"] == 2     # 退回 label 路


# --- 以下为 v2 已有契约, 在双表头结构下保持 --------------------------------

def test_absent_item_not_reported(demo):
    samples, _ = sample_demo_values(demo, CATALOG_ITEMS)
    assert "FAKEIT3" not in samples


def test_per_sheet_counts(demo):
    _, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert stats["per_sheet"] == {"FAKEFORM1": 4}
    assert stats["per_sheet_data_rows"] == {"FAKEFORM1": 4}


def test_max_per_item(demo):
    samples, _ = sample_demo_values(demo, CATALOG_ITEMS, max_per_item=1)
    assert samples["FAKEIT1"] == ["1"]


def test_items_dict_ambiguity_does_not_fall_through(tmp_path):
    """(b) 路歧义 (无行2 表头时): 不下坠 (c), 否则会误判为 FAKEIT8."""
    p = tmp_path / "b_ambig.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "FAKEFORM1"
    ws.append(["字典歧義"])
    ws.append(("v1",))                     # 非 OID → 行2 当数据
    _add_items_sheet(wb, extra=[("FAKEIT8", "字典歧義"), ("FAKEIT9", "字典歧義")])
    wb.save(p)
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["ambiguous"] == 1
    assert stats["resolved_items_dict"] == 0
    assert stats["resolved_label"] == 0     # 歧义后不下坠 (c)
    assert samples == {}


def test_unknown_sheet_counted(tmp_path):
    p = tmp_path / "ghost.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "GHOSTFORM"                 # 不在 catalog forms
    ws.append(["ラベル壱"])
    ws.append(("v1",))
    wb.save(p)
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["unknown_sheets"] == 1
    assert samples == {}


def test_known_sheets_not_counted_as_unknown(demo):
    _, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert stats["unknown_sheets"] == 0


def test_missing_items_sheet_degrades_gracefully(tmp_path):
    """无字典 → SubjectId 不在全集 → 5/6=0.83 < 0.9 → 行2 不判为 OID 表头, 退化为数据行."""
    p = _write_demo(tmp_path / "no_items.xlsx", with_items_sheet=False)
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["oid_header_sheets"] == 0
    assert stats["resolved_items_dict"] == 0
    assert stats["echo_dropped"] >= 1       # 行2 被当数据, 回声闸挡下
    assert samples["FAKEIT1"] == ["1", "0"]
