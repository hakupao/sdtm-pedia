# ChatGPT GPTs — Phase 3 Node 3b 执行手册 (Agent 优先 + 用户 Fallback)

> **双模式手册**: computer-use / chrome-devtools / playwright / claude-in-chrome MCP agent 优先执行 (Mode A); 遇无法做的 step (登录态 / 原生文件选择器) 自动 fallback 指示用户 (Mode B); 全程用户可接管 (Mode C).
> 模仿 `claude_projects/dev/checkpoints/CHECKPOINT_V2.*_HANDOFF.md` 的 Cowork 手册结构, 扩展为 agent + 用户通读版.
> 完成后报告粘回 Claude Code session, 主 session 派 Rule D smoke reviewer + 准备 commit C3b.

---

## 图例

| 标记 | 含义 |
|:---:|---|
| 🤖 | **Agent 可独立完成** (读文件 / 浏览器自动化 / 读 DOM) |
| 🙋 | **必须用户做** (登录态 / 原生 OS 文件选择器 / 账号权限) |
| 🤝 | **Agent 先尝试, 失败 fallback 用户** (可能遇反自动化 / 新 UI 变化) |

---

## 背景 (≤ 120 字)

Phase 3 Node 3a 双边 bundled PASS (Writer×2 + Reviewer×2, 9 种 subagent_type 独立链) 已 commit (C3a = cb13817). **Node 3b 是唯一必须人/agent 在浏览器里跑的环节**.

本批 **ChatGPT GPTs 批 1** = 4 文件 / 310,134 tokens (01/02/03/04), 使用 RAG + 20 文件硬限 + Indexing "Ready" 指示. PASS 判据 **≥ 4/5**, FAIL ≥ 2 走 P10 停机.

---

## 执行模式选择 (Agent 启动时先自检)

**Agent 自检清单** (开工前):
```
1. 是否有 claude-in-chrome MCP (mcp__claude-in-chrome__*)?
   → 有: 首选, 浏览器 DOM 原生可控, tier-full 不受 browser read-only 限制
   → 无: 降 computer-use + screenshot, 但 browser 是 tier "read" (点击被阻止), 必须 chrome MCP
2. 是否有 playwright/chrome-devtools MCP?
   → 有: 备选, 同样 DOM 可控
3. 以上都无?
   → 降 Mode C (全程用户手动)
```

**用户启动时**: 若不想让 agent 试, 直接按所有 🤖 / 🤝 step 人肉操作, 跳过 Mode A 指令.

---

## 你 (Agent / 用户) 的任务

在 `chat.openai.com` 账号下:
1. 🤝 新建 GPT `SDTM Expert` (Configure tab, **非** Create 问答模式)
2. 🤖/🤝 配置 Name / Description / Instructions / Conversation Starters
3. 🙋 **上传 4 个文件 (原生文件选择器, agent 大概率做不到)**
4. 🤖/🤝 关闭 Capabilities
5. 🙋 等 Indexing `Processing` → `Ready` (无 DOM 事件, agent 只能轮询 screenshot)
6. 🤖 Preview 跑 5 题 smoke (DOM 可控)
7. 🤖 读 5 个回答 + 按模板填报告
8. 🙋 把报告粘回 Claude Code session

**Agent 权限假设**: 用户已登录 OpenAI Plus/Team/Enterprise (Agent **不自行登录**, 若未登录**立即停并提示用户**).

**工作目录**: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/`

---

## Step 1: 打开 ChatGPT 并确认登录 🤝

**🤖 Agent 指令** (Mode A / chrome MCP):
```
tool: mcp__claude-in-chrome__navigate 或 mcp__playwright__browser_navigate
url: https://chat.openai.com
→ screenshot / snapshot → 确认右上角头像 (已登录) + 左侧 Explore GPTs 菜单可见
→ 若登录墙出现 (email/password 输入框): STOP, 输出 "未登录, 用户请登录后告知 agent 继续"
→ 已登录: 点击 左侧 "Explore GPTs" → 右上 "+ Create"
→ 进入 GPT Builder, 切到 "Configure" tab (**不是** Create 聊天模式)
```

**🙋 用户 Fallback / 手动**:
1. 浏览器打开 `https://chat.openai.com`, 确认右上头像 (已登录)
2. 左侧 **Explore GPTs** → 右上 **+ Create** → 切到 **Configure** tab

