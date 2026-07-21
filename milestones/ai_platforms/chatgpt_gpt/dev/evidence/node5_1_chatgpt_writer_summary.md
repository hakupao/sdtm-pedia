# Phase 6.5 ChatGPT GPTs · Phase 4 Node 5.1 — Writer Summary (P5 ChatGPT LOW Cleanup)

> **Writer**: oh-my-claudecode:executor (opus)
> **Date**: 2026-04-21
> **Scope**: Phase 3 N4 carry-over P5 (4 子项 LOW cleanup) + smoke v2 CO-2 (MEDIUM CMINDC 严苛化)
> **Upstream**: `ai_platforms/PHASE4_PLAN.md` §4 P5 行
> **Carry-over sources**: `phase3_node4_reviewer.md` (L1 L2 S2) + `smoke_v2_reviewer.md` (MEDIUM M1 / CO-2)

## 整体 verdict

PHASE4_N5_1_CHATGPT_WRITER 4/4 子项全部落地, 未跑 merge (P5 不涉 KB), 未跑 smoke (Phase 4 N5.2 主任务).

两脚本 py_compile PASS, system_prompt.md ≤ 8000 bytes budget 合规, upload_manifest.md README/order/Step 5/7 全量 batch 2 同步.

## 子项 1 — validate_chatgpt_stage.py L519 header 版本同步 (LOW L1)

**Before**:
```python
# L105-107 (imports 后)
ENCODING_NAME = "cl100k_base"

# L519 (render_report)
"> Script: `dev/scripts/validate_chatgpt_stage.py` (v1.1)",
```

**After**:
```python
# L105-111 (imports 后)
# 模块级版本常量 (Phase 4 N5.1 LOW L1 fix, reviewer phase3_node4_reviewer.md):
# 避免 render_report 硬编码 "(v1.1)" 与 docstring v1.5 不一致. 升版时改此处.
SCRIPT_VERSION = "v1.5"

ENCODING_NAME = "cl100k_base"

# L523 (render_report)
f"> Script: `dev/scripts/validate_chatgpt_stage.py` ({SCRIPT_VERSION})",
```

**Rationale**: docstring 已记录 v1.3/v1.4/v1.5 三次 sync (行 71-92), 但 render_report 始终输出 "(v1.1)". 次要成本: future 升版只改一处 SCRIPT_VERSION 常量, 不用同步 render_report inline 字符串.

**Verify**: `python3 -m py_compile` → PASS.

## 子项 2 — merge_for_chatgpt.py legacy helper DEPRECATED 标注 (SUGGESTION S2)

**Before** (行 239):
```python
def _collect_terminology(subdir: str) -> list[Path]:
    """legacy helper (v1.3 及以前): terminology/<subdir>/*.md, sorted.

    v1.4 起 07/08/09 不再直接用此 helper 作 collector, 仅保留供调试用.
    ...
    """
```

**After** (行 239-245):
```python
# DEPRECATED (Phase 4 N5.1): 此 helper 由 merge_for_chatgpt.py v1.5 的硬编码 MERGE_CONFIGS
# (07/08/09 expected sources 固定 15/49/27) 取代, 未来新批次引入新术语子库时再评估复用.
# 保留函数签名防 import 断裂, 但新代码不得调用.
def _collect_terminology(subdir: str) -> list[Path]:
    """legacy helper (v1.3 及以前): terminology/<subdir>/*.md, sorted.
    ...
    """
```

**Rationale**: 约束明示"不删除函数, 只加 DEPRECATED 注释块". 函数签名保留 → 防 import 断裂 (目前脚本本身无 import 用, 但保守处理). 注释块放在 def 上方 (Python 约定 top-level comment 紧贴 target).

**Verify**: `python3 -m py_compile` → PASS.

## 子项 3 — upload_manifest.md README/order 语义段手动同步 (LOW L2)

**Before — Header 段 (L1-8)**:
- "Phase 3 Node 3" 标题
- "状态: Ready to Upload (批 1 P0)"
- 最后更新 2026-04-20
- 总计 "批 1 = 4 文件 / 4/20 文件硬限 / 16 spare (批 2 预计再占 5-6)"

