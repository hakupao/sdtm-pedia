# Stage v2.2 A/B 测试报告

> 执行日期: 2026-04-19 16:35-16:42 (用户时区)
> 执行者: Claude Cowork (computer-use / Chrome MCP)
> v2 Project: SDTM-Knowledge-v2 (v2.2 态, 10 文件)
> Capacity (v2.2): **20%**  (v2.1 参照: 13%, 增 +7%)
> Indexing 用时: 未精确测量 (用户指示 indicator 显示有误导性, 不等 indexing 完成, 上传后直接问问题)
> 总测试用时: ~7 分钟 (4 题均在同一新对话中连续提问)
> 对话 URL: https://claude.ai/chat/7a476afc-9adb-4212-a8fb-4dcee84b6360

## 上传确认
- [x] `09_examples_data_high.md` 已上传 (用户手工完成; Chrome MCP `file_upload` 因权限策略拒绝了 sandbox + 用户机路径, 改由用户本地拖拽完成)
- [x] `system_prompt_v2.md` 全文覆盖至 Project Instructions (含 `<!-- stage v2.2 begin -->` 段, Examples 查询优先级 09 > 07)
- [x] Project Knowledge 现状: 10 文件 (9 v2.1 文件 + 1 新文件), 文件管面板显示 `09_examples_data_high.md` 3,113 lines
- [x] Indexing: 用户指示跳过等待, 直接测试 (indicator 非真实 gating)

---

## 4 题结果明细

### T13. DM Example 1 完整数据

**v2.1 答案 (参照)**: v2.1 Project 未含 examples 数据表, 按模板回落到源路径 ("DM Example 1 具体数据见源文件 `knowledge_base/domains/DM/examples.md`").

**v2.2 答案**:

```
Source: 09_examples_data_high.md (← knowledge_base/domains/DM/examples.md)
dm.xpt (6 subjects, 25 variables)
```

Claude 原文输出完整 6 行 × 25 列 dm.xpt 表, 变量覆盖:
STUDYID, DOMAIN, USUBJID, SUBJID, RFSTDTC, RFENDTC, RFXSTDTC, RFXENDTC, RFICDTC, RFPENDTC, SITEID, INVNAM, BRTHDTC, AGE, AGEU, SEX, RACE, ETHNIC, ARMCD, ARM, ACTARMCD, ACTARM, ARMNRS, ACTARMUD, COUNTRY

6 subject 涵盖场景:
- Row 1 (ABC12301001): Drug A, M/White/Hispanic, 57YEARS
- Row 2 (ABC12301002): Placebo, M/White/NotHispanic, 50YEARS
- Row 3 (ABC12301003): Placebo, F/Black, 68YEARS
- **Row 4 (ABC12301004): SCREEN FAILURE** — RFSTDTC/RFENDTC/RFXSTDTC/RFXENDTC/AGE/ARMCD/ARM/ACTARMCD/ACTARM = null, ARMNRS="SCREEN FAILURE", 仅 RFICDTC/RFPENDTC 有值
- Row 5 (ABC12302001): Placebo, F/AMIND_AK_NATIVE
- Row 6 (ABC12302002): Drug A, F/NATIVE_HAWAIIAN

附关键观察: 2 sites (01 JOHNSON/02 GONZALEZ), RACE 6 CT 值全覆盖, ARMNRS 在 screen failure 场景用法.

**精度**: ↑ (从路径兜底 → 完整表格)
**T13 判定**: **PASS**
**说明**: 09 命中, Examples 查询优先级 09 > 07 规则生效, 直接引用表格无 fallback.

---

### T14. EX 剂量调整 Example

**v2.1 答案 (参照)**: 回落兜底 — "EX examples 具体数据见 `knowledge_base/domains/EX/examples.md`", 不给数据表.

**v2.2 答案**:

```
EX 剂量调整 Example — Example 4 数据
Source: 09_examples_data_high.md (← knowledge_base/domains/EX/examples.md)
```

场景说明: Open-label 研究, Drug A 口服 QD 3 个月, 3 个 subject 演示 EXADJ:
- 37841001: 无调整 (1 条 record)
- 37841002: 因毒性减量 20→15 mg
- 37841003: 因疗效不足增量 20→25→30 mg

ex.xpt 完整 6 行 14 列 (STUDYID, DOMAIN, USUBJID, EXSEQ, EXTRT, EXDOSE, EXDOSU, EXDOSFRM, EXDOSFRQ, EXROUTE, EXADJ, EPOCH, EXSTDTC, EXENDTC), 含 "Reduced due to toxicity" / "Increased due to suboptimal efficacy" 真实 EXADJ free-text.

附三条建模要点: (1) 每次剂量变更=新 record, SDTMIG §6.2 "one record per constant-dosing interval"; (2) EXADJ 仅在调整时填写 (baseline 不填); (3) 日期连续性 (EXENDTC 与下一条 EXSTDTC 相邻无 gap). 并给出延伸 Examples 对照 (EC/EX Ex.7, ch04 CRF) + EXADJ CT 提醒 (无官方 codelist).

**精度**: ↑ (从路径兜底 → 完整表格 + 3 要点 + 延伸对照)
**T14 判定**: **PASS**
**说明**: 命中 09 文件, 场景准确对应 "剂量调整 Example" (EX Example 4), 多维信息 (结构规则 + CT 提醒) 随答案一并返回.

---

### T1. AEDECOD Core (回归)

**v2.1 答案 (参照)**: `AE.AEDECOD — Core: Req`, Role: Synonym Qualifier, CT: MedDRA Preferred Term, Source: 05_mega_spec.md AE spec row #13 / 04_variable_index.md (`Sy / R`) / 02_chapters.md §4.3.6 AE natural key.