---

## Step 2: 填 Name + Description 🤖

**🤖 Agent 指令**:
```
DOM 定位: Configure tab 下的 "Name" 输入框 + "Description" 输入框
Name 值: "SDTM Expert"
Description 值 (130 chars): "CDISC SDTMIG v3.4 + SDTM v2.0 Expert - Variable definitions, rule reasoning, controlled terminology, cross-domain linking"
操作: fill / type 到对应框
验证: screenshot 后读回 DOM, 确认两字段值匹配
```

**🙋 用户 Fallback**: 同内容手填.

---

## Step 3: 粘贴 Instructions (System Prompt) 🤖

**🤖 Agent 指令**:
```
Step 3.1: Read /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/current/system_prompt.md
         → 预期 4782 chars (≤ 7500 budget, buffer 36.2%)
Step 3.2: DOM 定位 "Instructions" 多行输入框
Step 3.3: 清空当前内容, 全文粘贴 system_prompt.md
         (agent 方法: fill 整段, 或 type 全文; chrome MCP 推荐 fill)
Step 3.4: screenshot 验证 DOM value 包含 "# SDTM Expert — GPT Instructions" (文首标志) 和 "Conversation Starters" (文末标志)
Step 3.5: 若 UI 报 "Instructions too long / 字符超限":
         → 停, 截 screenshot 记录阈值, 回报 Phase 1 MEDIUM carry-over 实测数据
         → 继续 (因本 prompt 设计在 budget 内, 不该触发)
```

**🙋 用户 Fallback**:
1. 用文本编辑器打开 `current/system_prompt.md`, `Cmd+A` 全选, `Cmd+C` 复制
2. 浏览器 Instructions 框 `Cmd+V` 粘贴

**Phase 1 MEDIUM 实测 carry-over**: UI 报错时记录阈值 → `dev/evidence/phase3_instructions_budget_reality.md` (主 session 建文件).

---

## Step 4: 填 Conversation Starters (4 条) 🤖

**🤖 Agent 指令**:
```
DOM 定位: "Conversation starters" 段下 4 个输入框 (通常为 "+ Add" 可新增)
填充 4 条 (从 system_prompt.md 末尾段复制):
  1. "AE 域的 AESER 变量定义是什么? 有哪些允许值?"
  2. "RELREC 是什么? 什么场景下需要用它?"
  3. "PC 和 PP 域之间是什么关系? 如何关联?"
  4. "ISO 8601 日期格式在 SDTM 中有什么特殊规则?"
操作: 逐条 fill
验证: screenshot 读回 DOM 全 4 条到位
```

**🙋 用户 Fallback**: 同内容手填.

---

## Step 5: 🚨 上传 4 个文件到 Knowledge 🙋 (Agent 大概率做不到)

**⚠️ 已知限制**: GPT Builder 的 "Upload files" 按钮触发**原生 OS 文件选择器对话框**, 这是浏览器外的 OS 原生控件. **computer-use tier-full 理论上可操作文件选择器, 但 chrome MCP / playwright 无法跨域到 OS 对话框**. 先前测试 agent **做不到上传文件**.

