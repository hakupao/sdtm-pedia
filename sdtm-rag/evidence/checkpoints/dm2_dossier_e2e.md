# DM2 — L3 e2e (2026-09-15)

## §0 判据 (跑前登记)

> 本文件在**任何一次跑之前**提交 (commit `docs(rag): DM2 T9 e2e 判据预登记 (跑前)`).
> 判分由**异 subagent** (opus, 不看本 session) 做, 结果写 §2; §1/§2 跑前为空.

题: 3 题 × 模型: 2 个 = **N=6**.

| id | 域 | 语言 / 域的给出方式 | 问题原文 |
|----|----|--------------------|----------|
| dm01 | DS | zh, 小写码 `ds` (用户原句, 逐字保留) | 本研究中，哪些数据适合进入 sdtm 的 ds domain？ |
| dm02 | DS | ja, 大写码 `DS` | この試験で収集しているデータのうち、SDTM の DS ドメインに入れるべきものはどれですか？ |
| dm05 | AE | en, 小写码 `ae` | In our study, which collected data items belong in the ae domain? |

模型: `opus-5`, `sonnet-5` (两者均走 `/api/ask_stream`, `dossier:"auto"`, `history:[]`).

**每题 PASS = 三条全过**:

① **定义齐**: 按域定义列出全部记录类别 (DS: 3 类, 即 `DISPOSITION EVENT` / `PROTOCOL MILESTONE` / `OTHER EVENT`; AE: 见 `knowledge_base/domains/AE/assumptions.md` item_1).

② **候选齐**: gold 4 卡 ≥ 3 张被点名 (表单 OID + 项目 OID 原样); 额外点名的 OID 全部在一览中存在 (零捏造, 用 `check_code_grounding` 码闸 + 一览 grep).

③ **标推测**: 每条归属带 推測/inference 标记; 明说无候选的类别.

**目标 ≥ 5/6 PASS**.

判分 = 异 subagent (opus, 不看本 session), 每题独立报告写 §2.

**成本**: 每题记 `usage.prompt_tokens` / `usage.completion_tokens` / 是否 cache 命中 (Bedrock 返回 `cache_read_input_tokens` 时).

**失败处置**: 若 < 5/6, 归档 `evidence/failures/dm2_task9_attempt_1.md`; 只允许改 `_DOSSIER_RULES` 的**规则层**措辞 (模式级), 不许加题面 example; 改后重跑 6 题**全部** (不只失败题).

gold 卡 basename 与一览文本仅在 gitignored runs/ 目录, 判分 agent 读那里。

## §0′ attempt 3 判据 (Claude 重跑 + 留出题; 跑前登记, 2026-09-25)

> 本节在 attempt 3 **任何一次跑之前**单独 commit。起因: 2026-09-25 实测 Bedrock 恢复 Anthropic 访问
> (复跑: `.venv/bin/python <probe>` 对 `bedrock/converse/global.anthropic.claude-{opus,sonnet}-5`
> 各发 `max_tokens=5` 的 `ping`, 两者返回 `OK`; 旧 runbook 的 `grep -c "not allowed"` 只数历史日志, 不能作判据)。
> **`_DOSSIER_RULES` 本轮一字不改** (commit `03096ad` 原样) —— 同时改规则与模型就不再是模型维度的对比。

**题 × 模型 = 6 × 2 = N=12**, 产物 `runs/dm2_e2e_claude/` (attempt 2 答案目录不覆盖):

| 组 | id | 域 | 类别轴形态 | 用途 |
|----|----|----|-----------|------|
| in-sample | dm01 / dm02 / dm05 | DS / DS / AE | DS `--CAT` 有 CT; AE 无 `--CAT` CT | 与 attempt 2 (deepseek) 同题可比 |
| **留出** | dm03 | DS (en) | `--CAT` 有 CT | 规则句在未见过的问法上是否仍逐类穷举 |
| **留出** | dm04 | DM | **无 `--CAT` 变量** | 无类别轴的域, ① 的空情形 |
| **留出** | dm07 | PR | `--CAT` 存在但**无 CT** | 显式改轴 + 「候補なし」分支可能被触发 |

跑命令: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --qids dm01,dm02,dm05,dm03,dm04,dm07 --out-subdir dm2_e2e_claude --require-no-fallback`

**G0 前置闸 (判分之前, 机器判)**: 12 run 全部 `attached=True` 且 `fell_back is False` (三态, `None` 也不过)。
不过 ⇒ 不判分, 事实原样留档 —— 回退的 run 不构成 Claude 结论。

**每 run PASS = ①′②′③′ 全过** (在 §0 基础上收紧三处缺口, 措辞写死):

①′ **定义齐** —— 按域形态三选一:
  - (a) `--CAT` 有 CT: 该 CT 每个取值各有一个小标题, 缺一即 FAIL; 用 `--SCAT` / epoch / 时点 / codelist 名顶替某个取值 = 该取值缺失。
  - (b) `--CAT` 存在但无 CT, 或 (c) 域无 `--CAT` 变量: 答案须**明说**「该域无受控 `--CAT` 取值」(或「无 `--CAT` 变量」) **且**点名它改用的分组轴; 未声明就自造类别 = FAIL。改哪条轴不设对错, 但须按域定义 (assumptions 首段) 讲得通, 判分方写一句理由。
  - 三种形态下, 每个分组要么列候选, 要么明写「候補なし / no candidate」; 静默跳过 = FAIL。

②′ **候选齐 + 零捏造 + 精度**:
  - recall: gold 卡 ≥ 3/4 被点名 (表单 OID + 项目 OID 原样) —— 同 §0。
  - 捏造: 点名的 EDC OID 全部在 `item_list_text` 中存在, 表单归属无错挂 —— 同 §0, 捏造 >0 即 FAIL。
  - **precision (新增)**: 判分方对答案作为**该域候选**点名的项目逐条 (整表倒出时按表逐项) 判「明显错归」= 该项目内容由另一 SDTM 域的 topic 变量承载, 且目标域 (含 `SUPP--`) 无任何变量可合理承载。明显错归 / 点名候选总数 **≤ 10%**, 超出 = FAIL。明确标为「不入本域 / 排除 / 参照」的项目不计入分母。
  - 判分方另报: 点名候选总数、明显错归数与 ≤5 条示例 (代称), 以及区间简写计数错误数 (**只报不判**)。

③′ **标推测, 粒度写死为「分组级」**: 每个列候选的分组 (小标题 / 表格) 须在其标题或首行带 推測 / inference 标记; 只有开篇一句全局免责 = FAIL; 逐条内联标记为更强但**不是**必要条件 (与 attempt 2 判过的口径一致, 避免换尺子)。

**目标 (预登记)**: 每个模型分开计 —— in-sample 3 题 ≥ 3/3 与留出 3 题 ≥ 2/3; 两模型分列, 不合并成一个比分。

**同尺子复判 attempt 2**: 判分方同时用 ①′②′③′ 复判 attempt 2 的 6 份 deepseek 答案 (`judge_pack_attempt_2.json`),
只作比较基线, 不改 §2.2 的历史判定。

**判分**: 异 subagent (规则 D, 不同 `subagent_type`), 只读本节 + §0 + 两份 judge pack, **不读** `judge_verdicts_attempt_{1,2}.md`。
逐 run 报告 (含真实 OID) 写 gitignored `runs/dm2_e2e_claude/judge_verdicts.md`; 摘要写 §2.3。

**失败处置**: 未达目标 ⇒ 归档 `evidence/failures/dm2_task9_attempt_3.md`; 规则句修改另起 attempt 4, 不与本轮合并。

## §0″ attempt 4 判据 (规则句 pattern 级修订后; 跑前登记, 2026-09-25)

> 本节在 attempt 4 **任何一次跑之前**、且在规则句修订 commit **之前**单独 commit。
> 起因: attempt 3 业务 FAIL (§2.3) + 判分方列出的判据歧义 —— 本节把它们**写死**, 不再留自由裁量。
> 生产 auto 挂载已暂停 (`dossier_auto_attach=False`, commit `5bd233a`), 本轮跑批显式 `dossier:"on"`; 触发器正确性另由 L2 闸 (`dm2_trigger_sweep.py`) 管, 不在本节。

**题 × 模型**: 与 §0′ 同 6 题 × `opus-5`/`sonnet-5` = N=12, 产物 `runs/dm2_e2e_attempt4/`。
跑命令: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --qids dm01,dm02,dm05,dm03,dm04,dm07 --out-subdir dm2_e2e_attempt4 --require-no-fallback --dossier on`
⚠ 留出 3 题在 attempt 3 已被看过 (失败模式来自它们) ⇒ attempt 4 **全部 6 题都是 in-sample 修复验证**, 不再有泛化维度;
泛化须另建新题 (本轮不做, 结论写清)。