**After — Header 段 (L1-8)**:
- "Phase 3 Node 3 + Node 4" 标题
- "状态: Ready to Upload (批 1 + 批 2, 共 9 文件)"
- 最后更新 2026-04-21 (N5.1 同步)
- 总计 "9 文件 (batch 1+2 合计 2,531,313 tokens, 9/20 GPT Builder 槽位, 11 spare)"

**Before — 上传顺序段 (L12-14)**:
- 仅批 1 顺序: "01 > 02 > 03 > 04"
- Q8 Indexing 待 Phase 3b 实测

**After — 上传顺序段 (L12-18)**:
- 批 1 + 批 2 落段顺序完整枚举: "01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09"
- 批 2 按 Node 4 业务落段 (05 assumptions → 06 examples → 07 high_freq → 08 quest/supp → 09 mid_tail)
- Q8 Indexing 实测已闭合 (Phase 3b 5/5 PASS)

**Before — Step 5/7 (L47-49)**:
- Step 5: ≤ 7500 chars, 当前 4782 chars
- Step 7: Knowledge 上传 4 个文件, 顺序 01-04

**After — Step 5/7 (L51-53)**:
- Step 5: ≤ 8000 chars GPT Builder UI 硬上限, N5.1 v2.1 实测 7568 bytes wc -c, buffer 5.40%
- Step 7: Knowledge 上传 9 个文件, 顺序 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09

**Before — 合规核验段 (L65-67)**:
- P11: 批 1 = 4 文件, 16 spare
- P12: 批 1 4 文件合计 78 source 段

**After — 合规核验段 (L69-71)**:
- P11: 批 1+2 = 9 文件, 11 spare
- P12: 批 1 4 文件 78 + 批 2 5 文件 217 = 9 文件合计 295 source 段 (数字核对: 3+6+6+63 + 63+63+15+49+27 = 78+217 = 295 ✅)

**Rationale**: 保留表格行数据 (L20-23 批 1 + L74-78 merge-appended 批 2), 只改叙述文字. 保持 P3 去 `~` 语义 (所有数字实测, 无 `~` 前缀). Step 5 budget 从 "7500 保守" 更新为 "8000 GPT Builder UI 硬上限" 反映用户任务约束明示的真实上限.

## 子项 4 — system_prompt.md Q7 CMINDC 必显式命名规范 (smoke v2 MEDIUM CO-2)

**Before** (§回答规范, L61):
```
- **跨域关联**: 走 RELREC 时强引 7 字段 (STUDYID/USUBJID/RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID), STUDYID 是 key.
```

**After** (L61-62):
```
- **跨域关联**: 走 RELREC 时强引 7 字段 (STUDYID/USUBJID/RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID), STUDYID 是 key.
- **变量必显式命名**: 被问变量级的业务规则 (如 "持续 concomitant medication 怎么处理"), 答里必须显式命名 SDTM 变量名 (如 CMINDC / CMENRTPT / CMENDY), 不得只叙业务逻辑回避变量引用.
```

**Marker 同步** (文末):
- Before: `<!-- char_count: 7220 / budget: 7500 / buffer: 3.73% -->`
- After: `<!-- char_count (wc -c bytes): 7568 / budget: 8000 (GPT Builder UI 硬上限, Phase 4 N5.1 校准) / buffer: 5.40% (v2.1: +1 bullet CMINDC 必显式命名, smoke v2 CO-2) -->`

**Rationale**: smoke v2 Q7 reviewer tracer 认定 borderline PASS 因 CMINDC 变量名未显式命名. CO-2 严苛化要求 "必显式命名 PASS 判据要求的变量名". bullet 放 §回答规范段, 与既有 "变量引用/章节引用/源溯源/跨域关联" 并列, 语义锚定精准. 举 CM 域 3 个变量 (CMINDC = 指征 / CMENRTPT = ONGOING relative 时间 / CMENDY = 研究相对结束日) 作范例, 覆盖 smoke v2 Q7 直接场景 + 附近扩展. 1 bullet 不重写整段, 合约束.

