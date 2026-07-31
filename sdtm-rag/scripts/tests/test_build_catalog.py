import csv
import json

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


def test_write_catalog_outputs(sp):
    cat = build_catalog(sp)
    write_catalog(cat, sp.out_dir)
    data = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    assert data["study"] == "st01"
    with (sp.out_dir / "coverage_ledger.csv").open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert {"sheet", "row", "status", "target"} <= set(rows[0])
    assert len(rows) == len(cat["ledger"])


def test_ledger_per_sheet_counts(sp):
    """覆盖恒等式测试锁: 台账行数逐 sheet 等于源表数据行数 (部分漏账必红)."""
    from collections import Counter
    cat = build_catalog(sp)
    per_sheet = Counter(r["sheet"] for r in cat["ledger"])
    assert per_sheet == {"Forms": 2, "Items and Groups": 4, "Code lists": 3}


def test_unknown_field_type_raises(sp, tmp_path):
    """未知结构值 (非脚注形态) 必须响亮失败, 不得静默当脚注吞掉."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_ITEMS
    bad = ("FAKEFORM1", "偽フォーム一", "Section", "FG9", "") + ("",) * 16
    new = build_config_report(tmp_path / "bad.xlsx",
                              items_rows=list(DEFAULT_ITEMS) + [bad])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="Section"):
        build_catalog(sp2)
    # 多词未知类型 + item 载荷: 词形启发拦不住, 语义不变量 (item_oid 非空) 必须拦住
    bad2 = ("FAKEFORM1", "偽フォーム一", "Item matrix", "FG9", "",
            "FAKEIT9") + ("",) * 15
    new2 = build_config_report(tmp_path / "bad2.xlsx",
                               items_rows=list(DEFAULT_ITEMS) + [bad2])
    sp3 = replace(sp, config_report_new=new2, config_report_old=None)
    with pytest.raises(ValueError, match="Item matrix"):
        build_catalog(sp3)


def test_trailer_rows_in_ledger(sp, tmp_path):
    """脚注行 (含空格形态) 落 trailer:footnote, 不进 forms/items."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_FORMS, DEFAULT_ITEMS
    trailer_form = ("See the Data checks sheet for details.", "", "", "", "")
    trailer_item = ("See the Data checks sheet for details.", "", "Footnote text",
                    "", "") + ("",) * 16
    new = build_config_report(tmp_path / "tr.xlsx",
                              forms_rows=list(DEFAULT_FORMS) + [trailer_form],
                              items_rows=list(DEFAULT_ITEMS) + [trailer_item])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    cat = build_catalog(sp2)
    trailer_rows = [r for r in cat["ledger"] if r["target"] == "trailer:footnote"]
    assert len(trailer_rows) == 2
    assert [f["oid"] for f in cat["forms"]] == ["FAKEFORM1", "FAKEFORM2"]
    assert all(i["row_type"] == "Item" for i in cat["items"])


def test_no_old_report_degrades(sp):
    from dataclasses import replace
    cat = build_catalog(replace(sp, config_report_old=None))
    assert (cat["diffs"], cat["new_items"], cat["removed_items"]) == ({}, [], [])
    assert cat["version_old"] == "VOLD"   # 标签仍来自注册表, 仅 diff 降级
