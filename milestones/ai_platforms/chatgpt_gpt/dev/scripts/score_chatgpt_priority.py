#!/usr/bin/env python3
"""Rule E 打分脚本 — ChatGPT GPTs Phase 3 优先级排序.

实现 PLAN.md §3.1 v1.1 **加法公式**:

    score(file) = (priority_weight × coverage_weight) + audience_bonus + novelty_bonus

字段来自 PLAN.md §3.2 v1.1 表 (9 合并文件清单, 每文件含
coverage / priority / audience / novelty 四维).

产物:
- stdout ranked list (score 从高到低)
- markdown 表到 `dev/evidence/score_phase3.md` (对齐 PLAN §3.2 + rank 列 + 时间戳)

floor 规则 (v1.1 简化): score < 0.15 取 0.15, 仅 coverage 严重降级兜底.

依据:
- PLAN.md §3.1 v1.1 (加法公式, 2026-04-20 主 session 修 MEDIUM)
- PLAN.md §3.2 v1.1 (score 数字: 01=02=3.4, 03=04=3.2, 05=1.5, 06=1.9, 07-09=1.2)
- PLAN.md §2.4 (9 合并文件清单)
- Rule E Q1=C / Q2=C / Q5=A (公开广播 + 混合受众 + 63 域全量)

Phase: 3 (执行) · Node: 1 (仅写脚本, 不执行)

Usage:
    python3 score_chatgpt_priority.py
    python3 score_chatgpt_priority.py --no-evidence  # 不写 score_phase3.md, 仅 stdout

Read-only (P5): 只读 PLAN 硬编码数据, 不碰 knowledge_base/.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent  # ai_platforms/chatgpt_gpt/
REPO_ROOT = PROJECT_ROOT.parent.parent  # SDTM-compare/
EVIDENCE_DIR = PROJECT_ROOT / "dev" / "evidence"
EVIDENCE_PATH = EVIDENCE_DIR / "score_phase3.md"

# ---------------------------------------------------------------------------
# 9 合并文件清单 + 四维字段 (硬编码, 来源 PLAN §2.4 + §3.2 v1.1)
# ---------------------------------------------------------------------------
# 字段说明:
#   coverage: 域覆盖完整度 (1.0 全量 / 0.7 缺 1-2 / 0.3 缺 >5)
#   priority: P0=3.0 / P1=1.5 / P2=1.0 (骨架 / 辅助 / 查表)
#   audience: 新手友好含导航/定义/示例 → +0.2; 仅专家 → +0.0
#   novelty : 命中公开受众题相关 → +0.2; 仅内部查询 → +0.0
# 语义锚点见 PLAN §3.1 v1.1 表 (audience/novelty bonus 解释)

FILES: list[dict] = [
    {
        "id": "01",
        "file": "navigation.md",
        "coverage": 1.0,
        "priority": 3.0,    # P0
        "priority_tag": "P0",
        "audience": 0.2,    # 导航对新手极友好
        "novelty": 0.2,     # "SDTM 是什么" 公开题命中
        "batch": 1,
    },
    {
        "id": "02",
        "file": "chapters_all.md",
        "coverage": 1.0,
        "priority": 3.0,    # P0
        "priority_tag": "P0",
        "audience": 0.2,    # 概念章节对新手友好
        "novelty": 0.2,     # 公开受众会问概念
        "batch": 1,
    },
    {
        "id": "03",
        "file": "model_all.md",
        "coverage": 1.0,
        "priority": 3.0,    # P0
        "priority_tag": "P0",
        "audience": 0.2,    # model 概念 (Obs class 等) 新手可消费
        "novelty": 0.0,     # 公开受众少问模型结构
        "batch": 1,
    },
    {
        "id": "04",
        "file": "domain_specs_all.md",
        "coverage": 1.0,
        "priority": 3.0,    # P0
        "priority_tag": "P0",
        "audience": 0.0,    # spec 变量表主要是专家查询
        "novelty": 0.2,     # Starter 命中 (AE/PC/PP 等)
        "batch": 1,
    },
    {
        "id": "05",
        "file": "assumptions_all.md",
        "coverage": 1.0,
        "priority": 1.5,    # P1
        "priority_tag": "P1",
        "audience": 0.0,    # assumptions 深层, 非新手入口
        "novelty": 0.0,     # 不直接命中公开题
        "batch": 2,
    },
    {
        "id": "06",
        "file": "examples_all.md",
        "coverage": 1.0,
        "priority": 1.5,    # P1
        "priority_tag": "P1",
        "audience": 0.2,    # examples 对新手理解场景关键
        "novelty": 0.2,     # Starter "关联/场景" 题命中
        "batch": 2,
    },
    # 07-09 视作三个独立条目 (PLAN §2.4 三行 terminology)
    {
        "id": "07",
        "file": "terminology_core.md",
        "coverage": 1.0,
        "priority": 1.0,    # P2
        "priority_tag": "P2",
        "audience": 0.2,    # 部分核心 CT (NY/FREQ) 新手可消费
        "novelty": 0.0,     # 公开受众少问 codelist
        "batch": 2,
    },
    {
        "id": "08",
        "file": "terminology_questionnaires.md",
        "coverage": 1.0,
        "priority": 1.0,    # P2
        "priority_tag": "P2",
        "audience": 0.2,    # QRS 代码对新手仍需查表, 但 Q8 查询场景加成
        "novelty": 0.0,     # 非公开题触发
        "batch": 2,
    },
    {
        "id": "09",
        "file": "terminology_supplementary.md",
        "coverage": 1.0,
        "priority": 1.0,    # P2
        "priority_tag": "P2",
        "audience": 0.2,    # 补充 CT 同上
        "novelty": 0.0,     # 非公开题触发
        "batch": 2,
    },
]

FLOOR = 0.15

# ---------------------------------------------------------------------------
# 计分
# ---------------------------------------------------------------------------


def compute_score(entry: dict) -> dict:
    """对单文件按 v1.1 加法公式计分.

    公式: score = (priority × coverage) + audience + novelty
    floor: score < 0.15 → 0.15
    """
    core = entry["priority"] * entry["coverage"]
    raw = core + entry["audience"] + entry["novelty"]
    score = max(raw, FLOOR)
    return {
        **entry,
        "core": core,
        "raw_score": raw,
        "score": score,
        "floored": raw < FLOOR,
    }


def rank_files() -> list[dict]:
    """计分 + 排序 (score 降序, id 升序 tiebreak, 稳定 & idempotent)."""
    scored = [compute_score(e) for e in FILES]
    scored.sort(key=lambda r: (-r["score"], r["id"]))
    return scored


# ---------------------------------------------------------------------------
# 输出
# ---------------------------------------------------------------------------


def print_ranked(scored: list[dict]) -> None:
    for i, r in enumerate(scored, start=1):
        print(
            f"{i:>2}. {r['id']}_{r['file']} "
            f"score={r['score']:.2f} "
            f"(priority={r['priority_tag']} "
            f"coverage={r['coverage']:.1f} "
            f"+audience={r['audience']:.1f} "
            f"+novelty={r['novelty']:.1f})"
        )


def write_evidence(scored: list[dict], path: Path) -> None:
    """写 markdown 表到 score_phase3.md (对齐 PLAN §3.2 + rank 列 + timestamp)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# ChatGPT GPTs Phase 3 打分结果 (v1.1 加法公式)",
        "",
        f"> Generated: {ts}",
        "> Script: `dev/scripts/score_chatgpt_priority.py`",
        "> Formula: `score = (priority_weight × coverage_weight) + audience_bonus + novelty_bonus`",
        "> Floor: score < 0.15 → 0.15 (仅 coverage 严重降级兜底)",
        "> Source: PLAN.md §3.1 v1.1 + §3.2 v1.1 + §2.4 (9 合并文件清单)",
        "",
        "## 打分明细 (按 score 降序)",
        "",
        "| rank | # | 文件 | coverage | priority | 核心 (pri×cov) | audience | novelty | score | 批次 |",
        "|:----:|:-:|------|:--------:|:--------:|:--------------:|:--------:|:-------:|:-----:|:----:|",
    ]
    for i, r in enumerate(scored, start=1):
        lines.append(
            f"| {i} | {r['id']} | {r['file']} | "
            f"{r['coverage']:.1f} | {r['priority_tag']} ({r['priority']:.1f}) | "
            f"{r['core']:.1f} | +{r['audience']:.1f} | +{r['novelty']:.1f} | "
            f"**{r['score']:.1f}** | {r['batch']} |"
        )

    lines += [
        "",
        "## 排序语义验证 (v1.1)",
        "",
        "- P0 核心 (01/02=3.4 > 03=04=3.2) > P1 辅助 (06=1.9 > 05=1.5) > P2 查表 (07-09=1.2)",
        "- 与 PLAN §3.2 数字应精确一致 (Phase 2 reviewer 认可).",
        "- floor 规则本次未触发 (所有文件 coverage=1.0, 核心分 ≥ 1.0).",
        "",
        "## Phase 3 Node 1 note",
        "",
        "- 本脚本为 Node 1 产出的静态打分器 (字段硬编码 PLAN §3.2 v1.1).",
        "- 若后续 coverage 因合并失败降级 (0.7 / 0.3), 本脚本可直接重跑, 会自动反映降级 score 与 floor 行为.",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Rule E score (PLAN §3.1 v1.1 加法公式) for ChatGPT GPTs 9 合并文件."
    )
    parser.add_argument(
        "--no-evidence",
        action="store_true",
        help="仅 stdout, 不写 dev/evidence/score_phase3.md",
    )
    args = parser.parse_args(argv)

    scored = rank_files()
    print_ranked(scored)

    if not args.no_evidence:
        write_evidence(scored, EVIDENCE_PATH)
        print(f"\n[evidence] wrote {EVIDENCE_PATH.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
