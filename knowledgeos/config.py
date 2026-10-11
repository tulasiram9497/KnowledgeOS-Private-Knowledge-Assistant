from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="KNOWLEDGEOS_",
        case_sensitive=False,
        env_file=".env",
        extra="ignore",
    )

    app_name: str = "KnowledgeOS"
    api_version: str = "v1"
    environment: str = Field(default="local")
    database_url: str = "sqlite:///./knowledgeos.db"
    log_level: str = "INFO"
    max_upload_size_mb: int = 20
    allowed_file_extensions: list[str] = ["pdf", "txt", "md", "markdown"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
