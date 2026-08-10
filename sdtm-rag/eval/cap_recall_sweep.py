"""§2.A2: 零 LLM 的 per-section 配额 x source recall 全集扫描。

背景 (kickoff `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md` §2.A2): 层② 用 LLM judge
作锚, 依据是"gold 判据对挤占结构性失明 (S1 前置注入把 gold 钉死了)"。该论断有一个
**从未写出的限定条件 —— 它只对 S1 有注入的那部分 gold 成立**。挤占最重的 8 题里
3 题 (q38/q39/q81) S1 注入为 0, 那几题的 source recall 对配额**完全有判别力**。
故同一件事可以用既有的确定性判据、零 LLM 调用测出来。

管线与层② 逐字相同 (`eval.crowding_ab.build_arm`, 不重写):
    fuse(fuse_out) -> apply_section_cap(cap) -> 截 top_k -> S1 注入
配额档 `{None, 1, 2, 3}`, A = cap None = 生产现状。

━━ 这把尺子的能力边界 (**开跑前写死, 不许看到数据再改**) ━━

`check_source_recall` 在本题集上**接近天花板**: 140 题里 138 题已经是 1.0
(仅 q38=0.3333 / q126=0.5), 上限余量 0.83pt。⇒ **本实验的上行与下行分辨力不对称**:

  * **上行**: 最多只能在 2 道题上看到改善 —— "净升"的幅度天然被封顶, 不能因为
    "只升了 1 题"就说效应小;
  * **下行**: 138 题都可能掉, 分辨力完整。

⇒ 本实验能**确定性回答**的是: **配额会不会伤 gold 召回** (下行), 以及
**配额能不能救 q38/q126** (上行的全部可测范围)。
它**回答不了**"配额是否改善答案质量" —— 那是层② 想测而没测成的东西 (量具饱和)。
**别把 source recall 的改善直接读成答案质量的改善** (kickoff §2.A2 限制 2)。

━━ 判定规则 (**先于数据写死**, 含 default 行与自毁条款; 硬规矩 8) ━━

自毁条款 (排在所有肯定性结论之前):
  V1. 任一题 A 臂 (cap=None) 与生产 `rag.retrieve` 逐位不同 -> `VOID_WIRING`。
      管线接错时后面所有对比都无意义。
  V2. 全部 cap 档在**全部题**上 context 与 A 逐位相同 -> `VOID_NO_EFFECT_MEASURED`。
      配额压根没生效, 同分是废话不是证据。

逐档结论 (只统计 **context 确实变了**的题; ctx 未变的题同分不构成任何证据):
  improved = recall > A 的题数; regressed = recall < A 的题数。
  R1. regressed == 0 且 improved >= 1        -> `SAFE_AND_HELPS`  (该档可做, 且救了题)
  R2. regressed == 0 且 improved == 0        -> `INERT_ON_THIS_RULER`
      (在本尺子上无可测效应 —— **鉴于天花板饱和, 这是预期的 null, 不等于"无害"**)
  R3. improved >= 1 且 regressed >= 1        -> `MIXED` (逐题看降的是什么题型, 分档施配额)
  R4. improved == 0 且 regressed >= 1        -> `HARMFUL` (该档确定性有害, 廉价关掉)
  R5. 以上都不落 (不可能, 留作 default 行)   -> `UNCLASSIFIED` (必须人工查明, 不许当无事)

全局结论 = 各档结论的组合, 由 `overall_verdict()` 给出, 同样写死。

━━ 分组读法 (kickoff §2.A2 限制 3) ━━
S1 注入 >= 1 的题, source recall 对**被 S1 钉死的那几条 gold** 仍然失明 (硬规矩 9)。
故逐题记录 `s1_injected` 并按 `s1_injected == 0` / `> 0` 分组给出两套统计。
**只有 s1_injected == 0 的那组是纯检索层效果。**

跑批 (从 sdtm-rag/ 起, 零 LLM 调用):
    .venv/bin/python -m eval.cap_recall_sweep \\
        --output evidence/checkpoints/cap_recall_sweep.json
    # 从落盘 JSON 零成本重算 (证据文档里的数字都出自这里)
    .venv/bin/python -m eval.cap_recall_sweep --summarize evidence/checkpoints/cap_recall_sweep.json
"""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter

