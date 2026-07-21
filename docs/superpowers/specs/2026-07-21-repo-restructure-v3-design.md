# Repo Restructure v3 — branches → milestones + sdtm-rag 提升 (设计)

> 日期: 2026-07-21
> 状态: 用户批准 (6 节设计 2026-07-21 逐节确认无异议)
> Tier: **2** (`.work/09_repo_refactor_v3/` 走 PLAN + _progress.json + evidence/ + RETROSPECTIVE)
> 前史: refactor v1 (2026-05-06~11, branches/ 命名由来) · refactor v2 (2026-05-11, release/ 提顶层, `docs/REPO_REFACTOR.md`)

## 0. 动机

- `branches/` 是 v1 的命名遗留 ("旁枝" 语义, 用户当时走默认未辩论), 与 git branch 撞名, 且语义已不符现实: 每个子目录实际是**项目的阶段性成果** (06 深审 CLOSED / jp 交付 CLOSED), 唯一活跃开发线 sdtm-rag 埋在 `branches/07_rag_kg/sdtm-rag/` 三层深处。
- 开发过程残留大量垃圾: 磁盘 ~460MB untracked 垃圾 + ~93MB tracked 冗余 + .git 146M 从未 gc (13676 全松散对象)。
- 目标: 结构反映 "活跃 vs 成果" 二分, 方便后续开发与维护; 顺手清垃圾。

## 1. 用户决策记录 (2026-07-21, 全部已确认)

| # | 决策点 | 用户选择 |
|---|--------|----------|
| D1 | 组织原则 | **活跃 vs 成果二分**: sdtm-rag 提顶层, 收官成果统一进 `milestones/` |
| D2 | 历史容器 | `.work/` 不动; `archive/` 并入 `milestones/archive/` |
| D3 | release/ 去向 | **进 milestones/**, 同步改 web 配置 + CF Pages (接受活网站改动面) |
| D4 | tracked 冗余 | **四类全删** (git rm): 06 的 15×.bak ~40M / `.work/07_release_v1_3/backups/` 26M / eval 已收口旧 run ~10M / 顶层 sharp 工具链 17M |
| D5 | jp_delivery git 保护 | **取消 ignore, 全部收进 git** (10M 含 9M 交付 zip), 先在原位收编再迁移 |

设计内定 (呈现时已提示, 用户无异议):
- parent-chain ×8 选**机械改深度** (最小 diff 行为等价), 不做单点收敛重构 (留 backlog)。
- eval 旧 run 删除**逐文件清单在 PLAN 中列出, 执行前用户复核**。

## 2. 目标结构

```
sdtm-pedia/
├── knowledge_base/       # 核心产出 (不动)
├── sdtm-rag/             # ★ 活跃开发线 (← branches/07_rag_kg/sdtm-rag, 深度 3→1)
├── web/                  # 网站 (位置不动)
├── milestones/           # 已收官的阶段性成果 (只读)
│   ├── 06_deep_verification/   # ← branches/06_deep_verification
│   ├── 07_rag_kg/              # ← branches/07_rag_kg 剩余文档层 (代码已提升走)
│   ├── jp_delivery/            # ← branches/jp_delivery (先收进 git 再迁)
│   ├── ai_platforms/           # ← ai_platforms/
│   ├── release/                # ← release/ (web 配置同步改)
│   └── archive/                # ← archive/
├── source/  docs/  .work/  tools/     # 全部不动
└── README·README_CN·CLAUDE.md·METHODOLOGY·LICENSE·DISCLAIMER·.nvmrc·.gitignore·.mcp.json
```

顶层目录 14 → 9; `branches/` 消失; 日常开发只碰 `sdtm-rag/`。

## 3. 迁移策略 — 六段时序, 每段独立 commit 可单独 revert

继承 v1/v2 方法论: git mv 保历史 · path_migration 枚举表 + sed 前先 grep 全量变体 (尾斜杠/括号/引号/.gitignore 行) · 双向 grep 校验 · **全程绝不 git stash** (v2 翻车教训) · 备份用 tag 不用 cp (v1 教训)。

| 段 | 内容 | 关键点 |
|---|---|---|
| 0 预备 | commit 在途 3 个 kg_viewer 修复文件; `git gc`; 打 tag `pre-restructure-v3` | 脏工作树清零后才动结构 |
| 1 磁盘垃圾 | 删全部 untracked 垃圾 (§4 上半, ~460MB) | chroma_backup 删前验证现役 chroma 健康 (`/api/ask` 真答一题) |
| 2 tracked 垃圾 | git rm D4 四类 (§4 下半, ~93MB 工作树) | 只删工作树, git 历史保留; 不做 history rewrite |
| 3 大迁移 | `launchctl bootout` api+ui → jp_delivery 原位 git add 收编 → 全部 git mv → rmdir branches | jp 先入 git 再搬, 全程有 git 保护; neo4j 服务不动 |
| 4 代码/配置修复 | §5 全部修复点 | venv 删旧重建 (`uv sync`), 不搬 |
| 5 文档/索引同步 | §6 active 清单; historical 不改 | memory 文件在 ~/.claude 下, 单独处理 |
| 6 验证收尾 | §7 验证矩阵 + RETROSPECTIVE | 顺手销 08_repo_refactor_v2 awaiting_user_ack 旧账 |

## 4. 清理清单

### 磁盘垃圾 (untracked, 直接删, ~460MB)
- `sdtm-rag/.mypy_cache` 86M · `.pytest_cache` · `.ruff_cache` · `__pycache__`×7 · `sdtm_rag.egg-info`
- `data/chroma_backup_20260608T104724Z` 93M + `chroma_backup_20260608T105002Z` 184K (删前验证现役库)
- `.omx/` 15M (最后活动 2026-06-01, 已废弃; 现役是 `.omc/`)
- 游离状态目录: `knowledge_base/.omc/` · `release/v1.0/.omc/` · 各 branches 内 `.omc/`
- `web/dist` 69M + `web/dist-bundles` 4.3M + `web/.astro` (可重建)
- 18× `.DS_Store`
- 顶层 `node_modules/` 17M + 磁盘上的 `package-lock.json` (sharp 一次性工具, 2026-04-27 后无引用)

### tracked 冗余 (git rm, D4 批准, ~93MB 工作树)
- `branches/06_deep_verification/` 下 15 个 `.bak` (~40M): 根级 9 个大 bak + evidence/checkpoints 4 个 + `_backups/in_flight/` 2 个
- `.work/07_release_v1_3/backups/` (26M, 75 文件)
- eval 已收口旧 run 输出 (~10M): **原则 = 已有 checkpoint 固化结论的 6 月旧 run (ablation_t1/ + 早期 prod_wirein 大份); 7 月 agg_*/kgval_* 保留; 逐文件清单在 PLAN 列出, 用户复核后执行**
- 根 `package.json` (仅含 sharp devDependency, 整个删除; `.nvmrc` 保留 — CF Pages 构建读取)

