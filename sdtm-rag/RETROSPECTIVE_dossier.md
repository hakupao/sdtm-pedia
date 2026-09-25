# RETROSPECTIVE — DM2 研读包旁路 (整本喂) (2026-09-15)

> 起源: DM1 D4 区分实验裁定 (`evidence/checkpoints/dm1_d4_discrimination.md`) —— study 侧候选卡 0/32 的根因是「SDTM 域定义 ↔ EDC 日文 label」语义鸿沟, 检索层没有廉价桥。用户裁定: **不做「域→表单」人手表, 走整本喂**。
> spec `docs/superpowers/specs/2026-09-15-study-dossier-design.md` / plan `docs/superpowers/plans/2026-09-15-study-dossier.md` / SDD ledger `.superpowers/sdd/2026-09-15-study-dossier/progress.md`。
> 终态: T1-T10 DONE (T11 prompt cache 可选未做)。触发默认 ON, 生产已 kickstart; L2 闸 140q 零触发 / 检索零回归; L3 e2e attempt 2 **6/6 PASS** (deepseek 采样, Claude 对比待 Bedrock 权限)。闸 `evidence/checkpoints/dm2_{gates,dossier_tokens,dossier_e2e}.md`。

## 1. 保留下来的做法

- **硬前置的量化闸挡在实现之前** (T2)。写码之前先量研读包 token: 166563 字 → **133652 token**, 两档 (含/去选择肢) 都 ≤ 150K, 用户据此裁「含选择肢」。关键是**把口径写进证据**: litellm 1.88.1 对四个 `bedrock/converse` 模型串全部没命中内置 tokenizer 映射表, 静默回落到 `cl100k_base`, 所以四列数字逐位相同 —— 是一套估计值不是四个模型的原生计数。**静默回落必须当场写明**, 否则后人会把估计值当实测值引用。
- **词类级触发词, 不写题面 example** (T3/T8)。范围词表定义为「研究指代词 + study/試験/研究」, 两次收紧都停在词类级: 剔裸 `EDC` / 裸 `in our` (它们让纯 CDISC 定义题误触发, 每次误触 = 134K token 白烧), 英文分支加 `\b` (`"f<our Trial>"` 跨词边误触发 q29)。两次都补了负例测试, 并同步 spec/plan。
- **零 LLM 的 L2 闸, 三集一起看** (T8)。`cdisc140` 0/140 (不该整本喂的题一次都没触发) + `study48` 0/51 + `mapping8` 7/8, 外加检索层逐题 diff `worse=[] better=[]` —— 证明新通道**没有**顺手改动检索。这套闸零成本可复跑, 是默认 ON 敢开的底气。
- **每个 task 一 commit + 异 agent 审 (规则 D)**。本单元 **19 个 commit** 全在 main (`3453652..5b714bb`, 不含基线; 终审文档 commit 随后跟进 → 20), 每个 task 由不同 agent 审; T1 的数据丢失、T5 的四个接线缺陷都是审出来的, 不是测试抓的。审查发现的每一条都记进 ledger 并当场裁定「现在修 / 归 T10 / deferred」, 没有一条无声消失。
- **失败归档不删 (规则 B)**: `evidence/failures/dm2_task8_attempt_1.md` (q29 误触发), `evidence/failures/dm2_task9_attempt_1.md` (类别轴混淆 4/6)。后者是 attempt 2 的唯一输入 —— 没有它就只能靠记忆重写规则句。
- **红线代称 + pre-commit 闸**。committed 文档一律 `F_xxx` / `I_xxx` 代称, 真值在 gitignored `data/study/st01/eval/dm1_codenames.md`; 判分报告 (含真实 OID) 全部留在 gitignored `runs/` 下, 证据文件只留无标识摘要。每个 commit 均 `CLEAN`, 无一次 `--no-verify`。

## 2. 必须补上的缺口

