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

### 规则 A 压缩率 × N 阈值矩阵 (补丁 17, 2026-04-24 via NotebookLM async lane)

上表按批规模定 N, 对于**压缩率触发** Rule A 的情况 (源 → 产物 压缩率 >50%) 另有 N 阈值矩阵:

| 压缩率 | N 建议 | 理由 |
|--------|--------|------|
| 50-70% | N ≥ 3 | 结构级 ∅ gap + 3 样本独立抽检足够 catch 粗粒度错 |
| 70-85% | N ≥ 5 (50%) | 压缩越高 risk 越大, 5 样本覆盖关键维度 |
| ≥ 85% | N ≥ 7 或全覆盖 | NotebookLM 86% 压缩实际只抽 3/10 (30%) 在边缘被 reviewer flag |

**N 必须写进 PLAN §Task** (非事后补登, `ai_platforms/_template/04_plan.md` §Task 定义时 explicit 列).

### Rule A 合规 vs meta-evidence trace 的 category 差异 (补丁 17, 重要警示)

多 retro 实践中出现 "meta-evidence trace 当 Rule A" 的类别错误 — retro trace 前序产物 (如 ∅ gap audit / 语义级审) 作 evidence base, 这是**合规** evidence 引用, **但不等于** Rule A 严格意义的 "N 独立样本抽检 (N 写进 PLAN, 独立抽**新**样本审)".

**两者 category 差异**:
- **trace 前序产物**: 证明 "已有 evidence 闭合"
- **N 独立抽检**: 证明 "新样本再打一次也稳"

**正交互补, 不能互替**. Retro 若仅列 trace 不说 "N 独立抽检未做", 容易在 reviewer category error 上被抓 (跨 4 retro 28th reviewer F3 + NotebookLM 独立 reviewer 重抓).

**写进 retro §Rule A 章节模板**:
> "本 retro 的 Rule A trace 是 **meta-evidence trace** (trace 前序产物作 evidence base), 非 Rule A 原文严格意义 "N 独立样本抽检". 严格 N≥X 独立抽检 [已做 / 挪 post-project optional]."

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

### T2 题型 citation dropout 豁免 (补丁 19, 2026-04-24 via NotebookLM async lane)

**现象**: source-grounded 架构平台 (NotebookLM 典型) 在 **T2 题型** (业务场景 / 举例类 / "某药物场景下 X 变量怎么填") 上 citation 数明显低于 **T1 题型** (事实查询类 / "X 变量的 Core 属性是什么").

**数据** (NotebookLM 实测):
- P3.4.5 语义级 N=10: 语义 10/10 顶阈值 + citation 7/10 (偏低)
- P3.8 smoke v3 Q1-Q10: T1 题 citation 均 ≥ 10 / T2 题 citation 3-5

**根因**: 业务场景 T2 题的 "source 支撑" 是 **spread across multiple bucket** 的 inference, 不是单一引文可覆盖; 模型倾向"答语义正确但省 inline cite".

**评分规则** (本范本采用): 业务场景/举例类 T2 题若答**语义正确**但 citation 数 **< T1 题均值**, **不扣分** (系统性现象非单题失误). 在 retro §缺口 登记作平台系统性弱点 (如 NotebookLM G-NBL-5 / F-3).

**非** 修复路径 (作 ICEBOX 备用):
- 调 System Prompt / Custom mode 加"业务例后强制 cite source"规则 (未实测效果)
- 报告给平台提 feature request (超项目 scope)

### A/B 维度按 anti-hallucination 机制分类 (补丁 18, 2026-04-24 via NotebookLM async lane)

设计 A/B 矩阵时, **按 platform_profile §G.1 选择的 anti-hallucination 机制** (架构级 / Prompt 级 / 混合) 分类, 不同机制的 AHP 阈值与归因不同:

| 机制 | AHP × 3 预期 | 阈值 | 失败归因 |
|------|-------------|------|----------|
| 架构级 in-KB-only | 3/3 PASS+ 最强 | ≥ 67% (2/3) 硬 gate | 如 FAIL 归因 "架构 bypass" (极罕见) |
| Prompt 级 anchor | 依赖锚设计 | ≥ 67% (2/3) 硬 gate | FAIL 归因 "锚缺 / 锚模糊" (如 Gemini R1 → R2 CO-5 修复) |
| 混合 | 预期 PASS 偏高 | ≥ 67% (2/3) 硬 gate | FAIL 时区分 "web 没补上 vs 锚失效" |

**重要**: AHP PASS **不等于** anti-hallucination 能力强, 需归因区分:
- NotebookLM 3/3 PASS+ 最强 = 架构优势 (天然)
- Claude 3/3 PASS+ = 训练深度 + 锚 (混合, 部分题靠 web)
- ChatGPT PARTIAL = 锚执行不严
- Gemini R2 3/3 = 锚精修后 (R1 0/3 → R2 3/3 因果闭环)

跨平台对比 AHP 结果时不要混为一谈 (源 NotebookLM R-NBL-6 + cross-4 platform AHP 矩阵).

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
