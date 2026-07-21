# SDTM 知识库 — Release v1.2 变更说明 (中文)

> Tag: `v1.2-company-release` (发布: 2026-05-19)
> 上一版: `v1.1-company-release` (2026-05-15)
> 触发: SMOKE_V4 R3 (2026-05-19) Gemini v7.1 出现 regression → v8.1 system prompt 修复

## 概要

v1.2 是 v1.1 的 **Gemini-only system prompt 刷新**. 知识库 / 4 平台 uploads / 全部元文档 / 其他 3 平台 (Claude / ChatGPT / NotebookLM) 的 system prompt 均与 v1.1 保持一致. **仅替换 `self_deploy/gemini/system_prompt.md`** (v7.1 → v8.1, 422 → 525 行, +24%).

## 触发: SMOKE_V4 R3 Gemini regression

v1.1 部署到 4 个 AI 平台后, 2026-05-19 跑了一次完整回归测 (SMOKE_V4 R3). 4 平台 3 个守住 R1 baseline:

- **Claude v2.6**: 17/17 (维持)
- **ChatGPT v2.2**: 17/17 (略升)
- **NotebookLM v2**: 15.5/17 (Q9 PUNT + Q11 PARTIAL 是 RAG 架构限制, 可预期)
- **Gemini v7.1**: **13/17 (4 FAIL)** — 相对 R1 16/17 倒退

Gemini 4 失败:

| # | 题型 | v7.1 失败模式 |
|---|---|---|
| Q3 | BE / BS / RELSPEC 生物样本处理 | 跑题答 AE / AESEV / AEGRPID (1,541 字符) |
| Q4 场景 A | 抗麻疹病毒 IgG 滴度 | 答 LB 而非 IS (R2 修过的退回) |
| Q11 | Dataset-JSON v1.1 vs XPT v5 | 跑题答 AE / CM (1,436 字符) |
| AHP1 | LBCLINSIG 变量幻觉探针 | 跑题答 CM 多药 / MH (1,485 字符) |

