"""S2 StudyLookup 单元测试 — 合成 catalog, 零真实 OID/label (红线)."""
import json
import re
from types import SimpleNamespace

import pytest

from server import rag as rag_mod
from server.study_lookup import (
    _LATIN_TOKEN_RE,
    _MAX_CARDS_TOTAL,
    _MIN_SEG_LEN,
    StudyLookup,
    StudyLookupResult,
)


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


def test_family_does_not_cross_form_with_shared_first_segment():
    # 家族键的另一半: 上面那条锁的是"同 form 不同首段", 这条锁"同首段不同 form"。
    # 键去掉 form_oid 全测试仍绿 —— 而真实数据里首段跨 form 复用是常态, 家族会静默变大。
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_U", "SEG_A1", "共通首段の甲ラベル"),
        _item("FRM_U", "SEG_A2", "共通首段の乙ラベル"),   # 同 form 同首段 = 同家族
        _item("FRM_V", "SEG_B1", "別フォームの丙ラベル"),  # 同首段だが別 form = 別家族
    ]})
    res = lk.resolve("共通首段の甲ラベルはどの項目?")
    assert res.cards == ["stx__FRM_U__SEG_A1.md", "stx__FRM_U__SEG_A2.md"]
    assert "stx__FRM_V__SEG_B1.md" not in res.cards


def test_label_shorter_than_4_never_fires():
    lk = StudyLookup(CATALOG)
    assert lk.resolve("熱がありますか").cards == []


def test_label_length_bound_is_exactly_four():
    # `_MIN_LABEL_LEN` 双向锁: 抬到 5/6 会静默废掉一大片短 label 的命中面 (真实数据 22.5%
    # 的 label 归一化后只有 4-5 字), 降到 3 会放进判别力不足的短 label。上面那条 1 字用例
    # 只咬得住"完全去掉过滤", 两个方向的挪动都咬不住。
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_T", "TFR_A", "偽甲乙丙"),   # 归一化後ちょうど 4 字 → 必ず fire
        _item("FRM_T", "TTR_B", "偽甲乙"),     # 3 字 → 索引に入ってはならない
    ]})
    # 4 字ちょうどで fire (下界を 5 以上に上げると空になる);
    # 同時に 3 字 label が索引入りしていれば此処にも混入する (下界を 3 に下げると赤)
    assert lk.resolve("偽甲乙丙はどの項目?").cards == ["stx__FRM_T__TFR_A.md"]
    # 3 字 label だけを含む問句では何も fire しない
    assert lk.resolve("偽甲乙はどの項目?").cards == []


def test_min_seg_len_matches_token_regex_lower_bound():
    # `_MIN_SEG_LEN` と正則の下界は同一の意味を二箇所の定数で表している:
    # 正則 `[A-Z][A-Z0-9]{2,}` = 3 位下界。片方だけ動かすと索引と抽出がズレ、
    # 症状は「その長さの token が黙って引けなくなる」だけで何処も赤くならない。
    # `_STUDY_MAX_CARDS == _MAX_CARDS_TOTAL` の同値錠と同じ手当て。
    m = re.search(r"\{(\d+),\}", _LATIN_TOKEN_RE.pattern)
    assert m, "token 正則の下界の書き方が変わった — この錠は失効している"
    assert int(m.group(1)) + 1 == _MIN_SEG_LEN


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


def test_whitespace_normalized_label_match():
    lk = StudyLookup(CATALOG)
    # 空白差异不阻断匹配 (label 側は連続, 問句側は全角スペースで割れている)
    res = lk.resolve("偽末梢症状　グレード について")
    assert "stx__FRM_A__GRP_TOX.md" in res.cards


def test_nfkc_normalized_label_match():
    # 空白除去だけでは届かない差 = NFKC の受け持ち分: 半角カナ ⇄ 全角カナ、
    # 全角ラテン ⇄ 半角ラテン。catalog 側と問句側で書き分けが違うのは実データの常態。
    # `_norm` から NFKC を外すと索引キーと問句が別物になり、このテストだけが赤くなる。
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_W", "WID_A", "ﾊﾞｲﾀﾙ測定ABC"),   # 半角カナ + 半角ラテン
    ]})
    assert lk.resolve("バイタル測定ＡＢＣはどこ?").cards == ["stx__FRM_W__WID_A.md"]


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


