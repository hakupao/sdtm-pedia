# ChatGPT GPTs — Phase 3 Node 2 Stage 1 (batch1) AB Report

> 日期: 2026-04-20
> Phase: 3 · Node: 2 (executor: opus subagent)
> Stage: batch1 (P0 文件 01-04)
> attempt: **2** (覆盖 attempt 1)
> Scripts: `score_chatgpt_priority.py` + `merge_for_chatgpt.py` **v1.3** + `validate_chatgpt_stage.py` **v1.3**
> 执行模式: 只跑不改 (硬禁令: 不修脚本 / 不删产物 / 不 auto-fix)

---

## attempt 1 Overview (简略, 完整归档见 failures/stage_1_attempt_1.md)

- attempt 1 产物结构健全 (V1-V4 + V7 全 PASS, 段数 / P12 / P13 / md5 全对齐).
- 唯一 FAIL 点: **V5 cap 单点**, `01_navigation.md` 46,170 tokens > cap 46,000 (超 170 tokens, 0.37% 边缘 FAIL).
- 决策: 经 3 轮 reviewer (pr-review-toolkit → feature-dev → oh-my-claudecode:critic) PASS, 采纳 **选项 A** = 调 `token_cap` 46K → 47K (+2.17% buffer), 不拆文件不裁 knowledge_base. 脚本升到 v1.3.
- attempt 2 预期: merge 输出确定性, 实际 tokens 不变 (46,170), 新 cap 47,000 → PASS, buffer 1.77%.

---

## Step 3 — Rule E 打分 (PLAN §3.2 v1.1)

**命令**: `python3 score_chatgpt_priority.py > ../evidence/phase3_score.md` (attempt 1 已跑, attempt 2 不重跑, 打分与 merge 无耦合)
**rc**: 0 (attempt 1 结果复用)

**排序结果** (符合 PLAN v1.1 预期, 与 attempt 1 一致):

| rank | 文件 | score | priority | audience | novelty | 批次 |
|:----:|------|:-----:|:--------:|:--------:|:-------:|:----:|
| 1 | 01_navigation.md | 3.40 | P0 | +0.2 | +0.2 | 1 |
| 2 | 02_chapters_all.md | 3.40 | P0 | +0.2 | +0.2 | 1 |
| 3 | 03_model_all.md | 3.20 | P0 | +0.2 | +0.0 | 1 |
| 4 | 04_domain_specs_all.md | 3.20 | P0 | +0.0 | +0.2 | 1 |
| 5 | 06_examples_all.md | 1.90 | P1 | +0.2 | +0.2 | 2 |
| 6 | 05_assumptions_all.md | 1.50 | P1 | +0.0 | +0.0 | 2 |
| 7 | 07_terminology_core.md | 1.20 | P2 | +0.2 | +0.0 | 2 |
| 8 | 08_terminology_questionnaires.md | 1.20 | P2 | +0.2 | +0.0 | 2 |
| 9 | 09_terminology_supplementary.md | 1.20 | P2 | +0.2 | +0.0 | 2 |

Evidence: `dev/evidence/phase3_score.md`, `dev/evidence/score_phase3.md`.

---

## Step 4 — merge_for_chatgpt --stage batch1 (attempt 2)

**命令**: `python3 merge_for_chatgpt.py --stage batch1 2>&1 | tee ../evidence/merge_batch1_attempt2.log`
**rc**: 0

**产物 (4 文件, 字节与 attempt 1 identical — merge 确定性验证)**:

| 文件 | tokens | target_cap (v1.3) | sources (actual/expected) | status |
|------|-------:|:----------:|:---------:|:---:|
| 01_navigation.md | 46,170 | ≤47,000 | 3/3 | **内** |
| 02_chapters_all.md | 60,607 | ≤72,000 | 6/6 | 内 |
| 03_model_all.md | 17,653 | ≤21,000 | 6/6 | 内 |
| 04_domain_specs_all.md | 185,704 | ≤193,000 | 63/63 | 内 |

**manifest_segments.json**: idempotent 覆盖, 4 entries (01 expected=3 actual=3, 02 expected=6 actual=6, 03 expected=6 actual=6, 04 expected=63 actual=63), 全部 `dynamic=false` `stage=batch1`. merge 脚本日志确认 "manifest: skipped (same)" — manifest 内容未变 (v1.3 fix 仅动 cap, 不动段数/源顺序).

**P12 溯源**: 每文件首行 `<!-- source: knowledge_base/... -->` 注释, 与 attempt 1 一致.

Evidence: `dev/evidence/merge_batch1_attempt2.log`, `current/manifest_segments.json`, `current/uploads/01-04_*.md`.

---

## Step 5 — validate_chatgpt_stage --stage batch1 (attempt 2)

**命令**: `python3 validate_chatgpt_stage.py --stage batch1 2>&1 | tee ../evidence/validate_batch1_attempt2.log`
**rc**: **0** (attempt 1 rc=1 → attempt 2 rc=0)

**矩阵 (28/28 PASS, v1.3 cap 47K 已生效)**:

| 文件 | V1 非空 | V2 段数 | V3 P12 覆盖 | V4 注释位置 | V5 token 上限 | V6 md5 | V7 表跨 heading | verdict |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 01_navigation.md | PASS | PASS | PASS | PASS | **PASS** | md5=555d17e5... | PASS | **PASS** |
| 02_chapters_all.md | PASS | PASS | PASS | PASS | PASS | md5=07a2edaf... | PASS | PASS |
| 03_model_all.md | PASS | PASS | PASS | PASS | PASS | md5=7fcf70b5... | PASS | PASS |
| 04_domain_specs_all.md | PASS | PASS | PASS | PASS | PASS | md5=79046731... | PASS | PASS |

