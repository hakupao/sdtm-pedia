# Repo Restructure v3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
> Spec: `docs/superpowers/specs/2026-07-21-repo-restructure-v3-design.md`

**Goal:** branches/ 解散 — sdtm-rag 提升顶层, 收官成果统一进 milestones/, 清理 ~550MB 垃圾, 全部引用/服务/构建同步修复。

**Architecture:** 六段时序迁移 (预备→磁盘垃圾→tracked 垃圾→git mv 大迁移→代码配置修复→文档同步→验证), 每段独立 commit 可单独 revert。继承 refactor v1/v2 方法论: git mv 保历史 · sed 前 grep 全量变体 · active/historical 二分 · 全程禁 git stash · tag 备份。

**Tech Stack:** git / launchd / uv / sed / pytest / npm (Astro)

## Global Constraints

- 仓库根: `/Users/bojiangzhang/MyProject/sdtm-pedia` (下称 `$R`)。所有命令从 `$R` 执行, 不依赖累积 cwd。
- **全程禁 `git stash`** (v2 翻车教训)。
- 每个 Task 一个 commit (Task 内多步允许多 commit 但语义清晰)。
- historical 文件 (release/v1.x 内部 · milestones 各 CLOSED 线内部 · .work/07_* evidence · worklog 正文 · docs/superpowers 已执行 spec/plan · docs/REPO_REFACTOR.md) **一律不改路径**。
- sed 替换顺序: 最长路径先替换 (`branches/07_rag_kg/sdtm-rag` → `sdtm-rag` 必须先于 `branches/07_rag_kg` → `milestones/07_rag_kg`)。
- 执行证据落 `.work/09_repo_refactor_v3/evidence/`; 失败归档 `.work/09_repo_refactor_v3/evidence/failures/` (Rule B)。
- 服务停机窗口: Task 5 bootout → Task 8 bootstrap, 期间 8000/8501 不可用 (本机自用, 已知)。neo4j 全程不动。

---

### Task 1: 段 0 预备 — 清零工作树 + git gc + tag

**Files:**
- Commit: `branches/07_rag_kg/sdtm-rag/{kg_viewer.html, scripts/build_kg_viewer.py, scripts/tests/test_build_kg_viewer.py}` (在途 SP6 viewer 修复)
- Create: `.work/09_repo_refactor_v3/` + `_progress.json`

- [ ] **Step 1: 验证在途修复测试过** — `cd $R/branches/07_rag_kg/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q`。Expected: `6 passed`。
- [ ] **Step 2: commit 在途修复**

```bash
cd $R && git add branches/07_rag_kg/sdtm-rag/kg_viewer.html branches/07_rag_kg/sdtm-rag/scripts/build_kg_viewer.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_build_kg_viewer.py
git commit -m "fix(sp6): viewer UX — pan 不吞节点点击 / 布局收敛静止 / explore 独立种子自动展开 / 硬边优先展开"
```

- [ ] **Step 3: 确认工作树全净** — `git status --porcelain` 输出空。
- [ ] **Step 4: git gc** — `git gc` (146M 全松散对象, 首次 repack)。之后 `git count-objects -vH` Expected: in-pack > 0, loose 接近 0, size 显著小于 146M。
- [ ] **Step 5: 打预迁移 tag + 建 progress 目录**

```bash
git tag pre-restructure-v3
mkdir -p $R/.work/09_repo_refactor_v3/evidence/failures
```

`_progress.json` 初始化: `{"tier": 2, "status": "in_progress", "started": "2026-07-21", "tasks_done": []}` (每 Task 完成后追加编号)。

- [ ] **Step 6: Commit** — `git add .work/09_repo_refactor_v3 && git commit -m "chore(restructure): 段0 预备 — progress 目录 + tag pre-restructure-v3"`

### Task 2: 段 1 磁盘垃圾清理 (untracked, ~460MB, 零 git 影响)

**Files:** 只删 untracked/ignored, 不产生 git diff。

- [ ] **Step 1: chroma 健康预检** (删备份的前置门)

```bash
curl -s -X POST http://127.0.0.1:8000/api/ask -H 'Content-Type: application/json' -d '{"question":"What is the AE domain?"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print('sources:', len(d.get('sources',[])))"
```

