# NotebookLM 架构 Pivot 记录 — 3 notebook → 1 notebook

> **Pivot 日期**: 2026-04-21
> **触发**: 用户 Phase 2 PASS 后 review 时提出 "3 notebook 是否过重 + 293 source 是否过多" 质疑
> **决定**: 推倒 Phase 2 PLAN v1 架构, 重做为 1 notebook × ≤50 sources

---

## 一、本文件的作用

本目录 `archive/v1_3notebook_SUPERSEDED_2026-04-21/` 冻结 Phase 0-2 v1 (3 notebook 架构) 全部产出, **仅作审计轨迹**, 不作任何现行参考. 新架构文档在 `ai_platforms/notebooklm/docs/PLAN.md` (v2).

**本文件是 Phase 2 v1 → v2 的唯一桥梁**: 解释 pivot 原因 + 证据链 + 被舍弃的决策 + 保留的资产, 避免新+旧混用造成误解.

---

## 二、被舍弃的 v1 核心假设

v1 PLAN 建立在以下**三条假设**之上, 本次 pivot **全部推翻**:

### 假设 1 (✗): Scope B 分享 "本质上两选一" — Mode A (invite) vs Mode B (public link) 不可共存, 必两独立 notebook

**v1 依据**: research.md v1 Q7 末尾 "但 Scope B 本质上两选一决策" — planner 从叙事里引伸
**推翻证据** (2026-04-21 三 WebFetch 交叉核实):
- Google 官方 `answer/16322204` 明文: "turn off public sharing by revoking public access" + "Set Notebook Access back to **Restricted**"
- UI 实况: 同一 notebook 可按需切 **Restricted / Anyone with link / Public** 三档 (用户实测报告)
- 三档切换随时, 不需要新建 notebook
**结论**: "两选一" 是叙事合成的伪约束, 不是平台约束. 一个 notebook 足以覆盖 Scope B 全部分享场景.

### 假设 2 (✗): "Mode A 50-cap 可能覆盖 Mode B" — 需要 Phase 3 I8 实测

**v1 依据**: research.md v1 Q7 UNVERIFIED 条 + `_progress.json` C2.9 / I8 carry-over
**推翻证据** (2026-04-21 WebFetch `answer/16206563` + AI summary):
- 官方原文 "Personal Gmail accounts can share a notebook with up to 50 users"
- WebFetch #1 结论: "This refers to the **invite-based method**, not 'Anyone with the link' or public sharing"
**结论**: 50-cap 仅套 Restricted invite 档, "Anyone with link" / "Public" 档**无 users 上限**. I8 / C2.9 直接 close, 免 Phase 3 实测.

### 假设 3 (✗): "293 sources 一对一上传到 Notebook 1 主训练" — 利用 Pro tier 300 slot 最大精度

**v1 依据**: PLAN v1 §3.1 Notebook 1 "293 md 一对一, 占 Pro cap 97.7%, 余 7 slot"
**推翻证据**:
- 官方 `answer/16213268`: "Sharing a notebook does not change the source limit for any collaborator" → viewer 自己 tier ceiling 不被 owner 上传量突破
- 即使不考虑 share, 以下独立理由仍支持 ≤50 压缩:
  1. Indexing silent fail 风险随 source 数线性 (研究 Q5 官方承认), 293 比 50 高 6x 风险面
  2. Citation 信噪比: source 数越多, 跨文件 citation 越分散, 业务问答噪声大
  3. Mind Map 可读性: 293 节点图退化成噪声, 50 节点可看
  4. Upload effort: 293 次 Web UI 操作 vs ≤50 次, 不是一个量级
  5. Workflow replication fallback (Rule E ack): 他人 Free tier Gmail 复刻 ceiling 是 50
  6. **Req 零丢失红线反而更容易守**: 50 slot 比 v1 Notebook 2 的 30 slot 宽松, concept cluster 重 bucket 有更多 outlier 容错余地
**结论**: 压缩到 ≤50 有 6 条独立证据, Pro 300 slot 余量不是该用就用.

---

## 三、被舍弃的 v1 具体决策清单

