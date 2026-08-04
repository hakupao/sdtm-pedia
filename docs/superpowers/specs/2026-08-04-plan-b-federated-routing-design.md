# Plan B 联邦路由 + 联网搜索开关 — 设计 spec

> 日期: 2026-08-04
> 状态: 已经用户逐节批准 (brainstorm 记录见本文件 §决策日志)
> 前置文档: `.work/meta/study_rag_handoff_2026-08-04.md` (交接) /
> `sdtm-rag/evidence/checkpoints/study_golden_v1.md` (golden v1.1 定稿 + 四类 miss)
> 红线: 本文档只含统计与结构描述, 无真实研究名/字段 OID/项目标签/单元格值

## 0. 背景与目标

Plan A (study 确定性轨) 已收官: `study_st01` 959 卡入库, golden v1.1 下
hybrid+CJK bigram **88.5% (PASS)**, 但**未接入服务** —— 服务目前只查
`sdtm_kb_v1` (CDISC, 4303 chunk)。

Plan B 目标: 把 study 库接入服务 (联邦路由), 补齐确定性轨遗留的四类检索 miss
(结构化直查), 修复 CDISC 侧变量索引挤占, 并新增联网搜索开关。

**基线数字 (务必用这一组)**: study 轨 source recall 88.5% (golden v1.1, 25 计分题,
hybrid+CJK bigram); CDISC 81.1% (140 题, retrieval-only + hybrid)。

## 决策日志 (用户裁决, 2026-08-04)

| # | 决策点 | 裁决 |
|---|--------|------|
| D1 | 范围 | 四块全做: 联邦路由核心 / study 结构化直查 / eval chunk 粒度判据 / CDISC 变量索引挤占 |
| D2 | 安全边界 | **局域网免密开放** — study 库同样免密, 局域网视为受信内网。此为明确决策, 非路由接线副作用 (满足交接 §5.3 要求) |
| D3 | 路由方式 | 自动路由 + 前端可显式覆盖 |
| D4 | 跨库问题 (EDC↔SDTM 映射类) | best-effort, 不进验收; 回答标注为推理性 |
| D5 | 路由器实现 | **LLM 判库** (light 模型), 以 temperature 0 + 严格 JSON 契约 + 失败降级双库并查收窄非确定性 |
| D6 | 联网搜索定位 | Anthropic 服务端 web search tool 透传给答题模型 |
| D7 | study × 联网搜索 | **允许但 UI 警示** — 开关对所有库生效, corpus 涉及 study 且搜索开启时前端常驻警示条 (检索词可能外发互联网), 不阻断 |

## 1. 总体架构

### 1.1 FederatedEngine (组合, 不改造)

新增 `server/federation.py`: `FederatedEngine` **组合**两个现有 `RAGEngine` 实例
(`sdtm_kb_v1` + `study_st01`), 不把 RAGEngine 改造为多 collection。

- 每个引擎保留自己的 BM25 索引 (study 侧天然获得 CJK bigram 切词);
- 直查通道各挂各的: S1 (现有 `structured_lookup.py`) 只挂 CDISC 引擎,
  S2 (本计划新增) 只挂 study 引擎;
- 引擎注册表按 list 设计 (未来 st02 可加), 本计划只有 st01 一个 study 实例。

### 1.2 LLM 路由器

- light 模型 (`anthropic/claude-haiku-4-5` via LiteLLM Router 现有 "light" 组);
- 输入: 问题 + 两库各一句话描述; 输出: 严格 JSON `{"corpus": "cdisc"|"study"|"both"}`;
- temperature 0, schema 校验;
- **任何异常 (解析失败/超时/非法值) → 降级 "both"** —— 兜底方向是宁可多查;
- API: `AskRequest` 加 `corpus: "auto"|"cdisc"|"study"|"both"` (默认 `"auto"`),
  非 auto 时跳过 LLM 路由;
- 前端: 下拉选择器, 默认 auto。

### 1.3 both 合并策略

按库配额取 top_k (各取 `ceil(k/2)`), **不做跨库分数排序** (两库相似度分布不可比)。
上下文中按库分组呈现, 组头标明库身份。

### 1.4 引用标识

- `SourceItem` 加 `corpus` 字段 (`"cdisc"` | `"study_st01"`);
- 前端徽章: 【標準 CDISC】/【本研究】;
- system prompt 更新: 要求回答标明信息来自哪个库; 跨库映射类回答标注为推理性 (D4)。

### 1.5 安全 (D2 记录)

服务保持 `0.0.0.0:8000` 局域网免密 (`SDTM_RAG_AUTH_ENABLED=false`)。study 库
接入后同样免密。风险已知悉: 真实临床研究字段结构对全局域网可见。
现有 `auth.py` 登录门保留在代码中不删, 未来可一键恢复。

## 2. 施工顺序 (5 个 Phase, 各有 eval 闸)

依赖链: Phase 0 → Phase 1 → {Phase 2, Phase 3, Phase 4 可并行}。