from eval.crowding_ab import _engine, _fused_candidates, build_arm

# 配额档。第一个必须是 None (A = 生产现状), 其余为待测档。
CAPS: tuple[int | None, ...] = (None, 1, 2, 3)


def _arm_label(cap: int | None) -> str:
    return "A" if cap is None else f"cap{cap}"


def _composition(chunks) -> list[dict]:
    return [{"source": c.source, "section": c.section,
             "via_lookup": bool(getattr(c, "via_lookup", False))} for c in chunks]


def _positional_diff(a: list[dict], b: list[dict]) -> int:
    """两组 context 的逐位不同位置数 (长度不等时缺位算不同)。

    与 `eval.crowding_ab._composition_diff` 同口径: 集合相同但顺序不同, 对下游仍是
    不同输入, 不算"相同"。
    """
    n = max(len(a), len(b))
    key = lambda x: (x["source"], x["section"])  # noqa: E731
    pa = [key(x) for x in a] + [None] * (n - len(a))
    pb = [key(x) for x in b] + [None] * (n - len(b))
    return sum(1 for x, y in zip(pa, pb, strict=True) if x != y)


def _max_cluster(comp: list[dict]) -> tuple[int, str | None]:
    cnt = Counter(x["section"] for x in comp if x["section"] is not None)
    if not cnt:
        return 0, None
    sec, n = cnt.most_common(1)[0]
    return n, sec


def run_sweep(rag, test_set, top_k: int, fuse_out: int, caps=CAPS) -> list[dict]:
    """逐题跑全部配额档。query 向量钉死 —— embedding 抖动不是本实验要量的东西。

    Chroma HNSW 的进程内抖动仍在: 它若出现会表现为 A 臂与生产不逐位相同, 由 V1
    自毁条款接住, 不许当噪声吞掉。
    """
    from eval.run_eval import check_source_recall

    rows: list[dict] = []
    real_embed = rag._embed_query
    try:
        for i, q in enumerate(test_set, 1):
            question = q["question"]
            vec = real_embed(question)
            rag._embed_query = lambda _t, _v=vec: list(_v)

            prod = [c.chunk_id for c in rag.retrieve(question, top_k=top_k)]
            fused, q_emb = _fused_candidates(rag, question, fuse_out)

            arms: dict[str, dict] = {}
            for cap in caps:
                final, capped, dropped = build_arm(rag, question, fused, q_emb, cap, top_k)
                comp = _composition(final)
                sources = [c.source for c in final]
                sections = [getattr(c, "section", None) for c in final]
                recall, hits, misses = check_source_recall(
                    sources,
                    q.get("expected_sources", []),
                    any_of=q.get("expected_sources_any"),
                    retrieved_sections=sections,
                )
                capped_ids = {c.chunk_id for c in capped}
                via_lookup = [c for c in final if getattr(c, "via_lookup", False)]
                injected = [c for c in via_lookup if c.chunk_id not in capped_ids]
                mc, mc_sec = _max_cluster(comp)
                arms[_arm_label(cap)] = {
                    "cap": cap,
                    "source_recall": round(recall, 4),
                    "source_hits": hits,
                    "source_misses": misses,
                    "seats": len(final),
                    "seats_before_s1": len(capped),
                    "s1_injected": len(injected),
                    "s1_total_in_final": len(via_lookup),
                    # S1 不受配额约束, 可能把被配额挤走的同名 section 又带回来
                    "s1_reintroduced_capped_section": [
                        {"source": c.source, "section": c.section}
                        for c in injected if c.section in dropped
                    ],
                    "max_cluster": mc,
                    "max_cluster_section": mc_sec,
                    "composition": comp,
                }
                if cap is None:
                    ids = [c.chunk_id for c in final]
                    arms["A"]["equals_production"] = ids == prod
                    arms["A"]["positional_diff_vs_production"] = sum(
                        1 for j in range(max(len(ids), len(prod)))
                        if (ids[j] if j < len(ids) else None)
                        != (prod[j] if j < len(prod) else None))

            base = arms["A"]["composition"]
            for label, a in arms.items():
                a["ctx_diff_vs_A"] = _positional_diff(base, a["composition"])

            rows.append({
                "id": q["id"],
                "category": q["category"],
                "question": question,
                "out_of_scope": bool(q.get("out_of_scope", False)),
                "n_fused": len(fused),
                "arms": arms,
            })
            deltas = "  ".join(
                f"{_arm_label(c)}:{arms[_arm_label(c)]['source_recall']:.4f}"
                f"({arms[_arm_label(c)]['seats']}席)" for c in caps)
            print(f"[{i}/{len(test_set)}] {q['id']:>5} "
                  f"A{'==' if arms['A']['equals_production'] else '≠'}prod  "
                  f"S1+{arms['A']['s1_injected']}  maxcl={arms['A']['max_cluster']:2d}  "
                  f"{deltas}", flush=True)
    finally:
        rag._embed_query = real_embed
    return rows


