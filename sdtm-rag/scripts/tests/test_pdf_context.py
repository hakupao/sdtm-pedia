"""I2-2: OID 集合 → 頁集合 → 画像 → 多模態片段 (`server/pdf_context.py`)。

合成索引で選頁を、monkeypatch した subprocess で描画を固める。実 PDF / 実 pdftoppm は
末尾の skipif 1 本だけ。
"""
from __future__ import annotations

import base64
import hashlib
import json

import pytest

from server.pdf_context import (
    PdfContextBuilder,
    PdfContextStatus,
    PdfPageIndex,
)
from server.pdf_trigger import CardFacts

# 合成索引: form FA は 4 つの activity に付くが、画面は 3 種類しかない
# (A_TWO と A_THREE は hidden_items が同一 = 同じ画面)。
WF_BYTES = b"%PDF-1.4\nfake workflow\n"
ANN_BYTES = b"%PDF-1.4\nfake annotated\n"


def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


INDEX = {
    "meta": {"pdfs": {"workflow": {"name": "wf.pdf", "pages": 40, "sha256": _sha(WF_BYTES)},
                      "annotated": {"name": "ann.pdf", "pages": 12, "sha256": _sha(ANN_BYTES)}}},
    "names": {"forms": {"FA": "偽フォーム甲", "FB": "偽フォーム乙", "FD": "偽フォーム丁"},
              "activities": {"A_ONE": "偽イベント一 › 偽活動一", "A_TWO": "偽イベント一 › 偽活動二",
                             "A_THREE": "偽イベント二 › 偽活動三", "A_FOUR": "偽イベント二 › 偽活動四"},
              "events": {}},
    "workflow": {
        "n_pages": 40,
        "blocks": [
            {"start": 3, "end": 5, "event_oid": "E1", "activity_oid": "A_ONE",
             "form_oid": "FA", "hidden_items": ["KX"]},
            {"start": 6, "end": 6, "event_oid": "E1", "activity_oid": "A_TWO",
             "form_oid": "FA", "hidden_items": ["WX", "KX"]},
            {"start": 9, "end": 9, "event_oid": "E2", "activity_oid": "A_THREE",
             "form_oid": "FA", "hidden_items": ["KX", "WX"]},
            {"start": 20, "end": 24, "event_oid": "E2", "activity_oid": "A_FOUR",
             "form_oid": "FA", "hidden_items": ["WX"]},
            {"start": 30, "end": 31, "event_oid": "E2", "activity_oid": "A_FOUR",
             "form_oid": "FB", "hidden_items": []},
        ],
    },
    "annotated": {
        "n_pages": 12,
        "blocks": [
            {"start": 2, "end": 4, "kind": "form", "form_oid": "FA"},
            {"start": 5, "end": 6, "kind": "codelist", "form_oid": "FA"},
            {"start": 7, "end": 8, "kind": "form", "form_oid": "FB"},
            # FD は**単頁**の form ブロック (実データにも 21 中 6 本ある)。頁索引メタが
            # 1 つも無い label を作れる唯一の形なので、fixture に要る。
            {"start": 10, "end": 10, "kind": "form", "form_oid": "FD"},
        ],
        "item_pages": {"FA": {"WX": [2], "WY": [2], "WZ": [2], "KX": [3], "K2": [3],
                              "K3": [4]},
                       "FB": {}, "FD": {"Q1": [10]}},
        # N3: 本頁に項目が在る catalog グループの並び (builder が catalog × item_pages で
        # 算出して焼く)。項目数は上の item_pages と 1 対 1 で噛み合わせてある ——
        # fixture が実際に有り得ない索引だと、そこで通ったテストは何も守らない。
        #   p.2 = 枠 2 つ (どちらも本頁で開始)   … WX,WY → G1 / WZ → G2
        #   p.3 = 枠 2 つ (先頭は前頁からの続き) … KX → G2 (p.2 から継続) / K2 → G3
        #   p.4 = 枠 1 つ (前頁からの続き)       … K3 → G3
        # N4: `continues` = その枠が**次の頁にも**続く (本頁で閉じない)。`continued` と対。
        "page_groups": {
            "FA": {"2": [{"group_oid": "G1", "name": "偽グループ甲", "n_items": 2,
                          "continued": False, "continues": False},
                         {"group_oid": "G2", "name": "", "n_items": 1,
                          "continued": False, "continues": True}],
                   "3": [{"group_oid": "G2", "name": "", "n_items": 1,
                          "continued": True, "continues": False},
                         {"group_oid": "G3", "name": "偽グループ丙", "n_items": 1,
                          "continued": False, "continues": True}],
                   "4": [{"group_oid": "G3", "name": "偽グループ丙", "n_items": 1,
                          "continued": True, "continues": False}]},
            "FD": {"10": [{"group_oid": "G9", "name": "偽グループ丁", "n_items": 1,
                           "continued": False, "continues": False}]},
        },
    },
}

