import shutil
import streamlit as st
from app.config.settings import RAW_DATA_DIR
from app.services.indexing_service import IndexingService
from app.vectorstore.vectorstore_factory import (
    VectorStoreFactory
)


def render_sidebar():

    st.sidebar.title("📂 Document Manager")

    uploaded_file = st.sidebar.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    # -----------------------------
    # Upload PDF
    # -----------------------------

    if uploaded_file is not None:

        save_path = RAW_DATA_DIR / uploaded_file.name

        with open(save_path, "wb") as file:

            shutil.copyfileobj(
                uploaded_file,
                file
            )

        st.sidebar.success(
            f"{uploaded_file.name} uploaded successfully."
        )

        # -----------------------------
        # Index Document
        # -----------------------------

        if st.sidebar.button(
            "🚀 Index Document",
            use_container_width=True
        ):

            with st.spinner(
                "Indexing document..."
            ):

                indexer = IndexingService()

                indexer.index_document(
                    str(save_path)
                )

            if uploaded_file.name not in st.session_state.indexed_documents:

                st.session_state.indexed_documents.append(
                    uploaded_file.name
                )

            st.sidebar.success(
                "✅ Indexing Completed Successfully!"
            )

    # -----------------------------
    # Clear Knowledge Base
    # -----------------------------

    st.sidebar.divider()

    if st.sidebar.button(
        "🗑 Clear Knowledge Base",
        use_container_width=True
    ):

        vector_store = VectorStoreFactory.get_vectorstore()

        vector_store.clear()

        st.session_state.chat_history.clear()

        st.session_state.indexed_documents.clear()

        st.sidebar.success(
            "Knowledge Base Cleared Successfully."
        )

        st.rerun()