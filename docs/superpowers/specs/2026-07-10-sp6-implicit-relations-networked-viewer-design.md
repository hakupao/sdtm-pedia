# SP6 设计 — 隐性关系挖掘 + 网状富节点查看器(Pilot: 肿瘤评估簇)

> 状态: **设计待评审** (2026-07-10)
> 来源: 本设计由一次 brainstorm 收敛而来(用户四项决策见 §1.3)。
> 上游: [[SP1 meta.yaml]] (硬结构真源) · SP4 Neo4j 探索层 · `scripts/build_kg_viewer.py`(现有查看器)
> 硬约束: 本单元产出的隐性关系是 **advisory 层, 永不写回 meta.yaml**(硬软彻底分层)。

## 1. 背景与目标

### 1.1 现状
- `meta.yaml` 只编码**硬结构关系**(域→变量、变量→码表、域→类、same_class、curated RELATED_TO)。
- 现有 `kg_viewer.html` 是 **3 个固定结构视图**(结构总览 / 域钻取 / 码表影响),每个是 2-3 层的树,非网状;节点只有 title,详情靠一个静态面板。
- IG 散文(`knowledge_base/domains/<D>/{assumptions,examples}.md`)里其实描述了大量**跨域语义/数据流关系**(如 RECIST 肿瘤评估:PR 的操作测量 → TR/MI → 汇总 RS → 关联 TU),但从未被结构化。

### 1.2 目标
1. **挖掘隐性关系**:从 IG 散文抽取三类跨域关系,证据锚定、标为推断/advisory,与硬关系分层。
2. **查看器升级**:从固定树 → **网状点击无限展开 + 富节点(可展开详情)**。

### 1.3 已决策(brainstorm)
| 维度 | 决策 |
|---|---|
| 定位 | **探索线索 · 证据锚定** —— 发现工具;每条推断关系附 IG 逐字引文 + 置信度 + "推断"标注;不追求穷尽或 100% 正确 |
| 关系类型 | **数据流(有向)** + **显式链接(RELREC 等)** + **共现(无向)**;不做"概念/语义相近"(与 same_class 重叠) |
| 广度 | **聚焦一簇先做透**:肿瘤评估簇 TU/TR/RS/PR/MI + 数据驱动浮现的直接邻居;验证后再议推广 |
| 富节点详情来源 | **混合**:结构化详情离线内嵌 + 可选"深入解释"按钮联网调 RAG |

### 1.4 Non-goals(YAGNI)
- 不做全 63 域挖掘(试点只做簇)。
- 不反哺 meta.yaml / 不进任何 golden 校验门。
- 不做语义相似类关系。
- 不追求穷尽或权威;低置信边默认收起。

## 2. 架构总览(4 组件)

```
knowledge_base/domains/<簇>/{assumptions,examples}.md   (IG 散文, 已逐页核验)
        │
        │  【组件 A】mine_implicit_relations.py  (离线管线)
        │   显式链接=正则 · 数据流=LLM+证据 · 共现=计数 ; 数据流过对抗核验
        ▼
data/meta/implicit_relations.json  (advisory, 证据锚定)  +  evidence/checkpoints/implicit_relations_audit.md
        │
        │  【组件 D】build_kg_viewer.py 同时内嵌 meta.yaml(硬) + implicit_relations.json(软)
        ▼
kg_viewer.html   【组件 B 网状探索 + 组件 C 富节点】   ──(可选,在线)──▶  :8000 RAG /api/ask
```

## 3. 组件 A — 隐性关系挖掘管线

**入口**: `scripts/mine_implicit_relations.py`(新增)。确定能确定的、只在必要处用 LLM——沿用 SP1 气质。

**输入**: 簇域(种子 TU/TR/RS/PR/MI)的 `assumptions.md` + `examples.md`;邻居域数据驱动浮现(散文里被这些域引用/链接到的其他域,纳入一跳)。

