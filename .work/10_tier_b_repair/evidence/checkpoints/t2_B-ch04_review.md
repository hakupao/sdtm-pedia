# T2 B-ch04 reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** — 29 atoms + 4 recheck 全部落地且逐字对 PDF; 3 处原位替换、3 处 D2 删除、2 张不可机检表逐格一致; T-1/T-2 判定同意.
未达 PASS 的原因: dispatch notes「R2 插入后残留旧改写句 → 删」与 R3「批内发现的叙述缺失也补」各有若干条未执行 (见修正清单 C1-C10).

### 命令 (repo 根; scratch = /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch04_reviewer)
```
S=<scratch>; manifest = B-ch04.json pdf_ranges (ch04, ig34 22-59)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → exit 1; status {'UNPARSEABLE': 33, 'OK': 19, 'DIFF': 1}; 唯一 DIFF = ch04:1295 eg.xpt Row 列 5↔6 (T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → exit 1 RED; regressions=13 全部为 p215 (CP) / p257-263 (MB) = 别批, p22-59 回归 0
  本批 29 atoms + 4 recheck + O3(p43_a015): 30 hit ch04; 不命中 3 = p43_a034 / p56_a005 / p56_a006 (见下, 原子 verbatim 错)
python3 tools/check_links.py | grep 'live docs' → broken relative links: 18668 (live docs: 42) = 基线
pdftoppm -r 110 p25/p42/p53/p54/p56, -r 90 p44 → 渲染逐格
```

### 预期不命中 3 条 (确认原子错, 非 writer 漏)
| atom | 原子 verbatim 问题 | 页面实况 (p56 渲染) | KB |
|---|---|---|---|
| p43_a034 | 带 `[TRUNCATED_AT_PAGE_BOUNDARY]` | 句子跨 p43→p44 | :925 整句逐字 |
| p56_a005 | "separate additional…", "COVAL+", "additional columns", "if appropriate" | "should be stored as a record in the SUPP-- dataset" / "COVAL1 to COVALn." | :1415 与渲染逐字 |
| p56_a006 | CO/TS 列缺 "to improve readability" | 三列都有 "…split between words to improve readability." | :1416 逐字 |

### 人工逐格 (渲染)
| 表 | 格 | 结果 |
|---|---|---|
| ch04:886-890 lb.xpt (p42) | 3 行 × 5 列 = 15 格 (含 O12 Week 1 VISITDY=7 / LBDY=7; Unscheduled VISITDY 空) | 全部一致 |
| ch04:1413-1417 >200 约定表 (p56) | 表头 4 格 + 3 行 × 4 PDF 列 = 12 格 (SUPP 格无句点、COVAL/TSVAL 格有句点、Not applicable. 有句点) | 全部一致; "Convention" 列 + Storage/Split rule/Label 为 KB 导航标签 (L1) |
| qscg :97 / qssw :121 (p25) | QSLOBXFL Y、VISITDY 1、SWLS010n、"My Life" | 一致 (独立于 census, 对渲染) |
| lb Ex1 :1271-1284 (p53) | r5 WBC/++/2+; r6 2016-02-01; r7 Y/3/2016-02-15 | 一致 |
| suppmh/suppae QEVAL (p55/p56) | 表头 + 空格 | 一致 |

### T-1 / T-2 裁定
- T-1 (p54 eg.xpt): PDF 表行序 4,6,5,7, "6"=INTP、"5"=PRAG; p53 说明 Row 5 = interpretation、Row 6 = PRAG. 正确值可由 PDF 叙述确定 → KB 写 5=INTP / 6=PRAG 并登记, **同意**.
- T-2 (p53 lb.xpt r7): 表头无 LBDRVFL, Y 落在 LBLOBXFL; 说明 "so LBDRVFL = "Y"". 照录 + T4 **同意**. 供用户参考: r1-r6 (visit 1) 均无 LOBXFL=Y 而 visit 3 有, 更像表头错标 (应为 LBDRVFL).

