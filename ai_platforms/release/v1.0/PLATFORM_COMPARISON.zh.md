---
lang: zh
slug: platform-comparison
order: 20
title: "4 平台多维对比"
---

# 4 平台多维对比

> 横向对比 4 平台 9 个维度. 数据快照: 2026-04-27 v1.0.

## 1. 评测得分 (smoke v4 / 17 题)

| 平台 | 得分 | 版本 | 主要失分点 |
|---|:---:|:---:|---|
| Claude Projects | 17/17 (100%) | v2.6 | 无 |
| ChatGPT GPTs | 16.5/17 (97%) | v2.2 LIVE | Q1 GFINHERT 拼写 (post v2.2 已修); 长尾 chunk 表格中段可能 miss |
| Gemini Gems | 16/17 (94%) | v7.1 LIVE | Q10 SUPP-- Core anchor (post v7.1 已修); R1 65% → R2 94% (v6→v7 升级) |
| NotebookLM | 15/17 (88%) | v1.0 / Custom mode | Q9 Pinnacle 21 / Q11 Dataset-JSON / Q12 CT version 三题 PUNT (in-KB-only 架构限制, 安全行为非 bug) |

## 2. 容量上限

| 平台 | 容量上限 | 当前用量 | 余量 |
|---|---|---|---|
| Claude Projects | 1.29M tokens (Pro 软上限附近) | 19 文件 / 77% | ~23%, 加新文件需先降级低优先 |
| ChatGPT GPTs | 20 文件硬上限 | 9 文件 (合并后, 如 04_domain_specs_all.md) | 11 文件 headroom |
| Gemini Gems | 1M tokens 上下文窗口 | 4 文件 (最激进合并) | 窗口余量充足, 冷启动首 token 略慢 |
| NotebookLM | 50 source 硬上限 (Pro 套餐) | 42 source | 8 source headroom |

## 3. 团队共享方式

| 平台 | 共享方式 | 是否需审核 |
|---|---|---|
| Claude Projects | Organization / Project 邀请 (Team / Enterprise 套餐共享 Project; Pro 用户需各自重新部署) | 不适用 (内部直接邀请) |
| ChatGPT GPTs | Custom GPT 分享至 organization (免审核) 或发布 GPT Store (走 OpenAI review) | 仅 Store 发布需审核 |
| Gemini Gems | Workspace 套餐: Daisy 直接分享; 个人账号: 同事各自自部署 (粘贴完整 v7.1 system prompt) | 不适用 |
| NotebookLM | 邮件邀请加入 notebook (Pro / Workspace), 或同事自建 (50-source cap) | 不适用 |

## 4. 套餐要求

| 平台 | 支持套餐 | Free 是否可用 |
|---|---|:---:|
| Claude Projects | Claude Pro / Team / Enterprise | 否 |
| ChatGPT GPTs | ChatGPT Plus / Team / Enterprise | 否 |
| Gemini Gems | Gemini Advanced 个人 / Google Workspace | 否 |
| NotebookLM | NotebookLM Pro / Google Workspace | 否 (50-source cap 仅 Pro/Workspace 套餐) |

## 5. 联网能力

| 平台 | 联网能力 | 默认状态 |
|---|---|---|
| Claude Projects | 可手动开启 web search | 默认关闭, 用户按需切 |
| ChatGPT GPTs | 可手动开启 web browsing | 默认关闭, 用户按需切 |
| Gemini Gems | 可手动开启 (Google Search 集成) | 默认关闭, 用户按需切 |
| NotebookLM | 严格 in-KB-only (仅 42 source 内, 不联网) | 设计如此, 非 bug; 跨 source 外问题主动 PUNT |

## 6. 反虚构倾向

| 平台 | 反虚构强度 | 机制 |
|---|:---:|---|
| Claude Projects | 强 | 多步推理 + system prompt anti-fabrication anchor + Stage 6 Deferred Stub 规则 |
| ChatGPT GPTs | 中 | system prompt 引导 + post v2.2 GFINHERT 精确变量校验; 长尾 chunk 偶尔 miss |
| Gemini Gems | 偏强 (post v7.1) | v6→v7 升级带 AHP guardrail, R1→R2 评分从 65% 升至 94%; 同事部署须完整粘贴 v7.1 system prompt |
| NotebookLM | 最强 | in-KB-only 架构天然反虚构; 不在 42 source 内宁可 PUNT 也不编造; inline citation 反查 |

## 7. 文件数限制

| 平台 | 文件数限制 | 当前文件数 |
|---|---|:---:|
| Claude Projects | 软上限受 token 容量约束 (~77% 已用 / 1.29M tokens) | 19 |
| ChatGPT GPTs | 20 文件硬上限 | 9 |
| Gemini Gems | 无显式文件数限制 (受 1M token 窗口约束) | 4 |
| NotebookLM | 50 source 硬上限 (Pro) — 详见 §2 | 42 |

## 8. 最强场景

| 平台 | 最强场景 |
|---|---|
| Claude Projects | 精确变量 + 多步推理 (Core + C-code + 跨变量, 例 PCTPT 五件套); 错前提纠错 (SUPPTS); 域边界判定 |
| ChatGPT GPTs | 全量域查询; 团队共享 / 发布 GPT Store; 组织内分享免审核 |
| Gemini Gems | 一次性塞大量上下文 / 跨域模式比对; 长会话; 大范围探索; 4 文件深度合并 |
| NotebookLM | 强反虚构 (审计 / 合规); inline citation 反查; 拒答优于编造; 跨域死亡日级对齐与 v3.4 新域 PASS+ |

## 9. 最弱场景

| 平台 | 最弱场景 |
|---|---|
| Claude Projects | 实时联网 (FDA / Pinnacle 21 需手动核 cdisc.org); 超大批量域对比; 容量已 77% 接近 Pro 软上限 |
| ChatGPT GPTs | 多步推理略弱于 Claude; Free 账号找不到入口; 长尾 chunk 表格中段可能 miss |
| Gemini Gems | 个人账号不能直接团队共享 (要 Workspace); 同事自部署须完整粘贴 v7.1 system prompt 否则丢 AHP guardrail |
| NotebookLM | 不在 42 source 内的题 (实时 Pinnacle 21 / breaking news / Dataset-JSON v1.1 / CT version locking + MedDRA) 主动 PUNT — 设计如此, 非 bug |

---
*v1.0 — 2026-04-27 — 维护者: Daisy*