def test_token_hits_survive_when_labels_would_fill_the_cap():
    # 通道① 独占 10 位时, 通道② 的精确段命中不得被挤掉 (截断发生在本模块, 注入层无从补救)
    items = ([_item("FRM_Z", f"L{i}_A", f"個別ラベル{i}号") for i in range(10)]
             + [_item("FRM_Z", "TGT_A", "無関係な別ラベル")])
    lk = StudyLookup({"study": "stx", "items": items})
    res = lk.resolve("".join(f"個別ラベル{i}号" for i in range(10)) + " TGT")
    assert res.cards[0] == "stx__FRM_Z__TGT_A.md"   # 精确信号先入队
    assert len(res.cards) == _MAX_CARDS_TOTAL       # 总 cap 仍生效, 被挤掉的是 label 卡


@pytest.mark.parametrize("text,expected", [
    ("QSTは何問の設問",       ["QST"]),   # 紧贴 CJK 必须取得出 (\b 在此不成立)
    ("XABCの理由は?",         ["XABC"]),  # 取整段, 不得从中切出 ABC
    ("eCRF の入力について",    []),        # 混写: 左邻 ASCII 字母阻断 (lookbehind)
    ("xABCを選択",            []),        # 同上, 小写前缀不得剥离
    ("ABC_DEF_R はどの項目",   []),        # 下划线算阻断邻居 → 完整 OID 整串取不出 (已知, m2)
    ("grade を教えて",        []),        # 纯小写不取
    ("Q1 の値",              []),        # 2 位不足 3 位下界
    ("BBB と CCC の項目",     ["BBB", "CCC"]),  # 空白分隔多 token
])
def test_latin_token_regex_boundary_semantics(text, expected):
    assert _LATIN_TOKEN_RE.findall(text) == expected


# ---- 通道②a 多 token 交集 (合取) ----------------------------------------------

def _straddle_catalog():
    """两个段各自超 cap, 但同属两段的卡只有少数 —— 单 token 全被挡, 交集才够窄。"""
    return {"study": "stx", "items":
            [_item("FRM_K", f"TTT_UUU_A{i}", f"両段の甲{i}") for i in range(4)]
            + [_item("FRM_K", f"TTT_VVV_B{i}", f"片段の乙{i}") for i in range(8)]
            + [_item("FRM_K", f"WWW_UUU_C{i}", f"片段の丙{i}") for i in range(6)]}


def test_intersection_fires_when_both_single_token_sets_are_over_cap():
    # 单 token: TTT 12 卡 / UUU 10 卡, 双双超 cap 被挡; 交集 4 卡落回 cap 内 → 只有交集入队
    lk = StudyLookup(_straddle_catalog())
    res = lk.resolve("TTT と UUU について")
    assert res.cards == [f"stx__FRM_K__TTT_UUU_A{i}.md" for i in range(4)]


def test_intersection_is_enqueued_before_single_token_hits():
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_I", "PPP_RRR_B", "交差の乙"),   # 仅 PPP; 故意排在交集卡之前
        _item("FRM_I", "PPP_QQQ_A", "交差の甲"),   # 两段都占
        _item("FRM_I", "SSS_QQQ_C", "交差の丙"),   # 仅 QQQ
    ]})
    res = lk.resolve("PPP と QQQ の項目")
    # 两个单 token 集合都在 cap 内也会 fire, 但交集卡必须排在最前 (合取判别力最强);
    # 若交集不先入队, 首位会是 catalog 序更靠前的 PPP_RRR_B
    assert res.cards == ["stx__FRM_I__PPP_QQQ_A.md",
                         "stx__FRM_I__PPP_RRR_B.md",
                         "stx__FRM_I__SSS_QQQ_C.md"]


