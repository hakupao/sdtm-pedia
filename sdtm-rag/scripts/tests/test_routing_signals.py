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
    _CT_CODE_RE,
    _DOMAIN_VAR_RE,
    CDISC_STRUCT_TERMS,
    WIDEN_REASON_BY_CORPUS,
    WIDEN_REASONS,
    RoutingSignals,
    _norm,
    build_signals,
)
from server.study_lookup import StudyLookup, StudyLookupResult


class FakeLookup:
    """S2 契约桩: strong_hit(query) -> bool (G1 后信号层只问这一个)。

    刻意也实现 `resolve` 并在被调用时炸: 信号层若退回 `resolve()`, 弱通道 ②b 就又成了
    widen 依据 —— 而那正是 Task 9 量到的 6 题误触来源。calls 用来证"没被问过"。
    """

    def __init__(self, strong=False):
        self.strong = strong
        self.calls: list[str] = []

    def strong_hit(self, query: str) -> bool:
        self.calls.append(query)
        return self.strong

    def resolve(self, query: str) -> StudyLookupResult:
        raise AssertionError("信号层不许走 resolve() —— 弱通道 ②b 会重新变成 widen 依据")


def _item(form, oid, label):
    return {"form_oid": form, "item_oid": oid, "label": label}


# 合成 catalog (零真实 OID/label, 红线同 test_study_lookup.py)
CATALOG = {"study": "stx", "items": [_item("FRM_A", "GRP_TOX", "偽ラベル甲その一")]}


# ── ① 方向 ──────────────────────────────────────────────────────────

def test_study_signal_fires_on_lookup_hit():
    sl = FakeLookup(strong=True)
    s = RoutingSignals(sl)
    assert s.widen_reason("cdisc", "偽ラベル甲その一はありますか") == "study_sig"


def test_study_signal_silent_when_lookup_misses():
    sl = FakeLookup()
    assert RoutingSignals(sl).widen_reason("cdisc", "一般的な質問") is None
    assert sl.calls == ["一般的な質問"], "问句必须原样交给 S2, 不做任何预处理"


def test_study_routed_question_never_consults_the_lookup():
    """routed=study 时 study 信号毫无意义 (它只会把 study 拓宽成 study)。
    真去问一遍不会让任何断言变红 —— 但那说明方向没写对, 且白烧一次全表扫描。"""
    sl = FakeLookup(strong=True)
    assert RoutingSignals(sl).widen_reason("study", "この項目の入力方法は?") is None
    assert sl.calls == []


def test_cdisc_signal_fires_on_struct_terms():
    s = RoutingSignals(FakeLookup())
    assert s.widen_reason("study", "この項目は SDTM のどの変数にマッピングされますか") == "cdisc_sig"


# ── G1: 强/弱通道 (拿**真** StudyLookup 跑, 桩证不了通道的事) ──────────
#
# 合成 catalog 刻意造出四条通道各自的判别用例 (零真名, 红线同 test_study_lookup.py):
#   ALPHA / BETA 段各 10 张卡 (> _MAX_CARDS_PER_MATCH=8) ⇒ 单 token 命中被 cap 挡掉,
#   只有两段的交集 (唯一那张 ALPHA_BETA 卡) 落在 cap 内 ⇒ ②a 单独可判别;
#   SOLO 段只 1 张卡 ⇒ ②b 单独可判别 (它正是要被排除的弱通道)。

_G1_CATALOG = {"study": "stx", "items": [
    *[_item("FRM_A", f"ALPHA_{i}", f"偽甲ラベル{i}") for i in range(9)],
    *[_item("FRM_A", f"BETA_{i}", f"偽乙ラベル{i}") for i in range(9)],
    _item("FRM_A", "ALPHA_BETA", "偽丙ラベル交差"),
    _item("FRM_B", "SOLO_X", "偽丁ラベル単独"),
    _item("FRM_B", "LONELABEL_Y", "偽戊ラベル全文一致"),
]}
_G1_ALIASES = [{"term": "偽フォーム呼称", "form": "FRM_B"}]


def _g1_signals():
    return RoutingSignals(StudyLookup(_G1_CATALOG, aliases=_G1_ALIASES))


@pytest.mark.parametrize("channel,question", [
    ("① label 全文子串", "偽戊ラベル全文一致はありますか"),
    ("②a 多 token 段交集", "ALPHA と BETA の関係は?"),
    ("③ 别名 form scope", "偽フォーム呼称について教えてください"),
])
def test_strong_channels_fire_the_study_signal(channel, question):
    assert _g1_signals().widen_reason("cdisc", question) == "study_sig", channel