Expected: `sources: >0`。失败则**停止, 不删 chroma_backup**, 归档 failures。

- [ ] **Step 2: 删 Python/工具缓存与废弃状态**

```bash
cd $R
rm -rf branches/07_rag_kg/sdtm-rag/.mypy_cache branches/07_rag_kg/sdtm-rag/.pytest_cache branches/07_rag_kg/sdtm-rag/.ruff_cache branches/07_rag_kg/sdtm-rag/sdtm_rag.egg-info
find . -type d -name __pycache__ -not -path "./.git/*" -not -path "*/node_modules/*" -not -path "*/.venv/*" -exec rm -rf {} +
rm -rf .omx knowledge_base/.omc release/v1.0/.omc web/.omc
find branches -type d -name ".omc" -exec rm -rf {} +
```

- [ ] **Step 3: 删 chroma 备份 + web 构建产物 + .DS_Store + 顶层 node 工具链磁盘件**

```bash
rm -rf branches/07_rag_kg/sdtm-rag/data/chroma_backup_20260608T104724Z branches/07_rag_kg/sdtm-rag/data/chroma_backup_20260608T105002Z
rm -rf web/dist web/dist-bundles web/.astro web/test-results
rm -rf node_modules package-lock.json
find . -name ".DS_Store" -not -path "./.git/*" -delete
```

- [ ] **Step 4: 验证** — `git status --porcelain` 仍为空 (全是 ignored 内容); `du -sh $R` 较之前减少 ~460MB。记录前后数字到 `evidence/step_disk_cleanup.md`。无 commit (无 git 变更, evidence 随下个 Task commit)。

### Task 3: 段 2a tracked 垃圾 git rm — .bak / release 备份 / sharp

**Files:**
- Delete (git rm): 06 的 15× .bak · `.work/07_release_v1_3/backups/` · 根 `package.json`

- [ ] **Step 1: git rm 06 的 .bak (15 个)**

```bash
cd $R && git ls-files 'branches/06_deep_verification/**/*.bak' 'branches/06_deep_verification/*.bak' | wc -l   # Expected: 15
git ls-files 'branches/06_deep_verification/**/*.bak' 'branches/06_deep_verification/*.bak' | xargs git rm -q
```

- [ ] **Step 2: git rm release_v1_3 备份 + sharp package.json**

```bash
git rm -r -q .work/07_release_v1_3/backups
git rm -q package.json
```

- [ ] **Step 3: 验证** — `git status` 只有删除项 + `ls $R/.nvmrc` 仍在 (CF Pages 需要)。
- [ ] **Step 4: Commit** — `git commit -m "chore(restructure): 段2a — git rm 06 深审 .bak×15 (~40M) + 07_release_v1_3/backups (26M) + 根 sharp 工具链 (git 历史保留可找回)"`

### Task 4: 段 2b eval 已收口旧 run git rm (逐文件清单, 用户已复核原则)

**删除线: 2026-06-20 及以前 commit 的 run 输出 (json/log/txt); 脚本 (.py/.sh/.js)、审查 md、题集资产 (kgval_authored_*/candidates/review)、6-21 kgval run、7 月 agg 全部保留。**

- [ ] **Step 1: 引用预检** — 确认无代码引用将删文件:

```bash
cd $R/branches/07_rag_kg/sdtm-rag && grep -rln "error_test_results.json\|validation_scenario_results.json\|baseline_report\|1d_report\|cmp_sonnet_v3\|ablation_t1" server/ scripts/ webchat/ ui/ --include="*.py" --include="*.js"
```

Expected: 空输出 (eval/ 自身脚本引用不算, 那些脚本只在重跑时用)。若有 server/scripts 引用则该文件移出删除清单并记录。

- [ ] **Step 2: git rm eval 根旧 run (10 个)**

```bash
cd $R/branches/07_rag_kg/sdtm-rag/eval
git rm -q baseline_report.json baseline_report_v0_full.json 1d_report_retrieval.json 1d_report_deepseek.json error_test_results.json validation_scenario_results.json cmp_sonnet_v3.json cmp_gpt4o_v3.json cmp_gpt54mini_v3.json cmp_deepseek_v3.json
```

