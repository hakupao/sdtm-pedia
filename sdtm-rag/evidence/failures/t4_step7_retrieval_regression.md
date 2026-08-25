# Task 4 Step 7 — 检索侧回归 (FAIL, S3 触发, 用户裁定退回)

## 输入

- 分支: `feat/study-workflow-events`
- 改动: task-4-brief.md 的完整实现 (`collect_scope` 推导 + `render_field_card` 新增
  `- 収集アクティビティ:` 行 + `build_cards` 调用处传 `assignments=catalog.get("assignments", [])`)。
- Step 1-6 (单测 22/22、959 卡回归闸 0 非预期) 全部按 brief 通过, 完整记录见
  `.superpowers/sdd/2026-08-25-study-workflow-events/task-4-report.md` ——
  **该路径 gitignored, 不入库**, 是本轮 SDD 工作稿, clone 者看不到; 本文件 (归档,
  规则 B) 才是随 git 走的永久记录, 关键数字均已复制进本文件, 不依赖那份工作稿。
- Step 7 重灌索引由**用户亲手**执行 (launchctl 权限被 Bash 沙箱 auto-mode classifier
  拒绝, 见下方"权限阻塞"小节), 重灌后 `study_st01`: 959 field card + `study_st01_docs`:
  114 doc chunk。
- 命令 (与既有 study golden v2 基线同形态):
  ```bash
  cd sdtm-rag
  for i in 1 2 3; do
    .venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
      --retrieval-only --hybrid --study-lookup \
      --collection study_st01 --kb-root data/study/st01/cards \
      --output /tmp/t4_run_$i.json
  done
  ```

## 产物 (实测输出)

- 三遍逐题完全稳定 (非 flaky, 确定性检索)。
- **overall = 84.38% (0.8438)**, 对照冻结基线 `data/study/st01/eval/runs/v2_baseline_s2on.json`
  的 **87.50%**。
- 逐题差异 (48 题中 2 题)。**以下全文用代号指代真实 OID** (真名↔代号映射不入 git;
  论证价值全在簇大小/排名/相似度差值/覆盖率这些计数, 不依赖真名本身, 见 C1 修复记录):

  | id | baseline | new | detail |
  |---|---|---|---|
  | st01_v2_q14 | 1.0 | **0.0** | expected 卡代号 `Q14-expected`; source_hits=[]; 完全跌出 top_k |
  | st01_v2_q21 | 1.0 | **0.5** | expected 两卡代号 `[Q21-expected, Q21-hit]`; 命中 Q21-hit, 未命中 Q21-expected |

## 权限阻塞 (过程记录, 与本次 FAIL 判定无因果, 供流程复盘)

Step 7 要求先停 `com.sdtmrag.api` (launchd) 再重灌, 原因: `ingest_study` 用
`delete_collection()` 删除后重建, 而 `server/rag.py` lifespan 启动时持有旧句柄,
边跑边灌会让线上句柄指向已删除的 collection。`launchctl bootout` 被 Bash 沙箱的
auto-mode classifier 拒绝 (团队 lead 独立复现同样被拒), 判定为需要真人介入的
outward-facing 操作, 未尝试任何绕过 (kill/编辑 plist 等), 交由用户亲手执行停/灌/起
四条命令。服务在整个等待期间保持 `health=200` 不受影响 (重灌前旧标签 `適用範囲`
943 处 / 新标签 `非表示アクティビティ` 0 处, 与 brief 断言吻合)。

## 技术判定 —— 归因实验 (三臂设计, 判读规则先写死后测)

**设计**: BASE (Task 1 之前, 冻结基线) / A (只含 Task 1 标签重命名, 无 収集アクティビティ
行) / AB (当前生产态, 两处改动都有, 即上面的 84.38%)。

**判读规则 (跑之前写死)**:
- A ≈ 87.50% 且逐题 Δ0 ⇒ 致害全部来自 Task 4 的新增行
- A ≈ 84.38% (q14/q21 同样回归) ⇒ 致害来自 Task 1 的标签重命名
- A 落在中间 ⇒ 两者各有贡献

