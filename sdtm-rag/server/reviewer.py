"""RAG semantic reviewer for SDTM datasets (Phase 1C.3).

Retrieves domain assumptions/examples via RAG, feeds dataset summary
to LLM for semantic analysis beyond what rule-based checks catch.

5 check types (PLAN §5 1C.3):
  1. Business rules — domain-specific requirements from assumptions.md
  2. Logical consistency — cross-variable relationships
  3. Pattern comparison — alignment with examples.md patterns
  4. Completeness assessment — expected data patterns
  5. Cross-domain relationships — DM/disposition/exposure linkage
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import litellm
import structlog

from server.rag import RAGEngine

log = structlog.get_logger()

MAX_ROWS_FOR_PROMPT = 50
MAX_CHARS_PER_CHUNK = 3000
MAX_CELL_LEN = 80


@dataclass
class SemanticFinding:
    severity: str  # ERROR, WARN, INFO
    check_type: str  # business_rule, logical, pattern, completeness, cross_domain
    title: str
    detail: str
    source_file: str | None = None

    def to_dict(self) -> dict:
        return {
            "severity": self.severity,
            "check_type": self.check_type,
            "title": self.title,
            "detail": self.detail,
            "source_file": self.source_file,
        }


@dataclass
class ReviewResult:
    domain: str
    findings: list[SemanticFinding] = field(default_factory=list)
    model_used: str = ""
    prompt_tokens: int = 0
    completion_tokens: int = 0

    @property
    def error_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "ERROR")

    @property
    def warn_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "WARN")

    def to_dict(self) -> dict:
        return {
            "domain": self.domain,
            "model_used": self.model_used,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "error_count": self.error_count,
            "warn_count": self.warn_count,
            "findings": [f.to_dict() for f in self.findings],
        }


def _sanitize_cell(val: str, max_len: int = MAX_CELL_LEN) -> str:
    """Truncate and strip control chars to mitigate prompt injection."""
    val = val[:max_len].replace("\n", " ").replace("\r", "").replace("\x00", "")
    return val


def _dataset_summary(df, domain: str, variables: list[str]) -> str:
    """Build a compact dataset summary for the LLM prompt."""
    lines = [
        f"Domain: {domain}",
        f"Rows: {len(df)}, Variables: {len(df.columns)}",
        f"Variables present: {', '.join(variables)}",
        "",
        "## Value distributions (top 5 per variable):",
    ]
    for col in variables[:30]:
        if col not in df.columns:
            continue
        vc = df[col].astype(str).value_counts().head(5)
        vals = ", ".join(f"{_sanitize_cell(str(v))}({c})" for v, c in vc.items())
        lines.append(f"  {col}: {vals}")

    lines.append("")
    lines.append(f"## Sample rows (first {min(len(df), MAX_ROWS_FOR_PROMPT)}):")
    sample = df.head(MAX_ROWS_FOR_PROMPT).copy()
    for col in sample.columns:
        sample[col] = sample[col].astype(str).apply(_sanitize_cell)
    lines.append(sample.to_string(index=False, max_colwidth=40))

    return "\n".join(lines)


_REVIEW_SYSTEM_PROMPT = """\
You are an expert SDTM (Study Data Tabulation Model) data reviewer.
You review clinical trial datasets for compliance with CDISC SDTMIG v3.4.

You will receive:
1. Knowledge base context (assumptions and examples for this domain)
2. A dataset summary with variable distributions and sample rows

Perform these 5 checks:
1. **Business Rules**: Check domain-specific requirements from the assumptions
2. **Logical Consistency**: Check cross-variable relationships (e.g., start <= end dates)
3. **Pattern Comparison**: Compare data patterns against examples
4. **Completeness Assessment**: Identify expected data patterns that are missing
5. **Cross-domain Relationships**: Flag potential cross-domain issues