| # | v1 决策 | v2 新决策 | 舍弃原因 |
|---|---------|----------|---------|
| D1 | 3 个 notebook 架构 (主训练 + invite + public) | **1 个 notebook** + 分享档位按需切 | 假设 1 推翻 |
| D2 | Notebook 1 = 293 md 一对一上传, Notebook 2/3 各 ≤30 精选 | 单 notebook × ≤50 精选 (concept cluster) | 假设 3 推翻 + 压缩合理性 |
| D3 | 总上传次数最坏 353 (293 + 30 + 30, 三 notebook 分别上传) | 总上传次数 ≤50 | D1 + D2 直接导出 |
| D4 | A/B 矩阵 45 题次 (3 notebook × 15 题 独立判定) | A/B 矩阵 15 题 (1 notebook × 15 题) | D1 直接导出 |
| D5 | 目录结构 `uploads_main/` + `uploads_invite/` + `uploads_public/` + `instructions_1/2/3.md` | 目录结构 `uploads/` + `instructions.md` (单) | D1 直接导出 |
| D6 | Phase A Setup 6 子动作 + A5 "webui batch upload 能力调研" (hard checkpoint) | Phase A Setup 简化 (A5 降级: 单 notebook 场景, 50 次上传 Web UI 手工可行, 不强制 Playwright 前置) | D3 导出 — 操作量级降 85%, 不必 tooling 前置 |
| D7 | P11 "per-day rate limit" + P12 "source 隔离" 作 hard rule | P11 保留 (仍适用) / P12 降级为信息段 (单 notebook 下无跨 notebook 引用需求) | D1 导出 |
| D8 | I8 / C2.9 carry-over 转 Phase 3 实测 | Close (WebFetch 证据闭合) | 假设 2 推翻 |
| D9 | `cluster_req_variables.py` 产 Notebook 2/3 的 ≤30 source bucket 方案 (内容一致, 独立上传) | `cluster_req_variables.py` 产单 notebook 的 ≤50 source bucket 方案 (slot 更宽松, Req 零丢失更易守) | D1 + D2 导出 |
| D10 | "Chat mode 三 notebook 分别决策 (Custom / Learning Guide / Custom public)" | 单 notebook Custom mode (SDTM 专家 system prompt, ≤10,000 char) | D1 导出 — 一个 notebook 只能一个 Chat mode |

---

## 四、保留的 v1 资产 (v2 继承)

以下资产**经验证仍有效**, v2 PLAN 直接继承, 无需 Phase 1 重跑:

### 保留 A: research.md Q1-Q6, Q8-Q10 事实 (共 9 问)

| Q | 事实 | 保留原因 |
|---|------|---------|
| Q1 | Pro tier 定义 (via Google AI Pro 订阅, 500 notebooks × 300 sources × 500 chat × 20 audio/day) | 独立于 notebook 数, 平台硬指标 |
| Q2 | 四档容量矩阵 (Standard/Plus/Pro/Ultra) + SKU 重命名警示 | 同上 |
| Q3 | SKU 时间线 (原 Plus → Pro 重命名 2025 H2) | 历史事实不变 |
| Q4 | Chat mode 三档 (Default / Learning Guide / Custom, 2025-10-29 全档开放) + Custom 10,000 char | 单 notebook 选 Custom, 保留不变 |
| Q5 | Indexing silent fail 官方承认 | 单 notebook 下仍适用 (只是只需做 1 次而非 3 次 gate) |
| Q6 | Audio Overview 4 format + Pro = 20/day | per-day rate limit 保留 |
| Q8 | Capacity 透明 → skip calibration | 独立于 notebook 数 |
| Q9 (§9) | Audio Overview 独有调研 | 独立于 notebook 数 |
| Q10 (§10) | Mind Map 调研 | 独立于 notebook 数 |

### 保留 B: Phase 1 / 2 Rule D 4-lane × 2 = 8 种 subagent_type 方法论

8 种 subagent_type 独立链的审查过程**本身合法**, 未被 pivot 破坏. v2 PLAN 的第 9 种 subagent_type 在 8 种基础上追加, Rule D 链继续延长.

### 保留 C: 用户 Q1 零丢失 + Q2 质量第一 ack (2026-04-21)

用户 2026-04-21 ack 的"0 Req 变量允许丢失"+"不限工时"决策继续成立, v2 PLAN 的 Req 零丢失红线逻辑**向内收紧不放松**.

### 保留 D: Rule E ack (ABC 全向 + Pro + Web UI + personal Gmail)

