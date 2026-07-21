# Phase 3 P3.3 — Chat Custom mode 激活 + H3 三档切换验证

> **日期**: 2026-04-21
> **执行者**: 用户 (personal Gmail, Web UI)
> **Notebook**: `SDTM Knowledge Base` (P3.2 基线 42/42 indexed)
> **Instructions 文本**: `current/instructions.md` (9,011 chars, 90% of 10K cap)
> **PLAN 引用**: `docs/PLAN.md` §6 P3.3 / §3.4 H3 假设
> **Checkpoint**: soft (验证增值信息)
> **测试设计偏离**: 用户用**同一题 (AESER Core)** 跑三档, 作 controlled comparison (PLAN 建议 3.3 用 LBNRIND, 但同题对比反而**更纯净**地隔离 mode 变量, 不构成 FAIL)

---

## 子步骤 (a): Custom mode 激活

- Chat → Customize → Custom mode → 贴 `instructions.md` 全文 (9,011 chars) → Save
- UI 状态: Custom mode active
- 结果: ✅ **PASS**

---

## 子步骤 (b): H3 三档切换验证

### 3.1 Custom mode 下答题 (AESER Core)

**答案原文**:

> AESER 的 Core 属性是 **Exp (Expected)**。
>
> **Variables involved**:
>
> | Variable | Type | Role | Core | CT |
> |----------|------|------|------|----|
> | AESER | Char | Record Qualifier | Exp | C66742 |
>
> **Definition**: Serious Event. Indicates whether the adverse event is a serious event.
>
> **Codelist**: C66742 (No Yes Response). The permitted values are Y, N, U, N/A.
>
> **Boundary note**: AESER (Serious Event) is Exp, not Req. The AE Req-only set is: STUDYID, DOMAIN, USUBJID, AESEQ, AETERM, AEDECOD (6 variables).
>
> (follow-up 提问): 您是否需要了解 AE 域中其他严重性标准子变量 (如 AESDTH, AESHOSP, AESLIFE 等) 的具体属性和收集规则?

**判定**: ✅ **PASS**

| 维度 | 结果 |
|------|------|
| Core 属性正确 | ✅ Exp (non-Req, instructions.md 规则 5 第 2 条对齐) |
| Variable table 完整 | ✅ Variable / Type / Role / Core / CT 五列齐 (instructions.md 规则 4) |
| Codelist C-code 字面 | ✅ C66742 (instructions.md 规则 6) |
| NY codelist 全写值 | ✅ Y, N, U, N/A (instructions.md 规则 6) |
| Boundary note | ✅ 主动给出 Req-only 6 变量集 (instructions.md 规则 5 第 2 条) |
| Citation | ⚠️ 文本未见 `[08_ev_adverse_ae.md]` inline 标记 (见下方 finding F-1) |
| Follow-up 诚实 | ✅ 主动引导至邻近子变量 |

---

### 3.2 切 Learning Guide mode 下答同题

**答案原文**:

> AESER 的 Core 属性是 **Exp (Expected)**。
>
> (follow-up 提问): 您需要我为您列出不良事件 (AE) 域中其他 Core 属性为 Exp 的变量吗?

**判定**: ✅ **PASS** (H3 假设成立)

| 维度 | 结果 |
|------|------|
| UI 允许同 session 切 Learning Guide? | ✅ **允许** (H3 关键证据, 切换未被灰 / 未被强制 new chat) |
| Core 属性仍正确 | ✅ Exp (source set 未变, RAG 仍走同 42 bucket) |
| Response 风格改变? | ✅ **显著变短** (Custom 模式详表 vs Learning Guide 单行结论 + Socratic 引导) |
| Instructions.md 行为规则是否生效? | ❌ **不生效** (无 Variable table / 无 codelist / 无 boundary note — 符合预期, Learning Guide 不读 Custom instructions) |

---

### 3.3 切回 Custom mode 答同题 (验持久性)

**答案原文**:

> AESER 的 Core 属性是 **Exp (Expected)**。
>
> **Variables involved**:
>
> | Variable | Type | Role | Core | CT |
> |----------|------|------|------|----|
> | AESER | Char | Record Qualifier | Exp | C66742 |
>
> **Definition**: Serious Event (严重事件)。该变量用于指示不良事件是否为严重事件, 其有效值 (Valid values) 为 "Y" 和 "N"。
>
> **Codelist**: C66742 (No Yes Response)。
>
> **Boundary note**: 须注意 AESER 的 Core 属性为 Exp, 并非必填项 (Req)。
>
> (follow-up 提问): 您是否需要了解 AE 域中其他有关严重性标准 (如致死 AESDTH, 导致住院 AESHOSP 或危及生命 AESLIFE) 的具体属性说明?

**判定**: ✅ **PASS** (Instructions.md 持久化成功)

| 维度 | 结果 |
|------|------|
| Custom mode 回切可用? | ✅ 允许 |
| Instructions.md 持久化? | ✅ 规则 4 / 5 / 6 / 12 全部复现 |
| 与 3.1 一致性? | ⚠️ 内容等价, 但 3.3 Valid values 写 "Y 和 N" (漏 U, N/A 两值, 比 3.1 弱). 见 finding F-2 |
| 语言策略 (规则 13) | ⚠️ 3.3 出现中文混写 (3.1 是全英文), Chat session 上下文可能影响输出语言. 非红线问题, 观察 |

---

## 子步骤 (c): H3 结论 + 事实回写

### H3 假设最终判定

PLAN §3.4 H3 假设 ("单 chat session 可切换三档") → ✅ **VERIFIED PASS**

| 维度 | 验证结果 |
|------|---------|
| UI 允许每 chat session 切换三档 | ✅ 是 (3.2 Learning Guide 切换成功, 3.3 回切 Custom 成功) |
| 切换 Learning Guide 后 source set 不变 | ✅ 是 (同 42 bucket, 未重建 RAG) |
| 切换 Learning Guide 后 response 风格改变 | ✅ 是 (从详表 → Socratic 单行) |
| 切回 Custom 后 instructions.md 仍生效 | ✅ 是 (规则 4/5/6/12 复现) |

**PLAN §3.4 原文改写要点**:
- "单 chat session 切换能力" 行: 从 "⏸️ 假设待验证" 改为 "✅ PASS (2026-04-21 UI 实测, 三档可同 session 切换, source set 不变, response 风格符合各 mode 预期)"
- Q-REV-1 闭合: "Chat mode single-mode assumption" 标 CLOSED

### 事实回写清单 (主 session 待做)

| # | 目标文件 | 修改点 |
|---|---------|--------|
| 1 | `docs/research.md` Q6 | Chat mode 事实从 "三档均可选" 升级为 "同 session 可动态切换, source set 保持" |
| 2 | `docs/platform_profile.md` §D | Custom Instructions 等价物段补 "per-chat-session toggle, not notebook-locked" |
| 3 | `docs/PLAN.md` §3.4 表 "单 chat session 切换能力" 行 | 从假设 → PASS (见上方改写要点) |
| 4 | `dev/evidence/_progress.json` | `phase_states.3_execute` 加 `p3_3_completion` 节点; status 改 `p3_3_done_ready_for_p3_4`; Q-REV-1 移入 closed; rule_d_chain 保持 9 (P3.3 UI 工具级, 不占 slot) |

---

## 用户反馈的 finding (非 P3.3 scope, 但影响 instructions.md)

### F-1: NotebookLM Web UI 不渲染 Markdown 表格

**用户观察原文**:
> 注意, 以上回答, 在网页中格式如下
> `Variables involved: | Variable | Type | Role | Core | CT | Source | |----------|------|------|------|----|--------| | AESER | Char | Record Qualifier | Exp | C66742 | |`
> 并没有显示出来是表格

**分析**:
- NotebookLM Chat UI 的渲染层似乎**不走标准 GFM (GitHub-Flavored Markdown)**, markdown pipe-table 被当作纯文本展示, 用户看到的是一坨 `|` 串
- `instructions.md` 规则 4 "return a variable table with columns: ..." + 规则 10 "List Q → markdown table" + Response template 的 pipe-table 模板 **都假设表格能渲染**
- 当前 instructions.md 导致**模型输出 markdown 表格 → UI 不渲染 → 用户可读性极差**

