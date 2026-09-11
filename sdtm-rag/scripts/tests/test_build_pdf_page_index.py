"""I2-1: 确定性 PDF 页索引 (PLAN_c2r_pdf_bypass.md §4)。

合成页文本 fixture, 零真名 / 零真实页 —— 切块逻辑只吃 `list[str]`, 子进程边界留在
`scripts/study/pdf_text.py` 一处 (与 split_sections.py 同纪律)。真 PDF 只在文末一条
skipif 集成测试里出现。
"""
from __future__ import annotations

import json

import pytest

from scripts.study import build_pdf_page_index as bpi

HDR = "ENSEMBLE | ENSEMBLE [59.0] "

CATALOG = {
    "forms": [
        {"oid": "FA", "name": "偽フォーム甲"},
        {"oid": "FB", "name": "偽フォーム乙"},
    ],
    "events": [
        {"oid": "E1", "name": "イベント一"},
        {"oid": "E2", "name": "イベント二"},
    ],
    "activities": [
        {"oid": "A1", "event_oid": "E1", "event_name": "イベント一", "name": "活動一"},
        {"oid": "A2", "event_oid": "E2", "event_name": "イベント二", "name": "活動二"},
    ],
    "assignments": [
        {"event_oid": "E1", "event_name": "イベント一", "activity_oid": "A1",
         "activity_name": "活動一", "form_oid": "FA", "hidden_items": "PS, ZWSTAT"},
        {"event_oid": "E1", "event_name": "イベント一", "activity_oid": "A1",
         "activity_name": "活動一", "form_oid": "FB", "hidden_items": ""},
        {"event_oid": "E2", "event_name": "イベント二", "activity_oid": "A2",
         "activity_name": "活動二", "form_oid": "FA", "hidden_items": "ZWSTAT"},
    ],
    # N3: `group_oid` / `group_name` / `row` は「本頁の項目グループ順」の材料。配列の並びを
    # わざと row 順と食い違わせてある —— 実装が catalog の配列順に寄りかかっていたら
    # `test_page_groups_follow_catalog_row_order` がそれを捕まえる。
    "items": [
        {"form_oid": "FA", "item_oid": "ZWSTAT", "label": "", "row": 2,
         "group_oid": "G2", "group_name": ""},
        {"form_oid": "FA", "item_oid": "ZWNOTE", "label": "偽注記", "row": 3,
         "group_oid": "G2", "group_name": ""},
        {"form_oid": "FA", "item_oid": "PS", "label": "全身状態", "row": 1,
         "group_oid": "G1", "group_name": "偽グループ甲"},
        {"form_oid": "FB", "item_oid": "PS", "label": "別フォームの同名 OID", "row": 1,
         "group_oid": "G3", "group_name": "偽グループ乙"},
        {"form_oid": "FB", "item_oid": "NOTONSCREEN", "label": "画面に出ない項目", "row": 2,
         "group_oid": "G3", "group_name": "偽グループ乙"},
        # G3 は p.4 と p.5 の両方に項目が在る = p.5 では枠の途中 (見出しは p.4 にしか無い)。
        # G4 は p.5 で始まる別の枠 —— 実データの「続きの枠 › 新しい枠」と同じ形。
        {"form_oid": "FB", "item_oid": "ZWMORE", "label": "続き頁の項目", "row": 3,
         "group_oid": "G3", "group_name": "偽グループ乙"},
        {"form_oid": "FB", "item_oid": "ZWNEW", "label": "次の枠の先頭", "row": 4,
         "group_oid": "G4", "group_name": "偽グループ丙"},
        # 2 字 OID が同じ form ブロックの隣の頁の**日本語見出しの頭**と衝突する形
        # (複審の実例)。ZK は p.4 に本物の badge が在り p.5 は誤検出、ZQ は badge が
        # どこにも無く衝突だけ = 定位そのものが誤り。
        {"form_oid": "FB", "item_oid": "ZK", "label": "衝突する 2 字 OID", "row": 5,
         "group_oid": "G3", "group_name": "偽グループ乙"},
        {"form_oid": "FB", "item_oid": "ZQ", "label": "衝突だけの 2 字 OID", "row": 6,
         "group_oid": "G3", "group_name": "偽グループ乙"},
    ],
}

