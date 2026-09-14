# C2R N5 — 卡片层接地闸 + census 扩围 + prompt 规则 (2026-09-14)

> 状态: **工程 DONE + 复审两轮 (见 §3) + 闸回扫 attempt 1 FAIL (归档) → attempt 2 (见 §4) + 模型复测 B 臂 gpt-terra/gpt-sol (见 §6)**; 默认 OFF 不动 (C2R 通道); prompt 规则进 study 引擎全局
> PLAN §10 (登记于实现前; brainstorm 经用户批准, 范围「测量 + prompt 一起做」为用户选择) · 起源 `evidence/step_c2r_n4_audit.md` §7 (+ Erratum) · 归档 `evidence/failures/c2r_n5_gate_attempt_1.md`

## 0. PATTERN (不限「非表示アクティビティ」一种)
挂 study `[Source: …]` 出典 (EDC 項目カード / 手順書章節) 的句子所列 OID 不在被引文件里。画面层 N1–N3 把『画面目視判読』『頁索引』各钉了闸后, 错误挪到没有闸的 study 出典层。**勘误**: N4 审计「该 OID 在 16 源 0 次」不成立 —— 它在同 run 另一张卡片的非表示列表里 (run json `text_preview` 只存 300 字, 非表示行恒在其外, 用预览 grep 必 0); 形态 = **兄弟卡片移植 + 挂真出典**, 对应闸的 `CONTEXT_MISCITED` 类。三方独立确认 (Writer / reviewer / judge)。

## 1. 三层防御 (改了什么)
1. **零 LLM 闸** `scripts/study/c2r_eval/check_card_grounding.py <runs>... [--unmask]` (eval 侧, 不改服务; 与 N2 共用切分 helper `line_starts/line_of/scope_start`, 抽出后 N2 65 tests + 36 文件 197 单元逐条相同): 单元 = 以 study 出典结尾的句/条目 (前一出典之后起, 『頁索引』也作切分点, 出典行无中身时向上吞整块); 实体 = catalog activity/event/item/group OID (≥3 字, token 边界; **form OID 不当实体**: 文书名 + 活动族简称; **日语名不当实体**: 合法来源是対応表); 判定 `SOURCE_GROUNDED` / `SIBLING_NAMED` (被引文件没有、但其自身卡片在本 run 文脈里的项目 OID = 文书名, 不标红、**单列不混入绿**) / `CONTEXT_MISCITED` (在本 run 其它 study 源 / 题面 / 附页文本层 = 出典违い) / `UNGROUNDED` (文脈里都没有) / `BAD_SOURCE` (被引路径磁盘不存在) / `NEGATED` (被引文件没有的 OID, 且同小句在 OID 之后有「含まれません」类否定 = 闸的事实与句子一致, 不标红但脱敏列出供抽检) / `NO_ENTITY`。名字括注 (`OID(イベント › 活動)`) 内用「不得紧邻 CJK」的严格边界 (名字里粘着日文的 OID 形碎片不算, 括注内独立成词的活动 OID 算)。attempt 2 加: 文头为画面指称且自身无出典的句子不计入卡片实体集 (`screen_sentences` 计数)。payload 记 `context.n_questions / page_text_available` (缺题面文件时 3 单元会从 MISCITED 掉到 UNGROUNDED, 必须可追溯); PDF 缺失降级不炸。
2. **census 扩围** (judge 侧): 规则 A 范围 + 「归因 study 出典的 OID 级主张」(PLAN §10)。
3. **prompt 规则** `server/rag.py` `_STUDY_OID_RULES` 第 4 条 (只进 study 引擎; CDISC 侧 prompt 与 HEAD 逐字节相同, study 侧 = HEAD + 该块, 联邦 `both` 路径下该块仍恰 1 次): 挂出典的记述所列 OID 限于该文书本文实际写有的; 列举 (非表示アクティビティ等) 只照抄, 不补不推; 要提该文书没有的 OID 就挂它所在文书的出典或写明不在文脈。reviewer 核: 与前三条 (名字来源) 层面不同不冲突; 与 rule 7/8 同族不同粒度; 不与 `_FEDERATION_RULES` 冲突; 有逃生口, 过度拒答风险低。
- 测试: 卡片闸 40 条 + wiring 1 条 (规则三锚点 / CDISC 侧不出现 / study 侧恰 1 次); 全量 pytest 2332 → **2379 passed** (0 fail; 含 attempt 2、两轮复审修法与 judge 后正则修正后的最终重跑)。

