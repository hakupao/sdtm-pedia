# NotebookLM Phase 3 P3.4.5 — Req 变量业务问答抽检 N=10 用户+Claude cowork 手顺

> **Node**: Phase 3 P3.4.5 (Q1 红线**语义级**自证, 规则 A 正本 N=10 Req 业务问答)
> **前置**: P3.4 完成 (42-tile 全扫 42/42 + 10 题 indexing smoke 10/10 PASS, commit `9dce0b0`, 2026-04-21)
> **执行者**: 用户 (Web UI Chat 问答原文) + cowork Claude (题设计 / 主动 prompt log 留档 / 评分) + **独立 subagent_type reviewer (第 10 种 slot)**
> **估时**: ~3 h (主 session 抽题 + 设计 30 min + 用户问答 45 min + evidence 落盘 30 min + **独立 reviewer 复核 45 min** + commit 30 min)
> **Checkpoint 级别**: **HARD** (Q1 红线语义级, 10/10 命中必过; 不过 gate 不进 P3.5/3.6/3.7)
> **下游**: P3.5 (Audio Overview × 3) / P3.6 (Mind Map) / P3.7 (Study Guide × 3)
> **PLAN 引用**: `docs/PLAN.md` §6 P3.4.5 (M1 fix)
> **Evidence 归档**: `dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md` (本手顺末尾模板)

---

## 背景 (≤400 字)

P3.4 完成 indexing smoke 10/10 PASS 后, 主 session 做 P3.4 **事后复核**, 识别 5 条方法论层疏漏:

1. **[最重要] Writer/Reviewer 隔离弱化** — cowork 既代跑 Chrome MCP 题目提交又自评, 规则 D 隔离松.
2. **Citation 判据从 inline text 降级到 DOM panel** — F-1 漂移 0/10 结论是读源面板 bucket ID 得出, 未肉眼核 inline citation 文本, 真实 inline 漂移率**未测**.
3. Checkpoint 手顺未入 git (已于 P3.4.5 启动前补 commit).
4. 大 bucket 38 (302K) "未截断" 用 Q08 单题推广偏强.
5. 题目原文 "未改字" 缺原始 prompt log 佐证.

P3.4.5 必须把这 5 条全部**硬约束化**, 不能沿用 P3.4 的松 precedent. 本手顺的设计就是这些约束的执行化表述.

**P3.4.5 目标**: 把 "176 独立 Req 变量在业务语境下被 NotebookLM RAG **语义级**召回" 作 Q1 红线闭合. 具体三件事:

1. **10 Req 变量随机抽样** (主 session 独立抽, 禁 cowork 预先看).
2. **10 业务问答** (非变量名查字典, 构造 real-world SDTM 场景).
3. **独立 subagent_type reviewer 复核** (第 10 slot, Rule D 链扩展到 10 种).

PASS 阈值 (PLAN §6 原文): **10/10 Req 业务语义命中** AND **≥9/10 citation 精确回指**.

---

## 规则 D 链扩展说明 (关键)

| Phase | 累计 subagent_type 种数 | slot 占用情况 |
|-------|--------------------------|--------------|
| 0-2 (研究+规划) | 9 种 | `general-purpose` / `verifier` / `executor` / `critic` / `planner` / `analyst` / `code-architect` / `code-reviewer` / `architect` |
| 3 (P3.1-P3.4 执行) | 9 种 (不变) | P3.2/P3.3/P3.4 均 UI 工具级 + cowork 评分, 不占 slot |
| **3 (P3.4.5 本步)** | **10 种** | **第 10 slot 必须用于独立 reviewer 复核本步产出** (不是 main session, 不是 cowork 自评) |

