# ChatGPT GPTs Phase 3 Node 1 Delta Reviewer Report

> Delta reviewer: oh-my-claudecode:debugger (opus)
> Scope: 原 reviewer HIGH-1 + MEDIUM-1 + MEDIUM-2 + MEDIUM-3 修复有效性审查 (4 bug, 非全脚本重审)
> 规则 D: 与 writer (executor)、fix-writer (executor)、原 reviewer (code-reviewer) 均不同 subagent_type
> Date: 2026-04-20
> Verdict: **FAIL_REWORK**

---

## 上下文

- 原 reviewer 报告: `ai_platforms/chatgpt_gpt/dev/evidence/phase3_node1_reviewer.md` (260 行, CONDITIONAL_PASS)
- 修复范围 (git diff HEAD 后): merge_for_chatgpt.py 479 → 601 行 (+122), validate_chatgpt_stage.py 374 → 624 行 (+250), 新增 `current/manifest_segments.json` (3 行 skeleton, untracked), PLAN.md §0 v1.2 + §2.4 / §2.5 / §4 Task B1 文字同步.
- `py_compile` 两脚本语法 PASS.
- 手写 mental trace 覆盖 V3 (6 场景), V7 (文件边界 + 文件内部), manifest JSON 轮换, rc propagation, 共 15 个 edge case.
- 未跑任何业务脚本 (Node 1 禁运行原则).

---

## D1 — HIGH-1 V3 修复有效性

### 认定: **PASS with minor residual gap**

**修复位置**: `validate_chatgpt_stage.py` 218-318 行 `_v3_p12_coverage` 彻底重写, 原 "seen_source 一次 True 永远 True" 状态机移除, 替换为 3 锚点 + heading 上游必存 source + 每 heading 上游最近 source 距离检查.

### 反例 mental trace (6 场景)

设 expected=3 (01_navigation 风格), 3 源 a/b/c.

**场景 1 (健康)**: `<!-- source: a -->\n# A\n<!-- source: b -->\n# B\n<!-- source: c -->\n# C`
- (a) source_count=3 == expected=3 PASS
- (b) 首非空 = source PASS
- (c) 首 heading line 2, 首 source line 1, 1 < 2 PASS; 每 heading 上游均有 source, max_distance=1 PASS
- **V3 PASS** ✓

**场景 2 (原 reviewer 反例, 第 2 个 source 漏删)**: `<!-- source: a -->\n# A\n# B\n<!-- source: c -->\n# C`
- source_count=2, expected=3 → **(a) FAIL** "source count 2 != expected 3"
- **V3 FAIL** ✓ (原 bug 被捕获)

**场景 3 (首段无 source, source 提到 heading 后)**: `# A\n<!-- source: a -->\n# B\n<!-- source: b -->\n<!-- source: c -->\n# C`
- source_count=3, expected=3 → (a) PASS
- 首非空 = `# A` (heading, 非 source) → **(b) FAIL** "first non-empty line 1 is not a source comment"
- **V3 FAIL** ✓ (首段起始锚点漏失被捕获)

**场景 4 (单段产物, expected=1)**: `<!-- source: a -->\n# A\nbody text`
- source_count=1 == expected=1 → (a) PASS
- 首非空 = source → (b) PASS
- 首 heading line 2, 首 source line 1, 1 < 2 → (c) PASS; max_distance=1
- **V3 PASS** ✓ (单段边界合理)

**场景 5 (无 heading, 只有 source, navigation 纯文本)**: `<!-- source: a -->\ntext\n<!-- source: b -->\ntext\n<!-- source: c -->\ntext`
- source_count=3 == expected=3 → (a) PASS
- 首非空 = source → (b) PASS
- heading_count=0, source_count=3 → 跳过 `if heading_count > 0 and source_count == 0` 分支
- 跳过 `if heading_count > 0` 主分支
- 落到 fallthrough `return "PASS", f"{source_count} sources, 0 headings"` → **V3 PASS** ✓

