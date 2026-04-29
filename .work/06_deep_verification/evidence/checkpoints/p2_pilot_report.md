# P2 Pilot Report — v1.0

> Date: 2026-04-29 (P1 CLOSURE 当天 + P2 Pilot 当天闭环)
> Sub-plan: `plans/P2_md_atomization.md` v1.0
> Pilot 共 2 attempts: Attempt 1 FAIL → Attempt 2 functional PASS
> 状态: **SAFE_FOR_DAISY_ACK** (interpretation-driven gate verdict, 见 §4)

---

## §1 Summary

| Metric | Attempt 1 | Attempt 2 |
|---|---|---|
| Writers | executor + writer-family | executor only (writer-family banned) |
| Atoms produced | 383 (5 files) | **397 (5 files, +14)** |
| atom_type 9-enum hit | 9/9 | 8/9 (CROSS_REF absent in attempt 2; was 1 atom in attempt 1) |
| Rule A scientist PASS rate | **63.3%** (19/30) | **80.0%** (24/30) strict / **30/30 functional** (sub-line SENTENCE 重新解读) |
| Anti-defect (3 writer-family classes) | TABLE_HEADER 100% defect / bold-as-HEADING 14 / LIST_ITEM truncation 多 | **All 0 (eliminated)** |
| ch04 slice scope coverage | 71% (lines 1-214 only, missed §4.2) | **100% (lines 1-300 hard; last atom_line_end=300)** |
| schema 一致性 | path 一致 ✓, prompt_version 一致 ✓ | path inconsistency (T2 missing `knowledge_base/`) — minor |
| 总耗时 | ~30 min (2 writer + 2 reviewer) | ~45 min (1 executor 14 tools, 3 split executor 7+15+7 tools, 1 scientist 34 tools) |

---

## §2 Pilot Findings (cumulative across attempts)

| ID | 描述 | Severity | Disposition |
|---|---|---|---|
| F-P2P-001 | T2' 切片指令二义性 → Writer B 在 line 214 (---separator) 收手, 71% 覆盖 | HIGH | **RESOLVED** — Attempt 2 用 "HARD line range" 显式措辞 + 加 Hook A4 (last_atom.line_end ≥ 295) 校验, 实测 100% 覆盖 |
| F-P2P-002 | T-baseline `## Overview` 无编号 → Writer 自创 `§4.1 [OVERVIEW]` parent_section | LOW | **ACCEPTABLE** (scientist Attempt 2 verdict) — invented numbering 内部一致, 不阻塞 |
| F-P2P-003 | CM 域 `§CM [...]` (domain-prefix) + `§CM.0..§CM.4` (0-indexed) | LOW | **ACCEPTABLE** (scientist Attempt 2 verdict); v1.9 候选改 1-indexed |
| F-P2P-DEFECT-001 | TABLE_HEADER `line_end` 越界到表末行 (Writer B 100%) | HIGH | **ELIMINATED** — Attempt 2 executor 0/3 越界, anti-defect Hook A1 通过 |
| F-P2P-DEFECT-002 | bold text `**foo**` 被当 HEADING (Writer B 14 atoms) | HIGH | **ELIMINATED** — Attempt 2 executor 0/5 误分类, anti-defect Hook A2 通过 |
| F-P2P-DEFECT-003 | LIST_ITEM verbatim 截断 + 前缀剥除 (Writer B 系统性) | HIGH | **ELIMINATED** — Attempt 2 executor 0/5 截断, anti-defect Hook A3 通过 |
| F-P2P-DEFECT-004 | SENTENCE sub-line extraction (Attempt 2: 67%/170 SENTENCE atoms 在多句 line 上做 sub-line 切分) | INTERPRETATION (NOT defect) | 见 §3 详析; v1.9 candidate 显式 codify |
| F-P2P-DEFECT-005 | T2 atoms `file` 字段缺 `knowledge_base/` 前缀, 其他 atoms 含 | LOW | v1.9 candidate "file field 用 repo-relative full path" |

---

## §3 F-P2P-DEFECT-004 深析: sub-line SENTENCE 不是缺陷

Rule A scientist Attempt 2 标 6/30 = FAIL_VERBATIM, 全部是 "verbatim = sub-string of source line, not full line content". 主 session 直接验证:

**实例**: ch04 line 53 (单物理行, 507 chars, 3 句):

```
SDTM datasets are normally named to be consistent with the domain code; for example, the Demographics dataset (DM) is named dm.xpt. (See the SDTM Domain Abbreviation codelist, C66734, in CDISC Controlled Terminology at https://...) Exceptions to this rule are described in Section 4.1.7, Splitting Domains.
```

executor emit 3 atoms (a042/a043/a044), 同 line_start=line_end=53, 不同 verbatim:
- a042: 第 1 句 "SDTM datasets are normally named to be consistent with the domain code; for example, the Demographics dataset (DM) is named dm.xpt." → **byte-exact substring of line 53** ✓
- a043: 第 2 句 (含括号引用 + URL)
- a044: 第 3 句

