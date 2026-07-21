# Q3 — LB 域 HbA1c 填写 + LBNRIND 三挡 (v2.1 关键回归)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e738b3-6ed4-83ab-9f9c-a9200f560167
**Date**: 2026-04-21
**关键点**: v2.1 Q3 判据修正 (H/L/N → HIGH/LOW/NORMAL 全写), v2.0 FAIL 此题应回归

## 原题

受试者空腹 HbA1c 检验结果为 6.8%, 参考范围 4.0-6.0%, 实验室标注为"高". 请说明 SDTM LB 域中, 这次检验应该如何填写以下变量: LBTEST (检验名) / LBTESTCD (检验代码) / LBORRES (原始结果) / LBORRESU (原始单位) / LBSTRESC (标准化字符结果) / LBSTRESN (标准化数值) / LBSTRESU (标准化单位) / LBNRIND (参考范围指示)? 指出 LBNRIND 的三挡分类 (低 / 正常 / 高) 用什么代号.

## ChatGPT 答案 (完整)

这条记录在 LB 域可这样填：

| 变量 | 建议填写 | 说明 |
|------|----------|------|
| LBTEST | Hemoglobin A1C | HbA1c 对应的标准检验名。术语中可见 LBTESTCD = HBA1C 对应 HbA1c，配套检验名为 Hemoglobin A1C。 |
| LBTESTCD | HBA1C | HbA1c 的标准短代码。 |
| LBORRES | 6.8 | 原始结果，填原始采集值。 |
| LBORRESU | % | 原始单位。LBORRESU 使用 UNIT codelist；这里原始单位就是 %。 |
| LBSTRESC | 6.8 | 标准化字符结果。只要有 ORRES，就要有 STRESC；本例未换算单位，直接拷贝数值即可。 |
| LBSTRESN | 6.8 | 标准化数值结果。STRESC 为数值时，再写入 STRESN。 |
| LBSTRESU | % | 标准化单位。本例未做单位换算，和原始单位相同。 |
| **LBNRIND** | **HIGH** | 结果 6.8% 高于参考范围上限 6.0%，且实验室已标注"高"，因此应填 HIGH。LBNRIND 用来表示结果相对参考范围的位置，不表示临床意义。 |

### LBNRIND 的三挡代号

- 低 = **LOW**（NCI code C78801）
- 正常 = **NORMAL**（NCI code C78727）
- 高 = **HIGH**（NCI code C78800）
- 另外，这个 codelist 还包含 ABNORMAL。

### 结论

对你这个例子，最直接的填写是：
- LBTEST = Hemoglobin A1C
- LBTESTCD = HBA1C
- LBORRES = 6.8
- LBORRESU = %
- LBSTRESC = 6.8
- LBSTRESN = 6.8
- LBSTRESU = %
- **LBNRIND = HIGH**

### 源溯源

- `<!-- source: knowledge_base/domains/LB/spec.md -->`
- `<!-- source: knowledge_base/domains/LB/assumptions.md -->`
- `<!-- source: knowledge_base/terminology/core/lb_part2.md -->`
- `<!-- source: knowledge_base/terminology/core/lb_part3.md -->`
- `<!-- source: knowledge_base/terminology/core/general_part4.md -->`

补一句: 你写了"空腹 HbA1c"，这个信息不进你本次问到的 8 个变量里；若研究确实采集空腹状态，通常会看是否需要另外填 LBFAST。

## 判据对齐 (v2.1)

- ✅ LBTEST = Hemoglobin A1C (正确)
- ✅ LBTESTCD = HBA1C (正确短码)
- ✅ LBORRES = 6.8 (字符)
- ✅ LBORRESU = % (单位)
- ✅ LBSTRESC = 6.8 (字符标准化)
- ✅ LBSTRESN = 6.8 (数值标准化)
- ✅ LBSTRESU = % (标准化单位)
- ✅ **LBNRIND = HIGH** (v2.1 判据, CDISC CT C78736 官方 submission value)
- ✅ 三档写全: LOW / NORMAL / HIGH + 额外 ABNORMAL
- ✅ NCI code 提供: C78801/C78727/C78800 (加分)
- ✅ 源溯源完整 (LB/spec + LB/assumptions + 3 个 terminology 文件)

## Verdict: **PASS** (1/1) 🎯 v2.1 回归成功

## 归因 + v2.0 对比

- **v2.0**: 判据为 "LBNRIND = H" (错, 与 CDISC CT 冲突), ChatGPT 当时可能答 HIGH → 被错判 FAIL. smoke_v2 记 9/10.
- **v2.1**: 判据修为 HIGH/LOW/NORMAL 全写 (C78736 官方), ChatGPT 此次答 **HIGH** + 三档全写 + NCI code + 溯源 → 干净 PASS.
- **回归结论**: v2.1 判据 + 当前 system_prompt + knowledge base → Q3 PASS, 修复了 v2.0 smoke 错判.
