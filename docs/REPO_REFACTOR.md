# Repo 重构设计 — Single Source of Truth (SSoT)

> 起草: 2026-05-11
> 触发: `ai_platforms/` + `branches/jp_delivery/` + `web/` 三方耦合糊, 同一份 `release/v1.0/` 被复制 3 处 (源 + web zip + jp zip), 版本号脱节, 改一处易漏
> 原则: **一个文件只保留一个出处, 只维护一个文件**

---

## 1. 现状关系图

```
              ai_platforms/  (主仓 = 内容唯一源 + 内部工程混居)
              ┌──────────────────────────────────────────────────┐
              │  顶层 SMOKE_V4.md · SYNC_BOARD.md · README.md     │
              │  _template/ · plans/ · retrospectives/            │
              │  chatgpt_gpt/ gemini_gems/ claude_projects/       │
              │  notebooklm/   ← 各平台 current/+dev/+docs/       │
              │                                                   │
              │  release/v1.0/   ★ 唯一对外发布载体               │
              │  ├─ *.md × 13 × 3 = 39 三语 META md               │
              │  └─ self_deploy/<platform>/                       │
              │      ├ tutorial.{en,ja,zh}.md                     │
              │      ├ system_prompt.md / instructions.md         │
              │      └ uploads/                                   │
              └──────────────────────────────────────────────────┘
                        │                               │
                        ▼ (read + 反向写 frontmatter)    ▼ (copy 嵌入)
              ┌──────────────────────┐         ┌────────────────────────┐
              │  web/                │         │ branches/jp_delivery/  │
              │  Astro glob          │         │  scripts/build_xlsx.py │
              │   release/v1.0/*.md  │         │   → 6 xlsx             │
              │  build-bundles.sh    │         │  (手工) zip            │
              │   → dist-bundles/    │         │   → deliverable/...zip │
              │   _bundle_v1.0.zip×4 │         │   内嵌 ai_platforms_   │
              │  prod: pages.dev     │         │   release_v1.0/ 副本    │
              └──────────────────────┘         └────────────────────────┘
```

## 2. 违反 SSoT 的 6 处 (按严重程度)

| # | 问题 | 后果 |
|---|---|---|
| 1 | `release/v1.0/` 内容被复制 3 处 (源 + web zip + jp zip), 无 build manifest | v0.5 jp zip 还停在旧 tutorial, 改源不知道要重打 |
| 2 | web 反向写入 ai_platforms (`add-frontmatter.mjs`) | 下游修改上游, 概念倒挂 |
| 3 | `claude_projects/current/UPLOAD_TUTORIAL.md` + `notebooklm/current/UPLOAD_TUTORIAL.md` 与 `self_deploy/<p>/tutorial.zh.md` 同源 diverge | 同一教程 2 份, 不知道改哪份 |
| 4 | `chatgpt_gpt/current/upload_manifest.md` + `gemini_gems/current/upload_manifest.md` 与 self_deploy/ 同主题但内容不同 | 命名误导 (像 tutorial 实则内部工程文档) |
| 5 | release tutorial 内引用 `../../../../notebooklm/dev/evidence/...` 在外部 zip 内全断链 | 现在靠"内部 QA 证据不在 release 包内"免责声明 patch |
| 6 | jp_delivery 没 build_zip 脚本, 全手工打包 | 改源永远滞后 |

---

## 3. 目标结构 (SSoT)

```
sdtm-pedia/
├── knowledge_base/         (KB 内容, 不变)
├── source/                 (PDF/xlsx 源, 不变)
├── docs/                   (项目 doc, 含本文件)
├── .work/                  (工作目录, 不变)
│
├── release/                ★ 唯一对外发布源 (从 ai_platforms/ 提升)
│   └── v1.0/
│       ├── *.md × 39       (三语 META md, frontmatter 直接写在源里)
│       ├── self_deploy/<platform>/
│       │   ├ tutorial.{en,ja,zh}.md   ← 唯一外部 tutorial 源
│       │   ├ system_prompt.md / instructions.md
│       │   └ uploads/
│       └── BUILD.md        (打包契约: 输出哪些产物, 给谁用)
│
├── ai_platforms/           (各平台内部开发, 不再含 release/)
│   ├── chatgpt_gpt/ · gemini_gems/ · claude_projects/ · notebooklm/
│   │   └ 各平台保留 current/+dev/+docs/+archive/
│   │     但 current/ 改名 dev_manifest.md (明示是内部工程)
│   │     删除 current/UPLOAD_TUTORIAL.md (claude/notebooklm)
│   ├── retrospectives/ · plans/ · _template/
│   └── SMOKE_V4.md · SYNC_BOARD.md
│
├── tools/                  (★ 新增, 统一 build 入口)
│   └── build_release.sh    (打 web bundles + jp zip, 写 BUILD_MANIFEST.json)
│
├── web/                    (派生消费者 1, 只读 release/)
│   ├── src/content.config.ts: glob ../release/v1.0/*.md
│   ├── scripts/build-bundles.sh: 改成被 tools/build_release.sh 调
│   └── dist-bundles/       (产物, .gitignore)
│
└── branches/
    └── jp_delivery/        (派生消费者 2, 只读 release/)
        ├── scripts/build_zip.sh   (★ 新增, 被 tools/build_release.sh 调)
        ├── deliverable/           (产物, .gitignore zip)
        └── (xlsx + 工作日志, 不变)
```