**第 10 种 subagent_type 候选** (任选其一, 不能与已用 9 种重复):
- `oh-my-claudecode:security-reviewer` (严谨, 善查 blind spot)
- `pr-review-toolkit:code-reviewer` — **已用** 禁选
- `oh-my-claudecode:code-reviewer` (与 pr-review-toolkit 的 code-reviewer **是不同 subagent_type**, 可选)
- `oh-my-claudecode:qa-tester` (tmux CLI 思维, 适合流程审)
- `oh-my-claudecode:scientist` (数据/证据思维)
- `oh-my-claudecode:document-specialist` (文档核实思维)
- **推荐**: `oh-my-claudecode:scientist` — 擅长证据/统计/分布核查, 匹配 P3.4.5 "语义命中率 + citation 精度" 两个定量判据

---

## Hard 约束 (P3.4 review addendums, 本步强制)

### HC-1: 独立 subagent_type reviewer 必派 (补规则 D 链)
- 主 session 落盘 evidence 后, **必须** 通过 `Agent` 工具派遣**与前 9 种不重复**的 subagent_type 做**独立复核**
- reviewer 输入: evidence md + prompt log + 答案全文
- reviewer 输出: 独立判据 verdict (PASS/CONDITIONAL_PASS/FAIL) + 每题单独核验 + 对 10/10 或 9/10 的 main-session 判分质疑
- reviewer 不是 "rubber stamp" — 必须独立重算每题 PASS/FAIL, 允许与 main-session 分歧, 分歧交用户仲裁

### HC-2: Citation 判据回到 inline text (不接受 DOM panel 代替)
- 每题答案**必须**肉眼检查 NotebookLM Chat 输出里的 inline citation 标记 (形如 `[1]`, `[2]`, 或 source 名引用 `[08_ev_adverse_ae.md]` 等)
- DOM panel `Bucket ID: N` 可作**辅助核对** (双保险), 但**不是** primary 判据
- 若 inline citation 缺失而 DOM panel 有源, 记作 F-1 漂移 **+1 计数** (本次必须真实统计漂移率, 不能 0/10)
- F-1 漂移率记入 evidence "F-1 真实漂移率" 段 (与 P3.4 的 "0/10 DOM 读取" 作对比)

### HC-3: Bucket 38 (或任何 >150K 大 bucket) 多区域采样
- 若抽到的 10 Req 变量里有 QS / FA / 其他 questionnaires 类, 且 citation 预期落在 bucket 38 或 39
- 则**额外**打 2 个补充验证题, 分别用变量定位到 bucket 38 的 part1 **头段** (AJCC 类, 位置 ~5%) 和 **尾段** (位置 ~95%) 的两个不同 codelist
- 若两个补充题都 PASS, bucket 38 的 "未截断" 断言才能写进 evidence
- 若只单区域 PASS, evidence 必须写 "**单区域验证, 不外推全 bucket**"

### HC-4: Prompt log 强制留档 (可 replay)
- cowork 若用 Chrome MCP 辅助提交 prompt, 每题**原始 prompt 字符串**必须 dump 到 `dev/evidence/p3_4_5_prompt_log.md`, 逐题原文
- 每题**原始答案完整文本** (不摘录) 也 dump 到同 log
- 用户若手动粘贴问, 也要把粘贴内容 copy-paste 到 log (不信口头声明 "原文未改字")
- reviewer (HC-1) 审的是 log, 不是 cowork 的总结

### HC-5: 执行/评分隔离 (Writer / Reviewer 分离)
- cowork 可自动化**提交 prompt** (Writer 级执行动作)
- cowork 可做**初判评分** (第一轮评估)
- 但**最终 verdict 不由 cowork 锁定** — 由 HC-1 的独立 subagent_type reviewer 出终审
- evidence 里同时记录 main-session 判分 + reviewer 判分 + 分歧项; 两判分都记, 不覆盖

---

## 环境固定参数

