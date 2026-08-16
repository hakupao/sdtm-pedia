"""eval/u5_verdict.py 单测 — 全合成 fixture, 判定逻辑逐条钉死 (U3 §6-10 教训:
判定脚本零测试 = 结论可翻不留痕). 变异集含对调型 (U2 §4.1 方向③)."""
import json

import pytest

from eval.u5_verdict import (
    EXPECTED_N,
    FRAGILE_4,
    I1_MIN_SAME_RATE,
    I2_MAX_UNSTABLE,
    I3_NEG_MAX,
    I3_POS_MIN,
    build_verdict,
    main,
    paired_effect,
    scores_by_id,
    stability,
)


def test_frozen_thresholds_are_literal():
    """T5 后判据冻结: 常量被改必须有人看见 (测试 import 常量 ⇒ 常量自身无守卫)."""
    assert (I1_MIN_SAME_RATE, I3_POS_MIN, I3_NEG_MAX) == (0.95, 0.80, 0.20)
    assert I2_MAX_UNSTABLE == {"cards": 7, "docs": 4}
    assert EXPECTED_N == {"cards": 48, "docs": 30}
    assert FRAGILE_4 == ("st01_v11_q19", "st01_v2_q14", "st01_v2_q15", "st01_v2_q21")


def _mkrun(scores: dict, n: int, judge_model: str = "stub-judge"):
    """scores: id -> float (judge 分) | None (parse 失败)."""
    return {"summary": {"n_questions": n, "judge_model": judge_model},
            "results": [{"id": i, "judge_fact_recall": (s if s is not None else 0.0),
                         "judge_parse_ok": s is not None} for i, s in scores.items()]}


def _pad(scores: dict, fam: str) -> dict:
    """补足到 EXPECTED_N[fam] 行. 填充题两侧同为 1.0 —— 对 cost/gain 与稳定性计数皆中性,
    只为满足行数闸 (审查 M3)."""
    out = dict(scores)
    i = 0
    while len(out) < EXPECTED_N[fam]:
        out.setdefault(f"_pad{i}", 1.0)
        i += 1
    return out


def _mkfull(scores: dict, fam: str, **kw):
    """行数与表头都合规的 run (build_verdict 级 fixture 用)."""
    return _mkrun(_pad(scores, fam), EXPECTED_N[fam], **kw)


def test_scores_by_id_none_on_parse_fail_and_skips_oos():
    run = _mkrun({"a": 1.0, "b": None}, n=2)
    run["results"].append({"id": "c", "out_of_scope": True, "judge_fact_recall": 1.0,
                          "judge_parse_ok": True})
    assert scores_by_id(run) == {"a": 1.0, "b": None}


def _ctl(mode: str, avg: float, n_ok: int = 6, n_rows: int = 6):
    """judge_controls 产物形状 (eval/judge_controls.py:57,64): mode 只带极性不带家族;
    parse 失败行的 recall 为 None (`verdict is None` 时不落分)."""
    return {"mode": mode, "avg": avg,
            "rows": [{"id": f"c{i}", "recall": avg if i < n_ok else None,
                      "parse_ok": i < n_ok} for i in range(n_rows)]}


def test_stability_flags_flip_and_parse_fail():
    r_ok = _mkrun({"a": 1.0, "b": 0.5, "c": 1.0}, n=48)
    r_flip = _mkrun({"a": 1.0, "b": 1.0, "c": 1.0}, n=48)      # b 翻转
    r_pf = _mkrun({"a": 1.0, "b": 0.5, "c": None}, n=48)       # c parse 失败
    stable, unstable = stability([r_ok, r_flip, r_pf])
    assert stable == {"a": 1.0}
    assert unstable == ["b", "c"]