**三个抽取器**:
1. **显式链接 `explicit_link`(确定性正则)**: 扫 examples/spec 里的 RELREC / `--LNKID` / `--LNKGRP` / `SUPP--` 用法与 "### Related Domains" 中带机制词的 bullet,产出带机制的跨域链接。`extractor="regex"`, `verified=true`(确定性命中即真)。
2. **数据流 `data_flow`(LLM + 证据)**: 对每对簇内(及一跳邻居)域,给 LLM 两域的相关散文,要求产出**有向**关系 + **逐字引文** + 关系短语 + 置信度。Prompt 强约束:引文必须逐字来自给定文本;判不出就返回空,**不许编**。
3. **共现 `co_occurrence`(确定性计数)**: 统计两域在同一 example/assumption 文件/段落中共同出现的频次;`extractor="count"`, `verified=true`。

**防幻觉 + 核验(两道,针对 data_flow)**:
- **闸 1 · 确定性引文校验**: 每条 LLM 边的 `evidence.quote` 必须作为子串**逐字命中**其 `source_file`;命中不了直接丢(廉价地灭掉编造引文)。
- **闸 2 · 对抗核验(Rule D 隔离)**: 独立 subagent/LLM 拿到 {引文, 声称的有向关系, 两域},被要求**尽力反驳**("这段引文是否真支持这条有向关系?方向对吗?不确定就判 refuted")。refuted 的边丢弃或标 `verified=false` 收起。
- 低于置信阈值(默认 0.6,写进管线常量)的边默认在 UI 收起。

**产物**:
- `data/meta/implicit_relations.json`(schema 见 §4)。
- `evidence/checkpoints/implicit_relations_audit.md`: **Rule A** N=8 分层人工抽检(每类抽样,逐条核对引文是否支持关系、方向是否对),留证。

## 4. 数据契约 — `implicit_relations.json`

```jsonc
{
  "meta": {
    "version": 1,
    "cluster_seeds": ["TU","TR","RS","PR","MI"],
    "domains": ["TU","TR","RS","PR","MI", "...一跳邻居"],
    "generated_from": "knowledge_base/domains/<D>/{assumptions,examples}.md",
    "confidence_threshold": 0.6
  },
  "edges": [
    {
      "id": "flow:PR>TR:0",
      "source": "PR", "target": "TR",
      "kind": "data_flow",            // data_flow | explicit_link | co_occurrence
      "directed": true,               // co_occurrence=false
      "relation": "measurements recorded in",  // 自由短语 / explicit_link=机制(RELREC…) / co_occurrence=null
      "evidence": {
        "quote": "…the tumor measurements obtained via the procedure are recorded in the TR dataset…",
        "source_file": "knowledge_base/domains/PR/examples.md",
        "line": 142
      },
      "confidence": 0.82,
      "extractor": "llm",             // llm | regex | count
      "verified": true,               // 通过闸1+闸2 / regex,count 恒 true
      "verify_note": "verifier: quote directly supports PR→TR direction"
    }
  ]
}
```
`co_occurrence` 边的 `evidence` 用共现位置列表 + `confidence` 由频次归一;`explicit_link` 边 `evidence` 指向那条 RELREC/link 行。

## 5. 组件 B — 查看器 explore 模式(网状点击展开)

在现有 `build_kg_viewer.py`/`kg_viewer.html` 上**新增 explore 模式**(保留 3 个固定视图作快捷预设):
- **展开**: 种子起,点节点 → 把其邻居**增量加到画布**(不换视图);默认加上限 K=12,按优先级(硬边邻居 > 高置信推断邻居),"展开更多"加其余。
- **收起 / 聚焦**: 再点已展开节点 → 移除其独占叶子;"聚焦"隔离某节点邻域。
- **两层边视觉编码**(线型带义,非仅颜色):硬结构=灰实线;数据流=蓝实线+箭头(有向);显式链接=绿虚线;共现=紫点线。
- **图层开关** + **置信度滑条**(过滤推断边);防毛线球。
- 力导向布局(复用现有引擎)。

