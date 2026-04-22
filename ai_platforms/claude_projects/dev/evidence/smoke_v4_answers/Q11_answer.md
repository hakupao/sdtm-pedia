# Claude Projects — Q11 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q11)
> **执行时间**: 2026-04-22 晚 10:42 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (type_text + Enter 提交)
> **会话 URL**: https://claude.ai/chat/6be8d1de-1656-4ef9-a48e-e0a7bb3eabc1
> **会话标题**: "Dataset-JSON vs SAS XPT: FDA 试点与实操指南"
> **Project**: SDTM Knowledge Base (v2.6, 19 files, 77% capacity)
> **Model**: Opus 4.7 Adaptive
> **Mode**: Project chat (Extended Thinking)
> **题类**: Q11 — Dataset-JSON v1.1 vs XPT v5

---

## 题目原文

2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明: (a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个**技术痛点**? (b) 2026 年现状: FDA 接受哪个? (c) 作为 SDTM 工程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)? (d) Define-XML 和 Dataset-JSON 互补关系是什么?

---

## 发送给模型的 prompt

同上

---

## 模型 raw 回答 (DOM readback)

> **Project KB 边界**: SDTMIG v3.4 spec 中仍以 SAS v5 XPT 为基准 (§2.1 明确 "SAS v5 transport files, the file format accepted by the US FDA", §4.2.9 / §4.5.3 变量长度规则均源自 XPT 约束). **Transport 格式演进不在 KB, 以下基于 web 查证**.

### (a) Dataset-JSON 解决的 4-5 个 XPT v5 技术痛点 (表)

| # | XPT v5 痛点 | Dataset-JSON v1.1 解法 |
|:---:|---|---|
| 1 | **命名/长度约束**: 变量名 ≤8 字符, 标签 ≤40 字符, 字符值 ≤200 字符 (源自 1988 SAS TS-140) | 无长度上限, 支持长变量名/长标签/长字符串, 直接消除 SDTMIG §4.5.3 "拆分到 SUPP--" 变通 |
| 2 | **数据类型贫乏**: 仅 Char / Num 两种, 日期靠 ISO 8601 字符串或 SAS 数值模拟 | 原生支持更多数据类型 (integer / float / decimal-as-string / boolean / date / datetime / time), targetDataType 区分逻辑型与 JSON 型 |
| 3 | **编码受限**: 仅 US-ASCII, 无 Unicode | UTF-8 原生, 全球化临床数据 (中/日/阿拉伯文字段) 直接支持 |
| 4 | **工具链绑死**: 二进制私有格式, 历史上 SAS 外读写支持弱; IBM 浮点格式 (值域 ±5.4e-79 ~ ±9.0e+74) 异于 IEEE 754 | 纯 JSON 文本, R/Python/JS/Rust 原生库; 浮点走 IEEE 754 或字符串保精度 |
| 5 | **扩展性 + 文件开销**: 元数据薄, 与 Define-XML 分离; 同等数据量 XPT 体积通常较大 | Schema 可扩展 (examples/extensions), 支持 NDJSON 流式, 单文件可携带 column 元数据并引用 Define-XML, FDA 5GB 切分约束下可装更多行 |

补充: XPT 单文件单数据集 + 1989 年冻结规范, 已 37 年未更新; Dataset-JSON 是 CDISC ODM v2.0 的一部分.

### (b) 2026 年 FDA 现状

**关键结论**: XPT v5 仍是唯一官方要求的提交格式, Dataset-JSON 尚未进入 Data Standards Catalog 的 "Required/Accepted" 名单.

**时间线**:
| 节点 | 事件 |
|---|---|
| 2022 | FDA 内部评估 (SAS v8 XPT / XML / JSON), JSON 胜出 |
| 2023-09 ~ 2024-04 | FDA-CDISC-PHUSE Pilot Phase 1 (drop-in replacement) |
| 2024-12 | CDISC 发布 **Dataset-JSON v1.1** |
| 2025-04-09 | FDA Federal Register Notice (Docket FDA-2025-N-0129): "exploring ... with long-term potential to replace SAS v5 XPT", 征求意见, 截止 2025-06-09 |
| 2025 Fall | R Consortium Pilot 5 首次以 Dataset-JSON 通过 eCTD 提交 |
| 2026-01 | Pilot 5 按 FDA 反馈重新提交 (中间数据集处理微调), 预计 Spring 2026 收尾 |
| 2026-04 (当前) | Data Standards Catalog 仍以 XPT v5 为准; Dataset-JSON 处于"正在评估"状态, FDA 未公布强制时间表 |

