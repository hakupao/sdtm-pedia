# 检索续跑 — 下一轮 kickoff

> 路由词: **「检索续跑 开始任务」**
> 建立: 2026-08-06 (Plan B Phase 2 + CDISC section 化 + study golden v2 三线收官后)
> 红线: 真实 study 的 form/field OID / label / 题面 / 别名词**只允许**存在于 `sdtm-rag/data/study/` (gitignored)。
> 任何 committed 文件与报告零真名; 红线检查**必须程序化** (与 `data/study/st01/catalog.json` 比对), **不许用"我觉得这个不算"豁免**。

## 0. 一句话现状

CDISC 与 study 两条检索轨的**判据都刚被修准**, 基线数字随之下修 —— 这是判据变准, 不是检索回归。
两把尺子现在都有判别力, 且各自指出了明确靶子。

## 1. 当前基线 (引用必须带口径, 否则会被误读)

| 轨 | 配置 | 值 | 口径 |
|---|---|---|---|
| CDISC | hybrid-only | 81.07% | 路径级判据 (未受本轮影响) |
| CDISC | hybrid + S1 | **98.93%** | **section 级判据** (`路径#节$`), 2026-08-07 D2 修完后; 此前 95.71% |
| study | v2, S2 关 | **80.49%** | v2 题集 (48 计分) |
| study | v2, S2 开 | **87.50%** | 同上; S2 真实增益 **+7.01pt**, 改善 5 题回归 0 题 |
| study | v1.1, S2 开 | 100.00% | **该题集已饱和, 判别力耗尽 —— 不要再用它衡量新改动** |

**三版 study 题集分数互不可比** (一版一把尺子), 只有同版内的开关对照才有意义。
CDISC 新旧口径同理。引用 98.93% 必须写明 "section 级判据"; 引用 81.07% 必须写明 "hybrid-only"。

> ⚠️ **CDISC 那一行有个已知陷阱**: 98.93% 与**已作废的路径级口径**数值相同, 且 18 题子集 (100.00%)
> 与其余 122 题 (98.77%) 也逐位全同。这是**结构必然不是巧合** —— 两把尺子的分歧只在那 18 题,
> 拉满后全集必然回到 138.5/140。**故数字对比在此无判别力, 禁止用"98.93%"论证任何事**;
> 判别只能靠 section 名 (q109 旧召回 `C66734` / 新召回 `C99073`)。已作废的路径级 98.93% 含约 3pt
> 假命中水分, **不得与本行并排陈列**。详见 `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md` §⚠️。

## 2. 剩余工作 (按依赖排序, 顺序有实质理由)

### A. q38 chapters 整文件单块策略
CDISC 140 题里**唯一一道 recall 0.0** 的题。根因: `chapters/` 下 ≤20KB 的文件整个当一个 chunk
(ch01/ch02/ch03 各只有 1 个), 语义被稀释。属 chunk 构造侧改动, 需重建索引。
**排在判据修准之后是有意的** —— 用粗判据量不出 chunk 构造改动的真实效果, 现在判据准了才能测。

### B. 联邦答题 eval (含一行硬前置修复)
**硬前置 (必须先做)**: `eval/run_eval.py` 的 `_FederatedAdapter.build_messages` 把 corpus
硬编码成 `"both"`, 应改为 `self.routed[-1]`。**一行改动 + 一条测试**; 调用序已核实安全
(`retrieve` 在 276 行, `build_messages` 在 309 行, 同循环体)。只影响答题侧 system prompt 拼接,
检索闸全是 `--retrieval-only` 故历史数字未被污染。
之后建答题侧的联邦闸 —— 目前答题侧联邦路径只有单测 + 冒烟, 没有成规模的闸。

### C. Plan B Phase 4 联网搜索开关
**必须排最后**: 其验收标准是"开关关 = 现状零回归", 而答题侧现无成规模闸 —— 先有 B 才有对照,
否则这条验收是空话。spec: `docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md` §Phase 4。

### D. 两个新浮现的靶子
1. **study `form_overview` 类别仅 50%** (v2 实测, S2 开)。失分 6 题全是 v2 新题, 继承题 0 失分。**未排期**。
2. ~~**CDISC 那 4 道假命中背后的真实检索缺陷**~~ → ✅ **DONE 2026-08-07**。S1 对 VARIABLE_INDEX 改按
   CT 码 / 变量名**字面定位 section** (映射从索引反建, 不拼格式串)。18 题子集 **75.00% → 100.00%**
   (5 升 0 回归), 其余 122 题逐题 Δ0, 823 → 852 passed。三方隔离抓到 3 条实现方自查漏掉的缺陷
   (锚点饥饿 / 部署路径 502 / guard 口径错位) 全部已修。
   收口 `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md`。
   **⚠️ 遗留**: VI §三 正文在 15 变量处截断, section 级判据对此零判别力 (q109/q69 的 gold 压在第 15 位
   过关) —— **禁止把"18 题 100%"读作"VI 类问题已解决"**; 修 VI ingest 截断是独立单元。

