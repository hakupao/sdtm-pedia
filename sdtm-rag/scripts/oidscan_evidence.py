#!/usr/bin/env python3
"""OID/label 泄漏扫描 —— 检查拟进 git 的证据/文档文件是否含真实 form/item/event/
activity 的 OID 或 label/name。

红线背景 (2026-08-25, C1): `evidence/failures/t4_step7_retrieval_regression.md` 把
17 处真实 OID (form 2 + item 11 + activity 4) 提交进了 git —— 本仓此前对"零真名"的
纪律靠人工审查维持, `leakscan_evidence.py` 只扫 gold **题面**, 对 OID 泄漏天然盲
(独立复核对这份文件跑过, 结果 CLEAN, 但真名照样在里面)。本脚本把"零真实 OID/label"
也做成可复跑的闸, 与 leakscan_evidence.py 分工互补, 不是替代。

用法:
    ./.venv/bin/python scripts/oidscan_evidence.py [target ...]
                                                  [--catalog PATH] [--show N]

    target 可给 0 个、1 个或多个文件/目录 (目录递归展开)。**不给时用固定的默认
    扫描面** (与 cwd 无关, 见下方"默认扫描面"): `<sdtm-rag>/evidence/`、
    `<git 仓库根>/docs/`、`<sdtm-rag>/docs/`、以及本脚本自身 —— 覆盖 spec §8
    第 1/3 条点名的证据/文档/spec/plan 位置, 外加闸自扫。给了 target 时按 CWD
    解析 (标准 CLI 行为), 不受下面的"默认扫描面用 git 根锚定"规则约束。

默认扫描面 (为什么不能用 cwd 相对路径): `evidence/` 只存在于 `<sdtm-rag>/evidence/`
一处, 但 `docs/` **在两处都存在且内容不同** —— `<git 仓库根>/docs/superpowers/`
放着本仓全部 spec/plan (spec §8 第 1 条点名的对象), `<sdtm-rag>/docs/` 是另一棵
独立小树 (只有 1 个无关文件)。若默认扫描面用 cwd 相对的 `"docs"`, 按文档教的
`cd sdtm-rag` 方式调用时只会展开成 `<sdtm-rag>/docs/`, repo 根的 spec/plan 整棵
**不在扫描面内**, 而闸打印的 `CLEAN` 会让人误信"spec/plan 也扫过了"。故默认目标
一律解析成绝对路径, 用从本文件向上找 `.git` 定位的仓库根锚定, 不依赖调用时的 cwd。

判定规则:
    needle 来源 : --catalog 指向的 catalog.json, 两个独立的 needle 池:
                  (1) OID 池 —— forms[].oid / items[].item_oid / events[].oid /
                      activities[].oid, 四池去重后取并集; len < DEFAULT_MIN_LEN
                      的取值剔除 (2026-08-26 起, 与 label 池同值)。
                  (2) label/name 池 —— forms[].name/description、
                      items[].label/group_name/form_name、events[].name、
                      activities[].name/event_name (spec §8 第 2 条把"真实
                      form/field OID **/ label**"并列, 只扫 OID 池闭合不了该条;
                      同样剔除 len < DEFAULT_MIN_LEN 的取值)。
                  两池取并集后统一过滤 (剔除纯数字 + 公开 CDISC 词汇, 见下)、
                  统一编译进同一条交替正则, 走同一套匹配/allowlist 逻辑。
    过滤        : 剔除**过短取值** (len < DEFAULT_MIN_LEN, 两池同用) —— 2-3 字符
                  OID 与大写缩写/模板占位符/变量名大量撞车, 实测假阳性率 87.5%
                  (26/26 命中来自 4 个短 needle, 无一是真泄漏, 见 c1_redline_triage.md);
                  这个噪声水平下闸无法接进 pre-commit/CI, 会长期红着然后被人为忽略。
                  盲区代价与其边界见 `load_needles` docstring。
                  另剔除纯数字取值 (`str.isdigit()`) —— 否则行号 / 长度字段这类到处
                  出现的数字会被当成"OID 命中", 制造大量假阳性 (教训: 若不过滤,
                  任何写了 `row: 12` 或 `len 34` 的证据文件都会被判 LEAK)。另剔除
                  公开 CDISC 词汇 (标准 domain 码 / 标准变量名 / 零散公开缩写撞车,
                  见 KNOWN_PUBLIC_COLLISIONS) —— 本仓公开讨论 CDISC 标准是常态,
                  不剔除会把"讨论 AE domain"误判成"泄漏私密 AE 表单"。
    匹配        : 每个 needle 按"字母数字边界"做整词匹配 —— **不是**正则 `\b`。
                  `\b` 把下划线算作词内字符, 而本仓的 `study__form__item.md` 文件名
                  约定 (双下划线分隔 form/item) 和多数 activity OID (如 `偽A_FU_偽B`
                  这类拼接式命名) 本身都靠下划线分隔; 真用 `\b` 会漏掉
                  `st01__偽FORM__偽ITEM.md` 里的 `偽FORM`/`偽ITEM` (下划线紧贴, `\b`
                  判定成"词内", 不算边界) —— 这正是本闸要防的那类泄漏最常见的出现
                  形态 (已用真实回归案例复核过, 见 evidence/failures/
                  t4_step7_retrieval_regression.md 的 C1 修复记录)。故边界定义为
                  "前后不是 [A-Za-z0-9]", 下划线和其他符号都算作边界外, 允许被下划线
                  包夹的 needle 命中。label 池的多字/带空格取值同样适用 (边界只检查
                  整个子串两端, 不逐词切)。
    allowlist   : (相对 git 仓库根的路径, needle) 二元组白名单, 命中判为"已知非泄漏"
                  并跳过, 不计入 LEAK, 但仍打印在报告里供人工复核 (不是静默放过)。

退出码:
    0  CLEAN (allowlist 命中已排除)
    1  发现未在 allowlist 的 OID/label 命中
    2  catalog 不存在 / 两个 needle 池全空 / 有 target 路径不存在, 拒绝给结论
       (fail-closed —— 目标路径拼错或 cwd 不对不能悄悄放行成 CLEAN, needle 集
       为空也一样"没扫到不构成任何保证", 与 leakscan_evidence.py 缺 gold set 时
       的处理同一纪律)

输出脱敏 (2026-08-25, 复审第 3 轮教训): 一把用来防红线的工具, 若自己的命中输出
把真名打进 stdout, 红线就从 git 绕道进了 CI 日志/issue/贴给 LLM 的截图 —— U6 §9
第 6 条明写过这个模式。**默认掩码**: 命中行只打 `file:line: <OID len=N>` /
`file:line: <LABEL len=N>`, 不打真值, 定位信息足够复现但不泄漏。真要看真值 (仅限
本机排查), 加 `--show-values`。rc 语义不受影响。
"""

