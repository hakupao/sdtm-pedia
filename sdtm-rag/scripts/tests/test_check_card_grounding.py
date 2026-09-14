"""N5: study 出典 (カード / 手順書章節) の接地闸 (`scripts/study/c2r_eval/check_card_grounding.py`)。

合成 catalog + 偽の文書テキスト (dict) だけで判定を固める。磁盘の cards/docs は
`SourceStore` の読み出し 1 箇所に寄せてあるので、ここでは dict を渡す。偽名は
`test_pdf_context.py` / `test_check_visual_grounding.py` の流儀に合わせる。
"""
from __future__ import annotations

import json

from scripts.study.c2r_eval import check_card_grounding as ccg

CATALOG = {
    "study": "st99",
    "forms": [{"oid": "FA", "name": "偽フォーム甲"}, {"oid": "FB", "name": "偽フォーム乙"}],
    "events": [{"oid": "E_ONE", "name": "偽イベント一"}],
    "activities": [{"oid": "A_ONE", "name": "偽活動一"}, {"oid": "A_TWO", "name": "偽活動二"},
                   {"oid": "A_ZOPE", "name": "偽手術活動"}],
    "items": [
        {"form_oid": "FA", "item_oid": "WX", "group_oid": "GA", "group_name": "偽枠一"},
        {"form_oid": "FA", "item_oid": "WEIGHT", "group_oid": "GA", "group_name": "偽枠一"},
        {"form_oid": "FA", "item_oid": "WEIGHTZST", "group_oid": "GA", "group_name": "偽枠一"},
        {"form_oid": "FB", "item_oid": "PS", "group_oid": "GB", "group_name": "偽枠二"},
    ],
}

# 偽の文書テキスト。カードの本文は実データと同じ形 (frontmatter + 箇条書き)。
DOCS = {
    "st99__FA__WEIGHT.md": (
        "---\nstudy: st99\nform_oid: FA\nfield_oid: WEIGHT\n---\n"
        "# [偽フォーム甲 FA] 体重 (WEIGHT)\n- Item group: 偽枠一 (GA)\n"
        "- 非表示アクティビティ: A_ONE, A_TWO\n"),
    "st99__FA__WEIGHTZST.md": (
        "---\nstudy: st99\nform_oid: FA\nfield_oid: WEIGHTZST\n---\n"
        "# [偽フォーム甲 FA] 体重未実施 (WEIGHTZST)\n- 非表示アクティビティ: A_ZOPE\n"),
    "st99__doc01__s8_1.md": "---\ndoc_type: protocol_section\n---\n## 8.1 検査\n体重は各来院で測定する。\n",
}


def _gate(retrieved=("st99__FA__WEIGHT.md", "st99__FA__WEIGHTZST.md", "st99__doc01__s8_1.md")):
    return ccg.Grounding(ccg.Vocab.from_catalog(CATALOG), ccg.SourceStore.from_dict("st99", DOCS)), list(retrieved)


def check(answer, retrieved=None):
    g, r = _gate() if retrieved is None else _gate(retrieved)
    return g.check_answer(answer, r)


# ── 判定 ───────────────────────────────────────────────────────────────
def test_an_oid_written_in_the_cited_card_is_source_grounded():
    vs = check("体重 (WEIGHT) は A_ONE と A_TWO で非表示である [Source: st99__FA__WEIGHT.md]")
    assert [v.klass for v in vs] == [ccg.SOURCE_GROUNDED]
    assert {e["oid"] for e in vs[0].entities} == {"WEIGHT", "A_ONE", "A_TWO"}


def test_an_oid_absent_from_the_cited_card_but_in_another_retrieved_source_is_miscited():
    """A_ZOPE は WEIGHTZST のカードに在るが、出典は WEIGHT のカード = 挂错出典。"""
    vs = check("体重 (WEIGHT) は A_ZOPE で非表示である [Source: st99__FA__WEIGHT.md]")
    assert vs[0].klass == ccg.CONTEXT_MISCITED
    st = {e["oid"]: e["status"] for e in vs[0].entities}
    assert st["A_ZOPE"] == ccg.CONTEXT_MISCITED and st["WEIGHT"] == ccg.SOURCE_GROUNDED


