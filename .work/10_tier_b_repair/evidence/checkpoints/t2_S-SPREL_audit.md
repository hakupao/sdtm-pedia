# T2S.S-SPREL Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-SPREL.md` / `t2_S-SPREL_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPREL_auditor/`

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=21).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py > $S/sample.json`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW}, 页 ∈ sections 范围, parent_section 归属:
    "§<sec>" + [空格/./结尾] (含子节, 如 §8.2.1/§8.2.2), 或 "<RELREC|RELSUB|RELSPEC> –" 前缀 (这些原子 parent_section 无节号);
    SE §5.3 p79-84 (p84 §5.4 SM 排除); RELREC §8.2 p429-430 (§8.3 排除); RELSUB §8.7 p437-439 (p437 §8.6.3 排除); RELSPEC §8.8 p439-440;
    OI §9.2: 原子页码 p442-444 (= PDF p441-443, 原子分页 +1, 已对 pdf_pages txt 核), 故 OI 用 lo..hi+1, p444 §10 排除;
    + intros §9 p441 (parent "§9 [") 原子 a002-a005. 减 ledger INTENTIONAL_EXCLUDE (实减 27: spec 表行 + 4 处脚注原子).
writer 页 = S-SPREL.writer.jsonl 中 action≠VERIFIED 的 pdf_page = {79,80,82,83,429,438,439,441,442}; C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 209, |C| = 127, N = 21 (writer 页 7 + 其余 14), seed = 20261126. 机械匹配 `python3 -I $S/match.py $S` (20/21 命中; #18 未命中 = 原子错, 渲染核).

## 样本判定 (TABLE_ROW 对 110dpi 渲染逐格: p82/83/84/430/439/440/443)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0083_a011 | 83: Ex2 se r1 123/SCRN | SE/examples.md:66 | 否 | 是 | 是 | 渲染逐格 |
| 2 | ig34_p0083_a005 | 83: Ex2 dates without times 句 | SE/examples.md:56 | 否 | 是 | 是 | |
| 3 | ig34_p0079_a007 | 79: SE 适合多治疗期/crossover | SE/assumptions.md:13 | 否 | 是 | 是 | Description 段 |
| 4 | ig34_p0429_a012 | 429: --GRPID 更高效 | RELREC/assumptions.md:18 | 否 | 是 | 是 | `## Relating Peer Records` 下 |
| 5 | ig34_p0438_a013 | 438: RELSUB asm 1 (APRELSUB) | RELSUB/assumptions.md:17 | 否 | 是 | 是 | |
| 6 | ig34_p0442_a014 | 441: OI spec OIPARMCD 行 | OI/spec.md:41-47 | 否 | 是 | 是 | 字段逐项; CT (OIPRMCD) vs C179591 = U5 归 S-CT 不计 |
| 7 | ig34_p0079_a016 | 79: SE spec DOMAIN 行 | SE/spec.md:14-20 | 否 | 是 | 是 | CT "SE" 空 = U6 归 S-CT 不计 |
| 8 | ig34_p0083_a017 | 83: Ex2 Row 1 叙述 | SE/examples.md:73 | 否 | 是 | 是 | |
| 9 | ig34_p0429_a007 | 429: RELID 命名惯例建议 | RELREC/assumptions.md:16 | 否 | 是 | 是 | |
| 10 | ig34_p0441_a003 | 441: §9 "following situations" | DI/assumptions.md:5 | 否 | 是 | 是 | §9 引言 DI 顶部 (U3); 与上句合段 = 段落合并不计 (S-FND 口径) |
| 11 | ig34_p0082_a020 | 82: Ex1 se r10 791/IV | SE/examples.md:34 | 否 | 是 | 是 | 渲染逐格 |
| 12 | ig34_p0440_a020 | 440: relspec r6 SPC-003-A/RNA | RELSPEC/examples.md:51 | 否 | 是 | 是 | 渲染逐格 |
| 13 | ig34_p0440_a019 | 440: relspec r5 SPC-003/TISSUE | RELSPEC/examples.md:50 | 否 | 是 | 是 | 渲染逐格 (TISSUE vs 图 Brain 照 PDF) |
| 14 | ig34_p0083_a018 | 83: Ex2 Row 2 叙述 (含 Rescue 句) | SE/examples.md:75 | 否 | 是 | 是 | 本批补 Rescue 句, 逐字对渲染 |
| 15 | ig34_p0080_a018 | 80: asm 1 PK 5/10/7 mg 例 | SE/assumptions.md:31 | 否 | 是 | 是 | |
| 16 | ig34_p0430_a020 | 430: RELREC Ex1 r1 AE/AESEQ 5/RELID 1 | RELREC/examples.md:19 | 否 | 是 | 是 | 渲染逐格 (Ex1 表) |
| 17 | ig34_p0429_a013 | 429: "should be used to represent either:" | RELREC/assumptions.md:20 | 否 | 是 | 是 | |
| 18 | ig34_p0083_a001 | 83: Ex1 dm r3 791/SMITH, J/IO/IV-ORAL/IO/IV-ORAL | SE/examples.md:47 | 否 | 是 | 是 | 原子错 (漏 ACTARM、多 "J."); 渲染 20 列逐格 = KB |
| 19 | ig34_p0439_a018 | 439: relsub r1 MOTHER, BIOLOGICAL | RELSUB/examples.md:35 | 否 | 是 | 是 | 渲染逐格 |
| 20 | ig34_p0444_a017 | 443: oi r14 H77/SUBTYP/A | OI/examples.md:32 | 否 | 是 | 是 | 渲染逐格 |
| 21 | ig34_p0081_a004 | 81: asm 7 EPOCH/Define-XML | SE/assumptions.md:43 | 否 | 是 | 是 | |

