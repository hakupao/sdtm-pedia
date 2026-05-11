# Gemini Gem 制作教程 — SDTM 知识库发布版

> 从零开始搭建一个能查 CDISC SDTM 标准 (63 域 + chapters + 业务弹药包) 的 Custom Gem.
> 读完本教程你会得到: 一个可用的 Gemini Gem, 能精确回答 SDTM 变量定义 / 业务场景映射 / 跨域关联, 且能识破常见虚构前提 (3 道反虚构锚 / anti-hallucination guard).
> 总耗时: **20-40 分钟** (Gemini indexing 比 ChatGPT 快得多).

---

## 0. 前置要求

- [ ] **Google 账号** (13 岁以上)。**Gem 的创建本身自 2025 年起 Free 账号即可使用**。但 **Knowledge 文件上传、共享给他人、大容量 instructions** 需要 **Google AI Plus / Pro / Ultra / Workspace 套餐之一**。本教程全量使用 Knowledge, 推荐 **Pro 及以上**。

  | 套餐 | 创建 Gem | Knowledge | 共享 |
  |------|----------|-----------|------|
  | Free | 可 | 受限 | 不可 |
  | Google AI Plus / Pro / Ultra | 可 | 全功能 | 可 |
  | Google Workspace (Business Standard 及以上) | 可 | 全功能 (管理员管控) | 可 |