import argparse
import json
import re
import sys
from pathlib import Path


def _find_git_root(start: Path) -> Path:
    """从 start 向上找含 `.git` 的目录 —— 默认扫描面靠这个锚定, 不依赖调用时 cwd
    (N2 修复: 之前默认目标是 cwd 相对的裸字符串, `cd sdtm-rag` 后调用会让 repo 根的
    `docs/superpowers/` spec/plan 整棵漏出扫描面, 但闸仍打印 CLEAN)。"""
    p = start.resolve()
    for candidate in (p, *p.parents):
        if (candidate / ".git").exists():
            return candidate
    raise RuntimeError(f"未找到 .git —— 无法定位仓库根 (从 {start} 向上找)")


# needle 最短长度 —— OID 池与 label 池同用一个默认值。低于它的取值永远进不了池,
# 因此**任何短于本值的 allowlist / KNOWN_PUBLIC_COLLISIONS 条目都是恒不触发的死代码**
# (由 test_*_are_reachable_under_default_min_len 两条元测试看守)。
DEFAULT_MIN_LEN = 4

REPO_ROOT = Path(__file__).resolve().parent.parent    # sdtm-rag/
GIT_ROOT = _find_git_root(Path(__file__))              # sdtm-pedia/ (可能与上面不同)
_SELF_PATH = Path(__file__).resolve()

