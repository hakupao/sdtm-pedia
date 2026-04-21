# SDTM Expert Smoke v2 — ChatGPT GPTs

> Run date: 2026-04-21
> Platform: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert
> Account: Plus (Bojiang Zhang)
> Reasoning mode: Extended (default of the GPT)
> Questions source: ai_platforms/SMOKE_QUESTIONS_V2.md v2.0
> Runner: MCP agent (Cowork via Chrome extension), each Q in a fresh conversation
> Submission method: Chrome MCP `javascript_tool` + ProseMirror `ClipboardEvent('paste')` + click `button[data-testid="send-button"]`

---

## ⚠️ 复查 + 纠正记录 (2026-04-21)

### 第一轮失败分析

**根因**: Chrome MCP `type` 动作对中英混合文本会吞掉英数字母/数字段.

**失败实证** (用户纠正前的提交实况):
| Q | 实际发出文本 | 状态 |
|---|---|---|
| Q1 | **无法核验** — 找不到任何对应 `/c/` 对话 URL (早期对话 tab 可能已丢失) | ❌ 作废 |
| Q2 | 仅发出 "3 天治疗..." 开头, 缺"一位受试者服药后出现严重皮疹并因此住院"前段 | ❌ 破损 |
| Q3 | 剪贴板粘贴试水成功, 与原题逐字一致 (tab 1009014472) | ✅ 正文对 |
| Q4-Q7 | **4 题揉在同一 tab 提交** (前 3 题英数码全被吞, 最后一题 Q6 完整), 覆盖 Q3+Q4+Q5+Q6 混答 (tab 1009014481) | ❌ 灾难性破损 |
| Q8-Q10 | 未提交 | ⚪ 空白 |

**用户纠正**: 2026-04-21 "你向gpt提问的q1-q10和规定中的问题完全不一样" — 用户主动指出不一致, 要求立即复查+纠正.

### 第二轮 (当前) 成功方案

**绕过 `type` 丢字**: Chrome MCP `javascript_tool` 在页面内 DOM 层直接 dispatch `ClipboardEvent('paste')` 到 ProseMirror 编辑器 — 完全绕过系统键盘/剪贴板, 不经 `type`. 提交后立刻回读 `[data-message-author-role="user"]` DOM 核验逐字一致.

**已验证**: Q1-Q10 **全部 10 题**提交的 user 消息在 DOM 回读层与原题**逐字一致**; Q1-Q10 答案已抓到并评分 (每题 `dev/evidence/smoke_v2_answers/Qx_answer.md`).

---

## 第二轮全部 10 题 ChatGPT 对话 URL + 收割状态

| Q | Conversation URL | User 消息核验 | 答案状态 | Verdict |
|---|---|:---:|---|:---:|
| Q1 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ee72-28d8-83a7-a63e-c796625e56be | ✅ 逐字对 | ✅ 已收割 | **PASS** |
| Q2 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6eec8-fa68-83aa-abeb-ef0d3d552545 | ✅ 逐字对 | ✅ 已收割 | **PASS** |
| Q3 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef21-ae04-83a8-b5af-8551a6fb9a0a | ✅ JS paste | ✅ 已收割 | **FAIL** |
| Q4 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef02-7ca8-83a4-b352-9e61c631d90c | ✅ JS paste | ✅ 已收割 | **PASS** |
| Q5 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef3a-50dc-83a9-82cb-04556d699bd6 | ✅ JS paste | ✅ 已收割 | **PASS** |
| Q6 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef52-5c14-83aa-a485-4ce9e08bb74c | ✅ JS paste | ✅ 已收割 | **PASS** |
| Q7 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef68-7b88-83a8-8009-ba3f00ae7111 | ✅ JS paste | ✅ 已收割 | **PASS** |
| Q8 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef81-2edc-83a6-b13e-2c1cac11d0e7 | ✅ JS paste | ✅ 已收割 | **PASS** |
| Q9 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef9a-07c4-83a7-b6ea-c6084bc9c48d | ✅ JS paste | ✅ 已收割 | **PASS** |
| Q10 | https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6efb4-cd4c-83a6-b6ae-0dbeb7ed89fb | ✅ JS paste | ✅ 已收割 | **PASS** |

