<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → _progress.json                       (程序化进度)
  → evidence/checkpoints/                (每 phase 快照)
  → ../../.work/03_verification/issues_found.md
  → ../../.work/meta/worklog/phase06_deep_verification.md
-->

# P7 人工抽样 + Retro — Sub-Plan

> 创建: 2026-05-12
> 状态: DRAFT v0.1
> 前置条件: P6 ALL GATES PASS (99.02% coverage, G1-G7 ✅, 2026-05-12)
> Tier: 3

---

## 0. 进入条件 (已满足)

| 条件 | 状态 |
|---|---|
| P6 G1 PASS (coverage ≥99%) | ✅ 99.02% |
| P6 G2 PASS (SKELETON_ONLY 全登记) | ✅ |
| P6 G3 PASS (STRUCTURE_DRIFTED 全修复) | ✅ |
| P6 G4 PASS (UNSOURCED 全分类) | ✅ 926/926 |
| P6 G5 PASS (HALLUCINATED=0) | ✅ 0 |
| P6 G6 PASS (Rule D oh-my-claudecode:critic) | ✅ PASS |
| P6 G7 PASS (trace.jsonl phase_report) | ✅ |

---

## 1. P7 目标

P7 是整个 06 Deep Verification 工程的**最终人工质量验证**阶段，目标：

1. **人工抽样复核**: 用户独立复检分层随机样本 (≥50 原子)，验证 AI 打标的 verdict 是否正确，误判率 <5%
2. **RETROSPECTIVE.md**: 三段 retro (保留做法 / 必须补缺口 / 关键决策复盘)，Rule C 强制
3. **Rule D 独立复核**: 不同 subagent_type reviewer PASS

---

## 2. 采样方案

### 2.1 样本量

- **最小**: ≥50 原子 (PLAN.md §0.3 exit criteria)
- **建议**: 60 原子 (加 10 buffer，容错 3 个误判仍 PASS)
- **误判容限**: 60 × 5% = 3 个误判 → PASS; 4+ → FAIL (需 root cause 分析)

### 2.2 分层方案 (按 verdict 分层)

| Verdict | 总量 | 采样数 | 说明 |
|---------|------|--------|------|
| EXACT | 3,748 | 12 | 抽检精确匹配质量 |
| EQUIVALENT | 4,235 | 18 | 最高风险：改写是否语义等价 |
| PARTIAL | 2,039 | 12 | 抽检部分覆盖判定是否合理 |
| INTENTIONAL_EXCLUDE | 2,087 | 8 | 抽检排除理由是否充分 |
| MISPLACED | 276 | 4 | 抽检错位判定 |
| ERROR | 93 | 4 | 抽检错误判定 |
| MISSING (9 figure-deferred) | 9 | 2 | 全为 FIGURE，确认 deferred 合理 |
| **合计** | | **60** | |

### 2.3 二级分层 (source)

- ig34 (SDTMIG v3.4) 与 sv20 (SDTM v2.0) 按比例代表
- ig34 约占总量 80% → 每 verdict bucket 优先 ig34

### 2.4 采样工具

采样脚本: `scripts/p7_sample.py`
输出: `evidence/checkpoints/p7_sample_sheet.md` (人工复检工作表)

---

## 3. 人工复检流程

每条原子，用户需判断:

**Q: AI 打的 verdict 是否正确？**
- `CORRECT` — verdict 合理，接受
- `WRONG: <建议 verdict>` — verdict 有误，给出正确判断

**参考对照材料**:
- `pdf_atoms.jsonl` 中该原子的 `verbatim` (PDF 原文)
- `coverage_ledger.jsonl` 中的 `md_atom_ids` (匹配到的 KB 内容)
- `md_atoms.jsonl` 中对应 md 原子的 verbatim

复检工作表会在每条原子旁附上 PDF verbatim + KB 匹配内容，用户直接在工作表上标注。

---

## 4. Gate 判定

| Gate | 阈值 | 说明 |
|------|------|------|
| **P7-G1** 误判率 <5% | ≤3/60 误判 → PASS | 4+ 误判 → 分析 root cause |
| **P7-G2** RETROSPECTIVE.md 完整 | 三段齐备 | Rule C 强制 |
| **P7-G3** Rule D reviewer PASS | 独立 subagent PASS | 不同 subagent_type |

三 Gate 全 PASS → **06 Deep Verification 工程 COMPLETE** ✅

---

## 5. 工作步骤

```
Step 1: 生成采样工作表 (scripts/p7_sample.py → evidence/checkpoints/p7_sample_sheet.md)
Step 2: 用户人工复检工作表 (标注 CORRECT/WRONG)
Step 3: 计算误判率 → P7-G1 判定
Step 4: 撰写 RETROSPECTIVE.md (Rule C)
Step 5: Rule D reviewer 独立复核 (P7-G3)
Step 6: 写 trace.jsonl P7 phase_report
Step 7: 更新 _progress.json + docs/PROGRESS.md → COMPLETE
```

---

## 6. 开放项承接 (来自 P6 OA-1/OA-2/OA-3)

| ID | 描述 | P7 行动 |
|----|------|---------|
| OA-1 | T4 Tier B: 56 SIBLING_DROPPED + 110 CONTENT_TRUNCATED 未修复 | **不阻塞 P7 gate**；在 Retro § "必须补上的缺口" 中记录 |
| OA-2 | 437 UNSOURCED_MANUAL atoms 待 human review | 纳入 Retro § "必须补上的缺口"；可作独立 follow-up 任务 |
| OA-3 | 9 FIGURE-deferred MISSING atoms | 2 个纳入 P7 采样；Retro 记录 |

---

## 7. RETROSPECTIVE.md 大纲

```markdown
# 06 Deep Verification — RETROSPECTIVE

## § 保留下来的做法
- 原子级字面对比的方法论 (发现 Issue 1-16 中 Step 0-4 未审出的问题)
- 分 phase 拆 sub-plan (P1-P7)
- Rule D subagent_type 轮换 (累计 NN 种)
- md_atoms.jsonl 倒排索引 + P3 语义检索
- ...

## § 必须补上的缺口
- T4 Tier B (SIBLING_DROPPED/CONTENT_TRUNCATED) 未完成修复
- 437 UNSOURCED_MANUAL 需人工 review
- section_coverage.jsonl P4b 快照未 post-fix 刷新
- 9 FIGURE-deferred MISSING atoms
- ...

## § 关键决策复盘
- 覆盖率分母选择 (扣除 IE 后的 10,400)
- P6 Tier B deferred 决策 (G1 已达标不继续推进)
- FIGURE 原子 deferred 处理策略
- ...
```

---

## 8. Changelog

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-05-12 | Initial (P6 ALL PASS 后创建) |
