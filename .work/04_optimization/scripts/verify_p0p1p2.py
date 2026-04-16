#!/usr/bin/env python3
"""
Phase 6 P0/P1/P2 验证脚本 (V1-V5)
按 p0p1p2_verification_plan.md 方案执行程序化验证
"""

import os
import re
import subprocess
import json
from pathlib import Path
from collections import defaultdict

# 项目根目录
ROOT = Path(__file__).resolve().parents[3]  # .work/04_optimization/scripts/ → project root
KB = ROOT / "knowledge_base"
DOMAINS_DIR = KB / "domains"

# Git commit before Cross References were added to spec.md
COMMIT_BEFORE_XREF = "86d761a"


def get_all_spec_files():
    """获取全部 63 个 spec.md 文件路径"""
    specs = sorted(DOMAINS_DIR.glob("*/spec.md"))
    return specs


def extract_cross_ref_section(filepath):
    """提取 spec.md 中 ## Cross References 及之后的全部内容"""
    text = filepath.read_text(encoding="utf-8")
    match = re.search(r'^## Cross References\s*$', text, re.MULTILINE)
    if not match:
        return None, text, ""
    start = match.start()
    return start, text[:start], text[start:]


def extract_links_from_text(text, source_file):
    """从 Markdown 文本中提取所有 [text](path) 链接，返回 (link_text, raw_path, resolved_path) 列表"""
    links = []
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', text):
        link_text = m.group(1)
        raw_path = m.group(2)
        # 跳过锚点链接和外部链接
        if raw_path.startswith('#') or raw_path.startswith('http'):
            continue
        # 去掉锚点部分
        clean_path = raw_path.split('#')[0]
        if not clean_path:
            continue
        resolved = (source_file.parent / clean_path).resolve()
        links.append((link_text, raw_path, resolved, source_file))
    return links


# ============================================================
# V1: 链接完整性
# ============================================================
def verify_v1_link_integrity():
    print("=" * 60)
    print("V1: Link Integrity — 链接完整性")
    print("=" * 60)

    all_links = []
    broken = []

    # 1. ROUTING.md
    routing = KB / "ROUTING.md"
    if routing.exists():
        text = routing.read_text(encoding="utf-8")
        links = extract_links_from_text(text, routing)
        all_links.extend(links)

    # 2. VARIABLE_INDEX.md
    varindex = KB / "VARIABLE_INDEX.md"
    if varindex.exists():
        text = varindex.read_text(encoding="utf-8")
        links = extract_links_from_text(text, varindex)
        all_links.extend(links)

    # 3. 63 个 spec.md 的 Cross References 段
    for spec in get_all_spec_files():
        _, _, xref_text = extract_cross_ref_section(spec)
        if xref_text:
            links = extract_links_from_text(xref_text, spec)
            all_links.extend(links)

    # 检查每个链接
    files_scanned = 2 + len(get_all_spec_files())  # ROUTING + VARINDEX + specs
    for link_text, raw_path, resolved, source in all_links:
        if not resolved.exists():
            broken.append((source.relative_to(ROOT), raw_path, link_text))

    # 报告
    print(f"Scanned: {files_scanned} files, {len(all_links)} links")
    if broken:
        print(f"FAIL: {len(broken)} broken links found:")
        for src, path, text in broken:
            print(f"  [{text}]({path}) in {src}")
    else:
        print(f"PASS: {len(all_links)}/{len(all_links)} links valid")
    print(f"Broken: {len(broken)}")
    print()
    return len(broken) == 0


