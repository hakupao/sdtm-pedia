# ChatGPT Q9 answer — Pinnacle 21 FAIL 分类

**Verdict**: PASS+

## 6 大类常见 FAIL (ChatGPT 重新组织, 非 P21 官方分组)

| # | 类别 | 典型触发例子 | 为什么常见 |
|---|---|---|---|
| 1 | 必填/主键问题 | AE.AETERM/USUBJID 为空; 同域内记录无法唯一识别; 重复 key | Required 不能缺失; 自然键要唯一 |
| 2 | 日期时间/时序问题 | AESTDTC=20240115 (非 ISO extended); Findings 错用 LBSTDTC 而非 LBDTC; 开始晚于结束 | ISO 8601 extended; Findings 用 --DTC |
| 3 | 受控术语/字典编码 | AEPRESP='N' (应 Y 或 null); 'Severe '尾随空格; CT 大小写不符; MedDRA 不一致 | CT 值 + 大小写必须匹配 |
| 4 | Findings 结果结构 | LBORRES 有值但 LBSTRESC 空; LBSTAT='NOT DONE' 但填 LBORRES; <0.1 塞 LBSTRESN | --ORRES/--STRESC/--STRESN 配套规则; NOT DONE 固定表示 |
| 5 | 多值/非标准建模 | AELOC='FACE;NECK;CHEST' 单变量塞多值; AETERM='Headache and nausea' 不拆分 | 应用 MULTIPLE + SUPP--; 多 topic 拆记录 |
| 6 | 元数据/可追溯性 | Expected 变量未采集却不留空列不说明; 长文本截断不解释; 推导规则不写 | SDTMIG 要求说明缺失/推导/缩写/自然键 |

## 何时修 vs 何时文档化

### 优先修 (Must Fix)
1. **Required / key / uniqueness**: 必填空 / 记录无法唯一 / 父子链接错
2. **明确标准格式**: ISO 8601 错 / Findings 时间放错变量 / --TESTCD 超 8 字符
3. **CT / 字典规则**: 不在 codelist; 大小写不同语义; --PRESP/--STAT/--OCCUR 非法值
4. **建模错误**: NOT DONE 同时有结果; 多值塞单值; 应拆记录未拆

### 可保留并 Reviewers Guide 解释 (Explain and Keep)
- **A. 未采集不能靠猜补**: Expected 变量研究未采集 → 空列 + Define-XML 说明
- **B. 不能安全推断**: EPOCH 不能确定 → 置空 + Define-XML 说明 (SDTMIG 明说不要 impute EPOCH)
- **C. 技术限制合法表示**: --TEST 超 40 字符缩写 → Define-XML / Reviewers Guide 注全称
- **D. 不应伪造 NOT DONE**: CRF 无 Done/Not Done 捕获, 不应造 fake 记录
- **E. Sponsor 合理建模**: MULTIPLE + SUPP-- / sponsor-defined qualifier 入自然键 / 元素起始时间推断 → 元数据说明

## 实务判断句 (三问法)

1. **是否违反 SDTMIG 明确规则?** 是 → 修
2. **是否误导 reviewer 事实/时序/分组/编码?** 是 → 修
3. **修会否变 sponsor 臆断/伪精度/改 collected reality?** 是 → 不修, 文档化

## 落地建议: 两篮分类
- **Must Fix**: Req/key/CT/ISO 8601/NOT DONE 结构/多值误建模/链接错误
- **Explain and Keep**: 未采集空值 / 不可推断 EPOCH 时间点 / 长文本合法缩写 / sponsor 合理非常规建模

## 评分要点
- ✓ 6 大类 FAIL 分类清晰 (必填/时序/CT/Findings/多值/元数据)
- ✓ 每类 1+ 具体例子 (如 AEPRESP='N'、LBORRES vs LBSTRESN、AELOC MULTIPLE)
- ✓ Must Fix 4 小类清单
- ✓ Explain and Keep 5 小类清单 (未采集 + EPOCH不推 + 长文本 + fake NOT DONE + sponsor 建模)
- ✓ 三问法决策框架
- ✓ 两篮实务落地建议
- ✓ 坦诚标注"非 P21 官方分组"