def test_weak_single_token_channel_does_not_fire_the_study_signal():
    """G1 的整条理由: ②b (单个大写 token 撞 OID 段) 不作 widen 依据。

    本研究 EDC 的 OID 段沿用 SDTM 风味命名, 于是一道**纯标准题**里的变量名会精确撞段
    —— Task 9 可见集实测 6 道纯标准题因此被误拓宽, 每题 −1 exact。
    """
    lk = StudyLookup(_G1_CATALOG, aliases=_G1_ALIASES)
    q = "SOLO はどの変数に対応しますか"
    # 非空断言先钉住"这条用例不是空跑": ②b 确实命中了 (旧口径会 fire), 只是不再算依据
    assert lk.resolve(q).cards, "用例失效: ②b 根本没命中, 这条测试证不了收紧"
    assert lk.strong_hit(q) is False
    assert RoutingSignals(lk).widen_reason("cdisc", q) is None


def test_strong_channel_still_fires_when_the_weak_one_also_hits():
    """收紧不是"有弱通道就一票否决": 强弱同时命中时照常 fire。
    写成 `not weak` 的实现会在这里露馅, 而只测纯强通道的用例看不见。"""
    lk = StudyLookup(_G1_CATALOG, aliases=_G1_ALIASES)
    q = "偽戊ラベル全文一致 と SOLO について"
    assert lk.resolve(q).cards
    assert RoutingSignals(lk).widen_reason("cdisc", q) == "study_sig"


# 方向表四格全钉 (修复环 1 I-1)。对角线 (判定 ← 对侧信号) 才拓宽; 反对角线 (判定 ←
# 同侧信号) 必须沉默 —— 同侧信号对每道 router 判对的单库题都成立, 认它等于把 auto 档
# 整体推成 both, 而这条错法在只测"该 fire 的格"时全绿。
_STUDY_HIT = True     # FakeLookup.strong_hit 的返回
_CDISC_Q = "SDTM のどの変数ですか"        # 只有 cdisc 信号
_PLAIN_Q = "この項目の入力方法は?"          # 两侧信号都没有 (lookup 桩空)


@pytest.mark.parametrize("routed,strong,question,expected", [
    ("cdisc", _STUDY_HIT, _PLAIN_Q, "study_sig"),   # 对角: cdisc 判定 + study 信号 → 拓宽
    ("study", False,      _CDISC_Q, "cdisc_sig"),   # 对角: study 判定 + cdisc 信号 → 拓宽
    ("cdisc", False,      _CDISC_Q, None),          # 反对角: cdisc 判定 + cdisc 信号 → 沉默
    ("study", _STUDY_HIT, _PLAIN_Q, None),          # 反对角: study 判定 + study 信号 → 沉默
])
def test_direction_table_all_four_cells(routed, strong, question, expected):
    s = RoutingSignals(FakeLookup(strong=strong))
    assert s.widen_reason(routed, question) == expected


def test_direction_table_matches_the_contract_map():
    """信号层的实际方向必须与 `WIDEN_REASON_BY_CORPUS` (decide_corpus 用它校验) 一致。
    两处各写各的, 症状是信号层每次 fire 都被判成 wrong_direction 而整层静默失效。"""
    s = RoutingSignals(FakeLookup(strong=_STUDY_HIT))
    assert s.widen_reason("cdisc", _PLAIN_Q) == WIDEN_REASON_BY_CORPUS["cdisc"]
    assert RoutingSignals(FakeLookup()).widen_reason("study", _CDISC_Q) == \
        WIDEN_REASON_BY_CORPUS["study"]


def test_contract_map_and_whitelist_are_one_source():
    """白名单加了新理由却没进方向表 (或反过来), 新理由会被 decide_corpus 一律拒收。"""
    assert set(WIDEN_REASON_BY_CORPUS) == {"cdisc", "study"}
    assert set(WIDEN_REASON_BY_CORPUS.values()) == set(WIDEN_REASONS)
    assert len(WIDEN_REASON_BY_CORPUS) == len(WIDEN_REASONS)   # 两个判定不许共用一个理由


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


