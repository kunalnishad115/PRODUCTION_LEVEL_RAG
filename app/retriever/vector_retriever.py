from langchain_core.documents import Document

from app.vectorstore.vectorstore_factory import (
    VectorStoreFactory
)

from app.retriever.base_retriever import BaseRetriever
from app.utils.logger import logger


class VectorRetriever(BaseRetriever):
    """
    Vector Retriever using ChromaDB.
    """

    def __init__(self):

        self.vectorstore = VectorStoreFactory.get_vectorstore()

    def retrieve(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:
        """
        Retrieve relevant documents using vector similarity search.
        """

        logger.info(
            f"Retrieving documents for query: {query}"
        )

        documents = self.vectorstore.similarity_search(
            query=query,
            k=k
        )

        logger.info(
            f"Retrieved {len(documents)} documents."
        )

        return documents

    def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ) -> list[tuple[Document, float]]:
        """
        Retrieve relevant documents along with similarity scores.
        """

        logger.info(
            f"Retrieving scored documents for query: {query}"
        )

        results = self.vectorstore.similarity_search_with_score(
            query=query,
            k=k
        )

        logger.info(
            f"Retrieved {len(results)} scored documents."
        )

        return results