| 字段 | 值 |
|------|----|
| Notebook URL | https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287 |
| Notebook name | `SDTM Knowledge Base` |
| 账号 | `bojiang.zhang.0904@gmail.com` (personal Gmail, Rule E ack) |
| Tier | Pro (Google AI Pro) |
| Source 数 | 42 (P3.2 基线锁定) |
| Chat mode | Custom (instructions.md 9,011 chars, P3.3 Save 后未动; P3.4 未动) |
| instructions.md 快照 | `ai_platforms/notebooklm/current/instructions.md` |
| Uploads MANIFEST | `ai_platforms/notebooklm/current/uploads/MANIFEST.md` |
| Req 变量全集 | `dev/evidence/req_vars_full_set.md` (176 个: 9 通用 + 167 领域专属) |
| Bucket→Req 映射 | `dev/evidence/source_mapping.md` |

---

## 前置检查 (cowork 接手开工前 2 min)

```bash
# 1. 分支干净
git -C /Users/bojiangzhang/MyProject/SDTM-compare status --short
# 期望: 无 P3.2/P3.3/P3.4 已 commit 的基线文件改动

# 2. 42 个 uploads md 未变
ls /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/current/uploads/*.md | wc -l
# 期望: 42

# 3. instructions.md 未变
wc -c /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/current/instructions.md
# 期望: ~9011 chars (± 20)

# 4. req_vars_full_set 可读
wc -l /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/dev/evidence/req_vars_full_set.md
# 期望: 694 行

# 5. P3.4 commit 已推
git -C /Users/bojiangzhang/MyProject/SDTM-compare log --oneline -3
# 期望: HEAD 含 9dce0b0 Phase 6.5 NotebookLM P3.4
```

任一 FAIL → 回主 session. 不进 P3.4.5.

---

## Step 1: 主 session 独立随机抽 10 Req 变量 (~15 min, 主 session 执行)

### 1.1 抽样规则

从 `dev/evidence/req_vars_full_set.md` 的 176 变量池独立随机抽, 满足约束:

| 约束 | 目标数 |
|------|-------|
| Non-core domain 覆盖 (findings_other / findings_device / findings_morphology / 冷区) | **≥3 个** (P3.4 先验: DD/SS PASS, 本步再压深) |
| 大 bucket 38 / 39 覆盖 (QS / FA 类) | **≥2 个** (若抽到, 触发 HC-3 多区域采样) |
| IG 权威章覆盖 (ch04 规则类变量) | **≥1 个** |
| Special-purpose 域 (DM / SE / SV / CO) | **≥1 个** |
| Relationships (RELREC / RELSPEC / RELSUB 类) | **可选** |
| 避免与 P3.4 smoke 重复 (STUDYID/AESEQ/AETERM/AEDECOD/DDTESTCD/SSTESTCD) | **禁止重复** |

主 session 用 Python / 脚本抽 (seed 记录到 evidence), **cowork 不预览抽样结果, 直到 evidence 落盘前**.

### 1.2 抽样 seed 记录

抽样过程写 `dev/evidence/p3_4_5_sampling_log.md`:

```markdown
# P3.4.5 抽样 log

- 日期: YYYY-MM-DD
- 工具: Python random (seed=<固定整数>) / 或 bash shuf
- 输入: dev/evidence/req_vars_full_set.md (176 Req)
- 约束: 如上表
- 输出 10 变量:
  1. <domain>.<varname> — <期望 bucket>
  2. ...
- 审核: 主 session 检查约束达成 ✅/❌
```

---

## Step 2: 业务问答设计 (~15 min, 主 session + cowork 协作)

### 2.1 题目设计原则 (PLAN §6 P3.4.5)

**不是**: "AESEQ 的 Core 属性是什么?" (变量名查字典, 太浅)
**是**: "某 AE 域记录不良事件, 按 SDTMIG 要求哪些变量必填?" (业务场景, 测 RAG 语义召回)

**3 类题型模板** (每题选一类):

| 类型 | 模板 | 测什么 |
|------|------|-------|
| T1 场景驱动 | "某 SDTM 域记录 <业务事件>, 按 SDTMIG 要求哪些变量必填? Core 属性分别是?" | Req 召回 + Core 属性 |
| T2 CT 绑定 | "<变量> 的 controlled terminology 是哪个 codelist? C-code 是? 列出允许值." | 跨 source 召回 (spec → CT) |
| T3 跨域一致性 | "<变量> 在哪些 domain 出现? 语义一致吗? Core 属性有无 domain 特异?" | 跨 domain 召回 |