DEFAULT_CATALOG = REPO_ROOT / "data" / "study" / "st01" / "catalog.json"
# 全部解析成绝对路径 (见模块 docstring"默认扫描面"段): evidence/ 只在 sdtm-rag/ 下有,
# docs/ 两处都有且内容不同, 都要覆盖; 闸自扫见 N-系列复审 (闸源码自己含 2 个真实 OID
# 当 allowlist 键, 若闸不自扫, 这 2 项就"因为在扫描面外而巧合地清白", 不是走正规
# allowlist 路径判出来的)。
DEFAULT_TARGETS: tuple[Path, ...] = (
    REPO_ROOT / "evidence",
    GIT_ROOT / "docs",
    REPO_ROOT / "docs",
    # 源码树 (2026-08-26 加入): C1 那次真实泄漏就在 `scripts/tests/` 里, 而当时默认面
    # 只有 evidence/ + docs/ —— "手跑一次闸"这个动作天然看不见它。pre-commit 只管新
    # 进 git 的文件, 存量面只能靠不带参数的全仓审计, 故默认面必须含源码。
    # 代价: 默认面 205 → 538 文件, 实测 10.0s → 11.3s (每文件约 62ms, 见
    # precommit_oidscan.py 的说明); 手动审计能接受, 这也正是 hook 不用默认面的原因。
    REPO_ROOT / "scripts",
    REPO_ROOT / "server",
    _SELF_PATH,
)

# 本仓 (sdtm-pedia) 公开发布的标准 SDTM domain 目录名 —— 全部是 CDISC 公开标准
# 词汇 (本 KB 的主题本身), 不是私密标识。EDC 表单常直接借用 domain 码做 form_oid
# (如 AE 表单 ↔ AE domain), 会与 catalog 的 forms[].oid 撞车; 若不剔除, 任何讨论
# AE/DM/LB/PR 等标准 domain 的证据文件都会被误判 LEAK。
# (具体假阳性数字不写死在这里 —— 数字随扫描面/needle 集版本漂移, 写死的绝对数在
# 复审第 4 轮被证明复现不出来, 见仓规矩"假实测比缺陷更害人"; 要看当前实际影响,
# 拿 --show-values 关掉三层排除各自跑一遍自行核对, 不要引用本文件里的历史数字)。
_CDISC_DOMAINS_DIR = GIT_ROOT / "knowledge_base" / "domains"
# 同理: 标准 SDTM 变量名 (STUDYID/AGE/VISIT/...) 也是公开词汇, 且 EDC item_oid 常
# 直接借用变量名 (item 是"这题录入哪个变量"的载体)。来源同一份已生成产物, 不新
# 引入数据依赖。
_VARIABLE_INDEX_PATH = GIT_ROOT / "knowledge_base" / "VARIABLE_INDEX.md"
_VARIABLE_ROW_RE = re.compile(r"^\| ([A-Z0-9_]+) \|", re.M)

# 全局排除 (不分文件, 对整个仓库任何位置都放行) —— 只留"token 本身不含研究识别
# 信息, 在任何上下文出现都是公开知识"的极窄集合。与 domain/变量码同类问题, 但
# 来源零散, 没有单一权威文件可读, 只能手工列, 每条附一句话理由供审计追溯。
# ⚠ SCRT 是本研究实际的 form/event/activity name (label 池命中, 不是 OID), **不是**
# 通用公开缩写这么简单 —— 它同时也是公开肿瘤学治疗方案缩写 (Short Course
# RadioTherapy), 两者字面重合。放这里是明知故犯的盲区: 放行后, 今后任何证据文件
# 写出这个真实事件名都不会被本闸抓到。之所以不改走 per-file ALLOWLIST, 是因为
# 现在只在 1 个文件命中、且那处用法明确是"公开肿瘤学缩写举例", 但**这条豁免不会
# 随文件搬家或复用而失效** —— 下一个人如果要在别的地方引用这个真实事件名, 本闸
# 另有 5 条 (len<4) 公开词汇条目与 11 条 ALLOWLIST 条目已于 2026-08-26 删除: OID 池
# 加了 min_len 后它们的 needle 根本进不了 needle 池, 条目恒不触发 = 死代码
# (由 test_*_are_reachable_under_default_min_len 两条元测试看守)。
KNOWN_PUBLIC_COLLISIONS: dict[str, str] = {
    "RECIST": "公开肿瘤学标准 (Response Evaluation Criteria in Solid Tumors), 非私密标识",
    "WEIGHT": "CDISC 标准 Controlled Terminology 取值 (VSTESTCD codelist 里的公开码, 如 C49678)",
    "HEIGHT": "同上 (VSTESTCD codelist, 如 C49679)",
    "有害事象": "CDISC AE domain 的标准日文译名 (\"不良事件\"), 用作 routing_signals.py 的"
              "通用术语关键词与 gold 题面示例, 与 AE/DM 等标准 domain 码同类, 非私密标识",
    "SCRT": "公开肿瘤学治疗方案缩写 (Short Course RadioTherapy) 与本研究真实 form/"
            "event/activity name 字面重合 —— 见上方大段警告, 这是有意保留的全局盲区",
    "CTCAE": "公开 NCI/FDA 不良事件分级标准 (Common Terminology Criteria for Adverse "
             "Events), 证据文件里作为举例出现",
    "SF-36": "公开健康调查量表名 (Short Form-36 Health Survey), 且**逐字出现在本仓公开 "
             "knowledge_base 的 CDISC SDTMIG 原文**里 (chapters/ch04_general_assumptions.md "
             "§4.1.7 拆分域示例 \"QS36 for SF-36\") —— 谈 QS domain 必然写到它",
}