def test_empty_intersection_does_not_fire():
    # 两段无公共卡 → 交集为空; 单 token 各 9 卡也超 cap → 整体不 fire
    lk = StudyLookup({"study": "stx", "items":
                      [_item("FRM_M", f"DDD_M{i}", f"独立の甲{i}") for i in range(9)]
                      + [_item("FRM_M", f"EEE_N{i}", f"独立の乙{i}") for i in range(9)]})
    assert lk.resolve("DDD と EEE について").cards == []


def test_oversized_intersection_does_not_fire():
    # 交集恒 ⊆ 单集合, 故交集超 cap 时单 token 必然也超 cap —— 三条路径全被挡
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_N", f"FFF_GGG_K{i}", f"全重なりの甲{i}") for i in range(9)
    ]})
    assert lk.resolve("FFF と GGG について").cards == []


def test_three_token_intersection_requires_all_three_segments():
    # 三段各 9 卡全超 cap; 只有同时占三段的那一张能通过交集
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_L", "AAA_BBB_CCC_X", "三段の甲"),
        _item("FRM_L", "AAA_BBB_DDD_Y", "二段の乙"),   # 缺 CCC, 两两交集会带出它
    ] + [_item("FRM_L", f"AAA_FIL{i}", f"埋め甲{i}") for i in range(7)]
      + [_item("FRM_L", f"BBB_GIL{i}", f"埋め乙{i}") for i in range(7)]
      + [_item("FRM_L", f"CCC_HIL{i}", f"埋め丙{i}") for i in range(8)]})
    res = lk.resolve("AAA と BBB と CCC の項目")
    assert res.cards == ["stx__FRM_L__AAA_BBB_CCC_X.md"]


def test_single_token_query_leaves_segment_channel_unchanged():
    # 不足 2 个 token 时不走交集路径 (单 token 的"交集"等于它自己, 行为上不可区分, 此处为定性锁)
    lk = StudyLookup({"study": "stx", "items": [
        _item("FRM_O", "HHH_R1", "単段の甲"),
        _item("FRM_O", "HHH_R2", "単段の乙"),
    ]})
    assert lk.resolve("HHH について").cards == ["stx__FRM_O__HHH_R1.md",
                                                "stx__FRM_O__HHH_R2.md"]


def test_token_absent_from_index_vetoes_the_whole_intersection():
    # 已知后果 (合取语义的直接推论): 题面多一个索引里没有的大写词, 交集即空, 通道整体让路。
    # 只会少 fire 不会误 fire —— 单 token 路径不受影响, 保守回落纯检索。
    lk = StudyLookup(_straddle_catalog())
    assert lk.resolve("TTT と UUU について").cards != []        # 对照: 无生词时 fire
    assert lk.resolve("TTT と UUU と ZZZ について").cards == []


def test_alias_term_in_query_yields_form_scope():
    lk = StudyLookup(CATALOG, aliases=[{"term": "偽光線", "form": "FRM_A"}])
    res = lk.resolve("偽光線に関する項目はどれですか?")
    assert res.form_scopes == ["FRM_A"]


def test_alias_term_normalized_like_query():
    # 别名词与问句同走 NFKC+去空白: 全角/空格差异不得阻断 (term 侧漏 _norm 会挂)
    lk = StudyLookup(CATALOG, aliases=[{"term": "偽光線 検査", "form": "FRM_A"}])
    assert lk.resolve("偽光線検査はどこ?").form_scopes == ["FRM_A"]
    # raw 保留作者在 yml 写的字面 (归一化形态排查时对不上账)
    assert lk.aliases == [{"term": "偽光線検査", "raw": "偽光線 検査", "form": "FRM_A"}]


@pytest.mark.parametrize("bad_term", ["", "　 　"])   # 空串 / 纯全角+半角空白
def test_alias_empty_term_rejected(bad_term):
    # 空 term 会子串命中所有问句 → 该 form 无差别 scope 进来, 是唯一的静默错误面
    with pytest.raises(ValueError, match="FRM_A"):
        StudyLookup(CATALOG, aliases=[{"term": bad_term, "form": "FRM_A"}])


