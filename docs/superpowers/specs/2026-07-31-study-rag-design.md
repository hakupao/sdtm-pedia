# Study RAG 独立知识库设计 (multi-RAG 联合检索第一步)

> 状态: **spec 已定稿, 待实施计划** (2026-07-31)
> 讨论记录: 本 spec 由 brainstorming 对话产出, 用户已确认方向
> 约定: 研究一律使用内部代号 **`st01`** (后续研究 st02, st03, …), 真实研究名在
> 文档/脚本/collection/metadata/UI 中**一律不出现**; 真名→代号映射存本地文件
> `sdtm-rag/data/study/studies.local.yaml` (gitignore), 进 git 的脚本只认代号、
> 经映射文件解析源目录。真名字符串仅存在于本地 `source/study/` 与该映射文件。

## 1. 背景与目标

`source/study/` 下放入了某具体研究 (代号 st01) 的专有资料: aCRF、protocol (日文)、
workflow、EDC ConfigurationReport (新旧两版 xlsx)、DEMO 数据导出 (xlsx)。
研究数据**不是 SDTM 格式**, 将来要做 SDTM mapping。

**目标**: 把 study 数据抽成 RAG knowledge base 中独立的一部分 (独立 collection),
与现有 CDISC 标准库平级, 为多 RAG 联合检索做准备。

**核心使用场景** (按优先级):

1. **SDTM mapping 助手**: 用户问「某画面的某字段应该放在 SDTM 标准的哪里、怎么做」,
   系统同时检索 study 库 (字段事实) + CDISC 库 (标准依据), 合并后给映射建议。
2. aCRF / mapping 定位、protocol 内容查询、EDC 配置查询等独立提问 (不依附 SDTM)。

## 2. 范围

**In scope (一期)**:

- ConfigurationReport xlsx → 结构化 field catalog → field card (主力检索单元)
- Protocol / workflow PDF → 章节级 markdown
- aCRF PDF → 页级粗切 (仅保底通道, 不做标注解析)
- DEMO xlsx → 实例值折进 field card (不整体入库)
- 独立 chroma collection `study_st01` + 多 collection 路由 (自动 + UI 强制开关)

**Out of scope (明确不做)**:

- aCRF 标注自动解析与字段级关联 — **二期**, 最难最有损, 先按页粗切保底
- 独立第二 RAG 服务 — 联邦第一步在单服务内做 multi-collection, 路由逻辑打磨对后将来可平移
- CDISC 库式全量深审仪式 — 用分轨保真替代 (见 §4)

## 3. Chunk 形态设计

### 3.1 Field card (主力单元, 每字段一张)

```markdown
---
study: st01
version: <ver>
doc_type: field_card
form_oid: <form>
field_oid: <field>
source: ConfigurationReport_<ver>, sheet=<s>, row=<n>
---
# [<form 名>] <字段 label> (<field_oid>)
- Form: <日文名> / <英文名>
- 型: <type/长度> / <必填性>
- Codelist: <选项 or 自由記述>
- Edit checks: <关联 check 摘要>
- DEMO 実例値: <采样值>
- 旧→新版差分: <有/无, 摘要>
```

### 3.2 其他单元

| 来源 | 单元 | metadata 关键字段 |
|------|------|------------------|
| Protocol PDF | 章节级 markdown chunk | heading path, 页码范围 |
| Workflow PDF | 章节/页级 chunk | 同上 |
| aCRF PDF | 页级 chunk (一期粗切) | 页码 (二期挂 field card) |

所有 chunk metadata 统一带 `study_id` / `doc_type` / `version`, 为多研究扩展预留。

## 4. 保真策略: 按转换性质分轨

深审流程的重量与"有损转换量"成正比。study 线把大部分工作放进确定性轨, 规避全量深审:

