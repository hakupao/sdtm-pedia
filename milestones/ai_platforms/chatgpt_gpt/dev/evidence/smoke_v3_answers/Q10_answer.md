# Q10 (H1 — SUPP-- 家族 5 字段) 综合场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83d0b-fad8-83a3-aaae-4114f855615d
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 2s

## 完整回答 (要点摘录)

### (a) QORIG / QEVAL 何时填, 何时不填

| 字段 | 含义 | 何时填 | 何时不填 |
|---|---|---|---|
| QORIG | QVAL 的来源 (origin), 例 "CRF" / "Assigned" / "Derived" | **每条 SUPP 都要填** (Req Core) | 不应留空 |
| QEVAL | 给该值/判定的人或机构角色 (evaluator role), 例 "ADJUDICATION COMMITTEE" / "SPONSOR" | 仅当 QVAL 是**主观判定/归因/解释**时填 | **客观采集或客观推导留空** (Exp Core) |

**SUPPAE 例**: adjudication committee 对 AE 严重度/因果性判定 → QORIG="CRF" + QEVAL="ADJUDICATION COMMITTEE".

### (b) SUPPTS vs SUPPAE 层级

- **SUPPAE = subject-level / record-level** (挂在每受试者每 AE 的父记录上)
- **TS = study-level** (TS assumption 直接写 "This is not subject-level data")

**诚实约束**: ChatGPT 检索 v3.4 KB 后明确指出 SUPP-- 适用父域是 Events / Findings / Interventions + DM + SV, **TS 没列**. TS 长文本应拆 TSVAL-TSVALn, 不应走 SUPPTS. 因此在 v3.4 严格语境下 SUPPTS 不是标准做法, 题目中的 "SUPPTS" 只是概念设问.

### (c) SUPPAE → AE 父记录定位键

核心 5 件套: **STUDYID + RDOMAIN + USUBJID + IDVAR + IDVARVAL**

SUPPAE 标准例:
- STUDYID = 12345
- RDOMAIN = AE
- USUBJID = 99-123
- IDVAR = AESEQ (最常见)
- IDVARVAL = 3

**USUBJID 角色**: SUPP-- 规范里它是 **Req**, 定义就是"父记录的 USUBJID". AESEQ 只在该 subject + 该 domain 内唯一, 所以必须先用 USUBJID 把 subject 范围锁住, 再用 AESEQ 定位行.

**通则**: ch04 写明 SUPP-- 子记录通过 STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL 关联回父. **DM 特例** IDVAR/IDVARVAL 可空; **AE 不是特例**, 必须用 AESEQ 等唯一标识.

### (d) QVAL 长度上限 + 拆分规则

**SAS V5 transport 物理上限 = 200 characters**. QVAL 必须有值, 不能 null.

超过 200 拆法:
1. 第 1 段放在原始 QNAM 对应那条 SUPP 记录
2. 每 200 字符开 1 条新 SUPP 记录
3. 应按**单词边界**拆, 提可读性
4. 后续段 QNAM 用顺序后缀: 原名, 原名1, 原名2…
5. **QLABEL 保持同一原始标签** (不因分段改名)
6. **若基础 QNAM 已 8 字符满长**, 替换最后一个字符为数字 (例 AEACNOTH → AEACNOT1, AEACNOT2)

例:
- 第 1 条: QNAM=AESOSP, QVAL=前 200 字
- 第 2 条: QNAM=AESOSP1, QVAL=第 201-400 字
- 第 3 条: QNAM=AESOSP2, QVAL=第 401-600 字

**对照 TS**: TS 长文本是拆 TSVAL-TSVALn, **不**走 SUPP--. 两套机制不能混.

源溯源命中:
- `knowledge_base/domains/SUPPQUAL/spec.md`
- `knowledge_base/domains/SUPPQUAL/assumptions.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/TS/assumptions.md`

## 判据对齐

- (a) QORIG=Req 每条都填, 来源 (CRF/Assigned/Derived); QEVAL=Exp 仅主观时填 ✓
- (b) SUPPAE subject-level vs TS study-level ✓; **诚实指出 v3.4 中 TS 不在 SUPP-- 适用域**, 不机械答 "SUPPTS 标准做法" ✓
- (c) STUDYID+RDOMAIN+USUBJID+IDVAR+IDVARVAL 5 件套 ✓; AESEQ 最常见 ✓; USUBJID Req 不可省 ✓
- (d) 200 char SAS V5 限 ✓; QNAM/QNAM1/QNAM2 顺序后缀 ✓; QLABEL 保持原标 ✓; 8 字符满长替换末字符 (AEACNOTH→AEACNOT1) ✓
- bonus: SUPPAE adjudication 例 (QORIG=CRF + QEVAL=ADJUDICATION COMMITTEE) ✓
- bonus: DM 特例 IDVAR/IDVARVAL 可空 ✓
- bonus: TS 长文本走 TSVAL-TSVALn 不走 SUPP-- 的对照 ✓

## 归因

PASS — Pure generalization. SUPP-- 5 字段 + 父记录定位 5 件套 + 长文本拆分 6 规则 全完整. (b) 中"SUPPTS 在 v3.4 不属 SUPP-- 标准适用范围"的诚实约束是非 trivial 加分项 (没瞎编 SUPPTS 标准用法). 8-char QNAM 替换末字符规则 (AEACNOTH→AEACNOT1) 是细节深度. 思考时长 2m 2s.