def test_same_form_synonyms_yield_one_scope():
    # 手写别名表常见形态: 同一 form 挂多个同义词; 同时命中不得产出重复 scope
    lk = StudyLookup(CATALOG, aliases=[
        {"term": "偽光線", "form": "FRM_A"},
        {"term": "偽検査", "form": "FRM_A"},
    ])
    assert lk.resolve("偽光線と偽検査について").form_scopes == ["FRM_A"]


def test_alias_unknown_form_fails_loud():
    with pytest.raises(ValueError, match="NOFORM"):
        StudyLookup(CATALOG, aliases=[{"term": "偽語", "form": "NOFORM"}])


def test_from_paths_missing_aliases_file_is_empty(tmp_path):
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps(CATALOG), encoding="utf-8")
    lk = StudyLookup.from_paths(cat, tmp_path / "no_such.yml")
    assert lk.aliases == []


def test_from_paths_missing_catalog_fails_loud(tmp_path):
    with pytest.raises(FileNotFoundError):
        StudyLookup.from_paths(tmp_path / "no_catalog.json", None)


def test_from_paths_loads_aliases(tmp_path):
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps(CATALOG), encoding="utf-8")
    al = tmp_path / "lookup_aliases.yml"
    al.write_text("aliases:\n  - term: 偽光線\n    form: FRM_A\n", encoding="utf-8")
    lk = StudyLookup.from_paths(cat, al)
    assert lk.resolve("偽光線の項目").form_scopes == ["FRM_A"]


# ---- stats(): 别名 0 条 = 通道③ 没通电, 只有条数能在外部看出来 ----

def test_stats_reports_both_counts():
    lk = StudyLookup(CATALOG, aliases=[{"term": "偽光線", "form": "FRM_A"}])
    assert lk.stats() == f"{len(CATALOG['items'])} items/1 aliases"


def test_stats_shows_zero_aliases_when_alias_file_missing(tmp_path):
    """今天的真实形态: catalog 加载成功但别名表还不存在 —— 必须显示为 0, 不能被含糊过去."""
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps(CATALOG), encoding="utf-8")
    lk = StudyLookup.from_paths(cat, tmp_path / "no_such.yml")
    assert lk.stats() == f"{len(CATALOG['items'])} items/0 aliases"


def test_stats_item_count_tracks_catalog_size():
    """条数必须来自 catalog 真实规模, 不是写死的常量."""
    small = {"study": "stx", "items": [_item("FRM_A", "A_1", "偽ラベル一")]}
    assert StudyLookup(small).stats() == "1 items/0 aliases"
    assert StudyLookup(CATALOG).n_items == len(CATALOG["items"])


# ---- RAGEngine 注入层 (Task 4) -----------------------------------------------
# RAGEngine.__new__ + monkeypatch _search: 不建 Chroma / 不发 embedding, 只锁注入契约。


class _StubLookup:
    def __init__(self, cards=(), scopes=()):
        self._res = StudyLookupResult(cards=list(cards), form_scopes=list(scopes))

    def resolve(self, query):
        return self._res


def _chunk(cid, source):
    return SimpleNamespace(chunk_id=cid, source=source, via_lookup=False)


def _engine(lookup, search_log):
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._study_lookup = lookup
    eng._structured_lookup = None

    def fake_search(query, n, where=None, query_embedding=None):
        search_log.append((n, where))
        if where and "source" in where:
            return [_chunk(f"lk:{where['source']}", where["source"])]
        if where and "form_oid" in where:
            return [_chunk(f"sc:{where['form_oid']}:{i}", f"x{i}.md") for i in range(n)]
        return []

    eng._search = fake_search
    return eng


