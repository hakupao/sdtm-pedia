# SDTM 知识库 — Release v1.4 变更说明 (中文)

> Tag: `v1.4-company-release` (发布: 2026-05-22)
> 上一版: `v1.3-company-release` (2026-05-20)
> 触发: Prompt full-stack refactor — 4 平台 v3/v9 clean rewrite (化石层移除 + KB-grounding default) + 4 项 v1.3 minor carry (C1-C4) + Claude bundle pipeline architectural fix. Gemini MAINTAINED_NO_SANITY_TEST per user 2026-05-22 decision.

## 概要

v1.4 是 SDTM Pedia 的 **prompt-pass 级**版本 — 3 个仍在维护的 AI 平台 (ChatGPT GPTs, Claude Projects, NotebookLM) 完成 system prompt / instructions 的全栈 clean rewrite, 移除 v1.0-v1.3 迭代化石层, 把 KB-grounding 重新立为主路径. Gemini Gems 平台 v1.4 起转为"维护但不再 sanity 测试"模式 (用户 2026-05-22 决策). 4 项 v1.3 minor carry (C1-C4) 同步合并. Claude bundle pipeline 修复 §N.N.N capture gap (Phase 6.5 reorg-A path bug 回归).

## v1.4 (2026-05-22) — Prompt pass + Minor carries + Pipeline fix

**类型**: prompt-pass + minor carries (相对 v1.3 KB-pass; 主要工作集中在 prompt 层, KB 层仅 1 个文件改动)

### Prompt 改动 (4 个平台 system_prompt / instructions)

驱动: v1.3 RETRO §二 8-carry list — 主线 = 4 平台 prompt 全栈重构 (Gemini v8.1 525 行包含 17 条 CO-N 化石规则 + 其他 3 平台并行积累). v1.4 main carry 是去化石 + KB-grounding 优先.

- **ChatGPT v3 system_prompt** (`self_deploy/chatgpt/system_prompt.md`): 120→119 行 + Method label anchor mapping 4 行 (L77-80). 移除 v1.0-v1.3 迭代注释, KB-grounding 优先 default. A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
- **Claude v3 system_prompt** (`self_deploy/claude/system_prompt.md`): 125→133 行. 5 essential rules + regex-gated CO-N + Files A-S 19-file table 全保留 (critic reviewer 在 attempt 1 找到 truncated 19→7 file table → attempt 2 surgical fix PASS_WITH_OBSERVATIONS).
- **NotebookLM v3 instructions** (`self_deploy/notebooklm/instructions.md`): 157→156 行. footer Sources citation 语义等价保留 (非 byte-exact, 行为 preserved). 移除 v1.0-v1.3 迭代化石.
- **Gemini v9 system_prompt** (`self_deploy/gemini/system_prompt.md`): 525→292 行 (含 2026-05-22 增补的 Method label anchor). **MAINTAINED_NO_SANITY_TEST** — 优化继续, 测试停 (详 KNOWN_LIMITATIONS §0.A).

### 知识库改动 (1 个文件修改)

- **PP/examples.md** — §6.3.5.9.3 加 13 行显式 Method label mapping table (A/B/C/D × IDVAR1+IDVAR2 4 行 + 表头). KB + prompt 双层 anchor, 解决 v1.3 Q-S2 ChatGPT PARTIAL label drift (C4).

### 各平台 bundle 变更

- **chatgpt**: `06_domain_examples_all.md` 重建 (含 PP/examples §6.3.5.9.3 Method label table); manifest 同步更新.
- **claude**: `09_examples_data_high.md` 重建 (2922→3268 行, A3.1 §N.N.N capture 修后首次正常). 含 Method label table + 3 处新捕获的 §N.N.N 段.
- **notebooklm**: bucket 16 (`16_fnd_pharma_pc_pp.md`) 重建 (含 Method label table).
- **gemini**: bundle 改动同步 KB delta (gem 自动 KB-grounding 拉取).

### Pipeline / build script 修复 (关键)