# ---- 判定 (规则写死在 docstring, 此处只是实现) --------------------------------


def _classify(improved: int, regressed: int) -> str:
    if regressed == 0 and improved >= 1:
        return "SAFE_AND_HELPS"          # R1
    if regressed == 0 and improved == 0:
        return "INERT_ON_THIS_RULER"     # R2
    if improved >= 1 and regressed >= 1:
        return "MIXED"                   # R3
    if improved == 0 and regressed >= 1:
        return "HARMFUL"                 # R4
    return "UNCLASSIFIED"                # R5 (default 行)


def _arm_stats(scored: list[dict], label: str, subset=None) -> dict:
    rows = [r for r in scored if subset is None or subset(r)]
    changed = [r for r in rows if r["arms"][label]["ctx_diff_vs_A"] > 0]
    imp = [r["id"] for r in changed
           if r["arms"][label]["source_recall"] > r["arms"]["A"]["source_recall"]]
    reg = [r["id"] for r in changed
           if r["arms"][label]["source_recall"] < r["arms"]["A"]["source_recall"]]
    tie = len(changed) - len(imp) - len(reg)
    n = len(rows)
    mean_a = sum(r["arms"]["A"]["source_recall"] for r in rows) / n if n else 0.0
    mean_x = sum(r["arms"][label]["source_recall"] for r in rows) / n if n else 0.0
    return {
        "n": n,
        "n_ctx_changed": len(changed),
        "improved": len(imp), "improved_ids": imp,
        "regressed": len(reg), "regressed_ids": reg,
        "tie_among_changed": tie,
        "net": len(imp) - len(reg),
        "mean_recall_A": round(mean_a, 6),
        "mean_recall": round(mean_x, 6),
        "delta_mean_pt": round((mean_x - mean_a) * 100, 4),
        "mean_seats": round(sum(r["arms"][label]["seats"] for r in rows) / n, 2) if n else 0,
        "verdict": _classify(len(imp), len(reg)),
    }


