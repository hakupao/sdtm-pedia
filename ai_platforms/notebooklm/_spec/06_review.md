# 06 审查 & A/B 回归

规则 A (语义抽检) + 规则 D (写审分离) 的执行落地. 每批的强制子步骤 + 终态整合.

---

## 三 Lane 审查模型

```
Writer lane         Reviewer lane              主控 (Coordinator)
──────────          ──────────────             ──────────────────
executor            code-reviewer              独立抽样
  │                    │                           │
  ▼                    ▼                           ▼
 产出 ────────► 审 ────────► 审 ────────► [合意 | 不合意]
                                               │
                                               ▼
                                              决策继续 / 重试 / 归档
```

三 lane 必须**不同 subagent_type** (规则 D), 禁止同一 context 自审.

---

## Lane 1: Writer (Executor subagent)

**职责**: 产出内容 (脚本代码 / 合并文件 / System Prompt 段 / RETROSPECTIVE 草稿).

**subagent_type 选项**:
- `executor` (通用) — model=opus 复杂 / model=sonnet 简单
- `feature-dev:code-architect` — 架构设计
- `oh-my-claudecode:writer` — 文档写作

**prompt 要求**:
- 明示输入文件 / 期望产物 / 验收标准
- 禁止读 reviewer 产物 (P6 上下文隔离)
- 每次调用的 prompt **归档到** `dev/evidence/subagent_prompts/<stage>_<role>_<N>.md`

---

## Lane 2: Reviewer (Code-reviewer subagent)

**职责**: 独立复核 Writer 产物.

**subagent_type 选项**:
- `code-reviewer` (通用)
- `oh-my-claudecode:code-reviewer` (带严重度评级)
- `feature-dev:code-reviewer` (feature 维度)
- `pr-review-toolkit:code-reviewer` (检查项目约定)

**必须**: 与 Lane 1 不同 subagent_type.

**prompt 要求**:
- 仅读 Writer 产物 + PLAN (不读 Writer 的 prompt)
- 输出 verdict: PASS / CONDITIONAL_PASS (列出需补的改动) / FAIL
- 严重度: BLOCKING / HIGH / MEDIUM / LOW / COSMETIC

**报告归档**: `dev/evidence/stage_<N>_review.md` 或 `<X>_reviewer.md`

---

## Lane 3: 主控独立抽样 (规则 A 核心)

**职责**: 业务语义抽检. **reviewer PASS 不能免掉这一刀** (v1 G1 教训).

**规则 A 触发**: 本批压缩率 >50% 或改写率 >50%.

**方法**:

1. 从 Writer 产物中**随机**抽 N 个样本 (e.g. 10 个变量 / 10 个 codelist / 10 个 chapter section)
2. 主控**直接读源文件**对照 (不看 Writer 产物的 "我做到了什么" 声明)
3. 每样本判 "业务 PASS / 业务 FAIL" (有信息丢失 / 语义错位算 FAIL)
4. 结果写 `dev/evidence/stage_<N>_audit.md`:

```markdown
# Stage <N> 主控独立抽样 (Rule A)

- 采样方法: ...
- N: 10
- PASS: 8/10
- FAIL: 2/10
  - 样本 1: <变量名>, 丢失 <信息>
  - 样本 2: <codelist>, Synonyms 位置错位
- 业务判定: PASS_WITH_ISSUES / FAIL
- 后续: 要求 Writer 重试 <哪些点>
```

**与 Reviewer 的区分**:
- Reviewer 看**结构**: 格式对不对, 段数对不对, md5 稳定
- 主控看**语义**: 信息有没有丢, 业务含义对不对

**两者必须独立**: reviewer 报告不应影响主控抽样, 反之亦然.

---

## 规则 A 抽样规格

| 批规模 | Reviewer N | 主控 N | 重叠 |
|-------|-----------|-------|------|
| 小 (<50 条目) | 5 | 3 | 允许部分重叠 |
| 中 (50-200) | 10 | 5 | 不重叠 |
| 大 (>200) | 15 | 10 | 不重叠 |

"disjoint" = reviewer 选的样本和主控选的样本**不重叠**, 保证覆盖面.

---

## A/B 回归矩阵

### 矩阵设计 (Phase 2 设计, 批次中执行)

本次 A/B 的测试题 = **原基线题** (T1-T<k>) + **新批新增题** (T<k+1>-T<N>).

