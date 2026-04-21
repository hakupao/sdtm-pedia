# Gemini Gems — Phase 3 Node 3b 执行手册 (Agent 优先 + 用户 Fallback)

> **双模式手册**: computer-use / chrome-devtools / playwright / claude-in-chrome MCP agent 优先执行 (Mode A); 遇无法做的 step (登录态 / 原生文件选择器) 自动 fallback 指示用户 (Mode B); 全程用户可接管 (Mode C).
> 模仿 `claude_projects/dev/checkpoints/CHECKPOINT_V2.*_HANDOFF.md` 的 Cowork 手册结构, 扩展为 agent + 用户通读版.
> 完成后报告粘回 Claude Code session, 主 session 派 Rule D smoke reviewer + 准备 commit C3b.

---

## 图例

| 标记 | 含义 |
|:---:|---|
| 🤖 | **Agent 可独立完成** (读文件 / 浏览器自动化 / 读 DOM) |
| 🙋 | **必须用户做** (登录态 / 原生 OS 文件选择器 / Google Pro 订阅权限) |
| 🤝 | **Agent 先尝试, 失败 fallback 用户** |

---

## 背景 (≤ 150 字)

Phase 3 Node 3a 双边 bundled PASS (Writer×2 + Reviewer×2, 9 种 subagent_type 独立链) 已 commit (C3a = cb13817).

本批 **Gemini Gems 单批即终态** (PLAN §5 P11) = **4 文件 / 884,918 tokens / 88.49% 窗口占用** (1M 上下文, 预留 ~115K 响应 buffer). **无 RAG / 无 indexing / 秒级就绪** — 上传即用, 全文始终在上下文.

**关键差异 vs ChatGPT**:
- Gemini 无 indexing 指示器 (Agent 不用轮询, 用户不用等)
- **S3 + S4 独立 P12 hard gate** (末尾召回 + Lost-in-Middle), 任一 FAIL 触发 P12 R1/R2
- 发布语义 = **分享链接给同事**, 非 GPT Store 广播; smoke 不含陌生公开受众题

PASS 判据 **≥ 4/5**, **S3 FAIL 停机**, **S3+S4 都 FAIL 触发 P12 R2 拆 04**.

---

## 执行模式选择 (Agent 启动时先自检)

**Agent 自检清单** (开工前):
```
1. 是否有 claude-in-chrome MCP / playwright / chrome-devtools MCP?
   → 有: 首选, DOM 原生可控
   → 无: 降 computer-use + screenshot (browser tier "read" 点击受限, 必须 chrome MCP 才可)
2. 以上都无?
   → 降 Mode C (全程用户手动)
```

**用户启动时**: 若不想让 agent 试, 直接按所有 🤖 / 🤝 step 人肉操作.

---

## 你 (Agent / 用户) 的任务

在 `gemini.google.com` + **Google AI Pro** 订阅账号下:
1. 🤝 新建 Gem `SDTM Expert` (Gems → New Gem)
2. 🤖/🤝 配置 Name / Description / Custom Instructions
3. 🙋 **上传 4 个文件 (原生文件选择器, agent 大概率做不到)**
4. 🤖 Save Gem (无 indexing, 秒级就绪)
5. 🤖 Preview 跑 5 题 smoke (含 2 题 P12 hard gate)
6. 🤖 读 5 个回答 + 按模板填报告
7. 🙋 把报告粘回 Claude Code session

**Agent 权限假设**: 用户已登录 Google 账号 + Google AI Pro 订阅活跃 (Agent **不自行登录/订阅**).

**工作目录**: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/`

---

## Step 1: 打开 Gemini 并确认订阅 🤝

**🤖 Agent 指令** (Mode A / chrome MCP):
```
tool: mcp__claude-in-chrome__navigate 或 mcp__playwright__browser_navigate
url: https://gemini.google.com
→ screenshot → 确认右上角 Google 账号头像 (已登录)
→ 若登录墙 / 账号选择器: STOP 提示用户登录后告知 agent 继续
→ 已登录: 检查左下角 "Google AI Pro" / "Gemini Advanced" 订阅标识
  → 无订阅标识: STOP 提示 "需 Google AI Pro 订阅才有 Gem 创建权, 用户请订阅或确认"