@pytest.mark.parametrize("q", ["Controlled Terminology の話", "Sdtm ではどうなりますか"])
def test_cdisc_signal_is_case_insensitive_on_terms(q):
    """词表比对走 `_norm` (NFKC + **小写**)。这两条问句里没有 4 位以上连续大写, 变量正则
    兜不住 —— 少了 lower 这一步就整条不 fire。用 "SDTM のどの変数" 那类问句量不出本步:
    它即使不 lower 也会被变量正则命中, 于是 lower 写没写都全绿 (修复环 1 M-2)。"""
    assert RoutingSignals(FakeLookup()).widen_reason("study", q) == "cdisc_sig"


@pytest.mark.parametrize("q", [
    "この値は 12345 ですか",      # 纯数字不是 CT 码
    "CRF の話です",               # 3 位大写 < 阈值
    "この項目は必須ですか",         # 无任何拉丁形态
])
def test_cdisc_signal_stays_silent_on_non_standard_shapes(q):
    assert RoutingSignals(FakeLookup()).widen_reason("study", q) is None


# ── ①' 阴性对照: 标定件的全部价值在「不该 fire 的时候不 fire」 ────────────
#
# Task 9 的标定判据恰恰是**别多触** (起点版 `[A-Z]{4,8}` 在可见集上误触 6 题, 每触
# −1 exact, 模拟 legacy 173 < 阈值 178)。上面那些用例只钉住「该 fire 时会 fire」——
# 把位数放宽或把两侧边界拆掉, 阳性侧一条都不会红 (抽检 B finding F-01)。
# 下面按**冻结形态的每一条边界**各配一格阴性对照。

@pytest.mark.parametrize("q,boundary", [
    ("この項目は C1234 ですか", "位数下界: 4 位不是 CT 码"),
    ("この項目は C1234567 ですか", "位数上界: 7 位不是 CT 码"),
    ("この項目は ZC12345 ですか", "左边界: 码形态不许从更长 ASCII 串里被切出"),
    ("この項目は C12345Z ですか", "右边界: 同上, 右侧"),
])
def test_ct_code_shape_stays_silent_outside_the_frozen_bounds(q, boundary):
    assert RoutingSignals(FakeLookup()).widen_reason("study", q) is None, boundary


@pytest.mark.parametrize("q,boundary", [
    ("ZAESEV はどの値ですか", "左边界: 变量名嵌在更长大写串里不算命中"),
    ("AESEVZ はどの値ですか", "右边界: 同上, 右侧"),
])
def test_variable_shape_stays_silent_inside_a_longer_ascii_run(q, boundary):
    """两侧边界写的是 ASCII 负向环视 (不能用 \\b: CJK 侧 \\b 不成立, 见源码注释)。

    拆掉任一侧, 试验缩写 / 系统名这类更长的大写串会开始整段误触 —— 而 Task 9 正是
    因为这类误触才把起点版 `[A-Z]{4,8}` 换成词表锚定的形态。
    """
    assert RoutingSignals(FakeLookup()).widen_reason("study", q) is None, boundary


def test_frozen_lexicon_and_patterns_are_literal():
    """Task 9 标定收敛后**冻结** (源码 docstring: 此后不许再动)。改词表 / 改形态必须同时
    改这条, 从而落到 code review 上 —— 不然放宽一位数字就是一次无人看守的重新标定。"""
    assert CDISC_STRUCT_TERMS == (
        "sdtm", "cdisc", "マッピング", "どの変数", "対応する変数", "どのドメイン",
        "controlled terminology", "提出データ")
    assert _CT_CODE_RE.pattern == r"(?<![A-Za-z0-9_])C\d{5,6}(?![A-Za-z0-9_])"
    assert _DOMAIN_VAR_RE.pattern.startswith("(?<![A-Za-z0-9_])")
    assert _DOMAIN_VAR_RE.pattern.endswith("(?![A-Za-z0-9_])")


@pytest.mark.parametrize("routed", ["both", "auto", "", "cdisc_sig"])
def test_widen_only_never_fires_outside_the_two_single_corpora(routed):
    """widen-only: both 已是最宽; 其余取值是调用方出错, 信号层一律沉默 (绝不换库)。"""
    sl = FakeLookup(strong=True)
    assert RoutingSignals(sl).widen_reason(routed, "SDTM のどの変数ですか") is None
    assert sl.calls == []


