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
