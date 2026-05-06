<!-- chain: REFACTOR-v1
  修改本文件后, 必须检查:
  → _progress.json                  (本重构进度)
  → path_migration.md               (Phase C 路径迁移枚举)
  → ../MANIFEST.md                  (Phase B 起再写)
  → ../meta/worklog.md              (重构每段 close 时 append)
  → /CLAUDE.md                      (Phase D/E/C 都会改)
-->

# 项目重构 v1 — 完整 PLAN

> 创建: 2026-05-06
> 触发: Bojiang 反映 "agent 检索/更新/规划越来越费力", 主 session 扫描确认项目体量已到必须重构节点
> Tier: **3** (路径迁移涉及 70+ kickoff、CLAUDE.md 路由词、3 套索引体系；高 stakes — 改错会让 06 multi-session agent 整批找不到 kickoff)
> 工时估算: 段 1 ~2h / 段 2 ~半天 / 段 3 ~1 天 / 总收尾 retro ~1h
> 关联约束: CLAUDE.md "CLAUDE.md 写作规则" + 规则 A/B/C/D + workflow-tier3.md

---

## §0 为什么要现在重构

实测数据 (扫描日 2026-05-06):

| 指标 | 实测 | 警戒 | 状态 |
|------|------|------|------|
| `.work/06_deep_verification/` | **115MB / 980 文件** | 单 phase >50MB 即异常 | 🔴 占整个 .work/ ~97% 体积 |
| `.bak` 文件总量 | **76 个 / 84MB** | git 已存, 不应再快照 | 🔴 |
| `.work/06` 顶层散落 .bak | **17 个** | 应在子目录 | 🔴 |
| `multi_session/` kickoff 累积 | **72 个** (round 2-14 + B-01/02/03/03c) | 无 archive 边界 | 🟡 |
| `worklog.md` | **2,449 行** | 单文件 >800 行该拆 | 🔴 |
| `MANIFEST.md` header 单句 | **~2KB 一句话** | <200 字符 | 🔴 |
| 三套索引 (MANIFEST/worklog/PROGRESS) | 内容 ~50% 重叠 | 收尾要同步 3 处 | 🔴 |
| 顶层"知识库"语义混乱 | knowledge_base/ + project_knowledge_base/ + web/ | agent 看不懂哪个是真 | 🟡 |
| 顶层 `evidence/` | **0B 空目录** | 应删 | 🔴 |
| CLAUDE.md | 120 行 | 150 上限 | 🟢 |

**结论**: 重构是必须的, 但不能裸跑 — 涉及路由词改动会让正在跑的 06 multi-session 直接断链, 必须时序化分段, PLAN 先行.

---

## §1 目标态 (重构后形态)

```
SDTM-compare/
├── CLAUDE.md                      # ≤150 行, 顶部加 AGENT_GUIDE 指针
├── README.md / README_CN.md
├── METHODOLOGY.md
├── DISCLAIMER.md / LICENSE
├── knowledge_base/                # 唯一英文 KB (已是当前形态)
├── web/                           # 站点产物 (Phase 7), 进 Key Paths
├── source/                        # PDF + xlsx 原始
├── docs/                          # 主项目文档 (jp/ 旁枝迁出)
├── ai_platforms/                  # 双平台部署旁枝 (保持现状)
├── archive/                       # 新增: 已搁置/历史产物归档
│   └── old_knowledge_base_v0/     # 原 project_knowledge_base/
├── branches/                      # 新增: 独立旁枝 (Phase C 后)
│   ├── 06_deep_verification/      # 原 .work/06_deep_verification/
│   └── jp_delivery/               # 原 docs/jp/
└── .work/
    ├── AGENT_GUIDE.md             # 新增: 一页纸 agent 进入指引
    ├── MANIFEST.md                # 瘦身: 纯结构清单, 不含状态
    ├── 00-04, 07/                 # 各 phase 工作区 (现状)
    ├── 05_rag_kg/                 # 已搁置, 显式标注
    └── meta/
        ├── worklog/               # 拆分: 按 phase 一文件
        │   ├── INDEX.md           # 引导
        │   ├── phase01_generation.md
        │   ├── phase02_indexing.md
        │   ├── ...
        │   └── phase06_deep_verification.md  (指针到 branches/)
        └── retrospective.md
```

**索引职责重划** (Phase B 核心):