**🤝 Agent 尝试** (仅 Mode A 且有 computer-use 并愿意试一次):
```
Step 5.1: DOM 点击 "Upload files" 按钮 → 触发 OS 文件选择器
Step 5.2: 切换到 computer-use 模式 (若 agent 有 computer-use 工具)
         → request_access 应用 ["Chrome", "Finder" 或 OS 文件选择器 app]
         → screenshot 确认文件选择器可见
Step 5.3: 依次导航到 4 个绝对路径, 选中 + Open
         → /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/current/uploads/01_navigation.md
         → ... 02_chapters_all.md
         → ... 03_model_all.md
         → ... 04_domain_specs_all.md
Step 5.4: 失败则 STOP, 输出 "Agent 无法操作文件选择器, 用户请手动上传 4 个文件后告知 agent 继续"
```

**🙋 用户 Fallback (默认路径)**:

**上传顺序 = score 降序 (PLAN §3.2 v1.1): 01 > 02 > 03 > 04**

| # | 绝对路径 | tokens (实测) | cap | buffer | sources | 用途 |
|---|---------|--------------:|----:|-------:|--------:|------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/current/uploads/01_navigation.md` | 46,170 | 47,000 | 1.77% | 3 | ROUTING + INDEX + VARIABLE_INDEX (先读) |
| 2 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/current/uploads/02_chapters_all.md` | 60,607 | 72,000 | 15.82% | 6 | SDTMIG ch01/02/03/04/08/10 |
| 3 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/current/uploads/03_model_all.md` | 17,653 | 21,000 | 15.94% | 6 | SDTM v2.0 Model |
| 4 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/current/uploads/04_domain_specs_all.md` | 185,704 | 193,000 | 3.78% | 63 | 63 域 spec (Rule E Q5=A 全量平权) |

**总计**: 310,134 tokens, 4/20 文件 (16 spare for 批 2).

**🚫 绝对不要上传** (meta / dev 文件, agent 和用户都避开):
- `upload_manifest.md` (dev 文档)
- `system_prompt.md` (已在 Instructions)
- `smoke_questions_draft.md` (dev 测试)
- `phase3_*_reviewer.md` (evidence)
- `dev/` 目录下任何文件
- 本 handoff 文件

---

## Step 6: 关闭 Capabilities (纯知识问答) 🤖

**🤖 Agent 指令**:
```
DOM 定位: Configure tab 下 "Capabilities" 段的 3 个 checkbox
操作: 确保 3 个都 unchecked
  - Web Search: unchecked
  - Code Interpreter (Advanced Data Analysis): unchecked
  - DALL-E Image Gen: unchecked
  - (若有) Canvas: unchecked
验证: screenshot 读回 aria-checked=false
```

**🙋 用户 Fallback**: 同内容手操作 checkbox.

**原因** (两种读者都要理解): 本 GPT 是知识问答, 启用反而增 hallucinate 面. Web Search 可能答过期/错信息, Code Interpreter 跟问题无关.

---

## Step 7: 等 Indexing "Processing" → "Ready" 🙋 (agent 只能轮询)

**🤝 Agent 轮询指令**:
```
Step 7.1: 每 60 秒 screenshot + snapshot, 读 Knowledge 段的 4 个文件状态
         → 寻找每文件状态是 "Processing..." / "Ready" / 绿色勾 / 红色错
Step 7.2: 记录 Indexing start 时间 + 每文件 Ready 时间
Step 7.3: 4 文件全 Ready 才进 Step 8 (否则 Q8 Indexing 假阳性)
Step 7.4: 若 >20 分钟仍 Processing: STOP 回报用户
Step 7.5: 若某文件显示 Error / Failed: STOP 回报用户 (可能需重上传)
```

**🙋 用户 Fallback**: 盯 Knowledge 列表到 4 文件全绿勾 / `Ready`, 记时长.

**Q8 Indexing 实测 (Phase 1 PARTIAL carry-over)**: 若 UI 已 `Ready` 但 smoke S5 答 "无法找到/无法访问 knowledge" → Indexing indicator 不可靠, 这是本 Node **关键发现**之一, 必记录归 `dev/evidence/phase3_q8_indexing_reality.md`.

---

## Step 8: Preview 面板跑 5 题 Smoke 🤖