- [ ] **Step 3: git rm ablation_t1 run 输出 (json+log, 保留 3 个 .md)**

```bash
cd $R/branches/07_rag_kg/sdtm-rag/eval/ablation_t1 && git rm -q *.json *.log
git ls-files . # Expected 只剩: review_T1.md review_rechunk.md testset_v2_audit.md
```

- [ ] **Step 4: git rm prod_wirein 6-09/6-10/6-15/6-20 的 run 输出 (json/log/txt only)**

```bash
cd $R/branches/07_rag_kg/sdtm-rag/eval/prod_wirein
git rm -q step0_levers_on.log step1_postrefactor.log step4_fix_retrieval.log step4_full_on_t0_fix.log step2_full_paired_t0.log step2_full_paired.log step0_levers_on_retrieval.json step1_postrefactor_retrieval.json step4_fix_retrieval.json forensic_answers.json forensic_answers.log step2_full_off.json step2_full_on.json step2_full_off_t0.json step2_full_on_t0.json step4_full_on_t0_fix.json step0_perq_src.json step3_latency.log
git rm -q g_on2_v2.log forensic_drops.json forensic_guardrail.json g_retrieval_sanity.json g_on_t0.json g_off_t0.json g_off2_t0.json g_on2_full.json guardrail_gate.log guardrail_paired_analysis.txt guardrail_v2_paired_analysis.txt noise_drops.log judge_bundle_v2.json
git rm -q v3_full_on_guardrail_t0.log v3_full_on_t0.log code_grounding_off.json code_grounding_on.json v3_full_off_t0.log judge_result_v3.json v3_drops_forensic.json judge_input_v3.json v3_full_paired_t0.log v3_full_off_t0.json v3_full_on_t0.json v3_full_on_guardrail_t0.json
git rm -q v3_sp2_paired_t0.log v3_sp2_off_t0.json v3_sp2_on_t0.json
```

- [ ] **Step 5: 验证保留清单完好** — `git ls-files . | sort`。Expected 仍在: 全部 `.py` (analyze_paired/bench_latency/forensic_answers/check_code_grounding/forensic_guardrail/heldout_probes/sp2p2_equiv_snapshot/analyze_kgval/kgval_fire_probe/agg_fire_probe/analyze_agg_e2e/sp3_graph_probes/sp4_isolation_probe/sp4_cookbook_golden) + `.sh`×2 + `.js`×2 + kgval_arm* 9 个 + kgval_*_run.log ×3 + kgval_analysis.json + kgval_fire.json + agg_* 全部。
- [ ] **Step 6: Commit** — `cd $R && git commit -m "chore(restructure): 段2b — git rm eval 已收口旧 run (≤2026-06-20 输出 ~9.6M); 脚本/审查md/题集/kgval/agg 保留"`

### Task 5: 段 3a 停服 + jp_delivery 原位收编

**Interfaces:** Produces: jp_delivery 全部 tracked (后续 Task 6 才能 git mv 它)。

- [ ] **Step 1: 停 api+ui 服务 (neo4j 不动)**

```bash
launchctl bootout gui/$(id -u)/com.sdtmrag.api
launchctl bootout gui/$(id -u)/com.sdtmrag.ui
curl -s -m 2 http://127.0.0.1:8000/api/health || echo "api down (expected)"
```

Expected: 最后一行输出 `api down (expected)`。

- [ ] **Step 2: 根 .gitignore 删 jp_delivery 规则** — Edit `$R/.gitignore`, 删除这两行:

```
# docs/jp deliverable パッケージ展開副本 (zip + sha256 のみ追跡; 解凍検証ディレクトリは無視)
branches/jp_delivery/
```

- [ ] **Step 3: 收编 jp_delivery 进 git**

```bash
cd $R && git add branches/jp_delivery .gitignore
git status --porcelain branches/jp_delivery | head -5   # Expected: 一批 A (added)
git ls-files branches/jp_delivery | wc -l               # Expected: >0 (原为 0)
git commit -m "chore(restructure): 段3a — jp_delivery 取消 ignore 全量收编进 git (10M 含交付 zip, 迁移前获得 git 保护)"
```

- [ ] **Step 4: 确认磁盘内容与 git 一致** — `git status --porcelain branches/jp_delivery` 输出空。

