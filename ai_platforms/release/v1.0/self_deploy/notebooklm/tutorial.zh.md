# NotebookLM 部署教程 — SDTM 知识库发布版 v1.0

> release v1.0 自部署教程 (NotebookLM 1 notebook × 42 sources + Custom mode).
> 读完本教程: 30-60 分钟得到一个 NotebookLM notebook, in-KB-only 天然反虚构, 完整 17 题测试 15/17 通过 (88%) 基线.
> 信源: 项目仓库 ./ (instructions.md + uploads/ × 42).
>
> ℹ️ 本文件中所有 `../../notebooklm/dev/evidence/...` 路径指向项目内部 QA 证据 (由 Bojiang Zhang 保管), 不在本 release 包内. 如需详情请联系 Bojiang Zhang.

---

## 0. 前置要求

- [ ] **Google AI Pro 订阅** (订阅页 [ai.google.com](https://ai.google.com)): 本部署 42 sources, 在 Pro 套餐限额内绰绰有余 (Pro 上限远超本项目用量). Free tier 50-source 上限刚好够装, 也能跑, 但 Pro 更稳. 详细各项 cap (notebooks / sources / words / chat / audio) 见 [`../../notebooklm/docs/PLAN.md`](../../notebooklm/docs/PLAN.md) §A
- [ ] **Google 账号** (个人 Gmail 或 Workspace): 一个账号管所有 notebooks; 如未来做团队分享建议统一用 Workspace 账号
- [ ] **网页访问** [notebooklm.google.com](https://notebooklm.google.com): 本教程全程 Web UI 操作 (NotebookLM 无 consumer GA API)
- [ ] **本地 clone 本仓库**: 需要上传 `./uploads/*.md` 下的 **42 个 source 文件** + 贴 `./instructions.md` 到 Chat Custom mode

**关于"能力 vs 容量"**:
- 发布版占用 **42/300 = 14%** Pro source slot (远低 cap, 8 slot headroom 未来扩展可容)
- 总 words **1,582,085** (最大 bucket 302K < 500K/source cap, 0 over-cap / 0 missing)
- Chat Custom mode instructions.md **8,925 Unicode chars / 10,000 char limit = 10.75% headroom**
- **覆盖范围**: 63/63 domains 全覆盖 / 176/176 Req 变量 ∅ gap (结构级 + 语义级双锚闭合) / 295 md 全入库分 42 concept bucket

---

## 1. 新建 NotebookLM notebook

1. 登录 [notebooklm.google.com](https://notebooklm.google.com) (用你的 Pro 订阅 Google 账号)
2. 左上角点 "**+ New notebook**" 或 "**Create new**"
3. **命名建议**: `SDTM Knowledge Base` 或 `CDISC SDTM Expert`
4. **Description** (可选, 在 notebook 设置里填): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards v3.4 IG. 42 concept-clustered sources covering 63 domains + 176 Req variables + chapters + terminology + examples. Answers variable definitions, Core attributes, codelist terms, cross-domain relationships, SUPPQUAL mechanics.`
5. **分享档位** (默认 Restricted, 稍后 §8 详解 3 档切换): 起步保持 Restricted, smoke test 通过再按场景切

---

## 2. 配置 Chat Custom mode (instructions.md)

NotebookLM **没有 System Prompt** — 唯一可 prompt engineer 的入口是 Chat 的 **Custom mode** (10K char limit). 本发布版提供 `./instructions.md` (8,925 Unicode chars, 89.25% 占用) 已经写好 SDTM 专家 prompt + 13 behavior rules + 锚点.

### 操作

1. 打开刚建好的 notebook
2. 右上角 Chat 区域找 "**Configure**" 或齿轮图标 → 选 "**Custom**" mode (默认是 "Default" / 另有 "Learning Guide")
3. **完整复制** `./instructions.md` 的全部内容 (不要截断)
4. 粘贴到 Custom goals 框里
5. **Save**

### 为什么 instructions.md 这么密

发布版 instructions.md 含:
- **13 条 behavior rules** — 优先级 / citation 强制 / 边界诚实 / 不脑补
- **SDTM 锚点** (高频易错点): AESER Core=Exp (非 Req) / LBNRIND 4 值 Y/N/U/NA 全写 / NY C66742 / ISO 8601 datetime / C-code 字面引用 / Day 1 无 Day 0 / RELREC+RELSPEC+RELSUB 三件套 / SUPP-- 结构
- **Authoritative layer 优先级**: `spec > ch04 > CT > assumptions > examples` (处理同一变量不同源冲突时按此优先级裁决)

**10.75% headroom** 留给你后续微调 (~1,000 char 可以加 3-5 条你自己的新锚点). 超过 10K 会被 NotebookLM 截断, 不要贴超.

### Custom mode 是按 chat 动态切的, 不锁 notebook 整体

每个 chat session 都可以独立切 Default / Learning Guide / Custom (UI level). 不会锁定整个 notebook. 如果你想验证:
1. 开一次 chat 切 "Learning Guide" 问 AE 域规则 → 会得到 Socratic 教学式回答
2. 再切回 "Custom" 问同一问题 → 会得到结构化 SDTM 专家回答
3. 同一 source set, 不同输出风格

---

## 3. 上传 42 个 source 文件

1. notebook 左侧 "**Sources**" 面板, 点 "**+ Add**"
2. 选 "**Upload**" (或拖拽)
3. **批量选择** `./uploads/*.md` 共 **42 个文件** (01-42 numbered buckets, 不包含 MANIFEST.md — MANIFEST 是 source 清单文档不是 source 本身)
4. **等上传完成**: 42 个文件会一起 queue, Web UI 单批支持. 实测约 2-5 分钟全部传完

### 关键: 防 "indexing silent fail"

NotebookLM 官方承认有极小概率 indexing silent fail (文件传上去但没真正被 index). 防线:

- **UI tile 级 spot check**: 上传完扫一遍每个 source tile, 看缩略图 + 字数预估 是否合理. 任何 tile 显示 "0 words" 或 error 状态 → **删重传**
- **全部 42 tile 完整**: 一条不能少. 每条都要 "Indexed" 绿状态
- **点开若干 source 预览**: 抽样 5-10 个 source (首 source_01 + 末 source_42 + 随机几个) 点开看首段文字, 防 "上传成功但内容乱码"

本发布版上传时实测 42/42 全 indexed, 0 silent fail (上传 log: `../../notebooklm/dev/evidence/p3_2_upload_log.md`).

---

## 4. 等 Indexing (不用真等)

- NotebookLM indexing 比 Claude 快很多, 42 个 source 通常 **2-10 分钟**全部变 "Indexed" 绿状态
- UI 上 sources 面板每个文件旁边有状态图标:
  - 🟡 转圈 = indexing 中, 暂不能 chat
  - ✅ 绿勾 = indexed, 可 chat
- 全部 ✅ 后才进 §5 smoke test
- 如果 >30 分钟还有黄 loading, 很可能该 source silent fail → 按 §3 重传
- **同时你可以做**: 把 §2 instructions.md 贴好 (前台操作), indexing 是后台, 两件并行

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
- answer 没 citation → Custom mode 没生效, 回 §2 重贴 instructions.md
- answer 说变量不在 KB → source 漏了或 indexing fail, 回 §3 重传对应 source
- answer 内容错 (如 AESER=Req) → instructions.md 贴不全, 回 §2 核对字数 8,925

### Release v1.0 完整 demo
除本教程的 sanity 3 题, release v1.0 还提供 10 题完整 demo, 见 [../DEMO_QUESTIONS.md](../DEMO_QUESTIONS.md). 注: NotebookLM 是 in-KB-only 设计, Q11/Q12 这类 supplemental topics 会 PUNT (拒答), 这是**正确反虚构行为**, 不是 bug, 见 [../KNOWN_LIMITATIONS.en.md](../KNOWN_LIMITATIONS.en.md) §L4-NB5.

---

## 6. 完整回归测试 (可选, 17 题, ~30 分钟)

本发布版完整测过 17 题题库 (含 3 道反虚构题), 实测 **15/17 通过 (88.2%)**, 3 道反虚构题全部识破 — 在 4 平台中并列最强 (NotebookLM in-KB-only 架构天然反虚构). 你可以复跑这 17 题, 验证自己部署的 notebook 同样稳.

- **题库**: [`../../../SMOKE_V4.md`](../../../SMOKE_V4.md) §2
- **逐题答案 + verdict**: `../../notebooklm/dev/evidence/smoke_v4_answers/*.md`
- **总结报告**: `../../notebooklm/dev/evidence/smoke_v4_results.md`
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

## 7. 3 档分享切换 (本平台独有)

NotebookLM 支持同一 notebook 在 3 个分享档位间动态切换, 不需要建多个 notebook. 三档切换实测 2026-04-23 VERIFIED + 深化 (`../../notebooklm/dev/evidence/share_level_toggle_drill.md`).

### 3 档语义

| 档位 | 访问规则 | 适用场景 | 50-cap 规则 |
|------|----------|----------|-------------|
| **Restricted** (默认) | 仅 owner + 邀请列表里的 Google 账号 | 个人用 / 小圈团队 | **Free tier invitee 受 50 source cap 限** (Pro owner 不受限) |
| **Anyone with link** | 有链接的任何 Google 账号登录即访问 | 定向外发 / 公司内部广播 | 不套用 Free tier cap |
| **Public** | 链接可分享给任何人 (仍需登录 Google) | 开放知识库 | 不套用 Free tier cap |

### 切换步骤

1. notebook 右上角 "**Share**" 按钮 → 打开 share panel
2. 选想要的档位, 点 "**Copy link**" 生成访问链接
3. 回切 Restricted 会**立即 revoke** 之前的 link (实测 PASS, 无 caching 残留)

### 重要: Public 档 ≠ 自动广播 (实测新发现)

- Public 档位是 "**允许任何持链接者无需登录访问**", 不是自动上 NotebookLM 公开画廊
- NotebookLM 公开画廊 (Featured) 是**策展 curated list** 非 auto-listed, 你 Public 档也**不会自动曝光**
- **隐私友好性** > ChatGPT GPT Store "Public=全网广播" 语义
- 适合: 小圈内部 + 定向外发组合场景

### Free tier 50-cap 只套 Restricted+Invite 场景

- 若 Restricted 档 + invite 了 Free tier Gmail 小号, 小号**可能只能看前 50 source**
- 本发布版 42 sources ≤ 50, **无影响**
- 未来若扩到 ≥ 51 sources, 且需要 Free tier viewer 访问, 要 A/B/C 解读实测 (见 PLAN §3.3)

---

## 8. 排错手册

| 症状 | 诊断 | 修 |
|------|------|-----|
| 答案没 citation | Custom mode 没生效 | 回 §2 重贴 instructions.md, 确认 Save 绿勾 |
| 答案说变量不在 KB (实际应在) | source indexing silent fail | §3 找对应 source tile 看状态, 黄 loading 超时 → 删重传 |
| 答案把 AESER 答成 Req | instructions.md 贴不全被截断 | wc -m 原文 8925, 若贴完后字符数显著少 → 重贴 |
| 17 题 Q9 FAIL (架构限制) | **预期** in-KB-only 架构限制, safety-correct PUNT | 不要改 instructions.md 加"允许外推", 会降 反虚构优势 |
| AHP1-3 出现虚构 (如答 LBCLINSIG 存在) | instructions.md "边界诚实"锚点失效 | 回 §2 核对 instructions.md 完整; 或切换 Chat mode 再切回 Custom 刷新 |
| Pro viewer 在 Anyone-with-link 档看不全 source | 不应该, 此档位不套 Free tier cap | Google 账号登录状态 check; share link 重生成 |
| 小表渲染漂移 (单行错位) | F-1-recurring 已知现象, 不扣语义分 | 重发同问题通常刷新; retry 幂等性不强制 |
| citation dropout (业务场景题) | F-3 系统性弱点 (T2 题型偏向) | 答案内容通常对, citation 偶失; 不扣语义分 |

---

## 9. 升级 / 降级 / 扩容路径

### 扩容 (42 → N sources)

- Pro cap 300 source, 当前用 14% 有 8 slot + 258 Pro cap headroom
- 若 KB 扩展 (如加 SDTMIG 下个版本 v3.5 / 新 domain), 在 `../../notebooklm/dev/scripts/bucket_config.json` 加 bucket 43+ → 跑 `merge_sources.py` → 上传新 source 增量
- 注意: ≥ 51 sources 会触发 Free tier viewer 50-cap, 要重做 Free tier 实测

### 降级 (42 → Free tier 兼容)

- Free tier 50 notebook × 50 sources × 150K words/source × 50 chat/day × 3 audio/day
- **本发布版 Free tier 下 words cap 破**: 最大 bucket 302K > 150K/source Free cap → 需要重切 bucket (细粒度拆, 每个 < 150K)
- 重切路径: `../../notebooklm/dev/scripts/` 写新 config, pack 80-100 bucket, 重上传
- 工时估 1-2 天

### instructions.md 微调

- 10K char 限, 留 10.75% headroom (~1,075 chars 可加 3-5 锚点)
- 加锚点时跟 CLAUDE.md + RETROSPECTIVE.md R-NBL-3 一起更新
- 超过 10K 会被截, wc -m 前先 check

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

PLAN §10 保留的 Studio 三件套:
- **Audio Overview** × 3 期 (SAFETY / EFFICACY / PK Deep Dive podcast, 每期 30-45 min)
- **Mind Map**: 63 domain 跨域关系 + RELREC/SUPPQUAL 覆盖
- **Study Guide**: AE / LB / CM Socratic 引导

触发条件: 你主动提出"回头精雕 Studio 三件套". 不触发不影响主 retro + 本教程 FINAL.

### 10.4 相关文档

| 文档 | 路径 | 用途 |
|------|------|------|
| **RETROSPECTIVE (本平台)** | `../../notebooklm/docs/RETROSPECTIVE.md` | Rule C 三段 + pivot 案例 + _template/ 补丁 |
| **跨 4 平台 Phase 5 retro** | `../../retrospectives/PHASE5_RETROSPECTIVE.md` | v1.0 FINAL 2026-04-24 Bojiang Zhang 认可 4 平台 sign-off |
| **PLAN** | `../../notebooklm/docs/PLAN.md` | 662 行 v2.2 (架构 pivot 后完整 plan) |
| **完整 17 题测试结果** | `../../notebooklm/dev/evidence/smoke_v4_results.md` + `smoke_v4_answers/` | 17 题逐题 verdict |
| **三档切换 evidence** | `../../notebooklm/dev/evidence/share_level_toggle_drill.md` | v1.0 FINAL 6 子步 + Public 语义深化 |
| **v1→v2 架构 pivot 记录** | `../../notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` | 关键教训: Writer 叙事合成伪约束 |
| **reviewer 报告** | `../../notebooklm/dev/evidence/phase5_retrospective_reviewer.md` | v0.2 post-fix 独立审 10 行动项 |

---

## 附: 部署后自查清单

部署完走一遍以下清单:

- [ ] notebook 新建, 命名 `SDTM Knowledge Base`
- [ ] Chat Custom mode 贴了 instructions.md 全文 (8,925 chars)
- [ ] 42 个 source 上传 + 全 ✅ Indexed
- [ ] Smoke 3 题 (AESER Core / LBNRIND 4 值 / CMINDC 场景) 3/3 PASS
- [ ] (可选) 完整 17 题测试 ≥ 12/17 PASS
- [ ] 3 档切换验证 ≥ 2 档 (至少 Restricted 和 Anyone with link)
- [ ] 记下你的 notebook URL 给团队 (仅 Anyone-with-link / Public 档位)
- [ ] 读完本教程 §10.2 已知限制, 不要把 Pinnacle 21 之类需求硬推到 NotebookLM

---

*v1.0 — 2026-04-27 — 公司发布版*
*本平台独立 retro 见 ../../notebooklm/docs/RETROSPECTIVE.md ; release v1.0 总览见 ../README.zh.md*