# 明确不算泄漏的 (相对 git 仓库根的路径, needle) —— 每条必须附一句话理由, 供审计
# 追溯。路径相对 GIT_ROOT (仓库根, 即 sdtm-pedia/), 用 posix 分隔符 —— 与默认扫描面
# 现在能覆盖仓库根内任意位置一致。这一档管的是"只在特定文件里才成立"的例外 (如
# 测试固件里刻意保留的真实临床用语、计划文档里的合成 fixture 值、模板占位符与真实
# needle 偶然撞车), 或闸源码自己因构造 allowlist/collisions 说明文字而必然写出的
# needle 字面量; token 本身放哪都安全的公开词汇走上面 KNOWN_PUBLIC_COLLISIONS 那档。
ALLOWLIST: dict[tuple[str, str], str] = {
    ("sdtm-rag/scripts/tests/test_build_field_cards.py", "EMVI"): (
        "真实 item OID, 但用作直肠癌 MRI 通用临床判读用语 "
        "(test_flat_preserves_bare_less_than_in_real_criteria), "
        "早于本任务已存在于仓库, 非本次改动引入"
    ),
    ("sdtm-rag/scripts/oidscan_evidence.py", "EMVI"): (
        "本闸把上面那条 allowlist 的 needle 字面量写进了自己的源码 (字典键必须是"
        "真实字符串才能匹配) —— 闸源码现已纳入默认扫描面自扫, 这条自引用因此需要"
        "走正规 allowlist, 不能靠「不在扫描面内」侥幸清白"
    ),
}

# 明显非文本的扩展名, 不尝试解码 (evidence/docs 下实测含 .png)
_BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".xlsx", ".zip"}


def load_cdisc_domain_codes(domains_dir: Path = _CDISC_DOMAINS_DIR) -> set[str]:
    """→ `knowledge_base/domains/` 下的目录名集合 (公开标准 domain 码); 目录不存在
    时返回空集并由调用方决定是否提示 (脚本仍可用, 只是失去这层过滤)。"""
    if not domains_dir.is_dir():
        return set()
    return {p.name for p in domains_dir.iterdir() if p.is_dir()}


def load_cdisc_variable_names(index_path: Path = _VARIABLE_INDEX_PATH) -> set[str]:
    """→ `knowledge_base/VARIABLE_INDEX.md` 表格第一列 (公开标准变量名, 如 AGE/VISIT);
    文件不存在时返回空集, 处理方式与 domain 码一致。"""
    if not index_path.is_file():
        return set()
    text = index_path.read_text(encoding="utf-8")
    return set(_VARIABLE_ROW_RE.findall(text))


