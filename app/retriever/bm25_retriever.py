from langchain_core.documents import Document

from langchain_community.retrievers import (
    BM25Retriever as LangChainBM25Retriever
)

from app.vectorstore.vectorstore_factory import (
    VectorStoreFactory
)

from app.retriever.base_retriever import BaseRetriever
from app.config.settings import TOP_K
from app.utils.logger import logger


class BM25Retriever(BaseRetriever):
    """
    BM25 keyword based retriever.
    """

    def __init__(self):

        self.vectorstore = (
            VectorStoreFactory.get_vectorstore()
        )

        documents = (
            self.vectorstore.get_all_documents()
        )

        if not documents:

            logger.warning(
                "No indexed documents found in ChromaDB."
            )

            self.retriever = None

            return

        self.retriever = (
            LangChainBM25Retriever.from_documents(
                documents
            )
        )

        self.retriever.k = TOP_K

        logger.info(
            f"BM25 initialized with {len(documents)} documents."
        )

    def retrieve(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:

        if self.retriever is None:
            return []

        if k is not None:
            self.retriever.k = k

        logger.info(
            f"BM25 retrieving documents for : {query}"
        )

        results = self.retriever.invoke(query)

        logger.info(
            f"BM25 retrieved {len(results)} documents."
        )

        return results

    def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ):

        raise NotImplementedError(
            "BM25 scores will be added during Hybrid Retrieval."
        )