For each finding, respond with a JSON array of objects:
{
  "severity": "ERROR" | "WARN" | "INFO",
  "check_type": "business_rule" | "logical" | "pattern" | "completeness" | "cross_domain",
  "title": "Short title",
  "detail": "Detailed explanation with specific variable/value references",
  "source_file": "KB source file referenced (if any)"
}

Only report genuine issues. Do NOT repeat findings about missing variables or
controlled terminology — those are handled by the rule-based validator.
Focus on semantic and business-logic issues that require domain knowledge.
Respond ONLY with the JSON array (no markdown fences, no extra text).
If no issues found, respond with [].
"""


def review(
    df,
    domain: str,
    variables: list[str],
    rag: RAGEngine,
    *,
    model: str = "hard",
    llm_router=None,
) -> ReviewResult:
    """Run RAG-assisted semantic review on a dataset.

    Args:
        df: Dataset DataFrame.
        domain: SDTM domain code.
        variables: List of variable names in dataset.
        rag: RAGEngine instance for KB retrieval.
        model: LLM model tier ("hard" = Opus for semantic review).
        llm_router: LiteLLM Router instance.

    Returns:
        ReviewResult with semantic findings.
    """
    result = ReviewResult(domain=domain)

    queries = [
        f"{domain} domain assumptions and requirements",
        f"{domain} domain example data patterns",
    ]

    all_chunks = []
    for q in queries:
        chunks = rag.retrieve(q, domain=domain, top_k=8)
        all_chunks.extend(chunks)

    if not all_chunks:
        chunks_general = rag.retrieve(f"SDTM {domain} domain", top_k=10)
        all_chunks.extend(chunks_general)

    seen_ids: set[str] = set()
    unique_chunks = []
    for c in all_chunks:
        if c.chunk_id not in seen_ids:
            seen_ids.add(c.chunk_id)
            unique_chunks.append(c)

    context_parts: list[str] = []
    for c in unique_chunks[:12]:
        text = c.text[:MAX_CHARS_PER_CHUNK]
        context_parts.append(f"[{c.source} -- {c.section or 'N/A'}]\n{text}")
    kb_context = "\n\n---\n\n".join(context_parts)

    ds_summary = _dataset_summary(df, domain, variables)

    user_msg = (
        f"## Knowledge Base Context\n\n{kb_context}\n\n"
        f"---\n\n## Dataset Summary\n\n{ds_summary}"
    )

    messages = [
        {"role": "system", "content": _REVIEW_SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]

    raw = "[]"
    try:
        if llm_router:
            response = llm_router.completion(model=model, messages=messages)
        else:
            response = litellm.completion(model=model, messages=messages)

        result.model_used = getattr(response, "model", model)
        if response.usage:
            result.prompt_tokens = response.usage.prompt_tokens or 0
            result.completion_tokens = response.usage.completion_tokens or 0

        raw = response.choices[0].message.content or "[]"
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
            raw = raw.strip()

        findings_data = json.loads(raw)
        if not isinstance(findings_data, list):
            findings_data = [findings_data]

        for item in findings_data:
            if not isinstance(item, dict):
                continue
            result.findings.append(
                SemanticFinding(
                    severity=item.get("severity", "INFO"),
                    check_type=item.get("check_type", "business_rule"),
                    title=item.get("title", "Untitled"),
                    detail=item.get("detail", ""),
                    source_file=item.get("source_file"),
                )
            )

    except json.JSONDecodeError as e:
        log.error("reviewer_json_parse_fail", error=str(e), raw=raw[:200])
        result.findings.append(
            SemanticFinding(
                "WARN",
                "business_rule",
                "LLM response parse error",
                f"Could not parse reviewer LLM output as JSON: {e}",
            )
        )
    except Exception as e:
        log.error("reviewer_llm_fail", error=str(e))
        result.findings.append(
            SemanticFinding(
                "WARN",
                "business_rule",
                "Semantic review unavailable",
                f"LLM call failed: {e}",
            )
        )

    return result
