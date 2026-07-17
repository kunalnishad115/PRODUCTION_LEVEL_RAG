import streamlit as st

from app.ui.sidebar import render_sidebar
from app.ui.chat import render_chat
from app.ui.document_panel import render_document_panel

from app.services.app_state_service import AppStateService


# =====================================================
# Streamlit Config
# =====================================================

st.set_page_config(
    page_title="Ask My Docs",
    page_icon="📄",
    layout="wide"
)

# =====================================================
# Session State
# =====================================================

if "indexed_documents" not in st.session_state:
    st.session_state.indexed_documents = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =====================================================
# Restore Previous State
# =====================================================

if AppStateService.has_indexed_documents():

    if not st.session_state.indexed_documents:

        st.session_state.indexed_documents.append(
            "Previously Indexed Documents"
        )

# =====================================================
# UI
# =====================================================

st.title("📄 Ask My Docs")

st.markdown(
    """
    Production Ready RAG Application
    """
)
render_sidebar()
render_document_panel()
render_chat()