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
    assert "DEMO 例値: 1 / 0" in body
    assert "旧→新版差分: なし" in body


def test_render_field_card_fallbacks(catalog):
    """30 无 label / 254 无组名 / 288 无示例值 / advanced 可見性 — 全部降级路径."""
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["label"] = ""
    item["group_name"] = ""
    item["visible_condition"] = ""
    item["raw"] = {**item["raw"], "Visibility::Show on advanced condition": "X"}
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert "# [偽フォーム一 FAKEFORM1] FAKEIT1 (FAKEIT1)" in card   # label 降级 item_oid
    assert "- Item group: — (FG1)" in card
    assert "- 表示条件: 条件あり (式は別ソース)" in card
    assert "- DEMO 例値: —" in card


def test_render_visibility_v2_parts(catalog):
    """可見性 v2: hide-simple 展开值 / advanced 只留标志措辞 / 多部件 '; ' 连接."""
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["visible_condition"] = ""
    item["raw"] = {**item["raw"],
                   "Visibility::Hide on simple condition": "FAKEIT2 == 1",
                   "Visibility::Show on advanced condition": "X",
                   "Visibility::Hide on advanced condition": "X"}
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert ("- 表示条件: 非表示条件: FAKEIT2 == 1; 条件あり (式は別ソース); "
            "非表示条件あり (式は別ソース)") in card
    assert "適用範囲" not in card              # Hidden in activity 空 → 无该行


def test_render_visibility_scope_row(catalog):
    """適用範囲 独立行: Hidden in activity 原值展开, 且与 visible_condition 并存 (27 项)."""
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["visible_condition"] = "FAKEIT3 != ''"
    item["raw"] = {**item["raw"], "Visibility::Hidden in activity": "偽アクティビティ甲, 偽乙"}
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert "- 表示条件: FAKEIT3 != ''" in card
    assert "- 適用範囲: 偽アクティビティ甲, 偽乙" in card   # 不混入表示条件
    assert "条件あり" not in card


def test_render_always_visible(catalog):
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["visible_condition"] = ""
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert "- 表示条件: 常時表示" in card


def test_render_strips_newlines(catalog):
    """真实 8 label + 1 组名含换行 — 折成单行, 否则打断 H1/bullet 结构."""
    cat, _ = catalog
    item = dict(cat["items"][0])
    item["label"] = "偽項目\nラベル一"
    item["group_name"] = "グループ\r\n甲"
    item["form_name"] = "偽フォーム\n一"
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert "# [偽フォーム 一 FAKEFORM1] 偽項目 ラベル一 (FAKEIT1)" in card
    assert "- Item group: グループ 甲 (FG1)" in card
    body_lines = [ln for ln in card.splitlines() if ln.startswith(("#", "- "))]
    assert len([ln for ln in body_lines if ln.startswith("# ")]) == 1


def test_build_cards_files_and_index(catalog):
    cat, sp = catalog
    paths = build_cards(cat, {}, sp.cards_dir)
    names = sorted(p.name for p in paths)
    assert names == ["st01__FAKEFORM1__FAKEIT1.md", "st01__FAKEFORM1__FAKEIT2.md",
                     "st01__FAKEFORM2__FAKEIT3.md"]
    index = (sp.cards_dir / "INDEX.md").read_text(encoding="utf-8")
    assert "| FAKEFORM1 | 偽フォーム一 | 2 |" in index      # 整行匹配: form + 名称 + 项目数
    assert "| FAKEFORM2 | 偽フォーム二 | 1 |" in index
    assert "# st01 Field Card Index" in index               # 标题取 catalog['study']
    assert (sp.cards_dir / "ROUTING.md").exists()


def test_build_cards_forms_filter(catalog):
    cat, sp = catalog
    paths = build_cards(cat, {}, sp.cards_dir, forms_filter={"FAKEFORM2"})
    assert [p.name for p in paths] == ["st01__FAKEFORM2__FAKEIT3.md"]
    index = (sp.cards_dir / "INDEX.md").read_text(encoding="utf-8")
    assert "| FAKEFORM2 | 偽フォーム二 | 1 |" in index
    assert "FAKEFORM1" not in index      # filter 外的 form 不列 (零计数行会误导模型)


def test_build_cards_idempotent_purges_stale(catalog):
    """幂等: cards_dir 全删重建 — 上一轮遗留 / 陌生文件不得存活."""
    cat, sp = catalog
    sp.cards_dir.mkdir(parents=True)
    stale = sp.cards_dir / "st01__GONEFORM__GONEIT.md"
    stale.write_text("stale", encoding="utf-8")
    (sp.cards_dir / "note.txt").write_text("stale", encoding="utf-8")
    build_cards(cat, {}, sp.cards_dir)
    assert not stale.exists()
    assert not (sp.cards_dir / "note.txt").exists()
    assert sorted(p.name for p in sp.cards_dir.iterdir()) == [
        "INDEX.md", "ROUTING.md", "st01__FAKEFORM1__FAKEIT1.md",
        "st01__FAKEFORM1__FAKEIT2.md", "st01__FAKEFORM2__FAKEIT3.md"]
