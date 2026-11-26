# T2S S-EVT reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 4 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/AE knowledge_base/domains/DS` (含 U7 delta). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-EVT_reviewer/`
  自写脚本 (不复用 writer 的): `bscan.py` (双向逐句; KB 按行再分句, PDF 按页拼接去页脚), `speccmp.py` (pdftotext -bbox 词框按表头 x 分列, 逐变量逐字段比 spec.md), `chk.py` (定点句); 渲染 p134/135/136/139/142(200dpi 左右两半)/155/156/165/166.
- 授权范围: `git diff HEAD --stat -- knowledge_base/` 只有 AE/assumptions, AE/spec, DS/assumptions, DS/spec (全部 ∈ kb_files; narrow_files 空). examples.md 两份未动.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-EVT_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; OK 24 / DIFF 3 / UNPARSEABLE 1; cells 1805; diffs 4 (全为已登记 T-n)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 60 regress, 对 t2_fp_expected_regressions.jsonl 差集 = 0
python3 -I $S/speccmp.py $S AE 134,135,136,137 ; python3 -I $S/speccmp.py $S DS 155,156   # AE 60/60 DS 16/16 变量顺序一致; 非 CT 字段全一致
python3 -I $S/bscan.py k2p 133 142 knowledge_base/domains/AE/assumptions.md   # 111 单元, miss 3 = 结构/导航 (见签字)
python3 -I $S/bscan.py k2p 155 167 knowledge_base/domains/DS/assumptions.md   # 59 单元, miss 1 = asm 6 PDF 用 U+2011 非断连字符 (排版)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- census PDF_ONLY 落在本批页的 3 张 (p133 su.xpt §6.1.6; p154-155 pr.xpt / p155 relrec.xpt §6.2.3) 均属别节, 不计.
- fp 台账: 本批 20 个 gap/intro/词级原子用 `fp_match.norm` 直查目标文件全部命中 (ig34_p0133_a010..a018 → AE/assumptions; p0137_a010 → AE/spec; p0155_a0014..a0017, p0156_a0008/a0018, p0157_a0007/a0010/a0026 → DS/assumptions; p0156_a0007 → DS/spec).

### 页范围复核
- AE §6.2.1 = p133-142: p133 上部 su.xpt 属 §6.1.6, §6.2 引言 + §6.2.1 起于 p133 中部; p142 止于 Ex6; p143 首行即 §6.2.2 BE. 同意 writer O20 更正.
- DS §6.2.4 = p155-167: p155 上部 pr/relrec 属 §6.2.3; p167 后部 §6.2.5 HO. 同意.