### Task 6: 段 3b 大迁移 — git mv 全部 + 根 .gitignore 重写 (同一 commit)

- [ ] **Step 1: git mv 全部迁移**

```bash
cd $R && mkdir milestones
git mv branches/07_rag_kg/sdtm-rag sdtm-rag
git mv branches/07_rag_kg milestones/07_rag_kg
git mv branches/06_deep_verification milestones/06_deep_verification
git mv branches/jp_delivery milestones/jp_delivery
git mv ai_platforms milestones/ai_platforms
git mv release milestones/release
git mv archive milestones/archive
rmdir branches   # Expected: 成功 (已空); 若非空 → ls branches 排查, 不强删
```

注意: `branches/07_rag_kg/prompts/` 是空目录 (git 不 track 空目录), rmdir branches 前若剩它则 `rmdir branches/07_rag_kg/prompts branches/07_rag_kg` 逐级清。sdtm-rag 内 ignored 的 `.venv/`、`data/chroma/`、`logs/`、`.env` 会随磁盘 mv 一起走 (git mv 对整目录操作时 untracked 内容同步移动); mv 后 `ls sdtm-rag/data/chroma` 确认在。

- [ ] **Step 2: 根 .gitignore 重写** — 完整新内容 (Write 覆盖):

```
# macOS
.DS_Store

# CDISC source files (copyrighted, not for redistribution)
source/

# Claude Code / tool state
.claude/
.omc/
.superpowers/
.playwright-mcp/

# Build output for the website's release-bundle pipeline (web/scripts/build-bundles.sh).
# Zips are uploaded to GitHub releases instead of committed.
web/dist-bundles/
```

变更说明: 删 legacy 死规则 (markdown/, reports/) · 删 /node_modules/ + /package-lock.json (工具链已除) · 删 .omx/ (已删且不会再生) · jp_delivery 规则已在 Task 5 删。`web/.gitignore`、`sdtm-rag/.gitignore` (相对路径, 随迁移仍有效)、`milestones/07_rag_kg/.gitignore` (无害) 均不动。

- [ ] **Step 3: 迁移完整性验证**

```bash
cd $R && git status --porcelain | grep -v "^R" | grep -v "^M .gitignore" | head   # Expected: 空 (全是 rename + .gitignore 修改)
ls sdtm-rag/server/main.py milestones/06_deep_verification/PLAN.md milestones/jp_delivery/PLAN.md milestones/ai_platforms/SYNC_BOARD.md milestones/release/v1.4 milestones/archive/old_knowledge_base_v0 milestones/07_rag_kg/PLAN.md   # Expected: 全部存在
git status --ignored=matching --porcelain sdtm-rag/data/chroma | head -2   # Expected: !! (仍 ignored)
```

- [ ] **Step 4: Commit** — `git add -A && git commit -m "refactor(restructure): 段3b — branches 解散: sdtm-rag 提顶层, 06/07docs/jp/ai_platforms/release/archive 进 milestones/; 根 .gitignore 重写"`

### Task 7: 段 4a sdtm-rag 代码路径修复 (深度 3→1) + pytest

**Files:**
- Modify: `sdtm-rag/server/config.py:15` · `sdtm-rag/scripts/ingest.py:35` · `sdtm-rag/scripts/build_meta.py:248` · `sdtm-rag/scripts/reconcile_meta.py:133` · `sdtm-rag/scripts/mine_implicit_relations.py:14` · `sdtm-rag/eval/validation_scenarios.py:26` · `sdtm-rag/eval/error_test_set.py:24` · `sdtm-rag/scripts/chunkers/_smoke_batch_b.py:28` · `sdtm-rag/eval/prod_wirein/judge_workflow.js:11-12` · `sdtm-rag/eval/prod_wirein/judge_workflow_v2.js:10`

**Interfaces:** Produces: 全部路径锚在新深度指向 `$R/knowledge_base` — Task 8 服务与 Task 12 实测依赖。

