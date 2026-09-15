# RETROSPECTIVE — DM1 域级映射题检索补齐 (2026-09-15)

> 起源: dogfood ⚑ 2026-09-15 13:27 (「sdtm 的 ds domain」被缩窄成单一表单). 计划 `PLAN_domain_mapping.md`, 实施计划 `docs/superpowers/plans/2026-09-15-domain-mapping-retrieval.md`, 闸 `evidence/checkpoints/dm1_gates.md`.
> 终态: T1-T8 DONE (11+1 commits, 三闸零回归, 映射 gold 10%→20%: 定义段 8/8, 候选卡 0/32); T9 e2e 待用户 kickstart; T10 D4 待裁; 本文即 T11.

## 1. 保留下来的做法

- **先零 LLM 复现再归因**. 用生产引擎 + 重构问句跑 retrieve, 5 分钟内把「模型幻觉」排除, 定位到检索三重失明 (大小写 / 定义段缺席 / 泛词挤占). 以后每条 ⚑ 都先这样做, 不先改 prompt.
- **盲出题 gold + 改前基线 + 逐题 IDENTICAL 闸**. 出题 agent 不看 server/; 8 题覆盖 6 域三语言; 每个 task 单独过 140q/48q 逐题闸. T3 的 dm05 暂降、T5 的 q47 回归都是被这个闸当场抓住的.
- **每个 lever 的四件套**: config 开关 → main.py 接线 → run_eval `retrieval_levers` 记实收值 → `check_code_grounding` 缺键=OFF 读回 + 两条 fidelity 测试. T4 review 抓出漏项后固定为模板, T5/T6 照抄零返工.
- **红线闸 + 代称表**. committed 文档一律用 F_DISC/F_REG/I_* 代称, 真值放 gitignored `data/study/st01/eval/dm1_codenames.md`. gold/run JSON 全部留在 gitignored 目录.
- **失败归档不删** (规则 B): `evidence/failures/dm1_step0_attempt1.md` (漏 S1 开关), `dm1_task3_attempt_1.md` (dm05 暂降), `dm1_task5_attempt_1.md` (label+structure 回归 q47). 三份都被后续 task 直接引用.

## 2. 必须补上的缺口

- **study 侧候选卡 0/32**. D1/D3/D5 全部只作用在 CDISC 侧; 纯日文 label 的里程碑卡对英文域名扩写零响应 (T5 独立尺子 `eval/prod_wirein/repro_t5_study_expand.py`: 目标表单内卡片 18/40→16/40, gold 0/32). D4 「域→候选表单」人手表触发, 交用户裁; 裁前先做区分实验 (gold 卡正文直接当 query 能否进 top-8).
- **答题层未验证**. 所有证据都是检索层 (top-k 组成). 定义段进了上下文后模型是否真的按 DSCAT 类别枚举、是否标推测, 要 T9 用原句 + 2 模型跑 `/api/ask_stream`, 异 agent 判三判据 (规则 A/D). 需用户 `launchctl kickstart`.
- **recall 指标对组成盲**. D3/D5 在三闸上全部「零变化」, 终审用组成实验才证明 IG overview 席位 10→2. 下一单元的闸要加一条组成指标 (目标域 chunk 占席比), 否则会把有益 lever 判成空转 — 本单元一度就这么记的.
- **140q 不触发 D1**. 新正则在 140 题上 0 次命中, 零回归对 D1 不构成证据; 安全性只靠阻断表 + 单测. 17 个词典词域码未阻断 (需相邻域词才触发). 若要真闸, 要一组小写/中日文问法的 CDISC 题.
- **gold 粒度**. 8 题的候选卡是出题者从每表单挑的 4 张具体 item, 同表单其它卡进了 top-5 也算 miss. 「候选表单齐」应改成表单级判据 (T5 的 in_form 尺子就是雏形).

## 3. 关键决策复盘

- **D1 大小写 + 锚定** (对). 用户原句是小写 `ds domain`, 不修这一条后面全白搭. 阻断表用「小写且是常见英文词」而不是全部两字母码, 保住了 IS/BE 的大写用法.
- **D2 定义席从 S1 自己的配额里出** (对). 席位总数不变, 140q 单域题 100% 不动. T4 review 的「泛用变量 (DOMAIN/USUBJID) 不算变量级」裁定是必要修正, 否则「DS DOMAIN」这种最常见写法会静默失效.
- **D3 收窄为 label-only** (对, 靠闸). structure 字段是跨域通用模板句, 喂进去让 q47 回归; 实现者按闸归档后收窄, 并把回归钉成测试.
- **D3/D5 默认开** (终审后裁定). recall 零变化但组成实验证明 IG overview 挤占减半, 且有 kill switch. 代价: 60/140 题 top-5 顺序变了而 recall 不动, 非 gold 席位的隐性回归要靠 T9 e2e 才看得见.
- **D4 不在本单元做** (对). 它是唯一往语料注入人工映射判断的路径, 与「只放出典」原则有张力, 且数据 (0/32) 现在才拿到, 裁定应基于数据.
- **流程失误**: T3 修复轮与 T4 实现并行, 共用 git index 撞车 (d8ab784 一度吞掉 T4 的 10 个文件, 已 reset 恢复, 历史干净). 规则: 修复轮不与下一 task 实现并行; commit 只用显式路径.
- **数字口径失误两次**: Step 0 漏 `--structured-lookup` 得 80%; T5 对 51 条 results 平均得 88.24% (真值 87.5%, 3 题 out_of_scope). 规则: 只认 run JSON `summary.source_recall_avg`; 实测必附命令 (T5 的 study 侧「2→4 张」正因无命令被 review 打回, 补尺子后结论反转).
