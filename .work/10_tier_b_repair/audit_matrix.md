# Audit Matrix — 08 Tier B repair

> 所有抽检 / 全检结果汇总. 失败行不删 (规则 B). 规则见 PLAN §5.3.

| Step / 批次 | 内容 | 改动原子 | 抽检 N / 全检 | 种子 | 样本来源 | 独有丢失率 | 忠实度错 | 技术判定 | 业务判定 |
|---|---|--:|---|---|---|--:|--:|---|---|
| T0.4 | 闸变异验证 | — | 3 变异 | — | 删句/改格/删子节 | — | — | 待跑 | — |
| T2.B-PCPP auditor a1 | prose 抽检 + PC Ex1 10 格 + 删除 diff | C=0 (P=56) | N=10 | 20261126 | P−C 对照 10 | 0/10 | 0 | PASS | 待主控 |
| T2.B-TR auditor a1 | prose 抽检 + Ex3 tr.xpt 10 格 + 删除 diff | C=0 (P=13) | N=10 | 20261126 | P−C 对照 10 | 0/10 (范围外 1: VS Overview 缺) | 0 | PASS | 待主控 |
| T2.B-MB auditor a1 | prose 抽检 + 10 随机格 + Ex3 mb/di/relrec/Ex4 全格 + D2 删除 10 行 + fp 回归集 | C=3 (P=61) | N=10 | 20261126 | C 3 + P−C 对照 7 | 0/10 (范围外观察 1: MS 假设 3.b 复制于 MB/assumptions) | 0 | PASS | 待主控 |

## 失败详情
(无)
