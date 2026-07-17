from abc import ABC, abstractmethod
from langchain_core.documents import Document

class BaseReranker(ABC):
  """
    Base interface for all rerankers.
  """
  @abstractmethod
  def rerank(
    self,query:str,
    documents: list[Document],
    top_k: int | None=None
  )-> list[Document]:
    """
    Rerank retrieved documents.
    """
    pass
  