def overall_verdict(per_arm: dict) -> tuple[str, str]:
    """全局结论 —— 由各档结论组合而成, 组合规则同样写死。"""
    vs = {k: v["verdict"] for k, v in per_arm.items()}
    if any(v == "UNCLASSIFIED" for v in vs.values()):
        return "UNCLASSIFIED", "有档落进 default 行 —— 必须人工查明, 不许当无事"
    if any(v == "SAFE_AND_HELPS" for v in vs.values()):
        best = [k for k, v in vs.items() if v == "SAFE_AND_HELPS"]
        return "CAP_HELPS", f"{'/'.join(best)} 零回归且有改善 -> 挤占有害被确定性证明, Task 7 可做"
    if any(v == "MIXED" for v in vs.values()):
        return "CAP_MIXED", "有升有降 -> 逐题看降的是什么题型, 可能需按题型分档施配额"
    if all(v == "HARMFUL" for v in vs.values()):
        return "CAP_HARMFUL", "全档只降不升 -> 配额有害, 这条线廉价关掉"
    return "CAP_INERT", ("全档在本尺子上无可测效应 —— **鉴于天花板饱和 (138/140 已 1.0), "
                         "这是预期的 null**, 不等于'挤占无害'")


def hidden_loss_shadow(rows: list[dict], labels: list[str]) -> dict:
    """分数没动但**命中集合变了**的题 —— OR 组把回归吃掉的取证。

    kickoff §2.A′ 末尾的存量债: q115 / q117 的 OR 组里有严格弱于同组其他成员的成员,
    且该 OR 组是这两题**唯一的计分单位** ⇒ 只命中最弱成员照样得 `source_recall = 1.0`。
    **一动检索, OR 组就会把回归吃掉、让分数纹丝不动。** 本实验就是"动检索"。

    故除了比分数, 还要比 `source_hits` 集合: 分数相同但 A 命中的某条 gold 在该档掉了,
    就是一次**被判据吞掉的退化**。它不进 improved/regressed (那是分数口径, 不许偷改),
    单列成影子信号供人逐条判。
    """
    out: dict = {}
    for label in labels:
        lost = []
        for r in rows:
            if r["out_of_scope"]:
                continue
            a, x = r["arms"]["A"], r["arms"][label]
            if x["source_recall"] != a["source_recall"]:
                continue                      # 分数已经反映了, 不属"影子"
            gone = [h for h in a["source_hits"] if h not in x["source_hits"]]
            if gone:
                lost.append({"id": r["id"], "recall": a["source_recall"],
                             "hits_lost": gone,
                             "hits_A": a["source_hits"], "hits_arm": x["source_hits"]})
        out[label] = {"n": len(lost), "ids": [x["id"] for x in lost], "detail": lost}
    return out


def analyze(rows: list[dict]) -> dict:
    scored = [r for r in rows if not r["out_of_scope"]]
    labels = [_arm_label(c) for c in CAPS if c is not None]

    wiring_fail = [r["id"] for r in rows if not r["arms"]["A"]["equals_production"]]
    any_ctx_change = any(r["arms"][l]["ctx_diff_vs_A"] > 0 for r in rows for l in labels)

    headroom_ids = [r["id"] for r in scored if r["arms"]["A"]["source_recall"] < 1.0]
    out: dict = {
        "n_total": len(rows),
        "n_scored": len(scored),
        "n_out_of_scope": len(rows) - len(scored),
        # 天花板声明 —— 必须与任何"净升"数字并排陈列
        "ceiling": {
            "n_below_1.0_in_A": len(headroom_ids),
            "ids_below_1.0_in_A": headroom_ids,
            "headroom_pt": round(
                sum(1.0 - r["arms"]["A"]["source_recall"] for r in scored) / len(scored) * 100, 4
            ) if scored else 0.0,
            "note": "上行分辨力只覆盖这几题; 下行分辨力覆盖全部计分题。两者不对称。",
        },
        "wiring_check": {"failed_ids": wiring_fail, "pass": not wiring_fail},
        "arms": {l: _arm_stats(scored, l) for l in labels},
        # kickoff §2.A2 限制 3: S1 注入 >0 的题, 判据对被钉死的 gold 失明
        # 分数没动但命中集合变了 —— OR 组把回归吃掉的取证 (不进 improved/regressed)
        "hidden_loss_shadow": hidden_loss_shadow(rows, labels),
        "by_s1_injection": {
            "s1_zero": {l: _arm_stats(scored, l, lambda r: r["arms"]["A"]["s1_injected"] == 0)
                        for l in labels},
            "s1_nonzero": {l: _arm_stats(scored, l, lambda r: r["arms"]["A"]["s1_injected"] > 0)
                           for l in labels},
        },
    }
    if wiring_fail:
        out["conclusion"], out["conclusion_text"] = (
            "VOID_WIRING", f"{len(wiring_fail)} 题 A 臂与生产不逐位相同 -> 管线接错, 整轮作废")
    elif not any_ctx_change:
        out["conclusion"], out["conclusion_text"] = (
            "VOID_NO_EFFECT_MEASURED", "全部档在全部题上 context 与 A 逐位相同 -> 配额没生效")
    else:
        out["conclusion"], out["conclusion_text"] = overall_verdict(out["arms"])
    return out


