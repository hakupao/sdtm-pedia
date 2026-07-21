# Q6 — DM.ARMCD vs DM.ARM 关系 + 中途换组

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef52-5c14-83aa-a485-4ce9e08bb74c
**Title**: SDTM Expert - DM ARMCD ARM 关系

## 原题

解释 DM 域的 ARMCD (Arm Code, 分组代号) 和 ARM (Arm Description, 分组描述) 的关系 (哪个是短代号, 哪个是 human-readable). 如果受试者因盲态问题在 Week 4 从 Arm A 转到 Arm B, 这个信息应该记录在 DM / SE / TA 哪个域? 分别说明各自的职责.

## ChatGPT 答案 (精简)

| 变量 | 含义 | 本质 |
|---|---|---|
| ARMCD | Arm Code | 短代号 / short code，更偏程序化、紧凑表示 |
| ARM | Arm Description | human-readable 描述，给人看的完整分组名称 |

ARMCD 在 TA 是 Topic variable, 在 DM 是 Record Qualifier; TA 负责"定义 trial arm 本身", DM 只是把 arm 信息作为受试者层面的属性带上. ARMCD 长度限制为 20 字符, 设计为适应 crossover 等复杂分组命名.

**本场景 (Week 4 从 Arm A 转到 Arm B) 归属**:
- **TA** (Trial Arms, 试验设计层): 不记录这个受试者实际切换事件本身. TA 是方案里计划好的 arm, 不是某个受试者后来实际怎么走.
- **SE** (Subject Elements, 受试者实际经历层): **这是最该记录"实际发生的切换路径"的地方**. 应在 SE 里体现为: 前一段 element 结束 + 新一段 element 开始.
- **DM** (Demographics, 受试者层面摘要): 只放受试者层面的 arm 汇总归属, 不放纵向切换历史. DM.ARMCD / DM.ARM 用于计划 arm 摘要; 若需表达实际接受的 arm, 通常用 **ACTARMCD / ACTARM** 做受试者层面 actual arm 摘要.

**简化判断规则**:
- 问"方案原本怎么设计？" → 看 TA
- 问"这个受试者实际上怎么走的、什么时候切换的？" → 看 SE
- 问"这个受试者最终/汇总归属是什么？" → 看 DM

**补充**: 如果从 A 到 B 的转换是方案预先设计好的 (crossover / re-randomization), TA/TE 先定义好设计, SE 记录受试者实际按设计走过哪些段. 如果是非计划的 (盲态问题临时切换), 也不要改写 TA; TA 仍表示设计, 实际发生仍应主要落在 SE.

## PASS 判据自检

- [x] ARMCD = 短代号 ✓ (明确)
- [x] ARM = Full description / human-readable ✓ (明确)
- [x] ARMCD 最长 20 字符 ✓ (提到 "长度限制为 20 字符")
- [x] ARMCD 是 TA 的 Topic var, DM.ARMCD 必须匹配 TA.ARMCD (隐含在 TA 定义 arm, DM 是 qualifier 的论述里)
- [x] 中途换组: DM 只记最终分组 (ACTARMCD/ACTARM) ✓
- [x] SE 记实际经过的 element 序列 ✓
- [x] TA 是设计非实际 ✓
- [x] 答案含 ACTARM / ACTARMCD vs ARM / ARMCD 区分 ✓

## Verdict: **PASS**

核心判据全中 + 额外层次: (1) ARMCD/ARM 的 SDTM model 层级别角色区分 (TA Topic vs DM Qualifier); (2) 计划 vs 非计划 crossover 的统一处理原则 ("不论计划与否, 都不改写 TA"); (3) 简化判断规则三问一答.
