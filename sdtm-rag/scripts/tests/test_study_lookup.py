"""S2 StudyLookup 单元测试 — 合成 catalog, 零真实 OID/label (红线)."""
import pytest

from server.study_lookup import StudyLookup, StudyLookupResult


def _item(form, oid, label):
    return {"form_oid": form, "item_oid": oid, "label": label}


CATALOG = {
    "study": "stx",
    "items": [
        # 家族甲: 同 form + OID 首段 GRP → 3 卡 (label 只有其一可被题面引用)
        _item("FRM_A", "GRP_TOX", "偽末梢症状グレード"),
        _item("FRM_A", "GRP_REL", "治療との関係"),
        _item("FRM_A", "GRP_SER", "重い/重くない"),
        # 家族乙 (干扰): 同 form 不同首段, 不得被家族甲扩张带出
        _item("FRM_A", "OTH_TOX", "別症状グレード"),
        # 近义双卡: ABC_DEF_R vs XABC_DEF_R (label 相同; 段 ABC 只属前者)
        _item("FRM_B", "ABC_DEF_R", "実施の理由"),
        _item("FRM_B", "XABC_DEF_R", "実施の理由"),
        # 段家族: token QST 命中 QST_Q1/Q2
        _item("FRM_C", "QST_Q1", "1. 偽質問その一"),
        _item("FRM_C", "QST_Q2", "2. 偽質問その二"),
        # 短 label (<4 字, 不入 label 索引)
        _item("FRM_C", "SHT_X", "熱"),
    ],
}


def test_label_substring_hits_card_and_expands_family():
    lk = StudyLookup(CATALOG)
    res = lk.resolve("偽末梢症状グレードと治療との関係は別々の項目ですか?")
    assert "stx__FRM_A__GRP_TOX.md" in res.cards
    assert "stx__FRM_A__GRP_REL.md" in res.cards      # 家族扩张
    assert "stx__FRM_A__GRP_SER.md" in res.cards
    assert "stx__FRM_A__OTH_TOX.md" not in res.cards  # 别的首段不带出
    assert res.form_scopes == []                      # 通道③前恒空


def test_label_shorter_than_4_never_fires():
    lk = StudyLookup(CATALOG)
    assert lk.resolve("熱がありますか").cards == []


def test_ambiguous_label_over_cap_is_skipped():
    # 同 label 9 卡 (各自独立首段家族, 扩张后仍 9) > cap 时该 label 不 fire (保守)
    big = {"study": "stx", "items": [
        _item("FRM_D", f"FAM{i}_R", "同名ラベルです") for i in range(9)
    ]}
    lk = StudyLookup(big)
    assert lk.resolve("同名ラベルですはどこ?").cards == []


def test_no_match_returns_empty_result():
    lk = StudyLookup(CATALOG)
    res = lk.resolve("全然関係ない質問")
    assert res == StudyLookupResult(cards=[], form_scopes=[])


def test_nfkc_and_whitespace_normalized_label_match():
    lk = StudyLookup(CATALOG)
    # 全角/空白差异不阻断匹配
    res = lk.resolve("偽末梢症状　グレード について")
    assert "stx__FRM_A__GRP_TOX.md" in res.cards


def test_latin_token_matches_oid_segment_family():
    lk = StudyLookup(CATALOG)
    # token 紧贴日文 (QSTは) 无空白分隔 — 真实题面形态
    res = lk.resolve("QSTは何問の設問で構成されていますか?")
    assert "stx__FRM_C__QST_Q1.md" in res.cards
    assert "stx__FRM_C__QST_Q2.md" in res.cards


def test_token_is_segment_exact_not_substring():
    # ABC 匹配段 ABC (ABC_DEF_R), 不匹配段 XABC (XABC_DEF_R) — 近义双卡判别
    lk = StudyLookup(CATALOG)
    res = lk.resolve("ABCを選択した場合、その理由はどの項目?")
    assert "stx__FRM_B__ABC_DEF_R.md" in res.cards
    assert "stx__FRM_B__XABC_DEF_R.md" not in res.cards


def test_token_hitting_oversized_set_does_not_fire():
    big = {"study": "stx", "items": [
        _item("FRM_E", f"TOK_F{i}", f"別々のラベル{i}号") for i in range(9)
    ]}
    lk = StudyLookup(big)
    assert lk.resolve("TOK はどこですか").cards == []


def test_short_or_lowercase_tokens_ignored():
    # 段 GRADE 真实存在, 小写 grade 仍不得触发 (否则断言空转); Q1 太短同样不触发
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_H", "GRADE_A", "甲のラベル"),
        _item("FRM_H", "QNO_B", "乙のラベル"),
    ]})
    # 2 位大写 (段 R 等) 与小写/混写词不触发
    assert lk.resolve("Q1 の grade を教えて").cards == []
    # 同一 fixture 上大写 3 位 token 确实 fire —— 证明上面的空结果不是机制没接
    assert lk.resolve("QNO を教えて").cards == ["stx__FRM_H__QNO_B.md"]


def test_total_cards_capped_at_10():
    # cap=8 以内的两个 token 各 fire 也不超过总 cap —— 用两个 6 卡段验证
    items = ([_item("FRM_G", f"BBB_K{i}", f"甲{i}のラベル") for i in range(6)]
             + [_item("FRM_G", f"CCC_K{i}", f"乙{i}のラベル") for i in range(6)])
    lk = StudyLookup({"study": "stx", "items": items})
    res = lk.resolve("BBB と CCC の項目を全部")
    assert len(res.cards) == 10
