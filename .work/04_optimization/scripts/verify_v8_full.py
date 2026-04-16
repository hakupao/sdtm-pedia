#!/usr/bin/env python3
"""
V8 全量变量精度验证脚本
对 VARIABLE_INDEX.md 中全部 1917 条目逐字段与源 spec.md 比对
"""

import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[3]
KB = ROOT / "knowledge_base"
DOMAINS_DIR = KB / "domains"
VARINDEX = KB / "VARIABLE_INDEX.md"


def parse_all_specs():
    """从全部 63 个 spec.md 解析变量定义，返回 {domain: {varname: {field: value}}}"""
    specs = {}
    for spec_path in sorted(DOMAINS_DIR.glob("*/spec.md")):
        domain = spec_path.parent.name
        text = spec_path.read_text(encoding="utf-8")

        # 去掉 Cross References 段
        xref_match = re.search(r'^## Cross References', text, re.MULTILINE)
        if xref_match:
            text = text[:xref_match.start()]

        variables = {}
        # 按 ### VARNAME 切分
        var_blocks = re.split(r'^### ([A-Z][A-Z0-9]+)\s*$', text, flags=re.MULTILINE)
        # var_blocks: [preamble, var1_name, var1_body, var2_name, var2_body, ...]
        for i in range(1, len(var_blocks), 2):
            varname = var_blocks[i]
            body = var_blocks[i + 1] if i + 1 < len(var_blocks) else ""

            fields = {}
            for field_name, field_key in [
                ("Label", "label"),
                ("Type", "type"),
                ("Role", "role"),
                ("Core", "core"),
                ("Controlled Terms", "ct"),
            ]:
                m = re.search(rf'- \*\*{field_name}:\*\*[ \t]*(.*)', body)
                if m:
                    val = m.group(1).strip()
                    fields[field_key] = val if val else ""
                else:
                    fields[field_key] = ""

            variables[varname] = fields
        specs[domain] = variables
    return specs


def parse_variable_index():
    """解析 VARIABLE_INDEX.md，返回 common_vars 和 domain_vars"""
    text = VARINDEX.read_text(encoding="utf-8")

    common_vars = []  # [{name, domain_count, domains_str, label, type, role, core}]
    domain_vars = []  # [{name, domain, label, type, role, core, ct}]

    in_common = False
    in_domain = False
    current_domain = None

    for line in text.splitlines():
        if "## 一、通用变量" in line:
            in_common = True
            in_domain = False
            continue
        if "## 二、领域专属变量" in line:
            in_common = False
            in_domain = True
            continue
        if "## 三、" in line:
            in_domain = False
            continue

        if in_common:
            # | VARNAME | N | 域列表 | Label | Type | Role | Core |
            m = re.match(r'^\|\s*([A-Z][A-Z0-9]+)\s*\|', line)
            if m:
                cols = [c.strip() for c in line.split('|')]
                if len(cols) >= 8:
                    common_vars.append({
                        "name": cols[1],
                        "domain_count": cols[2],
                        "domains_str": cols[3],
                        "label": cols[4],
                        "type": cols[5],
                        "role": cols[6],
                        "core": cols[7],
                    })

        if in_domain:
            dm = re.match(r'^###\s+([A-Z]{2,})\s+—', line)
            if dm:
                current_domain = dm.group(1)
                continue
            if current_domain:
                vm = re.match(r'^\|\s*([A-Z][A-Z0-9]+)\s*\|', line)
                if vm:
                    cols = [c.strip() for c in line.split('|')]
                    if len(cols) >= 7 and cols[1] not in ("变量名",):
                        domain_vars.append({
                            "name": cols[1],
                            "domain": current_domain,
                            "label": cols[2],
                            "type": cols[3],
                            "role": cols[4],
                            "core": cols[5],
                            "ct": cols[6],
                        })

    return common_vars, domain_vars


def resolve_common_domains(domains_str, all_domains):
    """解析通用变量的域列表字符串，返回域集合"""
    if "除" in domains_str and "外" in domains_str:
        excluded = set(re.findall(r'[A-Z]{2,}', domains_str.split("外")[0]))
        return all_domains - excluded
    elif "所有域" in domains_str:
        return set(all_domains)
    else:
        return set(re.findall(r'[A-Z]{2,}', domains_str))


def normalize_ct(ct_str):
    """规范化 CT 字段用于比较"""
    if not ct_str or ct_str == "—" or ct_str == "-":
        return ""
    return ct_str.strip()


