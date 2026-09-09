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
    "items": [
        {"form_oid": "FA", "item_oid": "PS", "label": "全身状態"},
        {"form_oid": "FA", "item_oid": "ZWSTAT", "label": ""},
        {"form_oid": "FB", "item_oid": "PS", "label": "別フォームの同名 OID"},
        {"form_oid": "FB", "item_oid": "NOTONSCREEN", "label": "画面に出ない項目"},
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

# annotated: p1-2 = form FA, p3 = codelist FA, p4 = form FB
ANN_PAGES = [
    HDR + "偽フォーム甲 FA #1 全身状態 PS #2 偽ラベル ZWSTAT",
    HDR + "続きのページ ZWSTATX は別トークン",
    HDR + "偽フォーム甲 - Code Lists PS 0 1 2 3 4",
    HDR + "偽フォーム乙 FB #1 PS ここにも同じ OID",
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
        {"start": 4, "end": 4, "kind": "form", "form_oid": "FB"},
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
    assert set(idx["annotated"]) == {"blocks", "item_pages", "n_pages"}
    assert "draft" not in idx["meta"]


def test_names_table_is_display_only_and_activity_carries_its_event():
    """見出し用の名前表。activity は L1 グロッサリと同じ `イベント › アクティビティ`。"""
    names = _index()["names"]
    assert names["forms"] == {"FA": "偽フォーム甲", "FB": "偽フォーム乙"}
    assert names["activities"]["A1"] == "イベント一 › 活動一"


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
