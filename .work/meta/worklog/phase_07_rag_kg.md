# Phase 07 RAG+KG (branches/07_rag_kg/) — 工作日志

> Phase 7 (RAG + Knowledge Graph) 旁枝 entries. PLAN 在 `branches/07_rag_kg/PLAN.md` + EXECUTION_PLAN 在 `branches/07_rag_kg/EXECUTION_PLAN.md` + 上游设计 `docs/DESIGN_RAG_KG.md`.

> **新 entry** append 到本文件 (按日期顺序), 保持 H2 标题 `## YYYY-MM-DD <topic> <verb>` 格式.

---

## 2026-05-22 branches/07_rag_kg/ Phase 0 Research CLOSED (调研 + PLAN v0.2 + critic Rule D PASS 1 + 用户 ack)

- **触発**: 用户「Phase 7 RAG+KG 启动」(2026-05-22), 指示「先调研+写方案, 尽量保证不返工」+ LLM 配置 (DeepSeek V4 Pro + ChatGPT Plus 代理 + Anthropic API 接口预留)
- **完了の作業**:
  - **STEP A 仓库骨架** (T1): `branches/07_rag_kg/` 创建 (PLAN.md / EXECUTION_PLAN.md / CHANGELOG.md / _progress.json / research/ / evidence/checkpoints/ / evidence/failures/ / prompts/). Tier 2 schema _progress.json
  - **STEP B T2 LLM 调研 (background document-specialist)**: WebSearch 调研 DeepSeek V4 Pro / ChatGPT Plus 代理 / Anthropic 2026 模型 / LiteLLM 兼容性. 落档 `research/llm_providers_2026-05-22.md` (含决策表 + 6 个 [UNVERIFIED] + Sources 18 个 URL)
  - **STEP C T3 chunker feasibility 调研 (main session 直接)**: KB 真实 grep — 296 md / 64 domain (DI 仅 assumptions Issue 15 修复后加) / 2164 spec.md 变量 / 1005 codelists / lb_part1-4 / VARIABLE_INDEX 63 H3 / PC examples 14 H4 / TA 20 mermaid / ch04 130KB. 落档 `research/chunker_feasibility_2026-05-22.md` (含 7 风险 R-1~R-7 + Phase 1A.0 6 [UNVERIFIED] + 5 chunker 实现规范)
  - **STEP D PLAN.md v0.1 + EXECUTION_PLAN.md v0.1 起草** (main session writer, 整合 T2 + T3): 5 处偏离设计 (A-1 examples domain-aware + A-2 INDEX 整体注入 + A-3 LLM 默 Sonnet + B-1 eval 提前 + B-2 KG defer gate); Phase 1A-1D + Phase 2 拆分; 12 决策表 (LLM/embedding/framework/chunker); 21 风险表 R-1~R-12; PASS 五条 + 工期 10-13 d (v0.1)
  - **STEP E critic Rule D PASS 1** (foreground): `oh-my-claudecode:critic` subagent 派发 (writer=main session 异 type), 审 PLAN + EXECUTION_PLAN + 2 research + 上游 design doc + CLAUDE.md. ADVERSARIAL 模式触发 (因第 1 处事实错误 lb_part4 漏列 surface). Verdict = **CONDITIONAL_PASS**, 32 findings (3 HIGH / 7 MED / 6 LOW / 4 INFO). 落档 `evidence/review_pass_1.md`
  - **STEP F v0.1 → v0.2 修订** (main session writer): 31 处 Edit 跨 3 文件
    - chunker_feasibility 10 处 (F-2 4 事实 + §0 TL;DR 数字 + §1 KB 表 + §6 LB part4 + §8 VARIABLE_INDEX H3 + §13 supplementary_part 命名 + §9 总数表)
    - PLAN 12 处 (F-1 PASS 术语 + F-2 §3/§6.5 同步 + F-3 R-13~R-21 加 + F-4/5 evidence 说明 + F-19/20/21 工期 + F-23 PASS 按 Phase + F-24 规则 A 抽检 N + F-27 1C reviewer.py + F-32 06 P7 表述)
    - EXECUTION_PLAN 9 处 (F-6 V4 Pro 非思考 + F-8 1A.2.d-e + F-11 1A.1.c-d + F-22 §9 注解 + F-25 main session 注 + F-23 §11 Per-Phase PASS 五条 + Phase 1A.0 sanity step)
  - **STEP G 5 LOW 当场修** (用户 ack 后):
    - F-12 (100MB 上限 + chunksize) — v0.2 主修订时 PLAN §5 1C.1 已含
    - F-13 (单用户/单租户) — PLAN §0.2 Out-of-scope 加明示
    - F-15 (metadata null vs omit) — PLAN §7 metadata schema 加 F-15 注释
    - F-16 (pyreadstat fallback) — EXECUTION_PLAN 1A.1.d 已含
    - F-17 (Streamlit timeout UX) — PLAN R-21 已含
  - **STEP H 顶层文档同步**:
    - `.work/MANIFEST.md`: 加 Chain 07_RAG + Plan Map 加 1 行 + Quick Ref 加 1 行
    - `CLAUDE.md` Key Paths: 加 1 行 (≤ 80 字符)
    - `docs/PROGRESS.md`: Phase 7 状态 ⏸ → 🟢 + milestone 列加 2026-05-22 entry
    - `.work/meta/worklog/INDEX.md`: 加 phase_07_rag_kg.md 行
    - `.work/meta/worklog/phase_07_rag_kg.md`: 新建本文件
  - **STEP I single commit + push**: Phase 0 closure
