---
lang: zh
slug: methodology
order: 15
title: "构建方法与验证声明"
---

# 构建方法与验证声明

> 最近更新: 2026-04-29 · 与构建过程同步维护. 下文报告的状态反映验证 track 的当前实际进展.

## 目的

本文件说明本仓库中 SDTM 知识库的构建方式, 用于保障准确性的控制措施, 以及任何单条断言如何对照源出版物进行独立审计的程序. 以这种形式公开发布, 旨在让在受监管工作中依赖本知识库的使用者 — FDA / PMDA / EMA 提交; SDTM 数据编程; 映射质量控制 — 能够建立并按需重新建立其所要求的信任水平.

本声明的结构遵循临床 IT 领域常见的验证逻辑: 声明权威来源 (§1), 已定义的构建流水线 (§2), 端到端可追溯性映射 (§3), 已识别不符合项及其闭环的公开记录 (§4), 项目强制执行的常设控制 (§5), 以及该制品的使用边界 (§6). 进行有针对性审阅的读者可直接从 [§4](#4-已识别并关闭的不符合项) 开始.

## 合规框架

本知识库源自 CDISC SDTM 出版物, 该出版物受美国 FDA 强制性引用, 受日本 PMDA 认可, 并被欧洲 EMA 接受用于临床研究数据提交. *使用* 本知识库进行的工作通常受 ICH E6 (R3) GCP 以及由 FDA / MHRA / WHO 共同确立的数据完整性原则 (ALCOA+) 约束.

下文所述的构建方法采用基于风险的验证路径, 参考了 GAMP 5 (ISPE) 的思路 — 声明式规范, 已执行的验证, 独立复核, 以及有据可查的异常追溯链 — 但**不**主张在上述框架下取得正式分类或认证. §5 中每一条控制都映射到对应的 ALCOA+ 维度, 验证证据保留在仓库内供再次审计.

## 1. 权威来源

`knowledge_base/` 下每一个制品都可追溯至 4 份 CDISC 官方出版物之一. 仓库中无任何内容由第三方摘要或对标准的转述生成. AI 辅助组件仅产生有源依据的抽取; 流水线不允许无源生成.

| 来源 | 版本 | 范围 |
|---|---|---|
| SDTM Implementation Guide (PDF) | v3.4 (2021-11-29) | 461 页 — 域规范 / 假设 / 示例 |
| SDTM Model (PDF) | v2.0 Final (2021-11-29) | 74 页 — 概念模型 |
| SDTMIG (xlsx) | v3.4 | 63 个域 / 1,917 个变量 |
| CDISC Controlled Terminology (xlsx) | 2024 发布 | 1,005 个 codelist / 37,939 个 term |

原始出版物不在仓库内再分发; 著作权归 CDISC 所有. 详见 [项目免责声明](https://github.com/hakupao/sdtm-pedia/blob/main/DISCLAIMER.md).

## 2. 构建流水线

知识库通过 7 阶段流水线生成. 每个阶段以独立工作包形式记录 — 阶段 plan / 执行日志 / 验证记录 — 存放于仓库 [`.work/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work) 目录, 构成可审计源的一部分, 而非另立文档产物.

| 阶段 | 活动 | 主要产出 |
|---|---|---|
| 1 | 程序化将 xlsx 规范转换为 Markdown (Python) | 63 份 `spec.md`; terminology 索引 |
| 2 | 程序化 PDF 页码索引 (无视觉估算) | `page_index.json` |
| 3 | AI 辅助的 SDTMIG PDF 抽取, 分 11 批执行, 每批配套验证 | 各域的 `assumptions.md` / `examples.md` |
| 4 | 补充内容抽取 (model 与 chapter 层) | 6 份 model 文件; 6 份 chapter 文件 |
| 5 | 全量验证与主索引建立 | `INDEX.md`; 验证报告 |
| 6 | 检索优化 (路由层 / 反向变量索引) | `ROUTING.md`; `VARIABLE_INDEX.md` (1,523 个变量) |
| 6.5 | AI 平台部署 | 4 平台发布包 |

与上述 7 阶段流水线并行, 一条**原子级字面验证审计** track 持续推进. 知识库中每一条原子断言均在源 PDF 上按页对账. 截至 2026-04-29, 该审计已覆盖范围内 **97% 页码**, 仍在进行中. 每批证据公开于 [`.work/06_deep_verification/evidence/checkpoints/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work/06_deep_verification/evidence/checkpoints).

## 3. 可追溯性 — 单条答案的审计

仓库结构刻意设计为: 任何单条答案都可在数秒内对账至源出版物, 支撑 ALCOA+ 中 *Attributable* (可归属) 与 *Accurate* (准确) 两个维度.

**域级断言的验证:**

1. 识别答案中的域代码 (`AE` / `LB` / `DM` 等).
2. 打开 `knowledge_base/domains/<DOMAIN>/`:
   - `spec.md` — 变量级规范 (源自 xlsx; Core / 类型 / codelist 绑定)
   - `assumptions.md` — 域内假设 (源自 PDF)
   - `examples.md` — 实施示例 (源自 PDF)
3. 各文件头部均标注对应 PDF 页码区间. 对照 SDTMIG v3.4 PDF 进行对账.
4. 变量 Core 与 codelist 绑定, 如有 SDTMIG xlsx 可直接对照.

**章节级断言的验证**: 打开 `knowledge_base/chapters/chXX_*.md`. 页码区间与小节号与 SDTMIG 目录直接对应.

**受控术语断言的验证**: `knowledge_base/terminology/` 下每份 codelist 文件均带 CDISC C-code (例如 `C66731`), 可在 NCI EVS Browser 反查.

完整的 source-to-output 映射已发布为 [溯源矩阵](https://github.com/hakupao/sdtm-pedia/blob/main/docs/TRACEABILITY.md) (`docs/TRACEABILITY.md`).

## 4. 已识别并关闭的不符合项

校验阶段识别出 2 项系统性不符合事项. 两者均已公开记录; 公开披露本身是本方法学的结构性特征, 与受监管临床 IT 环境对电子记录所要求的审计追溯链一致.

### NCR-001 — 页码索引偏移 (闭环于 2026-04-15)

PDF 图像与图表索引的首版依赖 AI 组件通过视觉识别页码. 领域专家抽样复核认定: TD example 页码引用偏移 4 页, 类似的 ±2 至 ±4 页偏移分散在约 60 张图上.

**根因**: 对 PDF 进行视觉读取的 AI 组件无法可靠观测页边界; 它们在估算. 当时流水线没有区分 *精确值* 与 *估算值*.

**纠正措施**: 页码索引重构为程序化生成. `page_index.json` 现在是唯一权威源; 所有下游文件统一引用; 任何无法程序化确认的 AI 页码引用一律标 `(estimated)` 且不写入权威索引.

调查记录: [`.work/03_verification/issue1_investigation.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issue1_investigation.md).

### NCR-002 — 骨架内容被判 PASS (闭环于 2026-04-15)

`ch04_general_assumptions.md` 在首轮校验中被判 PASS, 但其中约 30% 子节仅含 1–2 句占位文字, 标记为 `<!-- 待补全 -->`. SDTMIG 该章对应 38 页详细规则; 当时文件每页约 9 行, 修复后每页约 17 行.

**根因**: PASS 标准把 *"缺失内容已经清楚标了出来"* 等同于 *"内容已完整"*. 此外, 撰写该文件的 agent 同时执行了批准; 没有独立 reviewer 阅读源 PDF.

**纠正措施**: 所有被标记的子节按源 PDF 重写. PASS 标准重写为定量化: 行数/页数比值需达到基线; 零占位标记; 要点覆盖率 ≥ 95%. 写者-审者分离自此成为常设控制 (§5 第 2 条).

闭环记录: [`.work/03_verification/issues_found.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issues_found.md).

### 已知边界

部分限制无法在当前 AI 平台部署形态内彻底解决 — 例如大型 codelist 以 stub 形式保存, 实时外部查询无法内嵌. 这些边界单独跟踪, 在部署制品中披露: [已知限制](./known-limitations/).

## 5. 常设验证控制

上述两项不符合事项产生了 4 条常设控制. 它们适用于仓库内每条 track 的每个阶段, 证据保留以供再次审计.

| # | 控制 | ALCOA+ 维度 |
|---|---|---|
| 1 | **定量 PASS 标准.** 覆盖率, 行数/页数比, 零占位标记; 不接受"看起来对"这种主观判断. | Complete · Accurate |
| 2 | **写者-审者分离.** 撰写文件的 agent / 进程不得批准同一文件. Reviewer 独立阅读源 PDF, 输出结构化覆盖率报告. | Attributable |
| 3 | **AI 估算值必须标注.** 凡 AI 无法程序化确认的值, 均标 `(estimated)`, 不进入权威索引. | Original · Accurate |
| 4 | **每阶段收尾的人工抽样复核.** 每个阶段结束都对源 PDF 做随机抽样对账, 不是事后兜底. | Accurate · Available |

4 条控制及其对应的不符合事项完整记录于 [`.work/meta/retrospective.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/meta/retrospective.md).

验证 track 本身是迭代的. 截至本声明日期, §2 提到的深度验证审计已完成 14 轮复核; 每一轮均作为证据保留, 任何在某一轮发现的差异都回推至知识库.

## 6. 适用范围与边界

- **独立复核由设计支持.** 使用者可在数秒内定位源页, 直接对照 SDTMIG PDF 进行核验. 发现差异请通过 [GitHub issue](https://github.com/hakupao/sdtm-pedia/issues) 反馈; 审计 track 是开放的, 接受外部发现.
- **在受监管证据链中的使用.** 本知识库可作为 SDTM 数据编程, 映射审阅, SDTM 培训等场景的工作参考. 它本身**不**是 21 CFR Part 11 / PMDA 级别的电子记录, 也**不**替代组织内部对此类记录的标准操作规程.
- **不替代官方标准.** 法规提交场景的权威参考为对应的 CDISC 出版物 (SDTMIG, SDTM Model, Controlled Terminology). 本知识库与官方出版物若出现差异, 以官方出版物为准.

---

**仓库:** [github.com/hakupao/sdtm-pedia](https://github.com/hakupao/sdtm-pedia) · **许可证:** CC BY 4.0
