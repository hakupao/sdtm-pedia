#!/usr/bin/env python3
"""SDTM Phase 6.5 v2 stage builder.

Aggregates a single v2 expansion stage (v2.1 .. v2.5):
  1. dispatch to the batch script (chapters / examples / terminology)
  2. tally tokens across output_v2/*.md via tiktoken (cl100k_base)
  3. patch system_prompt_v2.md with the stage-specific block
     (<!-- stage v2.X begin --> ... <!-- stage v2.X end -->)
  4. append the stage row to upload_manifest_v2.md (idempotent)
  5. write stage_v2.X_*.md evidence
  6. update _progress.json (completed_stages deduped)
  7. append a stage_done line to trace.jsonl

Usage:
    python3 scripts_v2/build_v2_stage.py --stage v2.1 [--dry-run]

Read-only over knowledge_base/. Idempotent: running the same stage twice
does not duplicate upload_manifest rows or completed_stages entries.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable

import tiktoken

# ---------------------------------------------------------------------------
# Constants / paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent  # ai_platforms/claude_projects/
REPO_ROOT = PROJECT_ROOT.parent.parent  # SDTM-compare/

OUTPUT_V2 = PROJECT_ROOT / "output_v2"
EVIDENCE_V2 = OUTPUT_V2 / "evidence_v2"
SCRIPTS_V2 = PROJECT_ROOT / "scripts_v2"

SYSTEM_PROMPT = OUTPUT_V2 / "system_prompt_v2.md"
UPLOAD_MANIFEST = OUTPUT_V2 / "upload_manifest_v2.md"
PROGRESS_JSON = EVIDENCE_V2 / "_progress.json"
TRACE_JSONL = EVIDENCE_V2 / "trace.jsonl"

ENCODING_NAME = "cl100k_base"

STAGE_MAP = {
    "v2.1": {
        "batch": 1,
        "script": "rebuild_chapters_full.py",
        "script_args": [],
        "output": "02_chapters.md",
        "target_tokens_total": 270000,
        "description": "chapters 全展开",
        "slug": "chapters",
        "prompt_block": (
            "- 02_chapters.md 已升级为**完整版**: ch01/ch02/ch03/ch08/ch10 撤销 v1 精简, ch04 保持全文 (6 章节 byte-exact 源)。\n"
            "- ch08 §8.3 / §8.4 含 RELREC + SUPP-- 完整规则, 跨域关联问题优先读 ch08 全文而非精简段。\n"
            "- 原 v1 \"ch01/02/03/08/10 精简\" 兜底句作废, 不再适用。"
        ),
    },
    "v2.2": {
        "batch": 2,
        "script": "extract_examples_data.py",
        "script_args": ["--tier", "high"],
        "output": "09_examples_data_high.md",
        "target_tokens_total": 360000,
        "description": "examples 高频域",
        "slug": "examples_high",
        "prompt_block": (
            "- 新增 09_examples_data_high.md: 25-28 个高频域 examples 数据表全量。\n"
            "- Examples 查询优先级: **09 (高频) > 07 (目录)**; 若 09 命中, 直接引用表格, 不再 fallback 源路径模板。"
        ),
    },
    "v2.3": {
        "batch": 3,
        "script": "extract_examples_data.py",
        "script_args": ["--tier", "others"],
        "output": "10_examples_data_others.md",
        "target_tokens_total": 490000,
        "description": "examples 剩余域",
        "slug": "examples_others",
        "prompt_block": (
            "- 新增 10_examples_data_others.md (或 10a/10b 拆分): 其余 ~35 域 examples 数据表。\n"
            "- Examples 查询优先级: **09 > 10 > 07**; 2 份数据表覆盖 63 域后, 边界模板 ① 不再适用于已覆盖域。"
        ),
    },
    "v2.4": {
        "batch": 4,
        "script": "extract_terminology_terms.py",
        "script_args": ["--tier", "high"],
        "output": "11a_terminology_high_core.md",
        "target_tokens_total": 840000,
        "description": "terminology 高频 codelist",
        "slug": "terminology_high",
        "prompt_block": (
            "- 新增 3 个文件 (按 terminology subdir 拆分): 11a_terminology_high_core.md / 11b_terminology_high_questionnaires.md / 11c_terminology_high_supp.md, 合计 top 200 codelist 完整 Term 值 (Code / Submission Value / Synonyms / Definition), 每 codelist header 附 `Related Domains:` 行列出引用它的 SDTM 域集合。\n"
            "- CT Code 查询优先级: **11a/11b/11c (full Term) > 08 (映射)**; 若 11* 命中, 直接列 Term, 不再 fallback 源路径模板。子目录路由: codelist 属 core/questionnaires/supplementary 由 `<!-- source: -->` 注释定位, 多数核心 SDTM codelist (NY/FREQ/Epoch/Unit/...) 在 11a, QRS Test Code/Name pair 在 11b, Device/Functional Test codelist 在 11c。"
        ),
    },
    "v2.5": {
        "batch": 5,
        "script": "extract_terminology_terms.py",
        "script_args": ["--tier", "mid"],
        "output": "12a_terminology_mid_core.md",
        "target_tokens_total": 1400000,
        "description": "terminology mid codelist",
        "slug": "terminology_mid",
        "prompt_block": (
            "- 新增 3 个文件 (按 terminology subdir 拆分, mid tier, rank 201-500, 300 codelist): 12a_terminology_mid_core.md / 12b_terminology_mid_questionnaires.md / 12c_terminology_mid_supp.md, 每 codelist 使用 3 列 Term 表 (Code / Submission Value / Definition ≤100 字符, 词边界截断), 不含 Synonyms / NCI Concept Description 链接, 每 codelist header 附 `Related Domains:` 行。\n"
            "- CT Code 查询优先级: **11a/11b/11c (high full Term 4 列) > 12a/12b/12c (mid 压缩 Term 3 列) > 08 (codelist 名称映射)**; 若 11* 命中优先引完整 Term; 若仅 12* 命中, 引 Term 并注明 Definition 为 100 字符压缩版 + Synonyms 不在本 tier (如需 Synonyms 必须指向源 `knowledge_base/terminology/**/*.md`); 08 仅作 fallback 名称查询。子目录路由沿用 11 系: core → a / questionnaires → b / supplementary → c。"
        ),
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return (
        _dt.datetime.now(_dt.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ")
    )


def _log(stage: str, msg: str) -> None:
    print(f"[Stage {stage}] {msg}")


def _iter_md(root: Path) -> Iterable[Path]:
    if not root.is_dir():
        return []
    return sorted(p for p in root.glob("*.md") if p.is_file())


def _count_tokens_dir(root: Path) -> tuple[int, list[tuple[Path, int]]]:
    encoder = tiktoken.get_encoding(ENCODING_NAME)
    total = 0
    rows: list[tuple[Path, int]] = []
    for md in _iter_md(root):
        text = md.read_text(encoding="utf-8", errors="strict")
        n = len(encoder.encode(text))
        total += n
        rows.append((md, n))
    return total, rows


def _load_progress() -> dict:
    if not PROGRESS_JSON.exists():
        raise FileNotFoundError(f"progress json missing: {PROGRESS_JSON}")
    return json.loads(PROGRESS_JSON.read_text(encoding="utf-8"))


def _save_progress(data: dict) -> None:
    PROGRESS_JSON.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _patch_system_prompt(stage: str, block: str) -> str:
    """Append or replace the <!-- stage vX.Y begin --> ... end --> block.

    Returns: 'appended' or 'replaced'.
    """
    text = SYSTEM_PROMPT.read_text(encoding="utf-8")
    begin_marker = f"<!-- stage {stage} begin -->"
    end_marker = f"<!-- stage {stage} end -->"
    wrapped = (
        f"\n{begin_marker}\n"
        f"### Stage {stage} 增量 ({STAGE_MAP[stage]['description']})\n\n"
        f"{block}\n"
        f"{end_marker}\n"
    )

    if begin_marker in text and end_marker in text:
        pre, _, rest = text.partition(begin_marker)
        _, _, post = rest.partition(end_marker)
        # drop a trailing newline before wrapped to avoid double blank lines
        new_text = pre.rstrip() + "\n" + wrapped.lstrip("\n") + post.lstrip("\n")
        SYSTEM_PROMPT.write_text(new_text, encoding="utf-8")
        return "replaced"

    if not text.endswith("\n"):
        text += "\n"
    SYSTEM_PROMPT.write_text(text + wrapped, encoding="utf-8")
    return "appended"


def _append_manifest_row(
    stage: str,
    file_count: int,
    total_tokens: int,
    target_tokens: int,
    description: str,
) -> str:
    """Append one row to the 阶段历史 table; idempotent.

    Returns: 'appended' or 'skipped'.
    """
    text = UPLOAD_MANIFEST.read_text(encoding="utf-8")
    # check if this stage already has a row
    if f"| {stage} |" in text:
        return "skipped"

    date_str = _dt.date.today().isoformat()
    ratio_pct = (total_tokens / target_tokens * 100) if target_tokens else 0.0
    row = (
        f"| {stage} | {date_str} | {file_count} | {total_tokens:,} | "
        f"{ratio_pct:.1f}% of {target_tokens:,} target | {description} |\n"
    )

    # find the header of "## 阶段历史" table and append after the last table row
    header = "## 阶段历史"
    idx = text.find(header)
    if idx == -1:
        # fallback: append to end
        if not text.endswith("\n"):
            text += "\n"
        UPLOAD_MANIFEST.write_text(text + row, encoding="utf-8")
        return "appended"

    # locate end of the 阶段历史 section (next "## " header or EOF)
    section_start = idx
    next_h2 = text.find("\n## ", idx + 1)
    section_end = next_h2 if next_h2 != -1 else len(text)
    section = text[section_start:section_end]
    # find the header row ("| 阶段 | ...") separator line ("|------|") and split
    lines = section.splitlines(keepends=True)
    # we insert row right before the next section (or EOF), trimming trailing blanks
    before = text[:section_end].rstrip() + "\n"
    after = text[section_end:]
    new_text = before + row + after
    UPLOAD_MANIFEST.write_text(new_text, encoding="utf-8")
    return "appended"


def _write_evidence(
    stage: str,
    slug: str,
    description: str,
    batch_result: str,
    total_tokens: int,
    file_count: int,
    token_rows: list[tuple[Path, int]],
    prompt_patch_result: str,
    manifest_row_result: str,
) -> Path:
    path = EVIDENCE_V2 / f"stage_{stage}_{slug}.md"
    lines = [
        f"# Stage {stage} — {description}",
        "",
        f"> Completed: {_now_iso()}",
        f"> Batch script: {STAGE_MAP[stage]['script']} "
        f"{' '.join(STAGE_MAP[stage]['script_args'])}",
        "",
        "## Inputs",
        f"- stage: `{stage}` (batch {STAGE_MAP[stage]['batch']})",
        f"- expected output file: `{STAGE_MAP[stage]['output']}`",
        f"- target cumulative tokens: {STAGE_MAP[stage]['target_tokens_total']:,}",
        "",
        "## Batch script result",
        f"- {batch_result}",
        "",
        "## Token tally (output_v2/*.md)",
        f"- files: {file_count}",
        f"- total tokens: {total_tokens:,}",
        "",
        "| file | tokens |",
        "|------|-------:|",
    ]
    for p, n in token_rows:
        lines.append(f"| {p.name} | {n:,} |")
    lines += [
        "",
        "## Meta updates",
        f"- system_prompt_v2.md: {prompt_patch_result}",
        f"- upload_manifest_v2.md: {manifest_row_result}",
        "",
        "## Next",
        "- 参照 PLAN_V2.md 对应 checkpoint 决定是否进入下一阶段.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _append_trace(stage: str, total_tokens: int, file_count: int, status: str) -> None:
    line = {
        "ts": _now_iso(),
        "event": "stage_done",
        "stage": stage,
        "total_tokens": total_tokens,
        "files": file_count,
        "status": status,
    }
    with TRACE_JSONL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def _run_batch_script(stage: str) -> tuple[bool, str]:
    """Run the batch script for this stage.

    Returns (ok, message). For v2.1/v2.2/v2.3, executes the corresponding
    extract script (only if it exists). For v2.4/v2.5 the terminology
    extract script is out-of-scope for Phase D/E; we stub and warn without
    crashing.

    rc=1 with expected output present is accepted as a "cap-warning"
    outcome (spec deviation ack'd by main controller).
    """
    info = STAGE_MAP[stage]
    script_name = info["script"]
    script_path = SCRIPTS_V2 / script_name

    # v2.4: extract_terminology_terms.py was implemented in Phase F (tier=high)
    # but v2.4 was already materialized via manual orchestration; we keep the
    # stub to avoid re-writing the 11a/11b/11c files on downstream reruns.
    if stage == "v2.4":
        return True, (
            f"stage v2.4 materialized manually in Phase F "
            f"(11a/11b/11c already on disk). Skipped batch execution to "
            "preserve byte-identical outputs."
        )

    if not script_path.exists():
        return False, (
            f"需先写 {script_name} (not found at {script_path})."
        )

    # Stage-specific extra args.
    extra_args: list[str] = []
    if stage == "v2.2":
        domain_list = EVIDENCE_V2 / "D1_domain_list.md"
        if not domain_list.exists():
            return False, f"need D1_domain_list.md for v2.2 (not at {domain_list})"
        extra_args = ["--domain-list", str(domain_list)]
    elif stage == "v2.3":
        exclude_list = EVIDENCE_V2 / "E1_exclude_list.txt"
        if not exclude_list.exists():
            return False, f"need E1_exclude_list.txt for v2.3 (not at {exclude_list})"
        extra_args = ["--exclude-list", str(exclude_list)]
    elif stage == "v2.5":
        codelist_list = EVIDENCE_V2 / "G1_codelist_mid.txt"
        if not codelist_list.exists():
            return False, f"need G1_codelist_mid.txt for v2.5 (not at {codelist_list})"
        extra_args = ["--list", str(codelist_list)]

    cmd = [sys.executable, str(script_path), *info["script_args"], *extra_args]
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return False, f"failed to launch {script_name}: {exc}"

    expected = OUTPUT_V2 / info["output"]

    # rc=1 with output present: likely cap-warning (e.g. EXCEED_HARD_CAP).
    # Accept as soft-pass; main controller has already done spec-deviation ack.
    if completed.returncode == 1 and expected.exists():
        stderr_tail = (
            completed.stderr.strip().splitlines()[-1:]
            if completed.stderr else ["(no stderr)"]
        )
        return True, (
            f"{script_name} rc=1 but produced {info['output']} — "
            f"cap-warning accepted. stderr tail: {stderr_tail}"
        )

    if completed.returncode != 0:
        return False, (
            f"{script_name} exited rc={completed.returncode}. "
            f"stderr tail: {completed.stderr.strip().splitlines()[-3:] if completed.stderr else '(empty)'}"
        )

    if not expected.exists():
        return False, (
            f"{script_name} ran rc=0 but expected output `{info['output']}` missing."
        )
    return True, f"{script_name} OK, produced {info['output']}."


# ---------------------------------------------------------------------------
# Main flow
# ---------------------------------------------------------------------------


def run_dry(stage: str) -> int:
    info = STAGE_MAP[stage]
    plan = [
        (1, f"parse --stage {stage} → batch {info['batch']} ({info['description']})"),
        (
            2,
            f"run batch script `{info['script']} "
            f"{' '.join(info['script_args'])}` → expect `{info['output']}`",
        ),
        (3, f"tally tokens over {OUTPUT_V2.relative_to(REPO_ROOT)}/*.md via tiktoken"),
        (
            4,
            f"patch {SYSTEM_PROMPT.relative_to(REPO_ROOT)} with "
            f"<!-- stage {stage} begin/end --> block",
        ),
        (
            5,
            f"append 阶段历史 row for {stage} to "
            f"{UPLOAD_MANIFEST.relative_to(REPO_ROOT)} (idempotent)",
        ),
        (
            6,
            f"write evidence `stage_{stage}_{info['slug']}.md` under "
            f"{EVIDENCE_V2.relative_to(REPO_ROOT)}",
        ),
        (
            7,
            f"update {PROGRESS_JSON.relative_to(REPO_ROOT)} "
            f"(current_stage={stage}, completed_stages += {stage})",
        ),
        (
            8,
            f"append stage_done trace to "
            f"{TRACE_JSONL.relative_to(REPO_ROOT)}",
        ),
    ]
    for n, desc in plan:
        print(f"[DRY] Step {n}: {desc}")
    _log(stage, "dry-run complete, no files modified.")
    return 0


def run_stage(stage: str) -> int:
    info = STAGE_MAP[stage]

    # Step 1
    _log(stage, f"dispatch → batch {info['batch']} ({info['description']})")

    # Step 2
    ok, msg = _run_batch_script(stage)
    _log(stage, f"batch script: {msg}")
    batch_result = msg
    if not ok:
        _log(stage, "abort: batch script prerequisite failed (no meta update).")
        return 2

    # Step 3
    total_tokens, token_rows = _count_tokens_dir(OUTPUT_V2)
    file_count = len(token_rows)
    _log(
        stage,
        f"tokens: {total_tokens:,} across {file_count} file(s) "
        f"(target {info['target_tokens_total']:,}).",
    )

    # Step 4
    prompt_patch = _patch_system_prompt(stage, info["prompt_block"])
    _log(stage, f"system_prompt_v2.md: {prompt_patch}")

    # Step 5
    manifest_row = _append_manifest_row(
        stage=stage,
        file_count=file_count,
        total_tokens=total_tokens,
        target_tokens=info["target_tokens_total"],
        description=info["description"],
    )
    _log(stage, f"upload_manifest_v2.md: {manifest_row}")

    # Step 6
    ev_path = _write_evidence(
        stage=stage,
        slug=info["slug"],
        description=info["description"],
        batch_result=batch_result,
        total_tokens=total_tokens,
        file_count=file_count,
        token_rows=token_rows,
        prompt_patch_result=prompt_patch,
        manifest_row_result=manifest_row,
    )
    _log(stage, f"evidence: wrote {ev_path.relative_to(REPO_ROOT)}")

    # Step 7
    progress = _load_progress()
    completed = list(progress.get("completed_stages", []))
    if stage not in completed:
        completed.append(stage)
    progress["completed_stages"] = completed
    progress["current_stage"] = stage
    progress["current_batch"] = info["batch"]
    progress["last_updated"] = _now_iso()
    _save_progress(progress)
    _log(stage, f"_progress.json: current_stage={stage}, completed={completed}")

    # Step 8
    _append_trace(stage, total_tokens, file_count, "PASS")
    _log(stage, "trace.jsonl: stage_done appended.")

    _log(stage, "done.")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Build a single SDTM Phase 6.5 v2 expansion stage."
    )
    parser.add_argument(
        "--stage",
        required=True,
        choices=sorted(STAGE_MAP.keys()),
        help="stage id, e.g. v2.1",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the 8-step plan and exit without modifying files",
    )
    args = parser.parse_args(argv)

    stage = args.stage
    if args.dry_run:
        return run_dry(stage)
    return run_stage(stage)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
