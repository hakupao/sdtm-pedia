"""U6 T8: 双向确定性信号层 (spec §5.1) —— widen-only, 零 LLM, 合成数据 (红线)。

信号层是本单元唯一的修法机构。它只做 单库→both, 所以本文件钉的不是"判得准不准"
(那是 Task 9 可见集标定 + Task 10 全闸的事), 而是三件构造性的事:

① **方向**: routed=cdisc 只问 study 信号, routed=study 只问 cdisc 信号, both 一律不问。
   方向写反不会让任何"命中率"测试变红 —— 它只会把修法变成对症下药的反向噪声。
② **确定性**: 同一问句多次调用同一结果。信号层一旦引入任何非确定性, 三遍纪律
   (`--runs 3` 一致性) 量到的就不再是 router 的方差。
③ **词表纪律**: 零临床概念 (红线同 U3 §6.1 词表), 且词条形态必须与匹配用归一化自洽 ——
   写成 "SDTM" 的词条永远命不中 `_norm` 后的问句, 而词表是 Task 9 标定的**起点**:
   起点里躺着死条目, 标定会把"词表写错了"读成"信号没用"。
"""
from __future__ import annotations

import json

import pytest

from server.config import Settings
from server.routing_signals import (
    CDISC_STRUCT_TERMS,
    WIDEN_REASONS,
    RoutingSignals,
    _norm,
    build_signals,
)
from server.study_lookup import StudyLookupResult


class FakeLookup:
    """S2 契约桩: resolve(query) -> StudyLookupResult。calls 用来证"没被问过"。"""

    def __init__(self, cards=(), form_scopes=()):
        self.cards, self.form_scopes = list(cards), list(form_scopes)
        self.calls: list[str] = []

    def resolve(self, query: str) -> StudyLookupResult:
        self.calls.append(query)
        return StudyLookupResult(cards=list(self.cards), form_scopes=list(self.form_scopes))


def _item(form, oid, label):
    return {"form_oid": form, "item_oid": oid, "label": label}


# 合成 catalog (零真实 OID/label, 红线同 test_study_lookup.py)
CATALOG = {"study": "stx", "items": [_item("FRM_A", "GRP_TOX", "偽ラベル甲その一")]}


# ── ① 方向 ──────────────────────────────────────────────────────────

def test_study_signal_fires_on_lookup_hit():
    sl = FakeLookup(cards=["stx__FRM_A__GRP_TOX.md"])
    s = RoutingSignals(sl)
    assert s.widen_reason("cdisc", "偽ラベル甲その一はありますか") == "study_sig"


def test_study_signal_fires_on_form_scope_only():
    """通道③ (别名→form scope) 不产 cards。只看 cards 会让别名命中整条静默失效。"""
    s = RoutingSignals(FakeLookup(form_scopes=["FRM_A"]))
    assert s.widen_reason("cdisc", "偽フォームの話") == "study_sig"


def test_study_signal_silent_when_lookup_misses():
    sl = FakeLookup()
    assert RoutingSignals(sl).widen_reason("cdisc", "一般的な質問") is None
    assert sl.calls == ["一般的な質問"], "问句必须原样交给 S2, 不做任何预处理"


def test_study_routed_question_never_consults_the_lookup():
    """routed=study 时 study 信号毫无意义 (它只会把 study 拓宽成 study)。
    真去问一遍不会让任何断言变红 —— 但那说明方向没写对, 且白烧一次全表扫描。"""
    sl = FakeLookup(cards=["stx__FRM_A__GRP_TOX.md"])
    assert RoutingSignals(sl).widen_reason("study", "この項目の入力方法は?") is None
    assert sl.calls == []


def test_cdisc_signal_fires_on_struct_terms():
    s = RoutingSignals(FakeLookup())
    assert s.widen_reason("study", "この項目は SDTM のどの変数にマッピングされますか") == "cdisc_sig"


def test_pure_study_question_does_not_fire_cdisc_signal():
    assert RoutingSignals(FakeLookup()).widen_reason("study", "この項目の入力方法は?") is None


@pytest.mark.parametrize("q", [
    "C12345 に対応しますか",          # CT 码
    "C123456 に対応しますか",         # 6 位
    "AESEV はどの値をとりますか",      # 变量形态 (空格分隔)
    "AESEVはどの値をとりますか",       # ← 紧贴假名: \b 在 CJK 边界不成立, 这条是那个坑的锁
    "ＡＥＳＥＶはどの値ですか",         # 全角 (NFKC 归一后才是变量形态)
])
def test_cdisc_signal_fires_on_code_shapes(q):
    assert RoutingSignals(FakeLookup()).widen_reason("study", q) == "cdisc_sig"


