"""四模型离线对比裁判 — 预登记 `evidence/checkpoints/model_compare_2026-09.md`。

输入: `verified` 抽检落盘的 run_<tag>.json (同题集、同检索口径), **零生成成本**, 只花裁判调用。
J1 匿名四路排名 (复用 server.compare.run_judge, 标签按题随机置换) · J2 另一置换重裁 (稳定性)
· J3 语义 fact recall (run_eval.check_fact_recall_judge)。产物落 JSON, 自毁条款在脚本里判并打印。

跑法 (从 sdtm-rag/):
  .venv/bin/python eval/compare_verified_runs.py --limit 2      # 冒烟, 2 题 × (2 + 4) = 12 次调用
  .venv/bin/python eval/compare_verified_runs.py                # 全量 100 题, 600 次调用
  .venv/bin/python eval/compare_verified_runs.py --reaggregate evidence/checkpoints/model_compare_2026-09.json
      # 零调用: 用严格口径 (秩合法 + best==rank1 + 同分母) 从落盘逐题行重算聚合, 覆盖 j1/j2/自毁 字段

Rule D 审阅 (2026-09-07) 修订: F1 best 与 rank-1 可能不一致 ⇒ 聚合一律用 best_by_rank;
F2 秩必须恰为 {1,2,3,4} 否则该行计入 n_rank_invalid (不进 n_ok, 不混 parse_fail);
F3 J2 两指标同分母; F4 seed1 置换若与 seed0 撞车重摇 (旧产物记 n_same_perm, 报敏感性);
F5 自毁触发 ⇒ 对应数字置 None 并先打印条款; F6 传输失败与 parse 失败分列;
F8 --limit 冒烟不覆盖正式产物; F10/F11/F13 三条前置断言; F15 输出全两两胜率矩阵。
"""
from __future__ import annotations

import argparse
import asyncio
import itertools
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "eval" / "prod_wirein"))

from check_code_grounding import (  # noqa: E402
    assert_context_not_degenerate,
    check_fidelity,
    levers_from_report,
    prod_engine,
)

from eval.run_eval import DEFAULT_JUDGE_MODEL, check_fact_recall_judge, load_test_set  # noqa: E402
from server.compare import ModelAnswer, run_judge  # noqa: E402

TAGS = ["opus-5", "sonnet-5", "gpt-terra", "gpt-sol"]
RUNS_DIR = ROOT / "evidence" / "checkpoints" / "verified_runs"
BASELINE = "opus-5"
# 预登记: 剔除 opus-5 4096 上限撞顶的两题 (B-2 不齐)。从数据推导并断言, 不靠记忆。
PREREG_EXCLUDED = {"q36", "q83"}


def load_runs() -> dict[str, dict]:
    runs = {}
    for t in TAGS:
        raw = json.loads((RUNS_DIR / f"run_{t}.json").read_text(encoding="utf-8"))
        runs[t] = {"raw": raw, "by_id": {r["id"]: r for r in raw["results"]}}
    return runs


def truncated_ids(runs: dict) -> set[str]:
    """completion_tokens 撞到该 run 的 max_tokens 上限 ⇒ 截断 (opus-5 老报告无 truncated 字段, 上限 4096)。"""
    out = set()
    for r in runs.values():
        cap = r["raw"]["summary"].get("max_tokens") or 4096
        for q in r["raw"]["results"]:
            if (q.get("usage") or {}).get("completion_tokens", 0) >= cap:
                out.add(q["id"])
    return out


def rebuild_contexts(runs: dict, qids: list[str]) -> dict[str, str]:
    """同口径重建上下文; 四份 run 的落盘 top5 都必须与重建逐位一致 (保真闸), 否则拒绝出数。"""
    levers = {t: levers_from_report(r["raw"]) for t, r in runs.items()}
    if len({json.dumps(v, sort_keys=True) for v in levers.values()}) != 1:
        raise SystemExit(f"四份 run 检索口径不同, 不可比: {levers}")
    eng = prod_engine(levers[TAGS[0]])
    ctx = {}
    for qid in qids:
        q = runs[TAGS[0]]["by_id"][qid]["question"]
        chunks = eng.retrieve(q)
        top5 = [c.source for c in chunks][:5]
        for t in TAGS:
            check_fidelity(f"{qid}/{t}", runs[t]["by_id"][qid]["top5_sources"], top5)
        c = eng.format_context(chunks)
        assert_context_not_degenerate(qid, c)
        ctx[qid] = c
    return ctx


