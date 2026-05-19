# SMOKE_V4 R3 — kickoff (v1.1 deployed test)

> 触发: 2026-05-16 用户 ack 全量 R3 + Chrome MCP driver browser + 全部部署后一次跑
> 上一版 R1+R2 retrospective: `ai_platforms/retrospectives/{R1_RETROSPECTIVE,R2_RETROSPECTIVE}.md`
> 题库来源: `ai_platforms/SMOKE_V4.md §2` (17 题 = Q1-Q14 + AHP1-3)
> 评分判据: `ai_platforms/SMOKE_V4.md §3` (PASS / PARTIAL / FAIL)

## R3 vs R1 关键不同

| 维度 | R1 (baseline) | R3 (v1.1 post-deploy) |
|------|---------------|----------------------|
| 触发 | 4 平台首测 baseline | v1.1 内容 refresh 后回归 |
| 部署版本 | v2.6 Claude / v2.2 ChatGPT / v6 Gemini / v2 NotebookLM | 同上 + 06 修复 KB + Gemini v7.1 + DI domain |
| 期望 | 各平台第一次得分 | **回归无衰减** + 06 修复的题 (PC RELREC / TA / DI) 期望改善 |
| 分数门槛 | Claude ≥10/13 (77%), ChatGPT ≥12/17 (71%), Gemini ≥9/13 (70%), NotebookLM ≥11/13 (85%, R1 容错 ≥10/13) | 同 R1 门槛 |

## 4 平台跑顺 (per SMOKE_V4 §1 推荐, 用户 2026-04-22 决策)

> 跨平台公共题 Q11-Q14 / AHP1-3 各平台跑一遍, 容错 (PASS+ / PARTIAL / PUNT 都接受)

1. **NotebookLM 先** (RAG 限制最严, 测能力下限)
2. **Gemini 第二** (R1 失败大头, v7.1 修复后最大悬念)
3. **ChatGPT 第三** (R1 PASS, 验回归无衰减)
4. **Claude 最后** (R1 17/17, 主要测有无升级 + AHP 表现)

## 每题 cowork 流程 (Chrome MCP driver 模式)

> **2026-05-19 新增: 并行方法已 dry-run 验证可用**, 见 `r3_orchestration_parallel.md` (4 平台 fire-and-forget + 并行等待, ~2.5× 提速).
> 下面的串行流程保留作 **fallback** (并行失败 / Chrome tab 严重 throttle 时降级用).


1. 主 session (我) 从 SMOKE_V4 §2 取下一题文本
2. `mcp__chrome-devtools__select_page` 切到对应平台标签
3. `mcp__chrome-devtools__take_snapshot` 拿当前 DOM, 找输入框 uid
4. `mcp__chrome-devtools__fill <input_uid> <题文>` 填入
5. `mcp__chrome-devtools__click <send_button_uid>` 发送
6. `mcp__chrome-devtools__wait_for "回答结束"` 或定时 poll
7. `mcp__chrome-devtools__take_snapshot` 抓 raw 回答
8. 我按 SMOKE_V4 §3 判据打分 → 写 `evidence/<platform>/q<NN>.md`
9. 更新 `r3_matrix.md` 该 cell

## 题清单 (17 题, 概要)

| # | 题 | 主域 / 主考点 | 期望 v1.1 improvement |
|:-:|----|--------------|------|
| Q1 | GFGENE / GFINHERT 拼写 + Core | GF (v3.4 新域) | ChatGPT v2.2 已修过 R1 Q1 拼写; Gemini v7.1 CO-4 |
| Q2 | CP 细胞表型 | CP (v3.4 新域) | 无 06 直接修复, 但 CP/assumptions 改了 1 行 |
| Q3 | DM ARMCD / ACTARMCD | DM | v7 CO-1c ARMCD-null + ARMNRS C142179 已 LIVE |
| Q4 | 微生物归域 (IS/MB) | IS, MB | 无 06 改 |
| Q5 | 多场景归域 (FA/QS/CE) | FA/QS/CE | 06 FA/assumptions + FA/examples 改 → 期望提升 |
| Q6 | PK 时间窗 (PCTPT/PCTPTREF) | PC | 无 06 直接, PC/assumptions 改 |
| Q7 | DTC imputation | timing | 无 06 改 |
| Q8 | AE / SUPP-- 边界 | AE / SUPPQUAL | 无 06 改, v7.1 CO-1d SUPP-- Core LIVE |
| Q9 | Pinnacle 21 错误分类 | meta | 无 06 改 |
| Q10 | SUPPTS 前提纠错 (AHP) | TS / SUPP | v7.1 CO-1d scope 加 SV; AHP probe |
| Q11 | 罕见 codelist 跨域 | terminology | 无 06 改 |
| Q12 | TI/TE Trial Design supplemental | Trial Design | 06 TI/TS/TU assumptions 改 → 期望提升 |
| Q13 | observational study ARMCD null | DM | v7 CO-1c LIVE (R1 答 "NOTASSGN" 错; R2 已修) |
| Q14 | RELREC 选择 (AE↔CM) | RELREC | 无 06 直接修复, 但 KB 改 |
| **AHP1** | NSV (non-standard variable) attention gap | meta | Gemini R1 全 FAIL; v7.1 CO-1d L65 dual-grep clause LIVE |
| **AHP2** | 虚构变量 LBNRIND | LB | Gemini R1 FAIL; v7.1 CO-5 AHP-V1 LIVE |
| **AHP3** | AEDECOD 绑 MedDRA 边界 | AE | Gemini R1 FAIL; v7.1 CO-5 LIVE |

## R3 完成后 (写在哪)

1. 每题 evidence → `.work/07_release_v1_1/r3/evidence/<platform>/q<NN>.md`
2. R3 完整矩阵 → `.work/07_release_v1_1/r3/r3_matrix.md` (17 × 4 = 68 cell)
3. R3 RETROSPECTIVE → `.work/07_release_v1_1/r3/R3_RETROSPECTIVE.md`
4. SMOKE_V4.md §3 跨平台对比矩阵更新到 R3 结果
5. ai_platforms/SYNC_BOARD.md append R3 result row

## 用户 trigger

部署 4 平台完后, 发: **"R3 开始"** + 标签页打开状态 (e.g. "chrome 已开 4 个标签: chatgpt / gemini / claude / notebooklm 都登录了"), 主 session load chrome-devtools MCP 开跑.