→ 有订阅: 左侧导航点 "Gems" → 点 "+ New Gem" / "Create a Gem"
```

**🙋 用户 Fallback / 手动**:
1. 浏览器打开 `https://gemini.google.com`, 确认登录 + Google AI Pro 订阅
2. 左侧 **Gems** → **+ New Gem**

---

## Step 2: 填 Name + Description 🤖

**🤖 Agent 指令**:
```
DOM 定位: "Name" 输入框 + "Description" 输入框
Name 值: "SDTM Expert"
Description 值 (140 chars, ≤ 280 上限):
  "CDISC SDTMIG v3.4 + SDTM v2.0 Expert — variable definitions, rule reasoning, cross-domain comparison, and terminology lookup"
操作: fill
验证: screenshot 读回 DOM
```

**🙋 用户 Fallback**: 同内容手填.

---

## Step 3: 粘贴 Custom Instructions 🤖

**🤖 Agent 指令**:
```
Step 3.1: Read /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/system_prompt.md
         → 预期 5884 chars (≤ 8000 budget, 73.55% 占用)
Step 3.2: DOM 定位 "Custom Instructions" 或 "Instructions" 多行输入框
Step 3.3: 清空后全文粘贴
Step 3.4: screenshot 验证首行 "# SDTM Expert — Gem Custom Instructions" + 末行 "<!-- char_count: 5884 / budget: 8000 -->" 都在
Step 3.5: 若 UI 报超限: STOP 记录阈值回报 (预期不触发)
```

**🙋 用户 Fallback**:
1. 文本编辑器打开 `current/system_prompt.md`, `Cmd+A` + `Cmd+C`
2. Custom Instructions 框 `Cmd+V`

---

## Step 4: 🚨 上传 4 个文件到 Knowledge 🙋 (Agent 大概率做不到)

**⚠️ 已知限制**: Gem Knowledge 的 "Add Knowledge" 或拖拽上传 → **原生 OS 文件选择器对话框**. chrome MCP / playwright **无法跨域到 OS 对话框**. 先前测试 agent 做不到.

**🤝 Agent 尝试** (仅 Mode A 且有 computer-use):
```
Step 4.1: DOM 点击 "Add Knowledge" 按钮 → 原生文件选择器
Step 4.2: 切 computer-use (若有)
         → request_access ["Chrome", "Finder" 或 OS 文件选择器 app]
Step 4.3: 导航到 4 个绝对路径, 按 01→02→03→04 顺序选中 + Open
         → /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/uploads/01_core_reference.md
         → ... 02_domain_specs.md
         → ... 03_domain_knowledge.md
         → ... 04_terminology_core.md
Step 4.4: 失败 STOP, 输出 "Agent 无法操作文件选择器, 用户请手动按 01→02→03→04 顺序上传后告知 agent 继续"
```

**🙋 用户 Fallback (默认路径)**:

**上传顺序 = PLAN §3.1 position_fit 策略**: 01 头部 / 04 尾部 recency / 02-03 前中段 (顺序影响上下文位置)

| # | 绝对路径 | tokens | target | deviation | sources | 用途 |
|---|---------|-------:|-------:|----------:|--------:|------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/uploads/01_core_reference.md` | 124,512 | 120,000 | +3.76% | 15 | ch01-10 + SDTM v2.0 Model + 导航 |
| 2 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/uploads/02_domain_specs.md` | 185,785 | 168,000 | +10.59% | 63 | 63 域 spec (字母序) |
| 3 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/uploads/03_domain_knowledge.md` | 275,318 | 225,000 | **+22.36%** | 126 | 63 域 assumptions + examples (**WARN Q3=接受**) |
| 4 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/uploads/04_terminology_core.md` | 299,303 | 200,000 | **+49.65%** | 5 | 高频 codelist 5 段 (**WARN**; V6 tail 3/3 PASS) |

