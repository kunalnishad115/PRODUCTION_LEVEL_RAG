from pathlib import Path

import streamlit as st

from app.services.rag_service import RAGService


def render_chat():

    st.subheader("💬 Chat with your Documents")
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if not st.session_state.indexed_documents:
        st.info(
            "Please upload and index a document first."
        )
        return


    question = st.chat_input(
        "Ask anything about your documents..."
    )
    if not question:
        return
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            rag = RAGService()
            response = rag.ask(question)
            answer = response["answer"]
            citations = response["citations"]

            st.markdown(answer)
            if citations:
                st.markdown("---")
                st.markdown("### 📚 Sources")
                for citation in citations:
                    source = Path(
                        citation["source"]
                    ).name

                    page = citation.get(
                        "page",
                        0
                    )

                    with st.container():
                        st.markdown(
                            f"""
**📄 {source}**
📑 **Page:** {page + 1}
"""
                        )
                        st.divider()
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )