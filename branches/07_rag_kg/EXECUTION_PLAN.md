<!-- chain: 07_RAG' (HOW 落地方案 + agent 调度链; PLAN.md 链 07_RAG 的下游)
  修改本文件后, 必须检查:
  → branches/07_rag_kg/PLAN.md                    (上游 WHAT/WHY, 整合性確認)
  → branches/07_rag_kg/_progress.json             (Phase 開始 / 完了 双方更新)
  → branches/07_rag_kg/prompts/                   (各 subagent kickoff prompt 模板実体)
  → branches/07_rag_kg/evidence/failures/         (失敗時 retro 归档先, 规则 B)
-->

# branches/07_rag_kg/ — 落地方案 + Agent 调度設計

> 创建: 2026-05-22
> 状态: **DRAFT v0.2** — PLAN v0.2 同步, 反映 critic Rule D PASS 1 修订, 待用户 ack
> v0.1 → v0.2 (2026-05-22): F-6 V4-Pro 非思考 / F-8 加 1A.2.d-e LiteLLM Router sanity / F-11 加 1A.1.c .env / F-22 并行表加注 / F-25 main session 矩阵注 / F-23 PASS 按 Phase 细分
> 上游: `PLAN.md` v0.1 (WHAT/WHY + chunker/LLM 决策)
> 本书职责 (HOW): 各 Phase agent 配役 / 派发顺序 / 并行机会 / Rule D 隔离 / 失败回路
> Tier: **2** (与 PLAN 同 Tier)

---

## 1. 凡例 (本书共通)

| 记号 | 意味 |
|------|------|
| 🔀 | **同一 session 内并行** — 主 session 多 subagent fan-out (Task tool 并行调用) |
| 📡 | **多 session 并行** — Claude Code 多 instance (06 multi_session/ pattern 踏襲) |
| ➡️ | **直列必須** — 前段成果物が後段入力 |
| ⚠️ | **Rule D 注意** — 前段と異なる subagent_type 必須 |
| 💾 | **進捗書込み点** — `_progress.json` 更新タイミング |

---

## 2. Agent 配役表 (Default Lineup)

| 役割 | subagent_type | model | context 予算 | 用途 |
|------|--------------|-------|------------|------|
| **W: writer (code)** | `executor` | opus (chunker/validator) / sonnet (routine) | 中 (KB 抽样 + 设计文档 + 测试规范) | sdtm-rag/ 各模块编码 |
| **W: writer (doc/plan)** | main session 或 `writer` | opus | 大 | PLAN / EXECUTION_PLAN / RETROSPECTIVE |
| **R: reviewer (code)** | `code-reviewer` | opus | 中 | writer 产物 + PLAN §PASS 五条 审 |
| **R: reviewer (plan/design)** | `architect` 或 `critic` | opus | 中 | PLAN / EXECUTION_PLAN 独立审 (Rule D 隔离) |
| **A: 审计/合规** | `verifier` | opus | 中 | PASS 五条最终判定, eval 结论 sign-off |
| **S: 调研** | `document-specialist` | sonnet | 小-中 (web + 规格 PDF) | LLM provider / chunker library / framework 调研 |
| **D: 设计助言** | `architect` | opus | 小 | 中途设计判断 (chunker 边界 / KG schema 等) |
| **T: 测试** | `test-engineer` | sonnet | 中 | chunker 测试套件 / eval test set 设计 |
| **DBG: 调试** | `debugger` | opus | 中 | LiteLLM bug 排查 / ingest 失败 / 召回异常 |

### 2.1 Rule D 隔离矩阵 (writer ↔ 同 PASS 内的 reviewer 必须异 type)

> **矩阵注解 (v0.2, F-25)**: "main session" 视为非 subagent 的 main Claude (执行 Claude Code OMC 主控), 与任意 subagent_type 都视为异 type (因为 main session 不属于任何 subagent_type, Rule D 主旨 "writer ≠ reviewer 同 type 同 session 自审" 自动满足)。

| 工程 | writer | reviewer | 用语监查 / 合规 | 隔离 OK? |
|------|--------|---------|----------------|---------|
| Phase 0 PLAN / EXECUTION_PLAN | main session `<main>` | `architect` 或 `critic` | — | ✅ 异 (main vs critic, 2026-05-22 已 PASS 1) |
| Phase 1A chunker code | `executor` (opus) | `code-reviewer` | — | ✅ 异 type |
| Phase 1A chunker 测试 | `test-engineer` | `code-reviewer` | — | ✅ 异 type |
| Phase 1B Q&A 服务 | `executor` | `code-reviewer` | — | ✅ 异 |
| Phase 1B5 eval 起草 | `executor` 或 main | `scientist` 或 `verifier` (eval 设计审查) | — | ✅ 异 |
| Phase 1B5 eval 跑分 | `scientist` (跑分独立) | `verifier` (结论判定) | — | ✅ 异 |
| Phase 1C validator + reviewer | `executor` (opus) | `code-reviewer` + `security-reviewer` (validator 涉及用户上传数据) | — | ✅ 异 |
| Phase 1D 全 eval | `scientist` | `verifier` | — | ✅ 异 |
| Phase 1 RETROSPECTIVE | main session | `critic` | — | ✅ 异 |

---

## 3. 并行度上限 (Open Issue I-2 可覆写)

| 并行模式 | 上限 | 理由 |
|----------|------|------|
| 🔀 单 session 内 subagent fan-out | **3** | 主 session context 干扰回避; chunker 6 类可分 2-3 批并行写 |
| 📡 多 session 并行 | **不启** (本 RAG 项目不需 06 multi-session 那种长跑) | 单人开发, 不需多 session 协同 |
| 读取専用 research subagent | 制限なし | write 競合なし |

---

## 4. Phase ごとの派発計画

### Phase 0 — Research (本 Phase 大部分已完成)

| Step | 内容 | agent | 並列 | 状态 |
|------|------|-------|------|------|
| 0.1 | 旁枝骨架创建 | main 直接 Bash + Write | — | ✅ done |
| 0.2 | LLM providers 调研 | `document-specialist` (background) | 🔀 与 0.3 并行 | ✅ done |
| 0.3 | Chunker feasibility 调研 | main 直接 Bash + Read | 🔀 与 0.2 并行 | ✅ done |
| 0.4 | PLAN.md 起草 | main (writer) | ➡️ 0.2+0.3 完成后 | ✅ done |
| 0.5 | EXECUTION_PLAN.md 起草 | main (writer) | ➡️ 0.4 后 | 🟢 in_progress (本文件) |
| 0.6 | 独立 reviewer 审 PLAN+EXECUTION_PLAN | `architect` (Rule D 异 type) | ➡️ 0.5 后 ⚠️ | pending |
| 0.7 | 用户 ack + decision log D-2~D-8 | Bojiang | ➡️ 0.6 后 | pending |
| 0.8 | Phase 0 closure commit + push | main 直接 Bash (git) | ➡️ 0.7 后 | pending |
| 💾 | `_progress.json` Phase 0 PASS 記録 | main | — | pending |

**所要時間**: Phase 0 总共 1 工作日 (今天即可结)

---

### Phase 1A — Ingest (3-4 d, v0.2 加 1A.0 + 1A.1.c-d + 1A.2.d-e) 🔥 并行机会最多

#### Step 1A.0 — Sanity Re-grep Verify (0.3 d, v0.2 新增, F-3/R-13)

**目的**: 不信任 chunker_feasibility 估算, 1A.3 chunker writer 启动前 main session 必须 re-grep verify 6 项未验证项 (含 supplementary_part / qs_part / questionnaires 43 文件 H2 / mermaid 嵌套 / 表格变体 / tiktoken 实测), 把数字落实到 `evidence/checkpoints/phase_1a_0_sanity.md`。

