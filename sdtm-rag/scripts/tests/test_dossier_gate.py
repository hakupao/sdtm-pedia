"""DM2 研读包答案 生成后确定性闸 (spec docs/superpowers/specs/2026-09-25-dossier-output-gate-design.md §2).

纯函数, 零 LLM. ⛔ 本文件只用虚构 OID (FORM_X / ITEM_Y1 / ZQ1_YN …), 不写任何真实 study OID。
"""
from __future__ import annotations

import json

from server.dossier_gate import (
    JA_SIGNAL_RATIO,
    MIN_BODY_CHARS,
    REGEN_BUDGET,
    GateRun,
    OidIndex,
    check_answer,
    load_sdtm_names,
    observed_language,
    regenerate_feedback,
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


# ── 严格位不套宽白名单 (N2) / 误报形态 (N4) ─────────────────────────

def test_sdtm_name_in_item_slot_is_a_fabrication():
    # M1: 项目槽里写 SDTM 变量名 = 编了一个不存在的 EDC OID
    assert _unk("- [表X FORM_X] 重症度 (AETERM) (推測)") == ("AETERM",)


def test_truncated_family_prefix_in_item_slot_is_flagged():
    # M2: 族前缀只在宽松位 (说「这一族」) 才放行, 槽里写半截 = 捏造
    assert _unk("- [表X FORM_X] 登録日 (ITEM_Y) (推測)") == ("ITEM_Y",)


def test_abbreviation_listed_with_real_oid_in_item_slot_is_not_flagged():
    # F1
    assert _unk("- [表X FORM_X] 感染 (ITEM_Y1, HIV) (推測)") == ()
    assert _unk("- [表X FORM_X] 感染 (ITEM_Y1, ITEM_Y7) (推測)") == ("ITEM_Y7",)


def test_single_segment_brackets_are_not_form_slots():
    # F2: GitHub alert / 标签式方括号
    assert _unk("> [!NOTE]\n> ITEM_Y1 is inferred (推測).") == ()
    assert _unk("Mapping of ITEM_Y1 [TBD] (推測)") == ()
    # 单段方括号里像 OID 的仍然计 (宽松位)
    assert _unk("see [FORM_X9] for dates") == ("FORM_X9",)


def test_prefixed_form_scan_skips_forms_that_are_domain_codes():
    # F3: 表单 OID 恰是域码时, `<前缀>_AE` 说的是数据集
    idx = OidIndex(forms=frozenset({"AE", "FX"}), items=frozenset({"ITEM_Y1"}),
                   domains=frozenset({"AE"}), sdtm_names=frozenset({"AE"}))
    assert check_answer("SDTM dataset RAW_AE is derived from form AE", Q_EN, idx).unknown_oids == ()
    assert check_answer("form Z_FX holds the dates", Q_EN, idx).unknown_oids == ("Z_FX",)


def test_item_slot_prefers_the_paren_with_a_real_oid_over_trailing_prose():
    ans = "- [表X FORM_X] 詳細 (ITEM_Y1) — 標準変数ではないため **SUPPQUAL (SUPPAE) の提案**"
    assert _unk(ans) == ()


# ── G-LANG ─────────────────────────────────────────────────────────

EN = "This answer lists the candidate items for the target domain in plain English prose. " * 5
ZH = "以下是本研究中适合进入该域的候选项目，均为推测，需要结合标准定义逐项确认。" * 6
JA = "以下は本研究でこのドメインに入ると考えられる候補項目です。すべて推測であり、標準の定義と照合が必要です。" * 4


def test_language_ok_when_japanese_is_only_in_quoted_references():
    labels = "\n".join("- `[表X FORM_X] これはひらがなのラベルです (ITEM_Y1)`" for _ in range(40))
    labels += "\n" + "\n".join("- [表X FORM_X] これはひらがなのラベルです (ITEM_Y2)" for _ in range(40))
    r = check_answer(EN + "\n" + labels, Q_EN, IDX)
    assert r.lang_expected == "en" and r.lang_observed == "en" and r.ok


def test_hiragana_in_corner_quotes_is_not_counted():
    # MUT1: 英文答案里用「」引用日文原文 ⇒ 仍是 en
    r = check_answer(EN + "「これはひらがなで書かれた引用です」" * 30, Q_EN, IDX)
    assert r.lang_observed == "en" and r.ok


def test_language_drift_is_flagged_with_reason():
    r = check_answer(JA, Q_ZH, IDX)
    assert (r.lang_expected, r.lang_observed, r.ok) == ("zh", "ja", False)
    assert any("ja" in x and "zh" in x for x in r.reasons)


def test_ratio_decides_ja_vs_zh_and_cjk_vs_latin_decides_en():
    assert JA_SIGNAL_RATIO == 0.3 and MIN_BODY_CHARS == 200
    assert observed_language(JA) == "ja"
    assert observed_language(ZH) == "zh"
    assert observed_language(EN) == "en"
    # 比例边界 (「中」在 GB2312 里, 不算日本字形): ja 信号恰在阈值上 ⇒ ja, 低一点 ⇒ zh
    assert observed_language("あ" * 90 + "中" * 210) == "ja"
    assert observed_language("あ" * 89 + "中" * 211) == "zh"
    # 片假名与日本字形漢字也是 ja 信号
    assert observed_language("ア" * 90 + "中" * 210) == "ja"
    assert observed_language("項" * 90 + "中" * 210) == "ja"


def test_short_body_is_not_judged():
    # F5: 合法的短日文答案 —— 样本太小, 不判 (而不是误判成 zh)
    ans = "DS ドメインの候補は ITEM_Y1 です。これは同意の日付を記録する項目で、DSSTDTC に入ると考えられます (推測)。"
    r = check_answer(ans, "本試験で DS ドメインに入るデータはどれですか？", IDX)
    assert r.lang_observed is None and r.ok and r.to_dict()["lang_observed"] is None
    assert observed_language("あ" * (MIN_BODY_CHARS - 1)) is None


def test_table_cells_are_not_counted():
    # F4: 英文答案, 表格里全是日文 label
    rows = "\n".join("| ITEM_Y1 | これはひらがなのラベルです |" for _ in range(40))
    r = check_answer(EN + "\n| OID | Label |\n|---|---|\n" + rows, Q_EN, IDX)
    assert r.lang_observed == "en" and r.ok
    # F6: 中文答案, 表格里全是 OID / 变量名
    rows = "\n".join("| ITEM_Y1 ITEM_Y2 | AETERM AEDECOD | DSCAT | 严重 |" for _ in range(40))
    r = check_answer(ZH + "\n" + rows, Q_ZH, IDX)
    assert r.lang_observed == "zh" and r.ok


def test_fixed_markers_are_not_counted():
    assert observed_language(EN + "(推測) 候補なし / no candidate item in the EDC " * 20) == "en"


def test_empty_answer_never_passes():
    for ans in ("", "   \n "):
        r = check_answer(ans, Q_EN, IDX)
        assert not r.ok and "答案为空" in r.reasons


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


# ── 复审 probe (虚构 OID; 白名单用真实 KB 的 SDTM 名) ─────────────────

def _probe_idx():
    from server.config import Settings
    names, doms = load_sdtm_names(Settings().kb_root)
    return OidIndex(forms=frozenset({"ZQVITAL", "ZQADVEV"}),
                    items=frozenset({"ZQVTEMP", "ZQVPULS", "ZQAESEV1", "ZQAETERM"}),
                    sdtm_names=names, domains=doms)


PROBE_OID = {
    # 同行第二项 / label 自带括号 / 槽后散文: 半严格 (N-2)
    "- [ZQVITAL] Temperature (ZQVTEMP), Pulse (ZQVPULSE) (推測)": ("ZQVPULSE",),
    "- [ZQVITAL] Temperature (ZQVTEMP), Pulse (ZQVPULS2) (推測)": ("ZQVPULS2",),
    # 已知限制: 槽之后的括号只计「像 OID」的 (与一览共享 ≥3 字符前缀 / 带数字下划线), 新词干纯字母
    # 捏造在槽后会漏 —— 换来的是槽后散文里 (UNK) / (TBD) 这类词不再误报 (复审第三轮裁定)。
    "- [ZQVITAL] Temperature (ZQVTEMP), Weight (ZQWEIGHT) (推測)": (),
    "- [ZQVITAL] Pulse (ZQVPULSE) (推測)": ("ZQVPULSE",),
    "- [ZQVITAL] Temp (ZQVTMP) (ZQVTEMP)": ("ZQVTMP",),
    "- [ZQVITAL] Temperature (ZQVTEMP), BMI (ZQVBMI1)": ("ZQVBMI1",),
    "- [ZQVITAL] Temperature (ZQVTEMP) — 单位见 (ZQVTEMP_U)": ("ZQVTEMP_U",),
    "- [ZQVITAL] 体温 (ZQVTEMPX) — 参照 (SUPPVS)": ("ZQVTEMPX",),
    # 严格位列表: 例外只放宽白名单 (N-3)
    "- [ZQVITAL] Temp (ZQVTEMP, QXFAKE)": ("QXFAKE",),
    "- [ZQVITAL] Temp (ZQVTEMP, ZQVTEMPU)": ("ZQVTEMPU",),
    "- [ZQVITAL] Temperature (ZQVTEMP, HIV)": (),
    "- [ZQVITAL] Temperature (ZQVTEMP); [ZQVITAL] Pulse (ZQVPULSE)": ("ZQVPULSE",),
    "- [ZQVITALS] Temperature (ZQVTEMP)": ("ZQVITALS",),
    "- [Vital Signs ZQVITALX] Temperature (ZQVTEMP)": ("ZQVITALX",),
    # 误报 (N-4)
    "- [ZQVITAL] 全部映射到 Vital Signs (VS)": (),
    "- [ZQVITAL] form-level note (SDTM)": (),
    "见 [参考 VS] 说明": (),
    "参照 [See SDTMIG] 3.4 节": (),
    "> [!NOTE]\n> 说明": (),
    "- [ZQVITAL] Temperature (ZQVTEMP) → VSORRES; 另见 SUPPVS (QNAM)": (),
    "RAW_VS 数据集": (),
    "表里写 RAW_ZQVITAL": ("RAW_ZQVITAL",),
    "表里写 ZQVITAL_RAW": (),   # 已知限制 M10: 后缀形态不扫
}


def test_review_probe_oid_cases():
    idx = _probe_idx()
    for ans, want in PROBE_OID.items():
        assert check_answer(ans, Q_EN, idx).unknown_oids == want, ans


def test_review_probe_language_cases():
    # 体言止め列表 / 见出し多: 平仮名几乎为零的日文 ⇒ 仍是 ja
    ja_list = ("- 体温項目：生命徴候領域対応（推測）\n- 単位項目：結果単位変数対応\n"
               "- 測定日時：日付時刻変数対応\n- 測定部位：部位変数対応、補足修飾子候補\n") * 5 + "以上の通り。"
    assert observed_language(ja_list) == "ja"
    assert observed_language("### 生命徴候領域\n候補項目一覧。測定値、単位、評価日。\n" * 12) == "ja"
    assert observed_language("体温項目ハ生命徴候領域ニ対応。単位及結果別途記録、補足データセット説明要。" * 8) == "ja"
    # 夹未加引号日文 label 的中文 ⇒ 仍是 zh
    assert observed_language("体温项目（EDC 标签：体温を測定した日）应映射到 VSDTC，其余项目见下。" * 6) == "zh"
    assert observed_language("本研究的体温项目应当映射到生命体征域，其单位与结果需要分别记录并在补充数据集中说明。" * 6) == "zh"
    assert observed_language("本研究の体温項目は生命徴候領域へ対応付けることになります。単位と結果はそれぞれ記録して、"
                             "補足データセットで説明してください。" * 5) == "ja"
    assert observed_language("The item should map to VSORRES and the unit to VSORRESU per the standard. " * 6
                             + "注意：推测。") == "en"
    # 太短: 不判
    assert observed_language("- Item maps to VSORRES. " * 3 + "本研究的体温项目应当映射到生命体征域。" * 4) is None
    r = check_answer("答えは以下の通りです。体温は VS にマッピングされます。", "体温项目应映射到哪个域？", _probe_idx())
    assert r.ok and r.lang_observed is None


# ── 复审第三轮 ──────────────────────────────────────────────────────

def test_prose_parens_after_the_slot_only_count_when_oid_like():
    idx = _probe_idx()
    for w in ("TBD", "NA", "UNK", "BID", "MMHG", "IV", "ND", "OTHER", "CRO", "UNITX"):
        ans = f"- [ZQVITAL] Temperature (ZQVTEMP) — 未测时填 ({w})"
        assert check_answer(ans, Q_EN, idx).unknown_oids == (), w
    # 像 OID 的仍然抓: 与一览共享前缀 / 带数字
    assert check_answer("- [ZQVITAL] Temperature (ZQVTEMP) — 另见 (ZQVPULSE)", Q_EN,
                        idx).unknown_oids == ("ZQVPULSE",)
    assert check_answer("- [ZQVITAL] Temperature (ZQVTEMP) — 另见 (QXW2)", Q_EN,
                        idx).unknown_oids == ("QXW2",)
    # 槽之前 (label 自带括号) 的判定不变: 纯字母新词干照样计
    assert check_answer("- [ZQVITAL] Temp (QXFAKE) (ZQVTEMP)", Q_EN, idx).unknown_oids == ("QXFAKE",)


def test_two_segment_bracket_allows_sdtm_variable_names():
    idx = _probe_idx()
    assert check_answer("映射 [→ VSORRES] 见上", Q_EN, idx).unknown_oids == ()
    assert check_answer("详见 [参照 VSTESTCD]", Q_EN, idx).unknown_oids == ()
    assert check_answer("见 [参考 QXFAKE]", Q_EN, idx).unknown_oids == ("QXFAKE",)
    # 项目槽兜底不放变量名 (M1 形态照旧计)
    assert check_answer("- [ZQVITAL] 体温 (VSORRES) (推測)", Q_EN, idx).unknown_oids == ("VSORRES",)
