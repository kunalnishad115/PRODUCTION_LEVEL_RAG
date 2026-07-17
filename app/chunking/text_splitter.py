from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.settings import CHUNK_SIZE,CHUNK_OVERLAP

class TextChunker:
  def __init__(self):
    self.splitter=RecursiveCharacterTextSplitter(
      chunk_size=CHUNK_SIZE,
      chunk_overlap=CHUNK_OVERLAP,
      length_function=len,
      separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
    )

  def split_documents(self,documents):
    """
    Chunking Process ...  
    """
    return self.splitter.split_documents(documents)