def test_stability_flags_question_that_parse_failed_every_run():
    """三遍全 parse 失败 = 三遍"同值"(都 None) —— 必须进不稳定, 不能因同值被判稳定
    (复审 N5: 去掉 `None in vals` 这条的变异否则存活)."""
    stable, unstable = stability([_mkrun({"a": 1.0, "z": None}, n=48)] * 3)
    assert stable == {"a": 1.0}
    assert unstable == ["z"]


def test_stability_rejects_mismatched_question_sets():
    # SystemExit 而非 assert: python -O 会剥掉裸 assert, 静默放行 (审查 L1)
    with pytest.raises(SystemExit):
        stability([_mkrun({"a": 1.0}, n=48), _mkrun({"b": 1.0}, n=48),
                   _mkrun({"a": 1.0}, n=48)])


def test_paired_effect_two_sided_and_pt_math():
    a = {"q1": 1.0, "q2": 1.0, "q3": 0.5}
    b = {"q1": 0.5, "q2": 1.0, "q3": 1.0}
    e = paired_effect(a, b, n_scored=48)
    assert e["confirmed_cost_ids"] == ["q1"] and e["confirmed_gain_ids"] == ["q3"]
    assert e["confirmed_cost_pt"] == round(100 * 0.5 / 48, 2)   # 1.04pt
    assert e["confirmed_gain_pt"] == round(100 * 0.5 / 48, 2)


def test_paired_effect_swap_symmetry():
    # 对调型守卫: 输入对调后 cost/gain 必须互换 (集合断言的系统性盲区)
    a, b = {"q1": 1.0}, {"q1": 0.0}
    assert paired_effect(a, b, 48)["confirmed_cost_ids"] == \
           paired_effect(b, a, 48)["confirmed_gain_ids"] == ["q1"]


def _happy_inputs(cards_both_scores=None):
    cs = {f"q{i}": 1.0 for i in range(4)}
    cb = cards_both_scores or dict(cs)
    ds = {f"d{i}": 1.0 for i in range(3)}
    runs = {"cards_study": [_mkfull(cs, "cards")] * 3, "cards_both": [_mkfull(cb, "cards")] * 3,
            "docs_study": [_mkfull(ds, "docs")] * 3, "docs_both": [_mkfull(ds, "docs")] * 3}
    probes = {"cards": {"same_rate": 1.0, "n": 48, "n_orig_parse_fail": 0},
              "docs": {"same_rate": 1.0, "n": 30, "n_orig_parse_fail": 0}}
    controls = {"docs_positive": _ctl("positive", 1.0), "docs_negative": _ctl("negative", 0.0),
                "cards_positive": _ctl("positive", 1.0), "cards_negative": _ctl("negative", 0.0)}
    return runs, probes, controls


def test_build_verdict_happy_path_cheap():
    v, rc = build_verdict(*_happy_inputs())
    assert rc == 0 and v["E2_verdict"] == "cheap_on_this_ruler"
    assert v["I1"]["pass"] and v["I2"]["pass"] and v["I3"]["pass"]
    assert v["advisory_only"] is False


def test_build_verdict_cost_reported():
    cb = {"q0": 0.5, "q1": 1.0, "q2": 1.0, "q3": 1.0}
    v, rc = build_verdict(*_happy_inputs(cards_both_scores=cb))
    assert rc == 0 and v["E2_verdict"] == "cost_reported"
    assert v["E"]["cards"]["confirmed_cost_ids"] == ["q0"]


def test_build_verdict_cost_reported_when_pt_rounds_to_zero():
    """代价小到 round 2 位舍成 0.0pt 也必须 cost_reported —— 判 cheap 的依据是
    已确证代价集合为空, 不是 pt 读数 (审查 M1: 否则产物自相矛盾)."""
    cb = {"q0": 0.999, "q1": 1.0, "q2": 1.0, "q3": 1.0}
    v, rc = build_verdict(*_happy_inputs(cards_both_scores=cb))
    assert v["E"]["cards"]["confirmed_cost_pt"] == 0.0
    assert v["E"]["cards"]["confirmed_cost_ids"] == ["q0"]
    assert rc == 0 and v["E2_verdict"] == "cost_reported"


