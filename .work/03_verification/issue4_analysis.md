<!-- chain: A (验证进度链)
  修改本文件后，必须检查:
  → 03_verification/issues_found.md    (问题汇总)
  → meta/worklog.md                    (工作日志)
  → meta/retrospective.md             (反思与规则)
-->

# Issue 4: ch08_relationships.md 章节缺失（§8.2.1, §8.4.1, §8.4.4）

> 发现日期: 2026-04-16
> 发现人: 用户人工复查（Step 4-3 回归检查）
> 状态: **已修复** (2026-04-16)
> 严重性: **高** — 3 个子节缺失/不完整，影响 RELREC 和 SUPP-- 两个核心关系机制的完整性
> 关联: [issues_found.md](issues_found.md), [retrospective.md](../meta/retrospective.md)

---

## 1. 发现过程

### 1.1 时间线

| 时间点 | 事件 |
|--------|------|
| Issue 3 修复完成 | ch04 全文重审完成，1116→1395 行 |
| Step 4-3 回归检查 | 用户回到 step4_plan.md，人工检查 ch08，发现 §8.2.1、§8.4.1、§8.4.4 缺失 |

### 1.2 发现方式

用户在 Issue 3 解决完毕后，回到 Step 4 的人工检查流程，对照 PDF p.427-446 阅读 ch08_relationships.md，发现以下缺失：

- **§8.2.1 Related Records (RELREC)**: md 从 §8.2 简要介绍直接跳到 §8.2.2 Examples，缺少 §8.2.1 的 RELREC Description/Overview + 完整 Specification 表（含 CDISC Notes 列）
- **§8.4.1 Supplemental Qualifiers (SUPP--)**: md 有一个简化的 Specification 表（缺少 Role 和 CDISC Notes 列），但没有 §8.4.1 标题，且缺少完整的 CDISC Notes 详细说明
- **§8.4.4 When Not to Use Supplemental Qualifiers**: md 有 "When NOT to Use SUPP--" 内容但放在 §8.4.3 Examples **之前**（位置错误），应为 §8.4.4 排在 Examples 之后

---

## 2. 问题描述

### 2.1 确认的缺失节

| 节号 | 问题 | PDF 实际内容 | md 当前状态 |
|------|------|------------|-----------|
| §8.2.1 | 完整节缺失 | RELREC Description/Overview（1 段）+ 完整 Specification 表（7 变量 × 6 列含 Role + CDISC Notes）+ 脚注 | md 直接从 §8.2 intro 跳到 §8.2.2，RELREC spec 被合并到 §8.2 下的简化表中（缺 Role/CDISC Notes） |
| §8.4.1 | 标题缺失 + spec 不完整 | §8.4.1 标题 "Supplemental Qualifiers (SUPP--)" + 完整 Specification 表（11 变量 × 7 列含 Role + CDISC Notes 详细描述） | 有 "Specification" 但无 §8.4.1 编号，表只有 4 列（缺 Role + Controlled Terms + CDISC Notes） |
| §8.4.4 | 位置错误 | 紧跟 §8.4.3 Examples 之后 | 内容存在但放在 §8.4.2 和 §8.4.3 之前（结构错误） |

### 2.2 §8.2 intro 缺失内容

PDF 的 §8.2 intro 包含以下 md 中缺少的要点：
- RELREC 可描述 peer record 关系（本节）和 dataset 关系（§8.3）
- 关系通过 CRF 上的明确引用/复选框或 CRF 设计收集
- 每条记录通过 RELID 唯一标识关系对，RELID 在 USUBJID 内必须一致
- 建议使用标准命名约定（全字母、全数字、大写）
- 记录通过 STUDYID、RDOMAIN、USUBJID、IDVAR/IDVARVAL 组合键定位
- 可用 --GRPID 替代 --SEQ 作为 IDVAR，提高效率（如将一组 CM 记录关联到一条 AE）
- RELREC 应仅用于：(1) 显式关系如伴随用药与 AE 的因果关系；(2) 需要多数据集合并的信息

---

## 3. 根因分析

### 3.1 与前序 Issue 的关系

| Issue | 根因 | 本次是否同类 |
|-------|------|------------|
| Issue 2 | 占位标记过验证 | 否 — 本次不是占位标记，而是原始提取遗漏 |
| Issue 3 | agent 拆分盲区 | 部分相关 — ch08 在 Step 4 中由单 agent 处理（agent-final-ch08），不存在拆分盲区，但该 agent 未能发现 §8.2.1 和 §8.4.1 的缺失 |

### 3.2 根因

1. **原始 Phase 4 提取时的结构简化**: ch08 原始提取将 §8.2.1 的 RELREC spec 合并到 §8.2 intro 中，丢失了独立子节结构和完整 CDISC Notes
2. **Specification 表降级**: 完整的 7 列 spec 表（含 Role + CDISC Notes）被简化为 4 列表，丢失关键元数据
3. **Step 4 终验 agent 未检测到**: agent-final-ch08 的终验报告可能将 §8.2 下的简化 spec 视为"覆盖了"，未察觉它实际是 §8.2.1 的不完整版本
4. **§8.4.4 位置错误未被标记**: 终验 agent 可能只检查了内容是否存在，未验证章节顺序

---

## 4. 修复方案

### 4.1 核心原则

遵循 Issue 3 方法论（retrospective 规则 1-7）：
- 逐节对照 PDF 补全
- 写/审分离（修复后启动独立 reviewer agent）
- 输出逐子节覆盖率报告

### 4.2 修复范围

| 修复项 | 操作 | PDF 页码 |
|--------|------|---------|
| §8.2 intro | 扩展：补充 RELID、keying、--GRPID 效率说明 | p.429 |
| §8.2.1 | 新建：RELREC Description/Overview + 完整 Specification 表 | p.429-430 |
| §8.4 intro / §8.4.1 | 重构：添加 §8.4.1 标题 + 替换为完整 Specification 表（含 Role + CDISC Notes）+ 补充 --GRPID 分组说明 | p.432-433 |
| §8.4.4 | 移动：将 "When NOT to Use" 从 §8.4.2 之前移到 §8.4.3 之后 | p.435 |

### 4.3 预估影响

- 当前行数: 421 行
- 预计修复后: ~480-510 行（§8.2.1 spec 表 +30 行, §8.2 intro 扩展 +15 行, §8.4.1 spec 扩展 +20 行）
- 行/页比: 21.1 → ~24-25.5（合理范围内）