**G0 前置闸**: 12/12 `attached=True` (reason `forced_on`) 且 `fell_back is False`; judge pack 附 `attached`/`fell_back`/`models_used` 字段, 判分方可自核。

**每 run PASS = ①″–⑥″ 全过**:

①″ **分类轴** (同 §0′ 三形态, 两处写死):
  - (a) `--CAT` 有 CT: 每个 CT 取值须以 **CT 原文大写字符串**逐字出现在其分组标题中; 意译、缩写、codelist 名 (如 `OTHEVENT`) 均**不算**写出该取值 ⇒ 该取值缺失 ⇒ FAIL。
  - (b)(c) 同 §0′: 明说「无受控 `--CAT` 取值」/「无 `--CAT` 变量」**且**点名替代分组轴, 缺一 FAIL。
  - 每个分组要么列候选要么明写「候補なし / no candidate」, 静默跳过 = FAIL。
②″ **recall**: gold 卡 ≥ 3/4, 以**项目 OID 原样**出现为准; 表单 OID 写错 (非一览中的表单 OID) 不影响 recall 计分, 但归入 ③″ 捏造。表单 OID 出现在分组标题或同行均可。
③″ **零捏造, 作用域 = 全文**: 答案**任何位置** (候选 / 排除 / 参照 / 表格任一列) 出现的 EDC 项目 OID 与表单 OID 须在 `item_list_text` 中存在, 且项目挂在答案所称的表单下; 捏造 ≥1 = FAIL。
  族名前缀简写: 前缀在一览中确有成员则不计; 区间简写端点越界计捏造 (区间计数少报只报不判)。
④″ **precision** (重定义): 分母 = 作为本域候选点名的项目 (整表倒出按表逐项, 明确标「不入本域」的不计); 错归 = 下列任一:
  (i) 该项目内容无法由目标域任何变量 (含 `SUPP--` QNAM) 合理承载; (ii) **同一项目在答案中既被列为候选又被列为不入本域** (自相矛盾, 按项目计 1)。错归 / 分母 ≤ 10%, 超出 = FAIL。
⑤″ **SDTM 侧不捏造**: 答案点名为目标域变量的 SDTM 变量名须在 `knowledge_base/domains/<域>/spec.md` 中存在, 或显式标为 `SUPPQUAL`/QNAM 提案; 点名不存在的标准变量 ≥1 = FAIL。
⑥″ **标推測, 粒度 = 分组级**: 每个列候选的分组, 其**自身标题、首行或直接上级标题**带 推測 / inference 标记; 只在组尾总结句或开篇全局免责 = FAIL。
⑦″ **语言一致** (新增): 答案主体语言与问句语言一致 (zh→zh, ja→ja, en→en; OID / SDTM 名 / CT 值 / 原文引用除外); 不一致 = FAIL。

**跑前补注 (审查意见, 仍在任何一次跑之前)**: ⑦″ 的除外清单另含规则句规定的固定标记 (「候補なし / no candidate…」、(推測)), 它们不计入语言判定; judge pack 中 G0 字段名为 `dossier_attached` / `fell_back` / `models_used`。
规则句在 `f8523ad` 之后按审查意见再改一轮 (判分口吻改行为句 / CT 来源挪入 (a) / 推測粒度与 ⑥″ 对齐 / 去掉 DS 色彩的旧措辞), 本轮以最终 commit 为准。

**目标 (预登记)**: 每个模型 **6/6** (全部 in-sample 修复验证, 标准从 §0′ 的 3/3 + ≥2/3 收紧), 两模型分列。
**同尺子复判**: 判分方同时用 ①″–⑦″ 复判 attempt 3 的 12 份 Claude 答案 (`runs/dm2_e2e_claude/judge_pack.json`), 作为修订前基线; 不改 §2.3 历史判定。
**判分**: 异 subagent (规则 D; 与 attempt 3 判分方不同 `subagent_type`), 只读本节 + §0/§0′ + 两份 judge pack, 不读任何 `judge_verdicts*.md` 与 §1-§4。
**失败处置**: 未达 6/6 ⇒ 归档 `evidence/failures/dm2_task9_attempt_4.md`; 研读包 auto 继续暂停; 下一步由用户裁定。


---

## §0‴ attempt 5 判据 (新留出题泛化 + 语言结构性修法; 跑前登记, 2026-09-25)

> 本节在 attempt 5 **任何一次跑之前**单独 commit。代码基线 = 规则句 `7b9bdd0` + 语言行 `2868ba5` (研读包挂上时在最后一条 user 消息末尾按问句文字种类追加确定语言行)。
> 用户裁定 (2026-09-25): 下一步 = 新题泛化 + 语言修。

**题 × 模型 = 6 × 2 = N=12**, `dossier:"on"`, 产物 `runs/dm2_e2e_attempt5/`:

| 组 | id | 域 | 语言 | 类别轴形态 | 用途 |
|----|----|----|------|-----------|------|
| **新留出** | dm09 | IE | en (小写码) | `--CAT` 有 CT | 泛化 |
| **新留出** | dm10 | MH | zh | `--CAT` 无 CT | 泛化 (独立性最弱: gold 与 v1 NOTES 的排除清单重合; 规则句修订方未读过该 NOTES) |
| **新留出** | dm11 | EX | ja | `--CAT` 无 CT | 泛化 |
| **新留出** | dm12 | PC | en | `--CAT` 无 CT; **本研究预期无数据** | 「候補なし」分支 |
| 回归 | dm05 / dm07 | AE / PR | en / ja | — | attempt 4 sonnet 两个失败题 |

