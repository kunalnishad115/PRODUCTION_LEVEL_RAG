from langchain_cohere import CohereEmbeddings
from app.config.settings import COHERE_API_KEY,EMBEDDING_MODEL

from app.embeddings.base_embedding import BaseEmbedding

class CohereEmbedding(BaseEmbedding):
    """
    Cohere Embedding Provider
    """
    def __init__(self):
        self.embedding=CohereEmbeddings(
            model=EMBEDDING_MODEL,
            cohere_api_key=COHERE_API_KEY

        )
      
    def embed_documents(self,texts):
        return self.embedding.embed_documents(texts)
    def embed_query(self, text):
        return self.embedding.embed_query(text)
    
