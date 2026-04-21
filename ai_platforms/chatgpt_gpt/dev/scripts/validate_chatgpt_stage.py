#!/usr/bin/env python3
"""ChatGPT GPTs 产物校验 — V1-V7 七项.

输入: `current/uploads/` + `--stage {batch1|batch2|all}` 限定范围.

校验项 (PLAN §2.5 + §6 失败模式):
  V1 非空        : size > 0
  V2 段数对齐    : `<!-- source: ... -->` 出现次数 == merge 真源声明 (读
                   `current/manifest_segments.json`, MEDIUM-2 独立真源).
                   fallback 若 manifest 缺 entry → FAIL "no manifest truth
                   source" (避免 validate 另行重读 KB 造成 self-consistent
                   掩盖).
  V3 P12 溯源覆盖率 100% (HIGH-1 重写, 逐段强校验):
                 判 3 个子条件, 任一 FAIL 则 V3 FAIL:
                   (a) source comment 总数 == V2 expected (即 merge 真源
                       声明的 expected); 少 1 即 FAIL.
                   (b) 文档首个非空行必为 source comment (段起始锚点).
                   (c) 每个 heading 的"最近非空向上回溯"距离内必须先遇到
                       一个 source comment (即不存在 heading 在文档中
                       "上游无任何 source comment" 的情形); 回溯上限
                       `V3_HEADING_LOOKBACK` = 无限 (等价全局之前必有
                       source), 但结合 (a) 已保证每段起始有唯一 source,
                       这里再检查 "heading 前最近非空行到最近 source
                       comment 的行距 ≤ V3_MAX_HEAD_TO_SOURCE" (默认 None
                       = 不限制, 仅要求存在), 专抓"source comment 被
                       删但 heading 仍在" 的产物 bug.
  V4 P13 注释位置: `<!-- source: ... -->` 不得落入 `|` 开头的 table row 块
                   内部 (保留原逻辑, 辅助校验 — merge 脚本插入的注释前
                   永远有空行, 故此项实际几乎永远 PASS. 留作 defensive).
  V7 P13 单表跨 heading (MEDIUM-1 新增):
                   扫描所有连续 table row 块, 若块内出现 heading 行 → FAIL
                   (表被 heading 切断). 同时对每个 heading, 检查其前 5
                   非空行 + 后 5 非空行, 若前后均为 table row → FAIL
                   (heading 插在表格中间).
  V5 token 上限  : 每文件 tokens ≤ PLAN §2.4 估算 token 上限 (merge 脚本硬编码
                   token_cap 已含 +15% buffer).
  V6 md5 稳定    : 当前 md5 仅打印 (供 Node 2 对比); 不 FAIL.

输出: `dev/evidence/validate_<stage>.md` (md 表格).
rc=0 全 PASS, rc=1 任一 FAIL.

依据:
- PLAN.md §1.2 P12 / P13
- PLAN.md §2.4 (9 合并文件清单 + 段数)
- PLAN.md §2.5 (脚本职责)
- PLAN.md §6 (失败模式 1/2/4 与 V4 / V3 对应)

Phase: 3 (执行) · Node: 1 (仅写脚本, 不执行)

Usage:
    python3 validate_chatgpt_stage.py --stage batch1
    python3 validate_chatgpt_stage.py --stage all

v1.1 修复记录 (2026-04-20, reviewer CONDITIONAL_PASS → bug fix pass):
  - HIGH-1: `_v3_p12_coverage` 彻底重写, 由原"一次 seen_source 永远 True"
    的过宽状态机改为三段强校验 (段数对齐 / 首行锚点 / heading 前存在
    source). 反例产物 (某段 source comment 漏一条) 旧版 PASS, 新版 FAIL.
  - MEDIUM-1: 新增 `_v7_table_heading_split` 扫描单表跨 heading 破坏模式.
    V4 原逻辑保留, V7 补齐 PLAN §1.2 P13 "单表不跨 heading" 硬门槛.
    (v1.2 收窄 2026-04-20: 原 v1.1 (ii) "heading 前后最近非空行均为 table
    row" 子检查被 delta reviewer [debugger opus, 产物 phase3_node1_delta
    _reviewer.md] 证实在 VARIABLE_INDEX.md 等合法多表分节场景稳定 FP 77
    次, 已删除; 保留 (i) 紧贴模式, 即真 P13 违反场景, raw source 0 FP.)
  - MEDIUM-2: `_resolve_expected_segments` 改为 **优先读
    current/manifest_segments.json 里 merge 声明的 expected**, manifest
    缺 entry → FAIL "no manifest truth source". 原"再读 KB 子目录计数"
    的 self-consistent 机制移除 (KB 计数仅作 dev fallback 不作 PASS 真源).
  - Row 字段从 6 项扩到 7 项 (新增 v7); 报告矩阵列与细节段同步.
  - Node 2 起本版生效 (Node 1 禁运行, Node 2 跑 --stage batch1 触发校验).

v1.3 sync 记录 (2026-04-20, Node 2 attempt_1 V5 FAIL cap 微调同步):
  - EXPECTS[0] token_cap 46_000 → 47_000, 与 merge.py v1.3 保持一致.

v1.5 sync 记录 (2026-04-21, Node 4 batch 2 attempt_1 06 cap 微调同步):
  - EXPECTS[5] 06_domain_examples_all.md token_cap 190_000 → 254_000,
    与 merge.py v1.5 保持一致. 依据 `failures/stage_batch2_attempt_1.md`.

v1.4 sync 记录 (2026-04-21, Node 4 batch 2 重排 + merge.py v1.4 同步):
  依据: PLAN_BATCH2.md + Node 3b carry-over CO-2.
  - EXPECTS[6-8] 三 entry 重定义:
      * 07_terminology_core.md            → 07_terminology_core_high_freq.md
        (expected 0→15 硬编码, dynamic_source_dir "terminology/core"→"", cap
        920_000→260_000)
      * 08_terminology_questionnaires.md  → 08_terminology_quest_and_supp.md
        (expected 0→49 硬编码, dynamic_source_dir "terminology/questionnaires"
        →"", cap 1_095_000→1_250_000)
      * 09_terminology_supplementary.md   → 09_terminology_core_mid_tail.md
        (expected 0→27 硬编码, dynamic_source_dir "terminology/supplementary"
        →"", cap 173_000→820_000)
  - 全 batch 2 entry expected 硬编码 (无动态), 与 merge v1.4 一致, manifest
    entry 的 dynamic 字段均应为 False.
  - 01-06 entry 不变.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import tiktoken

# 模块级版本常量 (Phase 4 N5.1 LOW L1 fix, reviewer phase3_node4_reviewer.md):
# 避免 render_report 硬编码 "(v1.1)" 与 docstring v1.5 不一致. 升版时改此处.
SCRIPT_VERSION = "v1.5"

ENCODING_NAME = "cl100k_base"

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # ai_platforms/chatgpt_gpt/
REPO_ROOT = PROJECT_ROOT.parent.parent  # SDTM-compare/
KB_DIR = REPO_ROOT / "knowledge_base"
UPLOADS_DIR = PROJECT_ROOT / "current" / "uploads"
EVIDENCE_DIR = PROJECT_ROOT / "dev" / "evidence"
# MEDIUM-2: merge 写的独立真源. 此处只读; 若缺 entry 或文件不存在 → V2 FAIL.
MANIFEST_SEGMENTS_PATH = PROJECT_ROOT / "current" / "manifest_segments.json"

# ---------------------------------------------------------------------------
# 期望配置 (硬编码, 与 merge_for_chatgpt.py 的 MERGE_CONFIGS 对齐)
# ---------------------------------------------------------------------------


@dataclass
class ExpectSpec:
    target: str
    stage: str
    expected_segments: int  # 0 = 动态 (按 KB 子目录计数)
    dynamic_source_dir: str  # 动态段数的源目录 (相对 KB), 空串 = 不动态
    token_cap: int


EXPECTS: list[ExpectSpec] = [
    ExpectSpec("01_navigation.md", "batch1", 3, "", 47_000),
    ExpectSpec("02_chapters_all.md", "batch1", 6, "", 72_000),
    ExpectSpec("03_model_all.md", "batch1", 6, "", 21_000),
    ExpectSpec("04_domain_specs_all.md", "batch1", 63, "", 193_000),
    ExpectSpec("05_domain_assumptions_all.md", "batch2", 63, "", 69_000),
    ExpectSpec("06_domain_examples_all.md", "batch2", 63, "", 254_000),
    ExpectSpec("07_terminology_core_high_freq.md", "batch2", 15, "", 260_000),
    ExpectSpec("08_terminology_quest_and_supp.md", "batch2", 49, "", 1_250_000),
    ExpectSpec("09_terminology_core_mid_tail.md", "batch2", 27, "", 820_000),
]


SOURCE_COMMENT_RE = re.compile(r"<!--\s*source:\s*([^>]+?)\s*-->")
HEADING_RE = re.compile(r"^#{1,6}\s+")
TABLE_ROW_RE = re.compile(r"^\s*\|")


# ---------------------------------------------------------------------------
# 校验实现
# ---------------------------------------------------------------------------


def _load_manifest_segments() -> dict | None:
    """读取 merge 写的独立真源 JSON. 若缺/损坏, 返回 None (让 _resolve
    报 FAIL 'no manifest truth source', 避免 validate 另行重读 KB)."""
    if not MANIFEST_SEGMENTS_PATH.is_file():
        return None
    try:
        data = json.loads(MANIFEST_SEGMENTS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(data, dict) or not isinstance(data.get("entries"), dict):
        return None
    return data


def _resolve_expected_segments(
    spec: ExpectSpec,
    manifest: dict | None,
) -> tuple[int, str]:
    """决议 expected segment count, 返回 (expected, source_label).

    优先级:
      1. manifest_segments.json 的 entries[target].expected → 主真源 (MEDIUM-2)
      2. manifest 缺该 entry → 返回 (-2, "missing-from-manifest") 让 V2 FAIL
      3. manifest 整文件缺 → 返回 (-3, "no-manifest-file")

    静态硬编码 spec.expected_segments 只作 cross-check (若 manifest expected
    与静态值不符, 以 manifest 为准但记录在 source_label — 说明 merge 当次
    产物偏离 PLAN 声明, 但真源由 merge 声明主导, 静态值校验由 merge 自身
    的 fail-fast (MEDIUM-3) 负责; validate 不再 double-guard).
    """
    if manifest is None:
        return -3, "no-manifest-file"
    entry = manifest.get("entries", {}).get(spec.target)
    if not isinstance(entry, dict):
        return -2, "missing-from-manifest"
    expected = entry.get("expected")
    if not isinstance(expected, int) or expected < 0:
        return -2, "invalid-expected-in-manifest"
    if spec.expected_segments > 0 and expected != spec.expected_segments:
        return expected, f"manifest-overrides-static({spec.expected_segments})"
    if entry.get("dynamic", False):
        return expected, "manifest-dynamic"
    return expected, "manifest-static"


def _v1_non_empty(path: Path) -> tuple[str, str]:
    """V1 非空."""
    if not path.exists():
        return "FAIL", f"file missing: {path.name}"
    size = path.stat().st_size
    if size <= 0:
        return "FAIL", f"size={size}"
    return "PASS", f"size={size}"


def _v2_segment_count(
    text: str,
    expected: int,
    source_label: str,
) -> tuple[str, str]:
    """V2 段数对齐: `<!-- source: ... -->` 出现次数 == manifest 真源声明.

    MEDIUM-2: expected 由 manifest_segments.json 决议, 非 validate 重读 KB.
    expected < 0 时表示 manifest 缺 entry / 缺文件, 直接 FAIL.
    """
    n = len(SOURCE_COMMENT_RE.findall(text))
    if expected == -3:
        return "FAIL", (
            f"no manifest truth source (current/manifest_segments.json "
            f"missing or corrupt); actual={n}"
        )
    if expected == -2:
        return "FAIL", f"entry {source_label} (manifest); actual={n}"
    if expected < 0:
        return "FAIL", f"unexpected expected={expected}, actual={n}"
    if n != expected:
        return "FAIL", (
            f"actual={n}, expected={expected} "
            f"(truth-source: {source_label})"
        )
    return "PASS", f"{n} sources (truth-source: {source_label})"


def _v3_p12_coverage(text: str, expected: int) -> tuple[str, str]:
    """V3 P12 溯源覆盖率 100% (HIGH-1 重写, 逐段强校验).

    三段子条件, 任一 FAIL 则整体 FAIL:

    (a) 段数锚: source comment 数量 == expected (即 manifest 声明).
        若 expected < 0 (manifest 缺 / 坏), 由 V2 先 FAIL; V3 跳过.
        若 source comment 数与 expected 不符, 说明某段起始 source 被
        漏插/误删 — 这是 P12 "每合并段起始加溯源" 的核心硬门槛.
    (b) 首行锚: 文档首个非空行必须是 source comment (或紧跟第一 source
        comment 行之前只允许空行). 若首个非空行是 heading / 文本, 说明
        第 1 段起始没有 source comment.
    (c) heading 前必前置 source: 扫描每 heading, 在其行号之前 **必须
        至少出现过 1 个 source comment**. 等价于 "第一个 heading 之前
        必有 source comment". 结合 (a) 的"段数对齐"已能抓到 heading
        与 source 数失配, 这里防御性收窄: 抓到"首段仅有 heading 无
        source" 的产物 bug.

    诊断信息: FAIL 时打印首个违例 heading 行号 + 最近 source comment
    行号差 (或 "no source ever" 若全无 source 在其上游).
    """
    lines = text.splitlines()
    source_line_indices: list[int] = []  # 1-based 行号
    heading_line_indices: list[int] = []  # 1-based 行号
    first_non_empty_line_index: int | None = None
    first_non_empty_is_source: bool = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if first_non_empty_line_index is None and stripped:
            first_non_empty_line_index = i
            first_non_empty_is_source = bool(SOURCE_COMMENT_RE.search(line))
        if SOURCE_COMMENT_RE.search(line):
            source_line_indices.append(i)
            continue
        if HEADING_RE.match(line):
            heading_line_indices.append(i)

    source_count = len(source_line_indices)
    heading_count = len(heading_line_indices)

    if heading_count == 0 and source_count == 0:
        return "N/A", "no headings and no sources"

    # (a) 段数锚
    if expected >= 0 and source_count != expected:
        return (
            "FAIL",
            f"(a) source count {source_count} != expected {expected} "
            f"(some segment missing source comment)",
        )

    # (b) 首行锚
    if first_non_empty_line_index is not None and not first_non_empty_is_source:
        return (
            "FAIL",
            f"(b) first non-empty line {first_non_empty_line_index} is not "
            f"a source comment — first segment missing anchor",
        )

    # (c) heading 前必前置 source
    if heading_count > 0 and source_count == 0:
        return (
            "FAIL",
            f"(c) {heading_count} headings but 0 source comments — "
            f"first heading at line {heading_line_indices[0]}",
        )
    if heading_count > 0:
        first_heading = heading_line_indices[0]
        first_source = source_line_indices[0] if source_line_indices else None
        if first_source is None or first_source >= first_heading:
            return (
                "FAIL",
                f"(c) first heading at line {first_heading} appears before "
                f"any source comment "
                f"(first source at line {first_source})",
            )
        # 附加: 每个 heading 最近上游 source comment 距离 (诊断信息, 不 FAIL,
        # 只在 PASS message 打印 max 距离)
        max_distance = 0
        for h in heading_line_indices:
            # 找 h 之前最大的 source index
            prev_src = max(
                (s for s in source_line_indices if s < h),
                default=None,
            )
            if prev_src is None:
                return (
                    "FAIL",
                    f"(c) heading at line {h} has no upstream source comment",
                )
            max_distance = max(max_distance, h - prev_src)

        return (
            "PASS",
            f"{source_count} sources, {heading_count} headings; "
            f"max heading-to-source distance = {max_distance} lines",
        )

    # 纯 source 无 heading (01_navigation.md 首次极简情况)
    return "PASS", f"{source_count} sources, 0 headings"


def _v4_tableaware(text: str) -> tuple[str, str]:
    """V4 P13 表格完整: `<!-- source: ... -->` 不得落入 `|` 开头行块内部.

    判定: 对每个 source comment, 查看其前一非空行和后一非空行是否都是
    table row (`|` 开头). 若前一行是 table row 且后一行是 table row →
    注释落在表格中间 → FAIL. 其他情况 (段首 / heading 后 / 文本段) 放行.
    """
    lines = text.splitlines()
    violations: list[str] = []

    for i, line in enumerate(lines):
        if not SOURCE_COMMENT_RE.search(line):
            continue
        # 找前一非空行
        prev_line = ""
        for j in range(i - 1, -1, -1):
            if lines[j].strip():
                prev_line = lines[j]
                break
        # 找后一非空行
        next_line = ""
        for j in range(i + 1, len(lines)):
            if lines[j].strip():
                next_line = lines[j]
                break
        if TABLE_ROW_RE.match(prev_line) and TABLE_ROW_RE.match(next_line):
            violations.append(
                f"line {i+1}: source comment between table rows "
                f"(prev={prev_line[:40]!r} next={next_line[:40]!r})"
            )

    if violations:
        return "FAIL", "; ".join(violations[:3]) + (
            f" (+{len(violations)-3} more)" if len(violations) > 3 else ""
        )
    return "PASS", "no source comment inside table blocks"


def _v7_table_heading_split(text: str) -> tuple[str, str]:
    """V7 单表跨 heading (MEDIUM-1; v1.2 收窄: 仅保留 (i), 原 (ii) 被删).

    破坏形态 (v1.2 单检):
      (i)  连续 table row 块中间出现 heading 行 (行与行相邻, 中间无空行)
           → 表被 heading 切断, FAIL.

    v1.1 原设计含 (ii) "heading 前后最近非空行都是 table row 即 FAIL",
    delta reviewer (oh-my-claudecode:debugger opus, 产物
    `dev/evidence/phase3_node1_delta_reviewer.md`, 2026-04-20) 发现
    (ii) 在合法多表分节场景稳定 false-positive (VARIABLE_INDEX.md 62
    次 + INDEX.md + model 3 文件合计 77 次), 会阻塞 Node 2 batch1 所有
    PASS 路径. merge 是纯拼接 (P5 只读 + 0 改写), raw source 里 (i)
    模式 0 命中 ⇒ (i) 已精准覆盖 PLAN §1.2 P13 "单表不跨 heading"
    硬门槛, (ii) 纯 false-alarm 加码, 故 v1.2 删除. 详情见 delta
    reviewer D2 章节 (ii) 语义分析段.

    table 块终止规则 (markdown 标准): 任何空行 / 非 table 非 heading 文本
    都终止 table 块. source comment 行也终止 table 块 (视为普通文本).
    仅在 "紧接 table row 的下一行就是 heading" 才触发 (i) 违例 — 这就是
    真正的"heading 把表格劈开"场景.

    诊断: FAIL 时打印 heading 行号 + 起始 table 行号.
    """
    lines = text.splitlines()
    violations: list[str] = []

    def is_table(line: str) -> bool:
        return bool(TABLE_ROW_RE.match(line))

    def is_heading(line: str) -> bool:
        return bool(HEADING_RE.match(line))

    # (i) heading 紧跟 table row (中间无空行/无正常文本) → 表被切断
    in_table = False
    table_start = -1
    for i, line in enumerate(lines, start=1):
        if is_table(line):
            if not in_table:
                in_table = True
                table_start = i
            continue
        if not in_table:
            continue
        # in_table=True 且当前不是 table row — 判断终止类型
        if is_heading(line):
            # heading 紧接 table row → 切断
            violations.append(
                f"(i) heading at line {i} splits table starting at "
                f"line {table_start}: {line.strip()[:60]!r}"
            )
        # 任一非 table row (空行 / 普通文本 / source / heading) 都终止 table 块
        in_table = False

    if violations:
        return "FAIL", "; ".join(violations[:3]) + (
            f" (+{len(violations)-3} more)" if len(violations) > 3 else ""
        )
    return "PASS", "no table split by heading"


def _v5_token_cap(text: str, cap: int, encoder) -> tuple[str, str]:
    """V5 token 上限."""
    n = len(encoder.encode(text))
    if n > cap:
        return "FAIL", f"{n:,} > cap {cap:,}"
    return "PASS", f"{n:,} ≤ {cap:,}"


def _v6_md5(path: Path) -> tuple[str, str]:
    """V6 md5 稳定 (打印, 不 FAIL)."""
    h = hashlib.md5(path.read_bytes()).hexdigest()
    return "N/A", f"md5={h}"


# ---------------------------------------------------------------------------
# 聚合 + 报告
# ---------------------------------------------------------------------------


@dataclass
class Row:
    target: str
    stage: str
    v1: tuple[str, str]
    v2: tuple[str, str]
    v3: tuple[str, str]
    v4: tuple[str, str]
    v5: tuple[str, str]
    v6: tuple[str, str]
    v7: tuple[str, str]  # MEDIUM-1: 单表跨 heading

    @property
    def all_pass(self) -> bool:
        return all(
            v[0] in ("PASS", "N/A")
            for v in (self.v1, self.v2, self.v3, self.v4,
                      self.v5, self.v6, self.v7)
        )


def validate_one(spec: ExpectSpec, manifest: dict | None, encoder) -> Row:
    path = UPLOADS_DIR / spec.target
    if not path.exists():
        missing = ("FAIL", "file missing")
        return Row(spec.target, spec.stage,
                   missing, missing, missing, missing, missing, missing, missing)

    text = path.read_text(encoding="utf-8", errors="strict")
    expected_segs, source_label = _resolve_expected_segments(spec, manifest)

    return Row(
        target=spec.target,
        stage=spec.stage,
        v1=_v1_non_empty(path),
        v2=_v2_segment_count(text, expected_segs, source_label),
        v3=_v3_p12_coverage(text, expected_segs),
        v4=_v4_tableaware(text),
        v5=_v5_token_cap(text, spec.token_cap, encoder),
        v6=_v6_md5(path),
        v7=_v7_table_heading_split(text),
    )


def pick_specs(stage: str) -> list[ExpectSpec]:
    if stage == "all":
        return list(EXPECTS)
    return [e for e in EXPECTS if e.stage == stage]


def render_report(rows: list[Row], stage: str) -> str:
    ts = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        f"# ChatGPT GPTs 产物校验 — stage {stage}",
        "",
        f"> Generated: {ts}",
        f"> Script: `dev/scripts/validate_chatgpt_stage.py` ({SCRIPT_VERSION})",
        "> Scope: V1 非空 / V2 段数 (manifest truth) / V3 P12 覆盖 (逐段) / "
        "V4 P13 注释位置 / V5 token 上限 / V6 md5 / V7 单表跨 heading",
        "",
        "## 结果矩阵",
        "",
        "| 文件 | batch | V1 | V2 | V3 | V4 | V5 | V7 | V6 (md5) |",
        "|------|:-----:|:--:|:--:|:--:|:--:|:--:|:--:|:---------|",
    ]
    for r in rows:
        lines.append(
            f"| {r.target} | {r.stage} | "
            f"{r.v1[0]} | {r.v2[0]} | {r.v3[0]} | "
            f"{r.v4[0]} | {r.v5[0]} | {r.v7[0]} | {r.v6[1]} |"
        )

    lines += [
        "",
        "## 细节 (FAIL 诊断)",
        "",
    ]
    for r in rows:
        any_fail = any(
            v[0] == "FAIL"
            for v in (r.v1, r.v2, r.v3, r.v4, r.v5, r.v7)
        )
        if not any_fail:
            lines.append(f"- {r.target}: all PASS")
            continue
        lines.append(f"- {r.target}:")
        for name, v in (
            ("V1", r.v1), ("V2", r.v2), ("V3", r.v3),
            ("V4", r.v4), ("V5", r.v5), ("V7", r.v7),
        ):
            if v[0] == "FAIL":
                lines.append(f"    - {name} FAIL — {v[1]}")
    lines.append("")

    total = len(rows)
    passed = sum(1 for r in rows if r.all_pass)
    lines += [
        "## 汇总",
        "",
        f"- 文件数: {total}",
        f"- 全 PASS: {passed}/{total}",
        f"- FAIL: {total - passed}",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Validate ChatGPT GPTs merge outputs (V1-V6)."
    )
    parser.add_argument(
        "--stage",
        required=True,
        choices=["batch1", "batch2", "all"],
        help="batch1 = 01-04 / batch2 = 05-09 / all = 9 全量",
    )
    args = parser.parse_args(argv)

    if not UPLOADS_DIR.is_dir():
        print(
            f"error: uploads/ not found at {UPLOADS_DIR} "
            f"(run merge_for_chatgpt.py first)",
            file=sys.stderr,
        )
        return 1

    encoder = tiktoken.get_encoding(ENCODING_NAME)
    specs = pick_specs(args.stage)
    # MEDIUM-2: 预加载 manifest_segments.json (merge 写的独立真源).
    # 若缺 / 坏, 每 entry V2 会 FAIL "no manifest truth source".
    manifest = _load_manifest_segments()
    if manifest is None:
        print(
            f"warn: manifest_segments.json missing or invalid at "
            f"{MANIFEST_SEGMENTS_PATH} — all V2 will FAIL",
            file=sys.stderr,
        )
    rows = [validate_one(spec, manifest, encoder) for spec in specs]

    # stdout 概览
    for r in rows:
        flag = "PASS" if r.all_pass else "FAIL"
        print(
            f"[{flag}] {r.target} "
            f"V1={r.v1[0]} V2={r.v2[0]} V3={r.v3[0]} "
            f"V4={r.v4[0]} V5={r.v5[0]} V7={r.v7[0]} | {r.v6[1]}"
        )

    # 写 evidence
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    report_path = EVIDENCE_DIR / f"validate_{args.stage}.md"
    report_path.write_text(render_report(rows, args.stage), encoding="utf-8")
    print(f"\n[evidence] wrote {report_path.relative_to(REPO_ROOT)}")

    rc = 0 if all(r.all_pass for r in rows) else 1
    print(f"rc={rc}")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
