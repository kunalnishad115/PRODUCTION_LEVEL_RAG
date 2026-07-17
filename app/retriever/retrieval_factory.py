from app.config.settings import RETRIEVAL_TYPE

from app.retriever.vector_retriever import VectorRetriever
from app.retriever.bm25_retriever import BM25Retriever
from app.retriever.hybrid_retriever import HybridRetriever


class RetrievalFactory:

    @staticmethod
    def get_retriever():

        retrieval_type = RETRIEVAL_TYPE.lower()

        if retrieval_type == "vector":
            return VectorRetriever()

        elif retrieval_type == "bm25":
            return BM25Retriever()
        
        elif retrieval_type == "hybrid":
            return HybridRetriever()

        raise ValueError(
            f"Unsupported retrieval type : {RETRIEVAL_TYPE}"
        )