**总计**: 884,918 tokens / 900K WARN 阈 / 1M HARD FAIL. 余 ~115K 响应 buffer.

**🚫 绝对不要上传** (agent + 用户都避开):
- `upload_manifest.md`
- `system_prompt.md` (已在 Instructions)
- `smoke_questions_draft.md`
- `phase3_*_reviewer.md`
- `failures/stage_phase3_attempt_1.md`
- `dev/` 目录任何文件
- 本 handoff 文件

---

## Step 5: Save Gem, 秒级就绪 🤖

**🤖 Agent 指令**:
```
Step 5.1: DOM 点击 "Save Gem" / "Create" 按钮
Step 5.2: 等 toast / 页面跳转到 Gem Preview (通常 <5 秒)
Step 5.3: Gemini 无 indexing — 不需轮询状态
Step 5.4: 若 UI 报错 "File too large / Token limit exceeded": STOP 记录 (不预期, 884K < 1M)
```

**🙋 用户 Fallback**: 点 Save, 秒级进 Preview.

---

## Step 6: Preview 对话框跑 5 题 Smoke 🤖

**🤖 Agent 指令 (总纲)**:
```
对 S1-S5 每一题:
  a. DOM fill Gem Preview 输入框 = 题面文本
  b. 点 Send / 回车
  c. 等回答流式结束
  d. 读 assistant message innerText
  e. 存为 "Qx answer"
按 S1→S2→S3→S4→S5 顺序; 每题一条消息不合并
5 题全完后 Step 7 填报告
```

**🙋 用户 Fallback**: Preview 面板 S1→S5 逐题, 复制回答.

---

### S1 — 精确查询 (PLAN §7.1 T1, 原题保留)

**问**: `AE 域 AESER 变量的 Controlled Terms (允许值) 是什么?`

**预期命中**: `02_domain_specs.md` (AE 段, offset ~18%)

**预期答**: Y / N 二值

**PASS 判据**:
- ✅ 答 Y / N 二值
- ✅ 引用 `<!-- source: --> knowledge_base/domains/AE/spec.md`
- ✅ **零臆造** (不编 Y/N/U/NA 四值)

---

### S2 — codelist 头部 Term (PLAN §7.1 T2 改编; C66742 不在本 Gem)

**问**: `04_terminology_core.md 最前面的 codelist (Laboratory Test Code, C65047) 头 5 条 Term (Code + Submission Value + Synonym) 是什么?`

**预期命中**: `04_terminology_core.md` line 10-30, offset ~0.2% (line) / ~0.04% (char), source `knowledge_base/terminology/core/lb_part2.md`

**预期答** (line 21-25 前 5 条):
| # | Code | Submission Value | Synonym |
|---|------|------------------|---------|
| 1 | `C100429` | `A1AGLP` | Alpha-1 Acid Glycoprotein |
| 2 | `C181404` | `A1ANTRPF` | Alpha-1 Antitrypsin, Functional |
| 3 | `C80167` | `A1ANTRYP` | Alpha-1 Antitrypsin; Serum Trypsin Inhibitor |
| 4 | `C186022` | `A1MCGEXR` | Alpha-1 Microglobulin Excretion Rate |
| 5 | `C100462` | `A1MCREAT` | Alpha-1 Microglobulin/Creatinine |

**PASS 判据**:
- ✅ 5 条 Term 准确 (Code + Submission Value 必中)
- ✅ 引用 `lb_part2.md`
- ✅ **无臆造**

---

### S3 — P12 末尾召回 T-tail-1 (**🚨 hard checkpoint**)