**🤖 Agent 指令 (总纲)**:
```
Step 8.1: 右上角点击 "Preview" 按钮 → 打开对话窗 (DOM 可控)
Step 8.2: 对 S1-S5 每一题:
  a. DOM fill 输入框 = 题面文本
  b. 点 Send / 回车
  c. 等回答流式结束 (监控 DOM "stop generating" 按钮消失, 或 >30s 无更新)
  d. 读取最新 assistant message 的 innerText
  e. 保存到 agent 本地 "Qx answer" 变量
Step 8.3: 5 题全跑完后, 按 Step 9 模板组装报告
Step 8.4: 每题一条消息, 不合并; 若对话过长被 UI 截断, 开新 chat 继续 (Start new chat)
```

**🙋 用户 Fallback**: Preview 面板, 按 S1→S5 顺序逐题, 复制回答到记事本或直接进 Step 9 模板.

---

### S1 — 路由 / 变量精确查询 (PLAN §7.3 T01)

**问**: `AE 域的 AESER 变量定义是什么?`

**预期命中**: `04_domain_specs_all.md` → AE 段 → AESER 行

**PASS 判据** (全中才 PASS):
- ✅ 引用变量名 `AE.AESER` 或 `AESER`
- ✅ 给 Role (Record Qualifier)
- ✅ 给 Core (Perm 或等价)
- ✅ 若给 CT Code, 须 `C66742` / NY, 不编其他码
- ✅ **零臆造允许值** (不编 Y/N/U/NA)
- ✅ 源溯源: 答案含 `<!-- source: knowledge_base/domains/AE/spec.md -->` 或类似文字

---

### S2 — 跨域关联 (PLAN §7.3 T02)

**问**: `RELREC 是什么?`

**预期命中**: `02_chapters_all.md` (ch08) + `04_domain_specs_all.md` 相关域

**PASS 判据**:
- ✅ 识别为**关联关系数据集** (Related Records)
- ✅ 给使用场景 (跨域关联)
- ✅ **不臆造具体字段**; 若给字段必须 ch08 明写 + 源溯源
- ⚠️ **臆造陷阱**: RELREC 字段是常识, 模型可能从预训练答; 无源溯源 → 降级 PARTIAL

---

### S3 — 边界诚实 (PLAN §7.3 T03, **关键题, 公开 GPT 底线**)

**问**: `AERELN codelist 所有 Synonyms 是什么?`

**预期命中**: 批 1 **无 terminology** → 走边界模板 ②

**预期合规响应**:
> "批 1 未上传 terminology (见批 2 07_terminology_core 或源 `knowledge_base/terminology/core/*.md`). 完整 Synonyms 请查 [NCI EVS Browser](https://evsexplore.semantics.cancer.gov/)."

**PASS 判据**:
- ✅ **零臆造 Synonyms**
- ✅ 声明 "批 1 未收录 terminology Term 值"
- ✅ 给外部入口 (NCI EVS / 源路径)
- ❌ **任何臆造 synonym 即 FAIL** (Rule E Q1=C 公开场景零容忍)

---

### S4 — Q1=C 公开受众语气 (PLAN §7.2 T13, v1.3 升"必测")

**问**: `我是病人家属, 能简单解释 SDTM 是什么吗?`

**PASS 判据**:
- ✅ **新手友好**: 首段必有通俗类比 (Excel/标准化病历)
- ✅ **无术语堆砌**: 第一段不抛 "General Observation Class" / "Domain Model"
- ✅ **类比恰当**: Excel / 表格 (不用股票/编程跨域)
- ✅ **不假设行业背景**: 不说 "如您熟悉的 CDASH/ADaM..."
- ✅ **术语立刻解释**
- ✅ **专家路径仍可见**: 末尾可给 "如需技术细节见 §2.1"

---

### S5 — Q8 Indexing Indicator 实测 (Phase 1 PARTIAL carry-over, 必测)

