from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    API_PREFIX: str

    HOST: str
    PORT: int

    DEBUG: bool

    ALLOWED_ORIGINS: str

    # ==========================
    # Ollama
    # ==========================
    OLLAMA_MODEL: str

    # ==========================
    # Gemini
    # ==========================
    GEMINI_MODEL: str
    GEMINI_API_KEY: str

    # ==========================
    # Groq
    # ==========================
    GROQ_MODEL: str
    GROQ_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()