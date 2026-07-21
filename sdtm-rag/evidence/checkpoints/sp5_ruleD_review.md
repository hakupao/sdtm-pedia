# SP5 图增强校验器 — Rule D 独立审查

> 审查者: Rule D 独立 lane (异 subagent, 非实现者)。日期 2026-07-09。
> 范围: `git diff 2d5b5b9..HEAD -- branches/07_rag_kg/sdtm-rag/` (14 文件, +535 行)。
> 参照: spec `docs/superpowers/specs/2026-07-09-sp5-graph-validator-design.md` ·
> plan `docs/superpowers/plans/2026-07-09-sp5-graph-validator.md` ·
> 实现者数据修正 `evidence/failures/sp5_attempt_1.md`。
> 所有测试/lint/type 均本人独立复跑, 下附真实输出。

## 裁决: **APPROVE_WITH_NITS**

无 BLOCKER, 无 HIGH。1 条 MED (back-fill 语义与 spec 散文有分歧, 但方向安全、纯 advisory),
若干 LOW。SP5 可收口; MED/LOW 建议在 `sp5_summary.md` 诚实缺口段落记录, 或按下方选项择一修正。

**核心不变量全部成立**:
- advisory-only: graph findings 只可能是 WARN/INFO, **构造上无 ERROR 路径** (证据见 F1)。
- 单域 `/validate` **零回归**: 493 全绿; router.py/report.py 纯追加 (28/0, 53/0 numstat);
  单域 `validate_dataset` 函数体逐字节未变; 无任何 pre-existing 测试文件被改。
- 确定性: 只读内存 GraphEngine/MetaStore, 无 Neo4j / LLM import。
- 诚实性: 实现者的 lint/type 债务声明**逐条属实, 甚至偏保守** (见 §诚实核验)。

---

## 证据 (本人复跑)

```
$ .venv/bin/python -m pytest scripts/tests/ -q
493 passed, 1 warning in 17.39s

$ .venv/bin/mypy server/graph_validator.py
Success: no issues found in 1 source file

$ .venv/bin/ruff check server/graph_validator.py + 4 个新测试文件
All checks passed!

$ git diff 2d5b5b9..HEAD --numstat server/router.py server/report.py
28  0  server/report.py      # 纯追加
53  0  server/router.py      # 纯追加
$ diff (旧 vs 新 router.py 520-600 行)  → IDENTICAL (单域端点未动)
$ git diff --stat 测试文件  → 仅 3 个新文件, 无 pre-existing 测试被触碰
```

---

## Findings (按严重度)

### BLOCKER: 无
### HIGH: 无

### MED

**M1 — completeness back-fill: `_RELATIONSHIP_DATASETS` 的 RELSPEC/RELSUB 成员实为死码, 与 spec 散文产生静默 false-negative**
`server/graph_validator.py:13, 26-28`

```python
_RELATIONSHIP_DATASETS = {"RELREC", "RELSPEC", "RELSUB"}
...
if mech is None and target in _RELATIONSHIP_DATASETS:
    mech = target                       # RELSPEC 边 → mech="RELSPEC"
if mech == "RELREC" and target not in submitted:   # ← 只认 RELREC
```

back-fill 把 `mech` 设为 target 名, 但随后守卫是 `mech == "RELREC"`。因此:
- target=="RELREC" 且 mech=None → back-fill 后可触发 (meta.yaml 中此类边 **0 条**)。
- target=="RELSPEC"/"RELSUB" 且 mech=None → back-fill 后 mech="RELSPEC"/"RELSUB", **永不满足守卫**。

我对 meta.yaml 全域实测 (independent, 未 import graph_validator):
- 显式 RELREC 边: **仅 2 条** (AE→CM, AE→PR) — completeness 的全部活跃面。
- mech=None 且 target∈REL 的 back-fill 边: **5 条, 全部 target=RELSPEC** (BS/IS/LB/MB/MS)。
- 即: back-fill 当前对真实数据 **净效果为零**; 且提交 LB 而缺 RELSPEC → spec §3.2 散文
  ("back-fill: target∈{RELREC,RELSPEC,RELSUB}… 若 target∉S → Finding") 暗示应 WARN, 实现**静默**。

失败场景: 用户上传 {LB} (LB curated 关系含 mech=None→RELSPEC), 未附 RELSPEC 数据集。
按 spec 散文预期一条 GXDOM advisory; 实现不产 finding (false-negative, 影响 5 域)。

