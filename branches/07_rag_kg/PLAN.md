<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝)
  修改本文件后, 必须检查:
  → branches/07_rag_kg/_progress.json              (Phase 進捗真源, 同步更新)
  → branches/07_rag_kg/CHANGELOG.md                (改訂履歴記録)
  → branches/07_rag_kg/EXECUTION_PLAN.md           (HOW 落地方案, 整合性確認)
  → ../../.work/MANIFEST.md                        (入口登録 + Chain 07_RAG 追加)
  → ../../docs/PROGRESS.md                         (Phase 7 状态格更新)
  → ../../CLAUDE.md Key Paths                      (新規 Key Path 1 行追加, ≤ 80 字符)
  → ../../docs/DESIGN_RAG_KG.md                    (上游设计, 不修改但本 PLAN 偏离时必须 cross-ref)
-->

# branches/07_rag_kg/ — RAG + Knowledge Graph 落地实施計画

> 创建: 2026-05-22
> 状态: **DRAFT v0.2** — Phase 0 Research 完成 (chunker feasibility + LLM providers) + critic Rule D PASS 1 CONDITIONAL_PASS 32 findings 主要 HIGH/MED 已修, 用户 ack 待
> v0.1 → v0.2 修订 (2026-05-22): F-1 PASS 术语对齐 / F-2 chunker 事实错误同步 (4 处) + domains 数 63→64 / F-3 加 R-13~R-19 / F-6 V4-Pro Reasoner / F-7 Haiku context / F-9-F-11 运维 risk / F-14 reingest trigger / F-19-F-21 工期调整 / F-23-F-24 PASS 按 Phase + 规则 A 抽检 N 明示 / F-27 1C reviewer.py / F-32 06 P7 表述歧义
> 上游设计 (WHAT/WHY): [`docs/DESIGN_RAG_KG.md`](../../docs/DESIGN_RAG_KG.md) (Approved 2026-04-16)
> 本文件职责 (HOW 简版 + 落地化调整): 把设计文档对齐本项目当前 KB 真实状态 + 落到可执行的 Phase 拆分
> 详细 HOW (agent 配役 / 并行机会 / Rule D 隔离): [`EXECUTION_PLAN.md`](EXECUTION_PLAN.md)
> Tier: **2** (5-15 step, borderline 3; 走 Tier 2 模板 + evidence 全留)
> 受信者: 本人 (SDTM 自查) + 团队 (内部服务) + 技术探索 (向量库/知识图谱学习)

---

## 0. Charter

### 0.1 目的 (Why)

为 SDTM 知识库 (296 md / 9.8MB / 06 P7 字段验证 atom coverage 99.02% / Issues 5-16 已修复) 建立**智能检索 + 数据集校验**系统, 包含三大能力:

1. **语义问答** — 自然语言提问, 带溯源回答
2. **关系发现** — 跨域查询、CT 影响分析 (Phase 2 KG, defer 决策点见 §5)
3. **数据集校验** — 用户上传 SDTM 映射数据集 (CSV/XPT/SAS7BDAT), 自动出完整性 + 规则合规报告

### 0.2 範圍 (Scope)

**In-scope (Phase 1)**:
- RAG pipeline (chunking + embedding + Chroma + LiteLLM + FastAPI + Streamlit)
- 数据集校验 (规则引擎 + RAG 语义评审 + 报告生成)
- 本地优先 (Docker Compose 一键)
- 多 LLM provider (DeepSeek V4 + Anthropic + OpenAI 接口预留)
- 50 题 eval 测试集

**In-scope (Phase 2, defer 决策见 §5)**:
- P3 meta.yaml 生成 (从 spec.md + Cross References 自动派生)
- Neo4j 知识图谱
- 混合路由 (CONCEPT/RELATION/HYBRID)
- 图增强校验

**Out-of-scope**:
- 云部署 (Vercel/AWS/其他, 设计 §8 列, defer 到 Phase 1 上线后)
- **用户认证 / 多租户 (F-13 v0.2 明示)**: Phase 1 设计为**单用户/单租户**, FastAPI uvicorn `--workers 1`; 多用户并发 + 用户认证 defer 到云部署阶段
- 知识库自动同步管道 (KB 更新 → 自动 reingest, runtime 用 R-18 git HEAD 比对 warn 替代)
- SDTM 多版本管理 (仅 v3.4)
- 修改 `knowledge_base/` 任何内容 (硬约束 H-1: knowledge_base/ 严格只读)

### 0.3 不做 (Non-Goals)

- ❌ 不是要替代 LLM 直接读 KB — 是给 LLM 提供过滤后的精准 context
- ❌ 不是要做通用 SDTM tutorial — 是给已经懂 SDTM 的用户做查询/校验工具
- ❌ 不是 Phase 1 一次性把 KG 也做了 — KG 推到 Phase 2 单独评估
- ❌ 不是要把 ChatGPT Plus 包装成生产 API — 详见 §4.2 决策

---

## 1. 上游设计回顾 + 本 PLAN 的 3 处落地化调整

设计文档 `docs/DESIGN_RAG_KG.md` (2026-04-16 Approved) 的方向**完全保留**, 本 PLAN 仅在以下 7 处做落地化调整 (有 research/ evidence 支撑):

