# Release v1.4 Plan — 4-Platform Prompt Full-Stack Refactor + 7 Minor v1.3 Carries

> **入口建立**: 2026-05-20 PM (post v1.3 tag cut + RETROSPECTIVE)
> **上一版**: tag `v1.3-company-release` (KB pass + 4 平台 rebuild + light sanity APPROVE)
> **本版定位**: **4 平台 prompt 全栈 refactor** — Gemini v8.1 525 行 fossil layer → v9 ~200 行 + 5 essential rules + regex-gated CO-N; ChatGPT/Claude/NotebookLM 同步 clean rewrite, 不留迭代履历, KB-grounding 优先 default
> **Tier**: **Tier 3** (>15 step, 多天, prompt+R4+release+minor 多旁线联动, 高 stakes)
> **终止条件**: tag `v1.4-company-release` cut + 4 平台 system_prompt deployed + R4 17/17 ≥ baseline + RETROSPECTIVE.md 三段齐备 + post-audit pass 闭环
> **预估工期**: 3-5 工作日 (含 Gemini Pro quota 跨 cycle 等待)

---

## § 0. 背景: v1.3 RETROSPECTIVE §二 列出的 8 项 v1.4 carries

来自 `.work/07_release_v1_3/RETROSPECTIVE.md` §二:

| # | 项 | 类别 | 来源 | scope |
|:-:|---|---|---|:-:|
| **1** | **Gemini system_prompt v8.1 prompt bloat → v9** (525 行 17 CO-N → ~200 行 5 essential rules + regex-gated CO-N) | **MAIN** | v1.3 Phase C Q-S2 Gemini PP RELREC FAIL 触发 + 用户直觉 "履历都写进去了, 感觉不好" | **IN** |
| 2 | 4 平台 prompt 同样有 fossil layer (ChatGPT/Claude/NotebookLM 一并 clean rewrite) | MAIN (扩展) | v1.3 RETRO §二.2 | **IN** |
| 3 | Claude bundle 缺 PP RELREC Quick Reference (pipeline architectural gap, `## §N.N.N` heading 不被 v2 extract_examples_data.py capture) | minor architectural | v1.3 Phase D verifier 找到 | **IN** |
| 4 | ChatGPT method label 混淆 (PP RELREC Method A=B 的 label drift, 内部 prior 覆盖 KB) | minor KB anchor | v1.3 Phase C Q-S2 ChatGPT | **IN** |
| 5 | 全 437 UNSOURCED_MANUAL 分类 + 启发式分类器 bias 修 (v1.3 N=40 抽样验过, 全量分类逐条 grep pdf_atoms.jsonl) | minor (heavy) | v1.3 RETRO §二.5 + 06 P5 遗留 | **IN partial** (启发式修 + N=80 expansion; 全 437 拖 v1.5) |
| 6 | Tier B 156 节 (Batch H 1-10 470 atoms + Batch S 21-25 ~10 atoms + Level2 24 节 ~600 atoms) | minor (>1 周) | v1.3 RETRO §二.6 / 06 P6 Tier B 拖 | **DEFER v1.5** (工程量 > v1.4 体量, 单独 KB pass) |
| 7 | NotebookLM 旧 bucket 25 UI 操作清理教程 + screenshot | minor UX | v1.3 RETRO §二.7 + V1_3_DEPLOY_GUIDE | **IN** |
| 8 | section_coverage.jsonl 完整 pipeline rerun (md_atoms 增量 → p4a forward matcher → p4b aggregate) | minor (工程量 < 1 天) | v1.3 RETRO §二.8 + A5 baseline stale | **IN** |

**注**: v1.3 RETRO §二.1 + §二.2 合并为 v1.4 MAIN (4 平台 prompt full-stack refactor); §二.3-§二.8 为 7 minor carries.

---

## § 1. v1.4 Scope 决策

### 1.1 In scope (本 release 必须完成)

