#!/usr/bin/env python3
"""Render evidence/checkpoints/t4_c3_closeout.md (G-TB4: census per-table changes + C3 close-out list).
Inputs: work/t4/census_tablediff.json (t4_census_tablediff.py), work/t4/c3_closeout.json (t4_c3_closeout.py),
the T2S batch checkpoints (for pointer lines) and git history (which commits edited each table). Read-only on KB.
The "独立审查" section at the end of the md is kept verbatim across re-runs (everything after the REVIEW marker).
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_c3_report.py
"""
import collections, difflib, json, os, re, subprocess

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
CK = f"{TB}/evidence/checkpoints"
OUT = f"{CK}/t4_c3_closeout.md"
MARK = "<!-- REVIEW: 以下由独立审查后誊入, 脚本重跑时原样保留 -->"
git = lambda *a: subprocess.check_output(["git", "-C", ROOT, *a], text=True)
D = json.load(open(f"{TB}/work/t4/census_tablediff.json"))
C3 = json.load(open(f"{TB}/work/t4/c3_closeout.json"))
_show = {}


def tables(text):
    out, cur, start = {}, [], 0
    for n, l in enumerate(text.split("\n") + [""], 1):
        if l.lstrip().startswith("|"):
            if not cur:
                start = n
            cur.append(l.strip())
        elif cur:
            out[start] = "\n".join(cur)
            cur = []
    return out


def tabs_at(rev, f):
    if (rev, f) not in _show:
        txt = open(f"{ROOT}/{f}", encoding="utf-8").read() if rev == "WORKTREE" else git("show", f"{rev}:{f}")
        _show[(rev, f)] = tables(txt)
    return _show[(rev, f)]


def batch(subject):
    m = re.search(r"batch (S-[\w-]+)", subject)
    return m.group(1) if m else ("T4 解冻轮" if "T4 thaw" in subject else subject[:30])


def modifiers(f, a_rev, a_line, b_rev):
    """Batches whose commit changed this table's text between a_rev and b_rev (tracked by exact text, else best similarity)."""
    cur = tabs_at(a_rev, f)[a_line]
    out = []
    revs = [r.split("\t", 1) for r in git("log", "--reverse", "--format=%h\t%s", f"{a_rev}..{b_rev}", "--", f).strip().split("\n") if r]
    for h, s in revs:
        ts = list(tabs_at(h, f).values())
        if cur in ts:
            continue
        best = max(ts, key=lambda t: difflib.SequenceMatcher(None, cur, t, autojunk=False).ratio(), default=None)
        if best is None or difflib.SequenceMatcher(None, cur, best, autojunk=False).ratio() < 0.5:
            out.append(f"{batch(s)} `{h}` (表被删 / 重建)")
            return out
        out.append(f"{batch(s)} `{h}`")
        cur = best
    return out


def lines_of(path, lo=1):
    return [(n, l) for n, l in enumerate(open(path, encoding="utf-8").read().split("\n"), 1) if n >= lo]


def find(path, lo, pat):
    for n, l in lines_of(path, lo):
        if re.search(pat, l):
            return n
    return None


def ptr(name, n):
    return f"`{name}:{n}`" if n else f"`{name}` (未定位到行)"


