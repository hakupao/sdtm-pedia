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


def _norm_item(oid, *, label="", data_checks="", required=""):
    """比较归一化用的最小 Item 行 (21 列)."""
    return ("FAKEFORM1", "偽フォーム一", "Item", "FG1", "",
            oid, "text", required, "", "", data_checks, "", label, "Text box",
            "", "", "", "", "", "", "")


@pytest.fixture()
def norm_sp(sp, tmp_path):
    """新旧两版只差表記ゆれ (NBSP / HTML 实体) + 两处真实变更."""
    from dataclasses import replace
    new = build_config_report(tmp_path / "n2.xlsx", items_rows=[
        _norm_item("FAKENB1", label="偽項目\u00a0一"),        # NBSP 插在非空白字符之间
        _norm_item("FAKENB2", label="偽項目\u00a0二"),        # 旧版此处是普通空格 → 被 NBSP 顶替
        _norm_item("FAKEENT", label="A &amp;amp; B &lt; C"),  # 双重转义 + 实体
        _norm_item("FAKEREAL", data_checks="DC01"),           # 真实变更: 新增 data checks
        _norm_item("FAKEREQ", required="X"),                  # 真实变更: bool 字段
    ])
    old = build_config_report(tmp_path / "o2.xlsx", items_rows=[
        _norm_item("FAKENB1", label="偽項目一"),
        _norm_item("FAKENB2", label="偽項目 二"),
        _norm_item("FAKEENT", label="A & B < C"),
        _norm_item("FAKEREAL", data_checks=""),
        _norm_item("FAKEREQ", required=""),
    ])
    return replace(sp, config_report_new=new, config_report_old=old)


def test_diff_ignores_export_artifacts(norm_sp):
    """NBSP 插入 / NBSP 顶替空格 / HTML 实体 (含双重转义) 都不是变更."""
    diffs = build_catalog(norm_sp)["diffs"]
    assert set(diffs) == {"FAKEREAL", "FAKEREQ"}


def test_diff_keeps_real_changes(norm_sp):
    """值增删与 bool 翻转必须报出 (归一化不得吞真实变更)."""
    diffs = build_catalog(norm_sp)["diffs"]
    assert any(c.startswith("data_checks:") and "DC01" in c for c in diffs["FAKEREAL"])
    assert any(c.startswith("required:") and "False" in c and "True" in c
               for c in diffs["FAKEREQ"])


def test_diff_text_is_normalized(sp):
    """diff 文案用归一化值, 不把 NBSP 原样打进卡片."""
    from dataclasses import replace
    new = build_config_report(sp.config_report_new.parent / "n3.xlsx",
                              items_rows=[_norm_item("FAKEX", label="偽\u00a0項目\u00a0甲")])
    old = build_config_report(sp.config_report_new.parent / "o3.xlsx",
                              items_rows=[_norm_item("FAKEX", label="旧ラベル")])
    cat = build_catalog(replace(sp, config_report_new=new, config_report_old=old))
    line = cat["diffs"]["FAKEX"][0]
    assert "\u00a0" not in line and "偽 項目 甲" in line


def test_normalization_does_not_touch_new_removed(norm_sp):
    """归一化只作用于比较判定, 不影响 OID 集合运算."""
    from dataclasses import replace
    cat = build_catalog(norm_sp)
    assert cat["new_items"] == [] and cat["removed_items"] == []
    extra = build_config_report(norm_sp.config_report_new.parent / "n4.xlsx",
                                items_rows=[_norm_item("FAKENB1", label="偽項目\u00a0一"),
                                            _norm_item("FAKENEW")])
    cat2 = build_catalog(replace(norm_sp, config_report_new=extra))
    assert cat2["new_items"] == ["FAKENEW"]
    assert set(cat2["removed_items"]) == {"FAKENB2", "FAKEENT", "FAKEREAL", "FAKEREQ"}


def test_catalog_stores_raw_values(norm_sp):
    """存储的是原值: 归一化只是比较口径, 不改 catalog 内容 (卡片仍见真实导出值)."""
    cat = build_catalog(norm_sp)
    labels = {i["item_oid"]: i["label"] for i in cat["items"]}
    assert labels["FAKENB1"] == "偽項目\u00a0一"
    assert labels["FAKEENT"] == "A &amp;amp; B &lt; C"
