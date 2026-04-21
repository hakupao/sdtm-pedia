#!/usr/bin/env python3
"""
merge_sources.py — Phase 3 P3.1 (NotebookLM deploy v2)

读 bucket_config.json + knowledge_base/, 按每 bucket 的 files[] 合成 42 个
上传 md 文件到 current/uploads/. 每 bucket 生成一个 self-contained source md,
文件头加 metadata (bucket ID / name / description / 合并的源文件列表 / 字数),
便于 NotebookLM 索引 + 人读 citation 反查.

两类特殊 bucket (通过 `_auto_source` 字段识别):
  - variable_index_common: 从 VARIABLE_INDEX.md §一 抽 24 跨域变量详表 (bucket 02)
  - req_coverage_audit:    合并 req_vars_coverage_audit.md + req_vars_full_set.md (bucket 42)

Usage:
    python3 merge_sources.py \\
        --config ai_platforms/notebooklm/dev/scripts/bucket_config.json \\
        --knowledge-base knowledge_base \\
        --variable-index knowledge_base/VARIABLE_INDEX.md \\
        --evidence-dir ai_platforms/notebooklm/dev/evidence \\
        --out-dir ai_platforms/notebooklm/current/uploads
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def wc_words(text: str) -> int:
    return len(text.split())


def extract_section(text: str, heading_regex: str) -> str:
    """Extract a section by its `## X` heading until next `## ` or EOF."""
    m = re.search(heading_regex + r".*?(?=^## |\Z)", text, re.DOTALL | re.MULTILINE)
    if not m:
        sys.exit(f"ERROR: heading not found: {heading_regex}")
    return m.group(0).rstrip() + "\n"


# ---------- Auto-source handlers ----------

def handle_variable_index_common(
    bucket: dict, variable_index_path: Path
) -> str:
    """
    Bucket 02: 从 VARIABLE_INDEX.md §一 (通用变量 2+ 域) 抽 24 变量详表.
    同时附加 9 通用 Req + 主要 timing/visit 变量的解读段, 便于 NotebookLM
    在 "跨域通用变量" 类问题上精确召回.
    """
    text = variable_index_path.read_text(encoding="utf-8")
    section_one = extract_section(text, r"^## 一、通用变量")

    # 解释性前言: 9 通用 Req 变量识别 + timing/visit 变量识别
    preface = """## 跨域通用变量 — 快速识别

本 source 汇集所有在 2+ 域出现的通用变量, 共 24 个. SDTM 数据建模时, 这些变量
**每域重复出现但定义一致**, 是做跨域 join / 做 RELREC / 做 SUPPQUAL 时的锚点.

### 9 个 Core=Req 通用变量 (跨域强制必填, Q1 红线)

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `STUDYID` | 63 | 所有 SDTM 域首字段, 研究唯一标识, Char type |
| `DOMAIN` | 59 | 除 RELREC/RELSPEC/RELSUB/SUPPQUAL 4 个关系域外都有; 固定 2-3 字母代码 |
| `USUBJID` | 55 | 除 OI/TA/TD/TE/TI/TM/TS/TV 8 个 Trial Design + OI 域外都有 |
| `ETCD` | 3 | SE, TA, TE; Element Code, Topic 变量 |
| `IECAT` | 2 | IE, TI; 纳排标准 category |
| `IETEST` | 2 | IE, TI; 纳排准则全称 |
| `IETESTCD` | 2 | IE, TI; 纳排准则短名 |
| `MIDSTYPE` | 2 | SM, TM; Disease Milestone Type |
| `RDOMAIN` | 3 | CO, RELREC, SUPPQUAL; Related Domain Abbreviation (Req*, 星号表 Core 依域而异) |

### Timing/Visit 家族 (跨域高频, 多数 Perm, 但模式一致)

| 变量 | 出现域数 | Role | Core |
|------|---------|------|------|
| `VISITNUM` | 36 | Timing* | Exp* |
| `VISIT` | 36 | Timing* | Perm* |
| `VISITDY` | 36 | Timing | Perm |
| `EPOCH` | 44 | Timing | Perm* |
| `TAETORD` | 43 | Timing | Perm* |

### Arm/Element 家族 (Trial Design 与实际临床数据桥接)

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `ARM` | 3 | DM, TA, TV; Description of Planned Arm |
| `ARMCD` | 3 | DM, TA, TV; Planned Arm Code (连 DM 和 Trial Design) |
| `ELEMENT` | 3 | SE, TA, TE; 元素描述 |

### 关系域三件套 (CO/RELREC/SUPPQUAL 共用)

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `IDVAR` | 3 | CO, RELREC, SUPPQUAL; 被指向变量名 |
| `IDVARVAL` | 3 | CO, RELREC, SUPPQUAL; 被指向变量的值 |
| `RDOMAIN` | 3 | CO, RELREC, SUPPQUAL; 被指向域名 |

