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
    item["raw"] = {**item["raw"], "Visibility::Show on advanced condition": "COND_ADV"}
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="VNEW")
    assert "# [偽フォーム一 FAKEFORM1] FAKEIT1 (FAKEIT1)" in card   # label 降级 item_oid
    assert "- Item group: — (FG1)" in card
    assert "条件付き表示 (Show on advanced condition)" in card
    assert "- DEMO 例値: —" in card


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
