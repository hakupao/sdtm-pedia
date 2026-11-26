# Audit Matrix — 08 Tier B repair

> 所有抽检 / 全检结果汇总. 失败行不删 (规则 B). 规则见 PLAN §5.3.

| Step / 批次 | 内容 | 改动原子 | 抽检 N / 全检 | 种子 | 样本来源 | 独有丢失率 | 忠实度错 | 技术判定 | 业务判定 |
|---|---|--:|---|---|---|--:|--:|---|---|
| T0.4 | 闸变异验证 | — | 3 变异 | — | 删句/改格/删子节 | — | — | 待跑 | — |
| T2.B-PCPP auditor a1 | prose 抽检 + PC Ex1 10 格 + 删除 diff | C=0 (P=56) | N=10 | 20261126 | P−C 对照 10 | 0/10 | 0 | PASS | 待主控 |
| T2.B-TR auditor a1 | prose 抽检 + Ex3 tr.xpt 10 格 + 删除 diff | C=0 (P=13) | N=10 | 20261126 | P−C 对照 10 | 0/10 (范围外 1: VS Overview 缺) | 0 | PASS | 待主控 |
| T2.B-MB auditor a1 | prose 抽检 + 10 随机格 + Ex3 mb/di/relrec/Ex4 全格 + D2 删除 10 行 + fp 回归集 | C=3 (P=61) | N=10 | 20261126 | C 3 + P−C 对照 7 | 0/10 (范围外观察 1: MS 假设 3.b 复制于 MB/assumptions) | 0 | PASS | 待主控 |
| T2.B-LB auditor a1 | prose 抽检 + 补抽 N1-N15 + 通用表 10 格 + Ex1 10 格 (+全格目视) + Ex2/Ex3 全格 + 删除 X-1..X-4 | C=7 (P=45) | N=10 | 20261126 | C 5 + P−C 对照 5 | 0/10 (范围外观察 1: p196_a017 在 RELSPEC 非 BS) | 0 | PASS | 待主控 |
| T2.B-DS auditor a1 | prose 抽检 + 补抽 N-1..N-12 + p158-167 全量 106 原子正反扫 + 10 随机改动格 (渲染) + D-1..D-5 删除核 | C=0 (P=51) | N=10 | 20261126 | P−C 对照 10 (+N 组 12 补抽) | 0/10 (范围外观察 0; p161_a0012 原子抽取错 DSCAT) | 0 | PASS | 待主控 |
| T2.B-CP auditor a1 | prose 抽检 + 补抽新增 6/24 + 删除 6/20 + 全量忠实/丢失反扫 + 15 随机格 (渲染) + USUBJID 折行 + fp 回退集 | C=25 (P=100) | N=10 (+12 补抽) | 20261126 | C 5 + P−C 对照 5 | 0/10 (观察 1: CPGATEDEF 照录 vs T-2 改正口径不一) | 0 | PASS | 待主控 |
| T2.B-EX auditor a1 | prose 抽检 + 10 随机格 (Ex6 ec/ex, Ex7 ec; 渲染) + Ex7 CRF 勾选全核 + 删除行核 + fp 回归 | C=0 (P=36) | N=10 | 20261126 | P−C 对照 10 | 0/10 (观察 1: p118 "mg/mL" 疑 PDF 印刷错未登记) | 0 | PASS | 待主控 |
| T2.B-ch04 auditor a1 | prose 抽检 + 82 新增句逐字反查 + 本批页 fp 不命中全扫 + lb.xpt/约定表渲染逐格 + KB note 5 + 删除 10 行 | C=30 (P=214) | N=10 | 20261126 | C 7 + P−C 对照 3 | 0/10; 补充全扫 R2 丢失 3 (F1 p42_a015 xref 7.3.1 / F2 p55_a016 原因从句 / F3 p54_a025 URL) | 0 | FAIL | 待主控 (attempt 3 补 F1-F3) |
| T2.B-IS auditor a1 | prose 抽检 + p233-241 全量正反扫 (独立脚本) + 10 随机格 (Ex5 4 + 其他改动表 6; 渲染) + Ex5 整表目视 + D-1..D-5 删除核 + fp 回归 | C=1 (P=67) | N=10 | 20261126 | C 1 + P−C 对照 9 | 0/10 (观察: T-5 语法补全建议 T4 告知) | 0 | PASS | 待主控 |
| T2.B-model01 auditor a1 | prose 抽检 (正式 N=10 + 扩展 25) + sv20 pp4-12 169 原子正反全扫 (独立脚本) + D-1..D-14 删除核 (含终态 D-13/D-14 对 p15/p20) + T-1 核 + fp/links 回归 | C=28 (P=75; R3 新增 C'=124) | N=10 (+25 扩展) | 20261126 | C 5 + P−C 对照 5; 扩展 C' 13 + 对照 12 | 0/35; 全扫 0 | 0 | PASS | 待主控 (注: 续3 delta 无 reviewer 复审签字, auditor 已独立复核) |
| T2.B-ch02 auditor a1 | prose 抽检 + p11-16 独立双向全扫 (chk.py) + 3 表→bullet / §2.7 20 bullet 渲染核 + 删除 10 行 + D6 note 2 + §1.4.1 摘录核 + fp 隔离复跑 (回归 0, 仅 p15_a006) + md5 | C=32 (P=104) | N=10 | 20261126 | C 5 + P−C 对照 5 | 0/10; 全扫忠实度 1 (F1 ch02:203 KB 自写标题 "not fully evaluated" vs PDF "have not (yet) been evaluated"); 观察 O1 §1.4.1 截断无标记 (非阻断) | 1 | FAIL | 待主控 (改 :203 → reviewer delta → auditor a2) |
| T2.B-ch02 auditor a2 | prose 抽检 (新 seed) + p11-16 双向全扫 + KB 自写标题全扫 (F1 :167 / :158 / :178 vs p16) + §1 去重 D-24..27 核 + fp 隔离复跑 + links + md5/trace | C=32 (P=104) | N=10 | 20261127 | C 5 + 余数 5 | 0/10; F1 关闭; hit_any −4 (p9 a009/a020/a021, p10 a004; target=ch01 → B-ch01) | 0 | PASS | 待主控 |
| T2.B-EG auditor a1 | prose 抽检 + Ex1 10 格渲染 + Ex2/Ex4 改格 + 删除 diff | C=1 (P=17) | N=10 | 20261126 | C 1 + P−C 9 (含 DD 对照 3) | 0/10 | 0 | PASS (F-1 spec 首句非阻断待主控) | 待主控 |

## 失败详情
- T2.B-ch04 auditor a1 FAIL: seeded 样本 0/10, 但本批 kb_files/页内 R2 丢失 3 处 (F1-F3), 详见 evidence/checkpoints/t2_B-ch04_audit.md §3.
- T2.B-ch02 auditor a1 FAIL: seeded 样本 0/10, 但全扫发现 ch02:203 KB 自写小标题 "not fully evaluated" 与 PDF p15/p16 "have not (yet) been evaluated" 改义 (F1), 详见 evidence/checkpoints/t2_B-ch02_audit.md §2.
