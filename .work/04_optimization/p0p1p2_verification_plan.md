# Phase 6 P0/P1/P2 验证计划

> 创建日期: 2026-04-16
> 状态: **已完结** (2026-04-16)
> 验证对象: ROUTING.md (P0) + Cross References (P1) + VARIABLE_INDEX.md (P2)
> 阶段流程: 需求 → 方案 → 实现 → 汇报 → 修复 → 复核 → 收尾 → 完结

---

## 一、需求

Phase 6 P0-P2 三项检索优化已完成实施，但缺少独立验证环节。
根据项目 retrospective §4 的教训（"自写自判"是 Issue 2 根因），必须对产出物做独立验证。

**验证目标**:
1. **正确性** — 数据与源头一致，无错链/漏引/多引
2. **完备性** — 该覆盖的范围全覆盖，无遗漏
3. **精度** — 路由规则确实能把问题引导到正确文件（功能性验证）
4. **无副作用** — 追加的 Cross References 未破坏 spec.md 原有内容

---

## 二、方案

### 验证对象清单

| 产出物 | 文件 | 关键指标 |
|--------|------|----------|
| P0 ROUTING.md | `knowledge_base/ROUTING.md` (1 文件) | 7 类路由规则，引用 ~30 个文件路径 |
| P1 Cross References | `knowledge_base/domains/*/spec.md` 末尾 (63 文件) | 588 个 CT 引用，63 个域分组，~30 个域间关联 |
| P2 VARIABLE_INDEX.md | `knowledge_base/VARIABLE_INDEX.md` (1 文件) | 1523 唯一变量，1917 条目，63 域 |

### 验证层次与执行顺序

```
Layer 1: 程序化验证 (V1-V5)  ← Python 脚本全自动，100% 覆盖
  V1 链接完整性 ─┐
  V2 CT 一致性  ─┤
  V3 变量计数   ─┤ (独立，可并行)
  V4 域归类     ─┤
  V5 回归检查   ─┘
         ↓ 全部 PASS 后
Layer 2: 功能性验证 (V6-V8)  ← 设计测试问题，端到端验证精度
  V6 路由准确性 ─┐
  V7 交叉引用完备性 ─┤ (独立，可并行)
  V8 反向索引精度 ─┘
         ↓
汇总报告 → 修复(如需) → 复核
```

---

### V1: 链接完整性

- **范围**: ROUTING.md + VARIABLE_INDEX.md + 63 个 spec.md 的 Cross References 段
- **方法**: Python 脚本提取所有 Markdown 相对链接 `[text](path)` → 解析为绝对路径 → `os.path.exists()` 检查
- **PASS 标准**: 0 个悬空链接
- **产出**: 链接清单 + 检查结果

### V2: CT Code 双向一致性

- **范围**: 63 个 spec.md (变量定义中的 Controlled Terms 字段) ↔ 63 个 Cross References 的 CT 段
- **方法**: Python 脚本做双向比较:
  - **正向**: spec.md 变量定义中每个 CT Code → Cross References 中是否有对应条目？
  - **反向**: Cross References 中每个 CT Code → spec.md 变量定义中是否真的引用了？
- **PASS 标准**: 正向 0 漏引，反向 0 多引
- **产出**: 逐域比较表 + 差异清单

### V3: 变量计数一致性

- **范围**: 63 个 spec.md ↔ VARIABLE_INDEX.md
- **方法**: Python 脚本:
  - 从每个 spec.md 提取变量名列表（匹配 `### VARNAME` 标题行）
  - 从 VARIABLE_INDEX.md 提取每个域的变量名列表
  - 逐域比较: spec.md 有但 INDEX 没有 / INDEX 有但 spec.md 没有
- **PASS 标准**: 63 域全部一致，总数 1917
- **产出**: 逐域计数对比表 + 差异清单

### V4: 域归类正确性

- **范围**: 63 个 spec.md 的 class 声明 ↔ Cross References 中 "Same class" 列表
- **方法**: Python 脚本:
  - 从每个 spec.md 第 2-3 行提取 `> Class: XXX`
  - 从 Cross References 提取 `Same class (XXX):` 后的域列表
  - 验证: 同 class 下的域集合是否互相完整引用
- **PASS 标准**: 0 个归类错误
- **产出**: class 分组表 + 差异清单

### V5: 回归检查（全量）

- **范围**: 全部 63 个 spec.md
- **方法**: Python 脚本检查每个 spec.md:
  - Cross References 段是否在文件最末尾（段后无其他内容）
  - Cross References 段之前的内容行数与 git 追加前是否一致（`git show HEAD~1:path` 对比）
- **PASS 标准**: 63/63 原有内容无变化，Cross References 均在末尾
- **产出**: 逐文件检查结果

### V6: 路由准确性（功能性）

