# T2S S-SPEC2 reviewer — attempt 1

> 2026-11-26, oh-my-claudecode:code-reviewer (opus). Brief `t2s_scan_review_audit_v1.0.md` Reviewer 段 + `t2_reviewer_v1.0.md` / common brief / dispatch notes (含 T2S 段 + S-SPEC2 教训) / U1-U8 / T1 ack.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC2_reviewer/` (lay.py / cmp.py / bag2.py / ord.py / tbl.py / kbx.py / xl.py; 渲染 pNNN-NNN.png 80dpi 全 17 页, ctNNN-NNN.png 110dpi 左半页裁图). 只读 KB, 未 stash/checkout/commit.

## Verdict: **PASS**

## 方法 (独立于 writer 的 sc2.py / bbox)
1. **PDF 侧独立解析** `lay.py`: 读 `work/pdf_pages/ig34_pNNNN.txt` (pdftotext **-layout**, 非 bbox); 每页取最后一个 `Variable  Variable Label` 表头的字符列位置分列; 行起点 = 行首 ≤2 空格 + 全大写变量名; 首页从 `XX – Specification` 起 (BS 从 p196 `BS – Specification` 即 :39 之后, 前半页 §6.3.5.1 通用表不计), 止于 `In this column` / `©` / `XX – ` 标题; 无表头续页 (p179) 沿用前页列界; 跨页续行并入上一行.
2. **逐变量三重比对** (195 变量): (a) `bag2.py` 每行全部 PDF 词 (全列) vs KB 7 字段词袋; (b) `cmp.py` 逐列 (Label/Type/Role/CDISC Notes/Core) 精确比 (折行连字符 "x- y"→"x-y"; 引号/dash 归一, U1 归 S-TYPO); (c) 列切分串列的 25 个字段由 `ord.py` 去串入词后核**词序**.
3. **旁证** `kbx.py`: `source/cdisc/SDTMIG_v3.4.xlsx` Variables 表 (stdlib 解 xlsx) vs KB 全字段 + Order — 注: xlsx 是 KB 原始来源 (CT 列即 C-code), 只作旁证, 权威仍是 PDF.
4. **CT `*`**: layout CT 列 + 渲染图人工看 10 页 (p148 149 168 171 172 178 180 183 193 197); 其余 7 页 (150 167 169 179 181 196 198) layout 全页无 ` * ` (p196 的 5 处在 :3-13, 属 §6.3.5.1 通用表).

## 命令 (可复跑; S=上面 scratch)
```
python3 -I $S/lay.py $S/lay.json          # 输出各域变量序列; CE 32 HO 28 MH 27 DV 16 DA 27 DD 12 IE 18 BS 35
python3 -I $S/cmp.py $S/lay.json $S > $S/cmp_out.txt   # 列切分比对 (串列假差异见下)
python3 -I $S/bag2.py $S/lay.json $S      # 词袋: 仅 5 行解析伪差异
python3 -I $S/ord.py $S/lay.json $S       # 串列字段词序: checked 25 bad 1 (伪, 见下)
python3 -I $S/xl.py $S/x $S/xl_vars.json && python3 -I $S/kbx.py $S/xl_vars.json CE HO MH DV DA DD IE BS   # total diffs 28 = 20 `*` + 8 Notes 内 \n 段落 (排版)
python3 -I $S/tbl.py $S/lay.json $S > $S/tbl.md   # 195 行; DIFF 0; U5 46; U6 8; `*` 20
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RESULT: RED, exit 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # broken relative links: 18668 (live docs: 42)
```

## 计数闸 (PDF 变量数 = KB 变量数 + 顺序)
| 域 | spec 页 (复核) | PDF (layout) | KB | 顺序 | KB Order 1..N 连续 |
|---|---|---|---|---|---|
| CE | 148-150 | 32 | 32 | 一致 | 是 |
| HO | 167-169 | 28 | 28 | 一致 | 是 |
| MH | 171-172 | 27 | 27 | 一致 | 是 |
| DV | 178-179 | 16 | 16 | 一致 | 是 |
| DA | 180-181 | 27 | 27 | 一致 | 是 |
| DD | 183 | 12 | 12 | 一致 | 是 |
| IE | 193 | 18 | 18 | 一致 | 是 |
| BS | 196 (:39 后)-198 | 35 | 35 | 一致 | 是 |
| 计 | 17 页 | 195 | 195 | | |
页范围与 writer 结论一致 (止页脚注行: p150:12 p169:9 p172:37-38 p179:9 p181:27 p183:39-40 p193:44 p198:17).

## 逐字段结果 (Label/Type/Role/Core/CDISC Notes)
- 词袋: 195 行中 190 行 PDF=KB; 5 行差异全部为解析伪差异: MHENTPT / DDDY 多 "1" (脚注上标独占一行, 解析器未止); DADTC / IEDTC 少 "format." (续行 "or interval … format." 被表头跳行正则误吞; 原页 p181:24 / p193:40 有 "format.", KB 一致); BSSPEC "(SPECTYPE)(GENSMP)" 连写属 CT 列 (U5).
- 列切分串列 25 字段 (Char/Num/Perm/Exp/Timing/"to"/"of"/"End" 越列): 去串入词后词序全一致; 唯一 "ORDER-BAD" CESTDY Label = 算法删去了第一个 "of" (原页 p149:35 "Study Day of Start of / Event", KB "Study Day of Start of Event" 一致).
- 结论: **0 处真实差异**, 无 R2 丢失短语. CEDECOD Notes "Define- XML" 为折行连字符, KB "Define-XML" 正确 (同 writer).

## CT 列逐变量 (全部 195 变量; PDF 列为 layout 去串列后值, `*` 经渲染核)
| 域 | # | 变量 | PDF 页 | Label/Type/Role/Core/Notes (layout 逐词+顺序) | PDF CT (layout, 去串列) | KB CT | CT 判定 |
|---|---|---|---|---|---|---|---|
| CE | 1 | STUDYID | 148 | 一致 | — | — | 一致 |
| CE | 2 | DOMAIN | 148 | 一致 | CE | — | U6 (S-CT) |
| CE | 3 | USUBJID | 148 | 一致 | — | — | 一致 |
| CE | 4 | CESEQ | 148 | 一致 | — | — | 一致 |
| CE | 5 | CEGRPID | 148 | 一致 | — | — | 一致 |
| CE | 6 | CEREFID | 148 | 一致 | — | — | 一致 |
| CE | 7 | CESPID | 148 | 一致 | — | — | 一致 |
| CE | 8 | CETERM | 148 | 一致 | — | — | 一致 |
| CE | 9 | CEDECOD | 148 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| CE | 10 | CECAT | 148 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| CE | 11 | CESCAT | 149 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| CE | 12 | CEPRESP | 149 | 一致 | (NY) | C66742 | U5 (S-CT) |
| CE | 13 | CEOCCUR | 149 | 一致 | (NY) | C66742 | U5 (S-CT) |
| CE | 14 | CESTAT | 149 | 一致 | (ND) | C66789 | U5 (S-CT) |
| CE | 15 | CEREASND | 149 | 一致 | — | — | 一致 |
| CE | 16 | CEBODSYS | 149 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| CE | 17 | CESEV | 149 | 一致 | (SEVRS) | C165643 | U5 (S-CT) |
| CE | 18 | CETOXGR | 149 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| CE | 19 | TAETORD | 149 | 一致 | — | — | 一致 |
| CE | 20 | EPOCH | 149 | 一致 | (EPOCH) | C99079 | U5 (S-CT) |
| CE | 21 | CEDTC | 149 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| CE | 22 | CESTDTC | 149 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| CE | 23 | CEENDTC | 149 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| CE | 24 | CEDY | 149 | 一致 | — | — | 一致 |
| CE | 25 | CESTDY | 149 | 一致 | — | — | 一致 |
| CE | 26 | CEENDY | 149 | 一致 | — | — | 一致 |
| CE | 27 | CESTRF | 149 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| CE | 28 | CEENRF | 149 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| CE | 29 | CESTRTPT | 149 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| CE | 30 | CESTTPT | 150 | 一致 | — | — | 一致 |
| CE | 31 | CEENRTPT | 150 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| CE | 32 | CEENTPT | 150 | 一致 | — | — | 一致 |
| HO | 1 | STUDYID | 167 | 一致 | — | — | 一致 |
| HO | 2 | DOMAIN | 167 | 一致 | HO | — | U6 (S-CT) |
| HO | 3 | USUBJID | 168 | 一致 | — | — | 一致 |
| HO | 4 | HOSEQ | 168 | 一致 | — | — | 一致 |
| HO | 5 | HOGRPID | 168 | 一致 | — | — | 一致 |
| HO | 6 | HOREFID | 168 | 一致 | — | — | 一致 |
| HO | 7 | HOSPID | 168 | 一致 | — | — | 一致 |
| HO | 8 | HOTERM | 168 | 一致 | — | — | 一致 |
| HO | 9 | HODECOD | 168 | 一致 | (HODECOD) | C171444 | U5 (S-CT) |
| HO | 10 | HOCAT | 168 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| HO | 11 | HOSCAT | 168 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| HO | 12 | HOPRESP | 168 | 一致 | (NY) | C66742 | U5 (S-CT) |
| HO | 13 | HOOCCUR | 168 | 一致 | (NY) | C66742 | U5 (S-CT) |
| HO | 14 | HOSTAT | 168 | 一致 | (ND) | C66789 | U5 (S-CT) |
| HO | 15 | HOREASND | 168 | 一致 | — | — | 一致 |
| HO | 16 | TAETORD | 168 | 一致 | — | — | 一致 |
| HO | 17 | EPOCH | 168 | 一致 | (EPOCH) | C99079 | U5 (S-CT) |
| HO | 18 | HODTC | 168 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| HO | 19 | HOSTDTC | 168 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| HO | 20 | HOENDTC | 168 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| HO | 21 | HODY | 168 | 一致 | — | — | 一致 |
| HO | 22 | HOSTDY | 168 | 一致 | — | — | 一致 |
| HO | 23 | HOENDY | 168 | 一致 | — | — | 一致 |
| HO | 24 | HODUR | 168 | 一致 | ISO 8601 duration | ISO 8601 duration | 一致 |
| HO | 25 | HOSTRTPT | 168 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| HO | 26 | HOSTTPT | 168 | 一致 | — | — | 一致 |
| HO | 27 | HOENRTPT | 169 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| HO | 28 | HOENTPT | 169 | 一致 | — | — | 一致 |
| MH | 1 | STUDYID | 171 | 一致 | — | — | 一致 |
| MH | 2 | DOMAIN | 171 | 一致 | MH | — | U6 (S-CT) |
| MH | 3 | USUBJID | 171 | 一致 | — | — | 一致 |
| MH | 4 | MHSEQ | 171 | 一致 | — | — | 一致 |
| MH | 5 | MHGRPID | 171 | 一致 | — | — | 一致 |
| MH | 6 | MHREFID | 171 | 一致 | — | — | 一致 |
| MH | 7 | MHSPID | 171 | 一致 | — | — | 一致 |
| MH | 8 | MHTERM | 171 | 一致 | — | — | 一致 |
| MH | 9 | MHMODIFY | 171 | 一致 | — | — | 一致 |
| MH | 10 | MHDECOD | 171 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| MH | 11 | MHEVDTYP | 171 | 一致 | (MHEDTTYP) | C124301 | U5 (S-CT) |
| MH | 12 | MHCAT | 171 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| MH | 13 | MHSCAT | 171 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| MH | 14 | MHPRESP | 171 | 一致 | (NY) | C66742 | U5 (S-CT) |
| MH | 15 | MHOCCUR | 171 | 一致 | (NY) | C66742 | U5 (S-CT) |
| MH | 16 | MHSTAT | 172 | 一致 | (ND) | C66789 | U5 (S-CT) |
| MH | 17 | MHREASND | 172 | 一致 | — | — | 一致 |
| MH | 18 | MHBODSYS | 172 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| MH | 19 | TAETORD | 172 | 一致 | — | — | 一致 |
| MH | 20 | EPOCH | 172 | 一致 | (EPOCH) | C99079 | U5 (S-CT) |
| MH | 21 | MHDTC | 172 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| MH | 22 | MHSTDTC | 172 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| MH | 23 | MHENDTC | 172 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| MH | 24 | MHDY | 172 | 一致 | — | — | 一致 |
| MH | 25 | MHENRF | 172 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| MH | 26 | MHENRTPT | 172 | 一致 | (STENRF) | C66728 | U5 (S-CT) |
| MH | 27 | MHENTPT | 172 | 一致 | — | — | 一致 |
| DV | 1 | STUDYID | 178 | 一致 | — | — | 一致 |
| DV | 2 | DOMAIN | 178 | 一致 | DV | — | U6 (S-CT) |
| DV | 3 | USUBJID | 178 | 一致 | — | — | 一致 |
| DV | 4 | DVSEQ | 178 | 一致 | — | — | 一致 |
| DV | 5 | DVREFID | 178 | 一致 | — | — | 一致 |
| DV | 6 | DVSPID | 178 | 一致 | — | — | 一致 |
| DV | 7 | DVTERM | 178 | 一致 | — | — | 一致 |
| DV | 8 | DVDECOD | 178 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| DV | 9 | DVCAT | 178 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| DV | 10 | DVSCAT | 178 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| DV | 11 | TAETORD | 178 | 一致 | — | — | 一致 |
| DV | 12 | EPOCH | 178 | 一致 | (EPOCH) | C99079 | U5 (S-CT) |
| DV | 13 | DVSTDTC | 179 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| DV | 14 | DVENDTC | 179 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| DV | 15 | DVSTDY | 179 | 一致 | — | — | 一致 |
| DV | 16 | DVENDY | 179 | 一致 | — | — | 一致 |
| DA | 1 | STUDYID | 180 | 一致 | — | — | 一致 |
| DA | 2 | DOMAIN | 180 | 一致 | DA | — | U6 (S-CT) |
| DA | 3 | USUBJID | 180 | 一致 | — | — | 一致 |
| DA | 4 | DASEQ | 180 | 一致 | — | — | 一致 |
| DA | 5 | DAGRPID | 180 | 一致 | — | — | 一致 |
| DA | 6 | DAREFID | 180 | 一致 | — | — | 一致 |
| DA | 7 | DASPID | 180 | 一致 | — | — | 一致 |
| DA | 8 | DALNKID | 180 | 一致 | — | — | 一致 |
| DA | 9 | DALNKGRP | 180 | 一致 | — | — | 一致 |
| DA | 10 | DATESTCD | 180 | 一致 | (DATESTCD) | C78732 | U5 (S-CT) |
| DA | 11 | DATEST | 180 | 一致 | (DATEST) | C78731 | U5 (S-CT) |
| DA | 12 | DACAT | 180 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| DA | 13 | DASCAT | 180 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| DA | 14 | DAORRES | 180 | 一致 | — | — | 一致 |
| DA | 15 | DAORRESU | 180 | 一致 | (UNIT) | C71620 | U5 (S-CT) |
| DA | 16 | DASTRESC | 181 | 一致 | — | — | 一致 |
| DA | 17 | DASTRESN | 181 | 一致 | — | — | 一致 |
| DA | 18 | DASTRESU | 181 | 一致 | (UNIT) | C71620 | U5 (S-CT) |
| DA | 19 | DASTAT | 181 | 一致 | (ND) | C66789 | U5 (S-CT) |
| DA | 20 | DAREASND | 181 | 一致 | — | — | 一致 |
| DA | 21 | VISITNUM | 181 | 一致 | — | — | 一致 |
| DA | 22 | VISIT | 181 | 一致 | — | — | 一致 |
| DA | 23 | VISITDY | 181 | 一致 | — | — | 一致 |
| DA | 24 | TAETORD | 181 | 一致 | — | — | 一致 |
| DA | 25 | EPOCH | 181 | 一致 | (EPOCH) | C99079 | U5 (S-CT) |
| DA | 26 | DADTC | 181 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| DA | 27 | DADY | 181 | 一致 | — | — | 一致 |
| DD | 1 | STUDYID | 183 | 一致 | — | — | 一致 |
| DD | 2 | DOMAIN | 183 | 一致 | DD | — | U6 (S-CT) |
| DD | 3 | USUBJID | 183 | 一致 | — | — | 一致 |
| DD | 4 | DDSEQ | 183 | 一致 | — | — | 一致 |
| DD | 5 | DDTESTCD | 183 | 一致 | (DTHDXCD) | C116108 | U5 (S-CT) |
| DD | 6 | DDTEST | 183 | 一致 | (DTHDX) | C116107 | U5 (S-CT) |
| DD | 7 | DDORRES | 183 | 一致 | — | — | 一致 |
| DD | 8 | DDSTRESC | 183 | 一致 | — | — | 一致 |
| DD | 9 | DDRESCAT | 183 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| DD | 10 | DDEVAL | 183 | 一致 | (EVAL) | C78735 | U5 (S-CT) |
| DD | 11 | DDDTC | 183 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| DD | 12 | DDDY | 183 | 一致 | — | — | 一致 |
| IE | 1 | STUDYID | 193 | 一致 | — | — | 一致 |
| IE | 2 | DOMAIN | 193 | 一致 | IE | — | U6 (S-CT) |
| IE | 3 | USUBJID | 193 | 一致 | — | — | 一致 |
| IE | 4 | IESEQ | 193 | 一致 | — | — | 一致 |
| IE | 5 | IESPID | 193 | 一致 | — | — | 一致 |
| IE | 6 | IETESTCD | 193 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| IE | 7 | IETEST | 193 | 一致 | — | — | 一致 |
| IE | 8 | IECAT | 193 | 一致 | (IECAT) | C66797 | U5 (S-CT) |
| IE | 9 | IESCAT | 193 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| IE | 10 | IEORRES | 193 | 一致 | (NY) | C66742 | U5 (S-CT) |
| IE | 11 | IESTRESC | 193 | 一致 | (NY) | C66742 | U5 (S-CT) |
| IE | 12 | VISITNUM | 193 | 一致 | — | — | 一致 |
| IE | 13 | VISIT | 193 | 一致 | — | — | 一致 |
| IE | 14 | VISITDY | 193 | 一致 | — | — | 一致 |
| IE | 15 | TAETORD | 193 | 一致 | — | — | 一致 |
| IE | 16 | EPOCH | 193 | 一致 | (EPOCH) | C99079 | U5 (S-CT) |
| IE | 17 | IEDTC | 193 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| IE | 18 | IEDY | 193 | 一致 | — | — | 一致 |
| BS | 1 | STUDYID | 196 | 一致 | — | — | 一致 |
| BS | 2 | DOMAIN | 196 | 一致 | BS | — | U6 (S-CT) |
| BS | 3 | USUBJID | 196 | 一致 | — | — | 一致 |
| BS | 4 | SPDEVID | 196 | 一致 | — | — | 一致 |
| BS | 5 | BSSEQ | 196 | 一致 | — | — | 一致 |
| BS | 6 | BSGRPID | 197 | 一致 | — | — | 一致 |
| BS | 7 | BSREFID | 197 | 一致 | — | — | 一致 |
| BS | 8 | BSSPID | 197 | 一致 | — | — | 一致 |
| BS | 9 | BSTESTCD | 197 | 一致 | (BSTESTCD) | C124300 | U5 (S-CT) |
| BS | 10 | BSTEST | 197 | 一致 | (BSTEST) | C124299 | U5 (S-CT) |
| BS | 11 | BSCAT | 197 | 一致 | — | — | 一致 |
| BS | 12 | BSSCAT | 197 | 一致 | — | — | 一致 |
| BS | 13 | BSORRES | 197 | 一致 | — | — | 一致 |
| BS | 14 | BSORRESU | 197 | 一致 | (UNIT) | C71620 | U5 (S-CT) |
| BS | 15 | BSSTRESC | 197 | 一致 | — | — | 一致 |
| BS | 16 | BSSTRESN | 197 | 一致 | — | — | 一致 |
| BS | 17 | BSSTRESU | 197 | 一致 | (UNIT) | C71620 | U5 (S-CT) |
| BS | 18 | BSSTAT | 197 | 一致 | (ND) | C66789 | U5 (S-CT) |
| BS | 19 | BSREASND | 197 | 一致 | — | — | 一致 |
| BS | 20 | BSNAM | 197 | 一致 | — | — | 一致 |
| BS | 21 | BSSPEC | 197 | 一致 | (SPECTYPE)(GENSMP) | C78734; C111114 | U5 (S-CT) |
| BS | 22 | BSANTREG | 197 | 一致 | `*` | `*` | 一致 (`*` 本批补, 渲染核) |
| BS | 23 | BSSPCCND | 197 | 一致 | (SPECCOND) | C78733 | U5 (S-CT) |
| BS | 24 | BSMETHOD | 197 | 一致 | (METHOD) | C85492 | U5 (S-CT) |
| BS | 25 | BSBLFL | 197 | 一致 | (NY) | C66742 | U5 (S-CT) |
| BS | 26 | VISITNUM | 197 | 一致 | — | — | 一致 |
| BS | 27 | VISIT | 197 | 一致 | — | — | 一致 |
| BS | 28 | VISITDY | 197 | 一致 | — | — | 一致 |
| BS | 29 | BSDTC | 197 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |
| BS | 30 | BSDY | 198 | 一致 | — | — | 一致 |
| BS | 31 | BSTPT | 198 | 一致 | — | — | 一致 |
| BS | 32 | BSTPTNUM | 198 | 一致 | — | — | 一致 |
| BS | 33 | BSELTM | 198 | 一致 | ISO 8601 duration | ISO 8601 duration | 一致 |
| BS | 34 | BSTPTREF | 198 | 一致 | — | — | 一致 |
| BS | 35 | BSRFTDTC | 198 | 一致 | ISO 8601 datetime or interval | ISO 8601 datetime or interval | 一致 |

CT 汇总: 一致 141 (含本批补 `*` 20, 全部渲染确认; BSCAT/BSSCAT PDF 空 → KB 空, 正确); U5 46 / U6 8 → S-CT, 不在本批; **KB 中无 PDF 没有的 `*`**; 差异 0.

## 脚注 (gaps F ×8) + U7 位置
| 域 | KB 行 | 原子 | 逐字 (`norm(verbatim) in norm(file)`) | 位置 |
|---|---|---|---|---|
| CE | 294 | ig34_p0150_a004 | True | 末变量 CEENTPT 块 `---` 后, `## Cross References` 前 |
| HO | 258 | ig34_p0169_a0003 | True | HOENTPT 后, CR 前 |
| MH | 249 | ig34_p0172_a0013 | True | MHENTPT 后, CR 前 |
| DV | 150 | ig34_p0179_a0005 | True | DVENDY 后, CR 前 |
| DA | 249 | ig34_p0181_a013 | True | DADY 后, CR 前 |
| DD | 114 | ig34_p0183_a020 | True | DDDY 后, CR 前 |
| IE | 168 | ig34_p0193_a025 | True | IEDY 后, CR 前 |
| BS | 321 | ig34_p0198_a008 | True | BSRFTDTC 后, CR 前 |
8 行逐字相同 (`uniq -c` = 8); 与 p150:12 layout 文本去上标后逐字 `==` True; 上标 ¹ 照渲染; 格式同 AG/PR/EX 先例 (`> ¹In this column, …`).