| Item | 来源 carry | Phase |
|---|---|:-:|
| **Gemini system_prompt v9 clean rewrite** (525→~200 行, 5 essential rules, regex-gated CO-N, KB-grounding 优先 default) | RETRO §二.1 (MAIN) | A |
| **ChatGPT system_prompt v3 clean rewrite** (移除迭代履历 annotation, KB-grounding 优先, method label 显式锚) | RETRO §二.2 + §二.4 (MAIN + #4) | A |
| **Claude Project instructions v3 clean rewrite** (移除 v5/v6/v7/v8 fossil annotation, KB-grounding 优先) | RETRO §二.2 (MAIN) | A |
| **NotebookLM instructions v3 clean rewrite** (移除迭代履历 annotation, citation footer style 保留 v1.3) | RETRO §二.2 (MAIN) | A |
| **Claude bundle pipeline fix** (capture `## §N.N.N` section headings from domain examples.md, OR add Quick Reference section to v2 extract include-list) | RETRO §二.3 (#3) | A |
| **4 平台 prompt Rule D reviewer pass** (每平台独立 reviewer, writer ≠ reviewer 严格隔离) | Rule D | A 收尾 |
| **4 平台 light sanity (4 题 × 4 平台 = 16 cells)** 同 v1.3 Phase C 复用 (验 v9 prompt 不 regression KB-grounding) | sanity | B |
| **R4 17-question full regression on Gemini v9** (Pro only, 4-5 cycle 跨日 16-20h, OR Flash-Lite tradeoff) | v1.3 D1 deferred | B partial |
| **section_coverage.jsonl 完整 pipeline rerun** | RETRO §二.8 (#8) | C |
| **UNSOURCED 启发式分类器 bias 修 + N=80 expansion** (PDF grep 优先 → REASONABLE_INFERENCE; xlsx fallback) | RETRO §二.5 (#5) partial | C |
| **NotebookLM bucket 25 UX 教程 + screenshot 加 v1.4 DEPLOY_GUIDE** | RETRO §二.7 (#7) | C |
| **KNOWN_LIMITATIONS reconcile + §0 v1.3 → v1.4 移项** | release 流程 | D |
| **Cut release/v1.4/ + tag `v1.4-company-release`** | release 流程 | D |
| **Post-audit pass** (用户视角主动 audit ≥1 轮, 续 v1.1+v1.3 Post-Audit Pass 模式) | v1.1+v1.3 method | E |
| **RETROSPECTIVE.md** 三段齐备 | 规则 C | F |

### 1.2 Out of scope (v1.4 不做, 留 v1.5+)

| Item | 理由 |
|---|---|
| Tier B 156 节修复 (Batch H 470 + Batch S 10 + Level2 600 atoms) | RETRO §二.6 工程量 > v1.4 体量 (~5-7 工作日 单独 KB pass cycle) — 留独立 release |
| 全 437 UNSOURCED_MANUAL 全量分类 (v1.4 只做启发式 fix + N=80 expansion) | 全量逐条 PDF 比对 工程量大 — 启发式 fix 在 v1.4 即可消除 main bias, 全量精确化留 v1.5 |
| Phase 7 RAG + KG 启动 | 与 prompt refactor 并行不经济, 留独立 phase |
| v2.0 SDTMIG release (假设 CDISC 发新版 PDF) | 假设性, 不在 v1.4 触发条件内 |

### 1.3 Tier 3 工作流强制产物

按 `~/.claude/templates/workflow-tier3.md` 标准:

- `.work/07_release_v1_4/PLAN.md` ← **本文件**
- `.work/07_release_v1_4/_progress.json` (Tier 2 schema)
- `.work/07_release_v1_4/evidence/checkpoints/` (Phase A-F 每 step 完成事件)
- `.work/07_release_v1_4/evidence/failures/` (Rule B 强制, 失败归档不删)
- `.work/07_release_v1_4/trace.jsonl` (phase_report 事件时间线)
- `.work/07_release_v1_4/subagent_prompts/` (所有派出 subagent 的 prompt 留底)
- `.work/07_release_v1_4/audit_matrix.md` (Rule A 抽检 × 各 Phase 网格)
- `.work/07_release_v1_4/backups/` (4 平台 prompt v8.1/v2.6/v2.2/v2 baseline 备份)
- `.work/07_release_v1_4/RETROSPECTIVE.md` (规则 C 强制, Phase F 产物)

---

## § 2. Phase 分解

### Phase A — 4 平台 prompt clean rewrite (估 1.5-2 工作日, 4 个并行 writer subagent + 4 reviewer)

**A0. 立项** ← 本 plan 用户 ack 后, 起 _progress.json + audit_matrix.md initial + 4 平台 backups/.

**A1. Gemini system_prompt v9 clean rewrite (RETRO §二.1 MAIN, 优先级 HIGH)**

- 输入: `ai_platforms/gemini_gems/current/system_prompt.md` (v8.1 LIVE, 525 行) + v1.3 RETRO §二.1 finding
- 设计目标:
  - ~200 行 (vs 525, -62%)
  - 5 essential rules (vs 17 CO-N):
    1. **KB-grounding 优先 default** (任何答案先 KB 双核, 找不到再 reasoning)
    2. **AHP-V1/V2/V3 锚** (anti-hallucination 三层, 保留 v8.1 R4 sanity 5/5 验证有效部分)
    3. **biospecimen / file-format / scope-shift 守门** (CO-4 + CO-2f + CO-1e 合并为 1 rule, regex-gated 触发)
    4. **响应格式** (cite source 段 + section refs)
    5. **前提纠错** (用户 wrong premise 时识破后 proceed, 不沿错)
  - **regex-gated CO-N**: 每 CO 只在 specific regex match 时 fire, 不污染 general path. 例: CO-1e IS scope shift 只在 "antibody|IgG|MMR|HIV" match 时触发; default path 走 KB-grounding.
  - **0 fossil annotation**: 移除 "v5 新增 / v7 新增 / v8 新增" 等迭代履历 marker. Clean rewrite, header 只标 v9 LIVE.
  - **KB-grounding 优先 default**: 移除 "依赖题文 reflection scaffold" 的旧逻辑, 任何 SDTM-shaped 变量名先 KB grep, 找不到再 reasoning.
- Writer: `oh-my-claudecode:executor` (sonnet/opus, background)
- 产物: `ai_platforms/gemini_gems/dev/v9_draft/system_prompt_v9.md` + `v9_design_rationale.md`
- **Rule A**: writer 自审 5 spot-check (每 essential rule 1 个)

**A2. ChatGPT system_prompt v3 clean rewrite (RETRO §二.2 + §二.4, 优先级 HIGH)**

- 输入: `ai_platforms/chatgpt_gpt/current/system_prompt.md` (v2.2 LIVE) + v1.3 RETRO §二.4 (method label drift)
- 设计目标:
  - 移除 v1/v2/v2.1/v2.2 迭代履历 annotation, clean rewrite
  - **Method label 显式锚**: PP §6.3.5.9.3 段加 "Method A=Many-Many / B=One-Many / C=Many-One / D=One-One" 显式 mapping (防止 internal prior 覆盖 KB)
  - KB-grounding 优先 default (同 Gemini A1)
- Writer: `oh-my-claudecode:executor` (background, 并行 A1)
- 产物: `ai_platforms/chatgpt_gpt/dev/v3_draft/system_prompt_v3.md` + `v3_design_rationale.md`
- **Rule A**: 5 spot-check (含 method label anchor 验证)

**A3. Claude Project instructions v3 clean rewrite (RETRO §二.2, 优先级 HIGH)**

- 输入: `ai_platforms/claude_projects/current/instructions.md` (v2.6 LIVE) + v1.3 RETRO §二.3 (pipeline gap)
- 设计目标:
  - 移除迭代履历 annotation, clean rewrite
  - KB-grounding 优先 default
  - **同步 pipeline fix** (A3.1 sub-step): `ai_platforms/claude_projects/dev/scripts/extract_examples_data.py` 加 capture `## §N.N.N` section headings, 让 PP RELREC Quick Reference 类 prose 被纳入 `07_examples_catalog.md` build OR include-list 显式加
- Writer: `oh-my-claudecode:executor` (background, 并行 A1/A2)
- 产物: `ai_platforms/claude_projects/dev/v3_draft/instructions_v3.md` + `v3_design_rationale.md` + (sub) `extract_examples_data.py` patch + smoke test
- **Rule A**: 5 spot-check (含 pipeline fix 验证 PP RELREC Quick Reference 段在 rebuild bundle 中可 grep)

**A4. NotebookLM instructions v3 clean rewrite (RETRO §二.2, 优先级 MED)**

- 输入: `ai_platforms/notebooklm/current/instructions.md` (v2 LIVE post-v1.3 citation refactor)
- 设计目标:
  - 移除迭代履历 annotation, clean rewrite
  - **保留 v1.3 footer Sources citation style** (不重新引 inline `[bucket.md]`)
  - KB-grounding 优先 default
- Writer: `oh-my-claudecode:executor` (background, 并行 A1-A3)
- 产物: `ai_platforms/notebooklm/dev/v3_draft/instructions_v3.md` + `v3_design_rationale.md`
- **Rule A**: 5 spot-check (含 footer citation style preservation 验证)

**A5. Rule D reviewer pass (4 平台, writer ≠ reviewer 严格隔离)**

- 4 个独立 reviewer subagent, 不同 `subagent_type` (规则 D):
  - Gemini v9: `pr-review-toolkit:code-reviewer` (Rule D slot #22)
  - ChatGPT v3: `oh-my-claudecode:scientist` (Rule D slot #23)
  - Claude v3: `oh-my-claudecode:critic` (Rule D slot #24)
  - NotebookLM v3: `oh-my-claudecode:verifier` (Rule D slot #25)
- 每 reviewer 独立做 prompt-level audit (essential rules 完整性 / 0 fossil verify / KB-grounding default verify / regex-gated CO-N 触发条件 verify) + Rule A independent N=5 grep-check.
- Verdict: PASS / PASS_WITH_OBSERVATIONS / NEEDS_REVISION.
- **Phase A → B gate**: 4 平台至少 PASS_WITH_OBSERVATIONS (0 NEEDS_REVISION).

### Phase B — Sanity validation (估 0.5-1 工作日, 含 R4 Pro quota 跨 cycle 等)

**B0. Phase A close + Phase B kickoff** (写 _progress.json A→B 切换, 用户 ack v9 prompts LIVE-ready).

**B1. Light sanity 4 题 × 4 平台 = 16 cells** (复用 v1.3 Phase C 设计)

- 4 题 (sanity, A1/A2/A3/B5 v1.3 KB 改动覆盖):
  - Q-S1: BECAT EXTRACTION sponsor-extensible (验 v1.3 A2 改动跨 v9 prompts 仍 reach)
  - Q-S2: PP RELREC Method A/B/C/D label (v1.3 Q-S2 ChatGPT/Gemini fail 在 v9 prompts 应 PASS)
  - Q-S3: TR shall/must (v1.3 Batch M Tier B 修复 #4)
  - Q-S4: NotebookLM bucket 25 DI domain (验 bucket rename + citation footer style)
- 4 平台 deployed-post-upload 跑 Chrome MCP fire-and-forget (复用 v1.3 r3 scripts)
- Verdict: 16/16 PASS (理想) / 14-15/16 PASS (acceptable, log v1.5 carry) / <14/16 (NEEDS_REVISION 回 Phase A)
- 工程量: ~30 min (script 已就绪)
- **Rule A**: 16 grep-probe (post-platform-response 验证 v9 prompts 不 regression KB-grounding)

**B2. R4 17-question full regression on Gemini v9 (v1.3 D1 deferred)**

- 17 题 × 1 Gemini Pro = 17 cells
- Pro quota constraint: 4 题/window × 5h reset, 跨 4-5 cycle = 16-20h 墙钟
- 决策选项 (Phase B 启动时拍板, 默认 B2-α):
  - **B2-α (默认, 跨日跑)**: 3-4 cycles × 4 题 = 12-16 题, 余 1-2 题切 Flash-Lite tradeoff (v1.3 R4 sanity 实测 model mix 可行)
  - **B2-β (defer v1.5)**: 暂跳, v1.4 cut 不阻塞, R4 留 v1.5 prep
  - **B2-γ (并行 B1)**: 用 multiple Gem 账号并行 (用户没多账号 → 不可行)
- Verdict: 17/17 PASS (ideal) / 15-16/17 PASS (acceptable) / <15/17 (回 Phase A)
- **Rule A**: 17 cells × 1 grep-probe = 17 probes

**B3. Phase B → C gate**: B1 ≥14/16 PASS + B2 ≥15/17 PASS (OR B2-β defer).

### Phase C — Minor carries (估 1-1.5 工作日, 并行小修)

**C1. section_coverage.jsonl 完整 pipeline rerun (RETRO §二.8 #8)**

- 输入: v1.3 A5 baseline stale (md_atoms 增量未应用 p4a forward matcher → p4b aggregate)
- 步骤: 
  1. md_atoms 增量 detect (v1.3 KB 改动 11 文件)
  2. `branches/06_deep_verification/scripts/p4a_forward_match.py` 增量跑
  3. `branches/06_deep_verification/scripts/p4b_section_aggregate.py` rerun
  4. 生成新 `section_coverage.jsonl` + diff vs v1.3 baseline
- Writer: main session OR background executor
- 工程量: < 1 天 (脚本就绪, 增量 rerun 时间多在 p4a)
- **Rule A**: 5 probe (新 vs 旧 section 数 + status flag 自洽)

**C2. UNSOURCED 启发式分类器 bias 修 + N=80 expansion (RETRO §二.5 #5 partial)**

- 输入: v1.3 A4 N=40 sample (Rule D #19 scientist 找到 5/10 cat disagree DERIVED_FROM_XLSX→REASONABLE_INFERENCE bias)
- 改进:
  - 启发式分类器 fix: 先 grep `pdf_atoms.jsonl` 找 verbatim → 找到即 REASONABLE_INFERENCE; 找不到再 fallback xlsx 检查
  - N=80 expansion: 在 v1.3 N=40 基础上 +40 (HIGH stratum +20 + LOW stratum +20, seed=20260520 不同 partition)
- Writer: main session OR background executor
- 工程量: 0.5 工作日
- **Rule A**: 80 probes (HALLUCINATED expected 0; cat distribution vs v1.3 N=40 一致性)
- 全 437 全量分类 defer v1.5 (per § 1.2)

**C3. NotebookLM bucket 25 UX 教程 + screenshot (RETRO §二.7 #7)**

- 输入: v1.3 V1_3_DEPLOY_GUIDE.md 已提示删旧 source 但用户实操未删 (43 sources vs 应 42)
- 改进: 写 `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md`:
  - 显眼提示 (top-of-doc warning + 红色标识)
  - 加 screenshot 教程 (Chrome MCP 截图 NotebookLM source list UI + 删除 button 操作)
- Writer: main session
- 工程量: 0.5 工作日 (screenshot 需用户协作 OR Chrome MCP 自动)

**C4. ChatGPT method label drift fix (RETRO §二.4 #4)**

- 输入: v1.3 RETRO §二.4 finding (ChatGPT Q-S2 答 Method A=Many-to-One PCGRPID+PPSEQ = KB Method C, label drift)
- 改进: `knowledge_base/domains/PP/examples.md` §6.3.5.9.3 段加显式锚 "Method A=Many-Many / B=One-Many / C=Many-One / D=One-One" + ChatGPT prompt A2 改动 (Phase A 已 cover label anchor in prompt) cross-check.
- 注意: 这个 #4 一部分在 Phase A.A2 ChatGPT prompt clean rewrite 时 cover (prompt level anchor), 另一部分在 C4 KB level anchor (KB level mapping table).
- Writer: main session
- 工程量: 1 hour (1 段 KB edit)
- **Rule A**: 4 probe (KB grep + 4 平台 uploads grep 跨平台一致)

**C5. Phase C → D gate**: 4 carries (C1+C2+C3+C4) 全 PASS / PASS_WITH_OBSERVATIONS.

### Phase D — KNOWN_LIMITATIONS reconcile + Release cut (估 0.5 工作日)

**D1. KNOWN_LIMITATIONS 三语 §0 reconcile**

- 移除 v1.3 §0 已解决项:
  - "Gemini system_prompt 525 行 prompt bloat" → resolved (v9 ~200 行)
  - "4 平台 prompt fossil layer" → resolved (4 平台 clean rewrite)
  - "Claude bundle 缺 PP RELREC Quick Reference" → resolved (pipeline fix)
  - "ChatGPT method label drift" → resolved (Phase A + C4 双层 anchor)
- 加 v1.4 解决项 + v1.4 deferred 项:
  - section_coverage.jsonl 重跑 (resolved)
  - UNSOURCED 启发式 bias 修 + N=80 (resolved partial, 全 437 defer v1.5)
  - NotebookLM bucket 25 UX 教程 (resolved)
- 加 v1.5 deferred 项:
  - Tier B 156 节 (Batch H + S + Level2)
  - 全 437 UNSOURCED 全量分类
- §1-§6 durable disclaimer inherit v1.3 byte-identical

**D2. Cut release/v1.4/**

- `cp -r release/v1.3 release/v1.4` (base 28 文件 inherit)
- Surgical edit:
  - `BUILD_MANIFEST.json` v1.4 metadata (release_tag v1.4 + previous v1.3 + 4 prompts 改 + KB C4 改 + 其他 byte-identical)
  - `self_deploy/{gemini,chatgpt,claude,notebooklm}/system_prompt.md` (OR `instructions.md`) 替换为 v9/v3/v3/v3 LIVE
  - `CHANGELOG.{en,zh,ja}.md` 三语 v1.4 entry (driver + scope + verdict + carries)
  - `CHANGELOG.md` (web changelog) 加 v1.4 entry
  - `KNOWN_LIMITATIONS.{en,zh,ja}.md` D1 reconcile
- 4 平台 uploads + tutorials 大部分 byte-identical 继承 v1.3 (C4 KB 改触发 chatgpt/gemini bundle rebuild; C1/C2 不触发 bundle rebuild)
- 触发 partial bundle rebuild: chatgpt 06 examples + gemini 03 examples (PP §6.3.5.9.3 label anchor 改)

**D3. Rule D verifier audit (`oh-my-claudecode:verifier` Rule D slot #26)**

- 8 audit sections (类似 v1.3 D3):
  - 4 平台 prompt v9/v3 行数 + essential rules count 验证
  - 4 平台 uploads 与 v1.3 delta verify (C4 影响范围 chatgpt+gemini 局部 rebuild)
  - KNOWN_LIMITATIONS 三语 §0 reconcile completeness
  - CHANGELOG v1.4 entry 三语一致性
  - Tag 准备 (annotated message 草稿)
  - Rule A cumulative ≥97 verify
  - v1.3 immutability verify (release/v1.3/ + tag 0 post-cut 改动)
  - Phase F RETROSPECTIVE.md 三段框架准备
- Verdict: APPROVE / PASS_WITH_OBSERVATIONS / NEEDS_REVISION

**D4. Tag `v1.4-company-release`** (annotated, post user ack).

### Phase E — Post-audit pass (估 1-2 hour)

**E1. 用户视角主动 audit** (反 v1.1/v1.3 Post-Audit Pass 模式)

- 模拟用户跑 4 平台部署后第一个问题, 看 v9/v3 prompts 是否 KB-grounding default 生效
- Rule A 累计 grep target ≥97 (v1.4 累计应 100+)
- 4 平台 system_prompt 数字引用 0 不一致
- v1.4 KB 改 (C4 label anchor) 在 deployed bundles 反映 (chatgpt 06 + gemini 03 byte-exact delta verify)
- v1.3 immutability (release/v1.3/ + tag 0 post-cut 改动)
- Tier 3 工作流强制产物全产

**E2. 0 gap verdict** → 进 Phase F

### Phase F — RETROSPECTIVE + Sync + Commit (估 0.5 工作日)

**F1. RETROSPECTIVE.md 三段齐备** (规则 C 强制, Tier 3 项目)

- §一: 保留下来的做法 (4 platform parallel writer + 严格 Rule D 隔离 + clean rewrite 风格)
- §二: 必须补上的缺口 (v1.5 carries 8 项 e.g. Tier B + 全 437 UNSOURCED + Phase 7 启动)
- §三: 关键决策复盘 (clean rewrite vs incremental patch / 4 平台并行 vs 串行 / R4 跨 cycle 跑 vs defer)
- §四: Post-Audit Pass 结果 (E1 自查表)
- 附: v1.4 终态数字

**F2. 同步状态文件 (Chain B)**

- `.work/07_release_v1_4/_progress.json` → final status = "closed"
- `.work/meta/worklog/phase_07_release.md` → append v1.4 entry
- `docs/PROGRESS.md` → milestone + 状态总览更新
- `CLAUDE.md` Key Paths → 加 `Phase 6.5 Release v1.4` 一行

**F3. Commit + push + tag push**

- 单 commit "07 Release v1.4 — 4-platform prompt full-stack refactor + 7 minor carries"
- push origin main
- tag push `v1.4-company-release`

---

## § 3. Rule A/B/C/D 强制条款

### Rule A (语义抽检, 压缩率 / 改写率 > 50% 必走)

- v1.4 main carry Gemini v9 vs v8.1 改写率 ~62% (525 → 200 行) **必触**
- ChatGPT v3 vs v2.2 改写率 估 50%+ **必触**
- Claude v3 vs v2.6 改写率 估 50%+ **必触**
- NotebookLM v3 vs v2 改写率 估 40-50% (可能边界, 走 N=5 spot-check 即可)
- 目标累计 ≥97 grep probe (vs v1.3 实际 153+, target 与 v1.3 保持)
- 每 Phase 每 step 完成时 `audit_matrix.md` append 一行 + `_progress.json.rules.A.applied[]` 同步

### Rule B (失败归档不删)

- 任何 writer / reviewer / build / sanity 失败 attempt 归档到 `evidence/failures/<step>_attempt_<N>.md`
- 含输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入

### Rule C (Tier 3 必 RETROSPECTIVE)

- Phase F.F1 强制产 `RETROSPECTIVE.md` 三段齐备 + §四 Post-Audit Pass

### Rule D (审阅隔离, 不同 subagent_type)

- v1.4 预计 6+ slot (#22-#27+):
  - #22-#25: Phase A 4 平台 reviewer pass (4 个不同 subagent_type: code-reviewer / scientist / critic / verifier)
  - #26: Phase D verifier audit (`oh-my-claudecode:verifier`)
  - #27+: 备用 (e.g. Phase E post-audit additional / contingency)
- writer subagent_type 严格 ≠ reviewer subagent_type
- 同一 session 不允许 self-review

---

## § 4. 风险 + 缓解

| 风险 | 影响 | 缓解 |
|---|---|---|
| Gemini v9 clean rewrite 漏掉 v8.1 R4 sanity 5/5 验证有效的 anti-hallucination 机制 | regress R4 baseline | A1 design rationale 显式列 v8.1 → v9 保留 / 合并 / 删除 决策表; A5 reviewer 验保留 |
| 4 平台 prompt 并行 writer 之间风格 drift (4 个 executor 各做各的) | release inconsistency | A0 起 unified style guide (header format / KB-grounding default phrasing / regex-gated CO-N 命名) 写进 4 个 writer prompt 公共部分 |
| R4 Pro quota 跨 cycle 等待跑出 Tier 3 工期 (估 16-20h) | v1.4 延期 | B2 默认 α + Flash-Lite mix; 拍板 β defer v1.5 也接受 (B2-α/β 用户 Phase B 启动时拍板) |
| Tier B 156 节 defer v1.5 用户不接受, 要 v1.4 全 cover | scope creep, 工期翻倍 | § 1.2 显式 out-of-scope + RETRO §二 引证 (工程量 ~5-7 工作日 单独 KB pass) |
| Claude pipeline fix (A3 sub) 引入 regression (`extract_examples_data.py` 改动 capture rule 影响其他文件) | Claude bundle build break | A3 sub-step 加 smoke test (10 文件 grep cross-check + bundle size delta < 5% verify) |
| C4 KB label anchor 改 PP/examples.md 引入 atom-level regression (改 KB → md_atoms 改 → section_coverage 改) | section_coverage 重跑 churn | C4 与 C1 配合: C4 改 KB → C1 重跑 pipeline 时一并 reflect |

---

## § 5. Phase 启动门 (gate before Phase X kickoff)

- **A 启动前**: 本 PLAN 用户 ack + .work/07_release_v1_4/ workspace 全套建好
- **B 启动前**: A5 4 平台 reviewer 全 ≥ PASS_WITH_OBSERVATIONS + user ack v9/v3 prompts LIVE-ready
- **C 启动前**: B1 ≥14/16 + (B2 ≥15/17 OR B2-β defer)
- **D 启动前**: C1+C2+C3+C4 全 PASS / PASS_WITH_OBSERVATIONS
- **E 启动前**: D4 tag cut
- **F 启动前**: E2 0 gap

---

## § 6. 工期估算

| Phase | 估 | 累计 |
|---|---|---|
| A 4 平台 prompt clean rewrite + reviewer | 1.5-2 d | 1.5-2 d |
| B Sanity + R4 (含 quota 等) | 0.5-1 d (B1) + 0-1 d (B2 跨日, 可 background) | 2-4 d |
| C Minor carries (并行) | 1-1.5 d | 3-5.5 d |
| D KNOWN_LIMITATIONS + Release cut | 0.5 d | 3.5-6 d |
| E Post-audit | 1-2 h | 3.5-6 d |
| F RETROSPECTIVE + commit | 0.5 d | **3-5 工作日** (主估) |

**单 session 内完成可能**: 复用 v1.3 单日 Tier 3 模型 — 派 4-6 background subagent 并行, main session 协调. R4 跨 cycle 部分用 ScheduleWakeup 或 defer β.

---

## § 7. 用户决策点 (kickoff)

1. **Scope ack**: § 1.1 in-scope 14 items + § 1.2 out-of-scope (Tier B 156 节 + 全 437 UNSOURCED 全量) defer v1.5 — accept?
2. **B2 决策预拍板** (可 Phase B 再拍): α 跨日跑 R4 / β defer v1.5 — 倾向?
3. **A3.1 Claude pipeline fix 范围**: extract_examples_data.py capture `## §N.N.N` heading (general fix, 影响所有 domain examples.md) / OR Quick Reference include-list 显式加 (point fix, 仅 PP §6.3.5.9.3) — 倾向?
4. **Workspace 启动**: 是否本 session 直接进 Phase A (开 4 平台 writer subagents 并行) / 还是单独 ack 后再启?