| 文件 | 职责 (重构后) | 不应包含 |
|------|---------------|----------|
| `.work/AGENT_GUIDE.md` | 新 session agent 第 1 个读, 一页纸告诉去哪找什么 | 状态、历史 |
| `.work/MANIFEST.md` | 文件结构 + 变更链 + Key Paths 指针 | 任何 round/batch/version 状态描述 |
| `.work/meta/worklog/*` | 按 phase 拆分的执行日志 (append-only) | 当前状态 (那是 _progress.json 的) |
| `docs/PROGRESS.md` | **唯一**的"当前进度看板", 一目了然各 phase 状态 | 历史细节 |
| 各 phase `_progress.json` | 程序化进度 (现状, 不动) | — |

---

## §2 三段时序总览

| 段 | 触发条件 | 内容 | 工时 | 风险 |
|----|----------|------|------|------|
| **1** | **现在 (这个 session)** | D + E + A 零冲突部分 + 段 2/3 PLAN 落地 | ~2h | 低 (不动 06 / 不动索引) |
| **2** | **06 round 04 全部 close** (你那个终端 reconciler PASS, 但 round 05 未 kickoff 之前) | A .bak 整理 + B 索引去重 | ~半天 | 中 (改 MANIFEST/worklog/PROGRESS, 与 06 收尾抢同一行) |
| **3** | **整个 P2 B-03c 大 cycle 全部 close** (你判断, 可能再几个 round 后) | C 旁枝迁移 + 收尾 retro | ~1 天 | 高 (路由词 + 70+ kickoff 路径) |

---

## §3 段 1 详细步骤 (现在可执行)

### 3.1 D — `project_knowledge_base/` 归档 + `web/` 进 Key Paths

**前提**: Bojiang 已确认 (本对话 2026-05-06): "之前做过的一版, 作为参考, 没啥用了"; web/ 是说明书 + 展示界面.

**步骤** (可勾选):
- [ ] D-1 `mkdir -p archive/`
- [ ] D-2 `git mv project_knowledge_base archive/old_knowledge_base_v0`
- [ ] D-3 写 `archive/README.md`: 一句话说明 archive/ 用途 + old_knowledge_base_v0 是什么 (历史参考版, 已被 knowledge_base/ 取代)
- [ ] D-4 编辑 `CLAUDE.md` Key Paths 表:
  - 加入 `Web 站点 (Phase 7 产物) | web/`
  - 加入 `归档 (历史参考) | archive/`
- [ ] D-5 编辑 `.gitignore` 确认 `web/node_modules/` `web/dist*/` `web/test-results/` 都在内 (避免 579MB 大头进 git)
- [ ] D-6 验收: `du -sh archive/ web/ knowledge_base/` 各自合理; `grep -c "project_knowledge_base" CLAUDE.md README*.md` 应为 0 (或仅历史 reference)

**回滚**: `git mv archive/old_knowledge_base_v0 project_knowledge_base && git checkout CLAUDE.md`

### 3.2 E — 写 `.work/AGENT_GUIDE.md`

**目标**: 一页纸 (≤80 行), 让新 session agent 第 1 个读, 立刻知道:
- 找当前状态去哪 (→ docs/PROGRESS.md + 各 phase _progress.json)
- 找历史去哪 (→ .work/meta/worklog/)
- 找规则去哪 (→ CLAUDE.md + .work/meta/retrospective.md)
- 找 PDF/MD 产物去哪 (→ source/ + knowledge_base/)
- 找站点去哪 (→ web/)
- 各 phase 入口一行表

**步骤**:
- [ ] E-1 草稿写在 `.work/AGENT_GUIDE.md`
- [ ] E-2 CLAUDE.md "Session Startup" 段顶部加一行: `0. .work/AGENT_GUIDE.md — 一页纸进入指引 (优先读)`
- [ ] E-3 用 1 个 explore subagent 模拟"新 session 第一次进项目", 验证读 AGENT_GUIDE 后能不能定位"06 当前状态"+"知识库主文件"+"修复任意 issue 流程" — 写到 evidence/checkpoints/E_dryrun.md

**回滚**: `git rm .work/AGENT_GUIDE.md && git checkout CLAUDE.md`

### 3.3 A 零冲突部分

- [ ] A-1 删空目录: `rmdir evidence/` (顶层 0B 那个; 注意不要碰 `.work/06_deep_verification/evidence/`)
- [ ] A-2 `tmp/pdfs/` 处置: 看 §5 决策点 #2; 若决议归档 → `git mv tmp archive/old_tmp_pdfs/` + 写 README; 若决议删 → `git rm -r tmp/`
- [ ] A-3 `progress.txt` 处置: 这是 reconciler round 4 session log, 应迁到 `.work/06_deep_verification/evidence/checkpoints/reconciler_round4_session_log.md` (改名 .md, 更语义)
- [ ] A-4 `notes/` 处置: 看 §5 决策点 #3; 默认保留, 但 Key Paths 加一行
- [ ] A-5 验收: `ls -la` 顶层应只剩明确入口; `git status` 干净