### 2.2 每题 PASS 判据 (硬约束版)

- **内容正解** (语义): Req 变量名 + Core 属性 + (T2 专有) C-code + 允许值 / (T3 专有) domain 列表一致性
- **Inline citation 精确回指** (HC-2): 答案**文本**内出现 `[N]` 或 `[bucketN_xxx.md]` 标记, 对应 source 面板 bucket 至少命中 1 个预期 bucket
- **F-1 漂移单独统计**: 若 inline 缺失但 DOM panel 有源, 记 F-1 +1, **不扣 PASS 分**

### 2.3 每题 FAIL 判据

- 答 "未收录" (RAG 召回失败, **严重**, 触发 cluster 回炉)
- 漏 Req 变量或错答 Core 属性 (Exp ↔ Req 混淆)
- C-code 幻觉 (T2)
- citation 完全指向无关 bucket (如 Q 问 AE 域答 indexing 却回指 bucket 36 specialized)

---

## Step 3: 用户 Chat 问答 + cowork prompt log 留档 (~45 min)

### 3.1 执行角色分工 (HC-5)

| 角色 | 做什么 | 不做什么 |
|------|-------|---------|
| 用户 | 选择亲自粘贴 or 授权 cowork 用 Chrome MCP 代跑 | N/A |
| cowork | (如授权) Chrome MCP 逐题原文提交, **每题 dump prompt 原文 + 答案原文到 `p3_4_5_prompt_log.md`** | 不自作判终审 (HC-5) |
| 主 session | 每题初判评分, 写 evidence 表 | 不做终审, 终审由 HC-1 reviewer |

### 3.2 Chat session 管理

- 每 3-4 题开新 chat session (避免 context 污染)
- Custom mode 保持激活全程
- 每题问完等答案完整 (poll 完成标记) 再下一题
- **严禁** cowork 改题字, 严禁加 "请说明" / "请详述" 等 hint

### 3.3 Prompt log 格式 (HC-4)

文件: `dev/evidence/p3_4_5_prompt_log.md`

```markdown
# P3.4.5 Raw Prompt & Answer Log

> 作用: HC-4 可 replay 留档. reviewer (HC-1) 审本 log 而非 evidence 摘录.

## Q1: <题号> — 变量 <varname> — 类型 <T1/T2/T3>

**Raw prompt** (原样未改字):
\`\`\`
<完整 prompt 字符串>
\`\`\`

**Raw answer** (Chat UI 完整输出, 含 inline citation 标记):
\`\`\`
<完整 answer 字符串>
\`\`\`

**Inline citation count**: <N 个, 列出每个标记如 [1][2][08_ev_adverse_ae.md]>
**DOM panel Bucket IDs**: <从源面板 DOM 读出的 bucket ID 列表, 作辅助核对>
**F-1 漂移**: YES (inline 缺失但 DOM 有) / NO (inline 正常)

---

## Q2: ...
```

### 3.4 HC-3 触发 (如适用)

若 Step 1.1 抽到 QS / FA 等 questionnaires 类 Req 变量且预期 bucket 是 38 或 39:
- 在 Step 3.2 标准 10 题问完后, 额外加 2 题**补充验证**:
  - 补题 A: 问 bucket 38 头段 codelist (如 AJCC) 的一个具体 code
  - 补题 B: 问 bucket 38 尾段 codelist (part1_22 最后一个 codelist) 的一个具体 code
- 两题都要求 citation 回指 bucket 38
- 两题都 PASS → evidence 可写 "bucket 38 多区域验证 PASS"
- 否则只写 "bucket 38 单区域 PASS, 不外推全 bucket"
- 补题**不计入** 10/10 主评分, 仅作 bucket 38 断言支撑

---

## Step 4: Evidence 落盘 + 主 session 初判 (~30 min)

cowork Claude 创建 `dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md`, 按下面模板填:

```markdown
# Phase 3 P3.4.5 — Req 变量业务问答抽检 N=10 (Q1 红线语义级自证, Rule A 正本)

> **日期**: <YYYY-MM-DD HH:MM>
> **执行者**: 主 session (抽题) + 用户 (Chat 问答 或 ack cowork 代跑) + cowork Claude (prompt log + 初判)
> **前置 commit**: <7 位 hash>
> **手顺**: dev/checkpoints/CHECKPOINT_P3.4.5_HANDOFF.md
> **Prompt log**: dev/evidence/p3_4_5_prompt_log.md (HC-4)
> **Sampling log**: dev/evidence/p3_4_5_sampling_log.md (Step 1.2)
> **P3.4 review addendums 应用状态**: HC-1 独立 reviewer 已派 [待 Step 5 填] / HC-2 inline citation 判据 [已生效] / HC-3 大 bucket 多区域 [N/A 或 已补验] / HC-4 prompt log [已留档] / HC-5 Writer/Reviewer 分离 [已执行]

---

## Step 1 抽样结果

- Seed: <固定整数>
- 10 变量清单 (domain.var → 期望 bucket):
  1. ...
- 约束达成: non-core ≥3 ✅/❌ / 大 bucket 38/39 ≥2 ✅/❌ / IG ch04 ≥1 ✅/❌ / special-purpose ≥1 ✅/❌ / 无 P3.4 重复 ✅/❌

---

## Step 2+3 10 题抽检结果

| Q | 变量 | 题型 | 期望 bucket | 内容正解? | Inline citation? | F-1 漂移? | DOM 辅助核? | 主判分 |
|---|------|------|------------|----------|------------------|----------|-------------|-------|
| 1 | <dom>.<var> | T1 | bucket XX | ✅/❌ | YES/NO (inline 标记原文) | NO/YES | bucket XX 命中 | 1.0/0.5/0.0 |
| ... | | | | | | | | |
| 10 | | | | | | | | |

**主判总分**: <N> / 10

**F-1 真实漂移率 (HC-2)**: <N> / 10 题 inline 缺失 (P3.4 用 DOM 读 0/10 是低估; 本次真实值)

**HC-3 bucket 38 多区域验证**: 补题 A PASS/FAIL + 补题 B PASS/FAIL / N/A (未抽到 bucket 38 变量)

---

## Step 5 独立 subagent_type reviewer 复核 (HC-1)

**Reviewer subagent_type**: <第 10 种, e.g., `oh-my-claudecode:scientist`>
**Reviewer 输入**: 本 evidence + prompt_log.md + sampling_log.md
**Reviewer 独立判分**:

| Q | 主判分 | Reviewer 判分 | 分歧? | Reviewer 理由 (如分歧) |
|---|-------|--------------|-------|----------------------|
| 1 | 1.0 | 1.0/0.5/0.0 | NO/YES | |
| ... | | | | |

**Reviewer 总分**: <N> / 10
**Reviewer verdict**: PASS / CONDITIONAL_PASS / FAIL
**分歧题数**: <N>
**用户仲裁** (如有分歧): 最终分数 <X>/10

---

## Exit 决策

| 判定 | 处置 |
|------|------|
| **10/10 + reviewer PASS** | Q1 红线语义级自证 CLOSED, 进 P3.5 |
| **9/10 + reviewer PASS/CONDITIONAL_PASS** | Q1 仍算 PASS (citation ≥9/10 硬阈值), 记录 1 题细节, 进 P3.5 |
| **≤8/10 或 reviewer FAIL** | **Q1 红线破**, 触发 Phase A A3 cluster bucket 回炉 + instructions.md 加强 citation 约束 + attempt_<X> 归档 (规则 B) |

## Rule 合规自检

| Rule | 状态 |
|------|------|
| A 语义抽检 (本步是正本) | ✅ 10 Req × 业务问答 × 独立 reviewer, 三重闭合 |
| B 失败归档 | 如 FAIL 题, 归档 failures/task_p3_4_5_attempt_<X>.md / 无 FAIL 填 ✅ |
| D 写审分离 | ✅ **本步启用第 10 种 subagent_type**, cumulative 链扩展到 10 种 (补 P3.4 松口子) |
| E 用户优先级 | ✅ personal Gmail + Pro + Web UI |

---

## 下游 handoff

P3.4.5 hard checkpoint 状态: PASS / CONDITIONAL_PASS / FAIL

如 PASS → Q1 红线 CLOSED (结构 A4 + 语义 P3.4.5 双锚闭合), 进 P3.5 Audio Overview × 3

---

*evidence 落盘日期: <YYYY-MM-DD>. 来源: 本手顺 Step 1-4 产出 + HC-1 独立 reviewer 复核 (subagent_type=<X>).*
```

