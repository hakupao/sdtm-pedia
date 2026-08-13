"""Plan B Phase 1 闸 1: 路由准确率三遍评测.

红线: 逐题明细 (含题目文本) 只写 data/study/st01/eval/runs/ (gitignored);
stdout 只打统计, 不打题目文本。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

from eval.run_eval import load_test_set
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router

CDISC_SET = Path("eval/test_set_v3.yml")
STUDY_SET = Path("data/study/st01/eval/test_set_study_v1_1.yml")
# 日语措辞的 CDISC 标准题: 原 gold 里语言与语料一一对应 (cdisc 全英/study 全日),
# 任何"按语言判库"的路由规则在那份 gold 上都无法被证伪 —— 本文件专门补上这个盲区。
JA_SUPP_SET = Path("eval/routing_gold_ja_supplement.yml")
RUNS_DIR = Path("data/study/st01/eval/runs")
EXACT_THRESHOLD = 0.95
VALID_GOLD = ("cdisc", "study", "both")

DOCS_QUESTION_SET = Path("data/study/st01/eval/test_set_docs_v1.yml")
DOCS_ROUTING_SET = Path("data/study/st01/eval/routing_gold_docs.yml")

# spec §7 条款 5: 这三题只报告不作 PASS 条件, 单独分组。硬编码 id (非题面) 入库是有意的 ——
# 它们必须可被 code review 看见, 否则「哪三题被豁免」就成了口头约定。
FINAL_IDS = ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")
# spec §7 条款 1: U2 收口实测三遍稳定 179/181, 留 1 题噪声余量。**不许下调。**
LEGACY_EXACT_FLOOR = 178
# 数据文件**有权自称**的 group。`final` / `u1_doc` 不在其中: 它们只能由 load_u1_doc_gold
# 按 FINAL_IDS 产生。若把 `final` 放进这个白名单, routing_gold_docs.yml 里任何一题都可以
# 写 group: final 从而脱离 fatal_excl_final —— 而该 yml 是 gitignored, 不进 code review,
# 等于把「哪几题被条款 5 豁免」这个必须可被 review 看见的名单交给一个看不见的文件改写。
AUTHORED_GROUPS = ("dev", "heldout", "distractor_cdisc", "ambiguous_both")
NEW_GROUPS = ("u1_doc", "final", *AUTHORED_GROUPS)
GROUPS = ("legacy", *NEW_GROUPS)
# spec §5.2 的配比。写死而非「非空即可」: 两个 gold 文件都 gitignored, 少掉整整一组题
# (U1 题集删到只剩 FINAL_IDS 三题 / 新 gold 缩到 1 题) 在输出里长得跟「这组本来就不存在」
# 一模一样, 闸照样 PASS —— spec §7「不许从 gold 删题」就没有任何执行者。
# 数字改动必须走 code review, 这正是把它放进源码的理由。
EXPECTED_GROUP_SIZES = {"legacy": 181, "u1_doc": 27, "final": 3, "dev": 12,
                        "heldout": 12, "distractor_cdisc": 12, "ambiguous_both": 6}


def load_supplement(path: Path) -> list[dict]:
    """读路由专用补充 gold (自带 gold 标签, 不走 load_test_set 的检索 gold 校验).

    缺文件直接 raise: 该文件是闸的一部分, 悄悄少几题 = 闸口变松却无人察觉。
    """
    if not path.exists():
        raise FileNotFoundError(f"路由补充 gold 缺失: {path} —— 闸口不完整, 拒绝继续")
    items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not items:  # 空文件 / 全被注释掉: 静默返回 [] = 闸悄悄变松
        raise ValueError(f"路由补充 gold 为空: {path} —— 闸口不完整, 拒绝继续")
    out = []
    for q in items:
        if not q.get("id") or not q.get("question"):
            raise ValueError(f"{path}: 条目缺 id/question: {q!r}")
        if q.get("gold") not in VALID_GOLD:
            raise ValueError(f"{path}: {q['id']} 的 gold={q.get('gold')!r} 非法")
        out.append({"id": q["id"], "question": q["question"], "gold": q["gold"]})
    return out


def load_u1_doc_gold(path: Path) -> list[dict]:
    """U1 的 30 道 doc 题, gold 一律 study (spec §5.2)。

    统一标签而非逐题裁定 —— 逐题裁定意味着标签可以被路由结果反向塑造。
    手順書内容 CDISC 结构上答不了, 这个统一是有实据的 (U1 各题 note 均记录反向查卡 0 命中)。
    """
    if not path.exists():
        raise FileNotFoundError(f"U1 doc 题集缺失: {path} —— 闸口不完整, 拒绝继续")
    # 空题集 → 静默少 30 题 = 本单元要修的那个错重新对闸隐形。这一步必须在
    # load_test_set 之前: 它对空文件抛的是 TypeError('NoneType' object is not iterable),
    # 消息来自无关模块, 且会把下面那条 if not items 变成永远够不着的死代码。
    if not (yaml.safe_load(path.read_text(encoding="utf-8")) or []):
        raise ValueError(f"U1 doc 题集为空: {path} —— 闸口不完整, 拒绝继续")
    items = load_test_set(str(path))
    if not items:
        raise ValueError(f"U1 doc 题集为空: {path} —— 闸口不完整, 拒绝继续")
    ids = {q["id"] for q in items}
    missing = sorted(set(FINAL_IDS) - ids)
    if missing:  # 三题被改名/删掉而闸照跑 = 条款 5 的报告对象静默消失
        raise ValueError(f"{path}: FINAL_IDS 缺失 {missing} —— 条款 5 无报告对象, 拒绝继续")
    return [{"id": q["id"], "question": q["question"], "gold": "study",
             "group": "final" if q["id"] in FINAL_IDS else "u1_doc"}
            for q in items]


def load_docs_routing_gold(path: Path) -> list[dict]:
    """U3 新写的 42 道路由题 (自带 gold + group)。缺文件/空文件 raise —— 同 load_supplement。"""
    if not path.exists():
        raise FileNotFoundError(f"U3 手順書路由 gold 缺失: {path} —— 闸口不完整, 拒绝继续")
    items = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not items:  # 空文件 / 全被注释掉: 静默返回 [] = 闸悄悄变松
        raise ValueError(f"U3 手順書路由 gold 为空: {path} —— 闸口不完整, 拒绝继续")
    out = []
    for q in items:
        if not q.get("id") or not q.get("question"):
            raise ValueError(f"{path}: 条目缺 id/question: {q!r}")
        if q.get("gold") not in VALID_GOLD:
            raise ValueError(f"{path}: {q['id']} 的 gold={q.get('gold')!r} 非法")
        # legacy 被排除在外: 新题自称 legacy 会污染回归条款 1 的参照物。
        # final / u1_doc 同样被排除: 见 AUTHORED_GROUPS 的注释 —— 自称 final 即脱离 fatal。
        if q.get("group") not in AUTHORED_GROUPS:
            raise ValueError(
                f"{path}: {q['id']} 的 group={q.get('group')!r} 非法, 应属 {AUTHORED_GROUPS}")
        out.append({"id": q["id"], "question": q["question"],
                    "gold": q["gold"], "group": q["group"]})
    return out


def load_gold() -> list[dict]:
    items = [{"id": q["id"], "question": q["question"], "gold": "cdisc", "group": "legacy"}
             for q in load_test_set(str(CDISC_SET))]
    items += [{"id": f"st_{q['id']}", "question": q["question"], "gold": "study",
               "group": "legacy"}
              for q in load_test_set(str(STUDY_SET)) if not q.get("out_of_scope")]
    items += [{**q, "group": "legacy"} for q in load_supplement(JA_SUPP_SET)]
    items += load_u1_doc_gold(DOCS_QUESTION_SET)
    items += load_docs_routing_gold(DOCS_ROUTING_SET)
    ids = [g["id"] for g in items]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:  # predictions 以 id 为键, 重名会互相覆盖 → 静默改变计分
        raise ValueError(f"gold id 重复: {dupes}")
    # 条款 5 的豁免名单必须**恒等于**源码里的 FINAL_IDS。AUTHORED_GROUPS 已经拦住了
    # 数据文件自称 final 这条路, 这里是第二道: 任何来源 (含将来新增的第 6 个 gold 来源)
    # 只要往 final 组多塞或少塞一题, 就等于在一个不进 code review 的地方改豁免名单。
    final_ids = {g["id"] for g in items if g["group"] == "final"}
    if final_ids != set(FINAL_IDS):
        raise ValueError(
            f"final 组 ≠ FINAL_IDS —— 条款 5 的豁免名单被改写 "
            f"(多出 {sorted(final_ids - set(FINAL_IDS))}, 缺少 {sorted(set(FINAL_IDS) - final_ids)}), "
            f"拒绝继续")
    sizes = {name: sum(1 for g in items if g["group"] == name) for name in GROUPS}
    if sizes != EXPECTED_GROUP_SIZES:  # 整组消失长得跟「这组本来就不存在」一样, 必须点名
        diff = {k: (v, EXPECTED_GROUP_SIZES.get(k)) for k, v in sizes.items()
                if v != EXPECTED_GROUP_SIZES.get(k)}
        raise ValueError(
            f"gold 组题量与 spec §5.2 不符 (实际, 期望): {diff} —— 闸口题量被改动, 拒绝继续")
    return items


def score_run(gold: list[dict], predictions: dict[str, str]) -> dict:
    exact = 0
    fatal_items = []
    for g in gold:
        pred = predictions.get(g["id"])
        if pred == g["gold"]:
            exact += 1
        elif pred != "both":  # 错的单库 or 缺失: 该题 recall 归零, 致命
            fatal_items.append({"id": g["id"], "gold": g["gold"], "pred": pred})
    acc = exact / len(gold)
    return {"n": len(gold), "exact": exact, "exact_acc": round(acc, 4),
            "fatal": len(fatal_items), "fatal_items": fatal_items,
            "passed": acc >= EXACT_THRESHOLD and not fatal_items}


def score_by_group(gold: list[dict], predictions: dict[str, str]) -> dict[str, dict]:
    """按 group 切片各自 score_run。未知 group 直接 raise —— 分组口径写死在 spec §7。"""
    # repr 而非裸值: gold 同时缺 group (None) 与带未知字符串组时, sorted() 会先炸
    # TypeError('<' not supported between str and NoneType), 把这条写好的消息挤掉。
    unknown = sorted(map(repr, {g.get("group") for g in gold} - set(GROUPS)))
    if unknown:
        raise ValueError(f"未知 group: {unknown} —— 口径写死在 spec §7, 不许实施时新增")
    out = {}
    for name in GROUPS:
        subset = [g for g in gold if g.get("group") == name]
        if subset:
            out[name] = score_run(subset, predictions)
    return out


def gate_verdict(gold: list[dict], predictions: dict[str, str]) -> dict:
    """spec §7 条款 1 的判定。

    fatal 口径 = **全集减去 final 组** —— final 三题的 gold 是 study, 判去 cdisc 按
    score_run 就是 fatal; 若计入, 条款 1 会与条款 5 (只报告不作判据) 互相打架。
    """
    by_group = score_by_group(gold, predictions)
    if "legacy" not in by_group:  # 没有参照物时拒绝给结论, 而不是默认放行
        raise ValueError("legacy 子集缺失 —— 回归条款 1 无参照物, 拒绝给结论")
    non_final = [g for g in gold if g.get("group") != "final"]
    overall = score_run(non_final, predictions)
    legacy_exact = by_group["legacy"]["exact"]
    return {
        "n_scored_excl_final": overall["n"],
        "fatal_excl_final": overall["fatal"],
        "fatal_ids_excl_final": sorted(f["id"] for f in overall["fatal_items"]),
        "legacy_exact": legacy_exact,
        "legacy_floor": LEGACY_EXACT_FLOOR,
        "by_group": {k: {kk: vv for kk, vv in v.items() if kk != "fatal_items"}
                     for k, v in by_group.items()},
        "passed": overall["fatal"] == 0 and legacy_exact >= LEGACY_EXACT_FLOOR,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=3)
    args = parser.parse_args(argv)
    gold = load_gold()
    llm = create_router(settings)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    all_passed = True
    per_run_preds: list[dict[str, str]] = []
    for run_i in range(1, args.runs + 1):
        preds: dict[str, str] = {}
        n_fallback = 0
        for g in gold:
            corpus, fallback = route_corpus(llm, g["question"])
            preds[g["id"]] = corpus
            n_fallback += fallback
        v = gate_verdict(gold, preds)
        per_run_preds.append(preds)
        detail = [{**g, "pred": preds[g["id"]]} for g in gold]
        (RUNS_DIR / f"routing_run_{run_i}.json").write_text(
            json.dumps({"summary": v, "detail": detail}, ensure_ascii=False, indent=1))
        groups = "  ".join(
            f"{k}:{s['exact']}/{s['n']}" for k, s in v["by_group"].items())
        # PASS 后缀写死「(条款1)」: v["passed"] 只等于 spec §7 条款 1, 不含条款 2 (held-out
        # 与 dev 差 ≤25pt) / 3 (dev ≥10/12) / 4 (干扰题下降 ≤1)。裸 PASS + rc=0 极易被
        # 下游读成「本单元通过」, 那三条条款就凭空消失。条款 2/3/4 的原料在 groups: 那行。
        print(f"run {run_i}: legacy {v['legacy_exact']}/{v['by_group']['legacy']['n']} "
              f"(floor {v['legacy_floor']})  fatal_excl_final={v['fatal_excl_final']}  "
              f"fallback={n_fallback}  {'PASS(条款1)' if v['passed'] else 'FAIL(条款1)'}")
        print(f"         groups: {groups}")
        if v["fatal_ids_excl_final"]:
            print(f"         fatal ids: {v['fatal_ids_excl_final']}")
        all_passed &= v["passed"]

    stable = sum(
        1 for g in gold
        if len({p[g["id"]] for p in per_run_preds}) == 1
    )
    print(f"stability: {stable}/{len(gold)} 题三遍判定一致")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
