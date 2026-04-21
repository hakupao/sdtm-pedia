#!/usr/bin/env python3
"""
extract_req_vars.py — Phase A A2 (NotebookLM deploy v2)

从 knowledge_base/VARIABLE_INDEX.md 抽取所有 Core=Req 的 SDTM 变量, 产出结构化
req_vars_full_set.md 清单 (通用 Req + 领域专属 Req), 作 Q1 红线零丢失审计的
权威基线.

Usage:
    python3 extract_req_vars.py \\
        --index knowledge_base/VARIABLE_INDEX.md \\
        --out ai_platforms/notebooklm/dev/evidence/req_vars_full_set.md

Input: VARIABLE_INDEX.md 结构
- ## 一、通用变量（出现在 2+ 个域，共 24 个）→ 表头 7 列 (变量名|域数|出现的域|Label|Type|Role|Core)
- ## 二、领域专属变量（仅 1 个域，共 1499 个）→ per-domain subsection `### XX — Name (Class)`
  → 表头 6 列 (变量名|Label|Type|Role|Core|CT)
- ## 三、CDISC Controlled Terminology 交叉引用 → skip (无 Core)

Output: req_vars_full_set.md
- 通用 Req 表 (var, 域, Core, Label, Type, Role)
- 领域专属 Req per-domain 表 (var, Label, Type, Role, Core)
- 统计: 通用 Req 数 + 领域专属 Req 数 + 总 Req 记录数 + 去重独立 Req 变量数
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ReqRecord:
    variable: str
    core: str
    label: str = ""
    type_: str = ""
    role: str = ""
    ct: str = ""
    domain: str = ""
    cross_domain_list: str = ""  # 仅通用变量填


def parse_index(index_path: Path) -> tuple[list[ReqRecord], list[ReqRecord]]:
    """Parse VARIABLE_INDEX.md, return (common_req, domain_specific_req)."""
    text = index_path.read_text(encoding="utf-8")

    # Split by H2 sections
    sec_common = re.search(
        r"^## 一、通用变量.*?(?=^## 二、|^## 三、|\Z)",
        text, re.DOTALL | re.MULTILINE,
    )
    sec_domain = re.search(
        r"^## 二、领域专属变量.*?(?=^## 三、|\Z)",
        text, re.DOTALL | re.MULTILINE,
    )
    if not sec_common or not sec_domain:
        sys.exit("ERROR: cannot find '## 一' or '## 二' sections in index.")

    common_req = _parse_common(sec_common.group(0))
    domain_req = _parse_domain_specific(sec_domain.group(0))
    return common_req, domain_req


def _parse_common(section_text: str) -> list[ReqRecord]:
    """Parse Section 一 table. Columns: 变量名|域数|出现的域|Label|Type|Role|Core"""
    out: list[ReqRecord] = []
    # Match Markdown table rows: | col1 | col2 | ... |
    # First find table body (skip header + separator)
    lines = section_text.splitlines()
    in_table = False
    header_seen = False
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                break  # table ended
            continue
        # It's a table row
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 7:
            continue
        # Skip header (contains "变量名") and separator (contains "---")
        if cells[0] == "变量名":
            header_seen = True
            continue
        if "---" in cells[0] or "----" in cells[0]:
            in_table = True
            continue
        if not header_seen or not in_table:
            continue

        var, dom_count, dom_list, label, type_, role, core = cells[:7]
        # Core normalization: "Req" or "Req*" both count as Req
        if not _is_req(core):
            continue
        out.append(
            ReqRecord(
                variable=var,
                core=core,
                label=label,
                type_=type_,
                role=role,
                cross_domain_list=dom_list,
            )
        )
    return out


def _parse_domain_specific(section_text: str) -> list[ReqRecord]:
    """Parse Section 二. Iterate `### XX — Name` subsections, each followed by a table
    with columns: 变量名|Label|Type|Role|Core|CT"""
    out: list[ReqRecord] = []

    # Split by domain subsection headers `### XY — ...`
    # Pattern: lines like `### AE — Adverse Events (Events)`
    domain_pat = re.compile(r"^### ([A-Z]{2,}) — .*$", re.MULTILINE)

    matches = list(domain_pat.finditer(section_text))
    for i, m in enumerate(matches):
        domain = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(section_text)
        body = section_text[start:end]

        for line in body.splitlines():
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) < 6:
                continue
            if cells[0] == "变量名":
                continue
            if "---" in cells[0]:
                continue
            var, label, type_, role, core, ct = cells[:6]
            if not _is_req(core):
                continue
            out.append(
                ReqRecord(
                    variable=var,
                    core=core,
                    label=label,
                    type_=type_,
                    role=role,
                    ct=ct,
                    domain=domain,
                )
            )
    return out


def _is_req(core_value: str) -> bool:
    """Accept 'Req' or 'Req*' (with star marker for multi-domain variance)."""
    normalized = core_value.replace("*", "").strip()
    return normalized == "Req"


def render_output(common_req: list[ReqRecord], domain_req: list[ReqRecord]) -> str:
    """Render req_vars_full_set.md content."""
    lines: list[str] = []
    lines.append("# SDTM Core=Req 变量全集 (Phase A A2 产物)")
    lines.append("")
    lines.append("> **产出日期**: 2026-04-21")
    lines.append("> **执行脚本**: `dev/scripts/extract_req_vars.py`")
    lines.append("> **源文件**: `knowledge_base/VARIABLE_INDEX.md`")
    lines.append("> **目的**: 权威清单, 供 A3 cluster bucket 设计 + A4 结构级覆盖断言 + P3.4.5 语义级抽检 使用")
    lines.append("")

    total_records = len(common_req) + len(domain_req)
    unique_vars = set()
    for r in common_req:
        unique_vars.add(r.variable)
    for r in domain_req:
        unique_vars.add(r.variable)

    lines.append("## 统计")
    lines.append("")
    lines.append("| 指标 | 数 |")
    lines.append("|------|-----|")
    lines.append(f"| 通用 Req 变量 (出现在 2+ 域) | **{len(common_req)}** |")
    lines.append(f"| 领域专属 Req 变量记录 (by domain) | **{len(domain_req)}** |")
    lines.append(f"| **Req 记录总数** (通用 + 领域专属) | **{total_records}** |")
    lines.append(f"| **去重独立 Req 变量名数** | **{len(unique_vars)}** |")
    lines.append("")
    lines.append("> **说明**: 去重独立变量数计的是唯一变量名集合基数. 通用变量在 N 个域出现仍记 1 个独立变量;")
    lines.append("> 领域专属变量若同名在多域出现也只记 1 个独立变量 (如 `--SEQ` pattern 但 VARIABLE_INDEX 按域列)")
    lines.append("")

    # Section 1: 通用 Req
    lines.append("---")
    lines.append("")
    lines.append(f"## 一、通用 Req 变量 (出现在 2+ 域) — {len(common_req)} 个")
    lines.append("")
    if common_req:
        lines.append("| 变量名 | Core | Label | Type | Role | 出现的域 |")
        lines.append("|--------|------|-------|------|------|---------|")
        for r in sorted(common_req, key=lambda x: x.variable):
            lines.append(
                f"| {r.variable} | {r.core} | {r.label} | {r.type_} | {r.role} | {r.cross_domain_list} |"
            )
    else:
        lines.append("(空)")
    lines.append("")

    # Section 2: 领域专属 Req (group by domain)
    lines.append("---")
    lines.append("")
    by_domain: dict[str, list[ReqRecord]] = {}
    for r in domain_req:
        by_domain.setdefault(r.domain, []).append(r)

    lines.append(f"## 二、领域专属 Req 变量 (by domain) — {len(by_domain)} 域 × 平均 ~{len(domain_req)/max(len(by_domain),1):.1f} Req/域")
    lines.append("")
    for domain in sorted(by_domain.keys()):
        records = by_domain[domain]
        lines.append(f"### {domain} ({len(records)} Req)")
        lines.append("")
        lines.append("| 变量名 | Core | Label | Type | Role | CT |")
        lines.append("|--------|------|-------|------|------|----|")
        for r in sorted(records, key=lambda x: x.variable):
            lines.append(
                f"| {r.variable} | {r.core} | {r.label} | {r.type_} | {r.role} | {r.ct} |"
            )
        lines.append("")

    # Full list for diff / audit
    lines.append("---")
    lines.append("")
    lines.append("## 三、去重独立 Req 变量名全集 (A4 / P3.4.5 audit 基线)")
    lines.append("")
    lines.append("以下清单按字典序排列, A4 / P3.4.5 按此全集做蕴含式覆盖断言 (∀ req ∈ full_set, ∃ source, ...).")
    lines.append("")
    lines.append("```")
    for v in sorted(unique_vars):
        lines.append(v)
    lines.append("```")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*脚本执行结束. 独立 Req 变量 {len(unique_vars)} 个. Q1 红线零丢失审计基线 established.*")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract SDTM Core=Req variables from VARIABLE_INDEX.md")
    ap.add_argument("--index", required=True, type=Path, help="Path to VARIABLE_INDEX.md")
    ap.add_argument("--out", required=True, type=Path, help="Output path for req_vars_full_set.md")
    args = ap.parse_args()

    if not args.index.is_file():
        sys.exit(f"ERROR: index file not found: {args.index}")

    common_req, domain_req = parse_index(args.index)

    print(f"[extract_req_vars] 通用 Req 变量: {len(common_req)}", file=sys.stderr)
    print(f"[extract_req_vars] 领域专属 Req 记录: {len(domain_req)}", file=sys.stderr)
    unique = {r.variable for r in common_req} | {r.variable for r in domain_req}
    print(f"[extract_req_vars] 去重独立 Req 变量: {len(unique)}", file=sys.stderr)

    out_text = render_output(common_req, domain_req)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(out_text, encoding="utf-8")
    print(f"[extract_req_vars] Wrote: {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