### 不动
`source/` 24M (唯一源文件, ignored) · 现役 `data/chroma` 93M · `web/node_modules` 529M (CF/本地构建在用) · `.venv` (段 4 重建非清理)

### 附带
`git gc` (段 0): .git 146M 全松散 + 8 个 garbage tmp_obj, 从未 repack, 预计大幅压缩。

## 5. 代码与配置修复面 (调研摸清的全部破坏点)

### A 级 — 服务停摆 (顺序锁死)
1. `launchctl bootout gui/$UID/com.sdtmrag.{api,ui}` (neo4j 无仓库路径, 不动)
2. git mv 迁移
3. 旧 `.venv` 删除, 新位置 `uv sync` 重建 (shebang 全是绝对路径, 搬了必坏)
4. 重写 2 个 plist (`~/Library/LaunchAgents/com.sdtmrag.{api,ui}.plist`) 各 4 处路径: ProgramArguments[0] / WorkingDirectory / StandardOut+ErrPath
5. `launchctl bootstrap` 重载, 验活 8000/8501。预计停机 <30 分钟。

### 代码 (深度 3→1, 全部机械改 parent 计数)
| 文件 | 现状 |
|---|---|
| `server/config.py:15` | `_SDTM_RAG_ROOT.parent.parent.parent` → `.parent` |
| `scripts/ingest.py:35` | 同上 |
| `scripts/build_meta.py:248` · `scripts/reconcile_meta.py:133` · `scripts/mine_implicit_relations.py:14` | `parents[4]` → `parents[2]` |
| `eval/validation_scenarios.py:26` · `eval/error_test_set.py:24` · `scripts/chunkers/_smoke_batch_b.py:28` | `5×.parent` → `3×.parent` |
| `eval/prod_wirein/judge_workflow.js:11` · `judge_workflow_v2.js:10` | 硬编码绝对路径改新路径 |

⚠️ parent-chain 错了**不 crash, 静默指空** — 验证必须实测 (§7), 不能只看服务活。

### web / CF Pages (D3)
- `web/src/content.config.ts`: `../release/v1.4` → `../milestones/release/v1.4`
- `web/scripts/build-bundles.sh`: SRC_ROOT 同步
- 本地 `npm run build` 验证后 push; CF dashboard build watch paths 手动同步 (release 已冻结不再变, 影响极小)

