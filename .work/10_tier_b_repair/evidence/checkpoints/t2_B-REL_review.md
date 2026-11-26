# T2 B-REL — reviewer

## attempt 1 (oh-my-claudecode:code-reviewer / opus, 2026-11-26)

**verdict: CONDITIONAL** (1 项同文件移位; 其余全部通过)

审的是终态 (writer 续之后): 9 文件 md5 = checkpoint 表 (RELREC/assumptions = ae6ed604546ffa52974ade20e82aade8, 其余 8 个同 after 列). 未改 KB.

### 命令 (S = scratchpad/t2_B-REL_reviewer, 仓外)
| 命令 | 结果 |
|---|---|
| `table_census.py --manifest $S/manifest.json` (3 个 examples.md × ig34 427-440) | exit 1 (全局 PDF_ONLY 332 致 RED); 本批 KB 表 7 张 status **OK ×7**, cells 232, diffs **0**; 本批页 PDF_ONLY 0, pdf_unparsed 不在 427-440 |
| `fp_match.py --baseline work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | 全局 RESULT RED, 回归 48 条, 页码集 {118,174,215,218,254,257,258,260,262,263,363,364,370,373,374,396} — **p427-440 回归 0** |
| `python3 tools/check_links.py \| grep live` | live docs: **42** (写本文件 + trace 后复跑见末行) |
| `$S/xc.py` 反向: 9 文件逐行切句/逐格 → PDF p427-440 文本 + ch08 | PDF 缺 = H1/Source/KB note/导航标题/`> Class` 行/C-code/Cross References/Mermaid 体 + T-9 句号; spec 行级 "-C" 为 PDF 版面跨列打散, 已对渲染逐格核 (下表) |
| `$S/fw2.py` 正向: PDF §8 引言 IDVAR 段 + p429-431(至 8.4 前) + p437(8.7 起)-440, 按段切句 → 9 文件 | 残余仅 = PDF 节号标题 (8.2/8.2.1/8.2.2/8.3/8.3.1/8.7/8.8, 其后正文均命中)、spec 表跨列碎片 (渲染核过)、脚注 ¹ (O24 延后). **叙述句缺失 0** |
| `git diff HEAD --stat -- knowledge_base/` | REL 9 文件外: ch01 / SR×3 / TA×2 / FA/assumptions (+2 行 = SR 指针, 属 B-SR) — 均他批在途, 本批无白名单外改动 |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| RELREC/assumptions.md:17-22 | 4 位置 / 同文件顺序 | §8 引言 IDVAR 段+3 条 (p427) 位于 `## Relating Peer Records` (§8.2) 下、§8.2 正文之后. PDF 顺序 §8 引言 → §8.2; 同文件已对 §8.2 首两段做过移位, 同口径应移. KB note 只是说明, 不替代归节 | p427 "All relationships make use of the standard domain identifiers STUDYID, DOMAIN, and USUBJID." 位于 §8.1/§8.2 之前 |

**CONDITIONAL 修正清单 (writer attempt 2)**
1. RELREC/assumptions.md: 把 :17 (KB note) + :19-22 (引言段 + 3 bullet) 整块移到 :3 Source 行之后、:5 `## Relating Peer Records` 之前; 文字不改; KB note 可保留 (建议去掉 ", not from §8.2" 或改为 "…§8 introduction (p427)"). 记 RELOCATE (同文件), 不留指针. 移后 reviewer 复审 delta.

### 判定 (主控点名项)
- (1) Source 行: RELREC/assumptions §8 (intro), §8.2, §8.2.1, §8.3, §8.3.1 / examples §8.2.2, §8.3.1 / spec §8.2.1 / RELSUB×3 §8.7 / RELSPEC×3 §8.8 — 与 PDF 标题逐一相符 ✓.
- (2) 逐字: 两个 "(as described in this section)" / "(as described in Section 8.3, Relating Datasets)" ✓ (p429); IDVAR 引言段 + --SEQ / --REFID / --GRPID 三条全文 ✓ (p427, 含 "Within a Domain Using the --GRPID Variable"); D6 note 措辞合规 ✓; "Because IDVAR identifies the keys…not across datasets." ✓ (p431); 3 域 Description 句 + spec 首句 ✓ (p429/437/438/439); RELTYPE 三项去粗体、仅 NO/IS 粗体 = 渲染 p431 ✓; RELSUB "The relationship of the mother" ✓ (p439); RELSPEC 图题 "Figure. Sample Specimen Relationship" ✓ + D6 ✓; T-7 "therefore is does not" 照录 = ch08 ✓.
- (3) RELOCATE §8.2 首两段到 `## Relating Peer Records` 下: 文字与 before 逐字同 (仅括注已改为 PDF), 无指针, 锚点未变 ✓. RELTYPE 组合段 + "Because IDVAR…" 放 assumptions `## Relating Datasets` 下 §8.3 两段之后: 同文件内顺序 = PDF §8.3 → §8.3.1 剩余部分; Source 行已声明 §8.3.1; §8.3.1 Example 1 表 + 操作库段在 examples.md 逐字 → **可接受, 不阻断** (跨文件搬动需另授权且收益小).
- (5) 与 ch08 差异 (均有解释, 文字层面无冲突): ① 标题破折号: 域文件 `RELREC – …` en dash (= PDF 与 CM/IS 域先例), ch08 `**RELREC — …**` em dash — 纯格式; PDF 自身 "RELREC - Description/Overview" 用连字符而 Specification 用 en dash, KB 统一 en dash 可接受 (LOW). ② Mermaid: 域文件层级用 subgraph 标题, ch08 标在节点内; D6 措辞相应为 "subgroup titles" vs "inside the nodes" — 两者节点/边 (SPC-001→A,B; B→B-1; SPC-003→A) 均 = p440 图 ✓. ③ RELSUB item 7 句号 (T-9) 与 ch08 同. ④ Ex3 正文弯引号 "COMBO 1" → KB/ch08 均直引号, 同; "COMBO 1" vs 表 "COMBO1" 为 PDF 自身不一致, 照录.
- (7) fp p427-440 回归 0; live docs 42 ≤ 42 ✓. O24 (spec 记法 / 脚注 ¹) 已延后, 不判.

