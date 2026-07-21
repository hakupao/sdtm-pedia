# SP2 Phase 1 — RETROSPECTIVE (规则 C)

> 2026-06-20 收尾。SP2 = 确定性结构化答题通道。Phase 1 (答题通道, 不碰检索) DONE + 默认 ON。
> 上游: spec `docs/superpowers/specs/2026-06-19-sp2-structured-answer-design.md` · plan `docs/superpowers/plans/2026-06-19-sp2-structured-answer.md`。
> 证据: `evidence/checkpoints/sp2_phase1_paired_eval.md` · `evidence/checkpoints/sp2_phase1_ruleA_audit.md` · `evidence/failures/step_13_attempt_1.md`。
> 流程: brainstorming → spec → writing-plans → subagent-driven (每组 implementer + spec审 + 质量审 + fix loop)。

## 1. 保留下来的做法 (keep)

- **真实评测当验收 oracle, 不只信单测**。140q paired eval 暴露了接地闸 36 个假阳性——而那时所有单测都绿。这是「结构检查 ≠ 语义检查」的又一次实证: 单测验的是构造好的 case, 真实双语 LLM 答案里的数字形态完全不同。**任何会改用户可见输出的逻辑, 必须在真实答案语料上验, 不能只靠单测。**
- **两道独立验收门各抓到不同类缺陷**, 都是程序门 (fact_recall) 漏掉的:
  - Rule D (异 subagent_type 独立代码审) 抓到闸精度风险 + 词典词锚定。
  - Rule A (N=8 独立语义抽检) 抓到 q67 幻觉 (模型答「106 变量」, 真值 123, 而 fact_recall 还给 1.0 子串假阳)。
  - **结论: 规则 A/D 不是仪式, 是真能抓到自动指标盲区的错。继续严格执行。**
- **改了闸之后, 把修正版重新套到已保存的 140 个答案上 (oracle), 而不是重跑整轮评测**。省钱省时, 迭代快。同样适用于任何「改了下游处理逻辑、想验证对历史输出的影响」的场景。
- **反过拟合硬纪律有效**: 逻辑里零硬编 q-id / 变量名 (实体词表全来自 meta.yaml)、held-out 探针 (非测试集变量/域/CT)、must-fire/must-not-fire 电池。独立审 grep 确认零违规。
- **保守设计原则「漏纠可接受, 错纠是 bug」**: 闸 v2 的「缺席前提」(正确值在答案中出现就绝不追加) 把这条原则落进代码。注入也是 recall-additive (只加真事实)。这套「宁可少做、不可做错」的取向是答题通道能默认上线的根本。
- **subagent-driven 分组**: 把紧耦合同文件的 task 合一个 implementer, 仍走 spec审 + 质量审。granularity 合适, review 不爆。

## 2. 必须补上的缺口 (gaps → backlog)

- **接地闸的「数字归属」在 plan 阶段欠设计**。原 plan 的闸是「主语整句里任何整数 ≠ 期望 = 矛盾」——这个 heuristic 没扛住真实双语答案 (术语数/字符限值/章节号全被误判)。**教训: 涉及自然语言数字抽取的确定性闸, 要么上来就把「数字指代什么 kind」设计清楚, 要么先在真实答案样本上原型验证再锁 spec。** Phase 1 靠两轮重建 (v1 粗 → v2 精 → q67) 补回来了, 但本可在设计期省掉。
- **词典词变量锚定 (Rule D MAJOR #1)**: RACE/SEX/AGE/ARM 这些既是真实变量又是常用英文词, 没像 2 字母域代码那样上 SDTM-context 门。"How many RACE categories" 会注入「RACE 在 1 个域 DM」这条不相关真事实。非破坏性 (recall-additive), 但是最大残余精度缺口。→ 给短/词典词变量锚定加同样的 relevance gate。
- **s05 类 (Rule A PARTIAL)**: 问题点名某域、实则问该域里某变量的 codelist 元数据 (是否可扩展/示例) 时, 通道只注域级事实, 不注那个 codelist 的 extensible/示例 → 模型搪塞 (安全非答, 非错答)。→ 当 query 间接涉及某 codelist 时也注入其元数据。
- **enumerate corpus 路径只出计数不出列表** (Rule D Minor): "list all SDTM domains" 只注「63 个域」不列具体域。→ 补列表。
- **first-seen 属性跨域分歧** (meta_store): role 9 个变量、core 13 个跨域取值不同, 通道只返回首见值, 且不受闸保护。已文档化, 留 **SP3** (按 (var,domain) 建键)。
- **FP2 残余 + 闸角色 open question**: 正确值缺席 + 同句有无关但 kind 词邻近的合理数字时, 闸会追加一条「冗余但为真」的更正 (140 题里 35 次 fire 前提下 0 次自然发生)。**用户已决策 Phase 1 保留生产追加 (Q5)**; 但「是否改成 eval-log-only (只记录不改答案)」仍是值得复议的产品选择——它能彻底消除 FP2 + 词典词锚定的用户可见影响, 因为注入本身已经把正确计数喂给模型了。
- **双语行为**: DeepSeek 经常用中文答英文问题 (预存行为), 这让任何答案侧文本处理 (闸/校验) 都得双语。Phase 1 闸已双语化; 但这是个贯穿性复杂度, 记一笔。

## 3. 关键决策复盘 (decisions)

- **Q5「闸追加更正块」**: 决策方向对 (确定性兜底有价值), 但 plan 把实现 heuristic 想简单了 → 两轮返工。复盘: 锁「行为决策」(要不要追加) 没问题; 锁「实现机制」(怎么判矛盾) 前应在真实数据上验。用户在评测暴露问题后被请来重新拍 Q5 (选高精度+保留追加), 是对的——把「基于新证据复议已锁决策」做成了显式动作, 而非闷头改。
- **两阶段 (Phase 1 上线 / Phase 2 缓做)**: 验证为好决策。Phase 1 独立可上线 (Q1 锁的「各自独立回归门」兑现), 把脆弱的 structured_lookup 退役 (Phase 2, 全计划最高风险项) 隔离出去单独做。
- **先收 Phase 1 再做 Phase 2** (本次收尾): Phase 1 是真价值 (新能力), Phase 2 是技术债清理; 把验证过的成果先锁住, 让最高风险的退役工作在干净上下文里做。
- **subagent 报告必须独立核验**: 多个 subagent 中途截断 (长评测那个、一个 grounding fix 没 commit、eval 还在后台跑)。每次都独立查了 (commit 在不在? 测试绿不绿? 进程状态?), 抓到了「fix 没提交」和「eval 仍在跑」。**教训: 永远不信 subagent 的「完成」声明, 自己验状态。长时间付费评测别交给 subagent 跑, 用可追踪的后台任务自己驱动。**

## 遗留给 Phase 2 / 后续

Phase 2 (退役 structured_lookup 正则影子 KG → 读 meta.yaml, 含 load-bearing `len==6`) 未开始; 入口 plan §Phase 2 (Tasks 15-18)。上面 §2 的 backlog 项 (词典词锚定 / s05 / enumerate corpus / FP2 角色) 可在 Phase 2 或独立小轮处理。SP3 = 关系/影响查询 (内存图遍历)。