| 轨道 | 内容 | 转换性质 | 验证方式 |
|------|------|----------|----------|
| 确定性轨 | ConfigReport → catalog → field card | 代码解析 + 模板拼装, **零 LLM** | 机器全量: 行数守恒 + 覆盖台账 + round-trip 抽查 |
| 有损轨 | Protocol / workflow PDF → markdown | OCR/LLM 改写 | 规则 A 抽检 (范围仅几十页) |
| 二期轨 | aCRF 标注关联 | 最难最有损 | 一期不碰 |

### 4.1 约束机制 (从 06 深审提炼, 去掉重仪式)

1. **Pilot 先行, schema 后冻结**: 先写 ~10 个真实 mapping golden questions;
   取 1-2 个 form 端到端做通 field card, 用 golden questions 验证粒度够用,
   **然后才冻结 schema 跑全量**。防返工的根本手段。
2. **溯源 frontmatter**: 每张卡带 `source_file / sheet / row_range / version / generated_by`,
   问题一步定位到源 xlsx 行。
3. **覆盖台账**: 机器生成「源文件每行 → 落到哪张卡」清单, 孤儿行必须为 0。
   结构化源可做到全自动 100%。
4. **管线幂等**: 产物全部由脚本一键重生成, **勿手改产物**;
   源文件新版本到来 = 重跑 + diff。失败 attempt 按规则 B 归档。
5. **小批次硬约束 (经验教训)**: 有损轨每个 agent/session 任务限定小段
   (protocol 每批 ≤ 10 页, 单一职责), 防止 usage/context 压力下精度衰减。
   每批产物独立留痕, 批间不共享 context。

## 5. 联邦检索 (多 RAG 第一步)

- 同一 sdtm-rag 服务内 multi-collection: `cdisc` (现有) + `study_st01` (新)。
- **默认自动路由**: 按问题判断查哪个库或双库并查; mapping 类问题固定双库并查,
  study 库出字段事实, CDISC 库出标准依据, 合并进同一 prompt。
- **UI 强制开关**: chat UI 提供库选择, 可覆盖自动路由。
- Embedding 沿用 text-embedding-3-small (多语言, 日文可用);
  pilot 阶段附带小评测验证日文检索质量。

## 6. 数据安全红线

- **study KB 只存本地, 永不上传**: 源文件、field catalog / cards、chroma 索引
  全部只落本地磁盘 (计划放 `sdtm-rag/data/study/`, 补 gitignore 规则),
  不进 git (包括任何远端仓库)、不进 pages.dev / release bundle 等公开链路。
- 一切进 git 的文档与代码 (spec / plan / evidence / worklog / 脚本) 不出现真实研究名
  与真实字段数据, 只写结构与统计, 研究一律以代号 st01 指代 (映射文件本地解析)。
- 注: embedding / LLM 推理沿用项目既有决策走云端 API, study 文本会经 API 传输;
  若此边界不可接受, 需单独决策 (本地模型此前已放弃)。

## 7. 验收标准

1. 覆盖台账全绿: ConfigReport 每行落卡, 孤儿行 = 0 (机器校验)。
2. Golden questions (~10 题) 检索命中: mapping 类问题 field card 进 top-k。
3. 有损轨抽检 PASS: protocol markdown 按规则 A 独立抽检留痕。
4. 联邦路由: 双库并查场景下两库 chunk 同时进入 prompt, UI 开关可强制限定。
5. git 安全: `git status` 确认无 study 衍生产物被追踪; 进 git 文档无真实研究名。

## 8. 风险与对策

| 风险 | 对策 |
|------|------|
| ConfigReport 表结构复杂, parser 覆盖不全 | 覆盖台账暴露孤儿行; pilot 阶段先摸清 sheet 结构 |
| 日文 embedding 检索质量不达标 | pilot 小评测; 不达标再考虑 query 翻译或换模型 |
| 自动路由误判导致漏检 | UI 强制开关兜底; 路由规则从简 (关键词 + study 名) 起步 |
| schema 冻结后仍发现粒度问题 | golden questions 在冻结前验证; 管线幂等使重跑成本低 |
