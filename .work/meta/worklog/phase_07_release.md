# Phase 07 Release Worklog

> 入口: 跨 v1.0 + v1.1 (公司发布版) 工作日志.
> v1.0 历史细节在 `.work/07_release/{PLAN,RETROSPECTIVE}.md` (主体在那).
> v1.1 入口在 `.work/07_release_v1_1/PLAN.md`.
> Chain B: 本文件 → 各平台 `_progress.json` → `docs/PROGRESS.md`.

## 2026-04-27 — Release v1.0 (公司发布版) sign-off

详见 `.work/07_release/RETROSPECTIVE.md`. 24 文件三语 release 包, tag `v1.0-company-release`.

## 2026-05-15 — Release v1.1 cut (06 deep verification 修复回灌)

**触发**: 06 P7 COMPLETE 2026-05-12, 工程全部收官. knowledge_base/ 43 文件 +1,405 / -234 行净更新 (DI 新加, PC §6.3.5.9 RELREC 等) 未回灌到 ai_platforms 部署包和 release 自部署包.

**决策**: 走 v1.1 路线 (用户 ack 2026-05-15) — cut 新 tag, 而非 in-place 更新 v1.0 (tag 不可变).

**4 平台 rebuild**:
- chatgpt: merge_for_chatgpt.py --stage all, 9 文件 (4 changed: 02/03/05/06)
- gemini: merge_for_gemini.py --stage c_refactor, 3 KB 派生文件全 rebuild (01/02/03; 04 writer-authored 不动)
- notebooklm: merge_sources.py, 42 buckets (11 changed + bucket 25 加 DI)
- claude_projects: v1 + v2 双 builder 系统, executor subagent 后台跑 (路径 stale 需修复)

**Build 脚本改动**:
- chatgpt merge_for_chatgpt.py: 05 expected_segments 63→64 + token_cap 69K→85K (DI 加入)
- notebooklm bucket_config.json: bucket 25 (td_meta_ti_ts_oi) 加 domains/DI/assumptions.md

**Rule D 独立 reviewer**: TBD (pending claude rebuild 完成后统一 review)

**收尾**:
- evidence: `.work/07_release_v1_1/evidence/{diff_summary.md, rule_d_review.md, *_rebuild.log}`
- release 包: `release/v1.1/{CHANGELOG.{en,zh,ja}.md, BUILD_MANIFEST.json, self_deploy/{4 平台}/}`
- retrospective: `.work/07_release_v1_1/RETROSPECTIVE.md` (三段: 保留/缺口/决策)
- tag: `v1.1-company-release` 推送后

### 2026-05-15 PM — v1.1 cut COMPLETE (sign-off pending commit)

**Executor outcome** (sonnet, ~6.3 分钟, 51 tool uses):
- 7 文件 rebuilt (`02_chapters.md` +12.5KB, `03_model.md` +1.5KB, `06_assumptions.md` +24.2KB 含 DI, `07_examples_catalog.md` -4B, `09_examples_data_high.md` -15KB pre-existing cap, `10_examples_data_others.md` +202B)
- 1 文件 idempotent (`05_mega_spec.md` 0 byte; DI 无 spec.md, 63 域不变)
- 12 文件 unchanged (terminology + routing + index)
- Failures F1-F4 archived to `failures/claude_rebuild_failures.md` (Rule B 合规: stale REPO_ROOT path bug 工作绕过)

**Rule D verifier** (oh-my-claudecode:verifier opus, ~4.5 分钟, 46 tool uses): **ALL_PASS**
- Evidence 完整性 PASS
- Rule A 5/5 抽检 (PC §6.3.5.9 RELREC, DI assumption, TA assumption, ch02, ch08) × 4 平台 = 20 grep hits zero miss
- Build script 改动正确性 PASS (chatgpt 05 + notebooklm bucket 25, 最小必要)
- Release v1.1 包结构 PASS (4 平台 + 元文档 byte-identical 继承 v1.0 + 三语 CHANGELOG 一致 + BUILD_MANIFEST 完整)
- 红线 PASS (KB 0 反向污染 + baseline 25MB 完整 + failures Rule B 合规)
- 跨平台 delta oracle 自洽: chatgpt 05 ≡ gemini 02 = +74,178 bytes
- 5 项 LOW/MEDIUM 改善观察 (O1-O5) 已在 RETROSPECTIVE §二 主动记录

