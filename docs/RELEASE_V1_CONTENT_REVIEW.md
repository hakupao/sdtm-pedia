# release/v1.0 Markdown 内容审阅

日期: 2026-05-12
范围: `release/v1.0/*.md` 与 `release/v1.0/self_deploy/*/tutorial.{zh,en,ja}.md`

## 总体判断

当前 release Markdown 更像“内部部署验收包 + 平台调试手册 + 技术验证记录”的混合体，不像面向普通访问者的项目介绍与使用说明。医学与 IT 术语本身多数不是错，但展示层级不合理: 太早暴露 RAG、token、system prompt、PASS/FAIL、AHP、内部 benchmark、reviewer、pipeline、stub、PUNT 等工程或评测语言，导致读者需要理解项目背后的构建机制才能读懂网页。

建议把网站公开文档定位改成:

- 面向临床数据、医学事务、统计编程、数据管理、项目管理等非开发者读者。
- 只解释“这个工具解决什么问题、适合谁、能查什么、不能替代什么、如何开始使用”。
- 技术实现、内部验证、平台容量、文件上传策略、prompt 细节和回归题库，移入附录、管理员部署手册或内部文档。
- 医学措辞使用 CDISC/临床数据标准语境，IT 措辞使用“知识库、检索、引用、部署实例、访问权限、版本边界”等产品化表达，避免 agent/debug/benchmark 语气。

## 主要问题

### P0: 受众视角错位

公开网页目前假定读者理解 AI agent / prompt / RAG / token / benchmark / PASS+。这与“项目介绍和使用说明书”的目标冲突。

典型位置:

- `release/v1.0/USER_GUIDE.zh.md`: “295 个 Markdown 源, 加上提示词工程喂给 4 个 AI 平台”“反虚构探针”等属于实现视角。
- `release/v1.0/GLOSSARY.zh.md`: 把 AI/RAG/project-internal 术语作为主术语表内容，普通用户会被迫学习内部机制。
- `release/v1.0/DEMO_QUESTIONS.zh.md`: “内部完整测试 Q1-Q14”“PASS+”“反虚构题”“60+ 答案”等是验收体系，不是用户说明。
- `release/v1.0/self_deploy/*/tutorial.zh.md`: 大量 `system_prompt.md` 字符数、token、文件数、索引状态、降级路径，适合管理员，不适合公开介绍页。

建议:

- 顶层页面只保留用户价值、适用场景、使用入口、限制边界。
- “验证结果”保留为简短可信声明，例如“已用覆盖变量定义、术语、域边界和跨域关系的测试集进行验证”，不展示内部题号和 PASS 规则。
- “自部署教程”改名为“管理员部署指南”或从主导航降级为“高级设置”。

### P1: 术语专业性不稳定

医学侧术语有专业内容，但中英混杂、口语词和工程词削弱了可信度。

需要替换的表达方向:

| 当前表达 | 建议表达 |
| --- | --- |
| 大白话“翻 PDF 要十几分钟” | “降低 CDISC SDTM 标准检索与交叉核对成本” |
| “喂给 4 个 AI 平台” | “封装为可在多种 AI 平台使用的 SDTM 知识库” |
| “反虚构 / 幻觉 / PUNT” | “不确定性处理 / 避免无依据回答 / 超出知识库范围时明确提示” |
| “smoke test / PASS / FAIL / PASS+” | “快速验证 / 通过标准 / 未达到预期 / 增强通过” |
| “stub” | “摘要占位条目 / 外部权威来源链接” |
| “token / chunk / RAG miss” | “平台容量限制 / 检索召回限制 / 部分长尾术语可能需回查官方来源” |
| “agent / reviewer / pipeline” | “构建流程 / 独立复核 / 验证流程” |

### P1: 文档层级需要重组

建议公开网站只保留 5 类内容:

1. 项目简介: 是什么、服务谁、解决什么问题。
2. 使用指南: 怎么提问、怎么看引用、怎么判断回答是否可用。
3. 平台选择: Claude / ChatGPT / Gemini / NotebookLM 的适用场景和访问方式。
4. 术语说明: 只解释 SDTM/CDISC/域/变量/受控术语/MedDRA/SUPPQUAL/RELREC 等用户必须知道的概念。
5. 限制与免责声明: 不替代 CDISC 官方标准、不替代组织 SOP、不覆盖实时外部更新。

