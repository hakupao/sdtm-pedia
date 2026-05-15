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
