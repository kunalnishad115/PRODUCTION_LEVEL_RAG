from langchain_core.documents import Document

from app.utils.logger import logger


class ContextBuilder:
    """
    Builds LLM-ready context from retrieved documents.
    """

    @staticmethod
    def build(
        documents: list[Document]
    ) -> str:

        if not documents:

            logger.warning(
                "No documents found while building context."
            )

            return ""

        logger.info(
            f"Building context using {len(documents)} documents."
        )

        context_parts = []

        for index, document in enumerate(documents, start=1):

            source = document.metadata.get(
                "source",
                "Unknown Source"
            )

            page = document.metadata.get(
                "page",
                "Unknown"
            )

            chunk = f"""
==============================
Document {index}

Source : {source}

Page : {page}

Content:
{document.page_content}
"""

            context_parts.append(chunk)

        context = "\n".join(context_parts)

        logger.info(
            "Context built successfully."
        )

        return context