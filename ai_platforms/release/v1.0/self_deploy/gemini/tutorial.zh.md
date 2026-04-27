# Gemini Gem 制作教程 — SDTM 知识库发布版

> 从零开始搭建一个能查 CDISC SDTM 标准 (63 域 + chapters + 业务弹药包) 的 Custom Gem.
> 读完本教程你会得到: 一个可用的 Gemini Gem, 能精确回答 SDTM 变量定义 / 业务场景映射 / 跨域关联, 且能识破常见虚构前提 (3 道反虚构锚 / anti-hallucination guard).
> 总耗时: **20-40 分钟** (Gemini indexing 比 ChatGPT 快得多).

---

## 0. 前置要求

- [ ] **Google AI Pro 订阅** (个人版即可) — 免费 Gemini 无 Custom Gem 编辑权
- [ ] 网页访问 [gemini.google.com](https://gemini.google.com)
- [ ] **本地 clone 本仓库**: 需要读 `./` 下 `system_prompt.md` (约 29.9KB) 和 `uploads/` 下 4 个 .md 文件

**关于套餐与团队共享**:
- 个人 Google AI Pro 订阅可建 Gem, **不支持团队共享** (Gem 与个人账号绑定)
- Workspace 套餐有 Gem 共享能力, 但语义有别于 personal — 同事**各自部署**最稳妥
- Gemini 没有"GPT Store" 式公开画廊, 只能 link share

---

## 1. 新建 Custom Gem

1. 登录 [gemini.google.com](https://gemini.google.com) (用 Pro 订阅 Google 账号)
2. 左侧导航 → "**Gems**" → 右上 "**+ New Gem**" 或 "**Create a new Gem**"
3. **Name**: 建议 `SDTM Expert` 或 `CDISC SDTM Knowledge`
4. **Description**: `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, business scenario mapping, cross-domain.`

---

## 2. 配置 Instructions (system_prompt.md)

1. 在 Gem Edit 界面找 "**Instructions**" 或 "**Custom Instructions**" 框
2. **完整复制** `./system_prompt.md` (v7.1 LIVE, 29,919 chars) 粘贴
3. **强调**: Gemini 接受**远超 8K 字符**的 instructions (实测 30K 接受). 不要因为习惯 ChatGPT 8K 上限而手动截断, 截断会丢 anti-hallucination 锚

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

---

## 4. 等 Indexing

Gemini Gem **无 RAG / 无 chunk 检索** — 上传后**秒级就绪**, 全文始终在上下文. 一般 1-3 分钟内文件状态变 "Ready" 即可 chat.

ChatGPT 是 RAG 召回, Gemini 是全注入 — 两者底层架构不同, 不要套用 ChatGPT 的 indexing 等待经验.

---

## 5. Smoke Test (3 题, ~5 分钟)

**Preview** 一题一新 chat:

| # | 提问 | 期望要点 | 验证点 |
|---|------|---------|------|
| T1 | `AESER 的 Core 属性是 Req 还是 Exp?` | Core = **Exp** (不是 Req) | CO-1 高频易错锚 |
| T2 | `LB / MB / IS 三个域怎么区分? 微生物培养结果归哪个?` | LB = 临床实验室 (化学/血/尿); MB = 微生物 (培养/药敏); IS = 免疫 (抗体/疫苗) | 域边界识别 |
| T3 | `PF 域 (Pharmacogenomics Findings) 的变量清单?` (PF deprecated) | Gem 应**识破**: PF 在 v3.4 已废弃, 当前用 GF (Genomics Findings) / BE (Biospecimen Events) / BS (Biospecimen Findings) + RELSPEC | AHP3 deprecated 反虚构 (R1→R2 升级核心闭合点) |

**3/3 PASS** = 部署成功; 任一 FAIL → 看 §7 排错.

---

## 6. 完整回归 (10 题, ~30 分钟, 可选)

打开 [`../DEMO_QUESTIONS.md`](../DEMO_QUESTIONS.md), 逐题提问 D0-D9 (10 题 demo). **一题一新 chat**. 项目内部完整 17 题 baseline 16/17 (94.1%), 3 道反虚构题全识破; 你部署的 Gem 跑这 10 题 ≥ 8/10 = 等同基线.

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
| Knowledge 文件状态卡 "Processing" | 文件超 5MB / 编码异常 | 检查 02 文件 (~919KB 最大), 确认 UTF-8 LF 无 BOM |

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

**Gemini Gem 不支持团队共享** (与 ChatGPT GPT 不同):
- Gem 与个人 Google 账号绑定, 不能 invite 同事到同一 Gem
- 同事各自照本教程部署, 各自维护一份
- Workspace 套餐有 Gem 共享能力, 但实际语义复杂, 推荐**各自部署最稳妥**
- 不存在"Gemini Gem Store"公开发布路径, 仅 link share

---

## 10. 后续路径

- 本发布版已是**完整终态**, 短期内不会再扩容
- 长尾 terminology + Studio 三件套 (Audio Overview / Mind Map / Study Guide) 归后续 Phase 7 / NotebookLM 互补
- 知识库内容如有错漏, 反馈到项目 issue tracker

---

## 附: 验证清单

- [ ] Google AI Pro 订阅已启用
- [ ] Custom Gem 已建, 命名清晰
- [ ] Instructions 粘贴了完整 system_prompt.md (v7.1 LIVE, 29,919 chars)
- [ ] Knowledge 面板显示 4 个文件全 Ready
- [ ] T1 AESER Core=Exp PASS
- [ ] T2 LB/MB/IS 域边界 PASS
- [ ] T3 PF deprecated 反虚构识破 PASS

全部 ☑ = 部署成功, 可以开始日常使用.

---

*v1.0 — 2026-04-27 — 公司发布版*