def perm_for(qid: str, seed: int, avoid: list[str] | None = None) -> list[str]:
    """按 (seed, qid) 可复现的置换; F4: 给 `avoid` 时重摇直到与之不同 (4 元素撞车概率 1/24)。"""
    rng = random.Random(f"{seed}:{qid}")
    order = TAGS[:]
    rng.shuffle(order)
    while avoid is not None and order == avoid:
        rng.shuffle(order)
    return order


def judge_once(qid: str, question: str, context: str, runs: dict, seed: int, judge: str,
               order: list[str] | None = None) -> dict:
    order = order or perm_for(qid, seed)
    # F10: run_judge 的标签是 zip 到过滤后的非空答案上; 有空答案则 order.index 反推位置会错位
    assert all(runs[t]["by_id"][qid]["answer"].strip() for t in TAGS), f"{qid}: 有空答案, 位置映射不可信"
    answers = [ModelAnswer(model=t, answer=runs[t]["by_id"][qid]["answer"], usage=None,
                           latency_ms=0, cost_usd=None, error=None) for t in order]
    verdict = asyncio.run(run_judge(question, context, answers, judge))
    row = {"id": qid, "seed": seed, "order": order, "parse_ok": verdict is not None}
    if verdict is not None:
        row["rank"] = {r["model"]: r["rank"] for r in verdict["ranking"]}
        row["best"] = verdict["best_model"]  # 裁判自报, 仅记录; 聚合用 best_by_rank (F1)
        row["rationale"] = verdict["rationale"]
    return row


def rank_valid(r: dict) -> bool:
    return r.get("parse_ok", False) and sorted(r.get("rank", {}).values()) == [1, 2, 3, 4]


def best_by_rank(r: dict) -> str:
    return min(r["rank"], key=r["rank"].get)


def aggregate_j1(rows: list[dict], cats: dict[str, str]) -> dict:
    ok = [r for r in rows if rank_valid(r)]
    n_parse_fail = sum(1 for r in rows if not r["parse_ok"])
    n_rank_invalid = sum(1 for r in rows if r["parse_ok"] and not rank_valid(r))
    n_best_mismatch = sum(1 for r in ok if r.get("best") != best_by_rank(r))
    mean_rank = {t: round(sum(r["rank"][t] for r in ok) / len(ok), 3) if ok else None for t in TAGS}
    rank1 = Counter(best_by_rank(r) for r in ok)
    pair = {a: {b: 0 for b in TAGS if b != a} for a in TAGS}
    for r in ok:
        for a, b in itertools.permutations(TAGS, 2):
            if r["rank"][a] < r["rank"][b]:
                pair[a][b] += 1
    for a, b in itertools.combinations(TAGS, 2):  # 秩合法 ⇒ 无并列 ⇒ 胜负互补
        assert pair[a][b] + pair[b][a] == len(ok), (a, b)
    by_cat = defaultdict(lambda: defaultdict(list))
    for r in ok:
        for t in TAGS:
            by_cat[cats[r["id"]]][t].append(r["rank"][t])
    return {
        "n_ok": len(ok), "n_parse_fail": n_parse_fail, "n_rank_invalid": n_rank_invalid,
        "n_best_mismatch": n_best_mismatch,
        "mean_rank": mean_rank,
        "rank1": {t: rank1.get(t, 0) for t in TAGS},
        "pairwise_wins": pair,
        "pairwise_winrate": {a: {b: round(pair[a][b] / len(ok), 3) if ok else None
                                 for b in TAGS if b != a} for a in TAGS},
        "vs_baseline_winrate": {t: round(pair[t][BASELINE] / len(ok), 3) if ok else None
                                for t in TAGS if t != BASELINE},
        "best_pos_dist": dict(Counter("ABCD"[r["order"].index(best_by_rank(r))] for r in ok)),
        "mean_rank_by_category": {c: {t: round(sum(v) / len(v), 3) for t, v in d.items()}
                                  for c, d in by_cat.items()},
    }


def kendall_tau(ra: dict, rb: dict) -> float:
    conc = disc = 0
    for a, b in itertools.combinations(TAGS, 2):
        s = (ra[a] - ra[b]) * (rb[a] - rb[b])
        conc += s > 0
        disc += s < 0
    return (conc - disc) / 6


