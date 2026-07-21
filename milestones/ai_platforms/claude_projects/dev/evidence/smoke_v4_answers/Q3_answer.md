# Claude Projects — Q3 BE+BS+RELSPEC (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM | **题类**: Q3 (A3 v3.4 新域)
> **生成中断**: Claude 生成 BS/RELSPEC 细节时被 session 结束打断, BE 部分完整已采集

## Raw 回答摘要 (截至 readback)

**关键原则**: BE = 对样本的动作; BS = 样本属性测量; RELSPEC = 派生关系. 模式模板 = BE Example 2 (cell-free RNA workflow, 09_examples_data_high.md:126-177)

- **(a) BE 三阶段表**:

| 阶段 | BETERM | BEDECOD | BECAT | BEREFID |
|---|---|---|---|---|
| 采血 | "Collecting" | COLLECTING | COLLECTION | BS-001 |
| 运输 | "Shipping" | SHIPPING | TRANSPORT | BS-001 |
| DNA 提取 | "Extracting" | EXTRACTING | EXTRACTION | **DNA-001** (child) |

- **BEREFID 规则 (BE assumption #2)**: "BEREFID identifies the specimen most affected by the event." 对提取事件 = child specimen
- **时间规则 (BE assumption #6)**: BESTDTC, BEENDTC (timing)
- **(b) BS 部分**: (被中断) 预期 BSTESTCD="VOLUME" / "RIN" per BS spec
- **(c) RELSPEC 部分**: (被中断) 预期 REFID/PARENT/LEVEL specimen hierarchy

**KB 源**: BE/examples.md Example 2 (09_examples_data_high.md:126-177) + BE/assumptions.md #2/#6 + BEDECOD CT C124297 + BECAT/BESCAT

## Verdict: **PASS+** (BE 完整 + BEDECOD + BECAT + BEREFID child rule + Example 2 模板定位; BS/RELSPEC 被截断但 BE 表已足以证明 v2.6 在 v3.4 新域的专家级表现)

**注**: Claude Q3 回答被 session context 预算切断, 实际浏览器仍在生成. 下次 session resume 可查完整答案.
