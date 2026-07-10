from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "InvoiceAI Backend"
    APP_VERSION: str = "0.1.0"

    GEMINI_API_KEY: str
    SUPABASE_URL: str

    SUPABASE_SERVICE_ROLE_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()