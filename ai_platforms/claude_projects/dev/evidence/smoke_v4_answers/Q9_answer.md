# Claude Q9 answer — Pinnacle 21 FAIL 分类

**Verdict**: PASS+ (带明确边界声明)

## 边界声明
Claude 坦诚: "此问题涉及 P21 验证实践 + FDA 审查流程, 超 Project KB 覆盖范围. 以下基于行业通用经验; 具体 Rule ID 以 P21 官方 Validator Engine Rules 当前版本为准 (ID 示意居多, 版本可能位移)"

## 6 大 FAIL 类别 + Rule ID

| # | 类别 | Rule ID (示意) | 触发例子 |
|---|---|---|---|
| 1 | CT 违规 | SD1011/SD0065 | VS.VSTESTCD="BPSYS" 不在 C66741 (应 SYSBP) |
| 2 | Required/Expected 缺失 | SD0006/SD0005 | AE.AEDECOD Core=Req 为空 (MedDRA 未回填) |
| 3 | 重复/Key 唯一性 | SD1001/SD0083 | 同 USUBJID+LBTESTCD+LBDTC+LBCAT 2 条; --SEQ 重复 |
| 4 | ISO 8601 格式 | SD0007/SD0061 | AESTDTC="15JAN2024" 应 "2024-01-15"; EXDUR="7 days" 应 "P7D" |
| 5 | 跨域引用完整性 | SD0081/SD0003 | AE.USUBJID 在 DM 不存在 (orphan); VISITNUM 在 TV 未定义; EPOCH 落 SE 边界外 |
| 6 | Metadata/Define.xml | SD1021/DD0001 | 定义 $200 实际 max 45 (应截); Define.xml 声明 dataset 未提交; Label 不符 IG |

补充第 7 类: Timing 逻辑冲突 (EXSTDTC < RFSTDTC, AESTDTC > AEENDTC)

## 修 vs. 文档化 三级决策矩阵

### ✅ 应修 (Fix)
- 真实数据质量问题: 日期笔误/编码未跑/单位 mismatch/pipeline bug
- Core=Req 空值 (几乎无例外)
- 格式/大小写: ISO 8601, C66742 NY 只接受 Y/N 大写
- Orphan records (子表 USUBJID 不在 DM)
- Variable length 超实际 max (零成本修)
- Timing 逻辑冲突源于数据错

### 📝 应文档化 (cSDRG 解释保留)
- **合理 CT extension**: sponsor 扩 Extensible codelist (如自定义 LBTESTCD), P21 不识别 → cSDRG CT 节列清单+版本
- **Dictionary 版本 mismatch**: 研究用 MedDRA 27.0 但 P21 内置 26.1 (非数据问题)
- **Protocol-driven 合理异常**: 方案允许 unscheduled visit, emergency unblind 前 AE
- **Legacy/retro-conversion**: 历史字段无法补齐 (旧 RACE 粒度粗)
- **P21 rule 误报/版本 gap**: rule 对新 IG 解读滞后, Trial Design 判定过严
- **刻意保留 Warning/Notice** 经业务判断无风险
- Timing 冲突源自 protocol 设计 (run-in 期事件早于 RFSTDTC)

### 🚫 绝不能仅文档化 — **FDA Technical Rejection Criteria (TRC), 自动拒收**
- DM 缺 USUBJID/STUDYID
- 核心域 (DM/EX/AE/LB) 整域缺失或空
- Define.xml 缺失/无效/与 dataset 结构不符
- SDTM 与 ADaM / CRF annotations 关键一致性断裂

**TRC 级必修, cSDRG 无法豁免**.

## 操作原则
- **Error** → 逐条判 Fix vs Explain; TRC 级必修
- **Warning** → ≥90% 应 fix 或 justify, 不可无视
- **Notice** → 系统性 pattern 一笔带过, 零散可忽略
- **cSDRG** 每条保留 issue 需列: Rule ID / Dataset / Variable / # of records / 理由, 计数与 P21 报告一致
- Fix 后 re-validate, 防引入新 issue

## 源溯源
- Project 内: 06_assumptions.md (ch04 是 P21 rule upstream: ISO 8601 §4.4, CT §4.1.5, Req/Exp §4.1.1), 03_model.md (Core 定义)
- Project 外: P21 Validator Engine Rules 官方文档, FDA Study Data Technical Conformance Guide (TCG), **FDA Technical Rejection Criteria for Study Data**

## 评分要点
- ✓ 6 类 FAIL + Rule ID 示意 + 具体变量值触发例
- ✓ 补第 7 类 Timing 逻辑冲突
- ✓ 三级决策 (Fix / Explain / **TRC 必修**) — 比 ChatGPT 多 TRC 层
- ✓ TRC 具体 4 项清单 (DM 缺 key / 核心域空 / Define.xml 失效 / 跨数据集断裂)
- ✓ E/W/N 操作百分比原则 (≥90%)
- ✓ cSDRG 每条 issue 5 字段清单
- ✓ MedDRA 版本 mismatch (27.0 vs P21 26.1) 具体例
- ✓ **边界声明**: 超 KB 范围, Rule ID 示意 — 优于 ChatGPT 未明确