def test_build_verdict_i2_trigger_blocks_e():
    runs, probes, controls = _happy_inputs()
    # cards 阈值是绝对数 7 — 用 8 题全翻钉死触发:
    big = {f"q{i}": 1.0 for i in range(8)}
    big_flip = {f"q{i}": 0.0 for i in range(8)}
    runs["cards_study"] = [_mkfull(big, "cards"), _mkfull(big_flip, "cards"),
                           _mkfull(big, "cards")]
    runs["cards_both"] = [_mkfull(big, "cards")] * 3
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 2 and v["E"] is None and v["E2_verdict"] == "instrument_unusable"


def test_build_verdict_i3_trigger():
    runs, probes, controls = _happy_inputs()
    controls["cards_negative"] = _ctl("negative", 0.5)          # 阴性对照失守
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 2 and v["E2_verdict"] == "controls_failed" and v["E"] is None


def test_build_verdict_rejects_wrong_controls_keys():
    """错键名 → 两个 all() 零迭代 → 完全反转的阴性对照也能 pass (审查 H1)."""
    runs, probes, controls = _happy_inputs()
    del controls["cards_negative"]
    controls["cards_neg"] = _ctl("negative", 1.0)               # 完全反转 + 错键名
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_missing_control_key():
    """纯缺键 (非改名): 键集断言若从 != 弱化成 ⊆ 就漏 (复审 N4)."""
    runs, probes, controls = _happy_inputs()
    del controls["cards_negative"]
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_swapped_control_polarity():
    """阳阴两份产物对调塞错 flag = 唯一的静默假过路径: 真实阳性 0.1 / 阴性 0.9 (管线已坏),
    对调后两边都"合格" → I3 反判 pass. 靠 mode 断言关掉 (复审 极性半)."""
    runs, probes, controls = _happy_inputs()
    controls["cards_positive"] = _ctl("negative", 0.9)          # 阴性产物塞进阳性位
    controls["cards_negative"] = _ctl("positive", 0.1)          # 阳性产物塞进阴性位
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_control_with_zero_parsed_rows():
    """6 行全 parse 失败 → avg 兜底成 0.0, 阴性对照会"完美通过" —— 零信息不是证据
    (复审 N1, 与 probe n=0 同类病)."""
    runs, probes, controls = _happy_inputs()
    controls["cards_negative"] = _ctl("negative", 0.0, n_ok=0)
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_missing_probe_keys():
    """probes 为空 → all([]) is True → I1 空过 (审查 H1)."""
    runs, _, controls = _happy_inputs()
    with pytest.raises(SystemExit):
        build_verdict(runs, {}, controls)


def test_build_verdict_i1_degrades_to_advisory():
    runs, probes, controls = _happy_inputs()
    probes["docs"] = {"same_rate": 0.90, "n": 30, "n_orig_parse_fail": 0}
    v, rc = build_verdict(runs, probes, controls)
    assert rc == 3 and v["advisory_only"] is True and v["E"] is not None


def test_i1_records_denominator_and_parse_fail():
    """same_rate 单独看无意义 —— 分母与被排除行数必须同落盘 (审查 M2)."""
    runs, probes, controls = _happy_inputs()
    probes["cards"] = {"same_rate": 1.0, "n": 46, "n_orig_parse_fail": 2}
    v, _ = build_verdict(runs, probes, controls)
    assert v["I1"]["n"] == {"cards": 46, "docs": 30}
    assert v["I1"]["n_orig_parse_fail"] == {"cards": 2, "docs": 0}


