"""U6 T9 可见集标定台 (eval/u6_calibrate_signals.py) 的测试.

**为什么这个文件存在**: 标定台是 Task 9 唯一的判据来源, 而它同时踩两条红线 ——
① 可见集纪律 (只许看 legacy + dev, 其余组全程封存); ② 零题面 (stdout / 产物不许带题面)。
两条都属于「错了也全绿」的形态: 多读一组题不会让任何断言变红, 打印题面也不会。
故本文件把两条都做成哨兵断言 (`QMARK` 出现在任何输出里即红; 组集恒等断言)。

第三件被钉死的是**离线模拟与真跑等价**: 标定不再跑 LLM, 而是把冻结基线的 pred 当成
router 输出重放。若 `simulate` 自己抄一份 widen 逻辑 (而不是走 `decide_corpus`),
白名单闸 / 方向闸 / 异常旁路三条契约就会在标定台上与生产不同 —— 标定出来的词表
是按一把假尺子选的。等价测试对**五种信号层破法**逐一比对两条路径。

零真实题面 / 零真实产物 / 零 LLM 请求: gold 与 run json 都是合成的。
"""
from __future__ import annotations

import json
import types

import pytest

from eval.u6_calibrate_signals import (
    VISIBLE_GROUPS,
    load_base_preds,
    render,
    simulate,
    visible_subset,
)
from server.federation import decide_corpus

# 红线哨兵: 只要它出现在 render / 产物里, 就是题面泄漏的形态
QMARK = "PLACEHOLDER-QUESTION-TEXT-DO-NOT-EMIT"


def gitem(qid, group, gold, q=QMARK):
    return {"id": qid, "group": group, "gold": gold, "question": q}


def mk_gold(**counts):
    """合成 gold: {group: [(id, gold), ...]} 展开。默认给一份两组齐全的最小集。"""
    out = []
    for group, items in counts.items():
        out += [gitem(qid, group, gold) for qid, gold in items]
    return out


MINIMAL = mk_gold(legacy=[("L1", "cdisc"), ("L2", "study")], dev=[("D1", "study")])


# ── 桩: 各种信号层破法 (等价测试用) ──────────────────────────────────

class Silent:
    def widen_reason(self, routed, question):
        return None


class FiresBothDirections:
    """方向正确的理由, 对两个单库判定都 fire (最大化 widen 面)。"""

    def widen_reason(self, routed, question):
        return {"cdisc": "study_sig", "study": "cdisc_sig"}.get(routed)


class FiresStudySigOnly:
    def widen_reason(self, routed, question):
        return "study_sig" if routed == "cdisc" else None


class NotWhitelisted:
    """返回库名而非理由 —— decide_corpus 必须拒收 (不拓宽)。"""

    def widen_reason(self, routed, question):
        return "study"


class WrongDirection:
    """同侧理由 (cdisc 判定 + cdisc 信号) —— 方向闸必须拒收。"""

    def widen_reason(self, routed, question):
        return {"cdisc": "cdisc_sig", "study": "study_sig"}.get(routed)


class Boom:
    def widen_reason(self, routed, question):
        raise RuntimeError("signal layer exploded")


ALL_STUBS = [Silent, FiresBothDirections, FiresStudySigOnly, NotWhitelisted, WrongDirection, Boom]


class EchoRouter:
    """测试自备的 router 桩 (不用被测模块那份): 恒返回给定 corpus 的合法 JSON。"""

    def __init__(self, corpus):
        self.corpus = corpus

    def completion(self, **kwargs):
        msg = types.SimpleNamespace(content=json.dumps({"corpus": self.corpus}))
        return types.SimpleNamespace(choices=[types.SimpleNamespace(message=msg)])


# ── ① visible_subset: 可见集纪律 ────────────────────────────────────

def test_visible_subset_keeps_only_legacy_and_dev():
    gold = MINIMAL + mk_gold(heldout=[("H1", "study")], ambiguous_both=[("A1", "both")],
                             final=[("F1", "study")], u1_doc=[("U1", "study")],
                             distractor_cdisc=[("X1", "cdisc")])
    out = visible_subset(gold)
    assert {g["group"] for g in out} == set(VISIBLE_GROUPS)
    assert [g["id"] for g in out] == ["L1", "L2", "D1"]