**如何跑 A 臂而不碰生产** (硬约束: 不许碰 `study_st01` / launchd / `data/study/st01/cards/`):
1. 一次性脚本调用未改动的 `render_field_card`/`_write_index`, 对每张卡强制
   `assignments=None` (等价 Task 4 之前的调用形态), 渲染到 `/tmp/cards_arm_a/`。
   自检: 959 卡, 0 张含 `収集アクティビティ`, 231 张含 `非表示アクティビティ`,
   文件名集合与备份基线一致。
2. 复用 `ingest_study.py` 的 `load_cards`/`embed_texts`/`persist_study` (同一 embedding
   模型 `text-embedding-3-small`, 与生产参数一致, 可比), 灌进**新建**的临时 collection
   `study_st01_armA` (与 `study_st01` 同一 chroma_dir, 但独立 collection 名 —— `run_eval.py`
   的 `chroma_dir` 固定读 `settings.chroma_dir`, `--kb-root` 只影响 kb_root 元数据不影响
   连接目标, 故 A 臂必须落在同一物理目录下的另一个 collection 才能被 `--collection` 切换
   到)。
3. 用与 AB 臂完全相同的评测命令, 只把 `--collection`/`--kb-root` 换成临时的, 跑三遍。
4. 完成后立即 `delete_collection("study_st01_armA")` 清理, 复核 `study_st01` 计数仍为 959、
   服务仍 `health=200`。

**A 臂结果**:
- 三遍逐题稳定 ✓ (n=48)
- **overall = 87.50% (0.8750)**
- 与 BASE 逐题差异 = **0 题**

**按写死的判读规则**: A ≈ 87.50% 且逐题 Δ0 ⇒ **致害全部来自 Task 4 的新增行**, Task 1
的标签重命名 (`適用範囲` → `非表示アクティビティ`, 语义修正) 无责。

### D1 — q14/q21 完整 top15 排名对比 (只读查询, 未写入)

用与 `run_eval` 相同的 `RAGEngine` 构造 (`hybrid_enabled=True` + `StudyLookup`,
`top_k=15`), 对 ArmA collection 与生产 `study_st01` collection (只读 `.retrieve()`,
不做任何写操作) 直接查询两题原文, 打印完整 top15:

**st01_v2_q14** (expected 卡代号 `Q14-expected`):
- ArmA: Q14-expected 在 **rank 15/15** (sim 0.4319) —— 本就压线
- AB(生产): Q14-expected **完全跌出 top15**; 顶替它挤进列表的是同 form 内另一张卡
  (代号 `Q14-competitor`, sim 0.4321, 与 Q14-expected 原本的 0.4319 相差仅 **0.0002**)

**st01_v2_q21** (expected 卡代号 `Q21-expected`):
- ArmA: Q21-expected 在 **rank 15/15** (sim 0.5616) —— 同样压线
- AB(生产): Q21-expected **完全跌出 top15**

**同质簇验证 (决定性证据 —— 同簇兄弟卡与 expected 卡共享该行逐字文本)**:
- q14: `Q14-expected` 与 `Q14-sibling-1`/`Q14-sibling-2`/`Q14-sibling-3`/`Q14-sibling-4`/
  `Q14-sibling-5` 在该题 top15 命中范围内共 6 张卡, `収集アクティビティ` 的值 (2 个
  activity OID 拼接的字符串) **逐字相同**; 该取值的**全局同取值簇** = 35 张卡
  (不止 top15 内这 6 张; `Q14-competitor` 不在此簇内, 取值不同)
- q21: `Q21-expected` 与 `Q21-hit`/`Q21-sibling-1`/`Q21-sibling-2`/`Q21-sibling-3`/
  `Q21-sibling-4`/`Q21-sibling-5`/`Q21-sibling-6` 在该题 top15 命中范围内共 8 张卡,
  `収集アクティビティ` 的值 (单个 activity OID) **逐字相同**; 该取值的**全局同取值簇**
  = 73 张卡

