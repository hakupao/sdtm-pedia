# T2S S-CH1 writer checkpoint (扫描批: chapters ch01 / ch02)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `70a7373`; 两文件改前与 HEAD 一致 (cmp), **本批 KB 零改动** (md5 ch01 `e7c39a7ae829e3abe67a7e49808c584e` 109 行; ch02 `1c39874b259c58ba0e84630941acf7cb` 186 行; 前后相同).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH1_writer/`
  (ch0{1,2}_base.md = `git show HEAD:`; scripts/wdiff.py = PDF layout 全页词序列 vs KB 词序列 difflib 双向; scripts/sent.py = 逐页按句子串命中; p-007..p-016.png 90dpi 渲染逐页目视).
- 本文件 T2 历史 (`t2_B-ch01.md` / `t2_B-ch02.md`) 的 PDF_TYPO 登记继续有效: ch01 T-1 (p10 "has" keep-correct)、T-2 (p10 MANY 分句 LNKGRP/LNKID 对调 keep-correct); ch02 T-1 (p16 "Trials Sets" 照录 + T4).

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| chapters/ch01_introduction.md | §1 | 7-10 | **7-10** | p7 首行 `1 Introduction`; p10 末段为 §1.5 Known Issues 结束; p11 首行 `2 Fundamentals of the SDTM` → 无 §1 内容 |
| chapters/ch02_fundamentals.md | §2 | 11-16 | **11-16** | p11 首行 §2 章标题; p16 下部 `3 Submitting Data in Standard Format` / §3.1 起属 ch03 (边界页别节内容不归本批); §2.7 止于 p16 "…selected general observation class." |

### 双向全扫 — 逐页日志
方法: PDF→KB = 该页 layout 文本去列表符后逐词序列与 KB 全文词序列 difflib 对齐 (wdiff.py; 弯/直引号、U+2011 不换行连字符归一, 行尾连字符折行保留连字符), 另以逐句子串命中复核 (sent.py; 未命中项逐条人工判为跨列表项切句假阳); KB→PDF = 同一 difflib 的 KB 侧 insert/replace 全量列出 (未截断). 渲染逐页目视核列表层级、粗体、链接、图. 两章无表格 / CODE_LITERAL; 唯一 FIGURE 为 p15 图.

| 页 | 节 | PDF→KB: 句/列表项 数, 命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 7 | §1 / §1.1 / §1.2 / §1.3 首句 | 21 / 21 / 0 | ch01:1-30; :1 H1 + :3 `Source:` 行 = 导航 | 无表 | 切句未命中 1 = 章/节标题与首句拼接 (KB H1/H2 等价) |
| 8 | §1.3 bullets / 尾段 / §1.4 首 | 40 / 40 / 0 | ch01:32-55 一致 | 无表 | |
| 9 | §1.4 2-8 / guides / §1.4.1 前半 | 32 / 32 / 0 | ch01:56-83 一致 | 无表 (B-ch01 已把 KB 摘要表改为 PDF 列表) | 切句未命中 3 = 跨列表层级拼接假阳; 列表 4 级层级 (• / o / ▪ / •) 与 KB 缩进一致 (渲染核) |
| 10 | §1.4.1 后半 / §1.5 | 26 / 24 / 0 | ch01:84-109; 词差仅 :85 "has" (T-1) 与 :109 MANY 分句 LNKGRP/LNKID (T-2) | 无表 | 2 处 = 既有 PDF_TYPO keep-correct, 不动; "- -LNKID" = 行尾折行 |
| 11 | §2 / §2.1 / §2.2 前 | 34 / 34 / 0 | ch02:1-39; KB-only: :3 Source 行、:5-7 §1 交叉引用 (导航)、:13 / :23 KB 自拟 H3 (导航) | 无表 | "-- STRESN" / "- -TEST" / "-- POS" = 行尾折行; U+2011 归一 |
| 12 | §2.2 后 / §2.3 / §2.4 前 | 27 / 27 / 0 | ch02:39-67; KB-only :55 KB note (D6, 既有) | 无表 | |
| 13 | §2.4 末 / §2.5 / §2.6 首 | 33 / 33 / 0 | ch02:68-94; KB-only :76 KB 自拟 H3 (导航) | 无表 | 切句未命中 1 = "To create a custom domain," 与列表 1 拼接假阳 |
| 14 | §2.6 1-3h | 33 / 33 / 0 | ch02:94-108 一致 | 无表 | |
| 15 | §2.6 3i-k / 图 / §2.7 前 | 22 / 22 / 0 | ch02:109-150; KB-only :115-127 KB note + Mermaid (D6, 既有) | FIGURE (渲染核, 见下) | 图题 `**Figure. Creating a New Domain**` :113 = PDF |
| 16 | §2.7 后 (至 §3 标题前) | 22 / 22 / 0 | ch02:151-186; KB-only :133/:158/:167/:178 KB 自拟 H3 (导航) | 无表 | :176 "Trials Sets" = 照录 (ch02 T-1, T4) |

