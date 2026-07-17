from pathlib import Path

from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DOCXLoader
from app.loaders.txt_loader import TXTLoader

class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):
        extension = Path(file_path).suffix.lower()
        if extension == ".pdf":
            return PDFLoader()
        elif extension == ".docx":
            return DOCXLoader()
        elif extension == ".txt":
            return TXTLoader()
        else:
            raise ValueError(
                f"Unsupported File Type : {extension}"
            )
  