def test_apply_study_lookup_prepends_cards_and_scopes_dedup_to_k():
    log = []
    eng = _engine(_StubLookup(cards=["stx__F__A.md"], scopes=["FRM_Z"]), log)
    cosine = [_chunk("lk:stx__F__A.md", "stx__F__A.md")] + [
        _chunk(f"c{i}", f"c{i}.md") for i in range(14)
    ]
    out = eng._apply_study_lookup("q", cosine, 15, query_embedding=None)
    assert out[0].chunk_id == "lk:stx__F__A.md" and out[0].via_lookup
    assert [c.chunk_id for c in out[1:4]] == ["sc:FRM_Z:0", "sc:FRM_Z:1", "sc:FRM_Z:2"]
    assert len(out) == 15
    assert len([c for c in out if c.chunk_id == "lk:stx__F__A.md"]) == 1  # 去重
    assert (1, {"source": "stx__F__A.md"}) in log
    assert (3, {"form_oid": "FRM_Z"}) in log


def test_apply_study_lookup_filters_source_by_bare_filename():
    # study collection 的 chunk metadata 里 source 是裸卡文件名 (CDISC 侧才是绝对路径)。
    # 若误用 S1 的 _lookup_chunks_for_file (kb_root 拼绝对路径), filter 恒不命中 → 静默空注入。
    log = []
    eng = _engine(_StubLookup(cards=["stx__F__A.md"]), log)
    eng._apply_study_lookup("q", [], 15, query_embedding=None)
    assert log == [(1, {"source": "stx__F__A.md"})]


def test_apply_study_lookup_injects_scope_when_no_cards():
    # 通道③ 的主用例: 别名词与 gold 卡词面零重合 (这正是通道③ 存在的理由), 所以别名命中的
    # 问句上通道①② 按构造不 fire, cards 常为空。scopes-only 必须照样注入, 否则提前返回的
    # 判据写成 `if not res.cards:` 也咬不住 —— 而这条正是 Task 6 验收要靠的路径。
    log = []
    eng = _engine(_StubLookup(scopes=["FRM_Z"]), log)
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_study_lookup("q", cosine, 15, query_embedding=None)
    assert [c.chunk_id for c in out[:3]] == ["sc:FRM_Z:0", "sc:FRM_Z:1", "sc:FRM_Z:2"]
    assert all(c.via_lookup for c in out[:3])
    assert log == [(3, {"form_oid": "FRM_Z"})]


def test_apply_study_lookup_caps_cards_at_max():
    # resolve 已按 _MAX_CARDS_TOTAL 截断; 注入层再截一次是双保险 (stub 故意越界)
    log = []
    cards = [f"stx__F__C{i}.md" for i in range(14)]
    eng = _engine(_StubLookup(cards=cards), log)
    out = eng._apply_study_lookup("q", [], 15, query_embedding=None)
    assert len(log) == rag_mod.RAGEngine._STUDY_MAX_CARDS
    assert len(out) == rag_mod.RAGEngine._STUDY_MAX_CARDS


def test_engine_card_cap_matches_lookup_cap():
    # "同值双保险" 靠注释维系不住: 上面那条用 _STUDY_MAX_CARDS 自指, 改常量咬不住。
    # 若 _MAX_CARDS_TOTAL 调到 12 而注入层没跟, 注入会静默停在 10。
    assert rag_mod.RAGEngine._STUDY_MAX_CARDS == _MAX_CARDS_TOTAL


def test_apply_study_lookup_noop_when_resolve_empty():
    log = []
    eng = _engine(_StubLookup(), log)
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_study_lookup("q", cosine, 15, query_embedding=None)
    assert [c.chunk_id for c in out] == [f"c{i}" for i in range(15)]
    assert log == []  # 不 fire 就零额外检索


def test_apply_study_lookup_falls_back_when_lookup_chunks_empty():
    # resolve fire 了但目标卡在库里没有 chunk (catalog 与 collection 不同步) → 回落纯 cosine
    log = []
    eng = _engine(_StubLookup(cards=["gone.md"]), log)
    eng._search = lambda q, n, where=None, query_embedding=None: (log.append((n, where)) or [])
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_study_lookup("q", cosine, 15, query_embedding=None)
    assert [c.chunk_id for c in out] == [f"c{i}" for i in range(15)]
    assert log == [(1, {"source": "gone.md"})]


