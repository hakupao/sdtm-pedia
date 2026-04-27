# 术语速查 — SDTM AI 知识库

> 1 页 1 览, 不熟悉的术语回这查. 按 SDTM 行业 / AI 平台 / 项目内部 三大类分.

## 一、SDTM 行业术语

| 术语 | 中文 | 解释 |
|---|---|---|
| **SDTM** | 临床试验数据制表模型 | Study Data Tabulation Model. CDISC 标准之一, 规定临床试验数据如何组织成表 (域 / 变量 / codelist). |
| **SDTMIG v3.4** | SDTM 实施指南 v3.4 | SDTM Implementation Guide. 把 SDTM 模型具体写成"哪个域有哪些变量, 各自什么 Core 属性". 本项目用的 v3.4 是 2021 版主流. |
| **CDISC** | 临床数据交换标准协会 | Clinical Data Interchange Standards Consortium. 监管 SDTM/ADaM/CDASH 等一系列标准, FDA 提交必经. |
| **Domain (域)** | 域 | SDTM 把临床数据按主题分成 63 个域, 例 AE (Adverse Events) / DM (Demographics) / LB (Lab) / EX (Exposure). 每个域是一张表. |
| **Variable (变量)** | 变量 | 域内一列, 例 AE 域有 AESER (Serious Event 标志位) / AETERM (报告原文) / AEDECOD (MedDRA decode) 等. |
| **Core 属性** | Req / Exp / Perm | 每个变量的"必填等级": **Req** (Required, 必填) / **Exp** (Expected, 应有, 但缺失需备注) / **Perm** (Permissible, 可选). 例 USUBJID Core=Req, AESER Core=Exp, AESEV Core=Perm. |
| **CT (Controlled Terminology)** | 受控术语 | CDISC 规定的"该变量允许填什么值"的清单. 例 AESER 只能填 Y/N/U/NA 4 个值, 不能写 "yes"/"是". |
| **C-code** | NCI 术语编号 | 每个 codelist 有一个 NCI EVS C-code 唯一标识. 例 NY codelist = C66742, AESEV codelist = C66769. 这些 C-code 在 SDTMIG / NCI EVS Browser / Pinnacle 21 等都通用. |
| **Extensible** | 可扩展 | 标记 codelist 能否加 sponsor 自定义值. **Extensible=Yes** (例 LBNRIND 4 标准值 + sponsor 可加新档) vs **Non-Extensible** (例 NY 严格 Y/N/U/NA, 不可加). |
| **Codelist** | 编码表 | 一个具名值集合. 例 LBNRIND codelist 有 4 标准值 {HIGH/LOW/NORMAL/ABNORMAL}. 同 "CT" 用法一致. |
| **SUPPQUAL / SUPP--** | 补充域 | 当 SDTM 标准变量装不下时, 用 SUPPQUAL 域 + IDVAR/IDVARVAL/QNAM/QVAL 4 件套补. 每个标准域都有对应 SUPP-- (例 AE↔SUPPAE / LB↔SUPPLB). |
| **NSV** | 非标准变量 | Non-Standard Variable, 即只能进 SUPPQUAL 不能进主域的变量. SUPP-- 是装 NSV 的容器. |
| **RELREC / RELSPEC / RELSUB** | 关系域三件套 | SDTM 跨域关联机制. RELREC = record-level (例 一次 AE 关联一次 EX); RELSPEC = specimen-level; RELSUB = subject-level. |
| **MedDRA** | 不良事件医学词典 | 国际通用医学术语词典. AE 域 AEDECOD / AEHLT / AEHLGT 等变量 bind 到 MedDRA. 不属 CDISC CT 但 AE 域强依赖. |
| **NCI EVS** | NCI 企业词汇服务 | National Cancer Institute Enterprise Vocabulary Services. CDISC CT 官方发布站, [browser.evs.nci.nih.gov](https://browser.evs.nci.nih.gov). 长尾 codelist 实时查这. |
| **Pinnacle 21** | 标准合规检查工具 | 业界 SDTM 数据集 vs 标准合规自动检查工具, 类似"linter for SDTM". 本项目不直连 Pinnacle 21, 需 cdisc.org 或对应工具实测. |
| **ISO 8601** | 日期时间标准 | 国际标准日期时间格式 (例 `2026-04-27T13:45Z`, `2026-04-27`, `--MM-DD`). SDTM 所有 --DTC 变量必填 ISO 8601. |

## 二、AI 平台 / RAG 术语

| 术语 | 中文 | 解释 |
|---|---|---|
| **System Prompt / Instructions** | 系统提示词 | 给 AI 的"操作手册", 定义身份 / 优先级 / 守门规则 / 锚点等. ChatGPT 叫 Instructions / Custom Instructions, Claude 叫 System Prompt, Gemini 叫 Gem instructions, NotebookLM 叫 Custom mode. |
| **Custom mode** | NotebookLM 自定义模式 | NotebookLM Chat 三档之一 (Default / Learning Guide / Custom). 唯一可装 system prompt 的入口, 上限 10K chars. 本部署用 Custom mode 装 instructions.md. |
| **RAG** | 检索增强生成 | Retrieval-Augmented Generation. AI 收到问题后先从知识库检索相关片段, 再据片段生成回答, 不靠"凭印象". 4 平台都用 RAG (NotebookLM 是最严格的 in-KB-only RAG). |
| **Indexing** | 索引化 | 上传知识库后 AI 先"读完一遍 + 切片做向量索引", 完成后才能 chat. 各平台时间不同 (Gemini ~1-3 min / ChatGPT ~5-15 min / Claude / NotebookLM ~2-10 min). |
| **in-KB-only** | 仅限知识库 | NotebookLM 设计原则: 答案只能来自上传的 sources, 不能上网搜也不能凭参数回答. 不在 KB 内的题它会拒答 (PUNT). |
| **PUNT** | 回答拒绝 | NotebookLM 行话, 指"我不知道, 不在我已上传的 source 里". **PUNT 不是 bug 是 feature** — 比编造好. |
| **Hallucination / 幻觉 / 虚构** | AI 编造 | AI 在知识缺口处编造看似合理但实际错误的信息. 本项目重点防的就是这个. |
| **Anti-hallucination Probe (AHP) / 反虚构探针** | "故意问错"测试题 | 评测题里故意带假前提 (例问"PF 域有哪些变量?" 但 PF 已废), 看 AI 能否主动识破而不是顺着错前提编. 本项目用 3 道 AHP 测每个平台. |
| **PASS+** | 主动识破假前提的额外加分 | 评测术语. PASS = 答对核心事实; PASS+ = 答对 + 主动指出题里的假前提. AHP 题最看重 PASS+. |
| **Smoke test** | 烟雾测试 / 冒烟测试 | "上电先检查最基础的能不能跑" 这一类预检测试, 不追求覆盖全, 只确认主要功能没塌. 本项目部署完跑 D0/D1/D5 三题就算冒烟通过. |
| **token** | LLM 计数单位 | LLM 内部把文字切成 token (约 1 中文字 = 0.5-1 token, 1 英文 word = 1-2 token). Claude Project 容量 ~3-4M tokens, Gemini 1M context window. |
| **Context window** | 上下文窗口 | LLM 一次能"记住"的最大 token 数. 超过会丢前面的. Gemini 1M = 一次能塞 ~1000 页, Claude ~200K-1M. |

## 三、项目内部术语

| 术语 | 含义 |
|---|---|
| **17 题 / 内部完整题库** | 项目用来评测每个平台的 SDTM 问题集合, 14 通用题 + 3 道反虚构题. 见 `../../SMOKE_V4.md` §2. |
| **D0-D9 / Demo** | 给同事用的 10 题快速演示包, 本目录 `./DEMO_QUESTIONS.md`. 不等于内部 17 题, 二者编号无对应关系. |
| **4 条质量规则** | 项目内部产出 / 审稿流程纪律 (例: "改写率 >50% 必须独立抽样审", "失败归档不删", "终稿必写复盘", "审稿不能自审"). 同事可不必看细节. |
| **LIVE** | 平台部署完成 + 跑过完整 17 题 + 通过质量门, 可以给人用. 4 平台目前都是 LIVE. |
| **baseline** | 项目内部官方测得的"该平台跑这套题应得多少分", 你自己部署后跑同样题应能复现 (允许 ±2 分浮动). |

---

## 想深入了解?

| 主题 | 路径 |
|---|---|
| 完整测试题库 + 各平台逐题答案 | `../../SMOKE_V4.md` + 各平台 `dev/evidence/smoke_v4_answers/` |
| 完整限制清单 | [`./KNOWN_LIMITATIONS.en.md`](./KNOWN_LIMITATIONS.en.md) |
| 项目方法论 | `../../claude_projects/docs/RETROSPECTIVE_V2.md` (Claude v2 终态复盘) + `../../notebooklm/docs/RETROSPECTIVE.md` (NotebookLM 复盘) |
| 4 平台跨平台复盘 | `../../retrospectives/PHASE5_RETROSPECTIVE.md` (v1.0 FINAL) |

> ⚠️ 注: 本节中形如 `../../...` 或 `dev/evidence/...` 的路径指向项目内部文档 (由 Daisy 保管), 不在本 release 包内. 如需详情请联系 Daisy.

---
*v1.1 — 2026-04-27 — 维护者: Daisy*
