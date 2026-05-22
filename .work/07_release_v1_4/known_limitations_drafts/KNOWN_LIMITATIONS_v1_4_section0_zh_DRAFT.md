---
lang: zh
slug: known-limitations
order: 50
title: "已知限制"
release: v1.4
draft_status: DRAFT_phase_c_pre_release
---

# 已知限制 — v1.4 §0 reconcile DRAFT

> **DRAFT**: 仅 §0 reconcile 草稿. §1-§6 byte-exact 继承 v1.3 (Phase D 阶段最终 cut). en/ja 翻译留 Phase D 同步.

---

## 0. v1.4 审计范围 (2026-05-22 更新)

v1.4 是 SDTM Pedia 的 **prompt-pass 级**版本 — 针对 3 个仍在维护的 AI 平台 (ChatGPT GPTs, Claude Projects, NotebookLM) 进行 system prompt / instructions 的全栈 clean rewrite, 移除多版本迭代累积下来的化石层, 把 KB-grounding 重新立为主路径. 同时合并 4 项 v1.3 遗留 minor carry.

**重要变更 — Gemini Gems 平台 v1.4 起转为"维护但不再 sanity 测试"模式**, 详见下方 §0.A.

### 0.A. Gemini Gems 平台 — MAINTAINED_NO_SANITY_TEST (v1.4 onwards)

自 v1.4 起, **SDTM Pedia 不再对 Gemini Gems 跑 sanity / R4 回归测试**, 但**继续 best-effort 维护**:

- **决策日期**: 2026-05-22 (用户口头 clarification)
- **触发因素**: v1.4 Phase B B1 light sanity 暴露 Gemini v9 prompt 在 PP RELREC Method A/B/C/D 题上完全 hallucinate (4/4 mapping 全错). 同时 Gemini Pro 配额约束 (~4 题/5h 滚动 window) 长期阻碍全 17 题 R4 回归. 综合考虑, **测试不继续** (避免 quota 浪费); **优化继续** (KB delta + 关键 prompt 修).
- **v1.4 内 Gemini 优化交付**:
  - v9 system_prompt 加 Method label anchor 段 (paralleling ChatGPT v3 L77-80): A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
  - v1.4 KB delta (PP/examples §6.3.5.9.3 mapping table) 自动通过 KB grounding 影响 Gemini gem 行为 (即使没 bundle 上传, prompt 改后 gem 的 reasoning 会引用此 table).
- **维护边界**:
  - **继续 ✅**: KB delta 流入 Gemini gem instructions (release/ 含 Gemini bundle 改动); 关键 prompt 修正 (anchor / 错误 mapping 等明显 KB-grounding 修).
  - **不继续 ❌**: 跑 sanity 题集 (B1 4 题 × Gemini, R4 17 题 Gemini Pro full regression, smoke 题验证); 锁步看板 (R3+ 维护期看板已降级, Phase 0-5 gate 历史保留); 用户验证由 self-deploy 用户自跑.
- **保留**: `release/v1.3/self_deploy/gemini/` 作为 last sanity-verified baseline (v8.1 LIVE, 16/17 R3 PASS). v1.4 Gemini gem 在此 baseline 上加 v9 refactor + Method label anchor, 但**无 sanity 测试覆盖**, 用户自验.

### 0.B. v1.4 新增内容 (3 平台 in scope)

- **阶段 A — Prompt clean rewrite** (3 平台 system prompt / instructions clean rewrite, 经独立 Rule D reviewer 审计):
  - **ChatGPT v3 system_prompt** (120→119 行 + 显式 Method label anchor mapping 4 行): 移除 v1.0-v1.3 迭代注释, KB-grounding 优先 default, A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
  - **Claude v3 system_prompt** (125→133 行, 后经 critic reviewer 找到 attempt 1 truncated 19→7 file table → attempt 2 surgical fix PASS_WITH_OBSERVATIONS): 5 essential rules + regex-gated CO-N + Files A-S table 全保留.
  - **NotebookLM v3 instructions** (157→156 行): footer Sources citation 语义等价保留 (非 byte-exact, 但行为 preserved), 移除 v1.0-v1.3 迭代化石.
  - **A3.1 Claude bundle pipeline architectural fix** (`extract_examples_data.py` SECTION_HDR_RE capture): 修复 v1.3 Phase D verifier 发现的 `## §N.N.N` heading 不被 capture 的 pipeline gap. 实战在 B1 UI sanity Q-S2 Claude 命中 (paper PARTIAL → UI PASS+).

