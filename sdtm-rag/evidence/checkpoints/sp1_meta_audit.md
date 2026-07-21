# SP1 `meta.yaml` — N=8 Rule A 语义抽检证据

> 日期: 2026-06-17
> 审计者: independent agent (Rule D 隔离 — 与生成器 / reconciler 异 subagent，非同 context 自审)
> 被审产物: `branches/07_rag_kg/sdtm-rag/data/meta/meta.yaml` (21138 行, 64 域)
> 真源 (只读): `knowledge_base/domains/<D>/spec.md` · `terminology/**/*.md` · `model/*.md`
> 方法: 逐槽打开 meta.yaml 条目 ↔ 打开 source，逐字段手核。结构/计数检查已过 Gate 1 (下方)，本文档专核结构检查看不见的**语义层**。

---

## Gate 1 — 独立锚计数对账 (`scripts.reconcile_meta`)

reconciler 从 `VARIABLE_INDEX.md` / `INDEX.md` 文本独立复现计数 (不复用生成器 spec_loader)。原始输出：

```
[OK ] domains_counts_toward_63: expected=63 actual=63
[OK ] variable_entries_total: expected=1917 actual=1917
[OK ] unique_variable_names: expected=1523 actual=1523
[OK ] codelists_total: expected=1005 actual=1005
[OK ] terms_total: expected=37939 actual=37939
[OK ] TAETORD_domain_count: expected=43 actual=43
[OK ] VISITDY_domain_count: expected=36 actual=36
[OK ] raw_order_line_count: expected=1917 actual=1917
```

全 8 断言 OK。结构层 PASS。注意：结构 PASS ≠ 语义 PASS，下方为独立语义核验。

辅助全局不变量 (python 全表扫描)：
- 每域 `same_class` 成员**全部与该域同 class**，无自引用 → `errors: NONE`
- 每条 `relations_curated.target` 都是已知域 (无悬挂边) → `unknown target: NONE`
- 每个被变量引用的 `ct_codes` 元素都存在于 `codelists` 段 (无孤儿码) → `orphan: NONE`
- `mechanism` 全表分布 `{null: 50, RELREC: 2}` (与设计 §6「全 52 策划边仅 2 条非 null」逐字一致)
- `fidelity` 全表只取 `curated_prose` 一个值
- `scripts/tests/test_build_meta.py`：13 passed

---

## 逐槽 N=8 Rule A 抽检