def main():
    print("V8 Full Variable Precision Verification")
    print("=" * 60)

    specs = parse_all_specs()
    all_domains = set(specs.keys())
    common_vars, domain_vars = parse_variable_index()

    print(f"Spec files parsed: {len(specs)} domains")
    print(f"Common variables in INDEX: {len(common_vars)}")
    print(f"Domain-specific variables in INDEX: {len(domain_vars)}")
    print()

    errors = []
    warnings = []
    total_checked = 0

    # ============================================================
    # Part 1: 通用变量验证 (24 个)
    # ============================================================
    print("--- Part 1: Common Variables ---")

    for cv in common_vars:
        varname = cv["name"]
        idx_domains = resolve_common_domains(cv["domains_str"], all_domains)

        # 验证 1: 域列表
        actual_domains = set()
        for domain, var_dict in specs.items():
            if varname in var_dict:
                actual_domains.add(domain)

        if idx_domains != actual_domains:
            missing = actual_domains - idx_domains
            extra = idx_domains - actual_domains
            if missing:
                errors.append(f"[COMMON] {varname}: missing domains in INDEX: {sorted(missing)}")
            if extra:
                errors.append(f"[COMMON] {varname}: extra domains in INDEX: {sorted(extra)}")

        # 验证 2: Label/Type — 与任意域匹配即可
        idx_label = cv["label"]
        idx_type = cv["type"]
        label_match = False
        type_match = False
        for domain in actual_domains:
            if varname in specs[domain]:
                sf = specs[domain][varname]
                if sf["label"] == idx_label:
                    label_match = True
                if sf["type"] == idx_type:
                    type_match = True

        if not label_match and actual_domains:
            sample_labels = set()
            for d in sorted(actual_domains)[:5]:
                if varname in specs[d]:
                    sample_labels.add(specs[d][varname]["label"])
            errors.append(f"[COMMON] {varname}: Label mismatch — INDEX='{idx_label}', specs have {sample_labels}")
        if not type_match and actual_domains:
            errors.append(f"[COMMON] {varname}: Type mismatch — INDEX='{idx_type}'")

        # 验证 3: Role/Core 星号一致性
        for field_key, field_name in [("role", "Role"), ("core", "Core")]:
            idx_val = cv[field_key]
            has_star = idx_val.endswith("*")
            base_val = idx_val.rstrip("*")

            # 收集所有域的实际值
            actual_values = set()
            for domain in actual_domains:
                if varname in specs[domain]:
                    actual_values.add(specs[domain][varname][field_key])

            if len(actual_values) > 1:
                # 跨域不一致 — 应有星号
                if not has_star:
                    errors.append(
                        f"[COMMON] {varname}: {field_name} varies across domains {actual_values} "
                        f"but INDEX shows '{idx_val}' without asterisk"
                    )
            elif len(actual_values) == 1:
                # 跨域一致 — 不应有星号，且值应匹配
                actual_val = list(actual_values)[0]
                if has_star:
                    warnings.append(
                        f"[COMMON] {varname}: {field_name} is uniform '{actual_val}' "
                        f"but INDEX has unnecessary asterisk '{idx_val}'"
                    )
                if base_val != actual_val:
                    errors.append(
                        f"[COMMON] {varname}: {field_name} mismatch — INDEX='{base_val}', spec='{actual_val}'"
                    )

        total_checked += 1

    print(f"  Checked: {len(common_vars)} common variables")

    # ============================================================
    # Part 2: 专属变量验证 (1499 个)
    # ============================================================
    print("--- Part 2: Domain-Specific Variables ---")

    domain_error_count = defaultdict(int)

    for dv in domain_vars:
        varname = dv["name"]
        domain = dv["domain"]
        total_checked += 1

        if domain not in specs:
            errors.append(f"[{domain}] {varname}: domain not found in spec files")
            continue
        if varname not in specs[domain]:
            errors.append(f"[{domain}] {varname}: variable not found in {domain}/spec.md")
            continue

        sf = specs[domain][varname]

        # Label
        if dv["label"] != sf["label"]:
            errors.append(f"[{domain}] {varname}: Label — INDEX='{dv['label']}', spec='{sf['label']}'")
            domain_error_count[domain] += 1

        # Type
        if dv["type"] != sf["type"]:
            errors.append(f"[{domain}] {varname}: Type — INDEX='{dv['type']}', spec='{sf['type']}'")
            domain_error_count[domain] += 1

        # Role
        if dv["role"] != sf["role"]:
            errors.append(f"[{domain}] {varname}: Role — INDEX='{dv['role']}', spec='{sf['role']}'")
            domain_error_count[domain] += 1

        # Core
        if dv["core"] != sf["core"]:
            errors.append(f"[{domain}] {varname}: Core — INDEX='{dv['core']}', spec='{sf['core']}'")
            domain_error_count[domain] += 1

        # CT
        idx_ct = normalize_ct(dv["ct"])
        spec_ct = normalize_ct(sf["ct"])
        if idx_ct != spec_ct:
            errors.append(f"[{domain}] {varname}: CT — INDEX='{dv['ct']}', spec='{sf['ct']}'")
            domain_error_count[domain] += 1

    print(f"  Checked: {len(domain_vars)} domain-specific variables")

    # ============================================================
    # Summary
    # ============================================================
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total entries checked: {total_checked}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print()

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  {e}")
        print()

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w}")
        print()

    if domain_error_count:
        print("Errors by domain:")
        for d in sorted(domain_error_count.keys()):
            print(f"  {d}: {domain_error_count[d]} field mismatches")
        print()

    if not errors:
        print("V8 FULL: PASS — all fields match across all 1917 entries")
        return 0
    else:
        print(f"V8 FULL: FAIL — {len(errors)} mismatches found")
        return 1


if __name__ == "__main__":
    exit(main())
