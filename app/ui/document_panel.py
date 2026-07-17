import streamlit as st


def render_document_panel():

    st.subheader("📚 Indexed Documents")

    documents = st.session_state.get(
        "indexed_documents",
        []
    )

    if not documents:

        st.info(
            "No documents indexed yet."
        )

        return

    for document in documents:

        st.success(
            f"✅ {document}"
        )