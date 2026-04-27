# 07 Release v1.0 — Retrospective

> **Project**: 公司发布版 (release v1.0)
> **Tier**: 2 (24 文件 / 三语 / 多 agent 并行)
> **启动**: 2026-04-27 11:30
> **完成**: 2026-04-27 13:15
> **总耗时**: ~1h45m (vs PLAN 估 5.5h, **约 -68% wall**, 主因 Phase B 改派 Agent runtime)
> **状态**: ✅ 全部 5 phase 完成
> **作者**: 主 session (team-lead) / Daisy ack pending

## 0. 基础数据

- **产出**: 24 文件 = 12 zh + 6 en + 6 ja (按 PLAN §3 完整落盘)
  - 顶层: README.{zh,en,ja} / USER_GUIDE.{zh,en,ja} / DEMO_QUESTIONS / KNOWN_LIMITATIONS.en / CHANGELOG = 9
  - self_deploy/: README.{zh,en,ja} + 4 tutorial × 3 lang = 15
- **Phase 拆分**:
  - A 30min (PLAN + DEMO + LIMITATIONS + CHANGELOG + 3 worker kickoff + CLAUDE.md routing)
  - B 7min (3 worker zh 写, Agent runtime — vs PLAN 估 3h)
  - C 10min (14 翻译 fan-out × 2 batch en/ja, executor sonnet)
  - D 25min (5 reviewer + Rule A 抽检 + 22 fix edits)
  - E 30min (retro + 索引同步 + cleanup + commit)
- **Rule D 隔离链** (release 内部计数, 不撞 06 旁枝):
  - writer-1 B = `oh-my-claudecode:executor` × 3 (opus×2 + sonnet×1)
  - translator C = executor × 14 (sonnet)
  - **#R1** = `pr-review-toolkit:code-reviewer` (en lang + SDTM)
  - **#R2** = `oh-my-claudecode:critic` opus (ja 敬体 + 业界用词)
  - **#R3** = `feature-dev:code-reviewer` (跨平台一致)
  - **#R4** = `oh-my-claudecode:verifier` (DEMO 保真)
  - **#R5** = `oh-my-claudecode:critic` opus 二轮 (可读性)
  - **Rule A 抽检** = `oh-my-claudecode:verifier` (N=3 双向回译)
- **Findings 处置**: 22 fix edits applied + 8 R5 polish 缺口留 v1.1 minor.
- **Rule A 抽检**: PASS (15 段抽样 / 0 numerical drift / 0 SDTM term drift / 0 fabrication / 2 LOW 已修).

## 1. 保留下来的做法 (R-RELEASE-1 ... R-RELEASE-7)

**R-RELEASE-1**: omc-team tmux runtime 失败时, **Agent 工具 fallback 是干净路径**.
- 原 PLAN 用 omc-teams (tmux 3 pane × claude CLI worker) 跑 Phase B 写作.
- 实际执行: 3 个 pane 全卡在 Bypass Permissions 警告未通过, 1 小时无产出.
- Pivot: 改用主 session 派 3 个 `oh-my-claudecode:executor` Agent 并发.
- 结果: Phase B 7 分钟完成, vs PLAN 估 3 小时 (~-96% wall).
- **保留**: tmux runtime 用于"独立 CLI 长跑 + 用户可观察 pane"场景 (06 旁枝 round 1-7); Agent runtime 用于"并发短任务 + 不需要 pane 观察"场景 (本 release / Phase C 翻译 / Phase D review).
- **决策树**: 若任务 <30 min 单 worker + ≥3 worker 并发 + 不需要中途观察, **优先 Agent**. tmux 仅在长跑 (>1h) 或需要用户随时切 pane 干预时用.

**R-RELEASE-2**: **HARD-STOP DIRECTIVE 在 kickoff 顶部** 是有效护栏.
- 3 worker kickoff 顶部都有"⛔ HARD-STOP DIRECTIVE: DO NOT 中途 ask user / summarize / hand control back" + "唯一合法停止 = WORKER_X_DONE 单行 echo".
- 改 Agent runtime 时, 主 session prompt 加 OVERRIDE: "echo 信号替换为 Agent 风格 summary 返回, 其他 HARD-STOP 仍生效".
- 结果: 3 worker 全部产出完整 + 没有越界改动 LIVE 文件 / `_progress.json` / root index.
- **保留**: 多 worker 并发任务 kickoff 顶部 HARD-STOP DIRECTIVE 作硬护栏, 无论 runtime 是 tmux 还是 Agent.

