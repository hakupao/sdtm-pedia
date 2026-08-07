"""层②: context A/B1/B2 对照 —— 判定同质簇挤占是否**有害**。

层① 只能证明挤占存在。它是否有害, 用 gold 判据永远判不出来: S1 前置注入
(_merge_lookup_first) 已经确定性地保证了 gold 恒在 top-k, 判据因而对
"剩余席位的质量"结构性失明。故本模块的锚是**答案正确性** (LLM judge),
它在 section 名这个代理量之外。

三组同池同序, 唯一差别是配额 (Task 5 定稿: **放长融合输出, 不加深池**):
  A  = 无配额 (生产现状)
  B1 = 同名 section 限 1 席
  B2 = 同名 section 限 2 席
S1 注入的 chunk 三组一律豁免 (确定性 gold, 不属被检验对象)。

池一律用生产 hybrid_pool=30 (POOL_DEEP_OK=false: 加深池改 RRF 分数表, 实测 e2e
A/B 4032 对不一致 vs A/A 0 对)。三组统一把 _hybrid_fuse 的**输出** k 从 15 放长到
60 再施配额 —— FUSE_OUT_DEEP_OK=true 且**代码结构可证**: _hybrid_fuse 里 k 只出现在
最后一行 ranked[:k], best 字典 / RRF 分数表 / sorted 全排序都与 k 无关, sorted 稳定且
tie 由插入序决定 ⇒ 深融合输出的前 15 名恒等于浅融合输出 (实测 140/140 逐位相同)。
配额语义来自 server.diversity.apply_section_cap —— Task 7 的生产代码用同一份, 不重写。

**管线顺序定死: fuse(60) → 配额 → 截 15 → S1 注入**, 与 Task 7 的生产改法一致。
配额放在 S1 之前, 是为了不让配额挤掉 S1 的确定性 gold (那会让 B 组因与挤占无关的
原因掉 recall)。**已知限制**: S1 是前插且不受配额约束的, 它**可能把被配额挤走的
同名 section 又带回来, 部分抵消配额** —— 故逐题记录 S1 注入条数与 section, 并对
"带回被挤走 section"的题单独标注 (`s1_reintroduced_capped_section`)。

跑批 (从 sdtm-rag/ 起):
  # 先跑退化检查 (零 LLM 调用, 确认管线接对了再花钱)
  .venv/bin/python -m eval.crowding_ab --dry-run
  # 正式跑 (12 题 × 3 组答题 + judge)
  .venv/bin/python -m eval.crowding_ab --fuse-out 60 \\
    --output evidence/checkpoints/crowding_layer2.json
"""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter

from server.diversity import apply_section_cap

# 三组的配额档。A 组 cap=None 即生产现状。
ARMS = (("A", None), ("B1", 1), ("B2", 2))
# 判定门槛 (spec §2.2b, 先写死, 不许看到数据再改)
NET_GAIN_THRESHOLD = 3
MAX_REGRESSED = 1
# 同分题达到这个数, 整个层② 判定作废 —— 锤子选错, 换锚重做
TIE_ABORT = 8


def _fused_candidates(rag, question, fuse_out):
    """生产链的前半段, 但融合输出放长到 fuse_out (不加深池)。

    Task 5 实测: 池不变时深融合输出的前 15 名恒等于浅融合输出 (140/140 逐位相同),
    故 A 组用它取前 15 与生产一致; B 组则有更长的排序可供配额后补位。
    """
    q_emb = rag._embed_query(question)
    pool = max(rag.top_k, rag.hybrid_pool)          # 生产值, 不放大
    dense = rag._search(question, pool, None, query_embedding=q_emb)
    bm25 = rag._bm25_search(question, pool, None)
    return rag._hybrid_fuse(dense, bm25, fuse_out), q_emb


