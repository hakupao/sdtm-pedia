# NotebookLM Deployment Roadmap (v2, 2026-04-21 架构 pivot 后)

## 状态 (首屏)

- **当前状态**: Phase 2 v2 准备中 (2026-04-21 架构 pivot, v1 冻结于 archive/)
- **目标 Tier**: **Tier 2** (5-15 步, 半天-1 天)
- **模式**: 异步 (不参与 `SYNC_BOARD.md` 2-way 锁步)
- **参考基线**: Claude v2.6 方法论 + ChatGPT/Gemini 范本补丁
- **架构**: **1 notebook × ≤50 sources** (v1 3 notebook × 各 30-293 源已归档)

## v2 架构 (首屏)

### 1. 状态 + 日期
- **Phase 0-1 PASS 2026-04-21** — 事实依据已核实 (Pro tier / 500 notebooks / Chat custom goals / 50-cap 仅 Restricted invite)
- **Phase 2 v1 (3 notebook) 已废 + 归档** (2026-04-21, 见 `archive/v1_3notebook_SUPERSEDED_2026-04-21/`)
- **Phase 2 v2 (1 notebook × ≤50) 进行中** — PLAN 重写中

### 2. 着重方向 (本平台独有优势)
- **Audio Overview 培训产物**: SDTM 初学者 30 分钟可听完一期"SDTM Domain 速览"播客
- **Mind Map 关系可视化**: 跨 domain 的 RELREC / --STAT / Supplemental Qualifier 依赖关系图形化
- **Grounded citation 默认强**: 每句都能点回源 chunk, "SDTM 标准依据"类问题最稳
- **Study Guide / Briefing Doc 自动化**: 问卷式学习产出

### 3. 平台特性 (已 Phase 1 确认)

| 维度 | 值 | 来源 |
|------|-----|------|
| 订阅 | **Pro** (via Google AI Pro) — 500 notebooks × 300 sources × 500 chat × 20 audio/day | support.google.com/notebooklm/answer/16213268 |
| RAG | 内置 grounded retrieval, chunk-level inline citation | 官方 |
| Source 数上限 (硬) | Pro 300 / notebook; 500K words / source 全档统一 | 同上 |
| **本次实际使用** | **≤50 sources** (主动压缩 Free tier 兼容水位) | v2 架构 |
| 文件类型 | PDF, .txt, .md, Google Docs/Slides, 网页 URL, YouTube URL, 音频文件 | 官方 |
| 分享 | **同一 notebook 3 档** (Restricted / Anyone with link / Public) 可切 | answer/16322204 |
| Chat custom goals | 三档 (Default / Learning Guide / **Custom**), Custom 10K char 写 SDTM 专家 | blog.google 2025-10-29 |
| API | 无 GA consumer API (本次 Web UI only) | research §12 |

### 4. 内容策略 (已 Phase 2 v2 定)

- **单 notebook**: 293 md → concept cluster 重 bucket → **≤50 source**
- **ABC 三场景在同一 notebook 内按分享档位切换** (默认 Restricted, 按需切 Anyone with link / Public)
- **Req 零丢失红线** (用户 2026-04-21 ack Q1=0): concept cluster 保证 ~100-120 独立 Req 变量全覆盖
- **Chat mode**: Custom (10K char, SDTM 专家 prompt)

### 5. 执行步骤 (Phase 0-5)
- Phase 0 脚手架 ✓
- Phase 1 八问八答调研 ✓ (含 Chat custom goals / Indexing silent fail 三 WebFetch 核实)
- Phase 2 PLAN ✓ (v1 ×3 notebook 归档, v2 ×1 notebook 重写)
- Phase 3 单批上传 (≤50) + A/B 15 题 + 独有生成物评估 + 分享档位演练
- Phase 4 回归 + 跨平台 (Claude/ChatGPT/Gemini/NotebookLM 四平台) 同题对比
- Phase 5 RETROSPECTIVE (含本次 pivot 作关键案例) + `_template/` 缺陷补丁合并 + handoff

### 6. 验收标准 (A/B 矩阵 PASS 条件)
- **15 题** (10 SMOKE v2 + 5 独有生成物评估: Audio Overview 2 + Mind Map 2 + Study Guide 1)
- PASS 阈值: **≥13/15 (~87%) 业务正确 + 每个独有产出至少 1 题精确命中**
- **Req 变量零丢失** (用户 Q1 红线, 基于 `extract_req_vars.py` 产出对照审计)

## 实际产出 (收束时填)

- 文件数: _pending_ (目标 ≤50)
- 总 words: _pending_ (目标 <15M words, 远低 Pro cap)
- Source 占用: _pending_ / 300 Pro slot (预计 ~15%)
- A/B PASS: _pending_
- 跨平台对比: _pending_
- `_template/` 补丁: _pending_ (10 候选)

---

## CHANGELOG

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-04-21 (am) | v1 draft | 初版, Phase 0 脚手架, 3 notebook × 30-293 源假设 |
| 2026-04-21 (pm) | **v2** | **架构 pivot** (3 notebook → 1 × ≤50) — 用户 UI 实测 + 三 WebFetch 核实, 见 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md` |

---

*更新规则: 每 Phase 收束时刷新本文件首屏 + append 一条 CHANGELOG.*
