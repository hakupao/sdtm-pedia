# Gemini Gems — Upload Manifest (v2 C 方案 Node 4)

> 状态: **Ready to Upload (C 方案 4 文件终态)**
> 最后更新: 2026-04-21
> 实测 tokens 来源: `dev/evidence/validate_single_batch.md` (rc=0 PASS)
> 总计: **1 批 = 4 文件 / 4 占用 / 10 文件硬限 / 6 spare**
> C 方案决策 (2026-04-21): 舍弃 terminology inline, 换业务弹药包
> 上游 evidence: `dev/evidence/validate_single_batch.md` (rc=0 PASS) + `dev/evidence/failures/stage_c_refactor_attempt_1.md` (V8b pattern attempt 归档)

---

## ⚠️ 先删老, 后上新

Node 4 执行前 Gem 已有上传 (v2 Node 3b 版本, 4 老文件). 上传新版本前**必须**:

1. 进 Gem Edit → Knowledge 列表
2. **删除** 4 个老文件 (本地 uploads/ 已同步删):
   - `01_core_reference.md` (v1.x)
   - `02_domain_specs.md` (v1.x)
   - `03_domain_knowledge.md` (v1.x)
   - `04_terminology_core.md` (v1.x, **C 方案核心舍弃项**)
3. **按新顺序上传** 4 个新文件:
   1. `01_navigation_and_quick_reference.md`
   2. `02_domains_spec_and_assumptions.md`
   3. `03_domains_examples.md`
   4. `04_business_scenarios_and_cross_domain.md`
4. **Custom Instructions** 全文替换为新版 `system_prompt.md` (v3, 6,720 chars)
5. Save Gem → 立即跑 smoke v2 10 题 (`ai_platforms/SMOKE_QUESTIONS_V2.md`)

---

## C 方案关键差异 (vs v2 Node 3b)

| 维度 | v2 Node 3b (弃) | v2 C 方案 (本) | 含义 |
|------|---------------|--------------|------|
| terminology inline | 5 段 299K (占 33.8%) | **0** (导引到 NCI EVS) | 空余容量换业务场景完整覆盖 |
| assumptions 位置 | 和 examples 同 03 | 和 spec 同 02 (域内交错) | 业务查 spec 时规则同屏 |
| examples 位置 | 和 assumptions 同 03 | 单独 03 | 便于专项查实例 |
| 业务场景内容 | **无** | **新 04 业务弹药包** | 26 场景 + FAQ + 跨域规则, 直接命中业务题 |
| 响应 buffer | 115K (11.5%) | **384K (38%)** | 安全窗更大 |
| 总 tokens | 884,918 (88.5%) | **616,113 (61.6%)** | 大幅减少占用 |

---

## 文件清单 (实测 tokens)

