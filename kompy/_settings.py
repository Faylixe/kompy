from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings


class KompySettings(BaseSettings):
    database: Path

    class Config:
        env_prefix = "KOMPY"

    @lru_cache(maxsize=1)
    def to_database_uri(self) -> str:
        return f"sqlite://{self.database}"
