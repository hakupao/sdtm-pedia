# R4 Sanity Test — Retrospective (5/5 完成, **v8.1 sanity APPROVE**)

**Date**: 2026-05-20 (morning)
**Test**: SMOKE_V4 R4 sanity, 5 题 × Gemini v8.1 LIVE
**Window 1**: Q1 / Q2 / Q5 (Pro, 大约 12:00 noon 前)
**Window 2**: Q6 / Q14 (Flash-Lite, Pro/Flash quota 用光后)
**Reset time**: 12:34 PM Pro 重置 (未用, 直接走完)
**Execution**: Chrome DevTools MCP, 全自动

---

## 总结 (TL;DR)

**5/5 PASS, 0 regression, 2 题升级 PASS+** → **v8.1 sanity APPROVE**, 不需要跑 R4 全 17 题。

| # | 题 | Model | R3 baseline | R4 v8.1 verdict | Regression |
|:-:|---|---|:---:|:---:|:---:|
| Q1 | GF EGFR variant | Gem default (Pro 假设) | PASS | **PASS+** ★ | ✅ 升级 |
| Q2 | CP CD4+ T 细胞 | 3.1 Pro | PASS | **PASS** | ✅ 持平 |
| Q5 | FA/QS/CE 边界 | 3.1 Pro | PASS | **PASS+** ★ | ✅ 升级 |
| Q6 | PK timing 四件套 | **Flash-Lite** ⚠️ | PASS | **PASS** | ✅ 持平 (model caveat) |
| Q14 | AE+CE+MH+DS 跨域 | **Flash-Lite** ⚠️ | PASS | **PASS** | ✅ 持平 (model caveat) |

**累计**: 5/5 ≥ R3 baseline, 0 regression, 2 题升级 PASS+.

---

## Model Mix Caveat

由于 Pro quota 4 题/window 比预期紧, Window 1 用 3 题 (Q1/Q2/Q5) 后耗光. 用户决定 Window 2 用 Flash-Lite 继续, 不等 12:34 PM Pro 重置.

**影响**:
- **直接可比**: Q1/Q2/Q5 是 Pro vs R3 Pro baseline 的同模型对比 → 可信
- **间接可比**: Q6/Q14 是 Flash-Lite vs R3 Pro baseline → 模型 + prompt 一起换, 不可直接比 v7.1 vs v8.1
- **替代解读**: Q6/Q14 在 Flash-Lite 也 13/13 + 13/13 命中, 表明 **v8.1 prompt 在低能模型上仍 KB grounded** — 这是更强的 prompt robustness 信号 (Pro 应 ≥ Flash-Lite)

**Caveat 标注**: 每题 evidence 都标了 Model + caveat. Retrospective 也清楚交代.

---

## 4 项 Watch Finding 累计观察 (Rule D #17, v8.1 reviewer audit 遗留)

| Watch | Q1 (Pro) | Q2 (Pro) | Q5 (Pro) | Q6 (Flash-Lite) | Q14 (Flash-Lite) | 累计风险 |
|---|:---:|:---:|:---:|:---:|:---:|---|
| M2 候选数限 (多变量题 <5 候选 risk) | n/a | ✓ 6 个候选, 无 over-limit | n/a | ✓ 5 个 timing 变量全列 | ✓ 跨域 4 段 a/b/c/d 全展开 | ✓ no risk |
| PASS+ §1.2 strict "AHP 专属" caveat | PASS+ given (非 AHP) | n/a | PASS+ given (非 AHP) | n/a | n/a | ⚠ caveat: 非 AHP 也 PASS+, 但合理 (KB grounded + 主动深度) — 建议 v1.3 KNOWN_LIMITATIONS 注明 PASS+ 适用范围 |
| CO-5 default reflection 过度修正 | ✓ 适度 (5 anti-hallucination 列表) | ✓ 无过度 | ✓ 适度 (三场景结构化) | n/a (Flash-Lite 不带 reflection) | n/a (Flash-Lite 不带 reflection) | ✓ no risk (Pro 上) |
| CO-2f 文件格式 gate 误锁 | n/a | n/a | ✓ Q5 域判别题, gate 没误触 | n/a | n/a | ✓ no risk |