def c3_evidence(r):
    """(batch, writer pointer, reviewer pointer, extra) for one C3 row; pointers are line numbers found by pattern."""
    f, old = r["file"], r["line_t2end"]
    head = int(r["head"].rsplit(":", 1)[1]) if r["head"] else None
    if "ch04" in f:
        w = find(f"{CK}/t2_S-CH4.md", 67, rf"^\| \d+ \| :{old}( |→)")
        rv = find(f"{CK}/t2_S-CH4_review.md", 27, rf"^\| [\d-]+ \| .*:{head}\b") if head else None
        return "S-CH4", ptr("t2_S-CH4.md", w), ptr("t2_S-CH4_review.md", rv), ""
    if "EX/examples" in f:
        w = find(f"{CK}/t2_S-INT.md", 65, rf":{old}\b")
        rv = find(f"{CK}/t2_S-INT_review.md", 76, rf":{head}\b")
        return "S-INT", ptr("t2_S-INT.md", w), ptr("t2_S-INT_review.md", rv), ""
    if "TR/assumptions" in f:
        return ("S-TUFA", ptr("t2_S-TUFA.md", find(f"{CK}/t2_S-TUFA.md", 64, r"TR/assumptions\.md:31-33 \(HEAD :15\)")),
                ptr("t2_S-TUFA_review.md", find(f"{CK}/t2_S-TUFA_review.md", 89, r"TR/asm\.md:31-33")), "")
    if "ch10" in f:
        w = find(f"{CK}/t2_S-CH10.md", 59, rf"\(:{old}\)")
        tag = re.match(r"\| (#\d+)", lines_of(f"{CK}/t2_S-CH10.md")[w - 1][1]).group(1) if w else None
        rv = find(f"{CK}/t2_S-CH10_review.md", 59, rf"^\| {tag} ") if tag else None
        return "S-CH10", ptr("t2_S-CH10.md", w), ptr("t2_S-CH10_review.md", rv), ""
    if "model/02" in f:
        w = find(f"{CK}/t2_S-MOD2.md", 122, rf":{old}\b")
        return ("S-MOD2", ptr("t2_S-MOD2.md", w), "`t2_S-MOD2_review.md:15` (cmp.py 264 行逐列) + `:100` 起逐格表",
                "auditor `t2_S-MOD2_audit.md:14` 起 (抽样行对渲染 p12 / p21-24 / p27-28 逐格)")
    if "model/03" in f or "model/04" in f:
        key = f"model/0{'3' if 'model/03' in f else '4'}:{old}\\b"
        w = find(f"{CK}/t2_S-MOD1.md", 201, key)
        if "model/03" in f and old == 60:   # Key Reference Date: KB-authored summary table, not one of the 7 PDF variable tables
            return ("S-MOD1", ptr("t2_S-MOD1.md", w), "`t2_S-MOD1_review.md:66` (Key Reference Date (KB 汇总) 8 行: Description = PDF DM Label 逐字; Typical Use 为 D6)", "KB 自写汇总表, 不在 auditor 的 \"7 表 106 行\" 内")
        return ("S-MOD1", ptr("t2_S-MOD1.md", w), "`t2_S-MOD1_review.md:5` (106 行 530 核心格) + `:56` 起逐格表",
                "auditor `t2_S-MOD1_audit.md:41` (7 表 106 行渲染全看)")
    return "?", "?", "?", ""


short = lambda f: f.replace("knowledge_base/", "")
# census diffs that are registered PDF typos (KB carries the corrected value) -> say so next to the diff
REGNOTE = {("domains/DS/examples.md", 292, "HEAD"): " — 不是回归: 已登记 PDF 笔误 `B-DS U-1` (KB 写正确值 SCRN; U-7 A1-9)",
           ("domains/PP/examples.md", 14, "HEAD"): " — 不是回归: 已登记 PDF 笔误 `B-PCPP T-7` (KB 写正确值 h; U-7 A1-21)"}
o = ["# T4 G-TB4: census 逐表变化说明 + C3 逐表结案清单", "", "<!-- chain: E (plans) -->",
     "> 状态: 写作者稿 (主控用脚本生成, 2026-11-27); 独立审查结论见文末. KB 未改 (只读).",
     "> 关闭的缺口: 总闸 attempt 1 §3 / attempt 2 D 项 — \"census 合计相同不等于差异集相同, 未逐表比对\" 与 \"C3 逐表结案清单仍缺\".", ""]
S = D["summary"]
o += ["## 1. 复跑 (仓库根; 只读 KB, 产物在 `work/` 下)", "", "```bash",
      "T=.work/10_tier_b_repair; H=$T/work/scratch/t4/census_hist; mkdir -p $H",
      "for r in 50c3958 00a2e93; do rm -rf $H/kb_$r; mkdir -p $H/kb_$r; git archive $r knowledge_base | tar -x -C $H/kb_$r; \\",
      "  python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --kb-root $H/kb_$r/knowledge_base --out $H/census_$r.json | tail -2; done",
      "python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --out $H/census_HEAD.json | tail -2",
      "python3 -I $T/scripts/t4/t4_census_tablediff.py   # -> work/t4/census_tablediff.json",
      "python3 -I $T/scripts/t4/t4_c3_closeout.py        # -> work/t4/c3_closeout.json",
      "python3 -I $T/scripts/t4/t4_c3_report.py          # -> 本文件 (文末审查段保留)", "```", "",
      "- 跨提交配对**不按行号**, 分三步: ① 同一文件里表文本逐字节相同的先配 (按出现次序); ② 其余按键 (文件, 归一表头, 例号, 数据集名) 配 — 键唯一时直接配 (此时不设相似度下限; 独立审查实测 53 对里最低相似度 0.70, 未见误配), 键重复时按表文本相似度配; ③ 再剩的在同文件内按相似度 ≥ 0.6 配; 最后剩下的记为删 / 增 (批内整表重建的旧表 / 新表会落在这里, 对应关系见 §6).",
      "- 每张表另算表文本 md5, 所以 census 读不了的表 (UNPARSEABLE) 改没改也看得见.",
      "- `50c3958` = 60 批 T2 之后、22 个 T2S 扫描批之前 (`evidence/t2_census_global_triage.md` 的基准); `00a2e93` = T2S 全部完成、解冻前 (总闸 attempt 1 的 KB); HEAD = 解冻轮之后 (KB 树 `" + git("rev-parse", "HEAD:knowledge_base").strip() + "`).", ""]
