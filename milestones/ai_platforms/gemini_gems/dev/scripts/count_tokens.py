#!/usr/bin/env python3
"""Token counter for SDTM Phase 6.5 Gemini Gems 单批合并.

依据 PLAN.md §1.2 P1 (量化 PASS 标准 `<file>: <N> tokens`) + §2.4 (脚本单一职责).
依据 Phase 1 research Q1 (1M 窗口 needle-in-haystack 单针 >99.7% @ 1M, 多针 ~60%
@ 1M; token 计数需准确, 以验 P11 单批 ≤800K 约束).

Usage:
    python3 count_tokens.py <path> [<path> ...] [--total-only]

- <path> 是文件: 打印 "<file>: <N> tokens"
- <path> 是目录: 递归统计所有 .md 文件
- 多个 path: 汇总到单一 TOTAL
- --total-only: 只打印 "TOTAL: <N>"

只读: 不修改源文件 (PLAN §1.2 P5).

Project root: ai_platforms/gemini_gems/ (仅用于自指示范, 本脚本接受任意 path).
Dependencies: tiktoken (cl100k_base encoding, 与 Claude v2 count_tokens.py 一致).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

import tiktoken

ENCODING_NAME = "cl100k_base"


def iter_md_files(path: Path) -> Iterable[Path]:
    """Yield .md 文件 (目录递归 or 单文件自身)."""
    if path.is_file():
        yield path
        return
    if path.is_dir():
        for md in sorted(path.rglob("*.md")):
            if md.is_file():
                yield md
        return
    print(f"error: path not found: {path}", file=sys.stderr)
    sys.exit(2)


def count_tokens(encoder: "tiktoken.Encoding", file_path: Path) -> int:
    """用 tiktoken cl100k_base 计算单文件 token 数."""
    text = file_path.read_text(encoding="utf-8", errors="strict")
    return len(encoder.encode(text))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Count tokens in Markdown files using tiktoken cl100k_base."
    )
    parser.add_argument("paths", nargs="+", help="file(s) or directory(ies) to scan")
    parser.add_argument(
        "--total-only",
        action="store_true",
        help="print only the combined TOTAL line",
    )
    args = parser.parse_args(argv)

    encoder = tiktoken.get_encoding(ENCODING_NAME)

    total = 0
    file_count = 0
    for raw in args.paths:
        root = Path(raw)
        for md in iter_md_files(root):
            n = count_tokens(encoder, md)
            total += n
            file_count += 1
            if not args.total_only:
                print(f"{md}: {n} tokens")

    if args.total_only:
        print(f"TOTAL: {total}")
    elif file_count != 1:
        print(f"TOTAL: {total} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