**V5 详情 (v1.3 修复验证)**: `01_navigation.md: 46,170 ≤ cap 47,000` → PASS (buffer 830 tokens, 1.77%).

**md5 稳定性验证 (vs attempt 1)**:

| 文件 | attempt 1 md5 | attempt 2 md5 | identical ? |
|------|--------------|---------------|:-----------:|
| 01_navigation.md | 555d17e5ee0ae2d357b8ee2a3ba94d20 | 555d17e5ee0ae2d357b8ee2a3ba94d20 | YES |
| 02_chapters_all.md | 07a2edaf55abab8e9d08a790e6db5a8b | 07a2edaf55abab8e9d08a790e6db5a8b | YES |
| 03_model_all.md | 7fcf70b5c1035a4372013c7c238ff59c | 7fcf70b5c1035a4372013c7c238ff59c | YES |
| 04_domain_specs_all.md | 7904673feeef463333a56ec8d3625af0 | 7904673feeef463333a56ec8d3625af0 | YES |

4/4 md5 identical → **merge 确定性得证** (v1.3 仅动 validate 的 cap 配置, 未动 merge 逻辑 / 不改 uploads 内容).

**其他 check 解读**:
- V1: 4/4 非空.
- V2: 段数 == manifest truth (3/6/6/63), 全对齐.
- V3: P12 溯源覆盖率逐段强校验, 全过.
- V4: source comment 无一落入 `|` table row 内部.
- V7 (v1.2/v1.3 收窄): 单表跨 heading 0 条.
- V6: md5 attempt 1 = attempt 2 (稳定).

Evidence: `dev/evidence/validate_batch1_attempt2.log`, `dev/evidence/validate_batch1.md` (已覆盖为 4/4 PASS 版本).

---

## Step 6 — token 偏差检查 (attempt 2, vs 脚本 v1.3 cap)

**偏差表 (对比脚本 v1.3 token_cap)**:

| 文件 | 实际 tokens | 脚本 cap (v1.3) | 偏差 vs cap | 状态 |
|------|-----------:|---------:|:----:|:---:|
| 01_navigation.md | 46,170 | 47,000 | **−1.77%** | 内 (attempt 1 为 +0.37% 超) |
| 02_chapters_all.md | 60,607 | 72,000 | −15.82% | 内 (不变) |
| 03_model_all.md | 17,653 | 21,000 | −15.94% | 内 (不变) |
| 04_domain_specs_all.md | 185,704 | 193,000 | −3.78% | 内 (不变) |

**偏差表 (对比 PLAN §2.4 Step 6 prompt 粗估, WARN 保留, 不阻塞)**:

| 文件 | 实际 tokens | Step 6 prompt 估算 | 偏差 | >15% ? |
|------|-----------:|-----------:|:----:|:-----:|
| 01_navigation.md | 46,170 | ~15,000 | +207.8% | WARN |
| 02_chapters_all.md | 60,607 | ~30,000 | +102.0% | WARN |
| 03_model_all.md | 17,653 | ~30,000 | −41.2% | WARN |
| 04_domain_specs_all.md | 185,704 | ~150,000 | +23.8% | WARN |

**说明**: PLAN §2.4 "估算大小" 列的粗估口径与脚本 token_cap 真源不一致, WARN 保留. 建议 Phase 4 阶段由主 session 统一口径回写 upload_manifest.md (超本 Node 范围).

---

## Overall Verdict

**PASS** — Step 5 attempt 2 全 28/28 check PASS (V1-V7 × 4 文件 + V6 md5 稳定). merge 产物 4/4 md5 vs attempt 1 identical, 确认 v1.3 修复只动 validate cap 配置, uploads/ 字节不变. v1.3 fix 方案 (cap 46K → 47K) 落地生效.

**关键事实**:
- 01_navigation.md V5: 46,170 ≤ cap 47,000 → PASS, buffer 1.77% (830 tokens).
- 其他 3 文件偏差不变 (−15.82% / −15.94% / −3.78%), 均在 cap 内.
- md5 4/4 identical attempt 1 ↔ attempt 2, merge 确定性得证.
- manifest_segments.json idempotent 覆盖 (日志 "skipped (same)").

---

## 下一步建议 (给主 session)

1. **ChatGPT Node 2 Stage 1 批 1 产物可上线** (pending 主 session 派 reviewer 复核本 AB + Gemini attempt 2 同步).
2. **等 Gemini attempt 2**: 另一 executor 并行跑 Gemini 脚本 attempt 2. 双平台锁步规则 (SYNC_BOARD) 要求两边 attempt 2 都 PASS 再推 Phase 4.
3. **派 reviewer subagent**: Rule D 要求独立 subagent_type 复核本 AB. 建议 verifier / code-reviewer.
4. **failures/ 归档保留** (Rule B): `failures/stage_1_attempt_1.md` 不删, 作为 cap 决策的完整链路证据.
5. **未解 WARN**: Step 6 prompt 口径 vs 脚本 cap 口径不一致, 建议 Phase 4 起草 upload_manifest.md 时统一.

---

*generated by executor opus subagent, Phase 3 Node 2 attempt 2, Rule D (writer) — 独立 reviewer 请由主 session 派 verifier subagent 复核.*