def build_arm(rag, question, fused, q_emb, cap, top_k):
    """一组的 context: 配额 → 截 top_k → S1 注入。返回 (final, capped, dropped_sections)。

    `dropped_sections` = 被**配额本身**丢掉的条目的 section 集合 (不含"排在 top_k
    之外"这种普通落选) —— 用来判断 S1 有没有把被挤走的簇又带回来。
    """
    kept = apply_section_cap(fused, cap)
    kept_ids = {c.chunk_id for c in kept}
    dropped_sections = {c.section for c in fused if c.chunk_id not in kept_ids}
    capped = kept[:top_k]
    final = rag._apply_structured_lookup(question, capped, None, top_k,
                                         query_embedding=q_emb)
    return final, capped, dropped_sections


def _arm_record(final, capped, dropped_sections, top_k):
    """一组的结构性记录 (不含 LLM 结果)。席位数以**实际 context 长度**为准。"""
    capped_ids = {c.chunk_id for c in capped}
    via_lookup = [c for c in final if getattr(c, "via_lookup", False)]
    # 净新增才是"S1 从配额结果里夺走的席位"。已在 capped 里的那条只是被 S1 的副本
    # 顶到了前面 (去重留前者), 没占走额外席位 —— 两个数都记, 免得与 Task 5 报的
    # "注入条数"(总量口径) 对不上时无从分辨。
    injected = [c for c in via_lookup if c.chunk_id not in capped_ids]
    reintroduced = [
        {"source": c.source, "section": c.section}
        for c in injected if c.section in dropped_sections
    ]
    return {
        # 硬 gate 用这个: 模型真正看到几段。< top_k 的题不进主结论。
        "seats": len(final),
        "seats_before_s1": len(capped),
        "full_seats": len(final) >= top_k,
        "s1_injected": len(injected),
        "s1_total_in_final": len(via_lookup),
        "s1_injected_sections": [{"source": c.source, "section": c.section}
                                 for c in injected],
        "s1_all_sections": [{"source": c.source, "section": c.section}
                            for c in via_lookup],
        # S1 不受配额约束, 可能把被配额挤走的同名 section 又带回来 —— 部分抵消配额
        "s1_reintroduced_capped_section": reintroduced,
        "composition": [{"source": c.source, "section": c.section,
                         "via_lookup": bool(getattr(c, "via_lookup", False))}
                        for c in final],
    }


def select_targets(rows, n=11, extra="q38"):
    """层① 里 max_cluster 最大的 n 题 + extra。

    排序键带 id 兜底: max_cluster 并列时纯 `-max_cluster` 的取舍由 JSON 行序决定,
    换一次层① 跑批就可能换人。实测本次 (n=11) 两种排法选出的**集合相同**
    (q77/q108 并列 6, q84/q118 并列 5, 都在线内), 与 eval.pool_depth_probe.DEFAULT_IDS
    逐题一致。

    **实际题数是 11, 不是 brief 正文说的 12。** q38 的 max_cluster=14 是全场最大,
    本来就在前 11 里, 所以 `extra` 那一步从不触发 —— brief 的正文 (n=12、"同分题
    ≥8/12") 与它自己给的这段选题代码对不上。取 11: 这个集合与 Task 5 已落库的
    `pool_depth_probe.DEFAULT_IDS` 逐题相同, 席位可行性 (q38 在配额 2/3/5 下
    4/5/7 席) 就是在它上面测的; 凑到 12 只能从 max_cluster=4 的**四题并列**
    (q105/q28/q31/q57) 里按字典序抓一个, 那是排序副作用, 不是判据。
    同分作废阈值按写死的**绝对条数** ≥8 执行 (n=11 时即 ≥8/11, 比 8/12 更容易触发
    作废 —— 偏向"别改生产"这个保守方向)。
    """
    target = [r["id"] for r in sorted(rows, key=lambda x: (-x["max_cluster"], x["id"]))[:n]]
    if extra and extra not in target:
        target.append(extra)
    return target


def _engine(top_k):
    from server.config import settings
    from server.rag import RAGEngine

    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,   # 生产值, 不许改
    )


# ---- 退化检查 ---------------------------------------------------------------


