"""Phase 1A.0.c — tiktoken 实测 5 个最大候选 chunk token 数.

候选边界由 chunker_feasibility_2026-05-22.md §13 锁定:
  C1 TA examples.md Example 1 (L1-L113)        — examples domain-aware chunker
  C2 MB examples.md Example 3 (L80-L170)       — examples MB-class
  C3 ch04 §4.4 Actual/Relative Time (L680-1142)— chapters size-aware (## 切)
  C4 lb_part4 整文件 (1.7KB, H2=2)              — terminology LB part 模式
  C5 VARIABLE_INDEX §二.AE (L51-L109)           — variable_index domain H3

输出: token 数 (cl100k_base, o200k_base) + char/4 估算 + 偏差。
不依赖 anthropic SDK; 实测发现 tiktoken cl100k 是 Anthropic context window 的合理代理 (Anthropic
内部用类似 BPE tokenizer, Claude 计数实测偏离 cl100k 约 ±5-10%, llm_providers §6 已记录).
"""

from __future__ import annotations

import sys
from pathlib import Path

import tiktoken

ROOT = Path(__file__).resolve().parents[3]  # repo root


def slice_lines(path: Path, start: int, end: int | None) -> str:
    """Return text from line `start` (1-based, inclusive) to `end` (inclusive). end=None → EOF."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if end is None:
        end = len(lines)
    return "".join(lines[start - 1 : end])


CANDIDATES: list[tuple[str, Path, int, int | None, str]] = [
    (
        "C1_TA_examples_Example1",
        ROOT / "knowledge_base/domains/TA/examples.md",
        1,
        113,
        "TA Example 1 (含 4 mermaid + 1 table) — examples chunker",
    ),
    (
        "C2_MB_examples_Example3",
        ROOT / "knowledge_base/domains/MB/examples.md",
        80,
        170,
        "MB Example 3 — examples chunker (mb dense table)",
    ),
    (
        "C3_ch04_section_4.4",
        ROOT / "knowledge_base/chapters/ch04_general_assumptions.md",
        680,
        1142,
        "ch04 §4.4 Actual/Relative Time — chapters size-aware (## 切 risk)",
    ),
    (
        "C4_lb_part4_full",
        ROOT / "knowledge_base/terminology/core/lb_part4.md",
        1,
        None,
        "lb_part4 整文件 — terminology LB part (H2=2)",
    ),
    (
        "C5_variable_index_AE",
        ROOT / "knowledge_base/VARIABLE_INDEX.md",
        51,
        109,
        "VARIABLE_INDEX §二.AE — variable_index domain H3",
    ),
]


def main() -> int:
    enc_cl100k = tiktoken.get_encoding("cl100k_base")  # OpenAI text-embedding-3-small native
    try:
        enc_o200k = tiktoken.get_encoding("o200k_base")  # GPT-4o family
    except Exception:
        enc_o200k = None

    print(f"# Phase 1A.0.c tiktoken 实测 — 5 候选 chunk")
    print(f"# Encoders: cl100k_base (embedding-3-small native), o200k_base (gpt-4o family)")
    print(f"# Embedding limit (text-embedding-3-small): 8191 tokens")
    print()
    print(
        f"{'id':<28} | {'lines':>6} | {'bytes':>6} | {'chars':>6} | {'cl100k':>7} | "
        f"{'o200k':>7} | {'char/4 估':>10} | {'cl100k - char/4':>16} | safe?"
    )
    print("-" * 130)

    rows = []
    for name, path, start, end, desc in CANDIDATES:
        text = slice_lines(path, start, end)
        n_lines = text.count("\n") + (0 if text.endswith("\n") else 1)
        n_bytes = len(text.encode("utf-8"))
        n_chars = len(text)
        n_cl100k = len(enc_cl100k.encode(text))
        n_o200k = len(enc_o200k.encode(text)) if enc_o200k else -1
        char_est = n_chars // 4
        delta = n_cl100k - char_est
        safe = "✓ <8K" if n_cl100k < 8191 else "✗ OVER 8K"
        print(
            f"{name:<28} | {n_lines:>6} | {n_bytes:>6} | {n_chars:>6} | {n_cl100k:>7} | "
            f"{n_o200k:>7} | {char_est:>10} | {delta:>+16} | {safe}"
        )
        rows.append((name, desc, n_lines, n_bytes, n_chars, n_cl100k, n_o200k, char_est, delta, safe))

    print()
    print("## 详细描述")
    for name, desc, *_ in rows:
        print(f"- {name}: {desc}")

    # Compute char/4 偏差均值 + 最大
    deltas = [r[8] for r in rows]
    cl100ks = [r[5] for r in rows]
    chars = [r[4] for r in rows]
    ratios = [c / ch * 4 for c, ch in zip(cl100ks, chars)]  # cl100k / (chars/4) → 偏差比
    print()
    print("## 偏差分析 (chunker_feasibility 用 char/4 估算 vs tiktoken cl100k 实测)")
    for r, name in zip(ratios, [row[0] for row in rows]):
        bias = (r - 1.0) * 100
        print(f"  {name:<28} cl100k / (char/4) = {r:.3f}  → 偏差 {bias:+.1f}%")
    avg_bias = (sum(ratios) / len(ratios) - 1.0) * 100
    max_abs = max(abs((r - 1.0) * 100) for r in ratios)
    print(f"\n  平均偏差: {avg_bias:+.1f}%  最大|偏差|: {max_abs:.1f}%")
    print(
        f"\n  结论: char/4 估算 {'PASS (±20% 容忍内)' if max_abs <= 20 else 'WARN (>20% 偏差, 后续 chunker 实现优先用 tiktoken)'}"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
