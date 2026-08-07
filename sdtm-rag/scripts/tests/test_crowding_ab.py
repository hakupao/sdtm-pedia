"""配额语义: 同名 section 限 cap 席, 腾出的席位由池中下一位依次补足。

外加**判定规则**的单测: 规则表 (spec §2.2b) 写死在 `eval.crowding_ab.verdict` 里,
它算错就会把"不修"读成"修"。5 行表 + 硬 gate + judge 缺分, 逐条钉死。
"""
from eval.crowding_ab import verdict
from server.diversity import apply_section_cap


class _C:
    def __init__(self, cid, section, via_lookup=False):
        self.chunk_id, self.section = cid, section
        self.source = f"src/{cid}.md"
        self.via_lookup = via_lookup


def test_cap_keeps_first_n_of_each_cluster():
    """配额是**均匀**的: §Other 也只留 2 席, 不是"只削最大簇"。

    brief 初稿此处期望 [0, 1, 90, 91, 92] (§Other 三条全留), 与它自己的
    apply_section_cap 实现、与下面的 test_cap_preserves_relative_order (A/B 两簇同时
    受限)、以及 Task 5 已落库的 eval.pool_depth_probe.seats_under_quota
    (Σ_section min(count, quota) —— 同一批候选算出 4 席) 三者都矛盾。改期望值而非改
    语义: 席位可行性数字 (q38 在配额 2/3/5 下 4/5/7 席) 正是按均匀配额算的, 动语义
    会让 q38 的 fallback 口径失去依据。
    """
    pool = [_C(i, "DOMAIN") for i in range(5)] + [_C(90 + i, "Other") for i in range(3)]
    out = apply_section_cap(pool, cap=2)
    assert [c.chunk_id for c in out] == [0, 1, 90, 91]


def test_cap_preserves_relative_order():
    pool = [_C(0, "A"), _C(1, "B"), _C(2, "A"), _C(3, "A"), _C(4, "B")]
    out = apply_section_cap(pool, cap=1)
    assert [c.chunk_id for c in out] == [0, 1]


def test_lookup_chunks_exempt_from_cap():
    """S1 注入是确定性 gold, 不属被检验对象 —— 三组一律豁免。"""
    pool = [_C(0, "VISIT", via_lookup=True), _C(1, "VISIT", via_lookup=True),
            _C(2, "VISIT", via_lookup=True), _C(3, "VISIT"), _C(4, "VISIT"), _C(5, "X")]
    out = apply_section_cap(pool, cap=1)
    assert [c.chunk_id for c in out] == [0, 1, 2, 3, 5]


def test_cap_none_is_identity():
    pool = [_C(i, "A") for i in range(4)]
    assert [c.chunk_id for c in apply_section_cap(pool, cap=None)] == [0, 1, 2, 3]


def test_none_sections_are_not_clustered_together():
    """section=None 不是一个'簇名' —— 缺元数据不该被当成同质。"""
    pool = [_C(i, None) for i in range(4)]
    assert len(apply_section_cap(pool, cap=1)) == 4


# ---- 判定规则表 (spec §2.2b) -------------------------------------------------


def _rows(pairs, full_seats=True, parse_ok=True):
    """pairs = [(A分, B1分, B2分), ...] -> verdict() 吃的 results 结构。"""
    out = []
    for i, (a, b1, b2) in enumerate(pairs):
        out.append({"id": f"q{i}", "arms": {
            arm: {"score": s, "full_seats": full_seats, "judge_parse_ok": parse_ok}
            for arm, s in (("A", a), ("B1", b1), ("B2", b2))}})
    return out


def test_both_arms_pass_ties_on_net_takes_n2():
    """两组都过门槛且净改善并列 -> N=2 (表里写死的并列规则)。"""
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 4 + [(1.0, 0.0, 0.0)] * 1
                      + [(1.0, 1.0, 1.0)] * 7))
    assert v["arms"]["B1"]["net"] == 3 and v["arms"]["B2"]["net"] == 3
    assert (v["conclusion"], v["N"]) == ("FIX", 2)


def test_both_arms_pass_higher_net_wins():
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 5 + [(0.0, 1.0, 0.0)] * 1
                      + [(1.0, 1.0, 1.0)] * 6))
    assert v["arms"]["B1"]["net"] == 6 and v["arms"]["B2"]["net"] == 5
    assert (v["conclusion"], v["N"]) == ("FIX", 1)


def test_only_b1_passes_is_flagged_separately():
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 3 + [(0.0, 1.0, 0.0)] * 1
                      + [(1.0, 1.0, 0.0)] * 2 + [(1.0, 0.0, 1.0)] * 1
                      + [(1.0, 1.0, 1.0)] * 5))
    assert v["arms"]["B1"]["passes"] and not v["arms"]["B2"]["passes"]
    assert (v["conclusion"], v["N"]) == ("FIX_B1_ONLY", 1)