**问**: `04_terminology_core.md 最后一个 codelist (Category of Questionnaire, C100129) 最前面的 5 条 Term (Code + Submission Value + Synonym 列) 是什么?`

**预期命中**: line 6050-6068, offset 95.4% (line) / 87.7% (char) — **落 V6 tail 30% 内** (tail_start char 777,919)

**预期答** (line 6056-6060 前 5 条):
| # | Code | Submission Value | Synonym |
|---|------|------------------|---------|
| 1 | `C187516` | `ABC` | ABC01 |
| 2 | `C122370` | `ACQ` | ACQ01 |
| 3 | `C123658` | `ACT` | ACT01 |
| 4 | `C100762` | `ADAS-COG` | ADC |
| 5 | `C106888` | `ADCS-ADL MCI` | ADL03 |

**PASS 判据**:
- ✅ 5 条 Term 准确
- ✅ 引用 `qs_part1.md`
- ✅ **无 "未收录" fallback** (实际 inline 了)
- ✅ **无臆造**

**FAIL 后果** (🚨 hard gate):
- 🔴 S3 FAIL → recency bias 失效 → **P12 R1 触发**, 停机, 重合并 04 或拆 04

---

### S4 — P12 Lost-in-Middle T-tail-2 (**🚨 hard checkpoint**)

**问**: `04_terminology_core.md 中段的 Laboratory Test Name codelist (C67154) 最前面的 3 条 Term (Code + Submission Value + Synonym 列) 是什么?`

**预期命中**: line 2564-2575, offset 40.4% (line) / 34.0% (char) — **落 40-60% middle 危险区**

**预期答** (line 2570-2572 前 3 条):
| # | Code | Submission Value | Synonym |
|---|------|------------------|---------|
| 1 | `C179752` | `1,25-Dihydroxyvitamin D2` | 1,25-Dihydroxycalciferol; 1,25-Dihydroxyergocalciferol; 1,25-Dihydroxyvitamin D2; Ercalcitriol |
| 2 | `C179754` | `1,25-Dihydroxyvitamin D3` | 1,25-Dihydroxycholecalciferol; 1,25-Dihydroxyvitamin D; 1,25-Dihydroxyvitamin D3; Calcitriol |
| 3 | `C179753` | `1,25-DihydroxyvitD2+1,25-DihydroxyvitD3` | ... |

**PASS 判据**:
- ✅ 3 条 Term 准确 (Code + Submission Value 必中)
- ✅ 引用 `lb_part3.md`
- ✅ **无臆造**

**S3 + S4 对比矩阵** (P12 hard gate):
| S3 | S4 | 判定 | 行动 |
|:---:|:---:|---|---|
| PASS | PASS | ✅ P12 全绿 | 放心进 Node 4 |
| PASS | FAIL | 🟡 典型 Lost-in-Middle | 记录不阻塞, query anchor 缓解 |
| FAIL | PASS | 🔴 recency 失效 | **P12 R1 停机拆 04** |
| FAIL | FAIL | 🔴🔴 双 FAIL | **P12 R2 强制停机拆 04** |

---

### S5 — 边界诚实 (PLAN §7.4 T9; 零臆造硬门槛)

**问**: `AERELN codelist 的所有 Synonyms 是什么?`

**预期命中**: **04 不含 AERELN** (grep 0 匹配); 04 仅 inline 5 段 (lb_part2 / lb_part3 / oncology_part1 / interventions / qs_part1)

**预期合规响应**:
> "`AERELN` codelist 未收录于本 Gem `04_terminology_core.md`. 本 Gem 04 仅 inline 5 段高频 codelist: `lb_part2` / `lb_part3` / `oncology_part1` / `interventions` / `qs_part1`. 完整 Term + Synonyms 请查源 `knowledge_base/terminology/core/*.md` 或 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/"

**PASS 判据**:
- ✅ 声明未收录
- ✅ 给外部入口 (NCI EVS / 源路径)
- ❌ **零臆造 Synonym** (1 条假 Synonym = FAIL)