# workflow: p1 表紙 (無題), p2-3 = (E1,A1,FA), p4 = (E1,A1,FB), p5 = (E2,A2,FA)
WF_PAGES = [
    HDR + "表紙 デザインバージョン 59",
    HDR + "イベント一 / 活動一 偽フォーム甲 #1 重複チェック",
    HDR + "続きのページ 偽項目 偽検査値",
    HDR + "イベント一 / 活動一 偽フォーム乙 #1 なにか",
    HDR + "イベント二 / 活動二 偽フォーム甲 #1 なにか",
]

# annotated: p1-2 = form FA, p3 = codelist FA, p4-5 = form FB (p5 は題名の無い続き頁)
ANN_PAGES = [
    HDR + "偽フォーム甲 FA #1 全身状態 PS #2 偽ラベル ZWSTAT #3 偽注記 ZWNOTE",
    HDR + "続きのページ ZWSTATX は別トークン",
    HDR + "偽フォーム甲 - Code Lists PS 0 1 2 3 4",
    HDR + "偽フォーム乙 FB #1 PS ここにも同じ OID #2 ZK 検査値",
    # ZWMORE は行末 (次行の頭は日本語) —— 改行は norm_page で空白になるので badge の
    # まま。ZK / ZQ は日本語見出しに食い込んだ形で、badge ではない。
    HDR + "続きのページ ZWMORE\n偽ラベル 次の枠 ZWNEW\nZK検査日 ZQコース",
]


def _blocks(pages, catalog=CATALOG):
    return bpi.cut_workflow_blocks(catalog, pages)


# ── workflow 切块 ──────────────────────────────────────────────────────
def test_workflow_titles_resolve_to_oids():
    assert _blocks(WF_PAGES) == [
        {"start": 2, "end": 3, "event_oid": "E1", "activity_oid": "A1", "form_oid": "FA",
         "hidden_items": ["PS", "ZWSTAT"]},
        {"start": 4, "end": 4, "event_oid": "E1", "activity_oid": "A1", "form_oid": "FB",
         "hidden_items": []},
        {"start": 5, "end": 5, "event_oid": "E2", "activity_oid": "A2", "form_oid": "FA",
         "hidden_items": ["ZWSTAT"]},
    ]


def test_hidden_items_ride_along_on_the_block():
    """ブロックは「どの画面か」を答えられなければ選頁の役に立たない。同一 form の 18 個の
    activity が実データでは 5 種類の画面しか作らない (LB 実測) —— その判別は catalog の
    `hidden_items` にしか無く、消費側 (server/pdf_context.py) に catalog を持ち込むより
    ここで焼き込む方が「頁 = 画面」の対応が 1 箇所で完結する。"""
    b = _blocks(WF_PAGES)
    assert [x["hidden_items"] for x in b] == [["PS", "ZWSTAT"], [], ["ZWSTAT"]]


def test_cover_pages_belong_to_no_block():
    """封面/目次は誰のものでもない —— 前方埋めで p.1 を最初のブロックに吸わせない。"""
    assert min(b["start"] for b in _blocks(WF_PAGES)) == 2


def test_last_block_runs_to_the_last_page():
    pages = WF_PAGES + [HDR + "まだ活動二の続き"]
    assert _blocks(pages)[-1]["end"] == 6


def test_unknown_form_name_in_title_fails_loud():
    """(event, activity) は当たったのに form 名が catalog に無い = 索引が黙って壊れる形。"""
    pages = [HDR + "イベント一 / 活動一 未知フォーム #1"]
    with pytest.raises(ValueError, match="page 1"):
        _blocks(pages)


def test_title_triple_absent_from_assignments_fails_loud():
    """(E2,A2,FB) は assignments に無い組合せ。ページが有ると言うなら catalog と食い違う。"""
    pages = [HDR + "イベント二 / 活動二 偽フォーム乙 #1"]
    with pytest.raises(ValueError, match="assignment"):
        _blocks(pages)


