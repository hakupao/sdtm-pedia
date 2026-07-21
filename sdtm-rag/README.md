# sdtm-rag — SDTM Knowledge Base RAG + Dataset Validation

> Phase 7 RAG+KG 旁枝实际代码仓 (Phase 1A 起开始建).
> Status: **Phase 1 Complete** — RAG Q&A + Dataset Validation + 53-question eval PASS (88.5%).
> 上游 PLAN/EXECUTION_PLAN: [`../PLAN.md`](../PLAN.md), [`../EXECUTION_PLAN.md`](../EXECUTION_PLAN.md).
> 单用户/单租户 (PLAN §0.2 Out-of-scope), uvicorn `--workers 1`.

---

## What

为 SDTM 知识库 (`../../../knowledge_base/`, 294 md / 4146 chunks 实测 ingest) 提供:

1. **语义问答 RAG** — 自然语言查询, 带溯源
2. **数据集校验** — 上传 SDTM 映射 (CSV/XPT/SAS7BDAT), 出完整性 + 规则合规报告
3. (Phase 2, deferred) 关系发现 — Neo4j KG

## Architecture (Phase 1)

```
┌──────────────┐   query     ┌──────────────┐   filter+topK   ┌──────────────┐
│  Streamlit   │ ──────────► │   FastAPI    │ ──────────────► │    Chroma    │
│   (ui/)      │             │   (server/)  │                 │   (data/)    │
│              │ ◄────────── │              │ ◄────────────── │              │
└──────────────┘   answer    └──────────────┘    chunks       └──────────────┘
                                    │
                                    │ LiteLLM Router
                                    ▼
                            ┌──────────────────┐
                            │ Sonnet (主答)    │
                            │ V4-Pro (复检)    │
                            │ Opus (难题)      │
                            │ Haiku (轻分类)   │
                            └──────────────────┘
```

## Directory Layout

```
sdtm-rag/
├── pyproject.toml          PEP 621 manifest, Python >= 3.11
├── Dockerfile              python:3.11-slim base
├── docker-compose.yml      api + ui services
├── .env.example            填好 .env 用 (NEVER commit .env)
├── .gitignore              data/chroma/ + .env + caches
├── scripts/
│   ├── chunkers/           ← Phase 1A.3 实现 (8 chunker; config locks L-1..L-5 见 evidence/checkpoints/phase_1a_0_sanity.md §4)
│   ├── tests/              ← Phase 1A.4 测试套件
│   ├── shared/
│   ├── ingest.py           ← Phase 1A.5
│   └── parse_dataset.py    ← Phase 1C.1
├── server/
│   ├── main.py             ← FastAPI app
│   ├── router.py           ← intent 路由
│   ├── rag.py              ← Chroma 检索 + LLM 答
│   ├── validator.py        ← 7 类规则校验 (Phase 1C.2)
│   ├── reviewer.py         ← RAG 语义评审 (Phase 1C.3, Opus)
│   ├── llm_config.py       ← LiteLLM Router 配置
│   └── config.py
├── ui/
│   └── streamlit_app.py    ← chat + 溯源 + 上传校验
├── data/
│   └── chroma/             ← persistent (gitignored)
└── eval/
    ├── test_set_v0.yml     ← Phase 1B5 sanity 20 题
    ├── test_set_v1.yml     ← Phase 1D 完整 50 题
    └── run_eval.py
```

## Quick Start — Local (venv)

```bash
# 1. Create venv + install deps
cd sdtm-rag
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

# 2. Set up environment
cp .env.example .env
# Edit .env: fill ANTHROPIC_API_KEY, DEEPSEEK_API_KEY, OPENAI_API_KEY

# 3. Ingest knowledge base (one-time, ~82 seconds)
python scripts/ingest.py

# 4. Start API server
uvicorn server.main:app --host 0.0.0.0 --port 8000

# 5. Start Streamlit UI (separate terminal)
streamlit run ui/streamlit_app.py
# Open http://localhost:8501
```

## Quick Start — Docker Compose (local self-host)

> Prereq: Docker + Docker Compose v2. 单用户/单租户本地部署 (云部署 defer per H-2).
> Run from this dir (`sdtm-rag/`).

```bash
# 1. Environment — OPENAI_API_KEY 是硬性必需 (embedding, 无 fallback);
#    DEEPSEEK_API_KEY 当前是实际主答 (Anthropic credits 耗尽 → Router 回退 DeepSeek).
cp .env.example .env        # 然后填入 key (见下方 Environment Variables 表)

# 2. Build + start (api :8000, ui :8501; api healthcheck 通过后 ui 才起)
docker compose up --build -d

# 3. 向量库 chroma:
#    (a) 复用已 ingest 的 ./data/chroma (4146 chunks, 通过 volume 挂入) → 无需重 ingest, 直接可用; 或
#    (b) 全新 ingest (需 OPENAI_API_KEY, ~80s):
docker compose exec api python scripts/ingest.py

# 4. 验证
curl -fsS http://localhost:8000/api/health          # {"status":"ok"}
curl -s   http://localhost:8000/api/info            # 应见 structured_lookup/hybrid/prompt_guardrail = true
# API docs: http://localhost:8000/docs   |   UI: http://localhost:8501
```

