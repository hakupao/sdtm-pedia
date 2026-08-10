"""§2.A2 扫描的**判定规则**单测。

规则表写死在 `eval.cap_recall_sweep` 的 docstring 里 (硬规矩 8: 判定规则必须先于
数据写死, 自毁条款排在肯定性结论之前)。它算错就会把"配额有害"读成"配额可做"。
逐条钉死: 5 行逐档表 + 两条自毁条款的**优先级** + "ctx 没变的题不进统计" +
out_of_scope 排除 + S1 分组 + 天花板声明。
"""
import pytest

from eval.cap_recall_sweep import (
    _classify,
    analyze,
    hidden_loss_shadow,
    overall_verdict,
)


def _arm(recall, ctx_diff, *, seats=15, s1=0, hits=(), equals_production=True, is_a=False):
    a = {"source_recall": recall, "ctx_diff_vs_A": ctx_diff, "seats": seats,
         "s1_injected": s1, "source_hits": list(hits), "composition": []}
    if is_a:
        a["equals_production"] = equals_production
    return a


def _row(qid, a_recall, caps, *, s1=0, out_of_scope=False, equals_production=True):
    """caps: {label: (recall, ctx_diff)}"""
    arms = {"A": _arm(a_recall, 0, s1=s1, equals_production=equals_production, is_a=True)}
    for label, (recall, diff) in caps.items():
        arms[label] = _arm(recall, diff, s1=s1)
    return {"id": qid, "category": "x", "question": "q", "out_of_scope": out_of_scope,
            "n_fused": 60, "arms": arms}


def _uniform(qid, a_recall, recall, diff, **kw):
    return _row(qid, a_recall, {"cap1": (recall, diff), "cap2": (recall, diff),
                                "cap3": (recall, diff)}, **kw)


# ---- 逐档结论表 (R1-R5) -----------------------------------------------------


@pytest.mark.parametrize(("improved", "regressed", "expected"), [
    (2, 0, "SAFE_AND_HELPS"),        # R1
    (0, 0, "INERT_ON_THIS_RULER"),   # R2
    (3, 1, "MIXED"),                 # R3
    (1, 5, "MIXED"),                 # R3 (降多于升仍是 MIXED, 由人逐题看)
    (0, 4, "HARMFUL"),               # R4
])
def test_classify_table(improved, regressed, expected):
    assert _classify(improved, regressed) == expected


def test_classify_has_a_real_default_row():
    """R5 是 default 行: 非法输入必须落到 UNCLASSIFIED, 不许静默返回某个肯定性结论。

    四个条件对非负整数是穷举的, 故 R5 正常跑不到 —— 这正是 default 行的意义
    (硬规矩 8: 决策表要穷举, 或显式写 default 行)。用非法输入证明它真的存在。
    """
    assert _classify(-1, -1) == "UNCLASSIFIED"


# ---- 自毁条款的优先级 -------------------------------------------------------


def test_wiring_failure_voids_everything_even_when_results_look_great():
    """接线闸红时, 哪怕逐档表满是 SAFE_AND_HELPS, 结论也必须是 VOID_WIRING。

    自毁条款排在肯定性结论之前 —— 最省事的读法 ("A 臂差一点点, 但改善这么明显")
    必须够不着。
    """
    rows = [_uniform("q1", 0.5, 1.0, 5, equals_production=False),
            _uniform("q2", 0.5, 1.0, 5)]
    a = analyze(rows)
    assert a["conclusion"] == "VOID_WIRING"
    assert a["wiring_check"]["failed_ids"] == ["q1"]
    # 逐档统计仍然照算并落盘 (供查明用), 但不许成为结论
    assert a["arms"]["cap1"]["verdict"] == "SAFE_AND_HELPS"


def test_no_context_change_anywhere_voids():
    """配额压根没生效时, 全场同分是废话不是证据。"""
    rows = [_uniform("q1", 1.0, 1.0, 0), _uniform("q2", 1.0, 1.0, 0)]
    assert analyze(rows)["conclusion"] == "VOID_NO_EFFECT_MEASURED"