### 指定检查结论
| 项 | 结论 | 证据 |
|---|---|---|
| :868 替换 (a012+a013) | 一致 | p42 "for which data are collected only once during the study…expected to include VISITNUM" |
| :919 替换 (a023+a024) | 一致, 粗体标签保留 | p43 "doing so in conjunction with directly collecting…will blur" |
| :1413-1417 表 | 一致 | 见逐格 |
| D2 删 ICH E3 | 成立 (p41-42 无 ICH) | :848 现为 p42 原文三句 |
| D2 删 `--DTC - RFSTDTC (with no day 0)` | 成立, 缺 +1 与 p42 公式矛盾 | p42 公式 "+ 1 if --DTC is on or after RFSTDTC" |
| D2 删 --XSTDY/--CHSTDY | 成立, p43 为 "sponsor may define supplemental qualifier variables" | :894 |
| §4.4.5 "should" | PDF 原词 should, 正确 | p42 "There should be a one-to-one relationship" |
| "visits and" / ", as described above" | 正确 | :880 |
| §4.4.6 整段 | 逐字 | :894 |
| O3 --STRF 句 | 逐字, 位置在 --STRF 表后、ENRF 句前 (= PDF 顺序) | :913 |
| R3 p42 公式块 / p45 Ex2-Ex3 Assumptions / p56 CO-IE-TS-TI 清单 | 逐字 | :850-857 / :980-1000 / :1404-1411 |
| ch04:874-875 括注 | p42 planned-visit 第 3 条只有 "For visits that may last…start of the visit."; "(not the actual study day; do not use --DY)" **非 PDF 文字** → KB 自写, 作 KB note 合规; 改写后与 p42 "VISITDY is, by definition, the planned study day" 不矛盾 | p42 |

### D6 KB note 7 处逐条
| # | 行 | 矛盾? | 判定 |
|---|---|---|---|
| 1 | :863 Partial dates | 不矛盾 | OK (但其所在 Derivation notes 其余 3 条应删, C2) |
| 2 | :873 VISIT bullet | 不矛盾 | OK |
| 3 | :875 VISITDY note | 不矛盾 | OK |
| 4 | :896 SE start date/time | 不矛盾但为 :894 PDF 句 (a007) 的压缩重复, 且 "may use" 比 PDF "will be" 弱 | **应删** (C3) |
| 5 | :898 See also 5.3 | 纯导航, D6 范围外不应加前缀; 且与 :894 "(see Section 5.3, Subject Elements)" 重复 | **应删** (C3) |
| 6 | :951-954 Example applications | 不矛盾 (CMSTRF BEFORE 与 p43 例一致) | OK |
| 7 | :964 Mermaid | 不矛盾 (斜体图注≈图内文字, "The event" vs PDF "The medical event") | OK |

### R2 recheck
| atom | 判定 | KB |
|---|---|---|
| p43_a013 | REAL_GAP → 已补逐字 | :906 |
| p44_a003 | REAL_GAP → 已补 | :936 |
| p44_a004 | REAL_GAP → 已补 | :938-940 |
| p44_a008 | REAL_GAP → 已补 | :942-945 |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| C1 ch04:300 | 残留改写 | 插 a028 后, "When a test is not performed… See Section 4.5.1.2 for details." 为重复改写, 删除模拟不丢任何命中原子; 句 1 丢 "for individual data items" / "should" (a027) | p29 "Missing values for individual data items should be represented by nulls." |
| C2 ch04:861,862,864 | 残留改写 | Derivation notes 3 条复述 :848-857 PDF 文字, 删除不丢原子 → 删; :863 KB note 改为独立一行 | p42 公式块 |
| C3 ch04:896,898 | D6/重复 | 见 D6 #4/#5 | p43 |
| C4 ch04:947 | 残留改写 | "Restriction on --STRTPT values" 复述 :936-945 新插清单, 删除不丢原子 → 删 | p44 |
| C5 ch04:1402 | 残留改写 | 旧压缩行与 :1404-1409 清单重复 → 删 | p56 |
| C6 ch04:925 | R3 (本批已改行) | 丢 "(e.g., "Prior", "Ongoing")" 与 "and are not limited to the study reference period" (a031/a033) | p43 "…--ENTPT variables, and are not limited to the study reference period." |
| C7 ch04:838,840 | R3 (§4.4.4 已改) | 丢 "as day 1" (a044)、"the date portion of" (a045) | p41 "to the date portion of the subject reference start date" |
| C8 ch04:828 | R3 (writer 已发现未补) | 丢 "or foreword slash" (a038; PDF 拼写照录) | p41 "before the solidus or foreword slash [/]" |
| C9 ch04:956-958 | R3 一致性 | Ex2/Ex3 已补 Assumptions, Ex1 未补 (a014/a015) 及小节标题 "Examples of --STRTPT, --STTPT, --ENRTPT, and --ENTPT" (a011) | p44 |
| C10 ch04:876 | 词替换 (本批已改行) | "between VISIT and VISITNUM" 丢 "values of" (a019) | p42 "between values of VISIT and VISITNUM" |
| L1 ch04:1413 | 信息 | Convention 标签列 KB 自写, 属导航可保留 | — |
| L2 ch04:872,874 | 信息 | "numeric," / "the planned study day of the start of the visit;" 为 KB 改写前缀, 不矛盾; 可选恢复 a018/a020 原文 | p42 |
| L3 ch04:986,1002 | 保留合理 | 旧改写行承载 a006/a020 ("Example when … checked:") 等, 按规则保留, writer 应在 checkpoint 写明原因 | p45 |

