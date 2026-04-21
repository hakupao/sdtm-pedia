# ChatGPT GPTs — Phase 3 Node 4 HANDOFF (用户上传 + smoke v2 rerun)

> **生成时间**: 2026-04-21
> **状态**: Node 4 batch 2 执行 + Rule D reviewer PASS 完成, 等用户上传 + smoke v2 10 题 rerun
> **前置 PASS**: writer (executor opus) + reviewer (superpowers:code-reviewer 第 12 种 subagent_type, Verdict PASS 92%)

---

## Step 0. 先读清单 (3 分钟)

| # | 文件 | 看什么 |
|---|------|--------|
| 1 | `ai_platforms/chatgpt_gpt/dev/evidence/node4_writer_summary.md` | writer 完整产出 (脚本 + system_prompt + 5 新文件 tokens) |
| 2 | `ai_platforms/chatgpt_gpt/dev/evidence/phase3_node4_reviewer.md` | reviewer PASS 92% + 2 LOW carry-over |
| 3 | `ai_platforms/SMOKE_QUESTIONS_V2.md` | 10 题业务维度, 两平台共享 |

---

## Step 1. 上传 5 个新 batch 2 文件 到现有 GPT

**已有 GPT**: [SDTM Expert](https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert) (Plus 账号)

### 1.1 更新 Instructions (system_prompt v2)

- 打开 GPT Builder → Configure → Instructions
- 全文替换为 `ai_platforms/chatgpt_gpt/current/system_prompt.md` (7,220 chars / 7,500 budget / buffer 3.73%)
- Conversation Starters 4 个保留 (如 Builder 表单独立, 填现有 4 个)

### 1.2 Knowledge Files — 保留 batch 1 的 4 个 + 加 5 新

**batch 1 (已上, 不动)**:
- 01_navigation.md / 02_chapters_all.md / 03_model_all.md / 04_domain_specs_all.md

**batch 2 (新加 5 个, 按以下顺序)**:

| 顺序 | 文件 | tokens | 大小 | 备注 |
|:----:|------|-------:|-----:|------|
| 1 | `ai_platforms/chatgpt_gpt/current/uploads/05_domain_assumptions_all.md` | 54,658 | 244 KB | 63 域 assumptions |
| 2 | `ai_platforms/chatgpt_gpt/current/uploads/06_domain_examples_all.md` | 220,575 | 664 KB | 63 域 examples |
| 3 | `ai_platforms/chatgpt_gpt/current/uploads/07_terminology_core_high_freq.md` | 200,746 | 805 KB | 15 高频 core |
| 4 | `ai_platforms/chatgpt_gpt/current/uploads/08_terminology_quest_and_supp.md` | 1,047,119 | 4.1 MB | 43 quest + 6 supp |
| 5 | `ai_platforms/chatgpt_gpt/current/uploads/09_terminology_core_mid_tail.md` | 698,081 | 2.6 MB | 27 低频 core |

**合计 batch 2**: 2,221,179 tokens / 5 文件
**合计 batch 1+2**: 2,531,313 tokens / 9 文件 (20 硬限剩 11 槽位)

### 1.3 上传步骤

1. Knowledge Files 面板 → Upload files → 选 5 个 (顺序不影响 RAG)
2. 等每个文件 "Processing → Ready" 状态 (08 文件 4.1MB 可能等 2-5 分钟)
3. 若某文件卡 Processing >10 分钟 → 删重传 (File Search 偶发重建失败)
4. 9 个文件全 Ready 后, Save GPT

### 1.4 保存 + 验证

- Save + 等 "Update successful"
- 进 Preview (右侧 Chat), 问 "你的 knowledge base 有几个文件?" — 应答 9 个
- 问 "AE.AESER 的 Core 是什么?" — 应答 Exp (从新上的 04 / 05 retrieved)

---

## Step 2. Smoke v2 10 题 rerun

### 2.1 题目来源

`ai_platforms/SMOKE_QUESTIONS_V2.md` 10 题:
- I 场景应用 (Q1-Q3): CM 合并用药拆记录 / AE SAE / LB HbA1c
- II 规则判断 (Q4-Q6): AESEV vs CTCAE / PK LLOQ / ARM vs ARMCD
- III EDC→SDTM 映射 (Q7-Q8): MH 病史+CM / ISO 8601 + Study Day
- IV 域间鉴别 (Q9-Q10): SUPPAE 边界 / RELREC vs SUPP

### 2.2 执行

**方式 A (推荐)**: 用户在 [SDTM Expert GPT](https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert) Preview 里手跑 10 题, 每题答案 copy 到本地.

**方式 B**: claude-in-chrome MCP agent 在 chatgpt.com/c/新建 conversation 里跑, 自动 copy 答案.

### 2.3 结果落档

- 落盘: `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_results.md`
- 格式: 每题 1 段, 含题号 / 原题复制 / ChatGPT 答案 / PASS-FAIL-PARTIAL 判据对比 / 核心事实命中情况

### 2.4 Exit criteria

- **≥ 8/10 PASS** → N4 smoke 跨 gate, 可 commit C4 + 进 Node 5 full A/B
- **7/10 PASS** → CONDITIONAL_PASS, 列 carry-over 到 Node 5 修, 也可 commit C4
- **≤ 6/10 PASS** → FAIL_REWORK, 回头看 system_prompt / batch 2 route / 上传顺序

---

## Step 3. 回报格式

结束 smoke 后, 回报一条 message 含:

```
Smoke v2 结果 (ChatGPT):
- 分数: X/10 PASS
- 每题 verdict: Q1=PASS / Q2=PASS / ... / Q10=FAIL
- 问题 (若 FAIL): ...
- 下一步建议: [进 Node 5 / 补数据 / rework system_prompt / ...]
```

主 session 会起 Rule D 第 14 种 subagent_type 独立审 smoke 答题质量 + 写 reviewer evidence + 更新 SYNC_BOARD N4 → PASS.

---

## Carry-over 当前 session 未消 (信息)

### Node 4 新增 LOW (Node 5 前处理)
- **L1**: `validate_chatgpt_stage.py` 行 519 硬编码 `(v1.1)` → 改 `(v1.5)`.
- **L2**: legacy helper `_collect_terminology(subdir)` 标 DEPRECATED 或删.

### Node 2 继承
- 01 cap 47K buffer 1.77% (LOW-F1): 若 smoke 里 01 路由题命中率 <80%, 升 cap 重合并.

### Phase 1 Q8 Indexing indicator
- Node 3b smoke v1 已闭合 (S1+S5 Ready 状态命中), 本 Node 4 延续, 无新操作.

### Rule A N=5 HIGH_FREQ_CORE_HINTS 业务合理性
- 主 session 可选 `evidence/step_node4_audit.md` 追 HIGH_FREQ 选择依据. 非 blocker.

---

## 遇到问题的 escalation 路径

1. **上传卡 Processing**: 删重传, 不影响数据
2. **smoke 1-2 题 FAIL 但其他 PASS**: 先记录, Node 5 full A/B 再看模式
3. **≥ 3 题 FAIL**: 停下看 system_prompt, 可能 batch 2 路由规则需要细化
4. **GPT 答 "knowledge base 有 9 文件" 时错数**: File Search indexing 中, 等 5 分钟再问

---

**准备完毕**. 用户上传完 + 跑完 smoke v2 + 回报, 主 session 起 reviewer subagent 审 + 更新 SYNC_BOARD + commit C4.
