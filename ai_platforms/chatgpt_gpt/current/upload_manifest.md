# ChatGPT GPTs — Upload Manifest (Phase 3 Node 3)

> 状态: **Ready to Upload (批 1 P0)**
> 最后更新: 2026-04-20
> 实测 tokens 来源: `dev/evidence/_progress.json` `phases.3_execute.nodes.N2_scripts_run.product_stats` (去 `~` 前缀, 规则 P3)
> 总计: 批 1 = 4 文件 / 4/20 文件硬限 / 16 spare (批 2 预计再占 5-6, 仍远 ≤ 20)

> **Note**: 本 manifest 替代了 Node 2 脚本自动追加的旧骨架 (原仅含 token + 段数列). Node 3a 新增 cap/buffer/备注/上传步骤/carry-over 段. 未来 `merge_for_chatgpt.py --stage batch2` 如再追加, 应以 "## Auto-appended batch2" 二级节追加, 不覆盖本 header 区.

---

## 上传顺序

按 score 降序 (PLAN §3.2 v1.1 打分): **01 > 02 > 03 > 04** (01/02=3.4, 03/04=3.2). 上传后**必须**等 File Search indexing 完成 (UI 显示 "Processing..." → "Ready") 再开始 smoke. Q8 Indexing indicator 可靠性待 Phase 3b 实测 (见下 carry-over).

## 文件清单

| # | 文件 | tokens (实测) | cap | buffer | sources | 主要内容 | 备注 |
|---|------|---:|---:|---:|---:|---------|------|
| 01 | `01_navigation.md` | 46,170 | 47,000 | 1.77% | 3 | ROUTING + INDEX + VARIABLE_INDEX | **LOW-F1**: buffer 仅 1.77%, Node 4 批 2 合并后重评估 cap (建议升 48-50K 预防未来 KB 膨胀, 不改变本批可上传性) |
| 02 | `02_chapters_all.md` | 60,607 | 72,000 | 15.82% | 6 | SDTMIG 6 章节 (ch01/02/03/04/08/10) | PASS 常态 |
| 03 | `03_model_all.md` | 17,653 | 21,000 | 15.94% | 6 | SDTM v2.0 Model (concepts / observation_classes / datasets / relationships / associated_persons / etc.) | PASS 常态 |
| 04 | `04_domain_specs_all.md` | 185,704 | 193,000 | 3.78% | 63 | 63 域 spec.md (Rule E Q5=A 全量平权) | buffer 3.78% 可接受 |

**合计**: 310,134 tokens (批 1 RAG 检索池, 非一次性注入).

---

## Phase 1 carry-over 清单 (Phase 3b 实测收集)

- **MEDIUM (Instructions 8K 精度)**: Phase 3b 上传时实测 GPT Builder UI 是否拒收 7,500 字符 (`system_prompt.md` 当前 4,782 chars, buffer 36.2%); 若 UI 上限是 tokens (4x 宽松), 后续可扩 Instructions; 当前保守预算, 不阻塞. 归档: `dev/evidence/phase3_instructions_budget_reality.md` (待建).
- **PARTIAL (Q8 Indexing indicator)**: Phase 3b 上传后立即跑 smoke 题 S5 (参见 `smoke_questions_draft.md`), 验证 UI "Ready" 状态 = 实际可检索. 归档: `dev/evidence/phase3_q8_indexing_reality.md` (待建).

## Node 2 → Node 3 carry-over

- **LOW-F1** (已在 01 行备注): cap buffer 1.77% 偏紧, 但 attempt_2 PASS, 不阻塞本批上传. Node 4 前决定是否升 48-50K.
- **LOW-F2** (PLAN §2.4 Step 6 估算): 本 manifest 已按 P3 去 `~` 落实测数字 ✅; PLAN §2.4 Step 6 文字回写 (`~15K/30K/30K/150K` → 实测) 留**本 session 主 session** 修 (文档回写, 非本 manifest 产物).

---

## 上传操作步骤 (用户侧, Phase 3b 执行)

1. 访问 `chat.openai.com` → 左侧 **"Explore GPTs"** → 右上 **"+ Create"**
2. 进入 **Configure** tab (不是 Create tab 的聊天问答模式)
3. **Name**: `SDTM Expert` (或任意含 "SDTM" 前缀的名称)
4. **Description**: `CDISC SDTMIG v3.4 + SDTM v2.0 Expert - Variable definitions, rule reasoning, controlled terminology, cross-domain linking` (约 130 字符)
5. **Instructions**: 粘贴 `current/system_prompt.md` 全文 (≤ 7,500 chars, 当前 4,782 chars)
6. **Conversation starters**: 填入 4 条 (从 `system_prompt.md` 末尾 "Conversation Starters" 段复制)
7. **Knowledge**: 上传 4 个文件 from `current/uploads/` — **顺序 01 → 02 → 03 → 04** (score 降序)
8. **Capabilities**: 关闭 "Web Search" / 关闭 "Code Interpreter" / 关闭 "DALL-E Image Gen" (本 GPT 纯知识问答, 启用反而增加 hallucinate 面)
9. 等待每个文件 "Processing..." → "Ready" (预计每个 1-3 分钟)
10. 点 **Preview** → 按 `dev/evidence/smoke_questions_draft.md` 跑 5 题 smoke
11. 回报 smoke 结果到本 session 或新 session (Phase 3b), 结果入 `dev/evidence/smoke_batch1_results.md`

---

## 发布决策 (本 Node 不必决, Phase F5 再决)

本 Node **不**决定是否 GPT Store 公开. 默认 **Only me** (Private); Phase F5 Task F5 用户 ack 后再改 "Anyone with a link" 或 "GPT Store" 发布 (Rule E Q1=C 预设但可否决).

---

## 合规核验

- P3 AI 估算 `~` 前缀规则: ✅ 本 manifest 所有 tokens 数字为实测, 无 `~` 前缀
- P11 文件数 ≤ 20: ✅ 批 1 = 4 文件, 16 spare
- P12 源溯源: ✅ 每文件内含 `<!-- source: knowledge_base/... -->` 标记 (批 1 4 文件合计 78 source 段)
- P13 TableAware: ✅ Node 2 attempt_2 validate_batch1.md 28/28 check PASS
- Rule E Q1=C / Q2=C / Q5=A: ✅ Instructions 已乘入 (见 `system_prompt.md` 路由表 + 陌生公开受众段 + 63 域全量平权段)

---

*来源: PLAN v1.2 §2.4 + §3.2 + §5.1 + `_progress.json` N2_scripts_run.product_stats + phase3_node2_attempt2_ab_reviewer.md*
| 05 | 05_domain_assumptions_all.md | 54,658 tokens | 63 sources | batch2 |
| 06 | 06_domain_examples_all.md | 220,575 tokens | 63 sources | batch2 |
| 07 | 07_terminology_core_high_freq.md | 200,746 tokens | 15 sources | batch2 |
| 08 | 08_terminology_quest_and_supp.md | 1,047,119 tokens | 49 sources | batch2 |
| 09 | 09_terminology_core_mid_tail.md | 698,081 tokens | 27 sources | batch2 |