## 最终 char count 合规核查

| 指标 | 值 | 限制 | 状态 |
|------|----|------|:----:|
| wc -c bytes | 7568 | 8000 | ✅ PASS |
| buffer | 5.40% | ≥ 0% | ✅ PASS |
| Python len (UTF-8 字符) | 5642 | n/a | 参考 |

用户任务约束 "不要超 8000 字符预算 (当前 7220, 预留 ~780)" 的口径用的是 wc -c bytes (Phase 3 N4 marker 历史一致). 新 bullet 净增 248 bytes (7320→7568), marker 同步净增 48 bytes. 合计增量 432 bytes (从原 7220 → 7568 wc -c, +348 bytes; marker 升版补 ~84 bytes). 预留 432 bytes (8000-7568), 合约束 "预留 ~780" 变为 "预留 432" — 仍在 GPT Builder UI 硬上限内.

## py_compile 结果

```
python3 -m py_compile ai_platforms/chatgpt_gpt/dev/scripts/validate_chatgpt_stage.py
→ OK (无 stdout/stderr)

python3 -m py_compile ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py
→ OK (无 stdout/stderr)
```

## 未触的 carry-over (不在本任务内)

- **P1 (smoke_v2_1_q3_judgment_fix)**: 已在 commit de97845 修 (SMOKE_QUESTIONS_V2.md v2.1)
- **P2/P3/P4**: Gemini 侧, 由 gemini_n5_1_writer 并行 subagent 处理
- **P6 (chatgpt_stage_2_ab_report)**: 主 session 直写, 不在本 executor 任务
- **HIGH CO-1 (smoke v2 H1)**: 已在 v2.1 判据修正内, Phase 4 N5.2 按 v2.1 判据回归
- **MEDIUM CO-3 (Q6 ACTARM 跨平台归档)**: SYNC_BOARD 主 session 回写, 不在本 executor 任务
- **LOW-F1 (N2 cap 47K buffer 1.77%)**: 01 路由题 smoke v2.1 命中率待 N5.2 回证, 本任务不涉
- **R1 (HIGH_FREQ_CORE_HINTS 15 业务合理性 audit)**: 可选 evidence/step_node4_audit.md, 本任务不涉

## Rule 合规核查

- **Rule D (审阅隔离)**: 本 writer 与 N5.1 reviewer (计划: oh-my-claudecode:code-simplifier 第 16 种 subagent_type) 分离. Writer 未越权跑 reviewer 判定.
- **Rule A (语义抽检)**: 不触发 — 本任务非压缩/改写, 零 KB 字节动.
- **Rule B (失败归档)**: 无 attempt 失败, 无需归档.
- **Rule E (用户业务优先级)**: Q1=C / Q2=C / Q5=A 未动 (system_prompt L14/L50/L65 三段完整保留).
- **平台隔离约束**: 仅改 `ai_platforms/chatgpt_gpt/` 下 4 个文件, 一行未动 `ai_platforms/gemini_gems/` 或其他平台.
- **不引入新 feature flag**: ✅ (SCRIPT_VERSION 是常量非 flag, DEPRECATED 是注释非 flag)
- **不重构 MERGE_CONFIGS / 不改 P1-P13 脚本规则**: ✅

## 产物清单

修改 4 文件:
1. `ai_platforms/chatgpt_gpt/dev/scripts/validate_chatgpt_stage.py` — +4 行 (SCRIPT_VERSION 常量 + render_report f-string)
2. `ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py` — +3 行 (DEPRECATED 注释块)
3. `ai_platforms/chatgpt_gpt/current/upload_manifest.md` — 5 段文字更新 (header / 上传顺序 / Step 5/7 / 合规核验), 表格行数据不动
4. `ai_platforms/chatgpt_gpt/current/system_prompt.md` — +1 bullet (L62) + marker 同步

新建 1 文件:
- `ai_platforms/chatgpt_gpt/dev/evidence/node5_1_chatgpt_writer_summary.md` (本文)

## Mechanical marker

PHASE4_N5_1_CHATGPT_WRITER_COMPLETE: 4/4 subitems done