**Release artifact**: `release/v1.1/{CHANGELOG.{en,zh,ja}.md, BUILD_MANIFEST.json, self_deploy/{chatgpt(9.3M),claude(4.6M),gemini(2.2M),notebooklm(9.5M)}/}` = 26MB.

**Build script 改动** (Chain B 同步):
- `ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py` — 05 entry expected_segments 63→64 + token_cap 69_000→85_000
- `ai_platforms/notebooklm/dev/scripts/bucket_config.json` — bucket 25 加 `domains/DI/assumptions.md` + description 加 DI 注

**Tag 候选**: `v1.1-company-release` (待用户 ack push 后创建).

### 2026-05-19 — Chrome MCP dry-run + R3 SMOKE_V4 并行执行 scaffold

**触发**: 用户接管 Chrome (`--remote-debugging-port=9222` + 旁路 `~/ChromeDev` profile, 因 Chrome 136+ 静默忽略默认 profile 的 debug 端口) 探"Chrome MCP 全自动并行 4 平台 R3 retest" 可行性. 与 `.work/07_release_v1_1/r3/r3_kickoff.md` (4 月预设的串行 cowork) 互补, 不替换.

**Dry-run (无 AI 答题, 仅 a11y snapshot + screenshot + selector probe)**:
- 4 平台接管 OK (chrome-devtools-mcp 自动挂 9222, 无需配 `--browser-url`)
- 关键发现:
  - NotebookLM `textarea[aria-label="Query box"]` 与顶部 notebook 标题改名框完全可区分 (a11y 严格匹配 — 用户预先警告的"搜索框"陷阱避开)
  - Grammarly 扩展可见按钮 disable 后 DOM 残留 `grammarly-desktop-integration` 是空壳 (bbox 0×0, 不监听输入框)
- Evidence 4 份 + 4 screenshot: `ai_platforms/{platform}/dev/dry_run_2026-05-19/{feasibility.md, NN_<platform>.png}`

**Round 1 校准 (4 平台并行触发 "什么是 SDTM?", 验 done 信号 + 时序)**:
- 4 平台 fire-and-forget script 同时跑, 总墙钟 ~107s (派 12s + 等 90s + 收 5s)
- Done 信号锁定:
  - Gemini: send 按钮**消失** during gen → 重新出现 + `!disabled` 即 done (~41s, 含 Pro mode 切换)
  - ChatGPT: `[data-testid="stop-button"]` 消失 (~21s, 最快)
  - NotebookLM: `button[aria-label="Submit"]` 重出现 + `disabled=true` (~41s, 含 ~30s RAG 检索)
  - Claude: `Send message` 按钮重出现 (stop-response 消失) (~48s, 最慢)
- Pro mode 实测 label: `"Pro Advanced math and code with 3.1 Pro"` (3.1 Pro 模型)

**Round 2 校准 (响应抽取 selector 细化 + NotebookLM 删 chat history 路径)**:
- NotebookLM 响应: `mat-card-content.message-content .message-text-content` (Angular Material), 简化 `.message-text-content`
- Claude 响应: `div.standard-markdown` (Claude markdown 渲染专用 class)
- NotebookLM "Chat options" menu 实测含 menuitem `"Delete chat history Chat history is private to you."` ✓ (confirm dialog 结构待 R3 第 1 题校准)

**R3 scaffold 落档** (`.work/07_release_v1_1/r3/`):
- `r3_orchestration_parallel.md` — Phase A-D 流程 + selector 引用表 + Rule D reviewer 规则 + Rule B failure 归档
- `scripts/{gemini,chatgpt,notebooklm,claude}_runner.js` — fire-and-forget runner, `__QUESTION_PLACEHOLDER__` 待 sed 替换
- `scripts/reset_{gemini,notebooklm}.js` — await-able 重置 (Gemini 新 chat + Pro mode; NotebookLM 删 chat history + confirm dialog 兜底)
- `scripts/reviewer_prompt_template.md` — Rule D 隔离 reviewer subagent prompt (推荐 `oh-my-claudecode:scientist`)
- 原 `r3_kickoff.md` 串行流程加 4 行注脚指向并行方法 (保留作 fallback)