def aggregate_j2(r0: list[dict], r1: list[dict]) -> dict:
    a = {r["id"]: r for r in r0 if rank_valid(r)}
    b = {r["id"]: r for r in r1 if rank_valid(r)}
    both = sorted(set(a) & set(b))  # F3: best_agree 与 τ 同分母 (两轮都秩合法)
    same_perm = [q for q in both if a[q]["order"] == b[q]["order"]]  # F4: 旧产物里可能撞车
    def _agree(ids):
        return sum(best_by_rank(a[q]) == best_by_rank(b[q]) for q in ids)
    taus = [kendall_tau(a[q]["rank"], b[q]["rank"]) for q in both]
    excl = [q for q in both if q not in same_perm]
    return {"n_both": len(both), "n_partial_dropped": len(r0) - len(both),
            "best_agree": round(_agree(both) / len(both), 3) if both else None,
            "kendall_tau_mean": round(sum(taus) / len(taus), 3) if taus else None,
            "n_same_perm": len(same_perm), "same_perm_ids": same_perm,
            "best_agree_excl_same_perm": round(_agree(excl) / len(excl), 3) if excl else None}


def run_j3(runs: dict, qids: list[str], facts: dict[str, list[str]], judge: str) -> dict:
    assert all(facts[q] for q in qids), "有题 expected_facts 为空 ⇒ 每模型白送 1.0 (F13)"
    out = {}
    for t in TAGS:
        rows, fails = [], 0
        for qid in qids:
            v = check_fact_recall_judge(runs[t]["by_id"][qid]["question"],
                                        runs[t]["by_id"][qid]["answer"], facts[qid], judge)
            if v is None:
                fails += 1
                rows.append({"id": qid, "recall": None})
            else:
                rows.append({"id": qid, "recall": round(v[0], 4)})
        sc = [r["recall"] for r in rows if r["recall"] is not None]
        out[t] = {"mean": round(sum(sc) / len(sc), 4) if sc else None, "n": len(sc),
                  "parse_fail": fails, "rows": rows}
        print(f"  J3 {t}: mean={out[t]['mean']} n={len(sc)} parse_fail={fails}", flush=True)
    return out


def self_destruct(j1: dict, j1b: dict, j2: dict, j3: dict) -> list[str]:
    hits = []
    # C1 分母: parse 失败 + 秩非法都算"裁判没给出可用裁定" (严格口径, 只会更容易触发)
    if (j1["n_parse_fail"] + j1["n_rank_invalid"] > 10
            or j1b["n_parse_fail"] + j1b["n_rank_invalid"] > 10):
        hits.append("C1 JUDGE_UNPARSEABLE")
    # 复核规则 4 (预登记文档, 数据前写死): C2 以 best_agree 与剔除同置换题后的值中**较低者**判
    agree_vals = [v for v in (j2["best_agree"], j2.get("best_agree_excl_same_perm")) if v is not None]
    if not agree_vals or min(agree_vals) < 0.70:
        hits.append(f"C2 裁判不稳定 (min best_agree={min(agree_vals) if agree_vals else None} < 70%)")
    if j1["n_ok"] and max(j1["best_pos_dist"].values()) / j1["n_ok"] > 0.45:
        hits.append("C3 位置偏好 (某标签 rank-1 > 45%)")
    for t, v in j3.items():
        if v["parse_fail"] > 10:
            hits.append(f"C4 {t} J3 parse 失败 > 10")
    mr = [v for v in j1["mean_rank"].values() if v is not None]
    if len(mr) == 4 and max(abs(a - b) for a, b in itertools.combinations(mr, 2)) < 0.15:
        hits.append("C5 题集无分辨力 (mean rank 两两差 < 0.15)")
    return hits


def suppress(out: dict, hits: list[str]) -> None:
    """F5: 自毁触发 ⇒ 对应数字置 None + 标 suppressed_by, 不让作废的数留在产物里。"""
    tags = {h.split()[0] for h in hits}
    # 按预登记各条款的后果分别处置: C1 = 不出排名结论 (置 None); C2/C3 = 只报数字, ⛔ 不得据此决策;
    # C5 = 只能写「未发现差异」。后两类数字保留但打上 decision_barred_by, 消费方必须连带。
    for k in ("j1_seed0", "j1_seed1"):
        if "C1" in tags:
            for f in ("mean_rank", "rank1", "pairwise_winrate", "vs_baseline_winrate"):
                out[k][f] = None
            out[k]["suppressed_by"] = ["C1"]
        barred = sorted(tags & {"C2", "C3", "C5"})
        if barred:
            out[k]["decision_barred_by"] = barred
    for h in hits:
        if h.startswith("C4 "):
            t = h.split()[1]
            out["j3"][t]["mean"] = None
            out["j3"][t]["suppressed_by"] = "C4"


