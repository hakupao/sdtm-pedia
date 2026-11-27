# T4.1 补检 pack 8/8 — RULE_live-hit(was-IE-ack) 审查结果 (19 条, 全检)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读角色
- 时间: 2026-11-27T04:52:42Z (`date -u` 实测)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`; 样本包: `.work/10_tier_b_repair/work/t4/supp/supp_pack_8.md`
- 看过的渲染页: `source/cdisc/SDTMIG v3.4 (no header footer).pdf` p63 (DM RACE 行) / p150 (CE 脚注) / p195 (LB 通用规格表头); `source/cdisc/SDTM_v2.0.pdf` p64 (RELREC 表 APID 行)
- 用过的命令 (可复跑):
  - `grep -rn "In this column, an asterisk" knowledge_base/domains/{DM,SM,AE,CE,MH,DD,IE,CV,NV,RE,FT}/spec.md` (KB 脚注行号)
  - `grep -n "^\(su\|ae\|ce\|dd\|eg\)\.xpt" knowledge_base/domains/{SU,AE,CE,DD,EG}/assumptions.md`
  - `grep -n "(RACE)" knowledge_base/domains/DM/spec.md`; `grep -n "| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format" knowledge_base/domains/LB/*.md`
  - `grep -n -B1 "In this column, an asterisk" .work/10_tier_b_repair/work/pdf_pages/ig34_pNNNN.txt` (11 页 PDF 脚注定位)
  - 逐字比对脚本 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/supp8/cmp.py` (`python3 -I cmp.py`, 归一只做: 空白折叠、`¹/²`→`1/2`、去 `>` 引用符 / `**` / `|`、弯直引号; PDF 脚注 "1\n In" 拼接为 "1In"): 16 条句子 / 脚注全部 `EQ`
  - sv20 p64 APID 行: 取文本层 39-43 行第 129 列起 (Notes 列) 拼接, 与 `knowledge_base/model/06_relationship_datasets.md:40` 第 6 格比对 → `True`
  - 各 PDF 页节归属: `grep -E '^[A-Z]{2} – ' ig34_pNNNN.txt` 及页内变量前缀 (DMDTC / AESTDTC / CESTTPT / MHSTAT / EGSEQ / CVDTC / NVRFTDTC / RERFTDTC / FTSTRESU)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| 185 | `ig34_p0063_a022` | RULE_live-hit(was-IE-ack) | EXACT | HOLDS | `ig34_p0063.txt:44` + 渲染页 p63 RACE 行 Controlled Terms 格 = `(RACE)`; `knowledge_base/domains/DM/spec.md:198` (### RACE 块内) `(RACE) C74457` | `(RACE)` 逐字, 位于 DM RACE 变量块. 后缀 `C74457` 是 KB 附加的 NCI 码, 已由 `DM/spec.md:298` KB note 声明 "not in SDTMIG", 不改原值 |
| 186 | `ig34_p0064_a011` | 同上 | EXACT | HOLDS | `ig34_p0064.txt:38-39` (DM 规格末页, DMDTC 行后); `knowledge_base/domains/DM/spec.md:294` | 脚注逐字 (cmp EQ), 在 DM 规格表后 |
| 187 | `ig34_p0084_a018` | 同上 | EXACT | HOLDS | `ig34_p0084.txt:36-37` (§5.4 SM 规格); `knowledge_base/domains/SM/spec.md:96` | 逐字, 位置对 |
| 188 | `ig34_p0129_a005` | 同上 | EXACT | HOLDS | `ig34_p0129.txt:6` (SU – Specification 下); `knowledge_base/domains/SU/assumptions.md:9` (## SU – Specification 下) | 逐字, 位置对 |
| 189 | `ig34_p0134_a002` | 同上 | EXACT | HOLDS | `ig34_p0134.txt:2`; `knowledge_base/domains/AE/assumptions.md:21` (## AE – Specification 下) | 逐字, 位置对 |
| 190 | `ig34_p0137_a010` | 同上 | EXACT | HOLDS | `ig34_p0137.txt:27-28` (AE 规格末, AEDUR 等行后); `knowledge_base/domains/AE/spec.md:546` | 逐字, 位置对 |
| 191 | `ig34_p0148_a017` | 同上 | EXACT | HOLDS | `ig34_p0148.txt:23`; `knowledge_base/domains/CE/assumptions.md:9` (## CE – Specification 下) | 逐字, 位置对 |
| 192 | `ig34_p0150_a004` | 同上 | EXACT | HOLDS | `ig34_p0150.txt:12` + 渲染页 p150 (CE 表下脚注); `knowledge_base/domains/CE/spec.md:294` | 逐字, 位置对 |
| 193 | `ig34_p0172_a0013` | 同上 | EXACT | HOLDS | `ig34_p0172.txt:37-38` (MH 规格末); `knowledge_base/domains/MH/spec.md:249` | 逐字, 位置对 |
| 194 | `ig34_p0183_a006` | 同上 | EXACT | HOLDS | `ig34_p0183.txt:9`; `knowledge_base/domains/DD/assumptions.md:11` (## DD – Specification 下) | 逐字, 位置对 |
| 195 | `ig34_p0183_a020` | 同上 | EXACT | HOLDS | `ig34_p0183.txt:39-40` (DD 规格表下); `knowledge_base/domains/DD/spec.md:114` | 逐字, 位置对 |
| 196 | `ig34_p0185_a022` | 同上 | EXACT | HOLDS | `ig34_p0185.txt:27-28` (跨行, 拼接后一致); `knowledge_base/domains/EG/assumptions.md:9` (## EG – Specification 下) | 逐字, 位置对 |
| 197 | `ig34_p0193_a025` | 同上 | EXACT | HOLDS | `ig34_p0193.txt:44` (IE 规格表下); `knowledge_base/domains/IE/spec.md:168` | 逐字, 位置对 |
| 198 | `ig34_p0195_a008` | 同上 | EXACT | HOLDS | `ig34_p0195.txt:14-15` + 渲染页 p195 表头 7 格; `knowledge_base/domains/LB/assumptions.md:20` (§6.3.5.1 通用规格表, 紧随 `--.xpt, Generic Specimen-Based ...` 标题) | 7 格逐格一致: Variable Name / Variable Label / Type / Controlled Terms, Codelist or Format¹ / Role / CDISC Notes / Core (PDF 上标 1 ↔ KB `¹`); 位置为 §6.3.5.1 所在 KB 文件 |
| 199 | `ig34_p0288_a018` | 同上 | EXACT | HOLDS | `ig34_p0288.txt:41` (CV 规格末, CVDTC 等行后); `knowledge_base/domains/CV/spec.md:384` | 逐字, 位置对 |
| 200 | `ig34_p0296_a005` | 同上 | EXACT | HOLDS | `ig34_p0296.txt:10` (NV 规格末 NVRFTDTC 行后); `knowledge_base/domains/NV/spec.md:384` | 逐字, 位置对 |
| 201 | `ig34_p0310_a005` | 同上 | EXACT | HOLDS | `ig34_p0310.txt:14-15` (RE 规格末 RERFTDTC 行后); `knowledge_base/domains/RE/spec.md:429` | 逐字, 位置对 |
| 202 | `ig34_p0320_a023` | 同上 | EXACT | HOLDS | `ig34_p0320.txt:51` (FT 规格末); `knowledge_base/domains/FT/spec.md:348` | 逐字, 位置对 |
| 203 | `sv20_p0064_a020` | 同上 | EXACT | HOLDS | `sv20_p0064.txt:39-43` + 渲染页 SDTM v2.0 p64 (RELREC 表 APID 行); `knowledge_base/model/06_relationship_datasets.md:40` (§6.1 RELREC Dataset 表) | 逐格: # `4` / Variable Name `APID` / Label `Associated Persons Identifier` / Type `Char` / Role `Identifier` / Notes 全文逐字 (渲染页确认该文字在 Notes 列, KB 放在 Notes 列). PDF 其余 6 列 (Format, Variable(s) Qualified, Usage Restrictions, Variable C-code, Definition, Examples) 本行均为空, KB 表结构不设这些列; 无非空值丢失, 故判 HOLDS. 位置: SDTM v2.0 §6.1 对应的 model 文件, 正确 |

## 计数

| 层 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|---|
| RULE_live-hit(was-IE-ack) | 19 | 0 | 0 | 0 |
| 合计 | 19 | 0 | 0 | 0 |

层通过条件 (NOT_HOLD 0 且 UNVERIFIABLE 0): 满足.

## 样本外 KB 内容观察

- `knowledge_base/model/06_relationship_datasets.md:37,39` (RELREC 表 STUDYID / USUBJID 行) 未承载 SDTM v2.0 p64 的 Variable C-code (`C83082` / `C69256`) 和 Definition 列文字; USUBJID 的 Notes 为 KB 自写 (文件 KB note 已声明). 台账已有记录: `sv20_p0064_a017` / `sv20_p0064_a019` 为 INTENTIONAL_EXCLUDE (VERSION_MISMATCH; ruling:R1-row), 非新问题, 仅提示. 其它: 无.