`rule_E_user_priority` 字段全部成立. 1 notebook 策略下 ABC 三场景**在同一 notebook 内按分享档位切换实现**.

### 保留 E: `_template/` 补丁候选 7 条 + 本次新增

原 7 条中:
- #1 (system prompt 退化映射) — 保留
- #2 (独有生成物 A/B 维度) — 保留
- #3 (notebook-first Solution 设计) — 保留
- #4 (capacity 透明跳 calibration) — 保留
- #5 "多实例平台" — **重写**: 从"默认 multi-notebook"改为"**评估是否需要 multi-notebook 的决策树**", 强调本平台典型场景**一个 notebook 足够**, 只有 ABC 场景职责分离到不同 collaborator 圈时才升级多 notebook
- #6 (workflow_replication fallback 分享) — 保留
- #7 (tier 重命名漂移警示) — 保留

### 保留 F: 脚本 `extract_req_vars.py` + `cluster_req_variables.py` 设计意图

- `extract_req_vars.py` 从 VARIABLE_INDEX.md 抽 Core=Req 全集 — 设计意图不变
- `cluster_req_variables.py` concept cluster 重 bucket — 设计意图不变, 只是 target slot 从 30 改 ≤50, bucket 可能更粗粒度

---

## 五、Pivot 证据链 (WebFetch 核实 2026-04-21)

**三 WebFetch 并行** (本次 pivot 的决定性证据):

1. **`support.google.com/notebooklm/answer/16206563`** (Create a notebook)
   - 证据: "Personal Gmail accounts can share a notebook with up to 50 users but can't share with Google Groups"
   - 证据: "Enterprise and Education accounts ... can share a notebook with an unlimited number of individual users and Google Groups"
   - 结论: 50-cap 仅套 invite-based, 不覆盖其他档

2. **`support.google.com/notebooklm/answer/16322204`** (Public notebooks)
   - 证据: "turn off public sharing by revoking public access in the sharing panel" + "Set Notebook Access back to Restricted"
   - 结论: 档位可在同一 notebook 上切换, 不是两独立 notebook type
   - 证据: "Copy and share the link to anyone with a Google account to have them view your notebook"
   - 结论: Anyone with link 需 Google 账号, 非匿名

3. **`support.google.com/notebooklm/answer/16213268`** (Pro tier overview)
   - 证据: "Sharing a notebook does not change the source limit for any collaborator"
   - AI summary 解读: "the restriction follows the user, not the notebook" — Free tier 用户看共享 notebook 时 50-slot ceiling 仍在
   - 结论: 为 Free tier 兼容性预留 ≤50 sources 是稳策略 (即使解读不绝对, 保守性有效)

---

## 六、本 pivot 本身是否需要独立 Reviewer?

**是**. v2 PLAN 写完后, **派第 9 种 subagent_type** (前 8 种之外) 做架构级独立审查:

- 验证: 假设 1/2/3 的推翻证据是否充分
- 验证: v2 新决策 (D1-D10) 是否逻辑自洽
- 验证: Q1 零丢失红线是否在 slot 从 30 → ≤50 过程中被保留甚至加强
- 验证: 保留资产 (A-F) 是否真的无瑕疵继承, 无隐性矛盾

审查结果登记到 `dev/evidence/phase2_reviewer_v2.md` + `_progress.json phase_2 字段`.

---

## 七、审计一致性声明

本 pivot 操作**遵守规则 B** (失败归档不删) + 本次用户 2026-04-21 指示 ("干干净净"):
- v1 全部产出移到本目录 `archive/v1_3notebook_SUPERSEDED_2026-04-21/`, 文件内容不修改不删除
- 新 v2 产出在原位置 (`docs/PLAN.md` 等), 不与 v1 混放
- 本文件 `ARCHITECTURE_PIVOT_RECORD.md` 作为唯一桥梁, 防止误读

**Rule D 链完整性**: v1 产出经过 8 种 subagent_type 独立审, v2 产出计划经过第 9 种独立审, Rule D 链继续延长而非复位.

**Rule C (Phase 5 Retrospective) 预读**: 本次 pivot 事件应写入 RETROSPECTIVE.md 保留段"架构决策修正" — 典型案例 "Writer 叙事合成易生伪约束, 用户反问是关键救援路径".

---

*最后修改: 2026-04-21 (pivot 同日)*
