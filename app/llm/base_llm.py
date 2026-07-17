from abc import ABC,abstractmethod


class BaseLLM(ABC):
  """
    Base interface for all LLM providers.
  """
  @abstractmethod
  def generate(self,prompt:str)->str:
    pass