**v2.2 答案**:

```
AE.AEDECOD — Core: Req (Required)
Name:  AEDECOD
Label: Dictionary-Derived Term
Type:  Char
Role:  Synonym Qualifier
Core:  Req
CT:    MedDRA (Preferred Term)
Source: 05_mega_spec.md AE spec row #13 (← knowledge_base/domains/AE/spec.md)
```

上下文要点: SDTMIG §4.3.6 三元结构 (AETERM Req / AEMODIFY Perm / AEDECOD Req), AEDECOD 在 AE 域是 Req 而其他 Events 域同名变量 (BEDECOD/CEDECOD/MHDECOD) 为 Perm — 监管对 AE 编码的强要求 (AE assumptions §2c). 配套 AEPTCD (Preferred Term Code, Exp) 存 MedDRA 数值代码.

**精度**: **持平** (Core=Req 不变; 额外扩展了 §4.3.6 三元结构 + 其他 DECOD 跨域对照, 比 v2.1 信息略丰富但结论一致)
**说明**: 05_mega_spec.md 未变 → 核心答案稳定. 无回归衰减.

---

### T11. ch08 §8.3 RELREC (回归)

**v2.1 答案 (参照)**: 完整 §8.3 RELREC 内容, 含 dataset-level 变量规则 (USUBJID=null, IDVARVAL=null, RELTYPE 必填), RELTYPE 三种值 (ONE/ONE, ONE/MANY, MANY/MANY), 并注明 §6.3.5.9.3 PC↔PP 非典型案例.

**v2.2 答案**:

```
SDTMIG §8.3 — Relating Datasets Using RELREC
Source: 02_chapters.md (ch08 §8.3 全文, ← knowledge_base/chapters/ch08_relationships.md)
```

完整返回:
1. **核心定义 (§8.2 vs §8.3 对照表)** — 层级/USUBJID/IDVARVAL/RELTYPE/IDVAR/触发条件 6 维
2. **§8.3.1 Example 1 (TU ↔ TR)** — 完整 relrec.xpt 2 行表格, RELTYPE=ONE/MANY
3. **5-step 完整工作流** — 判断 §8.3 适用性 / 选择 IDVAR key / 填 RELREC 每 dataset 1 行 / 指定 RELTYPE 3 组合 / Define-XML 注释
4. **常见应用场景表** — TU↔TR, EC↔EX, PC↔PP (§6.3.5.9.3), PE↔MH
5. **§8.2 vs §8.3 对照 Example** — AE-CM-LB 123456 subject 的 peer-records relrec 表
6. **4 条关键提醒** — --SEQ 跨 dataset 不可用 / RELTYPE §8.3 必填 §8.2 通常留空 / sponsor 单 dataset 拆分需 §8.3 / Define-XML IDVAR 对应关系

**精度**: **持平** (或略 ↑) — ch08 全文在 02_chapters.md 未变, 答案结构完整且新增 §8.2 vs §8.3 对照 example 作为补充. 结论稳定.
**说明**: 02_chapters.md 没改动 → v2.1/v2.2 等价. 无回归衰减.

---

## 汇总矩阵

| # | 题目简称 | 精度 vs v2.1 | 新增 PASS? |
|---|---------|------------|-----------|
| T13 | DM Ex1 数据 | ↑ | **PASS** |
| T14 | EX 剂量调整 | ↑ | **PASS** |
| T1 | AEDECOD Core | 持平 | — |
| T11 | ch08 §8.3 RELREC | 持平 | — |

## 汇总
- 回归衰减 ↓ 数: **0 / 2**
- 新增 PASS: **2 / 2**
- 新增 FAIL: **0 / 2**

## 关键观察

1. **Examples 查询优先级规则生效**: T13/T14 均命中 09_examples_data_high.md, 答案 Source 明确标注 09, 无一例 fallback 到旧模板 "需查源 knowledge_base/..." 的兜底路径, 说明 Instructions 里的 "09 (高频) > 07 (目录)" 优先级指令被正确解读.
2. **回归零衰减**: T1 (基于 05_mega_spec.md) 与 T11 (基于 02_chapters.md) 答案结构和结论完全一致于 v2.1, 且 v2.2 还多了一些扩展上下文 (T1 三元结构; T11 §8.2 对照). 说明 112K 新文件对其他文件的 RAG 召回没有产生挤出/遮蔽.
3. **Capacity +7% 精确匹配预期**: v2.1 13% → v2.2 20%, 与规划 "20-22%" 范围一致, 验证 Option A 容量预算.

## 异常/警告

- **未测精确 indexing 时长**: 用户指示 indexing indicator 显示不可靠, 上传后立即提问依然得到完整答案, 说明实际 RAG 可用性早于 UI 状态变更. 若后续批次需要 indexing 时长数据, 需另行用 network request 监测.
- **Chrome MCP file_upload 受限**: sandbox 和用户机的绝对路径都被 `Not allowed` (code -32000) 拒绝, 本次只能由用户手工拖拽上传. 对自动化流水线是限制, 后续 Task E1 (批 3) 可能仍需用户参与上传环节.

---

## 决策建议 (供主控参考)

按 CHECKPOINT_V2.2_HANDOFF.md §决策矩阵:

| 条件 | 本次结果 | 判定 |
|-----|---------|-----|
| T1/T11 无 ↓ | 符合 (均持平) | ✅ |
| T13+T14 ≥ 1 PASS | 符合 (2/2 PASS) | ✅ |

→ **建议继续 Task E1 (批 3 examples 剩余域)**.