- **范围**: ROUTING.md 的 7 类路由规则
- **方法**: 设计 15 个测试问题（每类至少 2 个），执行流程:
  1. 读 ROUTING.md 确定路由路径
  2. 按路径读取目标文件
  3. 判定: 目标文件是否包含完整答案？

- **测试问题**:

  | # | 类型 | 测试问题 | 预期路由路径 |
  |---|------|---------|-------------|
  | Q1 | 变量定义 | AETERM 是什么变量？属性是什么？ | VARIABLE_INDEX → AE/spec.md |
  | Q2 | 变量定义 | USUBJID 出现在哪些域？ | VARIABLE_INDEX §一 通用变量 |
  | Q3 | 变量定义 | EPOCH 在 AE 域中是什么角色和 Core？ | VARIABLE_INDEX → AE/spec.md |
  | Q4 | 编码/术语 | AESER 可以填什么值？ | AE/spec.md → CT C66742 → terminology/core/general_part4.md |
  | Q5 | 编码/术语 | C66767 是什么 codelist？包含哪些值？ | VARIABLE_INDEX §三 → terminology/core/ae.md |
  | Q6 | 编码/术语 | QS 域的问卷编码在哪里找？ | ROUTING → terminology/questionnaires/ |
  | Q7 | 业务规则 | AE 数据收集有哪些通用假设？ | AE/assumptions.md + ch04 |
  | Q8 | 业务规则 | EPOCH 变量的使用规则是什么？ | ch04 §4.4 |
  | Q9 | 域间关系 | AE 和 CM 怎么关联？ | ch08 + RELREC/ + AE Cross Ref |
  | Q10 | 域间关系 | SUPPQUAL 怎么使用？ | SUPPQUAL/ + ch08 §8.4 |
  | Q11 | 实现示例 | 给我看一个交叉试验的 TA 设计示例 | TA/examples.md |
  | Q12 | 实现示例 | PC 和 PP 数据怎么关联？ | PC/examples.md + PP/examples.md |
  | Q13 | 概念/模型 | Events 和 Findings class 有什么区别？ | model/02_observation_classes.md |
  | Q14 | 跨域查询 | 哪些变量引用了 CT Code C66742？ | VARIABLE_INDEX §三 |
  | Q15 | 跨域查询 | Events class 包含哪些域？ | VARIABLE_INDEX §二 域分组 或 INDEX.md |

- **PASS 标准**: 15/15 路由到正确文件且文件中确实包含答案
- **产出**: 逐题验证记录（路由路径 → 读取文件 → 答案摘要 → PASS/FAIL）

### V7: 交叉引用完备性（功能性）

- **范围**: 需要跨文件回答的问题
- **方法**: 设计 6 个跨域问题，从起始文件出发，**仅靠 Cross References 段的指引**看能否到达所有必要文件

- **测试问题**:

  | # | 问题 | 起点 | 预期需要的全部文件 |
  |---|------|------|-------------------|
  | X1 | AEACN 可以填什么值？ | AE/spec.md | + terminology/core/ae.md (via Cross Ref CT 段) |
  | X2 | DM 域的 SEX 变量有哪些允许值？ | DM/spec.md | + terminology/core/dm.md (via Cross Ref CT 段) |
  | X3 | AE 和 FA 的关系是什么？ | AE/spec.md | + FA/ (via Cross Ref Related Domains) |
  | X4 | MB 和 MS 共享 examples 吗？ | MB/spec.md | + MS/ (via Cross Ref Related Domains) |
  | X5 | EX 变量的通用命名规则 | EX/spec.md | + ch04 (via Cross Ref General References) |
  | X6 | RELREC 的结构定义在模型哪里？ | RELREC/spec.md | + model/06 (via Cross Ref Model Definition) |

- **PASS 标准**: 6/6 能通过 Cross References 到达所有必要文件
- **产出**: 逐题路径追踪记录

### V8: 反向索引精度（功能性）

- **范围**: VARIABLE_INDEX.md
- **方法**: 抽 10 个变量，在 VARIABLE_INDEX 中查找，然后对照 spec.md 验证每个字段
- **抽样策略**: 覆盖不同类型
  - 3 个通用变量: STUDYID (63域), EPOCH (44域), SPDEVID (6域)
  - 5 个专属变量: AETERM (AE), LBTESTCD (LB), EXDOSE (EX), DSSTDTC (DS), TSVAL (TS)
  - 2 个边界变量: NHOID (4域, 含 OI 特殊域), MIDSTYPE (2域)
- **验证点**: 域列表正确、Label 正确、Type 正确、Role 正确、Core 正确、CT 正确
- **PASS 标准**: 10/10 全部字段匹配
- **产出**: 抽样比对表

---

## 三、实现

### 3.1 脚本开发

创建 `.work/04_optimization/scripts/verify_p0p1p2.py`，包含 V1-V5 五个验证函数:

```python
def verify_v1_link_integrity():     # 链接完整性
def verify_v2_ct_consistency():     # CT 双向一致性
def verify_v3_variable_counts():    # 变量计数一致性
def verify_v4_class_grouping():     # 域归类正确性
def verify_v5_regression_check():   # 回归检查（全量 63 文件）
```

脚本输出格式:
```
=== V1: Link Integrity ===
Scanned: 65 files, N links
PASS: N/N links valid
Broken: 0

=== V2: CT Code Consistency ===
Domain AE: spec→xref 8/8, xref→spec 8/8 ✓
...
PASS: 63/63 domains consistent

=== V3: Variable Counts ===
Domain AE: spec=34, index=34 ✓
...
PASS: 63/63 domains match, total 1917/1917

=== V4: Class Grouping ===
Events: {AE,BE,CE,DS,DV,HO,MH} — 7 domains, all cross-ref ✓
...
PASS: 8/8 classes correct

=== V5: Regression Check ===
AE/spec.md: original=545 lines, xref starts at 546 ✓
...
PASS: 63/63 files intact
```

### 3.2 功能性验证执行

V6-V8 由 AI agent 按测试问题逐题执行:
- 每题记录: 路由路径 → 读取的文件 → 是否找到答案 → PASS/FAIL
- 失败项记录具体原因和缺失内容

---

## 四、汇报

验证完成后，生成汇总报告: `.work/04_optimization/p0p1p2_verification_report.md`

报告结构:
```markdown
# Phase 6 P0/P1/P2 验证报告

## 汇总

| 验证项 | 范围 | 结果 | 发现问题数 |
|--------|------|------|-----------|
| V1 链接完整性 | 65文件/N链接 | PASS/FAIL | X |
| V2 CT 一致性 | 63域/N CT | PASS/FAIL | X |
| V3 变量计数 | 63域/1917变量 | PASS/FAIL | X |
| V4 域归类 | 8 class/63域 | PASS/FAIL | X |
| V5 回归检查 | 63文件 | PASS/FAIL | X |
| V6 路由准确性 | 15题 | N/15 PASS | X |
| V7 交叉引用完备性 | 6题 | N/6 PASS | X |
| V8 反向索引精度 | 10变量 | N/10 PASS | X |

## 详细结果
### V1-V5: 程序化验证
(脚本输出)
### V6-V8: 功能性验证
(逐题记录)

## 发现的问题清单
| # | 来源 | 问题描述 | 严重性 | 修复建议 |
```

---

## 五、修复

当汇报中存在 FAIL 项时，进入修复流程:

1. **分类**: 将 FAIL 项按严重性排序
   - **阻断性**: 链接悬空、变量缺失、CT 错误 → 必须修复
   - **非阻断性**: 边界 case、格式瑕疵 → 记录但可暂缓
2. **修复**: 逐项修复，每项修复后立即重跑对应 V 项
3. **连带重验**: 如果修复涉及修改 spec.md 内容 → 必须重跑 V5 回归检查
4. **更新报告**: 修复结果追加到验证报告的"修复记录"段

修复流程图:
```
FAIL 项 → 分类排序 → 逐项修复 → 重跑对应 V 项
                                    ↓
                              改了 spec.md？ → 是 → 重跑 V5
                                    ↓ 否
                              更新报告 → 下一项
```

---

## 六、复核

对验证过程本身的质量检查:

### 6.1 脚本逻辑复核
- 选 3 个域 (AE, DM, RELREC) 手动计算预期结果
- 与脚本输出比对，确认脚本逻辑无误
- 相当于验证脚本的 unit test

### 6.2 功能性验证复核
- 用户审阅 V6-V8 的逐题判定记录
- 重点检查: PASS 的判定理由是否合理（避免"假 PASS"）
- 对任何存疑的判定，要求 agent 提供原文摘录作为证据

---

## 七、收尾

1. 将验证中发现的新问题写入 `issues_found.md`（如有）
2. 更新 `retrieval_optimization.md` 中 P0/P1/P2 状态为"**已验证**"
3. 沿 Chain B 更新: `worklog.md` → `progress.json` → `docs/PROGRESS.md`

---

## 八、完结

**完结标准**:
- [x] V1-V5 程序化验证全部 PASS (2026-04-16)
- [x] V6 路由准确性 15/15 PASS (2026-04-16)
- [x] V7 交叉引用完备性 6/6 PASS (2026-04-16)
- [x] V8 反向索引精度 9/10 → 修复后 10/10 PASS (2026-04-16)
- [x] 发现的问题全部修复并重验 — F1 MIDSTYPE 已修复 (2026-04-16)
- [x] 复核通过 — 脚本 3 个 bug 已修复，功能性验证由独立 agent 执行 (2026-04-16)
- [x] Chain B 更新完成 — worklog + PROGRESS.md 已更新 (2026-04-16)
- [x] 验证报告已生成 — p0p1p2_verification_report.md (2026-04-16)

**Phase 6 P0-P2 验证正式完结。** (2026-04-16)