**场景 6 (空文件)**: 空串.
- first_non_empty_line_index=None → (b) 条件 `is not None` skip
- heading_count=0 + source_count=0 → 返回 "N/A, no headings and no sources"
- V1 前置会 FAIL "size=0" → rc=1 propagate ✓ (职责分离清晰)

### 3 锚点 vs PLAN §1.2 P12 "每段起始溯源" 等价性

PLAN 原文: "每合并段起始加 `<!-- source: <原路径> -->`". 3 锚点:
- (a) 段数锚: source_count == expected (manifest 声明) — 抓"某段 source 被漏插/误删"
- (b) 首行锚: 首非空行必是 source — 抓"首段起始没 source" (场景 3)
- (c) heading 上游必存 source + 每 heading 上游最近 source — 抓"heading 在文档中上游无 source"

**等价性评估**: 3 锚点联合 ≠ 完整"每段起始" 的严格等价, 但在产物的可观察信号上足够强:
- (a) 捕获"总数不对"
- (b) 捕获"第 1 段没 source"
- (c) 捕获"heading 出现在 source 之前"

### 残余 gap (LOW, 非本次 4 bug 范围)

**场景 R (新发现, source 路径重复)**: `<!-- source: a -->\n<!-- source: a -->\n# A\n# B\n<!-- source: c -->\n# C`
- source_count=3, expected=3 → (a) PASS
- 首非空 = source → (b) PASS  
- 每 heading 上游均有 source → (c) PASS
- **V3 PASS** — 但产物其实**丢了 source b, 多了重复 source a**. V2 + V3 都掩盖此 bug, 因为两者都只数 source 数量, 不检查 source 路径的**唯一性/与 merge 声明清单的集合一致性**.

**判定**: 此 gap **不在原 reviewer 4 bug 范围内**, 属于新发现的 LOW-level residual 风险. 不阻塞 HIGH-1 修复认定 PASS. 建议 Node 2 前或 Node 3 前增补 V3d 子条件: "source 路径集合 == merge 声明路径集合"; 或放到 `failures/` 归档为 carry-over. Node 2 的 Rule A 抽检 (N=5 段独立验证) 是兜底.

### D1 结论: **修好** (原 bug 反例场景 2/3 均能被捕获, 单段/空文件/纯 source 3 个边界合理). 残余 R 场景为新增发现, 不阻塞本次放行.

---

## D2 — MEDIUM-1 V7 修复有效性

### 认定: **FAIL_REWORK** (V7 (ii) 误杀, 且误杀密度极高, Node 2 跑必 FAIL)

**修复位置**: `validate_chatgpt_stage.py` 359-441 行 新增 `_v7_table_heading_split`. 两子条件:
- (i) 连续 table row 块中间直接出现 heading 行 (无空行过渡)
- (ii) heading 的最近前非空行 AND 最近后非空行都是 table row (skip blanks + skip source comments)

### V7 (i) 语义分析

(i) 要求 heading 紧跟 table row 无空行过渡. 扫描 **201 个** merge 源文件 (63 域 × 3 + chapters 6 + model 6 + 3 navigation + 42+43+6 terminology):

```
V7(i) pattern in raw sources: 0 files, 0 violations
```

Markdown 规范里 heading 前至少有空行是常态, raw source 无一命中. **(i) 语义健康, 真正可抓 merge 产物里的异常结构**. PASS.

### V7 (ii) 语义分析 — **误杀核心问题**

(ii) 判据: heading 前后**最近非空行**都是 table → FAIL. 这是**过度收敛**: 两张**独立**的表格之间若用 heading 分隔, 正是 markdown 标准做法, 不是 P13 违反.

**扫描 raw sources (未经 merge) 的 (ii) FP 密度**:

```
Files with intra-file V7(ii) FP pattern: 5
Total heading violations: 77
  knowledge_base/VARIABLE_INDEX.md: 62 headings     ← 严重, 合进 01_navigation.md
  knowledge_base/INDEX.md: 7 headings               ← 合进 01_navigation.md
  knowledge_base/model/02_observation_classes.md: 6 headings  ← 合进 03_model_all.md
  knowledge_base/model/03_special_purpose_domains.md: 1       ← 合进 03_model_all.md
  knowledge_base/model/06_relationship_datasets.md: 1         ← 合进 03_model_all.md
```

这 77 个 heading **在 raw source 就是合法内容**, merge 是纯拼接 (P5 只读, 0 改写), 产物里它们**原封不动**存在. V7 (ii) 会对 merge 产物 `01_navigation.md` 和 `03_model_all.md` **批量 FAIL**.

**具体反例 (来自 VARIABLE_INDEX.md 第 110 行)**:
```
| SITEID | AE.SITEID | AE | ... |   ← 前一域的 table 尾行
                                   ← 空行
### AG — Procedure Agents (Interventions)   ← heading (legitimate, 下一域标题)
                                   ← 空行
| Variable | Position | Domain | ... |   ← AG 域的 table 头
| DOMAIN | AG.DOMAIN | AG | ... |
```
backward nearest_non_empty → table row (前域 SITEID 行), forward nearest_non_empty → table row (后域 DOMAIN 行). V7 (ii) **FAIL** 即使这是**完全合法的 markdown**. 同样模式 VARIABLE_INDEX.md 里 62 次, 加上 INDEX/model 3 个文件 15 次, 合计 77 次.

### 这是 merge bug 吗? 不是.

PLAN §1.2 P13 原文: "md-heading 边界保护表格, 不在 table row 内切. **单表不跨 heading**". 语义是: 同一**张**表格不允许被 heading 打断. 两**张**独立表之间有 heading 合法, 甚至推荐 (用 heading 标记新 topic).

V7 (ii) 收紧到 "heading 最近邻前后若都是表行即 FAIL" 是**过度泛化**. 真正的 "单表跨 heading" 只能由 **chunker 切分时的行为** (800 token block 落入 table 中间) 触发, merge 脚本是纯拼接, 根本造不出这种产物 — 除非源文件本身就是"表中间夹 heading", 而 V7 (i) 已覆盖此场景 (且 raw sources 0 命中, 说明源无此问题).

### 构造反例: V7 (ii) 对 merge 边界的误杀

更糟的反例 (inter-file heading 在 merge 产物中):

```
...AE 域最后一张表尾行:
| ZDATE | AE.ZDATE | AE | ... |

<!-- source: knowledge_base/domains/AG/spec.md -->
# AG — Procedure Agents
```

AG/spec.md 首非空行是 `# AG — Procedure Agents`, 其下一非空行是 `> Class: Interventions | ...` (blockquote) — 不是 table. 所以此 inter-file 边界 **V7 (ii) PASS**. 这条路径侥幸没被误杀.

但 VARIABLE_INDEX.md 是**单文件内部**就有 62 个 "table-heading-table" 模式 (一个 flat list of domains × variables), merge 把它整块落盘后, 62 次全 FAIL.

### 反面: 能抓到的真 bug

构造 "merge 把 heading 塞进单表中间" 这种真 bug:
```
| col1 | col2 |
|------|------|
| x | y |
## inserted heading      ← merge 把 heading 插进表中
| z | w |
```
V7 (i) 立即 FAIL (heading 紧跟 table 无空行过渡). **所以 (i) 已覆盖真 bug 场景**. (ii) 纯属 false-alarm 加码.

### 修复建议

V7 (ii) 必须**放宽或删除**. 两个可选:

**选项 A (推荐, 最小改动)**: 删除 (ii), 只保留 (i). 理由:
- (i) 已精准覆盖 PLAN P13 "单表不跨 heading" 硬门槛 (因为若真被 heading 切断, 切断点两侧必有无空行紧邻的 table/heading 对).
- (ii) 对 markdown 正常多表分节模式一律误杀, 阻塞 Node 2 batch1 全部 PASS 的可能.

**选项 B (收紧 ii 语义)**: 把 (ii) 改为 "heading **同一个 table 块内部** 出现", 即扫描时若 in_table=True 且遇 heading (已是 (i) 语义). 本质和 (i) 合并. 等价选项 A.

### D2 结论: **不能放行**. V7 (ii) 作为 MEDIUM-1 的"额外补强"过度泛化, 77 个合法 heading 在 merge 产物 01/03 批处稳定误杀, Node 2 跑 validate batch1 必 FAIL 阻塞. 必须在 Node 2 前删除 (ii) 或等价收窄. (i) 保留 (0 FP, 覆盖 P13 硬门槛).

---

## D3 — MEDIUM-2 manifest 独立真源有效性

### 认定: **PASS**

**修复位置**:
- merge 侧 (L337-408): 新增 `_resolve_dynamic_expected` / `_load_manifest_segments` / `_write_manifest_segments` / `_update_manifest_segments`, 写模式下 (L540-542) run_entry 末尾为每产物写 `current/manifest_segments.json`.
- validate 侧 (L135-177): `_load_manifest_segments` + `_resolve_expected_segments` 改为**只读 manifest JSON**, 原"重读 KB 子目录计数"路径移除.

### 反例 mental trace

**Bug A (merge 少写 1 source, manifest 写 correct expected)**:
- merge 收集到 62 个 domain specs (AE 缺失) 但仍把 `expected=63` 写 manifest (假设 bug 是 source_collector 层的). 产物含 62 个 source comment, manifest `{"04_...": {"expected": 63, "actual": 62, ...}}`.
- 等等 — 代码实际行为: `_update_manifest_segments(entry, seg_count, expected, dynamic)` 中 `expected = _resolve_dynamic_expected(entry, seg_count)` 当静态 > 0 时返回 `entry.expected_segments=63`, actual=seg_count=62. 但 MEDIUM-3 修复已保证 seg_count != expected 时写模式直接 rc=2 **不写产物不更新 manifest** (L533-534 `if segment_mismatch: return 2`). 所以此 bug 路径在 manifest 更新前就 fail-fast 了.
- 若假设 fail-fast 失效, 走到 manifest 更新: validate 读 manifest expected=63, 数 actual source comment=62, V2 FAIL. **能抓到** ✓

**Bug B (merge 多写 source comment)**:
- 假设 source_collector 返回 63 但 `_merge_sources` 因 bug 为某源插 2 条 source comment (产物 64 条). seg_count=63, manifest写 expected=63 actual=63. validate 数产物 source comment=64, expected=63 → V2 FAIL. **能抓到** ✓

**Bug C (merge 写错误 expected)**:
- merge 内部一致 (expected=63, actual=63, 产物 63 source), 但实际 knowledge_base 只有 62 个 domain (某个域被删除). validate 读 manifest expected=63, 数产物 source=63, V2 PASS. **不能抓** — 但原 reviewer 在 M2-MEDIUM-2 描述里也接受此 gap: "若 merge 写出错误 expected, 谁能发现? 这是 self-consistent 在 merge 内部, 需要其他机制兜底; reviewer 可能接受因为 Node 2 Rule A 抽检是兜底". ✓

### 边界 mental trace