| Sub | 内容 | agent |
|-----|------|-------|
| 1A.0.a | grep supplementary_part1-6 + general_part* + qs_part* + questionnaires/ H2 数, 计 chunk 估算修正 | main 直接 Bash |
| 1A.0.b | 抽 3 个 examples.md (TA/DM/含 mermaid) 验 mermaid block 嵌套 + 表格变体 | main |
| 1A.0.c | tiktoken 实测 5 个最大 chunk (TA Example / MB Example / ch04 §4.4 / lb_part4 / VARIABLE_INDEX §二.AE) token 数 | main |
| 1A.0.d | 落 evidence/checkpoints/phase_1a_0_sanity.md (含修正后的 chunker config defaults) | main |
| 💾 | _progress.json 1A.0 PASS, chunker config 锁定 | — |

#### Step 1A.1 — sdtm-rag/ 仓库脚手架 (0.3 d)

| Sub | 内容 | agent | 备注 |
|-----|------|-------|------|
| 1A.1.a | `branches/07_rag_kg/sdtm-rag/` 目录树 + pyproject.toml + Dockerfile + docker-compose.yml | main 直接 Bash + Write | 单一 owner |
| 1A.1.b | .gitignore (data/chroma/ 不入库) + README.md (项目入门) | main | 同上 |
| **1A.1.c** (v0.2, F-11/R-17) | .env.example (列 ANTHROPIC_API_KEY / DEEPSEEK_API_KEY / OPENAI_API_KEY 不带值) + .gitignore 加 `.env` + README.md "Environment Variables" 段 + (可选) pre-commit hook 拦 .env diff | main | 防 secret 误 commit |
| **1A.1.d** (v0.2, R-20) | sanity `pip install pyreadstat && python -c 'import pyreadstat'`; 失败则 fallback `sas7bdat` 库 | main | Apple Silicon Py 3.11+ build 风险 |
| 💾 | _progress.json phase_1a.1 PASS | main | — |

#### Step 1A.2 — LiteLLM sanity (0.3 d, v0.2 扩展)

**目的**: Phase 1A 写代码前确认 DeepSeek V4 Pro multi-turn bug 真实影响 + Sonnet 2 轮对话正常 + Router fallback chain + Haiku context window 实测。

| Sub | 内容 | agent |
|-----|------|-------|
| 1A.2.a | `pip install litellm==1.85.1`, 跑 `scripts/sanity_litellm.py` (DeepSeek V4 Pro 2 轮思考模式 + Sonnet 2 轮 + DeepSeek V4 Flash 2 轮非思考) | `executor` (sonnet) |
| 1A.2.b | 记录结果到 `evidence/litellm_sanity_2026-MM-DD.md` | 同上 |
| 1A.2.c | 如果 V4 Pro bug 仍在: 标 `R-8 confirmed`, RAG multi-turn 改用 V4 Flash 非思考模式 | main (决策) |
| **1A.2.d** (v0.2, F-8/R-19) | LiteLLM Router fallback chain 2 轮对话 (Sonnet 主 → V4-Flash fallback 触发); 验 v1.84.0 breaking changes 在单机 SDK 模式不影响 | `executor` |
| **1A.2.e** (v0.2, F-7/R-14) | Haiku 4.5 context window 实测 (查 platform.claude.com docs + 实跑长 prompt 测) | `document-specialist` |
| 💾 | _progress.json | — |

#### Step 1A.3 — Chunker 实现 (1.5 d) 🔀 3 并行机会

| Batch | 内容 | agent | 并列 | Rule D |
|-------|------|-------|------|--------|
| **Batch A (simple)** | `chunkers/base.py` + `spec.py` + `assumptions.py` + `model.py` | `executor` (sonnet, low-risk) | 🔀 与 Batch B/C 并列 | — |
| **Batch B (★ high-risk examples)** | `chunkers/examples.py` (domain-aware + mermaid/table 保护) | `executor` (opus, 复杂逻辑) | 🔀 | — |
| **Batch C (★ med-risk)** | `chunkers/chapters.py` (size-aware) + `terminology.py` (LB part 模式) + `variable_index.py` | `executor` (opus) | 🔀 | — |
| **集成** | 主 session 集成 + base class 调整 (3 batch 完成后) | main | ➡️ | — |
| 💾 | _progress.json 每 batch PASS | — | — | — |