CARD = """---
study: st99
doc_type: field_card
form_oid: {form}
field_oid: {item}
---

- 表示条件: 常時表示
- 非表示アクティビティ: {hidden}
"""


def card(form="FA", item="WX", hidden="A_TWO, A_THREE"):
    return CardFacts.from_text(CARD.format(form=form, item=item, hidden=hidden))


@pytest.fixture
def builder(tmp_path):
    return _builder(tmp_path)


def _builder(tmp_path, index=None, **kw):
    (tmp_path / "wf.pdf").write_bytes(WF_BYTES)
    (tmp_path / "ann.pdf").write_bytes(ANN_BYTES)
    return PdfContextBuilder(
        PdfPageIndex(INDEX if index is None else index),
        {"workflow": tmp_path / "wf.pdf", "annotated": tmp_path / "ann.pdf"},
        cache_dir=tmp_path / "cache", **kw,
    )


def pages_of(sel):
    return [(p.pdf, p.page) for p in sel.pages]


# ── 選頁 ───────────────────────────────────────────────────────────────
def test_annotated_item_pages_come_first(builder):
    """画面↔DB の橋渡しは item OID の徽章が写っている annotated 頁。"""
    sel = builder.select_pages([card(item="WX"), card(item="KX")])
    assert pages_of(sel)[:2] == [("annotated", 2), ("annotated", 3)]


def test_form_block_first_page_is_the_fallback_when_the_oid_is_not_on_any_page(builder):
    """941/959 は当たるが 18 件は当たらない (S0 §1-1)。当たらない分を黙って捨てると、
    そのフォームの画面が 1 枚も付かない。"""
    sel = builder.select_pages([card(form="FB", item="NOTFOUND", hidden="—")])
    assert ("annotated", 7) in pages_of(sel)


def test_identical_screens_are_not_attached_twice(builder):
    """A_TWO と A_THREE は hidden_items が同じ = 同じ画面。2 枚付けるのは頁予算の空費。
    判別材料は catalog 由来の hidden_items (索引に焼いてある)。"""
    sel = builder.select_pages([card(item="WX")], max_pages=8)
    wf = [p.page for p in sel.pages if p.pdf == "workflow"]
    assert 6 in wf and 9 not in wf


def test_screens_that_display_a_retrieved_item_outrank_screens_that_hide_it(builder):
    """付ける価値は「画面に何が出ているか」。全部隠れている画面は、カードが既に
    そう言っているので新情報がほぼ無い —— 予算が苦しいときに先に落ちるべきはそちら。"""
    sel = builder.select_pages([card(item="WX")], max_pages=2)
    wf = [p.page for p in sel.pages if p.pdf == "workflow"]
    assert wf == [3]           # A_ONE (WX 表示) が, A_TWO/A_FOUR (WX 非表示) より先
    assert [p.page for p in sel.omitted if p.pdf == "workflow"][0] == 6


def test_activity_named_in_the_question_outranks_everything(builder):
    sel = builder.select_pages([card(item="WX")], question="A_FOUR ではどう表示されますか",
                               max_pages=2)
    assert pages_of(sel) == [("annotated", 2), ("workflow", 20)]


def test_full_width_oid_in_the_question_still_matches(builder):
    """日本語入力の全角 `Ａ＿ＦＯＵＲ`。NFKC を通さないと当たらず、症状は
    「OID を書いたのに 1 頁も付かない」という無症状の取りこぼしになる。
    正規化も境界照合も study_lookup の定義を借りている (定義は 1 つ)。"""
    sel = builder.select_pages([card(item="WX")], question="Ａ＿ＦＯＵＲ の画面は",
                               max_pages=2)
    assert ("workflow", 20) in pages_of(sel)


def test_question_oid_match_is_token_bounded(builder):
    """`A_FOUR` を裸の部分文字列で探すと `A_FOURTH` のような別語にも当たる。"""
    sel = builder.select_pages([card(item="WX")], question="A_FOURTH について", max_pages=2)
    assert ("workflow", 20) not in pages_of(sel)


def test_workflow_keeps_a_share_of_the_budget(builder):
    """annotated を無制限に先取りさせると、カードが 6 枚当たった時点で workflow が
    0 枚になる —— R1 (活動をまたぐ表示) の答えは workflow 側にしか無い。"""
    cards = [card(item="WX"), card(item="KX"), card(form="FB", item="Z1", hidden="—"),
             card(form="FB", item="Z2", hidden="—")]
    sel = builder.select_pages(cards, max_pages=4)
    assert sum(1 for p in sel.pages if p.pdf == "workflow") >= 1


