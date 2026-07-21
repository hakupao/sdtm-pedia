<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → ../_progress.json                     (phases.P3 字段)
  → ../evidence/checkpoints/              (P3 产物快照)
  → ../PLAN.md §5                         (phase 状态更新)
-->

# P3 — 候选索引构建 Sub-Plan

> Version: **v1.0 (2026-05-11, post P2 B-03c 収官)**
> 父 PLAN: `branches/06_deep_verification/PLAN.md` v0.6
> 前置: P1 ✅ (12,487 pdf_atoms) + P2 ✅ (10,435 md_atoms)
> 目标: 纯 Python 脚本, 为每个 pdf_atom 计算 top-5 md_atom 候选, 产 `p3_candidates.jsonl`
> Tier 3 / Phase 纯脚本 — 预估 **0.5 session**

---

## 0. 输入 / 输出契约

| 项 | 值 |
|---|---|
| 输入 1 | `branches/06_deep_verification/pdf_atoms.jsonl` (12,487 atoms) |
| 输入 2 | `branches/06_deep_verification/md_atoms.jsonl` (10,435 atoms) |
| 主输出 | `branches/06_deep_verification/p3_candidates.jsonl` (12,487 行) |
| 辅助输出 | `evidence/checkpoints/p3_report.md` (统计 + gate 验证) |
| P4a 消费格式 | 每行 1 个 pdf_atom_id + ≤5 md 候选 (含分数 + 依据) |

### p3_candidates.jsonl 行结构

```jsonc
{
  "pdf_atom_id": "ig34_p0425_a012",
  "pdf_atom_type": "SENTENCE",
  "pdf_source": "SDTMIG_v3.4",
  "pdf_parent_section": "§8.2.1 RELREC",
  "candidates": [
    {
      "md_atom_id": "md_relrec_ass_a003",
      "md_file": "knowledge_base/domains/RELREC/assumptions.md",
      "md_atom_type": "SENTENCE",
      "score": 0.82,
      "match_basis": "verbatim_token+section_domain"
    }
  ],
  "candidate_count": 3,
  "zero_candidate": false
}
```

**`candidate_count` 可为 0**（无候选）— P4a 直接给 `MISSING` verdict，无需 agent 比对。

---

## 1. 匹配算法设计 (纯 Python, 无 ML)

### Step 1 — Domain 路由（降维核心）

pdf `parent_section` 中抽取 domain 代码 → 对应 md `file` 路径前缀。

| pdf parent_section 模式 | 提取规则 | md 文件前缀 |
|---|---|---|
| `§X.Y DM ...` 或 `§DM.N ...` | 取大写2-4字母 domain code | `knowledge_base/domains/DM/` |
| `§4.x.y` 无 domain code | section 号映射到 chapters/ | `knowledge_base/chapters/` |
| `§1 / §2 / §3` 模型章节 | 映射到 model/ | `knowledge_base/model/` |

**域路由命中 → 候选池从 10,435 缩到 ~100-300**（同域文件原子），大幅提升精度和速度。

### Step 2 — Atom Type 过滤

同 atom_type 候选优先（权重 +0.3）。跨 type 降权但不排除（TABLE_ROW ↔ SENTENCE 允许，HEADING ↔ TABLE_ROW 降权）。

### Step 3 — Verbatim Token 相似度

```
score = jaccard(tokens(pdf.verbatim), tokens(md.verbatim))
tokens = 小写 + 去标点 + 3-gram 字符串集合
```

标准库实现，无依赖。Jaccard ∈ [0,1]。

### Step 4 — 综合分排序

```
final_score = score_verbatim * 0.6
            + score_atom_type_match * 0.3
            + score_domain_match * 0.1
```

取 top-5，score < 0.05 的候选截止（避免噪声）。

### Step 5 — 零候选标记

`candidates = []`, `zero_candidate = true` → P4a 不派 agent，直接登记 `MISSING`。

---

## 2. 脚本文件

| 文件 | 位置 | 用途 |
|---|---|---|
| `p3_build_index.py` | `branches/06_deep_verification/` | 主脚本，读两个 jsonl → 输出 p3_candidates.jsonl |
| `p3_report.py` | 同上 | 统计脚本，读 p3_candidates.jsonl → 输出 p3_report.md |