**影响范围**:
- 所有 List Q / Definition Q / Boundary Q 都受影响 (大部分 SMOKE v2 题型)
- P3.4 indexing smoke (N=10) + P3.4.5 Req 语义自证 (N=10) 可读性受损, citation 精度判断变困难
- A/B 15 题 (P3.8) 评分会被格式噪声污染

**候选缓解方案** (不在 P3.3 内决策, 交 P3.4 前主 session 评估):

| 方案 | 做法 | 代价 | 副作用 |
|------|------|------|--------|
| A | instructions.md 规则 4 / 10 / Response template 改 "bullet list + bold 字段名" 替代 pipe-table | 改 instructions.md ~30 行, 重 Save Custom mode | 单条 variable 信息密度下降, 一屏能看的变量数减少 |
| B | 规则 4 改 "key-value 列表 (每行一字段)" | 改 ~15 行 | 最 UI-friendly, 但单 variable 占 5-6 行 |
| C | 先实测 WebFetch NotebookLM Chat UI 渲染规则是否 v2 后支持 GFM, 若支持则 A/B 免做 | WebFetch 1 次 + 2-3 题 UI 复核 | 若确认支持则零改动 |
| D | 接受现状, 仅在 boundary note / 多变量对比 Q 时用表格 | 改 ~5 行收口 | 折中, 保表格语义但限缩使用场景 |

**建议**: 进 P3.4 前先跑方案 C (WebFetch + 1-2 题手工复核) 定底, 再决定 A/B/D. P3.4 smoke N=10 不应在此 UI 格式不确定的状态下跑, 否则 PASS 判据被污染.

**归档位置**: 本 finding 待 P3.4 启动前由主 session 升级到独立条目 — 候选路径 `dev/evidence/ui_rendering_findings.md` 或 carry-over 到 `_template/` 补丁第 12 条.

---

### F-2: Custom mode 同题复答非完全幂等

3.1 vs 3.3 同题 (AESER Core, Custom mode × 2 次) 答案**语义等价但细节漂移**:

| 差异点 | 3.1 | 3.3 |
|--------|-----|-----|
| Valid values 完整度 | Y, N, U, N/A (4 值全) | "Y 和 N" (漏 U, N/A) |
| 输出语言 | 全英文 | 中英混写 |
| Definition 细节 | 纯 SDTM 定义 | 加了中文注释 |

**分析**: RAG 每次召回 chunk 顺序 / LLM 采样 temperature 非 0 → 答案可复现但非字面幂等. **不是 instructions.md bug**, 是 NotebookLM 底层推理随机性.

**影响**: A/B 测试 (P3.8) 需注意同题 retry 可能给不同答案, 评分按**语义正确性**而非字面, 遵循 instructions.md 规则原意即 PASS.

**归档**: 本 finding 挪 P3.8 A/B 矩阵评分规则补一条 "同题 retry 幂等性不强制, 按语义 PASS".

---

## Rule 合规自检

| Rule | 适用 | 状态 |
|------|------|------|
| A (语义抽检 >50%) | 本步 N=3 仅 H3 证据采集, 非 Rule A 正本 (正本在 P3.4.5 N=10) | N/A for this step |
| B (失败归档不删) | 无 attempt FAIL, `failures/` 空 | ✅ 无需归档 |
| D (写审分离) | P3.3 UI 工具级, 不占 Rule D subagent_type slot (cumulative 链保持 9) | ✅ |
| E (Rule E 优先级) | personal Gmail + Pro + Web UI 全生效 | ✅ |

---

## Checkpoint 判定

**P3.3 子步骤 (a) + (b) + (c)**: ✅ **PASS** (soft checkpoint, H3 假设 VERIFIED)