def test_ambiguous_title_fails_loud():
    """同名 (event_name, activity_name) が 2 つの activity_oid を指す catalog では、
    どちらの OID を書いても 50% 嘘になる —— 黙って先勝ちさせない。"""
    cat = json.loads(json.dumps(CATALOG))
    cat["assignments"].append({
        "event_oid": "E1", "event_name": "イベント一", "activity_oid": "A1_DUP",
        "activity_name": "活動一", "form_oid": "FA",
    })
    with pytest.raises(ValueError, match="ambiguous"):
        _blocks(WF_PAGES, cat)


# ── annotated 切块 + item→页 ────────────────────────────────────────────
def test_annotated_blocks_split_form_and_codelist():
    assert bpi.cut_annotated_blocks(CATALOG, ANN_PAGES) == [
        {"start": 1, "end": 2, "kind": "form", "form_oid": "FA"},
        {"start": 3, "end": 3, "kind": "codelist", "form_oid": "FA"},
        {"start": 4, "end": 5, "kind": "form", "form_oid": "FB"},
    ]


def test_item_pages_use_token_boundary():
    """`ZWSTATX` は `ZWSTAT` ではない。境界無しの部分一致は定位率を偽って
    100% 近くに押し上げる (S0 勘察が途中で自己修正した方法誤り)。"""
    ip = bpi.item_pages_by_form(CATALOG, bpi.cut_annotated_blocks(CATALOG, ANN_PAGES), ANN_PAGES)
    assert ip["FA"]["ZWSTAT"] == [1]


def test_short_oid_confined_to_its_own_form_block():
    """短 OID 串味防止 (S0 §1-3): `PS` は FA と FB の両方に居る。form ブロック外まで
    探すと、FA の PS が FB のページを指す = 画面判読の出典が丸ごと嘘になる。"""
    ip = bpi.item_pages_by_form(CATALOG, bpi.cut_annotated_blocks(CATALOG, ANN_PAGES), ANN_PAGES)
    assert ip["FA"]["PS"] == [1]
    assert ip["FB"]["PS"] == [4]


def test_codelist_pages_are_not_item_pages():
    """code-list ブロックは画面ではない。p.3 の `PS` を拾うと「画面 p.3」と言い張る。"""
    ip = bpi.item_pages_by_form(CATALOG, bpi.cut_annotated_blocks(CATALOG, ANN_PAGES), ANN_PAGES)
    assert 3 not in ip["FA"]["PS"]


def test_items_never_found_are_omitted_not_empty_listed():
    """空リストを残すと「探した結果ゼロ」と「そもそも探していない」が区別できない。"""
    ip = bpi.item_pages_by_form(CATALOG, bpi.cut_annotated_blocks(CATALOG, ANN_PAGES), ANN_PAGES)
    assert "NOTONSCREEN" not in ip["FB"]


# ── 3 本の断言 ─────────────────────────────────────────────────────────
def _index():
    return bpi.build_index(CATALOG, WF_PAGES, ANN_PAGES, meta={})


def test_all_three_assertions_pass_on_synthetic_fixture():
    res = bpi.check_index(_index(), CATALOG)
    assert [r.name for r in res] == ["workflow_blocks_eq_assignments",
                                     "workflow_page_coverage",
                                     "annotated_form_blocks_eq_forms"]
    assert all(r.ok for r in res), [r.detail for r in res if not r.ok]


def test_a_failing_assertion_does_not_hide_the_other_two():
    """3 本とも計算して**全部**返す —— 1 本目で raise すると、直し切ったかが 1 回の
    実行で分からず、直す→走らせるを 3 往復することになる。"""
    idx = _index()
    idx["workflow"]["blocks"] = []   # 分母は n_pages のまま = 被覆 0/5 で 2 本目も落ちる
    res = bpi.check_index(idx, CATALOG)
    assert len(res) == 3
    assert [r.ok for r in res] == [False, False, True]


def test_coverage_assertion_counts_pages_not_blocks():
    idx = _index()
    cov = next(r for r in bpi.check_index(idx, CATALOG) if r.name == "workflow_page_coverage")
    assert "4/5" in cov.detail