结论: 回归不是"大幅错位", 是**同质簇稀释了 expected 卡本就贴线的相对区分度, 把它从
rank 15 推下检索窗口**——两题的 expected 卡与簇内多张兄弟卡共享大段逐字文本, 该维度上
彼此的相似度差距被系统性拉近, 原本就压线的排名因此进一步下滑; 顶替它跌入 top15
最后一位的是排序中紧邻的下一张卡, **不必然属于该簇** (q14 的顶替者 `Q14-competitor`
已确认不在簇内, 取值不同, 见上文)。

### D2 — 959 卡去重同质性量化

- 959 张卡 → `収集アクティビティ` **仅 46 种不同取值**
- **最大簇 175 卡 (18.2%) 逐字相同** (代号 `cluster-γ`, 单个 activity OID; 与
  q14/q21 两题的挤占竞争者无关, 单独作为"同质性有多极端"的量化例证)
- 簇大小分布严重右偏: **size≥30 的簇有 11 个, 合计覆盖 683 卡 (占全部 71%)**;
  size=1 的独有取值只有 6 个

### 假设验证

团队 lead 的先验假设 (跑数据前写下, 非事后编造): "新增行在同 form 内逐字相同, 给全部
959 卡引入了共享的 activity-OID 词汇 —— `crowding_and_gold_integrity.md` 记录过的
同质簇挤占机制的又一实例"。**D1 + D2 证实, 未被推翻**: 机制不是"全局都变差"(Δ0 覆盖
46/48 题), 而是精确命中了已经贴着 top-k 截止线的边缘题, 顶替者是共享该行文本的同簇卡。

## 业务判定

**FAIL** (相对 brief Step 7 冻结判据: overall 与基线 87.50% 一致 + 逐题 Δ0)。

按 brief 与团队 lead 的明确指令, **未做任何修复尝试, 未自判"影响不大", 未提交**,
仅完成归因实验并上报。

**用户裁定**: 执行 spec §6 S3。

- **回退 Task 4 的卡片渲染** —— 生产卡片不再输出 `- 収集アクティビティ:` 行。
- **保留 Task 1 的标签修复** (`非表示アクティビティ`) —— 归因已证明它逐题 Δ0, 无责。
- **保留 `collect_scope` 推导与其单测** —— spec §2.3 仍在 in-scope, 数据留在
  catalog 三池, 由 Task 6 的 `study_lookup` 直查交付; 只是不进向量库。
- 依据: spec §2 Out of scope 早已写明"事件层进向量库切 chunk (增量是关系型, 走确定性
  通道) 不做"。这次回归是违反自家原则的可预期后果, 退回不是退却, 是回到原则。

## 下一 attempt 输入 (S3 执行记录)

1. `build_cards` 内 `render_field_card` 调用处的 `assignments=catalog.get("assignments", [])`
   改回 `assignments=None`, 附醒目注释 (裁定日期/实测数字/机制/归因/指针, 见
   `scripts/study/build_field_cards.py` 对应处)。**不删** `render_field_card` 的
   `assignments` 形参, **不删** `collect_scope` 函数。
2. 测试: `collect_scope` 两条单测 + `test_render_collect_scope_row` 原样保留 (推导本身
   与"传 assignments 就渲染"的行为均未被否定); 新增 `test_build_cards_omits_collect_scope_row`
   作为本次裁定的守门人 (断言生产 `build_cards()` 路径渲染出的卡不含该字符串), 防止未来
   被"顺手"改回而无人察觉。`scripts/tests/test_build_field_cards.py`: 23/23 通过。
3. 重渲染 959 张卡, 自检: 0 张含 `収集アクティビティ` / 231 张含 `非表示アクティビティ` /
   0 张残留旧标签 `適用範囲`; 与 `/tmp/cards_arm_a/` 逐文件 `diff -rq` **完全一致**。
4. 全量测试: `tests=1721 failures=0 errors=0 skipped=0 passed=1721`。
5. 重灌索引 (需用户亲手跑, 同样的 launchctl 权限阻塞) + 三遍评测复核回到 87.50% 逐题
   Δ0, 通过后与本轮改动一起提交 —— 完整过程见工作稿 (gitignored, 不入库, 路径同上)。