脚本运行命令（新 session 执行）：
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
python3 branches/06_deep_verification/p3_build_index.py
python3 branches/06_deep_verification/p3_report.py
```

运行时间预估：~30 秒（10k × 10k 暴力搜太慢；域路由后 10k × ~200 = 200万次比对，可接受）。

---

## 3. Domain 路由映射表（脚本内嵌）

pdf `parent_section` 前缀 → md 文件路径前缀对照：

```python
DOMAIN_ROUTE = {
    # 63 domains — 按 parent_section 中 domain code 匹配
    # 示例: "AE" → "knowledge_base/domains/AE/"
    # 脚本动态从 md_atoms.jsonl file 字段提取所有 domain 代码自动构建
}
CHAPTER_ROUTE = {
    "§1": "knowledge_base/chapters/ch01",
    "§2": "knowledge_base/chapters/ch02",
    "§3": "knowledge_base/chapters/ch03",
    "§4": "knowledge_base/chapters/ch04",
    "§5": "knowledge_base/chapters/ch05",
    "§6": "knowledge_base/chapters/ch06",
}
MODEL_ROUTE = {
    "§1 [Intro": "knowledge_base/model/01",
    "§2 [SDTM": "knowledge_base/model/",
}
```

脚本自动从 md_atoms 的 `file` 字段提取 domain 列表，无需手写 63 个条目。

---

## 4. Edge Cases

| 情况 | 处理 |
|---|---|
| pdf `parent_section` 无法路由到任何 md 前缀 | 全库搜索（降速，记录 `match_basis: "global_search"`） |
| pdf `atom_type = FIGURE` | 候选仅限 md `atom_type = FIGURE`；无 FIGURE 候选则 `zero_candidate = true` |
| pdf `atom_type = HEADING` | 候选仅限 md HEADING；用于结构校验 |
| pdf verbatim 极短（≤ 5 tokens） | score 阈值降至 0.02，候选上限 10 |
| pdf source 含 `None` 或 `SDTM_v3.4`（139+1 条） | 仍正常处理，记录 `pdf_source` 字段 |

---

## 5. P3 Exit Gate

| 条件 | 门槛 |
|---|---|
| p3_candidates.jsonl 行数 | = 12,487（每个 pdf_atom 必有一行） |
| zero_candidate 率 | 记录但不 block；预期 < 20%（HEADING 类多） |
| 平均候选数（非零行） | ≥ 2.0（太低说明路由失败） |
| top-1 score 均值 | ≥ 0.20（太低说明匹配质量差） |
| 脚本运行无异常 | 0 exception / 0 JSON 解析错 |
| p3_report.md 产出 | 含按 atom_type 分层统计 + zero_candidate 分布 + score 分位数 |

Gate PASS → 写 `trace.jsonl` 1 条 `phase_report` 事件 + 更新 `_progress.json` `phases.P3`。

---

## 6. 新 session 启动 checklist

1. 读 `branches/06_deep_verification/PLAN.md` §5 + 本文件
2. 确认 `pdf_atoms.jsonl`（12,487）+ `md_atoms.jsonl`（10,435）均存在
3. 写 `p3_build_index.py`（见 §1-4 设计）
4. 写 `p3_report.py`（见 §5 gate 统计）
5. 运行脚本，产 `p3_candidates.jsonl` + `evidence/checkpoints/p3_report.md`
6. 对照 §5 gate 逐条核验
7. 更新 `_progress.json` phases.P3 + trace.jsonl
8. 若 gate PASS → 进 **P4a** (`plans/P4a_forward_matching.md`，见下一步)

---

## 7. P4a 输入契约（P3→P4a 接口定义）

P4a 每个 agent 调用的输入为：

```jsonc
{
  "pdf_atom": {
    "atom_id": "ig34_p0425_a012",
    "source": "SDTMIG_v3.4",
    "page": 425,
    "parent_section": "§8.2.1 RELREC",
    "atom_type": "SENTENCE",
    "verbatim": "RELREC is used to represent ..."
  },
  "candidates": [
    {
      "md_atom_id": "md_relrec_ass_a003",
      "md_file": "knowledge_base/domains/RELREC/assumptions.md",
      "md_atom_type": "SENTENCE",
      "verbatim": "RELREC represents relationships ...",
      "score": 0.82
    }
    // ... up to 5
  ]
}
```

`zero_candidate = true` 的 pdf_atom → P4a 脚本直接写 `verdict: "MISSING"` 到 `coverage_ledger.jsonl`，不派 agent。

---

*Next: `plans/P4a_forward_matching.md` (P3 gate PASS 后再写)*
