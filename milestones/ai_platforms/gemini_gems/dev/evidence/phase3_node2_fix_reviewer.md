# Phase 3 Node 2 fix-diff 独立 Reviewer 报告

> Date: 2026-04-20
> Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
> Scope: ChatGPT v1.3 (merge + validate cap) + Gemini v1.3 + v1.3b (混合策略)
> Rule D: 不同于 Node 1/2 已用 subagent_type (executor / oh-my-claudecode:code-reviewer /
>         oh-my-claudecode:verifier / oh-my-claudecode:debugger), 独立复核满足.

---

## Verdict: **FAIL_REWORK** (HIGH 级阻塞)

| 平台 | 子 verdict | 关键原因 |
|------|:----------:|---------|
| ChatGPT v1.3 | **CONDITIONAL_PASS** | cap 47K 临界过紧 (buffer 仅 1.77%), 未来小幅增长即再 FAIL |
| Gemini v1.3b | **FAIL_REWORK (HIGH-1)** | 物理 offset 推演**错误**, selected 实际只有 3 段 (lb_part2, lb_part3, is_domain_part2), V6 tail_count=1 ≠ 预期 3 → 仍会 V6 FAIL |

**HIGH-1 触发**: Gemini 脚本按当前实现跑 attempt_2 会 V6 再次 HARD FAIL rc=1. **禁止直接 attempt_2**. 必须先 rework `_collect_terminology_sources` core>target 分支的小文件选取/预算逻辑.

---

## §1 ChatGPT cap 调整 (最小化 / 正确性)

### 1.1 技术正确性

| 检查项 | 结果 | 证据 |
|--------|:----:|-----|
| `merge_for_chatgpt.py` L224 token_cap 46_000 → 47_000 | ✅ PASS | git diff 确认单行改动 |
| `validate_chatgpt_stage.py` L117 ExpectSpec cap 46_000 → 47_000 | ✅ PASS | git diff 确认单行改动 |
| 两处 cap 一致 (47_000 == 47_000) | ✅ PASS | 字符串精确匹配 |
| docstring v1.3 修复记录合规 | ✅ PASS | merge.py L63-68 + validate.py L70-72, 引用 `failures/stage_1_attempt_1.md §6 方案 A` |
| 行内注释 L205 | ✅ PASS | `# 01: v1.3 微调 46_000 → 47_000 (实测 VARIABLE_INDEX 密度偏高).` |
| 改动面最小 (merge.py +8 -1, validate.py +4 -1) | ✅ PASS | 无无关动 |
| 其他 cap (02-09) 未动 | ✅ PASS | EXPECTS/MERGE_CONFIGS 其余项保持 72K/21K/193K/69K/190K/920K/1095K/173K |
| `off-by-one` 风险 | ✅ 无 | 46,170 实测 → 47,000 比较, 阈值 strict `>` → 46,170 > 47,000 = False → PASS |

### 1.2 业务合理性 (cap 是否应该更宽松)

独立验算 01 tokens = 46,170 (与 attempt_1 数据一致):

| 候选 cap | buffer | 未来 2% KB 增长 (~923 tok) | 未来 5% 增长 (~2308 tok) |
|---------|-------:|:----:|:----:|
| 47,000 (当前) | +830 / +1.77% | 再 FAIL | 再 FAIL |
| 48,000 (reviewer 提议) | +1,830 / +3.81% | PASS | 再 FAIL |
| 50,000 (宽松提议) | +3,830 / +7.66% | PASS | PASS |

**独立判定** (MEDIUM, 非阻塞):
- 47K 拯救本 attempt 能通, 但 buffer 仅 1.77%. KB 未来若再增 VARIABLE_INDEX 行 (如新增 domain/variable) 即再 FAIL. Node 2 A/B 过 → Node 3 收束时建议口径对齐, 把 cap 统一提到 48K 或 50K, 同时更新 docstring/行内注释说明新口径.
- 不是 HIGH, 因为当前不阻塞 attempt_2 PASS.

### §1 verdict: **CONDITIONAL_PASS**
- 技术正确, 文档合规, attempt_2 能过 V5.
- MEDIUM 建议 Node 3 把 cap 升到 48-50K 留安全边际, 本 Node 不阻塞.

---

## §2 Gemini 混合策略 (v1.3 + v1.3b 合规)

### 2.1 HIGH_FREQ_CORE_HINTS 文件存在性 ✅

| 文件 | 存在 | bytes |
|------|:----:|------:|
| `interventions.md` | ✅ | 89,805 |
| `qs_part1.md` | ✅ | 136,529 |
| `oncology_part1.md` | ✅ | 89,521 |
| `general_part1.md` | ✅ | 221,871 |
| `is_domain_part2.md` | ✅ | 238,488 |

