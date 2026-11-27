# T4.1 补检结果 — 包 7/8 (RULE_T1-two-agent+T2-rework, 终态 EQUIVALENT, #160-184)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T04:52:26Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`; 样本包: `.work/10_tier_b_repair/work/t4/supp/supp_pack_7.md`
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 带 pages): p32, p71, p152, p153
- 文本层: `ig34_p0032.txt`, `ig34_p0071.txt`, `ig34_p0072.txt`, `ig34_p0073.txt` (CRACE05 行), `ig34_p0152.txt`, `ig34_p0153.txt` (均在 `.work/10_tier_b_repair/work/pdf_pages/`); p69/70/74 用于确认 DM Example 4 的页范围
- 用过的命令:
  - `cat .work/10_tier_b_repair/work/pdf_pages/ig34_p015{2,3}.txt`; `sed -n 1,45p .../ig34_p0032.txt`; `cat .../ig34_p0071.txt`; `sed -n 1,70p .../ig34_p0072.txt`
  - `python3` 读 `archive/deep_verification/pdf_atoms.jsonl` 列 p152/p153 全部原子 (用来确定同名选项 "Unknown" / "o No" / "o Severe" 各原子对应 CRF 的哪一行)
  - `python3` 读 `.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl` 查样本行
  - `cat -n knowledge_base/domains/CE/examples.md | sed -n 30,100p`
  - `grep -n -i "Indication for analgesic\|Post-operative pain\|Toothache\|Menstrual" knowledge_base/chapters/ch04_general_assumptions.md`; `sed -n 405,460p` 同文件
  - `grep -n -i "study participant answered\|CRACE05\|Check all that apply\|RACEC codelist\|BANGLADESHI" knowledge_base/domains/DM/*.md`; `sed -n 105,180p knowledge_base/domains/DM/examples.md`
  - `grep -n "Example\|aCRF\|CRACE05" .../ig34_p00{69,70,73,74}.txt`

