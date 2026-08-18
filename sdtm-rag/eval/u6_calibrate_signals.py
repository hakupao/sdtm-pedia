"""U6 T9 可见集标定台: 在冻结基线的 pred 上离线模拟信号层, 零 LLM, 只看 legacy + dev.

复跑:
  ./.venv/bin/python -m eval.u6_calibrate_signals \
      --baseline data/study/st01/eval/runs/u6_baseline_run_1.json

**可见集纪律** (spec §5.2 三道防线): 标定只许看 legacy 181 + dev 12; held-out / 干扰 /
amb / u1_doc / final 全程封存。run json 的 `detail` 里躺着**全部七组**含题面, 故过滤发生在
读入处 (`load_base_preds` 只收给定的可见 id), 而不是打印处 —— 读进来再在末端过滤的话,
中间任何一次调试打印都会把封存组带出来。

**零题面**: 本脚本 stdout 与 `--json-out` 产物只有题号 / 组名 / 计数 / 判定, 不含任何题面。

**离线模拟为什么与真跑等价**: 信号层 (`RoutingSignals.widen_reason`) 只吃 (判库结果, 原问句),
不吃 router 的任何内部状态。故把冻结基线的 pred 用一个重放 router 喂回 `decide_corpus`,
走的就是生产那条同一函数 —— 白名单闸 / 方向闸 / 异常旁路三条契约一并复用, 不是重写一份。
(重写一份的症状: 标定按一把与生产不同的尺子选词表, 而两把尺子的差只在破法上显形。)

**预登记选择规则** (plan Task 9, 先于数据写死): 采纳一版词表 iff 可见集上 —
  (a) legacy exact 相对基线不降;
  (b) dev exact 降 ≤ 1;
  (c) `study_sig` 与 `cdisc_sig` 各至少 fire 1 次 (无死信号)。

(c) 有两种读法, 本脚本**两种都算并都打印**:
  - `widen` 读法 = 该信号真的把某题从单库拓宽成 both;
  - `detect` 读法 = 该信号的探针在可见集某题上命中 (与该题判到哪库无关)。

`widen` 读法在本可见集上**不可满足, 且与词表无关** —— 这是基线聚合数字 (Task 6 冻结,
先于本次标定已知) 的算术推论, 不是看了标定数据才发现的:
  legacy 181 题 exact 179 且 fatal 0 ⇒ 那 2 道不 exact 的题 pred 必为 `both`
  (score_run: 非 exact 且非 fatal ⇒ pred == "both"); dev 12/12 全 exact。
  ⇒ 可见集里**每一道 pred 为单库的题, 现在都恰好判对**。widen-only 只把单库变 both,
    故可见集上任何一次 widen 都恰好 −1 exact (gold 是单库), 不可能 +1。
  ⇒ (a) 要求 legacy 上 0 次 widen; (b) 允许 dev 上 ≤1 次 widen; 而 (c) 的 widen 读法要求
    两个信号各 ≥1 次 —— 一道题只产一个理由 (方向由判库结果定死), 故需 ≥2 次 widen,
    两次都只能落在 dev ⇒ dev 掉 2 分 > 1, 与 (b) 冲突。三条恒不可同时成立。
故本脚本以 `detect` 为**操作性读法** (`C_RULE_READING`): 它量的正是「无死信号」这条规则
要防的东西 (词表被剪到永不命中), 且不与 (a)(b) 结构性冲突。`widen` 读法的数字照样打印,
引用 (c) 时必须连读法一起写。
"""
from __future__ import annotations

import argparse
import json
import types
from pathlib import Path

from eval.run_routing_eval import load_gold, score_run
from server.config import settings
from server.federation import VALID_CORPORA, decide_corpus
from server.routing_signals import WIDEN_REASON_BY_CORPUS, WIDEN_REASONS, build_signals

DEFAULT_BASELINE = "data/study/st01/eval/runs/u6_baseline_run_1.json"
# 可见集 (spec §5.2)。两组**都**必须在场: (a) 只读 legacy, (b) 只读 dev, 少一组等于那条
# 规则恒真, 而缺组在输出里长得跟「这组本来就不存在」一模一样。
VISIBLE_GROUPS = ("legacy", "dev")
# (c) 的操作性读法, 见模块 docstring 的不可满足性推证。
C_RULE_READING = "detect"


