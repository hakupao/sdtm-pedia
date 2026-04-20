# ChatGPT GPTs Phase 3 Node 1 Scripts Reviewer Report

> Reviewer: oh-my-claudecode:code-reviewer (opus, subagent_id a137d22...)
> Date: 2026-04-20
> Reviewed: 4 脚本 (count_tokens / score / merge / validate), 共 1210 行 Python
> Verdict: **CONDITIONAL_PASS** (1 HIGH 必修 + 4 MEDIUM Node 2 前必修 + 若干 LOW 可 carry-over)
> 落盘说明: reviewer subagent (code-reviewer) read-only 无 Write 权; 本文件由主 session 代写, 文字完全来自 reviewer 返回值, 主 session 未编辑语义.

---

## M1 — PLAN 合规 (hard-fail 维度)

### 1. `score_chatgpt_priority.py` — PLAN §3.1 v1.1 + §3.2 v1.1

- **公式结构**: `score = (priority × coverage) + audience + novelty` — 第 165-166 行 `core = entry["priority"] * entry["coverage"]` + `raw = core + entry["audience"] + entry["novelty"]`. **加法结构 PASS**, 与 PLAN §3.1 v1.1 "核心(priority×coverage)+audience_bonus+novelty_bonus" 精确对齐. 非旧 v1 乘法. ✅
- **9 文件 × 四维字段硬编码** (FILES 列表 58-150 行): 与 PLAN §3.2 v1.1 表行行对齐. 我做了独立心算复核 (脚本未跑), 全 9 行 score 数字精确 match PLAN §3.2:
  - 01=3.4 / 02=3.4 / 03=3.2 / 04=3.2 / 05=1.5 / 06=1.9 / 07=1.2 / 08=1.2 / 09=1.2 ✅ 全 PASS
- **Floor 规则** (第 152 行 `FLOOR = 0.15` + 167 行 `max(raw, FLOOR)`): 精确对齐 PLAN §3.2 v1.1 "floor 0.15". ✅
- **排序** (181 行 `key=lambda r: (-r["score"], r["id"])`): score 降序 + id 升序 tiebreak, 稳定 & idempotent. ✅
- **合规结论**: PASS, M1 无偏离.

### 2. `merge_for_chatgpt.py` — PLAN §2.4 / §1.2 P12 / P13

