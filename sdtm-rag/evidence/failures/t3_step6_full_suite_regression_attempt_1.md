# Task 3 Step 6 — 全量测试回归 attempt 1 (FAIL)

## 输入

- 分支: `feat/study-workflow-events`
- 改动: `scripts/study/build_catalog.py` 按 task-3-brief.md Step 3 逐字实现
  (import 三个新 parser + guard 三段 + ledger 追加三段 + 返回 dict 新增
  `events`/`activities`/`assignments` + `main()` print 行更新);
  新建 `scripts/tests/test_catalog_workflow_pools.py` (7 个测试, 逐字照抄 brief)。
- 命令:
  ```
  cd sdtm-rag
  .venv/bin/python -m pytest -p no:warnings -q --junitxml=/tmp/j.xml >/tmp/pytest_full_t3.log 2>&1; echo "rc=$?"
  .venv/bin/python -c "
  import xml.etree.ElementTree as ET
  r=ET.parse('/tmp/j.xml').getroot(); s=r if r.tag=='testsuite' else r.find('testsuite')
  t,f,e,k=(int(s.get(x)) for x in ('tests','failures','errors','skipped'))
  print(f'tests={t} failures={f} errors={e} skipped={k} passed={t-f-e-k}')
  "
  ```

## 产物 (实测输出)

```
rc=1
tests=1713 failures=14 errors=15 skipped=0 passed=1684
```

Brief Step 6 期望: `passed=1713` (1706 + 7, tests=1713 failures=0 errors=0 skipped=0)。

29 个回归全部集中在两个既有文件, 与本任务新增的 `test_catalog_workflow_pools.py`
(7/7 全绿, 独立验证过) 无关:

```
scripts/tests/test_build_catalog.py — 14 FAILED
  test_build_catalog_core / test_ledger_full_coverage / test_write_catalog_outputs /
  test_ledger_per_sheet_counts / test_unknown_field_type_raises / test_trailer_rows_in_ledger /
  test_no_old_report_degrades / test_diff_ignores_export_artifacts / test_diff_keeps_real_changes /
  test_diff_text_preserves_raw / test_normalization_does_not_touch_new_removed /
  test_catalog_stores_raw_values / test_footnote_form_row_still_trailer / test_diff_available_flag

scripts/tests/test_build_field_cards.py — 15 ERROR (全部 fixture setup 阶段)
  test_render_field_card_content / test_render_field_card_fallbacks / test_render_visibility_v2_parts /
  test_render_hidden_activity_row / test_render_always_visible / test_render_strips_newlines /
  test_render_strips_newlines_in_diff / test_build_cards_files_and_index / test_build_cards_forms_filter /
  test_build_cards_idempotent_purges_stale / test_render_diff_unavailable_says_not_compared /
  test_build_cards_passes_diff_available / test_build_cards_defaults_diff_available_true /
  test_rendered_card_unit_has_no_html / test_rendered_codelist_entries_have_no_html
```

单个用例的完整 traceback (`test_build_catalog_core`, 其余 28 个同一根因):

```
scripts/study/build_catalog.py:92: in build_catalog
    all_events = parse_events(sp.config_report_new)
scripts/study/parse_config_report.py:239: in parse_events
    for r in _read(path, "Study workflow-Events", has_section_row=True):
scripts/study/parse_config_report.py:227: in _read
    return read_sheet_records(wb[sheet], has_section_row=has_section_row)
.venv/lib/python3.14/site-packages/openpyxl/workbook/workbook.py:287: KeyError
E       KeyError: 'Worksheet Study workflow-Events does not exist.'
```

## 技术判定

**根因单一, 已定位**: `scripts/tests/study_fixtures.py::build_config_report()` 只合成
`Forms` / `Items and Groups` / `Code lists` 三个 sheet (预留于 Task 2 之前, 未跟进 workflow 三表)。
`test_build_catalog.py` 与 `test_build_field_cards.py` 的 `sp`/`catalog` fixture 都经它构造
一个不含 `Study workflow-{Events,Activities,Forms}` 的合成 xlsx, 再传给 `build_catalog(sp)`。

Task 3 按 brief Step 3 逐字实现后, `build_catalog` 对 `sp.config_report_new` **无条件**调用
`parse_events` / `parse_activities` / `parse_form_assignments` (对齐 brief 原文, 未加任何
"sheet 是否存在"判断)。这三个 parser 内部用 `wb[sheet_name]` 直接取表, 表不存在直接抛
`KeyError`(openpyxl 原生行为, 非本任务新写代码)。凡是经 `build_config_report()` 构造
fixture 的用例, 一律在 `build_catalog()` 第一行新增代码处炸掉。

**验证**: 本任务新建的 `test_catalog_workflow_pools.py` 用的是 `resolve_study("st01")`
(磁盘上的真实 ConfigReport, 含全部 workflow sheet), 7/7 全绿, 与本回归无关 —— 已单独
`pytest scripts/tests/test_catalog_workflow_pools.py -q` 确认 (`7 passed`)。

