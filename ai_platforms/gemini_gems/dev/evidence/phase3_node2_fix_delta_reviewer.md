# Phase 3 Node 2 fix v1.3c Delta Reviewer Report

> Date: 2026-04-20
> Reviewer subagent_type: `feature-dev:code-reviewer` (Rule D 第 6 种独立 subagent_type)
> Scope: v1.3b → v1.3c delta only (5-line code change + docstring + inline comments in `_collect_terminology_sources` core>target branch of `merge_for_gemini.py`).
> Prior reviewer: `pr-review-toolkit:code-reviewer` FAIL_REWORK (HIGH-1, 推荐修法 C = remaining 升序)
> 持久化: 本文件由主 session 从 subagent transcript 落盘 (feature-dev:code-reviewer 无 Write 工具).

---

## 1. Delta 准确实现 "bytes 升序" 修法?

| Check | Result | Evidence |
|-------|:------:|---------|
| `remaining_asc = sorted(core_by_size[2:], key=lambda x: x[1])` 存在 | PASS | L319 |
| `x[1]` 是 bytes (非 tokens) | PASS | L257 docstring 明示 `(path, bytes, tokens)` |
| 预算用 `src[2]` (tokens) | PASS | L325 `if cum_small + src[2] <= 80_000` |
| for 循环用 `remaining_asc` | PASS | L322 |
| 升序 (no minus sign) | PASS | `key=lambda x: x[1]` |

**§1 Verdict: PASS** — 机械实现正确.

---

## 2. V6 物理 offset 独立重算 (**关键**)

### Step 1: remaining_asc bytes 升序

| File | bytes | tokens (精确 tiktoken) |
|------|------:|-------:|
| oncology_part1.md | 89,521 | 24,651 |
| interventions.md | 89,805 | 23,235 |
| qs_part1.md | 136,529 | 36,059 |
| general_part1.md | 221,871 | 61,564 |
| is_domain_part2.md | 238,488 | 69,376 |

升序: onc → intv → qs → general_part1 → is_domain_part2.

### Step 2: 预算模拟 (80,000 token cap, 精确 tiktoken)

| iter | File | in HINTS? | tokens | cum | Decision |
|:---:|---|:---:|---:|---:|---|
| 1 | onc | ✓ | 24,651 | 24,651 | ADD |
| 2 | intv | ✓ | 23,235 | 47,886 | ADD |
| 3 | qs | ✓ | 36,059 | **83,945** | **SKIP** (> 80,000) |
| 4 | general_part1 | ✓ | 61,564 | — | SKIP |
| 5 | is_domain_part2 | ✓ | 69,376 | — | SKIP |

**small_head = [onc, intv] — 只 2 段.**

docstring L62 写 "intv(22K)+onc(22K)+qs(34K) 累计 78K ≤ 80K 全中" 用四舍五入近似, 实际 tiktoken 累加 **83,945 tok > 80,000** → qs 运行时被 skip.

### Step 3: selected 构成 + 物理 offset

selected = [lb_part2, lb_part3, onc, intv] — **4 段**.

Physical char offsets (ASCII, len==bytes):

| Segment | `<!-- source:` marker 位置 | 相对 tail_start |
|---|---:|:---:|
| lb_part2 | ~290 | HEAD |
| lb_part3 | ~378,197 | HEAD |
| onc | ~795,258 | TAIL ✓ |
| intv | ~884,834 | TAIL ✓ |

Total bytes ≈ 974,694; **tail_start = int(974,694 × 0.70) = 682,285**.

V6 tail_count = **2** (onc + intv), 需 ≥ 3 → **V6 HARD FAIL (rc=1)**.

docstring 称 "V6 PASS 3/3" 与 "selected=5 段" 均错误 (基于四舍五入 token 值的累加错误).

**§2 Verdict: FAIL — HIGH-2 (blocks attempt_2)**

根因: 80K token budget 太紧. onc+intv 已 47,886, 剩 32,114 不足 qs (36,059). 修法: budget 80,000 → 90,000 (或 84,000 边界紧配); 83,945 ≤ 90,000 → 全中 → selected=5 段 → V6 tail_count=3 PASS.

---

## 3. docstring v1.3c 合规

