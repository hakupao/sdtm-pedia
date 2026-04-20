# ChatGPT GPTs Phase 1 Research — Reviewer Verdict

**Verdict**: CONDITIONAL_PASS
**Reviewed by**: oh-my-claudecode:verifier subagent (独立 lane, 规则 D 满足)
**Date**: 2026-04-20
**Subject file**: ai_platforms/chatgpt_gpt/docs/research.md

---

## 覆盖度评估

| 原 J 8 问 + carry-over 2 | research.md 对应 Q# | verdict | 来源数 | 备注 |
|--------------------------|-------------------|---------|--------|------|
| J1: Assistants API vs GPT Builder Knowledge 同一套? | Q1 | ANSWERED | 3 | community.openai.com + developers.openai.com; sunset 声明来源有效 |
| J2: File Search chunk size / overlap 默认值? | Q2 | ANSWERED | 2 | 两条 community.openai.com 确认 800/400 |
| J3: Embeddings 模型 (3-small/3-large)? 可选? | Q3 | ANSWERED | 4 | openai.com 官方 + community; 不可选结论有据 |
| J4: 检索 top-K 默认值? 可调? | Q4 | ANSWERED | 2 | platform.openai.com/docs/assistants + community |
| J5: Plus/Team/Enterprise 三套餐文件数/容量差异? | Q5 | ANSWERED | 4 | community.openai.com + 第三方对比页; 核心结论 "20 文件全套餐相同" 有官方社区来源 |
| J6: GPT Store 审核标准 + 时间? | Q6 | ANSWERED | 5 | help.openai.com + openai.com/policies + 社区时间线讨论 |
| J7: Conversation Starters 上限个数? | Q7 | ANSWERED | 2 | 两条 community.openai.com 确认 4 个显示上限 |
| J8: Indexing indicator 是否可靠? | Q8 | PARTIAL → Phase 3 | 2 | 社区报告显示"显示已上传 ≠ 可检索"; 实际 GPT Builder 操作层实测延至 Phase 3 合理 |
| carry-over B: 总量无官方硬上限来源? | Q9 | CLOSED | 2 | 10GB/user / 100GB/org; help.openai.com/en/articles/8555545 |
| carry-over E: 权限粒度 Team/Enterprise 分级? | Q10 | CLOSED | 3 | help.openai.com Enterprise GPTs 文章 + community |

**覆盖度: 10/10** (9 ANSWERED + 1 PARTIAL-Phase3)

---

## 审查清单结果

- [x] **10 问全覆盖 (J section 8 + carry-over 2), 无遗漏** — Q1-Q10 逐一对应, 全部有答案段落. PASS.

- [x] **每问至少 1 个来源链接** — 所有 10 问均有 2-5 条来源 URL, 格式为 Markdown 链接. 全部 10 问 PASS. (注: Q5 的 docs-to-md.com 是第三方博客, 但同时有 community.openai.com 官方社区来源背书, 不影响结论.)

- [ ] **未标"待 P1 复核"的具体数字必须有来源支持** — **PARTIAL FAIL**: PLAN 修订段落 #2 声称 Instructions 长度限制为 "8,000 字符 (社区多次确认)", 但 research.md 正文中无对应 Q# 的八问八答段落, 无 URL 来源. Profile D 原字段标注的是 "估算 ~8K tokens (待 P1 确认)"; 修订表将其标为已确认, 但来源链接不存在于本文件. 此为 **文档链断裂 — MEDIUM 缺口**, 数字可能正确但在 research.md 内无据可查.

- [x] **"未决问题"段存在, Q8 Indexing 处置合理** — 未决问题段落包含 4 条, Q8 (Indexing 完成确认方法) 列为第 1 项, 明确说明 Phase 3 实测验证方法. 合理. PASS.

- [x] **"对 PLAN 的修订"段至少 5 条 (writer 声称 10 条)** — 实计 10 条: 表格 8 条 + 表格外 "新增修订建议 2 条". 见下节详细去重分析. PASS.

- [x] **"对 profile 的反馈"段关闭 Phase 0 carry-over 3 条** — 三条均有明确状态标注: B=CLOSED, E=CLOSED, C=PARTIAL CLOSE→Phase 3. PASS.

- [x] **无 hallucinate** — 所有具体数字 (800 tokens/400 tokens, top-K=20, 10GB/user, 4 个 Starters, 2-5 工作日) 均有对应来源. 唯一风险点: Instructions 8K 字符 (见上方 PARTIAL FAIL). 其余无编造官方未公开数据. 整体 PASS (1 项文档链不完整, 不是凭空捏造).

- [x] **与 Rule E ack 一致** — Q1=C (混合受众/降门槛): Q7 确认 4 个 Starter 上限与需求完全匹配, PLAN修订 #3 明确引用. Q2=C: PLAN修订 #3 再次确认 "全部 4 个均可使用, 无需妥协". Q5=A (全量覆盖可行性): Q5 确认 20 文件硬限跨套餐一致, PLAN修订 #1/#4/#5 均服务全量部署决策. PASS.

---

## 发现的缺口 / hallucinate 风险

### 缺口 1 (MEDIUM): Instructions 8,000 字符来源链断裂

