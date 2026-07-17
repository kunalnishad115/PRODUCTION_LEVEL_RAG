from abc import ABC,abstractmethod
from langchain_core.documents import Document

class BaseRetriever(ABC):
    """
    Base interface for all retrievers.
    """
    @abstractmethod
    def retrieve(self,query:str)-> list[Document]:
        """
        Retrieve relevant documents.
        """
        pass
    
    @abstractmethod
    def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ) -> list[tuple[Document, float]]:
        pass
    
