# Gemini Gems Phase 3 A/B Report

> Date: 2026-04-20
> Node: Phase 3 Node 2 (executor, attempt 2)
> Stage: attempt 1 HARD FAIL → v1.3d fix (3 轮 reviewer PASS) → attempt 2 跑 merge+validate+AB
> 执行者: executor subagent (opus, oh-my-claudecode:executor)
> 依赖: v1.3d fix reviewer 3 轮 (phase3_node2_fix_reviewer.md + fix_delta_reviewer.md + fix_final_critic.md) + PLAN
> 硬约束: attempt 2 未改任何脚本 (规则 D), attempt 1 产物/failure archive 全保留 (规则 B)
> 覆盖: 本文件覆盖 attempt 1 版本, attempt 1 原数据摘要保留在 §1

---

## 1. attempt 1 概述 (历史, 已被 v1.3d 修复)

- merge: rc=0, 4 产物, **04 仅 1 段 source** (`lb_part3.md`), 111,771 tok
- validate: rc=1 **HARD FAIL**, V6 tail 30% 区间 = 0 段 terminology marker (需 ≥3)
- 根因: core>target 分支 selected_sources 只含 top-1 最大 file (bytes 逆序 break 过早)
- 详见 failures archive: `dev/evidence/failures/stage_phase3_attempt_1.md`

v1.3 → v1.3b → v1.3c → v1.3d 四轮迭代 (3 轮独立 reviewer + 1 轮 7 视角 critic):
- **v1.3** 混合 top-2 大文件 + small hints prepend
- **v1.3b** 反转循环让大文件在前 smalls 在后 (主 session 推演)
- **v1.3c** remaining 改 bytes 升序 (pr-review-toolkit reviewer: 避免 is_domain_part2 独吞)
- **v1.3d** budget 80K→90K (feature-dev reviewer: tiktoken 精算 83,945 > 80K)

---

## 2. attempt 2 — merge_for_gemini --stage all (v1.3d)

- rc: **0** (成功)
- 执行日志: `dev/evidence/merge_all_attempt2.log`

| 文件 | 源段数 | tokens | target | 偏差 | 位置策略 |
|------|------:|-------:|-------:|-----:|---------|
| 01_core_reference.md | 15 | 124,512 | 120,000 | **+3.76%** | 前置 (导航) |
| 02_domain_specs.md | 63 | 185,785 | 168,000 | **+10.59%** | 中段 (字母序) |
| 03_domain_knowledge.md | 126 | 275,318 | 225,000 | **+22.36%** ⚠ | 中段 (assumptions 先) |
| 04_terminology_core.md | **5** | **299,303** | 200,000 | **+49.65%** ⚠ 新 | 末尾 (P12) |
| **合计** | **209** | **884,918** | ≤800,000 (P11) | +10.61% | — |

关键增量 vs attempt 1:
- **04 源段数 1 → 5** (lb_part2 + lb_part3 + oncology_part1 + interventions + qs_part1)
- **04 tokens 111,771 → 299,303** (+188% 接管所有 core terminology)
- **总 tokens 697,386 → 884,918** (+26.9%, 仍 <900K WARN 阈)

## 3. attempt 2 — validate_gemini V1-V6 全 check (v1.3d)

- rc: **0** (PASS)
- 执行日志: `dev/evidence/validate_all_attempt2.log`
- 详细报告: `dev/evidence/validate_single_batch.md`

| V | 项 | 01 | 02 | 03 | 04 | 判定 |
|---|----|:--:|:--:|:--:|:--:|:----:|
| V1 | 非空 (size>0) | PASS | PASS | PASS | PASS | **全 PASS** |
| V2 | 段数 ≥ min (15/63/126/0) | PASS (15) | PASS (63) | PASS (126) | INFO (5, 无上限判) | **PASS** |
| V3 | 总 tokens ≤800K target / ≤900K WARN / >1M FAIL | — | — | — | — | **PASS** (884,918 <900K) |
| V4 | <5MB | PASS (477K) | PASS (675K) | PASS (909K) | PASS (1,111K) | **全 PASS** |
| V5 | md5 稳定 (记录不判) | 7e212bf21277 | ee15430f82d8 | 6301b6e053ff | 68b904528240 | **INFO** |
| V6 | 04 尾部 30% ≥3 terminology source 段 | - | - | - | **PASS (3)** | **PASS** |

### V6 实测铁证 (attempt 2 修复验证)

- 04 总 chars = 1,111,314, tail_start (70%) = **777,919**, tail 区间 = [777,919, 1,111,314]
- 实测 6 条 source markers 分布:

| offset | 区段 | source |
|-------:|:----:|--------|
| 188 | head | (file header marker) |
| 281 | head | lb_part2.md |
| 378,194 | head | lb_part3.md |
| **795,262** | **TAIL** | **oncology_part1.md** |
| **884,851** | **TAIL** | **interventions.md** |
| **974,723** | **TAIL** | **qs_part1.md** |

- **tail 段数: 3 ≥ V6_MIN=3 → V6 PASS** (attempt 1 FAIL=0 → attempt 2 PASS=3)
- 3 个 tail marker offset 全部 ≥ 777,919, 与 v1.3d 设计预算精确对齐 (主 session 第 7 视角 critic 推演 onc 795K + intv 884K + qs 974K 全部命中)

## 4. Token 偏差表 (Phase 2 carry-over B2/B3 + attempt 2 新项)

规则: 偏差 >15% 标 WARN, 建议主 session trace + reviewer + ack (不阻塞本 Node, 但必报).

