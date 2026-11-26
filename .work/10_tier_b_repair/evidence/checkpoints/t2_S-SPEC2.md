# T2S 扫描批 S-SPEC2 (spec-only: CE HO MH DV DA DD IE BS) — writer attempt 1

> 2026-11-26, oh-my-claudecode:executor (opus). Brief `subagent_prompts/t2s_scan_writer_v1.0.md`; 批次 `work/t2_batches/S-SPEC2.json`.
> 只改 8 个 spec.md; assumptions/examples 未碰; 未 stash/checkout/commit. 基线 = `git show HEAD:<file>` (8 文件改前与 HEAD 一致).
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC2_writer/`
> (bb_N.html = `pdftotext -bbox`; sc2.py = speccmp.py 改进版 (见下); sc2w.py = 同上但空格敏感; cmp*_before/after.txt; ct_N-N.png = CT 列裁图 90dpi; base/ = HEAD 副本; apply.py 精确替换+命中断言)

md5 改后: CE `e0b7bfb8d3660c9c065ae36561184bdb` (311→313) · HO `13fc4cd385d01a04696b4784e17dfee7` (277→279) · MH `3549b775b43647400e4a8e96c6473ed8` (266→268) · DV `810eadba05f285987a352a6ea670eacb` (163→165) · DA `6a7ad298fc130deb5affbf33c1389b5f` (266→268) · DD `29a11460f1ecbde2718eaa29f17bd58a` (130→132) · IE `0360023552b6b435841ba6b5dfd60e62` (183→185) · BS `651e3318590d216f4ea4ffaee9f14866` (345→347)

## 完整节页范围 (O20 复核; 本批只扫各域 spec 表)
| 域 | 节 (json lo-hi) | spec 表所在页 (复核) | 起止依据 (layout `work/pdf_pages/ig34_pNNNN.txt`) |
|---|---|---|---|
| CE | §6.2.3 (148-155) | **148-150** | p148:19 节标题, :22 `CE – Specification`, :24 表头; p150:12 脚注, :15 `CE – Assumptions` |
| HO | §6.2.5 (167-171) | **167-169** | p167:30 节标题, :36 表头 (仅 STUDYID DOMAIN); p169:9 脚注, :14 `HO – Assumptions` |
| MH | §6.2.6 (171-178) | **171-172** | p171:12 节标题, :17 表头; p172 脚注 (bbox), :41 `MH – Assumptions` |
| DV | §6.2.7 (178-180) | **178-179** | p178:16 节标题, :21 表头; p179 无表头续表 (DVSTDTC..DVENDY), :9 脚注, :14 `DV – Assumptions` |
| DA | §6.3.1 (180-183) | **180-181** | p180:1 §6.3 章引言 (非本批), :5 节标题, :10 表头; p181:27 脚注, :32 `DA – Assumptions` |
| DD | §6.3.2 (183-185) | **183** | p183:1 节标题, :10 表头, 脚注同页 (bbox); p184:1 `DD – Assumptions` (非 spec, 不扫) |
| IE | §6.3.4 (193-194) | **193** | p193:1 节标题, :6 表头, :44 脚注; p194:1 `IE – Assumptions` |
| BS | §6.3.5.2 (196-199) | **196-198** | p196:1-26 = §6.3.5.1 通用表尾 + 其脚注 (属 LB, 不归本批); :31 BS 节标题, :41 BS 表头; p198:17 脚注, :22 `BS – Assumptions` |
- 边界页上别节内容 (p148 BE/BS relrec 与 References、p167 DS Ex、p171 HO Ex 尾、p178 MH Ex、p180 §6.3 引言、p196 §6.3.5.1) 不归本批.

## 方法
- `sc2.py` = `work/scratch/t2s_tools/speccmp.py` 修正版. 原脚本在本批 4 处失效 (实测 `python3 -I speccmp.py <scratch> HO 167,168,169` 等): ① 页顶正文 "In this study…" 被当成脚注止点 (p167 丢 3 变量); ② 页上两个表头时取错 (p196 读成 §6.3.5.1 通用表 → 假报 VISITNUM Core/VISIT Notes 差异); ③ 无表头续页 (p179) 无法解析; ④ 脚注上标 "1" 为独立词, 末变量吞入脚注. (另据改前输出: 两行表头页上表头下第一个变量被 `hy+25` 固定偏移吞掉 — MH/DV/DA 丢 STUDYID, HO 丢 USUBJID/HOENRTPT, DA 丢 DASTRESC, BS 丢 BSGRPID; 三行表头的 CE/IE/DD 未丢. 上文 ① 的 "p167 丢 3 变量" 为两因混合, 以此为准.) 修正: 表头取页上最后一个 `Variable…Label` 行, 正文起于表头 +15pt; 止点 = 脚注行 `^1? ?In this column` / `XX – ` 标题 / 编号节标题 / 版权行; 无表头页沿用前页列界.
- 每域逐变量逐字段比 (Label/Type/CT/Role/Core/CDISC Notes 全文) + 变量数/顺序 + KB `Order` 字段连续性; 两遍: sc2.py (去全部空白) + sc2w.py (仅合并空白, 折行连字符 "x- y" → "x-y", 空格敏感). 引号/dash 归一 (S-TYPO 口径).
- CT 列 `*` 复核: 渲染 17 页 CT 列裁图 (`ct_N-N.png`, 90dpi), 人工看图 10 页 (其余 7 页 p150 167 169 179 181 196 198 bbox 无 `*`, 未看图): p148 p149 p168 p171 p172 p178 p180 p183 p193 p197, `*` 位置与 bbox 完全一致 (含 BSCAT/BSSCAT PDF 为空、非 `*`).
- 续页盲区复核: sc2 丢弃 "表头与首变量名之间" 的词; 对 9 个续页 (p149 150 168 169 172 179 181 197 198) 查 layout 文本表头后首行, 均以变量名开头 (CESCAT CESTTPT USUBJID HOENRTPT MHSTAT DVSTDTC DASTRESC BSGRPID BSDY), 仅 p149/p150 有表头残词 "Format1" → 无跨页折断的 Notes 续行, 结论不变.
- KB 结构: 8 文件各变量块恰 7 字段, 变量块之外仅 H1 / `> Class|Structure` / `---` / Cross References (U8 导航).

## 双向全扫 (每域 spec 表逐变量结果表; 改后 sc2w.py)
PDF→KB: 195/195 变量命中, 顺序一致, Order 1..N 连续; KB→PDF: kb-only 变量 0, kb-only 字段 0. Label/Type/Role/Core/CDISC Notes **零差异** (唯一非 OK = CEDECOD Notes "Define- XML" = PDF 折行连字符, KB "Define-XML" 正确).
CT 列剩余差异全部为 U5 (C-code vs PDF 括号短名, 46 处) / U6 (DOMAIN, 8 处) → 归 S-CT, 本批不改.

| 域 | spec 页 | PDF 变量 | KB 变量 | 顺序 | 字段差异 (改前) | CT `*` 补 | 脚注 | U5 / U6 留 S-CT |
|---|---|---|---|---|---|---|---|---|
| CE | 148-150 | 32 | 32 | 一致 | 0 | 5 | 补 | 9 / 1 |
| HO | 167-169 | 28 | 28 | 一致 | 0 | 2 | 补 | 7 / 1 |
| MH | 171-172 | 27 | 27 | 一致 | 0 | 4 | 补 | 7 / 1 |
| DV | 178-179 | 16 | 16 | 一致 | 0 | 3 | 补 | 1 / 1 |
| DA | 180-181 | 27 | 27 | 一致 | 0 | 2 | 补 | 6 / 1 |
| DD | 183 | 12 | 12 | 一致 | 0 | 1 | 补 | 3 / 1 |
| IE | 193 | 18 | 18 | 一致 | 0 | 2 | 补 | 4 / 1 |
| BS | 196-198 | 35 | 35 | 一致 | 0 | 1 | 补 | 9 / 1 |
| 计 | 17 页 | 195 | 195 | | 0 | 20 | 8 | 46 / 8 |

### 逐变量结果
| 域 | # | 变量 | PDF 页 | Order/Label/Type/Role/Core/CDISC Notes | CT 列 | 处理 |
|---|---|---|---|---|---|---|
| CE | 1 | STUDYID | 148 | 一致 | 一致 | — |
| CE | 2 | DOMAIN | 148 | 一致 | DOMAIN CT `CE` (U6→S-CT) | — |
| CE | 3 | USUBJID | 148 | 一致 | 一致 | — |
| CE | 4 | CESEQ | 148 | 一致 | 一致 | — |
| CE | 5 | CEGRPID | 148 | 一致 | 一致 | — |
| CE | 6 | CEREFID | 148 | 一致 | 一致 | — |
| CE | 7 | CESPID | 148 | 一致 | 一致 | — |
| CE | 8 | CETERM | 148 | 一致 | 一致 | — |
| CE | 9 | CEDECOD | 148 | 一致 (PDF "Define- XML" 为折行连字符) | `*` (改前空) | REPLACED CT 空→`*` |
| CE | 10 | CECAT | 148 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CE | 11 | CESCAT | 149 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CE | 12 | CEPRESP | 149 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| CE | 13 | CEOCCUR | 149 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| CE | 14 | CESTAT | 149 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| CE | 15 | CEREASND | 149 | 一致 | 一致 | — |
| CE | 16 | CEBODSYS | 149 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CE | 17 | CESEV | 149 | 一致 | `(SEVRS)` vs `C165643` (U5→S-CT) | — |
| CE | 18 | CETOXGR | 149 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CE | 19 | TAETORD | 149 | 一致 | 一致 | — |
| CE | 20 | EPOCH | 149 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| CE | 21 | CEDTC | 149 | 一致 | 一致 | — |
| CE | 22 | CESTDTC | 149 | 一致 | 一致 | — |
| CE | 23 | CEENDTC | 149 | 一致 | 一致 | — |
| CE | 24 | CEDY | 149 | 一致 | 一致 | — |
| CE | 25 | CESTDY | 149 | 一致 | 一致 | — |
| CE | 26 | CEENDY | 149 | 一致 | 一致 | — |
| CE | 27 | CESTRF | 149 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| CE | 28 | CEENRF | 149 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| CE | 29 | CESTRTPT | 149 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| CE | 30 | CESTTPT | 150 | 一致 | 一致 | — |
| CE | 31 | CEENRTPT | 150 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| CE | 32 | CEENTPT | 150 | 一致 | 一致 | — |
| HO | 1 | STUDYID | 167 | 一致 | 一致 | — |
| HO | 2 | DOMAIN | 167 | 一致 | DOMAIN CT `HO` (U6→S-CT) | — |
| HO | 3 | USUBJID | 168 | 一致 | 一致 | — |
| HO | 4 | HOSEQ | 168 | 一致 | 一致 | — |
| HO | 5 | HOGRPID | 168 | 一致 | 一致 | — |
| HO | 6 | HOREFID | 168 | 一致 | 一致 | — |
| HO | 7 | HOSPID | 168 | 一致 | 一致 | — |
| HO | 8 | HOTERM | 168 | 一致 | 一致 | — |
| HO | 9 | HODECOD | 168 | 一致 | `(HODECOD)` vs `C171444` (U5→S-CT) | — |
| HO | 10 | HOCAT | 168 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| HO | 11 | HOSCAT | 168 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| HO | 12 | HOPRESP | 168 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| HO | 13 | HOOCCUR | 168 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| HO | 14 | HOSTAT | 168 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| HO | 15 | HOREASND | 168 | 一致 | 一致 | — |
| HO | 16 | TAETORD | 168 | 一致 | 一致 | — |
| HO | 17 | EPOCH | 168 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| HO | 18 | HODTC | 168 | 一致 | 一致 | — |
| HO | 19 | HOSTDTC | 168 | 一致 | 一致 | — |
| HO | 20 | HOENDTC | 168 | 一致 | 一致 | — |
| HO | 21 | HODY | 168 | 一致 | 一致 | — |
| HO | 22 | HOSTDY | 168 | 一致 | 一致 | — |
| HO | 23 | HOENDY | 168 | 一致 | 一致 | — |
| HO | 24 | HODUR | 168 | 一致 | 一致 | — |
| HO | 25 | HOSTRTPT | 168 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| HO | 26 | HOSTTPT | 168 | 一致 | 一致 | — |
| HO | 27 | HOENRTPT | 169 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| HO | 28 | HOENTPT | 169 | 一致 | 一致 | — |
| MH | 1 | STUDYID | 171 | 一致 | 一致 | — |
| MH | 2 | DOMAIN | 171 | 一致 | DOMAIN CT `MH` (U6→S-CT) | — |
| MH | 3 | USUBJID | 171 | 一致 | 一致 | — |
| MH | 4 | MHSEQ | 171 | 一致 | 一致 | — |
| MH | 5 | MHGRPID | 171 | 一致 | 一致 | — |
| MH | 6 | MHREFID | 171 | 一致 | 一致 | — |
| MH | 7 | MHSPID | 171 | 一致 | 一致 | — |
| MH | 8 | MHTERM | 171 | 一致 | 一致 | — |
| MH | 9 | MHMODIFY | 171 | 一致 | 一致 | — |
| MH | 10 | MHDECOD | 171 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MH | 11 | MHEVDTYP | 171 | 一致 | `(MHEDTTYP)` vs `C124301` (U5→S-CT) | — |
| MH | 12 | MHCAT | 171 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MH | 13 | MHSCAT | 171 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MH | 14 | MHPRESP | 171 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MH | 15 | MHOCCUR | 171 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MH | 16 | MHSTAT | 172 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| MH | 17 | MHREASND | 172 | 一致 | 一致 | — |
| MH | 18 | MHBODSYS | 172 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MH | 19 | TAETORD | 172 | 一致 | 一致 | — |
| MH | 20 | EPOCH | 172 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| MH | 21 | MHDTC | 172 | 一致 | 一致 | — |
| MH | 22 | MHSTDTC | 172 | 一致 | 一致 | — |
| MH | 23 | MHENDTC | 172 | 一致 | 一致 | — |
| MH | 24 | MHDY | 172 | 一致 | 一致 | — |
| MH | 25 | MHENRF | 172 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| MH | 26 | MHENRTPT | 172 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| MH | 27 | MHENTPT | 172 | 一致 | 一致 | — |
| DV | 1 | STUDYID | 178 | 一致 | 一致 | — |
| DV | 2 | DOMAIN | 178 | 一致 | DOMAIN CT `DV` (U6→S-CT) | — |
| DV | 3 | USUBJID | 178 | 一致 | 一致 | — |
| DV | 4 | DVSEQ | 178 | 一致 | 一致 | — |
| DV | 5 | DVREFID | 178 | 一致 | 一致 | — |
| DV | 6 | DVSPID | 178 | 一致 | 一致 | — |
| DV | 7 | DVTERM | 178 | 一致 | 一致 | — |
| DV | 8 | DVDECOD | 178 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| DV | 9 | DVCAT | 178 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| DV | 10 | DVSCAT | 178 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| DV | 11 | TAETORD | 178 | 一致 | 一致 | — |
| DV | 12 | EPOCH | 178 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| DV | 13 | DVSTDTC | 179 | 一致 | 一致 | — |
| DV | 14 | DVENDTC | 179 | 一致 | 一致 | — |
| DV | 15 | DVSTDY | 179 | 一致 | 一致 | — |
| DV | 16 | DVENDY | 179 | 一致 | 一致 | — |
| DA | 1 | STUDYID | 180 | 一致 | 一致 | — |
| DA | 2 | DOMAIN | 180 | 一致 | DOMAIN CT `DA` (U6→S-CT) | — |
| DA | 3 | USUBJID | 180 | 一致 | 一致 | — |
| DA | 4 | DASEQ | 180 | 一致 | 一致 | — |
| DA | 5 | DAGRPID | 180 | 一致 | 一致 | — |
| DA | 6 | DAREFID | 180 | 一致 | 一致 | — |
| DA | 7 | DASPID | 180 | 一致 | 一致 | — |
| DA | 8 | DALNKID | 180 | 一致 | 一致 | — |
| DA | 9 | DALNKGRP | 180 | 一致 | 一致 | — |
| DA | 10 | DATESTCD | 180 | 一致 | `(DATESTCD)` vs `C78732` (U5→S-CT) | — |
| DA | 11 | DATEST | 180 | 一致 | `(DATEST)` vs `C78731` (U5→S-CT) | — |
| DA | 12 | DACAT | 180 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| DA | 13 | DASCAT | 180 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| DA | 14 | DAORRES | 180 | 一致 | 一致 | — |
| DA | 15 | DAORRESU | 180 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| DA | 16 | DASTRESC | 181 | 一致 | 一致 | — |
| DA | 17 | DASTRESN | 181 | 一致 | 一致 | — |
| DA | 18 | DASTRESU | 181 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| DA | 19 | DASTAT | 181 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| DA | 20 | DAREASND | 181 | 一致 | 一致 | — |
| DA | 21 | VISITNUM | 181 | 一致 | 一致 | — |
| DA | 22 | VISIT | 181 | 一致 | 一致 | — |
| DA | 23 | VISITDY | 181 | 一致 | 一致 | — |
| DA | 24 | TAETORD | 181 | 一致 | 一致 | — |
| DA | 25 | EPOCH | 181 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| DA | 26 | DADTC | 181 | 一致 | 一致 | — |
| DA | 27 | DADY | 181 | 一致 | 一致 | — |
| DD | 1 | STUDYID | 183 | 一致 | 一致 | — |
| DD | 2 | DOMAIN | 183 | 一致 | DOMAIN CT `DD` (U6→S-CT) | — |
| DD | 3 | USUBJID | 183 | 一致 | 一致 | — |
| DD | 4 | DDSEQ | 183 | 一致 | 一致 | — |
| DD | 5 | DDTESTCD | 183 | 一致 | `(DTHDXCD)` vs `C116108` (U5→S-CT) | — |
| DD | 6 | DDTEST | 183 | 一致 | `(DTHDX)` vs `C116107` (U5→S-CT) | — |
| DD | 7 | DDORRES | 183 | 一致 | 一致 | — |
| DD | 8 | DDSTRESC | 183 | 一致 | 一致 | — |
| DD | 9 | DDRESCAT | 183 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| DD | 10 | DDEVAL | 183 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| DD | 11 | DDDTC | 183 | 一致 | 一致 | — |
| DD | 12 | DDDY | 183 | 一致 | 一致 | — |
| IE | 1 | STUDYID | 193 | 一致 | 一致 | — |
| IE | 2 | DOMAIN | 193 | 一致 | DOMAIN CT `IE` (U6→S-CT) | — |
| IE | 3 | USUBJID | 193 | 一致 | 一致 | — |
| IE | 4 | IESEQ | 193 | 一致 | 一致 | — |
| IE | 5 | IESPID | 193 | 一致 | 一致 | — |
| IE | 6 | IETESTCD | 193 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| IE | 7 | IETEST | 193 | 一致 | 一致 | — |
| IE | 8 | IECAT | 193 | 一致 | `(IECAT)` vs `C66797` (U5→S-CT) | — |
| IE | 9 | IESCAT | 193 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| IE | 10 | IEORRES | 193 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| IE | 11 | IESTRESC | 193 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| IE | 12 | VISITNUM | 193 | 一致 | 一致 | — |
| IE | 13 | VISIT | 193 | 一致 | 一致 | — |
| IE | 14 | VISITDY | 193 | 一致 | 一致 | — |
| IE | 15 | TAETORD | 193 | 一致 | 一致 | — |
| IE | 16 | EPOCH | 193 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| IE | 17 | IEDTC | 193 | 一致 | 一致 | — |
| IE | 18 | IEDY | 193 | 一致 | 一致 | — |
| BS | 1 | STUDYID | 196 | 一致 | 一致 | — |
| BS | 2 | DOMAIN | 196 | 一致 | DOMAIN CT `BS` (U6→S-CT) | — |
| BS | 3 | USUBJID | 196 | 一致 | 一致 | — |
| BS | 4 | SPDEVID | 196 | 一致 | 一致 | — |
| BS | 5 | BSSEQ | 196 | 一致 | 一致 | — |
| BS | 6 | BSGRPID | 197 | 一致 | 一致 | — |
| BS | 7 | BSREFID | 197 | 一致 | 一致 | — |
| BS | 8 | BSSPID | 197 | 一致 | 一致 | — |
| BS | 9 | BSTESTCD | 197 | 一致 | `(BSTESTCD)` vs `C124300` (U5→S-CT) | — |
| BS | 10 | BSTEST | 197 | 一致 | `(BSTEST)` vs `C124299` (U5→S-CT) | — |
| BS | 11 | BSCAT | 197 | 一致 | 一致 | — |
| BS | 12 | BSSCAT | 197 | 一致 | 一致 | — |
| BS | 13 | BSORRES | 197 | 一致 | 一致 | — |
| BS | 14 | BSORRESU | 197 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| BS | 15 | BSSTRESC | 197 | 一致 | 一致 | — |
| BS | 16 | BSSTRESN | 197 | 一致 | 一致 | — |
| BS | 17 | BSSTRESU | 197 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| BS | 18 | BSSTAT | 197 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| BS | 19 | BSREASND | 197 | 一致 | 一致 | — |
| BS | 20 | BSNAM | 197 | 一致 | 一致 | — |
| BS | 21 | BSSPEC | 197 | 一致 | `(SPECTYPE)(GENSMP)` vs `C78734; C111114` (U5→S-CT) | — |
| BS | 22 | BSANTREG | 197 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| BS | 23 | BSSPCCND | 197 | 一致 | `(SPECCOND)` vs `C78733` (U5→S-CT) | — |
| BS | 24 | BSMETHOD | 197 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| BS | 25 | BSBLFL | 197 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| BS | 26 | VISITNUM | 197 | 一致 | 一致 | — |
| BS | 27 | VISIT | 197 | 一致 | 一致 | — |
| BS | 28 | VISITDY | 197 | 一致 | 一致 | — |
| BS | 29 | BSDTC | 197 | 一致 | 一致 | — |
| BS | 30 | BSDY | 198 | 一致 | 一致 | — |
| BS | 31 | BSTPT | 198 | 一致 | 一致 | — |
| BS | 32 | BSTPTNUM | 198 | 一致 | 一致 | — |
| BS | 33 | BSELTM | 198 | 一致 | 一致 | — |
| BS | 34 | BSTPTREF | 198 | 一致 | 一致 | — |
| BS | 35 | BSRFTDTC | 198 | 一致 | 一致 | — |

### 逐页双向扫描日志
| 页 | 节 | PDF→KB: 变量/命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处→处理 | 表 | 备注 |
|---|---|---|---|---|---|
| 148 | §6.2.3 CE spec | 10 / 10; CT `*` 2→2 (CEDECOD CECAT) | CE/spec STUDYID..CECAT; 0 | spec bbox + 裁图 | 节标题/Description/spec 首句在 assumptions.md (已终版, 不碰); DOMAIN CT U6 |
| 149 | CE spec | 19 / 19; `*` 3→3 (CESCAT CEBODSYS CETOXGR) | CESCAT..CESTRTPT; 0 | 同上 | U5 8 处 |
| 150 | CE spec 尾 | 3 / 3; 脚注 1→1 | CESTTPT..CEENTPT + 脚注; 0 | 同上 | CEENRTPT U5 |
| 167 | §6.2.5 HO spec 首 | 2 / 2 | STUDYID DOMAIN; 0 | bbox | DOMAIN U6 |
| 168 | HO spec | 24 / 24; `*` 2→2 (HOCAT HOSCAT) | USUBJID..HOSTTPT; 0 | bbox + 裁图 | U5 6 处 |
| 169 | HO spec 尾 | 2 / 2; 脚注 1→1 | HOENRTPT HOENTPT + 脚注; 0 | bbox | U5 1 |
| 171 | §6.2.6 MH spec | 15 / 15; `*` 3→3 (MHDECOD MHCAT MHSCAT) | STUDYID..MHOCCUR; 0 | bbox + 裁图 | U5 3, U6 1 |
| 172 | MH spec 尾 | 12 / 12; `*` 1→1 (MHBODSYS); 脚注 1→1 | MHSTAT..MHENTPT + 脚注; 0 | bbox + 裁图 | U5 4 |
| 178 | §6.2.7 DV spec | 12 / 12; `*` 3→3 (DVDECOD DVCAT DVSCAT) | STUDYID..EPOCH; 0 | bbox + 裁图 | U5 1, U6 1 |
| 179 | DV spec 尾 (无表头) | 4 / 4; 脚注 1→1 | DVSTDTC..DVENDY + 脚注; 0 | bbox (沿用 p178 列界) | |
| 180 | §6.3.1 DA spec | 15 / 15; `*` 2→2 (DACAT DASCAT) | STUDYID..DAORRESU; 0 | bbox + 裁图 | U5 3, U6 1; §6.3 引言非本批 |
| 181 | DA spec 尾 | 12 / 12; 脚注 1→1 | DASTRESC..DADY + 脚注; 0 | bbox | U5 3 |
| 183 | §6.3.2 DD spec | 12 / 12; `*` 1→1 (DDRESCAT); 脚注 1→1 | 全 12 + 脚注; 0 | bbox + 裁图 | U5 3, U6 1 |
| 193 | §6.3.4 IE spec | 18 / 18; `*` 2→2 (IETESTCD IESCAT); 脚注 1→1 | 全 18 + 脚注; 0 | bbox + 裁图 | U5 4, U6 1 |
| 196 | §6.3.5.2 BS spec 首 | 5 / 5 (STUDYID..BSSEQ) | 对应前 5; 0 | bbox (取页上第 2 表头) | 页上半为 §6.3.5.1 通用表 (LB, 非本批); U6 1 |
| 197 | BS spec | 24 / 24; `*` 1→1 (BSANTREG) | BSGRPID..BSDTC 段; 0 | bbox + 裁图 | U5 9 (BSSPEC 双 codelist) |
| 198 | BS spec 尾 | 6 / 6; 脚注 1→1 | BSDY..BSRFTDTC + 脚注; 0 | bbox | |
注: 每页变量数由 `awk '/^####/{d=$2} /^[0-9]+ /{print d,$1}' cmpw_after.txt | sort | uniq -c` 机械生成 (变量起始行所在页).

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after | PDF 页 |
|---|---|---|---|---|---|
| 1 | CE/spec.md:81/90/99/144/162 | pdf:p148-149 CT 列 (CEDECOD CECAT CESCAT CEBODSYS CETOXGR) | REPLACED | CT 空 → `*` ×5 | 148-149 |
| 2 | CE/spec.md:294 | ig34_p0150_a004 | INSERTED | 脚注 `> ¹In this column, …` (`---` 后, Cross References 前; gap F) | 150 |
| 3 | HO/spec.md:90/99 | pdf:p168 CT 列 (HOCAT HOSCAT) | REPLACED | 空 → `*` ×2 | 168 |
| 4 | HO/spec.md:258 | ig34_p0169_a0003 | INSERTED | 脚注 | 169 |
| 5 | MH/spec.md:90/108/117/162 | pdf:p171-172 CT 列 (MHDECOD MHCAT MHSCAT MHBODSYS) | REPLACED | 空 → `*` ×4 | 171-172 |
| 6 | MH/spec.md:249 | ig34_p0172_a0013 | INSERTED | 脚注 | 172 |
| 7 | DV/spec.md:72/81/90 | pdf:p178 CT 列 (DVDECOD DVCAT DVSCAT) | REPLACED | 空 → `*` ×3 | 178 |
| 8 | DV/spec.md:150 | ig34_p0179_a0005 | INSERTED | 脚注 | 179 |
| 9 | DA/spec.md:108/117 | pdf:p180 CT 列 (DACAT DASCAT) | REPLACED | 空 → `*` ×2 | 180 |
| 10 | DA/spec.md:249 | ig34_p0181_a013 | INSERTED | 脚注 | 181 |
| 11 | DD/spec.md:81 | pdf:p183 CT 列 (DDRESCAT) | REPLACED | 空 → `*` | 183 |
| 12 | DD/spec.md:114 | ig34_p0183_a020 | INSERTED | 脚注 | 183 |
| 13 | IE/spec.md:54/81 | pdf:p193 CT 列 (IETESTCD IESCAT) | REPLACED | 空 → `*` ×2 | 193 |
| 14 | IE/spec.md:168 | ig34_p0193_a025 | INSERTED | 脚注 | 193 |
| 15 | BS/spec.md:198 | pdf:p197 CT 列 (BSANTREG) | REPLACED | 空 → `*` | 197 |
| 16 | BS/spec.md:321 | ig34_p0198_a008 | INSERTED | 脚注 | 198 |
- 合计 28 处 (CT `*` 20 + 脚注 8). 脚注文字取自 bbox 原词 (8 页文字相同), 上标 ¹ 照渲染; 格式与 AG/PR/EX/EC 先例一致.

## 结构改动清单
无 (无变量增删/挪位; 无标题改动).

## 删除清单
无 (20 处 REPLACED 的旧值均为空串).

## D6 标注清单
无新增. 8 文件 `> Class|Structure` 行 + Cross References 按 U8 为导航, 不标.

## PDF_TYPO 清单
无. (CEDECOD Notes "Define- XML" = PDF 折行连字符 (p148), 非笔误, KB "Define-XML" 不改.)

## 范围外发现
- 无 KB 内容错. (BS p196 若用原 speccmp.py 会假报 VISITNUM Core "Perm vs Exp" / VISIT Notes 缺句 — 那是 §6.3.5.1 通用表的行, 非 BS; 已用 sc2.py 排除, 供 reviewer 知悉.)
- 工具: `work/scratch/t2s_tools/speccmp.py` 4 个失效模式 (见 "方法"), 其他 spec 批若用原脚本可能漏变量/错表; 修正版在本批 scratch `sc2.py` / `sc2w.py` (未改共享工具).

## out_of_scope 处理 (O15 / O21 / O24 / O26)
- O15 / O26 (spec 表脚注): 本批 8 域全补 → 8 域关闭. spec 首句不属 spec-only 批 (各域 assumptions.md 已终版).
- O24: 本批 8 域 CT `*` 全补 (20); C-code 记法 → U5 S-CT.
- O21 (FA/spec) 不在本批 units, 本批不处理.

## 需主控定
无.

## git diff --stat
 knowledge_base/domains/BS/spec.md |  4 +++-
 knowledge_base/domains/CE/spec.md | 12 +++++++-----
 knowledge_base/domains/DA/spec.md |  6 ++++--
 knowledge_base/domains/DD/spec.md |  4 +++-
 knowledge_base/domains/DV/spec.md |  8 +++++---
 knowledge_base/domains/HO/spec.md |  6 ++++--
 knowledge_base/domains/IE/spec.md |  6 ++++--
 knowledge_base/domains/MH/spec.md | 10 ++++++----
 8 files changed, 36 insertions(+), 20 deletions(-)

## 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC2_writer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
for p in 148 149 150 167 168 169 171 172 178 179 180 181 183 193 196 197 198; do pdftotext -bbox -f $p -l $p "$P" $S/bb_$p.html; done
bash -c 'for a in "CE 148,149,150" "HO 167,168,169" "MH 171,172" "DV 178,179" "DA 180,181" "DD 183" "IE 193" "BS 196,197,198"; do set -- $a; python3 -I '$S'/sc2w.py '$S' $1 $2; done'
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```