class _ReplayRouter:
    """把冻结基线的 pred 当成 router 输出重放 —— 零 LLM, 零网络。

    只实现 `route_corpus` 真正用到的那一小片接口 (completion → choices[0].message.content)。
    pred 非法时故意不在这里兜底: `route_corpus` 会 fallback 成 ("both", True), 而
    `simulate` 见到 fallback 一律抛 —— 一次静默 fallback 在计数上与一次 widen 无法区分。
    """

    def __init__(self, pred: str):
        self.pred = pred

    def completion(self, **kwargs):
        msg = types.SimpleNamespace(content=json.dumps({"corpus": self.pred}))
        return types.SimpleNamespace(choices=[types.SimpleNamespace(message=msg)])


def visible_subset(gold: list[dict]) -> list[dict]:
    """gold → 只含 legacy / dev 的子集。组集不恒等于可见集就抛。"""
    out = [g for g in gold if g.get("group") in VISIBLE_GROUPS]
    groups = {g["group"] for g in out}
    if groups != set(VISIBLE_GROUPS):
        missing = sorted(set(VISIBLE_GROUPS) - groups)
        raise ValueError(
            f"可见集缺组 {missing} — (a)/(b) 两条选择规则各读一组, 缺组等于该条恒真, 拒绝标定")
    return out


def load_base_preds(path: str | Path, ids: set[str]) -> dict[str, str]:
    """冻结基线 run → {可见 id: pred}。**只收 `ids` 里的题**, 封存组当场丢弃。"""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    preds = {d["id"]: d["pred"] for d in data["detail"] if d["id"] in ids}
    missing = sorted(ids - set(preds))
    if missing:
        raise ValueError(f"基线 run 缺可见题 {missing} — 参照物不完整, 拒绝标定")
    bad = sorted(i for i, p in preds.items() if p not in VALID_CORPORA)
    if bad:
        raise ValueError(f"基线 pred 非法 {bad} — 重放会 fallback 成 both, 与一次拓宽同形")
    return preds


def _probe(signals, routed: str, question: str) -> bool:
    """探针: 该题在 `routed` 这一侧会不会给出**方向正确**的理由 (信号本身活着吗)。

    与实际判库无关, 故不经 `decide_corpus`。信号层抛异常时按"没命中"计 —— 与
    `decide_corpus` 的旁路语义同向 (坏掉的信号层退化成不拓宽, 而不是让标定崩掉)。
    """
    try:
        return signals.widen_reason(routed, question) == WIDEN_REASON_BY_CORPUS[routed]
    except Exception:
        return False


