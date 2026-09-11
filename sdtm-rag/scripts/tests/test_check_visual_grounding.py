"""N2: 画面出処の接地闸 (`scripts/study/c2r_eval/check_visual_grounding.py`)。

合成頁索引 + 偽の頁テキストだけで判定を固める。実 PDF / 実 `pdftotext` は 1 本も出てこない
—— 子プロセス境界は `page_text` コールバック 1 箇所に寄せてあるので、ここでは dict を渡す。
偽名は `test_pdf_context.py` の流儀 (FA/FB, 偽活動一…) に合わせる。
"""
from __future__ import annotations

import hashlib
import json

import pytest

from scripts.study.c2r_eval import check_visual_grounding as cvg

# 合成索引: form FA は 4 つの activity に付くが、画面は 3 種類しかない
# (A_TWO と A_THREE は hidden_items が同一 = 同じ画面 = 折り畳み対象)。
INDEX_DATA = {
    "meta": {"pdfs": {"workflow": {"name": "wf.pdf", "pages": 40, "sha256": "0" * 64},
                      "annotated": {"name": "ann.pdf", "pages": 12, "sha256": "1" * 64}}},
    "names": {"forms": {"FA": "偽フォーム甲", "FB": "偽フォーム乙"},
              "activities": {"A_ONE": "偽イベント一 › 偽活動一", "A_TWO": "偽イベント一 › 偽活動二",
                             "A_THREE": "偽イベント二 › 偽活動三", "A_FOUR": "偽イベント二 › 偽活動四",
                             # 名前が A_ONE の短名を含む = 極大一致の検査用
                             "A_FIVE": "偽イベント二 › 偽活動一_追加検査"},
              "events": {}},
    "workflow": {"n_pages": 40, "blocks": [
        {"start": 3, "end": 5, "event_oid": "E1", "activity_oid": "A_ONE",
         "form_oid": "FA", "hidden_items": ["KX"]},
        {"start": 6, "end": 6, "event_oid": "E1", "activity_oid": "A_TWO",
         "form_oid": "FA", "hidden_items": ["WX", "KX"]},
        {"start": 9, "end": 9, "event_oid": "E2", "activity_oid": "A_THREE",
         "form_oid": "FA", "hidden_items": ["KX", "WX"]},
        {"start": 20, "end": 24, "event_oid": "E2", "activity_oid": "A_FOUR",
         "form_oid": "FA", "hidden_items": ["WX"]},
    ]},
    "annotated": {"n_pages": 12, "blocks": [
        {"start": 2, "end": 4, "kind": "form", "form_oid": "FA"},
        {"start": 5, "end": 6, "kind": "codelist", "form_oid": "FA"},
        {"start": 7, "end": 8, "kind": "form", "form_oid": "FB"},
    ], "item_pages": {"FA": {"WX": [2], "KX": [3]}, "FB": {}},
        # N3 が足す頁内の項目グループ (label の「本頁の項目グループ順」の出どころ)。
        # p.2: 偽枠一 は見出しがこの頁に在る / 偽枠二 は**前頁からの続き** = 見出しは p.1
        # / 無題の枠は名前が無いので実体にしない。
        "page_groups": {"FA": {
            "2": [{"group_oid": "GA", "name": "偽枠一", "n_items": 3},
                  {"group_oid": "GB", "name": "偽枠二", "n_items": 2, "continued": True},
                  {"group_oid": "GC", "name": "", "n_items": 1},
                  {"group_oid": "GD", "name": "偽枠一_続き", "n_items": 2, "continued": True}],
            "3": [{"group_oid": "GE", "name": "偽枠三", "n_items": 4}]}},
     },
}
# N3 以前の索引 (page_groups が無い) —— 黙って素通しできること
INDEX_NO_GROUPS = json.loads(json.dumps(INDEX_DATA))
del INDEX_NO_GROUPS["annotated"]["page_groups"]

