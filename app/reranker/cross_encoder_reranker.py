from langchain_core.documents import Document

from app.reranker.base_reranker import BaseReranker
from app.config.settings import (
    RERANK_TOP_K,
    RERANKER_MODEL
)
from app.utils.logger import logger


class CrossEncoderReranker(BaseReranker):

    def __init__(self):

        self.model = None

    def _load_model(self):

        if self.model is None:

            logger.info(
                f"Loading Cross Encoder : {RERANKER_MODEL}"
            )

            from sentence_transformers import CrossEncoder

            self.model = CrossEncoder(
                RERANKER_MODEL
            )

            logger.info(
                "Cross Encoder loaded successfully."
            )

    def rerank(
        self,
        query: str,
        documents: list[Document],
        top_k: int | None = None
    ) -> list[Document]:

        if not documents:
            return []

        self._load_model()

        if top_k is None:
            top_k = RERANK_TOP_K

        logger.info(
            f"Reranking {len(documents)} documents..."
        )

        pairs = [
            (query, doc.page_content)
            for doc in documents
        ]

        scores = self.model.predict(
            pairs
        )

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        reranked_docs = [
            doc
            for doc, score in ranked[:top_k]
        ]

        logger.info(
            f"Returned Top {len(reranked_docs)} reranked documents."
        )

        return reranked_docs