- [ ] **Step 1: 逐处修改 parent 计数** (机械等价, 深度 3→1):
  - `config.py:15`: `_REPO_ROOT = _SDTM_RAG_ROOT.parent.parent.parent` → `_REPO_ROOT = _SDTM_RAG_ROOT.parent`
  - `ingest.py:35`: `REPO_ROOT = SDTM_RAG_ROOT.parent.parent.parent` → `REPO_ROOT = SDTM_RAG_ROOT.parent`
  - `build_meta.py:248` / `reconcile_meta.py:133` / `mine_implicit_relations.py:14`: `parents[4]` → `parents[2]`
  - `validation_scenarios.py:26` / `error_test_set.py:24` / `_smoke_batch_b.py:28`: 5 连 `.parent` → 3 连 `.parent`
  - `judge_workflow.js:11-12`: `` `${ROOT}/branches/07_rag_kg/sdtm-rag` `` → `` `${ROOT}/sdtm-rag` ``
  - `judge_workflow_v2.js:10`: `'/Users/bojiangzhang/MyProject/sdtm-pedia/branches/07_rag_kg/sdtm-rag'` → `'/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag'`

- [ ] **Step 2: 残留自检** — `grep -rn "parent.parent.parent\|parents\[4\]" $R/sdtm-rag/server $R/sdtm-rag/scripts $R/sdtm-rag/eval --include="*.py"` Expected: 0 hit (或仅命中与 repo-root 无关的其他用途, 逐条人工判定)。`grep -rn "branches/07_rag_kg" $R/sdtm-rag --include="*.py" --include="*.js" --include="*.sh"` → 只剩注释/docstring, 顺手改掉 (build_kg_viewer.py:14 · _smoke_batch_a.py:4,25 · deploy/deploy.sh:18 · deploy/README.md:22,56)。
- [ ] **Step 3: 路径锚点直测** (venv 未建, 用系统 uv 临时跑):

```bash
cd $R/sdtm-rag && uv run python -c "
from pathlib import Path
import sys; sys.path.insert(0, '.')
from server.config import get_settings
s = get_settings()
kb = Path(s.kb_root); print('kb_root:', kb)
assert kb == Path('$R/knowledge_base').resolve() and (kb/'INDEX.md').exists(), 'KB ANCHOR BROKEN'
print('OK')
"
```

Expected: `OK` (若 get_settings 接口名不符, 以 config.py 实际公开接口为准改探针, 断言目标不变: kb_root 指向 `$R/knowledge_base` 且 INDEX.md 存在)。

- [ ] **Step 4: Commit** — `git add -A sdtm-rag && git commit -m "fix(restructure): 段4a — sdtm-rag 深度 3→1 全部 parent-chain 锚点 + judge js 硬编码 + 注释路径"`

### Task 8: 段 4b venv 重建 + plist 重写 + 服务重启验活

- [ ] **Step 1: 重建 venv**

```bash
cd $R/sdtm-rag && rm -rf .venv && uv sync --all-extras
.venv/bin/python -c "import fastapi, chromadb; print('venv OK')"   # Expected: venv OK
```

- [ ] **Step 2: 重写 2 个 plist** — `~/Library/LaunchAgents/com.sdtmrag.api.plist` 与 `com.sdtmrag.ui.plist`: 把全部 4 处 `/Users/bojiangzhang/MyProject/sdtm-pedia/branches/07_rag_kg/sdtm-rag` 替换为 `/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag` (ProgramArguments[0] / WorkingDirectory / StandardOutPath / StandardErrorPath; 其余键一律不动)。

```bash
sed -i '' 's|/sdtm-pedia/branches/07_rag_kg/sdtm-rag|/sdtm-pedia/sdtm-rag|g' ~/Library/LaunchAgents/com.sdtmrag.api.plist ~/Library/LaunchAgents/com.sdtmrag.ui.plist
grep -c "branches" ~/Library/LaunchAgents/com.sdtmrag.api.plist ~/Library/LaunchAgents/com.sdtmrag.ui.plist   # Expected: 0 0
plutil -lint ~/Library/LaunchAgents/com.sdtmrag.api.plist ~/Library/LaunchAgents/com.sdtmrag.ui.plist          # Expected: OK ×2
```