# ============================================================
# V2: CT Code 双向一致性
# ============================================================
def verify_v2_ct_consistency():
    print("=" * 60)
    print("V2: CT Code Consistency — CT 双向一致性")
    print("=" * 60)

    total_missing_in_xref = 0
    total_extra_in_xref = 0
    domain_results = []

    for spec in get_all_spec_files():
        domain = spec.parent.name
        text = spec.read_text(encoding="utf-8")

        # 正向: 从变量定义提取 CT Codes (排除 MedDRA 等非 C-code)
        # 注: CT 字段可能包含多个分号分隔的 Code，如 "C85494; C128684; C128683"
        spec_ct_codes = set()
        for m in re.finditer(r'- \*\*Controlled Terms:\*\*\s*(.+)', text):
            ct_field = m.group(1)
            for code in re.findall(r'C\d{4,}', ct_field):
                spec_ct_codes.add(code)

        # 从 Cross References CT 段提取 CT Codes
        xref_ct_codes = set()
        _, _, xref_text = extract_cross_ref_section(spec)
        if xref_text:
            for m in re.finditer(r'\(C(\d{4,})\)', xref_text):
                xref_ct_codes.add(f"C{m.group(1)}")

        missing = spec_ct_codes - xref_ct_codes  # spec 有但 xref 没有
        extra = xref_ct_codes - spec_ct_codes      # xref 有但 spec 没有

        status = "✓" if not missing and not extra else "✗"
        spec_count = len(spec_ct_codes)
        xref_count = len(xref_ct_codes)

        domain_results.append((domain, spec_count, xref_count, missing, extra, status))
        total_missing_in_xref += len(missing)
        total_extra_in_xref += len(extra)

    # 报告
    fail_domains = [d for d in domain_results if d[5] == "✗"]
    pass_count = len(domain_results) - len(fail_domains)

    for domain, sc, xc, missing, extra, status in domain_results:
        detail = f"spec→xref {sc - len(missing)}/{sc}, xref→spec {xc - len(extra)}/{xc}"
        print(f"  {domain}: {detail} {status}")
        if missing:
            print(f"    Missing in xref: {missing}")
        if extra:
            print(f"    Extra in xref: {extra}")

    result = "PASS" if not fail_domains else "FAIL"
    print(f"\n{result}: {pass_count}/{len(domain_results)} domains consistent")
    print(f"Missing in xref: {total_missing_in_xref}")
    print(f"Extra in xref: {total_extra_in_xref}")
    print()
    return len(fail_domains) == 0


# ============================================================
# V3: 变量计数一致性
# ============================================================
def verify_v3_variable_counts():
    print("=" * 60)
    print("V3: Variable Counts — 变量计数一致性")
    print("=" * 60)

    # 从 VARIABLE_INDEX.md 构建 domain → set(变量名) 映射
    varindex = KB / "VARIABLE_INDEX.md"
    vi_text = varindex.read_text(encoding="utf-8")

    # 解析通用变量 (§一)
    index_vars = defaultdict(set)

    # 通用变量表: | STUDYID | 63 | 所有域 | ...
    # 需要解析 "出现的域" 列
    in_common = False
    in_domain_section = False
    current_domain = None

    for line in vi_text.splitlines():
        # 检测通用变量区
        if "## 一、通用变量" in line:
            in_common = True
            in_domain_section = False
            continue
        if "## 二、领域专属变量" in line:
            in_common = False
            in_domain_section = True
            continue
        if "## 三、" in line:
            in_domain_section = False
            continue

        if in_common:
            # 表格行: | VARNAME | N | 域列表 | ...
            m = re.match(r'^\|\s*([A-Z][A-Z0-9]+)\s*\|.*\|.*\|', line)
            if m:
                varname = m.group(1)
                # 解析域列表
                cols = [c.strip() for c in line.split('|')]
                if len(cols) >= 4:
                    domains_str = cols[3]  # 出现的域
                    if "除" in domains_str and "外" in domains_str:
                        # "除 X, Y, Z 外所有域" — 排除特定域
                        excluded = set(re.findall(r'[A-Z]{2,}', domains_str.split("外")[0]))
                        for spec in get_all_spec_files():
                            d = spec.parent.name
                            if d not in excluded:
                                index_vars[d].add(varname)
                    elif "所有域" in domains_str:
                        # 纯"所有域"（无排除）
                        for spec in get_all_spec_files():
                            d = spec.parent.name
                            index_vars[d].add(varname)
                    else:
                        for d in re.findall(r'[A-Z]{2,}', domains_str):
                            index_vars[d].add(varname)

        if in_domain_section:
            # 域标题: ### AE — Adverse Events (Events)
            dm = re.match(r'^###\s+([A-Z]{2,})\s+—', line)
            if dm:
                current_domain = dm.group(1)
                continue
            # 变量行: | AESEQ | ...
            if current_domain:
                vm = re.match(r'^\|\s*([A-Z][A-Z0-9]+)\s*\|', line)
                if vm:
                    varname = vm.group(1)
                    if varname not in ("变量名",):  # 跳过表头
                        index_vars[current_domain].add(varname)

    # 从每个 spec.md 提取变量名
    total_spec = 0
    total_index = 0
    mismatches = []

    for spec in get_all_spec_files():
        domain = spec.parent.name
        text = spec.read_text(encoding="utf-8")

        # 提取 ### VARNAME 行 (在 Cross References 之前)
        xref_pos, pre_xref, _ = extract_cross_ref_section(spec)
        target_text = pre_xref if xref_pos is not None else text

        spec_vars = set()
        for m in re.finditer(r'^### ([A-Z][A-Z0-9]+)\s*$', target_text, re.MULTILINE):
            spec_vars.add(m.group(1))

        idx_vars = index_vars.get(domain, set())
        only_in_spec = spec_vars - idx_vars
        only_in_index = idx_vars - spec_vars
        status = "✓" if not only_in_spec and not only_in_index else "✗"

        total_spec += len(spec_vars)
        total_index += len(idx_vars)

        print(f"  {domain}: spec={len(spec_vars)}, index={len(idx_vars)} {status}")
        if only_in_spec:
            print(f"    Only in spec: {only_in_spec}")
            mismatches.append((domain, "only_in_spec", only_in_spec))
        if only_in_index:
            print(f"    Only in index: {only_in_index}")
            mismatches.append((domain, "only_in_index", only_in_index))

    result = "PASS" if not mismatches else "FAIL"
    print(f"\n{result}: {len(get_all_spec_files()) - len(mismatches)}/{len(get_all_spec_files())} domains match")
    print(f"Total: spec={total_spec}, index={total_index}")
    print()
    return len(mismatches) == 0


