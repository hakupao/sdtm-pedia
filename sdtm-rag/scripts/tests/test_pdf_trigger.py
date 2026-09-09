"""I2-3: PDF 旁路触发判定 (P1 §3 R1/R2/R3 + 反例 N1-N3)。

题面用 P1 预登记的原文 (`evidence/checkpoints/c2r_pre_registration.md` §1/§2) —— 判据
先于实现登记, 实现不得改判据。卡片 fixture 是**合成**的 (假 OID / 假 label): 触发只看
卡片的**形状** (非表示アクティビティ 有几个 / 有没有「式は別ソース」), 不看具体研究值。
"""
from __future__ import annotations

import pytest

from server.pdf_trigger import CardFacts, should_attach_pdf

# ── 合成卡片 (真实卡片的版式, 假值) ────────────────────────────────────
_CARD_TMPL = """---
study: st99
version: VNEW
doc_type: field_card
form_oid: {form}
field_oid: {item}
---

# [偽フォーム {form}] {item} ({item})
- Form: 偽フォーム ({form})
- Item group: 偽グループ ({form}G1)
- 型: text / 任意
- Control: Checkboxes
- Codelist: CL_{item}
- Edit checks: —
- 表示条件: {cond}
- 非表示アクティビティ: {hidden}
- DEMO 例値: —
"""


def card(form="FA", item="ITEMA", cond="常時表示", hidden="A_ONE, A_TWO, A_THREE"):
    return _CARD_TMPL.format(form=form, item=item, cond=cond, hidden=hidden or "—")


ADVANCED = "条件あり (式は別ソース)"
HIDE_ADVANCED = "非表示条件あり (式は別ソース)"

# P1 §1 の T 組 / §2 の N 組 (committed 版の題面を逐字。実項目名は赤線纪律で
# gitignored 側にあり、ここには**サニタイズ済みの題面**が入る —— 触発判定は問題文の
# 語だけを見るので、実名の有無で結果は変わらない)。
T1 = ("帮我看一下st01这个研究的LB这个文件（Form），放的是什么数据，我看更像是采血数据。"
      "我看有身高体重这个数据收集，这个两个数据的收集逻辑是不是只登录一次，然后在后续的"
      "每个visit都显示，而不是每次采血都测量。")
T2 = "AE フォームの「その他」補足の自由記述項目はどんな条件で表示されますか"
T3 = "NAC フォームのカペシタビン投与量（某给药量项）はいつ入力画面に出ますか"
T4 = "術前化学療法 A 群で、Day1 と Day8 のLB表单は採取項目がどう違いますか"
T5 = "手術イベントの「术前LB活动名」は常に表示されますか、条件付きですか"
T6 = "TME フォームの画面で、項目はどう並んでいますか、グループ分けは"

N1 = "VS ドメインの Required 変数を教えて"
N2 = "DM フォームに生年月日の項目はありますか"
N3 = "体重 STAT 項 (選択子 `__LB__W`) のコードリストは何ですか"


def facts(*texts):
    return [f for f in (CardFacts.from_text(t) for t in texts) if f is not None]


# ── 解析 ───────────────────────────────────────────────────────────────
def test_card_facts_read_front_matter_and_hidden_list():
    f, = facts(card())
    assert (f.form_oid, f.item_oid) == ("FA", "ITEMA")
    assert f.hidden_activities == frozenset({"A_ONE", "A_TWO", "A_THREE"})
    assert f.has_advanced_condition is False


def test_card_facts_flag_both_spellings_of_the_missing_formula():
    assert facts(card(cond=ADVANCED))[0].has_advanced_condition
    assert facts(card(cond=HIDE_ADVANCED))[0].has_advanced_condition


def test_card_facts_ignore_a_plain_inline_condition():
    """`ZFLAG_YN == 1` は式が**カードに載っている** —— 画面を見に行く理由が無い。"""
    assert not facts(card(cond="非表示条件: ZFLAG_YN == 1"))[0].has_advanced_condition


def test_non_card_text_is_not_a_card():
    """手順書章節 chunk は field_card ではない。None を返さないと doc chunk が
    「非表示アクティビティ 0 個のカード」として静かに数に入る。"""
    assert CardFacts.from_text("---\nstudy: st99\ndoc_type: protocol_section\n---\n本文") is None
    assert CardFacts.from_text("## SDTMIG 6.3 VS ドメイン\n本文だけ") is None


def test_em_dash_hidden_list_is_empty_not_a_one_element_set():
    assert facts(card(hidden="—"))[0].hidden_activities == frozenset()