影响评级 MED 而非 HIGH: 纯 advisory (无 ERROR、不影响 pass/fail、不回归、不崩溃); 方向是**保守**
(少报而非多报); tests/golden 只覆盖 RELREC 故全绿。属"spec 散文 vs 实现契约"分歧 + 集合冗余成员。

建议 (二选一, 均可, 且请在 summary 诚实缺口段记录):
- (a) **收窄**: 从 `_RELATIONSHIP_DATASETS` 删 RELSPEC/RELSUB (只留 RELREC), docstring/spec 明确
  "completeness 仅覆盖 RELREC", back-fill 仅归一化 null→RELREC 边 (当前 0 条, 属防御性)。—— 最小改动, 与 tests 一致。
- (b) **放宽**: 守卫改 `if mech in _RELATIONSHIP_DATASETS and target not in submitted`, 使 RELSPEC/RELSUB
  完整性也生效; 需补一条 RELSPEC 域测试 + 重算 fail-fixture 期望。—— 若确实想要 RELSPEC/RELSUB 完整性。

### LOW

**L1 — 端点 `semantic_review` 参数声明但从不使用 (死参 / 误导性 API 面)**
`server/router.py:608` 声明 `semantic_review: str = Form("false")`, 函数体从不引用它, `review=None` 硬编码。
客户端传 `semantic_review=true` 会被静默忽略、无任何语义审查也无报错。建议删除该参数, 或加注释说明
study-level 刻意不做 per-domain semantic review (spec §5 已把 webchat 暴露/语义审查列范围外, 保留死参无必要)。

**L2 — 每请求重建 GraphEngine/MetaStore (轻微性能)**
`server/router.py:648` `engine = GraphEngine(MetaStore(settings.meta_path))` 每次 `/validate-study`
都重解析 meta.yaml。校验端点非热路径, 可接受; 若后续频繁调用可考虑缓存到 `app.state`。不阻塞。

**L3 — impact INFO 对通用标识列必然刷屏 (设计内噪声)**
实测 STUDYID n_domains=63 / DOMAIN=59 / USUBJID=55, 均 ≥ 阈值 10。故**任何** study 都会为这 3 列
各产 1 条 GIMPACT INFO。属 advisory INFO 设计意图 (不影响 pass/fail), 非误报; 但 UI 上可能淹没真正有用的
高 impact 提示。建议 report/UI 对 identifier 类高 impact 折叠或去重展示。不阻塞。

**L4 — plan 反复引用的 "test_validator.py 37 测试" 文件不存在**
plan Global Constraints + Task 6 Step4 均写 "现有 test_validator.py 37 测试必须仍绿", 但
`scripts/tests/` 下**无** `test_validator.py` (单域 `validate()` 仅在 test_report_study/新测试中间接触及)。
零回归结论**仍成立**, 但依据应改为更强的实证: 493 全绿 + 无 pre-existing 测试被改 + 单域端点字节未变。
属 plan 文档不实, 无代码影响; 收口 RETROSPECTIVE 应订正此说法, 别沿用不存在的门。

**L5 — cascade 比对的是"共享同一 codelist 的不同变量"的值集合, 合法覆盖差异会 WARN**
`server/graph_validator.py:37-63` 对绑定同一 ct_code 的**跨域不同变量** (如 AESER vs MHPRESP 均绑 C66742)
比较 distinct 值集合, 不同即 WARN。docstring 已诚实标注 "different coverage is legitimate, hence WARN not ERROR"。
可接受 (advisory), 但误报面真实存在: AE 用到 {Y,N}、MH 该窗口只出现 {Y} 即触发。建议在 summary/UI 明确
"cascade 为提示性、覆盖差异非错误"。已文档化, 不阻塞。

---

## 七项审查重点逐条结论

**1. advisory-only 不变量 — PASS (构造级保证)。**
`server/graph_validator.py` 全部 4 处 `Finding(...)` 首参严格为字面量:
- `:30` GXDOM → `"WARN"`  · `:60` GCASCADE → `"WARN"`  · `:82`/`:93` GIMPACT → `"INFO"`。
无变量化 severity、无分支可产 "ERROR"。`run_graph_checks` 仅做 list 拼接。
`generate_study_json` (report.py) 里 `g_err = sum(... if f.severity=="ERROR")` 对 graph findings 恒为 0 →
graph 侧永不把 study_verdict 推到 FAIL; study FAIL 只来自既有单域 validate() 的真实 ERROR (合规且预期)。
grep `error|neo4j|llm` 在 graph_validator 仅命中 docstring 文字。**无任何 ERROR 路径。**

