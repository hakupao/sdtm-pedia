# Q7 — MH + CM 双域 + CMINDC 必显式命名 (v2.1 关键回归)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e73f33-9980-83aa-902d-4982b60a6a89
**Date**: 2026-04-21
**Thought for**: 2m 45s
**关键点**: v2.1 system_prompt L62 "变量必显式命名" bullet 的核心验证题, **CMINDC 必须显式命名**

## 原题

EDC 系统里某字段值为 "病史: 高血压 10 年, 目前仍在服用氨氯地平 5 mg/日". 映射到 SDTM 时这条信息应该拆成哪些域的记录? 只进 MH? 只进 CM? 还是两域都要? 简要说明 MH 和 CM 的分工.

## ChatGPT 答案 (完整)

**结论**: 通常两域都要, 不是只进 MH, 也不是只进 CM.

因为这条源数据同时包含了两个不同的 SDTM 概念:

| 源信息片段 | 建议域 | 典型变量 |
|-----------|-------|---------|
| "病史: 高血压 10 年" | MH | MH.MHTERM, MH.MHDECOD |
| "目前仍在服用氨氯地平 5 mg/日" | CM | CM.CMTRT, CM.CMDECOD, **CMINDC**, 以及剂量/时序变量 |

### 为什么要拆成两域

- **MH 是 Events 类**, 记录"这个受试者有什么病/病史/医学状况";
- **CM 是 Interventions 类**, 记录"这个受试者用了什么药/治疗". SDTM 总体模型里就是这样分工的, CM 还明确是 "one record per recorded intervention occurrence or constant-dosing interval per subject".
- 通用规则里也明确区分了事件类和干预类的主题变量: 事件用 `--TERM`, 干预用 `--TRT`; 并且在已定义域里, MH 对应 MHTERM/MHDECOD, CM 对应 CMTRT/CMDECOD.

### 这条数据可怎么落

**MH 1 条**:
- MHTERM = 高血压
- MHDECOD = Hypertension (按字典编码后)
- "10 年"表示病史时长 / 起病已久; 如果原始采集允许, 可映射到 MHSTDTC (完整或部分日期).
- 如果原始采集表达"目前仍存在/仍活动", MH 也可以用相对时序表示 ongoing, 例如 **MHENRTPT = "ONGOING"** + MHENTPT 作为参考时间点, SDTM 给过 Medical History 的这种示例.

**CM 1 条**:
- CMTRT = 氨氯地平
- CMDECOD = Amlodipine (按药物字典标准化)
- 剂量可放 CMDOSE = 5, CMDOSU = mg
- 用药原因可放 **CMINDC = 高血压**; CM 示例里就有 CMINDC 记录适应症/用药指征的用法
- "目前仍在服用"通常表示 CM 记录是 ongoing; SDTM 例子里对 continuing medication 用 **CMENRTPT = "ONGOING"**, CMENTPT 表示参考时间点

### 一句话分工

- **MH: 记"病"**
- **CM: 记"药"**

### 实务判断小点

如果原始数据里只明确采集了药物, 并没有明确采集"高血压"这个病史, 就不要反推补造一条 MH. 但你给的例子里已经明确写了"病史: 高血压 10 年", 所以这条通常应拆为 MH + CM 两部分.

### 源溯源

- `knowledge_base/chapters/ch03_submitting_data.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/CM/examples.md`

## 判据对齐 (v2.1)

- ✅ **两域都要** (不是只进 MH, 也不是只进 CM) — 核心结论对
- ✅ **MH 域**: MHTERM / MHDECOD 命名 (v2.1 要求, 显式变量名)
- ✅ **CM 域**: CMTRT / CMDECOD 命名
- ✅ **CMINDC = 高血压** (v2.1 关键判据 L62 "变量必显式命名", 已显式命名 + 给出值 + 并指出"CM 示例里就有 CMINDC 记录适应症/用药指征的用法") 🎯
- ✅ 加分 MHENRTPT = "ONGOING" + MHENTPT (MH ongoing 表达, 示例级知识)
- ✅ 加分 CMENRTPT = "ONGOING" + CMENTPT (CM continuing medication 表达, 示例级知识)
- ✅ MH = Events 类 vs CM = Interventions 类分工 (模型层分类) 清晰
- ✅ --TERM (事件类) vs --TRT (干预类) 主题变量对比
- ✅ "MH 记病 / CM 记药"一句话分工
- ✅ 边界: 若原始只采集药物未采病史则不反推造 MH, 但本题有病史故拆两域
- ✅ 引 3 源 (ch03 + ch04 + CM/examples)

## Verdict: **PASS** (1/1) 🎯 v2.1 CMINDC 回归成功

## 归因 + v2.1 核心验证

- **v2.1 L62 bullet "变量必显式命名" 的核心压力测试**: Q7 是否显式点出 CMINDC, 是本次 smoke 最核心的判据.
- **本次结果**: CMINDC 在表格第一行立即显式命名 ("CM.CMTRT, CM.CMDECOD, **CMINDC**"), 并在"CM 1 条"细节中再次显式 "CMINDC = 高血压; CM 示例里就有 CMINDC 记录适应症/用药指征的用法", 两次出现, **PASS 无悬念**.
- **超判据基线**: MHENRTPT/CMENRTPT = "ONGOING" + MHENTPT/CMENTPT ongoing 表达属于 SDTMIG 示例级知识, 体现 system_prompt v2.1 + knowledge base 深度命中.
- **3 源溯源完整**: chapters (模型级) + CM examples (示例级) 两级证据链齐备.