def print_report(rows: list[dict], a: dict) -> None:
    labels = [_arm_label(c) for c in CAPS if c is not None]
    print("\n" + "=" * 72)
    print("§2.A2 配额 x source recall 全集扫描")
    print("=" * 72)
    print(f"计分题 {a['n_scored']} (out_of_scope {a['n_out_of_scope']} 不计分)")
    c = a["ceiling"]
    print(f"⚠ 天花板: A 臂只有 {c['n_below_1.0_in_A']} 题 < 1.0 ({', '.join(c['ids_below_1.0_in_A']) or '无'}), "
          f"上限余量 {c['headroom_pt']:.2f}pt —— 上行分辨力仅覆盖这几题, 下行覆盖全部")
    print(f"接线闸 (A == 生产 retrieve 逐位): "
          f"{'PASS' if a['wiring_check']['pass'] else 'FAIL ' + str(a['wiring_check']['failed_ids'])}")

    print("\n| 档 | 均值 | Δ vs A | ctx 变了的题 | improved | regressed | 同分(ctx变了) | 平均席位 | 逐档结论 |")
    print("|---|---|---|---|---|---|---|---|---|")
    a0 = a["arms"][labels[0]]["mean_recall_A"]
    print(f"| A (无配额) | {a0:.4f} | — | — | — | — | — | "
          f"{sum(r['arms']['A']['seats'] for r in rows if not r['out_of_scope']) / a['n_scored']:.2f} | 基准 |")
    for l in labels:
        s = a["arms"][l]
        print(f"| {l} | {s['mean_recall']:.4f} | {s['delta_mean_pt']:+.4f}pt | "
              f"{s['n_ctx_changed']} | {s['improved']} {s['improved_ids'] or ''} | "
              f"{s['regressed']} {s['regressed_ids'] or ''} | {s['tie_among_changed']} | "
              f"{s['mean_seats']} | {s['verdict']} |")

    for group, title in (("s1_zero", "S1 注入 = 0 (纯检索层效果, 判据完全有判别力)"),
                         ("s1_nonzero", "S1 注入 > 0 (判据对被 S1 钉死的 gold 失明)")):
        print(f"\n分组: {title}")
        for l in labels:
            s = a["by_s1_injection"][group][l]
            print(f"  {l:>5}: n={s['n']:3d} ctx变={s['n_ctx_changed']:3d} "
                  f"improved={s['improved']} {s['improved_ids'] or ''} "
                  f"regressed={s['regressed']} {s['regressed_ids'] or ''} "
                  f"Δ均值={s['delta_mean_pt']:+.4f}pt")

    print("\n影子信号 (分数没动但命中集合变了 —— OR 组把回归吃掉的取证, 不进 improved/regressed):")
    for l in labels:
        s = a["hidden_loss_shadow"][l]
        print(f"  {l:>5}: {s['n']} 题 {s['ids'] or ''}")
        for d in s["detail"]:
            print(f"         {d['id']} (recall 仍 {d['recall']}) 掉了: {d['hits_lost']}")

    print(f"\n结论: {a['conclusion']} — {a['conclusion_text']}")
    print("\n⚠ 读法 (写死在脚本 docstring, 不许在这里放宽):")
    print("  1. 本尺子测的是 **gold 召回**, 不是答案质量。source recall 的改善"
          "**不得**直接读成答案质量的改善。")
    print("  2. 上行分辨力受天花板限制 (见上); '净升幅度小' 不等于 '效应小'。")
    print("  3. S1 注入 >0 的题, 判据只对 gold 的剩余部分有判别力 —— 分组读。")