| Check | Result | Notes |
|---|:---:|---|
| 追加在 v1.3b 段之后 | PASS | L56-66, v1.3b at L48-54 preserved |
| 引用 reviewer pr-review-toolkit | PASS | L56 |
| 明示修法 "bytes 升序" | PASS | L62 |
| Physical offset 数据 match §2 重算 | **FAIL** | L62 "78K ≤ 80K 全中" 与运行时 83,945 > 80,000 冲突 |
| 称 "selected 5 段" | **FAIL** | 实际 4 段 |
| 称 "V6 PASS 3/3" | **FAIL** | 实际 tail=2 FAIL |

**§3 Verdict: FAIL** — 三处事实错误, 来自同一 rounded-token 算术误差. 非外观问题, 未来阅读者会被误导.

---

## 4. 回归风险

| Check | Result |
|---|:---:|
| 改动仅 remaining_asc sort + docstring | PASS |
| `big_tail` 逻辑未改 | PASS |
| `reversed(big_tail)` 循环未改 | PASS |
| small_head append 模式未改 | PASS |
| selected.append() 模式未改 | PASS |
| core<=target 分支未动 | PASS |
| questionnaires/supplementary 未动 | PASS |
| `py_compile` 语法 | Cannot run (reviewer 无 Bash 工具), 但代码语法合法 lambda, 无新 import |

**§4 Verdict: PASS** — delta 真正最小, 无 §2 以外回归风险.

---

## 5. ChatGPT 脚本独立性

- `merge_for_chatgpt.py` L218-225 token_cap=47_000 (v1.3 改动确认)
- `validate_chatgpt_stage.py` L117 ExpectSpec cap=47_000 (v1.3 改动确认)
- v1.3c delta 只动 `merge_for_gemini.py`, ChatGPT 两脚本未触碰

**§5 Verdict: PASS** — 无 cross-contamination.

---

## Overall Verdict: **FAIL_REWORK (HIGH-2)**

| § | Verdict |
|---|:---:|
| §1 delta 机械实现 | PASS |
| §2 V6 physical offset 重算 | **FAIL — HIGH-2** |
| §3 docstring 合规 | FAIL (consequential on §2) |
| §4 回归风险 | PASS |
| §5 ChatGPT 独立性 | PASS |

### HIGH-2 (blocks attempt_2)

**Location**: `merge_for_gemini.py` L319-327 + L62-66 docstring

**Issue**: 80,000 token budget 不足收纳 onc+intv+qs. 精确 tiktoken: onc=24,651 + intv=23,235 = 47,886; qs=36,059; 累加 83,945 > 80,000. 运行时 qs skip. small_head 只 2 文件 (onc, intv), selected=4 段, V6 tail_count=2 < 3 required.

**Fix (minimal)**:
```python
# L325:
if cum_small + src[2] <= 80_000:  →  if cum_small + src[2] <= 90_000:
```

预期 v1.3d: onc(24,651) + intv(23,235) + qs(36,059) = 83,945 ≤ 90,000 全中 → small_head=3, selected=5 段, tail_count=3 → V6 PASS.

docstring 对应需更新:
- L62: "78K ≤ 80K 全中" → "83.9K ≤ 90K 全中 (精确 tiktoken)"
- L63: "selected 5 段" (现正确)
- L65-66: tail 计算需重算 (~1,111,278 bytes; tail_start ~777,894; 3 markers @ 795K/884K/974K 全 > 777K)

**Confidence: 95** — tiktoken 每文件精确值独立于迭代顺序.

---

## 建议给主 session

- **禁止跑 attempt_2** (v1.3c 必 V6 FAIL, tail_count=2 < 3)
- **v1.3d 改 1 数字 + docstring 同步**
- **Rule D 独立 reviewer 第 3 轮建议**: 用未用过的 subagent_type (e.g. `oh-my-claudecode:critic`, `pr-review-toolkit:silent-failure-hunter`) 做 v1.3d narrow delta 审
- 同时建议 Node 3 收束时考虑: budget cap 应显式化为 `HIGH_FREQ_BUDGET_TOKENS = 90_000` 常量 + inline 注释引用三轮 reviewer 的 token 精算

---

*evidence file persisted from feature-dev:code-reviewer subagent transcript, 主 session 代写 (reviewer 无 Write 工具).*
