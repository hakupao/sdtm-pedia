"""U5 六段判定 (spec §5, 阈值冻结): I1 judge 重判 / I2 逐题稳定性 / I3 双向对照 /
E1 逐题配对双向效应 / E2 判定 / E3 脆弱 4 题 + E4 不可判池.

确定性脚本: 同输入恒同输出; 人不许手算改判 (spec §5.3-3). 产物零题面.
rc: 0 全过 · 2 = I2/I3 触发 (自毁/停下上报) · 3 = I1 降级 (advisory only).
"""
from __future__ import annotations

import argparse
import json

I1_MIN_SAME_RATE = 0.95
I2_MAX_UNSTABLE = {"cards": 7, "docs": 4}      # ≤15% of 48 / 30 (spec §5.1)
I3_POS_MIN, I3_NEG_MAX = 0.80, 0.20            # U2 冻结判据 (spec 修正案 2)
EXPECTED_N = {"cards": 48, "docs": 30}
FRAGILE_4 = ("st01_v11_q19", "st01_v2_q14", "st01_v2_q15", "st01_v2_q21")
CONTROL_KEYS = ("docs_positive", "docs_negative", "cards_positive", "cards_negative")
PROBE_KEYS = ("cards", "docs")


def scores_by_id(run: dict) -> dict:
    """scored 行的 judge 分; parse 失败记 None (该遍分数来自子串兜底, 不可信)."""
    out = {}
    for r in run["results"]:
        if r.get("out_of_scope"):
            continue
        out[r["id"]] = r["judge_fact_recall"] if r.get("judge_parse_ok", False) else None
    return out


def stability(runs: list) -> tuple:
    """三遍 → (稳定题 id→分, 不稳定/不可信 id 清单). 稳定 = 三遍同分且全 parse_ok."""
    maps = [scores_by_id(r) for r in runs]
    ids = set(maps[0])
    # 裸 assert 会被 python -O 剥掉 → 题集不一致静默放行, 故用显式 raise.
    if any(set(m) != ids for m in maps):
        raise SystemExit(f"三遍题集不一致: {[len(m) for m in maps]} 行, 无法逐题配对")
    stable, unstable = {}, []
    for i in ids:
        vals = [m[i] for m in maps]
        if None in vals or len(set(vals)) != 1:
            unstable.append(i)
        else:
            stable[i] = vals[0]
    return stable, sorted(unstable)


def paired_effect(stable_a: dict, stable_b: dict, n_scored: int) -> dict:
    """E1: 两侧都稳定的题里 a(study) vs b(both). 双向对称 — 单向口径既漏真回归
    又杀真改善 (U3 §6-6 实测教训)."""
    common = set(stable_a) & set(stable_b)
    cost = {i: stable_a[i] - stable_b[i] for i in common if stable_a[i] > stable_b[i]}
    gain = {i: stable_b[i] - stable_a[i] for i in common if stable_b[i] > stable_a[i]}
    return {"confirmed_cost_pt": round(100 * sum(cost.values()) / n_scored, 2),
            "confirmed_cost_ids": sorted(cost),
            "confirmed_gain_pt": round(100 * sum(gain.values()) / n_scored, 2),
            "confirmed_gain_ids": sorted(gain),
            "n_compared": len(common)}


