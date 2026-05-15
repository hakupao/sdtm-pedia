# Rule D Independent Review — v1.1 Rebuild

> Date: 2026-05-15
> Reviewer subagent_type: **oh-my-claudecode:verifier** (独立 lane, 与 main session opus 隔离)
> Writer / executor (隔离对象): main session claude (opus) + executor subagent (sonnet) — 由 main session 编排 4 平台 rebuild
> 隔离声明: 本审计在独立 verifier subagent context 完成, 未参与任何 build/write 动作, 仅做 read-only 证据核验
> Scope: 验证 06 旁枝 (P1-P7, 43 文件 +1,405/-234 行) 通过 4 平台 build pipeline 真实回灌至 release v1.1 uploads, 无 silent loss / regression / KB 反向污染

---

## § 评估 1 — Evidence 完整性

**Verdict**: **PASS**

| 文件 | 存在 | 大小 | 内容质量 |
|------|------|------|---------|
| `.work/07_release_v1_1/PLAN.md` | yes | 5.2K | 完整 10 步, Rule A/B/C/D 全显式声明, 退出标准列 7 条 |
| `.work/07_release_v1_1/RETROSPECTIVE.md` | yes | 7.6K | Rule C 三段齐备 (保留/缺口/决策复盘), 含终态数字表 |
| `evidence/diff_summary.md` | yes | OK | 4 平台 baseline→rebuilt byte-delta + 原因列, 含跨平台 oracle 一致性 (chatgpt 05 +74,178 == gemini 02 +74,178) |
| `evidence/chatgpt_rebuild.log` | yes | OK | 两跑都记录: 第一次 fail-fast (segment 64 != 63), 改脚本后第二次成功; baseline 未被破坏 (fail-fast abort write) |
| `evidence/gemini_rebuild.log` | yes | OK | 3 stages 全 PASS, cumulative 610,596 tokens < target 820K |
| `evidence/notebooklm_rebuild.log` | yes | OK | 42 bucket 全产出, missing=0, total 1,599,332 words, 0 over-cap |
| `evidence/claude_rebuild.log` | yes | OK | 7 file 重建详细 + path 修复说明 + Step 1-4 完整 |
| `failures/claude_rebuild_failures.md` | yes | OK | Rule B 合规, F1-F4 各项: 输入/产物/技术判定/业务判定/下一 attempt 输入俱全 |

**关键证据片段**:
- chatgpt_rebuild.log L1: `[Stage chatgpt-batch2] 05_domain_assumptions_all.md: FAIL segment count 64 != PLAN-expected 63 (fail-fast, abort write)` — 证明 baseline 未被坏数据覆盖 (write 被 abort)
- claude_rebuild_failures.md F4: 明确记录 path resolution bug + workaround + 下一步建议

---

## § 评估 2 — KB → uploads 可追溯性 (Rule A 抽检 N=5)

**Verdict**: **PASS (5/5 samples ALL HIT)**

### Sample 1 — PC §6.3.5.9 RELREC linking → 4 平台
唯一字符串: `"Relating PP Records to PC Records"` (PC/assumptions.md 第 19 行 `## §6.3.5.9.3` 锚)

| 平台 | 文件 | "Relating PP Records to PC Records" 命中 | "6.3.5.9" 命中 | 结果 |
|------|------|:---:|:---:|:---:|
| chatgpt | `current/uploads/05_domain_assumptions_all.md` | 2 | 3 | PASS |
| gemini  | `current/uploads/02_domains_spec_and_assumptions.md` | 2 | 3 | PASS |
| claude  | `current/uploads/06_assumptions.md` | 1 | 2 | PASS |
| notebooklm | `current/uploads/16_fnd_pharma_pc_pp.md` | 4 | 6 | PASS |

### Sample 2 — DI domain (新加文件) → 4 平台
唯一字符串: `"DI dataset was introduced"` + `"SDTMIG-MD"` (DI/assumptions.md L3-5)