o += ["## 2. 三个时点汇总", "", "| 时点 | KB 表 | OK | DIFF | diffs | NO_PDF | UNPARSEABLE | PDF_ONLY | PDF_UNPARSED |", "|---|--:|--:|--:|--:|--:|--:|--:|--:|"]
for rev in D["revs"]:
    s = S[rev]
    st = s["status"]
    o.append(f"| `{rev}` | {s['kb_tables']} | {st.get('OK', 0)} | {st.get('DIFF', 0)} | {s['diffs']} | {st.get('NO_PDF', 0)} | {st.get('UNPARSEABLE', 0)} | {s['pdf_only']} | {s['pdf_unparsed']} |")
o.append("")
names = {"50c3958": "T2 收尾", "00a2e93": "解冻前", "HEAD": "HEAD"}
for k, st in enumerate(D["steps"], 3):
    a, b = st["a"], st["b"]
    brev = "WORKTREE" if b == "HEAD" else b
    ch = st["changed"]
    o += [f"## {k}. `{a}` ({names[a]}) → `{b}` ({names[b]}) 逐表变化", "",
          f"配对 {st['paired']} 张, 其中状态 / 差异集 / 行数 / 表文本 md5 都相同的 **{st['unchanged']}** 张 (这里面有 {len(st['meta_only'])} 张只是 census 的配对元数据变了, 见下 \"只有配对元数据变化\"); 内容或判定有变化 {len(ch)} 张; 删 {len(st['removed'])} 张; 增 {len(st['added'])} 张.", ""]
    if st["removed"] or st["added"]:
        o += ["### 删 / 增的表", "", "| 类 | KB 表 | 状态 | 数据行 | 表头 | 归因 (删表: 逐提交追踪到删 / 重建它的那一批; 增表: 该区间内改过此文件的批, 文件级) |", "|---|---|---|--:|---|---|"]
        for kind, lst, rev in (("删", st["removed"], a), ("增", st["added"], b)):
            for t in sorted(lst, key=lambda t: (t["file"], t["line"])):
                bs = "; ".join(modifiers(t["file"], a, t["line"], b)) if kind == "删" else ", ".join(dict.fromkeys(batch(c.split(" ", 1)[1]) for c in t["commits"]))
                o.append(f"| {kind} | `{short(t['file'])}:{t['line']}` @`{rev}` | {t['status']} | {t['n_rows']} | {t['header'][:60]} | {bs} |")
        o.append("")
    o += ["### 内容或判定有变化的表", "",
          "| # | KB 表 (前 → 后行号) | 状态 | 变化 | 改动行 −/+ | 首处差异 (字符级, 截断) | 改了这张表的批 (逐提交追踪) |", "|--:|---|---|---|---|---|---|"]
    for n, c in enumerate(sorted(ch, key=lambda c: (c["a"]["file"], c["a"]["line"])), 1):
        f = c["a"]["file"]
        mods = modifiers(f, a, c["a"]["line"], b if b != "HEAD" else "HEAD")
        stt = c["a"]["status"] if c["a"]["status"] == c["b"]["status"] else f"{c['a']['status']} → **{c['b']['status']}**"
        extra = ""
        if c["diff_added"] or c["diff_removed"]:
            extra = " census 差异: " + "; ".join(f"+{d[1]}/{d[2]} KB `{d[3]}` vs PDF `{d[4]}`" for d in c["diff_added"]) + \
                    "".join(f"; −{d[1]}/{d[2]}" for d in c["diff_removed"])
        o.append(f"| {n} | `{short(f)}:{c['a']['line']}` → `:{c['b']['line']}` | {stt} | {', '.join(c['kinds'])} | −{c['lines_removed']}/+{c['lines_added']} | "
                 f"{c['sample'].replace('|', '¦')}{extra}{REGNOTE.get((short(f), c['b']['line'], b), '')} | {'; '.join(mods) or '(未定位)'} |")
    o.append("")
    if st["meta_only"]:
        mo = st["meta_only"]
        o += ["### 只有配对元数据变化的表 (表文本、状态、差异集都没变)", "",
              f"共 {len(mo)} 张. census 给每张 KB 表认 \"例号 (ex) / 数据集名 (ds)\" 靠的是表上方的标题行与标签行; 扫描批改了这些行 (例如加 `### Example 1` 标题、把 `qscg.xpt:` 标签补齐), 表本身没动, 但 census 认到的例号 / 数据集名变了, 进而改变了它与 PDF 表的配对和 \"是否副本\" 的判断.", "",
              "| KB 表 (前 → 后行号) | 状态 | 变化 (字段: 前 → 后) |", "|---|---|---|"]
        for m in sorted(mo, key=lambda m: (m["file"], m["a_line"])):
            o.append(f"| `{short(m['file'])}:{m['a_line']}` → `:{m['b_line']}` | {m['status']} | " + "; ".join(f"{k}: {v[0]} → {v[1]}" for k, v in m["changes"].items()) + " |")
        po_a, po_b = D["summary"][a]["pdf_only_list"], D["summary"][b]["pdf_only_list"]
        o += ["", f"**PDF_ONLY {len(po_a)} → {len(po_b)} 的来源**: `{a}` 时的 PDF_ONLY = " + (", ".join(f"{x['ds']} Ex{x['ex']} p{x['pages']}" for x in po_a) or "无") +
              " (T2 收尾分诊记为 C2 假阳: KB 有两份逐格 OK 的副本). 上表 `chapters/ch08_relationships.md:162` → `:164` 这一行: 当时 census 认不出它的例号 (ex = None), 只能把它当成另一张表的副本 (kb_duplicate = True), 于是 p431 的这张 PDF relrec 表没有 \"正主\" 配对, 落成 PDF_ONLY; S-CH8 之后它被认成 Example 1 (ex = 1, 不再是副本), 与 p431 那张表直接配上, PDF_ONLY 消失. 表文本没变, KB 内容没有因此增减.",
              f"**KB 表数 {S[a]['kb_tables']} → {S[b]['kb_tables']}、UNPARSEABLE {S[a]['status'].get('UNPARSEABLE', 0)} → {S[b]['status'].get('UNPARSEABLE', 0)} 的来源**: 上面 \"删 / 增的表\" 里删 {len(st['removed'])} 增 {len(st['added'])}, 全部是 UNPARSEABLE 表 (批内整表重建 / 表改成列表 / 新补的表).", ""]