def load_needles(catalog_path: Path, exclude: set[str] | None = None,
                 min_len: int = DEFAULT_MIN_LEN) -> set[str]:
    """→ catalog 四池 **OID** 的去重并集, 已剔除纯数字取值、过短取值与 `exclude`。

    label/name 池见 `load_label_needles` —— 两池分开加载, 由调用方 union。

    `min_len` 剔除过短取值 (默认 4, 与 label 池同值): 2-3 字符 OID 与大写缩写 /
    build 模板占位符 / Python 变量名 / CDISC 公开变量名大量撞车。**实测依据**
    (`evidence/checkpoints/c1_redline_triage.md`): 本闸对 `scripts/ server/` 报出的
    26 处命中**全部**来自 4 个 2-3 字符 OID needle, 逐条判定无一是真泄漏 ——
    假阳性率 **87.5% (28/32)**。这个噪声水平下闸无法接进 pre-commit/CI: 它会长期
    红着, 然后必然被人为忽略, 与"纸面规则等于没规则"同一种死法。

    **已知盲区 (不藏, 数字为 2026-08-26 本仓实测)**: 原始去重非数字 OID 1071 个中
    70 个 (6.5%) 长度 < 4, 有效 needle 池因此 1060 → 997 (净减 63; 差额 7 是本来就
    在公开词汇排除集里的)。但**盲区远小于这 70 个** —— 用短 OID 的 70 条记录
    (forms 13 + items 57) 里, **63 条自身名称仍在 label 池**, 成对泄漏时由 label 侧
    抓到 (C1 那次真实泄漏正是"OID 与其 label 同行成对"的形态; 由
    `test_short_oid_paired_with_its_label_still_leaks_via_label_pool` 看守, 该测试经
    两次变异实测会红)。**真正全盲的只有 7 条** (forms 5 + items 2): 短 OID 且自身
    名称也过短/被排除。用户 2026-08-26 裁定接受该盲区。
    """
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    raw: set[str] = set()
    for f in catalog.get("forms", []):
        raw.add(f.get("oid", ""))
    for i in catalog.get("items", []):
        raw.add(i.get("item_oid", ""))
    for e in catalog.get("events", []):
        raw.add(e.get("oid", ""))
    for a in catalog.get("activities", []):
        raw.add(a.get("oid", ""))
    exclude = exclude or set()
    return {n for n in raw
            if n and len(n) >= min_len and not n.isdigit() and n not in exclude}


def load_label_needles(catalog_path: Path, exclude: set[str] | None = None,
                       min_len: int = DEFAULT_MIN_LEN) -> set[str]:
    """→ catalog 的 form/item/event/activity **名称/标签**字段 (非 OID) 去重集合。

    spec §8 第 2 条把"真实 form/field OID **/ label**"并列 —— 只扫 OID 池闭合不了
    该条 (审查方实测: 构造一份只含真实 form name + item label + group_name、不含
    任何真实 OID 的文件, 旧版闸判 CLEAN)。字段选取: forms.name/description,
    items.label/group_name/form_name, events.name, activities.name/event_name
    (仅这几个, 不外扩 —— 与复核方的参照实现同一套字段, 便于交叉核数)。
    `min_len` 剔除过短取值 (默认 4): group_name/form_name 这类字段常见 1-3 字的
    通用词 (如单字缩写), 太短会重蹈"纯数字"式的大面积假阳性覆辙。
    """
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    raw: set[str] = set()
    for f in catalog.get("forms", []):
        raw.add(f.get("name") or "")
        raw.add(f.get("description") or "")
    for i in catalog.get("items", []):
        raw.add(i.get("label") or "")
        raw.add(i.get("group_name") or "")
        raw.add(i.get("form_name") or "")
    for e in catalog.get("events", []):
        raw.add(e.get("name") or "")
    for a in catalog.get("activities", []):
        raw.add(a.get("name") or "")
        raw.add(a.get("event_name") or "")
    exclude = exclude or set()
    return {
        v.strip() for v in raw
        if v and len(v.strip()) >= min_len
        and not v.strip().isdigit()
        and v.strip() not in exclude
    }


def compile_needle_pattern(needles: set[str]) -> re.Pattern:
    """把整个 needle 集编译成**一条**交替正则, 而不是"每个 needle 一条正则, 逐个
    对每行 search" —— 后者是 O(needle 数 × 行数), needle 集上千、目标文件上万行时
    (实测 evidence/checkpoints/*.json 单文件近万行) 会话把交互命令拖出 120s 超时。
    单条交替正则一次 `finditer` 扫完一行是 O(行数), 快了两个数量级。
    最长优先排列只是让交替分支里子串更专一的 needle 先试, 不影响本设计的正确性
    (整词边界已保证不会有"短 needle 抢到长 needle 的一部分"这类问题)。
    """
    alts = sorted((re.escape(n) for n in needles), key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z0-9])(" + "|".join(alts) + r")(?![A-Za-z0-9])")


def iter_target_files(targets: list[Path]) -> tuple[list[Path], list[Path]]:
    """→ (files, missing)。targets 里任何一项既不是目录也不是文件就进 missing ——
    调用方必须 fail-closed (N1 修复: 之前拼错路径 / cwd 不对会静默展开成空列表,
    最终打印 CLEAN 且 rc=0, 与本模块自己写的"缺 needle 就拒绝给结论"直接冲突;
    目标路径缺失是同一类问题, 必须同样不给结论)。"""
    out: list[Path] = []
    missing: list[Path] = []
    for p in targets:
        if p.is_dir():
            out.extend(sorted(q for q in p.rglob("*")
                              if q.is_file() and q.suffix.lower() not in _BINARY_EXT))
        elif p.is_file():
            out.append(p)
        else:
            missing.append(p)
    return out, missing


