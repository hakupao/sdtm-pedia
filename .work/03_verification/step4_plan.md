<!-- chain: A (验证进度链)
  修改本文件后，必须检查:
  → 03_verification/plan.md            (主计划)
  → 03_verification/issues_found.md    (问题汇总)
  → meta/worklog.md                    (工作日志)
  → progress.json                      (程序化进度)
  → ../docs/PROGRESS.md                (进度看板)
-->

# Step 4: 终验、汇总与项目收尾

> 创建日期: 2026-04-16
> 状态: **待执行**
> 派生自: plan.md Step 4
> 方案: 方案 C — 高风险文件终验 + 全局汇总
> 关联: [retrospective.md](../meta/retrospective.md) — 四条预防规则
> 关联: [repair_plan.md](repair_plan.md) — Issue 2 修复方法（写/审分离）
> 关联: [followup_plan.md](followup_plan.md) — 残余风险排查方法

---

## 1. 背景与目标

### 1.1 当前状态

Step 0 ~ 3.6 全部完成，Issue 1 & Issue 2 已修复，Followup M1-M5 已完成。
138 个 AI 提取文件已全部经过至少一轮验证和修复。

### 1.2 为什么还需要终验

6 个 chapters/ 文件经历了最多轮修改：

```
原始 AI 提取 → Step 3 验证修复 → Issue 2 大规模补全 → Followup 补全
```

多轮修改带来以下风险：
- **回归风险**: 后轮修改可能覆盖前轮正确内容
- **拼接不一致**: 不同 agent 在不同时间补写的内容，风格/术语可能不统一
- **遗漏累积**: 每轮验证各有盲区，但从未有一次"从头到尾"的完整检查

### 1.3 目标

1. 对 6 个高风险 chapters/ 文件做一次全新的、独立的终验
2. 修复终验发现的任何问题
3. 汇总 Step 0-4 全部验证数据，编写最终报告
4. 更新项目状态，关闭验证阶段

### 1.4 不做什么

- 不重复验证 spec.md (63)、terminology/ (91) — 程序化生成，已有脚本校验
- 不重复验证 assumptions.md (61) — 编号列表格式，Step 1 已逐条修复
- 不重复验证 examples.md (63) — Step 2 已逐域验证 + Followup M5 抽查 PASS
- 不重复验证 model/ (6) — Step 3-1/3-2 已 80 处逐修，内容为结构化定义

---

## 2. 终验对象

### 2.1 文件清单与风险评估

| 文件 | 行数 | PDF 页码 | 页数 | 行/页 | 修改轮数 | 风险等级 |
|------|------|----------|------|-------|----------|----------|
| ch01_introduction.md | 102 | p.7-10 | 4 | 25.5 | 3 轮 (Step3 + Issue2排查 + Followup M1) | 中 |
| ch02_fundamentals.md | 174 | p.11-16 | 6 | 29.0 | 3 轮 (Step3 + Issue2排查 + Followup M2) | 中 |
| ch03_submitting_data.md | 130 | p.17-22 | 6 | 21.7 | 3 轮 (Step3 + Issue2排查 + Followup M3) | 中 |
| ch04_general_assumptions.md | 654 | p.22-59 | 38 | 17.2 | 3 轮 (Step3 + Issue2核心修复 + 复核) | **高** |
| ch08_relationships.md | 360 | p.427-446 | 20 | 18.0 | 3 轮 (Step3 + Issue2修复 + 复核) | **高** |
| ch10_appendices.md | 230 | p.444-461 | 18 | 12.8 | 3 轮 (Step3 + Issue2修复 + 复核) | **高** ⚠️ 行/页比偏低 |

### 2.2 风险指标解读

- **行/页比基准**: 15-20 行/页（基于已验证通过的文件统计）
- ch10 仅 12.8 行/页，低于基准 → 可能仍有内容缺失，终验需重点关注
- ch01/ch02 行/页偏高（25-29），因 intro/fundamentals 文字密度高于技术章节，属正常

---

## 3. 终验方法

### 3.1 核心原则（来自 retrospective 四条规则）

| 规则 | 本次如何落实 |
|------|-------------|
| **规则 1: 定量 PASS 标准** | 覆盖率 ≥ 95% + 零占位标记 + 行/页比合理 |
| **规则 2: 写/审分离** | 终验 agent 独立于之前所有修复 agent；修复与复核由不同 agent 执行 |
| **规则 3: AI 估算值标记** | 终验不涉及页码估算（页码已在 page_index.json 确认） |
| **规则 4: 人工抽样检查点** | 终验结果提交用户后，用户选 1-2 节自行对照 PDF 抽查 |

### 3.2 终验流程（单文件）

