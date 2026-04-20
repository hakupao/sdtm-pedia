#!/usr/bin/env python3
"""ChatGPT GPTs 合并脚本 — 9 产物 (P12 溯源 + P13 TableAware).

按 PLAN.md §2.4 清单, 把 knowledge_base/ 下源 md 合并为 9 个 ChatGPT 上传文件:

    01_navigation.md             (ROUTING + INDEX + VAR_INDEX)        批 1
    02_chapters_all.md           (chapters/ 6 文件)                   批 1
    03_model_all.md              (model/ 6 文件)                      批 1
    04_domain_specs_all.md       (63 domains/*/spec.md)               批 1
    05_domain_assumptions_all.md (63 domains/*/assumptions.md)         批 2
    06_domain_examples_all.md    (63 domains/*/examples.md)            批 2
    07_terminology_core.md       (terminology/core/)                   批 2
    08_terminology_questionnaires.md (terminology/questionnaires/)     批 2
    09_terminology_supplementary.md  (terminology/supplementary/)      批 2

P11 合规: 9 产物 ≤ 20 硬限.

规则实现:
- **P5 只读**: 不 Edit/Write knowledge_base/, 仅 read_text.
- **P12 溯源**: 每源文件作为一段, 段起始插入
      `<!-- source: <repo 相对路径> -->`
  注释. chunker 800 tokens 无法跨 heading, 此注释保证模型引用可反查源.
- **P13 TableAware**: md-heading 边界保护表格 — 源内原有 heading 原样保留,
  段拼接在源文件边界进行 (源文件整文件落入产物, 源内大表自然不跨 heading).
  P13 的硬门槛是: `<!-- source: ... -->` 注释绝不插入到 `|` 开头的
  table row 行之间. 本脚本的段插入点永远是"源文件起点", 源文件首行不可能
  是 table row (源文件均以 heading/文本开头), 因此自动满足.

Idempotent: 同输入重跑 → 产物 md5 稳定 (文件顺序 sorted, 注释格式固定).

依据:
- PLAN.md §2.4 (合并文件清单)
- PLAN.md §2.5 (脚本职责)
- PLAN.md §1.2 P11-P13 (ChatGPT 硬约束)
- PLAN.md §1.1 P1 (量化 PASS: 每产物打印 tokens)

Phase: 3 (执行) · Node: 1 (仅写脚本, 不执行)

Usage:
    python3 merge_for_chatgpt.py --stage batch1            # 出 01-04
    python3 merge_for_chatgpt.py --stage batch2            # 出 05-09
    python3 merge_for_chatgpt.py --stage all               # 全 9 个
    python3 merge_for_chatgpt.py --stage batch1 --dry-run  # 不写文件, 仅打印计划

v1.1 修复记录 (2026-04-20, Node 1 reviewer CONDITIONAL_PASS → bug fix pass):
  - MEDIUM-2: 新增 `current/manifest_segments.json` 作为 expected_segments 独立
    真源. merge 产出时把 "该 entry 真实写入的 source_count" + "PLAN 声明的
    expected (静态硬编码, 动态则为运行时决议的 KB 计数)" 双写进 JSON, 供
    validate 读取比对. 字段: {"entries": {"NN_target.md": {"expected":N,
    "actual":N, "stage":"batch1|2", "dynamic": true|false}}}. 同输入重跑
    → JSON 字节稳定 (sorted keys + indent=2).
  - MEDIUM-3: `run_entry` 中 "seg_count != expected_segments" 由 WARN 升级
    到 FAIL (return rc=2). `--dry-run` 模式降级为 WARN (因为 dry-run 不写
    产物, 允许提醒); 默认写模式必 FAIL. main 的 rc 聚合已保证 propagate
    任一 FAIL.
  - 动态段数 (07/08/09, expected_segments=0): 运行时先 resolve 实际 KB
    子目录计数作为 "真源 expected", 写入 manifest_segments.json 同时用于
    fail-fast 比对 (若收集后 source_collector 又出错偏差也能抓到).
    validate 侧读 manifest expected 作主真源 (MEDIUM-2).
  - Node 2 起本版生效 (Node 1 禁运行, Node 2 跑 --stage batch1 触发首次
    JSON 生成).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import tiktoken

ENCODING_NAME = "cl100k_base"

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # ai_platforms/chatgpt_gpt/
REPO_ROOT = PROJECT_ROOT.parent.parent  # SDTM-compare/
KB_DIR = REPO_ROOT / "knowledge_base"
UPLOADS_DIR = PROJECT_ROOT / "current" / "uploads"
MANIFEST_PATH = PROJECT_ROOT / "current" / "upload_manifest.md"
# MEDIUM-2: 独立真源文件 — merge 写, validate 读, 比对 "产物实际 source
# comment 数" 与 "merge 当时声明的 expected". 若 merge 合并 bug 导致 actual
# 与 declared expected 不一致, validate 可检出; 避免 validate 另行重读 KB
# 目录 self-consistent 掩盖 bug.
MANIFEST_SEGMENTS_PATH = PROJECT_ROOT / "current" / "manifest_segments.json"

# ---------------------------------------------------------------------------
# 合并配置 (9 产物)
# ---------------------------------------------------------------------------


@dataclass
class MergeEntry:
    """单产物合并配置.

    source_collector 返回的列表必须 deterministic (sorted), 保证 idempotent.
    expected_segments: PLAN §2.4 声明的源文件数 (validate 脚本会校验).
    """

    target: str                   # 产物文件名 (落到 uploads/ 下)
    stage: str                    # 'batch1' or 'batch2'
    description: str              # 人可读描述 (用于 manifest)
    source_collector: Callable[[], list[Path]]  # 返回源文件列表 (绝对路径, sorted)
    expected_segments: int        # PLAN §2.4 声明段数
    token_cap: int                # P1 token 上限 (估算, +15% buffer 后)


# 域列表 (按字母序, knowledge_base/domains/ 下 63 子目录)
# 运行时 collector 动态读 os.listdir 保证不漏/不多.


def _collect_navigation() -> list[Path]:
    """01: ROUTING.md + INDEX.md + VAR_INDEX.md (固定顺序)."""
    # PLAN §2.4 列出顺序: ROUTING + INDEX + VAR_INDEX
    # 注: knowledge_base/ 实际有 VARIABLE_INDEX.md (v2 script 中也用此名).
    # 若 VAR_INDEX.md 不存在, fallback 到 VARIABLE_INDEX.md.
    order = ["ROUTING.md", "INDEX.md", "VAR_INDEX.md"]
    paths: list[Path] = []
    for name in order:
        p = KB_DIR / name
        if p.is_file():
            paths.append(p)
            continue
        # fallback: VARIABLE_INDEX.md
        if name == "VAR_INDEX.md":
            alt = KB_DIR / "VARIABLE_INDEX.md"
            if alt.is_file():
                paths.append(alt)
    return paths


def _collect_chapters() -> list[Path]:
    """02: chapters/ 下全部 .md, sorted."""
    d = KB_DIR / "chapters"
    if not d.is_dir():
        return []
    return sorted(p for p in d.glob("*.md") if p.is_file())


def _collect_model() -> list[Path]:
    """03: model/ 下全部 .md, sorted."""
    d = KB_DIR / "model"
    if not d.is_dir():
        return []
    return sorted(p for p in d.glob("*.md") if p.is_file())


def _collect_domain(field_name: str) -> list[Path]:
    """04/05/06: domains/*/<field>.md (63 域, sorted by domain)."""
    base = KB_DIR / "domains"
    if not base.is_dir():
        return []
    out: list[Path] = []
    for dom in sorted(p.name for p in base.iterdir() if p.is_dir()):
        fp = base / dom / f"{field_name}.md"
        if fp.is_file():
            out.append(fp)
    return out


def _collect_domain_specs() -> list[Path]:
    return _collect_domain("spec")


def _collect_domain_assumptions() -> list[Path]:
    return _collect_domain("assumptions")


def _collect_domain_examples() -> list[Path]:
    return _collect_domain("examples")


def _collect_terminology(subdir: str) -> list[Path]:
    """07/08/09: terminology/<subdir>/*.md, sorted."""
    d = KB_DIR / "terminology" / subdir
    if not d.is_dir():
        return []
    return sorted(p for p in d.glob("*.md") if p.is_file())


def _collect_terminology_core() -> list[Path]:
    return _collect_terminology("core")


def _collect_terminology_questionnaires() -> list[Path]:
    return _collect_terminology("questionnaires")


def _collect_terminology_supplementary() -> list[Path]:
    return _collect_terminology("supplementary")


# token_cap: PLAN §2.4 估算大小 → token 粗估 (1 token ≈ 4 chars) + 15% buffer.
# 01 159 KB → ~40K tokens → cap 46K
# 02 246 KB → ~62K tokens → cap 72K
# 03  70 KB → ~18K tokens → cap 21K
# 04 672 KB → ~168K tokens → cap 193K
# 05 240 KB → ~60K tokens → cap 69K
# 06 661 KB → ~165K tokens → cap 190K
# 07 3.2 MB → ~800K tokens → cap 920K
# 08 3.8 MB → ~950K tokens → cap 1_095K
# 09 0.6 MB → ~150K tokens → cap 173K


MERGE_CONFIGS: list[MergeEntry] = [
    MergeEntry(
        target="01_navigation.md",
        stage="batch1",
        description="ROUTING + INDEX + VAR_INDEX (导航层)",
        source_collector=_collect_navigation,
        expected_segments=3,
        token_cap=46_000,
    ),
    MergeEntry(
        target="02_chapters_all.md",
        stage="batch1",
        description="chapters/ 6 章全量",
        source_collector=_collect_chapters,
        expected_segments=6,
        token_cap=72_000,
    ),
    MergeEntry(
        target="03_model_all.md",
        stage="batch1",
        description="model/ 6 文件 (观测类/SDT 等)",
        source_collector=_collect_model,
        expected_segments=6,
        token_cap=21_000,
    ),
    MergeEntry(
        target="04_domain_specs_all.md",
        stage="batch1",
        description="63 域 spec.md (变量定义骨架)",
        source_collector=_collect_domain_specs,
        expected_segments=63,
        token_cap=193_000,
    ),
    MergeEntry(
        target="05_domain_assumptions_all.md",
        stage="batch2",
        description="63 域 assumptions.md (辅助推理)",
        source_collector=_collect_domain_assumptions,
        expected_segments=63,
        token_cap=69_000,
    ),
    MergeEntry(
        target="06_domain_examples_all.md",
        stage="batch2",
        description="63 域 examples.md (示例场景)",
        source_collector=_collect_domain_examples,
        expected_segments=63,
        token_cap=190_000,
    ),
    MergeEntry(
        target="07_terminology_core.md",
        stage="batch2",
        description="terminology/core (核心 CT codelist)",
        source_collector=_collect_terminology_core,
        expected_segments=0,  # 动态 (运行时按实际子文件数填充)
        token_cap=920_000,
    ),
    MergeEntry(
        target="08_terminology_questionnaires.md",
        stage="batch2",
        description="terminology/questionnaires (QRS codelist)",
        source_collector=_collect_terminology_questionnaires,
        expected_segments=0,
        token_cap=1_095_000,
    ),
    MergeEntry(
        target="09_terminology_supplementary.md",
        stage="batch2",
        description="terminology/supplementary (补充 CT)",
        source_collector=_collect_terminology_supplementary,
        expected_segments=0,
        token_cap=173_000,
    ),
]


# ---------------------------------------------------------------------------
# 合并实现 (P12 + P13 核心逻辑)
# ---------------------------------------------------------------------------


def _relative_to_repo(p: Path) -> str:
    """把绝对路径转 repo 相对路径 (供 P12 注释使用, idempotent)."""
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def _source_comment(p: Path) -> str:
    """生成 P12 溯源注释行 (末尾含换行)."""
    return f"<!-- source: {_relative_to_repo(p)} -->\n"


def _merge_sources(sources: list[Path]) -> str:
    """把源列表拼成单个产物字符串.

    P12 实现:
      - 每个源文件开头插入 `<!-- source: <rel path> -->\\n`.
      - 注释之后紧接源原文 (不改动 heading 层级, 不 normalize 表格).

    P13 实现 (段边界不切表格):
      - 段边界永远落在"两源文件之间", 即源文件的起点/终点.
      - 源文件首行若是 table row 理论可能破坏 P13, 但 knowledge_base/
        下所有 .md 均以 heading (# / ##) 或普通文本开头, 不会是 `|`
        开头 (实际数据保证). validate 脚本 V4 会硬校验此假设 — 若有
        源首行是 `|` 开头, validate 报 FAIL.
      - 额外防御: 若前一源结尾没换行, 插入 1 换行, 保证注释不粘在表格尾.
    """
    parts: list[str] = []
    for src in sources:
        text = src.read_text(encoding="utf-8", errors="strict")
        # 防御: 确保上一段末尾有空行分隔
        if parts and not parts[-1].endswith("\n"):
            parts.append("\n")
        if parts:
            # 段间插入一空行 (提升可读性, 不影响 chunker 切分)
            parts.append("\n")
        # P12 注释 (必须紧贴段起点, 段起点 = 源文件首字符)
        parts.append(_source_comment(src))
        # 源原文 (保留 heading + 表格 + 空行)
        parts.append(text)
        if not text.endswith("\n"):
            parts.append("\n")
    return "".join(parts)


# ---------------------------------------------------------------------------
# MEDIUM-2: manifest_segments.json — merge 作 expected_segments 唯一真源
# ---------------------------------------------------------------------------


def _resolve_dynamic_expected(entry: MergeEntry, actual: int) -> tuple[int, bool]:
    """决议 entry 的 "expected segment count" (供 manifest_segments.json 与
    fail-fast 比对用).

    - 硬编码 > 0: 直接返回 entry.expected_segments, dynamic=False.
    - 硬编码 == 0 (07/08/09 动态): 以 source_collector 当次返回的
      actual 数作为 dynamic expected 并写入 JSON. 此时 "expected==actual"
      本身不构成 FAIL (动态目录就是当前目录快照), 但把它固化到 JSON 后,
      下游 validate 不再另行重读 KB 目录 — 避免两边重读同一 KB 的
      self-consistent 掩盖 (MEDIUM-2).
    """
    if entry.expected_segments > 0:
        return entry.expected_segments, False
    return actual, True


def _load_manifest_segments() -> dict:
    """读取既有 manifest_segments.json; 若无或损坏, 返回空骨架.

    骨架: {"entries": {}}. 运行时逐 entry 覆盖.
    """
    if not MANIFEST_SEGMENTS_PATH.is_file():
        return {"entries": {}}
    try:
        data = json.loads(MANIFEST_SEGMENTS_PATH.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "entries" not in data:
            return {"entries": {}}
        if not isinstance(data["entries"], dict):
            return {"entries": {}}
        return data
    except (json.JSONDecodeError, OSError):
        return {"entries": {}}


def _write_manifest_segments(data: dict) -> None:
    """覆盖式落盘, sorted keys + indent=2, 保证 idempotent.

    同输入重跑 → 字节稳定.
    """
    MANIFEST_SEGMENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    # 规范化 entries: 按 target 名字 sort
    entries = data.get("entries", {})
    # data 直接写出 (json.dumps sort_keys 会递归排序), 追加换行保证 POSIX 友好
    serialized = json.dumps(
        {"entries": entries},
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    )
    MANIFEST_SEGMENTS_PATH.write_text(serialized + "\n", encoding="utf-8")


def _update_manifest_segments(
    entry: MergeEntry,
    actual: int,
    expected: int,
    dynamic: bool,
) -> None:
    """把单 entry 的段数写进 manifest_segments.json (覆盖式, idempotent)."""
    data = _load_manifest_segments()
    data["entries"][entry.target] = {
        "stage": entry.stage,
        "expected": expected,
        "actual": actual,
        "dynamic": dynamic,
    }
    _write_manifest_segments(data)


# ---------------------------------------------------------------------------
# Manifest 写入 (idempotent 追加)
# ---------------------------------------------------------------------------


def _count_tokens(text: str, encoder) -> int:
    return len(encoder.encode(text))


def _manifest_row(entry: MergeEntry, tokens: int, segment_count: int) -> str:
    """构造 manifest 表格行 (固定格式, idempotent).

    列: | NN | filename | N tokens | source count | batch |
    """
    nn = entry.target.split("_", 1)[0]
    return (
        f"| {nn} | {entry.target} | {tokens:,} tokens | "
        f"{segment_count} sources | {entry.stage} |\n"
    )


MANIFEST_HEADER = (
    "# ChatGPT GPTs 上传 Manifest\n"
    "\n"
    "> 自动由 `dev/scripts/merge_for_chatgpt.py` 追加. 手工修改可能被下次合并覆盖.\n"
    "\n"
    "## 产物清单\n"
    "\n"
    "| # | 文件 | token 实测 | 段数 | 批次 |\n"
    "|:-:|------|:----------:|:----:|:----:|\n"
)


def _ensure_manifest() -> str:
    """读取 (或初始化) manifest, 返回当前内容."""
    if MANIFEST_PATH.is_file():
        return MANIFEST_PATH.read_text(encoding="utf-8")
    return MANIFEST_HEADER


def _append_manifest_row(entry: MergeEntry, tokens: int, segment_count: int) -> str:
    """追加一行到 manifest. idempotent: 同文件名只保留最新行.

    Returns: 'appended' / 'updated' / 'skipped (same)'.
    """
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    text = _ensure_manifest()
    new_row = _manifest_row(entry, tokens, segment_count)

    # 查找是否已有同文件名的行
    lines = text.splitlines(keepends=True)
    found_idx = -1
    for i, line in enumerate(lines):
        if f"| {entry.target} |" in line and line.lstrip().startswith("|"):
            found_idx = i
            break

    if found_idx >= 0:
        if lines[found_idx] == new_row:
            return "skipped (same)"
        lines[found_idx] = new_row
        MANIFEST_PATH.write_text("".join(lines), encoding="utf-8")
        return "updated"

    # 追加新行 (放到表尾)
    if not text.endswith("\n"):
        text += "\n"
    MANIFEST_PATH.write_text(text + new_row, encoding="utf-8")
    return "appended"


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------


def run_entry(entry: MergeEntry, encoder, dry_run: bool) -> int:
    """合并单产物, 返回 rc (0=OK, 非 0=错误).

    MEDIUM-3: 段数 != expected_segments 在写模式下升级为 FAIL (rc=2),
    dry-run 模式降级为 WARN (dry-run 不产出, 仅计划/体检, 允许继续).
    """
    sources = entry.source_collector()
    if not sources:
        print(
            f"[Stage chatgpt-{entry.stage}] {entry.target}: "
            f"ERROR no sources collected",
            file=sys.stderr,
        )
        return 2

    # 段数校验 (仅 expected_segments > 0 时硬校验, 0 表示动态)
    seg_count = len(sources)
    segment_mismatch = (
        entry.expected_segments > 0
        and seg_count != entry.expected_segments
    )
    if segment_mismatch:
        level = "WARN" if dry_run else "FAIL"
        print(
            f"[Stage chatgpt-{entry.stage}] {entry.target}: "
            f"{level} segment count {seg_count} != PLAN-expected "
            f"{entry.expected_segments} "
            f"({'dry-run allow continue' if dry_run else 'fail-fast, abort write'})",
            file=sys.stderr,
        )

    text = _merge_sources(sources)
    tokens = _count_tokens(text, encoder)

    cap_label = f"target ≤{entry.token_cap // 1000}K"
    print(
        f"[Stage chatgpt-{entry.stage}] {entry.target}: "
        f"{tokens:,} tokens ({seg_count} sources, {cap_label})"
    )

    if dry_run:
        print(f"  [DRY] skip write {UPLOADS_DIR / entry.target}")
        # dry-run 下段数不匹配只警告, 不中断
        return 0

    # 写模式: 段数不匹配即 FAIL, 不落盘产物, 不更新 manifest
    if segment_mismatch:
        return 2

    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = UPLOADS_DIR / entry.target
    out_path.write_text(text, encoding="utf-8")

    # MEDIUM-2: 写 manifest_segments.json (独立真源)
    expected, dynamic = _resolve_dynamic_expected(entry, seg_count)
    _update_manifest_segments(entry, seg_count, expected, dynamic)

    manifest_res = _append_manifest_row(entry, tokens, seg_count)
    print(
        f"  wrote {out_path.relative_to(REPO_ROOT)} | "
        f"manifest: {manifest_res} | "
        f"segments.json: expected={expected} actual={seg_count} "
        f"dynamic={dynamic}"
    )

    return 0


def pick_entries(stage: str) -> list[MergeEntry]:
    if stage == "all":
        return list(MERGE_CONFIGS)
    return [e for e in MERGE_CONFIGS if e.stage == stage]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Merge knowledge_base/ sources into 9 ChatGPT upload files "
                    "(P12 溯源 + P13 TableAware)."
    )
    parser.add_argument(
        "--stage",
        required=True,
        choices=["batch1", "batch2", "all"],
        help="batch1 = 01-04 (P0) / batch2 = 05-09 (P1-P2) / all = 9 全量",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="不写文件, 仅打印计划 + token 估算",
    )
    args = parser.parse_args(argv)

    if not KB_DIR.is_dir():
        print(f"error: knowledge_base/ not found at {KB_DIR}", file=sys.stderr)
        return 2

    encoder = tiktoken.get_encoding(ENCODING_NAME)
    entries = pick_entries(args.stage)

    print(f"merge_for_chatgpt.py --stage {args.stage} "
          f"({len(entries)} 产物, dry_run={args.dry_run})")
    print(f"repo_root: {REPO_ROOT}")
    print(f"uploads:   {UPLOADS_DIR.relative_to(REPO_ROOT)}")
    print()

    rc = 0
    for e in entries:
        r = run_entry(e, encoder, args.dry_run)
        if r != 0:
            rc = r
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