- **manifest 文件缺**: `_load_manifest_segments` 返回 None → `_resolve_expected_segments` 返回 `(-3, "no-manifest-file")` → V2 "no manifest truth source" FAIL. ✓
- **manifest 存在但 entry 缺**: `entry = manifest.get("entries", {}).get(spec.target)` 返 None → `(-2, "missing-from-manifest")` → V2 FAIL. ✓
- **manifest entry.expected 缺字段 / 非 int**: `if not isinstance(expected, int) or expected < 0` → `(-2, "invalid-expected-in-manifest")` → V2 FAIL. ✓
- **manifest entry 存在, 静态 expected (spec.expected_segments=63) ≠ manifest expected (63)**: 两者相等走 "manifest-static" 正常 PASS. 若 manifest (e.g. 62) != static (63), 返回 `(expected, "manifest-overrides-static(63)")` — 以 manifest 为准. 实际 V2 拿 manifest=62 和 actual 比, 若 actual 也=62 PASS. 静态值的 discrepancy 仅做 source_label 诊断输出, **validate 不再 double-guard**. 这是 fix 的明示设计 (见 L163 docstring), **符合 MEDIUM-2 意图** (merge 侧 fail-fast 兜底).
- **manifest 损坏 JSON**: `except json.JSONDecodeError` 返 None, 同 "manifest 缺". ✓
- **merge 重跑**: `_update_manifest_segments` load → 覆盖该 entry → write. sorted keys + indent=2, **idempotent 确认**:
  ```
  sort_keys 轮换 serialize/load/re-serialize byte equality: True ← 独立验证
  ```
  ✓

### JSON Schema 稳定性

`{"entries": {<target>: {"stage", "expected", "actual", "dynamic"}}}` — 4 字段固定. sort_keys=True 保证递归字典顺序稳定. indent=2 固定. 字节 idempotent ✓ (已独立 py 测).

### .gitignore 检查

```
git check-ignore -v manifest_segments.json → exit=1 (not ignored)
git ls-files manifest_segments.json → empty (untracked, 骨架未 commit)
```
**不被误 ignore**, 但目前 skeleton 仍是 untracked. Node 2 首次 merge 跑会覆盖. Phase 3 Node 1 commit C1 应把 skeleton 入库, 否则 validate 在别的 session clean clone 场景会 FAIL "no manifest truth source". **建议**: C1 commit 把 `manifest_segments.json` 加入. (LOW, 不阻塞 D3 本身的 PASS 认定.)

### D3 结论: **修好**. 4 路径 (缺文件 / 缺 entry / 字段坏 / 正常) 均正确路由; Bug A/B 能被 V2 捕获, Bug C 不能但有 Rule A 兜底 (原 reviewer 同意). JSON idempotent 独立验证通过. 唯一需跟进: skeleton commit 入库.

---

## D4 — MEDIUM-3 fail-fast 有效性

### 认定: **PASS**

**修复位置**: `merge_for_chatgpt.py` L487-552 `run_entry` 重写:
- L504-507 计算 `segment_mismatch`
- L508-516 按 `dry_run` 分叉: dry_run → level="WARN", 写模式 → level="FAIL"
- L527-530 dry_run 下 return 0 (降级)
- L532-534 **写模式下 `if segment_mismatch: return 2` — 不落盘, 不写 manifest, 不 append manifest.md row**
- L592-597 main 聚合: `if r != 0: rc = r` — 任一 entry 非 0, main 最终 rc 非 0 (取最后 non-zero). 对聚合是否"取最严"严格考查: Python 语义是 "last non-zero wins", 但关键是 **至少有一个 non-zero 就 propagate**. 对 ChatGPT Node 2 场景 (期望 rc=0 才 smoke test) 语义足够: 任一 FAIL → main rc != 0 → Node 2 主控拒绝继续.

### 反例 mental trace

**Bug expected=63 collect=62 (写模式)**:
- sources 62 条, expected_segments=63, segment_mismatch=True.
- dry_run=False → level="FAIL" 打印 stderr.
- `text = _merge_sources(sources)` + tokens 仍计算 (让用户看 stdout 调试信息).
- stdout 正常打 `tokens_str`.
- `if dry_run: ... return 0` 跳过 (dry_run=False).
- `if segment_mismatch: return 2` — 返回 2, **不写产物, 不写 manifest, 不 append manifest.md**.
- main 收到 r=2, rc=2 propagate. sys.exit(2). ✓