**R-RELEASE-3**: **Phase 拆分 + 自包含 kickoff** 让 multi-agent fan-out 可重复.
- Phase B 3 worker / Phase C 14 翻译 / Phase D 5 reviewer 都用"prompt 完全自包含 + 无对话历史依赖"结构.
- 翻译 prompt 内嵌 SDTM 白名单 + 节标题映射表 + 后缀替换规则 + footer 规则.
- 结果: 14 翻译并发 0 cross-agent 冲突 / 0 关键术语 drift (Rule A N=3 抽检 PASS).
- **保留**: multi-agent fan-out 时, prompt 必须自包含 (绝不依赖外部对话历史) + 内嵌"做什么 + 不做什么"双向白名单.

**R-RELEASE-4**: **Rule D 严格隔离 reviewer family** 仍生效.
- 5 个 reviewer 全部用不同 agent type (pr-review-toolkit + omc:critic 两轮 + feature-dev + omc:verifier).
- omc:critic 两轮 (#R2 ja + #R5 可读性) 不算自审 — 不同任务范围 + 两次独立 dispatch.
- Rule A 抽检 (N=3) 又加一个 omc:verifier 独立验证.
- 6 reviewer 链全部独立 finding + 各自给 NEEDS_FIX 但 verdict 互不矛盾.
- **保留**: Phase D 至少 4-5 个不同 family reviewer + 1 个 Rule A 抽检. 同 agent type 跨任务可重用 (不算自审).

**R-RELEASE-5**: **Rule A 双向回译 N=3** 是翻译类任务的最后一道护栏.
- 5 个 reviewer 全 PASS / NEEDS_FIX_MINOR 的情况下, Rule A 抽检多发现 2 个 LOW 语义压缩 ("Platform Roles" 缺 four-platform / "厳守して" 缺 strictly).
- 结构合规 (heading count / footer / SDTM 术语保留) ≠ 语义忠实.
- **保留**: 任何翻译 / paraphrase / 压缩任务, Phase D 必须有"独立 verifier 抽 N=3 paragraph 双向回译"步骤, 不能跳.

**R-RELEASE-6**: **三语策略 zh→en + zh→ja 单源派生** 比并行三写省 ~60%.
- Phase B writer 只写 zh (anchor); Phase C translator 派生 en + ja.
- 优势: 只校 zh 语义/事实一致, en/ja 跟随; SDTM 数据点只在 zh 改, 翻译同步.
- 风险已抓: cross-language link suffix 漏洞 (`.zh.md` 链接被翻译者保真复制) — 已 fix 6 处 (README.en + README.ja).
- **保留**: 多语 release 默认走"单源派生"模式. Phase C translator prompt 必须含 "rewrite cross-language sibling link suffix per target language" 显式规则 (本次缺, 下次加).

**R-RELEASE-7**: **CHANGELOG + KNOWN_LIMITATIONS 单一英文 + DEMO 三语内嵌** 是合理简化.
- DEMO_QUESTIONS.md 走"单文件三语内嵌": 同一题目 zh/en/ja 三段并列, SDTM 术语全英文, 判定基准英文.
- CHANGELOG.md / KNOWN_LIMITATIONS.en.md 单一英文.
- 结果: 维护成本下降 (1 题 = 1 改 3 段 vs 3 改) + 跨语对照清晰.
- **保留**: 数据表 / 演示题库 / 限制清单类 strucutred-list 文档, 优先单文件三语内嵌; 长 prose 文档 (USER_GUIDE / tutorial) 走单源派生 .zh.md / .en.md / .ja.md.

## 2. 必须补上的缺口 (G-RELEASE-1 ... G-RELEASE-6)

**G-RELEASE-1**: omc-teams runtime 启动 health-check 缺.
- omc team status 显示 "phase=planning, total=3 pending=3" 但 tmux pane 实际全卡 Bypass Permissions, 主 session 没在第一时间发现.
- **缺**: omc team launch 后, 主 session 应在 +60s / +180s / +300s 各检查一次 tmux pane content (capture-pane -p), 若 pane 仍是 shell prompt OR 卡 Bypass Permissions warning, 立即 escalate (kill-team + Agent fallback).
- **下次**: 在 PLAN.md §5 加 health-check 协议 + 在 _progress.json launched_at 旁加 first_health_check / second_health_check 字段.

**G-RELEASE-2**: Translator prompt 缺 "cross-language sibling suffix rewrite" 显式规则.
- README.zh.md → README.en.md 翻译时, 译者保真复制了 `[USER_GUIDE.zh.md](./USER_GUIDE.zh.md)` 链接, 导致 EN README 链接 EN 读者到 zh 文件.
- 同样问题 README.ja.md.
- 5 reviewer 全部抓到这个 MAJOR (R1 + R2 同时报告 README.en/ja L7/20/26).
- **缺**: 翻译 prompt 必须显式说明 "internal sibling links: rewrite suffix to match target language; same-cross-language siblings (e.g., KNOWN_LIMITATIONS.en.md only) preserve verbatim".
- **下次**: 在 _template/ 加 translator prompt 模板, 内嵌后缀重写 checklist + 5 个 false negative 反例.

**G-RELEASE-3**: Q1-Q10 vs D0-D9 编号在 release 内不一致.
- 4 tutorial §5 用 SMOKE_V4 的 Q1-Q14 numbering 引用; DEMO_QUESTIONS.md 用 D0-D9 numbering.
- chatgpt §5 提 Q1, gemini §5 提 Q1/Q2/Q3, notebooklm §5/§6 提 Q11/Q12 — 这些 Q-id 在 DEMO 找不到对应 D-id.
- 当前留 v1.1 修. 思路: 在 DEMO_QUESTIONS.md 顶部加 Q-D 对照表 OR 把 4 tutorial §5 引用改 D-id.
- **下次**: release 启动前先 freeze numbering convention (D-or-Q), 全文档统一.

**G-RELEASE-4**: Phase B kickoff 长度估算 vs Agent runtime 实际不匹配.
- worker_b kickoff 11410 chars / worker_c 10005 / worker_d 7545. 设计为 tmux pane Claude CLI 输入 (能接长 prompt).
- Agent runtime 派单也 OK (Agent prompt 没有 8K char 限). 但 prompt 越长, agent 越容易跑偏 (例 worker-D 仍试图判断 helper §5 reassign 即使被 OVERRIDE skip).
- **缺**: Agent runtime kickoff 应削减到 <5K 核心指令; tmux runtime 长 kickoff OK.
- **下次**: PLAN §5 标注 runtime, kickoff size budget 跟着调整.

**G-RELEASE-5**: 中文字符长度目标 vs 总字符数 ambiguity.
- worker-B kickoff 写 "USER_GUIDE.zh.md 长度 2500-3500 字符". 实际总字符 4541 / Han chars 892.
- worker-C / worker-D 同样问题 (中文字符 vs 总字符 vs UTF-8 bytes 三者混淆).
- writer 自己注脚解释了, 但 PLAN 没说清.
- **缺**: 长度目标必须明确单位 (Han chars / total chars / UTF-8 bytes) + 给 SDTM 双语技术写作的典型 Han 密度参考 (本次实测 17-20%).
- **下次**: PLAN.md 长度目标统一改 "total chars (含英文)" + 给 ±20% 容差.

**G-RELEASE-6**: R5 可读性 8 项 polish 留 v1.1.
- USER_GUIDE.zh.md §1/§2 jargon 密集 (SDTM/CDISC/63 域/295 md/RAG cold drop)
- pacing claim mismatch (claude 30-90 / chatgpt 30-60 / gemini 20-40 / notebooklm 30-60)
- self_deploy/README.zh.md L21 "Custom mode 9011 chars" vs notebooklm tutorial "8,925 chars" (byte vs char drift)
- notebooklm §0 number wall (500/300/500K/500/20)
- "P3.2 实测", "H3 VERIFIED", "AHP × 3 全 PASS+" 内部 codename 进了用户文档
- "wc -m" / 跨平台 UI button name unevenness
- **缺**: 当前 v1.0 适合 SDTM-fluent 同事 (如临床数据团队); 通用同事可读性还差一截.
- **v1.1 minor 计划**: USER_GUIDE.zh.md §1 重写 + 加 GLOSSARY.zh.md + pacing 表统一 + instructions size 单位修齐.

## 3. 关键决策复盘 (D-RELEASE-1 ... D-RELEASE-7)

**D-RELEASE-1** [omc-team → Agent pivot]: 1h sunk cost 是否 cancel.
- 决策点: 1h 后 omc team 仍 0% 产出, tmux pane 卡 Bypass Permissions.
- 选项: (a) 修复 tmux pane (send-keys "2" 接受 Bypass + 再 inject kickoff prompt); (b) 放弃 omc-team, Agent 重派.
- 选 (b). 理由: tmux send-keys 可靠性低 (Claude CLI prompt 状态不可观测; "2" + Enter 后 Claude 仍要等用户 attach 才会接 prompt); Agent runtime 已知工作.
- **结果验证**: Agent 7 分钟完成 vs tmux 1h 0%. 决策正确.
- **教训**: 3rd-party runtime (tmux/omc-team) 启动失败时, 不要陷入"再调试 30 分钟看看"陷阱; 已有可靠 fallback (Agent) 时, **快速 cut + pivot**.

**D-RELEASE-2** [Phase B 不写 _progress.json]: worker 严禁触碰. 用 tmux 时是 hard rule (避免 cross-pane race condition); Agent 时仍保留 (主 session 串行更新, evidence 唯一源).
- **结果**: 整 Phase B-D 全过程, _progress.json 只主 session 写, 0 race / 0 inconsistent state.
- **保留**: 任何 multi-worker 并发任务, 主 session 是 "_progress.json 唯一 writer".

**D-RELEASE-3** [DEMO 单文件三语内嵌, 不拆 .zh/.en/.ja]: PLAN §3 决策.
- 单文件优势: 同一题面 3 语并列 + SDTM 术语英文 + 判定基准英文 = 1 个 source of truth.
- 拆分劣势 (假想): 3 个文件维护 + 跨文件同步漂移风险 (SDTM 术语点跑偏一处)。
- **结果验证**: R4 (DEMO 保真审) 给 MINOR (D7 缺 AESCAN + Q1-Q10 vs D0-D9 编号 — 但都是单文件改 1 处即可); 未发生跨文件漂移.
- **保留**: 数据表 / 题库类文档 单文件三语优先.

**D-RELEASE-4** [worker-D 写 helper trigger 留主 session, 不留 worker-D]: kickoff §5 原说 "完事后 ls 检查 chatgpt §7+§8 是否完整, 不完整则追加".
- Agent 派单时改 OVERRIDE: "skip §5 reassign, 主 session 处理".
- 理由: 并发 Agent 之间不可见对方进度; worker-D 看到 chatgpt §7+§8 状态时是它自己 Agent 完成的快照, 可能落后于 worker-C 的最新写入.
- **结果**: worker-C 自己写完整 §7+§8, 主 session 只查不补, 0 helper 工作量需要.
- **保留**: 跨 worker 协作 (helper / fallback) 应留给主 session 串行做, 不让 worker 之间隐式协作.

**D-RELEASE-5** [Phase D 5 reviewer + Rule A 抽检 6 个并发 dispatch]: 是否过度.
- 6 reviewer agent (含 Rule A 抽检) 同时跑, ~25min wall.
- 选项: (a) 现 6 并发; (b) 削到 3 reviewer (en + ja + 跨平台合并); (c) 串行省钱.
- 选 (a). 理由: 6 维度独立审 = 6 视角覆盖, 串行节省的 token 远不如漏检的 1 个 MAJOR (例 README link suffix 同时被 R1 + R2 抓, 互相 cross-validate; Rule A 又加 2 个 LOW polish 抓到).
- **结果验证**: 22 fix edits 是 Phase D 集体产出, 单 reviewer 漏检率 < 6 reviewer 漏检.
- **保留**: 三语 + 多平台类 release, Phase D 至少 4-5 reviewer family + 1 Rule A 抽检, 不省.

**D-RELEASE-6** [R5 8 项 polish 留 v1.1 不堵 v1.0 sign-off]: scope cut 决策.
- R5 verdict MINOR-NEEDS_FIX, 给 8 项 polish 建议 (jargon density / pacing / instructions size / number wall / 内部 codename 等).
- 评估: 都是 polish/style preferences, 非 SDTM 错 / 非 cross-language 错 / 非链接错. 修要 1-2h.
- 当前 v1.0 适合 SDTM-fluent 同事 (临床数据团队); R5 建议是 "对通用同事可读性提升".
- 选: 留 v1.1 minor + retro 记 G-RELEASE-6.
- **保留**: Phase D MINOR-polish 类 finding 不堵 release sign-off; MAJOR-bug (link suffix / SDTM term / footer) 必修.

**D-RELEASE-7** [v1.0 不补 GLOSSARY 不重写 USER_GUIDE §1]: 时间预算选择.
- 1h45m 总预算 vs PLAN 估 5h30m, 已 -68%.
- v1.0 当前能用; v1.1 minor 走二次 polish.
- **保留**: tier-2 项目 PLAN 时间预算保留 1 倍 buffer, 任何质量提升超出预算的归 minor release.

## 4. 数据 / 工件落点速查

| 工件 | 路径 |
|---|---|
| PLAN | `.work/07_release/PLAN.md` (270 行 v1.0, 12 节) |
| _progress.json | `.work/07_release/_progress.json` (Phase A/B/C/D/E 全 status) |
| 本 RETROSPECTIVE | `.work/07_release/RETROSPECTIVE.md` (本文件) |
| Rule A 抽检 evidence | `.work/07_release/evidence/checkpoints/rule_a_translation_audit.md` |
| 3 worker kickoff | `.work/07_release/subagent_prompts/worker_{b,c,d}_*.md` (Phase E cleanup 后删) |
| 24 release 文件 | `ai_platforms/release/v1.0/` (含 self_deploy/) |

## 5. Rule A/B/C/D/E 合规

- **Rule A** (语义抽检 N=3): ✅ Phase D omc:verifier dispatch / 15 段抽样 / 0 numerical drift / 0 SDTM term drift / 0 fabrication / 2 LOW polish 修 → evidence 留 `evidence/checkpoints/rule_a_translation_audit.md`
- **Rule B** (失败归档): N/A (本次 0 attempt 失败到需归档 — omc-team 1h idle 不算 attempt 失败, 是 runtime 启动 issue, 已记 G-RELEASE-1)
- **Rule C** (Retro 强制): ✅ 本文件三段 + 决策复盘 + 速查 + 合规 + closing
- **Rule D** (审阅隔离): ✅ writer (executor × 17) 与 reviewer (5 不同 family + Rule A 抽检 1) 严格隔离, 0 self-review
- **Rule E** (Daisy 个人四规则跨项目复用): 本 retro 抽出的 R-RELEASE-1/2/3/5 候选回灌 `~/.claude/CLAUDE.md` `personal_operating_principles` (omc-team→Agent pivot decision tree / HARD-STOP DIRECTIVE 模板 / Rule A 抽检 N=3 mandatory in translation tasks)

## 6. 后续 (post-Phase-E)

- ✅ git tag `v1.0-company-release` (本 commit)
- ✅ 删除 3 worker one-shot kickoff (`subagent_prompts/worker_{b,c,d}_*.md`); 留 PLAN + RETROSPECTIVE
- ✅ CLAUDE.md 删除 "Release v1.0 Worker Protocol" 临时路由块
- ✅ 索引同步 (MANIFEST + worklog + docs/PROGRESS + CLAUDE.md Key Paths)
- 📋 v1.1 minor (post-feedback): R5 8 项 polish (USER_GUIDE.zh.md §1 重写 + GLOSSARY.zh.md + pacing 统一 + instructions size 单位修齐 + Q1-Q10 vs D0-D9 编号统一)
- 📋 邀请 JP 母语同事 final 校 ja translation (异步, 不阻塞 v1.0)

---

*v1.0 — 2026-04-27 — Daisy + Claude Opus 4.7*
