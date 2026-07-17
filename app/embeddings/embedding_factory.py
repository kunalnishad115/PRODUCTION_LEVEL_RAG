from app.config.settings import EMBEDDING_PROVIDER

from app.embeddings.cohere_embedding import CohereEmbedding


class EmbeddingFactory:
    @staticmethod
    def get_embedding():

        if EMBEDDING_PROVIDER.lower() == "cohere":
            return CohereEmbedding()

        raise ValueError(
            f"Unsupported Embedding Provider : {EMBEDDING_PROVIDER}"
        )