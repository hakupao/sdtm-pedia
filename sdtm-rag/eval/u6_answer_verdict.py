"""U6 答题侧修订判定 (spec 2026-08-17 §4.3, 用户裁定, 冻结): E1 支配纳入 / E4 并集闸 /
I-1 结论词抑制 / divergent_readings.

A 臂 = 信号层 OFF 的 auto 三遍, B 臂 = ON 的 auto 三遍。B 比 A 差 = 代价, 反之 = 收益。

历史件 `eval/u5_verdict.py` 冻结不动 (U5 收口复跑用); 本件 import 其
`scores_by_id` / `stability` / `paired_effect` —— **稳定半的口径因此与 U5 逐字同源**,
本件只在其上并入支配题 (spec §4.3: 最坏界尺子并入 E1 本体, 单一清单单一判词, 消除
C1 型双口径反向的结构来源)。

rc: 0 正常 · 2 = E4 并集闸触发 (不下结论)。I-1 失守**不改 rc**, 只把结论词降成
`advisory_no_verdict` —— 这是 spec §4.3 冻结的出口口径; 消费方读结论词而非只读 rc。

引用纪律 (进 Task 11/12 读法条款): 判词与代价额**只引顶层 E1**。`E1.stable_half` 是
U5 稳定半口径的**子集** (不含支配题, 带 `caliber` 标记键), 单独摘引会把有代价的批次
读成无代价。

复跑:
  ./.venv/bin/python -m eval.u6_answer_verdict \
      --arm-a runs/u6_ans_off_{1,2,3}.json --arm-b runs/u6_ans_on_{1,2,3}.json \
      --family cards --probe rejudge_probe.json --output u6_answer_verdict.json

红线: 只搬 id 与数字, 不读也不落盘任何题面 —— run json 的 results 行里带 question,
判定产物是要进 checkpoint 的, 两者之间这道过滤只有这一层。
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from eval.u5_verdict import EXPECTED_N, I1_MIN_SAME_RATE, paired_effect, scores_by_id, stability

# 跨配置不可判并集上限 = 20% of 48 / 30 (spec §4.3: per-config ≤15% 不动; 实测并集 14.6%,
# 放大界 29.2% —— 20% 在实测之上留 5.4pt 余量且拦住放大)。
E4_MAX_UNION = {"cards": 9, "docs": 6}
# 判词词面自带池限定 (U5 §9-1): 结论被单独摘出来引用时也读不成"整体便宜"。
CHEAP_WORD = "cheap_on_this_ruler_comparable_pool"
# 符号判定的零门槛: judge 分落在 0.1/0.5 的网格上, 真实读数远大于此; 这个 eps 只用来
# 把浮点求和残渣 (1e-17 量级) 挡在"非 0"之外, 否则净额恰为 0 的批次会假报分歧。
_EPS = 1e-9


def _validate_arm(runs: list[dict], label: str, expected_n: int) -> None:
    """四道产物闸沿 U5 (三遍 / 表头题量 / judge 在场 / 计分行数) —— 仪器坏了必须炸,
    静默误诊比缺结论贵得多。"""
    if len(runs) != 3:
        raise SystemExit(f"{label} 臂需 3 份 run, 得 {len(runs)} 份 — 三遍纪律")
    for i, r in enumerate(runs, 1):
        n = r["summary"]["n_questions"]
        if n != expected_n:
            raise SystemExit(f"{label} 第 {i} 份: n_questions {n} != {expected_n} — "
                             f"题集变了, 阈值失义")
        # 漏 --judge 的 run 全行无 judge_parse_ok → 会被读成全不稳定 → E4 假触发 (U5 审查 M4)
        if not r["summary"].get("judge_model"):
            raise SystemExit(f"{label} 第 {i} 份: 无 summary.judge_model — 该 run 没跑 judge")
        n_rows = len(scores_by_id(r))
        if n_rows != expected_n:
            raise SystemExit(f"{label} 第 {i} 份: 计分行数 {n_rows} != {expected_n} — 产物残缺")


def _raw_maps(runs: list[dict]) -> list[dict]:
    """三遍 → 三张 id→分 表 (parse 失败记 None). 支配判据要看原始三遍值, 不能只看稳定题。

    同臂三遍题集一致这条闸不在这里重复: 它归 `u5_verdict.stability` 所有 (compare_arms
    对同一批 run 调它), 两处各写一遍会得到一条谁都测不动的死守卫。
    """
    return [scores_by_id(r) for r in runs]


def _dominance(maps_a: list[dict], maps_b: list[dict]) -> tuple[dict, dict]:
    """支配题 (spec §4.3 裁定): 六个值全 parse_ok, 且一臂三遍的最好值仍不及另一臂三遍的
    最差值。额 = 三遍均值差。档内不稳定也计入 —— 支配关系本身就是噪声稳健的方向证据。

    严格小于: 两臂区间贴边相等 (max(B) == min(A)) 不算支配。
    """
    cost, gain = {}, {}
    for i in sorted(set(maps_a[0]) & set(maps_b[0])):
        va = [m[i] for m in maps_a]
        vb = [m[i] for m in maps_b]
        if None in va or None in vb:
            continue
        mean_gap = sum(va) / len(va) - sum(vb) / len(vb)
        if max(vb) < min(va):
            cost[i] = mean_gap
        elif max(va) < min(vb):
            gain[i] = -mean_gap
    return cost, gain


def _all_parse_ok_ids(maps_a: list[dict], maps_b: list[dict]) -> list:
    return sorted(i for i in set(maps_a[0]) & set(maps_b[0])
                  if all(m[i] is not None for m in (*maps_a, *maps_b)))


def _i1_block(probe: dict | None) -> dict | None:
    """I-1 = judge 重判自洽率 (rejudge_run 产物). 缺省 = 本批没做重判, 不做抑制。"""
    if probe is None:
        return None
    if probe["n"] == 0:
        # rejudge_run 在 scored 为空时吐 same_rate=0.0 —— 无意义值, 不是 I1 失守
        raise SystemExit("probe: n=0, same_rate 无意义 — 检查 probe 输入")
    # same_rate 单看无意义: 分母与被排除行数必须同落盘 (U5 审查 M2); 硬下标 = 缺键即炸
    return {"same_rate": probe["same_rate"], "n": probe["n"],
            "n_orig_parse_fail": probe["n_orig_parse_fail"],
            "pass": probe["same_rate"] >= I1_MIN_SAME_RATE}


def compare_arms(arm_a: list, arm_b: list, n_scored: int, family: str,
                 expected_n: int | None = None, probe: dict | None = None) -> dict:
    """A 臂 (信号层 off) vs B 臂 (on) 的答题侧修订判定。同输入恒同输出。"""
    if family not in EXPECTED_N:
        raise SystemExit(f"family={family} 不在 {sorted(EXPECTED_N)} — 阈值无从查表")
    exp = EXPECTED_N[family] if expected_n is None else expected_n
    _validate_arm(arm_a, "A(off)", exp)
    _validate_arm(arm_b, "B(on)", exp)
    maps_a, maps_b = _raw_maps(arm_a), _raw_maps(arm_b)
    # 先走 stability: 同臂三遍题集不一致由它拒 (报错话术也是它的), 之后才轮到跨臂比对。
    stable_a, unstable_a = stability(arm_a)
    stable_b, unstable_b = stability(arm_b)
    if set(maps_a[0]) != set(maps_b[0]):
        # 题集不同 = 拿两把尺子相减: 支配与聚合会静默只算交集, 判词照出
        raise SystemExit("两臂题集不一致 — 逐题配对无从谈起")

    # 稳定半直接走 U5 的 paired_effect: 口径与 U5 逐字同源, 本件只在其上并入支配题。
    stable_half = paired_effect(stable_a, stable_b, n_scored)
    # 这个子块与顶层 E1 同名同形 (confirmed_cost_ids 等), 单独摘出来引用会被读成"无代价"
    # —— 它只是 U5 口径的**子集**, 支配题不在其中。标记键把这层限定钉在数据里, 不靠读者记性。
    stable_half["caliber"] = "u5_stable_only_subset"
    cost = {i: stable_a[i] - stable_b[i] for i in stable_half["confirmed_cost_ids"]}
    gain = {i: stable_b[i] - stable_a[i] for i in stable_half["confirmed_gain_ids"]}
    stable_moved = set(cost) | set(gain)
    dom_cost, dom_gain = _dominance(maps_a, maps_b)
    # 两侧都稳定且分差 ≠ 0 的题必然也满足支配, 且两种口径的额相等 (常数的均值差 = 常数差),
    # 所以并集不会因覆盖而改数。
    cost.update(dom_cost)
    gain.update(dom_gain)
    dominance_ids = sorted(set(dom_cost) | set(dom_gain))
    ok_ids = _all_parse_ok_ids(maps_a, maps_b)

    e1 = {"confirmed_cost_pt": round(100 * sum(cost.values()) / n_scored, 2),
          "confirmed_cost_ids": sorted(cost),
          "confirmed_gain_pt": round(100 * sum(gain.values()) / n_scored, 2),
          "confirmed_gain_ids": sorted(gain),
          "dominance_ids": dominance_ids,
          # 判词有多少压在最坏界尺子上, 读者要能拆开看 (U5 §9-1 引用纪律): 这一格是
          # "稳定半没收, 靠支配才进来"的那些题。
          "dominance_only_ids": sorted(set(dominance_ids) - stable_moved),
          "n_all_parse_ok": len(ok_ids),
          "stable_half": stable_half}

    # 集合并集, 不是两臂清单相加: 同一题在两臂都不稳定时只占一格。拼接求和会把重叠题双计,
    # 闸值是绝对题数 ⇒ 并集本已过闸的批次会被假触发成"不可判"。
    union = sorted(set(unstable_a) | set(unstable_b))
    e4 = {"unstable_a": unstable_a, "unstable_b": unstable_b,
          "union": union, "n_union": len(union), "max": E4_MAX_UNION[family],
          "gate_pass": len(union) <= E4_MAX_UNION[family]}

    # 两把尺子并列落盘, 符号相反即置 divergent (spec §4.3): 聚合看全池均值 (含被 E1 排除
    # 的题), 配对看已确证净额 —— 二者本就可能反向, 反向本身是要报的事实, 不是要调和的矛盾。
    diffs = [sum(m[i] for m in maps_b) / 3 - sum(m[i] for m in maps_a) / 3 for i in ok_ids]
    agg = sum(diffs) / len(ok_ids) if ok_ids else 0.0
    net = (sum(gain.values()) - sum(cost.values())) / n_scored
    # 符号判在未 round 的值上: pt 只留 2 位, 真实非 0 的小额会被舍成 0.0 (U5 审查 M1 同款)。
    divergent = abs(agg) > _EPS and abs(net) > _EPS and (agg > 0) != (net > 0)

    i1 = _i1_block(probe)
    # E4 闸响时 E1 / aggregate 的数字**照样落盘** —— 有意如此 (controller 裁定 2026-08-18),
    # 不学 U5 的 `E = None`: 失败归档纪律要求闸响那批的原始读数留得下来供复盘。
    # 代价是这些数字看着像结论 —— 唯一的判词信号是 `verdict_word` (None = 闸响不下结论),
    # 消费方必须读它, 不许拿本块任何 pt 读数当结论 (Task 11/12 读法条款)。
    suppressed = []
    if not e4["gate_pass"]:
        suppressed.append("E4_union_gate")
    if i1 is not None and not i1["pass"]:
        suppressed.append("I1_rejudge")
    if "E4_union_gate" in suppressed:
        word = None                       # 闸响 = 不下结论, 连"仅供参考"都不给
    elif suppressed:
        word = "advisory_no_verdict"
    elif not e1["confirmed_cost_ids"]:
        # 判 cheap 的依据是"已确证代价集合为空", 不是 pt 读数 —— pt 只 round 2 位,
        # 非空代价可被舍成 0.0, 那会让产物自相矛盾 (U5 审查 M1)。
        word = CHEAP_WORD
    else:
        word = "cost_reported"

    return {"family": family, "expected_n": exp, "n_scored": n_scored,
            "thresholds": {"E4_union_max": E4_MAX_UNION, "I1_min_same_rate": I1_MIN_SAME_RATE},
            "E1": e1, "E4": e4, "I1": i1,
            "aggregate_mean_diff_pt": round(100 * agg, 2), "aggregate_n": len(ok_ids),
            "paired_net_pt": round(100 * net, 2), "divergent_readings": divergent,
            "verdict_suppressed_by": suppressed, "verdict_word": word}


def verdict_rc(out: dict) -> int:
    """rc 只由 E4 决定 (spec §4.3): I-1 失守走结论词降级, 不改 rc。"""
    return 0 if out["E4"]["gate_pass"] else 2


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--arm-a", nargs=3, required=True, metavar="RUN",
                   help="信号层 OFF 的 auto 三遍 (对照臂)")
    p.add_argument("--arm-b", nargs=3, required=True, metavar="RUN",
                   help="信号层 ON 的 auto 三遍 (修法臂)")
    p.add_argument("--family", required=True, choices=sorted(EXPECTED_N))
    p.add_argument("--output", required=True)
    p.add_argument("--probe", metavar="JSON",
                   help="rejudge_run 产物 (I-1); 缺省 = 本批没做重判, 不做结论词抑制")
    p.add_argument("--expected-n", type=int,
                   help="覆盖家族默认题量 (合成 fixture 用; 同时作 pt 分母)")
    a = p.parse_args(argv)

    def load(f: str) -> Any:
        return json.loads(Path(f).read_text(encoding="utf-8"))

    exp = EXPECTED_N[a.family] if a.expected_n is None else a.expected_n
    out = compare_arms([load(f) for f in a.arm_a], [load(f) for f in a.arm_b],
                       n_scored=exp, family=a.family, expected_n=exp,
                       probe=load(a.probe) if a.probe else None)
    rc = verdict_rc(out)
    Path(a.output).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    e1, e4 = out["E1"], out["E4"]
    print(f"E1 cost {e1['confirmed_cost_pt']}pt {e1['confirmed_cost_ids']}"
          f" | gain {e1['confirmed_gain_pt']}pt {e1['confirmed_gain_ids']}")
    print(f"   dominance={e1['dominance_ids']} (其中支配独有 {e1['dominance_only_ids']})"
          f" 可比池: 稳定配对 {e1['stable_half']['n_compared']} / 全 parse_ok {e1['n_all_parse_ok']}")
    print(f"E4 gate_pass={e4['gate_pass']} n_union={e4['n_union']}/{e4['max']} {e4['union']}")
    print(f"I1 {out['I1']}")
    print(f"aggregate={out['aggregate_mean_diff_pt']}pt (n={out['aggregate_n']})"
          f" vs paired_net={out['paired_net_pt']}pt"
          f"  divergent_readings={out['divergent_readings']}")
    print(f"verdict_word={out['verdict_word']} suppressed_by={out['verdict_suppressed_by']}")
    print(f"rc={rc}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
