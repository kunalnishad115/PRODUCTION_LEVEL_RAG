from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.settings import (
    GEMINI_API_KEY,
    LLM_MODEL
)

from app.llm.base_llm import BaseLLM
from app.utils.logger import logger


class GeminiLLM(BaseLLM):
    """
    Gemini Chat Model Integration
    """

    def __init__(self):

        logger.info(
            f"Loading Gemini Model : {LLM_MODEL}"
        )

        self.llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL,
            google_api_key=GEMINI_API_KEY,
            temperature=0
        )

        logger.info(
            "Loaded Gemini Model Successfully."
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        logger.info(
            "Generating Response..."
        )

        try:

            response = self.llm.invoke(prompt)

            logger.info(
                "Response Generated Successfully."
            )

            content = response.content
            if isinstance(content, str):
                return content.strip()
            
            if isinstance(content, list):

                texts = []

                for block in content:

                    if isinstance(block, dict):

                        if block.get("type") == "text":
                            texts.append(
                                block.get("text", "")
                            )

                    elif hasattr(block, "text"):

                        texts.append(
                            block.text
                        )

                return "\n".join(texts).strip()

            return str(content)

        except Exception as e:

            logger.exception(
                f"Gemini Generation Failed : {e}"
            )

            return (
                "Sorry, I couldn't generate a response at the moment."
            )