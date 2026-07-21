# SP6 隐性关系抽检 (Rule A) — 清洗后复审

> 审计对象: `data/meta/implicit_relations.json` 当前 30 边 (post anti-fabrication gate)。
> 独立审计 (Rule D 隔离,审计者未参与生成/清洗)。逐条打开 `evidence.source_file` 在标注 `line` 附近逐字核引文,再独立判断引文是否真正支撑有向关系 (域对/方向对/关系真实蕴含,非过度解读)。
> 定位: advisory exploration hint — 有据的暗示性边 PASS;捏造目标域/方向明显错/明显过度解读 FAIL;边界 = WEAK。

边计数 (30 边): {'data_flow': 12, 'explicit_link': 9, 'co_occurrence': 9};被毙: 36 (旧集残留计数,以当前 JSON 为准)

**清洗对照**: 上一版 (stale) AUDIT_FAIL 的三条坏边 `data:FT>LB:0` / `data:MI>EG:0` / `data:RS>TU:0` (目标域捏造/张冠李戴) 在当前集中**已全部移除**。反捏造码闸 "target 必须在 quote 中被点名" 生效。

## N=10 抽检 (data_flow ×8 + explicit_link ×1 + co_occurrence ×1)

> 分层覆盖 5 个域簇 (IS/MI/PR/RS/TU 为源);8 条 data_flow 覆盖 12 条中的多数机制类型 (routing / RELREC / --LNKID / --LNKGRP)。

| # | 边 (id) | 类型 | 引文命中? | 关系/方向对? | 判定与理由 |
|--|--|--|--|--|--|
| 1 | data:IS>LB:21 | data_flow | PASS (逐字命中 IS/assumptions.md L21) | PASS | 引文 "Measurements of cytokines, chemokines, and complement proteins should be represented in the Laboratory Test Results (LB) domain." 显式点名 **LB**;IS 假设把该类测量路由到 LB,方向 IS→LB 作为 routing 提示成立,目标域真实点名。 |
| 2 | data:MI>LB:3 | data_flow | PASS (逐字命中 MI/assumptions.md L3) | PASS | 引文 "Some examinations of cells in fluid specimens ... are classified as lab tests and should be stored in the Laboratory Test Results (LB) domain." 显式点名 **LB**,明确区分显微组织学 (MI) 与流体细胞 lab 检验 (LB);MI→LB 提示成立。 |
| 3 | data:PR>EG:29 | data_flow | PASS (逐字命中 PR/examples.md L29) | PASS | 引文 "The heart rate findings from the procedure are represented in the ECG Test Results (EG) domain." 显式点名 **EG**;心率程序结果→EG,方向 PR→EG 正确。 |
| 4 | data:PR>EG:39 | data_flow | PASS (逐字命中 PR/examples.md L39) | PASS | 引文 "The relrec.xpt reflects a one-to-many dataset-level relationship between PR and EG using --LNKID." **PR、EG 双点名** + 机制 (--LNKID/RELREC) 明确;PR→EG 成立。 |
| 5 | data:PR>MI:10 | data_flow | PASS (逐字命中 PR/assumptions.md L10 段内) | PASS | 引文 "a biopsy may be performed to obtain a tissue sample ... details of the biopsy procedure can be represented in the PR domain and the histopathology findings in the Microscopic Findings (MI) domain." **PR、MI 双点名**;活检 (PR) 供组织→组织病理结果 (MI),方向正确。 |
| 6 | data:RS>CM:27 | data_flow | PASS (逐字命中 RS/assumptions.md L27a) | PASS | 引文 "The record in RS may be related and linked to record(s) in Concomitant/Prior Medications (CM) using CMLNKGRP and RSLNKGRP." **RS、CM 双点名** + 机制;RS→CM link 提示成立。 |
| 7 | data:RS>TR:18 | data_flow | PASS (逐字命中 RS/assumptions.md L18) | PASS | 引文 "The RSLNKGRP variable is used to provide a link between the records in a findings domain (e.g., Tumor/Lesion Results, TR; ...) that contribute to a record in the RS domain." **TR 显式点名** + RSLNKGRP 机制真实。注: 数据流严格看是 TR→RS (findings 贡献于 RS),但 RSLNKGRP 系 RS 域变量指向 findings 域,故 RS→TR 框定可辩护;link 本质双向,advisory 提示成立。(与已移除的坏边 RS>TU 关键差异: TR 系被点名的 findings 结果域,非未点名的 identification 域。) |
| 8 | data:TU>TR:22 | data_flow | PASS (逐字命中 TU/assumptions.md L22) | PASS | 引文 "...relate an identification record in the TU domain to assessment records in the Tumor/Lesion Results (TR) domain." **TU、TR 双点名**;TU 标识记录→TR 评估记录,方向正确。小瑕: 边 `relation` 标签写 "TULNKID" 而引文该句变量为 "TRLNKID" (同段后文另述 TULNKID),属标签措辞,不动核心关系/方向。 |
| 9 | expl:RS>LB:18 | explicit_link | PASS (assumption #4 整段逐字命中 RS/assumptions.md L18) | PASS | 确定性 RELREC 正则通道;引文含 "Records should exist in the RELREC dataset" 及 **LB 显式例** "might require lab results in the LB domain";RS↔LB RELREC (无向) 成立。 |
| 10 | co_o:TR>TU:0 | co_occurrence | N/A (确定性计数 "TR/TU co-mentioned 27x",无散文可逐字核) | PASS | 计数派生非散文引文;TR (肿瘤结果) 与 TU (肿瘤标识) 为强配对,27x 共现完全合理,并被 TU/assumptions L22 交叉引用佐证;无向共现成立。 |

## 总判定

**AUDIT_PASS** — grounding FAIL 0 (8/8 data_flow + explicit_link 引文逐字命中源文件,co_occurrence 为确定性计数 N/A);语义 FAIL 0;语义 WEAK 0。满足门槛 (0 grounding FAIL, ≤1 semantic FAIL, ≤2 WEAK)。

- **无坏边**。抽检的全部 8 条 data_flow 边其目标域均在引文中被**显式点名** (LB/EG/MI/CM/TR),这正是反捏造码闸的设计意图;上一版三条捏造/张冠李戴边 (FT>LB / MI>EG / RS>TU) 已被移除,不在当前集中。
- 两处轻微措辞瑕 (#7 方向为 link 本质双向的名义框定;#8 `relation` 标签 TULNKID vs 引文 TRLNKID),均不影响 grounding 或核心关系真实性,按 advisory 定位保留、无需降级。
- deterministic 通道 (explicit_link RELREC 正则 / co_occurrence 计数) 抽样全部可靠。

结论: 清洗后的 30 边集在本 N=10 独立样本上**语义与 grounding 均健康**,"target 必须在 quote 中点名" 硬校验在样本内 100% 生效,未见残留捏造。
