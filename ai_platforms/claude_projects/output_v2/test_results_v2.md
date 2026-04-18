# v2 A/B 测试结果矩阵

> 用户每阶段后回填; 主控写入并归档到 evidence_v2/stage_v2.X_audit.md

## T1-T8 回归 (源自 v1)

| # | 题目 | 期望 | v1 答案 | v2.X 答案 | 精度 | 阶段 |
|---|-----|------|--------|----------|------|------|
| T1 | AE.AEDECOD 的 Core 属性是什么? | Expected | TBD | TBD | TBD | TBD |
| T2 | AE 严重程度变化如何记录? | AEGRPID 方案 | TBD | TBD | TBD | TBD |
| T3 | PC↔PP 通过 RELREC 关联的 4 种方法? | Method A-D | TBD | TBD | TBD | TBD |
| T4 | 哪些域有 EPOCH 变量? | 完整列表 | TBD | TBD | TBD | TBD |
| T5 | 如何判断变量是否需要提交到 SUPP--? | ch08 §8.4 规则 | TBD | TBD | TBD | TBD |
| T6 | AE Example 2 的具体数据是什么? | 数据表 | TBD | TBD | TBD | TBD |
| T7 | CT Code C66742 有哪些具体值? | 完整 Term 表 | TBD | TBD | TBD | TBD |
| T8 | CV 域所有变量值范围? | "需查 examples/terminology" | TBD | TBD | TBD | TBD |

## T9-T20 新增 (覆盖 v2 五批)

| # | 批 | 题目 | 期望 | v1 答案 | v2.X 答案 | 精度 |
|---|----|-----|------|--------|----------|------|
| T9  | 1 | ch01 SDTM 整体架构 + Foundational concepts? | 完整段落 | (FAIL 期望) | TBD | TBD |
| T10 | 1 | ch02 §2.6 创建新 domain 的所有步骤? | 完整列表 | (FAIL 期望) | TBD | TBD |
| T11 | 1 | ch08 §8.3 RELREC 数据集关系示例完整流程? | 完整规则+示例 | TBD | TBD | TBD |
| T12 | 1 | ch10 附录所有 entity 列表? | 完整 | (FAIL 期望) | TBD | TBD |
| T13 | 2 | DM 的 Example 1 完整数据表? | 表格 | (兜底模板) | TBD | TBD |
| T14 | 2 | EX 剂量调整 Example 数据怎么写? | 表格 | (兜底) | TBD | TBD |
| T15 | 3 | RP 域 Example 数据? | 表格 | (兜底) | TBD | TBD |
| T16 | 3 | FT 域 Example 数据? | 表格 | (兜底) | TBD | TBD |
| T17 | 4 | C66742 codelist 所有 Term 值 + Definition? | 完整 Term 表 | (兜底) | TBD | TBD |
| T18 | 4 | AERELN codelist 全部 Synonyms? | Synonyms 字段 | TBD | TBD | TBD |
| T19 | 5 | FREQ codelist (中频) 全部 Term + Code? | 表格 | TBD | TBD | TBD |
| T20 | 5 | PROBLEM_TYPE codelist (中频) 全部值? | 表格 | TBD | TBD | TBD |

## 阶段汇总

(每阶段完成后追加一段)