def run_dry_run(rag, qs, target, top_k, fuse_out):
    """零 LLM 调用: 配额关掉时, 本管线必须与**生产 rag.retrieve** 逐位相同。

    这条断言便宜且能当场抓出接线错误 —— 池被放大、fuse→配额→S1 的顺序接反、
    apply_section_cap 在 cap=None 下不是恒等, 任何一条都会让它红。

    query 向量在比较期间钉死 (retrieve 会自己再 embed 一次; embedding 抖动不是
    本检查要量的东西)。Chroma HNSW 的进程内抖动仍在, 若出现不一致须逐条查明,
    不许当噪声吞掉。
    """
    ok, rows = True, []
    real_embed = rag._embed_query
    try:
        for qid in target:
            question = qs[qid]["question"]
            vec = real_embed(question)
            rag._embed_query = lambda _t, _v=vec: list(_v)
            prod = [c.chunk_id for c in rag.retrieve(question, top_k=top_k)]
            fused, q_emb = _fused_candidates(rag, question, fuse_out)
            row = {"id": qid, "n_fused": len(fused), "arms": {}}
            for arm, cap in ARMS:
                final, capped, dropped = build_arm(rag, question, fused, q_emb, cap, top_k)
                rec = _arm_record(final, capped, dropped, top_k)
                row["arms"][arm] = {k: rec[k] for k in
                                    ("seats", "seats_before_s1", "s1_injected",
                                     "s1_total_in_final", "s1_all_sections",
                                     "s1_reintroduced_capped_section")}
                if arm == "A":
                    ids = [c.chunk_id for c in final]
                    same = ids == prod
                    row["A_equals_production"] = same
                    row["A_positional_diff"] = sum(
                        1 for i in range(max(len(ids), len(prod)))
                        if (ids[i] if i < len(ids) else None)
                        != (prod[i] if i < len(prod) else None))
                    ok = ok and same
            rows.append(row)
            seats = "  ".join(
                f"{a}: {row['arms'][a]['seats_before_s1']}→{row['arms'][a]['seats']}席"
                f"(S1+{row['arms'][a]['s1_injected']})" for a, _ in ARMS)
            print(f"  {qid:>5} fused={row['n_fused']:3d} "
                  f"A{'==' if row['A_equals_production'] else '≠'}prod"
                  f"(逐位差{row['A_positional_diff']})  {seats}", flush=True)
    finally:
        rag._embed_query = real_embed
    return ok, rows


# ---- 归因: 挤占来自 dense 侧还是 BM25 侧 -------------------------------------


def route_breakdown(rag, question, top_k, fuse_out):
    """dense-only / BM25-only / hybrid 三路各自的 top_k 里, 各 section 簇占几席。

    独立证伪 Task 1 提出的假设 (**不是**已知事实):
      > hybrid 的 BM25 侧在 domain / code 这类高频标识符词上被 63 个同构 chunk 摊平,
      > 于是 RRF 融合后同构簇整体上浮, 挤掉 dense 的头名。
    判据: BM25-only 的簇席位显著多于 dense-only ⇒ 假设成立; 反之说明挤占源在 dense
    侧, per-section 配额仍适用但归因描述要改。
    """
    q_emb = rag._embed_query(question)
    pool = max(rag.top_k, rag.hybrid_pool)
    dense = rag._search(question, pool, None, query_embedding=q_emb)
    bm25 = rag._bm25_search(question, pool, None)
    hybrid = rag._hybrid_fuse(dense, bm25, fuse_out)

    def seats(chunks):
        head = list(chunks)[:top_k]
        cnt = Counter(c.section for c in head)
        top_sec, top_n = (cnt.most_common(1)[0] if cnt else (None, 0))
        return {"n": len(head), "max_cluster": top_n, "max_cluster_section": top_sec,
                "distinct_sections": len(cnt),
                "sections": [c.section for c in head]}

    out = {"question": question, "top_k": top_k,
           "routes": {"dense_only": seats(dense), "bm25_only": seats(bm25),
                      "hybrid": seats(hybrid)}}
    # 焦点簇 = hybrid 里最大的那个簇; 看它在各路的席位与最好排名
    focus = out["routes"]["hybrid"]["max_cluster_section"]
    out["focus_section"] = focus
    for name, chunks in (("dense_only", dense), ("bm25_only", bm25), ("hybrid", hybrid)):
        head = list(chunks)[:top_k]
        ranks = [i + 1 for i, c in enumerate(head) if c.section == focus]
        out["routes"][name].update({
            "focus_seats": len(ranks), "focus_best_rank": ranks[0] if ranks else None,
        })
    # RRF 是**加性**的: 同时出现在两张表里的 chunk 拿两份分, 只在一张表里的拿一份。
    # 所以"簇被谁抬起来"要看两个池的**交集**, 不能只看各路席位数。
    dense_ids = {c.chunk_id for c in dense}
    bm25_ids = {c.chunk_id for c in bm25}
    focus_in_hybrid = [c for c in hybrid[:top_k] if c.section == focus]
    out["pool_overlap"] = {
        "n_dense_pool": len(dense), "n_bm25_pool": len(bm25),
        "n_both": len(dense_ids & bm25_ids),
        "focus_seats_in_hybrid": len(focus_in_hybrid),
        "focus_in_both_pools": sum(1 for c in focus_in_hybrid
                                   if c.chunk_id in dense_ids and c.chunk_id in bm25_ids),
    }
    # dense 的头名去哪了 —— Task 1 说 hybrid 把 dense 排第 1 的 chunk 挤出了 top-15
    if dense:
        head1 = dense[0]
        hyb_ids = [c.chunk_id for c in hybrid[:top_k]]
        out["dense_top1"] = {
            "source": head1.source, "section": head1.section,
            "rank_in_hybrid": (hyb_ids.index(head1.chunk_id) + 1
                               if head1.chunk_id in hyb_ids else None),
            # 只在 dense 池里 = RRF 只给它一份分, 而两池都在的簇成员拿两份
            "in_bm25_pool": head1.chunk_id in bm25_ids,
        }
    return out


