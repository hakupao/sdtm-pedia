"""DM2 研读包答案 生成后确定性闸 (spec docs/superpowers/specs/2026-09-25-dossier-output-gate-design.md §2).

纯函数, 零 LLM. ⛔ 本文件只用虚构 OID (FORM_X / ITEM_Y1 / ZQ1_YN …), 不写任何真实 study OID。
"""
from __future__ import annotations

import json

from server.dossier_gate import (
    HIRAGANA_JA_MIN, REGEN_BUDGET, GateRun, OidIndex, check_answer, load_sdtm_names,
    observed_language, regenerate_feedback,
)
from server.dossier_trigger import ANSWER_LANGUAGE_LINE

IDX = OidIndex(
    forms=frozenset({"FORM_X", "FX", "FORM_W"}),
    items=frozenset({"ITEM_Y1", "ITEM_Y2", "ITEM_Y10", "ZQ1_YN", "ZQ2_YN", "CAPQA", "CAPQB"}),
    sdtm_names=frozenset({"AE", "DS", "AETERM", "AEDECOD", "DSCAT", "IETESTCD"}),
    domains=frozenset({"AE", "DS", "IE"}),
)
Q_EN = "Which EDC items in our study map to the ds domain?"
Q_ZH = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"


def _unk(answer, q=Q_EN):
    return check_answer(answer, q, IDX).unknown_oids


# ── G-OID: 规则句强制的引用形态 ─────────────────────────────────────

def test_known_reference_passes():
    r = check_answer("Candidates: `[表X FORM_X] 項目です (ITEM_Y1)` (推測)", Q_EN, IDX)
    assert r.ok and r.unknown_oids == () and r.reasons == ()


def test_unknown_item_in_item_slot_is_flagged():
    assert _unk("- [表X FORM_X] 登録日 (ITEM_Z9) (推測)") == ("ITEM_Z9",)


def test_unknown_form_in_form_slot_is_flagged():
    assert _unk("- [表Q FORM_Q] 登録日 (ITEM_Y1)") == ("FORM_Q",)


def test_item_slot_is_the_last_paren_of_the_reference_label():
    # 项目 label 自己带括号缩写 (如 (HIV)) —— 那不是 OID 槽, 最后一个括号才是
    assert _unk("- [表X FORM_X] ウイルス（HIV）感染を有する。 (ITEM_Y2)") == ()


def test_source_and_web_citations_are_not_references():
    assert _unk("text [Source: domains/AE/spec.md] and [Web: https://x.example/ZZTOP]") == ()


def test_whitelist_sdtm_names_domains_ccodes_abbreviations_supp():
    ans = ("`AETERM` / `AEDECOD` (DSCAT) (AE) codelist (C66727) via the (EDC) and (PRT) "
           "stored in (SUPPAE) — `DSCAT = \"DISPOSITION EVENT\"`")
    assert _unk(ans) == ()


def test_placeholders_and_wildcards_are_not_counted():
    assert _unk("`ITEM_Yn` `ITEM_*` `*_Y1` `ITEM_Ynn` (ITEM_Y1〜)") == ()


def test_family_prefix_counts_only_when_a_member_exists():
    assert _unk("the `ITEM_Y` family") == ()
    assert _unk("`[表X FORM_X] items (ITEM_Q)`") == ("ITEM_Q",)


def test_range_and_list_shorthand_endpoints_that_expand_to_real_members():
    assert _unk("`ITEM_Y1/Y2/Y10` and `ITEM_Y1〜ITEM_Y10`") == ()


def test_unknown_token_listed_next_to_a_real_oid_is_flagged():
    # 同一列表里与真实 OID 并列 = 同一类东西 (OID 断言), 不是散文词
    assert _unk("drug items (`CAPQA`, `CAPQZ/CAPQB`)") == ("CAPQZ",)


def test_bare_backtick_word_without_oid_shape_is_not_flagged():
    # SDTM 侧的取值 / 缩写单独出现在反引号里, 与一览的命名空间无关 ⇒ 不计
    assert _unk("`IETESTCD = ZQL05` e.g. `ZQL09` / `ZQL05`, category `EXCLUSION`") == ()


def test_near_miss_oid_with_catalog_stem_is_flagged():
    # 词干与一览里的 OID 相同、编号/后缀自造 ⇒ 补全/构造出来的 OID (规则 ③ 禁止)
    assert _unk("an EDC item OID (e.g. `ZQ05`)") == ("ZQ05",)


def test_prefixed_form_oid_anywhere_is_flagged():
    # 给真实表单 OID 自造前缀: 出现在表格裸文本里也算 (§4 预期迫使的全文扫描, 仅此一种形态)
    ans = "| 手術 | Z_FX（対応表より）の ITEM_Y1 | (推測) |\n| x | B_FORM_W | |"
    assert _unk(ans) == ("B_FORM_W", "Z_FX")


def test_unknown_oids_are_sorted_and_deduplicated():
    assert _unk("[a FORM_Q] x (ITEM_Z9) / [b FORM_Q] y (ITEM_Z9)") == ("FORM_Q", "ITEM_Z9")


def test_single_letter_tokens_are_never_candidates():
    assert _unk("[a FORM_X] x (Q)") == ()


# ── G-LANG ─────────────────────────────────────────────────────────