| 平台 | 文件 | "DI dataset was introduced" 命中 | "SDTMIG-MD" 命中 | 结果 |
|------|------|:---:|:---:|:---:|
| chatgpt | `05_domain_assumptions_all.md` | 1 | 3 | PASS |
| gemini  | `02_domains_spec_and_assumptions.md` | 1 | 3 | PASS |
| claude  | `06_assumptions.md` | 1 | 1 | PASS |
| notebooklm | `25_td_meta_ti_ts_oi.md` | 1 | 1 | PASS — DI 在 bucket 25 正确出现 |

### Sample 3 — TA/assumptions.md (+175 行) → 4 平台
唯一字符串: `"Distinguishing Between Branches and Transitions"` (TA L100 锚) + `"Trial Arms Issues"`

| 平台 | 文件 | "Distinguishing Between Branches and Transitions" 命中 | "Trial Arms Issues" 命中 | 结果 |
|------|------|:---:|:---:|:---:|
| chatgpt | `05_domain_assumptions_all.md` | 1 | 1 | PASS |
| gemini  | `02_domains_spec_and_assumptions.md` | 1 | 1 | PASS |
| claude  | `06_assumptions.md` | 1 | 1 | PASS |
| notebooklm | `23_td_arms_ta_tv.md` | 3 | 3 | PASS |

### Sample 4 — chapters/ch02_fundamentals.md → 4 平台
唯一字符串: `"Variable Roles"` + `"Datasets and Domains"` + `"Qualifier Variable Subclasses"` (ch02 多锚)

| 平台 | 文件 | VR | D&D | QVS | 结果 |
|------|------|:---:|:---:|:---:|:---:|
| chatgpt | `02_chapters_all.md` | 1 | 1 | 1 | PASS |
| gemini  | `01_navigation_and_quick_reference.md` | 2 | 1 | 2 | PASS |
| claude  | `02_chapters.md` | 1 | 1 | 1 | PASS |
| notebooklm | `28_ig_ch01_ch02_ch03.md` | 1 | 1 | 1 | PASS |

### Sample 5 — chapters/ch08_relationships.md → 4 平台
唯一字符串: `"Relating Groups of Records Within a Domain Using --GRPID"` + `"Relating Datasets Using RELREC"` + `"RELREC Dataset Examples"`

| 平台 | 文件 | GRPID | Datasets | Examples | 结果 |
|------|------|:---:|:---:|:---:|:---:|
| chatgpt | `02_chapters_all.md` | 1 | 1 | 2 | PASS |
| gemini  | `01_navigation_and_quick_reference.md` | 1 | 1 | 2 | PASS |
| claude  | `02_chapters.md` | 1 | 1 | 2 | PASS |
| notebooklm | `30_ig_ch08_ch10.md` | 1 | 1 | 2 | PASS |

**汇总**: 5 KB-源 × 4 平台 × ≥2 字符串 = 20 平台-字符串 全部命中 ≥1 次. 无 silent loss.

---

## § 评估 3 — Build script 改动正确性

**Verdict**: **PASS (最小必要 + 无新风险)**

### 改动 1: `merge_for_chatgpt.py` 05 entry
```python
MergeEntry(
    target="05_domain_assumptions_all.md",
    stage="batch2",
    description="64 域 assumptions.md (含 DI SDTMIG-MD, 06 deep verification 新加)",
    source_collector=_collect_domain_assumptions,
    expected_segments=64,         # 63 → 64
    token_cap=85_000,             # 69_000 → 85_000
```
- **必要性**: 实测 73,079 tokens (源 64 文件) — `expected_segments=63` 会触发 fail-fast (实测发生); 不改 token_cap 即便段数对也会因 73K > 69K 超 cap 失败. 两项改动绑定必要.
- **风险评估**: 仅扩 cap +23% (69K → 85K), 仍远低于 OpenAI 200K 上下文上限. 段数对 KB 改动一一对应. **不引入风险**.
- **遗留缺口** (RETROSPECTIVE §二.2 已记录): hardcoded segment count 在下次新增 domain 时还会坏, 应改 runtime-resolved. 不阻塞本次 release.

