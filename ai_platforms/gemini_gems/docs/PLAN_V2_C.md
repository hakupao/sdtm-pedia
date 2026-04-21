# Gemini Gems — C 方案 (Node 4 重整架构)

> **状态**: draft 2026-04-21, 等用户 ack
> **上下文**: 用户 Node 3b 反思后决策 (2026-04-21): 舍弃 terminology, 空余容量为"业务问答专家"优化, 不为"字典查询"优化
> **废弃**: 当前 4 文件架构 (01_core_reference + 02_domain_specs + 03_domain_knowledge + **04_terminology_core**)
> **取代**: C 方案新 4 文件架构, 04 从 terminology 换成"业务弹药包"

---

## 决策依据 (3 份官方文档 + 用户判断)

1. **ai.google.dev/gemini-api/docs/long-context** 原文: "Gemini's extensive context window invites a more direct approach: **providing all relevant information upfront**" → **全量灌 1M context, 非 RAG**
2. **support.google.com/gemini/answer/14903178**: "If you exceed the context window, this could lead to responses that don't take into account all the content provided or **miss connections or details** throughout the content" → 超 1M 静默丢失
3. **用户决策 2026-04-21**: terminology 完全舍弃 (由 NCI EVS Browser 承担), 空余容量加**业务问答**直接相关内容

---

## 当前 vs C 方案对比

### 当前 (v2, 已上传, Node 3b smoke v1 跑过)

| 文件 | tokens | sources | 定位 |
|------|--------|---------|------|
| 01_core_reference | 124,512 | 15 | chapters + model + 导航 |
| 02_domain_specs | 185,785 | 63 | 63 域 spec |
| 03_domain_knowledge | 275,318 | 126 | 63 域 assumptions + examples |
| **04_terminology_core** | **299,303** | **5** | **5 段高频 codelist inline 全文** |
| **合计** | **884,918 (88.49%)** | **209** | |

### C 方案 (重整)

| # | 文件 | est tokens | sources | 定位 |
|---|------|-----------:|--------:|------|
| 01 | `01_navigation_and_quick_reference.md` | ~150K | 15 + expansion | ROUTING 详表 + INDEX + VARIABLE_INDEX **扩展速查** + 6 章节 + 6 model |
| 02 | `02_domains_spec_and_assumptions.md` | ~370K | 126 | 63 域 spec **合并** 63 域 assumptions (同域内 spec + 规则邻近, 业务问答时一站式) |
| 03 | `03_domains_examples.md` | ~250K | 63 | 63 域 examples (实例数据, 保留完整) |
| 04 | `04_business_scenarios_and_cross_domain.md` | ~50K | 自编 + 引用 | **业务弹药包**: 跨域场景 / 常见映射 pitfall / 术语外引 EVS 说明 / RELREC vs SUPP 选择 / ISO 8601 Study Day / CTCAE↔AESEV 等 10+ 常问话题 |
| **合计** | **~820K (82%)** | **~204** | 留 **180K buffer** (18%) 给响应 + 对话 |

### 关键差异

| 维度 | 当前 | C 方案 | 含义 |
|------|------|--------|------|
| terminology inline | 5 段 299K (占 33.8%) | **0** (导引到 NCI EVS) | 用户问 codelist 具体 term → 边界模板 + 外链 |
| assumptions 位置 | 和 examples 同文件 | 和 spec 同文件 | 业务查变量 spec 时规则同屏, 减查询跳转 |
| examples 位置 | 和 assumptions 同文件 | 单独 | 便于专项查实例 |
| 业务场景内容 | **无** | **新增 04, 50K 弹药** | 跨域规则 / FAQ / pitfall 汇总, 直接命中业务题 |
| 响应 buffer | 115K (11.5%) | **180K (18%)** | 安全窗更大 |

---

## 04 业务弹药包内容清单 (新编, ~50K 预算)

### §1. 跨域场景 (15-20 短条目)

每条 ~200-500 字, 结构: **场景 → SDTM 映射 → 变量示例 → pitfall warning**

1. 合并用药同服多药, CM 拆记录规则
2. AE 升 SAE 判定 + Serious 子变量 (AESER / AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE)
3. 病史持续至试验 → MH 和 CM 双域记录
4. PK 采样 < LLOQ 的 PCORRES / PCSTRESN 记法
5. ISO 8601 部分精度 + Study Day 计算规则
6. LB 结果 + LBNRIND 三档 (L/N/H) 映射
7. Arm vs ActArm 中途换组处理
8. AESEV vs CTCAE Grade 1-5 映射
9. 同一事件跨域关联 → RELREC vs SUPPAE/SUPPCM 选择
10. SUPP-- 存储边界 (何时用 / 何时加标准变量)
11. DM.ARMCD 必须匹配 TA.ARMCD 键约束
12. General Observation Class (Events / Findings / Interventions) 分类决策
13. Subject Reference Start/End Date (RFSTDTC / RFENDTC) 在 Study Day 计算里的角色
14. EDC → SDTM 的常见 NULL 约定 (空 / 无数据 / 未收集 区分)
15. Controlled Terminology extensible vs non-extensible 规则

### §2. 常见 pitfall 警示

