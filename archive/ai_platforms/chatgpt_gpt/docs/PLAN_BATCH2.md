# ChatGPT GPTs — Batch 2 规划 (Node 4)

> **状态**: draft 2026-04-21, 等用户 ack
> **上下文**: 用户 Node 3b 反思后决策 (2026-04-21): ChatGPT 维持原 batch 2 策略, 保留 terminology (不和 Gemini 同步舍弃)
> **现状**: Batch 1 = 4 文件 310K tokens (navigation / chapters / model / domain_specs), 20 文件硬限剩 16 槽位
> **目标**: Batch 2 补 63 域 assumptions + 63 域 examples + terminology 精选, 覆盖 ~80-90% KB 源内容

---

## 决策依据

1. **ChatGPT 走 RAG**: 每问只检索相关 chunk, 不强制 ≤1M 全量, 20 文件硬限是主约束
2. **用户决策 2026-04-21**: 维持原 batch 2 计划, 继续加 terminology (和 Gemini 策略分化, 便于两平台对比)
3. **架构差异**: ChatGPT = RAG, 可容 ~20 文件 × ~500MB/文件 ≈ 10GB 理论上限; Gemini = full context, 1M token 硬顶. 两平台策略性错位

---

## 当前 batch 1 (已上传, Node 3b smoke v1 跑过)

| # | 文件 | tokens | sources | 定位 |
|---|------|--------|---------|------|
| 01 | `01_navigation.md` | 46,170 | 3 | ROUTING + INDEX + VARIABLE_INDEX |
| 02 | `02_chapters_all.md` | 60,607 | 6 | ch01/02/03/04/08/10 |
| 03 | `03_model_all.md` | 17,653 | 6 | Model 01-06 |
| 04 | `04_domain_specs_all.md` | 185,704 | 63 | 63 域 spec |
| **合计 batch 1** | **310,134** | **78** | |

---

## Batch 2 规划 (5 文件新增, 9 文件总)

### 估算 (基于 KB 源实测 bytes 反推 tokens)

| KB 源 | 文件数 | source bytes | est tokens (bytes/4) | 备注 |
|--------|:----:|------:|------:|------|
| 63 域 assumptions.md | 63 | ~1.5 MB | ~400K | TableAware + heading chunking |
| 63 域 examples.md | 63 | ~2 MB | ~500K | 实例数据多, 较大 |
| terminology/core (41 files) | 41 | ~4.5 MB | ~1.1M | 大头 |
| terminology/questionnaires (43 files) | 43 | ~1.5 MB | ~400K | 问卷详表 |
| terminology/supplementary (6 files) | 6 | ~0.4 MB | ~100K | 补充 |
| **合计新增预估** | **216 sources** | **~9.9 MB** | **~2.5M tokens** | 远超单文件容量 |

### 文件分配 (5 文件新增)

| # | 新文件 | sources | est tokens | cap | buffer | 定位 |
|---|-------|:----:|-----------:|------:|------:|------|
| 05 | `05_assumptions_all.md` | 63 | ~400K | 450K | 11.1% | 63 域 assumptions 合并, **按 PLAN §3.1 P0-P2 score 排序** |
| 06 | `06_examples_all.md` | 63 | ~500K | 560K | 10.7% | 63 域 examples 合并, 保持实例完整 |
| 07 | `07_terminology_core_high_freq.md` | 41 中精选 ~15 | ~400K | 450K | 11.1% | 高频 codelist: AE / DM / LB / VS / EG / PK / 通用 general / findings / interventions / disposition / special_purpose / trial_design |
| 08 | `08_terminology_questionnaires_and_supp.md` | 43 + 6 = 49 | ~500K | 560K | 10.7% | 问卷 43 + 补充 6 全量 (相对独立, 合并一文件可 RAG 分 chunk) |
| 09 | `09_terminology_core_mid_tail.md` | 41 剩 ~26 | ~700K | 780K | 10.3% | 低频 codelist: general_part2-5 / microbiology / pk_part1-4 / oncology_part2 / other_part1-5 / is_domain / eg_part2-3 / cp_part2 等 |
| **合计 batch 2 新增** | ~240 | **~2.5M** | | | |
| **batch 1+2 合计** | 9 文件 | ~2.81M tokens | | | **16/20 spare 11 槽位** |

### Terminology 精选策略 (07 vs 09 分档)

**高频 (07)** 选入依据:
- 业务 query 频次 (AE / DM / LB / VS 等每次研究必用)
- 对 smoke v2 10 题的覆盖价值
- 常问 codelist (如 NY Response C66742 / Severity C66769)

**低频 (09)** 进入依据:
- 冷门域 terminology (oncology subcategories / microbiology / cp / is / other)
- 精细 codelist (专项研究)