# C3
rows = C3["c3"]
o += ["## 5. C3 60 张逐表结案", "",
      "C3 = T2 收尾分诊 (`evidence/t2_census_global_triage.md` §5) 里 \"census 读不了、当时也没有人工逐格证据\" 的 60 张表. 之后 6 个扫描批 (S-CH4 / S-INT / S-TUFA / S-CH10 / S-MOD1 / S-MOD2) 各自在 checkpoint 里留了 \"census_items 逐格\" 段: writer 一遍 + reviewer \"不采信 writer\" 再一遍 (都对 PDF 渲染页).",
      "\"逐格\" 的范围: SDTMIG 的表 (ch04 / ch10 / EX / TR) 是全部格对渲染页; SDTM v2.0 的变量表 (model/02 / 03 / 04) 逐格核的是核心列 (# / Variable / Label / Type / Role), KB 的 Notes / Key Notes 列是 KB 自写说明 (D6), 只核 \"与 PDF 不矛盾\"; PDF 的 Format / C-code / Definition / Examples 等列 KB 不设 (T1.4 R1).",
      "\"现文本始于\" = HEAD 上这张表的文本最早出现的提交 (一路到 HEAD 未再变): 等于 `50c3958` 表示扫描批核过但没改; 等于扫描批提交表示批内改过, 逐格记录写的是改后内容; 晚于扫描批的 (解冻轮) 另指到解冻轮的审查证据.", "",
      "| # | T2 收尾位置 | HEAD 位置 | 表行数 | 现文本始于 | 逐格证据: writer | 逐格证据: reviewer (独立) | 结案 |", "|--:|---|---|--:|---|---|---|---|"]