### 3.4 段 1 收尾

- [ ] S1-close-1 commit: `refactor v1 段 1 — D 清 project_knowledge_base + E AGENT_GUIDE + A 零冲突清污`
- [ ] S1-close-2 更新本 PLAN _progress.json: `phase_1_status: closed`
- [ ] S1-close-3 写 `evidence/checkpoints/段1_完成报告.md` (规则 A: 抽检 D-2 git mv 后 archive/ 内文件数 = 原 project_knowledge_base/ 文件数)

---

## §4 段 2 详细步骤 (round 04 close 后执行)

> **触发**: 你在另一个终端跑完 round 04 (含 reconciler PASS), 在 round 05 kickoff **之前**, 来这个 session 说 "执行段 2".
> **预期间隔**: 几小时到 1-2 天 (round 03 = 12 batches/741 atoms 作参考).

### 4.1 A 余 — `.bak` 整理

**当前 .bak 分布** (扫描时):
- `.work/06_deep_verification/` 顶层: 17 个 (主要是 pdf_atoms.jsonl 14 个版本快照 + audit_matrix + _progress)
- 全项目其他位置: 76 - 17 = 59 个

**策略** (规则 B "失败归档不删" 的正确解读):
- 真正的 "failed attempt" → 留在 `failures/` (规则 B 字面要求)
- "round 之间的 cycle 边界全量快照" → git 已存, 不需要再保留 .bak 文件
- 决策: 已 close 的 round/batch 的 pre-XX.bak 一律 `git rm` (用 git history 取代); 当前 in-flight (round 04) 之前 1 个 .bak 保留作即时回滚

**步骤**:
- [ ] A-6 列出 `.work/06_deep_verification/*.bak`, 区分 "round close 之前" vs "in-flight 即时回滚"
- [ ] A-7 `mkdir .work/06_deep_verification/_backups/in_flight/` (留 in-flight 用)
- [ ] A-8 已 close 的 `git rm` (审计 commit history 确认能回查); in-flight 移到 `_backups/in_flight/`
- [ ] A-9 全项目其他 .bak 同样审计 (尤其 pdf_atoms.jsonl.pre-multi-XX.bak 这种 round 8-10 的, 全部 git rm)
- [ ] A-10 验收: `find . -name "*.bak" | wc -l` 从 76 降到 ≤5 (in-flight 容量)

**回滚**: `git revert <commit>`; .bak 在 git history 里都还在.

### 4.2 B — 索引去重

#### 4.2.1 MANIFEST.md 瘦身

- [ ] B-1 备份: `cp .work/MANIFEST.md .work/refactor_v1/evidence/checkpoints/MANIFEST_pre_B.md`
- [ ] B-2 重写 header: 删掉 ~2KB 那一句长状态; "最后更新" 字段只写 ISO 日期, 不塞内容
- [ ] B-3 删除任何 round/batch/version 状态描述 (按 CLAUDE.md "不要写" 规则); 这些去 worklog
- [ ] B-4 重写后行数应 ≤200 (现 357)
- [ ] B-5 收尾: `wc -l MANIFEST.md` < 200; `grep -E "round [0-9]+|batch [0-9]+|v1\.[0-9]" MANIFEST.md | wc -l` 应为 0 或仅极少 (链定义里的 chain 名称除外)

#### 4.2.2 worklog.md 拆分

- [ ] B-6 备份: `cp .work/meta/worklog.md .work/refactor_v1/evidence/checkpoints/worklog_pre_B.md`
- [ ] B-7 `mkdir .work/meta/worklog/`
- [ ] B-8 按 phase 拆: 用 grep 找 "## Phase N" 标题切分到独立文件
  - `phase00_planning.md` / `phase01_generation.md` / `phase02_indexing.md` / `phase03_verification.md` / `phase04_optimization.md` / `phase05_rag_kg.md` / `phase06_deep_verification.md` / `phase07_release.md` / `phase07_website.md` / `phase65_ai_platforms.md` / `meta_xxx.md`
- [ ] B-9 写 `worklog/INDEX.md`: 一行一文件链接 + 每文件最新 entry 日期
- [ ] B-10 把原 `.work/meta/worklog.md` 改成 1 行: `本文件已拆分, 见 .work/meta/worklog/INDEX.md`; 或直接 `git rm` (Bojiang 决策, 见 §5)
- [ ] B-11 验收: 每个 phase 文件 ≤500 行; INDEX.md 准确

#### 4.2.3 docs/PROGRESS.md 改成"唯一状态板"

