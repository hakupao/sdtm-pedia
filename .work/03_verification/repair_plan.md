<!-- chain: A (验证进度链)
  修改本文件后，必须检查:
  → 03_verification/issues_found.md  (问题汇总)
  → meta/worklog.md                  (工作日志)
-->

# Issue 2 修复计划：chapters/ 内容补全

> 创建日期: 2026-04-15
> 状态: **已完成/归档** (2026-04-15) — ch04 + ch08 + ch10
> 派生自: plan.md Step 3-4/3-5 执行中发现 Issue 2
> 子计划: → followup_plan.md (残余风险排查)
> 关联: issues_found.md — Issue 2 (ch04 内容严重不完整)

---

## 背景

验证流程（Step 3-4/3-5）存在 PASS 标准漏洞：对缺失内容仅标记占位而非实际补全，即判 PASS。
根因分析见 issues_found.md Issue 2 及 memory/project_issue2_root_cause.md。

## 必须修复的文件

| 优先级 | 文件 | PDF 页码 | 已知缺失 |
|--------|------|----------|----------|
| P0 | ch04_general_assumptions.md | p.22-59 (38页) | 7 处 `<!-- 此节待补全 -->` 标记 |
| P1 | ch08_relationships.md | p.427-446 (20页) | 5+ 项高严重性"内容补充待后续" |
| P2 | ch10_appendices.md | p.444-461 (18页) | 词汇表约 17 条 PDF 条目缺失 |

## 建议抽查的文件

| 文件 | PDF 页码 | 风险点 |
|------|----------|--------|
| ch01_introduction.md | p.7-12 | 26 问题仅修 3 高，23 低/中留存 |
| ch02_fundamentals.md | p.13-20 | 28 问题仅修 5 高，23 低/中留存 |
| ch03_submitting_data.md | p.17-22 | 18 问题仅修 4，Dataset 大表格跳过 |

---

## 修复方法：写/审分离 + 逐节锁定

### 核心原则

1. **写和审必须分离**: 补写内容的 agent 和复核的 agent 不能是同一上下文
2. **逐节闭环**: 每个节独立处理，复核通过后才进入下一节
3. **零占位标记**: 修复后文件中不允许残留任何 `待补全`/`TODO`/`待后续` 标记
4. **行数合理性**: 修复前后行数对比必须与 PDF 内容量匹配
5. **全程留 evidence**: 每个节的复核结果必须记录到结果文件

### 单节修复流程

```
Step A: 读 PDF 原文
  - 读取该节对应的 PDF 页码范围
  - 确认 PDF 中该节的全部内容边界（起止位置、子节数量、表格/列表/图片数量）

Step B: 补写内容
  - 将 PDF 内容转写为 Markdown，写入 ch04 文件对应位置
  - 删除该节的 <!-- 待补全 --> 标记
  - 保持与文件其他部分一致的格式风格

Step C: 独立 subagent 复核
  - 启动独立 Sonnet subagent
  - subagent 读取 PDF 同一页码范围 + 读取修复后的 md 文件对应节
  - subagent 输出:
    a) PDF 中该节包含的段落/要点总数
    b) md 中已覆盖的段落/要点数
    c) 覆盖率 = b/a
    d) 具体遗漏清单（如有）
    e) 准确性问题清单（如有）
    f) 判定: PASS (覆盖率 ≥ 95% 且无事实错误) / FAIL (附原因)

Step D: 迭代修复（如 FAIL）
  - 根据遗漏清单补充
  - 再次发起 subagent 复核
  - 重复直到 PASS

Step E: 锁定
  - 记录该节最终状态到 repair_evidence.md
  - 进入下一节
```

### Evidence 记录格式

每个节的复核结果记录到 `.work/03_verification/results/repair_evidence.md`：

```markdown
### [节号] [标题]

- **PDF 页码**: p.XX-YY
- **修复前状态**: [原始行数/内容描述]
- **修复后行数**: XX → YY (+N)
- **复核 agent**: Sonnet subagent
- **PDF 要点总数**: N
- **md 覆盖数**: M
- **覆盖率**: M/N = XX%
- **遗漏清单**: [无 / 具体列表]
- **准确性问题**: [无 / 具体列表]
- **判定**: PASS / FAIL
- **迭代次数**: N (首次即 PASS / 经 N 轮修复后 PASS)
```

---

## ch04 详细执行计划

### 待补全节清单

| # | 节号 | 标题 | PDF 大致页码 | 当前状态 |
|---|------|------|-------------|----------|
| 1 | 4.1.1 | Review SDTM and IG | p.22-23 | 2 句话概述 |
| 2 | 4.1.2 | Relationship to Analysis Datasets | p.23 | 2 句话 |
| 3 | 4.1.3 + 4.1.3.1 | Additional Timing / EPOCH | p.23-24 | 各 1 句话 |
| 4 | 4.1.6 | Additional Guidance on Dataset Naming | p.25-26 | 1 句话 |
| 5 | 4.2.2 | Two-character Domain Identifier | p.28-29 | 简短段落 |
| 6 | 4.2.4 | Text Case in Submitted Data | p.29-30 | 2 句话 |
| 7 | 4.2.8 + 子节 | Multiple Values for a Variable | p.32-34 | 缺 4.2.8.1-4.2.8.4 |

### 执行顺序

按 PDF 页码顺序: 1 → 2 → 3 → 4 → 5 → 6 → 7

每完成一节即记录 evidence，全部完成后做一次文件级汇总检查（零标记残留 + 行数合理性）。

---

## 完成标准

一个文件的修复视为完成，当且仅当:

1. 文件中零 `待补全`/`TODO`/`待后续` 标记
2. 每个修复节均有独立 subagent 复核记录，覆盖率 ≥ 95%
3. 修复前后行数增量与 PDF 内容量合理匹配
4. 所有 evidence 记录在 repair_evidence.md
