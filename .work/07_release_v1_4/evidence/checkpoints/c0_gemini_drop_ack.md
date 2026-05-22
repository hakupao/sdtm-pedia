# C0 — Gemini platform DROP ack (2026-05-22)

> **Type**: Phase B → C transition checkpoint
> **Date**: 2026-05-22
> **Trigger**: 用户决定 "Gemini 不做了"

## 1. 背景

v1.4 B1 UI sanity 暴露 Gemini v9 prompt Q-S2 Method label drift FAIL (4/4 mapping 错). Root cause: Gemini v9 简化 525→279L 时漏掉 Method label anchor 同步 (ChatGPT v3 L78 有, Gemini v9 没补).

v1.4 B2 R4 17-题 full regression 原本是 Gemini-only scope (v1.3 D1 deferred 给 v1.4 跑). B1 closed 后等用户 B2 α/β 决策时, 用户决定**整平台 drop**, 而非继续修 v9 prompt + 跑 B2.

## 2. Decision

**Gemini platform → ABANDONED v1.4 onwards**.

- `release/v1.3/self_deploy/gemini/` 保留 (tag immutable, last known good v8.1 LIVE)
- `ai_platforms/gemini_gems/dev/v9_draft/` 保留为历史 (Phase A 写好, 不 promote)
- `ai_platforms/gemini_gems/current/system_prompt.md` 处理待定 (revert v8.1 / 标 DEPRECATED / 移 archive — 见 _progress.json kickoff_decisions_pending §2)
- v1.5 carry "Gemini v9 Method label anchor sync" 一并 ABANDONED
- SYNC_BOARD.md 后续标 SUNSET (Phase F 阶段)

## 3. Impact on v1.4

| Item | 影响 |
|---|---|
| Phase A 输出 | ChatGPT v3 / Claude v3 / NotebookLM v3 valid; Gemini v9 invalidated (history only) |
| Phase B B1 (16 cells UI sanity) | 3 平台 12/12 PASS (Gemini 4 cells excluded); APPROVE |
| Phase B B2 (Gemini R4 17 题) | **ABANDONED**, Gemini-only scope, N/A |
| Phase B → C gate | 满足 (B1 三家 12/12 + B2 N/A) |
| Phase C 4 项 carry (C1-C4) | 全部针对 3 平台 / KB / pipeline, 不受 Gemini drop 影响 |
| Phase D release cut | `release/v1.4/` 包含 chatgpt + claude + notebooklm 3 平台 + KB + KNOWN_LIMITATIONS 标 Gemini ABANDONED |

## 4. Updates applied

- `_progress.json`:
  - `phase`: B → C
  - `step` / `status` 更新 (3-platform scope, Gemini ABANDONED)
  - `gemini_platform_status` 新增 (ABANDONED 详细记录)
  - `phase_b_b2_abandoned` 新增
  - `carries_in_scope` 移除 Gemini-only main carry (RETRO §二.1)
  - `phases.B.status` → closed_b1_pass_3_platform_b2_abandoned_gemini_dropped
  - `phases.C.status` → kickoff
  - `kickoff_decisions_pending` 更新

## 5. Next

- Task #2: 起草 KNOWN_LIMITATIONS §0 reconcile (含 Gemini ABANDONED 声明)
- Task #3-#6: 并行/顺序派发 C1-C4
- Task #7-#8: C4 后触发 3 平台 rebuild + Q-S2 复测
- Phase D-F: release cut + audit + retro