def test_index_shape_is_small_and_production_flavoured():
    """勘察草案 (1.16 MB, 全実体の逐ページ命中表) と違い、生産版はブロック表 +
    item→頁 の 2 枚だけ。draft 印も無い。"""
    idx = _index()
    assert set(idx) == {"meta", "names", "workflow", "annotated"}
    assert set(idx["workflow"]) == {"blocks", "n_pages"}
    assert set(idx["annotated"]) == {"blocks", "item_pages", "n_pages", "page_groups"}
    assert "draft" not in idx["meta"]


def test_names_table_is_display_only_and_activity_carries_its_event():
    """見出し用の名前表。activity は L1 グロッサリと同じ `イベント › アクティビティ`。"""
    names = _index()["names"]
    assert names["forms"] == {"FA": "偽フォーム甲", "FB": "偽フォーム乙"}
    assert names["activities"]["A1"] == "イベント一 › 活動一"


def test_an_oid_glued_to_a_japanese_heading_is_not_a_badge():
    """複審の実例: 2 字 OID が隣の頁の日本語見出しの**頭**と一致し、その頁に居ることに
    されてしまう。画面の OID 徽章は列として独立していて、日本語に食い込んでいない ——
    `_bounded_re` の境界 (ASCII 英数のみ) は CJK 隣接を素通しするので、ここで塞ぐ。"""
    ip = _item_pages()
    assert ip["FB"]["ZK"] == [4], "日本語見出しに食い込んだ 2 字 OID を頁として数えている"


def test_an_oid_that_only_collides_is_not_located_at_all():
    """衝突しか無い OID は「定位できない item」(実データで 18/959) であって、
    衝突した頁の item ではない。フォーム先頭頁への降級は消費側が既にやる。"""
    assert "ZQ" not in _item_pages()["FB"]


def test_a_badge_at_the_end_of_a_line_survives():
    """改行は `norm_page` で空白になる。行末の badge の次の行が日本語で始まるのは普通で、
    そこまで落とすと真の徽章 (実測 941 件の大半) を捨てることになる。"""
    assert _item_pages()["FB"]["ZWMORE"] == [5]


# ── N3: 本頁の項目グループ順 ───────────────────────────────────────────
def _item_pages(catalog=CATALOG, pages=ANN_PAGES):
    return bpi.item_pages_by_form(catalog, bpi.cut_annotated_blocks(catalog, pages), pages)


def _page_groups(catalog=CATALOG, pages=ANN_PAGES):
    return bpi.page_groups_by_form(catalog, _item_pages(catalog, pages))


def test_page_groups_follow_catalog_row_order():
    """並び順が答えの一部 (N3 の起源: 両モデルとも無題パネルを前のパネルに併合した)。
    順は catalog の `row` —— 配列順に寄りかかると、catalog の書き出し順が変わった日に
    索引が黙って別の並びを言い出す。"""
    assert [g["name"] for g in _page_groups()["FA"]["1"]] == ["偽グループ甲", ""]


def test_page_groups_count_only_the_items_located_on_that_page():
    """`n_items` は**この頁で定位できた**項目数。グループ全体の項目数を書くと、
    添付頁に無い項目まで「本頁に在る」と読める (N1 と同じ外推を索引側で作ることになる)。

    判別力のために、総数と定位数が**食い違う**組で見る: G3 は catalog に 5 項目
    あるが、p.4 に写っているのは 2 項目だけ。総数を
    書く実装なら 5 になってここが落ちる。"""
    assert [g["n_items"] for g in _page_groups()["FA"]["1"]] == [1, 2]
    assert [g["n_items"] for g in _page_groups()["FB"]["4"]] == [2]


def test_untitled_groups_keep_an_empty_name_in_the_index():
    """(無題) という表示語は label 側の語彙。索引には catalog の値 (空文字) をそのまま
    残す —— 索引に表示語を焼くと、表示を変えたい時に索引の再生成が要る。"""
    g2 = _page_groups()["FA"]["1"][1]
    assert g2["name"] == "" and g2["group_oid"] == "G2"