# 偽の頁テキスト層。実データと同じく **OID は 1 つも写っていない** (S0 実測: workflow の
# OID ヒットは 0) —— 頁が活動を名乗るのは日本語名だけ、という条件を再現しておかないと
# 「OID が頁に在る」前提の緩い実装が緑になってしまう。
PAGES = {
    ("workflow", 3): "偽イベント一 › 偽活動一 / 偽フォーム甲 の実表示\n偽項目甲  偽項目乙  偽項目丙",
    # ブロックの 2 頁目以降は見出しを持たない = 頁テキストだけでは誰の画面か分からない
    ("workflow", 4): "偽検査  項目一覧\n偽項目丁  偽項目戊",
    ("workflow", 6): "偽イベント一 › 偽活動二 / 偽フォーム甲 の実表示\n偽項目乙  偽項目丙",
    ("workflow", 20): "偽イベント二 › 偽活動四 / 偽フォーム甲 の実表示\n偽項目乙",
    # 見出しがこの頁に在るのは 偽枠一 だけ。偽枠二 / 偽枠一_続き は前頁からの続きなので、
    # この頁の画像にも文本層にも名前は無い (= 名前を書けば label を読んだということ)。
    ("annotated", 2): "偽フォーム甲 フォーム画面\n偽枠一\n#1 WX 偽項目乙   #2 KX 偽項目甲",
    # コードリスト頁はフォーム名を刷らない (実データも同様) —— 頁テキストに実体が無く、
    # 帰属はブロック表 = label のメタ情報からしか来ない頁。
    ("annotated", 6): "Code Lists\n1 = はい   2 = いいえ",
    ("annotated", 7): "偽フォーム乙 フォーム画面",
}


def page_text(pdf: str, page: int) -> str:
    return PAGES.get((pdf, page), "")


@pytest.fixture
def g() -> cvg.Grounding:
    return cvg.Grounding(cvg.PageIndex(INDEX_DATA), page_text)


def one(g: cvg.Grounding, answer: str, attached):
    verdicts = g.check_answer(answer, attached)
    assert len(verdicts) == 1, f"expected exactly 1 claim unit, got {len(verdicts)}"
    return verdicts[0]


# ── 出典のパース ──────────────────────────────────────────────────────────
@pytest.mark.parametrize("text,expected", [
    # 繁/日 と 简 の両方が実データに出る (同じ答案の中で混ざったことすらある)
    ("『画面目視判読 workflow p.6』", [("workflow", (6,))]),
    ("[画面目视判读 p.6]", [(None, (6,))]),
    # 頁名なし / 範囲 / 複数列挙
    ("『画面目視判読 annotated p.2–4, p.7』", [("annotated", (2, 3, 4, 7))]),
    ("[画面目视判读 p.174] [画面目视判读 p.175]", [(None, (174,)), (None, (175,))]),
    ("『画面目視判読 annotated p.2』『画面目視判読 workflow p.6』",
     [("annotated", (2,)), ("workflow", (6,))]),
    # 全角 (NFKC 前は p.6 に見えない)
    ("『画面目視判読 ｐ．６』", [(None, (6,))]),
])
def test_parse_citations(text, expected):
    got = [(c.pdf, c.pages) for c in cvg.parse_citations(cvg.nfkc(text))]
    assert got == expected


def test_marker_far_from_page_number_is_not_a_citation(g):
    """窓 (~40 字) の外の `p.N` は別の主張の出典 —— 地の文の「画面目視判読」に巻き込まない。"""
    answer = "これは画面目視判読という手段の説明であって、" + "あ" * 45 + "p.6 とは関係ない。"
    assert g.check_answer(answer, [("workflow", 6)]) == []


def test_marker_without_any_page_is_not_a_unit(g):
    assert g.check_answer("画面目視判読の内容はここまで。", [("workflow", 6)]) == []


