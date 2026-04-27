# SDTM AI 知识库 — 用户手册 v1.0

## 1. 这是什么 (项目背景)

SDTM (Study Data Tabulation Model) 是 CDISC 临床试验数据制表标准, 含 63 个域 + 上千变量 + 大量 CT (Controlled Terminology). 日常查一个变量 Core 属性或 C-code, 翻 SDTMIG v3.4 PDF + NCI EVS Browser 要十几分钟. 本项目把 CDISC SDTMIG v3.4 + v2.0 model + CDISC CT 整理成 295 个 Markdown 源, 部署到 4 个 AI 平台 (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM), 让同事**自然语言提问, 1 分钟拿到带 spec 引用的答案**.

## 2. 工作成果概览 (技术亮点)

4 平台均已 LIVE, 各跑过 17 题 smoke v4 评测 (含 3 道 anti-hallucination probe 反虚构探针):

| 平台 | smoke v4 | 版本 | 强项 |
|---|:---:|:---:|---|
| Claude Projects | 17/17 (100%) | v2.6 | 精确变量 + 多步推理 |
| ChatGPT GPTs | 16.5/17 (97%) | v2.2 LIVE | 全量 + 可团队/Store 共享 |
| Gemini Gems | 16/17 (94%) | v7.1 LIVE | 长上下文 + 大范围探索 |
| NotebookLM | 15/17 (88%) | Custom mode | in-KB-only 反虚构 |

亮点: v3.4 新域 (GF / CP / BE / BS) + Timing + CT Extensible + SUPPQUAL scope + 跨域死亡日级对齐 + 3 道 AHP (LBCLINSIG / Trial-Level SAE Aggregate / PF 已废域); 全程 Rule A-D 4 条质量规则 + 累计 28 个独立 reviewer 验证. 信源: `./CHANGELOG.md` + `../../SMOKE_V4.md` §3.

## 3. 我该用哪个平台? (决策树)

| 想做的事 | 推荐平台 | 理由 |
|---|---|---|
| 精确变量 + 多步推理 (Core + C-code + 跨变量) | **Claude Projects** | 1.29M tokens 全量, smoke 满分 |
| 团队/部门内分享, 或发布 GPT Store | **ChatGPT GPTs** | 组织内分享免审核, Store 走 review |
| 长上下文 + 一次性大范围探索 / 跨域模式 | **Gemini Gems** | 1M 窗口, 4 文件深度合并 |
| 100% 反虚构 (拒答优于编造) + 强 citation | **NotebookLM** | in-KB-only, 不在 42 sources 内宁可 PUNT |

简版: 不知道选什么 → Claude Projects. 拉同事一起用 → ChatGPT GPTs. 担心幻觉 → NotebookLM. 详细对比见 `../README.md` "四平台分工" 表.

## 4. 4 平台访问入口

### 4.1 Claude Projects (推荐入门)

- **访问**: 等 Daisy 加 organization 邀请, 邮件链接加入.
- **URL**: claude.ai → Projects → "SDTM Knowledge Base" (Daisy 单发具体 URL).
- **套餐**: Claude Pro / Team / Enterprise.
- **适合**: 精确变量 Core+CT 绑定 / 跨变量推理 (PCTPT 五件套) / 错前提纠错 (SUPPTS).
- **不适合**: 实时联网 FDA/Pinnacle 21 (手动核 cdisc.org); 超大批量域对比.

### 4.2 ChatGPT GPTs

- **访问**: Daisy 分享 Custom GPT 到 organization, "添加到我的 GPTs".
- **URL**: chatgpt.com → 顶部下拉 → "SDTM Knowledge Base".
- **套餐**: ChatGPT Plus / Team / Enterprise (Free 不可).
- **适合**: 全量域查询 / 团队共享 / 想发布 GPT Store 走 OpenAI review.
- **不适合**: 多步推理略弱于 Claude; Free 账号找不到入口.

### 4.3 Gemini Gems

- **访问**: Daisy 分享 (Workspace) 或自部署 (个人).
- **URL**: gemini.google.com → Gems → "SDTM Knowledge Base".
- **套餐**: Gemini Advanced 个人 / Google Workspace.
- **适合**: 一次性塞大量上下文 / 跨域模式比对 / 长会话.
- **不适合**: 个人账号不能直接团队共享 (要 Workspace).