```
Phase 1: 独立 subagent 终验
  ├─ 输入: PDF 页码范围 + md 文件路径（不提供之前的验证报告）
  ├─ subagent 读 PDF → 列出所有章节/段落/要点
  ├─ subagent 读 md → 逐要点比对
  ├─ 输出: 结构化终验报告（见 §3.4 输出格式）
  └─ 判定: PASS / FAIL

Phase 2: 修复（仅 FAIL 时触发）
  ├─ 主线程根据终验报告中的遗漏清单补写内容
  ├─ 补写完成后，启动新的独立 subagent 复核
  ├─ 复核 subagent 只检查被修改的节（不重复全文）
  ├─ 输出: 修复复核报告
  └─ 迭代直到 PASS

Phase 3: 锁定
  ├─ 将终验结果写入 evidence 文件
  └─ 标记该文件终验完成
```

### 3.3 终验 agent 分批方案

为避免单 agent 阅读量过大导致遗漏，按以下方式拆分：

| 批次 | Agent | 文件 | PDF 页码 | 阅读量 | 并行 |
|------|-------|------|----------|--------|------|
| A | agent-final-ch01-03 | ch01 + ch02 + ch03 | p.7-22 | 16 页 + 406 行 md | ✅ |
| B | agent-final-ch04-front | ch04 前半 §4.1 | p.22-40 | 19 页 + ~300 行 md | ✅ |
| C | agent-final-ch04-back | ch04 后半 §4.2 | p.41-59 | 19 页 + ~350 行 md | ✅ |
| D | agent-final-ch08 | ch08 | p.427-446 | 20 页 + 360 行 md | ✅ |
| E | agent-final-ch10 | ch10 | p.444-461 | 18 页 + 230 行 md | ✅ |

**为什么 ch04 拆成 2 个 agent**:
- 38 页 PDF 是单 agent 一次性比对的上限
- Issue 2 正是发生在 ch04，需要最高精度
- 按 §4.1 / §4.2 自然边界拆分

**5 个 agent 全部并行**，预计一轮完成。

### 3.4 终验 agent 输出格式

每个 agent 必须输出以下结构化报告：

```markdown
## [文件名] 终验报告

- **检查日期**: YYYY-MM-DD
- **检查人**: Sonnet subagent (agent-final-XXX)
- **PDF 页码**: p.XX-YY
- **md 文件**: [路径]
- **md 行数**: N 行

### 定量结果

- **PDF 章节/段落总数**: N
- **PDF 独立要点总数**: M
- **md 已覆盖要点数**: K
- **覆盖率**: K/M = XX.X%
- **占位标记扫描**: [grep 结果: 待补全/TODO/待后续/部分覆盖]
- **行/页比**: X.X (基准 15-20)

### 逐节明细

| 节号 | 标题 | PDF 要点数 | md 覆盖数 | 覆盖率 | 判定 |
|------|------|-----------|----------|--------|------|
| ... | ... | ... | ... | ... | PASS/FAIL |

### 问题清单（如有）

| # | 节号 | 类型 | 描述 | 严重性 |
|---|------|------|------|--------|
| 1 | ... | 遗漏/错误/不一致 | ... | 高/中/低 |

### 准确性抽查

[随机选取 3-5 个具体事实（变量名、规则描述、枚举值等），逐个对照 PDF 原文确认]

| # | 事实 | PDF 原文 | md 内容 | 匹配 |
|---|------|---------|---------|------|
| 1 | ... | ... | ... | ✅/❌ |

### 最终判定

- **判定**: PASS / FAIL
- **PASS 条件检查**:
  - [ ] 覆盖率 ≥ 95%
  - [ ] 零占位标记
  - [ ] 行/页比在合理范围
  - [ ] 准确性抽查无事实错误
- **FAIL 原因**（如适用）: ...
```

### 3.5 终验 agent 的 Prompt 要点

终验 agent 的 prompt 中必须包含以下指令：

1. **你是独立终验者**，不知道之前有哪些修复。把这个 md 文件当作第一次见到。
2. **逐节比对**，不要跳过任何节。对每个节，先列出 PDF 中的全部要点，再检查 md 是否覆盖。
3. **"要点"的定义**: 一条独立的规则、一个定义、一个示例、一个交叉引用、一个表格行、一个枚举值。
4. **不要因为 md 写得"看起来合理"就判 PASS**。你的任务是找"PDF 中有而 md 中没有的内容"。
5. **准确性抽查**: 随机选 3-5 个具体事实，逐字对照 PDF。
6. **输出必须包含逐节明细表**，不能只给一个总覆盖率。

---

## 4. 修复流程（仅 FAIL 时触发）

### 4.1 修复原则

- 继承 repair_plan.md 的方法: **写/审分离 + 逐节锁定**
- 修复 agent (主线程) ≠ 复核 agent (独立 subagent)
- 每个被修复的节必须有独立复核记录

### 4.2 修复单节流程

