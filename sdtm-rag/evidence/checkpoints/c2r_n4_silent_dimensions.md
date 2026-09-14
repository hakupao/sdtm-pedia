# C2R N4 — 沉默维度显式化 (2026-09-14)

> 状态: **工程 DONE + 复审 PASS (二轮) + 复测 B 臂 gpt-terra/gpt-sol 预登记四判据两模型全 PASS (N 系列首次; n=1)**; 默认 OFF 不动; opus-5 补跑按用户 2026-09-14 指示跳过 (仍是默认 ON 硬前置)
> PLAN §9 (登记于实现前, brainstorm 经用户批准) · 判分 `evidence/step_c2r_n4_audit.md` · 起源 `evidence/failures/c2r_n3_attempt_2.md`

## 0. PATTERN (不是对 p.161 的对症下药)
页级元数据在某维度**沉默**时 (单组页不写组序列; 无「前頁からの続き」印 ≠ 明示「本頁で開始」), 模型用视觉推测填补, 在跨页方向给出无证据续接。N3 a2 反证据: 写了印的页两模型两轮 0 错, 没写的页三轮 2 错分属两模型。修法是**全部 85 个 annotated 页**都声明状态 (其中 46 页单组, 12 页单组无题), p.161 只是其中一例。

## 1. 改了什么 (7 文件, +251 −28; 检索/选页/触发/SSE 零改动)
- `scripts/study/build_pdf_page_index.py` `page_groups_by_form`: 每组新增 `continues` (该组项目在同 form **更后**页也有定位 = 枠在本頁で閉じない), 与 `continued` 对称。加非连续页区间 fail-loud (label 说「次頁」而字段义是「后页」, 只在页区间连续时一致; 实测 28 件全部隣接, 非连续 0; 复审 MINOR-F: 刻意选「宁可不建也不写谎」, 替代方案写在 docstring)。真索引重生成: 与 N3 索引**逐字相等**除 `continues` + 时间戳 (复审另用真 catalog × item_pages 复算 = 在盘索引逐字相等)。
- `server/pdf_context.py` `_ann_label`: 每个 annotated 页都在「頁索引メタ:」段写 `前頁からの続き: あり/なし；次頁へ続く: あり/なし` (页级 = 首组 continued / 末组 continues); 单组页写 `本頁の枠: 1 (名 or (無題) [n 項目])` 不带枠内印; 多组页序列不变, 每组后缀补 `・次頁へ続く`。旧索引缺 `continues` → 只哑掉「次頁へ続く」维度 (`all` 判定, 部分迁移索引也不写假「なし」), 启动一次性提示。N3 注释「順は常に足すと狼少年」保留并补 N4 区别: 状态常驻是有意的 (51% 页是「なし/なし」), 兜底 = 判据 ③。
- `server/router.py` `_PDF_SOURCE_RULE`: 一句新规则 — 连续状态是頁索引确定的事实; 「前頁からの続き: なし」= 首枠本页开始 (有见出し的枠其见出し在本页; **(無題) 枠没有见出し, 不得去画面找, 不得把首项目标签报成枠名**); 「次頁へ続く: なし/あり」= 末枠本页闭合/不闭合; 画像から読み取った内容不得与之矛盾或超出 (「続きの可能性あり」等)。N3 枚举加「本頁の枠 / 前頁からの続き / 次頁へ続く」。**不新增出典样式名词** (复审 MAJOR-2: 「画面判読」不匹配 N2 闸正则 `画面目[視视]判[読读]`, 模型一模仿闸就失明); 『画面目視判読』出现次数仍钉 1。
- 测试 +13 (2319 → **2332 passed**, 0 fail; ruff 改动文件全过): 索引 continues 三态 + 非连续 fail-loud; 单组/无题/多组/双向开口/全闭 label; 部分迁移与全缺字段降级; 元数据在前缀之后; 规则句 wiring (無題句 + 「画面判読」不得出现 + 计数 1)。

