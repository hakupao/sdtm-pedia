# Q11 (F1 — Dataset-JSON v1.1 vs XPT v5) ChatGPT 专属

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83e5c-c2e4-83a5-a12c-3b545c698994
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 1m 43s

## 完整回答 (要点摘录)

### (a) Dataset-JSON 相比 SAS XPT v5 主要 4 个技术痛点

1. **解除老旧 transport 格式带来的长度/命名约束** — XPT 因 SAS V5 transport 限制: --TEST 限制 40 字符, --TESTCD/QNAM 受 8 字符思维影响; Dataset-JSON 把数据交换载体从老旧二进制约束解放, 减少为格式做的截断/拆分/缩写
2. **改善长文本表达** — XPT 超过 200 字符必须拆到 SUPP-- (载体格式逼着拆, 不是业务需要); JSON 文本序列化更适合原样承载长字符串
3. **降低大文件低效问题** — 超大 transport 文件已成监管处理瓶颈, 主因是 sponsor 把字符变量一律开 200; Dataset-JSON 避免 padding/固定宽度思维, 文件更适合现代系统处理/比较/压缩/自动化
4. **减少对 SAS 专有历史实现细节依赖** — XPT 是非常老的 SAS 传输格式, 现代非 SAS 工具链解析/生成/校验都带兼容遗产; Dataset-JSON 接近现代通用结构

### (b) 2026 年现状

**截至 2025-08 的最佳判断 (诚实未实时核验)**:
- FDA 正式、通用、生产性接受的主格式仍是 **SAS XPT v5**
- Dataset-JSON 属于**试点/过渡性接受**场景, 不应视为已全面替代
- 实务最安全答案: 正式申报主交付仍是 XPT + Define-XML; Dataset-JSON 仅在 FDA 试点范围或明确允许时并行

模型主动声明无法联网核对 FDA 2026 最新页面, 保留不确定性.

### (c) SDTM 程师实操建议 (4 步)

1. **开发环境**: 双轨制 — 内部主表示 dataframe/parquet/dataset-json-ready structure; 对外受监管交付物稳定生成 .xpt
2. **归档**: 保留 3 层 — canonical tabulation source / submission render (实际提交 XPT) / metadata package (Define-XML + aCRF + cSDRG + 验证报告). Dataset-JSON 可作内部归档/回归/试点副本, 但不能成唯一归档
3. **提交**: 当前默认 XPT + Define-XML; Dataset-JSON 仅试点/获准场景并行
4. **验证**: 现在就做 XPT 与 Dataset-JSON 一致性回归 (row count / 主键 / null pattern / CT / sort/order / Define-XML 一致), 监管接受范围扩大时切换成本低

**一句话总结**: 现在不要"等 FDA 完全切换后再准备", 应该是**现在内部就支持 Dataset-JSON, 但外部正式交付仍以 XPT 为准**.

### (d) Define-XML 和 Dataset-JSON 互补关系

- **Define-XML = 说明书 / 元数据合同**: 描述哪些 dataset 被提交 / 结构/purpose/location/key / CT / origin / value-level metadata
- **Dataset-JSON = 数据载体 / 数据包**: 承载行/列/值, 把 XPT 历史格式问题降下来, 但不等于完整监管元数据说明
- **关系不是替代, 而是分工**:
  - Dataset-JSON: 把"数据本身"送过去
  - Define-XML: 告诉审评者"这些数据是什么 / 怎么来的 / 怎么解释 / 键是什么 / CT 是什么 / 哪些是 derived/assigned/CRF collected"
- **不能只靠 Dataset-JSON**: 监管解释依赖 Define-XML 的 origin/CT/value-level metadata

## 判据对齐

- (a) **4 个痛点全中** ✓ (8 字符变量名约束 / 200 字符限制 / 存储低效 / SAS 专有依赖); 未明列 Unicode/数据类型有限, 但已达 4 项最低要求
- (b) **XPT 仍是 FDA 必需** ✓; 诚实声明无法实时核验 FDA 2026 最新状态 ✓
- (c) 实操 4 步 (开发/归档/提交/验证) ✓; 双轨/3 层归档/Dataset-JSON 仅试点 ✓
- (d) Define-XML 元数据合同 vs Dataset-JSON 数据载体, 互补不替代 ✓
- bonus: "现在内部支持 Dataset-JSON 但外部仍交 XPT" 一句话总结非 trivial ✓
- bonus: 一致性回归清单 (row/key/null/CT/sort/Define-XML) 有可操作性 ✓

源溯源命中:
- `knowledge_base/chapters/ch03_submitting_data.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`

## 归因

PASS — Pure generalization (KB 0 直接 Dataset-JSON 文档). 4 痛点 + 实操 4 步 + 互补关系全到位. **诚实声明 FDA 2026 状态无法实时核验**是非 trivial 加分项 (没瞎编 binding 接受范围). 双轨开发环境 + 3 层归档 + 一致性回归清单具备可操作性. 思考时长 1m 43s 合理.