**根因不在本任务新写的 parser 调用逻辑或 guard 逻辑本身** —— 三道验收闸 (§5.A/B/C) 与
Step 5 台账 diff (`ledger: 3508 -> 3717`, 既有池逐字未动) 全部按 brief 预期实测通过,
证明 `build_catalog.py` 对真实数据的新增逻辑是对的。破坏面是**两个既有测试文件依赖的合成
fixture 缺三张 sheet**, 是 Task 3 brief 未预料到的既有测试基建缺口。

## 业务判定

**FAIL** (相对 brief Step 6 期望 `passed=1713 failures=0 errors=0`)。

brief 未声明 `test_build_catalog.py` / `test_build_field_cards.py` 或
`scripts/tests/study_fixtures.py` 在改动文件清单内 (`Files:` 段只列
`scripts/study/build_catalog.py` 与新建的 `test_catalog_workflow_pools.py`)。修复此回归
需要以下两条路线之一, 均超出 brief 授权范围 / 需要架构判断, 不属于"照抄 brief 就能做"
的工作:

- **方案 A (fixture 补全)**: 给 `study_fixtures.py::build_config_report()` 增加合成的
  `Study workflow-{Events,Activities,Forms}` 三个 sheet (含 header/脚注行), 使既有 fixture
  重新自洽。但这会连带改变 `test_build_catalog.py::test_ledger_per_sheet_counts` 里硬编码
  的 `per_sheet == {"Forms": 2, "Items and Groups": 4, "Code lists": 3}` (需要新增三个键),
  以及可能牵动 `test_ledger_full_coverage` / `test_write_catalog_outputs` 等对 ledger 行数
  的隐含假设 —— 即需要连带修改 brief 未列出的既有测试文件的断言内容, 而非只加新 sheet。
- **方案 B (build_catalog 优雅降级)**: 仿照 `sp.config_report_old is None` 的既有降级模式
  (行 84-90), 给三个新 parser 调用加"目标 sheet 是否存在于 workbook"判断, 不存在则视为
  三池为空 (`events=[] activities=[] assignments=[]`), 不抛异常。这是对 brief Step 3 代码
  的**修改**(brief 原文是无条件调用, 明确写了"逐字"), 且需要确认这不会掩盖真实生产数据
  里 sheet 缺失的情况 (真实 st01 数据这三个 sheet 恒在, 若未来某个 study 真的没有这三个
  workflow sheet, 静默返回空池是否是期望行为需要产品判断)。

两条路线都要求对 brief 未列出的文件做出设计决策, 已触及"判据先于数据"边界 ——
**不擅自选择方案并动手, 停下来报告**。

## 下一 attempt 输入

等待控制方 (main/team-lead) 裁决方案 A / B / 其他, 明确后再继续:
- Step 6 (全量测试) 与 Step 7 (提交) 均未执行 (当前工作区含未提交的 build_catalog.py +
  test_catalog_workflow_pools.py 改动, 未 `git add`/`git commit`)。
- 三道验收闸 (§5.A/B/C) 与 Step 5 台账核对已经通过, 不需要重做; 复跑本任务新增测试
  只需 `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_catalog_workflow_pools.py -p no:warnings -q`。

## 控制方裁决 (attempt 2 输入)

**方案 A(补 fixture 三个 sheet)。明确否决方案 B。**

否决 B 的理由 (控制方原话摘录):
1. B 是静默降级 —— 本仓反复吃亏的模式 (C1 `embed_texts` 截断先例); `build_catalog`
   现有 Forms/Items 两处 guard 存在的全部意义就是"不能静默归为脚注", `KeyError` 是它
   在正常工作。
2. 若真实 ConfigReport 哪天缺 workflow sheet, B 会让下游 `collect_scope` 算出"空而合理"
   的采集范围 —— 看着正常、全是错的 (Task 2 审查警告过的失败模式: 结构检查 ≠ 语义检查)。
3. B 是为了迁就测试夹具去改生产行为, 方向反了。fixture 是"真实 ConfigReport 的合成模型";
   真实的有 7 个 sheet, fixture 只造了 3 个 —— 这是**夹具的缺陷**, 该修的是夹具。

执行要求 (摘录): 给 `study_fixtures.py` 补三个 sheet (结构照 `parse_config_report.py`
实际消费的列, 表头行数对齐 `has_section_row`), 全部 `偽` 前缀零真名, 每个 sheet 至少 1 条
脚注行, 保持引用完整性; 既有断言只许加强 (原有 3 个 sheet 的期望计数一个都不许改, 只能
新增三个 workflow sheet 的期望条数), 若某条既有断言不得不改数值才能过则停下报告;
收尾判据改为 `failures=0 且 errors=0` 硬性, `tests` 总数如实报告(不为了凑数删测试)。

见 `task-3-report.md` attempt 2 段落记录实际执行结果 (`test_ledger_per_sheet_counts` 与
`test_trailer_rows_in_ledger` 两条既有断言按"只许加强"原则更新, 均在报告里逐条列出)。
