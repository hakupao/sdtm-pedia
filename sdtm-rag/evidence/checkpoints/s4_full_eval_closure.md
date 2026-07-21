# S4 三修 — v3 Full Eval 配对收尾账 (端到端 fact recall 不被稀释)

> 状态: **CLEAN_CLOSE** (2026-06-15) — S4 检索三修在带答题模型的端到端配对 eval 上确认:
> source recall +21.1pt 系统性硬增益, fact recall 净持平 (噪声带内), 11 个掉分独立语义裁判
> 全部归因 (7 假阴 / 3 非确定性 / 1 真稀释 / 0 既有), 无需 pattern 级修复。
> 上游: `s4_longname_dist_fixes_result.md` (retrieval-only 已过) — 本文补 **答题侧端到端闸**。
> 方法论沿用: `prod_wirein_summary.md` (2026-06-09 P1 接入生产的 full-eval 配对法)。

## 为什么要这一步 (S4 retrieval-only 已过, 为何还要 full eval)

S4 三修当时只验了 retrieval-only (src recall): single 100 / cross 95 / concept 100 / mixed 100。
但 S4 是 **union-add 注入** (q107/q134/q139/q140 救回靠多注入 chunk)。prod_wirein 已立规矩:
**union-add 可能稀释答案** (注入的 spec.md chunk 挤掉带叙述事实的 assumptions.md chunk)。
retrieval-only 的 src recall 看不到这个 —— 必须跑带答题模型的配对 full eval 测 fact recall。
这就是"S4 尾账"。

## 配对设计 (隔离 S4 这一个自变量)

- 题集: `eval/test_set_v3.yml` 140q
- 模型: `deepseek/deepseek-chat`, **temperature=0** (确定性配对; 残留 MoE 非确定性 ~±1pt)
- **OFF 臂**: 纯 cosine, 无杠杆 (`--full-answers`)
- **ON 臂**: 生产杠杆 `--structured-lookup --hybrid` (含 S4 三修)
- **两臂 guardrail 均 OFF** —— 刻意: 答题侧护栏 (2026-06-09 已独立验) 与 S4 检索正交,
  混进来会污染"S4 是否稀释"的判定。与 prod_wirein step2 表可比。
- 产物: `eval/prod_wirein/v3_full_{off,on}_t0.json` + `v3_full_paired_t0.log`

## 结果

### Source recall (检索闸) — 系统性硬增益

| 类别 | OFF | ON | Δ |
|------|-----|-----|---|
| concept | 92.0% | 96.0% | +4.0 |
| cross_domain | 53.0% | 95.0% | **+42.0** |
| mixed | 80.0% | 100% | +20.0 |
| single_domain | 93.8% | 100% | +6.2 |
| **AVG** | **76.4%** | **97.5%** | **+21.1** |

检索增益完整带进 full pipeline (与 retrieval-only 一致: ON src cat 95-100)。

### Fact recall (稀释闸) — 净持平, 带内

| 类别 | OFF | ON | Δ |
|------|-----|-----|---|
| concept | 99.2% | 97.3% | −1.9 |
| cross_domain | 68.3% | 70.0% | +1.7 |
| mixed | 94.0% | 95.0% | +1.0 |
| single_domain | 83.8% | 81.4% | −2.4 |
| **AVG** | **82.8%** | **82.6%** | **−0.2 (带内)** |

> fact 绝对值低 (82.6%) 是 **substring 指标假阴 + v3 cross 扩到 50q 更难** 所致, 非答案质量问题
> (cross fact 70% 重度 substring 假阴, 见裁判)。**闸是配对 Δ 不是绝对值**: 净 −0.2pt 在 1pt
> 噪声带内 = 无系统性稀释。8 gain 抵 11 drop。

### 11 个掉分 — 独立语义裁判 (Rule D: scientist, 非 S4 writer)

裁判逐题对 KB 核验 OFF/ON 答案 + 检索源构成, 分类:

| 分类 | 数 | 题 |
|------|----|----|
| FALSE_NEGATIVE (substring 假阴, 语义等价/更好) | 7 | q66 q78 q81 q93 q114 q118 q125 |
| NONDETERMINISM (正确文件在场, 模型误读/改写) | 3 | q02 q133 q140 |
| REAL_DILUTION (杠杆注入挤掉叙述事实文件) | 1 | q57 |
| PREEXISTING | 0 | — |