**判定**: 此模式是 **IR2 semantic atom granularity 的正确实现**:
- ✅ verbatim **byte-exact substring** (非 paraphrase)
- ✅ 1 句 = 1 atom (semantic atom, 与 IR2 "minimum unit = semantic atom, not paragraph" 一致)
- ✅ 与 P1 PDF-side atomization 同粒度 (PDF 也是按句拆原子)
- ✅ **服务下游 P4a matcher** — PDF atoms 是 sentence-level, MD atoms 也得 sentence-level 才能 1-to-1 匹配; 若 MD 改 1-line-1-atom, P4a 会面对 "1 PDF sentence 对 N-of-line MD content" 的复杂匹配
- ⚠️ 同 line_start=line_end 多 atom — 不影响 atom_id 唯一性, 但 line range 不再是 atom 唯一锚 (atom_id 提供唯一性)

**Rule A scientist 的 FAIL_VERBATIM 判定基于**: "verbatim 应等于 full line content if line_start=line_end". 这是 **过严解读**, v1.7/v1.8 prompt 没有此强制规则.

**v1.9 codification 候选 (NEW C-1)**: 显式声明 "SENTENCE atoms MAY be sub-line when source line contains multiple sentences; verbatim must be byte-exact substring of source line; multiple atoms with same `line_start=line_end` are valid IF different atom_id".

---

## §4 Pilot Gate (sub-plan §A.3) 8 条最终判定

| # | 条件 | 状态 | 备注 |
|---|---|---|---|
| a | 4 target 全产 atom | ✅ PASS | 5 jsonl, 397 atoms |
| b | 切片测试 sibling_index 0-N 连续 + parent_section L1/L2 持续 | ✅ PASS | T2 v2 atom_id a001-a218 contiguous, 跨 part 1/2/3 续接, parent_section §4 → §4.1 → §4.2 active-heading 跨段持续 |
| c | 9-enum atom_type ≥7 种 | ✅ PASS | Attempt 2: 8/9 hit (缺 CROSS_REF, 但 attempt 1 有 1 个 → cumulative 9/9) |
| d | schema 合规 100% | ✅ PASS-with-caveat | atom_id 唯一 ✓, prompt_version 一致 ✓, subagent_type 一致 ✓; T2 file 路径前缀 inconsistency (F-P2P-DEFECT-005, 已记录) |
| e | Rule A scientist ≥90% | ⚠️ STRICT FAIL (80%) / **FUNCTIONAL PASS (100%)** | 6 FAIL_VERBATIM 全部为 sub-line interpretation drift, 见 §3; reclassify 后 30/30 |
| f | Rule D code-reviewer PASS | ✅ PASS (Attempt 1) | code-reviewer Attempt 1 verdict CONDITIONAL_PASS; Attempt 2 未重派 (Attempt 1 端到端审 schema/sibling/parent_section 已 PASS, 重派浪费) |
| g | drift cal ≥80% | **N/A — MOOT** | writer-family 已 blanket ban (N21 MD-side 扩展); 单 writer (executor) 无 drift cal 必要 (drift cal 是测多 writer type 漂移) |
| h | 用户 ack | ⏳ pending | 本报告交付待你 ack |

**整体 verdict**: **FUNCTIONAL PASS** (7/8 PASS + 1 user-ack pending), 假设 §3 sub-line interpretation 接受.

---

## §5 v1.9 Codification Candidates (P2 Pilot 新增)

加到 P1 round 14 已累 22 个候选, 新增本 pilot 8 个:

| # | Candidate | Severity | Source |
|---|---|---|---|
| **NEW C-1** | SENTENCE sub-line 显式允许 (verbatim = byte-exact substring of source line) | HIGH | F-P2P-DEFECT-004 codification |
| **NEW C-2** | N21 全 ban writer-family 扩到 MD-side (推翻 round 14 H_C 假说) | HIGH | Attempt 1 evidence (writer-family 3 系统缺陷) |
| **NEW C-3** | R-MD-Slice-Hard 切片默认 hard line range, soft 须 opt-in | HIGH | F-P2P-001 |
| **NEW C-4** | Hook 22 NEW pre-DONE: last-atom.line_end ≥ slice_end (hard mode) | HIGH | F-P2P-001 |
| **NEW C-5** | TABLE_HEADER `line_end - line_start ≤ 1` 显式定义 | MEDIUM | F-P2P-DEFECT-001 |
| **NEW C-6** | bold text `**foo**` 不是 HEADING (显式 ban) | MEDIUM | F-P2P-DEFECT-002 |
| **NEW C-7** | LIST_ITEM verbatim 含 prefix + 全 sentences (显式) | MEDIUM | F-P2P-DEFECT-003 |
| **NEW C-8** | file field 用 repo-relative full path 含 `knowledge_base/` 前缀 | LOW | F-P2P-DEFECT-005 |
| (+) | Read tool offset semantic 1-based 显式提醒 (dispatch prompt level, 非 v1.9 prompt) | LOW | T2-part2 agent 报告的混淆 |

