from langchain_community.document_loaders import Docx2txtLoader
from app.loaders.base_loader import BaseLoader
from app.utils.logger import logger

class DOCXLoader(BaseLoader):
  def load(self, file_path: str):
    try:
      logger.info(f"Loading Doc File {file_path}")
      loader=Docx2txtLoader(file_path)
      documents=loader.load()
      logger.info(
        f"Lodded Done Docx"
      )
      return documents
    except Exception as e:
      logger.exception(e)
      raise


    