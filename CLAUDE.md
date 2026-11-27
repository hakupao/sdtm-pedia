# SDTM Knowledge Base Project

## Project Overview

SDTM (Study Data Tabulation Model) knowledge base built from CDISC standard source files (PDF + xlsx).
293 Markdown files covering 63 domains, terminology, model concepts, and implementation guide chapters.
Public repo; RAG 问答服务在独立的公开仓 `hakupao/sdtm-rag` (以 submodule 引用本仓 `knowledge_base/`).

## CLAUDE.md 写作规则 (写入前必过闸)

CLAUDE.md 是**长效约束清单**, 不是工作日志, 不是状态看板.

- **可以写**: 启动 / 收尾 / 路由词 / Chain 等流程规则; 跨 session 硬约束 (规则 A/B/C/D, PASS 四条);
  Key Paths 一行指针 (单元格 ≤ 80 字符)
- **不要写**: round / batch / version 进度数字; in-flight 状态; 历史归档清单; 已在 MANIFEST / worklog 写过的内容;
  多子句长段落 / 表格单元格 > 100 字符 (拆专门 doc, 这里只留指针)
- **TTL**: 带日期 / 版本的状态句, 阶段关闭即删或迁到 `.work/meta/worklog/<phase>.md`; 收尾时扫一遍;
  Key Paths 条目 ≥ 2 个月没动过就重审 (在用就压短, 不在用就删)
- **红线**: 总行数 ≤ 150 行; 单章节 ≥ 30 行 = 拆 doc 留指针; 表格单行 ≤ 200 字符

## Session Startup

Every new session, **before doing any work**, read these files in order:

0. `.work/AGENT_GUIDE.md` — 一页纸进入指引 (找东西速查 + phase 入口表 + 路由词)
1. `.work/MANIFEST.md` — file layout, change chains, quick reference table
2. `docs/PROGRESS.md` — 当前各 phase 状态 (唯一状态源)
3. `.work/meta/worklog/INDEX.md` — 历史工作日志入口 (按 phase 拆分)
4. `.work/03_verification/issues_found.md` — open issues
5. `.work/meta/retrospective.md` § 4 — six prevention rules (1-4 内容抽取; 5-6 代码/测试: 变异验证 + 按成因选对策)

Then summarize to the user: current status, open issues, and suggested next step.

## 跨会话路由词

用户说这些词时, 直接按下列步骤执行:

- **「KB 更新」** — 改 `knowledge_base/` → 走 Chain D 溯源 (`.work/meta/mapping.md` →
  `docs/TRACEABILITY.md` → worklog) → `tools/check_links.py` live docs 计数不升 → commit →
  `git push origin main` (origin 已配两个 push URL, 一次推两处) → 打 KB tag `kb-YYYY.MM.DD`
  (annotated, 同日多次加 `.N`) 并 push → 提醒用户到 sdtm-rag 仓说「KB 更新」, submodule 钉到该 tag
- **「网站更新」** — 改 `web/` 或 `releases/v1.4/` → `cd web && npm ci && npm run build`
  (页数不应无故变化) → commit + push → 确认 Cloudflare Pages 部署成功、
  https://sdtm-pedia.pages.dev/ 正常
- **「收尾」/「wrap up」/「提交收尾」** — 见下方 Session Wrap-up

## Change Chains

When modifying any `.work/` file, check its `<!-- chain: X -->` header for related files that must also be updated.
Full chain definitions are in `.work/MANIFEST.md`.

## Key Paths

| What | Where |
|------|-------|
| Knowledge base (产品本体) | `knowledge_base/` |
| Source files (PDF/xlsx, gitignored) | `source/` |
| 发布包 v1.0-v1.4 (冻结; web 读 v1.4) | `releases/v1.{0-4}/` |
| Web 站点 (Astro; prod sdtm-pedia.pages.dev) | `web/` |
| 构建 / 校验工具 | `tools/build_release.sh`, `tools/check_links.py` |
| 新旧路径对照 (2026-11-25 重组) | `docs/PATH_MAP.md` |
| 已收口工作线 (只读) | `archive/` (deep_verification / ai_platforms / jp_delivery / legacy) |
| 06 深审入口 + 终态数字 | `archive/deep_verification/{PLAN,RETROSPECTIVE}.md` |
| Tier B 补修入口 + 复盘 | `.work/10_tier_b_repair/{PLAN,RETROSPECTIVE,HANDOFF}.md` |
| PDF 笔误登记 (KB≠PDF 先查) | `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` |
| METHODOLOGY 公开声明 | `METHODOLOGY.md` + `releases/v1.{0,1}/METHODOLOGY.{en,zh,ja}.md` |
| RAG 问答服务 | 独立公开仓 `hakupao/sdtm-rag` |
| Agent 进入指引 | `.work/AGENT_GUIDE.md` |
| Page index (authoritative) | `.work/02_indexing/page_index.json` |
| Verification plan / issues | `.work/03_verification/{plan,issues_found}.md` |
| Retrospective & rules | `.work/meta/retrospective.md` |
| Release 过程记录 | `.work/07_release{,_v1_1,_v1_2,_v1_3,_v1_4}/` |
| Website 过程记录 | `.work/07_website/` |

## 冻结线 (不再推进)

多平台部署 (`archive/ai_platforms/`) 与日语納品 (`archive/jp_delivery/`) 已于 2026-06-15 收口冻结
(用户决策); 终态 Release `v1.4-company-release`. 不要再推进, 仅历史只读.

## Session Wrap-up (收尾)

When the user says **"收尾"**, **"wrap up"**, or **"提交收尾"**, execute the following checklist automatically:

**索引职责**: `.work/MANIFEST.md` = 结构 + 变更链 (不写状态); `.work/meta/worklog/<phase>.md` =
append-only 日志; `docs/PROGRESS.md` = **唯一**当前状态源; `CLAUDE.md` Key Paths = 长效路径指针.

1. **Review** what was done this session (read git diff + new files)
2. **Update index files** (按相关性): worklog append; `docs/PROGRESS.md` (phase 状态变了才动);
   `.work/MANIFEST.md` (目录结构 / chain 改了才动); `CLAUDE.md` Key Paths (新 key path 才加)
3. **Prune CLAUDE.md** — 按写作规则剪掉过期状态; 行数 ≤ 150
4. **Check Change Chains** — `knowledge_base/` 改了 → Chain D; plans 改了 → Chain E
5. **Link check** — `python3 tools/check_links.py` 末行 `live docs` 计数不高于基线 (`docs/PATH_MAP.md`)
6. **Commit + push** — single commit, `git push origin main`
7. **Report** — one-line summary of what was committed

Do NOT ask for confirmation on each step — just execute the full checklist and report at the end.

## Conventions

- Knowledge base content is in English (extracted from English PDF sources)
- Work logs, plans, and meta docs are in Chinese
- File status fields use format: `> 状态: **已完成** (date)` or `> 状态: 描述`
- When completing a task, follow Chain B (worklog/<phase>.md → 相应 _progress.json → docs/PROGRESS.md)
