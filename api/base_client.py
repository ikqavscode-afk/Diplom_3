import allure
import requests

from config.settings import settings


class BaseClient:
    def __init__(self) -> None:
        self.session = requests.Session()

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{settings.base_url}{path}"
        with allure.step(f"{method} {path}"):
            return self.session.request(method, url, timeout=settings.timeout, **kwargs)