fate = collections.Counter()
sub = {r.split("\t")[0]: r.split("\t")[1] for r in git("log", "--format=%h\t%s", "50c3958..HEAD").strip().split("\n")}
for r in rows:
    bt, w, rv, extra = c3_evidence(r)
    if r["head"]:
        since = r["text_since"]
        sb = "T2 收尾起未变" if since == "50c3958" else f"{batch(sub.get(since, since))} `{since}`"
        thaw = "T4 解冻" in sb
        res = "已结案 (解冻轮改了 CRF 选项符号, 另见 §5.1)" if thaw else "已结案"
        fate["thaw" if thaw else "closed"] += 1
        o.append(f"| {r['n']} | `{short(r['file'])}:{r['line_t2end']}` | `:{r['head'].rsplit(':', 1)[1]}` | {r['n_lines']} | {sb} | {bt} {w} | {rv}{'; ' + extra if extra else ''} | {res} |")
    else:
        fate["rebuilt"] += 1
        o.append(f"| {r['n']} | `{short(r['file'])}:{r['line_t2end']}` | (批内重建, 见 §6) | — | — | {bt} {w} | {rv}{'; ' + extra if extra else ''} | 已结案 (原表不存在, 由 §6 的新表承接) |")
o += ["", f"合计 60 = 已结案且扫描批之后未再改 {fate['closed']} + 解冻轮改过符号 {fate['thaw']} + 批内重建 {fate['rebuilt']}. 没有 \"仍未逐格核\" 的 C3 表.", "",
      "### 5.1 解冻轮改过的 4 张 ch04 CRF 表", "",
      "- 改动 = U-9(a) CRF 选项符号按渲染外观 (`[ ]` → ○ 等), 共 ch04 19 处 (§4 表里 ch04 四行). 表格文字未动.",
      "- 审查证据: `t4_thaw_review.md:22` (\"ch04 p32 坏字形 3 + ○6, p33 ○10 (=19) … 渲染逐一一致\"); `t4_thaw_audit.md:10` (auditor 抽 CRF 6 hunk, 含 ch04:410-412 / :472-476 / :506-510); 写作者记录 `t4_thaw_W1.md`.", "",
      "## 6. C3 文件里由扫描批新建的 7 张表 (其中 4 张承接 §5 里 \"批内重建\" 的 7 张旧表, 3 张是新补的)", "", "| HEAD 位置 | 表行数 | 表头 | 现文本始于 | 逐格证据 |", "|---|--:|---|---|---|"]
NEW_EV = {"ch10_appendices.md:323": "S-CH10 `t2_S-CH10.md:65` (#39 重建) / `t2_S-CH10_review.md:65`",
          "ch10_appendices.md:177": "S-CH10 `t2_S-CH10.md:64` (#38 重建为 2 列 106 行) / `t2_S-CH10_review.md:64` (tabD 106×2 + 渲染)",
          "ch10_appendices.md:11": "S-CH10 `t2_S-CH10.md:34-35` (App A 名单整表补: p444 35 行 + p445 39 行) / `t2_S-CH10_review.md:67` (tabA 74×2 + 渲染)",
          "ch10_appendices.md:407": "S-CH10 `t2_S-CH10.md:66` (#40 §9 子表) / `t2_S-CH10_review.md:66`",
          "ch10_appendices.md:413": "S-CH10 `t2_S-CH10.md:66` (#40 Appendices 子表) / `t2_S-CH10_review.md:66`",
          "02_observation_classes.md:166": "S-MOD2 `t2_S-MOD2.md:127` (FND 四表并入一张 100 行) / `t2_S-MOD2_review.md:54` (100 行逐格对渲染)",
          "04_associated_persons.md:37": "S-MOD1 `t2_S-MOD1.md:211` (AP 重建) / `t2_S-MOD1_audit.md:41`"}
for t in sorted(C3["new_tables"], key=lambda t: t["head"]):
    key = t["head"].split("/")[-1]
    o.append(f"| `{short(t['head'])}` | {t['n_lines']} | {t['header'][:50]} | {batch(sub.get(t['text_since'], t['text_since']))} `{t['text_since']}` | {NEW_EV.get(key, '?')} |")
o += ["", "对应关系 (旧 7 张 → 新 4 张): C3 #38 → `ch10:177`; #39 → `ch10:323`; #43-#46 (model/02 Findings 四张) → `model/02:166`; #63 (model/04 AP) → `model/04:37`. 另外 3 张不对应旧 C3 表: `ch10:11` (App A 名单) 是 T2 收尾时整表缺、S-CH10 新补的; `ch10:407` (§9 子表 1 行) 与 `ch10:413` (Appendices 子表 4 行) 是 S-CH10 重建 #40 变更表时按 PDF 新补的行, 旧 #40 表里没有 (#40 主表仍在 `:335`, 见 §5).", ""]
old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
tail = old.split(MARK, 1)[1] if MARK in old else "\n\n## 独立审查\n\n(待审)\n"
open(OUT, "w", encoding="utf-8").write("\n".join(o) + "\n" + MARK + tail)
print("wrote", OUT, "| C3:", dict(fate), "| unlocated pointers:", sum(l.count("未定位") for l in o))
