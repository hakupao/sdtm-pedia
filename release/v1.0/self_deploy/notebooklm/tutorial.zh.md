# NotebookLM 部署教程 — SDTM 知识库发布版 v1.0

> release v1.0 自部署教程 (NotebookLM 1 notebook × 42 sources + Custom mode).
> 读完本教程: 30-60 分钟得到一个 NotebookLM notebook, in-KB-only 天然反虚构, 完整 17 题测试 15/17 通过 (88%) 基线.
> 信源: 项目仓库 ./ (instructions.md + uploads/ × 42).
>
> ℹ️ 本文件中所有 `../../../../notebooklm/dev/evidence/...` 路径指向项目内部 QA 证据 (由 Bojiang Zhang 保管), 不在本 release 包内. 如需详情请联系 Bojiang Zhang.

---

## 0. 前置要求

- [ ] **Google 账号与 NotebookLM 套餐** ([notebooklm.google.com](https://notebooklm.google.com)): **2026 年现行 NotebookLM 套餐结构 (Free / Plus / Pro 三档)**:

| 档位 | 套餐名 | Notebooks/用户 | Sources/notebook | 对话/天 |
|------|--------|---------------|------------------|---------|
| Free (Standard) | (个人 Google 账号) | 100 | **50** | 50 |
| Plus | Google One AI Premium (个人) | 200 | 100 | 200 |
| Pro | Workspace Enterprise / Education | 500 | 300 | 500 |

  本发布版 **42 sources** — **Free 档即可容纳** (50 cap 的 84%). **Plus / Pro 余量充足**.
  每个 source 字数上限: **500,000 words 或 200 MB/文件** (三档相同).
  本发布版最大 bucket: 302K words < 500K → 全档位安全.
- [ ] **Google 账号** (个人 Gmail 或 Workspace): 一个账号管所有 notebooks; 如未来做团队分享建议统一用 Workspace 账号
- [ ] **网页访问** [notebooklm.google.com](https://notebooklm.google.com): 本教程全程 Web UI 操作 (NotebookLM 无 consumer GA API)
- [ ] **本地 clone 本仓库**: 需要上传 `./uploads/*.md` 下的 **42 个 source 文件** + 贴 `./instructions.md` 到 Chat Custom mode

**关于"能力 vs 容量"**:
- 发布版使用 **42 sources** — Free 50 cap (84%) / Plus 100 cap (42%) / Pro 300 cap (14%). **三档均可容纳**, 稳定性建议 Plus 以上
- 总 words **1,582,085** (最大 bucket 302K < 500K/source cap, 0 over-cap / 0 missing)
- Chat Custom mode instructions.md: **8,925 Unicode chars — 实测可用 (2026-04), 建议保持 10K chars 以内**
- **覆盖范围**: 63/63 domains 全覆盖 / 176/176 Req 变量 ∅ gap (结构级 + 语义级双锚闭合) / 295 md 全入库分 42 concept bucket

---

## 部署流程概览

按实际 NotebookLM 现行 UI, 部署顺序必须是:

```
§1 新建 notebook (只填 Name)
       ↓
§2 上传 42 sources           ← 必须先上传
       ↓
§3 等 Indexing
       ↓
§4 配置 Custom Mode Instructions   ← 必须先有 sources 才能操作
       ↓
§5 Smoke Test
```

> **重要**: Custom mode (§4) 在 notebook 没有 sources 之前**无法**操作. 旧版"建好 notebook 立刻贴 prompt"的流程在现行 UI 行不通, 一定要先完成 §2.

---

## 1. 新建 NotebookLM notebook

1. 登录 [notebooklm.google.com](https://notebooklm.google.com) (用你的 Google 账号)
2. 点击 "**Create new notebook**" 按钮 (当前官方标签)
3. **命名建议**: `SDTM Knowledge Base` 或 `CDISC SDTM Expert`
4. **分享档位** (默认 Restricted, 稍后 §7 详解 2 档切换): 起步保持 Restricted, smoke test 通过再按场景切

> **注**: 现行 (2026 年) UI **没有 Description (描述) 输入框**. 只能设 Name. 旧教程的 "Description" 步骤已删除.

---

## 2. 上传 42 个 source 文件

1. notebook 左侧 "**Sources**" 面板, 点 "**Add**" 按钮 (无 + 号) → 弹出选择上传来源 (**Upload files / Google Drive / URL / 音频文件 / 粘贴文本** 任选)
2. 选 "**Upload files**" (或拖拽)
3. **批量选择** `./uploads/*.md` 共 **42 个文件** (01-42 numbered buckets, 不包含 MANIFEST.md — MANIFEST 是 source 清单文档不是 source 本身)
4. **等上传完成**: 42 个文件会一起 queue, Web UI 单批支持. 实测约 2-5 分钟全部传完

### 关键: 防 "indexing silent fail"

NotebookLM 官方承认有极小概率 indexing silent fail (文件传上去但没真正被 index). 防线:

- **UI tile 级 spot check**: 上传完扫一遍每个 source tile, 看缩略图 + 字数预估 是否合理. 任何 tile 显示 "0 words" 或 error 状态 → **删重传**
- **全部 42 tile 完整**: 一条不能少. 每条都要 "Indexed" 绿状态
- **点开若干 source 预览**: 抽样 5-10 个 source (首 source_01 + 末 source_42 + 随机几个) 点开看首段文字, 防 "上传成功但内容乱码"

本发布版上传时实测 42/42 全 indexed, 0 silent fail (上传 log: `../../../../notebooklm/dev/evidence/p3_2_upload_log.md`).

---

## 3. 等 Indexing

- NotebookLM indexing 比 Claude 快很多, 42 个 source 通常 **2-10 分钟**全部变 "Indexed" 绿状态
- UI 上 sources 面板每个文件旁边有状态图标:
  - 🟡 转圈 = indexing 中, 暂不能 chat
  - ✅ 绿勾 = indexed, 可 chat
  - **注**: 官方文档未明确图标样式 (🟡/✅) — 以上基于实测 UI, UI 改版时可能变化
- 全部 ✅ 后才进 §5 smoke test
- 如果 >30 分钟还有黄 loading, 很可能该 source silent fail → 按 §2 重传
- **同时你可以做**: 把 §4 的 Custom Mode Instructions 贴好 (前台操作). Indexing 是后台跑, 两件可并行

---

## 4. 配置 Custom Mode Instructions

NotebookLM **没有 System Prompt** — 唯一可 prompt engineer 的入口是 Chat 的 **Custom mode**. 本发布版提供 `./instructions.md` (8,925 Unicode chars, 89.25% 占用) 已经写好 SDTM 专家 prompt + 13 behavior rules + 锚点.

> **前提**: §2 已上传 sources. Chat 下的 Custom mode 入口要在 notebook 有 sources 后才可操作.

### 操作

1. 打开刚建好的 notebook, 确认 Sources 面板里 42 个 source 都在
2. 点击 Chat 面板内的**齿轮图标** → 打开 "**Configure Chat**" 菜单 → 在模式选择中选 "**Custom**" (默认是 "Default", 另有 "Learning Guide")
   > **注**: 2025/10 更新后, Custom mode 入口统一改为通过 "Configure Chat" 进入
3. **完整复制** `./instructions.md` 的全部内容 (不要截断)
4. 粘贴到 Custom goals 框里
5. **Save**

### 为什么 instructions.md 这么密

发布版 instructions.md 含:
- **13 条 behavior rules** — 优先级 / citation 强制 / 边界诚实 / 不脑补
- **SDTM 锚点** (高频易错点): AESER Core=Exp (非 Req) / LBNRIND 4 值 Y/N/U/NA 全写 / NY C66742 / ISO 8601 datetime / C-code 字面引用 / Day 1 无 Day 0 / RELREC+RELSPEC+RELSUB 三件套 / SUPP-- 结构
- **Authoritative layer 优先级**: `spec > ch04 > CT > assumptions > examples` (处理同一变量不同源冲突时按此优先级裁决)

**官方没有明文规定字符上限** (旧的 "10K char limit" 已从官方文档消失). 本 instructions.md 的 8,925 Unicode chars 实测可用 (2026-04). **建议保持 10K chars 以内**作为安全目标; headroom (~1,000 chars) 可再加 3-5 条自定义锚点.

### Custom mode 是按 chat 动态切的, 不锁 notebook 整体

每个 chat session 都可以独立切 Default / Learning Guide / Custom (UI level). 不会锁定整个 notebook. 如果你想验证:
1. 开一次 chat 切 "Learning Guide" 问 AE 域规则 → 会得到 Socratic 教学式回答
2. 再切回 "Custom" 问同一问题 → 会得到结构化 SDTM 专家回答
3. 同一 source set, 不同输出风格

---

## 5. Smoke Test (3 题 sanity, ~5 分钟)

用 3 个基础题验证 notebook 底座稳, 任何 1 题 FAIL 不要继续.

| # | 问 | 期望答 | 验证点 |
|---|---|---|---|
| 1 | `AESER 的 Core 属性是 Req 还是 Exp?` | **Exp (非 Req)** | 最高频易错点; answer 必含 `[08_ev_adverse_ae.md]` 类 citation |
| 2 | `LBNRIND 的 submission values 都有哪些?` | **Y / N / U / NA** (4 值全写, 不写 LOW/HIGH/WITHIN REF) | 带 Extensible=Yes + `[33_ct_general.md]` citation |
| 3 | `CMINDC 用于什么场景? 和 CMTRT 关系?` | **CMINDC = indication/reason for concomitant med; CRF "Other, specify" 走 SUPPCM 工作流; 不与 CMTRT 融合** | 必含 citation + SUPPCM 提及 |

**3/3 PASS** → 进 §6 可选完整回归.

**1 题 FAIL** → 排错:
- answer 没 citation → Custom mode 没生效, 回 §4 重贴 instructions.md
- answer 说变量不在 KB → source 漏了或 indexing fail, 回 §2 重传对应 source
- answer 内容错 (如 AESER=Req) → instructions.md 贴不全, 回 §4 核对字数 8,925

### Release v1.0 完整 demo
除本教程的 sanity 3 题, release v1.0 还提供 10 题完整 demo, 见 [../../DEMO_QUESTIONS.zh.md](../../DEMO_QUESTIONS.zh.md). 注: NotebookLM 是 in-KB-only 设计, Q11/Q12 这类 supplemental topics 会 PUNT (拒答), 这是**正确反虚构行为**, 不是 bug, 见 [../../KNOWN_LIMITATIONS.zh.md](../../KNOWN_LIMITATIONS.zh.md) §L4-NB5.

---

## 6. 完整回归测试 (可选, 17 题, ~30 分钟)

本发布版完整测过 17 题题库 (含 3 道反虚构题), 实测 **15/17 通过 (88.2%)**, 3 道反虚构题全部识破 — 在 4 平台中并列最强 (NotebookLM in-KB-only 架构天然反虚构). 你可以复跑这 17 题, 验证自己部署的 notebook 同样稳.

- **题库**: [`../../../../SMOKE_V4.md`](../../../../SMOKE_V4.md) §2
- **逐题答案 + verdict**: `../../../../notebooklm/dev/evidence/smoke_v4_answers/*.md`
- **总结报告**: `../../../../notebooklm/dev/evidence/smoke_v4_results.md`
- **合格阈**: ≥12/17 (71%) R1 首测容错

### 17 题分布

| 类别 | 题号 | 测什么 |
|------|------|--------|
| Sanity | sanity_01-03 | 底座稳 (§5 相同) |
| v3.4 新域 | Q1-Q3 | GF / CP / BE+BS+RELSPEC |
| 域边界 | Q4-Q5 | LB/MB/IS / FA/QS/CE |
| Timing | Q6-Q7 | PK 采血四件套 / Partial date |
| CT | Q8 | Extensible vs Non-Extensible |
| Pinnacle 21 | Q9 | 常见 FAIL 分类 (NotebookLM 预期 PUNT safety-correct) |
| SUPP 深化 | Q10 | QORIG/QEVAL + SUPPTS 前提纠错 |
| Bonus | Q11-Q14 | Dataset-JSON / CT 版本 / RWD / AE+CE+MH+DS 联动 |
| **AHP (anti-hallucination)** | AHP1-3 | **变量虚构 / 跨域虚构 / deprecated 虚构** — in-KB-only 天然优势测试 |

### 预期表现

- Q1-Q8 / Q10 / Q14 / AHP1-3 应 PASS (90%+)
- Q9 **预期 FAIL** (safety-correct PUNT, in-KB-only 架构天然找不到 Pinnacle 21 外部文档 — 非能力 FAIL)
- Q11-Q12 **预期 PARTIAL** (supplemental topics, in-KB 覆盖不全)
- 3 道反虚构题应全识破 — NotebookLM 架构天然反虚构

---

## 7. 分享档位切换 (2 档) + Featured Notebooks

NotebookLM 支持同一 notebook 在分享档位间动态切换, 不需要建多个 notebook. 切换实测 2026-04-23 VERIFIED + 深化 (`../../../../notebooklm/dev/evidence/share_level_toggle_drill.md`).

### 2 档语义

| 档位 | 访问规则 | 适用场景 |
|------|----------|----------|
| **Restricted** (默认) | 仅 owner + 邀请列表里的 Google 账号 | 个人用 / 小圈团队 |
| **Anyone with a link** | 有链接的任何 Google 账号登录即访问 | 定向发布 / 团队公告 |

> 当前 UI 的分享档位选项中不存在 "Public". 旧教程中的 "Public 档" 描述已删除.

### 切换步骤

1. notebook 右上角 "**Share**" 按钮 → 打开 share panel
2. 选想要的档位, 点 "**Copy link**" 生成访问链接
3. 回切 Restricted 会**立即 revoke** 之前的 link (实测 PASS, 无 caching 残留)

### Featured Notebooks (公开画廊)

- 策展列表 (研究者 / 出版社 / 非营利组织等), 由 Google 选定 — 普通用户无法申请
- **Workspace Enterprise / Education 账号不支持 Featured Notebooks 功能**
- 旧教程的 "Public 档" 概念最接近 Featured Notebooks, 但不是用户可自行切换的选项

### Free tier 50-cap 只套 Restricted+Invite 场景

- 若 Restricted 档 + invite 了 Free tier Gmail 小号, 小号**可能只能看前 50 source**
- 本发布版 42 sources ≤ 50, **无影响**
- 未来若扩到 ≥ 51 sources, 且需要 Free tier viewer 访问, 要 A/B/C 解读实测 (见 PLAN §3.3)

---

## 8. 排错手册

| 症状 | 诊断 | 修 |
|------|------|-----|
| 答案没 citation | Custom mode 没生效 | 回 §4 重贴 instructions.md, 确认 Save 绿勾 |
| 答案说变量不在 KB (实际应在) | source indexing silent fail | §2 找对应 source tile 看状态, 黄 loading 超时 → 删重传 |
| 答案把 AESER 答成 Req | instructions.md 贴不全被截断 | wc -m 原文 8925, 若贴完后字符数显著少 → 重贴 |
| 17 题 Q9 FAIL (架构限制) | **预期** in-KB-only 架构限制, safety-correct PUNT | 不要改 instructions.md 加"允许外推", 会降反虚构优势 |
| AHP1-3 出现虚构 (如答 LBCLINSIG 存在) | instructions.md "边界诚实" 锚点失效 | 回 §4 核对 instructions.md 完整; 或切换 Chat mode 再切回 Custom 刷新 |
| Pro viewer 在 **Anyone with a link** 档看不全 source | 不应该, 此档位不套 Free tier cap | Google 账号登录状态 check; share link 重生成 |
| 小表渲染漂移 (单行错位) | F-1-recurring 已知现象, 不扣语义分 | 重发同问题通常刷新; retry 幂等性不强制 |
| citation dropout (业务场景题) | F-3 系统性弱点 (T2 题型偏向) | 答案内容通常对, citation 偶失; 不扣语义分 |
| Chat 面板找不到 "Configure Chat" 菜单 / 无法点开 | §2 sources 还没上传完 | 检查 Sources 面板里是不是 42 个 source 都在; 若没, 先回 §2 完成上传 |

---

## 9. 升级 / 维护

### 扩容 (42 → N sources)

- Pro cap 300 source, 当前用 14% 有 8 slot + 258 Pro cap headroom
- 若 KB 扩展 (如加 SDTMIG 下个版本 v3.5 / 新 domain), 在 `../../../../notebooklm/dev/scripts/bucket_config.json` 加 bucket 43+ → 跑 `merge_sources.py` → 上传新 source 增量
- 注意: ≥ 51 sources 会触发 Free tier viewer 50-cap, 要重做 Free tier 实测

### Free tier 兼容性 — 无需改动

- Free tier 上限: 100 notebooks × 50 sources × 500K words/source × 50 chat/day × 3 audio/day
- **本发布版在 Free tier 下可直接运行**: 42 sources ≤ 50 cap, 最大 bucket 302K < 500K/source cap → **无需重切 bucket**
- 不需要重切或重上传. Free / Plus / Pro 三档部署步骤完全相同.

### instructions.md 微调

- **官方没有明文规定字符上限** (旧的 "10K char limit" 已从官方文档消失). 本 instructions.md 的 8,925 chars 实测可用 (2026-04). **建议保持 10K chars 以内**作为安全目标 (~1,075 chars headroom 可加 3-5 锚点)
- 加锚点时跟 CLAUDE.md + RETROSPECTIVE.md R-NBL-3 一起更新
- 贴入前用 wc -m 确认字符数

---

## 10. 后续路径

### 10.1 立即可用

- 问任何 SDTM 变量定义 / Core 属性 / codelist 值
- 问域边界 (LB vs MB vs IS / FA vs QS vs CE)
- 问 Timing (--TPT 四件套 / Partial date)
- 问 SUPPQUAL 机制 / RELREC 三件套
- **给错前提**希望 NotebookLM 纠错 (AHP 强项)

### 10.2 已知限制 (in-KB-only 架构)

NotebookLM 强约束只能从 sources 回答, 不访问训练数据 / web. **这是优势 (AHP) 也是限制**:

- Pinnacle 21 报告分类 → **PUNT**
- Dataset-JSON / XPT v5 比较 → supplemental topic PUNT (部分分支)
- RWD (Claims / EHR) 特有 SUPP 字段 → PUNT
- CT 版本锁定 operational milestones → PUNT 部分分支

如果你需要这些, 用 Claude / ChatGPT / Gemini 任一平台互补 (本项目同批部署).

### 10.3 ICEBOX (post-project optional)

PLAN §10 保留的 **Studio 面板 (2025/7 改版) 4 块瓷砖**:
- **Audio Overviews** × N 期 (SAFETY / EFFICACY / PK Deep Dive podcast, 每期 30-45 min)
- **Video Overviews** (2025/7 新增, Audio 的视频版)
- **Mind Maps**: 63 domain 跨域关系 + RELREC/SUPPQUAL 覆盖
- **Reports** (旧 Study Guide 已并入此 Reports 瓷砖): AE / LB / CM Socratic 引导

触发条件: 你主动提出"回头精雕 Studio 4 块瓷砖". 不触发不影响主 retro + 本教程 FINAL.

### 10.4 相关文档

| 文档 | 路径 | 用途 |
|------|------|------|
| **RETROSPECTIVE (本平台)** | `../../../../notebooklm/docs/RETROSPECTIVE.md` | Rule C 三段 + pivot 案例 + _template/ 补丁 |
| **跨 4 平台 Phase 5 retro** | `../../../../retrospectives/PHASE5_RETROSPECTIVE.md` | v1.0 FINAL 2026-04-24 Bojiang Zhang 认可 4 平台 sign-off |
| **PLAN** | `../../../../notebooklm/docs/PLAN.md` | 662 行 v2.2 (架构 pivot 后完整 plan) |
| **完整 17 题测试结果** | `../../../../notebooklm/dev/evidence/smoke_v4_results.md` + `smoke_v4_answers/` | 17 题逐题 verdict |
| **2 档切换 evidence** | `../../../../notebooklm/dev/evidence/share_level_toggle_drill.md` | v1.0 FINAL 6 子步 + 旧 "Public 档" 不存在的验证 |
| **v1→v2 架构 pivot 记录** | `../../../../notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` | 关键教训: Writer 叙事合成伪约束 |
| **reviewer 报告** | `../../../../notebooklm/dev/evidence/phase5_retrospective_reviewer.md` | v0.2 post-fix 独立审 10 行动项 |

---

## 附: 部署后自查清单

部署完走一遍以下清单 (顺序与实际 UI 流程对齐):

- [ ] notebook 新建, 命名 `SDTM Knowledge Base`
- [ ] 42 个 source 上传 + 全 ✅ Indexed
- [ ] Chat Custom mode 贴了 instructions.md 全文 (8,925 chars)
- [ ] Smoke 3 题 (AESER Core / LBNRIND 4 值 / CMINDC 场景) 3/3 PASS
- [ ] (可选) 完整 17 题测试 ≥ 12/17 PASS
- [ ] 分享档位切换验证 ≥ 2 档 (至少 Restricted 和 Anyone with a link)
- [ ] 已将 notebook URL 共享给团队 (使用 Anyone with a link 分发时)
- [ ] 读完本教程 §10.2 已知限制, 不要把 Pinnacle 21 之类需求硬推到 NotebookLM

---

*v1.2 — 2026-05-11 — 部署步骤改为对齐实 UI 流程 (上传 → Indexing → Custom mode 顺序; 无 Description 字段). v1.1 (UI 术语 2026 同步) 已内含.*
*本平台独立 retro 见 ../../../../notebooklm/docs/RETROSPECTIVE.md ; release v1.0 总览见 ../README.zh.md*
