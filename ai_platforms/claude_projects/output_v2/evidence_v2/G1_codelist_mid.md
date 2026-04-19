# G1 — 批 5 中频 codelist 清单 (rank 201-500)

> Stage: v2.5 (batch 5) preparation
> Script: `scripts_v2/score_codelists.py` (与 F1 同一脚本, 无修改)
> Log: `G1_codelist_score.log` (与 `F1_codelist_score.log` byte-identical, 幂等验证 PASS)
> Codelist 列表: `G1_codelist_mid.txt` (300 C-code, 一行一 code)
> Completed: 2026-04-19 (主控 review)

## 幂等性验证 (规则 A 子项)

```
diff -q F1_codelist_score.log G1_codelist_score.log  # rc=0, byte-identical
```

score_codelists.py 是纯读取脚本, 无随机性, 无外部依赖; 从同一 knowledge_base snapshot 跑两次输出完全一致. 本 G1 log 仅为 evidence 归档, 无新计算.

## 得分公式 (沿用 F1)

```
score = 0.5 * normalize(domain_ref_count)
      + 0.3 * sigmoid_term(term_count)
      + 0.2 * (50 if c_code in T_codelist_hits else 0)
```

T_codelist_hits (NY + FREQ) 已全部在批 4 命中 (rank 1/2), 本批不含加分 codelist. 分数纯由 domain_ref_count + term_count 驱动.

## T_codelist_hits 审计 (PLAN §G1 门回放)

| short_name | c_code | rank | 所在批 |
|-----------|--------|------|--------|
| NY | C66742 | 1 | 批 4 (v2.4 已命中, T17/T7 ↑ 质变 PASS) |
| FREQ | C71113 | 2 | 批 4 (v2.4 已命中; T19 批 5 原定测试点, 现在回归验证) |
| AERELN | — | — | knowledge_base 未收录 (spec 兼容, T18 边界声明 PASS) |
| PROBLEM_TYPE | — | — | knowledge_base 未收录 (T20 批 5 原定测试点需改配) |

**PLAN §G1 门**: 批 5 rank 201-500 无 T_codelist_hits 新入驻 (两个已收录的 T_hit 都在批 4). 批 5 测试题 T19 (FREQ) 已在批 4 完全命中, T20 (PROBLEM_TYPE) 始终缺源, 需在 G4 checkpoint 设计时改配为 "边界声明" 样式测试点 (沿用 T18 模板) 或替换为 mid tier 真实存在的 codelist (如 Route of Administration / Severity 之类).

## 容量预算

| 指标 | 值 |
|-----|-----|
| Total codelists | 1005 |
| 批 4 (top 200) 估算 tokens (spec 简化) | 201,660 (term_count × 30) |
| 批 4 实际 tokens (F2 产出) | 351,752 (含 Synonyms + NCI + Related Domains) |
| **批 5 (rank 201-500) 估算 tokens (spec 简化)** | **338,070** (term_count × 30) |
| 批 5 mid tier 算法调整系数 | mid tier 去 Synonyms + 去 NCI Description + Definition ≤100 字符, 估 real/heuristic ≈ 0.55-0.70 |
| **批 5 实际预期 tokens (mid 算法调整)** | **~190-240K** |
| v2.4 累计 (实际) | 719,241 tokens |
| **v2.5 预计终态 tokens** | **~910K-960K** (远低于 PLAN §G3 C12 硬约束 1.5M) |
| PLAN §G2 12a/12b 拆分目标 | 各 ~250K, 12a core + 12b questionnaires |

**结论**: mid tier 去大段 (Synonyms + NCI) 后的真实 token 值应与 PLAN §G2 "各 ~250K" 预估匹配. G2 按 top 300 全量抽取, 落盘后再按实际 token 决定拆 12a/12b 边界.

## 分布观察 (主控 review)

### 分数分布