# ── R1/R2/R3 ───────────────────────────────────────────────────────────
def test_r1_needs_both_two_activities_and_a_timing_word():
    two = facts(card(hidden="A_ONE, A_TWO"))
    assert should_attach_pdf("この項目はどの visit で表示されますか", two).rule == "R1"
    # 語だけ / 活動だけ ではどちらも発火しない (単独条件では不足)
    assert not should_attach_pdf("この項目の型は何ですか", two).fire
    one = facts(card(hidden="A_ONE"))
    assert not should_attach_pdf("どの visit で表示されますか", one).fire


def test_r2_needs_the_formula_to_be_missing_from_the_card():
    # 非表示 1 件だけ = R1 の条件を満たさない ⇒ R2 単独の判別になる (規則は R1→R2→R3 順)
    adv = facts(card(cond=ADVANCED, hidden="A_ONE"))
    assert should_attach_pdf("どんな条件で表示されますか", adv).rule == "R2"
    plain = facts(card(cond="非表示条件: X == 1", hidden="A_ONE"))
    assert not should_attach_pdf("どんな条件で表示されますか", plain).fire


def test_r3_needs_a_layout_word_and_a_card_that_the_study_channel_vouched_for():
    """M10: R3 には関連性のフロアが要る。corpus=both では study 側は**類似度の閾値
    なしに**配額で埋まるので、CDISC 寄りの問いに 画面/並び が入っているだけで、
    たまたま混じった 1 枚のカードで発火してしまう。フロア = そのカードが study 直查
    (`via_lookup`) 経由で来た、または問い自体が直查の強通道に当たること。"""
    vouched = [f.__class__(**{**f.__dict__, "via_lookup": True}) for f in facts(card(hidden="—"))]
    assert should_attach_pdf("画面のレイアウトを教えて", vouched).rule == "R3"
    assert should_attach_pdf("画面のレイアウトを教えて", facts(card(hidden="—")),
                             study_strong_hit=True).rule == "R3"
    assert not should_attach_pdf("画面のレイアウトを教えて", facts(card(hidden="—"))).fire
    assert not should_attach_pdf("画面のレイアウトを教えて", []).fire


# ── r3 修正 (V3 attempt 1 の T6 失敗を受けた予登記の改訂) ─────────────────
# フロアは 3 つの or: (a) 直查経由のカード (b) 問いが強通道に命中
# (c) 問いが study の**フォームを名指し**している (`resolve().form_scopes` 非空)。
def test_r3_floor_accepts_a_question_that_names_a_study_form():
    """T6 型 = 純粋な画面レイアウト問い。カードは cosine で来るだけなので (a) も (b) も
    満たさないが、問い自体がこの研究のフォームを名指ししている以上「偶然混じった
    1 枚」ではない。"""
    d = should_attach_pdf("画面で項目はどう並んでいますか", facts(card(hidden="—")),
                          study_form_named=True)
    assert d.rule == "R3" and "フォーム" in d.reason


def test_a_form_named_only_inside_a_card_does_not_clear_the_floor():
    """(c) の入力は**問い**。フォーム名がカード本文にしか無いなら、そのカードは配額で
    紛れ込んだ可能性が残るのでフロアとしては効かない。判定そのものは
    `PdfPageIndex.form_named_in` 側 (問いだけを見る) に閉じている。"""
    from server.pdf_context import PdfPageIndex
    idx = PdfPageIndex({
        "meta": {"pdfs": {}}, "names": {"forms": {"XFORM": "偽評価票"}},
        "workflow": {"n_pages": 1, "blocks": []},
        "annotated": {"n_pages": 1, "blocks": [], "item_pages": {}},
    })
    in_card = card(form="XFORM", hidden="—") + "\n- Form: 偽評価票 (XFORM)\n"
    unnamed = "画面の並びを教えてください"
    assert idx.form_named_in(unnamed) is None
    assert not should_attach_pdf(unnamed, facts(in_card),
                                 study_form_named=idx.form_named_in(unnamed) is not None).fire
    named = "偽評価票フォームの画面で、項目はどう並んでいますか"
    assert idx.form_named_in(named) == "XFORM"
    assert should_attach_pdf(named, facts(in_card),
                             study_form_named=True).rule == "R3"


def test_r1_and_r2_do_not_need_the_floor():
    """フロアは R3 だけ。R1/R2 はカードの**中身**(非表示名簿 / 式が別ソース) が
    証拠なので、そのカードが偶然混じったものではないことを自分で示している。"""
    two = facts(card(hidden="A_ONE, A_TWO"))
    assert should_attach_pdf("どの visit で表示されますか", two).rule == "R1"
    adv = facts(card(cond=ADVANCED, hidden="A_ONE"))
    assert should_attach_pdf("どんな条件で表示されますか", adv).rule == "R2"