**核验方法**: 每题提交后 `document.querySelectorAll('[data-message-author-role="user"]')` 取 DOM, 对比 `SMOKE_QUESTIONS_V2.md` 原文逐字符一致. 每题 answer 收割通过 `mcp__Claude_in_Chrome__get_page_text` 抓 `<main>` 全文.

---

## PASS/FAIL 汇总

**计分**: **9/10 PASS, 1 FAIL**

| # | 业务维度 | 题目主题 | Verdict | 关键判据命中 | 失误点 |
|---|---|---|:---:|---|---|
| Q1 | 场景→域映射 | CM "高血压 + 头痛" 2 天 → 2 条记录 | PASS | 2 条拆分 + STUDYID/DOMAIN/USUBJID/CMTRT/CMSEQ 全覆盖 | — |
| Q2 | 场景→域映射 | AE SAE 7 子变量 Y/N 判定 | PASS | AESER=Y / AESHOSP=Y / 其 5 个 N; 区分 seriousness vs severity | — |
| Q3 | 场景→域映射 | LB HbA1c 8 变量完整填法 | **FAIL** | 7/8 变量正确; **LBNRIND 填 HIGH/LOW/NORMAL (应为 H/L/N 短码)** | CT codelist 短码错 |
| Q4 | 规则/约束 | AESEV 枚举 + CTCAE Grade 5 → AEOUT=FATAL | PASS | MILD/MODERATE/SEVERE + NCI C66769/C66768 + Grade 5→FATAL | — |
| Q5 | 规则/约束 | PC LLOQ 不能写 0 | PASS | PCORRES=BLQ 或 <0.050 / PCSTRESN=null / PCLLOQ=0.050 / left-censored 概念 | — |
| Q6 | 规则/约束 | ARMCD vs ARM + 中途换组 TA/SE/DM | PASS | ARMCD 短码 20 字符 + TA=设计 / SE=实际 / DM=汇总 + ACTARM/ACTARMCD | — |
| Q7 | 鉴别判断 | MH vs CM 分工 + ONGOING | PASS | 双域 + MHENRTPT/CMENRTPT=ONGOING + Events vs Interventions | CMINDC 变量名未显式命名 (次要) |
| Q8 | 规则/约束 | ISO 8601 精度 + AESTDY 无 Day 0 | PASS | YYYY-MM-DDThh:mm / 只按日期部分算 / 锚点 DM.RFSTDTC | — |
| Q9 | 场景→域映射 | SUPPAE 4 场景 + QNAM/QLABEL/QVAL 例子 | PASS | AESOSP / Other Medically Important SAE / HIGH RISK FOR ADDITIONAL THROMBOSIS | — |
| Q10 | 鉴别判断 | RELREC vs SUPPAE/SUPPCM: AE←CM 因果 | PASS | 选 RELREC + 跨记录 vs 单记录补充分工 + 7 关键字段 | — |

## Q3 FAIL 详情

**题目原文要求** (SMOKE_QUESTIONS_V2.md line 65):
> 按 SDTMIG v3.4 LB 域, 给出: (1) LBTESTCD / LBTEST / LBCAT / LBORRES / LBORRESU / LBSTRESN / LBSTRESU / LBNRIND 各自的填写, (2) **LBNRIND 的 controlled terminology (代码表) 是什么**.

**PASS 判据** (SMOKE_QUESTIONS_V2.md line 69-71):
- LBNRIND 取值 ∈ {H, N, L} (codelist `NORMIND`)
- **LBNRIND = H** (8.4 > ULN 6.5)
- 8 个变量值完整

**ChatGPT 实答** (Q3_answer.md):
- LBTESTCD / LBTEST / LBCAT / LBORRES / LBORRESU / LBSTRESN / LBSTRESU 共 7 个变量全对
- LBNRIND = **HIGH** (应为 **H**)
- 且明确说"LBNRIND 的 controlled terminology: NORMAL / LOW / HIGH"

