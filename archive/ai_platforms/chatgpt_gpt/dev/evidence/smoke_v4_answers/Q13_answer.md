# ChatGPT GPTs — Q13 (R1 smoke v4.0, fresh chat)

> **题库版本**: v4.0 (fresh re-run, 原 v3.1 thread supereseded)
> **执行时间**: 2026-04-22 晚 11:13 PM
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8d614-ebb8-83a8-ad53-b82bc26a0c33
> **Thinking time**: 4m 47s
> **system_prompt**: v2 (7568 bytes, N5.2 lock)

---

## 模型 raw 回答 (要点, 详见 DOM)

> "我不能联网核对 2024 PDF. 下面分成两层: (1) 能被已上传 SDTMIG v3.4 直接证实 / (2) 基于规则对 observational/RWD 的保守推导. 不冒充 2024 PDF 原话."

### (a) 3 类 conformance rule 失效

1. **试验设计依赖型规则**: TA/TV/TE/SE/EPOCH/ARM — VISIT/VISITNUM/VISITDY 应来自 TV, DM.ARM/ARMCD 默认与 TA 对应
2. **Treatment/Exposure 锚点 Timing 规则**: RFSTDTC/RFENDTC/RFXSTDTC/RFXENDTC + --DY/--STDY/--ENDY + --TPTREF 相对给药. DM 假设明确承认: observational 可改用别的 protocol milestone 作 study day 起点 (enrollment/index date/consent date/cohort entry date 等 sponsor-defined 锚点)
3. **CRF-prespecification / not-done 语义规则**: --PRESP/--OCCUR/--STAT/--REASND 前提是 prespecified CRF. EHR/claims/registry "无记录 ≠ 未发生", collection-semantics conformance 天然失真

### (b) ARM/ARMCD/ARMNRS

| 变量 | 处理 |
|---|---|
| DM.ARMCD | **null** |
| DM.ARM | **null** |
| DM.ACTARMCD | null |
| DM.ACTARM | null |
| **DM.ARMNRS** | **NOT ASSIGNED** |

规则: ARMCD null → ARM 必 null → ARMNRS 必说明原因. C142179 Arm Null Reason CT: ASSIGNED NOT TREATED / NOT ASSIGNED / SCREEN FAILURE / UNPLANNED TREATMENT. **不要为了让 ARM 不空而伪造 TA/ARM**. 在 Define-XML/SDRG 明确说明.

### (c) SUPPQUAL/NSV + NS premise

**SUPPQUAL 仍然适用 + NSV 仍然适用** ✓. **"SDTMIG v3.4 里没有一个正式的、独立的 'NS = Non-Standard Domain' 机制"** ✓✓✓ 识破:
- 真正存在的标准机制: **SUPP--** (给父记录挂非标变量) + **Custom domain** (X/Y/Z 开头, SDTMIG 2.6 基于 3 个 GOC)
- 没有正式 NS = Non-Standard Domain 这一类 domain
- 若有人说 "NS domain", 在 v3.4 语境下更像是非正式口语 / 组织内部术语 / 把 custom domain 混叫成 NS — **不是 SDTMIG v3.4 的正式 domain class**

### (d) SUPPDM observational 用法

原则: subject-level / 与 DM 一条 subject 记录天然绑定 / 不能用 DM 标准变量表达 / 不更适合 AE/CM/MH 或 custom domain.

**合理候选 (observational/RWD subject-level 补充信息)**:
- **受试者来源/入组来源**: registry / EHR / claims / site chart abstraction / data partner network
- **cohort entry source / recruitment source**: 门诊/住院/疾病登记/药房数据库
- **consent / authorization 模式**: prospective consent / waiver / broad consent
- **data-linkage 相关 subject-level 说明**: 是否跨库链接 / 链接方式 / 链接可信度
- **healthcare-system / network descriptors**
- **DM 没有标准变量但需要保留的人口学补充**: 教育、居住、保险、社经层级

**源溯源**: ch03 / ch04 / ch08 / DM/assumptions / DM/spec / terminology/core/dm

---

## Self-score verdict

- **Verdict**: **PASS+ 最强** (NS premise caught + 3 rules classified + 4m 47s deep thinking + 源溯源完整)
- **对照 PASS 判据**:
  - (a) ✓✓ 3 类完整: Trial Design / Treatment timing / CRF prespecification. 匹配判据要求 "2-3 类", 多覆盖 CRF prespecification 独到
  - (b) ✓✓✓ **ARM/ARMCD/ACTARM/ACTARMCD 全 null + ARMNRS=NOT ASSIGNED + C142179 4 值全列** + Define-XML/SDRG 解释 + **"不要为了 ARM 不空而伪造 TA/ARM" 原则独到**
  - (c) ✓✓✓ **PASS+ NS premise 识破** — "SDTMIG v3.4 里没有正式的、独立的 'NS=Non-Standard Domain' 机制" + 3 真实机制 (SUPP-- / Custom X/Y/Z / NSV) + 若有人说 NS 是非正式口语
  - (d) ✓ Claims/EHR/Registry/cohort entry/consent/linkage 匹配判据 "RWD 特有 Claims/EHR/Registry/cohort ID"
- **触发 FAIL 判据?** 无
- **加分**: NS premise 识破 + "伪造 TA/ARM" 反 pattern 独到 + 3 rule categories 比判据 "2-3 类" 多一类 (CRF prespecification)
