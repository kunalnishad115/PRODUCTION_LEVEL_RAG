from langchain_core.documents import Document

from app.utils.logger import logger


class CitationService:
    """
    Generates citations from retrieved documents.
    """

    @staticmethod
    def build(
        documents: list[Document]
    ) -> list[dict]:

        citations = []

        seen = set()

        for document in documents:

            source = document.metadata.get(
                "source",
                "Unknown"
            )

            page = document.metadata.get(
                "page",
                "Unknown"
            )

            key = (source, page)

            if key in seen:
                continue

            seen.add(key)

            citations.append(
                {
                    "source": source,
                    "page": page
                }
            )

        logger.info(
            f"Generated {len(citations)} citations."
        )

        return citations