def test_an_oid_in_no_retrieved_source_is_ungrounded():
    """文脈のどこにも無い活動 OID を、あるカードの非表示活動として挙げ、そのカードの真の
    出典を付ける (N4 の真陽性は兄弟カードからの移植 = 下の CONTEXT_MISCITED の形; ここは
    その一段上の「凭空」)。"""
    vs = check("体重 (WEIGHT) は A_ZOPE で非表示である [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md", "st99__doc01__s8_1.md"])
    assert vs[0].klass == ccg.UNGROUNDED
    assert [e["oid"] for e in vs[0].entities if e["status"] == ccg.UNGROUNDED] == ["A_ZOPE"]


def test_a_cited_path_that_does_not_exist_is_bad_source():
    """出典そのものの捏造。実体照合は走らせない —— 照合先が無い。"""
    vs = check("体重は A_ONE で非表示である [Source: st99__FA__GHOST.md]")
    assert vs[0].klass == ccg.BAD_SOURCE and vs[0].entities == ()


def test_the_worst_entity_decides_the_unit_class():
    vs = check("WEIGHT は A_ONE と A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert vs[0].klass == ccg.UNGROUNDED


def test_a_unit_without_any_oid_is_no_entity_and_not_flagged():
    vs = check("体重は各来院で測定する [Source: st99__doc01__s8_1.md]")
    assert vs[0].klass == ccg.NO_ENTITY and vs[0].klass not in ccg.FLAGGED


# ── 実体の取り方 ───────────────────────────────────────────────────────
def test_oids_inside_the_source_marker_itself_are_not_entities():
    """`[Source: st99__FA__WEIGHT.md]` の中の FA / WEIGHT は出典の一部であって主張ではない。
    数えると出典を書いただけで実体が 2 つ立ち、しかも必ず grounded になって数を薄める。"""
    vs = check("各来院で測定する [Source: st99__FA__WEIGHT.md]")
    assert vs[0].entities == () and vs[0].klass == ccg.NO_ENTITY


def test_oid_matching_is_token_bounded():
    """`WEIGHTZST` の中の `WEIGHT`、`A_ONE_X` の中の `A_ONE` は別の語。"""
    vs = check("WEIGHTZST は A_ONE_X で非表示 [Source: st99__FA__WEIGHTZST.md]")
    assert {e["oid"] for e in vs[0].entities} == {"WEIGHTZST"}


def test_short_oids_are_skipped_and_counted():
    """2 字の OID (実データにも普通に在る) は英字 2 字の語に当たり放題。査せず、数だけ報告。"""
    vocab = ccg.Vocab.from_catalog(CATALOG)
    assert "PS" not in vocab.oids and "WX" not in vocab.oids
    # 落ちるのは項目だけではない: 2 字の枠 (GA/GB) も。フォーム (FA/FB) は長さに関係なく
    # 実体にしない (下のテスト)。
    assert vocab.n_skipped_short == 6 and set(vocab.oids) == {
        "A_ONE", "A_TWO", "A_ZOPE", "E_ONE", "WEIGHT", "WEIGHTZST"}


def test_form_oids_are_never_entities():
    """フォーム OID は文書の**名前** (path / 対応表 / 画面 label の全部に出る) で、活動 OID の
    族名としても書かれる (「NAC 系アクティビティ」)。中身の主張ではない。"""
    cat = json.loads(json.dumps(CATALOG))
    cat["forms"].append({"oid": "LONGFORM", "name": "長い名のフォーム"})
    assert "LONGFORM" not in ccg.Vocab.from_catalog(cat).oids


def test_glossary_style_names_in_parentheses_are_not_scanned():
    """対応表の書式 `A_ONE(偽イベント一 › WEIGHT2コース)`: 括弧の中は名前。名前に OID 形の
    語が偶然入っても (実データ: 「ZNAC1コース」の ZNAC1) 実体ではない。"""
    cat = json.loads(json.dumps(CATALOG))
    cat["items"].append({"form_oid": "FA", "item_oid": "WEIGHT2", "group_oid": "GA", "group_name": ""})
    g = ccg.Grounding(ccg.Vocab.from_catalog(cat), ccg.SourceStore.from_dict("st99", DOCS))
    vs = g.check_answer("`A_ONE(偽イベント一 › WEIGHT2コース)` で非表示 [Source: st99__FA__WEIGHT.md]",
                        ["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ONE"}
    # 括弧の外なら実体
    vs = g.check_answer("`A_ONE` と WEIGHT2 で非表示 [Source: st99__FA__WEIGHT.md]", ["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ONE", "WEIGHT2"}


def test_an_item_whose_own_card_was_retrieved_is_a_document_name_not_a_claim():
    """WEIGHTZST のカードが文脈に在る run で、WEIGHT のカードを引いた文に WEIGHTZST が
    出る = 兄弟項目の言及。文脈に在る文書の名前であって、WEIGHT カードの中身の主張ではない。"""
    vs = check("WEIGHT と WEIGHTZST は対になる [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md", "st99__FA__WEIGHTZST.md"])
    # 緑と同じ扱いだが別に数える (複審 MAJOR-2: 真の命中と混ぜると緑が水増しされる)
    assert vs[0].klass == ccg.SIBLING_NAMED and ccg.SIBLING_NAMED not in ccg.FLAGGED
    assert {e["oid"]: e["status"] for e in vs[0].entities}["WEIGHTZST"] == ccg.SIBLING_NAMED
    # そのカードが検索されていなければ、ただの文脈外 OID
    vs = check("WEIGHT と WEIGHTZST は対になる [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert vs[0].klass == ccg.UNGROUNDED


def test_an_activity_from_a_sibling_card_is_still_miscited():
    """設計の要: 活動 OID はカードの中身 (非表示リスト) の主張。兄弟カードに在っても、
    引いたカードに無ければ出典違い —— N4 の真陽性はこの形 (別カードの非表示リストから移植)。"""
    vs = check("WEIGHT は A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md", "st99__FA__WEIGHTZST.md"])
    assert vs[0].klass == ccg.CONTEXT_MISCITED


def test_the_question_and_attached_pages_count_as_context_not_as_source():
    g, _ = _gate(["st99__FA__WEIGHT.md"])
    vs = g.check_answer("WEIGHT は A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]", ["st99__FA__WEIGHT.md"],
                        extra_context="質問: A_ZOPE ではどう表示されますか")
    assert vs[0].klass == ccg.CONTEXT_MISCITED


def test_a_sentence_saying_the_oid_is_not_in_the_list_is_negated_not_flagged():
    """「A_ZOPE はこのカードの非表示一覧に含まれない」: 閘が見つけた事実 (A_ZOPE が引いた文書に
    無い) と文の主張が一致している。疑いとして立てない。"""
    vs = check("`A_ZOPE` は WEIGHT の非表示アクティビティに含まれません [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert vs[0].klass == ccg.NEGATED and ccg.NEGATED not in ccg.FLAGGED


def test_the_polite_progressive_negation_is_recognised():
    """judge (復測): 「含まれていません」が正規表現から漏れて、真の否定文が赤になった。"""
    vs = check("`A_ZOPE` は WEIGHT の非表示一覧に含まれていません [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert vs[0].klass == ccg.NEGATED


def test_negation_only_shields_the_sentence_it_is_in():
    """否定は文単位。前の文で肯定的に挙げた OID は、後の文の否定で守られない。"""
    vs = check("WEIGHT は A_ZOPE で非表示です。A_TWO は含まれません [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    st = {e["oid"]: e["status"] for e in vs[0].entities}
    assert st["A_ZOPE"] == ccg.UNGROUNDED and vs[0].klass == ccg.UNGROUNDED


def test_a_negation_in_a_later_clause_of_the_same_sentence_does_not_shield_an_earlier_oid():
    """複審 MINOR-1: 「A_ZOPE で非表示であり、他の活動は含まれません」の A_ZOPE は肯定の主張。
    否定は同じ小句で、しかも OID より後ろに無ければ効かない。"""
    vs = check("WEIGHT は A_ZOPE で非表示であり、他の活動は含まれません [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"]: e["status"] for e in vs[0].entities}["A_ZOPE"] == ccg.UNGROUNDED
    vs = check("含まれないのは A_ZOPE ではなく WEIGHT だ [Source: st99__FA__WEIGHT.md]", retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"]: e["status"] for e in vs[0].entities}["A_ZOPE"] == ccg.UNGROUNDED   # 否定が前


def test_a_comma_separated_list_before_the_negation_is_one_clause():
    """日本語の列挙は読点でつなぐ。「A_ZOPE、A_TWO では非表示指定はありません」の A_ZOPE を
    読点で切り離すと、正しい否定が赤になる (実データ 2 単元)。"""
    vs = check("`A_ZOPE`、`A_TWO` および `A_ONE` では、活動による非表示指定はありません [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert vs[0].klass == ccg.NEGATED


def test_a_decimal_or_page_number_does_not_split_the_sentence():
    """複審 NIT-4: `8.1` / `p.174` の `.` で切ると OID と否定の語が離れ、偽の赤になる。"""
    vs = check("A_ZOPE は 8.1 節の一覧に含まれません [Source: st99__FA__WEIGHT.md]", retrieved=["st99__FA__WEIGHT.md"])
    assert vs[0].klass == ccg.NEGATED


def test_the_masked_table_lists_negated_units_for_spot_check():
    vs = check("`A_ZOPE` は含まれません [Source: st99__FA__WEIGHT.md]", retrieved=["st99__FA__WEIGHT.md"])
    rep = ccg.AnswerReport(file="f", arm="B", model="m", qid="T1", n_units=1,
                           counts={k: 0 for k in ccg.CLASSES} | {ccg.NEGATED: 1}, verdicts=vs)
    t = ccg.render_table([rep])
    assert "negated units (1" in t and "A_ZOPE" not in t


def test_the_payload_records_whether_the_context_was_complete():
    pay = ccg._json_payload([], ccg.Vocab.from_catalog(CATALOG), n_questions=0, page_text_available=False)
    assert pay["context"] == {"n_questions": 0, "page_text_available": False}


def test_a_positive_transplant_is_not_shielded_by_a_negation_elsewhere_in_the_unit():
    """N4 真陽性の形は肯定 (「…を非表示活動として挙げる」)。同じ単元の別の文に否定が
    在っても、その文に無ければ赤のまま。"""
    vs = check("WEIGHT のカードは A_ZOPE を非表示活動として列挙している。なお他の活動は含まれません "
               "[Source: st99__FA__WEIGHT.md]", retrieved=["st99__FA__WEIGHT.md", "st99__FA__WEIGHTZST.md"])
    assert vs[0].klass == ccg.CONTEXT_MISCITED


def test_a_standalone_oid_inside_a_glued_parenthetical_is_still_an_entity():
    """複審 MAJOR-3: 括弧を丸ごと捨てると `WEIGHT (A_ZOPE で非表示扱い)` が素通りする。
    名前の中の OID 形の語は日本語に接着している (ZNAC1コース); 独立した語は本物の言及。"""
    vs = check("WEIGHT (A_ZOPE で非表示扱い) [Source: st99__FA__WEIGHT.md]", retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"WEIGHT", "A_ZOPE"} and vs[0].klass == ccg.UNGROUNDED


def test_a_name_parenthetical_without_the_arrow_is_still_a_name():
    """モデルは `›` を省いて `A_ONE(A群 WEIGHT2コース)` とも書く。OID に直付けの括弧は名前。"""
    cat = json.loads(json.dumps(CATALOG))
    cat["items"].append({"form_oid": "FA", "item_oid": "WEIGHT2", "group_oid": "GA", "group_name": ""})
    g = ccg.Grounding(ccg.Vocab.from_catalog(cat), ccg.SourceStore.from_dict("st99", DOCS))
    vs = g.check_answer("`A_ONE`(A群 WEIGHT2コース) で非表示 [Source: st99__FA__WEIGHT.md]", ["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ONE"}


def test_a_parenthesis_glued_to_the_path_is_not_part_of_the_path():
    vs = check("体重は各来院で測定する [Source: st99__doc01__s8_1.md(8.1)]")
    assert vs[0].sources == ("st99__doc01__s8_1.md",) and vs[0].klass == ccg.NO_ENTITY


def test_a_screen_sentence_without_its_own_citation_is_not_a_card_claim():
    """attempt 2: 「画面では X に注記がある。」は画面の主張 (N2 の担当)。後ろのカード出典に
    帰属させると X がカードに無いのは当たり前で、赤になる (回扫の純假陽性 2 件)。"""
    ans = ("画面では、`WEIGHTZST` に注記があります。また、`WEIGHT` は任意項目です。 "
           "[Source: st99__FA__WEIGHT.md]")
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"WEIGHT"} and vs[0].klass == ccg.SOURCE_GROUNDED
    assert vs[0].screen_sentences == 1


def test_a_mixed_sentence_mentioning_the_screen_mid_way_is_still_scanned():
    """文頭の画面指称だけ。「カードでは…、画面では…」のような混在文まで捨てると穴になる。"""
    ans = "カードでは A_ZOPE が非表示だが、画面では表示される [Source: st99__FA__WEIGHT.md]"
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ZOPE"} and vs[0].klass == ccg.UNGROUNDED


def test_a_mixed_sentence_without_its_own_citation_is_still_scanned():
    """複審 MAJOR (第二輪): 文頭の錨が load-bearing —— 文中の「画面」で捨てる実装は既知真陽性を
    消す (消融実測)。この用例は出典を自分で持たないので、「自带出典则保留」の閘では守れない。"""
    ans = ("カードでは A_ZOPE が非表示だが、画面では表示される。"
           "なお WEIGHT は任意項目です。 [Source: st99__FA__WEIGHT.md]")
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ZOPE", "WEIGHT"}
    assert vs[0].screen_sentences == 0


def test_a_screen_led_sentence_that_attributes_to_the_card_is_kept():
    """洞 B (複審): 文頭が画面指称でも、文中でカードに帰属している主張はカードの主張。"""
    ans = "画面上の表示条件は、`A_ZOPE` のカードに『常時表示』とある。 [Source: st99__FA__WEIGHT.md]"
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ZOPE"} and vs[0].screen_sentences == 0


def test_a_concessive_clause_does_not_lend_its_negation_backwards():
    vs = check("WEIGHT は A_ZOPE で非表示であるものの、他は含まれません [Source: st99__FA__WEIGHT.md]",
               retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"]: e["status"] for e in vs[0].entities}["A_ZOPE"] == ccg.UNGROUNDED


def test_a_screen_sentence_that_carries_a_card_citation_itself_is_scanned():
    """出典を自分で持つ画面文は、その出典の主張。捨てない。"""
    ans = "画面では A_ZOPE が非表示と読める [Source: st99__FA__WEIGHT.md]"
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ZOPE"}


def test_an_index_citation_cuts_the_unit():
    """『頁索引』は N3 が定めた出典。その前の文は頁索引の担当で、後ろのカード出典の担当ではない。"""
    ans = ("枠は A_ZOPE の順に並ぶ【頁索引】。体重は A_ONE で非表示 [Source: st99__FA__WEIGHT.md]")
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ONE"}


def test_cdisc_sources_are_not_units():
    """`[Source: domains/LB/…]` は標準側の出典。study の闸の対象ではない。"""
    vs = check("LBORRES は原値である [Source: domains/LB/spec.md]")
    assert vs == []


def test_japanese_names_are_not_entities():
    """名前の合法な出所は対応表であってカードではない (規則 `_STUDY_OID_RULES`)。名前を
    実体にすると、規則どおりに書いた答案が全部 UNGROUNDED になる。"""
    vs = check("偽手術活動では非表示 [Source: st99__FA__WEIGHT.md]")
    assert vs[0].klass == ccg.NO_ENTITY


# ── 単元の切り方 ───────────────────────────────────────────────────────
def test_consecutive_study_citations_are_one_attribution_list():
    vs = check("WEIGHT と WEIGHTZST はどちらも A_ZOPE を含む "
               "[Source: st99__FA__WEIGHT.md] [Source: st99__FA__WEIGHTZST.md]")
    assert len(vs) == 1 and vs[0].klass == ccg.SOURCE_GROUNDED
    assert vs[0].sources == ("st99__FA__WEIGHT.md", "st99__FA__WEIGHTZST.md")


def test_a_unit_starts_after_the_previous_citation_of_any_kind():
    """前の出典が画面出典でも、そこで切る。前の主張の OID を巻き込むと、それはこの
    カードには無いのが当たり前なので假陽性になる。"""
    ans = ("画面には A_ZOPE の行が見える『画面目視判読 workflow p.6』。"
           "体重は A_ONE で非表示 [Source: st99__FA__WEIGHT.md]")
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert len(vs) == 1
    assert {e["oid"] for e in vs[0].entities} == {"A_ONE"}


def test_a_trailing_citation_line_takes_the_whole_list_above_it():
    """箇条書きの後に出典が単独行で後置される形。行だけ見ると実体ゼロで素通り、
    塊の先頭に捏造が在れば見逃す。"""
    ans = ("非表示アクティビティ:\n- A_ZOPE\n- A_ONE\n- A_TWO\n\n[Source: st99__FA__WEIGHT.md]")
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert len(vs) == 1 and vs[0].klass == ccg.UNGROUNDED
    assert {e["oid"] for e in vs[0].entities} == {"A_ZOPE", "A_ONE", "A_TWO"}


def test_a_heading_stops_the_upward_extension():
    ans = ("## 前の節\nA_ZOPE の話。\n\n## 本節\n- A_ONE\n\n[Source: st99__FA__WEIGHT.md]")
    vs = check(ans, retrieved=["st99__FA__WEIGHT.md"])
    assert {e["oid"] for e in vs[0].entities} == {"A_ONE"}


# ── run ディレクトリ ────────────────────────────────────────────────────
def _run_json(answer, sources):
    return {"_meta": {"arm": "B", "model_id": "偽モデル", "qid": "T1"},
            "response": {"answer": answer,
                         "sources": [{"source": s, "corpus": "study"} for s in sources]
                         + [{"source": "domains/LB/spec.md", "corpus": "cdisc"}]}}


def test_analyse_dir_feeds_question_and_page_text_as_context(tmp_path):
    run = _run_json("WEIGHT は A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]", ["st99__FA__WEIGHT.md"])
    run["response"]["pdf_pages"] = [{"pdf": "annotated", "page": 3}]
    (tmp_path / "B_x_T1.json").write_text(json.dumps(run), encoding="utf-8")
    g, _ = _gate()
    assert ccg.analyse_dir(tmp_path, g)[0].counts[ccg.UNGROUNDED] == 1
    assert ccg.analyse_dir(tmp_path, g, questions={"T1": "A_ZOPE は?"})[0].counts[ccg.CONTEXT_MISCITED] == 1
    assert ccg.analyse_dir(tmp_path, g, page_text=lambda pdf, p: "A_ZOPE")[0].counts[ccg.CONTEXT_MISCITED] == 1


def test_analyse_dir_takes_retrieved_sources_from_the_run_json(tmp_path):
    (tmp_path / "B_x_T1.json").write_text(json.dumps(_run_json(
        "WEIGHT は A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]",
        ["st99__FA__WEIGHT.md", "st99__FA__WEIGHTZST.md"])), encoding="utf-8")
    (tmp_path / "B_y_T1.json").write_text(json.dumps(_run_json(
        "WEIGHT は A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]",
        ["st99__FA__WEIGHT.md"])), encoding="utf-8")
    g, _ = _gate()
    reps = {r.file: r for r in ccg.analyse_dir(tmp_path, g)}
    assert reps["B_x_T1.json"].counts[ccg.CONTEXT_MISCITED] == 1
    assert reps["B_y_T1.json"].counts[ccg.UNGROUNDED] == 1


def test_answers_that_cite_no_study_source_still_appear_with_zero_units(tmp_path):
    """A 臂 (画面無し) の答案も対象: カード層の捏造は画面通道と無関係。"""
    (tmp_path / "A_x_T1.json").write_text(json.dumps(_run_json("本文のみ", [])), encoding="utf-8")
    g, _ = _gate()
    reps = ccg.analyse_dir(tmp_path, g)
    assert len(reps) == 1 and reps[0].n_units == 0


def test_the_masked_table_never_prints_an_oid():
    vs = check("WEIGHT は A_ZOPE で非表示 [Source: st99__FA__WEIGHT.md]", retrieved=["st99__FA__WEIGHT.md"])
    rep = ccg.AnswerReport(file="f", arm="B", model="m", qid="T1", n_units=1,
                           counts={k: 0 for k in ccg.CLASSES} | {ccg.UNGROUNDED: 1}, verdicts=vs)
    table = ccg.render_table([rep])
    assert "A_ZOPE" not in table and "WEIGHT" not in table and "UNGROUNDED" in table
    assert "A_ZOPE" in ccg.render_table([rep], unmask=True)


def test_source_store_reads_cards_and_docs_from_disk(tmp_path):
    (tmp_path / "cards").mkdir()
    (tmp_path / "docs").mkdir()
    (tmp_path / "cards" / "st99__FA__WEIGHT.md").write_text("A_ONE", encoding="utf-8")
    (tmp_path / "docs" / "st99__doc01__s8_1.md").write_text("節", encoding="utf-8")
    store = ccg.SourceStore("st99", tmp_path)
    assert store.text("st99__FA__WEIGHT.md") == "A_ONE"
    assert store.text("st99__doc01__s8_1.md") == "節"
    assert store.text("st99__FA__GHOST.md") is None
    assert not store.is_study("domains/LB/spec.md") and store.is_study("st99__FA__WEIGHT.md")


def test_source_store_never_follows_an_unsafe_path(tmp_path):
    """発明された出典は何でもあり得る。区切りを含む path は読みに行かず「無い」扱い ——
    例外で回扫を止めもしない (1 つの怪しい出典で 36 份の結果が消える)。"""
    (tmp_path / "cards").mkdir()
    store = ccg.SourceStore("st99", tmp_path)
    assert store.text("st99__../../etc/passwd") is None
    assert store.text("st99__x/y.md") is None


def test_a_section_suffix_after_the_path_is_not_part_of_the_path():
    """実データの出典は節番号を後ろに付ける: `[Source: st99__doc01__s8_1.md 8.1]`。"""
    vs = check("体重は各来院で測定する [Source: st99__doc01__s8_1.md 8.1]")
    assert vs[0].klass == ccg.NO_ENTITY and vs[0].sources == ("st99__doc01__s8_1.md",)
    vs = check("体重は各来院で測定する [Source: st99__doc01__s8_1.md, §8.1]")
    assert vs[0].sources == ("st99__doc01__s8_1.md",)