```
Step A: 定位问题
  - 从终验报告的问题清单中取出一个 FAIL 节
  - 确认: 节号、PDF 页码、遗漏/错误的具体描述

Step B: 读 PDF 原文
  - 读取该节对应的 PDF 页码
  - 确认该节的全部内容边界（起止、子节、表格/列表数量）

Step C: 修复内容
  - 将缺失内容补写到 md 文件对应位置
  - 修正错误内容（如有）
  - 保持与文件其他部分一致的格式风格
  - 删除任何残留的占位标记

Step D: 独立 subagent 复核
  - 启动新的独立 Sonnet subagent
  - 复核 agent 读 PDF 同一页码 + 读修复后的 md 对应节
  - 输出:
    a) PDF 该节要点总数
    b) md 覆盖数
    c) 覆盖率
    d) 遗漏清单（如有）
    e) 准确性问题（如有）
    f) 判定: PASS / FAIL

Step E: 迭代（如复核 FAIL）
  - 根据复核反馈补充
  - 启动另一个新 subagent 复核（不复用之前的复核 agent）
  - 重复直到 PASS

Step F: 锁定
  - 记录到 evidence 文件
  - 进入下一个 FAIL 节
```

### 4.3 修复复核 agent 输出格式

```markdown
### [节号] [标题] — 修复复核

- **PDF 页码**: p.XX-YY
- **修复内容**: [简要描述修改了什么]
- **复核 agent**: Sonnet subagent (reviewer-XXX)
- **PDF 要点总数**: N
- **md 覆盖数**: M
- **覆盖率**: M/N = XX%
- **遗漏清单**: [无 / 具体列表]
- **准确性问题**: [无 / 具体列表]
- **判定**: PASS / FAIL
- **迭代次数**: N
```

---

## 5. 用户抽查（人工检查点）

### 5.1 时机

在 4-1 终验 + 4-2 修复全部完成后，汇总报告编写前。

### 5.2 流程

1. 向用户提交终验结果摘要（每个文件的覆盖率 + 问题数）
2. 用户选择 1-2 个节，自行对照 PDF 检查
3. 用户反馈:
   - 确认无误 → 进入汇总阶段
   - 发现问题 → 按 §4 修复流程处理，然后再次提交抽查

### 5.3 为什么需要这一步

- retrospective 规则 4 明确指出: 人工抽样是唯一有效的兜底机制
- Issue 1 和 Issue 2 都是用户抽查发现的
- AI 终验 agent 可能存在系统性盲区（"验证本身没有发现的缺失"）

---

## 6. Evidence 记录体系

### 6.1 文件结构

```
.work/03_verification/results/
├── step4_final_verification.md    ← 终验 evidence（5 个 agent 的报告合并）
├── step4_repair_evidence.md       ← 修复 evidence（仅 FAIL 时产生）
├── step4_user_review.md           ← 用户抽查记录
└── step4_final_report.md          ← 最终汇总报告
```

### 6.2 终验 evidence 格式 (step4_final_verification.md)

```markdown
# Step 4 终验 Evidence

> 生成日期: YYYY-MM-DD
> 终验方案: 方案 C (高风险文件终验 + 全局汇总)
> 终验对象: 6 个 chapters/ 文件

---

## 总览

| 文件 | 终验 Agent | 覆盖率 | 占位标记 | 行/页比 | 准确性 | 判定 |
|------|-----------|--------|---------|---------|--------|------|
| ch01 | agent-final-ch01-03 | XX% | 0 | XX.X | N/N OK | PASS/FAIL |
| ... | ... | ... | ... | ... | ... | ... |

---

[各 agent 的完整报告按 §3.4 格式依次排列]
```

### 6.3 修复 evidence 格式 (step4_repair_evidence.md)

仅在终验发现 FAIL 时产生，格式同 §4.3，按节逐条记录。

### 6.4 用户抽查记录格式 (step4_user_review.md)

```markdown
# Step 4 用户抽查记录

> 日期: YYYY-MM-DD

## 用户选择的抽查节

| # | 文件 | 节号 | PDF 页码 |
|---|------|------|----------|
| 1 | ... | ... | ... |

## 抽查结果

### [节号] [标题]
- **用户判定**: 通过 / 发现问题
- **问题描述**（如有）: ...
- **处理**: [无需处理 / 已按 §4 修复]
```

---

## 7. 最终汇总报告 (step4_final_report.md)

### 7.1 报告结构