**位置**: "对 PLAN 的修订"表格 #2 列
**问题**: 原 Profile D 标注 "估算 ~8K tokens (待 P1 确认)". PLAN修订 #2 将其改为 "8,000 字符 (社区多次确认)", 但:
1. research.md 正文中无以此为主题的 Q# 八问八答段落
2. 无来源 URL 支撑该 "字符" 而非 "tokens" 的区分
3. "tokens" 改 "字符" 是实质性精度变化 (8K tokens ≈ 32K 字符; 8K 字符 ≈ 2K tokens — 相差 4 倍)

**风险**: 若 Instructions 实际上限是 8K tokens 而非 8K 字符, PLAN 的系统提示设计基准将偏差 4 倍. 对 Phase 2 PLAN 有实际影响.
**建议 (可 Phase 2 并行修复)**: 在 research.md 补充一段 "Q2-补充: Instructions 字符 vs token 上限" 并附来源 URL, 或在 PLAN.md 中将该数字标注为 "待 Phase 3 实测确认".

---

## PLAN 修订段落质量评估

**10 条逐一验证:**

| # | 来源 Q# | 是否凑数/重复? | 评估 |
|---|---------|-------------|------|
| 1 | Q9 | 否 | 修正 profile B 错误描述, 有实际价值 |
| 2 | (无对应 Q#) | 否, 但来源断裂 | 数字精度变化 (tokens→字符) 无来源; 见缺口1 |
| 3 | Q7 | 否 | 直接对应 Starter 上限确认, 影响 A/B 矩阵设计 |
| 4 | Q2 | 否 | chunk 参数固定不可调, 影响文件合并策略 |
| 5 | Q4 | 否 | top-K=20 影响 A/B 跨 chunk 汇总题设计 |
| 6 | Q1 | 否 | Assistants API sunset 信息, 防止误用 |
| 7 | Q6 | 否 | 2-5 工作日审核, 影响 Phase 5 时间线 |
| 8 | Q10 | 否 | Plus 发布路径确认, 影响分阶段发布策略 |
| 9 | Q2+Q3 新综合 | 否 (有价值) | "格式质量是唯一可控变量"是 Q2/Q3 的正确推论, 提升为 P11 核心约束合理 |
| 10 | Q8 | 否 (有价值) | 实测验证步骤是 Q8 findings 的直接 actionable, 非凑数 |

**去重结论: 10 条全部独立, 无重复.** 修订 #9 和 #10 (超出原 profile 范围的新增) 属于合理 scope 延伸, 非 scope creep — 两条均直接服务 Phase 3 执行质量.

**实际有效条数: 10 条** (1 条来源链不完整需补齐, 但不影响数量计数).

---

## Phase 0 carry-over 关闭状态复核

| 原 carry-over | 原文内容 | writer 声明状态 | reviewer 认同? |
|--------------|---------|----------------|---------------|
| B: 总量无官方硬上限来源 | profile B 描述无来源 URL | **CLOSED** — 10GB/user, 100GB/org; help.openai.com 来源补齐 | **YES** — Q9 有 2 条来源; help.openai.com/en/articles/8555545 是官方文章 |
| E: 权限粒度 Team/Enterprise 分级? | "读/编辑 (owner)" 描述不完整 | **CLOSED** — Plus/Team/Enterprise 三级分明; 编辑仅 owner 确认 | **YES** — Q10 有 3 条来源; help.openai.com Enterprise GPTs 官方文章 |
| C: Indexing indicator 实测 | "推测可靠, 相比 Claude" — 主观假设 | **PARTIAL CLOSE → Phase 3 实测** | **YES (合理)** — 社区报告 (Q8 来源) 已提供文档层证据; 实际 GPT Builder 实测需要平台访问, Phase 3 是正确时机. 不应强求 Phase 1 完成 |

---

## 放行结论

**进 Phase 2: YES, 附 1 项 MEDIUM 条件**

**条件**: Instructions 字符上限 "8,000 字符" 数字在 PLAN.md 中必须标注 "来源待补 — 见 research.md 缺口 1" 或附实际社区来源 URL. Phase 2 PLAN 撰写阶段补齐此来源链, 不阻塞 Phase 2 启动.

**理由**:
- 10/10 问全覆盖, 无遗漏
- 所有问题均有官方或社区来源 (10 问 × ≥2 条)
- 9 项 ANSWERED + 1 项 PARTIAL-Phase3 (Q8 转 Phase 3 处置合理)
- 3 条 Phase 0 carry-over: 2 CLOSED + 1 PARTIAL (合理)
- 10 条 PLAN 修订均独立有价值, 无凑数; 2 条新增 scope 合理
- Rule E 对齐: Q1=C/Q2=C/Q5=A 三项选择均有对应 research 结论支撑
- 无 hallucinate: 所有具体数字有来源 (Instructions 8K 字符除外 — 该数字可能正确但证据链断裂)
- MEDIUM 缺口: Instructions 8K 字符来源断裂 — 数字精度 (字符 vs tokens) 有 4 倍级差异影响, 但可在 Phase 2 PLAN 撰写时并行补足, 不需重跑 Phase 1
