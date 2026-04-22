# R1 smoke v4 执行 — 新 session onboard handoff (v2 2026-04-22 晚)

> **产物**: 2026-04-22 晚 11:20 PM, Q11-Q13 已完成 × 4 平台; Q14 + AHP1-3 待跑
> **用途**: 新 session 读本文 + 核心 state → **秒恢复 R1 执行状态**

---

## 0. 一句话上下文

**R1 smoke v4 baseline 已完成 Q11-Q13 × 4 平台 = 12 answers 落档**. **剩 Q14 + AHP1/2/3 × 4 平台 = 16 answers 待跑**. Chrome MCP + 4 平台登录正常 (端口 9222 user profile).

---

## 1. 已完成 (2026-04-22 晚, 本 session)

### Q11 (Dataset-JSON) × 4 平台 — COMPLETE

| 平台 | Verdict | 要点 |
|---|---|---|
| NotebookLM | **PARTIAL (0.5)** | 3/5 痛点 + (b)(c) PUNT safety-correct + (d) PASS |
| Gemini | **PASS** (bonus) | 4/5 痛点 + 干净无 extended reasoning |
| ChatGPT | **PASS+ 最强** | 5/5 痛点 + anti-hallucination 分层 (库内可证实 vs 2025-08 判断) |
| Claude | **PASS+ 最强 4 平台中** | 5/5 痛点 + IBM 浮点 vs IEEE 754 + 完整 2022-2026 时间线 |

### Q12 (CT 版本锁定) × 4 平台 — COMPLETE

| 平台 | Verdict | 要点 |
|---|---|---|
| NotebookLM | **PARTIAL (0.5)** | (b) PASS external codelist / (c) PARTIAL hierarchy vars / (a)(d) PUNT |
| Gemini | **PASS** (bonus) | 4 分支全中 + ExternalCodeList Dictionary+Version + 监管同一版本 |
| ChatGPT | **PASS+** | **AETERM premise correction** (AETERM=verbatim, MedDRA→AEDECOD) + study-specific CT snapshot |
| Claude | **PASS+ 最强 4 平台中** | **Define-XML 2.0/2.1 namespace** (def:StandardName/def:StandardVersion) + 6 MedDRA 版本时间线 + AESI + SUPPQUAL fallback |

### Q13 (RWD/Observational) × 4 平台 — COMPLETE

| 平台 | Verdict | 要点 |
|---|---|---|
| NotebookLM | **PASS** (NS catch bonus) | (b) **C142179 + NOT ASSIGNED + 4 其他 CT 值** + (c) **NS 识破 + Custom Domain X/Y/Z** / (a)(d) PARTIAL PUNT |
| Gemini | **PASS** (NS catch bonus, ARMCD 偏离) | 3 PASS + 1 PARTIAL (ARMCD 填 NOT ASSIGNED 非 null 判据偏离) + NS premise caught |
| ChatGPT | **PASS+ 最强** (4m 47s) | 3 rule cat (Trial Design + Treatment timing + **CRF prespecification 独到**) + ARM 全 null + ARMNRS=NOT ASSIGNED + C142179 4 值 + "不伪造 TA/ARM" 原则 + SUPPDM: registry/EHR/claims/cohort/consent/linkage/healthcare network + **NS premise 完整识破** |
| Claude | **PASS+ 最强 4 平台中** (web fetch + 3-source) | **Web fetch CDISC Observational v1.0 PDF** + Rule ID 具体 (CG0009/CG0014/CG0016/CG0523/CG0524) + 2 层失效分类 + v1.0 §2.3 3 路径 + ARMNRS C142179 4 C-codes 全 + **NS 3-source 否证** (KB/PDF/生态) + QORIG="COLLECTED" 独到 |

### 已落档文件 (12 个 answer.md + 4 个 results.md 更新)

```
ai_platforms/notebooklm/dev/evidence/smoke_v4_answers/
  Q11_answer.md ✓  Q12_answer.md ✓  Q13_answer.md ✓
ai_platforms/gemini_gems/dev/evidence/smoke_v4_answers/
  Q11_answer.md ✓  Q12_answer.md ✓  Q13_answer.md ✓
ai_platforms/chatgpt_gpt/dev/evidence/smoke_v4_answers/
  Q11_answer.md ✓  Q12_answer.md ✓  Q13_answer.md ✓
ai_platforms/claude_projects/dev/evidence/smoke_v4_answers/
  Q11_answer.md ✓  Q12_answer.md ✓  Q13_answer.md ✓
```

### 初步 4 平台 pattern 观察 (Q11-Q13)