## 2. 复审 (规则 D, code-reviewer opus, 两轮, 独立 subagent)
- 第一轮 **FAIL**: MAJOR-1 规则句「なし = 見出しは本頁にある」对無題枠是假的 (单枠无题 12 页中 10 页 continued=false, p.161 就是), 会把 N3 (a)「首项目标签当组名」病根请回来; MAJOR-2 新词「画面判読」让 N2 闸失明, 判据 ② 空转。+ MINOR-3 (`any` 变异存活) / -4 (次頁 vs 后页语义无断言) / -5 (「なし」是正向断言, 定位漏项会写假「なし」) / -6 (狼少年注释被推翻) / -7 (docstring) / -8 (枚举) + NIT-9/10/11。变异 11 条抓 10。
- 第二轮 **PASS**: 8 条修法全部核对落地; 变异 7/7 抓 (含上轮存活的 M6); 日语措辞 MINOR-A/B (「閉じることを」补齐; 「画像に探す」→「画像の中に探さない」+ 括号点名 N3 (a) 病症, 避免泛化成「别在画面找任何标题」) + NIT-C/D/E (枚举用逐字串; 补「あり」释义; 注释里也不写「画面判読」) 复测前全修。
- **MINOR-5 独立复核** (Writer 用文本层重做, 与 reviewer pdftotext 结论一致): 「次頁へ続く: なし」且 form 块仍有后页且末组有未定位项目的暴露页 = **5** (p.1 / p.52 / p.75 / p.151 / p.183, 表单与组 OID 见 gitignored `runs/c2r_n4/minor5_exposure.txt`); 5/5 未定位项目的标签文本都在**本页**文本层 (非下一页) ⇒ 「なし」全部为真。这是「なし」可信度的唯一数字支撑。复跑:
  ```bash
  cd sdtm-rag && .venv/bin/python - <<'EOF'
  import json
  cat=json.load(open('data/study/st01/catalog.json')); idx=json.load(open('data/study/st01/pdf_page_index.json'))['annotated']
  blocks={b['form_oid']:b for b in idx['blocks'] if b['kind']=='form'}; items={}
  for it in cat['items']: items.setdefault((it['form_oid'],it['group_oid']),[]).append(it['item_oid'])
  for f,pages in idx['page_groups'].items():
      for p,gs in pages.items():
          last=gs[-1]; p=int(p)
          if last['continues'] or p>=blocks[f]['end']: continue
          loc=sum(1 for i in items[(f,last['group_oid'])] if idx['item_pages'][f].get(i)); tot=len(items[(f,last['group_oid'])])
          if loc<tot: print(f,p,last['group_oid'],loc,tot)
  EOF
  ```
  (再对每页用 `pdftotext -f P -l P -layout` 查未定位项目 label 前 12 字在本页/下页。)

## 3. 复跑命令 (B 臂, 与 N3 a2 同口径)
```bash
cd sdtm-rag
.venv/bin/python scripts/study/build_pdf_page_index.py          # 索引带 continues
nohup env SDTM_RAG_AUTH_ENABLED=false SDTM_RAG_PDF_CONTEXT_ENABLED=true .venv/bin/uvicorn server.main:app --port 8011 > /tmp/armB_8011.log 2>&1 &
until curl -s -m 2 localhost:8011/api/health >/dev/null; do sleep 1; done
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models gpt-terra,gpt-sol --qids T1,T3,T6 --timeout 900 --out c2r_n4
.venv/bin/python scripts/study/c2r_eval/tabulate_v3.py c2r_n4
.venv/bin/python scripts/study/c2r_eval/check_visual_grounding.py c2r_n4
```
实跑 2026-09-14: 6/6 status 200, 墙钟 18–32 s, 无截断无续写; 页集与 N3 a2 **逐字相同** (T1 ann p.174/175/176; T3 p.6/p.4; T6 p.161/162/164 + 各 3 workflow 页), 路由 both。送入模型的 label 用生产索引复算 (§1 命令), p.161 现为「本頁の枠: 1 ((無題) [16 項目])；前頁からの続き: なし；次頁へ続く: あり」= 归档真值。

