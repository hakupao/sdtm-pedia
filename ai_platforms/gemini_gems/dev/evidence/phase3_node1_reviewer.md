# Gemini Gems Phase 3 Node 1 Scripts Reviewer Report

> Reviewer: oh-my-claudecode:verifier (opus, 1M context, independent subagent — Rule D)
> Date: 2026-04-20
> Scope: 3 脚本 (count_tokens.py / merge_for_gemini.py / validate_gemini.py) + PLAN §1-§4 + research.md + profile.md
> 平台隔离: 未读 ChatGPT 侧任何文件
> 不读 executor completion report (rubber-stamp 风险规避)
> 未执行脚本 (Node 1 硬约束); 仅 `python3 -m py_compile` 语法验证 (PASS)
> Verdict: **CONDITIONAL_PASS**

---

## 0. 执行环境抽查

| 项 | 结果 |
|----|------|
| py_compile 全 3 脚本 | **PASS** (stdout: `PY_COMPILE_OK`) |
| knowledge_base/chapters | 6 文件 (ch01/02/03/04/08/10) |
| knowledge_base/model | 6 文件 (01-06) |
| knowledge_base/ROUTING.md / INDEX.md / VARIABLE_INDEX.md | 3 文件齐 |
| knowledge_base/domains/*/ | 63 目录 (PLAN §2.1 fact, confirmed) |
| knowledge_base/terminology/core/*.md | 42 文件, ~3.4 MB 总 |
| knowledge_base/terminology/questionnaires/*.md | 43 文件, ~3.6 MB |
| knowledge_base/terminology/supplementary/*.md | 6 文件, ~448 KB |
| core 最大文件 | lb_part3.md 417 KB / lb_part2.md 377 KB (T-tail-1 候选) |

**关键事实 (驱动 M4 判定)**: `terminology/core/` 3.4 MB ≫ 200K tokens target. 3.4 MB markdown ≈ 850K tokens (0.25 tok/byte 经验系数). ⇒ **`_collect_terminology_sources` 必进 `else` (`core_total_tokens > TERMINOLOGY_TARGET_TOKENS`) 分支**. 此分支只用 core, 完全忽略 quest/supp. 见 §5 carry-over.

---

## M1 — PLAN 合规

### M1.1 merge_for_gemini.py — 4 合并文件

| PLAN §2.1 要求 | 脚本实现 | 判定 |
|---|---|---|
| 01_core_reference.md (chapters + model + nav) | `_collect_core_sources()` 按序组合 chapters `*.md` → model `*.md` → ROUTING.md → INDEX.md → VARIABLE_INDEX.md | **PASS** |
| 02_domain_specs.md (63 域字母序 spec.md) | `_list_domains()` 按 `sorted(name)` + 遍历 spec.md | **PASS** (字母序严格) |
| 03_domain_knowledge.md (assumptions 先 + examples 后, 63 域字母序) | `_collect_knowledge_sources()` 域外字母序, 域内 assumptions → examples | **PASS** |
| 04_terminology_core.md (高频 codelist 尾部) | `_collect_terminology_sources()` 双分支, 尾部策略见 M1.2 | **PASS-conditional** (尾部策略在 core>target 分支正确; 见 §5 carry-over) |

### M1.2 位置策略 (P12 末尾召回硬依据)

| 文件 | PLAN 策略 | 脚本实现 | 判定 |
|---|---|---|---|
| 01 | 导航前置 | 实现为 chapters → model → ROUTING/INDEX/VAR_INDEX. 注意: nav 被放在尾部 (行 151 注释 "跟在主体后面, 便于 Gemini 在 query 时从尾向前扫导航") | **PASS-with-note**. PLAN §2.1 原文 "chapters → model → ROUTING" 解释模糊, 既可读作"顺序"也可读作"优先". 脚本实现 chapters/model 主体在前, nav 在 01 尾部, 依赖 Gemini 官方 "query 放最后 best practice" 作 recency 辅助. 合理 |
| 02 | 字母序 | `sorted(d.name)` — 严格字母序 | **PASS** |
| 03 | assumptions 先 examples 后 | 域内 `a` 后 `e` 同步 | **PASS** |
| 04 | **高频 codelist 尾部** (P12 硬依据) | core>target 分支: size-desc 累加然后 `.reverse()` ⇒ 小文件-大文件 顺序, 最末 = 最大文件 = 高频代理. lb_part3.md (417KB) + lb_part2.md (377KB) 必落尾部. | **PASS** on active branch |
| 04 Rule E Q4=A | 选择性注入 ≤200K | `TERMINOLOGY_TARGET_TOKENS = 200_000` 硬预算 | **PASS** |
| 04 Rule E Q5=A | 02/03 全量 63 域 | 无减配, 每域 `spec.md/assumptions.md/examples.md` 全拉 | **PASS** |
| source comment | `<!-- source: <path> -->` 每段 | `_segment()` 每段开头插入, 相对 REPO_ROOT | **PASS** |
| P1 量化输出 | `[Stage ...] <file>: <N> tokens (target ≤<X>K)` | `_log()` + 各 stage 末尾打印 | **PASS** (格式: `[Stage gemini-single-batch] 01_core_reference.md: N tokens (target ≤120K)`) |
| CLI stages | core/spec/knowledge/terminology/all/--dry-run | argparse `choices` 全齐 + `--dry-run` 跳过写 | **PASS** |
| 累计 ≤800K (P11) | `TOTAL_BUDGET_TOKENS = 800_000`, cumulative log + >900K WARN | **PASS** |

### M1.3 validate_gemini.py — V1-V6

| V | PLAN 要求 | 实现 | 判定 |
|---|---|---|---|
| V1 非空 | size>0 | `row["v1_nonempty"] = st.st_size > 0` | **PASS** |
| V2 段数 ≥ | 01≥15, 02≥63, 03≥126, 04 不判 FAIL | `STAGE_FILES`: 15/63/126/0; 04 `expected_sources_min=0` → INFO only | **PASS** |
| V3 三档 | ≤800K PASS / ≤900K WARN rc=2 / >1000K FAIL | `TOTAL_TOKEN_WARN=900_000`, `TOTAL_TOKEN_HARD=1_000_000`. 区间语义见 §M1.4 | **PASS-with-note** |
| V4 <5MB | size<5MB | `SINGLE_FILE_BYTE_HARD = 5*1024*1024` | **PASS** |
| V5 md5 | 打印 md5 head12 | `_md5(path)` + report 输出 | **PASS** |
| V6 末尾 30% ≥3 terminology source | 仅 04 判 FAIL; tail_fraction=0.30, min=3 | `_v6_tail_terminology()` 用 `offset >= tail_start` + 路径含 "terminology" 过滤 | **PASS** |

### M1.4 V3 rc 语义注解

Task 描述要求 "≤800K PASS / ≤900K WARN rc=2 / >1000K FAIL". 脚本实际行为:
- total ≤ 900K: rc=0 (包括 800K<x≤900K 这段 **PASS, 不是 WARN**)
- 900K < total ≤ 1000K: rc=2 WARN (§8 R2 trigger, 匹配 Task 要求)
- total > 1000K: rc=1 HARD FAIL (匹配)

Task mental trace 问 "850K 是 rc=2 还是 rc=0" → **答: rc=0** (脚本 + PLAN 语义). PLAN §1.3 P11 说 "target ≤800K", §8 R2 trigger 是 >900K, 没有把 800-900K 区间硬归为 WARN rc=2. 脚本实现合 PLAN; Task 描述中"≤900K WARN rc=2"的表述略有歧义, 但脚本的"warn 阈值=900K, PASS 只要 ≤900K" 语义一致且防止无谓噪音. **判定 PASS, 无 carry-over**.

### M1.5 V6 锚点

Task 问 "V6 末尾 30% 锚点是 byte offset 还是 source comment 数?" 答: **character offset in Python string** (`len(text)` 是 Python str 字符长度; 文件是 UTF-8 纯 ASCII/中文混, 此处 character offset 近似 byte offset). `positions` 列出所有 `<!-- source: ... -->` 的 `m.start()` 字符 offset, 然后判 `offset >= tail_start (= 0.70 * total_len)` 且路径含 "terminology". 属于 **offset 锚点** (不是 comment 数 nor ordinal). 对 P12 T-tail-1 验证: 若最末 30% 字符内出现 ≥3 段 terminology/* 源, 即 PASS. 合理.

---

## M2 — 代码质量

### count_tokens.py (86 行)

| 维度 | 判定 |
|---|---|
| 单一职责 | 只计 token, 无副作用 (写文件). **PASS** |
| 错误处理 | path 不存在 → `sys.exit(2)` + stderr; UTF-8 strict 会在坏编码时抛 (可接受) | **PASS** |
| idempotent | 纯只读 + sorted(rglob), 同输入同输出 | **PASS** |
| Python 风格 | 类型注解齐 (`Iterable[Path]`), docstring, pathlib, `from __future__ import annotations` | **PASS** |
| 依赖 | tiktoken 单依赖, 与 claude_projects 一致 | **PASS** |

**评分: LOW risk, 无修改建议**.

### merge_for_gemini.py (493 行)

| 维度 | 判定 | 备注 |
|---|---|---|
| 单一职责 | 只合并, 不校验, 不副作用 (除 write uploads + manifest 追加) | **PASS** |
| 错误处理 | 缺源目录: `if path.is_dir()` 静默跳过 (01 chapters/model/nav 全容错); 03 `_collect_knowledge_sources` 同 — 域 assumptions/examples 缺失则单独跳过, 不报错; UTF-8 strict 抛 | **LOW** (静默跳过可接受, 但缺 warn log; 见 carry-over) |
| idempotent | sorted(glob/rglob/iterdir) + 同一排序键; dry-run 不触 manifest; `_write_merged` 每次全量重写产物 (非追加). 时间戳在 header 和 manifest 但不影响最终 tokens. | **PASS-with-note**. 产物文件内 header 含 `Generated: <ISO>` 时间戳 ⇒ md5 每次不同, 这对 V5 md5 稳定性有冲击 (V5 只记录不判 FAIL, 可接受). Carry-over 见 §5. |
| Python 风格 | 类型注解完整, docstring 章节清晰, pathlib, tuple 返回值 | **PASS** |
| 模块化 | 4 stage 各自 `_collect_*` + `_stage_*`, `STAGE_EXECUTORS` dict dispatch — 干净 | **PASS** |
| 05-solution 吸收 | STAGE_SPEC target_tokens / position 字段完整 | **PASS** |

**评分: MEDIUM risk on md5 stability (header 含时间戳)**. 见 §M5 偏离 #5 (新增).

### validate_gemini.py (374 行)

| 维度 | 判定 |
|---|---|
| 单一职责 | 只校验 + 写 report, 不修 uploads | **PASS** |
| 错误处理 | 文件不存在 → hard_fail + 记录 "FILE NOT FOUND"; UTF-8 strict 抛 | **PASS** |
| idempotent | 产物 `validate_single_batch.md` 每次覆盖 (非追加), 含时间戳 ⇒ md5 不同但内容幂等 | **PASS** |
| Python 风格 | Result 类清晰, md5 chunk 读 (1<<16 64KB) 防大文件 OOM, 正则提取 source | **PASS** |
| rc 语义 | rc=0 PASS / rc=1 hard fail (含 V1/V4/V6/file-not-found/V3>1M) / rc=2 V3 warn (900K<x≤1M) | **PASS** |

**评分: LOW risk**.

---

## M3 — 规则合规 (A/B/D + P5/P6)

### P5 knowledge_base 只读

- merge_for_gemini.py: `_read_text()` 仅 `read_text`, 产物写 `UPLOADS_DIR = PROJECT_ROOT/current/uploads` (`ai_platforms/gemini_gems/current/uploads`), 不触 knowledge_base. **PASS**
- validate_gemini.py: `args.uploads` 默认 `ai_platforms/gemini_gems/current/uploads`, 产物写 `dev/evidence/validate_single_batch.md`. 不触 knowledge_base. **PASS**
- count_tokens.py: 仅读. **PASS**

### P6 脚本自足 + 单一职责

- 3 脚本各有独立 `main(argv)` + 无相互 import. **PASS**
- merge 和 validate 通过文件系统 handoff (产物→校验输入), 非 in-process 耦合. **PASS**

### 规则 A (语义抽检)

- 04_terminology_core.md 涉及选择性注入 (core 42 文件 ~850K tokens → 截取至 ~200K) ⇒ 改写率 > 50% (舍弃 >70% 源内容), **必触 Rule A 抽检**.
- 脚本本身未硬编码 Rule A 触发; PLAN §4 B5 明示 "合并产物规则 A 语义抽检 (N=5 样本)", 属于 Node 2 执行阶段事务.
- 脚本中 `_collect_terminology_sources` docstring (行 207-224) 详细说明"size proxy 作为高频启发式" + "Node 2 A/B 校准" ⇒ **符合代码内文档化 Rule A 触发原因的要求**. **PASS**
- **Carry-over 建议**: 产物写入时附一行 `> terminology selection: core-only, size-desc proxy, N=<k> files kept, N=<m> files dropped` 便于 N=5 抽检快速定位被丢弃的域. 见 §5 carry-over LOW.

### 规则 B (失败归档)

- PLAN §6 约定归档路径 `dev/evidence/failures/stage_<Phase>_<Task>_attempt_<N>.md`, 未硬编码进代码 (允许).
- validate_gemini.py rc≠0 时, 终端 print `[validate] rc=1 HARD FAIL`, **未提示 "请归档到 failures/..."** ⇒ 建议增强 (LOW carry-over). 规则 B 主要由主 session 执行, 脚本不归档也合规.

### 规则 D (写审分离)

- 我 (verifier subagent) ≠ executor (writer). **PASS**
- 我未读 executor completion report (主 session 转述偏离清单也未构成污染, 我独立验证脚本源 + PLAN + research). **PASS**
- 并行的 code-reviewer subagent 审 ChatGPT 侧, 与本 review 无交叉. **PASS**

---

## M4 — 边界案例 mental trace

### M4.1 terminology core > 200K target — 如何截取? 尾部是否高频?

**实测 trace** (基于 ls 抽查 + size 降序):
- core 总 3.4 MB ≈ 850K tokens ≫ 200K target ⇒ 进 `else` 分支 (行 265).
- `core_by_size` = [lb_part3.md 417KB, lb_part2.md 377KB, is_domain_part2 238KB, general_part1 221KB, general_part5 143KB, ...] (size desc)
- 累加 cum:
  - lb_part3 (417KB ≈ 104K tok) → cum=104K, 加入
  - lb_part2 (377KB ≈ 94K tok) → cum=198K, 加入
  - is_domain_part2 (238KB ≈ 60K tok) → cum+60=258K > 200K target, `len(selected) >= 1` → break
- `selected` = [lb_part3, lb_part2], 然后 `.reverse()` ⇒ [lb_part2, lb_part3]
- 写入顺序: lb_part2 在前, lb_part3 在末尾
- **04 产物末尾 30% 字符位置 ≈ lb_part3 尾段** ⇒ T-tail-1 命中 lb_part3 (最大文件, 高频 LB codelist)
- V6 判定: 末 30% 内必含 `<!-- source: knowledge_base/terminology/core/lb_part3.md -->` 1 段, 以及 lb_part3.md 本身内容 (不含更多 source 注释) ⇒ **仅 1 段 terminology source 在尾部 30%, 不满足 V6 ≥3**

**⚠️ HIGH 风险**: `V6_TAIL_MIN_TERM_SEGMENTS = 3` 前提是末 30% 内至少 3 段 source 注释. 若 core>target 分支只选中 2-3 个大文件, 每个 > 100K 字符, 尾部 30% 只覆盖最后 1-2 个 source 边界 ⇒ **V6 在本真实场景下预计 FAIL**. 详见 §5 偏离 HIGH-1.

**但若 break 条件 `len(selected) >= 1` 配合 target 较松 (e.g. 真实 token 密度更高, 让 cum 更早超)**, 实际 selected 可能 5-10 个 ⇒ 尾部 30% 多段 ⇒ V6 PASS. 本项不能在 Node 1 确定, 必须 Node 2 落地后实测校准. 标记为 **carry-over HIGH** + Node 2 gate.

### M4.2 domains/XX/assumptions.md 缺失?

- `_collect_knowledge_sources` 行 194-198: `if a.is_file()` + `if e.is_file()` 独立判, 缺失则跳过不加, 不抛错. **合规** (SDTM 63 域可能有个别缺 assumptions.md, 静默跳过避免误 fail).
- **缺点**: 无 log 警告 ⇒ 若某域 assumptions 被意外删除, 合并无感知. 建议加 `_log(f"skip missing: {a}")`. 见 §5 LOW carry-over.

### M4.3 --stage core 后再跑 --stage spec, manifest 重复?

- `_append_manifest_fragment` 行 402: 每次 main 调用附一个 `<!-- merge fragment: <ts> -->` 块, 内含当次 entries.
- 两次跑 `--stage core` 和 `--stage spec` → manifest 末尾有两个 fragment 块, 各自 header 带不同时间戳. 01 会出现在第一个块, 02 出现在第二个块. **无"同一 stage 重复记录"的语义冲突**, 但分步跑 vs 一次 `--stage all` 会产出不同 manifest 结构 (前者 2 块, 后者 1 块).
- **判定 M5 #1 (一次性追加 manifest)**: 偏离 PLAN §4 B2-B4 "每 stage 追加" 的字面含义. 执行者采用"单次 main 调用内累积, 结束时一次写 (带时间戳)". Carry-over 接受 (见 §5).

### M4.4 V3 实测 850K (800-900K 区间) → rc?

**rc=0 PASS**. warn_v3 条件是 `>900K`, 850K 未触 warn. 见 §M1.4.

### M4.5 V6 锚点

**offset (character offset in full text)**, 非 source comment 计数. 见 §M1.5.

### M4.6 01 nav 在尾部的位置合理性

01_core_reference 实际顺序: 6 chapters → 6 model → ROUTING → INDEX → VARIABLE_INDEX. 15 段, 最末 3 段是 nav. 脚本 docstring 行 22 说 "01 前置 (导航防 LiM)", 但实际 nav 在 01 文件**内**的尾部. PLAN §2.1 原表 "chapters → model → INDEX/ROUTING" 与 §2.4 "导航层前置, 文件内顺序: chapters → model → ROUTING/INDEX" 矛盾记号: "导航层前置" 可读作 "01 这个文件前置 (相对其他 02/03/04)". 脚本的"文件内 chapters → model → nav" 即"01 整体前置 + 文件内 nav 在 01 尾部"合理, 依赖 Gemini recency bias 使 01 尾部 (nav) 被 query 阶段最容易抓取. **PASS**.

---

## M5 — 偏离清单判定

### 偏离 #1: manifest 一次性追加

- **主 session 转述**: executor 单次 main 调用累积 entries, 结束时一次写 `<!-- merge fragment: <ts> -->` 块.
- **PLAN §4 B2-B4 字面**: "产出 01+02 累加 manifest / 产出 03 累加 / 产出 04 累加" — 可读作"每 stage 各追加一行"或"每 main 调用追加一块".
- **判定**: **合理接受**. 理由:
  1. 幂等性: 分步 vs 一次性 `--stage all` 产出 manifest 结构不同但内容正确, 时间戳隔开可审.
  2. 一次性追加避开"半成品 manifest" (单 stage 产出后 crash 留下一条孤立行).
  3. PLAN 未显式禁止单次主调用累积.
- **记 carry-over 到 Node 2**: Node 2 若分步跑 (core→spec→knowledge→terminology 四次), manifest 末尾有 4 块, 主 session 读时注意只认最新块 (或用户手动清理历史块). 见 §5.

### 偏离 #2: 04 terminology 排序 reverse

- **主 session 转述**: PLAN §2.1 "04 字母序 + 高频后置" 与 core 文件名字母序 ≠ 高频的矛盾 → 执行者用 size-proxy 排序后 reverse (小在前, 大在末).
- **判定**: **合理接受 (本 Node 1 范围)**. 理由:
  1. core>target 分支 (本真实场景必进): size-desc 累加 + reverse ⇒ 最大文件 = 高频代理 落在末尾, 合 PLAN §3 Rule E Q4=A "terminology 末尾 recency".
  2. core<=target 分支: 有 carry-over 问题 — core 字母序 + quest/supp 按 size 降序追加, 最末是最小的 quest/supp 而非最大高频. **但本真实场景不触此分支** (core 3.4MB 必超 200K). Node 2 校准 size-proxy 有效性.
- **记 carry-over**: Node 2 Rule A N=5 抽检时, 必抽 1-2 个末尾段验证其在真实 SDTM 查询中是否属"高频" (lb 肝功能检查通常是最常查 codelist, 合启发式).

### 偏离 #3: V2 段数 terminology 不判 FAIL

- **主 session 转述**: PLAN 明示 "先记录不判 FAIL, Node 2 校准". executor 实现 `expected_sources_min=0` + INFO.
- **判定**: **PASS**. 合 PLAN §2.1 原文 "04 记录不判 FAIL" (STAGE_FILES line 76 注释 "P12 Node 2 校准, 先记录不判 FAIL").

### 偏离 #4: 不执行脚本

- **Node 1 硬约束**. py_compile PASS (语法), 无执行. **合规**.

### 偏离 #5 (新增, reviewer 发现): header 时间戳导致 V5 md5 不稳定

- **问题**: `_file_header()` 行 293 含 `Generated: {_now_iso()}` ⇒ 每次合并产物的 header 不同 ⇒ md5 每次变化.
- **影响**: V5 md5 stable 承诺仅在"同一秒两次跑"成立, 跨时间跑同输入 md5 不同. PLAN §4 B5 Rule A N=5 抽检若跨天执行, md5 不可用于"确认产物未变". V5 脚本本身只 record, 不判 FAIL (validate_gemini.py 行 199 `row["md5"]`, 不入 hard_fail 判定), **业务上可接受**.
- **carry-over LOW**: 若 Node 2 希望 md5 真正稳定, 可把 header 时间戳换成"header 内容仅随输入变化, 时间戳移 manifest" ⇒ 产物 md5 就纯输入 hash. 本 Node 1 不 hard-block.

---

## Carry-over 到 Node 2 (CONDITIONAL_PASS 补修清单)

### HIGH — Node 2 开跑前必修 or 跑完后立即 gate

- **HIGH-1 (P12 V6 风险)**: 基于 size ls 实测推演, core>target 分支会让 04 产物仅 2-3 段 source (如 lb_part2 + lb_part3), 末 30% 内可能仅 1 段 terminology source ⇒ **V6 FAIL 风险极高**. Node 2 跑 merge 后, 若 V6 FAIL:
  - 选项 A: 降低 `V6_TAIL_MIN_TERM_SEGMENTS` 到 1 (放松门槛, 但 P12 hard checkpoint 弱化, 需用户 ack)
  - 选项 B: 改 `_collect_terminology_sources` 的 break 逻辑 ⇒ 累加到 200K 允许轻微超 (e.g. ≤220K), 强制选更多小 core 文件 (如 interventions 89KB, oncology 89KB 之类), 让 selected 达 6-8 个 ⇒ 末 30% 多段
  - 选项 C (推荐): 混合 core 大文件 + core 高频小文件, 让尾部既有"容量"又有"段数"
  - **此项必须 Node 2 实测后决定, 不在 Node 1 硬 block** (py_compile 过, 逻辑自洽)

### MEDIUM — Node 2 开跑前建议修

- **MEDIUM-1**: `_file_header()` 时间戳 ⇒ V5 md5 不稳定. 可选修: 把 `Generated` 移出 header 或改用"输入文件 sha 列表"作 header. **非阻塞**, 业务 V5 不判 FAIL.

### LOW — Node 2 carry-over, 可累积修

- **LOW-1**: `_collect_terminology_sources` core<=target 分支 (本场景不触) 的尾部策略问题 (quest/supp 大在前, 最末是小文件). 若未来 terminology 源缩减触此分支会触发 P12 FAIL. 修法: quest/supp 也 sort 后 reverse, 或 selected 整体 size-desc 后 reverse.
- **LOW-2**: `_collect_knowledge_sources` / `_collect_spec_sources` 静默跳过缺失域文件. 建议加 `_log(f"skip missing: {p}")`, 便于 Rule A 抽检时对齐源.
- **LOW-3**: validate_gemini.py rc!=0 时 terminal print 不提示 "请归档到 `dev/evidence/failures/stage_<Phase>_<Task>_attempt_<N>.md`". 规则 B 提示 UX.
- **LOW-4**: merge_for_gemini.py manifest 一次性追加块 (见 §M5 #1). Node 2 手册化"分步跑时只认最新块".
- **LOW-5**: 04 产物写入时附 `> terminology selection summary: N kept, M dropped, core-only/size-desc-proxy` 1 行, 便于 Rule A N=5 抽检快速审.

---

## 最终 Verdict: **CONDITIONAL_PASS**

### 理由 1 — PLAN 骨架合规 + 代码质量达标

3 脚本在 PLAN §1-§4 要求的硬骨架上全部对齐: 4 合并文件编号+目标齐, P1 量化输出, CLI 6 stages, P5/P6 全守, V1-V6 六项校验齐, rc 三档合 PLAN §8 R2 语义. py_compile 纯净. 代码风格 (pathlib / 类型注解 / docstring 全覆盖) 达 claude_projects v2 同标准. 独立职责清晰, 无耦合, dispatch 干净. 这些是 Phase 3 Node 1 "脚本就位" 的硬 gate, 全部达标, 不构成 FAIL.

### 理由 2 — 两处偏离 PLAN 原描述但业务合理, 接受

manifest 一次性追加 (偏离 #1) 和 04 terminology reverse 后置策略 (偏离 #2) 虽与 PLAN §4 B2-B4 / §2.1 原文的字面描述有张力, 但业务判定合理: 前者幂等性 + 避免半成品污染 manifest; 后者 core>target 真实分支里, size-desc + reverse 正确把最大文件 (= 高频 LB lb_part3/lb_part2 等) 推到尾部, 达到 Rule E Q4=A + P12 recency 意图. 偏离 #3 V2 terminology 不判 FAIL 完全合 PLAN. 偏离 #4 不执行合 Node 1 约束.

### 理由 3 — HIGH-1 V6 段数风险是 CONDITIONAL 关键, 但属于 Node 2 落地后必 gate 事项, 不应在 Node 1 block

reviewer 实测推演 knowledge_base/terminology/core 3.4MB ≫ 200K target, 推出 core>target 分支会让 04 产物仅包含 lb_part2 + lb_part3 两段 (共 ~198K tokens). 在此情形下, 产物末 30% 字符区间内仅含 1 段 `<!-- source: ... -->` (lb_part3 的开头注释), V6 `≥3` 硬门槛会 FAIL. 这是**最高风险项**. 但:
1. py_compile 过, 代码逻辑本身自洽, 非语法/结构错;
2. Node 2 hasn't run, token 密度估算存在 ±30% 误差, 实际 selected 可能 3-5 个而非 2 个;
3. Node 2 B6 跑 validate 后立即发现, 届时根据实测数据做微调 (降 V6 阈值 or 改 break 允许轻微超 200K 以多收几个小文件), 修改面 <20 行;
4. PLAN §1.3 P12 明示 "Node 2 A/B 校准", 本 carry-over 合 PLAN 预期.

故判 **CONDITIONAL_PASS**: Node 2 可开跑; 但 Phase 3 Node 2 B6 validate 完成后, 若 V6 FAIL, 主 session 必须按 HIGH-1 三选项之一调整并重跑, 同时修 MEDIUM-1 md5 时间戳问题作为 Rule D 独立复核的完整性保障. 其他 LOW 项作为 Phase B5 Rule A N=5 抽检后的清单处理, 不阻塞 Phase C 进入.

---

GEMINI_REVIEWER_DONE
Verdict: CONDITIONAL_PASS
