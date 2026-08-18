# U6 Task 10 attempt 1 — 条款 1 触发 (规则 B 失败归档)

> 2026-08-18 · controller 归档 · 判定详情 `evidence/u6_task10_gate.md` (commit 2a9937c)

## 输入

- 冻结基线: `u6_baseline_run_{1,2,3}.json` (sha 1fe5cda, 254 题, fatal 9, legacy 179)
- 修法: 确定性信号层 (widen-only; study 侧强通道 G1 版 + cdisc 侧词表 Task 9 标定零害版), 冻结于 c07dc96
- after: `u6_after_run_{1,2,3}.json` (sha 6b92857, --signal-layer on)

## 产物

- `u6_gate.json`: rc=1。条款 1 触发 (fatal 8/8/8 ≠ 0; legacy 179 ≥ 178 达标半); 条款 2/3/4/7 全 PASS; 254/254 三遍稳定。

## 技术判定

- widen fire 全集 2 次/遍 (study_sig ×2: `u3_doc_02` + `st01_v2_q07`, 均 cdisc→both, 均修复), cdisc_sig **0 次/遍**。
- 修好 1 fatal (doc_02) + final 组动机题 q07; 剩余 8 fatal (amb×5 + dist×3) baseline pred=study, 需 cdisc_sig, 而其零触发 ⇒ 修法未达而非修坏。
- 零回归: 除上述 2 题外全集零改判; 无收窄/换库形状。

## 业务判定

- 判库欠账部分修复: 打空形态 (study-gold 判 cdisc) 的 2 题被修; study→both 方向的 8 题债务原样。
- 失败根因: 规则 (a) (可见集 legacy 不降) 逼出的 cdisc 词表零害标定, 在封存组上同样零触发 —— **零害与有效在这份词表上不可兼得** (可见集无该方向的正例可标定)。
- 条款 1 的 fatal=0 全有或全无口径下, 部分修复 = FAIL。

## 下一 attempt 的输入 (若开新单元)

1. cdisc_sig 的标定困境是结构性的: 可见集 (legacy+dev) 没有「gold=cdisc/both 而被判 study」的活正例 (visible fatal=0), 任何零害约束都会把词表推向零触发。需要新的标定源 (如 legacy 里 2 题非致命错? 或用户授权把部分封存组转可见)。
2. amb 5 题 gold=both 的语义: mapping 类问句的词面特征 (マッピング/対応/どの変数) 在 U3 五轮 prompt 措辞与本次词表两条路上都没接住 — 下一步先做误差分析 (需授权读封存题面) 再谈机制。
3. 存续可复用: 全部 Phase 0 仪器 + 标定台 + (视用户裁定) 信号层本体。

## 处置 (用户裁定 2026-08-18)

预登记 (spec §7 / plan Global Constraints) 写「任一条款触发 ⇒ Phase 1 代码全部 revert」。实测失败形态为「零伤害部分达成」(非预登记设想的修坏型), controller 上报三选项, **用户裁定: 保留信号层 (生产继续启用), 单元按「条款 1 触发, 部分达成」FAIL 诚实收口**。引用纪律: 不得写成「验收通过」; 欠账 9→8 须连同「cdisc_sig 全集零触发」同框引用。