def test_language_ok_when_japanese_is_only_in_quoted_references():
    labels = "\n".join(f"- `[表X FORM_X] これはひらがなのラベルです (ITEM_Y1)`" for _ in range(40))
    labels += "\n" + "\n".join("- [表X FORM_X] これはひらがなのラベルです (ITEM_Y2)" for _ in range(40))
    r = check_answer("These are the candidates:\n" + labels, Q_EN, IDX)
    assert r.lang_expected == "en" and r.lang_observed == "en" and r.ok


def test_language_drift_is_flagged_with_reason():
    ans = "これは日本語の答えです。" * 30
    r = check_answer(ans, Q_ZH, IDX)
    assert (r.lang_expected, r.lang_observed, r.ok) == ("zh", "ja", False)
    assert any("ja" in x and "zh" in x for x in r.reasons)


def test_hiragana_threshold_boundary():
    assert HIRAGANA_JA_MIN == 100
    assert observed_language("あ" * (HIRAGANA_JA_MIN - 1)) != "ja"
    assert observed_language("あ" * HIRAGANA_JA_MIN) == "ja"


def test_kanji_vs_latin_words_decides_zh_vs_en():
    assert observed_language("这是中文答案" * 5 + " some words") == "zh"
    assert observed_language("Mostly English words here with 中文") == "en"


def test_fixed_markers_are_not_counted():
    assert observed_language("An English answer (推測) 候補なし / no candidate item in the EDC") == "en"


# ── GateResult / 反馈 / 编排 ─────────────────────────────────────────

def test_to_dict_is_json_shape_of_spec():
    d = check_answer("[a FORM_Q] x (ITEM_Y1)", Q_EN, IDX).to_dict()
    assert set(d) == {"ok", "unknown_oids", "lang_expected", "lang_observed", "reasons"}
    assert d["unknown_oids"] == ["FORM_Q"] and d["ok"] is False
    json.dumps(d)


def test_feedback_is_runtime_data():
    r = check_answer("[a FORM_Q] x (ITEM_Z9) " + "これは日本語です。" * 30, Q_EN, IDX)
    fb = regenerate_feedback(r)
    assert "FORM_Q" in fb and "ITEM_Z9" in fb
    assert ANSWER_LANGUAGE_LINE["en"] in fb
    ok = check_answer("fine", Q_EN, IDX)
    assert "FORM_Q" not in regenerate_feedback(ok)


def test_gate_run_regenerates_at_most_once():
    assert REGEN_BUDGET == 1
    g = GateRun(IDX, Q_EN)
    bad = "[a FORM_Q] x (ITEM_Y1)"
    r1 = g.observe(bad)
    assert not r1.ok and g.should_regenerate()
    msgs = [{"role": "system", "content": "S"}, {"role": "user", "content": "U"}]
    nxt = g.regenerate_messages(msgs, bad)
    assert nxt[:2] == msgs and nxt[2] == {"role": "assistant", "content": bad}
    assert nxt[3]["role"] == "user" and "FORM_Q" in nxt[3]["content"]
    assert len(msgs) == 2  # 不改调用方的列表
    g.observe(bad)
    assert not g.should_regenerate()
    p = g.payload()
    assert p["regenerated"] is True and p["final"]["ok"] is False and p["first"]["ok"] is False


def test_gate_run_pass_first_time():
    g = GateRun(IDX, Q_EN)
    g.observe("clean answer")
    assert not g.should_regenerate()
    assert g.payload() == {"final": g.final.to_dict(), "first": None, "regenerated": False}


def test_gate_run_empty_first_answer_reasks_without_assistant_turn():
    g = GateRun(IDX, Q_ZH)
    g.observe("")
    msgs = [{"role": "user", "content": "U"}]
    assert g.should_regenerate()
    assert g.regenerate_messages(msgs, "") == msgs


def test_gate_run_regeneration_failed_keeps_first_as_final():
    g = GateRun(IDX, Q_EN)
    g.observe("[a FORM_Q] x (ITEM_Y1)")
    assert g.should_regenerate()
    g.regeneration_failed("TimeoutError")
    p = g.payload()
    assert p["regenerated"] is False and p["first"] is None
    assert p["final"]["ok"] is False and p["regenerate_error"] == "TimeoutError"


# ── 构建 ────────────────────────────────────────────────────────────

def test_index_from_catalog_and_kb(tmp_path):
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps({"forms": [{"oid": "FORM_X"}],
                               "items": [{"item_oid": "ITEM_Y1", "form_oid": "FORM_X"}]}),
                   encoding="utf-8")
    kb = tmp_path / "kb"
    (kb / "domains" / "AE").mkdir(parents=True)
    (kb / "domains" / "AE" / "spec.md").write_text("# AE\n\n### AETERM\n\n### AESEV\n", encoding="utf-8")
    idx = OidIndex.from_catalog(cat, kb)
    assert idx.forms == {"FORM_X"} and idx.items == {"ITEM_Y1"}
    assert {"AE", "AETERM", "AESEV"} <= idx.sdtm_names and idx.domains == {"AE"}
    names, domains = load_sdtm_names(kb)
    assert "AESEV" in names and domains == {"AE"}


def test_real_kb_whitelist_is_non_trivial():
    from server.config import Settings
    names, domains = load_sdtm_names(Settings().kb_root)
    assert len(domains) >= 60 and len(names) >= 1000 and "DSDECOD" in names
