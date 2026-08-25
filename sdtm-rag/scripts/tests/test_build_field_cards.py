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
    assert "非表示アクティビティ" not in card   # Hidden in activity 空 → 无该行


def test_render_hidden_activity_row(catalog):
    """非表示アクティビティ 独立行: Hidden in activity 原值展开, 且与 visible_condition 并存 (27 项).

    列名是 'Hidden in activity' = 该字段在这些 activity 中**被隐藏**; 旧标签 '適用範囲'
    (=适用范围) 语义相反, 2026-08-25 修正. 与 Study workflow-Forms 的 'Hidden items'
    列互为精确转置 (实测 61/61 逐键相同 — 见 spec §4 F3 与 evidence/checkpoints/c2_pre_survey.md §8-5).
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


def test_render_strips_newlines_in_diff(catalog):
    """diff 串内嵌旧版多行 label (真实 1 item) — 折成单行, 否则甩出游离正文行."""
    cat, _ = catalog
    card = render_field_card(cat["items"][0], cat["forms"][0], None, [],
                             ["label: 旧\n値 → 新値", "data_type: text → integer"],
                             study="st01", version="VNEW")
    assert "- 旧→新版差分: label: 旧 値 → 新値; data_type: text → integer" in card
    body = card.split("---\n", 2)[2]
    assert all(ln.startswith(("#", "- ")) for ln in body.splitlines() if ln)


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


# ---- M-2: diff_available 贯通到卡片 ----

def test_render_diff_unavailable_says_not_compared(catalog):
    cat, _sp = catalog
    item = cat["items"][0]
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="V2", diff_available=False)
    assert "旧→新版差分: 未対比 (旧版なし)" in card
    assert "差分: なし" not in card


def test_build_cards_passes_diff_available(catalog, tmp_path):
    cat = dict(catalog[0])
    cat["diff_available"] = False
    paths = build_cards(cat, {}, tmp_path / "cards")
    text = paths[0].read_text(encoding="utf-8")
    assert "未対比" in text


def test_build_cards_defaults_diff_available_true(catalog, tmp_path):
    """旧 catalog.json (无 diff_available 键) 向后兼容: 维持原「なし」措辞."""
    cat = {k: v for k, v in catalog[0].items() if k != "diff_available"}
    paths = build_cards(cat, {}, tmp_path / "cards2")
    text = paths[0].read_text(encoding="utf-8")
    assert "未対比" not in text


# ---- §3.4: EDC 富文本导出残留的 HTML 标签剥离 ----

def test_flat_strips_whitelisted_html_tags():
    from scripts.study.build_field_cards import _flat
    assert _flat('<span style="color: red;">/mm<sup>3</sup></span>') == "/mm3"
    assert _flat("<strong>必須</strong>") == "必須"


def test_flat_decodes_entities():
    from scripts.study.build_field_cards import _flat
    assert _flat("cm&nbsp;＊注意") == "cm ＊注意"
    assert _flat("10.0&times;10<sup>4</sup>") == "10.0×104"


def test_flat_preserves_bare_less_than_in_real_criteria():
    """真実データに `5cm<AV≤10cm` の裸 < が存在 —— 汎用 <[^>]+> 正規表現なら
    後続の > まで丸ごと削る。白名单方式であることの回帰钉."""
    from scripts.study.build_field_cards import _flat
    s = "※5cm<AV≤10cm,T3a/bN0M0, EMVI-, MRF clear"
    assert _flat(s) == s


def test_flat_preserves_unknown_tag_like_text():
    from scripts.study.build_field_cards import _flat
    assert _flat("range <AV> check") == "range <AV> check"


def test_rendered_card_unit_has_no_html(catalog, tmp_path):
    """単位フィールドは _flat を通っていなかった —— カード面に生 HTML が残る."""
    from scripts.study.build_field_cards import render_field_card
    cat, _sp = catalog
    item = dict(cat["items"][0])
    item["unit"] = '<span style="color: red;">/mm<sup>3</sup>&nbsp;＊単位に注意</span>'
    card = render_field_card(item, cat["forms"][0], None, [], [],
                             study="st01", version="V2")
    assert "<span" not in card and "&nbsp;" not in card
    assert "/mm3 ＊単位に注意" in card


def test_rendered_codelist_entries_have_no_html(catalog):
    from scripts.study.build_field_cards import render_field_card
    cat, _sp = catalog
    item = dict(cat["items"][0])
    cl = {"data_type": "text",
          "entries": [["1", "<strong>はい</strong>"], ["0", "いいえ&nbsp;"]]}
    card = render_field_card(item, cat["forms"][0], cl, [], [],
                             study="st01", version="V2")
    assert "<strong>" not in card and "&nbsp;" not in card
    assert "1 = はい" in card


# ---- Task 4: 収集アクティビティ (spec §2.3) ----
# collect_scope() 自身的单测已挪到 test_collect_scope.py (Task 6, M5: 函数本体挪出
# 渲染器模块到 scripts/study/collect_scope.py); 这里只留"渲染器怎么用它"的测试。

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


def test_build_cards_omits_collect_scope_row(catalog):
    """用户 2026-08-25 裁定执行 spec §6 S3: 生产 build_cards 路径不渲染 収集アクティビティ 行
    (评测回归 87.50% → 84.38%, 见 evidence/failures/t4_step7_retrieval_regression.md)。

    本测试是这次裁定的守门人 —— build_cards 内部调用若被"顺手"改回传
    `catalog.get("assignments", [])`, 该行会在磁盘卡片上重新出现而没有测试察觉。
    collect_scope 推导本身与「传 assignments 就渲染」的行为均未被否定 (见上面两个
    collect_scope 单测 + test_render_collect_scope_row), 此处只锁生产调用路径。
    """
    cat, sp = catalog
    paths = build_cards(cat, {}, sp.cards_dir)
    for p in paths:
        assert "収集アクティビティ" not in p.read_text(encoding="utf-8")