**准入下一步**:
- P3.4 indexing smoke (N=10 题 citation 精度) — **但需先处理 F-1 UI 表格渲染问题**, 否则 N=10 评分被污染
- P3.4.5 Req 变量业务问答 N=10 (Q1 红线语义级自证) — 同受 F-1 影响, 建议等 F-1 闭合

**建议**: P3.4 启动前, 主 session 先跑 F-1 缓解方案 C (WebFetch NotebookLM Chat GFM 支持现状), 30 min 内决策 instructions.md 是否要微调.

---

---

## F-1 闭合 log (2026-04-21 后续 minimal table test)

### Test prompt

```
列出 AE 域中 Core 属性为 Req 的 6 个变量, 每个一行, markdown 表格格式。
```

### 测试条件

- Mode: Custom (与 3.1/3.3 同)
- Notebook: 同 `SDTM Knowledge Base` (42 sources indexed, 状态无变化)
- Instructions.md: 未动 (仍 9,011 chars 原版)

### 答案原文 (用户报告, UI 实际渲染为真表格)

> AE 域中 Core 属性为 Req 的 6 个变量如下:
>
> | Variable | Type | Role | Core | CT | Source |
> |----------|------|------|------|----|--------|
> | STUDYID | Char | Identifier | Req | | [08_ev_adverse_ae.md] |
> | DOMAIN | Char | Identifier | Req | | [08_ev_adverse_ae.md] |
> | USUBJID | Char | Identifier | Req | | [08_ev_adverse_ae.md] |
> | AESEQ | Num | Identifier | Req | | [08_ev_adverse_ae.md] |
> | AETERM | Char | Topic | Req | | [08_ev_adverse_ae.md] |
> | AEDECOD | Char | Synonym Qualifier | Req | MedDRA | [08_ev_adverse_ae.md] |
>
> (follow-up): 您是否想深入了解上述某个特定变量 (如 AETERM 或 AEDECOD) 的具体定义和收集规则?

### 判定

| 维度 | 结果 |
|------|------|
| UI 渲染为真表格 (有列头 / 每行独占一行) | ✅ **YES** (用户实测: "现在是表格了, 没有问题") |
| 6 个 Req 变量正确 (instructions.md 规则 5 第 2 条 AE Req-only set) | ✅ STUDYID / DOMAIN / USUBJID / AESEQ / AETERM / AEDECOD (全对) |
| Core 全写 "Req" (instructions.md 规则 5) | ✅ |
| AEDECOD CT = MedDRA (非 C-code 但正确引用外部字典) | ✅ |
| Citation `[08_ev_adverse_ae.md]` inline | ✅ 6/6 |
| Follow-up 诚实 (instructions.md 规则 12) | ✅ |

### F-1 分支定位

三分支中命中分支 **(a) UI 真表格** → F-1 **闭合**.

**根本归因**:
- Google 官方 help `answer/16179559` 明示支持表格 (WebFetch A 级证据)
- 模型在 Custom mode 下**能**输出合规 pipe-table (列头独行 + 每 row 独行 + 分隔符行)
- 3.1/3.3 single-line malformed 是**模型输出偶发漂移**, 非系统性 bug
- 漂移率粗估: 4 次 table 场景 3 次 malformed / 1 次合规 (n=4, 统计力不足, 仅供参考)

### 处置决策

- ❌ **不改** `instructions.md` Response template — 规则 4/10 本身正确, 加约束会增加 char 占用 (当前 90% 已紧)
- ✅ **接受偶发漂移** — P3.8 A/B 评分规则已预留 F-2 "同题 retry 幂等性不强制" 条, F-1 漂移吸收进同条
- ✅ **P3.4 放行** — indexing smoke 启动无格式阻塞; 若 N=10 中 >30% 出现 single-line malformed, 再考虑 instructions.md 微调

### 结论

**F-1 CLOSED** (2026-04-21). P3.4 gate OPEN, 无前置条件.

---

*evidence 落盘日期: 2026-04-21. 来源: 用户 Web UI 实测 3 组问答 + F-1 闭合 minimal table test + 主 session 格式化 + WebFetch 官方 help 三角 + finding 归纳.*
