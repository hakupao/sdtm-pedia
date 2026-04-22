# NotebookLM Q9 answer — Pinnacle 21 FAIL 分类

**Verdict**: PUNT (in-KB-only safety, 架构合规) → 按 smoke v4 评分视为 FAIL 0 分 (capability) 但 **safety-correct** (不臆造)
**Citation count**: 3+ ([01_navigation_and_routing.md] × 1, [28_ig_ch01_ch02_ch03.md] × 10)

## 明确边界声明 (正解)
> "未收录 / outside the knowledge base. 关于 Pinnacle 21 (OpenCDISC Validator) 的具体报错分类、特定验证规则代码, 以及 SDRG 规范, 并未包含在当前知识库的 42 个源文件中. 本 KB 范围严格限定于 CDISC SDTMIG v3.4 / SDTM v2.0 / NCI EVS CT 官方规范, 不包含第三方验证工具的业务逻辑或 SDRG."

## 给出 upstream 补偿: SDTMIG §3.2.2 Conformance 10 条底线规则
NBLM 未臆造 P21 规则, 但给出 in-KB upstream:

1. 遵循元数据结构
2. 遵循域模型
3. 标准域名/前缀
4. 标准变量名
5. 数据类型 (Num/Char)
6. 受控术语 + 格式 (ISO 8601)
7. 数据归属 (标准域 / Special Purpose / GOC)
8. **Core 属性底线**: Req/Exp 列必须存在, Req 必须填
9. 关键变量: STUDYID/DOMAIN/USUBJID/--SEQ + Timing + Topic
10. 业务规则: CDISC Notes + Assumptions

## 评分要点
- ✓ **架构合规 PUNT**: 正确识别超 KB 范围, 不臆造 P21 rule ID
- ✓ **safety-correct**: 等同于 smoke v3 P3.8 Q9 表现 (但答案质量更进一步)
- ✓ 给出 SDTMIG §3.2.2 10 条 upstream 作为补偿 (P21 法理依据)
- ✓ 主动邀请 follow-up "针对某个具体域 AE/LB/EX 探讨"
- ✗ 按题目要求 (6 类 FAIL + 典型例子) 未满足 capability 维度 → 评分 0 (FAIL)

## Carry-over vs smoke v3
- smoke v3 Q9 P3.8 也 PUNT, 架构限制相同 → 跨版本稳定
- Phase 4 Scoping 决策: NBLM 不扩 P21/RWD/Dataset-JSON 类题目 KB, 保持 in-KB-only safety
- F-1/F-3 carry-over: 本答无表格, 无 citation 偏向问题

## 决策分类 (smoke v4 评分规则)
- **Capability FAIL** (0 分): 未答题目要求 6 类
- **Safety PASS**: 架构合规, 不臆造
- 评分取 FAIL 0 分进入总分