- **9 合并文件目标**: MERGE_CONFIGS (186-259 行) 正好 9 条, 文件名 / stage (batch1/2) / expected_segments 与 PLAN §2.4 完全对齐. ✅
- **source glob 对齐 §2.4**:
  - 01: `_collect_navigation` 走 ROUTING/INDEX/VAR_INDEX 固定顺序 (第 98 行 `order` 列表) ✅
  - 02/03: `chapters/*.md` + `model/*.md` sorted ✅ (实测 KB 下 chapters=6, model=6, 与 PLAN §2.4 对齐)
  - 04/05/06: domains 子目录 × {spec,assumptions,examples}.md ✅ (实测 KB 下 63 域)
  - 07/08/09: terminology/{core,questionnaires,supplementary}/*.md ✅ (实测 42/43/6)
- **P12 溯源** (275-277 行 `_source_comment`, 304-305 行 "P12 注释 (必须紧贴段起点)"): 每源文件段起始插入 `<!-- source: <repo rel path> -->\n`, 紧贴源原文. 注释格式固定 (`<!--\s*source:\s*([^>]+?)\s*-->` 可匹配), 与 validate V3 regex (validate 91 行 `SOURCE_COMMENT_RE`) 对齐. ✅
- **P13 TableAware** (280-310 行 `_merge_sources` + 文档字符串 289-294 行): 段边界永远落在 "源文件起点/终点", 源内表格不可能被切 — 因为段边界不是 chunk 边界, 是文件拼接边界. **逻辑正确**. 我抽样检查 10 个域 (AE/AG/BE/BS/CE/CM/CO/CP/CV/DA) 的 spec/assumptions/examples — 全部不以 `|` 开头 (以 `#` 或普通文本开头), 前提成立. ✅ 但**未做 defensive 检测** — 见 M4-Issue-1.
- **合规结论**: PASS, M1 无偏离.

### 3. `validate_chatgpt_stage.py` — PLAN §2.5 V1-V6

| 校验 | 实现位置 | PLAN 依据 | 结论 |
|------|---------|----------|------|
| V1 非空 | 113-120 行 | §2.5 | PASS |
| V2 段数 | 123-130 行 (+ 动态 101-110 行) | §2.4 | PASS (01=3/02=6/03=6/04=63/05=63/06=63; 07/08/09 动态) |
| V3 P12 覆盖 | 133-169 行 | §1.2 P12 | ⚠️ **MEDIUM** — 见 M2 |
| V4 P13 表格 | 172-207 行 | §1.2 P13 | ⚠️ **MEDIUM** — 见 M4 |
| V5 token 上限 | 210-215 行 | §2.4 + §1.1 P1 | PASS (cap 硬编码 +15% buffer 见 174-183 行注释) |
| V6 md5 稳定 | 218-221 行 | §2.5 | PASS (打印, 不 FAIL, 与 PLAN "md5 稳定" 解读一致 — V6 是 Node 2 跨运次对比基线) |

### 4. `count_tokens.py` — PLAN §1.1 P1

- `tiktoken.get_encoding("cl100k_base")` ✅ (第 34 行 `ENCODING_NAME`)
- CLI 接口 `<file>: <N> tokens` (第 79 行) ✅ 对齐 PLAN §1.1 P1 "量化 PASS: 每 Step 打印 `[Stage X.Y] <file>: <N> tokens`"
- **MINOR**: PLAN §1.1 P1 格式要求前缀 `[Stage X.Y]`, 此脚本只打 `<file>: <N> tokens` 无 stage 前缀. merge 脚本 (413-416 行) 已补 `[Stage chatgpt-<stage>]` 前缀, count_tokens 作为独立工具不加前缀也可接受, 但在 "每 Step 打印" 场景下需调用方自己加前缀. LOW.

---

## M2 — 代码质量

### HIGH

**[HIGH-1] `validate_chatgpt_stage.py` V3 P12 覆盖率逻辑过宽, 漏检 "heading 跨源泄漏"** — 第 133-169 行

V3 语义设计如 docstring 所述 "允许 heading 之间共享一个 source comment" (第 141-142 行) — 一旦 `seen_source=True` 就永远为 True. 这意味着: 只要**首段**有 source comment, 之后**所有** heading 都算 covered, 即便中间段的 source comment 丢失也 PASS.

反例 mental trace: 若合并产物因 bug 变成
```
<!-- source: a.md -->
# A
<!-- source: b.md --> ← 丢失
# B     (源 b.md 的 heading)
```
如果仅仅第二个 source comment 被意外删掉, V3 仍报 PASS — 因为 `seen_source` 在第一行就被置 True. 这让 V3 **无法检测 P12 覆盖率低于 100%**, 而 P12 要求"每合并段起始加溯源"是**逐段**的 (PLAN §1.2 P12 原文).

**建议修正**: 语义应为 "段数 == source comment 数 == V2 expected_segments". V3 应改为逐段检查, 例如扫描 heading 时维护 "自上一 source comment 后是否未再见 source" 状态, 或更简单: 把 V3 的 "100% 覆盖" 等价到 V2 (段数对齐) + 新增 V3a "首个非空内容行必为 source comment"的结构检查. 当前实现**过度宽容**, 在 Node 2 真实校验时几乎永远 PASS, 无法履行 PLAN §1.2 P12 的实际把关作用.

**严重度 HIGH**: 语义与 PLAN §1.2 P12 不一致 (PLAN 强调每段起始溯源, 脚本只检查"首 heading 前有一条 source 即可"), Node 2 跑完看到 V3 PASS 也不能保证 P12 合规.

### MEDIUM

**[MEDIUM-1] `validate_chatgpt_stage.py` V4 边界检查逻辑太弱** — 第 172-207 行

`_v4_tableaware` 只检查 source comment 所在行的 **前一非空行** 和 **后一非空行** 是否都是 table row. 实际 merge 脚本在注释前会插入换行 + 空行 (280-310 行 `_merge_sources`): `parts.append("\n\n")` + `_source_comment(src)` + `text`. 因此 source comment 与源原文之间永无 `|` 相邻. 如果产物确实落入表格中, 那也是源文件内部结构异常, 而非 merge 造成 — **V4 对 merge 脚本的注释插入机制几乎永远无法 FAIL**.

这让 V4 沦为空跑. 真正的 P13 风险 (PLAN §1.2 P13 原文: "md-heading 边界保护表格, 不在 table row 内切. 单表不跨 heading") 包括两种:
- (a) source comment 落入表格 — V4 当前实现
- (b) **单表被 heading 切断** (即一个表格跨越两个 heading) — 完全未覆盖

V4 应至少加一项扫描: 对每个 heading, 检查其前 N 行与后 N 行是否都是 table row (说明一个表被 heading 切断). 或加 V7: 对每张 table 检查其内部没有 heading 行.

**严重度 MEDIUM**: V4 现实现逻辑自洽但语义窄, PLAN §1.2 P13 的硬门槛 "单表不跨 heading" 未被脚本实际执行.

**[MEDIUM-2] `merge_for_chatgpt.py` 07/08/09 段数期望为 0 (动态) 但无合规下限** — 第 240/248/256 行

动态段数允许 terminology 目录**完全为空**都 PASS (seg_count=0, expected_segments=0, 对比 `!=` 不触发 WARN 第 402 行). 但 405 行 `if not sources: return 2` 确实会早退. 路径: 若目录存在但无 .md, `sources=[]` → return 2, 仍会 FAIL. 好.

但 validate 端 `_v2_segment_count` (123-130 行) 对动态段数的 PASS 判据是 `n == expected` 且 `expected >= 0`. 若 terminology/core 有 42 个 md, expected 回填 42, 产物 source comment 也必为 42, PASS. 但**没有下限哨兵** — 如果某次合并只写出 1 个 source comment (bug), validate 会拿到 "actual=1, expected=1 (因为它从目录动态读)" PASS — 不对! expected 应该从 merge 时固化, 否则 dynamic 算两次都一样.

**建议修正**: merge 输出时把 "预期段数" 写入 manifest (或产物头注释), validate 读 manifest 或产物实际 source comment 数作为 truth, 再交叉验证. 当前 validate `_resolve_expected_segments` 再次读 `KB_DIR / subdir` 计数 (107-110 行) — 是同一口径重复, 没有独立 truth source.

**严重度 MEDIUM**: Node 2 若合并出错, validate 极可能掩盖 (两次读同一目录都算出 42, self-consistent 但错).

**[MEDIUM-3] `merge_for_chatgpt.py` 段数不匹配只 WARN 不 FAIL** — 第 402-408 行

```python
if entry.expected_segments > 0 and seg_count != entry.expected_segments:
    print(f"... WARN segment count {seg_count} != PLAN-expected ...", file=sys.stderr)
```

只打印 WARN, 不改 rc, 不 skip write. 产物仍会被写出. 若 04 期望 63 段而实际只 collect 到 50 段 (某些域缺 spec.md), merge 仍"成功", 只靠 validate 的 V2 兜底. 但 merge 脚本是 **Node 2 的 producer**, 默认应 fail-fast — PLAN §6 失败模式 #10 "源文件污染" 就要求立即回滚.

**建议修正**: 把 WARN 升级为 return 2 (或至少 return 非 0 让 rc 传播). 当前实现让 B3 "跑合并" 看起来 rc=0, Rule B 失败归档不会被触发.

**严重度 MEDIUM**: 与 PLAN §1.1 P1 "量化 PASS" + §6 失败模式抓取精神不符.

**[MEDIUM-4] `score_chatgpt_priority.py` 写 evidence 路径硬编码 `score_phase3.md` 与 PLAN 文档用语混用**

PLAN §4 Task B1 产物写 "score_phase2.md" (262 行), 脚本写 "score_phase3.md" (第 46 行). 不致命 (都在 dev/evidence/ 下), 但 verifier 走 PLAN 指引找不到文件会 confuse. 这个偏离 executor 未汇报, 但 PLAN 在 Task B1 位置确实写 phase2 (Phase 2 批 1 阶段的前置打分物).

**建议**: 以脚本实现为准 (phase3 正确, 因为这确实是 Phase 3 Node 1 的产物), 修 PLAN §4 Task B1 的文件名到 `score_phase3.md`. 或 carry-over 到 Node 2 前明确.

**严重度 MEDIUM**: PLAN vs 脚本对齐, Node 2 开跑前应明示选哪边.

### LOW

- **[LOW-1]** `merge_for_chatgpt.py` 第 53 行 `Callable` 从 typing 导入, 但同时从 `from __future__ import annotations` 开启前置延迟求值, 整行 `Callable[[], list[Path]]` 其实是字符串. 不影响 runtime. 代码洁癖意义上可以换成 `collections.abc.Callable` 或直接注释. 可忽略.
- **[LOW-2]** `count_tokens.py` 第 83-84 行: `elif file_count != 1:` 语义隐晦 — 意图是 "多文件时末尾额外打 TOTAL". 注释可加一行. 可忽略.
- **[LOW-3]** `validate_chatgpt_stage.py` V6 返回 `("N/A", ...)` (第 221 行), 但 `Row.all_pass` 把 "N/A" 算作 pass (第 243 行). 这是约定, 但 docstring 说 "不 FAIL" 隐含它不参与 PASS 判定 — 当前 V6 在 `any_fail` 检查 (第 303 行) 被排除, 正确. 只是语义透明度低, 需 comment.
- **[LOW-4]** 四个脚本的 `from __future__ import annotations` 在 Python 3.11+ 非必需, 但兼容 3.9/3.10 所以保留 OK.
- **[LOW-5]** `score_chatgpt_priority.py` 第 201 行 `write_evidence` 如被并发调用会产生竞争写, 但本脚本单进程无问题. 可忽略.
- **[LOW-6]** `merge_for_chatgpt.py` `_append_manifest_row` (353-381 行) 手工 parse markdown 表, 脆弱 — 若用户手动编辑 manifest 表列顺序, 匹配会失败. 范围可控 (只合并自动追加), 可 carry-over.
- **[LOW-7]** docstring 与 PLAN 对齐度高, 但缺显式 "依据 §X.Y" 条目在部分 helper 函数 (如 `_collect_navigation` 只写 "PLAN §2.4 列出顺序"). 可加强, 不阻塞.

---

## M3 — 规则合规 (A/B/D + P5/P6)

### P5 (knowledge_base/ 只读)
全 4 脚本对 `knowledge_base/` 仅做 `read_text` / `rglob` / `iterdir` / `is_file`. **无任何 Write / Edit / touch / copy / chmod**. ✅ 严格 P5.

- count_tokens: 52 行 `file_path.read_text` ✅
- merge: 297 行 `src.read_text` ✅, 写 out 仅到 `UPLOADS_DIR` (第 65 行 `PROJECT_ROOT / "current" / "uploads"`) 与 `MANIFEST_PATH` (第 66 行), 皆非 knowledge_base
- validate: 255 行 `path.read_text` (读 uploads, 非 KB), 220 行 `path.read_bytes` (md5, 读 uploads)
- score: 完全不碰 filesystem 的 KB, 硬编码 FILES list

### P6 (Subagent 上下文隔离, 脚本自给自足)
每脚本独立 argparse CLI, 无互相 import (count_tokens 被 merge/validate 内联重实现 `len(encoder.encode(text))`, 微重复但**更符合 P6 "每脚本独立"**). ✅

### 规则 A (压缩/改写 >50%)
merge 脚本对源文件做**拼接**, 不做 LLM 改写, 不做压缩 (每源文件原样落盘 + 注释头). 压缩率理论 = 0%. ✅ 不触发 Rule A N=5 抽检门槛. merge 脚本本身无 LLM 调用, 是纯 Python 拼接.

### 规则 B (失败归档)
**缺陷**: 所有 4 脚本都无 "失败时写 `dev/evidence/failures/stage_<N>_attempt_<M>.md`" 的代码路径. merge 脚本 run_entry 失败只打 stderr, 不写 evidence. 这是 Node 1 "仅写脚本" 接受的空缺 (失败归档是**主控** Rule B 职责, 非脚本), 但 docstring 也没提示 Node 2 运行方 "脚本失败时需手工归档".
**严重度**: LOW (规则 B 由主控执行, 脚本不担此责). 但文档可加一行提示.

### 规则 D (独立审阅)
本报告即是 Rule D 独立审阅. 我 (code-reviewer subagent_type) 与写脚本的 executor subagent 不同 type, 不读 executor completion 报告, 仅以 PLAN + 源脚本为真源. ✅ 自我合规.

---

## M4 — 边界案例 mental trace (不跑)

### [M4-Issue-1] 缺域目录 → merge 行为

假设 `knowledge_base/domains/AE/` 整个目录缺失. `_collect_domain("spec")` (129-139 行) 走 `sorted(p.name for p in base.iterdir() if p.is_dir())` — 若 AE dir 不存在, iterdir 不会 yield AE, spec 域列表 size = 62. `run_entry` 段数校验 (第 402 行) 发现 62 ≠ 63 → **只打 WARN, 仍写产物**. 见 MEDIUM-3.

### [M4-Issue-2] 若 spec.md 缺但 AE/ dir 存在

`_collect_domain("spec")` 内层 137 行 `if fp.is_file()` 过滤, 未命中不追加. 域列表静默 -1. 同 M4-Issue-1 WARN 路径.

### [M4-Issue-3] validate 产物段数少于 expected → rc

`_v2_segment_count` (第 129 行) 返回 ("FAIL", ...). `Row.all_pass` (241-245 行) `all(v[0] in ("PASS","N/A") ...)` → False. 最终 rc=1 (368 行). ✅ Node 2 会 rc 正确传播.

### [M4-Issue-4] `--no-evidence` flag 行为

`score_chatgpt_priority.py` 第 251-255 行 `--no-evidence` 走到 `args.no_evidence=True`, 第 260-262 行 skip `write_evidence`. stdout 仍打印 ranked list. **行为正确**. ✅

### [M4-Issue-5] Table cell 含 `|` 转义 (e.g. `\|` 或 `&#124;`)

`TABLE_ROW_RE = re.compile(r"^\s*\|")` (validate 93 行) — 只匹配行**开头**的 `|`. markdown 规范里, 内含 `\|` 转义也是在**中间**, 不会被误判为 table row. ✅ 不是问题.

**但有反向问题**: 若一行以 `| - some text` 开头 (quote 块内偶然的 markdown 表引用), 仍会被 TABLE_ROW_RE 匹配, 可能引入 V4 false positive. 鉴于源数据是 SDTM 标准文档 (大部分是正式表格), false positive 风险很低. LOW.

### [M4-Issue-6] `manifest.md` 首次初始化 vs 增量

merge 脚本 `_ensure_manifest` 第 346-350 行: 若 `MANIFEST_PATH.is_file()` 返回现有内容, 否则返回 `MANIFEST_HEADER`. 第二次 run 同 entry 时, `_append_manifest_row` 第 363-375 行查找同文件名 row, found → update 或 skip. **idempotent 成立**. ✅

### [M4-Issue-7] stdout 编码在 non-UTF8 locale

`encoding="utf-8"` 显式指定 (merge 297, score 243). `print` 默认用 sys.stdout.encoding, 若用户 terminal locale 非 UTF-8, 中文字符可能乱码但文件内容无损. LOW.

### [M4-Issue-8] KB_DIR 不存在

`merge_for_chatgpt.py` 第 457-459 行显式 check, return 2. ✅
`validate_chatgpt_stage.py` 第 341-347 行 check UPLOADS_DIR. ✅ 但 **不 check KB_DIR** — 当 07/08/09 动态段数 `_resolve_expected_segments` (107 行 `d = KB_DIR / spec.dynamic_source_dir`) 发现目录不存在返回 -1, V2 会 FAIL ("expected unknown") — 仍能工作. ✅

---

## M5 — 偏离清单判定

执行者自报 4 条偏离, 我以 PLAN 和脚本源码独立核对:

### 偏离 1: 01 合并源 `VAR_INDEX.md` 实际是 `VARIABLE_INDEX.md`, 脚本 fallback
**证据**: 实测 `knowledge_base/VARIABLE_INDEX.md` 存在 (134,513 B), 无 `VAR_INDEX.md`. 脚本 `_collect_navigation` (第 93-110 行) 设计了显式 fallback, 并在 docstring 注释解释.
**判定**: **合理接受**. 脚本产物正确 (3 段 = ROUTING+INDEX+VARIABLE_INDEX). 但 PLAN §2.4 行 1 "VAR_INDEX.md" 字面错误 — 建议 carry-over 修 PLAN 文字, 保持真实性.

### 偏离 2: 07/08/09 terminology 段数 PLAN 未给定 → validate V2 动态计数 (core=42 / questionnaires=43 / supplementary=6)
**证据**: PLAN §2.4 表 07/08/09 的段数列写的是 "N 段" 而非数字, 与 merge 脚本 `expected_segments=0` (动态) 对齐. 实测目录计数与执行者自报完全一致 (42/43/6). validate 脚本 `_resolve_expected_segments` 动态读 KB_DIR 子目录.
**判定**: **合理接受**. 但见 MEDIUM-2: 动态段数 "两边都读 KB" 无交叉验证, Node 2 前建议加独立 truth source (e.g. 合并时写 manifest 含 expected_segments, validate 从 manifest 读).

### 偏离 3: 合并配置未用外置 YAML, 改用 Python dataclass 硬编码 (减依赖 + 直白可审)
**证据**: merge 脚本 73-87 行 `@dataclass MergeEntry` + 186-259 行 `MERGE_CONFIGS`. 无 PyYAML 依赖. PLAN §2.5 表原文写 "合并配置 YAML" (第 167 行).
**判定**: **合理接受**. 理由:
- 规则 A 推崇 "直白可审" — dataclass 内联比 YAML 外置更易单文件审查
- 减少一个 pip 依赖 (PyYAML)
- idempotent 更强 (dataclass 不可能被用户手工误改)
- 但 PLAN §2.5 文字应修 "YAML" → "Python dataclass (硬编码)". Carry-over 到 Node 2 前文档同步.

### 偏离 4: 未执行任何脚本 (遵 Node 1 禁运行)
**判定**: **合理接受**. 脚本通过 `python3 -m py_compile` 我独立验证 (全 OK), 语法无误. Node 2 跑才是执行步.

---

## Carry-over 到 Node 2 (CONDITIONAL_PASS 必修)

### 必修 (Node 2 开跑前修完)
- [ ] **HIGH-1**: `validate_chatgpt_stage.py` V3 重写为真正逐段覆盖检查 (或并入 V2 等价). 否则 Node 2 V3 PASS 无意义.
- [ ] **MEDIUM-1**: V4 补 "单表跨 heading" 检查 (新增逻辑, 或接受 V4 范围受限并文档明示, 但后者要 PLAN §1.2 P13 做语义收窄说明).
- [ ] **MEDIUM-2**: 07/08/09 动态段数加独立 truth source (merge 写 manifest expected / validate 比对 manifest). 避免两边同源 self-consistent.
- [ ] **MEDIUM-3**: `merge_for_chatgpt.py` 第 402 行 WARN 升级 FAIL (return 非 0), fail-fast.
- [ ] **MEDIUM-4**: 确认 `score_phase3.md` vs PLAN §4 Task B1 `score_phase2.md` 取哪个 — 建议以 phase3 为准, 修 PLAN.

### 文档同步 (PLAN 修, 不改脚本)
- [ ] PLAN §2.4 行 1 `VAR_INDEX.md` → `VARIABLE_INDEX.md` (或并列标出 fallback 语义)
- [ ] PLAN §2.5 "YAML" → "Python dataclass 硬编码"
- [ ] PLAN §2.1 要求的 `dev/evidence/failures/`, `subagent_prompts/`, `checkpoints/` 三目录未创建 — 当前仅 `dev/evidence/` 扁平, Node 2 前建议预建空目录 + `.gitkeep` (Rule B 预留).

### 可 carry-over (不阻塞 Node 2)
- [ ] LOW-1..LOW-7 注释/文档改进
- [ ] count_tokens.py stage 前缀 (若需要 `[Stage X.Y]` 统一日志格式, 脚本间互相协商)

---

## 最终 Verdict + 理由

**CONDITIONAL_PASS**

**理由 1 — PLAN 合规 M1 核心 PASS, 打分数字精确命中**. score_chatgpt_priority 九行数字我做了独立心算复核, 全部 match PLAN §3.2 v1.1 (01=02=3.4 / 03=04=3.2 / 05=1.5 / 06=1.9 / 07-09=1.2), 加法公式结构正确, floor=0.15 一致. merge 9 文件目标 / source glob 对齐 §2.4 (VAR_INDEX 偏离有合理 fallback). P12 溯源注释格式 / idempotent / tokens 计算等硬点全过. 不需 FAIL 整个 Node 1.

**理由 2 — 1 条 HIGH 的 validate V3 语义缺陷必须修**. V3 的 "一次 seen_source 永远 True" 让 "P12 覆盖率 100%" 口号变成"首段有注释即 PASS", 这偏离 PLAN §1.2 P12 "每合并段起始" 的逐段要求. Node 2 若就此 PASS, 主控以 V3 为信号会拿到假阳性. 不修就进 Node 2 = 违反规则 D (Rule A 精神: 结构检查 ≠ 业务检查, V3 当前是弱结构检查伪装成业务检查).

**理由 3 — MEDIUM 集中在 "fail-fast 强度不足" 和 "动态校验无独立真源"**. 修复工作量低 (都是 1-10 行改动), 但不修 Node 2 会出现 "WARN 但 rc=0" "两边同源自洽但其实错" 的假阳性. 全部建议 Node 2 开跑前修完.

**理由 4 — 4 条偏离中 3 条合理接受**, 分别是 VAR_INDEX 重命名 (现实高于 PLAN 字面)、terminology 动态段数 (PLAN 留 "N" 占位, 脚本动态合理)、dataclass 替 YAML (直白可审优于外置). 第 4 条 "未运行脚本" 是 Node 1 基本约束, 自然接受. PLAN 文档需同步修改, 但不阻塞脚本本身.

**理由 5 — 规则合规扫描全 PASS**: P5 严格只读 (无 Write to KB), P6 脚本自给自足 (无互相 import), 规则 A 不触发 (纯拼接 0 压缩), 规则 D 独立审阅 (本报告). 脚本语法 py_compile 全过. 无安全问题 (无 secret / 无 injection / 无 eval / 无 subprocess 命令注入面).

综上: 脚本结构扎实, PLAN 合规度高, 但 validate 的 V3/V4 两个核心校验项语义过宽, 动态段数缺独立真源, fail-fast 点需要加强. 这些都是 Node 2 实际依赖的 "产物质量信号" — 不修就把风险传给 Phase 3 全链路. 建议主控回 executor 修 HIGH-1 + 4 MEDIUM 后, 重新对 validate_chatgpt_stage.py + merge_for_chatgpt.py 做一轮 delta review, 通过后放行 Node 2.

---

Verdict: CONDITIONAL_PASS

CHATGPT_REVIEWER_DONE
