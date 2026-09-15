"""DM2: 研读包 (Study Dossier) —— 域级映射题「整本喂」的原料, 启动时构建一次.

spec: docs/superpowers/specs/2026-09-15-study-dossier-design.md §3
纯文件读, 无 LLM 无网络; 同一输入永远得到同一 text/sha. 超预算抛错不截断.
⚠ 本文件不写任何 study OID / 表单名 / 日文 label.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TYPE_RE = re.compile(r"^- 型:\s*(?P<typ>[^\s(]+)(?:\s*\(len [^)]*\))?\s*/\s*(?P<req>\S+)", re.MULTILINE)
_CL_ENTRY_RE = re.compile(r"^\s+-\s+(?P<code>\S+)\s*=\s*(?P<label>.+?)\s*$", re.MULTILINE)


class DossierBuildError(RuntimeError):
    pass


@dataclass(frozen=True)
class StudyDossier:
    text: str
    sha: str
    chars: int
    sections: tuple[str, ...]
    n_items: int
    study: str
    version: str


def _frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = _FM_RE.search(text)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def _sec_key(sec: str) -> tuple[int, ...]:
    return tuple(int(p) for p in sec.split(".") if p.isdigit())


def _load_sections(docs_dir: Path, whitelist: Sequence[str]) -> list[tuple[str, str, str, str]]:
    """→ [(section_number, title, page_range, body)] 按自然序; 多 part 拼成一条.
    标题只从最低编号 part 的首行取; 其余 part 原文整段保留, 不丢续页首行.
    part 非整数 fail-loud, 不抛裸 ValueError."""
    want = set(whitelist)
    parts: dict[str, list[tuple[int, str, list[str]]]] = {}
    for p in sorted(docs_dir.glob("*.md")):
        fm, body = _frontmatter(p.read_text(encoding="utf-8"))
        if fm.get("doc_type") != "protocol_section":
            continue
        sec = fm.get("section_number", "")
        if sec.split(".")[0] not in want:
            continue
        lines = body.strip("\n").splitlines()
        pages = f"(p.{fm.get('page_start','?')}-{fm.get('page_end','?')})"
        raw_part = fm.get("part", "1") or "1"
        try:
            part_no = int(raw_part)
        except ValueError:
            raise DossierBuildError(f"{p}: part={raw_part!r} 非整数")
        parts.setdefault(sec, []).append((part_no, pages, lines))
    out = []
    for sec in sorted(parts, key=_sec_key):
        ps = sorted(parts[sec], key=lambda t: t[0])
        _, first_pages, first_lines = ps[0]
        title = next((l.strip() for l in first_lines if l.strip()), sec)
        pieces = ["\n".join(first_lines[1:]).strip("\n")]
        pieces.extend("\n".join(lns).strip("\n") for _, _, lns in ps[1:])
        body = "\n".join(pieces)
        out.append((sec, title, first_pages, body))
    return out


def _load_items(cards_dir: Path) -> tuple[list[tuple[str, int, str]], str, str]:
    """→ ([(form_oid, source_row, line)], study, version). 只取 doc_type=field_card;
    study/version 取按文件名排序后第一张卡 (INDEX/ROUTING 无 frontmatter 会被跳过);
    型解析失败 fail-loud, 不静默吞 '?'."""
    rows: list[tuple[str, int, str]] = []
    bad: list[str] = []
    study = version = "?"
    seen_first = False
    for p in sorted(cards_dir.glob("*.md")):
        fm, body = _frontmatter(p.read_text(encoding="utf-8"))
        if fm.get("doc_type") != "field_card":
            continue
        if not seen_first:
            study, version = fm.get("study", "?"), fm.get("version", "?")
            seen_first = True
        title = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), p.stem)
        m = _TYPE_RE.search(body)
        if not m:
            bad.append(str(p))
            continue
        typ = f"{m['typ']} {m['req']}"
        choices = " ".join(f"{e['code']}={e['label']}" for e in _CL_ENTRY_RE.finditer(body))
        line = f"{title} | {typ}" + (f" | {choices}" if choices else "")
        try:
            row = int(fm.get("source_row", "0") or 0)
        except ValueError:
            # 解析失败回落 0 只影响排序, 有意静默 (型解析失败才 fail-loud: 那影响内容).
            row = 0
        rows.append((fm.get("form_oid", ""), row, line))
    if bad:
        raise DossierBuildError(f"dossier: {len(bad)} field card(s) missing '- 型:' line: {', '.join(bad)}")
    rows.sort(key=lambda t: (t[0], t[1], t[2]))
    return rows, study, version


def build_dossier(docs_dir: Path, cards_dir: Path, *, sections: Sequence[str],
                  max_chars: int) -> StudyDossier:
    secs = _load_sections(Path(docs_dir), sections)
    if not secs:
        raise DossierBuildError(f"dossier: 0 sections matched whitelist {list(sections)} in {docs_dir}")
    items, study, version = _load_items(Path(cards_dir))
    if not items:
        raise DossierBuildError(f"dossier: 0 field cards in {cards_dir}")
    lo, hi = secs[0][0].split(".")[0], secs[-1][0].split(".")[0]
    buf = [f"## A. 研究計画書 (PRT) 抜粋: 第 {lo}-{hi} 章"]
    for sec, title, pages, body in secs:
        buf.append(f"### {title}  {pages}\n{body}")
    buf.append(f"## B. EDC 項目一覧 (全 {len(items)} 件; フォーム / 項目 / OID / 型 / 選択肢)")
    buf.extend(line for _, _, line in items)
    body_text = "\n\n".join(buf)
    sha = hashlib.sha256(f"{study}|{version}|{body_text}".encode("utf-8")).hexdigest()[:12]
    head = (f"# 【本研究 研読パッケージ】 (study={study}, version={version}, sha={sha}, "
            f"{len(secs)} 章 / {len(items)} 項目)\n\n")
    text = head + body_text
    if len(text) > max_chars:
        raise DossierBuildError(
            f"dossier: {len(text)} chars > max_chars={max_chars}; 收窄 dossier_prt_sections, 不截断")
    return StudyDossier(text=text, sha=sha, chars=len(text),
                        sections=tuple(s for s, *_ in secs), n_items=len(items),
                        study=study, version=version)