## 6. 组件 C — 富节点(混合详情)

- 点节点 → 详情面板(进化现有面板):**离线内嵌**结构化详情——域: label/类/结构/变量清单 + **assumptions 摘要**(取首段/短抽);变量: CDISC Notes/角色/core/码表;码表: 名称/可扩展/术语数(术语列表按需)。
- **关系分层展示**: 硬(结构)+ 推断(数据流/链接/共现)各带标签,推断项显示置信度 + ✓核验。
- **"深入解释 / 为何相关"按钮**: 启动时 `fetch(:8000/api/health)` 探活;在线则调 `/api/ask`(模板问题,如"In SDTM, explain how PR relates to TR and why")展示答案;离线自动隐藏。
- **点推断边** → 证据弹窗: 引文 + 来源文件:行 + 置信度 + 核验状态。

## 7. 组件 D — 数据血缘 / 硬软分层

`build_kg_viewer.py` 读 `meta.yaml`(硬,经 extract_graph)+ `implicit_relations.json`(软),把两层边都内嵌进 `kg_viewer.html`,UI 上视觉与图层分离。**软层永不改动 meta.yaml**;两者各自独立可重生成。

## 8. 分单元与文件清单(供实现计划)

| 单元 | 文件 | 动作 |
|---|---|---|
| U1 抽取器·显式链接 | `scripts/mine_implicit_relations.py` (regex 部分) | 新增 |
| U2 抽取器·共现 | 同上 (count 部分) | 新增 |
| U3 抽取器·数据流 + 两道核验 | 同上 (llm + verify) | 新增 |
| U4 产物 + 审计 | `data/meta/implicit_relations.json`, `evidence/checkpoints/implicit_relations_audit.md` | 生成 |
| U5 查看器·两层边 + explore 模式 | `scripts/build_kg_viewer.py` (数据内嵌 + JS) | 改 |
| U6 查看器·富节点混合详情 + RAG 按钮 + 边证据 | 同上 | 改 |
| U7 测试 | `scripts/tests/test_mine_implicit_relations.py` | 新增 |

> 注: `build_kg_viewer.py` 的 HTML 模板已偏大;实现时若 JS/CSS 继续膨胀,把模板拆成独立 `viewer/{template.html,app.js,style.css}` 于 build 时内联,保持单文件产物但源码可维护。

## 9. 测试与核验

- **确定性测试**(pytest): 引文逐字命中校验;显式链接正则 golden(簇内已知 RELREC);共现计数;JSON schema 合法。
- **Rule A 语义抽检**: N=8 分层抽样 data_flow 边,独立核对引文↔关系↔方向,留 `implicit_relations_audit.md`。
- **Rule D 隔离**: 抽取(writer)与对抗核验(reviewer)走不同 subagent,不同 session。
- **查看器**: 起本地静态服务 + 浏览器截图逐视图核验(explore 展开/收起、两层边、富节点、边证据、RAG 按钮在线/离线)。
- **失败归档(Rule B)**: 被核验毙掉的边归档到 `failures/`,不删(复盘用)。

## 10. 成功标准(验收)

从 **TU** 出发点击展开,能看到 **PR→TR/MI→RS→TU** 的有向推断边;**每条推断边点开都有可核验的 IG 逐字引文 + 置信度 + 核验状态**;能开关硬/软图层、拖置信滑条;点节点看混合详情;(联网时)能让 RAG 解释"为什么 PR 喂给 TR"。Rule A 抽检 PASS。

## 11. 风险与开放问题(实现计划期定)

- LLM 数据流抽取的置信阈值、每对域最多保留几条边(默认 0.6 / 每对 ≤2)——试点后据抽检结果调。
- 展开上限 K、低置信默认收起策略的手感。
- 抽取/核验用模型(默认 deepseek,与现有 Router 一致)。
- 共现的粒度(文件级 vs 段落级)。
- 邻居域"一跳"的纳入边界(避免簇膨胀)。