- **`ai_platforms/claude_projects/dev/scripts/extract_examples_data.py`** parents[3]→parents[4] path bugfix: Phase 6.5 reorg-A 引入的 path regression (script 移到更深一级目录后没同步 parents 索引). 影响: 全 28 domains 被误报 missing, A3.1 smoke 因不同 working config 漏检 (smoke 在 dev/ 跑, 实际生产路径不同). C4 rebuild 时实战触发 → fix → 3 bundle 重建成功 + 3268 行 examples bundle (含 §N.N.N capture).

### 验证

- **B1 UI sanity** (Chrome MCP fire-and-forget): 4 题 × 3 平台 = 12 cells = **10 PASS+ + 2 PASS + 0 PARTIAL + 0 FAIL = 100% PASS** (Gemini 4 cells excluded per §0.A).
  - Q-S1 BECAT EXTRACTION: 3/3 PASS
  - Q-S2 PP RELREC Method (v1.3→v1.4 main trigger): 3/3 PASS+ (Claude paper PARTIAL → UI PASS+ post A3.1 pipeline fix)
  - Q-S3 TR TRSTRESN/TRSTRESU typo: 3/3 PASS
  - Q-S4 DI domain (NotebookLM bucket 25): 3/3 PASS
- **B2 R4 17 题 full regression** (原 Gemini-only scope): **N/A** — 不再 sanity 测试 Gemini (详 §0.A; 优化继续, 测试不继续).
- **Q-S2 post-rebuild sanity recheck**: SKIPPED per user (grep-level 内容验证 deemed sufficient).
- **C2 UNSOURCED N=80 抽检**: 75 RI + 0 XLSX + 0 HALLUCINATED + 5 NEEDS_REVIEW (累计 N=80; v1.3 N=40 HIGH + v1.4 +40 LOW; HIGH pool 在 v1.3 已耗尽).
- **C1 section_coverage**: P4b deterministic rerun done — FULL_COVERAGE 101→137, SKELETON 67→46. md_atoms 仍 pre-v1.3 state (LLM pipeline rerun 推迟 v1.5 作为 C1-bis).

### 已知问题 (推迟至 v1.5 — 详见 KNOWN_LIMITATIONS §0)

- **C1-bis 完整 pipeline LLM rerun**: P2 增量 + P4a forward match + P4b (deterministic 部分 C1 已完成).
- **C1-ter post-P6 Makefile gate**: section_coverage 稳定性 gate.
- **C2 KB_INTERNAL_CROSSREF 新分类类别**: N=80 抽检暴露当前 4 类分类器需新增类别.
- **C2 3 个 deep paraphrase atoms manual review**: 5 个 NEEDS_HUMAN_REVIEW 中 3 个为 deep paraphrase 待人工判断.
- **C3 NotebookLM screenshot 教程 (Chrome MCP)**: v1.4 DEPLOY_GUIDE 加文字提示, screenshot 推迟.
- **Tier B 156 节 + 全 437 UNSOURCED + Phase 7 RAG+KG**: 全 carry from v1.3 §二.

### v1.3 → v1.4 升级方法

自部署用户:

1. **3 个有 sanity 覆盖平台 (ChatGPT / Claude / NotebookLM)**: 用 `self_deploy/<platform>/system_prompt.md` (或 `instructions.md`) 替换平台 system prompt; 用 `self_deploy/<platform>/uploads/` 中的对应 bundle 文件替换 uploads. 详细步骤见 `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md`.
2. **Gemini**: 用户自验. v1.4 提供 v9 system_prompt + Method label anchor + KB delta 增量, 但本平台**无 sanity 测试覆盖** — 答题正确性请用户自行验证, 推荐高正确性场景使用其他 3 平台.
3. **NotebookLM bucket 25** (v1.3 carry): 现有部署如仍含旧 source `25_td_meta_ti_ts_oi.md`, 上传 `25_td_meta_ti_ts_oi_di.md` 后**请手动删除旧 source** (43 → 42). v1.4 DEPLOY_GUIDE 含显眼提示.

**Tag**: `v1.4-company-release`

---

# SDTM 知识库 — Release v1.3 变更说明 (中文)

