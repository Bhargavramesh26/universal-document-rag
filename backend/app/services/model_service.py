from app.schemas.model import ModelInfo


class ModelService:

    @staticmethod
    def get_available_models() -> list[ModelInfo]:

        return [
            ModelInfo(
                id="ollama",
                name="Ollama",
                status="available"
            ),
            ModelInfo(
                id="gemini",
                name="Google Gemini",
                status="available"
            ),
            ModelInfo(
                id="groq",
                name="Groq",
                status="available"
            )
        ]