def test_ctor_rejects_both_lookups(tmp_path):
    with pytest.raises(ValueError, match="study_lookup"):
        rag_mod.RAGEngine(
            chroma_dir=tmp_path, kb_root=tmp_path, collection_name="x",
            embedding_model="m", structured_lookup_enabled=True,
            study_lookup=_StubLookup(),
        )


# ---- retrieve() 接线 (注入方法正确但没人调用 = 线上静默不通电) ----


def _retrieve_engine(query_expansion="none", cards=("stx__F__A.md",)):
    """retrieve() 走通 S2 分支所需的最小 RAGEngine 状态 (不建 Chroma / 不发 embedding)."""
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._structured_lookup = None
    eng._study_lookup = SimpleNamespace(
        resolve=lambda q: StudyLookupResult(cards=list(cards), form_scopes=[])
    )
    eng.top_k = 15
    eng.query_expansion = query_expansion
    eng.hybrid_enabled = False
    eng.rerank_enabled = False
    eng.rerank_candidates = 100
    return eng


def test_retrieve_routes_through_study_lookup():
    # 删掉 retrieve() 里的 S2 两行分支, 全量 757 条无一失败 —— 注入方法完全正确却
    # 根本没人调用, 表现为线上 S2 静默不通电、指标退回基线且无报错。
    eng = _retrieve_engine()
    embed_calls = []
    eng._embed_query = lambda t: embed_calls.append(t) or [0.0]
    emb_seen = []

    def fake_search(q, n, where=None, query_embedding=None):
        emb_seen.append(query_embedding)
        if where and "source" in where:
            return [_chunk("lk:card", where["source"])]
        return [_chunk(f"c{i}", f"c{i}.md") for i in range(n)]

    eng._search = fake_search
    out = eng.retrieve("q")
    assert out[0].chunk_id == "lk:card" and out[0].via_lookup, "retrieve() 没走 S2 注入"
    assert len(embed_calls) == 1, f"原查询应只 embed 一次, 实际 {len(embed_calls)}"
    assert all(e is not None for e in emb_seen), "S2 注入检索没复用预算好的 query 向量"


def test_retrieve_embeds_original_query_for_study_lookup_on_hyde_path():
    # need_q_emb 的 study 子句唯一可观测的场景: hyde 自己 embed 的是假想文档, 不 embed 原查询,
    # 所以缺了该子句 q_emb 就是 None, S2 注入退化成每卡各自重新 embed (最坏 13 次往返)。
    # query_expansion="none" 下 `!= "hyde"` 已为真, 该子句在别处恒被遮蔽, 咬不住。
    eng = _retrieve_engine(query_expansion="hyde")
    eng._hypothetical_doc = lambda q: "hypo doc"
    embed_calls = []
    eng._embed_query = lambda t: embed_calls.append(t) or [0.0]
    inject_emb = []

    def fake_search(q, n, where=None, query_embedding=None):
        if where and "source" in where:
            inject_emb.append(query_embedding)
            return [_chunk("lk:card", where["source"])]
        return [_chunk(f"c{i}", f"c{i}.md") for i in range(n)]

    eng._search = fake_search
    out = eng.retrieve("q")
    assert embed_calls == ["q"], "hyde+study 组合下原查询必须被 embed 恰好一次"
    assert inject_emb == [[0.0]], "原查询向量没转发给 S2 注入检索"
    assert out[0].chunk_id == "lk:card"


# ---- S1 回归: 尾部 merge 抽出为共用 _merge_lookup_first, 行为必须逐条不变 ----


def _s1_engine(targets, n_log=None):
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._structured_lookup = SimpleNamespace(resolve=lambda q: list(targets))

    def fake_lookup_chunks(query, rel_path, n, query_embedding=None):
        if n_log is not None:
            n_log.append((rel_path, n))
        return [_chunk(f"s1:{rel_path}:{i}", rel_path) for i in range(n)]

    eng._lookup_chunks_for_file = fake_lookup_chunks
    return eng


