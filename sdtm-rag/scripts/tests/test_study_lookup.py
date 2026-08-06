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


def test_label_shorter_than_4_never_fires():
    lk = StudyLookup(CATALOG)
    assert lk.resolve("熱がありますか").cards == []


def test_ambiguous_label_over_cap_is_skipped():
    # 同 label 两卡 + 各自家族合计 > cap 时该 label 不 fire (保守)
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