- [ ] 网页访问 [gemini.google.com](https://gemini.google.com)
- [ ] **本地 clone 本仓库**: 需要读 `./` 下 `system_prompt.md` (约 29.9KB) 和 `uploads/` 下 4 个 .md 文件

**关于套餐与共享**:
- 个人 Google AI Pro / Ultra 可创建并共享 Gem. **2025 年起 Gem 共享功能开放**, 与 Google Drive 同款 UI 设置 Viewer / Editor 权限 (见 §9).

---

## 1. 新建 Custom Gem

1. 登录 [gemini.google.com](https://gemini.google.com)
2. 侧边栏 → "**Gems**" → "**Explore Gems**" → "**New Gem**" 按钮 (无 + 号)
3. **Name**: 建议 `SDTM Expert` 或 `CDISC SDTM Knowledge`
4. **Description**: `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, business scenario mapping, cross-domain.`

---

## 2. 配置 Instructions (system_prompt.md)

1. 在 Gem Edit 界面找 "**Instructions**" 或 "**Custom Instructions**" 框
2. **完整复制** `./system_prompt.md` (v7.1 LIVE, 29,919 chars) 粘贴
3. **强调**: Gemini Gems 接受较长 Instructions. **官方未明确说明字符上限**, 本 v7.1 LIVE 的 29,919 chars 已实测可用 (2026-04 时点). **有报告指出过长的 Instructions 可能削弱 Knowledge 文件召回**, 建议保持必要最小长度. 不要因为习惯 ChatGPT 8K 上限而手动截断, 截断会丢 anti-hallucination 锚

**v7.1 LIVE 关键 patch (粘贴后必须保留)**:
- **§CO-1d SUPPQUAL Core + scope 硬锚**: QORIG Core=Req / QEVAL Core=Exp / CT C78735; SUPPQUAL 不适用 Trial Design (TS/TA/TE/TI/TV)
- **§CO-1c ARM/ARMCD/ARMNRS** 5 值含 NOT APPLICABLE Extensible=Yes
- **§CO-5 AHP-V1/V2/V3** 三档 anti-hallucination guard (变量级 / 跨域级 / deprecated 级)

---

## 3. 上传 4 个知识库文件

1. Gem Edit → "**Knowledge**" 面板 → "**Upload files**" 或拖拽
2. 选 `./uploads/` 下**全部 4 个 .md 文件**, 顺序:
   - `01_navigation_and_quick_reference.md` (~124K tokens)
   - `02_domains_spec_and_assumptions.md` (~240K tokens, 63 域 spec + assumptions 域内交错)
   - `03_domains_examples.md` (~220K tokens, 63 域 examples)
   - `04_business_scenarios_and_cross_domain.md` (~30K tokens, 26 业务场景 + FAQ)
3. **不要重命名 / 不要拆合并**

Gemini Knowledge **10 文件硬限**, 当前 4/10 (6 文件 headroom). 总 ~616K tokens 占 1M 上下文窗口约 62%, 留 ~38% 响应缓冲.

**补充**: **单文件一般上限 100 MB** (视频为 2 GB). **也可直接引用 Google Drive 文件** (始终拉取最新版, 文件更新后无需重新上传替换).

---

## 4. 等 Indexing (RAG 处理)

**2026 年现在, Gemini Gems 采用 RAG (Retrieval-Augmented Generation, 语义分块检索)**. 上传后 Knowledge 文件会被分块向量化, 每次查询时**仅动态注入语义相似度高的块**. Instructions 每轮全量注入, Knowledge 文件仅在相似度命中时才被调用.

一般 1-3 分钟内文件状态变 "Ready" 即可 chat.

**注意**: RAG 管道稳定性偶有波动 (2026/1 曾有文件引用退行 bug 报告). 如未出现 citation / 期望内容未命中, 请在新 chat 重试或参见 §7 排错.

---

## 5. Smoke Test (3 题, ~5 分钟)

**Preview** 一题一新 chat:

| # | 提问 | 期望要点 | 验证点 |
|---|------|---------|------|
| T1 | `AESER 的 Core 属性是 Req 还是 Exp?` | Core = **Exp** (不是 Req) | CO-1 高频易错锚 |
| T2 | `LB / MB / IS 三个域怎么区分? 微生物培养结果归哪个?` | LB = 临床实验室 (化学/血/尿); MB = 微生物 (培养/药敏); IS = 免疫 (抗体/疫苗) | 域边界识别 |
| T3 | `PF 域 (Pharmacogenomics Findings) 的变量清单?` (PF deprecated) | Gem 应**识破**: PF 在 v3.4 已废弃, 当前用 GF (Genomics Findings) / BE (Biospecimen Events) / BS (Biospecimen Findings) + RELSPEC | AHP3 deprecated 反虚构 (R1→R2 升级核心闭合点) |

**3/3 PASS** = 部署成功; 任一 FAIL → 看 §7 排错.

**为确认 Knowledge 文件已被 RAG 命中, 期望 Gem 在回答中包含 source citation.**

---

## 6. 完整回归 (10 题, ~30 分钟, 可选)

打开 [`../../DEMO_QUESTIONS.zh.md`](../../DEMO_QUESTIONS.zh.md), 逐题提问 D0-D9 (10 题 demo). **一题一新 chat**. 项目内部完整 17 题 baseline 16/17 (94.1%), 3 道反虚构题全识破; 你部署的 Gem 跑这 10 题 >= 8/10 = 等同基线.

---

## 7. 排错手册 (Gemini-specific)

| 症状 | 可能原因 | 处理 |
|------|---------|------|
| 答 ARM 时混 ARMCD / ARMNRS | §CO-1c 锚失效 | 重检 system_prompt §CO-1c (ARM 5 值列全 + Extensible=Yes) |
| SUPPQUAL Core 答错 (QORIG=Exp / QEVAL=Req) | §CO-1d v7.1 锚未生效 | 重贴 system_prompt 全文, 确认 §CO-1d 段在 |
| 答 PF / PGx domain 变量 (deprecated 虚构) | §CO-5 AHP-V3 锚失效 | 重检 §CO-5 + §回答规范 ⑧ Deprecated concept 段 |
| 答 LBCLINSIG (变量虚构) | §CO-5 AHP-V1 锚失效 | 重检 §CO-5 双核工作流 step 0 + AHP-V1 识破模板 |
| First-token 慢 (>10 秒) | 冷启动正常现象 | 后续 query 会快; 持续 >30 秒查 Google AI 状态 |
| 答案没 citation / 源路径 | §CO-3 锚失效 | 重贴 system_prompt §三条硬约束 + §回答规范 |
| Knowledge 文件状态长期 "Processing" | 文件远大于预期 (本发布最大 ~919 KB) / 编码异常 | 检查 02 文件 (~919 KB, 最大), 确认 UTF-8 LF, 无 BOM |

---

## 8. 升级 / 降级路径

**升级 (扩 KB)**:
- 当前 4/10 文件, 6 文件 headroom
- terminology 长尾 (questionnaires) 可加 05 文件; SDTMIG v3.5 新域可加 06 文件
- **不需降级**: 当前总 token 占 1M 窗口 62%, 38% 缓冲充裕

**降级 (容量警告, 一般用不到)**:
1. 先删 `04_business_scenarios_and_cross_domain.md` (业务弹药, 但 R2 升级关键)
2. 再删 `03_domains_examples.md` (examples)

底线保留: `01 + 02` (导航 + spec/assumptions) = 365K tokens.

---

## 9. 团队协作

**Gemini Gem 自 2025 年起支持共享** (原"不支持团队共享"限制已解除).

- **共享方法**: 在 Gem Manager 找到目标 Gem, 点击旁边的 "**Share**" → 与 Google Drive 同款 UI 选择 Viewer / Editor 权限 → 填邮箱地址邀请
- **Workspace 管理员管控**: Admin Console → Generative AI → Gemini app → Gem sharing 可开关
- **接收方行为**: 被共享的 Gem 不会自动出现在接收方 Gem Manager 中. 接收方需先打开并使用, 才能添加到 "My Gems"
- **注意**: Free 账号无法使用共享功能. 发送方与接收方均需 Pro / Ultra / Workspace
- **公开画廊**: 不存在类似 GPT Store 的公开市场. Google 提供的 "premade Gems" 显示在 Gems Manager 内, 但用户无法将 Gem 发布到公开商店

---

## 10. 后续路径

- 本发布版已是**完整终态**, 短期内不会再扩容
- 长尾 terminology + Studio 功能 (NotebookLM 的 Audio Overviews / Video Overviews / Mind Maps / Reports) 归后续 Phase 7 / NotebookLM 互补
- 知识库内容如有错漏, 反馈到项目 issue tracker

---

## 附: 验证清单

- [ ] Google AI Pro 及以上套餐已启用
- [ ] Custom Gem 已建, 命名清晰
- [ ] Instructions 粘贴了完整 system_prompt.md (v7.1 LIVE, 29,919 chars)
- [ ] Knowledge 面板显示 4 个文件全 Ready
- [ ] T1 AESER Core=Exp PASS
- [ ] T2 LB/MB/IS 域边界 PASS
- [ ] T3 PF deprecated 反虚构识破 PASS

全部 ☑ = 部署成功, 可以开始日常使用.

---

*v1.1 — 2026-05-11 — UI 术语同步至 2026 年官方规格 (RAG 采用 / Gem 共享开放 / Free 账号可创建)*
