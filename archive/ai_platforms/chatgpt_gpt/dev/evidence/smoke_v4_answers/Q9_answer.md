# ChatGPT GPTs — Q9 Pinnacle 21 常见 FAIL 分类 + Fix vs SDRG (V5C post-apply v2.2 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead7dc-27f0-83a5-9d5e-75572069ea3c
> **题类**: Q9 (E1 — Pinnacle 21 issue 分类)

## Raw (DOM readback, trimmed)

**结论**: P21 FAIL 先当 "审查风险提示", 不是所有都机械修数据. 违反 SDTMIG/CT/Define-XML 或影响 reviewer 使用 → 修; 数据忠实反映方案/CRF/医学事实, SDTMIG 允许 → cSDRG 保留并解释.

**注**: P21 rule ID/Severity 随 validator/rule package/config 变化; 下按问题类型归纳.

### 常见 6 大类 P21 FAIL

| 类别 | 常见 Severity | 典型触发例子 | 处理 |
|---|---|---|---|
| 1. 结构/Define-XML/元数据不一致 | Error/Warning | ae.xpt 有 AETOXGR 但 Define-XML 未声明; 空数据集提交; 变量顺序/label/type/length 与 Define 不一致 | 修元数据或数据 |
| 2. Required/Core 变量缺失或关键变量为空 | Error | AE.AETERM/AEDECOD 空; STUDYID/DOMAIN/USUBJID/--SEQ 缺失 | 通常必须修 |
| 3. CT/字典/大小写 | Error/Warning | AESER="YES" 而非 Y; AESEV="Severe" 非 SEVERE; LBSTRESU 非 UCUM; MedDRA/WHO Drug 版本未在 Define 外部 codelist 声明 | Non-Ext: 修; Ext+合理依据: Define/cSDRG 说明 |
| 4. 日期/时间/Study Day | Error/Warning | AESTDTC="20240301" 非 ISO 8601; --ENDTC < --STDTC; AESTDY 算错 | 格式错: 修; 部分/未知/ongoing: ISO 合规 + cSDRG 说明 |
| 5. Key/唯一性/关联完整性 | Error/Warning | AESEQ 重复; RELREC 指 AESEQ=99 但 AE 无此记录; SUPPAE IDVAR 回连失败 | 断链/重复: 修; legit many-to-many: 保留+解释 |
| 6. 跨域/业务规则/方案设计 | Warning/Notice/Error | DM.ARMCD 不在 TA; EPOCH 机械 impute; --STAT="NOT DONE" 同时有结果; VISIT/VISITNUM 与 TV/SV 异常 | 映射错: 修; 反映真实 deviation/unplanned: cSDRG |

### 什么时候修数据

建议修:
1. 违反硬性 SDTM/SDTMIG/CT/XPT/Define 规则
2. 映射或派生明显错误
3. 影响 reviewer 连接/筛选/复现 (RELREC/SUPP-- 断链)
4. 可从 source data 或 aCRF 纠正, 不改变临床事实

**原则**: 能修成更合规、更可追溯、且不伪造信息的, 就修.

### 什么时候 cSDRG 保留不修

保留+解释:
1. 数据真实反映 CRF/EDC/实验室/医学事实 (访视窗口外/非计划访视)
2. SDTMIG 允许但 P21 规则保守 (EPOCH 无法可靠判断时应空, 不要硬填)
3. 缺失是研究未收集或不适用 (Expected 可空)
4. 部分/未知日期是源数据事实 (不为消除 FAIL 补假日期)
5. Sponsor-defined / extensible CT 有合理依据, Define-XML 已声明
6. 规则不适配研究设计 (adaptive / basket trial / legacy)

### Reviewers Guide 推荐写什么

| 字段 | 内容 |
|---|---|
| P21 issue | Rule ID / message / severity / validator version |
| Scope | 域、变量、记录数、受影响 subjects |
| Root cause | 方案设计 / 源未收集 / 真实偏差 / CT 扩展 / partial date / legacy |
| Why not fixed | 修会造成不真实/不可追溯/违反 SDTMIG 表达原则 |
| Reviewer impact | 是否影响关键安全/疗效, 如何解释或筛选 |
| References | Define-XML comments / aCRF 页 / SAP / protocol / derivation |

**一句话**: Error 多数应修; Warning 判断临床/标准合理性; Notice 提醒/透明化. **不要为 "0 FAIL" 而改坏数据**, FDA reviewer 更关心数据标准/真实/可解释/可追溯.

**源路径**: `<!-- ch03_submitting_data.md -->` + `<!-- ch04_general_assumptions.md -->` + `<!-- ch08_representing_relationships.md -->`

## Self-score verdict

- **Verdict**: **PASS** (answer depth approaches PASS+)
- **对照 PASS 判据** (必含 5 大类, 合理即 PASS):
  - 1. Date consistency (--ENDTC < --STDTC) ✓ 类 4
  - 2. CT compliance (AESEV="SEV" 或 AESER="YES") ✓ 类 3
  - 3. Required/Expected 缺失 (AETERM/AEDECOD 空) ✓ 类 2
  - 4. Duplicate records (AESEQ 重复) ✓ 类 5
  - 5. Orig vs Std / numeric vs character 类型 (LBSTRESU 非 UCUM) ✓ 类 3
  - 6. Value-level consistency (--STAT="NOT DONE" 同时有结果) ✓ 类 6
  - 应修 vs 文档化原则: 真实数据错 → 修; 标准不匹配但真实 → SDRG ✓
- **触发 FAIL?** 无 (列 6 类 > 3 要求; Error/Warning/Notice 未混; 未说"所有 FAIL 必修"; 未给虚构 rule ID)
- **加分**:
  - Reviewers Guide 6 字段模板 (超预期)
  - "不要为 0 FAIL 改坏数据" 原则 (深入)
  - EPOCH 不 impute + part date 不补假日期 (精确避免 anti-pattern)
- **v5c→v2.2 delta**: 无 regression