**Bug expected=63 collect=62 (dry-run 模式)**:
- segment_mismatch=True, level="WARN".
- stderr 打 WARN.
- stdout 打 tokens.
- `if dry_run: print [DRY] skip write; return 0` — dry_run 允许继续, rc=0. **dry_run 语义合理**: 用户做计划/体检用, 不写产物就不污染 current/uploads/. ✓

**Bug sources=[] (源目录缺)**:
- L494-500 先 catch: "ERROR no sources collected" stderr → return 2. ✓ (比 segment_mismatch 更早 fail-fast).

**动态 entry (expected_segments=0, 不触发 segment_mismatch)**:
- L505 `entry.expected_segments > 0 and seg_count != entry.expected_segments` — expected_segments=0 时直接 False, segment_mismatch=False.
- 7/8/9 terminology 动态 entry 无论 seg_count 多少都不触发 fail-fast. **设计合理** (动态 expected 本就是运行时快照). MEDIUM-3 范围本就不覆盖动态 entry.

**多 entry 聚合**:
- pick_entries("batch1") = 4 entries. 若 entry 1 rc=0, entry 2 rc=2, entry 3 rc=0, entry 4 rc=2.
- main 循环: rc 初 0 → entry1 r=0 no update → entry2 r=2 rc=2 → entry3 r=0 no update (保留 rc=2) → entry4 r=2 rc=2 (还是 2).
- **任何非 0 rc 都 propagate 到 main**, 即便后续 entry 成功也不清零 (因为 `if r != 0: rc = r`). ✓

### 产物污染风险

严格查证 L532-542 顺序:
- L533 `if segment_mismatch: return 2` — **在 write_text 之前 return**.
- L537 `out_path.write_text(text, ...)` — 不会执行.
- L540-542 manifest 更新 — 不会执行.
- L544 manifest.md 追加 — 不会执行.

产物**确实没被写出** (不是"写了但 rc=2"). ✓

### D4 结论: **修好**. 写模式下 segment mismatch 真正 fail-fast (rc=2, 无落盘); dry-run 降级 WARN 合理. 多 entry 聚合保证任一 FAIL propagate 到 main.

---

## D5 — 交叉影响 (规则 A 精神: 结构检查 ≠ 语义检查)

### D5.1 V3 和 V7 交互

V3 和 V7 各有职责:
- V3 检查 source comment 的**数量 + 位置**
- V7 检查 **table / heading 相邻关系**

两者不共享状态. V3 会因场景 2 (某段 source 漏删) FAIL, 此时 V2 也 FAIL (同样的 source count 锚). V7 不受影响 (V7 不看 source 数量).

但 **D2 已指出 V7 (ii) 会在 `01_navigation.md` 和 `03_model_all.md` 上稳定 FAIL**. 这意味着 **Node 2 跑 validate batch1 聚合 rc=1**, 即便 V1/V2/V3/V4/V5 全 PASS, V7 单点拖垮. 交叉效果: V3/V4 的修复价值被 V7 的 FP 掩盖 (因为整条 rc 已非 0, 主控可能误以为"V3 也有问题"从而回到执行者做无谓修改).

### D5.2 manifest + fail-fast 交互

MEDIUM-2 (manifest) 依赖 MEDIUM-3 (fail-fast) 不污染 manifest. 检查: run_entry 里 fail-fast `return 2` 发生在 `_update_manifest_segments` 之前 (L533 < L542), 所以**坏产物不会把坏 expected/actual 写进 manifest**. Node 2 重跑时, manifest 仍保留上次成功运行的 expected (若首次就失败, manifest 就是空 entries 骨架 — validate 正确报 "missing-from-manifest"). ✓

### D5.3 manifest_segments.json 是否被 .gitignore 误 ignore