| # | 设计文档原方案 | 本 PLAN 调整 | 依据 |
|---|--------------|-------------|------|
| **A-1** | examples.md "Per Example heading (with full data table)" | **domain-aware chunker** — 探测每个 examples.md 最深 heading level (TA 用 H2 `## Example N`, PC 用 H4 `#### Method A-D` 嵌套, 14 chunk 不是 16), 不能写死 `### Example` | [research/chunker_feasibility_2026-05-22.md §3.2](research/chunker_feasibility_2026-05-22.md) |
| **A-2** | ROUTING.md 整体注入 system prompt | **ROUTING.md (2K tok) + INDEX.md (4K tok) 都整体注入 system prompt** — INDEX.md 设计文档未提, 但 4K token 完全可塞, 给 LLM 全 64 域 + 6 chapters + 91 terminology 入口映射 | research/chunker_feasibility_2026-05-22.md §7.2 |
| **A-3** | LLM "Provider-agnostic via LiteLLM" 默认 OpenAI text-embedding-3-small + Claude/GPT-4o | **default LLM = `claude-sonnet-4-6`** (RAG 主答, 1M context, $3/$15) + `deepseek-v4-flash` 复检 + `claude-opus-4-7` 难题 + `claude-haiku-4-5` 轻分类 + `openai/` 接口预留 (不接 Plus 代理) | [research/llm_providers_2026-05-22.md §6](research/llm_providers_2026-05-22.md) |
| **A-4** (v0.2 新增) | VARIABLE_INDEX "Split by alphabetical groups" | **按 §一 通用变量 1 chunk + §二 63 域 H3 各 1 chunk + §三 字母段 ~5 chunk** (实测 §二 是按 domain 分 H3 组, 不是字母组; 63 H3 不是 24) | chunker_feasibility §8 |
| **A-5** (v0.2 新增) | chapters "By `##` section, large sections split at `###`" 二档 | **三档 size-aware**: > 50KB → `###` 切 (ch04 130KB), 20-50KB → `##` 切 (ch08 52KB), < 20KB → 整文件 1 chunk (ch01 11KB) | chunker_feasibility §4 |
| **B-1** | Step 4 数据集校验 → Step 6 评测 | **eval 提前到 Step 2 (ingest) 后** — 20 题 sanity eval baseline, Step 5 (校验) 后扩 50 题完整 eval. 避免最后才发现召回拉胯 | 工程经验判断 (无强 evidence; 06 P5-P6 验证后修复成本高也是侧证) |
| **B-2** | Phase 2 (KG) Step 7-12 顺序衔接 | **Phase 2 默认 defer**, 决策点 = Phase 1D eval 完成后 RELATION 类 12 题召回 < 50% 才启动 | 个人判断 + 成本/价值评估; **50% 阈值非锁死**, Phase 1D 后 main + Bojiang 复评 |

---

## 2. Architecture (本项目落地版)

设计文档 §2 的总架构图保留 (`sdtm-rag/` 仓库布局), 本 PLAN 1 处偏离:

### 2.1 仓库位置 (设计偏离)

**设计文档**: 暗示独立项目 (`sdtm-rag/` sibling)
**本 PLAN**: **`branches/07_rag_kg/sdtm-rag/`** (此 branch 内部子目录)

理由 (用户 2026-05-22 ack):
- 跟 SDTM-pedia 项目命运绑在一起, 更好审计 / git history 同步
- KB 变更触发 reingest 时, 同 git tree 内一键脚本即可
- 与 06 / jp_delivery / 07 website 旁枝并列, 符合项目结构惯例

### 2.2 子目录树 (本 PLAN 落地版)

```
branches/07_rag_kg/
├── PLAN.md                  (本文件, WHAT/WHY + 落地化调整)
├── EXECUTION_PLAN.md        (HOW: agent 配役 + 并行 + Rule D 隔离)
├── CHANGELOG.md             改訂履歴
├── _progress.json           Tier 2 進捗真源
├── RETROSPECTIVE.md         (Phase 1 收口必写, 规则 C)
├── research/                Phase 0 Research evidence (完成)
│   ├── chunker_feasibility_2026-05-22.md
│   └── llm_providers_2026-05-22.md
├── evidence/
│   ├── checkpoints/         每 Phase 关闭时 evidence 归档
│   └── failures/            规则 B: 失败 attempt 归档
├── prompts/                 subagent kickoff prompt 模板
└── sdtm-rag/                ★ Phase 1A 起开始建, 实际代码仓
    ├── scripts/
    │   ├── ingest.py
    │   ├── chunkers/           ★ chunker 按文件类型分模块 (本 PLAN 强化)
    │   │   ├── base.py
    │   │   ├── spec.py
    │   │   ├── assumptions.py
    │   │   ├── examples.py     ★ domain-aware
    │   │   ├── chapters.py     ★ size-aware
    │   │   ├── model.py
    │   │   ├── terminology.py  ★ LB-part 模式识别
    │   │   └── variable_index.py
    │   ├── tests/              ★ chunker 测试套件 (Phase 1A 必写)
    │   ├── parse_dataset.py
    │   └── shared/
    ├── server/
    │   ├── main.py
    │   ├── router.py
    │   ├── rag.py
    │   ├── validator.py
    │   ├── reviewer.py
    │   ├── llm_config.py       ★ LiteLLM Router 配置 (引用 llm_providers §5)
    │   └── config.py
    ├── ui/
    │   └── streamlit_app.py
    ├── data/
    │   └── chroma/             (.gitignore)
    ├── eval/
    │   ├── test_set_v0.yml     ★ 20 题 sanity (Phase 1B5)
    │   ├── test_set_v1.yml     50 题完整 (Phase 1D)
    │   └── run_eval.py
    ├── docker-compose.yml
    ├── pyproject.toml
    └── README.md
```

---

## 3. KB 规模与 chunk 总数预期 (基于 T3 实测, v0.2 修订)

| 类别 | 文件数 | 估算 chunk 数 | 风险 |
|------|--------|-------------|------|
| spec.md (63 文件, DI 缺, 实测 2164 变量) | 63 | **2164** | LOW |
| assumptions.md (**64 文件**, DI 含, 412 numbered items + overviews) | 64 | ~460 | LOW |
| examples.md (63 文件, DI 缺, domain-aware) | 63 | ~500 | **HIGH** (A-1) |
| chapters/ (size-aware 三档) | 6 | ~90 | MED |
| model/ | 6 | ~35 | LOW |
| terminology/ (实测 1005 codelists; lb_part1-4 4 件含 part4 多 1 H2) | 91 | ~1050 | MED |
| VARIABLE_INDEX.md (**63 H3 by domain** + §一 + §三 5) | 1 | ~69 | LOW |
| ROUTING.md + INDEX.md (整体注入) | 2 | 0 | — |
| **TOTAL** | **296** | **~4368 chunks** (± 5%) | — |

