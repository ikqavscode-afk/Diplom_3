import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv(
        "BASE_URL", "https://qa-stellarburgers.education-services.ru"
    )
    timeout: int = int(os.getenv("TIMEOUT", "10"))


settings = Settings()