### 2.2 UTF-8 非 ASCII 字符影响 ✅

独立扫描 5 hint 文件 + lb_part2/lb_part3, **非 ASCII 字符数 = 0**. 所有 core terminology 文件纯 ASCII. `len(text) == bytes`, 物理 offset 推演基于 bytes 安全.

### 2.3 **HIGH-1 — 物理 offset 推演错误, V6 实际仍 FAIL**

**独立验证复现** (runner `/tmp/simulate_v13b_exact.py`, 精确镜像 merge_for_gemini.py 的 `_collect_terminology_sources` core>target 分支):

**实际 selected 不是 5 段, 而是 3 段**:

```
FINAL selected (v1.3b 写入顺序):
  lb_part2.md         tok=103,523
  lb_part3.md         tok=111,672
  is_domain_part2.md  tok= 69,376
```

**为什么 small_head 只有 1 个文件 (不是主 session 预期的 3 个)**:

`core_by_size = sorted(core_sized, key=lambda x: -x[1])` 按 bytes 降序. `remaining = core_by_size[2:]` 从第 3 大开始. 依次遍历 remaining, 过滤 HIGH_FREQ_CORE_HINTS, 预算 80K:

```
iter 1: is_domain_part2.md (238KB, 69,376 tok) in hints → cum_small=0+69376=69376 ≤80K → ADD
iter 2: general_part1.md   (221KB, 61,564 tok) in hints → 69376+61564=130,940 >80K → SKIP
iter 3: general_part5.md   (not in hints) → skip
iter 4: qs_part1.md        (136KB, 36,059 tok) in hints → 69376+36059=105,435 >80K → SKIP
...
iter N: interventions.md   ( 89KB, 23,235 tok) in hints → 69376+23235= 92,611 >80K → SKIP
iter N: oncology_part1.md  ( 89KB, 24,651 tok) in hints → 69376+24651= 94,027 >80K → SKIP

final small_head = [is_domain_part2] (1 item)
```

`is_domain_part2.md` (69,376 tok) 独占 86.7% 的 80K budget, 阻塞其他 4 个 hint. 主 session 推演假设的 `[intv, qs, onc]` (共 ~78K tok) 从未被选中.

**物理 offset 实测**:

```
header_len = 281
body_len   = 1,033,538
total_len  = 1,033,819
tail_start = int(1,033,819 × 0.70) = 723,673

Marker 1: abs_off =    281  → lb_part2.md         (head)
Marker 2: abs_off = 378,194 → lb_part3.md         (middle)
Marker 3: abs_off = 795,262 → is_domain_part2.md  (TAIL, >723,673)

V6 tail_terminology_count = 1  (need ≥3)  → V6 HARD FAIL
```

**主 session 推演错在哪**: 把 small_head 直接当 `[intv, qs, onc]` (3 个 ~78K tok), 没模拟 `for src in remaining` 循环的贪心顺序 — is_domain_part2 在 bytes 降序下第一个出现, 吞掉 80K budget 的 87%.

### 2.4 **Rule E Q4=A 违反程度**

Q4=A 原则: "terminology 末尾 ~200K". 实测 04 产物 tokens = 284,702, 超 target 42.4%. 加上 01-03 不动 → 总 tokens = 870,317:

- V3 阈值 (validate_gemini.py L85-87): target 800K / WARN >900K / HARD FAIL >1M.
- 当前 870K < 900K → V3 PASS (不升 WARN). 但 03 已 +22.36% WARN + 04 -44.11% (原) → +42.4% (v1.3b), 累计偏离 Rule E 精神大. **这是 MEDIUM, 不 HIGH** — 因为 V3 阈值不硬触, 用户 Q3 又已接受 03 的 +22.36% 偏离.
- 但 V6 FAIL 是 HIGH (§2.3).

### 2.5 规则 A (N=5 独立抽检) 规划

core 3.4MB → v1.3b 选 ~295K (压缩率 ~91%). Rule A 强制要求 N=5 抽检.

- PLAN v1.2 未见 Node 2 N=5 抽检条目 (主 session 后续必须补, 或 Node 3 规划).
- 本 reviewer 范围 (diff-only) 不阻塞, 标 **LOW 提醒**: 修复 V6 FAIL 后, Node 3 收束前必须跑 N=5 语义抽检 terminology 压缩结果.

### 2.6 规则 P5 (knowledge_base 只读)