## G-TB6 反向溯源 / 授权范围
- `git diff HEAD -- knowledge_base/domains/{CE,HO,MH,DV,DA,DD,IE,BS}/spec.md` 的 +/- 行 `sort | uniq -c`: `-` CT 空 ×20, `+` CT `*` ×20, `+` 脚注 ×8, `+` 空行 ×8. 无其他改动. 全部有 PDF 出处 (CT 列 `*` / 脚注).
- 结构行: 新增 8 空行 (脚注块分隔). 无标题/锚点/变量块增删; 删除清单 = 无 (旧值空串); D6 清单 = 无 (`> Class|Structure` + Cross References 为 U8 导航).
- 授权: `git diff HEAD --stat -- knowledge_base/` 中本批 8 文件之外的改动 (BE/CM/CO/DM/ML/SM/SU/SV spec, CO/assumptions, model/01/03/04/05) 属别批, 本批 `narrow_files` 空, 不计.
- census: `pdf_ranges` 空 (spec 变量块非 Row 表) → 跳过 table_census, 由上方独立 layout 逐变量 + 渲染替代. `census_items` 空.

## fp_match 回归
RESULT: RED (全局); 回归 72 条, 71 条在 `work/t2_fp_expected_regressions.jsonl`; 唯一新增 ig34_p0060_a024 (p60, ch04 页, 非本批文件). 本批页面上的回归仅 ig34_p0179_a0018 (DV example TABLE_ROW, 已在预期清单, 不在 spec.md). 本批 8 脚注原子 hit_any=PC/spec.md (glob 首个), 直接查本批目标文件均命中.

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无 | — |

## 备注 (非缺陷)
- xlsx 旁证: CESTRF/CEENRF/CESTRTPT/CEENRTPT/HOSTRTPT/HOENRTPT/MHENRF/MHENRTPT Notes 中 "Not all values…" 在 PDF 为单元格内另起一行 (p149 渲染可见), KB 并为一段 → 段落拆合差异, 按 S-FND 口径不算缺口.
- writer 方法自述 (sc2 4 种失效、续页盲区复核) 与本 reviewer 独立结果一致.
- check_links: live docs 42 (= 基线).