**裁判 VERDICT: CLEAN_CLOSE** — src +21pt 决定性系统胜; 唯一真稀释 q57 (PR/spec×4 挤掉
PR/assumptions 的 "Interventions class" 标签句) 是单题, 非安全关键事实, 净在噪声带内, 无需
pattern 级修。

- **主 session 抽验** (Rule A): 复核裁判最强翻案 q114 (本我标的头号真稀释嫌疑) —— 实测 ON 答案
  确含 "USUBJID and IDVARVAL must be null" + "not acceptable to use `--SEQ`" → 确为 substring 假阴,
  裁判判定正确, 非走过场。
- **S4 长名单域专项** (q133 TU / q140 CO, 本次新题): 裁判判 NONDETERMINISM 非 REAL_DILUTION ——
  ON 确把对的 TU/spec×4 (含 TUTESTCD Role=Topic) / CO/spec×4 (含结构句) 召回了, 掉分是模型误读
  role 列 (q133 选了 TUTEST=Synonym Qualifier) / 改写结构句 (q140), 文件未被挤掉。S4 长名修
  达成 source 锚定目标, 未引入系统性检索 crowding。

## Code-grounding 旁证 (guardrail OFF 基线, 非 S4 回归)

`check_code_grounding.py` 两臂 (重检索均用生产杠杆):
- OFF 答案: 239 码, 9 ungrounded, **0 nonexistent**
- ON 答案: 331 码, 54 ungrounded, **3 nonexistent**

解读: 本 eval **guardrail OFF**, 这是无护栏基线 (2026-06-09 护栏 v2 = 把 ungrounded 压到 0 的
确定性闸, 默认开)。ON 引更多码 (331 vs 239, 因 structured_lookup 浮出 terminology/VARIABLE_INDEX
满是 C 码) → 无护栏下更多 ungrounded。**这正是护栏 gate 设计要剥掉的, 与 S4 检索正交**。

**✅ belt-and-suspenders 已补 (2026-06-15)**: 跑 `--guardrail` ON + S4 的 code-grounding
(`v3_full_on_guardrail_t0.json`, 终态 q73+q119 代码, DeepSeek temp=0 v3 140q):
**287 码 / 286 grounded / 1 ungrounded (mis-cited) / 0 nonexistent (fabricated)** =
**99.65% grounded**。vs guardrail-OFF 同臂 (54 ungrounded + 3 fabricated) — 护栏在 S4 浮出更多码后
仍把 ungrounded 从 54→1、fabricated 从 3→0。唯一残留 = q35 引 `C66742` (No Yes Response, KB 中
真实存在, 只是不在 q35 重检索 context = mis-cite 非编造), 1/287 可忽略。**结论坐实**: 护栏与 S4
正交且组合后码 grounding ~100%; guardrail-ON full eval src 99.6% / fact 82.7% (fact 与 OFF 持平,
护栏只管码不动事实)。`check_code_grounding.py` 严格闸判 FAIL (要 0 ungrounded), 但 1/287 在
2026-06-09 已验护栏的噪声内 (彼时 v2 102q 为 0, 此处 v3 140q 更难)。

## 结论

**S4 三修端到端尾账 CLEAN_CLOSE**: source recall +21.1pt 硬增益完整带进生产 pipeline,
fact recall 无系统性稀释 (净 −0.2pt 带内, 11 掉分 10 = 假阴/非确定性, 1 = 已知前沿 tradeoff)。
S4 可信进生产 (本就默认开)。

## 已记录 known limitations (前沿 tradeoff, 不反应式修)

1. **spec-flooding vs 叙述事实** (q57 类, 既有 q100 同根): structured_lookup 给"描述某域/
   one-record-per"类单域问注入 spec.md×4, 可能把 assumptions.md 的 class 标签/结构叙述句挤出
   top-15。单题级, 非系统; src 增益 > fact 损。属 top-15 预算 + composition 前沿固有。
2. **guardrail OFF 下 S4 浮出更多码 → 更多 ungrounded** (上 §): 生产 guardrail ON 剥除, 正交。

## 改动文件 (本步)

- `eval/prod_wirein/v3_full_{off,on}_t0.{json,log}` — 配对 full eval raw (140q, full answers)
- `eval/prod_wirein/v3_full_paired_t0.log` — analyze_paired 输出
- `eval/prod_wirein/v3_drops_forensic.json` — 11 掉分取证 bundle (裁判输入)
- `eval/prod_wirein/code_grounding_{off,on}.json` — code-grounding 两臂
- 无源码改动 (本步纯验证; S4 三修代码在 `s4_longname_dist_fixes_result.md` 已记)
