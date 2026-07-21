# RETROSPECTIVE — AGG 独立答题通道 (2026-07-07, Tier 2)

目标: 价值 eval 两条榨值建议落地 (拓宽 aggregate 触发面 + 通道独立化)。结果: **DONE 默认 ON, e2e Δ+41.7pp, 诚实披露口径收口** (阈值族 novel 盲题 100% / 最高级族 25%, 长尾入 backlog)。

## 1. 保留下来的做法 (有效, 下次照做)

- **novelty check 进盲写门** (本单元最大流程沉淀): 同一 need card 跨轮盲写会措辞收敛, "fresh held-out" 不查重就会高估泛化 (r3 与烧毁集 4 逐字 + ~7 近逐字, 每个 task 审查都没抓到, Rule D 全量审抓出)。工具 `eval/novelty_check.py` (内容词 Jaccard ≥0.6), 下次盲写门直接复用。
- **失败门 → 形状类修 → 全新盲写** 的循环纪律: 两次门失败 (4/16, 12/16) 都归档 (规则 B)、只按语言形状类补 pattern、每轮换新盲写集。Rule D 逐条判定 9 组 pattern 无一按题硬编 — 纪律闭环成立。
- **审查者对抗式实测探针** (不只读 diff): 两轮抓出 4 个测试盲区真缺陷 (负向守卫只护一个分支 / 量化 dozen 错数值 / 跨从句过宽 / 版本号误触发); 修复者反向抓出审查处方本身的洞 ("2 dozen" 间隙词路径) — 双向制衡有效, 比单向审查强。
- **e2e 数字必须独立复算**: ON 臂 100% 这种漂亮数字, task 审查独立重算逐题吻合才可信; Rule A 再用第三码路 (raw yaml + 自写 fact_present) 核了 6 样本。
- **烧毁集不弃**: 每轮 burned held-out 保留为回归资产 (r1/r2 各 15/16 持续监控), 修复不回退旧覆盖。

## 2. 必须补上的缺口 (下次改进)

- **盲写门设计之初就该带 novelty check** — 本单元是 Rule D 事后抓出才补; 以后任何 "fresh held-out" 门, novelty check 是门的一部分而非事后审计。
- **need card 措辞会泄进写手输出**: 卡片说 "N or more" 写手就倾向写 "or more"。下次卡片语义要提前多样化 (本单元补充轮才这么做)。
- **最高级家族的措辞长尾没有词法解**: 3 轮数据点 (每轮挖出新同义表达: reach/adopted/top ones/champion...)。已造册 KL-4; 若 dogfood 显示尾巴频现, 立项 embedding/LLM 意图识别 (新设计单元, brainstorm 硬门), 不要再加第 10 个 regex 家族。
- **注入侧维度错配 (MED-3) 是唯一可能致错答的类** ("largest number of terms" 注入 by-variables 排名): backlog 优先, spread-noun 宾语限定。
- **provider 无关但流程有关**: 一个 implementer 的 `git add -A` 扫进同仓并行产物 (自纠了); 多 agent 同仓并行时 commit 要用显式文件清单。

## 3. 关键决策复盘

- **「诚实披露收口」vs 继续追 fire-rate** (用户决策): r3 形式过门 (15/16) 但 novelty 修正后真实泛化 50% (阈值 100%/最高级 25%)。选择如实分族披露而不是: (a) 拿形式 15/16 当真 (假 PASS), 或 (b) 无限 whack-a-mole。依据: 通道静默零伤害 + 触发时 Δ+41.7pp + 长尾成本收益要真实使用信号 (⚑) 说话。这是「规则 A 精神」(业务 PASS ≠ 程序 PASS) 的正确应用。
- **anchor 同义词 (datasets/vars) 修 vs 不修**: 判定为生产词库缺陷而非 example-tuning (SDTM 用户日常混用 dataset/domain), 修后阈值族 novel 4/4 — 类判断正确。分界线: 同义词 = 词库缺陷可修; 新句式家族 = 形状类要走失败驱动; 隐喻 (champion) = 不修。
- **Rule D 用最强模型 + 异 type 是值回票价的**: HIGH-1 (盲写收敛) 是全流程唯一没有任何其它 lane 抓到的问题, 而它直接改写了收口叙事。省这个审 = ship 一个高估的 "15/16 fresh"。
- **默认 ON 先于 Rule D/A** (plan 自带顺序): 本次无害 (审计全过), 但顺序上有暴露窗口; 下次 plan 把翻 ON 排在 Rule D/A 之后。
