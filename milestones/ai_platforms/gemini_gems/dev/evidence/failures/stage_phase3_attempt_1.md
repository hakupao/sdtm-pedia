# Gemini Gems Phase 3 — Attempt 1 Failure Archive

> Rule B 归档 (失败不删).
> Date: 2026-04-20
> Node: Phase 3 Node 2 (executor)
> Scope: merge_for_gemini.py + validate_gemini.py 首次跑通, V6 HARD FAIL.
> 不修脚本, 不尝试 fix, escalate 主 session 决策 HIGH-1 三选项.

---

## 1. 输入 (跑的是什么)

- Stage 脚本 (Node 1 已冻, 本 Node 未改任何一行):
  - `ai_platforms/gemini_gems/dev/scripts/merge_for_gemini.py`
  - `ai_platforms/gemini_gems/dev/scripts/validate_gemini.py`
- 命令序列:
  1. `python3 merge_for_gemini.py --stage all` (rc=0, 产出 4 合并文件)
  2. `python3 validate_gemini.py` (rc=1 HARD FAIL)
- 源数据 (只读 P5):
  - `knowledge_base/terminology/core/` 42 文件, 累计 ~3.4MB
  - `TERMINOLOGY_TARGET_TOKENS = 200_000`

## 2. 产物 (实测数据, 非估算)

| 文件 | bytes | tokens | target | segments | V1 | V2 | V4 | V6 |
|------|------:|-------:|-------:|---------:|:--:|:--:|:--:|:--:|
| 01_core_reference.md | 476,866 | 124,512 | ≤120,000 | 15 | PASS | PASS | PASS | - |
| 02_domain_specs.md | 675,446 | 185,785 | ≤168,000 | 63 | PASS | PASS | PASS | - |
| 03_domain_knowledge.md | 909,002 | 275,318 | ≤225,000 | 126 | PASS | PASS | PASS | - |
| 04_terminology_core.md | 417,349 | **111,771** | ≤200,000 | **1** | PASS | PASS | PASS | **FAIL** |
| **合计** | 2,478,663 | **697,386** | ≤800,000 (P11) | — | — | — | — | — |

`04_terminology_core.md` 详细:
- 总字符数: 417,349
- tail_start (30%): 292,144
- terminology source 段数 total: **1** (只有 `lb_part3.md`)
- tail 30% 区间内 terminology source 段数: **0**
- V6 要求: ≥3 ⇒ **FAIL**

## 3. 技术判定

`_collect_terminology_sources` 执行路径 (基于实测):

```
core_total_tokens = 850K+ > 200K target
  → 进 else 分支 (核心超 target)
  → core_by_size 按 bytes 降序: [lb_part3 (111672 tok), lb_part2 (103523 tok), is_domain_part2 (69376), ...]
  → 循环:
      iter 1: lb_part3, cum=0, 0+111672 <= 200K  → 加入 (cum=111672, selected=[lb_part3])
      iter 2: lb_part2, cum=111672, 111672+103523=215195 > 200K
             AND len(selected)=1 >= 1
             → break
  → selected.reverse() = [lb_part3]
```

**结果: selected 只含 `lb_part3.md` 1 个 source**, 比 Node 1 reviewer 推演的 2 个 (lb_part3 + lb_part2) 还少. 核心原因是 break 条件判定前已经 **不允许超 200K** (`cum + t > TERMINOLOGY_TARGET_TOKENS`), 而 `len(selected) >= 1` 在选了第一个文件后就满足, 所以第二个大文件一超就退出, 整个 04 只剩 1 段.

然后 source 段数 = 1, 必在文件头 (offset=281), tail 30% 区间 (>=292144) 内 0 段 ⇒ V6 `>=3` 必 FAIL.

## 4. 业务判定

- V6 FAIL 的业务含义: P12 末尾召回硬 checkpoint 准备破产 — 04 产物没有多段 codelist marker 落在尾部 recency 区, Gemini 回答 codelist 类问题时无法利用 recency bias 检索到多类代码本.
- 当前 04 只塞了 111K tok (单一 lb codelist), 实际 budget 有 ~88K tok 剩余 (到 200K 上限), 而 total 仍 697K 远低于 800K 预算 — **容量够, 但脚本策略选少了**.

## 5. 当前 reverse size-proxy selection 明细

selected (最终写入顺序, selected.reverse() 之后):
- [1] `knowledge_base/terminology/core/lb_part3.md` (417,006 bytes / 111,672 tok)

