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
    assert all(set(m) == ids for m in maps), "三遍题集不一致"
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
        stab[cfg], unstable[cfg] = stability(rs)

    i2_pass = all(len(v) <= I2_MAX_UNSTABLE[cfg.split("_")[0]] for cfg, v in unstable.items())
    out = {"thresholds": {"I1": I1_MIN_SAME_RATE, "I2": I2_MAX_UNSTABLE,
                          "I3": [I3_POS_MIN, I3_NEG_MAX]},
           "I1": {"same_rate": i1, "pass": i1_pass},
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
    cheap = (out["E"]["cards"]["confirmed_cost_pt"] == 0
             and out["E"]["docs"]["confirmed_cost_pt"] == 0)
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
    p.add_argument("--controls", nargs=4, required=True,
                   metavar=("DOCS_POS", "DOCS_NEG", "CARDS_POS", "CARDS_NEG"))
    p.add_argument("--output", required=True)
    a = p.parse_args(argv)
    runs = {cfg.replace("-", "_"): [_load(x) for x in getattr(a, cfg.replace("-", "_"))]
            for cfg in ("cards-study", "cards-both", "docs-study", "docs-both")}
    probes = {"cards": _load(a.probe_cards), "docs": _load(a.probe_docs)}
    keys = ("docs_positive", "docs_negative", "cards_positive", "cards_negative")
    controls = dict(zip(keys, (_load(x) for x in a.controls), strict=True))
    verdict, rc = build_verdict(runs, probes, controls)
    with open(a.output, "w", encoding="utf-8") as f:
        json.dump(verdict, f, ensure_ascii=False, indent=1)
    print(f"I1 pass={verdict['I1']['pass']} {verdict['I1']['same_rate']}")
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