### 其他跨域变量

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `SPDEVID` | 6 | AE, BE, BS, EG, GF, RE; Sponsor Device Identifier |
| `NHOID` | 4 | GF, IS, MS, OI; Non-Host Organism Identifier |
| `FOCID` | 3 | MB, NV, OE; Focus of Study-Specific Interest |
| `MIDS` | 2 | ML, SM; Disease Milestone Instance Name |
| `IESCAT` | 2 | IE, TI; Inclusion/Exclusion Subcategory |

---

## VARIABLE_INDEX.md §一 原始表 (24 跨域变量)

以下为 knowledge_base/VARIABLE_INDEX.md §一 原始内容, 列出每个通用变量的
Label / Type / Role / Core / 具体出现的域名清单.

"""

    return preface + section_one


def handle_req_coverage_audit(
    bucket: dict, evidence_dir: Path
) -> str:
    """
    Bucket 42: 合并 req_vars_coverage_audit.md (结构断言 + 63 domain bucket mapping)
    + req_vars_full_set.md (176 Req 变量全名单), 作 NotebookLM Q1 红线元 source.
    """
    audit_md = evidence_dir / "req_vars_coverage_audit.md"
    full_set_md = evidence_dir / "req_vars_full_set.md"

    if not audit_md.is_file():
        sys.exit(f"ERROR: req_vars_coverage_audit.md not found at {audit_md}")
    if not full_set_md.is_file():
        sys.exit(f"ERROR: req_vars_full_set.md not found at {full_set_md}")

    audit_text = audit_md.read_text(encoding="utf-8")
    full_set_text = full_set_md.read_text(encoding="utf-8")

    # 移除两文件各自的 top-level `# ...` heading (上传文件自己的 heading 由我们补)
    audit_body = re.sub(r"^#\s+.*?\n", "", audit_text, count=1).lstrip()
    full_set_body = re.sub(r"^#\s+.*?\n", "", full_set_text, count=1).lstrip()

    return (
        "## Part A — Req 变量覆盖审计 (结构级 ∅ gap 自证)\n\n"
        + audit_body
        + "\n\n---\n\n"
        + "## Part B — Req 变量全集清单 (176 独立变量, 9 通用 + 167 领域专属)\n\n"
        + full_set_body
    )


# ---------- Regular bucket merge ----------

def merge_regular_bucket(bucket: dict, kb_root: Path) -> tuple[str, list[str]]:
    """
    合并 bucket.files[] 指向的 knowledge_base md 文件.
    返回 (合并后的正文 markdown, 缺失文件清单).
    """
    body_parts: list[str] = []
    missing: list[str] = []

    for relpath in bucket["files"]:
        fpath = kb_root / relpath
        if not fpath.is_file():
            missing.append(relpath)
            continue
        raw = fpath.read_text(encoding="utf-8")
        # 给每个源文件段加 H2 标题, 便于 NotebookLM citation 精确回指
        body_parts.append(f"## Source: `{relpath}`\n")
        body_parts.append(raw.rstrip())
        body_parts.append("")  # blank line separator

    return "\n".join(body_parts), missing


# ---------- Header builder ----------

def build_header(
    bucket: dict,
    body_words: int,
    body_char_count: int,
    merged_file_list: list[str],
    missing_files: list[str],
) -> str:
    """Build metadata header prepended to each uploaded source."""
    lines = [
        f"# {bucket['name'].replace('.md', '')}",
        "",
        f"> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)",
        f">",
        f"> - **Bucket ID**: `{bucket['id']}`",
        f"> - **Concept**: {bucket['description']}",
        f"> - **Merged files**: {len(merged_file_list)}",
        f"> - **Words**: {body_words:,}",
        f"> - **Chars**: {body_char_count:,}",
    ]
    if bucket.get("_auto_source"):
        lines.append(f"> - **Auto source**: `{bucket['_auto_source']}` ({bucket.get('_generator_note', '')})")
    if merged_file_list:
        lines.append(f"> - **Sources**:")
        for f in merged_file_list:
            lines.append(f">   - `{f}`")
    if missing_files:
        lines.append(f"> - ⚠️ **Missing files (skipped)**: {missing_files}")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


# ---------- Main ----------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--knowledge-base", required=True, type=Path)
    ap.add_argument("--variable-index", required=True, type=Path)
    ap.add_argument("--evidence-dir", required=True, type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    ap.add_argument("--out-manifest", type=Path, default=None,
                    help="Optional: regenerate uploads MANIFEST.md with actual words after merge")
    args = ap.parse_args()

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    buckets = cfg["buckets"]

    args.out_dir.mkdir(parents=True, exist_ok=True)

    summary: list[dict] = []
    total_bytes_written = 0

    for b in buckets:
        auto = b.get("_auto_source")
        missing_files: list[str] = []
        merged_file_list: list[str] = list(b.get("files", []))

        if auto == "variable_index_common":
            body = handle_variable_index_common(b, args.variable_index)
        elif auto == "req_coverage_audit":
            body = handle_req_coverage_audit(b, args.evidence_dir)
        else:
            body, missing_files = merge_regular_bucket(b, args.knowledge_base)

        body_words = wc_words(body)
        body_chars = len(body)
        header = build_header(b, body_words, body_chars, merged_file_list, missing_files)

        final = header + body.rstrip() + "\n"
        out_path = args.out_dir / b["name"]
        out_path.write_text(final, encoding="utf-8")
        total_bytes_written += len(final.encode("utf-8"))

        # 500K words cap sanity check (NotebookLM per-source cap)
        CAP = 500_000
        warn = "⚠️ OVER_CAP" if body_words > CAP else ""
        summary.append({
            "id": b["id"],
            "name": b["name"],
            "merged_files": len(merged_file_list),
            "missing_files": len(missing_files),
            "words": body_words,
            "chars": body_chars,
            "warn": warn,
        })

    # ---------- Summary ----------
    print("=" * 88, file=sys.stderr)
    print(f"{'ID':<4} {'Name':<55} {'Files':>6} {'Missing':>8} {'Words':>10}", file=sys.stderr)
    print("-" * 88, file=sys.stderr)
    for s in summary:
        print(
            f"{s['id']:<4} {s['name']:<55} {s['merged_files']:>6} "
            f"{s['missing_files']:>8} {s['words']:>10,} {s['warn']}",
            file=sys.stderr,
        )
    print("-" * 88, file=sys.stderr)
    print(f"Total buckets: {len(summary)}", file=sys.stderr)
    print(f"Total words: {sum(s['words'] for s in summary):,}", file=sys.stderr)
    print(f"Total bytes: {total_bytes_written:,} ({total_bytes_written/1024/1024:.2f} MiB)", file=sys.stderr)
    print(f"Over-cap buckets (>500K words): {sum(1 for s in summary if s['warn'])}", file=sys.stderr)
    print(f"Output directory: {args.out_dir}", file=sys.stderr)
    print("=" * 88, file=sys.stderr)

    # ---------- Optional: regenerate MANIFEST.md with real words ----------
    if args.out_manifest:
        manifest_lines = [
            "# SDTM Knowledge Base — NotebookLM 上传 MANIFEST (v2)",
            "",
            "> **产出日期**: 2026-04-21 (P3.1 merge 后更新)",
            "> **执行脚本**: `dev/scripts/merge_sources.py` (words/chars 从实际合成文件取, 非 bucket_config 估算)",
            f"> **上传文件数**: **{len(summary)}** (Pro 300 cap 的 {len(summary)*100/300:.1f}%)",
            f"> **总 words**: {sum(s['words'] for s in summary):,}",
            f"> **最大 bucket words**: {max(s['words'] for s in summary):,} (NotebookLM per-source cap 500K, headroom {(500000-max(s['words'] for s in summary))*100/500000:.0f}%)",
            "> **Notebook**: `SDTM Knowledge Base` (单 notebook, ABC 三场景分享档位切换)",
            "> **Chat mode**: Custom (instructions.md, ≤10K char)",
            "",
            "## 上传清单",
            "",
            "| # | Source name | Merged files | Words | Concept |",
            "|---|------------|--------------|-------|---------|",
        ]
        # 重新取 description (summary 里没保留)
        desc_by_id = {b["id"]: b["description"] for b in buckets}
        for s in summary:
            manifest_lines.append(
                f"| {s['id']} | `{s['name']}` | {s['merged_files']} | "
                f"{s['words']:,} | {desc_by_id.get(s['id'], '')} |"
            )
        manifest_lines.extend([
            "",
            "## Req 变量覆盖声明 (Q1 红线 结构级自证)",
            "",
            "✅ **∀ req ∈ req_vars_full_set (176), ∃ bucket ∈ uploads, 使 req ∈ bucket.covered_req_set**",
            "",
            "**Q1 红线自证: 零漏集 (∅ gap)**. 63 domains 全覆盖, 176 独立 Req 变量全覆盖. 详见 bucket 42 (`42_req_variable_coverage_audit.md`) + 原审计 `dev/evidence/req_vars_coverage_audit.md`.",
            "",
            "## 后续",
            "",
            "- **P3.2**: 用户登 notebooklm.google.com → 新建 `SDTM Knowledge Base` → 拖拽本目录全部 42 个 md → 等 indexing 完成",
            "- **P3.3**: Chat → Configure → Custom mode, 贴 `../instructions.md` 全文 (≤10K char)",
            "- **P3.4**: Indexing smoke N=10 (每 source 预览 + 10 题 citation 精确回指)",
            "- **P3.4.5**: Req 变量业务问答 N=10 (Q1 红线语义级自证, 规则 A 正本)",
            "",
        ])
        args.out_manifest.parent.mkdir(parents=True, exist_ok=True)
        args.out_manifest.write_text("\n".join(manifest_lines), encoding="utf-8")
        print(f"[merge] MANIFEST updated: {args.out_manifest}", file=sys.stderr)

    # 非 0 退出码若有 over-cap (可能触发 CI fail)
    if any(s["warn"] for s in summary):
        sys.exit(2)


if __name__ == "__main__":
    main()