def test_page_keys_are_strings_so_the_json_round_trip_changes_nothing():
    """JSON のキーは文字列。組み立て時だけ int にすると、生成直後のテストは通って
    読み直した索引では 1 件も当たらない (consumer は `str(page)` で引く)。"""
    built = _page_groups()
    assert built == json.loads(json.dumps(built))
    assert set(built["FA"]) == {"1"}


def test_pages_without_any_located_item_are_absent():
    """継続頁 (p.2) には定位できた項目が無い。空リストを置くと「グループが 0 個の頁」と
    「調べていない頁」が混ざる (item_pages の空リストを載せないのと同じ理由)。"""
    assert "2" not in _page_groups()["FA"]


def test_an_item_that_is_not_a_catalog_item_fails_loud():
    """item_pages と catalog が食い違う索引は、黙って「グループの無い頁」を作る ——
    その頁だけ注記が消える無症状の壊れ方になる。"""
    with pytest.raises(ValueError, match="GHOST"):
        bpi.page_groups_by_form(CATALOG, {"FA": {"GHOST": [1]}})


def test_a_group_that_started_on_an_earlier_page_is_marked_continued():
    """複審 MAJOR-1: 枠の見出しは**始まった頁**にしか描かれない。実データでは名前付きの
    続き枠 25 件中 0 件しか続き頁に見出しが出ていないので、続きだと言わずに並びだけ
    渡すと、モデルは前頁にしか無い見出しを「本頁に在る」と報告する。"""
    p5 = _page_groups()["FB"]["5"]
    assert [(g["name"], g["continued"]) for g in p5] == [
        ("偽グループ乙", True), ("偽グループ丙", False)]


def test_a_group_that_starts_on_this_page_is_not_continued():
    """全部に印を付けると印の意味が消える (N1 の範囲注記と同じ天秤)。"""
    assert [g["continued"] for g in _page_groups()["FB"]["4"]] == [False]
    assert [g["continued"] for g in _page_groups()["FA"]["1"]] == [False, False]


def test_page_groups_ride_in_the_index_next_to_item_pages():
    assert _index()["annotated"]["page_groups"]["FB"]["4"] == [
        {"group_oid": "G3", "name": "偽グループ乙", "n_items": 2, "continued": False}]


# ── 実 PDF (skipif) ────────────────────────────────────────────────────
def _real_paths():
    try:
        from scripts.study.paths import resolve_study
        sp = resolve_study("st01")
    except Exception:
        return None
    if not (sp.pdf_workflow and sp.pdf_annotated):
        return None
    return sp


@pytest.mark.slow
@pytest.mark.skipif(_real_paths() is None, reason="st01 の実 PDF / registry が無い環境")
def test_real_pdfs_satisfy_all_three_assertions():
    sp = _real_paths()
    catalog = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    idx = bpi.build_from_pdfs(sp.pdf_workflow, sp.pdf_annotated, catalog,
                              cache_dir=sp.out_dir / ".pdf_page_text_cache")
    res = bpi.check_index(idx, catalog)
    assert all(r.ok for r in res), [r.detail for r in res if not r.ok]
    # S0 §1-4 の具体案 (dogfood の LB 題) を頁番号で釘付ける。真名は赤線纪律で
    # gitignored 側 (data/study/) に置く —— 期待値そのものが真の form/item/activity OID
    # なので、ここに書くと索引の正しさを守る代わりに真名を git に漏らすことになる。
    pins_path = sp.out_dir / "eval" / "c2r_index_pins.json"
    if not pins_path.is_file():
        pytest.skip(f"実値ピンが無い: {pins_path}")
    pins = json.loads(pins_path.read_text(encoding="utf-8"))
    a = pins["annotated_item"]
    assert a["page"] in idx["annotated"]["item_pages"][a["form_oid"]][a["item_oid"]]
    w = pins["workflow_block"]
    starts = [b["start"] for b in idx["workflow"]["blocks"]
              if b["activity_oid"] == w["activity_oid"] and b["form_oid"] == w["form_oid"]]
    assert starts == [w["start"]]