def summarize(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        payload = json.load(f)
    rows = payload["rows"]
    a = analyze(rows)          # 刻意重算而非读落盘 analysis, 不一致就露馅
    print(f"# {path}")
    m = payload["_meta"]
    print(f"top_k={m['top_k']} fuse_out={m['fuse_out']} hybrid_pool={m['hybrid_pool']} "
          f"caps={m['caps']} 题集={m['test_set']}")
    print_report(rows, a)
    stored = payload.get("analysis", {})
    if stored.get("conclusion") != a["conclusion"]:
        print(f"\n⚠ 落盘结论 ({stored.get('conclusion')}) 与重算 ({a['conclusion']}) 不一致")
    else:
        print("\n落盘结论与重算一致。")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="§2.A2 配额 x source recall 全集扫描 (零 LLM)")
    p.add_argument("--test-set", default="eval/test_set_v3.yml")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--fuse-out", type=int, default=60,
                   help="融合输出放长到多少再施配额 (与层② 同口径; 放长安全, 加深池不安全)")
    p.add_argument("--limit", type=int, default=None, help="只跑前 N 题 (冒烟用)")
    p.add_argument("--output", default="evidence/checkpoints/cap_recall_sweep.json")
    p.add_argument("--summarize", default=None, metavar="JSON")
    p.add_argument("--fused-profile", default=None, metavar="QIDS",
                   help="逗号分隔题号: 只报融合候选池的簇构成 (零 LLM, 不跑配额)")
    args = p.parse_args(argv)

    if args.summarize:
        return summarize(args.summarize)

    from eval.run_eval import load_test_set

    if args.fused_profile:
        qs = {q["id"]: q for q in load_test_set(args.test_set)}
        wanted = [s.strip() for s in args.fused_profile.split(",")]
        missing = [i for i in wanted if i not in qs]
        if missing:
            raise SystemExit(f"题号不在 {args.test_set}: {missing}")
        rag = _engine(args.top_k)
        for qid in wanted:
            fused, _ = _fused_candidates(rag, qs[qid]["question"], args.fuse_out)
            cnt = Counter(c.section for c in fused)
            sec, n = cnt.most_common(1)[0]
            print(f"{qid}: n_fused={len(fused)} distinct_sections={len(cnt)} "
                  f"最大簇={n} (§{sec}) 占比={n / len(fused):.1%}")
        return 0

    test_set = load_test_set(args.test_set)
    if args.limit:
        test_set = test_set[: args.limit]
    rag = _engine(args.top_k)

    t0 = time.time()
    rows = run_sweep(rag, test_set, args.top_k, args.fuse_out)
    a = analyze(rows)

    payload = {
        "_meta": {
            "what": "§2.A2 per-section 配额 x check_source_recall 全集扫描 (零 LLM 调用)",
            "pipeline": "fuse(fuse_out) → apply_section_cap(cap) → 截 top_k → S1 注入",
            "caps": list(CAPS),
            "top_k": args.top_k, "fuse_out": args.fuse_out,
            "hybrid_pool": rag.hybrid_pool,
            "test_set": args.test_set,
            "ruler_ceiling": "A 臂 138/140 已是 1.0 ⇒ 上行分辨力仅覆盖 2 题, "
                             "下行覆盖全部计分题。两者不对称, 引用必须并排声明。",
            "not_measured": "答案质量。source recall 的改善不得读成答案质量的改善。",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "elapsed_sec": round(time.time() - t0, 1),
        },
        "analysis": a,
        "rows": rows,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print_report(rows, a)
    print(f"\n明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
