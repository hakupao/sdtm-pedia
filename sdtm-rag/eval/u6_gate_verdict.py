"""U6 修订判据判定 (spec 2026-08-17 §4.2, 冻结): 条款 1/2/3 沿 U3, 条款 4/7 双列双闸.

历史件 eval/u3_task8_verdict.py 不动 (U3 收口 §8 复跑用). rc=0 仅当 1/2/3/4/7 全 PASS.
诚实声明: 本单元机制 widen-only, 条款 4/7 的 fatal 半由构造保证, 判别力在 exact 半 (spec §4.2).

复跑:
  ./.venv/bin/python -m eval.u6_gate_verdict \
      --baseline data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json \
      --after    data/study/st01/eval/runs/u6_after_run_{1,2,3}.json \
      --output   data/study/st01/eval/u6_gate_verdict.json

红线: 本脚本只搬 id / group / 数字, 不打印也不落盘任何题面 —— run json 的 detail 里带
question, 判定产物是要进 checkpoint 的, 两者之间这道过滤只有这一层。
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

LEGACY_FLOOR = 178          # spec §7 不许下调
C2_GAP_PT = 25.0
C3_DEV_MIN = 10.0
# dev / heldout 组量 (spec §5.2)。既是条款 2 百分比的分母, 也是下面组量闸的期望值 ——
# 两处共用一个常量, 免得改了分母忘了改闸 (或反过来)。
GROUP_N = 12
DUAL_GATE_GROUPS = {"clause4": "distractor_cdisc", "clause7": "u1_doc"}


def _g(run: dict, name: str, key: str) -> int:
    return run["summary"]["by_group"][name][key]


def _rev_sha(rev: str) -> str:
    """`git describe --always --dirty` 串取尾段 sha: `v1.4-7-gabc1234-dirty` → `abc1234`.

    比对必须落到 sha 段: 同一个 commit 在打了新 tag 前后 describe 串不同 (`v1.3-9-gabc1234`
    → `v1.4-gabc1234`), 整串比会把「同一版本代码」读成两个版本 (Task 1 审查结转)。
    """
    core = rev.removesuffix("-dirty")
    tail = core.rsplit("-", 1)[-1]
    if tail.startswith("g") and len(tail) > 1 and all(c in "0123456789abcdef" for c in tail[1:]):
        return tail[1:]
    return tail


def _warn_provenance(base: list[dict], after: list[dict]) -> None:
    """只告警不拦 (Task 1 审查结转): 出处可疑不等于数字无效, 但读者有权当场看见。"""
    sha: dict[str, set[str]] = {}
    for label, runs in (("baseline", base), ("after", after)):
        for i, r in enumerate(runs, 1):
            rev = r.get("meta", {}).get("git_rev") or "unknown"
            if rev.endswith("-dirty"):
                print(f"⚠ {label} 第 {i} 份产自脏工作树 (git_rev={rev}) — "
                      f"这批数字无法凭 sha 复现, 引用时须连这句一起写")
            sha.setdefault(label, set()).add(_rev_sha(rev))
    shared = (sha.get("baseline", set()) & sha.get("after", set())) - {"unknown"}
    if shared:
        print(f"⚠ baseline 与 after 共用 git_rev 尾段 {sorted(shared)} — "
              f"两批产自同一版本代码, 请确认不是拷贝错文件 (审查 I-2 的弱形态)")


def _check_groups(base: list[dict], after: list[dict]) -> None:
    """条款读得到组, 且双列闸两侧同分母 —— 否则拒绝给结论 (照 run_routing_eval 的组量闸)。

    整组缺席时 `_g` 会抛 KeyError, 尚且吵; 真正静默的是**组量变了**: u1_doc 从 27 缩到 20,
    exact 差值照样算得出来, 只是拿两把不同长度的尺子相减, 而条款 4/7 的判据是绝对题数。
    """
    need = ("dev", "heldout", *DUAL_GATE_GROUPS.values())
    for label, runs in (("baseline", base), ("after", after)):
        for i, r in enumerate(runs, 1):
            groups = r["summary"]["by_group"]
            missing = [name for name in need if name not in groups]
            if missing:
                raise SystemExit(
                    f"{label} 第 {i} 份 run 缺 group {missing} — 条款 2/3/4/7 无原料, 拒绝给结论")
            for name in ("dev", "heldout"):
                if groups[name]["n"] != GROUP_N:
                    raise SystemExit(
                        f"{label} 第 {i} 份 run 的 {name} 组量 {groups[name]['n']} ≠ {GROUP_N} — "
                        f"条款 2 的百分比分母写死 {GROUP_N} (spec §5.2), 组量改了必须重审判据")
    for clause, group in DUAL_GATE_GROUPS.items():
        sizes = sorted({_g(r, group, "n") for r in [*base, *after]})
        if len(sizes) > 1:
            raise SystemExit(
                f"{clause} 的 {group} 组量在六份 run 间不一致 {sizes} — "
                f"exact 差值会拿两把不同长度的尺子相减, 拒绝给结论")


def validate_inputs(base: list[dict], after: list[dict]) -> None:
    if len(base) != 3 or len(after) != 3:
        raise SystemExit(f"baseline/after 各需 3 份, 得 {len(base)}/{len(after)} — 三遍纪律")
    for label, runs in (("baseline", base), ("after", after)):
        for i, r in enumerate(runs, 1):
            if "meta" not in r or not r["meta"].get("generated_at"):
                raise SystemExit(f"{label} 第 {i} 份 run 缺 meta.generated_at — "
                                 f"先用 Task 1 修缮后的 run_routing_eval 重产")
        # 批内重复是最有欺骗性的一格: 同一份 run 喂三遍, 条款 1 的「每遍」恒等于那一遍,
        # 均值恒等于那一遍, clause6 更会报出「三遍全稳」—— 三遍纪律形同虚设却全绿。
        stamps = [r["meta"]["generated_at"] for r in runs]
        if len(set(stamps)) != len(stamps):
            raise SystemExit(
                f"{label} 三份 run 的 meta.generated_at 有重复 {sorted(stamps)} — "
                f"同一份 run 被当成多遍喂进来, 三遍纪律与 clause6 稳定性都会是假象")
    bdump = {json.dumps(r["summary"], sort_keys=True) for r in base}
    adump = {json.dumps(r["summary"], sort_keys=True) for r in after}
    # 两个条件是 AND: 确定性跑批下两批 summary 逐字相同是合法的, 只有连 meta (跑批时刻)
    # 都撞上才说明这是同一批文件被当成两批喂进来。
    if bdump & adump and {r["meta"]["generated_at"] for r in base} & {
            r["meta"]["generated_at"] for r in after}:
        raise SystemExit("baseline 与 after 内容相同 (含同 meta) — 疑似拷贝错文件 (审查 I-2)")
    _check_groups(base, after)
    _warn_provenance(base, after)


def _dual_gate(base: list[dict], after: list[dict], group: str) -> dict[str, Any]:
    fb = sum(_g(r, group, "fatal") for r in base) / 3
    fa = sum(_g(r, group, "fatal") for r in after) / 3
    eb = sum(_g(r, group, "exact") for r in base) / 3
    ea = sum(_g(r, group, "exact") for r in after) / 3
    return {"group": group, "fatal": {"base": round(fb, 2), "after": round(fa, 2)},
            "exact": {"base": round(eb, 2), "after": round(ea, 2)},
            "pass": fa <= fb + 1e-9 and eb - ea <= 1 + 1e-9,
            "note": "widen-only 机制下 fatal 半由构造保证, 判别力在 exact 半 (spec §4.2)"}


def verdict(base: list[dict], after: list[dict]) -> tuple[dict, int]:
    validate_inputs(base, after)
    c1 = all(r["summary"]["fatal_excl_final"] == 0 and r["summary"]["legacy_exact"] >= LEGACY_FLOOR
             for r in after)
    dev = sum(_g(r, "dev", "exact") for r in after) / 3 / GROUP_N * 100
    hold = sum(_g(r, "heldout", "exact") for r in after) / 3 / GROUP_N * 100
    c2, c3 = hold >= dev - C2_GAP_PT, sum(_g(r, "dev", "exact") for r in after) / 3 >= C3_DEV_MIN
    out: dict[str, Any] = {
        "clause1": {"pass": c1, "per_run": [
            {"fatal": r["summary"]["fatal_excl_final"], "legacy": r["summary"]["legacy_exact"],
             "fatal_ids": r["summary"]["fatal_ids_excl_final"]} for r in after]},
        "clause2": {"pass": c2, "dev_pct": round(dev, 2), "heldout_pct": round(hold, 2),
                    "majority_note": "dev/heldout 多数类基线 100%, 不得单独引用 (U3 §7.1)"},
        "clause3": {"pass": c3, "dev_mean": round(sum(_g(r, "dev", "exact") for r in after) / 3, 2)},
    }
    for name, grp in DUAL_GATE_GROUPS.items():
        out[name] = _dual_gate(base, after, grp)
    out["clause5_final_report_only"] = [
        {d["id"]: d["pred"] for d in r["detail"] if d["group"] == "final"} for r in after]
    preds = [{d["id"]: d["pred"] for d in r["detail"]} for r in after]
    # 已知盲点 (条款 6 只报告, 不进 rc): 题号全集取自第一遍。若某题只在第二/三遍出现
    # (三遍喂了不同版本 gold), 它不会被点名。组量闸已挡住成组的漂移, 单题漂移仍是盲的。
    out["clause6_unstable"] = sorted(
        k for k in preds[0] if len({p.get(k) for p in preds}) > 1)
    rc = 0 if all(out[c]["pass"] for c in ("clause1", "clause2", "clause3", "clause4", "clause7")) else 1
    return out, rc


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--baseline", nargs=3, required=True)
    p.add_argument("--after", nargs=3, required=True)
    p.add_argument("--output")
    a = p.parse_args(argv)

    def load(f: str) -> dict:
        return json.loads(Path(f).read_text(encoding="utf-8"))

    out, rc = verdict([load(f) for f in a.baseline], [load(f) for f in a.after])
    if a.output:
        Path(a.output).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for k in ("clause1", "clause2", "clause3", "clause4", "clause7"):
        print(k, "PASS" if out[k]["pass"] else "⛔ 触发", json.dumps(
            {kk: vv for kk, vv in out[k].items() if kk not in ("pass", "per_run")},
            ensure_ascii=False))
        # 条款 1 是主闸, 而它除 per_run 外没有别的键 —— 上面那行剩个空 `{}`, 主闸的逐遍
        # 数字就只在 --output 的 json 里才看得见。补逐遍一行 (只有 id 与数, 无题面)。
        for i, run in enumerate(out[k].get("per_run", []), 1):
            print(f"  r{i}: fatal={run['fatal']}  legacy={run['legacy']} (floor {LEGACY_FLOOR})"
                  f"  fatal_ids={run['fatal_ids']}")
    print("clause5 (只报告):", out["clause5_final_report_only"])
    print("clause6 unstable:", out["clause6_unstable"])
    print(f"rc={rc}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
