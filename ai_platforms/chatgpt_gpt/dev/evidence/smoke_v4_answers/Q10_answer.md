# Q10 — SUPPTS 前提纠错 (ChatGPT SDTM Expert GPT, smoke v4 R1, 2026-04-22 晚)

> Verdict: **PASS+ 最强** (SUPPTS 前提纠错 + TSVAL1-n + GOC+DM+SV 完整 + §4.2.8.4 多值 bonus + 两种场景 A/B 区分)

## Prompt (v4.0)
(同 SMOKE_V4.md §2 Q10)

## Raw Answer (DOM 全文, 5644 chars)

**结论先说**:
- QORIG 是 QVAL 的来源/起源; 用于说明 supplemental 值来自 CRF/Derived/Vendor/设备 等
- QEVAL 是赋值者/评价者角色; 主观判断/归因时填, 客观数据可留空
- **SUPP-- 不适用于 TS 这类 Trial Design 数据集**. TS 的长文本不是做 SUPPTS, 而是在 TS 自身拆成 TSVAL, TSVAL1-TSVALn
- SUPPAE 找 AE 父记录, 典型键: STUDYID + RDOMAIN='AE' + USUBJID + IDVAR='AESEQ' + IDVARVAL=AE.AESEQ
- QVAL 单段上限按 SAS V5 XPT 约束是 200 字符

### (a) QORIG / QEVAL

**QORIG**: 表示 QVAL origin. 值: CRF / Derived / Vendor / Assigned / Device / Protocol. 示例: SUPPAE 中 AEOSP.QORIG=CRF, AETRTEMA.QORIG=Derived. 是否"必填": SDTMIG 重点"用于 origin traceability, 实务应填"; 坦承"给你的检索片段里没有完整展开 SUPPQUAL 变量表的 Core 列, 从设计意图看应填".

**QEVAL**: 指定赋值者角色 (ADJUDICATION COMMITTEE / SPONSOR). **Section 4.5.4**: 客观数据不要求填, 可为空; 主观 attribution 应填 (填角色, 不一定具体人名). 示例: SUPPAE 中 AEOSP (CRF 客观补充) QEVAL 空; 另例 AESEV1/AEREL1/AERELNS1.QEVAL = ADJUDICATION COMMITTEE.

### (b) SUPPQUAL scope + TS 长文本 + SUPPTS?

**1) SUPPQUAL scope**: GOC (Events, Findings, Interventions) + DM (Demographics) + SV (Subject Visits). **SUPPQUAL 不覆盖 Trial Design datasets**.

**2) TS 是否在 SUPPQUAL scope?** 不在. TS 是 Trial Design 数据集, 不是 subject-level. TS assumptions 明确说 "TS is not subject-level data".

**3) 对 TS 的 long parameter value, 理应用 "SUPPTS" 吗?** **不应该. SDTMIG v3.4 下不是用 SUPPTS.**

**4) TS 长文本 (TSVAL > 200) 怎么处理?** TS 自己有专门规则: 拆到多个变量 TSVAL-TSVALn (TS assumptions + TS spec).
- AE 的 NSV → 用 SUPPAE
- TS 的长 TSVAL → 用 TSVAL1-TSVALn
- **不是 SUPPTS**

**5) TS "多值参数" bonus insight (Section 4.2.8.4)**: 这和长文本拆段不是一回事. 对 Trial Design/Study Reference 数据集 (TS, OI), 一个 parameter 多个值 → 多条记录 (不是 SUPPQUAL). 例: 同一 TSPARMCD="TTYPE" 两条: TSVAL="EFFICACY" + TSVAL="SAFETY".

### (c) SUPPAE 回指 AE 父记录 (RDOMAIN + IDVAR + IDVARVAL + USUBJID)

**核心定位键**: STUDYID + RDOMAIN + USUBJID + IDVAR + IDVARVAL

对 SUPPAE: RDOMAIN="AE", IDVAR="AESEQ", IDVARVAL=父 AE 记录的 AESEQ 值; USUBJID=父 AE 记录的受试者 ID (限定 join 在同一受试者内).

**最常见的 join 写法**:
```
SUPPAE.STUDYID  = AE.STUDYID
SUPPAE.RDOMAIN  = 'AE'
SUPPAE.USUBJID  = AE.USUBJID
SUPPAE.IDVAR    = 'AESEQ'
SUPPAE.IDVARVAL = AE.AESEQ
```