def test_visible_subset_preserves_items_verbatim():
    assert visible_subset(MINIMAL) == MINIMAL


@pytest.mark.parametrize("missing", ["legacy", "dev"])
def test_visible_subset_raises_when_a_visible_group_is_absent(missing):
    """一整组消失长得跟「这组本来就不存在」一样, 而 (a)/(b) 两条选择规则各自读一组 ——
    少一组等于那条规则恒真。必须响亮失败。"""
    gold = [g for g in MINIMAL if g["group"] != missing]
    with pytest.raises(ValueError, match=missing):
        visible_subset(gold)


def test_visible_subset_raises_on_empty_gold():
    with pytest.raises(ValueError):
        visible_subset([])


# ── ② load_base_preds: 只取可见 id ──────────────────────────────────

def mk_run(preds, path):
    detail = [{"id": qid, "group": grp, "gold": gold, "pred": pred, "question": QMARK}
              for qid, (grp, gold, pred) in preds.items()]
    path.write_text(json.dumps({"meta": {"generated_at": "t0"}, "summary": {}, "detail": detail},
                               ensure_ascii=False), encoding="utf-8")
    return path


def test_load_base_preds_drops_invisible_ids(tmp_path):
    """run json 的 detail 含全部 7 组。可见集纪律要求这层过滤在**读入处**发生 ——
    读进来再在打印处过滤, 中间任何一次调试打印都会把封存组带出来。"""
    p = mk_run({"L1": ("legacy", "cdisc", "cdisc"), "D1": ("dev", "study", "study"),
                "H1": ("heldout", "study", "cdisc"), "A1": ("ambiguous_both", "both", "study")},
               tmp_path / "run.json")
    out = load_base_preds(p, {"L1", "D1"})
    assert out == {"L1": "cdisc", "D1": "study"}


def test_load_base_preds_raises_when_a_visible_id_is_missing(tmp_path):
    p = mk_run({"L1": ("legacy", "cdisc", "cdisc")}, tmp_path / "run.json")
    with pytest.raises(ValueError, match="D1"):
        load_base_preds(p, {"L1", "D1"})


def test_load_base_preds_raises_on_invalid_pred(tmp_path):
    """pred 不是三个合法库之一时重放会 fallback 成 both, 而 fallback 长得跟一次拓宽一样。"""
    p = mk_run({"L1": ("legacy", "cdisc", "nonsense")}, tmp_path / "run.json")
    with pytest.raises(ValueError, match="L1"):
        load_base_preds(p, {"L1"})


# ── ③ simulate == decide_corpus (离线模拟与真跑等价) ────────────────

@pytest.mark.parametrize("stub", ALL_STUBS)
@pytest.mark.parametrize("pred", ["cdisc", "study", "both"])
def test_simulate_matches_decide_corpus_per_question(stub, pred):
    """五种破法 × 三种判定逐格比对。simulate 若自抄一份 widen 逻辑 (漏白名单闸 /
    漏方向闸 / 不吞异常), 这张表里必有一格不同。"""
    s = stub()
    gold = [gitem("L1", "legacy", "cdisc"), gitem("D1", "dev", "study")]
    rep = simulate(gold, {"L1": pred, "D1": pred}, s)
    expected_corpus, _, expected_reason = decide_corpus(EchoRouter(pred), QMARK, s)
    assert rep["sim_preds"] == {"L1": expected_corpus, "D1": expected_corpus}
    fired = {r for r, groups in rep["widen_fires"].items() for ids in groups.values() if ids}
    assert fired == ({expected_reason} if expected_reason else set())


def test_simulate_raises_when_a_base_pred_is_missing():
    with pytest.raises(ValueError, match="D1"):
        simulate(MINIMAL, {"L1": "cdisc", "L2": "study"}, Silent())


