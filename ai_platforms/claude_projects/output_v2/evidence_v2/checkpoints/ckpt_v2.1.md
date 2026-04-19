# Checkpoint @ Stage v2.1

> 时间: 2026-04-19 (跨日完成, v2.1 build 2026-04-18, cowork A/B 执行 2026-04-18 → 2026-04-19)
> 本文档按 PLAN_V2.md §5 Task C3 Step 2 模板落盘.

---

## 主控汇报 (C3 Step 1 原文, 经 CHECKPOINT_V2.1_HANDOFF.md 交给 cowork 执行)

```
=== Hard Checkpoint @ Stage v2.1 ===
本阶段产出: output_v2/02_chapters.md = 60,716 tokens (target ≤90K) [PASS]
累计文件数: 11 (与 v1 一致, 因替换非新增)
累计 token: 209,620 tokens (含 4 份元文档, 上传 9 个实体 .md = 205,895 tokens, target ~270K, 偏差 -22%)

Layer 1 自动检查: C2/C3/C4/C5/C11 全 PASS
Layer 2 reviewer (code-reviewer, opus): PASS (3 LOW findings, non-blocking)
Layer 3 audit (reviewer 5 段 + 主控 5 段 non-overlapping): 10/10 byte-exact PASS

变更对比 v1:
- 02_chapters.md: 31,068 tokens (v1 压缩) → 60,716 tokens (v2.1 全展开, +95.4%)
- 其他 8 文件 md5 与 v1 baseline 一致

请操作 (已通过 CHECKPOINT_V2.1_HANDOFF.md 交给 cowork 自动执行):
1. 在 Claude.ai 新建第二个 Project ("SDTM-Knowledge-v2")
2. 把 system_prompt_v2.md 全文粘贴到 Instructions
3. 上传 9 个 .md (00_routing 到 08_terminology_map, 不含 2 个元文档)
4. 等 indexing
5. 跑 12 题 T1-T12 A/B 测试 (v1 同题对照)
6. 按模板回报
```

---

## 用户回应 (来自 STAGE_V2.1_AB_REPORT.md, cowork 完整捕获)

- **Project 名**: `SDTM-Knowledge-v2` (v2) vs `SDTM Expert v3.4` (v1)
- **上传**: 9/9 文件成功, system_prompt_v2.md 粘贴到 Instructions, Indexing 完成
- **Capacity 实测**: **13%** (v1 对比 12%, 上升 1 个百分点符合 +95.4% token 预期 — 因 RAG 显示为分桶百分比)
- **测试用时**: 2 个会话 (跨日 compaction, v1/v2 答案分别落盘于会话临时文件)

### T1-T12 结果 (精度对比 / T9-T12 PASS 判定)

| # | 题目简称 | 精度 (v1→v2.1) | T9-T12 PASS? | 关键差异 |
|---|---------|--------------|-------------|---------|
| T1 | AEDECOD Core | 持平 | — | 两版同质, 均基于 mega_spec 表格 |
| T2 | AE 严重度变化 | ↑ | — | v2 多 5 处章节锚点 (§4.2.1/§4.3.6/§8.6.3/assum 7e/AE 3b) |
| T3 | RELREC 4 方法 | **↓** | — | v2 严格拒答 (§6.3.5.9.3 未收录); v1 给 3+1 重建方案含推测标注 |
| T4 | EPOCH 域列表 | ↑ | — | v2 增 §4.1.3.1 原文锚点, v1 只有数量来源 |
| T5 | SUPP-- 判定 | 持平 | — | 决策树同质, v2 补 SUPP-- spec 表但步骤 7→5 |
| T6 | AE Ex2 数据 | ↑ | — | 两版均不给数据行, v2 多给 6 个 Example catalog 表 |
| T7 | C66742 值 | ↑ (轻微) | — | v2 增 §4.3.7 原文引用 |
| T8 | CV 域变量 | ↑ (轻微) | — | v2 用 4-class value-range 组织, v1 用 6-Role 组织 |
| T9 | ch01 架构 | ↑ (轻微) | **PASS** ✅ | v2 精确到 §1.5, v1 只到 §1.4; 均纠正 "ch01 is Introduction not Foundational" |
| T10 | ch02 §2.6 | ↑ | **PASS** ✅ | v2 给完整 11 子步骤 a-k + v3.4 新增 SA/SQ 变更 |
| T11 | (变体题) | N/A | **PASS** ✅ | v2 立即检出虚构 §3.1.2.2 + 给 ch03 完整 TOC + 10 条命名规则映射表 |
| T12 | (变体题) | N/A | **PASS** ✅ | v2 §4.4.1-§4.4.10 全覆盖 + §4.4.8 "--STDTC 禁用 Findings" v3.4 新增条目 |

### 汇总数据

- T1-T8 衰减 (↓): **1** (T3)
- T1-T8 上升 (↑): **5** (T2, T4, T6, T7, T8)
- T1-T8 持平: **2** (T1, T5)
- T9-T12 PASS: **4/4**
- 直接可对比的 T9-T10 中 v2 表现: **2/2 ↑**
- 异常/拒答/截断: 无

### 题目变体说明

T11/T12 在 v1/v2 之间不一致:
- T11: v1 问 ch08 §8.3 RELREC → v2 问 ch03 §3.1.2.2 (虚构 section 测试)
- T12: v1 问 ch10 附录 entity → v2 问 ch04 §4.4 Timing

变体题**强化**了 chapter-test 价值 (检出虚构 section + 验证真实章节全覆盖), 但不能直接 A/B 对照精度, 两版各自独立判 PASS.

---

## 决议

- **继续 / 调整 / 暂停**: **待用户拍板** (按 PLAN §5 C3 Step 6 "1 衰减 → 询问用户是否仍进" 分支)
- **是否产生 regression**: **是** (T3 一题 ↓)
- **Regression 归因**: 见 `../failures/stage_v2.1_t3_regression.md` (reviewer 独立归因 — 设计意图: v2.1 边界严谨性拒绝幻觉重建, 非质量回退)
- **主控建议**: 继续进入 Task D1 (Phase D / batch 2 examples 高频展开), 因为:
  1. T3 ↓ 是设计选择的副作用 (严谨换实用), 非能力退化
  2. T9-T12 全 PASS 已强证明 chapter byte-exact 路径有效
  3. T1-T8 其余 7 题 5 ↑ / 2 持平, 整体趋势向好, 远低于"≥2 ↓ 立即停"红线
  4. 后续 batch 2 (examples 数据表) 正好能补 T3/T6 的 PC↔PP examples 缺口 (见报告"后续修复方向")

---

## 下一步 (待用户 ack)

| 用户回应 | 执行 |
|---------|------|
| "继续 / ack / 进 D1" | 进入 Phase D Task D1 (score_domains.py 打分 + 域清单) |
| "调整 / 改算法" | 回 C1 重做 (当前 executor prompt 已落盘 `subagent_prompts/C1_executor.md`) |
| "暂停" | trace.jsonl 写 phase_pause, 等下次 session 重启 |

---

## 附件

- A/B 报告原文: `output_v2/STAGE_V2.1_AB_REPORT.md`
- Cowork 执行手册: `output_v2/CHECKPOINT_V2.1_HANDOFF.md`
- T3 归因 evidence: `../failures/stage_v2.1_t3_regression.md`
- 阶段 audit: `../stage_v2.1_audit.md` (Layer 3)
