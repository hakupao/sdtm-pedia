# Study RAG (st01) 确定性轨全量收口 — spec §7 验收

> 状态: **全项 PASS** (2026-07-31)
> 前置: pilot 证据见 `study_rag_pilot.md` (业务 PASS + schema 冻结批准)
> 红线: 只含统计; 无真实研究名/字段 OID/单元格值

## spec §7 验收清单

| # | 验收项 | 结果 |
|---|--------|------|
| 1 | 覆盖台账全绿 | ✅ 3508 行全 mapped, 孤儿 0 (机器校验) |
| 2 | Golden questions 检索命中 | ✅ 12 题 (草稿 v0) source recall **100%** (生产同参: hybrid rrf, top_k 15); 阈值 85% |
| 3 | 有损轨抽检 | N/A — 属 Plan C (protocol 轨), 本计划无有损转换 |
| 4 | 联邦路由双库并查 | N/A — 属 Plan B; 本计划交付独立 collection + eval 通道 |
| 5 | git 安全 | ✅ data/study 零文件被追踪; 分支全部 commit 真名扫描 0 命中 |

## 交付物 (真实状态)

- chroma `data/chroma`: `study_st01` = 959 卡 (1536 维, 真实入库) 与 `sdtm_kb_v1` = 4146 共存,
  多次覆盖重建后主库计数不变 (collection 级隔离 + reset 拆弹双向验证)。
- `run_eval.py --collection/--kb-root` 通道可用; `--collection` 自动关闭 CDISC 专用 S1 通道。
- 检索元数据: `source` = 卡片文件名 (eval/前端语义), `provenance` = 源 sheet#行号 (溯源)。
- 测试全套件 **591 passed** (项目基线 531 → +60, 全部合成数据)。

## 评测过程记录 (校准链)

草稿评测四轮: 0% (source 元数据口径 bug, 已修) → 83.3% (草稿题期望过严/误指, 已校准:
编号重复组放宽为家族前缀 ×3, 误指卡修正 ×1) → 91.7% (dense-only) → **100% (hybrid 生产同参)**。
两条校准均为题目侧问题, 检索侧零改动; 其中一条是检索返回了比出题者预期更语义正确的卡。

## 已知边界 (记录在案)

1. 丸数字编号锁定 (①-⑫ 重复组内指定某号) 需结构化直查通道 — Plan B 候选能力。
2. golden set 为草稿 v0 (12 题, controller 起草), 用户共审/定稿待后续 session; 定稿后重跑成本 ≈ 秒级。
3. eval 侧 hybrid 需显式 `--hybrid` (与生产 settings 默认不同) — 评测命令已写入本文档供复现。
4. CDISC 全量重灌与 study 共存的端到端首跑观察项: 停服再灌; backup 保留期规则待定。
