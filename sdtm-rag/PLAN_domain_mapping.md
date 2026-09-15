# PLAN — DM1: 域级映射题的检索补齐 (「本研究哪些数据进 X 域」)

> 状态: **进行中** (2026-09-15 开工) · Tier 2 · 进度 `_progress_domain_mapping.json`
> 起源: dogfood 2026-09-15 13:27 (DS 域被缩窄成 F_DISC); 归因 `evidence/checkpoints/dogfood_ds_domain_2026-09-15.md`
> 用户定调 (2026-09-15): EDC→SDTM 映射文档不存在, 系统上限 = **定义齐 + 候选表单齐 + 标推测** 的推理; 这是今后最需要的能力. 修法必须是**模式级** (任意域/任意问法), 不是只修 DS.

> TL;DR: 「sdtm 的 ds domain」这类问句里唯一有信息量的 token 是两个字母的域码, 而现有检索对它三重失明: S1 域名识别只认大写; 命中域后只填变量行不带域级定义; `sdtm`/`domain` 泛词把 IG 通论章节顶进来. study 侧则被 OID 前缀锚定到 F_DISC, 纯日文 label 的里程碑卡 (RCT 割付日 / F_REG 登録日 / OC 転帰) 永远进不来. 本单元做四条确定性改动 (域码归一化识别 / 域级定义保底席 / 域码确定性扩写 / 泛词降权) + 问句落盘 + 一组跨域 gold 题闸. 「域→候选表单」人手表 (D4) 单独裁, 默认不做. 风险: CDISC v3 140 题与 study v2 48 题零回归是硬闸, 扩写与降权最可能触回归.

## 1. 需求 (why)

- **背景**: 用户问「本研究中哪些数据适合进入 sdtm 的 ds domain」, 第一轮只答出 F_DISC 两个字段, 追问两轮才自纠. 实测 (零 LLM, 生产引擎) 上下文里没有 DS 定义段, 没有里程碑卡; 模型对上下文忠实, 不是幻觉.
- **核心矛盾**: 语料里 DS 定义 (`domains/DS/assumptions.md` item_1) 和里程碑卡都**存在**, 但检索把它们截掉. 现状 = 有知识拿不到; 要求 = 域级映射题上下文必须含「该域定义 + 该域相关的候选卡片」.
- **衍生需求**: 服务端不落盘问句, 下次 ⚑ 仍无法复现第一轮 (本次只能用重构句).

## 2. 方案候选

| # | 路径 | 可达效果 | 核心问题 |
|---|---|---|---|
| A | 只改 prompt (规则句「先按定义枚举事件类别再逐表单找」) | 便宜 | 定义段不在上下文, 规则句无原料; 只能靠参数知识, 与反捏造护栏冲突 |
| B | **确定性检索层 4 改 + 落盘 + 跨域 gold 闸** | 任意域/问法生效; 零 LLM; 可复现 | 扩写/降权可能动 140+48 题基线, 需逐题 IDENTICAL-or-better 闸 |
| C | B + 人手「域→候选表单」表 | study 侧候选卡齐 | 往语料注入人的映射判断, 与「只放出典」原则有张力 |
| D | LLM 查询改写 (hard 组) 专修映射题 | 覆盖面广 | 不可复现; 每题多一次 LLM; 与 U1 多模型切换纠缠 |

## 3. 决策

- **选 B**, C 的人手表作 D4 待裁 (用户裁), A 的规则句并入 B 作末道护栏 (Task 7), D 不做.
- 边界决策:
  - **D1 域码识别**: 归一化 (casefold) 后查 meta.yaml 域表; 认 `DS`/`ds`/`DS域`/`DSドメイン`/`ds domain`. 2 字母 token 只在**明确域语境**下认 (后接 域/ドメイン/domain/dataset, 或前接 SDTM/sdtm), 防 `is`/`or`/`AE` 常词误触 (AE 本身既是域码也是常见缩写, 旧行为大写 AE 已认, 不收紧).
  - **D2 域级定义保底席**: S1 命中域 X 时, 第一席固定给 `domains/X/assumptions.md` 的首条 (section `item_1`, 无则 `overview`), 之后再按向量填变量行; 总席位不变 (保底席从 S1 自身配额里出, 不抢 cosine 席).
  - **D3 域码确定性扩写**: 识别到域 X 时, 把 meta.yaml 里 X 的正式名 + assumptions 首条前 N 个名词短语 (确定性抽取, 不用 LLM) 追加到检索用 query 副本 (仅用于 dense + BM25, 不改写用户原句给 LLM). CDISC 引擎与 study 引擎共用同一扩写 (federation 层做一次).
  - **D4 人手「域→候选表单」表**: 默认不做. 若 Task 9 gold 闸显示 study 侧 milestone 卡 recall 仍 < 50%, 提交用户裁.
  - **D5 泛词降权**: BM25 侧停用词加 `sdtm/cdisc/domain/dataset/データ/ドメイン` (仅 query 侧剔除, 不重建索引).
  - **D6 落盘**: `ask_stream`/`ask` 记一行 structlog: question[:100], routed corpus, chunk ids; 不记答案.
