"""Plan B Phase 1 闸 1: 路由准确率三遍评测.

红线: 逐题明细 (含题目文本) 只写 data/study/st01/eval/runs/ (gitignored);
stdout 只打统计, 不打题目文本。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from eval.run_eval import load_test_set
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router

CDISC_SET = Path("eval/test_set_v3.yml")
STUDY_SET = Path("data/study/st01/eval/test_set_study_v1_1.yml")
RUNS_DIR = Path("data/study/st01/eval/runs")
EXACT_THRESHOLD = 0.95


def load_gold() -> list[dict]:
    items = [{"id": q["id"], "question": q["question"], "gold": "cdisc"}
             for q in load_test_set(str(CDISC_SET))]
    items += [{"id": f"st_{q['id']}", "question": q["question"], "gold": "study"}
              for q in load_test_set(str(STUDY_SET)) if not q.get("out_of_scope")]
    return items


def score_run(gold: list[dict], predictions: dict[str, str]) -> dict:
    exact = 0
    fatal_items = []
    for g in gold:
        pred = predictions.get(g["id"])
        if pred == g["gold"]:
            exact += 1
        elif pred != "both":  # 错的单库 or 缺失: 该题 recall 归零, 致命
            fatal_items.append({"id": g["id"], "gold": g["gold"], "pred": pred})
    acc = exact / len(gold)
    return {"n": len(gold), "exact": exact, "exact_acc": round(acc, 4),
            "fatal": len(fatal_items), "fatal_items": fatal_items,
            "passed": acc >= EXACT_THRESHOLD and not fatal_items}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=3)
    args = parser.parse_args(argv)
    gold = load_gold()
    llm = create_router(settings)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    all_passed = True
    per_run_preds: list[dict[str, str]] = []
    for run_i in range(1, args.runs + 1):
        preds: dict[str, str] = {}
        n_fallback = 0
        for g in gold:
            corpus, fallback = route_corpus(llm, g["question"])
            preds[g["id"]] = corpus
            n_fallback += fallback
        s = score_run(gold, preds)
        per_run_preds.append(preds)
        detail = [{**g, "pred": preds[g["id"]]} for g in gold]
        (RUNS_DIR / f"routing_run_{run_i}.json").write_text(
            json.dumps({"summary": {k: v for k, v in s.items() if k != "fatal_items"},
                        "detail": detail}, ensure_ascii=False, indent=1))
        print(f"run {run_i}: exact {s['exact']}/{s['n']} = {s['exact_acc']:.1%}  "
              f"fatal={s['fatal']}  fallback={n_fallback}  "
              f"{'PASS' if s['passed'] else 'FAIL'}")
        all_passed &= s["passed"]

    stable = sum(
        1 for g in gold
        if len({p[g["id"]] for p in per_run_preds}) == 1
    )
    print(f"stability: {stable}/{len(gold)} 题三遍判定一致")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
