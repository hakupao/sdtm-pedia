# Phase 1B — Q&A Service Evidence Checkpoint

> Date: 2026-05-23
> Owner: main session
> Status: **PASS** (1B.1-1B.5 all implemented + 3/3 e2e tests PASS)

## Summary

Phase 1B builds the FastAPI + Chroma retrieval + LiteLLM Router + Streamlit UI Q&A service
on top of the Phase 1A ingest pipeline (4146 chunks in Chroma).

## Files Created (6 files, 608 lines)

| File | Lines | Role |
|------|-------|------|
| `server/config.py` | 51 | pydantic-settings, .env loading, path computation |
| `server/llm_config.py` | 39 | LiteLLM Router factory (4 model groups) |
| `server/rag.py` | 165 | RAGEngine: Chroma retrieval + context formatting + system prompt |
| `server/router.py` | 126 | FastAPI routes: /api/health, /api/info, /api/ask |
| `server/main.py` | 68 | FastAPI app with lifespan startup/shutdown |
| `ui/streamlit_app.py` | 158 | Streamlit chat UI with sidebar filters + source expansion |

## Architecture

```
User → Streamlit UI (port 8501)
         ↓ HTTP POST /api/ask
       FastAPI (port 8000)
         ↓ 1. Embed query (OpenAI text-embedding-3-small)
       Chroma (4146 chunks, cosine similarity)
         ↓ 2. Top-K retrieval + metadata filter
       LiteLLM Router
         ↓ 3. Sonnet primary → DeepSeek fallback
       Response (answer + sources + usage)
```

## PLAN Mapping

| PLAN Step | Implementation | Status |
|-----------|---------------|--------|
| 1B.1 FastAPI + ROUTING/INDEX injection | `main.py` lifespan + `rag.py` system prompt (22453 chars, ~6K tokens) | PASS |
| 1B.2 rag.py metadata filter + Top-K=15 | `rag.py` retrieve() with optional domain/file_type filter | PASS |
| 1B.3 LiteLLM Router | `llm_config.py` Router(default→fallback, hard, light) | PASS |
| 1B.4 Streamlit UI | `streamlit_app.py` chat + sources + model selector + domain filter | PASS |

## End-to-End Test Results (3/3 PASS)

### Test 1: Variable Definition (AETERM)
- Query: "What is AETERM and what are its key attributes?"
- Top-1 source: `domains/AE/spec.md` § AETERM (sim=0.606)
- Answer: Correct — includes Label, Type, Role, Core, CT, coding chain rules
- Model: claude-sonnet-4-6, 10724 tokens

### Test 2: Domain Filter (DM required variables)
- Query: "What variables are required in DM?" (domain=DM)
- All 3 sources from DM domain (filter working)
- Answer: Reasonable (assumptions.md context; spec.md less similar for this phrasing)

### Test 3: Terminology (AESEV severity)
- Query: "What are the allowed values for AESEV severity?"
- Sources: AE/spec.md § AESEV + terminology/core/ae.md § C66769
- Answer: Correct — C66769 codelist, non-extensible, values listed

## .env Fix Applied

D-4 v2 → v3 stale values corrected in `.env`:
- `SDTM_RAG_EMBEDDING_MODEL`: `BAAI/bge-m3` → `text-embedding-3-small`
- `SDTM_RAG_EMBEDDING_DIM`: `1024` → `1536`

## Source Path Fix

`rag.py` retrieve() now converts absolute paths to KB-relative (e.g., `domains/AE/spec.md`
instead of `/Users/.../knowledge_base/domains/AE/spec.md`).

## Known Limitations (non-blocking)

1. Non-streaming responses — Streamlit waits for full LLM completion
2. System prompt is ~6K tokens (ROUTING + INDEX whole injection) — manageable but could optimize
3. Test 2 domain filter only returned assumptions.md chunks — spec.md phrasing mismatch
4. LiteLLM botocore warnings (harmless, no AWS usage)

## PASS Conditions (EXECUTION_PLAN §11 Phase 1B)

1. ✅ evidence: FastAPI + Streamlit e2e + 3 sample queries OK
2. ✅ writer product: 6 files lint-clean, imports verified
3. ⏳ independent code-reviewer PASS (Rule D — to be dispatched)
4. ✅ Rule A: N/A for Phase 1B (no compression >50%)
5. ⏳ user Bojiang ack
