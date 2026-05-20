# A3 — Tier B Candidates Queue (sorted by priority)

> Date: 2026-05-20
> Source: `branches/06_deep_verification/section_coverage.jsonl` (399 sections total)
> Filter: aggregate_verdict ∈ {SIBLING_DROPPED, CONTENT_TRUNCATED} ∧ keyword_flag ∈ {level1, level2}
> Pool: **49** candidates (166 Tier B total - 117 keyword=None)
> Sort: level1 first, then by missing+partial atom count desc
> v1.3 PLAN.md A3 target: 20-30 节 — 选 ranks 1-25 (level1 全 25) + 部分 level2

---

## 1. 49 候选完整列表

### Level 1 — shall/MUST/required/may not (25 节)

| Rank | Verdict | Missing | Partial | Keyword | PDF Pages | section_id | Batch |
|:-:|---|:-:|:-:|---|---|---|:-:|
| 1 | CONTENT_TRUNCATED | 112 | 62 | MUST | 199-220 | ig34_§6.3.5.3 | **H** |
| 2 | CONTENT_TRUNCATED | 48 | 39 | MUST | 62-78 | ig34_§5.2 | **H** |
| 3 | CONTENT_TRUNCATED | 69 | 7 | MUST | 241-248 | ig34_§6.3.5.6 | **H** |
| 4 | CONTENT_TRUNCATED | 45 | 1 | MUST | 267-271 | ig34_§6.3.5.9.1 | **H** |
| 5 | CONTENT_TRUNCATED | 34 | 0 | required | 46-48 | ig34_§4.4.10 | **H** |
| 6 | CONTENT_TRUNCATED | 30 | 4 | MUST | 180-182 | ig34_§6.3.1 | **H** |
| 7 | CONTENT_TRUNCATED | 27 | 5 | may not | 171-178 | ig34_§6.2.6 | **H** |
| 8 | CONTENT_TRUNCATED | 31 | 1 | required | 424-425 | ig34_§7.4.2.1 | **H** |
| 9 | CONTENT_TRUNCATED | 20 | 1 | MUST | 60-62 | ig34_§5.1 | **H** |
| 10 | CONTENT_TRUNCATED | 20 | 1 | may not | 399-402 | ig34_§7.2.1 | **H** |
| 11 | CONTENT_TRUNCATED | 4 | 14 | MUST | 15-16 | ig34_§2.7 | **M** |
| 12 | CONTENT_TRUNCATED | 9 | 2 | MUST | 363-364 | ig34_§6.4.2 | **M** |
| 13 | CONTENT_TRUNCATED | 4 | 7 | MUST | 394-396 | ig34_§7.2.1 (dup) | **M** |
| 14 | CONTENT_TRUNCATED | 9 | 0 | MUST | 410-412 | ig34_§7.3.2 | **M** |
| 15 | CONTENT_TRUNCATED | 7 | 1 | MUST | 415 | ig34_§7.3.3 | **M** |
| 16 | CONTENT_TRUNCATED | 7 | 0 | may not | 52 | ig34_§4.5.1.2 | **M** |
| 17 | CONTENT_TRUNCATED | 6 | 0 | MUST | 350-352 | ig34_§6.3.12.2 | **M** |
| 18 | CONTENT_TRUNCATED | 5 | 1 | MUST | 364 | ig34_§6.4.3 | **M** |
| 19 | CONTENT_TRUNCATED | 5 | 1 | MUST | 402 | ig34_§7.2.1.1 | **M** |
| 20 | CONTENT_TRUNCATED | 5 | 0 | may not | 37 | ig34_§4.3.5 | **M** |
| 21 | CONTENT_TRUNCATED | 3 | 0 | MUST | 448-450 | ig34_Appendix_D | **S** |
| 22 | CONTENT_TRUNCATED | 2 | 1 | MUST | 22-23 | ig34_§4.1.5 | **S** |
| 23 | SIBLING_DROPPED | 2 | 0 | MUST | 404-405 | ig34_§7.2.2 | **S** |
| 24 | CONTENT_TRUNCATED | 2 | 0 | may not | 409-410 | ig34_§7.3.1.1 | **S** |
| 25 | CONTENT_TRUNCATED | 1 | 0 | MUST | 29 | ig34_§4.2.4 | **S** |

### Level 2 — should/cannot/only/except (24 节, 部分进入 v1.3 scope)

| Rank | Verdict | Missing | Partial | Keyword | PDF Pages | section_id | Batch |
|:-:|---|:-:|:-:|---|---|---|:-:|
| 26 | CONTENT_TRUNCATED | 105 | 23 | should | 228-241 | ig34_§6.3.5.5 | (deferred v1.4) |
| 27 | CONTENT_TRUNCATED | 99 | 6 | cannot | 252-256 | ig34_§6.3.5.7.2 | (deferred v1.4) |
| 28 | CONTENT_TRUNCATED | 64 | 20 | should | 220-228 | ig34_§6.3.5.4 | (deferred v1.4) |
| 29-49 | ... | ... | ... | ... | ... | ... | (deferred v1.4) |

---

## 2. Batch 分组 (v1.3 scope: 25 level1 sections)

| Batch | Ranks | Sections | Atoms (M+P) | Strategy | Status |
|:-:|---|:-:|:-:|---|---|
| **H (heavy)** | 1-10 | 10 | ~470 atoms | 单 executor 跑 1-2 节即可 ≤ context budget | Deferred to subsequent sessions |
| **M (medium)** | 11-20 | 10 | ~87 atoms | 派 background executor 单 subagent 串行跑 10 节 | **active this session** |
| **S (small)** | 21-25 | 5 | ~10 atoms | 主 session 直接做 (≤3 atoms 各, 单文件单 sentence) OR 合入 M batch | TBD this session |

**本 session 目标**: Batch M (10 节, ~87 atoms) + Batch S (5 节, ~10 atoms) = 15 节, ~97 atoms.
**v1.4+ candidate**: Batch H (10 节, ~470 atoms) + all level2 (24 节, est ~600 atoms).

---

## 3. 各 batch 的 md_target_files

需要后续从 section_coverage.jsonl 提取每节的 `md_target_files` 字段 → 写入 executor prompt. 见 `a3_batch_m_dispatch.md` (executor 完成后产生).

---

## 4. PLAN.md 对齐

- PLAN.md § 1.1 In scope: "**Tier B 高 shall/must 节修复** (56 SIBLING_DROPPED 中 shall/must 关键词出现率 ≥3 的节优先, 估 20-30 节)"
- 实际 Tier B 含 SIBLING_DROPPED (56) + CONTENT_TRUNCATED (110), 本次扩到两类
- shall/must 阈值: 由 keyword_flag=level1 (MUST/required/may not) 实现 — 比"出现率 ≥3" 更精确
- 25 节 = level1 全集合, 符合 plan target 20-30 区间

---

## 5. 下一步

A3 Batch M dispatch — main session 派 executor subagent (Rule D writer 角色, 与 main session 隔离), background 跑 ranks 11-20. 同时 foreground 启 A4 UNSOURCED_MANUAL N=40 抽样.
