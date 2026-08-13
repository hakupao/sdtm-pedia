"""U2 阳性/阴性对照 (spec §5.3)。

为什么必须有: judge 分数只有在"喂对答案会得高分、喂空会得低分"两侧都成立时才可解读。
U1 实测过一次 (卡片库 0.0 ×6 + 阳性 1.00 ×6), 但那是一次性脚本 —— 本单元把它固化,
否则下一个人无法复跑 (U1 §8 硬约束 5)。

抽样规则 (spec §5.3, 读数据前写死): id 升序后取 idx = ⌊k*n/7⌋, k=1..6。与分数无关。
"""
from __future__ import annotations

import argparse
import json

import yaml

from eval.run_eval import DEFAULT_JUDGE_MODEL, check_fact_recall_judge


def sample_ids(ids: list[str], n: int) -> list[str]:
    if n <= 0 or n > len(ids):
        raise ValueError(f"n={n} out of range for {len(ids)} ids")
    ordered = sorted(ids)
    # 撞位不可能: 闸已保证 n <= L, 而 n == L 时 (k*L)//(L+1) = k-1 (k=1..L) 已两两不同,
    # n < L 时步长更大 ⇒ 恒得 n 个位置。原先那条"撞位回落"分支据此删除 (暴力枚举
    # L=1..299 × n=1..L 零撞位, 见 evidence/step_u2_mutation_remediation.md)。
    idx = sorted({(k * len(ordered)) // (n + 1) for k in range(1, n + 1)})
    return [ordered[i] for i in idx]


def positive_answer(q: dict) -> str:
    """阳性对照答案 = gold facts 原句拼接。judge 若给不出 ≈1.0, 说明尺子本身坏了。"""
    return "\n".join(q["expected_facts"])


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("test_set")
    p.add_argument("--mode", choices=["positive", "negative"], required=True)
    p.add_argument("--n", type=int, default=6)
    p.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    p.add_argument("--output")
    a = p.parse_args(argv)

    qs = {q["id"]: q for q in yaml.safe_load(open(a.test_set, encoding="utf-8"))}
    picked = sample_ids(list(qs), a.n)
    rows = []
    for qid in picked:
        q = qs[qid]
        answer = positive_answer(q) if a.mode == "positive" else "情報が見つかりませんでした。"
        # 签名核对过 (eval/run_eval.py:254): (question, answer, expected_facts, judge_model,
        # temperature=0.0) -> (recall, hits, misses) | None; None = judge 回复不可解析。
        verdict = check_fact_recall_judge(
            q["question"], answer, q["expected_facts"],
            judge_model=a.judge_model, temperature=0.0,
        )
        recall = verdict[0] if verdict else None
        rows.append({"id": qid, "recall": recall, "parse_ok": verdict is not None})
        print(f"[{a.mode}] {qid} recall={recall} parse_ok={verdict is not None}", flush=True)

    ok = [r["recall"] for r in rows if r["recall"] is not None]
    avg = sum(ok) / len(ok) if ok else 0.0
    print(f"[{a.mode}] n={len(rows)} parse_ok={sum(r['parse_ok'] for r in rows)} avg={avg:.4f}")
    if a.output:
        json.dump({"mode": a.mode, "avg": avg, "rows": rows},
                  open(a.output, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