```markdown
# SDTM Knowledge Base 验证最终报告

> 生成日期: YYYY-MM-DD
> 验证周期: 2026-04-14 ~ 2026-04-16
> 验证计划: .work/03_verification/plan.md

---

## 1. 项目概述
  - 293 文件，4 类来源
  - 验证范围: 138 个 AI 提取文件

## 2. 验证方法总结
  - Step 0-3.6 各步骤方法概述
  - Step 4 终验方法
  - 四条预防规则的落实情况

## 3. 全局统计

### 3.1 文件级统计
| 类别 | 文件数 | 首次 PASS | 修复后 PASS | 终验 PASS | 最终状态 |
|------|--------|----------|------------|----------|----------|
| assumptions.md | 61 | XX | XX | — | 全 PASS |
| examples.md | 63 | XX | XX | — | 全 PASS |
| model/ | 6 | 0 | 6 | — | 全 PASS |
| chapters/ | 6 | 0 | 6 | X/6 | ... |
| **合计** | **138** | ... | ... | ... | ... |

### 3.2 问题级统计
| 指标 | 数值 |
|------|------|
| 发现问题总数 | N |
| 已修复 | N |
| Issue 级别问题 | 2 (Issue 1: 页码偏移, Issue 2: 内容空洞) |
| Followup 补全要点 | 27+ |
| 终验新发现 | N |

### 3.3 修复轮次分布
| 轮次 | 文件数 | 说明 |
|------|--------|------|
| 首次即 PASS | N | ... |
| 1 轮修复后 PASS | N | ... |
| 2+ 轮修复后 PASS | N | ... |

## 4. 各步骤详细结果
  - Step 0: page_index.json (指向 results/)
  - Step 1: assumptions (指向 results/step1_assumptions.md)
  - Step 2: examples (指向 results/step2_examples_summary.md)
  - Step 3: model + chapters (指向各 results/ 文件)
  - Step 3.5: 溯源矩阵 (指向 TRACEABILITY.md)
  - Step 3.6: 图像溯源 (指向 scans/image_inventory.md)
  - Step 4: 终验 (指向 step4_final_verification.md)

## 5. Issue 处理记录
  - Issue 1: 根因 + 影响 + 修复 + 预防
  - Issue 2: 根因 + 影响 + 修复 + 预防
  - 每个 Issue 附 evidence 文件指针

## 6. 质量保障措施
  - 四条预防规则及其落实
  - 写/审分离实践记录
  - 人工抽查记录

## 7. 遗留风险与建议
  - 已知限制（AI 验证的系统性边界）
  - 未覆盖区域（如有）
  - 后续维护建议

## 8. 结论
  - 最终质量判定: [全部 PASS / 附条件 PASS / ...]
  - 知识库可用性声明
```

### 7.2 数据来源映射

汇总报告中的每个数字都必须可追溯到具体的 evidence 文件：

| 数据 | 来源文件 |
|------|---------|
| Step 1 统计 | `results/step1_assumptions.md` |
| Step 2 统计 | `results/step2_examples_summary.md` + `step2_examples_detail.md` |
| Step 3 model/ 统计 | `results/step3_1_model_small.md` + `step3_2_model_rest.md` |
| Step 3 chapters/ 统计 | `results/step3_3_chapters_small.md` + `step3_4_ch04.md` + `step3_5_ch08_ch10.md` |
| Issue 2 修复统计 | `results/repair_evidence.md` |
| Followup 统计 | `results/followup_evidence.md` |
| Step 4 终验统计 | `results/step4_final_verification.md` |

---

## 8. 项目状态更新（Chain A）

终验 + 汇总完成后，按 Chain A 更新以下文件：

| 文件 | 更新内容 |
|------|---------|
| `plan.md` | Step 4 状态 → **已完成**，更新顶部状态行 |
| `issues_found.md` | 最终状态行更新 |
| `meta/worklog.md` | 添加 Step 4 工作日志条目 |
| `progress.json` | 更新验证阶段进度 |
| `docs/PROGRESS.md` | 同步进度看板 |

---

## 9. 执行步骤总览

| 步骤 | 内容 | 执行方式 | 产出 |
|------|------|---------|------|
| **4-1** | 终验 6 个 chapters/ 文件 | 5 个 Sonnet agent 并行 | `step4_final_verification.md` |
| **4-2** | 修复终验 FAIL 项 | 主线程修复 + 独立 agent 复核 | `step4_repair_evidence.md` |
| **4-3** | 用户抽查 | 用户对照 PDF | `step4_user_review.md` |
| **4-4** | 编写汇总报告 | 主线程汇总 | `step4_final_report.md` |
| **4-5** | 更新项目状态 | Chain A 全链更新 | 5 个文件更新 |

### 完成标准

Step 4 视为完成，当且仅当:

- [ ] 6 个 chapters/ 文件终验全部 PASS（含修复后 PASS）
- [ ] 终验发现的所有问题已修复并通过独立复核
- [ ] 用户抽查通过
- [ ] 汇总报告已编写，所有数字可追溯到 evidence 文件
- [ ] Chain A 全部更新完成
- [ ] 零残留占位标记（全 knowledge_base/ grep 确认）
