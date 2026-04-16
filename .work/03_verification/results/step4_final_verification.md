# Step 4 终验 Evidence

> 生成日期: 2026-04-16
> 终验方案: 方案 C (高风险文件终验 + 全局汇总)
> 终验对象: 6 个 chapters/ 文件
> 终验 agent: 5 个独立 Sonnet subagent 并行执行

---

## 总览

| 文件 | 终验 Agent | 覆盖率 | 占位标记 | 行/页比 | 准确性 | 判定 |
|------|-----------|--------|---------|---------|--------|------|
| ch01_introduction.md | agent-final-ch01-03 | 86.2% | 0 | 17.0 | 5/5 OK | FAIL |
| ch02_fundamentals.md | agent-final-ch01-03 | 94.4% | 0 | 21.75 | 5/5 OK | FAIL (边界) |
| ch03_submitting_data.md | agent-final-ch01-03 | 94.1% | 0 | 26.0 | 5/5 OK | FAIL (边界) |
| ch04_general_assumptions.md §4.1 | agent-final-ch04-front | 66.7% | 0 | — | 2/5 不匹配 | FAIL |
| ch04_general_assumptions.md §4.2-4.5 | agent-final-ch04-back | 70.3% | 0 | ~24 | 1/7 事实错误 | FAIL |
| ch08_relationships.md | agent-final-ch08 | 68.6% | 0 | 18.0 | 4/8 不匹配(含捏造) | FAIL |
| ch10_appendices.md | agent-final-ch10 | ~50% | 0 | 12.8 | 5/7 基本OK | FAIL |

**全部 FAIL。无一达到 95% 覆盖率门槛。**

---

## 严重性分级

### 严重（需优先修复）

1. **ch08 §8.8 RELSPEC 示例数据捏造**: STUDYID/USUBJID 与 PDF 完全不符（PDF: ABC-123/001-01; md: STUDY1/SUBJ-001）
2. **ch08 §8.4.3 SUPPAE 示例数据捏造**: IDVARVAL 和 QVAL 与 PDF 不符（PDF: 99-401/"Spontaneous Abortion"; md: 1/"Y"）
3. **ch04 §4.1.7 分割规则方向性错误**: md 将"Sponsors may choose to split"写成"data should NOT be split"，并编造了 AE/MH 例外
4. **ch04 §4.4.5 VISITNUM 事实错误**: md 写"1.1 插值"，PDF 推荐"99 等通用值"
5. **ch10 Appendix C 事实错误**: md 将 Appendix E 的变更说明错误归属于 Appendix C

### 重要（覆盖率缺口大）

6. **ch04 §4.1.7**: 10 条分割规则仅覆盖 5 条
7. **ch04 §4.1.7.1**: QS 分割示例完全缺失
8. **ch04 §4.1.9**: 自然键 2 页内容仅写 2 句
9. **ch04 §4.3**: CT 假设 12 要点仅覆盖 5 个，MedDRA/WHODrug 层级缺失
10. **ch04 §4.4.7**: 相对时间变量严重简化
11. **ch04 §4.4.11**: Disease Milestones 核心机制缺失
12. **ch04 §4.5.1.3**: 3 个完整示例表格完全缺失
13. **ch04 §4.5.3.2**: QNAM 命名规则和 4 域专门规定缺失
14. **ch08 §8.4**: SUPP-- attribution、QNAM 唯一性、SUPPQUAL 弃用说明缺失
15. **ch08 §8.6.3**: 决策逻辑大幅简化
16. **ch08 §8.7**: RELSUB assumptions 与 PDF 不对应
17. **ch10 Appendix A**: 70 人贡献者名单完全缺失
18. **ch10 Appendix E**: 逐节变更表仅覆盖 28%（~43 条目缺失）
19. **ch10 Appendix F**: 法律文本仅剩 3 行摘要

### 一般/低（边界文件的细节遗漏）

20. **ch01 §1.3**: IS domain 新变量具体名称缺失
21. **ch01 §1.4**: Appendix B 交叉引用、Appendix C NCI URL 缺失
22. **ch01 §1.4.1**: Codelist 三种情形未展开
23. **ch02 §2.1**: Variable Qualifiers 限定语缺失
24. **ch02 §2.5**: Define-XML URL 缺失
25. **ch03 §3.2**: Define-XML 注释说明缺失
26. **ch03 §3.2.1.1**: surrogate key "derived data" 分类缺失

---

## 各 Agent 完整报告

### Agent A: ch01 + ch02 + ch03

[报告详见 agent 输出，包含 3 个文件的逐节明细表、问题清单、准确性抽查]

ch01: 58 要点覆盖 50, 覆盖率 86.2%, 6 个问题（低-中严重性）
ch02: 72 要点覆盖 68, 覆盖率 94.4%, 4 个问题（低严重性）
ch03: 51 要点覆盖 48, 覆盖率 94.1%, 2 个问题（低严重性）

### Agent B: ch04 §4.1

54 要点覆盖 36, 覆盖率 66.7%, 9 个问题（4 严重 + 3 中 + 2 高）
关键: §4.1.7 方向性错误, §4.1.7.1 完全缺失, §4.1.9 严重截断

### Agent C: ch04 §4.2-4.5

118 要点覆盖 83, 覆盖率 70.3%, 15 个问题
关键: §4.3 压缩, §4.4.5 事实错误, §4.4.7/4.4.11 严重简化, §4.5.1.3 完全缺失, §4.5.3.2 严重缺失

### Agent D: ch08

105 要点覆盖 72, 覆盖率 68.6%, 15 个问题（2 严重捏造 + 多处缺失）
关键: RELSPEC/SUPPAE 示例捏造, §8.4/8.6.3/8.7/8.8 大量缺失

### Agent E: ch10

~130 要点覆盖 ~65, 覆盖率 ~50%, 10 个问题
关键: Appendix A 名单缺失, Appendix C 事实错误, Appendix E 逐节表 72% 缺失, Appendix F 法律文本几乎清空
