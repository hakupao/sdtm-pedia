# Q4 — Gemini v8.1 dry-run evidence

> 日期: 2026-05-19 16:37 PM
> Mode: Gemini 3.1 Pro (fresh chat post-navigate)
> Prompt: v8.1

## 题文

> 以下 3 个实验室检验结果, 在 SDTMIG v3.4 下分别记录到哪个域 (LB / MB / IS)?
> 场景 A: 疫苗试验, baseline 检测受试者血清中抗麻疹病毒 IgG 抗体滴度 1:128
> 场景 B: 抗肿瘤单抗治疗后, 受试者血清中检测抗药物抗体 (ADA) 阳性/阴性 + 滴度
> 场景 C: 受试者痰样做结核杆菌培养, 结果 positive
> 每个场景给出: (i) 域名; (ii) 理由; (iii) Topic 变量值示例. v3.4 下边界规则是什么?

## Verdict 矩阵

| 维度 | R3 v7.1 | v8.1 dry-run | Delta |
|---|:---:|:---:|---|
| Verdict | **FAIL** ⚠️ (A=LB) | **PASS+** ✓ | ⬆ 修复 |
| Response len | 1597 chars | **1763 chars** | OK |
| Total ms | — | 52,660 | OK |
| Scenario A (麻疹 IgG) | ❌ **LB** (退回 v3.3 旧 path) | ✅ **IS** + ISBDAGNT=MEASLES VIRUS + ISORRES="1:128" + ISCAT=NON-STUDY-RELATED IMMUNOGENICITY + 引 §2 | 完全修复 |
| Scenario B (ADA) | ✓ IS | ✅ IS + ISTSTOPO=SCREEN/QUANTIFY + ISCAT=ANTIDRUG ANTIBODIES + 引 §8 | 维持 + 加 ISTSTOPO |
| Scenario C (Mtb) | ✓ MB | ✅ MB + MBTESTCD=MCORGIDN + MBSPEC=SPUTUM + MBMETHOD=MICROBIAL CULTURE | 维持 + 加 method |
| v3.4 边界规则 | — | ✅ IS vs LB / IS vs MB 分述 + 例外 (细胞因子→LB) | 加分 |
| HIV exemption | — | ✅ "HIV Ag/Ab combo 联合检测... 强制走 MB, 不归 IS 不归 LB" | 加分 (Reviewer H1 fix fire) |

## Prong 验证

**Prong 3 (CO-1e IS scope shift v3.3→v3.4)**: ✅ **完全 fire**.
- "v3.4 标准中，所有的抗病原体抗体 (anti-microbial antibody) 测量值，不论其采集时机（如 baseline）..., 已全部划归 IS 域，严禁作为常规血清学检查放入 LB 域"
- 这是 KB IS Assumption 2 的直接执行
- 切断了 v7.1 R3 时 R2 修过的 Q4-A 退回 LB 的 path (R2 fix decay)

**Reviewer fix H1 (HIV Ag/Ab combo → MB, not LB)**: ✅ **fire 了**
- response 末段 "特殊豁免 (HIV Ag/Ab combo)：由于第四代 HIV 抗原/抗体联合检测的核心目的是进行病原体筛查与鉴定，而不是细化宿主免疫反应特征，因此作为边界例外，该联合检测强制走 MB 域，既不归 IS 也不归 LB"
- 这是 KB IS Assumption 5 的精确表述 — v8.1 reviewer fix 直接验证

**Sticky anchor 设计**: ✅ 起效. R3 测试时 Q4-A 退回 LB 表明 R2 v7.1 fix decay, v8.1 set sticky default 后没退回.

## 关键 response 片段

```
场景 A: 抗麻疹病毒 IgG baseline
结论：记录到 IS 域。
依据：抗麻疹病毒 IgG 滴度测定的是宿主对病原体产生的体液免疫反应，
而非病原微生物本身的分离培养，因此不属于 MB 域。在 v3.4 标准中，
所有的抗病原体抗体 (anti-microbial antibody) 测量值，不论其采集时机
(如 baseline) 或是否与研究直接相关，已全部划归 IS 域，
严禁作为常规血清学检查放入 LB 域。
- ISTESTCD = "IGG" / ISBDAGNT = "MEASLES VIRUS"
- ISORRES = "1:128" / ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY"
- 来源: SDTMIG v3.4 IS domain — assumptions §2

场景 B: ADA
结论：IS 域
- ISTESTCD = "ADA_BAB" / ISTSTOPO = "SCREEN" / "QUANTIFY"
- 来源: §8

场景 C: Mtb 培养
结论：MB 域
- MBTESTCD = "MCORGIDN" / MBSPEC = "SPUTUM" / MBMETHOD = "MICROBIAL CULTURE"

v3.4 边界规则:
- IS vs LB: 抗病原体抗体均放 IS, 例外: 细胞因子/补体 → LB
- IS vs MB: 宿主抗体反应 → IS / 直接微生物检出 → MB
- HIV Ag/Ab combo: 强制 MB, 不归 IS 不归 LB (边界例外, Assumption 5)
```
