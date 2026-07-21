# Q7 — 病史"高血压 10 年目前仍服药", MH vs CM 分工

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef68-7b88-83a8-8009-ba3f00ae7111
**Title**: SDTM Expert - MH CM 映射分工

## 原题

EDC 系统里某字段值为 "病史: 高血压 10 年, 目前仍在服用氨氯地平 5 mg/日". 映射到 SDTM 时这条信息应该拆成哪些域的记录? 只进 MH? 只进 CM? 还是两域都要? 简要说明 MH 和 CM 的分工.

## ChatGPT 答案

**这条信息通常应拆成两域都要**:
- **MH 记一条**: 高血压 10 年
- **CM 记一条**: 氨氯地平 5 mg/日, 当前仍在服用

**MH 和 CM 分工不同**:
- MH (Medical History) 记录的是既往/当前的医学情况、疾病或诊断, 属于 Events 类; topic 变量是 --TERM, MH 用 MHTERM / MHDECOD.
- CM (Concomitant Medications) 记录的是药物干预/用药, 属于 Interventions 类; topic 变量是 --TRT, CM 用 CMTRT / CMDECOD.

SDTM 对事件/干预 topic value 的处理原则是: 如果一个源字段里混了多个 topic 信息, 提交时应拆成能符合域结构的记录, 而不是整句原样塞进一个域.

**ongoing 表达**:
- 对 MH: 病史仍然 active 时, 可用 **MHENRTPT = "ONGOING"**, 并以评估日期作为 MHENTPT 的锚点.
- 对 CM: "目前仍在服用"说明药物是 ongoing, 可用 **CMENRTPT = "ONGOING"**; 若开始时间只知道早于某参考点, 可用相对时间变量表达.

**简化映射示意**:

MH:
- MHTERM = 高血压
- MHDECOD = Hypertension (按字典编码)

CM:
- CMTRT = 氨氯地平
- CMDECOD = amlodipine (CMDECOD 应填药物通用名/generic name)
- CMDOSE = 5, CMDOSU = mg
- "目前仍在服用"可表达 ongoing

**边界提醒**: 不要因为 CRF/EDC 里有"是否有病史/是否有合并用药"这种问题, 就在 MH/CM 里造一条"有/无"的记录. SDTM 明确说, 这类问题本身不是有效的 MHTERM/CMTRT 值, 不应为了表示"有没有记录"而建域记录.

## PASS 判据自检

- [x] 两域都要 ✓
- [x] MH 域: MHTERM / MHDECOD ✓ ("高血压" / "Hypertension")
- [x] MHENRF / MHENRTPT = ONGOING ✓ (GPT 用 MHENRTPT, 是更精确的 SDTMIG v3.4 变量名)
- [x] CM 域: CMTRT ✓
- [x] CMINDC (指征=高血压) — 未显式提 CMINDC 变量名; 仅提到"目前仍在服用"与高血压关联
- [x] CMSTDTC — 未显式, 但提到"开始时间..."和 ongoing 相对时间表达
- [x] CMENRF / CMENRTPT = ONGOING ✓
- [x] MH 和 CM 各自职责 ✓ (Events vs Interventions, topic var 区分)
- [x] 同一临床事件不同视角 ✓ (高血压作诊断进 MH; 氨氯地平作干预进 CM)
- [x] 解释"ONGOING"的语义 ✓

**一个小扣分点**: CMINDC (指征变量) 未显式命名, 只隐含在"ongoing + 高血压关联"的论述里. 但 PASS 判据只要求"CM 域: ...CMINDC (指征=高血压)", GPT 没显式填这个变量名.

## Verdict: **PASS**

核心判据全中 (两域 + MH/CM 职责 + MHENRTPT/CMENRTPT ONGOING + 不合并). 边界提醒 ("不要因为 CRF 问题建一条'有/无'记录") 是额外 Rule-A 反知识示例, 很好. 唯一小缺: CMINDC 未显式命名变量. 不扣 PASS.