# ============================================================
# V4: 域归类正确性
# ============================================================
def verify_v4_class_grouping():
    print("=" * 60)
    print("V4: Class Grouping — 域归类正确性")
    print("=" * 60)

    # 从每个 spec.md 提取 class
    domain_class = {}
    for spec in get_all_spec_files():
        domain = spec.parent.name
        text = spec.read_text(encoding="utf-8")
        m = re.search(r'>\s*Class:\s*([^|]+)', text)
        if m:
            domain_class[domain] = m.group(1).strip()

    # 按 class 分组
    class_domains = defaultdict(set)
    for d, c in domain_class.items():
        class_domains[c].add(d)

    # 从 Cross References 提取 Same class 列表
    errors = []
    for spec in get_all_spec_files():
        domain = spec.parent.name
        _, _, xref_text = extract_cross_ref_section(spec)
        if not xref_text:
            errors.append((domain, "No Cross References section"))
            continue

        m = re.search(r'\*\*Same class \(([^)]+)\):\*\*\s*(.*)', xref_text)
        if not m:
            # 某些域可能是唯一的 class 成员，没有 same class 行
            my_class = domain_class.get(domain, "?")
            if len(class_domains.get(my_class, set())) > 1:
                errors.append((domain, f"Missing 'Same class' line, class={my_class} has {len(class_domains[my_class])} members"))
            continue

        xref_class = m.group(1).strip()
        xref_domains_str = m.group(2).strip()
        xref_listed = set(re.findall(r'[A-Z]{2,}', xref_domains_str))

        my_class = domain_class.get(domain, "?")

        # 验证 1: xref 中声明的 class 与 spec.md 头部一致
        if xref_class != my_class:
            errors.append((domain, f"Class mismatch: spec='{my_class}', xref='{xref_class}'"))

        # 验证 2: xref 列出的同 class 域应该是 class_domains[my_class] - {domain}
        expected = class_domains.get(my_class, set()) - {domain}
        if xref_listed != expected:
            missing = expected - xref_listed
            extra = xref_listed - expected
            if missing:
                errors.append((domain, f"Same class missing: {missing}"))
            if extra:
                errors.append((domain, f"Same class extra: {extra}"))

    # 报告
    print("Class grouping from spec.md headers:")
    for cls in sorted(class_domains.keys()):
        domains = sorted(class_domains[cls])
        print(f"  {cls}: {{{', '.join(domains)}}} — {len(domains)} domains")

    print()
    if errors:
        print(f"FAIL: {len(errors)} errors found:")
        for domain, msg in errors:
            print(f"  {domain}: {msg}")
    else:
        print(f"PASS: {len(class_domains)}/{len(class_domains)} classes correct")
    print()
    return len(errors) == 0