# ---- 统计口径 ---------------------------------------------------------------


def test_ctx_unchanged_questions_do_not_count_as_evidence():
    """ctx 与 A 逐位相同的题, 同分不构成"配额无害"的证据, 不进 improved/regressed/tie。"""
    rows = [_uniform("q1", 1.0, 1.0, 0),          # ctx 没变
            _uniform("q2", 0.5, 1.0, 7)]          # ctx 变了且升
    a = analyze(rows)
    s = a["arms"]["cap1"]
    assert (s["n"], s["n_ctx_changed"]) == (2, 1)
    assert (s["improved"], s["improved_ids"]) == (1, ["q2"])
    assert s["tie_among_changed"] == 0
    # 均值仍按全部计分题算 —— 它是 eval 口径, 不是证据口径
    assert s["mean_recall_A"] == pytest.approx(0.75)


def test_regression_wins_over_improvement_in_arm_verdict():
    rows = [_uniform("q1", 0.5, 1.0, 7), _uniform("q2", 1.0, 0.5, 7)]
    a = analyze(rows)
    assert a["arms"]["cap1"]["verdict"] == "MIXED"
    assert a["arms"]["cap1"]["regressed_ids"] == ["q2"]
    assert a["conclusion"] == "CAP_MIXED"


def test_all_arms_harmful_gives_cap_harmful():
    rows = [_uniform("q1", 1.0, 0.5, 7), _uniform("q2", 1.0, 0.0, 7)]
    a = analyze(rows)
    assert a["conclusion"] == "CAP_HARMFUL"


def test_one_safe_arm_is_enough_to_recommend_task7():
    """逐档决策: 只要有一档零回归且有改善, 就够支撑 Task 7 (按那一档做)。"""
    rows = [_row("q1", 0.5, {"cap1": (1.0, 7), "cap2": (0.5, 7), "cap3": (0.25, 7)})]
    a = analyze(rows)
    assert a["arms"]["cap1"]["verdict"] == "SAFE_AND_HELPS"
    assert a["arms"]["cap3"]["verdict"] == "HARMFUL"
    assert a["conclusion"] == "CAP_HELPS"
    assert "cap1" in a["conclusion_text"]


def test_out_of_scope_excluded_from_scoring():
    """out_of_scope 题空 gold 恒得 1.0, 计进平均值就是白送分。"""
    rows = [_uniform("q1", 0.5, 1.0, 7), _uniform("q2", 1.0, 1.0, 7, out_of_scope=True)]
    a = analyze(rows)
    assert (a["n_total"], a["n_scored"], a["n_out_of_scope"]) == (2, 1, 1)
    assert a["arms"]["cap1"]["n"] == 1


def test_s1_injection_grouping_splits_the_blind_and_sighted_questions():
    """S1 注入 >0 的题, 判据对被 S1 钉死的 gold 失明 (硬规矩 9) —— 必须分组读。"""
    rows = [_uniform("q1", 0.5, 1.0, 7, s1=0), _uniform("q2", 0.5, 1.0, 7, s1=3)]
    a = analyze(rows)
    assert a["by_s1_injection"]["s1_zero"]["cap1"]["improved_ids"] == ["q1"]
    assert a["by_s1_injection"]["s1_nonzero"]["cap1"]["improved_ids"] == ["q2"]


def test_ceiling_is_reported_with_the_ids_that_carry_all_upside():
    """天花板声明必须能与任何"净升"数字并排陈列, 否则读者会把小幅度读成小效应。"""
    rows = [_uniform("q1", 1.0, 1.0, 3), _uniform("q2", 0.3333, 1.0, 3),
            _uniform("q3", 0.5, 1.0, 3)]
    c = analyze(rows)["ceiling"]
    assert c["n_below_1.0_in_A"] == 2
    assert c["ids_below_1.0_in_A"] == ["q2", "q3"]
    assert c["headroom_pt"] == pytest.approx((1 - (1 + 0.3333 + 0.5) / 3) * 100, abs=1e-3)