| # | 题目 | 期望答案特征 | 批次 | PASS 标准 |
|---|------|-------------|------|----------|
| T1 | (基线, e.g. 变量定义精确查询) | 引变量名 + Core 属性 + 章节号 | baseline | 每批都 PASS |
| T2 | (基线, e.g. 规则推导) | 引 ch04 章节号 + 多方案 | baseline | 每批都 PASS |
| ... | ... | ... | ... | ... |
| T<k+1> | (新批, e.g. 本批覆盖的某 codelist) | 完整 Term 表 | vB.1 | vB.1 起 PASS |
| T<N> | (边界题, 测模型是否坦诚) | "未收录"声明 + 源指引 | 任一批 | 零臆造 |

### 矩阵规格

| Tier | 矩阵大小 | 基线 T | 新批 T |
|------|---------|-------|-------|
| Tier 1 | 3-5 题 | 2-3 | 1-2 |
| Tier 2 | 10-15 题 | 5-8 | 5-7 |
| Tier 3 | 20+ 题 | 8-10 | 10+ |

### 每批跑什么

**错误**: 只跑本批新增题 (会漏掉跨批 regression).

**正确**: 每批跑**完整矩阵** (基线 + 历史新增 + 本批新增).

### 跨批正向 / 负向激活观察

每题的答案**质量对比 vs 上一批**:
- ↑ 质变 (拒答→PASS, 推测→命中)
- ↑ 轻微 (多一个章节引用 / 多一个例子)
- 持平
- ↓ 轻微 (少一个引用)
- ↓ 衰减 (PASS→拒答)

累积到 `dev/test_results.md` 和 `rag_decay_curve.md` (如建立).

---

## 衰减响应 (规则 P10)

| 衰减强度 | 响应 |
|---------|------|
| 0 衰减 | 继续推进 |
| 1 题 ↓ | 记 regression evidence, reviewer 归因, 问用户 continue/hold |
| ≥2 题 ↓ | **立即停**, reviewer 必归因, 用户决策 continue/rollback |

**归因必回答**:
1. 是 RAG 衰减 (容量超了) 还是覆盖缺口 (源没收录)?
2. 是本批产物 bug 还是上一批就有 (被本批暴露)?
3. 下一批能否自然修复? 还是必须 rollback?

**v2.1 T3 案例** (供参考): v1 PASS → v2.1 ↓ (拒答). 归因 = 覆盖缺口 (§6.3.5.9.3 narrative 没展开), 非 RAG 衰减. 决策 = continue, 等下批补. 结果 = v2.3 跨批正向激活 PASS.

---

## 终态整合审查 (Phase G)

所有批次完成后, 做一次**整合**:

- [ ] 跑完整 A/B 矩阵 (T1-T<N>)
- [ ] 对比所有批次的质量演进表
- [ ] 独立 reviewer 复核 (规则 D)
- [ ] 写 `ab_reports/STAGE_FINAL_AB_REPORT.md`

**审查报告必答**:

1. 矩阵 PASS 比? (e.g. 24/24)
2. 跨批 regression 题? (应为 0)
3. 边界题是否零臆造?
4. 有没有 reviewer PASS + 主控 FAIL 的未解冲突?

---

## RETROSPECTIVE 的独立审阅

RETROSPECTIVE.md 草稿由主控写, **必须**由独立 reviewer (不同 subagent_type) 复核:

- reviewer 检查 "保留/补上/决策复盘" 三段完备
- reviewer 检查规则 A/B/C/D/E 是否全都对照执行
- reviewer 输出 verdict, 归档 `dev/evidence/<H-task>_reviewer.md`

本次 Claude v2 的 H1 reviewer 报告是范例 (`claude_projects/dev/evidence/H1_reviewer.md`).

---

## 反例 (应避免)

| 反例 | 问题 |
|------|------|
| executor 和 reviewer 用同一 subagent_type | 违反规则 D, 自审无效 |
| Writer 看了 reviewer 的历史报告才写新产物 | 违反 P6, 污染上下文 |
| 主控只看 reviewer 的 PASS verdict, 不自己抽样 | v1 G1 教训 (技术 PASS ≠ 业务 PASS) |
| 只跑本批新增题 | 漏跨批 regression, P10 失效 |
| Reviewer 归因前急着 continue | 衰减原因没搞清就推进, 问题会累积 |
| RETROSPECTIVE 主控自审 | 违反规则 D |

---

*来源: claude_projects v1 Step 6 技术 PASS 被业务 FAIL 事故 + v2 Phase 3 三 lane 实操 + H1 reviewer 范例.*