- **関鍵決定 (用户全 ack 2026-05-22)**:
  - **D-1**: 仓库布局 `branches/07_rag_kg/sdtm-rag/` (跟 SDTM-pedia git 一起, 不开 sibling 项目)
  - **D-2**: LLM 主力 = `claude-sonnet-4-6` 主答 + `deepseek-v4-flash` 复检 (非思考模式绕 LiteLLM Issue #26395) + `claude-opus-4-7` 难题 + `claude-haiku-4-5` 轻分类
  - **D-3**: ChatGPT Plus 代理**不入生产** (违反 OpenAI ToS + 极低稳定性 + 数据安全风险), 仅在 chatgpt.com 网页用 Plus 配额做 prototype, LiteLLM 留 `openai/` base_url 接口供后续独立 OpenAI API 账户接入
  - **D-4**: Embedding = OpenAI `text-embedding-3-small` (1536d, 全 KB embedding 约 $0.01) + bge-m3 local fallback
  - **D-5**: Phase 2 KG **默认 defer**, 启动 gate = Phase 1D eval RELATION 类 12 题召回 < 50% (50% 阈值 1D 后用户 + main 复评, 不锁死)
  - **D-6**: chunker 三策略 — (a) examples.md domain-aware (探测最深 heading level, PC H4 嵌套 14 chunk 不是 16) + (b) chapters size-aware (>50KB → ### / 20-50KB → ## / <20KB → 整文件) + (c) terminology LB part 模式识别 (part1-3 各 1 codelist + part4 含 2 codelist 异常)
  - **D-7**: ROUTING.md (2K tok) + INDEX.md (4K tok) 都整体注入 system prompt (~6K base, 给 LLM 64 域 + 6 chapters + 91 terminology 入口映射)
  - **D-8**: Eval 提前 — Phase 1B5 sanity (20 题) 在 ingest 后立刻跑, Phase 1D 全 eval (50 题) 留收口前; 避免最后才发现召回拉胯
  - **D-r522-1 critic Rule D PASS 1 ADVERSARIAL 触发**: critic 在 spot-check 第 1 处事实错误 (lb_part4 漏列) 后升级 ADVERSARIAL 模式, 重新独立 grep 验证所有数字, surface F-2 系统性 evidence-vs-claim drift (4 处). 教训: chunker feasibility 类 evidence 文档下次写时, main session 自己 grep 后必须等 critic 异 type 再做 1 轮独立 grep verify
  - **D-r522-2 Phase 0 → Phase 1A.0 sanity 强制 gate**: PLAN.md v0.2 新增 Phase 1A.0 step (re-grep verify R-13 6 项 [UNVERIFIED]), 不信任 chunker_feasibility 估算; 6 项落实到 `evidence/checkpoints/phase_1a_0_sanity.md` 才进 1A.3 chunker writer
- **Carry-over for next session**:
  - **NEXT**: Phase 1A.0 sanity re-grep verify (supplementary_part / qs_part / questionnaires 43 文件 H2 / mermaid 嵌套 / 表格变体 / tiktoken 实测) — 工期 0.3 d
  - **その後**: Phase 1A.1 仓库脚手架 `branches/07_rag_kg/sdtm-rag/` 起 → 1A.2 LiteLLM v1.85.1 sanity (5 sub-step 含 R-8/R-14/R-19 验证) → 1A.3 chunker 6 类 fan-out 3 batch 并列 → 1A.4 chunker 测试套件 → 1A.5 ingest 全量 + Chroma backup → 1A.6 规则 A 抽检 (06 P5 reverse_ledger N=10 atom)
  - **Phase 2 deferred** (gated): KG 启动条件 = Phase 1D eval RELATION 召回 < 50%
  - **PASS 五条 Open**: 全 PASS for Phase 0; Phase 1A PASS 待 1A.6 完成
- **下一步**: commit + push (Phase 0 closure single commit)

---
