# SP5 attempt 1 — plan data-assumption corrections (pre-implementation verification)

> 规则 B 归档。SP5 plan (`docs/superpowers/plans/2026-07-09-sp5-graph-validator.md`)
> 在写码前假定了若干 meta.yaml 事实。开工前用 `MetaStore`/`GraphEngine` 逐条实测,
> 抓出 **1 个会导致测试失败的错误假设** + 2 个需澄清项。按 plan「不许改实现去凑,
> 改测试期望 + 归档」的纪律记录。

## 输入 (plan 假设) → 实测 → 判定

| # | plan 假设 | 实测 (meta.yaml via MetaStore) | 判定 |
|---|-----------|-------------------------------|------|
| A | Task 2/4: `MHSER` 绑 codelist `C66742`, 与 `AESER` 组跨域一致性对 | `ct_codes_for_variable("MHSER")` = **`[]`** (MHSER 不绑任何 codelist); `AESER`=`['C66742']` | **错误** → 换变量 |
| B | Task 1: `AE` 经 RELREC 关联 `CM` | AE `relations_curated` = FA(mech=**null**) / **CM(mech=RELREC)** / **PR(mech=RELREC)** | 部分: CM 对, 但还有 PR; 且 spec §4 写的 FA 是 null 边非 RELREC |
| C | Task 3: `USUBJID` n_domains≥10 高 impact; `AETERM` 低 impact | `impact_of_variable`: USUBJID=**55**, AETERM=**1** | 正确 |
| D | cascade 遍历所有列, 结构列 (DOMAIN/STUDYID/USUBJID/SEQ) 不应制造噪声 | 4 列 `ct_codes_for_variable` 全 = `[]` (不绑 codelist) | 正确 (无 GCASCADE 噪声) |

## 修正 A (唯一实质改动)

`MHSER` 不绑 codelist → 无法与 AESER 组成跨域共享 codelist 对。实测同绑 `C66742`
("No Yes Response", 41 域/123 变量) 的干净变量:
`AEPRESP`/`AESER` (AE), **`MHPRESP` (MH)**, `CMPRESP` (CM)。

**决定**: cascade 测试 + fixture 用 **`AESER` (AE) + `MHPRESP` (MH)** 组对 (均绑 C66742)。
不改 `check_ct_cascade` 实现逻辑, 只改测试/ fixture 里的变量名 (plan Task 2/4 明确允许)。

## 澄清 B (无需改测试)

Task 1 测试断言 `any("CM" in message)` + `all(severity=="WARN")`。AE 的 RELREC target 实为
{CM, PR} 两个 → `check_completeness({"AE"})` 产 2 条 GXDOM (CM, PR), 两断言仍成立。
`test_completeness_silent_when_target_present({AE, CM})` 抑制 CM finding, 残留 PR finding
(message 不含 "CM") → `not any("CM" in message)` 仍成立。**Task 1 测试逐字保留, 不改。**

## 修正 E (Task 4 fixture — pass study 必须 RELREC-闭合)

plan Task 4 pass study = `{AE, CM, MH}`, 期望 0 GXDOM。但 **AE 的 RELREC target = {CM, PR}**
(修正 B), PR 不在集合 → `check_completeness` 会对 PR 报 GXDOM → pass 版误报, golden FAIL。
plan 选 {AE,CM,MH} 基于「AE 只关联 CM」的错误假设。

**决定**: pass study 改 **`{AE, CM, PR}`** (RELREC-闭合: AE→CM✓ AE→PR✓; CM/PR/无 RELREC 出边)。
cascade 一致性用 3 域共绑 C66742 的 `AESER`(AE)/`CMPRESP`(CM)/`PRPRESP`(PR) 全 = `Y` → 一致 → 0 GCASCADE
(主动测「共享 codelist 一致→静默」路径, 非靠 codelist 缺席蒙混)。fail study 保持 plan 的 `{AE, MH}`
(缺 CM → GXDOM; AESER{Y,N} vs MHPRESP{U} → GCASCADE)。

## Task 3 fixture typo (plan)

plan Task 3 两处测试 DataFrame 列长不齐 (`{"DOMAIN":["AE"], "AESER":["Y","N"]}` → pandas ValueError),
且 merge 测试用 MHSER(不绑) → GCASCADE 不触发。已修: 列补齐 + MHSER→MHPRESP。属 plan 笔误, 非实现缺陷。

## 结论

无实现逻辑缺陷; 全部属「plan 写码期数据假设/ fixture 形状」与 meta.yaml 真值对齐。改动集中在
**测试/fixture 数据** (MHSER→MHPRESP; pass study {AE,CM,MH}→{AE,CM,PR}; 列长补齐), **实现逻辑一字未改去凑测试**。
后续 Rule A (Task 8) 用独立码路 (raw meta.yaml) 复核 impact/completeness/cascade 期望。
