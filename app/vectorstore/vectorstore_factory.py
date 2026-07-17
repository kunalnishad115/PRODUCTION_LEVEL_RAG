from app.config.settings import VECTOR_DB

from app.vectorstore.chroma_store import ChromaStore


class VectorStoreFactory:
    """
    Factory class for vector databases.
    """

    @staticmethod
    def get_vectorstore():

        if VECTOR_DB.lower() == "chroma":
            return ChromaStore()

        raise ValueError(
            f"Unsupported Vector Database : {VECTOR_DB}"
        )