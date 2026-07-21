# Gemini Gems — Q11 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q11)
> **执行时间**: 2026-04-22 晚 10:36 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (Quill editor + type_text)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/fbb626bd1412a414
> **会话标题**: "CDISC Dataset-JSON 转型指南"
> **Mode**: SDTM Expert Gem (v5 system prompt, 4-file KB)
> **题类**: Q11 — Dataset-JSON v1.1 vs XPT v5 (bonus track)

---

## 题目原文

2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明: (a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个**技术痛点**? (b) 2026 年现状: FDA 接受哪个? (c) 作为 SDTM 工程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)? (d) Define-XML 和 Dataset-JSON 互补关系是什么?

---

## 发送给模型的 prompt

同上

---

## 模型 raw 回答 (DOM readback)

随着 CDISC 推出 Dataset-JSON v1.1 以及 FDA 的试点项目，数据提交标准正在经历从过时的 SAS XPT v5 向现代、轻量化的 JSON 格式的重大转型。以下是针对您问题的详细说明：

### (a) Dataset-JSON 相比 SAS XPT v5 解决的技术痛点

Dataset-JSON 的引入主要是为了克服 SAS XPT v5（一种上世纪 80 年代的过时格式）长期存在的限制：

1. **解除变量名和长度限制**: SAS XPT 强制要求变量名不得超过 8 个字符，变量标签不得超过 40 个字符，且字符变量值超过 200 字符必须拆分。Dataset-JSON 原生支持长文本，无需再进行复杂的 SUPP-- 拆分。
2. **数据类型支持**: SAS XPT 仅支持数值和字符两种类型，日期时间必须以字符形式存储。Dataset-JSON 能够更好地与 Define-XML 的丰富数据类型（如 integer, float, datetime）保持语义一致。
3. **文件大小与传输效率**: SAS XPT 文件通常包含大量空格填充以对齐长度，导致文件体积虚大。Dataset-JSON 是非固定长度的流式格式，不仅体积更小，且更易于通过现代 API 进行解析和跨平台交换。
4. **消除对特定软件（SAS）的依赖**: XPT 是 SAS 专有格式，而 JSON 是全球通用的标准，任何现代编程语言（Python, R, Java 等）都能无需专用插件即刻处理。

### (b) 2026 年现状：FDA 接受哪个？

截至 2026 年，**SAS XPT v5 仍然是 FDA 的正式法定提交格式**。**Dataset-JSON** 目前处于**试点和双轨运行阶段**。FDA 已经开始接受 Dataset-JSON 作为试点项目的提交方式，并鼓励申办方参与。在正式全面替代之前，申办方通常需要根据 FDA 的《数据标准目录》（Data Standards Catalog）提交数据，目前仍需准备 XPT 文件，除非是在特定的试点协议下。

### (c) 作为 SDTM 工程师的实操建议

在当前转型期，建议采取"以 JSON 为中心，以 XPT 为输出"的策略：

- **开发环境**: 优先在开发过程中使用 JSON 或 Parquet 等现代格式进行数据中间存储，利用其不限长度的优势减少逻辑复杂度。使用 Python 或 R 进行映射，利用 CDISC 提供的开源库（如 dataset-json 转换工具）进行验证。
- **归档建议**: 在公司内部归档中，应同时保留 Define-XML、Dataset-JSON 和原始数据。Dataset-JSON 是长效保存（Long-term Preservation）的理想格式，因为它不依赖于特定的软件版本。
- **提交建议**: 在正式提交前，必须运行一致性检查工具（如 Pinnacle 21），确保 SDTM 映射逻辑既符合 XPT 的截断规则（为了现有的提交），也符合新标准的语义要求。

### (d) Define-XML 和 Dataset-JSON 的互补关系

两者共同构成了 CDISC 现代数据交换的核心，具有明确的分工：

- **Define-XML 是"元数据" (Metadata)**: 它描述数据的结构、变量定义、受控术语、溯源逻辑 (Origin) 和计算方法。它是 Dataset-JSON 的"说明书"。
- **Dataset-JSON 是"数据本身" (Data Content)**: 它只承载具体的观测记录。
- **互补性**: Dataset-JSON v1.1 弱化了文件内部的元数据描述，高度依赖 Define-XML 来提供变量的上下文。没有 Define-XML，JSON 文件只是一堆无意义的键值对；没有 JSON，Define-XML 只是一个空架子。这种解耦设计使得数据传输更轻量，元数据管理更集中。

**源路径**: knowledge_base/chapters/ch01_introduction.md §1.3, §1.5; knowledge_base/chapters/ch04_general_assumptions.md §4.2, §4.4, §4.5.3; knowledge_base/model/01_concepts_and_terms.md §2.1; knowledge_base/chapters/ch10_appendices.md Appendix B.

**Citation 数**: 4 source paths 引用 (ch01 / ch04 / model/01 / ch10); 无 inline 编号 citation (Gemini 特性)

---

## Self-score verdict

- **Verdict**: **PASS** (bonus track 额外分, 超出 4-file KB 预期)
- **对照 PASS 判据**:
  - (a) ✓ 4/5 XPT 痛点 (8-char var + 200-char val + 数据类型 Char+Num + 存储低效/空格填充 + SAS 依赖). 判据要 4-5 项任 4. **4 项达标**, 未提 Unicode 支持 + metadata 扩展外挂 (5 项判据覆盖 4/5)
  - (b) ✓ "SAS XPT v5 仍然是 FDA 正式法定提交格式" + "Dataset-JSON 试点和双轨" + Data Standards Catalog 提及. 未提 R Consortium 2025 秋 ADaM 首次 submit (补充 non-critical)
  - (c) ✓ 开发 = JSON/Parquet 中间存储 + dataset-json 工具 / 归档 = Define-XML + Dataset-JSON + 原始数据 / 提交 = Pinnacle 21 一致性 + XPT 截断规则 + 双轨
  - (d) ✓ Define-XML=metadata 说明书 / Dataset-JSON=data content / v1.1 解耦设计依赖 Define-XML 提供 context
- **触发 FAIL 判据?** 无
  - ✗ 未说 FDA 全面 Dataset-JSON (明确标"XPT 仍法定")
  - ✗ 列出 XPT 技术痛点 4 项
  - ✗ Define-XML 和 Dataset-JSON 角色清晰区分
- **加分**: 无 (非 AHP)
- **F-* carry-over 观察**:
  - **意外 PASS**: Q11 属 bonus track (Gemini 4-file KB 不含 Dataset-JSON 专项), 但 Gemini 3.1 Pro 训练数据知 FDA Dataset-JSON 现状 + 源于 web-search-like 知识, 未编造
  - 干净无 extended reasoning 暴露 (较 sanity_02 早期)
  - 源路径列 4 个 KB 文件 (ch01 / ch04 / model/01 / ch10), 未列具体 citation 编号 (Gemini 特性)