def test_annotated_takes_the_leftover_when_workflow_has_few_candidates(builder):
    sel = builder.select_pages([card(form="FB", item="Z1", hidden="—"),
                                card(form="FB", item="Z2", hidden="—")], max_pages=6)
    assert len(sel.pages) >= 2


def test_truncation_records_what_was_dropped(builder):
    sel = builder.select_pages([card(item="WX"), card(item="KX")], max_pages=2)
    assert sel.truncated and len(sel.pages) == 2 and sel.omitted


def test_no_truncation_flag_when_everything_fits(builder):
    sel = builder.select_pages([card(item="WX")], max_pages=20)
    assert not sel.truncated and not sel.omitted


def test_a_page_is_never_attached_twice(builder):
    """同じ form の 2 枚のカードが同じ annotated 頁を指すのは普通 (中位 1 頁/フォーム)。"""
    sel = builder.select_pages([card(item="WX"), card(item="WX")], max_pages=8)
    assert len(pages_of(sel)) == len(set(pages_of(sel)))


def test_unknown_form_is_skipped_not_crashed(builder):
    assert builder.select_pages([card(form="FZ", item="Q", hidden="—")]).pages == ()


def test_labels_name_the_pdf_the_page_and_the_screen(builder):
    sel = builder.select_pages([card(item="WX")], question="A_FOUR", max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated")
    wf = next(p for p in sel.pages if p.pdf == "workflow")
    assert "annotated p.2" in ann.label and "偽フォーム甲 (FA)" in ann.label
    assert "workflow p.20" in wf.label and "偽イベント二 › 偽活動四" in wf.label


# ── N1: 添付頁はブロックの部分集合 ─────────────────────────────────────
def test_a_multi_page_block_says_on_the_label_that_only_one_page_is_attached(builder):
    """V3 T3/T6: 付いたのはブロック先頭頁だけなのに、モデルは「この頁に無い ⇒ その
    活動の画面に無い」と外推した。頁範囲を label に書かないと、部分集合であることは
    モデルから見て観測不能。"""
    sel = builder.select_pages([card(item="WX")], question="偽活動四 の画面",
                               max_pages=3)
    wf = next(p for p in sel.pages if p.pdf == "workflow" and p.page == 20)
    assert "p.20–24" in wf.label and "のうち本頁" in wf.label


def test_the_range_note_distinguishes_partial_blocks_from_whole_ones(builder):
    """1 頁で全部なら部分集合ではない。同じ 1 回の選頁の中で、p.20 (ブロック 20–24) には
    断り書きが付き p.6 (ブロック 6–6) には付かないこと —— 常に足すと「一部しか見ていない」
    が狼少年になり、全部見えている頁でも断定を避け始める。"""
    sel = builder.select_pages([card(item="WX")], max_pages=8)
    labels = {p.page: p.label for p in sel.pages if p.pdf == "workflow"}
    assert "のうち" in labels[20] and "のうち" not in labels[6]


def test_annotated_label_carries_the_form_block_range(builder):
    """annotated 側も同じ: FA のフォーム画面は p.2–4 で、付くのは item OID の頁だけ。"""
    sel = builder.select_pages([card(item="WX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 2)
    assert "p.2–4 のうち本頁 p.2 のみ添付" in ann.label


# ── N3: 本頁の項目グループ順 / 索引メタの出処分離 ──────────────────────
def test_page_groups_are_read_off_the_index(builder):
    assert [g["name"] for g in builder.index.page_groups("FA", 2)] == ["偽グループ甲", ""]


def test_page_groups_are_empty_for_an_index_that_predates_the_field(tmp_path):
    """本番の索引は再生成しないと新欄を持たない。欄が無い索引で落ちる/注記を捏造する
    のではなく、**注記が付かないだけ**であること (旧索引はそのまま動く)。"""
    old = json.loads(json.dumps(INDEX))
    del old["annotated"]["page_groups"]
    b = _builder(tmp_path, index=old)
    assert b.index.page_groups("FA", 2) == []
    sel = b.select_pages([card(item="WX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 2)
    assert "項目グループ順" not in ann.label
    assert "p.2–4 のうち本頁 p.2" in ann.label      # 他のメタは生きている


def test_page_groups_of_an_unknown_form_or_page_are_empty(builder):
    assert builder.index.page_groups("FZ", 2) == [] and builder.index.page_groups("FA", 99) == []


def test_a_multi_group_page_writes_the_group_order_on_the_label(builder):
    """N3 の起源: 両モデルとも見出しの無い枠を前の枠に併合した (V3 §4 第 5 条)。枠の
    境界は catalog のグループ境界と逐字一致するので、並びを label に書けば観測できる。"""
    sel = builder.select_pages([card(item="WX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 2)
    assert "本頁の項目グループ順: 偽グループ甲 [2 項目] › (無題) [1 項目・次頁へ続く]" in ann.label


def test_a_single_group_page_gets_no_group_note(builder):
    """枠が 1 つの頁に「グループ順」と書いても順序の情報が無い。常に足すと N1 の範囲
    注記と同じで狼少年になり、本当に 2 枠ある頁の注記が読み飛ばされる。範囲注記の方は
    残る = 消えているのがグループ順だけであることも一緒に見る。"""
    sel = builder.select_pages([card(item="K3")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 4)
    assert "項目グループ順" not in ann.label and "のうち本頁 p.4 のみ添付" in ann.label


# ── N4: 沈黙している次元を明示する ─────────────────────────────────────
def _ann(builder, item, page, form="FA", hidden="A_TWO, A_THREE"):
    sel = builder.select_pages([card(form=form, item=item, hidden=hidden)], max_pages=3)
    return next(p for p in sel.pages if p.pdf == "annotated" and p.page == page)


def test_a_single_group_page_declares_its_one_frame_and_both_continuation_states(builder):
    """N3 a2 の残り 1 件 (ann p.161): 枠が 1 つの頁は label が何も言わないので、モデルは
    視覚で「前頁からの続きの可能性あり」を作った (実物は上辺が閉じ、**次頁**へ続く)。
    順序は書かない (無いから) が、枠の数と前後の連続状態は索引が知っている事実なので
    宣言する —— 沈黙を既知に変える。"""
    label = _ann(builder, "K3", 4).label
    assert "本頁の枠: 1 (偽グループ丙 [1 項目])" in label
    assert "前頁からの続き: あり" in label and "次頁へ続く: なし" in label


def test_a_single_untitled_frame_is_named_untitled(tmp_path):
    """実データの p.161 がまさに無題 1 枠。空名で書くと「枠: 1 ( [16 項目])」になり、
    見出しを画像から探しに行く余地を残す。"""
    idx = json.loads(json.dumps(INDEX))
    idx["annotated"]["page_groups"]["FD"]["10"][0]["name"] = ""
    label = _ann(_builder(tmp_path, index=idx), "Q1", 10, form="FD", hidden="—").label
    assert "本頁の枠: 1 ((無題) [1 項目])" in label


def test_a_multi_group_page_declares_the_page_level_continuation_states(builder):
    """複数枠の頁も「先頭の枠が前頁から続くか / 末尾の枠が次頁へ続くか」は沈黙だった。
    p.2 は先頭頁 (前頁なし) で、末尾の (無題) 枠が p.3 へ続く。"""
    label = _ann(builder, "WX", 2).label
    assert "前頁からの続き: なし" in label and "次頁へ続く: あり" in label
    assert "本頁の枠:" not in label            # 順が書けるときは枠数の宣言に置き換えない


def test_a_group_that_runs_onto_the_next_page_is_marked_on_the_sequence(builder):
    """`continued` の印と対称。末尾の枠が本頁で閉じないことを枠ごとにも見せる。"""
    label = _ann(builder, "WX", 2).label
    assert "(無題) [1 項目・次頁へ続く]" in label
    assert "偽グループ甲 [2 項目]" in label and "偽グループ甲 [2 項目・" not in label


def test_a_frame_open_on_both_sides_carries_both_marks(builder):
    """p.3 の (無題) は p.2 から続き p.3 で閉じる、偽グループ丙は p.3 で始まり p.4 へ
    続く。印の向きを取り違える実装 (continued と continues を逆に読む) をここで捕まえる。"""
    label = _ann(builder, "KX", 3).label
    assert "(無題) [1 項目・前頁からの続き]" in label
    assert "偽グループ丙 [1 項目・次頁へ続く]" in label
    assert "前頁からの続き: あり" in label and "次頁へ続く: あり" in label


def test_a_closed_single_frame_says_none_on_both_sides(builder):
    """「なし」が書かれることが本体。書かない (= 従来の沈黙) と何も変わらない。"""
    label = _ann(builder, "Q1", 10, form="FD", hidden="—").label
    assert "前頁からの続き: なし" in label and "次頁へ続く: なし" in label


def test_a_partially_migrated_index_stays_silent_on_the_next_page_dimension(tmp_path):
    """複審 MINOR-3: 判定が `any` だと、一部のグループにだけ欄が無い索引で、欄の無い
    グループに「次頁へ続く: なし」= 嘘を書く。1 グループだけ欄を落として釘付け。"""
    idx = json.loads(json.dumps(INDEX))
    idx["annotated"]["page_groups"]["FA"]["2"][1].pop("continues")   # 末尾の枠だけ欠ける
    label = _ann(_builder(tmp_path, index=idx), "WX", 2).label
    assert "次頁へ続く" not in label and "前頁からの続き: なし" in label


def test_an_index_without_the_continues_field_omits_only_that_dimension(tmp_path):
    """N3 の索引 (`continues` 無し) で起動しても落ちず、書けない次元だけ黙る。
    False で埋めると「次頁へ続く: なし」と**嘘**を書くことになる。"""
    idx = json.loads(json.dumps(INDEX))
    for form in idx["annotated"]["page_groups"].values():
        for groups in form.values():
            for g in groups:
                g.pop("continues")
    label = _ann(_builder(tmp_path, index=idx), "WX", 2).label
    assert "前頁からの続き: なし" in label
    assert "次頁へ続く" not in label


def test_continuation_states_live_behind_the_meta_prefix(builder):
    """索引由来の事実は全部 1 段 (N3 (b))。前置きの前に出ると画面の注記として引用される。"""
    label = _ann(builder, "K3", 4).label
    head, meta = label.split("頁索引メタ:")
    assert "本頁の枠" not in head and "続き" not in head
    assert "本頁の枠: 1" in meta and "次頁へ続く: なし" in meta


def test_a_group_continued_from_the_previous_page_says_so(builder):
    """複審 MAJOR-1: 枠の見出しは始まった頁にしか描かれない (実データの名前付き続き枠
    25 件中、続き頁に見出しが出ていたのは 0 件)。並びだけ渡すと、モデルは前頁にしか
    無い見出しを本頁の記載として報告する —— N2 の LABEL 型捏造の新しい面。"""
    sel = builder.select_pages([card(item="KX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 3)
    assert ("本頁の項目グループ順: (無題) [1 項目・前頁からの続き] › 偽グループ丙 [1 項目・次頁へ続く]"
            in ann.label)


def test_a_group_that_starts_on_this_page_carries_no_continued_mark(builder):
    """全部に印を付けると印の意味が消える。p.2 は form ブロックの先頭頁なので、
    どの枠も前頁から続きようがない。"""
    sel = builder.select_pages([card(item="WX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 2)
    # N4 以降、頁単位の状態「前頁からの続き: なし」は書かれる。消えているのは枠ごとの印。
    assert "・前頁からの続き" not in ann.label and "前頁からの続き: なし" in ann.label


def test_group_oids_stay_out_of_the_label(builder):
    """索引の group OID は annotated の文本層に **0/153** しか現れない (実測) ——
    画像から確かめようのない文字列を label に足すのは、N2 で問題になった「索引由来の
    メタが画面の注記として引用される」を増やすだけ。並び順と項目数で枠は特定できる。"""
    sel = builder.select_pages([card(item="WX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 2)
    assert "G1" not in ann.label and "G2" not in ann.label


def test_index_metadata_sits_behind_exactly_one_meta_prefix(builder):
    """N3 (b): 索引由来のメタ (ブロック範囲 / 同一画面 / グループ順) は頁そのものの
    身元ではない。1 箇所にまとめて前置きを付けないと、規則側が「どこからが索引由来か」
    を指せず、『画面目視判読』の出典で引用される (N2 起源の 3 件)。"""
    sel = builder.select_pages([card(item="WX")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 2)
    assert ann.label.count("頁索引メタ") == 1
    head, meta = ann.label.split("頁索引メタ: ")
    assert "偽フォーム甲 (FA)" in head and "のうち" not in head      # 身元だけが前に残る
    assert "のうち本頁 p.2 のみ添付" in meta and "項目グループ順" in meta


def test_a_label_with_nothing_to_add_has_no_meta_segment(tmp_path):
    """単頁ブロック・定位できた項目なし・折り畳み無し = 索引が足せる事実がゼロ。空の
    「頁索引メタ:」が残ると、無いものを探してモデルが注記を捏造する余地になる。
    (N4 以降、枠が 1 つでも在れば連続状態を書くので、「何も無い頁」= 項目が定位
    できずフォーム先頭頁に降級した頁だけ。)"""
    idx = json.loads(json.dumps(INDEX))
    idx["annotated"]["item_pages"]["FD"] = {}
    del idx["annotated"]["page_groups"]["FD"]
    sel = _builder(tmp_path, index=idx).select_pages(
        [card(form="FD", item="Q1", hidden="—")], max_pages=3)
    ann = next(p for p in sel.pages if p.pdf == "annotated" and p.page == 10)
    assert ann.label == "【画面 annotated p.10 — 偽フォーム丁 (FD) フォーム画面】"


def test_a_workflow_label_folds_range_and_shared_screen_into_one_segment(builder):
    """範囲注記と「同一画面」が同居する形。選頁を経由せず label 関数を直接叩くのは、
    この組合せが選頁の都合 (どのブロックが畳まれるか) ではなく label の性質だから。"""
    blk = next(b for b in INDEX["workflow"]["blocks"] if b["start"] == 20)
    label = builder._wf_label(blk, ["A_THREE"])
    assert label.count("頁索引メタ") == 1
    assert "p.20–24 のうち本頁 p.20 のみ添付；同一画面: 偽イベント二 › 偽活動三" in label


# ── 描画 + 多模態片段 ──────────────────────────────────────────────────
@pytest.fixture
def fake_pdftoppm(monkeypatch):
    """pdftoppm を差し替え、`-singlefile` が約束するファイル名だけを作る。"""
    calls = []

    def run(cmd, **kw):
        calls.append(cmd)
        out = cmd[-1] + ".png"
        with open(out, "wb") as fh:
            fh.write(b"\x89PNG-" + cmd[-1].encode()[-12:])
        class R:
            returncode = 0
            stderr = ""
        return R()

    monkeypatch.setattr("server.pdf_context.subprocess.run", run)
    monkeypatch.setattr("server.pdf_context.shutil.which", lambda _: "/usr/bin/pdftoppm")
    return calls


def test_render_shells_out_once_per_page_with_the_configured_dpi(builder, fake_pdftoppm):
    sel = builder.select_pages([card(item="WX")], max_pages=2)
    parts = builder.render(sel)
    assert len(parts) == len(sel.pages) == 2
    assert fake_pdftoppm[0][:6] == ["pdftoppm", "-r", "110", "-png", "-singlefile", "-f"]


def test_render_reuses_the_disk_cache_on_the_second_call(builder, fake_pdftoppm):
    sel = builder.select_pages([card(item="WX")], max_pages=1)
    builder.render(sel)
    n = len(fake_pdftoppm)
    builder.render(sel)
    assert len(fake_pdftoppm) == n, "同じ (pdf sha, 頁, dpi) を 2 度描画している"


def test_cache_key_separates_dpi_and_pdf(tmp_path, fake_pdftoppm):
    b1, b2 = _builder(tmp_path, dpi=110), _builder(tmp_path, dpi=150)
    sel = b1.select_pages([card(item="WX")], max_pages=1)
    b1.render(sel)
    b2.render(b2.select_pages([card(item="WX")], max_pages=1))
    assert len(fake_pdftoppm) == 2, "dpi 違いが同じキャッシュ鍵に潰れている"


def test_message_parts_pair_a_text_header_with_each_image(builder, fake_pdftoppm):
    sel = builder.select_pages([card(item="WX")], max_pages=2)
    parts = builder.to_message_parts(sel)
    assert [p["type"] for p in parts[:4]] == ["text", "image_url", "text", "image_url"]
    url = parts[1]["image_url"]["url"]
    assert url.startswith("data:image/png;base64,")
    assert base64.b64decode(url.split(",", 1)[1]).startswith(b"\x89PNG")
    assert "annotated p.2" in parts[0]["text"]


def test_truncated_selection_says_so_inside_the_message(builder, fake_pdftoppm):
    """落とした頁を黙って消すと、モデルは「これで全部」と思って断定する。"""
    sel = builder.select_pages([card(item="WX"), card(item="KX")], max_pages=1)
    tail = builder.to_message_parts(sel)[-1]
    assert tail["type"] == "text" and "未添付" in tail["text"] and "p.3" in tail["text"]


def test_no_pages_means_no_parts(builder, fake_pdftoppm):
    assert builder.to_message_parts(builder.select_pages([])) == []


# ── 不可用時 ───────────────────────────────────────────────────────────
def test_status_is_unavailable_when_pdftoppm_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr("server.pdf_context.shutil.which", lambda _: None)
    b = _builder(tmp_path)
    assert not b.status.available and "pdftoppm" in b.status.reason


def test_status_is_unavailable_when_a_pdf_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr("server.pdf_context.shutil.which", lambda _: "/usr/bin/pdftoppm")
    (tmp_path / "ann.pdf").write_bytes(ANN_BYTES)   # 片方だけ在る = もう片方が理由
    b = PdfContextBuilder(PdfPageIndex(INDEX),
                          {"workflow": tmp_path / "ghost.pdf", "annotated": tmp_path / "ann.pdf"},
                          cache_dir=tmp_path / "c")
    assert not b.status.available and "ghost.pdf" in b.status.reason


def test_unavailable_builder_renders_nothing_instead_of_raising(tmp_path, monkeypatch):
    monkeypatch.setattr("server.pdf_context.shutil.which", lambda _: None)
    b = _builder(tmp_path)
    sel = b.select_pages([card(item="WX")])
    assert sel.pages and b.render(sel) == [] and b.to_message_parts(sel) == []


def test_index_load_reads_a_file(tmp_path):
    p = tmp_path / "idx.json"
    p.write_text(json.dumps(INDEX), encoding="utf-8")
    assert PdfPageIndex.load(p).item_pages("FA", "WX") == [2]


def test_status_unavailable_carries_its_reason():
    s = PdfContextStatus.unavailable("なぜ使えないか")
    assert not s.available and s.reason == "なぜ使えないか"


# ── r3b: 問いがフォームを名指ししたか (R3 のフロア (c)) ────────────────
def test_form_named_by_its_oid_in_the_question():
    """T6 型は form を OID でも日本語名でも呼ぶ。判定材料は頁索引の名前表だけ ——
    別名表 (`lookup_aliases.yml`) には依存しない (依存すると 1 件しか無い実データで
    落ちる: V3 attempt 1)。"""
    assert PdfPageIndex(INDEX).form_named_in("FA フォームの画面の並びは") == "FA"


def test_form_named_by_its_japanese_name_in_the_question():
    assert PdfPageIndex(INDEX).form_named_in("偽フォーム乙の画面で項目はどう並ぶ") == "FB"


def test_form_oid_match_is_token_bounded():
    """`FA` が `FASTING` の中に当たると、study と無関係な問いがフロアを通ってしまう。"""
    assert PdfPageIndex(INDEX).form_named_in("FASTING の画面について") is None


def test_a_question_naming_no_form_returns_none():
    assert PdfPageIndex(INDEX).form_named_in("画面の並びを教えてください") is None


def test_short_form_names_are_not_matched_as_bare_substrings():
    """2-3 字の form 名は日本語の地の文に偶然現れる。OID 側は境界照合なので下限なし。"""
    idx = json.loads(json.dumps(INDEX))
    idx["names"]["forms"]["FC"] = "検査"
    assert PdfPageIndex(idx).form_named_in("この検査の画面は") is None


def test_the_longer_form_name_wins_when_one_contains_the_other():
    idx = json.loads(json.dumps(INDEX))
    idx["names"]["forms"]["FC"] = "偽フォーム乙の続き"
    assert PdfPageIndex(idx).form_named_in("偽フォーム乙の続きの画面") == "FC"


# ── M1: PDF の本人確認 ─────────────────────────────────────────────────
def test_a_replaced_pdf_makes_the_channel_unavailable(tmp_path, monkeypatch):
    """索引は「どの PDF の何頁か」しか言えない。PDF が版更新で差し替わると、同じ頁番号が
    別の画面を指し、答えは「出典付きで堂々と間違う」—— 索引欠落より悪い。sha を
    記録しておいて照合しないのは、鍵を作って鍵穴を作らないのと同じ。"""
    monkeypatch.setattr("server.pdf_context.shutil.which", lambda _: "/usr/bin/pdftoppm")
    b = _builder(tmp_path)
    assert b.status.available
    (tmp_path / "wf.pdf").write_bytes(WF_BYTES + b"another version\n")   # 版更新を模す
    b2 = PdfContextBuilder(PdfPageIndex(INDEX),
                           {"workflow": tmp_path / "wf.pdf", "annotated": tmp_path / "ann.pdf"},
                           cache_dir=tmp_path / "cache2")
    assert not b2.status.available
    assert "workflow" in b2.status.reason and "sha256" in b2.status.reason


# ── M2: 日本語で名指しされた活動 / 同一画面の折り畳み ──────────────────
def test_an_activity_named_in_japanese_is_treated_as_asked(builder):
    """実際の問いは活動を OID ではなく日本語名で呼ぶ (T4/T5, dogfood)。OID しか見ないと
    名指しされた画面が黙って落ちる。"""
    sel = builder.select_pages([card(item="WX")], question="偽活動四 の画面を見せて",
                               max_pages=2)
    assert ("workflow", 20) in pages_of(sel)


def test_t4_shaped_question_keeps_the_named_duplicate_screen(builder):
    """T4 型: 2 つの活動が**同じ画面**を作る (hidden_items 一致) のに、問いは 2 つ目を
    名指ししている。折り畳みで黙って消すと「両日とも同じ画面」という答えの根拠が
    無くなる —— 名指しされた側は tier 0 で残る。"""
    sel = builder.select_pages([card(item="WX")], question="偽活動三 では何が出ますか",
                               max_pages=6)
    wf = [p.page for p in sel.pages if p.pdf == "workflow"]
    assert 6 in wf and 9 in wf


def test_folded_screens_are_named_on_the_surviving_page(builder):
    """折り畳んだ活動を label に書く。「この画面は 活動X と 活動Y で共通」は答えそのもの
    なので、予算節約のために消していい情報ではない。"""
    sel = builder.select_pages([card(item="WX")], max_pages=8)
    p6 = next(p for p in sel.pages if p.page == 6 and p.pdf == "workflow")
    assert "同一画面" in p6.label and "偽活動三" in p6.label


def test_folded_blocks_are_metadata_not_budget_omissions(builder):
    """折り畳みは「予算で落とした」ではない。omitted に混ぜると、頁上限を上げれば
    出てくるかのように読める (実際は上げても出てこない)。"""
    sel = builder.select_pages([card(item="WX")], max_pages=8)
    assert [p.page for p in sel.folded] == [9]
    assert 9 not in [p.page for p in sel.omitted]


# ── M3 / M6 / 文言 ─────────────────────────────────────────────────────
def test_message_parts_use_the_images_actually_rendered(builder, fake_pdftoppm, monkeypatch):
    """描画に失敗した頁は片段にも出ない。呼び出し側が「付けた頁」を報告できるよう、
    描画結果を渡せる形にしておく (選んだ頁ではなく)。"""
    sel = builder.select_pages([card(item="WX"), card(item="KX")], max_pages=2)
    images = builder.render(sel)[:1]
    parts = builder.to_message_parts(sel, images)
    assert sum(1 for p in parts if p["type"] == "image_url") == 1


def test_zero_page_budget_attaches_nothing(builder, fake_pdftoppm):
    """M6: 上限 0 は「実質 OFF」であって「1 枚だけ」ではない。"""
    sel = builder.select_pages([card(item="WX")], max_pages=0)
    assert sel.pages == () and builder.to_message_parts(sel) == []


def test_degraded_hint_is_japanese_and_shows_the_configured_cap(builder, fake_pdftoppm):
    """回答は日本語。片段の中で 1 行だけ中国語だと、その語彙が答えに漏れる。
    また上限は**設定値**であって、たまたま付いた枚数ではない。"""
    sel = builder.select_pages([card(item="WX"), card(item="KX")], max_pages=1)
    tail = builder.to_message_parts(sel)[-1]
    assert "ページ未添付" in tail["text"] and "ページ上限 1" in tail["text"]
    assert "页" not in tail["text"]


def test_pages_that_failed_to_render_are_named_in_the_hint(builder, fake_pdftoppm):
    """予算で落とした頁と、描画に失敗した頁は、モデルから見れば同じ「見ていない頁」。
    後者だけ黙っていると「これで全部」と思って断定する。"""
    sel = builder.select_pages([card(item="WX"), card(item="KX")], max_pages=2)
    parts = builder.to_message_parts(sel, builder.render(sel)[:1])   # 2 枚目が描画失敗
    assert "p.3" in parts[-1]["text"]


def test_nothing_rendered_means_no_parts_at_all(builder, fake_pdftoppm):
    """1 枚も描画できなかったときに案内文だけ残すと、画像の無い会話に
    「画面目視判読」という出典名だけが漂う (使ってよい出典だとモデルが読む)。"""
    sel = builder.select_pages([card(item="WX"), card(item="KX")], max_pages=2)
    assert builder.to_message_parts(sel, []) == []


# ── 実 PDF (skipif) ────────────────────────────────────────────────────
def _real():
    try:
        from scripts.study.paths import resolve_study
        sp = resolve_study("st01")
    except Exception:
        return None
    idx = sp.out_dir / "pdf_page_index.json"
    if not (sp.pdf_workflow and sp.pdf_annotated and idx.is_file()):
        return None
    return sp, idx


@pytest.mark.slow
@pytest.mark.skipif(_real() is None, reason="st01 の実 PDF / 索引が無い環境")
def test_real_render_produces_a_real_png(tmp_path):
    sp, idx = _real()
    b = PdfContextBuilder(PdfPageIndex.load(idx),
                          {"workflow": sp.pdf_workflow, "annotated": sp.pdf_annotated},
                          cache_dir=tmp_path)
    from server.pdf_context import PageRef
    sel = type(b.select_pages([]))(pages=(PageRef("workflow", 315, "x", "probe"),),
                                   omitted=(), truncated=False)
    part, = b.render(sel)
    raw = base64.b64decode(part.b64)
    assert raw[:8] == b"\x89PNG\r\n\x1a\n" and len(raw) > 20_000
