# P3.9 Share Level Toggle Drill — 三档切换演练 Evidence

> **Date**: 2026-04-23
> **Scope**: NotebookLM v2 架构单 notebook × 42 sources, 三档分享切换演练 (H3 hypothesis 正式归档)
> **PLAN Ref**: `ai_platforms/notebooklm/docs/PLAN.md §6 P3.9` (L479-488, 40 分钟 hard checkpoint)
> **Executor**: 用户 cowork (2026-04-23)
> **总体 Verdict**: **PASS** (5 PASS + 1 PARTIAL + 1 SKIP, 核心切换+revoke 机制 VERIFIED, 1 新发现 meta-insight)

---

## §1 子步骤 verdicts (按 PLAN §P3.9 a-f)

### (a) Restricted (默认) — 截屏 share panel

- **Verdict**: ✅ **PASS**
- **观察**: Share panel 以 Restricted 为默认态, 控制项可见

### (b) Anyone with link — 生成链接 + 2 账号测

- **Verdict**: ✅ **PASS** (b1+b2+b3 全过)
- 子步 b1: 切 "Anyone with link" + 生成链接 → PASS
- 子步 b2: 匿名窗口 (非 Google 账号) 试打开 → PASS (预期行为)
- 子步 b3: 另 Google 账号打开 → PASS (能看到 notebook)

### (c) Public — 在 NotebookLM 公开画廊搜

- **Verdict**: 🟡 **PARTIAL** (重要新发现, 非能力 FAIL)
- **观察**: 切 Public 档后, 在 NotebookLM 公开画廊**搜不到**本 notebook, 画廊**只显示官方精选笔记本** ("Featured" curated list)
- **新发现 meta-insight**: **"Public" 档位 ≠ 自动广播到 public gallery**. Public 档位是"允许任何持链接的人无需登录即访问", 而 NotebookLM 公开画廊是**策展的 curated list**, 非 auto-listed. 这与 ChatGPT GPT Store "Public = 全网广播" 语义**不同**
- **对 Phase 5 retro 的影响**: 强化 D5-6 的判断 — NotebookLM v2 "1 notebook × 3 档分享" 的 scope 实质是 **Restricted (私有) / Anyone with link (定向内部传播) / Public (公开链接但非画廊广播)**, 跟 v1 多 notebook 架构想象的"公开广播"是两回事. "Public" 档的实际 reach < 用户预期, 但这反而降低隐私风险

### (d) 回切 Restricted — 测旧链接失效

- **Verdict**: ✅ **PASS**
- **旧 Public 链接在 Restricted 后**: 被 revoke, 预期行为生效

### (e) L3 fix — 快速多次切换 (Restricted ↔ Public × 2)

- **Verdict**: ✅ **PASS**
- **做法**: 连续 Restricted ↔ Public 切 2 次后, 第一次的 Public 链接被 revoke 成功 (档位切换无 caching 残留)
- **结论**: NotebookLM 档位切换状态管理合规, 无 "旧链接幽灵残留" 安全问题

### (f) S1 SUGGESTION — Free tier 50-cap 实测 (证据 3 解读)

- **Verdict**: ⚪ **SKIP** (客观无法测, 非执行疏忽)
- **实际**: 本 notebook 上传 **42 sources (≤50)**, 未触及 Free tier 50-cap, **无法测试** A/B/C 三路径
- **对证据 3 的影响**: Evidence 3 解读 **悬置 (unverifiable-in-this-drill)**, 不升成 A 也不证伪
  - **主归因 (indexing silent fail 风险 + citation 信噪比) 不受影响** — 这是 ≤50 策略的 **HIGH 级证据**, 独立于 Free tier cap
  - **次要归因 (Free tier viewer 兼容) 维持 MEDIUM 悬置** — 若未来扩展到 42 → ≥51 sources, 需补测此项
- **补做路径 (optional, post-Phase-5)**:
  1. 制造 >50 source 测试集 (临时 bucket 分裂 / 重新 merge), 让 notebook 超 50 触发 cap
  2. Free tier Gmail 小号 invite 查看
  3. 看小号能看到多少 source (A/B/C 判定)
- **接受残余风险** (Daisy 2026-04-23): ≤50 策略主归因 HIGH, 次要归因悬置不阻塞 Phase 5 sign-off