# ============================================================
# V5: 回归检查（全量 63 文件）
# ============================================================
def verify_v5_regression_check():
    print("=" * 60)
    print("V5: Regression Check — 回归检查（全量）")
    print("=" * 60)

    errors = []
    specs = get_all_spec_files()

    for spec in specs:
        domain = spec.parent.name
        rel_path = spec.relative_to(ROOT)

        # 当前文件内容
        text = spec.read_text(encoding="utf-8")
        xref_pos, pre_xref, xref_text = extract_cross_ref_section(spec)

        # 检查 1: Cross References 段存在
        if xref_pos is None:
            errors.append((domain, "No Cross References section"))
            continue

        # 检查 2: Cross References 段在文件最末尾（段后不应有其他 ## 标题）
        after_xref = xref_text
        other_h2 = re.findall(r'^## (?!Cross References)', after_xref, re.MULTILINE)
        if other_h2:
            errors.append((domain, f"Content after Cross References: {other_h2}"))

        # 检查 3: Cross References 之前的内容与 git 历史一致
        # 注: 追加 Cross References 时在前面加了空行分隔符，这是预期行为，不算内容变更
        try:
            result = subprocess.run(
                ["git", "show", f"{COMMIT_BEFORE_XREF}:{rel_path}"],
                capture_output=True, text=True, cwd=ROOT
            )
            if result.returncode == 0:
                original = result.stdout
                # 去掉尾部分隔符(---) 和空白行后比较实际内容
                # Cross Ref 生成脚本在段前添加了 "---\n\n" 视觉分隔符，属于预期行为
                pre_cleaned = re.sub(r'\n---\s*$', '', pre_xref.rstrip())
                pre_lines = pre_cleaned.rstrip().splitlines()
                orig_lines = original.rstrip().splitlines()
                if pre_lines != orig_lines:
                    # 找具体差异
                    if len(pre_lines) != len(orig_lines):
                        errors.append((domain, f"Line count changed: original={len(orig_lines)}, current_pre_xref={len(pre_lines)}"))
                    else:
                        diff_lines = [i+1 for i, (a, b) in enumerate(zip(pre_lines, orig_lines)) if a != b]
                        if diff_lines:
                            errors.append((domain, f"Content differs at lines: {diff_lines[:5]}..."))
            else:
                # 文件在该 commit 中不存在（不应发生）
                errors.append((domain, f"Not found in git commit {COMMIT_BEFORE_XREF}"))
        except Exception as e:
            errors.append((domain, f"Git error: {e}"))

        status = "✓" if domain not in [e[0] for e in errors] else "✗"
        orig_lines = len(pre_xref.rstrip().splitlines())
        xref_start = orig_lines + 1
        print(f"  {domain}/spec.md: original={orig_lines} lines, xref starts at {xref_start} {status}")

    # 报告
    print()
    fail_count = len(set(e[0] for e in errors))
    pass_count = len(specs) - fail_count
    if errors:
        print(f"FAIL: {fail_count} files with issues:")
        for domain, msg in errors:
            print(f"  {domain}: {msg}")
    else:
        print(f"PASS: {len(specs)}/{len(specs)} files intact")
    print()
    return len(errors) == 0


# ============================================================
# Main
# ============================================================
def main():
    print("Phase 6 P0/P1/P2 Verification Script")
    print(f"Project root: {ROOT}")
    print(f"Knowledge base: {KB}")
    print(f"Spec files: {len(get_all_spec_files())}")
    print()

    results = {}
    results["V1"] = verify_v1_link_integrity()
    results["V2"] = verify_v2_ct_consistency()
    results["V3"] = verify_v3_variable_counts()
    results["V4"] = verify_v4_class_grouping()
    results["V5"] = verify_v5_regression_check()

    # 汇总
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for v, passed in results.items():
        status = "PASS ✓" if passed else "FAIL ✗"
        print(f"  {v}: {status}")

    all_pass = all(results.values())
    print()
    if all_pass:
        print("ALL PROGRAMMATIC CHECKS PASSED")
    else:
        failed = [v for v, p in results.items() if not p]
        print(f"FAILED: {', '.join(failed)}")

    return 0 if all_pass else 1


if __name__ == "__main__":
    exit(main())