**2. check_ct_cascade 误报面 — 可接受且已文档化; 无结构列噪声 bug。**
独立实测: `ct_codes_for_variable` 对 STUDYID/DOMAIN/USUBJID/AESEQ/MHSEQ/CMSEQ/PRSEQ **全 = []** →
结构列不绑 codelist, 不进 cascade, 无噪声 (与 attempt_1 修正 D 一致)。合法覆盖差异触发 WARN 属设计
(见 L5), docstring 显式承认。无"遍历所有列却把结构列算进去"的缺陷。

**3. completeness back-fill 逻辑 — 对 AE→CM/PR 正确; target 在场时正确静默; 但见 M1 的 RELSPEC/RELSUB 死码。**
- AE→CM (mech=RELREC): 缺 CM → WARN; 有 CM → 静默。✓ (测试 + 我复跑确认)
- AE→PR (mech=RELREC): 同上, 且 fail study {AE,MH} 正确同时产 CM+PR 两条 GXDOM。✓
- AE→FA (mech=None, target=FA∉REL): 不 back-fill、不 WARN, 正确回避 null 边误报。✓
- **无 false-positive** (当前 back-fill 净产 0 warning)。RELSPEC/RELSUB false-negative → M1。

**4. 单域 /validate 零回归 — PASS。** 全套 **493 passed** (含所有 pre-existing)。
router.py/report.py 纯追加 (numstat 28/0、53/0); 单域 `validate_dataset` 函数体逐字节 IDENTICAL;
无 pre-existing 测试文件被 diff 触碰。(注: plan 所称 test_validator.py 不存在 → L4。)

**5. 端点错误处理 — PASS。**
- 缺 DOMAIN 列 → 422: `router.py:632-635` `if not dom: raise HTTPException(422, ...)`;
  `test_validate_study_missing_domain_column_422` 复跑通过。✓
- ParseError → 422 且带 `from e`: `router.py:628` `raise HTTPException(422, ...) from e`。✓
- 文件读取: `await uf.read()` 逐文件顺序读, async 正确, 无泄漏/竞态。✓

**6. lint/type 诚实性 — PASS (见下节, 声明属实且偏保守)。**

**7. spec 符合性 — PASS。** 六条锁定决策全落:
Q1 完整 3 类 ✓ · Q2 impact advisory (实现为 INFO-only; spec 允许 INFO/WARN, 取子集更保守、零误报, 符合意图) ·
Q3 新 study 端点、单域不动 ✓ · Q4 无 Neo4j (diff 无 neo4j/LLM import) ✓ · Q5 合成 fixture ✓ ·
Q6 back-fill 仅 SP5-local 内存推断、未写回 meta.yaml ✓。
范围外 §5 全部尊重: 无 Neo4j、无 webchat 暴露 (仅 router+streamlit)、无 per-domain attr、back-fill 不落盘。

---

## 诚实核验 (审查重点 6)

实现者声明: "report.py/router.py 有 pre-existing ruff/mypy 债; SP5 自身新增干净, 仅 1 个
idiomatic B008 (`files: list[UploadFile] = File(...)`)"。**独立复核结论: 属实, 甚至偏保守。**

同一 in-project ruff 配置下 base(2d5b5b9) vs HEAD:
- **router.py: 11 → 12 (+1)**。新增唯一违规 = `B008 @ :607` (`files: list[UploadFile] = File(...)`),
  与 pre-existing `:524`/`:526` 的 File(...) idiom 完全同型。新函数 (602-655) 内无其它违规 (import 已排序、
  ParseError 已 `from e`)。**恰好 1 条新违规, 与声明字字相符。**
- **report.py: 5 → 4 (−1)**。新函数 `generate_study_json` 引用了 `Finding`, 消除了 base 里
  `F401 Finding imported but unused (@ :12)`。新函数**零新违规**, 反而顺手清了一条旧死 import。
- mypy: graph_validator **clean**; report.py 6 error 全在 `:113-122` (既有 SemanticFinding 处理),
  **不在** generate_study_json (157+); router.py 仅一条 `annotation-unchecked` NOTE (既有)。SP5 新增 mypy error = 0。

无夸大、无隐瞒。诚实性通过。

---

## 结论
SP5 实现可靠, 三大不变量 (advisory-only / 单域零回归 / 确定性无 Neo4j) 均以构造级或实证级证据成立,
诚实性核验通过。唯一实质发现 M1 是纯 advisory 方向的 spec-散文 vs 实现分歧 (RELSPEC/RELSUB 死码 +
静默 false-negative), 不阻塞收口, 建议按 (a)/(b) 择一了结并写入诚实缺口。LOW 项择机清理。

**裁决: APPROVE_WITH_NITS。**
