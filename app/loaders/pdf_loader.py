from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from app.utils.logger import logger
from app.loaders.base_loader import BaseLoader

class PDFLoader(BaseLoader):
  def load(self,file_path: str):
    try:
      logger.info(f"loading file: {file_path}")
      loader=PyPDFLoader(file_path)
      documents=loader.load()
      logger.info(
        f"Loaded {len(documents)} pages successfully."
      )
      return documents
    except Exception as e:
      logger.exceptio(e)

      raise e
