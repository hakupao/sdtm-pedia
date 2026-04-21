# Q1 — CM 域拆记录 + Core=Req 变量

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ee72-28d8-83a7-a63e-c796625e56be
**Title**: SDTM Expert - SDTM CM 记录拆分
**DOM user-msg verify**: ✅ 与原题逐字一致

## 原题

受试者在同一天开始服用两种降压药 (氯沙坦 50 mg/日 + 氨氯地平 5 mg/日), 计划持续服用整个试验期, 目的是控制高血压. 请问在 SDTM CM 域里应该拆成几条记录? 每条记录至少要填哪些 Core=Req 变量? 简要说明字段含义 (不需要给具体 NCI Code).

## ChatGPT 答案

我先查 CM 域规范和假设，确认"是否拆记录"和"Core=Req 变量"这两个点，再给你一个可直接落地的结论。我已经确认到通用规则：CM 属于 Interventions，且"持续到研究结束"的场景可用相对时间变量表示 ongoing。还差最后一步：把 CM 域变量表精确定位出来，确认 Req 字段名单。

**Thought for 1m 44s**

应拆成 **2 条 CM 记录**：一条是氯沙坦，一条是氨氯地平。依据是 CM 属于 Interventions（干预）类，主题变量是 CMTRT；当同一受试者报告两个药物时，应以两个药物名分别成两条记录提交。SDTMIG 的通用示例里，两个伴随用药 ibuprofen 和 diclofenac 也是分成两条 CMTRT 记录表示的。

### 每条记录至少要填的 Core=Req 变量

基于已检索到的 SDTMIG 通用规则，至少可以确定这些是必需的核心识别/主题变量：

| 变量 | 含义 |
|---|---|
| STUDYID | 研究编号，标识这条记录属于哪个试验 |
| DOMAIN | 域名，CM 域固定为 CM |
| USUBJID | 受试者唯一编号 |
| CMSEQ | CM 域内该受试者的序号，用来保证每条记录唯一 |
| CMTRT | 报告的药物名称/治疗名称，这是 CM 的主题变量 |

依据：SDTMIG 说明 Required 变量是"识别记录所必需的关键变量和主题变量"；同时 Required identifiers 包括 STUDYID、DOMAIN、USUBJID，而 --SEQ 也是记录级唯一性的关键标识。CM 作为 Interventions 域，其主题变量是 --TRT，在 CM 中就是 CMTRT。

### 这个场景下通常还应填的关键变量

虽然你问的是 Core=Req，但就这个案例，下面这些变量通常也很重要：

| 变量 | 这个案例怎么理解 |
|---|---|
| CMDECOD | 标准化后的药名，CM 中通常填通用名/generic name；SDTMIG 明确说伴随用药这里应填药物的 generic name。对你这个例子，基本就是 losartan / amlodipine。 |
| CMSTDTC | 开始用药日期；两条记录应是同一天开始 |
| CMENDTC | 停药日期；如果整个试验期间持续且尚无实际停药日，可为空 |
| CMENRTPT + CMENTPT | 若采集到"持续中/ongoing"，可用相对时间表示"到某参考点仍未结束"；SDTMIG 对 CM 专门给了 prior/concomitant medication 的 ongoing 例子。 |
| CMINDC | 用药适应症/原因；本例可表示"控制高血压" |
| 剂量相关变量（CMDOSE, CMDOSU, CMDOSFRQ） | 分别放 50 mg/日、5 mg/日这类给药信息 |

### 你这个例子的建模要点

不要合并成 1 条"联合降压治疗"记录；因为记录主题是单个 CMTRT。应拆成 2 条，但两条可以有相同的：USUBJID / CMSTDTC / CMINDC（控制高血压）。两条记录的不同点主要是：CMSEQ / CMTRT / CMDECOD / 剂量/频次字段。

### 一个小提醒

我这次检索没有直接命中 knowledge_base/domains/CM/spec.md 的变量表原文，所以关于 CM 域完整的 Req 名单，我给的是"根据 SDTMIG 通用规则可确定的最低必需集"。其中 CMDECOD 在 CM 中通常应填这一点有明确通用规则支持，但我没有拿到 CM 变量表原文来逐项核对 Core 列。若你要，我下一条可以直接按"这 2 条 CM 记录应如何填写到变量级别"给你列一个精简模板。

## PASS 判据自检

- [x] 两条 CM 记录 (每药一条, 不合并) ✓
- [x] Req 含 STUDYID / DOMAIN / USUBJID / CMTRT ✓ (全列)
- [x] 含 CMSEQ ✓
- [x] 提到 CMSTDTC (开始日) ✓
- [x] 提到 CMINDC (指征=控制高血压) ✓
- [x] 两条指征都是高血压 ✓ (明确"两条可以有相同的 CMINDC")
- [x] 未臆造变量名 ✓
- [x] 未误列 CMCAT/CMSCAT 为 Req ✓

## Verdict: **PASS**

核心判据 (拆 2 条 + Req 4 变量全列 + CMSEQ + CMSTDTC + CMINDC + 同一指征) 全中. 特别亮点: 提到 SDTMIG 的 ibuprofen+diclofenac 典型双药示例作证据, 并坦诚 CMDECOD 层面"未拿到 CM 变量表原文逐项核对" (Rule-A 反知识 / 认识论谦虚).