# ---- 判定 -------------------------------------------------------------------


def verdict(results):
    """按写死的规则算 improved/regressed/tie 与结论。**只用补满席位的题** (硬 gate)。"""
    main = [r for r in results if all(a["full_seats"] for a in r["arms"].values())]
    fallback = [r["id"] for r in results if r not in main]
    out = {"n_main": len(main), "n_fallback": len(fallback), "fallback_ids": fallback,
           "arms": {}, "n_judge_unparsed": sum(
               1 for r in results for a in r["arms"].values() if not a["judge_parse_ok"])}
    ties = 0
    for arm, _cap in ARMS[1:]:
        imp = reg = tie = skipped = 0
        for r in main:
            a, b = r["arms"]["A"]["score"], r["arms"][arm]["score"]
            if a is None or b is None:
                skipped += 1
                continue
            if b > a:
                imp += 1
            elif b < a:
                reg += 1
            else:
                tie += 1
        ties = max(ties, tie)
        net = imp - reg
        out["arms"][arm] = {
            "improved": imp, "regressed": reg, "tie": tie, "skipped": skipped,
            "net": net, "passes": bool(net >= NET_GAIN_THRESHOLD and reg <= MAX_REGRESSED),
        }
    out["max_tie"] = ties
    out["tie_aborts"] = bool(ties >= TIE_ABORT)

    b1, b2 = out["arms"]["B1"], out["arms"]["B2"]
    if out["tie_aborts"]:
        concl, n = "VOID_TIE", None
    elif b1["regressed"] >= 4 or b2["regressed"] >= 4:
        concl, n = "NO_FIX_SIGNAL", None       # 同质簇是有效信号 → 不修, 更正 spec 假设
    elif b1["passes"] and b2["passes"]:
        concl = "FIX"
        n = 1 if b1["net"] > b2["net"] else (2 if b2["net"] > b1["net"] else 2)
    elif b2["passes"]:
        concl, n = "FIX", 2
    elif b1["passes"]:
        concl, n = "FIX_B1_ONLY", 1
    else:
        concl, n = "NO_FIX_HARMLESS", None     # 挤占存在但无害 → 跳过 Task 7
    out["conclusion"], out["N"] = concl, n
    return out


_CONCLUSION_TEXT = {
    "VOID_TIE": "同分题 ≥8 → 层② 判定作废, 换锚重做 (不许顺着读结论)",
    "NO_FIX_SIGNAL": "任一组 regressed ≥4 → 同质簇是有效信号, 不修, 并更正 spec 的假设",
    "FIX": "有害 → Task 7 实施",
    "FIX_B1_ONLY": "仅 B1 过门槛 → N=1, 证据里单列 B2 为何不够",
    "NO_FIX_HARMLESS": "均不过门槛且 regressed 均 ≤1 → 挤占存在但无害, 跳过 Task 7",
}