**问**: `根据 04_domain_specs_all.md, 请列出 AE 域 Core=Req 的变量名 (至少 3 个)`

**预期命中**: `04_domain_specs_all.md` → AE 段前部 Identifier + Topic 变量

**预期答候选集**: `STUDYID` / `DOMAIN` / `USUBJID` / `AESEQ` / `AETERM` / `AEDECOD` 等

**PASS 判据**:
- ✅ 命中 3+ Req 变量
- ✅ 变量名拼写正确
- ✅ 注明 Core 字段来自 `04_domain_specs_all.md`

**Q8 失败信号** (独立归 `dev/evidence/phase3_q8_indexing_reality.md`):
- 🔴 UI `Ready` 但答 "无法找到" → Indexing indicator 不可靠
- 🟡 答错非 Req (如 AESPID) → chunk 覆盖不足, 非 Q8 问题

---

## Step 9: 填写报告模板 🤖 + 🙋

**🤖 Agent 指令**: Step 8 收集 5 个回答后, 按下模板填空, 用 Write 工具写到:
```
/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/chatgpt_gpt/dev/evidence/smoke_batch1_results.md
```

**🙋 用户 Fallback**: 按模板填空, 直接粘回 Claude Code session.

```markdown
# ChatGPT GPTs — Phase 3 Node 3b Smoke 报告

> 执行日期: 2026-04-XX HH:MM
> 执行者: Agent (chrome MCP / computer-use) / 用户
> GPT Name: SDTM Expert

## Step 2-7 配置确认
- [x] Name: SDTM Expert
- [x] Description: <130 chars>
- [x] Instructions: system_prompt.md 全文粘贴 (<实测 char_count>, UI 超限: 是/否)
- [x] Conversation Starters: 4 条全填
- [x] Knowledge: 4 文件按 01→02→03→04 顺序上传
- [x] Capabilities: Web Search/Code Interpreter/DALL-E 全关
- [x] Indexing: 4 文件全 Ready (总用时 N 分钟)

## Q8 Indexing 实测 (关键 carry-over)
- Indexing indicator 可靠性: 可靠 / 不可靠 / 待定
- 观察: <若 Ready 后 S5 命中即可靠; 若 Ready 后 S5 答无法访问不可靠>

## Smoke 5 题结果明细

### S1. AE 域 AESER 变量定义
- **答**: <完整粘贴 GPT 回答>
- **PASS/FAIL**: PASS / FAIL / PARTIAL
- **源路径引用**: 是 (<路径>) / 否
- **是否臆造**: 否 / 是 (<具体点>)
- **备注**: ...

### S2. RELREC 是什么?
- **答**: ...
- **PASS/FAIL**: ...
- **源路径引用**: 是 (<ch08 ?>) / 否 → PARTIAL
- **是否臆造 RELREC 字段**: 否 / 是
- **备注**: ...

### S3. AERELN Synonyms
- **答**: ...
- **PASS/FAIL**: ...
- **是否走边界模板**: 是 / 否
- **是否臆造 Synonym**: 否 (PASS 必需) / 是 → FAIL
- **是否给外部入口**: 是 (NCI EVS / 源路径) / 否
- **备注**: ...

### S4. 病人家属解释 SDTM
- **答**: ...
- **PASS/FAIL**: ...
- **首段类比**: 有 (<什么类比>) / 无 → FAIL
- **第一段是否纯术语**: 是 → FAIL / 否
- **术语立刻解释**: 是 / 否
- **备注**: ...

### S5. AE Core=Req 变量 3 个
- **答**: ...
- **PASS/FAIL**: ...
- **命中 Req 变量数**: N (目标 ≥3)
- **拼写是否正确**: 是 / 否
- **是否注明 04 文件**: 是 / 否
- **备注**: ...

## 汇总
- **PASS 比**: N/5 (目标 ≥ 4/5)
- **FAIL 题**: [列 S-id + 原因]
- **PARTIAL 题**: [列 S-id + 原因]

## 关键观察 (2-4 句)
- <例: "S2 答出 RELREC 4 字段但无源溯源, 判 PARTIAL">
- <例: "S4 首段通俗 + 第二段专业, 混合受众 PASS. Q1=C 公开语气兑现">
- <例: "Indexing 12 分钟完成 4 文件, UI Ready 与 S5 命中一致, 可靠">

## 异常/警告
- <或 "无异常">

## 浏览器截图 (Agent 贴 screenshot 路径 / 用户可选贴链接)
- <Knowledge 列表 / 某一题回答 / Capacity 指示>

## 执行元数据 (agent 填, 用户可留空)
- 浏览器工具链: chrome-MCP / playwright / computer-use / 用户手动
- Step 5 上传模式: agent fallback 用户 / agent 成功 / 用户全程手动
- 总用时: N 分钟
```

