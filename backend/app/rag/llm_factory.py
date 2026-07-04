from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from app.core.config import settings


class LLMFactory:

    @staticmethod
    def get_llm(model_provider: str):

        provider = model_provider.lower()

        if provider == "ollama":

            return ChatOllama(
                model=settings.OLLAMA_MODEL,
                temperature=0
            )

        elif provider == "gemini":

            return ChatGoogleGenerativeAI(
                model=settings.GEMINI_MODEL,
                google_api_key=settings.GEMINI_API_KEY,
                temperature=0
            )

        elif provider == "groq":

            return ChatGroq(
                model=settings.GROQ_MODEL,
                api_key=settings.GROQ_API_KEY,
                temperature=0
            )

        raise ValueError(
            f"Unsupported model provider: {model_provider}"
        )