> Tag: `v1.3-company-release` (发布: 2026-05-20)
> 上一版: `v1.2-company-release` (2026-05-19)
> 触发: 知识库 pass — PP RELREC OA-4 缺口 + BECAT EXTRACTION prompt-KB 分叉 + Tier B 部分修复 + 4 平台重建 + 轻量 sanity 14-15/16 PASS

## 概要

v1.3 是**知识库 pass 级**版本 — 自 v1.0 以来最大规模的内容更新. 本版本直接修改 KB, 从更新后的源文件重建全部 4 平台 bundle, 并在 4 个已部署 AI 平台中端到端验证交付效果. Gemini system prompt (v8.1, 525 行) **不变** (与 v1.2 相同); v1.4 prompt 全栈重构推迟.

## v1.3 (2026-05-20) — 知识库 pass + 4 平台重建 + 轻量 sanity

**类型**: 知识库 pass (自 v1.0 以来最大规模内容改动; 非 prompt-only 刷新)

### 知识库改动 (11 个文件修改)

- **PP/examples.md** — 新增 §6.3.5.9.3 RELREC Method 快速参考 (Method A/B/C/D 表格 + Method C 的 1 个缩略 relrec.xpt). 关闭 06 Deep Verification 项目遗留的 OA-4 缺口. (bundle 中 +2,620 行)
- **BE/spec.md** — L111: 在 CDISC 标准示例 COLLECTION / PREPARATION / TRANSPORT 旁新增 `EXTRACTION` 作为申办方可扩展的第 4 个示例. 使知识库与 Gemini v8.1 prompt L272 保持一致.
- **TR/spec.md** (§6.3.12.2) — 修正列头 typo: TR 结果展示表中 `TRSTRESN` → `TRSTRESU`.
- **Tier B 修复 (另 8 个文件)** — 修复 10 个高密度 shall/must 节: §2.7 SDTM 变量规则, §6.4.2 FA 命名, §7.2.1 Trial Arms Example 4, §7.3.2/§7.3.3 TD/TM, §4.5.1.2 Tests Not Done, §6.4.3 FA --OBJ, §7.2.1.1 TA Distinguishing, §4.3.5.

### 各平台 bundle 变更

- **chatgpt**: 3 个文件更新 — `04_specs_and_context.md` (+284), `05_domain_assumptions.md` (+333), `06_domain_examples_all.md` (+5,432)
- **gemini**: 3 个文件更新 — `01_navigation_and_routing.md` (+3,103), `02_specs_and_assumptions.md` (+617), `03_domains_examples.md` (+5,432)
- **notebooklm**: 7 个文件更新 + 1 个改名 (`25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md`, bucket 名称现已体现 DI)
- **claude**: 5 个文件更新 — `02_chapters.md`, `03_model_structure.md`, `06_assumptions_all.md`, `09_examples_data_high.md` (+592), `10_examples_data_others.md`

### 构建脚本改动 (防御化加固)

- ChatGPT `merge_for_chatgpt.py`: `expected_segments` 由硬编码 `63/64/63` 改为动态 `len(_collect_domain_assumptions())`. 无段数 regression; delta >5% 时 warn 不 fail.
- NotebookLM 新增 `validate_bucket_coverage.py`: 190/190 KB 文件命中 bucket, 0 陈旧引用, 0 未路由域.

### 验证

- **阶段 B 跨平台 delta oracle**: 4 个字节精确等式 PASS (ChatGPT 04 delta = NotebookLM bucket 10 delta = Gemini 02 局部 delta, 以 BE/spec 改动为例). 0 静默丢失.
- **阶段 C 轻量 sanity (4 道题 × 4 平台 = 16 个格)**: 14-15/16 PASS.
  - Q-S1 BECAT EXTRACTION: 4/4 PASS (2 PASS+)
  - Q-S2 PP RELREC 4 方法: Claude PASS+, NotebookLM PASS+, ChatGPT PARTIAL (IDVAR 组合正确, Method 标签错位), Gemini FAIL (prompt bloat — v1.4 遗留)
  - Q-S3 TR TRSTRESN/TRSTRESU typo: 4/4 PASS (2 PASS+)
  - Q-S4 DI 域 / bucket 25 改名: NotebookLM PASS+ (footer 引用 `25_td_meta_ti_ts_oi_di.md`), Claude PASS+, Gemini PASS, ChatGPT 预期 PASS