def test_neither_passes_is_no_fix():
    """两组净改善都不够 -> 不修, 跳过 Task 7。"""
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 3 + [(1.0, 0.0, 0.0)] * 2
                      + [(1.0, 1.0, 1.0)] * 7))
    assert v["arms"]["B1"]["net"] == 1 and not v["arms"]["B1"]["passes"]
    assert v["arms"]["B2"]["net"] == 1 and not v["arms"]["B2"]["passes"]
    assert (v["conclusion"], v["N"]) == ("NO_FIX_HARMLESS", None)


def test_harmless_row_with_regressed_le_1_is_unreachable_at_n12():
    """规则表的"均不过且 regressed 均 ≤1"这一行, 在 n=12 下**够不着**。

    tie < 8 要求非同分题 ≥5, 即 improved + regressed ≥ 5; 配上 regressed ≤ 1 就有
    improved ≥ 4, 于是 净改善 ≥ 3 —— 自动过门槛。所以 n=12 时 regressed ≤1 而又不
    过门槛的局面必然 tie ≥ 8, 先撞上作废规则。钉死它, 免得下一个人读表以为 12 题
    也能走到那一行。
    """
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 3 + [(1.0, 0.0, 0.0)] * 1
                      + [(1.0, 1.0, 1.0)] * 8))
    assert v["arms"]["B1"]["regressed"] == 1 and v["arms"]["B1"]["net"] == 2
    assert v["max_tie"] == 8
    assert v["conclusion"] == "VOID_TIE"


def test_harmless_row_is_reachable_at_the_n11_we_actually_run():
    """同一行在 n=11 (本轮实际题数) 下够得着 —— 差一题就换结论, 故两个 n 都钉死。

    n=11: tie ≤7 只要非同分题 ≥4, 配 regressed ≤1 得 improved ≥3, 净改善 ≥2 ——
    可以停在 2, 不过门槛而不撞作废。
    """
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 3 + [(1.0, 0.0, 0.0)] * 1
                      + [(1.0, 1.0, 1.0)] * 7))
    assert v["arms"]["B1"]["regressed"] == 1 and v["arms"]["B1"]["net"] == 2
    assert v["max_tie"] == 7 and not v["tie_aborts"]
    assert (v["conclusion"], v["N"]) == ("NO_FIX_HARMLESS", None)


def test_regressed_four_means_cluster_is_signal_do_not_fix():
    """任一组 regressed ≥4 -> 不修, 且要更正 spec 的假设。即使另一组净改善很高。"""
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 6 + [(1.0, 1.0, 0.0)] * 4
                      + [(1.0, 1.0, 1.0)] * 2))
    assert v["arms"]["B1"]["passes"] and v["arms"]["B2"]["regressed"] == 4
    assert (v["conclusion"], v["N"]) == ("NO_FIX_SIGNAL", None)


def test_eight_ties_voids_the_whole_layer():
    """同分 ≥8/12 -> 判定作废, 不许顺着读结论 (即便 B1 净改善过了门槛)。"""
    v = verdict(_rows([(0.0, 1.0, 1.0)] * 4 + [(1.0, 1.0, 1.0)] * 8))
    assert v["max_tie"] == 8 and v["tie_aborts"]
    assert (v["conclusion"], v["N"]) == ("VOID_TIE", None)


def test_short_seated_questions_never_enter_the_main_verdict():
    """硬 gate: 席位不满的题只进 fallback —— 这里它正好能把结论从"不修"翻成"修"。

    3 道不足席的题若混进来, B1 就是 improved=6 regressed=2 净改善=4 (过门槛);
    gate 挡掉后是 improved=3 regressed=2 净改善=1 (不过)。
    """
    short = _rows([(0.0, 1.0, 1.0)] * 3, full_seats=False)
    main = _rows([(0.0, 1.0, 1.0)] * 3 + [(1.0, 0.0, 0.0)] * 2 + [(1.0, 1.0, 1.0)] * 4)
    v = verdict(short + main)
    assert v["n_main"] == 9 and v["n_fallback"] == 3
    assert v["arms"]["B1"]["improved"] == 3 and v["arms"]["B1"]["net"] == 1
    assert v["conclusion"] == "NO_FIX_HARMLESS"


def test_unparsed_judge_scores_are_skipped_not_counted_as_tie():
    rows = _rows([(None, None, None)] * 2, parse_ok=False) + _rows([(1.0, 1.0, 1.0)] * 10)
    v = verdict(rows)
    assert v["n_judge_unparsed"] == 6
    assert v["arms"]["B1"]["skipped"] == 2 and v["arms"]["B1"]["tie"] == 10