**3 并列 → 工期压缩约 40%** (从 1.5 d 直列 → 0.9 d 并列)

#### Step 1A.4 — Chunker 测试套件 (0.5 d) ⚠️ Rule D 异 type

| Sub | 内容 | agent | 备注 |
|-----|------|-------|------|
| 1A.4.a | 写测试套件 (TA/PC/IS/DS examples + LB part + ch04 chapter + assumptions 多变体) | `test-engineer` | Rule D: 与 1A.3 writer (executor) 异 type |
| 1A.4.b | 跑测试, 修 fail case (如有) | `executor` ↔ `test-engineer` 反复 | 失败 attempt 归 `evidence/failures/chunker_test_attempt_N.md` (规则 B) |
| 1A.4.c | 全 PASS 后 reviewer 审测试覆盖 | `code-reviewer` | Rule D 第三方 |
| 💾 | _progress.json | — | — |

#### Step 1A.5 — ingest.py 全量跑 (0.3 d)

| Sub | 内容 | agent |
|-----|------|-------|
| 1A.5.a | ingest.py 主流程: 遍历 KB → 各 chunker → embedding (OpenAI text-embedding-3-small) → Chroma | `executor` |
| 1A.5.b | 跑全量, 记录 chunk 总数 + size 分布 + 耗时 + 成本 (期望 ~$0.01) | 同上 |
| 1A.5.c | sample 10 个查询验 retrieval (e.g., "AETERM 是什么", "TA Example 1") 召回 Top-5 看是否合理 | main + `verifier` 抽检 |
| 💾 | _progress.json + evidence/checkpoints/ingest_v1.md | — |

#### Step 1A.6 — 规则 A 抽检 (0.2 d) ⚠️ Rule D 第三方

**目的**: 06 P5 reverse_ledger.jsonl 已 ground truth 化, 拿 N=10 atom 验 chunk-atom 边界对齐。

| Sub | 内容 | agent |
|-----|------|-------|
| 1A.6.a | 从 `branches/06_deep_verification/reverse_ledger.jsonl` 随机 N=10 SOURCED atom (seed=20260522) | main 直接 Bash |
| 1A.6.b | 对每个 atom: 检查其 `(domain, file_type, section)` 是否能 1:1 对应到一个 Chroma chunk | `scientist` (独立审, Rule D 第三方) |
| 1A.6.c | 报告 chunk-atom 对齐率 (期望 ≥9/10), 出 `evidence/checkpoints/rule_A_chunk_atom_alignment.md` | 同上 |
| 💾 | _progress.json Phase 1A PASS | main | — |

**Phase 1A PASS 五条** (CLAUDE.md 规则 D + 本旁枝):
1. evidence: chunker 测试 100% PASS + ingest 全量成功 + 1A.6 抽检 ≥9/10
2. writer (executor) 产物 lint/typecheck PASS
3. 独立 reviewer (`code-reviewer`) PASS
4. 规则 A 抽检 PASS (1A.6)
5. 用户 Bojiang ack

---

### Phase 1B — Q&A 服务 (2 d)

| Step | 内容 | agent | 备注 |
|------|------|-------|------|
| 1B.1 | FastAPI router + ROUTING.md + INDEX.md system prompt 注入 + 配置文件 | `executor` (sonnet) | — |
| 1B.2 | rag.py: metadata filter 设计 (LLM 抽 filter 条件) + Chroma 语义检索 Top-K=15 | `executor` (opus, 复杂) | — |
| 1B.3 | (可选) Cohere Rerank 集成 Top-5 — 先不开, eval 后决定 | `executor` (按需) | — |
| 1B.4 | LiteLLM Router (`llm_config.py`): Sonnet 主 + DeepSeek Flash fallback + Opus 难题 | `executor` | 引用 research/llm_providers §5 |
| 1B.5 | Streamlit UI 极简 (chat + 溯源展开 + 模型 selector) | `executor` (sonnet) + `designer` 审 UX | 🔀 1B.1-1B.4 完成后 |
| 1B.6 | reviewer 审 server 代码 | `code-reviewer` | Rule D ⚠️ |
| 💾 | _progress.json Phase 1B PASS | — | — |