- **UNSOURCED_MANUAL N=40 抽样**: 0% HALLUCINATED (80% REASONABLE_INFERENCE + 20% DERIVED_FROM_XLSX). Rule D `scientist` reviewer 确认.
- **system_prompt 审计**: 全 4 平台 20/20 grep 探针 PASS (0 陈旧数字引用).

### 已知问题 (推迟至 v1.4 — 详见 KNOWN_LIMITATIONS §0)

- **Gemini PP RELREC 检索弱** (阶段 C Q-S2 FAIL): Gemini v8.1 prompt bloat (525 行, 17 条 CO-N rules 形成化石层) 导致 PP RELREC 知识库接地失败. v1.4 主要遗留: 全 4 平台 prompt 全栈重构 (~200 行精简版, regex 门控 CO-N rules).
- **437 个 UNSOURCED_MANUAL 全量分类**: v1.3 仅抽样 N=40. 全量推迟.
- **Tier B 节 11-25 + 全部 level-2 Tier B**: v1.3 修复了排名 11-20 (10 节). 剩余约 156 节推迟.
- **R4 全 17 题 Gemini 回归**: v1.3 使用 4 道轻量 sanity 题 × 4 平台; Pro-only R4 因配额限制推迟.
- **section_coverage.jsonl 全流程重跑**: 基线已备份; 完整重跑推迟至 v1.4.

### v1.2 → v1.3 升级方法

自部署用户:

1. **全 4 平台**: 用 `self_deploy/<platform>/uploads/` 中的文件替换 uploads.
2. **NotebookLM**: 上传 `25_td_meta_ti_ts_oi_di.md` 并**删除**旧的 `25_td_meta_ti_ts_oi.md` (source 数应从 43 降至 42).
3. **System prompts / instructions**: 无需更改 (Gemini v8.1 + 其他 3 平台 prompt 与 v1.2 相同).

**Tag**: `v1.3-company-release`

---

## v1.2 (2026-05-19) — Gemini-only prompt 刷新 v7.1 → v8.1

> Tag: `v1.2-company-release` (发布: 2026-05-19)
> 上一版: `v1.1-company-release` (2026-05-15)
> 触发: SMOKE_V4 R3 (2026-05-19) Gemini v7.1 出现 regression → v8.1 system prompt 修复

v1.2 是 v1.1 的 **Gemini-only system prompt 刷新**. 知识库 / 4 平台 uploads / 全部元文档 / 其他 3 平台 (Claude / ChatGPT / NotebookLM) 的 system prompt 均与 v1.1 保持一致. **仅替换 `self_deploy/gemini/system_prompt.md`** (v7.1 → v8.1, 422 → 525 行, +24%).

### 触发: SMOKE_V4 R3 Gemini regression

v1.1 部署到 4 个 AI 平台后, 2026-05-19 跑了一次完整回归测 (SMOKE_V4 R3). 4 平台 3 个守住 R1 baseline:

- **Claude v2.6**: 17/17 (维持)
- **ChatGPT v2.2**: 17/17 (略升)
- **NotebookLM v2**: 15.5/17 (Q9 PUNT + Q11 PARTIAL 是 RAG 架构限制, 可预期)
- **Gemini v7.1**: **13/17 (4 FAIL)** — 相对 R1 16/17 倒退

### v8.1 改动概要

4-prong fix: CO-4 入口守门 (biospecimen 关键词) + CO-2f 文件格式 ground rule + CO-1e IS scope shift v3.3→v3.4 + CO-5 默认反思 (SDTM-regex KB 双核). 6 项 reviewer 驱动修订 (H1/H2/M1/M2/L1/L2). 详见完整 CHANGELOG.zh.md.

### 验证

- v8.1 dry-run: 4/4 PASS, Gemini 3.1 Pro (与 R3 baseline 同 model).
- Rule D #16 (`pr-review-toolkit:code-reviewer`): PASS_WITH_OBSERVATIONS, 6 项 reconcile fix apply.
- Rule D #17 (`oh-my-claudecode:verifier`): APPROVE 0 blocker.

**Tag**: `v1.2-company-release`
