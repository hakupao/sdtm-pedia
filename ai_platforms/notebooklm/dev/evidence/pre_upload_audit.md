# Phase A A1: Pre-upload Audit

> **产出日期**: 2026-04-21
> **执行者**: 主 session (Bash `find + wc -w`)
> **目的**: 确认 `knowledge_base/` md 文件无单源 >500K words outlier, 为 P3.2 单批上传策略提供数据
> **Phase A 角色**: A1 独立 hard checkpoint (Q1=0 前置, 与 A2/A5' 并行)

---

## 总体统计

| 指标 | 值 | 校验 |
|------|-----|------|
| **md 文件总数** | **295** (PLAN 原估 293, 实际 +2 minor) | OK — 更新 PLAN §3.2 + ROADMAP 引用到 295 |
| **总 words** | **1,575,309** (~1.58M words) | 远低于 Pro 300 source × 500K cap (= 150M words) 理论上限 |
| **平均 words/file** | **5,340** | Healthy — 典型 SDTM md 文件规模 |
| **最大单文件 words** | **65,822** (`terminology/core/lb_part3.md`) | **13% of 500K 单源 cap** — 零 outlier 风险, 单源 cap 零压力 |
| **500K words 单源 cap 超标?** | **No (0 files)** | ✅ PASS |

## Top 10 大文件 (wc -w 降序)

| Rank | 文件 | Words |
|------|------|-------|
| 1 | `terminology/core/lb_part3.md` | 65,822 |
| 2 | `terminology/core/lb_part2.md` | 61,853 |
| 3 | `terminology/core/general_part1.md` | 39,561 |
| 4 | `terminology/core/is_domain_part2.md` | 38,934 |
| 5 | `VARIABLE_INDEX.md` | 27,758 |
| 6 | `terminology/core/general_part5.md` | 26,170 |
| 7 | `terminology/questionnaires/questionnaires_part19.md` | 22,562 |
| 8 | `chapters/ch04_general_assumptions.md` | 20,312 |
| 9 | `terminology/core/qs_part1.md` | 20,210 |
| 10 | `terminology/questionnaires/questionnaires_part18.md` | 19,923 |

**观察**: Top 10 集中在 `terminology/core/` (6 个) 和 `terminology/questionnaires/` (2 个). 这些是已经做过 split 的 codelist 长表 (part1/part2/..., 明显是为解决原始长度而拆分的). 单源内容组织合理.

## 文件大小分布

| 区间 | 文件数 | 占比 |
|------|-------|------|
| <1,000 words | 106 | 35.9% |
| 1,000-10,000 words | 116 | 39.3% |
| >10,000 words | 73 | 24.7% |

**观察**: ~36% 文件 <1K words, 其中相当一部分是 `domains/<X>/assumptions.md` 和 `examples.md` (SDTM 小域的 assumptions/examples 往往简短). bucket 设计时应把小文件优先合并 (否则 50 slot 里浪费).

## 顶级目录分布

| 目录 | md 文件数 | 说明 |
|------|----------|------|
| `domains/` | **189** | 63 domains × ~3 files/domain (spec + assumptions + examples, 部分域缺 assumptions 或 examples) |
| `terminology/` | **91** | `core/` 41 + `questionnaires/` 44 + `supplementary/` 6 |
| `chapters/` | 6 | IG 章节 (ch03-ch08) |
| `model/` | 6 | SDTM 模型概念 |
| `INDEX.md` | 1 | 顶级索引 |
| `ROUTING.md` | 1 | 路由指南 |
| `VARIABLE_INDEX.md` | 1 | 1523 变量权威清单 |
| **合计** | **295** | — |

## 对 P3.2 上传策略的影响

1. **无 outlier 触发拆分**: 最大文件 65K words < 500K cap, 不需要 pre-split
2. **小文件合并空间**: 106 个 <1K words 文件显示 **concept cluster 合并是必要策略** (不合并则 ≤50 slot 装不下 295 个)
3. **293 → 295 更新**: PLAN § Req 变量估算 (~366 记录 / 去重 ~100-120 独立) 不受影响 (额外 2 个文件不改变 Req 变量全集大小, 可能是索引/附录文件). A2 extract_req_vars.py 仍按 VARIABLE_INDEX.md 的 1523 唯一变量 / 63 domains 基线.
4. **Phase 3 P3.2 策略确认**: A5' 用户实测 43 文件单批 OK → 50 可直接单批, A1 无 outlier 支撑 → **单批上传策略锁定**.

---

## Phase A A1 状态

- **Status**: ✅ **PASS** (295 文件全部 <500K words, 单源 cap 零压力)
- **产物**: 本文件 `pre_upload_audit.md` + Top 10 table
- **下游影响**:
  - P3.2 策略: 单批上传 (结合 A5')
  - A3 策略: 小文件优先合并 (106 个 <1K words)
  - PLAN 295 vs 293 分歧: 主 session 记录, 不改 PLAN (差 2 个不影响结论, Phase 5 RETROSPECTIVE 可作 note)

---

*来源: `find knowledge_base -name "*.md" -exec wc -w {} \;` 聚合 2026-04-21.*