### 双向全扫 — 逐页 (reviewer 自己的计数; spec 页以 speccmp 逐字段为准)
| 页 | PDF→KB | KB→PDF | 表 | 结论 |
|---|---|---|---|---|
| 133 | §6.2 标题 + 1 句 + 7 项 + §6.2.1/Description 全命中 (su.xpt 别节) | AE/asm 1-17 行全有出处; `## §6.2` 的 § 为结构 (FT/LB/NV 先例) | — | 一致 |
| 134 | 22 变量 | 22 变量逐字段 | CT: `*` 3 (AECAT/AESCAT/AEBODSYS) 渲染一致; DOMAIN `AE`/空 (U6); AEPRESP (NY)/C66742 (U5) | 一致 (U5/U6 范围外) |
| 135 | 18 变量 | 同 | `*` 3 (AEREL/AERLDEV/AEPATT); C-code 10 格 (U5) | 一致 |
| 136 | 12 变量 | 同 | `*` 3 (AERLPRT/AERLPRC/AETOXGR); C-code 8 格 (U5) | 一致 |
| 137 | 8 变量 + 脚注 + asm 1-2c | 脚注逐字; asm 逐句 | C-code 2 格 (STENRF ×2, U5) | 一致 |
| 138 | asm 2d-6: 28 句全命中 | 全有出处 | — | 一致 |
| 139 | asm 6a-7e: 列表 3 项 + CRF 表 + 叙述全命中 | `**CRF: AE Seriousness Classification**` 无 PDF 出处 (L-2) | CRF 2×2 渲染逐格 | 一致 |
| 140 | asm 7e-12 + Ex1 叙述: 33 句全命中 | 全有出处 | — | 一致 |
| 141 | Ex1-Ex4 叙述全命中 | 全有出处 | 4 表 census OK | 一致 |
| 142 | Ex4-Ex6 叙述: 仅 "related to the event" 未命中 = T-3 (KB device) | 同 | Ex4/Ex6 OK; Ex5 渲染逐格 (下) | 一致 (T-1/T-2/T-3/T-4 已登记) |
| 155 | §6.2.4 标题/Description/Spec 句全命中; CE 尾别节 | DS/asm 1-9 行全有出处 | 10 变量逐字段; DOMAIN `DS`/空 (U6); DSDECOD/DSCAT C-code (U5) | 一致 |
| 156 | 6 变量 + 脚注 + Assumptions 标题 + asm 1-2e 全命中 | 同 | DS 无 `*` 格 (渲染确认); DSSCAT/EPOCH C-code (U5) | 一致 |
| 157 | asm 2f-5: 29 句全命中 (含 3b-ii codelist / 3d / 5 “grouped) | 全有出处 | — | 一致 |
| 158 | asm 5 续-6 + Ex1 叙述全命中 (asm 6 仅 U+2011 排版差) | 原 asm 7 已删; 列表止于 6 | — | 一致 |
| 159-164 | 叙述逐句命中 (定点核 13 句, chk.py); p161 "epocch" = T-4; p164 " DG2INDG" = T-6; p160 DSDTDTC = T-3 | 全有出处 | census 全 OK | 一致 |
| 165 | 叙述全命中 | 同 | se.xpt 渲染逐格 (下); ds.xpt OK | 一致 (T-1) |
| 166 | 叙述全命中; "recieved" = T-5 | 同; examples.md:349 承载原 asm 7 的 PDF 原句 | te.xpt 渲染逐格 (下); ta/se OK | 一致 (T-2) |
| 167 | "The subject died." + ds.xpt; HO 别节 | 同 | census OK | 一致 |

### census_items 人工逐格 (渲染, 不采信 writer)
| 表 | 渲染 | 结果 |
|---|---|---|
| AE/assumptions.md:61-63 CRF (UNPARSEABLE) p139 | 90dpi | 2 行 × 2 格: Serious? / [ ] Yes [ ] No; If yes, check all that apply / [ ] Fatal [ ] Life-threatening [ ] Inpatient hospitalization… [ ] etc. — 逐格一致 (PDF 无表头, Markdown 首行充表头 = 结构) |
| AE/examples.md:79-82 Ex5 p142 | 200dpi 左右两半裁切 | 2 行 × 30 列逐格: r1 仅 AEENDTC (PDF 2014-04-26 / KB 2018-04-26, T-1: AESTDTC 2018-04-21 + AEENDY 10 自证) 不同; r2 仅 AEOUT (PDF SEQUELLAE / KB SEQUELAE, T-2) 不同; 表头首格 PDF 空 / KB Row (T-4). 其余 57 格一致 |
| DS/examples.md:292-301 se.xpt p165 | 90dpi | 8 行 × 11 列逐格一致; 表头 PDF SDSEQ / KB SESEQ (T-1) |
| DS/examples.md:342-348 te.xpt p166 | 90dpi | 4 行 × 8 列逐格一致; r3 TESTRL PDF 缺 "is" (T-2, 同表 r2 平行句自证) |

