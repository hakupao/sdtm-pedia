# T2 B-DI writer checkpoint

## attempt 1 (2026-11-26T05:06:05Z, oh-my-claudecode:executor / opus)

- base HEAD: `beaefa9cbea4bdd86deffb7091650174ca411c83` (DI 文件改前 `git diff --quiet -- knowledge_base/domains/DI` = clean)
- md5: DI/assumptions.md `3f33ea8f8d8d1a8a8effeef6782a9923` → `b69bf6bd2574d4390ca35e562db12e39` (5 行不变; 仅 :5 行首插入 1 句)
- 白名单: DI/assumptions.md (batch json). domains/DI/ 仅此一个文件 (无 spec/examples; SDTMIG v3.4 不含 DI spec, 见 PDF 指向 SDTMIG-MD).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DI_writer/` (assumptions.before.md)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0; census 0 表; pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): §9.1 = p441 单页 (p441 顶部 "9 Study References" 章引言 → "9.1 Device Identifiers" 1 段 5 行 → 同页 "9.2 Non-host Organism Identifiers (OI)" 开始). p440 末为 §8 RELSPEC Examples, p442 为 OI Assumptions. 完整范围 = p441 (§9.1 段). batch pdf_pages [441] 覆盖完整; pdf_ranges 空 (无表).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | DI/assumptions.md:5 | ig34_p0441_a007 | INSERTED | 段首补 PDF §9.1 首句 "The Device Identifiers (DI) dataset establishes identifiers for devices, … SPDEVID." (逐字); 原后续句不动 | 441 |

- 覆盖率自查: atoms 1 = 表中 atom 行 1.
- spec 首句: PDF §9.1 无 spec (无 "di.xpt, …" 句) → 不适用. 节引言 NOTE: §9.1 无 → 不适用.

### 双向全扫
- PDF→KB: p441 §9.1 段 (首句至 "examples of its use.") 空白规范化后与 KB :5 **完全相等** (522 字符 = 522, 脚本见复跑命令). §9.1 无表/列表/CODE_LITERAL.
- KB→PDF: :1 `# DI — Assumptions`、:3 `## DI – Description/Overview (§9.1)` 为导航标题 (PDF 标题为 "9.1 Device Identifiers"; 不改已有标题, 规则 6); :5 全句均在 PDF. 无 KB 自写解释性内容 (D6 无), 无伪节号.

### PDF_TYPO 清单
- 无.

### 删除清单
- 无.

### 新增 atom 清单 (R3)
- 无 (§9.1 除 a007 外均已 PRESENT).

### 范围外发现 / 需主控定
- F-1 (需主控定, 建议不补): p441 §9 章引言 ("There are occasions when … identified thus far:" + 2 条 bullet) 不在 DI 文件; 已逐字在 `chapters/ch10_appendices.md:66-69` (`## Section 9: Study References (p441)`). 属 §9 章级而非 §9.1, 且 OI/assumptions.md 同样未收; 若要求域文件也带章引言, 由主控定 (DI/OI 一并).
- F-2: `model/05_study_level_data.md:257` 附近也有 "Identifiers for non-host organisms" (SDTM v2.0 侧), 不在本批, 未核.

### 触碰的 unparseable 表
- 无.

### git diff --stat
```
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 复跑命令
```
git show HEAD:knowledge_base/domains/DI/assumptions.md | diff - knowledge_base/domains/DI/assumptions.md
python3 -I -c "import re;t=open('.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt').read();p=re.sub(r'\s+',' ',t[t.index('The Device Identifiers (DI)'):t.index('9.2 Non-host')]).strip();k=re.sub(r'\s+',' ',open('knowledge_base/domains/DI/assumptions.md').read().split('(§9.1)')[1]).strip();print(p==k,len(p),len(k))"   # True 522 522
grep -rn "necessary to establish study-specific terminology" knowledge_base/   # 仅 ch10_appendices.md:66
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