以下内容应降级到内部或高级文档:

- 完整平台部署步骤、文件上传清单、prompt 字符数。
- 17 题/24 题回归测试、AHP、内部 Q 编号。
- token 容量、chunk 策略、RAG 实现细节。
- `.work`、`dev/evidence`、reviewer chain、pipeline phase。

### P1: 三语版本需要统一“产品文案”口径

中英日内容目前基本是逐项翻译，问题也同步存在。尤其日文大量保留英文工程词，如 `system prompt`, `token`, `PUNT`, `anti-hallucination`, `source`，会显得像内部技术备忘。

建议先重写中文主稿，再用中文主稿作为 source of truth 重写英文和日文。不要直接在现有英文/日文上局部润色，否则会保留原有信息架构问题。

## 文件级建议

| 文件组 | 当前定位 | 建议处理 |
| --- | --- | --- |
| `README.*.md` | 发布包目录说明 | 改成网站入口摘要，减少文件名导航，突出项目用途和适用人群。 |
| `USER_GUIDE.*.md` | 用户手册 + 技术亮点 +平台说明 | 重点重写。保留“是什么、怎么用、选哪个平台、限制”，删除内部实现细节。 |
| `GLOSSARY.*.md` | SDTM + AI +内部术语 | 拆分。公开术语表只保留医学/临床数据标准术语；AI/内部术语移到高级文档。 |
| `PLATFORM_COMPARISON.*.md` | 性能基准 +容量表 | 改成“选择建议”。减少分数、token、chunk，增加业务场景语言。 |
| `KNOWN_LIMITATIONS.*.md` | 技术限制清单 | 保留，但产品化表达。强调边界和官方来源，而不是 bug/guardrail/PUNT。 |
| `METHODOLOGY.*.md` | 审计/合规声明 | 可保留为“方法与验证声明”，但压缩公开页；详细审计链移附录。 |
| `DEMO_QUESTIONS.*.md` | 验收题库 | 改成“示例问题”。隐藏评分体系和内部 benchmark，只展示推荐问题与预期回答要点。 |
| `CHANGELOG.*.md` | 内部发布记录 | 缩短为用户可读版本历史；内部 Phase、reviewer、benchmark 细节移出。 |
| `self_deploy/*/tutorial.*.md` | 平台部署操作手册 | 改名/降级为“管理员部署指南”。公开站点不应把它当普通用户主路径。 |

## 推荐重写口径

### 项目一句话

建议:

> SDTM Pedia 是一个面向临床研究数据标准的 AI 辅助知识库，帮助用户更快查询 CDISC SDTM 变量、域、受控术语和跨域关系，并在回答中保留可回查的依据。

避免:

> 把 295 个 Markdown 源加提示词工程喂给 4 个 AI 平台。

### 用户价值

建议:

> 适用于 SDTM 数据映射、变量定义查询、域边界判断、受控术语核对和培训场景。对于法规提交和正式数据标准解释，仍应以 CDISC 官方出版物和组织内部 SOP 为准。

避免:

> smoke 满分、AHP 全识破、RAG 深度命中。

### 平台说明

建议:

> Claude 适合复杂标准问题和跨域推理；ChatGPT 适合团队共享和日常查询；Gemini 适合长上下文查询；NotebookLM 适合需要强引用和严格来源边界的场景。

避免:

> 1.29M tokens / 77% capacity / chunk miss / PUNT / system prompt guardrail。

## 建议执行顺序

1. 先确定公开网站的目标读者和导航层级。
2. 先重写 `README.zh.md` 与 `USER_GUIDE.zh.md`，形成新的语气样板。
3. 再重写 `GLOSSARY.zh.md` 和 `PLATFORM_COMPARISON.zh.md`，统一医学/IT 术语。
4. 将 `DEMO_QUESTIONS` 改为“示例问题”，保留少量代表题，删除内部评分叙事。
5. 将 `self_deploy` 从普通用户路径降级为管理员部署材料。
6. 最后用中文主稿同步英文和日文，避免三语风格继续分叉。

## 结论

这批文档不建议做局部润色。应按“公开产品说明 + 用户手册 + 管理员附录”的结构整体重写。核心不是减少专业性，而是把专业性放在正确层级: 对普通用户讲清临床数据标准价值、使用边界和可信来源；对管理员再讲部署、prompt、文件和验证细节。