- [ ] B-12 重写: 只列各 phase 的 "状态 / 当前活动 / 下一步", 不写历史细节
- [ ] B-13 重写后 ≤150 行 (现 339)

#### 4.2.4 CLAUDE.md Chain B 更新

- [ ] B-14 编辑 CLAUDE.md "Session Wrap-up" 段, 反映新的三套索引职责; 删掉重复同步的指示

### 4.3 段 2 收尾

- [ ] S2-close-1 commit: `refactor v1 段 2 — A bak 整理 + B 索引去重`
- [ ] S2-close-2 _progress.json: `phase_2_status: closed`
- [ ] S2-close-3 写 `evidence/checkpoints/段2_完成报告.md` + 规则 A 抽检: 拆分后 worklog 总行数 应 ≈ 原 2449 行 (允许 ±5% 误差是 INDEX 元数据)

---

## §5 段 3 详细步骤 (大 cycle close 后执行)

> **触发**: 你判断 P2 B-03c 整个大 cycle 收官 (可能再 N 个 round, 你说了算), 来这个 session 说 "执行段 3".
> **重点**: 段 3 必须**先**做 path migration dry-run, 确认 70+ kickoff 文件路径全部更新无遗漏, 才能执行实搬.

### 5.1 C — 旁枝迁移到 `branches/`

#### 5.1.1 准备

- [ ] C-1 完整阅读 `path_migration.md` (本 PLAN 同目录), 它枚举了所有需要更新引用的文件
- [ ] C-2 全量备份: `cp -r .work/06_deep_verification .work/refactor_v1/evidence/checkpoints/06_pre_C/`
- [ ] C-3 `mkdir branches/`

#### 5.1.2 06 搬家

- [ ] C-4 `git mv .work/06_deep_verification branches/06_deep_verification`
- [ ] C-5 按 `path_migration.md` 表 1: 更新 `branches/06_deep_verification/PLAN.md` 的 chain F 引用 (../03_verification/ → ../../.work/03_verification/, 等)
- [ ] C-6 按表 2: 更新 `branches/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` 中所有 `.work/06_deep_verification/` → `branches/06_deep_verification/` 引用
- [ ] C-7 按表 3: 更新所有 kickoff 文件 (72 个) 中的硬编码路径 — **用 sed 脚本批量, 不手改**

#### 5.1.3 docs/jp 搬家

- [ ] C-8 `git mv docs/jp branches/jp_delivery`
- [ ] C-9 更新 `branches/jp_delivery/PLAN.md` `EXECUTION_PLAN.md` `WORKLOG.md` 内部相对路径

#### 5.1.4 CLAUDE.md 路由词更新

- [ ] C-10 编辑 CLAUDE.md "## 06 Deep Verification" 段:
  - `.work/06_deep_verification/` → `branches/06_deep_verification/`
  - 路由词描述里的所有路径
- [ ] C-11 编辑 CLAUDE.md Key Paths 表对应行
- [ ] C-12 编辑 `docs/jp/` 那一行 → `branches/jp_delivery/`

#### 5.1.5 索引文件 (来自段 2) 同步更新

- [ ] C-13 `.work/MANIFEST.md` 更新结构指针
- [ ] C-14 `.work/AGENT_GUIDE.md` 更新 06 入口路径
- [ ] C-15 `.work/meta/worklog/phase06_deep_verification.md` 改为 1 行指针 → `branches/06_deep_verification/`

#### 5.1.6 Dry-run 验证

- [ ] C-16 派 1 个 explore subagent 做 dry-run: 模拟 "新 session, 收到路由词 'P2 bulk B-03c round 05 自治连跑' " (假设有 round 05), 看 agent 能不能正确定位到 `branches/06_deep_verification/multi_session/P2_B-03c_round_05_kickoff.md` (用 grep 验证不会去找老路径)
- [ ] C-17 跑 `grep -r "\.work/06_deep_verification" --include="*.md" --include="*.json" .` 应只剩 archive/历史 reference, 不应在 active 文件里出现
- [ ] C-18 反向: `grep -r "branches/06_deep_verification" --include="*.md" .` 应在 CLAUDE.md / MANIFEST.md / AGENT_GUIDE.md / 所有 multi_session/ 文件里都出现 (>= 70 hits)

### 5.2 总收尾 retro (规则 C 强制)

- [ ] R-1 写 `.work/refactor_v1/RETROSPECTIVE.md`, 至少三段:
  - **保留**: 时序化分段 (段 1/2/3) 是否有效避免了和 06 跑批的冲突
  - **缺口**: 是否有遗漏的引用 / 是否 dry-run 不够 / agent 检索是否真的变快
  - **决策复盘**: branches/ vs phases/ 命名选择 / project_knowledge_base 归档 vs 删 / .bak git rm 策略