### 改动 2: `bucket_config.json` bucket 25
```json
{
  "id": 25, "name": "25_td_meta_ti_ts_oi.md",
  "files": [
    "domains/TI/spec.md", "domains/TI/assumptions.md", "domains/TI/examples.md",
    "domains/TS/spec.md", "domains/TS/assumptions.md", "domains/TS/examples.md",
    "domains/OI/spec.md", "domains/OI/assumptions.md", "domains/OI/examples.md",
    "domains/DI/assumptions.md"       ← 新加
  ]
}
```
- **必要性**: notebooklm 用 hardcoded list, 不像 chatgpt/gemini 扫目录. 不主动加 DI 它就被静默漏掉.
- **决策正确性**: bucket 25 为 "study reference dataset" (TI/TS/OI), DI 在 SDTM v1.7+ 也是 study reference dataset (DI/assumptions.md L3 明示) — 类型匹配.
- **风险**: 1 文件 (~65 words) 加入 8K word bucket, 远低于 500K cap (实际 bucket 25 仅 8,651 words). **不引入 over-cap 风险**.
- **遗留缺口** (RETROSPECTIVE §二.3 已记录): bucket name 仍叫 `25_td_meta_ti_ts_oi.md` 而含 DI, 命名 mismatch — 推后到 v1.2 解决 (避免破坏部署 URL). 不阻塞.

---

## § 评估 4 — Release v1.1 包结构

**Verdict**: **PASS**

### 4.1 文件数比对 (v1.0 vs v1.1 uploads)
| 平台 | v1.0 uploads | v1.1 uploads | Δ | 结果 |
|------|:---:|:---:|:---:|:---:|
| chatgpt | 9 | 9 | 0 | PASS (idempotent terminology + refreshed 02/03/05/06) |
| claude | 19 | 19 | 0 | PASS (refreshed 7, unchanged 12) |
| gemini | 4 | 4 | 0 | PASS (refreshed 1/2/3, 04 writer-authored 不动) |
| notebooklm | 43 | 43 | 0 | PASS (含 42 buckets + 索引文件) |

Note: BUILD_MANIFEST 说 notebooklm `files_count=42` 但 ls=43 — 差 1 是 `00_README.md` / 索引类元文件, 不是 bucket. 不算 manifest 错 (manifest 报告的是 buckets count). **建议在 v1.2 manifest 字段 rename `files_count` → `buckets_count`** 消歧.

### 4.2 元文档继承 (system_prompt + tutorial.{en,zh,ja})
```
=== meta-docs unchanged from v1.0 ===
[diff -q output: 0 行 — 完全相同]
```
4 平台 × 5 候选文件 (system_prompt.md | instructions.md + tutorial 三语) **全部 byte-identical**. **PASS**.

### 4.3 CHANGELOG 三语一致 + 准确
| 文件 | 大小 | 关键事实 |
|------|------|----------|
| `CHANGELOG.en.md` | 4.7K | "64 domains (was 63)", "+1,405/-234 lines", "DI", "PC §6.3.5.9", "TA +175" |
| `CHANGELOG.zh.md` | 4.0K | 同上 (中文措辞精炼) |
| `CHANGELOG.ja.md` | 4.4K | 同上 (日文术语精准, 例 "支線" / "ナレッジベース") |
三语 head 比对: release tag / previous tag / 43 文件 / +1,405-234 / 64 domains / DI / PC §6.3.5.9 / TA +175 全部一致. **PASS**.

### 4.4 BUILD_MANIFEST.json 字段完整性
顶层 keys: `release_tag, release_date, previous_tag, previous_date, driver, knowledge_base, platforms, verification, unchanged_from_v1_0` — 全部存在.
平台子键: `claude, chatgpt, gemini, notebooklm` (每平台含 `uploads_dir, files_count, files_changed_in_v1_1` 等).
verification 字段指向 `diff_summary.md / rule_d_review.md / RETROSPECTIVE.md` 三个 evidence 文件 (本文件即其一).
unchanged_from_v1_0 字段明示 7 metadata_docs + 4 平台 system_prompt 不变.
**PASS**.

### 4.5 release/v1.1/uploads vs current/uploads 一致性
```
chatgpt:    diff -rq 输出 0 行  → 完全一致
claude:     diff -rq 输出 0 行  → 完全一致
gemini:     "Only in current: .omc"  → release 不含开发临时目录 (正确)
notebooklm: diff -rq 输出 0 行  → 完全一致
```
release v1.1 uploads 真实反映 current/uploads 状态. **PASS**.

---