## 2. 闸的演化 (为「对症下药」可审而写)
首跑 56 文件标红 61 → 六条 pattern 规则 → 9 (attempt 1) → attempt 2 一条规则 → 7。每条规则的**留一消融** (reviewer 第一轮, 36 文件 289 单元):
| 规则 (关掉) | flagged | 增量是什么 | 真阳性存活 |
|---|---|---|---|
| 基线 | 9 | — | ✅ |
| form OID 当实体 | 27 (+18) | 18/18 全是三个表单名 | ✅ |
| 兄弟项目 | 25 (+16) | 16/16 单个兄弟项目 OID 提名 | ✅ |
| 括注剥离 | 18 (+9) | 9/9 全是同一个活动名内粘着的 OID 形碎片 | ✅ |
| 题面+页文本 | 9 (0) | 3 条从 MISCITED 掉进 UNGROUNDED | ✅ |
| 『頁索引』切分 | 9 (0) | 零效果 (保留, 理由成立) | ✅ |
| NEGATED | 15 (+6) | 6/6 含否定的活动 OID | ✅ |
| path 取到空白 | 35 (+26) | 27 BAD_SOURCE = 节号被当 path | ✅ |
| ≤2 字 OID | 10 (+1) | 2 字项目 OID | ✅ |
每条被压掉的单元由**单一重复模式**主导, 真阳性在全部消融下存活 ⇒ reviewer 判「不是对症下药」。attempt 2 规则的消融见 §3 第二轮。

