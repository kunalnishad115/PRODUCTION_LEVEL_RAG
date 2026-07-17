from abc import ABC, abstractmethod
class BaseLoader(ABC):
  @abstractmethod
  def load(self,file_path: str):
    """
    Load the document and return LangChain Documents.
    """
    pass