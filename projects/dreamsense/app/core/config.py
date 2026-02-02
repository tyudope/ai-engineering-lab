from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Where to read env vars from
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding= "utf-8",
        extra = "forbid"
    )
    # openai
    openai_api_key: str
    openai_model: str = "gpt-4.1-mini"


settings = Settings()