def test_build_verdict_requires_probe_parse_fail_count():
    """N6 硬下标的守卫: 缺 n_orig_parse_fail 必须炸, 不能静默落 None 进归档 (复审 LOW)."""
    runs, probes, controls = _happy_inputs()
    p = dict(probes["cards"])
    del p["n_orig_parse_fail"]
    probes["cards"] = p
    with pytest.raises(KeyError):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_probe_n_zero():
    """probe n=0 时 rejudge_run 会吐 same_rate=0.0 (无意义值) — 必须炸而不是当 I1 失守.
    (Task 2 复审遗留: same_rate 读数须与 n 同看)"""
    runs, probes, controls = _happy_inputs()
    probes["docs"] = {"same_rate": 0.0, "n": 0, "n_orig_parse_fail": 30}
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_wrong_n():
    """表头闸独占覆盖: 行数合规 (48), 只有 n_questions 不对 —— 否则删掉表头闸也全绿
    (复审 N3)."""
    runs, probes, controls = _happy_inputs()
    bad = _mkfull({f"q{i}": 1.0 for i in range(4)}, "cards")
    bad["summary"]["n_questions"] = 47                          # 题集变了 = 阈值失义
    runs["cards_study"] = [bad] * 3
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_row_count_mismatch():
    """表头 n_questions 对但实际计分行数不对 = 产物残缺 (审查 M3)."""
    runs, probes, controls = _happy_inputs()
    runs["cards_study"] = [_mkrun({"q0": 1.0}, EXPECTED_N["cards"])] * 3
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_build_verdict_rejects_run_without_judge():
    """漏 --judge 的 run 全行无 judge_parse_ok → 会被误诊成 instrument_unusable (审查 M4)."""
    runs, probes, controls = _happy_inputs()
    r = _mkfull({f"q{i}": 1.0 for i in range(4)}, "cards")
    del r["summary"]["judge_model"]
    runs["cards_study"] = [r] * 3
    with pytest.raises(SystemExit):
        build_verdict(runs, probes, controls)


def test_fragile_and_undecidable_reported():
    runs, probes, controls = _happy_inputs()
    cs = {FRAGILE_4[0]: 1.0, "x": 1.0}
    cb = {FRAGILE_4[0]: 0.5, "x": 1.0}
    runs["cards_study"] = [_mkfull(cs, "cards")] * 3
    runs["cards_both"] = [_mkfull(cb, "cards")] * 3
    v, _ = build_verdict(runs, probes, controls)
    f = v["E3_fragile"][FRAGILE_4[0]]
    assert (f["study"], f["both"], f["stable_study"], f["stable_both"]) == (1.0, 0.5, True, True)
    assert v["E4_undecidable"] == {"cards": [], "docs": []}


# ---- 冻结阈值的边界 (复审 N2): 各钉 "== 阈值 ⇒ pass" 与 "越界一步 ⇒ fail".
# T5 付费跑批后判据即冻结, 边界一旦松动没人会再发现 ----

@pytest.mark.parametrize(("same_rate", "expect_pass"), [(0.95, True), (0.9499, False)])
def test_i1_threshold_boundary(same_rate, expect_pass):
    runs, probes, controls = _happy_inputs()
    probes["docs"] = {"same_rate": same_rate, "n": 30, "n_orig_parse_fail": 0}
    v, rc = build_verdict(runs, probes, controls)
    assert v["I1"]["pass"] is expect_pass
    assert rc == (0 if expect_pass else 3)


@pytest.mark.parametrize(("n_unstable", "expect_pass"), [(7, True), (8, False)])
def test_i2_threshold_boundary(n_unstable, expect_pass):
    runs, probes, controls = _happy_inputs()
    base = {f"q{i}": 1.0 for i in range(n_unstable)}
    flip = {f"q{i}": 0.0 for i in range(n_unstable)}
    runs["cards_study"] = [_mkfull(base, "cards"), _mkfull(flip, "cards"),
                           _mkfull(base, "cards")]
    runs["cards_both"] = [_mkfull(base, "cards")] * 3
    v, rc = build_verdict(runs, probes, controls)
    assert v["I2"]["counts"]["cards_study"] == n_unstable
    assert v["I2"]["pass"] is expect_pass
    assert rc == (0 if expect_pass else 2)