```
.gitignore 全文仅: .DS_Store / source/ / project_knowledge_base/ / markdown/ / reports/ / tmp/ / .claude/ / .omc/ / .omx/ / notes/
git check-ignore manifest_segments.json → exit=1 (not ignored)
```
**不误 ignore**. ✓ 但目前 untracked (L: 3 行 skeleton, `ls-files` 空). 主控 Phase 3 Node 1 C1 commit 应 `git add` 之, 否则 Node 2 clean-clone 场景 validate 直接 "no-manifest-file" FAIL. **LOW**, 不改变 D5 本身的判定.

### D5.4 V7 性能开销

V7 扫整个 lines 两遍 (一次 for i, 一次 per-heading nearest_non_empty). 对 63 域 domain_specs_all.md (~672KB, ~50-60K 行) 是 O(N + H×N) ≈ O(N²) 最坏 (H 最大约 200 个 heading). 实测 N=60000, H=200, 操作次数 60000 + 200×60000 ≈ 1.2e7, Python 原生 ~1-2 秒, 可接受. 对 3.8MB 的 08_terminology_questionnaires.md (~300K 行, H~400) 最坏 1.2e8 操作, ~10-20 秒. **性能可接受但非优**. 非阻塞.

若 V7 (ii) 删除 (按 D2 建议), 性能回到 O(N) 单遍, ~亚秒级. 顺便解决 5.4.

### D5 结论: **除 V7 (ii) 对 batch1 产物的 FP 会掩盖其它修复价值**, 其它交叉无害. fail-fast 正确先于 manifest 更新. manifest 文件未被 gitignore 误伤.

---

## D6 — 可维护性 (轻权重)

### D6.1 docstring 链接

- merge_for_chatgpt.py L45-62 v1.1 修复记录段: 明确列 MEDIUM-2 / MEDIUM-3, 描述了新 JSON schema 和 WARN→FAIL 升级. ✓
- validate_chatgpt_stage.py L54-66 v1.1 修复记录段: 明确列 HIGH-1 / MEDIUM-1 / MEDIUM-2, 链到原 reviewer "CONDITIONAL_PASS → bug fix pass". ✓
- **未显式 link 到 `phase3_node1_reviewer.md` 文件路径** (只有"reviewer" 字样). LOW. 可加条: `see dev/evidence/phase3_node1_reviewer.md § M2 HIGH-1 / MEDIUM-1~3`.

### D6.2 代码风格

- pathlib: ✓ (全部用 Path, 无 os.path.join)
- dataclass: merge L97-110 `@dataclass MergeEntry`, validate L101-108 `@dataclass ExpectSpec`, validate L463-481 `@dataclass Row` (扩到 7 字段). ✓
- 中文注释: 保持. ✓
- 类型注解: L342 `tuple[int, bool]`, L135 `dict | None` 等 PEP 604 union. ✓
- `from __future__ import annotations` 保留. ✓

### D6.3 v7 字段顺序

Row 从 v1..v6 扩到 v1..v7 (v7 插在 v6 前后). 实际定义顺序: v1, v2, v3, v4, v5, v6, v7 (L467-473). 报告矩阵顺序 (L525): `V1 V2 V3 V4 V5 V7 V6`. stdout 顺序 (L608): `V1 V2 V3 V4 V5 V7 | V6 md5`. **字段在 Row 按时间序, 在报告按业务序**, 轻微不一致但可读 (注释里 v7 挤在 v6 前). 可接受.

### D6 结论: **基本合格**. docstring 链 reviewer 报告路径是 LOW 级小缺漏, 不阻塞.

---

## 最终 Verdict + 结论

**Verdict: FAIL_REWORK** (不能放行 C1 commit).