**失误性质**: **硬性 CT codelist 错误** — SDTMIG NORMIND codelist (NCI C78736) 明确是 `H / N / L` 单字符短码, 非 `HIGH/LOW/NORMAL` 全写. 这是 LB 域最常见的硬规则之一, 答错会导致 SDTM 数据集 validator 直接报错.

**不是"表达不全"问题, 是"用错代码值"问题**.

---

## 退出阈值决策 (按 SMOKE_QUESTIONS_V2.md 退出标准)

**标准**:
- ≥8/10 PASS → 进 Phase 4 (回归)
- 7/10 PASS → CONDITIONAL (补窟窿再复测)
- ≤6/10 PASS → FAIL_REWORK (回 Phase 3 重整 batch)

**本次成绩**: **9/10 PASS** → ✅ **进 Phase 4 (回归)**

唯一 FAIL (Q3 LBNRIND 短码) 是**局部硬规则错**, 不是**系统性检索失败**. 推荐 Phase 4 补救动作:

1. **在 02/03 文件补强 CT codelist 短码硬规则**: 新增"LBNRIND 短码 = H/N/L, 禁 HIGH/LOW/NORMAL"这一行显式规则 — 不依赖检索, 写进系统提示兜底
2. **Phase 4 回归单独复测 Q3**, 确认修复
3. **其他 9 题不复测** (PASS 已证系统在相应业务维度达标)

---

## 详细 Q1-Q10 答案 + Verdict

每题完整答案 + PASS 判据自检 + Verdict 存于:
`ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_answers/Qx_answer.md` (x = 1-10, 10 个文件齐全)

---

## Gemini Gems smoke v2 (后续已完成)

**状态**: **已完成** — 见 `ai_platforms/gemini_gems/dev/evidence/smoke_v2_results.md` (2026-04-21 同日跑完).

**跨平台对比**: ChatGPT 9/10 PASS vs Gemini 8/10 PASS (strict) / 8.5 (PARTIAL=0.5).
- Q3 (LBNRIND H/N/L) 两平台同题 FAIL, 但失败模式结构性不同: ChatGPT 答 "HIGH/LOW/NORMAL" (知识错), Gemini 按 CO-2 拒答 (守则守约).
- Q6 (ARMCD 换组) ChatGPT PASS (含 ACTARM), Gemini PARTIAL (漏 ACTARM, 错层到 ADaM).
- 其他 8 题两平台双 PASS.

---

## 本次 session 主要技术教训

1. **`type` 混合文本坑**: Chrome MCP 的 `type` 动作对"中文+英数"混合文本会丢英数段. **禁用 `type` 发中英混合 prompt**.
2. **可靠方案**: 页面内 JS `DataTransfer + ClipboardEvent('paste')` dispatch 到编辑器 DOM — 绕过所有系统层, ProseMirror/React 内部状态都会正确同步.
3. **验证是必需的**: 每次提交后必须 DOM 回读 `[data-message-author-role="user"]` 核验, 不能只看 `tool output` 的返回字符串 (如 `Q2_SENT` 只代表按钮点击成功, 不代表文本发对).
4. **tab group 重置**: `tabs_close_mcp` 有 race condition, 一次关多个会触发 "session's tab group no longer exists" — 关 tab 后应立刻重新 `tabs_context_mcp`.
5. **收割策略**: `get_page_text` (抓 `<main>`) 优于 `javascript_tool` (后者返回 1500 字符被截断). 每题 navigate → wait 4-5s → get_page_text 一条龙.
6. **Context 预算**: 200+ tool call 级任务需要切到多 session 接力, 或用 subagent.

---

## Session 状态

- ChatGPT GPTs Smoke v2 收割 + 评分 = **完成**
- 决策 = **Phase 4 进行** (9/10 PASS, 1 FAIL 局部可修)
- Phase 4 待办 = 补强 NORMIND codelist 短码硬规则 + 单独复测 Q3
- Gemini Gems 平行 smoke v2 = **未启动** (下 session)
