from langchain_community.document_loaders import TextLoader
from app.loaders.base_loader import BaseLoader
from app.utils.logger import logger

class TXTLoader(BaseLoader):
  def load(self, file_path: str):
    try:
      logger.info(f"Loading Txt File {file_path}")
      loader=TextLoader(file_path)
      documents=loader.load()
      logger.info(
        "Txt Load Done"
      )
      return documents
    
    except Exception as e:
      logger.exception(e)
      raise

    
    