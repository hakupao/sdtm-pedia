#!/usr/bin/env python3
"""
Generate VARIABLE_INDEX.md from all spec.md files in knowledge_base/domains/.

Parses each spec.md to extract variable metadata, then produces a three-section
reverse index: shared variables, domain-specific variables, and CT cross-references.
"""

import re
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# Paths
KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"
DOMAINS_DIR = KB_ROOT / "domains"
OUTPUT_FILE = KB_ROOT / "VARIABLE_INDEX.md"


def parse_spec_md(filepath: Path) -> dict:
    """Parse a single spec.md file, return domain metadata + variable list."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Line 1: # AE — Adverse Events
    m = re.match(r"^#\s+(\S+)\s+—\s+(.+)$", lines[0])
    if not m:
        raise ValueError(f"Cannot parse header in {filepath}: {lines[0]}")
    domain_code = m.group(1)
    domain_name = m.group(2).strip()

    # Line 3: > Class: Events | Structure: One record per ...
    obs_class = ""
    structure = ""
    for line in lines[1:5]:
        m2 = re.match(r"^>\s*Class:\s*(.+?)\s*\|\s*Structure:\s*(.+)$", line)
        if m2:
            obs_class = m2.group(1).strip()
            structure = m2.group(2).strip()
            break

    # Parse variable blocks
    variables = []
    current_var = None

    for line in lines:
        # New variable header
        m3 = re.match(r"^###\s+(\S+)\s*$", line)
        if m3:
            if current_var:
                variables.append(current_var)
            current_var = {
                "name": m3.group(1),
                "order": None,
                "label": "",
                "type": "",
                "ct": "",
                "role": "",
                "core": "",
            }
            continue

        if current_var is None:
            continue

        # Field extraction
        field_patterns = {
            "order": r"^\-\s+\*\*Order:\*\*\s*(.+)$",
            "label": r"^\-\s+\*\*Label:\*\*\s*(.+)$",
            "type": r"^\-\s+\*\*Type:\*\*\s*(.+)$",
            "ct": r"^\-\s+\*\*Controlled Terms:\*\*\s*(.*)$",
            "role": r"^\-\s+\*\*Role:\*\*\s*(.+)$",
            "core": r"^\-\s+\*\*Core:\*\*\s*(.+)$",
        }
        for field, pattern in field_patterns.items():
            m4 = re.match(pattern, line)
            if m4:
                val = m4.group(1).strip()
                if field == "order":
                    current_var[field] = int(val) if val.isdigit() else val
                else:
                    current_var[field] = val
                break

    if current_var:
        variables.append(current_var)

    return {
        "domain": domain_code,
        "full_name": domain_name,
        "class": obs_class,
        "structure": structure,
        "variables": variables,
    }


def extract_ct_code(ct_string: str) -> str:
    """Extract the primary CT code from a Controlled Terms value."""
    if not ct_string:
        return ""
    # Match C-code pattern like C66742
    m = re.match(r"(C\d+)", ct_string)
    return m.group(1) if m else ""


def generate_index(domains_data: list[dict]) -> str:
    """Generate the full VARIABLE_INDEX.md content."""
    # Build reverse index: var_name -> list of {domain, label, type, role, core, ct}
    var_index = defaultdict(list)
    ct_index = defaultdict(list)  # ct_code -> list of "DOMAIN.VARNAME"

    total_entries = 0
    for d in domains_data:
        for v in d["variables"]:
            total_entries += 1
            var_index[v["name"]].append({
                "domain": d["domain"],
                "class": d["class"],
                "label": v["label"],
                "type": v["type"],
                "role": v["role"],
                "core": v["core"],
                "ct": v["ct"],
            })
            ct_code = extract_ct_code(v["ct"])
            if ct_code:
                ct_index[ct_code].append(f"{d['domain']}.{v['name']}")

    unique_vars = len(var_index)

    # Split into shared (2+ domains) and domain-specific (1 domain)
    shared_vars = {}
    specific_vars = defaultdict(list)  # domain -> list of (var_name, entry)

    for var_name, entries in var_index.items():
        if len(entries) >= 2:
            shared_vars[var_name] = entries
        else:
            e = entries[0]
            specific_vars[e["domain"]].append((var_name, e))

    # Sort shared vars by domain count descending, then alphabetically
    shared_sorted = sorted(shared_vars.items(), key=lambda x: (-len(x[1]), x[0]))

    # Build domain lookup for full names and classes
    domain_info = {d["domain"]: (d["full_name"], d["class"]) for d in domains_data}
    all_domain_codes = sorted(domain_info.keys())

    # --- Generate markdown ---
    lines = []
    today = date.today().isoformat()

    lines.append("# SDTM Variable Index")
    lines.append("")
    lines.append(f"> 自动生成，勿手动编辑 | 生成日期: {today}")
    lines.append(f"> 唯一变量数: {unique_vars} | 条目总数: {total_entries} | 覆盖域: {len(domains_data)}")
    lines.append("")
    lines.append("## 使用说明")
    lines.append("")
    lines.append("查询变量时，在本文件搜索变量名即可找到它出现在哪些 domain、属于什么角色/类型/核心程度。")
    lines.append("")
    lines.append("- **通用变量**（出现在 2+ 个域）：表头标注出现域数，域列表用逗号分隔")
    lines.append("- **领域专属变量**（仅 1 个域）：按域分组，直接标注所属域")
    lines.append("- **CT 交叉引用**：按 CDISC Controlled Terminology Code 分组，列出所有引用该 CT 的变量")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Section 1: Shared Variables ===
    lines.append(f"## 一、通用变量（出现在 2+ 个域，共 {len(shared_sorted)} 个）")
    lines.append("")
    lines.append("| 变量名 | 域数 | 出现的域 | Label | Type | Role | Core |")
    lines.append("|--------|------|---------|-------|------|------|------|")

    for var_name, entries in shared_sorted:
        domain_count = len(entries)
        domains_list = sorted(set(e["domain"] for e in entries))

        # For display: if all 63, say "所有域"; if most, list exclusions
        if domain_count == len(all_domain_codes):
            domains_str = "所有域"
        elif domain_count >= len(all_domain_codes) - 8:
            missing = sorted(set(all_domain_codes) - set(domains_list))
            domains_str = f"除 {', '.join(missing)} 外所有域"
        else:
            domains_str = ", ".join(domains_list)

        # Use the most common label/type/role/core
        label = entries[0]["label"]
        var_type = entries[0]["type"]
        role = entries[0]["role"]

        # Core: check if consistent
        cores = set(e["core"] for e in entries)
        if len(cores) == 1:
            core_str = cores.pop()
        else:
            # Most common core
            from collections import Counter
            core_counts = Counter(e["core"] for e in entries)
            most_common = core_counts.most_common(1)[0][0]
            others = [f"{c}({n})" for c, n in core_counts.most_common() if c != most_common]
            core_str = f"{most_common}*"

        lines.append(f"| {var_name} | {domain_count} | {domains_str} | {label} | {var_type} | {role} | {core_str} |")

    lines.append("")
    lines.append("> \\* Core 值后带星号表示该变量在不同域中 Core 不完全一致，以最常见值显示。")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Section 2: Domain-Specific Variables ===
    specific_count = sum(len(v) for v in specific_vars.values())
    lines.append(f"## 二、领域专属变量（仅 1 个域，共 {specific_count} 个），按域分组")
    lines.append("")

    for domain_code in all_domain_codes:
        if domain_code not in specific_vars:
            continue
        full_name, obs_class = domain_info[domain_code]
        vars_list = sorted(specific_vars[domain_code], key=lambda x: x[1].get("order", 999) if isinstance(x[1].get("order"), int) else 999)

        lines.append(f"### {domain_code} — {full_name} ({obs_class})")
        lines.append("")
        lines.append("| 变量名 | Label | Type | Role | Core | CT |")
        lines.append("|--------|-------|------|------|------|----|")

        for var_name, e in vars_list:
            ct_display = e["ct"] if e["ct"] else "—"
            lines.append(f"| {var_name} | {e['label']} | {e['type']} | {e['role']} | {e['core']} | {ct_display} |")

        lines.append("")

    lines.append("---")
    lines.append("")

    # === Section 3: CT Cross-Reference ===
    lines.append(f"## 三、CDISC Controlled Terminology 交叉引用（共 {len(ct_index)} 个 CT Code）")
    lines.append("")
    lines.append("| CT Code | 引用数 | 引用此 CT 的变量 (域.变量名) |")
    lines.append("|---------|--------|---------------------------|")

    for ct_code in sorted(ct_index.keys()):
        refs = sorted(ct_index[ct_code])
        ref_count = len(refs)
        # Truncate if too many
        if len(refs) > 15:
            refs_str = ", ".join(refs[:15]) + f" ... (共 {ref_count} 个)"
        else:
            refs_str = ", ".join(refs)
        lines.append(f"| {ct_code} | {ref_count} | {refs_str} |")

    lines.append("")

    return "\n".join(lines), total_entries, unique_vars, len(domains_data)


def main():
    # Discover all spec.md files
    spec_files = sorted(DOMAINS_DIR.glob("*/spec.md"))
    print(f"Found {len(spec_files)} spec.md files")

    # Parse all
    domains_data = []
    for f in spec_files:
        try:
            data = parse_spec_md(f)
            domains_data.append(data)
            print(f"  {data['domain']:10s} — {len(data['variables']):3d} variables")
        except Exception as e:
            print(f"  ERROR parsing {f}: {e}", file=sys.stderr)
            sys.exit(1)

    # Generate index
    content, total_entries, unique_vars, domain_count = generate_index(domains_data)

    # === Assertions (acceptance criteria C1-C5) ===
    assert total_entries == 1917, f"C1 FAIL: total entries {total_entries} != 1917"
    print(f"\n✓ C1 PASS: total entries = {total_entries}")

    assert unique_vars == 1523, f"C2 FAIL: unique vars {unique_vars} != 1523"
    print(f"✓ C2 PASS: unique vars = {unique_vars}")

    assert domain_count == 63, f"C3 FAIL: domain count {domain_count} != 63"
    print(f"✓ C3 PASS: domain count = {domain_count}")

    # C4: per-domain variable count matches
    for data in domains_data:
        spec_file = DOMAINS_DIR / data["domain"] / "spec.md"
        expected = data["variables"]
        # Re-count ### lines
        with open(spec_file) as fh:
            h3_count = sum(1 for line in fh if re.match(r"^### \S+\s*$", line))
        actual = len(expected)
        assert actual == h3_count, f"C4 FAIL: {data['domain']} has {actual} parsed vs {h3_count} ### lines"
    print(f"✓ C4 PASS: all 63 domains variable counts match")

    # C5: total from per-domain sums
    per_domain_sum = sum(len(d["variables"]) for d in domains_data)
    assert per_domain_sum == 1917, f"C5 FAIL: per-domain sum {per_domain_sum} != 1917"
    print(f"✓ C5 PASS: per-domain sum = {per_domain_sum}")

    # Write output
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    file_size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"\n✓ Written to {OUTPUT_FILE}")
    print(f"  File size: {file_size_kb:.1f} KB")


if __name__ == "__main__":
    main()
