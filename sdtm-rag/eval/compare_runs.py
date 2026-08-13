"""U3 Task 1: run_eval 产物的逐题比对与跨遍稳定性 (spec 2026-08-13 §4).

为什么要它: U2 §5-1 实测检索有非确定性 (源在 embedding API, 同一 query 6 次得 2 种向量),
任何「逐题 Δ0」都必须连跑 3 遍才有意义。此前各单元的逐题比对都是一次性 ad hoc 脚本,
没有测试守护 —— 而比对器自己出错的表现是**静默报无差异**, 与「真的没差异」不可区分。

红线: 只吐 id 与分数, 不吐 question 文本 (id 形如 docs_v1_qNN, 不含语料内容)。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_scores(path: str | Path) -> dict[str, float]:
    """读 run_eval 产物, 返回 {question_id: source_recall}."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    results = data["results"]
    if not results:  # 空产物比对恒等于「无差异」
        raise ValueError(f"{path}: results 为空 —— 空比对恒真, 拒绝继续")
    out: dict[str, float] = {}
    for r in results:
        if r["id"] in out:  # 后者覆盖前者 = 静默改变比对
            raise ValueError(f"{path}: id 重复 {r['id']!r}")
        out[r["id"]] = r["source_recall"]
    return out


def load_summary_avg(path: str | Path) -> float | None:
    """读产物**自称**的 `summary.source_recall_avg`; 缺 summary / 缺该键返回 None.

    为什么不自己算: run_eval 的 source_recall_avg 先剔掉 out_of_scope 题再平均 (那些题
    expected_sources 为空、恒得 1.0 = 白送分), 而 `results` 里**保留**这些行。比对器若
    自己 sum(results)/len(results), 就会得到一个与产物自称值不同、却同名的 avg ——
    cards 题集实测 0.8333 vs 0.8229 (48 计分 + 3 out_of_scope: 0.8229*48+3 = 42.5, /51)。

    静默回退自算正是这个 bug 的形状, 故缺键时返回 None、由调用方打 n/a: 复制口径就会漂移,
    世界上只许有一个 avg。逐题比对不受影响 —— 按 id 比, 与除数无关。
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return (data.get("summary") or {}).get("source_recall_avg")


def diff_scores(a: dict[str, float],
                b: dict[str, float]) -> dict[str, tuple[float | None, float | None]]:
    """逐题差异 {id: (a, b)}; 只含不相等的题, 缺席一侧记 None.

    键集合取并集而非交集: 「一边少了几题」必须表现为差异, 不许被读成无差异。
    """
    return {k: (a.get(k), b.get(k))
            for k in sorted(set(a) | set(b))
            if a.get(k) != b.get(k)}


def unstable_ids(runs: list[dict[str, float]]) -> dict[str, list[float | None]]:
    """跨 N 遍不稳定的题 {id: [每遍分数]}. 少于 2 遍拒绝 —— 单遍返回 {} 会被读成「一致」."""
    if len(runs) < 2:
        raise ValueError(f"稳定性需要 >= 2 遍, 收到 {len(runs)} 遍")
    keys: set[str] = set().union(*runs)
    out: dict[str, list[float | None]] = {}
    for k in sorted(keys):
        vals = [r.get(k) for r in runs]
        if len(set(vals)) > 1:
            out[k] = vals
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="run_eval 产物逐题比对 (只吐 id, 不吐题面)")
    p.add_argument("runs", nargs="+", help="两个或以上 run_eval --output 产物")
    args = p.parse_args(argv)
    # 「连跑 3 遍」最常见的操作事故: 循环里 --output 忘了带轮次变量, 三遍写进同一个文件。
    # 此时三份「产物」字面上是同一个文件, 比对器会给出干净的 rc=0 稳定性证明 ——
    # 与 load_scores 挡掉的「空产物比对恒真」是同一格危害。按内容哈希去重不行:
    # run_eval 的 result dict 无 latency/时间戳, 两遍真独立且恰好稳定的跑批可以字节相同。
    resolved = [Path(f).resolve() for f in args.runs]
    if len(set(resolved)) != len(resolved):
        p.error("同一产物路径传了多次 —— 自我比对恒等于稳定")
    scored = [load_scores(f) for f in args.runs]
    for i, f in enumerate(args.runs, 1):
        avg = load_summary_avg(f)
        shown = f"{avg:.4f}" if avg is not None else "n/a (产物无 summary.source_recall_avg)"
        # rows= 是**比对的行数**, 不是 avg 的除数 (avg 已剔 out_of_scope, 分母更小)。
        # 两个数并排放且都叫 n 时, 读者拿 avg*n 对账必然对不上 —— U2 的 51 池 vs 48 池同一个坑。
        print(f"run {i}: rows={len(scored[i - 1])} avg={shown}  {f}")
    unstable = unstable_ids(scored)
    print(f"unstable across {len(scored)} runs: {len(unstable)}")
    for k, vals in unstable.items():
        print(f"  {k}: {vals}")
    if len(scored) == 2:
        d = diff_scores(scored[0], scored[1])
        print(f"pairwise diff: {len(d)}")
        for k, (va, vb) in d.items():
            print(f"  {k}: {va} -> {vb}")
    return 1 if unstable else 0


if __name__ == "__main__":
    sys.exit(main())
