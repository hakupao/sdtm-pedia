# 08 Repo Refactor v2 — PLAN

> 起草: 2026-05-11
> Tier: **2** (10 step, 半天-1 天)
> 目标: 根据 `docs/REPO_REFACTOR.md` 设计, 把 release 提升到顶层, 消除重复 tutorial, 建统一 build 入口
> 设计文档 (单一真源): `docs/REPO_REFACTOR.md`
> 决策: A/B/C/D 全部按推荐 (顶层提升 / 删 UPLOAD_TUTORIAL / tools 总入口 / pre-commit 警告)

---

## 步骤

| # | 步骤 | 文件/动作 | 状态 |
|---|---|---|------|
| 1 | git mv release | `git mv ai_platforms/release release` | ⬜ |
| 2 | web content config | 改 `web/src/content.config.ts` 的 RELEASE_DIR | ⬜ |
| 3 | web build script | 改 `web/scripts/build-bundles.sh` 的 SRC_ROOT | ⬜ |
| 4 | 删 frontmatter 脚本 | `web/scripts/add-frontmatter.mjs` (frontmatter 已写, 脚本作废) | ⬜ |
| 5 | 删 UPLOAD_TUTORIAL | `claude_projects/current/UPLOAD_TUTORIAL.md` + `notebooklm/current/UPLOAD_TUTORIAL.md` | ⬜ |
| 6 | 改名 upload_manifest | `chatgpt_gpt/current/upload_manifest.md` + `gemini_gems/current/upload_manifest.md` → `dev_manifest.md` | ⬜ |
| 7 | 建 build 入口 | `tools/build_release.sh` + `branches/jp_delivery/scripts/build_zip.sh` | ⬜ |
| 8 | 引用替换 | grep `ai_platforms/release` → `release` (active 文件; historical 不动) | ⬜ |
| 9 | .gitignore | `web/dist-bundles/*.zip`, `branches/jp_delivery/deliverable/*.zip` | ⬜ |
| 10 | pre-commit hook | 三语 tutorial.{en,ja,zh}.md mtime 偏差警告 | ⬜ |

---

## Active 文件清单 (步骤 8 引用替换)

**只更新这些 (active references)**:
- 仓库顶层: `CLAUDE.md`, `README.md`, `README_CN.md`, `METHODOLOGY.md`
- `docs/REPO_REFACTOR.md` (自指, 含路径示例需更新)
- web: `web/src/content.config.ts`, `web/scripts/*.{sh,mjs}`, `web/.cloudflare-pages.md`, `web/README.md`, `web/RELEASE.md`
- jp_delivery (active): `CHANGELOG.md`, `WORKLOG.md`, `_progress.json`, `sources/*.yml` (4 份)
- jp_delivery glossary/research_reports/*.md (8 份, 历史调研但 zip 引用还要重打)
- `docs/superpowers/plans/2026-04-27-sdtm-release-website.md` + `specs/...-design.md`
- 内部 `ai_platforms/release/v1.0/self_deploy/README.{en,ja,zh}.md` (git mv 后变 `release/v1.0/self_deploy/README.*`)

**不动 (historical / 归档)**:
- `.work/07_release/*` (closed phase)
- `.work/07_website/*` (closed)
- `.work/meta/*` historical worklog / handoffs
- `.work/refactor_v1/*` checkpoint 快照

---

## 验证 (step done = 这条 PASS)

- 步骤 1: `ls release/v1.0/` 存在 & `ls ai_platforms/release/` 不存在
- 步骤 2-3: `grep -l "ai_platforms/release" web/src/*.ts web/scripts/*` 返回空
- 步骤 4: `ls web/scripts/add-frontmatter.mjs` 不存在
- 步骤 5: 两个 UPLOAD_TUTORIAL.md 都不存在
- 步骤 6: 两个 upload_manifest.md 都改名为 dev_manifest.md
- 步骤 7: `tools/build_release.sh` + `branches/jp_delivery/scripts/build_zip.sh` 存在且可 bash -n 通过
- 步骤 8: `grep -rln "ai_platforms/release" --include="*.md"` 在 active 清单内为 0
- 步骤 9: `.gitignore` 含两条新规则
- 步骤 10: `.git/hooks/pre-commit` (或 husky 配置) 含三语检查

---

## 失败处理

任何步骤失败, 归档到 `evidence/failures/step_NN_attempt_X.md`, 不删数据, 记入下一 attempt 输入.

## 退出条件

- 全部 10 步骤验证 PASS
- 写 `RETROSPECTIVE.md` (Rule C 强制: 保留 / 缺口 / 决策)
- 用户 ack

---

*Single Source of Truth: 本 PLAN.md 只做执行追踪, 设计原理见 `docs/REPO_REFACTOR.md`*