### Phase 0 — 前置: eval 判据下沉 chunk/section 粒度

- `check_source_recall` 支持 `file#section` 形态的期望 (检索元数据已有 `section`
  字段), 纯文件路径写法向后兼容;
- 动机: CDISC 侧存在 222-chunk 单文件, 文件粒度判别力≈0; 两库混判必须先有此判据
  (交接 §5.1 硬前置);
- **刻意不做**: 13 道疑似 OR 语义题的改判 (须非受益方逐题裁定, 交接 §7 已记录)。

### Phase 1 — 联邦路由核心

交付: FederatedEngine + LLM 路由器 + 配额合并 + API/前端 corpus 参数 + 引用标识。

验收 (三闸):

1. **路由准确率**: 165 道现有 golden 题 (study 25 + CDISC 140) 每题库归属已知,
   免费充当 routing gold。**跑 3 遍测稳定性** (LLM 路由是全计划唯一非确定性组件),
   阈值 ≥95%; 方向性硬要求: "study 题被路由成 cdisc-only" 必须为 **0**
   (这是唯一致命方向; 错成 both 可容, 只损效率不损召回);
2. **端到端零回归**: auto 路由下 study 25 题 ≥88.5%, CDISC 140 题 ≥81.1%
   (同索引对比, 无重灌噪声);
3. **hybrid 接线后重测** (交接 §5.2): 联邦路径下 study 侧 hybrid+CJK bigram
   配置生效性复核。

### Phase 2 — study 结构化直查通道 (S2)

对齐 S1 契约: `resolve(query)` → 命中卡 id, union 并入检索结果。数据源全部来自
catalog / config report 确定性产物 (`scripts/study/build_catalog.py` 等)。

覆盖四类实测 miss (golden_v1 §3.3 + §3.2, 用户已裁决卡片保持纯净、全部转本通道):

| 类 | 直查依据 |
|---|---|
| 多卡家族只召回其一 (丸数字重复组) | OID 前缀家族枚举 |
| 近义双卡判别失败 | codelist ID / item group / 显示条件精确判别 |
| ID 与语义脱钩的长尾卡 | OID / 标签精确匹配 |
| form 缩写词汇缺口 | **直查层内建显式别名表** (手工、小、有据可查; 不写入卡片) |

验收: 4 道已知 miss 题转命中 + study 25 题全量零回归。

### Phase 3 — CDISC 变量索引挤占修复

域特定问法下对 VARIABLE_INDEX 做确定性降权/过滤 (S1 同层规则)。

步骤: 先从 `cdisc_gold_scope_review.md` 圈出受影响题集 → 设计触发形状 (域特定
问句 + 域 spec 存在) → 修后受影响题集提升且 CDISC 140 题全量零回归。

### Phase 4 — 联网搜索开关

- Anthropic 服务端 web search tool 透传给答题模型, 模型自主决定是否搜索;
- 前端独立开关, **默认关**; API `AskRequest` 加 `web_search: bool`;
- 降级规则 (确定性): 答题落到 DeepSeek fallback (不支持该 tool) → 自动不搜,
  响应标注 "本题未联网"; 开关关闭 → 完全不挂工具, 行为与现状逐字节一致;
- study 交互 (D7): 对所有库生效; corpus 涉及 study 且搜索开启时前端常驻警示条;
- 引用: web 来源单独分组 (【Web】徽章 + URL), 与 KB 引用不混排;
- **码闸交互**: web search 实际发生 (响应含 search 工具使用记录) 的回答,
  `check_code_grounding` 从"阻断"降级为 "advisory 标注", 回答头部标明
  "含联网内容, 确定性护栏部分不适用"; 搜索未发生则护栏原样全开;
- **eval 隔离**: 所有 golden 评测固定开关关跑 (联网结果不可复现, 不进确定性评测)。

验收: 开关关 = 现状零回归 (全量 eval 数字不变); 开关开 = 冒烟测试验证工具透传 /
引用分组 / fallback 降级 / 警示条 (人工核验, 不设阈值)。

## 3. 测试与红线

- 全程 TDD; 全量测试基线 669 passed 只增不减;
- git 安全延续: study 数据零入库 (`data/study` gitignore), commit 真名扫描;
- Phase 1 / Phase 2 合并前走独立复审 (规则 D, 不同 subagent_type);
- LLM 路由与联网搜索是仅有的非确定性组件, 其余全部确定性; 两者的非确定性
  均被隔离在 eval 之外 (路由 3 遍稳定性测量; 搜索不进 eval)。

## 4. 明确不做 (out of scope)

- 跨库映射 gold 题与阈值 (D4: best-effort);
- 13 道 OR 语义题改判 (交接 §7);
- 卡片写入推断关联 (用户既有裁决: 卡片保持纯净);
- chapters.py 整file单块策略重评 / 跨重灌漂移 n≥3 实验 (交接 §7 backlog, 独立排期);
- 多 study (st02+) 实装 (注册表留口, 不实装)。