**核心改动**:
- `release/` 提升到仓库顶层 ← 概念清晰 (顶级产物, 不属于 ai_platforms 内部)
- 各平台 `current/UPLOAD_TUTORIAL.md` (claude/notebooklm) **删除**
- 各平台 `current/upload_manifest.md` (chatgpt/gemini) **改名** `dev_manifest.md` 防误导
- 反向写入消除: frontmatter 直接写在 `release/v1.0/*.md` 源 (一次性), 删 `web/scripts/add-frontmatter.mjs`
- `tools/build_release.sh` 一个总入口, 派出 web + jp 产物, 写 `BUILD_MANIFEST.json` 记 hash
- zip 产物加 .gitignore (默认不进 git, 或留 latest 一份)

---

## 4. 迁移步骤 (Tier 2, 5-8 step)

1. **新建 `release/`** 在仓库顶层, `git mv ai_platforms/release release`
2. **改 web/src/content.config.ts**: `RELEASE_DIR` 从 `../ai_platforms/release/v1.0` → `../release/v1.0`
3. **改 web/scripts/build-bundles.sh**: `SRC_ROOT` 路径同上
4. **执行一次 `web/scripts/add-frontmatter.mjs`** 把 frontmatter 写进 release md, 然后**删除该脚本**
5. **删除 `claude_projects/current/UPLOAD_TUTORIAL.md` + `notebooklm/current/UPLOAD_TUTORIAL.md`** (已被 self_deploy/ tutorial 取代)
6. **改名** `chatgpt_gpt/current/upload_manifest.md` + `gemini_gems/current/upload_manifest.md` → `dev_manifest.md`
7. **新建 `tools/build_release.sh`** + `branches/jp_delivery/scripts/build_zip.sh`, 串起来
8. **更新引用** (一次性 grep 替换):
   - `ai_platforms/release/v1.0/` → `release/v1.0/` (全仓)
   - CLAUDE.md Key Paths
   - jp_delivery PLAN/WORKLOG/CHANGELOG/sources/00_納品範囲.yml
   - `.work/MANIFEST.md`, `docs/PROGRESS.md`
9. **加 `.gitignore`**: `web/dist-bundles/*.zip`, `branches/jp_delivery/deliverable/*.zip` (可选保留 latest)
10. **(可选)** pre-commit hook 检查三语 tutorial.{en,ja,zh}.md mtime 偏差

---

## 5. 决策点 (待用户定)

| 点 | 选项 | 推荐 |
|---|---|---|
| **A** release/ 位置 | (a) 提升顶层 / (b) 留 ai_platforms/release/ | **(a) 提升** — 概念清晰, 改动可控 (主要是 grep 替换路径) |
| **B** current 教程 | (a) 删 UPLOAD_TUTORIAL.md / (b) 留只读标记 | **(a) 删** — 没人维护两份 |
| **C** build 入口 | (a) tools/build_release.sh 总入口 / (b) 各自维护 / (c) Makefile | **(a)** — 总入口最清楚 |
| **D** 三语锁步 | (a) pre-commit hook 警告 / (b) CHANGELOG 强制 / (c) 手动靠记忆 | **(a)** — 自动化 + 警告 (非阻断), 不影响开发 |

---

## 6. 重构后维护规则

- **改外部发布内容 → 只改 `release/v1.0/`**, 任何下游 (web / jp / GH release) 都从这里派生
- **改内部平台开发 → 只改 `ai_platforms/<platform>/`**, 不影响发布
- **改三语 tutorial → 必同步三语**, pre-commit 警告
- **发布新版本 → `tools/build_release.sh v1.1`** 一键产出所有 zip, 写 BUILD_MANIFEST.json

---

## 附: 不在本重构范围内 (单独处理)

- `branches/06_deep_verification/` (本身就是独立旁枝)
- `knowledge_base/` (KB 内容, 由 Phase 1-5 维护)
- `.work/07_website/phase{6,7,8}/` (web 历史归档, closed)
- `branches/jp_delivery/glossary/research_reports/` (Phase 1 调研报告, 已完成)

*重构是结构层面, 不动产物内容.*
