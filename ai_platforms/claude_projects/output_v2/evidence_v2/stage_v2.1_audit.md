# Stage v2.1 Audit (规则 A 强制 N=10 语义抽检)

> 审计日期: 2026-04-18
> 规则 A: writer/reviewer PASS ≠ 业务 PASS, 必须独立样本核验
> 批次: Batch 1 — chapters 全展开
> 产出: `ai_platforms/claude_projects/output_v2/02_chapters.md` (60,716 tokens)

## 1. 输入
- 6 章节源 (knowledge_base/chapters/):
  - `ch01_introduction.md` (102 行, 11,058 chars)
  - `ch02_fundamentals.md` (174 行, 12,192 chars)
  - `ch03_submitting_data.md` (130 行, 19,698 chars)
  - `ch04_general_assumptions.md` (1395 行, 124,560 chars)
  - `ch08_relationships.md` (439 行, 49,955 chars)
  - `ch10_appendices.md` (310 行, 28,823 chars)
- 源合计 2550 行 / 246,286 chars

## 2. Agent 调度
- **executor**: `oh-my-claudecode:executor` (model=opus)
  - prompt: `evidence_v2/subagent_prompts/C1_executor.md`
  - 产出 `scripts_v2/rebuild_chapters_full.py` + `output_v2/02_chapters.md`
  - 自报: `C1 executor DONE, tokens=60716, sources=6`
- **reviewer**: `oh-my-claudecode:code-reviewer` (model=opus)
  - prompt: `evidence_v2/subagent_prompts/C1_reviewer.md`
  - 结论 PASS (5-sample byte-exact + ch04 与 v1 baseline 等价)

**规则 D 合规**: executor 与 reviewer 为不同 subagent_type + 不同 session 隔离.

## 3. 产出
- `output_v2/02_chapters.md` = **60,716 tokens** (target ≤90K soft, ≤110K hard)
  - 偏差: 60,716 / 90,000 = 67.5% of soft target, 55.2% of hard cap → 余量 49,284 tokens (44.8%)
- 6 source 注释块: 全有
- 首行 ISO ts: ✓
- `---` 章节分隔: ✓

## 4. Reviewer 抽样 (5 段, 已 PASS)
- ch01 §1.1 Purpose — byte-exact ✓
- ch02 §2.5 SDTM Standard Domain Models — byte-exact ✓
- ch04 §4.1 General Domain Assumptions (4.1.1-4.1.7 前半) — byte-exact ✓
- ch08 §8.4.1 Supplemental Qualifiers SUPP-- — byte-exact ✓
- ch10 Appendix D CDISC Variable-naming Fragments — byte-exact ✓

## 5. 主控独立抽样 (5 段, 与 reviewer 不重叠, 已 PASS)
Python 逐字节对比 src vs v2 输出:

| 样本 | 源行 char | v2 char | byte-exact |
|------|----------|---------|-----------|
| ch01 §1.4 How to Read | 4,741 | 4,741 | ✓ |
| ch02 §2.3 | 1,499 | 1,499 | ✓ |
| ch03 §3.2 | 17,164 | 17,164 | ✓ |
| ch08 §8.3 (RELREC) | 3,576 | 3,576 | ✓ |
| ch10 Appendix C | 1,760 | 1,760 | ✓ |

结论: 5/5 byte-exact 匹配, 含关键的 ch08 §8.3 (RELREC Spec 段, v1 曾精简).

## 6. 偏差与处理
**无偏差**. v2 产出是对源的纯拼接 (首行 ISO ts + 头部 + 6 章节按序 + 章节间 `---`), 无压缩/改写/重排. reviewer + 主控共 10 段抽样全 byte-exact 一致.

## 7. 累计指标
- 累计 v2 files (output_v2/*.md): 11 (与 v1 一致, 02_chapters 是替换而非新增)
  - 00_routing / 01_index / 02_chapters (v2新) / 03_model / 04_variable_index / 05_mega_spec / 06_assumptions / 07_examples_catalog / 08_terminology_map / system_prompt_v2 / upload_manifest_v2
- 累计 token (v2 stage v2.1 预测): 约 **208K** (v1 基线约 192K + 02_chapters Δ 约 +30K 因 ch01/02/03/08/10 展开 + ch04 不变)
  - 精确值 Task C2 (build_v2_stage.py --stage v2.1) 会实测

## 8. 下一步
进 Task C2 (build_v2_stage.py --stage v2.1 阶段聚合: 更新 system_prompt_v2.md + upload_manifest_v2.md + _progress.json + trace.jsonl + 写 stage_v2.1_chapters.md evidence)