---

## Step 5: 派独立 subagent_type reviewer (HC-1, ~45 min)

### 5.1 Reviewer 派遣命令 (主 session 执行)

```
Agent 工具调用:
- subagent_type: oh-my-claudecode:scientist (推荐, 或其他第 10 种候选)
- description: "P3.4.5 独立复核"
- prompt: 详述 P3.4.5 目标 + 提供 evidence md + prompt_log.md 路径 + sampling_log.md 路径 + 硬约束 HC-1/HC-2 说明; 要求独立重判每题, 不受 main-session 判分影响, 输出独立 verdict
```

### 5.2 Reviewer prompt 模板

```
你是 NotebookLM Phase 3 P3.4.5 的独立复核 reviewer (第 10 种 subagent_type, Rule D 链扩展). 本步是 Q1 红线语义级自证的独立核验.

## 输入
- evidence: /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md
- prompt log: /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/dev/evidence/p3_4_5_prompt_log.md
- sampling log: /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/dev/evidence/p3_4_5_sampling_log.md
- 判据: 本手顺 §2.2 + HC-2 (citation 必须 inline text, 不接受 DOM 代替)

## 任务
1. 审 prompt_log 里每题的**原始答案文本**, 不看 evidence 的摘录
2. 独立判每题 PASS/FAIL:
   - 内容语义是否命中预期 Req 变量 + Core + CT (按 T1/T2/T3 对应)
   - inline citation 是否出现在答案文本 (非 DOM)
   - 分歧于 main session 判分时, 给出详细理由
3. 核对 F-1 真实漂移率 (inline 缺失 / DOM 有源 的题数)
4. HC-3 多区域验证有效性 (如适用)
5. 出独立 verdict: PASS / CONDITIONAL_PASS / FAIL

## 输出
修改 evidence md 的 "Step 5" 段, 填入 reviewer 表 + verdict + 分歧理由
```

### 5.3 分歧处理

- 无分歧 → evidence 直接封, 进 Step 6
- 1-2 题分歧 → 回报用户仲裁, 用户判断; 用户 ack 后封
- ≥3 题分歧 → CONDITIONAL_PASS 最多, 主 session 评估是否补测

---

## Step 6: _progress.json 更新 + git commit (~30 min, cowork 执行)

### 6.1 _progress.json 更新

在 `phase_states.3_execute` 下加 `p3_4_5_completion` 节点, 并更新 top-level:

```json
"current_phase": "3_execute_p3.4.5_done_ready_for_p3.5",
"last_update": "<YYYY-MM-DD>_phase3_p3.4.5_done_ready_for_p3.5",

// phase_states.3_execute.status
"status": "p3_4_5_done_ready_for_p3_5",

// 新增 p3_4_5_completion
"p3_4_5_completion": {
  "date": "<YYYY-MM-DD>",
  "executor": "user (Chat 问答) + cowork (prompt log + 初判) + <10th subagent_type> (独立 reviewer)",
  "evidence": "dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md",
  "prompt_log": "dev/evidence/p3_4_5_prompt_log.md",
  "sampling_log": "dev/evidence/p3_4_5_sampling_log.md",
  "handoff_doc": "dev/checkpoints/CHECKPOINT_P3.4.5_HANDOFF.md",
  "sub_steps": {
    "main_session_initial_score": "<N>/10",
    "reviewer_score": "<N>/10",
    "final_score_after_user_arbitration": "<N>/10",
    "f_1_real_drift_count": "<N>/10 (inline 判据 HC-2, 与 P3.4 DOM 读取 0/10 对比)",
    "hc_3_bucket_38_multi_region": "PASS / N/A"
  },
  "rule_d_chain_extension": {
    "new_subagent_type_added": "<10th type, e.g., oh-my-claudecode:scientist>",
    "cumulative_chain_count": 10,
    "cumulative_chain_list": [
      "general-purpose", "oh-my-claudecode:verifier", "oh-my-claudecode:executor",
      "oh-my-claudecode:critic", "oh-my-claudecode:planner", "oh-my-claudecode:analyst",
      "feature-dev:code-architect", "pr-review-toolkit:code-reviewer", "oh-my-claudecode:architect",
      "<10th>"
    ]
  },
  "q1_red_line_closure": {
    "structure_level_a4": "PASS (Phase A, 176/176 ∅ gap)",
    "semantic_level_p3_4_5": "PASS / CONDITIONAL_PASS / FAIL",
    "dual_anchor_closed": true / false
  },
  "ready_for_p3_5": true / false
}
```

### 6.2 Commit

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/notebooklm/dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md \
        ai_platforms/notebooklm/dev/evidence/p3_4_5_prompt_log.md \
        ai_platforms/notebooklm/dev/evidence/p3_4_5_sampling_log.md \
        ai_platforms/notebooklm/dev/evidence/_progress.json

git commit -m "$(cat <<'EOF'
Phase 6.5 NotebookLM: Phase 3 P3.4.5 完成 (Q1 红线语义级自证, Rule A 正本)

10 Req 业务问答抽检 <N>/10 (main) → 第 10 种 subagent_type <X> 独立 reviewer 复核 <N>/10. Q1 红线双锚 (结构 A4 + 语义 P3.4.5) 闭合. F-1 inline citation 真实漂移率 <N>/10 (修正 P3.4 DOM 读取的 0/10 低估). Rule D 链扩展到 10 种, 补 P3.4 松口子.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## 失败回退决策树

| 症状 | 判定 | 动作 |
|------|------|------|
| 抽样约束不达 (non-core <3 / 大 bucket <2) | 抽样重跑 | 改 seed 重抽, 记录两次 sampling log |
| 某题答 "未收录" | RAG 召回失败 | FAIL 该题; 若 >1 题, Q1 红线破, 回 Phase A A3 |
| inline citation 缺失但 DOM 有 >5/10 | F-1 漂移率高 | 记入 P3.8 风险条; 若 >8/10 主 session 微调 instructions.md 规则 2 |
| main vs reviewer 分歧 ≥3 题 | 判据本身有歧义 / RAG 噪声大 | CONDITIONAL_PASS; 用户仲裁 + evidence 透明记录 |
| reviewer 给 FAIL | 语义命中不达标 | Q1 红线破; cluster bucket 回炉 + attempt_<X> 归档 |
| HC-3 bucket 38 多区域仅一区 PASS | 大 bucket 边界可能有洞 | evidence 写 "单区域 PASS", 挪 P3.8 加题深查 |

---

## 不在 P3.4.5 scope (明示)

- ❌ Audio Overview × 3 → **P3.5**
- ❌ Mind Map → **P3.6**
- ❌ Study Guide → **P3.7**
- ❌ A/B 15 题 → **P3.8**
- ❌ 3 档分享切换 → **P3.9**
- ❌ `_template/` 11 条补丁 PR → Phase 5

**P3.4.5 只关注**: 10 Req 业务语义命中 + inline citation + 独立 reviewer 复核.

---

## Rule D 链扩展声明 (本手顺权威定调)

P3.4.5 **必须** 占用第 10 种 subagent_type slot. 前 9 种 subagent_type 列表见 _progress.json `cumulative_rule_d_chain_subagent_types_phase_0_to_2` + v2 extension.