def simulate(gold_subset: list[dict], base_preds: dict[str, str], signals) -> dict:
    """在基线 pred 上离线施加信号层, 出标定报告 (零题面)。"""
    def _empty() -> dict[str, dict[str, list[str]]]:
        return {r: {g: [] for g in VISIBLE_GROUPS} for r in WIDEN_REASONS}

    widen_fires, detector_fires = _empty(), _empty()
    sim_preds: dict[str, str] = {}
    for g in gold_subset:
        qid, group = g["id"], g["group"]
        if qid not in base_preds:
            raise ValueError(f"{qid} 无基线 pred — 无参照物, 拒绝标定")
        corpus, fallback, reason = decide_corpus(_ReplayRouter(base_preds[qid]),
                                                 g["question"], signals)
        if fallback:
            raise ValueError(f"{qid}: 基线 pred {base_preds[qid]!r} 重放失败并 fallback 成 both "
                             f"— 那与一次拓宽同形, 拒绝计数")
        sim_preds[qid] = corpus
        if reason is not None:
            widen_fires[reason][group].append(qid)
        for routed, r in WIDEN_REASON_BY_CORPUS.items():
            if _probe(signals, routed, g["question"]):
                detector_fires[r][group].append(qid)

    by_group = {}
    for name in VISIBLE_GROUPS:
        sub = [g for g in gold_subset if g["group"] == name]
        base = score_run(sub, base_preds)
        sim = score_run(sub, sim_preds)
        by_group[name] = {
            "n": base["n"], "base_exact": base["exact"], "base_fatal": base["fatal"],
            "sim_exact": sim["exact"], "sim_fatal": sim["fatal"],
            "d_exact": sim["exact"] - base["exact"],
            "widened": sum(len(f[name]) for f in widen_fires.values()),
        }

    legacy, dev = by_group["legacy"], by_group["dev"]
    rules = {
        "a_legacy_exact_not_lower": {
            "pass": legacy["sim_exact"] >= legacy["base_exact"],
            "base": legacy["base_exact"], "sim": legacy["sim_exact"]},
        "b_dev_exact_drop_le_1": {
            "pass": dev["base_exact"] - dev["sim_exact"] <= 1,
            "base": dev["base_exact"], "sim": dev["sim_exact"],
            "drop": dev["base_exact"] - dev["sim_exact"]},
    }
    for reading, fires in (("widen", widen_fires), ("detect", detector_fires)):
        counts = {r: sum(len(ids) for ids in fires[r].values()) for r in WIDEN_REASONS}
        rules[f"c_both_signals_alive_{reading}"] = {
            "pass": all(n >= 1 for n in counts.values()), "counts": counts,
            "operative": reading == C_RULE_READING}
    accepted = all(v["pass"] for k, v in rules.items()
                   if not k.startswith("c_") or v["operative"])
    return {"n": len(gold_subset), "by_group": by_group, "widen_fires": widen_fires,
            "detector_fires": detector_fires, "rules": rules,
            "c_rule_reading": C_RULE_READING, "sim_preds": sim_preds, "accepted": accepted}


def render(report: dict) -> list[str]:
    """报告 → stdout 行 (只有题号 / 组名 / 计数 / 判定; 零题面)。"""
    out = [f"可见集: {report['n']} 题 " + " ".join(
        f"{g}:{d['n']}" for g, d in report["by_group"].items())]
    out.append("")
    out.append("组       n   exact(base→sim)   fatal(base→sim)   Δexact   widened")
    for name, d in report["by_group"].items():
        out.append(f"{name:8s} {d['n']:3d}   {d['base_exact']:3d} → {d['sim_exact']:3d}"
                   f"          {d['base_fatal']:2d} → {d['sim_fatal']:2d}"
                   f"           {d['d_exact']:+d}      {d['widened']}")
    out.append("")
    for label, key in (("widen fire (拓宽真的发生)", "widen_fires"),
                       ("detector fire (探针命中)", "detector_fires")):
        out.append(f"{label}:")
        for reason in WIDEN_REASONS:
            for group in VISIBLE_GROUPS:
                ids = report[key][reason][group]
                out.append(f"  {reason:10s} {group:8s} n={len(ids):3d}  {ids}")
    out.append("")
    for name, r in report["rules"].items():
        mark = "PASS" if r["pass"] else "⛔ 未达标"
        extra = {k: v for k, v in r.items() if k not in ("pass", "operative")}
        tail = "" if "operative" not in r else (
            "  ← 操作性读法" if r["operative"] else "  (仅报告, 见模块 docstring 的不可满足性推证)")
        out.append(f"{name:32s} {mark}  {json.dumps(extra, ensure_ascii=False)}{tail}")
    out.append(f"accepted = {report['accepted']}  (c 读法: {report['c_rule_reading']})")
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="U6 T9 可见集标定 (零 LLM, 零题面)")
    p.add_argument("--baseline", default=DEFAULT_BASELINE)
    p.add_argument("--json-out", help="报告落盘路径 (同样零题面)")
    a = p.parse_args(argv)
    gold = visible_subset(load_gold())
    preds = load_base_preds(a.baseline, {g["id"] for g in gold})
    report = simulate(gold, preds, build_signals(settings))
    if a.json_out:
        # sim_preds 逐题预测不进落盘产物: 它是中间量, 而产物是要贴进 evidence 的。
        Path(a.json_out).write_text(
            json.dumps({k: v for k, v in report.items() if k != "sim_preds"},
                       ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(render(report)))
    return 0 if report["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
