from app.retriever.retrieval_factory import RetrievalFactory
from app.reranker.reranker_factory import RerankerFactory
from app.services.context_builder import ContextBuilder
from app.prompts.rag_prompt import RAG_PROMPT
from app.llm.llm_factory import LLMFactory
from app.services.citation_service import CitationService
from app.utils.logger import logger


class RAGService:
    """
    Complete RAG Pipeline.
    """

    def __init__(self):
        self.retriever = RetrievalFactory.get_retriever()
        self.reranker = RerankerFactory.get_reranker()
        self.llm = LLMFactory.get_llm()

    def ask(self, question: str) -> str:
        logger.info(
            f"Question : {question}"
        )

        # Step 1 : Retrieve
        retrieved_docs = self.retriever.retrieve(
            question
        )

        # Step 2 : Rerank
        reranked_docs = self.reranker.rerank(
            query=question,
            documents=retrieved_docs
        )

        # Step 3 : Build Context
        context = ContextBuilder.build(
            reranked_docs
        )

        # Step 4 : Build Prompt
        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        # Step 5 : Generate Answer
        answer = self.llm.generate(
            prompt
        )
        
        logger.info(
            "Answer generated successfully."
        )
        
        # step 6 : Build Citations
        citations = CitationService.build(reranked_docs)
        
        return {
    "answer": answer,
    "citations": citations
      }