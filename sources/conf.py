from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    builds_path: Path = "builds/builds.yaml"
    tasks_path: Path = "builds/tasks.yaml"


settings = Settings()