**分档不是硬删**, 只是**文件归档**, RAG 检索时两文件都命中.

---

## 单文件 cap 和 ChatGPT RAG 限制验证

### ChatGPT GPT Knowledge 限制 (OpenAI 官方)
- 每 GPT ≤ 20 文件
- 每文件 ≤ 512 MB (估 2M tokens, 本 plan 每文件 ≤ 780K tokens, 安全 buffer 60%)
- 每文件会被 chunking + embedded, 非 full context
- 查询时 retrieval top-k 命中检索 chunk (默认 top_k=20)

### 精选脚本约束 (merge_for_chatgpt.py v1.4 需升级)
- 新增 `--stage batch2` CLI 选项
- P12 source marker `<!-- source: knowledge_base/... -->` 在每 source 起始
- P13 TableAware chunking (表跨 heading 不裂)
- V5 md5 + V4 heading + V3 source count + V7 manifest 真源 + V1 文件数 ≤ cap + V2 总 tokens ≤ cap

---

## 执行步骤 (Node 4)

### Step 1. merge_for_chatgpt.py v1.4 扩展

- 新增 `_collect_assumptions_sources()` 按域字母序
- 新增 `_collect_examples_sources()` 按域字母序
- 新增 `_collect_terminology_sources(tier='high'/'mid_tail')` 按频次排序
- manifest_segments.json 新增 batch2 5 个文件的 segments 真源
- py_compile + Rule D reviewer 第 12/13 种 subagent_type 独立审

### Step 2. 跑脚本 + V5 merge + validate

- `python dev/scripts/merge_for_chatgpt.py --stage batch2` → 5 个新文件 + 日志
- `python dev/scripts/validate_chatgpt_stage.py --stage batch2` → V1-V7 check
- 失败归档 Rule B
- Rule A N=5 抽检 (批 2 压缩率估 >50%, 需强制)

### Step 3. 上传 5 文件 到现有 GPT

- 按 score 升序 (低频 09 先 → 高频 07 后 → assumptions 05 → examples 06 → questionnaires 08)
- 每文件等 Processing → Ready
- 或按依赖: 05 assumptions 先 (支撑业务规则) → 06 examples → 07/09 terminology → 08 questionnaires/supp

### Step 4. smoke v2 10 题重跑

- 共用 `ai_platforms/SMOKE_QUESTIONS_V2.md` 10 题
- 落档 `dev/evidence/smoke_v2_results.md`
- Rule D 第 12 种 subagent_type 审
- 目标 ≥ 8/10 PASS

### Step 5. system_prompt.md 微调

- 原 v1 `system_prompt.md` 路由表只涵盖 batch 1 的 4 文件
- 新增: 05 (业务规则) / 06 (实例) / 07-09 (terminology) 的路由规则
- 新增: 术语题必引 04_terminology_* 文件 + 给 NCI EVS 外链补
- Instructions ≤ 7500 chars 预算守恒

### Step 6. upload_manifest.md v2 + A/B 预演

- 新 `current/upload_manifest.md` 反映 9 文件 batch 1+2
- manifest_segments.json 同步
- Phase 5 完整 A/B 前可预演 smoke v2 10 题 2 轮以估 PASS 率收敛

---

## 风险 + 缓解

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| 07/09 terminology 精选偏差 | 中 | 冷门 codelist 被分到 "09 低频" 但用户常问 | Phase 5 全量 A/B 10 题 + 5 道冷门 codelist 抽查; 若偏差大迭代分档 |
| 05 assumptions 合并超 450K cap | 中 | V2 FAIL | 预估 400K 有 12.5% buffer, attempt_2 cap 升 500K 可接 |
| 06 examples 合并超 560K cap | 中 | V2 FAIL | 同上, cap 调节空间大 |
| ChatGPT 用户每文件 RAG top-k 命中率低 | 中 | smoke PASS 率受影响 | 统计命中率 (开 ChatGPT 开发者模式可见 "Retrieved X chunks"), 调 chunk_size 或增 top-k |
| 重复上传时, File Search index 需重 build | 低 | 本 session 不阻塞, 下 session 等 Ready 延迟 | Node 4 规划预留 30 分钟 indexing 时间 |

---

## 变更记录

| 日期 | 变更 | 原因 |
|------|------|------|
| 2026-04-21 | batch 2 规划 draft 建立 | Node 3b 完成 + 用户 ack ChatGPT 维持原计划保留 terminology |

---

*Batch 2 ack 路径: 用户 review 本文件 → ack 5 文件架构 + terminology 分档策略 → 派 executor opus 改 merge_for_chatgpt.py v1.4 + 跑 → smoke v2 10 题实测*