---

### Phase 1B5 — Sanity Eval (0.7-1.5 d, 本 PLAN 新增, 提前到 1C 前)

| Step | 内容 | agent | Rule D 关键 |
|------|------|-------|-------------|
| 1B5.1 | 写 20 题 ground truth (yml: question + ground_truth_answer + expected_source_files + category) | main (writer) + `scientist` (eval 设计审, 异 type) | ⚠️ writer ≠ reviewer |
| 1B5.2 | run_eval.py: 跑题 → 记录 answer + 引用文件 + 召回 chunk ids → 跟 ground truth 比对 | `scientist` (独立跑分) | 跑分 owner 应独立 |
| 1B5.3 | 出 baseline report: correctness % / source citation accuracy / recall % | 同上 | — |
| 1B5.4 | 决策点: 召回 < 80% 回头改 chunker / Top-K (1B5.4.a) 或 chunk size (1B5.4.b) | main + `architect` 助言 | — |
| 1B5.5 | reviewer 审 eval 结论合理性 | `verifier` | Rule D 第三方 ⚠️ |
| 💾 | _progress.json Phase 1B5 PASS | — | — |

---

### Phase 1C — Dataset Validation (3.5-4 d) — 核心价值

#### Step 1C.1 — Dataset Parser (0.5 d)

| Sub | 内容 | agent |
|-----|------|-------|
| 1C.1 | `parse_dataset.py`: pandas + pyreadstat 解析 CSV/XPT/SAS7BDAT → DataFrame + 自动检测 domain | `executor` (sonnet) |

#### Step 1C.2 — Validator 规则引擎 (1.5 d)

**7 类规则检查**, 设计 §4.2:

| Sub | 检查 | 依赖数据 |
|-----|------|---------|
| 1C.2.a | Req 完整性 | spec.md Core=Req 列 |
| 1C.2.b | Exp 完整性 | spec.md Core=Exp 列 |
| 1C.2.c | CT 合规 | terminology/ codelists |
| 1C.2.d | 数据类型 (Char/Num) | spec.md Type 列 |
| 1C.2.e | 主键唯一 (STUDYID+USUBJID+--SEQ) | DM as 参照 |
| 1C.2.f | 跨域 USUBJID 对 DM | DM 全 USUBJID 集 |
| 1C.2.g | 变量名 (未知变量警告) | spec.md 变量清单 |

| Sub | 内容 | agent |
|-----|------|-------|
| 1C.2 | `validator.py` 7 类规则引擎实现 | `executor` (opus) |
| 1C.2.x | reviewer 审 + 边界 case 测试 (空表 / 重复主键 / 缺列等) | `code-reviewer` + `test-engineer` | Rule D ⚠️ |

#### Step 1C.3 — RAG 语义评审 (1 d)

| Sub | 内容 | agent |
|-----|------|-------|
| 1C.3.a | `reviewer.py`: 检索 assumptions.md + examples.md → 喂 LLM (Opus 4.7) → 判业务规则合规 | `executor` (opus) |
| 1C.3.b | 5 类语义检查 (业务规则 / 逻辑一致 / pattern 比对 / 完整性评估 / 跨域关系) | 同上 |
| 1C.3.c | reviewer 审 + 假数据测 (人造错误集 20 例) | `code-reviewer` + `security-reviewer` (用户上传数据涉合规) | Rule D ⚠️⚠️ 双审 |

#### Step 1C.4 — 报告生成 (0.5 d)