原子对应关系 (按 `pdf_atoms.jsonl` 顺序, 与渲染页逐行核对):
- p152 CRF: a0004-0006 = Nausea 行 (Yes/Mild; No/(dd)/Moderate; Severe); a0007-0009 = Vomit 行; a0010-0012 = Diarrhea 行; a0013-0015 = "Other, Specify:" 行 (该行无 Yes/No, a0014 = 两个 (dd/mmm/yyyy) + Moderate, a0015 = Severe).
- p153 CRF: a0006-0009 = How did fracture occur? 四项; a0011-0013 = laterality 三项; a0014-0016 = Were therapeutic measures required? (Yes/No/**Unknown**); a0017-0019 = therapeutic measures 复选三项; a0020-0022 = Were there any complications? (Yes/No/**Unknown**); a0023-0025 = complications 复选三项.
- 所以包里 #166/#167/#169/#170/#171/#172/#179/#181 的 KB 指针 (CE examples.md:43 / :77) 是错位的, 下表填的是实际对应行.

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| 160 | `ig34_p0032_a014` | RULE_T1-two-agent+T2-rework | EQUIVALENT | HOLDS | 渲染页 p32 + `ig34_p0032.txt:20-26`; `knowledge_base/chapters/ch04_general_assumptions.md:425-432` | 信息点: 标签 "Indication for analgesic"; 6 个单选项 Post-operative pain / Headache / Menstrual pain / Myalgia / Toothache / "Other, specify: ____". KB 全部 6 项、顺序一致、单选符号 ○; 差异仅版式 (标签单独占表头行, 选项分行; "Other," 与 "specify:" 合一行; 下划线长度). 位置: §4.2.7.1 正文 "For example, consider a CRF ... (CMINDC)" 段之后, 正确. 包里指针 :400 偏了 |
| 161 | `ig34_p0071_a002` | 同上 | EQUIVALENT | HOLDS | 渲染页 p71 (整页为 CRF 截图, 文本层只有 4 行 "If the study participant answered" 小标题); `knowledge_base/domains/DM/examples.md:135,153,170,190` | p71 ASIAN 面板信息点: ① 完成说明 "Select each value that applies if the subject answered "ASIAN". Check all that apply." ② 问题 "Which of the following racial designations best describes you?" ③ CRACE05-CRACE10 ④ 注释 "For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value." ⑤ 复选框 ASIAN AMERICAN / ASIAN INDIAN / BANGLADESHI / CHINESE / JAPANESE / KOREAN ⑥ <RACEC codelist>. KB Example 4 (p70 起, 与 PDF 同例) 内: :190 逐字含 ①②③④ + (RACEC) + 6 个值 + checkbox; :135 Mermaid SC2 含 CRACE05-10→SUPPDM.QVAL 和 6 个 ☐ 选项 (与图不矛盾); :153 小标题; :170 KB note 复述. 无丢失、值一致 |
| 162 | `ig34_p0152_a0004` | 同上 | EQUIVALENT | HOLDS | 渲染页 p152 + `ig34_p0152.txt:6`; `knowledge_base/domains/CE/examples.md:43` | Nausea / ○ Yes / 起止日期空格 2-3-4 位 (`__/___/____`) / ○ Mild 全在; KB 把同格多行合到一行 |
| 163 | `ig34_p0152_a0005` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:7`; `CE/examples.md:43` | ○ No、两个 "(dd/mmm/yyyy)"、○ Moderate 均在 Nausea 行 |
| 164 | `ig34_p0152_a0006` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:8`; `CE/examples.md:43` | ○ Severe 在 Nausea 行 Severity 格 |
| 165 | `ig34_p0152_a0007` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:9`; `CE/examples.md:44` | Vomit / ○ Yes / 两个日期空格 / ○ Mild |
| 166 | `ig34_p0152_a0008` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:10`; `CE/examples.md:44` | Vomit 行的 ○ No、两个 (dd/mmm/yyyy)、○ Moderate. 包里指针 :43 错位, 实际对应 :44 |
| 167 | `ig34_p0152_a0009` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:11`; `CE/examples.md:44` | Vomit 行 ○ Severe. 包指针 :43 错位 |
| 168 | `ig34_p0152_a0010` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:12`; `CE/examples.md:45` | Diarrhea / ○ Yes / 两个日期空格 / ○ Mild |
| 169 | `ig34_p0152_a0011` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:13`; `CE/examples.md:45` | Diarrhea 行 ○ No、两个 (dd/mmm/yyyy)、○ Moderate. 包指针 :43 错位 |
| 170 | `ig34_p0152_a0012` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:14`; `CE/examples.md:45` | Diarrhea 行 ○ Severe. 包指针 :43 错位 |
| 171 | `ig34_p0152_a0014` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:16` (渲染页确认该行第 2 列无 Yes/No); `CE/examples.md:46` | "Other, Specify:" 行: 两个 (dd/mmm/yyyy) + ○ Moderate; KB :46 同, 且同样不带 Yes/No (与 PDF 一致). 包指针 :43 错位 |
| 172 | `ig34_p0152_a0015` | 同上 | EQUIVALENT | HOLDS | p152 `ig34_p0152.txt:17`; `CE/examples.md:46` | "Other, Specify:" 行 ○ Severe. 包指针 :43 错位 |
| 173 | `ig34_p0153_a0006` | 同上 | EQUIVALENT | HOLDS | 渲染页 p153 + `ig34_p0153.txt:6`; `CE/examples.md:77` | "How did fracture occur?" + ○ Pathologic (单选 ○, 与 PDF 同) |
| 174 | `ig34_p0153_a0007` | 同上 | EQUIVALENT | HOLDS | p153 `:7`; `CE/examples.md:77` | ○ Fall, 同一问题下 |
| 175 | `ig34_p0153_a0008` | 同上 | EQUIVALENT | HOLDS | p153 `:8`; `CE/examples.md:77` | ○ Other trauma |
| 176 | `ig34_p0153_a0011` | 同上 | EQUIVALENT | HOLDS | p153 `:11`; `CE/examples.md:79` | "What was the laterality?" + ○ Left |
| 177 | `ig34_p0153_a0012` | 同上 | EQUIVALENT | HOLDS | p153 `:12`; `CE/examples.md:79` | ○ Right |
| 178 | `ig34_p0153_a0013` | 同上 | EQUIVALENT | HOLDS | p153 `:13`; `CE/examples.md:79` | ○ Not applicable |
| 179 | `ig34_p0153_a0016` | 同上 | EQUIVALENT | HOLDS | p153 `:16` (Were therapeutic measures required? 的第 3 项); `CE/examples.md:80` | ○ Unknown 在 "Were therapeutic measures required?" 下, KB :80 有. 包指针 :77 (fracture occur 的 Unknown) 错位 |
| 180 | `ig34_p0153_a0018` | 同上 | EQUIVALENT | HOLDS | p153 `:18`; `CE/examples.md:81` | □ Traction (复选), KB 用 □ 与 PDF 一致. 原子 verbatim 写 "o Traction" (单选符) 与 PDF 不符, 属抽取物瑕疵, KB 按 PDF 写对 |
| 181 | `ig34_p0153_a0022` | 同上 | EQUIVALENT | HOLDS | p153 `:22` (Were there any complications of the fracture? 第 3 项); `CE/examples.md:82` | ○ Unknown 在 complications 问题下, KB :82 有. 包指针 :77 错位 |
| 182 | `ig34_p0153_a0023` | 同上 | EQUIVALENT | HOLDS | p153 `:23`; `CE/examples.md:83` | 问题文本逐字 + □ Infection of fracture site. 原子写 "o" 而 PDF 是 □, KB 用 □ 正确 |
| 183 | `ig34_p0153_a0024` | 同上 | EQUIVALENT | HOLDS | p153 `:24`; `CE/examples.md:83` | □ Improper healing requiring bone reset (原子 "o" 同上) |
| 184 | `ig34_p0153_a0025` | 同上 | EQUIVALENT | HOLDS | p153 `:25`; `CE/examples.md:83` | □ Soft tissue damage, specify location + 填写横线 (PDF `______` 6 位, KB `___`, 仅空格长度). 原子 "o" 同上 |

## 计数

| 层 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 合计 |
|---|---|---|---|---|---|
| RULE_T1-two-agent+T2-rework | 25 | 0 | 0 | 0 | 25 |

层通过 (NOT_HOLD 0, UNVERIFIABLE 0).

## 样本外发现

KB 内容问题: 无.

非 KB 的记录项 (只记录, 不改):
- 台账 `.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl` 里部分样本的 `md_atom_ids` 指向别的域: `ig34_p0153_a0009/a0016/a0022` → `md_dmDM_ex_a182`, `ig34_p0153_a0018` → `md_dmEX_ex_a040`, `ig34_p0152_a0015` → `md_ch10_a109`. 实际承载位置是 `knowledge_base/domains/CE/examples.md:43-46,77-83`. 看起来是 06 旧匹配留下的 id, 本项目改标时没重写. 不影响本包判定.
- p153 "If ... select all that apply" 下的复选项, 原子 verbatim 一律写成 "o" (单选符), PDF 是 □ (#180, #182-184 以及未抽中的 a0017/a0019). KB 用 □, 是对的.
