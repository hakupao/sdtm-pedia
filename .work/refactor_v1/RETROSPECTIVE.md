# 项目重构 v1 — RETROSPECTIVE

> 创建: 2026-05-11 (段 3 close)
> 整体用时: 段 1 ~0.5h + 段 2 ~0.75h + 段 3 ~1.5h ≈ 3h total (低于 ~2-3 工作日估算)
> 触发: Bojiang 反映 agent 检索/更新/规划越来越费力

---

## 1. 保留下来的做法

**时序化分段执行**是本次重构最有效的策略。将高风险的路径迁移（段 3）锁定在 B-03c 大 cycle 收官后触发，完全避免了和正在跑批的 06 multi-session 抢写同一行的风险。段 1 / 段 2 在 06 round 间隙执行，零冲突。三段均各有独立 commit，可单独 `git revert`。

**path_migration.md 枚举表**提前写好、段 3 对照执行，效果非常好。sed 批量替换 + 双向 grep 校验（C-17/C-18）保证了无遗漏。最终验证：0 个 kickoff 文件还引用旧路径，所有主路由文件新路径引用齐备。

**"历史文件保留原样"原则**简化了执行。`historical_2026_04.md`、`website_phase*_handoff_*.md`、`07_website/phase*/` 内的 checkpoint 等全部保留旧引用，作为不可变历史记录，这与 path_migration.md 落空风险点一致，不引发路由断链。

---

## 2. 必须补上的缺口

**绝对路径与无尾斜杠双重问题**：METHODOLOGY.md 和 release 版的 Markdown 链接 URL 部分（`(.work/06_deep_verification/evidence/checkpoints)`，无尾斜杠）被第一轮 sed 漏掉——sed 模式带了尾斜杠，未匹配到。执行前 path_migration.md 没有单独列出这类无斜杠 URL 变体，导致需要补刀。**下次做 sed 批替换前，应先用 `grep -rn "旧串" | less` 浏览全量匹配，确认模式覆盖所有变体（带斜杠/不带斜杠/引号包裹/括号包裹）。**

**`.gitignore` 里的 `docs/jp/deliverable/*/`** 是隐蔽引用点，path_migration.md 表 9 虽提到了"检查 .gitignore"，但没明确列出这一条。下次迁移涉及 .gitignore 规则的路径时，应在 path_migration.md 表 9 直接写出需修改的行，而非仅写"检查命令"。

**`cp -r` 50MB 备份**耗时且在 repo 内占空间。本次备份目的是防 `git mv` 出错，但实际上 git 自身已经完整记录 mv 前状态，`git checkout HEAD -- .work/06_deep_verification/` 即可回滚。下次可改为：mv 前先做一个 commit（tag `pre-migration-snapshot`），省去 50MB 本地备份，也不污染工作区。

---

## 3. 关键决策复盘

**`branches/` 命名**：正确。`phases/` 在本项目已被 `.work/0N_xxx/` 占用语义，`branches/` 清晰表达"已从主工作流分离出去的独立旁枝"。后续如有新旁枝（如 docs/ko/ 或 Phase 8 附属产物）可直接加入 `branches/`。

**`project_knowledge_base/` 归档到 archive/**（段 1 决策）：正确。5MB 小目录，不值得 git rm，且偶尔回查"之前做错了什么"时仍有参考价值。

**`.bak` git rm 策略**（段 2 决策）：正确。从 85 个降到 1 个，.work/ 体积从 ~115MB 降到可管理范围。git history 是唯一可信的回滚来源，.bak 快照是重复冗余。

**`worklog.md` → 拆分 phase 文件**（段 2 决策）：正确。拆分后每文件 ≤500 行，`INDEX.md` 做统一入口，检索效率显著提升。唯一代价是 phase_jp_delivery.md 的 `docs/jp/` 历史 entry 留了下来，属可接受的历史痕迹。

---

> 规则 C 强制 retro — refactor v1 收官 2026-05-11
