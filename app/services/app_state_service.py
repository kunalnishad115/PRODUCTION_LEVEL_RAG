from app.vectorstore.vectorstore_factory import VectorStoreFactory


class AppStateService:
    """
    Handles application startup state.
    """

    @staticmethod
    def has_indexed_documents() -> bool:

        vectorstore = VectorStoreFactory.get_vectorstore()

        collection = vectorstore.db.get()

        return len(collection["ids"]) > 0