def print_verdict(v, output=None):
    print("\n===== 层② 判定 =====")
    print(f"主结论题数 {v['n_main']} (走 fallback 口径的题 {v['n_fallback']}: "
          f"{v['fallback_ids'] or '无'})")
    if v["n_judge_unparsed"]:
        print(f"⚠ judge 未解析 {v['n_judge_unparsed']} 次 —— 这些臂的分数不可用, 逐条查明再判")
    for arm in ("B1", "B2"):
        a = v["arms"][arm]
        print(f"  {arm}: improved={a['improved']} regressed={a['regressed']} "
              f"tie={a['tie']} 净改善={a['net']} -> {'过门槛' if a['passes'] else '不过门槛'}"
              + (f"  (跳过 {a['skipped']} 题: 分数缺失)" if a["skipped"] else ""))
    print(f"\n同分题最多 {v['max_tie']}/{v['n_main']}"
          + ("  ⚠ ≥8 -> 层② 判定作废, 换锚重做" if v["tie_aborts"] else ""))
    print(f"结论: {v['conclusion']} — {_CONCLUSION_TEXT[v['conclusion']]}"
          + (f"  N={v['N']}" if v["N"] else ""))
    if output:
        print(f"明细: {output}")


# ---- 跑批 -------------------------------------------------------------------


def _composition_diff(a, b):
    """两组 context 的逐位不同位置数 (长度不等时缺位算不同)。

    集合相同但顺序不同, 对答题模型仍是不同输入, 不算"相同"。
    """
    n = max(len(a), len(b))
    key = lambda x: (x["source"], x["section"])  # noqa: E731
    pa = [key(x) for x in a] + [None] * (n - len(a))
    pb = [key(x) for x in b] + [None] * (n - len(b))
    return sum(1 for x, y in zip(pa, pb, strict=True) if x != y)