## 3. 复审 (规则 D, code-reviewer opus, 两轮)
- 第一轮 **条件 PASS**: MAJOR-1 三处仍写「16 源 0 次」+ 判据 ① 对已知真阳性无判别力 (类是 MISCITED) → 加带日期的 ①′; MAJOR-2 兄弟项目豁免与真命中同色 → `SIBLING_NAMED` + 盲点「跨卡片比较主张素通」; MAJOR-3 括注整块剥离 = 造假者的洞 (`<項目> (<活動> で非表示)` 形隐身) 且已吃掉一条真主张 (组 OID) → 括注内严格边界。MINOR-1..4 / NIT-1..4 全修 (否定同小句且在 OID 后, 列举读点不切; payload 记文脈完整性; PDF 降级; NEGATED 列出; `.` 只在后随空白时切句)。变异 11 杀 9 (2 存活为「零效果规则」的测试未钉性质, 已记)。
- 第二轮 **PASS** (三 MAJAOR 修法双向验证; 变异 12 杀 10, 2 存活为 reviewer 自认空变异后重做即杀) + 1 MAJOR 测试缺口: `_SCREEN_LEAD_RE` 的文头锚定是 **load-bearing** (消融: 放宽成「句中任意处提画面」→ screen_dropped 2 → 31 且**已知真阳性消失**) 却无测试钉住 → 补无出典混在文测试。洞 A (捏造前置「画面では、」对两闸隐身, N2 也接不住) 与倒装否定 (假阳性方向, 本集 0 例) 写进盲点; 洞 B (文头画面指称但句内归属カード的主张被剔) → 加 カード/手順書/対応表 归属词让步 (核: #8/#9 原句不含, 标红集不变); 逆接连词 ものの/けれど 入小句切分; `_strict_re` 加 lru_cache (整扫 64 s → 7 s, 行为不变)。
- **reviewer 硬性要求的三条数字**: (1) attempt 2 规则 `screen_dropped = 2` —— 它在整个验证集上只在要移除的那 2 个单元开火, **本验证集无法区分「通用规则」与「拟合规则」** (程序上干净: 实现前预登记 + 判据未改 + judge 只核 delta; 通用性是机制论证非样本证据, 同 N4 §9.2 的形状); (2) MINOR-1 修法 (否定同小句且在 OID 后) 在本集**零效果** (三种变体逐位相同), 被数据背书的只是其内部的「列举读点不切」让步 (每読点都切 → NEGATED 6→4, 标红 7→9 = 挡 2 条假阳性); (3) 假阳性 7 → 5 **正好顶格 ≤ 5 零余量**, 且这个 PASS 依赖用户「CITATION_ERROR 计入」的裁定 (剩 5 条里 3 条是 CITATION_ERROR)。

## 4. 闸回扫验证 (独立 judge, `evidence/step_c2r_n5_scan_audit.md`)
```bash
cd sdtm-rag && .venv/bin/python scripts/study/c2r_eval/check_card_grounding.py c2r_v3 c2r_n1 c2r_n3 c2r_n3_a2 c2r_n4 [--unmask]
```
- **attempt 1** (标红 9): 召回 **PASS** 1/1 (+ 预登记外新真阳性 1: 被引卡「30 个随访活动全非表示」被推广到另两个项目组, 真值 28/30 显示, 反证在同 run 上下文且被同答案上文引过); 假阳性字面 **7 > 5 FAIL** (CITATION_ERROR 3 = 主张真出典挂错 + 纯 FP 4)。NEGATED 6/6 真; SOURCE_GROUNDED 随机 10/10 真。**用户裁定: CITATION_ERROR 计入, 维持 FAIL, 走 attempt 2** (归档 `failures/c2r_n5_gate_attempt_1.md`)。
- **attempt 2** (只加画面句规则, 登记于实现前; judge delta 核验 `step_c2r_n5_scan_audit.md` §8): 标红 9 → **7**, 消失的恰是 attempt 1 判纯 FP 的 #8/#9, 新增 0, 其余 7 条红实体/行号逐字相同 ⇒ **判据 ② 字面 5 ≤ 5 PASS (压线, 零余量)**; 精确率 2/7。被剔画面句全集 = **2 句** (都由模型自己在下一行挂了画面页, 页文本层证实, 无卡片主张被误剔)。机制: 一条剔句后单元变 NO_ENTITY (剩余 OID ≤2 字) = **退出检查范围而非通过**; 被剔第 1 句内容同时也在卡片层 ⇒ 卡片主张以「画面では」开头且不自带出典即绕过 (已登记盲点, 洞 A)。
- **judge 后的机械修正** (不改判定): `_NEGATION_RE` 漏 「含まれていません」活用形 (复测 c2r_n5 唯一标红 = 此假阳性) → 补上 + 测试; 复扫验证集 7 条不变, c2r_n5 标红 1 → 0 (转 NEGATED)。
- **SIBLING_NAMED 16 条全核 (judge)**: 15 真 / **1 假 = 漏检** (v3 A 臂 opus-5 T6 L35: 5 个登録時系项目打包断言「非表示名单都含随访系全体」, 其中 2 项在 30 个随访活动里显示 15 个, 说反)。放行成因叠加: 一项在被引卡名单里 (纯关系盲点, 哪版闸都放行) + 一项落进 SIBLING 豁免 (**无豁免会标红且标得对**)。⇒ 豁免代价 = 16 分之 1 条真阳性; 它把精确率 2/25 抬到 2/9, 关掉则 3/25 精确率 + 3/3 召回。
- **召回两种口径 (都写)**: 判据 ① 口径 已知真阳性 1/1 PASS; **已测到的真实召回 2/3** (三条独立核实的真错误, 抓 2 漏 1)。核验覆盖 41/289。
- **闸的命中带偶然成分** (judge): 同一模型同一题 A/B 两臂各犯一次同型过度推广, 闸抓 B 漏 A, 差别只在被引卡名单里恰好有没有那个 OID。**不能读成「闸能识别过度推广」**。
- **闸的判别力边界** (交接必读): 只在「OID 不在被引文件」一维有效; 「OID 在被引卡里但关系说反」漏检率不可测 (SOURCE_GROUNDED 池随机 10/10 真, 但漏检成因 1 证明该池能藏错)。

## 5. 零回归
- 检索侧 golden v2 48 题 (零 LLM, `--retrieval-only --hybrid --study-lookup`): source recall 0.875 = 基线 0.875, 逐题 0 差异 (prompt 不碰检索, 预期)。
- 答题侧 golden v2 48 题 × gpt-terra (`bedrock/converse/global.openai.gpt-5.6-terra`, `--max-tokens 8000 --full-answers`; HEAD 臂 = `git stash push -- server/rag.py` 后跑, 再 pop 跑 N5 臂; 脚本 `golden_ab.sh` 见 checkpoint 同目录说明): substring fact recall **HEAD 77.1% → N5 80.9%** (+3.8 pt), source recall 两臂 87.5% 逐题相同 (检索不受 prompt 影响)。逐题 fact 差异 10 题: **7 升 3 降** —— 降的 3 题: q08 (源本就 0% 未检索到该卡, HEAD 凭记忆写出项目 OID 得分, N5 按新规则不写文脈外 OID = **规则按设计生效, 被 substring 尺子记为 miss**); q12/q13 各漏 1 个 codelist 取值串 (措辞差异)。**非 Δ0**, 按登记「逐题列差异并归档」。**噪声底** (N5 臂第二次重跑 `n5_golden_gpt-terra_n5_rep2.json`): fact avg N5-1 80.9% / N5-2 76.4% / HEAD 77.1%; N5-1 vs N5-2 逐题差 **9 题** (同 prompt 同模型), HEAD vs N5-2 只差 **1 题** ⇒ +3.8 pt 是噪声, prompt 效应 ≈ 0。两次 N5 都低于 HEAD 的只有 **q13** (1.0 → 0.67, 各漏同一个 codelist 取值串) = 唯一稳定位移; **judge 判为措辞方差非规则所致** (`step_c2r_n5_retest_audit.md` §9: 被漏串逐字在被引卡码表行里, 两次 N5 都保留全部 8 个取值代码并引用该卡, 丢的只是 HEAD 额外加的举例注释; 臂内方差 > 臂间差; 弱假设「规则把码表渲染推向光秃取值列表」需 HEAD 臂补 1–2 次重跑才能断死); 两次都高于 HEAD 的 0 题。q08 的「不写文脈外 OID」在 rep2 未复现 (0.33), 即模型对该规则的遵守本身也有方差。答案平均长度 526 → 547 字符 (+4%, 反驳「规则致冗长」)。

## 6. 模型复测 (B 臂 T1/T3/T6 × gpt-terra/gpt-sol → `runs/c2r_n5`)
```bash
nohup env SDTM_RAG_AUTH_ENABLED=false SDTM_RAG_PDF_CONTEXT_ENABLED=true .venv/bin/uvicorn server.main:app --port 8011 > /tmp/armB_8011.log 2>&1 &
until curl -s -m 2 localhost:8011/api/health >/dev/null; do sleep 1; done
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models gpt-terra,gpt-sol --qids T1,T3,T6 --timeout 900 --out c2r_n5
.venv/bin/python scripts/study/c2r_eval/tabulate_v3.py c2r_n5
.venv/bin/python scripts/study/c2r_eval/check_visual_grounding.py c2r_n5
.venv/bin/python scripts/study/c2r_eval/check_card_grounding.py c2r_n5
```
实跑: 6/6 status 200, 墙钟 19–31 s; **页集 / 截断 / 路由 / 16 源与 N4 逐字相同, 只有 prompt 变了 ⇒ 可归因**。闸字面: N5 闸 MISCITED 1 (gpt-sol T3 L9; 核验 = 否定正则漏活用形的假阳性, 修后 0) / UNGROUNDED 0 / BAD 0; N2 闸 LABEL 2 (sameness-vocab) + OFF_PAGE 1 (N4 为 LABEL 1 / OFF 1)。
**判分** (独立 judge, `evidence/step_c2r_n5_retest_audit.md`; 判分点冻结; census 规则 A 全量: 画面/頁索引 52 条全 verified 0 contradicted; **卡片出典 OID 级 31 条 (N5 扩围首做) 31/31 在被引文件、31/31 关系一致、0 UNGROUNDED、0 移植**; N4 §7 那条捏造全文消失, 且同位置主张本轮用了范围限定词「一部の…」与真值一致):
| qid (满分) | N4 terra | N5 terra | N4 sol | N5 sol |
|---|---|---|---|---|
| T1 (5) | 3 | 3 | 3 | **4** |
| T3 (4) | 4 | 4 | 4 | 4 |
| T6 (3) | 3 | 3 | 3 | 3 |
| 合计 (12) | 10 | **10** | 10 | **11** |
| 判据 (PLAN §10) | gpt-terra | gpt-sol |
|---|---|---|
| ① 卡片层 UNGROUNDED 核验后 0 | PASS (字面 0) | PASS (字面 0) |
| ①′ 兄弟卡片移植 MISCITED 核验后 0 | PASS (字面 0) | PASS (**字面 1** = 正则假阳性) |
| ② 逐点 ≥ N4 | PASS (10) | PASS (11) |
| ③ N4 判据①④不退 | PASS (跨页续接 0; 頁索引 3/3, 挂画面 0) | PASS (0; 8/8, 0) |
| ④ N2 闸不新增标红 | **字面 FAIL 2→3**, 核验后真错 0 | 同左 |
- ④ 三条标红逐条核: 否定极性 (四轮连续假阳性) / 同一性词「一致」(三轮连续) / **边界条 = 「同一画面」元数据五轮来第一次被读、用对、并标『頁索引』, 然后被闸标红** —— 闸在惩罚自己四轮求之不得的行为; 修法方向 (不在本轮): 单元含『頁索引』标记时同一性词规则豁免, 否则模型学会「不引元数据」就能变绿 = 反向激励。
- **prompt 副作用** (judge 专查): 过度拒答无 (「无法确定」0–2 条/份, 与 N4 同量级); 多出典冗长无; 対応表名字使用不减反增 (sol T1 裸活动 OID 4→0, 那一分就是这么来的)。**但一处明确的能力损失: T1 两模型 CDISC 标准层出典 2→0** (terra 连正文标准内容 3→0 整段消失, sol 保留内容但不挂出典) —— 规则只写 study 引擎却溢出压住了 CDISC 侧引用。登记为 N6 候选 (§8)。
- **两条口径敏感性 (由 PLAN 所有者裁)**: (1) T1 ⑤「三分来源标注」judge 按 V3 §2 逐字口径 (手順書章節充当「标准」维) 给 1; 若「标准」严格读成 CDISC 则 ⑤=0, terra 9 ⇒ **判据 ② 对 terra 翻 FAIL** (sol 10 仍 PASS); (2) 判据 ④ 原文是字面口径 ⇒ 字面 FAIL, ①/①′ 原文「核验后」⇒ 按核验判 —— 三条判据三种口径不混读, 本文两种都写。
- n=1 提醒 (judge): 靶心捏造 n=1, 消失也 n=1, 与「改法有效」和「运气好」都相容; 判分点 T1 ③ **五轮同 0** (补它所需元数据五轮在 label 里没人用, 本规则没碰到); 本轮两闸共标红 4 条、真捕获 0 = 两闸史上第一次同时零真捕获, 「答案变好」与「闸失灵」分不开。

## 7. 诚实边界 (汇总)
- 闸: 真实召回 2/3 (SIBLING 豁免漏 1); 精确率 2/7; 假阳性顶格 5/5 且依赖「CITATION_ERROR 计入」裁定; attempt 2 规则 screen_dropped=2 (通用性靠机制论证); 「关系说反」维零判别力; 洞 A/B/倒装否定已登记; 两闸标红 4 真捕获 0 的原因分不开。
- prompt: 效应在 golden 噪声底内 (§5); 靶心 n=1; CDISC 层出典 2→0 是明确代价。
- 生产: launchd 未 kickstart; opus-5 未测 (默认 ON 硬前置仍在)。

## 8. 下一单元候选 (未登记, 须 brainstorm)
- **N6 CDISC 层出典塌陷**: study 规则溢出压住 CDISC 引用 (T1 2→0)。方向: 规则措辞限定「本研究コーパスの出典」或在联邦 prompt 明写 CDISC 引用不受此限; 判据须含 CDISC 出典计数 ≥ N4。
- **N2 闸同一性规则豁免『頁索引』单元** (judge §④ 边界条): 不修 = 反向激励。
- **T1 ③ 五轮同 0**: 元数据在 label 里五轮没人用, 「在」≠「被用」的老问题, 需答题侧仪器而非再加 label。