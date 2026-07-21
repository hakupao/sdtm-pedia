# Q10 — RELREC vs SUPPAE/SUPPCM: AE ← CM 因果关联

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6efb4-cd4c-83a6-b6ae-0dbeb7ed89fb
**Title**: SDTM Expert - RELREC vs SUPPAE 用途

## 原题

一位受试者的某次 AE (头晕) 被 Investigator 判定和某合并用药 (复方降压药) 引起的血压下降有关. 这种"AE 由 CM 引起"的关联, 应该用 RELREC (Related Records) 记录, 还是用 SUPPAE / SUPPCM 存储? 解释两者的差异 (RELREC 负责什么 / SUPPAE/SUPPCM 负责什么), 说明本场景的选择理由.

## ChatGPT 答案

**结论**: 本场景应优先用 **RELREC** 记录 AE↔CM 的关联; SUPPAE / SUPPCM 只用于补充父记录的额外属性, 不应代替跨域记录链接.

**职责对照**:

| 机制 | 负责什么 | 不负责什么 | 本场景是否主用 |
|---|---|---|---|
| **RELREC** | 明确"哪一条 AE 记录"和"哪一条 CM 记录"有关; 记录级/跨域关系数据集 | 不表达关系语义本身; SDTMIG 明说它只表示"有关系", 不说明关系的性质 | **是** |
| **SUPPAE / SUPPCM** | 给某一条 AE 或 CM 父记录补充非标准变量、自由文本、"Other, specify"、长文本、次评估/次要响应等 | 不擅长表达"AE 这条记录对应 CM 那条记录"的标准跨域链接 | 否 (仅可辅助) |

**依据**:

1. **RELREC 的职责是"链接记录", 不是"解释关系性质"**. SDTMIG 原文: "RELREC indicates that there is a relationship between records or datasets, but not the nature of the relationship". 也就是 RELREC 负责"谁和谁相关", 但不负责把"因为…引起""导致血压下降后出现头晕"这种语义写进去. RELREC 的标准键字段: STUDYID / USUBJID / RDOMAIN / IDVAR / IDVARVAL / RELTYPE / RELID.

2. **SUPP-- 的职责是"补充父记录属性"**. SDTMIG 规定: 当自由文本是为了补充一个标准非结果限定变量时, 应放到 SUPP--. 若一个标准变量只能放一个主值, 次要值进 SUPP--. 次评估者的数据也应进 SUPP--.

**本场景建模**:

1. **用 RELREC 连接具体 AE 记录和具体 CM 记录**:
   - AE 这条记录的 AESEQ
   - CM 这条记录的 CMSEQ
   - 用同一个 RELID 连起来
   - RDOMAIN 分别指向 AE 和 CM, IDVAR/IDVARVAL 分别写 AESEQ / CMSEQ 的值

2. **"与非研究治疗有关"的判定放在 AE 端的因果性信息里** — SDTMIG 的 AE/SUPPAE 示例明确提到 Relationship to Non-study Treatment 这一概念.

3. **只有在下列情况才用 SUPPAE / SUPPCM**:
   - 需要补充自由文本 (如"与复方降压药导致的血压下降有关")
   - 第二评估者的因果性意见
   - 主值之外的次要响应
   - "Other, specify"或长文本

**推荐**: RELREC + AE 端因果性判定 (必要时辅以 SUPPAE)

**不推荐仅用 SUPPAE/SUPPCM 的原因**:
- SUPP-- 只是在某条 AE 或 CM 记录上"加一列补充信息"
- 它不能天然、标准地表达"这条 AE 就是和那条 CM 相连"
- 一旦同一受试者有多条 CM, 仅写补充文本会变得不够可追溯

**一句话总结**: "AE 由某条 CM 引起/相关"这类问题, RELREC 负责把 AE 记录和 CM 记录连起来; SUPPAE / SUPPCM 负责给 AE 或 CM 记录补充说明. 前者是"连谁和谁", 后者是"补充这条记录还想说什么".

## PASS 判据自检

- [x] 选 RELREC (跨域关系) ✓
- [x] 解释 RELREC 和 SUPP 的分工 ✓ (职责对照表 + 依据)
- [x] RELREC 负责跨记录关系 ✓ ("谁和谁相关")
- [x] SUPP-- 负责单条记录的补充属性 ✓ ("加一列补充信息")
- [x] 不应用 SUPPAE/SUPPCM 存储跨域关系 ✓ (明确"不能天然、标准地表达这条 AE 就是和那条 CM 相连")
- [x] RELREC 关键字段 ✓ (STUDYID/USUBJID/RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID)
- [x] 建议主域存因果变量 + RELREC 连记录 ✓ (分层策略)

## Verdict: **PASS**

核心判据全中 + 3 个额外亮点:
1. 职责对照表 (机制 / 负责 / 不负责 / 是否主用) 结构化
2. RELREC 字段完整 (7 个: STUDYID/USUBJID/RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID)
3. AE-CM 建模三段式 (RELREC 连记录 + AE 端因果变量 + SUPPAE 辅助) 层次清晰
4. 反例: 为什么不仅用 SUPP (多条 CM 时不可追溯) — Rule A 反知识示例

Rule A 反知识: "SUPP-- 不能天然表达这条 AE 就是和那条 CM 相连" — 明确击穿"用补充域塞关系"的误用.