- **判据 ② 只测 recall 不测 precision** (判分方原话)。AE 题两份答案各点名 200+ 个 OID, 只要把相关几张表整片倒出来, 4 张 gold 卡必然被覆盖 —— 判据拦不住过度列举 (部位字段 / 注释字段被列进 AE 候选, 实际发生了)。下一轮要加**条目级 precision 判据** (点名项目中不该进该域的比例上限), 否则「整本喂」会奖励「整本抄」。
- **判据 ① 对 AE 域是空判据**。AE 的 definition text 不定义任何 `--CAT` 值, 「按域定义列出全部记录类别」在 AE 题上没有可核清单; 两份答案都只能显式改轴, 而「改哪个轴才算合格」判据没写。⇒ ① 只在有 `--CAT` CT 的域上有判别力, 无 CT 的域需要另一条判据。
- **判据 ③ 未规定标记粒度**。「每条归属带 (推測)」与「章节标题级标记」之间没有划线, 本轮按「章节级 > 单一全局免责」判过 (dm05/opus 就是章节级)。若收紧到逐条即会 FAIL。**判据里的模糊词 = 判分时的自由裁量 = 下轮不可比**, 粒度必须写死。
- **「候補なし」分支在 AE 题上完全未被检验**。AE 两份在自选的模块轴下没有空模块, 全篇零「候補なし」声明。规则 ② 的一半 (显式申报无候选) 只在 DS 题上验过。
- **(2026-09-25 更新) 模型维度已补 = attempt 3 业务 FAIL**: Bedrock 恢复后 Claude 两模型 12 run 全真未回退, 按跑前登记的 §0′ (含 3 道留出题) 判 **opus 2/3·2/3, sonnet 1/3·1/3, 均未达标** (`dm2_dossier_e2e.md` §2.3, `evidence/failures/dm2_task9_attempt_3.md`)。要点: sonnet 三道无 CT 域题全部跳过「声明 + 点名替代轴」(与口径无关); 第三个 `DSCAT` 值在 ja 问句上两模型族都再次失守; 捏造首次非零 (2/12); 新增 precision 判据 18/18=0% 无判别力。**「deepseek 6/6」不能外推到生产默认模型 Claude。** 研读包实收 146.8K-155.5K token (Claude 原生), 4/12 越过 T2 的 150K 估计线。
- **(2026-09-25) attempt 4**: 生产 auto 暂停 (`dossier_auto_attach=False`, 用户裁定) + §0″ 判据写死 attempt 3 暴露的歧义 (跑前) + 规则句 pattern 级修订 (异 agent 审, 去掉 DS 色彩旧措辞) → **opus 6/6 (主判; ④″(ii) 严口径 3/6), sonnet 4/6** ⇒ 按「每模型 6/6」仍 FAIL。修订实效: 捏造 2→0 / SDTM 变量捏造 2→0 / 分类轴 7→12 of 12; 同尺子复判 attempt 3 = opus 1/6·sonnet 0/6 (多为 ⑥″ 格式项, 勿读成推断质量)。**教训**: ① 每轮判分都会暴露上一版判据的新歧义 (§0′→§0″→④″(ii) 四形态), 「跑前写死」只能写死**已见过**的歧义; ② sonnet 的语言跟随靠规则句措辞压不住 (两轮同题同病), 下一步应是结构性手段; ③ 6 题已全部见过, 泛化维度须新题。见 §2.4 + `evidence/failures/dm2_task9_attempt_4.md`。
- **(2026-09-25) attempt 5**: 盲出新留出 4 题 (IE/MH/EX/PC 空域) + 回归 2 题; 答题语言改结构性手段 (最后一条 user 消息末尾按问句地の文追加确定语言行, 异 agent 审出「嵌入表单名误判」后加固) → 字面 **opus 5/6 (宽 6/6), sonnet 4/6 (宽 5/6)**, 仍 FAIL。**语言问题 12/12 解决** (sonnet 两轮同病消失) —— 印证「措辞压不住的就换结构」; 空域「候補なし」分支首次被检验 2/2。opus 唯一失败是示例值里 1 个自造 OID; sonnet 失败分散 (把上下文未见当标准不存在 / 边缘候选 / precision 余量) —— **模型间差距是稳定信号** (attempt 3/4/5 三轮 opus 均 ≥ sonnet)。见 §2.5 + `evidence/failures/dm2_task9_attempt_5.md`。
- **(2026-09-25) attempt 6 (opus 单跑)**: 规则句再补三处 → 主口径 **5/6** (attempt 5 同尺子复判也是 5/6), 失败题从「示例值自造 OID」换成「中文问日文答」。**教训**: 连续两轮同分、失败落在不同低频模式 = 采样尾部; 规则句措辞的边际收益已接近零, 继续逼近 100% 要靠**生成后确定性闸** (OID ∈ 一览 / 语言计数) + 重生成, 不是再写一句话。判据方面, 每轮仍冒新歧义 (本轮: 「专门承载」的定义) —— 预登记能挡「跑后改尺子」, 挡不住「尺子本身会被新答案刺穿」。
- ~~**模型维度缺席**~~ (历史原文保留)。12 次调用全 `fell_back=True` → deepseek-v4-pro。Bedrock 账号当前拒绝 Anthropic 模型 (`Access to Anthropic models is not allowed for this account`), 属账号权限问题不是代码问题。**Claude 两模型在研读包下的表现本单元拿不到**; 重跑命令在 `evidence/checkpoints/dm2_dossier_e2e.md` §4, 权限恢复后需异 agent 重判并另起 §2.3。
- **prompt cache 未做** (T11 可选)。每题 106-108K prompt token 全价, 无 `cache_read_input_tokens`。做不做要等 Claude 真能跑起来 (deepseek 本就不走 Anthropic prompt cache)。
- **`dm08` 型长名前缀问句不自动触发**。问句只给域英文长名前缀 (无域码) 时 D1 识别不出域码 ⇒ 不触发, 需手动 `dossier: on`。本单元不扩 D1 (140q 回归风险), 已写进 spec §8 与 gates。
- **Streamlit UI 不显示研读包徽章 (已知面)**。`ui/streamlit_app.py` 调 `/api/ask` 时**不带** `dossier` 键 ⇒ 后端按默认 `auto` 判定, 该挂就挂; 但它只渲染答案与 sources, **没有** 📖 徽章, 也不落 `dossier` 存档字段。⇒ 从 Streamlit 看到的答案, 「这条吃没吃研读包」在界面上无从判断 (webchat 有徽章)。不是 bug 是未接线面, 记在这里以免下次把它当成「研读包没生效」。
- **PDF 通道共存只接线未验证**。T5 fix 之后 PDF 触发器看的是过滤前 chunks, 两通道可同时触发, 但 PDF 默认 OFF, 端到端共存行为无人跑过。
- **一处事实性漏报未被任何闸拦住**: dm05/opus 把某组项目的区间写成 8 个, 实为 10 个。是 under-count 不是捏造, 码闸只查「是否存在」不查「数得对不对」。区间简写的计数正确性目前**只靠人判**。

