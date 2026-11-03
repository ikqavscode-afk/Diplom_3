import os
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://qa-stellarburgers.education-services.ru")
    timeout: int = int(os.getenv("TIMEOUT", "10"))
    allure_dir: Path = BASE_DIR / "allure-results"


settings = Settings()
