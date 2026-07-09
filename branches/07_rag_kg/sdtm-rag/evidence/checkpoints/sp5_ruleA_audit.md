# SP5 Rule A 独立核验 — 图增强校验器 (N=6, 实测 8 样本)

> 规则 A 独立科学家审计。目标: 从 **raw meta.yaml** 手算 3 类图增强校验的 EXPECTED 行为,
> 与实现 `server.graph_validator.run_graph_checks(...)` 的 ACTUAL 输出对账。
> **反过拟合纪律**: EXPECTED 侧只 `yaml.safe_load(META)` + 自建反向索引, **不 import
> `server.graph_validator`, 不用 `MetaStore`/`GraphEngine` 算期望**; 这些只在 ACTUAL 侧用。
> 审计人: 独立 subagent (与 writer 异 context)。日期 2026-07-09。

## 0. 方法与独立性

- META 路径: `data/meta/meta.yaml` (经 `settings.meta_path` 取路径, 文件自己 yaml 解析)。
- EXPECTED 侧自建索引 (仅 raw yaml, 复刻 MetaStore 的**唯一**结构性口径 `counts_toward_63==True`
  → 63 real domains; 该口径来自对 yaml 字段的独立阅读, 非调用 MetaStore):
  - `var_to_domains[name] = {含该变量名的 real domain}`
  - `ct_to_domains[code] / ct_to_vars[code] = {绑该 codelist 的 real domain / 变量名}`
  - `relrec_targets[dom]`: 扫 `relations_curated` 全条目, `mechanism=='RELREC'`, 或 back-fill
    `mechanism is None and target∈{RELREC,RELSPEC,RELSUB}` 时 **机制即该 target** (spec §3.2 原话
    「机制即该 target」= 推断为该具体 target 名), 最后只收 `mechanism=='RELREC'` 的。
- ACTUAL 侧: `engine = GraphEngine(MetaStore(settings.meta_path))`; `run_graph_checks({dom: df}, engine)`。
- 比对键: Finding 四元组 `(severity, rule, variable, message)` **逐字全串匹配** (含消息内嵌数字)。

## 1. 独立复算的关键 raw 数字

| 量 | raw yaml 手算值 | 用途 |
|----|----------------|------|
| USUBJID `n_domains` | **55** (≥10) | 高 impact 变量 |
| STUDYID / DOMAIN `n_domains` | 63 / 59 (≥10) | fixture 内高 impact 变量 (副产物) |
| AETERM `n_domains` | **1** (<10), ct_codes=[] | 低 impact 变量 (静默) |
| AESER/MHPRESP/CMPRESP/PRPRESP `n_domains` | 各 **1** (<10) | 变量本身非高 impact |
| C66742 `n_domains` / `n_variables` | **41 / 123** (≥10) | 高 impact codelist ("No Yes Response") |
| AE RELREC targets (spec-precise) | **{CM, PR}** | completeness |
| FA 边 | `mechanism=null`, target=FA∉REL集 → **非 RELREC** | 不触发 (与 attempt_1 一致) |
| 结构列 DOMAIN/STUDYID/USUBJID/xxSEQ 的 ct_codes | 全 `[]` | 无 GCASCADE 噪声 |

**全域扫描 (63 real domains 各单独提交)**: 仅 **AE** 触发 GXDOM (→CM, →PR)。其余 62 域 0 条。

## 2. 六个必核样本 (+2 探针) 期望 vs 实测

EXPECTED 全部由 §1 raw 索引重构字符串 (数字来自手算); ACTUAL 来自 `run_graph_checks`。

| # | 样本 | 输入 (dom→列/值) | EXPECTED (独立 raw) | 实测 | 判定 |
|---|------|------------------|---------------------|------|------|
| C1 | completeness (AE 全缺 target) | {AE: AESER=Y} | GXDOM(AE→CM), GXDOM(AE→PR), +GIMPACT C66742(AESER) | 同 | **PASS** |
| C2 | completeness (AE 缺 PR) | {AE: AESER=Y, CM: CMPRESP=Y} | GXDOM(AE→PR) 单条 (CM 在集内被抑制), +2 GIMPACT C66742 | 同 | **PASS** |
| Ca1 | cascade 冲突 | {CM: CMPRESP∈{Y,N}, MH: MHPRESP∈{U}} | GCASCADE C66742 `CM=['N','Y']; MH=['U']`, +2 GIMPACT | 同 | **PASS** |
| Ca2 | cascade 一致 | {CM: CMPRESP=Y, MH: MHPRESP=Y} | 无 GCASCADE (静默), 仅 2 GIMPACT C66742 | 同 | **PASS** |
| I1 | impact 高变量 | {DM: USUBJID} | GIMPACT USUBJID "appears in **55** domains" | 同 | **PASS** |
| I2 | impact 低变量 | {DM: AETERM} | 无 finding (AETERM=1<10, 不绑 CT) | 空 | **PASS** |
| I3 | impact 高 codelist | {MH: MHPRESP=Y} | GIMPACT "C66742 … **41** domains / **123** variables" (via MHPRESP) | 同 | **PASS** |
| C3 | back-fill 探针 (BS→RELSPEC) | {BS: BSSEQ} | spec-precise: RELSPEC≠RELREC → **静默** | 空 | **PASS** |