**预估**: R3 实跑 17 题总墙钟 ~20 min (vs 串行 ~50 min, 2.5× 提速)

**遗留 (R3 实跑第 1 题校准)**:
1. NotebookLM "Delete chat history" confirm dialog 结构 (`reset_notebooklm.js` best-effort 兜底, 不命中则主 session 介入)
2. Claude multi-segment `.standard-markdown` (简单题单段; SMOKE_V4 含 mapping 表 / artifact 题需扩到外层包裹容器)
3. 4 平台 dry-run 测试 conversation 留有 1 道 "什么是 SDTM?" Q&A (Gemini/ChatGPT/Claude 新 chat / NotebookLM 共用 chat), R3 跑前 reset 流程自动清

### 2026-05-19 PM — SMOKE_V4 R3 实跑 + 4-prong Gemini v8.1 prompt draft (v1.2 prep)

**R3 实跑 (commit `080eb88`)**: 4 平台 × 17 题 = 68 cells, Chrome MCP 并行 fire-and-forget ~50 min 主跑 (墙钟超估算 20 min, 因 Claude project URL navigate 不稳定 + done-signal 高密度题误判, AHP3 manual fallback ~3 min):

| 平台 | R3 总分 | PASS+ | vs R1 | Gate |
|---|:--:|:--:|:--:|:--:|
| Claude v2.6 | 17/17 | 11 | = (11 题升级 PASS+) | ✅ |
| ChatGPT v2.2 | 17/17 | 13 | ↑ +0.5 | ✅ |
| NotebookLM v2 | 15.5/17 | 11 | = (1 PARTIAL + 1 PUNT 架构限制) | ✅ |
| Gemini v7.1 | 13/17 | 5 | ↓ -3 ⚠️ | ⚠️ regression |

Gemini 4 FAIL: Q3 BE/BS/RELSPEC 跑题答 AE (1541 chars off-topic) / Q4-A 麻疹 IgG 退回 LB (R2 修过的退回) / Q11 Dataset-JSON 跑题答 AE/CM / AHP1 LBCLINSIG 跑题答 CM/MH. AHP probe **4/5 caught** (Q10/Q13/AHP2/AHP3 ✓, AHP1 ✗) — v7.1 anti-hallucination 锚仅在题文含 reflection scaffold ("如果你听说过 X") 时触发, plain factual + 邻域关键词时 fallback 兜底.

