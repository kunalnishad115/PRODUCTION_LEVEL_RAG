from abc import ABC,abstractmethod
from langchain_core.embeddings import Embeddings

class BaseEmbedding(Embeddings,ABC):
  """
    Base interface for all embedding providers.
    """
  
  @abstractmethod
  def embed_documents(self, texts: list[str]) -> list[list[float]]:
        pass

  @abstractmethod
  def embed_query(self, text: str) -> list[float]:
        pass