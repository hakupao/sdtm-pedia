# Gemini Gems — Phase 3 Node 4 HANDOFF (用户删老上传新 + smoke v2 rerun)

> **生成时间**: 2026-04-21
> **状态**: Node 4 C 方案执行 + Rule D reviewer CONDITIONAL_PASS 完成, 等用户替换 Gem knowledge + smoke v2 10 题 rerun
> **前置 PASS**: writer (executor opus) + reviewer (oh-my-claudecode:architect 第 13 种 subagent_type, Verdict CONDITIONAL_PASS 88%)

---

## Step 0. 先读清单 (5 分钟)

| # | 文件 | 看什么 |
|---|------|--------|
| 1 | `ai_platforms/gemini_gems/dev/evidence/node4_writer_summary.md` | writer 完整产出 (C 架构 4 文件 + 04 业务弹药 + CO-1/2/3 landing) |
| 2 | `ai_platforms/gemini_gems/dev/evidence/phase3_node4_reviewer.md` | reviewer CONDITIONAL_PASS 88% + SDTM 事实 10/10 + 2 MEDIUM / 3 LOW carry-over |
| 3 | `ai_platforms/gemini_gems/docs/PLAN_V2_C.md` | C 方案原设计 (终止前版本参考) |
| 4 | `ai_platforms/SMOKE_QUESTIONS_V2.md` | 10 题业务维度, 两平台共享 |

---

## Step 1. 替换 Gem knowledge (核心: 删老 4 + 上新 4)