合计: PDF→KB 缺口 0 (已补 0); KB→PDF 无出处内容全部为下列已登记导航 / D6 / PDF_TYPO, 无新增.

### p15 图 (Mermaid) 渲染核
PDF 图: Identifier Variables —AND— Timing Variables —AND— Topic and Qualifier Variables; Topic and Qualifier 分出 Interventions-/Events-/Findings-Specific Variables (三者间 OR); Identifier、Timing 实线箭头 + 三个 Specific 虚线箭头均指向 New Domain. ch02:117-127 Mermaid: A/B -- AND --> D, C → E/F/G, E/F/G -- OR --> D → 分支与顺序一致; D6 标注 :115 已在. 不改.

### KB 自写内容 (保留, 不改)
| ch02 行 | 内容 | 类别 | 处理 |
|---|---|---|---|
| :5, :7 | `## Section 1 Context (Reference Material)` + 交叉引用 ch01 | 导航 (B-ch02 a2 D2 去重产物) | 保留, 不标 D6 |
| :13, :23, :76 | `### Variable Roles (5 major roles)` / `### Qualifier Variable Subclasses` / `### General rules for determining which variables to include:` | KB 自拟小标题 (导航) | 规则 6 不动标题; 不标 D6 |
| :133, :158, :167, :178 | §2.7 四个 KB 自拟 H3 | 同上; 措辞 B-ch02 a2 已按 p16 修正, 与 PDF 不矛盾 | 同上 |
| :55 | KB note 按类举例域 | D6 (既有) | 复核不矛盾 (EX/CM/PR = Interventions, AE/DS/MH = Events, LB/VS/EG = Findings) |
| :115-127 | Mermaid + KB note | D6 (既有) | 见上 |
| ch01:1,3 / ch02:1,3 | H1 + `Source:` 行 | 导航 | — |

### 观察 (不改, 供 reviewer 知悉)
- ch02 KB 有 PDF 无的粗体强调: :11 "observations"、:27-31 五个 Qualifier 名、:37 "domain"、:51-53 三个类名、:80 "STUDYID, USUBJID, DOMAIN, and --SEQ" (渲染核 PDF 均为常规体). 规则 1 允许 Markdown 粗体语法, 文字逐字一致; B-ch02 reviewer/auditor 已过. 未改.
- PDF p15/p16 "must **NEVER**" 为粗体+下划线, KB :135/:160 为常规体 "NEVER" (文字一致). 同上未改.
- 列表符号: PDF "o"/"▪" 与 lettered a.-k. 在 KB 用 `-` / `- a.` 缩进表达, 层级一致; 排版字符 (直/弯引号) 归 S-TYPO.

### 变更清单
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| — | — | — | — | 无 KB 改动 (两文件 PDF↔KB 双向全扫零缺口) | 7-16 |

### 结构改动清单
无.

### 删除清单
无.

### D6 标注清单
无新增 (既有 2 处: ch02:55, ch02:115).

### PDF_TYPO 清单
无新增; 沿用: ch01 T-1 (:85, p10 缺 "has", keep-correct, 依据 p49 同短语)、ch01 T-2 (:109, p10 MANY 分句, keep-correct, 依据同段前句 + p31 §4 定义)、ch02 T-1 (:176, p16 "Trials Sets" 照录, T4, 依据 sv20 p53).

### 范围外发现
无.

### 需主控定
无. (可选: 上文 "观察" 两项粗体差异是否在 S-TYPO 一并统一; 本批未动.)

### 验证 (repo 根; S = 上述 scratch)
```
python3 -I $S/scripts/wdiff.py knowledge_base/chapters/ch01_introduction.md 7 10
python3 -I $S/scripts/wdiff.py knowledge_base/chapters/ch02_fundamentals.md 11 16 "3 Submitting Data in Standard Format"
python3 -I $S/scripts/sent.py $S
python3 tools/check_links.py 2>&1 | grep "live docs"   → broken relative links: 18668 (live docs: 42)
git diff --stat -- knowledge_base/chapters/ch01_introduction.md knowledge_base/chapters/ch02_fundamentals.md   → (空)
```
wdiff 输出: ch01 ratio 0.9947, 非 equal 段 = H1/Source 行、"has" (T-1)、LNKGRP/LNKID (T-2)、折行 "- -LNKID"; ch02 ratio 0.961, 非 equal 段 = H1/Source/§1 交叉引用、7 个 KB H3、2 处 D6、3 处行尾折行 ("-- STRESN" "- -TEST" "-- POS").
