# RETROSPECTIVE — KG 价值 eval (2026-06-21, Tier 2)

唯一问题: SP1-3 KG 通道是否真让端到端答案变好 → 决定 SP4/SP5。结论: **SP2 是价值, SP3 端到端≈0, SP4/SP5 不靠答案质量证明**。

## 1. 保留下来的做法 (有效, 下次照做)

- **3-臂隔离设计** (arm0 检索 / arm1 +SP2 / arm2 +SP2+SP3): 纠正了 kickoff 原 2-臂 (会把 SP2/SP3 功劳混在一起)。拎出 ΔSP3 是整个 eval 的关键, 没有它得不出"价值全在 SP2"。
- **反过拟合四件套**: 盲写 (4 写手无 graph 源) + gold 程序导 (gen) + **独立 reconcile (raw-yaml 另一码路, 防 gold 与注入同源共错)** + 独立 reviewer (Rule D)。
- **fire-rate 仪表** (kickoff 没要求, 我加的): 区分 "SP3 没价值" vs "SP3 没触发" vs "触发了没用"。结果 SP3 仅 45% 触发, 是核心发现之一; 没有它会把"没触发"误读成"没价值"。
- **确定性指标为主 (set_recall 词边界+大小写敏感)**: 免疫 judge 缺陷。事后证明关键——judge 在 iv01 判松, set_recall 自动捕获。
- **对抗式 Rule A (独立 critic lane)**: 抓到了 writer/executor 自评必漏的两件事——judge iv01 判松 + 我自己的"relationship 反伤"误判。

## 2. 必须补上的缺口 (下次改进)

- **单 judge 同族风险**: judge=deepseek 与 ds 答题臂同族, 且无第二 judge / majority vote。iv01 判松若不是 set_recall 兜底会漏。下次: 第二 judge 或 judge 校准集。
- **无 n>1 方差控制**: rl05 在 temp=0 仍 1.0↔0.0 摆动 (解码变异), 单样本 ΔSP3 不稳。下次对小 delta 结论应 n≥3 采样定方差。
- **relationship gold 未按问法钉定**: rl08 问"同观测类"但 gold 并入 curated DM (越类) → 罚正确答案。aggregate 阈值已按 strict/inclusive 钉定, relationship 应同样按"同类问 vs 关系问"钉定 gold。(已记入 checkpoint 建议; 不影响 verdict。)
- **provider 配额未预估**: gpt54 arm2 跑空 OpenAI 配额 (见 failures/)。贵模型作确认臂前先确认配额够 N 臂。

## 3. 关键决策复盘

- **纠正 kickoff 的实验设计**: kickoff bash 的 ON 臂漏 `--structured-answer` (非生产配置且混淆 SP2/SP3)。读 run_eval 源码发现两 flag 独立 → 改 3-臂。**教训: 立项文档的命令也要过代码核, 别照抄。**
- **模型替换链**: Sonnet (生产默认) 被 Anthropic 余额卡 → gpt-4o (用户问性价比时指出 4o 已 legacy) → gpt-5.4 真前沿 (但配额耗尽 arm2)。**verdict 不依赖任何单一第二模型, 设计上对模型替换鲁棒。**
- **最大教训 — 差点下错结论**: 我基于初版数据写了"SP3 注入反伤 relationship"。独立对抗 Rule A 证实那是 rl05 (SP3 根本没触发) 的单题解码变异, ΔSP3 实为 0。**若 writer/executor (我) 自审就会把这个错误结论 ship 出去 → 直接印证规则 D/A: 同 context 自审 = 无审。** 而且这个更正不是削弱而是强化了主结论。
- **盲写 vs 触发率张力**: 自然措辞经常不命中 SP3 极窄触发词。坚持不为凑触发改措辞 (反 example-tuning, 用户敏感点), 把低触发率作为诚实发现报出 → 它本身成了对 SP4 决策最有用的输入 (瓶颈是 NL 路由不是图能力)。
