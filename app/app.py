
import os
import sys

APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

import streamlit as st

# Shown on the diagnostic screen so we can verify WHICH build is live on Streamlit Cloud.
BUILD_MARKER = "diag-1610-a"

try:
    from src.screens.home_screen import home_screen
    from src.screens.teacher_screen import teacher_screen
    from src.screens.student_screen import student_screen
    from src.components.dialog_auto_enroll import auto_enroll_dialog
except Exception as exc:
    # Catches ImportError/ModuleNotFoundError (missing packages) AND secrets errors
    # (StreamlitSecretNotFoundError) — any failure while loading the app's modules.
    # Streamlit redacts the uncaught-traceback message, but this rendered text is NOT redacted,
    # so the real missing module name stays visible for debugging.
    import importlib.util
    import traceback

    st.set_page_config(page_title="SnapClass - import diagnostics", page_icon=":wrench:")
    st.error(f"Import failed — build marker: {BUILD_MARKER}")
    st.subheader("Real error (not redacted)")
    st.code(f"{type(exc).__name__}: {exc}", language="text")
    st.subheader("Full traceback")
    st.code(traceback.format_exc(), language="text")
    try:
        spec = importlib.util.find_spec("supabase")
    except Exception as spec_exc:  # pragma: no cover - diagnostic only
        spec = f"find_spec raised: {spec_exc!r}"
    st.subheader("Environment")
    st.code(
        f"python: {sys.version}\n"
        f"supabase find_spec: {spec}\n"
        f"sys.path[:6]: {sys.path[:6]}",
        language="text",
    )
    st.subheader("Module availability (is it ONLY supabase, or everything?)")
    import importlib

    rows = []
    for mod in ["streamlit", "supabase", "bcrypt", "segno", "numpy", "torch", "pandas"]:
        try:
            importlib.import_module(mod)
            rows.append(f"{mod}: OK")
        except Exception as mod_exc:
            rows.append(f"{mod}: FAIL -> {type(mod_exc).__name__}: {mod_exc}")
    st.code("\n".join(rows), language="text")
    st.subheader("Installed distributions (count + supabase presence)")
    try:
        from importlib import metadata

        dists = sorted(d.name for d in metadata.distributions())
        supa = [d for d in dists if "supabase" in d.lower() or d in ("postgrest", "storage3", "realtime")]
        st.code(
            f"total distributions: {len(dists)}\n"
            f"supabase-related: {supa}\n"
            f"first 25: {dists[:25]}",
            language="text",
        )
    except Exception as dist_exc:
        st.code(f"distributions failed: {dist_exc!r}", language="text")
    st.caption(
        "Screenshot this whole box and share it — it contains the exact missing module name."
    )
    st.stop()

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()