独立 reviewer (`oh-my-claudecode:scientist`, Rule D #15) 核对一致, 根因为 Gemini v7.1 system prompt 缺 4 个锚点覆盖:

1. **Q3** — 无 biospecimen 关键词入口守门, Gemini 走高频 SDTM 域 (AE / CM) 兜底.
2. **Q4 A** — 无 v3.3 → v3.4 IS scope shift sticky anchor; R2 修过的 fix decay.
3. **Q11** — 无文件格式 ground rule; Gemini 用 SDTM domain 内容替换了文件格式问题的回答.
4. **AHP1** — Anti-hallucination 锚仅在题文含 reflection scaffold 时触发; plain factual 探针漏触发.

## v8.1 改动详情

### 4-prong fix

- **CO-4 入口守门 (NEW)**: 题文含 biospecimen 关键词 (中英文 13 项), 强制锚 BE / BS / RELSPEC, 禁 AE / CM fallback.
- **CO-2f 文件格式 ground rule (NEW)**: 题文涉及 XPT / Dataset-JSON / Define-XML / submission format, 答案 ground 在 CDISC 公布格式 spec. 含答完 off-topic 守门.
- **CO-1e IS scope shift v3.3 → v3.4 (NEW)**: anti-microbial antibody 测量 (麻疹 / HBsAb / HCV / COVID / ADA, 不论 timing) 归 IS, 不归 LB / MB. HIV Ag / Ab combo 例外走 MB (KB IS Assumption 5). ISTSTOPO 三层结构标注 Assumption 8.
- **CO-5 默认反思 (MOD)**: 题文中任何匹配 SDTM-shaped regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 的标识符, 在主答前**必先**做 KB 双核, 不依赖题文 phrasing. KB 未命中触发 AHP-V1 识破模板. 否定清单 + CO-2f 优先 gate 防过度触发.

### 6 reviewer 驱动修订 (Rule D #16 reconcile)

- **H1**: HIV Ag / Ab combination → MB (不是 LB), KB IS Assumption 5.
- **H2**: CO-2f 文件格式锚优先于 CO-5 regex 变量幻觉路径.
- **M1**: regex 否定清单 — 常见非 SDTM 缩写 (`FDA` / `CDISC` / `XPT` / `JSON` 等) + SDTM 域缩写跳过 KB 双核.
- **M2**: 题文候选 ≥ 5 时, 仅对题文显式提及的 3-5 个跑双核.
- **L1**: ISTSTOPO 来源更正为 IS Assumption 8 (之前误标 7a).
- **L2**: BECAT 示例 `"EXTRACTION"` 注 sponsor-extensible (KB BE / spec L111 只 inline 3 个标准 examples).

## Dry-run 验证 (Gemini 3.1 Pro, 2026-05-19 16:35-16:40 PM)

Pro 配额重置后立即重测 v7.1 4 道失败题, 使用与 R3 baseline 相同 model. 4/4 PASS:

| # | v7.1 R3 | v8.1 dry-run | Prong + Fix 验证 |
|---|---|---|---|
| Q3 | FAIL (AE 跑题) | PASS (1,439c, 47.6s) | Prong 1 + L2 |
| Q4 | FAIL (A=LB) | PASS (1,763c, 52.7s) | Prong 3 + H1 + L1 |
| Q11 | FAIL (AE/CM 跑题) | PASS (3,768c, 30.6s) | Prong 2 + H2 |
| AHP1 | FAIL (CM/MH 跑题) | PASS (694c, 46.6s) | Prong 4 + M1 — 7/7 AHP-V1 元素 fire |

独立 Rule D #17 reviewer (`oh-my-claudecode:verifier`) 对照 KB 源验证 4/4 PASS, APPROVE 0 blocker.

## 各平台包变更

### Gemini Gems (`self_deploy/gemini/`)

- **system_prompt.md**: 替换 (v7.1 → v8.1, 422 → 525 行).
- **uploads/*.md**: **不变** (与 v1.1 完全一致; KB 自 v1.1 后未改).
- **tutorial.{en,zh,ja}.md**: 不变.

### Claude Projects / ChatGPT GPTs / NotebookLM

- 全部文件 byte-identical 继承 v1.1. 无 KB rebuild, 无 prompt 改动.

## v1.1 不变项

- 全部知识库内容.
- 4 平台全部 uploads bundles.
- 全部元文档 (METHODOLOGY / USER_GUIDE / PLATFORM_COMPARISON / DEMO_QUESTIONS / GLOSSARY / README 各 en/zh/ja).
- Claude / ChatGPT / NotebookLM 全部 system prompts 和 tutorials.

## 验证

- v8.1 dry-run: 4/4 PASS, Gemini 3.1 Pro (与 R3 baseline 同 model).
- Rule D #16 (`pr-review-toolkit:code-reviewer`): PASS_WITH_OBSERVATIONS, 6 项 reconcile fix apply.
- Rule D #17 (`oh-my-claudecode:verifier`): PASS_WITH_OBSERVATIONS — APPROVE 0 blocker.
- 完整 audit evidence: `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-19/`.

## 已知 caveat (留 v1.2 post-cut)

- **R4 17 题全量回归**: 仅 4 道 v7.1 FAIL 题重测, 13 道 v7.1 PASS 题在 v8.1 下未测. CO-5 默认反思 regex 与候选数限在多变量题上未独立验证. 留 v1.2 post-cut.
- **BECAT EXTRACTION KB-prompt 注释**: v8.1 prompt L272 把 `"EXTRACTION"` 列入 BECAT 示例, KB BE / spec L111 只 inline 3 个标准 examples. 答案已标注 sponsor-extensible, 未来 prompt 修订可加显式来源引.
- **M2 候选数限**: 4 道 dry-run 题候选数 < 5, 没真触发 threshold. 留 R4 多变量题验证.

## v1.1 → v1.2 升级方法

自部署用户:

1. 替换 Gemini Gem instructions field 内容为 `self_deploy/gemini/system_prompt.md` (525 行).
2. **其他无需操作**. Uploads / 其他平台 prompts / tutorials / 元文档**均不变**.
3. Gemini Gem 上现有 chat session 在下一条消息时自动使用新 prompt.