**已有 Gem**: [SDTM Expert (Custom Gem)](https://gemini.google.com/u/1/gem/3b572e310813/d053fd5f9418b93c) (Google AI Pro)

**架构变更** (重要): Node 3b v1 的 4 文件 → 舍弃 terminology 换业务弹药包

| v1 (要删) | v2 C (要上) | 变化 |
|----------|-------------|------|
| 01_core_reference.md | 01_navigation_and_quick_reference.md | 改名 + 功能扩 (导航速查强化) |
| 02_domain_specs.md | 02_domains_spec_and_assumptions.md | 改名 + **spec 和 assumptions 域内交错** |
| 03_domain_knowledge.md | 03_domains_examples.md | 改名 + **只留 63 域 examples** (assumptions 已移 02) |
| 04_terminology_core.md | 04_business_scenarios_and_cross_domain.md | **完全新** 业务弹药包 (30K tokens, 舍弃 terminology) |

### 1.1 更新 Custom Instructions (system_prompt v3)

- 打开 Gem → Configure → Custom Instructions
- 全文替换为 `ai_platforms/gemini_gems/current/system_prompt.md` (6,720 chars / 8,000 budget / buffer 16%)
- 关键改动说明:
  - **CO-1 AE 边界锚点**: "AE 域多数 Core=Req, 但 AESER Core=Exp, 逐变量精确引用不邻变量模式推断"
  - **CO-2 NCI 零臆造**: "具体 Term 查 NCI EVS Browser, 不在 04 §3 索引表里的 Code 一律给外链"
  - **CO-3 citation 强制**: 每答必附 "源路径: `knowledge_base/...`" 段
  - **战略转向**: 舍弃 terminology inline, 换业务场景完整覆盖

### 1.2 Knowledge — 删 4 老 + 上 4 新 (顺序 very important)

**动作步骤**:

**A. 删老 4**:
1. Gem Knowledge 面板 → 逐个点 `01_core_reference.md` → Remove
2. 同样删 `02_domain_specs.md` / `03_domain_knowledge.md` / `04_terminology_core.md`
3. 确认 Knowledge 空

**B. 上新 4 (严格按此顺序 — 首尾 recency bias 对 Gemini 关键)**:

| 顺序 | 文件 | tokens | 位置策略 |
|:----:|------|-------:|----------|
| 1 | `ai_platforms/gemini_gems/current/uploads/01_navigation_and_quick_reference.md` | 124,515 | 前置 (导航防 Lost-in-Middle) |
| 2 | `ai_platforms/gemini_gems/current/uploads/02_domains_spec_and_assumptions.md` | 240,453 | 前中段 (域 spec + 规则同屏) |
| 3 | `ai_platforms/gemini_gems/current/uploads/03_domains_examples.md` | 220,657 | 中段 (域 examples) |
| 4 | `ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md` | 30,488 | **末尾** (业务弹药包 + recency bias) |

**合计**: 616,113 tokens / 61.6% 占用 1M 窗口 / 384K buffer 响应余量

### 1.3 保存 + 验证

- Save
- 进 Gem 对话 problem:
  - Q: "AE 域里 AESER 的 Core 属性是什么?"
  - 期望答: **Core=Exp (Expected)**. 若答 Req → CO-1 落地失败, 跑 smoke 前查 system_prompt / 04 §1.2 §2.1 是否真的上对了
  - Q: "你的 knowledge 里有哪些文件?"
  - 期望答: 4 个 (01/02/03/04 新名字)

---

## Step 2. Smoke v2 10 题 rerun

### 2.1 题目

`ai_platforms/SMOKE_QUESTIONS_V2.md` 10 题 (和 ChatGPT 完全一致, 便于跨平台对比):
- I 场景应用 Q1-Q3: CM 合并用药 / AE SAE / LB HbA1c
- II 规则判断 Q4-Q6: AESEV vs CTCAE / PK LLOQ / ARM vs ARMCD
- III 映射 Q7-Q8: MH + CM / ISO 8601 + Study Day
- IV 鉴别 Q9-Q10: SUPPAE 边界 / RELREC vs SUPP

### 2.2 执行

**方式 A (推荐)**: 用户在 [Gem Preview](https://gemini.google.com/u/1/gem/3b572e310813/d053fd5f9418b93c) 手跑 10 题.

**方式 B**: claude-in-chrome MCP agent 在 gemini.google.com 里跑.

### 2.3 结果落档

- 落盘: `ai_platforms/gemini_gems/dev/evidence/smoke_v2_results.md`
- 格式: 每题 1 段, 题号 / 原题 / Gemini 答案 / PASS-FAIL-PARTIAL / 核心事实命中

### 2.4 Exit criteria

- **≥ 8/10 PASS** → N4 smoke 跨 gate, 可 commit C4 + 进 Node 5 full A/B
- **7/10 PASS** → CONDITIONAL_PASS, 列 carry-over 到 Node 5
- **≤ 6/10 PASS** → FAIL_REWORK, Reviewer 的 MED-1 就 firing: 需扩 04 15-25K 重传 + rerun

---

## Step 3. 回报格式

```
Smoke v2 结果 (Gemini):
- 分数: X/10 PASS
- 每题 verdict: Q1=PASS / Q2=PASS / ... / Q10=FAIL
- CO-1 验证 (AESER Core): 答对 / 答错 / 未触
- CO-2 验证 (NCI Code 零臆造): ...
- CO-3 验证 (源路径引用): 答题都带 / 偶有 / 全无
- 问题 (若 FAIL): ...
- 下一步建议: ...
```

---

## Carry-over (Reviewer 标 MEDIUM/LOW, 交 Node 5)

### MEDIUM (Node 5 前或 smoke 后必修)

**CARRY-N5-1 (from MED-1)**: 04 扩 15-25K tokens 到 50-60K target
- **Reviewer 建议**: smoke 前预防性扩, 免 2 轮
- **若 smoke ≥ 8/10 PASS**: 延到 Node 5 A/B 后决定
- **若 smoke < 8/10**: 必扩 (case likely: "场景/鉴别"题命中不足)
- 优先域: RECIST / 影像 / Oncology / Trial Design (TS/TI/TM) / IE / AG / PR

**CARRY-N5-2 (from MED-2)**: V8 pattern v2.1 收紧 (技术债)
- 当前 attempt_2 用"列表格式绕过"pattern false-positive, 非修根
- Node 5 或 Node 6 改 `validate_gemini.py` V8 pattern 只 FAIL 真 Term Submission Value

### LOW (文档/精度)

**CARRY-N5-3**: writer summary 统计口径 (AESER 9 处 vs 独立 Grep 分布) 不透明, 未来统一"硬锚点段"vs"散落提及"两档.

**CARRY-N5-4**: 04 内部 §1.26 / §2.1 / §8 信息 redundancy ~10%, 去重释 3-4K tokens.

**CARRY-N5-5**: §1.15-§1.26 子域段统一加 "Core: 域内 Req 集 / 典型 Exp 集" 摘要.

### INFO

**CARRY-N5-6**: 02 实测 240K 比 PLAN 370K 低 130K, buffer 释放去向 Node 5 前决定 (扩 04 / 扩 01 / 留给响应).

---

## 遇到问题的 escalation 路径

1. **上传卡**: Gemini 1M 窗口上传秒级 (无 RAG indexing), 若卡超过 1 分钟 → 删重传
2. **AESER 答 Req**: CO-1 落地失败. 查 system_prompt 是否真的上了新版; 查 04 §1.2 AESER 段; 若都 OK 但 Gemini 仍答 Req → CO-1 需要更多 reinforcement, smoke 后扩 04 §1.2 段
3. **zero 源路径引用**: CO-3 格式强制不够硬, 需要 system_prompt 加"若不给源路径视为不合规"
4. **NCI Code 臆造**: CO-2 guard 不够, smoke 后加更多 example pattern
5. **smoke ≥ 3 题 FAIL**: reviewer 预判 — 04 覆盖面不够. 直接执行 CARRY-N5-1 扩容

---

## 架构关键决策 (提醒)

- **战略舍弃 terminology**: 基于 1M context 物理限制 + Gemini 非 RAG + 用户 2026-04-21 决策. Gemini 不再能回答"某 codelist 的所有 Term 值"这类字典查询, 统一指向 NCI EVS Browser.
- **业务场景弹药换 terminology**: 10 题 smoke v2 全是业务问法, 04 直接对 smoke 设计弹药. ROI 比 inline terminology 高一个数量级 (Reviewer 评估).
- **384K buffer 保守**: 总 616K 占用, 留 38%. Reviewer 认为过度保守, 建议下一轮挤出 100K 给 04/01 更深覆盖.

---

**准备完毕**. 用户删老上新 + 跑完 smoke v2 + 回报, 主 session 起 reviewer subagent 审 smoke + 更新 SYNC_BOARD + commit C4.