def mask_needle(needle: str, kind: str) -> str:
    """→ 命中输出的默认展示形态 —— 只报类型与长度, 不报真值 (见模块 docstring
    "输出脱敏"段)。`kind` 是 "OID" 或 "LABEL" (由调用方按 needle 出自哪个池判定)。"""
    return f"<{kind} len={len(needle)}>"


def scan_file(path: Path, pattern: re.Pattern) -> list[tuple[int, str]]:
    """→ [(行号, needle), ...]; 二进制/解码失败的文件返回空 (不是本闸的扫描面)。"""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    out: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        out.extend((lineno, m.group(1)) for m in pattern.finditer(line))
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("targets", nargs="*",
                        help="待扫描的文件/目录 (缺省: 见模块 docstring 默认扫描面)")
    parser.add_argument("--catalog", default=str(DEFAULT_CATALOG),
                        help=f"catalog.json 路径 (默认 {DEFAULT_CATALOG})")
    parser.add_argument("--show", type=int, default=50, help="最多打印几条命中明细")
    parser.add_argument(
        "--show-values", action="store_true",
        help="打印命中的真实取值而不是掩码 <OID len=N>/<LABEL len=N>。"
             "⚠ 仅限本机排查, 输出含真名, 不要贴进 issue/CI 日志/发给任何 LLM/"
             "任何形式的截图分享。")
    args = parser.parse_args(argv)

    catalog_path = Path(args.catalog)
    if not catalog_path.exists():
        print(f"ABORT: catalog 不存在: {catalog_path} —— 拒绝给结论 (needle 集为空 "
              "不构成任何扫描保证)。")
        return 2

    cdisc_domains = load_cdisc_domain_codes()
    cdisc_variables = load_cdisc_variable_names()
    cdisc_collisions = set(KNOWN_PUBLIC_COLLISIONS)
    cdisc_public = cdisc_domains | cdisc_variables | cdisc_collisions

    oid_raw = load_needles(catalog_path)               # 已剔除纯数字, 未剔除公开词汇
    label_raw = load_label_needles(catalog_path)        # 已剔除纯数字+过短, 未剔除公开词汇
    needles_raw = oid_raw | label_raw
    needles = {n for n in needles_raw if n not in cdisc_public}
    # 掩码展示要报"这是 OID 还是 label" —— 按池归类; 理论上两池可能撞出同一字符串
    # (未实测遇到过), 此时 OID 优先 (对定位/复核更直接), 靠 dict 更新顺序实现。
    needle_kind: dict[str, str] = {n: "LABEL" for n in label_raw}
    needle_kind.update({n: "OID" for n in oid_raw})
    if not needles:
        print(f"ABORT: {catalog_path} 的 OID 池与 label 池合并后为空 —— "
              "拒绝给结论 (同上, fail-closed)。")
        return 2
    if not cdisc_domains:
        print(f"警告: 未找到 {_CDISC_DOMAINS_DIR}, 未剔除标准 CDISC domain 码 —— "
              "若目标文件讨论标准 domain (AE/DM/...), 可能出现假阳性。")
    if not cdisc_variables:
        print(f"警告: 未找到 {_VARIABLE_INDEX_PATH}, 未剔除标准 CDISC 变量名 —— "
              "若目标文件讨论标准变量 (AGE/VISIT/...), 可能出现假阳性。")

    # pattern 提前到这里编译 (原来在 target 解析之后) —— 下面 ABORT 分支要打印的
    # 缺失路径本身也可能含真名 (用户手滑传了真实卡片路径但打错了字), 必须先有
    # pattern 才能对路径做同款掩码 (复审第 4 轮 Item 2)。
    pattern = compile_needle_pattern(needles)

    def _display(needle: str) -> str:
        # 默认掩码, --show-values 才打真值 (模块 docstring "输出脱敏" 段)。
        if args.show_values:
            return repr(needle)
        return mask_needle(needle, needle_kind.get(needle, "?"))

    def _display_path(text: str) -> str:
        # 路径/文件名同样要掩码 —— study__form__item.md 文件名约定本身就是真名的
        # 载体, R3 只掩了打印出的 needle 本身, 没掩路径, 复审第 4 轮实测: 954/961
        # 张卡片文件名即真名, 默认模式扫 30 张卡仍会在 stdout 打出真名 (全部经由
        # 路径行, _display() 那份贡献 0)。用同一条 pattern 把路径文本里的 needle
        # 子串也替换成掩码。
        if args.show_values:
            return text
        return pattern.sub(lambda m: mask_needle(m.group(0), needle_kind.get(m.group(0), "?")),
                           text)

    # target 解析: 显式给了就按 CWD 解析 (标准 CLI 行为); 不给就用已经绝对化、
    # 锚定 GIT_ROOT/REPO_ROOT 的 DEFAULT_TARGETS (N2 修复, 见模块 docstring)。
    targets = [Path(t) for t in args.targets] if args.targets else list(DEFAULT_TARGETS)
    files, missing = iter_target_files(targets)
    if missing:
        print(f"ABORT: {len(missing)} 个 target 路径不存在, 拒绝给结论 (fail-closed —— "
              "拼错路径/cwd 不对不能悄悄放行成 CLEAN):")
        for m in missing:
            print(f"    缺失: {_display_path(str(m))}")
        return 2
    if not files:
        # N1 原来只关了"路径不存在"这一半门: 路径**存在**但展开后 0 个文件 (空目录 /
        # 只含二进制扩展名) 仍会往下走到"0 个文件, 0 处命中" → CLEAN rc=0, 同样是
        # "扫了个寂寞"却给绿灯 (复审第 4 轮 Item 3)。目录/文件都存在但没东西可扫,
        # 与路径整个不存在是同一类不给结论的场景。
        print(f"ABORT: target 展开后 0 个文件可扫 —— 拒绝给结论 (fail-closed, 同上): "
              f"{[_display_path(str(t)) for t in targets]}")
        return 2

    excluded_n = len(needles_raw) - len(needles)
    print(f"catalog     : {catalog_path} (OID {len(oid_raw)} 个 + label {len(label_raw)} 个 "
          f"→ 去重合并后 {len(needles)} 个 needle; 已剔除纯数字/过短取值 + "
          f"{excluded_n} 个公开 CDISC 词汇 [domain {len(cdisc_domains & needles_raw)} / "
          f"变量名 {len(cdisc_variables & needles_raw)} / 零散撞车 "
          f"{len(cdisc_collisions & needles_raw)}])")
    print(f"targets     : {[_display_path(str(t)) for t in targets]} → {len(files)} 个文件")

    # rel 与 (path, lineno, needle) 一起存, 打印时直接用而不是重算 —— 重算过一次
    # key 用来判 allowed/leak, 打印时再重算一次很容易两处算出不一致的 key (曾经真的
    # 错过一回: 判定用 rel, 打印用 str(path), 两者不同导致 KeyError, 靠单测揪出来)。
    leaks: list[tuple[str, int, str]] = []
    allowed: list[tuple[str, int, str]] = []
    for path in files:
        try:
            rel = path.resolve().relative_to(GIT_ROOT).as_posix()
        except ValueError:
            rel = path.as_posix()
        for lineno, needle in scan_file(path, pattern):
            key = (rel, needle)
            if key in ALLOWLIST:
                allowed.append((rel, lineno, needle))
            else:
                leaks.append((rel, lineno, needle))

    if allowed:
        print(f"\nallowlist 命中 ({len(allowed)} 条, 已知非泄漏, 不计入 LEAK):")
        for rel, lineno, needle in allowed:
            print(f"    {_display_path(rel)}:{lineno}: {_display(needle)} — "
                  f"{ALLOWLIST[(rel, needle)]}")

    if leaks:
        print(f"\nLEAK: {len(leaks)} 处未在 allowlist 的真实 OID/label 命中"
              + ("" if args.show_values else " (默认掩码, 加 --show-values 看真值)"))
        for rel, lineno, needle in leaks[: args.show]:
            print(f"    {_display_path(rel)}:{lineno}: {_display(needle)}")
        if len(leaks) > args.show:
            print(f"    ... 另 {len(leaks) - args.show} 处")
        return 1

    print(f"\nCLEAN: 0 处未在 allowlist 的 OID/label 命中 ({len(files)} 个文件)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