- **阶段 B — Light sanity (3 平台 12/12 PASS, Gemini 4 cells excluded due to drop)**:
  - B1 UI-level (Chrome MCP fire-and-forget): 4 题 × 3 平台 = 12 cells = **10 PASS+ + 2 PASS + 0 PARTIAL + 0 FAIL = 100% PASS**.
  - 题集: Q-S1 BECAT EXTRACTION (v1.3 carry), Q-S2 PP RELREC Method (v1.3 触发 v1.4 main refactor), Q-S3 TR TRSTRESN/TRSTRESU typo, Q-S4 DI domain (NotebookLM bucket 25 rename).
  - B2 R4 17 题 full regression 原 Gemini-only scope: **N/A — 不再 sanity 测试 Gemini** (详 §0.A; 优化继续, 测试不继续).

- **阶段 C — Minor carries (4 项)**:
  - **C1 section_coverage.jsonl 完整 pipeline rerun** — 关闭 v1.3 A5 baseline stale.
  - **C2 UNSOURCED 启发式分类器修 + N=80 抽检** — Rule D `scientist` v1.3 找到的 DERIVED_FROM_XLSX→REASONABLE_INFERENCE bias 修, N=40 (v1.3) + 40 (v1.4 new) 扩展.
  - **C3 NotebookLM bucket 25 UX 教程 + screenshot** — v1.3 实操中用户漏删旧 source (43→应 42), v1.4 DEPLOY_GUIDE 加显眼提示 + Chrome MCP screenshot 教程.
  - **C4 ChatGPT PP RELREC Method label KB anchor** — `PP/examples.md §6.3.5.9.3` 加显式 4 行 mapping table, 解决 v1.3 Q-S2 ChatGPT PARTIAL label drift (KB + prompt 双层 anchor).

### 0.C. v1.3 §0 项 reconcile

| v1.3 §0 项 | v1.4 状态 |
|---|---|
| 4 平台 system_prompt/instructions 全栈重构 (主线) | **resolved** — 4 平台 (ChatGPT/Claude/NotebookLM/Gemini) 完成 v3/v9 clean rewrite; Gemini v9 加 Method label anchor (Phase A 主体 + 2026-05-22 增补); 仅 Gemini sanity 测试不继续 (详 §0.A) |
| 437 UNSOURCED_MANUAL 全量分类 | **部分 resolved** — 启发式 bias 修 + N=80 抽检 done; 全 437 逐条仍 defer v1.5 |
| Tier B 节 11-25 + 全 level-2 (~156 节) | **defer v1.5** — 工程量 > v1.4 体量 (~5-7 工作日 单独 KB pass cycle), 留独立 release |
| Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW Tier-B MEDIUM 修复 | **defer v1.5** — 见 06 Deep Verification §二; 与 Tier B 全量同期处理 |
| section_coverage.jsonl 完整 pipeline rerun | **resolved** — v1.4 C1 done |
| R4 全 17 题 Gemini Pro 回归 | **N/A — 不再 sanity 测试 Gemini** (Pro quota 约束 + 测试停; 优化继续) |
| PASS+ §1.2 严格"仅 AHP"范围扩展 | **acknowledged** — v1.4 sanity 中继续应用扩展定义 (KB-grounding + 超基线深度 = PASS+); 未来 smoke 设计正式纳入 |

### 0.D. v1.4 未做项 (推迟至 v1.5+)

- **Tier B 节 156 节** (Batch H 排名 1-10 ~470 atoms + Batch S 21-25 ~10 atoms + level-2 24 节 ~600 atoms) — 工程量 > v1.4 体量, 留独立 KB pass cycle.
- **437 UNSOURCED_MANUAL 全量逐条分类** — v1.4 仅启发式 fix + N=80 抽检, 全量精确化留 v1.5.
- **Phase 7 RAG + KG 启动** — 与 prompt refactor 并行不经济, 留独立 phase (设计已完成 `docs/DESIGN_RAG_KG.md`).

### 0.E. 外观 / 部署注意事项

- **Gemini 用户**: v1.4 提供 Gemini gem 增量 (system_prompt v9 clean rewrite + Method label anchor + KB delta). 但本平台**无 sanity 测试覆盖**, 答题正确性请用户自验. 推荐对正确性要求高的场景使用 ChatGPT / Claude / NotebookLM (本 release 有 sanity 覆盖).
- **NotebookLM bucket 25** (v1.3 carry, v1.4 加强教程): 现有 v1.0-v1.3 NotebookLM 部署如仍含旧 source `25_td_meta_ti_ts_oi.md`, 上传 `25_td_meta_ti_ts_oi_di.md` 后**请手动删除旧 source** (清理后 43 → 42). v1.4 `V1_4_DEPLOY_GUIDE.md` 含显眼提示 + screenshot 教程.
- **ChatGPT PP RELREC Method label**: v1.4 KB + prompt 双层 anchor 已 cover, v1.3 PARTIAL drift 应 resolved (sanity 复测 Phase C 收尾验证).

---

(以下 §1-§6 byte-exact 继承 v1.3, Phase D cut 时不动)
