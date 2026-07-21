# Production Wire-In (S1+S2 levers) — Rule D Independent Review + Resolution

> 日期: 2026-06-09
> Writer: main session (config.py / main.py / rag.py / router.py edits)
> Reviewer: `oh-my-claudecode:code-reviewer` (opus) — **异 subagent_type, 非 writer 自审 (Rule D PASS)**
> Verdict: **APPROVE_WITH_NITS** (0 CRITICAL / 0 HIGH / 2 MEDIUM / 2 LOW / 2 NIT)

## 改动范围 (Step 1)

把 P1 验证过的两个检索杠杆 (S1 `structured_lookup` + S2 `hybrid` BM25) 从"仅 eval flag"接进生产 `/ask`,默认开:
- `config.py`: 加 `structured_lookup_enabled=True` + `hybrid_enabled` 翻 `True` (均 `SDTM_RAG_` 环境变量可关)
- `main.py`: lifespan 转发 5 个杠杆参数进 `RAGEngine`,计时 init,log 杠杆状态
- `rag.py`: **embed-once 重构** — query 原文从"每次 dense + 每个 S1 lookup 各嵌一次 (最多 ~6 次/查询)"改为"全程嵌一次复用"
- `router.py`: `/info` 暴露杠杆状态

## Reviewer 的关键验证 (摘)

- **`need_q_emb` guard 全 12 分支 (4 expansion × S1 on/off) 逐一 trace**: `q_emb` 仅在 pure-hyde+S1-off 路径为 None,而该路径证明从不读 `q_emb` (嵌 hypo 而非 query,且不进 `_apply_structured_lookup`)。**唯一脆弱行,且正确。**
- **behavior-preserving 结论**: 传入预算 embedding 只改"是否调 `litellm.embedding`",Chroma `query_embeddings` payload + 下游 fusion/ranking 对同输入字节一致 → 这正是 per-question eval 完全相同的原因。
- env-override rollback 实测 `false` → Python `False` (字段名 `SDTM_RAG_STRUCTURED_LOOKUP_ENABLED` / `SDTM_RAG_HYBRID_ENABLED` 正确)。
- `/info` 读的 3 个引擎属性在 `__init__` 无条件赋值 → 不会 AttributeError。

## 6 findings + 处置

| # | 级别 | 问题 | 处置 |
|---|------|------|------|
| M-1 | MEDIUM | 无任何 guard 强制 "S1+S2 必须一起开"。半套 env rollback (S1=off / hybrid=on) 静默落入已知坏配置 (single 96→83),无报错 | **已修**: `main.py` 生产 boot 路径加 `log.warning` (eval ablation 路径不受限,仍可单测 hybrid) — 实测 rollback 配置下 warning 正确触发 |
| M-2 | MEDIUM | `_embed_query` 无 429 retry,而兄弟 `_llm`/`_rerank` 有;重构后它是所有 embedding 流量唯一入口 (非回归,但集中后该补) | **已修**: 加同款 5-attempt 指数退避 (仅错误路径,happy-path 不变 → 回归 eval 仍字节一致) |
| L-1 | LOW | `_search` 的 `query_text` 在传入 embedding 时变 vestigial | **跳过**: docstring 已说明条件行为,reviewer 自评"as-is acceptable" |
| L-2 | LOW | `rag_init_s` 仅 startup log,未上 `/info` | **跳过**: startup log 已足够 (0.41s 已记录) |
| N-1 | NIT | `/info` `hybrid_fusion` None 语义未注释 | 跳过 (cosmetic) |
| N-2 | NIT | config 注释用 `→`/`—` 非 ASCII | 跳过 (该文件既有注释已用 `—`,一致) |

## 修后复验 (writer 自验, 非审批)

| 项 | 结果 |
|----|------|
| py_compile 4 文件 | OK |
| pytest scripts/tests/ | **214 passed** (0 fail) |
| embed-once 回归 (retrieval-only v2 102q, levers on) | 逐题**等于 Step 0** (concept 100 / cross 96 / mixed 100 / single 100 / overall 99.02%) |
| embed-once 证明 (2-target S1 query) | `litellm.embedding` 调用 **恰 1 次** (重构前为 3);via_lookup chunk 命中 |
| FastAPI /info smoke (both on) | 200,structured_lookup=True hybrid=True,**无 warning**,startup 0.41s |
| guard 证明 (env S1=off hybrid=on) | warning **正确触发** + /info 反映 + env-override rollback 端到端 OK |

> M-1/M-2 修复只动 boot 路径 + 错误路径,不碰 retrieval happy-path,故 embed-once 字节一致结论不受影响。
> 全文 review (含 12 分支 trace 表) 见本 session transcript / agent a25900dace8da90f1。
