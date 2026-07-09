# RETROSPECTIVE — SP4 (Neo4j 探索层)

> 2026-07-09 · KG 重启子项目 4/5 (可选单元，仅产品 UX 理由，非精度)。在 SP1 meta.yaml 之上建 brew+launchd 本机 Neo4j 探索层 (幂等导入脚本 + 独立对账门 + Cypher 查询库 + Browser)。生产答题通道 (内存 `DictBackend`) 零改动、零依赖、零扰动。
> 全流程: brainstorm (3 决策) → spec (批准 2026-07-08) → plan (9 task) → subagent-driven (每 task fresh implementer + 同 task 内 review-fix 循环) → Rule D 全量异 type (`feature-dev:code-reviewer`)。四门全过。

## 1. 保留下来的做法 (有效, 下次照做)

- **plan 期程序对源数据实测抓偏差, 而非停在 brainstorm 期的口头描述。** D1-D4 全部是写码前跑 `yaml.safe_load(meta.yaml)` 现场核数字抓出来的 (C66742 是 41 域不是 spec 写的 44；FOCID/C119013 的 closure≠location；`model_defhome` 目标是 model 文件不是域；59 个 defhome 变量里有 18 个不在任何 IG 域)。**为什么 plan 期是对的抓点、而不是 brainstorm 期**: brainstorm 阶段决策的是"要不要建 Neo4j、用什么部署方式、交付面多宽"这类**范围/架构问题**，此时 spec 里写的具体数字 (44 域、DEFHOME→Domain) 还只是从 `docs/DESIGN_RAG_KG.md` 的旧图 schema 誊抄／估算的占位描述，源数据本身 (`meta.yaml`) 那时甚至还没被为此目的重新扫过。真正到了 plan 阶段——要写 golden 数字、要定 Cypher 查询的确定性锚点——才第一次被迫对着**当前真实的 meta.yaml** 逐字段核对，偏差自然在这一步现形。**如果提早到 brainstorm 期去抠这四个数字，成本不对等**（brainstorm 决策的是要不要做、不是怎么建模，逐字段核对在那个粒度是过早优化）；**如果拖到 review 期才抓，就要走一轮 REQUEST_CHANGES 返工**。plan 期"写 golden 数字表"这个动作天然强制了实测，是**结构性**抓点，不是运气。值得固化为惯例：任何要建"golden 锚定数字"的验收门，其编写本身就是最佳的偏差探测时机。
- **纯函数 / 导入层分层, 让 Gate 3 (停机 477 passed) 自然成立而非靠额外 mock。** `build_neo4j.py` 把 `extract_graph(meta) -> rows` 做成零 I/O 纯函数 (golden-anchored TDD 单测直接对纯数据结构断言)，`import_graph(driver, rows)` 才做真正的 Neo4j 写入。测试套件只测 `extract_graph`（不需要活库），真正碰 driver 的代码路径完全在 `server/` 之外的 `scripts/` 里。这个分层不是为了 Gate 3 才后补的——是 Task 3/4 写码顺序本身的自然产物——但正因为分层干净，"Neo4j 停机时全套 pytest 绿" 这件事**不需要额外设计一个隔离测试策略**，隔离性是架构形状自带的副产品。**值得沉淀为惯例**: 任何要接一个外部有状态服务 (数据库/API) 的模块，先把"从源数据结构算出目标结构"这一步做成零 I/O 纯函数并独立测试，I/O 层薄到只做写入 + 自校验，这样"目标系统停机时代码库仍然可测"是设计的默认结果而非事后补丁。
- **两 lane 纪律 (reconcile 独立 yaml lane vs cookbook GraphEngine 等价 lane) 真正互补, 而非同一验证的重复。** Gate 1 (`reconcile_neo4j.py`) **禁止 import** `build_neo4j`/`MetaStore`/`GraphEngine`，只能用 `yaml.safe_load` + neo4j driver 读库；Gate 2 (`sp4_cookbook_golden.py`) 反过来锚定生产 `GraphEngine`（本身是 meta.yaml 之上的内存图引擎）。两条 lane 结构不同形（一个是遍历原始 yaml 重新聚合，一个是走生产内存图引擎的公开 API），对同一个难例 (D2 的 FOCID/C119013 逐域精确=1 而非 closure=3) 各自独立算出答案，**加上第三条路径**（`extract_graph` 本身，是被两条 lane 分别间接验证的对象）三方吻合，比单一 lane 的"结构镜像自我对账"强得多——reviewer 在 Gate 4 明确验证了 `expected_from_yaml` 的遍历确实是不同形状 (set/dict 推导 vs 导入器的 accumulate-in-dict)，不是表面上的"重写一遍相同逻辑"。
- **launchd + brew 运维一致性 (`com.sdtmrag.*` 命名族).** Neo4j 的 plist 沿用了 RAG API/UI 服务已经在用的 `com.sdtmrag.{api,ui}` 前缀，变成 `com.sdtmrag.neo4j`，端口/绑定策略 (localhost-only) 、runbook 结构 (安装→配置→验证→常见故障) 都对齐既有的 `deploy/README.md` 风格。这不是新发明，是**复用现成的运维心智模型**——同一台机器上未来若再加服务，操作员只需要认一种模式。