独有丢失 0 / 21; 忠实度错误 0 / 21; 位置错误 0.

## 另查
- **P 全量机械正扫** (`python3 -I $S/match.py $S full`): 209 中 195 命中; 14 未命中逐条处置: p79 a004/a006/a009/a010 = 原子 verbatim 抄自旧 KB (KB 现与 p79 pdftotext 逐字一致: "epochs and elements" / "definitions (TESTRL values)" / "--DTC" / "relate"/"--DY"; 已列 fp 预期回归 69-72); p80 a010 脚注原子上标 1 抽成 `*`; p80 a020 原子错 (KB asm 3 = p80 txt "first of a series of 5 daily doses and end after 1 week … after 4 weeks"); dm 5 行 (p82 a026/a027, p83 a001/a021, p84 a001) = 原子错, 渲染 p82/83/84 逐格 = KB; p440 a009 = FIGURE 占位 (Mermaid D6 对渲染一致: 4 条边/3 层); p443 a004/a006 = 多行列表跨行断句, KB 子项逐字在 OI/assumptions.md:17-28.
- **gaps**: SE S (`## SE – Specification` + se.xpt 句, SE/assumptions.md:21-23 逐字对 p79) + F (SE/spec.md:123); RELREC/RELSUB/RELSPEC F (各 spec.md 最后变量块 `---` 之后、`## Cross References` 之前, U7); OI D/S/A 标题 + oi.xpt 句 (OI/assumptions.md:3/9/13, 逐字对 p441) + F (OI/spec.md:69). 5 处脚注逐字 = PDF ("¹In this column … enclosed in parentheses."). ✔
- **intros §9**: DI/assumptions.md:3-8 `## §9 Study References` + 2 句 + 2 bullet 逐字对 p441, 位于 DI 顶部、§9.1 之前 (U3/O46). DI narrow (b) 无 DI spec 表 (PDF §9.1 仅 1 段, 指向 SDTMIG-MD) → 跳过正确. ✔
- **CT `*`** (pdftotext -layout CT 列): SE ETCD/ELEMENT, RELREC IDVAR, OI OIVAL = 4; RELSUB/RELSPEC 0; KB `*` 同 4 处, 其余变量 CT 差异仅 C-code (U5) / DOMAIN 空 (U6) 不计. ✔
- **反向 KB→PDF 全 16 文件** (`python3 -I $S/reverse.py $S`, 去非字母数字对 pdftotext -raw p78-85 / p427-444): 未命中仅 (a) 导航: H1/H2、`> Source text:` 行 (D7 既有)、`> Class|Structure`、Cross References 块 (U8)、DI `## DI – Description/Overview (§9.1)`; (b) D6: RELREC/assumptions.md:5、RELSPEC/examples.md:11 + Mermaid; (c) U5 C-code; (d) SE/examples.md:44/:79 表头 BRTHDTC (PDF BIRTHDTC 笔误 = SE T-1, DM spec 证 BRTHDTC). 无 PDF 出处且未 D6 的行 = 0. RELREC 文件另承载 §8 引言段/§8.3/§8.3.1 (B-REL 既有), 反向扫同样无孤行.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/{SE,RELREC,RELSUB,RELSPEC,OI,DI}` = 9 文件, 38+/9-; 8 个 ⊂ kb_files, DI/assumptions.md 仅 +7 行 §9 引言 (narrow (a)). ✔
- **G-TB8**: trace 343 writer (executor) 07:32:02Z、349 reviewer (code-reviewer, PASS) 07:41:55Z; 本批 KB 文件最晚 mtime 16:28:26 JST = 07:28:26Z < reviewer 完成; 无 agent main 写 KB. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).
- 观察 (不计, 范围外): `chapters/ch10_appendices.md:64-69` 仍有 §9 引言副本, 现与 DI 顶部重复 (D2 应改一行交叉引用; ch10 非本批文件, writer 已列需主控定 #3).

## 对照 writer / reviewer (判完后读)
与 writer 登记 (SE T-1 BIRTHDTC、SE T-2 / OI T-1 / OI T-2 照录、p79 fp 预期回归 4、ch10 重复待主控) 及 reviewer PASS (CT * 4/4、脚注 5 处 U7、DI narrow 仅引言、census OK10/DIFF2) 一致. 无分歧.
