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

## 结论

无实现逻辑缺陷; 属数据假设与真值对齐。仅 MHSER→MHPRESP 一处测试/fixture 变量替换。
后续 Rule A (Task 8) 会用独立码路 (raw meta.yaml) 复核 impact/completeness/cascade 期望。
