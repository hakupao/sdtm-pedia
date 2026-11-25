# Sanity Q3 — CMINDC 使用场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e82ea6-92c4-83aa-81be-6ca69347d581
> 提交时间: 2026-04-22
> 题: CMINDC 用于哪种场景?
> 期望: 显式命名 CMINDC (concomitant medication indication)
> Verdict: **PASS**

## 完整回答

CMINDC 用在 CM（Concomitant and Prior Medications）域里记录"用药适应症/用药原因"的场景。也就是：这条药物记录是因为什么医学原因而用的。它的定义是 CM.CMINDC (Label: Indication, Role: Record Qualifier, Core: Perm)，CDISC 注释写的是"Denotes why a medication was taken or administered"，示例值有 "NAUSEA"、"HYPERTENSION"。

更直白地说：
- 药名/治疗本身 放在 CMTRT
- 为什么吃这个药 放在 CMINDC

例如，某受试者服用甲氨蝶呤或柳氮磺吡啶，若是为了治疗类风湿关节炎，那么 CMINDC 可以填 RHEUMATOID ARTHRITIS；CM 示例里就是这样表示的。

它还有一个很典型的使用场景：
当 CRF 不是自由文本，而是用一个预设列表来采集"用药适应症"，并带有 "Other, specify" 时，CMINDC 就是承载这个"适应症"值的标准变量。SDTMIG 给的例子是镇痛类合并用药的适应症选项：术后痛、头痛、痛经、肌痛、牙痛、Other。若研究者选了 OTHER 并写了 "Broken arm"，有三种提交方式：

1. 保持 CT 只限预设项：CMINDC = "OTHER"，自由文本放 SUPPCM (QNAM="CMINDOTH"、QVAL="BROKEN ARM")
2. 保持 CT，但允许申办方扩展术语：CMINDC = "FRACTURE"（或类似编码值），SUPPCM 可保留 verbatim
3. 不要求维护 CT：直接 CMINDC = "BROKEN ARM"，不一定需要 SUPPCM

源溯源:
- `<!-- source: knowledge_base/domains/CM/spec.md -->`
- `<!-- source: knowledge_base/domains/CM/examples.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`

## 判据

- 显式命名 CMINDC ✓
- 命名 CM 域 ✓
- 区分 CMTRT vs CMINDC ✓
- 给出 RHEUMATOID ARTHRITIS / NAUSEA / HYPERTENSION 示例 ✓
- "Other, specify" + SUPPCM (QNAM=CMINDOTH) 三方案完整 ✓ (N5.1 batch 2 bullet 命中)

PASS — N5.1 batch 2 terminology + ch04 assumptions 锚点全部生效
