# Phase 6 P0/P1/P2 验证报告

> 执行日期: 2026-04-16
> 执行方案: `.work/04_optimization/p0p1p2_verification_plan.md`
> 验证脚本: `.work/04_optimization/scripts/verify_p0p1p2.py`

---

## 汇总

| 验证项 | 范围 | 结果 | 发现问题数 |
|--------|------|------|-----------|
| V1 链接完整性 | 65 文件 / 724 链接 | **PASS** | 0 |
| V2 CT 双向一致性 | 63 域 | **PASS** | 0 |
| V3 变量计数一致性 | 63 域 / 1917 变量 | **PASS** | 0 |
| V4 域归类正确性 | 8 class / 63 域 | **PASS** | 0 |
| V5 回归检查 | 63 文件 | **PASS** | 0 |
| V6 路由准确性 | 15 题 | **15/15 PASS** | 0 |
| V7 交叉引用完备性 | 6 题 | **6/6 PASS** | 0 |
| V8 反向索引精度 | **1523 变量全量** | **PASS** | 9 (全部已修复) |

**总体结论**: 8/8 验证项全部 PASS。V8 升级为全量 1523 变量验证，发现 9 个通用变量 Role 跨域差异缺星号，全部已修复。

---

## 详细结果

### Layer 1: 程序化验证 (V1-V5)

#### V1: 链接完整性
- 扫描范围: ROUTING.md + VARIABLE_INDEX.md + 63 个 spec.md Cross References
- 总链接数: 724
- 悬空链接: 0
- **结果: PASS**

#### V2: CT Code 双向一致性
- 正向 (spec→xref): 63/63 域全部覆盖，0 漏引
- 反向 (xref→spec): 63/63 域全部一致，0 多引
- **结果: PASS**
- 注: 脚本初版因未解析分号分隔的多 CT 字段（如 `C85494; C128684`）而误报 14 个"多余" CT，修复后全部 PASS

#### V3: 变量计数一致性
- 63 域逐域比对: 全部一致
- 总变量数: spec=1917, index=1917
- **结果: PASS**
- 注: 脚本初版因"除…外所有域"解析优先级 bug 而误报 5 域不匹配，修复后全部 PASS

#### V4: 域归类正确性
- 8 个 class 分组:
  - Events: AE, BE, CE, DS, DV, HO, MH (7)
  - Findings: CP, CV, DA, DD, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SR, SS, TU, TR, UR, VS (32)
  - Findings About: FA, SR (注: FA 同时归入 Findings)
  - Interventions: AG, CM, EC, EX, ML, PR, SU (7)
  - Relationship: RELREC, RELSPEC, RELSUB, SUPPQUAL (4)
  - Special-Purpose: CO, DM, SE, SM, SV (5)
  - Study Reference: OI (1)
  - Trial Design: TA, TD, TE, TI, TM, TS, TV (7)
- **结果: PASS**

#### V5: 回归检查（全量）
- 63 个 spec.md 的 Cross References 段前原有内容与 git 历史 (commit 86d761a) 完全一致
- Cross References 段均在文件最末尾
- **结果: PASS**
- 注: 生成脚本在 Cross References 前添加了 `---` 分隔线，属于预期视觉分隔，不影响原有内容

---

### Layer 2: 功能性验证 (V6-V8)

#### V6: 路由准确性 (15 题)

| # | 类型 | 问题 | 路由结果 | 判定 |
|---|------|------|----------|------|
| Q1 | 变量定义 | AETERM 是什么？属性？ | VARIABLE_INDEX → AE/spec.md，找到完整定义 | **PASS** |
| Q2 | 变量定义 | USUBJID 出现在哪些域？ | VARIABLE_INDEX §一，列出 55 域 | **PASS** |
| Q3 | 变量定义 | EPOCH 在 AE 中的 Role/Core？ | VARIABLE_INDEX → AE/spec.md: Timing/Perm | **PASS** |
| Q4 | 编码/术语 | AESER 可以填什么值？ | AE/spec.md → C66742 → terminology/core/general_part4.md | **PASS** |
| Q5 | 编码/术语 | C66767 是什么 codelist？ | VARIABLE_INDEX §三 → terminology/core/ae.md: 8 个值 | **PASS** |
| Q6 | 编码/术语 | QS 问卷编码在哪？ | ROUTING → terminology/questionnaires/ (43 文件) | **PASS** |
| Q7 | 业务规则 | AE 数据收集假设？ | AE/assumptions.md: 8 条详细假设 | **PASS** |
| Q8 | 业务规则 | EPOCH 使用规则？ | ch04 §4.1.3.1 + §4.4 | **PASS** |
| Q9 | 域间关系 | AE 和 CM 怎么关联？ | ch08 §8.2 + AE Cross Ref: RELREC | **PASS** |
| Q10 | 域间关系 | SUPPQUAL 怎么用？ | SUPPQUAL/ + ch08 §8.4 | **PASS** |
| Q11 | 示例 | 交叉试验 TA 设计？ | TA/examples.md Example 2: 含 Mermaid 图 | **PASS** |
| Q12 | 示例 | PC/PP 数据关联？ | PC/examples.md: 4 种 RELREC 方法详解 | **PASS** |
| Q13 | 概念 | Events vs Findings 区别？ | model/02_observation_classes.md: 三大类定义 | **PASS** |
| Q14 | 跨域 | 哪些变量引用 C66742？ | VARIABLE_INDEX §三: 123 个变量 | **PASS** |
| Q15 | 跨域 | Events class 包含哪些域？ | INDEX.md + VARIABLE_INDEX §二: 7 域 | **PASS** |