def build_verdict(runs: dict, probes: dict, controls: dict) -> tuple:
    # 键集必须先钉死: all() 对空生成器返回 True, 错键名/空字典会让 I3、I1 零迭代空过,
    # 完全反转的对照也能判 pass (审查 H1).
    if set(controls) != set(CONTROL_KEYS):
        raise SystemExit(f"controls 键集 {sorted(controls)} != {sorted(CONTROL_KEYS)} — 闸会空过")
    if set(probes) != set(PROBE_KEYS):
        raise SystemExit(f"probes 键集 {sorted(probes)} != {sorted(PROBE_KEYS)} — 闸会空过")
    for key, c in controls.items():
        # 极性绑定: judge_controls 产物的 mode 只带极性 (positive/negative), 不带家族.
        # 阳阴两份产物对调塞错 flag 时 I3 会反判 pass —— 这是唯一的静默假过路径.
        if c["mode"] != key.rsplit("_", 1)[1]:
            raise SystemExit(f"control {key}: mode={c['mode']} 与所在位极性不符 — 产物塞错 flag")
        # 信息量闸 (同 probe n=0 病): 全行 parse 失败时 avg 兜底成 0.0, 阴性对照会"完美通过".
        if sum(r["parse_ok"] for r in c["rows"]) == 0:
            raise SystemExit(f"control {key}: 0/{len(c['rows'])} 行 parse 成功 — avg 零信息, 不能过闸")
    i3 = {k: c["avg"] for k, c in controls.items()}
    i3_pass = (all(v >= I3_POS_MIN for k, v in i3.items() if k.endswith("positive"))
               and all(v <= I3_NEG_MAX for k, v in i3.items() if k.endswith("negative")))
    for k, p in probes.items():
        # rejudge_run 在 scored 为空时吐 same_rate=0.0 —— 那是无意义值, 不是 I1 失守.
        if p["n"] == 0:
            raise SystemExit(f"probe {k}: n=0, same_rate 无意义 — 检查 probe 输入")
    i1 = {k: p["same_rate"] for k, p in probes.items()}
    i1_pass = all(v >= I1_MIN_SAME_RATE for v in i1.values())

    stab, unstable = {}, {}
    for cfg, rs in runs.items():
        fam = cfg.split("_")[0]
        for r in rs:
            n = r["summary"]["n_questions"]
            if n != EXPECTED_N[fam]:
                raise SystemExit(f"{cfg}: n_questions {n} != {EXPECTED_N[fam]} — 题集变了, 阈值失义")
            # 漏 --judge 的 run 全行无 judge_parse_ok → 会被读成全不稳定 → 误诊
            # instrument_unusable (审查 M4, 与 Task 2 rejudge 的 judge 断言同款规矩).
            if not r["summary"].get("judge_model"):
                raise SystemExit(f"{cfg}: run 无 summary.judge_model — 该 run 没跑 judge")
            n_rows = len(scores_by_id(r))
            if n_rows != EXPECTED_N[fam]:
                raise SystemExit(f"{cfg}: 计分行数 {n_rows} != {EXPECTED_N[fam]} — 产物残缺")
        stab[cfg], unstable[cfg] = stability(rs)

    i2_pass = all(len(v) <= I2_MAX_UNSTABLE[cfg.split("_")[0]] for cfg, v in unstable.items())
    out = {"thresholds": {"I1": I1_MIN_SAME_RATE, "I2": I2_MAX_UNSTABLE,
                          "I3": [I3_POS_MIN, I3_NEG_MAX]},
           "I1": {"same_rate": i1,
                  # same_rate 单看无意义, 分母与被排除行数必须同落盘 (审查 M2)
                  "n": {k: p["n"] for k, p in probes.items()},
                  "n_orig_parse_fail": {k: p["n_orig_parse_fail"] for k, p in probes.items()},
                  "pass": i1_pass},
           "I2": {"counts": {c: len(v) for c, v in unstable.items()},
                  "unstable": unstable, "pass": i2_pass},
           "I3": {"avg": i3, "pass": i3_pass},
           "advisory_only": not i1_pass}
    if not (i3_pass and i2_pass):
        out["E"] = None
        out["E2_verdict"] = "controls_failed" if not i3_pass else "instrument_unusable"
        return out, 2

    out["E"] = {"cards": paired_effect(stab["cards_study"], stab["cards_both"], EXPECTED_N["cards"]),
                "docs": paired_effect(stab["docs_study"], stab["docs_both"], EXPECTED_N["docs"])}
    # cheap 的依据是"已确证代价集合为空", 不是 pt 读数 —— pt 只 round 2 位, 非空代价
    # 可被舍成 0.0, 那会让产物自相矛盾 (cost_ids 非空却判 cheap) (审查 M1).
    cheap = (not out["E"]["cards"]["confirmed_cost_ids"]
             and not out["E"]["docs"]["confirmed_cost_ids"])
    out["E2_verdict"] = "cheap_on_this_ruler" if cheap else "cost_reported"
    out["E3_fragile"] = {q: {"study": stab["cards_study"].get(q),
                             "both": stab["cards_both"].get(q),
                             "stable_study": q in stab["cards_study"],
                             "stable_both": q in stab["cards_both"]} for q in FRAGILE_4}
    out["E4_undecidable"] = {
        "cards": sorted(set(unstable["cards_study"]) | set(unstable["cards_both"])),
        "docs": sorted(set(unstable["docs_study"]) | set(unstable["docs_both"]))}
    return out, (3 if not i1_pass else 0)


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    for cfg in ("cards-study", "cards-both", "docs-study", "docs-both"):
        p.add_argument(f"--{cfg}", nargs=3, required=True, metavar="RUN")
    p.add_argument("--probe-cards", required=True)
    p.add_argument("--probe-docs", required=True)
    # 四个对照各用具名 flag: 身份绑进 flag 名. 位置传参一旦家族/极性对调, 会静默错标
    # I3.avg 归档 (家族对调) 或假自毁 (极性对调) —— 且要等 12 次付费跑批之后才现形 (审查 M5).
    for flag, what in (("--controls-docs-pos", "docs 阳性对照 (judge_controls mode=docs_positive)"),
                       ("--controls-docs-neg", "docs 阴性对照 (docs_negative)"),
                       ("--controls-cards-pos", "cards 阳性对照 (cards_positive)"),
                       ("--controls-cards-neg", "cards 阴性对照 (cards_negative)")):
        p.add_argument(flag, required=True, metavar="JSON", help=what)
    p.add_argument("--output", required=True)
    a = p.parse_args(argv)
    runs = {cfg.replace("-", "_"): [_load(x) for x in getattr(a, cfg.replace("-", "_"))]
            for cfg in ("cards-study", "cards-both", "docs-study", "docs-both")}
    probes = {"cards": _load(a.probe_cards), "docs": _load(a.probe_docs)}
    controls = {"docs_positive": _load(a.controls_docs_pos),
                "docs_negative": _load(a.controls_docs_neg),
                "cards_positive": _load(a.controls_cards_pos),
                "cards_negative": _load(a.controls_cards_neg)}
    verdict, rc = build_verdict(runs, probes, controls)
    with open(a.output, "w", encoding="utf-8") as f:
        json.dump(verdict, f, ensure_ascii=False, indent=1)
    print(f"I1 pass={verdict['I1']['pass']} same_rate={verdict['I1']['same_rate']}"
          f" n={verdict['I1']['n']} orig_parse_fail={verdict['I1']['n_orig_parse_fail']}")
    print(f"I2 pass={verdict['I2']['pass']} counts={verdict['I2']['counts']}")
    print(f"I3 pass={verdict['I3']['pass']}")
    print(f"E2_verdict={verdict['E2_verdict']}  advisory_only={verdict['advisory_only']}")
    if verdict["E"]:
        for d in ("cards", "docs"):
            e = verdict["E"][d]
            print(f"  {d}: cost {e['confirmed_cost_pt']}pt {e['confirmed_cost_ids']}"
                  f" | gain {e['confirmed_gain_pt']}pt {e['confirmed_gain_ids']}")
    print(f"rc={rc}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
