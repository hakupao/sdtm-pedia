"""Streamlit UI for SDTM RAG Q&A + Dataset Validation (Phase 1B.4 + 1C.5).

Run (after starting FastAPI server):
  streamlit run ui/streamlit_app.py
"""
from __future__ import annotations

import json
import os

import requests
import streamlit as st

API_URL = os.getenv("SDTM_RAG_API_URL", "http://localhost:8000")

st.set_page_config(page_title="SDTM Knowledge Base", layout="wide")

tab_qa, tab_validate = st.tabs(["Q&A", "Dataset Validation"])

# ── Sidebar (shared) ────────────────────────────────────────────────────

with st.sidebar:
    st.header("Settings")
    model = st.selectbox(
        "Model",
        ["default", "hard", "light"],
        index=0,
        help="default=Sonnet, hard=Opus, light=Haiku",
    )
    top_k = st.slider("Retrieval Top-K", 5, 30, 15)
    domain_filter = st.text_input("Domain filter (e.g. AE, DM)", "")
    file_type_filter = st.selectbox(
        "File type filter",
        [
            "(all)",
            "spec",
            "assumptions",
            "examples",
            "chapter",
            "model",
            "terminology",
            "variable_index",
        ],
    )

    st.divider()
    if st.button("Check API"):
        try:
            r = requests.get(f"{API_URL}/api/health", timeout=5)
            st.success(f"API OK: {r.json()}")
            r2 = requests.get(f"{API_URL}/api/info", timeout=5)
            info = r2.json()
            st.info(
                f"Collection: {info['collection_name']}  \n"
                f"Chunks: {info['chunk_count']}  \n"
                f"Model: {info['default_model']}"
            )
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect. Start server first.")
        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()


# ── Helpers ──────────────────────────────────────────────────────────────


def _render_sources(sources: list[dict]) -> None:
    with st.expander(f"Sources ({len(sources)})"):
        for s in sources:
            label = f"**{s['source']}**"
            if s.get("section"):
                label += f" -- {s['section']}"
            label += f"  (sim: {s['similarity']:.3f})"
            st.markdown(label)
            st.text(s["text_preview"])
            st.divider()


# ══════════════════════════════════════════════════════════════════════════
# Tab 1: Q&A
# ══════════════════════════════════════════════════════════════════════════

with tab_qa:
    st.header("SDTM Knowledge Base Q&A")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "history" not in st.session_state:
        st.session_state.history = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                _render_sources(msg["sources"])

    if prompt := st.chat_input("Ask about SDTM..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Retrieving and generating..."):
                payload: dict = {
                    "question": prompt,
                    "model": model,
                    "top_k": top_k,
                    "history": st.session_state.history[-10:],
                }
                if domain_filter.strip():
                    payload["domain"] = domain_filter.strip().upper()
                if file_type_filter != "(all)":
                    payload["file_type"] = file_type_filter

                try:
                    r = requests.post(
                        f"{API_URL}/api/ask", json=payload, timeout=120
                    )
                    r.raise_for_status()
                    data = r.json()

                    answer = data["answer"]
                    st.markdown(answer)

                    sources = data.get("sources", [])
                    if sources:
                        _render_sources(sources)

                    if data.get("usage"):
                        st.caption(
                            f"Model: {data['model_used']} | "
                            f"Tokens: {data['usage']['total_tokens']}"
                        )

                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer, "sources": sources}
                    )
                    st.session_state.history.append(
                        {"role": "user", "content": prompt}
                    )
                    st.session_state.history.append(
                        {"role": "assistant", "content": answer}
                    )

                except requests.exceptions.ConnectionError:
                    st.error(
                        "Cannot connect to API server. "
                        "Start it first: `uvicorn server.main:app`"
                    )
                except requests.exceptions.HTTPError as e:
                    st.error(
                        f"API error {e.response.status_code}: "
                        f"{e.response.text[:500]}"
                    )
                except Exception as e:
                    st.error(f"Unexpected error: {e}")


# ══════════════════════════════════════════════════════════════════════════
# Tab 2: Dataset Validation
# ══════════════════════════════════════════════════════════════════════════