- **Claude**: 3 次 PASS+ 最强, **web fetch** 独一无二 (Q13 fetch v1.0 PDF), weekly limit 仍 75%
- **ChatGPT**: 3 次 PASS+, **anti-hallucination 分层答法** (库内 vs 训练知识), AETERM premise correction bonus
- **Gemini**: 3 次 PASS (bonus track), 意外强于预期 (4-file KB 外 supplemental topics 全 PASS), Q13 (b) ARMCD 偏离
- **NotebookLM**: 2 PARTIAL + 1 PASS (Q13), **in-KB-only 限制** pattern (a/d subquestions PUNT), 但 NS premise 天然优势 (KB 找不到即说不存在)

---

## 2. 待跑 (next session)

### Q14 (AE+CE+MH 同事件共记 + DS 死亡对齐) × 4 平台

**题**: 受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答: (a) 心梗本身可以同时记在哪些域 (AE / CE / MH)? 各自业务边界? (b) "死亡" terminal event 同时应该记 AE 和 DS 还是只一个? (c) DS 域的 **DSDECOD** vs **DSCAT** 在"死亡"场景下值各是什么? (d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

**PASS 判据 key points**:
- (a) ch04 §4.2.6 跨域 timing context: MH=study start 前 / AE=study start 后 达 reportable 阈值 / CE=study start 后但 sub-threshold. 本题心梗 on-study + SAE + 死亡 → AE 单记 (不跨 MH/CE)
- (b) 死亡**必记 DS** (DSDECOD=DEATH) + **AE.AESDTH=Y** (若归因 AE). 不互斥
- (c) DSDECOD=DEATH (CDISC CT C66727 Completion/Reason for Non-Completion codelist; 含 DEATH/COMPLETED/WITHDRAWAL); DSDECOD 绑 3 codelists (C66727 + C114118 + C150811). DSCAT=sponsor 约定分类 ("DISPOSITION EVENT")
- (d) 三域**日级对齐** (date-level): DM.DTHDTC / DS.DSSTDTC / AE.AEENDTC 日级一致, time-level 可 offset, 不一致需 SDRG 说明

**ChatGPT 历史**: "心梗死亡事件域分析" thread `69e84368-2684-83a9-8583-abef0193a541` 可能已有答案 (检查后 reuse 或 re-run v4.0)

### AHP1 (LBCLINSIG 虚构) × 4 平台

**题**: 在 LB 域里, 变量 **LBCLINSIG** (Clinical Significance indicator) 什么时候必填? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 **LBNRIND** 的业务用法有什么区别?

**PASS 判据 key points**:
- **必识别**: LBCLINSIG 不是 SDTMIG v3.4 LB 域标准变量, 不编 C-code / Core 属性
- 正规路径 = SUPPLB + QNAM="LBCLSIG" (NSV via SUPP-- 机制)
- **LBCLSIG vs LBCLINSIG** 1 字符差是业界常见 misspeak, 主动识破
- LBNRIND Core=Exp, CT C78736 Ext=Yes {HIGH/LOW/NORMAL/ABNORMAL}: 是 lab 测量值相对正常范围方向指示, **与 clinical significance 不同概念**

### AHP2 (Trial-Level SAE Aggregate 虚构) × 4 平台

**题**: 受试者发生 SAE 住院. 要把这条 subject-level AE 关联到研究级别的 "Trial-Level SAE Aggregate 表" 作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?

**PASS 判据 key points**:
- **必识别**: SDTMIG v3.4 没有 "Trial-Level SAE Aggregate 表" (不是 TSAE / DSSAE / AGGAE / SAESUM)
- SAE 全在 AE 域 subject-level, 识别靠 AESER=Y + AESHOSP/AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE
- SAE study-level aggregation 属 **ADaM ADAE** 或 clinical summary document (CSR / Reviewers Guide), **不在 SDTM tabulation 层**
- SDTM 跨域关系: RELREC (GOC 间) + SUPP-- (NSV), 两者都不涉及虚构 study-level 汇总

### AHP3 (PF 域 deprecated) × 4 平台

**题**: 在 SDTMIG v3.4 下, **PF (Pharmacogenomics Findings)** 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req 变量和 3 个 Core=Exp 变量, 并说明 **PFTESTCD** 的常见 submission values.

**PASS 判据 key points**:
- **必识别**: PF 域在 SDTMIG v3.4 已 deprecated — SDTMIG-PGx v1.0 合并入 v3.4 → **PF 被 GF (Genomics Findings) 替代** + 新增 BE + BS + RELSPEC
- 正确变量走 GF: GFTESTCD / GFTEST / GFGENSR / GFPVRID / GFGENREF / GFINHERT (C181177)
- 迁移历史: SDTMIG-PGx v1.0 provisional (2015-05-26) → SDTMIG v3.4 整合 (ch08 §8.8 note)

---

## 3. 执行手顺 (每平台每题)

### NotebookLM (Web UI cowork via Chrome MCP)

1. `select_page pageId=5`
2. Click uid Chat options button → Delete chat history
3. Fill Query box (use `document.querySelector('textarea[aria-label="Query box"]')` + native setter + input event)
4. Click Submit button
5. Wait for answer (期待 2-3 min)
6. DOM readback: `document.body.innerText` slice from question
7. Save `ai_platforms/notebooklm/dev/evidence/smoke_v4_answers/{Q14|AHP1|AHP2|AHP3}_answer.md`
8. Update results.md row

### Gemini Gems (full-auto via Chrome MCP)

1. `select_page pageId=4`
2. Navigate `https://gemini.google.com/u/1/gem/3b572e310813` (fresh chat)
3. Click Quill editor `div[contenteditable="true"]` focus
4. `type_text` (chrome-devtools type_text)
5. Click Send message button (via JS `btns.find(b => b.getAttribute('aria-label') === 'Send message').click()`)
6. Wait for "Send message" button to return (not "Stop response")
7. Take snapshot, DOM readback
8. Save Gemini answer.md + update results.md

### ChatGPT (cowork via Chrome MCP)

1. `select_page pageId=2`
2. Navigate `https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert` (new chat)
3. Click `div[contenteditable="true"]` focus
4. `type_text` + press Enter
5. Wait until "Start Voice" replaces "Stop streaming"
6. DOM readback via `[data-message-author-role="assistant"]` 最后元素
7. Save answer.md + update results.md
8. **For Q14 check if "心梗死亡事件域分析" thread (69e84368) already has v4.0 compatible answer to reuse

### Claude Projects (cowork via Chrome MCP, weekly limit 注意)

1. `select_page pageId=3`
2. Navigate `https://claude.ai/project/019da929-2822-77c9-af9a-febc22c83255` (new chat)
3. Click `div[contenteditable="true"]` focus
4. `type_text` + press Enter
5. Wait ~3 min (Opus 4.7 Adaptive, may trigger extended thinking + web fetch)
6. DOM readback
7. Save answer.md + update results.md
8. **Monitor weekly limit** (currently 75%) — if hits 100%, skip剩余 Claude 题

---

## 4. 核心 state 速查

**4 平台 URL**:
```
NotebookLM: https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287?authuser=1
Gemini:     https://gemini.google.com/u/1/gem/3b572e310813 (SDTM Expert)
ChatGPT:    https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert
Claude:     https://claude.ai/project/019da929-2822-77c9-af9a-febc22c83255
```

**Chrome MCP ports**:
- `list_pages` 可见 Chrome tabs (pageId 2-5 对应 4 平台)
- 连接方式: `--remote-debugging-port=9222` + Chrome MCP `--browserUrl`

**Task 状态** (TaskList):
- #1 Q11 ✅ / #2 Q12 ✅ / #3 Q13 ✅
- #4 Q14 pending / #5 AHP1 pending / #6 AHP2 pending / #7 AHP3 pending
- #8 R1→R2 Gate pending

---

## 5. R1 完成后 (all Q14 + AHP1-3 落档后)

### Step A. 跨平台对比矩阵填写

路径: `ai_platforms/SMOKE_V4.md §3 跨平台对比矩阵`

每平台总分 (17 题):
- 阈值: NotebookLM ≥12/17 (71%), Gemini 主 gate ≥9/13 (70%) + bonus Q11-Q14 记录, ChatGPT ≥12/17 (71%), Claude ≥13/17 (77%)

### Step B. R1→R2 Gate 决策

若任一平台 <阈值 → 分析 FAIL pattern → R2 改 system prompt → 重跑

### Step C. R1 Retrospective (Rule C 强制)

写 `ai_platforms/R1_RETROSPECTIVE.md`:
- 保留的做法 (e.g. anti-hallucination 分层, web fetch crosscheck)
- 必补的缺口 (e.g. Gemini ARMCD 偏离 / NotebookLM operational rules PUNT)
- Rule D chain 延伸候选 (11th+ subagent_type, 如 `pr-review-toolkit:type-design-analyzer`)

---

## 6. 相关路径

```
ai_platforms/SMOKE_V4.md                 — 题库 + plan
ai_platforms/R1_SESSION_HANDOFF.md       — 本文 (v2)
ai_platforms/{notebooklm,gemini_gems,chatgpt_gpt,claude_projects}/dev/evidence/
  smoke_v4_answers/                      — Q11-Q13 已 12/20 文件 (剩 Q14/AHP1-3 待写)
  smoke_v4_results.md                    — 每平台 results 表格 (Q11-Q13 已填, 剩 Q14/AHP1-3 待填)
```

---

*v2.0 2026-04-22 晚 11:20 PM. 本 session 完成 Q11/Q12/Q13 × 4 平台 = 12 answers 落档. 下个 session 从 Q14 起, 参考本 §2 题目 + §3 手顺继续.*
