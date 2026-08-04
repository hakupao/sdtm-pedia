"""Plan B Phase 1 闸 1: 路由打分逻辑. LLM 调用不进单测 (真实三遍在 eval 执行)."""
from eval.run_routing_eval import score_run

GOLD = [{"id": "q1", "gold": "cdisc"}, {"id": "q2", "gold": "study"},
        {"id": "q3", "gold": "study"}, {"id": "q4", "gold": "cdisc"}]


def test_all_exact():
    s = score_run(GOLD, {"q1": "cdisc", "q2": "study", "q3": "study", "q4": "cdisc"})
    assert s["exact_acc"] == 1.0 and s["fatal"] == 0 and s["passed"] is True


def test_both_is_nonfatal_but_not_exact():
    s = score_run(GOLD, {"q1": "cdisc", "q2": "both", "q3": "study", "q4": "cdisc"})
    assert s["exact_acc"] == 0.75 and s["fatal"] == 0
    assert s["passed"] is False  # 0.75 < 0.95


def test_wrong_single_corpus_is_fatal_both_directions():
    s = score_run(GOLD, {"q1": "study", "q2": "cdisc", "q3": "study", "q4": "cdisc"})
    assert s["fatal"] == 2 and s["passed"] is False
    assert {f["id"] for f in s["fatal_items"]} == {"q1", "q2"}


def test_missing_prediction_counts_fatal():
    # 断题 (LLM 全挂被 route_corpus 兜成 both 之外的缺失) 不许静默
    s = score_run(GOLD, {"q1": "cdisc", "q2": "study", "q3": "study"})
    assert s["fatal"] >= 1
