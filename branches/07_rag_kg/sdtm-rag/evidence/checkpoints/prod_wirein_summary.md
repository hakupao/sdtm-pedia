# P1 杠杆接入生产 + 端到端验证 — 收口总结 (规则 C retro)

> 日期: 2026-06-09 (单 session)
> 目标 (用户 ① 第一优先): 把 P1 验证过的 structured_lookup + hybrid 接进 `/ask` 默认开 (不只 eval flag) + 跑带答题模型的 full eval 确认 fact recall 不被稀释 + 测延迟。
> 结果: **达成**。levers 进生产默认开; src 80.9→99.0%; fact 在噪声带内持平 (95.2% avg, 你定的 93-96% 内); 延迟 +14ms/查询 + 0.5s 一次性启动。full eval 闸抓到少数真稀释, q02 已修, 其余记残留。

## 改动 (code)

| 文件 | 改动 |
|------|------|
| `server/config.py` | 加 `structured_lookup_enabled=True` + `hybrid_enabled` 翻 True (均 `SDTM_RAG_` env 可关) |
| `server/main.py` | lifespan 转发 5 杠杆参数; 计时 init; log 杠杆态; **hybrid-on-without-S1 守卫 warning** (Rule D M-1) |
| `server/rag.py` | **embed-once 重构** (query 嵌一次复用, S1 多次往返→1); **q02 修复** (单域 spec 查询注入 4 chunk); `_embed_query` 加 429 退避 (Rule D M-2) |
| `server/router.py` | `/info` 暴露杠杆态 |
| `eval/run_eval.py` | 加 `--temperature` (确定性配对必需) + answer_preview 300→600 (取证) |

## 验证闸 (全过)

| 闸 | 方法 | 结果 |
|----|------|------|
| 检索未腐化 | retrieval-only v2 102q (Step 0) | single 100/cross 96/concept 100/mixed 100/**99.02%** = 复现 P1 |
| embed-once 行为保持 | retrieval-only 逐题 == Step 0 | **逐题字节一致** ✓ |
| embed-once 真省 | 2-target S1 query 计 embedding 调用 | **1 次** (重构前 3) ✓ |
| 单测 | pytest scripts/tests/ | **214 passed** ✓ |
| FastAPI 启动 | TestClient /info | 杠杆 on, startup 0.41s ✓ |
| Rule D 代码审 | `oh-my-claudecode:code-reviewer` (异 type) | APPROVE_WITH_NITS, 2 MEDIUM 已采纳 ([[prod_wirein_rule_d_review]]) |
| **Full eval 配对闸** | DeepSeek temp=0, v2 102q, OFF vs ON | src **80.9→99.0**; fact 96.3→95.2 (噪声带内); 见下 |
| **Rule A 语义抽检** | `oh-my-claudecode:scientist` (异 type) KB 核验 n=15 | 4 better/6 equal/2 artifact/**3 real-worse** ([[prod_wirein_rule_a_semantic_judge]]) |
| q02 修复后检索闸 | retrieval-only 全类仍 ≥95% | **99.02% 未动** ✓ (composition 改, recall 不变) |
| 延迟 | bench_latency.py | 启动 BM25 +0.5s 一次性; 每查询 +14ms p50; S1-fired p50 116ms (embed-once 生效) |

## Full eval 配对 (DeepSeek temp=0, OFF → ON-fixed)

| 类别 | src | fact |
|------|-----|------|
| concept | 92→100 | 97.7→97.3 |
| cross_domain | 52→96 | 96.7→92.7 |
| mixed | 80→100 | 95.0→95.0 |
| single | 98→100 | 96.0→95.7 |
| **avg** | **80.9→99.0** | **96.3→95.2** |

cross fact 92.7 是唯一 <93, 语义裁判判定**主要是 substring 假阴** (q34/q66 丢 token 不丢事实; OFF 在 q34/s05 反而**编造/错误**)。fact 净 -1.1 在 DeepSeek temp=0 **残留非确定性**噪声带内 (实测 q78 context 未变但答案变, 证明 provider 非确定)。

## q02 修复 (保留, 用户 2026-06-09 ack)

- **机制**: S1 resolve() 恰返回单个域 spec.md (纯单域查询) 时, 注入该文件 4 chunk (非 1), 让模型有足够变量行枚举。`_SINGLE_DOMAIN_SPEC_CHUNKS=4`, 最窄触发。
- **效果**: q02 33→67 (枚举出 STUDYID/DOMAIN/USUBJID/SUBJID/SITEID/SEX 表; 残留 miss RFSTDTC/AGE 是 **gold 标错**——KB 标 Exp 非 Req); q24 67→100 (附带正向)。
- **代价 (诚实记)**: 把广度问题从"枚举全部"挪到"多变量具体问" → **q100 100→75** (问 ARMCD+ETCD, 4 个注入 chunk 全关于 ARMCD, 把 ETCD 挤出 → 模型 punt ETCD)。net 语义正向 (q02+q24 > q100), 但**是 relocation 非消除** = 复盘所述 precision/recall 前沿。
- **决策**: 保留 (q02 是高频题, net 正向), **停手不再调** (避免 whack-a-mole, 遵复盘教训)。

## 残留 known limitations (不修, 已 ack)

1. **q100 类** (多变量具体单域问): 4-chunk 注入偏向首个变量, 可能挤出第二个。前沿固有 (top-15 预算 + composition)。
2. **q37** (special-purpose 误判): 答题模型过度采信注入的关系类 chunk。干净修=答题侧提示护栏 (用户选不动提示词)。
3. **q93** (编 "INJECTABLE C42899"): 已检索对的源仍幻觉。答题侧, 检索修不到。
4. **C-code 幻觉** (q90/q91/q93 给对取值配错 NCI 码): **off/on 都有, 非杠杆引入**, 答题侧通病。干净修=提示护栏 (declined)。
5. **q73** (P1 既有残留, cross): 分布题 gold=model/06, 未顶进 top-15。cross 仍 96% 达标。

## 方法论备注 (规则 A)

- **substring fact-recall 是结构检查, 不可单独判业务**: 多个"掉分"实为假阴 (答案对/更好但 token 不匹配)。必须语义裁判 override。
- **DeepSeek temp=0 仍有残留非确定性** (MoE 路由): 配对 fact 比较有 ~±1pt 噪声底; src (确定) 的 +18pt 是硬增益。
- 评测 gold 双向有错 (q02 期望 Exp 当 Req; q37 期望 relationship dataset 当 special-purpose) → 扩题集时需修。

## 现成可复用资产 (默认 off, eval 用)

`eval/prod_wirein/`: `analyze_paired.py` (配对分析) + `bench_latency.py` (延迟) + `forensic_answers.py` (取证全答案) + 所有 raw JSON/log。`run_eval.py --temperature` flag。