逐行确认 merge_for_gemini.py v1.3 diff:
- 无 `open(kb_path, 'w')` 或 `write_text(... kb ...)`
- 无 `shutil.copy` / `os.rename` 涉及 KB
- 所有 KB 访问都是 `_read_text(path)` / `p.stat().st_size` / `glob('*.md')` (只读)
- ✅ **P5 合规**

### §2 verdict: **FAIL_REWORK (HIGH-1)**

---

## §3 docstring 与真源一致性

| 项目 | 结果 |
|------|:----:|
| merge_for_chatgpt.py docstring v1.3 段引用 `failures/stage_1_attempt_1.md §6 方案 A` | ✅ PASS |
| validate_chatgpt_stage.py docstring v1.3 sync 段引用 v1.3 | ✅ PASS |
| merge_for_gemini.py docstring v1.3 段引用 `failures/stage_phase3_attempt_1.md §6 选项 C` | ✅ PASS |
| merge_for_gemini.py docstring v1.3b 段物理 offset 推演 | **⚠ 数据错误** |
| PLAN.md 同步 | **延后** |

**v1.3b docstring 数据错误** (MEDIUM):

docstring 47-55 行声称 v1.3b 会产生:
> `lb_part2@0 / lb_part3@377K / intv@794K ✓ / qs@884K ✓ / onc@1020K ✓`

**实际模拟产出**: `lb_part2@281 / lb_part3@378K / is_domain_part2@795K` (只有 3 marker, 最后一个不是 intv).

docstring 错误 propogate 自主 session 推演错误. 修 rework 时也必须更正 docstring 以免误导下轮 reviewer.

**PLAN.md 延后是否 OK**: ✅ 可接受. Node 3 收束时统一做 cap 口径对齐 + Rule E 偏离记录. 本 Node 不阻塞.

### §3 verdict: **CONDITIONAL_PASS** (MEDIUM docstring 错误需在 rework 时修正)

---

## §4 回归风险

### 4.1 Gemini 代码其他分支未动 ✅

diff 确认:
- `_collect_terminology_sources` **core<=target 分支** (L254-278): 未动 (逻辑 = core 全量 + quest/supp 补尾).
- `questionnaires` / `supplementary` 收集逻辑: 未动.
- `_collect_core_sources` / `_collect_spec_sources` / `_collect_knowledge_sources`: 未动.
- `_write_merged` / `_file_header` / `_segment`: 未动.

### 4.2 v1.3b 相比 v1.3 差 (仅改循环顺序)

v1.3 (理论) vs v1.3b (落地) 关键差别:
```
# v1.3 (主 session 推演, 未落地):
selected = small_head + big_tail                 # small_head 先, big_tail 后
# v1.3b (已落地):
for p,_,t in reversed(big_tail): selected.append(...)  # big_tail 倒序先
for p,_,t in small_head: selected.append(...)    # small_head 后
```

新逻辑变更量: **2 个 for 循环 (5 行)**, 无新数据结构, 无新依赖. 回归面确实最小.

### 4.3 ChatGPT 回归风险 ✅

merge.py 只改 1 行 token_cap 数值; validate.py 只改 1 行 ExpectSpec cap 数值. 无逻辑变更, 无分支变更. 其他 8 个 MergeEntry 完全未动.

### §4 verdict: **PASS**

---

## §5 潜在 still-FAIL 风险

### 5.1 Gemini V3 (总 tokens)

独立验算 (假设 01/02/03 与 attempt_1 相同 / 04 = v1.3b 产物):

| 文件 | tokens |
|------|-------:|
| 01 | 124,512 |
| 02 | 185,785 |
| 03 | 275,318 |
| 04 (v1.3b) | 284,702 |
| **Total** | **870,317** |

阈值对照 (validate_gemini.py L84-86):
- `TOTAL_TOKEN_TARGET=800_000` (target, 超不 FAIL)
- `TOTAL_TOKEN_WARN=900_000` → rc=2 WARN
- `TOTAL_TOKEN_HARD=1_000_000` → rc=1 FAIL

870,317 > 800,000 target 但 < 900,000 WARN → 不触 WARN, 只触报告 "NOTE" (L528-530).

**独立结论**: V3 **不 FAIL 不 WARN**, 仅触 NOTE. 870K 距 900K 仅 29,683 tok (3.4%) — 若后续 04 再增 (如 KB 更新 lb_part3 tokens 升), 可能触 WARN.

### 5.2 Gemini V6 **仍 FAIL**

(§2.3 已详述)

### 5.3 Gemini V4 (单文件 <5MB) ✅

04 = 1,033,819 bytes ≈ 1.03 MB, 远 < 5MB. PASS.

### 5.4 ChatGPT 回归 ✅

v1.3 cap 47K, 01 实测 46,170 < 47,000 → V5 PASS. 其他 check (V1-V4, V7) 与 attempt_1 相同产物, 全 PASS.