- **检索/答题杠杆默认全开** (structured_lookup + hybrid + 答题侧 grounding 护栏); `SDTM_RAG_*` env 可单独关。
- Knowledge base 通过只读 volume `../../../knowledge_base:/app/knowledge_base:ro` 挂入 (H-1 read-only 硬约束)。
- `data/` (chroma 持久化 + 上传数据集) 是 bind volume, 不烘进镜像 (见 `.dockerignore`); secrets 经 `env_file` 运行时注入, 永不入镜像。
- **Anthropic credits 耗尽时**: 默认 model = Sonnet 4.6, 但 Router 自动回退 `deepseek/deepseek-v4-pro` (实测 `model_used=deepseek-v4-pro`); 补足 credits 后自动走 Sonnet, 无需改配置。

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/info` | GET | System info (chunks, model) |
| `/api/ask` | POST | RAG Q&A (JSON: `{"question": "..."}`) |
| `/api/validate` | POST | Dataset validation (multipart file upload) |

## Eval

```bash
# Retrieval-only (free, no LLM) — source recall
python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --structured-lookup --hybrid

# Full eval (substring fact recall — under-counts ~11pt, kept as secondary metric)
python eval/run_eval.py eval/test_set_v3.yml --model deepseek/deepseek-chat --output eval/report.json

# Full eval with SEMANTIC fact recall (--judge): the trustworthy number; drives the
# verdict, substring shown as secondary. Adds 1 judge LLM call/question (--judge-model
# default deepseek). Use temp=0 + levers for a production-faithful run.
python eval/run_eval.py eval/test_set_v3.yml --model deepseek/deepseek-chat --temperature 0 \
    --structured-lookup --hybrid --judge --output eval/report.json
```

> 语义 judge fact recall ≈ **93.9%** on v3 140q (vs substring 82.6%); see
> `evidence/checkpoints/llm_judge_fact_recall.md`. Always prefer `--judge` for reported
> fact-recall numbers; the substring metric is for fast/free sanity only.

## Environment Variables

详见 `.env.example`. 关键说明:

| Var | 必需? | 说明 |
|-----|-------|------|
| `OPENAI_API_KEY` | ★★ 硬必需 | Embedding: text-embedding-3-small (D-4 v3); **无 fallback**, ingest+query 都靠它, 缺则服务不可用 |
| `DEEPSEEK_API_KEY` | ★ 必 | **当前实际主答** (Anthropic credits 耗尽时 Router 回退到此; V4-Pro 非思考模式; **不**用 Reasoner 因 LiteLLM Issue #26395 multi-turn bug) |
| `ANTHROPIC_API_KEY` | 可选 (实务) | 默认 model (Sonnet 4.6) + 难题 (Opus 4.7) + 轻分类 (Haiku 4.5); credits 耗尽时自动回退 DeepSeek, 故实务上可选 |
| `COHERE_API_KEY` | 可选 | Phase 1B.2 Top-K 重排 (按需) |
| `SDTM_RAG_DEFAULT_MODEL` | 默 sonnet | LiteLLM identifier |
| `SDTM_RAG_FALLBACK_MODEL` | 默 v4-pro 非思考 | D-4 v2 |
| `SDTM_RAG_EMBEDDING_MODEL` | 默 text-embedding-3-small | D-4 v3 cloud; OpenAI API |
| `SDTM_RAG_EMBEDDING_DIM` | 默 1536 | text-embedding-3-small native |
| `SDTM_RAG_MAX_UPLOAD_MB` | 默 100 | 数据集上传上限 (Phase 1C.1) |

**.env hygiene (R-17)**:
- `.env` 已加入 `.gitignore`, 永远不入库
- 误 commit `.env` → 立即 rotate 所有 key (Anthropic / OpenAI / DeepSeek dashboard)
- 共享密钥用 `.env.example` 占位, 不写真值

## Phase 1 PASS 五条 (引用 `../PLAN.md` §9)

每 Phase 收口必通过:
1. evidence 存在 (research/checkpoints/eval 报告)
2. writer 产物 lint + typecheck PASS
3. 独立 reviewer subagent PASS (Rule D 异 type)
4. 规则 A 抽检 (chunker N≥10 / eval N=5 / 1C 假错误集 N≥5)
5. 用户 Bojiang ack

## chunker config 5 lock (来自 1A.0 sanity, 1A.3 writer 必准拠)

详见 `../evidence/checkpoints/phase_1a_0_sanity.md` §4:

- **L-1** mermaid 状态机 (0 嵌套, 不用 stack)
- **L-2** GFM pipe-table 简单 regex (0 HTML rowspan/colspan/`<table>`)
- **L-3** tiktoken cl100k_base 实测强制 (char/4 偏差 23.6% > 20% 容许带)
- **L-4** chapters/ ≥ 50KB 强制 `^### ` 切 (ch04 §4.4 = 9598 cl100k > 8K embedding limit)
- **L-5** terminology core part: H2=1 → part 模式 / H2>1 → codelist 模式

## Testing

```bash
pytest scripts/tests/
ruff check .
mypy server/ scripts/
```

## Roadmap

| Phase | Step | Status |
|-------|------|--------|
| 1A | 0 sanity / 1 scaffold / 2 LiteLLM sanity / 3 chunker / 4 tests / 5 ingest / 6 Rule A | ✅ ALL (4146 chunks / pytest 205+2xfail / Rule A 10/10) |
| 1B + 1B5 | Q&A 服务 + UI + sanity eval 20 题 | ✅ (sanity 92.5%) |
| 1C | Dataset validation (7 规则 + RAG 语义评审) | ✅ (Rule A 错误检出 94.7%) |
| 1D | Full eval 53 题 | ✅ **PASS 88.5%** (DeepSeek; src 82.1% + fact 94.8%) |
| 2 KG | Neo4j + graph reasoning | deferred (cross_domain 召回 61.5% > 50% gate; **95% bar 下待重评**) |
| 次 | 检索质量优化 (src recall → >95%) | BACKLOG — 见 [`../TODO_retrieval_quality.md`](../TODO_retrieval_quality.md) |

## License

Proprietary — internal. 不发布到 PyPI / Docker Hub.
