#!/usr/bin/env python3
"""Phase 6.5 Step 12 — build_all.py: Layer 1 verification + upload manifest.

Runs Layer 1 checks (PLAN.md §5.1 C1-C10) against the 10 content artifacts
already present in ai_platforms/claude_projects/output/ and emits
`output/upload_manifest.md` — a single sheet listing per-file token counts,
md5s, total tokens, C1-C10 PASS/FAIL, and the compression-rate summary
(§5.3).

Default behaviour: read-only on the 10 output .md files + sources; only
writes `upload_manifest.md`. Idempotent (driven by source mtime; rerun ->
byte-identical manifest). Never mutates any compressed output.

Optional `--refresh` reruns the 9 upstream compression scripts in dependency
order (Step 2-10) before computing the manifest. Skipped by default.

Usage:
    python3 build_all.py              # verify + emit manifest
    python3 build_all.py --refresh    # rerun 9 scripts, then verify

Exits 0 if C1-C10 all PASS, 1 otherwise (manifest still written).
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import tiktoken

ENCODING_NAME = "cl100k_base"
TOKEN_LIMIT = 195_000

ROOT = Path(__file__).resolve().parents[3]
KB = ROOT / "knowledge_base"
OUT_DIR = ROOT / "ai_platforms" / "claude_projects" / "output"
SCRIPTS = ROOT / "ai_platforms" / "claude_projects" / "scripts"
MANIFEST = OUT_DIR / "upload_manifest.md"

# Output files in upload order. system_prompt.md is the 10th artifact; it goes
# into Project Instructions, not Project Knowledge.
CONTENT_FILES = [
    ("00", "00_routing.md",            "Project Knowledge"),
    ("01", "01_index.md",              "Project Knowledge"),
    ("02", "02_chapters.md",           "Project Knowledge"),
    ("03", "03_model.md",              "Project Knowledge"),
    ("04", "04_variable_index.md",     "Project Knowledge"),
    ("05", "05_mega_spec.md",          "Project Knowledge"),
    ("06", "06_assumptions.md",        "Project Knowledge"),
    ("07", "07_examples_catalog.md",   "Project Knowledge"),
    ("08", "08_terminology_map.md",    "Project Knowledge"),
    ("--", "system_prompt.md",         "**粘贴到 Project Instructions**"),
]

# §5.3 baseline: source tokens per partition (PLAN §3.3 Appendix A).
SOURCE_TOKENS = {
    "00_routing.md":          2_657,
    "01_index.md":            5_032,
    "02_chapters.md":        60_525,
    "03_model.md":           17_573,
    "04_variable_index.md": 38_452,
    "05_mega_spec.md":     184_943,
    "06_assumptions.md":    53_708,
    "07_examples_catalog.md": 219_814,
    "08_terminology_map.md": 1_944_449,
}
SOURCE_LABELS = {
    "00_routing.md":          "ROUTING",
    "01_index.md":            "INDEX",
    "02_chapters.md":         "chapters",
    "03_model.md":            "model",
    "04_variable_index.md":   "VARIABLE_INDEX",
    "05_mega_spec.md":        "specs (63)",
    "06_assumptions.md":      "assumptions (63)",
    "07_examples_catalog.md": "examples (63)",
    "08_terminology_map.md":  "terminology (91)",
}
LOSSY_MAP = {
    "00_routing.md":          "否",
    "01_index.md":            "部分",
    "02_chapters.md":         "部分",
    "03_model.md":            "否",
    "04_variable_index.md":   "部分",
    "05_mega_spec.md":        "部分",
    "06_assumptions.md":      "部分",
    "07_examples_catalog.md": "有损 (目录化)",
    "08_terminology_map.md":  "有损 (映射表)",
}

REFRESH_STEPS = [
    ("Step 2  compress_index",       "compress_index.py"),
    ("Step 3  compress_chapters",    "compress_chapters.py"),
    ("Step 4  merge_model",          "merge_model.py"),
    ("Step 5  compress_var_index",   "compress_var_index.py"),
    ("Step 6  merge_specs",          "merge_specs.py"),
    ("Step 7  compress_assumptions", "compress_assumptions.py"),
    ("Step 8  catalog_examples",     "catalog_examples.py"),
    ("Step 9  catalog_terminology",  "catalog_terminology.py"),
    # Step 10 (copy ROUTING) + Step 11 (system_prompt.md) are not re-runnable
    # scripts; they are already materialised in OUT_DIR.
]


# ---------------------------------------------------------------------------
# utilities
# ---------------------------------------------------------------------------

def md5_of(path: Path) -> str:
    h = hashlib.md5()
    h.update(path.read_bytes())
    return h.hexdigest()


def count_tokens(enc: "tiktoken.Encoding", path: Path) -> int:
    return len(enc.encode(path.read_text(encoding="utf-8")))


def iso_mtime(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fmt(n: int) -> str:
    return f"{n:,}"


# ---------------------------------------------------------------------------
# Layer 1 checks (C1-C10)
# ---------------------------------------------------------------------------

def check_c1(total: int) -> tuple[bool, str, str]:
    std = f"≤{fmt(TOKEN_LIMIT)}"
    return total <= TOKEN_LIMIT, std, fmt(total)


def check_c2(text: str) -> tuple[bool, str, str]:
    """Mega Spec: 63 × `## XX — …` domain headings."""
    n = len(re.findall(r"(?m)^## [A-Z]{2,} —", text))
    return n == 63, "63 × `## XX —`", f"{n}"


def check_c3(text: str) -> tuple[bool, str, str]:
    """Assumptions: 63 × `## XX` (domain-code only, end of line)."""
    n = len(re.findall(r"(?m)^## [A-Z]{2,}$", text))
    return n == 63, "63 × `## XX`", f"{n}"


def check_c4(text: str) -> tuple[bool, str, str]:
    """Examples Catalog: 63 × `### XX` (domain-code only, end of line)."""
    n = len(re.findall(r"(?m)^### [A-Z]{2,}$", text))
    return n == 63, "63 × `### XX`", f"{n}"


def check_c5(text: str) -> tuple[bool, str, str]:
    """Mega Spec: 63 × `### Cross References`."""
    n = len(re.findall(r"(?m)^### Cross References", text))
    return n == 63, "63 × `### Cross References`", f"{n}"


def check_c6(chapters_text: str, ch04_src: Path) -> tuple[bool, str, str]:
    """ch04 verbatim retention ≥ 95% of source char count."""
    src_chars = len(ch04_src.read_text(encoding="utf-8"))
    # Extract ch04 segment from 02_chapters.md: from its source marker up to
    # the next chapter source marker (ch08) or EOF.
    start_pat = r"<!-- source: knowledge_base/chapters/ch04_general_assumptions\.md -->"
    next_pat = r"<!-- source: knowledge_base/chapters/"
    m = re.search(start_pat, chapters_text)
    if not m:
        return False, "ch04 ≥95% of source chars", "ch04 segment missing"
    tail = chapters_text[m.end():]
    m2 = re.search(next_pat, tail)
    segment = tail[:m2.start()] if m2 else tail
    pct = (len(segment) / src_chars) * 100.0 if src_chars else 0.0
    ok = pct >= 95.0
    return ok, "ch04 ≥95% of source chars", f"{pct:.2f}% ({len(segment)}/{src_chars} chars)"


def check_c7(routing_out: Path, routing_src: Path) -> tuple[bool, str, str]:
    """ROUTING.md copy is byte-identical (md5 match)."""
    out_md5 = md5_of(routing_out)
    src_md5 = md5_of(routing_src)
    return out_md5 == src_md5, "md5(out) == md5(src)", f"{out_md5[:10]} vs {src_md5[:10]}"


def check_c8(out_dir: Path) -> tuple[bool, str, str]:
    """Every merged content file (02-08) carries per-source provenance.

    Standard form is `<!-- source: knowledge_base/... -->`. For
    08_terminology_map.md the compact design (Step 9) replaces HTML comments
    with `### \`<file>.md\` -> <Domain>` section headings — one per source
    file — which serves the same traceability purpose; this pattern is also
    accepted.
    """
    merged = [
        "02_chapters.md",
        "03_model.md",
        "04_variable_index.md",
        "05_mega_spec.md",
        "06_assumptions.md",
        "07_examples_catalog.md",
        "08_terminology_map.md",
    ]
    heading_pat = re.compile(r"(?m)^### `[^`]+\.md` -> ")
    missing = []
    for name in merged:
        text = (out_dir / name).read_text(encoding="utf-8")
        has_comment = "<!-- source:" in text
        has_heading = bool(heading_pat.search(text)) if name == "08_terminology_map.md" else False
        if not (has_comment or has_heading):
            missing.append(name)
    ok = not missing
    detail = "all 7 merged files annotated" if ok else f"missing in: {', '.join(missing)}"
    return ok, "≥1 source-path annotation per merged file", detail


def check_c9(term_text: str) -> tuple[bool, str, str]:
    """Terminology map: ≥1000 codelist rows (C-code prefix)."""
    n = len(re.findall(r"(?m)^C[0-9]+ [EF] ", term_text))
    return n >= 1000, "≥1000 codelist rows", f"{n}"


def check_c10(out_dir: Path) -> tuple[bool, str, str]:
    """Exactly 11 .md files in output/ (9 content + routing + system_prompt
    + upload_manifest itself; manifest is excluded from the count to keep the
    spec stable: the spec talks about "9 内容 + routing + system_prompt" = 10
    *pre-manifest* artifacts, plus the manifest this script emits = 11)."""
    mds = sorted(p.name for p in out_dir.glob("*.md"))
    # Expected content artifacts (Step 2-11 outputs).
    expected = {name for _, name, _ in CONTENT_FILES}
    present = set(mds)
    # The manifest itself is allowed but not required when counting artifacts.
    content_present = present - {"upload_manifest.md"}
    extras = content_present - expected
    missing = expected - content_present
    ok = not extras and not missing
    if ok:
        detail = f"10 content .md present + upload_manifest.md = 11"
    else:
        problems = []
        if missing:
            problems.append(f"missing: {sorted(missing)}")
        if extras:
            problems.append(f"unexpected: {sorted(extras)}")
        detail = "; ".join(problems)
    return ok, "10 artifacts (9 content + routing + system_prompt)", detail


# ---------------------------------------------------------------------------
# manifest rendering
# ---------------------------------------------------------------------------

def render_manifest(file_rows, total_tokens, budget_left, checks, source_mtime, compression_rows, all_pass):
    lines: list[str] = []
    lines.append("# Upload Manifest — Phase 6.5 Claude Project")
    lines.append("")
    lines.append(f"> Generated: {source_mtime} (max mtime of output/*.md)")
    lines.append(f"> Source: ai_platforms/claude_projects/output/*.md")
    lines.append(f"> Built by: scripts/build_all.py (Layer 1 verifier)")
    lines.append("")
    lines.append("## 文件清单 (11 个)")
    lines.append("")
    lines.append("| 序 | 文件 | Tokens | md5 | 上传说明 |")
    lines.append("|----|------|-------:|-----|---------|")
    for idx, name, tokens, digest, note in file_rows:
        lines.append(f"| {idx} | {name} | {fmt(tokens)} | {digest} | {note} |")
    lines.append(f"| **合计** | — | **{fmt(total_tokens)}** | — | — |")
    lines.append("")
    pct_used = (total_tokens / TOKEN_LIMIT) * 100.0
    pct_buf = (budget_left / TOKEN_LIMIT) * 100.0
    lines.append(
        f"预算余量: {fmt(budget_left)} tokens "
        f"({pct_buf:.2f}%; limit={fmt(TOKEN_LIMIT)}, used={pct_used:.2f}%)"
    )
    lines.append("")
    lines.append("## Layer 1 检查 (§5.1)")
    lines.append("")
    lines.append("| # | 检查项 | 标准 | 实测 | 结果 |")
    lines.append("|---|-------|------|------|:-:|")
    for row in checks:
        cid, desc, std, actual, ok = row
        mark = "PASS" if ok else "FAIL"
        lines.append(f"| {cid} | {desc} | {std} | {actual} | {mark} |")
    lines.append("")
    n_pass = sum(1 for r in checks if r[4])
    lines.append(f"**Layer 1 结果: {n_pass}/{len(checks)} PASS**")
    lines.append("")
    lines.append("## 压缩率统计 (§5.3)")
    lines.append("")
    lines.append("| 分区 | 源 tokens | 压缩后 | 压缩率 | 是否有损 |")
    lines.append("|------|----------:|-------:|-------:|---------|")
    total_src = 0
    total_out = 0
    for label, src, out, rate, lossy in compression_rows:
        total_src += src
        total_out += out
        lines.append(f"| {label} | {fmt(src)} | {fmt(out)} | {rate} | {lossy} |")
    overall = ((total_src - total_out) / total_src * 100.0) if total_src else 0.0
    lines.append(
        f"| **合计** | **{fmt(total_src)}** | **{fmt(total_out)}** | "
        f"**{overall:.1f}%** | 部分有损 |"
    )
    lines.append("")
    lines.append("## 上传步骤 (手动, Step 13)")
    lines.append("")
    lines.append("1. 登录 Claude → 新建 Project \"SDTM Expert v3.4\"")
    lines.append("2. 在 **Project Instructions** 粘贴 `system_prompt.md` 全文")
    lines.append("3. 在 **Project Knowledge** 上传 9 个内容文件 (`00_routing.md` … `08_terminology_map.md`)")
    lines.append("4. 确认 Project 容量显示 ≈ 95–98%")
    lines.append("5. 执行 §5.2 T1-T8 测试矩阵（Step 14）")
    lines.append("")
    lines.append("## 若 Layer 1 FAIL")
    lines.append("")
    lines.append("- 找对应 Step 重跑脚本 (见 PLAN.md §7.4)")
    lines.append("- 修复后再跑 `python3 build_all.py` 刷新本 manifest")
    lines.append("- 不要在本脚本里做 hack 式绕过；失败信号属于上游 Step")
    lines.append("")
    if all_pass:
        reco = "READY_FOR_UPLOAD — Layer 1 全部 PASS, 可进入 Step 13"
    else:
        reco = "NEEDS_FIX — 有 C* 项 FAIL, 回到对应 Step 修复后重跑"
    lines.append(f"**Recommendation**: {reco}")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# refresh (optional)
# ---------------------------------------------------------------------------

def refresh_outputs() -> None:
    for label, script in REFRESH_STEPS:
        script_path = SCRIPTS / script
        if not script_path.exists():
            print(f"[refresh] skip {label}: {script} not found", file=sys.stderr)
            continue
        print(f"[refresh] running {label} ({script})", file=sys.stderr)
        proc = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            sys.stderr.write(proc.stdout)
            sys.stderr.write(proc.stderr)
            raise SystemExit(f"[refresh] FAIL: {script} exited {proc.returncode}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Phase 6.5 build_all + Layer 1")
    ap.add_argument(
        "--refresh",
        action="store_true",
        help="rerun Step 2-9 compression scripts before verifying",
    )
    args = ap.parse_args(argv)

    if args.refresh:
        refresh_outputs()

    # Sanity: every expected output file must exist.
    for _, name, _ in CONTENT_FILES:
        if not (OUT_DIR / name).exists():
            raise SystemExit(f"missing artifact: {OUT_DIR / name}")

    enc = tiktoken.get_encoding(ENCODING_NAME)

    # Gather per-file stats + mtime envelope.
    file_rows = []
    total_tokens = 0
    mtime_max = 0.0
    token_map: dict[str, int] = {}
    for idx, name, note in CONTENT_FILES:
        p = OUT_DIR / name
        tok = count_tokens(enc, p)
        token_map[name] = tok
        digest = md5_of(p)
        mtime_max = max(mtime_max, p.stat().st_mtime)
        total_tokens += tok
        file_rows.append((idx, name, tok, digest, note))

    budget_left = TOKEN_LIMIT - total_tokens

    # Load texts once for checks.
    t_chapters = (OUT_DIR / "02_chapters.md").read_text(encoding="utf-8")
    t_mega = (OUT_DIR / "05_mega_spec.md").read_text(encoding="utf-8")
    t_assum = (OUT_DIR / "06_assumptions.md").read_text(encoding="utf-8")
    t_ex = (OUT_DIR / "07_examples_catalog.md").read_text(encoding="utf-8")
    t_term = (OUT_DIR / "08_terminology_map.md").read_text(encoding="utf-8")

    checks_raw = [
        ("C1",  "总 tokens",                      *check_c1(total_tokens)),
        ("C2",  "Mega Spec 63 域覆盖",             *check_c2(t_mega)),
        ("C3",  "Assumptions 63 域覆盖",           *check_c3(t_assum)),
        ("C4",  "Examples Catalog 63 域覆盖",      *check_c4(t_ex)),
        ("C5",  "Cross References 保留",           *check_c5(t_mega)),
        ("C6",  "ch04 完整保留",                   *check_c6(t_chapters, KB / "chapters" / "ch04_general_assumptions.md")),
        ("C7",  "ROUTING 原样搬运",                *check_c7(OUT_DIR / "00_routing.md", KB / "ROUTING.md")),
        ("C8",  "源路径标注存在",                  *check_c8(OUT_DIR)),
        ("C9",  "Terminology 映射覆盖",            *check_c9(t_term)),
        ("C10", "输出文件数",                      *check_c10(OUT_DIR)),
    ]
    # Reorder tuple → (id, desc, std, actual, ok)
    checks = [(cid, desc, std, actual, ok) for (cid, desc, ok, std, actual) in checks_raw]
    all_pass = all(c[4] for c in checks)

    # Compression rows — 9 content files (system_prompt excluded: no source).
    compression_rows = []
    for _, name, _ in CONTENT_FILES:
        if name not in SOURCE_TOKENS:
            continue
        src = SOURCE_TOKENS[name]
        out = token_map[name]
        if src <= 0:
            rate = "n/a"
        else:
            # Compression percent: positive = shrank, negative = grew.
            # Convention (task §5.3): show a leading `+` when output grew
            # past the source (i.e. negative compression); show bare
            # percent for normal compression; "0%" when byte-identical.
            shrink = (src - out) / src * 100.0
            if out == src:
                rate = "0%"
            elif shrink < 0:
                rate = f"+{-shrink:.2f}%"
            else:
                rate = f"{shrink:.1f}%"
        compression_rows.append((SOURCE_LABELS[name], src, out, rate, LOSSY_MAP[name]))

    manifest = render_manifest(
        file_rows=file_rows,
        total_tokens=total_tokens,
        budget_left=budget_left,
        checks=checks,
        source_mtime=iso_mtime(mtime_max),
        compression_rows=compression_rows,
        all_pass=all_pass,
    )
    MANIFEST.write_text(manifest, encoding="utf-8")

    # Stdout summary (verifier consumption).
    n_pass = sum(1 for c in checks if c[4])
    print(f"[Step 12 DONE] output/upload_manifest.md: {MANIFEST.stat().st_size} bytes")
    print(f"Layer 1 C1-C10: {n_pass}/{len(checks)} PASS")
    print(f"Grand total tokens: {total_tokens} (limit {TOKEN_LIMIT}, buffer {budget_left})")
    for cid, desc, std, actual, ok in checks:
        mark = "PASS" if ok else "FAIL"
        print(f"  {cid} {mark}: {desc} | std={std} | actual={actual}")
    reco = "READY_FOR_UPLOAD" if all_pass else "NEEDS_FIX"
    print(f"Recommendation: {reco}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