| Sub | 内容 | agent |
|-----|------|-------|
| 1C.4 | `report.py`: Markdown + JSON 双格式 (完整性 % + ERROR/WARN/INFO 分级表 + 推荐) | `executor` (sonnet) |

#### Step 1C.5 — UI 集成 (0.3 d)

| Sub | 内容 | agent |
|-----|------|-------|
| 1C.5 | Streamlit 加 upload panel + 校验报告展示 | `executor` (sonnet) |

**1C PASS 五条**:
1. evidence: 人造错误集 20 例的 ERROR/WARN/INFO 分级精度报告
2. writer 产物 lint + typecheck PASS
3. 独立 `code-reviewer` + `security-reviewer` 双审 PASS
4. 规则 A: 20 例错误集独立 ground truth (Bojiang 或 architect 标注) 后跑 false positive / false negative
5. 用户 Bojiang ack

---

### Phase 1D — Full Eval (2 d)

| Step | 内容 | agent | 备注 |
|------|------|-------|------|
| 1D.1 | 扩 50 题 (设计 §6.1: 单域精准 12 + 跨域关系 12 + 概念规则 12 + 混合 12 + 校验场景 5) | main + `scientist` (异 type) | ⚠️ writer ≠ reviewer |
| 1D.2 | 跨模型对比 (Sonnet vs Opus vs **DeepSeek V4 Pro 非思考 single-turn** vs V4 Flash) | `scientist` (跑分) | 用 LiteLLM Router 切模型; **不用 V4 Pro Reasoner 思考模式** (LiteLLM Issue #26395 multi-turn bug, R-8) |
| 1D.3 | 出 eval report: correctness/citation/recall 三指标 + 跨模型对比表 | `scientist` + `verifier` 终判 | Rule D ⚠️ |
| 1D.4 | 决策点: RELATION 类 12 题召回 < 50% → 触发 Phase 2 KG 启动条件 | main + Bojiang | — |
| 💾 | _progress.json Phase 1D PASS | — | — |

---

### Phase 1 收口 (1 d)

| Step | 内容 | agent | 备注 |
|------|------|-------|------|
| 1.收.1 | RETROSPECTIVE.md 三段齐备 (保留下来的做法 / 必须补上的缺口 / 关键决策复盘, 规则 C) | main (writer) | — |
| 1.收.2 | Docker Compose 一键起部署文档 (sdtm-rag/README.md 扩) | `writer` 或 main | — |
| 1.收.3 | Phase 2 决策点评估文档 (基于 1D.4) | main + `architect` | — |
| 1.收.4 | RETROSPECTIVE 独立审 | `critic` | Rule D ⚠️ |
| 1.收.5 | Phase 1 closure commit + push + tag (如 `phase7-rag-v1.0`) | main | — |
| 💾 | _progress.json Phase 1 PASS | — | — |

---

## 5. Kickoff Prompt 模板

各 subagent 派发时使用 `prompts/` 下模板. Phase 0 完成后写入:

```
prompts/
├── 1A3_chunker_writer.md         (Batch A/B/C 共用, 内有 batch 参数)
├── 1A4_chunker_test_engineer.md
├── 1A4_code_reviewer.md
├── 1A5_ingest_writer.md
├── 1A6_rule_A_scientist.md
├── 1B_qa_writer.md
├── 1B5_eval_scientist.md
├── 1C2_validator_writer.md
├── 1C3_semantic_reviewer_writer.md
├── 1D_full_eval_scientist.md
└── retrospective_critic.md
```

**模板共同结构**:
1. 目标 (1 句)
2. 上游 context (引用 PLAN.md 章节 + research/ evidence 文件)
3. 输入文件清单
4. 期待产出 (含文件路径)
5. PASS 条件 (引用 PLAN §9 五条)
6. Rule D 隔离声明 (writer ≠ reviewer 同 type)
7. 失败时归档路径 (`evidence/failures/`)
8. 工期估算

---

## 6. 失败回路 (规则 B 强制)

任何 Phase 内 attempt 失败 (writer 输出不合规 / reviewer FAIL / 用户拒绝 / 测试不过):

1. **归档**: `evidence/failures/{phase}_{step}_attempt_{N}.md` 含:
   - 输入 (kickoff prompt 引用)
   - 产物 (失败的代码 / 文档)
   - 技术判定 (lint / test / type-check)
   - 业务判定 (reviewer 评论 / 用户反馈)
   - 下一 attempt 的输入调整
2. **不删原产物** — `git restore` 失败版本前先 cp 到 `failures/`
3. **重派**: 调整 prompt + 换 subagent_type 或 model

---

## 7. 升级 Tier 3 触发条件

本 PLAN 默认 Tier 2. 升 Tier 3 触发 (若发生):
- Phase 1A chunker 测试套件失败重写 ≥ 3 次 (复杂度超预期)
- LiteLLM bug 导致多 LLM 集成需要原生 SDK 直接调用 (绕过抽象层)
- 数据集校验需要建专门 schema validator (e.g., JSON Schema 2020-12) 跨工程同步
- Phase 2 KG 启动 (P3 meta.yaml 生成 + Neo4j + Cypher LLM-gen 是天然 Tier 3 级)

升级后增加: `trace.jsonl` 全链 + `subagent_prompts/` 全留 + `audit_matrix.md`.

---

## 8. Context 預算

| Phase | main session context | subagent context | 备注 |
|-------|---------------------|------------------|------|
| Phase 0 (本) | 已用 ~30K (KB 抽样 + 调研整合) | document-specialist ~45K | 中等 |
| Phase 1A | ~50K (chunker writer dispatch + reviewer 报告读) | executor ~80K (含 KB 样本) | 高 |
| Phase 1B | ~30K | executor ~50K | 中 |
| Phase 1B5 | ~25K | scientist ~40K | 低 |
| Phase 1C | ~50K (复杂规则引擎) | executor ~80K | 高 |
| Phase 1D | ~40K | scientist ~60K | 中-高 |

主 session context 余量在每 phase 收口前压缩 — 用 `_progress.json` 持久化关键决策, 不留长 history。

---

## 9. 並列効果サマリ (v0.2 修订, F-22)

> **注解 (v0.2)**: Phase 总压缩来源**主要是 Phase 1A 三 batch chunker writer 并列 (~25%) + Phase 1C 部分并列 (~15%)**, 其他 Phase (1B/1B5/1D/收口) 无并列空间。整体不能简单按比例外推。06 P2 实绩并行只压缩 ~15%, 本估算 17-25% 已含 Tier 2 仪式 + Rule D 反复 overhead。

| Phase | 直列工期 | 并列工期 | 压缩 | 备注 |
|-------|---------|---------|------|------|
| Phase 0 | 1 d | 1 d | — | 0.2+0.3 并列已用 |
| Phase 1A | 5 d (含 1A.0 + 1A.1.c-d + 1A.2.d-e + 1A.4 失败回归 + 1A.5 backup) | 3-4 d | **20-30%** | 1A.3 三并列 + 集成 + Rule D 反复 |
| Phase 1B | 2 d | 2 d | — | 无并列空间 |
| Phase 1B5 | 1.5 d | 1-1.5 d | 0-33% | 跳过 chunker 修则压 |
| Phase 1C | 6.5 d | 5-6 d | ~15% | 1C.2 / 1C.3 部分并列 |
| Phase 1D | 2 d | 2 d | — | 跨模型对比天然 batch |
| 收口 | 1 d | 1 d | — | — |
| **Phase 1 总** | **19-20 d** (直列含 Tier 2 仪式) | **13-17 d** (并列压缩 + 失败回归 overhead) | **15-25%** | v0.1 估 10-13 d 偏紧, v0.2 上调 |

---

## 10. Open Issues / 待用户决策

- **I-2**: Phase 1A 写代码用 Claude Code (Opus, executor subagent) 还是其他 IDE / 直接调 API? — 默认 Claude Code OMC 体系
- **I-3**: Phase 1A.6 规则 A 抽检 N=10 用什么 random seed? — 默认 seed=20260522 (今天日期)
- **I-4**: Phase 1C 用户上传数据是否需要本地加密 / 加密静态盘? — 默认不加密 (本地 dev), 云部署再议
- **I-5**: deploy target — 本地 Mac 还是用户公司服务器? — 默认本地 (Mac M-series GPU 可跑 bge-m3 fallback)

---

## 11. Per-Phase PASS 五条 (v0.2 新增, F-23)

每个 Phase 收口 PASS 条件 (PLAN §9 PASS 五条按 Phase 实例化):

### Phase 1A PASS
1. evidence: chunker 测试 100% PASS + ingest 全量成功 + 1A.6 抽检 ≥9/10 + 1A.0 sanity 6 项落实
2. writer (`executor`) 产物 lint/typecheck PASS
3. 独立 `code-reviewer` (异 type) PASS
4. 规则 A 抽检: 1A.4 chunker 测试套件 N≥10 sample 边界验 + 1A.6 atom-chunk 对齐 N=10
5. 用户 Bojiang ack

### Phase 1B PASS
1. evidence: FastAPI 端到端 + Streamlit UI 跑通 + 5 题 sample 召回合理
2. writer (`executor`) 产物 lint/typecheck PASS
3. 独立 `code-reviewer` PASS
4. 规则 A: 无 (本 Phase 不触发压缩率 > 50%)
5. 用户 ack

### Phase 1B5 PASS
1. evidence: 20 题 ground truth + baseline 报告 + 召回 ≥ 80%
2. writer (main + `executor`) 产物合规
3. 独立 `verifier` PASS
4. 规则 A: scientist 独立写 N=5 ground truth 对照 main 写的 15 题 (PASS 五条 4.b)
5. 用户 ack

### Phase 1C PASS
1. evidence: 7 类规则单元测试 + 假错误集 20 例 + 真实 dataset (Bojiang 提供) 校验报告
2. writer (`executor` opus) 产物 lint/typecheck PASS
3. 独立 `code-reviewer` + `security-reviewer` 双审 PASS
4. 规则 A: verifier 独立标 N=5 错误 ground truth, 验 false positive / false negative (4.d); reviewer.py LLM 输出 N≥5 user-data-row 验业务规则准确率
5. 用户 ack

### Phase 1D PASS
1. evidence: 50 题 + 跨模型对比表 + correctness/citation/recall 三指标
2. writer (`scientist`) 跑分独立, 不接触 ground truth 写作
3. 独立 `verifier` 终判 PASS
4. 规则 A: scientist 独立写 N=5 ground truth 对照 main 写的 45 题 (4.c)
5. 用户 ack

### Phase 1 收口 PASS
1. evidence: RETROSPECTIVE.md 三段齐备 + Docker Compose deploy 文档 + Phase 2 决策点报告
2. writer (main) 产物
3. 独立 `critic` PASS
4. 规则 A: 不触发 (回顾性写作)
5. 用户 Bojiang ack tag `phase7-rag-v1.0` 之前

## 12. Next Action

1. ✅ Phase 0.5 EXECUTION_PLAN.md 起草 v0.1
2. ✅ Phase 0.6 critic Rule D PASS 1 (CONDITIONAL_PASS, 32 findings)
3. ✅ Phase 0.6.5 v0.1 → v0.2 修订 (chunker_feasibility 10 处 + PLAN 12 处 + EXECUTION_PLAN 9 处)
4. ⏳ Phase 0.7 用户 ack 决策 D-2~D-8 + I-2~I-5 + 5 LOW findings 是否当场修
5. ⏳ Phase 0.8 commit + push (single commit Phase 0 closure)
6. ⏳ Phase 1A.0 sanity (re-grep verify R-13 6 项) → 1A.1 启动

---

> **Note**: 本 EXECUTION_PLAN 是 HOW 落地文档, 用户 ack PLAN.md 同时本文件也同步 ack. Phase 1A 启动前 prompts/ 模板必须先写.