- [ ] **Step 3: 重启服务**

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.api.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.ui.plist
sleep 5 && curl -s http://127.0.0.1:8000/api/health   # Expected: {"status":"ok"}
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8501   # Expected: 200
```

- [ ] **Step 4: 端到端真答一题** — 同 Task 2 Step 1 的 `/api/ask` 探针。Expected: `sources: >0` (证明 chroma + KB 路径全通)。
- [ ] **Step 5: pytest 全量** — `cd $R/sdtm-rag && .venv/bin/python -m pytest -q`。Expected: **521+ passed, 0 failed**。
- [ ] **Step 6: Commit evidence** — 服务验活输出 + pytest 摘要写 `.work/09_repo_refactor_v3/evidence/step_services_smoke.md`; `git add .work/09_repo_refactor_v3 && git commit -m "chore(restructure): 段4b — venv 重建 + plist 迁移 + 服务验活 evidence (plist 在 ~/Library 不入库)"`

### Task 9: 段 4c web / tools 修复 + 本地构建验证

**Files:**
- Modify: `web/src/content.config.ts` · `web/scripts/build-bundles.sh` · `tools/build_release.sh:53,70` · `tools/git-hooks/pre-commit`

- [ ] **Step 1: web 内容源改指 milestones** — `content.config.ts`: `path.resolve(..., '../release/v1.4')` → `'../milestones/release/v1.4'` (以文件内实际写法为准, 只改路径段); `build-bundles.sh`: `SRC_ROOT` 中 `release/${VERSION}` → `milestones/release/${VERSION}`。
- [ ] **Step 2: tools 修复** — `build_release.sh` 行 53 `branches/jp_delivery/scripts/build_zip.sh` → `milestones/jp_delivery/scripts/build_zip.sh`; 行 70 同理 `deliverable` glob; 文件内其余 `release/` 源路径 → `milestones/release/` (先 `grep -n "release\|jp_delivery" tools/build_release.sh` 全量看再逐处改)。`tools/git-hooks/pre-commit`: 正则 `^release/v[0-9.]+/self_deploy/` → `^milestones/release/v[0-9.]+/self_deploy/`。`bash -n tools/build_release.sh tools/git-hooks/pre-commit` Expected: 无输出。
- [ ] **Step 3: web 本地构建验证**

```bash
cd $R/web && npm install && npm run build
```

Expected: build 成功, `web/dist/index.html` 存在。失败即修 (最可能是 content.config 路径写法), 不带病提交。

- [ ] **Step 4: Commit** — `cd $R && git add web/src/content.config.ts web/scripts/build-bundles.sh tools/ && git commit -m "fix(restructure): 段4c — web 内容源/构建脚本/tools 指向 milestones/release + milestones/jp_delivery"`
- [ ] **Step 5: CF Pages watch paths** — dashboard 手动项 (用户或浏览器工具): Build watch paths 中 `release/**` → `milestones/release/**` (release 已冻结, 此项影响极小, 不阻塞后续 Task; push 后线上构建验证在 Task 12)。

### Task 10: 段 5a 活文档路径同步

**Files (active 清单, 只改这些):**
- Modify: `CLAUDE.md` · `README.md` · `README_CN.md` · `METHODOLOGY.md` · `docs/PROGRESS.md` (仅路径, 重切在 Task 11) · `.work/AGENT_GUIDE.md` · `.work/MANIFEST.md` · `.work/meta/worklog/INDEX.md` · `docs/DESIGN_RAG_KG.md` · `sdtm-rag/KG_ROADMAP.md` · `sdtm-rag/DEPLOY_PLAN.md` (以 grep 实际命中为准增删)

- [ ] **Step 1: 生成全量命中清单** (sed 前先看, v1 教训):

```bash
cd $R && grep -rn "branches/" --include="*.md" CLAUDE.md README.md README_CN.md METHODOLOGY.md docs/ .work/AGENT_GUIDE.md .work/MANIFEST.md .work/meta/worklog/INDEX.md sdtm-rag/ 2>/dev/null | grep -v "docs/superpowers/" > .work/09_repo_refactor_v3/evidence/path_hits_before.txt
grep -rn "ai_platforms/\|^release/\|(release/\|\`release/\|archive/" --include="*.md" CLAUDE.md README.md README_CN.md METHODOLOGY.md docs/PROGRESS.md .work/AGENT_GUIDE.md .work/MANIFEST.md >> .work/09_repo_refactor_v3/evidence/path_hits_before.txt
wc -l .work/09_repo_refactor_v3/evidence/path_hits_before.txt
```

人工浏览清单, 剔除 historical 命中 (worklog 正文 / superpowers / REPO_REFACTOR.md / evidence 文档)。

- [ ] **Step 2: 长路径优先 sed (只对 active 文件逐个跑)**

```bash
ACTIVE="CLAUDE.md README.md README_CN.md METHODOLOGY.md docs/PROGRESS.md .work/AGENT_GUIDE.md .work/MANIFEST.md .work/meta/worklog/INDEX.md docs/DESIGN_RAG_KG.md sdtm-rag/KG_ROADMAP.md sdtm-rag/DEPLOY_PLAN.md"
for f in $ACTIVE; do
  sed -i '' -e 's|branches/07_rag_kg/sdtm-rag|sdtm-rag|g' \
            -e 's|branches/07_rag_kg|milestones/07_rag_kg|g' \
            -e 's|branches/06_deep_verification|milestones/06_deep_verification|g' \
            -e 's|branches/jp_delivery|milestones/jp_delivery|g' "$R/$f"
done
```

`ai_platforms/` → `milestones/ai_platforms/`、`release/` → `milestones/release/`、`archive/` → `milestones/archive/` 三组**不用盲 sed** (常见词多义): 按 Step 1 清单逐处 Edit, 只改真路径引用。

- [ ] **Step 3: 结构描述段人工重写** — README.md + README_CN.md 的 Project Structure/项目结构段 (行 ~91-159) 按 spec §2 新树成对重写 (顺手修 "release 在 ai_platforms 下" 陈旧描述); CLAUDE.md Key Paths 表逐行核对; MANIFEST 目录树 + Chain 07_RAG 定义更新, 并加注记行: `> 2026-07-21 布局变更 (restructure v3): 历史文档中 branches/ · 顶层 ai_platforms/ · release/ · archive/ 均为旧布局。`
- [ ] **Step 4: 语义复核** — 逐文件 `git diff` 人眼过一遍 (v2 教训: sed 保路径不保语义), 特别是 CLAUDE.md Key Paths 描述文字与 METHODOLOGY.md 超链接 (渲染不 404)。
- [ ] **Step 5: Commit** — `git add -A && git commit -m "docs(restructure): 段5a — 活文档路径全量迁移 (active/historical 二分, historical 不动)"`

### Task 11: 段 5b PROGRESS.md 重切 + memory 更新

- [ ] **Step 1: PROGRESS.md 第 4 行巨段重切** — 把 84K 单行"最后更新"段替换为 ≤10 行摘要 (当前态: SP6 DONE + restructure v3 完成 + 指针 `.work/meta/worklog/phase_07_rag_kg.md`); 被剪内容不搬运 (worklog 已有对应收口记录, git 历史可查)。全文件确认 ≤150 行且无单行 >2000 字符: `awk '{ if (length($0) > 2000) print NR }' docs/PROGRESS.md` Expected: 空。
- [ ] **Step 2: memory 更新** (在 ~/.claude 下, 不入 repo git):
  - `~/.claude/projects/-Users-bojiangzhang-MyProject-sdtm-pedia/memory/project_kg_decision.md`: 3 处 `branches/07_rag_kg/sdtm-rag/` → `sdtm-rag/` (KG_ROADMAP 等指针)
  - `~/.claude/projects/-Users-bojiangzhang-MyProject-sdtm-pedia/memory/project_local_deploy_plan.md`: 4 处同理
  - 各加一行: `(2026-07-21 restructure v3: sdtm-rag 已提升至仓库顶层)`
- [ ] **Step 3: Commit** — `git add docs/PROGRESS.md && git commit -m "docs(restructure): 段5b — PROGRESS.md 巨段重切回轻量看板 (细节在 worklog/git 历史)"`

### Task 12: 段 6 验证矩阵 + push + 线上构建

- [ ] **Step 1: 双向 grep 零残留**

```bash
cd $R && grep -rn "branches/" --include="*.md" --include="*.py" --include="*.js" --include="*.sh" --include="*.ts" --include="*.yml" --include="*.yaml" --include="*.json" . 2>/dev/null | grep -v "^./.git" | grep -v node_modules | grep -v ".venv" | grep -v "milestones/" | grep -v "docs/superpowers/" | grep -v ".work/07_" | grep -v ".work/refactor_v1" | grep -v ".work/meta/worklog" | grep -v "docs/REPO_REFACTOR.md" | grep -v ".work/09_repo_refactor_v3"
```

Expected: 0 行 (排除项全是 historical 与本次 evidence)。命中即改或归 historical 白名单并记录。反向: `ls $R/branches 2>&1` Expected: No such file or directory。

- [ ] **Step 2: 服务四联验** — health + `/api/ask` 真答 (sources>0) + 8501 HTTP 200 + `curl -s http://127.0.0.1:7474` (neo4j 未受扰)。
- [ ] **Step 3: 管线实测** (parent-chain 静默失败的强制检查) — `cd $R/sdtm-rag && .venv/bin/python scripts/reconcile_meta.py` (或其 `--check` 等价模式) Expected: 锚点全过 (63 域/1917/1523/1005 等既有锚) — 证明 build/reconcile 码路在新深度读到真 KB。
- [ ] **Step 4: pytest 复跑** — `.venv/bin/python -m pytest -q` Expected: 521+ passed (Task 8 后无代码变更, 应同额通过)。
- [ ] **Step 5: subagent dry-run** (Rule D 精神) — 派独立 Explore agent: "按 $R/CLAUDE.md 的 Session Startup 清单模拟新 session: 逐个确认所列文件存在并可读, 再按 Key Paths 表逐行验证路径存在; 报告一切踩空。" Expected: 0 踩空。结果存 `evidence/step_dryrun_agent.md`。
- [ ] **Step 6: push + CF 线上构建** — `git push origin main --tags`; 等 CF Pages 自动构建, 验证 https://sdtm-pedia.pages.dev/ 正常返回 (构建挂则已部署版本继续 serve, 修复 config 重推)。
- [ ] **Step 7: Commit evidence** — 验证矩阵结果写 `evidence/step_verification_matrix.md`, commit。

### Task 13: 收尾 — RETROSPECTIVE + 三套索引 + 销旧账

- [ ] **Step 1: RETROSPECTIVE.md** (Rule C 三段: 保留的做法 / 必须补的缺口 / 关键决策复盘) 写 `.work/09_repo_refactor_v3/RETROSPECTIVE.md`; `_progress.json` 置 `"status": "closed"`。
- [ ] **Step 2: 销 08 旧账** — `.work/08_repo_refactor_v2/_progress.json`: `"awaiting_user_ack"` → `"closed"` 加注 `"closed_note": "2026-07-21 随 restructure v3 收尾销账; v2 遗留 smoke (build_release/web build) 已被 v3 Task 9/12 实测覆盖"`。
- [ ] **Step 3: 三套索引收尾** (CLAUDE.md Session Wrap-up 惯例) — worklog: `.work/meta/worklog/phase_meta_refactor.md` append restructure v3 记录; `docs/PROGRESS.md` 状态行更新; MANIFEST 已在 Task 10 更新; CLAUDE.md Key Paths 加一行 `| 09 restructure v3 | .work/09_repo_refactor_v3/ (branches→milestones, 2026-07-21) |`。
- [ ] **Step 4: 最终 commit + push** — `git add -A && git commit -m "docs(restructure): 段6 收尾 — RETROSPECTIVE + 索引 + 销 08 旧账" && git push origin main`。
- [ ] **Step 5: 汇报** — 一行总结: 迁移前后结构对比 + 释放磁盘数字 + 服务/网站/测试全绿证据。

---

## Self-Review 记录

- Spec 覆盖: §2 结构→Task 6 · §3 六段→Task 1-13 · §4 清单→Task 2/3/4 · §5 修复面→Task 7/8/9 · §6 文档→Task 10/11 · §7 验证→Task 12 · D1-D5 全落地 · §8 范围外无任务违反。
- 类型/命名一致: `milestones/` 六子目录名在 Task 6/10/12 一致; plist 路径 Task 8 与调研原文一致。
- eval 删除清单已逐文件枚举 (Task 4), 与"≤2026-06-20 run 输出"原则一致, 脚本/题集/kgval/agg 排除。