R3 reviewer: `oh-my-claudecode:scientist` (Rule D #15 unique slot, background) 68/68 cells concordance, 给出 4 v8 prompt 改进 finding (HIGH/HIGH/HIGH/MEDIUM). Evidence: `.work/07_release_v1_1/r3/{r3_matrix,R3_RETROSPECTIVE}.md` + `evidence/q01-q14_combined.md` + `ahp1-3_combined.md` + `_reviews/r3_review.md` (190 lines).

**Gemini v8.1 prompt draft (本次 commit)**: 主 session 起 `ai_platforms/gemini_gems/dev/v8_draft/` workspace, 实现 R3 reviewer §5 4-finding 一对一 4-prong fix + 后续 v8 reviewer reconcile 6 项:

| Prong | 位置 | 修复 R3 FAIL |
|---|---|---|
| **CO-4 入口守门** (NEW v8) | system_prompt L217-228 | Q3 BE/BS/RELSPEC: biospecimen 关键词 (中英 13 项) → BE/BS/RELSPEC, 禁 AE/CM fallback |
| **CO-2f 文件格式 ground rule** (NEW v8) | system_prompt L182-206 | Q11 Dataset-JSON: XPT/Dataset-JSON/Define-XML → ground CDISC 格式 spec, 禁替换 SDTM domain + 跑题守门 |
| **CO-1e IS scope shift** (NEW v8) | system_prompt L119-160 | Q4-A 麻疹 IgG: v3.4 IS Assumption 2 anti-microbial antibody → IS 不论 timing; HIV Ag/Ab combo → MB (Assumption 5 exemption); ISTSTOPO Assumption 8; sticky anchor 防 R2 fix decay |
| **CO-5 default reflection** (MOD v8) | system_prompt L295-364 + L499-508 + L301-303 三处协同改 | AHP1 LBCLINSIG: regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 触发 KB 双核, 不依赖题文 reflection scaffold |

**v8 → v8.1 reviewer reconcile**: `pr-review-toolkit:code-reviewer` (Rule D #16 unique slot, background) verdict **PASS_WITH_OBSERVATIONS**, 6 项全 apply (2 HIGH + 2 MEDIUM + 2 LOW):
- **H1 (factual)**: HIV Ag/Ab combo → MB (不是 LB), per KB IS Assumption 5 (v8 初稿误写 LB, 已修)
- **H2 (architecture)**: CO-2f 优先级 gate, 文件格式题不走 AHP-V1 regex 路径 (防 "Dataset-JSON" 题误判变量幻觉)
- **M1 (regex)**: 否定清单 (FDA/USA/NCI/EVS/CDISC/ADaM/SDTM/XPT/XML/JSON/SAS/EDC/CRF/RWD/ADAE/ADSL/ADTTE + 域缩写 AE/CM/DM/LB/IS/MB/BE/BS) 跳过双核
- **M2 (verbose)**: 候选 ≥ 5 时只扫题文显式提及 3-5 个
- **L1 (numbering)**: ISTSTOPO Assumption 7a → 8 (per KB, 3 处)
- **L2 (CT note)**: BECAT EXTRACTION 注 "sponsor-extensible, 非 CT 锁定" (KB BE/spec L111 只 inline COLLECTION/PREPARATION/TRANSPORT)

**Artifacts (本次 commit 范围)**:
- `ai_platforms/gemini_gems/dev/v8_draft/system_prompt_v8.md` (525 lines, v7.1 423 + 102 = +24%)
- `ai_platforms/gemini_gems/dev/v8_draft/v8_design_rationale.md` (R3 4 FAIL → 4 prong mapping + reviewer §5 alignment + 改动量估算 + 预期 dry-run outcome + 附录 v8→v8.1 reconcile 表)
- `ai_platforms/gemini_gems/dev/v8_draft/dry_run_plan.md` (Phase A-D + 4 题 verdict 标准 + 风险 contingency 5 条)
- `ai_platforms/gemini_gems/dev/v8_draft/evidence/v8_reviewer_audit.md` (149 lines, Rule D #16 audit)
- `ai_platforms/gemini_gems/dev/evidence/_progress.json` (r3_test COMPLETE + v8_draft WRITER_RECONCILED_DRY_RUN_PENDING_USER_ACK 两 top-level 条目)
- `ai_platforms/SYNC_BOARD.md` (允许的下一动作段更新, 反映 v8.1 draft 待 dry-run)

**遗留 (下一动作 = 用户部署 + dry-run)**:
1. 用户部署 v8.1 system_prompt 到 Gemini Gem instructions field (UI 操作只能用户做)
2. 部署后主 session dispatch Chrome MCP 跑 4 fail 题 (Q3 / Q4-A / Q11 / AHP1) ~10 min
3. evidence 落到 `dev/v8_draft/dry_run_2026-05-XX/q<NN>_combined.md`
4. 派 Rule D #17 unique reviewer cross-check 4 题 verdict
5. 若 4/4 PASS → v8.1 promote → `current/system_prompt.md` + cut v1.2 release tag
6. v1.2 cut 不在本次 commit scope (待 dry-run PASS 后单独议题)

### 2026-05-19 16:35-16:50 PM — Gemini v8.1 dry-run 4 题 ALL_PASS + Rule D #17 audit APPROVE

**Pro quota 等待 (~57 min)**: 用户上午 R3 17 题 × 4 平台跑爆 Gemini Pro 配额 (今天重置 16:34 PM). 主 session ScheduleWakeup 3540s + 用户 16:35 主动 "继续". Pro 16:35 重置即用.

**Dry-run 实跑 (Chrome MCP, Gemini 3.1 Pro, 同 R3 baseline model)**: 串行 4 R3 FAIL 题, 每题 navigate `/gem/<id>` 重 fresh chat ("New chat" anchor 跳 /app 脱 Gem context, 不能用). 实跑 5.5 min vs 估 10 min.

| 题 | R3 v7.1 | v8.1 dry-run | Prong + Fix 验证 |
|---|:---:|:---:|---|
| Q3 BE/BS/RELSPEC | FAIL 跑题→AE (1541c) | **PASS+** (1439c, 47.6s) | Prong 1 + L2 (BECAT sponsor-ext 注 + "禁臆造 BM") |
| Q4 LB/MB/IS | FAIL A=LB (R2 修过的退回) | **PASS+** (1763c, 52.7s) | Prong 3 + H1 (HIV→MB Assumption 5) + L1 (Assumption 8) |
| Q11 Dataset-JSON | FAIL 跑题→AE/CM (1436c) | **PASS+** (3768c, 30.6s) | Prong 2 + H2 (CO-2f 优先 gate) |
| AHP1 LBCLINSIG | FAIL 跑题→CM/MH (1485c) | **PASS+** (694c, 46.6s) | Prong 4 + M1 (regex 否定清单) — 7/7 AHP-V1 模板元素 fire |

**Rule D #17 reviewer audit** (`oh-my-claudecode:verifier`, background): **PASS_WITH_OBSERVATIONS — APPROVE** 0 blocker.

reviewer KB grep 独立确认 4/4 PASS: BE/spec L111 BECAT examples + BS/spec L84 BSTESTCD VOLUME/RIN C124300 + IS/assumptions §2/§5/§8 exact + LBCLINSIG absent KB + LBCLSIG L410 C66742 + LBNRIND C78736. 10 项 Prong/Fix 9 强 evidence, 1 弱 (M2 候选数限 — Q4 候选 < 5 没真触发 threshold).

reviewer findings (4 项 LOW/MEDIUM, 0 HIGH):
- **PASS+ 标签 vs SMOKE_V4 §1.2 "AHP 专属"**: §1.2 L170 明文 "PASS+ (AHP 专属)", 严格 Q3/Q4/Q11 应只 PASS, 只 AHP1 计 PASS+. 主 session 加 caveat (informal bonus marker 与 R3 r3_matrix 历史惯例一致, 正式 score 4/4 PASS, AHP1 PASS+). Risk LOW. 已 apply.
- **BECAT EXTRACTION KB-prompt 分叉 LOW**: v8.1 prompt L272 添 EXTRACTION 不在 KB BE/spec L111 (只 inline 3 Examples), response 用 "sponsor-extensible" 注释 conservatively 承认. 建议 v1.2 post-cut 加来源注释. Risk LOW.
- **M2 fix 隐式 LOW**: Q4 候选 < 5, threshold 没真触发. 建议 R4 用 Q1 (GF 多变量) / Q14 (跨域多变量) 独立验证.
- **17 全题在 v8.1 未测 MEDIUM**: 13 道原 PASS 题 v8.1 行为未测, 建议 v1.2 post-cut 立即跑 R4 全量回归 (anti-cheating long-tail probe; 用户 cheating 顾虑 — 4 fail 修复必要不充分, 17 全题才充分).

**Artifacts (本次 commit 范围)**:
- `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-19/{q03,q04,q11,ahp1}_v8_evidence.md` (4 题 evidence, 含 verdict 矩阵 / R3 delta / response 片段)
- `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-19/dry_run_verdict.md` (主 session 4/4 PASS+ verdict, post-reviewer-#17 加 PASS+ caveat + reviewer findings 5/6/7 caveat)
- `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-19/v8_1_dry_run_audit.md` (Rule D #17 audit, reviewer reports 149 lines verdict + KB grep + 4 findings)
- `ai_platforms/gemini_gems/dev/evidence/_progress.json` 加 `v8_1_dry_run` top-level 条目 (status=ALL_PASS_PLUS_REVIEWER_DISPATCHED + reviewer_verdict + 4 findings + recommendation APPROVE)
- `ai_platforms/SYNC_BOARD.md` 允许下一动作段更新

**v8.1 仍在 dev/ 不 promote**: 此 commit 仅保护 dry-run + reviewer evidence. 用户决策 v8.1 promote `current/system_prompt.md` + cut v1.2 release tag 是单独议题 (reviewer 0 blocker, 等用户 ack).

**Pre-promote checklist (待用户 ack 后)**:
1. cp `dev/v8_draft/system_prompt_v8.md` → `current/system_prompt.md` (替换 v7.1 LIVE)
2. 用户 Gemini Gem 已部署 v8.1 (16:35 PM 之前完成), `current/` LIVE 与 deployed 即匹配
3. cut `release/v1.2/` + v1.2 release tag (单独 packaging cycle)
4. R4 17 题 full 回归测建议 v1.2 post-cut

### 2026-05-19 16:55 PM — Gemini v8.1 PROMOTED LIVE (用户 ack Plan A → C → B)

**用户决策**: 选 Plan A (promote 立刻) → Plan C (R4 17 全题回归) → Plan B (v1.2 release cut).

**Plan A 执行**:
1. `cp ai_platforms/gemini_gems/dev/v8_draft/system_prompt_v8.md → ai_platforms/gemini_gems/current/system_prompt.md` (Bash 内置 cp, 525 行 → 525 行 identical 验证)
2. Header L1 `v8.1 DRAFT post-R3 reviewer reconcile` → `v8.1 LIVE post-R3 promote 2026-05-19`; L3 cut signal 描述更新 "Promoted from dev/v8_draft/ after dry-run 4/4 PASS + Rule D #17 APPROVE 0 blocker. Replaces v7.1 LIVE"
3. 用户 16:30 PM 之前已 paste v8.1 内容到 Gemini Gem instructions field (UI 操作), `current/system_prompt.md` ↔ deployed Gem instructions 现完全一致
4. `_progress.json` v8_1_dry_run 加 `promoted_to_current` 子段记录 promote 时间 + 动作
5. `SYNC_BOARD.md` 允许下一动作 → Plan C (R4 17 全题) + Plan B (v1.2 cut)
6. `docs/PROGRESS.md` 加 16:55 PM PROMOTED LIVE milestone (★★★ — 替换 v7.1 LIVE 是 Phase 6.5 重大状态变更)

**v7.1 → v8.1 关键改动 (LIVE diff)**:
- +CO-1e (IS scope shift v3.3→v3.4): anti-microbial antibody → IS regardless of timing; HIV Ag/Ab combo → MB (Assumption 5 exemption); ISTSTOPO Assumption 8
- +CO-2f (文件格式 ground rule): XPT/Dataset-JSON/Define-XML → ground CDISC published spec, 禁替换 SDTM domain content + 跑题守门
- +CO-4 入口守门 (biospecimen 关键词 13 项中英 → BE/BS/RELSPEC, 禁 AE/CM fallback)
- CO-5 共同执行规则 #1 + 工作流程 Step 1 + AHP-V1 触发条件 (3 处协同) 改 default: SDTM-shaped identifier regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 触发 KB 双核 (不依赖题文 reflection scaffold), 加否定清单 (FDA/CDISC/XPT/JSON 等) + CO-2f 优先 gate + 候选数 ≥ 5 限制
- +CO-5 #7 跑题守门 (答完扫主体 domain vs 题文 domain 不一致即重答)
- v8.1 vs v7.1: 525 行 vs 423 行 (+102 行 +24%)

**Next plan (待执行)**:
- **Plan C (R4 17 全题回归测)**: Pro quota check — 今日已用 R3 17 + dry-run 4 = 21 题, 16:34 PM reset 后剩余可能不够 17 题. 若不够: ScheduleWakeup 明日 16:34 PM Pro reset 后跑. R4 测目的: anti-cheating long-tail probe — 验证 v8.1 改动没让 13 道 R3 PASS 题 regression (尤其 CO-5 regex default + 候选数限制是否影响多变量题 response).
- **Plan B (v1.2 release cut)**: 类比 release/v1.1/ packaging — 4 平台 KB rebuild (v8.1 only 改 Gemini prompt, 其他 3 平台不变 → 仅 Gemini bundle rebuild), CHANGELOG.{en,zh,ja}.md, KNOWN_LIMITATIONS reconcile (v1.1 §0 Tier B 已记 R3 Gemini regression), self_deploy/ 4 平台教程更新, release/v1.2/ 目录, tag `v1.2-company-release`. 工程 ~半天 sprint.