# ---- 影子信号 (OR 组把回归吃掉的取证) ---------------------------------------
#
# 2026-08-11 抽检方变异测试补上的: 首版把 `hidden_loss_shadow` 改成恒返回空,
# 17 条单测**全绿** —— 那个信号当时是装饰 (硬规矩 16②: 一道不会红的闸就是装饰)。


def _shadow_row(qid, recall_a, hits_a, recall_x, hits_x, *, out_of_scope=False):
    """只在 cap1 上制造影子; cap2/cap3 原样复制 A (ctx 没变), 免得干扰逐档统计。"""
    row = _row(qid, recall_a, {"cap1": (recall_x, 5), "cap2": (recall_a, 0),
                               "cap3": (recall_a, 0)}, out_of_scope=out_of_scope)
    row["arms"]["A"]["source_hits"] = list(hits_a)
    row["arms"]["cap1"]["source_hits"] = list(hits_x)
    for lab in ("cap2", "cap3"):
        row["arms"][lab]["source_hits"] = list(hits_a)
    return row


def test_shadow_catches_a_lost_hit_that_the_score_hides():
    """分数没动但 A 命中的某条 gold 掉了 —— OR 组把回归吃掉的确切形态。

    kickoff §2.A′: q115/q117 的 OR 组是该题**唯一计分单位**且含严格弱成员 ⇒
    只命中最弱成员照样 1.0。这条断言就是为了让那种退化**看得见**。
    """
    rows = [_shadow_row("q115", 1.0, ["strong.md", "weak.md"], 1.0, ["weak.md"])]
    s = hidden_loss_shadow(rows, ["cap1"])["cap1"]
    assert s["n"] == 1 and s["ids"] == ["q115"]
    assert s["detail"][0]["hits_lost"] == ["strong.md"]


def test_shadow_ignores_losses_the_score_already_reflects():
    """分数已经掉了的题不算"影子" —— 它进 regressed, 不该被重复计一次。"""
    rows = [_shadow_row("q08", 1.0, ["a.md", "b.md"], 0.5, ["a.md"])]
    assert hidden_loss_shadow(rows, ["cap1"])["cap1"]["n"] == 0


def test_shadow_is_silent_when_nothing_was_lost():
    rows = [_shadow_row("q01", 1.0, ["a.md"], 1.0, ["a.md"]),
            _shadow_row("q02", 1.0, ["a.md"], 1.0, ["a.md", "extra.md"])]
    assert hidden_loss_shadow(rows, ["cap1"])["cap1"]["n"] == 0


def test_shadow_skips_out_of_scope_questions():
    rows = [_shadow_row("q99", 1.0, ["a.md"], 1.0, [], out_of_scope=True)]
    assert hidden_loss_shadow(rows, ["cap1"])["cap1"]["n"] == 0


def test_analyze_carries_the_shadow_signal_through():
    """analyze() 必须把影子信号带出来 —— 只在函数里算而不落进结论, 等于没算。"""
    rows = [_shadow_row("q115", 1.0, ["strong.md", "weak.md"], 1.0, ["weak.md"])]
    a = analyze(rows)
    assert a["hidden_loss_shadow"]["cap1"]["ids"] == ["q115"]


def test_overall_verdict_flags_unclassified_first():
    per_arm = {"cap1": {"verdict": "SAFE_AND_HELPS"}, "cap2": {"verdict": "UNCLASSIFIED"}}
    assert overall_verdict(per_arm)[0] == "UNCLASSIFIED"


def test_inert_conclusion_text_refuses_to_claim_harmlessness():
    """全档 INERT 时, 结论文字必须明说"这不等于挤占无害" —— 上一轮就栽在这个读法上。"""
    rows = [_uniform("q1", 1.0, 1.0, 7)]
    a = analyze(rows)
    assert a["conclusion"] == "CAP_INERT"
    assert "不等于" in a["conclusion_text"]
