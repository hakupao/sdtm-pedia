#!/usr/bin/env python3
"""SDTM Phase 6.5 Gemini Gems 产物校验脚本.

依据文档:
- PLAN.md §4 Phase B6 (validate_gemini.py 产物完整性校验)
- PLAN.md §1.3 P11 (总 ≤800K, 硬警 >900K)
- PLAN.md §1.3 P12 (末尾召回 hard checkpoint 准备: 04 尾部 30% 内 ≥3 codelist 段)
- PLAN.md §2.1 (4 合并文件 + 预期源段数)
- PLAN.md §8 R2 (超限降级)

依据 Phase 1 research:
- Q2: 10 文件硬限 / 100 MB per file (本校验 <5MB 远低于硬限, 防御性)
- Q1: 1M 窗口 + 多针降级 ⇒ total ≤800K 留响应余量

Usage:
    python3 validate_gemini.py [--stage {core|spec|knowledge|terminology|all}] [--uploads DIR]

校验项:
- V1 非空: 每文件 size > 0
- V2 段数对齐: `<!-- source: ... -->` 段数 ≥ PLAN §2.1 预期 (01≥15, 02≥63, 03≥126, 04 记录不判 FAIL)
- V3 token 上限: 单文件 + 累计 ≤800K; >900K 触 §8 R2 警告 (rc=2); >1000K FAIL
- V4 单文件 <5MB: 字节大小 (Gemini 100MB 上限远高, 本项防御)
- V5 md5 稳定: 输出 md5 供 Node 2 对比 (纯记录, 不判 FAIL)
- V6 位置策略合规: 04 产物末尾 30% 内 ≥3 个 `<!-- source: terminology ... -->` (P12 准备)

Return codes:
- rc=0: 全 PASS
- rc=1: V1/V4/V5/V6 任一 FAIL (硬失败)
- rc=2: V3 警告 (>900K 未超 1M, 但 P11 破线)

产出: dev/evidence/validate_single_batch.md (md 表格).

Dependencies: tiktoken (cl100k_base), Python 3 stdlib.
Read-only over uploads/ + 源 (P5).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import re
import sys
from pathlib import Path

import tiktoken

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent                # ai_platforms/gemini_gems/
REPO_ROOT = PROJECT_ROOT.parent.parent                 # SDTM-compare/

DEFAULT_UPLOADS = PROJECT_ROOT / "current" / "uploads"
EVIDENCE_DIR = PROJECT_ROOT / "dev" / "evidence"
REPORT_PATH = EVIDENCE_DIR / "validate_single_batch.md"

ENCODING_NAME = "cl100k_base"

# PLAN §2.1 合并文件映射 + 预期源段数
STAGE_FILES = {
    "core": {
        "name": "01_core_reference.md",
        "expected_sources_min": 15,        # 6 chapters + 6 model + 3 nav ≈ 15
        "target_tokens": 120_000,
    },
    "spec": {
        "name": "02_domain_specs.md",
        "expected_sources_min": 63,        # 63 domains
        "target_tokens": 168_000,
    },
    "knowledge": {
        "name": "03_domain_knowledge.md",
        "expected_sources_min": 126,       # 63 × 2 (assumptions + examples)
        "target_tokens": 225_000,
    },
    "terminology": {
        "name": "04_terminology_core.md",
        "expected_sources_min": 0,          # P12 Node 2 校准, 先记录不判 FAIL
        "target_tokens": 200_000,
    },
}
STAGE_ORDER = ["core", "spec", "knowledge", "terminology"]

# 阈值
SINGLE_FILE_BYTE_HARD = 5 * 1024 * 1024    # 5MB 防御上限
TOTAL_TOKEN_TARGET = 800_000               # P11 target
TOTAL_TOKEN_WARN = 900_000                 # §8 R2 warn
TOTAL_TOKEN_HARD = 1_000_000               # 1M 窗口硬上限

# V6 P12 末尾 30% 内至少几段 terminology
V6_TAIL_FRACTION = 0.30
V6_TAIL_MIN_TERM_SEGMENTS = 3

SOURCE_MARK_RE = re.compile(r"^<!--\s*source:\s*([^\s]+)\s*-->", re.MULTILINE)


# ---------------------------------------------------------------------------
# 结果记录
# ---------------------------------------------------------------------------


class Result:
    def __init__(self) -> None:
        self.rows: list[dict] = []
        self.hard_fail = False
        self.warn = False
        self.total_tokens = 0

    def add(self, row: dict) -> None:
        self.rows.append(row)


def _now_iso() -> str:
    return (
        _dt.datetime.now(_dt.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def _md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _count_source_marks(text: str) -> tuple[int, list[tuple[int, str]]]:
    """返回 (总段数, [(offset, path), ...])."""
    positions: list[tuple[int, str]] = []
    for m in SOURCE_MARK_RE.finditer(text):
        positions.append((m.start(), m.group(1)))
    return len(positions), positions


def _v6_tail_terminology(text: str, positions: list[tuple[int, str]]) -> tuple[bool, int]:
    """V6: 04 产物尾部 30% 内 ≥3 个 `terminology/...` 源段.

    text: 完整文件内容; positions: [(offset, rel_path), ...]
    返回 (pass?, 尾部段数).
    """
    total_len = len(text)
    tail_start = int(total_len * (1.0 - V6_TAIL_FRACTION))
    tail_term_segments = [
        rel for offset, rel in positions
        if offset >= tail_start and "terminology" in rel
    ]
    return (len(tail_term_segments) >= V6_TAIL_MIN_TERM_SEGMENTS, len(tail_term_segments))


# ---------------------------------------------------------------------------
# 校验主体
# ---------------------------------------------------------------------------


def validate_file(
    stage_key: str,
    path: Path,
    encoder: "tiktoken.Encoding",
    result: Result,
) -> None:
    spec = STAGE_FILES[stage_key]
    row = {
        "stage": stage_key,
        "file": spec["name"],
        "exists": path.is_file(),
        "bytes": 0,
        "tokens": 0,
        "source_segments": 0,
        "target_tokens": spec["target_tokens"],
        "md5": "",
        "v1_nonempty": False,
        "v2_segments_ok": False,
        "v4_under_5mb": False,
        "v6_tail_ok": None,        # None=仅 terminology 判定
        "v6_tail_count": None,
        "notes": [],
    }

    if not row["exists"]:
        row["notes"].append("FILE NOT FOUND")
        result.hard_fail = True
        result.add(row)
        return

    # V1 非空 + V4 size
    st = path.stat()
    row["bytes"] = st.st_size
    row["v1_nonempty"] = st.st_size > 0
    row["v4_under_5mb"] = st.st_size < SINGLE_FILE_BYTE_HARD
    if not row["v1_nonempty"]:
        row["notes"].append("V1 FAIL: empty file")
        result.hard_fail = True
    if not row["v4_under_5mb"]:
        row["notes"].append(f"V4 FAIL: {st.st_size} bytes ≥ 5MB")
        result.hard_fail = True

    # 读内容
    text = path.read_text(encoding="utf-8", errors="strict")

    # V5 md5
    row["md5"] = _md5(path)

    # token 计数
    row["tokens"] = len(encoder.encode(text))
    result.total_tokens += row["tokens"]

    # V2 段数
    seg_count, positions = _count_source_marks(text)
    row["source_segments"] = seg_count
    min_expected = spec["expected_sources_min"]
    if min_expected > 0:
        row["v2_segments_ok"] = seg_count >= min_expected
        if not row["v2_segments_ok"]:
            row["notes"].append(
                f"V2 WARN: segments {seg_count} < expected {min_expected}"
            )
            # V2 偏离记录为 WARN (不触 hard fail, Node 2 A/B 校准)
            result.warn = True
    else:
        # terminology: 记录不判
        row["v2_segments_ok"] = True
        row["notes"].append(f"V2 INFO: {seg_count} segments recorded (no min cap)")

    # V6 仅对 terminology 判 (尾部 recency + P12 hard checkpoint 准备)
    if stage_key == "terminology":
        ok, n_tail = _v6_tail_terminology(text, positions)
        row["v6_tail_ok"] = ok
        row["v6_tail_count"] = n_tail
        if not ok:
            row["notes"].append(
                f"V6 FAIL: tail 30% has {n_tail} terminology source segments "
                f"(need ≥{V6_TAIL_MIN_TERM_SEGMENTS}); P12 tail-recall prep broken"
            )
            result.hard_fail = True
        else:
            row["notes"].append(
                f"V6 PASS: tail 30% has {n_tail} terminology segments (≥{V6_TAIL_MIN_TERM_SEGMENTS})"
            )

    result.add(row)


def write_report(result: Result, stages: list[str], warn_v3: bool, hard_v3: bool) -> Path:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Gemini Gems 单批校验报告",
        "",
        f"> Generated: {_now_iso()}",
        f"> Stages validated: {', '.join(stages)}",
        f"> Total tokens: {result.total_tokens:,} (target ≤{TOTAL_TOKEN_TARGET:,})",
        "",
        "## 校验矩阵",
        "",
        "| file | exists | bytes | tokens | target | segments | V1 | V2 | V4 | V6 | md5 (head12) |",
        "|------|:------:|------:|-------:|-------:|---------:|:--:|:--:|:--:|:--:|--------------|",
    ]

    for row in result.rows:
        v6 = "-" if row["v6_tail_ok"] is None else ("PASS" if row["v6_tail_ok"] else "FAIL")
        lines.append(
            f"| {row['file']} "
            f"| {'Y' if row['exists'] else 'N'} "
            f"| {row['bytes']:,} "
            f"| {row['tokens']:,} "
            f"| {row['target_tokens']:,} "
            f"| {row['source_segments']} "
            f"| {'PASS' if row['v1_nonempty'] else 'FAIL'} "
            f"| {'PASS' if row['v2_segments_ok'] else 'WARN'} "
            f"| {'PASS' if row['v4_under_5mb'] else 'FAIL'} "
            f"| {v6} "
            f"| {row['md5'][:12] if row['md5'] else '-'} |"
        )

    lines += [
        "",
        "## V3 累计 token 判定",
        "",
        f"- Total: **{result.total_tokens:,}** tokens",
        f"- Target (P11): ≤{TOTAL_TOKEN_TARGET:,}",
        f"- Warn threshold (§8 R2): >{TOTAL_TOKEN_WARN:,}",
        f"- Hard threshold (1M 窗口): >{TOTAL_TOKEN_HARD:,}",
        "",
    ]
    if hard_v3:
        lines.append(f"- **V3 FAIL**: total {result.total_tokens:,} > {TOTAL_TOKEN_HARD:,} 硬上限.")
    elif warn_v3:
        lines.append(f"- **V3 WARN (rc=2)**: total {result.total_tokens:,} > {TOTAL_TOKEN_WARN:,} 警告阈值, 触 §8 R2.")
    else:
        lines.append(f"- **V3 PASS**: total {result.total_tokens:,} ≤ target.")

    lines += [
        "",
        "## 备注 (逐文件)",
        "",
    ]
    for row in result.rows:
        if row["notes"]:
            lines.append(f"### {row['file']}")
            for note in row["notes"]:
                lines.append(f"- {note}")
            lines.append("")

    lines += [
        "## 判定",
        "",
    ]
    if result.hard_fail:
        lines.append("- rc=1 (HARD FAIL)")
    elif hard_v3:
        lines.append("- rc=1 (V3 hard threshold)")
    elif warn_v3 or result.warn:
        lines.append("- rc=2 (WARN, non-blocking)")
    else:
        lines.append("- rc=0 (PASS)")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return REPORT_PATH


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Gemini Gems single-batch merge artifacts.",
    )
    parser.add_argument(
        "--stage",
        choices=["core", "spec", "knowledge", "terminology", "all"],
        default="all",
        help="which stage(s) to validate",
    )
    parser.add_argument(
        "--uploads",
        type=Path,
        default=DEFAULT_UPLOADS,
        help=f"uploads dir (default: {DEFAULT_UPLOADS})",
    )
    args = parser.parse_args(argv)

    stages = STAGE_ORDER if args.stage == "all" else [args.stage]
    encoder = tiktoken.get_encoding(ENCODING_NAME)

    result = Result()
    for stage in stages:
        spec = STAGE_FILES[stage]
        path = args.uploads / spec["name"]
        validate_file(stage, path, encoder, result)

    # V3 累计
    hard_v3 = result.total_tokens > TOTAL_TOKEN_HARD
    warn_v3 = (not hard_v3) and (result.total_tokens > TOTAL_TOKEN_WARN)

    report_path = write_report(result, stages, warn_v3=warn_v3, hard_v3=hard_v3)

    # 终端摘要
    print(f"[validate] report: {report_path}")
    print(f"[validate] stages: {stages}")
    print(f"[validate] total tokens: {result.total_tokens:,} (target ≤{TOTAL_TOKEN_TARGET:,})")

    if result.hard_fail or hard_v3:
        print("[validate] rc=1 HARD FAIL")
        return 1
    if warn_v3:
        print("[validate] rc=2 WARN (V3 > 900K, §8 R2 trigger)")
        return 2
    print("[validate] rc=0 PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
