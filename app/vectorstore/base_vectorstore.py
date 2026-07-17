from abc import ABC, abstractmethod
from langchain_core.documents import Document


class BaseVectorStore(ABC):
    """
    Abstract base class for all vector database implementations.
    """

    @abstractmethod
    def add_documents(
        self,
        documents: list[Document]
    ) -> None:
        """
        Store documents in the vector database.
        """
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:
        """
        Retrieve similar documents.
        """
        pass

    @abstractmethod
    def similarity_search_with_score(
        self,
        query: str,
        k: int | None = None
    ) -> list[tuple[Document, float]]:
        """
        Retrieve documents with similarity score.
        """
        pass

    # ==============================
    # NEW
    # ==============================

    @abstractmethod
    def get_all_documents(
        self
    ) -> list[Document]:
        """
        Return all indexed documents.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Delete all indexed documents.
        """
        pass
       
      