@pytest.mark.parametrize("word", ["タイミング", "毎回", "違い", "違う", "比較", "出ます"])
def test_r1_difference_and_timing_class(word):
    """M9: P1 に登記した追加語クラスを code 側が全部持っていること (doc と code の
    食い違いは、登記した判据と実際の判定がズレるという最も気付きにくい形の嘘)。"""
    two = facts(card(hidden="A_ONE, A_TWO"))
    assert should_attach_pdf(f"この項目の{word}を教えて", two).rule == "R1"


def test_empty_card_set_never_fires_whatever_the_question():
    """卡片ゼロ = study 側が何も当たっていない。鍵 (form/item OID) が無い以上、
    どのページを付けるかを決める材料が無い —— 語だけで発火させてはいけない。"""
    for q in (T1, T2, T3, T4, T5, T6):
        assert not should_attach_pdf(q, [], study_strong_hit=True).fire


# ── P1 予登記: T 組は全部発火 / N 組は 1 つも発火しない ────────────────
@pytest.mark.parametrize("q,cards,rule", [
    (T1, [card(item="ZSTAT", hidden="A_ONE, A_TWO, A_THREE"),
          card(item="ZKSTA", hidden="A_ONE, A_FOUR")], "R1"),
    (T2, [card(form="FB", item="ZOTHER", cond=ADVANCED, hidden="A_ONE")], "R2"),
    (T3, [card(form="FC", item="ZDOSE", cond=ADVANCED, hidden="A_ONE")], "R2"),
    (T4, [card(item="ZTESTX", hidden="A_ONE, A_TWO"),
          card(item="ZTESTY", hidden="A_TWO, A_THREE")], "R1"),
    (T5, [card(item="ZPERFX", hidden="A_ONE, A_TWO")], "R1"),
    (T6, [card(form="FD", item="ZTMEA", hidden="—")], "R3"),
])
def test_pre_registered_positive_questions_fire(q, cards, rule):
    # T6 は R3 ⇒ M10 のフロアが要る。実運用では form 名を含む問いが study 直查の
    # 強通道に当たって来るので、ここでは strong_hit 側で満たす。
    d = should_attach_pdf(q, facts(*cards), study_strong_hit=True)
    assert d.fire, d.reason
    assert d.rule == rule, d.reason


# M10 で足した反例。corpus=both の配額で紛れ込んだ 1 枚 (直查経由ではない) + CDISC 寄りの
# 問い。語 (画面) だけで発火してはいけない。
N4_CDISC = "SDTM の VS ドメインで、標準の画面並びに相当する変数順序はどう決まりますか"
# N5 = V3 で実際に走らせた反例 (gitignored の run 索引にある原文)。study のフォームを
# 1 つも名指ししていないので r3 の (c) でも発火しない。
N5_CDISC = "SDTM の VS ドメインは画面のどの項目から作りますか"


@pytest.mark.parametrize("q,cards", [
    (N1, []),                                             # study 側ゼロ命中
    (N2, [card(form="FE", item="ZBIRTH", hidden="A_ONE, A_TWO")]),
    (N3, [card(item="ZSTAT", hidden="A_ONE, A_TWO, A_THREE")]),
    (N4_CDISC, [card(form="FF", item="ZSTRAY", hidden="—")]),
    (N5_CDISC, [card(form="FF", item="ZSTRAY", hidden="—")]),
])
def test_pre_registered_negative_questions_do_not_fire(q, cards):
    # r3 の 3 つのフロアをすべて外した状態 —— N 組はどれも study のフォームを名指しせず、
    # 直查にも当たらない (合成 lookup での確認は上の (c) テスト)。
    d = should_attach_pdf(q, facts(*cards))
    assert not d.fire, f"误触 {d.rule}: {d.reason}"
    assert d.rule is None


def test_decision_reason_names_the_evidence_not_just_the_rule():
    """理由が "R1" だけだと、なぜ付いたのか (どの活動/どの語) が後から追えない ——
    誤触の切り分けはその 2 つが要る。"""
    d = should_attach_pdf("どの visit で表示されますか", facts(card(hidden="A_ONE, A_TWO")))
    assert "visit" in d.reason and "2" in d.reason


def test_card_facts_carry_the_lookup_provenance():
    """`via_lookup` は chunk 側のフラグで、カード本文からは読めない —— 本文だけ見る
    `from_text` の既定は False (「保証なし」) でなければならない。"""
    assert facts(card())[0].via_lookup is False
    from server.pdf_trigger import parse_chunks

    class _Chunk:
        def __init__(self, text, via):
            self.text, self.via_lookup = text, via
    got = parse_chunks([_Chunk(card(item="ZA"), True), _Chunk(card(item="ZB"), False),
                        _Chunk("front matter の無い chunk", True)])
    assert [(c.item_oid, c.via_lookup) for c in got] == [("ZA", True), ("ZB", False)]
