# Study RAG 确定性轨收官 → Plan B 交接 (2026-08-04)

> 下个 session 从本文件进入。范围: study 轨 (st01) 确定性轨全部收尾 + 一批基础设施修复。
> 红线: 本文档只含统计与结构描述, 无真实研究名/字段 OID/项目标签。

## 0. 一句话状态

确定性轨 (Plan A) **全部完成并定稿**; 本轮把三层"测量与基础设施在说谎"的问题挖了出来并修掉;
**Plan B (联邦路由) 可以开工**, 但有 3 条硬前置 (见 §5)。

## 1. 当前运行状态

| 项 | 状态 |
|---|---|
| git | `main` 与远端同步, 工作区干净 |
| 服务 | `com.sdtmrag.api` (0.0.0.0:8000) / `com.sdtmrag.ui` (127.0.0.1:8501) / `com.sdtmrag.neo4j` 均在运行 |
| 向量库 | `sdtm_kb_v1` = 4303 chunk (CDISC) / `study_st01` = 959 卡 (**未接入服务**) |
| 索引新鲜度 | 绿 (`python -m scripts.check_index_freshness` 退出 0) |
| 测试 | 全量 **669 passed** |
| **认证** | **已关闭** (`SDTM_RAG_AUTH_ENABLED=false`), 局域网免密访问 (本机 LAN IP 192.168.100.32) |

## 2. 本轮基线数字 (务必用这一组, 旧数字已作废)

| 指标 | 值 | 备注 |
|---|---|---|
| study 轨 source recall | **88.5%** | golden v1.1 / 25 计分题 / hybrid+CJK bigram; 阈值 85% PASS |
| CDISC source recall | **81.1%** | 140 题 / retrieval-only + hybrid |

**已作废的旧数字**: study 轨的 "100%" (v0 题集缺陷所致) 与 "94.7%" (v1, 含结构性白送分题);
CDISC 的 "74.3%" (陈旧索引)。理由见 §3。

## 3. 本轮三层发现 (共同点: 错了但看不见)

### (a) 评测在说谎 — golden set 重做
v0 的 12 题由 controller **看着卡片起草** (出题人=答题人), 题目偏软且覆盖偏科。改为
**protocol 概念驱动**重出 27 题 (25 计分 + 2 反幻觉), form 覆盖 6→18/21。两轮独立审阅
(critic REVISE → verifier REVISE) 每轮都抓到出题人自查漏掉的硬伤。真实基线 88.5%。

### (b) 检索通道在说谎 — BM25 对日文零信号
`bm25s.tokenize` 无日文分词, 整句被切成**一个 token**。修法是 CJK 字符 bigram
(`server/ja_tokenize.py`, 对英文恒等), BM25 单通道 gold recall 12.0%→60.9%,
端到端 83.3%→88.5%。**v0 那个 100% 有一部分正是出题泄漏喂饱了 BM25** (题目里带着
从卡片抄来的拉丁标识符)。

### (c) 基础设施在说谎 — 部署索引长期陈旧
向量库把一个 KB 文件欠切 70% (65 vs 222 chunk), 跨越 chunker 一次演进无人察觉,
CDISC recall 白丢 5.7pt。已重灌 (74.3%→80.0%) 并新增**索引陈旧闸** (内容指纹,
接入 ingest 写戳 / 服务启动告警 / `check_index_freshness` CLI / deploy.sh)。

### (d) 附带: KB 里的中文与一次被驳回的 gold 放宽
- `VARIABLE_INDEX.md` 的中文来自**生成脚本硬编码骨架**, 非源 PDF → 已全部转英文
  (数据行经两种独立方法验证零变化)。`ROUTING.md`/`INDEX.md` 的中文**有意保留**
  (整file注入 system prompt, 是写给模型的指令)。
- 我曾把一题判为 "gold 太窄"并放宽, **经独立复核驳回并撤回**: 核验只做到"文件含答案",
  没做到"**被召回的 chunk** 含答案"。教训已固化进 `check_source_recall` docstring。

## 4. 本轮提交链

`fa91c2e` P2/P3 清账 → `170ee16` golden v1.1 + out_of_scope → `6266e21` CJK bigram →
`879283d` VARIABLE_INDEX 转英文 → `a11dce5` 卡片剥 HTML → `8d520b4` 中文溯源+陈旧发现 →
`fec1074` 索引陈旧闸 → `b56263a` OR 语义 + schema 校验 + gold 放宽撤回

## 5. Plan B 硬前置 (开工前必须处理)

1. **source 判据下沉到 chunk/section 粒度** —— 现在 `check_source_recall` 按**文件路径**
   子串匹配。study 卡片是一卡一文件 (没问题), 但 CDISC 侧有 222-chunk 的单文件, 判别力≈0。
   联邦路由后两库混判, 不解决这条**这类题根本无法正确计分**。metadata 已有 `section` 字段。
2. **hybrid 裁决已完成** (CJK bigram 实装), 但注意混检净效应随题目措辞分布摆动, 接线后需重测。
3. **安全边界必须重新决策** —— 服务当前**局域网免密开放**, 但只服务 CDISC 库
   (源自公开标准)。**Plan B 一旦把 study 库接进 API, 就等于把真实临床研究的字段数据
   暴露给整个局域网**。这必须是一次明确决策 (谁能访问 / 要不要给 study 库单独加门),
   不能作为路由接线的副作用被继承。

## 6. Plan B brainstorm 待定点

- 路由判定: 自动判库 vs 显式切库 vs 双库并查
- 引用标识: 两库混答时来源怎么标, 前端怎么区分
- 结构化直查通道覆盖哪几类 (已知四类, 均为 study 轨实测 miss):
  多卡家族只召回其一 / 近义双卡判别失败 / ID 与语义脱钩的长尾卡 / form 缩写词汇缺口
- CDISC 侧同源问题: 变量索引挤占域 spec, 对**域特定问题**会给错误答案 (跨域聚合值)

## 7. 其余 backlog (非阻断)

- `chapters.py` ≤20KB 整file单块策略 (ch01/ch02/ch03 各 1 chunk) 按检索质量重评
- `expected_facts_any` (facts 侧同样有表面拼写导致的 gold 缺陷)
- 33 道多源题中 13 题疑似应为 OR 语义 —— **诊断已做, 刻意不改**, 须先有 chunk 级判据
  且由非受益方逐题裁定
- 跨重灌漂移做 n≥3 重复实验 (当前 n=1, "±2 题噪声"只是假说)
- 三个下游取证脚本只读 `expected_sources`, 未来若有题用 OR 组会显示为空 gold
- study 轨 4 个已知 miss (§6 四类) —— 用户裁决: **卡片保持纯净**, 全部交 Plan B

## 8. 入口文件

| 用途 | 路径 |
|---|---|
| golden set 定稿 + 检索缺陷四发现 | `sdtm-rag/evidence/checkpoints/study_golden_v1.md` |
| KB 中文溯源 + 索引陈旧 | `sdtm-rag/evidence/checkpoints/kb_chinese_and_stale_index.md` |
| CDISC 4 题定性 + 被驳回的放宽 | `sdtm-rag/evidence/checkpoints/cdisc_gold_scope_review.md` |
| 题集与逐题细节 (gitignore 区) | `sdtm-rag/data/study/st01/eval/` |
| Plan A 计划 (已完成) | `docs/superpowers/plans/2026-07-31-study-rag-deterministic-track.md` |