@pytest.mark.parametrize(("avg", "expect_pass"), [(0.80, True), (0.7999, False)])
def test_i3_positive_threshold_boundary(avg, expect_pass):
    runs, probes, controls = _happy_inputs()
    controls["cards_positive"] = _ctl("positive", avg)
    v, rc = build_verdict(runs, probes, controls)
    assert v["I3"]["pass"] is expect_pass
    assert rc == (0 if expect_pass else 2)


@pytest.mark.parametrize(("avg", "expect_pass"), [(0.20, True), (0.2001, False)])
def test_i3_negative_threshold_boundary(avg, expect_pass):
    runs, probes, controls = _happy_inputs()
    controls["cards_negative"] = _ctl("negative", avg)
    v, rc = build_verdict(runs, probes, controls)
    assert v["I3"]["pass"] is expect_pass
    assert rc == (0 if expect_pass else 2)


# ---- main() 级: CLI 接线 / 对照身份绑定 / rc 传播 (审查 M5) ----

def _write_json(tmp_path, name: str, obj) -> str:
    p = tmp_path / f"{name}.json"
    p.write_text(json.dumps(obj), encoding="utf-8")
    return str(p)


def _main_argv(tmp_path, probe_cards=None, controls=None):
    cs = {f"q{i}": 1.0 for i in range(4)}
    ds = {f"d{i}": 1.0 for i in range(3)}
    argv = []
    for flag, sc, fam in (("--cards-study", cs, "cards"), ("--cards-both", cs, "cards"),
                          ("--docs-study", ds, "docs"), ("--docs-both", ds, "docs")):
        stem = flag.lstrip("-").replace("-", "_")
        argv.append(flag)
        argv += [_write_json(tmp_path, f"{stem}_{k}", _mkfull(sc, fam)) for k in range(3)]
    argv += ["--probe-cards",
             _write_json(tmp_path, "probe_cards",
                         probe_cards or {"n": 48, "same_rate": 1.0, "n_orig_parse_fail": 0}),
             "--probe-docs",
             _write_json(tmp_path, "probe_docs",
                         {"n": 30, "same_rate": 1.0, "n_orig_parse_fail": 0})]
    # 四个 avg 刻意互不相同: 家族或极性传错会在 I3.avg 上现形
    ctl = controls or {"docs-pos": 0.9, "docs-neg": 0.1, "cards-pos": 0.85, "cards-neg": 0.05}
    for k, v in ctl.items():
        mode = "positive" if k.endswith("-pos") else "negative"
        argv += [f"--controls-{k}",
                 _write_json(tmp_path, f"ctl_{k.replace('-', '_')}", _ctl(mode, v))]
    argv += ["--output", str(tmp_path / "verdict.json")]
    return argv


def test_main_happy_binds_control_identity(tmp_path):
    argv = _main_argv(tmp_path)
    assert main(argv) == 0
    v = json.loads((tmp_path / "verdict.json").read_text(encoding="utf-8"))
    assert v["I3"]["avg"] == {"docs_positive": 0.9, "docs_negative": 0.1,
                             "cards_positive": 0.85, "cards_negative": 0.05}
    assert v["I3"]["pass"] and v["E2_verdict"] == "cheap_on_this_ruler"


def test_main_missing_control_flag_exits(tmp_path):
    argv = _main_argv(tmp_path)
    i = argv.index("--controls-cards-neg")
    del argv[i:i + 2]                                          # 少一个对照 = 必须炸
    with pytest.raises(SystemExit):
        main(argv)


def test_main_bad_probe_exits(tmp_path):
    argv = _main_argv(tmp_path,
                      probe_cards={"n": 0, "same_rate": 0.0, "n_orig_parse_fail": 48})
    with pytest.raises(SystemExit):
        main(argv)