## 4. 零 LLM 闸 (N2) 原样
| file | units | grounded | LABEL | OFF | range | ambig |
|---|---|---|---|---|---|---|
| gpt-sol T1 | 9 | 9 | 0 | 0 | 0 | 0 |
| gpt-sol T3 | 1 | 1 | 0 | 0 | 0 | 0 |
| gpt-sol T6 | 10 | 9 | 0 | **1** | 0 | 0 |
| gpt-terra T1 | 7 | 6 | **1** | 0 | 0 | 0 |
| gpt-terra T3 | 1 | 1 | 0 | 0 | 0 | 0 |
| gpt-terra T6 | 10 | 10 | 0 | 0 | 0 | 0 |
闸字面: **LABEL_ATTRIBUTED = 1** (gpt-terra T1, workflow p.87, 同一性词规则 — 与 a2 假阳性同型), OFF_PAGE = 1 (gpt-sol T6, workflow p.44)。判据 ② 按登记以**核验后**计, 字面计数不得省略。

## 5. 判分 (独立 Judge opus, 规则 A 全量主张核验, 未写码/未跑 eval/未写闸)
详见 `evidence/step_c2r_n4_audit.md` (红线版) 与 gitignored `runs/c2r_n4/audit_detail.md`。
| 判据 (PLAN §9) | gpt-terra | gpt-sol |
|---|---|---|
| ① 跨页续接型 contradicted = 0 | PASS (0) | PASS (0) |
| ② 闸 LABEL_ATTRIBUTED 核验后 = 0 | PASS (**字面闸 1**, 核验假阳性) | PASS (字面 0) |
| ③ T1/T3/T6 逐点 ≥ a2 | PASS (10/12, 24 点逐点全等) | PASS (10/12, 逐点全等) |
| ④ 新状态文本出典 = 頁索引 | PASS (5/5) | PASS (5/12 引用, 5/5 頁索引) |
- 靶心页 (三轮两错的单枠无题页): 两模型本轮都**显式引用新状态文本**并给出正确方向, 不是「这次没提」。声明本身经独立核验为真 (被附 8 页渲染裁边 8/8; 页集外抽检 2/2; 全 85 页对称性探针零矛盾)。
- 主张 census 64 条 (a2 46) verified 64 / contradicted 0 / unverifiable 0 — 分母涨 39% 下零 contradicted。
- **本轮最重发现 (§7 audit): 错误换层** — gpt-terra T1 凭空造一条**卡片层**事实并挂真出处 (该 OID 在 16 个检索源出现 0 次, 与自己上一节自相矛盾)。四判据 / N2 闸 / census 范围三道闸**都不覆盖卡片层捏造**。不是 N4 引起, 但 N4 是第一轮看见它的。⇒ 下一单元候选: 卡片层主张纳入 census 或加卡片接地闸 (PLAN §10)。
- 两处口径敏感性 (audit §8.1): 卡片捏造是否污染证据链 / gpt-sol 一处是否算面板合并 — 任一采反读法, 判据 ③ 对该模型翻 FAIL。由 PLAN 所有者裁, 引用时须带上。
- 闸质量: 三轮累计假阳性 6 / 真捕获 0; N2 的「假阳性 ≤ 5」只钉 N2 自己的 18 份验证集, 目前无预登记上限在管闸质量。

## 6. 诚实边界
- n=1 复测, 两模型; 靶心历史基率下 2 份同时不出错的概率约 0.25; 判据 ① 只有 T6 的 2 份有判别力 (改法 pattern 级, 验收面 example 级); 转写错误 3→5, 两处是 a2 改对又错回去的 (非本单元靶向)。 opus-5 未测 (账号拒绝 Anthropic, 用户指示跳过)。默认 ON 硬前置未变。
- 「なし」的可信度靠定位完整性, 暴露面 5 页今日全真, 但未来索引重生成后须重跑 §2 命令。
- 元数据「在」≠「被用」: N3 已证 T1 三轮零引用頁索引; 本轮是否被引用见 audit。
- 顺带观察 (非本单元, 未动): p.164 一个组名含换行 (组名原文见 gitignored `runs/c2r_n4/minor5_exposure.txt`), label 元数据段内出现换行, 是 catalog 原文所致; 若下一单元要动 label 分段, 先看这个。
- PLAN §9 登记的单枠格式把两个状态写在括号内, 实现放在括号外用同一分隔符串接 (NIT-9), 文本等价, 此处记明。