# ── ④ 计分与 fire 清单 ──────────────────────────────────────────────

def test_simulate_scores_baseline_and_widened_per_group():
    gold = mk_gold(legacy=[("L1", "cdisc"), ("L2", "study")], dev=[("D1", "study")])
    rep = simulate(gold, {"L1": "cdisc", "L2": "study", "D1": "study"}, FiresBothDirections())
    legacy, dev = rep["by_group"]["legacy"], rep["by_group"]["dev"]
    assert (legacy["n"], legacy["base_exact"], legacy["base_fatal"]) == (2, 2, 0)
    # 全部被拓宽成 both ⇒ 单库 gold 全部不再 exact, 但 both 不算 fatal (widen-only 构造)
    assert (legacy["sim_exact"], legacy["sim_fatal"], legacy["d_exact"]) == (0, 0, -2)
    assert (dev["base_exact"], dev["sim_exact"], dev["d_exact"]) == (1, 0, -1)


def test_widen_fire_ids_are_listed_by_signal_and_group():
    gold = mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "study")])
    rep = simulate(gold, {"L1": "cdisc", "D1": "study"}, FiresBothDirections())
    assert rep["widen_fires"]["study_sig"] == {"legacy": ["L1"], "dev": []}
    assert rep["widen_fires"]["cdisc_sig"] == {"legacy": [], "dev": ["D1"]}


def test_detector_fires_are_probed_independently_of_the_routed_corpus():
    """探针读的是「信号本身活着吗」(两个方向各问一次), 与该题实际判到哪库无关。
    只数 widen 的话, 一个活着但从没赶上对侧判定的信号会被读成死信号。"""
    gold = mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "study")])
    # study_sig 探针恒 fire, 但 D1 判到 study ⇒ 该题不会被拓宽
    rep = simulate(gold, {"L1": "study", "D1": "study"}, FiresStudySigOnly())
    assert rep["detector_fires"]["study_sig"] == {"legacy": ["L1"], "dev": ["D1"]}
    assert rep["detector_fires"]["cdisc_sig"] == {"legacy": [], "dev": []}
    assert rep["widen_fires"]["study_sig"] == {"legacy": [], "dev": []}


def test_gold_both_items_gain_exact_when_widened():
    """widen 的收益面: gold=both 而判成单库的题 (欠账形态) 被拓宽后转正, 且 fatal 减 1。"""
    gold = mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "both")])
    rep = simulate(gold, {"L1": "cdisc", "D1": "study"}, FiresBothDirections())
    assert rep["by_group"]["dev"]["base_fatal"] == 1
    assert (rep["by_group"]["dev"]["sim_exact"], rep["by_group"]["dev"]["sim_fatal"]) == (1, 0)


def test_simulate_never_creates_a_new_fatal():
    """widen-only 的构造保证: 拓宽只会把单库变 both, 而 both 永不计 fatal。"""
    gold = mk_gold(legacy=[("L1", "cdisc"), ("L2", "study")], dev=[("D1", "both")])
    rep = simulate(gold, {"L1": "study", "L2": "study", "D1": "study"}, FiresBothDirections())
    for g in rep["by_group"].values():
        assert g["sim_fatal"] <= g["base_fatal"]


# ── ⑤ 预登记选择规则三条 ────────────────────────────────────────────

def test_rule_a_fails_when_legacy_exact_drops():
    rep = simulate(mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "study")]),
                   {"L1": "cdisc", "D1": "study"}, FiresStudySigOnly())
    assert rep["rules"]["a_legacy_exact_not_lower"]["pass"] is False
    assert rep["accepted"] is False


def test_rule_a_passes_when_legacy_untouched():
    rep = simulate(mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "study")]),
                   {"L1": "cdisc", "D1": "study"}, Silent())
    assert rep["rules"]["a_legacy_exact_not_lower"]["pass"] is True


