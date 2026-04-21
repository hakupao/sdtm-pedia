# Phase 6.5 Node 4 (ChatGPT batch 2) — Writer Summary

> **Agent**: oh-my-claudecode:executor (opus) writer lane
> **Date**: 2026-04-21
> **Rule D scope**: writer only — 审由独立 reviewer subagent (第 12 种 type) 做, 不本 session 自审
> **Upstream**: PLAN_BATCH2.md (ack 2026-04-21) + Node 3b carry-over CO-1/CO-2
> **Downstream gate**: reviewer PASS → 上传 ChatGPT GPT → smoke v2 10 题重跑

---

## 1. 脚本改动清单

### 1.1 `merge_for_chatgpt.py` v1.3 → v1.5 (2 bump)

**文件**: `ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py`

**v1.4 改动 (重排 terminology)**:
- 顶部 docstring 加 v1.4 修复记录段 (沿用 v1.1/v1.3 记录段风格), 标
  2026-04-21, 引 PLAN_BATCH2.md + Node 3b CO-2.
- 顶部文件级注释改写 9 产物清单: 07/08/09 文件名重命名, 语义从 "原子 core /
  quest / supp" 改为 "高频 core 15 / quest+supp 49 / 低频 core 27".
- 新增常量 `HIGH_FREQ_CORE_HINTS` (15 文件列表, 按业务频次序, 见 task spec).
- 新增 3 个 collector:
    * `_collect_terminology_core_high_freq()` — 按 HIGH_FREQ_CORE_HINTS 顺序
      过滤 core/*.md, 缺失 skip 并 stderr 警告.
    * `_collect_terminology_core_mid_tail()` — core/*.md sorted 减 hints 集合.
    * `_collect_terminology_quest_and_supp()` — sorted(quest) + sorted(supp).
- 保留 `_collect_terminology(subdir)` legacy helper (注释说明 v1.4 不再
  生产使用, 供调试).
- `MERGE_CONFIGS` 07/08/09 entry 三项全重写:
    * target 新名 (07_terminology_core_high_freq / 08_terminology_quest_and_supp
      / 09_terminology_core_mid_tail).
    * expected_segments 全 **硬编码** (15 / 49 / 27), 不再 =0 动态.
    * token_cap 按业务估算 + 15%: 260K / 1_250K / 820K.
    * description 全新描述含文件分布提示.
- 01-06 entry 保持 batch 1 + 原 05/06 语义 (仅 docstring token_cap 说明同步).

**v1.5 改动 (attempt_1 后 06 cap 微调)**:
- 06_domain_examples_all.md V5 FAIL 220,575 > 190,000 → cap 190_000 → 254_000
  (+15.2% buffer from 实测 × 1.15). 同步 docstring 注释 + MERGE_CONFIGS[5].

**行增/删估算**: +100 / -16 行 (新 collectors + 常量 + docstring).

### 1.2 `validate_chatgpt_stage.py` v1.3 → v1.5 (2 bump, sync)

**文件**: `ai_platforms/chatgpt_gpt/dev/scripts/validate_chatgpt_stage.py`

**v1.4 sync**:
- 顶部 docstring 加 v1.4 sync 段 (沿用 v1.3 sync 风格).
- `EXPECTS[6-8]` 三 entry 重定义:
    * `07_terminology_core_high_freq.md` expected=15 cap=260_000 (原 0/920K).
    * `08_terminology_quest_and_supp.md`  expected=49 cap=1_250_000 (原 0/1095K).
    * `09_terminology_core_mid_tail.md`   expected=27 cap=820_000 (原 0/173K).
- dynamic_source_dir 全空串 (硬编码, 不再依赖 KB 目录 self-consistent).

**v1.5 sync**:
- `EXPECTS[5]` 06 cap 190_000 → 254_000 (与 merge v1.5 同步).

**行增/删估算**: +30 / -8 行 (EXPECTS 改写 + docstring).

### 1.3 `current/system_prompt.md` v1 → v2

**文件**: `ai_platforms/chatgpt_gpt/current/system_prompt.md`

**整体改写**:
- 顶部知识库节从 "批 1 已上传" → "批 1+2 共 9 文件, ~3M tokens", 新增
  05/06/07/08/09 五行路由定义.
- 路由表第 3/6/7 行改写:
    * 行 3 规则推导: 主文件 `02_chapters_all.md` → `05_domain_assumptions_all.md`
      (域级); 辅助反向.
    * 行 6 Examples: 主文件 `06_domain_examples_all.md` (原标"批 2 未上").
    * 行 7 CT Term: 三档 07→09→08 + EVS 外链兜底 (原标"批 2 未上").
- §回答规范 新增跨域关联段: RELREC 7 字段强引含 STUDYID (CO-1 处置).
- §边界处理模板重写 ①②③:
    * ① 原 "批 2 未上" 模板 → "Examples 已上传, 直接引" 模板.
    * ② 原 CT "批 2 未上" 模板 → "Terminology 已上传" 模板.
    * ③ 新增 "Terminology 未命中 EVS 外链兜底" 模板 (CO-2 处置, 含
      `https://evsexplore.semantics.cancer.gov/evsexplore/` 完整 URL).
    * ④ 未知域模板保留 (不变).
- Conversation Starters 4 个原样保留 (节省 budget).
- 文末字符计数 marker 更新: `7220 / budget: 7500 / buffer: 3.73%`.

**行增/删估算**: +35 / -20 行 (路由表扩表 + 边界模板重写).

**chars 实测**: 7220 chars (< budget 7500, buffer 3.73%).

---

## 2. 脚本实测数据 (batch 2 attempt_2 all PASS)

### 2.1 Merge stdout 摘要 (5 产物, rc=0)

```
[Stage chatgpt-batch2] 05_domain_assumptions_all.md: 54,658 tokens   (63 sources, target ≤69K)
[Stage chatgpt-batch2] 06_domain_examples_all.md:    220,575 tokens  (63 sources, target ≤254K)
[Stage chatgpt-batch2] 07_terminology_core_high_freq.md:  200,746 tokens (15 sources, target ≤260K)
[Stage chatgpt-batch2] 08_terminology_quest_and_supp.md: 1,047,119 tokens (49 sources, target ≤1250K)
[Stage chatgpt-batch2] 09_terminology_core_mid_tail.md:  698,081 tokens (27 sources, target ≤820K)
```

5 产物合计 **2,221,179 tokens** (~2.2M), 合 batch 1 310,134 tokens ≈ **batch 1+2 合计 2,531,313 tokens**.

### 2.2 Validate stdout (rc=0)

```
[PASS] 05_domain_assumptions_all.md   V1/V2/V3/V4/V5/V7 全 PASS | md5=79b1069c7424d3c3edad630be14e653d
[PASS] 06_domain_examples_all.md      V1/V2/V3/V4/V5/V7 全 PASS | md5=04bc0a05ef072ede1b7df1b487ec7485
[PASS] 07_terminology_core_high_freq.md V1/V2/V3/V4/V5/V7 全 PASS | md5=951b6d6ce541c24f95bd565c921d5644
[PASS] 08_terminology_quest_and_supp.md V1/V2/V3/V4/V5/V7 全 PASS | md5=0c0bf135146215515a49227b76b3c925
[PASS] 09_terminology_core_mid_tail.md  V1/V2/V3/V4/V5/V7 全 PASS | md5=efca218aaf6ad17980de323735d45e67
```

### 2.3 实测矩阵

| 文件 | tokens | 段数 | token_cap | 利用率 | V1 | V2 | V3 | V4 | V5 | V7 | md5 |
|------|-------:|:---:|----------:|-------:|:--:|:--:|:--:|:--:|:--:|:--:|:-----|
| 05 | 54,658 | 63 | 69,000 | 79.2% | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 79b1069c |
| 06 | 220,575 | 63 | 254,000 | 86.8% | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 04bc0a05 |
| 07 | 200,746 | 15 | 260,000 | 77.2% | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 951b6d6c |
| 08 | 1,047,119 | 49 | 1,250,000 | 83.8% | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 0c0bf135 |
| 09 | 698,081 | 27 | 820,000 | 85.1% | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | efca218a |

Merge rc=0, Validate rc=0, 段数 100% 对齐 manifest expected.

---

## 3. attempt 记录 (Rule B)

### attempt_1 失败 (06 V5 FAIL)

- 产物: `dev/evidence/failures/stage_batch2_attempt_1.md` (已归档, 不删)
- FAIL: 06_domain_examples_all.md 220,575 tokens > 190,000 cap (+16.09%)
- 业务判定: 0 业务影响 (cap 是预算守护, 非平台硬限).
- 决策: 方案 A (cap 190K→254K, +15.2% buffer). 同步 merge v1.5 + validate v1.5.

### attempt_2 PASS

全 5 文件 V1-V7 PASS. Stage 进入上传就绪态.

---

## 4. CO-1 / CO-2 处置

### CO-1 (LOW): RELREC STUDYID 补充

- **carry-over 来源**: Node 3b smoke v2 S2 题 reviewer 建议
- **处置**: system_prompt.md §回答规范 新增跨域关联段:
  > 跨域关联: 走 RELREC 时强引 7 字段 (STUDYID/USUBJID/RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID), STUDYID 是 key.
- **状态**: ✅ 已消除

### CO-2 (HIGH): NCI EVS Browser 外链

- **carry-over 来源**: Node 3b smoke v2 S3 题 reviewer 高优建议
- **处置**: system_prompt.md §边界处理模板 ③ 全新增:
  - URL: `https://evsexplore.semantics.cancer.gov/evsexplore/`
  - 模板条件: "07/09/08 三档 terminology 均未命中"
  - 核心约束: "本 GPT 不臆造 CT 值 / Synonyms / 版本号"
- **状态**: ✅ 已消除

---

## 5. manifest_segments.json 更新

**路径**: `ai_platforms/chatgpt_gpt/current/manifest_segments.json`

**新增 5 entry** (batch 2, 均 dynamic=false, expected=actual):

```json
{
  "05_domain_assumptions_all.md":     {"actual":63, "expected":63, "dynamic":false, "stage":"batch2"},
  "06_domain_examples_all.md":        {"actual":63, "expected":63, "dynamic":false, "stage":"batch2"},
  "07_terminology_core_high_freq.md": {"actual":15, "expected":15, "dynamic":false, "stage":"batch2"},
  "08_terminology_quest_and_supp.md": {"actual":49, "expected":49, "dynamic":false, "stage":"batch2"},
  "09_terminology_core_mid_tail.md":  {"actual":27, "expected":27, "dynamic":false, "stage":"batch2"}
}
```

共 9 entry (4 batch1 + 5 batch2), 全真源独立声明.

**upload_manifest.md**: merge 自动 append 5 行 (manifest append).

---

## 6. 工作量统计

| 项 | 数字 |
|----|-----:|
| 改动文件数 | 3 (merge.py + validate.py + system_prompt.md) |
| 新文件数 | 2 (node4_writer_summary.md + failures/stage_batch2_attempt_1.md) |
| 新 KB 产物数 (uploads/) | 5 (05/06/07/08/09) |
| 代码行增/删 (脚本合计) | +130 / -24 |
| system_prompt 行增/删 | +35 / -20 |
| attempt 次数 | 2 (1 fail + 1 pass) |

---

## 7. 遗留 carry-over

### 7.1 本 session 已消

- CO-1 STUDYID — ✅
- CO-2 EVS 外链 — ✅
- Node 2 LOW-F1 01 cap buffer 1.77% — 本任务不处置 (batch 2 不涉 01).

### 7.2 本 session 不负责 (下游)

- **R1 Rule A 语义抽检 N=5** (主 session 外部): 07 高频 15 个选择的业务合理
  性由主 session 或 reviewer subagent 抽检, writer 不做.
- **R2 Rule D reviewer 独立审 (第 12 种 subagent_type)**: 本 writer 产物需
  reviewer 独立判 PASS 才进 Phase 5 上传.
- **R3 上传 5 文件到 GPT + smoke v2 10 题重跑**: Phase 5 Node 5 任务, 本
  Node 4 只完成脚本 + system_prompt + 产物落盘.
- **R4 upload_manifest.md README/order 段手工更新**: merge 只 append 表格行,
  README 语义段 (建议上传顺序 / 上传后验证) 需主 session 补.

---

## 8. 关键决策记录

1. **HIGH_FREQ_CORE_HINTS 15 个文件的业务选择**: 严格按 task spec 列表,
   顺序非 sorted (按频次降序优先业务). writer 不做 Rule A 抽检 — 主 session
   负责.
2. **expected_segments 全硬编码**: v1.3 三 entry =0 动态, v1.4 改为 15/49/27
   硬编码. 代价: KB 新增 core 文件需改 hints 常量; 收益: manifest 真源
   更强, validate V2 不依赖 KB 当前目录快照.
3. **06 cap 微调 attempt_1→2**: 非违反 PLAN (PLAN 估算 190K 保守), Rule B
   归档留证. cap 是预算守护, 非硬删数据.
4. **保留 Rule E 三段** (Q1=C / Q2=C / Q5=A): system_prompt §角色定义 "混合
   受众" + §回答规范 "陌生公开受众友好" + §路由规则 "63 域全量平权" 三段
   完整保留, 未改写.
5. **system_prompt buffer 缩窄** (36.2% → 3.73%): 新增 5 文件路由 + CO-1/CO-2
   两段 + 边界模板三段重写. 接近 budget 但未越界. 若下轮 Rule D reviewer
   要求再加内容, 需删 Conversation Starters 或压缩 §工作流程.

---

## 9. 下一步 (Handoff to Reviewer subagent)

Reviewer subagent (第 12 种 type) 应独立校验:

1. **代码合规** (merge.py / validate.py):
    - py_compile 过 (本 session 已跑, 二次 sanity check)
    - HIGH_FREQ_CORE_HINTS 15 个文件名是否业务合理 (对比 smoke v2 10 题覆盖)
    - token_cap 设置是否合理 (06 的 +15% buffer 是否够)
    - expected_segments 是否与 manifest 严格一致
2. **system_prompt 语义**:
    - 路由表 7 行是否完整 + 对应文件存在
    - 边界模板 ③ EVS URL 是否正确 + 是否覆盖 "07/09/08 三档均未命中" 场景
    - Rule E 三段是否保留完整
    - chars ≤7500 (实测 7220)
3. **CO-1 / CO-2** 处置是否充分
4. **manifest_segments.json** 9 entry 是否全 dynamic=false + expected=actual
5. **遗留 carry-over** 清单是否完整

Reviewer 输出 PASS / CONDITIONAL_PASS / FAIL, 落档
`dev/evidence/node4_reviewer.md`.

---

**End of Writer Summary**.