**USUBJID 作用 insight**: AESEQ 只在某个 domain+subject 内唯一; 所以不能只靠 AESEQ=1 去找, 因为别的受试者也可能有 AESEQ=1. 必须: RDOMAIN 说父域 + USUBJID 锁受试者 + IDVAR/IDVARVAL 锁具体记录.

### (d) QVAL 长度 + 拆分

**1) 上限**: SAS V5 XPT 字符变量长度限制 200. Section 4.2.9 提醒不要无必要把字符长度都设到 200. 单条记录中的单个字符值, 实务 200 字符一段.

**2) 超过 200 怎么拆 (Section 4.5.3.2)**:
- 前 200 字符放当前变量/当前段
- 后续每 200 字符放一条 SUPP-- 记录
- **按单词边界拆** (提高可读性)
- 第一个 QNAM 用原名不加数字后缀
- 追加段依次 QNAM1, QNAM2, ...
- QLABEL 保持同一个原始 label 不加数字

**3) QNAM 已满 8 字符特例**: 数字替换最后一个字符. 例: AEACNOTH 超长 → SUPPAE 用 AEACNOT1, AEACNOT2, ...

**4) 两种场景 A/B 区分 (独到)**:
- **场景 A 标准父变量超长** (例 AE.AEACNOTH > 200): 前 200 留 AEACNOTH, 余下 SUPPAE QNAM=AEACNOT1/AEACNOT2
- **场景 B SUPP 自己 NSV 的 QVAL 超长** (sponsor-defined NSV 的 QVAL > 200): 第一条原 QNAM, 后续 QNAM1/QNAM2, QLABEL 不变

### 汇总表

| 问题 | 结论 |
|---|---|
| QORIG 是什么 | QVAL 来源 (CRF/Derived/Vendor/Assigned) |
| QORIG 必填 | 实务应填, 示例均填 |
| QEVAL 是什么 | 谁给值/判断 (SPONSOR/ADJ COMMITTEE) |
| QEVAL 必填 | 主观 attribution 填, 客观空 |
| SUPPQUAL scope | GOC + DM + SV |
| TS 用 SUPPQUAL | 不能作为标准 v3.4 用法 |
| TS 长文本 | TSVAL, TSVAL1-TSVALn |
| SUPPAE 回指 AE | STUDYID + RDOMAIN='AE' + USUBJID + IDVAR='AESEQ' + IDVARVAL=AESEQ |
| QVAL 单段长度 | 200 字符 |
| 超过 200 | 分段; QNAM1/QNAM2; QLABEL 不变 |

### 依据与溯源 (5 citation)

- SUPPQUAL scope / QORIG / QEVAL 总体: `SUPPQUAL/assumptions.md`
- Origin 含义: `ch04 §4.1.8`
- QEVAL 主客观场景 + ADJ 示例: `ch04 §4.5.4`
- SUPPAE 通过 AESEQ 指回 AE: `SUPPQUAL/examples.md`
- TS 非 subject-level, TSVAL >200 TSVAL1-n: `TS/assumptions.md`, `TS/spec.md`
- 长文本 >200 一般拆分: `ch04 §4.5.3.2`
- Trial Design 多值参数多条记录非 SUPPQUAL: `ch04 §4.2.8.4`

## Verdict 打分

| 判据 | 结果 |
|---|---|
| (a) QORIG/QEVAL 含义精准 | ✅ (Req 属性坦承自限但业务对) |
| (b) SUPPQUAL scope = GOC + DM + SV | ✅✅ 完整 (vs Gemini 漏 SV) |
| (b) **"SUPPTS 不应该用" + TSVAL1-n** | ✅✅ premise correction caught |
| (b) **§4.2.8.4 多值参数 bonus** | ✅ 独到 (Gemini/NBL 无) |
| (c) 5 键完整 + join 代码 + USUBJID 唯一性 insight | ✅ |
| (d) 200 + 分段 + QNAM 规则 + 8-char truncate + **场景 A/B 区分** | ✅ 场景区分独到 |
| Citation chain | ✅ 5 个 source 精准锚点 |
| FAIL triggers | 无 |

**最终**: **PASS+ 最强 (1 分 + 0.25 bonus)**, 4 平台中最详尽, Gemini/NBL 未提的 §4.2.8.4 多值参数 insight + 两种场景 A/B 区分为独到 bonus.

## 对比 SMOKE_V4.md 判据
- 核心 PASS 判据 (a)(b)(c)(d) 全中
- PASS+ 条件: SUPPTS 识破 + TSVAL1-n 给出 → 中
- 多 1 个 §4.2.8.4 独到观点 (trial design 多值不用 SUPPQUAL)
- 多 1 个 A/B 场景区分独到
