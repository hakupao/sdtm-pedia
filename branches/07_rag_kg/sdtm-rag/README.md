# sdtm-rag — SDTM Knowledge Base RAG + Dataset Validation

> Phase 7 RAG+KG 旁枝实际代码仓 (Phase 1A 起开始建).
> Status: **Phase 1A.1 scaffold** (脚手架已建, chunker 实现在 1A.3).
> 上游 PLAN/EXECUTION_PLAN: [`../PLAN.md`](../PLAN.md), [`../EXECUTION_PLAN.md`](../EXECUTION_PLAN.md).
> 单用户/单租户 (PLAN §0.2 Out-of-scope), uvicorn `--workers 1`.

---

## What

为 SDTM 知识库 (`../../../knowledge_base/`, 296 md / 9.8MB / 4304 chunks 估) 提供:

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
                            │ V4-Flash (复检)  │
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

## Quick Start (本地 dev)

### 1. 准备 `.env`

```bash
cp .env.example .env
# 编辑 .env, 填入 ANTHROPIC_API_KEY / OPENAI_API_KEY (必), DEEPSEEK_API_KEY / COHERE_API_KEY (可选)
```

### 2a. 直接 Python (推荐 dev, Python ≥ 3.11)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
# 跑 ingest (Phase 1A.5 实现后)
python scripts/ingest.py
# 起 server
uvicorn server.main:app --reload --port 8000
# 另一终端起 UI
streamlit run ui/streamlit_app.py --server.port 8501
```

### 2b. Docker Compose (推荐 demo / 公司机器)

```bash
docker compose up --build
# api  → http://localhost:8000  (FastAPI)
# ui   → http://localhost:8501  (Streamlit)
```

Knowledge base 通过只读 volume `../../../knowledge_base:/app/knowledge_base:ro` 挂入 (H-1 read-only 硬约束).

## Environment Variables

详见 `.env.example`. 关键说明:

| Var | 必需? | 说明 |
|-----|-------|------|
| `ANTHROPIC_API_KEY` | ★ 必 | LiteLLM 主答 (Sonnet 4.6) + 难题 (Opus 4.7) + 轻分类 (Haiku 4.5) |
| `OPENAI_API_KEY` | ★ 必 | Embedding (text-embedding-3-small) |
| `DEEPSEEK_API_KEY` | 可选 | Cross-check / fallback (V4-Flash 非思考模式; **不**用 V4-Pro Reasoner 因 LiteLLM Issue #26395) |
| `COHERE_API_KEY` | 可选 | Phase 1B.2 Top-K 重排 (按需) |
| `SDTM_RAG_DEFAULT_MODEL` | 默 sonnet | LiteLLM identifier |
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
| 1A | 0 sanity / 1 scaffold / 2 LiteLLM sanity / 3 chunker / 4 tests / 5 ingest / 6 Rule A | 0 ✅ / 1 🟢 / 2-6 ⏳ |
| 1B | Q&A 服务 + UI | ⏳ |
| 1B5 | Sanity eval 20 题 | ⏳ |
| 1C | Dataset validation | ⏳ |
| 1D | Full eval 50 题 | ⏳ |
| 2 KG | Neo4j + graph reasoning | deferred (gate: 1D RELATION 召回 < 50%) |

## License

Proprietary — internal. 不发布到 PyPI / Docker Hub.
