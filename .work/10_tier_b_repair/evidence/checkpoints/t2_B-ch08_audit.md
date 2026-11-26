# T2 B-ch08 auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 判定对象: `knowledge_base/chapters/ch08_relationships.md` md5 `154743c22e466e03124bdd18a7b34b95` (= reviewer 续 签字 md5); diff vs bdb54fe +94/−91.
- 真值: `work/pdf_pages/ig34_p0427-0440.txt` + 渲染 `pdftoppm -f N -l N -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf"` (p428/436/437/438/440, Read 目视).
- 顺序: 先独立判 (抽样 + 双向扫 + 渲染格 + 删除核), 判完才读 writer checkpoint / review.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch08_auditor/` (sample.json, supp_sample.txt, bidir.py, fp_after.jsonl, fp_regress.jsonl, p*.png)

### 1. 抽样 (prompt v1.0 命令原样, batch_id=B-ch08, seed=20261126)
→ `{"C": 3, "P": 40, "N": 10}`; 样本 = C 3 (a018, a019, a010) + P−C 7.
另: 本批 R3 新增 44 原子 (writer 清单) 中再 seeded 补抽 10 (`random.Random(20261126).sample(R3−主样本, 10)`, 池 42), 原子 verbatim 归一化子串 vs ch08 全文 + 人工复读.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0427_a018 | p427 L23-27 --SEQ bullet (DM 例外, 25 AE→25 AESEQ, sponsor-defined, 未必连续) | ch08:20 | 否 | 是 | 是 (§8 intro) | 5 句全在, R2 短语已恢复 |
| 2 | ig34_p0427_a019 | p427 L28-31 --REFID bullet (electronic data transfer; 例 lab-specimen/ECG; Perm 非 Req; alphanumeric) | ch08:21 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0427_a010 | p427 L15-17 §8.6 bullet (separate domain vs SUPP; findings about other GOC) | ch08:14 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0427_a007 | p427 L8-9 §8.3 bullet (2+ datasets 关系) | ch08:11 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0427_a024 | p428 L5-6 §8.1 "same unique character value to --GRPID" | ch08:28 | 否 | 是 | 是 (§8.1) | 逐字 (atom 页号记 427, 实在 p428) |
| 6 | ig34_p0427_a026 | p428 L8-9 "--GRPID no inherent meaning across subjects/domains" | ch08:28 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0427_a017 | p427 L22 "examples of variables that could be used in IDVAR:" | ch08:18 | 否 | 是 | 是 | 逐字; 顺序 = PDF |
| 8 | ig34_p0433_a034 | p433 例2 "IDVARVAL has values for 2 questionnaires—BPI / ADAS-Cog—2 subjects" | ch08:237 | 否 | 是 | 是 (§8.4.3) | 仅破折号两侧空格 / en dash→hyphen |
| 9 | ig34_p0427_a008 | p427 L10-13 §8.4 bullet (DM / general observation-class record(s)) | ch08:12 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0427_a016 | p427 L21 "specific set of identifiers … following sections" | ch08:18 | 否 | 是 | 是 | 已移回 PDF 顺序 |
| S1 | ig34_p0438_a004 | p438 relsub.xpt 首句 "One record per relationship per related subject per subject" | ch08:349 | 否 | 是 | 是 | 逐字 |
| S2 | ig34_p0438_a001 | p438 标题 "RELSUB – Specification" | ch08:347 | 否 | 是 | 是 | em dash (文件惯例) |
| S3 | ig34_p0427_a009 | p427 §8.5 bullet (see also Section 5.1; AE 例) | ch08:13 | 否 | 是 | 是 | 逐字 |
| S4 | ig34_p0427_a021 | p428 §8.1 标题 "…Using the --GRPID Variable" | ch08:26 | 否 | 是 | 是 | 逐字 |
| S5 | ig34_p0434_a011 | p434 §8.4.4 bullet 2 (EGTESTCD="INTP", see 4.5.5) | ch08:255 | 否 | 是 | 是 | 逐字 |
| S6 | ig34_p0434_a013 | p434 §8.4.4 bullet 4 (separate GOC / special-purpose) | ch08:257 | 否 | 是 | 是 | 逐字 |
| S7 | ig34_p0433_a011 | p433 §8.4.2 "SUPPQUAL … introduced in SDTMIG v3.1 was deprecated" | ch08:222 | 否 | 是 | 是 | 逐字 |
| S8 | ig34_p0438_a019 | p438 RELSUB 假设 7 (2 directional relationships) | ch08:369 | 否 | 是 | 是 | 逐字 (KB 末加句号, 已登记) |
| S9 | ig34_p0430_a016 | p430 "Example 2 is the same scenario as Example 1." | ch08:121 | 否 | 是 | 是 | 逐字 |
| S10 | ig34_p0437_a017 | p437 RELSUB Desc "pregnant women … most common case" | ch08:345 | 否 | 是 | 是 | 逐字 |

**独有丢失 0/10 (补抽 0/10); 忠实度错 0.**

### 2. 独立双向扫 (`python3 -I $S/bidir.py`, p427-440 全文 vs ch08 全文件, 归一化引号/破折号/空白)
- KB→PDF 未命中 (全部可归类, 无自造): 文件标题/Source 行 (导航); :15 "DIZYGOTIC" (PDF p427 "DIZOGOTIC", 同 PDF p439 表 = DIZYGOTIC, T-1); :40 CMGRPID (PDF "GMGRPID", T-2); :222 "SQAPFAMH)" (T-3); :226 "illustrate" (T-4); :237 "Example 2:" (T-5); :158/:228 "**Example 1:**" 标签内联 (PDF 独立行, 格式); 4 处 `^1^` 脚注 (上标 1); :443 D6 KB note + Mermaid.
- PDF→KB 未命中: 全部为表格版面拼行 / 跨页表头 / 标题与正文粘连 / "o" 子项 / T-2·T-4·T-6 等已登记 typo; 无叙述句缺失.
- 注: T-7 (:434 "therefore is does not") / T-8 (:317 "represent as an event") 现照录 PDF, 双向均命中, 已列 T4 用户裁定.

### 3. 10 随机格 (seeded `random.Random(20261126).sample(cm 12×11 ∪ RELSUB spec 5×6 ∪ Question 表 6×2, 10)`) vs 渲染
| 格 | KB | 渲染 | 结果 |
|---|---|---|---|
| cm Row12 STUDYID | 1234 | p428 1234 | ✓ |
| cm Row11 CMSEQ | 5 | 5 | ✓ |
| cm Row1 CMDOSU | mg | mg | ✓ |
| RELSUB SREL Role | Record Qualifier | p438 Record Qualifier | ✓ |
| Q表 行5 Interp | Yes→traditional Events record / No→multiple time-based → FA | p437 同 | ✓ |
| cm Row2 CMSTDTC | 2004-01-17 | 2004-01-17 | ✓ |
| cm Row7 CMDOSU | mg | mg | ✓ |
| cm Row8 CMDECOD | Generic Med H | Generic Med H | ✓ |
| Q表 行1 Interp | Yes→finding (about the event) / No→inconclusive | p436 同 | ✓ |
| cm Row6 USUBJID | 1234 | 1234 | ✓ |
另目视全表: cm.xpt 12×12、RELSUB spec 5×7 (label "Subject Relationship", CT (RELSUB)) 、Question 表 6 行 (含 p437 续页 "A "No" answer is inconclusive. This does not rule out…" 归行 4) 与渲染一致.

### 4. 删除核 (git diff bdb54fe 的 − 行逐条)
- "### Key Rules" 4 条 bullet → 内容全部在 ch08:212/214/216/218 (PDF p433 四段), 仅去伪小标题 + 恢复 "the key variables"; 无 PDF 内容丢失.
- 旧 §8.4.2 段 (SDTMIGv3.1 / 无 URL) → 由 ch08:222 PDF 全文替换 (含 URL); §8.4.2 内重复 "See Section 4.5.3 …" 段删除, 原段保留于 §8.4.1 后 ch08:216 (PDF p433 仅此一处).
- 旧 overview / IDVAR bullets、Example 2/3 改写句、§8.6.2 碎段、Question 表、RELSUB 4 列简表、"**Note:**" 标签、"**ONE and ONE.**" 粗体: 均被 PDF 原文超集替换; 旧 RELSUB label "…to Related Subject/Pool" 与 PDF 矛盾, 删除正确.
- 旧 Source "Pages 427-446" → 427-440: p441 首行 "9 Study References", 正确.
→ 删除丢失 PDF 内容 0.

### 5. Mermaid vs p440 图
渲染: SPC-001(Tissue) L1 → SPC-001-A(Tissue), SPC-001-B(Tissue) L2; SPC-001-B → SPC-001-B-1(DNA) L3; SPC-003(Brain) L1 → SPC-003-A(RNA) L2. KB :446-450 分支/层级/类型一致; :443 D6 前缀 `> KB note (not in SDTMIG):` + "KB rendering of the PDF figure" ✓. 图 "(Brain)" vs relspec Row5 "TISSUE" 为 PDF 内部不一致, 两处各自照录 ✓.

### 6. 回归 / 链接
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RESULT RED, 48 行 (全为他批工作树页 p118/215/218/254-264/363-364/396); `grep -c ch08` = 0, `grep -cE '"ig34_p04(2[7-9]|3[0-9]|40)_'` = 0 → **ch08 fp 回归 0**.
- `python3 tools/check_links.py 2>&1 | grep 'live docs'` → `broken relative links: 18668 (live docs: 42)` = 基线.

### 7. G-TB8
- trace: writer `oh-my-claudecode:executor` subagent_done (02:39:16Z); reviewer `oh-my-claudecode:code-reviewer` CONDITIONAL ×2 + 续 PASS (03:04:53Z, attempt 2). `agent: main` 记录 6 条, 无 ch08 相关 → 无主控写 KB.
- 终态必经 reviewer: ch08 mtime 2026-11-26T03:03:28Z < reviewer 续 签字 03:04:53Z; 当前 md5 = 签字 md5 `154743c2…` ✓.
- 观察 (非阻断): writer 续 (T-7/T-8 照录 delta) 只记在 `B-ch08.writer.jsonl` 末 2 行 + checkpoint "续", trace 无 writer attempt-2 事件, 建议主控补一行.
- D7 (t1_user_ack.md:19): domains/RELREC/RELSUB/RELSPEC/SUPPQUAL 本批未动 (`git diff --stat` 仅 ch08) ✓.

### 观察 (非阻断, 交主控)
- ch08:34 PDF p428 "This example illustrates how CMGRPID…" 为独立段, KB 并入前段 (仅分段, 预存).
- T-7 / T-8 待 T4 用户裁定.

### 判定
独有丢失 0 / 忠实度错 0 / ch08 fp 回归 0 / G-TB8 ✓ → **PASS**.
