# C3 — event 通道 precision 取舍单元 (2026-08-26)

> 定位: 最终整分支审查列的候选 C3 ("逐条相减"替代"整 form 让位" + 名称→assignment
> 入口), 要求**合成一个带数据判据的单元, 而不是各自反射性补齐**。本文件是那个判据。
> 尺子: `data/study/st01/eval/test_set_events_v1.yml` 33 题 (gitignored, 题面零进 git)。
> 口径: 命中 = 该题返回集合里**至少一条**落在 `expected_sources`; precision = 全部
> 返回里 tp 占比。全部数字为本轮实跑, 脚本逻辑见 §5。
> 红线: 全文零真名, 一律用题号 (`ev_qNN`) + 类别 + 计数。

## 0. 一句话结论

**复审原议的两个半边, 数据上都不该做** —— 各自零 recall 收益、纯加噪声。真正的杠杆在
**Tier 1b 的判别力闸**: 让清单过长的 form 整个不 fire, precision **10.81% → 54.00%**,
返回 **259 → 50**, 代价是 33 题里丢 1 题 (`ev_q10`, 使 `event_form_assignment` 由 1/5
变 0/5)。已按用户裁定实施 (`_MAX_ASSIGNMENTS_PER_FORM = 1`)。

## 1. 基线逐层分解 (先归因再谈方案)

| 层 | 返回 | tp | fp | 层内 precision |
|---|---|---|---|---|
| Tier 1a (OID 精确) | 5 | 5 | 0 | **100%** |
| Tier 2 (collect_scope 减法) | 12 | 12 | 0 | **100%** |
| **Tier 1b (form → 原始清单)** | **220** | **6** | **214** | **2.7%** |
| Tier 3 (名称子串) | 22 | 5 | 17 | 22.7% |
| 合计 | 259 | 28 | 231 | 10.81% |

全局 259/28/10.81% 与 `study_workflow_events.md` §6-15 逐位吻合 (独立复算)。
**Tier 1b 一层占 85% 的返回与 93% 的噪声** —— 全局那个 10.81% 基本由它一层决定。

各 form 的 assignment 清单长度分布: `{1: 13, 2: 3, 4: 1, 14: 1, 15: 1, 18: 1, 40: 1}`
—— 噪声集中在那 4 个长清单 form。

## 2. 复审原议的两个半边: 实测都是纯亏损

| 方案 | 命中 | 返回 | precision |
|---|---|---|---|
| 基线 (整 form 让位) | 21/33 | 259 | 10.81% |
| 半边 A: 逐条相减 | **21/33 (不变)** | 309 | **9.06%** |
| 半边 B: 名称→assignment 入口 | **21/33 (不变)** | 297 | **9.43%** |
| A + B (复审原议的 C3) | **21/33 (不变)** | 347 | **8.07%** |

**半边 A 的诊断值得单独记**: 它要修的是一个**真实的设计缺陷** —— "整 form 让位"会静默
吞掉该 form 里被该 item 隐藏、但仍是真实分配的条目。实测确认缺陷存在: 33 题共吞掉
**66 条**, 其中 **12 条确实在 gold 里**。但那 12 条**全部属于已经命中的题**, 所以在
"每题≥1条 gold"这个口径下, **这把尺子根本看不见这个缺陷**。
⇒ 现在修它 = 确定付出 50 条噪声, 换一个尺子量不到的收益。**判定: 不做**, 待评测口径
换成条目级 recall 后重新评估 (见 §4 限定③)。

## 3. 采纳方案: Tier 1b 判别力闸

`_MAX_ASSIGNMENTS_PER_FORM`: 该 form 的 assignment 清单超过本值 = 不具判别力, **整个
跳过**。与既有 `_MAX_CARDS_PER_MATCH` 同精神。

| 阈值 | 命中 | 返回 | precision | 相对基线新丢 |
|---|---|---|---|---|
| 全去掉 Tier 1b | 15/33 | 41 | 53.66% | 6 题 (`ev_q10` + 5 题 repeating_rule) |
| **=1 (采纳)** | **20/33** | **50** | **54.00%** | **1 题 (`ev_q10`)** |
| 2 ~ 13 | 20/33 | 54 | 50.00% | 1 题 (同上; 多出的 4 条实测全是 fp) |
| ≥20 | 21/33 | 189~259 | 14.81%~10.81% | 0 |