### ⛔ 已裁定不做
**Plan B Phase 3 (CDISC 变量索引挤占)** —— 勘察实证放弃, 证据
`sdtm-rag/evidence/checkpoints/planb_phase3_probe_not_worth_doing.md`。生产通道挤占失分题数 = 0,
按 spec 实现修法反事实实跑 Δrecall **精确为 0**, 而下行风险真实 (−0.71pt)。它在修一个已被既有 S1 修掉的问题。

## 3. 本轮立下的硬规矩 (下一轮必须继续守)

1. **判据检查工具必须与被检查的判据逐字同语义**。本轮 lint 剥 `.md` 后匹配、严于真实判据, 制造 8 条假阳性,
   并连锁导致出题人删掉合法 gold、lead 做出错误判断。已加"两者语义等价"的测试锁。
2. **写「实测」必须附可复跑的一行命令**, 写不出命令就不许用这个词。
   理由 (审阅者原话): *一条写错的「实测」比缺陷本身更值得纠正 —— 它会让下一个人跳过复验。*
3. **红线检查程序化, 不许自我豁免**。lead 本轮曾把 17 个真实 form 标识写进待提交文件,
   并在自查里用"属通用缩写"放行, 靠程序化复扫才抓出。
4. **三方隔离** (规则 D): 出题 ≠ 审题 ≠ 抽检/验收, 各用不同 `subagent_type`。本轮三方各自抓到了对方看不见的缺陷。
5. **规则 A 抽样总体应等于本轮实际变更集合**, 而非变更后全集 (抽检人 §4.2 建议; 否则改写率中等时抽不到要害)。

## 4. 必须随分数一起声明的已知限制

- **study 继承题存量债** (为保 v1.1 历史可比性刻意不动): 3 题 fact 命中 >100 卡 (最宽 574/481/352) /
  1 题**全部 fact 无判别力** (fact_recall 结构上恒 1.0) / **7 题题面回声即得分**。v2 新题 25 道四类均为 0。
- **harness 系统性盲区**: 子串判据**看不出"两项互换"** —— 近义双卡判别题若把两个 OID 的语义对调,
  source 与 fact **仍双满分**, 而这类题的出题意图正是考这个映射。
  **这类题的成绩必须在 `--judge` 语义模式下读**; 纯子串模式只能证明"检索找对了卡", 不能证明"答案没说反"。
- **S2 通道③ 别名表只有 1 条**, 通用性无从评估。
- **②a 多 token 交集的 fire 正确性证据仍为 n=1** (爆炸半径: 27 题中实际 fire 1 题); 全库统计证明的是
  形状的 cap 安全性与复现性, **不是** fire 正确性。

## 5. 入口文件

| 用途 | 路径 |
|---|---|
| 本轮三份收口证据 | `sdtm-rag/evidence/checkpoints/{planb_phase2_study_lookup,cdisc_gold_section_granularity,study_golden_v2}.md` |
| Phase 3 放弃裁定 | `sdtm-rag/evidence/checkpoints/planb_phase3_probe_not_worth_doing.md` |
| v2 扩容计划 (含判据语义订正的教训段) | `docs/superpowers/plans/2026-08-06-study-golden-v2-expansion.md` |
| S2 实施计划 | `docs/superpowers/plans/2026-08-06-plan-b-phase2-study-structured-lookup.md` |
| Plan B spec (Phase 4 定义) | `docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md` |
| gold 唯一性 lint | `sdtm-rag/eval/lint_gold.py` (AND + OR 双侧) |
| study 题集 v2 + 审计脚本 | `sdtm-rag/data/study/st01/eval/{test_set_study_v2.yml,audit_v2.py}` (gitignored) |

## 6. 开跑前的自检命令 (全部应绿)

```bash
cd sdtm-rag
.venv/bin/python -m pytest -q                                   # 823 passed
.venv/bin/python -m eval.lint_gold data/study/st01/eval/test_set_study_v2.yml \
    --catalog data/study/st01/catalog.json                      # EXIT 0
.venv/bin/python data/study/st01/eval/audit_v2.py               # ALL PASS
curl -s localhost:8000/api/info                                 # federation: true
```