**新 slot 不能复用前 9 种**. 推荐 `oh-my-claudecode:scientist` (数据/证据思维匹配语义命中率 + citation 精度量化判据).

**P3.4 松口子**: P3.2/P3.3/P3.4 都走 "UI 工具级不占 slot" 路线. P3.4.5 起重新强制每个 hard checkpoint 都派独立 reviewer, 不允许 cowork 自评自跑成终审.

---

## 关联项 (P3.4 review addendums 全集应用)

| Addendum | 本步体现 |
|----------|---------|
| A1 Writer/Reviewer 隔离弱化 | HC-1 + HC-5 强制独立 subagent_type |
| A2 Citation 判据 inline 回归 | HC-2 强制 |
| A3 Checkpoint 入 git | 本文件 P3.4.5 启动前已补 commit P3.4 handoff |
| A4 大 bucket 单题外推 | HC-3 多区域采样 |
| A5 Prompt log 缺证据 | HC-4 强制 dump 原始 prompt + answer |

---

## 给 cowork Claude 的额外提示

1. **不要自判终审** — 你的角色是 Writer + 初判 + prompt log 留档. 最终 verdict 走 HC-1 独立 reviewer.
2. **不要改 instructions.md / uploads** — P3.4.5 是抽检, 不改 Writer 基线.
3. **不要自选 subagent_type** — 10th slot 派遣由主 session 决策.
4. **Prompt log 不得摘录** — dump 原始 prompt + 原始 answer 全文, 不 TLDR.
5. **Inline citation 真实漂移要记** — 哪怕 100% 都漂, 也如实记. 不要为 "F-1 CLOSED" 的 P3.3 结论背书.
6. **Seed 保留** — 抽样 seed 写 log, 可复现.
7. **分歧题不硬判** — 标 "判定存疑" 待 reviewer + 用户仲裁.

---

## 估时与节奏建议

| 环节 | 估时 | 谁做 |
|------|:----:|------|
| 前置检查 | 2 min | cowork |
| Step 1 抽样 | 15 min | 主 session |
| Step 2 设题 | 15 min | 主 session + cowork |
| Step 3 问答 + log | 45 min | 用户 / cowork + prompt log |
| Step 4 evidence 落盘 + 主判 | 30 min | cowork |
| Step 5 独立 reviewer | 45 min | 第 10 种 subagent_type |
| Step 6 _progress.json + commit | 30 min | cowork |
| 用户仲裁 (如分歧) | 15 min | 用户 |
| **总计** | **~3 h** | |

Q2 保险 2x → 6 h 内可收, **不跨天**, 允许跨 session.

---

## 入口文件引用清单

| 文件 | 作用 |
|------|------|
| `docs/PLAN.md` §6 P3.4.5 | 原始规格 (M1 fix) |
| `dev/evidence/_progress.json` | P3.4 完成状态 + carry_over_to_p3_4_5 + Rule D 链 9 种 |
| `dev/evidence/indexing_smoke.md` | P3.4 evidence + P3.4 先验信心加强项 |
| `dev/evidence/req_vars_full_set.md` | 176 Req 变量全名单 (抽样池) |
| `dev/evidence/source_mapping.md` | bucket ↔ domain ↔ Req 映射 (期望 bucket 查表) |
| `current/uploads/MANIFEST.md` | 42 bucket 清单 |
| `current/instructions.md` | Custom mode 规则 (判据依据) |
| `.work/meta/retrospective.md` § 4 | 四条全局规则 A/B/C/D |
| `CLAUDE.md` Session Wrap-up | 收尾 Chain |

---

*本手顺产出日期: 2026-04-22. 来源: `docs/PLAN.md` §6 P3.4.5 (M1 fix) + `_progress.json` P3.4 carry_over_to_p3_4_5 + P3.4 事后 review 识别的 5 条方法论层疏漏 (HC-1..HC-5 硬约束化).*