**理由 1 — V7 (ii) 是规则 A "结构检查 ≠ 业务检查" 的反面教材, 且拖垮 Node 2**. V7 (ii) 的本意是抓 P13 "单表跨 heading", 但实现收紧到 "heading 最近邻前后都是 table row 即 FAIL", 误把"两张独立表之间用 heading 分节"这种 markdown 标准做法当成违规. raw source 扫描显示 **77 个合法 heading 在 5 个源文件中命中此 FP 模式**, 其中 VARIABLE_INDEX.md 一家 62 次. merge 是 P5 只读纯拼接, 无法"改造"这些合法结构, 所以 V7 (ii) 会在 `01_navigation.md` 和 `03_model_all.md` 上**稳定 FAIL**. Node 2 跑 `validate_chatgpt_stage.py --stage batch1` 聚合 rc=1 **必定发生**, HIGH-1/MEDIUM-2/MEDIUM-3 的修复价值被掩盖, 主控会误以为修复有其它问题. 这是 "reviewer 要求加检查" 的 over-correction 典型失败.

**理由 2 — HIGH-1 / MEDIUM-2 / MEDIUM-3 三处修复扎实**. V3 重写覆盖 6 个 mental trace 场景 (健康 / 原 reviewer 反例 / 首段无 source / 单段 / 纯 source 无 heading / 空文件), 3 锚点逻辑清楚, 反例全能捕获. manifest 独立真源 4 条路径 (缺文件 / 缺 entry / 字段坏 / 正常) 均正确, JSON idempotent 独立 py 验证 True. fail-fast 在 write_text 之前严格 return 2, 不污染产物, 不污染 manifest; dry-run 降级 WARN 合理; 多 entry 聚合保证 propagate. 三点单独看是 PASS 质量.

**理由 3 — D1/D3/D4 PASS 不能抵消 D2 的 FAIL**. 规则 D 的判定是"4 bug 全部 root-cause fix"才 PASS, 任一 HIGH 或 ≥2 MEDIUM 未修好即 FAIL_REWORK. 当前 MEDIUM-1 的 V7 (ii) 部分**不是修不到位, 而是修过头误杀合法内容**, 等同于引入新 bug. 按 delta reviewer 的 "无引入新问题" 标准, 当前 fix 不能放行 C1 commit.

### 必改项 (executor 重工, 修完再找独立 reviewer 二审)

1. **MEDIUM-1 V7 (ii) 删除或等价收窄到 (i)** 的语义. 推荐最小改动: 仅保留 (i) "连续 table 块中间无空行直接出现 heading" 一条, 因为 (i) 已覆盖 PLAN §1.2 P13 "单表不跨 heading" 的真实破坏形态 (raw source 0 FP, 语义精准). 修完把本 delta 反例 (VARIABLE_INDEX.md 62 headings 场景) 加进 V7 docstring 作"不抓此模式, 属合法"的说明.
2. **[carry-over, LOW]** manifest_segments.json skeleton 加入 C1 commit (git add), 防 Node 2 clean clone 场景 FAIL.
3. **[carry-over, LOW]** V3 残余 R 场景 (source 路径重复/缺失 但 count 相等) 在 Phase 3 Node 2 前或 Node 3 增补 V3d 子条件 "source 路径集合 == merge 声明集合". 非阻塞本次放行.
4. **[carry-over, LOW]** V7 性能若保留 (ii) 则评估大文件 (3.8MB terminology_questionnaires) 跑时. 若按建议删除 (ii), 性能非问题.
5. **[carry-over, LOW]** docstring 里补 `see dev/evidence/phase3_node1_reviewer.md` 路径链接.

### 不改动项 (本次 fix 其它部分保留)

- V3 全部重写逻辑. ✓
- manifest_segments.json 的 schema / idempotent / 优先级路由. ✓
- run_entry 的 fail-fast / rc=2 / 产物不落盘. ✓
- PLAN v1.2 文档同步 (VAR_INDEX / YAML→dataclass / score_phase3). ✓

---

DELTA_REVIEWER_DONE FAIL_REWORK
