#!/usr/bin/env python3
"""SDTM Phase 6.5 Gemini Gems 产物校验脚本 (v2.0 C 方案).

依据文档:
- PLAN_V2_C.md (2026-04-21) Node 4 C 方案: 舍弃 terminology, 04 业务弹药包
- PLAN.md §4 Phase B6 (validate_gemini.py 产物完整性校验)
- PLAN.md §1.3 P11 (总 ≤900K WARN, 1M 窗口硬上限)
- SMOKE_QUESTIONS_V2.md (Node 4 10 题业务视角)

依据 Phase 1 research:
- Q2: 10 文件硬限 / 100 MB per file (本校验 <5MB 远低于硬限, 防御性)
- Q1: 1M 窗口 + 多针降级 ⇒ total ≤900K 留响应余量

Usage:
    python3 validate_gemini.py [--stage {navigation|spec_plus_assumptions|examples_only|business_scenarios|all}] [--uploads DIR]

校验项:
- V1 非空: 每文件 size > 0
- V2 段数对齐: `<!-- source: ... -->` 段数 ≥ PLAN §2.1 预期 (business_scenarios 无 KB 源不判)
- V3 token 上限: 单文件 + 累计 ≤820K target; >900K WARN (rc=2); >1000K FAIL
- V4 单文件 <5MB: 字节大小防御 (Gemini 100MB 上限远高)
- V5 md5 稳定: 输出 md5 供对比
- V8 新增 (04 弹药包合规):
    - V8a: 04 字节 > 10000 (非 stub, 保 ~50KB 业务内容)
    - V8b: 04 不含 codelist 字面值表 (防意外 inline terminology)
      扫行 pattern `r"^\s*\|\s*C\d{5,7}\s*\|\s*\w+"` 若命中 ≥5 行触 FAIL
- V6 废除 (v2.0, 无 terminology 尾部 gate): 删 _v6_tail_terminology + V6_* 常量

Return codes:
- rc=0: 全 PASS
- rc=1: V1/V4/V5/V8 任一 FAIL 或 V3 硬超
- rc=2: V3 WARN (>900K 未超 1M) 或 V2 WARN

产出: dev/evidence/validate_single_batch.md (md 表格).

Dependencies: tiktoken (cl100k_base), Python 3 stdlib.
Read-only over uploads/ + 源 (P5).

v2.0 迁移说明:
  - 旧 STAGE_FILES core/spec/knowledge/terminology 整体废除 (v1.x 在 git 历史)
  - 新 STAGE_FILES: navigation / spec_plus_assumptions / examples_only / business_scenarios
  - V6 terminology 尾部 gate 删除 (C 方案无 terminology)
  - V8 新增 (04 业务弹药包合规): 非 stub + 无 inline codelist
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

# v2.0 C 方案 4 文件
STAGE_FILES = {
    "navigation": {
        "name": "01_navigation_and_quick_reference.md",
        "expected_sources_min": 15,        # 6 chapters + 6 model + 3 nav ≈ 15
        "target_tokens": 150_000,
    },
    "spec_plus_assumptions": {
        "name": "02_domains_spec_and_assumptions.md",
        "expected_sources_min": 120,       # 63 spec + ≤63 assumptions (可能有缺)
        "target_tokens": 400_000,
    },
    "examples_only": {
        "name": "03_domains_examples.md",
        "expected_sources_min": 60,        # 63 examples 有几个可能缺
        "target_tokens": 280_000,
    },
    "business_scenarios": {
        "name": "04_business_scenarios_and_cross_domain.md",
        "expected_sources_min": 0,         # 自编无 KB 源
        "target_tokens": 60_000,
    },
}
STAGE_ORDER = ["navigation", "spec_plus_assumptions", "examples_only", "business_scenarios"]

# 阈值
SINGLE_FILE_BYTE_HARD = 5 * 1024 * 1024    # 5MB 防御上限
TOTAL_TOKEN_TARGET = 820_000               # C 方案 ~820K target
TOTAL_TOKEN_WARN = 900_000                 # WARN 阈
TOTAL_TOKEN_HARD = 1_000_000               # 1M 硬上限

# V8 常量 (04 弹药包合规)
V8_MIN_BYTES = 10_000                          # 04 字节下限, 防 stub
V8_CODELIST_LINE_RE = re.compile(
    r"^\s*\|\s*C\d{5,7}\s*\|\s*\w+",
    re.MULTILINE,
)
V8_CODELIST_LINE_HARD_MAX = 5                  # ≥5 命中 FAIL

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


def _v8_business_scenarios(path: Path, text: str) -> tuple[bool, list[str]]:
    """V8: 04 弹药包合规.

    V8a: size > V8_MIN_BYTES (非 stub)
    V8b: 不含 codelist 字面值表 (pattern: `| Cxxxxx | word`) ≥5 行 FAIL

    返回 (pass, [notes]).
    """
    notes: list[str] = []
    ok = True

    size = path.stat().st_size
    if size <= V8_MIN_BYTES:
        ok = False
        notes.append(f"V8a FAIL: size {size} ≤ {V8_MIN_BYTES} (stub or too thin)")
    else:
        notes.append(f"V8a PASS: size {size:,} > {V8_MIN_BYTES:,}")

    codelist_hits = V8_CODELIST_LINE_RE.findall(text)
    hit_count = len(codelist_hits)
    if hit_count >= V8_CODELIST_LINE_HARD_MAX:
        ok = False
        notes.append(
            f"V8b FAIL: inline codelist lines matched {hit_count} "
            f"(≥{V8_CODELIST_LINE_HARD_MAX}); 04 应仅列 CT Code + 英文名, 不给 Term 值"
        )
    else:
        notes.append(
            f"V8b PASS: inline codelist lines matched {hit_count} "
            f"(<{V8_CODELIST_LINE_HARD_MAX})"
        )

    return ok, notes


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
        "v8_ok": None,            # 仅 business_scenarios 判定
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
    seg_count, _positions = _count_source_marks(text)
    row["source_segments"] = seg_count
    min_expected = spec["expected_sources_min"]
    if min_expected > 0:
        row["v2_segments_ok"] = seg_count >= min_expected
        if not row["v2_segments_ok"]:
            row["notes"].append(
                f"V2 WARN: segments {seg_count} < expected {min_expected}"
            )
            result.warn = True
    else:
        # business_scenarios: 记录不判 (自编无 KB 源)
        row["v2_segments_ok"] = True
        row["notes"].append(
            f"V2 INFO: {seg_count} segments (writer-authored, no KB source required)"
        )

    # V8 仅对 business_scenarios 判 (04 弹药包合规)
    if stage_key == "business_scenarios":
        ok, v8_notes = _v8_business_scenarios(path, text)
        row["v8_ok"] = ok
        row["notes"].extend(v8_notes)
        if not ok:
            result.hard_fail = True

    result.add(row)


def write_report(result: Result, stages: list[str], warn_v3: bool, hard_v3: bool) -> Path:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Gemini Gems v2.0 C 方案校验报告",
        "",
        f"> Generated: {_now_iso()}",
        f"> Stages validated: {', '.join(stages)}",
        f"> Total tokens: {result.total_tokens:,} (target ~{TOTAL_TOKEN_TARGET:,})",
        "",
        "## 校验矩阵",
        "",
        "| file | exists | bytes | tokens | target | segments | V1 | V2 | V4 | V8 | md5 (head12) |",
        "|------|:------:|------:|-------:|-------:|---------:|:--:|:--:|:--:|:--:|--------------|",
    ]

    for row in result.rows:
        v8 = "-" if row["v8_ok"] is None else ("PASS" if row["v8_ok"] else "FAIL")
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
            f"| {v8} "
            f"| {row['md5'][:12] if row['md5'] else '-'} |"
        )

    lines += [
        "",
        "## V3 累计 token 判定",
        "",
        f"- Total: **{result.total_tokens:,}** tokens",
        f"- Target (C 方案): ~{TOTAL_TOKEN_TARGET:,}",
        f"- Warn threshold: >{TOTAL_TOKEN_WARN:,}",
        f"- Hard threshold (1M 窗口): >{TOTAL_TOKEN_HARD:,}",
        "",
    ]
    if hard_v3:
        lines.append(f"- **V3 FAIL**: total {result.total_tokens:,} > {TOTAL_TOKEN_HARD:,} 硬上限.")
    elif warn_v3:
        lines.append(f"- **V3 WARN (rc=2)**: total {result.total_tokens:,} > {TOTAL_TOKEN_WARN:,} 警告阈.")
    else:
        lines.append(f"- **V3 PASS**: total {result.total_tokens:,} ≤ warn 阈.")

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
        description="Validate Gemini Gems v2.0 C refactor artifacts.",
    )
    parser.add_argument(
        "--stage",
        choices=["navigation", "spec_plus_assumptions", "examples_only", "business_scenarios", "all"],
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
    print(f"[validate] total tokens: {result.total_tokens:,} (target ~{TOTAL_TOKEN_TARGET:,})")

    if result.hard_fail or hard_v3:
        print("[validate] rc=1 HARD FAIL")
        return 1
    if warn_v3:
        print("[validate] rc=2 WARN (V3 > 900K)")
        return 2
    if result.warn:
        print("[validate] rc=2 WARN (V2 segments below expected)")
        return 2
    print("[validate] rc=0 PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