### 其余
- `.gitignore` ×4 (根/web/07_rag_kg/sdtm-rag): 路径规则按新布局重写; jp_delivery 规则删除 (D5); legacy 死规则 (markdown/, reports/) 清掉; 07_rag_kg/.gitignore 随代码搬走后按新布局合并/裁撤
- `tools/build_release.sh` 行 53/70: jp_delivery + release 新路径
- `tools/git-hooks/pre-commit` 正则 `^release/` → `^milestones/release/`
- `sdtm-rag/deploy/README.md` runbook 的 cd 指令 (deploy 模板指向仓库外 ~/sdtm-rag-service 是刻意设计, **不改**)

## 6. 文档/索引同步 — active vs historical 二分

### 改 (active)
- `CLAUDE.md`: Key Paths 全表 + §06 段 + Session Startup
- `README.md` + `README_CN.md`: Project Structure 段成对同步 (顺手修 "release 在 ai_platforms 下" 的陈旧描述)
- `METHODOLOGY.md`: 对外公开, 含真实超链接, 漏改即 404
- `docs/PROGRESS.md`: 路径更新 + **顺手重切 84K 单行巨段** (已违反自己 "轻量看板" 定位; 细节迁 worklog)
- `.work/AGENT_GUIDE.md` · `.work/MANIFEST.md` (Chain 07_RAG 定义 + 目录树 + Quick Ref) · `.work/meta/worklog/INDEX.md`
- `docs/superpowers/` 活 spec/plan 中的路径引用
- `docs/DESIGN_RAG_KG.md` 等 active docs 中 branches/ 引用
- **memory ×2** (`~/.claude/.../memory/project_kg_decision.md` + `project_local_deploy_plan.md`): 7 处路径指针, 仓库 grep 会漏, 单列步骤

### 不改 (historical, 保留旧路径原貌)
`release/v1.x` 内部 · jp_delivery 内部 ~30 md · `.work/07_release*` evidence · `.work/refactor_v1/` · worklog 正文 (append-only) · closed checkpoint/kickoff/handoff。
在 MANIFEST 加注记: "2026-07-21 布局变更 (repo restructure v3), 历史文档中 `branches/`、顶层 `ai_platforms/`、`release/`、`archive/` 为旧布局"。

## 7. 验证矩阵 (全过才算段 6 PASS)

1. 服务: 8000/8501/7474 全活 + `/api/ask` 真答一题接地 sources
2. pytest 全量 (sdtm-rag 521+) 零回归
3. **路径实测**: `build_meta.py` dry-run 或 reconcile 锚点跑通 (证 parent-chain 指对 knowledge_base), ingest `--dry-run` 或等价探针
4. web: 本地 `npm run build` 成功; push 后 CF 线上构建绿, prod 站点正常
5. 双向 grep: 旧路径 (`branches/`, 顶层 `ai_platforms/`, `^release/`, `archive/`) 在 active 文件 0 残留; 新路径可达
6. 独立 subagent dry-run 走查 (Rule D 精神): 模拟新 session 按 CLAUDE.md 启动清单找到全部入口
7. `git status` 干净, 每段 commit 语义清晰, tag `pre-restructure-v3` 在
8. RETROSPECTIVE.md (Rule C 三段) + 三套索引收尾 + 销 08 旧账

## 8. 范围外 (明确不做)

- git history rewrite (缩 .git 中的历史大文件) — 与 tag `v1.4-company-release` 冲突, 不做
- parent-chain 单点收敛重构 (config.py 统一 repo-root 发现) — 留 backlog
- `web/node_modules` 529M 清理 — 构建在用
- release/ 五版 self_deploy 去重 (~100M tracked) — 冻结承诺, 不动内容
- knowledge_base 296/64 vs README 293/63 口径差 — 顺手核对可, 修正属内容工作非结构工作
- sdtm-rag 内部结构调整 — 本次只搬位置不动内部

## 9. 风险与对策

| 风险 | 对策 |
|---|---|
| jp_delivery 0 git 保护, mv 出错即永久丢失 | 段 3 先原位 git add + commit 收编, 再 git mv |
| parent-chain 静默指空 | §7.3 强制实测, 不依赖服务存活判断 |
| KeepAlive 服务在旧路径无限重启 | 段 3 第一步 bootout, 段 4 末 bootstrap |
| sed 变体漏改 (v1 翻过车) | 枚举表 + sed 前 grep -rn 全量浏览变体 |
| .gitignore 规则失配把大件收进 git | 段 3/4 同 commit 改 .gitignore, git status 复核后再 commit |
| 冻结历史被误改 | active/historical 二分清单写进 PLAN, sed 只对 active 清单跑 |
| CF Pages 构建挂 | 已部署版本继续 serve 不受影响; 本地 build 先验再 push |
| 在途改动被吞 | 段 0 先 commit 清零; 全程禁 stash |