## 2. 必须补上的缺口 (下次改进)

- **Gate 2 golden harness 数字口径在 plan 文本和实际产物之间有一处笔误未清干净**：plan 的 commit message 草稿写"cookbook golden 7 条"，实际是 7 条 drift-check + 8 条 golden-value check = 15 条；task-6 的 report 也留了同款 off-by-one 记录（"承 brief off-by-one, gitignored 不影响交付"）。数字本身没错（15/15 harness 输出是对的），但**面向用户的一句话总结**如果照抄 plan 早期文案就会带错数字出去。这次收口专门核对了 `sp4_cookbook_golden.txt` 的实测行数才写文档；下次应当在 plan 文本定稿前就把"验收门里出现的具体计数"和"脚本实际产出"对一遍，而不是留到收口阶段才发现要修正。
- **两 lane 共享 meta.yaml 单一源头的局限没有在 plan 阶段被显式提前警示**——是本次收口 checkpoint 写「限制/诚实缺口」时才捋清楚讲透（reconcile 与 cookbook 两门都只能抓代码路径 bug，抓不出 meta.yaml 相对 PDF/xlsx 源文件本身的错误，那是 SP1 `reconcile_meta.py` 的职责）。这个边界在 spec/plan 里是隐含成立的（因为 SP1 已经做过独立锚对账），但没有一句话写在 SP4 自己的验收门描述里，容易让读者误以为 SP4 的两道验收门是"双重独立证明数据正确"。下次给建在既有可信数据层之上的新验收门写文档时，应当显式声明"本门验证的是什么层级的正确性，不验证什么"。
- **Term 节点 (controlled terminology 具体值) 未物化是 spec 明文 backlog，但落到实现层几乎没有代码层面的"占位钩子"**——如果 SP5 或未来某个单元真的要把 Term 节点加进图，需要重新过一遍 Gate 1-3 全部四门（新节点标签、新边、reconcile 的 41 项断言要扩），而不是增量扩展。这不算本单元的失职（spec 明确排除了 Term），但值得记一笔：如果未来确定要做，宜及早重新走完整设计循环，而不是指望现有骨架"轻松加个标签"。

## 3. 关键决策复盘

