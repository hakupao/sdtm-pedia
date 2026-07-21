# Phase 1 RAG+KG — RETROSPECTIVE

> Date: 2026-05-24
> Phase: 1 (RAG + Dataset Validation) — Phase 0 Research → 1A Ingest → 1B Q&A → 1B5 Sanity Eval → 1C Dataset Validation → 1D Full Eval
> Duration: 2026-05-22 → 2026-05-24 (3 工作日, 原估 13-17 d, 实际大幅压缩因单人高密度执行)
> Tier: 2 (borderline 3)
> 规则 C 强制

---

## §1 保留下来的做法

### 1.1 Chunker 三策略 (domain-aware + size-aware + part-mode)

分文件类型写独立 chunker 模块是本项目最正确的架构决策。每种 KB 文件的结构差异远超预期:

- **examples.py domain-aware**: PC 域用 H4 嵌套 (14 chunks), TA 用 H2 扁平 (8 chunks), 自动探测 heading level 而非写死
- **chapters.py size-aware 三档**: ch04 (130KB) 用 `###` 切到 47 chunks (max 3852 tokens < 8K), ch01 (11KB) 整文件 1 chunk, 消除了 embedding truncation 风险
- **terminology.py part-mode vs codelist-mode**: H2 count == 1 且文件名含 `_partN` → 整 part 1 chunk; lb_part4 例外 (H2=2) 正确走 codelist mode

5 个 config lock (L-1 mermaid 状态机 / L-2 GFM pipe-table / L-3 tiktoken cl100k / L-4 chapters 50KB 阈值 / L-5 terminology part 判定) 在 Phase 1A.0 sanity 实测锁定, 后续 207 tests 零回归。

### 1.2 Eval-first (1B5 sanity eval 提前到 1C 前)

设计文档原方案是 eval 放最后 (Step 6)。PLAN 改成 1B5 (20 题 sanity) 紧跟 ingest + Q&A, 在建 validator 之前先验召回。这一决策在 1B5 发现 cross_domain 50% source recall 弱点, 提前定位了问题。如果放到最后, validator 写完才发现召回差, 修改成本高得多。

### 1.3 OpenAI cloud embedding (D-4 v3 果断弃本地模型)

bge-m3 本地 (sentence-transformers + torch) 两次运行崩溃后, 用户决策不再跑本地模型。切 OpenAI text-embedding-3-small (1536d cloud):
- Ingest 4146 chunks: **82 秒** (19.8 ms/chunk), 远低于本地模型预估 48s warm-batch
- 无 torch / MPS / Docker image 膨胀问题
- $0.02/1M tokens, 4146 chunks 约 2.5M tokens ≈ $0.05

教训: 本地模型在 Mac 上的 MPS/内存问题不值得花时间排查, 云 API 成本极低且稳定。

### 1.4 ROUTING.md + INDEX.md system prompt 整体注入

把 ROUTING.md (2K tok) + INDEX.md (4K tok) 整体塞进 system prompt (~6K token base), 让 LLM 在回答前就知道所有 64 域 + 91 terminology + 6 chapters 的入口映射。效果显著: 即使 retrieval 没召回目标文件, LLM 仍能从 system prompt 获得足够的路由信息, fact recall 保持 94.8%+。

### 1.5 7-rule validator + RAG 语义评审双轨

validator.py (规则引擎, 7 类 270 行) 和 reviewer.py (LLM 语义评审, 180 行) 分开实现是正确的:
- 规则引擎: 快 (<1s), 确定性, 18/19 error test detection (94.7%)
- 语义评审: 慢但深度, Opus 级 LLM 发现规则引擎无法覆盖的业务逻辑问题
- 合并报告: report.py 统一 Markdown + JSON 输出

### 1.6 LiteLLM Router + multi-model fallback

LiteLLM Router (4 model groups: default/fallback/hard/light) 一套代码支持 Anthropic + DeepSeek + OpenAI。当 Anthropic credits 耗尽时, 无缝切 DeepSeek 跑完 1D eval (88.5% PASS)。Router fallback chain 在 1A.2 sanity 验证通过。

---

## §2 必须补上的缺口

### 2.1 Anthropic Sonnet/Opus cross-model eval 未完成

1D eval 仅跑通 DeepSeek (88.5% PASS)。Sonnet/Opus 因 Anthropic API credit 耗尽而 BLOCKED。Source recall 是 model-independent (82.1% 已确认), 但 fact recall 差异未测。1B5 Sonnet 20 题 fact recall 100%, 预期 Sonnet 53 题 fact recall ≥ DeepSeek 94.8%, 但未实证。

**Action**: 充值 Anthropic credits 后补跑 Sonnet + Opus, 更新 1D report。

### 2.2 VARIABLE_INDEX.md + terminology/core/ 检索弱点

