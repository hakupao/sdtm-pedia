# C2R V3 — 画面 PDF 旁路 A/B 实测记录 (runner 半场, **零判分**)

> 单元: `PLAN_c2r_pdf_bypass.md` V3 · 判据登记于 `evidence/checkpoints/c2r_pre_registration.md`
> 日期: 2026-09-09 · 本文只记录**确定性观测**, 答案质量判分由**非本 session 的 Reviewer subagent** 另做 (规则 D)
> 结论一句话: 28 次真实 `/api/ask` 全部 200 零失败; **N 组 4 题 `pdf_trigger` 全 null (达标)**;
> T 组 T1–T5 两模型触发规则与页集逐题完全一致, **T6 两模型均未触发 (预登记外的结构性发现, §5)**。

## 0. 红线与真值伴生件

本文按 `scripts/oidscan_evidence.py` 红线**不写任何真实 item/activity/event OID 与 label/name**,
题面一律用 `c2r_pre_registration.md` §1/§2 与 `c2r_s0_survey.md` §0-1 已有的结构化说法指代。
**页码 / 计数 / token / 墙钟 / 规则名原样保留** (页码不是红线值)。

含真值的伴生件 (落在 `.gitignore:10` 的 `data/study/` 下, 不进 git):

    data/study/st01/eval/runs/c2r_v3/questions.json   题面真值 (qid → 原文)
    data/study/st01/eval/runs/c2r_v3/INDEX.md         全部 raw run 索引 + 题面对照
    data/study/st01/eval/runs/c2r_v3/*.json           28 份完整 AskResponse
    data/study/st01/eval/runs/c2r_v3/server_logs/     两臂服务日志 (含 question= 与 reason= 真值)

本文闸 (必须 CLEAN):

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python -m scripts.oidscan_evidence evidence/checkpoints/c2r_v3_eval.md \
  --catalog data/study/st01/catalog.json
```

### 0-1 题面代号 (与预登记 §1/§2 同一说法)

| qid | 结构化题面 | 预期 |
|---|---|---|
| T1 | LB 表单「身高体重是只录一次还是每次采血都测」题 (dogfood 2026-09-09 原文, 中文) | 触发 |
| T2 | AE 表单某补充自由记述项的显示条件题 (日语) | 触发 |
| T3 | NAC 表单某给药量项的显示时点题 (日语) | 触发 |
| T4 | 术前化疗 A 群 Day1 与 Day8 的临床检查采取项目差异题 (日语) | 触发 |
| T5 | 手术事件下术前 LB 活动是否常时显示题 (日语) | 触发 |
| T6 | TME 表单画面布局 / 分组题 (日语) | 触发 |
| N1 | 纯 CDISC: VS 域 Required 变量题 | 不触发 |
| N2 | DM 表单某单项目有无题 (卡片层可完整回答) | 不触发 |
| N3 | 体重 STAT 项的 code list 题 (单卡片字段属性) | 不触发 |
| N5 | 偏 CDISC 但含「画面」词的题 (M10 相关性下限反例) | 不触发 |

## 1. 复跑 (全部命令逐字可跑)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
SD=<scratchpad>/c2r_v3            # 本轮 = /private/tmp/claude-501/.../scratchpad/c2r_v3

# ① 生产索引在位 (缺则重建; 本轮**未**重建, 用的是 I2-1 已有产物)
ls -l data/study/st01/pdf_page_index.json
# uv run python scripts/study/build_pdf_page_index.py      # ← 本轮没跑

# ② 两台一次性服务 (auth 关, 非 8000 端口; 生产 launchd 全程未动)
nohup env SDTM_RAG_AUTH_ENABLED=false \
  uv run uvicorn server.main:app --port 8010 > $SD/armA_8010.log 2>&1 &          # arm A: flag OFF
nohup env SDTM_RAG_AUTH_ENABLED=false SDTM_RAG_PDF_CONTEXT_ENABLED=true \
  uv run uvicorn server.main:app --port 8011 > $SD/armB_8011.log 2>&1 &          # arm B: flag ON
until curl -s -m 2 localhost:8010/api/health >/dev/null; do sleep 1; done
until curl -s -m 2 localhost:8011/api/health >/dev/null; do sleep 1; done
curl -s localhost:8011/api/info | python3 -m json.tool | grep -A4 selectable_models

# ③ 打点 (N 组 arm B 单模型 4 次 + T 组 6 题 × 2 模型 × 2 臂 24 次; 顺序执行, 每次间隔 5s)
.venv/bin/python $SD/run_v3.py --group N --arms B --models opus-5 --timeout 900
.venv/bin/python $SD/run_v3.py --group T --arms A,B --models opus-5,gpt-terra --timeout 900

# ④ 汇总 (零 LLM, 纯确定性; 不打印题面与答案正文)
.venv/bin/python $SD/tabulate_v3.py
.venv/bin/python $SD/gen_index.py     # → data/study/st01/eval/runs/c2r_v3/INDEX.md
```

`run_v3.py` 的调用形态: `POST /api/ask`, body `{"question": <题面>, "model": <id>, "corpus": "auto"}`
(`AskRequest` 是 `extra="forbid"`, 无多余键)。5xx / 超时重试 1 次, 仍失败则整包落
`runs/c2r_v3/failures/` (规则 B)。**本轮 failures/ 为空。**

三个 runner 脚本 (`run_v3.py` / `tabulate_v3.py` / `gen_index.py`) 只在 scratchpad, 自身不含任何真值,
题面从 gitignored `questions.json` 读。**本轮零 `server/` 与 `scripts/` 代码改动** (`git status` 与开工前一致)。

## 2. 环境

| 项 | 值 | 取法 |
|---|---|---|
| commit | `0860a87` + 未提交工作树 (I2 改动在树上) | `git rev-parse --short HEAD` |
| Python / uv | 3.14.4 / 0.11.17 | `.venv/bin/python -V`; `uv --version` |
| poppler | `pdftoppm version 26.04.0` (`pdftoppm` 在 `/opt/homebrew/bin`) | `pdftoppm -v` |
| 页索引 | 102,406 B · sha256 `357877dea191c63f…` · generated `2026-09-09T04:09:26Z` · catalog `V59` | `shasum -a 256 data/study/st01/pdf_page_index.json` |
| 索引块数 | workflow 933 页 / 110 块 · annotated 212 页 / 42 块 + 21 item_pages | 读 `pdf_page_index.json` |
| arm B 通道参数 | `pdf_context max_pages=6 dpi=110` (启动日志一行) | `grep pdf_context $SD/armB_8011.log` |
| arm A 通道 | 启动日志**无** `pdf_context` 行 = `app.state.pdf_context is None` | 同上 grep 空 |

模型 (取自 arm B `GET /api/info` 的 `selectable_models`, 按任务要求取 opus-5 + 一个非 Anthropic 家):

| id | model 串 | 本轮用途 |
|---|---|---|
| `opus-5` | `bedrock/converse/global.anthropic.claude-opus-5` | T 组两臂 + N 组 |
| `gpt-terra` | `bedrock/converse/global.openai.gpt-5.6-terra` | T 组两臂 |

`AskResponse` **没有** `fell_back` 字段 (那是 `/api/ask_stream` done 事件才有的), 所以回退检查只能看
`model_used`: 28/28 与请求模型一致 (`opus-5` → `global.anthropic.claude-opus-5` ×16;
`gpt-terra` → `global.openai.gpt-5.6-terra` ×12), **零回退**。
`truncated` 28/28 为 False, `continue_rounds` 28/28 为 0, `continue_error` 全 None。

## 3. T 组 arm B — 触发规则与页 (核心表)

`pdf_trigger` / `pdf_pages` 直接取自 `AskResponse` 字段, 非日志推断。

| qid | 模型 | `pdf_trigger` | 页数 | `pdf_pages` (pdf + 页号) |
|---|---|---|---|---|
| T1 | opus-5 / gpt-terra | **R1** | 6 | annotated p.174, p.175, p.176; workflow p.29, p.74, p.87 |
| T2 | opus-5 / gpt-terra | **R2** | 6 | annotated p.50, p.113, p.116; workflow p.14, p.216, p.252 |
| T3 | opus-5 / gpt-terra | **R1** | 6 | annotated p.4, p.5, p.6; workflow p.80, p.94, p.143 |
| T4 | opus-5 / gpt-terra | **R1** | 6 | annotated p.46, p.52, p.174; workflow p.29, p.74, p.80 |
| T5 | opus-5 / gpt-terra | **R1** | 6 | annotated p.57, p.152, p.174; workflow p.4, p.17, p.315 |
| T6 | opus-5 / gpt-terra | **null** | 0 | — (见 §5) |

**两个模型逐题拿到的规则与页集完全相同** —— 触发与选页是确定性纯函数, 与答题模型无关, 本表因此
每题只写一行。5/6 触发, 命中率 **5/6 = 83.3%**。

选页细节 (arm B 服务日志 `pdf_context_attached` 的数值字段; `reason=` 含真值故不摘录):

| qid | rule | selected | 实际附上 | folded (同屏折叠) | truncated (候选超 6 页上限) |
|---|---|---|---|---|---|
| T1 | R1 | 6 | 6 | 13 | True |
| T2 | R2 | 6 | 6 | 0 | True |
| T3 | R1 | 6 | 6 | 9 | True |
| T4 | R1 | 6 | 6 | 22 | True |
| T5 | R1 | 6 | 6 | 36 | True |

五题**全部**顶到 `max_pages=6` 上限且 `truncated=True` (候选页多于 6)。opus-5 与 gpt-terra 两轮
10 次 attach 的 folded 序列逐位相同 (13/0/9/22/36 各两次), 再次印证选页与模型无关。
`pdf_context_no_pages_rendered` 警告 **0 次** (渲染零失败)。

复跑:

```bash
grep -c pdf_context_attached  $SD/armB_8011.log            # → 10
grep -c pdf_context_no_pages_rendered $SD/armB_8011.log    # → 0
```

## 4. N 组 (arm B, opus-5, flag ON) — 全 null

预登记 §5 通过判据之一。**4/4 达标。**

| qid | `pdf_trigger` | `pdf_pages` | 页数 | `routed_corpus` | 检索到的 sources | 答案字符数 |
|---|---|---|---|---|---|---|
| N1 | null | null | 0 | cdisc | 15 | 1548 |
| N2 | null | null | 0 | study | 23 | 1482 |
| N3 | null | null | 0 | both | 24 | 1128 |
| N5 | null | null | 0 | both | 24 | 2247 |

N5 是 M10 修订专门加的反例: 它在 `corpus=both` 下确实被塞进了 24 条 source (study 侧按配额填充),
`画面` 一词也确实命中 R3 词表, 但相关性下限把它挡住了 —— **这条正是本轮设计里最该验的一条, 已验过。**

## 5. 发现 — T6 两个模型均未触发 (预登记外)

预登记 §1 把 T6 列在「应触发」的 T 组, 实测 `pdf_trigger` 为 null。成因**已用零 LLM 探针钉死**,
不是随机性也不是模型差异:

```bash
.venv/bin/python - <<'EOF'
import json
from server.config import settings as s
from server.study_lookup import StudyLookup
from server.pdf_trigger import _R1_WORDS, _R2_WORDS, _R3_WORDS, _hit
QS = json.load(open("data/study/st01/eval/runs/c2r_v3/questions.json"))
lk = StudyLookup.from_paths(s.study_catalog_path, s.study_aliases_path)
for g in ("T", "N"):
    for q, t in QS[g].items():
        print(q, _hit(t,_R1_WORDS), _hit(t,_R2_WORDS), _hit(t,_R3_WORDS), lk.strong_hit(t))
EOF
```

| qid | R1 命中词 | R2 命中词 | R3 命中词 | `strong_hit` |
|---|---|---|---|---|
| T1 | `visit` | `显示` | — | False |
| T2 | `表示` | `条件` | — | False |
| T3 | `いつ` | `いつ` | `画面` | False |
| T4 | `違い` | — | — | False |
| T5 | `表示` | `条件` | — | False |
| **T6** | **—** | **—** | **`画面`** | **False** |
| N1 / N2 / N3 | — | — | — | False |
| N5 | — | — | `画面` | False |

T6 只能走 R3。R3 在 r2 修订 (I2 复审 M10) 后带**相关性下限**: 必须「命中集合里至少一张卡片经 study
直查注入 (`via_lookup`)」**或**「问题命中直查强通道 (`strong_hit`)」。T6 两者皆无, 于是
`server/pdf_trigger.py:156-163` 返回不触发。**同一条下限同时挡住了 N5 (设计意图) 和 T6 (预登记期望触发)。**

旁证 (确定性, 不依赖日志): T6 两臂 `prompt_tokens` **逐字节相同** —— gpt-terra 22,161 = 22,161,
opus-5 28,549 = 28,549。若挂了 6 张图, arm B 应比 arm A 多约 6×1.4–1.6k token (S0-3 实测的单页图开销);
其余 5 题 arm B 确实每题多出 7.6k–9.5k。这证明 T6 的 arm B 请求**确实一张图都没挂**, 不是挂了没报。

⚠ 本文只报事实, 不提修法。R3 下限该不该放宽、放宽后 N5 会不会回潮, 属 C4 的判断, 且预登记明写
「不达 = 归档 failures/, **不改判分点**」。判分点未动。

## 6. A/B 对照 — 答案长度与墙钟

| qid | 模型 | A 长度 | B 长度 | Δ | A 墙钟 s | B 墙钟 s | A prompt tok | B prompt tok | Δ tok |
|---|---|---|---|---|---|---|---|---|---|
| T1 | opus-5 | 3252 | 4247 | **+995** | 66.3 | 76.0 | 19,999 | 29,580 | +9,581 |
| T1 | gpt-terra | 2660 | 2705 | +45 | 20.2 | 32.6 | 15,326 | 22,948 | +7,622 |
| T2 | opus-5 | 1211 | 1368 | +157 | 27.7 | 28.2 | 17,584 | 27,086 | +9,502 |
| T2 | gpt-terra | 809 | 746 | **−63** | 11.3 | 9.6 | 13,948 | 21,527 | +7,579 |
| T3 | opus-5 | 1992 | 2143 | +151 | 27.7 | 43.9 | 19,653 | 29,235 | +9,582 |
| T3 | gpt-terra | 468 | 905 | **+437** | 6.0 | 17.0 | 15,257 | 22,878 | +7,621 |
| T4 | opus-5 | 2143 | 2866 | **+723** | 42.0 | 62.2 | 25,112 | 34,694 | +9,582 |
| T4 | gpt-terra | 739 | 1147 | +408 | 11.8 | 18.8 | 19,682 | 27,308 | +7,626 |
| T5 | opus-5 | 1554 | 1671 | +117 | 34.3 | 35.1 | 25,666 | 35,171 | +9,505 |
| T5 | gpt-terra | 333 | 443 | +110 | 10.5 | 19.3 | 20,096 | 27,671 | +7,575 |
| T6 | opus-5 | 3757 | 3982 | +225 | 50.3 | 49.3 | 28,549 | 28,549 | **0** |
| T6 | gpt-terra | 1562 | 1957 | +395 | 11.6 | 12.7 | 22,161 | 22,161 | **0** |

- 6 页图的入参开销: opus-5 每题 +9.5k token, gpt-terra +7.6k (与 S0-3 单页 1,564 / 1,370 token × 6 一致)。
- 长度只是**体量**不是质量, 判分归 Reviewer。12 组里 11 组 B 更长, 唯一变短的是 T2/gpt-terra (−63)。
- T6 两臂 token 完全相同 = 未挂图的确定性证据 (§5)。
- 墙钟合计 836.5 s / 28 次。按臂: A-opus 248.3s(6), A-gpt 71.3s(6), B-opus 406.8s(10, 含 N 组 4 次), B-gpt 110.0s(6)。

## 7. 来源标签与引用 (纯字符串存在性, **不判对错**)

`视觉` = 答案含字符串 `画面目視判読`; `引用` = 答案含 `[Source:`。

| qid | opus-5 A 视觉/引用 | opus-5 B 视觉/引用 | gpt-terra A 视觉/引用 | gpt-terra B 视觉/引用 |
|---|---|---|---|---|
| T1 | ✗ / ✓ | **✓** / ✓ | ✗ / ✗ | **✗** / ✓ |
| T2 | ✗ / ✓ | **✓** / ✓ | ✗ / ✓ | **✓** / ✓ |
| T3 | ✗ / ✓ | **✓** / ✓ | ✗ / ✓ | **✓** / ✓ |
| T4 | ✗ / ✓ | **✓** / ✓ | ✗ / ✓ | **✓** / ✓ |
| T5 | ✗ / ✓ | **✓** / ✓ | ✗ / ✓ | **✓** / ✓ |
| T6 | ✗ / ✓ | ✗ / ✓ | ✗ / ✓ | ✗ / ✓ |

- **arm A 12/12 无 `画面目視判読`** —— flag OFF 时来源标签一次都没漂出来 (这正是
  `server/router.py:61` 那条注释担心的失败形态, 本轮零发生)。
- arm B 触发的 5 题里 opus-5 **5/5** 打了标签; gpt-terra **4/5**, 缺的是 T1 —— 它挂了 6 页图、
  答案里也写了这 6 个页号, 却没用规定的标签串。这是**格式面**的观测, 是非对错交 Reviewer。

## 8. 页号一致性 (确定性反捏造检查)

把答案里所有 `p.NN` 形态的页号与该次实际挂上的 6 页做集合比对:

| qid | opus-5 B 答案引用页 | gpt-terra B 答案引用页 | 越界 (不在挂上集合内) |
|---|---|---|---|
| T1 | 29, 74, 87, 174, 175, 176 (6/6) | 29, 74, 87, 174, 175, 176 (6/6) | 无 |
| T2 | 50, 113, 216 (3/6) | 113 (1/6) | 无 |
| T3 | 4, 80, 94, 143 (4/6) | 4 (1/6) | 无 |
| T4 | 29, 74 (2/6) | 74 (1/6) | 无 |
| T5 | 174, 315 (2/6) | 315 (1/6) | 无 |

**24/24 次调用零越界页号**; arm A 12 次答案里**一个 `p.NN` 都没有**。
两模型都只引用真的挂上的页, 没有编出第 7 页。opus-5 平均引用 3.4/6 页, gpt-terra 2.0/6。
T5 的 workflow p.315 正是 S0 §4 人眼坐实过的那一页 (术前 LB 活动块首页), 两模型都引到了它。

## 9. 原始产物

| 路径 | 内容 |
|---|---|
| `data/study/st01/eval/runs/c2r_v3/INDEX.md` | 28 份 run 的索引 + qid→题面真值对照 (gitignored) |
| `data/study/st01/eval/runs/c2r_v3/<arm>_<model>_<qid>.json` | 28 份: `_meta` (arm/model/qid/status/attempts/wall_s) + `request` + 完整 `response` |
| `data/study/st01/eval/runs/c2r_v3/failures/` | **空** (零失败零重试) |
| `data/study/st01/eval/runs/c2r_v3/questions.json` | 题面真值 |
| `data/study/st01/eval/runs/c2r_v3/server_logs/arm{A,B}_*.log` | 两臂服务日志 (含真值, 故收在 gitignored 侧) |

命名: `A_` = flag OFF (:8010), `B_` = `SDTM_RAG_PDF_CONTEXT_ENABLED=true` (:8011)。

## 10. 本轮**没做**的事 (交接边界)

- **没有判分**。判分点在预登记 §1, 由异 subagent Reviewer 按规则 D 执行, 12 份 arm B 答案全量核验 (规则 A, N=12), 结果落 `evidence/step_c2r_v3_audit.md`。
- **没碰任何代码**: `server/` `scripts/` 零改动; 也没重建页索引。
- **没动生产**: 8000 端口的 launchd 服务全程未触碰, 收尾复检 `/api/health` 仍 `{"status":"ok"}`。
- **没跑 G2 零回归** (48 题 golden): 那是 I2-3 的闸, 不在 V3 范围。
- T6 未触发**没有就地修**, 见 §5 末尾。

## 11. attempt 2 (r3b) — T6 のみ再走

> 日付: 2026-09-09 · attempt 1 の T6 不発 (§5) を受けた予登記改訂 **r3b** の実測。
> 手順は attempt 1 と同一 (使い捨てサーバ 8010/8011, `SDTM_RAG_AUTH_ENABLED=false`,
> arm B のみ `SDTM_RAG_PDF_CONTEXT_ENABLED=true`; :8000 の launchd 本番は不触)。
> **本節も零判分** —— 触発と token だけの確定的観測。

### 11-1 r3b が変えたもの (実装側)

R3 の関連性フロア (c)「問いが study のフォームを名指し」の判定を **頁索引の名前表**
(`PdfPageIndex.form_named_in`) でも行うようにした。attempt 1 で T6 が落ちた原因は
`StudyLookup.resolve().form_scopes` を埋めるのが**手書き別名表だけ**で、実データの
別名表が 1 件しか無いこと (T6 が名指しした form は未登録)。別名表を増やす道は
`_apply_study_lookup` の注入を通じて**検索を動かす**ため golden 再走が要る; 名前表を
見る道は触発判定だけを見て検索を 1 件も動かさない。(a)(b) と別名表経由の (c) は存置。

### 11-2 結果 (4 回の実 `/api/ask`, 全 200 零失敗零リトライ)

| arm | model | 墙钟 s | `pdf_trigger` | 添付頁 | prompt tok | completion tok | 答案字数 | 「画面目視判読」出現 |
|---|---|---|---|---|---|---|---|---|
| A | opus-5 | 42.76 | **null** | — | 28,549 | 2,651 | 2,713 | 0 |
| B | opus-5 | 99.87 | **R3** | ann 161 / 162 / 164 · wf 34 / 44 / 79 | 38,626 | 7,645 | 6,411 | 13 |
| A | gpt-terra | 16.00 | **null** | — | 22,161 | 1,222 | 1,754 | 0 |
| B | gpt-terra | 35.34 | **R3** | ann 161 / 162 / 164 · wf 34 / 44 / 79 | 30,111 | 3,241 | 4,724 | 10 |

**両モデルとも R3 で発火し、頁集は 6 頁で完全一致** (attempt 1 の T1–T5 と同じ性質:
選頁は確定的なのでモデル差が出ない)。judged corpus は 4 回とも `study`。

token 差分 (B − A):

| model | prompt | completion |
|---|---|---|
| opus-5 | **+10,077** | +4,994 |
| gpt-terra | **+7,950** | +2,019 |

prompt 側の増分を添付 6 頁で割ると 1 頁あたり **1,325–1,680 token** で、S0 §4-4 の
見積り (≈1.5k/頁) と整合。completion が倍増しているのは画面から読める事実が増えた分で、
質は本節の対象外 (判分は Reviewer)。

### 11-3 反例の再確認 (零 LLM)

`N5` (CDISC 寄りで 画面 を含む問い) は r3b 後も **不発** —— 頁索引の名前表に対して
form OID も form 名も当たらないため。`N4` も同様。実装単体テストで釘付け済み。

### 11-4 原始产物

`data/study/st01/eval/runs/c2r_v3/{A,B}_{opus-5,gpt-terra}_T6_r3b.json` (4 份, gitignored)。
`_meta.amendment = "r3b"` で attempt 1 の 28 份と区別できる。

### 11-5 本節でも**していない**こと

- 判分していない (規則 D: 異 subagent の Reviewer が行う)。
- 別名表 (`lookup_aliases.yml`) は 1 文字も触っていない ⇒ 検索は動いていない。
- T1–T5 と N 組は再走していない (r3b は R3 のフロアだけを緩める変更で、
  R1/R2 経路と N 組の判定には触れない)。
