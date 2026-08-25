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
    # workflow 三池: 内容级断言 (不止台账计数) — 防 is_trailer filter 写反 (真实数据侧的闸
    # 在没有 data/study/ 检出的分支上是 ERROR 不是 skip, 合成路径必须自己兜住)
    assert [e["oid"] for e in cat["events"]] == ["EV_FAKE01", "EV_FAKE02"]
    assert [a["oid"] for a in cat["activities"]] == ["AC_FAKE01", "AC_FAKE02"]
    assert [f["form_oid"] for f in cat["assignments"]] == ["FAKEFORM1", "FAKEFORM2"]


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
    assert per_sheet == {"Forms": 2, "Items and Groups": 4, "Code lists": 3,
                          "Study workflow-Events": 3, "Study workflow-Activities": 3,
                          "Study workflow-Forms": 3}


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
    # 2 (本用例追加的 Forms/Items 脚注行) + 3 (三个 workflow sheet 默认各自带 1 条脚注行)
    assert len(trailer_rows) == 5
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


def test_diff_text_preserves_raw(sp):
    """diff 文案打原值: NFKC 会把丸数字①→1、全角括号→半角, 卡片须逐字可溯源."""
    from dataclasses import replace
    raw_label = "偽\u00a0項目（①）"
    new = build_config_report(sp.config_report_new.parent / "n3.xlsx",
                              items_rows=[_norm_item("FAKEX", label=raw_label)])
    old = build_config_report(sp.config_report_new.parent / "o3.xlsx",
                              items_rows=[_norm_item("FAKEX", label="旧ラベル")])
    cat = build_catalog(replace(sp, config_report_new=new, config_report_old=old))
    line = cat["diffs"]["FAKEX"][0]
    assert raw_label in line and "旧ラベル" in line


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


# ---- P2: 停用 form 语义钉死 / P3: diff_available ----

def test_deactivated_form_shape_raises(sp, tmp_path):
    """form 形态 Id (无空格) + In use 空 = 疑似停用 form, 不得静默按脚注吞掉."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_FORMS
    dead_form = ("FAKEDEAD", "停用フォーム", "", "", "")
    new = build_config_report(tmp_path / "dead.xlsx",
                              forms_rows=list(DEFAULT_FORMS) + [dead_form])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="In use"):
        build_catalog(sp2)


def test_footnote_form_row_still_trailer(sp, tmp_path):
    """真脚注行 (含空格句子形态 + In use 空) 仍走 trailer, 不误伤."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_FORMS
    footnote = ("See the Data checks sheet for details.", "", "", "", "")
    new = build_config_report(tmp_path / "fn.xlsx",
                              forms_rows=list(DEFAULT_FORMS) + [footnote])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    cat = build_catalog(sp2)
    assert [f["oid"] for f in cat["forms"]] == ["FAKEFORM1", "FAKEFORM2"]


def test_diff_available_flag(sp):
    """diffs=={} 歧义消解: 有旧版对比 → True, 无旧版降级 → False (Plan B 输入)."""
    from dataclasses import replace
    assert build_catalog(sp)["diff_available"] is True
    sp2 = replace(sp, config_report_old=None)
    assert build_catalog(sp2)["diff_available"] is False


def test_blank_id_with_payload_raises(sp, tmp_path):
    """Id 空但 Name/Description 有载荷: 不得静默归脚注 (与 Items 二次闸对称)."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_FORMS
    ghost = ("", "幽霊フォーム", "", "", "")
    new = build_config_report(tmp_path / "ghost.xlsx",
                              forms_rows=list(DEFAULT_FORMS) + [ghost])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="payload"):
        build_catalog(sp2)


# ---- workflow 三表二次闸: 四条可达 raise 路径 (审查方 C1 指出 Events/Activities 旧判据
# 恒假, 是死代码; 修复后必须证明"没有闸时会红, 加了闸变绿"—— 全仓此前对这三段 guard
# 零 pytest.raises 覆盖) ----

def test_workflow_events_blank_id_with_payload_raises(sp, tmp_path):
    """Events: Id 空但 Event name / Event type 有载荷 — 唯一可达的判据 (oid 形态判据恒假)."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_WORKFLOW_EVENTS
    ghost = ("", "偽イベント零", "", "偽タイプZ", "", "", "", "")
    new = build_config_report(tmp_path / "ev_ghost.xlsx",
                              events_rows=list(DEFAULT_WORKFLOW_EVENTS) + [ghost])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="blank Id with payload"):
        build_catalog(sp2)


def test_workflow_activities_blank_id_with_payload_raises(sp, tmp_path):
    """Activities: Id 空但 Study event ID 有载荷 — 唯一可达的判据."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_WORKFLOW_ACTIVITIES
    ghost = ("", "EV_FAKE01", "偽イベント一", "", "", "")
    new = build_config_report(tmp_path / "ac_ghost.xlsx",
                              activities_rows=list(DEFAULT_WORKFLOW_ACTIVITIES) + [ghost])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="blank Id with payload"):
        build_catalog(sp2)


def test_workflow_forms_activity_id_shaped_raises(sp, tmp_path):
    """Forms: Form ID 空但 Activity ID 是 OID 形态 (与 activity_oid 解耦, 判据可达)."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_WORKFLOW_FORMS
    ghost = ("", "", "AC_FAKE01", "", "", "", "", "")
    new = build_config_report(tmp_path / "fm_ghost_a.xlsx",
                              workflow_forms_rows=list(DEFAULT_WORKFLOW_FORMS) + [ghost])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="Activity ID"):
        build_catalog(sp2)


def test_workflow_forms_event_id_shaped_raises(sp, tmp_path):
    """Forms: Form ID 空但 Event ID 是 OID 形态 (第二条判据, 与上一条互相独立)."""
    from dataclasses import replace
    from scripts.tests.study_fixtures import DEFAULT_WORKFLOW_FORMS
    ghost = ("EV_FAKE01", "", "", "", "", "", "", "")
    new = build_config_report(tmp_path / "fm_ghost_b.xlsx",
                              workflow_forms_rows=list(DEFAULT_WORKFLOW_FORMS) + [ghost])
    sp2 = replace(sp, config_report_new=new, config_report_old=None)
    with pytest.raises(ValueError, match="Event ID"):
        build_catalog(sp2)