落在设计 §3.4 估算的 "3000-5000 chunks well within Chroma's capacity" 中段。注: KB 总 .md 实测 296 件 (CLAUDE.md 写 293 是早期数, 不准)。**Phase 1A.0 sanity** 启动前 main session 必须 re-grep verify chunker_feasibility §13 6 项未验证项 (不信任本估算)。

---

## 4. 关键技术决策表

### 4.1 数据层

| 项 | 选择 | 理由 |
|----|------|------|
| Vector DB | **Chroma** (本地, `pip install chromadb`) | 设计 §3.4, 3-5K chunks 远低于上限, 零运维 |
| Embedding (D-4 **v2** 2026-05-22) | **bge-m3 (1024d, local sentence-transformers)** ★ | 用户决策不开 OpenAI API account; Mac M-series MPS 推理 ~ms 级 (1A.2.f 实测); $0 API 成本; 首次 ~2.5GB 下载 |
| Embedding fallback (留接口暂不调) | OpenAI `text-embedding-3-small` (1536d) | `llm_config.py` 留 `openai/` base_url 配置化接口 (D-3); 用户后续若开 OpenAI API account 或决定切回, 一行 `.env` (`SDTM_RAG_EMBEDDING_MODEL=openai/...`) 切换 |
| Embedding 不选 | text-embedding-3-large / Cohere v3 | 仅当 1B5 eval 显示 bge-m3 召回 < 80% 才考虑 (Cohere 需另开账户) |

### 4.2 LLM 层 (引用 research/llm_providers_2026-05-22.md)