- **D1-D4 全部走"数据接地即改，不回头改 spec"的路线** (用户批准的 plan 惯例，AGG 单元同款)。四处偏差都是"spec 文字描述与实测数据不符"，不是"设计决策错了"——按 spec §5 gate 1 的原则（golden 数字从独立程序实测导出）处理，plan 文档头部专列"Spec 偏差"表 + Rule D 把它列为审查项。复盘：这条路线对，因为偏差的根源是 spec 写作时的估算/誊抄误差，不是架构判断分歧；如果是后者就该回头改 spec 而不是在 plan 里"修正"。
- **两 lane 分工 (reconcile 独立 yaml vs cookbook GraphEngine 等价) 而非合并成一道门。** 若图省事把两者合并（例如都走 GraphEngine），会失去"结构不同形的独立验证"这个反过拟合价值；若两者都走独立 yaml 重导，则无法验证生产 `GraphEngine` 本身与图数据库的等价性（Gate 2 存在的意义）。分开两道门、各自禁止互相 import，是本单元验收设计里最值得保留的一条。
- **Task 7 (Gate 3) 首派遭 API 登出中断，选择"复用未提交的探针脚本 + 干净重跑"而非"从零重写"。** 中断发生时探针脚本 (`sp4_isolation_probe.py`) 已经写完、内容与 brief 逐字比对完全一致（只是没提交），pytest 一行输出被截断。重派任务时的判断是：脚本本身没有质量问题，问题出在**运行/捕获层**（诊断出根因是命令行 `-q` 叠加 `pyproject.toml` 的 `addopts = "-ra -q"` 导致 pytest verbosity 到 -2，pytest 9.x 在此级别静默省略"N passed"汇总行），于是保留探针不变，只修正跑法（去掉多余 `-q`、直接捕获 `$?`、写日志文件而非走管道截断）重新跑一遍三条 clause。**这个决策复盘的价值在于**：中断后的第一反应不是"重写"而是"先诊断中断留下的产物是否可信、根因是环境还是代码"——诊断成本远低于重写成本，且诊断本身产出了一条值得记录的 pytest 行为知识（避免未来任何 ad-hoc 门脚本再犯同样的双重 `-q` 静默 bug）。这与本单元多处"程序门抓不到、独立门抓到"的模式一致：**先问"这是真缺陷还是流程/环境噪音"，再决定要不要动代码**。
- **默认不新增答题能力，只做探索层** (brainstorm 决策①的产品定位)。KG 价值 eval (2026-06-21) 早已定论"SP4/SP5 不靠答案质量证明"，本单元严格守住这条线——`server/` 零改动是可验证的硬约束（Gate 3 静态 grep + 运行时 `sys.modules` 双重校验），而不是"承诺不改就不改"的口头约束。这条纪律保证了即便 SP4 探索层本身有 bug，也不可能污染生产答题通道，是本单元风险最小化设计的核心。

## 4. 验收 (四门, PASS)

- **Gate 1** reconcile 41/41 `[OK]` + 幂等 (两建 snapshot 5254 行逐字节同) + N=9 分层邻域 + 2 确定性锚点。`evidence/checkpoints/sp4_reconcile_gate.txt`。
- **Gate 2** cookbook golden 15/15 (7 drift + 8 golden)，锚定生产 GraphEngine 等价 lane。`evidence/checkpoints/sp4_cookbook_golden.txt`。
- **Gate 3** Neo4j 停机全套 477 passed + composite off/on byte-identical (6225B) + `server/` 零 neo4j 引用。`evidence/checkpoints/sp4_isolation_gate.txt`。
- **Gate 4** Rule D 异 type (`feature-dev:code-reviewer`) APPROVE_WITH_NITS，0 BLOCKER/HIGH，1 MED + 2 LOW 均修补验证。`evidence/checkpoints/sp4_ruleD_review.md` + `sp4_localhost_binding.txt`。

## 5. 产出

见 `evidence/checkpoints/sp4_neo4j_summary.md` 「产物清单」段（脚本/plist/cookbook/runbook/证据全列）。

## 6. next

- **SP5 (图增强校验器)** 是唯一剩余可选单元 (impact / 跨域完整性 / CT 级联一致性接进 Validator, DESIGN §5.6) — **新设计单元，必须先 `superpowers:brainstorming`**（无现成 spec/plan，不可跳过设计直接实现）。
- 若用户不要图校验器，KG 主线 (SP1-3 能力交付 + AGG 独立通道) 与探索层 (SP4) 均已收口。
