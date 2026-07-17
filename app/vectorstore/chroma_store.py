from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config.settings import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
    TOP_K
)

from app.embeddings.embedding_factory import EmbeddingFactory
from app.vectorstore.base_vectorstore import BaseVectorStore
from app.utils.id_generator import generate_chunk_id
from app.utils.logger import logger


class ChromaStore(BaseVectorStore):
    """
    ChromaDB implementation of the vector store.
    """

    def __init__(self):
        self.embedding_model = EmbeddingFactory.get_embedding()

        self.db = Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=str(CHROMA_DB_DIR),
            embedding_function=self.embedding_model
        )

        logger.info("ChromaDB initialized successfully.")

    def add_documents(self, documents: list[Document]) -> None:
        """
        Index only new documents into ChromaDB using deterministic IDs.
        Prevents duplicate indexing.
        """
        if not documents:
            logger.warning("No documents found for indexing.")
            return

        logger.info(
            f"Preparing {len(documents)} chunks for indexing..."
        )

        # Generate Deterministic IDs
        ids = []

        for chunk_index, document in enumerate(documents):
            chunk_id = generate_chunk_id(
                document=document,
                chunk_index=chunk_index
            )
            ids.append(chunk_id)

        logger.info(
            f"Generated {len(ids)} deterministic chunk IDs."
        )

        # Fetch Existing IDs
        existing = self.db.get()
        existing_ids = set(existing.get("ids", []))

        logger.info(
            f"Found {len(existing_ids)} existing chunks in ChromaDB."
        )

        # Filter New Documents
        new_documents = []
        new_ids = []
        skipped = 0

        for document, chunk_id in zip(documents, ids):
            if chunk_id in existing_ids:
                skipped += 1
                continue

            new_documents.append(document)
            new_ids.append(chunk_id)

        # Nothing New
        if not new_documents:
            logger.info(
                "No new chunks found. ChromaDB is already up-to-date."
            )
            return

        # Add Only New Chunks
        self.db.add_documents(
            documents=new_documents,
            ids=new_ids
        )

        logger.info(
            f"Indexed {len(new_documents)} new chunks."
        )
        logger.info(
            f"Skipped {skipped} duplicate chunks."
        )

    def similarity_search(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:
        """
        Retrieve similar documents from ChromaDB.
        """
        if k is None:
            k = TOP_K

        logger.info(
            f"Searching top {k} documents for query: {query}"
        )

        results = self.db.similarity_search(
            query=query,
            k=k
        )

        logger.info(
            f"Retrieved {len(results)} relevant chunks."
        )

        return results

    def similarity_search_with_score(
        self,
        query: str,
        k: int | None = None
    ) -> list[tuple[Document, float]]:
        """
        Retrieve similar documents along with similarity scores.
        """
        if k is None:
            k = TOP_K

        logger.info(
            f"Searching top {k} documents with similarity scores for query: {query}"
        )

        results = self.db.similarity_search_with_score(
            query=query,
            k=k
        )

        logger.info(
            f"Retrieved {len(results)} scored documents."
        )

        return results
    
    def get_all_documents(self) -> list[Document]:
        """
        Return all indexed documents from ChromaDB.
        Used by BM25 Retriever.
        """
        logger.info(
            "Loading all indexed documents from ChromaDB..."
        )

        data = self.db.get(
            include=["documents", "metadatas"]
        )

        documents = []

        # If data is empty or missing expected keys, safely handle it
        docs_list = data.get("documents") or []
        metadatas_list = data.get("metadatas") or []

        for content, metadata in zip(docs_list, metadatas_list):
            documents.append(
                Document(
                    page_content=content,
                    metadata=metadata or {}
                )
            )

        logger.info(
            f"Loaded {len(documents)} documents from ChromaDB."
        )
        
        return documents
    
    def clear(self):
        logger.info(
        "Deleting all documents from ChromaDB..."
    )
        ids=self.db.get()["ids"]
        if ids:
            self.db.delete(ids=ids)
        
        logger.info(
            "Knowledge Base Clear"
        )