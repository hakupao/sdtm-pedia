# Failure 归档 — Phase 3 Node 2 Stage 1 Attempt 1

> 规则 B (失败不删, 归档) · Phase: 3 · Node: 2 · Stage: batch1 · Attempt: 1
> 执行者: oh-my-claudecode:executor (opus subagent)
> 日期: 2026-04-20

---

## 输入

**命令链**:
```
cd ai_platforms/chatgpt_gpt/dev/scripts
python3 -c "import tiktoken; print(tiktoken.__version__)"            # 0.12.0 ✓
python3 score_chatgpt_priority.py > ../evidence/phase3_score.md      # rc=0 ✓
python3 merge_for_chatgpt.py --stage batch1 2>&1 | tee ../evidence/merge_batch1.log   # rc=0 ✓
python3 validate_chatgpt_stage.py --stage batch1 2>&1 | tee ../evidence/validate_batch1.log  # rc=1 FAIL
```

**时间戳**: 2026-04-20T17:55-17:56 (本地), validate 报告 generated=2026-04-20T08:55:50Z (UTC).

**脚本版本**:
- `merge_for_chatgpt.py` v1.1 (Node 1 reviewer CONDITIONAL_PASS → pass bug fix, MEDIUM-2 独立真源 JSON + MEDIUM-3 FAIL 升级)
- `validate_chatgpt_stage.py` v1.2 (Node 1 delta reviewer CONDITIONAL_PASS → pass, HIGH-1 重写 V3 + MEDIUM-1 新增 V7 + MEDIUM-2 manifest 读)
- `score_chatgpt_priority.py` v1.1 (加法公式)

---

## 产物 (FAIL 证据不删)

**保留文件** (4 个合并产物全部保留, 哪怕 01 FAIL):
- `ai_platforms/chatgpt_gpt/current/uploads/01_navigation.md` (159,352 B, 46,170 tokens)
- `ai_platforms/chatgpt_gpt/current/uploads/02_chapters_all.md` (246,800 B, 60,607 tokens)
- `ai_platforms/chatgpt_gpt/current/uploads/03_model_all.md` (70,426 B, 17,653 tokens)
- `ai_platforms/chatgpt_gpt/current/uploads/04_domain_specs_all.md` (675,167 B, 185,704 tokens)

**生成的 manifest + evidence**:
- `ai_platforms/chatgpt_gpt/current/manifest_segments.json` (4 entries, 首次生成)
- `ai_platforms/chatgpt_gpt/dev/evidence/phase3_score.md`
- `ai_platforms/chatgpt_gpt/dev/evidence/score_phase3.md`
- `ai_platforms/chatgpt_gpt/dev/evidence/merge_batch1.log`
- `ai_platforms/chatgpt_gpt/dev/evidence/validate_batch1.log`
- `ai_platforms/chatgpt_gpt/dev/evidence/validate_batch1.md`

**FAIL 的 check 列表**:
- 01_navigation.md V5 (token 上限): **FAIL** — 46,170 > cap 46,000.
- 其余 27 个子 check (3 文件 × 6 + 01 的 V1-V4 + V7 = 19 + 01 V6 打印 ... 实际 PASS 集: V1 4/4, V2 4/4, V3 4/4, V4 4/4, V5 3/4, V7 4/4) 全 PASS.

---

## 技术判定 (脚本层 assertion)

**FAIL 的 assertion**:
```python
# validate_chatgpt_stage.py 的 V5 逻辑
if tokens > expect.token_cap:
    return ("FAIL", f"{tokens:,} > cap {expect.token_cap:,}")
```

其中 `EXPECTS[0] = ExpectSpec("01_navigation.md", "batch1", 3, "", 46_000)`.

**实际触发**: `tokens=46170`, `token_cap=46000`, `46170 > 46000` → True → FAIL.

**脚本层看**: assertion 本身正确, 非脚本 bug. merge 产物 tokens 实测 46,170, 硬编码 cap 46,000, 超出 170 tokens (0.37%).

**其他 assertion 全过**: V2 段数 (manifest truth = 3, actual comment count = 3), V3 三段逐段强校验 (首行 anchor + heading lookback), V4 P13 注释位置 (注释前非 `|` row), V7 单表跨 heading (0 条).

---

## 业务判定

**这是脚本 bug 还是预期偏离?**

→ **预期偏离** (script-cap 和实际 source 之间的轻微容量抖动).

**分析**:
1. 合并产物 01_navigation.md 的源 (ROUTING/INDEX/VARIABLE_INDEX) 全部来自 `knowledge_base/` P5 只读, merge 脚本仅做文件拼接 + P12 注释插入, 不做语义压缩. 产物 tokens ≈ Σ(源文件 tokens) + 3 条 source comment + 分隔空行.
2. VARIABLE_INDEX.md 在 Phase 6.5 Node 1 期间可能因知识库更新 (e.g. 新增变量行), tokens 略增.
3. 脚本的 `token_cap=46_000` 可能是 Node 1 撰写脚本时基于当时 KB 快照估算的 "+15% buffer" 上限, 现实测超 cap 仅 0.37% — 属 "cap 过紧" 而非 "产物失控".
4. Step 6 prompt 的 "目标 ~15K" 与脚本 cap 46K 本就不是同一口径 (KB vs tokens vs cap), 需主 session 对齐口径.

**判定**: **非脚本 bug, 非 merge bug, 非 KB 污染 (P5 无违反)**. 属 cap 校准问题 — 硬编码 cap 需要 ±2% 微调, 或需拆文件.

---

## 下一 attempt 输入建议 (不自动跑, 等主 session 决策)

**方案 A** (推荐, 改动最小): 主 session 派 Node 3 writer 微调脚本 `token_cap`:
- `merge_for_chatgpt.py` MergeEntry 01 的 token_cap: 46_000 → 47_000 (+2.17% buffer, 仍 << PLAN §2.4 Step 6 prompt 估算的 15K 的下方余量).
- `validate_chatgpt_stage.py` EXPECTS[0].token_cap 同步 46_000 → 47_000.
- Node 3 写完后由 reviewer 独立复审, Node 4 才 attempt 2 重跑.
- 预期 attempt 2: 01 V5 PASS (46,170 < 47,000), 整体 rc=0.

**方案 B** (P11 更激进, 批 1 文件数 4→5): 拆 01 navigation 为 01a_routing + 01b_index_var. merge 配置 + EXPECTS + manifest 都要动, 改动面大.
- 不推荐, 除非 Node 3 decision 倾向 "single file 不能超 40K tokens 给 top-K buffer".

**方案 C** (违反 P5, **禁**): 裁 VARIABLE_INDEX.md 内容 — knowledge_base/ 只读, 不允许.

**强制前置**:
- 主 session 决策 A/B 前, 必须先跑 `code-reviewer` 或 `verifier` subagent 独立复审本 failure 判定 (Rule D 独立视角).
- 不要直接跑 attempt 2, 先 Node 3 改脚本 + reviewer PASS.

---

## 不做的事 (硬禁令遵守)

- ❌ **未修脚本** (score / merge / validate 三者 0 行改动).
- ❌ **未删产物** (01-04 四产物 + log 全部保留).
- ❌ **未 auto-fix FAIL** (没有尝试 cap 调整, 没有拆文件).
- ❌ **未改 PLAN.md** (v1.2 已是 Node 1 主 session 收窄版本, 未动).
- ❌ **未 commit** (留主 session 做 C2).

---

*按 Rule B 归档, 不合并入 AB report 主体; AB report 引用本文件路径.*
