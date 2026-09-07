"""compare_verified_runs 严格口径聚合 (Rule D 审阅 F1/F2/F3/F4 + 复核规则 4)。零 LLM。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "eval"))

from compare_verified_runs import (  # noqa: E402
    TAGS, aggregate_j1, aggregate_j2, best_by_rank, perm_for, rank_valid, self_destruct)

CATS = {f"q{i}": "concept" for i in range(10)}


def _row(qid, ranks, best=None, order=None, ok=True):
    r = {"id": qid, "seed": 0, "order": order or TAGS[:], "parse_ok": ok}
    if ok:
        r["rank"] = dict(zip(TAGS, ranks))
        r["best"] = best or best_by_rank(r)
    return r


def test_rank_invalid_rows_are_excluded_and_counted_separately():
    """F2: 并列 / 越界秩不进 n_ok, 也不混进 parse_fail。若不校验, 并列会压胜率与 mean rank。"""
    rows = [_row("q0", [1, 2, 3, 4]), _row("q1", [1, 1, 3, 4]), _row("q2", [0, 1, 2, 3]),
            _row("q3", None, ok=False)]
    j = aggregate_j1(rows, CATS)
    assert (j["n_ok"], j["n_rank_invalid"], j["n_parse_fail"]) == (1, 2, 1)


def test_best_is_taken_from_rank1_not_judge_self_report():
    """F1: 裁判自报 best 与 rank-1 打架时, 聚合只信秩; 打架次数落盘。"""
    rows = [_row("q0", [2, 1, 3, 4], best="opus-5")]  # 自报 opus-5, 但 rank-1 是 sonnet-5
    j = aggregate_j1(rows, CATS)
    assert j["rank1"]["sonnet-5"] == 1 and j["rank1"]["opus-5"] == 0
    assert j["n_best_mismatch"] == 1


def test_pairwise_wins_are_complementary_when_ranks_valid():
    rows = [_row("q0", [1, 2, 3, 4]), _row("q1", [4, 3, 2, 1])]
    j = aggregate_j1(rows, CATS)
    assert j["pairwise_wins"]["opus-5"]["gpt-sol"] + j["pairwise_wins"]["gpt-sol"]["opus-5"] == 2
    assert j["pairwise_winrate"]["opus-5"]["gpt-sol"] == 0.5


def test_j2_same_denominator_and_same_perm_sensitivity():
    """F3/F4: best_agree 与 τ 同分母 (两轮都秩合法); 同置换题单列并给剔除后的值。"""
    o1, o2 = TAGS[:], list(reversed(TAGS))
    r0 = [_row("q0", [1, 2, 3, 4], order=o1), _row("q1", [1, 2, 3, 4], order=o1), _row("q2", [1, 1, 3, 4])]
    r1 = [_row("q0", [1, 2, 3, 4], order=o1), _row("q1", [2, 1, 3, 4], order=o2), _row("q2", [1, 2, 3, 4])]
    j = aggregate_j2(r0, r1)
    assert j["n_both"] == 2 and j["n_partial_dropped"] == 1
    assert j["best_agree"] == 0.5 and j["same_perm_ids"] == ["q0"]
    assert j["best_agree_excl_same_perm"] == 0.0


def test_c2_uses_the_lower_of_the_two_agreement_values():
    """复核规则 4 (数据前写死): C2 以 best_agree 与剔除同置换后的值中较低者判。
    分辨力: 只看 best_agree (0.72) 不会触发; 取较低者 (0.65) 必须触发。"""
    j1 = {"n_parse_fail": 0, "n_rank_invalid": 0, "n_ok": 10, "best_pos_dist": {"A": 3, "B": 3, "C": 2, "D": 2},
          "mean_rank": {"opus-5": 1.0, "sonnet-5": 2.0, "gpt-terra": 3.0, "gpt-sol": 4.0}}
    j2 = {"best_agree": 0.72, "best_agree_excl_same_perm": 0.65}
    j3 = {t: {"parse_fail": 0} for t in TAGS}
    hits = self_destruct(j1, j1, j2, j3)
    assert any(h.startswith("C2") for h in hits)
    j2b = {"best_agree": 0.72, "best_agree_excl_same_perm": 0.71}
    assert not any(h.startswith("C2") for h in self_destruct(j1, j1, j2b, j3))


def test_perm_for_avoid_guarantees_a_different_permutation():
    """F4: seed1 置换若与 seed0 撞车必须重摇。q41/q54/q72/q75 是本轮实测撞车的四题。"""
    for q in ("q41", "q54", "q72", "q75"):
        o0 = perm_for(q, 0)
        assert perm_for(q, 1) == o0, f"{q} 本应撞车 (审阅实测), 若不撞说明置换算法变了"
        assert perm_for(q, 1, avoid=o0) != o0
    assert rank_valid({"parse_ok": True, "rank": dict(zip(TAGS, [1, 2, 3, 4]))})