逐类 recall (基线 → 采纳后):

| 类别 | 基线 | 采纳后 |
|---|---|---|
| repeating_rule | 5/5 | **5/5** |
| item_collection_scope | 5/5 | 5/5 |
| oid_name_mapping | 6/6 | 6/6 |
| conditional_event | 4/7 | 4/7 |
| event_timing | 0/5 | 0/5 |
| **event_form_assignment** | **1/5** | **0/5** ← 唯一变化 |

**读法**: Tier 1b 的真实价值集中在**短清单**上 (repeating_rule 5/5 全保住); 它服务的
另一类 `event_form_assignment` 即便放任 214 条噪声也只有 1/5 —— 那 1 题更像撞上的,
不像稳定能力。闸拿掉的不是一个 working capability。

**被淘汰的替代形状**: "Tier 1b 每题最多贡献 K 条" 被全面压制 (K=1 时 20/33 · 61 返回 ·
44.26%, 各项均劣于 form 级闸), 且取哪 K 条依赖 `dict` 插入序 —— 该脆弱性已记在
`study_workflow_events.md` 已知限制里, 不宜再往上叠判据。

## 4. 四条限定 (引用上面任何数字必须同框)

1. **n=33 且是自出的尺子**, 采纳方案与基线只差 **1 题** —— 这个 margin 在 33 题上就是
   噪声量级, 不构成"cap=1 优于基线"的强证据。
2. **`resolve_events` 零生产调用方** —— 本次改动今天不影响线上任何一个字节。卡片侧
   `resolve()` 与 `_form_assignment_index` 无交集 (引用面 grep 确认), 结构上不受影响。
3. **评测口径对条目级 recall 失明** —— §2 半边 A "无收益"的结论完全由这个口径导出;
   换成条目级 recall / F1, 结论可能翻。
4. **对 33 题之外的泛化未测**。特别地, `=1` 意味着通道**永远无法**回答"这个 form 被
   分配到 2 处以上"这类问法。

**契约变更留痕**: 既有测试 `test_resolve_events_form_oid_lists_raw_assignments` 原用一个
2 条 assignment 的 form 断言"两条都在", 该断言在本次之后**不再成立**。已改写为
`..._lists_assignments_without_subtraction` (用 1 条 assignment 的 form 演示同一意图:
Tier 2 会减、Tier 1b 不减), 并在 docstring 里显式记下契约变更 —— **不是改绿, 是换契约**。

## 5. 复跑

```bash
cd sdtm-rag
./.venv/bin/python -m pytest -q                       # 1791 → 1792 passed / 0 failed
# 真实实现在 33 题上的表现 (非 replica):
./.venv/bin/python -c "
import json,sys,yaml; sys.path.insert(0,'.')
from server.study_lookup import StudyLookup
cat=json.load(open('data/study/st01/catalog.json',encoding='utf-8'))
qs=yaml.safe_load(open('data/study/st01/eval/test_set_events_v1.yml',encoding='utf-8'))
lk=StudyLookup(cat); tp=fp=h=0
for q in qs:
    g=set(q['expected_sources']); got=lk.resolve_events(q['question'])
    h+=any(t in g for t in got)
    for t in got: tp+=t in g; fp+=t not in g
print(h,'/33', tp+fp, f'{tp/(tp+fp)*100:.2f}%')"
# => 20 /33 50 54.00%
```

§1/§2/§3 的对照数字由 scratchpad 脚本产出 (复刻分层逻辑以便逐层归因); **§3 采纳行与
§5 的数字由真实 `resolve_events` 复核, 逐格一致** —— replica 的结论不当实现的结论用。

## 6. 给 C4 的输入 (本单元不做 C4)

- 接线前要定的 precision 门槛, 现在有了可比基准: **本通道当前上限约 54%**, 且是在
  自出尺子上。
- 若门槛定在 54% 以上, **本通道现在就不合格**, C4 应先停。
- `event_timing` 0/5 与 `event_form_assignment` 0/5 是**两个整类答不出** —— 接线不会
  改善它们, 只会把它们的噪声送进检索。