def finalize(out: dict, cats: dict[str, str], path: str) -> None:
    """从逐题行重算全部聚合 + 自毁 + 压制, 落盘并打印 (自毁条款先于数字)。"""
    j1, j1b = aggregate_j1(out["j1_rows_seed0"], cats), aggregate_j1(out["j1_rows_seed1"], cats)
    j2 = aggregate_j2(out["j1_rows_seed0"], out["j1_rows_seed1"])
    j3 = out["j3"]
    hits = self_destruct(j1, j1b, j2, j3)
    out.update({"j1_seed0": j1, "j1_seed1": j1b, "j2": j2, "self_destruct": hits})
    suppress(out, hits)
    Path(path).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n自毁条款:", hits or "无触发")
    print(f"J1 (seed0) n_ok={j1['n_ok']} parse_fail={j1['n_parse_fail']} rank_invalid={j1['n_rank_invalid']}"
          f" best!=rank1={j1['n_best_mismatch']}")
    print("   mean rank:", out["j1_seed0"]["mean_rank"], "\n   rank-1:", out["j1_seed0"]["rank1"],
          "\n   vs opus-5 胜率:", out["j1_seed0"]["vs_baseline_winrate"], "\n   位置分布:", j1["best_pos_dist"])
    print("J2:", j2)
    print("J3:", {t: d["mean"] for t, d in out["j3"].items()})
    print("saved ->", path)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    ap.add_argument("--limit", type=int, default=None, help="冒烟: 只裁前 N 题")
    ap.add_argument("--output", default=str(ROOT / "evidence" / "checkpoints" / "model_compare_2026-09.json"))
    ap.add_argument("--test-set", default=str(ROOT / "eval" / "test_set_v2.yml"))
    ap.add_argument("--reaggregate", default=None, help="零调用: 从已落盘产物的逐题行按严格口径重算聚合")
    a = ap.parse_args(argv)
    ts = load_test_set(a.test_set)
    cats = {q["id"]: q["category"] for q in ts}

    if a.reaggregate:
        out = json.loads(Path(a.reaggregate).read_text(encoding="utf-8"))
        out["reaggregated_strict"] = True
        finalize(out, cats, a.reaggregate)
        return 0
    if a.limit and a.output == ap.get_default("output"):
        a.output = a.output.replace(".json", f"_smoke{a.limit}.json")  # F8: 冒烟不覆盖正式产物

    runs = load_runs()
    ids = [r["id"] for r in runs[TAGS[0]]["raw"]["results"]]
    for t in TAGS:
        if [r["id"] for r in runs[t]["raw"]["results"]] != ids:
            raise SystemExit(f"{t} 题序与 {TAGS[0]} 不同")
        for q in ids:  # F11: 题面逐字一致
            if runs[t]["by_id"][q]["question"] != runs[TAGS[0]]["by_id"][q]["question"]:
                raise SystemExit(f"{t}/{q} 题面与 {TAGS[0]} 不同")
    trunc = truncated_ids(runs)
    if trunc != PREREG_EXCLUDED:
        raise SystemExit(f"数据推导的截断题 {sorted(trunc)} != 预登记剔除集 {sorted(PREREG_EXCLUDED)}, 停下报告")
    qids = [q for q in ids if q not in trunc]
    if a.limit:
        qids = qids[:a.limit]
    facts = {q["id"]: q["expected_facts"] for q in ts}
    print(f"题 {len(qids)} (剔除 {sorted(trunc)}) · 裁判 {a.judge_model} · 预计调用 {len(qids) * 6}", flush=True)

    ctx = rebuild_contexts(runs, qids)
    print(f"重建保真: {len(qids)} 题 × 4 run 全一致 ✓", flush=True)

    j1_rows, j1b_rows = [], []
    for i, qid in enumerate(qids, 1):
        q = runs[TAGS[0]]["by_id"][qid]["question"]
        o0 = perm_for(qid, 0)
        o1 = perm_for(qid, 1, avoid=o0)  # F4: 保证"另一个置换"
        j1_rows.append(judge_once(qid, q, ctx[qid], runs, 0, a.judge_model, order=o0))
        j1b_rows.append(judge_once(qid, q, ctx[qid], runs, 1, a.judge_model, order=o1))
        print(f"  [{i}/{len(qids)}] {qid} ok s0={j1_rows[-1]['parse_ok']} s1={j1b_rows[-1]['parse_ok']}", flush=True)
    j3 = run_j3(runs, qids, facts, a.judge_model)
    out = {"judge_model": a.judge_model, "n_questions": len(qids), "excluded": sorted(trunc),
           "j3": {t: {k: v for k, v in d.items() if k != "rows"} for t, d in j3.items()},
           "j3_rows": {t: d["rows"] for t, d in j3.items()},
           "j1_rows_seed0": j1_rows, "j1_rows_seed1": j1b_rows}
    finalize(out, cats, a.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