---

## §2 总表

| 子步骤 | Verdict | 备注 |
|---|---|---|
| (a) Restricted 截屏 | ✅ PASS | 默认态控制项可见 |
| (b1) Anyone with link 生成 | ✅ PASS | 链接可生成 |
| (b2) 匿名试访 | ✅ PASS | 预期被要求登录 |
| (b3) 另 Google 账号 | ✅ PASS | 能看到 notebook |
| (c) Public 公开画廊 | 🟡 PARTIAL | **新发现**: Public ≠ 画廊广播, 画廊只显示官方精选 |
| (d) 回切 + 旧链接失效 | ✅ PASS | Revoke 生效 |
| (e) L3 快速多切 | ✅ PASS | 无 caching 残留 |
| (f) Free tier 50-cap | ⚪ SKIP | 42 sources ≤50 未触发 cap, 无法测, 接受残余风险 |

**总体 verdict**: ✅ **PASS** (核心 4/5 子步全过 + (c) PARTIAL 是 meta-insight 非 FAIL + (f) 客观 SKIP)

---

## §3 H3 hypothesis 归档

**H3 原陈述**: NotebookLM 三档分享切换 UI 是 per-notebook-session dynamic toggle, 非 notebook 锁定.

**P3.3 初步 VERIFIED** (参考 `chat_mode_toggle_test.md` 2026-04-21), 本 P3.9 正式归档.

**本 drill 对 H3 的印证**:
- ✅ **Dynamic toggle 性质 VERIFIED**: (d) + (e) 显示档位切换即时生效 + 旧链接 revoke 合规 + 无 caching 残留
- ✅ **Per-notebook-session scope VERIFIED**: 档位是 notebook-level 设置, 不影响 viewer session 内部行为
- 🆕 **Meta-insight (P3.9 新增)**: "Public" 档的**实质语义**是"公开链接访问", **不等同于 "上 public gallery 被动曝光"**. 画廊是 curated 而非 auto-listed. 这修正了 v1 3-notebook 架构时期的"Public=广播"假设 (ARCHITECTURE_PIVOT_RECORD D3 的一部分被 P3.9 实测印证并深化)

**H3 最终归档状态**: ✅ **VERIFIED + 深化** (3 档机制实证可用, 且 Public 档语义比预期更保守/隐私友好)

---

## §4 Phase 5 retrospective 回灌入口

本 drill 完成, 本文件作为 `PHASE5_RETROSPECTIVE.md` 以下 4 处 `[TBD post-P3.9]` marker 的数据源:

- **§1.6 R5-6 三档切换 UI 级 VERIFIED 做法** ← (a)+(b)+(d)+(e) 联合作保留做法
- **§2.5 G5-5 Free tier 50-cap 证据 3 解读 A/B/C** ← (f) SKIP, 悬置不闭合, 接受残余风险 (主归因不受影响)
- **§3.7 D5-7 三档分享实测决策** ← (c) 新发现 + 总体 PASS 证 v1→v2 架构 pivot 正确
- **§4.15 `_template/` 补丁 15 (single-notebook 多 scope 新范式)** ← Public 语义深化, 补丁文案加 "Public ≠ gallery 广播" 澄清

主 session 下一步: grade 本文 → 灌 retro → 派 28th reviewer slot → Phase 5 FINAL.

---

## §5 Daisy 回看

- **实际耗时 vs PLAN 40 min 估值**: 完成, 未记录精确耗时
- **过程中发现的 NotebookLM 新 UI 行为 (未在 PLAN 覆盖)**: (c) Public 档不 auto-list 到公开画廊, 画廊是 curated Featured list. PLAN §6 P3.9 原描述 "在 NotebookLM 公开画廊搜" 隐含 auto-list 假设, 实测不成立
- **(f) SKIP 的残余风险处置**: 接受. ≤50 策略主归因 HIGH 级证据稳 (indexing silent fail + citation 信噪比), 次要归因 (Free tier 兼容) 悬置, 未来若 ≥51 source 时补测

---

*v1.0 FINAL 2026-04-23. Daisy 完成 drill + 给 verdict, 主 session 填完整 evidence. Phase 5 最后一个 hard checkpoint 闭合.*