- [ ] R-2 commit: `refactor v1 段 3 + retro CLOSED — 项目重构 v1 收官`
- [ ] R-3 _progress.json: `phase_3_status: closed`, `overall_status: closed`

---

## §6 决策点 (Bojiang 拍板, 段 1 开跑前敲定)

| # | 问题 | 选项 | 我的默认建议 |
|---|------|------|--------------|
| 1 | `project_knowledge_base/` 归档保留还是 git rm? | (a) `git mv archive/` 保留; (b) `git rm` 彻底删 (git history 仍在) | (a) 归档 — 5MB 不大, 且可能某天回查"之前做错过什么" |
| 2 | `tmp/pdfs/` 处置? | (a) 归档 archive/old_tmp_pdfs/; (b) git rm; (c) 保留并写 README | (b) git rm — 是早期实验残留, git history 留即可 |
| 3 | `notes/` 处置? | (a) 保留, Key Paths 加指针; (b) 迁到 `.work/meta/notes/`; (c) 归档 | (b) 迁到 .work/meta/notes/ — 是工作笔记类内容, 跟 retrospective 同级 |
| 4 | `worklog.md` 原文件拆分后处置? | (a) 留 1 行指针; (b) 直接 git rm | (b) git rm — 拆分后保留指针文件容易让人误读, INDEX 够用 |
| 5 | 旁枝目录命名: `branches/` 还是 `phases/`? | branches / phases / sidetrack | `branches/` — phase 已经被 .work/0N_xxx 占了语义, branches 表达"独立分支" 更准 |
| 6 | 06 子目录的 .bak 阈值: 保留多少? | 0 / 1 / 3 / 5 个 in-flight | 1 个 (最近一次, 给即时回滚) |

**段 1 启动前**: 你回这 6 个决策, 我立刻按你的回答执行. 不回就用我的默认.

---

## §7 风险 + 回滚预案

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| 段 2 改 MANIFEST 时, 你那个 06 终端正好在 round 04 收尾 | 低 (你触发) | 高 (写冲突) | 段 2 必须由你确认 round 04 reconciler PASS 之后再触发 |
| 段 3 漏改某个 kickoff 路径, 路由词无法路由 | 中 | 高 (后续 round agent 找不到 kickoff) | C-16 dry-run 必做 + C-17/C-18 双向 grep 校验 |
| 索引拆分后, 旧 commit 消息引用的路径失效 | 高 | 低 (历史可读性下降) | git history 不变, 只影响人工 ctrl-F; 可接受 |
| .bak git rm 后某次需要回滚发现 git history commit 不全 | 低 | 中 | 段 2 A-9 之前先确认每个待删 .bak 对应的 round close commit 存在; 不存在的保留 |
| project_knowledge_base 归档后被发现还有引用 | 低 | 低 | D-6 grep 校验 |

**整体回滚**: 每段独立 commit, 不满意可 `git revert <commit>` 回退一段, 不影响其他段.

---

## §8 验收标准 (整个重构 done 的判据)

- [ ] 顶层目录数 ≤12 (现 14, 删 evidence/ tmp/ project_knowledge_base/ 后)
- [ ] `.work/` 体积从 ~118MB 降到 ≤10MB (06 搬走后)
- [ ] `.bak` 文件数 ≤5
- [ ] `MANIFEST.md` ≤200 行
- [ ] 每个 worklog/phase*.md ≤500 行
- [ ] `docs/PROGRESS.md` ≤150 行
- [ ] CLAUDE.md ≤150 行 (现 120, 重构期间只增不减是问题)
- [ ] AGENT_GUIDE.md 存在且 ≤80 行
- [ ] dry-run subagent 能用 AGENT_GUIDE 在 3 步内定位任意 phase 当前状态
- [ ] RETROSPECTIVE.md 三段齐备 (规则 C)
- [ ] 段 1/2/3 各有 evidence/checkpoints/段N_完成报告.md (规则 A 抽检)

---

## §9 段 1 启动前 checklist

执行段 1 前确认:
- [ ] Bojiang 已读完本 PLAN
- [ ] Bojiang 已回 §6 六个决策点 (或同意默认)
- [ ] 当前 git working tree 干净 (除已知的 .bak 文件)
- [ ] 你那个 06 终端 round 04 任意 batch 都不在写 archive/ 或 tmp/ 或 CLAUDE.md (这些是段 1 唯一会动的)

确认后说 **"执行段 1"** 即开跑.
