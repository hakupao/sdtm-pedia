# 07 Release v1.0 — 公司发布版 PLAN

> **Tier**: 2 重 (24 文件 / 三语 / OMC team 物理并行)
> **启动**: 2026-04-27
> **目标**: 一天内交付 release v1.0 给公司, 含 (1) 同事消费方手册 (2) 自部署教程 (3) 工作成果展示
> **状态**: Phase A 进行中

## 1. 三个交付目标

| # | 目标 | 主产物 |
|---|------|------|
| 1 | 同事直接用我部署好的 4 个实例 | `USER_GUIDE` + `DEMO_QUESTIONS` + 顶层 `README` |
| 2 | 同事看教程自己部署一套 | `self_deploy/` 4 平台 `tutorial.{zh,en,ja}.md` |
| 3 | 向公司展示工作成果 (技术能力) | `USER_GUIDE` 内嵌"项目背景与成果"段 (无独立 EXEC, 用户已确认) |

## 2. 三语策略

| 文档层 | zh | en | ja |
|---|:---:|:---:|:---:|
| 顶层 README | ✓ | ✓ | ✓ |
| USER_GUIDE | ✓ | ✓ | ✓ |
| self_deploy/README | ✓ | ✓ | ✓ |
| 4 × tutorial | ✓ | ✓ | ✓ (用户改"小白培训", 全 ja 化升级) |
| DEMO_QUESTIONS | 多语内嵌单文件 (英文 SDTM 题面 + 三语翻译题干) | | |
| KNOWN_LIMITATIONS | en 单一 | | |
| CHANGELOG | en 单一 | | |

## 3. 产出清单 (24 文件)

```
ai_platforms/release/v1.0/
├── README.{zh,en,ja}.md                        ⓵ 索引 (短)
├── USER_GUIDE.{zh,en,ja}.md                    ② 消费者主文档 (~3000 字)
├── DEMO_QUESTIONS.md                           ③ 10 题, 多语内嵌
├── KNOWN_LIMITATIONS.en.md                     ④ 单一英文
├── CHANGELOG.md                                ⑤ 单一英文
└── self_deploy/
    ├── README.{zh,en,ja}.md                    ⑥ 自部署索引 + 平台决策树
    └── {claude,chatgpt,gemini,notebooklm}_tutorial.{zh,en,ja}.md  ⑦ 4 × 3 = 12 文件
```

合计 12 zh + 6 en + 6 ja + 3 单一英文 = **27 文件** (修订: 含 4 tutorial × 3 lang = 12, 而非 12 总).

## 4. Phase 拆分

| Phase | 工作 | 终端配置 | 工时 |
|:---:|---|---|:---:|
| **A** | PLAN + 修过期标记 + DEMO + LIMITATIONS + CHANGELOG + 3 worker kickoff + CLAUDE.md routing | 主 session 1 个 (本次) | 30min |
| **B** | 3 worker zh 内容写作 (OMC team) | TeamCreate `sdtm-release-v1` + 3 workers parallel | ~3h |
| **C** | 12 翻译 fan-out (zh→en × 6 + zh→ja × 6) | 主 session 派 12 subagent 并发 | ~30min |
| **D** | 5 reviewer fan-out (en/ja/跨平台/DEMO/可读性) + Rule A N=3 抽检 | 主 session 派 5 subagent 并发 + fix loop | ~1h |
| **E** | RETROSPECTIVE.md + git tag + 索引同步 | 主 session | ~30min |
| **总** | | | **~5.5h** |

## 5. omc-teams tmux 配置 (Phase B) — 用户改 native team → omc-teams (tmux 进程级并行)

```
team_name: sdtm-release-v1
runtime: omc-teams (tmux pane × 3 claude CLI workers)
launch command: omc team 3:claude "Release v1.0 Phase B parallel writers. Each worker reads its assigned kickoff at .work/07_release/subagent_prompts/worker_{b,c,d}_*.md based on the task you claim. Self-contained instructions inside."
```

各 worker 自包含 kickoff 路径:
- `worker-b` (consumer-doc lane, ~3h): `.work/07_release/subagent_prompts/worker_b_consumer_doc.md`
  - files: USER_GUIDE.zh.md + 顶层 README.zh.md + self_deploy/README.zh.md
- `worker-c` (new-tutorials lane, ~3h): `.work/07_release/subagent_prompts/worker_c_new_tutorials.md`
  - files: chatgpt_tutorial.zh.md + gemini_tutorial.zh.md
- `worker-d` (adapt-tutorials lane, ~1h + 帮 c): `.work/07_release/subagent_prompts/worker_d_adapt_tutorials.md`
  - files: claude_tutorial.zh.md + notebooklm_tutorial.zh.md
  - bonus: 完事后帮 worker-c 写 chatgpt §7 排错 + §8 升降级

**完成信号** (各 worker 单行 echo, team-lead 通过 `omc team status` + tmux capture-pane 监控):
- SUCCESS: `WORKER_X_DONE: <files count> files written at <paths>`
- BLOCKED: `WORKER_X_BLOCKED: <reason>`

## 6. Rule D 隔离链 (release 独立计数)

