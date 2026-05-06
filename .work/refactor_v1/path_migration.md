# Phase C — 路径迁移枚举表

> 用途: 段 3 执行 `git mv` 之后, 用本表逐项更新所有"内部引用". 每条都对应一次 `sed` 或手工编辑.
> 必须在 Phase C 实搬之前 review 本表完整性 — 漏一条引用 = round 路由断链.
>
> **Convention**: 路径以 repo root 为基准. CLAUDE.md / 顶层 README 用 repo 相对; 各 phase 内部文档可能用 `..` 相对.

---

## 表 0 — 顶层 git mv 操作

| 旧路径 | 新路径 | 命令 |
|--------|--------|------|
| `.work/06_deep_verification/` | `branches/06_deep_verification/` | `git mv .work/06_deep_verification branches/06_deep_verification` |
| `docs/jp/` | `branches/jp_delivery/` | `git mv docs/jp branches/jp_delivery` |
| (段 1 已做) `project_knowledge_base/` | `archive/old_knowledge_base_v0/` | (段 1 已 mv) |

---

## 表 1 — `.work/06_deep_verification/PLAN.md` 内部引用

文件搬到 `branches/06_deep_verification/PLAN.md` 后, 内部 chain F header 的相对路径要改:

| 旧引用 (从 .work/06/ 视角) | 新引用 (从 branches/06/ 视角) |
|---------------------------|-------------------------------|
| `→ ../03_verification/issues_found.md` | `→ ../../.work/03_verification/issues_found.md` |
| `→ ../meta/worklog.md` | `→ ../../.work/meta/worklog/phase06_deep_verification.md` (假设段 2 已拆) |
| `→ _progress.json` | (不变, 同目录) |
| `→ evidence/checkpoints/` | (不变, 同目录) |

**搜索命令** (确认本表覆盖):
```bash
grep -nE "(\.\./|\.work/)" branches/06_deep_verification/PLAN.md
```

---

## 表 2 — `multi_session/MULTI_SESSION_PROTOCOL.md` 内部硬编码路径

PROTOCOL 文件里硬编码了大量 `.work/06_deep_verification/` 绝对路径 (从 repo root 视角写的). 全部改:

| 旧 | 新 |
|----|-----|
| `.work/06_deep_verification/evidence/checkpoints/` | `branches/06_deep_verification/evidence/checkpoints/` |
| `.work/06_deep_verification/pdf_atoms.jsonl` | `branches/06_deep_verification/pdf_atoms.jsonl` |
| `.work/06_deep_verification/audit_matrix.md` | `branches/06_deep_verification/audit_matrix.md` |
| `.work/06_deep_verification/_progress.json` | `branches/06_deep_verification/_progress.json` |
| `.work/06_deep_verification/multi_session/` | `branches/06_deep_verification/multi_session/` |
| `.work/06_deep_verification/subagent_prompts/` | `branches/06_deep_verification/subagent_prompts/` |
| `.work/06_deep_verification/schema/` | `branches/06_deep_verification/schema/` |

**批量命令** (示例, 实跑前用 `grep` 先 dry-run):
```bash
sed -i.refactor_bak 's|\.work/06_deep_verification/|branches/06_deep_verification/|g' \
  branches/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md
# review 后删 .refactor_bak
```

---

## 表 3 — 72 个 kickoff 文件的硬编码路径

`branches/06_deep_verification/multi_session/` 下 72 个 kickoff/retro 文件, 全部含硬编码路径. 用同一 sed 批跑:

```bash
find branches/06_deep_verification/multi_session/ -name "*.md" -exec \
  sed -i.refactor_bak 's|\.work/06_deep_verification/|branches/06_deep_verification/|g' {} \;

# 验证: 不应再有 .work/06_deep_verification/ 出现
grep -rn "\.work/06_deep_verification" branches/06_deep_verification/multi_session/
# 应输出空 (除注释里历史 reference)

# review 后清理
find branches/06_deep_verification/ -name "*.refactor_bak" -delete
```

---

## 表 4 — `subagent_prompts/` 里的路径

Writer/Matcher/Reviewer prompts 模板可能引用主目录路径:

```bash
grep -rn "\.work/06_deep_verification" branches/06_deep_verification/subagent_prompts/
```

针对每个匹配, 同样 sed 批改. 这些 prompt 是后续 batch 派发用的, 改错就让 subagent 找不到 schema / atoms.

---

## 表 5 — CLAUDE.md (项目根)

整段 "## 06 Deep Verification (旁枝)" 都要改:

| 旧 | 新 |
|----|-----|
| `.work/06_deep_verification/_progress.json` | `branches/06_deep_verification/_progress.json` |
| `.work/06_deep_verification/multi_session/batch_NN_kickoff.md` | `branches/06_deep_verification/multi_session/batch_NN_kickoff.md` |
| `.work/06_deep_verification/multi_session/reconciler_kickoff_roundN.md` | `branches/06_deep_verification/multi_session/reconciler_kickoff_roundN.md` |
| `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` | `branches/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` |
| `.work/06_deep_verification/PLAN.md` | `branches/06_deep_verification/PLAN.md` |

Key Paths 表对应行:

| 旧 | 新 |
|----|-----|
| `06 Deep Verification 入口 \| .work/06_deep_verification/PLAN.md` | `06 Deep Verification 入口 \| branches/06_deep_verification/PLAN.md` |
| `06 Deep Verification schema \| .work/06_deep_verification/schema/...` | `06 Deep Verification schema \| branches/06_deep_verification/schema/...` |
| `docs/jp/ iTMS 納品旁枝 \| docs/jp/PLAN.md + EXECUTION_PLAN.md` | `iTMS 納品旁枝 \| branches/jp_delivery/PLAN.md + EXECUTION_PLAN.md` |

---

## 表 6 — `.work/MANIFEST.md` (段 2 已瘦身)

MANIFEST 段 2 后只剩结构指针, 仍要改:

| 旧 | 新 |
|----|-----|
| 任何指向 `.work/06_deep_verification/` 的指针 | `branches/06_deep_verification/` |
| 任何指向 `docs/jp/` | `branches/jp_delivery/` |

---

## 表 7 — `.work/meta/worklog/phase06_deep_verification.md` (段 2 已拆)

如段 6 决策中 worklog 拆分到此文件, 该文件应改成 1 行:
```markdown
# Phase 06 Deep Verification — 工作日志

> 本 phase 已迁移到独立旁枝目录: `branches/06_deep_verification/`
> 详细 PLAN / 进度 / multi_session 历史见该目录.
> 本文件保留作 .work/meta/worklog/INDEX.md 的占位指针.
```

---

## 表 8 — `docs/PROGRESS.md`

各 phase 状态板里 06 那一行的路径指针:

| 旧 | 新 |
|----|-----|
| (任何 .work/06_deep_verification/ 引用) | branches/06_deep_verification/ |

---

## 表 9 — `.gitignore` (确认无影响)

```bash
grep -n "06_deep_verification\|jp" .gitignore
```

如有针对这俩路径的规则, 同步改; 默认无.

---

## 表 10 — `branches/jp_delivery/` 内部文件

| 文件 | 内部相对路径需要改吗? |
|------|----------------------|
| `branches/jp_delivery/PLAN.md` | 视内部链接, 跑 `grep -nE "\.\./|docs/" branches/jp_delivery/PLAN.md` 看 |
| `branches/jp_delivery/EXECUTION_PLAN.md` | 同上 |
| `branches/jp_delivery/WORKLOG.md` | 同上 |
| `branches/jp_delivery/CHANGELOG.md` | 同上 |

---

## Dry-run 校验脚本 (C-16/17/18 实现)

```bash
# 1. 反向: 不应有任何 active 文件还引用旧路径
grep -rn "\.work/06_deep_verification\|docs/jp/" \
  --include="*.md" --include="*.json" \
  --exclude-dir=archive \
  --exclude-dir=.git \
  .
# 期望: 仅在 .work/refactor_v1/ 文档自身 (历史 reference) 出现

# 2. 正向: 新路径应在以下文件被引用 ≥1 次
for f in CLAUDE.md .work/MANIFEST.md .work/AGENT_GUIDE.md docs/PROGRESS.md; do
  count=$(grep -c "branches/06_deep_verification" "$f" 2>/dev/null || echo 0)
  echo "$f: $count refs"
done

# 3. multi_session/ 全部 kickoff 自检
grep -L "branches/06_deep_verification" branches/06_deep_verification/multi_session/*.md
# 期望: 空输出 (每个文件都至少含 1 次新路径自指)
```

---

## 落空风险点

1. **绝对路径 vs 相对路径混用**: 有些文件用 `.work/06...`, 有些用 `../../`. sed 只覆盖前者. 后者要单独 grep.
2. **代码块里的路径**: bash 命令示例里的路径也算引用, 要改.
3. **commit message 里的路径**: 不改 (历史 commit 不可变).
4. **.bak 文件里的路径**: 段 2 已大部分 git rm, 残留的不重要, 不改.

---

> 本表段 3 启动前再 review 一遍, 段 3 实跑时 check 一项删一项, 漏一项 = dry-run 失败. 整个段 3 不允许"边跑边发现新引用".