### spec.md Controlled Terms 逐变量 (bbox 分列 + layout + 渲染三法)
- **AE 60 变量**: Label/Type/Role/Core/CDISC Notes 全一致 (AERLDEV/AERLPRT/AERLPRC Notes 的 • 列表 KB 为 `*`, 仅格式).
  - PDF `*` 9 = KB `*` 9: AECAT AESCAT AEBODSYS AEREL AERLDEV AEPATT AERLPRT AERLPRC AETOXGR (p134-136 渲染逐格确认; layout `grep ' \* '` 3/3/3/0).
  - PDF 空 = KB 空 15: STUDYID USUBJID SPDEVID AESEQ AEGRPID AEREFID AESPID AETERM AEMODIFY AEACNOTH AERELNST TAETORD AESTDY AEENDY AEENTPT.
  - 字面值一致 14: MedDRA ×11 (AELLT AELLTCD AEDECOD AEPTCD AEHLT AEHLTCD AEHLGT AEHLGTCD AEBDSYCD AESOC AESOCCD); ISO 8601 datetime or interval ×2 (AESTDTC AEENDTC); ISO 8601 duration ×1 (AEDUR).
  - U6 (范围外) 1: DOMAIN `AE`/空. U5 (范围外) 21: (NY) ×13 AEPRESP AESER AESCAN AESCONG AESDISAB AESDTH AESHOSP AESLIFE AESOD AESMIE AESINTV AEUNANT AECONTRT; (LOC) AELOC; (AESEV) AESEV; (ACN) AEACN; (DEACNDEV) AEACNDEV; (OUT) AEOUT; (EPOCH) EPOCH; (STENRF) AEENRF AEENRTPT. 合计 9+15+14+1+21 = 60.
- **DS 16 变量**: 非 CT 字段全一致. PDF 无 `*` 格 (p155-156 渲染 + layout grep 0). PDF 空 = KB 空 9: STUDYID USUBJID DSSEQ DSGRPID DSREFID DSSPID DSTERM DSDY DSSTDY; ISO 8601 ×2 (DSDTC DSSTDTC) 一致; U6 1 (DOMAIN); U5 4 (DSDECOD (NCOMPLT)(PROTMLST)(OTHEVENT), DSCAT, DSSCAT, EPOCH). 合计 16.

### gaps / intros / footnote 逐项
| 项 | 位置 | 逐字 | 签字 |
|---|---|---|---|
| intro §6.2 (ig34_p0133_a010..a018) | AE/assumptions.md:3-13, H1 后、`## AE – Description/Overview` 前 (U3 host 顶部) | 句子 + 7 项逐字, 顺序同 PDF | ✔ |
| AE F (ig34_p0137_a010) | AE/spec.md:546, 最后变量块 AEENTPT 的 `---` 之后、`## Cross References` (:548) 之前 (U7) | 逐字; ¹ 上标写法同 GF/CO/LB/NV 先例 | ✔ |
| DS D (a0014/a0015) | DS/assumptions.md:3-5 | 逐字 | ✔ |
| DS S (a0016/a0017) | DS/assumptions.md:7-9 (Description 与 Assumptions 之间, CM 先例) | 逐字 (含 em dash —) | ✔ |
| DS A (a0008) | DS/assumptions.md:11 `## DS – Assumptions` (en dash 同 PDF) | 逐字 | ✔ |
| DS F (ig34_p0156_a0007) | DS/spec.md:150, DSSTDY `---` 之后、`## Cross References` (:152) 之前 (U7) | 逐字 | ✔ |