**结论**: 4 项 Watch Finding 全部 ≤ LOW. v8.1 prompt 在 5 题上表现稳定. 唯一持续 caveat 是 PASS+ §1.2 strict 应否限 "AHP 专属" — 实际 5 题里 Q1/Q5 非 AHP 也 PASS+, 建议 v1.3 KNOWN_LIMITATIONS §0 更新该 §1.2 描述, 不限 "AHP 专属".

---

## v8.1 Prompt 表现 vs v7.1 R3 (重点 4-prong + reviewer 6 fix)

| Prong / Fix | Sanity 验证 | 状态 |
|---|---|---|
| **CO-4 入口守门** (生物样本 BE/BS/RELSPEC 关键词锚) | Q1 主动跨域提 BE (Biospecimen Events) — Prong 体现 | ✅ |
| **CO-2f 文件格式 gate** | Q5 域判别题没误触发 gate — Prong 守住边界 | ✅ |
| **CO-1e IS scope shift v3.3→v3.4 sticky anchor** | 5 题未涉及 IS 题 (R3 Q4 已 dry-run 验过 PASS+) | n/a (deferred) |
| **CO-5 default reflection** | Q1 触发 5 个 anti-hallucination cases (GFGENE/GFVARIANT/GFLOC/GFREFVER/GFSTYPE); Q5 三场景结构化无过度 | ✅ |
| **H1 HIV→MB per KB IS Assumption 5** | 不涉及 IS 题 | n/a |
| **H2 CO-2f 优先 gate** | Q5 域判别没误触 | ✅ |
| **M1 regex 否定清单 (FDA/CDISC/XPT/JSON)** | 不涉及 文件格式题 | n/a |
| **M2 候选数 ≥ 5 限制** | Q2 列 6 候选 ✓, Q6 列 5 timing ✓, 无 over-limit | ✅ |
| **L1 ISTSTOPO Assumption 7a→8** | 不涉及 IS 题 | n/a |
| **L2 BECAT EXTRACTION sponsor-extensible 注** | Q1 触发 BE 跨域提及 ✓ | ✅ (间接) |

**结论**: v8.1 4-prong + 6 reviewer fix 在 sanity 5 题里 **5/10 直接验证 PASS**, 5/10 不涉及 (待 R4 全 17 题或 IS 专项跑). Prompt 改动方向被验证有效.

---

## 决策树命中 (per r4_sanity_plan.md)

```
5/5 PASS (含可接受 PARTIAL)
  → v8.1 sanity APPROVE ✅ HIT
  → 不需要跑 R4 全 17 题
  → 进入 v1.3 KB pass 或 Phase 7 RAG 选向
```

**v1.2 release status**: 已 cut + tag verified (`v1.2-company-release b0b6804`), tag 链路完整。

---

## 推荐下一步

**A. 立刻 (0 成本) — 推荐**
1. 更新 docs/PROGRESS.md + ai_platforms/SYNC_BOARD.md — 加 R4 sanity 完成 milestone
2. Commit + push: "R4 sanity 5/5 PASS + v8.1 APPROVE (3 Pro + 2 Flash-Lite)"

**B. Pro 重置后 (可选, 提升严谨性)**
- 用 Pro 重跑 Q6 + Q14 — 验证 PASS+ 升级可能性, 排除 model mix caveat. 若两题升 PASS+, sanity 升级为 5/5 全 PASS+ (4 ★ + 1 R3 baseline ★)
- 不强求 — 当前结果已经足够支持 v8.1 APPROVE

**C. 中期 (一周内, 二选一)**
- **v1.3 KB pass plan** — BECAT EXTRACTION KB-prompt 分叉 + 166 Tier B + 437 UNSOURCED_MANUAL (06 旁枝 KB 层债)
- **Phase 7 RAG + KG 启动** — `docs/DESIGN_RAG_KG.md` 已完成, 实施前 5 步 handoff 已就绪