def test_apply_structured_lookup_merge_is_lookup_first_deduped_and_capped():
    eng = _s1_engine(["domains/XX/other.md", "domains/YY/other.md"])
    cosine = [_chunk("s1:domains/XX/other.md:0", "a")] + [
        _chunk(f"c{i}", f"c{i}.md") for i in range(14)
    ]
    out = eng._apply_structured_lookup("q", cosine, None, 15, query_embedding=None)
    ids = [c.chunk_id for c in out]
    assert ids[:2] == ["s1:domains/XX/other.md:0", "s1:domains/YY/other.md:0"]
    assert ids[2:] == [f"c{i}" for i in range(13)]   # 去重后 cosine 顺序不变, 截到 k
    assert len(out) == 15
    assert all(c.via_lookup for c in out[:2])


def test_apply_structured_lookup_single_spec_still_injects_four():
    n_log = []
    eng = _s1_engine(["domains/XX/spec.md"], n_log)
    out = eng._apply_structured_lookup("q", [], None, 15, query_embedding=None)
    assert n_log == [("domains/XX/spec.md", rag_mod.RAGEngine._SINGLE_DOMAIN_SPEC_CHUNKS)]
    assert len(out) == rag_mod.RAGEngine._SINGLE_DOMAIN_SPEC_CHUNKS


def test_apply_structured_lookup_noop_when_resolve_empty():
    eng = _s1_engine([])
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_structured_lookup("q", cosine, None, 15, query_embedding=None)
    assert [c.chunk_id for c in out] == [f"c{i}" for i in range(15)]


# ── G1: strong_hit (U6 判库信号层专用) + resolve 行为不变 ─────────────────
#
# `strong_hit` 与 `resolve` 共用 `_channel_hits` 一处实现。共用是为了不漂移, 代价是
# 重构动了 resolve 的内脏 —— 故这里既钉新方法的通道语义, 也钉 resolve 的合并顺序
# (跨通道去重 + 总 cap 截断这两件事最容易在重构里悄悄变形)。

# ALPHA/BETA 段各 10 张 (> _MAX_CARDS_PER_MATCH) ⇒ 单 token 被 cap 挡掉, 唯有交集落在
# cap 内; SOLO 段 1 张 ⇒ 只有 ②b 命中; 另留一张长 label 卡走 ①。
_G1_CATALOG = {"study": "stx", "items": [
    *[_item("FRM_A", f"ALPHA_{i}", f"偽甲ラベル{i}") for i in range(9)],
    *[_item("FRM_A", f"BETA_{i}", f"偽乙ラベル{i}") for i in range(9)],
    _item("FRM_A", "ALPHA_BETA", "偽丙ラベル交差"),
    _item("FRM_B", "SOLO_X", "偽丁ラベル単独"),
    _item("FRM_B", "LONELABEL_Y", "偽戊ラベル全文一致"),
]}
_G1_ALIASES = [{"term": "偽フォーム呼称", "form": "FRM_B"}]


def _g1():
    return StudyLookup(_G1_CATALOG, aliases=_G1_ALIASES)


@pytest.mark.parametrize("channel,query", [
    ("①  label 全文子串", "偽戊ラベル全文一致はありますか"),
    ("②a 多 token 段交集", "ALPHA と BETA の関係は?"),
    ("③  别名 form scope", "偽フォーム呼称について"),
])
def test_strong_hit_true_for_each_strong_channel(channel, query):
    assert _g1().strong_hit(query) is True, channel


def test_strong_hit_false_for_the_weak_single_token_channel():
    """②b 单 token 撞段是弱通道: 对注入层够用 (多召回几张卡), 对判库层不够 ——
    纯标准题里的 SDTM 变量名会精确撞上本研究 OID 段 (Task 9 实测 6 题误触)。"""
    lk = _g1()
    q = "SOLO はどの変数に対応しますか"
    assert lk.resolve(q).cards, "用例失效: ②b 没命中, 这条就证不了排除的是弱通道"
    assert lk.strong_hit(q) is False


