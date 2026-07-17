from app.llm.gemini_llm import GeminiLLM

class LLMFactory:
    _instance = None

    @staticmethod
    def get_llm():
        if LLMFactory._instance is None:
            LLMFactory._instance = GeminiLLM()
        return LLMFactory._instance