### Slot 1 — TE (tiny, Trial Design) · **PASS**
meta L19457-19526 vs `domains/TE/spec.md`。
- class=`Trial Design` / label=`Trial Elements` / structure=`One record per planned Element` — 全对 (spec L1-3)。
- same_class=`[TA,TD,TI,TM,TS,TV]` — 全 Trial Design，含自身排除 — 对 (spec L72 同类 bullet)。
- 7 变量逐字对 spec：STUDYID(Id/Req), DOMAIN(Id/Req), ETCD(Topic/Req), ELEMENT(Synonym Qualifier/Req), TESTRL(Rule/Req), TEENRL(Rule/**Perm**), TEDUR(Timing/**Perm**, ct_dict=[ISO 8601 duration])。Type/Role/Core 全对。
- relations_curated: 1 条 target=TA, category=`Trial Design`, mechanism=**null**, note="elements compose arms" — 散文 (spec L73「elements compose arms」) 无机制词 → null 正确，**未臆造**；"Same class" bullet 正确未进 relations_curated。

### Slot 2 — TD (tiny, Trial Design) · **PASS**
meta L19377-19456 vs `domains/TD/spec.md`。
- class=`Trial Design` / label=`Trial Disease Assessments` / structure=`One record per planned constant assessment period` — 全对。
- same_class=`[TA,TE,TI,TM,TS,TV]` — 全 Trial Design — 对。
- 9 变量逐字对 spec：STUDYID, DOMAIN, TDORDER(Num/Timing/Req), TDANCVAR(Char/Timing/Req), TDSTOFF/TDTGTPAI/TDMINPAI/TDMAXPAI (Char/Timing/Req, 均 ct_dict=[ISO 8601 duration]), TDNUMRPT(Num/Record Qualifier/Req)。全对。
- relations_curated=`[]` — TD spec 只有 same-class bullet 无跨类 — 正确。

### Slot 3 — VS (medium, Findings) · **PASS**
meta (38 vars) vs `domains/VS/spec.md`。
- class=`Findings` / label=`Vital Signs` / structure=`One record per vital sign measurement per time point per visit per subject` — 全对 (spec L1-3)。
- same_class=29 域，**全部 Findings 类**，= (全 30 Findings 域 − VS 自身)，自身正确排除 — 校验脚本确认无非 Findings 成员。
- 抽 ~7 变量对 spec：前 6 (STUDYID/DOMAIN/USUBJID/VSSEQ/VSGRPID/VSSPID) 全对；VSTESTCD(ct=**C66741**, Topic/Req — spec L63), VSTEST(ct=**C67153**, Synonym Qualifier/Req — spec L72), VSPOS(ct=**C71148**, Record Qualifier/Perm — spec L99), VSORRESU(ct=C66770/Variable Qualifier/Exp)。ISO 时间型 (VSDTC/VSELTM/VSRFTDTC) 正确进 ct_dict 而非 ct_codes。

### Slot 4 — LB (large, Findings) · **PASS**
meta (62 vars) vs `domains/LB/spec.md` + terminology。
- class=`Findings` / label=`Laboratory Test Results` / 62 变量 / same_class 全 Findings。
- LBTESTCD ct=`[C65047]` (spec L70, Topic/Req) → codelists 解析 = "Laboratory Test Code" (terminology/core/lb_part2.md, n=2536)。
- LBTEST ct=`[C67154]` (Synonym Qualifier/Req) → "Laboratory Test Name" (lb_part3.md, n=2536)。
- LBSTRESC ct=`[C102580]` (spec L205, Result Qualifier/Exp) → "Laboratory Test Standard Character Result" (lb_part4.md, n=6)。
- 全表孤儿码检查：所有 64 域所有变量的 ct_codes 均存在于 codelists 段 — **零孤儿**。

### Slot 5 — DM (special-purpose) · **PASS**
meta L8244-... (32 vars) vs `domains/DM/spec.md`。
- class=`Special-Purpose` / label=`Demographics` / structure=`One record per subject` — 全对。
- 32 变量 = spec 32 个 `Order:` 行 (spec 的 36 个 `###` 含 Cross-Refs 子标题，不可用)。
- same_class=`[CO,SE,SM,SV]` — 全 Special-Purpose，DM 自身正确排除 — 对。
- ct-bearing 变量逐一对 spec：DTHFL=C66742, AGEU=C66781, SEX=C66731, RACE=C74457, ETHNIC=C66790, ARMNRS=C142179 — 全对 (spec L126/180/189/198/207/252)。
- 前 14 变量 (STUDYID..DTHFL) Type/Role/Core 全对。relations_curated=`[]` (DM spec 仅 same-class bullet)。

### Slot 6 — RELREC (relationship) · **PASS**
meta L16990-17052 vs `domains/RELREC/spec.md`。
- class=`Relationship` / label=`Related Records` / structure=`One record per related record, group of records or dataset` — 全对。
- same_class=`[RELSPEC,RELSUB,SUPPQUAL]` — 全 Relationship — 对。
- 7 变量逐字对 spec：STUDYID(Req/Id), **RDOMAIN**(Req/Id, ct=C66734), USUBJID(Exp/Id), **IDVAR**(Req/Id), IDVARVAL(Exp/Id), **RELTYPE**(Exp/Record Qualifier, ct=C78737), RELID(Req/Record Qualifier)。RDOMAIN/IDVAR/RELTYPE 均在且正确。
- `model_defhome["RDOMAIN"] == "model/06_relationship_datasets.md"` (meta L21111) — **对**。

### Slot 7 — DI vs SUPPQUAL 边界 (corrected one) · **PASS**
真源核实：磁盘 `domains/DI/` 仅 `assumptions.md` (无 spec.md)；`domains/SUPPQUAL/` 有 spec/assumptions/examples 且在 `INDEX.md` L134。
- **DI 桩** (meta L8235-8243)：class=`''`, counts_toward_63=**false**, is_special=**true**, label=`''`, structure=`''`, variables=**[]**, relations_curated=**[]**, same_class=**[]** — 完美桩，与「DI 只有 assumptions.md」一致。
- **SUPPQUAL** (meta L19064-19147)：is_special=**false**, counts_toward_63=**true**, class=`Relationship`, label=`Supplemental Qualifiers for [domain name]`, structure=`One record per supplemental qualifier per related parent domain record(s)`。10 变量全对 spec.md：STUDYID, RDOMAIN(ct=C66734), USUBJID, IDVAR(Exp), IDVARVAL(Exp), **QNAM**(Topic/Req), **QLABEL**(Synonym Qualifier/Req), **QVAL**(Result Qualifier/Req), QORIG(Record Qualifier/Req), QEVAL(ct=C78735, Exp)。QNAM/QLABEL/QVAL/RDOMAIN/IDVAR 全部在且正确。

### Slot 8a — 多码变量 DS.DSDECOD · **PASS**
meta vs `domains/DS/spec.md` L77-84。
- spec L81 `Controlled Terms: C66727; C114118; C150811` (3 码) → meta `ct_codes: [C66727, C114118, C150811]` — 分号切分顺序全对，**恰 3 码**。
- DSDECOD role=Synonym Qualifier, core=Req, type=Char — 对。
- 3 码全解析到真 codelist (terminology/core/disposition.md)：C66727=Completion/Reason for Non-Completion(n=37), C114118=Protocol Milestone(n=4), C150811=Other Disposition Event Response(n=**0**)。C150811 term_count=0 已回真源核实：disposition.md L59-61「## Other Disposition Event Response (C150811) / Extensible: Yes」**无 term 表** → 0 为真值非漏解析。

### Slot 8b — AE relations_curated 机制不臆造 · **PASS**
meta L5033-5048 vs `domains/AE/spec.md` L558-562。
- spec L560 `**Findings About:** [FA] — prespecified AE findings (AEPRESP)` → meta target=FA, category=`Findings About`, mechanism=**null** (散文无机制词) — **未发明机制**。
- spec L561 `**Treatment:** [CM] — concomitant medications linked via RELREC` → meta target=CM, mechanism=**RELREC** (字面有 "via RELREC")。
- spec L562 `**Treatment:** [PR] — procedures linked via RELREC` → meta target=PR, mechanism=**RELREC**。
- spec L559 `**Same class (Events):** ...` → 正确**未**进 relations_curated；改进 same_class=[BE,CE,DS,DV,HO,MH]。

---

## 完整性核查 (vs 设计 §3 + SP2/SP3 需求)

| 检查项 | 结果 |
|--------|------|
| 顶层键 = {meta_version, generated_from, domains, codelists, model_defhome} | ✅ 全在 (§3 schema) |
| domain 字段集 = {domain,class,label,structure,is_special,counts_toward_63,variables,same_class,relations_curated} | ✅ 64 域无缺字段 |
| variable 字段集 = {name,label,role,type,core,ct_codes,ct_dict} | ✅ |
| relation 字段集 = {target,category,mechanism,note,fidelity} | ✅ |
| codelist 字段集 = {ct_code,name,extensible,term_count,termfile} | ✅ |
| SP2 计数锚：TAETORD→43 / VISITDY→36 (Gate 1) | ✅ |
| SP2 exact-lookup：ct_code→codelist 全解析 (零孤儿) | ✅ |
| SP3 关系线索：relations_curated 标 fidelity=curated_prose，mechanism 仅字面 | ✅ (50 null / 2 RELREC) |
| model_defhome 退役 structured_lookup 依据 (含 TAETORD) | ✅ 59 条 (设计本就只映 model 章节引入的变量，非全 1523) |

**gap / findings**：无 Rule A FAIL。一处**非缺陷的设计说明**记录在案——`model_defhome` 仅 59 条而非覆盖全部 1523 变量；这与设计 §3 一致 (它只映 `model/*.md` 章节定义动词锚引入的变量，是 structured_lookup 退役所需的最小集)，不是漏数据。另注：设计 §3 schema 示例里 C66742 写 `term_count: 2`，实测真值为 4 (N/NA/U/Y, general_part4.md L11-14)——示例是示意占位，meta.yaml 取的是真值 4，正确。

---

## 总判定 — **PASS**

8 个分层槽全部 PASS，逐字段手核无 invented 机制 / 无错码 / 无漏数据 / 无计数错。Gate 1 (8 断言) + 全局不变量 (same_class 同类、无悬挂边、无孤儿码、mechanism 分布吻合设计) + 13 单测全过。meta.yaml 语义层经独立 (Rule D) 抽检确认与 KB 真源一致，可作为 SP2 (计数/精确查) + SP3 (关系) 的硬前置。

> meta.yaml 与 scripts/ 在本次审计中保持只读未改动 (git status clean)。