def test_every_fired_reason_is_whitelisted():
    hits = [
        RoutingSignals(FakeLookup(strong=True)).widen_reason("cdisc", "偽ラベル"),
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
    s = RoutingSignals(FakeLookup(strong=True))
    assert {s.widen_reason(routed, question) for _ in range(100)} == {expected}


# ── ③ 词表纪律 ──────────────────────────────────────────────────────

def test_terms_contain_no_clinical_concepts():
    """红线闸: 词表只许含标准结构词汇。临床概念词一进来, 信号层就从"结构信号"
    退化成"题面关键词命中", 那正是 U3 §6.1 已经判死的路子。

    黑名单必须覆盖**本域最核心的那类临床词根**: 起初只写了 ("病","癌","検査値","薬",
    "投与量","mg","腫"), 而「有害事象」这类最典型的临床概念一个字根都不沾, 照样进得来
    (抽检 B finding F-01)。下面按本域实际会出现的临床词根补齐。
    """
    banned_roots = (
        # 起初版
        "病", "癌", "検査値", "薬", "投与量", "mg", "腫",
        # 本域最核心的临床概念词根 (F-01 补)
        "有害", "事象", "症状", "疾患", "患者", "被験者", "診断", "治療", "副作用",
        "発現", "重篤", "転帰", "既往", "併用", "妊娠", "死亡", "用量", "服用", "処方",
        "adverse", "event", "disease", "symptom", "patient", "subject", "diagnos",
        "therap", "dose", "drug", "medicat", "concomitant",
    )
    assert not [t for t in CDISC_STRUCT_TERMS for b in banned_roots if b in t]


def test_terms_are_already_in_matching_normal_form():
    """词条与问句同走 `_norm`; 词条自己不是归一形态 = 永不命中的死条目。"""
    assert [t for t in CDISC_STRUCT_TERMS if _norm(t) != t] == []


@pytest.mark.parametrize("raw,normalized", [
    ("SDTM", "sdtm"),
    ("ＳＤＴＭ", "sdtm"),                                   # 全角 → NFKC → 小写
    ("Controlled Terminology", "controlled terminology"),
    ("マッピング", "マッピング"),                            # 已是归一形态: 恒等
])
def test_norm_is_nfkc_plus_lowercase(raw, normalized):
    """上面那条自检闸的**量尺**本身要有锚。

    `_norm` 在生产路径上没有调用点 (`_cdisc_signal` 走内联的 NFKC + `.lower()`), 于是
    删掉这里的 `.lower()` 生产行为一字不变、全量测试全绿, 而自检闸从此接受大写词条 ——
    大写词条正是它存在的理由 (抽检 B finding F-05 / 探针 1b: 两处各自无害, 合起来把
    红线词表的归一化纪律注销掉)。
    """
    assert _norm(raw) == normalized


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


def test_build_signals_actually_loads_the_alias_table_when_present(tmp_path):
    """上一条只证"缺表不抛"; 缺的是"在场时真的被读进来了"。

    `StudyLookup.stats()` 的 docstring 已点名这个坑: 「别名 0 条 = 通道③ 完全没通电」
    与「别名表加载成功」在外部表现一致。而通道③ 是 `strong_hit` 的强通道之一 —— 路径
    不传进去, 它整条静默空转, study 侧信号覆盖面缩水而全部测试照旧全绿 (finding F-06)。
    """
    s = build_signals(_settings(
        tmp_path, aliases="aliases:\n  - term: 偽フォーム呼称\n    form: FRM_A\n"))
    assert s.study_lookup.stats() == "1 items/1 aliases"
    assert s.widen_reason("cdisc", "偽フォーム呼称について教えてください") == "study_sig"


def test_build_signals_reuses_a_given_lookup_without_touching_disk(tmp_path):
    """生产侧必须复用 lifespan 已构造的那一份 S2 —— 再造一份等于把同一份 catalog
    读两遍并各持一份索引, 而两份可以来自不同文件 (路径 override 只改一处时)。"""
    sl = FakeLookup(strong=True)
    s = build_signals(Settings(study_catalog_path=tmp_path / "nope.json"), study_lookup=sl)
    assert s.study_lookup is sl
    assert s.widen_reason("cdisc", "q") == "study_sig"


def test_build_signals_raises_on_missing_catalog_never_returns_none(tmp_path):
    """契约 (Task 7 已写死): eval 侧 build_signals 返回 None ⇒ SystemExit。
    工厂用 None 表达"装不上"会让 --signal-layer on 悄悄跑成 off, 而 meta 仍写着 on。"""
    with pytest.raises(FileNotFoundError) as e:
        build_signals(Settings(study_catalog_path=tmp_path / "nope.json"))
    assert "nope.json" in str(e.value)