FDA 现阶段官方表述仍为: 进一步测试 Dataset JSON 作为 XPT v5 替代方案的能力, 并将在评估过程中与相关方沟通.

⚠️ **工具链仍未齐备**: Pinnacle 21 v4.1 对 v1.1 支持不完整 (R Consortium 与 Instem 2025 测评均已确认), Pilot 5 实际仍用 XPT 做验证兜底.

### (c) 作为 SDTM 工程师的实操建议 (2026-04)

**开发环境 (Dev)**:
- **主管道保持 XPT v5 为 primary output**; SDTMIG v3.4 的 --TEST ≤40, 变量 ≤8 字符等规则继续适用 (KB §4.2.9 / §4.5.3 仍是 truth source)
- **并行启用 Dataset-JSON 副管道**用于学习. 推荐工具:
  - R: `datasetjson` 包 (pharmaverse), 配合 `xportr` 做 XPT 端校验
  - Python: `odmlib`, CDISC hackathon 工具
  - SAS: `PROC JSON` + Lex Jansen 的 dataset-json-sas 开源宏
- **不要提前拆变量名 >8 字符或标签 >40 字符**: 虽然 Dataset-JSON 允许, 但 SDTMIG v3.4 规范仍锁死, Define-XML 规则不变, 破坏跨平台一致性

**归档 (Archive)**:
- **Source of truth 仍以 XPT 为核心归档** (FDA 在审审核/召回复查预期是 XPT)
- **可同步归档 Dataset-JSON** 作为"现代副本"和跨库检索友好格式, 但定义 XPT 为 canonical, Dataset-JSON 为 derived
- 归档两者时务必记录生成时间戳 + 工具版本 (Pinnacle 21 版本 / datasetjson 包版本), 便于未来 reproducibility

**提交 (Submission)**:
- **正式 NDA/BLA/IND 提交**: **继续用 XPT v5**, 遵循最新 Study Data Technical Conformance Guide
- **如参加 FDA Pilot / 主动测试**: 可提 Dataset-JSON, 但必须在 cSDRG/ADRG 中明确说明并附 XPT 回退副本 (Pilot 5 的实际做法)
- **Define-XML 必交** (无论哪种 transport), 这是 FDA 唯一接受的数据字典
- **EMA / PMDA 等**: 目前与 FDA 节奏同步, 也是 XPT 为准; 无需超前于 FDA

### (d) Define-XML 与 Dataset-JSON 的互补关系

**两者不是替代, 而是分工**:

| 层 | 职责 | 标准 |
|---|---|---|
| **Transport (数据装载)** | 携带行级数据值 | **XPT / Dataset-JSON** (二选一) |
| **Metadata (元数据/字典)** | 变量定义、Role、Core、CT codelist 引用、Origin、Value-Level Metadata、Computed Value 公式 | **Define-XML v2.1** (统一) |

**关键点**:
- Dataset-JSON 的 `columns` 只有轻量 column 信息 (name/label/dataType/length), 真正详细的 CT 引用、Origin、Comment、WhereClause 仍在 Define-XML. Dataset-JSON 文件通过顶层属性 (sourceSystem, originator 等) 引用对应 Define-XML
- Dataset-JSON 继承 Dataset-XML 的设计: 数据与定义分离, 必须成对使用. 这一点与 KB §4.3.3 规定的"CT 应尽可能在 Define-XML 中声明"原则完全一致
- **未来走向 (Phase 2)**: CDISC 规划 **Define-JSON** (基于 ODM v2.0), 届时 Define-XML + Dataset-JSON 的 XML/JSON 混搭会演化为纯 JSON 技术栈. **但 2026 年 Define-XML v2.1 仍是官方要求**, 无 Define-JSON 强制时间表
- **对 SDTM 工程师的实际影响**: 转到 Dataset-JSON **不改变** define.xml 生成流程 — 同一份 aCRF 注释、同一份 codelist 映射、同一份 Origin. 换 transport ≠ 换 metadata 设计