| 段 | 内容 | rank 范围 | 分数区间 |
|----|------|----------|---------|
| 头部 | Tumor/Lesion Result + Q20 airway + Cardiovascular FA + Rivermead Concussion + Chronic Respiratory 长家族 (含 1st/Follow-up/Parent/Proxy 多版本) + Duchenne MDSTAT + Harvey-Bradshaw IBD + Beck Depression + Kansas City Cardiomyopathy 等多个 PRO/QRS pair | 201-260 | 0.26x (平台) |
| 中段 | EORTC/QLQ QRS 家族多分支版本 + AIDS HIV Dementia + Yale Social Support + Somatic Symptom + PROMIS pediatric/adult | 261-400 | 0.22x-0.25x |
| 尾部 | 小众 + 罕见 questionnaire (Hypoglycemic Confidence, Work Productivity 2.0, Edinburgh Postnatal, Prostate Specific QoL 等) | 401-500 | 0.209 (平台) |

- 无 "score cliff" 拐点: 从 rank 201 (0.261) 到 rank 500 (0.209) 平滑衰减 ~20%, 无自然批 5 边界信号. rank 500 是 PLAN 规定的 hard cap.
- 整体仍是 **QRS/PRO pair 主导** (Test Name + Test Code 对称冗余), 每 pair 同分, 这是 CDISC CT 客观结构.
- 批 4 已收录的核心 SDTM codelist (Epoch/Unit/Not Done/Evaluator 等) 本批不重复; 批 5 几乎是纯 questionnaire tier.

### 内容类型

批 5 ≈ **300 个 QRS/PRO questionnaire codelist**, 90%+ 是 Test Name / Test Code pair 形式. 这意味着:
- mid tier 算法 "去 Synonyms" 特别有效 — questionnaire terms 大量重复 submission values, synonyms 冗余高
- Definition 截断 ≤100 字符 损失小 — questionnaire items 本身命名已较短
- "12a core + 12b questionnaires" 拆分可能需调整为 "12a Findings/Events/Interventions + 12b QRS/Questionnaires", 因为批 5 ~90% 是 questionnaire, 若 strict 按 core/questionnaires 划, 12a 会很小

## 预计 F1 → G1 整体覆盖

| 级别 | 量 | 说明 |
|------|----|------|
| Total CDISC codelists | 1,005 | 100% |
| v2.4 覆盖 (批 4 top 200) | 200 | 19.9% |
| **v2.5 覆盖 (批 4+5, top 500)** | **500** | **49.8%** — 中庸 50% 覆盖目标达成 |
| v2.5 后未收录 | 505 | 50.2% (long tail, 低优先级; Phase 7 RAG 方案可补) |

## 交接给 G2

G2 任务: 实现 `scripts_v2/extract_terminology_terms.py --tier mid` (当前 stub 返回 rc=2 NOT_IMPLEMENTED).

**G2 算法差异 (vs tier=high, 沿 PLAN §G2)**:
1. 完整保留 Code + Term + Definition (截断 ≤100 字符, vs high tier 的 ≤200)
2. 不保留 Synonyms 大段
3. 不保留 NCI Concept Description 链接
4. 保留 codelist-header 级 Related Domains 行 (与 high tier 一致, 结构省 token)
5. 必拆 12a_terminology_mid_core.md + 12b_terminology_mid_questionnaires.md (按 terminology subdir, 与 11a/11b/11c 相同路由)
6. Reviewer 抽样 N=10 (规则 A 强制, 因 mid tier 压缩率更高)

**G2 输入**: `evidence_v2/G1_codelist_mid.txt` (300 C-code, 与 F1_codelist_high.txt 同格式)

**G2 实现要点 (vs F2)**:
- `extract_terminology_terms.py` 第 285-290 行 `--tier mid` 当前是 stub (`print NOT_IMPLEMENTED, return rc=2`); 需实现 mid tier 分支
- 复用 `parse_codelists` / `build_codelist_index` / `build_domain_index` (tier-agnostic)
- 新增 `_truncate_definition_mid` (100 字符) 或在现有函数基础上传 tier 参数
- `render_codelist` 按 tier 分支跳过 Synonyms 列 / NCI Description 链接
- `build_subdir_documents` 需对 mid tier 产出 12a/12b 路径 (而非 11a/11b/11c)

**G2 reviewer 要点**:
- 抽样 10 codelist 独立 read 源 vs 产出, 验证 Term 表无丢失
- 验证 Definition 截断无中途截词 (应在单词/句子边界)
- 验证 idempotency (rc=0 两次跑 MD5 一致)

Commit 路径: `Phase 6.5 v2 G1: rank 201-500 codelist mid 清单 (~300 codelist, v2.5 准备)`
