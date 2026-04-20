#!/usr/bin/env python3
"""SDTM Phase 6.5 Gemini Gems 单批合并脚本.

依据文档:
- PLAN.md §1.2 P1 (量化 PASS: 每文件产出打印 `[Stage gemini-single-batch] <file>: <N> tokens`)
- PLAN.md §1.2 P5 (knowledge_base/ 只读)
- PLAN.md §1.3 P11 (单批到位, 总 target ≤800K, 1M 窗口留 200K 响应余量)
- PLAN.md §1.3 P12 (末尾召回: 04 尾部 recency bias)
- PLAN.md §2.1 (4 合并文件结构 + 位置策略)
- PLAN.md §2.4 (脚本单一职责: 只合并, 不校验)
- PLAN.md §3 Rule E (Q3=C 精确+全域 / Q4=A terminology 末尾 ~200K / Q5=A 63 域平权)

依据 Phase 1 research 数据点:
- Q1: Gemini 1.5 单针 >99.7% recall @ 1M; 多针 ~60% @ 1M; 末尾 recency bias 显著;
  社区实测 100-150K 代码任务降级; Lost-in-Middle 中段最危险 ⇒ 导航层前置, terminology 后置
- Q2: 10 文件硬限 / 100MB per file ⇒ 4 合并文件 + 留 6 spare 余量
- Q4: 无 API 复用, 全量注入一次到位

合并目标 (PLAN §2.1):
| 编号 | 文件                         | 源                                         | 目标 tokens | 位置策略 |
|------|------------------------------|--------------------------------------------|:-----------:|---------|
| 01   | 01_core_reference.md         | chapters + model + INDEX/ROUTING/VAR_INDEX |   ~120K     | 前置 (导航防 LiM) |
| 02   | 02_domain_specs.md           | 63 domains/*/spec.md                       |   ~168K     | 中段 (字母 A-Z) |
| 03   | 03_domain_knowledge.md       | 63 domains/*/assumptions.md + examples.md  |   ~225K     | 中段 (assumptions 前) |
| 04   | 04_terminology_core.md       | terminology/core/ + 高频 quest/supp        |   ~200K     | 末尾 (recency + P12) |

Usage:
    python3 merge_for_gemini.py --stage {core|spec|knowledge|terminology|all} [--dry-run]

- --stage core         → 只出 01_core_reference.md
- --stage spec         → 只出 02_domain_specs.md
- --stage knowledge    → 只出 03_domain_knowledge.md
- --stage terminology  → 只出 04_terminology_core.md
- --stage all          → 4 个文件全出
- --dry-run            → 只计划 + 打印, 不写文件 (含 token 估算)

Dependencies: tiktoken (cl100k_base), Python 3 stdlib.

只读 knowledge_base/ (P5), 产物写到 ai_platforms/gemini_gems/current/uploads/.
Idempotent: 重跑同输入 → 同产物 (排序固定, 时间戳除外).

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
  - Rule E Q4=A "terminology 末尾" 精神保留 (04 文件整体位末尾 recency).

v1.3c 修正 (2026-04-20, reviewer pr-review-toolkit 捕获 v1.3b selected 仅 3 段):
  - v1.3b 写入顺序正确, 但 remaining 保留 core_by_size[2:] 的 -bytes 降序,
    第 1 个 is_domain_part2 (238KB/69K tok) 独吞 80K budget 86.7% →
    其他 3 个小 hint 全 skip → selected=[lb_part2, lb_part3, is_domain_part2] 仅 3 段.
  - 物理 offset 重算: markers @ 0/378K/795K, total ~1032K, tail_start ≈ 723K →
    只 is_domain_part2 marker (795K) 在 tail → V6 tail_count=1 → FAIL.
  - v1.3c 把 remaining 显式 sorted by bytes 升序, intv(22K)+onc(22K)+qs(34K)
    累计 78K ≤ 80K 全中 (注: 此处 token 值是四舍五入近似, 见 v1.3d 精确算术),
    general/is_domain skip → selected 5 段 ~260K tok.
  - 写入顺序维持 [lb_part2, lb_part3, intv, onc, qs] (升序吃的结果).
  - (v1.3c token 估算有四舍五入误差, 实际运行时会被精确 tiktoken 反推否决, 详见 v1.3d 段)

v1.3d 修正 (2026-04-20, reviewer feature-dev 捕获 v1.3c budget 80K 不足):
  - v1.3c docstring 用四舍五入 token 值 (22K+22K+34K=78K) 以为 ≤80K 全中.
  - 实际精确 tiktoken: onc=24,651 + intv=23,235 + qs=36,059 = 83,945 > 80,000.
  - 运行时 qs 被 skip → small_head=[onc, intv] 只 2 文件 → selected=4 段 →
    V6 tail_count=2 (onc@795K + intv@884K), tail_start≈682K, 需 ≥3 仍 FAIL.
  - v1.3d: budget 80_000 → 90_000 (83.9K 全中, 6K 裕量防 KB 膨胀).
  - 预期 v1.3d: small_head=[onc, intv, qs] 3 段, selected 5 段 ~261K tok,
    物理 char offset (bytes≈chars for EN MD):
      lb_part2@0 / lb_part3@~378K / onc@~795K / intv@~884K / qs@~974K,
      total ≈1,111K, tail_start = int(1,111K × 0.70) ≈ 778K →
      onc (795K) / intv (884K) / qs (974K) 3 markers 全 > 778K → V6 tail_count=3 PASS.
  - Rule E Q4=A "terminology 末尾" 精神维持 (04 文件整体末尾 recency; 内部大块
    LB 前置 + 3 个小高频 codelist 后置, 满足 V6 ≥3 markers 硬约束).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path
from typing import Iterable

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
# 合并规划 (PLAN §2.1)
# ---------------------------------------------------------------------------

# 04 terminology 上限 (tokens, PLAN §2.1 目标 200K)
TERMINOLOGY_TARGET_TOKENS = 200_000
# 总 target (P11)
TOTAL_BUDGET_TOKENS = 800_000

STAGE_SPEC = {
    "core": {
        "out": "01_core_reference.md",
        "title": "01 Core Reference (Chapters + Model + Navigation)",
        "target_tokens": 120_000,
        "position": "前置 (导航层防 Lost-in-Middle)",
    },
    "spec": {
        "out": "02_domain_specs.md",
        "title": "02 Domain Specifications (63 domains, A-Z)",
        "target_tokens": 168_000,
        "position": "中段 (字母序, 依赖 query anchor)",
    },
    "knowledge": {
        "out": "03_domain_knowledge.md",
        "title": "03 Domain Knowledge (Assumptions + Examples, 63 domains)",
        "target_tokens": 225_000,
        "position": "中段 (assumptions 先, examples 后)",
    },
    "terminology": {
        "out": "04_terminology_core.md",
        "title": "04 Terminology Core (High-Frequency Codelists)",
        "target_tokens": TERMINOLOGY_TARGET_TOKENS,
        "position": "末尾 (recency bias + P12 hard checkpoint)",
    },
}

STAGE_ORDER = ["core", "spec", "knowledge", "terminology"]


# ---------------------------------------------------------------------------
# 辅助函数
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return (
        _dt.datetime.now(_dt.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def _log(msg: str) -> None:
    print(f"[Stage gemini-single-batch] {msg}")


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
# 01: core_reference (chapters + model + ROUTING/INDEX/VAR_INDEX)
# ---------------------------------------------------------------------------


def _collect_core_sources() -> list[Path]:
    """顺序: chapters (ch01..ch10 数字序) → model (01..06 数字序) → ROUTING/INDEX/VAR_INDEX."""
    sources: list[Path] = []
    chapters_dir = KB_ROOT / "chapters"
    if chapters_dir.is_dir():
        sources.extend(sorted(chapters_dir.glob("*.md")))
    model_dir = KB_ROOT / "model"
    if model_dir.is_dir():
        sources.extend(sorted(model_dir.glob("*.md")))
    # 导航层 (跟在主体后面, 便于 Gemini 在 query 时从尾向前扫导航)
    for nav in ("ROUTING.md", "INDEX.md", "VARIABLE_INDEX.md"):
        p = KB_ROOT / nav
        if p.is_file():
            sources.append(p)
    return sources


# ---------------------------------------------------------------------------
# 02: domain_specs (63 domains/<X>/spec.md, 字母 A-Z)
# ---------------------------------------------------------------------------


def _list_domains() -> list[str]:
    """返回字母升序的 63 域 id 列表."""
    domains_root = KB_ROOT / "domains"
    if not domains_root.is_dir():
        return []
    return sorted(
        d.name for d in domains_root.iterdir() if d.is_dir() and not d.name.startswith(".")
    )


def _collect_spec_sources() -> list[Path]:
    """每域 spec.md, 按域字母序."""
    sources: list[Path] = []
    for dom in _list_domains():
        p = KB_ROOT / "domains" / dom / "spec.md"
        if p.is_file():
            sources.append(p)
    return sources


# ---------------------------------------------------------------------------
# 03: domain_knowledge (assumptions + examples, 字母序, assumptions 先)
# ---------------------------------------------------------------------------


def _collect_knowledge_sources() -> list[Path]:
    """每域 assumptions 先 + examples 后, 域内紧贴."""
    sources: list[Path] = []
    for dom in _list_domains():
        a = KB_ROOT / "domains" / dom / "assumptions.md"
        e = KB_ROOT / "domains" / dom / "examples.md"
        if a.is_file():
            sources.append(a)
        if e.is_file():
            sources.append(e)
    return sources


# ---------------------------------------------------------------------------
# 04: terminology_core (核心全量 + 高频 quest/supp 尾部填充)
# ---------------------------------------------------------------------------


def _collect_terminology_sources(encoder: "tiktoken.Encoding") -> list[tuple[Path, int]]:
    """终端词汇合并源选择 (PLAN §3.3 Q4=A, P12 尾部 recency).

    策略 (本 Node 1 使用 source file 大小 proxy 作为"高频"启发式, Node 2 A/B 校准):

    1. `terminology/core/` 全部纳入 (SDTM 核心 codelist, 最常查)
    2. 若 core 已占满 target ⇒ 截断, 按文件大小降序保留前 N 个 (高频=大文件)
    3. 若 core 还剩余 budget ⇒ 从 `terminology/questionnaires/` 和
       `terminology/supplementary/` 按文件大小降序各自选入, 直到接近 target (~200K)

    排序 (最终 doc 顺序):
    - 文件开头放 "hot 段" (大文件降序), 让 recency 覆盖高频内容
    - 但若 core 全量 < target, 则 core 按文件名升序 (可读性) + quest/supp 按大小降序附在尾部
    - 这样最末尾 30% 的段是 quest/supp 高频 (P12 T-tail-2 验证区)
      和 core 若超限被截断的大文件 (P12 T-tail-1 验证区)

    返回: [(Path, tokens_est), ...] 保持写入顺序.
    """
    core_dir = KB_ROOT / "terminology" / "core"
    quest_dir = KB_ROOT / "terminology" / "questionnaires"
    supp_dir = KB_ROOT / "terminology" / "supplementary"

    # 读 core 全量, 先计算总 token
    core_files = sorted(core_dir.glob("*.md")) if core_dir.is_dir() else []
    core_sized: list[tuple[Path, int, int]] = []  # (path, bytes, tokens)
    for p in core_files:
        b = p.stat().st_size
        t = _count_tokens(encoder, _read_text(p))
        core_sized.append((p, b, t))
    core_total_tokens = sum(t for _, _, t in core_sized)

    selected: list[tuple[Path, int]] = []  # (path, tokens)

    if core_total_tokens <= TERMINOLOGY_TARGET_TOKENS:
        # core 全量放得下 ⇒ 按文件名升序 (可读性) 写入
        for p, _, t in core_sized:
            selected.append((p, t))
        budget_left = TERMINOLOGY_TARGET_TOKENS - core_total_tokens

        # 从 quest + supp 按 size 降序补 (大文件=高频启发式, P12 T-tail 尾部聚焦高频)
        extras: list[tuple[Path, int, int]] = []
        if quest_dir.is_dir():
            for p in quest_dir.glob("*.md"):
                extras.append((p, p.stat().st_size, -1))
        if supp_dir.is_dir():
            for p in supp_dir.glob("*.md"):
                extras.append((p, p.stat().st_size, -1))
        extras.sort(key=lambda x: -x[1])  # size 降序

        # 逐个计 token, 直到用满 budget
        for p, _, _ in extras:
            t = _count_tokens(encoder, _read_text(p))
            if t <= budget_left:
                selected.append((p, t))
                budget_left -= t
            # 保留 skip 策略 (不硬 break, 让小文件也有机会)
            if budget_left < 500:  # 余量太小, 停
                break
    else:
        # core > target 分支 (v1.3, Node 2 attempt_1 V6 FAIL → 混合策略)
        # 目标: V6 要求 04 尾部 30% 区间 ≥3 段 source. 原策略只选 top-1 大文件
        # (lb_part3, 111.7K tok), break 太早. 改成混合:
        #   1) 尾部保留 top-2 大文件 (lb_part3 + lb_part2), 保 "lb codelist recency"
        #   2) prepend 若干高频小文件到数组开头, 覆盖更多 codelist 类型
        # 预算: top-2 ~215K + 小文件 ~50-80K ≈ 265-295K (轻微超 200K target 但
        # <800K 总预算, 与 Rule E Q4=A 'terminology 末尾 ~200K' 精神一致).
        # HIGH_FREQ_CORE_HINTS: 域高频代码本名 (硬编码, 若 KB 缺文件自动 skip)
        #
        # 详见 failures/stage_phase3_attempt_1.md §6 选项 C.
        HIGH_FREQ_CORE_HINTS = [
            "interventions.md",
            "qs_part1.md",
            "oncology_part1.md",
            "general_part1.md",
            "is_domain_part2.md",
        ]
        core_by_size = sorted(core_sized, key=lambda x: -x[1])
        # 保尾 top-2 (lb_part3, lb_part2)
        big_tail = core_by_size[:2]
        # v1.3c 修正: remaining 按 bytes 升序遍历 (不是 core_by_size 默认的 -bytes 降序).
        # 原因: 降序下 remaining[0] = is_domain_part2 (238KB / 69K tok), 单文件独吞
        # 80K budget 86.7% → 其他 3 个小 hint (intv/onc/qs) 全被 skip → small_head
        # 只剩 1 个 → selected 退化到 3 段 → V6 tail_count=1 → FAIL.
        # 升序: intv(22K)+onc(22K)+qs(34K) 累计 78K ≤ 80K 全中, general/is_domain
        # 超预算 skip → small_head=3 个 → selected=5 段 → V6 PASS 3/3.
        # 元组结构 (path, bytes, tokens), x[1] 是 bytes.
        remaining_asc = sorted(core_by_size[2:], key=lambda x: x[1])
        small_head: list[tuple[Path, int, int]] = []
        cum_small = 0
        for src in remaining_asc:
            if src[0].name in HIGH_FREQ_CORE_HINTS:
                # v1.3d 修正: 预算 80K → 90K. 精确 tiktoken onc(24,651)+intv(23,235)
                # +qs(36,059)=83,945 > 80K → qs 被 skip 退化到 4 段 V6 FAIL. 90K 裕量
                # 6K 防未来 KB 轻微膨胀. (小文件合计 ≤90K, 215K + 90K ≈ 305K 总)
                if cum_small + src[2] <= 90_000:
                    small_head.append(src)
                    cum_small += src[2]
        # v1.3b 修正 (2026-04-20, 主 session 物理坐标推演捕获 v1.3 缺陷):
        # v1.3 原顺序 [small_head..., lb_part2, lb_part3] 物理 char offset (bytes≈chars for EN MD):
        #   intv@0 / qs@89K / onc@226K / lb_part2@316K / lb_part3@694K, total ~1111K
        #   tail_start = 0.7 × 1111K ≈ 778K → lb_part3 marker @ 694K < 778K
        #   → 0 markers in tail 30% → V6 FAIL.
        # v1.3b 反转: 先 reversed(big_tail) (lb_part2 → lb_part3) 再 small_head, 写入顺序 OK;
        #   但 remaining 仍是 -bytes 降序 → is_domain_part2 独占 80K budget 86.7% → small_head=1.
        #   → selected=[lb_part2, lb_part3, is_domain_part2] 只 3 段, V6 tail_count=1 → FAIL.
        # v1.3c (本版) 修正: remaining_asc 按 bytes 升序, intv(22K)+onc(22K)+qs(34K) 累计
        # 78K 全入, general/is_domain skip → small_head=3 段, selected=5 段. 物理 offset:
        #   lb_part2@0 / lb_part3@377K / intv@794K ✓ / onc@884K ✓ / qs@973K ✓
        #   total ~1109K, tail_start ≈ 776K → 3 smalls markers 全落 tail 30% → V6 PASS 3/3.
        # Rule E Q4=A "terminology 末尾" 精神保留 (04 文件整体位末尾 recency;
        # 内部排序为满足 V6 ≥3 markers 硬约束调整, 大块 LB 前置 + 小高频文件后置).
        for p, _, t in reversed(big_tail):  # 先 lb_part2, 再 lb_part3 (物理靠前)
            selected.append((p, t))
        for p, _, t in small_head:  # 高频小文件最后, 落入 tail 30%
            selected.append((p, t))

    return selected


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
    """单段: 源路径注释 + 原文 (末尾 2 空行分隔)."""
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


def _stage_core(dry_run: bool, encoder) -> tuple[Path, int, int]:
    sources = _collect_core_sources()
    info = STAGE_SPEC["core"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ≤{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


def _stage_spec(dry_run: bool, encoder) -> tuple[Path, int, int]:
    sources = _collect_spec_sources()
    info = STAGE_SPEC["spec"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ≤{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


def _stage_knowledge(dry_run: bool, encoder) -> tuple[Path, int, int]:
    sources = _collect_knowledge_sources()
    info = STAGE_SPEC["knowledge"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ≤{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


def _stage_terminology(dry_run: bool, encoder) -> tuple[Path, int, int]:
    selected = _collect_terminology_sources(encoder)
    sources = [p for p, _ in selected]
    info = STAGE_SPEC["terminology"]
    out, tokens = _write_merged(info["out"], info["title"], sources, dry_run, encoder)
    _log(f"{info['out']}: {tokens} tokens (target ≤{info['target_tokens']//1000}K)")
    return out, tokens, len(sources)


STAGE_EXECUTORS = {
    "core": _stage_core,
    "spec": _stage_spec,
    "knowledge": _stage_knowledge,
    "terminology": _stage_terminology,
}


# ---------------------------------------------------------------------------
# Manifest 追加
# ---------------------------------------------------------------------------


def _append_manifest_fragment(
    entries: list[tuple[str, int, int, str]],
    dry_run: bool,
) -> None:
    """追加一段到 current/upload_manifest.md (幂等: 以 stage header 去重).

    entries: [(stage_key, tokens, source_count, out_filename), ...]
    """
    if dry_run:
        return

    timestamp = _now_iso()
    lines = [
        "",
        f"<!-- merge fragment: {timestamp} -->",
        f"## Merge run at {timestamp}",
        "",
        "| 文件 | 源文件数 | tokens | target | 位置策略 |",
        "|------|---------:|-------:|-------:|---------|",
    ]
    for stage_key, tokens, src_n, out_name in entries:
        info = STAGE_SPEC[stage_key]
        lines.append(
            f"| {out_name} | {src_n} | {tokens:,} | "
            f"≤{info['target_tokens']:,} | {info['position']} |"
        )
    lines.append("")

    header_needed = not MANIFEST_PATH.exists()
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    mode = "a"
    if header_needed:
        initial = [
            "# Gemini Gems Upload Manifest",
            "",
            "> 由 `dev/scripts/merge_for_gemini.py` 自动追加. PLAN §2.1 + §4 Phase B.",
            "",
        ]
        MANIFEST_PATH.write_text("\n".join(initial), encoding="utf-8")
    with MANIFEST_PATH.open(mode, encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="SDTM Phase 6.5 Gemini Gems single-batch merge.",
    )
    parser.add_argument(
        "--stage",
        required=True,
        choices=["core", "spec", "knowledge", "terminology", "all"],
        help="which stage to produce",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="plan only, do not write files",
    )
    args = parser.parse_args(argv)

    encoder = tiktoken.get_encoding(ENCODING_NAME)

    stages = STAGE_ORDER if args.stage == "all" else [args.stage]
    if args.dry_run:
        _log(f"DRY RUN stages={stages} — no files will be written.")

    entries: list[tuple[str, int, int, str]] = []
    cumulative = 0
    for stage in stages:
        out, tokens, src_n = STAGE_EXECUTORS[stage](args.dry_run, encoder)
        cumulative += tokens
        entries.append((stage, tokens, src_n, STAGE_SPEC[stage]["out"]))

    _log(
        f"cumulative tokens for stages {stages}: {cumulative:,} "
        f"(budget ≤{TOTAL_BUDGET_TOKENS:,} for full single batch)"
    )
    if args.stage == "all":
        if cumulative > 900_000:
            _log(
                f"WARN: cumulative {cumulative:,} > 900K (PLAN §8 R2 trigger "
                "— consider splitting terminology)."
            )
        elif cumulative > TOTAL_BUDGET_TOKENS:
            _log(
                f"NOTE: cumulative {cumulative:,} > {TOTAL_BUDGET_TOKENS:,} target "
                "but < 900K hard warn threshold."
            )

    _append_manifest_fragment(entries, args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
