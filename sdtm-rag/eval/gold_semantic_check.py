"""gold 语义完整性自查 —— 四道入池闸都**不**做的那一件事 (确定性, 零 LLM)。

## 存在的理由 (2026-08-11 审题实测逼出, 批 1 因缺它漏了 4 题)

四道闸检查的是「gold 唯一定位」「锚串落在 gold 里且不溢出」「fact 够长」「卡片不含全部
probe 词」。**没有一道**检查: **答案本身是不是也完整落在别的 chunk 里。**

闸 B 只看**锚串**。锚串唯一 ⇒ 闸 B 绿, 但锚串只是答案的一句; 另一个 chunk 完全可能
用近乎逐字的措辞承载**全部** `expected_facts`。此时 gold 漏写了那个 chunk, 检索返回它
会答对却被判 miss —— 分数低不是因为检索差, 是因为尺子错。

批 1 实测 (12 题) 命中 4 处, 其中最严重的一处: 某题 gold 只写了 A, 而非 gold 的 B
开头一段近逐字含**全部三条 fact**; 四闸全绿, 因为锚串恰好只在 A。**这正是
`DOCS_V1_NOTES.md` §8.1「限制 1」预言的形态在真实数据上的实例。**

## 为什么是"人工复核触发器"而不是闸

分数高**不等于**错: 同一份 protocol 里相邻节交叉引用、复述同一规则是常态, 合法的
「跨节聚合题」本来就该有多个 chunk 得高分。能自动判的只有"有没有值得看一眼的候选",
判定要人来做。故本模块**只排序 + 标记, 不设退出码闸** —— 与
`docs_gold_gates.probe_binding` / `lint_gold.or_groups` 同一取向 (无原则的阈值会把
排序搞反)。`THRESHOLD` 是**复核触发线**, 不是合格线。

## 输出口径

只回 qid / chunk 文件名 / 分数。**不回正文, 不回 fact 原文** —— 输出会被贴进
`evidence/checkpoints/` (进 git, 红线零正文零真名), 且 chunk 正文实测含研究者姓名与
联系方式, 整段引用是红线事故。
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from eval.docs_gold_gates import chunk_bodies
from eval.lint_gold import load_questions, match_names

# 复核触发线 (非合格线)。审题方 2026-08-11 给的口径。
THRESHOLD = 0.7

# 拉丁词与数字按词切; 日文**按字符 n-gram 切**。
_LATIN_NUM = re.compile(r"[A-Za-z][A-Za-z0-9.\-]{2,}|[0-9]+(?:[.,][0-9]+)?")
_JA_RUN = re.compile(r"[ぁ-んァ-ヶ一-龯ー々]+")
_WS = re.compile(r"\s+")

# 日文 n-gram 长度。**这个选择是本模块唯一容易搞错的地方, 记清楚为什么**:
#
# 初版把日文按"连续假名汉字段"整段当一个 token, 结果**实测失效**: 它会产出
# `日以内にプロトコール治療を開始する` 这种十几字的黏连长串, 只有措辞逐字一致才命中。
# 于是一个**确实**含有同一答案的 chunk 被判 0.43, 全批 0 处触发 —— 而人工审题在同一
# 对象上判出 4 处。**长 token 会把"换个说法表达同一事实"直接判成不相关, 恰好把本模块
# 唯一要抓的东西滤掉了。**
#
# 改用字符 n-gram: 日语无空格分词, 没有形态素解析器时 n-gram 是检索领域的标准做法,
# 且天然对语序/助词/送り仮名差异稳健。n=3 是常用默认: n=2 会被助词("の""に""を")
# 刷成普遍高分, n>=4 又开始退回长串的老毛病。
_NGRAM = 3


@dataclass(frozen=True)
class Overlap:
    qid: str
    chunk: str
    score: float
    is_gold: bool


@dataclass(frozen=True)
class SelfSufficient:
    qid: str
    chunk: str
    per_fact: tuple[float, ...]


def _norm(s: str) -> str:
    return _WS.sub("", s)


def fact_tokens(facts: list[str], n: int = _NGRAM) -> list[str]:
    """去重后的内容单元: 拉丁词/数字整词 + 日文字符 n-gram。

    去重是必要的: 同一个单元在多条 fact 里重复出现会给它加权, 而我们要问的是
    "这个 chunk 覆盖了多少**种**答案要素", 不是"命中了多少次"。
    """
    seen: dict[str, None] = {}
    for f in facts:
        # 拉丁/数字在**规范化之前**切 —— 先抹空白会把 `CTCAE v5.0` 黏成 `CTCAEv5.0`,
        # 把 `Organ preservation-adapted DFS` 黏成一个长串, 即日文那个长 token 病的
        # 拉丁版。切完再去规范化后的正文里做子串匹配, 空白差异照样不影响命中。
        for t in _LATIN_NUM.findall(f):
            seen.setdefault(t, None)
        flat = _norm(f)
        for run in _JA_RUN.findall(flat):
            if len(run) <= n:
                seen.setdefault(run, None)
            else:
                for i in range(len(run) - n + 1):
                    seen.setdefault(run[i:i + n], None)
    return list(seen)


def coverage(questions: list[dict], bodies: dict[str, str]) -> list[Overlap]:
    """每题 × 每个 chunk 的 token 覆盖率, 按分数降序。gold 与非 gold 都回, 由调用方筛。"""
    normed = {name: _norm(body) for name, body in bodies.items()}
    out: list[Overlap] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        toks = fact_tokens(q.get("expected_facts") or [])
        if not toks:
            continue
        gold = list(q.get("expected_sources") or []) + list(q.get("expected_sources_any") or [])
        gold_names = {n for g in gold for n in match_names(g, qid, list(bodies))}
        for name, body in normed.items():
            hit = sum(1 for t in toks if t in body)
            out.append(Overlap(qid, name, hit / len(toks), name in gold_names))
    return sorted(out, key=lambda o: (o.qid, -o.score))


def flagged(questions: list[dict], bodies: dict[str, str],
            threshold: float = THRESHOLD) -> list[Overlap]:
    """需人工看一眼的: **非 gold** 且覆盖率 >= 触发线。"""
    return [o for o in coverage(questions, bodies)
            if not o.is_gold and o.score >= threshold]


def _per_fact_coverage(facts: list[str], normed_body: str) -> tuple[float, ...]:
    """**逐条** fact 的覆盖率 (与 `coverage` 共用 `fact_tokens`, 只是不把 fact 合并)。

    无可计数单元的 fact (纯符号/超短串) 跳过而不是记 0: 记 0 会让整题恒不触发,
    即在"闸 C 没拦住的坏 fact"上恰好失明。跳过则该题按剩下的 fact 判 —— 方向是
    多报, 而这是触发器不是闸, 多报的代价只是多看一眼。
    """
    out: list[float] = []
    for f in facts:
        toks = fact_tokens([f])
        if not toks:
            continue
        out.append(sum(1 for t in toks if t in normed_body) / len(toks))
    return tuple(out)


def self_sufficient_golds(questions: list[dict], bodies: dict[str, str],
                          threshold: float = THRESHOLD) -> list[SelfSufficient]:
    """多 gold 题里**单独一个 gold 就答得全每一条 fact** 的那些 gold。

    ## 存在的理由: `flagged()` 结构上看不见这件事

    `flagged()` 的条件是 `not o.is_gold and ...` —— **gold 按设计豁免**。于是"两个
    gold 里其实有一个自足, 另一个是冗余"这一形态, 它**不可能**报出来。而多 gold 题
    正是跨节探针的题型 ⇒ 那道判据对最需要它的题型覆盖率恒为 0。`q40` 的 L6 探针
    (part02 单侧自足、part01 冗余) 是人工发现的; 现在知道了原因: 工具报不了。

    ## 为什么逐 fact 而不是合并覆盖率

    合并口径把所有 fact 的单元并成一袋, **一条 fact 满分能替另一条完全没答上的
    补票**。实测 (30 题题集, 10 道多 gold 题, 命令见下): 合并 >= 0.7 的单 gold 有
    5 个 (q18/q22/q24/q41/q57), 其中 4 个各有一条明显没答上的 fact
    (逐 fact 最低分 0.15 / 0.54 / 0.50 / 0.62) —— 那 4 个恰恰是**真跨节**, 合并口径
    会把它们全报成"疑似冗余"。逐 fact 口径只剩 1 个 (q24), 噪声降到 1/5。

        .venv/bin/python -m eval.gold_semantic_check \\
          data/study/st01/eval/test_set_docs_v1.yml \\
          --docs-dir data/study/st01/docs --mode selfsuff

    ## 为什么只看 AND 侧

    `expected_sources_any` 按定义就是"任一成员命中即得分" —— OR 组成员本来就该各自
    自足。把它当多 gold 会把**设计意图**报成缺陷, 且每道 OR 题必报, 排序立刻被淹。

    ## 仍然是触发器不是闸

    与 `flagged` / `probe_binding` / `or_groups` 同取向: 报出来**不等于**坏题。
    实测 q24 被独立审题人工判为真跨节 (读 `s16_2` 全文确认无判别内容), 触发只是
    "值得看一眼"。故不改退出码语义。
    """
    normed = {name: _norm(body) for name, body in bodies.items()}
    out: list[SelfSufficient] = []
    for q in questions:
        qid = q.get("id", "<no id>")
        golds = list(q.get("expected_sources") or [])
        if len(golds) < 2:
            continue
        facts = q.get("expected_facts") or []
        # 走 match_names: "哪些 chunk 算这题的 gold" 只许有一个实现 (见 lint_gold)。
        names = {n for g in golds for n in match_names(g, qid, list(bodies))}
        for name in sorted(names):
            per = _per_fact_coverage(facts, normed[name])
            if per and all(s >= threshold for s in per):
                out.append(SelfSufficient(qid, name, per))
    return sorted(out, key=lambda r: (r.qid, r.chunk))


def _print_self_sufficiency(questions: list[dict], bodies: dict[str, str],
                            threshold: float) -> int:
    """selfsuff 模式的打印。无条件先打**每道多 gold 题每个 gold 的逐 fact 分数**。

    照抄 `probe_binding` 的做法: 只报触发项, 后人无从判断这项判据对该题集**有没有
    约束力** —— 一份 0 触发的输出既可能是"题都很干净", 也可能是"它根本没看这些题",
    两者长得一模一样。可见性行让这两种情形可分。
    """
    rows = self_sufficient_golds(questions, bodies, threshold)
    hit = {(r.qid, r.chunk) for r in rows}
    normed = {n: _norm(b) for n, b in bodies.items()}
    n_multi = 0
    for q in questions:
        golds = list(q.get("expected_sources") or [])
        if len(golds) < 2:
            continue
        n_multi += 1
        qid = q.get("id", "<no id>")
        facts = q.get("expected_facts") or []
        names = sorted({n for g in golds for n in match_names(g, qid, list(bodies))})
        shown = " · ".join(
            f"{n}{'!' if (qid, n) in hit else ''}="
            f"[{', '.join(f'{s:.2f}' for s in _per_fact_coverage(facts, normed[n]))}]"
            for n in names)
        print(f"[selfcov] {qid}: {shown}   (! = 单 gold 自足)")
    for r in rows:
        print(f"[SELF] {r.qid}: gold {r.chunk} 逐 fact "
              f"[{', '.join(f'{s:.2f}' for s in r.per_fact)}] 全 >= {threshold} "
              f"— 人工复核另一个 gold 是否冗余")
    print(f"\n{len(rows)} 处单 gold 疑似自足 / {n_multi} 道多 gold 题 (触发线 {threshold}) "
          f"— 本项是**排序触发器不是闸**: 自足不等于坏题, 判定由人做")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="gold 语义完整性自查 (排序+触发器, 非闸; 确定性零 LLM)")
    ap.add_argument("test_set")
    ap.add_argument("--docs-dir", required=True)
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    ap.add_argument("--top", type=int, default=3, help="每题额外打印的最高分 chunk 数")
    ap.add_argument("--mode", choices=("overlap", "selfsuff"), default="overlap",
                    help="overlap=非 gold 覆盖率 (默认, 原行为); "
                         "selfsuff=多 gold 题的单 gold 自足性")
    args = ap.parse_args(argv)

    questions = load_questions(args.test_set)
    bodies = chunk_bodies(args.docs_dir)
    if args.mode == "selfsuff":
        return _print_self_sufficiency(questions, bodies, args.threshold)
    allcov = coverage(questions, bodies)

    by_q: dict[str, list[Overlap]] = {}
    for o in allcov:
        by_q.setdefault(o.qid, []).append(o)
    for qid, rows in by_q.items():
        head = rows[:args.top]
        shown = " · ".join(
            f"{r.chunk}{'*' if r.is_gold else ''}={r.score:.2f}" for r in head)
        print(f"[cover] {qid}: {shown}   (* = gold)")

    hits = [o for o in allcov if not o.is_gold and o.score >= args.threshold]
    for o in hits:
        print(f"[FLAG] {o.qid}: 非 gold {o.chunk} 覆盖率 {o.score:.2f} "
              f">= {args.threshold} — 人工复核 gold 是否漏写")
    print(f"\n{len(hits)} 处触发人工复核 (触发线 {args.threshold}) "
          f"— 本项是**排序触发器不是闸**: 高分不等于错, 判定由人做")
    return 0


if __name__ == "__main__":
    sys.exit(main())