### 修正清单 (CONDITIONAL → writer attempt 2)
C1-C5 删除/改写 (每条 fp 复跑确认不丢命中); C6-C10 按 PDF 逐字补回. 主控若决定 C6-C9 移交 T3, 则本批可降为 PASS-with-deferral.

### G-TB6 结构行签字
lb/suppmh/suppae 表头与分隔行、约定表表头/分隔行、"Assumptions:" 标签 (PDF 原词)、公式 ``` 围栏、KB note 前缀行 (D6) — 已逐条核, 签字.
新增/改动行 ~104, 无出处 0 (D6 标注行除外, 已逐条确认).

## attempt 2 复审 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (附 1 条 LOW 可选项 L3').

### 方法 / 命令
```
git show 6fea563:<ch04> > $S/base.md; patch $S/base.md < evidence/failures/t2_B-ch04_attempt_1.patch → md5 0df37d79… (= attempt 1 记录值)
diff $S/a1.md knowledge_base/chapters/ch04_general_assumptions.md   # attempt1→attempt2 净改动, 逐条对 PDF
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_a2.jsonl --baseline … → 全局 RED regressions=15 (均非 p22-59); ch04 页 vs base 回归 0, vs attempt1 丢失 0, 新命中 9
python3 tools/check_links.py → live docs: 42 (= 基线)
table_census (同 manifest) → OK 19 / DIFF 1 (T-1) / UNPARSEABLE 33
```

### C1-C10 落实
| C | ch04:line | 结果 | PDF |
|---|---|---|---|
| C1 | 300 | 句 1 = a027 原文; 旧 "When a test is not performed… for details." 已删, 信息由 a028 句承载 | p29 |
| C2 | 859 | Derivation notes 标签 + 3 条复述删除, 内容在 :848-857 PDF 原文; Partial dates KB note 独立一行 | p42 |
| C3 | (原 896/898) | 两行 KB note 删除, :893 PDF 段含 SE 与 "(see Section 5.3, Subject Elements)" | p43 |
| C4 | (原 947) | Restriction 行删除, "AFTER" 两情形由 :932-942 p44 清单承载 | p44 |
| C5 | (原 1402) | 旧压缩行删除, :1397-1404 清单承载 | p56 |
| C6 | 916 | 整段与 p43-44 逐字 (含 "(e.g., "Prior", "Ongoing")"、"and are not limited to the study reference period") | p43-44 |
| C7 | 838, 840 | "as day 1" / "the date portion of" / "from" 逐字 | p41 |
| C8 | 828 | "solidus or foreword slash [/]" 照录 | p41 |
| C9 | 945, 949-952 | `#### Examples of --STRTPT, --STTPT, --ENRTPT, and --ENTPT` = PDF 粗体小节标题 (p44 渲染, 与 "--STRTPT, --STTPT…" 同级), 逐字; Ex1 Assumptions 两条逐字 | p44 |
| C10 | 871 | 逐字 + 句点; 去掉的 `**…**` 是 KB 自加强调, PDF 无粗体, 去除合规 | p42 |

删除项均无 PDF 内容丢失 (被删文字的信息点都在 PDF 原文行出现); fp 对 attempt 1 丢失 0.

### L3 保留行 (ch04:954 / 982 / 998)
保留成立 (该行承载 "Example when … checked:" 一类原子 p44_a016 / p45_a006 / p45_a020 的 EQUIVALENT 信息, 删掉则该引导句缺失).
但 writer 理由 "删了会丢命中" 不准确: 这三条原子当前 fp **不命中** (只是 EQUIVALENT).
L3' (LOW, 可选): 三行前半已与新补 Assumptions 重复, 可各替换为 PDF 原句 "Example when "Active" is checked:" / "Example when both "Prior" and "Continuing" are checked:" / "Example when "Unknown" is checked:" — 去重且使 3 原子命中. 不阻断.