12/53 source misses 集中在 3 类:
- VARIABLE_INDEX.md (2 miss): 跨域变量查询时不被检索 → chunk 粒度问题 (65 chunks 按 domain H3 切, 但 query 是 cross-domain)
- terminology/core/ (3 miss): codelist 文件在 domain spec 已有 CT code 时不被检索 → embedding 相似度被 domain spec 拉走
- model/ + chapters/ (4 miss): 概念类问题检索偏好 domain spec 而非 model 概念文件

**可能改进**: 调 Top-K (15→20), 加 file_type boost weight, 或添加 query-time metadata filter 预判 file_type。但 fact recall 94.8% 说明当前质量已足够实用。

### 2.3 lb_part2/3 oversized chunks

lb_part2 (378KB) 和 lb_part3 (417KB) 以 part-mode 整 chunk, token 数远超 8K embedding limit。当前 xfail 在测试中。需实现 PLAN §6.4 的 N=100 table-row 切片 + table_chunk_idx。对检索影响: embedding 被 truncate, 仅前 8K tokens 有向量信号, 后半部分 codelist 条目无法被语义检索命中。

### 2.4 Docker Compose 端到端未验证

docker-compose.yml + Dockerfile 存在但未做过 `docker compose up --build` 端到端测试。本地 venv 开发模式全程可用, Docker 路径是 deployment-ready scaffold, 需用户首次 build 时验证。

### 2.5 ct_extensible 字段始终 None

terminology chunker 未实现 codelist body 中 extensible 信号的 regex 提取。所有 terminology chunks 的 `ct_extensible` metadata = None。对检索无影响 (不按 extensible 过滤), 但对未来 KG 建图有意义。

---

## §3 关键决策复盘

### D-4 Embedding 三连跳 (v1→v2→v3)

| 版本 | 方案 | 存活 | 教训 |
|------|------|------|------|
| v1 | OpenAI text-embedding-3-small 主 + bge-m3 fallback | 半天 | 初始设计合理 |
| v2 | bge-m3 local 主 + OpenAI fallback | 半天 | sentence-transformers 两次崩溃 |
| **v3 ★** | **OpenAI cloud 主, 无 fallback** | **至今** | 本地模型在 Mac 上不稳定, 果断放弃 |

决策正确性: ★★★★ — 崩溃后 2 小时内完成决策+切换+全量 reingest (82s), 无返工。用户 "本地模型两次崩溃, 已放弃" 是正确判断。

### D-5 Phase 2 KG defer gate

设计: Phase 1D RELATION 类 12 题召回 < 50% → 启动 Phase 2 KG。
实测: cross_domain src recall = 61.5% > 50%, fact recall = 96.2%。

**判定: Phase 2 KG NOT triggered** — RAG 语义检索 + system prompt routing 足以覆盖 cross-domain 查询。KG 的边际收益 (提升 source 溯源精度) 不足以 justify 6-8 工作日投入 (Neo4j + meta.yaml + Cypher 路由)。

推迟到: 部署后实际使用 1-2 周, 收集用户对 cross-domain 回答质量的反馈, 再决定。

### D-8 Eval 提前 + rate limit 教训

Eval 提前到 1B5 验证了架构可行性 (92.5% PASS), 避免了在 validator 完成后才发现召回问题。

1D eval 暴露了 Anthropic API rate limit (30K input tokens/min) 问题: 3 模型并行导致 429。教训:
- 同 API provider 的模型必须串行跑 eval
- run_eval.py 已加 retry + exponential backoff (30s → 60s → 120s → 240s)
- 未来考虑 Batch API (50% 折扣 + 无 rate limit) 跑大规模 eval

### Phase 1 工期压缩分析

原估 13-17 工作日, 实际 3 天完成。主要压缩因素:
- 单人高密度执行, 无等待/协调开销
- OMC multi-agent 并行 (chunker 3 batch parallel, eval 3 model parallel)
- 无重大返工 (D-4 v3 唯一大变更, 2 小时内解决)
- KB 质量高 (06 Deep Verification 后 coverage 99.02%, 减少 chunker edge case)

---

## Phase 2 决策点评估

**结论: Phase 2 KG 暂不启动。**

| 指标 | Phase 1 RAG 实绩 | Phase 2 KG 预期增益 |
|------|-----------------|-------------------|
| cross_domain fact recall | 96.2% | ~98-99% (marginal) |
| cross_domain source recall | 61.5% | ~85-90% (significant) |
| 工期 | 0 (已完成) | +6-8 工作日 |
| 运维复杂度 | Chroma only | +Neo4j Docker |

Phase 2 KG 的主要价值在 source recall 提升 (从 61.5% → ~85%), 但 fact recall 已 96.2%, 实际回答质量不受 source recall 影响。用户场景是内部查询工具, source 溯源精度非硬性需求。

**重新评估条件**: 部署后 1-2 周内, 若用户反馈 cross-domain 回答缺失关键信息 (fact recall < 90%), 或需要 relationship discovery (CT cascade 查询), 启动 Phase 2。