- **结果: 15/15 PASS**
- 观察: Q8 中 ROUTING.md 引导到 ch04 §4.4（通用时间变量），EPOCH 专门指导在 §4.1.3.1，两者都在 ch04 中，功能正确但可更精确

#### V7: 交叉引用完备性 (6 题)

| # | 问题 | 起点 | Cross Ref 能否到达所有必要文件 | 判定 |
|---|------|------|-------------------------------|------|
| X1 | AEACN 可选值？ | AE/spec.md | → terminology/core/ae.md (C66767): 8 个值 | **PASS** |
| X2 | DM SEX 允许值？ | DM/spec.md | → terminology/core/dm.md (C66731): 4 个值 | **PASS** |
| X3 | AE↔FA 关系？ | AE/spec.md | → "Findings About: FA": AEPRESP 预设 AE | **PASS** |
| X4 | MB/MS 共享 examples？ | MB/spec.md | → "Shared Dataset: MS": 确认共享 | **PASS** |
| X5 | EX 命名规则？ | EX/spec.md | → ch04: §4.2.1 变量命名规范 | **PASS** |
| X6 | RELREC 模型定义？ | RELREC/spec.md | → model/06: §6.1 RELREC 完整定义 | **PASS** |

- **结果: 6/6 PASS**

#### V8: 反向索引精度 (10 变量)

**已升级为全量验证** (脚本: `.work/04_optimization/scripts/verify_v8_full.py`)

| 类别 | 数量 | 验证字段 | 结果 |
|------|------|----------|------|
| 通用变量 | 24 | 域列表 + Label + Type + Role星号 + Core星号 | **PASS** |
| 专属变量 | 1499 | Label + Type + Role + Core + CT (逐字段精确匹配) | **PASS** |
| **合计** | **1523 (1917条目)** | | **0 错误** |

修复的 9 个通用变量 Role 跨域差异缺星号:

| 变量 | 域数 | Role 差异 | 修复 |
|------|------|-----------|------|
| MIDSTYPE | 2 | SM=Record Qualifier, TM=Topic | 加星号 |
| VISIT | 36 | 多数 Timing, SV=Synonym Qualifier | 加星号 |
| VISITNUM | 36 | 多数 Timing, TV=Topic | 加星号 |
| ARMCD | 3 | DM=Record Qualifier, TA/TV=Topic | 加星号 |
| ETCD | 3 | SE=Record Qualifier, TA/TE=Topic | 加星号 |
| IDVAR | 3 | CO=Identifier, RELREC/SUPPQUAL=Record Qualifier | 加星号 |
| IDVARVAL | 3 | CO=Identifier, RELREC/SUPPQUAL=Record Qualifier | 加星号 |
| RDOMAIN | 3 | CO=Identifier, RELREC/SUPPQUAL=Record Qualifier | 加星号 |
| MIDS | 2 | ML=Timing, SM=Topic | 加星号 |

- **结果: 全量 PASS (修复后 0 错误)**

---

## 发现的问题清单

| # | 来源 | 问题描述 | 严重性 | 状态 |
|---|------|---------|--------|------|
| F1-F9 | V8 全量 | 9 个通用变量 (MIDSTYPE, VISIT, VISITNUM, ARMCD, ETCD, IDVAR, IDVARVAL, RDOMAIN, MIDS) 的 Role 存在跨域差异但 INDEX 中未加星号标注 | 非阻断性 | **全部已修复** — 添加 Role 星号，重验 V1-V5 + V8 全量 PASS |

**影响评估**: VARIABLE_INDEX 原有的星号惯例仅覆盖 Core 字段的跨域差异，未扩展到 Role 字段。全量验证发现 24 个通用变量中有 9 个存在 Role 跨域差异，全部已修复。用户查某变量在特定域中的角色时不会再被误导。

---

## 脚本 bug 修复记录

验证过程中发现并修复了 3 个脚本 bug（均为验证脚本自身的解析问题，非数据问题）:

| # | 影响 V 项 | 问题 | 修复 |
|---|-----------|------|------|
| B1 | V3 | "除…外所有域"中含"所有域"子串，误入全量分支 | 调整判断优先级：先检查"除…外"再检查"所有域" |
| B2 | V5 | Cross Ref 前的 `---` 分隔符 + 空行被误判为内容变更 | 比较前去除尾部 `---` 分隔符 |
| B3 | V2 | CT 字段含多个分号分隔 Code 时只提取第一个 | 改用 `findall` 提取所有 C-code |
