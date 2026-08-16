"""对已落盘 run json 的存量答案重跑 judge (不重新答题) — U5 仪器闸 I1 的探针.

把「judge 自身噪声」从「答题噪声」里分解出来. 输入 run 必须带全文答案
(--full-answers 跑出的 "answer" 字段), 否则 fail loud. 产物零题面: 只存 id 与数字.
"""
from __future__ import annotations

import argparse
import json

from eval.run_eval import DEFAULT_JUDGE_MODEL, check_fact_recall_judge, load_test_set


def rejudge(run: dict, facts_by_id: dict[str, list[str]], judge_model: str) -> dict:
    rows = []
    for r in run["results"]:
        if r.get("out_of_scope"):
            continue
        if "answer" not in r:
            raise SystemExit(
                f"{r['id']}: run json 无全文答案 — 不是 --full-answers 跑出的, I1 探针无法执行")
        if not r.get("judge_parse_ok", False):
            # 原 run 的 judge 没 parse 成功时 run_eval 把 judge_fact_recall 回落成
            # substring 分 (系统性低估). 拿它当 orig 比, 量到的是跨口径分歧却会被读成
            # judge 自噪声 —— 整行排除出 same_rate 分母, 单列计数.
            # 缺 judge_parse_ok 键 (非 --judge 跑的 / 旧版产物) 同样排除: 不能证明
            # orig 是真语义分就不拿它当基准.
            rows.append({"id": r["id"], "orig_parse_fail": True})
            continue
        verdict = check_fact_recall_judge(
            r["question"], r["answer"], facts_by_id[r["id"]], judge_model)
        if verdict is None:
            rows.append({"id": r["id"], "orig": r["judge_fact_recall"],
                         "rejudged": None, "same": False, "parse_fail": True})
            continue
        recall = round(verdict[0], 4)
        rows.append({"id": r["id"], "orig": r["judge_fact_recall"],
                     "rejudged": recall, "same": recall == r["judge_fact_recall"],
                     "parse_fail": False})
    scored = [r for r in rows if not r.get("orig_parse_fail")]
    n_same = sum(r["same"] for r in scored)
    return {"n": len(scored), "n_same": n_same,
            "same_rate": round(n_same / len(scored), 4) if scored else 0.0,
            "n_orig_parse_fail": len(rows) - len(scored), "rows": rows}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("run_json")
    p.add_argument("test_set")
    p.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    p.add_argument("--output", required=True)
    a = p.parse_args(argv)
    with open(a.run_json, encoding="utf-8") as f:
        run = json.load(f)
    # 模型不一致 = 测的是跨模型分歧, 不是同模型自噪声. 直接下标: summary 缺 judge_model
    # (非 --judge 跑出的 run) 同样炸.
    run_model = run["summary"]["judge_model"]
    if run_model != a.judge_model:
        raise SystemExit(
            f"judge model mismatch: run={run_model!r} vs --judge-model={a.judge_model!r}")
    facts_by_id = {q["id"]: q["expected_facts"] for q in load_test_set(a.test_set)}
    out = rejudge(run, facts_by_id, a.judge_model)
    print(f"rejudge n={out['n']} same={out['n_same']} same_rate={out['same_rate']:.4f}"
          f" orig_parse_fail={out['n_orig_parse_fail']}")
    with open(a.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