八样本 4 元组 (含消息全串) **全等**, 无一 mismatch。要求的 N=6 (2 completeness + 2 cascade + 2 impact)
已覆盖, 另含高 impact codelist (I3) + back-fill 探针 (C3) 两项额外核。

## 3. completeness back-fill 语义: 一处需披露的判定 (非缺陷)

任务 prompt 规则 #1 的措辞「A relation counts as RELREC if … OR (back-fill) mechanism is null AND
target∈{RELREC,RELSPEC,RELSUB}」若**字面直读**, 会把 null-mech 且 target=RELSPEC 的边也当 RELREC。
raw yaml 中 **BS/IS/LB/MB/MS** 各有一条 `mechanism=null, target=RELSPEC` 边:

| 域 | prompt-字面读 会 flag | 实现实际 fired |
|----|----------------------|----------------|
| BS/IS/LB/MB/MS | RELSPEC (各 1 条 GXDOM) | **NONE** (静默) |

**判定: 实现正确, prompt #1 属宽松转述, 不是代码 bug。** 依据:
1. **权威 spec §3.2 原文**「target∈{RELREC,RELSPEC,RELSUB} 时机制即该 target」— 用「该 target」
   (RELSPEC→RELSPEC) 而非「即 RELREC」, 刻意保留三者区分; 随后只有 `mechanism=='RELREC'` 入
   RELREC-linked 集。实现 `mech=target; if mech=='RELREC'` 精确复刻此语义。
2. spec §1 硬约束「全 advisory / 避免误报 / curated LOW fidelity 不可 hard-fail」— 把 RELSPEC/RELSUB
   也报会增假阳, 与保守基调相悖。
3. back-fill 的 RELREC 分支仅当存在 `target=='RELREC'` 的 null-mech 边才激活; 全 meta.yaml **无**
   此类边 (52 条 curated 关系中 mechanism 计数 = {null:50, RELREC:2}, target 落 REL 集者全是 RELSPEC),
   故该分支对当前数据**休眠但防御性正确**。

**风险披露 (给产品判定, 非本次 gate 项)**: 若业务意图是「任何指向关系数据集 (RELSPEC/RELSUB) 的链接
也应提示」, 则当前 BS/IS/LB/MB/MS 的 RELSPEC 缺失**不会**被 completeness 捕获。此为设计口径选择,
建议在 KG_ROADMAP/SP5 段留一句 known-scope 说明。当前实现与 spec 一致 → 不判 FAIL。

## 4. fixture 金样交叉核 (绑定 spec §4 验收)

- **pass study `{AE,CM,PR}`** (attempt_1 修正 E 的 RELREC-闭合集): graph-WARN = **0** ✓
  (仅 INFO/GIMPACT: STUDYID/DOMAIN/USUBJID + C66742×3, 全 advisory)。
- **fail study `{AE,MH}`**: graph-WARN = **3** ✓, 精确命中
  GXDOM(AE→CM) + GXDOM(AE→PR) + GCASCADE C66742 `AE=['N','Y']; MH=['U']`。
  (spec §4 文字写「缺 FA→WARN」是松散表述; 真 RELREC 边为 CM/PR, FA 是 null 边不触发 — 与 attempt_1
   披露一致, 实现跟 meta.yaml 真值走, 正确。)

## 5. 结论

**Rule A 判定: PASS。**

- 6 必核样本 (+2 探针) 的独立 raw-yaml 期望与 `run_graph_checks` 实测**四元组逐字全等**, 零 mismatch。
- 关键数字独立复核无误: USUBJID=55, AETERM=1, C66742=41 域/123 变量, AE RELREC={CM,PR}。
- impact (阈值 10, INFO, 变量+codelist 双通道)、completeness (仅 AE 触发, GXDOM WARN)、
  cascade (共享 codelist 值集对称差, GCASCADE WARN) 三类语义与 raw 数据一致。
- 唯一需披露项: completeness back-fill 对 RELSPEC/RELSUB **有意不报** — 经查证符合 spec §3.2 精确措辞
  与 advisory 硬约束, **属正确设计口径, 非缺陷** (prompt 规则 #1 为宽松转述)。已就潜在业务口径给出建议。
