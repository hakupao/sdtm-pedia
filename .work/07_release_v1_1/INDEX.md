# .work/07_release_v1_1/ — Index

> Release v1.1 工程目录索引. v1.1 release cut 2026-05-15 + post-audit pass 2026-05-16, Tier 2 工作流纪律产物.
> Tag: `v1.1-company-release` + `v1.1` (短形式挂 GitHub Release). 上一版 v1.0 工程目录在 `.work/07_release/`.

## 顶层入口 (按读顺序)

| 文件 | 用途 | 触发 |
|------|------|------|
| `PLAN.md` | Tier 2 项目纪律入口, 10 step 工作流 + Rule A/B/C/D 约束 + 决策点 + 退出标准 | session 启动先读 |
| `RETROSPECTIVE.md` | Rule C 强制收尾产物, 四段: § 一 保留 / § 二 缺口 / § 三 决策 / § 四 post-audit (用户二次拷问后) | release 收尾必读 |
| `INDEX.md` | 本文件 | — |

## evidence/ — Rule A 抽检 + Rule D 审 + 构建日志 (10 files)

### 初次 rebuild (2026-05-15)

| 文件 | 内容 | 大小 |
|------|------|:---:|
| `diff_summary.md` | 4 平台 baseline vs rebuilt diff, byte-level delta 与 KB 06 改动一致性核 | 2.6KB |
| `rule_d_review.md` | Rule D verifier (`oh-my-claudecode:verifier` opus) 5/5 评估 ALL_PASS + Rule A 5×4=20 grep hits zero miss + 跨平台 delta oracle 自洽 | 13KB |
| `chatgpt_rebuild.log` | `merge_for_chatgpt.py --stage all` + batch2 retry (post DI 63→64 fix) 输出 | 3.7KB |
| `gemini_rebuild.log` | `merge_for_gemini.py --stage c_refactor` 输出 | 0.4KB |
| `notebooklm_rebuild.log` | `merge_sources.py` 输出 (42 buckets, 含 bucket 25 加 DI) | 4.3KB |
| `claude_rebuild.log` | executor subagent (sonnet) rebuild 7 文件 + 1 idempotent + 4 failures 详细 | 4.4KB |

### Post-audit (2026-05-16 用户拷问 ×2 后)

| 文件 | 内容 | 大小 |
|------|------|:---:|
| `rule_a_n20_audit.md` | subagent A 跑 Rule A EXTENDED audit (N=20 KB × 4 平台 + 22 bucket × 2 sample = 124 probe), **100% PASS** | 11.6KB |
| `gemini_04_audit.md` | subagent B 审 gemini writer-authored 04 文件, 发现 3 HIGH/MEDIUM omission gap + 4 diff 建议 | 11.2KB |
| `known_limitations_reconcile.md` | subagent B 比对 KNOWN_LIMITATIONS §1-§6 vs 06 RETROSPECTIVE §二 6 gaps vs Phase 5 carry, 建议 §0 加 Tier B 子项 | 11.5KB |

## failures/ — Rule B 失败归档 (不删, 留复盘)

| 文件 | 内容 |
|------|------|
| `claude_rebuild_failures.md` | F1-F4: executor 跑 claude rebuild 时遇到的 stale `REPO_ROOT` path bug + workaround |
| `rule_a_extended_failures.md` | subagent A 跑 Rule A N=20 时 Claude 4 个 verbatim near-miss (TA TATRANS / DI 分类 / FA Points to Consider / DS SUPPDS 例) — 设计上 Claude 是 compressed mega_spec/assumptions, KB 内容在 bundle 内但非 verbatim, 非 hard miss |

## 与 v1.1 release artifact 的关系

| 工程目录 (本) | release artifact |
|---|---|
| `PLAN.md` / `RETROSPECTIVE.md` | 内部纪律, 不进 release 包 |
| `evidence/diff_summary.md` 等 | 内部审 evidence, 不进 release 包 |
| `failures/*.md` | 内部 Rule B 归档, 不进 release 包 |
| → `release/v1.1/CHANGELOG.{en,zh,ja}.md` | 公开 release notes |
| → `release/v1.1/BUILD_MANIFEST.json` | 公开 release 文件清单 |
| → `release/v1.1/KNOWN_LIMITATIONS.{en,zh,ja}.md` | 公开限制声明 (§0 v1.1 audit scope + Tier B 子项) |
| → `release/v1.1/self_deploy/*/uploads/*.md` | 公开 deploy bundle (4 平台 self-host pack) |
| → GitHub Release v1.1 上的 4 个 zip 资产 | 公开下载入口 |

## Backups (已删)

最初备份 `backups/{chatgpt,gemini,notebooklm,claude}_uploads_baseline/` 共 25MB. v1.1 commit 上 main 后 baseline 可从 git 历史 (commit e63e5e7 前) 恢复, 删除以节空间. 见 `RETROSPECTIVE.md § 三 决策 1`.

## 后续 v1.2 计划

详见 `RETROSPECTIVE.md § 二 缺口` + `release/v1.1/KNOWN_LIMITATIONS § 0 v1.1 Audit Scope`:

- SMOKE_V4 R3 on deployed v1.1 (用户协作 cowork)
- Gemini 04 §12.3 TA TABRANCH/TATRANS depth (LOW 优先级 defer)
- Notebooklm bucket 25 改名 (含 DI 但仍叫 td_meta_ti_ts_oi — 改名 break 部署 URL)
- Tier B 166 KB sections (56 SIBLING_DROPPED + 110 CONTENT_TRUNCATED) 后续修复
- 437 UNSOURCED_MANUAL atoms 分类
- KNOWN_LIMITATIONS 自动 reconcile (vs RETROSPECTIVE §二缺口) workflow 集成