---

## Step 7: 填写报告模板 🤖 + 🙋

**🤖 Agent 指令**: 用 Write 写到:
```
/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/smoke_results.md
```

**🙋 用户 Fallback**: 按模板填空, 粘回 Claude Code session.

```markdown
# Gemini Gems — Phase 3 Node 3b Smoke 报告

> 执行日期: 2026-04-XX HH:MM
> 执行者: Agent (chrome MCP / computer-use) / 用户
> Gem Name: SDTM Expert

## Step 2-5 配置确认
- [x] Name: SDTM Expert
- [x] Description: <140 chars>
- [x] Custom Instructions: system_prompt.md 全文粘贴 (5,884 chars)
- [x] Knowledge: 4 文件按 01→02→03→04 顺序上传 (884,918 tokens)
- [x] Save Gem: 成功, 秒级就绪 (无 indexing)
- [ ] UI 警告: 无 / 有 (<内容>)

## Smoke 5 题结果明细

### S1. AE.AESER Controlled Terms
- **答**: <完整粘贴 Gemini 回答>
- **PASS/FAIL**: PASS / FAIL
- **是否 Y/N 二值**: 是 / 否 (编 U/NA → FAIL)
- **源路径引用**: 是 (<AE/spec.md>) / 否
- **是否臆造**: 否 / 是
- **备注**: ...

### S2. C65047 Lab Test Code 头 5 条 (头部)
- **答**: ...
- **PASS/FAIL**: ...
- **5 条 Code 准确数**: N/5
- **Submission Value 准确数**: N/5
- **源路径引用**: 是 (<lb_part2.md>) / 否
- **是否臆造**: 否 / 是
- **备注**: ...

### S3. ⚠️ P12 hard gate — C100129 头 5 条 (末尾)
- **答**: ...
- **PASS/FAIL**: PASS / **FAIL 🚨**
- **5 条 Code 准确数**: N/5
- **是否答 "未收录" fallback**: 否 (PASS 必需) / 是 → FAIL
- **源路径引用**: 是 (<qs_part1.md>) / 否
- **是否臆造**: 否 / 是
- **末尾召回语义**: ✅ recency 成功 / 🔴 失效

### S4. ⚠️ P12 hard gate — C67154 头 3 条 (中段)
- **答**: ...
- **PASS/FAIL**: PASS / FAIL
- **3 条 Code 准确数**: N/3
- **源路径引用**: 是 (<lb_part3.md>) / 否
- **是否臆造**: 否 / 是
- **中段召回语义**: ✅ Lost-in-Middle 未发生 / 🟡 典型中段遗漏

### S5. AERELN Synonyms (零臆造硬门槛)
- **答**: ...
- **PASS/FAIL**: ...
- **是否声明 "本 Gem 未收录"**: 是 / 否 → FAIL
- **是否给外部入口**: 是 (NCI EVS / 源路径) / 否
- **是否臆造任意 Synonym**: 否 (PASS 必需) / 是 → FAIL
- **备注**: ...

## P12 hard gate 矩阵判定 (S3 + S4)
- S3: PASS / FAIL
- S4: PASS / FAIL
- **矩阵判定**: 全绿 / Lost-in-Middle (S3✓ S4✗) / recency 失效 (S3✗ S4✓) / 双 FAIL (P12 R2)

## 汇总
- **PASS 比**: N/5 (目标 ≥ 4/5)
- **FAIL 题**: [列 S-id + 原因]
- **P12 状态**: 全绿 / 触发 R1 / 触发 R2

## 关键观察 (2-4 句)
- <例: "S3 PASS 5/5, 末尾 recency 成功, 印证 Gemini 1M 窗口 @884K 末尾 recall >99%">
- <例: "S4 PASS 3/3, Lost-in-Middle 未发生, 但响应比 S3 慢 ~3 秒">
- <例: "S5 声明 AERELN 未收录 + 给 NCI EVS, 零臆造 PASS">

## 异常/警告
- <或 "无异常">

## 浏览器截图 (Agent 贴 screenshot 路径 / 用户可选贴)
- <Knowledge 列表 / S3 回答 / Save token 计数>

## 执行元数据 (agent 填, 用户可留空)
- 浏览器工具链: chrome-MCP / playwright / computer-use / 用户手动
- Step 4 上传模式: agent fallback 用户 / agent 成功 / 用户全程手动
- 总用时: N 分钟
```

