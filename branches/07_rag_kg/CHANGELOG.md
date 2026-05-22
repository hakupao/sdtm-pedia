# branches/07_rag_kg/ — 改訂履歴

> 本ファイル管理 branches/07_rag_kg/ 配下のPhase / 産出物 / 決定の履歴.

---

## Phase 0 Research v0.1 (2026-05-22)
- 区分: 新規作成
- 内容: 旁枝骨架 (PLAN/EXECUTION_PLAN/_progress.json/research/evidence/prompts/) 創建. Phase 0 (調研 + PLAN 起草) 起動. T2 LLM provider 調研派遣 background document-specialist. T3 chunker feasibility 主 session 着手.
- 上流参照: `docs/DESIGN_RAG_KG.md` (2026-04-16 Approved) + `.work/05_rag_kg/session_2026-04-16_design.md`
- 触発: 用户「Phase 7 RAG+KG 启动」(2026-05-22)
- 着手 PASS 五条: 評価は Phase 0 終結時.

## Phase 0 Research v0.2 (2026-05-22, critic Rule D PASS 1 反映)
- 区分: 内容修正 + 構造修正 (事实错误修正)
- 触発: critic subagent (Rule D 异 type, writer=main session) 独立审 → CONDITIONAL_PASS verdict, 32 findings (3 HIGH / 7 MED / 6 LOW / 4 INFO)
- 修订内容:
  - **F-1 HIGH (PASS 术语)**: PLAN §9 加 "项目根 CLAUDE.md PASS 四条 + 本旁枝因 chunker 高压缩率加规则 A 抽检为第 5 条" 声明
  - **F-2 HIGH (事实错误)**: chunker_feasibility 4 处事实修正 — (a) lb_part4 漏列 (实测含 2 H2 codelist) (b) VARIABLE_INDEX §二 H3 24 → 63 (c) PC examples H4 16 → 14 (Example 4 仅有 Method A+D) (d) supplementary 文件命名 general_part* → supplementary_part1-6; 同时 domains 数 63 → 64 (含 DI/RELREC/RELSPEC/RELSUB; DI 仅 assumptions.md Issue 15 修复后); PLAN §3 / §6.5 同步
  - **F-3 HIGH (未验证项)**: PLAN §8 风险表加 R-13~R-21 (含 6 项 [UNVERIFIED] follow-up + 4 项运维 risk); 加 Phase 1A.0 sanity re-grep verify step
  - F-6 MED (V4 Pro Reasoner): EXECUTION_PLAN §1D.2 "V4 Pro Reasoner 思考模式" → "V4 Pro 非思考 single-turn" (避 LiteLLM Issue #26395)
  - F-7 MED (Haiku context): R-14 加, 1A.2.e 实测
  - F-8 MED (LiteLLM v1.84.0 breaking): 1A.2.d Router fallback sanity
  - F-9/F-10/F-11 MED (运维 risk): R-15 embedding rate limit + R-16 Chroma backup + R-17 .env 管理
  - F-14 MED (reingest trigger): R-18 server/main.py git HEAD 比对 + warn
  - F-19/F-20/F-21 MED (工期): Phase 1A 2.5-3 d → 3-4 d, Phase 1C 3.5-4 d → 5-6 d, Phase 1 总 10-13 d → 13-17 d
  - F-22 MED (并行注解): EXECUTION_PLAN §9 表加注解
  - F-23 MED (PASS 按 Phase 细分): EXECUTION_PLAN §11 新增, 含 1A/1B/1B5/1C/1D/收口 各 PASS 五条
  - F-24 MED (规则 A 抽检 N 明示): PLAN §9.4 细化 (a)chunker N≥10 (b)1B5/1D N=5 ground truth (c)1C N=5 错误标注
  - F-25 LOW (main session 矩阵注): EXECUTION_PLAN §2.1 加 `<main>` 注解
  - F-27 MED (1C reviewer.py 规则 A): PLAN §9.4 (d) 加 reviewer.py N≥5 user-data-row
  - F-32 INFO (06 P7 表述歧义): PLAN §0.1 "06 P7 99.02% coverage" → "06 P7 字段验证 atom coverage 99.02%"
- 落档 evidence: `evidence/review_pass_1.md` (critic 完整审查报告 + 32 findings 详表)
- 修订统计: chunker_feasibility 10 处 + PLAN 12 处 + EXECUTION_PLAN 9 处 = **31 处 Edit**
- 留 5 LOW (F-12/F-13/F-15/F-16/F-17) 待用户 ack 时决定是否当场修
- 作成: main session (Bojiang指示)
- 確認: critic subagent (Rule D 异 type, 已 PASS 1)
- 承認: Bojiang ack 2026-05-22 (PLAN OK + 同意 critic review + 5 LOW 当场修 + commit 可做)

## Phase 0 Research v0.2 final (2026-05-22, 5 LOW 当场修 + 用户全 ack)
- 区分: 内容修正 (LOW 收口)
- 修订内容:
  - F-12 LOW: PLAN §5 Phase 1C.1 已含 "100MB 上限 + chunksize=10000 流式" (v0.2 主修订时已加)
  - F-13 LOW: PLAN §0.2 Out-of-scope 明示 "Phase 1 单用户/单租户, FastAPI uvicorn --workers 1"
  - F-15 LOW: PLAN §7 metadata schema 加注 "不适用字段一律存 None, 不省略 (Chroma filter null vs missing 行为不同)"
  - F-16 LOW: EXECUTION_PLAN 1A.1.d pyreadstat sanity + sas7bdat fallback (v0.2 主修订已含)
  - F-17 LOW: PLAN R-21 Streamlit st.status/progress + 60s timeout (v0.2 主修订已含)
- 用户决策 ack: D-2 LLM 主力 (Sonnet 主+V4-Flash 复检+Opus 难题) + D-3 不接 Plus 代理 + D-4 text-embedding-3-small + D-5 KG defer (1D 后 gate) + D-6 chunker 三策略 + D-7 INDEX+ROUTING 整体注入 + D-8 eval 提前
- Phase 0 全闭环, Phase 1A.0 sanity 起步可启动
- 作成: main session
- 確認: critic Rule D PASS 1 (2026-05-22)
- 承認: Bojiang Zhang (2026-05-22 全 ack)

---