| Slot | Phase | Agent | 备注 |
|:---:|---|---|---|
| writer-1 | B | `oh-my-claudecode:executor` (opus) ×2 + (sonnet) ×1 | 主创作 |
| translator-en | C | `oh-my-claudecode:executor` (sonnet) ×6 | en 翻译 |
| translator-ja | C | `oh-my-claudecode:executor` (sonnet) ×6 | ja 翻译 |
| **#R1** | D | `pr-review-toolkit:code-reviewer` | en 语言 + SDTM 保留审 |
| **#R2** | D | `oh-my-claudecode:critic` (opus) | ja 敬体一致 + 业界用词审 |
| **#R3** | D | `feature-dev:code-reviewer` | 4 tutorial 跨平台一致性审 |
| **#R4** | D | `oh-my-claudecode:verifier` | DEMO 答案保真审 (vs SMOKE_V4 evidence) |
| **#R5** | D | `oh-my-claudecode:critic` (opus 二轮) | 小白可读性审 (抽 2 tutorial) |
| Rule A 抽检 | D | 主 session 直审 | 12 翻译文件抽 N=3 双向回译 |

## 7. SDTM 术语保留白名单 (翻译时不动)

**绝不翻译** (保英文原样):
- 平台名: Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM / GPT Store
- 域 2 字符缩写: AE, CM, DM, LB, EX, VS, MB, IS, GF, CP, BE, BS, RELREC, RELSPEC, SUPPQUAL, SUPP--
- 变量名 (大写或带 prefix): AESER, AESEV, AETERM, AEDECOD, AEHLT, USUBJID, STUDYID, LBNRIND, LBORRES, GFTESTCD, GFGENSR, GFPVRID, GFGENREF, GFINHERT, CPTESTCD, CPCELSTA, BSTESTCD, ARMCD, ARM, ARMNRS, DSDECOD, DSCAT, RDOMAIN, IDVAR, IDVARVAL, QORIG, QEVAL, QNAM, QLABEL, QVAL, TSVAL1-TSVALn, AESTDTC, DTHDTC, EX*DTC...
- CT C-code: C66742, C66769, C78735, C78736, C66727, C66728, C181172, C181177, C181178, C142179, C124300...
- 概念缩写: SDTM, SDTMIG, ADaM, CDISC, CRF, EDC, FDA, NCI EVS, MedDRA, ISO 8601, RAG, JSON, XPT, NSV, RWD, SAE, AE, MH, CE, DV, IE, TS, TA, TE, TV, TI, EPOCH, PK, PGx, PROMIS, EORTC, SF-36, DAS28
- Core 属性值: Req / Exp / Perm
- 文件路径 / URL / 代码块 / 命令: 一律不译

**可翻译**: 解释性文字, 例: "Adverse Event domain" → "副作用领域 / 副作用ドメイン" 但保留 AE 缩写.

## 8. 不动清单 (workers 严禁碰)

- `ai_platforms/{platform}/current/` 一切已部署的 system_prompt.md / instructions.md / uploads/ — LIVE 状态, 不能动
- 4 平台 docs/ / dev/ / archive/ — 历史归档
- `.work/06_deep_verification/` — 当前另 5 终端 round 6 在跑
- 顶层 SMOKE_V4.md / SYNC_BOARD.md / README.md (release 完成后由主 session 一并同步, 不在 worker 范围)

## 9. 完成信号 (worker 单行 echo)

每 worker 完成后通过 `SendMessage` 报告 team-lead, 内容简明:
- 成功: `WORKER_X_DONE: <files written count> files at <paths>, ready for translation`
- 失败: `WORKER_X_BLOCKED: <reason>`
- 中途 status check: 主 session 主动 SendMessage 询问

主 session 收到 3 个 `WORKER_X_DONE` 后启动 Phase C.

## 10. 风险 + Mitigation

| 风险 | Mitigation |
|---|---|
| Worker 翻译 SDTM 术语 | Phase A 7 节白名单内嵌 worker prompt; Phase D Rule A 抽检兜底 |
| 跨 4 tutorial 结构漂移 | Phase A worker prompt 含**统一 10 章节 spec**; Phase D #R3 跨平台一致性审 |
| ja 翻译质量 | Phase D #R2 opus critic + 用户邀请 JP 母语同事 final 校对 (E 后异步) |
| Worker D 工作量轻不平衡 | Worker D kickoff 含 reassign 协议: 完事后领 worker C 章节 7+8 |
| 译文丢链接 | translator prompt 内嵌"代码块/URL 不动" 白名单 |
| 公司同事看不懂技术细节 | USER_GUIDE 写法限"小白可读"; #R5 抽审兜底 |

## 11. Phase E 产出 (Rule C 强制)

`RETROSPECTIVE.md` 三段 + git tag `v1.0-company-release` + 同步索引 (`MANIFEST.md` + `worklog.md` + `docs/PROGRESS.md` + `CLAUDE.md` Key Paths).

## 12. CLAUDE.md 临时路由规则 (Phase A 末加)

```
| `release worker b` / `release b 开始` | .work/07_release/subagent_prompts/worker_b_consumer_doc.md |
| `release worker c` / `release c 开始` | .work/07_release/subagent_prompts/worker_c_new_tutorials.md |
| `release worker d` / `release d 开始` | .work/07_release/subagent_prompts/worker_d_adapt_tutorials.md |
```

(用户用 OMC team 自动派, 路由规则保留作 fallback / 复盘记录, Phase E 末删除)

---

*绑定 personal rules A/B/C/D 全合规. 失败归档: `.work/07_release/evidence/failures/phase_X_attempt_Y.md`. Retro: `.work/07_release/RETROSPECTIVE.md` (Phase E).*
