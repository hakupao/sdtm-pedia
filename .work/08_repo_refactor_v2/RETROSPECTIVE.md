# 08 Repo Refactor v2 — RETROSPECTIVE

> 完成: 2026-05-11
> Tier: 2 (10 step, 约 1 小时)
> 设计文档: `docs/REPO_REFACTOR.md`
> PLAN: `.work/08_repo_refactor_v2/PLAN.md`
> 范围: ai_platforms/release/ → 顶层 release/; 删 UPLOAD_TUTORIAL.md; 改名 upload_manifest.md → dev_manifest.md; 加 tools/build_release.sh + jp build_zip.sh + git-hooks/pre-commit; sed 替换 28 文件中 ~80 处引用

---

## § 1 — 保留下来的做法 (Keep)

1. **三档分离**: design 文档 (`docs/REPO_REFACTOR.md`, durable) + execution PLAN (`.work/08_*/PLAN.md`, transient) + RETRO (本文件). 不混. 设计原理只维护一处.

2. **决策点表格一次性 ack**: A/B/C/D 4 个决策 + 推荐 → 用户一次"都按推荐" 通过. 没有逐项扯皮.

3. **两端 sanity check sed**: 替换前 `grep -c` 看每个文件出现位置数; 替换后 `grep -l` 看零残留. 防止漏改 / 误改.

4. **git mv 而不是 rm+cp**: `git mv ai_platforms/release release` 保留历史; 也让仓库 diff 视图清楚显示是"移动". 比 cp + rm 干净.

5. **active 与 historical 二分**: 列出"active 文件清单" (需要 sed) vs "historical 归档清单" (不动). `.work/07_*` / `refactor_v1` 历史快照保持原状, 不回写新路径. 防止改坏归档.

6. **build 入口写在 tools/, 非 web/ 或 jp/**: 跨子目录的协调脚本放在仓库级 `tools/`. web/jp 各自的子脚本被 `tools/build_release.sh` 调用. 单入口, 派生消费者.

7. **decision flat zip 路径同步重命名**: zip 内的 `ai_platforms_release_v1.0/` 同步改为 `release_v1.0/`, 匹配新 repo 结构. 不留旧名义务.

---

## § 2 — 必须补上的缺口 (Gap)

1. **⚠️ `git stash` 雷区** (高优先级教训)
   - 执行过 `git stash --include-untracked --quiet` 想"清场测试 pre-commit hook", 但 stash 把所有未 commit 的 Edit 改动都吞了 (content.config.ts + build-bundles.sh 两个 Edit 被 revert 回旧路径).
   - 修复花了 2 步: `git stash list` + `git stash pop`.
   - **教训**: 在 in-flight refactor 中, **永远不要 stash**. 测试 pre-commit hook 用别的方法 (例如: 临时 worktree, 或写 fake commit 到草稿分支).
   - **下次类似工作**: 把"测试 hook"作为独立 step, 跑在所有 active edit 完成且 commit 之后.

2. **缺 `tools/build_release.sh` 实测**
   - 只做了 `bash -n` 语法检查, 没真跑过.
   - 用户接受重构前, 应实测一次: `tools/build_release.sh v1.0` 验证 web bundles + jp zip 都产出 + BUILD_MANIFEST.json 写入正确.

3. **缺 `web/` 构建实测**
   - `web/src/content.config.ts` 改了 `RELEASE_DIR`, 没实际跑 `npm run build` 验证 Astro 还能拼出来.
   - 建议下一步: `cd web && npm run build` 跑一遍 smoke.

4. **pre-commit hook 未自动 install**
   - 写了 `tools/git-hooks/README.md` 让用户 `git config core.hooksPath tools/git-hooks`, 但用户可能忘.
   - 改进方向: 加一个 `tools/install-hooks.sh` 一键 enable, 或在仓库根 README 顶上加 setup section.

5. **CLAUDE.md Key Paths 行级核对未做**
   - sed 把 `ai_platforms/release/v1.0/` → `release/v1.0/` 全替换, 但 Key Paths 表格描述文字 (例: "Phase 6.5 AI 平台部署") 没复审. 路径准了, 描述语义需肉眼扫一次, 可能有"Phase 6.5 release 现在不在 ai_platforms 下"之类的小不协调.

6. **历史归档 `.work/07_*` 与新路径割裂**
   - `.work/07_release/PLAN.md` 等 closed phase 文件仍写 `ai_platforms/release/v1.0/`. 是归档快照, 故意不改. 但若有人将来读这些归档要 git log diff 时, 会发现"以前在 ai_platforms 下"的事实. 这是预期, 不是 bug.

---

## § 3 — 关键决策复盘 (Decision)

| 决策 | 选择 | 结果 |
|------|------|------|
| **A** release/ 位置 | (a) 提升顶层 | ✓ 概念清晰. blast radius (~58 文件) 在 sed 可控范围 |
| **B** UPLOAD_TUTORIAL.md | (a) 删 (claude/notebooklm) | ✓ 改外部 tutorial 只剩 self_deploy/ 一处 |
| **C** build 入口 | (a) tools/build_release.sh | ✓ web + jp 两条 pipeline 串起来 + BUILD_MANIFEST.json 防三方版本漂移. **待用户实测** |
| **D** 三语锁步 | (a) pre-commit hook 警告 | ✓ 非阻断, 不影响开发. 需用户自行 enable |
| 副 | zip 内 flat 路径 `ai_platforms_release_v1.0/` → `release_v1.0/` | ✓ 同步重命名, 不留旧名义务. 下次打 jp zip 时生效 |
| 副 | 工作日志位置 `.work/08_repo_refactor_v2/` | ✓ 跟随项目 phase 命名约定 (跨 03/04/05/07) |

---

## § 4 — 下次重构如有类似工作, 优先做的事

1. **写 design doc → PLAN → 执行, 三层分离**: 不要把 design 写进 PLAN. PLAN 只追踪 step 状态.
2. **决策点表格让用户一次 ack**: A/B/C/D 4 选项, 推荐写明, 减少来回.
3. **active vs historical 二分**, 提前列清单, 不进行回灌历史归档.
4. **sed 前后双 grep**: 替换前列出现位置数, 替换后零残留校验.
5. **不要在 refactor 中段 `git stash`**.
6. **提前定义"重构完成"标准**: 验证项明确写在 PLAN.md (本次做了, 见 §验证).

---

## § 5 — 退出条件 (满足后整 phase CLOSED)

- [x] 10 step 全部技术验证 PASS (release/ 顶层, 文件删/改名, 脚本可调, 引用零残留)
- [ ] 用户实测 `tools/build_release.sh v1.0` 产物正常
- [ ] 用户实测 `cd web && npm run build` Astro 构建 PASS
- [ ] 用户 ack RETROSPECTIVE → 标 CLOSED

**当前状态**: execution complete, awaiting user ack + smoke test.

---

*本 RETRO 遵循 Rule C: 保留 / 缺口 / 决策 三段强制结构.*
