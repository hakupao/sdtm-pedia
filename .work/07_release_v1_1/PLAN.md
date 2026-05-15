# Release v1.1 Plan — Rebuild 4 AI Platform Bundles after 06 Deep Verification

> Tier 2 项目纪律 (Rule A/B/C/D 强制)
> 入口建立: 2026-05-15
> 终止条件: v1.1 release tag cut + 4 平台 uploads 同步 + CHANGELOG/SYNC_BOARD 更新 + RETROSPECTIVE.md 三段齐备
> 上一版: tag `v1.0-company-release` (2026-04-27)

## 背景

06 Deep Verification 旁枝 (P1-P7, 2026-04-24→2026-05-12) 完成后, knowledge_base/ 有 43 文件 +1,405 / -234 行净更新, 包括:
- 新增 domain DI (Device Identifiers SDTMIG-MD); KB 现 64 domains
- chapters/ch02/ch04/ch08/ch10 补强
- PC/assumptions 补 §6.3.5.9 RELREC linking (+118 行)
- TA/assumptions 补 +175 行
- 多 30+ 文件 P6 T4 Tier A 修复

这些修复尚未回灌至:
- `ai_platforms/{claude_projects,chatgpt_gpt,gemini_gems,notebooklm}/current/uploads/` (各平台 deploy bundle)
- `release/v1.0/self_deploy/*/uploads/` (release tag 不可变, 但需 cut v1.1)

## 工作步骤

### Step 1 — Setup ✅
- 建 `.work/07_release_v1_1/{evidence,failures,backups}/`
- 备份 4 平台 current/uploads/ baseline 到 backups/ (25 MB)

### Step 2-5 — 4 平台 rebuild (并行)
- **chatgpt** (Task #2): `merge_for_chatgpt.py --stage all`
  - Bug 修复: 05 expected_segments 63→64 (DI 新加 1 assumption), token_cap 69K→85K
- **gemini** (Task #3): `merge_for_gemini.py --stage c_refactor`
  - 脚本自动迭代 domains/ 目录, 无 stale 硬编码
- **notebooklm** (Task #4): `merge_sources.py`
  - bucket_config.json 修补: bucket 25 加 `domains/DI/assumptions.md` (DI 属 study reference dataset, 与 TI/TS/OI 同 bucket)
- **claude_projects** (Task #5, 派 executor 后台跑): v1 + v2 双 builder 系统, 路径需修复

### Step 6 — Diff baseline vs rebuilt (Rule A 抽检)
- 文件级 diff + size delta + 段数核验
- 写到 `evidence/diff_summary.md`
- 抽检: 改动应集中在 06 P6 T4 涉及的 KB 源文件

### Step 7 — Rule D 独立 reviewer
- 候选 subagent_type (不同于 main session): `oh-my-claudecode:verifier` 或 `oh-my-claudecode:critic`
- 评估: rebuilt uploads 是否真实反映 06 修复 / 没有 silent 数据损失 / 段数 token 数合理
- 输出 `evidence/rule_d_review.md`

### Step 8 — Cut release v1.1
- 创建 `release/v1.1/self_deploy/{claude,chatgpt,gemini,notebooklm}/{uploads, system_prompt.md/instructions.md, tutorial.*}`
- 元文档继承 v1.0 (system_prompt, tutorial 三语 — 06 未改方法论核心)
- CHANGELOG.{en,zh,ja}.md (说明: rebuilt for 06 P6 T4, DI domain added, 4 platform bundles refreshed)
- BUILD_MANIFEST.json (各平台文件清单 + 总 token/word 数)

### Step 9 — Sync state
- `ai_platforms/SYNC_BOARD.md`: 新增 v1.1 rebuild Phase 段
- 各 `_progress.json`: 加 v1.1 entry
- `.work/meta/worklog/phase_07_release.md`: append v1.1 cut record (新建若无)
- `docs/PROGRESS.md`: milestone "06 旁枝 → release v1.1 rebuild"
- `CLAUDE.md` Key Paths: 加 `release/v1.1/` 入口, 清理过期 round 状态

### Step 10 — RETROSPECTIVE + commit (Rule C 强制)
- `.work/07_release_v1_1/RETROSPECTIVE.md` 三段
- 单 commit + push: "07 Release v1.1 — rebuild 4 platform uploads incorporating 06 deep verification fixes"

## 规则约束

- **Rule A** (语义抽检): 改动 >50% (新加 DI 整域) → 至少 N=5 抽检 8 个原子级 sample
- **Rule B** (失败归档): 任何 rebuild 失败的文件 → `failures/<file>_attempt_N.md`, 不删
- **Rule C** (Retro 强制): 收尾前必写 RETROSPECTIVE.md 三段
- **Rule D** (审阅隔离): writer (main session) ≠ reviewer (派独立 subagent_type)
- **PASS 四条**: evidence 存在 / writer 合规 / 独立 reviewer PASS / 用户口头 ack

## 关键决策点

1. **DI 加进 notebooklm bucket 25 (td_meta_ti_ts_oi)** — DI 是 study reference dataset, 与 TI/TS/OI 同类; 替代方案 bucket 18 (device findings) 类型不符 (DI 非 findings)
2. **claude_projects v1 + v2 双 builder 都需要 run** — 19 文件中 11 来自 v2 (chapters/examples/terminology), 8 来自 v1 (routing/index/specs/assumptions/examples_catalog/terminology_map/model); 06 改的 chapters/assumptions/examples 跨越两套
3. **terminology bundle 不重 build** — terminology/ 在 06 完全未触, 11/12/13 (claude) 和 07/08/09 (chatgpt) 保持 idempotent skip
4. **release v1.0 tag 不可变, cut 新 v1.1 tag** — 保留 v1.0 历史完整性, v1.1 反映 06 后状态

## 失败模式预案

- 若 claude 某 v1 子脚本 broken (路径或依赖) → 该文件保留 v1.0 baseline + 写 failures/, 不阻塞 release v1.1 cut (其他 18 文件已新)
- 若 notebooklm DI 加进 bucket 25 但破坏 token budget → 改加进 bucket 18 (device 类) 或 bucket 30 (ig appendix), 写 failures/

## 退出标准 (规则 D + 用户 ack)

- [ ] 4 平台 rebuild 至少 3 个完整 PASS, 失败 ≤1 文件 (含原因)
- [ ] diff_summary.md 写就 + 与 KB 06 改动一致性 RuleA 抽检 PASS
- [ ] Rule D 独立 subagent reviewer PASS
- [ ] release/v1.1/ 结构完整, CHANGELOG 三语 + BUILD_MANIFEST.json
- [ ] SYNC_BOARD.md / docs/PROGRESS.md / CLAUDE.md Key Paths 更新
- [ ] RETROSPECTIVE.md 三段齐备
- [ ] 用户 ack 进 commit + push + tag