## § 评估 5 — 红线项 (KB 反向污染 / baseline / failures)

**Verdict**: **PASS (3/3 红线无突破)**

### 5.1 KB 未被反向污染
```
$ git diff HEAD -- knowledge_base/
[空输出]
$ git diff HEAD --stat -- knowledge_base/ | tail -5
[空输出 — 当前 working tree 对 KB 零修改]
```
所有 build script 严格 read-only KB. **PASS**.

### 5.2 baseline 完整保留
```
chatgpt baseline:   9 files, 9.2M
claude baseline:   19 files, 4.6M
gemini baseline:    4 files, 2.1M
notebooklm baseline: 43 files, 9.3M
Total: 25 MB (符合 PLAN §Step 1 声明)
```
baseline 完整存活. 即使 chatgpt 第一次 fail (fail-fast abort write) baseline 也未被坏数据覆盖 (从 log L1 可证). **PASS**.

### 5.3 失败归档存在
```
$ ls failures/
claude_rebuild_failures.md
```
含 F1-F4 (DI no-spec / DI no-examples / 09 over-cap / path bug), 每条 5 字段 (输入/产物/技术判定/业务判定/下一 attempt). Rule B 合规. **PASS**.

---

## § 总判定

**ALL_PASS** ✅

**核心证据**:
1. **Rule A 抽检 5/5 命中**: 20 平台-字符串 zero miss
2. **Rule B 失败归档完整**: failures/ 含 F1-F4 五字段
3. **Rule C Retro 三段齐备**: RETROSPECTIVE.md 保留/缺口/决策复盘 + 终态数字表
4. **Rule D 隔离**: 本审计在独立 verifier subagent 完成, writer (main + executor sonnet) ≠ reviewer (verifier)
5. **红线全过**: KB 零回污染 / baseline 25MB 完整保留 / failures 归档存在
6. **跨平台 oracle 自洽**: chatgpt 05 +74,178 bytes ≡ gemini 02 +74,178 bytes (同 KB 不同 pipeline 同 delta), 强证据无 silent loss
7. **build script 改动最小必要**: 仅 2 处 (chatgpt 05 entry expected_segments+token_cap, notebooklm bucket 25 加 DI), 不引入新风险
8. **release 元文档继承**: 4 平台 × 5 元文件 = 20 byte-identical, 方法论层未动 (与 06 内容修复职责吻合)

**轻微观察 (不阻塞 release v1.1 cut, 后续改善建议)**:

| # | 项 | 严重度 | 建议时机 |
|---|----|:------:|:--------:|
| O1 | bucket 25 命名仍是 `25_td_meta_ti_ts_oi.md` 但内容含 DI — 命名 mismatch | LOW | v1.2 (避免破坏 v1.1 部署 URL) |
| O2 | chatgpt `expected_segments` 仍 hardcoded — 下次新 domain 还会坏 | LOW | v1.2 build script 改为 runtime resolve |
| O3 | notebooklm 缺 `validate_bucket_coverage.py` — 新 domain 加入靠人工 grep | LOW | v1.2 加 validation CI step |
| O4 | 没跑 SMOKE_V4 验证部署后回答质量 — 仅验证了"上传包结构" | MEDIUM | v1.2 部署后跑 R3 vs R1 对比 |
| O5 | BUILD_MANIFEST 里 notebooklm `files_count=42` 与 ls=43 略偏 (索引文件) | LOW | v1.2 字段 rename → `buckets_count` |

**注**: O1-O5 全部在 RETROSPECTIVE.md § 二 "必须补上的缺口" 已主动记录, 不属遗漏.

---

## § 给 main session 一句话

`Rule D verdict: ALL_PASS; 5 个评估全过, Rule A 5/5 抽检命中 (20 平台-字符串 zero miss), KB 未反向污染, baseline 25MB 完整, failures Rule B 合规, 元文档 byte-identical 继承 v1.0, 跨平台 delta oracle 自洽 (chatgpt 05 ≡ gemini 02 = +74,178 bytes); 5 项 LOW/MEDIUM 改善观察 (O1-O5) 已在 RETROSPECTIVE §二 主动记录, 不阻塞 v1.1 cut; 详见 evidence/rule_d_review.md`