### 人工逐格 (渲染 p429/430/431/438/439/440 目视, 独立于 census bbox)
| 表 | 行 | 结果 |
|---|---|---|
| RELREC Ex1 relrec (p430) | R1-6 (STUDYID..RELID, RELTYPE 空) | 一致 |
| RELREC Ex2 relrec (p430) | R1-5 | 一致 |
| RELREC Ex3 relrec (p430) | R1-4 (R2 CMGRPID/COMBO1) | 一致 |
| RELREC 8.3.1 relrec (p431) | R1 TU/TULNKID/ONE/1; R2 TR/TRLNKID/MANY/1; USUBJID/IDVARVAL 空 | 一致 |
| RELSUB dm (p439) | R1-3 | 一致 |
| RELSUB relsub (p439) | R1-6 | 一致 |
| RELSPEC relspec (p440) | R1-6 (R1/R5 PARENT 空) | 一致 |
| RELREC spec (p429) | 7 变量 × Label/Type/CT/Role/Core/Notes | 一致 (CT: (DOMAIN)=C66734, (RELTYPE)=C78737; IDVAR "*" → 空 = O24) |
| RELSUB spec (p438) | 5 变量 | 一致 (SREL (RELSUB)=C100130) |
| RELSPEC spec (p439) | 6 变量 | 一致 (SPEC (SPECTYPE)(GENSMP)=C78734; C111114) |
| Structure 行 ×3 | `> Class … Structure:` vs spec 首句 | 一致 |

### R2 recheck
本批 `t2_recheck[]` 为空; 全扫中未发现改写丢短语 (除已修的 2 处括注 / 3 条截断 bullet).

### G-TB6 结构行签字 (KB 自写导航, 保留)
- 9 个 `> Source text: …` 行 (D7) ✓
- 新增标题: RELREC/RELSUB/RELSPEC `– Description/Overview` / `– Specification`, RELSUB/RELSPEC `– Assumptions` = PDF 标题 ✓
- 导航标题保留 (代 PDF 标题): `## Relating Peer Records` (§8.2)、`## Relating Datasets` (§8.3)、`## Peer Record Examples` (§8.2.2 RELREC Dataset Examples)、`## Dataset Relationship Example` (§8.3.1)、`### Example n` / `## Example 1`; RELSUB/RELSPEC examples 无 "– Examples" 标题 = CM 域先例 ✓
- 表前 `**relrec.xpt**` 等、`**Row n:**` 标签; spec.md `### VAR` 块 / `## Cross References` (全库格式) ✓
- KB note ×2 (RELREC/assumptions:17, RELSPEC/examples:11) 前缀合规 ✓

check_links 复跑 (写完本文件与 trace 后): `broken relative links: 18668 (live docs: 42)`

## 续 签字 (reviewer, 复审 writer「attempt 1 续 2」delta)
- RELREC/assumptions.md md5 → 69882fb2c0d1772d33c21ca7f61dc1ee (46 行); 其余 8 文件 md5 未变.
- 修正 1 已落实: KB note :5 (已去 ", not from §8.2") + §8 引言段 :7 + 3 bullet :8-10 位于 Source 行后、`## Relating Peer Records` (:12) 前 = PDF 顺序 p427 §8 引言 → p429 §8.2 ✓; 标题顺序 :12 §8.2 → :24 Description → :28 Specification → :32 §8.3 → :40-46 §8.3.1 余段 ✓.
- 反向扫 `$S/xc.py`: RELREC/assumptions 无出处行仅 H1/Source/KB note; 正向扫 `$S/fw2.py` 叙述缺失 0.
- `fp_match.py … --regress-out $S/fp2_regress.jsonl` → 全局 RED 48 条, p427-440 回归 0; `check_links.py | grep live` → live docs: 42.
- **终态签字: PASS** (B-REL 9 文件; O24 延后不判).