---

## Retrospective 三段 (per 规则 C)

### 保留下来的做法
- **Chrome DevTools MCP 全自动 sanity 测试** — 不需要人 paste-in-the-middle, 主 session 直接 fill/send/wait_for/抓 a11y snapshot 抽答案. R4 比 R3 (Chrome MCP 并行) 效率高 (5 题 ~30 min vs R3 17 题 ~50 min)
- **Strict 判据表格化 evidence** — 每题 evidence 用判据 × 答案 matrix, 命中率一目了然
- **Window 1/2 分批 + model caveat 显式标注** — 透明告知 Pro vs Flash-Lite 跑哪几题, evidence 不混淆
- **决策树预设 (r4_sanity_plan.md)** — 跑前已写好 5/5 PASS → APPROVE 路径, 跑完直接走流程不犹豫
- **TaskCreate 跟踪 5 题** — 主 session 不会丢失 task 状态

### 必须补上的缺口
- **Pro quota 4 题/window 估计偏乐观** — 实际 plan 假设 Window 1 跑 4 题, 但用户今早可能已用过 1 题, quota 只够 3 题. Future sanity plan 应预留 1 题缓冲 + 提前 verify quota status
- **Q1 model 不明示** — Q1 用 Gem default mode (没显式切 Pro), 后期 evidence 加 caveat. Future test 第一步必须 verify mode picker 当前选项
- **Flash-Lite 引入无关 framing 风险** — Q14 开头提"CM 合并用药" 不相关. 虽不影响 verdict, 但 evidence 解读需小心. Pro 似乎更 grounded
- **R4 全 17 题 deferred** — 本 sanity 不涉及 IS/AHP/timing 复杂题 (R3 4 FAIL 中已 dry-run 验过的 Q3/Q4/Q11/AHP1). v1.3 KB pass 时建议补全 17 题回归一次

### 关键决策复盘
- **决策 1 (跑 vs 等)**: 用户 Window 2 选 Flash-Lite 而不等 12:34 PM Pro 重置 — 加速 sanity 完成, 接受 model mix caveat. **判断**: 合理 (Window 1 已 3 ≥ baseline + 2 升级, 风险小, Flash-Lite 13/13 命中证实 prompt robustness)
- **决策 2 (5/5 PASS → APPROVE)**: 决策树明确 5/5 PASS = APPROVE, 不强求 Pro 重跑 Q6/Q14. **判断**: 合理 (Strict 判据全过 + Watch finding 全 LOW, v8.1 sanity 信号已足)
- **决策 3 (新 conversation per 题)**: 每题独立 conversation 避免 KV 污染, 但 quota 消耗也独立 (4/window 限制). **判断**: 合理 — 隔离更严谨, 但下次 plan 应估 quota 缓冲
- **决策 4 (Strict vs Pro Watch finding M2 候选数限 验证)**: Q2 列 6 候选 + Q6 列 5 timing 全展开, 验证 v8.1 M2 没 over-limit. **判断**: Watch finding 落实, v1.3 不需额外补 M2 验证

---

## Evidence 索引

| 文件 | 行数 | 内容 |
|---|---|---|
| `evidence/q01_sanity.md` | ~120 | Q1 GF EGFR (Pro 假设) PASS+ |
| `evidence/q02_sanity.md` | ~130 | Q2 CP CD4+ (Pro) PASS |
| `evidence/q05_sanity.md` | ~140 | Q5 FA/QS/CE (Pro) PASS+ |
| `evidence/q06_sanity.md` | ~150 | Q6 PK timing (Flash-Lite) PASS |
| `evidence/q14_sanity.md` | ~130 | Q14 AE+CE+MH+DS (Flash-Lite) PASS |
| `WINDOW_1_INTERIM.md` | ~80 | Window 1 halt 中转报告 (历史) |
| `R4_SANITY_RETROSPECTIVE.md` | (本文) | 终态 retrospective |
| `r4_sanity_plan.md` | 127 | 跑前 plan (parent dir) |
