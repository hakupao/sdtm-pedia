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