---

## Step 8: 交回主 session 🙋

粘完报告 (或 agent Write 后) 通知主 session.

**不要自己判 overall PASS/FAIL** — 主 session 会:
1. 派 Rule D smoke reviewer (不同 subagent_type, 第 11 种) 独立复核
2. 归档 `dev/evidence/smoke_results.md`; 若 P12 触发归 `dev/evidence/failures/stage_phase3_node3b_attempt_N.md`
3. 按 P12 矩阵决策
4. commit C3b

---

## 决策矩阵 (供主控参考)

| 报告 | 主控决策 |
|---------|---------|
| ≥ 4/5 PASS + S3 PASS + S4 PASS | 派 Rule D reviewer + commit C3b + 进 Node 4 / 跳 Node 5 (Gemini 单批终态可跳 Node 4) |
| ≥ 4/5 PASS + S3 PASS + S4 FAIL | Lost-in-Middle 记录, 不阻塞; Node 5 A/B 加 query anchor |
| < 4/5 PASS 但 S3/S4 PASS | 归因 + attempt_2 |
| **S3 FAIL (P12 R1)** | **停机**, 重合并 04 (脚本 budget 90K→100K) 或拆 04 |
| **S3 + S4 都 FAIL (P12 R2)** | **强制停机拆 04** |
| S5 FAIL (臆造 Synonym) | **关键 FAIL**, Instructions §边界补强, 必 attempt_2 |
| UI 报 token 超限 | 降 04 size 或拆 04a/04b |

---

## 不要做 (agent + 用户都适用)

- **不要自行登录** gemini.google.com (agent 见登录墙立停)
- **不要自行判 overall PASS/FAIL** — 留给主 session + reviewer
- **不要编造 Gemini 回答** — 如实粘贴 UI 看到的
- **不要修改** `current/uploads/` 任何 .md
- **不要跳题** — 5 题必全跑 (S3/S4 P12 hard gate 核心)
- **不要上传 meta** (upload_manifest / smoke_questions_draft / dev/* / failures/* / 本 handoff)
- **不要延长 Instructions** — 只粘 system_prompt.md 原文
- **不要尝试"公开发布"给陌生用户** — Gemini 的"公开"= 链接分享给同事, 非 Store 广播, 默认 Private
- **不要混淆 S3 与 S5** — S3 codelist **在 Gem 内** (答具体 Term), S5 codelist **不在 Gem 内** (声明未收录); 答反即 FAIL
- **(agent)** 不要在原生文件选择器强推, 失败即停提示用户

---

## 完成信号

报告送达主 session 后:
1. 派 Rule D smoke reviewer (第 11 种 subagent_type)
2. 归档 evidence
3. 按 P12 矩阵进 Node 4 / 重合并 / 拆 04
4. commit C3b bundled (双平台)

**Agent 准备好从 Step 1 开始; 用户准备好跟 agent 协作或自己从 Step 1 手动开始.**

---

*来源: PLAN §7.1/§7.3/§7.4 + `smoke_questions_draft.md` (writer 实读 04 选题过程) + `upload_manifest.md` V6 tail markers 独立段 + Phase 3 Node 3a reviewer 产物 (M1 R1 坐标系 + M2 R2 tail markers) + claude_projects/dev/checkpoints/CHECKPOINT_V2.*_HANDOFF.md 结构*
