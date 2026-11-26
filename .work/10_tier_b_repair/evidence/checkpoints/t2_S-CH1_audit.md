# T2S.S-CH1 Auditor (Rule A) — attempt 1

> agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同. 先独立判, 判完才读 `t2_S-CH1.md` / `t2_S-CH1_review.md`.

## 抽样 (可复跑)
- 脚本: scratch `t2s_S-CH1_auditor/sample.py` (下为逻辑). 总体 P = pdf_atoms 中 atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, ig34 页 7-10 且 parent_section ∈ §1(.x), 页 11-16 且 ∈ §2(.x); 去 ledger INTENTIONAL_EXCLUDE (2). intros = [] 无并入.
- writer.jsonl 全为 VERIFIED (KB 零改动; `git diff HEAD --stat -- knowledge_base/chapters/` 空), "改动页 1/3" 不适用, N 全部 P 随机.
- |P| = 223; N = min(30, max(20, ceil(22.3)), 223) = 23; seed = 20261126.
```
python3 -I sample.py   # J=S-CH1.json; insec: lo<=page<=hi and parent_section 以 §<sec> 或 §<sec>. 开头
rng = random.Random(20261126); sample = sorted(rng.sample(P, 23))
```

## 样本判定 (PDF = `work/pdf_pages/ig34_p00NN.txt`, 原页逐行对照)
| # | atom_id | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0007_a012 | p7 §1.2 Section 2 项 | ch01:18 | 否 | 是 | §1.2 | 逐字 |
| 2 | ig34_p0008_a001 | p8 §1.3 DA 范围扩展 + 6.3.1 引用 | ch01:32 | 否 | 是 | §1.3 | 逐字 |
| 3 | ig34_p0008_a007 | p8 §1.3 BE/BS/RELSPEC 自 PGx 复制 + 3 引用 | ch01:38 | 否 | 是 | §1.3 | 逐字 |
| 4 | ig34_p0008_a013 | p8 §1.3 CT 更新 | ch01:44 | 否 | 是 | §1.3 | 逐字 |
| 5 | ig34_p0009_a016 | p9 §1.4.1 "The columns of the table are:" | ch01:72 | 否 | 是 | §1.4.1 | 逐字 |
| 6 | ig34_p0009_a022 | p9 §1.4.1 sponsor 自建 label | ch01:79 | 否 | 是 | §1.4.1 | 逐字, 嵌套层级同 PDF |
| 7 | ig34_p0010_a007 | p10 多 codelist + VLM | ch01:90 | 否 | 是 | §1.4.1 Codelist | 逐字 |
| 8 | ig34_p0010_a008 | p10 codelist + * = 外部词典 | ch01:91 | 否 | 是 | §1.4.1 Codelist | 逐字 |
| 9 | ig34_p0010_a016 | p10 Core 3 值 + 4.1.5 引用 | ch01:99 | 否 | 是 | §1.4.1 | 逐字 (含 em dash) |
| 10 | ig34_p0010_a024 | p10 §1.5 例子未系统复核 | ch01:109 | 否 | 是 | §1.5 LNKID 小节 | 逐字 |
| 11 | ig34_p0011_a017 | p11 Synonym Qualifiers | ch02:29 | 否 | 是 | §2.1 | 逐字 (PDF ‑‑ 非断字连字符 = 排版) |
| 12 | ig34_p0011_a027 | p11 §2.2 关系逻辑 | ch02:37 | 否 | 是 | §2.2 | 逐字 |
| 13 | ig34_p0012_a006 | p12 Define-XML URL | ch02:41 | 否 | 是 | §2.2 | 逐字, URL 完整 |
| 14 | ig34_p0012_a025 | p12 §2.4 4 类数据集 | ch02:63 | 否 | 是 | §2.4 | 逐字 |
| 15 | ig34_p0012_a027 | p12 TDM 数据集 + §7 引用 | ch02:66 | 否 | 是 | §2.4 | 逐字 |
| 16 | ig34_p0013_a006 | p13 §2.5 标准 + 自定义域 | ch02:74 | 否 | 是 | §2.5 | 逐字 |
| 17 | ig34_p0013_a021 | p13 §2.6 首句 | ch02:91 | 否 | 是 | §2.6 | 逐字 |
| 18 | ig34_p0013_a022 | p13 域数量依研究 | ch02:91 | 否 | 是 | §2.6 | 逐字 |
| 19 | ig34_p0013_a023 | p13 "To create a custom domain," | ch02:91 | 否 | 是 | §2.6 | 逐字 |
| 20 | ig34_p0013_a025 | p13-14 共同主题建域 + 例 | ch02:94 | 否 | 是 | §2.6 步 1 子项 | 逐字 (跨页续文 "topics are: …" 亦在) |
| 21 | ig34_p0014_a004 | p14 分 CRF 模块可入既有域 | ch02:97 | 否 | 是 | §2.6 步 1 子项 | 逐字 |
| 22 | ig34_p0014_a008 | p14 步 3a 标识变量 | ch02:101 | 否 | 是 | §2.6 步 3 | 逐字 |
| 23 | ig34_p0016_a003 | p16 --RPDY (Timing Variables) | ch02:153 | 否 | 是 | §2.7 SEND-only 列表 | 逐字 |

**独有丢失 0 / 忠实度错误 0 / 位置错误 0.**

## 补充核验
- P 全 223 机械正扫 (scratch `fullscan.py`: 规范化空白/‑/弯引号/`- -` 折行后子串匹配 ch01+ch02): 未命中 3 = ig34_p0009_a024 (原子错: 原子写 "Codelist or Format", PDF p9 与 KB:81 均为 "Codelist, or Format")、ig34_p0010_a002 (ch01 T-1 "has" keep-correct)、ig34_p0010_a023 (ch01 T-2 MANY 分句 LNKGRP/LNKID keep-correct). 均为既有登记, 非缺口.
- 反向 KB→PDF (两文件全文逐行人工对 p7-16): 无出处行仅 H1 / `Source:` 行 / ch02:5-7 §1 交叉引用 (导航) / ch02 KB 自拟 H3 7 个 (:13 :23 :76 :133 :158 :167 :178, 标题=导航, U8) / D6 2 处 (ch02:55 类别示例域、:115 Mermaid 标注) / ch02:113 粗体图题 (PDF 原有). 无未标注的解释性内容 → 忠实度错误 0.
- 图 p15 "Creating a New Domain" 渲染 (pdftoppm -r 80) 对 ch02:117-127 Mermaid: Identifier/Timing/Topic-Qualifier 三者 AND, Topic 分 Interventions/Events/Findings-Specific 三支 OR → New Domain; 逻辑一致, D6 标注在.
- PDF 粗体+下划线 "NEVER" 在 KB 为纯文本 = 强调格式差异 (S-CH1 主控口径), 不计.
- 本批无表 (TABLE_ROW 原子 0)、intros/gaps/footnote/census_items 均空 → 无需落地核.
- 授权范围: `git diff HEAD --stat -- knowledge_base/chapters/` 输出空 (KB 零改动).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (= 基线).
- G-TB8: trace 中 `T2S.S-CH1` 有 executor (07:37:52Z) 与 code-reviewer PASS (07:41:51Z) 的 subagent_done; 无 main 写 KB 记录.

## 对照 writer / reviewer (独立判完后)
writer "双向全扫零缺口; 差异仅 T-1/T-2/Trials Sets 照录" 与 reviewer PASS 与本审计结论一致; 无分歧.

**Verdict: PASS** (Rule A N=23 seed=20261126: 丢失 0 忠实 0)
