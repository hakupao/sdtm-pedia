#!/usr/bin/env python3
"""SDTM Phase 6.5 Gemini Gems 合并脚本 (v2.0 C 方案).

依据文档:
- PLAN_V2_C.md (2026-04-21) Node 4 C 方案重整: 舍弃 terminology, 04 换业务弹药包
- ai.google.dev/gemini-api/docs/long-context + support.google.com/gemini/answer/14903178:
  全量灌 1M context, 非 RAG; 超窗静默丢失
- SMOKE_QUESTIONS_V2.md (Node 4 重设 10 题 v2, 4 业务维度: 场景/规则/映射/鉴别)
- 用户决策 2026-04-21: 空余容量优化"业务问答", 不为"字典查询"优化

v2.0 (C 方案, 2026-04-21) — 舍弃 terminology, 4 新文件架构:

| # | 文件                                           | 源                                         | est tokens | 备注 |
|---|------------------------------------------------|--------------------------------------------|-----------:|------|
| 01| `01_navigation_and_quick_reference.md`         | ROUTING+INDEX+VARIABLE_INDEX+chapters+model| ~150K      | 导航前置 |
| 02| `02_domains_spec_and_assumptions.md`           | 63 域 spec + assumptions 域内交错          | ~370K      | 业务查变量时规则同屏 |
| 03| `03_domains_examples.md`                       | 63 域 examples                             | ~250K      | 实例独立 |
| 04| `04_business_scenarios_and_cross_domain.md`    | **主 session 手写**                         | ~50K       | **脚本不产**, writer Write |

新 CLI: 仅 `--stage c_refactor` (产 01/02/03). 废 v1.3d 旧 stage name (core/spec/knowledge/terminology).
04 由 Node 4 writer 直接 Write 到 uploads/ (非 KB 源, 脚本不参与).

Usage:
    python3 merge_for_gemini.py --stage c_refactor [--dry-run]

Dependencies: tiktoken (cl100k_base), Python 3 stdlib.

只读 knowledge_base/ (P5), 产物写到 ai_platforms/gemini_gems/current/uploads/.
Idempotent: 重跑同输入 → 同产物 (排序固定, 时间戳除外).

---

v1.x 历史 (保留, 供回溯):

v1.3 修复记录 (2026-04-20, Node 2 attempt_1 V6 HARD FAIL → 混合策略):
  - 原 core>target 分支 break 条件 `cum+t > 200K AND len>=1` 第 2 iter 即满足
    (lb_part3=111.7K + lb_part2=103.5K > 200K, len=1>=1) → 只选 1 个 source.
  - v1.3 改成: top-2 大文件保尾 + prepend 若干高频小文件, 预期 selected 5-8 段.
  - 详见 failures/stage_phase3_attempt_1.md §6 选项 C.

v1.3b 修正 (2026-04-20, 主 session 物理坐标推演捕获 v1.3 实施缺陷):
  - v1.3 选 selected = [small_head..., lb_part2, lb_part3], 但物理 offset
    推演后 lb_part3 marker @ 694K < tail_start 778K, 不在 tail 30% → V6 仍 FAIL.
  - v1.3b 反转 for 循环顺序: [lb_part2, lb_part3, small_head...] → 3 smalls
    markers (intv @ 794K / qs @ 884K / onc @ 1020K) 全落 tail 30% (tail_start ~776K),
    V6 PASS 3/3.

v1.3c 修正 (2026-04-20, reviewer 捕获 selected 仅 3 段): budget/排序修正.
v1.3d 修正 (2026-04-20, reviewer feature-dev 捕获 budget 80K 不足): 80K→90K.

v2.0 迁移说明 (2026-04-21):
  - terminology 整块舍弃 (由 NCI EVS Browser 承担, 见 system_prompt v3)
  - _collect_terminology_sources / _stage_terminology 移除 (v1.x 保留在 git 历史可溯)
  - STAGE_SPEC 的 core/spec/knowledge/terminology 全废除, 新 3 stage 名反映业务含义
  - 04 改由主 session 手写业务弹药包, 脚本不涉及
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path

import tiktoken

# ---------------------------------------------------------------------------
# 路径常量
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent                # ai_platforms/gemini_gems/
REPO_ROOT = PROJECT_ROOT.parent.parent                 # SDTM-compare/
KB_ROOT = REPO_ROOT / "knowledge_base"                 # 源, 只读 (P5)

UPLOADS_DIR = PROJECT_ROOT / "current" / "uploads"     # 产物目录
MANIFEST_PATH = PROJECT_ROOT / "current" / "upload_manifest.md"

ENCODING_NAME = "cl100k_base"

# ---------------------------------------------------------------------------
# v2.0 C 方案合并规划
# ---------------------------------------------------------------------------

# C 方案 3 stage (04 由主 session 手写, 脚本不产)
STAGE_SPEC = {
    "navigation": {
        "out": "01_navigation_and_quick_reference.md",
        "title": "01 Navigation & Quick Reference (Chapters + Model + Indexes)",
        "target_tokens": 150_000,
        "position": "前置 (导航层防 Lost-in-Middle)",
    },
    "spec_plus_assumptions": {
        "out": "02_domains_spec_and_assumptions.md",
        "title": "02 Domains Spec & Assumptions (63 domains, spec+assumptions interleaved)",
        "target_tokens": 370_000,
        "position": "前中段 (业务查 spec 时规则同屏)",
    },
    "examples_only": {
        "out": "03_domains_examples.md",
        "title": "03 Domains Examples (63 domains, implementation examples)",
        "target_tokens": 250_000,
        "position": "中段 (实例数据, 便于专项查)",
    },
}

# c_refactor dispatch: 顺跑 navigation → spec_plus_assumptions → examples_only
STAGE_ORDER = ["navigation", "spec_plus_assumptions", "examples_only"]

# 总 target (v2.0 C 方案 ~820K, 04 ~50K 主 session 手写)
TOTAL_BUDGET_TOKENS = 820_000


# ---------------------------------------------------------------------------
# 辅助函数
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return (
        _dt.datetime.now(_dt.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def _log(msg: str) -> None:
    print(f"[Stage gemini-c-refactor] {msg}")


def _read_text(path: Path) -> str:
    """只读一个 KB 源文件 (P5)."""
    return path.read_text(encoding="utf-8", errors="strict")


def _rel_to_repo(p: Path) -> str:
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def _count_tokens(encoder: "tiktoken.Encoding", text: str) -> int:
    return len(encoder.encode(text))


# ---------------------------------------------------------------------------
# 01: navigation (chapters + model + ROUTING + INDEX + VARIABLE_INDEX)
# ---------------------------------------------------------------------------


def _collect_navigation_sources() -> list[Path]:
    """顺序: chapters (ch01..ch10) → model (01..06) → ROUTING/INDEX/VARIABLE_INDEX.

    v2.0 扩展: VARIABLE_INDEX 入并作为 fallback 防查不到变量 routing 时回退.
    """
    sources: list[Path] = []
    chapters_dir = KB_ROOT / "chapters"
    if chapters_dir.is_dir():
        sources.extend(sorted(chapters_dir.glob("*.md")))
    model_dir = KB_ROOT / "model"
    if model_dir.is_dir():
        sources.extend(sorted(model_dir.glob("*.md")))
    # 导航层 (跟在主体后面, 便于 Gemini 从尾向前扫导航)
    for nav in ("ROUTING.md", "INDEX.md", "VARIABLE_INDEX.md"):
        p = KB_ROOT / nav
        if p.is_file():
            sources.append(p)
    return sources


# ---------------------------------------------------------------------------
# 02: domains spec + assumptions (域内交错)
# ---------------------------------------------------------------------------


def _list_domains() -> list[str]:
    """返回字母升序的 63 域 id 列表."""
    domains_root = KB_ROOT / "domains"
    if not domains_root.is_dir():
        return []
    return sorted(
        d.name for d in domains_root.iterdir() if d.is_dir() and not d.name.startswith(".")
    )


def _collect_spec_and_assumptions_sources() -> list[Path]:
    """每域 spec.md 后紧跟 assumptions.md, 按域字母序.

    某域若 assumptions 缺 skip (63 域并非全有 assumptions).
    业务查 spec 时规则同屏, 减查询跳转 (C 方案核心动机).
    """
    sources: list[Path] = []
    for dom in _list_domains():
        s = KB_ROOT / "domains" / dom / "spec.md"
        a = KB_ROOT / "domains" / dom / "assumptions.md"
        if s.is_file():
            sources.append(s)
        if a.is_file():
            sources.append(a)
    return sources


# ---------------------------------------------------------------------------
# 03: domains examples (独立实例)
# ---------------------------------------------------------------------------


def _collect_examples_only_sources() -> list[Path]:
    """每域 examples.md, 域字母序. 某域若 examples 缺 skip."""
    sources: list[Path] = []
    for dom in _list_domains():
        e = KB_ROOT / "domains" / dom / "examples.md"
        if e.is_file():
            sources.append(e)
    return sources


# ---------------------------------------------------------------------------
# 合并写文件
# ---------------------------------------------------------------------------


def _file_header(title: str, sources: list[Path], total_tokens: int | None = None) -> str:
    lines = [
        f"# {title}",
        "",
        f"> Generated: {_now_iso()}",
        f"> Source files: {len(sources)}",
    ]
    if total_tokens is not None:
        lines.append(f"> Total tokens (cl100k_base): {total_tokens:,}")
    lines += [
        "",
        "> Source order is preserved for traceability. `<!-- source: ... -->` comments "
        "mark each segment's origin file (relative to repo root).",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def _segment(path: Path, text: str) -> str:
    """单段: 源路径注释 + 原文 (末尾 1 空行)."""
    rel = _rel_to_repo(path)
    if not text.endswith("\n"):
        text = text + "\n"
    return f"<!-- source: {rel} -->\n{text}\n"


def _write_merged(
    out_name: str,
    title: str,
    sources: list[Path],
    dry_run: bool,
    encoder: "tiktoken.Encoding",
) -> tuple[Path, int]:
    """合并 sources 到 UPLOADS_DIR/out_name, 返回 (path, tokens)."""
    parts: list[str] = []
    for p in sources:
        parts.append(_segment(p, _read_text(p)))
    body = "".join(parts)
    total_tokens = _count_tokens(encoder, body)

    header = _file_header(title, sources, total_tokens=total_tokens)
    full_text = header + body

    out_path = UPLOADS_DIR / out_name
    if not dry_run:
        UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
        out_path.write_text(full_text, encoding="utf-8")
    # 以完整输出 (含 header) 再算一次作为权威
    final_tokens = _count_tokens(encoder, full_text)
    return out_path, final_tokens


# ---------------------------------------------------------------------------
# Stage executors
# ---------------------------------------------------------------------------


def _stage_navigation(dry_run: bool, encoder) -> tuple[Path, int, int]:
    sources = _collect_navigation_sources()
    info = STAGE_SPEC["navigation"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ~{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


def _stage_spec_plus_assumptions(dry_run: bool, encoder) -> tuple[Path, int, int]:
    sources = _collect_spec_and_assumptions_sources()
    info = STAGE_SPEC["spec_plus_assumptions"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ~{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


def _stage_examples_only(dry_run: bool, encoder) -> tuple[Path, int, int]:
    sources = _collect_examples_only_sources()
    info = STAGE_SPEC["examples_only"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ~{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


STAGE_EXECUTORS = {
    "navigation": _stage_navigation,
    "spec_plus_assumptions": _stage_spec_plus_assumptions,
    "examples_only": _stage_examples_only,
}


# ---------------------------------------------------------------------------
# Manifest 追加
# ---------------------------------------------------------------------------


def _append_manifest_fragment(
    entries: list[tuple[str, int, int, str]],
    dry_run: bool,
) -> None:
    """追加一段到 current/upload_manifest.md.

    entries: [(stage_key, tokens, source_count, out_filename), ...]
    """
    if dry_run:
        return

    timestamp = _now_iso()
    lines = [
        "",
        f"<!-- merge fragment: {timestamp} -->",
        f"## Merge run at {timestamp} (v2.0 c_refactor)",
        "",
        "| 文件 | 源文件数 | tokens | target | 位置策略 |",
        "|------|---------:|-------:|-------:|---------|",
    ]
    for stage_key, tokens, src_n, out_name in entries:
        info = STAGE_SPEC[stage_key]
        lines.append(
            f"| {out_name} | {src_n} | {tokens:,} | "
            f"~{info['target_tokens']:,} | {info['position']} |"
        )
    lines.append("")

    header_needed = not MANIFEST_PATH.exists()
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    if header_needed:
        initial = [
            "# Gemini Gems Upload Manifest",
            "",
            "> 由 `dev/scripts/merge_for_gemini.py` 自动追加. v2.0 C 方案.",
            "",
        ]
        MANIFEST_PATH.write_text("\n".join(initial), encoding="utf-8")
    with MANIFEST_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="SDTM Phase 6.5 Gemini Gems v2.0 c_refactor merge.",
    )
    parser.add_argument(
        "--stage",
        required=True,
        choices=["c_refactor"],
        help="v2.0 仅支持 c_refactor: 顺跑 navigation + spec_plus_assumptions + examples_only",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="plan only, do not write files",
    )
    args = parser.parse_args(argv)

    encoder = tiktoken.get_encoding(ENCODING_NAME)

    # c_refactor = STAGE_ORDER (3 stage 顺跑)
    stages = STAGE_ORDER
    if args.dry_run:
        _log(f"DRY RUN stages={stages} — no files will be written.")

    entries: list[tuple[str, int, int, str]] = []
    cumulative = 0
    for stage in stages:
        out, tokens, src_n = STAGE_EXECUTORS[stage](args.dry_run, encoder)
        cumulative += tokens
        entries.append((stage, tokens, src_n, STAGE_SPEC[stage]["out"]))

    _log(
        f"cumulative tokens for 3 stages: {cumulative:,} "
        f"(target ~{TOTAL_BUDGET_TOKENS:,}, 04 ~50K writer-authored, totals ~820K C 方案)"
    )
    if cumulative > 900_000:
        _log(
            f"WARN: cumulative {cumulative:,} > 900K WARN 阈 "
            "— C 方案预算可能被超, 检查 02/03 token 膨胀."
        )
    elif cumulative > TOTAL_BUDGET_TOKENS:
        _log(
            f"NOTE: cumulative {cumulative:,} > {TOTAL_BUDGET_TOKENS:,} target "
            "but < 900K WARN 阈 (acceptable, 04 ~50K 加后仍 < 900K)."
        )

    _append_manifest_fragment(entries, args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
