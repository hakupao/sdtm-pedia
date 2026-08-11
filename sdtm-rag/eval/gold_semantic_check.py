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


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="gold 语义完整性自查 (排序+触发器, 非闸; 确定性零 LLM)")
    ap.add_argument("test_set")
    ap.add_argument("--docs-dir", required=True)
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    ap.add_argument("--top", type=int, default=3, help="每题额外打印的最高分 chunk 数")
    args = ap.parse_args(argv)

    questions = load_questions(args.test_set)
    bodies = chunk_bodies(args.docs_dir)
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
