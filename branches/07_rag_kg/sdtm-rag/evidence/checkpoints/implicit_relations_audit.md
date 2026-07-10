# SP6 隐性关系抽检 (Rule A)
> 生成: 见 git;域: CM, EG, FT, IS, LB, MI, PR, RS, TR, TU
边计数: {'co_occurrence': 9, 'data_flow': 24, 'explicit_link': 16};被毙: 36

## N=8 分层抽检
> 独立审计 (Rule D 隔离,未参与生成)。每条边独立打开 `evidence.source_file` 逐字核引文,再判断引文是否真正支撑有向关系。
> 分层: data_flow ×6 (最高风险,含 3 条 well-grounded 对照 + 3 条可疑) + explicit_link ×1 + co_occurrence ×1。

| # | 边 (id) | 类型 | 引文命中? | 关系/方向对? | 判定与理由 |
|--|--|--|--|--|--|
| 1 | data:FT>LB:0 | data_flow | PASS (逐字在 FT/assumptions.md,实际 L11;JSON 记 L3 行号偏) | **FAIL** | 引文只提 "FT and QS domains ... Clinical Classifications use case of RS"。QRS 家族=Questionnaires/Ratings/Scales,**不含 LB**;LB(Laboratory)从未出现。verify_note "QS which includes LB under QRS" 事实错误。目标域 LB 被凭空捏造。 |
| 2 | data:MI>EG:0 | data_flow | PASS (逐字在 MI/assumptions.md L3) | **FAIL** | 引文 "microscopic examination of tissue samples" 全程未提 EG;该段实际把 MI 与 **LB**(lab tests)区分,不是 EG(心电图)。EG 与显微组织学无任何关系,目标域捏造(疑似把 LB 误写成 EG)。 |
| 3 | data:EG>LB:0 | data_flow | PASS (逐字在 EG/assumptions.md L18) | WEAK | 引文述 EGNRIND/EGORNRLO/EGORNRHI/EGCLSIG 引用 "Section 4.5.5 ... Findings Observation Class"。这是 Findings 类通用 --NRIND/--ORNRLO/HI/--CLSIG 模式,LB 确有对应(见 LB 兄弟边 LBNRIND 等),平行关系真实;但引文本身未点名 LB,LB 由通用变量推断。作为 advisory 提示可接受,不独立成立。 |
| 4 | data:RS>TU:0 | data_flow | PASS (逐字在 RS/assumptions.md L18) | **FAIL** | 引文: RSLNKGRP 连接 **findings 域**(举例 TR、LB)贡献结果到 RS。TU 是 Tumor/Lesion **Identification** 域,非 findings 结果域,引文未点名;RS 不经 RSLNKGRP 连 TU(链路应为 TU→TR→RS)。边宣称的具体机制 "via RSLNKGRP" 对 TU 错误,属机制过度声称。 |
| 5 | data:IS>LB:0 | data_flow | PASS (逐字在 IS/assumptions.md L21) | PASS | 引文 "Measurements of cytokines, chemokines, and complement proteins should be represented in the Laboratory Test Results (LB) domain." 显式点名 LB,方向 IS→LB 正确,完全支撑。 |
| 6 | data:TR>RS:0 | data_flow | PASS (逐字在 TR/assumptions.md L9) | PASS | 引文 "TRLNKGRP is used to relate records in the TR domain to a response assessment record in the RS domain." 显式点名 TR、RS、TRLNKGRP,方向正确。 |
| 7 | expl:RS>LB:18 | explicit_link | PASS (逐字整段,RS/assumptions.md L18 assumption #4) | PASS | 确定性 RELREC 正则命中;引文明言 "Records should exist in the RELREC dataset" 且给出 LB 显式例("might require lab results in the LB domain")。RS↔LB RELREC(无向)成立。 |
| 8 | co_o:TR>TU:0 | co_occurrence | N/A→PASS (确定性计数 "TR/TU co-mentioned 27x",无 prose 引文;抽检佐证 TR↔TU 在 TR/assumptions L3、L7 反复交叉引用) | PASS | 计数派生,非可逐字核的散文;TR(肿瘤结果)与 TU(肿瘤标识)为强配对,27x 共现完全合理,无向共现成立。 |

## 总判定
**AUDIT_FAIL** — 语义 FAIL ×3(阈值 ≥2 即 FAIL),另 WEAK ×1;grounding FAIL 0(8/8 引文逐字命中,co-occurrence 为确定性计数)。三条坏边均为 LLM `data_flow`:
- **data:FT>LB:0** — QRS 共享假设家族(FT/QS/RS)不含 LB,目标域捏造,verify_note 断言事实错误。
- **data:MI>EG:0** — 引文从未提 EG,实际对比域是 LB;EG 与显微组织学无关,目标域捏造。
- **data:RS>TU:0** — RSLNKGRP 连的是 findings 结果域(TR/LB)非 identification 域 TU,机制过度声称;TU 未在引文出现。

说明: grounding(机械核引文)整体健康——deterministic 通道(explicit_link/co_occurrence)全部可靠,LLM 引文均真实存在于源文件、无伪造引文。问题集中在 LLM `data_flow` 的**语义层**:引文真实但被过度解读/张冠李戴,凭"未点名的目标域"生成有向边。即便按 advisory/exploration-hint 的宽松定位,#1/#2 属捏造、#4 属错误机制声称,均超出"可信提示"范围。建议: 对未在引文中显式点名 target 域的 `data_flow` 边加硬校验(target 必须出现在 quote 或近邻文本),或降级为无向 co-occurrence 提示。#3 EG>LB 这类"通用 Findings 模式平行"边可保留但应标注为弱推断。