- LBSTRESN 不能写 "<LLOQ" (字符应走 LBSTRESC)
- AESEV ≠ AESER (两维度别混淆)
- MH 和 CM 不是互斥 (持续病史可双记)
- RELREC 不是 SUPP-- (跨域关系 vs 同域补充)
- Study Day = 1 (起始日为 Day 1 非 Day 0)
- ISO 8601 `T` 分隔符日期时间
- AESTDTC 精度允许到秒, 部分精度合法

### §3. Controlled Terminology 外部参考

- **NCI EVS Browser**: `https://evsexplore.semantics.cancer.gov/evsexplore/` — 查任一 codelist 的 term / submission value / synonym / extensible 标志
- **SDTM CT Package** release notes: 每 Q1-Q4 更新
- 本 Gem **不 inline** 具体 codelist term, 原因: 1M context 窗口物理限制下牺牲 terminology 换取业务规则 + 示例完整覆盖
- 用户问具体 term → Gem 答 "请查 NCI EVS Browser 搜索 C<code>" 而非臆造

### §4. 10 题 smoke v2 判据映射 (供自测对照)

对照 `ai_platforms/SMOKE_QUESTIONS_V2.md` 的 10 题 Q1-Q10, 每题指向本 04 文件对应 section.

---

## 执行步骤 (Node 4)

### Step 1. 脚本改造 (dev/scripts/merge_for_gemini.py v2.0)

- 新增 `--stage c_refactor` CLI 选项
- 删除 _collect_terminology_sources() 调用
- 合并 _collect_spec_sources() + _collect_assumptions_sources() → `_collect_spec_and_assumptions_sources()` (按域字母序, 每域 spec 后紧跟 assumptions)
- 独立 _collect_examples_sources() 生成 03
- 新建 _write_business_scenarios() (模板生成 04 起骨架, 实际内容由主 session 填充)
- 实测 md5 稳定 + V5 check PASS

### Step 2. 业务弹药包 04 编写

- Writer: executor opus subagent 按 §1 15-20 条目 + §2 pitfalls + §3 EVS 导航 + §4 smoke 映射
- 预算 ~50K tokens, 超则削 §1 条目数
- 产物: `ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md`
- Reviewer: 第 12 种 subagent_type (规则 D) 独立审 04 业务准确性 + 跨源一致 + 无 codelist inline 违反

### Step 3. Merge + Validate

- 重跑 merge_for_gemini.py --stage c_refactor
- 重跑 validate_gemini.py: V1 不变 + V2 放宽 (不再要求 terminology ≥3) + V6 废 (无 tail terminology gate) + 新加 V8 (04 弹药包非空 + 无 codelist term 字面值)
- 失败归档 Rule B

### Step 4. 重上传 + smoke v2 10 题

- 删当前 Gem knowledge → 上 4 新文件按 01→02→03→04
- 跑 SMOKE_QUESTIONS_V2.md 的 10 题
- 落档 `dev/evidence/smoke_v2_results.md`
- Rule D 第 12 种 subagent_type 审 smoke 答题质量
- 目标 ≥ 8/10 PASS, 若 < 8 则 FAIL_REWORK (04 弹药或 system_prompt 迭代)

### Step 5. system_prompt.md 微调

- 原 `system_prompt.md` 的 "04_terminology_core" 引用 → 更新为 "04_business_scenarios"
- 路由规则加: 用户问具体 term → 先看 04 §3 导航 + 给 NCI EVS 外链, 不臆造
- §知识库组成: 更新为新 4 文件比例

### Step 6. upload_manifest v2 + 评估

- 新 `current/upload_manifest.md` 反映 C 方案
- manifest_segments 同步更新
- Node 4 终态评估: 新架构 vs 当前 (Node 3b v1 时) 的业务题命中率对比
- 如显著优于当前 → Phase 4 进回归 + 完整 A/B 1 轮 (10 题 v2)
- 如不显著 → 反思架构并迭代

---

## 风险 + 缓解

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| 04 业务弹药包内容编写慢 | 中 | Node 4 时间拉长 2-3 天 | executor subagent opus 自动化编, 主 session 审. 复用 SDTMIG chapters 内容, 不新编纯原创 |
| 合并 02 spec + assumptions 后超 400K | 低 | V5 FAIL | 预测 spec 186K + assumptions 275K/2 = ~320K (假设一半 assumptions 为 examples 已在 03). 需要实测 |
| 用户改主意要回填 terminology | 低 | 重做 | C 方案 04 设计**保留 terminology_map 22K + EVS 导航**, 用户要回填时按需扩 |
| 10 题 smoke v2 PASS 率 < 8 | 中 | C 方案设计需迭代 | 留 180K buffer 给 system_prompt 扩 / 04 弹药扩 |

---

## 变更记录

| 日期 | 变更 | 原因 |
|------|------|------|
| 2026-04-21 | C 方案 draft 建立 | Node 3b smoke v1 暴露字典查题设计错 + 1M context 物理限制不能全量 terminology, 用户决策舍弃 |

---

*C 方案 ack 路径: 用户 review 本文件 → ack 4 文件架构 → ack 04 弹药包 15-20 条目清单 → 派 executor opus 写 04 + 重跑脚本 → smoke v2 10 题实测*