with tab_validate:
    st.header("SDTM Dataset Validation")
    st.caption("Upload a dataset (CSV/XPT/SAS7BDAT) to validate against the SDTM knowledge base.")

    col_upload, col_options = st.columns([2, 1])

    with col_upload:
        uploaded_file = st.file_uploader(
            "Dataset file",
            type=["csv", "xpt", "sas7bdat"],
            key="validate_file",
        )
        dm_file = st.file_uploader(
            "DM file (optional, for cross-domain USUBJID check)",
            type=["csv", "xpt", "sas7bdat"],
            key="dm_file",
        )

    with col_options:
        domain_override = st.text_input(
            "Domain override (auto-detected if empty)",
            "",
            key="domain_override",
        )
        semantic_review = st.checkbox("Run semantic review (RAG + LLM)", value=True)

    if uploaded_file and st.button("Validate", type="primary"):
        with st.status("Validating dataset...", expanded=True) as status:
            st.write("Uploading and parsing...")

            files: dict = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/octet-stream")}
            form_data: dict = {"semantic_review": str(semantic_review).lower()}
            if domain_override.strip():
                form_data["domain"] = domain_override.strip().upper()

            if dm_file:
                files["dm_file"] = (dm_file.name, dm_file.getvalue(), "application/octet-stream")

            st.write("Running validation rules...")

            try:
                r = requests.post(
                    f"{API_URL}/api/validate",
                    files=files,
                    data=form_data,
                    timeout=120,
                )
                r.raise_for_status()
                report = r.json()

                status.update(label="Validation complete", state="complete", expanded=False)

            except requests.exceptions.ConnectionError:
                status.update(label="Error", state="error")
                st.error("Cannot connect to API. Start server first.")
                st.stop()
            except requests.exceptions.HTTPError as e:
                status.update(label="Error", state="error")
                st.error(f"Validation error: {e.response.text[:500]}")
                st.stop()
            except Exception as e:
                status.update(label="Error", state="error")
                st.error(f"Unexpected error: {e}")
                st.stop()

        # ── Render report ────────────────────────────────────────────
        verdict = report.get("verdict", "?")
        verdict_colors = {"PASS": "green", "PASS_WITH_WARNINGS": "orange", "FAIL": "red"}
        vc = verdict_colors.get(verdict, "gray")

        st.markdown(f"### Verdict: :{vc}[{verdict}]")

        mc1, mc2, mc3, mc4 = st.columns(4)
        mc1.metric("Domain", report.get("domain", "?"))
        mc2.metric("Completeness", f"{report.get('completeness_pct', 0)}%")
        mc3.metric("Errors", report.get("total_errors", 0))
        mc4.metric("Warnings", report.get("total_warnings", 0))

        st.markdown(
            f"**Rows:** {report.get('row_count', 0):,} | "
            f"**Variables:** {report.get('col_count', 0)} | "
            f"**Info:** {report.get('total_info', 0)}"
        )

        # ── Rule-based findings ──────────────────────────────────────
        val = report.get("validation", {})
        findings = val.get("findings", [])
        if findings:
            st.subheader("Rule-Based Findings")
            for sev in ("ERROR", "WARN", "INFO"):
                sev_items = [f for f in findings if f.get("severity") == sev]
                if not sev_items:
                    continue
                with st.expander(f"{sev} ({len(sev_items)})", expanded=(sev == "ERROR")):
                    for f in sev_items:
                        var = f.get("variable", "")
                        rule = f.get("rule", "")
                        msg = f.get("message", "")
                        st.markdown(f"**[{rule}]** `{var}`: {msg}")
                        if f.get("value_sample"):
                            st.caption(f"Sample: {f['value_sample']}")

        # ── Semantic review findings ─────────────────────────────────
        rev = report.get("review")
        if rev and rev.get("findings"):
            st.subheader("Semantic Review (RAG + LLM)")
            st.caption(
                f"Model: {rev.get('model_used', '?')} | "
                f"Tokens: {(rev.get('prompt_tokens', 0) + rev.get('completion_tokens', 0)):,}"
            )
            for f in rev["findings"]:
                sev = f.get("severity", "INFO")
                icon = {"ERROR": "!!!", "WARN": "!!", "INFO": "i"}.get(sev, "?")
                st.markdown(
                    f"**[{icon} {f.get('check_type', '')}]** {f.get('title', '')}\n\n"
                    f"{f.get('detail', '')}"
                )
                if f.get("source_file"):
                    st.caption(f"Source: {f['source_file']}")
                st.divider()

        # ── JSON download ────────────────────────────────────────────
        st.download_button(
            "Download JSON Report",
            data=json.dumps(report, indent=2, ensure_ascii=False),
            file_name=f"sdtm_validation_{report.get('domain', 'unknown')}.json",
            mime="application/json",
        )
