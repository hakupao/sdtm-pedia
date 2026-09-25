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

> 旧判分档不要删 (规则 B): `runs/dm2_e2e/judge_verdicts_attempt_1.md` = attempt 1,
> `judge_verdicts.md` = attempt 2; 重跑前先把后者改名, 免得新判分 agent 读到上一轮结论。