# ── 判定 5 種 ─────────────────────────────────────────────────────────────
def test_page_grounded_when_activity_name_is_printed_on_the_page(g):
    v = one(g, "`A_TWO`（偽イベント一 › 偽活動二）では偽項目乙のみ。『画面目視判読 workflow p.6』",
            [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED and not v.no_entity


def test_no_entity_unit_is_page_grounded_but_counted_separately(g):
    v = one(g, "画面には入力欄が上から順に並んでいます。『画面目視判読 workflow p.6』",
            [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED and v.no_entity


def test_label_attributed_when_entity_only_in_folded_set(g):
    """A_THREE は p.6 の頁テキストに無いが、同 form・同 hidden_items = 折り畳み集合に在る。

    これが N2 が狙う形態そのもの: 底層の事実は真 (索引が言っている) だが、出処が
    『画面目視判読』になっている。
    """
    v = one(g, "この表示は `A_THREE` でも用いられます。『画面目視判読 workflow p.6』",
            [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED
    assert any(e["status"] == "label" for e in v.entities)


def test_label_attributed_accepts_fullwidth_oid(g):
    v = one(g, "この表示は `Ａ＿ＴＨＲＥＥ` でも用いられます。『画面目視判読 workflow p.6』",
            [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED


def test_page_own_block_identity_is_not_flagged(g):
    """頁の**宛名** (属するブロックの form/activity) は label の見出しで全頁に付いている。

    「この頁は FA の画面だ」は捏造ではなく宛名の復唱 —— ここを焼くと、頁テキストに
    フォーム名を刷らない頁 (コードリスト等) の正しい記述が全部赤くなる。
    """
    v = one(g, "`FA` のコードリストです。『画面目視判読 annotated p.6』", [("annotated", 6)])
    assert v.klass == cvg.PAGE_GROUNDED
    assert [e["status"] for e in v.entities] == ["own"]


def test_other_form_on_annotated_page_is_off_page(g):
    v = one(g, "`FB` の項目です。『画面目視判読 annotated p.6』", [("annotated", 6)])
    assert v.klass == cvg.OFF_PAGE


def test_own_activity_absent_from_page_text_is_not_flagged(g):
    """workflow 頁に OID は 1 つも刷られていない (S0 実測)。ブロック 2 頁目以降は
    見出しすら無い —— 自ブロックの宛名を書いただけで赤くなると闸が鳴りっぱなしになる。"""
    v = one(g, "`A_ONE` の画面です。『画面目視判読 workflow p.4』", [("workflow", 4)])
    assert v.klass == cvg.PAGE_GROUNDED
    assert [e["status"] for e in v.entities] == ["own"]


def test_off_page_when_entity_is_neither_on_page_nor_in_label(g):
    """A_FOUR は同じ form だが hidden_items が違う = 別画面 = 折り畳み集合の外。"""
    v = one(g, "`A_FOUR` でも同項目が出ます。『画面目視判読 workflow p.6』", [("workflow", 6)])
    assert v.klass == cvg.OFF_PAGE


def test_out_of_range_when_cited_page_is_not_attached(g):
    v = one(g, "`A_THREE` の画面です。『画面目視判読 workflow p.9』", [("workflow", 6)])
    assert v.klass == cvg.OUT_OF_RANGE


def test_out_of_range_wins_over_entity_classes(g):
    """1 頁でも添付外を引いたら、その主張は接地の話以前に出処が嘘 —— 先に落とす。"""
    v = one(g, "偽項目乙が並びます。『画面目視判読 workflow p.6, p.9』", [("workflow", 6)])
    assert v.klass == cvg.OUT_OF_RANGE


def test_ambiguous_when_page_number_is_attached_in_both_pdfs(g):
    v = one(g, "偽項目乙の欄があります。『画面目視判読 p.6』", [("workflow", 6), ("annotated", 6)])
    assert v.klass == cvg.AMBIGUOUS


def test_page_number_without_pdf_name_resolves_when_unique(g):
    v = one(g, "`A_TWO` の画面です。『画面目視判読 p.6』", [("workflow", 6), ("annotated", 2)])
    assert v.klass == cvg.PAGE_GROUNDED
    assert v.pages == (("workflow", 6),)


# ── 有界照合 ──────────────────────────────────────────────────────────────
def test_oid_match_is_token_bounded(g):
    """`FB` が `FBX` の中に当たると、無関係な語が実体に化けて全部 OFF_PAGE になる。"""
    v = one(g, "FBX の欄があります。『画面目視判読 workflow p.6』", [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED and v.no_entity


def test_bounded_oid_outside_page_and_label_is_off_page(g):
    v = one(g, "`FB` の項目が出ています。『画面目視判読 workflow p.6』", [("workflow", 6)])
    assert v.klass == cvg.OFF_PAGE


# ── 項目グループ名 (N3 が label に載せる頁索引メタ) ───────────────────────
def test_group_heading_printed_on_the_page_is_grounded(g):
    v = one(g, "「偽枠一」の枠が最初に来ます。『画面目視判読 annotated p.2』", [("annotated", 2)])
    assert v.klass == cvg.PAGE_GROUNDED
    assert [(e["kind"], e["status"]) for e in v.entities] == [("group", "page")]


def test_continued_group_name_is_label_attributed(g):
    """続きの枠は**見出しが前の頁**に在る。その頁の画像には名前が無いので、名前を挙げて
    『画面目視判読』と書けたということは label の頁索引メタを読んだということ。

    N3 の合格判据 (LABEL_ATTRIBUTED = 0) はこれが見えないと枠名の捏造に素通しになる。
    """
    v = one(g, "続いて「偽枠二」の枠が来ます。『画面目視判読 annotated p.2』", [("annotated", 2)])
    assert v.klass == cvg.LABEL_ATTRIBUTED
    assert v.entities[0]["kind"] == "group" and v.entities[0]["continued"] is True


def test_group_names_take_the_longest_match(g):
    """枠名も入れ子になる (偽枠一 ⊂ 偽枠一_続き)。短い方まで名指し扱いすると、
    頁に在る枠を書いただけで続きの枠まで巻き添えになる。"""
    v = one(g, "「偽枠一_続き」の枠です。『画面目視判読 annotated p.2』", [("annotated", 2)])
    assert [e["oid"] for e in v.entities] == ["GD"]


def test_unnamed_group_is_not_an_entity(g):
    ents = g.index.page_group_entities("annotated", 2)
    assert [e.oid for e in ents] == ["GA", "GB", "GD"]      # 無題の GC は入らない
    assert g.index.page_group_entities("workflow", 6) == []


def test_group_names_are_skipped_when_the_index_has_none():
    """N3 以前の索引でも落ちない (黙って素通し)。"""
    g = cvg.Grounding(cvg.PageIndex(INDEX_NO_GROUPS), page_text)
    v = one(g, "続いて「偽枠二」の枠が来ます。『画面目視判読 annotated p.2』", [("annotated", 2)])
    assert v.klass == cvg.PAGE_GROUNDED and v.no_entity


def test_group_entities_do_not_leak_to_other_pages(g):
    """p.3 の枠名を p.2 の主張で書いても、p.2 の枠一覧には無い = 実体にならない
    (頁ごとの集合であって、フォーム全体の辞書ではない)。"""
    v = one(g, "「偽枠三」の枠です。『画面目視判読 annotated p.2』", [("annotated", 2)])
    assert v.klass == cvg.PAGE_GROUNDED and v.no_entity


# ── 主張単元の範囲 ────────────────────────────────────────────────────────
def test_unit_extends_back_to_the_previous_citation(g):
    """出処が単独行で後置される形 (実データに頻出) でも、それが担っている本文まで見る。"""
    answer = ("同じ表示は以下にも共通です。\n"
              "\n"
              "- `A_THREE`\n"
              "\n"
              "名称は対応表より。『画面目視判読 workflow p.6』")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED


def test_unit_does_not_reach_past_the_previous_citation(g):
    answer = ("`A_FOUR` の画面です。『画面目視判読 workflow p.20』\n"
              "この画面には項目が並びます。『画面目視判読 workflow p.6』")
    verdicts = g.check_answer(answer, [("workflow", 6), ("workflow", 20)])
    assert [v.klass for v in verdicts] == [cvg.PAGE_GROUNDED, cvg.PAGE_GROUNDED]
    assert verdicts[1].no_entity


def test_extension_takes_the_whole_list_block(g):
    """箇条書きの後に出典が後置された時は**塊ごと**取る。

    「中身が足りたら止める」にすると最後の 1 項目しか入らず、捏造が塊の**先頭**に在れば
    素通りする。ここでは 7 項目の先頭だけが折り畳み集合の活動。
    """
    answer = ("同じ列挙は以下にも当てはまります。\n"
              "\n"
              "- `A_THREE`\n"
              + "".join(f"- 項目{i}\n" for i in range(2, 8))
              + "\n名称は対応表より。『画面目視判読 workflow p.6』")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED
    assert v.reason == cvg.REASON_ENTITY


def test_table_attribution_phrase_is_stripped_not_the_whole_sentence(g):
    """「対応表」を含む**文**を丸ごと中身ゼロ扱いにすると、混在文を持つ出典行まで
    上へ伸びて、手前の行の実体を巻き込む。落とすのは帰属**句**だけ。"""
    answer = ("- 別の時点のアクティビティは `A_FOUR` です。\n"
              "- 名称は対応表より。添付の画面では偽項目乙と偽項目丙が確認でき、"
              "個別の偽入力欄は当該頁には出ていません。『画面目視判読 workflow p.6』")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED
    assert "A_FOUR" not in v.unit.text


def test_pure_attribution_line_still_extends_upward(g):
    """逆側: 帰属句しか無い出典行は、担っている本文が上にあるので伸びる (既知捏造 1 件が
    この形)。上の 2 つは同じ `_content_len` の裏表なので両方無いと片方向に壊れる。"""
    answer = ("この表示は `A_THREE` にも当てはまります。\n"
              "名称は対応表より。『画面目視判読 workflow p.6』")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED


def test_unit_ends_at_its_own_citation(g):
    """出典は後置の帰属 —— その後ろに続くカード由来の文はこの主張の担当ではない。"""
    answer = ("画面には偽項目乙が出ています。『画面目視判読 workflow p.6』"
              "なおカードでは `A_FOUR` も列挙されています。[Source: st99__FA__WX.md]")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED


def test_card_citation_bounds_the_scope(g):
    """カード出典もマーカー: 手前のカード事実 (非表示アクティビティの列挙など) を
    画面主張の単元に巻き込むと、頁に無いのは当たり前なので全部 OFF_PAGE になる。

    **同じ行**に置く: 行を分けると行頭起点の規則だけでも緑になり、この規則を
    検査したことにならない (実データの假陽性も同一行の形だった)。
    """
    answer = ("非表示アクティビティ: `A_FOUR` [Source: st99__FA__WX.md]。"
              "画面でも偽項目乙の欄が確認できます。『画面目視判読 workflow p.6』")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED and v.no_entity


def test_longest_name_wins_over_nested_shorter_name(g):
    """活動短名は互いに入れ子になる。裸の部分文字列照合だと長い名前を 1 つ書いただけで
    短い名前の活動まで「名指しされた」ことになる。"""
    v = one(g, "偽活動一_追加検査 の画面です。『画面目視判読 workflow p.6』", [("workflow", 6)])
    assert [e["oid"] for e in v.entities] == ["A_FIVE"]


def test_adjacent_citations_are_one_attribution_list(g):
    """`[… p.6] [… p.20]` は 1 つの頁リスト。割ると同じ本文が最初の頁だけで採点される。"""
    v = one(g, "`A_FOUR` の画面です。[画面目視判読 workflow p.6] [画面目視判読 workflow p.20]",
            [("workflow", 6), ("workflow", 20)])
    assert v.pages == (("workflow", 6), ("workflow", 20))
    assert v.klass == cvg.PAGE_GROUNDED      # A_FOUR は p.20 に写っている


def test_unreadable_page_range_is_not_silently_collapsed(g):
    """`p.6–900` を先頭頁に丸めると「引用頁はこの 1 枚」と誤って断定することになる。"""
    v = one(g, "偽項目乙が並びます。『画面目視判読 workflow p.6–900』", [("workflow", 6)])
    assert v.klass == cvg.AMBIGUOUS


def test_ambiguous_is_flagged_and_not_reported_as_no_entity(tmp_path, g):
    _run_file(tmp_path / "B_m1_T1.json", answer="偽項目乙の欄があります。『画面目視判読 p.6』",
              pages=[("workflow", 6), ("annotated", 6)])
    reports = cvg.analyse_dir(tmp_path, g)
    table = cvg.render_table(reports)
    assert cvg.AMBIGUOUS in cvg.FLAGGED
    assert "**AMBIGUOUS**" in table and "no entity" not in table


def test_verify_pdf_sha_refuses_a_swapped_pdf(tmp_path):
    """頁番号は PDF の版に紐づく。索引と中身がずれた時に黙って出数すると、闸は
    別の画面を根拠に「接地している」と言う。"""
    wf, ann = tmp_path / "wf.pdf", tmp_path / "ann.pdf"
    wf.write_bytes(b"%PDF-1.4 wf")
    ann.write_bytes(b"%PDF-1.4 ann")
    index = cvg.PageIndex(INDEX_DATA)            # sha は "0"*64 / "1"*64 = 一致しない
    with pytest.raises(RuntimeError, match="sha256 mismatch"):
        cvg.verify_pdf_sha(index, {"workflow": wf, "annotated": ann})
    good = json.loads(json.dumps(INDEX_DATA))
    for key, path in (("workflow", wf), ("annotated", ann)):
        good["meta"]["pdfs"][key]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    cvg.verify_pdf_sha(cvg.PageIndex(good), {"workflow": wf, "annotated": ann})


def test_verify_pdf_sha_refuses_a_missing_pdf(tmp_path):
    with pytest.raises(FileNotFoundError):
        cvg.verify_pdf_sha(cvg.PageIndex(INDEX_DATA),
                           {"workflow": tmp_path / "nope.pdf", "annotated": None})


def test_page_numbers_after_the_citation_are_not_part_of_it(g):
    """「〔画面目視判読 workflow p.6〕 ただし、これは p.3–5 ブロックのうち…」の
    ブロック範囲を引用頁に数えると、N1 で仕込んだ正しい但し書きが OUT_OF_RANGE になる。"""
    answer = "偽項目乙が出ています〔画面目視判読 workflow p.6〕。ただし、これは p.3–5 のうち 1 頁です。"
    v = one(g, answer, [("workflow", 6)])
    assert v.pages == (("workflow", 6),)
    assert v.klass == cvg.PAGE_GROUNDED


def test_pdf_name_after_the_break_is_not_borrowed(g):
    answer = "偽項目乙が出ています。画面目視判読 p.6\n\nこれは annotated p.2 とは別です。"
    v = one(g, answer, [("workflow", 6), ("annotated", 2)])
    assert v.pages == (("workflow", 6),)


def test_unit_does_not_reach_past_a_heading(g):
    answer = ("`A_FOUR` について。\n"
              "\n"
              "### 別の節\n"
              "\n"
              "項目が並びます。『画面目視判読 workflow p.6』")
    v = one(g, answer, [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED and v.no_entity


# ── 画面同一性の主張 (実体に解決できない形態への 2 枚目の網) ──────────────
SAMENESS = "所附页面注明与其他活动采用同一显示画面。[画面目视判读 p.6]"

# 「1 枚の頁画像は別の画面の同一性を証明できない」という概念に当たる言い回し。
# 実体に解決できる名前は**わざと入れていない** —— 入れると実体層が先に発火して、
# この規則を検査したことにならない。
FIRES = [
    "この画面は他のアクティビティと共有です。",
    "この表示は他の時点でも共用されています。",
    "他の時点でも同様の画面が使われます。",
    "他の時点の画面と一致します。",
    "他の時点の画面とまったく同じです。",
    "与其他时点的画面完全相同。",
    "其他时点也是同样的画面。",
    "画面は他の時点と共用されている。",
]
# 「1 つの画面の中の話」「同一性の対象が画面ではない」= 概念が違う。
QUIET = [
    "同一画面上に偽項目乙と偽項目丙が並んでいます。",
    "同じ画面に偽項目乙が並びます。",
    "同一の画面に偽項目乙が表示されます。",
    "同一画面内に偽項目乙と偽項目丙が並んでいます。",
    "チェック文言「前回の値と同一である」が出ています。",
    "画面には同じ項目が 2 回出てきます。",
]


@pytest.mark.parametrize("claim", FIRES)
def test_sameness_claim_fires_on_paraphrases(g, claim):
    v = one(g, claim + "『画面目視判読 workflow p.6』", [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED and v.reason == cvg.REASON_SAMENESS


@pytest.mark.parametrize("claim", QUIET)
def test_sameness_claim_stays_quiet(g, claim):
    v = one(g, claim + "『画面目視判読 workflow p.6』", [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED


def test_sameness_does_not_fire_when_two_attached_pages_are_compared(g):
    """見えている 2 枚を見比べて「同じ」と言うのは画像から言える —— label は要らない。"""
    v = one(g, "p.6 と p.20 は同じ画面です。『画面目視判読 workflow p.6 と p.20』",
            [("workflow", 6), ("workflow", 20)])
    assert v.pages == (("workflow", 6), ("workflow", 20))
    assert v.klass == cvg.PAGE_GROUNDED


def test_sameness_rule_ignores_the_citation_marker_itself(g):
    """出典「画面目視判読」自体が『画面』を含む。消さずに照合すると、出典を書いただけで
    画面名詞が 1 つ立ち、同一性語が近くにあれば何でも発火する。"""
    assert not cvg.is_screen_sameness_claim("項目の並びは同じです。『画面目視判読 p.6』")
    assert cvg.is_screen_sameness_claim("他の時点の画面と同じです。『画面目視判読 p.6』")


def test_sameness_vocabulary_is_label_attributed(g):
    v = one(g, SAMENESS, [("workflow", 6)])
    assert v.klass == cvg.LABEL_ATTRIBUTED
    assert v.reason == cvg.REASON_SAMENESS


def test_sameness_rule_can_be_switched_off():
    g = cvg.Grounding(cvg.PageIndex(INDEX_DATA), page_text, sameness_rule=False)
    v = one(g, SAMENESS, [("workflow", 6)])
    assert v.klass == cvg.PAGE_GROUNDED


# ── 集計 / 掩码 ───────────────────────────────────────────────────────────
def _run_file(path, *, arm="B", model="m1", qid="T1", answer="", pages=()):
    path.write_text(json.dumps({
        "_meta": {"arm": arm, "model_id": model, "qid": qid},
        "response": {"answer": answer,
                     "pdf_pages": [{"pdf": p, "page": n} for p, n in pages]},
    }, ensure_ascii=False), encoding="utf-8")


def test_analyse_dir_skips_answers_without_attached_pages(tmp_path, g):
    _run_file(tmp_path / "B_m1_T1.json", answer="この表示は `A_THREE` でも。『画面目視判読 workflow p.6』",
              pages=[("workflow", 6)])
    _run_file(tmp_path / "B_m1_T2.json", qid="T2",
              answer="画面は見ていません。『画面目視判読 workflow p.6』", pages=[])
    reports = cvg.analyse_dir(tmp_path, g)
    assert [r.qid for r in reports] == ["T1"]
    assert reports[0].counts[cvg.LABEL_ATTRIBUTED] == 1


def test_analyse_dir_arm_filter(tmp_path, g):
    _run_file(tmp_path / "A_m1_T1.json", arm="A", answer="x『画面目視判読 workflow p.6』",
              pages=[("workflow", 6)])
    _run_file(tmp_path / "B_m1_T1.json", arm="B", answer="x『画面目視判読 workflow p.6』",
              pages=[("workflow", 6)])
    assert [r.arm for r in cvg.analyse_dir(tmp_path, g, arm="B")] == ["B"]


def test_table_is_masked_by_default(tmp_path, g):
    _run_file(tmp_path / "B_m1_T1.json",
              answer="この表示は `A_THREE`（偽イベント二 › 偽活動三）でも。『画面目視判読 workflow p.6』",
              pages=[("workflow", 6)])
    reports = cvg.analyse_dir(tmp_path, g)
    masked = cvg.render_table(reports)
    assert "A_THREE" not in masked and "偽活動三" not in masked
    assert "LABEL_ATTRIBUTED" in masked and "B_m1_T1.json" in masked
    assert "A_THREE" in cvg.render_table(reports, unmask=True)