留出题由**盲于实现**的异 agent 出 (未开 server/ / eval/*.py / evidence/ / runs/), 存 gitignored `data/study/st01/eval/test_set_domain_mapping_v2_holdout{.yml,_NOTES.md}`;
controller 独立复核: 4 题 facts 均为 assumptions 原文子串、卡片均存在。
跑命令: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --yml test_set_domain_mapping_v1.yml,test_set_domain_mapping_v2_holdout.yml --qids dm09,dm10,dm11,dm12,dm05,dm07 --out-subdir dm2_e2e_attempt5 --require-no-fallback --dossier on`

**G0**: 同 §0″ (12/12 attached + `fell_back=False`, judge pack 字段自核)。

**每 run PASS = §0″ ①″–⑦″ 全过, 附以下写死 (本轮起生效)**:
- ①‴ 形态判定须与 `knowledge_base/domains/<域>/spec.md` 一致 (把 (b) 说成 (c) 或声称不存在实际存在的 `--CAT` = FAIL)。
- ②‴ recall: gold 卡为 0 张的题 (dm12) recall 不适用; 该题 PASS 须**明写**本研究无该域候选 (「候補なし / no candidate」或等义句), 且**不得**把任何 EDC 项目列为该域候选 (列 ≥1 即 ④ FAIL)。
- ②‴ dm09 附加: 须说明该域只记录**未满足**的入选/除外规准 (IE assumptions item 2 要点); 把全部规准 Y/N 当作逐条记录源而不说明此点 = FAIL。
- ②‴ dm11: 「先入 EC 再导出 EX」与「直接入 EX」均接受。
- ④‴(ii) **用户裁定写死**: 条目内「本体属他域 / 仅作派生源」注记、同句条件式二选一、排除条目内提 SUPP 方案、未点名 OID 的表单级短语 —— 四者**均不算**自相矛盾; 只有同一项目 OID 被无条件地既列为候选又列为不入本域才算。
- ④‴(i) 有标准域的 topic/timing 变量可承载时, SUPP-- 不算「合理承载」(attempt 4 判分方解释, 本轮起写死); 阈值改为 **错归数 ≤ max(1, 10% × 分母)** (小分母过敏修正)。
- ⑤‴ 真值源 = 该域 `spec.md` ∪ 该域 `assumptions.md` 原文点名的变量。
- ⑦″ 不变 (固定标记、OID、SDTM 名、CT 值除外)。

**目标 (预登记)**: 每个模型 **6/6** (新留出 4/4 + 回归 2/2), 两模型分列; 另报 attempt 4 那 12 份在 ①‴/④‴ 变更下是否翻转 (只报不改判)。
**判分**: 异 subagent (规则 D, 与 attempt 3 `critic` / attempt 4 `verifier` 均不同 type), 只读 §0/§0′/§0″/§0‴ + judge pack + 留出题 NOTES, 不读任何 `judge_verdicts*.md` 与 §1-§4。
**失败处置**: 未达目标 ⇒ 归档 `evidence/failures/dm2_task9_attempt_5.md`; auto 继续暂停; 下一步由用户裁定。达标 ⇒ 由用户裁定是否恢复 auto (及是否按模型区分)。

---

## §0⁗ attempt 6 判据 (Opus 单模型补跑; 跑前登记, 2026-09-25)

> 本节在 attempt 6 **任何一次跑之前**、且在规则句修订 commit **之前**单独 commit。
> 用户裁定 (2026-09-25): opus 补一轮 —— 规则 (3) 补「举例也只用一览真实 OID」+ 判据余项写死, **只跑 opus**; 达标则**只对 opus 恢复 auto**, sonnet 维持手动。

**题 × 模型 = 6 × 1 = N=6** (`opus-5` 单模型), 同 §0‴ 题集 (dm09-dm12 + dm05/dm07), `dossier:"on"`, 产物 `runs/dm2_e2e_attempt6/`。
⚠ 6 题均已在 attempt 5 见过 ⇒ 本轮是 **in-sample 修复验证 + 采样重复**, 不是新的泛化证据; 泛化证据仍以 §2.5 (opus 新留出 3/4, 宽 4/4) 为准。
跑命令: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --yml test_set_domain_mapping_v1.yml,test_set_domain_mapping_v2_holdout.yml --qids dm09,dm10,dm11,dm12,dm05,dm07 --models opus-5 --out-subdir dm2_e2e_attempt6 --require-no-fallback --dossier on`

**判据 = §0″ + §0‴ 全部条款, 另写死 attempt 5 判分方提出的余项 (本轮起生效)**:
- ③⁗ **示例值入核**: 答案中凡被称为或以形态呈现为 EDC 项目 / 表单 OID 的 token (含「例:」「e.g.」举例、占位说明) 一律入核; 不存在即捏造。
- ④⁗ **候选三态**: 以「弱候选 / 可能 / 更可能属于他域 / 参考」等保留语气列在候选段内的项目, **计入分母** (视为候选); 只有明确标为「不入本域 / 排除」的才不计。
- ④⁗ **同标准域竞争**: 目标域 topic 变量技术上可写、但 SDTM 另有专门承载该内容的标准域时, 计错归 (i)。
- ②⁗ **族简写对称**: recall 计数接受区间 / 族简写, 条件是展开后覆盖 gold 项目 OID 且 ③ 核验其成员均存在; 占位符 (`_n` 等未给端点的形式) 不计 recall。
- ①⁗ 形态判定真值源 = spec.md ∪ assumptions.md (与 ⑤‴ 统一)。
- 阈值不变: 错归 ≤ max(1, 10% × 分母)。

**跑前补注 (审查意见, 仍在任何一次跑之前)**: 判分方另报「gold 项目被列为排除」的个数 (只报不判) —— 规则句新增「他域专属则列排除」可能以 recall 为代价, 须单独可见。
规则句 `abbecb7` 之后按审查再改一轮 (缺席≠不存在前移到选形态之前 / 他域排除加对称条件 / 占位符入禁); 本轮以最终 commit 为准。

**目标 (预登记)**: opus **6/6**。达标 ⇒ 实施「仅 opus 恢复 auto」(另起 commit + 异 agent 审 + kickstart + 生产探针); 未达 ⇒ 归档 `evidence/failures/dm2_task9_attempt_6.md`, auto 维持暂停, 交用户裁定。
**同尺子复判**: 判分方同时用本节口径复判 attempt 5 的 6 份 opus 答案 (`runs/dm2_e2e_attempt5/judge_pack.json` 中 model=opus-5 者), 只报不改 §2.5。
**判分**: 异 subagent (规则 D; 与 attempt 3/4/5 判分方 critic / verifier / scientist 均不同 type), 只读 §0-§0⁗ + judge pack + 出题 NOTES, 不读 `judge_verdicts*.md` 与 §1-§4。

---

## §0⁵ attempt 7 判据 (生成后确定性闸上线后 Opus 实跑; 跑前登记, 2026-09-25)

> 本节在 attempt 7 **任何一次跑之前**、检测器定稿 (`9148969`) 之后单独 commit; 此后检测器 / 规则句 / 判据一字不改直到判分完成。
> 用户裁定 (2026-09-25): 做生成后确定性检查。spec `docs/superpowers/specs/2026-09-25-dossier-output-gate-design.md` (含 §7 已知限制)。
> 实现 13 commit `86e5f94..9148969` + judge pack 加 `first_answer`; 三轮异 agent 审 (silent-failure-hunter → architect ×2), 离线回放 42/42 (按 OID 哈希比身份), 2585 passed。

**题 × 模型 = 6 × 1 = N=6** (`opus-5`), 同 §0‴/§0⁗ 题集, `dossier:"on"`, 产物 `runs/dm2_e2e_attempt7/`。⚠ 6 题均已见过 ⇒ 修复验证, 非泛化证据。
跑命令: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --yml test_set_domain_mapping_v1.yml,test_set_domain_mapping_v2_holdout.yml --qids dm09,dm10,dm11,dm12,dm05,dm07 --models opus-5 --out-subdir dm2_e2e_attempt7 --require-no-fallback --dossier on`

**G0**: 同前 + **`GATE grounding` PASS** (6/6 挂研读包且 `grounding` 非 null) + `/api/info.dossier_gate == true` (跑前实测)。

**主判 (业务)**: 按 §0″+§0‴+§0⁗ 全部条款判**最终轮答案** (`answer`)。**目标 6/6**。

**闸自身的判定 (只报不判, 但必须报)**:
- 触发率: 6 run 中 `regenerated=true` 的个数; 最终 `grounding.final.ok=false` 的个数。
- 对每个触发了重答的 run, 判分方按 ③⁗/⑦ 独立判**首轮** (`first_answer`): 闸拦得对 (首轮确有 ③ 或 ⑦ 违规) / 闸误拦 (首轮 ③⑦ 均无违规)。
- 对未触发重答的 run: 最终轮若被判分方判 ③ 或 ⑦ FAIL ⇒ 记「闸漏报」, 并说明属于 spec §7 哪一类已知限制或是新形态。
- 已登记的已知误报 / 漏报形态 (spec §7): 槽后新词干纯字母捏造漏报; M3/M5/M6/M10; 繁体→ja; 表格为主正文不判语言; 两段方括号兜底等。
- 语言: `lang_observed=None` 的个数与 `zh→ja` 误判个数单列。

**成本 (预登记预期)**: 每个重答 = 再一次 ~150K prompt; 预期残差 ≈ 低频模式概率平方, **不是**消除; 闸看不见的 ④①⑤ 失败不受影响。
**达标 (6/6) ⇒** 实施「仅 opus 恢复 auto」(另起 commit + 审 + kickstart + 生产探针), 并同步 webchat title。**未达 ⇒** 归档 `evidence/failures/dm2_task9_attempt_7.md`, 交用户裁定。
**判分**: 异 subagent, 与既有判分方 (critic / verifier / scientist / tracer) 及本单元实现 / 审查方 (executor / silent-failure-hunter / architect) 均不同 type; 只读 §0-§0⁵ + judge pack + 出题 NOTES + spec §7。

---

## §0⁶ attempt 8 判据 (研读包 prompt cache 布局上线后 Opus 实跑; 跑前登记, 2026-09-25)

> 本节在 attempt 8 **任何一次跑之前**、实现定稿 (`24ecca8` `5a3f9e7` + 前缀稳定回归测试) 之后单独 commit。spec `docs/superpowers/specs/2026-09-25-dossier-prompt-cache-design.md`。
> 审查 (oh-my-claudecode:debugger): 无 BLOCKING; 前缀实测仅 1 种 (跨问题 / 语言 / history / 端点); deepseek 回退 wire 上 system 为字符串; gpt 无 cachePoint; kill switch 布局与 `3e5fb1c` 逐字节一致 (旧代码 git archive 重放验证)。

**题 × 模型 = 6 × 1 (`opus-5`)**, 同 §0⁵ 题集与顺序 (dm09, dm10, dm11, dm12, dm05, dm07), `dossier:"on"`, 产物 `runs/dm2_e2e_attempt8/`。唯一变量 = 研读包位置 (user 消息 → system 末尾带断点) + 规则指代句。
跑命令: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --yml test_set_domain_mapping_v1.yml,test_set_domain_mapping_v2_holdout.yml --qids dm09,dm10,dm11,dm12,dm05,dm07 --models opus-5 --out-subdir dm2_e2e_attempt8 --require-no-fallback --dossier on`

**G0**: 同 §0⁵ (attached / 不回退 / grounding 非 null) + 跑前实测 `/api/info.dossier_prompt_cache == true`。
**主判 (业务, 质量不得降)**: §0″+§0‴+§0⁗+§0⁵ + §0 常设裁定, 判最终轮答案, **目标 6/6** (= attempt 7)。未达 ⇒ `dossier_prompt_cache=False` 回滚旧布局 + 归档 `evidence/failures/dm2_task11_attempt_1.md`。
**缓存判定 (机器, 只报不改业务判定, 但必须报)**:
- 第 1 题 `cache_creation_input_tokens` ≈ 研读包 + system 规模 (>100K)。
- 第 2-6 题: `cache_read_input_tokens > 100K`; **豁免**: 上一题 `wall_seconds > 280` (5m TTL 从请求开始计时, 可能已过期) 或本题 `fell_back=True` (deepseek 自身缓存会被读成 cache_read, 不算 Anthropic 命中)。非豁免的未命中 ≥1 ⇒ 缓存判定 FAIL (排查前缀), 不影响业务判定。
- 成本口径: litellm `prompt_tokens` **已含** cache 读写; 相对成本按 `未命中部分×1 + 写入×1.25 + 读取×0.1` 计, 与 attempt 7 全价 `prompt_tokens` 比。
**判分**: 异 subagent (未用过的 type), 只读 §0-§0⁶ + judge pack + NOTES + spec §7 (闸) / 本 spec; 不读 `judge_verdicts*.md` 与 §1-§4。

---

## §0 常设裁定 (2026-09-25 起各轮沿用, 非某轮预登记)

> attempt 6 (tracer) 与 attempt 7 (analyst) 两个异 type 判分方独立收敛到同一读法; 此后各轮直接沿用, 不再重议。改动须用户裁定并另起一节。
- **占位 / 族写法** (`_n`、`nn`、`*`、未给端点的区间): 按**展开成员**核验 —— 展开后成员全部存在于一览 ⇒ 不计捏造; 占位写法本身**不计 recall** (②⁗)。字面口径 (占位即捏造) 只作敏感性分析并列报告。
- **方案规定的放疗**: 归 EX 或归 PR **均接受**, 不计 ④⁗「同标准域竞争」错归 (EX assumptions 要求方案治疗入 EX; PR 亦列举 radiotherapy; 题集 NOTES 两边均接受)。
- **④ 阈值** 仍为 max(1, 10% × 分母); 大分母 (≳200) 时须另报「确定错归」与「有争议错归」两个计数。

---

## §1 运行记录

两个 attempt 都跑满 6 次生产 `/api/ask_stream` (3 题 × 2 模型 id), 生产 = 本机 launchd
`com.sdtmrag.api` 直读主工作树, 每次跑前均已 `launchctl kickstart -k`。
全文 / usage / 徽章落 gitignored `data/study/st01/eval/runs/dm2_e2e/`, 不进版本库。

### 1.1 attempt 1 (代码基线 `37bcb3e`)

```bash
cd sdtm-rag
curl -s localhost:8000/api/info | grep -o '"federation":[a-z]*'   # → "federation":true
.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py
```

六条 summary 行 (脚本 `_summary_line` 原样):

```
dm01 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=105930 completion_tokens=11519 continue_rounds=0 truncated=False wall_seconds=202.1 answer_chars=5145
dm01 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=105930 completion_tokens=10741 continue_rounds=0 truncated=False wall_seconds=179.8 answer_chars=3446
dm02 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106889 completion_tokens=13193 continue_rounds=0 truncated=False wall_seconds=232.3 answer_chars=4102
dm02 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106889 completion_tokens=11810 continue_rounds=0 truncated=False wall_seconds=190.6 answer_chars=3382
dm05 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=107742 completion_tokens=14952 continue_rounds=0 truncated=False wall_seconds=255.8 answer_chars=6280
dm05 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=107742 completion_tokens=20314 continue_rounds=0 truncated=False wall_seconds=199.6 answer_chars=9667
# GATE attached: 6/6 PASS
# fell_back: 6/6   truncated: none   retried: none
```

研读包徽章 6 次完全一致: `sha=ed632b14cd34` / `chars=166563` / 52 章 / `reason=auto:domain+scope`;
B 部一览 74031 chars / 959 项。

**中途 OOM → 断点续跑 (过程记录, 非失败)**: 第一次跑到第 6 次调用时后台进程被系统以内存不足
杀掉 (前 5 次已落盘)。处置 = 给 runner 加 `--resume` 语义 (已落盘的 `<qid>_<model>.json` 原样
复用), 只补跑第 6 条, **没有**重打前 5 条 —— 重打等于让「跑批」和「判分」看两批不同采样。
上表前 5 行来自第一次进程, 第 6 行来自续跑进程, 数字未经加工。

### 1.2 attempt 2 (代码基线 `03096ad`, 规则句重写后)

```bash
cd sdtm-pedia && launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api
curl -s -o /dev/null -w "%{http_code}" localhost:8000/api/info    # 200 (~6s)
cd sdtm-rag && .venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume
```

`--no-resume` 是这一轮的硬要求 (§0 失败处置条款: 改后重跑 6 题**全部**, 不只失败题);
不加则会复用 attempt 1 的落盘档。

```
dm01 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106013 completion_tokens=13107 continue_rounds=0 truncated=False wall_seconds=211.3 answer_chars=6440
dm01 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106013 completion_tokens=12122 continue_rounds=0 truncated=False wall_seconds=196.6 answer_chars=5374
dm02 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106972 completion_tokens=12011 continue_rounds=0 truncated=False wall_seconds=209.8 answer_chars=4080
dm02 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106972 completion_tokens=13041 continue_rounds=0 truncated=False wall_seconds=205.1 answer_chars=6663
dm05 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=107825 completion_tokens=11637 continue_rounds=0 truncated=False wall_seconds=184.5 answer_chars=8114
dm05 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=107825 completion_tokens=17088 continue_rounds=0 truncated=False wall_seconds=242.5 answer_chars=8392
# GATE attached: 6/6 PASS
# fell_back: 6/6   truncated: none   retried: none
```

**新规则确实上线的旁证**: 同题 `prompt_tokens` 较 attempt 1 各 **+83** (105930→106013 /
106889→106972 / 107742→107825), 三题一致的 +83 = 改长后规则句的 token 差。
同题两个模型 id 的 `prompt_tokens` 逐位相同, 与「研读包对触发题是同一份、请求体只差 model」一致。

### 1.3 ⚠ Bedrock 回退 (两 attempt 相同, 本文件最重要的口径限定)

**12 次调用 (6+6) 全部 `fell_back=True` / `model_used=deepseek-v4-pro`**。根因是 AWS 账号
当前对 Bedrock 上的 Anthropic 模型无权限, `opus-5` 与 `sonnet-5` 两个路由组都命中同一条
`default-fallback`:

```bash
cd sdtm-rag
grep -c "not allowed for this account" logs/api.launchd.log     # >0 = 仍在拒绝
grep "model_fell_back" logs/api.launchd.log | tail -3
# BedrockError('{"message":"Access to Anthropic models is not allowed for this account."}')
# → model_fell_back model_id=opus-5 models_used=['deepseek-v4-pro']
```

后果: §0 写的「模型: opus-5, sonnet-5」**未兑现**, N=6 的模型维度塌陷为 1 ——
本文件是 **3 题 × 2 次采样**, 不是两个模型的对比。按指示未静默重跑, 事实原样留档。
附带: `done_event.verified` 仍按**用户选的 id** 报 (`opus-5`→True / `sonnet-5`→False),
与实际作答模型无关; 回退场景下这两件事会分叉 (既有行为, 非本单元引入)。

## §2 判分结果

判分均由**异 subagent** (opus, 规则 D) 做, 只读 §0 判据 + gitignored `judge_pack.json`
(6 runs + `item_list_text` 959 项), 不读本 plan、不读本 session。
逐 run 报告含真实 OID, 留 gitignored `runs/dm2_e2e/judge_verdicts{_attempt_1,}.md`;
本节只留无标识摘要 (表单 / 项目代称见 gitignored `data/study/st01/eval/dm1_codenames.md`)。

### 2.1 attempt 1 — **4/6, 业务 FAIL** (< §0 的 ≥5/6)

| run | 实跑模型 | ① 定义齐 | ② 候选齐 (零捏造) | ③ 标推测 | 判定 |
|-----|---------|---------|--------------------|---------|------|
| dm01 / zh / DS | deepseek-v4-pro (请求 opus-5) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS | **PASS** |
| dm01 / zh / DS | deepseek-v4-pro (请求 sonnet-5) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS | **PASS** |
| dm02 / ja / DS | deepseek-v4-pro (请求 opus-5) | **FAIL 2/3** | PASS gold 4/4, 捏造 0 | PASS | **FAIL** |
| dm02 / ja / DS | deepseek-v4-pro (请求 sonnet-5) | **FAIL 2/3** | PASS gold 4/4, 捏造 0 | PASS | **FAIL** |
| dm05 / en / AE | deepseek-v4-pro (请求 opus-5) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS (弱: 仅全局标记) | **PASS** |
| dm05 / en / AE | deepseek-v4-pro (请求 sonnet-5) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS | **PASS** |

**失败模式 = 类别轴混淆 (category-axis confusion), pattern 级**: DS 的记录类别沿 `DSCAT` 的 CT
取 3 值, dm02 两跑都只列了前两个, 再用**别的轴**把条数凑到 3 (一路用 `DSSCAT` 子类别再切一刀,
另一路拿 IG 的阶段/时点轴当第三类); 第三个 `DSCAT` 值全文 0 次出现, 且「无候选类别」一节
也没申报它 —— 缺失是静默的。同域同包同模型的 dm01 两跑三类全列 ⇒ **不是语料缺失, 是规则层
缺约束**: 原规则第 (1) 步只说「enumerate the record categories」没说沿哪条轴, 第 (5) 步
「说明哪类没候选」又挂在 (1) 的产物上, (1) 漏了 (5) 跟着哑, 两条一起失效。
归档: `evidence/failures/dm2_task9_attempt_1.md` (规则 B)。

**修法 (commit `03096ad`, 只动 `server/router.py::_DOSSIER_RULES`, pattern 级)**:
① 改为**沿域自身的类别变量 `--CAT` 的 CT 逐类穷举**, 每个类别值各起一个小标题, 在看任何
EDC 项目之前, 禁止用 `--SCAT` / epoch / 时点轴顶替; ② 把原 (2)(5) **合并** —— 每个类别小标题下
要么列候选, 要么明写「候補なし / no candidate item in the EDC」, 任何类别不得静默跳过
(合并是关键: 让「漏」变成看得见的空标题); ③ 每一条归属**行内**带 (推測), 不能只在开头声明一次。
**规则里不出现任何域名 / CT 取值 / 表单 / 项目 OID** —— 写题面 example 会把 dm02 修绿而让跨域
失败原样留着。同 commit 加 `test_rule_pins_category_axis_and_no_candidate_wording` 钉住实际
拼进 system 的那段文本含 `--CAT` 与 `no candidate` (措辞不是结构, 最容易被下次重写静默抹掉)。

### 2.2 attempt 2 — **6/6 PASS, 达标** (判分 agent 为新 opus, 未读 attempt 1 判分)

| run | 实跑模型 | ① 定义齐 | ② 候选齐 (named/4, 捏造) | ③ 标推测 | 判定 |
|-----|---------|---------|--------------------------|---------|------|
| dm01 / zh / DS | deepseek-v4-pro (请求 opus-5) | PASS (`DSCAT` 3/3 全枚举) | PASS (4/4, 捏造 0) | PASS (逐条内联) | **PASS** |
| dm01 / zh / DS | deepseek-v4-pro (请求 sonnet-5) | PASS (3/3 全枚举) | PASS (4/4, 捏造 0) | PASS (逐条内联, 最强) | **PASS** |
| dm02 / ja / DS | deepseek-v4-pro (请求 opus-5) | PASS (3/3 全枚举, 并显式拒绝用 `DSSCAT` 顶替) | PASS (4/4, 捏造 0) | PASS (逐条内联) | **PASS** |
| dm02 / ja / DS | deepseek-v4-pro (请求 sonnet-5) | PASS-有瑕 (瑕疵 A) | PASS (4/4, 捏造 0) | PASS-偏弱 (组级非逐条) | **PASS** |
| dm05 / en / AE | deepseek-v4-pro (请求 opus-5) | PASS-有瑕 (AE 无 `--CAT` CT, 显式改用 EDC 模块轴) | PASS (4/4, 捏造 0) | PASS-最弱 (瑕疵 B) | **PASS** |
| dm05 / en / AE | deepseek-v4-pro (请求 sonnet-5) | PASS-有瑕 (同上, 显式改轴) | PASS (4/4, 捏造 0) | PASS (逐条 `(inference)`, 含排除项) | **PASS** |

**捏造 0/6 且可复跑**: 判分方从 `item_list_text` 抽 958 个项目 OID + 21 个表单 OID, 对每份答案
两轮扫描 (反引号/括号内 token + 全文宽扫 `\b[A-Z][A-Z0-9_]{1,}\b`), 差集人工分流为 SDTM 变量名 /
NCI C 码 / 英文大写词 / 文件名, **6 份答案的差集中没有一个是 EDC OID 形状的未知项**;
区间简写逐前缀核过实际最大编号。表单归属 (OID 存在但挂错表单) 亦 0 处。

**三处瑕疵 (均未判 FAIL, 但要记住)**:
- **A** dm02/sonnet 的第三类用 `DSDECOD` codelist 名 (`OTHEVENT`) 代替 `DSCAT` 值 (`OTHER EVENT`),
  且 §まとめ 收尾时把这一整类丢掉 (正文有、总结没有)。
- **B** dm05/opus 的 (推測) 只到**章节标题级** + 开篇全局免责, 30 行三元组表与两组列表没有逐条标记;
  判据 ③ 未写死粒度, 按「章节级 > 单一全局免责」判过 —— 判据若收紧到逐条即会 FAIL。
- **C** dm05 两份把部位字段 / 注释字段也列进 AE 候选 (过度列举, opus 路径更重), 且 dm05/opus 一处
  区间漏报 (某组项目写成 8 个, 实为 10 个 —— 是 under-count 不是捏造, 同题 sonnet 写对);
  另: AE 两份全篇无任何「候補なし」声明 (它们自选的模块轴下无空模块), **该半结构在 AE 题上未被检验**。

**判分方对判据本身的三条意见 (原样收录, 记为缺口)**:
1. **② 对 AE 题几乎无判别力**: dm05 两份各点名 200+ 个 OID, 只要把 AE 相关的几张表整片倒出来,
   4 张 gold 卡必然被覆盖; 该判据**只测 recall, 完全不测 precision**, 过度列举不扣分。
2. **① 对 AE 域是空判据**: AE 的 definition text 不定义任何 `--CAT` 值, 「定义齐」在 AE 题上没有
   可核的清单, 两份答案只能显式改轴, 而「改哪个轴才算合格」判据没写。DS 题上 ① 是实打实的。
3. **③ 未规定标记粒度**: 「每条归属带标记」与章节级标记之间没有划线; 若要让 ③ 有判别力,
   需把粒度写死 (逐条 / 逐表行)。

### 2.3 attempt 3 — Claude 两模型 + 留出题, **两模型均未达 §0′ 目标, 业务 FAIL** (2026-09-25)

代码基线 `19e6ea3` (`_DOSSIER_RULES` 与 `03096ad` 一字不差)。**G0 PASS**: 12/12 `attached=True`,
12/12 `fell_back=False`, `models_used` 全为请求的 `global.anthropic.claude-{opus,sonnet}-5` (跑批脚本
`--require-no-fallback` 闸输出 `# GATE no-fallback: PASS`; 判分方无法核 G0, judge pack 不含这两字段 —— 由跑批日志证)。
判分 = 异 subagent (`oh-my-claudecode:critic` opus, 异 session; attempt 1/2 判分方的 subagent_type 未留档, 故不声称 type 相异), 只读 §0/§0′ + 两份 judge pack;
逐 run 报告 + 扫描脚本在 gitignored `runs/dm2_e2e_claude/judge_verdicts.md`。

| run | 模型 | ①′ | ②′ recall · 捏造 · precision | ③′ | 判定 |
|-----|------|----|-------------------------------|----|------|
| dm01 DS zh | opus-5 | P | 4/4 · 0 · 0% | P | **PASS** |
| dm02 DS ja | opus-5 | **F** (第三个 `DSCAT` 值以意译 + codelist 名 `OTHEVENT` 立题, 原文取值 0 次) | 4/4 · 0 · 0% | P | **FAIL** |
| dm05 AE en | opus-5 | P (声明 AECAT 无 CT, 改模块轴) | 4/4 · 0 · 0% | P | **PASS** |
| dm03 DS en 留出 | opus-5 | P | 4/4 · 0 · 0% | P | **PASS** |
| dm04 DM ja 留出 | opus-5 | P (声明无 `--CAT`, 改逐目标变量) | 4/4 · 0 · 0% | P | **PASS** |
| dm07 PR ja 留出 | opus-5 | P (声明 PRCAT 无 CT, 改 assumptions 手技类型轴) | 4/4 · **1** · 0% | P | **FAIL** (捏造在「不入 PR」排除清单) |
| dm01 DS zh | sonnet-5 | P | 4/4 · 0 · 0% | P | **PASS** |
| dm02 DS ja | sonnet-5 | **F** (`DSCAT` 只 2/3) | 4/4 · 0 · 0% | P | **FAIL** |
| dm05 AE en | sonnet-5 | **F** (未声明无 CT / 未点名轴) | 3/4 · 0 · 0% | P | **FAIL** |
| dm03 DS en 留出 | sonnet-5 | P | 4/4 · 0 · 0% | P | **PASS** |
| dm04 DM ja 留出 | sonnet-5 | **F** (同 dm05) | 4/4 · 0 · 0% | P | **FAIL** |
| dm07 PR ja 留出 | sonnet-5 | **F** (同 dm05) | 严 0/4 · **3** (虚构表单 OID) · 0% | P | **FAIL** |

| 模型 | in-sample (目标 3/3) | 留出 (目标 ≥2/3) | 达标 |
|------|---------------------|-----------------|------|
| opus-5 | 2/3 | 2/3 | ✗ |
| sonnet-5 | 1/3 | 1/3 | ✗ |
| deepseek (attempt 2 同尺子复判, 仅比较) | 5/6 (dm02「sonnet」跑 ①′③′ 严判 FAIL) | — | — |

**controller 非自洽复核 (关键两条)**: ① dm07 两份的 4 个疑似捏造 token 用独立脚本对 `item_list_text` 全量大写 token 集合查 ——
4/4 在答案中、0/4 在一览中, 捏造属实; ② sonnet dm04/dm05/dm07 答案全文 `CAT` 子串 0 次, ①′(b)(c) 「未声明」属实。

**读法 (必须同时写)**:
- **口径敏感性 (判分方报)**: ①′ 若接受「意译 + codelist 名」⇒ opus in-sample 3/3; 捏造若只计候选段 ⇒ opus 留出 3/3; 两宽口径同开 ⇒ opus 达标。
  **这两处宽口径是跑后才被发现的歧义, 本轮不改判** (跑后改尺子 = 下轮不可比), 只进 §0″ 候选修订。
- **sonnet 在任何口径下都不达标**: dm04/05/07 的 ①′ 失败与口径无关 —— 规则句要求的「无 CT 时明说并点名换轴」sonnet 三题全未执行。
  同一规则句下 deepseek 与 opus 在无 CT 域上都执行了 ⇒ 是**模型对规则句的遵从差异**, 不是研读包缺料。
- **第三个 `DSCAT` 值再次是薄弱点**: attempt 1 (deepseek) 的失败模式在 Claude 两模型的 dm02 (ja) 上复现 (sonnet 静默缺失 / opus 意译顶替);
  同域 dm01 (zh) / dm03 (en) 两模型均 PASS ⇒ 与**问句语言**相关的非稳态, n=1/格, 不下因果结论。
- **捏造首次非零**: attempt 2 的 deepseek 6 份捏造 0; 本轮 Claude 12 份中 2 份出现 (opus 1 个项目 OID 在排除清单; sonnet 3 个表单 OID 在候选表)。
- **precision 18/18 = 0%**: 判分方指出 §0′ 的「明显错归」定义过窄实际不设防 (抓不到自相矛盾归属、非 topic 变量错归) —— **该新判据本轮无判别力**。
- **观察项**: 答题语言与问句不一致 2/12 (opus dm01 zh→ja, sonnet dm05 en→ja); sonnet 虚构 SDTM 变量 `AETESTCD` 且把 CTCAE grade 对到 AESEV —— 判据无条款约束 SDTM 侧正确性。
- 归档: `evidence/failures/dm2_task9_attempt_3.md` (规则 B)。

### 2.4 attempt 4 — 规则句修订后, **opus 6/6 (主判) / sonnet 4/6 ⇒ 按 §0″ 目标 (每模型 6/6) 业务 FAIL** (2026-09-25)

代码基线 `7b9bdd0` (规则句 = `f8523ad` + 审查意见修订), `dossier:"on"`。**G0 PASS** (判分方从 judge pack 自核: 12/12 `dossier_attached=True`, `fell_back=False`, `models_used` 为 Claude 串)。
判分 = 异 subagent (`oh-my-claudecode:verifier` opus, 与 attempt 3 判分方 `critic` 不同 type), 只读 §0/§0′/§0″ + 两份 judge pack; 逐 run 报告 + 3 个扫描脚本在 gitignored `runs/dm2_e2e_attempt4/judge_verdicts.md`。

| run | opus-5 | sonnet-5 |
|-----|--------|----------|
| dm01 DS zh | PASS (④″ 1/28) | PASS |
| dm02 DS ja | PASS | PASS |
| dm05 AE en | PASS (④″ 8/418) | **FAIL ⑦″** (英文问, 答案主体日文) |
| dm03 DS en | PASS | PASS |
| dm04 DM ja | PASS | PASS |
| dm07 PR ja | PASS | **FAIL ④″** 2/18 = 11.1% (入院/退院日列为 PR 候选) |

- ③″ 捏造 **0/12** (attempt 3: 2/12); ⑤″ SDTM 变量捏造 **0/12** (attempt 3: 2); ①″ 分类轴 12/12 (attempt 3 同尺子: 7/12)。
- **同尺子复判 attempt 3 (修订前基线)**: opus **1/6**, sonnet **0/6** (主要败在 ⑥″ 推測位置 / ①″ / ⑦″)。⑥″ 属格式合规, 这组对比放大了「修订效果」, 不能读作推断质量提升了这么多。
- **controller 非自洽复核**: 独立脚本数 12 份答案的假名/汉字/拉丁字符 —— sonnet dm05 (en 问) 假名 764、opus dm05 同题 18 ⇒ ⑦″ FAIL 属实; 其余 11 份语言与问句一致。
- **口径敏感性 (必须并列读)**:
  - ④″(ii) 自相矛盾的四种形态 (条目内「本体属他域 / 仅作派生源」注记、同句条件式二选一、排除条目内提 SUPP 方案、表单级短语是否展开到项目) **§0″ 未写死**。主判不计 ⇒ opus 6/6; 严口径全计 ⇒ opus **3/6** (dm01 10.7% / dm03 16.1% / dm04 15.4%)。
  - ④″(i) 「有标准域可承载时 SUPP 不算合理承载」是判分方附加解释; 不加 ⇒ sonnet 5/6, 仍不达标。
  - **sonnet 在任何口径下都不达 6/6**: ⑦″ 语言失败与口径无关, 且与 attempt 3 同题同病 ⇒ 规则句在 sonnet 上执行不稳。
- **泛化维度缺席**: 6 题全部在 attempt 3 已见 (§0″ 预登记), opus 6/6 是 in-sample 修复验证。
- 判分方另报: ①″ 未要求形态识别正确 (sonnet dm05 称 AE 无 `--CAT`, 实有 AECAT); gold 把生存转归项算 DS 候选与 IG 「生存状态入 SS」有张力, 建议复核该 gold 卡; 10% 阈值对小分母 (DM/PR 6-18) 过敏、对 AE (≈420) 几乎不触发; KB 内 PR assumptions 提到 PRSTAT 而 spec 无 (⑤″ 真值源内部不一致)。
- 归档: `evidence/failures/dm2_task9_attempt_4.md`。
- **用户裁定 (2026-09-25)**: ④″(ii) 的四种形态**不算**自相矛盾 ⇒ attempt 4 **opus 6/6 成立**, sonnet 4/6; 本裁定自 §0‴ 起写入判据。

### 2.5 attempt 5 — 新留出题 + 语言结构性修法, **字面口径 opus 5/6 · sonnet 4/6 ⇒ 按 §0‴ 目标 (每模型 6/6) 业务 FAIL** (2026-09-25)

代码基线 `28f60c7` (规则句 `7b9bdd0` + 语言行 `2868ba5`/`28f60c7`), `dossier:"on"`。**G0 PASS** (判分方自核 12/12)。
判分 = 异 subagent (`oh-my-claudecode:scientist` opus; 与 attempt 3 `critic` / attempt 4 `verifier` 不同 type), 只读 §0-§0‴ + judge pack + 出题 NOTES;
逐 run 报告 + 4 个扫描脚本在 gitignored `runs/dm2_e2e_attempt5/judge_verdicts.md`。

| run | opus-5 | sonnet-5 |
|-----|--------|----------|
| dm09 IE en 新留出 | **FAIL ③** (举例称某 token 为 EDC OID, 一览不存在; 其余 48+5 个 OID 全真) — 宽口径 PASS | PASS |
| dm10 MH zh 新留出 | PASS | **FAIL ④** 4-5/20 > 阈值 2 (吸烟组以「弱候选」列出, SU 有标准变量) — 宽口径 PASS |
| dm11 EX ja 新留出 | PASS | PASS |
| dm12 PC en 新留出 (空域) | PASS (明写无候选, 零诱饵) | PASS |
| dm05 AE en 回归 | PASS | **FAIL ①‴** (称 AE 无 `--CAT` 变量并引 spec 为据, 实有 AECAT) |
| dm07 PR ja 回归 | PASS | PASS (④ 6-7/≈78, 余量 < 1 项) |

| 模型 | 新留出 | 回归 | 字面 | 宽口径 |
|------|--------|------|------|--------|
| opus-5 | 3/4 | 2/2 | **5/6** | 6/6 |
| sonnet-5 | 3/4 | 1/2 | **4/6** | 5/6 (dm05 任何口径 FAIL) |

- **语言修法生效**: ⑦ 12/12 PASS; sonnet dm05 (attempt 3/4 两轮 en→ja) 本轮英文作答 —— controller 独立计数: 平假名 6 / 拉丁词 609。
- **空域分支首次被检验**: dm12 两模型均明写无候选、诱饵 (检体/基因型类) 零误列。
- **controller 非自洽复核**: ① opus dm09 IESPID 段内 OID 形 token 对一览全量大写 token 集合查 → 不存在, 属实; ② sonnet dm05 原文「No AECAT variable … case (c)」并引 spec 为据, 与 `knowledge_base/domains/AE/spec.md` 矛盾, 属实 (把「上下文未见」当「不存在」)。
- **读法**: opus 唯一失败是示例值里 1 个错 OID (③ 全文作用域, 用户 §0″ 写死), 泛化维度首次有数据 = opus 新留出 3/4 (宽 4/4)。sonnet 的失败分散在三类 (形态误判 / 边缘候选 precision / precision 余量极小), 不是单一可修模式。
- 判分方对判据意见 7 条 (示例值是否入核 / 「弱候选」三态 / ②③ 族简写口径不对称 / 同标准域竞争 / ①⑤ 真值源不一致 / 阈值区分力不均等) —— 本轮不改判。
- 归档: `evidence/failures/dm2_task9_attempt_5.md`。

### 2.6 attempt 6 — Opus 单模型补跑, **主口径 5/6 ⇒ 按 §0⁗ 目标 (6/6) 业务 FAIL; auto 不恢复** (2026-09-25)

代码基线 `0b71822`, `dossier:"on"`, 仅 `opus-5`。**G0 PASS** (判分方自核)。判分 = 异 subagent (`oh-my-claudecode:tracer` opus; 与 critic / verifier / scientist 均不同 type); 报告 + 4 脚本在 gitignored `runs/dm2_e2e_attempt6/judge_verdicts.md`。

| run | 判定 | 要点 |
|-----|------|------|
| dm09 IE en | PASS | ③ 零捏造 (attempt 5 的示例值错 OID 未复现) |
| dm10 MH zh | **FAIL ⑦** | 中文问 → 日文作答 (attempt 5 同题中文作答) |
| dm11 EX ja | PASS (严口径 A FAIL) | 放疗项入 EX 是否算「同标准域竞争」—— §0⁗ 未定义「专门」|
| dm12 PC en | PASS | 空域 |
| dm05 AE en | PASS | |
| dm07 PR ja | PASS | |

- 同尺子复判 attempt 5 opus: 主口径 **5/6** (dm09 ③⁗ 示例值) —— 两轮都是 5/6, **失败题不同** (示例值 OID → 语言)。
- 「gold 项目被列为排除」两轮 **0/20** ⇒ 新增「他域专属则列排除」未以 recall 为代价。
- **controller 非自洽复核**: dm10 问句 `answer_language` = zh, 追加行为中文语言行; 答案平假名 595 / 漢字 657 (attempt 5 同题 31 / 978) ⇒ ⑦ FAIL 属实。**语言行降低了概率但未消除** (attempt 5: 0/12 语言失败; attempt 6: 1/6)。
- **读法 (关键)**: attempt 5→6 opus 主口径都是 5/6, 且每轮失败落在**不同的**低频模式上 (示例值自造 OID / 语言漂移)。规则句措辞修一个, 下一轮在别处冒一个 —— 这是**采样尾部**, 继续改措辞收敛性差; 下一步若要逼近 100% 应换**结构性后验闸** (生成后确定性核 OID ∈ 一览 + 语言计数, 不过则重生成或标注), 而非再改规则句。
- 判分方对判据意见: ⑦ 计数口径写死 / ④⁗「专门」需定义 (题集自身在 EX/PR 间两放) / ③⁗ 对 SDTM 侧示例与 `_n` 占位的作用域 / 短 OID 撞词白名单 / ④ 分母需机器可识别段标题。
- 归档: `evidence/failures/dm2_task9_attempt_6.md`。

### 2.7 attempt 7 — 确定性闸上线后 Opus 实跑, **主判 6/6 ⇒ 达 §0⁵ 目标 (有两处读法前提)** (2026-09-25)

代码基线 `d42b51c` (闸 13 commit + judge pack first_answer), 生产 kickstart 后 `/api/info.dossier_gate == true` (controller 跑前实测)。**G0 PASS** + `GATE grounding: PASS` (6/6 grounding 非 null)。
判分 = 异 subagent (`oh-my-claudecode:analyst` opus; 与既有 4 个判分方及本单元实现 / 审查方均不同 type), 不读闸源码、不调闸, 自写脚本; 报告在 gitignored `runs/dm2_e2e_attempt7/judge_verdicts.md`。

| run | 判定 | 备注 |
|-----|------|------|
| dm09 IE en | PASS | |
| dm10 MH zh | PASS | ⑦ zh (attempt 6 同题 zh→ja 未复现) |
| dm11 EX ja | PASS | 放疗 11 项归 EX (NOTES 事先接受) |
| dm12 PC en | PASS | 空域, 明写无候选 |
| dm05 AE en | PASS | 占位族写法按展开成员核验 |
| dm07 PR ja | PASS | |

- **闸自身**: 6/6 首轮即过、`regenerated=0`、`final.ok=false` 0 ⇒ **拦对 0 / 误拦 0**; 主判口径闸漏报 0; `lang_observed=None` 0; zh→ja 误判 0。⚠ **重答路径本轮零真实触发** —— 其有效性仍只有单测 + 42 份离线回放为证。
- **敏感性 (必须并列读)**: 严 A「占位 / 通配族写法按字面计捏造」⇒ 4/6 (dm05/dm09; 该形态闸按 spec §2 白名单放行, 判分方记为 §7 未登记的新形态); 严 B「放疗以 PR 为专门域」⇒ 5/6; A+B ⇒ 3/6。主判两处读法与 attempt 6 判分方 (tracer) 的主口径一致。
- **controller 非自洽复核**: 独立脚本对 6 份答案的反引号 / 方括号 / 圆括号 token 查「既不在一览、也不在 SDTM spec 标题」—— 仅 5 个, 全部位于 SDTM 变量上下文、与一览 OID 零 3 字符前缀共享 ⇒ 是 assumptions 点名的 SDTM 侧变量 (⑤‴ 并集), 非 EDC 捏造; ③ 零捏造属实。
- **读法**: 连续 attempt 5→6→7 opus 主口径 5/6 → 5/6 → 6/6, 本轮 6/6 **没有经过闸的重答**, 是采样首轮全对; 不能读成「闸把 5/6 修成 6/6」。6 题均已见过 (修复验证非泛化)。
- 判分方对判据意见: 占位符地位 (③⁗/②⁗/③″ 三处不一致) 与放疗双归属须写死; ④ 阈值在大分母 (≈424) 上无区分力; ④ 分母人工计数成本高。

### 2.8 attempt 8 — 研读包 prompt cache 布局上线后 Opus 实跑, **主判 6/6 (质量未降) + 缓存判定 PASS + 输入成本 33.5%** (2026-09-25)

代码基线 `24ecca8` `5a3f9e7` + 前缀回归测试; 生产 `/api/info.dossier_prompt_cache == true` (跑前实测)。G0 PASS + GATE grounding PASS。
判分 = 异 subagent (`oh-my-claudecode:test-engineer` opus, 未用过的 type), 自写 5 脚本, 不读闸源码; 报告在 gitignored `runs/dm2_e2e_attempt8/judge_verdicts.md`。

| run | 业务判定 | 缓存 (usage 实收) | 有效输入成本 / attempt 7 全价 |
|-----|---------|------------------|-------------------------------|
| dm09 IE en | PASS | write 144264 | 182582 / 146513 (125%, 首题写入溢价) |
| dm10 MH zh | PASS (**闸重答 1 次**) | read 288528 (两轮均命中) | 40939 / 148008 (28%) |
| dm11 EX ja | PASS | read 144264 | 16620 / 146455 |
| dm12 PC en | PASS | read 144264 | 18628 / 148463 |
| dm05 AE en | PASS | read 144264 | 20794 / 150629 |
| dm07 PR ja | PASS | read 144264 | 18388 / 148223 |

- **缓存判定 PASS**: 第 1 题写入 144264 (> 100K); 第 2-6 题全部 read ≥ 144264, 0 非豁免未命中; 闸重答轮同前缀命中。**合计有效输入成本 = attempt 7 的 33.5%** (含一次重答; 口径 = 未命中×1 + 写入×1.25 + 读取×0.1; 复算脚本见 worklog)。
- **闸首次生产真实触发**: dm10 首轮 zh 问 → 日文作答 (判分方逐节 kana 比 0.37-0.58, 首节中文 0.03), 闸拦下、重答为中文 ⇒ **闸拦对 1 / 误拦 0 / 漏报 0**; `lang_observed=None` 0。这是重答路径的第一份生产实证。
- **敏感性**: 三个独立宽口径 (dm09 sponsor 检验码按 OID 形态入核 / dm11 药剂级中止理由算 DS 竞争 / dm05 日文原名组标题计入主体语言) 各使一题翻转 ⇒ 最低 5/6。
- 6 题均已见过 ⇒ 修复验证 + 重复采样, 非泛化证据。判分方意见 7 条 (③⁗ 限定槽位 / 撞词清单 / ⑦ 原文类别名标题与固定标记 / ④⁗ 双点名情形 / judge pack 加 usage / ⑤ timing 变量真值源)。

## §3 成本

| qid | 请求 model id | attempt 1 prompt / completion | attempt 2 prompt / completion |
|-----|---------------|-------------------------------|-------------------------------|
| dm01 | opus-5 | 105930 / 11519 | 106013 / 13107 |
| dm01 | sonnet-5 | 105930 / 10741 | 106013 / 12122 |
| dm02 | opus-5 | 106889 / 13193 | 106972 / 12011 |
| dm02 | sonnet-5 | 106889 / 11810 | 106972 / 13041 |
| dm05 | opus-5 | 107742 / 14952 | 107825 / 11637 |
| dm05 | sonnet-5 | 107742 / 20314 | 107825 / 17088 |

- 每题输入稳定在 **106-108K prompt tokens** (deepseek 侧计数), 研读包本身 166563 字 /
  ≈134K token (cl100k_base 估计, 见 `dm2_dossier_tokens.md`) —— 两个口径不同源, 不可直接相减。
- **cache 命中: n/a**。`usage` 实收键只有 `prompt_tokens` / `completion_tokens` / `total_tokens`,
  无 `cache_read_input_tokens`; 实际作答的是 deepseek, 本就不走 Anthropic prompt cache。
  这一格要等 Bedrock 权限恢复 + (可选) Task 11 prompt cache 之后才有意义。
- 单次 wall time 180-256 s, 6/6 `truncated=False` / `continue_rounds=0` / 0 次重试。

**attempt 3 (Claude 实收, 2026-09-25)**:

| qid | prompt (两模型同) | opus-5 completion / wall s | sonnet-5 completion / wall s |
|-----|------------------|---------------------------|-----------------------------|
| dm01 | 147339 | 8965 / 129.8 | 7306 / 84.4 |
| dm02 | 148895 | 5100 / 83.3 | 12691 / 142.4 |
| dm05 | 150148 | 10680 / 144.3 | 1942 / 37.7 |
| dm03 | 155543 | 7376 / 96.8 | 7060 / 77.3 |
| dm04 | 146791 | 3349 / 58.1 | 1591 / 33.1 |
| dm07 | 147738 | 8851 / 117.6 | 2248 / 44.8 |

- **Claude 原生计数 146.8K-155.5K, 4/12 次 > T2 的 150K 线**。T2 闸的 133652 是 cl100k_base 估计 (见 `dm2_dossier_tokens.md`),
  Claude tokenizer 实收比它高约 10%; 已记为 T2 闸的口径缺陷 (估计值作闸, 实值越线), 不影响本轮调用 (未截断, 模型上下文远大于此)。
- **cache 命中: 仍 n/a** —— Claude 实收 `usage` 键同样只有 `prompt_tokens`/`completion_tokens`/`total_tokens`, 每次全价。T11 现可做。
- 12/12 `truncated=False` / `continue_rounds=0` / 0 次重试。**L1 `fell_back` 两分支现均有真实 Bedrock 实测**
  (attempt 1/2 = 真回退 `True`, attempt 3 = 真未回退 `False` 且 `models_used` 为真实模型串)。

## §4 结论与限定

1. **业务判定 PASS**: attempt 2 **6/6 ≥ §0 预登记的 5/6**。三条判据无一条在任何 run 上 FAIL。
2. **结论范围限定 (硬)**: 6 次调用全部 `fell_back=True`, 实际作答模型 **只有 deepseek-v4-pro**。
   本文件 **不是** Opus 5 / Sonnet 5 的对比, 也不构成这两个模型在研读包下的任何结论;
   它是「研读包通道 + 规则句」在**一个**模型上的 3 题 × 2 次采样。
3. **有效结论**: (a) 研读包通道的 grounding 成立 —— 约 450 处 EDC 项目主张、**捏造 0**, 一览穷尽 +
   行式原样引用按设计工作; (b) 规则句的修法是**模式级**而非题面级 —— 三个 DS run 一律走
   「`--CAT` 值 → 候选 或 候補なし」同一骨架, 两个 AE run 一律先声明「无 `--CAT` CT」再显式换轴,
   不是记住了某几个 OID。
4. **attempt 2 属修复验证 (in-sample), 非泛化验证**: attempt 2 的规则句是**针对 attempt 1 的
   失败重写**, 并在**同一 3 题**上复跑 —— 题目在修法之前就已知, 所以 6/6 证明的是「这次修法
   把已知的失败模式修掉了」, 不是「这套规则句在没见过的映射题上也成立」。留出题
   **dm03 / dm04 / dm06 / dm07 未跑**。下次 (Bedrock 权限恢复后的 Claude 重跑) 必须从留出题里
   加 **≥2 题**, 否则泛化维度永远缺席。
5. **未覆盖**: AE 题上的「候補なし」分支未被检验; 判据 ② 不测 precision; 判据 ③ 粒度未写死
   (三条均入 `RETROSPECTIVE_dossier.md` §2 缺口)。`dm08` 型长名前缀问句不会自动触发 (D1 已知限制,
   需手动 `dossier: on`)。
6. **Bedrock 权限恢复后的重跑命令** (拿 Claude 两模型维度的结论):

```bash
cd sdtm-rag
grep -c "not allowed for this account" logs/api.launchd.log       # 先确认不再拒绝
cd .. && launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api
cd sdtm-rag && .venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume
# 再派**异 subagent** (规则 D) 只读 §0 + 新 judge_pack.json 判分, 结果另起 §2.3
```

7. **(2026-09-25) 第 6 条已执行 = attempt 3**, 结果见 §2.3: 两模型均未达 §0′ 目标 (opus 2/3·2/3, sonnet 1/3·1/3)。
   上面第 2 条「本文件不是 Claude 对比」对 attempt 1/2 仍成立; Claude 结论只以 §2.3 为准。

> 旧判分档不要删 (规则 B): `runs/dm2_e2e/judge_verdicts_attempt_1.md` = attempt 1,
> `judge_verdicts.md` = attempt 2; 重跑前先把后者改名, 免得新判分 agent 读到上一轮结论。
