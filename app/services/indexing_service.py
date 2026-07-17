from app.loaders.loader_factory import LoaderFactory
from app.chunking.text_splitter import TextChunker
from app.vectorstore.vectorstore_factory import (
    VectorStoreFactory
)
from app.utils.logger import logger


class IndexingService:
    """
    Handles complete document indexing pipeline.
    """

    def __init__(self):

        self.chunker = TextChunker()

        self.vector_store = (
            VectorStoreFactory.get_vectorstore()
        )

    def index_document(
        self,
        file_path: str
    ) -> None:

        logger.info(
            f"Indexing document : {file_path}"
        )

        # Step 1 : Load Document
        loader = LoaderFactory.get_loader(file_path)

        documents = loader.load(file_path)

        logger.info(
            f"Loaded {len(documents)} pages."
        )

        # Step 2 : Split into Chunks
        chunks = self.chunker.split_documents(
            documents
        )

        logger.info(
            f"Generated {len(chunks)} chunks."
        )

        # Step 3 : Index into ChromaDB
        self.vector_store.add_documents(
            chunks
        )

        logger.info(
            "Saved chunks into ChromaDB."
        )

        logger.info(
            "Indexing completed successfully."
        )