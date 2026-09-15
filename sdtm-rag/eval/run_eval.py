"""Phase 1D Full Evaluation runner.

Modes:
  --retrieval-only   Score source recall only (no LLM calls, fast+free)
  (default)          Full: retrieval + LLM answer + (substring) fact recall

Flags:
  --model MODEL      Override LLM model string (bypasses Router, uses litellm directly)
                     e.g. anthropic/claude-sonnet-4-6, deepseek/deepseek-chat
  --judge            Add SEMANTIC fact recall via an LLM judge (fixes the substring
                     metric's ~11pt under-count); drives the verdict, substring kept
                     as a secondary metric. --judge-model sets the judge (default deepseek).
  --threshold FLOAT  Override pass/fail threshold (default 0.85)
  --tag TAG          Label added to output JSON for cross-model comparison

  python eval/run_eval.py eval/test_set_v3.yml --model deepseek/deepseek-chat \
      --temperature 0 --structured-lookup --hybrid --judge --output eval/report.json

Run from sdtm-rag/:
  python eval/run_eval.py eval/test_set_v0.yml --retrieval-only
  python eval/run_eval.py eval/test_set_v0.yml
  python eval/run_eval.py eval/test_set_v0.yml --output eval/baseline_report.json
  python eval/run_eval.py eval/test_set_v1.yml --model anthropic/claude-sonnet-4-6 --tag sonnet --output eval/report_sonnet.json
  python eval/run_eval.py eval/test_set_v1.yml --model deepseek/deepseek-chat --tag deepseek --threshold 0.80 --output eval/report_deepseek.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

import litellm
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from server.config import settings  # noqa: E402
from server.federation import FederatedEngine  # noqa: E402
from server.llm_config import create_router  # noqa: E402
from server.domain_expand import build_expander
from server.rag import RAGEngine  # noqa: E402

TOP_K = 15

# V-2: 生成调用的 max_tokens 必须**显式**给, 不能吃 litellm 的 provider 默认值
# (Bedrock Converse=4096, OpenAI 系是模型上限) —— 默认值不同 ⇒ 各模型截断率不同
# ⇒ 截断会少发码 ⇒ 话痨模型在 (a) 层显得更干净。跨模型比较必须同一个上限。
MAX_TOKENS = 8192


def build_completion_kwargs(
    messages: list, temperature: float | None, max_tokens: int
) -> dict:
    """生成调用的 kwargs。max_tokens 恒进, temperature 只在给了时进。"""
    kwargs: dict = {"messages": messages, "max_tokens": max_tokens}
    if temperature is not None:
        kwargs["temperature"] = temperature  # 0.0 => deterministic paired runs
    return kwargs


def find_truncated(results: list[dict], max_tokens: int) -> list[str]:
    """撞满 max_tokens 的题 id —— 这些答案很可能被切在句中。

    ⚠ 截断必须**可见**: 2026-09-02 那轮 q36/q83 撞顶无任何提示, 靠人工比对才发现。
    没有 usage 的条目 (retrieval-only / 生成失败) 跳过, 不算截断也不炸。
    """
    return [
        r["id"] for r in results
        if (r.get("usage") or {}).get("completion_tokens") == max_tokens
    ]


_GOLD_KEYS = ("expected_sources", "expected_sources_any")
_KNOWN_EXPECTED_KEYS = _GOLD_KEYS + ("expected_facts",)


def load_test_set(path: str) -> list[dict]:
    """读题集并做 schema 校验。

    校验的理由: `check_source_recall` 对空 gold 返回 1.0 —— 键名写错 (如
    `expected_source_any`) 或两个 gold 键都空时, 该题白得满分, 且偏差**单向朝上**、
    幅度小, 不会被任何闸拦住。这类静默计分地雷比缺功能危险。
    """
    with open(path, encoding="utf-8") as f:
        test_set = yaml.safe_load(f)
    for q in test_set:
        qid = q.get("id", "<no id>")
        unknown = [k for k in q
                   if k.startswith("expected") and k not in _KNOWN_EXPECTED_KEYS]
        if unknown:
            raise ValueError(f"{qid}: unknown key(s) {unknown} — 拼错的 gold 键会被静默忽略")
        if q.get("out_of_scope"):
            continue
        if not any(q.get(k) for k in _GOLD_KEYS):
            raise ValueError(
                f"{qid}: 无非空 gold ({' / '.join(_GOLD_KEYS)}) —— 该题会白得满分")
    return test_set


def source_matches(
    expected: str,
    retrieved_sources: list[str],
    retrieved_sections: list[str | None] | None = None,
) -> bool:
    """单条 gold 的匹配判定 —— check_source_recall 与判据扫描工具的**唯一**实现。

    硬规矩 1 (2026-08-06 的教训): 判据检查工具与判据必须逐字同语义。上一轮用
    "照着再写一遍"来保证, lint 剥 `.md` 后匹配、严于真实判据, 制造 8 条假阳性,
    并连锁导致出题人删掉合法 gold。故同语义在此是**结构保证**: 谁都不许有第二份实现。

    语法与语义 (完整背景见 check_source_recall 的 docstring):
      - `路径`         -> 对 retrieved_sources 做子串匹配
      - `路径#节`      -> 双条件: 路径子串命中某条目 **且** 节子串命中**同一条目**的 section
      - `路径#节$`     -> 同上, 但 section 要求**精确相等** (对付互为子串的兄弟 section)
      - `路径#` (空节) -> ValueError (空 sec 下子串恒真, 会静默放宽判据)
      - 含 `#` 但未传 retrieved_sections -> ValueError (静默降级为路径匹配属测量缺陷)
      - section 为 None 的条目永不命中 section 级 gold
    """
    if "#" in expected:
        path, sec = expected.split("#", 1)
        exact = sec.endswith("$")
        if exact:
            sec = sec[:-1]
        if not sec.strip():
            raise ValueError(
                f"section-level gold {expected!r} has an empty section — 写全 `路径#节`, "
                "或改回纯路径写法。空 section 会静默退化成路径匹配 (判据比声称的宽)"
            )
        if retrieved_sections is None:
            raise ValueError(
                f"section-level gold {expected!r} requires retrieved_sections "
                "(caller must pass [c.section for c in chunks])"
            )
        if len(retrieved_sections) != len(retrieved_sources):
            raise ValueError("retrieved_sections length mismatch")
        return any(
            path in src and (s == sec if exact else sec in (s or ""))
            for src, s in zip(retrieved_sources, retrieved_sections)
        )
    return any(expected in src for src in retrieved_sources)


def check_source_recall(
    retrieved_sources: list[str],
    expected_sources: list[str],
    any_of: list[str] | None = None,
    retrieved_sections: list[str | None] | None = None,
) -> tuple[float, list[str], list[str]]:
    """expected_sources 是 AND (每条都要命中); any_of 是 OR (任一命中即满足该组).

    单条匹配委托给模块级 `source_matches` —— 判据扫描工具共用同一实现 (硬规矩 1)。

    加 OR 的原因: 常见真相是"这几个来源里任一个都能完整回答该问题"。用 AND 表达会把
    正确检索记成部分失败, 与 study 轨家族题同属"gold 语义表达不了"的一类测量缺陷。

    **使用纪律 (血的教训, 2026-08-04)**: OR 组不增加分母, 但候选越多越容易命中 ——
    机制本身**挡不住**滥用。一次实际尝试放宽某题就翻了车: 声称"该文件含答案"故加入
    OR 组, 但实测召回的 chunk **不含**答案 (该文件有 222 chunk, 本函数按**路径子串**
    匹配, 任一 chunk 命中即算) → 把正确的 true negative 改成了 false positive。故:

      1. any_of 的每个成员必须**独立覆盖全部 expected_facts**;
      2. 判据是"**实际被召回的 chunk** 能否回答", 不是"文件里有没有这段文字";
      3. 超大文件 (chunk 数多) 慎入 OR 组 —— 路径级匹配对它们判别力≈0;
      4. 放宽 gold 应由**非受益方**裁定。

    **section 粒度语法 (Plan B Phase 0)**: 上述第 3 条的直接对策 —— gold 写成
    `路径#节` (如 `chapters/ch04.md#4.1`) 时按**双条件**匹配: `路径`子串命中某条
    retrieved source **且** `节`子串命中**同一条目**的 section。这样 222-chunk 大文件
    也有判别力: "被召回的那个 chunk 是不是该节"而非"该文件里有没有"。

    调用方须传 `retrieved_sections` (与 `retrieved_sources` 等长, 元素可 None,
    即 `[c.section for c in chunks]`)。gold 含 `#` 但未传 → 抛 ValueError 而非静默
    降级为路径匹配 (静默降级会让判据比声称的宽, 属测量缺陷)。section 为 None 的条目
    永不命中 section 级 gold。纯路径写法行为逐字节不变。

    **`路径#` (井号后为空) 抛 ValueError**: 空 `sec` 下 `"" in (s or "")` 恒 True, 该 gold
    不但退化成路径匹配, 还绕过了上一段"section 为 None 永不命中"的承诺 —— 比纯路径写法
    更松。改写 gold 时打空一个 section 会静默把该题退回无判别力口径, 偏差单向朝上、幅度小,
    任何闸都拦不住, 与 `load_test_set` 拦拼错 gold 键属同一类防御。

    **`路径#节$` = 精确匹配整个 section** (子串仍是默认, 不带 `$` 时行为不变)。加它的原因:
    section 判据是子串语义, 而 VARIABLE_INDEX 有 6 组 section 互为子串
    (`§一 通用变量: ARM` ⊂ `…ARMCD`, `…VISIT` ⊂ `…VISITNUM` 等)。q107 要 ARM + ARMCD 两节
    却只召回 ARMCD, 子串语义下 ARM 会被 ARMCD 的 chunk 冒名命中 —— 正是 section 化要消灭的
    那种假命中, 只是换到了 section 层。**子串匹配对"标识符类 gold"是一类通用隐患**: study 侧
    同期也排查了这一形态 (gold 写成更长兄弟卡的前缀), 但那边卡名带 `.md` 后缀因而实际有判别力,
    真正失效的是一条家族前缀 gold。教训: 凡"标识符 + 子串匹配", 都要问"有没有更长的兄弟标识符",
    并按各自 gold 的实际写法逐一验证, 而不是照搬结论。
    全库无 section 含 `$`, 故该标记不与真实 section 冲突。
    """
    hits: list[str] = []
    misses: list[str] = []
    for exp in expected_sources:
        found = source_matches(exp, retrieved_sources, retrieved_sections)
        (hits if found else misses).append(exp)

    n_groups = len(expected_sources)
    n_hit = len(hits)
    if any_of:
        n_groups += 1                       # OR 组整体算一个计分单位
        matched = [e for e in any_of if source_matches(e, retrieved_sources, retrieved_sections)]
        if matched:
            n_hit += 1
            hits.extend(matched)
        else:
            misses.extend(any_of)

    recall = n_hit / n_groups if n_groups else 1.0
    return recall, hits, misses


def check_fact_recall(
    answer: str,
    expected_facts: list[str],
) -> tuple[float, list[str], list[str]]:
    answer_lower = answer.lower()
    hits: list[str] = []
    misses: list[str] = []
    for fact in expected_facts:
        if fact.lower() in answer_lower:
            hits.append(fact)
        else:
            misses.append(fact)
    recall = len(hits) / len(expected_facts) if expected_facts else 1.0
    return recall, hits, misses


# ---- semantic fact recall (LLM judge) ---------------------------------------
#
# The substring check_fact_recall above is structurally blind to paraphrase /
# synonym / spelled-out-vs-numeric / value-shown-in-a-table, so it systematically
# UNDER-counts (measured ~11pt low on v3). --judge replaces it with a semantic
# verdict: per gold fact, does the answer convey it by meaning? Both metrics are
# reported; with --judge the PASS/FAIL verdict uses the judge number.

DEFAULT_JUDGE_MODEL = "deepseek/deepseek-chat"

_JUDGE_SYS = (
    "You are a STRICT but SEMANTIC fact-recall judge for an SDTM knowledge-base QA "
    "system. For each GOLD fact, decide whether the ANSWER conveys that fact by MEANING "
    "— any surface form counts as covered: paraphrase, synonym, spelled-out vs numeric "
    "(\"two-character\" == \"2-character\"), a value shown in a table, equivalent phrasing. "
    "Mark covered=false ONLY if the answer omits the fact, contradicts it, or is merely "
    "topically adjacent without stating it. Do not reward topical-but-absent; do not "
    "punish correct-but-reworded. Output ONLY a JSON object "
    "{\"covered\": [true, false, ...]} with EXACTLY one boolean per gold fact, in order."
)


def _parse_covered(content: str, n_facts: int) -> list[bool] | None:
    """Extract the aligned boolean list from a judge response. Returns a list of
    exactly n_facts bools, or None if the response can't be parsed / length mismatches
    (caller then falls back to the substring metric for that question, never crashes)."""
    if not content:
        return None
    text = content.strip()
    # tolerate ```json fences and surrounding prose: grab the outermost {...} or [...]
    for opener, closer in (("{", "}"), ("[", "]")):
        i, j = text.find(opener), text.rfind(closer)
        if i != -1 and j != -1 and j > i:
            try:
                obj = json.loads(text[i : j + 1])
            except (json.JSONDecodeError, ValueError):
                continue
            raw = obj.get("covered") if isinstance(obj, dict) else obj
            # Accept ONLY a list of bool/int (0/1). Reject lists of dicts/strings:
            # `bool(x)` would coerce a non-empty dict or "no" to True and silently
            # INFLATE recall with judge_parse_ok=True — the exact trust violation this
            # metric exists to prevent. A non-bool list -> None -> counted substring fallback.
            if (
                isinstance(raw, list)
                and len(raw) == n_facts
                and all(isinstance(x, (bool, int)) for x in raw)
            ):
                return [bool(x) for x in raw]
    return None


def check_fact_recall_judge(
    question: str,
    answer: str,
    expected_facts: list[str],
    judge_model: str,
    temperature: float = 0.0,
) -> tuple[float, list[str], list[str]] | None:
    """Semantic fact recall via an LLM judge. Returns (recall, hits, misses) or None
    when the judge response is unparseable (caller falls back to substring)."""
    if not expected_facts:
        return 1.0, [], []
    facts_block = "\n".join(f"{i + 1}. {f}" for i, f in enumerate(expected_facts))
    user = (
        f"QUESTION:\n{question}\n\nANSWER:\n{answer}\n\n"
        f"GOLD FACTS ({len(expected_facts)}):\n{facts_block}\n\n"
        f'Return JSON {{"covered": [...]}} with exactly {len(expected_facts)} booleans, in order.'
    )
    messages = [
        {"role": "system", "content": _JUDGE_SYS},
        {"role": "user", "content": user},
    ]
    content = ""
    for _attempt in range(5):
        try:
            resp = litellm.completion(
                model=judge_model, messages=messages, temperature=temperature
            )
            content = resp.choices[0].message.content or ""
            break
        except Exception as exc:  # noqa: BLE001 — match the answer-call retry policy
            is_rate = "rate_limit" in str(exc).lower() or "429" in str(exc)
            if is_rate and _attempt < 4:  # don't sleep after the final attempt
                wait = min(30 * (2 ** _attempt), 120)  # cap to avoid multi-min dead sleeps
                print(f"\n  [JUDGE RATE LIMIT] waiting {wait}s...", end=" ", flush=True)
                time.sleep(wait)
            elif is_rate:
                break  # exhausted -> content="" -> None -> counted substring fallback
            else:
                raise
    covered = _parse_covered(content, len(expected_facts))
    if covered is None:
        return None
    hits = [f for f, c in zip(expected_facts, covered, strict=True) if c]
    misses = [f for f, c in zip(expected_facts, covered, strict=True) if not c]
    return len(hits) / len(expected_facts), hits, misses


def run_evaluation(
    test_set: list[dict],
    rag: RAGEngine,
    router=None,
    retrieval_only: bool = False,
    direct_model: str | None = None,
    top_k: int = TOP_K,
    temperature: float | None = None,
    full_answers: bool = False,
    judge: bool = False,
    judge_model: str = DEFAULT_JUDGE_MODEL,
    answerer=None,
    max_tokens: int = MAX_TOKENS,
) -> list[dict]:
    results: list[dict] = []
    for q in test_set:
        qid = q["id"]
        print(f"[{qid}] {q['question'][:60]}...", end=" ", flush=True)
        t0 = time.perf_counter()

        chunks = rag.retrieve(q["question"], top_k=top_k)
        retrieved_sources = [c.source for c in chunks]

        src_recall, src_hits, src_misses = check_source_recall(
            retrieved_sources,
            q.get("expected_sources", []),
            any_of=q.get("expected_sources_any"),
            # getattr 而非 c.section: 既有测试用无 section 的 duck-type chunk 桩。
            # 真 Chunk 恒有该字段; 缺失时退化为"全 None"→ section 级 gold 判 miss,
            # 是保守方向 (不会把 miss 判成 hit)。
            retrieved_sections=[getattr(c, "section", None) for c in chunks],
        )

        result: dict = {
            "id": qid,
            "category": q["category"],
            "question": q["question"],
            # 题集侧标记: 该题答案不在本 KB 范围内 (反幻觉题)。retrieval-only 下无判别力,
            # 必须带进 result 供 print_summary 排除统计, 否则空 expected_sources 恒得 1.0
            "out_of_scope": bool(q.get("out_of_scope", False)),
            "source_recall": round(src_recall, 4),
            "source_hits": src_hits,
            "source_misses": src_misses,
            "top5_sources": retrieved_sources[:5],
            "top5_similarities": [c.similarity for c in chunks[:5]],
        }

        if not retrieval_only and (router is not None or direct_model is not None):
            context = rag.format_context(chunks)
            facts = answerer.resolve(q["question"]) if answerer is not None else None
            if facts is not None:
                from server.structured_answer import augment_context
                context = augment_context(facts, context)
            messages = rag.build_messages(q["question"], context)

            comp_kwargs = build_completion_kwargs(messages, temperature, max_tokens)
            for _attempt in range(5):
                try:
                    if direct_model is not None:
                        response = litellm.completion(model=direct_model, **comp_kwargs)
                    else:
                        response = router.completion(model="default", **comp_kwargs)
                    break
                except Exception as exc:
                    if "rate_limit" in str(exc).lower() or "429" in str(exc):
                        wait = 30 * (2 ** _attempt)
                        print(f"\n  [RATE LIMIT] waiting {wait}s...", end=" ", flush=True)
                        time.sleep(wait)
                    else:
                        raise

            answer = response.choices[0].message.content or ""
            if facts is not None:
                from server.grounding import apply_counting_gate
                answer, _viol = apply_counting_gate(answer, facts)
            usage = {}
            if response.usage:
                usage = {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens,
                }

            fact_recall, fact_hits, fact_misses = check_fact_recall(
                answer, q.get("expected_facts", [])
            )
            result.update({
                "fact_recall": round(fact_recall, 4),
                "fact_hits": fact_hits,
                "fact_misses": fact_misses,
                "answer_preview": answer[:600],
                "usage": usage,
                "model": direct_model if direct_model is not None else getattr(response, "model", "unknown"),
            })
            if full_answers:
                result["answer"] = answer  # untruncated (for code-grounding / semantic judge)

            if judge:
                verdict = check_fact_recall_judge(
                    q["question"], answer, q.get("expected_facts", []),
                    judge_model=judge_model,
                    temperature=temperature if temperature is not None else 0.0,
                )
                if verdict is not None:
                    j_recall, j_hits, j_misses = verdict
                    result.update({
                        "judge_fact_recall": round(j_recall, 4),
                        "judge_fact_hits": j_hits,
                        "judge_fact_misses": j_misses,
                        "judge_parse_ok": True,
                    })
                else:
                    # unparseable judge response -> fall back to substring, flag it
                    result.update({
                        "judge_fact_recall": round(fact_recall, 4),
                        "judge_fact_hits": fact_hits,
                        "judge_fact_misses": fact_misses,
                        "judge_parse_ok": False,
                    })

        elapsed = time.perf_counter() - t0
        result["elapsed_s"] = round(elapsed, 2)

        tag = "SRC" if retrieval_only else "FULL"
        src_pct = f"{src_recall:.0%}"
        fact_pct = f"{result.get('fact_recall', 0):.0%}" if not retrieval_only else "n/a"
        judge_pct = (
            f" judge={result['judge_fact_recall']:.0%}"
            + ("" if result.get("judge_parse_ok", True) else "(parse-fail->substr)")
            if judge and not retrieval_only else ""
        )
        print(f"[{tag}] src={src_pct} fact={fact_pct}{judge_pct} {elapsed:.1f}s")
        results.append(result)

    return results


# 屏幕回执上给空转 lever 打的标记。抽成常量: 闸按它断言, 改文案不会静默让闸失效。
INERT_LEVER_MARK = "[INERT: retrieval-only, no LLM call]"


def print_summary(
    results: list[dict],
    retrieval_only: bool = False,
    threshold: float = 0.85,
    model: str | None = None,
    judge: bool = False,
) -> dict:
    # out_of_scope 题 (答案不在 KB 内) 在本 harness 无判别力 —— 空 expected_sources 恒得
    # 1.0, 计进平均值就是白送分。全部统计只跑 scored 集, out_of_scope 单列。
    out_of_scope = [r for r in results if r.get("out_of_scope")]
    # 过滤**之前**数: out_of_scope 题同样会走答题分支, n_answered 问的是"这轮发生过多少次
    # 答题", 不是"计分题里答了几道" —— 用过滤后的集合算会低报。
    n_answered = sum(1 for r in results if "answer_preview" in r)
    results = [r for r in results if not r.get("out_of_scope")]
    n = len(results)
    avg_src = sum(r["source_recall"] for r in results) / n if n else 0.0
    src_by_cat: dict[str, list[float]] = {}
    for r in results:
        src_by_cat.setdefault(r["category"], []).append(r["source_recall"])

    print("\n" + "=" * 60)
    print("EVAL SUMMARY")
    print("=" * 60)
    print(f"Questions: {n}")
    if model:
        print(f"Model:     {model}")
    print(f"Threshold: {threshold:.0%}")
    print(f"Source recall (avg): {avg_src:.1%}")
    for cat, vals in sorted(src_by_cat.items()):
        print(f"  {cat}: {sum(vals)/len(vals):.1%} ({len(vals)} q)")

    if out_of_scope:
        print(f"\nout_of_scope (未计分, 需人工看答案): {len(out_of_scope)}")
        for r in out_of_scope:
            print(f"  {r['id']}: {r['question'][:60]}")

    summary: dict = {
        # n_questions 保留旧键名 (下游兼容), 但其语义在 out_of_scope 过滤后 = 计分题数;
        # n_total 给出题集总数, 避免读者把 n_questions 当总数
        "n_questions": n,
        "n_scored": n,
        "n_total": n + len(out_of_scope),
        "n_out_of_scope": len(out_of_scope),
        # ---- 本轮到底有没有生成过答案 ----
        # 决定 summary 里 prompt_guardrail / web_search 两个**答题侧** lever 有没有因果
        # 意义: retrieval-only 不发任何 LLM 调用 (run_evaluation 的 `if not retrieval_only
        # ...` 跳过整个答题分支), 那两个 lever 完全空转, 却照样落盘 ⇒ 一份
        # `prompt_guardrail: true` 无法区分「护栏开着跑出来的答案质量」与「根本没生成答案」
        # (spec §10.1 B6)。
        # 两个键分工明确, 缺一不可:
        #   retrieval_only — 记**模式** (命令行意图)
        #   n_answered     — 记**事实** (产物自证)。答题分支另有 `router is not None or
        #     direct_model is not None` 一层条件, 所以 retrieval_only 为 False **不蕴含**
        #     真的答了题; 只有这个数能挡住"模式说会答题、实际一次都没答"。
        "retrieval_only": bool(retrieval_only),
        "n_answered": n_answered,
        "model": model,
        "threshold": threshold,
        "source_recall_avg": round(avg_src, 4),
        "source_recall_by_category": {
            cat: round(sum(vals) / len(vals), 4) for cat, vals in sorted(src_by_cat.items())
        },
    }

    if not retrieval_only:
        avg_fact = sum(r.get("fact_recall", 0) for r in results) / n if n else 0.0
        total_tokens = sum(r.get("usage", {}).get("total_tokens", 0) for r in results)
        print(f"Fact recall (substring, avg): {avg_fact:.1%}")
        print(f"Total tokens used:   {total_tokens:,}")

        fact_by_cat: dict[str, list[float]] = {}
        for r in results:
            fact_by_cat.setdefault(r["category"], []).append(r.get("fact_recall", 0))
        for cat, vals in sorted(fact_by_cat.items()):
            print(f"  {cat}: {sum(vals)/len(vals):.1%}")
        summary.update({
            "fact_recall_avg": round(avg_fact, 4),
            "fact_recall_by_category": {
                cat: round(sum(vals) / len(vals), 4) for cat, vals in sorted(fact_by_cat.items())
            },
            "total_tokens": total_tokens,
        })

        # Judge (semantic) fact recall: the trustworthy metric — drives the verdict
        # when --judge is on; substring stays reported as a (low-biased) secondary.
        gate_fact, gate_label = avg_fact, "substring"
        if judge:
            avg_judge = sum(r.get("judge_fact_recall", 0) for r in results) / n
            parse_fail = sum(1 for r in results if r.get("judge_parse_ok") is False)
            judge_by_cat: dict[str, list[float]] = {}
            for r in results:
                judge_by_cat.setdefault(r["category"], []).append(r.get("judge_fact_recall", 0))
            print(f"\nFact recall (judge/semantic, avg): {avg_judge:.1%}")
            for cat, vals in sorted(judge_by_cat.items()):
                print(f"  {cat}: {sum(vals)/len(vals):.1%}")
            if parse_fail:
                print(f"  ⚠ judge parse-fail (fell back to substring): {parse_fail}/{n} questions")
            summary.update({
                "judge_fact_recall_avg": round(avg_judge, 4),
                "judge_fact_recall_by_category": {
                    cat: round(sum(vals) / len(vals), 4) for cat, vals in sorted(judge_by_cat.items())
                },
                "judge_parse_failures": parse_fail,
            })
            gate_fact, gate_label = avg_judge, "judge"

        overall = (avg_src + gate_fact) / 2
        print(f"\nOverall (src + {gate_label} fact, avg): {overall:.1%}")
        verdict = "PASS" if overall >= threshold else "FAIL"
        print(f"Threshold: {threshold:.0%}  ->  {verdict}")
        summary.update({
            "overall": round(overall, 4),
            "overall_metric": gate_label,
            "verdict": verdict,
        })
    else:
        verdict = "PASS" if avg_src >= threshold else "FAIL"
        print(f"\nThreshold: {threshold:.0%}  ->  {verdict} (retrieval-only)")
        summary.update({"verdict": verdict})

    failures = [r for r in results if r["source_recall"] < 1.0]
    if failures:
        print(f"\nQuestions with source misses ({len(failures)}):")
        for r in failures:
            print(f"  {r['id']}: src={r['source_recall']:.0%} miss={r['source_misses']}")

    return summary


class _FederatedAdapter:
    """FederatedEngine → run_evaluation 的 rag 形状 (retrieve 返回 list, 记录判库)."""

    def __init__(self, fed, corpus: str = "auto"):
        self.fed = fed
        self.corpus = corpus
        self.routed: list[str] = []
        self.routed_fallback: list[bool | None] = []

    def retrieve(self, q, top_k=None):
        chunks, routed = self.fed.retrieve(q, corpus=self.corpus, top_k=top_k)
        self.routed.append(routed)
        self.routed_fallback.append(getattr(self.fed, "last_route_fallback", None))
        return chunks

    def format_context(self, chunks):
        return self.fed.format_context(chunks)

    def build_messages(self, q, context, history=None):
        # 本题判库 (生产 router.py 同口径 corpus=routed); 曾硬编码 "both", 会让单库题
        # 拿到双库 system prompt —— 答题闸测的就不是生产行为了。
        if not self.routed:
            raise RuntimeError("build_messages before retrieve: no routed corpus recorded")
        return self.fed.build_messages(q, context, history, corpus=self.routed[-1])


def attach_routing_fields(results: list[dict], retriever: "_FederatedAdapter") -> None:
    """逐题判库观测写进产物 (both_ruler §5-8/§5-11 缺口). 长度不齐 = 取证链断了, fail loud."""
    if len(retriever.routed) != len(results):
        raise RuntimeError(
            f"routed({len(retriever.routed)}) != results({len(results)}): "
            "per-question routing evidence broken; refusing to write partial fields")
    for r, routed, fb in zip(results, retriever.routed, retriever.routed_fallback, strict=True):
        r["routed"] = routed
        r["routed_fallback"] = fb


def _non_empty(v: str) -> str:
    """argparse type: 空串既非 None (走默认) 也非有效值, 静默回落默认库比报错更危险."""
    v = v.strip()
    if not v:
        raise argparse.ArgumentTypeError("must be a non-empty value")
    return v


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 1D Full Evaluation")
    parser.add_argument("test_set", help="Path to test_set YAML file")
    parser.add_argument("--retrieval-only", action="store_true")
    parser.add_argument("--output", help="Save results JSON to file")
    parser.add_argument(
        "--model",
        default=None,
        help="Override LLM model string (bypasses Router, uses litellm directly). "
             "E.g. anthropic/claude-sonnet-4-6, deepseek/deepseek-chat",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Pass/fail threshold (default 0.85)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=TOP_K,
        help=f"Chunks retrieved per query (default {TOP_K}); T1 ablation lever",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=MAX_TOKENS,
        help=f"V-2: explicit generation cap (default {MAX_TOKENS}). Pinned so that "
             "providers' differing defaults cannot give models different truncation "
             "rates (truncation suppresses codes -> flatters the code-grounding check)",
    )
    parser.add_argument(
        "--rerank",
        action="store_true",
        help="T2: enable Cohere rerank (wide pool -> rerank -> top_k). Needs COHERE_API_KEY",
    )
    parser.add_argument(
        "--rerank-candidates",
        type=int,
        default=None,
        help="T2 candidate pool size before rerank (default settings.rerank_candidates=100)",
    )
    parser.add_argument(
        "--query-expansion",
        choices=["none", "multiquery", "hyde", "hyde_rrf"],
        default=None,
        help="T4: rewrite query before search. multiquery=decompose+RRF, hyde=hypothetical doc, "
             "hyde_rrf=fuse original+hyde (augment, not replace)",
    )
    parser.add_argument(
        "--structured-lookup",
        action="store_true",
        help="S1: deterministic structured-lookup union-add (var/CT-code -> gold "
             "file via spec.md xref + VARIABLE_INDEX). Off by default.",
    )
    parser.add_argument(
        "--no-domain-expand",
        action="store_true",
        help="DM1 D3 kill switch: 关掉域码确定性扩写 (问句里的域码追加该域 meta.yaml 的 "
             "正式名 label, 只喂稠密/BM25)。默认跟随 settings.domain_expand_enabled, "
             "给本 flag 才强制关 —— 用于 A/B。",
    )
    parser.add_argument(
        "--hybrid",
        action="store_true",
        help="S2: hybrid BM25 (bm25s) over indexed chunks, additively fused with "
             "dense cosine (RRF default). Re-floats literal-token hits. Off by default.",
    )
    parser.add_argument(
        "--hybrid-fusion",
        choices=["rrf", "weighted"],
        default=None,
        help="S2 fusion method (default settings.hybrid_fusion=rrf). weighted uses --hybrid-alpha.",
    )
    parser.add_argument(
        "--hybrid-alpha",
        type=float,
        default=None,
        help="S2 weighted-fusion dense weight (1-alpha=BM25; default settings.hybrid_alpha=0.5)",
    )
    parser.add_argument(
        "--hybrid-pool",
        type=int,
        default=None,
        help="S2 per-list fusion pool depth (default settings.hybrid_pool=100)",
    )
    parser.add_argument(
        "--no-bm25-query-stopwords",
        action="store_true",
        help="DM1 D5 kill switch: 关掉查询侧 BM25 泛用语停用 (sdtm/cdisc/domain/dataset "
             "等), 退回 bm25s 内置 english stopwords。默认跟随 "
             "settings.bm25_query_stopwords_enabled, 给本 flag 才强制关 —— 用于 A/B。",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="Answer-model sampling temperature. Default None = provider default "
             "(non-deterministic). Set 0.0 for deterministic paired off/on comparisons.",
    )
    parser.add_argument(
        "--guardrail",
        action="store_true",
        help="Answer-side trust guardrail: append CT-code + classification grounding "
             "rules to the system prompt. Off by default (prompt byte-identical to "
             "pre-guardrail prod); pass for the guardrail-ON arm of a paired eval.",
    )
    parser.add_argument(
        "--web-search",
        action="store_true",
        help="Reproduce prod's system prompt: append the Rule 9 web-source rules, "
             "which prod carries on EVERY request (independent of the per-request "
             "'web' field). Prompt-only -- eval does NOT search the web, because the "
             "tool loop lives solely in /api/ask_stream. Pass it whenever the numbers "
             "are meant to describe the production configuration.",
    )
    parser.add_argument(
        "--full-answers",
        action="store_true",
        help="Store the untruncated answer per question (field 'answer') in addition to "
             "the 600-char preview. Needed for code-grounding / semantic-judge passes.",
    )
    parser.add_argument(
        "--judge",
        action="store_true",
        help="Semantic fact recall: an LLM judge decides per gold fact whether the answer "
             "conveys it by meaning (fixes the substring metric's ~11pt under-count). Adds "
             "one judge LLM call per question; reports judge_fact_recall and drives the "
             "PASS/FAIL verdict (substring kept as a secondary metric).",
    )
    parser.add_argument(
        "--judge-model",
        default=DEFAULT_JUDGE_MODEL,
        help=f"Model for --judge (default {DEFAULT_JUDGE_MODEL}; temp=0). Kept separate "
             f"from --model so the judge is independent of the answerer.",
    )
    parser.add_argument(
        "--structured-answer",
        action="store_true",
        help="SP2: inject meta.yaml authoritative facts + counting gate (eval/prod parity "
             "via shared augment_context + apply_counting_gate helpers).",
    )
    parser.add_argument(
        "--graph-answer",
        action="store_true",
        help="SP3: add deterministic graph (relationship/impact) facts",
    )
    parser.add_argument(
        "--aggregate-answer",
        action="store_true",
        help="AGG: add deterministic aggregate facts (variables-in-min-domains / "
             "most-shared codelists; split out of the SP3 graph channel)",
    )
    parser.add_argument(
        "--collection",
        default=None,
        type=_non_empty,
        help="Override settings.collection_name (e.g. study_st01). Forces "
             "structured-lookup OFF: the S1 gold map is CDISC-specific.",
    )
    parser.add_argument(
        "--kb-root",
        default=None,
        type=_non_empty,
        help="Override settings.kb_root (dir holding the indexed corpus)",
    )
    parser.add_argument(
        "--federated", action="store_true",
        help="Plan B: cdisc+study 双引擎 + LLM 路由 (corpus=auto) 走全联邦检索路径。"
             "与 --collection/--kb-root 互斥。study 引擎 S1 恒关。",
    )
    parser.add_argument(
        "--study-lookup", action="store_true",
        help="S2: study 侧确定性直查 union-add (catalog+别名表)。需 --collection <study "
             "collection> 或 --federated (作用于其 study 引擎)",
    )
    parser.add_argument(
        "--study-docs", action="store_true",
        help="U2: study 侧 doc 通道 (手順書章节 chunk 追加 N 席)。需 --federated",
    )
    parser.add_argument(
        "--doc-seats", type=int, default=None,
        help="doc 追加席位数 N (默认取 settings.study_docs_seats)。加席不抢席: "
             "cards 的 top_k 不受影响",
    )
    parser.add_argument(
        "--corpus", default="auto", choices=["auto", "cdisc", "study", "both"],
        help="强制判库 (默认 auto = 走 LLM 路由, 与生产逐字相同)。强制 study 用于把"
             "判库损耗与接线损耗拆开",
    )
    parser.add_argument(
        "--signal-layer", choices=("off", "on"), default="off",
        help="U6 确定性信号层 (widen-only)。默认 off = 判库行为逐位同挂之前; "
             "on 经生产同款工厂 build_signals 挂上 (答题侧 off/on 双臂的唯一开关)",
    )
    parser.add_argument(
        "--tag",
        default=None,
        help="Optional label added to output JSON for cross-model comparison",
    )
    args = parser.parse_args(argv)

    if args.federated and (args.collection or args.kb_root):
        parser.error("--federated 与 --collection/--kb-root 互斥 (联邦模式引擎路径取自 settings)")
    if args.study_lookup and not (args.collection or args.federated):
        parser.error("--study-lookup 需要 --collection 或 --federated")
    if args.study_docs and not args.federated:
        parser.error("--study-docs 需要 --federated (doc 通道挂在联邦的 study 引擎上)")
    if args.corpus != "auto" and not args.federated:
        parser.error("--corpus 只在 --federated 下有意义")
    if args.signal_layer == "on" and not args.federated:
        parser.error("--signal-layer 只在 --federated 下有意义 (信号层挂在联邦判库上)")
    if args.signal_layer == "on" and args.corpus != "auto":
        # 强制判库不走 decide_corpus ⇒ 信号层整层惰性, 而 summary 与回执照样写 "on"。
        # 那是假标签面: 一批信号层从未通电的数字, 事后与真 on 臂一字不差。
        parser.error("--signal-layer on 只在 --corpus auto 下有意义 "
                     "(强制判库不经 decide_corpus, 信号层不会被调用)")

    collection_name = args.collection or settings.collection_name
    kb_root = Path(args.kb_root) if args.kb_root else settings.kb_root
    if args.collection and not args.kb_root:
        print(
            f"warning: --collection {args.collection} given without --kb-root; "
            f"kb_root stays at {settings.kb_root} and may not match this collection"
        )
    structured_lookup = args.structured_lookup and args.collection is None
    if args.structured_lookup and not structured_lookup:
        print("--structured-lookup ignored: S1 gold map only applies to the CDISC collection")

    # S2: catalog 缺失响亮失败 —— 显式给了 --study-lookup 却静默不通电, 会把一次退回基线的
    # 评测读成"S2 没效果"。
    study_lookup = None
    if args.study_lookup:
        from server.study_lookup import StudyLookup
        study_lookup = StudyLookup.from_paths(
            settings.study_catalog_path, settings.study_aliases_path)
    # 联邦模式下主引擎是 cdisc 引擎, S2 归下面那台 study 引擎; 非联邦时 flag 闸已保证
    # --collection 在场 (即这台就是指向 study 库的那台)。
    main_study_lookup = None if args.federated else study_lookup

    # DM1 D3: 域码扩写器。一个对象喂本次运行的全部引擎 (cdisc / study cards / study docs),
    # 与生产 lifespan 同一个装配点 (server/domain_expand.build_expander) —— 那里说明了它
    # 为什么恒读 settings 的路径而不跟 --kb-root 覆盖走。
    domain_expander = (
        None if args.no_domain_expand
        else build_expander(settings) if settings.domain_expand_enabled
        else None
    )
    # DM1 D5 kill switch: 同上模式, 缺 flag 时跟 settings 走。
    bm25_query_stopwords = (
        False if args.no_bm25_query_stopwords else settings.bm25_query_stopwords_enabled
    )

    test_set = load_test_set(args.test_set)
    print(f"Loaded {len(test_set)} questions from {args.test_set}")

    rag = RAGEngine(
        chroma_dir=settings.chroma_dir,
        kb_root=kb_root,
        collection_name=collection_name,
        embedding_model=settings.embedding_model,
        top_k=args.top_k,
        rerank_enabled=args.rerank,
        rerank_model=settings.rerank_model,
        rerank_candidates=(
            args.rerank_candidates
            if args.rerank_candidates is not None
            else settings.rerank_candidates
        ),
        query_expansion=args.query_expansion or settings.query_expansion,
        expansion_model=settings.expansion_model,
        expansion_n_queries=settings.expansion_n_queries,
        structured_lookup_enabled=structured_lookup,
        domain_definition_seat=settings.domain_definition_seat_enabled,
        domain_expander=domain_expander,
        study_lookup=main_study_lookup,
        hybrid_enabled=args.hybrid,
        hybrid_fusion=args.hybrid_fusion or settings.hybrid_fusion,
        hybrid_alpha=(
            args.hybrid_alpha if args.hybrid_alpha is not None else settings.hybrid_alpha
        ),
        hybrid_pool=(
            args.hybrid_pool if args.hybrid_pool is not None else settings.hybrid_pool
        ),
        bm25_query_stopwords=bm25_query_stopwords,
        prompt_guardrail_enabled=args.guardrail,
        # Rule 9 是否进 system prompt。生产恒 on 且与请求级 web 真假无关 ⇒ 不给
        # --web-search 跑出来的数字描述的是一个生产不跑的构型 (spec §10.1 B3')。
        # ⚠ 本 lever 只复现 prompt 构型, eval 并不联网 —— 工具循环只在 /api/ask_stream (§10.0)。
        # ⚠ 将来 eval 真接工具循环时, 必须用这同一个 args.web_search 同时驱动循环与本
        #   lever, 不得新开第二个 flag: 否则会跑「无 Rule 9 构型」却当生产数字上报。
        web_search_enabled=args.web_search,
    )
    rerank_info = (
        f", rerank={rag.rerank_model} pool={rag.rerank_candidates}" if args.rerank else ""
    )
    qexpand_info = (
        f", expansion={rag.query_expansion}({rag.expansion_model})"
        if rag.query_expansion != "none" else ""
    )
    lookup_info = ", structured_lookup=ON" if structured_lookup else ""
    # 读引擎实收值: 默认开的 lever 一旦装配点漏改, 屏幕/落盘都得跟着变成 OFF。
    expand_info = ", domain_expand=ON" if rag.domain_expander is not None else ""
    # 屏幕回执: 不给 --output 时 summary JSON 看不到, 人肉跑就完全看不出 S2 开没开
    study_lookup_info = (
        f", study_lookup=ON({main_study_lookup.stats()})"
        if main_study_lookup is not None else ""
    )
    hybrid_info = (
        f", hybrid={rag.hybrid_fusion}"
        + (f"(alpha={rag.hybrid_alpha})" if rag.hybrid_fusion == "weighted" else "")
        if args.hybrid else ""
    )
    # 下面两个回执读**引擎实收值**而不是 args: 记事实, 不记意图。读 args 时注入点漏改
    # (引擎实收 OFF) 屏幕照打 ON, 就能跑出一批标着 ON 实际 OFF 的 140q 数字, 事后无从分辨。
    # 同 print 里 rerank_info / qexpand_info / hybrid_info 一向读 rag.*, 这里对齐。
    # retrieval-only 一次 LLM 调用都不发 ⇒ 这两个**答题侧** lever 完全空转。不标注就会
    # 在屏幕上打出一个与本轮产物无因果关系的 "guardrail=ON" (spec §10.1 B6)。只标注开着
    # 的那个 —— 关着时 info 串本来就是空的, 没有可误导的东西。
    inert = INERT_LEVER_MARK if args.retrieval_only else ""
    guardrail_info = f", guardrail=ON{inert}" if rag.prompt_guardrail_enabled else ""
    # web_search 文案额外写死"不联网": flag 名读起来像 eval 会去搜, 实际只是 prompt 构型 (§10.0)
    web_search_info = (
        f", web_search=ON(prompt-only, no live search){inert}"
        if rag.web_search_enabled else ""
    )
    collection_info = f", collection={collection_name}" if args.collection else ""
    print(f"RAG engine: {rag.collection.count()} chunks, model={settings.default_model}, top_k={args.top_k}{rerank_info}{qexpand_info}{lookup_info}{expand_info}{study_lookup_info}{hybrid_info}{guardrail_info}{web_search_info}{collection_info}")

    # 联邦模式: 上面那台是 cdisc 引擎, 再起一台 study 引擎 (S1 恒关 —— gold map 是 CDISC 专属),
    # 其余 lever 与 cdisc 一致, 由 FederatedEngine 判库分发。retriever 是喂给 run_evaluation 的
    # 那一台; rag 仍指向 cdisc 引擎, 供下方 info/summary 读 lever 实参。
    retriever = rag
    if args.federated:
        # 检索杠杆一份, 两台 study 引擎共用 (Task 3b)。原先 docs 引擎这份是手抄的, 少了
        # rerank/expansion 三族 ⇒ 跑 `--rerank`/`--query-expansion` 时 cards 与 docs 口径
        # 不一致, 而数字上完全看不出来。共用一份后"漏一个 lever"在结构上不可能。
        study_levers = dict(
            rerank_enabled=args.rerank,
            rerank_model=settings.rerank_model,
            rerank_candidates=(
                args.rerank_candidates
                if args.rerank_candidates is not None
                else settings.rerank_candidates
            ),
            query_expansion=args.query_expansion or settings.query_expansion,
            expansion_model=settings.expansion_model,
            expansion_n_queries=settings.expansion_n_queries,
            hybrid_enabled=args.hybrid,
            hybrid_fusion=args.hybrid_fusion or settings.hybrid_fusion,
            hybrid_alpha=(
                args.hybrid_alpha if args.hybrid_alpha is not None else settings.hybrid_alpha
            ),
            hybrid_pool=(
                args.hybrid_pool if args.hybrid_pool is not None else settings.hybrid_pool
            ),
            bm25_query_stopwords=bm25_query_stopwords,
            prompt_guardrail_enabled=args.guardrail,
            # 与上面 cdisc 引擎同一个 args.web_search —— 两处注入点必须同源: 只改一处时
            # 联邦两臂的 prompt 构型不一致, 而数字上完全看不出来 (B3' 就是这么活下来的)。
            web_search_enabled=args.web_search,
            # 与上面 cdisc 引擎同一个对象 —— 各造一份会让两臂对同一问句扩写不同, 而
            # 数字上完全看不出来 (与 web_search 同源纪律)。
            domain_expander=domain_expander,
        )
        study_rag = RAGEngine(
            chroma_dir=settings.chroma_dir,
            kb_root=settings.study_kb_root,
            collection_name=settings.study_collection_name,
            embedding_model=settings.embedding_model,
            top_k=args.top_k,
            structured_lookup_enabled=False,
            study_lookup=study_lookup,
            **study_levers,
        )
        study_engine = study_rag
        if args.study_docs:
            doc_seats = (
                args.doc_seats if args.doc_seats is not None else settings.study_docs_seats
            )
            # 装配走 server/study_corpus.py 的工厂 —— server/main.py 的 lifespan 是同一个
            # 调用。两条路径共用一个装配点, 尺子量的引擎与生产跑的引擎因此不会各自漂移。
            from server.study_corpus import StudyCorpusEngine, make_docs_engine
            docs_rag = make_docs_engine(
                RAGEngine,
                chroma_dir=settings.chroma_dir,
                kb_root=settings.study_kb_root,      # 与 U1 上界口径逐字相同
                collection_name=settings.study_docs_collection_name,
                embedding_model=settings.embedding_model,
                seats=doc_seats,
                levers=study_levers,
            )
            study_engine = StudyCorpusEngine(study_rag, docs_rag, doc_seats=doc_seats)
            print(f"Study docs channel: {docs_rag.collection.count()} chunks, "
                  f"collection={settings.study_docs_collection_name}, seats={doc_seats}")
        # U6 信号层: 惰性导入且只在 on 分支 —— 默认路径 (含全量单测) 因此不依赖它。
        # 生产 lifespan 复用同一份 S2, 这里同样传 study_lookup: 另造一份可以来自别的文件
        # (路径 override 只改一处时), 而信号层用的那份从不出现在任何日志里。
        signals = None
        if args.signal_layer == "on":
            from server.routing_signals import build_signals
            signals = build_signals(settings, study_lookup=study_lookup)
            # 工厂返回 None 就等于悄悄跑成 off, 而 summary 仍写 "on" —— 那批数字会被当成
            # 「信号层开着」的证据引用 (run_routing_eval 同款闸)。
            if signals is None:
                raise SystemExit("--signal-layer on 但 build_signals 返回 None —— "
                                 "信号层未装配, 拒绝跑出一批会被误读成「开着」的数字")
        retriever = _FederatedAdapter(
            FederatedEngine(rag, study_engine, create_router(settings), top_k=args.top_k,
                            signals=signals),
            corpus=args.corpus,
        )
        print(
            f"Federated: study engine {study_rag.collection.count()} chunks, "
            f"collection={settings.study_collection_name}, structured_lookup=OFF"
            f", study_lookup={f'ON({study_lookup.stats()})' if study_lookup is not None else 'OFF'}; "
            # corpus 曾硬编码 auto: 强制档跑批的屏幕与日志因此自称 auto, 而那正是
            # U5 用来拆「判库损耗 vs 接线损耗」的开关 —— 回执必须打命令行真给的那个。
            f"routing={'LLM(light)' if args.corpus == 'auto' else 'forced'}"
            f"(corpus={args.corpus}), signal_layer={args.signal_layer}"
        )

    router = None
    if not args.retrieval_only:
        if args.model:
            print(f"LLM mode: direct litellm, model={args.model}")
        else:
            router = create_router(settings)
            print(f"LLM router: {len(router.model_list)} models")

    answerer = None
    if args.structured_answer or args.graph_answer or args.aggregate_answer:
        from server.meta_store import MetaStore
        store = MetaStore(settings.meta_path)
        engine = None
        if args.graph_answer or args.aggregate_answer:
            from server.graph_engine import GraphEngine
            engine = GraphEngine(store)
        parts = []
        if args.structured_answer:
            from server.structured_answer import StructuredAnswerer
            parts.append(StructuredAnswerer(store))
        if args.aggregate_answer:
            from server.aggregate_answer import AggregateAnswerer
            parts.append(AggregateAnswerer(engine))
        if args.graph_answer:
            from server.graph_answer import GraphAnswerer
            parts.append(GraphAnswerer(engine))
        if len(parts) == 1:
            answerer = parts[0]
        else:
            from server.structured_answer import CompositeAnswerer
            answerer = CompositeAnswerer(parts)
        print("Structured-answer channel: ON (meta.yaml facts + counting gate)"
              + (", aggregate-answer: ON" if args.aggregate_answer else "")
              + (", graph-answer: ON" if args.graph_answer else ""))

    print()
    if args.judge and not args.retrieval_only:
        print(f"Judge mode: ON, judge_model={args.judge_model} (temp=0)")
    results = run_evaluation(
        test_set, retriever, router, args.retrieval_only, direct_model=args.model,
        top_k=args.top_k, temperature=args.temperature, full_answers=args.full_answers,
        judge=args.judge, judge_model=args.judge_model, answerer=answerer,
        max_tokens=args.max_tokens,
    )
    summary = print_summary(
        results,
        retrieval_only=args.retrieval_only,
        threshold=args.threshold,
        model=args.model,
        judge=args.judge,
    )
    summary["top_k"] = args.top_k
    if args.rerank:
        summary["rerank"] = {
            "model": rag.rerank_model,
            "candidates": rag.rerank_candidates,
        }
    if rag.query_expansion != "none":
        summary["query_expansion"] = {
            "mode": rag.query_expansion,
            "model": rag.expansion_model,
            "n_queries": rag.expansion_n_queries,
        }
    if structured_lookup:
        summary["structured_lookup"] = True
    if args.study_lookup:
        summary["study_lookup"] = True
    if args.hybrid:
        summary["hybrid"] = {
            "fusion": rag.hybrid_fusion,
            "alpha": rag.hybrid_alpha if rag.hybrid_fusion == "weighted" else None,
        }
    if args.collection:
        summary["collection"] = collection_name
    if args.federated:
        attach_routing_fields(results, retriever)
        routing = dict(Counter(retriever.routed))
        print(f"routing: {routing}")
        summary["federated"] = True
        summary["routing"] = routing
        # 两臂产物除文件名外必须能自证 off/on —— 事后只靠文件名认臂是没有取证价值的
        summary["signal_layer"] = args.signal_layer
    # 两行同口径: 记**引擎实收值**(事实), 不记 args(意图) —— 注入点漏改时这两行会跟着变,
    # 而读 args 会落盘一个与引擎无关的标签 (标着 ON 实际 OFF 的数字, 事后无从分辨)。
    # ⚠ 这两个是**答题侧** lever: 只在真发生 LLM 调用时才有因果意义。它们是否空转,
    # 由 print_summary 落的 retrieval_only / n_answered 两个键作证 (spec §10.1 B6) ——
    # 单看这两行会把"没答题"读成"护栏开着的答案质量"。
    summary["prompt_guardrail"] = rag.prompt_guardrail_enabled
    summary["web_search"] = rag.web_search_enabled
    summary["structured_answer"] = args.structured_answer
    summary["graph_answer"] = args.graph_answer
    summary["aggregate_answer"] = args.aggregate_answer
    # V-1: 检索实参必须落盘, 否则事后重建上下文只能猜 —— 2026-09-02 那轮
    # check_code_grounding.py 猜错 (写死 lookup/hybrid=ON, 实际全 OFF), 8 条 ungrounded
    # 全是假阳性。同上, 记**引擎实收值**不记 args。
    summary["retrieval_levers"] = {
        "top_k": rag.top_k,
        "structured_lookup": rag.structured_lookup_enabled,
        "domain_definition_seat": rag.domain_definition_seat,
        # 记**引擎实收**的有/无 (bool), 不记 args —— 装配点漏改时这行会跟着变。
        "domain_expand": rag.domain_expander is not None,
        "hybrid": rag.hybrid_enabled,
        "bm25_query_stopwords": rag.bm25_query_stopwords,
        "rerank": rag.rerank_enabled,
        "query_expansion": rag.query_expansion,
    }
    # V-2: 上限本身 + 撞顶的题。撞顶 = 答案很可能被切在句中 ⇒ 少发码 ⇒ (a) 层偏乐观。
    summary["max_tokens"] = args.max_tokens
    truncated = find_truncated(results, args.max_tokens)
    summary["truncated"] = truncated
    if truncated:
        print(f"\n⚠ TRUNCATED at max_tokens={args.max_tokens} ({len(truncated)}): "
              f"{', '.join(truncated)}")
    if args.judge:
        summary["judge_model"] = args.judge_model

    if args.output:
        out: dict = {"summary": summary, "results": results}
        if args.tag:
            out["tag"] = args.tag
        Path(args.output).write_text(
            json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"\nResults saved to {args.output}")

    return 0 if summary["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