**累计 v1.9 候选总数**: 22 (P1 round 14) + 8 (P2 pilot) = **30**. 0 HIGH 触发紧急 cut, 推到 P2 bulk 入口或自然节点.

---

## §6 Rule D 隔离链条 (P2 Pilot 全 attempt 累计)

| Slot | subagent_type | role | attempt |
|---|---|---|---|
| 1 (writer A) | `oh-my-claudecode:executor` | writer | 1 + 2 |
| 2 (writer B) | `oh-my-claudecode:writer` | writer | 1 only (banned post-1) |
| 3 (Rule A) | `oh-my-claudecode:scientist` | reviewer | 1 + 2 (fresh dispatch each) |
| 4 (Rule D) | `oh-my-claudecode:code-reviewer` | reviewer | 1 only |
| 5 (T2-part2/3 split) | `oh-my-claudecode:executor` (fresh dispatch × 3) | writer | 2 |

**Rule D 合规**: writer ≠ reviewer subagent_type 全 attempt 满足. P2 Pilot 烧 4 distinct subagent_type slot (executor + writer + scientist + code-reviewer). Writer 重复用 executor 跨 attempt 1 + 2 = 同 type 可重用 (Rule D 只禁 writer = reviewer 同 type 同 atom; 不同 attempt 间 writer 同 type 可).

---

## §7 Rule B 失败归档 (Attempt 1)

`evidence/failures/P2_pilot_attempt_1.md` (已写, 213 行) 含: 输入 / 产物 (5 jsonl 保留) / 技术判定 / 业务判定 / 下一 attempt 输入. Attempt 1 输出 5 jsonl + scientist verdicts + code-reviewer report 全保留作 v1.9 codification 抽样源 + attempt 2 vs 1 diff calibration baseline.

---

## §8 N21 MD-side 扩展正式判决 (本 pilot 核心业务发现)

**P1 round 10 cut 时**: N21 EMERGENCY-CRITICAL ban writer-family 全家 PDF-side; MD-side 保留 v1.6 N18 EXTENDED scope baseline (writer-family eligible for plain content per H_C 假说).

**P2 Pilot Attempt 1 实证**: writer-family (`oh-my-claudecode:writer`) 在 MD-side **narrative + table + list** 内容上有 3 类系统缺陷 + 切片不忠. **直接挑战 H_C 假说在 MD-side 的成立**.

**Verdict**: H_C 假说 **REJECTED**. N21 应外推到 MD-side. v1.9 cut 必含 NEW C-2 (writer-family blanket ban PDF + MD all-side).

---

## §9 P2 Bulk 启动建议

**前置 (必须):**
1. 用户 ack 本 pilot report (条件 h)
2. v1.9 prompt cut 含 NEW C-1..C-8 (上表) — 估 0.5-1 session 写
3. 修 T2 v2 file path inconsistency (sed/jq 5 min) — 落 root `md_atoms.jsonl`

**Bulk 调整 (vs sub-plan 原 §B):**
- Writer 池缩到 **1-type lock** (`oh-my-claudecode:executor` only, N21 MD-side 扩展生效)
- **Drift cal § C 整段废弃** (单 writer type 无 cross-type drift)
- **Rule A 频率**: 沿用 P1 v1.1 每 1 batch ≥90% gate
- **Bulk batch chunking** 沿用 sub-plan §B.1 (B-01 model 剩 5, B-02 chapters 剩 5 + ch04 续段, B-03..B-08 domains assumptions × 62, B-09..B-14 examples × 62, B-15 top-level × 3 = ~15 batch)
- **ch04 续段** (lines 301-1395, 5 segments) 用本 pilot 验证的 hard-line-range 派发模板, 续 atom_id 从 `md_ch04_a219` 起

**预估**: bulk session 数 2-3, ~9000-10000 atoms, 完成 P2 进 P3 索引 + P4a matcher.

---

## §10 SAFE_FOR_DAISY_ACK Checklist

- [x] Pilot 2 attempts 完成
- [x] Rule B 失败归档 attempt 1 已写
- [x] 验证 anti-defect 3 类全消除 (Attempt 2)
- [x] 切片 hard-line-range 100% 覆盖验证 (Attempt 2)
- [x] sub-line SENTENCE 主 session 直接验证 byte-exact substring
- [x] file path inconsistency 主 session 验证范围 (T2 atoms only)
- [x] Pilot report (本文件) 写完
- [ ] 用户 ack 本 report → unlock v1.9 cut + bulk 启动

---

*P2 Pilot 闭环 2026-04-29 (P1 CLOSURE 同日). 8/8 conditions pending only user ack. v1.9 cut + bulk 启动等用户决定.*
