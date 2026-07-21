# Production Wire-In — Rule A Independent Semantic Judge (full eval OFF vs ON)

> 日期: 2026-06-09
> Judge: `oh-my-claudecode:scientist` (opus) — **独立 (非 writer, 非 code-reviewer), KB 逐一核验, 规则 A 4.c 语义抽检**
> 样本: n=15 purposive (5 metric-drops + 5 metric-gains + 5 spot-check), temp=0 确定性答案
> 输入: `eval/prod_wirein/forensic_answers.json` (full untruncated off/on answers)

## 为什么需要它

substring fact-recall 是**结构检查**; "检索召回涨 ≠ 答案变好" 必须做**语义检查** (规则 A: Writer PASS + Reviewer PASS ≠ 业务 PASS)。裁判被指示**证伪** "ON 不差于 OFF",并可 grep KB 核实每个事实。

## 判决 (counts)

| 判定 | n | 题 |
|------|---|----|
| ON_BETTER | 4 | q64, q91, q100, q38 |
| EQUAL | 6 | q24, q34, q66, q01, q07, q19 |
| ON_WORSE_ARTIFACT (指标假阴, 答案实际不差或更好) | 2 | s05, q90 |
| **ON_WORSE_REAL (确认真回归)** | **3** | **q02, q37, q93** |

## 关键发现

1. **cross_domain 92.7% 的"掉"大部分是 substring 假阴**: q34/q66 丢 token 不丢事实; s05/q90 指标反而罚了**更安全/更对**的 ON (OFF 在 s05 **错误**断言 VS codelist 不可扩展; OFF 在 q34 **编造** IE/PC 映射)。OFF 不是干净基线。
2. **"ON 不差于 OFF" 被证伪**: 3 例真回归, 同源机制 = S1/S2 把关系类/兄弟域/重复 example chunk 顶进 context, 答题模型 (a) 在它们后面找不到 spec 变量表 → punt (q02), 或 (b) 过度采信 → 编错答案 (q37 把 RELREC/SUPPQUAL 误判 special-purpose; q93 编 "INJECTABLE C42899" 不存在)。**噪声稀释假说被坐实 (少数)**。
3. **substring 完全漏掉的缺陷**: 答题模型编造 NCI C-code (q90/q91/q93 给对的取值名配错的码) — **off/on 都有, 非杠杆引入** (答题侧通病)。
4. **测试集 gold 本身有错**: q02 期望 RFSTDTC/AGE/ARM 为 DM Req (KB 标 Exp); q37 期望 SUPPQUAL 为 special-purpose (KB 归 relationship dataset)。substring 双向不可靠, 语义读须覆盖它。

## 真回归 + 处置

| 题 | 真回归描述 | 检索层成因 | 处置 |
|----|-----------|-----------|------|
| **q02** | "列 DM 所有必填变量": OFF 枚举, ON 只给 DOMAIN + "spec 未完整检索" punt。DM/spec.md 在 ON 源里但变量表被挤出 top-k | hybrid/关系类 chunk + 重复 DM/examples.md 占位, 挤掉 DM spec 变量行 | **已修 (检索层)**: 单域 spec 查询注入 4 chunk; 见 `prod_wirein_q02_fix.md` |
| q37 | "special-purpose 域": ON 正确 5 个 + 误加 RELREC/SUPPQUAL/RELSUB/RELSPEC | hybrid 注入关系类 chunk, 模型当 in-scope | 干净修=答题侧护栏 (用户选不动提示词) → **残留 known limitation** (单域 spec 注入修不到它, 纯检索压制关系类会威胁 cross) |
| q93 | EXDOSFRM 例: ON 编 "INJECTABLE C42899" (不存在), 漏正确 "INJECTION" | 已检索对的 interventions.md, 仍幻觉 → 答题侧 | 干净修=答题侧护栏 (declined) → **残留** (检索改动修不到模型幻觉) |

## OVERALL VERDICT (裁判原话要点)

接通杠杆**未整体降质**: 净中性偏正 (4 真改善 + 6 等价 + 2 例指标罚了更好的 ON)。cross 的"掉"大部分是 artifact。**但** 3 例真回归确认了噪声稀释。**Ship 建议: 默认开可上 (净质量正向), 但 q02 是高频 bread-and-butter 问题的真回归, 应在 GA 前修, 不可静默接受。**

## 局限 (规则 A 诚实标注)

n=15 purposive (非随机, 过采样争议题), 不是全 102 题的总体率估计; 是"杠杆在哪帮/在哪伤"的 profile。test gold 双向有错, 语义读 override substring。

> 全文 (per-question 逐题 justification + KB 证据引用) 见 session transcript / agent af10770f0e620b997。
