from langchain_core.documents import Document
from app.retriever.base_retriever import BaseRetriever
from app.retriever.vector_retriever import VectorRetriever
from app.retriever.bm25_retriever import BM25Retriever
from app.utils.logger import logger

class HybridRetriever(BaseRetriever):
  """
    Hybrid Retriever that combines
    Vector Search + BM25 Search.
    """
  def __init__(self):
    self.vector=VectorRetriever()
    self.bm25=BM25Retriever()
    logger.info(
            "Hybrid Retriever initialized successfully."
        )
    
  def retrieve(
        self,query:str,k:int | None=None
    )->list[Document]:
        logger.info(
            f"Running Hybrid Retrieval for query: {query}"
        )

        vector_docs = self.vector.retrieve(
            query=query,
            k=k
        )

        bm25_docs = self.bm25.retrieve(
            query=query,
            k=k
        )

        merged_docs = vector_docs + bm25_docs

        unique_docs = {}

        for doc in merged_docs:

            unique_docs[doc.page_content] = doc

        results = list(unique_docs.values())

        logger.info(
            f"Hybrid Retriever returned {len(results)} unique documents."
        )

        return results
  def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ):

        raise NotImplementedError(
            "Hybrid score fusion will be implemented later."
        )