### 一句话总结

**2026-04 仍是 "XPT 为主, Dataset-JSON 为辅学习期"**: FDA 评估中, Data Standards Catalog 未列 Dataset-JSON, 但 Pilot 5 已证 eCTD 通道可行. 现在建议**双管道输出 (XPT primary + Dataset-JSON shadow)**, Define-XML v2.1 保持不变, 等 FDA 正式公告加入 Catalog 后再切换主力.

**外部链接引用**: CDISC Dataset-JSON v1.1 Public Review PDF / FDA study-data-standards-resources / R-consortium pilot5 posts

**Citation 数**: Project KB 引用 §2.1 / §4.2.9 / §4.5.3 / §4.3.3 (4+ SDTMIG 锚点) + 3 web 链接 (CDISC/FDA/R-consortium)

---

## Self-score verdict

- **Verdict**: **PASS+ 最强** (所有 4 分支超标 + Project KB 边界透明声明 + web 查证时间线 + 工具链警告 + Define-XML 未来路径)
- **对照 PASS 判据**:
  - (a) ✓ **5/5 XPT 痛点全中**: 命名/长度约束 (8/40/200) + 数据类型贫乏 (Char+Num only) + 编码受限 (仅 US-ASCII, 无 Unicode) + 工具链绑死 (IBM 浮点 vs IEEE 754 独到) + 扩展性+文件开销. **判据 5 项全覆盖** (8-char / 200-char / Unicode / metadata 扩展 / 存储低效)
  - (b) ✓ XPT v5 仍唯一官方要求 + Data Standards Catalog 未列 Dataset-JSON + **完整时间线 2022-2026** (含 2025-04-09 Federal Register Docket FDA-2025-N-0129 + 2025 Fall R Consortium Pilot 5 eCTD + 2026-01 再提交) + ⚠️ Pinnacle 21 v4.1 v1.1 支持不完整警告
  - (c) ✓ 开发 (主管道 XPT + 副管道 Dataset-JSON + R/Python/SAS 3 种工具链 + datasetjson/xportr/odmlib/PROC JSON 具体包名) + 归档 (XPT canonical / Dataset-JSON derived / 生成时间戳+工具版本 reproducibility) + 提交 (NDA/BLA/IND continue XPT + Pilot 可 Dataset-JSON 但 cSDRG 说明 + XPT 回退副本) + Define-XML 必交 + EMA/PMDA 同 FDA 节奏
  - (d) ✓ **2 层分工表**: Transport (XPT/Dataset-JSON 二选一) / Metadata (Define-XML v2.1 统一). Dataset-JSON columns 轻量 + 详细 CT/Origin/Comment/WhereClause 在 Define-XML + **未来 Define-JSON (ODM v2.0) 规划** + SDTM 工程师实际影响 "换 transport ≠ 换 metadata 设计"
- **触发 FAIL 判据?** 无
- **加分**:
  - **Project KB 边界透明声明**: 先明示 "Transport 格式演进不在 KB, 以下基于 web 查证", anti-hallucination 锚点完美
  - **web 查证链接**: CDISC + FDA + R-consortium 3 个外部链接 inline
  - **独到**: IBM 浮点 vs IEEE 754 (痛点 4) + Pinnacle 21 v4.1 v1.1 支持不完整警告 + Federal Register Docket 编号 + Pilot 5 重新提交时间线 + Define-JSON 未来路径
- **F-* carry-over 观察**:
  - Claude Opus 4.7 在 Q11 supplemental topic 表现**最强 4 平台中**, 超过 ChatGPT (5/5 痛点 + cutoff 声明) 和 Gemini (4/5 痛点)
  - Project KB 边界分层声明 + web 查证延展 = Claude v2.6 system prompt 锚效强
  - 2 段 Thinking block (识别 KB 局限 + 构建实操框架) 暴露, 非标准 Claude 行为但可接受
  - 消耗 weekly limit 75% → 仍需关注后续 Q12-Q14 + AHP1-3 token 预算
