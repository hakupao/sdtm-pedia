<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝) -->

# KICKOFF — 答题侧可信度护栏 (P1 接入生产的后续 ①)

> 创建: 2026-06-09 (P1 接入生产收尾时立项, 供下个 session 路由进入)
> **状态: ✅ DONE (2026-06-09) — 护栏 v2 PASS, SHIP_DEFAULT_ON; 收口 `sdtm-rag/evidence/checkpoints/guardrail_v2_summary.md`**
> 路由词: **"RAG 答题护栏 开始任务"**
> Tier: 1-2 (单 session, 仅动系统提示词 + eval gold 修正; 不碰已验证的检索层)
> 前置已完成: P1 杠杆已接入生产默认开 (commit 0a16a5b); 配对 full-eval + 语义裁判 harness 现成

> **收口结论 (2026-06-09)**: v1 wording FAIL (对抗式裁判抓 q93/q44 漏穿 + q37 变糟, Rule B 归档) → v2 重写 (per-value 默认 name-only + 权威 Class 列分类) PASS。**码 fabrication 确定性消除 (全 102 答案 147 码 0 ungrounded; v1=10) + q37 分类修复 + 零过度拒答 + fact 噪声带内**。新增确定性闸 `check_code_grounding.py` 补 substring 指标盲区。残留 q93 值名/q96 = 检索覆盖 (护栏范围外, 已记)。下方 §1-§7 为立项时计划, 实施见 checkpoint。

## 0. 一句话

P1 接入生产时, **Rule A 语义裁判挖出答题侧的信任硬伤**: 答题模型会**给对的取值名配错的 NCI C-code**, 还会把关系类数据集误判成 special-purpose。本任务用**系统提示护栏**修这两类 (与检索杠杆正交, off/on 都有)。**用户已明确这是 P1 之外的独立任务** (P1 期间故意不动提示词)。

## 1. 要修什么 (Rule A 裁判实证, 见 `sdtm-rag/evidence/checkpoints/prod_wirein_rule_a_semantic_judge.md`)

| 缺陷 | 实例 | 危害 |
|------|------|------|
| **C-code 幻觉** | q90 (EXROUTE 路由名全对, 但 INTRAMUSCULAR→C38239 实为 INTRADISCAL 等码全错) / q91 (LOST TO FOLLOW-UP/ADVERSE EVENT 码错) / q93 (编 "INJECTABLE C42899" 不存在) | 临床标准工具给错码 = 高危; substring 指标完全漏掉 |
| **special-purpose 误判** | q37 (把 RELREC/SUPPQUAL/RELSUB/RELSPEC 当 special-purpose, 实为 relationship datasets / model/06) | 概念性错误 |

两者根因同: **答题模型过度采信/补全, 输出检索 chunk 里没有的内容**。

## 2. 怎么修 (系统提示层, `server/rag.py` `_build_system_prompt`)

在现有 Rules 后加两条 (措辞自拟, 核心语义):
1. **C-code 只准照搬**: 不得输出任何**未在检索 context 中逐字出现**的 controlled-terminology code (Cxxxxx)。给取值名时, 只有源里有码才附码; 否则只给名 + 标注"码见 terminology 文件"。
2. **分类需有源**: 不得断言某域属于某 class (special-purpose / relationship / Findings...) 除非检索 context 明确陈述。注入的关系类 chunk ≠ 该域是 special-purpose。

> ⚠️ 反过拟合 (规则, 见 [[feedback_prompt_anti_cheating]]): 写的是**通用 pattern** (不准编码 / 分类需源), **不是**针对 q37/q90/q93 的题号特例。验证时必须在测试集外探针上确认泛化。

## 3. 先决小修 — eval gold 错误 (否则验证被脏 gold 干扰)

裁判 KB 核验发现 `eval/test_set_v2.yml` 两处 gold 错 (substring 指标双向失真的根源):
- **q02**: expected_facts 含 RFSTDTC/AGE/ARM, 但 KB `domains/DM/spec.md` 标这些为 **Exp 非 Req**。DM 真 Req = STUDYID/DOMAIN/USUBJID/SUBJID/SITEID/SEX/COUNTRY。→ 修 gold。
- **q37**: expected 把 SUPPQUAL 当 special-purpose, 但 KB `model/03` 不含它 (它是 relationship dataset, model/06)。→ 修 gold。
- 修正必须 **scientist 独立 KB 核验** (规则 A 4.c, 异 subagent_type)。

## 4. 怎么验 (harness 全现成, 在 `sdtm-rag/eval/prod_wirein/`)

1. 配对 full-eval (DeepSeek **temp=0**, v2 102q): 提示护栏 OFF vs ON。命令见 `run_eval.py --temperature 0.0 --structured-lookup --hybrid`。
2. `analyze_paired.py <off>.json <on>.json` 看 fact 逐类 + 逐题 diff。
3. **Rule A 语义裁判** (`oh-my-claudecode:scientist`, 异 type, KB 核验): 重点验 q37/q90/q91/q93 是否修好 + 全局**无新回归** + 护栏没把对的内容也压掉 (over-refusal)。用 `forensic_answers.py` 重生成全答案喂裁判。
4. retrieval-only **不需重跑** (提示改动不碰检索; 但可顺手确认 99.02% 不变)。
5. 闸: 目标 q90/q91/q93 不再编码 + q37 不再误分类, 且 fact recall 全类不回退 (温度噪声带 ±1pt 内), 无 over-refusal。

## 5. 约束 / 规则

- **Rule D**: writer (改提示, executor/main) ≠ reviewer (跑 eval/裁判, 异 subagent_type)。
- **Rule B**: 失败 attempt 归 `evidence/failures/`。
- **不碰**: 已验证的检索杠杆 (config/rag.py 检索逻辑/Chroma)、`knowledge_base/` (只读)。只动 `_build_system_prompt` + test_set gold。
- **反过拟合**: pattern 非 example-patch; 测试集外探针验泛化。

## 6. 现成资产

- 残留缺陷详单: `sdtm-rag/evidence/checkpoints/prod_wirein_summary.md` §残留 + `prod_wirein_rule_a_semantic_judge.md`
- 全答案取证: `sdtm-rag/eval/prod_wirein/forensic_answers.json`
- harness: `run_eval.py --temperature` / `prod_wirein/{analyze_paired,forensic_answers,bench_latency}.py`
- 基线 (护栏前 ON): `prod_wirein/step4_full_on_t0_fix.json` (fact by cat: concept 97.3/cross 92.7/mixed 95.0/single 95.7)

## 7. 收尾

PASS 四条 + 规则 A 抽检; 更新 PROGRESS / worklog / 本 KICKOFF 标 DONE; 单 commit。