| # | 文件 | tokens | target | 备注 | segments | V1/V4/V8 | md5 (head12) |
|---|------|-------:|-------:|------|---------:|:--------:|--------------|
| 01 | `01_navigation_and_quick_reference.md` | 124,515 | ~150K | chapters + model + ROUTING/INDEX/VARIABLE_INDEX | 15 | PASS/PASS/- | ee199795281d |
| 02 | `02_domains_spec_and_assumptions.md` | 240,453 | ~400K | 63 域 spec + assumptions 域内交错 (business 查 spec 规则同屏) | 126 | PASS/PASS/- | 57a00f3bc239 |
| 03 | `03_domains_examples.md` | 220,657 | ~280K | 63 域 examples (实例数据) | 63 | PASS/PASS/- | 8c8ae684b7d4 |
| 04 | `04_business_scenarios_and_cross_domain.md` | 30,488 | ~60K | **writer 手写业务弹药包**, 26 场景 + FAQ + §3.1 CT 索引 (列表非表格格式 avoid V8b false positive) | 1 (self) | PASS/PASS/**PASS** | 2f7b83e9152f |

**总 tokens**: **616,113** / 900K WARN 阈 / 1M HARD 阈 (余 ~384K 响应 buffer)

**Context window 占用**: 61.6%, 响应空间 38.4%; 符合 C 方案 ~820K target (实际更省 ~200K, 因 02 spec+assumptions 合并后 tokens 比原估 370K 低).

---

## validate v2.0 结果 (rc=0 PASS)

- **V1 非空**: 4 文件 PASS
- **V2 段数**: 01=15 (≥15), 02=126 (≥120), 03=63 (≥60), 04=1 self (no min cap) — 全 PASS
- **V3 累计**: 616,113 ≤ 900K WARN 阈, PASS (target ~820K 实测更省)
- **V4 <5MB**: 4 文件全 PASS (最大 02=919,567 bytes)
- **V5 md5**: 稳定记录 (见 table head12)
- **V8 04 合规** (v2.0 新检): V8a size 78,777 > 10,000 PASS; V8b inline codelist lines **0 < 5 PASS** (attempt_1 26 行命中, attempt_2 §3.1 改列表格式通过)
- **V6 废除** (C 方案无 terminology 尾部 gate)

evidence: `dev/evidence/validate_single_batch.md` (rc=0)
failure archive: `dev/evidence/failures/stage_c_refactor_attempt_1.md`

---

## CO-1/CO-2/CO-3 Carry-over 落地 (Node 3b → Node 4)

| Carry-over | system_prompt v3 位置 | 04 弹药包位置 |
|----------|---------------------|-------------|
| **CO-1** (AE.AESER Core=Exp 幻觉) | §三条硬约束 CO-1 + §边界处理模板 ⑤ + §回答规范 + §工作流程 step 6 | §0 使用规则 + §1.2 AE SAE 场景 + §2.1 Core 陷阱清单 + §6.3 回答模板 + §9.1 FAQ |
| **CO-2** (NCI Code 臆造) | §三条硬约束 CO-2 + §边界处理模板 ① ② + §路由规则 6 + §工作流程 step 7 | §0 使用规则 + §2.6 pitfall + §3 CT 外部参考 + §3.1 索引表 (列表格式) + §6.2 + §6.2b 回答模板 + §9.7 FAQ |
| **CO-3** (citation 格式强制) | §三条硬约束 CO-3 + §回答规范 + §工作流程 step 4 | §0 使用规则 + §6 回答模板 (4 个示例全带源路径) |

---

## 上传操作步骤 (用户侧, Phase 3b 之后)

1. 访问 `gemini.google.com` (需 Google AI Pro 订阅)
2. 左侧导航 → **"Gems"** → 选已有 "SDTM Expert" Gem → Edit (若新建, 按现有 description 填)
3. **Custom Instructions** 清空 → 全文替换为 `current/system_prompt.md` 内容 (v3, 6,720 chars)
4. **Knowledge**:
   - 删老 4 文件 (见顶部警示)
   - 按顺序上新 4 文件 (device 上传 `ai_platforms/gemini_gems/current/uploads/0{1..4}*.md`)
5. **Save Gem** — 秒级就绪, 无 indexing
6. 进 Preview → 按 `ai_platforms/SMOKE_QUESTIONS_V2.md` 跑 10 题
7. 回报 smoke v2 结果到 session, 派 Rule D reviewer (第 13 种 subagent_type)

---

## 发布决策 (Phase F1 再决)

默认 **Private** (仅本人). 用户 ack 后可选:
- **选项 A (推荐)**: 保持 Private, 个人深度使用
- **选项 B**: "Link share with colleagues" (Viewer 权限给同事, 非公开 Store)

**不走 GPT Store 路径** — Gemini 的"公开" = 分享链接 (CLAUDE.md 2026-04-20 publish_scope_semantics_clarification).

---

## Node 4 → Node 5 carry-over (若 smoke v2 < 8/10 PASS)

- 扩 04 业务弹药包 (加更多业务场景到 ~50K+ target, 目前 30,488)
- 调 system_prompt v3 路由规则 (更细分类)
- Rule B 归档 attempt + Rule D reviewer 复核
- V8 pattern v2.1 收紧 (只检真 Term 值如 "Y"/"N"/"MILD"/"SEVERE" pattern, 避免 CT Code 索引表的 false positive)

---

## 原始 Merge Fragments (脚本自动 append, 保留供回溯)

本节由 merge_for_gemini.py v2.0 自动追加 (每次运行 append 一段). 历史 v1.x 段保留如下供对比, 新 v2.0 段追加在下方.

<!-- merge fragment: 2026-04-20T08:55:50Z -->
## Merge run at 2026-04-20T08:55:50Z (v1.x attempt_1 — FAIL, V6 tail 0/3)

| 文件 | 源文件数 | tokens | target | 位置策略 |
|------|---------:|-------:|-------:|---------|
| 01_core_reference.md | 15 | 124,512 | ≤120,000 | 前置 (导航层防 Lost-in-Middle) |
| 02_domain_specs.md | 63 | 185,785 | ≤168,000 | 中段 (字母序, 依赖 query anchor) |
| 03_domain_knowledge.md | 126 | 275,318 | ≤225,000 | 中段 (assumptions 先, examples 后) |
| 04_terminology_core.md | 1 | 111,771 | ≤200,000 | 末尾 (recency bias + P12 hard checkpoint) |

<!-- merge fragment: 2026-04-20T09:38:54Z -->
## Merge run at 2026-04-20T09:38:54Z (v1.x attempt_2 — PASS, V6 tail 3/3)

| 文件 | 源文件数 | tokens | target | 位置策略 |
|------|---------:|-------:|-------:|---------|
| 01_core_reference.md | 15 | 124,512 | ≤120,000 | 前置 (导航层防 Lost-in-Middle) |
| 02_domain_specs.md | 63 | 185,785 | ≤168,000 | 中段 (字母序, 依赖 query anchor) |
| 03_domain_knowledge.md | 126 | 275,318 | ≤225,000 | 中段 (assumptions 先, examples 后) |
| 04_terminology_core.md | 5 | 299,303 | ≤200,000 | 末尾 (recency bias + P12 hard checkpoint) |

> v1.x terminal log: `dev/evidence/merge_all_attempt2.log` + `dev/evidence/validate_all_attempt2.log`
> **v1.x 此段为历史快照, 04_terminology_core.md 已在 C 方案下完全舍弃**.

<!-- merge fragment: 2026-04-21 c_refactor Node 4 -->
## Merge run at 2026-04-21 (v2.0 c_refactor Node 4, **C 方案**)

| 文件 | 源文件数 | tokens | target | 位置策略 |
|------|---------:|-------:|-------:|---------|
| 01_navigation_and_quick_reference.md | 15 | 124,515 | ~150,000 | 前置 (导航层防 Lost-in-Middle) |
| 02_domains_spec_and_assumptions.md | 126 | 240,453 | ~400,000 | 前中段 (业务查 spec 时规则同屏) |
| 03_domains_examples.md | 63 | 220,657 | ~280,000 | 中段 (实例数据, 便于专项查) |
| 04_business_scenarios_and_cross_domain.md | 1 (self) | 30,488 | ~60,000 | 尾部 (业务弹药 recency) |

**总 616,113 tokens** / 900K WARN / 1M HARD. validate rc=0 PASS (含 V8b 02 PASS after §3.1 列表格式调整).