## 3. 关键决策复盘

- **D4 → 整本喂** (对, 且是本单元存在的理由)。0/32 的数据先拿到再裁: 人手表要到 item 粒度、是唯一往语料注入人工映射判断的路径; 整本喂用确定性换成本 (每题 +134K token), 把「检索选得对不对」的问题直接消掉 —— study 侧不再检索, B 部穷尽, 「不在一览里就是不存在」变成可断言的前提。
- **T2 token 闸放在实现前** (对)。若当时 > 150K, 收窄顺序 (先去选择肢再收白名单) 也已写死由用户点, 不在代码里静默截。用户最终选含选择肢, 理由是「选择肢是判断字段归属的关键线索」—— 这条在 e2e 里被验证: 答案大量引用选择肢做归属判断。
- **触发误报比漏报贵** (对)。两次收紧都朝「更严」走: 漏触发用户可手动 on 兜底, 误触发是每次 134K token 的静默浪费 + 纯 CDISC 题被 study 内容污染。
- **T1 part-join 数据丢失: 审查抓到, 测试没抓到** (教训)。多 part 章拼回时**续页首行被吃掉** (实测一章丢 2 行), 直接违反 spec §3「与文件字节一一对应」。单元测试当时全绿 —— 因为测试用的是自造的 3 章 tmp 数据, 没有覆盖「续页」形态。**结构测试绿 ≠ 内容对**; 同轮还修了 study/version 取未排序 glob 首文件 (可能命中 `INDEX.md` → `"?"`)、型解析失败静默 `"?"` 无计数。
- **T5 的四个接线缺陷全部出自「旁路」的隐性副作用** (教训)。研读包挂上后: ① PDF 通道**饿死** (拿到的是过滤后只剩 CDISC 的 chunks) —— 按 spec §5「共存」裁定改为传过滤前 chunks; ② `answerer` 判断用了 **pre-helper 的 routed** (陈旧值), 使确定性 CDISC 事实通道在研读包路径上不工作, 而研读规则第 ① 步恰恰依赖它 —— 把 helper 整体上移到 `answerer` 之前; ③ 补取异常返 500 而非 502; ④ 补取丢 `domain`/`file_type` 且 k 口径与联邦不一致。**规律: 在管道中间插一个「替换输入」的旁路, 会同时打断所有下游读这份输入的消费者**; 下次插旁路先列清单「谁读这份数据、读的是哪个版本」。
- **e2e attempt 1 的修法停在 pattern 级** (对, 且是本单元最重要的纪律)。失败是 DS 的第三个 `DSCAT` 值被静默漏掉, 用 `DSSCAT` 子类别 / 阶段轴顶替。**example 级修法** = 在规则里写「DS 有三类」或写出那个 CT 取值 —— 能把 dm02 修绿, 但凡「分类轴不止一条」的域全部原样复发, 且下次换个域再翻车时没人知道为什么。**pattern 级修法** = 只说「沿域自身的 `--CAT` 轴逐类穷举, 不许用 `--SCAT`/epoch/时点轴顶替」, 不出现任何域名 / CT 取值 / 表单 / 项目 OID。
  配套的**分层防御** (单条规则不可靠, 四层互补):
  1. **规则文本层**: 类别轴写死 + 每类各起小标题 + 「在看任何 EDC 项目之前」的顺序约束; 原第 (5) 步「申报无候选类别」**并入** 第 (2) 步 —— 原来它挂在 (1) 的产物上, (1) 漏了它跟着哑, 合并后「漏」变成看得见的空标题。
  2. **判据层**: §0 判据跑前预登记并单独 commit, 判分由**未参与**写码/写答案/写判据的 agent 做 (规则 D), attempt 2 的判分 agent 还被隔离于 attempt 1 的结论之外。
  3. **反捏造层**: 零捏造由 `item_list_text` 逐 token 核 (958 项 + 21 表单, 两轮扫描 + 差集人工分流), 6/6 捏造 0。
  4. **闸层**: `test_rule_pins_category_axis_and_no_candidate_wording` 钉住**实际拼进 system 的那段文本**含 `--CAT` 与 `no candidate` —— 规则句是措辞不是结构, 下次重写最容易被静默抹掉。