@pytest.mark.parametrize("q", [
    "この値は 12345 ですか",      # 纯数字不是 CT 码
    "CRF の話です",               # 3 位大写 < 阈值
    "この項目は必須ですか",         # 无任何拉丁形态
])
def test_cdisc_signal_stays_silent_on_non_standard_shapes(q):
    assert RoutingSignals(FakeLookup()).widen_reason("study", q) is None


@pytest.mark.parametrize("routed", ["both", "auto", "", "cdisc_sig"])
def test_widen_only_never_fires_outside_the_two_single_corpora(routed):
    """widen-only: both 已是最宽; 其余取值是调用方出错, 信号层一律沉默 (绝不换库)。"""
    sl = FakeLookup(cards=["stx__FRM_A__GRP_TOX.md"])
    assert RoutingSignals(sl).widen_reason(routed, "SDTM のどの変数ですか") is None
    assert sl.calls == []


def test_every_fired_reason_is_whitelisted():
    hits = [
        RoutingSignals(FakeLookup(cards=["x.md"])).widen_reason("cdisc", "偽ラベル"),
        RoutingSignals(FakeLookup()).widen_reason("study", "SDTM のどの変数ですか"),
    ]
    assert hits and all(h in WIDEN_REASONS for h in hits)


def test_whitelist_is_frozen_and_ordered():
    assert WIDEN_REASONS == ("study_sig", "cdisc_sig")


# ── ② 确定性 ────────────────────────────────────────────────────────

@pytest.mark.parametrize("routed,question,expected", [
    ("cdisc", "偽ラベル甲その一はありますか", "study_sig"),
    ("study", "SDTM のどの変数にマッピングされますか", "cdisc_sig"),
    ("study", "この項目の入力方法は?", None),
])
def test_deterministic(routed, question, expected):
    s = RoutingSignals(FakeLookup(cards=["x.md"]))
    assert {s.widen_reason(routed, question) for _ in range(100)} == {expected}


# ── ③ 词表纪律 ──────────────────────────────────────────────────────

def test_terms_contain_no_clinical_concepts():
    """红线闸: 词表只许含标准结构词汇。临床概念词一进来, 信号层就从"结构信号"
    退化成"题面关键词命中", 那正是 U3 §6.1 已经判死的路子。"""
    banned_roots = ("病", "癌", "検査値", "薬", "投与量", "mg", "腫")
    assert not [t for t in CDISC_STRUCT_TERMS for b in banned_roots if b in t]


def test_terms_are_already_in_matching_normal_form():
    """词条与问句同走 `_norm`; 词条自己不是归一形态 = 永不命中的死条目。"""
    assert [t for t in CDISC_STRUCT_TERMS if _norm(t) != t] == []


def test_terms_have_no_blanks_or_duplicates():
    assert all(t.strip() for t in CDISC_STRUCT_TERMS)
    assert len(set(CDISC_STRUCT_TERMS)) == len(CDISC_STRUCT_TERMS)


# ── build_signals: 生产与 eval 同源工厂 ─────────────────────────────

def _settings(tmp_path, catalog=CATALOG, aliases: str | None = None):
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps(catalog), encoding="utf-8")
    ali = tmp_path / "aliases.yml"
    if aliases is not None:
        ali.write_text(aliases, encoding="utf-8")
    return Settings(study_catalog_path=cat, study_aliases_path=ali)


def test_build_signals_loads_from_settings_paths(tmp_path):
    s = build_signals(_settings(tmp_path))
    assert isinstance(s, RoutingSignals)
    assert s.widen_reason("cdisc", "偽ラベル甲その一はありますか") == "study_sig"


def test_build_signals_tolerates_a_missing_alias_table(tmp_path):
    """别名表缺失是 S2 刻意的优雅降级 (通道③ 空转); 工厂不得把它升级成硬失败。"""
    assert build_signals(_settings(tmp_path)) is not None


def test_build_signals_reuses_a_given_lookup_without_touching_disk(tmp_path):
    """生产侧必须复用 lifespan 已构造的那一份 S2 —— 再造一份等于把同一份 catalog
    读两遍并各持一份索引, 而两份可以来自不同文件 (路径 override 只改一处时)。"""
    sl = FakeLookup(cards=["x.md"])
    s = build_signals(Settings(study_catalog_path=tmp_path / "nope.json"), study_lookup=sl)
    assert s.study_lookup is sl
    assert s.widen_reason("cdisc", "q") == "study_sig"


def test_build_signals_raises_on_missing_catalog_never_returns_none(tmp_path):
    """契约 (Task 7 已写死): eval 侧 build_signals 返回 None ⇒ SystemExit。
    工厂用 None 表达"装不上"会让 --signal-layer on 悄悄跑成 off, 而 meta 仍写着 on。"""
    with pytest.raises(FileNotFoundError) as e:
        build_signals(Settings(study_catalog_path=tmp_path / "nope.json"))
    assert "nope.json" in str(e.value)
