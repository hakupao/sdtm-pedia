# NotebookLM 平台部署

> **状态**: Phase 0 进行中 (2026-04-21 起跑)
> **模式**: **异步** (不参与 `SYNC_BOARD.md` 的 ChatGPT ↔ Gemini 2-way 锁步 — 独立推进, 吸收前两平台收束后的范本补丁再跑也无妨)
> **范本来源**: `ai_platforms/_template/` (已 `cp` 到 `_spec/`)

---

## 我想做什么?

### 部署一个可用的 NotebookLM 实例
→ 去 [**current/**](current/), 读 `UPLOAD_TUTORIAL.md` (待 Phase 4 产出).

### 理解这套知识库怎么做出来的
→ 去 [**docs/**](docs/) 看 `platform_profile.md` / `research.md` / `PLAN.md`.

### 考古 / 复盘 / 贡献改进
→ 去 [**dev/**](dev/) (evidence + scripts + ab_reports) 或 [**archive/**](archive/) (暂无, 待 v1 发布后再填).

---

## 当前进度 (v2 架构: 1 notebook × ≤50 sources, 2026-04-21 pivot 后)

| Phase | 状态 | 产物 |
|-------|------|------|
| 0 启动 | ✅ **PASS** | `docs/platform_profile.md` (v2) + `ROADMAP.md` (v2) + `_progress.json` + 本 README; Rule E ack (ABC + Pro + Web UI + personal Gmail) |
| 1 调研 | ✅ **PASS** | `docs/research.md` (Q7/§11 已 v2 重写, Q1-Q6/Q8-Q10 facts 保留) + Rule D 4-lane 审 |
| 2 PLAN v1 (3 notebook) | 🗄️ **归档** | v1 已 freeze 至 `archive/v1_3notebook_SUPERSEDED_2026-04-21/`, 背景见 `ARCHITECTURE_PIVOT_RECORD.md` |
| 2 PLAN v2 (1 notebook) | 🟡 **doing** | `docs/PLAN.md` v2 重写中 (1 notebook × ≤50 sources + 分享档位切换 + Req 零丢失红线) |
| 3 落地 | 🔒 locked | 上传 ≤50 + A/B 15 题 + evidence |
| 4 审查 | 🔒 locked | 回归 + 跨 4 平台同题对比 |
| 5 收束 | 🔒 locked | RETROSPECTIVE (含 pivot 复盘) + UPLOAD_TUTORIAL + `_template/` 补丁 (10 候选) |

**pivot 背景**: 2026-04-21 用户 review Phase 2 v1 时质疑 3 notebook 架构过重, 三 WebFetch 核实官方文档后确认 "UI 3 档可切" + "50-cap 仅 Restricted" + "viewer 自己 tier cap", 推翻 v1 三假设. 详见 [`archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md`](archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md).

---

## 本平台独有关注点

和 ChatGPT / Gemini / Claude 不同的三条:

1. **无 Custom Instructions** — 范本 `00_platform_profile.md §D` 全部字段在 NotebookLM 下退化为 "notebook-wide prompt engineering" 或 "Audio Overview instructions" (Plus 版). `system_prompt.md` 概念要重新定义.
2. **独有生成物** — Audio Overview (播客对谈) / Mind Map / Study Guide / Briefing Doc / FAQ / Timeline. A/B 矩阵 (范本 `06_review.md`) 必须加 "生成物质量" 维度, 不只是问答召回.
3. **Source-grounded only** — 模型被强约束只能从 sources 回答, "边界诚实"是默认行为而非考点. 范本 `00_platform_profile.md §G` Claude 那条"边界诚实"可以从 A/B 矩阵摘掉.

这三条就是本平台对 `_template/` 能贡献的**缺陷补丁**, 收束时合并回范本.

---

## 与 ChatGPT / Gemini 锁步的关系

- **不参与 `SYNC_BOARD.md`** — 那是 2-way gate, 本平台独立推进
- **可复用 ChatGPT + Gemini 收束产出** — 尤其 Phase 3 Node 4 "战略转向业务问答优化" 的内容策略 (见两平台 `docs/PLAN_V2_C.md` / `PLAN_BATCH2.md`), NotebookLM 的 source 合并粒度可以直接借鉴, 不重踩
- **收束时交叉复盘** — 产出 `docs/RETROSPECTIVE.md` 的"跨平台对比"段, 写进 handoff 给下个平台

---

## 快速索引

| 产物 | 路径 |
|------|------|
| 范本 (只读参照) | `_spec/` (cp 自 `ai_platforms/_template/`) |
| 平台画像初稿 | [`docs/platform_profile.md`](docs/platform_profile.md) |
| 进度单一来源 | [`dev/evidence/_progress.json`](dev/evidence/_progress.json) |
| 路线图 | [`ROADMAP.md`](ROADMAP.md) |
| 开发区路径映射 | [`dev/README.md`](dev/README.md) |

---

*建立日期: 2026-04-21 — session 起跑同日填写.*