| 场景 | 主模型 | Fallback | 单位成本 |
|------|--------|----------|---------|
| RAG 主答 | `anthropic/claude-sonnet-4-6` (1M ctx) | `deepseek/deepseek-v4-pro` **非思考** (D-4 v2) | $3/$15 → DeepSeek V4-Pro 非思考 (用户持 V4-Pro API key) |
| 难题语义评审 / dataset reviewer.py | `anthropic/claude-opus-4-7` (1M ctx) | `anthropic/claude-sonnet-4-6` | $5/$25 → $3/$15 |
| 轻量分类 / intent 路由 | `anthropic/claude-haiku-4-5` | `deepseek/deepseek-v4-pro` **非思考** (D-4 v2) | $1/$5 |
| 复检 / cross-check | `deepseek/deepseek-v4-pro` **非思考模式** (D-4 v2; 绕开 LiteLLM Issue #26395 multi-turn bug) | — | per DeepSeek pricing |
| 批量 eval | `anthropic/claude-sonnet-4-6` Batch API | — | $1.50/$7.50 (50% 折扣) |
| OpenAI API + ChatGPT Plus | ❌ **不接入生产** (D-3 + D-4 v2 联合) — Plus 代理 ToS+稳定性 risk (llm_providers §3) + OpenAI API account 用户暂不开; embedding 主路径改 bge-m3 local (§4.1); 留 `openai/` base_url 接口预留 | — | — |

**OpenAI 决策 (D-3 + D-4 v2 联合, 2026-05-22 用户 ack)**:
- ❌ **ChatGPT Plus 代理**: 不纳入 LiteLLM Router default fallback chain — 违反 OpenAI ToS, 极低稳定性, 数据安全风险高
- ❌ **OpenAI API account**: 用户暂不开通; **embedding 主路径改为 bge-m3 local** (§4.1 D-4 v2) — bge-m3 1024d sentence-transformers, Mac MPS, $0 API, ~2.5GB 下载
- ✅ 在 `llm_config.py` 留 `openai/` provider 接口 (base_url 配置化), 用户后续若开 OpenAI API account **或决定切回 OpenAI embedding**, 一行 `.env` (`SDTM_RAG_EMBEDDING_MODEL=openai/text-embedding-3-small` + `OPENAI_API_KEY=...`) 切换
- ✅ daily prototype / 人工测试 → 用户直接在 chatgpt.com 网页用 Plus 配额, 不强行 API 化
- ✅ 详细折中建议在 `llm_providers_2026-05-22.md §3.折中建议`

### 4.3 框架层

| 项 | 选择 | 理由 |
|----|------|------|
| LLM Abstraction | **LiteLLM v1.85.1+** (Python SDK Router) | 设计 §3.6, 支持 deepseek+anthropic+openai 同 router |
| API 层 | **FastAPI** | 设计 §2, Python RAG 生态标准 |
| 前端 | **Streamlit** | 设计 §3.7, MVP 速度最快 |
| 数据集解析 | **pandas + pyreadstat (XPT/SAS7BDAT)** | Python 生态标准 |
| 容器化 | **Docker Compose** (Chroma + FastAPI; Phase 2 +Neo4j) | 设计 §2, 本地一键 |

### 4.4 已知 LLM 集成风险 (来自 llm_providers §2)

| 风险 | 影响 | 缓解 |
|------|------|------|
| LiteLLM Issue #26395 (DeepSeek V4 Pro multi-turn thinking 模式 reasoning_content 被剥除 → 第二轮 400) | RAG multi-turn 用 V4-Pro 思考模式会断 | Phase 1B 主用 Sonnet, 复检用 `deepseek-v4-flash` 非思考模式; Phase 1A 写代码前先 `pip install litellm==1.85.1` 跑 2 轮对话 sanity |
| DeepSeek V4-Pro 75% 折扣 2026-05-31 到期 | 价格可能上涨 | 2026-06-01 后重查 pricing, 必要时切 V4-Flash |
| LiteLLM v1.84.0 breaking changes (proxy multi-pod) | 单机 SDK 模式可能不影响 | 用 Python SDK Router 不用 proxy server, 规避 |

---

## 5. Phase 拆分

### Phase 0 — Research (本 Phase, 进行中)

| Step | 内容 | Owner | 状态 |
|------|------|-------|------|
| 0.1 | 旁枝骨架创建 (T1) | main | ✅ done |
| 0.2 | LLM providers 调研 (T2) | document-specialist (bg) | ✅ done |
| 0.3 | Chunker feasibility 调研 (T3) | main | ✅ done |
| 0.4 | PLAN.md 起草 (T4) | main | 🟢 in_progress |
| 0.5 | EXECUTION_PLAN.md 起草 | main | pending |
| 0.6 | Writer/reviewer 分离审 (T5, Rule D) | architect 或 critic 异 subagent_type | pending |
| 0.7 | 用户 ack | Bojiang | pending |
| 0.8 | Phase 0 closure commit | main | pending |

**Phase 0 PASS 五条**:
1. evidence: research/ 2 份报告齐全 + 不含 [UNVERIFIED] 未标注的猜测
2. writer 产物: PLAN.md + EXECUTION_PLAN.md 引用 evidence + 决策有依据
3. 独立 reviewer subagent PASS (Rule D: writer=main, reviewer=architect/critic 异 type)
4. 用户 (Bojiang) 口头 ack
5. 不启动 Phase 1A 前: jp_delivery 01 v1.1-draft 未提交改动用户独立处理 (本 PLAN 不绑定)

### Phase 1A — Ingest (前置: Phase 0 PASS)

**性质**: chunker + embedding + Chroma 离线管道。**最大风险在 examples.md chunker (A-1)**。

| Step | 内容 | 工期 | PASS 条件 |
|------|------|------|----------|
| **1A.0** (v0.2 新增) | Phase 1A.0 sanity: re-grep verify R-13 6 项 (supplementary_part / qs_part / questionnaires / mermaid 嵌套 / table 变体 / tiktoken 实测) | 0.3 d | 6 项数字落实到 chunker config, 1A.3 不带未验证假设进 |
| 1A.1 | `sdtm-rag/` 仓库脚手架 (pyproject + Docker Compose + 目录树 + .env/.env.example/.gitignore R-17) | 0.3 d | structure OK + chromadb 起 + .env 不入库 |
| 1A.2 (D-4 v2 修订) | LiteLLM v1.85.1 sanity: (a) DeepSeek **V4-Pro 非思考模式** 2 轮 [用户主用] + V4-Pro 思考 1 轮 [verify Issue #26395 R-8 single-turn], (b) Sonnet 2 轮, (c) Router fallback chain 2 轮 Sonnet → V4-Pro 非思考 (R-19), (d) Haiku context window 实测 (R-14), (e) **bge-m3 sentence-transformers 安装 + ~2.5GB 下载 + 5 sample text embedding + Mac MPS 速度 < 100ms/chunk (R-22)** | **0.5 d** | 都跑通, bug 规避确认 (V4-Pro 非思考 ok); bge-m3 dim 1024 + MPS 速度达标 |
| 1A.3 | chunker base + 6 类实现 (spec/assumptions/examples/chapters/model/terminology) + variable_index | 1.5 d | 单元测试覆盖 (见 §6) |
| 1A.4 | chunker 测试套件 (TA/PC/IS/DS examples + LB part1-4 + ch04 + supplementary_part) | 0.7 d | 100% PASS + 边界 byte-exact + 含失败回归 |
| 1A.5 | ingest.py 全量跑 + Chroma persistence + backup ckpt (R-16) + ingested_at_commit.txt (R-18) | 0.5 d | ~4368 chunks 全入库, sample 10 个查询验证 retrieval 召回 |
| 1A.6 | 规则 A 抽检 (PASS 五条 4.a): 06 P5 reverse_ledger.jsonl 抽 N=10 SOURCED atom 与 chunk 边界对齐验证 | 0.2 d | ≥9/10 chunk-atom 边界吻合 |

**工期**: 3-4 工作日 (含 1A.0 sanity + 1A.1 .env + 1A.4 失败回归 + 1A.5 backup)

### Phase 1B — Q&A 服务 (前置: 1A PASS)

| Step | 内容 | 工期 |
|------|------|------|
| 1B.1 | FastAPI router + ROUTING.md + INDEX.md 整体注入 system prompt | 0.5 d |
| 1B.2 | rag.py: metadata filter + 语义 Top-K=15 + (可选) Cohere Rerank Top-5 | 0.5 d |
| 1B.3 | LiteLLM Router 集成 (Sonnet 主 + Deepseek Flash fallback) | 0.5 d |
| 1B.4 | Streamlit UI 极简 (chat + 溯源展开) | 0.5 d |

**工期**: 2 工作日

### Phase 1B5 — Sanity Eval (本 PLAN 新增, 提前到 1C 前)

20 题手工 ground truth: 单域 5 + 跨域 5 + 概念 5 + 混合 5

| Step | 内容 | 工期 |
|------|------|------|
| 1B5.1 | 写 20 题 ground truth (yml 格式, 答案 + 期望溯源文件) | 0.5 d |
| 1B5.2 | run_eval.py baseline 跑分 | 0.2 d |
| 1B5.3 | 若召回 < 80% 回头调 chunk size / Top-K / 重排 | 0-1 d (按需) |

**工期**: 0.7-1.5 工作日

### Phase 1C — 数据集校验 (核心价值, 设计 §4, 工期 v0.2 调整 F-20)

| Step | 内容 | 工期 |
|------|------|------|
| 1C.1 | parse_dataset.py: CSV / XPT / SAS7BDAT via pandas + pyreadstat (R-20 fallback sas7bdat); 文件大小 100MB 上限 + chunksize=10000 流式 | 0.5 d |
| 1C.2 | validator.py 规则引擎 (7 类): Req/Exp/CT/Type/主键/USUBJID/变量名 + 边界 case (空表 / 重复主键 / 缺列 / 类型不匹配 / Date 格式) | **1.5-2 d** |
| 1C.3 | reviewer.py RAG 语义评审 (5 类): 业务规则 + 逻辑一致 + pattern 比对 + 完整性 + 跨域关系; Opus 4.7 评估; 假错误集 20 例设计 + 标注 (规则 A 抽检 PASS 五条 4.d) | **1.5 d** |
| 1C.4 | 报告生成: Markdown + JSON, 完整性 % + ERROR/WARN/INFO 分级 | 0.5 d |
| 1C.5 | 上传 UI 集成到 Streamlit + st.status/progress 60s timeout (R-21) | **0.5-1 d** |

**工期**: 5-6 工作日

### Phase 1D — Full Eval

| Step | 内容 | 工期 |
|------|------|------|
| 1D.1 | 扩到 50 题 (设计 §6.1 四类各 12 题) + 校验场景 5 题 | 1 d |
| 1D.2 | 跨模型对比 (Sonnet vs Opus vs DeepSeek V4-Pro) | 0.5 d |
| 1D.3 | 评 correctness/citation/recall, 出 report | 0.5 d |

**工期**: 2 工作日

### Phase 1 收口

| Step | 内容 | 工期 |
|------|------|------|
| 1.收.1 | RETROSPECTIVE.md 三段齐备 (规则 C) | 0.3 d |
| 1.收.2 | Docker Compose 一键起部署文档 | 0.2 d |
| 1.收.3 | Phase 2 决策点评估 (RELATION 类 12 题召回, 决定是否启 Phase 2) | 0.5 d |

**工期**: 1 工作日

### Phase 1 总工期

**10-13 工作日** (单人, 含 Tier 2 evidence/failures/audit 留档)

### Phase 2 — KG (decision-gated)

**启动条件 (本 PLAN 新增 gate)**: Phase 1D eval 完成后 **RELATION 类 12 题召回 < 50%** 才启动。否则 KG 推到 Phase 1 上线 + 实测 1-2 周后再评估。

如启动, Phase 2 工期约 6-8 工作日:
- Step 7: P3 meta.yaml 生成 (脚本从 spec.md + Cross References 派生 63 域) — 2 d
- Step 8: Neo4j Docker + build_graph.py 导入 — 1 d
- Step 9: graph.py LLM → Cypher → Neo4j → format — 1.5 d
- Step 10: router.py 意图分类 + CONCEPT/RELATION/HYBRID 三路融合 — 1 d
- Step 11: 图增强校验 (跨域依赖 + CT cascade) — 1 d
- Step 12: eval 扩展 + Phase 2 PASS — 1 d

**注**: P3 meta.yaml 是 KG 启动硬前置, 也同时是 jp_delivery 02 §3.4/§3.5 粒度议的同源数据 — 一举两得。

---

## 6. Chunker 实现规范 (来自 research/chunker_feasibility §3-§8)

### 6.1 spec.md / assumptions.md / model/ — Simple

```python
# spec.md: regex split by ^### , 1 chunk per variable
# assumptions.md: 顶部 Description = 1 chunk + numbered items 各 1 chunk + table 不切
# model/: regex split by ^## , 1 chunk per section
```

测试: 各 sample 5 文件 verify chunk 边界 + metadata 字段。

### 6.2 examples.md — ★ 最高风险, domain-aware

```python
class ExamplesChunker:
    def chunk(self, file_path: Path) -> list[Chunk]:
        # 1. 探测最深 heading level (H2/H3/H4)
        # 2. 按 Example heading 切 (level 自动决定)
        #    - TA: H2 "## Example N" (8 examples + 1 "## Trial Arms Issues")
        #    - PC: H4 "#### Method A-D" (16 Method × 4 Example = 16 chunks)
        # 3. split point 保护:
        #    - ```mermaid ... ``` 整体不切
        #    - | ... | table 块整体不切
        # 4. metadata: domain, cdisc_section_id, example_index, sub_label (e.g., "Method A"),
        #              has_mermaid (bool), has_table (bool), chunk_size_tokens
```

**测试套件 (必写, Phase 1A.4 通过条件)**:
- TA examples.md (mermaid 20 + table 157 行) — 8 chunk, 0 mermaid 被切
- PC examples.md (H4 嵌套, 16 Method) — 16 chunk
- IS examples.md (单行密集 95 table 行) — table 不被切
- DS examples.md (11 H2 扁平) — baseline

### 6.3 chapters/ — size-aware

```python
# > 50KB → 按 ### sub-section 切 (e.g., ch04 130KB → 38 chunks)
# 20-50KB → 按 ## section 切 (e.g., ch08 52KB → 10 chunks)
# < 20KB → 整文件 1 chunk (e.g., ch01 11KB)
```

### 6.4 terminology/ — LB part 模式识别

```python
class TerminologyChunker:
    def chunk(self, file_path: Path) -> list[Chunk]:
        # 1. 默认: 按 ^## codelist 切, 每 codelist = 1 chunk (含表格)
        # 2. LB part 兜底: 文件名匹配 *_part[0-9]+.md 且 H2 count == 1:
        #    → 整 part 文件 = 1 chunk, metadata 标 part_index (lb_part1/2/3 适用)
        # 3. LB part4 异常 (H2 count = 2, 1.7KB 小文件, 不是 codelist 内部切片):
        #    → 按默认 ^## codelist 切 = 2 chunk
        # 4. 巨型 codelist (单 codelist chunk > 6K token): 按 N=100 table row 切片,
        #    metadata 加 table_chunk_idx
        # 5. metadata: codelist_code (e.g., "C65047"), codelist_name, ct_extensible,
        #              parent_domain (LB/QS/supplementary/...), part_index?, table_chunk_idx?
```

### 6.5 VARIABLE_INDEX.md / ROUTING.md / INDEX.md

```python
# VARIABLE_INDEX.md (A-4 偏离):
#   - §一 通用变量 = 1 chunk
#   - §二 每个 ### 域 = 1 chunk (63 H3 chunks, v0.1 误写 24)
#   - §三 CT 交叉引用 = 按字母段切 ~5 chunk

# ROUTING.md (8KB / 2K token) + INDEX.md (16.7KB / 4K token):
#   - 不切, 整体注入 system prompt (合计 ~6K token base)
```

---

## 7. Chunk Metadata Schema (落地版, 扩展设计 §3.2)

```python
{
    # 基本 (设计 §3.2)
    "source": "domains/AE/spec.md",
    "domain": "AE",
    "class": "Events",
    "file_type": "spec",        # spec | assumptions | examples | chapter | model | terminology | variable_index
    "section": "AETERM",
    "chunk_index": 0,

    # 本 PLAN 扩展 (chunker_feasibility §12)
    "cdisc_section_id": "§6.3.5.9.3",   # 引用 06 P5 reverse_ledger 同款 section id
    "example_index": null,               # examples.md 专用 (1-7)
    "sub_label": null,                   # PC examples "Method A-D" 专用
    "has_mermaid": false,                # examples.md 含 mermaid 块
    "has_table": false,
    "ct_code": null,                     # terminology 专用 codelist code
    "ct_extensible": null,
    "part_index": null,                  # terminology LB part1/2/3 专用
    "table_chunk_idx": null,             # 巨型 codelist 按行切时
    "chunk_size_tokens": 1234,           # tiktoken 实测

    # KB 版本追踪 (本 PLAN 强化, R-7)
    "kb_commit_sha": "abc123...",        # ingest 时 KB git HEAD
    "ingest_at": "2026-MM-DD"
}

# F-15 v0.2 明示: schema 字段约定
# - 所有上方字段一律 fill, 不适用时存 None (Python null), 不省略字段
# - 理由: Chroma metadata filter 时 `where: {field: null}` 与 missing field 行为不同;
#   全量 fill 后 chunker 测试套件断言完整性也更直接
```

---

## 8. 风险清单 (v0.2 扩展)

来源: research/chunker_feasibility §10 + research/llm_providers §2 + critic Rule D PASS 1 finding F-3/F-7/F-9-F-11/F-14

| # | 风险 | 影响 | 概率 | 严重性 | 缓解 | 验证 Phase |
|---|------|------|------|-------|------|------------|
| R-1 | examples.md heading level domain-specific (PC H4 嵌套) | examples chunker | 100% (已确认) | HIGH | domain-aware chunker + 配置 | 1A.4 |
| R-2 | TA mermaid + table 混排切分边界 | TA + DM examples | 100% | HIGH | split point 保护 + 测试套件 | 1A.4 |
| R-3 | LB part 文件命名 + part4 异常 (2 codelist) | LB 系列 terminology | 100% | MED | terminology chunker 识别 part 模式 + part4 兼容 | 1A.4 |
| R-4 | ch04 130KB 单 ## section 超 8K token 限 | ch04 only | 100% | MED | ch04 直接按 ### 切 | 1A.4 |
| R-5 | VARIABLE_INDEX 与 spec.md 召回重复 | 跨变量查询 | 待 eval 验 | LOW-MED | Phase 1B5 实测后决定 boost 或剔除 | 1B5 |
| R-6 | 06 P5 reverse_ledger 与 chunk 边界对齐 | chunker 正确性校验 | 待验 | LOW | 1A.6 抽 N=10 atom 对齐验 | 1A.6 |
| R-7 | KB 后续微调 (07 website / jp_delivery 反向影响) | reingest 频率 | 低 | LOW | chunk metadata 含 `kb_commit_sha` + KB 变更触发 reingest | runtime |
| R-8 | LiteLLM Issue #26395 DeepSeek V4 Pro multi-turn 思考模式 bug | RAG multi-turn 用 V4-Pro 思考模式会断 | 100% (Open) | **MED→HIGH (D-4 v2 用户主用 V4-Pro)** | 主用 Sonnet, **复检 + fallback 用 V4-Pro 非思考模式** (D-4 v2); 1A.2.a 跑 V4-Pro 非思考 2 轮 + V4-Pro 思考 1 轮 sanity (verify bug single-turn 复现); LiteLLM Router config 明示 `extra_body={"thinking": {"type": "disabled"}}` 防回归 | 1A.2 |
| R-9 | DeepSeek V4-Pro 75% 折扣 2026-05-31 到期 | 成本上涨 | 100% | LOW | 2026-06-01 复查 pricing | runtime |
| R-10 | examples.md 单 chunk 最大 ~2.7K token (MB) | embedding 限 8K, 仍安全 | 0% | 0 | (验证完成, 不需缓解) | done |
| R-11 | Phase 2 KG 价值未验 — 可能 RAG 就够 | Phase 2 投入产出 | 待 1D eval | MED | 1D eval 决策点 gate | 1D |
| R-12 | ChatGPT Plus 代理违反 ToS + 数据安全 | 若强行接入会封号 + 数据泄露 | 高 | HIGH | **不接入** 生产, 仅 prototype 用 chatgpt.com 网页 | (架构决策) |
| **R-13** (v0.2) | Phase 1A.0 6 项 [UNVERIFIED] (supplementary_part / qs_part / questionnaires 43 文件 H2 / mermaid 嵌套 / 表格变体 / tiktoken 实测) 未 grep verify | chunker 实现可能漏处理 | 100% | MED | Phase 1A.0 main session re-grep verify 6 项 (新增 Phase 1A.0 sanity, 见 §5) | 1A.0 |
| **R-14** (v0.2) | Haiku 4.5 context window 仅推测 200K (llm_providers §7 [UNVERIFIED]) | intent 路由 / 轻分类 context 限 | 待 verify | LOW-MED | Phase 1A.2 sanity 时 verify platform.claude.com docs; 若 ≤ 64K 降级 Sonnet | 1A.2 |
| **R-15** (v0.2) | OpenAI text-embedding-3-small rate limit (Tier 1 3000 RPM) | reingest + 用户查询并发可能命中 limit | 中 | MED | ingest.py 限速 + 用户查询 embedding LRU 缓存 | 1A.5 |
| **R-16** (v0.2) | Chroma data 没备份策略, 全量 reingest 失败可能破坏旧 data | RAG 不可用 | 低 | MED | ingest.py 每次 ingest 前 `cp data/chroma data/chroma_backup_<timestamp>` | 1A.5 |
| **R-17** (v0.2) | LLM API key / `.env` 管理 + 误 commit 风险 | secret 泄漏 | 低 | MED | 1A.1.c: .env / .env.example + .gitignore 含 .env + README env vars 列表 + pre-commit hook 拦 .env diff | 1A.1 |
| **R-18** (v0.2) | reingest 触发机制 — KB 改了但没人手工 reingest | RAG 答案过期 | 中 | MED | 1A.5.d: server/main.py 启动比对 KB 当前 git HEAD vs `data/chroma/ingested_at_commit.txt`, 不一致 warn + 启 reingest 命令提示 | 1A.5 |
| **R-19** (v0.2) | LiteLLM v1.84.0 breaking changes (proxy multi-pod) 单机 SDK 是否影响未 verify | Router fallback chain 可能断 | 待 verify | LOW-MED | 1A.2.d: LiteLLM Router 2 轮对话 + fallback chain 端到端测 | 1A.2 |
| **R-20** (v0.2) | pyreadstat (Phase 1C XPT/SAS7BDAT 解析) 在 Apple Silicon Py 3.11+ build 可能失败 | 1C.1 dataset parser | 中 | LOW | 1A.1 加 sanity `pip install pyreadstat && python -c 'import pyreadstat'`; fallback `sas7bdat` 库 | 1A.1 |
| **R-21** (v0.2) | Streamlit 用户上传 + RAG + LLM 超时 UX 无反馈 | 用户体验差 | 中 | LOW | 1C.5 加 `st.status()` + `st.progress()` + 60s warning timeout | 1C.5 |
| **R-22** (D-4 v2) | bge-m3 本地 model 首次 ~2.5GB 下载 + Mac M-series MPS 推理速度未实测 + Docker torch CPU image ~800MB | Phase 1A.2 sanity 时间 + Docker build + ingest 耗时 | 100% | LOW-MED | 1A.2.f bge-m3 sanity 实测 5 sample text MPS 速度 (期望 < 100ms/chunk); Docker build multi-stage defer (1A.5 后看 image 大小决定); HuggingFace mirror 候选 (中国大陆 access slow 时) | 1A.2 / 1A.5 |

**R-1/R-2/R-4/R-8 必须 Phase 1A 前测试套件覆盖**, 不能上来就 ingest。**R-13 + R-17 必须 Phase 1A.0 sanity 完成才可进 1A.3 chunker writer**。**R-22 (bge-m3) 在 Phase 1A.2.f sanity 验证**。

---

## 9. PASS 五条 (本 旁枝 适用, v0.2 修订)

**术语对齐声明 (v0.2)**: 项目根 CLAUDE.md 定义 **PASS 四条** (evidence / writer / reviewer / 用户 ack)。本旁枝 RAG 项目因含 chunker 高压缩率步 + Phase 1C reviewer.py LLM 输出大幅压缩+改写, 加 **规则 A 抽检** 为第五条, 合计五条:

1. **evidence 存在** — 引用的 design doc / research report / git artifact 全实在
2. **writer 产物合规** — chunker 测试 100% PASS / eval 召回 ≥ 80% (Phase 1B5) → ≥ 85% (Phase 1D)
3. **独立 reviewer subagent PASS** — writer / reviewer / verifier 三 type 完全隔离 (Rule D)
4. **规则 A 抽检 PASS** — 任何步骤压缩率 > 50% 或改写率 > 50%, 必须 N 样本独立抽检:
   - **(a) Phase 1A chunker**: 每改一次 chunker 单元 (e.g., examples.py), 独立 reviewer 抽 **N≥10 sample chunk** 验切分边界 + metadata 完整性
   - **(b) Phase 1B5 sanity eval (20 题)**: scientist 独立写 **N=5 ground truth** 对照 main 写的 15 题, 比 50% 重合率 — 验题目质量不自审
   - **(c) Phase 1D full eval (50 题)**: 同上但 N=5 against 45 题
   - **(d) Phase 1C reviewer.py (LLM 语义评审)**: verifier 独立标 **N=5 user-data-row** ground truth, 验 LLM 评审输出业务规则准确率 / false positive / false negative; 同时假错误集 20 例独立标 ≥5 例
5. **用户 (Bojiang) 口头 ack**

每个 Phase 收口必带 PASS 五条 evidence (chunker_feasibility 抽检报告 / eval baseline / 1C audit 等), 见 EXECUTION_PLAN §Phase 1A-1D 末尾各 PASS 段。

---

## 10. 工期总览 (v0.2 修订, critic F-19/F-20/F-21)

| Phase | 工期 v0.1 | **工期 v0.2** | 状态 | 调整理由 |
|-------|----------|--------------|------|---------|
| Phase 0 Research | 1 d | 1 d | 🟢 in_progress | — |
| **Phase 1A Ingest** (加 1A.0 sanity + 1A.2.f bge-m3, D-4 v2) | 2.5-3 d | **3.5-4.5 d** | in_progress (1A.0/1A.1 closed 2026-05-22) | F-19 + 1A.0 sanity 0.3 d + 1A.2.f bge-m3 sanity 0.2 d (Mac MPS) |
| Phase 1B Q&A | 2 d | 2 d | pending | — |
| Phase 1B5 Sanity Eval | 0.7-1.5 d | 1-1.5 d | pending | — |
| **Phase 1C Dataset Validation** | 3.5-4 d | **5-6 d** | pending | F-20: 1C.2 规则引擎边界 case ≥1.5 d, 1C.3 RAG 评审 + 假错误集 ≥1.5 d, 1C.5 UI > 0.3 d |
| Phase 1D Full Eval | 2 d | 2 d | pending | — |
| Phase 1 收口 | 1 d | 1 d | pending | — |
| **Phase 1 TOTAL** | 10-13 d | **13.5-17.5 d** | — | F-21 + D-4 v2 (bge-m3 +0.2 d on 1A.2.f + marginally slower ingest/Docker build) |
| Phase 2 KG (defer, gated) | +6-8 d | +6-8 d | deferred | — |

---

## 11. Decisions Log (用户 ack 时点)

| # | 决定 | Decision | Date |
|---|------|---------|------|
| D-1 | 仓库布局 | `branches/07_rag_kg/sdtm-rag/` (跟 SDTM-pedia 一起 git) | 2026-05-22 (Bojiang ack) |
| D-2 (D-4 v2 修订) | LLM 主力 | Anthropic Claude Sonnet 4.6 主答 + **DeepSeek V4 Pro 非思考 复检/fallback** (D-4 v2; ex-V4-Flash) + Opus 4.7 难题 + Haiku 4.5 轻分类 | 2026-05-22 (Bojiang ack v1 + v2 修订) |
| D-3 | ChatGPT Plus 代理 | 不接入生产 (ToS + 稳定性), 仅 prototype 用网页 + 留 OpenAI base_url 接口 (`llm_config.py`) | 2026-05-22 (Bojiang ack) |
| D-4 v1 (superseded) | Embedding (原方案) | OpenAI text-embedding-3-small 主 (1536d) + bge-m3 fallback | superseded 2026-05-22 by D-4 v2 |
| **D-4 v2** ★ | Embedding (v2 修订) | **bge-m3 (1024d, local sentence-transformers)** 主 + OpenAI text-embedding-3-small fallback (留接口暂不调) | 2026-05-22 (Bojiang ack); 理由: 用户暂不开 OpenAI API account, Anthropic chat 链保留 |
| D-5 | Phase 2 KG | defer, Phase 1D RELATION 召回 < 50% 才启动 | 2026-05-22 (Bojiang ack) |
| D-6 | chunker | domain-aware (examples) + size-aware (chapters) + part 模式 (LB) | 2026-05-22 (Bojiang ack) |
| D-7 | INDEX.md 整体注入 system prompt | 加入 base prompt (~6K token w/ ROUTING) | 2026-05-22 (Bojiang ack) |
| D-8 | Eval 提前 | 20 题 sanity 在 ingest 后立刻跑, 50 题完整 eval 留 1D | 2026-05-22 (Bojiang ack) |

---

## 12. Open Issues

- **I-1**: P3 meta.yaml 是 Phase 2 KG 启动硬前置, 也是 jp_delivery 02 §3.4/§3.5 粒度议同源数据. Phase 1 期间是否提前启动 P3 (与 Phase 1 并行)? — pending Bojiang 决策
- **I-2**: Phase 1A 写代码用 Claude Code (Opus) 还是其他 IDE / LLM? — 本 PLAN 默认用 Claude Code OMC 体系, 见 EXECUTION_PLAN agent 配役表
- **I-3**: deploy target — 本地 Mac (设计 §1.4 默认) 还是用户公司服务器? — 默认本地, 云部署 defer

---

## 13. Next Actions

1. ✅ Phase 0 Research evidence 落档 (chunker + LLM)
2. ✅ PLAN.md v0.1 起草
3. ✅ EXECUTION_PLAN.md v0.1 起草 (HOW 详细)
4. ✅ Writer/reviewer 分离审 (critic Rule D PASS 1, CONDITIONAL_PASS, 32 findings)
5. ✅ v0.1 → v0.2 修订 (HIGH F-1/F-2/F-3 + MED F-6/F-7/F-9-F-11/F-14/F-19-F-21/F-23/F-24/F-27 + INFO F-32 全修)
6. ⏳ 用户 Bojiang ack PLAN v0.2 + D-2~D-8 决策 + 5 个 LOW findings (F-12/F-13/F-15/F-16/F-17 等) 是否当场修
7. ⏳ Phase 0 closure commit + push (单 commit 含骨架 + PLAN v0.2 + EXECUTION_PLAN v0.2 + 2 research + critic review_pass_1.md + MANIFEST/CLAUDE.md/PROGRESS 更新)
8. ⏳ Phase 1A.0 sanity (re-grep verify R-13 6 项) → 1A.1 启动 (sdtm-rag/ 仓库脚手架)

## 14. 失败回路 (规则 B 强制)

任何 attempt 失败 (writer 输出不合规 / reviewer FAIL / 用户拒绝 / 测试不过) 必须归档到 `evidence/failures/{phase}_{step}_attempt_{N}.md`, 含输入/产物/技术判定/业务判定/下一 attempt 调整。**不删原产物**。完整规范见 [`EXECUTION_PLAN.md §6`](EXECUTION_PLAN.md)。本次 critic Rule D PASS 1 是 v0.1 → v0.2 的 attempt 1 → attempt 2 反复, evidence 即 [`evidence/review_pass_1.md`](evidence/review_pass_1.md)。

---

> **Note**: 本 PLAN 是 Tier 2 规格. 写代码前必须完成 PASS 五条 + 用户 ack. 失败 attempt 归 `evidence/failures/` (规则 B). 收口必写 RETROSPECTIVE.md (规则 C).
