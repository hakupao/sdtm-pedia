#!/usr/bin/env python3
"""
Generate VARIABLE_INDEX.md from all spec.md files in knowledge_base/domains/.

Parses each spec.md to extract variable metadata, then produces a three-section
reverse index: shared variables, domain-specific variables, and CT cross-references.
"""

import re
import os
import sys
from collections import Counter, defaultdict
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


def extract_ct_codes(ct_string: str) -> list[str]:
    """Extract **every** CT code from a Controlled Terms value, in order.

    以前只取首码 (`re.match(r"(C\\d+)")`)。但 CT 字段可以列多个码表, 例如
    `PP.PPORRESU = "C85494; C128684; C128683; C128685; C128686"` —— 该变量对这几个
    码表都是真引用。只取首码的后果: 10 个多码变量的 18 个 (码, 变量) 引用对进不了
    §三, 且 12 个码表在 §三 **整行不存在** (C101834 / C114118 / C118971 / C120522-4 /
    C128683-6 / C150811 / C181169 / C111114)。

    §二 渲染的是 CT 全串, 于是同一个文件自相矛盾: §二 说 BS.BSSPEC 引用 C111114,
    §三 里 C111114 这一行根本没有。问"哪些变量引用 C128683"时检索不到, 而 section 名
    照常存在 —— 与被截断时同样看不出来。

    由 scripts/tests/test_kb_crossref_completeness.py 的
    test_section3_covers_every_ct_reference_declared_by_the_specs 钉住。
    """
    return re.findall(r"C\d+", ct_string or "")


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
            for ct_code in extract_ct_codes(v["ct"]):
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
    lines.append(f"> Auto-generated — do not edit manually | Generated: {today}")
    lines.append(f"> Unique variables: {unique_vars} | Total entries: {total_entries} | Domains covered: {len(domains_data)}")
    lines.append("")
    lines.append("## How to Use")
    lines.append("")
    lines.append("Search this file by variable name to find which domains the variable appears in, and its role, type, and core status.")
    lines.append("")
    lines.append("- **Common variables** (present in 2+ domains): the table lists the domain count and a comma-separated domain list.")
    lines.append("- **Domain-specific variables** (present in exactly 1 domain): grouped by domain.")
    lines.append("- **CT cross-reference**: grouped by CDISC Controlled Terminology code, listing every variable that references it.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Section 1: Shared Variables ===
    lines.append(f"## 1. Common Variables (present in 2+ domains, {len(shared_sorted)} total)")
    lines.append("")
    lines.append("| Variable | Domains | Appears In | Label | Type | Role | Core |")
    lines.append("|--------|------|---------|-------|------|------|------|")

    for var_name, entries in shared_sorted:
        domain_count = len(entries)
        domains_list = sorted(set(e["domain"] for e in entries))

        # For display: if all 63, say "All domains"; if most, list exclusions
        if domain_count == len(all_domain_codes):
            domains_str = "All domains"
        elif domain_count >= len(all_domain_codes) - 8:
            missing = sorted(set(all_domain_codes) - set(domains_list))
            domains_str = f"All domains except {', '.join(missing)}"
        else:
            domains_str = ", ".join(domains_list)

        # Use the most common label/type/role/core
        label = entries[0]["label"]
        var_type = entries[0]["type"]

        # Role: first domain's value, suffixed with '*' when domains disagree.
        # (Phase 6 V8 fix 45c8e9b was applied to the .md only; ported here so
        # regeneration reproduces it. Role keeps the first-entry value rather
        # than the most common one — that is what V8 signed off on.)
        role = entries[0]["role"]
        if len(set(e["role"] for e in entries)) > 1:
            role = f"{role}*"

        # Core: most common value, suffixed with '*' when domains disagree.
        cores = set(e["core"] for e in entries)
        if len(cores) == 1:
            core_str = cores.pop()
        else:
            core_counts = Counter(e["core"] for e in entries)
            core_str = f"{core_counts.most_common(1)[0][0]}*"

        lines.append(f"| {var_name} | {domain_count} | {domains_str} | {label} | {var_type} | {role} | {core_str} |")

    lines.append("")
    lines.append("> \\* An asterisk on Core means the Core value is not identical across domains; the most common value is shown.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Section 2: Domain-Specific Variables ===
    specific_count = sum(len(v) for v in specific_vars.values())
    lines.append(f"## 2. Domain-Specific Variables (1 domain only, {specific_count} total), grouped by domain")
    lines.append("")

    for domain_code in all_domain_codes:
        if domain_code not in specific_vars:
            continue
        full_name, obs_class = domain_info[domain_code]
        vars_list = sorted(specific_vars[domain_code], key=lambda x: x[1].get("order", 999) if isinstance(x[1].get("order"), int) else 999)

        lines.append(f"### {domain_code} — {full_name} ({obs_class})")
        lines.append("")
        lines.append("| Variable | Label | Type | Role | Core | CT |")
        lines.append("|--------|-------|------|------|------|----|")

        for var_name, e in vars_list:
            ct_display = e["ct"] if e["ct"] else "—"
            lines.append(f"| {var_name} | {e['label']} | {e['type']} | {e['role']} | {e['core']} | {ct_display} |")

        lines.append("")

    lines.append("---")
    lines.append("")

    # === Section 3: CT Cross-Reference ===
    lines.append(f"## 3. CDISC Controlled Terminology Cross-Reference ({len(ct_index)} CT Codes)")
    lines.append("")
    lines.append("| CT Code | References | Variables Referencing This CT (DOMAIN.VARIABLE) |")
    lines.append("|---------|--------|---------------------------|")

    for ct_code in sorted(ct_index.keys()):
        refs = sorted(ct_index[ct_code])
        ref_count = len(refs)
        # 不截断: 这张表是"哪些变量引用该码表"的唯一权威来源, 截到 15 条等于半张表。
        # 全展开对最宽的 C66742 (123 个引用) 也只有约 1.5K 字符; 全库 131.3 -> 133.8 KiB
        # (+2527 B), 复跑: `git show 6ed3d2b:knowledge_base/VARIABLE_INDEX.md | wc -c`
        # 对比 `wc -c < knowledge_base/VARIABLE_INDEX.md`。旧的 15 条上限买到的就是这
        # 2.5 KB, 代价是 9 个最需要它的宽码表答不全。
        # 检索侧判据看不出这个缺陷 (section 名不变), 故由
        # sdtm-rag/scripts/tests/test_kb_crossref_completeness.py 钉住 (含对 spec.md
        # 反建的外部锚 —— 只钉"条目数 == 自己声称的 N"是自洽的, 挡不住回归)。
        lines.append(f"| {ct_code} | {ref_count} | {', '.join(refs)} |")

    lines.append("")

    return "\n".join(lines), total_entries, unique_vars, len(domains_data)


def main():
    # Optional output override (used to diff a candidate against the committed file).
    out_file = Path(sys.argv[1]) if len(sys.argv) > 1 else OUTPUT_FILE

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
    out_file.write_text(content, encoding="utf-8")
    file_size_kb = out_file.stat().st_size / 1024
    print(f"\n✓ Written to {out_file}")
    print(f"  File size: {file_size_kb:.1f} KB")


if __name__ == "__main__":
    main()