dropped (42 core + 43 quest + 6 supp = 91 个):
- core top-10 dropped (by size): lb_part2 (103K tok), is_domain_part2 (69K), general_part1 (62K), general_part5 (38K), qs_part1 (36K), general_part3 (25K), other_part3 (28K), microbiology_part3 (26K), other_part4 (21K), interventions (N/A)
- questionnaires: 43 文件全未选 (core>target 分支忽略 quest/supp)
- supplementary: 6 文件全未选 (同上)

## 6. 下一 Attempt 输入 (给主 session 的决策材料)

HIGH-1 三选项 (必须主 session ack 后才能改脚本重跑):

### 选项 A: 降 V6 `V6_TAIL_MIN_TERM_SEGMENTS` 由 3 到 1
- 修改: `validate_gemini.py` 行 90 `V6_TAIL_MIN_TERM_SEGMENTS = 3` → `= 1`
- 优点: 1 行 diff, 不动 merge 逻辑, 当前产物直接 PASS
- 缺点: P12 hard checkpoint 完全弱化, 末尾 recency 仅验证"有 1 段 terminology", 丧失"多类 codelist 并存"的语义保证
- 风险: 规则 A/D 可能质疑"门槛降低掩盖问题"
- 评分: ⬜ 不推荐作为首选 (业务弱化明显)

### 选项 B: 允许 04 轻微超 target (≤220K)
- 修改: `merge_for_gemini.py` 行 272 的 break 条件
  - 从: `if cum + t > TERMINOLOGY_TARGET_TOKENS and len(selected) >= 1: break`
  - 到: `if cum + t > int(TERMINOLOGY_TARGET_TOKENS * 1.1) and len(selected) >= 2: break`
  (或更激进到 1.2x + >=5)
- 预期 selected: lb_part3 + lb_part2 + is_domain_part2 + general_part1 + general_part5 ≈ 215K-245K tok (2-5 段)
- 优点: V6 有望满足 (5 段里至少 1-2 段落在 tail 30%), 总 tokens 仍 ~800K 左右无超 1M 风险
- 缺点: 轻微违 PLAN §2.1 "04 target ~200K"; 具体阈值需试跑
- 风险: V2 WARN 已允许 (validate.py 行 216 `result.warn = True` 不 hard_fail), 超 10% 算合 Phase 2 口头澄清 "±15% WARN"
- 评分: ⬜ 可接受 (轻度妥协, 但保 P12 精神)

### 选项 C (推荐): 混合策略 — 大文件保尾 + 小高频补段数
- 修改: 重构 `_collect_terminology_sources` core>target 分支:
  1. 先留 top-2 大文件 (lb_part3 + lb_part2, 共 215K tok) — 保 "lb 高频 LB codelist" 落尾 recency
  2. 然后 selected.reverse(), 但 reverse 前先 **前插** 若干高频小文件 (如 interventions / oncology_part1 / qs_part1 共 ~87K tok) 到数组开头
  3. 最终 doc 顺序: [小高频文件 1..N] → lb_part2 → lb_part3 (尾部)
- 预期 selected: 5-8 个 source, 总 ~200-260K tok
- 优点: V6 最稳 (5+ 段分布), 保 recency 语义 (lb 最末), 还能覆盖更多 codelist 类型
- 缺点: 修改面 ~20 行 merge 代码, Node 1 reviewer HIGH-1 明示推荐此选项
- 风险: Rule D 独立复核需重走 (改动 Node 1 冻结的 merge 代码)
- 评分: ⬛ 推荐 (reviewer 同口径, 业务最稳)

## 7. 建议

主 session 建议采纳 **选项 C**. 理由:
1. Node 1 reviewer HIGH-1 明文推荐 (phase3_node1_reviewer.md Carry-over §HIGH-1)
2. 不降校验门槛 (选项 A 弱化 P12)
3. token 预算充裕 (697K 总, 04 上限 200K 未触), 容量问题不是约束
4. 单一 `_collect_terminology_sources` 内修改, 影响面可控

若主 session 选 **选项 B**, 建议阈值: `1.1x + len(selected)>=2`, attempt_2 先跑一次看 selected size.
若选 **选项 A**, 仅改 validate.py 1 行, 但需在 RETROSPECTIVE 里记录门槛降级原因.

---

## 状态

- attempt_1 状态: FAIL_WAITING_MAIN_SESSION_ACK
- 需主 session 决策 A/B/C 后 → attempt_2 (下一次 merge + validate)
- 产物未删 (Rule B "失败归档不删"), 04_terminology_core.md 保留现场供 attempt_2 对比
