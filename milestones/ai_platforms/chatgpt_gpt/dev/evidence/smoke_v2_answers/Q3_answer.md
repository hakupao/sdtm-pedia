# Q3 — LB 域 HbA1c 记录 + LBNRIND 三挡

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef21-ae04-83a8-b5af-8551a6fb9a0a
**Title**: SDTM Expert - SDTM LB填写指导

## 原题

受试者空腹 HbA1c 检验结果为 6.8%, 参考范围 4.0-6.0%, 实验室标注为"高". 请说明 SDTM LB 域中, 这次检验应该如何填写以下变量: LBTEST (检验名) / LBTESTCD (检验代码) / LBORRES (原始结果) / LBORRESU (原始单位) / LBSTRESC (标准化字符结果) / LBSTRESN (标准化数值) / LBSTRESU (标准化单位) / LBNRIND (参考范围指示)? 指出 LBNRIND 的三挡分类 (低 / 正常 / 高) 用什么代号.

## ChatGPT 答案

这条 LB（Laboratory Test Results）记录，可按下面填写：

| 变量 | 建议值 | 说明 |
|---|---|---|
| LBTEST | Glycohemoglobin A1C | HbA1c 的标准检验名。我这次没从当前检索结果里直接打到该术语行，但按 CDISC LB 常用受控术语通常这样填。 |
| LBTESTCD | HBA1C | HbA1c 的标准检验代码；--TESTCD 需使用受控术语，且长度不超过 8 个字符。 |
| LBORRES | 6.8 | 原始结果，保留实验室原始数值。 |
| LBORRESU | % | 原始单位。 |
| LBSTRESC | 6.8 | 标准化字符结果。数值型结果若原始单位已是标准单位，可直接拷贝到 --STRESC。 |
| LBSTRESN | 6.8 | 标准化数值结果。数值型结果应填数值；非数值结果才留空。 |
| LBSTRESU | % | 标准化单位。原始单位已是标准单位时，通常与 LBORRESU 相同。 |
| LBNRIND | **HIGH** | 结果 6.8% 高于参考范围上限 6.0%，且实验室标注"高"，所以应判为高。 |

LBNRIND 的三挡分类，通常写成：
- 低：**LOW**
- 正常：**NORMAL**
- 高：**HIGH**

几点依据：Findings 域中的 --TESTCD 应使用受控术语；如果 CRF 上是自由填写的检验名，也要映射成一致的 --TESTCD/--TEST。--TESTCD 不能超过 8 个字符。对数值型化验结果，如果原始单位已经是标准单位，则原始值可直接拷贝到 --STRESC / --STRESN / --STRESU。

坦诚说明：这次检索没有直接返回 HbA1c 对应术语表那一行，所以 HBA1C / Glycohemoglobin A1C 这一对值是按标准 LB 术语惯例给出的。

## PASS 判据自检

- [x] LBTEST = "Glycohemoglobin A1C" ✓ (近似 "Hemoglobin A1C")
- [x] LBTESTCD = "HBA1C" ✓
- [x] LBORRES = "6.8" ✓
- [x] LBORRESU = "%" ✓
- [x] LBSTRESC = "6.8" ✓
- [x] LBSTRESN = 6.8 (数值) ✓
- [x] LBSTRESU = "%" ✓
- [ ] **LBNRIND = "H"** ❌ GPT 写 "HIGH" (全长)
- [ ] **三档代号 L / N / H** ❌ GPT 写 "LOW / NORMAL / HIGH" (全长)

## FAIL 判据命中

- ⚠️ **LBNRIND 三档说错** — GPT 给 "LOW / NORMAL / HIGH" 而非 "L / N / H". 这正是题目 FAIL 判据明文要 hit 的陷阱.

**注**: CDISC CT LBNRIND codelist 受控术语实际是 `L` / `N` / `H` / `ABNORMAL` / `NORMAL` 等混用 (取决于版本), 但本题 PASS 判据明确要求 "H / N / L" 三档代号, GPT 答 "HIGH/NORMAL/LOW" 直接触及 FAIL 条件.

## Verdict: **FAIL**

LBNRIND 三档代号错误 (触 FAIL 判据 #1). 其他 7 变量值 (LBTEST/LBTESTCD/LBORRES/LBORRESU/LBSTRESC/LBSTRESN/LBSTRESU) 全对, LBORRES vs LBSTRESN 字符/数值区分清楚, LBSTRESC vs LBSTRESN 区分清楚. 但 LBNRIND 这一核心检点是题目 7 个判据中**唯一 FAIL 判据明文标注的点**, 故扣 PASS.

备选判定: **PARTIAL (0.5)** — 因 7/8 变量值对, 仅 LBNRIND 的代号粒度错 (是写长版还是短版), 业务理解是对的. 若按"核心判据 >= 50% 中 + 0-1 小缺漏"可给 0.5. 但 FAIL 判据明文命中, 偏向 FAIL.

**最终 Verdict: FAIL** (或 PARTIAL 0.5, 取决于评分严格度).