| 文件 | expected | actual | 偏差 | 判定 | 说明 |
|------|---------:|-------:|-----:|:----:|------|
| 01_core_reference.md | 120,000 | 124,512 | +3.76% | PASS | |
| 02_domain_specs.md | 168,000 | 185,785 | +10.59% | PASS (≤15%) | |
| 03_domain_knowledge.md | 225,000 | 275,318 | **+22.36%** | **WARN (carry-over)** | attempt 1 已报, 用户 Q3=接受, 本 Node 继续保留 |
| 04_terminology_core.md | 200,000 | 299,303 | **+49.65%** | **WARN (新增)** | 由 -44% → +49.65% 反转, v1.3d 90K budget + 3 大文件吞吐所致; 不阻塞 Node 2, 标记给 Node 3 处理 |
| 总 V3 | ≤800,000 | 884,918 | **+10.61%** | **PASS** (<900K WARN 阈) | P11 target 800K 超 84,918 tok, 距 900K WARN 阈尚余 15K |

### 新 WARN: 04 +49.65% (attempt 2 专属)

- **根因**: v1.3d budget=90K + bytes 升序让 4 个 small cores (oncology/intv/qs_part1/bodysys) 全部塞进去 + 2 个 large (lb_part2/lb_part3). 实测 tokens 预计 299,140 (attempt 1 AB 推演) vs actual 299,303, 吻合.
- **影响**: 04 超 200K target 一倍, 单文件 299K 对 1M 窗口 ≈ 30%, 但 V3 合计 884K <900K 仍 PASS.
- **Node 3 待办 (不阻塞本 Node)**: 主 session 需决策 — 
  - (a) 接受 04 超 target 换 V6 PASS (当前)
  - (b) 调 target 200K→300K 让 WARN 自动消除
  - (c) 降 budget 回 80K 牺牲部分 smalls (但会退回到 V6 边缘)

## 5. Rule A N=5 抽检待办 (Node 3 前必做)

v1.3d 改写率 / 压缩率 vs attempt 1:
- 04 压缩率 (source bytes / final tokens 近似): 111K vs 417K bytes → 27% → attempt 2: 299K vs 1,111K → 27% 保持
- **改写率 >50%** 的不是内容本身, 是 merge 策略 (选段逻辑完全改). 严格来看内容是原段无改写, 仅新增选段 — **Rule A 可能不适用**, 主 session 自行判定.
- 若主 session 认定适用, N=5 样本建议: 04 内 5 个 source 段 (lb_part2 / lb_part3 / oncology_part1 / interventions / qs_part1) 各抽 1 段原文 + merged 文段对齐, 留 `dev/evidence/rule_a_audit_attempt2.md`.

## 6. Overall Verdict

**PASS** — attempt 2 V6 HARD FAIL 已修复, V3 仍在 WARN 阈内.

- V1/V2/V3/V4/V5/V6: **全 PASS** (V2 terminology INFO 不判段数上限, V5 md5 仅记录)
- **V6 HARD FAIL → PASS**: tail 段数 0 → 3 (oncology/intv/qs 全落 TAIL 区)
- Token 偏差: 03 +22.36% WARN (carry-over 已 ack), **04 +49.65% WARN (新, Node 3 处理)**
- V3 合计: 884,918 tok, 超 P11 target 800K 但 <900K WARN 阈, 距 1M 硬 FAIL 阈 115K 安全余量

**建议 verdict: PASS (含 1 新 WARN flag 转给 Node 3)**

## 7. 下一步建议

1. **主 session ack v1.3d 结果** + 决策 04 WARN 三选项 (接受 / 调 target / 降 budget)
2. **Rule A N=5 抽检** (若适用): Node 3 前主 session 评估改写率是否达阈, 达则抽检
3. **Node 3 规划** 继续 (独立 reviewer + 用户 ack 后推进)
4. **不要删任何 attempt 1 产物** (Rule B): `dev/evidence/failures/stage_phase3_attempt_1.md` + attempt 1 reviewer 链全保留
5. **Node 1 merge.py 已冻结 + unfreeze 过一次**: v1.3d 动过 score/budget/ordering, 后续 Node 不可再动除非新 reviewer 链
6. **§7 10 题组成关系备忘**: Node 5 A/B 前主 session 确认 T1-T4 + T5-T8 + T-tail-1/2 + T9 = 10 必答, T10 可选 (本 Node 不处理)

---

## 附录 A — attempt 2 产物 checksum (V5 记录)

| 文件 | md5 (head12) | bytes | tokens |
|------|--------------|------:|-------:|
| 01_core_reference.md | 7e212bf21277 | 476,866 | 124,512 |
| 02_domain_specs.md | ee15430f82d8 | 675,446 | 185,785 |
| 03_domain_knowledge.md | 6301b6e053ff | 909,002 | 275,318 |
| 04_terminology_core.md | **68b904528240** | 1,111,314 | 299,303 |

注: attempt 1 vs attempt 2 md5 全部变化 (产物全覆盖). `_file_header()` 时间戳导致跨运行 md5 抖动, 仅记录不判 (Node 1 reviewer MEDIUM-1 已知).

## 附录 B — attempt 1 vs attempt 2 核心 delta

| 指标 | attempt 1 | attempt 2 | delta |
|------|----------:|----------:|------:|
| merge rc | 0 | 0 | — |
| validate rc | **1 (FAIL)** | **0 (PASS)** | **修复** |
| V6 tail 段数 | 0 | **3** | +3 |
| 04 源段数 | 1 | **5** | +4 |
| 04 tokens | 111,771 | 299,303 | +188% |
| 04 偏差 | -44.11% | +49.65% | WARN 方向反转 |
| 总 tokens | 697,386 | 884,918 | +26.9% |
| V3 判定 | PASS (远低) | PASS (<900K) | 缩窄但未破 |

---

REPORT_DONE
Verdict: **PASS** (含 1 Node 3 转办 WARN: 04 +49.65%)