- **风险与应对**:
  - 140+48 题回归 → 每个检索改动单独跑闸, 逐题 IDENTICAL-or-better; 任何题变差 = 该改动归档 failures/ 后重做, 不许合并.
  - 扩写词把 study 侧席位从 F_DISC 挪走却仍进不了里程碑卡 (纯日文 label) → 这正是 D4 的触发条件, 数据说话.
  - 规则 A: 新 gold 题 (Task 9) 由**不看检索实现**的 writer 出题, 独立 reviewer 复核 (规则 D).

## 4. 实施 (Step 表)

| Step | 任务 | 输入 | 输出 | 目标指标 | Ckpt | Parallel |
|---|---|---|---|---|---|---|
| 0 | 基线: 跑 CDISC v3 (140) + study v2 (48) 零 LLM 检索; 存 `_before.json` | 现有 test set | `eval/runs/dm1_cdisc_before.json`, `data/study/st01/eval/runs/dm1_study_before.json` | 记录数字 | none | — |
| 1 | D6 问句落盘 (最小, 先上, 与检索无关) | router.py | log 行 + 测试 | pytest 绿 | none | 2 |
| 2 | 跨域映射 gold 题 (6-8 题, ≥4 域, 含 DS 原句+2 重构句), gold = 定义段 + 候选卡; **出题 writer 不看检索代码** | KB + catalog | `data/study/st01/eval/test_set_domain_mapping_v1.yml` (federated, corpus=both) | lint_gold 过; 改前 recall 记为基线 | **hard** (题面给用户过目) | 1 |
| 3 | D1 域码归一化识别 | structured_lookup.py | 代码 + 测试 | 140/48 IDENTICAL-or-better | none | — |
| 4 | D2 域级定义保底席 | structured_lookup.py / rag.py | 代码 + 测试 | 同上; Task 2 gold 定义段 recall ↑ | soft | — |
| 5 | D3 域码确定性扩写 (federation 层) | federation.py / rag.py | 代码 + 测试 | 同上; study 侧非 F_DISC 卡进入 | soft | — |
| 6 | D5 泛词降权 (query 侧) | rag.py BM25 | 代码 + 测试 | 同上 | soft | — |
| 7 | both 模式规则句 (域级映射题: 先按定义枚举事件类别, 再逐表单找状态/日期/原因; 源表单名相似 ≠ 唯一来源) | federation.py | prompt + 钉文本测试 | pytest 绿 | none | 3-6 |
| 8 | 复跑 Task 2 gold + 140 + 48; 逐题 diff | Task 3-7 产物 | `evidence/checkpoints/dm1_gates.md` | gold 整组 ↑ (不只 DS 题); 140/48 零回归 | **hard** | — |
| 9 | 端到端: 用户原句 + 2 重构句走 `/api/ask_stream` (B 臂 2 模型), Reviewer 异 subagent 判「定义齐/候选齐/标推测」三判据; 规则 A N=3 句×2 模型 | 生产服务 (需 kickstart) | `evidence/checkpoints/dm1_e2e.md` | 三判据 PASS | **hard** | — |
| 10 | D4 裁定 (若 study milestone recall < 50%) → 用户 | Task 8 数字 | 决定 | — | hard | — |
| 11 | RETROSPECTIVE_domain_mapping.md; `_progress` 收口; CLAUDE.md Key Path 一行; dogfood 条目回写「已修/复跑结果」 | — | — | — | none | — |

## 5. 验证

- **L1 结构**: pytest 全绿; lint_gold 退出码 0; 两个 before/after run JSON 逐题 diff 脚本输出 0 regress.
- **L2 语义** (规则 A): Task 2 出题独立 (writer 不看检索代码, reviewer 异 agent); Task 9 端到端 N=6 (3 句 × 2 模型) 独立判分, 判据预登记在 `dm1_e2e.md` §0 先于跑题.
- **零回归复跑命令** (登记于实现前):

```bash
# CDISC 140
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup \
  --output eval/runs/dm1_cdisc_after.json
# study 48
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup --collection study_st01 \
  --kb-root data/study/st01/cards --output data/study/st01/eval/runs/dm1_study_after.json
# 映射 gold (联邦 both)
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml \
  --retrieval-only --hybrid --federated --corpus both --output data/study/st01/eval/runs/dm1_mapping_after.json
.venv/bin/python -m pytest -q
```

## 6. 不做

- 不改 KB 内容, 不重 ingest, 不动 doc 轨席位规则 (U3/U6 FAIL 史)
- 不用 LLM 做查询改写
- 不在本单元写「域→候选表单」表 (D4 待裁)
