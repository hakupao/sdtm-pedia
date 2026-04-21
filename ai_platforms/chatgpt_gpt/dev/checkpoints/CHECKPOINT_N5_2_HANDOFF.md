# Phase 4 Node 5.2 — ChatGPT 用户操作 Handoff

> **Node**: Phase 4 N5.2 (smoke v2.1 重新上传 + 回归)
> **前置 commit**: `1cff7fe` (Phase 4 N5.1 前置修复 PASS)
> **执行者**: 用户 + claude cowork MCP 代理 (Chrome JS paste + DOM 回读)
> **估时**: 更新 system_prompt ~3 min + 验证 ~3 min + smoke 10 题 ~20-30 min
> **下游 gate**: 回报 smoke v2.1 score → 主 session 派 N5.2 reviewer 第 18 种 subagent_type + 决策进 N5.3

---

## Step 1: 更新 Custom Instructions (GPT Builder)

1. 登录 https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert (Bojiang Zhang Plus 账号)
2. "Edit GPT" → Instructions 框**整段清空**, 粘贴 `ai_platforms/chatgpt_gpt/current/system_prompt.md` **全文**
3. 核查: 右下角字符数显示应 ~5681 chars (ChatGPT UI 按 chars 计, 不按 bytes; 本地文件 7568 bytes 是 UTF-8 编码后含中文的字节长度). GPT Builder 硬上限 8000 chars, 当前 buffer 29.0%.
4. 保存 (右上 "Save" → "Update")

## Step 2: Knowledge 文件 (**不变**)

- ChatGPT 9 文件 knowledge 全部**保持 N4 batch 2 上传的版本**, N5.1 仅改 system_prompt + 脚本 + 文档, 没动 uploads/ 字节
- 无需重传任何文件

## Step 3: 验证 Step 1 生效

在新对话框问 3 题:

### Q_verify_1: "CMINDC 用于哪种场景?"
- **期望**: 显式命名 CMINDC (concomitant medication indication) 变量名, 解释用途 (治疗适应症), 提源路径 (CM/spec.md 或 terminology)
- **反例 (FAIL 若如此答)**: 仅说"指示原因"不提 CMINDC 变量名

### Q_verify_2: "MH+CM 同步进行中的治疗怎么记录?"
- **期望**: 显式 CMINDC (原因) + CMENRTPT/CMENDY (持续/结束) + MHENRTPT (持续指示), 对应 CO-2 MED fix
- **反例**: 只叙业务逻辑不命名变量

### Q_verify_3: "AESER 的 Core 属性是 Req 还是 Exp?"
- **期望**: Exp (Expected), 引 AE/spec.md L254 或 §AESER
- **反例 (回归)**: Req (LLM 邻变量污染幻觉)

3 题全 PASS → Step 1 生效, 进 Step 4

## Step 4: 跑 SMOKE_QUESTIONS_V2.md v2.1 (10 题)

- 打开 `ai_platforms/SMOKE_QUESTIONS_V2.md` (v2.1, Q3 判据 2026-04-21 修正版)
- 按题号顺序问 10 题, 每题开新对话 (避 context 污染)
- 推荐方式: claude cowork MCP 代理 Chrome JS `ClipboardEvent('paste')` 绕 type 丢字 (参考 Node 3b/4 经验)
- 严格按 v2.1 判据评分 (特别 Q3 改用 HIGH/LOW/NORMAL 判据)

## Step 5: 落档

保存到: `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_1_results.md`

结构 (沿用 smoke_v2_results.md 格式):
```markdown
# ChatGPT GPTs — smoke v2.1 10 题回归结果

> Date: <date>
> SMOKE_QUESTIONS_V2.md v2.1 (Q3 判据 HIGH/LOW/NORMAL 修正版)
> 前置 commit: 1cff7fe (Phase 4 N5.1 前置修复 PASS)
> 执行者: user + claude cowork MCP Chrome JS paste
> 预期 score: 10/10 strict (Q3 按 v2.1 判据 + CMINDC bullet N5.1 fix 后 Q7 严判)

## 逐题结果

### Q1: CM 域多条 concomitant medication 怎么合并
- 对话 URL: ...
- 完整回答路径: dev/evidence/smoke_v2_1_answers/Q1_answer.md
- 判据对齐: ...
- Verdict: PASS / FAIL / PARTIAL
- 归因: ...

### Q2-Q10: 类似

## 总结
- strict score: X/10
- 与 v2.0 (9/10) 对比: Q3 是否转 PASS? 其他题是否保持 PASS?
- CO-2 CMINDC bullet 是否在 Q7 引发显式命名?
```

另存每题完整回答到 `dev/evidence/smoke_v2_1_answers/Q{N}_answer.md` (10 个文件)

## Step 6: 回报主 session

回报格式:
```
ChatGPT smoke v2.1 完成: X/10 strict PASS
- Q3: PASS (v2.0 FAIL 已回归) / FAIL (仍错)
- Q7: CMINDC 是否显式命名 PASS / borderline
- 其他: ...
```

主 session 接手后: 派 N5.2 reviewer (第 18 种 subagent_type, 建议 `pr-review-toolkit:type-design-analyzer` 或 `oh-my-claudecode:qa-tester`) 独立审 + 进 N5.3 Full A/B 矩阵 (扩 3-5 新题由主 session 拟草稿用户 review).

---

## 若 smoke v2.1 未达预期 (<10/10 strict)

- **Q3 仍 FAIL**: 核 system_prompt v2.1 是否粘贴完整 + 是否生效 (GPT Builder 有时需 refresh). 若确实生效仍 FAIL, Rule B 归档 `failures/stage_n5_2_attempt_<N>.md`, 折衷 9/10 过阈可进 Phase 4 Gate
- **Q7 CMINDC 不显式**: 核 system_prompt 新 bullet 是否在合理语境段 (工作流 / 边界处理), 重验证 Q_verify_1
- **其他回归 (v2.0 PASS 的题现 FAIL)**: 不正常, 主 session 起 debug session 核 system_prompt 是否误删关键段

## 相关路径

- SMOKE 题目: `ai_platforms/SMOKE_QUESTIONS_V2.md` (v2.1)
- 前轮 smoke (v2.0): `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_results.md` (9/10)
- 前轮 reviewer: `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_reviewer.md` (tracer 第 14 种 subagent_type)
- N5.1 writer 产物: `ai_platforms/chatgpt_gpt/dev/evidence/node5_1_chatgpt_writer_summary.md`
- N5.1 reviewer 产物: `ai_platforms/chatgpt_gpt/dev/evidence/phase4_n5_1_reviewer.md`
- Phase 4 总 plan: `ai_platforms/PHASE4_PLAN.md` (§3 N5.2 行, §4 P1 消化)
