"""parse_demo v2: 三路合并 + form 作用域解析. 全合成数据, 无真实研究内容."""
from pathlib import Path

import openpyxl
import pytest

from scripts.study.parse_demo import sample_demo_values

# 合成 catalog: FAKEFORM1 六项 (含同 label 歧义对) + OTHERFORM 一项 (作用域测试)
CATALOG_ITEMS = [
    {"item_oid": "FAKEIT1", "form_oid": "FAKEFORM1", "label": "ラベル壱"},
    {"item_oid": "FAKEIT2", "form_oid": "FAKEFORM1", "label": "ラベル弐"},
    {"item_oid": "FAKEIT3", "form_oid": "FAKEFORM1", "label": "ラベル参"},
    {"item_oid": "FAKEIT4", "form_oid": "FAKEFORM1", "label": "ラベル肆"},
    {"item_oid": "FAKEIT5", "form_oid": "FAKEFORM1", "label": "ダブり"},
    {"item_oid": "FAKEIT6", "form_oid": "FAKEFORM1", "label": "ダブり"},
    {"item_oid": "FAKEIT7", "form_oid": "OTHERFORM", "label": "ラベル漆"},
]


def _write_demo(path: Path, *, with_items_sheet: bool = True) -> Path:
    wb = openpyxl.Workbook()
    wb.active.title = "README"
    ws = wb.create_sheet("FAKEFORM1")
    # 列头依次命中: 非列 / (a)直配OID / (c)域内label / (b)Items字典 / 歧义 / 跨form越界
    ws.append(["SubjectId", "FAKEIT1", "ラベル弐", "デモ側ラベル肆", "ダブり", "FAKEIT7"])
    for r in [
        ("S1", 1, "値甲", "X1", "d1", "z1"),
        ("S2", 0, "値乙", "X1", "d2", "z2"),
        ("S3", 1, "", "X2", "d3", "z3"),
        ("S4", 1, "値甲", "X2", "d4", "z4"),
    ]:
        ws.append(r)
    if with_items_sheet:
        it = wb.create_sheet("Items")          # DEMO 侧列名字典, 单行表头
        it.append(["ID", "Label", "Data Type"])
        it.append(["FAKEIT4", "デモ側ラベル肆", "text"])
        it.append(["FAKEUNKNOWN", "無関係", "text"])   # ID 不在 catalog, 应忽略
    wb.create_sheet("CodeLists")               # 字典 sheet, 应跳过
    wb.save(path)
    return path


@pytest.fixture()
def demo(tmp_path) -> Path:
    return _write_demo(tmp_path / "fake_demo.xlsx")


def test_three_resolution_paths(demo):
    samples, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert samples["FAKEIT1"] == ["1", "0"]           # (a) 直配 OID, 去重保序
    assert samples["FAKEIT2"] == ["値甲", "値乙"]      # (c) 域内 label, 空值跳过
    assert samples["FAKEIT4"] == ["X1", "X2"]         # (b) Items 字典 Label→ID
    assert stats["resolved_direct"] == 1
    assert stats["resolved_items_dict"] == 1
    assert stats["resolved_label"] == 1


def test_ambiguous_column_skipped(demo):
    samples, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert "FAKEIT5" not in samples                   # 同 form 内同 label 两候选 → 不猜
    assert "FAKEIT6" not in samples
    assert stats["ambiguous"] == 1


def test_form_scope_blocks_cross_form_column(demo):
    samples, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert "FAKEIT7" not in samples                   # OID 属 OTHERFORM, 在本 sheet 越界
    assert stats["unmatched"] == 2                    # SubjectId + FAKEIT7


def test_absent_item_not_reported(demo):
    samples, _ = sample_demo_values(demo, CATALOG_ITEMS)
    assert "FAKEIT3" not in samples                   # DEMO 里没有的项目不出现


def test_per_sheet_counts(demo):
    _, stats = sample_demo_values(demo, CATALOG_ITEMS)
    assert stats["per_sheet"] == {"FAKEFORM1": 3}     # README/Items/CodeLists 不计


def test_max_per_item(demo):
    samples, _ = sample_demo_values(demo, CATALOG_ITEMS, max_per_item=1)
    assert samples["FAKEIT1"] == ["1"]


def test_missing_items_sheet_degrades_gracefully(tmp_path):
    p = _write_demo(tmp_path / "no_items.xlsx", with_items_sheet=False)
    samples, stats = sample_demo_values(p, CATALOG_ITEMS)
    assert stats["resolved_items_dict"] == 0
    assert "FAKEIT4" not in samples                   # 少了字典就少一列, 其余不受影响
    assert samples["FAKEIT1"] == ["1", "0"]
    assert stats["unmatched"] == 3                    # 该列退化为未匹配
