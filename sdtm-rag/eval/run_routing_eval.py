"""Plan B Phase 1 闸 1: 路由准确率三遍评测.

红线: 逐题明细 (含题目文本) 只写 data/study/st01/eval/runs/ (gitignored);
stdout 只打统计, 不打题目文本。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

from eval.run_eval import load_test_set
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router

CDISC_SET = Path("eval/test_set_v3.yml")
STUDY_SET = Path("data/study/st01/eval/test_set_study_v1_1.yml")
# 日语措辞的 CDISC 标准题: 原 gold 里语言与语料一一对应 (cdisc 全英/study 全日),
# 任何"按语言判库"的路由规则在那份 gold 上都无法被证伪 —— 本文件专门补上这个盲区。
JA_SUPP_SET = Path("eval/routing_gold_ja_supplement.yml")
RUNS_DIR = Path("data/study/st01/eval/runs")
EXACT_THRESHOLD = 0.95
VALID_GOLD = ("cdisc", "study", "both")


def load_supplement(path: Path) -> list[dict]:
    """读路由专用补充 gold (自带 gold 标签, 不走 load_test_set 的检索 gold 校验).

    缺文件直接 raise: 该文件是闸的一部分, 悄悄少几题 = 闸口变松却无人察觉。
    """
    if not path.exists():
        raise FileNotFoundError(f"路由补充 gold 缺失: {path} —— 闸口不完整, 拒绝继续")
    items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    out = []
    for q in items:
        if not q.get("id") or not q.get("question"):
            raise ValueError(f"{path}: 条目缺 id/question: {q!r}")
        if q.get("gold") not in VALID_GOLD:
            raise ValueError(f"{path}: {q['id']} 的 gold={q.get('gold')!r} 非法")
        out.append({"id": q["id"], "question": q["question"], "gold": q["gold"]})
    return out


def load_gold() -> list[dict]:
    items = [{"id": q["id"], "question": q["question"], "gold": "cdisc"}
             for q in load_test_set(str(CDISC_SET))]
    items += [{"id": f"st_{q['id']}", "question": q["question"], "gold": "study"}
              for q in load_test_set(str(STUDY_SET)) if not q.get("out_of_scope")]
    items += load_supplement(JA_SUPP_SET)
    ids = [g["id"] for g in items]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:  # predictions 以 id 为键, 重名会互相覆盖 → 静默改变计分
        raise ValueError(f"gold id 重复: {dupes}")
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