def test_strong_hit_ignores_hits_that_the_cap_already_dropped():
    """命中集超 cap 在 resolve 里就是"不具判别力, 整体跳过"; 信号层没有理由反倒认它。
    ALPHA 单段 10 张 > cap ⇒ 既不进 cards, 也不算强信号。"""
    lk = _g1()
    assert lk.resolve("ALPHA について").cards == []
    assert lk.strong_hit("ALPHA について") is False


def test_repeating_one_token_does_not_promote_the_weak_channel():
    """②a 的「多 token」语义全靠 `_channel_hits` 那一次 token 去重保障。

    去重一拆, 同一个 token 在题面里出现两次就让 `len(tokens) >= 2` 成立, 交集退化成该
    单 token 的命中集 ⇒ 弱通道 ②b 的形态从 ①②a③ 的后门走成了强通道 —— 正是 G1 判死的
    那条路 (finding F-07, 抽检 B 探针 2 实证)。
    """
    lk = _g1()
    once, twice = "SOLO はどの変数ですか", "SOLO と SOLO はどの変数ですか"
    assert lk.resolve(once).cards == lk.resolve(twice).cards != [], "用例失效: ②b 没命中"
    assert lk.strong_hit(once) is False
    assert lk.strong_hit(twice) is False


def test_repeated_oid_segment_is_counted_once_against_the_cap():
    """同一张卡的 OID 里出现重复段时, 段索引只许记它一次。

    不去重的话该卡被重复计进 `_segment_index`, 把 `_MAX_CARDS_PER_MATCH` 的计数灌高 ⇒
    本该 fire 的命中被 cap 挡掉 (finding F-14)。下面刚好卡在界上: 去重后 8 张 = cap,
    不去重则 9 条记录 > cap, 整条通道静默不 fire。
    """
    cat = {"study": "stx", "items": [
        *[_item("FRM_R", f"REP_N{i}", f"偽反復ラベル{i}") for i in range(7)],
        _item("FRM_R", "REP_X_REP", "偽反復ラベル末"),
    ]}
    cards = StudyLookup(cat).resolve("REP について").cards
    assert len(cards) == 8
    assert "stx__FRM_R__REP_X_REP.md" in cards


def test_strong_hit_true_when_strong_and_weak_both_hit():
    # 收紧 ≠ 有弱通道就一票否决 (写成 `not weak` 的实现在这里露馅)
    assert _g1().strong_hit("偽戊ラベル全文一致 と SOLO について") is True


@pytest.mark.parametrize("query,expected", [
    # ②a 交集 (ALPHA∩BETA; 两个单段各 10 张均超 cap) 在 label 子串之前
    ("ALPHA と BETA と 偽戊ラベル全文一致 の話",
     ["stx__FRM_A__ALPHA_BETA.md", "stx__FRM_B__LONELABEL_Y.md"]),
    # ②b 单 token (SOLO) 同样在 label 子串之前
    ("SOLO と 偽戊ラベル全文一致 の話",
     ["stx__FRM_B__SOLO_X.md", "stx__FRM_B__LONELABEL_Y.md"]),
])
def test_resolve_puts_segment_hits_before_label_substring(query, expected):
    """跨通道合并顺序 (段级 → label) + 首次出现去重 —— G1 重构最易碰坏的地方。
    顺序即优先级: 末尾按总 cap 截断时, 段级精确命中不该被 label 子串挤掉。
    (②a 先于 ②b 已由 test_intersection_is_enqueued_before_single_token_hits 钉住。)"""
    assert _g1().resolve(query).cards == expected


def test_resolve_total_cap_still_truncates_after_the_refactor():
    # 9 张同 label 家族 + 别的通道, 总量必须仍被 _MAX_CARDS_TOTAL 截断
    cat = {"study": "stx", "items": [
        _item("FRM_C", f"FAM_{i}", "偽共通ラベル") for i in range(12)
    ]}
    assert len(StudyLookup(cat).resolve("偽共通ラベルの話").cards) <= _MAX_CARDS_TOTAL
