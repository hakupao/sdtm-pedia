# 验证过程中发现的问题

> 创建日期: 2026-04-15
> 状态: Issue 1 已解决 (2026-04-15), Issue 2 全部已修复 (2026-04-15), Followup M1-M5 已完成 (2026-04-16)

---

## Issue 1: 图像扫描页码不可靠 → page_index.json 权威索引偏差

**状态**: **已解决** (2026-04-15) — 详见 [issue1_investigation.md](issue1_investigation.md)

**发现方式**: 用户审阅 Step 3.6 图像清单时发现 TD Example 页码偏移

**问题描述**:
6 个 Sonnet agent 扫描 PDF 图像时，页码通过"Read PDF → 视觉识别 → agent 手动标注"获取，没有程序化的页码提取机制。用户核实发现 TD Example 实际从 p.412 开始，而清单标注为 p.416-418，存在明显偏移。

**影响范围**:
- `step3_6_image_inventory.md` 中所有 60 幅图像的页码均为近似值
- 扫描密集区域（如 TA p.386-403 连续 24 幅图）偏移风险更高
- 其他依赖扫描页码的文件也可能受影响

**根因**: Sonnet agent 视觉读取 PDF 时，无法精确定位页码。Read tool 的 pages 参数指定读取范围，但返回内容中页码边界不总是清晰，agent 只能估算。

**待处理事项**:
1. 对 step3_6_image_inventory.md 中所有"待判定"图像的页码逐一核实
2. 评估是否需要对已转化图像（Step 2-final / Step 3-final）的页码也做一次核实
3. 考虑是否需要更可靠的页码获取方法（如对单页逐一读取关键区域）

**优先级**: 高 — 页码是溯源矩阵的核心数据，不准确会导致整个溯源链不可信

---

## Issue 2: ch04_general_assumptions.md 内容严重不完整

**发现方式**: 用户对照 PDF p.22-59（38页）阅读 ch04_general_assumptions.md，发现内容远比 PDF 简陋

**问题描述**:
ch04_general_assumptions.md 在 Step 3-4 验证中被标记为"FAIL → 重构后 PASS"，但实际上仅完成了"骨架修正"（节号体系重建），大量节的内容以 1-2 句话占位，并用 `<!-- [验证注记] ...此节待补全 -->` 标记。

**具体缺失清单** (带"待补全"标记的节):

| 节号 | 标题 | 当前状态 | PDF 实际内容量 |
|------|------|----------|---------------|
| 4.1.1 | Review SDTM and IG | 2 句话概述 | 详细阅读指导，含推荐阅读顺序 |
| 4.1.2 | Relationship to Analysis Datasets | 2 句话 | traceability 详细说明 |
| 4.1.3 | Additional Timing Variables | 1 句话 | EPOCH 详细使用指导 |
| 4.1.3.1 | EPOCH Variable Guidance | 1 句话 | 完整的 EPOCH 规则和示例 |
| 4.1.6 | Additional Guidance on Dataset Naming | 1 句话 | 保留代码完整列表、命名规则、例外 |
| 4.2.2 | Two-character Domain Identifier | 简要段落 | 完整字符规则、例外变量列表 |
| 4.2.4 | Text Case in Submitted Data | 2 句话 | 详细规则 + 例外清单 |
| 4.2.7 | Submitting Free Text (整体) | 标注"仅部分覆盖" | 4 个子节各有详细规则和示例 |
| 4.2.8 | Multiple Values for a Variable | 2 句话 | 4 个子节 (4.2.8.1-4.2.8.4) 各有详细规则 |

**根因分析**:
1. 原始 AI 提取质量差：节号全部错位、大量节缺失
2. Step 3-4 验证的修复策略为"完整重构"，但实际只完成了结构重建
3. 对缺失内容仅添加 1-2 句话占位 + 标记，未实际补全
4. **PASS 判定标准有漏洞**: "结构正确 + 已有内容准确 + 缺失已标记" 即判 PASS，但标记缺失 ≠ 内容完整

**数据佐证**:
- 重构前后行数: 331 → ~340（仅增 9 行，38 页 PDF 内容不可能只需 9 行增量）
- PDF 覆盖率估计: 60-70%（结构 100%，但多个节内容空洞）
- 验证报告原文 (step3_4_results.md 第 110 行): "验证注记 | 无 | 7 处标注待补全内容"

**待处理事项**:
1. 重新对照 PDF p.22-59，逐节补全所有"待补全"标记的内容
2. 补全后重新验证完整性和准确性
3. 修正验证流程：未来 PASS 标准应要求内容完整，不允许留有"待补全"标记
4. 排查其他已 PASS 的文件是否存在类似的"标记但未补全"问题

**优先级**: 严重 — 这是知识库内容质量的核心问题，38 页 PDF 内容大量缺失意味着知识库在 General Assumptions 这一关键章节上不完整

### Issue 2 扩展: 同类问题排查结果 (2026-04-15)

**根因**: 验证 PASS 标准漏洞 — "标记缺失"被等同于"内容完整"。修复和验证在同一上下文完成（自写自判）。

**同样受影响的文件**:

| 文件 | 证据 | 严重性 |
|------|------|--------|
| ch08_relationships.md | Step 3-5 验证报告中 5+ 项高严重性标注"内容补充待后续" | 高 |
| ch10_appendices.md | Step 3-5 验证报告中词汇表约 17 条缺失标注"部分待后续补充" | 高 |

**建议抽查**: ch01_introduction.md, ch02_fundamentals.md, ch03_submitting_data.md（低/中严重性问题中可能藏有内容缺失）

**修复计划**: [repair_plan.md](repair_plan.md) — 写/审分离 + 逐节锁定 + 独立 subagent 复核 + evidence 全记录

### Issue 2 修复进度 (2026-04-15)

| 文件 | 状态 | Evidence |
|------|------|----------|
| ch04_general_assumptions.md | **已修复** — 7 节 + §4.2.7 全部补全，8/8 独立复核 PASS，零占位标记，行数 499→654 | [repair_evidence.md](results/repair_evidence.md) |
| ch08_relationships.md | **已修复** — 5 高严重性内容缺口补全(Overview/8.1/8.2/8.3/8.5)，行数 258→360 | [repair_evidence.md](results/repair_evidence.md) |
| ch10_appendices.md | **已修复** — Appendix B 词汇表 40/40 条目完整，行数 212→230 | [repair_evidence.md](results/repair_evidence.md) |