def summarize(path):
    """从落盘 JSON **重算**逐题分数表与判定 —— 证据文档里的每个数字都出自这里。

    刻意不读 JSON 里存的 verdict 而是重跑 verdict(): 存的那份若与规则不符, 这里会
    露馅 (下面会把两者对照)。
    """
    with open(path, encoding="utf-8") as f:
        payload = json.load(f)
    results = payload["results"]
    v = verdict(results)
    print(f"# {path}")
    m = payload["_meta"]
    print(f"答题模型 {m['answer_model']} / judge {m['judge_model']} / "
          f"top_k={m['top_k']} fuse_out={m['fuse_out']} hybrid_pool={m['hybrid_pool']}")
    print("\n| 题号 | facts | A | B1 | B2 | 席位 A/B1/B2 | S1 净注入 A/B1/B2 | "
          "context 逐位差 B1/B2 | 答案与 A 相同 B1/B2 | 进主结论 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    def s(arms, arm):
        x = arms[arm]["score"]
        return "—" if x is None else f"{x:.2f}"

    n_ctx_same = {"B1": 0, "B2": 0}
    for r in results:
        a = r["arms"]
        full = all(x["full_seats"] for x in a.values())
        diff = {arm: _composition_diff(a["A"]["composition"], a[arm]["composition"])
                for arm in ("B1", "B2")}
        same_ans = {arm: a[arm]["answer"] == a["A"]["answer"] for arm in ("B1", "B2")}
        for arm in ("B1", "B2"):
            if diff[arm] == 0:
                n_ctx_same[arm] += 1
        print(f"| {r['id']} | {r['n_expected_facts']} | {s(a, 'A')} | {s(a, 'B1')} | "
              f"{s(a, 'B2')} | "
              f"{a['A']['seats']}/{a['B1']['seats']}/{a['B2']['seats']} | "
              f"{a['A']['s1_injected']}/{a['B1']['s1_injected']}/{a['B2']['s1_injected']} | "
              f"{diff['B1']}/{diff['B2']} | "
              f"{'是' if same_ans['B1'] else '否'}/{'是' if same_ans['B2'] else '否'} | "
              f"{'是' if full else '否 (fallback)'} |")
    print()
    # 同分只有在 context 确实变了的题上才有解释力: context 没变的题, 同分是废话。
    for arm in ("B1", "B2"):
        print(f"{arm}: context 与 A **完全相同**的题 {n_ctx_same[arm]}/{len(results)} "
              f"—— 这些题的同分不构成'配额无害'的证据, 只说明配额在该题没生效")
    print_verdict(v)
    stored = payload.get("verdict")
    if stored and (stored.get("conclusion"), stored.get("N")) != (v["conclusion"], v["N"]):
        print(f"\n⚠ 落盘 verdict ({stored.get('conclusion')}) 与重算 ({v['conclusion']}) 不一致")
    else:
        print("\n落盘 verdict 与重算一致。")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="层② context A/B1/B2 对照")
    p.add_argument("--layer1", default="evidence/checkpoints/crowding_layer1.json")
    p.add_argument("--test-set", default="eval/test_set_v3.yml")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--fuse-out", type=int, default=60,
                   help="融合输出放长到多少再施配额 (Task 5: 放长安全, 加深池不安全)")
    p.add_argument("--model", default=None, help="答题模型; 默认 settings.default_model")
    p.add_argument("--output", default="evidence/checkpoints/crowding_layer2.json")
    p.add_argument("--dry-run", action="store_true",
                   help="只跑退化检查与席位统计, 零 LLM 调用")
    p.add_argument("--dry-run-output", default=None)
    p.add_argument("--attribution", default=None, metavar="QIDS",
                   help="逗号分隔题号: 只报 dense/BM25/hybrid 三路的簇席位归因, 零 LLM 调用")
    p.add_argument("--attribution-output", default=None)
    p.add_argument("--summarize", default=None, metavar="JSON",
                   help="从已落盘的结果 JSON 重算逐题分数表与判定, 零 LLM 调用")
    args = p.parse_args(argv)

    if args.summarize:
        return summarize(args.summarize)

    from eval.run_eval import (
        DEFAULT_JUDGE_MODEL,
        check_fact_recall_judge,
        load_test_set,
    )
    from server.config import settings

    with open(args.layer1, encoding="utf-8") as f:
        rows = json.load(f)
    target = select_targets(rows)
    qs = {q["id"]: q for q in load_test_set(args.test_set)}
    model = args.model or settings.default_model

    rag = _engine(args.top_k)

    if args.attribution:
        wanted = [s.strip() for s in args.attribution.split(",")]
        missing = [i for i in wanted if i not in qs]
        if missing:
            raise SystemExit(f"题号不在 {args.test_set}: {missing}")
        rep = {}
        for qid in wanted:
            r = route_breakdown(rag, qs[qid]["question"], args.top_k, args.fuse_out)
            rep[qid] = r
            print(f"\n{qid}  焦点簇 §{r['focus_section']}")
            for name in ("dense_only", "bm25_only", "hybrid"):
                x = r["routes"][name]
                print(f"  {name:<10} top-{args.top_k}: 焦点簇 {x['focus_seats']:2d} 席 "
                      f"(最好排名 {x['focus_best_rank']}), 最大簇 {x['max_cluster']:2d} "
                      f"席 §{x['max_cluster_section']}, 不同 section {x['distinct_sections']}")
            po = r["pool_overlap"]
            print(f"  池交集: dense {po['n_dense_pool']} / bm25 {po['n_bm25_pool']} "
                  f"/ 两池都在 {po['n_both']}; hybrid 里的焦点簇 "
                  f"{po['focus_in_both_pools']}/{po['focus_seats_in_hybrid']} 席两池都在")
            d1 = r.get("dense_top1")
            if d1:
                print(f"  dense 第 1 名 {d1['source']} §{d1['section']} "
                      f"-> hybrid top-{args.top_k} 里排名 {d1['rank_in_hybrid'] or '落榜'}"
                      f"; 它在 bm25 池里: {d1['in_bm25_pool']}")
        if args.attribution_output:
            with open(args.attribution_output, "w", encoding="utf-8") as f:
                json.dump({"generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                           "top_k": args.top_k, "fuse_out": args.fuse_out,
                           "hybrid_pool": rag.hybrid_pool, "questions": rep},
                          f, ensure_ascii=False, indent=1)
            print(f"\n明细: {args.attribution_output}")
        return 0

    if args.dry_run:
        print(f"退化检查 (cap=None 必须与生产 retrieve 逐位相同), {len(target)} 题:")
        ok, dry = run_dry_run(rag, qs, target, args.top_k, args.fuse_out)
        print(f"\n退化检查: {'PASS' if ok else 'FAIL'} "
              f"({sum(1 for r in dry if r['A_equals_production'])}/{len(dry)} 题 A==生产)")
        if args.dry_run_output:
            with open(args.dry_run_output, "w", encoding="utf-8") as f:
                json.dump({"generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                           "top_k": args.top_k, "fuse_out": args.fuse_out,
                           "hybrid_pool": rag.hybrid_pool, "ids": target,
                           "degradation_check_pass": ok, "rows": dry},
                          f, ensure_ascii=False, indent=1)
            print(f"明细: {args.dry_run_output}")
        return 0 if ok else 1

    import litellm

    results = []
    t0 = time.time()
    for i, qid in enumerate(target, 1):
        q = qs[qid]
        # 一次检索, 三组共用 —— 保证同池同序, 唯一变量是配额。
        # 走放长的融合输出 (不是加深池), 再各自施配额并补满 top_k 席。
        fused, q_emb = _fused_candidates(rag, q["question"], args.fuse_out)
        arms = {}
        for arm, cap in ARMS:
            final, capped, dropped = build_arm(rag, q["question"], fused, q_emb,
                                               cap, args.top_k)
            rec = _arm_record(final, capped, dropped, args.top_k)
            ctx = rag.format_context(final)
            msgs = rag.build_messages(q["question"], ctx)
            resp = litellm.completion(model=model, messages=msgs, temperature=0.0)
            answer = resp.choices[0].message.content or ""
            judged = check_fact_recall_judge(
                q["question"], answer, q.get("expected_facts", []), DEFAULT_JUDGE_MODEL
            )
            rec.update({
                "cap": cap,
                "score": judged[0] if judged else None,
                "hits": judged[1] if judged else None,
                "misses": judged[2] if judged else None,
                "judge_parse_ok": judged is not None,
                "answer": answer,
            })
            arms[arm] = rec
            print(f"[{i}/{len(target)}] {qid} {arm}: seats={rec['seats']} "
                  f"(配额后{rec['seats_before_s1']}+S1 {rec['s1_injected']}) "
                  f"score={rec['score']}", flush=True)
        results.append({"id": qid, "question": q["question"],
                        "n_expected_facts": len(q.get("expected_facts", [])),
                        "n_fused": len(fused), "arms": arms})

    v = verdict(results)
    payload = {
        "_meta": {
            "what": "层② context A/B1/B2 对照 —— 锚是答案正确性 (LLM judge), 不是 gold recall",
            "pipeline": "fuse(fuse_out) → apply_section_cap → 截 top_k → S1 注入",
            "arms": {a: c for a, c in ARMS},
            "answer_model": model, "judge_model": DEFAULT_JUDGE_MODEL,
            "top_k": args.top_k, "fuse_out": args.fuse_out,
            "hybrid_pool": rag.hybrid_pool,
            "pool_deep_ok": False, "fuse_out_deep_ok": True,
            "sampling": "按层① max_cluster 选出的**极端样本, 不是随机样本** —— "
                        "结论只能推广到'重挤占题', 不能推广到全 140 题",
            "known_limit_s1": "S1 前插且不受配额约束, 可能把被配额挤走的同名 section "
                              "带回来, 部分抵消配额 (见各臂 s1_reintroduced_capped_section)",
            "hard_gate": "席位数 < top_k 的题一律走 fallback 口径, 不进主结论",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "elapsed_sec": round(time.time() - t0, 1),
            "test_set": args.test_set, "layer1": args.layer1, "ids": target,
        },
        "verdict": v,
        "results": results,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)

    print_verdict(v, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