### 4.4 NotebookLM

- **访问**: Daisy 邀请加入 notebook, 或自建 (50-source cap).
- **URL**: notebooklm.google.com → "SDTM Knowledge Base".
- **套餐**: NotebookLM Pro / Google Workspace.
- **适合**: 强反虚构 (审计/合规) / inline citation 反查 / 拒答优于编造.
- **不适合**: 不在 42 source 内的题 (实时 Pinnacle 21 / breaking news) 它会拒答 — 设计如此, 非 bug.

## 5. 5 分钟快速试用 (3 题热身)

打开常用平台 (建议先 Claude Projects), 依次问 3 题, 答案对照 `./DEMO_QUESTIONS.md` Expected:

1. **D0 (热身)**: "AESER 是 SDTMIG v3.4 哪个域什么变量? Core? 绑哪个 CT C-code?" 预期: AE 域 / Serious Event / Exp / C66742 NY {Y/N/U/NA}.
2. **D1 (新域)**: 复制 DEMO_QUESTIONS.md D1 题面 (EGFR / Exon 19 / dbSNP). 预期 Domain=GF, 答出 GFGENSR / GFPVRID / GFGENREF / GFINHERT.
3. **D5 (前提纠错)**: "SUPPTS 是 SDTM 标准里什么? QORIG 必填吗?" 预期: 主动识破 "SUPPTS 不在 SDTMIG v3.4" → 走 TSVAL1-TSVALn = PASS+.

判 PASS/FAIL: 核心事实 (域 / 变量 / Core / C-code) 都中 = PASS; 主动识破错前提 = PASS+; 沿错前提编 = FAIL.

## 6. 完整 demo 包 (10 题)

10 题完整版在 `./DEMO_QUESTIONS.md` (三语题面 + 英文判据). 5 分钟入门 = D0/D1/D5; 30 分钟全跑 = D0→D9 (含 3 道 AHP D6 LBCLINSIG / D7 SAE Aggregate / D8 PF 已废 + 跨域终极 D9 AE/MH/CE + DS 死亡日级对齐). 跑完对照 §2 baseline (17/17 / 16.5/17 / 16/17 / 15/17) 看实例是否到位.

## 7. 已知限制 (高频问题)

完整版见 `./KNOWN_LIMITATIONS.en.md`, 中文摘要:

- **L1 — QS codelist 不全**: 296 个长尾 questionnaire codelist (PROMIS/EORTC) 因容量约束未全展开 (Claude ~55.8%), 其余落 NCI EVS Browser 链接.
- **L2 — 巨型 codelist 走 stub**: LBTESTCD (2536 term) 等 6 表只存 stub + 指针, 不会编 term.
- **L3 — 实时联网**: NotebookLM 严格 in-KB-only, breaking news / 最新 Pinnacle 21 不知道 (PUNT). 其他 3 平台可联网需手动开启.
- **Claude**: 容量 77% 接近 Pro 软上限, 加新文件需先降级低优先.
- **ChatGPT**: 20-file 硬上限 (当前 9), 长尾 chunk 表格中段可能 miss.
- **Gemini**: 个人账号不能直接团队共享 (要 Workspace); v7.1 system prompt 必须完整粘贴.
- **NotebookLM**: 50-source cap (当前 42); Q9/Q11/Q12 三题主动 PUNT 是**正确安全行为**.

## 8. 反馈渠道

发现错误 / 幻觉 / 答非所问: (1) 截图 + 留底完整问题原文 + AI 回答; (2) 附平台 + 版本号 (例 "ChatGPT GPT v2.2 LIVE 2026-04-24") + 期望答案 (引 SDTMIG v3.4 章节号或 CDISC CT C-code); (3) 邮件 Daisy / 公司 issue tracker / 部门群 @Daisy. 汇总到 `./CHANGELOG.md` 走下个 minor release.

## 9. 后续路径

短期 (v1.0 维护): 收反馈修 SDTM 错点, 季度 v1.x minor. 中期 (Phase 7 自建 RAG): 摆脱 4 平台容量约束, 295 文件全量 + QS codelist 全展开. 长期: 跟 SDTMIG v3.5+ 同步 + ADaM / Define-XML 扩展.

---
*v1.0 — 2026-04-27 — 维护者: Daisy*