### 结构改动 / 删除 / 词级修改 逐条签字
| # | 改动 | PDF 依据 | 签字 |
|---|---|---|---|
| S-1 / D-1 | DS asm 7 整条删除 ("…transition to an AB element or follow some other defined protocol.") | p156-158 DS 列表止于 6, 其后即 `DS – Examples` (p158); "defined protocol" 在 p155-167 layout 文本 0 命中; 原句是 p166 Ex11 TA 叙述的改写 (PDF 作 "or follow-up"), 与 PDF 不符 → 无出处且矛盾, 删除合规 (非 D6). PDF 原句逐字在 DS/examples.md:349 | ✔ |
| S-2 | AE/assumptions 新增 `## §6.2 Models for Events Domains` 节 | p133 a010 标题; § 前缀同 FT/LB/NV/FA 先例 (结构行) | ✔ |
| S-3 | DS/assumptions 新增 3 个 `## DS – …` 标题 | p155 a0014/a0016, p156 a0008 | ✔ |
| W-1 (#16) | 2b "then DSCAT provides" → "then DSSCAT provides this distinction" | p156: "…then DSSCAT provides this distinction." | ✔ |
| W-2 (#17) | 3b-ii "Terminology Codelist" → "codelist" | p157: "…extensible Controlled Terminology codelist NCOMPLT." | ✔ |
| W-3 (#18) / D-2 | 3d 删 "DSTERM and" | p157: "When DSCAT = “OTHER EVENT”, DSDECOD uses sponsor terminology." | ✔ |
| W-4 (#19) | asm 5 在 grouped 前补开引号 “ (U+201C) | p157: "…summaries should be “grouped by treatment and by major reason.”" ; 新插字符照 PDF 原字符 | ✔ |
| D-4 (#2-10) | AE spec 9 处 CT 空 → `*` | p134-136 渲染 (见上) | ✔ |
| #21/#22 MOVED | 两脚注由文件末尾移到 Cross References 前 | U7 | ✔ |
- G-TB6 结构行签字: `## §6.2 …` / `## DS – Description/Overview` / `## DS – Specification` / `## DS – Assumptions` (标题); 7 项 `- ` 列表标记; 两处 `> ¹…` 引用块前缀 (PDF 文字的承载格式, 非 D6). 新增行无出处数 = 0.
- D6: 本批无新增 D6 标注, 也无应加未加 (U8: `> Class|Structure` 行与 Cross References 为导航).

### 问题表 (全部 LOW, 不阻断)
| ref | 检查项 | 问题 | 证据 / 建议 |
|---|---|---|---|
| L-1 DS/assumptions.md:43 | 排版 | 开引号补为 “, 闭引号仍为直引号 `reason."` (既有文字); 同行其余引号亦为直引号 | 既有文字排版差异归 S-TYPO (U1), 不算本批缺陷; S-TYPO 时整行统一 |
| L-2 AE/assumptions.md:59 | 导航口径 | `**CRF: AE Seriousness Classification**` PDF 无出处 (p139 表前无标签); 按 dispatch notes "表前短标签如 `**CRF:**`" 视为导航, writer 同判 | 建议主控在 auditor brief 里明示此类 "CRF: <KB 自拟名>" 标签归 U8 导航, 避免 auditor 计忠实错误 |
| L-3 S-EVT.writer.jsonl | 台账枚举 | action `DELETED` / `VERIFIED` 不在 v1.0 枚举; writer 已说明且核过无脚本按枚举取值 | 可接受; 若后续 S 批沿用, 建议在 t2s writer brief 补入枚举 |
| L-4 S-EVT.json `footnote` | 批次口径 | 字段仍写 "文件末尾", 已被 U7 覆盖 | 后续 S 批 json 模板改为 "最后变量块之后、Cross References 之前" |

### R2 recheck
- 本批 json 无 `t2_recheck[]`; 全扫未发现改写丢短语 (R2) 项. 新增 REAL_GAP 0.

### 总结
- G-TB4: census 28 表 = OK 24 + DIFF 3 (4 格, 全为已登记 T-n) + UNPARSEABLE 1 (人工逐格一致); census_items 4 表人工逐格一致 (差异仅已登记 T-n).
- G-TB6: 新增/改动 KB 行 39+/15- 全有 PDF 出处或为签字结构行; 无出处 0.
- fp_match 本批无新增回归; check_links live docs 42.
