# 自部署指引 — SDTM AI 知识库 v1.0

> 给想自己搭一套的同事. 4 平台均可单独部署, 30-60 分钟即可上线.

## 1. 我应该选哪个平台部署?

| 平台 | 部署时间 | 套餐 | 团队共享 |
|---|:---:|---|---|
| **NotebookLM** | ~30 min | Pro / Workspace | notebook 邀请 (50-source cap) |
| **Gemini Gems** | ~30 min | Advanced / Workspace | 个人不可直接共享, 要 Workspace |
| **ChatGPT GPTs** | ~45 min | Plus / Team / Enterprise | organization 内免审核, GPT Store 走 review |
| **Claude Projects** | ~60 min | Pro / Team / Enterprise | Team/Enterprise 共享, Pro 各自重部 |

部署视角挑选 (与 USER_GUIDE.zh.md §3 一致): 想最快 (~30 min) → NotebookLM 或 Gemini; 想最深 RAG → Claude Projects; 想团队共享 → ChatGPT GPTs; 想最强反虚构 → NotebookLM.

## 2. 4 平台部署教程 (选一个跟着做)

- **Claude Projects** → [./claude/tutorial.zh.md](./claude/tutorial.zh.md) (19 文件 + system_prompt + 24 题 smoke)
- **ChatGPT GPTs** → [./chatgpt/tutorial.zh.md](./chatgpt/tutorial.zh.md) (Custom GPT + 9 文件 + v2.2 system prompt + 17 题 smoke)
- **Gemini Gems** → [./gemini/tutorial.zh.md](./gemini/tutorial.zh.md) (Gem + 4 合并文件 + v7.1 system prompt + AHP 验收)
- **NotebookLM** → [./notebooklm/tutorial.zh.md](./notebooklm/tutorial.zh.md) (notebook + 42 sources + Custom mode instructions 8,925 chars + 三档分享)

## 3. 通用前置准备

1. 进入本目录 (公司云下载 release pack, 或 `git clone` 本仓库后进 `ai_platforms/release/v1.0/`). 各平台部署资产已就位在 `./{claude,chatgpt,gemini,notebooklm}/` (`system_prompt.md` 或 `instructions.md` + `uploads/` + `tutorial.<lang>.md`).
2. 准备账号 + 套餐 (按 §1 表格).
3. 打开 §2 对应 tutorial, 严格按章节顺序执行 (跳步会丢 system_prompt 守门规则).

## 4. 部署后验证 (smoke test)

部署完跑 `../DEMO_QUESTIONS.md` D0 + D1 + D5 三题快速验收 (5 分钟):

- **D0**: AESER 基础查询 (AE / Exp / C66742 NY) — 验基础 RAG.
- **D1**: GF 域 EGFR 场景 (GFGENSR / GFPVRID / GFGENREF / GFINHERT) — 验新域 + 多变量推理.
- **D5**: SUPPTS 前提纠错 — 验 anti-hallucination 守门 (主动识破 → TSVAL1-n).

3 题全 PASS = 部署成功. 1 题不 PASS, 看 `../KNOWN_LIMITATIONS.en.md` 排错: 优先检查 (a) system_prompt.md 是否完整粘贴未截断, (b) uploads/ 文件数和大小是否符合教程清单.

## 5. 升级 / 维护

release 包后续会更新: 每个 minor release (`../CHANGELOG.md` 标 v1.1 / v1.2) 或 SDTMIG 新版 (v3.5+) 时, Daisy 通过公司云分发新 release pack. 重传步骤: 拿到新 pack → 进对应平台子目录 (`./{claude,chatgpt,gemini,notebooklm}/`) → 删旧 uploads + 重传 → **完整复制粘贴新 system_prompt.md** (绝不能截断, 否则丢 AHP 守门规则, 例 Gemini v7.1 CO-1d SUPPQUAL 硬锚 + ChatGPT v2.2 v3.4 新域变量名校验). 回滚: 联系 Daisy 取历史 release pack.

## 6. 反馈

发现错误 / 幻觉: (1) 截图 + 留底完整问题原文 + AI 回答; (2) 附平台 + 版本 (例 "ChatGPT GPT v2.2 LIVE 2026-04-24") + 期望答案 (引 SDTMIG v3.4 章节号或 CDISC CT C-code) + 自部署版本号 + smoke 分数; (3) 邮件 Daisy / issue tracker / 部门群 @Daisy. 汇总到 `../CHANGELOG.md` 走下个 minor release.