---

## Step 10: 交回主 session 🙋

粘完报告 (或 agent Write 到 evidence 后) 通知主 session.

**不要自己判 overall PASS/FAIL** — 主 session 会:
1. 派 Rule D smoke reviewer (不同 subagent_type, 第 10 种) 独立复核
2. 归档 `dev/evidence/smoke_batch1_results.md` + `phase3_q8_indexing_reality.md`
3. 按决策矩阵推进 Node 4 或 attempt_2
4. commit C3b

---

## 决策矩阵 (供主控参考)

| 报告 | 主控决策 |
|---------|---------|
| ≥ 4/5 PASS + 无臆造 | 派 Rule D reviewer + commit C3b + 进 Node 4 (批 2 合并) |
| < 4/5 PASS, S3 未触 | 归因 + attempt_2 |
| **S3 FAIL (臆造 Synonym)** | **关键 FAIL**, Instructions §零臆造补强, 必 attempt_2 |
| S4 FAIL (纯术语无类比) | Instructions §陌生公开受众补强 |
| S5 FAIL + 答"无法访问" | Q8 实锤不可靠, 考虑重上传 |
| Capacity 超限 / 上传失败 | 记 evidence, 决定是否拆文件 |

---

## 不要做 (agent + 用户都适用)

- **不要自行登录** chat.openai.com (agent 见登录墙立停提示用户)
- **不要自行判 overall PASS/FAIL** — 留给主 session + reviewer
- **不要编造 GPT 的回答** — 如实粘贴 UI 看到的, 即使 "I don't know" / 拒答
- **不要修改** `current/uploads/` 任何 .md
- **不要跳题** — 5 题必全跑 (S3/S5 关键 gate)
- **不要上传 meta** (upload_manifest / smoke_questions_draft / dev/* / 本 handoff)
- **不要延长 Instructions** — 只粘 system_prompt.md 原文
- **不要启用 Web Search** — 绕过 Knowledge, hallucinate 高
- **不要在 Indexing 未 Ready 时跑 smoke** — 假阴性
- **(agent)** 不要在原生文件选择器强推, 失败即停提示用户
- **(agent)** 不要轮询间隔 <30s (浪费 token + 可能触发反爬)

---

## 完成信号

报告送达主 session 后:
1. 主 session 派 Rule D smoke reviewer (第 10 种 subagent_type)
2. 归档 evidence
3. 按决策矩阵进 Node 4 或 attempt_2
4. commit C3b bundled (双平台 smoke 结果 + reviewer + SYNC_BOARD 更新)

**Agent 准备好从 Step 1 开始; 用户准备好跟 agent 协作或自己从 Step 1 手动开始.**

---

*来源: PLAN v1.3 §7.2/§7.3 + `smoke_questions_draft.md` + `upload_manifest.md` + Phase 1 research.md carry-over + Phase 3 Node 3a reviewer 产物 + claude_projects/dev/checkpoints/CHECKPOINT_V2.*_HANDOFF.md 结构*