@pytest.mark.parametrize("n_dev_hit,expected", [(0, True), (1, True), (2, False)])
def test_rule_b_allows_at_most_one_dev_exact_drop(n_dev_hit, expected):
    dev_ids = [(f"D{i}", "study") for i in range(1, 4)]
    gold = mk_gold(legacy=[("L1", "cdisc")], dev=dev_ids)

    class HitFirstN:
        def __init__(self, ids):
            self.ids = ids

        def widen_reason(self, routed, question):
            return "cdisc_sig" if routed == "study" and question in self.ids else None

    hit = {f"D{i}" for i in range(1, n_dev_hit + 1)}
    gold = [{**g, "question": g["id"]} for g in gold]      # 让桩按 id 命中
    preds = {"L1": "cdisc", **{f"D{i}": "study" for i in range(1, 4)}}
    rep = simulate(gold, preds, HitFirstN(hit))
    assert rep["rules"]["b_dev_exact_drop_le_1"]["pass"] is expected


def test_rule_c_reports_both_readings_and_marks_the_operative_one():
    """(c) 有两种读法: widen 计数 (拓宽真的发生了) vs 探针计数 (信号本身活着)。
    两者都必须出现在报告里 —— 只报一个数就等于把读法藏进实现。"""
    rep = simulate(MINIMAL, {"L1": "cdisc", "L2": "study", "D1": "study"}, Silent())
    rules = rep["rules"]
    assert set(rules) == {"a_legacy_exact_not_lower", "b_dev_exact_drop_le_1",
                          "c_both_signals_alive_widen", "c_both_signals_alive_detect"}
    assert rep["c_rule_reading"] in ("widen", "detect")
    assert rules[f"c_both_signals_alive_{rep['c_rule_reading']}"]["operative"] is True
    other = "widen" if rep["c_rule_reading"] == "detect" else "detect"
    assert rules[f"c_both_signals_alive_{other}"]["operative"] is False


def test_rule_c_dead_signal_fails():
    rep = simulate(MINIMAL, {"L1": "cdisc", "L2": "study", "D1": "study"}, Silent())
    assert rep["rules"]["c_both_signals_alive_detect"]["pass"] is False
    assert rep["accepted"] is False


def test_accepted_requires_all_three_rules():
    """两个信号探针都活着 + 零 widen ⇒ 三条全过。这是标定的目标形态。"""
    gold = mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "study")])
    gold = [{**g, "question": g["id"]} for g in gold]

    class AliveButNeverWidens:
        """L1 判 cdisc 而只有 cdisc 探针命中 / D1 判 study 而只有 study 探针命中 ⇒
        两个探针都活着, 但方向都对不上, 一次拓宽都不发生。"""

        def widen_reason(self, routed, question):
            if routed == "study" and question == "L1":
                return "cdisc_sig"
            if routed == "cdisc" and question == "D1":
                return "study_sig"
            return None

    rep = simulate(gold, {"L1": "cdisc", "D1": "study"}, AliveButNeverWidens())
    assert all(r["pass"] for k, r in rep["rules"].items() if not k.startswith("c_")
               or r["operative"])
    assert rep["accepted"] is True
    assert rep["rules"]["c_both_signals_alive_widen"]["pass"] is False   # widen 读法下不成立


# ── ⑥ 红线: 输出零题面 ──────────────────────────────────────────────

def test_render_emits_no_question_text():
    gold = mk_gold(legacy=[("L1", "cdisc"), ("L2", "study")], dev=[("D1", "study")])
    rep = simulate(gold, {"L1": "cdisc", "L2": "study", "D1": "study"}, FiresBothDirections())
    text = "\n".join(render(rep))
    assert QMARK not in text
    assert "L1" in text and "D1" in text          # id 该出现 (定位用)
    assert "legacy" in text and "dev" in text


def test_report_carries_no_question_text():
    """报告 dict 本身也不许带题面 —— 它会被序列化进 evidence / --json-out。"""
    gold = mk_gold(legacy=[("L1", "cdisc")], dev=[("D1", "study")])
    rep = simulate(gold, {"L1": "cdisc", "D1": "study"}, FiresBothDirections())
    assert QMARK not in json.dumps(rep, ensure_ascii=False)
