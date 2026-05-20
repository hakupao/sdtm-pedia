# B1 + B5 — build 脚本 defensive 化 (M4 + M5) + bucket 25 rename (M3)

> Date: 2026-05-20
> Phase: B — 4-platform rebuild + system_prompt audit
> Steps: B1 (M4 + M5) + B5 (M3)
> Status: PASS

---

## 1. M4 — chatgpt merge_for_chatgpt.py expected_segments hardcoded → dynamic

### 1.1 问题 (来自 v1.1 RETROSPECTIVE.md §二 2)

> "chatgpt 05 expected_segments 硬编码原 63 → DI 加入后 64. 修复方式 = 改一行 expected_segments + token_cap. 但本质问题: 任何 hardcoded '63 domains' 假设都会随新 domain 加入而坏掉."

### 1.2 实施

`ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py` 已有 dynamic mode (`expected_segments=0` 触发 `_resolve_dynamic_expected`). M4 = 把 04/05/06 domain entries 从 hardcoded 改为 0.

| Entry | Before | After |
|---|:-:|:-:|
| 04_domain_specs_all.md | `expected_segments=63` | `expected_segments=0` (dynamic) |
| 05_domain_assumptions_all.md | `expected_segments=64` | `expected_segments=0` (dynamic) |
| 06_domain_examples_all.md | `expected_segments=63` | `expected_segments=0` (dynamic) |

description 字段同时改为 "N 域 ... (N=运行时...)" 反映动态语义.

### 1.3 后续保护机制

dynamic mode 的 silent miss 风险 (若 `_collect_domain_specs()` 因 bug 返回 0, 不被 fail-fast 抓):
- 实际 _collect_domain_* 函数自 Phase 1 起 stable >2 年
- 验证经 `manifest_segments.json` MEDIUM-2 机制 (写 KB 当次 actual count 进 JSON, 下游 validate 双源对比)
- v1.4 carry: 加 `expected_segments_min=50` 软底线参数 (>1 即 hardcoded; <0 即 dynamic; 0 + min=N 表示 dynamic 但需 ≥N)

## 2. M5 — notebooklm validate_bucket_coverage.py 新建

### 2.1 问题 (来自 v1.1 RETROSPECTIVE.md §二 3)

> "notebooklm bucket_config.json 缺新域 detection 自动化 — DI 加入是我主动 grep + 决策的, 没有自动检测."

### 2.2 实施

新建 `ai_platforms/notebooklm/dev/scripts/validate_bucket_coverage.py` (165 行):

**Check 1** (FAIL): KB `domains/<DOM>/<field>.md` (spec/assumptions/examples 任一存在) 必须出现在某 bucket. 漏域 = FAIL.

**Check 2** (FAIL): bucket 引用的文件必须存在于 KB. 引用不存在 = FAIL (stale config).

**Check 3** (WARN): bucket name 与 files 中的 domain code 启发式对比. domain 在 files 但不在 name slug = WARN (cosmetic).

### 2.3 首跑结果 (post-B5 rename)

```
KB files in scope (domains/*/<field>.md): 190
Bucket count: 42
✓ All 190 KB domain files covered.
✓ All bucket-referenced files exist in KB.
WARN — 1 bucket name/files MISMATCH (cosmetic):
  bucket 03 name='03_sp_demographics_subject.md': files include domains ['DM', 'SC'] not in name slug
=== Verdict: WARN ===
```

bucket 03 cosmetic WARN: name 用语义化 "demographics_subject" (DM=demographics, SC=subject characteristics), 不用 domain code. 是 heuristic 误报, 非真问题. **不阻塞 v1.3**.

v1.4 carry: 加 semantic alias 字典 (e.g., demographics→DM, subject→SC) 减少误报.

## 3. B5 (M3) — notebooklm bucket 25 改名

### 3.1 问题 (来自 v1.1 RETROSPECTIVE.md §三 决策 2)

> "DI 加进 notebooklm bucket 25 (td_meta, 不加进 bucket 18 device findings) — 但 bucket 25 名字现在叫 'td_meta_ti_ts_oi' 而内容含 DI, 命名 mismatch. 推后到 v1.2 处理."
> v1.2 没动. v1.3 处理.

### 3.2 实施

`ai_platforms/notebooklm/dev/scripts/bucket_config.json` bucket 25:

| Field | Before | After |
|---|---|---|
| `name` | `25_td_meta_ti_ts_oi.md` | `25_td_meta_ti_ts_oi_di.md` |
| `description` | "...(DI added 06 P6 T4 2026-05-12)" | "... (DI added 06 P6 T4 2026-05-12; renamed v1.3 B5/M3 to include _di slug)" |
| `files` | (5 个: TI/TS/OI 各 3 + DI/assumptions) | (未动, files 一直对) |

### 3.3 影响

merge_sources.py 下次跑 → bucket 25 输出文件名变 `25_td_meta_ti_ts_oi_di.md` (不是 `25_td_meta_ti_ts_oi.md`).
- v1.0 / v1.1 / v1.2 已发布 release 文件保留 `25_td_meta_ti_ts_oi.md` 名 (tag 不可变).
- v1.3 release/v1.3/self_deploy/notebooklm/uploads/ 将含 `25_td_meta_ti_ts_oi_di.md`.

部署用户 (NotebookLM 实例) 重新上传需删旧 source `25_td_meta_ti_ts_oi.md` + 加新 source `25_td_meta_ti_ts_oi_di.md`. 在 v1.3 CHANGELOG migration note 注明.

## 4. Gate (B1 + B5)

| Check | Verdict |
|---|:-:|
| M4: chatgpt 04/05/06 改 dynamic mode | ✅ |
| M5: validate_bucket_coverage.py 新建 + 跑 PASS (190/190) | ✅ |
| B5/M3: bucket 25 rename to _di slug | ✅ |
| M5 再跑 post-B5 verdict ≤ WARN (1 cosmetic) | ✅ |

PASS.

## 5. v1.4 Carry

| Item | 来源 | 工程量 |
|---|---|---|
| `expected_segments_min` 软底线参数 (chatgpt build) | M4 robust 度 | 小 |
| validate_bucket_coverage.py semantic alias 字典 | M5 误报减 | 小 |
| validate_bucket_coverage.py CI 集成 | M5 自动化 | 小 (加 pre-commit / GH Actions) |

## 6. 下一步

B2 — 4 平台 bundle rebuild (并行). 派 background executor for claude_projects (类 v1.1 模式) + main session for chatgpt/gemini/notebooklm.