- **判分方对判据的意见照单收录** (对)。判分 agent 判了 6/6 PASS 的同时指出三条判据缺陷 (② 无 precision / ① 对 AE 空转 / ③ 粒度未写死)。**PASS 与「判据可靠」是两件事**, 达标不等于量具好用; 三条全部进 §2 缺口, 不因为达标就吞掉。
- **流程失误五条** (全部记 ledger, 供下轮直接避开):
  1. **带 `name:` 的 agent 派发**结果不直接回到 controller (走 teammate 消息、延迟到达), 一度被误判为「不回报」而重复派发; 真因还叠加了 Bash 默认 120s 超时把首次全量 pytest 掐断。规则: implementer 派发写明 `timeout≥300000`; 两种派发通道都可用但要知道回报路径。
  2. **全量 `-q` 叠加吞掉 summary 行** (pyproject `addopts` 已含 `-q`), 实现者据此报了 9 个不存在的 failure (实为 `.pytest_cache` 陈旧 `lastfailed` 条目)。规则: 全量用 `-p no:cacheprovider -rfE`, 不再叠 `-q`。
  3. **implementer 在再审之后又 amend** (T1 `2b3d41d`→`e96fc6b`)。本次内容无害 (纯文档措辞 + 更严测试) 故接受并冻结该 agent, 但**审过的 hash 被改掉 = 审查结论与 HEAD 脱钩**。规则: 审查基线确定后 implementer 不得再动 HEAD。
  4. **前端先行于后端的那段窗口, 归因要说准** (T7)。T7 把 `dossier` 字段发进请求时生产还跑着旧
     后端, controller 的 `curl` 当场吃到 **422** —— 但那是打在 **`/api/ask`** 上的: 只有
     `AskRequest` 设了 `model_config = ConfigDict(extra="forbid")`, 未知字段必 422。**webchat 走的是
     `/api/ask_stream`**, `AskStreamRequest` 没有 `extra="forbid"` (pydantic 默认 ignore), 旧后端
     **静默忽略**该字段照常作答 ⇒ **窗口期 webchat 并没有坏**, 坏的说法是从一个不同端点的 422
     外推来的。重启仍然必要 —— 不重启功能压根不存在 (旧进程没有研读包这段码), 只是「必须重启」
     与「不重启就 500/422」是两回事。规则: 端点级的配置差异 (`extra="forbid"` 只在 `/api/ask`)
     会让同一个请求字段在两个端点上有完全不同的失败形态, 归因前先确认打的是哪个端点。
  5. **controller 的「ids only」红线指令过严** (T8)。它禁止在 committed 文件里引任何题面, 但映射集问句本身不含 OID / 表单名 / 日文 label, 且同类问句早已在 committed 测试与 spec 中; 该指令被当场撤回, 红线以 **OID 扫描器**为准。规则: 红线由**可执行的闸**定义, 不由口头指令加码 —— 加码会让归档失去可读性。