### §5 verdict: **ChatGPT PASS / Gemini FAIL (V6)**

---

## 下一步建议 (给主 session)

### HIGH-1 (阻塞, 必修)

**Gemini `_collect_terminology_sources` core>target 分支重新 rework**. 至少 3 个修法方向:

**修法 A (推荐, 最小改动)**: 从 HIGH_FREQ_CORE_HINTS 排除 `is_domain_part2.md`, 改为显式"小文件池" (intv + qs + onc + oncology_part1/general_part1 取其小的), 且把预算从 `<= 80_000` 改成 `< 80_000` 且对 **单文件 tokens > 40_000 的 hint 主动 skip**. 这样 is_domain_part2 (69K) 不进, intv/qs/onc 3 段全进, small_head 有 3 markers 落 tail.

**修法 B**: 预算改成 "至少接纳 3 个 hint 文件后才停". 循环逻辑改为:
```python
for src in remaining:
    if src[0].name in HIGH_FREQ_CORE_HINTS:
        if len(small_head) < 3 or cum_small + src[2] <= 80_000:
            small_head.append(src)
            cum_small += src[2]
```
但这样不保证 V6 ≥3 tail (仍依赖物理 offset 落点).

**修法 C**: 直接在 HIGH_FREQ_CORE_HINTS 改序 + byte proxy 翻转. 按 **bytes 升序** 遍历 remaining (而不是 `core_by_size` 降序), 优先吃小文件 ⇒ intv(89K) + onc(89K) + qs(136K) 前 3 段会 ADD, cum_small 接近 79K ≈ budget, 然后 is_domain_part2 超即 skip. 预期 small_head = [intv, onc, qs], V6 能 PASS 3/3.

**建议采修法 C**, 因为它落回主 session 最初推演的 5 段语义 ([lb_part2, lb_part3, intv, onc, qs]), 物理 offset 推演基本正确, docstring 只需微调.

### MEDIUM (非阻塞, Node 3 收束时处理)

1. ChatGPT cap 统一升到 48K 或 50K (1.77% buffer 过紧).
2. PLAN.md 本 Node 延后同步的 cap / 策略改动, 在 Node 3 收束时一次性更新.
3. 修 v1.3b docstring 数据错误 (主 session 推演 [intv, qs, onc] 的 3 marker, 需要按 rework 后实际产出重写).

### LOW (后续 Node)

1. Rule A N=5 语义抽检 terminology 压缩结果 (压缩率 ~91% 必须做), Node 3 收束前必须安排.
2. Rule E Q4=A 偏离 ~42% 记入 RETROSPECTIVE (不是违规, 是妥协).

### 不可做

- ❌ 跑 attempt_2 (Gemini 必 V6 FAIL, 浪费运行).
- ❌ 降 V6 阈值 (选项 A, 用户已 Q2=C 否决).
- ❌ 改 KB (P5).

---

## 评分分项

| 项 | 满分 | 得分 | 备注 |
|---|:----:|:----:|-----|
| ChatGPT cap 正确性 | 20 | 18 | cap 对, buffer 薄 -2 |
| Gemini 文件存在性 | 10 | 10 | 5 hints 全存在 |
| Gemini UTF-8 风险 | 5 | 5 | 全 ASCII, 无风险 |
| Gemini 物理 offset | 30 | **0** | **推演错误 + V6 仍 FAIL** |
| Gemini 预算/budget 逻辑 | 15 | 5 | 80K cap 被 is_domain_part2 独占, 策略失效 |
| docstring 合规 | 10 | 7 | 引用 failure archive 到位; v1.3b 数据段有误 -3 |
| 回归风险 | 10 | 10 | 改动面确实最小 |
| **Total** | 100 | **55** | **FAIL_REWORK** |

---

## 独立证据

- 源脚本 diff: `git diff HEAD` (已查)
- HIGH_FREQ_CORE_HINTS 文件存在性: `ls -la knowledge_base/terminology/core/` 已验
- 物理 offset 模拟: `/tmp/simulate_v13b_exact.py` + `tiktoken cl100k_base`, 精确镜像 `_collect_terminology_sources`. 产物 final_tokens=284,702, markers=3, tail_count=1.
- UTF-8 扫描: 5 hint 文件 + lb_part2/lb_part3 全 0 非 ASCII.
- ChatGPT 01 实测 tokens: 46,170 (独立验算, 与 attempt_1 AB 一致).

---

*产物路径: 本文件同步写入 `ai_platforms/chatgpt_gpt/dev/evidence/phase3_node2_fix_reviewer.md`.*
